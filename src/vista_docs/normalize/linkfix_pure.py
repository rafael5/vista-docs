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
