"""
Unit tests for analyze/headings.py — pure heading extraction, normalization,
and frequency profiling.

All tests operate on in-memory strings; no filesystem I/O.
"""

from vista_docs.analyze.headings import (
    BOILERPLATE,
    COMMON,
    UNIQUE,
    DocTypeProfile,
    build_profile,
    extract_headings,
    normalize_heading,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

DOC_WITH_ALL_LEVELS = """\
---
doc_type: release-note
---

# Document Title

## Introduction

### Background

#### Deep subsection

## Changes
"""

DOC_SIMPLE = """\
## Overview

## Installation Steps

### Pre-requisites

## Summary
"""

DOC_WITH_PATCH_HEADINGS = """\
## PSO*7*801 Release Notes

## Patch OR*3.0*636 Changes

## Introduction

## DG*5.3*887 Implementation Guide
"""

DOC_WITH_VERSIONS = """\
## Outpatient Pharmacy Version 7.0 Overview

## Installation Guide for Release 4.6

## Configuration v2.1 Steps

## Summary
"""

DOC_WITH_TRAILING_PARENS = """\
## Overview (Updated OR*3.0*636)

## Installation Steps (pso_7_p622)

## Summary (see also appendix a)
"""

DOC_WITH_PKG_PREFIX = """\
## CPRS: Technical Manual Overview

## PSO: Installation Requirements

## Introduction
"""

DOC_FRONTMATTER = """\
---
title: Some Document
doc_type: release-note
---

## Introduction

## Changes
"""

STUB_LIKE_DOC = """\
## Contents
"""


# ---------------------------------------------------------------------------
# TestExtractHeadings
# ---------------------------------------------------------------------------


class TestExtractHeadings:
    def test_h2_extracted(self):
        result = extract_headings("## Overview\n\n## Summary\n")
        assert result == [(2, "Overview"), (2, "Summary")]

    def test_h3_extracted(self):
        result = extract_headings("## Overview\n\n### Background\n")
        assert result == [(2, "Overview"), (3, "Background")]

    def test_h1_skipped_by_default(self):
        result = extract_headings("# Title\n\n## Body\n")
        assert result == [(2, "Body")]

    def test_h4_and_deeper_skipped_by_default(self):
        result = extract_headings(DOC_WITH_ALL_LEVELS)
        levels = [level for level, _ in result]
        assert 1 not in levels
        assert 4 not in levels

    def test_only_h2_and_h3_by_default(self):
        result = extract_headings(DOC_WITH_ALL_LEVELS)
        assert result == [(2, "Introduction"), (3, "Background"), (2, "Changes")]

    def test_frontmatter_dashes_not_parsed_as_headings(self):
        result = extract_headings(DOC_FRONTMATTER)
        texts = [t for _, t in result]
        assert "---" not in texts
        assert "doc_type: release-note" not in texts

    def test_frontmatter_headings_skipped(self):
        # The --- block should be stripped; headings inside it are not real
        result = extract_headings(DOC_FRONTMATTER)
        assert result == [(2, "Introduction"), (2, "Changes")]

    def test_empty_document(self):
        assert extract_headings("") == []

    def test_no_headings_in_range(self):
        assert extract_headings("# Title\n\nJust prose.\n") == []

    def test_custom_level_range_h1_only(self):
        result = extract_headings("# Title\n\n## Body\n", min_level=1, max_level=1)
        assert result == [(1, "Title")]

    def test_heading_text_stripped_of_trailing_spaces(self):
        result = extract_headings("## Overview   \n")
        assert result == [(2, "Overview")]


# ---------------------------------------------------------------------------
# TestNormalizeHeading
# ---------------------------------------------------------------------------


class TestNormalizeHeading:
    def test_lowercase(self):
        assert normalize_heading("INTRODUCTION") == "introduction"

    def test_plain_heading_unchanged_modulo_case(self):
        assert normalize_heading("Overview") == "overview"

    def test_strips_va_patch_identifier_ns_v_p(self):
        # OR*3.0*636 should be stripped entirely
        assert normalize_heading("OR*3.0*636 Release Notes") == "release notes"

    def test_strips_patch_identifier_integer_version(self):
        # PSO*7*801 — integer version field
        assert normalize_heading("PSO*7*801 Changes") == "changes"

    def test_strips_patch_identifier_mid_string(self):
        assert normalize_heading("Patch DG*5.3*887 Overview") == "patch overview"

    def test_strips_version_string(self):
        assert normalize_heading("Version 5.0 Overview") == "overview"

    def test_strips_version_string_mid_heading(self):
        assert normalize_heading("Pharmacy Version 7 User Manual") == "pharmacy user manual"

    def test_strips_v_dot_version(self):
        # "v2.1" — requires at least one separator so "v2" alone is not stripped
        assert normalize_heading("Configuration v2.1 Steps") == "configuration steps"

    def test_strips_release_string(self):
        assert normalize_heading("Release 4.6 Installation") == "installation"

    def test_strips_trailing_parenthetical(self):
        assert normalize_heading("Overview (Updated OR*3.0*636)") == "overview"

    def test_strips_trailing_parenthetical_plain(self):
        assert normalize_heading("Summary (see also appendix a)") == "summary"

    def test_strips_all_caps_package_prefix_before_colon(self):
        assert normalize_heading("CPRS: Technical Manual Overview") == "technical manual overview"

    def test_strips_short_package_prefix(self):
        assert normalize_heading("PSO: Installation Requirements") == "installation requirements"

    def test_does_not_strip_mixed_case_prefix(self):
        # "Kernel: Installation Guide" — "Kernel" is mixed case, should NOT be stripped
        result = normalize_heading("Kernel: Installation Guide")
        assert "kernel" in result

    def test_collapses_whitespace(self):
        assert normalize_heading("Introduction  To   The  System") == "introduction to the system"

    def test_empty_string(self):
        assert normalize_heading("") == ""

    def test_heading_that_is_only_patch_id(self):
        # After stripping the patch ID, nothing remains
        assert normalize_heading("OR*3.0*636") == ""

    def test_strips_trailing_colon(self):
        assert normalize_heading("Overview:") == "overview"

    def test_strips_trailing_dash(self):
        assert normalize_heading("Summary -") == "summary"


# ---------------------------------------------------------------------------
# TestBuildProfile
# ---------------------------------------------------------------------------


class TestBuildProfile:
    def test_returns_doc_type_profile(self):
        profile = build_profile("release-note", [DOC_SIMPLE])
        assert isinstance(profile, DocTypeProfile)
        assert profile.doc_type == "release-note"

    def test_doc_count_matches_input(self):
        profile = build_profile("release-note", [DOC_SIMPLE, DOC_SIMPLE])
        assert profile.doc_count == 2

    def test_empty_docs_list(self):
        profile = build_profile("release-note", [])
        assert profile.doc_count == 0
        assert profile.headings == []

    def test_single_doc_all_headings_are_100pct(self):
        profile = build_profile("release-note", [DOC_SIMPLE])
        assert all(r.doc_frequency == 1.0 for r in profile.headings)

    def test_heading_in_all_docs_is_boilerplate(self):
        # "overview" appears in every doc → BOILERPLATE
        doc1 = "## Overview\n\n## Unique Section A\n"
        doc2 = "## Overview\n\n## Unique Section B\n"
        doc3 = "## Overview\n\n## Unique Section C\n"
        doc4 = "## Overview\n\n## Unique Section D\n"
        doc5 = "## Overview\n\n## Unique Section E\n"
        doc6 = "## Overview\n\n## Unique Section F\n"
        doc7 = "## Overview\n\n## Unique Section G\n"
        docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7]
        profile = build_profile("release-note", docs)
        overview = next(r for r in profile.headings if r.normalized == "overview")
        assert overview.category == BOILERPLATE
        assert overview.doc_frequency == 1.0

    def test_heading_in_minority_is_unique(self):
        # "special section" in 1 of 10 docs → 10% → UNIQUE
        base = "## Introduction\n\n## Changes\n"
        special = "## Introduction\n\n## Changes\n\n## Special Section\n"
        docs = [base] * 9 + [special]
        profile = build_profile("release-note", docs)
        special_r = next(r for r in profile.headings if r.normalized == "special section")
        assert special_r.category == UNIQUE
        assert special_r.doc_count == 1
        assert special_r.doc_frequency == 0.1

    def test_heading_in_middle_band_is_common(self):
        # "background" in 4 of 10 docs → 40% → COMMON
        with_bg = "## Introduction\n\n## Background\n"
        without_bg = "## Introduction\n"
        docs = [with_bg] * 4 + [without_bg] * 6
        profile = build_profile("release-note", docs)
        bg = next(r for r in profile.headings if r.normalized == "background")
        assert bg.category == COMMON
        assert bg.doc_frequency == 0.4

    def test_heading_appearing_twice_in_one_doc_counts_once(self):
        # "overview" appears twice in doc1 but doc_count should be 1
        doc1 = "## Overview\n\nSome text.\n\n## Overview\n\nMore text.\n"
        doc2 = "## Other\n"
        profile = build_profile("release-note", [doc1, doc2])
        overview = next(r for r in profile.headings if r.normalized == "overview")
        assert overview.doc_count == 1
        assert overview.doc_frequency == 0.5

    def test_sorted_by_frequency_descending(self):
        doc_always = "## Introduction\n"
        doc_sometimes = "## Introduction\n\n## Rare\n"
        docs = [doc_always] * 8 + [doc_sometimes] * 2
        profile = build_profile("release-note", docs)
        freqs = [r.doc_frequency for r in profile.headings]
        assert freqs == sorted(freqs, reverse=True)

    def test_raw_variants_preserved(self):
        doc1 = "## PSO*7*801 Release Notes\n"
        doc2 = "## PSO*7*900 Release Notes\n"
        profile = build_profile("release-note", [doc1, doc2])
        rn = next(r for r in profile.headings if r.normalized == "release notes")
        assert len(rn.raw_variants) == 2
        assert "PSO*7*801 Release Notes" in rn.raw_variants
        assert "PSO*7*900 Release Notes" in rn.raw_variants

    def test_patch_tagged_headings_merge_to_one_normalized(self):
        # Different patch IDs → same normalized form → one HeadingRecord
        doc1 = "## OR*3.0*636 Changes\n"
        doc2 = "## OR*3.0*588 Changes\n"
        doc3 = "## OR*3.0*499 Changes\n"
        profile = build_profile("release-note", [doc1, doc2, doc3])
        changes = [r for r in profile.headings if r.normalized == "changes"]
        assert len(changes) == 1
        assert changes[0].doc_count == 3

    def test_level_counts_recorded(self):
        doc1 = "## Overview\n"
        doc2 = "### Overview\n"
        profile = build_profile("release-note", [doc1, doc2])
        overview = next(r for r in profile.headings if r.normalized == "overview")
        assert overview.level_counts.get(2, 0) >= 1
        assert overview.level_counts.get(3, 0) >= 1

    def test_custom_thresholds_respected(self):
        # With boilerplate_threshold=0.5, a heading in 5/10 docs is BOILERPLATE
        with_h = "## Section\n"
        without_h = "## Other\n"
        docs = [with_h] * 5 + [without_h] * 5
        profile = build_profile(
            "release-note",
            docs,
            boilerplate_threshold=0.5,
            unique_threshold=0.1,
        )
        section = next(r for r in profile.headings if r.normalized == "section")
        assert section.category == BOILERPLATE

    def test_frontmatter_headings_excluded(self):
        doc = "---\ntitle: Some Doc\ndoc_type: rn\n---\n\n## Introduction\n"
        profile = build_profile("release-note", [doc])
        norms = [r.normalized for r in profile.headings]
        assert "title: some doc" not in norms
        assert "introduction" in norms

    def test_unique_normalized_count(self):
        doc = "## Section A\n\n## Section B\n\n## Section C\n"
        profile = build_profile("release-note", [doc])
        assert profile.unique_normalized_count == 3

    def test_total_heading_occurrences(self):
        # 3 headings in doc1, 2 in doc2 → total 5
        doc1 = "## A\n\n## B\n\n## C\n"
        doc2 = "## A\n\n## D\n"
        profile = build_profile("release-note", [doc1, doc2])
        assert profile.total_heading_occurrences == 5
