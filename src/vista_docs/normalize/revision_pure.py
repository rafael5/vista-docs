"""F5 — revision-history extraction (spec §6 F5).

Harvests the revision ``<table>`` pandoc dumps at the top of Word-origin docs,
drops the uniformly-redacted ``Project Manager`` / ``Technical Writer`` columns
(the only true deletion), and returns structured records plus a frontmatter
summary. The table is removed from the body; the polluted ``description:`` (which
captured the table caption) is cleared so audit regenerates it.

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


def find_revision_table(body: str) -> tuple[int, int, str] | None:
    """Return ``(start, end, html)`` of the revision table, or ``None``."""
    for m in _TABLE_RE.finditer(body):
        header = _header_text(m.group(0))
        if "date" in header and "change" in header and ("version" in header or "patch" in header):
            return m.start(), m.end(), m.group(0)
    return None


def parse_revision_table(table_html: str) -> list[RevisionRecord]:
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


def depollute_description(desc: object) -> str:
    """Clear a ``description:`` that begins with the revision-table caption."""
    if not isinstance(desc, str):
        return ""
    if _CAPTION_RE.match(desc):
        return ""
    return desc
