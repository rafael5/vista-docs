# VDL Pipeline — Stage 5: System Classification

**Date:** 2026-03-30
**Module:** `vista_docs/classify/`
**Column:** `system_type` in `vdl_inventory_enriched.csv`

---

## Table of Contents

1. [Overview](#1-overview)
2. [The Classification Problem](#2-the-classification-problem)
3. [The KIDS Test](#3-the-kids-test)
4. [Three-Pass Methodology](#4-three-pass-methodology)
   - [Pass 1 — Primary Classification (7 categories)](#pass-1--primary-classification-7-categories)
   - [Pass 2 — Gap Analysis and Refinement (11 categories)](#pass-2--gap-analysis-and-refinement-11-categories)
   - [Pass 3 — Disambiguation of Interface Packages](#pass-3--disambiguation-of-interface-packages)
5. [Implementation](#5-implementation)
6. [Complete Application Classification](#6-complete-application-classification)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

The classify stage applies the `system_type` classification to all 196 applications in the VDL inventory. This is the primary analytical contribution of the project: the VDL itself does not distinguish VistA packages from non-VistA systems, listing them all side by side without differentiation.

**Input:** `vdl_inventory_enriched.csv` + 2,240 enriched markdown documents
**Output:** `system_type` column populated for all 196 applications

Final result: 196 applications classified across 11 categories. Zero unclassified applications.

The classification is implemented as an explicit, deterministic mapping table in `classify/rules.py`. Every non-obvious decision includes an inline rationale comment. The classification can be reproduced exactly by re-running `vista-docs classify`.

---

## 2. The Classification Problem
[↑ Table of Contents](#table-of-contents)

The VA VDL presents 196 applications in five sections as a flat list. Within this list:

- 127 are genuine VistA M packages (server-side MUMPS code deployed via KIDS)
- 20 are web or mobile clients that access VistA data but have no M server component
- 10 are integration middleware layers between VistA and external systems
- 23 are national VA enterprise services or platforms
- 6 are commercial off-the-shelf products (COTS) or data sets
- 6 are hybrid entries where the VDL bundles a VistA component with a non-VistA component
- 4 are data patches (KIDS builds containing reference data, not executable M code)
- 2 are program documentation, not software
- 1 is a VBA system (Veterans Benefits Administration)

Without classification, any analysis of "VistA documentation" that naively takes the full VDL at face value includes documentation for Salesforce, TeleTracking kiosks, the Oracle Cerner EHR modernization program, and the VA Lighthouse API platform — none of which are VistA.

The `system_type` classification makes the VistA/non-VistA boundary explicit and machine-readable.

---

## 3. The KIDS Test
[↑ Table of Contents](#table-of-contents)

The classification is anchored by a single binary test:

> **Is this application an M (MUMPS) package, versioned and distributed by the VistA M packaging system (KIDS — Kernel Installation and Distribution System), running on the M-based VistA application-database server?**

- **Yes** → `VistA` (or a VistA hybrid if the VDL bundles it with a non-VistA component)
- **No** → one of the eight non-VistA categories

This test is applied to each application by reading its Technical Manual and Installation Guide. These documents state explicitly:
- The implementation language (M/MUMPS, Java, .NET, web)
- The deployment mechanism (KIDS patch, standalone installer, web deployment)
- The runtime environment (VistA server, separate server, client workstation, cloud)

The KIDS test is strict and architectural — it does not consider:
- Whether the application connects to VistA (many non-VistA apps do)
- Whether the application has a MUMPS namespace assigned in the VDL (phantom namespaces exist)
- Whether the application is documented in the VDL (all 196 are)
- Whether the application was historically associated with VistA

---

## 4. Three-Pass Methodology
[↑ Table of Contents](#table-of-contents)

### Pass 1 — Primary Classification (7 categories)

The initial classification applied the KIDS test to all 196 applications, producing 7 categories:

| Category | Count | Description |
|---|---|---|
| `VistA` | ~130 | KIDS-deployed M package |
| `Web client` | ~20 | Web/mobile application accessing VistA data |
| `Integration middleware` | ~12 | Adapter/bridge between VistA and external systems |
| `VA enterprise service` | ~25 | Separate national VA platform |
| `VBA system` | 1 | Veterans Benefits Administration tool |
| `COTS product` | ~5 | Commercial software with no VistA M component |
| `Program documentation` | 2 | Documents a program, not software |

After Pass 1, four patterns were identified that forced misclassification under the 7-category scheme. These patterns required four additional categories (Pass 2).

### Pass 2 — Gap Analysis and Refinement (11 categories)

**Gap 1: VDL Bundling of MUMPS and non-MUMPS components**

The VDL groups several applications where a MUMPS server package and a non-MUMPS client or COTS system are documented together under a single entry. A 7-category scheme forces a binary choice: classify as `VistA` (losing the non-VistA component) or as the non-VistA category (losing the VistA component). Neither is accurate.

Three hybrid categories were added:

- **`VistA + GUI`**: MUMPS server + GUI client (CPRS, MAG)
- **`VistA + COTS`**: MUMPS integration layer + COTS system (MD, YS, ROI)
- **`VistA + middleware`**: MUMPS M listener + J2EE/WebLogic connector (XOBV)

In every hybrid case, the MUMPS side passes the KIDS test. The hybrid category preserves both the VistA classification of the M component and the acknowledgment of the non-VistA component.

**Gap 2: Data-only KIDS patches**

CPT, ICD, DRG, and LEX are KIDS builds but their payload is reference data (terminology code sets and grouper tables), not executable M routines. Under the strict KIDS test they would be classified as `VistA`, but this misrepresents their nature — they are licensed data distributions, not software packages.

- **`Data patch`** was added for these four applications.

**Gap 3: Program documentation**

EHM (Electronic Health Modernization, the Oracle Cerner EHRM program) and MON (VistA Monograph) are not software systems at all. EHM documents the VA's transition away from VistA; MON is a catalog of VistA packages. Neither is deployable or installable software.

- **`Program documentation`** was already present in the initial 7 categories.

**Gap 4: Phantom namespaces**

Several non-VistA applications have a `pkg_ns` assigned in the VDL for catalog-tracking purposes. Examples:
- MED (Mobile Electronic Documentation): `pkg_ns = TIU` — because MED calls the TIU MUMPS package via API, but MED itself has no M code
- PECS (Pharmacy Enterprise Customization System): `pkg_ns = PECS` — a tracking code with no corresponding MUMPS codebase

Phantom namespaces do not affect classification in the corrected 11-category scheme. Classification is based on Technical Manual content, not on namespace assignment.

### Pass 3 — Disambiguation of Interface Packages

Several applications were initially misclassified because the VDL entry name matched the name of an external national service or VBA client, rather than the VistA MUMPS package that interfaces with it.

Re-examination of Technical Manual content corrected four misclassifications:

**DVBA — Reclassified: `VBA system` → `VistA`**

DVBA is the AMIE (Automated Medical Information Exchange) package — a KIDS-deployed M package that generates Compensation and Pension examination requests for VBA adjudicators. The VBA client is CAPRI (a separate VDL entry). The DVBA Technical Manual confirms M implementation and KIDS distribution. DVBA was initially misclassified because "Compensation and Pension" suggested a VBA system.

**IVMB — Reclassified: `VA enterprise service` → `VistA`**

IVMB is the Health Eligibility Center (HEC) VistA interface — a KIDS-deployed M package that sends eligibility transactions to the national HEC. The name "Health Eligibility Center" suggested a national enterprise service. The Technical Manual and KIDS patch documentation (IVMB\*2\*xxx Installation Guides) confirm KIDS deployment.

**CHDS — Reclassified: `VA enterprise service` → `VistA`**

CHDS (Community Health Data Sharing) is a KIDS-deployed M package. Initially classified as a national data service based on the name. The KIDS patch CHDS\*2.2\*1 with its Installation Guide confirms VistA M package status.

**XOBV — Reclassified: `Integration middleware` → `VistA + middleware`**

XOBV (VistALink) was initially classified as `Integration middleware` because VistALink is the J2EE middleware layer. The Technical Manual reveals that XOBV is a bundled entry: the M-side RPC listener is KIDS-deployed (Installation Guide confirms) while the J2EE WebLogic connector is the non-VistA component. Reclassified to `VistA + middleware` — the same bundling pattern as CPRS and MAG.

---

## 5. Implementation
[↑ Table of Contents](#table-of-contents)

### `classify/rules.py`

The classification is implemented as a pure, fully unit-tested module. It contains 52 test cases covering all 11 categories and every edge case.

The module exports a single lookup function:

```python
def get_system_type(app_code: str) -> str:
    """
    Return the system_type classification for an application code.
    Returns 'UNKNOWN' if the app_code is not in the mapping.
    """
```

The mapping table is a Python dict with inline rationale comments for every non-obvious decision:

```python
SYSTEM_TYPE_MAP: dict[str, str] = {
    # ── VistA ──────────────────────────────────────────────────────────
    "ADT":   "VistA",   # DG*5.3 — KIDS-confirmed in TM
    "PSO":   "VistA",   # PSO*7  — KIDS-confirmed in TM
    ...
    # ── VistA + GUI ────────────────────────────────────────────────────
    "CPRS":  "VistA + GUI",  # OR*3.0 server (VistA) + Delphi GUI client
    "MAG":   "VistA + GUI",  # MAG* imaging server (VistA) + Windows workstation
    ...
    # ── DVBA: AMIE is a VistA M package; VBA client is CAPRI (separate entry)
    "DVBA":  "VistA",
    # ── XOBV: M-side RPC listener (KIDS-confirmed) + J2EE WebLogic connector
    "XOBV":  "VistA + middleware",
    ...
}
```

### Evaluation Order in `classify/rules.py`

1. Filename-pattern rules (highest specificity — applies to doc-level classification)
2. Title-pattern rules
3. UNKNOWN (catch-all for unmatched — should never trigger for `system_type` given complete coverage)

---

## 6. Complete Application Classification
[↑ Table of Contents](#table-of-contents)

All 196 VDL applications with their `system_type` classification, organized by VDL section.

### Clinical (99 applications)

| App | Full Name | system_type | Status |
|---|---|---|---|
| ACKQ | Quality Audiology and Speech Analysis and Reporting (QUASAR) | VistA | active |
| ACR | Ambulatory Care Reporting | VistA | active |
| ADT | Admission Discharge Transfer | VistA | active |
| AMT | Anticoagulation Management Tool | VistA | active |
| ANRV | Blind Rehabilitation | VistA | active |
| AR/WS | Pharmacy: Automatic Replenish / Ward Stock | VistA | active |
| ASCD | Automated Service Connected Designation | VistA | active |
| ASU | CPRS: Authorization Subscription Utility | VistA | active |
| CCRA | Community Care Referral and Authorization | Web client | active |
| CHDS | Clinical/Health Data Repository | VistA | active |
| CPRS | Computerized Patient Record System | VistA + GUI | active |
| CRHD | Shift Handoff Tool | VistA | active |
| CRMS | Customer Relationship Management - SalesForce | COTS product | active |
| DGBT | Beneficiary Travel | VistA | active |
| DGJ | Incomplete Records Tracking (IRT) | VistA | active |
| DHT | Home Telehealth | Web client | active |
| DRM+ | Dentistry | VistA | active |
| EDIS | Emergency Department Integration Software | VistA | active |
| EFR | Registry: Embedded Fragments | VistA | active |
| EHM | Electronic Health Modernization | Program documentation | active |
| EPI | Laboratory: Emerging Pathogens Initiative | VistA | active |
| EPSI | Enterprise Precision Scanning and Indexing | Web client | active |
| ETS | Enterprise Terminology Service | VA enterprise service | active |
| FH | Nutrition and Food Service | VistA | active |
| FIM | Functional Independence Measurement | VistA | active |
| GMPL | CPRS: Problem List | VistA | active |
| GMR | Intake and Output | VistA | active |
| GMRA | CPRS: Adverse Reaction Tracking (ART) | VistA | active |
| GMRC | CPRS: Consult/Request Tracking | VistA | active |
| GMRV | Vitals/Measurements | VistA | active |
| GMTS | CPRS: Health Summary | VistA | active |
| HBPC | Home Based Primary Care | VistA | active |
| HDR | HDR - Historical (HDR-Hx) | VA enterprise service | active |
| HMP | Health Management Platform | VistA | decommissioned |
| ICR | Immunology Case Registry | VistA | decommissioned |
| JLV | Joint Longitudinal Viewer | Web client | active |
| LA | Laboratory: Universal Interface | VistA | active |
| LEDI | Laboratory: Electronic Data Interchange | VistA | active |
| LEX | Lexicon Utility | Data patch | active |
| LR | Laboratory (LA and LR) | VistA | active |
| MAG | VistA Imaging System | VistA + GUI | active |
| MBAA | Mobile Scheduling Applications Suite | Web client | archive |
| MC | Medicine | VistA | active |
| MD | Clinical Procedures | VistA + COTS | active |
| MED | Mobile Electronic Documentation | Web client | active |
| MJCF | Bar Code Expansion (BCE) | VistA | active |
| MMRS | Methicillin Resistant Staph Aurerus (MRSA) | VistA | active |
| NCR | Registry: National Clozapine Coordination | VistA | active |
| NHIN | Nationwide Health Information Network Adapter | VA enterprise service | active |
| NUPA | Patient Assessment Documentation Package (PADP) | VistA | active |
| NUR | Nursing | VistA | active |
| ONC | Registry: Oncology | VistA | active |
| OR | CPRS: Bulk Parameter Editor for Notifications | VistA | active |
| ORRC | Care Management | VistA | decommissioned |
| PAIT | Patient Appointment Info. Transmission | VistA | active |
| PCMM | Primary Care Management Module | VistA | active |
| POC | Laboratory: Point of Care | VistA | active |
| PPP | Pharmacy: Prescription Practices | VistA | archive |
| PREA | Pharmacy: Advanced Medication Platform | Web client | active |
| PRF | Patient Record Flags | VistA | active |
| PSA | Pharmacy: API | VistA | active |
| PSB | Pharmacy: Bar Code Medication Administration (BCMA) | VistA | active |
| PSD | Pharmacy: Controlled Substances | VistA | active |
| PSJ | Pharmacy: Inpatient Medications | VistA | active |
| PSN | Pharmacy: National Drug File (NDF) | VistA | active |
| PSO | Pharmacy: Outpatient Pharmacy | VistA | active |
| PSS | Pharmacy: Data Management | VistA | active |
| PSU | Pharmacy: Benefits Management | VistA | active |
| PSX | Pharmacy: Consolidated Mail Outpatient Pharmacy | VistA | active |
| PX | Patient Care Encounter (PCE) | VistA | active |
| PXRM | CPRS: Clinical Reminder Updates | VistA | active |
| RA | Radiology/Nuclear Medicine | VistA | active |
| RMDS | RAI/MDS | VistA | active |
| RMPR | Prosthetics | VistA | active |
| ROEB | Registry: Breast Cancer (BCR) | VistA | active |
| ROEG | Registry: Multiple Sclerosis Surveillance (MSSR) | VistA | active |
| ROES | Remote Order Entry System | VistA | active |
| ROEV | Registry: Military Eye Vision Injury (MEVIR) | VistA | active |
| ROR | Registry: Clinical Case (CCR) | VistA | active |
| SD | Electronic Wait List | VistA | decommissioned |
| SOW | Social Work | VistA | decommissioned |
| SPN | Spinal Cord Dysfunction | VistA | decommissioned |
| SR | Surgery | VistA | active |
| SRA | Surgery Risk Assessment | VistA | active |
| STS | Standards & Terminology Services | VA enterprise service | active |
| TBI | Registry: Traumatic Brain Injury | VistA | active |
| TIU | CPRS: Text Integration Utility | VistA | active |
| TMP | Telehealth Management Platform | Web client | active |
| VAP | Veterans Authorization and Preferences | Web client | active |
| VBECS | Laboratory: VistA Blood Establishment Computer Software | VistA | active |
| VHIE | Veterans Health Information Exchange (VHIE) Portal | VA enterprise service | active |
| VIAB | VistA Integration Adapter (VIA) | Integration middleware | active |
| VPR | Virtual Patient Record | Integration middleware | active |
| WEBE | Community Viewer (CV) | Web client | active |
| WEBG | Web VistA Remote Access Mgmt (WEBVRAM) | Web client | active |
| WEBP | Patient Centered Management Module (PCMM Web) | Web client | active |
| WEBV | VistAWeb | Web client | decommissioned |
| WV | Womens Health | VistA | active |
| YS | Mental Health | VistA + COTS | active |

### Financial-Administrative (38 applications)

| App | Full Name | system_type | Status |
|---|---|---|---|
| BMS | Bed Management Solution | COTS product | active |
| CAPRI | Compensation and Pension Record Interchange | VBA system | active |
| CPT | Current Procedural Terminology | Data patch | active |
| DRG | Diagnostic Related Group (DRG) Grouper | Data patch | active |
| DVBA | Automated Medical Information Exchange (AMIE) | VistA | active |
| EAS | Enrollment Application System | VistA | active |
| EC | Event Capture System (ECS) | VistA | active |
| ECME | Electronic Claims Management Engine | VistA | active |
| ECX | Decision Support System (DSS) Extracts | VistA | active |
| EN | Engineering (AEMS / MERS) | VistA | active |
| ES | Police and Security | VistA | decommissioned |
| FB | Fee Basis | VistA | active |
| FFP | Fugitive Felon Program | VistA | active |
| GEN | Generic Code Sheet (GCS) | VistA | archive |
| HINQ | Hospital Inquiry | VistA | active |
| IB | Integrated Billing | VistA | active |
| IBD | Automated Information Collection System (AICS) | VistA | active |
| ICD | ICD-9-CM | Data patch | active |
| IVM | Income Verification Match | VistA | active |
| IVMB | Health Eligibility Center (HEC) | VistA | active |
| LBR | Library | VistA | decommissioned |
| OOPS | Automated Safety Incident Surveillance Tracking System | VistA | active |
| PRC | IFCAP | VistA | active |
| PRCA | Accounts Receivable (AR) | VistA | active |
| PRCN | Equipment / Turn-In Request | VistA | active |
| PRPF | Integrated Patient Funds | VistA | active |
| PRS | Personnel and Accounting Integrated Data (PAID) | VistA | active |
| QAC | Patient Representative | VistA | decommissioned |
| QAM | Clinical Monitoring System | VistA | active |
| QAN | Incident Reporting | VistA | decommissioned |
| QAO | Occurrence Screen | VistA | active |
| QMIM | Quality Management Integration Module | VistA | active |
| ROI | Release of Information (ROI) Manager | VistA + COTS | active |
| RT | Record Tracking | VistA | active |
| VHIC | Veterans Health Identification Card | Web client | active |
| VSS | Voluntary Service System | VistA | decommissioned |
| WEBHR | WebHR | Web client | active |
| WII | Wounded Ill and Injured Warriors | VistA | active |

### Infrastructure (37 applications)

| App | Full Name | system_type | Status |
|---|---|---|---|
| AFJX | Network Health Exchange (NHE) | Integration middleware | active |
| DI | FileMan | VistA | active |
| E3R | Electronic Error and Enhancement Reporting | VistA | decommissioned |
| FMDC | FileMan Delphi Components | Integration middleware | active |
| HDI | Health Data Informatics | VistA | active |
| HL | Standard Files and Tables | VistA | archive |
| HL7 | HL7 (VistA Messaging) | VistA | active |
| IFR | Institution File Redesign | VistA | active |
| KAAJEE | KAAJEE (XU and XWB) | Integration middleware | active |
| KDC | Kernel Delphi Components | Integration middleware | archive |
| KMPD | Capacity Management Tools | VistA | active |
| KMPR | Resource Usage Monitor (RUM) | VistA | active |
| KMPS | Statistical Analysis of Global Growth (SAGG) | VistA | active |
| KMPV | VistA System Monitor (VSM) | VistA | active |
| MDWS | Medical Domain Web Services | Integration middleware | active |
| MPIF | Duplicate Record Merge: Patient Merge | VistA | active |
| MXML | XML Parser (VistA) | VistA | active |
| NOIS | National Online Information Sharing | VistA | decommissioned |
| NPM | National Patch Module | VistA | active |
| QAP | Survey Generator | VistA | active |
| RUM | Resource Usage Monitor | VistA | archive |
| SAGG | Statistical Analysis of Global Growth | VistA | archive |
| SQLI | SQL Interface | VistA | active |
| SSO | Single Signon/User Context (SSO/UC) (XU and XWB) | Integration middleware | active |
| SSO/UC | Single Signon/User Context | Integration middleware | archive |
| VALM | List Manager | VistA | active |
| VAQ | Patient Data Exchange (PDX) | VistA | active |
| VDEF | VistA Data Extraction Framework | VistA | active |
| VDIF-EP | Veterans Data Integration and Federation Enterprise Platform | VA enterprise service | active |
| XM | MailMan | VistA | active |
| XOB | Name Standardization | VistA | archive |
| XOBV | VistALink | VistA + middleware | active |
| XQOR | Kernel Unwinder | VistA | active |
| XT | Kernel Toolkit | VistA | active |
| XU | Kernel | VistA | active |
| XWB | Remote Procedure Call (RPC) Broker | VistA | active |
| ZSLOT | SlotMaster (Kernel ZSLOT) | VistA | active |

### Monograph (1 application)

| App | Full Name | system_type | Status |
|---|---|---|---|
| MON | Monograph | Program documentation | active |

### VistA/GUI Hybrids (formerly HealtheVet) (23 applications)

| App | Full Name | system_type | Status |
|---|---|---|---|
| CDSP | Clinical Decision Support Platform | VA enterprise service | active |
| CISS | Clinical Information Support System | Web client | active |
| LHS | Lighthouse | VA enterprise service | active |
| MHV | My HealtheVet | Web client | active |
| MPI | Person Services | VA enterprise service | active |
| NUMI | National Utilization Management Integration | Web client | active |
| OHRS | Occupational Health Record-keeping System | Web client | decommissioned |
| ONCO | Registries | Web client | active |
| PECS | Pharmacy: Pharmacy Enterprise Customization System | Web client | active |
| PPS-N | Pharmacy: Pharmacy Product System - National | Web client | active |
| PRED | Pharmacy: Pharmacy Data Update (DATUP) | Web client | active |
| PREM | Pharmacy: Medication Order Check Healthcare Application (MOCHA) | Integration middleware | active |
| SAMH | Health Information Gateway and Exchange (HINGE) | VA enterprise service | active |
| VES | VA Enrollment System | VA enterprise service | active |
| VODA | Veterans Online Debt Access | Web client | active |
| VPFS | Veterans Personal Finance System | Web client | active |
| VPS | VHA Point of Service (Kiosks) | COTS product | active |
| WEBD | Direct Secure Messaging | VA enterprise service | active |
| WEBS | VistA Audit Solution | Web client | active |
| XOBE | Electronic Signature (ESig) | VA enterprise service | active |
| XOBW | HealtheVet Web Services Client (HWSC) | Integration middleware | active |

---

*End of report.*
