"""
Pure markdown post-processing for VA DOCX → markdown output.

All functions take a markdown string and return a cleaned markdown string.
No I/O, no external dependencies.
"""

from __future__ import annotations

import html
import re

# ---------------------------------------------------------------------------
# TOC stripping
# ---------------------------------------------------------------------------

# HTML-comment-fenced TOC (e.g. from markdown-toc generators)
_TOC_COMMENT_RE = re.compile(
    r"<!-- TOC -->.*?<!-- /TOC -->",
    re.DOTALL | re.IGNORECASE,
)

# Docling-style TOC: bold "Table of Contents" header + following link list
_TOC_HEADING_RE = re.compile(
    r"\*\*Table of Contents\*\*\n+(?:[-*]\s*\[.*?\]\(#.*?\)\n*)+",
    re.IGNORECASE,
)


def strip_toc(md: str) -> str:
    """Remove TOC blocks from markdown."""
    md = _TOC_COMMENT_RE.sub("", md)
    md = _TOC_HEADING_RE.sub("", md)
    return md


# ---------------------------------------------------------------------------
# Heading normalisation
# ---------------------------------------------------------------------------

_HEADING_RE = re.compile(r"^(#{1,6})\s+(\d+(?:\.\d+)*\.?)\s+(.+)$", re.MULTILINE)
_HEADING_LINE_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)


def strip_outline_numbering(md: str) -> str:
    """Remove leading outline numbers from headings (e.g. '# 1.2.3 Title' → '# Title')."""
    return _HEADING_RE.sub(r"\1 \3", md)


def cap_heading_depth(md: str) -> str:
    """Cap heading depth at H4: H5/H6 become H4."""

    def _cap(m: re.Match[str]) -> str:
        hashes = m.group(1)
        if len(hashes) > 4:
            return "#### "
        return hashes + " "

    return _HEADING_LINE_RE.sub(_cap, md)


# ---------------------------------------------------------------------------
# Callout formatting
# ---------------------------------------------------------------------------

_CALLOUT_PREFIXES = ["NOTE", "WARNING", "CAUTION", "IMPORTANT", "REMINDER"]
_CALLOUT_RE = re.compile(
    r"^(" + "|".join(_CALLOUT_PREFIXES) + r"):\s*(.*)$",
    re.MULTILINE | re.IGNORECASE,
)


def format_callouts(md: str) -> str:
    """Convert 'NOTE: text' paragraphs into '> **NOTE:** text' blockquotes."""

    def _replace(m: re.Match[str]) -> str:
        keyword = m.group(1).upper()
        body = m.group(2)
        return f"> **{keyword}:** {body}"

    return _CALLOUT_RE.sub(_replace, md)


# ---------------------------------------------------------------------------
# Boilerplate stripping
# ---------------------------------------------------------------------------

_BOILERPLATE_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"^Department of Veterans Affairs\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^Veterans Health Administration\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^Office of Information\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^Washington,\s*DC\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^Version\s+\d+\.\d+\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^Revised\s+\w+\s+\d{4}\s*$", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^This page intentionally left blank\s*$", re.MULTILINE | re.IGNORECASE),
]


def strip_boilerplate(md: str) -> str:
    """Remove VA title page boilerplate lines."""
    for pattern in _BOILERPLATE_PATTERNS:
        md = pattern.sub("", md)
    return md


# ---------------------------------------------------------------------------
# Pandoc pipeline: artifact stripping
# ---------------------------------------------------------------------------


