"""
Pure markdown post-processing for VA DOCX → markdown output.

All functions take a markdown string and return a cleaned markdown string.
No I/O, no Docling dependency.
"""
from __future__ import annotations

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

_HEADING_RE = re.compile(r"^(#{1,6})\s+(\d+(?:\.\d+)*)\s+(.+)$", re.MULTILINE)
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
