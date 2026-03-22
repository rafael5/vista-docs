"""
I/O thin layer: orchestrate one document through the ingest stage.

ingest_entry(entry, markdown_dir, scaffold, force) → ManifestEntry
"""

from __future__ import annotations

import logging
from dataclasses import replace
from pathlib import Path

from vista_docs.ingest.prepare import build_markdown
from vista_docs.models.manifest import FetchStatus, ManifestEntry

logger = logging.getLogger(__name__)


def ingest_entry(
    entry: ManifestEntry,
    markdown_dir: Path,
    scaffold: bool = False,
    force: bool = False,
) -> ManifestEntry:
    """
    Ingest one document: convert (or scaffold) → postprocess → write markdown.

    Returns an updated ManifestEntry with ingest_status, markdown_path, or
    ingest_error populated.

    Skips entries whose fetch_status is not OK.
    Skips entries already ingested unless force=True.
    """
    # Skip unfetched docs
    if entry.fetch_status != FetchStatus.OK:
        logger.debug("Skipping %s — fetch_status=%s", entry.doc_title, entry.fetch_status)
        return replace(entry, ingest_status=FetchStatus.SKIPPED)

    # Output path
    out_dir = markdown_dir / entry.app_code
    out_path = out_dir / entry.output_filename

    # Skip if already ingested and not forcing
    if not force and entry.ingest_status == FetchStatus.OK and out_path.exists():
        logger.debug("Already ingested: %s", out_path)
        return replace(entry, markdown_path=str(out_path))

    # Validate source file exists
    src = Path(entry.local_path)
    if not src.exists():
        msg = f"Source file not found: {src}"
        logger.warning(msg)
        return replace(entry, ingest_status=FetchStatus.ERROR, ingest_error=msg)

    try:
        if scaffold:
            raw_md = ""
        else:
            from vista_docs.ingest.converter import convert_to_markdown

            raw_md = convert_to_markdown(src)

        md_content = build_markdown(entry, raw_md)

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md_content, encoding="utf-8")
        logger.info("Wrote %s", out_path)

        return replace(
            entry,
            ingest_status=FetchStatus.OK,
            markdown_path=str(out_path),
            ingest_error="",
        )

    except Exception as exc:
        msg = str(exc)[:200]
        logger.error("Ingest failed for %s: %s", entry.doc_title, msg)
        return replace(entry, ingest_status=FetchStatus.ERROR, ingest_error=msg)
