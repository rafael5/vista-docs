"""Unit tests for F9 figure/caption recovery (normalize stage)."""

from vista_docs.normalize.figures_pure import recover_figures


def test_caption_after_image_becomes_alt():
    body = "![](dir/003.png)\n\nFigure 3: Order entry dialog\n"
    out = recover_figures(body)
    assert "![Figure 3: Order entry dialog](dir/003.png)" in out


def test_caption_before_image_becomes_alt():
    body = "Figure 5: Sign-on screen\n\n![](dir/005.png)\n"
    out = recover_figures(body)
    assert "![Figure 5: Sign-on screen](dir/005.png)" in out


def test_no_caption_leaves_image_untouched():
    body = "![](dir/001.png)\n\nSome unrelated paragraph.\n"
    assert recover_figures(body) == body


def test_existing_alt_not_overwritten():
    body = "![Already set](dir/002.png)\n\nFigure 2: Ignored caption\n"
    assert recover_figures(body) == body


def test_idempotent():
    body = "![](dir/003.png)\n\nFigure 3: Order entry dialog\n"
    once = recover_figures(body)
    assert recover_figures(once) == once
