"""
Unit tests for ingest/prepare.py — pure functions for markdown assembly.

No I/O, no Docling, no filesystem.
"""

from vista_docs.ingest.prepare import build_markdown, make_frontmatter
from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _entry(**kwargs) -> ManifestEntry:
    defaults = dict(
        package_id="OR*3.0",
        app_code="CPRS",
        doc_title="CPRS Technical Manual: GUI Version",
        doc_type=DocType.TECHNICAL_MANUAL,
        patch="OR*3.0*636",
        docx_url="https://www.va.gov/vdl/documents/Clinical/CPRS/cprsguitm.docx",
        pdf_url="https://www.va.gov/vdl/documents/Clinical/CPRS/cprsguitm.pdf",
        output_filename="cprs-technical-manual-gui-version.md",
        fetch_status=FetchStatus.OK,
        local_path="/data/raw/CPRS/cprsguitm.docx",
        fetched_ext="docx",
    )
    defaults.update(kwargs)
    return ManifestEntry(**defaults)


# ---------------------------------------------------------------------------
# make_frontmatter
# ---------------------------------------------------------------------------


class TestMakeFrontmatter:
    def test_returns_string(self):
        fm = make_frontmatter(_entry())
        assert isinstance(fm, str)

    def test_has_yaml_fences(self):
        fm = make_frontmatter(_entry())
        assert fm.startswith("---\n")
        assert fm.strip().endswith("---")

    def test_includes_title(self):
        fm = make_frontmatter(_entry())
        assert "title:" in fm
        assert "CPRS Technical Manual" in fm

    def test_includes_doc_type(self):
        fm = make_frontmatter(_entry())
        assert "doc_type:" in fm
        assert "technical-manual" in fm

    def test_includes_app_code(self):
        fm = make_frontmatter(_entry())
        assert "app_code: CPRS" in fm

    def test_includes_patch(self):
        fm = make_frontmatter(_entry())
        assert "patch: OR*3.0*636" in fm

    def test_includes_source_urls(self):
        fm = make_frontmatter(_entry())
        assert "docx_url:" in fm
        assert "pdf_url:" in fm

    def test_empty_patch_omitted_or_blank(self):
        fm = make_frontmatter(_entry(patch=""))
        # Either patch is absent or blank — must not crash
        assert isinstance(fm, str)

    def test_title_quoted_when_contains_colon(self):
        """YAML titles with colons must be quoted to stay valid YAML."""
        fm = make_frontmatter(_entry(doc_title="CPRS Technical Manual: GUI Version"))
        # The title value must be wrapped in quotes
        assert '"CPRS Technical Manual: GUI Version"' in fm or (
            "'CPRS Technical Manual: GUI Version'" in fm
        )


# ---------------------------------------------------------------------------
# build_markdown
# ---------------------------------------------------------------------------


_RAW_MD = """\
<!-- TOC -->
- [Intro](#intro)
<!-- /TOC -->

# 1. Introduction

NOTE: Read this carefully.

Department of Veterans Affairs

## 1.1 Overview

Some content here.

###### Very deep heading
"""


class TestBuildMarkdown:
    def test_returns_string(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert isinstance(result, str)

    def test_starts_with_frontmatter(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert result.startswith("---\n")

    def test_toc_stripped(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "<!-- TOC -->" not in result

    def test_outline_numbers_stripped(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "# Introduction" in result
        assert "# 1. Introduction" not in result

    def test_deep_headings_capped(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "###### " not in result
        assert "#### Very deep heading" in result

    def test_callouts_formatted(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "> **NOTE:**" in result
        assert "NOTE: Read" not in result

    def test_boilerplate_stripped(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "Department of Veterans Affairs" not in result

    def test_content_preserved(self):
        result = build_markdown(_entry(), _RAW_MD)
        assert "Some content here." in result

    def test_empty_raw_md_still_has_frontmatter(self):
        result = build_markdown(_entry(), "")
        assert result.startswith("---\n")
