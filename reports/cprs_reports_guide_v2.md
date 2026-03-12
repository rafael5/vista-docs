# VistA / CPRS — Reports & Clinical Data Views
## A Developer & Implementer Reference

*Synthesised from the VA VistA Documentation Library (VDL)*

**Primary sources (all fetched):** cprsguium.docx (OR\*3.0\*626), cprsguitm.docx (OR\*3.0\*636), cprssetup.docx, cprslmtm.docx (OR\*3.0\*626), tiutm.docx (TIU\*1.0\*372), tiuum.docx (TIU\*1.0\*364), constm.docx (GMRC\*3.0\*189), consum.docx (GMRC\*3.0\*206), sd_pims_tm.docx (SD PIMS v5.3), pso_7_tm.docx (PSO\*7\*766), pso_7_pharm_um.docx (PSO\*7\*795), pso_7_man_um.docx (PSO\*7\*795), psj_5_0_p447_tm.docx (PSJ\*5.0\*447), PSJ_5_0_p447_PHAR_UM.docx, PSJ_5_0_NURSE_UM.docx, lab5_2tm.docx (LR\*5.2\*570), lab5_2um.docx, ra5_0tm.docx, ra5_0um.docx, ra5_0ag.docx, sr_3_um.docx (SR\*3.0\*205), sr_3_tm_r1115.docx (SR\*3\*184), ecx_3_tm.docx (ECX\*3\*196), gmts_2_7_p133_um.docx (GMTS\*2.7\*133), hsum_2_7_tm.docx, gmplum.docx, gmra_4_0_um.docx, gmra_4_0_tm.docx, vitl5_um.docx, vitl5_tm.docx, pxrm_2_um.docx, pxrm_2_4_tm.docx, acr_p_pimstm.docx

**March 2026**

---

> **VDL COVERAGE NOTE:** This guide reflects VDL documentation through OR\*3.0\*636 and the patch levels listed above. All cited source documents have been fetched and ingested. Content marked **[SYNTHESIS]** is inferred from cross-package documentation and VistA architecture knowledge where source docs do not provide explicit detail. The prior VDL GAP notices for Laboratory, Health Summary, Vitals, Allergies, and Consults have been resolved — all packages are now represented in the corpus.

---

## 1. Architecture: How CPRS Aggregates Clinical Data

CPRS (Computerized Patient Record System) is a GUI front-end for VistA. It does not store clinical data — every data element displayed is owned by a back-end VistA package and retrieved at runtime via Remote Procedure Calls (RPCs). Understanding this ownership model is essential for implementers: the same clinical fact can surface simultaneously on the Coversheet, in the Reports tab, in a Health Summary, and in a Clinical Reminder, each rendering differently via different RPCs from different VistA packages.

### 1.1 Package Ownership Map

