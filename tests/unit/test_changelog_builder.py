"""
Unit tests for migrate/changelog_builder.py — CHANGELOG entry building,
pub_date sorting, summary extraction, and full CHANGELOG generation.

All tests use in-memory strings and ManifestRecord objects; no filesystem I/O.
"""

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.changelog_builder import (
    build_changelog,
    extract_rn_summary,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _rn_rec(
    *,
    package: str = "PSO",
    patch_id: str = "PSO*7.0*507",
    pub_date: str = "January 2022",
    original_path: str = "originals/release-note/PSO_PSO_7_0_507_RN_rn.md",
    word_count: int = 1500,
    doc_layer: str = "patch",
) -> ManifestRecord:
    return ManifestRecord(
        package=package,
        repo=f"vista-{package.lower()}",
        original_path=original_path,
        original_sha256="a" * 64,
        source_markdown_path=f"/data/{package}/rn.md",
        doc_type="release-note",
        doc_layer=doc_layer,
        pub_date=pub_date,
        patch_id=patch_id,
        word_count=word_count,
        transformation="release-note",
        consolidated_master="",
        consolidated_role="",
    )


_RN_TEXT = """\
---
title: PSO*7.0*507 Release Notes
doc_type: release-note
patch_id: PSO*7.0*507
pub_date: January 2022
---

## Overview

This patch introduces new drug interaction checking capabilities and updates
the formulary management workflow. Pharmacists will notice improved performance
when processing high-volume prescription queues.

## New Features

### Drug Interaction Checking

Enhanced algorithms for detecting major drug-drug interactions.

## Fixes

- Resolved issue with refill date calculation for controlled substances.
"""

_MINIMAL_RN = """\
---
title: Short Note
---

Brief content only.
"""


# ---------------------------------------------------------------------------
# TestExtractRnSummary
# ---------------------------------------------------------------------------


class TestExtractRnSummary:
    def test_strips_frontmatter(self):
        summary = extract_rn_summary(_RN_TEXT)
        assert "doc_type:" not in summary
        assert "patch_id:" not in summary

    def test_returns_first_paragraph_content(self):
        summary = extract_rn_summary(_RN_TEXT)
        assert "drug interaction" in summary.lower() or "patch" in summary.lower()

    def test_truncated_to_reasonable_length(self):
        summary = extract_rn_summary(_RN_TEXT)
        assert len(summary) <= 400

    def test_empty_doc_returns_empty(self):
        assert extract_rn_summary("") == ""

    def test_frontmatter_only_returns_empty(self):
        doc = "---\ntitle: Test\npatch_id: X\n---\n"
        result = extract_rn_summary(doc)
        assert result == ""

    def test_heading_lines_not_in_summary(self):
        summary = extract_rn_summary(_RN_TEXT)
        # The summary should not start with a heading marker
        assert not summary.startswith("#")

    def test_minimal_content(self):
        summary = extract_rn_summary(_MINIMAL_RN)
        assert "Brief content" in summary

    def test_no_leading_trailing_whitespace(self):
        summary = extract_rn_summary(_RN_TEXT)
        assert summary == summary.strip()


# ---------------------------------------------------------------------------
# TestBuildChangelog
# ---------------------------------------------------------------------------


class TestBuildChangelog:
    def _records(self) -> list[ManifestRecord]:
        return [
            _rn_rec(
                patch_id="PSO*7.0*500",
                pub_date="March 2019",
                original_path="originals/release-note/PSO_PSO_7_0_500_RN_.md",
            ),
            _rn_rec(
                patch_id="PSO*7.0*507",
                pub_date="January 2022",
                original_path="originals/release-note/PSO_PSO_7_0_507_RN_.md",
            ),
            _rn_rec(
                patch_id="PSO*7.0*519",
                pub_date="June 2023",
                original_path="originals/release-note/PSO_PSO_7_0_519_RN_.md",
            ),
        ]

    def _content_map(self) -> dict[str, str]:
        return {
            "originals/release-note/PSO_PSO_7_0_500_RN_.md": _MINIMAL_RN,
            "originals/release-note/PSO_PSO_7_0_507_RN_.md": _RN_TEXT,
            "originals/release-note/PSO_PSO_7_0_519_RN_.md": _MINIMAL_RN,
        }

    def test_returns_string(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert isinstance(cl, str)

    def test_ends_with_newline(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert cl.endswith("\n")

    def test_contains_package_name(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "PSO" in cl

    def test_newest_entry_appears_first(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        pos_519 = cl.index("7.0*519")
        pos_500 = cl.index("7.0*500")
        assert pos_519 < pos_500

    def test_all_patch_ids_present(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "PSO*7.0*500" in cl
        assert "PSO*7.0*507" in cl
        assert "PSO*7.0*519" in cl

    def test_pub_dates_present(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "2019" in cl
        assert "2022" in cl
        assert "2023" in cl

    def test_links_to_original_files(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "originals/release-note/" in cl

    def test_summary_content_included(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        # _RN_TEXT summary should appear
        assert "drug interaction" in cl.lower() or "patch" in cl.lower()

    def test_empty_records_returns_placeholder(self):
        cl = build_changelog("PSO", [], {})
        assert "PSO" in cl
        assert "no release notes" in cl.lower() or "0" in cl

    def test_unknown_pub_date_sorts_last(self):
        records = self._records() + [
            _rn_rec(
                patch_id="PSO*7.0*999",
                pub_date="",
                original_path="originals/release-note/PSO_PSO_7_0_999_RN_.md",
            )
        ]
        cl = build_changelog("PSO", records, self._content_map())
        pos_519 = cl.index("7.0*519")
        pos_999 = cl.index("7.0*999")
        # Unknown date should be at the end (after known dates)
        assert pos_519 < pos_999

    def test_record_count_in_header(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "3" in cl

    def test_missing_content_graceful(self):
        # Content map doesn't have all entries — should not crash
        cl = build_changelog("PSO", self._records(), {})
        assert "PSO*7.0*507" in cl

    def test_no_frontmatter_in_output(self):
        cl = build_changelog("PSO", self._records(), self._content_map())
        assert "doc_type:" not in cl
        assert "patch_id:" not in cl
