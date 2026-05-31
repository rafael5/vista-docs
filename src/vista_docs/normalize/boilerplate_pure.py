"""F2 — running header/footer stripping (spec §6 F2).

Removes the page furniture pandoc replays from Word layout:

  * ``Page N`` / ``Page N of M`` footer lines;
  * running header/footer lines that recur >=3 times and carry a month-year or
    ``Page`` token (a fuzzy per-document template);
  * isolated page-number-only lines (a bare integer alone on its own line).

Returns ``(body, removed_count)``. Idempotent: a second pass removes nothing.
"""

from __future__ import annotations

import re
from collections import Counter

_PAGE_LINE_RE = re.compile(r"^\s*Page\s+\d+(?:\s+of\s+\d+)?\s*$", re.IGNORECASE)
_NUM_ONLY_RE = re.compile(r"^\s*\d{1,4}\s*$")
_MONTH_RE = re.compile(
    r"\b(January|February|March|April|May|June|July|August|September|"
    r"October|November|December)\b",
    re.IGNORECASE,
)
_WS_RE = re.compile(r"\s+")


def _norm(s: str) -> str:
    return _WS_RE.sub(" ", s).strip()


def _blank_or_edge(lines: list[str], i: int) -> bool:
    return i < 0 or i >= len(lines) or not lines[i].strip()


def strip_boilerplate(body: str) -> tuple[str, int]:
    lines = body.split("\n")
    counts = Counter(_norm(line) for line in lines if _norm(line))
    repeated = {
        key
        for key, c in counts.items()
        if c >= 3 and (_MONTH_RE.search(key) or "page" in key.lower())
    }
    out: list[str] = []
    removed = 0
    for i, line in enumerate(lines):
        norm = _norm(line)
        if _PAGE_LINE_RE.match(line):
            removed += 1
            continue
        if norm and norm in repeated:
            removed += 1
            continue
        if (
            _NUM_ONLY_RE.match(line)
            and _blank_or_edge(lines, i - 1)
            and _blank_or_edge(lines, i + 1)
        ):
            removed += 1
            continue
        out.append(line)
    return "\n".join(out), removed
