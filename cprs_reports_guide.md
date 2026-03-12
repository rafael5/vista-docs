---
title: "CPRS Clinical Information Views — Multiple Views of the Same Patient Data"
packages: ["OR (CPRS)", "GMTS", "GMPL", "GMRA", "GMRV"]
vdl_sources: ["prt_ug_r.docx", "prt_tm_r.docx", "hsum_2_7_um.docx", "hsum_2_7_tm.docx", "gmts_2_7_p133_um.docx", "vitl5_um.docx", "vitl5_tm.docx", "gmplum.docx", "gmra_4_0_um.docx", "or_3_*_setup*.docx"]
audience: developer-implementer
compiled: 2026-03
synthesis_policy: "VDL-sourced content unmarked. Inferred content marked [SYNTHESIS]. Multi-view analytical insights marked [MULTI-VIEW INSIGHT]. Corpus gaps marked [GAP]."
status: draft
---

# CPRS Clinical Information Views
## Multiple Views of the Same Patient Data
### Developer & Implementer Reference Guide

> **Source policy:** Content derived from VA VDL documents is unmarked. Content synthesised from general VistA knowledge is marked **[SYNTHESIS]**. Analytical observations about the multi-view architecture are marked **[MULTI-VIEW INSIGHT]**. Corpus gaps are marked **[GAP]**.

---

## 1. The Multi-View Architecture of CPRS

CPRS is designed around a fundamental principle: the same patient data is surfaced in multiple places, at multiple levels of granularity, through multiple interaction modes. This is not redundancy — it is intentional clinical design. A clinician reviewing a patient may need a quick snapshot on the Coversheet, a historical trend on the Reports tab, a graph for pattern recognition, and a structured printable summary — all derived from the same underlying VistA file records.

Understanding this multi-view architecture is essential for implementers configuring CPRS, for developers extending it, and for anyone building data extraction pipelines from VistA.

### 1.1 The Four Surface Types

| Surface | Location in CPRS | Interaction Mode | Primary Use |
|---|---|---|---|
| Coversheet panes | Default tab on patient open | Read-only snapshot, clickable | Quick situational awareness |
| Reports tab (text) | Reports tab — ad hoc queries | Parameterised query, scrollable text | Historical review, detail |
| Reports tab (graph) | Reports tab — graphing | Interactive graph with zoom/overlay | Trend analysis, pattern recognition |
| Health Summary | Reports tab or standalone | Structured printable component-based report | Structured handoff, consult, discharge |

> **[MULTI-VIEW INSIGHT]:** The same lab value — e.g. a serum creatinine — appears simultaneously in: (1) the Coversheet Labs pane as the most recent result, (2) the Reports tab under Lab Results for historical context, (3) the Graph view as a trend line, and (4) a Health Summary if a lab component is configured. Each surface is appropriate for a different clinical task.

### 1.2 Data Ownership Map — Who Owns What

Each pane in CPRS pulls from a specific owning package in VistA. Implementers must understand ownership to correctly configure, troubleshoot, and extend each view:

| Clinical Domain | VistA Package | Primary File(s) | CPRS Surface(s) |
|---|---|---|---|
| Active medications | PSO/PSJ (Pharmacy) | PRESCRIPTION #52, NON-VA MED #55.05 | Coversheet, Reports, Graph |
| Lab results | LA (Lab) | LAB DATA #63 | Coversheet, Reports, Graph |
| Vital signs | GMRV (Vitals) | VITAL MEASUREMENT #120.5 | Coversheet, Reports, Graph |
| Allergies/ADRs | GMRA | PATIENT ALLERGIES #120.8 | Coversheet, Reports |
| Problem list | GMPL | PROBLEM #9000011 | Coversheet, Reports |
| Appointments | SD (Scheduling) | APPOINTMENT #2.98 in PATIENT #2 | Coversheet, Reports |
| Clinical reminders | PXRM | REMINDER DEFINITION #811.9 | Coversheet (drawer) |
| Progress notes / TIU | TIU | TIU DOCUMENT #8925 | Coversheet (recent), Reports |
| Orders | OR (CPRS) | ORDERS #100 | Coversheet (active orders), Reports |
| Consults | GMRC | REQUEST/CONSULTATION #123 | Coversheet, Reports |
| Health Summary | GMTS | HEALTH SUMMARY TYPE #142 | Reports tab, standalone |
| Discharge summaries | TIU | TIU DOCUMENT #8925 (type=DS) | Reports |

