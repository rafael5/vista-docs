"""Normalize-stage CI lint helpers (spec §11) — pure.

Used by the publish/push hard gate and corpus CI to fail on residual noise or
dangling anchors after normalize. Each check takes a document body and returns
plain values; the runner walks the corpus and aggregates.
"""

from __future__ import annotations

import re

from vista_docs.normalize.anchors_pure import extract_headings
from vista_docs.normalize.linkfix_pure import find_dead_anchors

_FORM_FEED_RE = re.compile(r"[\x0c]")
_SPACE_RUN_RE = re.compile(r" {6,}")
_PAGE_LINE_RE = re.compile(r"^\s*Page\s+\d+(?:\s+of\s+\d+)?\s*$", re.IGNORECASE | re.MULTILINE)
_NUM_ONLY_RE = re.compile(r"^\s*\d{1,4}\s*$", re.MULTILINE)
_REDACTED_CELL_RE = re.compile(r"<t[dh]\b[^>]*>\s*(?:Redacted|N/A)\s*</t[dh]>", re.IGNORECASE)
_ID_ATTR_RE = re.compile(r'<(?:span|a)\b[^>]*\bid="([^"]+)"')


def noise_violations(body: str) -> list[str]:
    """Return sorted noise codes still present in ``body`` (empty == clean)."""
    codes: set[str] = set()
    if _FORM_FEED_RE.search(body):
        codes.add("form_feed")
    if _SPACE_RUN_RE.search(body):
        codes.add("space_run")
    if _PAGE_LINE_RE.search(body) or _NUM_ONLY_RE.search(body):
        codes.add("page_number_line")
    if _REDACTED_CELL_RE.search(body):
        codes.add("redacted_cell")
    return sorted(codes)


def valid_anchor_ids(body: str) -> set[str]:
    """Every in-document target an anchor reference may legitimately resolve to:
    heading slugs plus explicit ``id=`` attributes (legacy bookmarks, page ids).
    """
    ids = {h.slug for h in extract_headings(body)}
    ids.update(_ID_ATTR_RE.findall(body))
    return ids


def dead_anchors(body: str) -> list[str]:
    """Referenced in-document anchors that resolve to no heading slug or id."""
    return find_dead_anchors(body, valid_anchor_ids(body))
