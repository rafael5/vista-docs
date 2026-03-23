"""
Unit tests for enrich/extractors.py — Cycle 2 extractors.

Covers: pub_date (extended), package_name, package_namespace,
        package_version, audience, figure_count.

Fixtures mirror real Docling output from VDL release notes and TMs.
"""

from vista_docs.enrich.extractors import (
    extract_audience,
    extract_figure_count,
    extract_package_name,
    extract_package_namespace,
    extract_package_version,
    extract_pub_date,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

# Release note: date is bold, appears AFTER an H2 title heading
RELEASE_NOTE_TITLE = """\
## Enrollment System Modernization (ESM) Phase 2   VistA REE

**DG*5.3*1006**

### Release Notes

<!-- image -->

**March 2020**

**Department of Veterans Affairs**
"""

# Technical manual: date is plain text on its own line before any heading
TM_TITLE_PAGE = """\
<!-- image -->

Inpatient Medications

Technical Manual/Security Guide

Department of Veterans Affairs

October 2023

Office of Information and Technology
"""

# Setup guide: date is bold on its own line
SETUP_GUIDE_TITLE = """\
<!-- image -->

**CPRS Setup Guide**

**June 2021**

Veterans Health Administration
"""

NO_DATE = """\
## Introduction

This document describes the system configuration.
No date is present in this document.
"""

# Package name: "Full Name (CODE)" pattern on title page
TITLE_WITH_PARENS = """\
<!-- image -->

Computerized Patient Record System (CPRS)

INSTALLATION GUIDE

April 2007
"""

TITLE_INPATIENT = """\
<!-- image -->

Inpatient Medications

Technical Manual
"""

# Audience section patterns
AUDIENCE_H2 = """\
## Introduction

Some intro text.

## Audience

This document targets IRM staff and VistA system administrators responsible
for installation and maintenance.

## Overview

More content here.
"""

INTENDED_AUDIENCE_H3 = """\
### Intended Audience

The intended audiences are Provider Systems, Health Systems Design
and Development (HSD&D) staff, and Software Quality Assurance (SQA) staff.

### Document Conventions
"""

NO_AUDIENCE = """\
## Introduction

No audience section present.

## Configuration
"""

# Figure patterns: TOC entries have tab+page, body captions do not
FIGURES_TOC_AND_BODY = """\
Table of Contents

Figure 1: Login Screen\t5
Figure 2: Patient List\t6
Figure 3: Order Entry Dialog\t8

## Introduction

Some body text here.

Figure 1: Login Screen

Figure 2: Patient List

Figure 3: Order Entry Dialog
"""

FIGURES_BODY_ONLY = """\
## Chapter 1

Figure 1: Address Confirmation Prompts

Some description here.

Figure 2: Phone Number Change Dialog

More text.

Figure 10: Summary Screen
"""

NO_FIGURES = """\
## Introduction

No figures in this document. Just tables and text.
"""


# ---------------------------------------------------------------------------
# pub_date extended — release notes with bold dates after H2 title heading
# ---------------------------------------------------------------------------


class TestExtractPubDateExtended:
    def test_bold_date_after_h2(self):
        """Release note pattern: **March 2020** after H2 title heading."""
        assert extract_pub_date(RELEASE_NOTE_TITLE) == "March 2020"

    def test_plain_date_in_tm(self):
        assert extract_pub_date(TM_TITLE_PAGE) == "October 2023"

    def test_bold_date_in_setup_guide(self):
        assert extract_pub_date(SETUP_GUIDE_TITLE) == "June 2021"

    def test_no_date_returns_empty(self):
        assert extract_pub_date(NO_DATE) == ""


# ---------------------------------------------------------------------------
# package_name
# ---------------------------------------------------------------------------


class TestExtractPackageName:
    def test_extracts_name_before_parens(self):
        result = extract_package_name(TITLE_WITH_PARENS)
        assert result == "Computerized Patient Record System"

    def test_returns_empty_when_no_parens_pattern(self):
        # No "(CODE)" pattern in title page
        result = extract_package_name(TITLE_INPATIENT)
        assert result == ""

    def test_empty_doc_returns_empty(self):
        assert extract_package_name("") == ""


# ---------------------------------------------------------------------------
# package_namespace — derived from patch field in frontmatter
# ---------------------------------------------------------------------------


FRONTMATTER_OR = """\
---
title: CPRS Technical Manual
app_code: CPRS
patch: OR*3.0*636
---

Body content.
"""

FRONTMATTER_DG = """\
---
title: ADT Release Notes
app_code: ADT
patch: DG*5.3*1057
---

Body.
"""

FRONTMATTER_NO_PATCH = """\
---
title: Some Doc
app_code: CPRS
---

Body.
"""

FRONTMATTER_SHORT_PATCH = """\
---
title: Inpatient Meds
app_code: PSJ
patch: PSJ*5*423
---

Body.
"""


class TestExtractPackageNamespace:
    def test_extracts_or_from_patch(self):
        assert extract_package_namespace(FRONTMATTER_OR) == "OR"

    def test_extracts_dg_from_patch(self):
        assert extract_package_namespace(FRONTMATTER_DG) == "DG"

    def test_multi_part_patch(self):
        assert extract_package_namespace(FRONTMATTER_SHORT_PATCH) == "PSJ"

    def test_no_patch_returns_empty(self):
        assert extract_package_namespace(FRONTMATTER_NO_PATCH) == ""


# ---------------------------------------------------------------------------
# package_version — derived from patch field
# ---------------------------------------------------------------------------


class TestExtractPackageVersion:
    def test_version_with_decimal(self):
        assert extract_package_version(FRONTMATTER_OR) == "3.0"

    def test_version_dg(self):
        assert extract_package_version(FRONTMATTER_DG) == "5.3"

    def test_version_without_decimal(self):
        assert extract_package_version(FRONTMATTER_SHORT_PATCH) == "5"

    def test_no_patch_returns_empty(self):
        assert extract_package_version(FRONTMATTER_NO_PATCH) == ""


# ---------------------------------------------------------------------------
# audience
# ---------------------------------------------------------------------------


class TestExtractAudience:
    def test_h2_audience_section(self):
        result = extract_audience(AUDIENCE_H2)
        assert "IRM staff" in result
        assert "administrator" in result.lower()

    def test_intended_audience_h3(self):
        result = extract_audience(INTENDED_AUDIENCE_H3)
        assert "Provider Systems" in result or "HSD" in result

    def test_no_audience_returns_empty(self):
        assert extract_audience(NO_AUDIENCE) == ""

    def test_truncated_to_300_chars(self):
        result = extract_audience(AUDIENCE_H2)
        assert len(result) <= 300

    def test_empty_doc_returns_empty(self):
        assert extract_audience("") == ""


# ---------------------------------------------------------------------------
# figure_count
# ---------------------------------------------------------------------------


class TestExtractFigureCount:
    def test_deduplicates_toc_and_body(self):
        """TOC + body both list same figures — should count unique figure numbers."""
        assert extract_figure_count(FIGURES_TOC_AND_BODY) == 3

    def test_body_only_figures(self):
        assert extract_figure_count(FIGURES_BODY_ONLY) == 3

    def test_no_figures(self):
        assert extract_figure_count(NO_FIGURES) == 0

    def test_counts_double_digit_figures(self):
        md = "Figure 10: Some screen\n\nFigure 11: Another screen\n"
        assert extract_figure_count(md) >= 2
