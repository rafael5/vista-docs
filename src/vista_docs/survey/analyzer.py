"""I/O thin layer: survey enriched markdown corpus → reports."""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

from vista_docs.models.manifest import FetchStatus, ManifestEntry
from vista_docs.survey.stats import DocStats, analyze_doc, summarize_corpus

logger = logging.getLogger(__name__)

ENRICHMENT_FIELDNAMES = [
    "app_code",
    "doc_title",
    "doc_type",
    "patch",
    "md_path",
    "line_count",
    "word_count",
    "heading_count",
    "table_count",
    "callout_count",
    "is_stub",
]

STUB_FIELDNAMES = [
    "app_code",
    "doc_title",
    "doc_type",
    "patch",
    "word_count",
    "md_path",
]


def build_enrichment_row(stats: DocStats, md_path: str) -> dict:
    """Build a per-document row for survey-enrichment.csv."""
    return {
        "app_code": stats.app_code,
        "doc_title": stats.doc_title,
        "doc_type": stats.doc_type,
        "patch": stats.patch,
        "md_path": md_path,
        "line_count": stats.line_count,
        "word_count": stats.word_count,
        "heading_count": stats.heading_count,
        "table_count": stats.table_count,
        "callout_count": stats.callout_count,
        "is_stub": stats.is_stub,
    }


def build_stub_row(stats: DocStats, md_path: str) -> dict:
    """Build a row for survey-stubs.csv (stub documents only)."""
    return {
        "app_code": stats.app_code,
        "doc_title": stats.doc_title,
        "doc_type": stats.doc_type,
        "patch": stats.patch,
        "word_count": stats.word_count,
        "md_path": md_path,
    }


def run_survey(
    markdown_dir: Path,
    entries: list[ManifestEntry],
    out_dir: Path,
    pkg: str = "",
) -> dict:
    """
    Walk enriched markdown files, analyze each, write 3 reports.

    Reports written to out_dir:
      survey-summary.json     — corpus-wide aggregate stats
      survey-stubs.csv        — stub documents for quality review
      survey-enrichment.csv   — per-document row of all stats

    Returns {ok, errors, stubs}.
    """
    to_survey = [e for e in entries if e.ingest_status == FetchStatus.OK]
    if pkg:
        to_survey = [e for e in to_survey if e.app_code.upper() == pkg.upper()]

    all_stats: list[DocStats] = []
    enrichment_rows: list[dict] = []
    ok = errors = 0

    for entry in to_survey:
        md_path = _resolve_md_path(markdown_dir, entry)
        if not md_path.exists():
            logger.warning("Markdown file not found: %s", md_path)
            errors += 1
            continue

        try:
            md = md_path.read_text(encoding="utf-8")
            stats = analyze_doc(md, entry)
        except Exception as exc:
            logger.warning("Failed to analyze %s: %s", md_path, exc)
            errors += 1
            continue

        all_stats.append(stats)
        enrichment_rows.append(build_enrichment_row(stats, str(md_path)))
        ok += 1

    summary = summarize_corpus(all_stats)
    stub_rows = [
        build_stub_row(s, r["md_path"]) for s, r in zip(all_stats, enrichment_rows) if s.is_stub
    ]

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / "survey-summary.json", summary)
    _write_csv(out_dir / "survey-stubs.csv", STUB_FIELDNAMES, stub_rows)
    _write_csv(out_dir / "survey-enrichment.csv", ENRICHMENT_FIELDNAMES, enrichment_rows)

    logger.info(
        "Survey complete: %d ok, %d errors, %d stubs → %s",
        ok,
        errors,
        len(stub_rows),
        out_dir,
    )
    return {"ok": ok, "errors": errors, "stubs": len(stub_rows)}


def _resolve_md_path(markdown_dir: Path, entry: ManifestEntry) -> Path:
    """Resolve the markdown file path for an entry."""
    if entry.markdown_path:
        return Path(entry.markdown_path)
    return markdown_dir / entry.app_code / entry.output_filename


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
