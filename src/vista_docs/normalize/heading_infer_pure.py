"""F3 — heading inference / promotion (spec §6 F3, highest-value transform).

Promotes flattened paragraphs back to ATX headings, *conservatively*: only
standalone lines (a single-line paragraph surrounded by blanks) that match a
strong heading signal are promoted, and never anything already a heading or
inside a code fence. Ambiguous lines are left alone.

Signals (and inferred depth):
  * ``Chapter N`` / ``Appendix X``            -> ``#``
  * numbered prefix ``1`` / ``1.2`` / ``1.2.3`` -> depth = dot-count (capped 3)
  * ALL-CAPS short line                        -> ``##``
  * bold-only short line ``**Text**``          -> ``###`` (markers stripped)

Returns ``(body, promoted_count)``. Idempotent.
"""

from __future__ import annotations

import re

_HEADING_RE = re.compile(r"^#{1,6}\s")
_CHAPTER_RE = re.compile(r"^(?:Chapter\s+\d+|Appendix\s+[A-Z])\b", re.IGNORECASE)
_NUMBERED_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(\S.*)$")
_BOLD_RE = re.compile(r"^\*\*([^*].*?)\*\*$")


def _blank_or_edge(lines: list[str], i: int) -> bool:
    return i < 0 or i >= len(lines) or not lines[i].strip()


def _is_all_caps(s: str) -> bool:
    if not (3 <= len(s) <= 60):
        return False
    if any(c.islower() for c in s):
        return False
    return sum(c.isalpha() for c in s) >= 3


def _promote(line: str) -> str | None:
    """Return the promoted heading line, or ``None`` to leave ``line`` as-is."""
    s = line.strip()
    if _CHAPTER_RE.match(s):
        return f"# {s}"
    m = _NUMBERED_RE.match(s)
    if m and len(s) <= 80 and not s.endswith(".") and m.group(2)[:1].isupper():
        depth = min(m.group(1).count(".") + 1, 3)
        return f"{'#' * depth} {s}"
    if _is_all_caps(s):
        return f"## {s}"
    b = _BOLD_RE.match(s)
    if b and len(b.group(1)) <= 60:
        return f"### {b.group(1).strip()}"
    return None


def infer_headings(body: str) -> tuple[str, int]:
    lines = body.split("\n")
    out = list(lines)
    promoted = 0
    in_fence = False
    for i, line in enumerate(lines):
        st = line.strip()
        if st.startswith("```") or st.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not st or _HEADING_RE.match(line):
            continue
        if not (_blank_or_edge(lines, i - 1) and _blank_or_edge(lines, i + 1)):
            continue
        new = _promote(line)
        if new is not None and new != line:
            out[i] = new
            promoted += 1
    return "\n".join(out), promoted
