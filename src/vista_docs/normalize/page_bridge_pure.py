"""F7 — page-number bridge, pure logic (spec §6 F7).

Realizes preserve -> bridge -> retire for paginated-only (Class C) docs, each
step reversible via the ``*.toc.yaml`` sidecar:

  1. inject silent ``<a id="pN"></a><!-- page N -->`` anchors at page starts;
  2. resolve each ``pN`` to the nearest *following* heading slug;
  3. retire the ``pN`` anchors once the original TOC links point at real slugs.

The PDF text extraction + alignment that locates page starts is I/O and lives in
``pdf_reader.py`` (coverage-omitted); everything here is pure and testable.
"""

from __future__ import annotations

import re

from vista_docs.normalize.anchors_pure import Slugger, _iter_heading_lines

_PAGE_ID_RE = re.compile(r'<a id="(p\d+)"></a>')
_MARKER_RE = re.compile(r'<a id="p\d+"></a><!-- page \d+ -->')
_MARKER_LINE_RE = re.compile(r'^\s*<a id="p\d+"></a><!-- page \d+ -->\s*$')


def page_anchor_markup(n: int) -> str:
    """The silent page anchor for page ``n``."""
    return f'<a id="p{n}"></a><!-- page {n} -->'


def inject_page_anchors(body: str, page_lines: list[tuple[int, int]]) -> str:
    """Insert page anchors before the given ``(page_no, line_index)`` positions."""
    lines = body.split("\n")
    for page_no, line_index in sorted(page_lines, key=lambda x: x[1], reverse=True):
        lines.insert(line_index, page_anchor_markup(page_no))
    return "\n".join(lines)


def map_pages_to_slugs(body: str) -> dict[str, str]:
    """Map each ``pN`` anchor to the slug of the nearest following heading."""
    lines = body.split("\n")
    slugger = Slugger()
    headings = [(i, slugger.slug(text)) for i, _level, text in _iter_heading_lines(body)]
    result: dict[str, str] = {}
    for i, line in enumerate(lines):
        for m in _PAGE_ID_RE.finditer(line):
            following = [(hidx, slug) for hidx, slug in headings if hidx >= i]
            if following:
                result[m.group(1)] = min(following, key=lambda h: h[0])[1]
    return result


def rewrite_page_toc(toc: list[dict], page_to_slug: dict[str, str]) -> list[dict]:
    """Return a copy of the original-TOC entries with ``#pN`` -> ``#slug``."""
    out: list[dict] = []
    for entry in toc:
        new = dict(entry)
        anchor = new.get("anchor", "")
        if anchor.startswith("#") and anchor[1:] in page_to_slug:
            new["anchor"] = "#" + page_to_slug[anchor[1:]]
        out.append(new)
    return out


def retire_page_anchors(body: str) -> tuple[str, int]:
    """Delete page anchors and their ``<!-- page -->`` comments. Idempotent."""
    count = len(_MARKER_RE.findall(body))
    lines = [line for line in body.split("\n") if not _MARKER_LINE_RE.match(line)]
    out = _MARKER_RE.sub("", "\n".join(lines))
    return out, count
