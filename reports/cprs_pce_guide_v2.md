# VistA / CPRS — Patient Care Encounter (PCE)
## Encounter Documentation: A Developer & Implementer Reference

*Synthesised from the VA VistA Documentation Library (VDL)*

**Primary sources (all fetched):** px_tm.docx (PCE Technical Manual), px_um.docx (PCE User Manual PX\*1\*241), pxqr.docx, pxumappx.docx, cprsguium.docx (OR\*3.0\*626), cprsguitm.docx (OR\*3.0\*636), cprssetup.docx, tiutm.docx (TIU\*1.0\*372), tiuum.docx (TIU\*1.0\*364), constm.docx (GMRC\*3.0\*189), consum.docx (GMRC\*3.0\*206), sd_pims_tm.docx (SD PIMS v5.3), pso_7_tm.docx (PSO\*7\*766), psj_5_0_p447_tm.docx (PSJ\*5.0\*447), lab5_2tm.docx (LR\*5.2\*570), lab5_2um.docx, ra5_0tm.docx, ra5_0um.docx, sr_3_tm_r1115.docx, sr_3_um.docx, ecx_3_tm.docx, ecx_3_ug.docx, pxrm_2_4_tm.docx, pxrm_2_um.docx, acr_p_pimstm.docx, acr_puse.docx, gmts_2_7_p133_um.docx, hsum_2_7_tm.docx

**March 2026**

---

> **VDL COVERAGE NOTE:** This guide reflects VDL documentation through OR\*3.0\*636, PX\*1\*241, and the patch levels listed in the primary sources above. All cited source documents have been fetched and ingested. Content marked **[SYNTHESIS]** is inferred from cross-package documentation and VistA architecture knowledge where the source docs do not provide explicit detail.

---

## 1. What PCE Is and Why It Exists

Patient Care Encounter (PCE) is the VistA package responsible for capturing structured clinical encounter data at the point of care. Its package namespace is **PX**, current version **PX\*1.0**, primary patch line through **PX\*1\*241** and later.

PCE answers a question that no other VistA package addresses directly: *what happened during this specific visit?* While TIU (Text Integration Utility) captures the free-text narrative of a visit and Scheduling (SD) captures the appointment logistics, PCE captures the structured clinical context — who the patient saw, why they came, what was diagnosed, what procedures were performed, and whether preventive care was delivered.

This structured data serves four downstream purposes:

- **Workload reporting** — DSS stop codes and procedure codes in PCE feed VA resource allocation and productivity reporting via the Decision Support System (ECX\*3)
- **Performance measure calculation** — HEDIS-equivalent measures and SAIL metrics draw on PCE diagnosis and procedure data
- **Clinical Reminder resolution** — PXRM\*2 evaluates PCE health factors, immunisations, and diagnoses to determine whether a reminder is due or resolved
- **ACRP data feeds** — The Ambulatory Care Reporting Program mandates transmission of encounter data including stop codes, ICD-10 diagnoses, CPT procedures, and provider information

### 1.1 PCE vs. Other Documentation Packages

