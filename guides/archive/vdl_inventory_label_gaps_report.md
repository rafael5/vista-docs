# VDL Inventory — Unlabelled Documents Report
## Documents with `doc_code = ''` and `doc_label = ''`

**Date:** 2026-03-29 (updated after pattern fixes and filename-suffix analysis)
**Source:** `vdl_inventory_enriched.csv`

---

## Summary

| Metric | Baseline | After title-pattern fixes | After filename-suffix (projected) |
|---|---|---|---|
| Total rows with empty `doc_code` and `doc_label` | 741 | 691 | ~443 |
| — of which `noise_type = 'va_ref'` (boilerplate) | 149 | 149 | 149 |
| **Substantive unlabelled rows** | **592** | **542** | **~294** |
| Unique documents (by `doc_slug`) | **297** | **272** | **~148** |

The 542 remaining substantive rows represent **272 unique documents**. A dry-run filename-suffix classification (see §5) projects resolving a further ~124 unique documents, leaving ~148 irreducible hard cases.

---

## 1. Distribution by `doc_layer`

| `doc_layer` | Rows | Unique docs |
|---|---|---|
| `anchor` | 288 | 144 |
| `patch` | 161 | 81 |
| `plain` | 93 | 48 |
| **Total** | **542** | **272** |

The `plain` layer shrank significantly (100 → 48 unique docs): the extended `PATCH_B` regex now detects bare version strings (`v2.2`, `Release N`, `X.Y.Z`), promoting many previously `plain` documents to `anchor`. Of those newly promoted anchor documents, a subset also had their `doc_code` resolved by the new type patterns; the rest are now correctly classified as `anchor` but remain unlabelled.

The `anchor` count rose (108 → 144 unique docs) for this reason: more documents are now recognised as version-level references, but their doc-type keyword still falls outside `DOC_TYPE_PATTERNS`.

---

## 2. Distribution by App

| `app_code` | App Name | anchor | patch | plain | total rows |
|---|---|---|---|---|---|
| `JLV` | Joint Longitudinal Viewer | 51 | — | — | 51 |
| `MAG` | VistA Imaging System | — | 16 | 18 | 34 |
| `PRC` | IFCAP | 32 | — | 2 | 34 |
| `SD` | Scheduling | 26 | 2 | 1 | 29 |
| `XU` | Kernel | 10 | 16 | 2 | 28 |
| `CAPRI` | Compensation and Pension Record Interchange | — | 22 | 2 | 24 |
| `KAAJEE` | KAAJEE (XU and XWB) | 10 | 10 | 2 | 22 |
| `NOIS` | National Online Information Sharing | 14 | — | 6 | 20 |
| `VBECS` | Laboratory: VistA Blood Establishment Computer Software | 16 | — | 2 | 18 |
| `PPS-N` | Pharmacy: Pharmacy Product System - National | 16 | 2 | — | 18 |
| `LR` | Laboratory (LA and LR) | 2 | 4 | 8 | 14 |
| `TMP` | Telehealth Management Platform | 12 | 2 | — | 14 |
| `NUMI` | National Utilization Management Integration | 12 | — | 2 | 14 |
| `DI` | FileMan | 4 | — | 8 | 12 |
| `XOBV` | VistALink | 12 | — | — | 12 |
| `XWB` | RPC Broker | — | 10 | — | 10 |
| `PECS` | Pharmacy Enterprise Customization System | 4 | 6 | — | 10 |
| `HL7` | HL7 (VistA Messaging) | 8 | — | — | 8 |
| `TIU` | CPRS: Text Integration Utility | 2 | 2 | 2 | 6 |
| `LA` | Laboratory: Universal Interface | 6 | — | — | 6 |
| `XM` | MailMan | 4 | 2 | — | 6 |
| `ECX` | Decision Support System (DSS) Extracts | 2 | 4 | — | 6 |
| *(55 other apps)* | | | | | 146 |

**Non-VistA and peripheral apps account for 203 rows (101 unique docs)** — JLV, CAPRI, VBECS, KAAJEE, NOIS, PPS-N, TMP, NUMI, XOBV, DHT, and XWB use naming conventions that predate or diverge from the standard VA doc-type vocabulary, so the title parser finds no match.

**Core VistA packages account for 339 rows (172 unique docs)** where a label should exist but was not parsed.

---

## 3. Root Causes

### Cause 1 — Patch-prefixed titles with non-standard doc-type suffix (81 unique docs)

