"""Unit tests for F4 anchor assignment + GitHub slug algorithm."""

from vista_docs.normalize.anchors_pure import (
    Heading,
    Slugger,
    build_anchor_aliases,
    extract_headings,
    github_slug,
)

# --- github_slug -----------------------------------------------------------


def test_slug_basic():
    assert github_slug("Hello World") == "hello-world"


def test_slug_strips_punctuation_keeps_hyphen_and_underscore():
    assert github_slug("Foo: Bar!") == "foo-bar"
    assert github_slug("foo_bar") == "foo_bar"
    assert github_slug("Re-order Now") == "re-order-now"


def test_slug_strips_html_and_emphasis():
    assert github_slug("**Bold** Heading") == "bold-heading"
    assert github_slug("Ordering <u>Simple Dose</u>") == "ordering-simple-dose"


def test_slug_collapses_per_space_not_per_run_like_github():
    # GitHub maps each space to a hyphen (a removed colon leaves an extra space)
    assert github_slug("Foo : Bar") == "foo--bar"


def test_slug_unicode_letters_preserved():
    assert github_slug("Café Menu") == "café-menu"


# --- Slugger de-dup --------------------------------------------------------


def test_slugger_dedupes_with_numeric_suffix():
    s = Slugger()
    assert s.slug("Overview") == "overview"
    assert s.slug("Overview") == "overview-1"
    assert s.slug("Overview") == "overview-2"


def test_slugger_suffix_does_not_collide_with_real_heading():
    s = Slugger()
    assert s.slug("Notes") == "notes"
    assert s.slug("Notes 1") == "notes-1"
    assert s.slug("Notes") == "notes-2"  # would-be notes-1 is taken


# --- extract_headings ------------------------------------------------------


def test_extract_headings_levels_and_slugs():
    body = "# Title\n\nsome text\n\n## Section A\n\n### Sub\n"
    hs = extract_headings(body)
    assert hs == [
        Heading(1, "Title", "title"),
        Heading(2, "Section A", "section-a"),
        Heading(3, "Sub", "sub"),
    ]


def test_extract_headings_skips_fenced_code():
    body = "# Real\n\n```\n# not a heading\n```\n\n## Also Real\n"
    hs = extract_headings(body)
    assert [h.text for h in hs] == ["Real", "Also Real"]


def test_extract_headings_dedupes():
    body = "# Notes\n\n## Notes\n"
    hs = extract_headings(body)
    assert [h.slug for h in hs] == ["notes", "notes-1"]


# --- build_anchor_aliases --------------------------------------------------


def test_alias_from_span_on_line_before_heading():
    body = '<span id="_Toc112615110"></span>\n\n# Ordering Inpatient Simple\n'
    aliases = build_anchor_aliases(body)
    assert aliases == {"_Toc112615110": "ordering-inpatient-simple"}


def test_alias_from_id_embedded_in_heading_line():
    body = '# Ordering Simple <a id="OrderingInpatientSimple"></a>\n'
    aliases = build_anchor_aliases(body)
    assert aliases["OrderingInpatientSimple"] == "ordering-simple"


def test_alias_ignores_anchor_far_from_any_heading():
    body = (
        '# A Heading\n\nlots of text here\n\nmore\n\n<span id="orphan"></span>\n\nplain paragraph\n'
    )
    aliases = build_anchor_aliases(body)
    assert "orphan" not in aliases
