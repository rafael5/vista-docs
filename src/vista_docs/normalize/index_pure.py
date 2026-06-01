"""Corpus anchor index (spec §11.5) — pure.

Builds the ``doc → {headings, slugs, aliases}`` index emitted to ``survey/`` and
used by F8 cross-doc link resolution and the dead-anchor check. Per-doc entries
are pure; the corpus walk + JSON write live in the omitted ``index_runner.py``.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from vista_docs.normalize.anchors_pure import extract_headings

_TAG_RE = re.compile(r"<[^>]+>")
_EMPH_RE = re.compile(r"[*`]")
_WS_RE = re.compile(r"\s+")


def _display(text: str) -> str:
    return _WS_RE.sub(" ", _EMPH_RE.sub("", _TAG_RE.sub("", text))).strip()


def anchor_index_entry(doc: str, body: str, aliases: Mapping[str, str] | None = None) -> dict:
    """One index record: the doc's headings, their slugs, and its alias map."""
    headings = extract_headings(body)
    return {
        "doc": doc,
        "headings": [
            {"level": h.level, "text": _display(h.text), "slug": h.slug} for h in headings
        ],
        "slugs": [h.slug for h in headings],
        "aliases": dict(aliases or {}),
    }


def build_anchor_index(entries: Sequence[dict]) -> dict:
    """Merge per-doc entries into a ``{doc: {headings, slugs, aliases}}`` map."""
    return {e["doc"]: {k: v for k, v in e.items() if k != "doc"} for e in entries}
