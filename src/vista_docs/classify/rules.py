"""
Pure document type classification.

classify(filename, title) → DocType

Filename patterns take priority over title patterns.
All matching is case-insensitive.
"""

from __future__ import annotations

import re

from vista_docs.models.manifest import DocType

# ---------------------------------------------------------------------------
# Filename pattern rules (checked first, in priority order)
# ---------------------------------------------------------------------------

_FILENAME_RULES: list[tuple[re.Pattern[str], DocType]] = [
    # Technical manual: ends with "tm" before extension, or explicit keyword
    (re.compile(r"(tm\.|technical.?manual)", re.I), DocType.TECHNICAL_MANUAL),
    # User manual: ends with "um" before extension
    (re.compile(r"(um\.|user.?manual)", re.I), DocType.USER_MANUAL),
    # Installation / DIBR (Deployment Installation Back-out Rollback) guide
    (re.compile(r"(ig\.|install|dibr)", re.I), DocType.INSTALLATION_GUIDE),
    # Release notes: contains "rn" suffix or "release"
    (re.compile(r"(rn\.|release.?note|patch.*rn)", re.I), DocType.RELEASE_NOTE),
    # Quick reference: "qr" suffix or "quick"
    (re.compile(r"(qr\.|quick.?ref)", re.I), DocType.QUICK_REF),
    # Change page: "cp" suffix
    (re.compile(r"cp\.", re.I), DocType.CHANGE_PAGE),
    # Supplement: "sp" suffix
    (re.compile(r"sp\.", re.I), DocType.SUPPLEMENT),
]

# ---------------------------------------------------------------------------
# Title pattern rules (fallback when filename doesn't match)
# ---------------------------------------------------------------------------

_TITLE_RULES: list[tuple[re.Pattern[str], DocType]] = [
    (re.compile(r"technical.?manual", re.I), DocType.TECHNICAL_MANUAL),
    (re.compile(r"user.?manual", re.I), DocType.USER_MANUAL),
    (
        re.compile(r"installation.?guide|deployment.*installation|dibr", re.I),
        DocType.INSTALLATION_GUIDE,
    ),
    (re.compile(r"release.?note", re.I), DocType.RELEASE_NOTE),
    (re.compile(r"quick.?ref", re.I), DocType.QUICK_REF),
    (re.compile(r"change.?page", re.I), DocType.CHANGE_PAGE),
    (re.compile(r"supplement", re.I), DocType.SUPPLEMENT),
    (re.compile(r"security", re.I), DocType.BASE_SECURITY),
    (re.compile(r"hl7|interface.?spec", re.I), DocType.BASE_HL7),
    (re.compile(r"setup|configuration", re.I), DocType.BASE_SETUP),
    (re.compile(r"developer|programming", re.I), DocType.BASE_DEV),
    (re.compile(r"implementation", re.I), DocType.BASE_IMPL),
]


def classify(filename: str, title: str) -> DocType:
    """
    Classify a document as a DocType based on its filename and title.

    Filename patterns are checked first. Falls back to title patterns.
    Returns DocType.UNKNOWN if nothing matches.
    """
    stem = filename.lower()

    for pattern, doc_type in _FILENAME_RULES:
        if pattern.search(stem):
            return doc_type

    title_lower = title.lower()
    for pattern, doc_type in _TITLE_RULES:
        if pattern.search(title_lower):
            return doc_type

    return DocType.UNKNOWN
