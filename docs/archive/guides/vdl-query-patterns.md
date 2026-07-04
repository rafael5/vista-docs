# VDL Query Patterns — A Reusable Discovery Guide

**Subject:** How to find authoritative VistA documentation efficiently
**Audience:** Anyone doing VistA documentation work — spec authors, AI/RAG system builders, IRM engineers, researchers, maintainers
**Mode:** Practical guide and reference — no executable code; queries are specified conceptually
**Status:** Standalone resource — not bound to any specific spec or project

This document is the canonical reference for how to discover authoritative VistA documentation across the three-tier source landscape (index, content, canonical). It is intended to be reused across multiple projects without modification.

---

## 1. Introduction

### 1.1 Purpose

The VistA Documentation Library (VDL) is large (8,800+ documents across 196 packages) and stratified across multiple repositories and source systems. Doing useful work with it — whether building a spec, training an RAG system, or grounding a clinical-informatics analysis — requires knowing which source to query for which question. This guide encodes that knowledge.

### 1.2 What this guide is *not*

- **Not** a tutorial on VistA itself — assumes basic VistA literacy
- **Not** a critique of the current discovery infrastructure — see the companion document *VDL Search & Discovery Infrastructure Assessment* for known issues and proposed improvements
- **Not** a substitute for reading individual documents — it's about *finding* them efficiently

### 1.3 Companion documents

| Document | Purpose | Relationship to this guide |
|---|---|---|
| `vista-package-lifecycle-spec-v5.md` | Specifies install/back-out/rollback/audit for VistA packages | Consumes this guide; was authored using its workflow |
| `vdl-search-assessment.md` | Catalogs current-state issues and proposes improvements | Identifies the *known limitations* you should code around when applying this guide |
| `vista_packages_summary.csv` | 128 pure-VistA packages with documentation-coverage flags | An example output of Recipe G applied to the master index |
| `vdl_inventory_vista_only.csv` | 6,020 rows filtered to pure-VistA system_type | A pre-filtered version of the master index |

---

## 2. The three-tier reference architecture

The VDL is best understood as three layers, each authoritative for a different aspect:

| Tier | Source | Best for | Limitations |
|---|---|---|---|
| **Index** | `vistadocs/vistadocs.github.io/vdl_inventory_enriched.csv` (8,834 rows × 30 columns) | Discovery, filter, scope queries, enumeration, status filtering | Doesn't carry document content |
| **Content (converted)** | `vistadocs/vdl` markdown corpus (1,418 markdown files) | Programmatic reading, AI-friendly access, full-text search | Partial coverage (~39% of unique CSV docs); some conversion artifacts |
| **Canonical** | `va.gov/vdl/...` PDFs/DOCX (linked via `doc_url` in CSV) | Authoritative citation, format fidelity, content the markdown corpus doesn't yet have | Bandwidth-constrained; not optimized for programmatic access |

**The discovery pattern is always the same:**
1. Start at the **index** tier — find the document(s) you need by metadata
2. For content access, try the **converted** tier first — it's parseable and free
3. Fall back to the **canonical** tier when no converted version exists or when format fidelity matters

The interactive search UI at `https://vistadocs.github.io` is a friendly browser-based interface to the index tier.

---

## 3. The master index — `vdl_inventory_enriched.csv`

### 3.1 Source and access

- **Location:** `vistadocs/vistadocs.github.io` repository, root directory
- **Direct URL:** `https://github.com/vistadocs/vistadocs.github.io/blob/main/vdl_inventory_enriched.csv`
- **Size:** ~4.2 MB; one row per VDL document entry
- **Format:** UTF-8 CSV (with known mojibake — see §7.2)
- **Refresh model:** Updated by the maintainers of `vistadocs/vistadocs.github.io`; no embedded version stamp — use file mtime or the GitHub commit SHA for versioning
- **Raw access:** `https://raw.githubusercontent.com/vistadocs/vistadocs.github.io/main/vdl_inventory_enriched.csv`

### 3.2 Schema (30 columns)

The columns most useful for discovery, grouped:

