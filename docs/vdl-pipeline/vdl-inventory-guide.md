# VDL Inventory Field Guide

**File:** `vdl_inventory_enriched.csv`
**Schema:** `vdl_inventory_schema.json`
**Row count:** 8,834 (one row per document file; PDF and DOCX editions of the same document are separate rows)
**Last updated:** 2026-03-30

---

## Overview

Each row in the inventory represents a single document file hosted on the VA VistA Documentation Library (VDL). A single VistA patch may have multiple document rows (e.g., a Release Notes DOCX and its PDF companion). Fields are grouped below by the aspect of the inventory they describe.

### Table Column Definitions

Each field table has four columns:

| Column | Meaning |
|---|---|
| **Field** | The CSV column name. |
| **Type** | The data type of the field's values: `string` (text), `integer` (whole number), or `boolean` (stored as `0`/`1` string in the CSV). |
| **Raw / Derived** | **Raw** — scraped directly from the VDL website with no transformation beyond storage. **Derived** — computed or inferred from raw fields, filenames, or document titles by the enrichment pipeline. |
| **Nullable** | Whether the field can be blank for some rows. **No** — always populated; safe to use without checking. **Yes** — blank for some rows, typically for a well-defined reason documented in the Description (e.g., `decommission_date` is only set when `app_status = decommissioned`). |

---

## Field Reference

### Section Fields

These fields describe the top-level organizational category on the VDL site.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `section_name` | string | Raw | No | Full display name of the VDL section the application belongs to. Values: `Clinical`, `Financial-Administrative`, `Infrastructure`, `VistA/GUI Hybrids (formerly HealtheVet)`, `Monograph`. |
| `section_code` | string | Derived | No | Short uppercase code for the section, assigned during enrichment for use as a stable key in filenames, slugs, and filters. Values: `CLI`, `FIN`, `INF`, `GUI`, `MON`. Derived by mapping `section_name` to a fixed lookup table. |

---

### Application Fields

These fields describe the VistA application (package) that owns the document. All application fields are uniform across every row that belongs to the same app.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `app_name_full` | string | Raw | No | Full display name of the application as shown on the VDL site. Example: `Admission Discharge Transfer`. |
| `app_name_abbrev` | string | Raw | No | Official VistA abbreviation for the application. Example: `ADT`. Used as the primary app identifier throughout the inventory. |
| `app_status` | string | Raw | No | **Document-level** status tag from the VDL site. Values: `active` (current, published document), `archive` (older or superseded edition of a document — the application itself may still be fully operational), `decommissioned` (the application has been formally retired). Note: most active applications have both `active` and `archive` rows; the presence of `archive` rows alone does not indicate the application is out of service. |
| `system_type` | string | Raw | No | Technical architecture category as listed on the VDL site. Values include: `VistA`, `VistA + GUI`, `VistA + COTS`, `VistA + middleware`, `Web client`, `VA enterprise service`, `Integration middleware`, `COTS product`, `VBA system`, `Data patch`, `Program documentation`. |
| `cots_dependent` | string | Raw | Yes | Name of the commercial off-the-shelf (COTS) product the application depends on, if any. Empty for applications with no COTS dependency. Examples: `First Databank drug interaction service (MOCHA dosing checks)`, `3M DRG Grouper (commercial classification algorithm + weight tables)`. |
| `decommission_date` | string | Raw | Yes | Month the application was formally decommissioned, in `YYYY-MM` format. Only present when `app_status = decommissioned`. Empty for active and archive documents. The most reliable single indicator that an application is no longer in operation. |

---

### Patch Fields

