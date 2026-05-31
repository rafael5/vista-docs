"""F1 — whitespace / layout denoise (spec §6 F1).

Pure, idempotent, safe on all document classes. Run first in the normalize
pipeline. Strips the layout noise pandoc replays from Word/PDF originals:

  * runs of >=6 consecutive spaces collapse to a single space (layout padding);
  * form-feeds and other C0 control chars (except tab/newline) are removed;
  * trailing whitespace is trimmed per line;
  * runs of >=3 blank lines collapse to a single blank line.

CRLF/CR line endings are normalized to LF first so the rules apply uniformly.
"""

from __future__ import annotations

import re

# C0 control chars except tab (\x09) and newline (\x0a); includes form-feed (\x0c).
_CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_SPACE_RUN_RE = re.compile(r" {6,}")
_TRAILING_WS_RE = re.compile(r"[ \t]+$", re.MULTILINE)
_BLANK_LINES_RE = re.compile(r"\n{3,}")


def denoise(text: str) -> str:
    """Collapse layout whitespace and strip control chars. Idempotent."""
    if not text:
        return text
    s = text.replace("\r\n", "\n").replace("\r", "\n")
    s = _CTRL_RE.sub("", s)
    s = _SPACE_RUN_RE.sub(" ", s)
    s = _TRAILING_WS_RE.sub("", s)
    s = _BLANK_LINES_RE.sub("\n\n", s)
    return s