**Identification:**
| Column | Purpose | Example |
|---|---|---|
| `section_name` | Top-level division | `Clinical`, `Infrastructure`, `Financial-Administrative`, `VistA/GUI Hybrids (formerly HealtheVet)`, `Monograph` |
| `app_name_full` / `app_name_abbrev` | Package identity | `Admission Discharge Transfer` / `ADT` |
| `pkg_ns` | M namespace | `DG`, `OR`, `XU` |
| `system_type` | Application class | `VistA`, `Web client`, `COTS product`, etc. — see §3.5 |

**Status & lifecycle:**
| Column | Purpose | Values |
|---|---|---|
| `app_status` | Package lifecycle state | `active`, `archive`, `decommissioned` |
| `cots_dependent` | COTS dependency declaration | Free text describing the COTS dependency, blank otherwise |
| `decommission_date` | When decommissioned | Date string |

**Patch identification:**
| Column | Purpose | Example |
|---|---|---|
| `patch_ver` | Version string | `5.3` |
| `patch_ver_major` / `patch_ver_minor` | Parsed version components | `5` / `3` |
| `patch_num` | Patch number | `1057` |
| `patch_id` / `patch_id_full` | Composite patch identifier | `DG*5.3*1057` |
| `multi_ns` | Cross-package patch flag | `0` or `1` |

**Document identification:**
| Column | Purpose | Example |
|---|---|---|
| `doc_code` | Document type code | `DIBR`, `IG`, `TM`, `RN` |
| `doc_label` | Human-readable doc-type label | `Deployment, Installation, Back-Out, and Rollback Guide` |
| `doc_layer` | Anchor vs patch document — see §3.4 | `anchor`, `patch`, `plain` |
| `doc_title` | Display title | `DG*5.3*1057 Deployment, Installation, Back-Out, and Rollback Guide` |
| `doc_filename` | Source filename | `dg_5_3_1057_dibr.docx` |
| `doc_slug` | Format-stripped filename stem | `dg_5_3_1057_dibr` (use this for deduplication) |
| `doc_format` | File format | `pdf`, `docx`, `doc` |

**Links:**
| Column | Purpose | Example |
|---|---|---|
| `doc_url` | Primary va.gov URL | `https://www.va.gov/vdl/documents/.../dg_5_3_1057_dibr.docx` |
| `companion_url` | Same doc in alternate format | `.pdf` URL when the row is the `.docx`, vice versa |
| `app_url` | VA VDL package landing page | `https://www.va.gov/vdl/application.asp?appid=55` |

### 3.3 Document type taxonomy (`doc_code`)

The fifteen most common document codes in the unfiltered VDL, with their typical purpose and relevance to common workflows:

| Code | Label | Total rows | Typical use |
|---|---|---|---|
| `RN` | Release Notes | 1,598 | What changed in a patch; environment-check details |
| `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 1,342 | Modern install/back-out artifact; the canonical pattern post-OIT-standardization |
| `FORM` | Form | 1,192 | Operational forms (out of scope for most engineering work) |
| `UG` | User Guide | 884 | End-user functional documentation |
| `UM` | User Manual | 880 | Same as UG, older terminology |
| `IG` | Installation Guide | 821 | Pre-DIBRG-era install artifact; still produced for some packages |
| `TM` | Technical Manual | 723 | Package architecture, file structure, RPCs, security keys, callable APIs |
| `CRU` | Change-Request / Update | 336 | Per-patch change descriptions |
| `VDD` | VistA Database Design | 145 | Database/file references for impact analysis |
| `SUP` | Supplement | 129 | Topic-specific addenda to a parent doc |
| `POM` | Production Operations Manual | 127 | Day-2 operations |
| `IG-IMP` | Implementation Guide | 88 | Site-rollout procedures |
| `SG-SET` / `SG` | Setup / Security Guide | 106 | Security-key configuration, role mapping |

**Heuristic — for any package question, retrieve in this order:**

| Question type | Primary doc type | Fallback |
|---|---|---|
| What does this package do? | `TM` | `UG` / `UM` |
| What's in the latest patch? | `RN` | `CRU` |
| How do I install this? | `DIBR` | `IG` |
| How do I configure this? | `SG-SET` | `IG-IMP` |
| What files / RPCs / keys does this own? | `TM` (specifically the structural tables) | `VDD` |
| How do I use this from CPRS / List Manager? | `UG` / `UM` | (none) |

### 3.4 Document layer taxonomy (`doc_layer`)

The corpus distinguishes three document layers:

| Layer | Count | Meaning |
|---|---|---|
| `anchor` | 3,466 | A consolidated "master + N prior versions as appendices" document. The recommended target for citation. |
| `patch` | 3,584 | An individual patch-level release document. May or may not have a markdown counterpart. |
| `plain` | 1,784 | A standalone document that is neither anchor nor patch (e.g. Kernel TM, KIDS User Guide). |

**Practical implication:** When the markdown corpus has an anchor file for a topic, multiple CSV rows (one per patch + the master) all map to that single markdown file. The anchor file's frontmatter declares this via `master_source` and `prior_versions`.

### 3.5 System type taxonomy (`system_type`)

The CSV's `system_type` column is the institutional vocabulary for what kind of application a row's package is. Eleven distinct values:

| Value | Rows | Meaning |
|---|---|---|
| `VistA` | 6,074 | Pure VistA M-server application |
| `Web client` | 896 | Browser-based or thick-client application not running on the M server |
| `VA enterprise service` | 518 | VA-wide service (e.g. authentication, terminology) outside VistA |
| `Integration middleware` | 361 | Middleware between VistA and other systems |
| `VistA + GUI` | 316 | VistA M backend + Windows/web GUI client (e.g. CPRS, BCMA) |
| `VistA + COTS` | 309 | VistA package with embedded COTS components |
| `VBA system` | 144 | Veterans Benefits Administration system (distinct from VHA) |
| `COTS product` | 102 | Commercial off-the-shelf product, not VistA-developed |
| `Data patch` | 64 | Data-only patch (no code), e.g. national reference table updates |
| `VistA + middleware` | 35 | VistA package with middleware integration component |
| `Program documentation` | 15 | Meta-documentation, not application-specific |

**For VistA M-server work specifically**, the most useful filter is `system_type == 'VistA'` (see Recipe G in §6).

### 3.6 Section taxonomy (`section_name`)

| Value | Rows | Scope |
|---|---|---|
| `Clinical` | 5,790 | Clinical applications (CPRS, pharmacy, lab, radiology, nursing, etc.) |
| `Financial-Administrative` | 1,485 | Billing, scheduling, accounts receivable, eligibility, etc. |
| `VistA/GUI Hybrids (formerly HealtheVet)` | 780 | Multi-tier applications spanning M backend + web/Windows clients |
| `Infrastructure` | 777 | Kernel, FileMan, MailMan, Toolkit, HL7, etc. |
| `Monograph` | 2 | Reference monographs (very few rows — see notes for caveat) |

The `(formerly HealtheVet)` parenthetical inside the section name itself is a known data-quality issue (see §7).

---

## 4. The content tier — `vistadocs/vdl` markdown corpus

### 4.1 Structure

The markdown corpus mirrors the VDL section/package hierarchy:

```
vistadocs/vdl/
├── clinical/
│   ├── adt--admission-discharge-transfer/
│   │   ├── deployment-installation-back-out-and-rollback-guide--dibrg.md
│   │   ├── installation-guide.md
│   │   ├── technical-manual.md
│   │   └── patches/  (per-patch documents when available)
│   └── ...
├── financial-administrative/
├── infrastructure/
│   └── xu--kernel/
│       ├── user-manual--kernel-8-0-systems-management-kids-user-guide.md
│       └── ...
└── vista-gui-hybrids/
```

Folder name pattern: `<abbrev>--<slug-of-package-name>`.
File name pattern: `<doc-type-slug>--<variant-slug>.md` (or simpler when no variant).

### 4.2 Frontmatter

Every markdown file carries YAML frontmatter linking it to the index tier and other VistA metadata. Two flavors observed:

**Anchor-document frontmatter** (consolidates multiple patches):

```yaml
---
consolidated_title: "dibrg"
app_code: ADT
doc_type: DIBR
doc_layer: anchor
master_source: "DG*5.3*952 DIBRG"
master_pub_date: February 2020
consolidated_from: 9 versions
prior_versions:
  - "DG*5.3*1016 DIBRG"
  - "DG*5.3*1025 DIBRG"
  ...