These fields identify the specific VistA patch a document belongs to. They are extracted by regex from the document filename and title during enrichment. Empty for baseline (non-patch) documents.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `pkg_ns` | string | Derived | Yes | VistA package namespace — the alphabetic prefix of the patch identifier. Example: `DG` for the Registration package, `PSO` for Outpatient Pharmacy. Extracted from the filename or doc title by matching the leading uppercase letter segment before `*`. |
| `patch_ver` | string | Derived | Yes | Full version string for the package, as it appears in the patch ID. Example: `5.3`. Do not sort this field lexicographically — use `patch_ver_major` and `patch_ver_minor` for correct numeric ordering. |
| `patch_ver_major` | integer | Derived | Yes | Major version number parsed from `patch_ver`. Example: `5` from `5.3`. |
| `patch_ver_minor` | integer | Derived | Yes | Minor version number parsed from `patch_ver`. Example: `3` from `5.3`. |
| `patch_num` | integer | Derived | Yes | Sequential patch number within the package version. Example: `1057` in `DG*5.3*1057`. Higher numbers indicate more recent patches; the maximum value for a given app reflects cumulative patch activity over the application's lifetime. |
| `patch_id` | string | Derived | Yes | Primary patch identifier in standard VistA notation: `NS*V*P` for patches or `NS*V` for version anchors. Example: `DG*5.3*1057`. Uniquely identifies a patch within the VistA namespace. |
| `patch_id_full` | string | Derived | Yes | Full multi-namespace patch identifier when a patch spans more than one VistA package. Populated only when `multi_ns = 1`. Components are separated by `/`. Example: `DG*5.3*554/TIU*1*184/USR*1*27`. The primary namespace appears first. |
| `multi_ns` | boolean (0/1) | Derived | No | Flag indicating whether the patch touches more than one VistA package namespace. `1` = multi-namespace patch (the full compound ID is in `patch_id_full`); `0` = single namespace. Affects 48 rows (~0.5% of all rows). |
| `group_key` | string | Derived | Yes | Stable composite key for grouping all documents belonging to the same application and package version: `app_name_abbrev:pkg_ns:patch_ver`. Example: `ADT:DG:5.3`. Useful for aggregating or filtering across all patches and documents for a given app. |

---

### Document Classification Fields

These fields describe the type, tier, and subject of each document. They are assigned by the enrichment pipeline using filename pattern matching, title parsing, and a manual review pass for residual gaps.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `doc_code` | string | Derived | Yes | Short standardized code identifying the document type. Assigned primarily by automated filename/title pattern matching; a small subset was assigned by human review (see `doc_labelling`). Common values: `RN` (Release Notes), `DIBR` (Deployment/Installation/Back-Out/Rollback Guide), `IG` (Installation Guide), `UM` (User Manual), `UG` (User Guide), `TM` (Technical Manual), `FORM` (VBA Form), `CRU` (Clinical Reminder Update), `VDD` (Version Description Document), `POM` (Production Operations Manual), `SUP` (Supplement), `SG` (Setup Guide), `TRG` (Training Guide), `QRG` (Quick Reference Guide). Empty (~151 rows) for documents that could not be classified. |
| `doc_label` | string | Derived | Yes | Human-readable expansion of `doc_code`. Example: `doc_code = DIBR` → `doc_label = Deployment, Installation, Back-Out, and Rollback Guide`. Used for display and filtering. Always consistent with `doc_code`. |
| `doc_layer` | string | Derived | No | Structural tier indicating how the document relates to patch activity. Values: `patch` — document is specific to a numbered patch (has a populated `patch_num`); `anchor` — baseline or version-level document not tied to a specific patch number; `plain` — document with no patch structure at all (e.g., standalone reference materials, forms). Derived from whether `patch_num` is present and whether the document is a versioned baseline. |
| `doc_labelling` | string | Derived | No | Provenance of the `doc_code` assignment. Values: `code` — assigned automatically by the pipeline using filename/title pattern matching (8,526 rows); `manual` — assigned by human review during a gap-fill pass on residual unlabelled documents (308 rows, per `vdl_inventory_label_gaps_residual.md`, 2026-03-30). Useful for distinguishing high-confidence automated labels from human-reviewed ones. |
| `doc_subject` | string | Derived | Yes | Best-effort topical subject extracted from `doc_title`. Populated for 5,356 rows; empty where extraction was ambiguous or not attempted. Not guaranteed to be consistent across similar documents. |

---

### Document Identity Fields

