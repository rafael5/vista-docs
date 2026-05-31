"""Integration tests for the corpus-wide validate runner (filesystem I/O)."""

from __future__ import annotations

import csv

from vista_docs.validate.frontmatter import safe_dump_frontmatter
from vista_docs.validate.runner import (
    format_summary,
    validate_tree,
    write_flags_csv,
)


def _clean_fm():
    return {
        "title": "XU Technical Manual",
        "doc_type": "TM",
        "doc_label": "Technical Manual",
        "app_code": "XU",
        "app_name": "Kernel",
        "section": "INF",
        "pkg_ns": "XU",
    }


def _write(path, fm_yaml_body, body="content\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{fm_yaml_body}---\n{body}", encoding="utf-8")


def test_validate_tree_all_clean(tmp_path):
    _write(tmp_path / "inf" / "xu" / "tm.md", safe_dump_frontmatter(_clean_fm()))
    _write(tmp_path / "inf" / "xu" / "ug.md", safe_dump_frontmatter(_clean_fm()))
    report = validate_tree(tmp_path)
    assert report.total == 2
    assert report.clean == 2
    assert report.hard_failures == 0
    assert report.ok


def test_validate_tree_skips_index_and_readme(tmp_path):
    _write(tmp_path / "inf" / "xu" / "tm.md", safe_dump_frontmatter(_clean_fm()))
    (tmp_path / "INDEX.md").write_text("# Index\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# Readme\n", encoding="utf-8")
    report = validate_tree(tmp_path)
    assert report.total == 1
    assert report.ok


def test_validate_tree_flags_invalid_and_missing(tmp_path):
    # invalid YAML
    _write(tmp_path / "a" / "bad.md", 'title: "x \\3"\ndescription: "k: v"\n  - oops\n')
    # missing section + legacy schema
    _write(tmp_path / "a" / "legacy.md", "consolidated_title: x\nmaster_source: y\napp_code: ADT\n")
    # clean
    _write(tmp_path / "a" / "ok.md", safe_dump_frontmatter(_clean_fm()))
    report = validate_tree(tmp_path)
    assert report.total == 3
    assert report.hard_failures == 2
    assert not report.ok
    codes = report.by_code
    assert codes["invalid_yaml"] >= 1
    assert codes["legacy_schema"] >= 1


def test_write_flags_csv_and_summary(tmp_path):
    _write(tmp_path / "a" / "legacy.md", "consolidated_title: x\nmaster_source: y\n")
    report = validate_tree(tmp_path)
    csv_path = tmp_path / "out" / "flags.csv"
    write_flags_csv(report, csv_path)
    rows = list(csv.DictReader(csv_path.open()))
    assert rows
    assert {"rel_path", "code", "severity", "detail"} == set(rows[0].keys())
    summary = format_summary(report)
    assert "hard failures" in summary
    assert "Validated 1 documents" in summary
