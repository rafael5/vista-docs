"""Unit tests for F10 table policy (normalize stage)."""

from vista_docs.normalize.tables_pure import (
    convert_tables,
    html_table_to_gfm,
    is_complex_table,
)

SIMPLE = (
    "<table>\n<thead>\n<tr><th>Date</th><th>Change</th></tr>\n</thead>\n"
    "<tbody>\n<tr><td>06/2023</td><td>Added <strong>warning</strong></td></tr>\n"
    "<tr><td>05/2023</td><td>Fixed bug</td></tr>\n</tbody>\n</table>"
)

COLSPAN = '<table><tr><td colspan="2">Merged</td></tr><tr><td>a</td><td>b</td></tr></table>'

NESTED = (
    "<table><thead><tr><th>H</th></tr></thead>"
    "<tbody><tr><td><ul><li>one</li><li>two</li></ul></td></tr></tbody></table>"
)


def test_is_complex_detects_colspan():
    assert is_complex_table(COLSPAN) is True


def test_is_complex_detects_nested_list():
    assert is_complex_table(NESTED) is True


def test_simple_table_is_not_complex():
    assert is_complex_table(SIMPLE) is False


def test_simple_table_to_gfm():
    gfm = html_table_to_gfm(SIMPLE)
    assert gfm == (
        "| Date | Change |\n| --- | --- |\n| 06/2023 | Added warning |\n| 05/2023 | Fixed bug |"
    )


def test_complex_table_returns_none():
    assert html_table_to_gfm(COLSPAN) is None
    assert html_table_to_gfm(NESTED) is None


def test_pipe_in_cell_is_escaped():
    html = "<table><thead><tr><th>A</th></tr></thead><tbody><tr><td>x|y</td></tr></tbody></table>"
    assert "x\\|y" in html_table_to_gfm(html)


def test_convert_tables_replaces_simple_keeps_complex():
    body = f"Intro\n\n{SIMPLE}\n\nMiddle\n\n{COLSPAN}\n\nEnd\n"
    out = convert_tables(body)
    assert "| Date | Change |" in out  # simple converted
    assert 'colspan="2"' in out  # complex left as raw HTML
    assert "<table>" in out  # the complex one survives


def test_convert_tables_idempotent():
    body = f"x\n\n{SIMPLE}\n"
    once = convert_tables(body)
    assert convert_tables(once) == once
