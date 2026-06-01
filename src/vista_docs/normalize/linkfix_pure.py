"""F8 — link rewrite + dead-anchor sweep (spec §6 F8).

Runs LAST, once every anchor is finalized. Rewrites in-document ``#legacy_id``
references to their slugs via the F4 alias map, collects every in-document anchor
target, and reports targets that resolve to no known slug (the CI dead-anchor
gate).
"""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping

_LINK_TARGET_RE = re.compile(r"\]\(#([^)]+)\)")
_HREF_RE = re.compile(r'href="#([^"]+)"')
# Inline markdown link to an internal anchor: [text](#id). The text may contain
# escaped brackets (``\[CODE\]``, common in VistA TOC entries) but stops at the
# first *unescaped* ``]`` so adjacent links are never merged.
_MD_LINK_RE = re.compile(r"\[((?:\\.|[^\]\\])+)\]\(#([^)]+)\)")
# Whole html anchor to an internal target: <a ... href="#id" ...>inner</a>.
_HTML_A_RE = re.compile(r'<a\b[^>]*\bhref="#([^"]+)"[^>]*>(.*?)</a>', re.DOTALL)


def rewrite_legacy_links(text: str, aliases: Mapping[str, str]) -> str:
    """Rewrite ``](#legacy)`` and ``href="#legacy"`` targets via ``aliases``."""
    if not aliases:
        return text

    def repl_md(m: re.Match[str]) -> str:
        tgt = m.group(1)
        return f"](#{aliases[tgt]})" if tgt in aliases else m.group(0)

    def repl_href(m: re.Match[str]) -> str:
        tgt = m.group(1)
        return f'href="#{aliases[tgt]}"' if tgt in aliases else m.group(0)

    text = _LINK_TARGET_RE.sub(repl_md, text)
    return _HREF_RE.sub(repl_href, text)


def collect_anchor_targets(text: str) -> set[str]:
    """Return the set of in-document anchor ids referenced by ``text``."""
    return set(_LINK_TARGET_RE.findall(text)) | set(_HREF_RE.findall(text))


def find_dead_anchors(body: str, valid_slugs: Iterable[str]) -> list[str]:
    """Sorted list of referenced anchors that match no known slug."""
    valid = set(valid_slugs)
    return sorted(t for t in collect_anchor_targets(body) if t not in valid)


def sweep_dead_links(body: str, valid_ids: Iterable[str]) -> tuple[str, int]:
    """Neutralize internal links whose target resolves to nothing.

    Runs LAST (after alias rewriting), so any reference an alias could resolve is
    already a valid slug and is preserved. A markdown ``[text](#dead)`` collapses
    to ``text``; an html ``<a href="#dead">inner</a>`` collapses to ``inner``
    (keeping any inline markup). Links to a ``valid_ids`` target and external
    links are untouched. Returns ``(body, swept_count)``; idempotent.
    """
    valid = set(valid_ids)
    total = 0
    # Iterate to a fixpoint: stripping a dead *outer* link can reveal a dead
    # *inner* link (`[… [x](#dead1) …](#dead2)`) that one re.sub pass skips.
    while True:
        body, n = _sweep_pass(body, valid)
        total += n
        if not n:
            return body, total


def _sweep_pass(body: str, valid: set[str]) -> tuple[str, int]:
    count = 0

    def md(m: re.Match[str]) -> str:
        nonlocal count
        if m.group(2) in valid:
            return m.group(0)
        count += 1
        return m.group(1)

    def html(m: re.Match[str]) -> str:
        nonlocal count
        if m.group(1) in valid:
            return m.group(0)
        count += 1
        return m.group(2)

    body = _MD_LINK_RE.sub(md, body)
    body = _HTML_A_RE.sub(html, body)
    return body, count
