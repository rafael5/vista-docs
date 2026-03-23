"""
Pure corpus element classifiers.

All functions take plain Python values and return classification enums/strings.
No docx imports at module level — docx objects are duck-typed via protocols.
"""

from __future__ import annotations

from enum import Enum

SCREEN_STYLES = {
    "Screen Capture",
    "screen display",
    "capture",
    "screen",
    "Screen",
    "Screen capture Char",
}
CODE_STYLES = {"Code"}
LIST_STYLES = {"List Paragraph"}
BODY_STYLES = {"Body Text", "Normal"}


class StyleClass(str, Enum):
    SCREEN = "screen"
    CODE = "code"
    LIST = "list"
    BODY = "body"
    HEADING = "heading"
    OTHER = "other"


TABLE_PATTERNS: dict[str, list[str]] = {
    "revision": ["patch", "date", "description", "project manager"],
    "rpc": ["rpc name", "remote procedure", "return type"],
    "api-function": ["routine", "callable", "api", "dbia"],
    "hl7-segment": ["segment", "seq", "len", "dt", "opt", "rp/"],
    "menu-option": ["option name", "menu text", "lock", "type"],
    "fileman-file-registry": ["file name", "file number", "global"],
    "security-key": ["security key", "key name", "description"],
    "acronym-glossary": ["acronym", "abbreviation", "term", "definition"],
}

CALLOUT_PREFIXES = ["NOTE", "WARNING", "REMINDER", "IMPORTANT", "CAUTION"]


def classify_style(style_name: str) -> StyleClass:
    """Map a paragraph style name to a StyleClass."""
    if style_name in SCREEN_STYLES:
        return StyleClass.SCREEN
    if style_name in CODE_STYLES:
        return StyleClass.CODE
    if style_name in LIST_STYLES:
        return StyleClass.LIST
    if style_name in BODY_STYLES:
        return StyleClass.BODY
    if style_name.startswith("Heading"):
        return StyleClass.HEADING
    return StyleClass.OTHER


def classify_table(header_texts: list[str]) -> str:
    """
    Classify a table by its header row texts.
    Returns a table type key or 'reference-table' as default.
    """
    joined = " ".join(h.lower() for h in header_texts)
    for table_type, keywords in TABLE_PATTERNS.items():
        if all(kw in joined for kw in keywords[:2]):
            return table_type
    return "reference-table"


def detect_callout(text: str) -> str | None:
    """Return callout prefix if paragraph starts with a callout keyword, else None."""
    upper = text.upper().strip()
    for prefix in CALLOUT_PREFIXES:
        if upper.startswith(prefix):
            return prefix
    return None
