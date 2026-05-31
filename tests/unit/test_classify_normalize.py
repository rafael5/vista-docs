"""Unit tests for the normalize-stage document classifier (spec §8)."""

from vista_docs.normalize.classify_pure import DocFeatures, classify


def _f(**kw):
    base = dict(
        has_headings=False,
        has_word_anchors=False,
        has_inferred_headings=False,
        is_paginated=False,
        has_pdf=False,
    )
    base.update(kw)
    return DocFeatures(**base)


def test_class_a_modern_word_anchors():
    r = classify(_f(has_headings=True, has_word_anchors=True))
    assert r.doc_class == "A"
    assert r.anchors_source == "word"
    assert r.toc == "generated"
    assert r.page_bridge is False


def test_class_a_mixed_when_word_and_inferred():
    r = classify(_f(has_headings=True, has_word_anchors=True, has_inferred_headings=True))
    assert r.doc_class == "A"
    assert r.anchors_source == "mixed"


def test_class_b_headings_only():
    r = classify(_f(has_headings=True))
    assert r.doc_class == "B"
    assert r.anchors_source == "none"
    assert r.toc == "generated"


def test_class_c_flat_paginated_with_pdf():
    r = classify(_f(has_inferred_headings=True, is_paginated=True, has_pdf=True))
    assert r.doc_class == "C"
    assert r.anchors_source == "inferred"
    assert r.toc == "generated"
    assert r.page_bridge is True


def test_class_c_no_pdf_no_bridge():
    r = classify(_f(has_inferred_headings=True, is_paginated=True, has_pdf=False))
    assert r.doc_class == "C"
    assert r.page_bridge is False


def test_class_d_hopeless():
    r = classify(_f())
    assert r.doc_class == "D"
    assert r.toc == "none"
    assert r.anchors_source == "none"
    assert r.page_bridge is False
