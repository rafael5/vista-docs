"""I/O thin layer: download a document, write to raw/, update state."""

from __future__ import annotations

import logging

import requests

from vista_docs.config import RAW_DIR, REQUEST_TIMEOUT
from vista_docs.fetch.strategy import candidate_urls
from vista_docs.models.manifest import FetchStatus, ManifestEntry

logger = logging.getLogger(__name__)


def download_entry(entry: ManifestEntry, session: requests.Session) -> ManifestEntry:
    """
    Download the document for a ManifestEntry. Tries candidate_urls in order.
    Returns a new ManifestEntry with fetch_status, local_path, etc. updated.
    """
    from dataclasses import replace

    urls = candidate_urls(entry.docx_url, entry.pdf_url)
    if not urls:
        return replace(entry, fetch_status=FetchStatus.ERROR, fetch_error="no URLs available")

    dest_dir = RAW_DIR / entry.app_code
    dest_dir.mkdir(parents=True, exist_ok=True)

    for url in urls:
        ext = url.rsplit(".", 1)[-1].lower()
        filename = url.rsplit("/", 1)[-1]
        dest = dest_dir / filename
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)
            if resp.status_code == 200:
                dest.write_bytes(resp.content)
                size = dest.stat().st_size
                logger.info("Downloaded %s → %s (%d bytes)", url, dest, size)
                return replace(
                    entry,
                    fetch_status=FetchStatus.OK,
                    local_path=str(dest),
                    fetched_ext=ext,
                    fetch_size=size,
                )
            logger.warning("HTTP %d for %s", resp.status_code, url)
        except requests.RequestException as exc:
            logger.warning("Request failed for %s: %s", url, exc)

    return replace(
        entry,
        fetch_status=FetchStatus.ERROR,
        fetch_error=f"all URLs failed: {urls}",
    )