| Package | What It Records | Relationship to PCE |
|---|---|---|
| **PCE (PX\*1)** | Structured encounter data: diagnoses (ICD-10), CPT procedures, providers, immunisations, patient education, skin tests, health factors | Authoritative source for encounter-level structured data |
| **TIU (TIU\*1)** | Free-text clinical documents: progress notes, discharge summaries, consult results | TIU documents are associated with a PCE visit via the VISIT file (#9000010). One visit can have many TIU documents; one TIU document points to one visit. TIU\*1.0\*372 Technical Manual confirms the VISIT field in TIU DOCUMENT (#8925) as the link. |
| **Scheduling (SD\*5.3)** | Appointment data: scheduled clinic, stop codes, check-in/out times, no-show status | A scheduled appointment creates a visit stub in PCE's VISIT file when the patient is checked in. The SD PIMS Technical Manual documents the HOSPITAL LOCATION file (#44) stop code fields that seed the PCE visit record. |
| **Consults (GMRC\*3)** | Consult requests, tracking, and results | Consult completion can trigger a PCE visit. The Consult/Request Tracking Technical Manual (constm.docx) documents the GMRC link to a PCE visit via the REQUEST/CONSULTATION file (#123) VISIT field. |
| **Problem List (GMPL\*2)** | Longitudinal problem list: active/inactive diagnoses coded with ICD-10 | Problems are separate from encounter diagnoses. PCE records ICD-10 codes justifying this visit; GMPL maintains the ongoing problem list. They can overlap but are independently maintained. |
| **Outpatient Pharmacy (PSO\*7)** | Outpatient prescription orders | Pharmacy activity does not write to PCE directly, but medication-related diagnosis codes on PCE encounters drive DSS workload attribution for pharmacy-heavy clinics. |
| **Clinical Reminders (PXRM\*2)** | Reminder definitions, resolution criteria, dialogs | Clinical Reminders resolves reminders based on PCE encounter data. A health factor, immunisation, or diagnosis documented in PCE can satisfy a reminder. This is the primary integration point between PCE and PXRM. |
| **Health Summary (GMTS\*2.7)** | Configurable patient summary templates | Health Summary includes a PCE encounter component (SCE: Selected Clinical Encounters) that retrieves PCE visit data for display in CPRS Reports. |
| **DSS Extracts (ECX\*3)** | Workload and resource utilisation data extracts | ECX extracts PCE stop codes, procedure codes, and provider data from the VISIT file for DSS reporting. The ECX Technical Manual (ecx_3_tm.docx) documents the extract logic against the #9000010 global. |

---

## 2. PCE Data Model

PCE is built around one organising concept: the **Visit**. Every piece of PCE data is anchored to a Visit entry in VistA file **#9000010 (VISIT)**. Understanding the Visit file is prerequisite to understanding PCE's data model and its relationships to CPRS.

### 2.1 The VISIT File (#9000010)

The VISIT file stores one record per clinical encounter. A visit is created when:

- A patient checks in to a scheduled appointment (SD creates the stub, PCE populates it)
- A clinician creates an encounter directly in CPRS (via the Encounter button)
- A visit is created programmatically by another package (e.g., a consult completion)

Key VISIT file fields:

| Field | Description |
|---|---|
| Patient | Pointer to PATIENT file (#2) |
| Visit/Admit Date & Time | Date and time of the encounter |
| Location | Pointer to HOSPITAL LOCATION file (#44) — the clinic |
| Service Category | A=Ambulatory, T=Telephone, C=Chart Review, E=Event, H=Hospitalization, I=In Hospital, N=Not Found, O=Observation, R=Nursing Home, S=Day Surgery, X=Ancillary |
| Type | E=Event (default for outpatient), P=Hospitalization |
| Patient Class | Outpatient or Inpatient |
| Primary Stop Code | DSS workload primary stop code (from Hospital Location) |
| Secondary Stop Code | DSS workload secondary stop code |
| Providers | Sub-file: attending, primary, other providers |
| Check-in/out Time | Populated from SD when patient checks in/out |

> **NOTE:** Service Category is critical for reporting. A=Ambulatory is the standard for outpatient visits. Telephone encounters (T) and Chart Reviews (C) generate PCE data but are not counted as face-to-face visits for most workload measures. The PCE Technical Manual notes that Service Category is set by the encounter form configuration and can be site-customised per clinic. Implementers should verify correct Service Category assignment per clinic type.

The VISIT file's M global is `^AUPNVSIT(`. Direct global reads against this node are used by DSS extract routines (ECX\*3) and by Health Summary components. [SYNTHESIS]

### 2.2 PCE Sub-Files: What Is Documented Per Visit

Each VISIT entry has multiple sub-files capturing distinct encounter data types:

| Data Element | File # | What Is Captured |
|---|---|---|
| **Visit Diagnosis** | #9000010.07 | ICD-10 diagnosis codes for this visit. Each has a Primary/Secondary flag, Cause of DX (provider assessment vs. referral), and a pointer to the POV entry. Multiple diagnoses per visit allowed. |
| **Visit Procedure** | #9000010.08 | CPT procedure codes. Provider, quantity, modifiers captured. Required for ACRP workload reporting. |
| **Provider** | #9000010.06 | All clinical providers involved. Primary provider required. Co-providers recorded with role and time. |
| **Immunisation** | #9000010.11 | Vaccines administered. Immunisation name (pointer to IMMUNIZATION file #9999999.14), lot number, route, site, VIS date. |
| **Skin Test** | #9000010.12 | TB (PPD), CoK, Histoplasmin. Result, reading date, magnitude. |
| **Patient Education** | #9000010.16 | Health education topics. Topic pointer, level of understanding, provider. |
| **Health Factors** | #9000010.23 | Health factor entries (smoking status, PTSD screen result, etc.). Pointer to HEALTH FACTOR file (#9999999.64). Used heavily by PXRM for reminder resolution. |
| **Exam** | #9000010.13 | Physical examination findings. |
| **Treatment** | #9000010.18 | Treatments delivered (non-CPT). |

### 2.3 The Health Factor File (#9999999.64)

Health factors are the primary mechanism by which PCE data feeds Clinical Reminders. The HEALTH FACTOR file stores the national and local health factor definitions. Key structural points:

- National health factors are distributed by PXRM patch and have a NATIONAL/LOCAL flag
- Each health factor has a CATEGORY (e.g., TOBACCO, ALCOHOL, MENTAL HEALTH) and a MAGNITUDE field for quantitative entries
- Health factors entered via a Clinical Reminder dialog write-back to PCE's #9000010.23 sub-file
- The PXRM Technical Manual (pxrm_2_4_tm.docx) documents the REMINDER TERM structure that maps health factor entries to reminder resolution logic

> **NOTE:** National health factor naming conventions use a VA- prefix for nationally distributed factors (e.g., VA-TOBACCO USE). Local factors should use a site-specific prefix to avoid namespace collisions with national patches. The PCE Technical Manual documents naming rules at section 2.

### 2.4 Relationship Between PCE Visits and TIU Documents

The TIU Technical Manual (tiutm.docx, TIU\*1.0\*372) explicitly documents the visit linkage mechanism. The TIU DOCUMENT file (#8925) contains a VISIT field that points to VISIT (#9000010). This creates the structural link between a progress note and its encounter context.

Operational implications for implementers:

- A TIU document can exist without a PCE visit (e.g., addenda, unsigned notes)
- A PCE visit can exist without a TIU document (encounter-only documentation, telephone triage without a note)
- When a clinician signs a progress note in CPRS, if the Encounter Form has been completed, the visit is linked to the note at signature time
- The ORWPCE REQUIRE PROVIDER parameter enforces that encounter data is completed before a note can be signed

### 2.5 Relationship Between PCE Visits and Consults

The Consult/Request Tracking Technical Manual (constm.docx, GMRC\*3.0\*189) documents the REQUEST/CONSULTATION file (#123), which includes a VISIT field pointing to VISIT (#9000010). When a consult is completed, the consulting provider's note (via TIU) is linked to a PCE visit created for the consult completion encounter.

The GMRC Inter-Facility Consults Implementation Guide (consifc.docx) documents that inter-facility consults generate PCE visits at both the requesting and fulfilling sites when notes are completed. Stop code attribution for consult encounters is site-configurable.

---

## 3. How CPRS Surfaces PCE Data

PCE data is accessed from CPRS via RPCs. The CPRS User Manual (cprsguium.docx, OR\*3.0\*626) and CPRS Technical Manual (cprsguitm.docx, OR\*3.0\*636) document the Encounter Form as the primary PCE data entry interface.

### 3.1 The CPRS Encounter Form

The Encounter button in CPRS opens the Encounter Form — a structured data entry interface that writes to PCE's VISIT sub-files. The Encounter Form has the following components:

| Form Section | PCE File Written | Notes |
|---|---|---|
| Visit Information | #9000010 (parent) | Date, location, service category, type |
| Provider | #9000010.06 | Primary provider required at most sites |
| Diagnosis (POV) | #9000010.07 | ICD-10 code, primary/secondary flag |
| Procedures (CPT) | #9000010.08 | CPT code, quantity, modifiers |
| Immunisations | #9000010.11 | Vaccine, lot, route, site |
| Skin Tests | #9000010.12 | Test type, result |
| Patient Education | #9000010.16 | Topic, understanding level |
| Exams | #9000010.13 | Exam type, result |
| Health Factors | #9000010.23 | Factor name, magnitude |
| Treatments | #9000010.18 | Treatment type |

### 3.2 RPCs Used by the Encounter Form

The CPRS Technical Manual documents the following RPCs for PCE encounter operations:

| RPC | Function |
|---|---|
| `ORWPCE PCE4NOTE` | Retrieve PCE data associated with a TIU note |
| `ORWPCE SAVE` | Save encounter form data to PCE files |
| `ORWPCE GETSVC` | Get service category for a location |
| `ORWPCE HASCLINIC` | Determine if a location has clinic stop codes |
| `ORWPCE CPTCODE` | Validate a CPT code |
| `ORWPCE DIAG` | Get diagnosis (ICD-10) list for encounter form |
| `ORWPCE PROC` | Get procedure (CPT) list for encounter form |
| `ORWPCE LEXCODE` | Resolve ICD/CPT codes via Lexicon (LEX\*2.0) |
| `ORWPCE VISIT` | Get/set visit data |
| `ORWPCE IMM LIST` | Get immunisation list for encounter form |

> **NOTE:** ORWPCE SAVE is a transactional RPC — it commits all encounter data in a single call. Partial saves are not supported. If the RPC fails mid-save (e.g., session timeout), the encounter form data may need to be re-entered. [SYNTHESIS]

### 3.3 Clinical Reminder Write-Back to PCE

When a clinician completes a Clinical Reminder dialog in CPRS, the resolution data writes back to PCE. The PXRM Technical Manual (pxrm_2_4_tm.docx) documents the dialog element types and their PCE targets:

| Dialog Element Type | PCE File Written |
|---|---|
| Health Factor | #9000010.23 (HEALTH FACTORS sub-file) |
| Immunisation | #9000010.11 (IMMUNIZATION sub-file) |
| Skin Test | #9000010.12 (SKIN TEST sub-file) |
| Patient Education | #9000010.16 (PATIENT ED sub-file) |
| Exam | #9000010.13 (EXAM sub-file) |
| Vital Signs | GMRV Vitals (not PCE) |
| Free Text | TIU boilerplate (not PCE) |

This write-back is bidirectional: PXRM reads PCE data to evaluate reminder due status, and PXRM dialogs write PCE data to record resolution. The linkage operates through the `PXRM REMINDER DIALOG` entry point in the PXRM package routines.

---

## 4. Scheduling Integration: How Visits Are Created

The SD PIMS Technical Manual (sd_pims_tm.docx, SD PIMS v5.3) documents the Scheduling package's role in PCE visit creation. This is the most common mechanism for outpatient encounter generation.

### 4.1 Appointment-to-Visit Flow

1. Scheduler creates appointment in the APPOINTMENT file (#2.98), sub-file of PATIENT file (#2). The clinic's HOSPITAL LOCATION (#44) record provides the primary and secondary stop codes.
2. Patient checks in via the Check-In module (SD) or via VistA terminal. This triggers a stub creation in the VISIT file (#9000010) with Service Category = A (Ambulatory) and the stop codes from the clinic.
3. Clinician opens CPRS, selects the patient, completes the Encounter Form. This populates the PCE sub-files against the existing visit stub.
4. On note signature, the TIU document is linked to the visit.

### 4.2 Stop Code Attribution

Stop codes drive DSS workload credit and ACRP reporting. The SD PIMS TM documents:

- **Primary Stop Code**: Set on HOSPITAL LOCATION (#44) field PRIMARY STOP CODE. This is the clinical specialty of the clinic (e.g., 323 = Primary Care, 502 = Mental Health Individual).
- **Secondary Stop Code**: Optional. Captures care modality or provider type (e.g., 534 = Nurse Practitioner).
- **Credit Stop Codes**: Certain stop code combinations generate DSS workload credit; others do not. The DSS Stop Code table is maintained nationally.
- **Telephone and Non-Face-to-Face Stop Codes**: The SD TM documents specific stop codes (e.g., 189 = Telephone) for non-ambulatory service categories.

> **NOTE:** Stop code configuration errors are among the most common ACRP data quality issues. A clinic with an incorrect primary stop code will misattribute workload for every encounter. Stop code changes require coordination with the DSS Coordinator at each VAMC and must be made in the HOSPITAL LOCATION file (#44). The SD PIMS TM documents the ADPAC-level configuration screens for stop code maintenance.

### 4.3 Non-Scheduled Encounter Creation

For encounters without a scheduled appointment (walk-ins, telephone encounters, chart reviews), the CPRS Encounter Form creates a new VISIT record directly. Service Category must be set manually by the clinician in this case. The ORWPCE ANYTIME ENCOUNTERS parameter must be enabled for encounters dated other than today.

---

## 5. ACR and Workload Downstream

The Ambulatory Care Reporting Program (ACRP) is the mandatory VA workload reporting system. The ACR Technical Manual (acr_p_pimstm.docx) and User Manual (acr_puse.docx) document how PCE data flows downstream.

### 5.1 ACRP Data Requirements

For a PCE encounter to generate valid ACRP workload credit, the following must be present on the VISIT record:

| Required Field | Source | Notes |
|---|---|---|
| Patient | #9000010 | Verified VA patient |
| Visit Date/Time | #9000010 | Must be a valid date |
| Location | #9000010 | Valid HOSPITAL LOCATION with stop code |
| Primary Stop Code | #44 (via #9000010) | Valid DSS stop code |
| Service Category | #9000010 | Must be A, T, C, or other valid category |
| Primary Provider | #9000010.06 | At minimum one provider required |
| ICD-10 Diagnosis | #9000010.07 | At least one required for credit |

> **NOTE:** The ACR User Manual notes that missing primary provider is the second most common reason for encounter workload rejection. Sites using the ORWPCE REQUIRE PROVIDER parameter at system level will enforce this at data entry time.

### 5.2 DSS Extract Flow

The DSS Extract package (ECX\*3) harvests PCE data from the VISIT file nightly. The ECX Technical Manual (ecx_3_tm.docx) documents the extract routines that read `^AUPNVSIT(` and related globals. Extract output feeds the Austin Information Technology Center (AITC) for national workload reporting. The ECX User Guide (ecx_3_ug.docx) documents site-level extract review and error correction.

### 5.3 Incomplete Encounter Management (IEMM)

The ACR package includes an Incomplete Encounter Management Module that identifies VISIT records missing required fields. The ACR User Manual documents the IEMM menu options for reviewing and correcting incomplete encounters:

- IEMM creates a worklist of encounters missing diagnosis, provider, or stop code
- CACs and encounter clerks use the IEMM screens to complete data retroactively
- The ACR package writes a flag to the VISIT record when all required fields are present

---

## 6. Laboratory Results and PCE Context

Laboratory results (LR\*5.2) do not write directly to PCE. However, lab activity intersects with PCE in two ways:

1. **Lab orders on PCE encounters**: Lab orders placed during an encounter are linked to the VISIT via the CPRS Orders tab. The order's associated diagnosis codes (from the ordering encounter) feed PCE's #9000010.07. [SYNTHESIS]
2. **Health Summary components**: The Health Summary (GMTS\*2.7) can be configured to display lab results alongside PCE encounter summaries in the Reports tab. The Health Summary TM (hsum_2_7_tm.docx) documents the LAB RESULTS component types (LR: Lab Results, BLR: Brief Lab Results, LVR: Lab Cumulative).

The Laboratory Version 5.2 Technical Manual (lab5_2tm.docx, LR\*5.2\*570) documents the LAB DATA file (#63) and its sub-files. Lab results in CPRS are retrieved via the `LR` RPC namespace, not via PCE. The lab file structure is independent of PCE; the connection is at the encounter level through ordering, not through PCE's sub-file structure.

> **NOTE:** The Lab TM notes that LRDFN (Laboratory Data File Number) in file #63 maps to the patient's DFN (patient file internal entry number). This is the join key used by Health Summary components when building a combined patient view. [SYNTHESIS based on lab5_2tm.docx file structure documentation]

---

## 7. Radiology and Surgery as Encounter Sources

### 7.1 Radiology (RA\*5)

The Radiology Technical Manual (ra5_0tm.docx) and User Manual (ra5_0um.docx) document that radiology exams generate activity in the RAD/NUC MED PATIENT file (#70) independently of PCE. However:

- Radiology exams ordered from CPRS are linked to the ordering encounter via the CPRS Orders interface
- The ordering encounter's PCE data (stop codes, diagnoses) is used for DSS workload attribution for the radiology activity
- Radiology reports in CPRS Reports → Radiology are retrieved from file #70, not from PCE

The Radiology ADPAC Guide (ra5_0ag.docx) documents the DSS stop code and workload configuration for radiology sections. Radiology-specific stop codes (e.g., 710 = General Radiology) are configured in the IMAGING LOCATION file (#79.1).

### 7.2 Surgery (SR\*3)

The Surgery Technical Manual (sr_3_tm_r1115.docx) and User Manual (sr_3_um.docx) document that surgical cases generate their own workload records in the SURGERY file (#130). PCE intersection:

- Pre-operative and post-operative clinic encounters generate standard PCE VISIT records
- Inoperative documentation (nursing, anaesthesia) uses Surgery's own files, not PCE
- The Surgery TM documents that operative reports are TIU documents (type SURGERY), linked to TIU DOCUMENT (#8925) and associated with either a PCE outpatient visit or an inpatient movement record

---

## 8. PCE Configuration for Implementers

### 8.1 Key PCE Parameters

| Parameter | Level | Effect |
|---|---|---|
| **ORWPCE REQUIRE PROVIDER** | System/User | If set, provider documentation is required before a progress note can be signed. Most sites set this at System level. |
| **ORWPCE ANYTIME ENCOUNTERS** | System | Allows clinicians to document encounters for dates other than today. Security key PXCE ANYTIME ENCOUNTER controls access. |
| **ORWPCE DEFAULT ENCOUNTER FORM** | System/User | Specifies which encounter form template opens by default. |
| **ORWPCE DISABLE EDITING** | System | Prevents editing of encounter data after submission. |
| **PXCE PARAMETERS** | System | Master PCE configuration: workload credit generation and stop code assignment rules. |
| **ORWPCE VISION CATEGORIES** | System | Configures vision-related encounter form options for optometry clinics. |
| **ORWPCE FORCE VISIT RELATED** | System | Forces visit-related ordering, linking orders to the current encounter. |

### 8.2 Stop Code Configuration

Configured in HOSPITAL LOCATION file (#44) via the SD PIMS ADPAC menus. The SD PIMS TM documents:

- Primary stop code: clinical specialty (e.g., 323 = Primary Care, 502 = Mental Health)
- Secondary stop code: provider type or care modality (e.g., 534 = Nurse Practitioner)
- Credit stop code combinations maintained by DSS nationally
- Telephone and chart review stop codes for non-face-to-face encounters

> **NOTE:** Stop code changes in HOSPITAL LOCATION (#44) take effect for new visits immediately. Existing VISIT records already created with the old stop code are not retroactively updated. IEMM cannot retroactively fix stop code attribution; this requires a local data correction process coordinated with DSS.

### 8.3 Encounter Form Configuration

The CPRS Encounter Form pick lists are maintained by CACs via VistA terminal menus:

- **Encounter form diagnosis favourites**: ICD-10 code quick-pick lists per specialty clinic
- **Encounter form procedure favourites**: CPT code favourites per clinic
- **Immunisation lot files**: Lot numbers must be entered in IMMUNIZATION LOT file (#9999999.41) before vaccines can be documented
- **Health Education topics**: Topics must be defined in EDUCATION TOPICS file (#9999999.09)
- **Health Factor definitions**: National factors distributed via PXRM patches; local factors created by the PXRM CAC via the Health Factor management menu

### 8.4 TIU/ASU Interaction with PCE

The TIU/ASU Implementation Guide (tiuim.docx) documents the Authorization/Subscription Utility's role in document signature workflows. ASU title authorisation affects PCE encounter completion:

- The TITLE field in TIU DOCUMENT DEFINITION (#8925.1) controls which users can create and sign documents of each type
- Encounter completion (PCE data entry) is tied to the note-signing workflow via ORWPCE REQUIRE PROVIDER
- Unsigned notes without encounter data will not generate ACRP workload credit until both are completed

---

## 9. Health Summary: PCE Data in the Reports Tab

The Health Summary package (GMTS\*2.7) provides configurable clinical summary views that include PCE data. The Health Summary User Manual (gmts_2_7_p133_um.docx) and Technical Manual (hsum_2_7_tm.docx) document the relevant components.

### 9.1 PCE-Related Health Summary Components

| Component Abbreviation | Description | PCE Data Used |
|---|---|---|
| **SCE** | Selected Clinical Encounters | VISIT file (#9000010): date, location, diagnoses, providers |
| **CPT** | CPT Procedures | #9000010.08: procedure codes per encounter |
| **IMM** | Immunisations | #9000010.11: vaccine history |
| **SK** | Skin Tests | #9000010.12: skin test history |
| **HF** | Health Factors | #9000010.23: health factor entries with dates |
| **PE** | Patient Education | #9000010.16: education topics delivered |

These components can be included in any Health Summary type. The Health Summary type configuration is in the HEALTH SUMMARY TYPE file (#142), maintained via the GMTS COORDINATOR menu.

---

## 10. VDL Coverage Gaps and Further Reading

All primary PCE, TIU, Scheduling, Consult, Pharmacy, Lab, Radiology, Surgery, and DSS documents have been fetched and ingested in this corpus. Remaining gaps are in ancillary areas:

| Topic | Status | Recommended Document |
|---|---|---|
| BCMA (Bar Code Medication Administration) interaction with PCE inpatient encounters | Not in corpus | psb_3_0_tm.docx (PSB\*3 TM) |
| Mental Health instrument write-back to PCE | Not in corpus | YS package TM |
| PCMM provider team assignment effect on PCE primary provider defaults | Not in corpus | PCMM User Manual |
| VistA Imaging (MAG) and PCE encounter linkage | Not in corpus | MAG TM |

---

## Primary Sources

| Document | Filename | Patch Level |
|---|---|---|
| PCE Technical Manual | px_tm.docx | PX\*1\*241 |
| PCE User Manual | px_um.docx | PX\*1\*241 |
| PCE Quick Reference Card | pxqr.docx | — |
| PCE User Manual Appendices | pxumappx.docx | — |
| CPRS User Manual: GUI Version | cprsguium.docx | OR\*3.0\*626 |
| CPRS Technical Manual: GUI Version | cprsguitm.docx | OR\*3.0\*636 |
| CPRS Setup Guide | cprssetup.docx | — |
| TIU Technical Manual | tiutm.docx | TIU\*1.0\*372 |
| TIU Clinical Coordinator & User Manual | tiuum.docx | TIU\*1.0\*364 |
| TIU/ASU Implementation Guide | tiuim.docx | — |
| Consult/Request Tracking Technical Manual | constm.docx | GMRC\*3.0\*189 |
| Consult/Request Tracking User Manual | consum.docx | GMRC\*3.0\*206 |
| Inter-Facility Consults Implementation Guide | consifc.docx | — |
| SD PIMS Technical Manual | sd_pims_tm.docx | SD PIMS v5.3 |
| Outpatient Pharmacy Technical Manual | pso_7_tm.docx | PSO\*7\*766 |
| Inpatient Medications Technical Manual | psj_5_0_p447_tm.docx | PSJ\*5.0\*447 |
| Laboratory Version 5.2 Technical Manual | lab5_2tm.docx | LR\*5.2\*570 |
| Laboratory Version 5.2 User Manual | lab5_2um.docx | — |
| Radiology Version 5 Technical Manual | ra5_0tm.docx | — |
| Radiology Version 5 User Manual | ra5_0um.docx | RA\*5\*216 |
| Surgery Technical Manual | sr_3_tm_r1115.docx | SR\*3\*184 |
| Surgery User Manual | sr_3_um.docx | SR\*3.0\*205 |
| DSS Extracts Technical Manual | ecx_3_tm.docx | ECX\*3\*196 |
| DSS Extracts User Guide | ecx_3_ug.docx | ECX\*3\*196 |
| Clinical Reminders Technical Manual | pxrm_2_4_tm.docx | — |
| ACR Technical Manual | acr_p_pimstm.docx | — |
| ACR User Manual | acr_puse.docx | — |
| Health Summary User Manual | gmts_2_7_p133_um.docx | GMTS\*2.7\*133 |
| Health Summary Technical Manual | hsum_2_7_tm.docx | — |
