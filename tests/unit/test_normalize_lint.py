"""Unit tests for the normalize CI lint helpers (spec §11)."""

from vista_docs.normalize.lint_pure import (
    dead_anchors,
    noise_violations,
    valid_anchor_ids,
)


def test_noise_detects_form_feed_and_space_run():
    v = noise_violations("a\fb\n\nfoo" + " " * 8 + "bar\n")
    assert "form_feed" in v
    assert "space_run" in v


def test_noise_detects_page_number_lines():
    assert "page_number_line" in noise_violations("text\n\nPage 5 of 12\n\nmore\n")
    assert "page_number_line" in noise_violations("text\n\n233\n\nmore\n")


def test_noise_detects_redacted_cells():
    assert "redacted_cell" in noise_violations("<tr><td>x</td><td>Redacted</td></tr>")
    assert "redacted_cell" in noise_violations("<tr><td>x</td><td>N/A</td></tr>")


def test_clean_body_has_no_noise():
    assert noise_violations("# Title\n\nClean prose here.\n") == []


def test_valid_anchor_ids_includes_heading_slugs_and_explicit_ids():
    body = '# My Heading\n\n<span id="LegacyBookmark"></span>\n\n<a id="p7"></a>\n'
    ids = valid_anchor_ids(body)
    assert "my-heading" in ids
    assert "LegacyBookmark" in ids
    assert "p7" in ids


def test_dead_anchors_flags_unresolved_targets():
    body = "# Real Heading\n\n[ok](#real-heading) and [bad](#missing-target)\n"
    assert dead_anchors(body) == ["missing-target"]


def test_no_dead_anchors_when_all_resolve():
    body = '# Real Heading\n\n<span id="Legacy"></span>\n\n[a](#real-heading) [b](#Legacy)\n'
    assert dead_anchors(body) == []
