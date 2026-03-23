"""
Pure metadata extractors for enriching VDL markdown documents.

All functions take a markdown string and return plain Python values.
No I/O, no filesystem, no external dependencies beyond stdlib.

Extraction is designed around real Docling output from VA VDL DOCX files:
  - Title page: date appears as bold (**Month YYYY**) or plain text near top
  - TOC: "Section Title<tab>page_number" lines
  - Revision history: table with Date column near the top of the document
  - Appendices: headings starting with "Appendix"
"""

from __future__ import annotations

import re
from collections import Counter

# ---------------------------------------------------------------------------
# Shared patterns
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# Dates: "April 2007", "March 2020", "2023-10-19", "4/30/07", "10/14/98"
_MONTH_YEAR_RE = re.compile(
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+(\d{4})\b",
    re.IGNORECASE,
)
_ISO_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
_US_DATE_RE = re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4})\b")

# TOC: line ending with tab + integer page number
_TOC_PAGE_RE = re.compile(r"\t(\d+)\s*$", re.MULTILINE)

# Table separator row
_TABLE_SEP_RE = re.compile(r"^\|[-| :]+\|$", re.MULTILINE)

# Appendix heading (## Appendix A...) or TOC line (Appendix A...<tab>N)
_APPENDIX_RE = re.compile(r"(?:^#{1,6}\s+)?Appendix\s+([A-Z])\b", re.MULTILINE | re.I)

# H2 section headings
_H2_RE = re.compile(r"^##\s+", re.MULTILINE)

# Stopwords for keyword extraction
_STOPWORDS = {
    "the",
    "and",
    "for",
    "are",
    "can",
    "that",
    "this",
    "with",
    "from",
    "have",
    "been",
    "will",
    "not",
    "you",
    "all",
    "any",
    "its",
    "may",
    "use",
    "used",
    "each",
    "into",
    "also",
    "when",
    "then",
    "than",
    "more",
    "but",
    "one",
    "which",
    "such",
    "they",
    "their",
    "there",
    "these",
    "those",
    "has",
    "had",
    "was",
    "were",
    "who",
    "how",
    "new",
    "see",
    "per",
    "via",
    "etc",
    "must",
    "should",
    "would",
    "could",
    "file",
    "page",
    "section",
    "following",
    "using",
    "enter",
    "select",
    "click",
    "option",
    "name",
    "type",
    "note",
    "value",
    "list",
    "menu",
    "screen",
    "field",
    "item",
    "text",
    "display",
    "information",
    "following",
    "user",
    "users",
    "system",
    "data",
    "set",
}

# Top-of-document scan limit (lines) for pub_date
_TITLE_PAGE_LINES = 60


# ---------------------------------------------------------------------------
# Cycle 1: publication date
# ---------------------------------------------------------------------------


def extract_pub_date(md: str) -> str:
    """
    Extract the publication date from the top of the document.

    Scans the first ~80 lines (title page area) without stopping at headings,
    because release notes have an H2 title heading followed by the date.
    Priority: ISO date > Month YYYY > (nothing).
    Bold markers (**text**) are stripped before matching.
    Returns empty string if not found.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    top = "\n".join(body.splitlines()[:_TITLE_PAGE_LINES])
    # Strip bold markers
    top_clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", top)

    m = _ISO_DATE_RE.search(top_clean)
    if m:
        return m.group(1)
    m = _MONTH_YEAR_RE.search(top_clean)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return ""


# ---------------------------------------------------------------------------
# Cycle 2: page count (from TOC)
# ---------------------------------------------------------------------------


def extract_page_count(md: str) -> int:
    """
    Estimate page count from the highest integer page number in the TOC.

    TOC lines look like: "Section Title<tab>124"
    Ignores Roman numeral page numbers (front matter).
    Returns 0 if no TOC found.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    pages = [int(m.group(1)) for m in _TOC_PAGE_RE.finditer(body)]
    return max(pages) if pages else 0


# ---------------------------------------------------------------------------
# Cycle 3: revision history
# ---------------------------------------------------------------------------


def _parse_date_value(s: str) -> str | None:
    """Return a date string if s looks like a date, else None."""
    s = s.strip()
    if _ISO_DATE_RE.fullmatch(s):
        return s
    if _US_DATE_RE.fullmatch(s):
        return s
    return None


