"""Unit tests for F7 page-number bridge pure logic (normalize stage)."""

from vista_docs.normalize.page_bridge_pure import (
    inject_page_anchors,
    map_pages_to_slugs,
    page_anchor_markup,
    retire_page_anchors,
    rewrite_page_toc,
)


def test_markup_format():
    assert page_anchor_markup(123) == '<a id="p123"></a><!-- page 123 -->'


def test_inject_before_lines():
    body = "alpha\nbeta\ngamma\n"
    out = inject_page_anchors(body, [(1, 1), (2, 2)])
    assert out == (
        "alpha\n"
        '<a id="p1"></a><!-- page 1 -->\n'
        "beta\n"
        '<a id="p2"></a><!-- page 2 -->\n'
        "gamma\n"
    )


def test_map_pages_to_following_heading_slug():
    body = (
        '<a id="p10"></a><!-- page 10 -->\n\n'
        "# Agent Cashier Menu\n\nbody\n\n"
        '<a id="p20"></a><!-- page 20 -->\n\n'
        "## Balances\n"
    )
    assert map_pages_to_slugs(body) == {"p10": "agent-cashier-menu", "p20": "balances"}


def test_rewrite_page_toc():
    toc = [
        {"title": "Agent Cashier Menu", "page": 10, "anchor": "#p10"},
        {"title": "Balances", "page": 20, "anchor": "#p20"},
    ]
    out = rewrite_page_toc(toc, {"p10": "agent-cashier-menu", "p20": "balances"})
    assert out[0]["anchor"] == "#agent-cashier-menu"
    assert out[1]["anchor"] == "#balances"
    # original untouched
    assert toc[0]["anchor"] == "#p10"


def test_retire_removes_markers():
    body = 'x\n<a id="p1"></a><!-- page 1 -->\ny\n<a id="p2"></a><!-- page 2 -->\nz\n'
    out, n = retire_page_anchors(body)
    assert n == 2
    assert "<!-- page" not in out
    assert '<a id="p' not in out
    assert "x" in out and "y" in out and "z" in out


def test_retire_idempotent():
    body = 'a\n<a id="p5"></a><!-- page 5 -->\nb\n'
    once, _ = retire_page_anchors(body)
    twice, n2 = retire_page_anchors(once)
    assert twice == once
    assert n2 == 0
