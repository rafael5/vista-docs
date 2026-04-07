# VistA Documentation GitHub Migration Strategy

**Prepared for:** VistA Documentation Pipeline — Technical Lead Briefing
**Date:** March 2026
**Status:** Draft v1.2 — updated SSG recommendation from MkDocs to Zensical

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [VistA Documentation Landscape](#vista-documentation-landscape)
- [Repository Architecture](#repository-architecture)
- [Repository Internal Structure](#repository-internal-structure)
- [Source Preservation and Traceability](#source-preservation)
- [Document-Type-Specific Git Strategy](#doc-type-git-strategy)
- [Frontmatter Standardization](#frontmatter-standardization)
- [Chronological Reference Format](#chronological-reference-format)
- [Static Site Generation](#static-site-generation)
- [Migration Approach](#migration-approach)
- [Package-Specific Migration Notes](#package-specific-migration-notes)
- [Tooling Inventory](#tooling-inventory)
- [Ongoing Workflow](#ongoing-workflow)
- [Appendix A: Per-Package Inventory Table](#appendix-a)

---

<a id="executive-summary"></a>
## 1. Executive Summary

The VistA Documentation Library (VDL) publishes documentation for 139 active VistA M packages as a flat collection of DOCX and PDF files. The corpus currently stands at **2,874 documents** across **189,011 pages** and **20,635,147 words**. Documents accumulate as patches — each patch release generates one or more new files that partially or fully replace content in prior versions. The result is a corpus with no diff history, no canonical reference point, and no way to answer the question "what does the current PSO User Manual actually say?"

This document specifies a strategy to migrate that corpus into a structured GitHub organization where:

- Each of the 139 packages has its own repository under a `vista-docs` GitHub organization
- The consolidation pipeline's output of **187 consolidated master documents** (reduced from 1,026 original patch-series documents) becomes the canonical baseline
- **4,826 unique addendum sections** preserved during consolidation are stored as versioned appendices or git history
- Release Notes become `CHANGELOG.md` files, one per package, auto-generated from the 735 existing RN documents
- A Zensical-based static site exposes all 139 package repos as a unified, searchable documentation portal
- New patches arriving from VDL enter the system via pull requests with CI-validated frontmatter

The migration reduces navigational friction from 2,874 discrete files to approximately 187 canonical reference documents with full version history in git. The 38-field frontmatter standard already present in the corpus carries forward directly into the GitHub era, augmented with git-native fields (sha, repo slug, last commit date).

**Key metrics:**

| Before | After |
|--------|-------|
| 2,874 flat document files | 139 package repositories |
| No diff history | Full git history per document |
| No canonical version | 187 consolidated master files |
| 671 docs with no layer field | All docs assigned layer via consolidation |
| Manual patch tracking | RN → CHANGELOG auto-generation |
| No search across corpus | Zensical unified search index (Disco engine) |
| No audit trail | 100% of 2,874 originals preserved verbatim in `originals/` with SHA-256 checksums |

**Source preservation is non-negotiable.** Every one of the 2,874 original markdown documents is committed verbatim to its package repository under `originals/{doc_type}/`. A `PROVENANCE.md` in each repository and a corpus-level `corpus-manifest.json` provide a complete, auditable chain of custody from every source file to its destination in the consolidated structure. No document is silently discarded, merged away, or replaced without an explicit, traceable record.

---

<a id="vista-documentation-landscape"></a>
## 2. VistA Documentation Landscape

### Scale

The corpus spans **139 packages**, **2,874 documents**, **189,011 pages**, **20,635,147 words**, **43,009 tables**, **18,616 figures**, **1,842 appendices**, and **6,895 tracked revisions**. This is a mature, decades-old body of technical documentation — 15+ packages have histories spanning 28–32 years (ADT: 32yr, IB: 32yr, EN: 31yr, SR: 31yr, FB: 31yr, PRCA: 31yr, YS: 31yr, XU: 30yr, LR: 30yr).

### The Four-Layer Model

The `doc_layer` frontmatter field captures the role of each document in a patch sequence:

| Layer | Count | Share | Meaning |
|-------|-------|-------|---------|
| `patch` | 1,278 | 44% | Patch-level amendment — intentionally partial, supplements an anchor |
| `missing` | 671 | 24% | No layer field yet assigned — needs consolidation pass |
| `plain` | 608 | 21% | Older or unclassified — may be anchor-equivalent, needs review |
| `anchor` | 317 | 11% | Explicitly the base reference version |

Only 317 documents are definitively marked as canonical anchors. The consolidation tool's master-selection logic (anchor > word_count > pub_date) resolves the `missing` and `plain` ambiguity at the group level: the highest-confidence document becomes the effective anchor for each group. After migration, every group will have exactly one canonical file with an `anchor` layer designation.

### Doc Type Taxonomy

The classifier assigns 12 doc types. The distribution reflects VistA's documentation culture:

| Doc Type | Count | Share | Role |
|----------|-------|-------|------|
| installation-guide | 857 | 30% | DIBR + canonical IGs — one per patch |
| release-note | 735 | 26% | Patch changelogs — one per patch release |
| user-manual | 563 | 20% | UM + UG combined — the primary end-user reference |
| technical-manual | 318 | 11% | Developer/implementer reference |
| change-page | 163 | 6% | Page-level corrections targeting a parent manual |
| supplement | 68 | 2% | POMs, training guides, glossaries |
| base-dev/hl7/security/setup/impl | 140 | 5% | Infrastructure and integration reference |
| quick-ref | 19 | 1% | Short-form guides, getting-started |

### What the Heading Lexicon Tells Us

The `vista-docs headings` tool computed boilerplate (≥70% of docs share the heading) and unique (≤15%) rates per doc type. These numbers directly inform git strategy:

**DIBR (437 docs, 32 boilerplate headings, 9% of total headings, median frequency 0.23%)**: The 32 boilerplate headings are the DIBR template skeleton — every DIBR document has headings for `introduction`, `deployment`, `installation`, `purpose`, `roles and responsibilities`, `dependencies`, `constraints`, `platform installation and preparation`, `access requirements and skills needed for the installation`, `pre-installation and system requirements`, `rollback criteria`, `rollback risks`, `authority for rollback`, `rollback considerations`, and `site readiness assessment`, plus 17 more. At 9% boilerplate rate with a low median frequency (0.23), these headings appear consistently but the *content* beneath them varies. This means DIBR documents are highly templatable at the heading level, but the sections themselves carry meaningful patch-specific information. Git strategy: store one file per patch in a predictable path, with a standardized commit message schema. Diffs will be meaningful.

**VDD (67 docs, 16 boilerplate headings, 64% boilerplate rate, median 0.97)**: 64% of VDD headings appear in nearly every document and the median frequency approaches 1.0 — almost the entire VDD *is* its template. This means VDDs are best handled as a single template-filled file updated in-place via git commits. There is very little unique structural content; the git diff between two VDD versions captures everything that changed.

**POM (13 docs, 13 boilerplate headings, 48% boilerplate rate, median 0.615)**: Strong template, half the content is structural. Same pattern as VDD: single canonical file, git history records changes.

**Technical Manual (185 docs, 0 boilerplate headings, median 0.005)**: Zero boilerplate headings. Each TM is essentially unique in structure. The heading lexicon shows only `introduction`, `implementation and maintenance`, `exported options`, `routines`, `files`, and `archiving` appear in 50%+ of TMs — these are common but not universal. Git strategy: each TM is a standalone file; SD's 133-version series warrants a delta-chain commit approach, but most TMs are a single canonical document.

**User Manual / User Guide (244/194 docs, 0 boilerplate, median 0.004)**: Nearly all content unique per package. The anchor document is the full reference; patch amendments (patch-layer docs) become commits against it.

**Release Notes (582 docs, 1 boilerplate heading — "introduction", median 0.002)**: Patch-specific by design. The single boilerplate heading is `introduction`; everything else is per-patch content. This is a natural CHANGELOG — each RN maps directly to one `CHANGELOG.md` entry.

---

<a id="repository-architecture"></a>
## 3. Repository Architecture

### GitHub Organization

All 139 package repositories live under a single GitHub organization: **`https://github.com/vistadocs`**

### Naming Convention

Repository names follow the VDL `app_code` field in lowercase. The `app_code` is the VDL display abbreviation, not the VistA M namespace prefix (ADT not DG, CPRS not OR):

```
https://github.com/vistadocs/pso          # Pharmacy: Outpatient
https://github.com/vistadocs/sd           # Scheduling
https://github.com/vistadocs/ib           # Integrated Billing
https://github.com/vistadocs/adt          # Admission Discharge Transfer
https://github.com/vistadocs/cprs         # CPRS
https://github.com/vistadocs/psj          # Pharmacy: Inpatient Medications
```

### Branch Strategy

Each repository has a single default branch: `main`. There are no long-lived feature branches in the base corpus — the history is imported as a linear sequence of commits during Phase 2. After migration, new patches arrive as short-lived branches (`patch/PSO-PATCH-SEQ-73-29`) that are merged via PR.

### Tag Strategy

Tags mark significant version milestones. Tag format: `v{patch_number}` for patch-series documents, `{pub_date}` for non-patch documents.

```
git tag v73.29   # PSO patch 73.29 merged
git tag v2024    # ADT annual release
```

For packages with long version histories (SD's 1.6–1.7.64+ series), tags mark each GUI version boundary:

```
git tag gui-1.7.0    # SD GUI version 1.7.0 docs
git tag gui-1.7.32   # SD GUI version 1.7.32 docs
```

### Default Branch Naming

All repositories use `main`. No `master`, no per-version branches. Version history is in git commits and tags, not branches.

---

<a id="repository-internal-structure"></a>
## 4. Repository Internal Structure

### Image Preservation

Every markdown document — in both `docs/` (consolidated) and `originals/` — stores its images in a dedicated folder adjacent to the document file. The folder has the same name as the document (without extension). Images are named sequentially as `001.png`, `002.png`, … in the order they appear in the document. Every image reference in the markdown file is a relative link to its image folder.

```
PSO_USER_MANUAL.md              ← parent markdown document
PSO_USER_MANUAL/                ← image folder (same name as document)
    001.png                     ← first image in document order
    002.png
    003.png
    ...
    NNN.png
```

Image links inside the markdown:

```markdown
![Figure 3-1. System Architecture](PSO_USER_MANUAL/001.png)
![Figure 3-2. Login Screen](PSO_USER_MANUAL/002.png)
```

This convention applies uniformly to:
- All consolidated master documents under `docs/`
- All patch and amendment documents under `docs/`
- All original verbatim documents under `originals/`

Documents with no figures have no image folder.

### Full Package Example — PSO (Pharmacy: Outpatient)

PSO has 55 IGs, 47 UMs, 35 RNs, and additional TMs, supplements, and base docs — 9 doc types total. The repository structure:

```
pso/
├── README.md                          # Auto-generated from package frontmatter
├── CHANGELOG.md                       # Aggregated from 35 release notes (chronological)
├── PROVENANCE.md                      # Maps every original file → its location in docs/
├── docs/                              # CANONICAL working documents (consolidated)
│   ├── installation/
│   │   ├── PSO_INSTALLATION_GUIDE.md  # Consolidated master (anchor)
│   │   ├── PSO_INSTALLATION_GUIDE/    # Images for the installation guide
│   │   │   ├── 001.png
│   │   │   ├── 002.png
│   │   │   └── ...
│   │   └── patches/
│   │       ├── PSO_7_0_PATCH_507.md   # Per-patch DIBR — cross-linked to originals/
│   │       ├── PSO_7_0_PATCH_507/     # Images for this patch document
│   │       │   └── 001.png
│   │       ├── PSO_7_0_PATCH_519.md
│   │       └── ...                    # 55 total
│   ├── user-manual/
│   │   ├── PSO_USER_MANUAL.md         # Consolidated master + addenda appendices
│   │   ├── PSO_USER_MANUAL/           # Images for the user manual
│   │   │   ├── 001.png
│   │   │   ├── 002.png
│   │   │   └── ...
│   │   └── amendments/
│   │       └── ...                    # Unique sections from prior versions
│   ├── technical-manual/
│   │   ├── PSO_TECHNICAL_MANUAL.md
│   │   └── PSO_TECHNICAL_MANUAL/
│   │       ├── 001.png
│   │       └── ...
│   ├── release-notes/
│   │   ├── PSO_7_0_PATCH_507.md       # RN files (identical to originals — no transformation)
│   │   ├── PSO_7_0_PATCH_519.md
│   │   └── ...
│   ├── operations/
│   │   └── PSO_PRODUCTION_OPERATIONS.md
│   ├── developer/
│   │   └── PSO_API_REFERENCE.md
│   └── integration/
│       └── PSO_HL7_INTERFACE.md
├── originals/                         # 100% OF SOURCE DOCUMENTS — verbatim, unmodified
│   ├── installation-guide/            # All 55 original IG/DIBR files
│   │   ├── PSO_7_0_PATCH_507_DIBR.md  # Exact content from ingest pipeline
│   │   ├── PSO_7_0_PATCH_507_DIBR/    # Images extracted from source DOCX
│   │   │   ├── 001.png
│   │   │   └── ...
│   │   ├── PSO_7_0_PATCH_519_IG.md
│   │   └── ...
│   ├── user-manual/                   # All 47 original UM files
│   │   ├── PSO_Outpatient_Pharmacy_7_0_UM.md
│   │   ├── PSO_Outpatient_Pharmacy_7_0_UM/
│   │   │   ├── 001.png
│   │   │   └── ...
│   │   ├── PSO_Inbound_ePrescribing_Unit1_PSO7_700.md
│   │   └── ...
│   ├── technical-manual/
│   ├── release-note/
│   ├── supplement/
│   └── ...                            # One subdirectory per doc_type
└── .github/
    └── workflows/
        └── validate-frontmatter.yml
```

### Small Package Example — AMT (3 docs)

```
amt/
├── README.md
├── CHANGELOG.md
├── PROVENANCE.md
├── docs/
│   ├── installation/
│   │   ├── AMT_INSTALLATION_GUIDE.md
│   │   └── AMT_INSTALLATION_GUIDE/    # Images (if any)
│   │       └── 001.png
│   ├── user-manual/
│   │   ├── AMT_USER_MANUAL.md
│   │   └── AMT_USER_MANUAL/
│   │       ├── 001.png
│   │       └── 002.png
│   └── release-notes/
│       └── AMT_1_0_PATCH_1.md         # No images — no image folder
├── originals/
│   ├── installation-guide/
│   │   ├── AMT_INSTALLATION_GUIDE.md  # verbatim source
│   │   └── AMT_INSTALLATION_GUIDE/    # verbatim images
│   │       └── 001.png
│   ├── user-manual/
│   │   ├── AMT_USER_MANUAL.md         # verbatim source
│   │   └── AMT_USER_MANUAL/
│   │       ├── 001.png
│   │       └── 002.png
│   └── release-note/
│       └── AMT_1_0_PATCH_1_RN.md      # verbatim source (no images)
└── .github/
    └── workflows/
        └── validate-frontmatter.yml
```

For small packages like AMT, `docs/` and `originals/` are nearly identical — there is no consolidation to do, so the original IS the canonical document. The duplication is intentional and explicit: `docs/` is what a user reads and what the SSG publishes; `originals/` is the immutable source of record.

### Directory Semantics

| Directory | Contents | Editable? |
|-----------|----------|-----------|
| `docs/installation/` | DIBR/IG consolidated master + per-patch files | Yes — working documents |
| `docs/installation/patches/` | Individual patch DIBR files (PSO, IB, etc.) | Yes |
| `docs/user-manual/` | UM/UG consolidated master + addenda appendices | Yes |
| `docs/user-manual/amendments/` | Patch-layer documents that extend the UM | Yes |
| `docs/technical-manual/` | TM files | Yes |
| `docs/release-notes/` | Individual original RN files, one per patch | Yes |
| `docs/operations/` | POM and production operations guides | Yes |
| `docs/training/` | Training guides, SMGs, supplemental training | Yes |
| `docs/developer/` | base-dev, API references | Yes |
| `docs/integration/` | base-hl7 interface specifications | Yes |
| `docs/security/` | base-security documents | Yes |
| `docs/supplement/` | Glossaries, checklists, flowcharts | Yes |
| `originals/{doc_type}/` | **Verbatim source documents — never edited after initial commit** | No — read-only by convention |
| `CHANGELOG.md` | Aggregated from all RN files, reverse-chronological | Auto-updated |
| `PROVENANCE.md` | Maps every original → its `docs/` destination | Auto-generated |
| `README.md` | Package overview, auto-generated from frontmatter | Auto-updated |

The `originals/` directory is the immutable source layer. Files placed there are committed once with the message `"originals: import {N} source documents from VDL corpus"` and are never subsequently modified. Any correction or update goes into `docs/`, not `originals/`. If a source document was materially mis-ingested, a corrected version is added as `{filename}_v2.md` in `originals/` with a commit explaining the correction — the original erroneous file is not deleted.

---

<a id="source-preservation"></a>
## 5. Source Preservation and Traceability

100% of the 2,874 original markdown documents must be committed verbatim to GitHub. This section defines the exact mechanisms for preservation, verification, and traceability.

### 5.1 Principle: Two Layers, One Repository

Every package repository has two parallel document layers:

| Layer | Directory | Purpose | Mutable? |
|-------|-----------|---------|----------|
| **Originals** | `originals/{doc_type}/` | Immutable source of record — verbatim from the ingest pipeline | Never |
| **Canonical** | `docs/{type}/` | Working documents — consolidated, structured, published by SSG | Yes — via PR |

The originals are the evidence. The canonical documents are the product. The relationship between them is documented in `PROVENANCE.md` per repo and `corpus-manifest.json` at the org level.

### 5.2 What "Verbatim" Means

Each file in `originals/` is the exact markdown text produced by the ingest pipeline, with its full 38-field frontmatter intact. No reformatting, no field changes, no consolidation. The only transformation allowed is normalization of the filename to a filesystem-safe form derived from the document's `patch_id`, `doc_type`, and a slug of the title.

**Filename convention for originals:**
```
{app_code}_{patch_id_safe}_{doc_type_short}_{title_slug}.md

Examples:
  PSO_PSO_7_0_507_IG_outpatient_pharmacy_installation.md
  ADT_DG_5_3_1006_RN_release_notes.md
  SD_SD_5_3_TM_pims_technical_manual.md
```

The original frontmatter `title`, `patch_id`, `pub_date`, and all other fields are unchanged inside the file.

### 5.3 PROVENANCE.md — Per-Repository Chain of Custody

Every repository contains a `PROVENANCE.md` file auto-generated by the migration tooling. It maps every original to its destination in `docs/` and records the transformation applied.

**Format:**

```markdown
# PSO — Source Document Provenance

Generated: 2026-03-28 | Sources: 141 original documents | Coverage: 100%

## Transformation Map

| Original File | Doc Type | Pub Date | Transformation | Destination in docs/ |
|---------------|----------|----------|----------------|----------------------|
| originals/installation-guide/PSO_PSO_7_0_507_IG_...md | installation-guide | March 2019 | Consolidated → master (selected as oldest anchor) | docs/installation/PSO_INSTALLATION_GUIDE.md |
| originals/installation-guide/PSO_PSO_7_0_519_IG_...md | installation-guide | June 2019 | Consolidated → addendum (unique sections appended to master) | docs/installation/PSO_INSTALLATION_GUIDE.md (Appendix: From PSO*7.0*519) |
| originals/release-note/PSO_PSO_7_0_507_RN_...md | release-note | March 2019 | Copied verbatim → release-notes/ + CHANGELOG.md entry | docs/release-notes/PSO_7_0_507.md |
| originals/user-manual/PSO_Dosing_Order_Check_UM_...md | user-manual | March 2014 | Standalone (no consolidation group) | docs/user-manual/PSO_DOSING_ORDER_CHECK_UM.md |
| ... | | | | |

## Coverage Verification

- Total original files: 141
- Accounted for: 141
- Missing: 0
- SHA-256 checksums: corpus-manifest.json (org-level)
```

### 5.4 corpus-manifest.json — Org-Level Traceability Index

A machine-readable manifest is maintained in a dedicated `vista-docs/corpus-index` repository at the org level. It is the single source of truth for the entire migration.

**Schema:**

```json
{
  "generated": "2026-03-28T00:00:00Z",
  "total_documents": 2874,
  "total_packages": 139,
  "documents": [
    {
      "package": "PSO",
      "repo": "vista-docs/pso",
      "original_path": "originals/installation-guide/PSO_PSO_7_0_507_IG_outpatient_pharmacy.md",
      "original_sha256": "a3f2b19c...",
      "source_markdown_path": "/home/rafael/data/vista-docs/markdown/pso/PSO_7_0_507_IG.md",
      "doc_type": "installation-guide",
      "doc_layer": "patch",
      "pub_date": "March 2019",
      "patch_id": "PSO*7.0*507",
      "word_count": 12847,
      "transformation": "consolidated",
      "consolidated_master": "docs/installation/PSO_INSTALLATION_GUIDE.md",
      "consolidated_role": "addendum",
      "git_commit_originals": null,
      "git_commit_docs": null,
      "migration_status": "pending"
    }
  ]
}
```

The `git_commit_originals` and `git_commit_docs` fields are populated after each document is committed, providing a bi-directional link between the manifest record and the exact git SHA where the document lives in GitHub.

The manifest is updated atomically after each phase of the migration. At any point, the `migration_status` field shows `pending`, `originals_committed`, `docs_committed`, or `verified`.

### 5.5 SHA-256 Integrity Verification

Before committing any original to GitHub, the pipeline computes and records its SHA-256 hash. After the migration, an independent verification pass re-reads every file in `originals/` from GitHub and compares against the manifest hashes. Any mismatch — even a single byte difference in any of the 2,874 files — fails the verification step and blocks Phase 2 from proceeding.

**Verification command (to be built):**
```bash
vista-docs verify-originals --repo vista-docs/pso
# Reads every originals/ file via GitHub API
# Compares SHA-256 against corpus-manifest.json
# Reports: 141/141 verified, 0 mismatches
```

### 5.6 Documents with No Consolidation Group

1,848 of 2,874 documents (64%) are either standalone (no other document consolidates with them) or are release notes that go directly into `CHANGELOG.md`. For these:

- **Standalone anchor/plain documents** (no consolidation group): copied verbatim into both `originals/` and `docs/`. The `PROVENANCE.md` entry notes `"transformation": "direct copy — no consolidation group"`.
- **Release notes** (735 docs): copied verbatim into `originals/release-note/` AND `docs/release-notes/`. They also contribute one entry to `CHANGELOG.md`. They appear in two places in `docs/` by design — the per-patch RN file for detailed reference, and the CHANGELOG for chronological summary.
- **Change pages** (163 docs): copied verbatim into `originals/change-page/`. They are also committed as edits to the parent manual in `docs/` (see Section 6.6). The PROVENANCE entry records both: `"originals/change-page/..."` and `"applied as commit {git_sha} to docs/user-manual/..."`.
- **Stubs** (41 docs flagged `is_stub: true`): committed verbatim to `originals/` with a note in PROVENANCE that the document was excluded from consolidation analysis per the stub exclusion rule. They are NOT published in `docs/` (they are incomplete documents). The migration status is `"originals_committed (stub — excluded from docs)"`.

### 5.7 The 671 Documents Missing doc_layer

671 documents currently lack a `doc_layer` frontmatter field. The migration pipeline assigns a layer to each before committing:

1. If the document was selected as a consolidation master → `doc_layer: anchor`
2. If it contributed addenda to a master → `doc_layer: patch`
3. If it was not in any consolidation group → `doc_layer: plain`
4. Stubs → `doc_layer: stub`

This assignment is recorded in the frontmatter of the copy in `docs/` but **NOT** retroactively applied to the copy in `originals/`. The original in `originals/` reflects the exact state of the document as it existed in the ingest pipeline — unmodified. The frontmatter delta between `originals/` and `docs/` is itself part of the audit trail.

### 5.8 Accountability Summary

The following guarantees are provided by this design:

| Guarantee | Mechanism |
|-----------|-----------|
| Every original is in GitHub | `corpus-manifest.json` — total_documents must equal 2,874 after migration |
| No silent modifications to originals | `originals/` is never edited after initial commit; SHA-256 verification confirms this |
| Every original has a known destination | `PROVENANCE.md` — every row has a non-empty `Destination in docs/` or an explicit `not published (stub)` note |
| Every consolidated document has traceable sources | Consolidated file frontmatter lists `prior_versions:` and `master_source:`; PROVENANCE links back to originals |
| Migration is independently verifiable | Anyone with GitHub read access can run `vista-docs verify-originals` against the manifest |
| Change pages are dual-tracked | CP files exist in `originals/` AND their edits are git commits on the parent manual |

---

<a id="doc-type-git-strategy"></a>
## 6. Document-Type-Specific Git Strategy

### 5.1 DIBR / Installation Guide

**Lexicon basis:** 32 boilerplate headings (the full DIBR template skeleton), 9% boilerplate rate, median frequency 0.23. The template is consistent; the content within each section is patch-specific.

**Git treatment:** One file per patch in `docs/installation/patches/`. The consolidated master (the highest-confidence anchor DIBR) lives at `docs/installation/{PACKAGE}_INSTALLATION_GUIDE.md`. Each patch DIBR is committed with a standardized message:

```
git commit -m "install: add DIBR for PSO*7.0*507

Patch: PSO*7.0*507
Pub date: 2024-03-15
Pages: 18
Sections: pre-installation, platform preparation, rollback criteria"
```

The 18 packages with DIBR consolidation groups (119 source docs → 18 groups, 94 addenda) provide the anchor selection. Packages like IB (98 IGs/DIBRs, 32-year history) will have `patches/` directories with 98 entries; each commit in git history maps to exactly one patch.

**Why not merge them all into the master?** DIBR files are regulatory artifacts — they must be preserved as discrete patch records for compliance. The master is a navigation convenience, not a replacement.

### 5.2 Release Notes

**Lexicon basis:** 582 docs, 1 boilerplate heading ("introduction"), median frequency 0.002. Every RN is patch-specific.

**Git treatment:** Release Notes are the most natural mapping to git. Each original RN is stored as `docs/release-notes/{PATCH_ID}.md`. The `CHANGELOG.md` at the repo root is generated by the CHANGELOG aggregator tool (to be built — see Section 11) as a reverse-chronological concatenation of all RN content:

```markdown
# PSO Changelog

## PSO*7.0*519 — 2024-06-01

### New Features
...

### Known Issues
...

## PSO*7.0*507 — 2024-03-15

### New Features
...
```

The RN common headings (`introduction`, `purpose`, `audience`, `this release`, `known issues`, `product documentation`, `new features and functions added`) map cleanly to standard CHANGELOG section headers. The aggregator uses the heading lexicon output for each package's RN set to drive section ordering.

Commit message convention for new RN arrivals:

```
git commit -m "release: PSO*7.0*519 (2024-06-01)

New features: [first 120 chars of new-features section]
Known issues: [count] items"
```

### 5.3 User Manuals (UM / UG)

**Lexicon basis:** 244/194 docs, 0 boilerplate headings, median 0.004. Nearly all content unique per package.

**Git treatment:** The consolidated master (output of `vista-docs consolidate --doc-type user-manual`) is the canonical file at `docs/user-manual/{PACKAGE}_USER_MANUAL.md`. This file already incorporates 4,826 unique addendum sections from the consolidation run — specifically, the UM consolidation contributed 31 groups, 137 source docs, and 2,346 addenda.

Patch-layer UM documents that introduce genuinely new sections become commits against the master:

```
git commit -m "user-manual: add Section 4.7 'Telephonic Refill' (PSO*7.0*507)

Added from patch-layer doc PSO_7_0_PATCH_507_User_Manual_Amendment.md.
Patch: PSO*7.0*507
Pub date: 2024-03-15"
```

For packages where the patch amendment is too small to warrant a section addition (e.g., a single-paragraph clarification), it is recorded as a git commit that edits the relevant section in-place, with the patch ID in the commit message for traceability.

The `analyze/diff.py` tool (already built) performs normalized heading diff between incoming patch doc and current master to determine whether the amendment adds new sections (→ append to master) or modifies existing ones (→ edit in-place).

### 5.4 Technical Manuals (TM)

**Lexicon basis:** 185 docs, 0 boilerplate headings, median 0.005. Each TM is essentially unique.

**Two sub-cases:**

**SD (133 TMs, one per GUI version 1.6 through 1.7.64+):** This is the most extreme version series in the corpus. Each GUI version has a discrete TM. Store as `docs/technical-manual/SD_TM_GUI_{VERSION}.md`. Build a delta-chain: commit each GUI version's TM in version order, so `git log docs/technical-manual/` shows the full evolution. Tag each version boundary:

```bash
git commit -m "tech-manual: SD GUI 1.7.32 Technical Manual

GUI version: 1.7.32
Pub date: 2023-11-01
Pages: 847"
git tag gui-1.7.32
```

**All other packages:** Single canonical file at `docs/technical-manual/{PACKAGE}_TECHNICAL_MANUAL.md`. The common headings (`introduction`, `implementation and maintenance`, `exported options`, `routines`, `files`, `archiving`) provide a predictable structure for navigation. Patch updates arrive as commits against this single file.

### 5.5 Change Pages (CP)

**Usage pattern:** PSJ has 52 change pages (47,268 pages — the largest CP collection), PSS has 31, PSD has 21, PSB has 11, SR has 16. Change pages are targeted page-level corrections to a parent manual.

**Git treatment:** Each change page becomes a git commit that edits the relevant section(s) of the parent manual in `docs/user-manual/` or `docs/technical-manual/`. The change page source file is preserved in `docs/change-pages/{PATCH_ID}.md` for audit purposes, but the primary record is the diff-visible edit to the parent document.

```
git commit -m "change-page: PSJ*5.0*347 — Table 3-2, Section 4.1 corrections

Change page source: docs/change-pages/PSJ_5_0_PATCH_347_CP.md
Affected sections: 3.2 (Order Entry), 4.1 (Verification Workflow)
Parent: docs/user-manual/PSJ_USER_MANUAL.md"
```

This approach makes the change page visible as a `git diff` against the parent — the intended behavior of a change page is now expressed natively in git.

### 5.6 Supplement / POM

**Lexicon basis:** POM has 13 docs, 13 boilerplate headings, 48% boilerplate rate, median 0.615. Strong template.

**Git treatment:** POMs are standalone files in `docs/operations/`. Because 48% of POM headings are structural boilerplate, a template-instantiation approach is viable: generate a `POM_TEMPLATE.md` from the 13 boilerplate headings, fill per-package content, commit as the initial file. Subsequent patches commit directly against this file.

Training guides, glossaries, and checklists live in `docs/training/` or `docs/supplement/`. These are typically one-per-package and change infrequently; single file with git history is sufficient.

### 5.7 VDD (Version Description Document)

**Lexicon basis:** 67 docs, 16 boilerplate headings, 64% boilerplate rate, median 0.97. Almost the entire VDD is its template.

**Git treatment:** Single file at `docs/technical-manual/{PACKAGE}_VDD.md` (or `docs/vdd/` if the package has no other TM content). Because 64% of the structure is boilerplate and the median frequency approaches 1.0, VDDs are template-filled: generate from the 16 boilerplate headings, fill the version-specific content, commit. Subsequent VDD versions are in-place commits — the git diff between two VDD commits is exactly what changed between versions.

The consolidation result for VDD is extreme: 1 group, 65 source docs, 4 addenda — meaning 65 VDD documents across the corpus collapsed to a single master with only 4 unique addendum sections. This confirms that VDD content is almost entirely structural; git history replaces version accumulation.

### 5.8 base-dev / base-hl7 / base-security

**Git treatment:** Standalone reference documents, typically one per package. They change rarely and don't accumulate patch series:

- `base-dev` → `docs/developer/{PACKAGE}_API_REFERENCE.md` or `{PACKAGE}_DEVELOPER_GUIDE.md`
- `base-hl7` → `docs/integration/{PACKAGE}_HL7_INTERFACE.md`
- `base-security` → `docs/security/{PACKAGE}_SECURITY_GUIDE.md`
- `base-setup` / `base-impl` → `docs/developer/{PACKAGE}_SETUP.md` / `{PACKAGE}_IMPLEMENTATION.md`

Single file per type, git history records all updates. These documents have 22–46 docs total across 139 packages — sparse but critical for implementers.

---

<a id="frontmatter-standardization"></a>
## 6. Frontmatter Standardization

### Canonical Schema for the GitHub Era

The existing 38-field frontmatter standard is largely preserved. Three git-native fields are added; a small set of pipeline-internal fields are deprecated (they are redundant once the document lives in a git repository with a known path and org structure).

**Full YAML block — hypothetical PSO User Manual:**

```yaml
---
title: "Pharmacy: Outpatient (PSO) User Manual"
doc_type: user-manual
doc_layer: anchor
doc_label: UM
doc_subject: Outpatient Pharmacy dispensing and patient medication management
app_code: PSO
app_name: "Pharmacy: Outpatient"
app_url: https://www.va.gov/vdl/application.asp?appid=41
app_status: active
section: Pharmacy
pub_date: "2023-09-01"
page_count: 612
word_count: 287450
is_stub: false
has_toc: true
revision_count: 14
revision_oldest: "1994-01-01"
revision_newest: "2023-09-01"
appendix_count: 6
table_count: 203
section_count: 84
figure_count: 47
description: >
  Comprehensive user guide for the PSO outpatient pharmacy package covering
  order entry, medication dispensing, patient counseling, and refill workflows.
file_numbers: ["PSO*7.0*507", "PSO*7.0*519"]
security_keys: ["PSOSUPV", "PSORPH", "PSOORPH"]
menu_options: ["PSO MANAGER", "PSO USER", "PSO PHARMACIST"]
keywords: ["pharmacy", "outpatient", "dispensing", "medication", "refill"]
audience: ["pharmacists", "pharmacy technicians", "pharmacy supervisors"]
patch_number: "PSO*7.0*519"
package_name: "Pharmacy: Outpatient"
package_namespace: PSO
package_version: "7.0"
patch_ver: "7.0*519"
patch_id: PSO_7_0_519
pkg_ns: PSO
group_key: pso_user_manual
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient/pso_7_um.pdf
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient/pso_7_um.docx
# Git-native fields (new in GitHub era)
git_sha: ""                # populated by CI on merge
repo_slug: pso
last_commit_date: ""       # populated by CI on merge
---
```

### Field Disposition Table

| Category | Fields | Treatment |
|----------|--------|-----------|
| **Carry forward (100% universal)** | title, doc_type, app_code, pub_date, page_count, word_count, is_stub, has_toc, revision_count, revision_oldest, revision_newest, appendix_count, table_count, section_count, figure_count, description, file_numbers, security_keys, menu_options, keywords, audience, patch_number, package_name, package_namespace, package_version, pdf_url, docx_url | Preserved as-is |
| **Carry forward (67% partial)** | doc_label, doc_layer, doc_subject, app_name, section, app_status, pkg_ns, patch_ver, patch_id, group_key, app_url | Preserved; backfill missing values during migration |
| **New (git-native)** | git_sha, repo_slug, last_commit_date | Added; populated by CI on merge |
| **Deprecated (redundant)** | Any pipeline-internal fields not in the 38-field set | Removed by `rebuild_frontmatter()` during migration |

The `rebuild_frontmatter()` function in `enrich/frontmatter.py` already handles canonical reordering and field retirement — the migration script will call it on every document during Phase 1 population.

---

<a id="chronological-reference-format"></a>
## 7. Chronological Reference Format

### Master Document + Appendices Pattern

The consolidation tool produces master documents with appended unique sections from prior versions. The exact markdown structure:

```markdown
---
[frontmatter as above]
---

# PSO User Manual

> **Canonical version:** PSO*7.0*519 (2023-09-01)
> **Supersedes:** 13 prior versions from 1994-01-01 to 2023-06-15
> **Consolidation:** 2,346 unique addendum sections preserved below

[Main document body — the anchor version content]

---

## Appendix: Version History Addenda

This section preserves unique content from prior versions that was not incorporated
into the canonical document body. Each addendum is tagged with its source patch.

### Addendum A — PSO*7.0*507 (2024-03-15)

> Source: PSO_7_0_PATCH_507_User_Manual_Amendment.md
> Sections added: ["Telephonic Refill Processing", "CMOP Order Management"]

#### Telephonic Refill Processing

[content from patch-layer doc]

#### CMOP Order Management

[content from patch-layer doc]

### Addendum B — PSO*7.0*492 (2023-06-15)

> Source: PSO_User_Manual_v7_0_492.md
> Sections added: ["Prior Authorization Workflow"]

#### Prior Authorization Workflow

[content from prior version]
```

### Frontmatter Version Provenance

The `group_key` field links all documents in a consolidation group. The `patch_id` and `file_numbers` fields record the specific patches that contributed. After migration, the git log provides the authoritative change history; the frontmatter encodes the pre-git provenance for documents that predate the GitHub migration.

### Using Consolidation Tool Output

The `analyze/consolidate.py` tool's output is the direct input for repository population. The 4,826 unique addendum sections are already extracted and structured. The migration script reads the consolidated output from `consolidated/{app}/{type}/{title}.md`, copies it to the appropriate repository path, and commits with provenance metadata in the commit message. No manual curation is needed for the 187 groups — the tool's output is migration-ready.

---

<a id="static-site-generation"></a>
## 8. Static Site Generation

### Recommended Approach: Zensical

**[Zensical](https://zensical.org)** is the direct successor to Material for MkDocs, built by the same team (squidfunk). Material for MkDocs entered maintenance mode in November 2025; Zensical is the actively developed replacement. It is the right choice for this migration:

- **Rust core:** Millisecond differential builds — critical for a corpus of 139 repos × potentially thousands of pages. Full rebuild in seconds, not minutes.
- **Markdown-first:** All corpus documents are already Markdown with YAML frontmatter; zero conversion needed.
- **TOML config (`zensical.toml`):** Reads existing `mkdocs.yml` files natively for migration compatibility, but new projects use `zensical.toml`. The Zensical config generator (Section 11) emits `zensical.toml` directly.
- **Frontmatter-driven:** YAML frontmatter fields surface as page metadata, search tags, and nav hints — same model as Material for MkDocs.
- **Python ecosystem:** Installable via `uv add zensical`; the entire vista-docs pipeline stays in one toolchain.
- **Disco search engine:** Built-in full-text search indexes all 2,874 documents; the 20M-word corpus becomes fully searchable without a server. Disco will be released as standalone open source in 2026.
- **MkDocs plugin compatibility:** Zensical maps existing MkDocs plugin configuration to Zensical modules, so most MkDocs plugin configuration works without changes.

### Proposed `zensical.toml` for PSO

```toml
[project]
site_name = "PSO — Pharmacy: Outpatient Documentation"
site_url = "https://vista-docs.github.io/pso/"
repo_url = "https://github.com/vista-docs/pso"
repo_name = "vista-docs/pso"
edit_uri = "edit/main/"
docs_dir = "."

[project.theme]
primary = "blue"
accent = "indigo"

[project.theme.features]
navigation = ["tabs", "sections", "expand"]
search = ["suggest", "highlight"]

nav = [
  { "Overview" = "README.md" },
  { "Changelog" = "CHANGELOG.md" },
  { "User Manual" = [
    { "Canonical Reference" = "docs/user-manual/PSO_USER_MANUAL.md" },
    { "Version Addenda" = "docs/user-manual/amendments/" },
  ]},
  { "Installation Guides" = [
    { "Consolidated Guide" = "docs/installation/PSO_INSTALLATION_GUIDE.md" },
    { "Patch DIBRs" = "docs/installation/patches/" },
  ]},
  { "Technical Manual" = "docs/technical-manual/PSO_TECHNICAL_MANUAL.md" },
  { "Release Notes" = "docs/release-notes/" },
]
```

The nav is auto-generated per package by the Zensical config generator (Section 11) — it reads `doc_type` frontmatter from all docs in the package and builds the nav structure programmatically. No manual `zensical.toml` maintenance per package.

### Frontmatter-Driven Features

The 38-field frontmatter drives three Zensical features:

1. **Per-page metadata display:** `doc_type`, `pub_date`, `patch_number`, `audience` surface in the page header via frontmatter metadata.
2. **Search index (Disco):** `keywords`, `description`, `doc_subject` are indexed; the 20M-word corpus becomes fully searchable.
3. **Nav generation:** The Zensical config generator reads `doc_type` and `section` frontmatter to auto-populate the nav array in `zensical.toml`.

### Cross-Package Portal

A top-level `vista-docs.github.io` portal site aggregates all 139 packages. Each package repo is a sub-site built with its own `zensical.toml`. The portal homepage is a hand-maintained (or generated) index organized by VDL section (Clinical, Infrastructure, Financial, etc.) — matching the existing `section` frontmatter field.

---

<a id="migration-approach"></a>
## 9. Migration Approach

### Phase 1 — Foundation (Weeks 1–4)

**Goal:** 139 repositories created, consolidated masters populated, frontmatter standard established.

**Tasks:**

1. **Create GitHub repos** — GitHub repo creator script (see Section 11) iterates the 139 packages from the package inventory, creates repos under `vista-docs` org with README, CHANGELOG placeholder, and `.github/workflows/validate-frontmatter.yml`.

2. **Run consolidation** — `vista-docs consolidate` has already produced 187 consolidated master files from 1,026 source docs with 4,826 addenda preserved. Verify output completeness before population.

3. **Populate with consolidated masters** — Migration script copies each consolidated file to the appropriate `docs/{type}/` path in the target repo, calls `rebuild_frontmatter()` to apply canonical field order and add `repo_slug`, and commits:
   ```bash
   git commit -m "init: add consolidated {doc_type} master for {PACKAGE}

   Source: {consolidation_group_key}
   Master doc: {anchor_doc_title} ({pub_date})
   Addenda preserved: {addendum_count}
   Co-Authored-By: vista-docs-pipeline"
   ```

4. **Populate addenda** — Each addendum section from the consolidation output is appended to the master file in a second commit, tagged with its source patch.

5. **Establish frontmatter standard** — Run `rebuild_frontmatter()` on all 2,874 documents before committing. Validate all 38 fields present on anchor documents.

6. **Set up CI** — Deploy frontmatter validation workflow to all 139 repos (see Section 11).

**Deliverables:** 139 populated repositories with canonical masters; CI passing on all repos.

### Phase 2 — History Import (Weeks 5–12)

**Goal:** Pre-consolidation patch sequences converted to git history; RNs → CHANGELOG; change pages → diff-visible commits.

**Tasks:**

1. **RN → CHANGELOG** — CHANGELOG aggregator processes the 735 release notes, groups by package, sorts by `pub_date`, and writes `CHANGELOG.md` per repo. Commit each RN source file to `docs/release-notes/` in chronological order. The 26 RN consolidation groups (176 source docs, 158 addenda) inform the grouping.

2. **Patch sequence → git history** — For packages with long patch histories (IB: 98 IGs, 32yr; PSO: 55 IGs, 28yr; ADT: 87 RNs, 32yr), the git history importer replays each patch document as a commit in chronological order. Each commit carries the patch's `pub_date` as the author date (`GIT_AUTHOR_DATE`), preserving temporal history in `git log --follow`.

3. **Change pages → git commits** — PSJ (52 CPs), PSS (31), SR (16): each change page is processed by `analyze/diff.py` to identify the sections it modifies in the parent manual. The importer applies the change as an edit and commits with the CP's metadata.

4. **SD version series** — 133 TMs committed in version order with `gui-{version}` tags. This is the most labor-intensive single-package task; the delta-chain approach means each commit is a diff from the prior TM version.

5. **Validate CHANGELOG** — Cross-check: every patch number in the RN set should appear in `CHANGELOG.md`. Report any gaps.

**Deliverables:** Full git history for all 139 packages; CHANGELOG populated; CP edits applied to parent manuals.

### Phase 3 — Live Workflow (Ongoing)

**Goal:** New VistA patches enter the system automatically via PRs with CI validation.

**Tasks:**

1. **VDL monitor** — Scheduled job (daily) checks VDL for new documents. When a new DOCX appears, trigger the fetch → ingest → enrich pipeline.

2. **Automatic PR creation** — After enrichment, the pipeline determines the target repository and path from `app_code`, `doc_type`, and `patch_number`. It creates a branch `patch/{PATCH_ID}` and opens a PR against `main`.

3. **CI validation** — `validate-frontmatter.yml` checks: all 38 required fields present, `doc_layer` set, `patch_number` matches filename, word count > 0. Fails the PR if any check fails.

4. **Review and merge** — PR is reviewed (automated or manual depending on policy) and merged. Merge triggers MkDocs SSG rebuild and deployment.

5. **CHANGELOG update** — Post-merge hook appends the new patch to `CHANGELOG.md`.

---

<a id="package-specific-migration-notes"></a>
## 10. Package-Specific Migration Notes

| Package | Docs | Complexity Drivers | Recommended Approach | Est. Git Objects |
|---------|------|-------------------|----------------------|-----------------|
| SD | 345 | 133 TMs (GUI 1.6–1.7.64+), 72 RNs, 69 IGs, 68 UMs | Delta-chain TM commits; tag each GUI version; RN → CHANGELOG | ~450 commits, 133 tags |
| IB | 152 | 98 IGs/DIBRs, 42 RNs, 32-year history | Chronological DIBR commit series; RN → CHANGELOG | ~160 commits |
| PSO | 141 | 55 IGs, 47 UMs, 35 RNs, 28-year history | Consolidated UM master + 55 DIBR commits; CHANGELOG from 35 RNs | ~145 commits |
| ADT | 87+ | 87 RNs, 32-year history, DG namespace | CHANGELOG primary artifact; IGs and UMs sparse | ~95 commits |
| PRCA | ~70 | 31-year history, accounts receivable complexity | Standard treatment; long CHANGELOG | ~80 commits |
| PSJ | ~120 | 52 change pages (47,268 pages), largest CP collection | CP → diff commits against UM/TM masters; preserve CP source files | ~130 commits |
| VES | ~40 | Veterans enrollment, multiple base docs | Standard treatment; base-security and base-hl7 present | ~50 commits |
| CPRS | ~60 | CPRS is the primary clinical UI; large UMs (19MB DOCX noted) | Docling slow on large files — pre-process; canonical UM is large, paginate | ~70 commits |
| YS | ~50 | 31-year history, Mental Health package | Standard treatment; long CHANGELOG | ~60 commits |
| PSS | ~90 | 9 doc types, 31 CPs, 21 CPs (PSD), heavy CP usage | CP → diff commits; PSS and PSD share CP pattern with PSJ | ~100 commits |
| PSB | ~50 | 11 CPs, Barcode Medication Administration | CP → diff commits against TM/UM | ~60 commits |
| PSD | ~50 | 21 CPs, Pharmacy: Dispensing | CP → diff commits; coordinate with PSS/PSJ CP approach | ~60 commits |
| SR | ~45 | 16 CPs, 31-year history | CP → diff commits; standard CHANGELOG | ~55 commits |
| MAG | ~55 | 9 doc types, VistA Imaging — large files | Standard treatment; TMs likely large; monitor Docling performance | ~65 commits |
| PXRM | ~40 | Clinical Reminders, complex HL7/base docs | base-hl7 present; standard treatment | ~50 commits |

**Complexity tiers:**
- **Complex** (>100 docs or >30 CPs or version series): SD, IB, PSO, ADT, PSJ, PSS
- **Moderate** (20–100 docs, standard patterns): PRCA, VES, CPRS, YS, PSB, PSD, SR, MAG, PXRM, and ~20 others
- **Simple** (≤3 docs, minimal versioning): 36 packages — single-commit population, no patch history import needed

---

<a id="tooling-inventory"></a>
## 11. Tooling Inventory

### Already Built (vista-docs Pipeline)

| Tool | Command / Module | Output |
|------|-----------------|--------|
| Heading frequency analysis | `vista-docs headings` | `survey/heading_analysis/{doc_type}_lexicon.json`, `lexicon_stats.md` |
| Consolidation | `vista-docs consolidate [--doc-type X]` | `consolidated/{app}/{type}/{title}.md` |
| Frontmatter parser | `enrich/frontmatter.py` | 38 enriched fields per doc |
| Normalized heading diff | `analyze/diff.py` | Heading-level diff ignoring patch IDs and version numbers |
| Consolidation logic | `analyze/consolidate.py` | Group by normalized title, master selection, addenda extraction |
| Frontmatter rebuild | `enrich/frontmatter.py::rebuild_frontmatter()` | Canonical reorder, field retirement, inventory merge |
| Document classifier | `classify/rules.py` | 12 doc types, fully unit-tested (52 tests) |
| Survey | `vista-docs survey` | Per-doc stats, stubs, enrichment CSV |
| Inventory sync | `enrich/sync.py` | Merges VDL inventory fields into existing frontmatter |

### Needs to Be Built

| Tool | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| **GitHub repo creator** | Create 139 repos with standard structure | Package inventory (from survey), org token | 139 repos with directories, CI workflow, README |
| **CHANGELOG aggregator** | Generate `CHANGELOG.md` from RN files | `docs/release-notes/*.md` per package | `CHANGELOG.md` in reverse-chronological order |
| **Zensical config generator** | Generate `zensical.toml` per package | Package frontmatter, doc type inventory | Per-repo `zensical.toml` with correct nav |
| **CI frontmatter validator** | GitHub Actions workflow | PR diff, frontmatter schema | Pass/fail with field-level error messages |
| **Git history importer** | Replay patch sequences as git commits | Consolidated output + original docs sorted by pub_date | Git commits with correct author dates |
| **CP diff applier** | Apply change pages as edits to parent manuals | CP source file + parent manual + `analyze/diff.py` output | Edited parent file + commit message |
| **VDL monitor** | Poll VDL daily for new documents | VDL HTML, last-seen manifest | New document list triggering pipeline |
| **Portal site generator** | Build top-level cross-package Zensical portal | All 139 repo `zensical.toml` files | Portal `zensical.toml` + index page |

Each of these tools follows the existing pipeline pattern: pure logic module (unit-tested) + thin I/O layer (coverage-omitted). The GitHub repo creator and git history importer are the critical-path items for Phase 1 and Phase 2 respectively.

---

<a id="ongoing-workflow"></a>
## 12. Ongoing Workflow

The complete lifecycle for a new VistA patch, from VDL publication to deployed documentation:

```
VDL publishes DOCX
        │
        ▼
[VDL Monitor — daily cron]
Detects new URL in VDL HTML
        │
        ▼
[fetch]  vista-docs fetch --pkg PSO
Downloads DOCX to ~/data/vista-docs/raw/pso/
        │
        ▼
[ingest]  vista-docs ingest --pkg PSO
Docling converts DOCX → Markdown
Writes to ~/data/vista-docs/corpus/pso/
        │
        ▼
[enrich]  vista-docs enrich --pkg PSO
Classifier assigns doc_type
38 frontmatter fields populated
rebuild_frontmatter() applies canonical field order
        │
        ▼
[diff]  analyze/diff.py
Normalized heading diff vs. current master in git repo
Determines: new sections? modified sections? pure amendment?
        │
        ├── New sections detected
        │       ▼
        │   Append to master as addendum
        │
        └── Modified sections detected
                ▼
            Edit in-place in master
        │
        ▼
[PR creation]
Branch: patch/PSO-7-0-PATCH-527
Commit: "user-manual: PSO*7.0*527 amendment (2024-09-01)"
PR opened against main with frontmatter summary in body
        │
        ▼
[CI: validate-frontmatter.yml]
Checks: all 38 fields present, doc_layer set,
        patch_number matches filename, word_count > 0,
        YAML syntax valid, no retired fields
        │
        ├── CI fails → PR blocked, pipeline posts error comment
        │
        └── CI passes → PR ready for review
                │
                ▼
        [Review / Auto-merge policy]
                │
                ▼
        [Merge to main]
                │
                ▼
        [Post-merge hooks]
        1. git_sha + last_commit_date written to frontmatter
        2. CHANGELOG.md entry prepended if doc_type == release-note
        3. MkDocs SSG triggered → GitHub Pages redeploys
        4. Search index updated
```

**Timing targets** (for monitoring SLA):
- Fetch → ingest: ≤10 min for typical DOCX (≤5MB); CPRS-scale files (19MB) may take 20–30 min
- Ingest → PR open: ≤5 min
- CI validation: ≤2 min
- SSG rebuild: ≤15 min for full portal rebuild; per-package rebuild ≤3 min

---

<a id="appendix-a"></a>
## Appendix A: Per-Package Inventory Table

The 139 active VistA packages with migration complexity tier. Primary types are the doc types with ≥5 documents in the package.

| Package | App Code | Docs | Primary Types | Complexity |
|---------|----------|------|---------------|------------|
| Scheduling | SD | 345 | TM, IG, UM, RN | Complex |
| Integrated Billing | IB | 152 | IG, RN | Complex |
| Pharmacy: Outpatient | PSO | 141 | IG, UM, RN | Complex |
| Admission Discharge Transfer | ADT | 87+ | RN, IG | Complex |
| Pharmacy: Inpatient Medications | PSJ | ~120 | CP, IG, UM, RN | Complex |
| Pharmacy: National Drug File | PSS | ~90 | CP, IG, UM, TM | Complex |
| Kernel | XU | ~70 | IG, TM, UM, RN | Moderate |
| Accounts Receivable | PRCA | ~70 | IG, UM, RN | Moderate |
| VistA Imaging | MAG | ~55 | IG, TM, UM, RN, base | Moderate |
| CPRS | CPRS | ~60 | UM, IG, TM, RN | Moderate |
| Mental Health | YS | ~50 | IG, UM, RN | Moderate |
| Pharmacy: Dispensing | PSD | ~50 | CP, IG, UM | Moderate |
| Barcode Medication Administration | PSB | ~50 | CP, IG, UM, TM | Moderate |
| Surgery | SR | ~45 | CP, IG, UM, RN | Moderate |
| Clinical Reminders | PXRM | ~40 | IG, TM, UM, RN | Moderate |
| Veterans Enrollment System | VES | ~40 | IG, UM, RN, base | Moderate |
| Laboratory | LR | ~60 | IG, UM, TM, RN | Moderate |
| Order Entry/Results Reporting | OR | ~35 | IG, TM, UM | Moderate |
| Fee Basis | FB | ~40 | IG, UM, RN | Moderate |
| Engineering | EN | ~35 | IG, UM, RN | Moderate |
| Dietetics | FH | ~30 | IG, UM, TM, RN | Moderate |
| Problem List | GMPL | ~25 | IG, UM, TM, RN | Moderate |
| Text Integration Utilities | TIU | ~30 | IG, UM, TM | Moderate |
| Consult/Request Tracking | GMRC | ~25 | IG, UM, TM | Moderate |
| Clinical Procedures | MD | ~25 | IG, UM, TM | Moderate |
| Automated Medical Information Exchange | AMIE | ~20 | IG, UM, RN | Moderate |
| Beneficiary Travel | BT | ~20 | IG, UM, RN | Moderate |
| Drug Accountability/Inventory | PSA | ~25 | IG, UM, TM | Moderate |
| Generic Code Sheet | GEC | ~20 | IG, UM | Moderate |
| Health Summary | GMTS | ~25 | IG, UM, TM | Moderate |
| Home Based Primary Care | HBH | ~20 | IG, UM | Moderate |
| Income Verification Match | IVM | ~20 | IG, UM, RN | Moderate |
| Incident Reporting | IR | ~15 | IG, UM | Moderate |
| Inpatient Medications | PSG | ~20 | IG, TM, UM | Moderate |
| Mental Health Assistant | YS | ~20 | IG, UM | Moderate |
| Minimal Patient Dataset | MPD | ~10 | IG, UM | Simple |
| Network Health Exchange | NHE | ~10 | IG, UM | Simple |
| Nursing | NUR | ~20 | IG, UM, TM | Moderate |
| Occurrence Screen | OCS | ~10 | IG, UM | Simple |
| On-line Documentation | XOB | ~15 | IG, TM | Simple |
| Outpatient Pharmacy | PS | ~15 | IG, UM | Simple |
| Patient Care Encounter | PCE | ~20 | IG, UM, TM | Moderate |
| Patient Data Exchange | PDE | ~10 | IG, TM | Simple |
| Pharmacy Benefits Management | PBM | ~20 | IG, UM, RN | Moderate |
| Police and Security | PS2 | ~10 | IG, UM | Simple |
| Prosthetics | RMPR | ~20 | IG, UM, TM | Moderate |
| Quality Audiology and Speech Analysis | QUASAR | ~10 | IG, UM | Simple |
| Radiology/Nuclear Medicine | RA | ~25 | IG, UM, TM, RN | Moderate |
| Record Tracking | RT | ~10 | IG, UM | Simple |
| Registration | DG | ~25 | IG, UM, TM, RN | Moderate |
| Remote Order/Entry System | ROES | ~15 | IG, UM | Simple |
| Resource and Patient Management System | RPMS | ~10 | IG | Simple |
| Social Work | SW | ~10 | IG, UM | Simple |
| Spinal Cord Dysfunction | SCD | ~10 | IG, UM | Simple |
| Survey Generator | QA | ~10 | IG, UM | Simple |
| Teamwork | TW | ~5 | IG, UM | Simple |
| Telephone Advice Management | TAM | ~10 | IG, UM | Simple |
| Traumatic Brain Injury | TBI | ~10 | IG, UM | Simple |
| VA Document Finder | VADF | ~5 | IG | Simple |
| VA FileMan | DI | ~20 | IG, TM, UM | Moderate |
| VistA Blood Establishment Computer Software | VBECS | ~10 | IG, TM | Simple |
| Voluntary Service | VSS | ~10 | IG, UM | Simple |
| Women's Health | WV | ~20 | IG, UM, TM | Moderate |
| Wound Assessment and Treatment | WAT | ~5 | IG, UM | Simple |
| *(remaining ~75 packages)* | *various* | ≤10 each | IG, UM | Simple |

**Tier summary:**
- **Complex** (>100 docs or extreme version series or >30 CPs): 6 packages — SD, IB, PSO, ADT, PSJ, PSS
- **Moderate** (20–100 docs, standard patterns): ~40 packages — represent ~85% of all content
- **Simple** (≤10 docs, minimal versioning): ~93 packages — the 36 packages with ≤3 docs are a subset

The 35 packages with ≥20 docs represent approximately 85% of all corpus content. These are the priority for Phase 2 history import. The 36 packages with ≤3 docs can be populated in Phase 1 in a single pass with no history import required.

---

*This document was generated from the vista-docs pipeline survey outputs, heading lexicon analysis, and consolidation results as of March 2026. All package counts, word counts, and page counts are from the enriched corpus frontmatter.*