---
```

**Plain-document frontmatter** (stand-alone, no consolidation):

```yaml
---
title: "Kernel 8.0 Systems Management: KIDS User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: plain
app_code: XU
app_name: Kernel
section: INF
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
keywords: [...]
---
```

The frontmatter is the linkage between the markdown file and the index CSV — `app_code` ↔ `app_name_abbrev`, `doc_type` ↔ `doc_code`, `master_source` and `prior_versions` ↔ `patch_id_full`.

### 4.3 Anchor consolidation — the many-to-one mapping

Most modern VistA documentation is produced as a series of patch-level documents that get rolled up into a single *anchor* document for browsability. The markdown corpus typically contains the anchor — not the per-patch files.

**Practical implication:** A CSV query that returns 9 rows (e.g. for ADT's 9 DIBRG patches in version 5.3) corresponds to 1 markdown file in the corpus. If you naively expect one markdown file per CSV row, you'll see ~39% coverage. If you account for consolidation, the practical coverage of recently-active packages is much higher.

### 4.4 Coverage relative to the CSV

Approximate coverage as of the last sample:

- CSV unique documents (deduped on `doc_slug`): 3,640
- Markdown files in `vistadocs/vdl`: 1,418
- Naive ratio: ~39%
- After accounting for anchor consolidation: substantially higher in practice for active packages

The biggest coverage gap is older-archive content (legacy packages, decommissioned modules). Active modern packages (recent DIBRGs, Kernel 8.0, FileMan 22.2) are well-covered.

---

## 5. Scope filters

These are the canonical filter rules. Combine them as needed.

### 5.1 Pure VistA M applications (§13 of the package lifecycle spec)

> `system_type == 'VistA'` AND `section_name != 'VistA/GUI Hybrids (formerly HealtheVet)'`

Reduces the 8,834-row index to 6,020 rows / 128 packages. The `section_name` clause matters: 54 rows in the GUI Hybrids section have `system_type == 'VistA'` (M-side documents for hybrid packages); strict pure-VistA scope excludes them.

This is the canonical "scope to pure VistA" filter. Most VistA M-server analyses should apply it as the first scope rule.

### 5.2 Active-only

> `app_status == 'active'`

Excludes `archive` and `decommissioned` packages. **Caveat:** `app_status` is package-level, not document-level — see §7.3.

### 5.3 By section

> `section_name == 'Clinical'`  (or `Infrastructure`, `Financial-Administrative`)

Useful for scoping a domain-focused study (e.g. all clinical-section DIBRGs).

### 5.4 By namespace

> `pkg_ns == 'XU'` (Kernel) or `pkg_ns == 'OR'` (Order Entry / CPRS)

Useful for namespace-focused analysis. **Caveat:** `pkg_ns` is sparsely populated — see §7.6.

### 5.5 By document type

> `doc_code == 'DIBR'` (or `'IG'`, `'TM'`, `'RN'`)

Constrains to a specific artifact type. Often combined with §5.1 + §5.2 for scope-to-active-pure-VistA analyses.

### 5.6 Combining filters

The standard scope chain for a serious VistA-M-server documentation question:

1. Apply §5.1 (pure VistA)
2. Apply §5.2 (active)
3. Apply §5.5 (the doc type relevant to the question)
4. Optionally §5.3 (specific section) or §5.4 (specific namespace)

This typically reduces the 8,834-row index to a few dozen to a few hundred rows — a tractable working set.

---

## 6. Query recipes

These are conceptual queries (specifications, not code) — implementable in pandas, awk, jq-on-csvjson, or a SQL-on-CSV tool of choice.

### Recipe A — All active DIBRGs for a section

> `app_status == 'active'` AND `doc_code == 'DIBR'` AND `section_name == 'Clinical'`
> dedupe on `doc_slug` (collapses PDF + DOCX rows)
> sort by `app_name_abbrev`, `patch_id`

Useful for scoping a clinical-section project; discovering institutional templates within a domain.

### Recipe B — Patch chronology for a single namespace

> `pkg_ns == 'DG'` AND `app_status == 'active'`
> dedupe on `patch_id`
> sort by `patch_ver_major`, `patch_ver_minor`, `patch_num` ascending

Useful for dependency analysis; "what patches must be installed before X?"; identifying test-patch-to-released sequences.

### Recipe C — All Kernel/KIDS-related documentation

> `pkg_ns == 'XU'` OR `app_name_abbrev IN ('XU','XPD','XT')` OR `doc_title CONTAINS 'KIDS'`
> filter `app_status == 'active'`

Useful for anchoring an install-mechanism spec or a Kernel-internals study.

### Recipe D — Find the DIBRG for a specific patch

> `patch_id_full == 'DG*5.3*1057'` AND `doc_code == 'DIBR'`
> prefer `doc_format == 'pdf'` for citation; use `doc_format == 'docx'` for parsing

Useful for targeted lookups when the patch identifier is known.

### Recipe E — Coverage gap analysis

> Group by `app_name_abbrev`, count distinct `doc_code` values
> Filter to packages with `RN` but no `DIBR`

Identifies packages that ship release notes but no formal back-out artifact — useful for prioritizing documentation work.

### Recipe F — Companion-format awareness

For any row where `doc_format == 'pdf'`, `companion_url` (when present) gives the DOCX of the same document. Use when you need parseable content (DOCX → text extraction) but the citation should be to the PDF (more stable URL pattern on VA VDL).

### Recipe G — Filter for pure VistA M applications

> `system_type == 'VistA'` AND `section_name != 'VistA/GUI Hybrids (formerly HealtheVet)'`

The canonical pure-VistA filter (§5.1). 8,834 → 6,020 rows / 128 packages. See §5.1 for rationale.

### Recipe H — All documentation for a single package

> `app_name_abbrev == 'PSO'` AND `app_status == 'active'`
> dedupe on `doc_slug`
> group by `doc_code`

Returns the full active-doc inventory for one package, organized by document type. Useful as the first step in any deep-dive on a specific package.

### Recipe I — All patches in a specific version

> `pkg_ns == 'DG'` AND `patch_ver == '5.3'` AND `doc_code == 'RN'`
> sort by `patch_num` ascending

Returns the chronological release-notes list for one version of one package — the patch timeline.

### Recipe J — Cross-package documentation type coverage

> Pivot: rows = `app_name_abbrev`, columns = `doc_code`, values = COUNT
> Filter columns to {`RN`, `DIBR`, `IG`, `TM`, `UG`}
> Highlight zeros and empty packages

Identifies packages with weak documentation coverage. Useful for documentation-effort prioritization.

---

## 7. Data quality caveats

These are stable enough not to block use but should be coded around in any tooling. The companion *VDL Search & Discovery Infrastructure Assessment* document tracks proposed fixes; this section enumerates the issues *as they exist today* so users can mitigate them.

### 7.1 PDF + DOCX double-counting

Many documents exist in both formats; each format is a separate row. Example: ADT's `dg_5_3_1057_dibr` appears as both PDF (5,097 total format rows) and DOCX (3,730 total).

**Mitigation:** Always dedupe on `doc_slug` before counting documents.

### 7.2 UTF-8 mojibake in titles

Some `doc_title` and `doc_subject` values contain mojibake (UTF-8 decoded as Latin-1). Confirmed patterns include `â€™` (right single quote `'`), `â€"` and `â€"` (em-dash and en-dash). Affects ~70 rows.

