"""F10 — table policy (spec §6 F10).

Simple HTML tables become GFM pipe tables; complex tables (colspan/rowspan,
nested lists or tables, or multi-paragraph cells) are kept verbatim as raw HTML
to avoid corruption. Conversion is idempotent: a converted GFM table no longer
matches the ``<table>`` scanner.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser

_TABLE_RE = re.compile(r"<table\b.*?</table>", re.DOTALL | re.IGNORECASE)
_COMPLEX_ATTR_RE = re.compile(r"\b(?:colspan|rowspan)\s*=", re.IGNORECASE)
_BLOCK_IN_CELL_RE = re.compile(r"<(?:ul|ol|table)\b", re.IGNORECASE)
_CELL_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.DOTALL | re.IGNORECASE)
_P_RE = re.compile(r"<p\b", re.IGNORECASE)
_WS_RE = re.compile(r"\s+")


def is_complex_table(html: str) -> bool:
    """True if the table cannot be safely flattened to a GFM pipe table."""
    if _COMPLEX_ATTR_RE.search(html):
        return True
    # Block elements / multiple paragraphs *inside a cell* mean complex content.
    for cell in _CELL_RE.findall(html):
        if _BLOCK_IN_CELL_RE.search(cell) or len(_P_RE.findall(cell)) > 1:
            return True
    return False


class _Grid(HTMLParser):
    """Collect ``(is_header_row, [cell_text, ...])`` rows from a simple table."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[tuple[bool, list[str]]] = []
        self._row: list[str] | None = None
        self._row_has_th = False
        self._cell: list[str] | None = None
        self._in_thead = False

    def handle_starttag(self, tag: str, attrs: object) -> None:
        t = tag.lower()
        if t == "thead":
            self._in_thead = True
        elif t == "tr":
            self._row, self._row_has_th = [], False
        elif t in ("td", "th"):
            self._cell = []
            if t == "th":
                self._row_has_th = True
        elif t == "br" and self._cell is not None:
            self._cell.append(" ")

    def handle_startendtag(self, tag: str, attrs: object) -> None:
        if tag.lower() == "br" and self._cell is not None:
            self._cell.append(" ")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t == "thead":
            self._in_thead = False
        elif t in ("td", "th"):
            if self._cell is not None and self._row is not None:
                self._row.append(_WS_RE.sub(" ", "".join(self._cell)).strip())
            self._cell = None
        elif t == "tr" and self._row is not None:
            self.rows.append((self._in_thead or self._row_has_th, self._row))
            self._row = None

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)


def html_table_to_gfm(html: str) -> str | None:
    """Convert a simple HTML table to GFM, or return ``None`` if complex/empty."""
    if is_complex_table(html):
        return None
    grid = _Grid()
    grid.feed(html)
    if not grid.rows:
        return None
    header_idx = next((i for i, (h, _) in enumerate(grid.rows) if h), 0)
    header = grid.rows[header_idx][1]
    ncol = len(header)
    if ncol == 0:
        return None
    body_rows = [r for i, (_h, r) in enumerate(grid.rows) if i != header_idx]

    def fmt(cells: list[str]) -> str:
        padded = (cells + [""] * ncol)[:ncol]
        return "| " + " | ".join(c.replace("|", "\\|") for c in padded) + " |"

    lines = [fmt(header), "| " + " | ".join(["---"] * ncol) + " |"]
    lines.extend(fmt(r) for r in body_rows)
    return "\n".join(lines)


def convert_tables(body: str) -> str:
    """Replace every simple ``<table>`` in ``body`` with GFM; keep complex ones."""

    def repl(m: re.Match[str]) -> str:
        gfm = html_table_to_gfm(m.group(0))
        return gfm if gfm is not None else m.group(0)

    return _TABLE_RE.sub(repl, body)
