"""
Pure URL derivation for document fetching.

Given a document's known URLs (DOCX and/or PDF), returns an ordered
list of candidate URLs to try. DOCX is always tried first.
"""

from __future__ import annotations

import re

_EXT_RE = re.compile(r"\.(docx|pdf)$", re.I)


def swap_extension(url: str) -> str:
    """Swap .docx ↔ .pdf in a URL. Returns url unchanged if neither extension found."""
    m = _EXT_RE.search(url)
    if not m:
        return url
    current = m.group(1).lower()
    new = "pdf" if current == "docx" else "docx"
    return _EXT_RE.sub(f".{new}", url)


def candidate_urls(docx_url: str, pdf_url: str) -> list[str]:
    """
    Return an ordered list of URLs to try for a document.

    Strategy:
    - DOCX is always preferred over PDF.
    - If only one URL is known, derive the other by extension swap.
    - Returns at most 2 unique URLs, DOCX first.
    - Returns [] if no URLs are available.
    """
    if not docx_url and not pdf_url:
        return []

    if docx_url and pdf_url:
        return [docx_url, pdf_url]

    if docx_url:
        return [docx_url, swap_extension(docx_url)]

    # Only PDF known — derive DOCX
    derived_docx = swap_extension(pdf_url)
    return [derived_docx, pdf_url]
