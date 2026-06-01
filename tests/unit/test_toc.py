"""Unit tests for F6 TOC generation (normalize stage)."""

from vista_docs.normalize.anchors_pure import Heading
from vista_docs.normalize.toc_pure import build_toc


def test_build_toc_nested():
    hs = [
        Heading(
            1,
            "Ordering Inpatient Medications (Simple Dose)",
            "ordering-inpatient-medications-simple-dose",
        ),
        Heading(2, "Complex Dose", "complex-dose"),
    ]
    toc = build_toc(hs)
    assert toc == (
        "## Table of Contents\n\n"
        "- [Ordering Inpatient Medications (Simple Dose)]"
        "(#ordering-inpatient-medications-simple-dose)\n"
        "  - [Complex Dose](#complex-dose)\n"
    )


def test_build_toc_heading_matches_back_link_anchor():
    # The injected back-to-toc links target '#table-of-contents'; the generated
    # heading must slug to exactly that, or the back-links go dead.
    toc = build_toc([Heading(1, "Intro", "intro")])
    assert toc.startswith("## Table of Contents\n")


def test_build_toc_excludes_below_max_level():
    hs = [Heading(1, "A", "a"), Heading(2, "B", "b"), Heading(4, "Deep", "deep")]
    toc = build_toc(hs, max_level=3)
    assert "Deep" not in toc
    assert "- [A](#a)" in toc


def test_build_toc_cleans_html_in_display_text():
    hs = [Heading(2, "Ordering <u>Simple</u> **Dose**", "ordering-simple-dose")]
    toc = build_toc(hs)
    assert "- [Ordering Simple Dose](#ordering-simple-dose)" in toc


def test_build_toc_empty_when_no_headings():
    assert build_toc([]) == ""
    assert build_toc([Heading(4, "Deep", "deep")], max_level=3) == ""


def test_build_toc_indents_relative_to_shallowest():
    hs = [Heading(2, "Top", "top"), Heading(3, "Child", "child")]
    toc = build_toc(hs)
    assert "- [Top](#top)" in toc
    assert "  - [Child](#child)" in toc