---

## 2. Coversheet — The Situational Awareness Layer

The CPRS Coversheet is the first screen displayed when a patient is selected. It provides a configurable snapshot across multiple clinical domains simultaneously. Each pane is independent, pulling from its owning package.

### 2.1 Coversheet Panes — Standard Configuration

| Pane | Data Shown | Owning Package | Key RPC |
|---|---|---|---|
| Active Problems | Problem list items (Active status) | GMPL | ORWPT PROB LIST |
| Allergies / ADRs | Active allergy/ADR entries | GMRA | ORWPT ALLERGY |
| Postings | CWAD flags (Crisis, Warning, Allergy, Directive) | GMRA / OR | ORWPT CWAD |
| Active Medications | Active Rx — outpatient, inpatient, non-VA, IV | PSO / PSJ | ORWPS COVER |
| Clinical Reminders | Due/applicable reminders for this patient | PXRM | PXRM REMINDERS APPLICABLE |
| Recent Lab Results | Most recent results per test within lookback | LA | ORWRP REPORT TEXT |
| Vitals | Most recent vital signs | GMRV | GMV LATEST VM |
| Appointments | Upcoming and recent visits | SD | ORWPT APPTLST |
| Visit Information | Current visit context | OR / SD | ORWPT VISIT SELECT |

### 2.2 Active Medications on the Coversheet

The Active Medications pane aggregates across all medication types. This is a cross-pharmacy view — the most complex aggregation on the Coversheet:

