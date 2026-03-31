"""
I/O layer for document consolidation.

Reads the markdown corpus, groups documents by (app_code, doc_type,
normalized_title), runs consolidate_group on each multi-member group,
and writes consolidated markdown + a summary report to out_dir.

This module is intentionally thin: all logic lives in consolidate.py and
diff.py (pure, unit-tested). This file is excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS (operational, inherited from consolidate.py)
-------------------------------------------------------------------------------

A.  ONLY MULTI-MEMBER GROUPS ARE WRITTEN.
    Groups with a single document are skipped — there is nothing to
    consolidate. Their count is reported in the summary.

B.  OUTPUT STRUCTURE:
      {out_dir}/
        {app_code}/
          {doc_type}/
            {safe_group_title}.md      — consolidated master + appendices
        consolidation_summary.md       — per-group statistics report

C.  CONSOLIDATED DOCUMENT FORMAT:
      YAML frontmatter with provenance fields (master_source, consolidated_from,
      version_sources), then the full master text verbatim, then a markdown
      appendix section containing all unique sections labelled by source.

D.  MINIMUM GROUP SIZE: groups with exactly 1 member are skipped (Axiom A).
    The --min-versions flag (default 2) controls this threshold. Setting it
    to 1 would write every document unchanged, which is not useful.

E.  WORD_COUNT AND PUB_DATE are read from frontmatter fields. Missing values
    default to 0 and "" respectively — these still sort deterministically
    (anchor layer wins regardless).
"""

from __future__ import annotations

import logging
import re
import shutil
from pathlib import Path

from vista_docs.analyze.consolidate import (
    ConsolidationResult,
    DocumentRecord,
    UniqueSection,
    consolidate_group,
    group_documents,
)

log = logging.getLogger(__name__)

# Frontmatter field extractors (reuse simple regex pattern)
_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FIELD_RE = re.compile(r"^(\w+):\s*(.+?)\s*$", re.MULTILINE)


def _fm_field(text: str, field: str) -> str:
    m = _FM_RE.match(text)
    if not m:
        return ""
    for fm in _FIELD_RE.finditer(m.group(1)):
        if fm.group(1) == field:
            return fm.group(2).strip().strip('"').strip("'")
    return ""


def _fm_int(text: str, field: str) -> int:
    val = _fm_field(text, field)
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0


def _safe_name(s: str) -> str:
    """Convert a string to a safe filesystem name."""
    return re.sub(r"[^a-z0-9_\-]", "_", s.lower()).strip("_")[:80]


