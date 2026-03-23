"""
Unit tests for enrich/extractors.py — pure metadata extraction from markdown.

Fixtures are trimmed excerpts that mirror real Docling output from VDL documents.
No filesystem I/O.
"""

from vista_docs.enrich.extractors import (
    extract_appendices,
    extract_keywords,
    extract_page_count,
    extract_pub_date,
    extract_revision_history,
    extract_section_count,
    extract_table_count,
)

# ---------------------------------------------------------------------------
# Shared fixtures (real VDL patterns)
# ---------------------------------------------------------------------------

# Title-page block: date appears as bold or plain text near the top
TITLE_PAGE = """
<!-- image -->

Computerized Patient Record System (CPRS)

INSTALLATION GUIDE


April 2007


Technical Services
"""

TITLE_PAGE_BOLD = """
**DG*5.3*1006**

### Release Notes

**March 2020**

**Department of Veterans Affairs**
"""

TITLE_PAGE_ISO = """
CPRS Technical Manual

2023-10-19

Office of Information Technology
"""

# TOC block: section title <tab> page number
TOC_BLOCK = """
Table of Contents

Introduction\t6

Pre-Install Instructions\t7

Installation\t24

Release Notes\t78

Appendix A: Define CONSULTS\t118

Appendix B: Hardware Requirements\t124
"""

TOC_ROMAN = """
Table of Contents

Introduction\ti

Overview\tii

Chapter 1\t1

Appendix A\t45
"""

# Revision history table (real VDL pattern)
REVISION_TABLE = """
Revision History

| Date     | Page | Change                          |
|----------|------|---------------------------------|
| 4/30/07  | 75   | Revised section about CPRSUpdate|
| 6/7/06   | 124  | Added hardware link             |
| 12/30/04 | var  | Minor SOP compliance changes    |
| 10/14/98 | 35   | Removed ORPURGE TASK step       |
"""

REVISION_TABLE_ISO = """
| Date       | Patch      | Description                     |
|------------|------------|---------------------------------|
| 2023-10-19 | OR*3.0*636 | Updated order check parameters  |
| 2022-09-01 | OR*3.0*588 | Added SMART imaging support     |
| 2020-06-02 | OR*3.0*377 | Added parameter definitions     |
"""

# Body with headings, tables, appendices
RICH_BODY = """
## Introduction

Some content here.

## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| timeout | 30    | Seconds     |

### Subsection

> **NOTE:** Important note here.

## Installation

More content.

| Package | Version |
|---------|---------|
| OR      | 3.0     |

## Appendix A: Setup Details

Appendix content here.

## Appendix B: Reference Tables

More appendix content.
"""

KEYWORDS_BODY = """
## Overview

The Computerized Patient Record System (CPRS) provides order entry and
results reporting for VistA. Clinicians can enter pharmacy orders, laboratory
orders, and radiology orders through CPRS. The graphical user interface
displays patient data including vitals, allergies, and problem lists.
Order checks prevent duplicate orders and drug interactions.
"""


# ---------------------------------------------------------------------------
# Cycle 1: pub_date
# ---------------------------------------------------------------------------


class TestExtractPubDate:
    def test_month_year_plain(self):
        assert extract_pub_date(TITLE_PAGE) == "April 2007"

    def test_month_year_bold(self):
        assert extract_pub_date(TITLE_PAGE_BOLD) == "March 2020"

    def test_iso_date(self):
        assert extract_pub_date(TITLE_PAGE_ISO) == "2023-10-19"

    def test_returns_empty_when_not_found(self):
        assert extract_pub_date("## Just a heading\n\nSome body text.") == ""

    def test_scans_top_of_doc_only(self):
        # Date buried deep in body (beyond line 60) should not be returned
        deep = "## Introduction\n\n" + ("word\n" * 65) + "\nJanuary 2010\n"
        assert extract_pub_date(deep) == ""


# ---------------------------------------------------------------------------
# Cycle 2: page_count
# ---------------------------------------------------------------------------


