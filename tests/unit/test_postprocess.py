"""
Unit tests for ingest/postprocess.py — pure markdown transforms.
"""

from vista_docs.ingest.postprocess import (
    cap_heading_depth,
    format_callouts,
    strip_boilerplate,
    strip_outline_numbering,
    strip_toc,
)


class TestStripToc:
    def test_removes_toc_block(self):
        md = "# Title\n\n<!-- TOC -->\n1. Section\n2. Other\n<!-- /TOC -->\n\n## Body"
        result = strip_toc(md)
        assert "<!-- TOC -->" not in result
        assert "## Body" in result

    def test_no_toc_unchanged(self):
        md = "# Title\n\n## Body text here"
        assert strip_toc(md) == md

    def test_docling_toc_heading_style(self):
        md = "**Table of Contents**\n\n- [Section 1](#section-1)\n- [Section 2](#section-2)\n\n## Real Content"
        result = strip_toc(md)
        assert "Table of Contents" not in result
        assert "## Real Content" in result


class TestStripOutlineNumbering:
    def test_strips_single_level(self):
        assert strip_outline_numbering("# 1. Introduction") == "# Introduction"

    def test_strips_multi_level(self):
        assert strip_outline_numbering("## 1.2.3 Sub Section") == "## Sub Section"

    def test_no_numbering_unchanged(self):
        assert strip_outline_numbering("# Introduction") == "# Introduction"

    def test_preserves_heading_level(self):
        result = strip_outline_numbering("### 2.3.4 Deep Section")
        assert result.startswith("### ")

    def test_applies_to_all_headings(self):
        md = "# 1. Top\n\n## 1.1 Sub\n\nBody text\n\n### 1.1.1 Deep"
        result = strip_outline_numbering(md)
        assert "# Top" in result
        assert "## Sub" in result
        assert "### Deep" in result
        assert "1." not in result
        assert "1.1" not in result


class TestCapHeadingDepth:
    def test_h5_becomes_h4(self):
        assert cap_heading_depth("##### H5 Heading") == "#### H5 Heading"

    def test_h6_becomes_h4(self):
        assert cap_heading_depth("###### H6 Heading") == "#### H6 Heading"

    def test_h4_unchanged(self):
        assert cap_heading_depth("#### H4 Heading") == "#### H4 Heading"

    def test_h1_h2_h3_unchanged(self):
        for level in range(1, 4):
            prefix = "#" * level
            heading = f"{prefix} Heading"
            assert cap_heading_depth(heading) == heading

    def test_applies_to_all_headings_in_block(self):
        md = "# One\n\n##### Five\n\n###### Six"
        result = cap_heading_depth(md)
        assert "##### " not in result
        assert "###### " not in result


class TestFormatCallouts:
    def test_note_becomes_blockquote(self):
        md = "NOTE: This is important."
        result = format_callouts(md)
        assert result.strip() == "> **NOTE:** This is important."

    def test_warning_becomes_blockquote(self):
        md = "WARNING: Danger here."
        result = format_callouts(md)
        assert "> **WARNING:**" in result

    def test_caution_becomes_blockquote(self):
        md = "CAUTION: Be careful."
        result = format_callouts(md)
        assert "> **CAUTION:**" in result

    def test_important_becomes_blockquote(self):
        md = "IMPORTANT: Read this."
        result = format_callouts(md)
        assert "> **IMPORTANT:**" in result

    def test_reminder_becomes_blockquote(self):
        md = "REMINDER: Do not forget."
        result = format_callouts(md)
        assert "> **REMINDER:**" in result

    def test_normal_text_unchanged(self):
        md = "This is regular text."
        assert format_callouts(md) == md

    def test_case_insensitive(self):
        md = "note: lowercase."
        result = format_callouts(md)
        assert "> **NOTE:**" in result


class TestStripBoilerplate:
    def test_strips_department_of_veterans_affairs(self):
        md = "Department of Veterans Affairs\n\n## Content"
        result = strip_boilerplate(md)
        assert "Department of Veterans Affairs" not in result
        assert "## Content" in result

    def test_strips_intentionally_blank(self):
        md = "This page intentionally left blank\n\n## Content"
        result = strip_boilerplate(md)
        assert "intentionally left blank" not in result

    def test_normal_content_preserved(self):
        md = "## Important Section\n\nThis is the real content."
        assert strip_boilerplate(md) == md
