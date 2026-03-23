"""
Pure markdown corpus analysis.

analyze_doc(md, entry)      → DocStats
summarize_corpus(stats)     → summary dict

No I/O. Takes strings and dataclasses, returns dataclasses and dicts.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from vista_docs.models.manifest import ManifestEntry

_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
_TABLE_ROW_RE = re.compile(r"^\|.+\|$", re.MULTILINE)
_TABLE_SEP_RE = re.compile(r"^\|[-| :]+\|$", re.MULTILINE)
_CALLOUT_RE = re.compile(r"^> \*\*(NOTE|WARNING|CAUTION|IMPORTANT|REMINDER):\*\*", re.MULTILINE)
_FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# A doc is a stub if its body (after stripping frontmatter) has fewer than
# this many non-blank lines.
_STUB_THRESHOLD = 3


@dataclass
class DocStats:
    app_code: str
    doc_title: str
    doc_type: str
    patch: str
    line_count: int
    word_count: int
    heading_count: int
    table_count: int
    callout_count: int
    is_stub: bool


def analyze_doc(md: str, entry: ManifestEntry) -> DocStats:
    """
    Analyze a single markdown document string.

    Counts headings, tables, callouts, words, lines.
    Detects stubs (frontmatter-only with no real body content).
    """
    body = _FRONTMATTER_RE.sub("", md, count=1)

    lines = md.splitlines()
    body_lines = [line for line in body.splitlines() if line.strip()]

    word_count = len(body.split())
    heading_count = len(_HEADING_RE.findall(body))

    # Count tables: a table is a block with a separator row (|---|---|)
    table_count = len(_TABLE_SEP_RE.findall(body))

    callout_count = len(_CALLOUT_RE.findall(body))

    is_stub = len(body_lines) < _STUB_THRESHOLD

    return DocStats(
        app_code=entry.app_code,
        doc_title=entry.doc_title,
        doc_type=entry.doc_type.value,
        patch=entry.patch,
        line_count=len(lines),
        word_count=word_count,
        heading_count=heading_count,
        table_count=table_count,
        callout_count=callout_count,
        is_stub=is_stub,
    )


def summarize_corpus(stats: list[DocStats]) -> dict:
    """
    Aggregate DocStats into a corpus-level summary dict.

    Keys:
      total_docs, total_stubs, total_words, total_lines
      by_package:  {app_code: {docs, stubs, words, headings, tables, callouts}}
      by_doc_type: {doc_type: count}
      quality_flags: {stubs: [...], short_docs: [...]}
    """
    if not stats:
        return {
            "total_docs": 0,
            "total_stubs": 0,
            "total_words": 0,
            "total_lines": 0,
            "by_package": {},
            "by_doc_type": {},
            "quality_flags": {"stubs": [], "short_docs": []},
        }

    by_package: dict[str, dict] = {}
    by_doc_type: dict[str, int] = {}
    stubs = []
    short_docs = []

    for s in stats:
        # by_package
        pkg = by_package.setdefault(
            s.app_code,
            {"docs": 0, "stubs": 0, "words": 0, "headings": 0, "tables": 0, "callouts": 0},
        )
        pkg["docs"] += 1
        pkg["words"] += s.word_count
        pkg["headings"] += s.heading_count
        pkg["tables"] += s.table_count
        pkg["callouts"] += s.callout_count
        if s.is_stub:
            pkg["stubs"] += 1
            stubs.append({"app_code": s.app_code, "doc_title": s.doc_title})

        # by_doc_type
        by_doc_type[s.doc_type] = by_doc_type.get(s.doc_type, 0) + 1

        # short but not stub: converted but suspiciously thin
        if not s.is_stub and s.word_count < 200:
            short_docs.append(
                {"app_code": s.app_code, "doc_title": s.doc_title, "words": s.word_count}
            )

    return {
        "total_docs": len(stats),
        "total_stubs": sum(1 for s in stats if s.is_stub),
        "total_words": sum(s.word_count for s in stats),
        "total_lines": sum(s.line_count for s in stats),
        "by_package": by_package,
        "by_doc_type": by_doc_type,
        "quality_flags": {"stubs": stubs, "short_docs": short_docs},
    }
