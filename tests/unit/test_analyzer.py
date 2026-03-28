"""
Unit tests for survey/analyzer.py — pure helper functions.

No filesystem I/O. Tests row-building helpers and fieldname constants.
"""

from vista_docs.survey.analyzer import (
    ENRICHMENT_FIELDNAMES,
    STUB_FIELDNAMES,
    build_enrichment_row,
    build_stub_row,
)
from vista_docs.survey.stats import DocStats

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_STATS = DocStats(
    app_code="CPRS",
    doc_title="CPRS Technical Manual",
    doc_type="technical-manual",
    patch="OR*3.0*636",
    line_count=500,
    word_count=4000,
    heading_count=20,
    table_count=5,
    callout_count=3,
    is_stub=False,
)

_STUB_STATS = DocStats(
    app_code="ADT",
    doc_title="ADT Installation Guide",
    doc_type="installation-guide",
    patch="",
    line_count=8,
    word_count=20,
    heading_count=0,
    table_count=0,
    callout_count=0,
    is_stub=True,
)


# ---------------------------------------------------------------------------
# build_enrichment_row
# ---------------------------------------------------------------------------


class TestBuildEnrichmentRow:
    def test_returns_dict(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert isinstance(row, dict)

    def test_contains_app_code(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["app_code"] == "CPRS"

    def test_contains_doc_title(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["doc_title"] == "CPRS Technical Manual"

    def test_contains_doc_type(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["doc_type"] == "technical-manual"

    def test_contains_patch(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["patch"] == "OR*3.0*636"

    def test_contains_md_path(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["md_path"] == "CPRS/cprs-technical-manual.md"

    def test_contains_counts(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["line_count"] == 500
        assert row["word_count"] == 4000
        assert row["heading_count"] == 20
        assert row["table_count"] == 5
        assert row["callout_count"] == 3

    def test_contains_is_stub(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert row["is_stub"] is False

    def test_keys_match_fieldnames(self):
        row = build_enrichment_row(_STATS, "CPRS/cprs-technical-manual.md")
        assert set(row.keys()) == set(ENRICHMENT_FIELDNAMES)


# ---------------------------------------------------------------------------
# build_stub_row
# ---------------------------------------------------------------------------


class TestBuildStubRow:
    def test_returns_dict(self):
        row = build_stub_row(_STUB_STATS, "ADT/adt-installation-guide.md")
        assert isinstance(row, dict)

    def test_contains_required_fields(self):
        row = build_stub_row(_STUB_STATS, "ADT/adt-installation-guide.md")
        assert row["app_code"] == "ADT"
        assert row["doc_title"] == "ADT Installation Guide"
        assert row["doc_type"] == "installation-guide"
        assert row["word_count"] == 20
        assert row["md_path"] == "ADT/adt-installation-guide.md"

    def test_keys_match_fieldnames(self):
        row = build_stub_row(_STUB_STATS, "ADT/adt-installation-guide.md")
        assert set(row.keys()) == set(STUB_FIELDNAMES)


# ---------------------------------------------------------------------------
# Fieldname constants
# ---------------------------------------------------------------------------


class TestFieldnames:
    def test_enrichment_fieldnames_is_list(self):
        assert isinstance(ENRICHMENT_FIELDNAMES, list)
        assert len(ENRICHMENT_FIELDNAMES) > 0

    def test_stub_fieldnames_is_list(self):
        assert isinstance(STUB_FIELDNAMES, list)
        assert len(STUB_FIELDNAMES) > 0

    def test_enrichment_includes_is_stub(self):
        assert "is_stub" in ENRICHMENT_FIELDNAMES

    def test_enrichment_includes_word_count(self):
        assert "word_count" in ENRICHMENT_FIELDNAMES

    def test_stub_includes_word_count(self):
        assert "word_count" in STUB_FIELDNAMES