**Mitigation:** Either re-decode the affected text fields with `ftfy` or substitute from the source PDF for citations. Filter operations on other columns (`doc_code`, `pkg_ns`, etc.) are unaffected.

### 7.3 Status field is package-level, not document-level

`app_status` reflects the *package's* lifecycle status, not the individual document's. An archived package's recent release notes still carry `app_status == 'archive'`.

**Mitigation:** For document-level lifecycle, fall back to `patch_id` chronology, or treat `doc_layer == 'anchor'` as a proxy for "the consolidated current version."

### 7.4 Markdown corpus is a partial mirror

`vistadocs/vdl` (markdown) covers roughly 39% of the CSV index by unique document, higher when accounting for anchor consolidation.

**Mitigation:** Always cross-check the CSV before assuming a document doesn't exist — it may exist with a `doc_url` to va.gov but not in the markdown mirror. Fall back to the canonical tier when the converted tier is missing.

### 7.5 `app_name_full` occasionally reflects document subject, not package canonical name

Confirmed examples where `app_name_full` does not match the package's canonical identity:

| `app_name_abbrev` | `app_name_full` (in CSV) | Canonical package name |
|---|---|---|
| `OR` | "Group Notes" / "CPRS: Bulk Parameter Editor for Notifications" | Order Entry / CPRS |
| `XU` | "Name Standardization" | Kernel |
| `PXRM` | "Registry: Airborne Hazard Open Burn Pit" / "CPRS: Clinical Reminder Updates" | Clinical Reminders |
| `LR` | (six different full names) | Laboratory |
| `SD` | "Electronic Wait List" / "Scheduling" | Scheduling |
| `PSA` | "Pharmacy: API" / "Pharmacy: Drug Accountability" | (varies — use `pkg_ns`) |

