---
title: "VistA / CPRS Architecture & Function Reference"
description: "Comprehensive, corpus-referenced guide to VistA system architecture, CPRS clinical surfaces, package integrations, and developer internals"
corpus: "152-document VDL corpus"
date: "2026-03"
packages: [OR, LR, PSO, PSJ, PSB, RA, GMRV, GMRC, TIU, GMRA, GMPL, PXRM, PX, GMTS, MAG, YS, PCMM, WEBP, SR, ACR, SD, ECX, LRAP, LRBB]
gaps: [ADT, ASU, PSS, MD, XU, PSN, XWB, NUR, LEDI]
repo: "https://github.com/rafael5/vista-docs"
---

# VistA / CPRS Architecture & Function Reference

> Synthesized from 152-document VDL corpus · March 2026  
> Corpus sources: `cprsguitm.docx`, `cprssetup.docx`, and 150 additional TM/UM/ICD documents across 24 packages  
> Knowledge gaps are explicitly annotated with **⚠ GAP** throughout.

---

## PART I — SYSTEM ARCHITECTURE

---

## 1. What VistA Is

VistA (Veterans Information Systems and Technology Architecture) is the Veterans Health Administration's clinical information system — a collection of ~190 active software packages running on a shared MUMPS (M) runtime and database that together constitute the complete electronic health record environment for the VA healthcare system.

VistA is not a monolithic EHR application. It is a federated ecosystem of packages, each owning its own namespace, files, globals, routines, and documentation, loosely coupled through four integration mechanisms: VA FileMan (shared data schema), RPC Broker (synchronous GUI transport), HL7 (asynchronous event bus), and DBIAs (formal inter-package contracts).

CPRS (Computerized Patient Record System) is the primary clinician-facing Windows GUI for VistA. From the user's perspective, CPRS is the EHR. From the system's perspective, CPRS is a thin rendering client that aggregates data owned by ~20 backend packages, retrieved entirely through the RPC Broker transport layer.

### 1.1 Scale and Scope

From the full VA VDL inventory (March 2026):
- 396 total applications (192 active, 188 archived, 16 decommissioned)
- 8,276 VDL documents (4,817 PDF, 3,452 DOCX, 7 DOC)
- Sections: Clinical (~213 apps), Infrastructure (69), Financial-Administrative (68), VistA/GUI Hybrids (45)
- Core clinical surface covered by this guide: 24 packages, 152 source documents

### 1.2 The Five Structural Laws

> Understanding these five constraints is sufficient to reason correctly about any VistA integration question.

1. **No cross-package direct global reads without a DBIA.** Package A cannot read `^GLOBALB` without an explicit Database Integration Agreement with Package B. All inter-package data access is contracted.

2. **FileMan is the schema.** All VistA data lives in FileMan files. The data dictionary defines field types, cross-references, and access controls. Global notation follows from the file definition — not the other way around.

3. **RPC Broker is the only synchronous client transport.** CPRS communicates with VistA exclusively through RPC calls over the Broker TCP connection. There is no direct database access from the client, no REST API, no SOAP service — just RPCs.

4. **HL7 is the asynchronous backbone.** Events between packages (lab results arriving, medication administrations, scheduling updates) flow through the VistA HL7 engine. RPC is client-pull; HL7 is server-push between packages.

5. **Context option = authorized RPC surface.** What RPCs a GUI session can call is defined entirely by its context option. The context option is a security boundary, not a configuration file.

---

## 2. VistA Runtime Model

### 2.1 MUMPS / M Language and Global Database

VistA runs on a MUMPS (M) runtime. The language is interpreted, operates without type enforcement, and writes directly to a persistent hierarchical global database with no separate DBMS process. Globals are sparse, multi-level persistent arrays:

```mumps
^LR(63, patientIEN, "CH", inverseDate, testIEN) = value
^OR(100, orderIEN, 0) = orderData
^TIU(8925, docIEN, 0) = docHeader
```

Routines (code) are stored in the database alongside data. Each package owns a namespace (2–5 letters) and one or more global roots matching that namespace. The system is single-process per user session; concurrency is handled at the OS level by M jobbing and application-level locking primitives.

### 2.2 VA FileMan (DI Namespace)

FileMan is the schema and data-access layer for all VistA data. It provides:

- **Data Dictionary**: every file has typed fields with `.01` (name/key) through N. Field types: free text, date, pointer, set of codes, word processing, multiple (sub-file).
- **Cross-references**: B (standard lookup by name/key), C, D, and custom computed cross-references. Trigger cross-references fire on update.
- **Access codes**: per-file, per-field access control using `@`, `#`, `^` codes for read/write/delete.
- **DBS APIs (programmatic access)**: `GETS^DIQ` (retrieve), `FILE^DIE` (update), `UPDATE^DIE` (update with locking), `LIST^DIC` (list), `FIND^DIC` (find). These are the correct APIs for all programmatic cross-package access.
- **Classic APIs (interactive)**: `^DIC` (lookup), `^DIE` (input), `^DIP` (print) — the older terminal-session API.

FileMan files are globally mapped: file #63 → `^LR`, file #8925 → `^TIU(8925,`. The mapping is defined in the file's data dictionary header node.

### 2.3 Kernel (XU Namespace)

Kernel is the VistA operating environment. It provides user authentication, session management, security keys, menus, background job scheduling (TaskMan), internal messaging (MailMan), and the Parameter system (XPAR).

Key Kernel constructs:

