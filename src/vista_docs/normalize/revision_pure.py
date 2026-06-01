"""F5 — revision-history extraction (spec §6 F5).

Harvests the revision table at the top of Word-origin docs, drops the
uniformly-redacted ``Project Manager`` / ``Technical Writer`` columns (the only
true deletion), and returns structured records plus a frontmatter summary. The
table is removed from the body; the polluted ``description:`` (which captured the
table caption) is cleared so audit regenerates it.

Two table dialects are recognized: the HTML ``<table>`` pandoc dumps, and the
GFM pipe table the Docling backend emits (see ``DOCLING_DOCS`` in
``ingest/converter``). ``find_revision_table``/``parse_revision_table`` dispatch
on whichever form is present.

All output is plain Python values — the I/O layer writes the ``*.history.yaml``
sidecar and routes the summary through ``audit_frontmatter``.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import dataclass, field

_TABLE_RE = re.compile(r"<table\b.*?</table>", re.DOTALL | re.IGNORECASE)
_ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
_CELL_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.DOTALL | re.IGNORECASE)
_HREF_RE = re.compile(r'href="(#[^"]+)"')
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")
_BLOCK_END_RE = re.compile(r"</(?:li|p|ul|ol)>", re.IGNORECASE)
_INT_RE = re.compile(r"\d+")
_MMYYYY_RE = re.compile(r"^(\d{1,2})/(\d{4})$")
_MDY_RE = re.compile(r"^(\d{1,2})/(\d{1,2})/(\d{2,4})$")
_CAPTION_RE = re.compile(r"(?i)^\s*(revision history|this table lists the history)")


@dataclass(frozen=True)
class RevisionRecord:
    """One revision-history row, PM/TW columns dropped."""

    date: str
    version: str
    pages: list[int]
    change: str
    refs: list[str] = field(default_factory=list)


def _flatten(cell_html: str) -> str:
    return _WS_RE.sub(" ", _html.unescape(_TAG_RE.sub("", cell_html))).strip()


def _flatten_change(cell_html: str) -> str:
    s = _BLOCK_END_RE.sub(" \n", cell_html)
    s = _html.unescape(_TAG_RE.sub("", s))
    parts = [_WS_RE.sub(" ", line).strip() for line in s.split("\n")]
    return "; ".join(p for p in parts if p)


def _norm_date(text: str) -> str:
    t = text.strip()
    m = _MMYYYY_RE.match(t)
    if m:
        return f"{m.group(2)}-{int(m.group(1)):02d}"
    m = _MDY_RE.match(t)
    if m:
        month, year = int(m.group(1)), m.group(3)
        if len(year) == 2:
            year = ("20" if int(year) < 50 else "19") + year
        return f"{year}-{month:02d}"
    return t


def _refs(cell_html: str) -> list[str]:
    return _HREF_RE.findall(cell_html)


def _header_text(table_html: str) -> str:
    rows = _ROW_RE.findall(table_html)
    if not rows:
        return ""
    return " ".join(_flatten(c).lower() for c in _CELL_RE.findall(rows[0]))


def _is_revision_header(header: str) -> bool:
    return "date" in header and "change" in header and ("version" in header or "patch" in header)


def find_revision_table(body: str) -> tuple[int, int, str] | None:
    """Return ``(start, end, table)`` of the revision table, or ``None``.

    Prefers the HTML ``<table>`` (pandoc); falls back to a GFM pipe table
    (Docling). ``table`` is the raw matched block, dispatched on by
    :func:`parse_revision_table`.
    """
    for m in _TABLE_RE.finditer(body):
        if _is_revision_header(_header_text(m.group(0))):
            return m.start(), m.end(), m.group(0)
    return _find_pipe_table(body)


# --- GFM pipe-table dialect (Docling-origin docs) --------------------------

_PIPE_LINE_RE = re.compile(r"^[ \t]*\|.*\|[ \t]*$")
_PIPE_SEP_RE = re.compile(r"^[ \t]*\|[ \t:|-]+\|[ \t]*$")
_PIPE_SPLIT_RE = re.compile(r"(?<!\\)\|")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((#[^)]*)\)")


def _pipe_cells(line: str) -> list[str]:
    """Split a GFM row into cells (outer pipes dropped, ``\\|`` unescaped)."""
    parts = _PIPE_SPLIT_RE.split(line.strip())
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.replace("\\|", "|").strip() for p in parts]


def _md_link_text(s: str) -> str:
    """``[170](#anchor)`` -> ``170`` so anchors don't pollute page/change text."""
    return _MD_LINK_RE.sub(r"\1", s)


def _md_link_refs(s: str) -> list[str]:
    return [m.group(2) for m in _MD_LINK_RE.finditer(s)]


def _find_pipe_table(body: str) -> tuple[int, int, str] | None:
    lines = body.split("\n")
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    for i in range(len(lines) - 1):
        if not (_PIPE_LINE_RE.match(lines[i]) and _PIPE_SEP_RE.match(lines[i + 1])):
            continue
        if not _is_revision_header(" ".join(_pipe_cells(lines[i])).lower()):
            continue
        j = i + 2
        while j < len(lines) and _PIPE_LINE_RE.match(lines[j]):
            j += 1
        start = offsets[i]
        end = offsets[j - 1] + len(lines[j - 1])
        return start, end, "\n".join(lines[i:j])
    return None


def parse_revision_table(table: str) -> list[RevisionRecord]:
    """Parse a revision table (HTML or GFM pipe) into records, dropping PM/TW."""
    if "<table" in table.lower():
        return _parse_html_table(table)
    return _parse_pipe_table(table)


def _parse_pipe_table(table: str) -> list[RevisionRecord]:
    lines = [ln for ln in table.split("\n") if _PIPE_LINE_RE.match(ln)]
    if len(lines) < 2:
        return []
    header = [h.lower() for h in _pipe_cells(lines[0])]

    def col(*names: str) -> int | None:
        for i, h in enumerate(header):
            if any(n in h for n in names):
                return i
        return None

    di, vi, pi, ci = col("date"), col("version", "patch"), col("page"), col("change")
    records: list[RevisionRecord] = []
    for row in lines[2:]:  # skip header + separator
        if _PIPE_SEP_RE.match(row):
            continue
        cells = _pipe_cells(row)

        def cell(idx: int | None) -> str:
            return cells[idx] if idx is not None and idx < len(cells) else ""

        page_raw, change_raw = cell(pi), cell(ci)
        records.append(
            RevisionRecord(
                date=_norm_date(cell(di)),
                version=cell(vi),
                pages=[int(n) for n in _INT_RE.findall(_md_link_text(page_raw))],
                change=_WS_RE.sub(" ", _md_link_text(change_raw)).strip(),
                refs=_md_link_refs(page_raw) + _md_link_refs(change_raw),
            )
        )
    return records


def _parse_html_table(table_html: str) -> list[RevisionRecord]:
    """Parse a revision table into records, dropping PM/TW columns."""
    rows = _ROW_RE.findall(table_html)
    if not rows:
        return []
    header = [_flatten(c).lower() for c in _CELL_RE.findall(rows[0])]

    def col(*names: str) -> int | None:
        for i, h in enumerate(header):
            if any(n in h for n in names):
                return i
        return None

    di, vi, pi, ci = col("date"), col("version", "patch"), col("page"), col("change")
    records: list[RevisionRecord] = []
    for row in rows[1:]:
        cells = _CELL_RE.findall(row)
        if not cells:
            continue

        def cell(idx: int | None) -> str:
            return cells[idx] if idx is not None and idx < len(cells) else ""

        page_html = cell(pi)
        change_html = cell(ci)
        records.append(
            RevisionRecord(
                date=_norm_date(_flatten(cell(di))),
                version=_flatten(cell(vi)),
                pages=[int(n) for n in _INT_RE.findall(_flatten(page_html))],
                change=_flatten_change(change_html),
                refs=_refs(page_html) + _refs(change_html),
            )
        )
    return records


def summarize_revisions(records: list[RevisionRecord]) -> dict:
    """Frontmatter summary: count + newest/oldest normalized dates."""
    dates = [r.date for r in records if re.fullmatch(r"\d{4}-\d{2}", r.date)]
    return {
        "revision_count": len(records),
        "revision_newest": max(dates) if dates else None,
        "revision_oldest": min(dates) if dates else None,
    }


def remove_revision_table(body: str) -> tuple[str, bool]:
    """Remove the revision table (and a preceding ``Revision History`` caption)."""
    found = find_revision_table(body)
    if not found:
        return body, False
    start, end, _ = found
    before = re.sub(r"\n*[ \t]*Revision History[ \t]*\n*$", "", body[:start])
    after = body[end:]
    new = before.rstrip("\n") + "\n\n" + after.lstrip("\n")
    return new, True


_REV_CAPTION_BODY_RE = re.compile(
    r"(?i)^\s*(?:revision history\s*)?this table lists the history for each revision"
)


def strip_revision_caption(body: str) -> tuple[str, int]:
    """Remove the residual revision-table caption paragraph from the body.

    Pandoc duplicates the table's ``<caption>`` ("Revision HistoryThis table
    lists the history for each revision …") as a body paragraph that survives
    table removal. Drop it. Matches only the polluted concatenated form, never a
    clean ``Revision History`` heading. Returns ``(body, removed_count)``.
    """
    lines = body.split("\n")
    kept = [line for line in lines if not _REV_CAPTION_BODY_RE.match(line)]
    return "\n".join(kept), len(lines) - len(kept)


def depollute_description(desc: object) -> str:
    """Clear a ``description:`` that begins with the revision-table caption."""
    if not isinstance(desc, str):
        return ""
    if _CAPTION_RE.match(desc):
        return ""
    return desc
