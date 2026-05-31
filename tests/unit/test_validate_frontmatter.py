"""Unit tests for the frontmatter validator / sanitizer / safe serializer.

These guardrails make a broken corpus impossible to publish:
  - sanitize_scalar strips HTML / markdown / control junk to plain text
  - safe_dump_frontmatter round-trips through strict YAML and raises on failure
  - validate_frontmatter flags every data-quality defect at the source
"""

from __future__ import annotations

import pytest
import yaml

from vista_docs.validate.frontmatter import (
    LEGACY_ONLY_KEYS,
    REQUIRED_KEYS,
    VALID_SECTIONS,
    Violation,
    safe_dump_frontmatter,
    sanitize_scalar,
    validate_doc_bytes,
    validate_frontmatter,
)

# ---------------------------------------------------------------------------
# sanitize_scalar
# ---------------------------------------------------------------------------


def test_sanitize_strips_html_table_blob():
    raw = (
        '<table style=\\"width:100%;\\"> <colgroup> <col style=\\"width: 13%\\" /> '
        '<tbody> <tr class=\\"odd\\"> <td><strong>Date</strong></td> </tr> </tbody> </table>'
    )
    out = sanitize_scalar(raw)
    assert "<" not in out and ">" not in out
    assert "table" not in out.lower() or "Date" in out  # tag names gone, cell text may remain
    assert "Date" in out


def test_sanitize_strips_html_comment_and_md_link():
    raw = "<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)"
    out = sanitize_scalar(raw)
    assert "<!--" not in out
    assert "](#" not in out
    assert "(#table-of-contents)" not in out


def test_sanitize_fixes_mojibake():
    # ftfy repairs the cp1252 mojibake; it also uncurls the quote (’ → ').
    out = sanitize_scalar("Developerâ€™s Guide")
    assert "â€" not in out
    assert out in ("Developer’s Guide", "Developer's Guide")


def test_sanitize_removes_c0_control_chars():
    out = sanitize_scalar("foo\x03bar\x07baz")
    assert "\x03" not in out and "\x07" not in out
    assert "foo" in out and "baz" in out


def test_sanitize_collapses_whitespace_and_strips():
    assert sanitize_scalar("  a\n\n  b   c\t ") == "a b c"


def test_sanitize_non_string_returns_empty():
    assert sanitize_scalar(None) == ""
    assert sanitize_scalar(123) == ""


def test_sanitize_is_idempotent():
    raw = "<p>Hello <b>world</b></p>  &amp; more"
    once = sanitize_scalar(raw)
    assert sanitize_scalar(once) == once


# ---------------------------------------------------------------------------
# safe_dump_frontmatter — round-trip guard
# ---------------------------------------------------------------------------


def test_safe_dump_roundtrips_backslash_value():
    # The (ACKQ\3.0\3) case — invalid as a double-quoted YAML escape.
    fm = {"title": "T", "description": "The module (ACKQ\\3.0\\3) was developed."}
    out = safe_dump_frontmatter(fm)
    reparsed = yaml.safe_load(out)
    assert reparsed["description"] == "The module (ACKQ\\3.0\\3) was developed."


def test_safe_dump_roundtrips_colon_and_quotes():
    fm = {"title": 'Part 1: "Overview"', "group_key": "ACKQ:ACKQ:3"}
    reparsed = yaml.safe_load(safe_dump_frontmatter(fm))
    assert reparsed["title"] == 'Part 1: "Overview"'
    assert reparsed["group_key"] == "ACKQ:ACKQ:3"


def test_safe_dump_orders_canonical_keys_first():
    fm = {"zzz_extra": 1, "title": "T", "section": "CLI", "app_code": "XU"}
    out = safe_dump_frontmatter(fm)
    lines = [ln.split(":")[0] for ln in out.splitlines() if ln and not ln.startswith(" ")]
    assert lines.index("title") < lines.index("zzz_extra")
    assert lines.index("section") < lines.index("zzz_extra")


def test_safe_dump_preserves_lists_and_ints():
    fm = {"title": "T", "keywords": ["a", "b"], "word_count": 42, "file_numbers": []}
    reparsed = yaml.safe_load(safe_dump_frontmatter(fm))
    assert reparsed["keywords"] == ["a", "b"]
    assert reparsed["word_count"] == 42
    assert reparsed["file_numbers"] == []


