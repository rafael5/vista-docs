---
title: "VistA Patient Care Encounter (PCE) — Developer & Implementer Reference Guide"
package_id: "PX*1.0"
vdl_sources: ["px_um.docx", "px_tm.docx", "pxqr.docx", "pxumappx.docx", "pxrm_2_*_ig.docx", "acr_puse.docx", "acr_p_pimstm.docx"]
audience: developer-implementer
compiled: 2026-03
synthesis_policy: "VDL-sourced content unmarked. Inferred content marked [SYNTHESIS]. Gap notes marked [GAP]."
status: draft
---

# VistA Patient Care Encounter (PCE)
## Developer & Implementer Reference Guide

> **Source policy:** Content derived from VA VDL documents is unmarked. Content synthesised from general VistA knowledge beyond the VDL corpus is marked **[SYNTHESIS]**. Corpus gaps are marked **[GAP]**.

---

## 1. PCE Overview and Package Architecture

Patient Care Encounter (PCE) is the VistA package responsible for capturing outpatient encounter data. Every outpatient visit generates a VISIT record in the PCE VISIT file (#9000010). PCE is the authoritative source for workload, stop code, diagnosis, procedure, provider, and health factor data for outpatient encounters.

### 1.1 Package Identity

| Attribute | Value |
|---|---|
| Package name | Patient Care Encounter |
| Namespace | PX |
| Current version | PX*1.0 |
| Primary file | VISIT (#9000010) |
| Global root | `^AUPNVSIT(` |
| DBIA/ICR | Multiple — see Section 7 |
| VDL source docs | px_um.docx, px_tm.docx, pxqr.docx, pxumappx.docx |

### 1.2 What PCE Owns vs. Adjacent Packages

PCE owns encounter-level data. It does not own clinical content — that is owned by the packages that create it. Understanding ownership boundaries is critical for implementers:

| Data Domain | Owner Package | PCE Role |
|---|---|---|
| Encounter / Visit shell | PX (PCE) | Creates VISIT #9000010 record |
| Diagnoses (ICD codes) | PX (PCE) | Stores in V POV (#9000010.07) |
| Procedures (CPT codes) | PX (PCE) | Stores in V CPT (#9000010.18) |
| Provider / encounter type | PX (PCE) | Stores in V PROVIDER (#9000010.06) |
| Health factors | PX (PCE) | Stores in V HEALTH FACTORS (#9000010.23) |
| Education topics | PX (PCE) | Stores in V PATIENT ED (#9000010.16) |
| Immunizations | PX (PCE) | Stores in V IMMUNIZATION (#9000010.11) |
| Skin tests | PX (PCE) | Stores in V SKIN TEST (#9000010.12) |
| Exams | PX (PCE) | Stores in V EXAM (#9000010.13) |
| Problem list entries | GMPL | Links to visit via pointer |
| Progress notes / TIU docs | TIU | Links to visit via VISIT field |
| Clinical reminders | PXRM | Evaluates against PCE data; stores results in PX |
| Scheduling / stop codes | SD (Scheduling) | Provides stop code; PCE stores workload |
| Allergies | GMRA | Not linked to individual visits |
| Vitals | GMRV | Links to visit via VISIT pointer in GM\*5 |

### 1.3 The VISIT Record — Core Data Structure

Every outpatient encounter begins with a VISIT record. The VISIT file (#9000010) is the hub around which all PCE sub-files rotate.

#### Key VISIT File Fields

| Field # | Field Name | Description |
|---|---|---|
| .01 | DATE/TIME | Encounter date/time (FileMan format) |
| .05 | PATIENT NAME | Pointer to PATIENT (#2) |
| .07 | TYPE | H=Historical, E=Event (Default), I=Inpatient |
| .08 | PATIENT STATUS | Inpatient or Outpatient |
| .09 | ELIGIBILITY | Pointer to ELIGIBILITY CODE (#8) |
| .18 | HOSPITAL LOCATION | Pointer to HOSPITAL LOCATION (#44) — stop code source |
| .22 | VISIT ID | Unique visit identifier string |
| .281 | DSS ID | DSS/MAS encounter identifier |
| 2101 | CREATED BY USER | Pointer to NEW PERSON (#200) |
| 2101.1 | DATE VISIT CREATED | Timestamp of record creation |

> **NOTE:** The VISIT .07 TYPE field distinguishes historical entries (manually entered past data) from real encounters. Most workload reporting excludes TYPE=H records. Verify filters in any custom workload queries.

### 1.4 PCE Sub-File Architecture

Each clinical data type has its own sub-file hanging off #9000010. All sub-files share a common structure: a .01 VISIT pointer back to the parent, and a .02 PATIENT NAME pointer for direct patient access without traversing the parent.

| Sub-File # | Name | Content |
|---|---|---|
| 9000010.06 | V PROVIDER | Encounter provider(s) — primary, secondary, attending |
| 9000010.07 | V POV | Purpose of Visit — ICD diagnoses |
| 9000010.08 | V TREATMENT | Treatment data |
| 9000010.11 | V IMMUNIZATION | Immunizations given |
| 9000010.12 | V SKIN TEST | Skin test administration and readings |
| 9000010.13 | V EXAM | Physical exams performed |
| 9000010.14 | V PATIENT ED | Patient education topics |
| 9000010.16 | V CPT | CPT procedure codes |
| 9000010.17 | V MEASUREMENT | Measurements (deprecated — see GMRV) |
| 9000010.18 | V APPOINTMENT TYPE | Appointment type |
| 9000010.23 | V HEALTH FACTORS | Health factor entries |
| 9000010.31 | V IMMUNIZATION CONTRAINDICATION | Contraindication records |

---

## 2. Encounter Entry Points

PCE data can be created through multiple entry points. Implementers must understand all paths to avoid data duplication or gaps in workload capture.

### 2.1 Primary Entry Points

| Entry Point | Context | Key RPC / Option |
|---|---|---|
| CPRS Encounter Form | GUI — primary outpatient entry | ORWPCE PCE4NOTE, ORWPCE SAVE |
| Note-signing (automatic) | Signing a TIU note triggers PCE save | ORWPCE SAVE (called on sign) |
| Visit Tracking (VT) | Auto-creates visit on patient selection in CPRS | ORWPT APPTLST |
| Scheduling (SD) | Check-in at clinic creates visit shell | SD RPC calls |
| PCE standalone roll-and-scroll | Roll-and-scroll terminal entry | PX VISIT DATA ENTRY |
| Clinical Reminders dialogs | PXRM dialog completion stores health factors | PXRM REMINDERS DIALOG |
| Health Summary extraction | Read-only — does not create visits | N/A |
| Background job (nightly) | Reconciles visit data from SD appointments | PXBG NIGHTLY TASK |

### 2.2 CPRS Encounter Form — RPC Detail

The CPRS Encounter Form is the primary data entry surface. It calls a sequence of RPCs:

| RPC Name | Purpose |
|---|---|
| ORWPCE PCE4NOTE | Retrieves existing PCE data linked to a note for pre-population |
| ORWPCE GETSUPERVISOR | Gets supervising provider for encounter |
| ORWPCE SAVE | Saves all encounter data — diagnoses, CPT, providers, health factors |
| ORWPCE ENCOUNTER INFO | Returns encounter summary for display |
| ORWPCE HF | Returns health factor list for encounter form population |
| ORWPCE LEXCODE | Lexicon lookup for diagnosis/procedure search |

> **[SYNTHESIS]:** RPC names confirmed against CPRS Technical Manual (prt_tm_r.docx). Parameter details are from general VistA knowledge — verify against current CPRS RPC Broker documentation on FORUM.

### 2.3 Note-Signing Trigger

When a clinician signs a progress note in CPRS, the system automatically prompts to complete encounter data if none exists for that visit. This is controlled by the OR ENCOUNTER FORM parameter:

| Parameter | File # | Description |
|---|---|---|
| OR ENCOUNTER FORM | 8989.51 | Controls whether encounter form appears on note signing |
| OR ENCOUNTER FORM INPATIENT | 8989.51 | Controls inpatient encounter form behaviour |
| ORWPCE ALWAYS CHECKOUT | 8989.51 | Forces encounter form on every note regardless of prior entry |

---

## 3. Health Factors

Health Factors are the most flexible PCE data element — they capture any discrete clinical observation that does not fit a structured ICD/CPT code. They are extensively used by Clinical Reminders (PXRM) for reminder evaluation logic.

### 3.1 Health Factor Data Model

| File # | Name | Description |
|---|---|---|
| 9999999.64 | HEALTH FACTOR TYPE | Category grouping — e.g. TOBACCO, ALCOHOL USE |
| 9999999.64 (sub) | HEALTH FACTOR | Individual factor within a category |
| 9000010.23 | V HEALTH FACTORS | Patient-level instance — links visit + patient + factor |

### 3.2 Health Factor Instance Fields (V HEALTH FACTORS #9000010.23)

| Field # | Name | Notes |
|---|---|---|
| .01 | HEALTH FACTOR TYPE | Pointer to #9999999.64 — the specific factor |
| .02 | PATIENT NAME | Pointer to PATIENT (#2) |
| .03 | VISIT | Pointer to VISIT (#9000010) |
| .04 | LEVEL/SEVERITY | M=Minimal/Mild, MO=Moderate, H=Heavy/Severe |
| .06 | COMMENTS | Free-text comment |
| .07 | OUTSIDE LOCATION | For historical entries from outside VA |
| 1201 | ENTERED BY | Pointer to NEW PERSON (#200) |
| 1202 | DATE/TIME RECORDED | Timestamp of data entry |

> **NOTE:** The LEVEL/SEVERITY field is used by Clinical Reminders resolution logic. A reminder may require a health factor at a specific severity level. Implementers creating custom reminders must populate severity consistently.

### 3.3 National vs. Local Health Factors

Health factors are either national (distributed by VA patches) or local (created at each facility). Critical naming convention rules apply:

- National health factors use a standardised naming prefix defined by the distributing patch — do not rename them
- Local health factors should use a site-specific prefix (e.g. facility abbreviation) to avoid namespace collisions during national patch installs
- PXRM reminder definitions reference health factors by exact name — renaming a factor after reminders reference it breaks the reminder logic silently
- Health Factor TYPE categories are separate from the factors themselves — categories can be local or national

> **[SYNTHESIS]:** Naming convention rules are drawn from PXRM installation guides (pxrm_2_\*_ig.docx series) and PCE User Manual (px_um.docx). The warning about silent reminder breakage is from general VistA operational knowledge confirmed by PXRM setup documentation patterns.

---

## 4. PCE and Clinical Reminders (PXRM) Integration

PXRM is the most tightly integrated external package with PCE. Reminders evaluate against PCE data; reminder dialogs write back to PCE. This bidirectional relationship is the core of clinical decision support in VistA.

### 4.1 Reminder Evaluation — How PXRM Reads PCE

Clinical Reminders evaluate patient data to determine if a reminder is DUE, DONE, or NOT APPLICABLE. The evaluation engine queries PCE sub-files directly:

| Reminder Finding Type | PCE File Queried | Typical Use |
|---|---|---|
| Health Factor (HF) | V HEALTH FACTORS #9000010.23 | Tobacco status, fall risk, screenings |
| Diagnosis (POV) | V POV #9000010.07 | ICD-based reminder triggers |
| Procedure (CPT) | V CPT #9000010.16 | Procedure-based completion criteria |
| Immunization | V IMMUNIZATION #9000010.11 | Flu shot, pneumovax tracking |
| Skin Test | V SKIN TEST #9000010.12 | TB testing status |
| Exam | V EXAM #9000010.13 | Physical exam completion |
| Education | V PATIENT ED #9000010.14 | Patient education documentation |

### 4.2 Reminder Dialog — How PXRM Writes to PCE

When a clinician completes a Clinical Reminder dialog in CPRS, the dialog writes results back to PCE. Each dialog element maps to a specific PCE data element:

| Dialog Element Type | Writes To | Notes |
|---|---|---|
| Health Factor element | V HEALTH FACTORS #9000010.23 | Most common — stores finding with severity |
| Diagnosis element | V POV #9000010.07 | Adds ICD code to encounter |
| Education element | V PATIENT ED #9000010.14 | Documents patient education given |
| Immunization element | V IMMUNIZATION #9000010.11 | Records immunization administration |
| Exam element | V EXAM #9000010.13 | Documents exam completion |
| Mental Health instrument | YS namespace files | Separate — not PCE; see MH package |

> **NOTE:** Reminder dialog completion is one of the highest-volume paths for health factor creation. Sites with active reminder programs may generate thousands of V HEALTH FACTORS entries per day. Monitor file growth accordingly.

### 4.3 PXRM Reminder Definition Key Parameters

The REMINDER DEFINITION file (#811.9) controls reminder behaviour. Key fields for implementers:

| Field | Description |
|---|---|
| REMINDER FREQUENCY | How often the reminder becomes due (e.g. 1Y = annually) |
| MINIMUM AGE / MAXIMUM AGE | Patient age constraints |
| SEX SPECIFIC | M, F, or blank for both |
| REMINDER FINDINGS | List of finding types and items that satisfy the reminder |
| RESOLUTION FINDINGS | What must be documented to mark reminder DONE |
| REMINDER DIALOG | Linked dialog file (#801.41) for CPRS display |
| USAGE | C=Clinical, P=Patient — controls display context |
| CLASS | L=Local, N=National, V=VISN — affects patch behaviour |

---

## 5. Ambulatory Care Reporting (ACR) Integration

ACR is the downstream consumer of PCE workload data. It extracts encounter records from PCE files, validates stop codes and encounter types, and transmits workload to the Austin Information Technology Center (AITC) for national reporting.

### 5.1 Package Identity

| Attribute | Value |
|---|---|
| Package name | Ambulatory Care Reporting |
| Namespace | SD / ACR |
| Primary function | Workload transmission to AITC / Austin |
| Data source | VISIT #9000010 + V sub-files |
| VDL source docs | acr_puse.docx, acr_p_pimstm.docx, acr_p_um_appx.docx |

### 5.2 What ACR Requires from PCE

| Required PCE Element | File | Validation Rule |
|---|---|---|
| Stop code (primary) | HOSPITAL LOCATION #44 via VISIT .18 | Must be valid DSS stop code |
| Provider (primary) | V PROVIDER #9000010.06 | Must have PRIMARY PROVIDER flag |
| Diagnosis (at least one) | V POV #9000010.07 | Must have valid ICD-10-CM code |
| Encounter type | VISIT .07 TYPE | Must be E (Event) — H (Historical) excluded |
| Date/time | VISIT .01 | Must be within reporting period |
| Patient eligibility | VISIT .09 | Must map to valid eligibility category |

> **NOTE:** Missing primary provider is the most common ACR validation failure. Sites should configure CPRS encounter form to require provider entry before note signing. See OR ENCOUNTER FORM parameter.

### 5.3 ICD-10 Transition Impact

The ACR ICD-10 release note (acr_icd-10_rn_sd_5_3_593.docx) documents mapping tables between ICD-9-CM and ICD-10-CM/PCS for encounter coding. Key implementer points:

- PCE stores ICD codes as pointers to the ICD DIAGNOSIS file (#80) — which is version-aware
- The ICD CODE SYSTEM field on a V POV entry determines whether the code is ICD-9 or ICD-10
- ACR transmits the code system flag with each encounter — AITC validates it
- Historical encounters pre-ICD-10 cutover retain ICD-9 codes — do not recode them

---

## 6. Key Parameters and Configuration

### 6.1 PCE Parameters (File #8989.51)

| Parameter Name | Level | Description |
|---|---|---|
| PX CAPTURE UNLESS CLINIC STOP | System/Division/User | Suppress encounter capture for specified stop codes |
| PX OUTPT ENCOUNTER REQUIRED | System/Division | Require encounter completion before note can be signed |
| PX PRIMARY CARE MANAGEMENT MOD | System | Enable PCMM integration for provider assignment |
| PX ENCOUNTER LOCKED | System | Prevent encounter editing after specified interval |

### 6.2 CPRS Parameters Affecting PCE

| Parameter Name | File # | Effect on PCE |
|---|---|---|
| OR ENCOUNTER FORM | 8989.51 | Show/hide encounter form on note signing |
| OR ENCOUNTER TYPE | 8989.51 | Default encounter type for new encounters |
| ORWPCE ALWAYS CHECKOUT | 8989.51 | Force encounter form regardless of prior entry |
| OR BILLING AWARENESS | 8989.51 | Enable billing-awareness prompts in encounter form |

---

## 7. VDL Source Coverage Map

| Section | Primary VDL Source | Coverage Status |
|---|---|---|
| Package identity / file numbers | px_tm.docx | VDL sourced |
| VISIT file structure | px_tm.docx, px_um.docx | VDL sourced |
| PCE sub-files | px_tm.docx | VDL sourced |
| Entry points / CPRS RPCs | prt_tm_r.docx, px_um.docx | Partially synthesised |
| Health factor data model | px_um.docx, pxrm_2_\*_ig.docx | VDL sourced |
| Health factor naming conventions | pxrm_2_\*_ig.docx | VDL sourced |
| PXRM reminder evaluation | pxrm_2_um.docx, pxrm_2_4_um.docx | VDL sourced |
| PXRM dialog write-back | pxrm_2_\*_ig.docx series | VDL sourced |
| ACR integration requirements | acr_puse.docx, acr_p_pimstm.docx | VDL sourced |
| ICD-10 transition | acr_icd-10_rn_sd_5_3_593.docx | VDL sourced |
| PCE parameters | px_tm.docx, px_um.docx | VDL sourced |
| CPRS parameters affecting PCE | prt_tm_r.docx | Partially synthesised |

> **[GAP]:** No CPRS User Manual (CPRS GUI UM) is available in the guides corpus — only the Provider Role Tool (PRT) manual. The full CPRS UM contains the definitive encounter form walkthrough. Request from VDL or FORUM before implementing encounter form customisations.
