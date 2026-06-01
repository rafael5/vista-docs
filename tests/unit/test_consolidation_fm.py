"""
Unit tests for consolidation_runner._fm_field — frontmatter field extraction.

Regression guard: an empty-valued field (e.g. `doc_subject:`) must NOT swallow the
field on the following line. The old `\\s*(.+?)\\s*$` regex matched newlines in
MULTILINE mode, so an empty value consumed the next line — dropping `app_code` and
silently excluding the doc from consolidation grouping.
"""

from vista_docs.analyze.consolidation_runner import _fm_field

# Frontmatter with an empty `doc_subject` immediately before `app_code` — the exact
# shape the enrich stage emits for the CPRS GUI user manual.
_FM = """---
title: "CPRS User Manual: GUI Version (Updated OR*3.0*499)"
doc_type: UM
doc_subject:
app_code: CPRS
app_name: Computerized Patient Record System
---

Body text here.
"""


class TestFmFieldEmptyValue:
    def test_field_after_empty_value_is_not_swallowed(self):
        # The bug: doc_subject (empty) ate the app_code line.
        assert _fm_field(_FM, "app_code") == "CPRS"

    def test_empty_field_reads_as_empty(self):
        assert _fm_field(_FM, "doc_subject") == ""

    def test_surrounding_fields_still_parse(self):
        assert _fm_field(_FM, "doc_type") == "UM"
        assert _fm_field(_FM, "app_name") == "Computerized Patient Record System"
        assert _fm_field(_FM, "title") == "CPRS User Manual: GUI Version (Updated OR*3.0*499)"

    def test_missing_field_returns_empty(self):
        assert _fm_field(_FM, "nonexistent") == ""
