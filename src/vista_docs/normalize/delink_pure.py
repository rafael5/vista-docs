"""F3a — unwrap pandoc TOC / navigation-link wrapping (spec §6 F3, real-corpus).

Discovered on the CPRS GUI UM prototype (impl-plan Change Log 2026-05-31): pandoc
renders the Word "return to TOC" hyperlink that decorates every paragraph as a
link wrapper around the text, e.g.

    [[The Computerized Patient Record System …](#_Toc17877604)](#_Toc17877476)
    [A normal paragraph …](#_Toc17877476)
    [[  ](#OR_signature_key_update)](#_Toc17877476)        # empty bookmark marker

All such targets are dead — they are *referenced* but never *defined* anywhere in
the document. This transform recovers the clean inner text and drops the dead
anchors, which (a) un-mangles ~1850 prose lines, (b) lets F3 infer real headings
from the recovered text, and (c) removes the dead targets before F8's sweep.

Conservative: a single ``[text](#id)`` link is only unwrapped when its target is
**not defined** in the document, so legitimate cross-references to a real
``<span id>`` / ``<a name>`` / pandoc ``[]{#id}`` anchor are preserved. A nested
``[[…](#a)](#b)`` link-wrapping-a-link is never legitimate prose, so it is always
unwrapped.
"""

from __future__ import annotations

import re

from vista_docs.normalize.anchors_pure import extract_headings

# Nested wrapper ``[[TEXT](#a)](#b)`` anywhere (prefixes/inline/multi-line). The
# double ``](#..)](#..)`` close is unambiguous, so a lazy global match is safe:
# the inner TEXT may itself contain a single inline ``[x](#y)`` link.
_DBL_RE = re.compile(r"\[\[(?P<text>.*?)\]\(#[^)]+\)\]\(#[^)]+\)", re.DOTALL)
# Whole-line single link (optional ``>`` / ``-`` / ``*`` prefix) whose text holds
# no ``]`` — i.e. the entire line is one link, not a sentence of two. Unwrapped
# only when the target is dead (undefined), so real cross-references survive.
_SGL_LINE_RE = re.compile(r"^(?P<prefix>>\s+|[-*]\s+|)\[(?P<text>[^\]]*)\]\(#(?P<a>[^)]+)\)$")

_DEF_ATTR_RE = re.compile(r'<(?:span|a)\b[^>]*\b(?:id|name)="([^"]+)"')
_DEF_PANDOC_RE = re.compile(r"\[\]\{#([^}\s]+)")


def defined_anchor_ids(body: str) -> set[str]:
    """Anchor ids that are actually *defined* in ``body`` (link targets that resolve)."""
    ids = set(_DEF_ATTR_RE.findall(body))
    ids.update(_DEF_PANDOC_RE.findall(body))
    return ids


def unwrap_toc_links(body: str, defined: set[str] | None = None) -> tuple[str, int]:
    """Unwrap dead TOC/nav-link wrapping. Returns ``(body, unwrapped_count)``.

    ``defined`` is the set of resolvable in-doc targets — explicit ids plus
    heading slugs — so legitimate links (incl. generated TOC entries) survive.
    """
    if defined is None:
        defined = defined_anchor_ids(body) | {h.slug for h in extract_headings(body)}

    body, count = _DBL_RE.subn(lambda m: m.group("text"), body)

    out: list[str] = []
    for line in body.split("\n"):
        m = _SGL_LINE_RE.match(line.rstrip())
        if m and m.group("a") not in defined:
            out.append(m.group("prefix") + m.group("text"))
            count += 1
        else:
            out.append(line)
    return "\n".join(out), count