def strip_artifacts(text: str) -> str:
    """Remove HTML comment artifacts from Word track-changes / hidden fields."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*\s*\*\*", "", text)  # empty bold
    text = re.sub(r"\*\s*\*", "", text)  # empty italic
    text = re.sub(r"^>\s*$", "", text, flags=re.MULTILINE)  # stray empty blockquotes
    return text


# ---------------------------------------------------------------------------
# Word TOC stripping (Pandoc output — three forms)
# ---------------------------------------------------------------------------


def strip_word_toc(text: str) -> str:
    """
    Remove Word TOC artifacts from Pandoc output.

    Form 1 — plain bare link lines:  [Title [4](#anchor)](#_TOC...)
    Form 2 — bullet list under ## Table of Contents
    Form 3 — heading-level link lines:  # [Title [ii](#p)](#anchor)
    """
    lines = text.splitlines()

    # ── Form 1: plain bare link lines ──
    bare_link_re = re.compile(r"^\[.+\]\(#[^)]+\)\s*$")
    blockquote_toc_re = re.compile(r"^>\s*table of contents\s*$", re.IGNORECASE)

    i = 0
    while i < len(lines):
        if blockquote_toc_re.match(lines[i].strip()):
            lines.pop(i)
            continue
        if bare_link_re.match(lines[i]):
            j = i
            while j < len(lines) and (bare_link_re.match(lines[j]) or not lines[j].strip()):
                j += 1
            n_links = sum(1 for ln in lines[i:j] if bare_link_re.match(ln))
            if n_links >= 3:
                while j < len(lines) and not lines[j].strip():
                    j += 1
                lines = lines[:i] + lines[j:]
                continue
        i += 1

    # ── Form 3: heading-level TOC entries  # [Title [page](#p)](#anchor) ──
    toc_heading_re = re.compile(r"^(#{1,6})\s+\[.+\]\(#[^)]+\)\s*$")
    toc_title_re = re.compile(r"^#{1,6}\s+table\s+of\s+contents\s*$", re.IGNORECASE)

    i = 0
    while i < len(lines):
        if toc_title_re.match(lines[i]):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and toc_heading_re.match(lines[j]):
                while j < len(lines) and (toc_heading_re.match(lines[j]) or not lines[j].strip()):
                    j += 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                lines = lines[:i] + lines[j:]
                continue
        elif toc_heading_re.match(lines[i]):
            lines.pop(i)
            continue
        i += 1

    # ── Form 2: "## Table of Contents" bullet list section ──
    out: list[str] = []
    i = 0
    while i < len(lines):
        if re.match(r"^#{1,3}\s+Table of Contents\s*$", lines[i], re.IGNORECASE):
            heading_level = len(re.match(r"^(#+)", lines[i]).group(1))  # type: ignore[union-attr]
            i += 1
            while i < len(lines) and not re.match(r"^#{1," + str(heading_level) + r"} ", lines[i]):
                i += 1
            while out and not out[-1].strip():
                out.pop()
        else:
            out.append(lines[i])
            i += 1

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Figure caption linking
# ---------------------------------------------------------------------------

_CAPTION_PATTERN = re.compile(
    r"(!\[[^\]]*\]\([^)]+\))\n\n"
    r"((?:Figure|Fig\.?|Exhibit|Chart|Diagram|Illustration|Plate|Table)\s+"
    r"[\d\w.\-]+\.?\s+[^\n]+)",
    re.IGNORECASE,
)


def link_figure_captions(text: str) -> str:
    """
    Promote figure captions that immediately follow an image into the alt text,
    and render them as italics below the image.
    """

    def _replace(m: re.Match[str]) -> str:
        img_tag = m.group(1)
        caption = m.group(2).strip()
        new_img = re.sub(r"!\[[^\]]*\]", f"![{caption}]", img_tag, count=1)
        return f"{new_img}\n\n*{caption}*"

    return _CAPTION_PATTERN.sub(_replace, text)


# ---------------------------------------------------------------------------
# Whitespace normalization
# ---------------------------------------------------------------------------


def normalize_whitespace(text: str) -> str:
    """Collapse 3+ blank lines to 2, ensure single trailing newline."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# Back-to-TOC links
# ---------------------------------------------------------------------------

BACK_LINK = "[↑ Table of Contents](#table-of-contents)"
BACK_MARKER = "<!-- back-to-toc -->"


def strip_back_links(text: str) -> str:
    """Remove previously inserted back-to-TOC lines (idempotent)."""
    lines = [ln for ln in text.splitlines() if not ln.startswith(BACK_MARKER)]
    return "\n".join(lines)


def insert_back_links(text: str) -> str:
    """
    Insert a back-to-TOC link after every H1, H2, and H3 heading in the body,
    except the generated '## Table of Contents' heading itself.
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = re.match(r"^(#{1,3}) (.+)", line)
        if m:
            heading_text = m.group(2).strip()
            if heading_text and not re.match(
                r"^Table of Contents\s*$", heading_text, re.IGNORECASE
            ):
                i += 1
                while i < len(lines) and not lines[i].strip():
                    out.append(lines[i])
                    i += 1
                out.append(BACK_MARKER + BACK_LINK)
                out.append("")
                continue
        i += 1
    return "\n".join(out)


# ---------------------------------------------------------------------------
# GFM anchor generation and TOC building
# ---------------------------------------------------------------------------


def gfm_anchor(text: str, seen: dict[str, int]) -> str:
    """Generate a GitHub Flavored Markdown anchor with deduplication."""
    text = html.unescape(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # strip links
    text = re.sub(r"[`*_~]", "", text)  # strip emphasis
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # remove punctuation
    text = re.sub(r"\s+", "-", text)  # spaces → hyphens
    text = re.sub(r"-+", "-", text).strip("-")
    if not text:
        return ""
    base = text
    count = seen.get(base, 0)
    seen[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


def build_toc(lines: list[str], max_depth: int = 3) -> str:
    """Build a linkable GFM TOC from heading lines."""
    entries = []
    seen: dict[str, int] = {}
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if not m:
            continue
        level = len(m.group(1))
        if level > max_depth:
            continue
        raw = m.group(2).strip()
        if not raw:
            continue
        anchor = gfm_anchor(raw, seen)
        if not anchor:
            continue
        display = re.sub(r"[`*_~]", "", html.unescape(raw)).strip()
        display = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", display)
        indent = "  " * (level - 1)
        entries.append(f"{indent}- [{display}](#{anchor})")
    if not entries:
        return ""
    return "## Table of Contents\n\n" + "\n".join(entries)


def insert_toc(text: str) -> str:
    """
    Insert a generated linkable TOC after the H1 title (or after frontmatter if
    there is no H1). Skips YAML frontmatter when searching for H1.
    """
    lines = text.splitlines()
    toc_str = build_toc(lines)
    if not toc_str:
        return text

    # Find end of YAML frontmatter
    fm_end = 0
    if lines and lines[0].strip() == "---":
        fm_end = 1
        while fm_end < len(lines) and lines[fm_end].strip() != "---":
            fm_end += 1
        fm_end += 1  # past closing ---

    # Find first H1 after frontmatter
    h1_idx: int | None = None
    for idx in range(fm_end, len(lines)):
        if re.match(r"^# ", lines[idx]):
            h1_idx = idx
            break

    if h1_idx is not None:
        insert_at = h1_idx + 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        before = "\n".join(lines[:insert_at])
        after = "\n".join(lines[insert_at:])
        return before + "\n\n" + toc_str + "\n\n" + after
    else:
        before = "\n".join(lines[:fm_end])
        after = "\n".join(lines[fm_end:]).lstrip("\n")
        sep = "\n\n" if before else ""
        return before + sep + toc_str + "\n\n" + after


# ---------------------------------------------------------------------------
# List compaction
# ---------------------------------------------------------------------------

_LIST_ITEM_RE = re.compile(
    r"^\s*(?:"
    r"[-*+]"  # bullet: - * +
    r"|\d+[.)]"  # numbered: 1. 2)
    r"|[A-Za-z][.)](?!\S)"  # lettered: a. B) — not abbreviations
    r"|(?:i{1,3}|iv|vi{0,3}|viii|ix|x{1,3}|xl|l)[.)]"  # roman: i. iv. viii.
    r")\s"
)


def _is_list_item(line: str) -> bool:
    return bool(_LIST_ITEM_RE.match(line))


def _is_list_continuation(line: str) -> bool:
    return bool(re.match(r"^\s{2,}\S", line))


def compact_lists(text: str) -> str:
    """
    Remove blank lines between list items so all lists are tight (single-spaced).
    Applies to bulleted, numbered, lettered, and roman numeral lists at any depth.
    Blank lines inside fenced code blocks are never touched.
    """
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence

        if not in_fence and not stripped:
            prev = next((ln for ln in reversed(out) if ln.strip()), None)
            nxt = next((lines[j] for j in range(i + 1, len(lines)) if lines[j].strip()), None)
            if prev is not None and nxt is not None:
                prev_is_list = _is_list_item(prev) or _is_list_continuation(prev)
                next_is_list = _is_list_item(nxt)
                if prev_is_list and next_is_list:
                    continue  # suppress blank line between list items

        out.append(line)

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Reference section compaction
# ---------------------------------------------------------------------------

COMPACT_SECTION_RE = re.compile(
    r"^(#{1,6})\s+("
    r"index|table of contents|contents|glossary|"
    r"list of (?:tables|figures|illustrations|abbreviations|exhibits|plates)|"
    r"abbreviations|acronyms|bibliography|references|"
    r"list of (?:effective pages?|changes?)"
    r")\s*$",
    re.IGNORECASE,
)


def compact_reference_sections(text: str) -> str:
    """
    Within reference sections (Index, Glossary, List of Tables, etc.),
    remove blank lines between content lines so entries are single-spaced.
    Back-to-TOC markers, headings, and code fences retain surrounding blank lines.
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = COMPACT_SECTION_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        heading_level = len(m.group(1))
        out.append(line)
        i += 1

        section: list[str] = []
        while i < len(lines):
            if re.match(r"^#{1," + str(heading_level) + r"} ", lines[i]):
                break
            section.append(lines[i])
            i += 1

        compacted: list[str] = []
        in_fence = False
        prev_is_content = False

        for sl in section:
            if sl.startswith("```"):
                in_fence = not in_fence

            if in_fence:
                compacted.append(sl)
                prev_is_content = False
                continue

            is_blank = not sl.strip()
            is_back_link = sl.startswith(BACK_MARKER)
            is_heading = bool(re.match(r"^#+\s", sl))
            is_special = is_back_link or is_heading

            if is_blank:
                if not prev_is_content:
                    compacted.append(sl)
                continue

            if is_special:
                if prev_is_content and compacted and compacted[-1].strip():
                    compacted.append("")
                compacted.append(sl)
                prev_is_content = False
            else:
                compacted.append(sl)
                prev_is_content = True

        while compacted and not compacted[-1].strip():
            compacted.pop()
        compacted.append("")

        out.extend(compacted)

    return "\n".join(out)
