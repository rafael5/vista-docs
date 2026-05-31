"""Unit tests for F1 whitespace/layout denoise (normalize stage)."""

from vista_docs.normalize.denoise_pure import denoise


def test_collapses_long_space_runs_to_single_space():
    assert denoise("foo" + " " * 12 + "bar") == "foo bar"


def test_all_space_line_becomes_empty():
    text = "para1\n" + " " * 2000 + "\npara2"
    assert denoise(text) == "para1\n\npara2"


def test_removes_form_feeds_and_control_chars():
    assert denoise("a\fb") == "ab"
    assert denoise("a\x00\x07b") == "ab"


def test_keeps_tabs_and_newlines():
    assert denoise("a\tb\nc") == "a\tb\nc"


def test_trims_trailing_whitespace_per_line():
    assert denoise("line1   \nline2\t\n") == "line1\nline2\n"


def test_collapses_three_or_more_blank_lines_to_one():
    assert denoise("a\n\n\n\n\nb") == "a\n\nb"


def test_normalizes_crlf():
    assert denoise("a\r\nb\rc") == "a\nb\nc"


def test_short_space_runs_preserved():
    # fewer than 6 spaces is normal prose spacing — untouched
    assert denoise("a     b") == "a     b"  # 5 spaces


def test_idempotent():
    raw = "x" + " " * 30 + "y\n\n\n\n\fz   \n"
    once = denoise(raw)
    assert denoise(once) == once


def test_empty_string():
    assert denoise("") == ""
