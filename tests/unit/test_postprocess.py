"""
Unit tests for ingest/postprocess.py — pure markdown transforms.
"""

from vista_docs.ingest.postprocess import (
    BACK_MARKER,
    build_toc,
    cap_heading_depth,
    compact_lists,
    compact_reference_sections,
    format_callouts,
    gfm_anchor,
    insert_back_links,
    insert_toc,
    link_figure_captions,
    normalize_whitespace,
    strip_artifacts,
    strip_back_links,
    strip_boilerplate,
    strip_outline_numbering,
    strip_toc,
    strip_word_toc,
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


class TestStripArtifacts:
    def test_removes_html_comments(self):
        result = strip_artifacts("before <!-- hidden --> after")
        assert "<!-- hidden -->" not in result
        assert "before" in result

    def test_removes_multiline_comment(self):
        result = strip_artifacts("start\n<!-- track\nchange\n-->\nend")
        assert "track" not in result
        assert "start" in result and "end" in result

    def test_removes_empty_bold(self):
        assert strip_artifacts("** **") == ""

    def test_removes_empty_italic(self):
        assert strip_artifacts("* *") == ""

    def test_removes_stray_blockquote(self):
        result = strip_artifacts("> \n\n## Heading")
        assert "> " not in result
        assert "## Heading" in result

    def test_normal_text_unchanged(self):
        md = "# Title\n\nThis is plain text with no artifacts."
        assert strip_artifacts(md) == md


class TestStripWordToc:
    def test_form1_bare_link_block_removed(self):
        md = "[Introduction](#introduction)\n[Methods](#methods)\n[Results](#results)\n\n## Introduction"
        result = strip_word_toc(md)
        assert "[Introduction](#introduction)" not in result
        assert "## Introduction" in result

    def test_form1_fewer_than_3_links_kept(self):
        md = "[A](#a)\n[B](#b)\n\n## Body"
        result = strip_word_toc(md)
        assert "[A](#a)" in result

    def test_form1_blockquote_toc_label_removed(self):
        md = "> Table of Contents\n\n## Section"
        result = strip_word_toc(md)
        assert "Table of Contents" not in result
        assert "## Section" in result

    def test_form2_bullet_toc_section_removed(self):
        md = "## Table of Contents\n\n- [Intro](#intro)\n- [Body](#body)\n\n## Introduction\n\nContent."
        result = strip_word_toc(md)
        assert "- [Intro](#intro)" not in result
        assert "## Introduction" in result

    def test_form3_heading_toc_entries_removed(self):
        md = "# Table of Contents\n\n# [Chapter 1 [1](#p1)](#ch1)\n## [Sub [2](#p2)](#sub)\n\n# Real Chapter"
        result = strip_word_toc(md)
        assert "[Chapter 1" not in result
        assert "# Real Chapter" in result

    def test_form3_orphan_heading_link_removed(self):
        # A TOC heading entry without a preceding "Table of Contents" heading
        md = "# [Some Title [5](#p5)](#anchor)\n\n## Real Body"
        result = strip_word_toc(md)
        assert "[Some Title" not in result
        assert "## Real Body" in result

    def test_form1_blank_lines_after_block_consumed(self):
        # Blank lines between the bare-link block and content are absorbed
        md = "[A](#a)\n[B](#b)\n[C](#c)\n\n\n## Content"
        result = strip_word_toc(md)
        assert "[A](#a)" not in result
        assert "## Content" in result

    def test_form3_blank_lines_after_toc_heading_block_consumed(self):
        # Blank lines after the TOC heading entries are absorbed
        md = "# Table of Contents\n\n# [Ch 1 [1](#p1)](#ch1)\n\n\n# Real Chapter"
        result = strip_word_toc(md)
        assert "[Ch 1" not in result
        assert "# Real Chapter" in result

    def test_form2_trailing_blank_lines_trimmed(self):
        # Blank line before the TOC heading in the output is removed
        md = "Intro.\n\n## Table of Contents\n\n- [A](#a)\n\n## Body"
        result = strip_word_toc(md)
        assert "- [A](#a)" not in result
        # No trailing blank line before Body
        assert "## Body" in result

    def test_no_toc_unchanged(self):
        md = "# Title\n\n## Section\n\nContent."
        assert strip_word_toc(md) == md


class TestLinkFigureCaptions:
    def test_links_figure_caption(self):
        md = "![](img/001.png)\n\nFigure 1. The system architecture."
        result = link_figure_captions(md)
        assert "![Figure 1. The system architecture.]" in result
        assert "*Figure 1. The system architecture.*" in result

    def test_links_table_caption(self):
        md = "![](img/tbl.png)\n\nTable 2.1 Summary of results."
        result = link_figure_captions(md)
        assert "![Table 2.1" in result

    def test_no_caption_unchanged(self):
        md = "![](img/001.png)\n\nSome regular paragraph."
        assert link_figure_captions(md) == md

    def test_caption_must_be_separated_by_blank_line(self):
        # Single newline — should NOT match
        md = "![](img/001.png)\nFigure 1. Caption."
        assert link_figure_captions(md) == md


class TestNormalizeWhitespace:
    def test_collapses_triple_blank_lines(self):
        result = normalize_whitespace("a\n\n\n\nb")
        assert "\n\n\n" not in result
        assert "a\n\nb" in result

    def test_ensures_trailing_newline(self):
        assert normalize_whitespace("text").endswith("\n")

    def test_strips_leading_whitespace(self):
        result = normalize_whitespace("\n\ntext\n")
        assert result == "text\n"


class TestStripBackLinks:
    def test_removes_back_link_lines(self):
        text = (
            "# Heading\n\n<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)\n\nContent"
        )
        result = strip_back_links(text)
        assert BACK_MARKER not in result
        assert "# Heading" in result
        assert "Content" in result

    def test_idempotent_on_clean_text(self):
        md = "# Title\n\n## Section\n\nBody."
        assert strip_back_links(md) == md


class TestInsertBackLinks:
    def test_inserts_after_h1(self):
        md = "# Title\n\nBody."
        result = insert_back_links(md)
        assert BACK_MARKER in result

    def test_skips_toc_heading(self):
        md = "## Table of Contents\n\n- [item](#item)"
        result = insert_back_links(md)
        assert BACK_MARKER not in result

    def test_idempotent(self):
        md = "# Title\n\nBody."
        once = insert_back_links(md)
        # strip then re-insert should not double-insert
        twice = insert_back_links(strip_back_links(once))
        assert twice.count(BACK_MARKER) == once.count(BACK_MARKER)

    def test_h4_not_linked(self):
        md = "#### Deep Heading\n\nContent."
        result = insert_back_links(md)
        assert BACK_MARKER not in result


class TestGfmAnchor:
    def test_basic(self):
        assert gfm_anchor("Hello World", {}) == "hello-world"

    def test_strips_inline_code(self):
        assert gfm_anchor("`foo` bar", {}) == "foo-bar"

    def test_strips_links(self):
        assert gfm_anchor("[text](url)", {}) == "text"

    def test_deduplicates(self):
        seen: dict[str, int] = {}
        a1 = gfm_anchor("Title", seen)
        a2 = gfm_anchor("Title", seen)
        assert a1 == "title"
        assert a2 == "title-1"

    def test_empty_returns_empty(self):
        assert gfm_anchor("!@#", {}) == ""

    def test_html_entities_decoded(self):
        assert gfm_anchor("AT&amp;T", {}) == "att"


class TestBuildToc:
    def test_builds_toc(self):
        lines = ["# Title", "## Section One", "### Sub"]
        result = build_toc(lines)
        assert "## Table of Contents" in result
        assert "[Title]" in result
        assert "[Section One]" in result

    def test_respects_max_depth(self):
        lines = ["# H1", "#### H4"]
        result = build_toc(lines)
        assert "[H4]" not in result

    def test_empty_heading_skipped(self):
        lines = ["# ", "## Real"]
        result = build_toc(lines)
        assert "[Real]" in result

    def test_no_headings_returns_empty(self):
        assert build_toc(["plain text", "more text"]) == ""

    def test_heading_with_no_anchor_skipped(self):
        # heading made entirely of punctuation produces empty anchor
        lines = ["# !@#$%"]
        assert build_toc(lines) == ""


class TestInsertToc:
    def test_inserts_after_h1(self):
        md = "# My Doc\n\n## Section\n\nBody."
        result = insert_toc(md)
        assert "## Table of Contents" in result
        idx_h1 = result.index("# My Doc")
        idx_toc = result.index("## Table of Contents")
        assert idx_toc > idx_h1

    def test_inserts_after_frontmatter_when_no_h1(self):
        md = "---\ntitle: Doc\n---\n\n## Section\n\nBody."
        result = insert_toc(md)
        assert "## Table of Contents" in result
        # TOC appears after the frontmatter block
        idx_fm = result.index("---\ntitle")
        idx_toc = result.index("## Table of Contents")
        assert idx_toc > idx_fm

    def test_no_toc_if_no_headings(self):
        md = "Just a paragraph."
        assert insert_toc(md) == md


class TestCompactLists:
    def test_removes_blank_between_items(self):
        md = "- item one\n\n- item two\n\n- item three"
        result = compact_lists(md)
        assert "\n\n- " not in result
        assert "- item one\n- item two\n- item three" in result

    def test_preserves_blanks_outside_lists(self):
        md = "Paragraph one.\n\nParagraph two."
        assert compact_lists(md) == md

    def test_does_not_touch_code_fences(self):
        md = "```\n- not a list\n\n- still not\n```"
        result = compact_lists(md)
        assert "\n\n- still not\n" in result

    def test_numbered_list_compacted(self):
        md = "1. first\n\n2. second\n\n3. third"
        result = compact_lists(md)
        assert "\n\n2." not in result

    def test_fence_toggle_resets(self):
        md = "```\ncode\n```\n\n- a\n\n- b"
        result = compact_lists(md)
        assert "- a\n- b" in result


class TestCompactReferenceSections:
    def test_compacts_index_section(self):
        md = "## Index\n\nEntry A\n\nEntry B\n\nEntry C\n\n## Next Section"
        result = compact_reference_sections(md)
        assert "Entry A\nEntry B\nEntry C" in result
        assert "## Next Section" in result

    def test_preserves_normal_sections(self):
        md = "## Normal\n\nParagraph one.\n\nParagraph two."
        assert compact_reference_sections(md) == md

    def test_back_link_gets_blank_line_before(self):
        back = BACK_MARKER + "[↑ Table of Contents](#table-of-contents)"
        md = f"## Glossary\n\nTerm A\n\n{back}\n\n## Next"
        result = compact_reference_sections(md)
        # back link should still be present
        assert BACK_MARKER in result

    def test_code_fence_inside_section_preserved(self):
        md = "## Glossary\n\nTerm A\n\n```\ncode line\n\nmore code\n```\n\nTerm B\n\n## End"
        result = compact_reference_sections(md)
        assert "code line\n\nmore code" in result

    def test_section_ends_at_same_level_heading(self):
        md = "## Glossary\n\nTerm A\n\nTerm B\n\n## References\n\nRef A\n\nRef B\n\n## End"
        result = compact_reference_sections(md)
        assert "Term A\nTerm B" in result
        assert "Ref A\nRef B" in result
