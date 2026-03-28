"""
Normalized heading diff between two markdown documents.

diff_headings(text_a, text_b) → HeadingDiff

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  COMPARISON IS ON NORMALIZED HEADINGS, NOT RAW STRINGS.
    Both documents have their headings extracted (H2/H3 by default) and each
    heading is normalized via normalize_heading() before comparison. This means
    two headings that differ only in patch number, version string, or trailing
    annotation are treated as identical. A section "PSO*7*801 Release Notes"
    in version A and "PSO*7*900 Release Notes" in version B are the SAME
    heading ("release notes") — they are not different, and do not appear as
    added or removed.

B.  EACH HEADING APPEARS AT MOST ONCE PER DOCUMENT (set semantics).
    If a heading appears twice in document A, it is treated as present once.
    Frequency is not tracked here — only presence/absence. This matches the
    doc-frequency counting convention in headings.py (Axiom 5).

C.  LEVEL-INDEPENDENT COMPARISON.
    "Overview" at H2 and "Overview" at H3 are the same heading. Level
    information is not used to distinguish headings in the diff. If a heading
    moves from H2 to H3 between versions it is counted as COMMON, not as
    added+removed. Rationale: structural depth often shifts between doc
    versions without the section's identity or content changing.

D.  RESULT SETS ARE DISJOINT.
    A normalized heading appears in exactly one of: added, removed, common.
    Never in two sets simultaneously.

E.  RAW VARIANTS ARE PRESERVED FOR HUMAN REVIEW.
    For each heading in added, removed, and common, the distinct raw strings
    that produced that normalized form are stored in the corresponding _raw
    dict. These allow a reviewer to verify that normalization correctly grouped
    semantically related headings.

F.  DIRECTION: diff_headings(a, b) describes changes TO REACH b FROM a.
    added   = in b, not in a  (new in b)
    removed = in a, not in b  (lost from a)
    common  = in both
    This is consistent with standard diff semantics.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from vista_docs.analyze.headings import extract_headings, normalize_heading


@dataclass
class HeadingDiff:
    """
    Result of comparing two documents' normalized heading sets.

    All lists contain normalized heading strings.
    The _raw dicts map normalized → list of distinct raw strings seen
    in the relevant document(s).
    """

    added: list[str]
    """Normalized headings present in doc_b but not doc_a (Axiom F)."""

    removed: list[str]
    """Normalized headings present in doc_a but not doc_b (Axiom F)."""

    common: list[str]
    """Normalized headings present in both doc_a and doc_b."""

    added_raw: dict[str, list[str]] = field(default_factory=dict)
    """Raw variants for each added heading, from doc_b (Axiom E)."""

    removed_raw: dict[str, list[str]] = field(default_factory=dict)
    """Raw variants for each removed heading, from doc_a (Axiom E)."""

    common_raw: dict[str, list[str]] = field(default_factory=dict)
    """Raw variants for each common heading, from both docs (Axiom E)."""


def diff_headings(
    text_a: str,
    text_b: str,
    min_level: int = 2,
    max_level: int = 3,
) -> HeadingDiff:
    """
    Compute the normalized heading diff between two markdown documents.

    Extracts H2/H3 headings from each document, normalizes them, then
    computes added/removed/common sets. See module axioms for semantics.

    Args:
        text_a:    Full markdown text of the "before" document.
        text_b:    Full markdown text of the "after" document.
        min_level: Minimum heading level to compare (default 2).
        max_level: Maximum heading level to compare (default 3).

    Returns:
        HeadingDiff with sorted added/removed/common lists and raw variant dicts.
    """
    norms_a, raw_a = _heading_set(text_a, min_level, max_level)
    norms_b, raw_b = _heading_set(text_b, min_level, max_level)

    added_set = norms_b - norms_a
    removed_set = norms_a - norms_b
    common_set = norms_a & norms_b

    # Merge raw variants for common from both docs (Axiom E)
    common_raw: dict[str, list[str]] = {}
    for norm in common_set:
        seen: list[str] = []
        for rv in raw_a.get(norm, []) + raw_b.get(norm, []):
            if rv not in seen:
                seen.append(rv)
        common_raw[norm] = seen

    return HeadingDiff(
        added=sorted(added_set),
        removed=sorted(removed_set),
        common=sorted(common_set),
        added_raw={n: raw_b[n] for n in added_set},
        removed_raw={n: raw_a[n] for n in removed_set},
        common_raw=common_raw,
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _heading_set(
    text: str,
    min_level: int,
    max_level: int,
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Extract the set of normalized headings from a markdown text.

    Returns:
        (norm_set, raw_dict) where raw_dict maps normalized → [raw, ...].
        Headings that normalize to empty string are silently dropped.
    """
    norm_set: set[str] = set()
    raw_dict: dict[str, list[str]] = {}

    for _level, raw in extract_headings(text, min_level, max_level):
        norm = normalize_heading(raw)
        if not norm:
            continue
        norm_set.add(norm)
        if norm not in raw_dict:
            raw_dict[norm] = []
        if raw not in raw_dict[norm]:
            raw_dict[norm].append(raw)

    return norm_set, raw_dict
