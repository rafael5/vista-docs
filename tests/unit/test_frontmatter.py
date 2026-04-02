"""
Unit tests for enrich/frontmatter.py — pure YAML frontmatter rewriting.
"""

from vista_docs.enrich.frontmatter import (
    CANONICAL_FIELD_ORDER,
    RETIRED_FIELDS,
    parse_frontmatter,
    rebuild_frontmatter,
    rewrite_frontmatter,
)

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

    def test_empty_scalar_value_is_empty_string_not_list(self):
        """'key: ' (blank value) must parse as '' not [], even when followed by another key."""
        md = "---\nrevision_oldest: \nrevision_newest: \npage_count: 8\n---\n"
        result = parse_frontmatter(md)
        assert result["revision_oldest"] == ""
        assert result["revision_newest"] == ""

    def test_explicit_empty_list_stays_as_string(self):
        """'key: []' must stay as the string '[]', not be converted to a list."""
        md = "---\nsecurity_keys: []\n---\n"
        result = parse_frontmatter(md)
        assert result["security_keys"] == "[]"

    def test_list_with_items_still_parsed_as_list(self):
        """Blank-value key followed by '  - item' lines must still produce a list."""
        md = "---\nkeywords: \n  - order\n  - pharmacy\n---\n"
        result = parse_frontmatter(md)
        assert result["keywords"] == ["order", "pharmacy"]


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


# ---------------------------------------------------------------------------
# rebuild_frontmatter constants
# ---------------------------------------------------------------------------


class TestFrontmatterConstants:
    def test_canonical_order_is_list(self):
        assert isinstance(CANONICAL_FIELD_ORDER, list)
        assert len(CANONICAL_FIELD_ORDER) > 0

    def test_canonical_order_contains_key_fields(self):
        required = {
            "title",
            "doc_type",
            "app_code",
            "section",
            "pkg_ns",
            "patch_id",
            "word_count",
            "pub_date",
            "docx_url",
        }
        assert required.issubset(set(CANONICAL_FIELD_ORDER))

    def test_canonical_order_has_no_retired_fields(self):
        assert not RETIRED_FIELDS.intersection(CANONICAL_FIELD_ORDER)

    def test_retired_fields_set(self):
        assert RETIRED_FIELDS == {
            "patch",
            "patch_number",
            "package_name",
            "package_namespace",
            "package_version",
        }

    def test_identity_group_precedes_application_group(self):
        assert CANONICAL_FIELD_ORDER.index("title") < CANONICAL_FIELD_ORDER.index("app_code")

    def test_application_group_precedes_vista_group(self):
        assert CANONICAL_FIELD_ORDER.index("app_code") < CANONICAL_FIELD_ORDER.index("pkg_ns")

    def test_vista_group_precedes_content_group(self):
        assert CANONICAL_FIELD_ORDER.index("pkg_ns") < CANONICAL_FIELD_ORDER.index("description")

    def test_content_group_precedes_counts_group(self):
        assert CANONICAL_FIELD_ORDER.index("keywords") < CANONICAL_FIELD_ORDER.index("word_count")

    def test_counts_group_precedes_revisions_group(self):
        assert CANONICAL_FIELD_ORDER.index("word_count") < CANONICAL_FIELD_ORDER.index("pub_date")

    def test_revisions_group_precedes_urls_group(self):
        assert CANONICAL_FIELD_ORDER.index("pub_date") < CANONICAL_FIELD_ORDER.index("docx_url")


# ---------------------------------------------------------------------------
# rebuild_frontmatter
# ---------------------------------------------------------------------------

_FULL_MD = """\
---
title: PSO User Manual
doc_type: user-manual
app_code: PSO
patch: PSO*7.0*599
patch_number: 599
package_name: Outpatient Pharmacy
package_namespace: PSO
package_version: 7.0
docx_url: https://va.gov/docs/pso_um.docx
pdf_url: https://va.gov/docs/pso_um.pdf
pub_date: April 2023
page_count: 200
word_count: 45000
keywords:
  - pharmacy
  - order
is_stub: False
has_toc: True
---

Body content here.
"""


class TestRebuildFrontmatter:
    def test_removes_retired_fields(self):
        result = rebuild_frontmatter(_FULL_MD)
        for field in RETIRED_FIELDS:
            assert f"\n{field}:" not in result
            assert f"\n{field}: " not in result

    def test_preserves_non_retired_fields(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert "title: PSO User Manual" in result
        assert "app_code: PSO" in result
        # URLs contain ':' so they are quoted by _serialize_value
        assert '"https://va.gov/docs/pso_um.docx"' in result
        assert "word_count: 45000" in result

    def test_preserves_body(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert "Body content here." in result

    def test_valid_frontmatter_fences(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert result.startswith("---\n")
        lines = result.splitlines()
        fence_lines = [i for i, ln in enumerate(lines) if ln == "---"]
        assert len(fence_lines) == 2

    def test_title_before_app_code(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert result.index("title:") < result.index("app_code:")

    def test_app_code_before_pkg_ns(self):
        result = rebuild_frontmatter(_FULL_MD)
        # pkg_ns not in this fixture, so add it via extra_fields
        result = rebuild_frontmatter(_FULL_MD, {"pkg_ns": "PSO"})
        assert result.index("app_code:") < result.index("pkg_ns:")

    def test_word_count_before_pub_date(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert result.index("word_count:") < result.index("pub_date:")

    def test_pub_date_before_docx_url(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert result.index("pub_date:") < result.index("docx_url:")

    def test_extra_fields_merged(self):
        result = rebuild_frontmatter(_FULL_MD, {"section": "CLI", "doc_layer": "anchor"})
        assert "section: CLI" in result
        assert "doc_layer: anchor" in result

    def test_extra_fields_overwrite_existing(self):
        result = rebuild_frontmatter(_FULL_MD, {"doc_type": "UM"})
        assert "doc_type: UM" in result
        assert result.count("doc_type:") == 1

    def test_extra_fields_none_is_ok(self):
        result = rebuild_frontmatter(_FULL_MD, None)
        assert "title: PSO User Manual" in result

    def test_unknown_field_appended_at_end(self):
        result = rebuild_frontmatter(_FULL_MD, {"custom_field": "custom_value"})
        fm_end = result.index("\n---\n")
        assert "custom_field: custom_value" in result
        assert result.index("custom_field:") < fm_end

    def test_list_values_round_trip(self):
        result = rebuild_frontmatter(_FULL_MD)
        assert "keywords:" in result
        assert "  - pharmacy" in result
        assert "  - order" in result

    def test_colon_values_quoted(self):
        result = rebuild_frontmatter(_FULL_MD, {"group_key": "PSO:PSO:7.0"})
        assert '"PSO:PSO:7.0"' in result

    def test_retired_field_in_extra_fields_still_excluded(self):
        """Even if extra_fields tries to add a retired field, it should be dropped."""
        result = rebuild_frontmatter(_FULL_MD, {"patch": "PSO*7.0*599"})
        assert "\npatch: " not in result
        assert "\npatch:" not in result