def run_consolidation(
    markdown_dir: Path,
    out_dir: Path,
    min_versions: int = 2,
    doc_types: list[str] | None = None,
) -> dict[str, ConsolidationResult]:
    """
    Consolidate all multi-version document groups in the markdown corpus.

    Args:
        markdown_dir:  Root of the markdown corpus (*.md files walked recursively).
        out_dir:       Directory to write consolidated files (created if absent).
        min_versions:  Minimum group size to consolidate (default 2).
        doc_types:     If provided, only consolidate these doc types. None = all.

    Returns:
        Dict of {group_key: ConsolidationResult} for all consolidated groups.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load all documents
    records: list[DocumentRecord] = []
    total_files = 0

    for md_path in sorted(markdown_dir.rglob("*.md")):
        total_files += 1
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            log.warning("Could not read %s: %s", md_path, e)
            continue

        doc_type = _fm_field(text, "doc_type")
        app_code = _fm_field(text, "app_code")
        title = _fm_field(text, "title")

        if not doc_type or not app_code or not title:
            continue
        if doc_types and doc_type not in doc_types:
            continue

        records.append(
            DocumentRecord(
                path=str(md_path),
                title=title,
                doc_type=doc_type,
                app_code=app_code,
                word_count=_fm_int(text, "word_count"),
                pub_date=_fm_field(text, "pub_date"),
                doc_layer=_fm_field(text, "doc_layer"),
                text=text,
            )
        )

    log.info("Loaded %d documents from %d files", len(records), total_files)

    groups = group_documents(records)
    multi = [g for g in groups if len(g.members) >= min_versions]
    single = len(groups) - len(multi)

    log.info(
        "Groups: %d total, %d multi-version (≥%d), %d single-doc (skipped)",
        len(groups),
        len(multi),
        min_versions,
        single,
    )

    results: dict[str, ConsolidationResult] = {}

    for group in multi:
        group_key = f"{group.app_code}:{group.doc_type}:{group.group_title}"
        try:
            result = consolidate_group(group)
        except Exception as e:
            log.error("Failed to consolidate %s: %s", group_key, e)
            continue

        results[group_key] = result

        # Write output file
        type_dir = out_dir / _safe_name(group.app_code) / _safe_name(group.doc_type)
        type_dir.mkdir(parents=True, exist_ok=True)
        out_path = type_dir / f"{_safe_name(group.group_title)}.md"
        _write_consolidated(out_path, result)

        # Copy sibling image directories from every member alongside the output file
        for member in result.group.members:
            src_img_dir = Path(member.path).with_suffix("")
            if src_img_dir.is_dir():
                dest_img_dir = type_dir / src_img_dir.name
                if dest_img_dir.exists():
                    shutil.rmtree(dest_img_dir)
                shutil.copytree(src_img_dir, dest_img_dir)

        log.info(
            "%-20s %-25s  members=%3d  addenda=%3d  → %s",
            group.app_code,
            group.doc_type,
            len(group.members),
            len(result.addenda),
            out_path.relative_to(out_dir),
        )

    _write_summary(out_dir / "consolidation_summary.md", results, single_count=single)
    log.info("Summary written to %s", out_dir / "consolidation_summary.md")

    return results


def _write_consolidated(path: Path, result: ConsolidationResult) -> None:
    """Write a consolidated markdown file: provenance frontmatter + master + appendices."""
    lines: list[str] = []

    # Provenance frontmatter
    version_list = "\n".join(
        f'  - "{d.title}"' for d in result.group.members if d is not result.master
    )
    lines.append("---")
    lines.append(f'consolidated_title: "{result.group.group_title}"')
    lines.append(f"app_code: {result.group.app_code}")
    lines.append(f"doc_type: {result.group.doc_type}")
    lines.append(f'master_source: "{result.master.title}"')
    lines.append(f"master_pub_date: {result.master.pub_date}")
    lines.append(f"consolidated_from: {len(result.group.members)} versions")
    if version_list:
        lines.append("prior_versions:")
        lines.append(version_list)
    lines.append("---")
    lines.append("")

    # Master document (strip its own frontmatter — we replaced it above)
    master_body = _FM_RE.sub("", result.master_text, count=1).lstrip("\n")
    lines.append(master_body)

    # Appendices
    if result.addenda:
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Appendix: Unique Sections from Prior Versions")
        lines.append("")
        lines.append(
            "_These sections appeared in earlier versions of this document "
            "but are not present in the current master. They may describe "
            "features, procedures, or configurations that were removed, "
            "superseded, or restructured._"
        )
        lines.append("")

        # Group addenda by source title
        by_source: dict[str, list[UniqueSection]] = {}
        for s in result.addenda:
            by_source.setdefault(s.source_title, []).append(s)

        for source_title, sections in by_source.items():
            lines.append(f"### From: {source_title}")
            lines.append("")
            for s in sections:
                lines.append(s.content)
                lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def _write_summary(
    path: Path,
    results: dict[str, ConsolidationResult],
    single_count: int,
) -> None:
    """Write a Markdown summary report of all consolidations."""
    lines: list[str] = []
    lines.append("# VistA Corpus — Consolidation Summary")
    lines.append("")
    lines.append(
        f"**{len(results)}** multi-version groups consolidated · "
        f"**{single_count}** single-document groups skipped"
    )
    lines.append("")

    # Stats
    total_members = sum(len(r.group.members) for r in results.values())
    total_addenda = sum(len(r.addenda) for r in results.values())
    lines.append(
        f"Total documents consolidated: **{total_members}** → **{len(results)}** master files  "
    )
    lines.append(f"Total unique addendum sections preserved: **{total_addenda}**")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per doc-type breakdown
    by_type: dict[str, list[ConsolidationResult]] = {}
    for r in results.values():
        by_type.setdefault(r.group.doc_type, []).append(r)

    lines.append("## By Document Type")
    lines.append("")
    lines.append("| Doc Type | Groups | Total Docs | Addendum Sections |")
    lines.append("|----------|--------|------------|-------------------|")
    for dt in sorted(by_type):
        rs = by_type[dt]
        total_docs = sum(len(r.group.members) for r in rs)
        total_add = sum(len(r.addenda) for r in rs)
        lines.append(f"| {dt} | {len(rs)} | {total_docs} | {total_add} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Full table
    lines.append("## All Groups")
    lines.append("")
    lines.append("| Package | Doc Type | Group Title | Versions | Master | Addenda Sections |")
    lines.append("|---------|----------|-------------|----------|--------|-----------------|")
    for r in sorted(results.values(), key=lambda x: (x.group.app_code, x.group.doc_type)):
        lines.append(
            f"| {r.group.app_code} | {r.group.doc_type} "
            f"| {r.group.group_title[:50]} "
            f"| {len(r.group.members)} "
            f"| {r.master.title[:50]} "
            f"| {len(r.addenda)} |"
        )
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
