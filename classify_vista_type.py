#!/usr/bin/env python3
"""
Add (or update) the vista_type and cots_dependent columns in vdl_inventory_enriched.csv.

11-value classification scheme
───────────────────────────────────────────────────────────────────────────
VistA                — M/MUMPS package deployed via KIDS; pure server-side
VistA + GUI          — MUMPS server package AND a dedicated GUI client
                       co-documented under one VDL app entry; the MUMPS side
                       IS VistA, the client is NOT
VistA + COTS         — MUMPS integration/adapter layer AND a COTS system
                       co-documented; the MUMPS side IS VistA, the COTS is NOT
VistA + middleware   — MUMPS server component (KIDS-deployed) AND a non-VistA
                       connector/adapter layer co-documented; the M side IS VistA,
                       the connector is NOT (e.g. VistALink M listener + J2EE)
GUI client           — standalone desktop application connecting to VistA;
                       no significant MUMPS server component
Web client           — web or mobile application accessing VistA data
Integration middleware — adapter/bridge between VistA and external systems;
                       no clinical/administrative functionality of its own
VA enterprise service — separate national VA platform, service, or API layer
VBA system           — Veterans Benefits Administration system or tool
COTS product         — commercial off-the-shelf software; no VistA MUMPS side
Data patch           — KIDS build that delivers reference data, not M routines;
                       includes licensed code sets (CPT, ICD), commercial
                       classification algorithms (DRG), and terminology packages
Program documentation — documents a program or initiative, not a software
                       package (EHRM program docs, VistA Monograph)
───────────────────────────────────────────────────────────────────────────

cots_dependent column
───────────────────────────────────────────────────────────────────────────
Names the specific COTS product a package depends on.  Set on any package
whose function requires a licensed commercial product — whether that COTS
component is co-documented in the VDL entry (VistA + COTS), embedded as a
data license (CPT, DRG), or called as an external service (PREM).
Empty for packages with no COTS dependency.
───────────────────────────────────────────────────────────────────────────

Design rule: every app must fall into exactly one category with zero residual
ambiguity.  The two hybrid categories (VistA + GUI, VistA + COTS) exist
specifically because the VDL groups MUMPS and non-MUMPS components under one
app entry — the KIDS test applies to the MUMPS side, not to the whole entry.
"""

from __future__ import annotations

import csv
import shutil
from collections import Counter
from pathlib import Path

ENRICHED_CSV = Path.home() / "data/vista-docs/inventory/vdl_inventory_enriched.csv"

# ---------------------------------------------------------------------------
# Classification map   key = app_name_abbrev
# ---------------------------------------------------------------------------
# Legend for inline comments
#   (M)       = MUMPS package confirmed; KIDS deployed
#   (M+GUI)   = MUMPS server + GUI client bundled in VDL entry
#   (M+COTS)  = MUMPS integration layer + COTS product bundled in VDL entry
#   (ext)     = external system; VistA has only a stub/config, not the app
# ---------------------------------------------------------------------------

