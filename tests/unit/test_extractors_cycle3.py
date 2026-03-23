"""
Unit tests for enrich/extractors.py — Cycle 3 extractors.

Covers: word_count, is_stub, has_toc, patch_number, description,
        file_numbers, security_keys, menu_options.

Fixtures mirror real Docling output from VA VDL DOCX files.
"""

from vista_docs.enrich.extractors import (
    extract_description,
    extract_file_numbers,
    extract_has_toc,
    extract_is_stub,
    extract_menu_options,
    extract_patch_number,
    extract_security_keys,
    extract_word_count,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_FRONTMATTER = """\
---
title: CPRS Technical Manual
doc_type: technical-manual
app_code: CPRS
patch: OR*3.0*636
---
"""

TOC_DOC = """\
---
title: Some TM
patch: OR*3.0*636
---

Table of Contents

Introduction\t1
Configuration\t5
Appendix A\t42
"""

NO_TOC_DOC = """\
---
title: Release Notes
patch: OR*3.0*636
---

## Overview

No table of contents here, just prose.
"""

RICH_BODY = """\
---
title: CPRS Technical Manual
patch: OR*3.0*636
---

## Introduction

This document describes the Computerized Patient Record System technical
configuration and installation requirements for VistA administrators.
System managers should read this guide before deploying or configuring
the CPRS graphical user interface on any VistA host system.

## Configuration

This section covers the required setup steps including kernel parameter
configuration, device setup, terminal type assignments, and security key
assignment for all users who will access the CPRS GUI application.
"""

STUB_DOC = """\
---
title: Stub Doc
patch: OR*3.0*636
---

## Introduction

Stub content.
"""

OVERVIEW_DOC = """\
---
title: ADT TM
patch: DG*5.3*1057
---

## Overview

This module provides patient registration and admission, discharge,
and transfer (ADT) functionality within the VistA hospital information
system. It is used by registrars, ward clerks, and clinical staff.

## Configuration
"""

NO_INTRO_DOC = """\
---
title: Some Doc
patch: OR*3.0*636
---

## Step 1: Pre-Installation

Before beginning, ensure that the target system meets the minimum hardware
requirements listed in the VistA system requirements document published
by the Office of Information Technology.

## Step 2: Installation
"""

FILE_NUMBERS_DOC = """\
---
title: ADT TM
patch: DG*5.3*1057
---

## FileMan Files

This package uses File #2 (Patient), File #44 (Hospital Location),
and File #405 (Registration). It also modifies File #2 in several routines.
See File #200 (New Person) for user definitions.
"""

NO_FILE_NUMBERS_DOC = """\
---
title: Release Notes
patch: OR*3.0*636
---

This document describes changes in this patch. No FileMan file references.
"""

SECURITY_KEYS_TABLE_DOC = """\
---
title: CPRS TM
patch: OR*3.0*636
---

## Security

### Security Keys

The following security keys are exported with this package:

| Security Key | Description |
|---|---|
| OR CPRS GUI CHART | Allows access to CPRS GUI |
| ORES | Allows order entry |
| ORELSE | Allows release of orders |

## Menu Options
"""

SECURITY_KEYS_LIST_DOC = """\
---
title: PSJ TM
patch: PSJ*5*423
---

### Security Keys

- PSGW VERIFY - Allows pharmacy verification
- PSJ PHARM TECH - Pharmacy technician access
- PSJI MGR - Inpatient meds manager key

## Options
"""

NO_SECURITY_KEYS_DOC = """\
---
title: Release Notes
patch: OR*3.0*636
---

## Overview

No security keys in this document.
"""

MENU_OPTIONS_DOC = """\
---
title: CPRS TM
patch: OR*3.0*636
---

## Menu Options

The following options are exported:

| Option Name | Description |
|---|---|
| [OR CPRS GUI CHART] | Main CPRS chart access |
| [OR CPRS REPORT] | CPRS reporting |
| [ORES SIGN] | Order signing |

You can also access [OR CPRS GUI CHART] from the patient context menu.
"""

NO_MENU_OPTIONS_DOC = """\
---
title: Release Notes
patch: OR*3.0*636
---

## Overview

No menu options documented here.
"""


# ---------------------------------------------------------------------------
# word_count
# ---------------------------------------------------------------------------


class TestExtractWordCount:
    def test_counts_body_words(self):
        result = extract_word_count(RICH_BODY)
        assert result > 20

    def test_frontmatter_not_counted(self):
        # Doc with only frontmatter and minimal body
        md = _FRONTMATTER + "\nHello world.\n"
        result = extract_word_count(md)
        # Should count "Hello world" (2), not frontmatter keys
        assert result < 10

    def test_empty_returns_zero(self):
        assert extract_word_count("") == 0

    def test_stub_has_low_count(self):
        assert extract_word_count(STUB_DOC) < 20


# ---------------------------------------------------------------------------
# is_stub
# ---------------------------------------------------------------------------


class TestExtractIsStub:
    def test_stub_doc_is_stub(self):
        assert extract_is_stub(STUB_DOC) is True

    def test_rich_doc_is_not_stub(self):
        assert extract_is_stub(RICH_BODY) is False

    def test_empty_is_stub(self):
        assert extract_is_stub("") is True


# ---------------------------------------------------------------------------
# has_toc
# ---------------------------------------------------------------------------


class TestExtractHasToc:
    def test_detects_toc(self):
        assert extract_has_toc(TOC_DOC) is True

    def test_no_toc_returns_false(self):
        assert extract_has_toc(NO_TOC_DOC) is False

    def test_empty_returns_false(self):
        assert extract_has_toc("") is False


# ---------------------------------------------------------------------------
# patch_number
# ---------------------------------------------------------------------------


class TestExtractPatchNumber:
    def test_three_part_patch(self):
        assert extract_patch_number(_FRONTMATTER) == "636"

    def test_two_part_patch(self):
        md = "---\npatch: PSJ*5*423\n---\n"
        assert extract_patch_number(md) == "423"

    def test_decimal_version_patch(self):
        md = "---\npatch: DG*5.3*1057\n---\n"
        assert extract_patch_number(md) == "1057"

    def test_no_patch_returns_empty(self):
        assert extract_patch_number("---\ntitle: No Patch\n---\n") == ""


# ---------------------------------------------------------------------------
# description
# ---------------------------------------------------------------------------


class TestExtractDescription:
    def test_extracts_from_introduction(self):
        result = extract_description(RICH_BODY)
        assert "Computerized Patient Record System" in result or "VistA" in result

    def test_extracts_from_overview(self):
        result = extract_description(OVERVIEW_DOC)
        assert "ADT" in result or "registration" in result.lower()

    def test_falls_back_to_body_when_no_intro(self):
        result = extract_description(NO_INTRO_DOC)
        assert len(result) > 0

    def test_truncated_to_300_chars(self):
        result = extract_description(RICH_BODY)
        assert len(result) <= 300

    def test_empty_returns_empty(self):
        assert extract_description("") == ""

    def test_stub_may_return_empty(self):
        # Very short stub doc — description may be empty or very short
        result = extract_description(STUB_DOC)
        assert len(result) <= 300


# ---------------------------------------------------------------------------
# file_numbers
# ---------------------------------------------------------------------------


class TestExtractFileNumbers:
    def test_extracts_unique_sorted(self):
        result = extract_file_numbers(FILE_NUMBERS_DOC)
        assert result == ["2", "44", "200", "405"]

    def test_deduplicates(self):
        # File #2 appears twice in FILE_NUMBERS_DOC
        result = extract_file_numbers(FILE_NUMBERS_DOC)
        assert result.count("2") == 1

    def test_no_file_numbers(self):
        assert extract_file_numbers(NO_FILE_NUMBERS_DOC) == []

    def test_empty_returns_empty(self):
        assert extract_file_numbers("") == []


# ---------------------------------------------------------------------------
# security_keys
# ---------------------------------------------------------------------------


class TestExtractSecurityKeys:
    def test_extracts_from_table(self):
        result = extract_security_keys(SECURITY_KEYS_TABLE_DOC)
        assert "OR CPRS GUI CHART" in result
        assert "ORES" in result
        assert "ORELSE" in result

    def test_extracts_from_list(self):
        result = extract_security_keys(SECURITY_KEYS_LIST_DOC)
        assert "PSGW VERIFY" in result
        assert "PSJ PHARM TECH" in result
        assert "PSJI MGR" in result

    def test_returns_sorted(self):
        result = extract_security_keys(SECURITY_KEYS_TABLE_DOC)
        assert result == sorted(result)

    def test_no_section_returns_empty(self):
        assert extract_security_keys(NO_SECURITY_KEYS_DOC) == []

    def test_empty_returns_empty(self):
        assert extract_security_keys("") == []


# ---------------------------------------------------------------------------
# menu_options
# ---------------------------------------------------------------------------


class TestExtractMenuOptions:
    def test_counts_bracketed_options(self):
        # [OR CPRS GUI CHART] appears twice — deduplicated to 1
        # [OR CPRS REPORT] and [ORES SIGN] each appear once
        result = extract_menu_options(MENU_OPTIONS_DOC)
        assert result == 3

    def test_deduplicates_repeated_options(self):
        # [OR CPRS GUI CHART] appears twice in the fixture
        result = extract_menu_options(MENU_OPTIONS_DOC)
        # Should be 3 unique, not 4
        assert result == 3

    def test_no_options_returns_zero(self):
        assert extract_menu_options(NO_MENU_OPTIONS_DOC) == 0

    def test_empty_returns_zero(self):
        assert extract_menu_options("") == 0