These documents have a valid `NS*V*P` patch prefix — the parser correctly identified the namespace, version, and patch number — but the remainder of the title after stripping the patch identifier did not match any pattern in `DOC_TYPE_PATTERNS`. The document has a `doc_layer = 'patch'` but no `doc_code`.

**Examples (still unresolved):**

| App | Title |
|---|---|
| `MD` | `MD*1*72 CliO Terminology Dictionary & Clinical Data Model Revised` |
| `PSB` | `PSB*3*47/PSS*1*141 BCMA Version 3 Immunizations Documentation` |
| `PSB` | `PSB*3*84 BCBU Version 3 Securing the Cache Cube for BCMA Backup` |
| `ASU` | `USR*1*33 Show User Class Name in ASU Options` |
| `PSS` | `PSS*1*127 Pharmacy Data Management Drug Exception List` |
| `PXRM` | `PXRM*2*54 Using The Ebola Risk Triage Tool Template` |
| `PXRM` | `PXRM*2*74 COVID-19 CPRS Status Version 5` |
| `GMRC` | `GMRC*3*57 Suicide Hotline Consult Setup` |
| `RMPR` | `RMPR*3*61 Prosthetics Inventory Package (PIP) Lessons Learned` |
| `LR` | `LA*5.2*68 Laboratory HL7 Specification` |

The singular "Release Note" (→ `RN`), `Install/Implement Guide` (→ `IG`), `Action Item` (→ `IG`), brochures, and checklists that were listed in this section previously have been resolved by the title-pattern fixes. The remaining cases use purely descriptive titles — "Immunizations Documentation", "Drug Exception List", "Ebola Risk Triage Tool Template" — with no standard VA doc-type keyword in the title. Many of these will be resolved by filename-suffix classification (see §5).

---

### Cause 2 — Version-level docs (anchor layer) with non-standard type names (144 unique docs)

These documents carry a version phrase so the parser assigned `doc_layer = 'anchor'`, but the doc-type keyword in the title does not match any `DOC_TYPE_PATTERNS` entry. This count is higher than before the fixes (108 → 144) because the extended `PATCH_B` regex now promotes additional plain-layer documents to anchor when a bare version string (`v2.2`, `Release N`, `X.Y.Z`) is detected.

**Examples (still unresolved):**

| App | Title |
|---|---|
| `TIU` | `Additional Signer Utility Guide (TIU*1.0*357)` |
| `ACKQ` | `QUASAR Version 3 Technical/Pkg Security (Updated ACKQ*3*13)` |
| `RA` | `Radiology Version 5 HL7 Setup Manual` |
| `EDIS` | `Emergency Department Integration Software Glossary` |
| `TBI` | `TBI Version 4.2 System Management Guide` |
| `JLV` | `JLV Release 2.10 POM` |
| `PRC` | `IFCAP Version 5.1 Accounts Payable User Manual` |
| `NOIS` | `NOIS Version 7.0 Technical and User Manual` |
| `PXRM` | `Clinical Reminders Version 2 Manager's Manual` |

**Root cause sub-patterns:**

1. **Doc-type keyword present but ordering/format mismatch.** `IFCAP Version 5.1 Accounts Payable User Manual` — `User Manual` is a valid pattern but a whitespace or encoding artifact in this specific row prevents the match.

2. **POM as standalone acronym.** JLV uses `POM` at the end of titles (`JLV Release 2.10 POM`). The `\bpom\b` pattern in `DOC_TYPE_PATTERNS` should match — these rows likely have a trailing whitespace or encoding artifact. Resolvable by filename suffix `_pom`.

3. **Compound type names.** `Technical/Pkg Security`, `System Management Guide`, `Technical and User Manual` — these combine two doc-type keywords in a way no single pattern covers.

---

### Cause 3 — Plain-layer docs with no version, no patch, and no recognized type (48 unique docs)

These documents have no parseable version or patch in either the title or filename, and their title does not match any doc-type pattern. This category shrank from 100 to 48 unique docs — partly through new pattern matches, partly through PATCH_B promoting bare-version titles to anchor.

**Examples (still unresolved):**

| App | Title |
|---|---|
| `ACR` | `Ambulatory Care Reporting Menu` |
| `PSS` | `Pharmacy Interface Automation (PIA) Startup and Troubleshooting Guide` |
| `TIU` | `TIU Generic HL7 Interface Handbook` |
| `PCMM` | `Primary Care Management Module (PCMM) Mass Discharge Scenarios` |
| `RMDS` | `RAI/MDS Electronic Transmission Manual` |
| `PXRM` | `AHOBP Clinical Portal Manual` |
| `HMP` | `eHMP Integration Control Registrations (ICRs) Status: Memorandum for Record` |
| `SD` | `Test Document VDL` |
| `LR` | `001: Not Performed/Multiple Specimens/Incomplete Data Entry` |
| `LR` | `002: Antibody Lookup` |