| Clinical Domain | VistA Package | Package Code | Primary Files | CPRS Surfaces |
|---|---|---|---|---|
| **Active Medications (Outpatient)** | Outpatient Pharmacy | PSO\*7 | PRESCRIPTION (#52) | Coversheet → Meds, Reports → Medications, Orders |
| **Inpatient Medications** | Inpatient Medications | PSJ\*5 | PHARMACY PATIENT (#55) | Coversheet → Meds, Reports → Medications, Orders |
| **Lab Results** | Laboratory | LR\*5.2 | LAB DATA (#63) | Coversheet → Labs, Reports → Labs, Graphing |
| **Vital Signs** | Vitals/Measurements | GMRV\*5 | GMRV VITAL MEASUREMENT (#120.5) | Coversheet → Vitals, Reports → Vitals, Graphing |
| **Allergies / ADRs** | Adverse Reaction Tracking | GMRA\*4 | PATIENT ALLERGIES (#120.8) | Coversheet → Allergies, Reports → Allergies, Banner |
| **Problem List** | Problem List | GMPL\*2 | PROBLEM (#9000011) | Coversheet → Problems, Reports → Diagnoses |
| **Clinical Documents** | Text Integration Utility | TIU\*1 | TIU DOCUMENT (#8925) | Notes tab, Reports → Progress Notes / Discharge Summaries |
| **Radiology Reports** | Radiology/Nuclear Medicine | RA\*5 | RAD/NUC MED PATIENT (#70) | Reports → Radiology Reports |
| **Consults** | Consult/Request Tracking | GMRC\*3 | REQUEST/CONSULTATION (#123) | Consults tab, Reports → Consults |
| **Clinical Reminders** | Clinical Reminders | PXRM\*2 | REMINDER DEFINITION (#811.9) | Coversheet → Reminders, Reminders drawer |
| **Health Summary** | Health Summary | GMTS\*2.7 | HEALTH SUMMARY TYPE (#142) | Reports → Health Summary |
| **Scheduling / ADT** | Scheduling (PIMS) | SD\*5.3 / DG\*5.3 | APPOINTMENT (#2.98), PATIENT MOVEMENT (#405) | Coversheet → Postings, Reports → Admissions |
| **Encounter / Visit Data** | PCE | PX\*1 | VISIT (#9000010) | Encounter form, Reports → Encounters (via Health Summary) |
| **Surgery** | Surgery | SR\*3 | SURGERY (#130) | Reports → Surgery |
| **Anatomic Pathology** | Laboratory (AP) | LR\*5.2 | LAB DATA (#63) sub-files | Reports → Lab (AP section) |
| **Orders** | CPRS / Order Entry | OR\*3 | ORDER (#100) | Orders tab, Coversheet → Orders |
| **DSS Workload** | DSS Extracts | ECX\*3 | VISIT (#9000010) downstream | Not displayed in CPRS; feeds external DSS reporting |

> **NOTE (Lab):** The Laboratory Version 5.2 Technical Manual (lab5_2tm.docx, LR\*5.2\*570) documents the LAB DATA file (#63) as the primary storage file. Lab results in CPRS are retrieved via the `LR` RPC namespace. The lab package has multiple sub-packages (Anatomic Pathology, Blood Bank, Universal Interface) each with their own documentation but sharing the LR\*5.2 core package.

### 1.2 The Four CPRS Display Surfaces

CPRS renders clinical data across four distinct surface types, each with different data currency, formatting, and configuration:

| Surface | Location | Currency | Configuration |
|---|---|---|---|
| **Coversheet panes** | Default patient view | Parameterised time windows | Site/user-level OR parameters |
| **Reports tab (text)** | Reports → [category] | On-demand query with date range | Report time ranges, Health Summary types |
| **CPRS Graphing** | Reports → Graphing or toolbar | On-demand, user-selectable range | Graph type, overlay, reference ranges |
| **Health Summary** | Reports → Health Summary | Defined per HS type | HEALTH SUMMARY TYPE (#142) configuration |

The same vital sign reading will appear in all four surfaces simultaneously: the most recent value in the Coversheet pane, the full history in the Reports Vitals text view, as a trend line in Graphing, and as a component in a configured Health Summary.

---

## 2. The Coversheet: First-Look Clinical Snapshot

The Coversheet is the default view when a patient is selected in CPRS. It presents a parameterised, read-only snapshot of current clinical status drawn from multiple packages simultaneously. The CPRS User Manual (cprsguium.docx) documents each pane's content and the CPRS Setup Guide (cprssetup.docx) documents site-level parameter configuration.

### 2.1 Coversheet Panes, Data Sources, and Parameters

| Coversheet Pane | Data Source | Key Parameters | Implementation Notes |
|---|---|---|---|
| **Active Problems** | GMPL\*2, file #9000011 | ORQQPL COVERSHEET (configures display) | Active problems only. ICD-10 code and free-text narrative. Problem list must be actively maintained by clinicians. gmplum.docx documents the workflow. |
| **Allergies / Adverse Reactions** | GMRA\*4, file #120.8 | None — always shown | Verified allergies and adverse reactions. Unverified entries shown with flag. Also always visible in the banner bar. gmra_4_0_um.docx documents the verification workflow. |
| **Postings (Flags)** | DG\*5.3, DGPF | None — always shown | Patient Record Flags (PRFs) and clinical postings. Category I (national) flags shown first. Requires DG\*5.3\*425+. |
| **Active Medications** | PSO\*7 (#52), PSJ\*5 (#55) | ORWRP MEDS DISPLAYED (time window) | Outpatient and inpatient medications. Time window configurable. Pending, active, and recently discontinued shown. The PSO Pharmacist UM (pso_7_pharm_um.docx) documents medication status values. |
| **Clinical Reminders** | PXRM\*2 | PXRM reminder configuration | Due and applicable reminders. Requires reminder definitions, terms, and patient cohort logic. Click-through launches reminder dialog. |
| **Lab Results** | LR\*5.2 (#63) via OR RPCs | ORQQCS RANGE, ORQQCS START | Most recent results per test. Date range configurable (default: 1 year). Abnormal values flagged. The Lab TM documents result normalcy flags. |
| **Vital Signs** | GMRV\*5 (#120.5) | ORQQVS (time limit) | Latest recorded vitals. BMI computed. Date of last entry shown. vitl5_um.docx documents entry workflow. |
| **Appointments / Visits** | SD\*5.3 (#2.98) | ORQQAPPT (time limit) | Upcoming and recent appointments. Requires scheduling module. sd_pims_tm.docx documents appointment file structure. |

### 2.2 Coversheet Configuration Parameters (CPRS Setup Guide)

The CPRS Setup Guide (cprssetup.docx) documents these site-level parameters:

| Parameter | Purpose |
|---|---|
| ORWCH BOUNDS | Coversheet pane size/position for each user |
| ORQQCS RANGE | Lab results date range on Coversheet |
| ORQQVS SEARCH RANGE | Vitals time window on Coversheet |
| ORQQAPPT SEARCH RANGE | Appointments time window on Coversheet |
| ORWRP MEDS DISPLAYED | Medications time window on Coversheet |
| ORCH CONTEXT MEDS | Which medication types to display |

---

## 3. The Reports Tab: Full Clinical History

The Reports tab provides on-demand access to the full clinical history for a patient. Unlike the Coversheet (which shows current/recent data), the Reports tab accepts a user-specified date range and returns all records in that window. The CPRS User Manual (cprsguium.docx) documents the Reports tab at length; the CPRS Technical Manual (cprsguitm.docx) documents the RPCs.

### 3.1 Report Categories and Data Sources

| Report Category | Data Package | Primary File | RPC Namespace | Notes |
|---|---|---|---|---|
| **Progress Notes** | TIU\*1 | TIU DOCUMENT (#8925) | `TIU` | All signed progress note types. TIU Technical Manual (tiutm.docx) documents document types and status values. |
| **Discharge Summaries** | TIU\*1 | TIU DOCUMENT (#8925) | `TIU` | Inpatient discharge documents. Same TIU infrastructure as progress notes, different document type. |
| **Clinical Procedures** | TIU\*1 / MD | TIU DOCUMENT (#8925) | `TIU` | Clinical procedure results embedded as TIU documents. |
| **Consults** | GMRC\*3 | REQUEST/CONSULTATION (#123) | `GMRC` | Consult requests, status, and results. constm.docx documents file #123 structure; consum.docx documents clinician workflow. |
| **Surgery** | SR\*3 | SURGERY (#130) | `SR` | Operative reports and anaesthesia records. sr_3_um.docx documents the surgery report types. |
| **Radiology / Nuclear Med** | RA\*5 | RAD/NUC MED PATIENT (#70) | `RA` | Radiology reports by modality. ra5_0um.docx documents report statuses (DRAFT, VERIFIED, etc.). |
| **Lab Results** | LR\*5.2 | LAB DATA (#63) | `LR` | Chemistry, haematology, microbiology, anatomic pathology. Multiple display formats (see §4.2). |
| **Vital Signs** | GMRV\*5 | GMRV VITAL MEASUREMENT (#120.5) | `ORWGRPC` / `GMV` | Text tabular view and graphing. vitl5_tm.docx documents the measurement file. |
| **Medications** | PSO\*7, PSJ\*5 | PRESCRIPTION (#52), PHARMACY PATIENT (#55) | `ORWPS` | Outpatient and inpatient medication history. Full detail including discontinued. |
| **Allergies / Adverse Reactions** | GMRA\*4 | PATIENT ALLERGIES (#120.8) | `ORQQAL` | Full allergy history including unverified. gmra_4_0_tm.docx documents file #120.8. |
| **Immunisations** | PCE (PX\*1) | IMMUNIZATION (#9000010.11) | `ORWPCE` | Via PCE VISIT sub-file. |
| **Health Summary** | GMTS\*2.7 | HEALTH SUMMARY TYPE (#142) | `ORWRP` | Configurable multi-component summaries. See §6. |
| **Admissions** | DG\*5.3 | PATIENT MOVEMENT (#405) | `DGPM` | Inpatient admissions, discharges, transfers. |
| **Blood Bank** | LR\*5.2 (VBECS) | Via HL7 from VBECS | Read-only | Blood bank results from VBECS system via HL7; read-only in CPRS. Requires OR\*3\*309+. |

### 3.2 Report Date Range Behaviour

All Reports tab categories accept a user-specified date range. Default date ranges are controlled by parameters:

| Parameter | Default | Controls |
|---|---|---|
| ORWRP TIME/OCC LIMITS ALL | Site-configurable | Default date range for all reports |
| ORWRP TIME/OCC LIMITS INDV | Per-user override | User-level date range preference |
| ORQQCN DATE RANGE | 6 months | Consults default date range |
| ORQQRA SEARCH RANGE | 1 year | Radiology default date range |

---

## 4. Clinical Data Deep Dives: Multi-Surface Rendering

### 4.1 Medications: Three-Layer View

Medications are unique in CPRS because two separate pharmacy packages (PSO outpatient, PSJ inpatient) feed the same display surfaces. Both are documented in depth with their respective TMs and UMs now in the corpus.

**Outpatient Pharmacy (PSO\*7)** — PRESCRIPTION file (#52):

The PSO Technical Manual (pso_7_tm.docx, PSO\*7\*766) and Pharmacist/Manager UMs document the PRESCRIPTION file as the authoritative source. Key status values that affect CPRS display:

| Status | CPRS Medication Display | Notes |
|---|---|---|
| ACTIVE | Shown on Coversheet and Reports | Primary active medication |
| SUSPENDED | Shown on Coversheet (flagged) | Temporarily stopped |
| DISCONTINUED | Shown in Reports only (if in date range) | Not on Coversheet after cutoff |
| EXPIRED | Shown in Reports only | Prescription end date passed |
| PENDING | Shown on Coversheet (PENDING flag) | Not yet dispensed |
| ON HOLD | Shown on Coversheet (flagged) | Pharmacist hold |

**Inpatient Medications (PSJ\*5)** — PHARMACY PATIENT file (#55):

The PSJ Technical Manual (psj_5_0_p447_tm.docx, PSJ\*5.0\*447) and the Pharmacist UM document the inpatient medication workflow. The Nurse's UM (PSJ_5_0_NURSE_UM.docx) documents the administration record view. Key differences from outpatient:

- Inpatient orders are linked to inpatient admissions (PATIENT MOVEMENT #405)
- Medication Administration Records (MAR) are stored in the PHARMACY PATIENT file
- IV and unit-dose orders are separate order types within PSJ
- BCMA (Bar Code Medication Administration, PSB\*3) records actual administration events against PSJ orders

**RPC flow for medication display:**

The CPRS Technical Manual documents `ORWPS COVER` (Coversheet medications) and `ORWPS DETAIL` (full medication detail) as the primary medication RPCs. Both RPCs aggregate PSO and PSJ data in a single response.

### 4.2 Laboratory Results: Four Display Formats

The Laboratory Version 5.2 TM (lab5_2tm.docx) and UM (lab5_2um.docx) document the LAB DATA file (#63) structure. Lab results in CPRS appear in four formats, each pulling from the same underlying file:

| Format | Location | Data Rendered | Notes |
|---|---|---|---|
| **Coversheet recent labs** | Coversheet → Labs | Most recent result per test, date range configurable | Abnormal flag shown. Date of last result. |
| **Reports → Lab Results (text)** | Reports tab | All results in date range, grouped by specimen type | Most detailed; shows reference ranges, units, collection time |
| **Reports → Lab Cumulative** | Reports tab | Results in columnar/cumulative format by date | Useful for trend review without graphing |
| **CPRS Graphing** | Reports → Graph or toolbar | Numeric results as time-series lines | Multiple tests overlaid; reference range bands shown |

The Lab TM documents the LAB DATA (#63) sub-file structure for each specimen type. LRDFN (internal file number in #63) maps to the patient's DFN. Lab results are retrieved via the `LR` RPC namespace.

> **NOTE:** Microbiology results display differently — susceptibility data is tabular in the Reports view but cannot be graphed (non-numeric values). Blood bank results are read-only from VBECS via HL7 and display in a dedicated Blood Bank section. The Lab TM (lab5_2tm.docx) notes that VBECS results require the HL7 interface configured per the Universal Interface documentation (labuig.docx).

**Anatomic Pathology (AP)** — documented in apump422.docx and lab_ap_lr_5_2_ug.docx:

AP reports (surgical pathology, cytology, autopsy) are stored in LAB DATA (#63) sub-files for AP. They appear in CPRS Reports → Lab under an Anatomic Pathology section. AP reports are structured documents (not numeric results) rendered as text in the Reports tab.

**Blood Bank** — documented in lr_52_p267_ug.docx:

Blood bank results come from VBECS (Veterans Blood Establishment Computer Software) via HL7 interface. They display in CPRS Reports as read-only transfusion history. The Blood Bank ISBT User Guide documents the interface configuration.

### 4.3 Vital Signs: Coversheet, Reports Text, and Graphing

The Vitals TM (vitl5_tm.docx) documents the GMRV VITAL MEASUREMENT file (#120.5). Vitals follow the same three-tier pattern as other data:

- **Coversheet → Vitals**: most recent single measurement per vital type; BMI computed; date shown
- **Reports → Vital Signs (text)**: all recorded vitals in date range, tabular format, each timestamped and attributed to entering user
- **CPRS Graphing**: trend lines; multiple vitals overlaid; configurable range; reference ranges shown where defined

The Vitals UM (vitl5_um.docx) documents entry via the CPRS Vitals widget (introduced in OR\*3.0\*405) and via the standalone Vitals application. Both write to the same GMRV file and appear identically in all CPRS views.

Vital types supported for graphing (from vitl5_tm.docx): Blood Pressure (systolic/diastolic), Heart Rate, Temperature, Respiration Rate, Weight, Height, BMI, Pulse Oximetry, Pain Score, Circumference/Girth, Central Venous Pressure.

### 4.4 Allergies: The Persistent Cross-Context View

The Adverse Reaction Tracking TM (gmra_4_0_tm.docx) documents PATIENT ALLERGIES file (#120.8). Allergies are unique: the only data type always visible regardless of CPRS tab.

- **Banner bar**: abbreviated display (e.g., PENICILLIN; LATEX) at top of all CPRS screens while patient is selected; click-through to full detail
- **Coversheet → Allergies**: full verified allergy list with causative agent, reaction type, and severity
- **Reports → Allergies / Adverse Reactions**: full history including unverified entries, dates, documenting users

The ART UM (gmra_4_0_um.docx) documents the verification workflow. Key operational points:

- Unverified entries appear in the Reports allergy view visually distinguished from verified entries
- Order checks evaluate both verified and unverified entries (ORCHECK RPCs)
- Allergy entries have a MECHANISM field (Pharmacologic vs. Allergy vs. Unknown) that affects order check logic
- The gmra_4_0_tm.docx documents the ALLERGY field in file #120.8 as a free-text causative agent, resolved against the GMR ALLERGY file for national allergen matching

### 4.5 Progress Notes and Clinical Documents

The TIU Technical Manual (tiutm.docx, TIU\*1.0\*372) is the authoritative source for the TIU DOCUMENT file (#8925). Progress notes, discharge summaries, consult results, and clinical procedure notes are all stored as TIU documents and all appear in the CPRS Reports tab.

Key TIU document statuses (from tiutm.docx):

| Status | CPRS Visibility | Notes |
|---|---|---|
| UNSIGNED | Notes tab only | Visible to author only until cosigned |
| UNCOSIGNED | Notes tab | Awaiting cosignature |
| COMPLETED | Reports → Progress Notes | Signed and complete |
| AMENDED | Reports → Progress Notes | Amendment attached to original |
| RETRACTED | Not visible to clinicians | Administrative retraction |
| DELETED | Not visible | Hard delete |

The TIU Clinical Coordinator UM (tiuum.docx) documents the document type configuration (TIU DOCUMENT DEFINITION file #8925.1), which controls which note types appear in which CPRS tab sections. The TIU/ASU Implementation Guide (tiuim.docx) documents title-level access control via the Authorization/Subscription Utility.

> **NOTE (TIU):** The tiutm.docx documents that CPRS note display uses the `TIUSRVR` RPC namespace for retrieval and `TIUSRVLO` for list operations. Note signing uses `TIUSRVS`. Understanding these RPC namespaces is essential for troubleshooting note display issues.

### 4.6 Consults: From Request to Report

The Consult TM (constm.docx, GMRC\*3.0\*189) documents the REQUEST/CONSULTATION file (#123) in detail, including 39 HL7 segment tables for the HL7 interface that supports inter-facility consults.

Consults appear in CPRS in two locations:

1. **Consults tab**: Active and pending consult requests with status tracking
2. **Reports → Consults**: Full consult history including completed results

The Consult UM (consum.docx, GMRC\*3.0\*206) documents the clinician workflow. Key states in REQUEST/CONSULTATION (#123):

| Status | Description | CPRS Visibility |
|---|---|---|
| PENDING | Awaiting acceptance | Consults tab (requesting side) |
| ACTIVE | Accepted by service | Consults tab (both sides) |
| SCHEDULED | Appointment made | Consults tab |
| COMPLETE | Result filed | Reports → Consults; result in Notes tab |
| DISCONTINUED | Cancelled | Reports → Consults (historical) |

The Inter-Facility Consults Guide (consifc.docx) documents HL7-based routing between VA sites for consults sent to other facilities. These appear in CPRS with a REMOTE indicator.

### 4.7 Radiology Reports

The Radiology TM (ra5_0tm.docx) documents the RAD/NUC MED PATIENT file (#70) and the Radiology UM (ra5_0um.docx, RA\*5\*216) documents the clinician-facing workflow.

Radiology reports appear in CPRS Reports → Radiology Reports. Key report statuses (from ra5_0um.docx):

| Status | Meaning | CPRS Visibility |
|---|---|---|
| WAITING FOR EXAM | Ordered, not performed | Not yet in Reports |
| EXAMINED | Performed, not reported | Shows in Reports (status only) |
| TRANSCRIBED | Report dictated | Reports → Radiology (TRANSCRIBED flag) |
| VERIFIED | Radiologist signed | Reports → Radiology (full report) |
| AMENDED | Amendment attached | Reports → Radiology |

The Radiology ADPAC Guide (ra5_0ag.docx) documents the IMAGING LOCATION file (#79.1) configuration, including modality-specific setup (X-ray, CT, MRI, Nuclear Medicine, Ultrasound, Fluoroscopy). This drives which report types appear in the CPRS Radiology section.

> **NOTE (Radiology):** The ra5_0um.docx documents that CPRS retrieves radiology reports via the `RA` RPC namespace. Radiology orders placed in CPRS flow from ORDER (#100) to the radiology package when the order is accepted. The actual exam result flows back as a report and is stored in file #70, not in TIU.

### 4.8 Surgery Reports

The Surgery UM (sr_3_um.docx, SR\*3.0\*205) and TM (sr_3_tm_r1115.docx) document the SURGERY file (#130). Surgical cases appear in CPRS Reports → Surgery.

Surgery reports are TIU documents of type SURGERY stored in TIU DOCUMENT (#8925) and linked to the SURGERY file entry. The Surgery TM documents that:

- Operative reports are authored by the surgeon, cosigned by the attending
- Anaesthesia records are separate documents
- Pre/post-operative notes are standard TIU progress notes linked to outpatient PCE encounters
- The SURGERY file (#130) tracks the surgical case; the TIU documents are the actual narrative reports

---

## 5. CPRS Graphing

CPRS Graphing is a distinct rendering surface supporting time-series visualisation of numeric clinical data. It is accessible from the Reports tab and from the CPRS toolbar. The CPRS Technical Manual (cprsguitm.docx) documents the graphing RPCs.

### 5.1 Data Types Supported for Graphing

| Data Type | Source Package | File | Notes |
|---|---|---|---|
| Vital Signs | GMRV\*5 | #120.5 | All numeric vitals; systolic/diastolic as separate series |
| Lab Chemistry | LR\*5.2 | #63 | Numeric results only; microbiology excluded |
| Lab Haematology | LR\*5.2 | #63 | CBC components as individual series |
| Medications (dose/duration) | PSO\*7, PSJ\*5 | #52, #55 | Medication timelines overlaid with lab/vitals [SYNTHESIS] |
| Blood Glucose (if structured) | LR\*5.2 | #63 | Numeric lab result |
| Pulse Oximetry | GMRV\*5 | #120.5 | SpO2 percentage |
| Weight | GMRV\*5 | #120.5 | Trend over time; useful with A1c for diabetes management |

### 5.2 Graphing Configuration

The CPRS Setup Guide (cprssetup.docx) documents graph parameters:

| Parameter | Controls |
|---|---|
| ORWGRPC PAGESIZE | Number of data points per graph page |
| ORWG GRAPH SETTING | User-level graph type and display preferences |
| ORWG GRAPH EXCLUDE | Data types excluded from graphing at site level |

Reference ranges for lab results displayed as bands in graphs are sourced from the LAB REFERENCE RANGES file within LR\*5.2.

---

## 6. Health Summary: Configurable Multi-Component Views

The Health Summary package (GMTS\*2.7) provides configurable patient summary templates that aggregate data from multiple VistA packages. The Health Summary UM (gmts_2_7_p133_um.docx, GMTS\*2.7\*133) and TM (hsum_2_7_tm.docx) are now fully ingested.

### 6.1 Health Summary Architecture

A Health Summary type is a named template stored in HEALTH SUMMARY TYPE file (#142). Each type contains an ordered list of **components**, where each component corresponds to a specific clinical data domain from a specific package. When a Health Summary is generated in CPRS, each component fires a query against its source package.

Configuration is managed by the Health Summary Coordinator using the GMTS COORDINATOR menu in VistA.

### 6.2 Health Summary Component Reference

| Component Code | Name | Data Source | File | Configurable Options |
|---|---|---|---|---|
| **AD** | Admissions | DG\*5.3 | PATIENT MOVEMENT (#405) | Occurrences, date range |
| **A** | Allergies/Adverse Reactions | GMRA\*4 | #120.8 | Verified only / all |
| **BLR** | Brief Lab Results | LR\*5.2 | #63 | Occurrences per test, tests to include |
| **CL** | Clinical Reminders | PXRM\*2 | #811.9 | Due/resolved/all |
| **CN** | Consults | GMRC\*3 | #123 | Date range, status filter |
| **CPT** | CPT Procedures | PCE (PX\*1) | #9000010.08 | Date range |
| **D** | Diagnoses (Problem List) | GMPL\*2 | #9000011 | Active only / all |
| **HF** | Health Factors | PCE (PX\*1) | #9000010.23 | Category filter, date range |
| **IMM** | Immunisations | PCE (PX\*1) | #9000010.11 | Date range |
| **LR** | Lab Results | LR\*5.2 | #63 | Date range, test list |
| **LVR** | Lab Cumulative | LR\*5.2 | #63 | Date range, columnar format |
| **M** | Medications (Outpatient) | PSO\*7 | #52 | Active only / all, date range |
| **MI** | Medications (Inpatient) | PSJ\*5 | #55 | Date range |
| **MHV** | My HealtheVet | MHV | — | Patient-entered data |
| **PN** | Progress Notes | TIU\*1 | #8925 | Document type filter, date range |
| **PO** | Problem List | GMPL\*2 | #9000011 | Active/inactive/all |
| **RA** | Radiology Reports | RA\*5 | #70 | Date range, modality filter |
| **RS** | Reminders Summary | PXRM\*2 | #811.9 | Due only / all |
| **SCE** | Selected Clinical Encounters | PCE (PX\*1) | #9000010 | Date range, service category |
| **SK** | Skin Tests | PCE (PX\*1) | #9000010.12 | Date range |
| **SP** | Surgery/Procedures | SR\*3 | #130 | Date range |
| **V** | Vital Signs | GMRV\*5 | #120.5 | Date range, vital type filter |

### 6.3 Health Summary Configuration Workflow

From the Health Summary UM (gmts_2_7_p133_um.docx):

1. **Create or edit a Health Summary Type** in HEALTH SUMMARY TYPE (#142) via the GMTS COORDINATOR menu
2. **Add components** from the component list above, specifying occurrence/date limits per component
3. **Assign the type** to one or more CPRS locations/users via the OR CPRS parameter system (parameter: ORWRP HEALTH SUMMARY TYPE LIST)
4. **Test** by generating the summary in CPRS Reports → Health Summary

> **NOTE:** Health Summary generation can be slow for patients with large record volumes, since each component fires a separate VistA query. The Health Summary TM documents that component ordering matters — high-volume components (lab results, vitals) should be placed last to avoid timeout on the first rendered components.

---

## 7. Remote Data Views

CPRS supports display of clinical data from remote VistA sites via Remote Data Interoperability (RDI) and Remote Data Views (RDV). The CPRS Technical Manual documents this mechanism.

### 7.1 Implementation Requirements

- OR\*3\*294 (Remote Data Interoperability) must be installed
- HL7 messaging (HL\*1.6) provides inter-site transport — documented in the HL7 package TM (now included in corpus via the HL\*1.6 HLO docs)
- Patient lookup at remote sites uses MPI (Master Patient Index)
- Remote data is read-only — no ordering, documenting, or editing against remote records

### 7.2 Remote Data Coverage by Report Type

| Report Type | Remote Data Supported |
|---|---|
| Medications (outpatient) | Yes |
| Lab Results | Yes |
| Vital Signs | Yes |
| Allergies | Yes |
| Problem List | Yes |
| Radiology Reports | Yes |
| Progress Notes | Yes |
| Discharge Summaries | Yes |
| Consults | No |
| Clinical Reminders | No |
| Health Summary | No |
| Orders | No |

> **NOTE:** Remote Data Views depend on each remote site's VistA availability. Performance varies by network and remote site load. The CPRS TM recommends informing users that remote data reflects the state at time of retrieval and may be stale if the remote site was recently updated.

---

## 8. Clinical Scenarios: Data Through All Surfaces

### Scenario 1: Patient with Diabetes — A1c Monitoring

*Data path for a diabetes A1c result:*

1. Lab order placed in CPRS Orders tab → ORDER (#100) created → transmitted to LR via HL7
2. Lab specimen collected, result entered in LR → LAB DATA (#63) updated
3. **Coversheet → Labs**: A1c appears as most recent result for that test with abnormal flag if > 9.0
4. **Reports → Lab Results**: A1c with reference range, collection time, performing lab
5. **Reports → Lab Cumulative**: A1c column with all historical values in date range
6. **CPRS Graphing**: A1c trend line; can overlay Weight (GMRV) for combined metabolic view
7. **Health Summary (SCE + LR components)**: A1c in brief lab section alongside encounter list
8. **Clinical Reminder**: PXRM evaluates most recent A1c date and value against HbA1c reminder definition; if > 6 months old, reminder fires on Coversheet

### Scenario 2: Medication Change During Encounter

*Data path for a medication change:*

1. Clinician renews outpatient prescription in CPRS Orders tab
2. Order transmitted to PSO; pharmacist verifies and dispenses → PRESCRIPTION (#52) updated
3. **Coversheet → Medications**: new prescription appears as ACTIVE; discontinued prescription falls off within configurable time window (ORWRP MEDS DISPLAYED)
4. **Reports → Medications**: full history including discontinued prescription visible in date range
5. **Encounter Form**: prescribing encounter ICD-10 diagnosis codes written to PCE (#9000010.07) for workload attribution

### Scenario 3: Consult Request and Completion

*Data path for a dermatology consult:*

1. Primary care physician places consult order in CPRS → ORDER (#100) → GMRC creates entry in REQUEST/CONSULTATION (#123) with status PENDING
2. **Consults tab**: consult appears in ordering clinician's view; dermatology service sees it in their worklist
3. Dermatology accepts → status ACTIVE; schedules patient → status SCHEDULED
4. Dermatology completes consult, files note via TIU → TIU DOCUMENT (#8925) created of type CONSULT RESULT; #123 status → COMPLETE
5. **Consults tab**: consult marked complete; link to result note available
6. **Reports → Consults**: full consult lifecycle visible
7. **Reports → Progress Notes**: consult result note visible under dermatology author
8. PCE visit created at dermatology encounter; stop code attributed to dermatology specialty

### Scenario 4: Vital Signs Across All Surfaces

*Data path for a blood pressure reading:*

1. Nurse enters BP via CPRS Vitals widget or standalone Vitals app → GMRV VITAL MEASUREMENT (#120.5)
2. **Coversheet → Vitals**: most recent BP (systolic/diastolic) displayed immediately
3. **Reports → Vital Signs (text)**: BP with timestamp, entering user, measurement method
4. **CPRS Graphing**: systolic and diastolic as separate lines; can overlay with weight or medications timeline
5. **Health Summary (V component)**: BP in vitals section of any HS type that includes the V component
6. **Clinical Reminder**: PXRM hypertension reminder evaluates most recent BP against threshold criteria

---

## 9. VDL Coverage: What Has Changed Since v1

The first version of this guide (March 2026, v1) identified six VDL gaps. All have been resolved:

| Prior Gap | Resolution | Key Documents Added |
|---|---|---|
| Health Summary configuration | Resolved | gmts_2_7_p133_um.docx, hsum_2_7_tm.docx |
| Allergy verification workflow | Resolved | gmra_4_0_um.docx, gmra_4_0_tm.docx |
| Vitals entry and configuration | Resolved | vitl5_um.docx, vitl5_tm.docx |
| Lab package file structure | Resolved | lab5_2tm.docx (LR\*5.2\*570), lab5_2um.docx |
| TIU document infrastructure | Resolved (new addition) | tiutm.docx, tiuum.docx, tiuim.docx |
| Consult file structure | Resolved (new addition) | constm.docx, consum.docx, consifc.docx |
| Pharmacy file structure | Resolved (new addition) | pso_7_tm.docx, psj_5_0_p447_tm.docx + UMs |
| Scheduling/SD architecture | Resolved (new addition) | sd_pims_tm.docx |
| Radiology and Surgery reports | Resolved (new addition) | ra5_0tm/um/ag, sr_3_tm/um |

Remaining gaps (not yet in corpus):

| Topic | Recommended Documents |
|---|---|
| BCMA administration records affecting inpatient medication display | psb_3_0_tm.docx (PSB TM) |
| VistA Imaging integration with CPRS (images in reports) | MAG TM/UM |
| Mental Health instruments in Reports | YS package documentation |
| PCMM provider team display in CPRS header | PCMM UM/PCMM Web |

---

## Primary Sources

| Document | Filename | Patch Level |
|---|---|---|
| CPRS User Manual: GUI Version | cprsguium.docx | OR\*3.0\*626 |
| CPRS Technical Manual: GUI Version | cprsguitm.docx | OR\*3.0\*636 |
| CPRS Setup Guide | cprssetup.docx | — |
| CPRS Technical Manual: List Manager Version | cprslmtm.docx | OR\*3.0\*626 |
| TIU Technical Manual | tiutm.docx | TIU\*1.0\*372 |
| TIU Clinical Coordinator & User Manual | tiuum.docx | TIU\*1.0\*364 |
| TIU/ASU Implementation Guide | tiuim.docx | — |
| Consult/Request Tracking Technical Manual | constm.docx | GMRC\*3.0\*189 |
| Consult/Request Tracking User Manual | consum.docx | GMRC\*3.0\*206 |
| Inter-Facility Consults Implementation Guide | consifc.docx | — |
| SD PIMS Technical Manual | sd_pims_tm.docx | SD PIMS v5.3 |
| Outpatient Pharmacy Technical Manual | pso_7_tm.docx | PSO\*7\*766 |
| Outpatient Pharmacy Pharmacist's User Manual | pso_7_pharm_um.docx | PSO\*7\*795 |
| Outpatient Pharmacy Manager's User Manual | pso_7_man_um.docx | PSO\*7\*795 |
| Inpatient Medications Technical Manual | psj_5_0_p447_tm.docx | PSJ\*5.0\*447 |
| Inpatient Medications Pharmacist's User Manual | PSJ_5_0_p447_PHAR_UM.docx | PSJ\*5\*447 |
| Inpatient Medications Nurse's User Manual | PSJ_5_0_NURSE_UM.docx | PSJ\*5\*423 |
| Laboratory Version 5.2 Technical Manual | lab5_2tm.docx | LR\*5.2\*570 |
| Laboratory Version 5.2 User Manual | lab5_2um.docx | — |
| Laboratory Anatomic Pathology User Manual | apump422.docx | LR\*5.2\*422 |
| Laboratory Anatomic Pathology Version 5.2 UM | lab_ap_lr_5_2_ug.docx | — |
| Laboratory Blood Bank ISBT User Guide | lr_52_p267_ug.docx | LR\*5.2\*267 |
| Radiology Version 5 Technical Manual | ra5_0tm.docx | — |
| Radiology Version 5 User Manual | ra5_0um.docx | RA\*5\*216 |
| Radiology Version 5 ADPAC Guide | ra5_0ag.docx | — |
| Surgery User Manual | sr_3_um.docx | SR\*3.0\*205 |
| Surgery Technical Manual | sr_3_tm_r1115.docx | SR\*3\*184 |
| DSS Extracts Technical Manual | ecx_3_tm.docx | ECX\*3\*196 |
| Health Summary User Manual | gmts_2_7_p133_um.docx | GMTS\*2.7\*133 |
| Health Summary Technical Manual | hsum_2_7_tm.docx | — |
| Problem List User Manual | gmplum.docx | — |
| Adverse Reaction Tracking User Manual | gmra_4_0_um.docx | — |
| Adverse Reaction Tracking Technical Manual | gmra_4_0_tm.docx | — |
| Vitals/Measurements User Manual | vitl5_um.docx | — |
| Vitals/Measurements Technical Manual | vitl5_tm.docx | — |
| Clinical Reminders Technical Manual | pxrm_2_4_tm.docx | — |
| ACR Technical Manual | acr_p_pimstm.docx | — |
