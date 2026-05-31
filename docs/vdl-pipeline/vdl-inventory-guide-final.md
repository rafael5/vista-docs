# VA VistA Documentation Library — Inventory Reference Guide

**Version:** 2.0
**Date:** 2026-03-30
**Source data:** `~/data/vista-docs/inventory/vdl_inventory_enriched.csv`
**Corpus:** `~/data/vista-docs/markdown/` (2,240 documents, 44 packages)

---

## Table of Contents

1. [Scope and Purpose](#1-scope-and-purpose)
2. [What the VDL Contains](#2-what-the-vdl-contains)
   - [Application Status](#application-status)
   - [Document Types](#document-types)
   - [Document Layers](#document-layers)
   - [Document Format](#document-format)
3. [Inventory Summary Statistics](#3-inventory-summary-statistics)
   - [Full Table Dimensions](#full-table-dimensions)
   - [Corpus Dimensions](#corpus-dimensions-downloaded-and-processed-documents)
4. [Classification Scheme](#4-classification-scheme)
   - 4.1 [system_type — System Classification](#41-system_type--system-classification)
     - [Full Distribution](#full-distribution)
     - [VistA vs. Non-VistA Summary](#vista-vs-non-vista-summary)
     - [Category Definitions](#category-definitions)
   - 4.2 [noise_type — Document-Level Noise](#42-noise_type--document-level-noise)
   - 4.3 [cots_dependent — Commercial Dependencies](#43-cots_dependent--commercial-dependencies)
5. [The VistA Working Definition](#5-the-vista-working-definition)
   - [The KIDS Test](#the-kids-test)
   - [What Is NOT VistA](#what-is-not-vista)
   - [Why Hybrid Categories Are Necessary](#why-hybrid-categories-are-necessary)
   - [A Note on HL7](#a-note-on-hl7)
   - [A Note on MUMPS Namespace Assignments](#a-note-on-mumps-namespace-assignments)
6. [Column Reference](#6-column-reference)
   - [Group 1: Application Identity (cols 1–5)](#group-1-application-identity-cols-15)
   - [Group 2: Classification (cols 6–7)](#group-2-classification-cols-67)
   - [Group 3: Package Identity (cols 8–16)](#group-3-package-identity-cols-816)
   - [Group 4: Document Metadata (cols 17–26)](#group-4-document-metadata-cols-1726)
   - [Group 5: URLs (cols 27–29)](#group-5-urls-cols-2729)
7. [Related Reports](#7-related-reports)

---

## 1. Scope and Purpose
[↑ Table of Contents](#table-of-contents)

The **VA VistA Documentation Library (VDL)** is the official public repository of technical documentation for VistA — the Veterans Health Administration's electronic health record system — and for related VA software, services, and systems. It is published at `va.gov/vdl` and is maintained by the Department of Veterans Affairs.

This guide documents the structure, content, and classification of the VDL inventory as captured and analyzed in the `vdl_inventory_enriched.csv` table. That table is the authoritative artifact of a systematic, AI-driven analysis of the complete VDL catalog and every document within it.

The inventory covers:
- Every application listed in the VDL as of the crawl date
- Every document listed under each application
- Enriched metadata derived from downloading, converting, and reading each document

**This guide is the definitive reference for:**
- Understanding what the VDL does and does not contain
- The classification scheme used to distinguish VistA packages from non-VistA systems
- The meaning and provenance of every column in the enriched inventory table

For pipeline design, implementation, lessons learned, and methodology, see the [Related Reports](#7-related-reports).

---

## 2. What the VDL Contains
[↑ Table of Contents](#table-of-contents)

The VDL organizes its content into five sections:

| Section Code | Section Name | Apps | Rows |
|---|---|---|---|
| CLI | Clinical | 99 | 5,790 |
| FIN | Financial-Administrative | 38 | 1,485 |
| INF | Infrastructure | 37 | 777 |
| GUI | VistA/GUI Hybrids (formerly HealtheVet) | 23 | 780 |
| MON | Monograph | 1 | 2 |
| | **TOTAL** | **196** | **8,834** |

The **Clinical** section is by far the largest, encompassing all patient care packages — laboratory, pharmacy, radiology, surgery, nursing, clinical documentation, registries, and clinical decision support.

**Financial-Administrative** covers billing (Integrated Billing, Accounts Receivable, Fee Basis), HR/payroll (PAID), engineering, and quality management.

**Infrastructure** covers the Kernel platform (XU), VA FileMan (DI), MailMan (XM), HL7 messaging, RPC Broker, and the integration middleware layer.

**VistA/GUI Hybrids** is a legacy section label. It was originally created for web and client applications but now contains a heterogeneous mix of national VA services, web portals, and middleware.

**Monograph** contains a single entry — the VistA Monograph — which is a catalog of all VistA packages, not a package itself.

### Application Status

Of the 196 unique applications in the VDL:

| Status | Apps |
|---|---|
| Active | 172 (88%) |
| Decommissioned | 15 (8%) |
| Archive | 9 (5%) |

Decommissioned and archived applications remain in the VDL for historical reference. Their documentation is retained but no longer updated.

### Document Types

The VDL assigns every document a `doc_code` and a `doc_label`. It does **not** assign a `doc_layer`. That field is a derived heuristic added during the enrichment stage of this pipeline.

#### The `doc_layer` heuristic

**The problem.** The VDL presents each application's documents as a flat, undifferentiated list. A Technical Manual for PSO Version 7 and a Technical Manual patch supplement for `PSJ*5*381` sit side by side in the same table with no structural distinction. For the pipeline to serve documents to readers usefully — and to select a single canonical document when multiple versions of the same type exist — the flat list had to be stratified into documentation tiers.

**What the VDL title encodes.** VistA document titles are not free-form. They follow two conventions that encode the structural role of the document directly in the title:

1. **Patch-level titles** contain a KIDS patch identifier in `NS*V*P` format as a prefix, e.g. `DG*5.3*1057 Deployment, Installation, Back-Out, and Rollback Guide`. The namespace (`DG`), version (`5.3`), and patch number (`1057`) are machine-parseable.

2. **Version-level titles** contain a version phrase but no patch number, e.g. `Pharmacy Patient Safety Journal (PSJ) Version 5 Technical Manual` or `PIMS Version 5.3 ADT Technical Manual`. These describe the entire package at a version, not a specific patch.

3. **Plain titles** contain neither a parseable version nor a patch number, e.g. `PSO Technical Manual` or `Nursing User Manual`. These are the oldest documents in the corpus, predating the version-in-title convention.

**The rules.** For each row, the enrichment script attempts to extract `patch_ver` (a version string) and `patch_num` (a patch sequence number) from the document title and filename. The layer is then assigned deterministically:

| Condition | `doc_layer` | Rationale |
|---|---|---|
| `patch_ver` present AND `patch_num` absent | `anchor` | Has a version designation but no patch number — canonical reference document for that version |
| `patch_num` present (with or without version) | `patch` | Names a specific KIDS patch — patch-level supplement or update |
| Neither `patch_ver` nor `patch_num` present | `plain` | No parseable version or patch signal — version-ambiguous document |

**Where the heuristic is imperfect.** The `plain` tier is a residual category: it captures every document whose title did not yield a version or patch number. It includes genuinely versionless documents (cross-cutting guides, glossaries), very old documents that predate version-in-title conventions, and documents whose titles were too idiosyncratic for the parser to extract version information. The 741 unlabelled rows (no `doc_code`) are overwhelmingly `plain`, reflecting the same parsing gap.

| `doc_code` | `doc_label` | patch | plain | anchor | total |
|---|---|---|---|---|---|
| `RN` | Release Notes | 951 | 299 | 308 | 1,558 |
| `DIBR` | Deployment, Installation, Back-Out, and Rollback Guide | 863 | 186 | 257 | 1,306 |
| `FORM` | VBA Form *(noise)* | — | 1,192 | — | 1,192 |
| `UM` | User Manual / Clinical Coordinator Manual | 400 | 265 | 206 | 871 |
| `UG` | User Guide / Manager/ADPAC Guide | 104 | 247 | 453 | 804 |
| `IG` | Installation Guide | 456 | 191 | 132 | 779 |
| *(empty)* | *(unlabelled)* | 179 | 347 | 215 | 741 |
| `TM` | Technical Manual | 206 | 324 | 177 | 707 |
| `CRU` | Clinical Reminder Update | 282 | — | 54 | 336 |
| `VDD` | Version Description Document | 2 | 143 | — | 145 |
| `IG-IMP` | Implementation Guide | 38 | 24 | 26 | 88 |
| `POM` | Production Operations Manual | 10 | 10 | 46 | 66 |
| `SG-SET` | Setup Guide | 26 | 14 | 14 | 54 |
| `SG` | Security Guide | 10 | 26 | 8 | 44 |
| `INT` | Interface Specification / Interface Feed Guide | 18 | 12 | 6 | 36 |
| `CFG` | Configuration Guide / Setup and Configuration Guide | 14 | — | 2 | 16 |
| `API` | API Manual | 2 | 16 | — | 18 |
| `QRG` | Quick Reference Guide | 4 | 12 | 2 | 18 |
| `TG` | Technical Guide | 9 | 6 | — | 15 |
| `TRG` | Training Guide | 2 | 6 | 2 | 10 |
| `REF` | Reference / Interface Toolkit | — | 6 | 2 | 8 |
| `PDD` | Patch Description Document | 6 | 2 | — | 8 |
| `APX` | Appendix | — | 2 | 2 | 4 |
| `FAQ` | Frequently Asked Questions | — | — | 4 | 4 |
| `DESC` | Description Document | — | 2 | 2 | 4 |
| `CVG` | Conversion Guide | 2 | — | — | 2 |
| | **Total** | **3,584** | **3,332** | **1,918** | **8,834** |

Notes: `RN` and `DIBR` dominate because they are issued per KIDS patch and many packages have hundreds of patches. `FORM` rows are the `vba_form` noise type — the same 8 VA benefit forms attached to every application. The 741 unlabelled rows have no `doc_code` assigned in the VDL.

### Document Layers

| Layer | Count | Meaning |
|---|---|---|
| `patch` | 3,584 | Documents a specific patch (e.g., `OR*3.0*500`) |
| `plain` | 1,991 | Version-level document with no specific patch reference |
| `anchor` | 1,918 | Canonical version document (e.g., `PSO Version 7 Technical Manual`) |

### Document Format

| Format | Substantive Docs |
|---|---|
| PDF | 3,756 |
| DOCX | 3,730 |
| DOC (legacy) | 7 |

The VDL has migrated largely to PDF for recent patches, with DOCX used for older and editable materials.

---

## 3. Inventory Summary Statistics
[↑ Table of Contents](#table-of-contents)

### Full Table Dimensions

| Metric | Value |
|---|---|
| Total rows | 8,834 |
| Unique applications | 196 |
| Substantive document rows | 7,493 |
| Noise rows (boilerplate, forms) | 1,341 |
| Total columns | 29 |

### Corpus Dimensions (Downloaded and Processed Documents)

| Metric | Value |
|---|---|
| Markdown files produced | 2,240 |
| Package directories | 44 |
| Files with extracted metadata | 2,240 (100%) |
| Files with word count | 2,220 |
| Total words across corpus | 14,881,751 |
| Mean words per document | 6,703 |
| Largest single document | 180,233 words |
| Files with page count | 1,897 |
| Total equivalent pages | 85,308 |
| Mean pages per document | 45 |
| Largest single document | 3,802 pages |

The 14.9 million words across 2,240 documents represents the complete body of VistA technical documentation available through the VDL for the 44 packages processed.

---

## 4. Classification Scheme
[↑ Table of Contents](#table-of-contents)

### 4.1 `system_type` — System Classification

The `system_type` column classifies every application in the VDL according to what kind of system it is. This classification is the primary analytical contribution of this project: the VDL itself does not distinguish VistA packages from non-VistA systems.

The classification scheme has 11 values organized around a single working definition (see Section 5).

#### Full Distribution

| system_type | Apps | % of Apps | Rows | % of Rows |
|---|---|---|---|---|
| VistA | 127 | 65% | 6,014 | 68% |
| VistA + GUI | 2 | 1% | 316 | 4% |
| VistA + COTS | 3 | 2% | 309 | 3% |
| VistA + middleware | 1 | 1% | 35 | 0% |
| Web client | 20 | 10% | 896 | 10% |
| Integration middleware | 10 | 5% | 361 | 4% |
| VA enterprise service | 23 | 12% | 578 | 7% |
| VBA system | 1 | 1% | 144 | 2% |
| COTS product | 3 | 2% | 102 | 1% |
| Data patch | 4 | 2% | 64 | 1% |
| Program documentation | 2 | 1% | 15 | 0% |
| **TOTAL** | **196** | | **8,834** | |

#### VistA vs. Non-VistA Summary

| | Apps | % | Rows | % |
|---|---|---|---|---|
| VistA (all four VistA categories) | 133 | 68% | 6,674 | 76% |
| Non-VistA | 63 | 32% | 2,160 | 24% |

#### Category Definitions

**`VistA`** — A MUMPS/M-language package deployed to VA server nodes via the Kernel Installation and Distribution System (KIDS). Runs as server-side M code. This is the canonical VistA package. 127 apps, 65% of the catalog.

**`VistA + GUI`** — The VDL bundles a KIDS-deployed MUMPS server package and a dedicated GUI client application under a single catalog entry. The MUMPS server side IS VistA; the GUI client is not.

| App | MUMPS side | GUI side |
|---|---|---|
| CPRS | OR\*3.0 Orders/CPRS server | Delphi Windows GUI client |
| MAG | MAG\* imaging server (index, routing) | Windows VistA Imaging workstation (C++) |

**`VistA + COTS`** — The VDL bundles a MUMPS integration/adapter layer and a COTS system under a single entry.

| App | MUMPS side | COTS side |
|---|---|---|
| MD | MD\* clinical device bridge (HL7) | COTS bedside monitors, EKG, Holter devices |
| YS | YS\*5.01 legacy mental health package | Netsmart Mental Health Suite |
| ROI | DSIR\* release-of-information module | COTS ROI vendor system (Ciox / DSSI) |

**`VistA + middleware`** — The VDL bundles a KIDS-deployed MUMPS component and a non-VistA connector/adapter layer.

| App | MUMPS side | Connector side |
|---|---|---|
| XOBV | M-side RPC listener (KIDS-deployed, XWB namespace) | J2EE WebLogic connector (VistALink) |

**`Web client`** — A web or mobile application that accesses VistA data. No MUMPS server component of its own. 20 apps including CPRS-related viewers, patient portals (My HealtheVet), pharmacy systems (PECS, PRED, PPS-N), and scheduling applications.

**`Integration middleware`** — An adapter or bridge between VistA and external systems. No clinical or administrative functionality of its own. 10 apps including VistALink (XOBV), KAAJEE, VistA Integration Adapter (VIAB), MOCHA drug-check server (PREM), and HL7 routing middleware (AFJX).

**`VA enterprise service`** — A separate national VA platform, API layer, or enterprise service that VistA interfaces with but does not contain. 23 apps including Master Person Index (MPI), Health Data Repository (HDR), Nationwide Health Information Network (NHIN), and VA Lighthouse API platform (LHS).

**`VBA system`** — A Veterans Benefits Administration tool or client. 1 app: CAPRI (Compensation and Pension Record Interchange). The VistA-side AMIE package (DVBA) is classified separately as `VistA`.

**`COTS product`** — Commercial off-the-shelf software with no VistA MUMPS component. 3 apps:

| App | Product |
|---|---|
| BMS | TeleTracking bed management platform |
| CRMS | Salesforce customer relationship management |
| VPS | Commercial point-of-service kiosk hardware/software |

**`Data patch`** — A KIDS build whose payload is reference data or licensed terminology, not executable M routines.

| App | Content |
|---|---|
| CPT | AMA Current Procedural Terminology code set |
| ICD | WHO/CMS ICD-9/10-CM diagnostic code set |
| DRG | 3M Diagnosis-Related Group grouper and weight tables |
| LEX | NLM/SNOMED clinical terminology reference data (Lexicon Utility) |

**`Program documentation`** — Documents a VA program or initiative, not a software package.

| App | Content |
|---|---|
| EHM | Electronic Health Modernization (Oracle Cerner EHRM) program documentation |
| MON | VistA Monograph — a catalog of VistA packages |

---

### 4.2 `noise_type` — Document-Level Noise

The VDL attaches a set of boilerplate documents to every application section regardless of relevance. These are identified by `noise_type` and excluded from substantive analysis.

| noise_type | Rows | % of Total | Content |
|---|---|---|---|
| *(empty — substantive)* | 7,493 | 84.8% | Real technical documentation |
| `vba_form` | 1,192 | 13.5% | VA benefits and claims forms |
| `va_ref` | 149 | 1.7% | VA Strategic Plan FY 2014–2020 |

The 8 VBA forms and 1 strategic plan appear under all 149 active applications during the crawl period, producing 1,341 noise rows. Filtering on `noise_type = ''` isolates the 7,493 substantive document rows.

**Applications where every document is noise (no substantive VDL documentation):**

ICD, E3R, HL, MJCF, ONCO, RUM, SAGG, SSO/UC, XOB, KDC, MDWS, CRMS, HDR, ROI, SAMH, VODA, WEBD, WEBHR

---

### 4.3 `cots_dependent` — Commercial Dependencies

The `cots_dependent` column identifies any application whose function requires a specific licensed commercial product. It is set regardless of `system_type`.

| App | system_type | Commercial Dependency |
|---|---|---|
| MD | VistA + COTS | COTS clinical device systems (EKG/Holter/bedside monitors) |
| YS | VistA + COTS | Netsmart Mental Health Suite (treatment planning / DSIU) |
| ROI | VistA + COTS | COTS ROI vendor system (Ciox / DSSI) |
| CPT | Data patch | AMA CPT code set (commercial license required) |
| DRG | Data patch | 3M DRG Grouper (commercial classification algorithm + weight tables) |
| PREM | Integration middleware | First Databank drug interaction service (MOCHA dosing checks) |

ICD is not flagged because ICD codes are WHO- and CMS-published and available to the VA without a commercial license. LEX draws from NLM/SNOMED which is also publicly available to US government users.

---

## 5. The VistA Working Definition
[↑ Table of Contents](#table-of-contents)

A precise working definition of VistA is necessary because the VDL mixes VistA packages with GUI clients, web applications, national enterprise services, COTS products, and data standards — all listed side by side without distinction.

**VistA (Veterans Information Systems Technology and Architecture)** is the integrated application-database server that provides clinical, business, and platform services to support operations of all VHA medical centers nationwide.

> **VistA is an integrated application-database platform comprised exclusively of MUMPS (M) technology, with all M applications integrated via M infrastructure to a single shared M database.**

### The KIDS Test

*Is an application an M package, versioned and distributed by the VistA M packaging system (KIDS), running on the M-based VistA application-database server?* If yes, it is VistA. If no — regardless of whether it connects to VistA, integrates with VistA, or is documented in the VDL — it is not VistA.

### What Is NOT VistA

| Category | Definition | Examples |
|---|---|---|
| GUI client | Delphi/Windows desktop application connecting to VistA via RPC | CPRS GUI |
| Web client | Web or mobile application accessing VistA data via API or RPC | JLV, My HealtheVet, WEBP, MBAA |
| Integration middleware | Adapter between VistA and external systems | VistALink (XOBV), KAAJEE, VIA (VIAB), MDWS |
| VA enterprise service | Separate national VA platform or API layer | MPI, HDR, NHIN, Lighthouse (LHS) |
| VBA system | Veterans Benefits Administration tool | CAPRI |
| COTS product | Commercial software with no VistA MUMPS component | BMS, CRMS, VPS |
| Data patch | KIDS build whose payload is reference data, not M routines | CPT, ICD, DRG, LEX |
| Program documentation | Documents a program, not a software package | EHM, MON |

### Why Hybrid Categories Are Necessary

Three patterns in the VDL create genuine classification ambiguity: the VDL bundles a VistA M component and a non-VistA component under a single application entry:

- **`VistA + GUI`**: MUMPS server + GUI client co-documented (CPRS, MAG)
- **`VistA + COTS`**: MUMPS integration layer + COTS system co-documented (MD, YS, ROI)
- **`VistA + middleware`**: MUMPS M listener + non-VistA connector co-documented (XOBV)

In each hybrid case, the MUMPS side passes the KIDS test and IS VistA; the non-MUMPS side does not.

### A Note on HL7

HL7 messaging is used pervasively within VistA as an intra-package communication mechanism. HL7 is therefore not a discriminator between VistA and non-VistA systems — it is part of VistA's internal architecture.

### A Note on MUMPS Namespace Assignments

The VDL assigns a `pkg_ns` to some non-VistA applications for catalog tracking purposes. The presence of a namespace does not imply the existence of a MUMPS package. Examples: MED uses `pkg_ns=TIU` because it calls TIU; PECS uses `pkg_ns=PECS` as a tracking code with no M codebase. Classification is based on actual architecture documented in technical manuals, not on namespace assignment.

---

## 6. Column Reference
[↑ Table of Contents](#table-of-contents)

The enriched inventory table has 29 columns organized into five groups.

### Group 1: Application Identity (cols 1–5)

| Column | Type | Description |
|---|---|---|
| `section_name` | string | VDL section full name (Clinical, Financial-Administrative, Infrastructure, VistA/GUI Hybrids, Monograph) |
| `section_code` | string | VDL section code (CLI, FIN, INF, GUI, MON) |
| `app_name_full` | string | Full application name as listed in the VDL |
| `app_name_abbrev` | string | Short application code — primary identifier throughout the pipeline |
| `app_status` | string | `active`, `archive`, or `decommissioned` |

### Group 2: Classification (cols 6–7)

| Column | Type | Description |
|---|---|---|
| `system_type` | string | System classification (11 values; see Section 4.1). Not yet present in current CSV export — will be added in a future pipeline run. |
| `cots_dependent` | string | Named commercial dependency, or empty if none (see Section 4.3) |

### Group 3: Package Identity (cols 8–16)

| Column | Type | Description |
|---|---|---|
| `decommission_date` | string | Date of decommission, if applicable |
| `pkg_ns` | string | Primary MUMPS namespace prefix (e.g., `OR`, `DG`, `PSO`). May be a phantom tracking code for non-VistA apps. |
| `patch_ver` | string | Full version string parsed from the patch identifier |
| `patch_ver_major` | string | Major version component |
| `patch_ver_minor` | string | Minor version component |
| `patch_num` | string | Patch sequence number |
| `patch_id` | string | Structured patch identifier (e.g., `OR*3.0*500`) |
| `patch_id_full` | string | Full patch identifier including multi-patch notation |
| `multi_ns` | flag | Set when a document covers multiple MUMPS namespaces |
| `group_key` | string | Grouping key for multi-patch installation sets |

### Group 4: Document Metadata (cols 17–26)

| Column | Type | Description |
|---|---|---|
| `doc_code` | string | VDL document type code |
| `doc_label` | string | Human-readable document type (Release Notes, Technical Manual, etc.) |
| `doc_layer` | string | Documentation tier: `patch`, `anchor`, or `plain` |
| `doc_title` | string | Full document title as listed in the VDL |
| `doc_filename` | string | Source filename |
| `doc_slug` | string | URL slug |
| `doc_format` | string | File format: `pdf`, `docx`, `doc` |
| `doc_subject` | string | Subject/version string from VDL metadata |
| `noise_type` | string | `vba_form`, `va_ref`, or empty for substantive documents (see Section 4.2) |

### Group 5: URLs (cols 27–29)

| Column | Description |
|---|---|
| `app_url` | VDL application page URL |
| `doc_url` | Direct document download URL |
| `companion_url` | Companion document URL (alternate format) |

---

## 7. Related Reports
[↑ Table of Contents](#table-of-contents)

The pipeline design, implementation, and full technical methodology are documented in a set of companion reports:

| Report | Contents |
|---|---|
| [`vdl-0-overview.md`](vdl-0-overview.md) | End-to-end pipeline overview; design principles (TDD, modular, idempotent, portable); completeness and determinism criteria |
| [`vdl-1-crawl.md`](vdl-1-crawl.md) | VDL catalog extraction — structure, parser design, output |
| [`vdl-2-inventory.md`](vdl-2-inventory.md) | Inventory normalization and enrichment — all eight passes |
| [`vdl-3-fetch.md`](vdl-3-fetch.md) | Document download — design, rate limiting, state tracking, lessons learned |
| [`vdl-4-ingest.md`](vdl-4-ingest.md) | Document conversion to markdown — Docling, post-processing, lessons learned |
| [`vdl-5-enrich.md`](vdl-5-enrich.md) | Metadata extraction — all seven enrichment cycles, methodology, tools |
| [`vdl-6-system-classification.md`](vdl-6-system-classification.md) | System classification — three passes, all 196 applications |

---

*End of guide.*
