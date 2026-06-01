"""Unit tests for the frontmatter JSON-schema validator (spec §11.1)."""

import json
from pathlib import Path

from vista_docs.validate.schema import (
    FRONTMATTER_SCHEMA,
    SCHEMA_PATH,
    validate_against_schema,
)


def _ok_fm(**over):
    fm = {
        "title": "T",
        "doc_type": "UM",
        "doc_label": "User Manual",
        "app_code": "CPRS",
        "app_name": "CPRS",
        "section": "GUI",
        "pkg_ns": "OR",
        "has_toc": True,
        "toc": "generated",
        "anchors_source": "word",
        "page_count": 5,
    }
    fm.update(over)
    return fm


def test_valid_fm_has_no_violations():
    assert validate_against_schema(_ok_fm()) == []


def test_enum_violation_toc_is_hard():
    v = validate_against_schema(_ok_fm(toc="bogus"))
    assert any(x.code == "schema_enum:toc" and x.severity == "hard" for x in v)


def test_enum_violation_anchors_source():
    v = validate_against_schema(_ok_fm(anchors_source="weird"))
    assert any(x.code == "schema_enum:anchors_source" for x in v)


def test_bad_section_enum():
    v = validate_against_schema(_ok_fm(section="XYZ"))
    assert any(x.code == "schema_enum:section" for x in v)


def test_type_violation_has_toc():
    v = validate_against_schema(_ok_fm(has_toc="yes"))
    assert any(x.code == "schema_type:has_toc" for x in v)


def test_integer_field_rejects_bool():
    v = validate_against_schema(_ok_fm(page_count=True))
    assert any(x.code == "schema_type:page_count" for x in v)


def test_required_missing_is_hard():
    fm = _ok_fm()
    del fm["app_code"]
    v = validate_against_schema(fm)
    assert any(x.code == "schema_required:app_code" and x.severity == "hard" for x in v)


def test_null_allowed_for_revision_newest():
    assert validate_against_schema(_ok_fm(revision_newest=None)) == []


def test_anchor_aliases_must_be_mapping():
    assert validate_against_schema(_ok_fm(anchor_aliases={"_Toc1": "slug"})) == []
    v = validate_against_schema(_ok_fm(anchor_aliases=["not", "a", "map"]))
    assert any(x.code == "schema_type:anchor_aliases" for x in v)


def test_unknown_key_is_soft():
    v = validate_against_schema(_ok_fm(bogus_key="x"))
    assert any(x.code == "schema_unknown_key:bogus_key" and x.severity == "soft" for x in v)


def test_json_artifact_matches_dict():
    # The committed JSON Schema file must not drift from the source-of-truth dict.
    assert json.loads(Path(SCHEMA_PATH).read_text(encoding="utf-8")) == FRONTMATTER_SCHEMA