These fields identify the physical file and provide stable handles for referencing or downloading it.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `doc_title` | string | Raw | No | Full document title as displayed on the VDL site. Example: `DG*5.3*1057 Deployment, Installation, Back-Out, and Rollback Guide`. |
| `doc_filename` | string | Raw | No | Filename of the document file as hosted on the VDL site, including extension. Example: `dg_5_3_1057_dibr.docx`. Note: this is a web document filename — not a VistA FileMan filename. |
| `doc_slug` | string | Derived | No | URL-safe stable identifier derived from the filename stem (lowercase, non-alphanumeric characters replaced with `_`). PDF and DOCX editions of the same document share the same slug, making it the preferred key for deduplicating format pairs. Example: both `dg_5_3_1057_dibr.docx` and `dg_5_3_1057_dibr.pdf` → `dg_5_3_1057_dibr`. |
| `doc_format` | string | Derived | No | File format without the leading dot, derived from the `doc_filename` extension. Values: `pdf`, `docx`, `doc`. Use this field rather than parsing `doc_filename` directly. For YAML frontmatter or format-specific processing pipelines. |

---

### Flag Fields

These fields mark rows that should be excluded from substantive VistA documentation analysis.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `noise_type` | string | Derived | No | Classification of non-substantive document rows. Empty string = substantive VistA documentation (7,491 rows, ~85%). `vba_form` = VA Benefits Administration form — not VistA technical documentation (1,192 rows); `va_ref` = VA-wide reference document unrelated to a specific VistA package (149 rows); `test_document` = test or placeholder document (2 rows). Exclude rows where `noise_type != ''` when performing documentation coverage analysis. |

---

### URL Fields

These fields provide direct links to the application's VDL page and the document file itself.

| Field | Type | Raw / Derived | Nullable | Description |
|---|---|---|---|---|
| `app_url` | string | Raw | No | URL of the application's landing page on the VDL site. Points to `https://www.va.gov/vdl/application.asp?appid=N`. All documents belonging to the same application share the same `app_url`. |
| `doc_url` | string | Raw | No | Direct download URL for the specific document file. Points to the `.pdf`, `.docx`, or `.doc` file on the VDL server. |
| `companion_url` | string | Derived | Yes | URL of the paired format edition of the same document. For a DOCX row, this points to the PDF, and vice versa. Populated for 7,422 of 8,834 rows (~84%). Empty when no paired format exists for that document. Derived by matching `doc_slug` values across rows and cross-referencing `doc_format`. |

---

## Field Categories at a Glance

| Category | Fields | Raw | Derived |
|---|---|---|---|
| Section | `section_name`, `section_code` | `section_name` | `section_code` |
| Application | `app_name_full`, `app_name_abbrev`, `app_status`, `system_type`, `cots_dependent`, `decommission_date` | all 6 | — |
| Patch identity | `pkg_ns`, `patch_ver`, `patch_ver_major`, `patch_ver_minor`, `patch_num`, `patch_id`, `patch_id_full`, `multi_ns`, `group_key` | — | all 9 |
| Doc classification | `doc_code`, `doc_label`, `doc_layer`, `doc_labelling`, `doc_subject` | — | all 5 |
| Doc identity | `doc_title`, `doc_filename`, `doc_slug`, `doc_format` | `doc_title`, `doc_filename` | `doc_slug`, `doc_format` |
| Flags | `noise_type` | — | `noise_type` |
| URLs | `app_url`, `doc_url`, `companion_url` | `app_url`, `doc_url` | `companion_url` |

**Raw fields: 15 — Derived fields: 15**

---

## Common Filters

| Goal | Filter |
|---|---|
| Substantive docs only | `noise_type == ''` |
| Currently active documents | `app_status == 'active'` |
| Applications in operation | `decommission_date == ''` (no date set) |
| Patch-specific documents | `doc_layer == 'patch'` |
| Baseline / version docs | `doc_layer == 'anchor'` |
| Avoid double-counting PDF+DOCX pairs | `doc_format == 'pdf'` (or `docx`) — pick one consistently |
| Single app, all docs | `app_name_abbrev == 'ADT'` |
| All docs for a patch | `patch_id == 'DG*5.3*1057'` |
