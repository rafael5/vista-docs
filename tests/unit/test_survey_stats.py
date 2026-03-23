"""
Unit tests for survey/stats.py — pure markdown doc analysis.

No filesystem I/O. All inputs are strings and dataclasses.
"""

from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry
from vista_docs.survey.stats import DocStats, analyze_doc, summarize_corpus

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_FRONTMATTER = """\
---
title: CPRS Technical Manual
doc_type: technical-manual
app_code: CPRS
patch: OR*3.0*636
docx_url: https://example.com/cprsguitm.docx
pdf_url: https://example.com/cprsguitm.pdf
---
"""

_RICH_BODY = """\
## Overview

Some introductory text here with several words.

## Configuration

> **NOTE:** Read this carefully before proceeding.

| Column A | Column B |
|----------|----------|
| value 1  | value 2  |

### Subsection

More content with enough words to be meaningful.

> **WARNING:** Do not skip this step.
"""

_STUB_BODY = ""  # scaffold-only: no body content


def _entry(**kwargs) -> ManifestEntry:
    defaults = dict(
        package_id="",
        app_code="CPRS",
        doc_title="CPRS Technical Manual",
        doc_type=DocType.TECHNICAL_MANUAL,
        patch="OR*3.0*636",
        fetch_status=FetchStatus.OK,
        ingest_status=FetchStatus.OK,
        output_filename="cprs-technical-manual.md",
    )
    defaults.update(kwargs)
    return ManifestEntry(**defaults)


# ---------------------------------------------------------------------------
# DocStats from analyze_doc
# ---------------------------------------------------------------------------


class TestAnalyzeDoc:
    def test_returns_docstats(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert isinstance(result, DocStats)

    def test_line_count(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.line_count == len(md.splitlines())

    def test_word_count(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.word_count > 0

    def test_heading_count(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.heading_count == 3  # ##, ##, ###

    def test_table_count(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.table_count == 1

    def test_callout_count(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.callout_count == 2  # NOTE + WARNING

    def test_stub_detection_empty_body(self):
        md = _FRONTMATTER + _STUB_BODY
        result = analyze_doc(md, _entry())
        assert result.is_stub is True

    def test_stub_detection_rich_body(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.is_stub is False

    def test_carries_entry_fields(self):
        md = _FRONTMATTER + _RICH_BODY
        result = analyze_doc(md, _entry())
        assert result.app_code == "CPRS"
        assert result.doc_type == "technical-manual"
        assert result.patch == "OR*3.0*636"

    def test_empty_markdown_is_stub(self):
        result = analyze_doc("", _entry())
        assert result.is_stub is True
        assert result.line_count == 0


# ---------------------------------------------------------------------------
# summarize_corpus
# ---------------------------------------------------------------------------

_STATS = [
    DocStats(
        app_code="CPRS",
        doc_title="TM",
        doc_type="technical-manual",
        patch="OR*3.0*636",
        line_count=500,
        word_count=4000,
        heading_count=20,
        table_count=5,
        callout_count=3,
        is_stub=False,
    ),
    DocStats(
        app_code="CPRS",
        doc_title="IG",
        doc_type="installation-guide",
        patch="",
        line_count=8,
        word_count=40,
        heading_count=0,
        table_count=0,
        callout_count=0,
        is_stub=True,
    ),
    DocStats(
        app_code="ADT",
        doc_title="UG",
        doc_type="user-manual",
        patch="",
        line_count=300,
        word_count=2500,
        heading_count=12,
        table_count=3,
        callout_count=1,
        is_stub=False,
    ),
]


class TestSummarizeCorpus:
    def test_returns_dict(self):
        result = summarize_corpus(_STATS)
        assert isinstance(result, dict)

    def test_total_docs(self):
        result = summarize_corpus(_STATS)
        assert result["total_docs"] == 3

    def test_total_stubs(self):
        result = summarize_corpus(_STATS)
        assert result["total_stubs"] == 1

    def test_by_package_counts(self):
        result = summarize_corpus(_STATS)
        assert result["by_package"]["CPRS"]["docs"] == 2
        assert result["by_package"]["ADT"]["docs"] == 1

    def test_by_package_stubs(self):
        result = summarize_corpus(_STATS)
        assert result["by_package"]["CPRS"]["stubs"] == 1
        assert result["by_package"]["ADT"]["stubs"] == 0

    def test_by_doc_type(self):
        result = summarize_corpus(_STATS)
        assert result["by_doc_type"]["technical-manual"] == 1
        assert result["by_doc_type"]["installation-guide"] == 1
        assert result["by_doc_type"]["user-manual"] == 1

    def test_quality_flags_stubs(self):
        result = summarize_corpus(_STATS)
        stubs = result["quality_flags"]["stubs"]
        assert len(stubs) == 1
        assert stubs[0]["doc_title"] == "IG"

    def test_empty_corpus(self):
        result = summarize_corpus([])
        assert result["total_docs"] == 0
