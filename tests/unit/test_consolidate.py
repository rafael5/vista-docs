"""
Unit tests for analyze/consolidate.py — master selection, document grouping,
section content extraction, and consolidation result assembly.

All tests use in-memory strings and DocumentRecord objects; no filesystem I/O.
"""

from vista_docs.analyze.consolidate import (
    ConsolidationGroup,
    ConsolidationResult,
    DocumentRecord,
    UniqueSection,
    consolidate_group,
    extract_unique_sections,
    group_documents,
    normalize_title,
    select_master,
)

# ---------------------------------------------------------------------------
# Fixtures — DocumentRecord helpers
# ---------------------------------------------------------------------------


def _doc(
    title: str,
    *,
    path: str = "/fake/path.md",
    doc_type: str = "technical-manual",
    app_code: str = "PSO",
    word_count: int = 1000,
    pub_date: str = "January 2020",
    doc_layer: str = "plain",
    text: str = "",
) -> DocumentRecord:
    return DocumentRecord(
        path=path,
        title=title,
        doc_type=doc_type,
        app_code=app_code,
        word_count=word_count,
        pub_date=pub_date,
        doc_layer=doc_layer,
        text=text,
    )


# ---------------------------------------------------------------------------
# TestNormalizeTitle
# ---------------------------------------------------------------------------


class TestNormalizeTitle:
    def test_strips_version_number(self):
        assert normalize_title("PSO Outpatient Pharmacy 7.0 User Manual") == normalize_title(
            "PSO Outpatient Pharmacy User Manual"
        )

    def test_strips_patch_id(self):
        assert normalize_title("OR*3.0*636 Release Notes") == normalize_title("Release Notes")

    def test_strips_gui_version(self):
        assert normalize_title("VSE GUI 1.7.1 Technical Manual") == normalize_title(
            "VSE GUI 1.7.64 Technical Manual"
        )

    def test_bare_single_version_number_stripped(self):
        # "Version 5.3" → stripped
        assert normalize_title("PIMS Version 5.3 Technical Manual") == normalize_title(
            "PIMS Technical Manual"
        )

    def test_different_subjects_not_equal(self):
        assert normalize_title("Outpatient Pharmacy User Manual") != normalize_title(
            "Inpatient Pharmacy User Manual"
        )

    def test_empty_string(self):
        assert normalize_title("") == ""


# ---------------------------------------------------------------------------
# TestSelectMaster
# ---------------------------------------------------------------------------


class TestSelectMaster:
    def test_anchor_wins_over_higher_word_count(self):
        anchor = _doc("Doc A", doc_layer="anchor", word_count=500)
        plain = _doc("Doc B", doc_layer="plain", word_count=9999)
        assert select_master([anchor, plain]) is anchor

    def test_anchor_wins_over_newer_date(self):
        anchor = _doc("Doc A", doc_layer="anchor", pub_date="January 2010")
        plain = _doc("Doc B", doc_layer="plain", pub_date="December 2023")
        assert select_master([anchor, plain]) is anchor

    def test_multiple_anchors_picks_highest_word_count(self):
        a1 = _doc("Doc A", doc_layer="anchor", word_count=500)
        a2 = _doc("Doc B", doc_layer="anchor", word_count=800)
        assert select_master([a1, a2]) is a2

    def test_no_anchor_picks_highest_word_count(self):
        low = _doc("Low WC", doc_layer="plain", word_count=200)
        high = _doc("High WC", doc_layer="plain", word_count=5000)
        assert select_master([low, high]) is high

    def test_word_count_tie_picks_latest_pub_date(self):
        old = _doc("Old", doc_layer="plain", word_count=1000, pub_date="January 2018")
        new = _doc("New", doc_layer="plain", word_count=1000, pub_date="March 2022")
        assert select_master([old, new]) is new

    def test_single_doc_returns_that_doc(self):
        d = _doc("Only")
        assert select_master([d]) is d

    def test_patch_layer_loses_to_plain(self):
        patch = _doc("Patch", doc_layer="patch", word_count=9000)
        plain = _doc("Plain", doc_layer="plain", word_count=100)
        assert select_master([patch, plain]) is plain


# ---------------------------------------------------------------------------
# TestGroupDocuments
# ---------------------------------------------------------------------------


class TestGroupDocuments:
    def test_same_title_different_versions_same_group(self):
        docs = [
            _doc("VSE GUI 1.7.1 Technical Manual", app_code="SD"),
            _doc("VSE GUI 1.7.64 Technical Manual", app_code="SD"),
            _doc("VSE GUI 1.7.10 Technical Manual", app_code="SD"),
        ]
        groups = group_documents(docs)
        assert len(groups) == 1
        assert len(groups[0].members) == 3

    def test_different_subjects_different_groups(self):
        docs = [
            _doc("Outpatient Pharmacy User Manual", app_code="PSO"),
            _doc("Inpatient Pharmacy User Manual", app_code="PSO"),
        ]
        groups = group_documents(docs)
        assert len(groups) == 2

    def test_different_app_code_different_groups(self):
        docs = [
            _doc("Technical Manual", app_code="PSO"),
            _doc("Technical Manual", app_code="OR"),
        ]
        groups = group_documents(docs)
        assert len(groups) == 2

    def test_different_doc_type_different_groups(self):
        docs = [
            _doc("CPRS User Manual", doc_type="user-manual", app_code="CPRS"),
            _doc("CPRS Technical Manual", doc_type="technical-manual", app_code="CPRS"),
        ]
        groups = group_documents(docs)
        assert len(groups) == 2

    def test_single_doc_groups_alone(self):
        docs = [_doc("Unique Document")]
        groups = group_documents(docs)
        assert len(groups) == 1
        assert len(groups[0].members) == 1

    def test_groups_have_correct_app_code_and_doc_type(self):
        docs = [
            _doc("CPRS Technical Manual v1", doc_type="technical-manual", app_code="CPRS"),
            _doc("CPRS Technical Manual v2", doc_type="technical-manual", app_code="CPRS"),
        ]
        groups = group_documents(docs)
        assert groups[0].app_code == "CPRS"
        assert groups[0].doc_type == "technical-manual"


