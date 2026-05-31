"""Unit tests for F3 heading inference / promotion (normalize stage)."""

from vista_docs.normalize.heading_infer_pure import infer_headings


def test_promotes_chapter():
    body = "intro\n\nChapter 3 Ordering Medications\n\ntext\n"
    out, n = infer_headings(body)
    assert "# Chapter 3 Ordering Medications" in out
    assert n == 1


def test_promotes_appendix():
    body = "x\n\nAppendix D Error Messages\n\ny\n"
    out, n = infer_headings(body)
    assert "# Appendix D Error Messages" in out


def test_numbered_depth():
    body = "p\n\n1 Overview\n\nq\n\n1.2 Ordering Medications\n\nr\n\n1.2.3 Simple Dose\n\ns\n"
    out, _ = infer_headings(body)
    assert "# 1 Overview" in out
    assert "## 1.2 Ordering Medications" in out
    assert "### 1.2.3 Simple Dose" in out


def test_promotes_all_caps_short_line():
    body = "lead\n\nINTRODUCTION\n\nbody\n"
    out, _ = infer_headings(body)
    assert "## INTRODUCTION" in out


def test_promotes_bold_only_line_and_strips_markers():
    body = "lead\n\n**Important Notes**\n\nbody\n"
    out, _ = infer_headings(body)
    assert "### Important Notes" in out


def test_does_not_promote_sentence():
    body = "This is a normal paragraph that ends with a period.\n"
    out, n = infer_headings(body)
    assert out == body
    assert n == 0


def test_does_not_touch_existing_heading():
    body = "# Already A Heading\n\ntext\n"
    out, n = infer_headings(body)
    assert out == body
    assert n == 0


def test_skips_inside_code_fence():
    body = "```\nINTRODUCTION\n```\n"
    out, n = infer_headings(body)
    assert out == body
    assert n == 0


def test_idempotent():
    body = "lead\n\nChapter 1 Start\n\nINTRODUCTION\n\n1.2 Sub\n\nbody\n"
    once, _ = infer_headings(body)
    twice, n2 = infer_headings(once)
    assert twice == once
    assert n2 == 0
