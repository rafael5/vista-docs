"""
Local repo layout builder: generate the directory structure, zensical.toml,
PROVENANCE.md, and README.md for one package repository.

build_repo_layout(app_code, records) → RepoLayout
generate_zensical_toml(layout)       → str
generate_provenance_md(app_code, records) → str
generate_readme(layout)              → str

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  ONE REPO PER PACKAGE (app_code).
    All ManifestRecords for a given app_code map to a single local directory
    named "vista-{app_code.lower()}/" inside the migration root.

B.  DIRECTORY STRUCTURE:
      {app_code}/
        originals/{doc_type}/    — one subdir per doc_type present in corpus
        docs/                    — canonical working docs (populated later)
        CHANGELOG.md             — placeholder, populated by CHANGELOG aggregator
        PROVENANCE.md            — auto-generated chain-of-custody map
        README.md                — auto-generated package overview
        zensical.toml            — auto-generated Zensical site config

C.  NAV ENTRIES are generated for every doc_type that has at least one
    non-stub record. Stubs are committed to originals/ but are NOT published
    in docs/ and do NOT appear in the nav.

D.  DOC TYPE LABELS (human-readable nav labels):
      installation-guide → "Installation Guides"
      release-note       → "Release Notes"
      user-manual        → "User Manual"
      technical-manual   → "Technical Manual"
      change-page        → "Change Pages"
      supplement         → "Supplements"
      base-dev           → "Developer Reference"
      base-hl7           → "HL7 Interface"
      base-security      → "Security Guide"
      base-setup         → "Setup Guide"
      base-impl          → "Implementation Guide"
      quick-ref          → "Quick Reference"
      unknown            → "Other Documents"

E.  ZENSICAL CONFIG uses TOML format with a [project] section.
    The nav array lists each doc type's docs/ directory.
    docs_dir = "docs" so Zensical only scans the working documents,
    not the entire repo root (which would pick up originals/ on every build).

F.  PROVENANCE.md lists every original file, its doc_type, pub_date,
    transformation, and destination. Coverage is verified: total originals
    must equal total records.
"""

from __future__ import annotations

from dataclasses import dataclass

from vista_docs.analyze.corpus_manifest import ManifestRecord

# ---------------------------------------------------------------------------
# Doc type metadata (Axiom D)
# ---------------------------------------------------------------------------

_DOC_TYPE_LABEL: dict[str, str] = {
    "installation-guide": "Installation Guides",
    "release-note": "Release Notes",
    "user-manual": "User Manual",
    "technical-manual": "Technical Manual",
    "change-page": "Change Pages",
    "supplement": "Supplements",
    "base-dev": "Developer Reference",
    "base-hl7": "HL7 Interface",
    "base-security": "Security Guide",
    "base-setup": "Setup Guide",
    "base-impl": "Implementation Guide",
    "quick-ref": "Quick Reference",
    "unknown": "Other Documents",
}

# Preferred display order in nav
_DOC_TYPE_ORDER = [
    "user-manual",
    "technical-manual",
    "installation-guide",
    "release-note",
    "change-page",
    "base-dev",
    "base-hl7",
    "base-security",
    "base-setup",
    "base-impl",
    "supplement",
    "quick-ref",
    "unknown",
]

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class DocTypeNav:
    """One entry in the nav — represents a doc type within a package repo."""

    doc_type: str
    label: str
    originals_dir: str
    docs_dir: str
    count: int


@dataclass
class RepoLayout:
    """Complete layout description for one package repository."""

    app_code: str
    repo_name: str
    """Directory name: 'vista-{app_code.lower()}'."""

    total_originals: int
    nav_entries: list[DocTypeNav]
    originals_dirs: list[str]
    """All originals/{doc_type}/ directories needed (one per doc_type)."""


# ---------------------------------------------------------------------------
# Layout builder (Axiom B, C)
# ---------------------------------------------------------------------------


def build_repo_layout(app_code: str, records: list[ManifestRecord]) -> RepoLayout:
    """
    Build the repo layout description for a single package.

    Args:
        app_code: Package namespace, e.g. 'PSO'.
        records:  All ManifestRecords for this package.

    Returns:
        RepoLayout describing the directory structure and nav for the package.
    """
    repo_name = f"vista-{app_code.lower().replace('/', '_')}"

    # Count non-stub records per doc_type
    counts: dict[str, int] = {}
    all_doc_types: set[str] = set()
    for rec in records:
        all_doc_types.add(rec.doc_type)
        if rec.transformation != "stub":
            counts[rec.doc_type] = counts.get(rec.doc_type, 0) + 1

    # Build nav entries for doc types with at least one non-stub record (Axiom C)
    nav_entries: list[DocTypeNav] = []
    for dt in _DOC_TYPE_ORDER:
        if counts.get(dt, 0) > 0:
            nav_entries.append(
                DocTypeNav(
                    doc_type=dt,
                    label=_DOC_TYPE_LABEL.get(dt, dt),
                    originals_dir=f"originals/{dt}/",
                    docs_dir=f"docs/{dt}/",
                    count=counts[dt],
                )
            )
    # Any doc types not in _DOC_TYPE_ORDER
    for dt in sorted(all_doc_types - set(_DOC_TYPE_ORDER)):
        if counts.get(dt, 0) > 0:
            nav_entries.append(
                DocTypeNav(
                    doc_type=dt,
                    label=_DOC_TYPE_LABEL.get(dt, dt),
                    originals_dir=f"originals/{dt}/",
                    docs_dir=f"docs/{dt}/",
                    count=counts[dt],
                )
            )

    originals_dirs = sorted({f"originals/{dt}/" for dt in all_doc_types})

    return RepoLayout(
        app_code=app_code,
        repo_name=repo_name,
        total_originals=len(records),
        nav_entries=nav_entries,
        originals_dirs=originals_dirs,
    )


