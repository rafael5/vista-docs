"""Unit tests for F3a — unwrap pandoc TOC/nav-link wrapping (normalize stage).

The real consolidated CPRS doc wraps ~1850 prose lines in dead "return-to-TOC"
links: ``[[text](#_TocNNN)](#_TocMMM)`` (double), ``[text](#_TocMMM)`` (single),
and empty ``[[ ](#bookmark)](#_TocMMM)`` markers — all pointing at anchors that
are never *defined* in the document. Unwrapping recovers clean text and removes
the dead anchors, so F3 heading inference / F8 dead-anchor sweep can work.
"""

from vista_docs.normalize.delink_pure import defined_anchor_ids, unwrap_toc_links


def test_unwrap_double_wrapped_line():
    body = "[[The Computerized Patient Record System is great](#_Toc604)](#_Toc476)\n"
    out, n = unwrap_toc_links(body)
    assert out == "The Computerized Patient Record System is great\n"
    assert n == 1


def test_unwrap_preserves_inner_inline_link():
    body = "[[See [details](#x) here](#_Toc604)](#_Toc476)\n"
    out, _ = unwrap_toc_links(body)
    assert out == "See [details](#x) here\n"


def test_remove_empty_multiline_wrapper():
    body = "before\n\n[[  \n](#OR_signature_key_update)](#_Toc476)\n\nafter\n"
    out, n = unwrap_toc_links(body)
    assert "OR_signature_key_update" not in out
    assert "before" in out and "after" in out
    assert n == 1


def test_unwrap_single_link_to_undefined_target():
    body = "Plain paragraph wrapped in nav link.](#_Toc476)\n"  # not a wrapper
    # full-line single link form:
    body = "[Plain paragraph wrapped in nav link](#_Toc476)\n"
    out, n = unwrap_toc_links(body)
    assert out == "Plain paragraph wrapped in nav link\n"
    assert n == 1


def test_preserve_single_link_to_defined_target():
    body = '<span id="fig1" class="anchor"></span>\n\n[See the figure](#fig1)\n'
    out, n = unwrap_toc_links(body)
    assert "[See the figure](#fig1)" in out  # legitimate link preserved
    assert n == 0


def test_preserve_normal_prose_and_inline_links():
    body = "Normal text with an [inline link](#defined) mid-sentence.\n"
    out, n = unwrap_toc_links(body, defined={"defined"})
    assert out == body
    assert n == 0


def test_defined_anchor_ids_collects_spans_and_pandoc():
    body = '<span id="a1" class="anchor"></span>\n<a name="a2">x</a>\n[]{#a3}\n'
    assert defined_anchor_ids(body) == {"a1", "a2", "a3"}


def test_unwrap_blockquote_prefixed_double():
    body = "> [[This dialog saves clinic lists](#_Toc464)](#_Toc476)\n"
    out, n = unwrap_toc_links(body)
    assert out == "> This dialog saves clinic lists\n"
    assert n == 1


def test_unwrap_list_prefixed_single_to_dead_target():
    body = "- [Select Save For All Days](#_Toc476)\n"
    out, n = unwrap_toc_links(body)
    assert out == "- Select Save For All Days\n"
    assert n == 1


def test_unwrap_inline_double_wrapper_mid_line():
    body = "Prefix text [[wrapped bit](#_Toc464)](#_Toc476) suffix text\n"
    out, n = unwrap_toc_links(body)
    assert out == "Prefix text wrapped bit suffix text\n"
    assert n == 1


def test_does_not_corrupt_line_of_two_inline_links():
    body = "[first](#a) and [second](#b)\n"
    out, n = unwrap_toc_links(body, defined=set())
    assert out == body
    assert n == 0


def test_idempotent():
    body = "[[Heading text](#_Toc604)](#_Toc476)\n[A para](#_Toc476)\n"
    once, _ = unwrap_toc_links(body)
    twice, n2 = unwrap_toc_links(once)
    assert twice == once
    assert n2 == 0