- **DUZ**: the user's internal entry number (IEN) in NEW PERSON file #200 — the identity anchor for all security and attribution in VistA.
- **Security keys**: named flags held by users, checked via `$G(^XUSEC("KEY NAME",DUZ))`. Examples: `ORES` (order signer), `ORELSE` (limited order entry), `PSB MANAGER` (BCMA manager), `MAG DELETE` (image deletion).
- **Context option**: a menu OPTION (#19) that defines which RPCs a GUI session may call. Setting the context option is step 2 of the broker authentication flow. Without a valid context option, no RPCs can be called.
- **TaskMan**: background job scheduler. Scheduled tasks are queued in `^%ZTSK`. Examples: `PSB PX BCMA2PCE TASK` (nightly BCMA→PCE immunization sync), PCMM background filer.

> **⚠ GAP — XU (Kernel)**: `krn_8_0_tm.docx` (140 active VDL docs) not yet in corpus. The above is derived from cross-references in other packages' documentation. First-party Kernel documentation would add: Kernel API reference, TaskMan API, MailMan API, full security key grant mechanics, and electronic signature internals.

### 2.4 RPC Broker (XWB Namespace)

The RPC Broker is the only synchronous transport between GUI clients and VistA. TCP-based, typically port 9200 (site-configured).

#### Authentication and Session Flow

1. Client connects to VistA TCP listener
2. Client authenticates: access code/verify code exchange → VistA returns DUZ
3. Client sets context option (e.g., `OR CPRS GUI CHART`)
4. Kernel validates option exists, user has access, option is enabled
5. Client calls RPCs by name + parameters → VistA executes M `routine^tag` → returns result
6. Client closes connection

#### RPC Authorization Model

An RPC call is authorized if: (1) the RPC is listed in the context option's allowed RPC list, AND (2) the user holds the required security key (if defined). Unauthorized calls are rejected by the Broker before execution.

#### RPC Registration

RPCs are registered in **REMOTE PROCEDURE file #8994**. Each RPC record specifies: name, routine, tag, return value type (`SINGLE VALUE`, `ARRAY`, `WORD PROCESSING`, `GLOBAL ARRAY`), and required option context. The **784-row RPC table** in `cprsguitm.docx` is the definitive enumeration of all RPCs called by CPRS.

> **⚠ GAP — XWB (RPC Broker)**: `xwb_1_1_tm_r.docx` not yet in corpus. Wire protocol details, connection multiplexing, error code taxonomy, and the full Delphi client library API are absent.

### 2.5 HL7 Messaging

HL7 is the asynchronous event bus within VistA. HL7 and RPC Broker serve distinct roles:

| Dimension | RPC Broker | HL7 |
|---|---|---|
| Direction | Client-initiated (pull) | Event-driven (push) |
| Timing | Synchronous — client waits | Asynchronous — queued and delivered |
| Initiator | GUI client (CPRS, BCMA, MHA...) | VistA package |
| Receiver | VistA M server | Another package or external system |
| Examples | CPRS requesting lab results | Lab result filing, BCMA admin event |

Key HL7 flows:
- **Lab results**: Analyzer → `ORU^R01` → VistA HL7 engine → `^LR(63,`. CPRS is not in this path — it reads results after they are filed.
- **BCMA administration**: PSB sends `RAS^O17`. MSH: `MSH^~|&^PSB HL7 SRV^^PSB HL7 SUB^^{datetime}^^RAS~O17^{msgid}^P^2.4`
- **Radiology order status**: RA → `ORR^O02` → CPRS order status update
- **Workload**: PCE encounters → HL7 → ECX/DSS workload reporting

### 2.6 Parameter System (XPAR)

Parameters are the VistA configuration store — they replace hard-coded site-specific logic. Parameters are defined in PARAMETER DEFINITION (#8989.51) and stored in PARAMETER (#8989.5).

**Precedence hierarchy** (highest to lowest):
1. User
2. Location (clinic or ward)
3. Service
4. Division
5. System (site-wide default)
6. Package (built-in default)

`cprssetup.docx` is the authoritative reference for all OR/CPRS parameters — 35 tables mapping parameter names to behaviors, covering notifications, order checking, display defaults, alert recipients, and GUI behaviors.

### 2.7 Package System and DBIAs

Each package has a unique 2–5 letter namespace, version number, owned FileMan files, exported options, security keys, and DBIAs. DBIA types:

- **Supported**: calling package may use this entry point
- **Private**: internal use only
- **Restricted**: limited use, case-by-case
- **Custodial**: the owning package defines the terms

### 2.8 Patch System and Versioning

Patches are the unit of change. Format: `NAMESPACE*VERSION*PATCH_NUMBER`

- `OR*3.0*387` — CPRS (OR) v3.0, patch 387 (adds PACT header display)
- `PSB*3*131` — BCMA (PSB) v3, patch 131
- `YS*5.01*191` — Mental Health (YS) v5.01, patch 191
- `SD*5.3*603` — Scheduling/PIMS (SD) v5.3, patch 603 (installs PCMM Web server changes)

Patch history is recorded in revision tables in each Technical Manual. 73 of 152 corpus documents have such tables. This is the only version control record for most packages. Patches are distributed via FORUM and applied via KIDs (Kernel Installation and Distribution System).

---

## PART II — CPRS CLIENT ARCHITECTURE

---

## 3. CPRS Overview

### 3.1 Package Identity

CPRS is the clinician-facing GUI. Its VistA-side package is **OR** (Order Entry/Results Reporting), version 3.0. "CPRS" names the client; "OR" names the VistA package. They are the same entity.

Primary corpus documents:
- `cprsguitm.docx` — CPRS GUI Technical Manual (2,145 headings, 39 tables, **784-row RPC table**)
- `cprsguium.docx` — CPRS GUI User Manual (570 headings)
- `cprssetup.docx` — CPRS Setup Guide (106 headings, 35 parameter tables)
- `cprslmtm.docx` — CPRS List Manager TM (427 headings, 46 tables, 8 RPC tables) — character-based interface

### 3.2 What CPRS Owns

| File # | File Name | Global | Purpose |
|---|---|---|---|
| 100 | ORDER | `^OR(100,` | All CPRS-placed orders |
| 100.8 | ORDER CHECKS | `^ORD(100.8,` | Order check definitions (ORK routines) |
| 100.9 | OE/RR NOTIFICATIONS | `^ORB` | Alert/notification definitions |
| 101 | PROTOCOL | `^ORD(101,` | Event driver protocols |
| 101.41 | ORDER DIALOG | `^ORD(101.41,` | Order entry dialog definitions |

> **CPRS is a rendering client, not a data owner.** Everything it displays — problems, medications, lab results, vitals, consults, notes, images — is owned by other packages and retrieved via RPCs. This is the foundational architectural fact of the CPRS system.

---

## 4. CPRS Display Surfaces

### 4.1 Patient Header Bar

Persistent across all tabs. Displays: patient name, DOB, SSN (last 4), age, ward/clinic, attending provider, and — since `OR*3.0*387` — the PACT team header from PCMM.

PACT header mechanics: text stored in OUTPATIENT PROFILE #404.41 field `.06` (CPRS HEADER TEXT). Populated by routine `SCMCDD1` when team assignments change. Retrieved by RPC `ORWPT1 PRCARE`. Full PACT details window via `ORWPT1 PCDETAIL`. Depends on `SD*5.3*603`.

### 4.2 Coversheet

Default landing view when a patient is loaded. Each component is a separate RPC call:

| Component | Package | File / Global | RPC Family | Notes |
|---|---|---|---|---|
| Active Problems | GMPL | #9000011 `^AUPNPROB` | ORWPCE / GMPL | ICD-coded |
| Allergies/ADRs | GMRA | #120.8 `^GMRD(120.8,` | ORWRP | Feeds order checking |
| Postings / Flags | DG | PATIENT #2 `^DPT` | ORWRP | Patient record flags |
| Active Medications | PSO / PSJ | #52 `^PSRX` / PSJ | ORWPS / ORWRP | Outpt + inpt meds |
| Clinical Reminders | PXRM | `^PXRM` | PXRM RPCs | DUE / NOT DUE status |
| Recent Vitals | GMRV | #120.5 `^GMR(120.5,` | GMRV via ORWRP | Last recorded values |
| Upcoming Appts | SD | Scheduling files | ORWRP | Future appointments |
| Recent Lab Results | LR | #63 `^LR` | ORWRP | Abnormals flagged |
| Med Admin History | PSB (BCMA) | #53.79 `^PSB(53.79,` | PSB COVERSHEET1 | → `PSBMLHS` routine |

### 4.3 Problems Tab

Renders PROBLEM LIST (#9000011) from `^AUPNPROB`. ICD-coded. Write path goes through GMPL package routines. Problems linked to encounter diagnoses (V DIAGNOSIS #9000010.07).

### 4.4 Meds Tab

Aggregates: outpatient prescriptions (PSO, PRESCRIPTION #52), inpatient orders (PSJ), and non-VA medications. Medication Administration History (MAH) from BCMA via `PSB COVERSHEET1` RPC → `PSBMLHS` routine → `^PSB(53.79,`.

### 4.5 Orders Tab

Primary order entry surface. Order sequence:

1. Clinician selects order type → CPRS loads ORDER DIALOG (#101.41) via `ORWDX` RPC
2. Clinician enters parameters → CPRS calls package-specific verification RPCs
3. ORK-namespace routines execute order checks against allergies (#120.8), active meds (#52/PSJ), lab results (#63), drug database (PSS/PSN)
4. Clinician reviews checks, overrides or accepts, signs with e-sig
5. CPRS calls filing RPCs → receiving package creates its record: PSO → PRESCRIPTION #52; RA → RAD/NUC MED ORDERS #70.2; LR → lab order; PSJ → inpatient order
6. ORDER #100 record created and linked to receiving package record via order IEN

### 4.6 Notes Tab

Renders TIU DOCUMENT (#8925) of class PROGRESS NOTES. Users create, edit, sign, co-sign. TIU governs document class hierarchy (#8925.1), signing authority (ASU), addendum logic, and e-sig. Signed documents are immutable; addenda are separate TIU documents linked to parent IEN.

### 4.7 Consults Tab

Renders REQUEST/CONSULTATION (#123) from GMRC. Lifecycle: PENDING → ACTIVE → COMPLETE / DISCONTINUED / CANCELLED. Completed result is TIU DOCUMENT (#8925) of class CONSULT RESULT, linked to consult IEN. Interface defined in `consifc.docx` (39 reference tables).

### 4.8 D/C Summaries Tab

Renders TIU DOCUMENT (#8925) of class DISCHARGE SUMMARY. Same TIU infrastructure as Notes tab.

### 4.9 Labs Tab

Direct view into LAB DATA (#63). Global structure: `^LR(63, patIEN, 'CH', inverseDate, testIEN)` for chemistry/hematology; `'MI'` microbiology; `'SP'` surgical pathology; `'CY'` cytology; `'BB'` blood bank. Retrieved via ORWRP RPCs.

### 4.10 Reports Tab

Configurable multi-view surface. User selects category + date range; CPRS calls the appropriate RPC:

| Report Category | Package | Notes |
|---|---|---|
| Health Summary | GMTS | Configurable component-based; reads LR, PSO, GMRV, TIU, etc. |
| Lab (cumulative, micro, blood bank) | LR | `^LR(63,` all sub-types |
| Radiology reports | RA | `^RA(74,` — camera icon = linked MAG image |
| Clinical Procedures | MD | Cardiology, GI, pulmonology; MD files TIU documents |
| Vital Signs trends | GMRV | `^GMR(120.5,` — trending and graphing |
| Surgery reports | SR | Filed as TIU documents; linked to SR surgical case records |
| Mental Health assessments | YS | `^YTD(601.92,` — MHA scored results |
| Outpatient encounters | PX/PCE | VISIT #9000010 `^AUPNVSIT` |

> **⚠ GAP — MD (Clinical Procedures)**: `md_1_p16_tm.docx` not yet in corpus. MD package file numbers, global structure, RPC surface, and CPRS Reports tab integration are not fully characterized.

### 4.11 Graphing

Graphical trending of vitals (GMRV #120.5), lab results (#63), and medication administration. The server provides data points; the CPRS client renders the graph.

### 4.12 CPRS Tools Menu

Launches external processes. Not a plugin API — CPRS does not manage data flow to/from launched applications except via CCOW context synchronization.

- **VistA Imaging Clinical Display (MAG)** — separate Windows GUI; CCOW-synchronized
- **Mental Health Assistant (MHA) (YS)** — separate Windows GUI; CCOW-synchronized

### 4.13 Notifications (Alerts)

Generated by VistA packages on events (new lab result, new consult, med expiring, unsigned order). Stored in OE/RR NOTIFICATIONS (#100.9, `^ORB`). ORB-namespace parameters control which alert types are enabled at which scope (System / Division / Service / Location / User).

---

## 5. CPRS RPC Surface

The definitive source is the **784-row RPC table** in `cprsguitm.docx`.

| RPC Namespace | Functional Scope |
|---|---|
| `ORWRP` | Reports retrieval — lab, vitals, meds, allergies, coversheet aggregation |
| `ORWPS` | Pharmacy — medication display and ordering |
| `ORWPCE` | PCE/encounter data — problem list, diagnoses, encounter linking |
| `ORWPT` | Patient selection, demographics |
| `ORWPT1` | PCMM/PACT team header and PC Details window (OR*3.0*387) |
| `ORWDX` | Order dialog — display and save |
| `ORWDXR` | Order dialog — release / sign |
| `ORWCS` | Order checking — execute checks against proposed order |
| `ORWNOTE` | Notes / TIU documents — create, retrieve, sign, list |
| `ORWCONSULT` | Consults — display and management |
| `ORWGRAPH` | Graphing — retrieve time-series data |
| `ORWU` | Utility RPCs — lookups, parameter retrieval, session setup |
| `ORWOR` | Orders retrieval — list, details, status |
| `ORWLR` | Lab orders — laboratory-specific functions |
| `ORWRA` | Radiology orders — radiology-specific functions |
| `PSB COVERSHEET1` | BCMA medication administration history (external package RPC) |
| `PXRM *` | Clinical reminder evaluation and display |
| `GMRV *` | Vitals — direct GMRV RPCs for detailed access |
| `SCMC *` | PCMM Web RPCs (added SD*5.3*603) |

### 5.1 Order Checking Detail

ORK-namespace routines evaluate proposed orders against:
- PATIENT ALLERGIES (#120.8) — allergy and drug-allergy interactions
- Active medications (PRESCRIPTION #52, PSJ files) — drug-drug, therapeutic duplication
- Lab results (#63) — lab-drug interactions
- Drug database (National Drug File — PSS/PSN) — formulary, dosing, controlled substance checks

Definitions in ORDER CHECKS (#100.8). Results displayed in review dialog before signing; overridable with documented reason.

### 5.2 CCOW

CPRS acts as a CCOW context manager participant. When VistA Imaging or MHA is launched from the Tools menu, CCOW keeps patient context synchronized between CPRS and the launched application.

### 5.3 Key Architectural Constraints

- CPRS cannot write to package globals directly — all writes go through RPCs that execute receiving package filing routines
- Every CPRS display element is a cached RPC result — no live push; display reflects state at last RPC call
- The context option is a security boundary — unauthorized RPCs cannot be called regardless of client attempts
- CPRS has no offline mode
- Multiple CPRS sessions can access the same patient simultaneously — M locking handles record-level concurrency
- CPRS List Manager (`cprslmtm.docx`) is the character-based terminal companion — supports most workflows via VALM package rendering

---

## PART III — PACKAGE INTEGRATIONS

---

## 6. Clinical Package Integrations

Packages are ordered by clinical centrality to CPRS. Gaps are flagged with **⚠ GAP**.

---

### 6.1 OR — CPRS / Order Entry Results Reporting

| | |
|---|---|
| **Namespace** | OR |
| **Version** | 3.0 |
| **Key corpus docs** | `cprsguitm.docx` · `cprsguium.docx` · `cprssetup.docx` · `cprslmtm.docx` |

OR is the CPRS package — see Parts I and II for full architecture. Key owned files: ORDER #100 (`^OR(100,`), ORDER CHECKS #100.8, OE/RR NOTIFICATIONS #100.9, PROTOCOL #101, ORDER DIALOG #101.41. Security keys: `ORES`, `ORELSE`, `OR AUTORENEWAL`. 784 RPCs documented in `cprsguitm.docx`.

---

### 6.2 LR — Laboratory

| | |
|---|---|
| **Namespace** | LR |
| **Version** | 5.2 |
| **Key corpus docs** | `lab5_2tm.docx` · `lab5_2um.docx` · `lab5_2sg.docx` |

- Primary file: LAB DATA #63 (`^LR`) — multi-level global by patient IEN, accession date, test
- Also: LABORATORY TEST #60 (`^LAB(60,`), COLLECTION SAMPLE #62
- CPRS surfaces: Labs tab, Coversheet (recent/abnormals), Reports tab, Graphing
- **HL7 flow**: External analyzers → `ORU^R01` → VistA HL7 engine → filing routines → `^LR(63,`. CPRS is not in the filing path.
- **RPC**: `ORWRP REPORT TEXT` with lab-specific parameters
- **Notifications**: Abnormal results trigger `ORB ABNORMAL LAB RESULTS`

---

### 6.3 PSO — Outpatient Pharmacy

| | |
|---|---|
| **Namespace** | PSO |
| **Version** | 7.0 |
| **Key corpus docs** | `pso_7_tm.docx` · `pso_7_pharm_um.docx` · `pso_7_man_um.docx` |

- Primary file: PRESCRIPTION #52 (`^PSRX`) — active and discontinued outpatient Rx
- Also: PHARMACY PATIENT #55 (`^PS(55,`)
- CPRS integration: Active Rx on Meds tab and Coversheet; order entry via OR dialogs → PSO filing → PRESCRIPTION #52 created
- **RPC family**: `ORWPS`
- `pso_7_tm.docx`: 74 reference tables — the densest parameter document in the corpus

---

### 6.4 PSJ — Inpatient Medications

| | |
|---|---|
| **Namespace** | PSJ |
| **Version** | 5.0 |
| **Key corpus docs** | `psj_5_0_p447_tm.docx` · `PSJ_5_0_p447_PHAR_UM.docx` · `PSJ_5_0_NURSE_UM.docx` |

- Owns unit dose and IV order files; PHARMACY PATIENT #55 shared with PSO
- CPRS integration: Inpatient orders on Meds tab; feeds BCMA (PSB) for administration
- Order path: CPRS → ORDER #100 → PSJ picks up → PSJ order records → BCMA reads PSJ
- BCMA callable routine `PSBAPIPM` called by PSJ to determine start dates for renewed orders

---

### 6.5 PSB — BCMA (Bar Code Medication Administration)

| | |
|---|---|
| **Namespace** | PSB |
| **Version** | 3.0 |
| **Key corpus docs** | `PSB_3_0_P131_tm.md` (uploaded gap doc) |

- Global: `^PSB`
- Key files: #53.66 BCMA IV PARAMETERS, #53.68 MISSING DOSE REQUEST, #53.69 REPORT REQUEST, #53.77 UNABLE TO SCAN LOG, #53.78 MEDICATION VARIANCE LOG, #53.79 BCMA MEDICATION LOG (`^PSB(53.79,`) — every administration event
- **Callable routines (DBIA)**: `PSBAPIPM` (start date for renewed orders, called by PSJ); `PSBMLHS` (medication history, called by CPRS via `PSB COVERSHEET1`)
- **41 published RPCs** including: `PSB COVERSHEET1`, `PSB MEDICATION HISTORY`, `PSB SCANMED`, `PSB SCANPT`, `PSB VALIDATE ORDER`, `PSB VITALS`
- **CPRS touch point**: Meds tab MAH via `PSB COVERSHEET1` → `PSBMLHS` → `^PSB(53.79,`
- **HL7**: Sends `RAS^O17`. MSH: `MSH^~|&^PSB HL7 SRV^^PSB HL7 SUB^^{datetime}^^RAS~O17^{msgid}^P^2.4`
- **Security keys**: `PSB MANAGER`, `PSB INSTRUCTOR`, `PSB CPRS MED BUTTON`, `PSB UNABLE TO SCAN`, `PSB NO WITNESS`
- **Dependencies**: Inpatient Medications 5.0, Kernel 8.0, Nursing 4.0, Order Entry 3.0, PCE 1.0, Pharmacy Data Management 1.0, RPC Broker 1.1, Vitals 5.0

> **⚠ GAP — PSS / PSN**: DRUG file #50 (`^PSDRUG`, owned by PSS) and National Drug File (PSN) not in corpus. PSS owns the drug data model underpinning all pharmacy packages. Without PSS/PSN documentation, the order checking drug database context is incompletely characterized.

---

### 6.6 RA — Radiology/Nuclear Medicine

| | |
|---|---|
| **Namespace** | RA |
| **Version** | 5.0 |
| **Key corpus docs** | `ra5_0tm.docx` · `ra5_0um.docx` · `ra5_0ag.docx` (187 headings, 100 tables) |

- Key files: RAD/NUC MED REPORTS #74 (`^RA(74,`), RADIOLOGY PATIENT #70 (`^RA(70,`), RAD/NUC MED ORDERS #70.2 (`^RA(70.2,`)
- CPRS integration: Orders via Orders tab; reports on Reports tab; camera icon = linked IMAGE #2005 record set by MAG/DICOM Gateway
- **HL7**: RA → `ORR^O02` → CPRS order status update

---

### 6.7 GMRV — Vitals/Measurements

| | |
|---|---|
| **Namespace** | GMRV |
| **Version** | 5.0 |
| **Key corpus docs** | `vitl5_tm.docx` · `vitl5_um.docx` · `vitl_5_p22_tm.docx` · `vitl_5_p22_um.docx` |

- Key file: GMRV VITAL MEASUREMENT #120.5 (`^GMR(120.5,`) — measurements with timestamp, type, value, units, entered-by
- CPRS surfaces: Coversheet recent vitals, Vitals tab, Reports tab (trending), Graphing
- Note: `vitl_5_p23_tm_change_pages.docx` contains RPC tables for patch 23 — orphaned fragment requiring base TM for context

---

### 6.8 GMRC — Consults/Request Tracking

| | |
|---|---|
| **Namespace** | GMRC |
| **Key corpus docs** | `constm.docx` (78 tables) · `consum.docx` · `consifc.docx` (39 tables) |

- Key file: REQUEST/CONSULTATION #123 (`^GMR(123,`)

**Consult status lifecycle**:

| Code | Status | Meaning |
|---|---|---|
| 1 | PENDING | Ordered, not yet received |
| 2 | ACTIVE | Service received and working |
| 3 | COMPLETE | Result note (TIU #8925, class CONSULT RESULT) filed and linked |
| 4 | DISCONTINUED | Cancelled after activation |
| 5 | CANCELLED | Cancelled before activation |

- **GMRC↔TIU interface**: `consifc.docx` (39 reference tables) — definitive ICD for the consult-to-note linkage

---

### 6.9 TIU — Text Integration Utility

| | |
|---|---|
| **Namespace** | TIU |
| **Key corpus docs** | `tiutm.docx` (51 tables) · `tiuum.docx` · `tiuim.docx` (implementation guide) |

- Key files: TIU DOCUMENT #8925 (`^TIU(8925,`), TIU DOCUMENT DEFINITION #8925.1
- Document class → CPRS surface:
  - PROGRESS NOTES → Notes tab
  - CONSULT RESULTS → Consults tab (linked to GMRC #123)
  - DISCHARGE SUMMARY → D/C Summaries tab
  - CLINICAL PROCEDURES → Reports tab (MD files these)
  - SURGERY REPORTS → Reports tab (SR files these)
- **RPC mediator**: `ORWNOTE` namespace

> **⚠ GAP — ASU**: `asutm.docx` not in corpus. The Authorization/Subscription Utility rules engine — defining exactly who can sign each TIU document class — is not characterized. This is a real gap for any notes/signature workflow analysis.

---

### 6.10 GMRA — Adverse Reaction Tracking (Allergies)

| | |
|---|---|
| **Namespace** | GMRA |
| **Version** | 4.0 |
| **Key corpus docs** | `gmra_4_0_tm.docx` · `gmra_4_0_um.docx` (162 headings) |

- Key file: PATIENT ALLERGIES #120.8 (`^GMRD(120.8,`)
- CPRS surfaces: Coversheet allergies; feeds order checking (ORK queries #120.8 before signing)

---

### 6.11 GMPL — Problem List

| | |
|---|---|
| **Namespace** | GMPL |
| **Version** | 2.0 |
| **Key corpus docs** | `gmpl_2_0_49_tm.docx` · `gmplum.docx` |

- Key file: PROBLEM #9000011 (`^AUPNPROB`) — active/inactive problem list, ICD-coded
- CPRS surfaces: Coversheet problems panel, Problems tab

---

### 6.12 PXRM — Clinical Reminders

| | |
|---|---|
| **Namespace** | PXRM |
| **Version** | 2.0 |
| **Key corpus docs** | `pxrm_2_4_tm.docx` + 44 additional corpus docs (largest by doc count — 45 total) |

- Global: `^PXRM`
- Key constructs: Reminder Definition, Reminder Term (atomic finding), Reminder Taxonomy (ICD/CPT groupings), Reminder Dialog (structured data entry)
- Evaluation at CPRS patient load: engine checks each active reminder against patient's record (reads LR, PSO, PX, GMPL, etc. via DBIAs) → returns DUE / NOT DUE / APPLICABLE / NOT APPLICABLE
- CPRS surfaces: Coversheet (due reminders), write-back (marks done → files data to PCE V-files #9000010.x), Reports tab

---

### 6.13 PX — Patient Care Encounter (PCE)

| | |
|---|---|
| **Namespace** | PX |
| **Version** | 1.0 |
| **Key corpus docs** | `px_tm.docx` (3 FileMan registry tables) · `px_um.docx` · `pxumappx.docx` |

- V-files (all `^AUPN` prefix): VISIT #9000010 (`^AUPNVSIT`), V PROVIDER #9000010.06, V DIAGNOSIS #9000010.07, V IMMUNIZATION #9000010.11, V TREATMENT #9000010.18
- PROBLEM #9000011 (`^AUPNPROB`) shared with GMPL — same global, same file
- Clinical Reminders write-back files data to V-files
- **BCMA→PCE**: `PSB PX BCMA2PCE TASK` (PSBPXFL, PSBPXLP routines) runs nightly to file immunization data from BCMA administration events

---

### 6.14 GMTS — Health Summary

| | |
|---|---|
| **Namespace** | GMTS |
| **Version** | 2.7 |
| **Key corpus docs** | `gmts_2_7_p133_tm.docx` · `hsum_2_7_tm.docx` · `gmts_2_7_p133_um.docx` · `hsum_2_7_um.docx` |

Aggregation service — assembles multi-package clinical data into structured summary reports. Each Health Summary Type is configured with components pulling data from specific packages (LR, PSO, GMRV, TIU, GMRC, etc.) via DBIAs. CPRS Reports tab: GMTS RPCs execute the component set and return assembled text.

---

### 6.15 MAG — VistA Imaging

| | |
|---|---|
| **Namespace** | MAG |
| **Key corpus docs** | `IMGTECHMAN_F.md` (655K TM, uploaded) · `MAG_Display_User_Manual.md` (469K, uploaded) |

Three-tier architecture:
1. **VistA server**: IMAGE #2005 (`^MAG(2005,`) metadata, NETWORK LOCATION #2005.2 (`^MAG(2005.2,`)
2. **DICOM Gateway**: ingests radiology images from PACS, links IMAGE #2005 to RA report IENs
3. **Clinical Display workstation**: Windows GUI launched from CPRS Tools menu

CPRS integration:
- Camera icon on RA report: MAG links IMAGE #2005 to RA report IEN → icon appears → click launches Clinical Display to that study
- TIU note image capture: clinicians attach images to TIU notes via `MAGCAP` key; images in `^MAG` linked to TIU document IEN
- CCOW: VistA Imaging uses CCOW for patient context sync

Security keys: `MAGDISP CLIN`, `MAGDISP ADMIN`, `MAG DELETE`, `MAG SYSTEM`, `MAGCAP`, `MAG EDIT`

---

### 6.16 YS — Mental Health

| | |
|---|---|
| **Namespace** | YS |
| **Version** | 5.01 |
| **Key corpus docs** | `YS_MHA_UM.md` · `ys_mha_tm.md` · `mha_web_um.md` (all uploaded) |

- Global roots: `^YTT` (instrument definitions, scoring, batteries) · `^YTD` (patient data, responses, results)
- 29 files: MH INSTRUMENT #601 through #601.94
- Key files: #601.84 MH ADMINISTRATIONS (`^YTD(601.84,`), #601.92 MH RESULTS (`^YTD(601.92,`)

CPRS integration (bidirectional):
- MHA launched from CPRS Tools menu; CCOW synchronizes patient context
- Reports tab: MHA scored results from `^YTD(601.92,`
- Clinical Reminders: MHA results can trigger/satisfy reminders; write-back through PXRM
- Consults: some MHA workflows generate GMRC consult requests
- Context option: `YS MHA CONTEXT`

---

### 6.17 PCMM / WEBP — Primary Care Management Module

| | |
|---|---|
| **Namespaces** | SCMC (routines), OR (CPRS side), SD (data side) |
| **Key corpus docs** | `pcmmug.md` · `pcmmmhtcug.md` · `pcmm_web_ug.md` · `sd_53_603_tm.md` (all uploaded) |

Migration: Legacy PCMM GUI → PCMM Web. `SD*5.3*603` installs server changes; `OR*3.0*387` adds PACT header to CPRS.

Key files:
- OUTPATIENT PROFILE #404.41: field `.06` (CPRS HEADER TEXT), field `.07` (CPRS PC WINDOW CACHE)
- PATIENT TEAM ASSIGNMENT #404.42: assignment type, status codes
- PATIENT TEAM POSITION ASSIGNMENT #404.43: new C cross-reference added by SD*5.3*603
- POSITION ASSIGNMENT HISTORY #404.52: FTEE history, teamlet designation
- PCMM PATIENT EVENTS #404.54: new file; tracks patient DOD events

Assignment status codes (#404.42/.43): `DU` DOD Unassign, `IU` Inactive Unassign, `PR` Patient Relocated, `FT` Intra-Facility Transfer, `DC` Discharge from Care, `ER` Error (+ others)

CPRS integration (via OR*3.0*387):
- PACT header: `SCMCDD1` maintains #404.41,.06 on team assignment changes
- RPCs: `ORWPT1 PRCARE` (header text), `ORWPT1 PCDETAIL` (full PACT details window)
- PCMM Web RPCs (SCMC namespace): `SCMC FILER`, `SCMC FINDER`, `SCMC FTEE CREATE/READ/UPDATE/DELETE`, `SCMC PATIENT INFO`, `SCMC PCDETAIL` — thin wrappers over FileMan DBS APIs
- MHTC (Mental Health Treatment Coordinator): `SCMCMHTC` handles assignment; `ORB PROVIDER RECIPIENTS` parameter with 'C' code for MHTC notifications

---

### 6.18 SR — Surgery

| | |
|---|---|
| **Namespace** | SR |
| **Version** | 3.0 |
| **Key corpus docs** | `sr_3_um.docx` (344 reference tables — largest in corpus) · `sr_3_tm_r1115.docx` |

Surgical cases documented in SR; surgical reports filed as TIU DOCUMENT (#8925). Reports appear on CPRS Reports tab. `sr_3_um.docx` has the highest reference table count of any document in the corpus.

---

### 6.19 ACR / SD — Ambulatory Care Reporting / Scheduling (PIMS)

| | |
|---|---|
| **Namespaces** | ACR / SD |
| **Key corpus docs** | `acr_p_pimstm.docx` (121 tables, 10 RPC tables) · `sd_pims_tm.docx` (259 tables, 10 RPC tables) |

- HOSPITAL LOCATION #44 (`^SC`) — clinics and wards used in all CPRS location selectors
- PATIENT #2 (`^DPT`) — master patient record (owned by DG/Registration, heavily referenced here)
- CPRS coversheet: Upcoming Appointments panel

> **⚠ GAP — ADT/DG (Registration)**: `adt_pims_tm.docx` not in corpus. PATIENT #2 (`^DPT`) is the single most-referenced file in all of VistA — the anchor for every patient record. Without ADT/DG documentation, the full patient data model (admission status, attending provider, room/bed, eligibility, enrollment) is characterized only through what other packages say about it, not from first-party documentation. This is the most significant gap in the corpus.

---

### 6.20 ECX — Event Capture / DSS

| | |
|---|---|
| **Namespace** | ECX |
| **Version** | 3.0 |
| **Key corpus docs** | `ecx_3_ug.docx` (150 headings) · `ecx_3_tm.docx` |

Workload reporting — captures clinical event data for DSS cost/workload analysis. Receives encounter data via HL7 from PCE and other packages. CPRS integration is indirect.

---

### 6.21 LRAP / LRBB — Lab Anatomic Pathology / Blood Bank

| | |
|---|---|
| **Namespaces** | LRAP / LRBB |
| **Key corpus docs** | `lrap_5_2_tm.docx` · `lrbb5_2tm.docx` |

Sub-packages of LR. LRAP: surgical pathology (`^LR(63, patIEN, 'SP')`), cytology (`'CY'`). LRBB: blood bank (`'BB'`). Both surfaces on CPRS Labs tab and Reports tab.

---

## PART IV — DEVELOPER REFERENCE TABLES

---

## 7. Master File → Global → Package → CPRS Surface Map

| File # | File Name | Global Root | Package | CPRS Surface / Notes |
|---|---|---|---|---|
| 2 | PATIENT | `^DPT` | DG | Patient header, everywhere — master anchor (**⚠ GAP**) |
| 44 | HOSPITAL LOCATION | `^SC` | SD | Location selectors (clinics, wards) |
| 52 | PRESCRIPTION | `^PSRX` | PSO | Coversheet meds, Meds tab (outpatient Rx) |
| 53.79 | BCMA MEDICATION LOG | `^PSB(53.79,` | PSB | Coversheet MAH, Meds tab (admin events) |
| 55 | PHARMACY PATIENT | `^PS(55,` | PSJ/PSO | Meds tab (inpatient pharmacy record) |
| 60 | LABORATORY TEST | `^LAB(60,` | LR | Test definitions (reference) |
| 63 | LAB DATA | `^LR` | LR | Labs tab, Coversheet, Reports tab |
| 70 | RADIOLOGY PATIENT | `^RA(70,` | RA | Radiology patient record |
| 70.2 | RAD/NUC MED ORDERS | `^RA(70.2,` | RA | Radiology orders (linked from OR #100) |
| 74 | RAD/NUC MED REPORTS | `^RA(74,` | RA | Reports tab; camera icon = linked MAG image |
| 100 | ORDER | `^OR(100,` | OR | Orders tab (all CPRS-placed orders) |
| 100.8 | ORDER CHECKS | `^ORD(100.8,` | OR | Order entry (ORK routines) |
| 100.9 | OE/RR NOTIFICATIONS | `^ORB` | OR | CPRS notification list (alerts) |
| 101.41 | ORDER DIALOG | `^ORD(101.41,` | OR | Order entry dialog definitions |
| 120.5 | GMRV VITAL MEASUREMENT | `^GMR(120.5,` | GMRV | Coversheet vitals, Vitals tab, Graphing |
| 120.8 | PATIENT ALLERGIES | `^GMRD(120.8,` | GMRA | Coversheet allergies; feeds order checking |
| 123 | REQUEST/CONSULTATION | `^GMR(123,` | GMRC | Consults tab (full lifecycle) |
| 200 | NEW PERSON | `^VA(200,` | XU | Provider selectors, e-sig, DUZ identity |
| 404.41 | OUTPATIENT PROFILE | SD global | PCMM/SD | CPRS PACT header (.06), PC cache (.07) |
| 404.42 | PATIENT TEAM ASSIGNMENT | SD global | PCMM | PACT team assignments |
| 601 | MH INSTRUMENT | `^YTT(601,` | YS | Reports tab (instrument definitions) |
| 601.84 | MH ADMINISTRATIONS | `^YTD(601.84,` | YS | Reports tab (administration records) |
| 601.92 | MH RESULTS | `^YTD(601.92,` | YS | Reports tab (computed MHA scores) |
| 2005 | IMAGE | `^MAG(2005,` | MAG | Tools menu (Clinical Display); camera icon |
| 8925 | TIU DOCUMENT | `^TIU(8925,` | TIU | Notes, Consults, D/C, Reports tabs |
| 8925.1 | TIU DOCUMENT DEFINITION | `^TIU(8925.1,` | TIU | Document class hierarchy (selectors) |
| 8989.51 | PARAMETER DEFINITION | `^XTMP("XPAR"` | XU/XPAR | CPRS configuration (35 tables in cprssetup.docx) |
| 9000010 | VISIT | `^AUPNVSIT` | PX | Encounter records; Reports tab |
| 9000011 | PROBLEM | `^AUPNPROB` | GMPL | Coversheet problems, Problems tab |

### Lab Data Global Structure (^LR)

| Subscript pattern | Content |
|---|---|
| `^LR(63, patIEN, "CH", invDate, testIEN)` | Chemistry / hematology results |
| `^LR(63, patIEN, "MI", ...)` | Microbiology |
| `^LR(63, patIEN, "SP", ...)` | Surgical pathology (LRAP) |
| `^LR(63, patIEN, "CY", ...)` | Cytology (LRAP) |
| `^LR(63, patIEN, "BB", ...)` | Blood bank (LRBB) |

---

## 8. Security Keys Reference

| Security Key | Package | Purpose |
|---|---|---|
| `ORES` | OR | Full clinician order signer |
| `ORELSE` | OR | Limited order entry (ward clerks) |
| `OR AUTORENEWAL` | OR | Automatic renewal of medication orders |
| `TIU AUTHOR` | TIU | Can author TIU clinical documents |
| `PSB MANAGER` | PSB | Full BCMA administrative access |
| `PSB INSTRUCTOR` | PSB | BCMA training mode access |
| `PSB CPRS MED BUTTON` | PSB | Nurse documenting verbal STAT orders via CPRS |
| `PSB UNABLE TO SCAN` | PSB | Document administration without barcode scan |
| `PSB NO WITNESS` | PSB | Administer controlled substances without witness |
| `MAGDISP CLIN` | MAG | Clinical viewing in VistA Imaging |
| `MAGDISP ADMIN` | MAG | Administrative viewing in VistA Imaging |
| `MAG DELETE` | MAG | Delete images |
| `MAG SYSTEM` | MAG | VistA Imaging system administration |
| `MAGCAP` | MAG | Image capture — attach images to TIU documents |

---

## 9. GUI Context Options

| Context Option | Package | Application |
|---|---|---|
| `OR CPRS GUI CHART` | OR | CPRS GUI — full chart access (primary clinical workstation) |
| `PSB GUI CONTEXT – USER` | PSB | BCMA GUI — medication administration workstation |
| `YS MHA CONTEXT` | YS | Mental Health Assistant (MHA) GUI |
| `SCMC PCMMR APP PROXY MENU` | PCMM | PCMM Web application proxy |
| `SCMC PCMMR WEB USER MENU` | PCMM | PCMM Web user-facing context |
| `MAG WINDOWS` | MAG | VistA Imaging Clinical Display workstation |

---

## 10. Cross-Package File Linkages

| From File | To File | Mechanism | Packages |
|---|---|---|---|
| REQUEST/CONSULTATION #123 | TIU DOCUMENT #8925 | Consult IEN pointer in TIU document | GMRC → TIU |
| ORDER #100 | PRESCRIPTION #52 | Order IEN in PSO prescription record | OR → PSO |
| ORDER #100 | RAD/NUC MED ORDERS #70.2 | Order IEN in RA order record | OR → RA |
| TIU DOCUMENT #8925 | IMAGE #2005 | TIU document IEN in image record | TIU → MAG |
| IMAGE #2005 | RAD/NUC MED REPORTS #74 | Image linked to RA report IEN — sets camera icon | MAG → RA |
| VISIT #9000010 | TIU DOCUMENT #8925 | Visit IEN in TIU document — encounter attribution | PX → TIU |
| PROBLEM #9000011 | PATIENT #2 | DFN — all problem records keyed by patient | GMPL → DG |
| PATIENT ALLERGIES #120.8 | PATIENT #2 | DFN — all allergy records keyed by patient | GMRA → DG |
| BCMA MED LOG #53.79 | ORDER #100 / PSJ order | Order IEN in administration event record | PSB → OR/PSJ |
| OUTPATIENT PROFILE #404.41 | PATIENT #2 | DFN — PACT header keyed by patient | PCMM → DG |

---

## 11. HL7 Message Flow Summary

| Sender | Receiver | Message Type | Event / Notes |
|---|---|---|---|
| External analyzer | LR (`^LR`) | `ORU^R01` | Lab result filing; CPRS reads result after filing |
| PSB (BCMA) | Workload/notification | `RAS^O17` | Med administration event; HL7 v2.4 |
| RA | OR (CPRS) | `ORR^O02` | Radiology order status update |
| PCE / PX | ECX / DSS | ADT / workload | Encounter workload events |

---

## 12. Documented Knowledge Gaps

| Package | Name | VDL Active Docs | Impact |
|---|---|---|---|
| ADT/DG | Admission Discharge Transfer / Registration | 94 | PATIENT #2 data model; admission status; room/bed; attending; eligibility — every package references #2. **Most significant gap.** |
| ASU | Authorization/Subscription Utility | 6 | TIU signing authority rules engine — who can sign each document class is uncharacterized. |
| PSS | Pharmacy: Data Management | 174 | DRUG file #50 (`^PSDRUG`) — the drug data model underpinning all pharmacy packages and order checking. |
| MD | Clinical Procedures | 126 | File numbers, global structure, RPC surface, CPRS Reports tab integration not fully characterized. |
| XU | Kernel | 140 | Kernel API, TaskMan API, MailMan API, security key grant mechanics — currently derived, not first-party. |
| PSN | National Drug File | 30 | National drug reference for interaction checking and formulary. |
| XWB | RPC Broker | 18 | Wire protocol, connection management, error codes, Delphi client library API absent. |
| NUR | Nursing | 16 | Nursing 4.0 is a BCMA dependency. Nursing-specific CPRS functions and care plan documentation uncharacterized. |
| LEDI | Lab Electronic Data Interchange | 14 | HL7 interface for external lab results entering VistA; LEDI-specific configuration and mapping unknown. |

**To resolve**: fetch and ingest 1 TM + 1 UM per package using `fetch_tier1.py` (vista-docs/scripts/). Estimated 10–20 additional documents close all 9 gaps.

---

## Appendix A: Key Patch Reference

| Patch | Significance |
|---|---|
| `OR*3.0*387` | Adds PACT team header to CPRS patient header bar. New RPCs: `ORWPT1 PRCARE`, `ORWPT1 PCDETAIL`. Depends on SD*5.3*603. |
| `SD*5.3*603` | Installs PCMM Web VistA server changes. Adds PCMM PATIENT EVENTS #404.54, new C cross-reference on #404.43, SCMC namespace RPCs. |
| `PSB*3*131` | Most recent BCMA patch in corpus. 41 published RPCs. Adds VHIC 4.0 / DoD CAC barcode support via `RPCVIC^DPTLK` in `PSB SCANPT`. |
| `YS*5.01*191` | Adds MHA Web capability. Extends YS file schema (#601.751, #601.781). |
| `DG*5.3*857` | Adds `RPCVIC^DPTLK` API to Registration for VIC 4.0 patient lookup — consumed by BCMA `PSB SCANPT`. |

---

## Appendix B: Data Dictionary Conventions

When reading VistA documentation, these patterns appear everywhere:

- **File reference**: `FILE NAME (#number)` — e.g., `PATIENT (#2)`, `ORDER (#100)`, `TIU DOCUMENT (#8925)`
- **Global notation**: `^GLOBALROOT(fileNum, IEN, ...)` — e.g., `^LR(63,`, `^OR(100,`
- **Field reference**: `FILE(#).FIELD(#)` — e.g., `404.41,.06` means file #404.41, field .06
- **Global location**: expressed as `node;piece` — e.g., `1;1` means global node `1`, piece `1` (caret-delimited)
- **Pointer fields**: a field whose value is an IEN in another file
- **Multiple fields**: a sub-file within a file (creates a sub-global level)
- **Set of codes**: an enumerated type — e.g., `'1' FOR PRIMARY CARE; '98' FOR PENDING; '99' FOR OTHER`
- **Inverse date**: VistA stores dates as `9999999 - FM_date` so that sorting is chronological (most recent first)