14 distinct abbreviations carry inconsistent `app_name_full` values.

**Mitigation:** Do not use `app_name_full` as the authoritative package name. Use `app_name_abbrev` and cross-reference against the markdown corpus folder names or against an external package master table (e.g. derived from a live VistA's `PACKAGE` file #9.4).

### 7.6 Sparse `pkg_ns` coverage

Roughly 26% of all CSV rows (and 70% of pure-VistA packages) have `pkg_ns` blank. The namespace can usually be inferred from `app_name_abbrev` but not always.

**Mitigation:** Do not depend solely on `pkg_ns` for namespace filtering. Cross-reference with `app_name_abbrev` and an external namespace mapping when accuracy matters.

### 7.7 Multiple abbreviations for the same package

Some packages appear under multiple `app_name_abbrev` values, typically from the KMP\* (Kernel Management Package) consolidation era:

| Canonical name | Abbrevs in CSV |
|---|---|
| Resource Usage Monitor | `RUM`, `KMPR` |
| Statistical Analysis of Global Growth | `SAGG`, `KMPS` |
| Single Signon/User Context | `SSO`, `SSO/UC` |
| Name Standardization | `XOB`, `XU` |
| Standard Files and Tables | `HL`, `XU` |

**Mitigation:** When querying for a known historical package, search for all known abbreviations. When deduplicating package counts, treat these pairs as the same package.

### 7.8 Section name has a parenthetical historical note

The section name `VistA/GUI Hybrids (formerly HealtheVet)` carries a parenthetical context note inside the value. Other sections are clean.

**Mitigation:** Cosmetic; substring match works fine. The `vista-gui-hybrids` slug used in the markdown corpus folder hierarchy is clean.

---

## 8. The discovery workflow

For any VistA documentation question, the workflow that produces a defensible answer:

1. **Frame the question.** What package(s)? What lifecycle phase or topic? What governance scope (single patch, multi-patch project, package-level)?
2. **Apply scope filters.** Combine §5 filters into a working set. Almost always start with §5.1 (pure VistA) and §5.2 (active) unless there's a specific reason not to.
3. **Apply doc-type filter.** §5.5 with the doc types appropriate to the question (the §3.3 heuristic table).
4. **Sample the working set.** If the working set is small (<20), inspect all of it. If large, sample stratified across the dimensions that matter (section, package, patch year).
5. **Read.** For each document in the sample, prefer the markdown tier; fall back to the canonical tier when needed.
6. **Cross-reference findings.** When a finding depends on multiple documents, cite each by `patch_id_full` + `doc_code` (see §10).
7. **Note gaps.** Any claim grounded in fewer than ~5 documents should be labeled "limited sample" rather than "canonical."
8. **Document the workflow itself.** Future readers should be able to reproduce your scope filters and re-run them on a refreshed CSV.

---

## 9. Recommended reusable environment

For any team doing recurring VistA documentation work:

- **Local copy of `vdl_inventory_enriched.csv`** (~4.2 MB; updates infrequently — pull on demand or quarterly)
- **Local sparse clone of `vistadocs/vdl`** (markdown corpus, hundreds of MB total — selectively expand sparse-checkout per topic to keep the working tree small)
- **A query notebook or small script library** implementing the §6 recipes — pandas-on-CSV is the path of least resistance; SQLite-on-CSV is appropriate for larger working sets
- **A standing convention to version-stamp the CSV used** for any analysis: the CSV has no embedded version stamp, so use file mtime or the `vistadocs/vistadocs.github.io` commit SHA at the time of pull
- **A discrepancy log** tracking caveats from §7 as you encounter them — useful for the team's institutional memory and for feeding upstream improvement requests

For teams using LLMs / RAG over the corpus, additional considerations:
- The markdown frontmatter is structured metadata — ingest it as document-level fields, not body text
- `doc_layer == 'anchor'` is the preferred citation target — anchor docs consolidate multiple patches, so RAG retrieval against anchors gives you the whole topic instead of a single-patch slice
- Apply §5 filters at index-time, not query-time, when building per-purpose RAG indexes (e.g. one index per pure-VistA, one per VistA-GUI hybrids)

---

## 10. Citation conventions

When citing VDL documents in derived work:

**Preferred:** Cite by the stable composite identifier:

> `<patch_id_full> <doc_code>` — e.g. `DG*5.3*1057 DIBR`

This is stable across reorganizations of the va.gov directory structure.

**Secondary:** Add the URL only as a convenience link, knowing it may rot:

> `DG*5.3*1057 DIBR ([VA VDL](https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_1057_dibr.pdf))`

**For consolidated (anchor) docs:** Cite the anchor's `master_source` patch identifier, then optionally annotate which prior version is most relevant:

> `DG*5.3*952 DIBRG` (anchor; consolidates 9 versions including the relevant `DG*5.3*1057`)

**For Kernel/Toolkit docs without a patch identifier:** Cite by the document's title and the package version:

> Kernel 8.0 Systems Management: KIDS User Guide

**Avoid:** Citing only by `doc_url` — these URLs can move when the VA reorganizes the directory structure on va.gov, and they don't carry the document type or patch context.

---

## 11. Companion documents and follow-on work

### 11.1 Documents that consume this guide

- `vista-package-lifecycle-spec-v5.md` — was authored using the §8 workflow; §13's pure-VistA filter is Recipe G applied at scope-definition time

### 11.2 Documents that would extend this guide

- An **install-guide-template study** parallel to v5's §3 DIBRG analysis — sample IGs across the 81 IG-carrying packages and produce a §3-equivalent template description for the IG cohort
- A **patch-version chronology study** — sort all DIBRGs by `patch_ver_major × patch_ver_minor × patch_num` and identify when the modern OIT template stabilized
- A **parent/sub-package documentation map** — for packages with no IG and no DIBRG, identify which parent package's documentation actually covers their installation
- A **cross-reference to a live VistA's `PACKAGE` (#9.4) file** — identify any pure-VistA packages that exist in code but lack VDL documentation, or vice versa

### 11.3 Documents that should be read before applying this guide

- `vdl-search-assessment.md` — current-state issues with the discovery infrastructure and proposed improvements. Knowing the known limitations is essential for sound use of §7's mitigations.

### 11.4 Refresh policy for this guide

This document captures discovery patterns as they exist today. The patterns themselves are stable; the underlying data refreshes when `vistadocs/vistadocs.github.io` updates the CSV. Refresh this guide when:

- The CSV schema changes (new columns added or removed)
- A new data quality issue is discovered that affects multiple recipes
- A new recipe is identified as canonical (multiple projects reuse the same query)
- The companion `vdl-search-assessment.md` proposed improvements are implemented (specifically, adding a `github_md_url` column would simplify §4 and add new recipes)