**Root cause sub-patterns:**

1. **Specialist operational documents.** "Memorandum for Record", "Mass Discharge Scenarios", "Startup and Troubleshooting Guide" — VA-internal terminology with no standard doc-type keyword.

2. **Numbered lab procedure documents.** LR's `001:`, `002:`, `003:` series are package-specific lab procedure resolution docs with a unique naming convention.

3. **Standalone tool documentation.** `Ambulatory Care Reporting Menu`, `TIU Generic HL7 Interface Handbook` — genuine reference documents whose type label (`Menu`, `Handbook`) has no entry in `DOC_TYPE_PATTERNS`. Many will be resolved by filename suffix.

---

## 4. Fixes Applied (Title Patterns and PATCH_B)

The following changes to `enrich_inventory.py` were implemented and resolved **50 rows / 25 unique documents**:

| Pattern added | `doc_code` | `doc_label` | Resolved |
|---|---|---|---|
| `Release\s+Notes?\b` (singular + plural) | `RN` | Release Notes | `RA*5*97 Release Note` and similar |
| `Install\s*/\s*Implement\s+Guide` | `IG` | Installation Guide | `ACKQ*3*13 Install/Implement Guide` |
| `\bDIBORG\b` (added to existing DIBR pattern) | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | DHT DIBORG build documents |
| `Programmer\s+Manual` | `API` | API Manual | `VA FileMan Programmer Manual` |
| `Developer.*Manual` | `API` | API Manual | `HL7 Developer and Operations Manual` |
| `(?:Site\s+)?Manager.*Manual\b` | `UG` | Manager/ADPAC Guide | `HL7 Site Manager & Developer Manual` |
| `\bbrochure\b` | `QRG` | Quick Reference Guide | `Clinician Brochure`, `Quick Reference Brochure` |
| `\bchecklist\b` | `QRG` | Quick Reference Guide | `CAC Checklist`, `Airborne Hazard Checklist` |
| `\bAction\s+Item\b` | `IG` | Installation Guide | VSE GUI Action Item-Install notes |
| `\bsetup\s+notes?\b\|\bset.up\s+notes?\b` | `IG` | Installation Guide | `OR*3*190 Set Up Notes` |
| Extended `PATCH_B` to match `v\d+\.\d+`, `Release\s+\d+`, bare `\d+\.\d+\.\d+` | — | — | Promoted 52 plain docs to anchor layer; enabled doc_type resolution for version-bearing titles |

---

## 5. Filename-Suffix Classification Strategy

### Background

VA document filenames follow a consistent naming convention: the final `_`-separated segment before the extension encodes the document type (e.g. `jlv_2_10_pom.docx`, `psb_3_p84_bcbu_sg.docx`, `xobv_1_6_dg.docx`). The `enrich_inventory.py` enrichment pipeline's `classify_doc_type()` function currently operates exclusively on the document title. The `doc_filename` field — which carries this VA naming-convention signal — is not consulted.

Adding a filename-suffix classification pass as a **secondary signal** (applied when title classification returns empty) would resolve an estimated **~124 additional unique documents** using a deterministic, auditable mapping table, requiring no fuzzy matching or inference.

### Evaluation Order

The recommended evaluation order for `classify_doc_type()`:

```
1. Title patterns (DOC_TYPE_PATTERNS)   — existing, highest precision
2. Filename suffix mapping               — new; applied only when title returns ''
3. Unresolved                            — doc_code remains ''
```

Title patterns take precedence because the same filename suffix can map to different doc types in different packages (e.g. `_ig` on `psb_3_p47_pss_1_p141_ig.docx` is genuinely an IG, but `_tg` sometimes appears on troubleshooting guides that the title already classifies). Using the filename as a fallback, not an override, preserves the precision of the title pass.

### Anomalies to Resolve Before Implementation

Two known filename/title mismatches require manual review:

1. **MAG `_pom` anomaly (5 docs).** Filenames end in `_pom` but titles read "Central VistA Imaging Exchange (CVIX) Administrator's Guide". The title correctly describes an Administrator's Guide (`AG` under the `_ag` mapping); the `_pom` suffix appears to be a VDL cataloguing error. These should be assigned `AG`, not `POM`.

