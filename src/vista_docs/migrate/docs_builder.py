"""
Docs directory entry builder: classify which records go into docs/ and where.

build_docs_entries(records) → list[DocsEntry]
consolidated_group_title(consolidated_master_path) → str

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  ONLY PUBLISHABLE RECORDS ENTER docs/.
    - consolidated-master  → YES (source: consolidated output file)
    - standalone           → YES (source: originals/ verbatim copy)
    - release-note         → YES (source: originals/ — also feeds CHANGELOG)
    - change-page          → YES (source: originals/ — CP diff applied later)
    - consolidated-addendum → NO (content already embedded in master)
    - stub                 → NO (incomplete document; not published)

B.  DESTINATION PATHS:
    - consolidated-master:  docs/{doc_type}/{safe_group_title}.md
    - standalone:           docs/{doc_type}/{original_filename}
    - release-note:         docs/release-note/{original_filename}
    - change-page:          docs/change-page/{original_filename}

C.  SOURCE CLASSIFICATION:
    - "consolidated": the docs_runner must find the pre-built consolidated file
      using (app_code, consolidated_title) as the lookup key.
    - "original": the docs_runner copies from originals/{doc_type}/{filename}
      within the same repo.

D.  GROUP TITLE EXTRACTION:
    The consolidated_master field on a ManifestRecord stores the intended
    docs/ path: "docs/{doc_type}/{group_title}.md". The group_title is the
    third path component without the .md extension.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from vista_docs.analyze.corpus_manifest import ManifestRecord

_TRANSFORMATIONS_IN_DOCS = {"consolidated-master", "standalone", "release-note", "change-page"}

_SAFE_RE = re.compile(r"[^a-z0-9_\-]")


def _safe_name(s: str) -> str:
    return _SAFE_RE.sub("_", s.lower()).strip("_")[:80]


# ---------------------------------------------------------------------------
# Data structure
# ---------------------------------------------------------------------------


@dataclass
class DocsEntry:
    """One document that should be written into docs/ for a package repo."""

    app_code: str
    doc_type: str
    transformation: str

    original_path: str
    """Relative path within the repo: 'originals/{doc_type}/{filename}'."""

    docs_path: str
    """Destination relative path within the repo: 'docs/{doc_type}/{filename}'."""

    source: str
    """'consolidated' | 'original' — where the runner reads the source file."""

    consolidated_title: str
    """
    For source='consolidated': the group_title to look up in the consolidated
    output directory. Empty for source='original'.
    """


# ---------------------------------------------------------------------------
# Group title extraction (Axiom D)
# ---------------------------------------------------------------------------


def consolidated_group_title(consolidated_master_path: str) -> str:
    """
    Extract the group_title from a consolidated_master path.

    'docs/technical-manual/pso technical manual.md' → 'pso technical manual'
    ''                                               → ''
    """
    if not consolidated_master_path:
        return ""
    stem = consolidated_master_path.rsplit("/", 1)[-1]
    return stem[:-3] if stem.endswith(".md") else stem


# ---------------------------------------------------------------------------
# Entry builder (Axioms A–C)
# ---------------------------------------------------------------------------


def build_docs_entries(records: list[ManifestRecord]) -> list[DocsEntry]:
    """
    Classify all publishable records and compute their docs/ destinations.

    Args:
        records: All ManifestRecords for a single package.

    Returns:
        List of DocsEntry for records that belong in docs/ (Axiom A).
        Stubs and addenda are excluded.
    """
    entries: list[DocsEntry] = []

    for rec in records:
        if rec.transformation not in _TRANSFORMATIONS_IN_DOCS:
            continue

        original_filename = rec.original_path.split("/")[-1]

        if rec.transformation == "consolidated-master":
            group_title = consolidated_group_title(rec.consolidated_master)
            safe_title = _safe_name(group_title) + ".md"
            docs_path = f"docs/{rec.doc_type}/{safe_title}"
            entries.append(
                DocsEntry(
                    app_code=rec.package,
                    doc_type=rec.doc_type,
                    transformation=rec.transformation,
                    original_path=rec.original_path,
                    docs_path=docs_path,
                    source="consolidated",
                    consolidated_title=group_title,
                )
            )

        else:
            # standalone, release-note, change-page — copy from originals/
            docs_path = f"docs/{rec.doc_type}/{original_filename}"
            entries.append(
                DocsEntry(
                    app_code=rec.package,
                    doc_type=rec.doc_type,
                    transformation=rec.transformation,
                    original_path=rec.original_path,
                    docs_path=docs_path,
                    source="original",
                    consolidated_title="",
                )
            )

    return entries