def _compare_dates(a: str, b: str) -> int:
    """
    Compare two date strings for ordering. Returns -1, 0, or 1.
    Handles ISO (YYYY-MM-DD) and US (M/D/YY or M/D/YYYY) formats.
    Mixed formats: ISO < US dates from 2000s, heuristically.
    """

    def _sort_key(d: str) -> tuple:
        if "-" in d:  # ISO
            parts = d.split("-")
            return (int(parts[0]), int(parts[1]), int(parts[2]))
        parts = d.split("/")
        year = int(parts[2])
        if year < 100:
            year += 1900 if year > 50 else 2000
        return (year, int(parts[0]), int(parts[1]))

    ka, kb = _sort_key(a), _sort_key(b)
    return -1 if ka < kb else (1 if ka > kb else 0)


def extract_revision_history(md: str) -> dict:
    """
    Find the revision history table and return count, oldest, newest dates.

    Looks for a table with a 'Date' column header near the top half of the doc.
    Returns {"count": 0, "oldest": "", "newest": ""} if not found.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    lines = body.splitlines()

    # Find table blocks by locating separator rows
    dates: list[str] = []
    in_table = False
    date_col: int | None = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect header row with "Date" column
        if not in_table and stripped.startswith("|") and "date" in stripped.lower():
            cells = [c.strip().lower() for c in stripped.split("|")]
            for j, cell in enumerate(cells):
                if cell == "date":
                    date_col = j
                    in_table = True
                    break

        elif in_table and _TABLE_SEP_RE.match(stripped):
            continue  # separator row

        elif in_table and stripped.startswith("|") and date_col is not None:
            cells = [c.strip() for c in stripped.split("|")]
            if date_col < len(cells):
                val = _parse_date_value(cells[date_col])
                if val:
                    dates.append(val)

        elif in_table and not stripped.startswith("|"):
            in_table = False
            date_col = None

    if not dates:
        return {"count": 0, "oldest": "", "newest": ""}

    # Sort in-place using bubble sort (avoids unused variable)
    for _ in range(len(dates)):
        for j in range(len(dates) - 1):
            if _compare_dates(dates[j], dates[j + 1]) > 0:
                dates[j], dates[j + 1] = dates[j + 1], dates[j]

    return {"count": len(dates), "oldest": dates[0], "newest": dates[-1]}


# ---------------------------------------------------------------------------
# Cycle 4: appendices
# ---------------------------------------------------------------------------


def extract_appendices(md: str) -> int:
    """
    Count the number of appendices in the document.

    Matches both heading lines (## Appendix A: ...) and TOC entries
    (Appendix A<tab>N). Deduplicates by letter to avoid double-counting.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    letters: set[str] = set()
    for m in _APPENDIX_RE.finditer(body):
        letters.add(m.group(1).upper())
    return len(letters)


# ---------------------------------------------------------------------------
# Cycle 5: table count
# ---------------------------------------------------------------------------


def extract_table_count(md: str) -> int:
    """Count markdown tables by separator rows (|---|---|)."""
    body = _FRONTMATTER_RE.sub("", md, count=1)
    return len(_TABLE_SEP_RE.findall(body))


# ---------------------------------------------------------------------------
# Cycle 6: section count (H2 headings)
# ---------------------------------------------------------------------------


def extract_section_count(md: str) -> int:
    """Count top-level sections (H2 headings)."""
    body = _FRONTMATTER_RE.sub("", md, count=1)
    return len(_H2_RE.findall(body))


# ---------------------------------------------------------------------------
# Cycle 7: keywords
# ---------------------------------------------------------------------------


def extract_keywords(md: str, max_keywords: int = 10) -> list[str]:
    """
    Extract the most frequent meaningful terms from the document body.

    Strips frontmatter, markdown syntax, and stopwords.
    Returns up to max_keywords terms, ranked by frequency.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    if not body.strip():
        return []

    # Strip markdown syntax
    body = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)  # headings
    body = re.sub(r"\*\*?([^*]+)\*\*?", r"\1", body)  # bold/italic
    body = re.sub(r"^\|.*\|$", "", body, flags=re.MULTILINE)  # table rows
    body = re.sub(r"^>.*$", "", body, flags=re.MULTILINE)  # blockquotes
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)  # html comments
    body = re.sub(r"https?://\S+", "", body)  # urls
    body = re.sub(r"[^a-zA-Z\s]", " ", body)  # non-alpha

    words = [w.lower() for w in body.split() if len(w) > 3]
    words = [w for w in words if w not in _STOPWORDS]

    freq = Counter(words)
    return [word for word, _ in freq.most_common(max_keywords)]


# ---------------------------------------------------------------------------
# Cycle 8: package name
# ---------------------------------------------------------------------------

# "Full Package Name (CODE)" — CODE is 2-8 uppercase letters/digits
_PKG_NAME_RE = re.compile(
    r"^([A-Z][A-Za-z ,:/&-]{10,}?)\s+\(([A-Z0-9]{2,8})\)\s*$",
    re.MULTILINE,
)


def extract_package_name(md: str) -> str:
    """
    Extract the full package name from the title page.

    Looks for lines matching "Full Name (ABBREV)" pattern in the first 80 lines.
    Returns the full name (without the abbreviation in parens), or empty string.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    top = "\n".join(body.splitlines()[:_TITLE_PAGE_LINES])
    m = _PKG_NAME_RE.search(top)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# Cycle 9: package namespace (from frontmatter patch field)
# ---------------------------------------------------------------------------

_PATCH_FIELD_RE = re.compile(r"^patch:\s*([A-Z0-9]+)\*", re.MULTILINE)


def extract_package_namespace(md: str) -> str:
    """
    Extract the VistA M package namespace from the patch field in frontmatter.

    e.g. patch: OR*3.0*636  →  "OR"
         patch: DG*5.3*1057 →  "DG"
    Returns empty string if no patch field or no namespace found.
    """
    m = _PATCH_FIELD_RE.search(md)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Cycle 10: package version (from frontmatter patch field)
# ---------------------------------------------------------------------------

_PATCH_VERSION_RE = re.compile(r"^patch:\s*[A-Z0-9]+\*([0-9]+(?:\.[0-9]+)?)\*", re.MULTILINE)


def extract_package_version(md: str) -> str:
    """
    Extract the package version from the patch field in frontmatter.

    e.g. patch: OR*3.0*636  →  "3.0"
         patch: DG*5.3*1057 →  "5.3"
         patch: PSJ*5*423   →  "5"
    Returns empty string if no patch field found.
    """
    m = _PATCH_VERSION_RE.search(md)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Cycle 11: audience
# ---------------------------------------------------------------------------

_AUDIENCE_HEADING_RE = re.compile(
    r"^#{1,4}\s+(?:Intended\s+)?Audience\s*$",
    re.MULTILINE | re.IGNORECASE,
)
_NEXT_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)