VISTA_TYPE: dict[str, str] = {
    # ════════════════════════════════════════════════════════════════════════
    # VistA — pure MUMPS, KIDS deployed, server-side
    # ════════════════════════════════════════════════════════════════════════
    # ── Infrastructure platform ─────────────────────────────────────────────
    "XU": "VistA",  # (M) Kernel — XU*8.0
    "DI": "VistA",  # (M) VA FileMan — DI*22.2
    "XM": "VistA",  # (M) MailMan — XM*8.0
    "XWB": "VistA",  # (M) RPC Broker M-side — XWB*1.1  (client libs are not VistA)
    "HL7": "VistA",  # (M) HL7 VistA Messaging — HL*1.6
    "HL": "VistA",  # (M) Standard Files and Tables (archive)
    "XT": "VistA",  # (M) Kernel Toolkit — XT*7.3
    "SQLI": "VistA",  # (M) SQL Interface — DI namespace
    "VALM": "VistA",  # (M) List Manager
    "VDEF": "VistA",  # (M) VistA Data Extraction Framework
    "MPIF": "VistA",  # (M) Duplicate Record Merge / MPI adapter
    "MXML": "VistA",  # (M) XML Parser — XT namespace
    "KMPD": "VistA",  # (M) Capacity Management Tools
    "KMPR": "VistA",  # (M) Resource Usage Monitor
    "KMPS": "VistA",  # (M) Statistical Analysis of Global Growth (SAGG)
    "KMPV": "VistA",  # (M) VistA System Monitor
    "RUM": "VistA",  # (M) Resource Usage Monitor (archive)
    "SAGG": "VistA",  # (M) Statistical Analysis of Global Growth (archive)
    "SSO": "VistA",  # (M) Single Signon/User Context — XU namespace
    "SSO/UC": "VistA",  # (M) Single Signon/User Context (archive)
    "IFR": "VistA",  # (M) Institution File Redesign — XU namespace
    "XQOR": "VistA",  # (M) Kernel Unwinder
    "ZSLOT": "VistA",  # (M) SlotMaster
    "VAQ": "VistA",  # (M) Patient Data Exchange (PDX)
    "QAP": "VistA",  # (M) Survey Generator
    "NOIS": "VistA",  # (M) National Online Information Sharing — decommissioned
    "E3R": "VistA",  # (M) Electronic Error and Enhancement Reporting — decommissioned
    "XOB": "VistA",  # (M) Name Standardization (archive)
    "LEX": "Data patch",  # Lexicon Utility — MUMPS wrapper delivering NLM/SNOMED
    # clinical terminology reference data; content is data, not code
    # ── Patient administration ───────────────────────────────────────────────
    "ADT": "VistA",  # (M) Admissions/Discharge/Transfer — DG*5.3
    "DGBT": "VistA",  # (M) Beneficiary Travel — DG sub-package
    "DGJ": "VistA",  # (M) Incomplete Records Tracking — DG sub-package
    "FFP": "VistA",  # (M) Fugitive Felon Program — DG sub-package
    "PRF": "VistA",  # (M) Patient Record Flags — DGPF sub-package
    "PCMM": "VistA",  # (M) Primary Care Management Module — M-side (WEBP is the web app)
    "PAIT": "VistA",  # (M) Patient Appointment Info Transmission — SD sub-module
    "RT": "VistA",  # (M) Record Tracking
    # ── Clinical documentation ───────────────────────────────────────────────
    "OR": "VistA",  # (M) CPRS server package — OR*3.0  (the Delphi GUI is under CPRS)
    "TIU": "VistA",  # (M) Text Integration Utilities — TIU*1.0
    "PX": "VistA",  # (M) Patient Care Encounter (PCE) — PX*1.0
    "GMPL": "VistA",  # (M) Problem List
    "GMRA": "VistA",  # (M) Adverse Reaction Tracking
    "GMRC": "VistA",  # (M) Consult/Request Tracking
    "GMRV": "VistA",  # (M) Vitals/Measurements
    "GMTS": "VistA",  # (M) Health Summary
    "ASU": "VistA",  # (M) Authorization Subscription Utility — CPRS sub-package
    "GMR": "VistA",  # (M) Intake and Output (nursing I&O)
    "VPR": "VistA",  # (M) Virtual Patient Record — MUMPS data extraction API
    "HMP": "VistA",  # (M) Health Management Platform — decommissioned MUMPS
    # ── Clinical specialties ─────────────────────────────────────────────────
    "LR": "VistA",  # (M) Laboratory — LR*5.2
    "LA": "VistA",  # (M) Lab Universal Interface — LA*5.2
    "LEDI": "VistA",  # (M) Lab Electronic Data Interchange — part of LR/LA
    "EPI": "VistA",  # (M) Lab: Emerging Pathogens Initiative
    "POC": "VistA",  # (M) Lab: Point of Care — LA namespace
    "VBECS": "VistA",  # (M) VistA Blood Establishment Computer Software — MUMPS blood bank
    "RA": "VistA",  # (M) Radiology/Nuclear Medicine — RA*5.0
    "SR": "VistA",  # (M) Surgery — SR*3.0
    "SRA": "VistA",  # (M) Surgery Risk Assessment
    "MC": "VistA",  # (M) Medicine
    "NUR": "VistA",  # (M) Nursing
    "FH": "VistA",  # (M) Nutrition and Food Service
    "WV": "VistA",  # (M) Women's Health
    "HBPC": "VistA",  # (M) Home Based Primary Care — HBH namespace
    "RMDS": "VistA",  # (M) RAI/MDS — DGRU namespace; long-term care assessment
    "FIM": "VistA",  # (M) Functional Independence Measurement — RMIM namespace
    "CRHD": "VistA",  # (M) Shift Handoff Tool
    "DRM+": "VistA",  # (M) Dentistry — DENT namespace
    "EDIS": "VistA",  # (M) Emergency Dept Integration Software — EDP namespace
    "MMRS": "VistA",  # (M) MRSA
    "TBI": "VistA",  # (M) Registry: Traumatic Brain Injury
    "ROR": "VistA",  # (M) Registry: Clinical Case — ROR namespace
    "ONC": "VistA",  # (M) Registry: Oncology
    "NCR": "VistA",  # (M) Registry: National Clozapine Coordination
    "EFR": "VistA",  # (M) Registry: Embedded Fragments
    "ROEB": "VistA",  # (M) Registry: Breast Cancer
    "ROEG": "VistA",  # (M) Registry: Multiple Sclerosis
    "ROEV": "VistA",  # (M) Registry: Military Eye Vision Injury
    "ACKQ": "VistA",  # (M) Quality Audiology and Speech Analysis
    "ANRV": "VistA",  # (M) Blind Rehabilitation — ANRV namespace
    "ONCO": "VistA",  # (M) Registries — MUMPS registry framework
    # ── Pharmacy ────────────────────────────────────────────────────────────
    "PSO": "VistA",  # (M) Outpatient Pharmacy — PSO*7.0
    "PSJ": "VistA",  # (M) Inpatient Pharmacy — PSJ*5.0
    "PSS": "VistA",  # (M) Pharmacy Data Management — PSS*1.0
    "PSB": "VistA",  # (M) BCMA — Bar Code Medication Administration
    "PSD": "VistA",  # (M) Controlled Substances
    "PSX": "VistA",  # (M) Consolidated Mail Outpatient Pharmacy (CMOP)
    "PSN": "VistA",  # (M) National Drug File (NDF)
    "PSU": "VistA",  # (M) Pharmacy Benefits Management
    "PSA": "VistA",  # (M) Pharmacy API
    "PREA": "VistA",  # (M) Pharmacy: Advanced Medication Platform
    "AR/WS": "VistA",  # (M) Pharmacy: Auto Replenish / Ward Stock
    "PPP": "VistA",  # (M) Pharmacy: Prescription Practices (archive)
    # ── Decision support, scheduling, admin ──────────────────────────────────
    "PXRM": "VistA",  # (M) Clinical Reminders — PXRM*2.0
    "SD": "VistA",  # (M) Scheduling — SD*5.3  (EWL sub-entry)
    "RMPR": "VistA",  # (M) Prosthetics
    "AMT": "VistA",  # (M) Anticoagulation Management Tool — OR namespace
    "NUPA": "VistA",  # (M) Patient Assessment Documentation Package
    "ACR": "VistA",  # (M) Ambulatory Care Reporting — part of SD
    "ASCD": "VistA",  # (M) Automated Service Connected Designation
    "MJCF": "VistA",  # (M) Bar Code Expansion (BCE)
    "ORRC": "VistA",  # (M) Care Management — decommissioned
    "SOW": "VistA",  # (M) Social Work — decommissioned
    "SPN": "VistA",  # (M) Spinal Cord Dysfunction — decommissioned
    "ICR": "VistA",  # (M) Immunology Case Registry — decommissioned
    # ── VistA ↔ external-system interface packages ───────────────────────────
    # These are KIDS-deployed MUMPS packages whose job is to interface VistA
    # with a national VA service.  The VistA M package IS VistA; the national
    # service it talks to is NOT.  The VDL entry documents the VistA side.
    "DVBA": "VistA",  # (M) AMIE — Automated Medical Information Exchange DVBA*2.7
    # VistA MUMPS package that sends exam data to VBA/CAPRI.
    # The VBA client is CAPRI (separate VDL entry, "VBA system").
    "IVMB": "VistA",  # (M) Health Eligibility Center interface — IVMB*2.x
    # VistA-side MUMPS package for income verification and means
    # test sharing with the national HEC.  Has real KIDS patches.
    "CHDS": "VistA",  # (M) CHDR — Clinical Data Repository CHDS*2.2
    # VistA-side MUMPS extractor that sends clinical data to the
    # national Health Data Repository (HDR).  Has KIDS installation.
    # ── Financial / billing ──────────────────────────────────────────────────
    "IB": "VistA",  # (M) Integrated Billing — IB*2.0
    "PRCA": "VistA",  # (M) Accounts Receivable — PRCA*4.5
    "ECME": "VistA",  # (M) Electronic Claims Management Engine
    "EC": "VistA",  # (M) Event Capture System
    "ECX": "VistA",  # (M) DSS Extracts — MUMPS data extraction
    "FB": "VistA",  # (M) Fee Basis
    "PRC": "VistA",  # (M) IFCAP — PRC*5.1
    "PRCN": "VistA",  # (M) Equipment / Turn-In Request (IFCAP sub-module)
    "PRPF": "VistA",  # (M) Integrated Patient Funds
    "PRS": "VistA",  # (M) PAID — Personnel and Accounting
    "IBD": "VistA",  # (M) AICS (Automated Information Collection System)
    "EN": "VistA",  # (M) Engineering (AEMS/MERS)
    "GEN": "VistA",  # (M) Generic Code Sheet (archive)
    "LBR": "VistA",  # (M) Library — decommissioned
    "VSS": "VistA",  # (M) Voluntary Service System — decommissioned
    "QAC": "VistA",  # (M) Patient Representative — decommissioned
    "QAN": "VistA",  # (M) Incident Reporting — decommissioned
    "OOPS": "VistA",  # (M) Automated Safety Incident Surveillance
    "QAM": "VistA",  # (M) Clinical Monitoring System
    "QAO": "VistA",  # (M) Occurrence Screen
    "QMIM": "VistA",  # (M) Quality Management Integration Module
    "WII": "VistA",  # (M) Wounded Ill and Injured Warriors
    "ES": "VistA",  # (M) Police and Security — decommissioned
    # ════════════════════════════════════════════════════════════════════════
    # VistA + GUI — MUMPS server + GUI client bundled in one VDL entry
    # The MUMPS server side IS VistA; the client is NOT.
    # Use this when the VDL app entry conflates both under one abbrev.
    # ════════════════════════════════════════════════════════════════════════
    "CPRS": "VistA + GUI",  # OR*3.0 (MUMPS) + Delphi Windows GUI client
    # OR server docs are VistA; CPRS GUI is a Delphi app
    # Both documented under app_name_abbrev=CPRS in VDL
    "MAG": "VistA + GUI",  # MAG MUMPS server (image indexing/linking) +
    # Windows VistA Imaging workstation (large C++ app)
    # Both documented under app_name_abbrev=MAG in VDL
    # ════════════════════════════════════════════════════════════════════════
    # VistA + COTS — MUMPS integration layer + COTS system, co-documented
    # The MUMPS integration layer IS VistA; the COTS system is NOT.
    # ════════════════════════════════════════════════════════════════════════
    "MD": "VistA + COTS",  # MD namespace: MUMPS bridge that passes results from
    # COTS clinical device systems (bedside monitors, EKG,
    # Holter) into VistA/CPRS via HL7
    "YS": "VistA + COTS",  # YS*5.01 MUMPS package (legacy mental health) +
    # COTS Mental Health Suite (DSIU) for treatment plans;
    # both documented together under app_name_abbrev=YS
    "ROI": "VistA + COTS",  # DSIR namespace: MUMPS VistA-side module +
    # COTS Release of Information system (DSSI vendor)
    # integrated for ROI workflow
    # ════════════════════════════════════════════════════════════════════════
    # GUI client — desktop application only; no MUMPS server component
    # ════════════════════════════════════════════════════════════════════════
    # (Note: CPRS Delphi GUI is part of the "VistA + GUI" CPRS entry above;
    #  no standalone GUI-client-only apps remain as separate VDL entries)
    # ════════════════════════════════════════════════════════════════════════
    # Web client — web or mobile application accessing VistA data
    # ════════════════════════════════════════════════════════════════════════
    "JLV": "Web client",  # Joint Longitudinal Viewer — VA/DoD web viewer
    "WEBP": "Web client",  # PCMM Web — J2EE care team management
    "WEBV": "Web client",  # VistAWeb — decommissioned web viewer (Feb 2020)
    "WEBE": "Web client",  # Community Viewer (CV)
    "WEBG": "Web client",  # Web VistA Remote Access Management (WEBVRAM)
    "WEBHR": "Web client",  # WebHR — web-based HR application
    "MBAA": "Web client",  # Mobile Scheduling Applications Suite
    "EPSI": "Web client",  # Enterprise Precision Scanning and Indexing
    "MED": "Web client",  # Mobile Electronic Documentation — mobile app using TIU
    "ROES": "Web client",  # Remote Order Entry System
    "CCRA": "Web client",  # Community Care Referral and Authorization
    "PECS": "Web client",  # Pharmacy Enterprise Customization System (HealtheVet)
    "PRED": "Web client",  # Pharmacy Data Update / DATUP (HealtheVet)
    "PPS-N": "Web client",  # Pharmacy Product System - National
    "MHV": "Web client",  # My HealtheVet — Veteran-facing portal
    "NUMI": "Web client",  # National Utilization Management Integration
    "VODA": "Web client",  # Veterans Online Debt Access
    "VPFS": "Web client",  # Veterans Personal Finance System — J2EE
    "WEBS": "Web client",  # VistA Audit Solution
    "SAMH": "Web client",  # Health Information Gateway and Exchange (HINGE)
    # ════════════════════════════════════════════════════════════════════════
    # VistA + middleware — MUMPS component (KIDS) + non-VistA connector layer
    # Same pattern as VistA + GUI and VistA + COTS: the M side IS VistA;
    # the connector/adapter side is NOT.
    # ════════════════════════════════════════════════════════════════════════
    "XOBV": "VistA + middleware",  # XOBV*1.x: VistA-side M listener (KIDS-deployed) +
    # J2EE WebLogic connector layer (not VistA).
    # The M listener enables external Java apps to call
    # VistA RPCs; both sides documented under XOBV in VDL.
    # ════════════════════════════════════════════════════════════════════════
    # Integration middleware — adapter or bridge; no clinical/admin function
    # ════════════════════════════════════════════════════════════════════════
    "KAAJEE": "Integration middleware",  # Kernel Auth for J2EE — interim web auth
    "VIAB": "Integration middleware",  # VistA Integration Adapter (VIA API layer)
    "MDWS": "Integration middleware",  # Medical Domain Web Services — SOAP layer over VistA
    "AFJX": "Integration middleware",  # Network Health Exchange — HL7 routing middleware
    "FMDC": "Integration middleware",  # FileMan Delphi Components — client library
    "KDC": "Integration middleware",  # Kernel Delphi Components — client library (archive)
    "XOBE": "Integration middleware",  # Electronic Signature service (ESig)
    "XOBW": "Integration middleware",  # HealtheVet Web Services Client (HWSC)
    "TMP": "Integration middleware",  # Telehealth Mgmt Platform — (ext) external telehealth
    # platform; VistA has HL7 stubs only, not the system
    "PREM": "Integration middleware",  # MOCHA drug-check server — (ext) Java/WebLogic service;
    # VistA calls it; pkg_ns=PREM refers to config stubs only
    # ════════════════════════════════════════════════════════════════════════
    # VA enterprise service — separate national VA platform or API layer
    # ════════════════════════════════════════════════════════════════════════
    "HDR": "VA enterprise service",  # HDR - Historical (same platform, legacy entry)
    "VHIE": "VA enterprise service",  # Veterans Health Information Exchange Portal
    "NHIN": "VA enterprise service",  # Nationwide Health Information Network Adapter
    "ETS": "VA enterprise service",  # Enterprise Terminology Service
    "STS": "VA enterprise service",  # Standards & Terminology Services
    "VAP": "VA enterprise service",  # Veterans Authorization and Preferences
    "EAS": "VA enterprise service",  # Enrollment Application System (national)
    "IVM": "VA enterprise service",  # Income Verification Match — national VA/IRS service
    "HINQ": "VA enterprise service",  # Hospital Inquiry — national VA inquiry service
    "VHIC": "VA enterprise service",  # Veterans Health ID Card — national card issuance
    "VES": "VA enterprise service",  # VA Enrollment System — national enrollment platform
    "MPI": "VA enterprise service",  # Person Services / MPI — national identity service
    "LHS": "VA enterprise service",  # Lighthouse — VA API platform for external developers
    "CDSP": "VA enterprise service",  # Clinical Decision Support Platform
    "CISS": "VA enterprise service",  # Clinical Information Support System
    "WEBD": "VA enterprise service",  # Direct Secure Messaging — DirectTrust network
    "OHRS": "VA enterprise service",  # Occupational Health Record-keeping — decommissioned
    "NPM": "VA enterprise service",  # National Patch Module (FORUM) — national patch coord
    "HDI": "VA enterprise service",  # Health Data Informatics
    "VDIF-EP": "VA enterprise service",  # Veterans Data Integration and Federation
    "DHT": "VA enterprise service",  # Home Telehealth — VA program using COTS devices/platforms
    # ════════════════════════════════════════════════════════════════════════
    # VBA system — Veterans Benefits Administration tools and interfaces
    # ════════════════════════════════════════════════════════════════════════
    "CAPRI": "VBA system",  # Compensation & Pension Record Interchange — VBA rating tool
    # (the VBA-side client; the VistA side is DVBA below)
    # NOTE: DVBA is the VistA MUMPS package for AMIE and lives in the VistA section above.
    # ════════════════════════════════════════════════════════════════════════
    # COTS product — commercial software; no VistA MUMPS component
    # ════════════════════════════════════════════════════════════════════════
    "BMS": "COTS product",  # Bed Management Solution — TeleTracking commercial product
    "CRMS": "COTS product",  # Customer Relationship Management — Salesforce
    "VPS": "COTS product",  # VHA Point of Service Kiosks — commercial kiosk hardware/SW
    # ════════════════════════════════════════════════════════════════════════
    # Data patch — KIDS build delivering reference data, not M routines.
    # These ship as KIDS patches but their payload is data tables or licensed
    # terminology, not executable MUMPS code.
    # ════════════════════════════════════════════════════════════════════════
    "CPT": "Data patch",  # Current Procedural Terminology — AMA-licensed code set;
    # installed via KIDS as a data-only patch
    "ICD": "Data patch",  # ICD-9/10-CM — WHO/CMS diagnostic code set;
    # installed via KIDS as a data-only patch
    "DRG": "Data patch",  # DRG Grouper — 3M commercial classification algorithm
    # and weight tables; installed via KIDS as a data-only patch
    # ════════════════════════════════════════════════════════════════════════
    # Program documentation — not software; documents a program or initiative
    # ════════════════════════════════════════════════════════════════════════
    "EHM": "Program documentation",  # Electronic Health Modernization — Oracle Cerner
    # EHRM program docs; not a software package
    "MON": "Program documentation",  # VistA Monograph — catalog of VistA packages;
    # documentation artifact, not a package itself
}