2. **GMRC `_rn` anomaly (1 doc).** `GMRC*3*57 Suicide Hotline Consult Setup` has filename suffix `_rn` but the title describes a setup document. The filename appears to be a VDL mislabelling. The correct code is likely `IG`.

### Comprehensive Suffix → doc_code Mapping Table

This table covers all suffixes observed in the unlabelled inventory. Suffixes in the **Implemented** column are ready to add. Suffixes marked **Needs title disambiguation** require a title sub-pass before mapping.

| Filename suffix | `doc_code` | `doc_label` | Unique docs resolved | Notes |
|---|---|---|---|---|
| `_pom` | `POM` | Production Operations Manual | 32 | Excludes 5 MAG docs (title/filename mismatch — assign `TG` manually) |
| `_tg` | `TG` | Technical Guide | 7 | Troubleshooting guides, startup guides |
| `_dg` | `DG` | Developer Guide | 8 | Developer's guides |
| `_ag` | `AG` | Administrator's Guide | 6 | Administrator's guides |
| `_wf` | `WF` | Workflow Guide | 11 | CAPRI workflow documents |
| `_kda` | `SUP` | Supplement | 7 | VBECS Known Defects and Anomalies |
| `_sp` | `SUP` | Supplement | 1 | Lock Manager Supplement |
| `_sm` | `SM` | Site Manual / Systems Management Guide | 4 | Site Manual, Systems Management Guide |
| `_puse` | `UG` | User Guide | 1 | Ambulatory Care Reporting Menu (patient use) |
| `_adpac` | `UG` | Manager/ADPAC Guide | 1 | NOIS Application Coordinator training |
| `_clerk` | `UG` | User Guide | 4 | IFCAP role-specific Clerk guides |
| `_coord` | `UG` | User Guide | 1 | IFCAP Application Coordinator guide |
| `_orders` | `UG` | User Guide | 1 | IFCAP Delivery Order guide |
| `_card` | `UG` | User Guide | 1 | IFCAP Purchase Card guide |
| `_agent` | `UG` | User Guide | 1 | IFCAP Purchasing Agent guide |
| `_tech` | `UG` | User Guide | 1 | IFCAP Accounting Technician guide |
| `_analyst` | `UG` | User Guide | 2 | IFCAP Budget/Requirements Analyst guides |
| `_irms` | `UG` | User Guide | 1 | NOIS Information Resource Manager training |
| `_ug` | `UG` | User Guide | 1 | ECX User's Guide |
| `_ig` | `IG` | Installation Guide | 5 | BCMA, PXRM, LR, MPIF, XOBW installation guides |
| `_dibrg` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 2 | PSO and TMP DIBRG |
| `_dibr` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 1 | TMP DIBR |
| `_bckout` | `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 2 | KAAJEE Rollback Instructions |
| `_rn` | `RN` | Release Notes | 4 | Excludes 1 GMRC mislabelled doc (assign `IG` manually) |
| `_readme` | `RN` | Release Notes | 3 | KAAJEE and XU ReadMe files |
| `_notes` | `RN` | Release Notes | 1 | VIAB DIBRO notes |
| `_tm` | `TM` | Technical Manual | 2 | QUASAR, TMP |
| `_sg` | `SG` | Security Guide | 1 | BCMA backup security guide |
| `_qr` | `QRG` | Quick Reference Guide | 1 | XU Quick Reference Guide |
| `_tut` | `TRG` | Training Guide | 1 | FM ScreenMan Tutorial |
| `_tutorial` | `TRG` | Training Guide | 2 | FM Key and Index Tutorial, VA FileMan DDE Tutorial |
| `_addendum` | `UG` | User Guide | 13 | SD VSE GUI User Guide Addenda (all 13 are addenda to a UG) |
| `_manual` | `UM` | User Manual | 3 | RAI/MDS, IFCAP Point of Use, RTLS Manual |
| `_ddd` | `SUP` | Supplement | 2 | ECX Data Definitions Documents |
| `_glossary` | `SUP` | Supplement | 1 | EDIS Glossary |
| `_guide` | — | (needs title sub-pass) | 10 | Mixed types: Set Up Guide→`IG`, Developer Guide→`TG`, Troubleshooting Guide→`SUP`, Quick Start Guide→`QRG`, Admin Guide→`TG`. Do not map blindly. |
| `_binder` | — | (needs title sub-pass) | 2 | Kernel Developer's Guide: Binder→`TG`; Systems Management: Binder→`UG` |

**Total unambiguously resolvable by filename suffix: ~124 unique documents**

### Suffixes With No Clear Mapping (Irreducible by Suffix Alone)

| Filename suffix | Docs | Example title | Disposition |
|---|---|---|---|
| `_cds` | 1 | `PXRM*2*54 Using The Ebola Risk Triage Tool Template` | Clinical Decision Support — no standard VDL code; manual review |
| `_ddd` | 2 | DSS Data Definitions Documents | Mapped to `SUP` above |
| `_bank` | 1 | LR `003: Invalid 'C' Cross-Ref` | Lab procedure series; no standard suffix mapping |
| `_me` | 1 | `Note regarding the decommissioning of ICR 2.1` | Administrative notice; no standard code |
| `_vdl` | 1 | `Test Document VDL` | Test/placeholder document; exclude |
| `_plan` | 1 | `MHV*1*24 Emergency Patch Instructions` | Emergency patch instructions; possibly `IG` |
| `_pm` | 1 | `Fee Basis Annual Patch Manual` | Patch manual; possibly `IG` |

---

## 6. Irreducible Hard Cases (~148 unique docs after all fixes)

After applying both the title-pattern fixes (§4) and the filename-suffix classification (§5), approximately **148 unique documents** are expected to remain unlabelled. These fall into four permanent categories:

### Category A — Purely descriptive patch titles (~40 docs)
Patch-layer documents whose titles describe the content rather than the document type. No standard VA doc-type keyword is present in either the title or the filename.

Examples: `MD*1*72 CliO Terminology Dictionary`, `PXRM*2*54 Using The Ebola Risk Triage Tool Template`, `PSS*1*127 Pharmacy Data Management Drug Exception List`

**Disposition:** Manual labelling or accept `doc_code = ''` for patch-layer documents where the title is the complete description.

### Category B — Numbered lab procedure documents (~10 docs)
LR package documents numbered `001:`, `002:`, `003:` — a unique series with no VA doc-type vocabulary match.

Examples: `001: Not Performed/Multiple Specimens/Incomplete Data Entry`, `002: Antibody Lookup`

**Disposition:** Add a pattern `r'^\d{3}:'` → `SUP` (Supplement) in `DOC_TYPE_PATTERNS` to cover the entire series with one rule.

### Category C — Specialist operational documents (~20 docs)
Documents using VA-internal terminology that has no standard doc-type label: memoranda, retirement notices, workflow scenarios, startup/troubleshooting procedures that span multiple doc types.

Examples: `eHMP Integration Control Registrations (ICRs) Status: Memorandum for Record`, `PCMM Mass Discharge Scenarios`, `Retiring Pharmacy Prescription Practices Message`

**Disposition:** Accept `doc_code = ''`; these are genuinely outside the standard taxonomy.

### Category D — Non-VistA apps with idiosyncratic naming (~78 docs)
JLV, CAPRI, VBECS, KAAJEE, NOIS, PPS-N, TMP, NUMI, XOBV, DHT, XWB documents whose titles and filenames use neither the standard VDL vocabulary nor the VA filename-suffix convention. Mostly resolvable only by reading the document content.

Examples: All remaining JLV POM docs (already resolved by `_pom`), remaining CAPRI workflow docs (already resolved by `_wf`), remaining KAAJEE and TMP docs with non-standard naming.

**Disposition:** The `_pom` and `_wf` filename-suffix fixes will clear most of these. The residual ~78 docs require either manual review or content-based classification.

---

## 7. Impact on the Corpus

Of the 272 unique currently-unlabelled documents, the missing `doc_code` does not prevent a document from being fetched, ingested, or enriched — it only means the document appears as `doc_type: unknown` in its frontmatter and in the survey output. Downstream effects:

- **Portal navigation:** unlabelled documents appear in the "Uncategorized" nav section rather than under their correct doc type
- **Consolidation:** the `select_master` function in `consolidate.py` cannot distinguish an unlabelled User Manual from an unlabelled Technical Manual — both are treated as equal rank within their `doc_layer`
- **Survey counts:** the `unknown` entries in the survey summary (`doc_type distribution`) are a subset of these 272 documents — specifically those that were fetched and ingested but whose `classify()` call in `rules.py` also returned `UNKNOWN`

After implementing the filename-suffix strategy, the projected ~148 remaining unknowns represent **5.1% of all 2,874 corpus documents** — an acceptable residual for a corpus of this size and age, given that many are genuinely outside the standard taxonomy.
