"""
CHANGELOG builder: generate CHANGELOG.md per package from release-note records.

build_changelog(app_code, records, content_map) → str
extract_rn_summary(text)                        → str

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  ENTRIES ARE SORTED NEWEST FIRST.
    Records are sorted by pub_date descending using the same (year, month) parse
    logic as consolidate.py. Records with unparseable dates (unknown → (0,0))
    sort to the end of the list.

B.  EACH ENTRY CONTAINS:
    - Patch ID as the section heading
    - Publication date
    - Word count
    - Link to the original file in originals/release-note/
    - A brief summary extracted from the document body (Axiom C)

C.  SUMMARY EXTRACTION:
    The summary is the first non-empty, non-heading paragraph of the document
    body (frontmatter stripped). Truncated at 300 characters. If the body
    contains no prose paragraph, the summary is empty and the entry still
    renders (just without a summary line).

D.  EMPTY PACKAGE (no release notes):
    Returns a minimal CHANGELOG.md noting that no release notes are available.
    This is valid — not all packages have release notes.

E.  MISSING CONTENT:
    If a record's original_path is not in content_map, the entry is rendered
    with metadata only (no summary). No error is raised.
"""

from __future__ import annotations

import re

from vista_docs.analyze.consolidate import _parse_pub_date  # type: ignore[attr-defined]
from vista_docs.analyze.corpus_manifest import ManifestRecord

_FM_RE = re.compile(r"^---\n.*?\n---\n?", re.DOTALL)
_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)


# ---------------------------------------------------------------------------
# Summary extraction (Axiom C)
# ---------------------------------------------------------------------------

_SUMMARY_MAX = 300


def extract_rn_summary(text: str) -> str:
    """
    Extract a brief prose summary from a release note document.

    Strips frontmatter, skips heading lines, returns the first non-empty
    paragraph truncated to _SUMMARY_MAX characters.

    Args:
        text: Full markdown text of the release note.

    Returns:
        Summary string (no leading/trailing whitespace), or '' if none found.
    """
    if not text:
        return ""

    # Strip frontmatter
    body = _FM_RE.sub("", text, count=1).lstrip("\n")

    # Walk paragraphs: split on blank lines, skip headings
    for block in re.split(r"\n{2,}", body):
        block = block.strip()
        if not block:
            continue
        # Skip heading-only blocks
        if _HEADING_RE.match(block):
            continue
        # Strip any inline heading prefix if block starts with one
        lines = [line for line in block.splitlines() if not _HEADING_RE.match(line)]
        prose = " ".join(lines).strip()
        if prose:
            return prose[:_SUMMARY_MAX]

    return ""


# ---------------------------------------------------------------------------
# Sort key (Axiom A)
# ---------------------------------------------------------------------------


def _sort_key(rec: ManifestRecord) -> tuple[int, int]:
    """Sort key: newest first. Unknown dates → (0, 0) → sort last."""
    year, month = _parse_pub_date(rec.pub_date)
    # Negate for descending sort; unknown (0,0) → (0,0) stays at end
    if year == 0:
        return (0, 0)
    return (-year, -month)


# ---------------------------------------------------------------------------
# CHANGELOG builder (Axioms A–E)
# ---------------------------------------------------------------------------


def build_changelog(
    app_code: str,
    records: list[ManifestRecord],
    content_map: dict[str, str],
) -> str:
    """
    Generate CHANGELOG.md content for a package.

    Args:
        app_code:    Package namespace (e.g. 'PSO').
        records:     ManifestRecords with doc_type == 'release-note' for this package.
        content_map: {original_path: markdown_text} for reading summaries.

    Returns:
        CHANGELOG.md string, sorted newest-first.
    """
    lines: list[str] = []
    lines.append(f"# {app_code} — Changelog")
    lines.append("")

    if not records:
        lines.append("_No release notes available for this package._")
        lines.append("")
        return "\n".join(lines) + "\n"

    sorted_records = sorted(records, key=_sort_key)
    # Unknown-date records end up first after negation trick → move them last
    known = [r for r in sorted_records if _parse_pub_date(r.pub_date) != (0, 0)]
    unknown = [r for r in sorted_records if _parse_pub_date(r.pub_date) == (0, 0)]
    sorted_records = known + unknown

    lines.append(
        f"_Auto-generated from **{len(records)}** release notes. "
        f"See [`originals/release-note/`](originals/release-note/) for full text._"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    for rec in sorted_records:
        heading = rec.patch_id if rec.patch_id else rec.original_path.split("/")[-1]
        date_str = rec.pub_date if rec.pub_date else "date unknown"

        lines.append(f"## {heading} — {date_str}")
        lines.append("")

        if rec.word_count:
            lines.append(f"**Words:** {rec.word_count:,}")
            lines.append("")

        # Link to original
        lines.append(f"[Full release note]({rec.original_path})")
        lines.append("")

        # Summary
        text = content_map.get(rec.original_path, "")
        summary = extract_rn_summary(text)
        if summary:
            lines.append(summary)
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines) + "\n"