# ---------------------------------------------------------------------------
# COTS dependency map   key = app_name_abbrev, value = COTS product name
# Set on any package that cannot function without a specific commercial product.
# Empty string = no COTS dependency.
# ---------------------------------------------------------------------------

COTS_DEPENDENCY: dict[str, str] = {
    # VistA + COTS — MUMPS side wraps or calls the named COTS product
    "MD": "COTS clinical device systems (EKG/Holter/bedside monitors)",
    "YS": "Netsmart Mental Health Suite (treatment planning / DSIU)",
    "ROI": "COTS ROI vendor system (Ciox / DSSI)",
    # Data patch — content requires a commercial license
    "CPT": "AMA CPT code set (commercial license required)",
    "DRG": "3M DRG Grouper (commercial classification algorithm + weight tables)",
    # Integration middleware — calls an external COTS service
    "PREM": "First Databank drug interaction service (MOCHA dosing checks)",
}

# ---------------------------------------------------------------------------
# Rationale notes for the four new categories (for the printed report)
# ---------------------------------------------------------------------------

NEW_CATEGORY_RATIONALE = {
    "VistA + GUI": (
        "The VDL bundles MUMPS server documentation and GUI client documentation under "
        "a single app entry. The MUMPS server IS VistA (KIDS-deployed); the GUI client "
        "is not. This category preserves the distinction without splitting the VDL entry."
    ),
    "VistA + COTS": (
        "The VDL bundles a MUMPS integration/adapter layer and a COTS system under a "
        "single app entry. The MUMPS layer IS VistA; the COTS system is not. Typically "
        "the MUMPS side handles VistA data plumbing while the COTS side provides the "
        "clinical application or algorithm."
    ),
    "VistA + middleware": (
        "The VDL entry documents both a KIDS-deployed MUMPS component and a non-VistA "
        "connector/adapter layer. The M component IS VistA (passes the KIDS test); the "
        "connector is not. Identified by the same bundling pattern as VistA+GUI and "
        "VistA+COTS. XOBV (VistALink) is the canonical case: M-side RPC listener "
        "installed via KIDS + J2EE WebLogic connector that is external to VistA."
    ),
    "Data patch": (
        "CPT, ICD, DRG, and LEX are KIDS builds whose payload is reference data or "
        "licensed terminology, not executable M routines. 'Data patch' is the correct "
        "VistA-idiomatic term. The earlier label 'Standards/data' was accurate but "
        "not VistA-specific; 'COTS product' was worse — it implied an installable "
        "application, which is incorrect."
    ),
    "Program documentation": (
        "EHM documents the Oracle Cerner EHRM program; MON is a catalog of VistA "
        "packages. Neither is a software system of any kind. Forcing them into 'VA "
        "enterprise service' misrepresented them as deployable platforms."
    ),
}


