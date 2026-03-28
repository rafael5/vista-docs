"""
I/O layer for heading frequency analysis.

Walks the markdown corpus, groups documents by doc_type, calls build_profile,
and writes JSON + Markdown report outputs.

This module is intentionally thin: all logic lives in headings.py (pure,
unit-tested). This file is excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS (inherited from headings.py — repeated here for operational clarity)
-------------------------------------------------------------------------------

A.  DOC TYPE SOURCE: doc_type is read from the markdown frontmatter field
    "doc_type". Documents with doc_type "unknown" or missing are grouped into
    a synthetic "_unknown" bucket and profiled separately. They are NOT
    excluded — their heading patterns may still reveal useful structure.

B.  STUB EXCLUSION: Documents with frontmatter field is_stub: True are
    excluded from their doc_type's profile. See headings.py Axiom 7.

C.  MINIMUM DOCUMENT COUNT: Doc types with fewer than MIN_DOCS non-stub
    documents produce a profile but are flagged with a warning in the summary.
    The caller sets MIN_DOCS (default 5). Profiles with fewer docs may have
    unreliable frequency estimates.

D.  OUTPUT STRUCTURE:
      {out_dir}/
        {doc_type}.json       — full HeadingRecord list for one doc type
        summary.md            — human-readable ranked report for all types

E.  JSON SCHEMA per doc type file:
      {
        "doc_type": str,
        "doc_count": int,
        "total_heading_occurrences": int,
        "unique_normalized_count": int,
        "boilerplate_threshold": float,
        "unique_threshold": float,
        "headings": [
          {
            "normalized": str,
            "raw_variants": [str, ...],
            "level_counts": {"2": int, "3": int},
            "doc_count": int,
            "doc_frequency": float,
            "category": "BOILERPLATE" | "COMMON" | "UNIQUE"
          },
          ...
        ]
      }
    Keys in level_counts are strings (JSON requires string keys).
"""

from __future__ import annotations

import json
import logging
import re
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

from vista_docs.analyze.headings import (
    BOILERPLATE,
    BOILERPLATE_THRESHOLD,
    COMMON,
    UNIQUE,
    UNIQUE_THRESHOLD,
    DocTypeProfile,
    build_profile,
)

log = logging.getLogger(__name__)

# Minimum non-stub documents to include a doc type in the summary report.
# Types below this threshold are still written to JSON but flagged.
MIN_DOCS: int = 5

# Regex patterns for frontmatter field extraction
_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FIELD_RE = re.compile(r"^(\w+):\s*(.+?)\s*$", re.MULTILINE)


def _parse_fm_field(text: str, field: str) -> str:
    """Extract a single field value from YAML frontmatter. Returns '' if absent."""
    fm_match = _FM_RE.match(text)
    if not fm_match:
        return ""
    for m in _FIELD_RE.finditer(fm_match.group(1)):
        if m.group(1) == field:
            return m.group(2).strip().strip('"').strip("'")
    return ""


def _is_stub(text: str) -> bool:
    val = _parse_fm_field(text, "is_stub")
    return val.lower() in ("true", "1", "yes")


def _doc_type(text: str) -> str:
    dt = _parse_fm_field(text, "doc_type")
    return dt if dt else "_unknown"


