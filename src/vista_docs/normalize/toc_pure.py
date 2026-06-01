"""F6 — TOC generation (spec §6 F6).

Builds a portable, link-based table of contents from the heading tree produced
by :func:`vista_docs.normalize.anchors_pure.extract_headings` (which the runner
sources from the stage-6.5 chunk tree). Headings deeper than ``max_level`` are
omitted; indentation is relative to the shallowest included heading.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from vista_docs.normalize.anchors_pure import Heading, extract_headings

_TAG_RE = re.compile(r"<[^>]+>")
_EMPH_RE = re.compile(r"[*`]")
_WS_RE = re.compile(r"\s+")
# A markdown list item that is a single link to an internal anchor: ``- [t](#a)``.
# Greedy text + final ``](#anchor)$`` so polluted text (an ``![]`` image, leaked
# ``##``) still matches and the original-TOC block is recognized whole.
_TOC_ITEM_LINK_RE = re.compile(r"^\s*[-*]\s+\[.+\]\(#([^)]+)\)\s*$")
_TOC_CAPTION_RE = re.compile(r"^#{0,6}\s*(?:table of\s+)?contents\s*$", re.IGNORECASE)


def _display_text(text: str) -> str:
    s = _TAG_RE.sub("", text)
    s = _EMPH_RE.sub("", s)
    return _WS_RE.sub(" ", s).strip()


def remove_original_toc(
    body: str, min_items: int = 6, hit_fraction: float = 0.5
) -> tuple[str, int]:
    """Remove the original pandoc TOC so F6 can regenerate a clean one (spec §6 F6).

    A contiguous run of >= ``min_items`` list-item links where at least
    ``hit_fraction`` of the targets resolve to real heading slugs is treated as
    the document's table of contents and removed (along with a preceding
    ``Contents`` / ``Table of Contents`` caption). The slug-resolution signal —
    not position — identifies the TOC, which also sweeps up its malformed entries
    (leaked ``##`` markers, fused images) in one shot. Returns ``(body, items_removed)``.
    """
    slugs = {h.slug for h in extract_headings(body)}
    lines = body.split("\n")
    remove: set[int] = set()
    i, n = 0, len(lines)
    while i < n:
        if not _TOC_ITEM_LINK_RE.match(lines[i]):
            i += 1
            continue
        start = i
        anchors: list[str] = []
        while i < n and (m := _TOC_ITEM_LINK_RE.match(lines[i])):
            anchors.append(m.group(1))
            i += 1
        if len(anchors) >= min_items and sum(a in slugs for a in anchors) / len(anchors) >= (
            hit_fraction
        ):
            remove.update(range(start, start + len(anchors)))
            k = start - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            if k >= 0 and _TOC_CAPTION_RE.match(lines[k]):
                remove.add(k)
    removed_items = sum(1 for idx in remove if _TOC_ITEM_LINK_RE.match(lines[idx]))
    out = "\n".join(line for idx, line in enumerate(lines) if idx not in remove)
    return out, removed_items


# Docling emits the original TOC as a caption with *any* number of leading ``#``
# (markdown caps headings at 6, so ``########### Table of Contents`` renders as
# literal text) followed by tab-separated ``Entry<TAB>page`` lines — neither a
# heading nor a link list, so ``remove_original_toc`` misses it.
_CAPTION_TOC_RE = re.compile(r"^#*[ \t]*(?:table of[ \t]+)?contents[ \t]*$", re.IGNORECASE)
_CAPTION_TOC_ENTRY_RE = re.compile(r"^.+\t+\d+[ \t]*$")


def remove_caption_toc(body: str, min_items: int = 6) -> tuple[str, int]:
    """Remove a Docling-style original TOC (spec §6 F6).

    Anchored on a ``Table of Contents`` caption (with any number of leading
    ``#``) immediately followed by a contiguous run of >= ``min_items``
    ``Entry<TAB>page`` lines — the caption requirement keeps the tab+number
    heuristic from eating ordinary content. Returns ``(body, items_removed)``.
    """
    lines = body.split("\n")
    remove: set[int] = set()
    i, n = 0, len(lines)
    while i < n:
        if _CAPTION_TOC_RE.match(lines[i]):
            j = i + 1
            while j < n and not lines[j].strip():  # blank(s) between caption + entries
                j += 1
            start = j
            while j < n and _CAPTION_TOC_ENTRY_RE.match(lines[j]):
                j += 1
            if j - start >= min_items:
                remove.add(i)  # caption
                remove.update(range(i + 1, j))  # blanks + entries
                i = j
                continue
        i += 1
    removed = sum(1 for idx in remove if _CAPTION_TOC_ENTRY_RE.match(lines[idx]))
    out = "\n".join(line for idx, line in enumerate(lines) if idx not in remove)
    return out, removed


def build_toc(
    headings: Sequence[Heading], max_level: int = 3, heading: str = "Table of Contents"
) -> str:
    """Render a nested markdown TOC. Returns ``""`` when nothing is in range.

    The heading is ``Table of Contents`` (slug ``table-of-contents``) to match the
    ``[↑ Table of Contents](#table-of-contents)`` back-links injected at ingest —
    a ``Contents`` heading slugs to ``contents`` and leaves every back-link dead.
    """
    items = [h for h in headings if h.level <= max_level]
    if not items:
        return ""
    base = min(h.level for h in items)
    lines = [f"## {heading}", ""]
    for h in items:
        indent = "  " * (h.level - base)
        lines.append(f"{indent}- [{_display_text(h.text)}](#{h.slug})")
    return "\n".join(lines) + "\n"