def test_safe_dump_output_always_reparses():
    nasty = {
        "title": "ACKQ*3*12 Audiometric â€“ Module",
        "description": '<table> <col style=\\"width: 4%\\" /> "quoted: colon" \\3 end',
        "audience": "<!-- x -->[↑](#t)",
        "group_key": "A:B:C",
    }
    out = safe_dump_frontmatter(nasty)
    # Must not raise:
    reparsed = yaml.safe_load(out)
    assert isinstance(reparsed, dict)


# ---------------------------------------------------------------------------
# validate_frontmatter
# ---------------------------------------------------------------------------


def _good_fm():
    return {
        "title": "ACKQ Technical Manual",
        "doc_type": "TM",
        "doc_label": "Technical Manual",
        "app_code": "ACKQ",
        "app_name": "Quality Audiology",
        "section": "CLI",
        "pkg_ns": "ACKQ",
        "description": "A clean plain-text description.",
        "audience": "Technical staff",
    }


def test_validate_clean_doc_has_no_violations():
    assert validate_frontmatter(_good_fm()) == []


def test_validate_flags_missing_required_keys():
    fm = _good_fm()
    del fm["section"]
    fm["app_name"] = "   "  # empty after strip
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "missing_key:section" in codes
    assert "missing_key:app_name" in codes
    assert all(v.severity == "hard" for v in validate_frontmatter(fm))


def test_validate_flags_bad_section():
    fm = _good_fm()
    fm["section"] = "CLINICAL"
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "bad_section" in codes


def test_validate_all_valid_sections_pass():
    for sec in VALID_SECTIONS:
        fm = _good_fm()
        fm["section"] = sec
        assert not any(v.code == "bad_section" for v in validate_frontmatter(fm))


def test_validate_flags_html_in_scalar():
    fm = _good_fm()
    fm["description"] = "<table><tr><td>x</td></tr></table>"
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "html_in_scalar:description" in codes


def test_validate_flags_markdown_comment_in_scalar():
    fm = _good_fm()
    fm["audience"] = "<!-- back-to-toc -->"
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "html_in_scalar:audience" in codes


def test_validate_flags_mojibake_in_scalar():
    fm = _good_fm()
    fm["title"] = "Developerâ€™s Guide"
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "mojibake:title" in codes


def test_validate_flags_control_char_in_scalar():
    fm = _good_fm()
    fm["doc_subject"] = "bad\x03subject"
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "control_char:doc_subject" in codes


def test_validate_flags_legacy_schema():
    fm = {
        "consolidated_title": "x",
        "master_source": "y",
        "app_code": "ADT",
        "doc_type": "RN",
    }
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "legacy_schema" in codes


def test_validate_consolidated_with_required_keys_not_legacy():
    fm = _good_fm()
    fm["master_source"] = "Some master"
    fm["prior_versions"] = ["v1", "v2"]
    codes = {v.code for v in validate_frontmatter(fm)}
    assert "legacy_schema" not in codes


# ---------------------------------------------------------------------------
# validate_doc_bytes — whole-document checks
# ---------------------------------------------------------------------------


def test_validate_doc_bytes_detects_invalid_yaml():
    bad = b'---\ntitle: "a \\3 b"\ndescription: "x: y"\n  - oops\n---\nbody\n'
    vs = validate_doc_bytes(bad)
    assert any(v.code == "invalid_yaml" for v in vs)


def test_validate_doc_bytes_detects_non_utf8():
    raw = "---\ntitle: x\n---\n".encode("utf-8") + b"\xff\xfe body"
    vs = validate_doc_bytes(raw)
    assert any(v.code == "not_utf8" for v in vs)


def test_validate_doc_bytes_detects_missing_frontmatter():
    vs = validate_doc_bytes(b"# Just a heading\n\nNo frontmatter here.\n")
    assert any(v.code == "no_frontmatter" for v in vs)


def test_validate_doc_bytes_clean_doc_passes():
    fm = _good_fm()
    doc = ("---\n" + safe_dump_frontmatter(fm) + "---\nbody\n").encode("utf-8")
    assert validate_doc_bytes(doc) == []


def test_required_keys_and_sections_constants():
    assert set(REQUIRED_KEYS) == {
        "title",
        "doc_type",
        "doc_label",
        "app_code",
        "app_name",
        "section",
        "pkg_ns",
    }
    assert VALID_SECTIONS == frozenset({"CLI", "FIN", "GUI", "INF", "MON"})
    assert "consolidated_title" in LEGACY_ONLY_KEYS


def test_violation_is_frozen():
    v = Violation("x", "hard")
    with pytest.raises(Exception):
        v.code = "y"  # type: ignore[misc]