def extract_audience(md: str) -> str:
    """
    Extract the audience description from an Audience or Intended Audience section.

    Returns the first paragraph after the heading, truncated to 300 characters.
    Returns empty string if no audience section found.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    m = _AUDIENCE_HEADING_RE.search(body)
    if not m:
        return ""

    after = body[m.end() :].lstrip("\n")
    # Find the next heading to bound the section
    next_h = _NEXT_HEADING_RE.search(after)
    section = after[: next_h.start()] if next_h else after

    # Take first non-blank paragraph
    paragraphs = [p.strip() for p in section.split("\n\n") if p.strip()]
    if not paragraphs:
        return ""

    text = paragraphs[0]
    # Strip HTML entities and extra whitespace
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&[a-z]+;", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:300]


# ---------------------------------------------------------------------------
# Cycle 12: figure count
# ---------------------------------------------------------------------------

_FIGURE_RE = re.compile(r"^Figure\s+(\d+)\s*[:\.]", re.MULTILINE | re.IGNORECASE)


def extract_figure_count(md: str) -> int:
    """
    Count the number of unique figures referenced in the document.

    Matches "Figure N:" or "Figure N." lines in both TOC and body.
    Deduplicates by figure number so TOC + body entries are not double-counted.
    Returns 0 if no figures found.
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)
    numbers: set[int] = set()
    for m in _FIGURE_RE.finditer(body):
        numbers.add(int(m.group(1)))
    return len(numbers)
