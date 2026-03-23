"""
I/O thin layer: walk markdown corpus and enrich each file's frontmatter.

enrich_entry(path, entry) → updated markdown written in-place
enrich_corpus(markdown_dir, entries, force) → summary dict
"""

from __future__ import annotations

import logging
from pathlib import Path

from vista_docs.enrich.extractors import (
    extract_appendices,
    extract_audience,
    extract_figure_count,
    extract_keywords,
    extract_package_name,
    extract_package_namespace,
    extract_package_version,
    extract_page_count,
    extract_pub_date,
    extract_revision_history,
    extract_section_count,
    extract_table_count,
)
from vista_docs.enrich.frontmatter import rewrite_frontmatter
from vista_docs.models.manifest import FetchStatus, ManifestEntry

logger = logging.getLogger(__name__)


def enrich_file(path: Path) -> bool:
    """
    Read a markdown file, extract metadata, rewrite frontmatter in-place.

    Returns True on success, False on error.
    """
    try:
        md = path.read_text(encoding="utf-8")

        rev = extract_revision_history(md)
        new_fields = {
            "pub_date": extract_pub_date(md),
            "page_count": extract_page_count(md),
            "revision_count": rev["count"],
            "revision_oldest": rev["oldest"],
            "revision_newest": rev["newest"],
            "appendix_count": extract_appendices(md),
            "table_count": extract_table_count(md),
            "section_count": extract_section_count(md),
            "figure_count": extract_figure_count(md),
            "keywords": extract_keywords(md),
            "package_name": extract_package_name(md),
            "package_namespace": extract_package_namespace(md),
            "package_version": extract_package_version(md),
            "audience": extract_audience(md),
        }

        updated = rewrite_frontmatter(md, new_fields)
        path.write_text(updated, encoding="utf-8")
        logger.info("Enriched %s", path.name)
        return True

    except Exception as exc:
        logger.error("Failed to enrich %s: %s", path, exc)
        return False


def enrich_corpus(
    markdown_dir: Path,
    entries: list[ManifestEntry],
    force: bool = False,
) -> dict:
    """
    Enrich all ingested markdown files in markdown_dir.

    Skips entries without a markdown_path or with ingest_status != OK.
    Returns {"ok": N, "skipped": N, "errors": N}.
    """
    ok = skipped = errors = 0

    for entry in entries:
        if entry.ingest_status != FetchStatus.OK or not entry.markdown_path:
            skipped += 1
            continue

        path = Path(entry.markdown_path)
        if not path.exists():
            logger.warning("Markdown file missing: %s", path)
            skipped += 1
            continue

        if enrich_file(path):
            ok += 1
        else:
            errors += 1

    return {"ok": ok, "skipped": skipped, "errors": errors}