class TestExtractPageCount:
    def test_finds_last_page_number(self):
        # Last TOC entry is page 124
        assert extract_page_count(TOC_BLOCK) == 124

    def test_ignores_roman_numerals(self):
        # Roman numeral pages (i, ii) are front matter — last real page is 45
        assert extract_page_count(TOC_ROMAN) == 45

    def test_returns_zero_when_no_toc(self):
        assert extract_page_count("## Just content\n\nNo table of contents.") == 0


# ---------------------------------------------------------------------------
# Cycle 3: revision_history
# ---------------------------------------------------------------------------


class TestExtractRevisionHistory:
    def test_count_us_date_format(self):
        result = extract_revision_history(REVISION_TABLE)
        assert result["count"] == 4

    def test_oldest_date(self):
        result = extract_revision_history(REVISION_TABLE)
        assert result["oldest"] == "10/14/98"

    def test_newest_date(self):
        result = extract_revision_history(REVISION_TABLE)
        assert result["newest"] == "4/30/07"

    def test_iso_dates(self):
        result = extract_revision_history(REVISION_TABLE_ISO)
        assert result["count"] == 3
        assert result["oldest"] == "2020-06-02"
        assert result["newest"] == "2023-10-19"

    def test_no_revision_table(self):
        result = extract_revision_history("## Introduction\n\nNo revisions here.")
        assert result["count"] == 0
        assert result["oldest"] == ""
        assert result["newest"] == ""


# ---------------------------------------------------------------------------
# Cycle 4: appendices
# ---------------------------------------------------------------------------


class TestExtractAppendices:
    def test_counts_appendix_headings(self):
        assert extract_appendices(RICH_BODY) == 2

    def test_toc_appendix_entries(self):
        # TOC has 2 appendix lines
        assert extract_appendices(TOC_BLOCK) == 2

    def test_no_appendices(self):
        assert extract_appendices("## Intro\n\n## Config\n\n## Install\n") == 0


# ---------------------------------------------------------------------------
# Cycle 5: table_count
# ---------------------------------------------------------------------------


class TestExtractTableCount:
    def test_counts_separator_rows(self):
        assert extract_table_count(RICH_BODY) == 2

    def test_revision_table_counted(self):
        assert extract_table_count(REVISION_TABLE) == 1

    def test_no_tables(self):
        assert extract_table_count("## Heading\n\nJust prose.") == 0


# ---------------------------------------------------------------------------
# Cycle 6: section_count
# ---------------------------------------------------------------------------


class TestExtractSectionCount:
    def test_counts_h2_headings(self):
        # RICH_BODY has: Introduction, Configuration, Installation, Appendix A, Appendix B = 5
        assert extract_section_count(RICH_BODY) == 5

    def test_ignores_h3_and_deeper(self):
        md = "## Top\n\n### Sub\n\n#### Deep\n\n## Another Top\n"
        assert extract_section_count(md) == 2

    def test_no_sections(self):
        assert extract_section_count("Just prose here.") == 0


# ---------------------------------------------------------------------------
# Cycle 7: keywords
# ---------------------------------------------------------------------------


class TestExtractKeywords:
    def test_returns_list(self):
        result = extract_keywords(KEYWORDS_BODY)
        assert isinstance(result, list)

    def test_returns_up_to_ten(self):
        result = extract_keywords(KEYWORDS_BODY)
        assert len(result) <= 10

    def test_domain_terms_present(self):
        result = extract_keywords(KEYWORDS_BODY)
        # High-frequency domain terms should surface
        joined = " ".join(result).lower()
        assert any(term in joined for term in ["order", "cprs", "vista", "pharmacy"])

    def test_stopwords_excluded(self):
        result = extract_keywords(KEYWORDS_BODY)
        stopwords = {"the", "and", "for", "are", "can", "that", "this", "with"}
        assert not any(w.lower() in stopwords for w in result)

    def test_empty_body_returns_empty(self):
        assert extract_keywords("") == []
