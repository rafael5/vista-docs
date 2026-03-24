#!/usr/bin/env python3
"""
One-off script: fetch, ingest, enrich, and sync packages whose app_code is blank
in vdl_inventory.csv.  Assigns synthetic app_codes so the pipeline functions work.

Usage (from ~/vista-docs/):
    python ingest_blank_appcode.py

Currently handles:
    LR  — Laboratory (LA and LR)
    HL7 — HL7 (VistA Messaging)
"""

from __future__ import annotations

import csv
import logging
import sys
import time
from dataclasses import replace
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

INVENTORY_CSV = Path.home() / "data/vista-docs/inventory/vdl_inventory.csv"
ENRICHED_CSV  = Path.home() / "data/vista-docs/inventory/vdl_inventory_enriched.csv"
RAW_DIR       = Path.home() / "data/vista-docs/raw"
MARKDOWN_DIR  = Path.home() / "data/vista-docs/markdown"
DB_PATH       = Path.home() / "data/vista-docs/state/pipeline.db"

# Map: app_name (as it appears in the CSV) → synthetic app_code to assign
APP_NAME_TO_CODE: dict[str, str] = {
    "Laboratory (LA and LR)": "LR",
    "HL7 (VistA Messaging)":  "HL7",
}


def load_patched_rows() -> list[dict]:
    """Read the plain inventory, patch app_code for blank-code packages, return relevant rows."""
    with open(INVENTORY_CSV, newline="", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    patched = []
    for row in all_rows:
        synthetic = APP_NAME_TO_CODE.get(row.get("app_name", ""))
        if synthetic:
            row = dict(row)
            row["app_code"] = synthetic
            row["app_status"] = row.get("app_status") or "active"
            patched.append(row)

    log.info("Loaded %d rows for LR+HL7 (after patching app_code)", len(patched))
    return patched


def run_fetch(entries: list) -> list:
    """Download each entry. Returns updated entries with fetch status."""
    from vista_docs.crawl.session import make_session
    from vista_docs.fetch.downloader import download_entry
    from vista_docs.manifest.store import open_db, upsert
    from vista_docs.models.manifest import FetchStatus

    session = make_session()
    db = open_db(DB_PATH)
    updated = []

    for i, entry in enumerate(entries, 1):
        dest_dir = RAW_DIR / entry.app_code
        dest_dir.mkdir(parents=True, exist_ok=True)

        log.info("[%d/%d] fetch %s — %s", i, len(entries), entry.app_code, entry.doc_title[:60])
        result = download_entry(entry, session)
        upsert(db, result)
        if result.fetch_status == FetchStatus.OK:
            log.info("  ok %s %dKB", result.fetched_ext, result.fetch_size // 1024)
        else:
            log.warning("  FAIL %s", result.fetch_error[:80])
        updated.append(result)
        if i < len(entries):
            time.sleep(1.0)

    db.close()
    return updated


def run_ingest(entries: list, force: bool = False) -> list:
    """Convert fetched DOCX/PDF → markdown. Returns updated entries."""
    from vista_docs.ingest.runner import ingest_entry
    from vista_docs.manifest.store import open_db, upsert
    from vista_docs.models.manifest import FetchStatus

    db = open_db(DB_PATH)
    to_ingest = [e for e in entries if e.fetch_status == FetchStatus.OK]
    log.info("Ingesting %d/%d fetched entries", len(to_ingest), len(entries))

    updated = []
    for i, entry in enumerate(to_ingest, 1):
        log.info("[%d/%d] ingest %s — %s", i, len(to_ingest), entry.app_code, entry.doc_title[:60])
        result = ingest_entry(entry, MARKDOWN_DIR, scaffold=False, force=force)
        upsert(db, result)
        if result.ingest_status == FetchStatus.OK:
            log.info("  ok → %s", result.markdown_path)
        elif result.ingest_status == FetchStatus.SKIPPED:
            log.info("  skipped (already exists)")
        else:
            log.warning("  FAIL %s", result.ingest_error[:80])
        updated.append(result)

    db.close()
    return updated


def run_enrich(entries: list) -> None:
    """Enrich all successfully ingested markdown files."""
    from vista_docs.enrich.runner import enrich_corpus
    from vista_docs.models.manifest import FetchStatus

    to_enrich = [e for e in entries if e.ingest_status == FetchStatus.OK]
    log.info("Enriching %d entries", len(to_enrich))
    result = enrich_corpus(MARKDOWN_DIR, to_enrich, force=True)
    log.info("Enrich done: %d ok, %d skipped, %d errors", result["ok"], result["skipped"], result["errors"])


def run_sync(pkg: str) -> None:
    """Sync enriched inventory fields into frontmatter for a package folder."""
    from vista_docs.enrich.sync import sync_inventory_corpus

    log.info("Syncing inventory fields for %s", pkg)
    result = sync_inventory_corpus(MARKDOWN_DIR, ENRICHED_CSV, pkg=pkg, force=True)
    log.info(
        "Sync done: %d synced, %d skipped, %d no_match, %d errors",
        result["ok"], result["skipped"], result["no_match"], result["errors"],
    )


def main() -> None:
    from vista_docs.manifest.builder import build_entries_from_rows
    from vista_docs.manifest.store import load_all, open_db
    from vista_docs.models.manifest import FetchStatus

    patched_rows = load_patched_rows()
    all_entries = build_entries_from_rows(patched_rows)
    log.info("Built %d ManifestEntry objects", len(all_entries))

    # Skip entries already in DB with fetch_status=OK to allow re-runs
    db = open_db(DB_PATH)
    existing = {(e.app_code, e.doc_title): e for e in load_all(db)}
    db.close()

    to_fetch = [
        e for e in all_entries
        if existing.get((e.app_code, e.doc_title), None) is None
        or existing[(e.app_code, e.doc_title)].fetch_status != FetchStatus.OK
    ]
    already_ok = [
        existing[(e.app_code, e.doc_title)]
        for e in all_entries
        if (e.app_code, e.doc_title) in existing
        and existing[(e.app_code, e.doc_title)].fetch_status == FetchStatus.OK
    ]

    log.info("%d to fetch, %d already fetched", len(to_fetch), len(already_ok))

    fetched = run_fetch(to_fetch) if to_fetch else []
    all_fetched = already_ok + fetched

    ingested = run_ingest(all_fetched)

    # Reload from DB to get accurate ingest_status for entries that were already ingested
    db = open_db(DB_PATH)
    all_in_db = {(e.app_code, e.doc_title): e for e in load_all(db)}
    db.close()
    all_entries_db = [
        all_in_db[(e.app_code, e.doc_title)]
        for e in all_entries
        if (e.app_code, e.doc_title) in all_in_db
    ]

    run_enrich(all_entries_db)

    for pkg in ("LR", "HL7"):
        run_sync(pkg)

    log.info("=== Done: LR + HL7 fully processed ===")


if __name__ == "__main__":
    main()
