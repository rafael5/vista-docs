#!/usr/bin/env python3
"""
One-off script: fetch, ingest, and enrich the VistA Monograph.

The Monograph has app_code='' in the source CSV so it cannot be reached
via --pkg MON in the normal pipeline commands.  This script bypasses the
manifest filter and drives the same underlying functions directly.

Run from the vista-docs project root:
    python ingest_monograph.py
"""

from __future__ import annotations

import logging
import sys
from dataclasses import replace
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(__name__)

DOCX_URL = "https://www.va.gov/vdl/documents/Monograph/Monograph/vista_monograph_0723_r.docx"
PDF_URL  = "https://www.va.gov/vdl/documents/Monograph/Monograph/vista_monograph_0723_r.pdf"
APP_CODE = "MON"
DOC_TITLE = "Vista Monograph July 2023"

RAW_DIR      = Path.home() / "data/vista-docs/raw/MON"
MARKDOWN_DIR = Path.home() / "data/vista-docs/markdown"


# ---------------------------------------------------------------------------
# Step 1 — Fetch
# ---------------------------------------------------------------------------

def fetch() -> Path:
    from vista_docs.crawl.session import make_session

    dest = RAW_DIR / "vista_monograph_0723_r.docx"
    if dest.exists():
        log.info("Already fetched: %s", dest)
        return dest

    log.info("Downloading %s", DOCX_URL)
    session = make_session()
    resp = session.get(DOCX_URL, stream=True, timeout=60)
    resp.raise_for_status()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=65536):
            f.write(chunk)
    log.info("Saved %s (%.1f MB)", dest, dest.stat().st_size / 1_048_576)
    return dest


# ---------------------------------------------------------------------------
# Step 2 — Ingest
# ---------------------------------------------------------------------------

def ingest(docx_path: Path) -> Path:
    from vista_docs.classify.rules import classify
    from vista_docs.ingest.converter import convert_to_markdown
    from vista_docs.ingest.prepare import build_markdown
    from vista_docs.models.manifest import FetchStatus, ManifestEntry

    out_dir = MARKDOWN_DIR / APP_CODE
    out_dir.mkdir(parents=True, exist_ok=True)

    # Slugify title the same way the pipeline does
    import re
    slug = re.sub(r"[^a-z0-9]+", "-", DOC_TITLE.lower()).strip("-")[:80]
    out_path = out_dir / f"{slug}.md"

    if out_path.exists():
        log.info("Already ingested: %s", out_path)
        return out_path

    log.info("Converting %s via Docling (this may take a while)…", docx_path.name)
    raw_md = convert_to_markdown(docx_path)
    log.info("Converted: %d chars", len(raw_md))

    entry = ManifestEntry(
        package_id="",
        app_code=APP_CODE,
        doc_title=DOC_TITLE,
        doc_type=classify(docx_path.name, DOC_TITLE),
        patch="",
        docx_url=DOCX_URL,
        pdf_url=PDF_URL,
        output_filename=out_path.name,
        fetch_status=FetchStatus.OK,
        local_path=str(docx_path),
        fetched_ext=".docx",
    )

    md_content = build_markdown(entry, raw_md)
    out_path.write_text(md_content, encoding="utf-8")
    log.info("Wrote %s", out_path)
    return out_path


# ---------------------------------------------------------------------------
# Step 3 — Enrich
# ---------------------------------------------------------------------------

def enrich(md_path: Path) -> None:
    from vista_docs.enrich.runner import enrich_file

    log.info("Enriching %s", md_path.name)
    ok = enrich_file(md_path)
    if not ok:
        log.error("Enrich failed")
        sys.exit(1)
    log.info("Enrich done")


# ---------------------------------------------------------------------------
# Step 4 — Sync inventory fields
# ---------------------------------------------------------------------------

def sync(md_path: Path) -> None:
    import csv
    from vista_docs.enrich.frontmatter import parse_frontmatter, rebuild_frontmatter
    from vista_docs.enrich.inventory_fields import build_inventory_index, fields_for_doc

    enriched_csv = Path.home() / "data/vista-docs/inventory/vdl_inventory_enriched.csv"
    with open(enriched_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    index = build_inventory_index(rows)

    text = md_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    new_fields = fields_for_doc(index, fm.get("app_code", ""), fm.get("title", ""))

    if new_fields is None:
        log.warning("No inventory match — frontmatter will not have inventory fields")
        return

    updated = rebuild_frontmatter(text, new_fields)
    md_path.write_text(updated, encoding="utf-8")
    log.info("Sync done")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    docx_path = fetch()
    md_path   = ingest(docx_path)
    enrich(md_path)
    sync(md_path)
    log.info("=== Done: %s ===", md_path)
