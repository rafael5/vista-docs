"""F4 — anchor assignment + alias map (spec §6 F4).

Pure helpers for slugging headings with the GitHub algorithm, de-duplicating
collisions, and recovering legacy Word bookmarks (``_Toc…``, named anchors) into
a ``legacy_id -> slug`` alias map. A later transform (F8) rewrites in-document
``#legacy_id`` references to the slugs recorded here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_TAG_RE = re.compile(r"<[^>]+>")
_EMPH_RE = re.compile(r"[*`]")
# Keep word chars (incl. underscore + unicode letters), hyphen and space; drop rest.
_NON_SLUG_RE = re.compile(r"[^\w\- ]+", re.UNICODE)

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")

_ID_ATTR_RE = re.compile(r'<(?:span|a)\b[^>]*\bid="([^"]+)"')
_NAME_ATTR_RE = re.compile(r'<a\b[^>]*\bname="([^"]+)"')
_PANDOC_ATTR_RE = re.compile(r"\{#([^\s}]+)[^}]*\}")


@dataclass(frozen=True)
class Heading:
    """An ATX heading: depth, raw text, and its (de-duplicated) GitHub slug."""

    level: int
    text: str
    slug: str


def github_slug(text: str) -> str:
    """Slug ``text`` with GitHub's anchor algorithm.

    Lowercase; strip HTML tags and ``*``/`` ` `` emphasis markers; remove
    punctuation except hyphen and underscore; map each remaining space to a
    hyphen (so a removed colon can leave a double hyphen, exactly as GitHub does).
    """
    s = _TAG_RE.sub("", text)
    s = _EMPH_RE.sub("", s)
    s = s.strip().lower()
    s = _NON_SLUG_RE.sub("", s)
    s = s.replace(" ", "-")
    return s


class Slugger:
    """Stateful slugger that de-duplicates repeats with ``-1``, ``-2`` suffixes."""

    def __init__(self) -> None:
        self._seen: dict[str, int] = {}

    def slug(self, text: str) -> str:
        base = github_slug(text)
        if base not in self._seen:
            self._seen[base] = 0
            return base
        n = self._seen[base]
        while True:
            n += 1
            candidate = f"{base}-{n}"
            if candidate not in self._seen:
                break
        self._seen[base] = n
        self._seen[candidate] = 0
        return candidate


def _iter_heading_lines(body: str):
    """Yield ``(line_index, level, raw_text)`` for ATX headings, skipping fences."""
    in_fence = False
    for i, line in enumerate(body.splitlines()):
        st = line.strip()
        if st.startswith("```") or st.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = _HEADING_RE.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2).strip()


def extract_headings(body: str) -> list[Heading]:
    """Return ordered, de-duplicated :class:`Heading` records for ``body``."""
    slugger = Slugger()
    return [
        Heading(level, text, slugger.slug(text)) for _, level, text in _iter_heading_lines(body)
    ]


def build_anchor_aliases(body: str, window: int = 2) -> dict[str, str]:
    """Map each legacy bookmark id to the slug of its nearest heading.

    Scans for ``<span id>`` / ``<a id>`` / ``<a name>`` / pandoc ``{#id}``
    anchors. An id within ``window`` lines of a heading is aliased to that
    heading's slug (ties prefer the *following* heading — anchors mark the start
    of the section they precede). Anchors with no heading in range are ignored.
    """
    lines = body.splitlines()
    slugger = Slugger()
    headings: list[tuple[int, str]] = [
        (i, slugger.slug(text)) for i, _level, text in _iter_heading_lines(body)
    ]
    aliases: dict[str, str] = {}
    for i, line in enumerate(lines):
        for rx in (_ID_ATTR_RE, _NAME_ATTR_RE, _PANDOC_ATTR_RE):
            for mm in rx.finditer(line):
                legacy = mm.group(1)
                best_key: tuple[int, int] | None = None
                best_slug = ""
                for hidx, hslug in headings:
                    dist = abs(hidx - i)
                    if dist <= window:
                        key = (dist, 0 if hidx >= i else 1)
                        if best_key is None or key < best_key:
                            best_key, best_slug = key, hslug
                if best_key is not None:
                    aliases.setdefault(legacy, best_slug)
    return aliases
