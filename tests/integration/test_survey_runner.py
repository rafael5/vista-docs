"""
Integration tests for survey/analyzer.py — run_survey() I/O layer.

Uses real temp directories and real markdown files.
"""

import csv
import json

import pytest

from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry
from vista_docs.survey.analyzer import run_survey

pytestmark = pytest.mark.integration


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_FRONTMATTER = """\
---
title: {title}
doc_type: {doc_type}
app_code: {app_code}
patch: {patch}
---
"""

_RICH_BODY = """\
## Overview

Some introductory text here. This document covers many topics.

## Configuration

| Column A | Column B |
|----------|----------|
| value 1  | value 2  |

More content here with enough words to be meaningful across the corpus.
"""

_STUB_BODY = ""


def _make_entries_and_files(tmp_path):
    """Write 3 markdown files and return corresponding ManifestEntries."""
    md_dir = tmp_path / "markdown"

    specs = [
        dict(
            app_code="CPRS",
            doc_title="CPRS Technical Manual",
            doc_type=DocType.TECHNICAL_MANUAL,
            patch="OR*3.0*636",
            filename="cprs-technical-manual.md",
            body=_RICH_BODY,
        ),
        dict(
            app_code="CPRS",
            doc_title="CPRS Installation Guide",
            doc_type=DocType.INSTALLATION_GUIDE,
            patch="",
            filename="cprs-installation-guide.md",
            body=_STUB_BODY,
        ),
        dict(
            app_code="ADT",
            doc_title="ADT User Manual",
            doc_type=DocType.USER_MANUAL,
            patch="",
            filename="adt-user-manual.md",
            body=_RICH_BODY,
        ),
    ]

    entries = []
    for s in specs:
        pkg_dir = md_dir / s["app_code"]
        pkg_dir.mkdir(parents=True, exist_ok=True)
        md_path = pkg_dir / s["filename"]
        fm = _FRONTMATTER.format(
            title=s["doc_title"],
            doc_type=s["doc_type"].value,
            app_code=s["app_code"],
            patch=s["patch"],
        )
        md_path.write_text(fm + s["body"])

        entries.append(
            ManifestEntry(
                package_id=f"{s['app_code']}*1.0",
                app_code=s["app_code"],
                doc_title=s["doc_title"],
                doc_type=s["doc_type"],
                patch=s["patch"],
                output_filename=s["filename"],
                fetch_status=FetchStatus.OK,
                ingest_status=FetchStatus.OK,
                markdown_path=str(md_path),
            )
        )
    return md_dir, entries


# ---------------------------------------------------------------------------
# run_survey
# ---------------------------------------------------------------------------


class TestRunSurveyOutputs:
    def test_returns_dict(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        result = run_survey(md_dir, entries, out_dir)
        assert isinstance(result, dict)

    def test_returns_counts(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        result = run_survey(md_dir, entries, out_dir)
        assert "ok" in result
        assert "errors" in result
        assert "stubs" in result
        assert result["ok"] == 3

    def test_creates_output_dir(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey" / "nested"
        run_survey(md_dir, entries, out_dir)
        assert out_dir.exists()

    def test_writes_summary_json(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        assert (out_dir / "survey-summary.json").exists()

    def test_writes_stubs_csv(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        assert (out_dir / "survey-stubs.csv").exists()

    def test_writes_enrichment_csv(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        assert (out_dir / "survey-enrichment.csv").exists()


class TestRunSurveySummaryJson:
    def test_summary_json_is_valid(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert isinstance(data, dict)

    def test_summary_total_docs(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert data["total_docs"] == 3

    def test_summary_total_stubs(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert data["total_stubs"] == 1

    def test_summary_has_by_package(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert "by_package" in data
        assert "CPRS" in data["by_package"]
        assert "ADT" in data["by_package"]

    def test_summary_has_by_doc_type(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert "by_doc_type" in data


class TestRunSurveyCsvContents:
    def test_enrichment_csv_has_headers(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        with open(out_dir / "survey-enrichment.csv", newline="") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
        assert headers is not None
        assert "app_code" in headers
        assert "word_count" in headers
        assert "is_stub" in headers

    def test_enrichment_csv_row_count(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        with open(out_dir / "survey-enrichment.csv", newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 3

    def test_stubs_csv_has_headers(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        with open(out_dir / "survey-stubs.csv", newline="") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
        assert headers is not None
        assert "app_code" in headers
        assert "doc_title" in headers

    def test_stubs_csv_row_count(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir)
        with open(out_dir / "survey-stubs.csv", newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 1


class TestRunSurveyFiltering:
    def test_pkg_filter_limits_docs(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        result = run_survey(md_dir, entries, out_dir, pkg="ADT")
        assert result["ok"] == 1

    def test_pkg_filter_summary_only_has_that_pkg(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        out_dir = tmp_path / "survey"
        run_survey(md_dir, entries, out_dir, pkg="ADT")
        data = json.loads((out_dir / "survey-summary.json").read_text())
        assert "ADT" in data["by_package"]
        assert "CPRS" not in data["by_package"]

    def test_skips_entries_not_ok(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        # Mark one entry as pending
        from dataclasses import replace

        entries[0] = replace(entries[0], ingest_status=FetchStatus.PENDING)
        out_dir = tmp_path / "survey"
        result = run_survey(md_dir, entries, out_dir)
        assert result["ok"] == 2


class TestRunSurveyErrorHandling:
    def test_missing_markdown_file_counts_as_error(self, tmp_path):
        md_dir, entries = _make_entries_and_files(tmp_path)
        # Point one entry to a nonexistent file
        from dataclasses import replace

        entries[0] = replace(
            entries[0],
            markdown_path="/nonexistent/path/file.md",
            output_filename="nonexistent.md",
        )
        out_dir = tmp_path / "survey"
        result = run_survey(md_dir, entries, out_dir)
        assert result["errors"] == 1
        assert result["ok"] == 2
