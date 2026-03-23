"""
Unit tests for enrich/frontmatter.py — pure YAML frontmatter rewriting.
"""

from vista_docs.enrich.frontmatter import parse_frontmatter, rewrite_frontmatter

_BASE_MD = """\
---
title: CPRS Technical Manual
doc_type: technical-manual
app_code: CPRS
patch: OR*3.0*636
---

## Introduction

Some content here.
"""

_MD_WITH_LIST = """\
---
title: Some Doc
keywords:
  - order checks
  - pharmacy
---

Body content.
"""


class TestParseFrontmatter:
    def test_parses_string_fields(self):
        result = parse_frontmatter(_BASE_MD)
        assert result["title"] == "CPRS Technical Manual"
        assert result["doc_type"] == "technical-manual"
        assert result["app_code"] == "CPRS"

    def test_parses_list_field(self):
        result = parse_frontmatter(_MD_WITH_LIST)
        assert result["keywords"] == ["order checks", "pharmacy"]

    def test_empty_string_returns_empty(self):
        assert parse_frontmatter("") == {}

    def test_no_frontmatter_returns_empty(self):
        assert parse_frontmatter("## Just a heading\n\nBody.") == {}


class TestRewriteFrontmatter:
    def test_adds_new_field(self):
        result = rewrite_frontmatter(_BASE_MD, {"pub_date": "April 2007"})
        assert "pub_date: April 2007" in result

    def test_preserves_existing_fields(self):
        result = rewrite_frontmatter(_BASE_MD, {"pub_date": "April 2007"})
        assert "title: CPRS Technical Manual" in result
        assert "doc_type: technical-manual" in result

    def test_preserves_body_content(self):
        result = rewrite_frontmatter(_BASE_MD, {"pub_date": "April 2007"})
        assert "## Introduction" in result
        assert "Some content here." in result

    def test_adds_integer_field(self):
        result = rewrite_frontmatter(_BASE_MD, {"page_count": 124})
        assert "page_count: 124" in result

    def test_adds_list_field(self):
        result = rewrite_frontmatter(_BASE_MD, {"keywords": ["order", "pharmacy"]})
        assert "keywords:" in result
        assert "  - order" in result
        assert "  - pharmacy" in result

    def test_adds_multiple_fields(self):
        result = rewrite_frontmatter(
            _BASE_MD,
            {"pub_date": "April 2007", "page_count": 124, "table_count": 5},
        )
        assert "pub_date: April 2007" in result
        assert "page_count: 124" in result
        assert "table_count: 5" in result

    def test_quotes_value_with_colon(self):
        result = rewrite_frontmatter(_BASE_MD, {"subtitle": "Part 1: Overview"})
        assert '"Part 1: Overview"' in result

    def test_overwrites_existing_field(self):
        result = rewrite_frontmatter(_BASE_MD, {"app_code": "ADT"})
        assert "app_code: ADT" in result
        assert result.count("app_code:") == 1

    def test_zero_value_written(self):
        result = rewrite_frontmatter(_BASE_MD, {"page_count": 0})
        assert "page_count: 0" in result

    def test_empty_list_written(self):
        result = rewrite_frontmatter(_BASE_MD, {"keywords": []})
        assert "keywords: []" in result

    def test_result_has_valid_fences(self):
        result = rewrite_frontmatter(_BASE_MD, {"pub_date": "April 2007"})
        assert result.startswith("---\n")
        lines = result.split("\n")
        closing = [i for i, ln in enumerate(lines) if ln == "---"]
        assert len(closing) >= 2

    def test_no_existing_frontmatter_creates_one(self):
        md = "## Just a heading\n\nBody."
        result = rewrite_frontmatter(md, {"pub_date": "April 2007"})
        assert result.startswith("---\n")
        assert "pub_date: April 2007" in result
        assert "Body." in result
