"""Unit tests for F8 link rewrite + dead-anchor sweep (normalize stage)."""

from vista_docs.normalize.linkfix_pure import (
    collect_anchor_targets,
    find_dead_anchors,
    rewrite_legacy_links,
    sweep_dead_links,
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


# --- sweep_dead_links ------------------------------------------------------


def test_sweep_strips_dead_internal_link_to_text():
    out, n = sweep_dead_links("See [the section](#missing) now.", {"real"})
    assert out == "See the section now."
    assert n == 1


def test_sweep_preserves_valid_link():
    body = "[ok](#real)"
    assert sweep_dead_links(body, {"real"}) == (body, 0)


def test_sweep_preserves_external_link():
    body = "[site](https://example.com)"
    assert sweep_dead_links(body, set()) == (body, 0)


def test_sweep_unwraps_dead_html_anchor_keeps_inner_markup():
    out, n = sweep_dead_links('<a href="#dead"><strong>X</strong></a>', set())
    assert out == "<strong>X</strong>"
    assert n == 1


def test_sweep_preserves_valid_html_anchor():
    body = '<a href="#fig1">img</a>'
    assert sweep_dead_links(body, {"fig1"}) == (body, 0)


def test_sweep_counts_multiple_and_keeps_valid():
    out, n = sweep_dead_links("[a](#x) [b](#y) [c](#keep)", {"keep"})
    assert out == "a b [c](#keep)"
    assert n == 2


def test_sweep_idempotent():
    once, _ = sweep_dead_links("[a](#x) [b](#keep)", {"keep"})
    twice, n2 = sweep_dead_links(once, {"keep"})
    assert twice == once
    assert n2 == 0
