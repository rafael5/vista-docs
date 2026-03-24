"""
I/O thin layer: sync enriched inventory fields into markdown frontmatter.

sync_inventory_corpus(markdown_dir, enriched_csv, pkg, force) → summary dict
"""

from __future__ import annotations

import csv
import logging
from pathlib import Path

from vista_docs.enrich.frontmatter import parse_frontmatter, rebuild_frontmatter
from vista_docs.enrich.inventory_fields import build_inventory_index, fields_for_doc

logger = logging.getLogger(__name__)


def sync_inventory_corpus(
    markdown_dir: Path,
    enriched_csv: Path,
    pkg: str = "",
    force: bool = False,
) -> dict:
    """
    Merge enriched inventory fields into every markdown file's frontmatter.

    Walks markdown_dir (optionally limited to one pkg subfolder).
    Looks up each file's (app_code, title) in the enriched CSV index.
    Rewrites frontmatter in-place with inventory fields added/updated.

    Returns {"ok": N, "skipped": N, "no_match": N, "errors": N}.
    """
    with open(enriched_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    index = build_inventory_index(rows)

    search_root = markdown_dir / pkg.upper() if pkg else markdown_dir
    md_files = sorted(search_root.rglob("*.md"))

    ok = skipped = no_match = errors = 0

    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)

            if not fm:
                logger.warning("No frontmatter: %s", path.name)
                skipped += 1
                continue

            # Check if already synced (has 'section' key) — skip unless force
            if not force and "section" in fm:
                skipped += 1
                continue

            app_code = fm.get("app_code", "")
            title = fm.get("title", "")
            if not app_code or not title:
                logger.warning("Missing app_code or title in frontmatter: %s", path.name)
                skipped += 1
                continue

            new_fields = fields_for_doc(index, app_code, title)
            if new_fields is None:
                logger.debug("No inventory match for %s / %s", app_code, title)
                no_match += 1
                continue

            updated = rebuild_frontmatter(text, new_fields)
            path.write_text(updated, encoding="utf-8")
            logger.info("Synced %s", path.name)
            ok += 1

        except Exception as exc:
            logger.error("Failed to sync %s: %s", path, exc)
            errors += 1

    return {"ok": ok, "skipped": skipped, "no_match": no_match, "errors": errors}
