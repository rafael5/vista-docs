"""F6 — TOC generation (spec §6 F6).

Builds a portable, link-based table of contents from the heading tree produced
by :func:`vista_docs.normalize.anchors_pure.extract_headings` (which the runner
sources from the stage-6.5 chunk tree). Headings deeper than ``max_level`` are
omitted; indentation is relative to the shallowest included heading.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from vista_docs.normalize.anchors_pure import Heading

_TAG_RE = re.compile(r"<[^>]+>")
_EMPH_RE = re.compile(r"[*`]")
_WS_RE = re.compile(r"\s+")


def _display_text(text: str) -> str:
    s = _TAG_RE.sub("", text)
    s = _EMPH_RE.sub("", s)
    return _WS_RE.sub(" ", s).strip()


def build_toc(headings: Sequence[Heading], max_level: int = 3, heading: str = "Contents") -> str:
    """Render a nested markdown TOC. Returns ``""`` when nothing is in range."""
    items = [h for h in headings if h.level <= max_level]
    if not items:
        return ""
    base = min(h.level for h in items)
    lines = [f"## {heading}", ""]
    for h in items:
        indent = "  " * (h.level - base)
        lines.append(f"{indent}- [{_display_text(h.text)}](#{h.slug})")
    return "\n".join(lines) + "\n"
