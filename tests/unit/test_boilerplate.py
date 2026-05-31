"""Unit tests for F2 running header/footer stripping (normalize stage)."""

from vista_docs.normalize.boilerplate_pure import strip_boilerplate


def test_removes_page_n_of_m_lines():
    body = "para one\n\nPage 5 of 12\n\npara two\n"
    out, n = strip_boilerplate(body)
    assert "Page 5 of 12" not in out
    assert n == 1
    assert "para one" in out and "para two" in out


def test_removes_repeated_running_header():
    header = "CPRS User Manual June 2023"
    body = f"{header}\n\nintro\n\n{header}\n\nmiddle\n\n{header}\n\nend\n"
    out, n = strip_boilerplate(body)
    assert header not in out
    assert n == 3


def test_removes_isolated_page_number():
    body = "end of section.\n\n233\n\nNext Section\n"
    out, n = strip_boilerplate(body)
    assert "\n233\n" not in out
    assert n == 1


def test_keeps_number_adjacent_to_text():
    body = "step 1\n3\nis the answer\n"
    out, n = strip_boilerplate(body)
    assert "3" in out
    assert n == 0


def test_does_not_remove_infrequent_header_like_line():
    body = "Some Title March 2020\n\nbody\n"
    out, n = strip_boilerplate(body)
    assert "Some Title March 2020" in out
    assert n == 0


def test_idempotent():
    body = "x\n\nPage 1 of 9\n\n233\n\ny\n"
    once, _ = strip_boilerplate(body)
    twice, n2 = strip_boilerplate(once)
    assert twice == once
    assert n2 == 0