- Outpatient Rx from PRESCRIPTION file (#52) — PSO namespace
- Inpatient medications from PHARMACY PATIENT (#55) — PSJ namespace
- Non-VA medications (documented only) from NON-VA MEDICATION STATEMENT (#55.05)
- IV medications from IV file — PSJ namespace
- Pending (unsigned) orders from ORDERS (#100) — OR namespace

> **[MULTI-VIEW INSIGHT]:** The Coversheet Medications pane shows ALL active medications regardless of source. The Reports tab Medications report can filter by type, date range, and status. The Graph can plot a single medication's dose/fill history. Three different entry points into the same pharmacy data — each appropriate for a different clinical question.

### 2.3 Lab Results on the Coversheet

The Recent Lab Results pane is controlled by two parameters that implementers must configure per site:

| Parameter | File # | Description |
|---|---|---|
| ORWRP REPORT LIST | 8989.51 | Configures which lab panels appear on the Coversheet |
| ORWRP LEGACY VIEWER LABEL | 8989.51 | Controls display label for legacy lab viewer link |
| OR REPORT DATE RANGE INPT | 8989.51 | Date lookback for inpatient lab results on Coversheet |
| OR REPORT DATE RANGE OUTPT | 8989.51 | Date lookback for outpatient lab results on Coversheet |

> **NOTE:** If the Coversheet lab pane is blank for a patient who has recent labs, the most common cause is that the lab tests are not included in ORWRP REPORT LIST at the system/division level, or the date range parameters are too narrow.

### 2.4 Vitals on the Coversheet

The Coversheet Vitals pane calls `GMV LATEST VM`, which returns the single most recent value per vital type. The source is VITAL MEASUREMENT file (#120.5) owned by GMRV.

| Vital Type | Normal Display |
|---|---|
| Blood Pressure | Systolic/Diastolic mmHg |
| Temperature | Degrees F (or C per site config) |
| Pulse | Beats per minute |
| Respirations | Breaths per minute |
| Weight | Pounds (or kg per site config) |
| Height | Inches (or cm per site config) |
| Pulse Oximetry | SpO2 percentage |
| Pain Score | 0–10 scale |

> **[MULTI-VIEW INSIGHT]:** The Coversheet shows only the most recent vital. The Reports tab Vital Signs report shows a date-range history in text. The Graph shows a trend line for any vital over any date range with configurable overlay. Same VITAL MEASUREMENT #120.5 data — three completely different clinical uses.

---

## 3. Reports Tab — The Historical Review Layer

The CPRS Reports tab provides parameterised access to historical clinical data. Unlike the Coversheet (which shows the current snapshot), the Reports tab allows date-range queries, sorting, and filtering. It is the primary tool for clinical review over time.

### 3.1 Report Categories

The Reports tab is organised into categories. Each category contains individual reports. The categories and their contents are configurable via `ORWRP REPORT LIST`:

| Category | Key Reports | Data Source Package |
|---|---|---|
| Clinical Reports | Lab Results, Microbiology, Blood Bank, Anatomic Path | LA (Lab) |
| Vital Signs/Measurements | Vitals — date range, graph view | GMRV |
| Medications | Outpatient Rx, Inpatient, Non-VA, IV, All Meds | PSO, PSJ |
| Allergies | Allergy/ADR list with dates and reactions | GMRA |
| Problem List | Active/inactive problems with onset/resolution dates | GMPL |
| Visits/Admissions | Clinic visits, hospital admissions, discharge summaries | SD, MAS |
| Progress Notes | Notes by date range, author, type | TIU |
| Consults | Consult requests and results | GMRC |
| Surgery | Operative reports | SR |
| D/C Summaries | Inpatient discharge summaries | TIU |
| Health Summaries | Configured GMTS health summary types | GMTS |
| Remote Data | Data from other VA facilities via HDR/VLER | HDR/VLER |

### 3.2 Medications — Multiple Report Views

Medications illustrate the multi-view principle most clearly. From the Reports tab, a clinician can access the same medication data through several lenses:

| Report Name | What It Shows | Key Filter Options |
|---|---|---|
| Outpatient Medications | Outpatient Rx history — active, expired, discontinued | Date range, status, drug name |
| Inpatient Medications | Inpatient MAR — scheduled and PRN doses | Date range, ward, drug |
| Non-VA Medications | Documented non-VA/OTC medications | Date range |
| IV Medications | IV admixtures and solutions | Date range, type |
| All Medications | Combined view across all types | Date range, status |
| Medication Administration History | Actual administration records (MAR) | Date range, drug |

> **[MULTI-VIEW INSIGHT]:** The 'All Medications' report is the most important for medication reconciliation — it aggregates across all pharmacy sub-systems. The Coversheet shows only currently active meds. A patient may have recently expired Rx that are clinically relevant — only visible in the Reports tab with a date range extension.

### 3.3 Lab Results — Multiple Report Views

Laboratory results are available in several report formats from the Reports tab, each providing different analytical value:

| Report/View | Format | Best Used For |
|---|---|---|
| Lab Results | Chronological text list — all results in date range | Reviewing recent labs in sequence |
| Most Recent Lab Results | Most recent value per test — snapshot format | Quick review without date scanning |
| Lab Results (cumulative) | Columnar — dates as columns, tests as rows | Tracking trends across multiple draws |
| Microbiology | Culture results, sensitivities, gram stains | Infection management |
| Blood Bank | Transfusion history, type and screen | Pre-procedure review |
| Anatomic Pathology | Surgical pathology, cytology reports | Oncology / diagnostic review |
| Lab Graph (via Graph tab) | Visual trend line per test | Pattern recognition over time |

> **[MULTI-VIEW INSIGHT]:** The Coversheet shows one lab value (most recent). The Reports Lab Results shows all values in a date range as a list. The Cumulative report pivots to show multiple time points side by side for the same tests. The Graph plots the same values visually. A nephrologist tracking CKD progression needs all four views — each for a different clinical task.

### 3.4 Vital Signs — Text vs. Graph Views

The GMRV package surfaces vitals in two fundamentally different modes within the Reports tab:

| Mode | Format | Source RPC | Best Used For |
|---|---|---|---|
| Vital Signs report (text) | Date-ordered list of all vital types and values | ORWRP REPORT TEXT with GMRV template | Documentation review, exact values |
| Vital Signs graph | Interactive graph — one vital per series | GMV GRAPH | Trend analysis, pattern recognition |
| Vital Signs (entered in error) | Shows voided vital entries | ORWRP REPORT TEXT | Audit, data quality review |

> **NOTE:** Vitals entered in error remain in VITAL MEASUREMENT #120.5 with a REASON ENTERED IN ERROR flag. The standard Coversheet and Reports views filter these out. Use the 'Entered in Error' report specifically to audit data quality.

---

## 4. CPRS Graphing — The Trend Analysis Layer

The CPRS Graph view provides an interactive visual representation of time-series clinical data. It is accessible via the Reports tab and from individual result displays. Multiple data types can be overlaid on the same graph.

### 4.1 Data Types Supported in CPRS Graphing

| Data Type | Source Package | Source File | RPC |
|---|---|---|---|
| Lab results (individual tests) | LA | LAB DATA #63 | ORWRP REPORT TEXT (graph variant) |
| Vital signs | GMRV | VITAL MEASUREMENT #120.5 | GMV GRAPH |
| Medications (fill/dose timeline) | PSO | PRESCRIPTION #52 | ORWPS GRAPH |
| Blood pressure (systolic/diastolic) | GMRV | VITAL MEASUREMENT #120.5 | GMV GRAPH |
| Weight | GMRV | VITAL MEASUREMENT #120.5 | GMV GRAPH |
| Blood glucose | LA | LAB DATA #63 | ORWRP REPORT TEXT |
| HbA1c | LA | LAB DATA #63 | ORWRP REPORT TEXT |

### 4.2 Graph Configuration Parameters

| Parameter | File # | Description |
|---|---|---|
| ORWGRPC FROMEVENT | 8989.51 | Starting event for graph date range |
| ORWGRPC TOEVENT | 8989.51 | Ending event for graph date range |
| ORWGRPC ALLSOURCES | 8989.51 | Include all data sources in graph (including remote) |
| ORWGRPC MAX GRAPHS | 8989.51 | Maximum number of simultaneous graph series |
| ORWGRPC PUBLICREMOTE | 8989.51 | Include remote VA facility data in graphs |
| ORWGRPC AUTOSAVE | 8989.51 | Auto-save graph settings per user |

> **[MULTI-VIEW INSIGHT]:** CPRS graphing is the only view that can overlay multiple data types on the same axis — for example, plotting HbA1c alongside weight and medication fill dates for a diabetic patient. This is not possible in text-based Reports views. The graph surfaces relationships that are invisible in tabular data.

---

## 5. Health Summary (GMTS) — The Structured Summary Layer

Health Summary is a component-based report engine that produces structured, printable patient summaries. Unlike the ad hoc Reports tab, Health Summary uses pre-configured HEALTH SUMMARY TYPE definitions to produce standardised outputs.

### 5.1 Package Identity

| Attribute | Value |
|---|---|
| Package name | Health Summary |
| Namespace | GMTS |
| Current version | GMTS\*2.7 |
| Key file | HEALTH SUMMARY TYPE #142 |
| Component file | HEALTH SUMMARY COMPONENTS #142.1 |
| VDL source docs | hsum_2_7_um.docx, gmts_2_7_p133_um.docx, hsum_2_7_tm.docx |

### 5.2 Health Summary Architecture

A Health Summary Type is an ordered list of components. Each component corresponds to a specific data extraction from a VistA package. The same underlying data visible on the Coversheet and Reports tab is formatted into a structured printable output:

| Component Category | Example Components | Source Package |
|---|---|---|
| Medications | Active Outpatient Meds, Active Inpatient Meds, Non-VA Meds | PSO, PSJ |
| Lab results | Selected Lab Tests, Chemistry/Hematology, Microbiology | LA |
| Vital signs | Vital Signs, Blood Pressure, Weight | GMRV |
| Problem list | Active Problems, Inactive Problems | GMPL |
| Allergies | Adverse Drug Reactions, Allergies | GMRA |
| Clinical notes | Brief Clinical Notes, Progress Notes | TIU |
| Appointments | Outpatient Encounters, Future Appointments | SD |
| Immunizations | Immunizations | PX (PCE) |
| Reminders | Reminder Summary | PXRM |
| PCE data | Health Factors, Patient Education, Exams | PX (PCE) |
| Consults | Consult/Request Results | GMRC |

### 5.3 Key HEALTH SUMMARY TYPE Fields (#142)

| Field # | Name | Description |
|---|---|---|
| .01 | NAME | Summary type name — displayed in CPRS Reports tab |
| .02 | TITLE | Printed header on the summary output |
| .03 | SUPPRESS PRINT OF DISCLAIMER | Suppress standard VA disclaimer on print |
| 1 | COMPONENTS | Multiple sub-file — ordered list of components with parameters |
| 100 | OWNER | User who created/owns this summary type |
| 101 | LOCK | Security key required to use this summary type |

> **NOTE:** Health Summary Types with CLASS=NATIONAL are distributed by VA patches and should not be modified locally. Create site-specific types by copying a national type and setting CLASS=LOCAL. Changes to national types are overwritten on the next applicable patch install.

### 5.4 Health Summary in CPRS Reports Tab

Health Summary types appear in the Reports tab under the 'Health Summaries' category. The RPC `ORWRP REPORT TEXT` with a health summary template parameter drives the CPRS display. Configuration steps for implementers:

- Create or select a HEALTH SUMMARY TYPE in file #142
- Add the type to the `ORWRP REPORT LIST` parameter at system or division level
- Set the `GMTS HS REQUIRE USER OK` parameter if user confirmation before printing is required
- Assign the `GMTS MANAGER` security key to staff authorised to create/edit Health Summary types
- Test with `GMTS USER` option before deploying to clinical users

---

## 6. Multi-View Scenarios — The Same Data, Multiple Surfaces

This section traces specific clinical data items through all available CPRS views. This is the core of the multi-view architecture — understanding exactly where each piece of data appears, in what form, and through what technical path.

### 6.1 Scenario: Current Medications

> **[MULTI-VIEW INSIGHT]:** A clinician wants to review a patient's current medications. Depending on their clinical task, they will use a different CPRS surface.

| Clinical Task | CPRS Surface | What They See | Technical Path |
|---|---|---|---|
| Quick check — is patient on warfarin? | Coversheet — Active Medications pane | All active meds, scrollable list | ORWPS COVER RPC → PSO/PSJ files |
| Medication reconciliation — all meds including recent fills | Reports → All Medications | Active + expired + non-VA by date range | ORWRP REPORT TEXT → PSO #52, PSJ #55 |
| Are they actually taking it? Fill history? | Reports → Outpatient Medications | Rx with each fill date and days supply | ORWRP REPORT TEXT → PSO #52 |
| Dose trend over time (e.g. insulin adjustment) | Graph → Medications | Timeline of fills/doses as bar chart | ORWPS GRAPH RPC → PSO #52 |
| Structured handoff — next provider needs full picture | Health Summary with Meds component | Formatted printable medication section | ORWRP REPORT TEXT → GMTS #142 → PSO/PSJ |

### 6.2 Scenario: Blood Pressure Monitoring

> **[MULTI-VIEW INSIGHT]:** A clinician managing hypertension needs to review a patient's blood pressure history at multiple levels of detail.

| Clinical Task | CPRS Surface | What They See | Technical Path |
|---|---|---|---|
| Most recent BP at a glance | Coversheet — Vitals pane | Single most recent BP reading | GMV LATEST VM → VITAL MEASUREMENT #120.5 |
| Last month of BP readings — exact values | Reports → Vital Signs (text) | Date-ordered list of all BP entries | ORWRP REPORT TEXT → GMRV GMTS component |
| 6-month trend — is it improving? | Reports → Vital Signs (graph) | Graph of systolic/diastolic over time | GMV GRAPH RPC → VITAL MEASUREMENT #120.5 |
| BP alongside medication changes | Graph — overlay BP + Med fills | BP trend with medication start/stop markers | GMV GRAPH + ORWPS GRAPH overlay |
| Structured summary for referral | Health Summary with Vital Signs component | Formatted vital sign section in printable output | ORWRP REPORT TEXT → GMTS #142 → GMRV |

### 6.3 Scenario: Diabetes Management (Labs + Meds + Vitals)

> **[MULTI-VIEW INSIGHT]:** The most powerful use of CPRS multi-view is for chronic disease management where multiple data streams must be correlated.

| Clinical Task | CPRS Surface | Data Shown | Packages Involved |
|---|---|---|---|
| Quick glucose check at appointment | Coversheet — Recent Labs | Most recent glucose and HbA1c | LA (Lab) |
| HbA1c trend over 2 years | Reports → Lab Results (cumulative) | HbA1c in columns by date | LA |
| Glucose + HbA1c + weight overlay | Graph — multi-series | Three trend lines on one graph | LA + GMRV |
| Medication adjustments alongside glucose | Graph — overlay with insulin fills | Glucose trend + medication timeline | LA + PSO |
| Problem list — is DM documented? | Coversheet → Active Problems or Reports → Problem List | Problem list with ICD codes and onset dates | GMPL |
| Full DM management summary | Health Summary — custom DM type | Labs, meds, vitals, problems — structured | GMTS → LA, PSO, GMRV, GMPL |

### 6.4 Scenario: Allergy Review

| Clinical Task | CPRS Surface | What They See | Technical Path |
|---|---|---|---|
| Does patient have penicillin allergy? | Coversheet — Postings / Allergies pane | CWAD allergy flag + active allergy list | ORWPT CWAD + ORWPT ALLERGY → #120.8 |
| Full allergy history with reactions | Reports → Allergies / ADR | Date, causative agent, reaction, severity | ORWRP REPORT TEXT → GMRA #120.8 |
| Health summary allergy section | Health Summary — Allergy component | Formatted allergy section for handoff | GMTS → GMRA #120.8 |

---

## 7. Implementation Reference

### 7.1 Key RPCs for Reports and Graphing

| RPC Name | Purpose | Parameters |
|---|---|---|
| ORWRP REPORT TEXT | Primary report retrieval RPC — drives most Reports tab content | Patient DFN, report name, date range, max occurrences |
| ORWRP REPORT LIST | Returns list of available reports for Reports tab menu | None (returns configured list) |
| GMV LATEST VM | Returns most recent vital for each vital type | Patient DFN, vital type list |
| GMV GRAPH | Returns vital sign data formatted for graphing | Patient DFN, vital type, date range |
| ORWPS COVER | Returns active medications for Coversheet pane | Patient DFN, visit |
| ORWPS GRAPH | Returns medication fill data for graphing | Patient DFN, date range |
| ORWPT ALLERGY | Returns allergy/ADR list | Patient DFN |
| ORWPT CWAD | Returns CWAD flag summary for Postings pane | Patient DFN |
| ORWPT PROB LIST | Returns problem list entries | Patient DFN, status filter |
| PXRM REMINDERS APPLICABLE | Returns applicable reminders for Coversheet drawer | Patient DFN, location, user |

### 7.2 Key Configuration Parameters for Reports

| Parameter | File # | Scope | Effect |
|---|---|---|---|
| ORWRP REPORT LIST | 8989.51 | System/Division/User | Controls which reports appear in Reports tab and their order |
| ORWRP HEADER TEXT | 8989.51 | System | Custom header on printed reports |
| OR REPORT DATE RANGE INPT | 8989.51 | System/Division | Default date lookback for inpatient reports |
| OR REPORT DATE RANGE OUTPT | 8989.51 | System/Division | Default date lookback for outpatient reports |
| ORWRP LEGACY VIEWER LABEL | 8989.51 | System | Label for legacy lab viewer link on Coversheet |
| ORWGRPC MAX GRAPHS | 8989.51 | System/Division | Maximum graph series — performance control |
| ORWGRPC ALLSOURCES | 8989.51 | System | Include HDR/VLER remote data in graphs |
| GMTS HS REQUIRE USER OK | 8989.51 | System/Division | Require confirmation before Health Summary print |

### 7.3 Health Summary Key Setup Steps

- `GMTS MANAGER` security key — required for creating/editing Health Summary types
- HEALTH SUMMARY TYPE file #142 — define components, order, date ranges, max occurrences per component
- `ORWRP REPORT LIST` parameter — add new HS types to the Reports tab menu
- Test via roll-and-scroll using `GMTS USER` option before CPRS deployment
- GMTS\*2.7\*133 (gmts_2_7_p133_um.docx) — review patch-specific component changes before upgrading

---

## 8. VDL Source Coverage Map

| Section | Primary VDL Source(s) | Coverage Status |
|---|---|---|
| Multi-view architecture overview | prt_ug_r.docx, general CPRS RN series | Synthesised from corpus patterns |
| Coversheet pane structure and RPCs | CPRS RN series (or_3_\*_rn.docx) | Partially synthesised — no CPRS UM in corpus |
| Medications multi-view | CPRS RN series, PSO/PSJ (not in corpus) | Synthesised — PSO/PSJ not in guides corpus |
| Lab results multi-view | CPRS RN series | Synthesised — LA package not in guides corpus |
| Vital signs views | vitl5_um.docx, vitl5_tm.docx | VDL sourced for GMRV detail |
| Graph configuration parameters | or_3_0_405_setup_r.docx, or_3_0_498_setup_r.docx | VDL sourced |
| Health Summary architecture | hsum_2_7_um.docx, hsum_2_7_tm.docx, gmts_2_7_p133_um.docx | VDL sourced |
| Health Summary components | hsum_2_7_um.docx | VDL sourced |
| Problem list | gmplum.docx, gmpl_2_0_49_tm.docx | VDL sourced |
| Allergies | gmra_4_0_um.docx, gmra_4_0_tm.docx | VDL sourced |
| RPC reference | prt_tm_r.docx, CPRS TM (not in corpus) | Partially synthesised |
| Multi-view clinical scenarios | Cross-package synthesis | Synthesised — analytical content |

> **[GAP]:** The CPRS GUI User Manual and CPRS Technical Manual are not in the guides corpus — only the Provider Role Tool (PRT) sub-manual is available. The CPRS GUI UM is the authoritative reference for Coversheet configuration, Reports tab navigation, and graphing. Request these documents from VDL before finalising any CPRS configuration changes.

> **[GAP]:** Pharmacy (PSO/PSJ), Lab (LA), Scheduling (SD), and Consults (GMRC) packages are not in the guides corpus. Their file structures and RPCs cited in this guide are from general VistA knowledge, not VDL source documents. Verify against those packages' own VDL documentation.