def classify_row(row: dict) -> tuple[str, str]:
    abbrev = row.get("app_name_abbrev", "")
    vista_type = VISTA_TYPE.get(abbrev, "unclassified")
    cots_dep = COTS_DEPENDENCY.get(abbrev, "")
    return vista_type, cots_dep


def main() -> None:
    with open(ENRICHED_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    # Insert vista_type after app_status if not present
    if "vista_type" not in fieldnames:
        idx = fieldnames.index("app_status") + 1
        fieldnames.insert(idx, "vista_type")

    # Insert cots_dependent immediately after vista_type
    if "cots_dependent" not in fieldnames:
        idx = fieldnames.index("vista_type") + 1
        fieldnames.insert(idx, "cots_dependent")

    for row in rows:
        row["vista_type"], row["cots_dependent"] = classify_row(row)

    backup = ENRICHED_CSV.with_suffix(".csv.bak")
    shutil.copy2(ENRICHED_CSV, backup)

    with open(ENRICHED_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Backup : {backup}")
    print(f"Updated: {ENRICHED_CSV}")
    print()

    # ── Per-app summary ──────────────────────────────────────────────────────
    seen: dict[str, str] = {}
    for row in rows:
        a = row["app_name_abbrev"]
        if a not in seen:
            seen[a] = row["vista_type"]

    app_counts = Counter(seen.values())
    row_counts = Counter(r["vista_type"] for r in rows)
    total_apps = len(seen)
    total_rows = len(rows)

    ORDER = [
        "VistA",
        "VistA + GUI",
        "VistA + COTS",
        "VistA + middleware",
        "GUI client",
        "Web client",
        "Integration middleware",
        "VA enterprise service",
        "VBA system",
        "COTS product",
        "Data patch",
        "Program documentation",
        "unclassified",
    ]

    print(f"{'Category':<26}  {'Apps':>5} {'%':>4}   {'Rows':>6} {'%':>4}")
    print("─" * 56)
    for cat in ORDER:
        ac = app_counts.get(cat, 0)
        rc = row_counts.get(cat, 0)
        if ac == 0 and rc == 0:
            continue
        ap = ac / total_apps * 100
        rp = rc / total_rows * 100
        marker = "  ← new" if cat in NEW_CATEGORY_RATIONALE else ""
        print(f"  {cat:<24}  {ac:>5} {ap:>3.0f}%   {rc:>6} {rp:>3.0f}%{marker}")
    print("─" * 56)
    print(f"  {'TOTAL':<24}  {total_apps:>5}        {total_rows:>6}")
    print()

    # ── Unclassified ─────────────────────────────────────────────────────────
    unclassified = [a for a, t in seen.items() if t == "unclassified"]
    if unclassified:
        print(f"UNCLASSIFIED ({len(unclassified)}):")
        for a in sorted(unclassified):
            row0 = next(r for r in rows if r["app_name_abbrev"] == a)
            print(f"  {a:12}  ns={row0['pkg_ns']:8}  {row0['app_name_full'][:55]}")
        print()
    else:
        print("No unclassified apps.\n")

    # ── COTS dependency summary ───────────────────────────────────────────────
    cots_apps = {a: COTS_DEPENDENCY[a] for a in sorted(COTS_DEPENDENCY)}
    print("COTS DEPENDENCIES\n")
    for app, dep in cots_apps.items():
        vt = seen.get(app, "?")
        print(f"  {app:<8}  [{vt}]")
        print(f"           {dep}")
    print()

    # ── New-category rationale ────────────────────────────────────────────────
    print("NEW CATEGORIES — rationale\n")
    for cat, apps in [
        ("VistA + GUI", [a for a, t in seen.items() if t == "VistA + GUI"]),
        ("VistA + COTS", [a for a, t in seen.items() if t == "VistA + COTS"]),
        ("VistA + middleware", [a for a, t in seen.items() if t == "VistA + middleware"]),
        ("Data patch", [a for a, t in seen.items() if t == "Data patch"]),
        ("Program documentation", [a for a, t in seen.items() if t == "Program documentation"]),
    ]:
        print(f"  {cat}  →  {', '.join(sorted(apps))}")
        for line in NEW_CATEGORY_RATIONALE[cat].split(". "):
            if line.strip():
                print(f"    {line.strip()}.")
        print()


if __name__ == "__main__":
    main()
