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
_PAGE_LINE_RE = re.compile(r"^\s*Page\s+\d+(?:\s+of\s+\d+)?\s*$", re.IGNORECASE)
_NUM_ONLY_RE = re.compile(r"^\s*\d{1,4}\s*$")
# Any element carrying an id is a definition — incl. pandoc footnotes (<li id="fn1">,
# <a id="fnref1">) — plus pandoc empty-span ``[]{#id}`` and heading ``{#id}`` attrs.
_ID_ATTR_RE = re.compile(r'<[a-zA-Z][^>]*\bid="([^"]+)"')
_PANDOC_ID_RE = re.compile(r"\{#([^}\s]+)")


def _blank_or_edge(lines: list[str], i: int) -> bool:
    return i < 0 or i >= len(lines) or not lines[i].strip()


def noise_violations(body: str) -> list[str]:
    """Return sorted noise codes still present in ``body`` (empty == clean).

    Page-number detection mirrors F2 exactly: a ``Page N`` footer line, or a
    numeric-only line *isolated* by blanks on both sides (an orphan page number).
    A bare number with a text neighbor is content (table data), not noise — so it
    is not flagged, keeping the linter consistent with what F2 removes. Redacted
    PM/TW cells are owned by F5 (it drops the whole revision table); remaining
    ``Redacted`` cells are legitimate source content and are not flagged.
    """
    codes: set[str] = set()
    if _FORM_FEED_RE.search(body):
        codes.add("form_feed")
    if _SPACE_RUN_RE.search(body):
        codes.add("space_run")
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if _PAGE_LINE_RE.match(line) or (
            _NUM_ONLY_RE.match(line)
            and _blank_or_edge(lines, i - 1)
            and _blank_or_edge(lines, i + 1)
        ):
            codes.add("page_number_line")
            break
    return sorted(codes)


def valid_anchor_ids(body: str) -> set[str]:
    """Every in-document target an anchor reference may legitimately resolve to:
    heading slugs plus explicit ``id=`` attributes (legacy bookmarks, page ids).
    """
    ids = {h.slug for h in extract_headings(body)}
    ids.update(_ID_ATTR_RE.findall(body))
    ids.update(_PANDOC_ID_RE.findall(body))
    return ids


def dead_anchors(body: str) -> list[str]:
    """Referenced in-document anchors that resolve to no heading slug or id."""
    return find_dead_anchors(body, valid_anchor_ids(body))


def sidecar_violations(
    doc_name: str,
    revision_sidecar: str | None,
    existing_sidecars: set[str],
    sidecar_document: str | None = None,
) -> list[str]:
    """Sidecar-integrity check (spec §11.4).

    A doc's ``revision_sidecar`` must name an existing sidecar file, and that
    sidecar's ``document`` back-reference must point back at the doc.
    """
    if not revision_sidecar:
        return []
    if revision_sidecar not in existing_sidecars:
        return [f"missing_sidecar:{revision_sidecar}"]
    if sidecar_document is not None and sidecar_document != doc_name:
        return [f"sidecar_backref_mismatch:{sidecar_document}"]
    return []