# ---------------------------------------------------------------------------
# TestExtractUniqueSections
# ---------------------------------------------------------------------------

_DOC_MULTIHEADING = """\
## Introduction
Some introductory content.
Multiple lines here.

## Background
Background content here.

### Sub-background
Subsection content.

## Configuration
Config content.

## Summary
Summary content.
"""


class TestExtractUniqueSections:
    def test_extracts_requested_heading(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        assert len(sections) == 1
        assert sections[0].normalized == "background"

    def test_extracted_content_includes_heading_line(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        assert "## Background" in sections[0].content

    def test_extracted_content_includes_body_text(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        assert "Background content here" in sections[0].content

    def test_section_ends_at_sibling_heading(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        # Should NOT include "Configuration" content
        assert "Config content" not in sections[0].content

    def test_subsections_included_in_parent_section(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        # H3 "Sub-background" is nested under H2 "Background" — include it
        assert "Sub-background" in sections[0].content

    def test_multiple_headings_extracted(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background", "configuration"})
        norms = {s.normalized for s in sections}
        assert norms == {"background", "configuration"}

    def test_heading_not_in_doc_returns_empty(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"nonexistent heading"})
        assert sections == []

    def test_empty_set_returns_empty(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, set())
        assert sections == []

    def test_section_heading_level_recorded(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"background"})
        assert sections[0].level == 2

    def test_h3_section_extracted(self):
        sections = extract_unique_sections(_DOC_MULTIHEADING, {"sub-background"})
        assert len(sections) == 1
        assert "Subsection content" in sections[0].content

    def test_frontmatter_not_treated_as_headings(self):
        doc = "---\ntitle: Some Doc\n---\n\n## Introduction\nContent.\n"
        sections = extract_unique_sections(doc, {"introduction"})
        assert len(sections) == 1

    def test_patch_normalized_heading_found(self):
        doc = "## PSO*7*801 Release Notes\nContent.\n## Summary\nEnd.\n"
        sections = extract_unique_sections(doc, {"release notes"})
        assert len(sections) == 1
        assert "release notes" == sections[0].normalized


# ---------------------------------------------------------------------------
# TestConsolidateGroup
# ---------------------------------------------------------------------------

_MASTER_TEXT = """\
## Introduction
Master introduction content.

## Configuration
Master configuration content.

## Summary
Master summary.
"""

_PRIOR_TEXT = """\
## Introduction
Old introduction.

## Legacy Feature
This feature was removed in a later version.

## Configuration
Old config.

## Deprecated Procedure
Another removed section.
"""


class TestConsolidateGroup:
    def _make_group(self) -> ConsolidationGroup:
        master = _doc(
            "PSO Technical Manual v2",
            doc_layer="plain",
            word_count=2000,
            pub_date="January 2022",
            text=_MASTER_TEXT,
        )
        prior = _doc(
            "PSO Technical Manual v1",
            doc_layer="plain",
            word_count=1500,
            pub_date="June 2019",
            text=_PRIOR_TEXT,
        )
        return ConsolidationGroup(
            app_code="PSO",
            doc_type="technical-manual",
            group_title="pso technical manual",
            members=[master, prior],
        )

    def test_returns_consolidation_result(self):
        group = self._make_group()
        result = consolidate_group(group)
        assert isinstance(result, ConsolidationResult)

    def test_master_is_highest_ranked_doc(self):
        group = self._make_group()
        result = consolidate_group(group)
        assert result.master.title == "PSO Technical Manual v2"

    def test_master_text_preserved(self):
        group = self._make_group()
        result = consolidate_group(group)
        assert result.master_text == _MASTER_TEXT

    def test_addenda_contain_unique_sections_from_prior(self):
        group = self._make_group()
        result = consolidate_group(group)
        addendum_norms = {s.normalized for s in result.addenda}
        assert "legacy feature" in addendum_norms
        assert "deprecated procedure" in addendum_norms

    def test_addenda_exclude_common_headings(self):
        group = self._make_group()
        result = consolidate_group(group)
        addendum_norms = {s.normalized for s in result.addenda}
        assert "introduction" not in addendum_norms
        assert "configuration" not in addendum_norms

    def test_addenda_source_title_recorded(self):
        group = self._make_group()
        result = consolidate_group(group)
        assert all(s.source_title == "PSO Technical Manual v1" for s in result.addenda)

    def test_single_member_group_no_addenda(self):
        d = _doc("Only Doc", text=_MASTER_TEXT)
        group = ConsolidationGroup(
            app_code="PSO",
            doc_type="technical-manual",
            group_title="only doc",
            members=[d],
        )
        result = consolidate_group(group)
        assert result.addenda == []

    def test_addenda_is_list_of_unique_sections(self):
        group = self._make_group()
        result = consolidate_group(group)
        assert all(isinstance(s, UniqueSection) for s in result.addenda)