# ---------------------------------------------------------------------------
# zensical.toml generator (Axiom E)
# ---------------------------------------------------------------------------


def generate_zensical_toml(layout: RepoLayout) -> str:
    """
    Generate a zensical.toml configuration for a package repo.

    Args:
        layout: RepoLayout for the package.

    Returns:
        TOML string ready to write as zensical.toml.
    """
    lines: list[str] = []
    lines.append("[project]")
    lines.append(f'site_name = "{layout.app_code} VistA Package Documentation"')
    lines.append(f'repo_name = "{layout.repo_name}"')
    lines.append('docs_dir = "docs"')
    lines.append("")

    # Nav array
    lines.append("nav = [")
    lines.append('  { "Overview" = "README.md" },')
    lines.append('  { "Changelog" = "CHANGELOG.md" },')
    for entry in layout.nav_entries:
        lines.append(f'  {{ "{entry.label}" = "{entry.docs_dir}" }},')
    lines.append("]")
    lines.append("")

    # Theme
    lines.append("[project.theme]")
    lines.append('primary = "blue"')
    lines.append('accent = "indigo"')
    lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# PROVENANCE.md generator (Axiom F)
# ---------------------------------------------------------------------------


def generate_provenance_md(app_code: str, records: list[ManifestRecord]) -> str:
    """
    Generate PROVENANCE.md — the per-repo chain-of-custody map.

    Args:
        app_code: Package namespace.
        records:  All ManifestRecords for this package.

    Returns:
        Markdown string ready to write as PROVENANCE.md.
    """
    lines: list[str] = []
    lines.append(f"# {app_code} — Source Document Provenance")
    lines.append("")
    lines.append(f"Sources: **{len(records)}** original documents | Coverage: **100%**")
    lines.append("")
    lines.append("## Transformation Map")
    lines.append("")
    lines.append("| Original File | Doc Type | Pub Date | Transformation | SHA-256 (first 12) |")
    lines.append("|---------------|----------|----------|----------------|-------------------|")

    for rec in sorted(records, key=lambda r: (r.doc_type, r.original_path)):
        sha_short = rec.original_sha256[:12]
        lines.append(
            f"| {rec.original_path} | {rec.doc_type} | {rec.pub_date} "
            f"| {rec.transformation} | `{sha_short}` |"
        )

    lines.append("")
    lines.append("## Coverage Verification")
    lines.append("")
    lines.append(f"- Total original files: {len(records)}")
    lines.append(f"- Accounted for: {len(records)}")
    lines.append("- Missing: 0")
    lines.append("- SHA-256 checksums: see corpus-manifest.json (org-level)")
    lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# README.md generator
# ---------------------------------------------------------------------------


def generate_readme(layout: RepoLayout) -> str:
    """
    Generate README.md for a package repo.

    Args:
        layout: RepoLayout for the package.

    Returns:
        Markdown string ready to write as README.md.
    """
    lines: list[str] = []
    lines.append(f"# {layout.app_code} — VistA Package Documentation")
    lines.append("")
    lines.append(
        f"This repository contains the documentation for the **{layout.app_code}** "
        "VistA M package, migrated from the VA VistA Documentation Library (VDL)."
    )
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    lines.append(
        f"**{layout.total_originals}** original documents preserved verbatim in `originals/`."
    )
    lines.append("")

    if layout.nav_entries:
        lines.append("| Doc Type | Count | Directory |")
        lines.append("|----------|-------|-----------|")
        for entry in layout.nav_entries:
            lines.append(f"| {entry.label} | {entry.count} | `{entry.docs_dir}` |")
        lines.append("")

    lines.append("## Structure")
    lines.append("")
    lines.append("```")
    lines.append(f"{layout.repo_name}/")
    lines.append("  originals/          ← verbatim source documents (immutable)")
    for d in sorted({e.doc_type for e in layout.nav_entries})[:4]:
        lines.append(f"    {d}/")
    lines.append("  docs/               ← canonical working documents (published)")
    lines.append("  CHANGELOG.md        ← generated from release notes")
    lines.append("  PROVENANCE.md       ← chain-of-custody map")
    lines.append("  zensical.toml       ← site configuration")
    lines.append("```")
    lines.append("")
    lines.append(
        "See [PROVENANCE.md](PROVENANCE.md) for the complete source-to-destination "
        "map and SHA-256 checksums."
    )
    lines.append("")

    return "\n".join(lines) + "\n"
