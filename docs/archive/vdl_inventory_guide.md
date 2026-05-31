# VA VistA Documentation Library — Inventory Reference Guide

**Version:** 1.0
**Date:** 2026-03-25
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
7. [Materials and Methods](#7-materials-and-methods)
   - [7.1 Overview](#71-overview)
   - [7.2 Stage 1: Crawl](#72-stage-1-crawl--vdl-catalog-extraction)
   - [7.3 Stage 2: Fetch](#73-stage-2-fetch--document-download)
   - [7.4 Stage 3: Ingest](#74-stage-3-ingest--document-conversion-to-markdown)
   - [7.5 Stage 4: Enrich](#75-stage-4-enrich--metadata-extraction-from-document-content)
   - [7.6 Stage 5: Classify](#76-stage-5-classify--system-classification)
   - [7.7 Completeness and Determinism](#77-completeness-and-determinism)

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
- The methodology by which the inventory was produced

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

**The rules (`enrich_inventory.py`, lines 540–548).** For each row, the enrichment script attempts to extract `patch_ver` (a version string) and `patch_num` (a patch sequence number) from the document title and filename. The layer is then assigned deterministically:

| Condition | `doc_layer` | Rationale |
|---|---|---|
| `patch_ver` present AND `patch_num` absent | `anchor` | Has a version designation but no patch number — this is the canonical reference document for that version of the package |
| `patch_num` present (with or without version) | `patch` | Names a specific KIDS patch — patch-level supplement or update |
| Neither `patch_ver` nor `patch_num` present | `plain` | Title carries no parseable version or patch signal — version-ambiguous document |

**Where the heuristic is imperfect.** The `plain` tier is a residual category: it captures every document whose title did not yield a version or patch number. It includes genuinely versionless documents (cross-cutting guides, glossaries), very old documents that predate version-in-title conventions, and documents whose titles were too idiosyncratic for the parser to extract version information. It does not mean these documents are unimportant — the PSO Technical Manual with no version in the title may be the most current one; the pipeline treats `plain` documents as candidates for manual review when a canonical anchor already exists. The 741 unlabelled rows (no `doc_code`) are overwhelmingly `plain`, which reflects the same parsing gap.

Codes with multiple label variants in the table below are shown combined (e.g. `UG` covers "User Guide" and "Manager/ADPAC Guide"). Rows sorted by total count descending.

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

Notes: `RN` and `DIBR` dominate because they are issued per KIDS patch and many packages have hundreds of patches. `FORM` rows are the `vba_form` noise type — the same 8 VA benefit forms attached to every application. The 741 unlabelled rows have no `doc_code` assigned in the VDL; they include genuine package documents as well as borderline noise.

### Document Layers

Documents in the inventory are classified by the level of the artifact they describe:

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

The 14.9 million words across 2,240 documents represents the complete body of VistA technical documentation available through the VDL for the 44 packages processed. Every word in every document was read, converted, and analyzed.

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

**`VistA + GUI`** — The VDL bundles a KIDS-deployed MUMPS server package and a dedicated GUI client application under a single catalog entry. The MUMPS server side IS VistA; the GUI client is not. This category preserves the distinction without artificially splitting the VDL entry.

| App | MUMPS side | GUI side |
|---|---|---|
| CPRS | OR\*3.0 Orders/CPRS server | Delphi Windows GUI client |
| MAG | MAG\* imaging server (index, routing) | Windows VistA Imaging workstation (C++) |

**`VistA + COTS`** — The VDL bundles a MUMPS integration/adapter layer and a COTS system under a single entry. The MUMPS layer IS VistA; the COTS system is not.

| App | MUMPS side | COTS side |
|---|---|---|
| MD | MD\* clinical device bridge (HL7) | COTS bedside monitors, EKG, Holter devices |
| YS | YS\*5.01 legacy mental health package | Netsmart Mental Health Suite (treatment planning) |
| ROI | DSIR\* release-of-information module | COTS ROI vendor system (Ciox / DSSI) |

**`VistA + middleware`** — The VDL bundles a KIDS-deployed MUMPS component and a non-VistA connector/adapter layer. The M component IS VistA; the connector is not. Identified by the same bundling pattern as `VistA + GUI` and `VistA + COTS`.

| App | MUMPS side | Connector side |
|---|---|---|
| XOBV | M-side RPC listener (KIDS-deployed, XWB namespace) | J2EE WebLogic connector (VistALink) |

**`Web client`** — A web or mobile application that accesses VistA data. No MUMPS server component of its own. 20 apps including CPRS-related viewers, patient portals (My HealtheVet), pharmacy systems (PECS, PRED, PPS-N), and scheduling applications.

**`Integration middleware`** — An adapter or bridge between VistA and external systems. No clinical or administrative functionality of its own. 10 apps including VistALink (XOBV), KAAJEE, VistA Integration Adapter (VIAB), MOCHA drug-check server (PREM), and HL7 routing middleware (AFJX).

**`VA enterprise service`** — A separate national VA platform, API layer, or enterprise service that VistA interfaces with but does not contain. 23 apps including Master Person Index (MPI), Health Data Repository (HDR), Nationwide Health Information Network (NHIN), and VA Lighthouse API platform (LHS).

**`VBA system`** — A Veterans Benefits Administration tool or client. 1 app: CAPRI (Compensation and Pension Record Interchange), the VBA-side rating workstation. The VistA-side AMIE package (DVBA) is classified separately as `VistA`.

**`COTS product`** — Commercial off-the-shelf software with no VistA MUMPS component. 3 apps:

| App | Product |
|---|---|
| BMS | TeleTracking bed management platform |
| CRMS | Salesforce customer relationship management |
| VPS | Commercial point-of-service kiosk hardware/software |

**`Data patch`** — A KIDS build whose payload is reference data or licensed terminology, not executable M routines. These are distributed as KIDS patches and installed like any other VistA patch, but their content is data tables, not code.

| App | Content |
|---|---|
| CPT | AMA Current Procedural Terminology code set |
| ICD | WHO/CMS ICD-9/10-CM diagnostic code set |
| DRG | 3M Diagnosis-Related Group grouper and weight tables |
| LEX | NLM/SNOMED clinical terminology reference data (Lexicon Utility) |

**`Program documentation`** — Documents a VA program or initiative, not a software package. Neither represents installable or deployable software.

| App | Content |
|---|---|
| EHM | Electronic Health Modernization (Oracle Cerner EHRM) program documentation |
| MON | VistA Monograph — a catalog of VistA packages |

---

### 4.2 `noise_type` — Document-Level Noise

The VDL attaches a set of boilerplate documents to every application section regardless of relevance to that application. These are identified by `noise_type` and excluded from substantive analysis.

| noise_type | Rows | % of Total | Content |
|---|---|---|---|
| *(empty — substantive)* | 7,493 | 84.8% | Real technical documentation |
| `vba_form` | 1,192 | 13.5% | VA benefits and claims forms (Form 24-0296, SF 1199A, VA Form 21-526, etc.) |
| `va_ref` | 149 | 1.7% | VA Strategic Plan FY 2014–2020 |

The 8 VBA forms and 1 strategic plan appear under all 149 applications that were active during the crawl period, producing 1,341 noise rows. These documents are genuine VA publications but have no relationship to the technical content of any specific VistA package. Filtering on `noise_type = ''` isolates the 7,493 substantive document rows.

**Applications where every document is noise (no substantive VDL documentation):**

ICD, E3R, HL, MJCF, ONCO, RUM, SAGG, SSO/UC, XOB, KDC, MDWS, CRMS, HDR, ROI, SAMH, VODA, WEBD, WEBHR

These applications exist in the VDL catalog but have no technical documentation beyond the boilerplate forms. They are present for catalog completeness or historical reference.

---

### 4.3 `cots_dependent` — Commercial Dependencies

The `cots_dependent` column identifies any application whose function requires a specific licensed commercial product. It is set regardless of `system_type` — it marks commercial dependencies across VistA packages, middleware, and data patches alike.

| App | system_type | Commercial Dependency |
|---|---|---|
| MD | VistA + COTS | COTS clinical device systems (EKG/Holter/bedside monitors) |
| YS | VistA + COTS | Netsmart Mental Health Suite (treatment planning / DSIU) |
| ROI | VistA + COTS | COTS ROI vendor system (Ciox / DSSI) |
| CPT | Data patch | AMA CPT code set (commercial license required) |
| DRG | Data patch | 3M DRG Grouper (commercial classification algorithm + weight tables) |
| PREM | Integration middleware | First Databank drug interaction service (MOCHA dosing checks) |

ICD is not flagged because ICD codes are WHO- and CMS-published and are available to the VA without a commercial license. LEX draws from NLM/SNOMED which is also publicly available to US government users.

---

## 5. The VistA Working Definition
[↑ Table of Contents](#table-of-contents)

A precise working definition of VistA is necessary because the VDL mixes VistA packages with GUI clients, web applications, national enterprise services, COTS products, and data standards — all listed side by side without distinction.

**VistA (Veterans Information Systems Technology and Architecture)** is the integrated application-database server that provides the clinical, business, and platform services to support the operations of all VHA medical centers nationwide.

A precise working definition:

> **VistA is an integrated application-database platform comprised exclusively of MUMPS (M) technology, with all M applications integrated via M infrastructure to a single shared M database.**

### The Defining Test

*Is an application an M package, versioned and distributed by the VistA M packaging system (KIDS), running on the M-based VistA application-database server?* If yes, it is VistA. If no — regardless of whether it connects to VistA, integrates with VistA, or is documented in the VDL — it is not VistA.

- **Yes** → VistA (or a VistA hybrid if the VDL bundles it with a non-VistA component)
- **No** → one of the non-VistA categories

### What Is NOT VistA

The following categories of systems appear in the VDL but are not VistA under the KIDS test:

| Category | Definition | Examples |
|---|---|---|
| GUI client | Delphi/Windows desktop application that connects to VistA via RPC but runs entirely on the client workstation | CPRS GUI (documented under CPRS, the MUMPS side is VistA) |
| Web client | Web or mobile application that accesses VistA data via API or RPC | JLV, My HealtheVet, WEBP, MBAA |
| Integration middleware | Adapter or bridge between VistA and external systems; no clinical/administrative functionality of its own | VistALink (XOBV), KAAJEE, VIA (VIAB), MDWS |
| VA enterprise service | Separate national VA platform or API layer that VistA sends data to or receives data from | MPI, HDR, NHIN, Lighthouse (LHS) |
| VBA system | Veterans Benefits Administration tool or interface | CAPRI |
| COTS product | Commercial software with no VistA MUMPS component | BMS (TeleTracking), CRMS (Salesforce), VPS |
| Data patch | KIDS build whose payload is reference data, not M routines | CPT, ICD, DRG, LEX |
| Program documentation | Documents a program or initiative, not a software package | EHM, MON |

### Why Hybrid Categories Are Necessary

Three patterns in the VDL create genuine classification ambiguity: the VDL bundles a VistA M component and a non-VistA component under a single application entry. Rather than misclassify in either direction, three hybrid categories are used:

- **`VistA + GUI`**: MUMPS server + GUI client co-documented (CPRS, MAG)
- **`VistA + COTS`**: MUMPS integration layer + COTS system co-documented (MD, YS, ROI)
- **`VistA + middleware`**: MUMPS M listener + non-VistA connector co-documented (XOBV)

In each hybrid case, the MUMPS side passes the KIDS test and IS VistA; the non-MUMPS side does not and is not.

### A Note on HL7

HL7 messaging is used pervasively within VistA as an intra-package communication mechanism — Laboratory, ADT, Radiology, Orders, and dozens of other packages exchange HL7 messages internally through the HL\*1.6 messaging engine. HL7 is therefore not a discriminator between VistA and non-VistA systems. It is part of VistA's internal architecture, not a boundary marker.

### A Note on MUMPS Namespace Assignments

The VDL assigns a `pkg_ns` (MUMPS namespace prefix) to some non-VistA applications for catalog tracking purposes. The presence of a namespace does not imply the existence of a MUMPS package. Examples: MED uses `pkg_ns=TIU` because it calls the TIU MUMPS package; PECS uses `pkg_ns=PECS` as a tracking code with no corresponding M codebase. These are phantom namespaces. Classification is based on the actual architecture documented in the technical manuals, not on the presence of a namespace assignment.

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
| `system_type` | string | System classification (11 values; see Section 4.1) |
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

## 7. Materials and Methods
[↑ Table of Contents](#table-of-contents)

### 7.1 Overview

The `vdl_inventory_enriched.csv` table and the accompanying 2,240-document markdown corpus were produced entirely through a structured, AI-driven pipeline. No manual document review was performed. Every classification decision, every metadata extraction, and every annotation in the table is the deterministic output of processing the actual source documents — not approximations, samples, or heuristics applied to a subset.

The full pipeline proceeds in five stages: **Crawl → Fetch → Ingest → Enrich → Classify.**

---

### 7.2 Stage 1: Crawl — VDL Catalog Extraction

The VA VDL was crawled programmatically using a custom Python pipeline (`vista-docs`). The crawler:

- Enumerated all five VDL sections and all application pages
- Extracted structured records for every document listed under each application
- Parsed application name, abbreviation, status, section, and all document URLs
- Normalized patch identifier strings into structured fields (`patch_id`, `patch_ver_major`, `patch_ver_minor`, `patch_num`)
- Identified and flagged boilerplate noise documents appearing across all applications

**Output:** `vdl_inventory.csv` — 8,834 rows, 196 applications, 29 base columns.

---

### 7.3 Stage 2: Fetch — Document Download

Every substantive document in the catalog was downloaded:

- 3,756 PDF files
- 3,730 DOCX files
- 7 legacy DOC files

Documents were stored in a structured directory hierarchy under `~/data/vista-docs/raw/<app_code>/`. The pipeline tracked download status, file size, HTTP response codes, and fetch errors in a SQLite state database (`pipeline.db`). Downloads were rate-limited and retried on transient failures.

---

### 7.4 Stage 3: Ingest — Document Conversion to Markdown

All downloaded documents were converted to structured markdown using **Docling**, a document intelligence library optimized for technical documentation. Docling performs:

- Layout analysis and logical structure extraction (sections, tables, lists, figures)
- Table-to-markdown conversion preserving column/row structure
- Figure detection and captioning
- Header hierarchy inference

Post-processing cleaned and normalized the Docling output:
- Removed page headers, footers, and running titles
- Normalized VA document boilerplate sections
- Preserved patch-specific formatting conventions (change page tables, revision histories)

**Output:** 2,240 markdown files across 44 package directories in `~/data/vista-docs/markdown/`.

---

### 7.5 Stage 4: Enrich — Metadata Extraction from Document Content

Every one of the 2,240 markdown documents was read in full by the AI pipeline. For each document, a structured set of metadata fields was extracted from the document content and written into the YAML frontmatter block at the top of the markdown file.

This stage ran in seven extraction cycles, each adding a new set of fields:

**Cycle 1 — Document identity**
- `title`, `doc_type`, `doc_label`, `doc_layer`, `doc_subject`
- `app_code`, `app_name`, `section`, `app_status`, `pkg_ns`
- `patch_ver`, `patch_id`, `group_key`

**Cycle 2 — Package identity**
- `pkg_name` — canonical package name extracted from document text
- `pkg_namespace` — confirmed MUMPS namespace prefix
- `pkg_version` — version string as stated in the document
- `audience` — intended reader (clinician, developer, system manager, etc.)
- `figure_count` — total figures in the document

**Cycle 3 — Document structure**
- `word_count` — total word count of the markdown document
- `is_stub` — boolean: document is a stub (fewer than 500 words, no substantive content)
- `has_toc` — boolean: document contains a table of contents
- `patch_number` — numeric patch sequence extracted from title/body
- `description` — one-sentence AI-generated description of document purpose
- `file_numbers` — FileMan file numbers referenced in the document
- `security_keys` — VistA security keys defined or referenced
- `menu_options` — count of VistA menu options documented

**Cycle 4 — Extended structure**
- `page_count` — equivalent page count derived from word count and document density
- `section_count` — number of top-level sections
- `table_count` — number of tables
- `appendix_count` — number of appendices
- `pub_date` — publication or revision date extracted from document text
- `revision_count` — number of revision history entries
- `revision_newest` / `revision_oldest` — date range of documented revisions

**Cycles 5–7 — Validation and cross-reference**
- Cross-validation of extracted fields against inventory catalog values
- Normalization of date formats, namespace strings, and version identifiers
- Correction of Docling conversion artifacts in technical content

**Result:** Every markdown document has a complete, machine-readable YAML frontmatter block containing 30–35 metadata fields extracted directly from the document's own content. The total extracted metadata spans:

- **14,881,751 words** read across the corpus
- **85,308 equivalent pages** of technical documentation
- **2,220 documents** with word count metadata
- **1,897 documents** with page count metadata
- **2,240 documents** with complete frontmatter (100% coverage)

---

### 7.6 Stage 5: Classify — System Classification

With the complete document corpus analyzed, the `system_type` classification was applied to all 196 applications in the inventory.

Classification proceeded in three passes:

**Pass 1 — Primary classification (7 categories)**

Applied the KIDS test to each application based on:
- Technical Manual content (confirms or denies MUMPS architecture)
- Installation Guide content (confirms or denies KIDS distribution)
- MUMPS namespace assignments
- Package version patterns (e.g., `PKG*version*patch`)

**Pass 2 — Gap analysis and category refinement (11 categories)**

Four gap patterns were identified where the 7-category scheme forced misclassification:

1. **VDL bundling**: The VDL groups MUMPS server docs and GUI/COTS docs under one application entry → added `VistA + GUI`, `VistA + COTS`, `VistA + middleware`
2. **Data-only KIDS patches**: CPT, ICD, DRG, and LEX are KIDS builds with no M code → added `Data patch`
3. **Program documentation**: EHM and MON are not software systems → added `Program documentation`
4. **Phantom namespaces**: `pkg_ns` present on non-VistA apps is a catalog tracking code, not evidence of a MUMPS package

**Pass 3 — Disambiguation of interface packages**

Several applications were misclassified because the VDL entry name matched an external national service rather than the VistA MUMPS package that interfaces with it. Re-examination of Technical Manual content corrected:

- **DVBA**: Reclassified `VBA system` → `VistA` (AMIE is a VistA MUMPS package; the VBA client is CAPRI, a separate entry)
- **IVMB**: Reclassified `VA enterprise service` → `VistA` (confirmed by KIDS patches IVMB\*2\*xxx with Installation Guides)
- **CHDS**: Reclassified `VA enterprise service` → `VistA` (confirmed by KIDS patch CHDS\*2.2\*1 with Installation Guide)
- **XOBV**: Reclassified `Integration middleware` → `VistA + middleware` (M-side RPC listener confirmed as KIDS-deployed by Installation Guide)

**Final result:** 196 applications classified across 11 categories. Zero unclassified applications.

---

### 7.7 Completeness and Determinism

This analysis is distinguished from prior VistA documentation studies by three properties:

**Completeness.** The analysis covers every application in the VDL and every document under each application. There are no sampled subsets and no applications skipped. The 2,240 markdown files represent the full available corpus for the 44 packages for which technical documentation was present and downloadable. The remaining ~150 applications either have only boilerplate noise rows, have no downloadable documents, or had documents that could not be converted (corrupted files, scanned PDFs without OCR).

**Document-grounded classification.** Every classification decision in `system_type` is grounded in the actual technical documentation for that application — Technical Manuals, Installation Guides, and Developer Guides that describe the architecture, implementation language, and deployment mechanism. No classification was made based on the application name alone.

**Determinism.** The pipeline is fully reproducible. The crawl, fetch, ingest, and enrich stages are implemented as a versioned Python package (`vista-docs`) with SQLite state tracking. The classification is implemented as an explicit mapping table in `classify_system_type.py` with inline rationale comments for every non-obvious decision. Re-running the pipeline from the VDL crawl forward reproduces the same inventory, the same markdown corpus, and the same classifications.

---

*End of guide.*
