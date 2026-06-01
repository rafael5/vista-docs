"""Unit tests for the normalize CI lint helpers (spec §11)."""

from vista_docs.normalize.lint_pure import (
    dead_anchors,
    noise_violations,
    sidecar_violations,
    valid_anchor_ids,
)


def test_noise_detects_form_feed_and_space_run():
    v = noise_violations("a\fb\n\nfoo" + " " * 8 + "bar\n")
    assert "form_feed" in v
    assert "space_run" in v


def test_noise_detects_page_number_lines():
    assert "page_number_line" in noise_violations("text\n\nPage 5 of 12\n\nmore\n")
    # An *isolated* numeric line (blank both sides) is an orphan page number.
    assert "page_number_line" in noise_violations("text\n\n233\n\nmore\n")


def test_noise_ignores_numeric_line_with_text_neighbor():
    # Consistent with F2: a number that is content (e.g. table data), not an
    # orphan page number, is left alone — so the linter must not flag it.
    assert noise_violations("cytopath\n8\n86-04\n") == []
    assert noise_violations("blah\n\n230\nFiles 20\n") == []


def test_noise_does_not_flag_redacted_cells():
    # F5 deterministically removes the revision table's PM/TW columns; any
    # remaining "Redacted"/"N/A" cells are legitimate source redactions.
    assert noise_violations("<tr><td>x</td><td>Redacted</td></tr>") == []


def test_clean_body_has_no_noise():
    assert noise_violations("# Title\n\nClean prose here.\n") == []


def test_valid_anchor_ids_includes_heading_slugs_and_explicit_ids():
    body = '# My Heading\n\n<span id="LegacyBookmark"></span>\n\n<a id="p7"></a>\n'
    ids = valid_anchor_ids(body)
    assert "my-heading" in ids
    assert "LegacyBookmark" in ids
    assert "p7" in ids


def test_valid_anchor_ids_recognizes_any_element_id_and_pandoc():
    # Pandoc footnotes define ids on <li> and <a>; headings via {#id}.
    body = (
        '<li id="fn1"><p>note</p></li>\n'
        '<a href="#fn1" id="fnref1">1</a>\n'
        "## Section {#sec-x}\n"
        "[]{#legacy}\n"
    )
    ids = valid_anchor_ids(body)
    assert {"fn1", "fnref1", "sec-x", "legacy"} <= ids


def test_footnote_links_not_flagged_dead():
    body = '<a href="#fn1" id="fnref1">1</a>\n<li id="fn1">note <a href="#fnref1">back</a></li>\n'
    assert dead_anchors(body) == []


def test_sidecar_ok_when_present_and_backref_matches():
    assert sidecar_violations("x.md", "x.history.yaml", {"x.history.yaml"}, "x.md") == []


def test_sidecar_none_is_clean():
    assert sidecar_violations("x.md", None, set()) == []


def test_sidecar_missing_file():
    v = sidecar_violations("x.md", "x.history.yaml", set(), "x.md")
    assert v == ["missing_sidecar:x.history.yaml"]


def test_sidecar_backref_mismatch():
    v = sidecar_violations("x.md", "x.history.yaml", {"x.history.yaml"}, "other.md")
    assert v == ["sidecar_backref_mismatch:other.md"]


def test_dead_anchors_flags_unresolved_targets():
    body = "# Real Heading\n\n[ok](#real-heading) and [bad](#missing-target)\n"
    assert dead_anchors(body) == ["missing-target"]


def test_no_dead_anchors_when_all_resolve():
    body = '# Real Heading\n\n<span id="Legacy"></span>\n\n[a](#real-heading) [b](#Legacy)\n'
    assert dead_anchors(body) == []