def run_heading_analysis(
    markdown_dir: Path,
    out_dir: Path,
    min_docs: int = MIN_DOCS,
    boilerplate_threshold: float = BOILERPLATE_THRESHOLD,
    unique_threshold: float = UNIQUE_THRESHOLD,
) -> dict[str, DocTypeProfile]:
    """
    Analyze heading frequencies across all doc types in the corpus.

    Reads every *.md file under markdown_dir, groups by doc_type from
    frontmatter, calls build_profile for each group, writes JSON and
    summary Markdown to out_dir.

    Args:
        markdown_dir:          Root of the markdown corpus.
        out_dir:               Directory to write output files (created if absent).
        min_docs:              Minimum non-stub docs to include a type in the
                               summary report (Axiom C). Types below this
                               threshold are still written to JSON.
        boilerplate_threshold: Passed through to build_profile.
        unique_threshold:      Passed through to build_profile.

    Returns:
        Dict of {doc_type: DocTypeProfile} for all doc types found.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    # Collect texts by doc_type
    buckets: dict[str, list[str]] = defaultdict(list)
    stub_counts: dict[str, int] = defaultdict(int)
    total_files = 0

    for md_path in sorted(markdown_dir.rglob("*.md")):
        total_files += 1
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            log.warning("Could not read %s: %s", md_path, e)
            continue

        dt = _doc_type(text)
        if _is_stub(text):
            stub_counts[dt] += 1
            continue
        buckets[dt].append(text)

    log.info(
        "Loaded %d files across %d doc types (%d stubs excluded)",
        total_files,
        len(buckets),
        sum(stub_counts.values()),
    )

    profiles: dict[str, DocTypeProfile] = {}

    for doc_type, texts in sorted(buckets.items()):
        if len(texts) < 1:
            continue
        profile = build_profile(
            doc_type,
            texts,
            boilerplate_threshold=boilerplate_threshold,
            unique_threshold=unique_threshold,
        )
        profiles[doc_type] = profile
        _write_json(out_dir / f"{_safe_filename(doc_type)}.json", profile)
        log.info(
            "%-25s  docs=%4d  headings=%4d  boilerplate=%3d  unique=%4d",
            doc_type,
            profile.doc_count,
            profile.unique_normalized_count,
            sum(1 for r in profile.headings if r.category == BOILERPLATE),
            sum(1 for r in profile.headings if r.category == UNIQUE),
        )

    _write_summary(out_dir / "summary.md", profiles, min_docs=min_docs)
    log.info("Summary written to %s", out_dir / "summary.md")

    return profiles


def _safe_filename(doc_type: str) -> str:
    """Convert a doc_type string to a safe filesystem name."""
    return re.sub(r"[^a-z0-9_\-]", "_", doc_type.lower())


def _write_json(path: Path, profile: DocTypeProfile) -> None:
    """Serialize a DocTypeProfile to JSON."""
    data = asdict(profile)
    # JSON requires string keys in objects; convert int level keys
    for h in data["headings"]:
        h["level_counts"] = {str(k): v for k, v in h["level_counts"].items()}
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _write_summary(
    path: Path,
    profiles: dict[str, DocTypeProfile],
    min_docs: int,
) -> None:
    """Write a human-readable Markdown summary report."""
    lines: list[str] = []
    lines.append("# VistA Corpus — Heading Frequency Analysis")
    lines.append("")
    lines.append(
        "Headings are classified by how frequently they appear across all "
        "documents of a given type:\n"
        f"- **BOILERPLATE** ≥ {BOILERPLATE_THRESHOLD:.0%} of docs — "
        "structural convention; skip when looking for unique content\n"
        f"- **COMMON** {UNIQUE_THRESHOLD:.0%}–{BOILERPLATE_THRESHOLD:.0%} — "
        "present in a significant minority; may contain useful content\n"
        f"- **UNIQUE** ≤ {UNIQUE_THRESHOLD:.0%} of docs — "
        "the highest-information headings; likely to contain novel content"
    )
    lines.append("")

    # TOC
    lines.append("## Table of Contents")
    lines.append("")
    for dt in sorted(profiles):
        anchor = _safe_filename(dt)
        lines.append(f"- [{dt}](#{anchor})")
    lines.append("")
    lines.append("---")
    lines.append("")

    for dt in sorted(profiles):
        p = profiles[dt]
        anchor = _safe_filename(dt)
        lines.append(f'<a id="{anchor}"></a>')
        lines.append("")
        lines.append(f"## {dt}")
        lines.append("")
        lines.append("[Back to TOC](#table-of-contents)")
        lines.append("")

        if p.doc_count < min_docs:
            lines.append(
                f"> ⚠️ Only {p.doc_count} document(s) — frequency estimates "
                "unreliable (minimum is {min_docs})."
            )
            lines.append("")

        bp = [r for r in p.headings if r.category == BOILERPLATE]
        cm = [r for r in p.headings if r.category == COMMON]
        uq = [r for r in p.headings if r.category == UNIQUE]

        lines.append(
            f"**{p.doc_count} documents** · "
            f"{p.unique_normalized_count} distinct headings · "
            f"{len(bp)} boilerplate · "
            f"{len(cm)} common · "
            f"{len(uq)} unique"
        )
        lines.append("")

        # Boilerplate table
        if bp:
            lines.append("### BOILERPLATE Headings")
            lines.append("")
            lines.append(
                "_These headings appear in ≥"
                f"{p.boilerplate_threshold:.0%} of documents. "
                "They are structural conventions of this doc type — "
                "safe to skip when diff-ing for unique content._"
            )
            lines.append("")
            lines.append("| Heading | Docs | Freq | Example Raw Forms |")
            lines.append("|---------|------|------|-------------------|")
            for r in bp:
                variants = "; ".join(r.raw_variants[:3])
                lines.append(
                    f"| `{r.normalized}` | {r.doc_count} | {r.doc_frequency:.0%} | {variants} |"
                )
            lines.append("")

        # Common table (collapsed — top 20 only for readability)
        if cm:
            show_cm = cm[:20]
            lines.append("### COMMON Headings")
            lines.append("")
            lines.append(
                f"_Present in {p.unique_threshold:.0%}–"
                f"{p.boilerplate_threshold:.0%} of documents. "
                "These headings indicate recurring but non-universal patterns._"
            )
            if len(cm) > 20:
                lines.append(f"_(Showing top 20 of {len(cm)} — see JSON for full list.)_")
            lines.append("")
            lines.append("| Heading | Docs | Freq |")
            lines.append("|---------|------|------|")
            for r in show_cm:
                lines.append(f"| `{r.normalized}` | {r.doc_count} | {r.doc_frequency:.0%} |")
            lines.append("")

        # Unique section — show only top 30 by doc_count (descending within unique)
        if uq:
            # Sort unique by doc_count desc (most-common unique first)
            uq_sorted = sorted(uq, key=lambda r: r.doc_count, reverse=True)
            show_uq = uq_sorted[:30]
            lines.append("### UNIQUE Headings (sample — highest doc-count first)")
            lines.append("")
            lines.append(
                f"_Present in ≤{p.unique_threshold:.0%} of documents. "
                "These are the highest-information headings — "
                "they appear only in a minority of documents and are "
                "most likely to contain novel, doc-specific content._"
            )
            if len(uq) > 30:
                lines.append(f"_(Showing top 30 of {len(uq)} — see JSON for full list.)_")
            lines.append("")
            lines.append("| Heading | Docs | Freq | Example Raw Form |")
            lines.append("|---------|------|------|------------------|")
            for r in show_uq:
                variant = r.raw_variants[0] if r.raw_variants else ""
                lines.append(
                    f"| `{r.normalized}` | {r.doc_count} | {r.doc_frequency:.1%} | {variant} |"
                )
            lines.append("")

        lines.append("---")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
