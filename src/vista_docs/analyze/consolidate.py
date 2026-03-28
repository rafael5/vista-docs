"""
Document consolidation: master selection, grouping, and addenda assembly.

group_documents(docs)      → list[ConsolidationGroup]
consolidate_group(group)   → ConsolidationResult

A ConsolidationResult contains:
  - master_text: the full text of the selected master document
  - addenda: sections from prior versions whose normalized headings
             are NOT present in the master

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  MASTER SELECTION PRIORITY (in order):
      1. doc_layer == "anchor"  — explicitly classified as the base document
      2. Highest word_count     — most content → most complete
      3. Latest pub_date        — most recent → most current
      4. First in stable sort   — deterministic tiebreaker
    Rationale: "anchor" is the strongest editorial signal. Word count is the
    best proxy for completeness when layer is unavailable. Date breaks ties.
    "patch" documents are penalized: they rank below "plain" because patch
    docs are intentionally partial (they only describe changes, not the whole
    system).

B.  GROUPING KEY: (app_code, doc_type, normalize_title(title)).
    Documents are grouped by normalized title within the same package and doc
    type. normalize_title() strips version numbers, patch IDs, and trailing
    parentheticals so that "VSE GUI 1.7.1 Technical Manual" and "VSE GUI
    1.7.64 Technical Manual" map to the same group key. Documents with
    fundamentally different subjects (even within the same package) form
    separate groups. Single-member groups are valid — they produce a result
    with no addenda.

C.  ADDENDA CONTAIN SECTIONS UNIQUE TO PRIOR VERSIONS.
    For each non-master document, a heading-level diff is run against the
    master. Sections whose normalized heading appears in the diff's "removed"
    set (i.e., in the prior doc but not the master) are extracted as unique
    sections. Sections already present in the master are NOT copied —
    the master version is authoritative.

D.  SECTION CONTENT EXTRACTION IS HEADING-BOUNDED.
    A "section" is the content from a heading line until the next heading at
    the same or higher level. Subsections (deeper headings) are included.
    Content is extracted verbatim from the source document; no reformatting.

E.  PUB_DATE PARSING: "Month YYYY" format.
    Dates are expected as "Month YYYY" (e.g. "March 2022"). Unknown formats
    parse to (0, 0) and sort to the beginning, so well-formed dates always
    rank above missing/malformed ones.

F.  WORD_COUNT ZERO TREATED AS UNKNOWN.
    A word_count of 0 means the field was not successfully extracted during
    enrichment. Zero-count documents rank below any document with a positive
    word count. They do NOT rank below documents with a negative word count
    (there are none).

G.  ADDENDA DE-DUPLICATION ACROSS PRIOR VERSIONS.
    If multiple prior versions contain the same unique section (same normalized
    heading), only the instance from the most recent prior version is kept.
    "Most recent" is determined by the same master-selection ordering.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field

from vista_docs.analyze.diff import diff_headings
from vista_docs.analyze.headings import (
    _FRONTMATTER_RE,  # reuse internal compiled regex
    _HEADING_RE,
    normalize_heading,
)

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class DocumentRecord:
    """Lightweight record describing one document for consolidation purposes."""

    path: str
    """Filesystem path to the markdown file (may be empty for tests)."""

    title: str
    """Document title from frontmatter."""

    doc_type: str
    """Canonical doc type (e.g. 'technical-manual')."""

    app_code: str
    """Package namespace (e.g. 'PSO')."""

    word_count: int
    """Word count from enrichment. 0 means unknown (Axiom F)."""

    pub_date: str
    """Raw publication date string, typically 'Month YYYY' (Axiom E)."""

    doc_layer: str
    """'anchor' | 'patch' | 'plain' | '' (Axiom A)."""

    patch_id: str = ""
    """Frontmatter patch_id value, e.g. 'PSO*7.0*507'. Empty if absent."""

    is_stub: bool = False
    """True if the document was flagged as a stub during enrichment."""

    text: str = ""
    """Full markdown text. Populated lazily by the runner before use."""


@dataclass
class UniqueSection:
    """A section from a prior document not present in the master."""

    normalized: str
    """Normalized heading text (the section identity key)."""

    raw_heading: str
    """First raw variant of the heading as it appears in the source."""

    level: int
    """Heading level (2 = H2, 3 = H3)."""

    content: str
    """Full markdown content from heading line to end of section (Axiom D)."""

    source_title: str
    """Title of the document this section came from."""


@dataclass
class ConsolidationGroup:
    """A set of documents that represent versions of the same artifact."""

    app_code: str
    doc_type: str
    group_title: str
    """Normalized title used as the grouping key (Axiom B)."""

    members: list[DocumentRecord] = field(default_factory=list)
    """All documents in this group (any size ≥ 1)."""


@dataclass
class ConsolidationResult:
    """Output of consolidating one ConsolidationGroup."""

    group: ConsolidationGroup
    master: DocumentRecord
    """The selected master document (Axiom A)."""

    master_text: str
    """Full text of the master document."""

    addenda: list[UniqueSection]
    """Unique sections from prior versions, de-duplicated (Axiom C, G)."""


# ---------------------------------------------------------------------------
# Title normalization (Axiom B)
# ---------------------------------------------------------------------------

# Bare version numbers like "1.7.1", "5.3", "7" that appear standalone
# (not already caught by headings.py's _VERSION_RE which requires "version" keyword or "v" prefix)
_BARE_VER_RE = re.compile(r"\b\d+(?:\.\d+)+\b")


def normalize_title(title: str) -> str:
    """
    Normalize a document title for grouping purposes.

    Applies the heading normalization pipeline (strips patch IDs, version
    keywords, trailing parentheticals, ALL-CAPS prefixes) then additionally
    strips bare version numbers like "1.7.1" or "5.3" that may not have
    an explicit "version" keyword prefix.

    Args:
        title: Raw document title string.

    Returns:
        Normalized lowercase title suitable as a grouping key.
    """
    s = normalize_heading(title)
    s = _BARE_VER_RE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------------------
# Master selection (Axiom A)
# ---------------------------------------------------------------------------

_LAYER_RANK = {"anchor": 0, "plain": 1, "patch": 2, "": 3}

_MONTH_MAP = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def _parse_pub_date(raw: str) -> tuple[int, int]:
    """Parse 'Month YYYY' or 'YYYY' to (year, month) for comparison. Unknown → (0, 0)."""
    s = raw.strip().lower()
    m = re.match(r"(\w+)\s+(\d{4})", s)
    if m:
        return (int(m.group(2)), _MONTH_MAP.get(m.group(1), 0))
    m = re.match(r"(\d{4})", s)
    if m:
        return (int(m.group(1)), 0)
    return (0, 0)


def select_master(docs: list[DocumentRecord]) -> DocumentRecord:
    """
    Select the master document from a group (Axiom A).

    Priority: anchor layer > highest word_count > latest pub_date > stable index.

    Args:
        docs: Non-empty list of DocumentRecord objects.

    Returns:
        The selected master DocumentRecord.
    """

    def _key(doc: DocumentRecord) -> tuple[int, int, tuple[int, int]]:
        layer = _LAYER_RANK.get(doc.doc_layer, 3)
        wc = doc.word_count if doc.word_count > 0 else 0
        date = _parse_pub_date(doc.pub_date)
        # Sort: layer asc (anchor=0 first), then wc desc, then date desc
        return (layer, -wc, (-date[0], -date[1]))

    return min(docs, key=_key)


# ---------------------------------------------------------------------------
# Document grouping (Axiom B)
# ---------------------------------------------------------------------------


def group_documents(docs: list[DocumentRecord]) -> list[ConsolidationGroup]:
    """
    Group documents by (app_code, doc_type, normalize_title(title)).

    Args:
        docs: List of DocumentRecord objects (any mix of packages/types).

    Returns:
        List of ConsolidationGroup, one per distinct group key.
        Preserves stable ordering: groups sorted by (app_code, doc_type, group_title).
    """
    buckets: dict[tuple[str, str, str], list[DocumentRecord]] = defaultdict(list)
    for doc in docs:
        key = (doc.app_code, doc.doc_type, normalize_title(doc.title))
        buckets[key].append(doc)

    groups = []
    for (app_code, doc_type, group_title), members in sorted(buckets.items()):
        groups.append(
            ConsolidationGroup(
                app_code=app_code,
                doc_type=doc_type,
                group_title=group_title,
                members=members,
            )
        )
    return groups


# ---------------------------------------------------------------------------
# Section content extraction (Axiom D)
# ---------------------------------------------------------------------------


def extract_unique_sections(
    text: str,
    heading_norms: set[str],
    min_level: int = 2,
    max_level: int = 3,
) -> list[UniqueSection]:
    """
    Extract markdown sections whose normalized heading is in heading_norms.

    Each section spans from its heading line to (but not including) the next
    heading at the same or higher level. Subsections are included (Axiom D).

    Args:
        text:          Full markdown document text.
        heading_norms: Set of normalized heading strings to extract.
        min_level:     Minimum heading level to consider (default 2).
        max_level:     Maximum heading level to consider (default 3).

    Returns:
        List of UniqueSection objects, in document order.
    """
    if not heading_norms:
        return []

    body = _FRONTMATTER_RE.sub("", text, count=1)
    lines = body.split("\n")

    sections: list[UniqueSection] = []
    in_section = False
    section_level = 0
    section_norm = ""
    section_raw = ""
    section_lines: list[str] = []

    def _flush() -> None:
        if in_section and section_lines:
            sections.append(
                UniqueSection(
                    normalized=section_norm,
                    raw_heading=section_raw,
                    level=section_level,
                    content="\n".join(section_lines).rstrip(),
                    source_title="",  # filled in by caller
                )
            )

    for line in lines:
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            raw = m.group(2).strip()
            norm = normalize_heading(raw)

            if in_section and level <= section_level:
                # End of current section — hit a sibling or ancestor heading
                _flush()
                in_section = False
                section_lines = []

            if not in_section and norm in heading_norms and min_level <= level <= max_level:
                in_section = True
                section_level = level
                section_norm = norm
                section_raw = raw

        if in_section:
            section_lines.append(line)

    _flush()  # handle section that runs to end of file
    return sections


# ---------------------------------------------------------------------------
# Consolidation (Axioms C, G)
# ---------------------------------------------------------------------------


def consolidate_group(group: ConsolidationGroup) -> ConsolidationResult:
    """
    Consolidate a group of documents into a master + addenda.

    Selects the master document, then for each non-master document diffs
    its headings against the master and extracts sections whose headings
    are not present in the master.

    Args:
        group: ConsolidationGroup with at least one member. Member texts
               must be populated (DocumentRecord.text != '').

    Returns:
        ConsolidationResult with master, master_text, and addenda list.
    """
    master = select_master(group.members)
    prior_docs = [d for d in group.members if d is not master]

    if not prior_docs:
        return ConsolidationResult(
            group=group,
            master=master,
            master_text=master.text,
            addenda=[],
        )

    # Collect addenda per unique normalized heading.
    # For de-duplication (Axiom G): keep only the section from the most
    # recent prior version, determined by select_master ordering.
    # We process prior_docs in master-selection order so that the first
    # instance we encounter for each normalized heading wins.
    prior_sorted = sorted(prior_docs, key=lambda d: _key_for_sort(d))
    seen_norms: set[str] = set()
    addenda: list[UniqueSection] = []

    for doc in prior_sorted:
        diff = diff_headings(master.text, doc.text)
        # "removed" from master's POV = headings in doc but not master
        # Wait: diff_headings(a, b).added = in b not a.
        # diff_headings(master, doc).added = in doc, not master = unique to doc ✓
        unique_norms = set(diff.added) - seen_norms
        if not unique_norms:
            continue
        sections = extract_unique_sections(doc.text, unique_norms)
        for s in sections:
            s.source_title = doc.title
            seen_norms.add(s.normalized)
        addenda.extend(sections)

    return ConsolidationResult(
        group=group,
        master=master,
        master_text=master.text,
        addenda=addenda,
    )


def _key_for_sort(doc: DocumentRecord) -> tuple[int, int, tuple[int, int]]:
    """Sort key matching select_master priority (anchor first, then wc desc, date desc)."""
    layer = _LAYER_RANK.get(doc.doc_layer, 3)
    wc = doc.word_count if doc.word_count > 0 else 0
    date = _parse_pub_date(doc.pub_date)
    return (layer, -wc, (-date[0], -date[1]))
