"""Unit tests for F8 link rewrite + dead-anchor sweep (normalize stage)."""

from vista_docs.normalize.linkfix_pure import (
    collect_anchor_targets,
    find_dead_anchors,
    rewrite_legacy_links,
)

ALIASES = {
    "_Toc112615110": "ordering-inpatient-simple",
    "OrderingInpatientSimple": "ordering-inpatient-simple",
}


def test_rewrite_markdown_link():
    text = "See [Ordering](#_Toc112615110) now."
    assert rewrite_legacy_links(text, ALIASES) == "See [Ordering](#ordering-inpatient-simple) now."


def test_rewrite_html_href():
    text = '<a href="#OrderingInpatientSimple">x</a>'
    assert rewrite_legacy_links(text, ALIASES) == '<a href="#ordering-inpatient-simple">x</a>'


def test_non_aliased_target_unchanged():
    text = "[keep](#real-slug)"
    assert rewrite_legacy_links(text, ALIASES) == text


def test_empty_aliases_noop():
    text = "[x](#anything)"
    assert rewrite_legacy_links(text, {}) == text


def test_collect_anchor_targets():
    text = '[a](#one) and <a href="#two">b</a> and [ext](https://x)'
    assert collect_anchor_targets(text) == {"one", "two"}


def test_find_dead_anchors():
    body = "[a](#good) [b](#bad) [c](#also-bad)"
    assert find_dead_anchors(body, {"good"}) == ["also-bad", "bad"]


def test_no_dead_anchors():
    body = "[a](#good)"
    assert find_dead_anchors(body, {"good"}) == []
