"""F9 — figure / caption recovery (spec §6 F9).

Pandoc emits bare ``![](dir/001.png)`` images. Where a ``Figure N: …`` caption
sits immediately adjacent (the next or previous non-blank line), fold it into the
image alt text for searchability and accessibility. Images that already carry alt
text are left untouched, so the transform is idempotent.
"""

from __future__ import annotations

import re

_IMG_RE = re.compile(r"^!\[\]\(([^)]+)\)\s*$")
_CAPTION_RE = re.compile(r"^(Figure\s+\d+[.:]?\s+.+?)\s*$", re.IGNORECASE)


def _caption_on(lines: list[str], idx: int) -> str | None:
    if 0 <= idx < len(lines):
        m = _CAPTION_RE.match(lines[idx])
        if m:
            return m.group(1)
    return None


def _next_nonblank(lines: list[str], i: int, step: int) -> int:
    j = i + step
    while 0 <= j < len(lines) and not lines[j].strip():
        j += step
    return j


def recover_figures(body: str) -> str:
    lines = body.splitlines(keepends=False)
    out = list(lines)
    for i, line in enumerate(lines):
        m = _IMG_RE.match(line)
        if not m:
            continue
        caption = _caption_on(lines, _next_nonblank(lines, i, 1)) or _caption_on(
            lines, _next_nonblank(lines, i, -1)
        )
        if caption:
            out[i] = f"![{caption}]({m.group(1)})"
    text = "\n".join(out)
    if body.endswith("\n") and not text.endswith("\n"):
        text += "\n"
    return text
