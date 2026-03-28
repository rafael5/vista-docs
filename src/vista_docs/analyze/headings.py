"""
Heading frequency analysis for VA VDL documents.

build_profile(doc_type, docs) → DocTypeProfile

-------------------------------------------------------------------------------
AXIOMS — invariants this module is built on
-------------------------------------------------------------------------------

1.  HEADING LEVELS ANALYZED: H2 (##) and H3 (###) only.
    - H1 (#) is the document title. It is always unique per document (the doc
      title is not a reusable section name), so it contributes no signal about
      structural repetition across documents.
    - H4–H6 are implementation-level subsections. They are too granular and
      package-specific for cross-document pattern detection at the doc-type
      level. Including them would flood the boilerplate list with headings that
      are coincidentally identical but conceptually unrelated.

2.  NORMALIZATION BEFORE COMPARISON.
    Two headings are considered structurally identical after normalization.
    The normalization pipeline (in order):
      a. Lowercase the full heading string.
      b. Strip VA patch identifiers — patterns like OR*3.0*636, PSO*7*123,
         DG*5.3*887. These embed specific patch numbers into heading titles
         (e.g., "PSO*7*801 Release Notes") but the underlying section is the
         same across patches.
      c. Strip standalone version strings — "version 5.0", "v2.1", "release
         4.6". Same rationale: version-tagged headings represent the same
         structural section across versions.
      d. Strip trailing parentheticals — anything in (...) at the end of the
         heading (e.g., "(Updated OR*3.0*636)", "(pso_7_p622)"). These are
         annotations, not section identifiers.
      e. Strip an ALL-CAPS package-name prefix before a colon — e.g.,
         "CPRS: Technical Manual Overview" → "technical manual overview". The
         package name is context, not part of the section identity.
      f. Collapse internal whitespace runs to a single space.
      g. Strip leading/trailing punctuation (colon, dash, period, whitespace).
    ASSUMPTION: Two headings that differ only in patch number, version number,
    or trailing annotation represent the same conceptual section. This may
    produce false positives if two packages coincidentally share a section name
    with different content — but at the doc-type aggregate level this tradeoff
    is acceptable and the expected false-positive rate is low.

3.  BOILERPLATE THRESHOLD (default 70%).
    A normalized heading is BOILERPLATE when it appears in ≥70% of the
    documents in a doc type. Rationale: if a heading is present in 7 of 10
    documents, it is a structural convention of that doc type, not a signal of
    unique information in any individual document.
    This threshold is a parameter — lower it to be more aggressive (e.g., 50%),
    raise it to be more conservative (e.g., 85%).

4.  UNIQUE THRESHOLD (default 15%).
    A normalized heading is UNIQUE when it appears in ≤15% of documents of a
    doc type. These headings are the highest-information candidates: they appear
    only in a minority of documents and are likely to contain content specific
    to that document rather than boilerplate procedure.
    The band between UNIQUE and BOILERPLATE (15%–70%) is labeled COMMON —
    present often enough to be a known pattern, but not ubiquitous.

5.  FREQUENCY DENOMINATOR IS DOCUMENT COUNT, NOT OCCURRENCE COUNT.
    A heading that appears three times in one document still counts as one
    occurrence for that document. Frequency = (docs containing heading) /
    (total docs in doc type). This prevents a single document with many
    repeated headings from inflating the frequency of those headings.

6.  MINIMUM DOCUMENT COUNT (default 5).
    Doc types with fewer than 5 documents are excluded from analysis. With
    fewer than 5 documents, every heading in a single document would show up
    as 20%+ frequency, making BOILERPLATE/UNIQUE categorization meaningless.
    The caller controls this threshold via the runner; the pure module has no
    minimum — it analyzes whatever docs it is given.

7.  STUB EXCLUSION.
    Documents flagged as stubs (is_stub: True in frontmatter, typically <200
    words) are excluded before calling build_profile. Stubs often have
    placeholder or incomplete heading structures (e.g., a single H2 "Contents"
    with no body) that would distort frequency counts for their doc type.
    Stub filtering is the caller's responsibility; this module accepts only
    the non-stub document texts.

8.  HEADING IDENTITY IS LEVEL-INDEPENDENT.
    "Overview" at H2 and "Overview" at H3 in different documents are treated
    as the same normalized heading for frequency counting. The heading text is
    the identity; the level is informational metadata only (preserved in
    level_counts). Rationale: structural variation in heading depth across
    documents of the same type should not prevent matching of semantically
    identical sections. If level matters for a specific use case, filter
    HeadingRecord.level_counts after profiling.

9.  RAW VARIANTS ARE PRESERVED.
    The up-to-MAX_VARIANTS distinct raw heading strings that map to each
    normalized form are stored. This allows a human reviewer to verify that
    the normalization correctly grouped semantically related headings, and to
    investigate cases where normalization may have over-aggressively merged
    unrelated headings.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Axiom 3
BOILERPLATE_THRESHOLD: float = 0.70
# Axiom 4
UNIQUE_THRESHOLD: float = 0.15

# How many raw variant strings to preserve per normalized heading (Axiom 9)
MAX_VARIANTS: int = 10

# Heading categories
BOILERPLATE = "BOILERPLATE"
COMMON = "COMMON"
UNIQUE = "UNIQUE"

# ---------------------------------------------------------------------------
# Normalization helpers (Axiom 2)
# ---------------------------------------------------------------------------

# 2b: VA patch identifiers, e.g. OR*3.0*636 / PSO*7*123 / DG*5.3*887
_PATCH_RE = re.compile(r"[a-z]+\*[\d.]+\*\d+", re.I)

# 2c: standalone version strings
_VERSION_RE = re.compile(
    r"\b(?:version|ver|release|rev)\s*[\d]+(?:[._-][\d]+)*\b"
    r"|\bv\s*\d+(?:[._-]\d+)+\b",  # v2.1 / v2_1 — require at least one dot/sep
    re.I,
)

# 2d: trailing parenthetical — greedy match of last (...) group at end of string
_TRAILING_PAREN_RE = re.compile(r"\s*\([^)]*\)\s*$")

# 2e: ALL-CAPS package-name prefix before colon, e.g. "CPRS: " or "PSO: "
# Only strips when the prefix is ALL_CAPS (pure letters/digits) up to 12 chars
_PKG_PREFIX_RE = re.compile(r"^[A-Z][A-Z0-9]{0,11}:\s+")

# 2g: leading/trailing punctuation after all other normalization
_EDGE_PUNCT_RE = re.compile(r"^[^\w]+|[^\w]+$")


def normalize_heading(raw: str) -> str:
    """
    Normalize a raw heading string for cross-document comparison.

    Applies the normalization pipeline defined in Axiom 2 (a–g).
    Returns an empty string if normalization reduces the heading to nothing
    (e.g., a heading that was entirely a patch ID).

    Args:
        raw: The raw heading text extracted from a markdown document,
             without the leading '#' characters.

    Returns:
        Normalized lowercase heading string, or "" if nothing remains.
    """
    s = raw.strip()
    # 2e: strip ALL-CAPS package prefix before colon (do this before lowercasing
    #     so the ALL-CAPS regex still works)
    s = _PKG_PREFIX_RE.sub("", s)
    # 2a: lowercase
    s = s.lower()
    # 2b: strip patch identifiers
    s = _PATCH_RE.sub("", s)
    # 2c: strip version strings
    s = _VERSION_RE.sub("", s)
    # 2d: strip trailing parenthetical (one pass — handles most cases)
    s = _TRAILING_PAREN_RE.sub("", s)
    # 2f: collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    # 2g: strip leading/trailing non-word characters
    s = _EDGE_PUNCT_RE.sub("", s).strip()
    return s


# ---------------------------------------------------------------------------
# Heading extraction (Axiom 1)
# ---------------------------------------------------------------------------

# Matches markdown ATX headings: one or more # followed by a space and text.
# Capture group 1 = hashes, group 2 = heading text.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)

# Frontmatter block to skip (YAML between first --- and second ---)
_FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def extract_headings(
    md_text: str,
    min_level: int = 2,
    max_level: int = 3,
) -> list[tuple[int, str]]:
    """
    Extract headings from a markdown document within the given level range.

    Skips YAML frontmatter if present (the --- ... --- block at the top of the
    file). Returns a list of (level, raw_text) tuples in document order.

    Args:
        md_text:   Full markdown text of the document.
        min_level: Minimum heading level to include (default 2 = H2).
        max_level: Maximum heading level to include (default 3 = H3).
                   See Axiom 1 for rationale.

    Returns:
        List of (level, heading_text) tuples. level is an integer (2 or 3
        with defaults). heading_text is the raw text without leading '#'.
    """
    # Strip frontmatter so --- lines are not confused with headings
    body = _FRONTMATTER_RE.sub("", md_text, count=1)
    results = []
    for m in _HEADING_RE.finditer(body):
        level = len(m.group(1))
        if min_level <= level <= max_level:
            results.append((level, m.group(2)))
    return results


# ---------------------------------------------------------------------------
# Profile data structures
# ---------------------------------------------------------------------------


@dataclass
class HeadingRecord:
    """Frequency profile for a single normalized heading within a doc type."""

    normalized: str
    """Normalized heading text used as the grouping key."""

    raw_variants: list[str]
    """Up to MAX_VARIANTS distinct raw strings that normalized to this form."""

    level_counts: dict[int, int]
    """Occurrence counts by heading level, e.g. {2: 14, 3: 3}."""

    doc_count: int
    """Number of documents (in this doc type) that contain this heading."""

    doc_frequency: float
    """doc_count / total docs analyzed. Range [0.0, 1.0]."""

    category: str
    """BOILERPLATE | COMMON | UNIQUE (see Axioms 3 and 4)."""


@dataclass
class DocTypeProfile:
    """Heading frequency profile for all documents of one doc type."""

    doc_type: str
    """The DocType value being profiled (e.g. 'release-note')."""

    doc_count: int
    """Number of non-stub documents analyzed."""

    total_heading_occurrences: int
    """Total heading occurrences across all docs (counts repeats in a doc)."""

    unique_normalized_count: int
    """Number of distinct normalized headings found."""

    boilerplate_threshold: float
    """Threshold used for BOILERPLATE classification."""

    unique_threshold: float
    """Threshold used for UNIQUE classification."""

    headings: list[HeadingRecord] = field(default_factory=list)
    """All heading records, sorted by doc_frequency descending."""


# ---------------------------------------------------------------------------
# Profile builder (pure — no I/O)
# ---------------------------------------------------------------------------


def build_profile(
    doc_type: str,
    doc_texts: list[str],
    boilerplate_threshold: float = BOILERPLATE_THRESHOLD,
    unique_threshold: float = UNIQUE_THRESHOLD,
    min_level: int = 2,
    max_level: int = 3,
) -> DocTypeProfile:
    """
    Build a heading frequency profile for a collection of documents.

    All documents passed here are assumed to be of the same doc type and to
    have already had stubs filtered out (Axiom 7).

    Args:
        doc_type:             String label for the doc type being profiled.
        doc_texts:            List of full markdown texts (one per document).
        boilerplate_threshold: Frequency above which a heading is BOILERPLATE.
        unique_threshold:     Frequency at or below which a heading is UNIQUE.
        min_level:            Minimum heading level to extract (Axiom 1).
        max_level:            Maximum heading level to extract (Axiom 1).

    Returns:
        DocTypeProfile with all HeadingRecords sorted by doc_frequency desc.
    """
    total_docs = len(doc_texts)

    # Per normalized heading: set of doc indices that contain it (Axiom 5),
    # all raw variants seen (Axiom 9), and level occurrence counts.
    doc_sets: dict[str, set[int]] = defaultdict(set)
    raw_variants: dict[str, list[str]] = defaultdict(list)
    level_counts: dict[str, Counter] = defaultdict(Counter)
    total_occurrences = 0

    for doc_idx, text in enumerate(doc_texts):
        for level, raw in extract_headings(text, min_level, max_level):
            total_occurrences += 1
            norm = normalize_heading(raw)
            if not norm:
                continue
            # Axiom 5: count doc once regardless of how many times heading appears
            doc_sets[norm].add(doc_idx)
            level_counts[norm][level] += 1
            # Axiom 9: store up to MAX_VARIANTS distinct raw forms
            if raw not in raw_variants[norm] and len(raw_variants[norm]) < MAX_VARIANTS:
                raw_variants[norm].append(raw)

    records: list[HeadingRecord] = []
    for norm, doc_set in doc_sets.items():
        freq = len(doc_set) / total_docs if total_docs > 0 else 0.0
        cat = _categorize(freq, boilerplate_threshold, unique_threshold)
        records.append(
            HeadingRecord(
                normalized=norm,
                raw_variants=raw_variants[norm],
                level_counts=dict(level_counts[norm]),
                doc_count=len(doc_set),
                doc_frequency=round(freq, 4),
                category=cat,
            )
        )

    records.sort(key=lambda r: r.doc_frequency, reverse=True)

    return DocTypeProfile(
        doc_type=doc_type,
        doc_count=total_docs,
        total_heading_occurrences=total_occurrences,
        unique_normalized_count=len(records),
        boilerplate_threshold=boilerplate_threshold,
        unique_threshold=unique_threshold,
        headings=records,
    )


def _categorize(
    frequency: float,
    boilerplate_threshold: float,
    unique_threshold: float,
) -> str:
    """Classify a heading frequency into BOILERPLATE, COMMON, or UNIQUE."""
    if frequency >= boilerplate_threshold:
        return BOILERPLATE
    if frequency <= unique_threshold:
        return UNIQUE
    return COMMON
