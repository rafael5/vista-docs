# VDL Inventory — Label Gaps Strategy
## Resolving `doc_code` and `doc_label` Coverage

**Date:** 2026-03-29
**Source inventory:** `vdl_inventory_enriched.csv`
**Pipeline file:** `enrich_inventory.py`

---

## Table of Contents

1. [Current State](#1-current-state)
2. [Root Cause Taxonomy](#2-root-cause-taxonomy)
3. [Strategy Overview](#3-strategy-overview)
4. [Step 1 — Fix Title Pattern Gaps](#4-step-1--fix-title-pattern-gaps)
5. [Step 2 — Filename Suffix Classification](#5-step-2--filename-suffix-classification)
6. [Step 3 — Group Key Peer Inference](#6-step-3--group-key-peer-inference)
7. [Step 4 — Residual Manual Review](#7-step-4--residual-manual-review)
8. [Reference: Complete doc_code Lexicon](#8-reference-complete-doc_code-lexicon)
9. [Reference: Corpus-Validated Suffix Map](#9-reference-corpus-validated-suffix-map)
10. [Reference: Known Anomalies](#10-reference-known-anomalies)
11. [Projected Impact Summary](#11-projected-impact-summary)

---

## 1. Current State

| Metric | Value |
|---|---|
| Total inventory rows | 8,834 |
| Labelled rows (`doc_code` filled) | 8,143 (92.2%) |
| `va_ref` noise rows (boilerplate, not fixable) | 149 |
| **Substantive unlabelled rows** | **542** |
| **Unique unlabelled documents** | **272** |

The 272 unique unlabelled documents represent **9.5% of the 2,874-document corpus** actually fetched and ingested. They appear as `doc_type: unknown` in frontmatter and in the "Uncategorized" portal nav section.

### Current `doc_code` Distribution (labelled docs)

| `doc_code` | `doc_label` | Count |
|---|---|---|
| `RN` | Release Notes | 1,570 |
| `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 1,316 |
| `FORM` | VBA Form | 1,192 |
| `UM` | User Manual | 871 |
| `UG` | User Guide | 814 |
| `IG` | Installation Guide | 785 |
| `TM` | Technical Manual | 707 |
| `CRU` | Clinical Reminder Update | 336 |
| `VDD` | Version Description Document | 145 |
| `IG-IMP` | Implementation Guide | 88 |
| `POM` | Production Operations Manual | 66 |
| `SG-SET` | Setup Guide | 54 |
| `SG` | Security Guide | 44 |
| `INT` | Interface Specification | 36 |
| `QRG` | Quick Reference Guide | 24 |
| `API` | API / Programmer Manual | 24 |
| `CFG` | Configuration Guide | 16 |
| `TG` | Technical Guide | 15 |
| `TRG` | Training Guide | 10 |
| `REF` | Reference | 8 |
| `PDD` | Patch Description Document | 8 |
| `APX` | Appendix | 4 |
| `FAQ` | Frequently Asked Questions | 4 |
| `DESC` | Description Document | 4 |
| `CVG` | Conversion Guide | 2 |

### Extended doc_codes (proposed — not yet in labelled corpus)

| `doc_code` | `doc_label` | Basis |
|---|---|---|
| `DG` | Developer Guide | Filename suffix `_dg`; title "Developer's Guide" |
| `AG` | Administrator's Guide | Filename suffix `_ag`; title "Administrator's Guide" |
| `SM` | Site Manual / Systems Management Guide | Filename suffix `_sm`; title "Systems Management Guide" |
| `WF` | Workflow Guide | Filename suffix `_wf`; CAPRI workflow documents |
| `RS` | Requirements Specification | Filename suffix `_rs`; TMP Requirements docs |
| `SUP` | Supplement | Filename suffix `_kda`, `_sp`; Known Defects, Supplements |

---

## 2. Root Cause Taxonomy

The 272 unlabelled documents fail for three reasons in priority order:

### Cause A — Title pattern gap in `DOC_TYPE_PATTERNS` (~100 docs)

The title contains a recognizable VA doc-type keyword, but `DOC_TYPE_PATTERNS` in `enrich_inventory.py` has no regex that covers it. This includes:

- Possessive forms: "User's Guide" (apostrophe breaks `User\s+Guide`)
- Acronym-only titles: "JLV Release 2.10 POM" (standalone `\bPOM\b`)
- Phrases in `classify/rules.py` but absent from `DOC_TYPE_PATTERNS`: "Systems Management Guide", "Deployment Guide", "Troubleshooting Guide", "Administrator's Guide", "Developer's Guide"

### Cause B — Filename encodes type but title does not (~80 docs)

The VA naming convention embeds a doc-type abbreviation as the last `_`-separated segment of the filename stem (e.g., `_pom`, `_dg`, `_ag`, `_wf`). `enrich_inventory.py` never reads the filename — it classifies by title only.

### Cause C — No lexical signal in either title or filename (~92 docs)

Purely descriptive titles ("BCMA Version 3 Immunizations Documentation", "Ebola Risk Triage Tool Template") with no standard VA doc-type keyword, and no clean filename suffix. These are the irreducible hard cases.

---

## 3. Strategy Overview

Four steps in priority order. Each step operates only on rows still empty after the previous step.

```
Step 1: Fix title pattern gaps           (~90 unique docs resolved)
Step 2: Filename suffix classification   (~50 additional unique docs)
Step 3: Group_key peer inference         (~20 additional unique docs)
Step 4: Residual manual review           (~100 docs — accept or manual-label)
─────────────────────────────────────────────────────────────────────
Projected residual after Steps 1–3:     ~112 unique docs (~3.9% of corpus)
```

All changes go in `enrich_inventory.py`. No changes to `classify/rules.py` — that classifier serves a different pipeline stage (manifest/frontmatter assignment). The two files maintain separate but compatible lexicons.

---

## 4. Step 1 — Fix Title Pattern Gaps

**File:** `enrich_inventory.py` → `DOC_TYPE_PATTERNS`
**Mechanism:** Add or fix regex patterns matched against the document title
**Ordering rule:** More specific patterns before broader ones; new patterns added in the existing logical sections

### 1a. Critical correction — `User.?s?\s+Guide`

**Current pattern:** `(r'User\s+Guide', 'UG', 'User Guide')`
**Problem:** Does not match "User's Guide" (possessive with apostrophe) or "Users Guide" (no apostrophe).
**Fix:** Change to `User.?s?\s+Guide`

**Docs resolved (18):** All 16 IFCAP Version 5.1 role-specific User's Guides, NOIS User's Guide, ECX DSS FY21 User's Guide, VPFS VistAMigrate Users Guide.

### 1b. `\bPOM\b` standalone acronym

**Problem:** Pattern `\bpom\b` exists in `DOC_TYPE_PATTERNS` but does not fire on 31 JLV/PREM titles ending in "POM". Likely cause: trailing whitespace or encoding artifact in raw VDL title field.
**Fix:** Inspect raw bytes of 2–3 affected rows. If whitespace, strip titles at ingest. If encoding, add `\bPOM\s*$` as a fallback pattern.

**Docs resolved (31):** Entire JLV Release POM series (25 docs), PREM MOCHA POM series (2 docs), others.

### 1c. `System.?s?\s+Management`

**Current pattern:** None in `DOC_TYPE_PATTERNS`. Present in `rules.py` only.
**Fix:** Add `(r'System.?s?\s+Management', 'SM', 'Site Manual / Systems Management Guide')` before the generic `Guide` catchall.

**Docs resolved (19):** NUMI System Management Guides (6 versions), VistALink System Management Guides (3 versions), XWB, XOBE, XOBW, TBI, VPFS, NOIS, QAC, Slotmaster.

### 1d. `Troubleshooting\s+Guide`

**Current pattern:** None.
**Fix:** Add `(r'Troubleshooting\s+Guide', 'SUP', 'Supplement')` in the Supplement section. Troubleshooting guides are adjunct material, not standalone manuals.

**Docs resolved (15):** PIA Startup and Troubleshooting Guide (2 apps), PPS-N Troubleshooting Guide (4 versions), PECS Troubleshooting Guide, YS Troubleshooting Guide, others.

### 1e. `Developer.?s?\s+Guide`

**Current pattern:** `Developer.*Manual` → `API` was added. But "Developer's Guide" with possessive or "Developer Guide" without possessive is not covered.
**Fix:** Add `(r'Developer.?s?\s+Guide', 'DG', 'Developer Guide')` in the Technical docs section, before the generic Guide catchall.

**Docs resolved (12):** VPR Developer's Guide, FM Developer's Guide, XWB Developer's Guide, VistALink Developer Guide (2 versions), VistaLink Developer Guide, YS Developer Guide, others.

### 1f. `Administrator.?s?\s+Guide`

**Current pattern:** `administrator.?s?\s+guide` exists in `rules.py`. Absent from `DOC_TYPE_PATTERNS`.
**Fix:** Add `(r'Administrator.?s?\s+Guide', 'AG', "Administrator's Guide")` in the User docs section.

**Docs resolved (11):** MAG VistA Imaging Exchange (VIX) Administrator's Guide (5 versions), MAG CVIX compound titles, BMS Admin Guide, others.

Note: MAG CVIX titles are compound — "CVIX Administrator's Guide and Production Operations Manual". This pattern will assign `AG`; these docs are dual-purpose. Accept `AG` as primary designation unless a compound-type pattern is added.

### 1g. `Deployment\s+Guide`

**Current pattern:** `deploy\w*\s+guide` exists in `rules.py`. Absent from `DOC_TYPE_PATTERNS`.
**Fix:** Add `(r'Deployment\s+Guide', 'IG', 'Installation Guide')` in the IG section. Deployment guides are operationally equivalent to installation guides.

**Docs resolved (7):** KAAJEE Classic/SSOWAP Deployment Guides (4 versions), XU*8*337 Deployment Guide, MMRS Remediation Guide.

### 1h. `Operations?\s+Manual`

**Current pattern:** `Production\s+Operations\s+Manual` → `POM` (exact match). Does not cover "Operations Manual" without "Production" prefix, or "Productions Operations Manual" (typo with plural "Productions").
**Fix:** Update to `Productions?\s+Operations\s+Manual` and add `Operations?\s+Manual\b` as a broader fallback → `POM`.

**Docs resolved (9):** PREM MOCHA Productions Operations Manual (2), remaining MAG CVIX compound titles, PRC InterSystems Health Connect POM.

### 1i. `\bHandbook\b`

**Fix:** Add `(r'\bHandbook\b', 'UG', 'User Guide')` → `UG`. Handbooks are user-facing reference documents.

**Docs resolved (1):** TIU Generic HL7 Interface Handbook.

### 1j. `\bMenu\b` (standalone)

**Fix:** Add `(r'\bMenu\b', 'UM', 'User Manual')` at end of User docs section. The labelled corpus shows `_menu` → UM (100%, 2/2).

**Docs resolved (1):** Ambulatory Care Reporting Menu.

### Summary — Step 1 patterns to add

Add to `DOC_TYPE_PATTERNS` in `enrich_inventory.py`, in the sections shown:

```python
# User docs section
(r"User.?s?\s+Guide",              'UG',  'User Guide'),           # fix existing User\s+Guide
(r"Administrator.?s?\s+Guide",     'AG',  "Administrator's Guide"),
(r"System.?s?\s+Management",       'SM',  'Site Manual / Systems Management Guide'),
(r"\bHandbook\b",                  'UG',  'User Guide'),
(r"\bMenu\b",                      'UM',  'User Manual'),

# Technical docs section
(r"Developer.?s?\s+Guide",         'DG',  'Developer Guide'),

# IG section
(r"Deployment\s+Guide",            'IG',  'Installation Guide'),

# Supplement section
(r"Troubleshooting\s+Guide",       'SUP', 'Supplement'),

# POM section (update existing Production Operations Manual pattern)
(r"Productions?\s+Operations?\s+Manual", 'POM', 'Production Operations Manual'),
(r"Operations?\s+Manual\b",        'POM', 'Production Operations Manual'),
(r"\bPOM\b",                       'POM', 'Production Operations Manual'),  # after encoding investigation
```

**Estimated net unique docs resolved: ~90** (after deduplication of overlapping patterns)

---

## 5. Step 2 — Filename Suffix Classification

**File:** `enrich_inventory.py` → add `DOC_FILENAME_SUFFIX_MAP` + secondary pass in `enrich_row()`
**Mechanism:** Extract the final `_`-separated segment of `doc_slug` and map to `doc_code`
**Evaluation order:** Applied only when Step 1 returns empty — title classification always takes precedence

### Implementation pattern

```python
import re as _re

_SLUG_SUFFIX_RE = _re.compile(r'[_\-]([a-z]{2,8})$', _re.I)

DOC_FILENAME_SUFFIX_MAP = {
    # key: lowercase suffix → (doc_code, doc_label)
    # ... (see full table below)
}

def classify_by_filename(doc_slug: str):
    m = _SLUG_SUFFIX_RE.search(doc_slug)
    if m:
        return DOC_FILENAME_SUFFIX_MAP.get(m.group(1).lower(), ('', ''))
    return ('', '')
```

In `enrich_row()`, after the title pass:
```python
doc_code, doc_label = classify_doc_type(remainder)
if not doc_code:
    doc_code, doc_label = classify_by_filename(row['doc_slug'])
```

### Complete Filename Suffix Map

All entries are validated against the labelled corpus (see §9 for consensus statistics). The `Corpus %` column shows the agreement rate among all labelled docs with that suffix.

| Suffix | `doc_code` | `doc_label` | Corpus % | Projected docs | Notes |
|---|---|---|---|---|---|
| `_pom` | `POM` | Production Operations Manual | 100% (40/40) | 27 | Excludes 5 MAG docs (title/filename mismatch — see §10) |
| `_raci` | `POM` | Production Operations Manual | 100% (14/14) | — | No unlabelled docs; validates POM mapping |
| `_tg` | `TRG` | Training Guide | 100% (8/8) | 7 | **NOT** Technical Guide — `_tg` = Training Guide in VA convention |
| `_dg` | `DG` | Developer Guide | corpus: mixed | 8 | Developer's guides; Step 1 title pass will catch most |
| `_ag` | `AG` | Administrator's Guide | corpus: mixed | 6 | Step 1 title pass will catch most |
| `_wf` | `WF` | Workflow Guide | N/A | 11 | CAPRI workflow documents; no corpus precedent |
| `_kda` | `SUP` | Supplement | N/A | 7 | VBECS Known Defects and Anomalies |
| `_sp` | `SUP` | Supplement | N/A | 1 | Lock Manager Supplement |
| `_sm` | `SM` | Site Manual / Systems Management Guide | N/A | 4 | Step 1 title pass will catch most |
| `_puse` | `UG` | User Guide | N/A | 1 | Patient use |
| `_adpac` | `UG` | Manager/ADPAC Guide | N/A | 1 | NOIS Application Coordinator |
| `_irms` | `UG` | User Guide | N/A | 1 | NOIS Information Resource Manager |
| `_mm` | `UG` | User Guide | 100% (6/6) | — | No unlabelled docs |
| `_menu` | `UM` | User Manual | 100% (2/2) | 1 | Step 1 `\bMenu\b` will catch this |
| `_ig` | `IG` | Installation Guide | N/A | 5 | BCMA, PXRM, LR, MPIF, XOBW |
| `_dibrg` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 100% (594/594) | 2 | |
| `_dibr` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 100% (422/424) | 1 | |
| `_bckout` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | N/A | 2 | KAAJEE Rollback Instructions |
| `_diborg` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 100% (10/10) | — | Already added to title pattern |
| `_rn` | `RN` | Release Notes | 96% (1068/1112) | 4 | Excludes 1 GMRC mislabel — see §10 |
| `_readme` | `RN` | Release Notes | N/A | 3 | KAAJEE and XU ReadMe files |
| `_notes` | `RN` | Release Notes | 99% (208/210) | 1 | VIAB DIBRO notes |
| `_tm` | `TM` | Technical Manual | 97% (253/262) | 2 | QUASAR, TMP |
| `_manual` | `TM` | Technical Manual | 82% (136/166) | 3 | Corpus majority is TM; minority UM — title pass preferred |
| `_sg` | `SG` | Security Guide | N/A | 1 | BCMA backup security guide |
| `_qr` | `QRG` | Quick Reference Guide | 100% (4/4) | 1 | XU Quick Reference Guide |
| `_tut` | `TRG` | Training Guide | N/A | 1 | FM ScreenMan Tutorial |
| `_tutorial` | `TRG` | Training Guide | N/A | 2 | FM Key and Index Tutorial, VA FileMan DDE Tutorial |
| `_addendum` | `UG` | User Guide | 100% (94/94) | 13 | All SD VSE GUI User Guide Addenda |
| `_pm` | `API` | API / Programmer Manual | 100% (2/2) | 1 | Fee Basis Annual Patch Manual (FB) |
| `_ddd` | `SUP` | Supplement | N/A | 2 | ECX Data Definitions Documents |
| `_glossary` | `SUP` | Supplement | N/A | 1 | EDIS Glossary |
| `_rs` | `RS` | Requirements Specification | N/A | 1 | TMP Requirements Specifications |
| `_signed` | `RS` | Requirements Specification | conflict | 2 | TMP Requirements (signed); labelled corpus maps `_signed`→POM for PRC — app-specific rule needed (see §10) |
| `_plan` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 100% (2/2) | 1 | MHV Emergency Patch Instructions — review before applying |

### Suffixes requiring title sub-pass before mapping

These suffixes are too generic to map blindly; run the title pass first.

| Suffix | Docs | Recommended approach |
|---|---|---|
| `_guide` | 10 | Title determines type: `deployment_guide`→IG, `developer_guide`→DG, `troubleshooting_guide`→SUP, `quick_start_guide`→QRG |
| `_binder` | 2 | Title: "Developer's Guide: Binder"→DG, "Systems Management: Binder"→SM |

### Suffixes with no mapping (accept as unlabelled)

| Suffix | Docs | Title | Disposition |
|---|---|---|---|
| `_cds` | 1 | PXRM Clinical Decision Support template | No standard VDL code; accept `''` |
| `_bank` | 1 | LR lab procedure `003:` series | Covered by §7 (numbered procedure pattern) |
| `_me` | 1 | Note regarding decommissioning of ICR 2.1 | Administrative notice; accept `''` |
| `_vdl` | 1 | Test Document VDL | Placeholder; exclude from corpus if possible |

**Estimated net unique docs resolved by Step 2 (beyond Step 1): ~50**

---

## 6. Step 3 — Group Key Peer Inference

**File:** `enrich_inventory.py` → add peer-inference fallback after Steps 1 and 2
**Mechanism:** For rows still empty after Steps 1–2, look up `group_key` peers with a `doc_code` and apply the consensus code if agreement is 100% among peers.

### Background

`group_key` groups all documents belonging to the same application version (e.g., all docs for `PSJ:PSJ:5`). **198 of 272 unlabelled unique documents** have at least one labelled sibling in the same `group_key`. The labelled-peer distribution:

| Peer `doc_code` | Unlabelled docs with that peer |
|---|---|
| `IG` | 67 |
| `DIBR` | 64 |
| `RN` | 26 |
| `UG` | 18 |
| `UM` | 10 |
| `TM` | 7 |
| `SG-SET` | 5 |
| `API` | 1 |

### Why this is a heuristic, not a rule

A doc in the same `group_key` as an IG is not necessarily itself an IG. The group contains all doc types for that version — User Manual, Technical Manual, Release Notes, and Installation Guide may all share the same group. Peer inference is only reliable when:

1. The group has **exactly one** distinct labelled `doc_code` (all labelled peers agree), AND
2. The unlabelled doc's title or filename offers no contradiction (e.g., a doc whose title contains "workflow" should not inherit `IG` from peers)

### Implementation

```python
def infer_from_peers(row, by_group):
    gk = row.get('group_key')
    if not gk:
        return '', ''
    peers = [p for p in by_group[gk]
             if p['doc_code'] and p['doc_slug'] != row['doc_slug']]
    if not peers:
        return '', ''
    peer_codes = Counter(p['doc_code'] for p in peers)
    # Only apply if all labelled peers agree
    if len(peer_codes) == 1:
        code = list(peer_codes.keys())[0]
        label = peers[0]['doc_label']
        return code, label
    return '', ''
```

Apply only when Steps 1 and 2 both returned empty. Flag inferred rows with a new field `doc_code_inferred = True` for downstream review.

**Estimated net unique docs resolved: ~20** (conservative — only groups where all labelled peers agree)

---

## 7. Step 4 — Residual Manual Review

After Steps 1–3, approximately **~112 unique documents** will remain unlabelled. These fall into four permanent categories:

### Category A — Descriptive patch titles (~40 docs)
Patch-layer documents whose titles describe clinical or operational content with no standard type keyword. Cannot be resolved by any pattern-based approach.

Examples: `MD*1*72 CliO Terminology Dictionary`, `PXRM*2*54 Using The Ebola Risk Triage Tool Template`, `PSS*1*127 Pharmacy Data Management Drug Exception List`

**Disposition:** Accept `doc_code = ''` for these patch-layer documents. Consider bulk-assigning `RN` to patch docs with no other signal — most patch-specific documents without a type keyword are release-note-adjacent.

### Category B — Numbered lab procedure documents (~10 docs)
LR package documents numbered `001:`, `002:`, `003:` with a unique naming convention.

**Disposition:** Add one pattern to `DOC_TYPE_PATTERNS`:
```python
(r'^\d{3}:', 'SUP', 'Supplement')
```
This resolves the entire LR numbered series with a single rule.

### Category C — Specialist operational documents (~20 docs)
Documents using VA-internal terminology outside the standard taxonomy: memoranda, retirement notices, workflow scenarios, combined startup/troubleshooting procedures.

Examples: `eHMP ICRs Status: Memorandum for Record`, `PCMM Mass Discharge Scenarios`, `Retiring Pharmacy Prescription Practices Message`

**Disposition:** Accept `doc_code = ''`. These are genuinely outside the standard taxonomy and cannot be reliably auto-labelled.

### Category D — Non-VistA apps with idiosyncratic naming (~42 docs)
JLV, CAPRI, VBECS, KAAJEE, NOIS, PPS-N, TMP, NUMI, XOBV docs whose titles and filenames do not follow the standard VDL vocabulary. Steps 1–2 will clear most of these; the residual are truly non-standard.

**Disposition:** For the largest remaining non-VistA clusters (JLV POM series is already resolved by `\bPOM\b`; CAPRI Workflow series is resolved by `_wf`), accept the residual or apply app-specific rules as a final fallback:

```python
APP_SPECIFIC_FALLBACKS = {
    # app_name_abbrev → (doc_code, doc_label)
    # Only applied when all other strategies fail
}
```

---

## 8. Reference: Complete doc_code Lexicon

All codes used or proposed in the VDL enrichment pipeline. The **Status** column indicates whether the code is in the current labelled corpus, proposed as an extension, or in `classify/rules.py` only.

| `doc_code` | `doc_label` | Status | Typical title patterns |
|---|---|---|---|
| `RN` | Release Notes | Active (1,570) | `Release Notes`, `Release Note`, `ReadMe`, patch `*rn*` suffix |
| `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | Active (1,316) | `DIBR`, `DIBRG`, `DIBORG`, `Rollback`, `Back-Out` |
| `FORM` | VBA Form | Active (1,192) | VA form numbers (`22-*`, `21-*`, etc.) |
| `UM` | User Manual | Active (871) | `User Manual`, `Clinical Coordinator Manual`, role manuals |
| `UG` | User Guide | Active (814) | `User Guide`, `User's Guide`, addenda, ADPAC guides |
| `IG` | Installation Guide | Active (785) | `Installation Guide`, `Install Guide`, `Deploy Guide`, `Deployment Guide` |
| `TM` | Technical Manual | Active (707) | `Technical Manual`, `_manual` suffix |
| `CRU` | Clinical Reminder Update | Active (336) | `Clinical Reminder Update` |
| `VDD` | Version Description Document | Active (145) | `Version Description Document` |
| `IG-IMP` | Implementation Guide | Active (88) | `Implementation Guide`, `_impg`, `_cig` suffix |
| `POM` | Production Operations Manual | Active (66) | `Production Operations Manual`, `\bPOM\b`, `_pom`, `_raci` suffix |
| `SG-SET` | Setup Guide | Active (54) | `Setup Guide`, `Set Up and Configuration Guide` |
| `SG` | Security Guide | Active (44) | `Security Guide`, `Security Manual`, `_sg` suffix |
| `INT` | Interface Specification | Active (36) | `Interface Specification`, `HL7 Interface`, `_id`, `_spec`, `_flows` suffix |
| `QRG` | Quick Reference Guide | Active (24) | `Quick Reference Guide`, `Brochure`, `Checklist`, `_qr` suffix |
| `API` | API / Programmer Manual | Active (24) | `API Manual`, `Programmer Manual`, `Developer.*Manual`, `_pm` suffix |
| `CFG` | Configuration Guide | Active (16) | `Configuration Guide`, `Setup and Configuration Guide` |
| `TG` | Technical Guide | Active (15) | `Technical Guide` (title-matched; NOT `_tg` suffix) |
| `TRG` | Training Guide | Active (10) | `Training Guide`, `Training Manual`, `Tutorial`, `_tg` suffix (100% corpus) |
| `REF` | Reference | Active (8) | `Reference Card`, `Reference Guide`, Flowcharts |
| `PDD` | Patch Description Document | Active (8) | `Patch Description` |
| `APX` | Appendix | Active (4) | `Appendix` |
| `FAQ` | Frequently Asked Questions | Active (4) | `FAQ`, `Frequently Asked Questions` |
| `DESC` | Description Document | Active (4) | `Description Document` |
| `CVG` | Conversion Guide | Active (2) | `Conversion Guide` |
| `DG` | Developer Guide | **Proposed** | `Developer's Guide`, `Developer Guide`, `_dg` suffix |
| `AG` | Administrator's Guide | **Proposed** | `Administrator's Guide`, `Admin Guide`, `_ag` suffix |
| `SM` | Site Manual / Systems Management Guide | **Proposed** | `Systems Management Guide`, `System Management Guide`, `Site Manual`, `_sm` suffix |
| `WF` | Workflow Guide | **Proposed** | Workflow documents, `_wf` suffix |
| `RS` | Requirements Specification | **Proposed** | Requirements Specifications, `_rs` suffix (TMP-specific) |
| `SUP` | Supplement | **Proposed** | Known Defects, Supplements, Troubleshooting Guides, numbered lab procedures, `_kda`, `_sp`, `_wf` suffix |

---

## 9. Reference: Corpus-Validated Suffix Map

Derived from the 8,143 labelled rows in `vdl_inventory_enriched.csv`. Only suffixes with ≥4 labelled occurrences and ≥80% consensus are listed. These have statistical backing from the existing corpus — they are not manual assignments.

| Filename suffix | `doc_code` | Consensus | Sample size |
|---|---|---|---|
| `_are` | `FORM` | 100% | 1,043 |
| `_dibrg` | `DIBR` | 100% | 594 |
| `_dibr` | `DIBR` | 100% | 422 |
| `_rn` | `RN` | 96% | 1,112 |
| `_um` | `UM` | 97% | 315 |
| `_tm` | `TM` | 97% | 262 |
| `_ug` | `UG` | 94% | 265 |
| `_notes` | `RN` | 99% | 210 |
| `_vdd` | `VDD` | 99% | 147 |
| `_manual` | `TM` | 82% | 166 |
| `_addendum` | `UG` | 100% | 94 |
| `_form` | `FORM` | 100% | 149 |
| `_pom` | `POM` | 100% | 40 |
| `_impg` | `IG-IMP` | 100% | 26 |
| `_raci` | `POM` | 100% | 14 |
| `_cig` | `IG-IMP` | 88% | 16 |
| `_diborg` | `DIBR` | 100% | 10 |
| `_dirb` | `DIBR` | 100% | 8 |
| `_img` | `IG-IMP` | 100% | 8 |
| `_tg` | `TRG` | **100%** | 8 |
| `_id` | `INT` | 100% | 7 |
| `_mm` | `UG` | 100% | 6 |
| `_faq` | `FAQ` | 100% | 4 |
| `_qr` | `QRG` | 100% | 4 |
| `_spec` | `INT` | 100% | 4 |
| `_iug` | `UG` | 100% | 4 |
| `_rec` | `UM` | 100% | 4 |

**Critical note on `_tg`:** In VA naming convention, `_tg` means **Training Guide** (TRG), not Technical Guide (TG). The corpus confirms this at 100% (8/8). Any implementation that maps `_tg` to TG is incorrect.

---

## 10. Reference: Known Anomalies

These are cases where the filename suffix and document title disagree. Do not apply the generic suffix map to these rows — assign manually.

| `doc_slug` pattern | App | Title says | Suffix says | Correct code | Action |
|---|---|---|---|---|---|
| `mag_cx_*_ag_pom` (5 docs) | MAG | "CVIX Administrator's Guide" | `_pom` | `AG` | Title takes precedence; `_pom` is a VDL cataloguing error |
| `mag_cvix_admin_prod_ops_guide_f` | MAG | "CVIX Administrator's Guide and Production Operations Manual" | (compound) | `AG` | Compound title; assign primary type |
| `gmrc_*_57rn` | GMRC | "Suicide Hotline Consult Setup" | `_rn` | `IG` | Setup document mislabelled as RN in VDL |
| `hc_hl7_messaging_pom_ecms_signed` | PRC | "HL7 Messaging Product Operations Manual" | `_signed` | `POM` | Labelled corpus: `_signed` → POM for PRC |
| `tmp_*_signed` (2 docs) | TMP | "Requirements" | `_signed` | `RS` | TMP Requirements docs — different from PRC POM |

The `_signed` suffix requires app-specific disambiguation: for `app_name_abbrev == 'PRC'` → `POM`; for `app_name_abbrev == 'TMP'` → `RS`.

---

## 11. Projected Impact Summary

| Step | Mechanism | New unique docs resolved | Cumulative resolved | Remaining |
|---|---|---|---|---|
| Baseline | — | — | 0 | 272 |
| Title pattern fixes (§4) | 10 new/fixed patterns in `DOC_TYPE_PATTERNS` | ~90 | ~90 | ~182 |
| Filename suffix map (§5) | Secondary pass on `doc_slug` suffix | ~50 | ~140 | ~132 |
| Group_key peer inference (§6) | 100%-consensus peer association | ~20 | ~160 | ~112 |
| LR numbered procedure pattern (§7B) | `^\d{3}:` → SUP | ~5 | ~165 | ~107 |
| **Projected residual** | | | | **~107 docs** |
| **As % of 2,874-doc corpus** | | | | **~3.7%** |

The projected residual of ~107 documents (3.7% of corpus) consists of genuinely atypical documents — purely descriptive patch titles, VA-internal administrative notices, and non-VistA apps with idiosyncratic naming — that cannot be reliably classified by any lexical or structural heuristic without reading the document content.

### Implementation priority

| Priority | Step | Effort | Yield |
|---|---|---|---|
| 1 | Fix `User.?s?\s+Guide` (1-char change) | Trivial | 18 docs |
| 2 | Add `\bPOM\b` after encoding investigation | Low | 31 docs |
| 3 | Add remaining title patterns (§4c–§4j) | Low | ~40 docs |
| 4 | Implement filename suffix map | Medium | ~50 docs |
| 5 | Group_key peer inference | Medium | ~20 docs |
| 6 | LR `^\d{3}:` pattern | Trivial | ~5 docs |
| 7 | Accept or manually label residual ~107 | High | ~107 docs |
