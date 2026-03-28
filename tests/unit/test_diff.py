"""
Unit tests for analyze/diff.py — normalized heading diff between two markdown texts.

All tests use in-memory strings; no filesystem I/O.
"""

from vista_docs.analyze.diff import HeadingDiff, diff_headings

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

DOC_A = """\
## Introduction
Some text.
## Background
Details.
### Subsection
More.
## Summary
"""

DOC_B = """\
## Introduction
Different text.
## New Section
Added.
## Summary
"""

DOC_WITH_PATCH = """\
## PSO*7*801 Release Notes
## Introduction
## Changes
"""

DOC_WITHOUT_PATCH = """\
## Release Notes
## Introduction
## Summary
"""

DOC_FRONTMATTER = """\
---
title: Some Doc
doc_type: TM
---
## Introduction
## Configuration
"""

DOC_EMPTY = ""

DOC_H3_ONLY = """\
### Overview
### Details
"""

DOC_IDENTICAL = """\
## Introduction
## Configuration
## Summary
"""


# ---------------------------------------------------------------------------
# TestHeadingDiffBasic
# ---------------------------------------------------------------------------


class TestHeadingDiffBasic:
    def test_returns_heading_diff(self):
        result = diff_headings(DOC_A, DOC_B)
        assert isinstance(result, HeadingDiff)

    def test_added_headings(self):
        # "new section" in B but not A
        result = diff_headings(DOC_A, DOC_B)
        assert "new section" in result.added

    def test_removed_headings(self):
        # "background" in A but not B
        result = diff_headings(DOC_A, DOC_B)
        assert "background" in result.removed

    def test_common_headings(self):
        # "introduction" and "summary" in both
        result = diff_headings(DOC_A, DOC_B)
        assert "introduction" in result.common
        assert "summary" in result.common

    def test_added_not_in_common(self):
        result = diff_headings(DOC_A, DOC_B)
        assert not (set(result.added) & set(result.common))

    def test_removed_not_in_common(self):
        result = diff_headings(DOC_A, DOC_B)
        assert not (set(result.removed) & set(result.common))

    def test_added_not_in_removed(self):
        result = diff_headings(DOC_A, DOC_B)
        assert not (set(result.added) & set(result.removed))

    def test_identical_docs_no_added_or_removed(self):
        result = diff_headings(DOC_IDENTICAL, DOC_IDENTICAL)
        assert result.added == []
        assert result.removed == []
        assert len(result.common) == 3

    def test_empty_a_all_added(self):
        result = diff_headings(DOC_EMPTY, DOC_A)
        assert set(result.added) == {"introduction", "background", "subsection", "summary"}
        assert result.removed == []
        assert result.common == []

    def test_empty_b_all_removed(self):
        result = diff_headings(DOC_A, DOC_EMPTY)
        # DOC_A has introduction, background, subsection (H3), summary
        assert set(result.removed) == {"introduction", "background", "subsection", "summary"}
        assert result.added == []

    def test_both_empty(self):
        result = diff_headings(DOC_EMPTY, DOC_EMPTY)
        assert result.added == []
        assert result.removed == []
        assert result.common == []


# ---------------------------------------------------------------------------
# TestNormalizationInDiff
# ---------------------------------------------------------------------------


class TestNormalizationInDiff:
    def test_patch_ids_normalized_before_comparison(self):
        # Both "PSO*7*801 Release Notes" and "Release Notes" normalize to "release notes"
        result = diff_headings(DOC_WITH_PATCH, DOC_WITHOUT_PATCH)
        assert "release notes" in result.common

    def test_subsection_h3_included_in_diff(self):
        # "subsection" is H3 in DOC_A, not in DOC_B
        result = diff_headings(DOC_A, DOC_B)
        assert "subsection" in result.removed

    def test_frontmatter_not_diffed(self):
        result = diff_headings(DOC_FRONTMATTER, DOC_A)
        # frontmatter fields like "title" should not appear
        assert "title: some doc" not in result.common
        assert "title: some doc" not in result.added
        assert "title: some doc" not in result.removed

    def test_version_strings_normalized_before_comparison(self):
        doc_v1 = "## Configuration Version 5.3 Overview\n## Summary\n"
        doc_v2 = "## Configuration Version 7.0 Overview\n## Summary\n"
        result = diff_headings(doc_v1, doc_v2)
        # Both normalize to "configuration overview" → common
        assert "configuration overview" in result.common
        assert result.added == []


# ---------------------------------------------------------------------------
# TestRawVariants
# ---------------------------------------------------------------------------


class TestRawVariants:
    def test_added_raw_variants_present(self):
        result = diff_headings(DOC_A, DOC_B)
        assert "new section" in result.added_raw
        assert len(result.added_raw["new section"]) >= 1

    def test_removed_raw_variants_present(self):
        result = diff_headings(DOC_A, DOC_B)
        assert "background" in result.removed_raw
        assert "Background" in result.removed_raw["background"]

    def test_raw_variant_is_original_casing(self):
        # Raw variant should preserve the original heading text
        doc = "## INTRODUCTION\n## Summary\n"
        result = diff_headings(doc, DOC_EMPTY)
        assert "introduction" in result.removed_raw
        assert "INTRODUCTION" in result.removed_raw["introduction"]

    def test_patch_id_heading_raw_variant_preserved(self):
        result = diff_headings(DOC_WITH_PATCH, DOC_WITHOUT_PATCH)
        # "release notes" came from "PSO*7*801 Release Notes" in A and "Release Notes" in B
        assert "release notes" in result.common_raw
        raws = result.common_raw["release notes"]
        assert any("PSO" in r for r in raws) or any(r == "Release Notes" for r in raws)


# ---------------------------------------------------------------------------
# TestDiffSymmetry
# ---------------------------------------------------------------------------


class TestDiffSymmetry:
    def test_added_in_a_b_is_removed_in_b_a(self):
        ab = diff_headings(DOC_A, DOC_B)
        ba = diff_headings(DOC_B, DOC_A)
        assert set(ab.added) == set(ba.removed)
        assert set(ab.removed) == set(ba.added)
        assert set(ab.common) == set(ba.common)
