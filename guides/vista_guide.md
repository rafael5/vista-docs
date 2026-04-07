# VistA: A Comprehensive Guide

*Based on the VA VistA Documentation Library (VDL) — 44 packages, ~1,500 markdown documents*
*Last updated: 2026-03-24*

---

## Table of Contents

- [Part I: What Is VistA?](#part-i-what-is-vista)
- [Part II: What Is NOT VistA](#part-ii-what-is-not-vista)
- [Part III: VistA Architecture](#part-iii-vista-architecture)
- [Part IV: Infrastructure Platform](#part-iv-infrastructure-platform)
- [Part V: Patient Administration](#part-v-patient-administration)
- [Part VI: Clinical Documentation and Orders](#part-vi-clinical-documentation-and-orders)
- [Part VII: Clinical Specialties](#part-vii-clinical-specialties)
- [Part VIII: Decision Support and Care Coordination](#part-viii-decision-support-and-care-coordination)
- [Part IX: Financial and Administrative](#part-ix-financial-and-administrative)
- [Part X: Enterprise Integration and Viewers](#part-x-enterprise-integration-and-viewers)
- [Part XI: Package Quick Reference](#part-xi-package-quick-reference)
- [Part XII: VistA's Place in the Broader VA Ecosystem](#part-xii-vistas-place-in-the-broader-va-ecosystem)
- [Appendix: Source Materials](#appendix-source-materials)

---


## Part I: What Is VistA?

[Back to TOC](#table-of-contents)

### Working Definition

**VistA (Veterans Information Systems Technology and Architecture)** is the integrated
application-database server that provides the clinical, business, and platform services to support
the operations of all VHA medical centers nationwide.

A precise working definition:

> **VistA is an integrated application database comprised exclusively of MUMPS (M) technology,
> which provides a single integrated platform of over 180 M applications integrated with a single
> shared M database.**

The defining test: *Is an application an M package, versioned and distributed by the KIDS M
packaging system, running in the M-based VistA server?* If yes, it is VistA. If no — regardless
of whether it connects to VistA, integrates with VistA, or is documented in the VDL — it is
not VistA.

### Scope and Scale

- **~187 active packages** registered in VASI (VA System Inventory), July 2023
- **221 applications** documented in the VDL (includes some non-MUMPS entries)
- **~1,500+ sites** nationwide: VAMCs, Community Based Outpatient Clinics (CBOCs),
  Community Living Centers (CLCs), Vet Centers
- **Application Database:** MUMPS (M) — an integrated application and database technology
- **Governance:** VA Office of Information and Technology (OIT), Office of Electronic Health Records
  Management (OEHRM)
- **Custodian:** The VA is the sole custodian of VistA. VistA and all its documentation are
  released to the public domain. Documentation is available on the VA VDL (va.gov/vdl).
  Source code is available via FOIA request.
- **Age:** Origins in the 1970s (DHCP); continuously patched ever since; some packages have 600+
  patch releases

### Key Structural Properties

**Package-based modular architecture.** Each VistA package is a self-contained module with:
- A unique **namespace prefix** (e.g., `OR`, `PSO`, `DI`) — all routines, globals, and files
  use this prefix
- A **version identifier** (e.g., `OR*3.0`, `PSO*7.0`) tracked in the installed file
- **FileMan files** it owns for persistent storage
- **Security keys** it defines to gate access
- **RPCs** (Remote Procedure Calls) it exports to GUI clients
- **DBIA agreements** (Database Integration Agreements) that formally authorize cross-package access

**FileMan is the universal data layer.** All VistA data lives in FileMan files (M globals).
There is no separate SQL engine. The entire data model — 8,000+ files across all packages — is
stored as M globals and described by the FileMan data dictionary.

**KIDS is the universal deployment mechanism.** Every patch, version upgrade, or new package
enters a VistA instance via KIDS (Kernel Installation and Distribution System), which distributes
software via MailMan messages or host files, then installs it into the running system.

**Tight inter-package coupling.** Packages are not independent microservices. They share a
common database, call each other's routines under DBIA agreements, and build on a shared
infrastructure stack. Removing one package typically breaks many others.

---

## Part II: What Is NOT VistA

[Back to TOC](#table-of-contents)

The VDL documents many things that are *not* VistA but that interact with it, connect to it,
or were developed alongside it. Confusing these is a common error.

### 1. GUI Clients (Connect to VistA, Not Part of It)

These are standalone applications that communicate with VistA over the network via RPC Broker
or VistALink, but run outside the MUMPS server. They have their own deployment lifecycle,
version, and codebase.

| Application | Language/Platform | What It Is |
|---|---|---|
| **CPRS** (Computerized Patient Record System) | Delphi (Windows) | The primary clinical GUI — connects to VistA via RPC Broker |
| **VistA Imaging** (MAG) | Windows client | Image capture/display client — connects to VistA + PACS |
| **VistA Scheduling GUI** | C#/.NET (Windows) | Appointment management GUI for SD package |
| **Mental Health Assistant (MHA)** | Web | Instrument administration tool for YS package |

> **Why this matters:** CPRS is documented in the VDL and heavily referenced in VistA package
> documentation. It is the *user interface* for many VistA packages. But CPRS itself is not a
> MUMPS package — it is a Delphi Windows application. Upgrading CPRS does not upgrade the OR
> (CPRS-server) package, and vice versa. The VDL section for CPRS documents both the server
> package (OR) and the GUI client — a source of confusion.

### 2. Web Applications (VA Enterprise Web Systems)

These are J2EE, .NET, or modern web applications deployed on VA application servers. They may
read/write VistA data (via VistALink or APIs), but they are not part of the MUMPS codebase.

| Application | What It Is |
|---|---|
| **PCMM Web** (WEBP) | J2EE web app for care team management — reads/writes SD/PCMM data via VistALink |
| **HealtheVet applications** (PECS, PRED, PREM) | Web-based pharmacy configuration and enterprise systems |
| **JLV** (Joint Legacy Viewer) | Web-based multi-site read-only viewer |
| **VistAWeb** (WEBV, decommissioned) | Web-based read-only viewer — decommissioned February 2020 |
| **Patient Safety Reporting** (various WEB* packages) | Web portals for safety event reporting |

### 3. Integration Middleware (Bridges, Not VistA)

These packages enable external systems to talk to VistA but are not clinical or administrative
MUMPS packages themselves.

| Component | What It Is |
|---|---|
| **VistALink** (XOBV) | J2EE Connector enabling Java applications to call M RPCs — an adapter, not a clinical system |
| **KAAJEE** | Authentication library for J2EE applications — interim web auth solution, being replaced |
| **RPC Broker** (XWB) | *This one straddles the line*: the M-side of the broker (XWB package) IS VistA; the Delphi/Java client libraries are not |

### 4. VA Enterprise Services (Interoperate With VistA, Not Part of It)

These are national VA services — often hosted centrally — that VistA exchanges data with.

| Service | What It Is |
|---|---|
| **Master Veteran Index / MVI** | National patient identity service (assigns ICN). Separate enterprise system — VistA's MPIF package is the *interface* to it, not MVI itself |
| **CHDR** (Clinical Health Data Repository) | VA/DoD data sharing platform — separate from VistA |
| **Enrollment System (ES)** | VA Health Benefits enrollment — national service, VistA integrates |
| **Veterans Information Service Architecture (VIAB/VIA)** | API layer exposing VistA data to external consumers — the adapter is not VistA |
| **VASI** (VA System Inventory) | VA system registry — metadata about VistA, not VistA itself |

### 5. VBA (Veterans Benefits Administration) Systems

VBA and VHA are separate VA entities. VBA has its own systems for disability claims,
compensation, education benefits, and direct deposit. These occasionally appear in VDL-adjacent
documentation but are not part of VistA.

| Item | What It Is |
|---|---|
| **VBA Forms** (VBA_FORM=1 in VDL) | 8 VA benefits forms attached as noise to all VDL app pages — not VistA documentation |
| **CAPRI** | Client application for VBA raters to view VistA clinical records — a *consumer* of VistA, not part of it |
| **Benefits.va.gov / eBenefits** | Veteran-facing VBA web portals — entirely separate |

### 6. COTS (Commercial Off-the-Shelf) Systems Integrated with VistA

| System | What It Is |
|---|---|
| **Mental Health Suite (DSIU)** | COTS treatment planning software integrated with VistA's YS package |
| **PACS systems** | Picture Archiving and Communication Systems — integrated with VistA Imaging via HL7/DICOM |
| **Automated dispensing robots (OPAI)** | Pharmacy automation hardware/software — interfaced to PSO |
| **Anesthesia information systems** | COTS anesthesia software — interfaced to SR via HL7 |
| **External laboratory systems (LIS)** | Third-party lab information systems — interfaced via LA Universal Interface |

### 7. Decommissioned Systems

The VDL retains documentation for systems that are no longer deployed. These are historical
artifacts, not current VistA.

Notable decommissioned packages: **VistAWeb** (Feb 2020), **Kernel Toolkit** (XT, legacy),
**NOIS** (Problem Tracking, replaced by Remedy/ServiceNow), portions of the **Mental Health** (YS)
legacy package.

---

## Part III: VistA Architecture

[Back to TOC](#table-of-contents)

### The Three-Layer Model

The entire VistA stack is M technology — every layer is comprised exclusively of MUMPS (M) code
running in an M application server. The GUI clients, web apps, and hosting platform sit outside
this stack and are not VistA.

```
  GUIs & Web Apps (NOT VistA)
  CPRS · VistA Imaging · PCMM Web · JLV · HealtheVet
  ↕ RPC Broker / VistALink / HL7 / APIs
┌─────────────────────────────────────────────────────────────┐
│  Layer 3 — Clinical & Administrative M Packages (~180+)     │
│  Lab · Pharmacy · ADT · Surgery · Scheduling · Billing      │
│  CPRS-server (OR) · TIU · PCE · Reminders · Consults       │
├─────────────────────────────────────────────────────────────┤
│  Layer 2 — Infrastructure M Packages                        │
│  FileMan (DI) — DBMS (M database management system)        │
│  Kernel (XU) — OS portability layer                         │
│  RPC Broker (XWB) — client interface                        │
│  HL7 (HL) — system interfacing                              │
├─────────────────────────────────────────────────────────────┤
│  Layer 1 — M Database                                       │
│  Persistent M globals — the single shared VistA database    │
└─────────────────────────────────────────────────────────────┘
  Server Hosting Platform (NOT VistA)
  AWS GovCloud (Linux)
```

**M application server implementations** (any can host the VistA stack):
- InterSystems IRIS (and legacy Caché)
- Fidelity GT.m
- YottaDB

**Hosting platform:** All VistA servers have been migrated to Linux and are hosted on a single,
secure, centralized commercial cloud platform — Amazon Web Services (AWS) GovCloud. There are
no remaining instances of VistA on OpenVMS.

### Integration Mechanisms

| Mechanism | Used By | Purpose |
|---|---|---|
| **DBIA** (Database Integration Agreement) | M-to-M | Authorized cross-package routine calls |
| **RPCs** (Remote Procedure Calls) | GUI clients → VistA | GUI applications calling M routines |
| **HL7 messages** | VistA ↔ external systems | Structured health data exchange |
| **MailMan messages** | VistA ↔ VistA (inter-facility) | Patch distribution, alerts, data |
| **FileMan APIs** (LIST^DIC, GETS^DIQ, etc.) | Any package → FileMan | Database read/write |
| **VistALink (JCA)** | Java apps → VistA | J2EE connector for M RPCs |

---

## Part IV: Infrastructure Platform

[Back to TOC](#table-of-contents)

These packages form the foundation on which all other VistA packages run. Every clinical and
administrative package depends on all of them.

---

### Kernel — `XU*8.0`

**The operating system abstraction layer.** Kernel makes VistA portable across M implementations
and operating systems by providing a consistent API for all OS-level services.

**What it provides:**
- **Sign-on and security** — user authentication, access/verify codes, device restrictions,
  time-of-day and day-of-week access controls; full audit trail by user, device, program, file, field
- **Menu Manager** — standardized hierarchical menus across all applications; per-user customization
- **KIDS** (Kernel Installation and Distribution System) — packages and installs patches via
  MailMan or host files; the universal software distribution mechanism
- **Task Manager** — background job scheduling (like cron for VistA)
- **Device Handler** — abstracts terminal types; standardizes I/O
- **Error processing** — consistent error recording and recovery
- **Library functions** — date arithmetic, string manipulation, math, trigonometry, DNS resolution
- **ZOSF/ZOSV** — OS interface layer that insulates applications from platform specifics

**Every VistA package depends on Kernel.** It is the OS of VistA.

---

### VA FileMan — `DI*22.2`

**The database management system.** All VistA clinical and administrative data is stored in
FileMan files (M globals), described by a data dictionary.

**What it provides:**
- **Relational data model** in M globals — files (tables), fields, cross-references (indexes)
- **Data dictionary** — schema definitions for every file in the system; introspectable at runtime
- **Form-based data entry** — standardized input/output for terminal applications
- **Query and reporting** — flexible ad-hoc queries, print templates, sort templates
- **Import/export** — data interchange with external systems
- **Archiving and transport** — data archiving, inter-system data transfers
- **Keys and compound cross-references** — unique constraints and complex indexing
- **Client-server access** — APIs for GUI applications to read/write data (GETS^DIQ, FILE^DIE, etc.)

**Every VistA package stores data in FileMan files.** The complete VistA data model — clinical
records, patient demographics, drug files, scheduling data, billing records — lives in FileMan.

FileMan file numbers are the global addressing scheme:
| File Number Range | Domain |
|---|---|
| 0–99 | Kernel/infrastructure |
| 100–199 | CPRS / Orders |
| 200 | New Person (users) |
| 350–389 | Billing (IB) |
| 404.x | Scheduling / PCMM |
| 560.x | Virtual Patient Record |
| 771+ | HL7 |
| 8925.x | TIU documents |
| 8994 | Remote Procedures (RPCs) |
| 9002313.x | ECME/pharmacy claims |

---

### RPC Broker — `XWB*1.1`

**The client-server communication layer.** RPC Broker enables GUI applications running on Windows
workstations (or web servers) to communicate securely with VistA M servers over TCP/IP.

**What it provides:**
- Authenticated TCP connections from GUI clients to M server
- Remote Procedure Call execution — GUI calls M routines by name
- Single sign-on (SSO) and silent sign-on
- CCOW (Clinical Context Object Workgroup) support for patient context synchronization
- M-to-M Broker for inter-facility server communication
- Broker Security Enhancement (BSE) for delegated authentication
- Shared broker (multiple client windows from one workstation = one connection)

**CPRS, VistA Imaging, and all Windows-based VistA clients communicate exclusively via RPC Broker.**
The M-side XWB package IS part of VistA; the Delphi/Java client libraries are not.

---

### MailMan — `XM*8.0`

**The internal messaging and transport layer.** MailMan provides electronic mail for VistA users
and applications, and is the transport vehicle for KIDS patch distribution.

**What it provides:**
- User-to-user electronic mail within and between facilities
- Mail groups for broadcast messaging
- **Bulletins** — automated messages triggered by FileMan field changes (the VistA event system)
- Software distribution — KIDS patches travel as MailMan messages
- TCP/IP transmission to SMTP-compatible external mail systems
- Surrogate mail management

**MailMan bulletins are how VistA packages signal events to each other.** When a lab result is
filed, a bulletin can trigger downstream actions in other packages.

---

### Health Level 7 — `HL*1.6`

**The external interoperability standard.** HL7 enables VistA to exchange structured health data
with external systems — other VistA instances, commercial lab analyzers, PACS systems, DoD, etc.

**What it provides:**
- ANSI HL7 2.x message protocol implementation
- Point-to-point and publish-subscribe messaging
- Transport via HLLP (Hybrid Lower-Level Protocol), MLLP, X3.28
- Message queuing for reliable delivery
- Automatic MSH (message header) generation
- ACK (acknowledgment) handling
- Dynamic message routing
- **HLO** (HL7 Optimized) — redesigned high-throughput variant for modern workloads

**HL7 is how VistA talks to the world outside itself.** Laboratory interfaces with external
analyzers and LEDI (Lab Electronic Data Interchange). ADT sends A01-A13 admit/transfer/discharge
events. Pharmacy sends claims. Radiology interfaces with PACS.

---

### Kernel Toolkit — `XT*7.3`

**Development and quality assessment tools.** Primarily used by VistA developers and system
managers, not end users.

**What it provides:**
- **XINDEX** — checks MUMPS programming standards and namespace adherence
- Portable routine/global editor
- Data standardization utilities
- Error trapping and reporting
- Quality assessment tools for code and data dictionary comparison
- XML data tools

*Note: Kernel Toolkit is largely legacy/maintenance-mode. Many functions have been absorbed into
modern tooling.*

---

### VistALink — `XOBV*1.6`

**Java integration middleware.** VistALink enables J2EE applications and application servers to
call VistA M RPCs, following the J2EE Connectors (JCA) specification.

**What it provides:**
- Synchronous RPC calls from Java clients to M
- J2EE Application Server connectivity (BEA WebLogic, JBoss, etc.)
- JCA compliance for enterprise Java integration
- Authentication via KAAJEE

**VistALink is the bridge between the Java web tier and VistA.** PCMM Web, VPFS, and HealtheVet
applications use VistALink. The XWB/RPC Broker handles Delphi/Windows clients; VistALink handles
Java clients.

---

### KAAJEE — `XU` (subsystem)

**Authentication for Java/J2EE web applications.** KAAJEE (Kernel Authentication & Authorization
for Java 2EE) provides a custom authentication provider for BEA WebLogic servers.

**What it provides:**
- Web form authentication against VistA Kernel user store
- Security key retrieval via VistALink
- Custom WebLogic authentication provider

*Note: KAAJEE is documented as an "interim solution" and was designed for a specific generation
of VA web infrastructure. Modern VA authentication uses PIV cards and enterprise IAM services.*

---

## Part V: Patient Administration

[Back to TOC](#table-of-contents)

These packages manage the patient's identity, eligibility, care relationships, and movement
through the VA healthcare system.

---

### ADT / Registration — `DG*5.3`

**Admissions, Discharge, Transfer, and Patient Registration.** ADT is the focal system for all
patient demographic, eligibility, insurance, and movement data.

**What it does:**
- **Patient registration** — creates and maintains the patient record; initial VA registration
- **Eligibility determination** — verifies eligibility for VA care
- **Means testing** — determines patient financial responsibility for copays
- **Bed control** — tracks patient movements during inpatient stays (census)
- **ADT event generation** — feeds HL7 A01-A13 events to downstream systems (Lab, Pharmacy,
  HL7 interfaces to external systems)
- **Patient Treatment File (PTF)** — generates inpatient episode records for national reporting
- **Sensitive patient records** — restricts access to records of employees, government officials,
  and others requiring special protection
- **VHIC support** — Veterans Health Identification Card issuance
- **MST tracking** — Military Sexual Trauma designation
- **ICD-10 compliance** — diagnosis coding

**ADT is where every patient's record starts.** No clinical activity can occur without a patient
existing in ADT. All other packages retrieve patient demographics from ADT files (primarily
PATIENT file #2).

---

### Master Patient Index / Master Veteran Index — `MPIF*1.0`

**National patient identity service interface.** MPIF is VistA's integration point with the
national MVI/MPI service, which assigns and maintains the ICN (Integration Control Number) —
the unique national identifier for every VA patient.

**What it does:**
- Submits new patient registrations to MVI for ICN assignment
- Resolves duplicate identities across VA facilities
- Synchronizes demographics between local VistA and national MVI
- Enables patient matching with DoD systems (for CHDR/dual consumers)
- Correlates patients with VBA and NCA (National Cemetery Administration) records

*Note: MVI itself is a separate national service, not part of VistA. MPIF is VistA's adapter to it.*

---

### Scheduling — `SD*5.3`

**Outpatient appointment management.** Scheduling manages the complete appointment lifecycle —
clinic setup, booking, check-in/out, cancellations, wait lists, and national workload reporting.

**What it does:**
- **Clinic management** — creates and maintains clinic definitions (fixed/variable patterns,
  availability, overbook limits)
- **Appointment booking** — schedules, reschedules, cancels appointments
- **Electronic wait list (EWL)** — manages patients awaiting appointments
- **Check-in/check-out** — processes patient arrival and departure
- **Cancellation and no-show tracking** — generates patient notification letters
- **National reporting** — transmits workload data to Austin Information Technology Center (AITC)
- **Record Tracking integration** — automatically requests patient chart at appointment booking
- **Ambulatory Care Reporting Project (ACRP)** — encounter-based transmission to national database
- **VistA Scheduling GUI** — separate Windows C#/.NET client application (not MUMPS)

---

### Patient Centered Management Module Web — `WEBP`

**Care team and patient panel management.** PCMM Web manages the Patient-Aligned Care Team
(PACT) model — which providers are on which teams, and which patients are assigned to which teams.

**What it does:**
- Defines care teams by type (Primary Care, Mental Health, Specialty)
- Assigns staff to team positions (RN, pharmacist, social worker, PCP)
- Assigns patients to teams and primary care providers (PCPs)
- Manages patient panel size and workload
- Supports multiple PACT (for Veterans receiving care at multiple sites)
- Automates inactivation of stale assignments (24 months for new, 12 for established patients)
- Synchronizes with VistA PCMM files for legacy software compatibility

*Note: PCMM Web is a J2EE web application (NOT MUMPS). It writes to VistA via VistALink.*

---

### Patient Record Flags — `DGPF` (PRF)

**Patient safety alerting.** Patient Record Flags alert VA staff when a patient has a known risk
profile — behavioral risk, wandering history, harm potential, or other safety-relevant information.

**What it does:**
- Creates and assigns flags to patient records
- Two categories:
  - **Category I (national)** — shared via HL7 to all treating facilities (e.g., Missing Patient)
  - **Category II (local)** — VISN or facility-specific flags
- Displays flags prominently in CPRS when a provider opens the patient record
- Links flags to TIU progress note definitions for documentation
- Routes flag review to designated mail groups

---

## Part VI: Clinical Documentation and Orders

[Back to TOC](#table-of-contents)

These packages support the core clinical workflow: documenting encounters, entering orders, and
recording results.

---

### CPRS Server — `OR*3.0`

**The clinical order management engine.** The CPRS package (`OR`) is the server-side MUMPS
package that manages orders, coversheet data, alerts, and clinical lists. It is what CPRS GUI
(the Windows client) calls via RPC.

*Important distinction: the CPRS GUI client (Delphi application) is NOT this package. `OR*3.0`
is the server-side M package. Together, "CPRS" refers to both, but technically the VistA package
is `OR`.*

**What it does:**
- **Order entry/management** — creates, edits, signs, holds, discontinues all order types
  (lab, pharmacy, radiology, diet, nursing, consult, procedure)
- **Order checks** — real-time clinical decision support: allergy alerts, drug-drug interactions,
  duplicate orders, critical lab values
- **Electronic signature** — validates provider identity and credentials for orders/notes
- **CPRS Coversheet** — assembles active problems, allergies, medications, pending orders,
  recent results, clinical reminders
- **Patient alerts** — generates and routes actionable alerts to providers
- **OE/RR Lists** — team lists, team rosters, care groups for ward/team-based work
- **Reports tab** — aggregates results from Lab, Pharmacy, Radiology, etc. into unified views
- **Inter-facility ordering** — CPRS/Consults for Community Care referrals

---

### Text Integration Utilities — `TIU*1.0`

**Clinical document management.** TIU manages all clinical documentation — progress notes,
discharge summaries, operative reports, consult notes, H&Ps — in a structured, signed, versioned
electronic record.

**What it does:**
- **Document types and templates** — defines all note types; supports point-and-click CPRS
  templates for rapid documentation
- **Electronic signature and authentication** — providers sign notes with access/verify codes;
  cosignature for trainees
- **Addenda, amendments, retraction** — full document lifecycle management
- **Document linking** — attaches images (VistA Imaging), labs, and other data to notes
- **Multiple capture methods** — direct CPRS entry, transcription, voice recognition, ASCII upload
- **Interdisciplinary notes** — multiple authors contributing to a single encounter note
- **TIU text alerts** — automatic alerts to providers based on document content or unsigned status
- **Incomplete Record Tracking (IRT)** — manages unsigned/incomplete documents workflow
- **CWAD** — Crisis Notes, Warning Notes, Allergy notices, Advance Directives postings;
  displayed in CPRS header for every patient

**Document types managed by TIU:**
Progress Notes · Discharge Summaries · Consult Notes · Operative Reports · Procedure Notes ·
H&P (History & Physical) · Advance Directives · Crisis Notes

---

### Patient Care Encounter — `PX*1.0`

**Outpatient encounter data capture.** PCE is the structured clinical repository for ambulatory
encounter data — diagnoses, procedures, immunizations, and patient education.

**What it does:**
- **Long-term encounter repository** — stores structured data from every outpatient visit
- **ICD-10 and CPT capture** — diagnosis codes, procedure codes, stop codes for workload reporting
- **Immunization tracking** — vaccine administration records
- **Patient education documentation** — what was taught, patient comprehension
- **Service connection tracking** — SC conditions, Agent Orange, MST, SHAD, Gulf War status
- **Encounter form scanning** — supports scanned paper encounter forms as data entry method
- **Health Summary components** — PCE data feeds clinical summary views
- **Billing integration** — CPT and stop codes flow to IB for charge capture

---

### Health Summary — `GMTS`

**Synthesized patient summary views.** Health Summary assembles customizable displays of patient
data from multiple packages into a single coherent document.

**What it does:**
- Extracts and formats data from Lab, Pharmacy, Vitals, PCE, TIU, Radiology, ADT, etc.
- Supports customizable component selection per summary type
- Generates printed or online summaries
- Used in CPRS Reports tab as the data backbone

---

### Problem List — `GMPL`

**Persistent patient problem tracking.** The Problem List maintains the longitudinal record of
a patient's active and resolved medical problems.

**What it does:**
- Records ICD-coded diagnoses as active/inactive/removed
- Links problems to Clinical Reminders, PCE encounters, and TIU notes
- Provides continuity across visits and providers
- Feeds CPRS Coversheet problem display

---

### Adverse Reaction Tracking — `GMRA`

**Allergy and adverse reaction documentation.** Tracks all known allergies and adverse reactions
and makes them visible across the patient record.

**What it does:**
- Records drug, food, and other allergies with reaction type and severity
- Provides real-time allergy checking during medication order entry (via CPRS order checks)
- Displays in CPRS CWAD header and Coversheet
- Feeds IB for allergy information on claims

---

## Part VII: Clinical Specialties

[Back to TOC](#table-of-contents)

---

### Laboratory — `LR*5.2` / Universal Interface `LA*5.2`

**Comprehensive laboratory information system.** Laboratory manages lab operations from order
entry through result reporting, for General Lab, Microbiology, Histology, Cytology, Autopsy,
and Electron Microscopy.

**What it does:**
- **Order entry** — lab tests ordered from CPRS, forwarded to appropriate sections
- **Specimen collection** — specimen labels, collection lists, container management
- **Accessioning** — specimen receipt and logging
- **Result entry and verification** — technician entry, supervisor verification, electronic signature
- **Report generation** — result reports to CPRS and Health Summary
- **Lab instrument interfaces** — bidirectional interfaces with automated analyzers
- **LEDI** (Lab Electronic Data Interchange) — HL7 interface with external reference labs
- **Point of Care (POC)** — handheld/bedside testing devices
- **Blood Bank** — blood product management, compatibility testing, transfusion tracking
- **Anatomic Pathology (AP)** — surgical pathology, histology, cytology
- **Billing** — stop codes for lab procedures captured for IB

**LA (Universal Interface):** Standardized interface layer for lab data entry from automated
equipment via HL7.

---

### Radiology/Nuclear Medicine — `RA*5.0`

**Imaging department management.** Radiology automates the complete imaging workflow from order
entry through report generation.

**What it does:**
- **Order entry and scheduling** — radiology procedures ordered from CPRS, scheduled in RA
- **Exam processing** — patient registration for exam, exam status tracking
- **Report entry and verification** — radiologist report entry, physician electronic verification
- **PACS interface** — HL7 messaging to/from Picture Archiving and Communication Systems
- **Nuclear medicine** — radiopharmaceutical tracking and dosimetry
- **Radiation dosage aggregation** — cumulative dose tracking per patient
- **Contrast reaction tracking** — adverse reaction recording
- **Workload reporting** — statistics to national database
- **Mammography tracking** — Women's Health integration
- **Results display** — reports available in CPRS and Health Summary

---

### Surgery — `SR*3.0`

**Operating room and surgical records management.** Surgery manages the complete surgical
workflow — procedure scheduling, intraoperative documentation, post-operative reporting,
and morbidity/mortality tracking.

**What it does:**
- **Surgical request and booking** — procedure requests entered from CPRS, scheduled in OR
- **OR scheduling and utilization** — operating room time management, staff scheduling
- **Intraoperative data entry** — staff, times, anesthesia, diagnoses, complications
- **Nurse Intraoperative Report** — real-time nursing documentation
- **Post-operative report generation** — automatically assembled from intraoperative data
- **Morbidity & Mortality tracking** — structured M&M data for quality reporting
- **Risk assessment** — observed-to-expected ratios; cardiac, trauma, specialty sub-modules
- **HL7 interface** — integration with automated anesthesia information systems (COTS)
- **Quarterly and annual reporting** — data transmission to VA Central Office
- **Billing** — surgical stop codes to IB

---

### Pharmacy — `PSO*7.0 / PSJ*5.0 / PSS*1.0 / PSB / PSU`

**Medication management across the care continuum.** Pharmacy is a suite of tightly integrated
packages covering every aspect of medication dispensing and management.

#### Outpatient Pharmacy — `PSO*7.0`
Manages ambulatory prescription filling, refills, and patient counseling.
- Prescription order entry from CPRS (or direct pharmacy entry)
- Drug interaction checking (MOCHA — Medication Order Check Healthcare Application)
- Prescription label printing; multi-language labels; microchip-embedded labels for visually impaired
- Refill request processing; automated refill via phone/web
- Outpatient Pharmacy Automation Interface (OPAI) — integration with dispensing robots
- Pharmacy copay billing to IB
- State Prescription Monitoring Program (PDMP) reporting
- OneVA Pharmacy — multi-site prescription dispensing
- Inbound ePrescribing from external providers (Surescripts)
- Clozapine dispensing controls

#### Inpatient Pharmacy — `PSJ*5.0`
Manages hospital ward medications — unit dose, IV therapy, and controlled substances.
- Inpatient medication orders from CPRS
- Unit Dose (UD) distribution system
- IV Therapy (large volume, small volume, TPN/hyperalimentation)
- Controlled Substances tracking
- BCMA (Bar Code Medication Administration) integration — confirms right patient/drug/dose/route/time at bedside

#### Pharmacy Data Management — `PSS*1.0`
Maintains the drug information database and orderable items.
- National Formulary maintenance
- Drug file (#50), Pharmacy Orderable Items (#50.7), IV Additives (#52.6)
- Drug accountability tracking
- NDF (National Drug File) — VA's national drug master
- Drug Use Evaluation (DUE) templates
- Procure-to-pay integration with IFCAP

#### Pharmacy Benefits Management — `PSB / PSU`
National medication data collection and analytics.
- Collects dispensing data from all VA facilities
- Drug usage analytics, cost projections, pharmaceutical outcomes

#### Pharmacy Enterprise Customization System — `PECS`
Web-based tool for configuring and managing VA pharmacy formulary and parameters.
*(PECS is a web application, not a MUMPS package.)*

---

### Mental Health — `YS*5.01` / MH Suite (DSIU)

**Mental health and behavioral health services.** Two overlapping systems serve this domain.

**YS (legacy MUMPS package):**
- Computerized psychological test administration and scoring
- DSM-IV/ICD-10 diagnostic interviews
- GAF (Global Assessment of Functioning) scoring
- Mental Health Assistant (MHA) — web-based instrument administration
- Addiction Severity Index (ASI-MV) — multimedia version

**Mental Health Suite (COTS, DSIU namespace):**
- Multidisciplinary treatment plan development
- DSM-5 format compliance
- Risk identification and prevention tools
- JCAHO/CARF accreditation support

*Note: YS is formally "Inactive" in VASI but continues to be used. Mental Health Suite is COTS
software integrated via HL7/RPC.*

---

## Part VIII: Decision Support and Care Coordination

[Back to TOC](#table-of-contents)

---

### Clinical Reminders — `PXRM*2.0`

**Point-of-care decision support.** Clinical Reminders alerts clinicians when patients are due for
preventive care, screenings, disease management interventions, or performance measure compliance.

**What it does:**
- **Clinical data indexing** — maintains a real-time index of clinical findings that trigger reminders
- **Patient identification** — identifies which patients have specific conditions or are due for actions
- **Reminder display in CPRS** — shows actionable reminders in clinical workflow
- **Resolution tracking** — records which clinical activities satisfied the reminder
- **Aggregate reporting** — caseload-level reports on reminder compliance
- **Performance measure support** — tracks VHA national performance measures
- **ICD-10 compliance** — condition-based reminders fire on coded diagnoses

---

### Consult/Request Tracking — `GMRC*3.0`

**Inter-service consultation management.** GMRC enables clinicians to request consultations from
specialists, track consult progress, and record results — creating a permanent record in the chart.

**What it does:**
- **Consult order entry** — ordered from CPRS; intra- or inter-facility routing
- **Status tracking** — pending/active/scheduled/complete lifecycle
- **Notifications** — alerts to requesting and consulting providers at key transitions
- **Results entry** — via TIU-linked consult note templates
- **Prosthetics integration** — home oxygen, eyeglasses, contact lens consults
- **COVID Toolbox** — COVID-19 exposure and status documentation module
- **Consult Toolbox (CTB)** — standardized consult templates for common referral types
- **HL7 communication** — transmits consult data to Healthcare Claims Processing System (HCPS)

---

### Vitals/Measurements — `GMRV*5.0`

**Vital signs and physical measurements.** Stores all vital sign and measurement data in the
patient record and makes it available across CPRS.

**What it does:**
- Records: blood pressure, temperature, pulse, respiration, height, weight, pain score,
  oxygen saturation, CVP, circumference, body mass index
- Both metric and US customary units
- Customizable high/low abnormal value ranges per site
- Graphic trending display
- Vital sign monitor interface (bedside devices)
- Latest vitals summary for CPRS Coversheet
- APIs for other packages to retrieve current values

---

## Part IX: Financial and Administrative

[Back to TOC](#table-of-contents)

---

### Integrated Billing — `IB*2.0`

**Third-party insurance billing and patient copayments.** IB captures billable events from
clinical services, creates insurance claims, and manages the billing lifecycle.

**What it does:**
- **Insurance data management** — company setup, plan benefits, policy information, electronic
  insurance discovery (EICD)
- **Billable event capture** — receives charges from SD (visit), PSO (pharmacy), RA (imaging),
  LR (lab), SR (surgery), Prosthetics
- **Claim creation** — assembles and transmits electronic claims (HIPAA EDI 837)
- **Patient copayment** — calculates and bills pharmacy copays, outpatient visit copays
- **Pre-certification and utilization review** — prior authorization tracking
- **Medicare and commercial insurance** — dual billing capability
- **Electronic payment processing** — EDI 835 Health Care Claim Payment/Advice
- **Medical Care Collections Fund (MCCF)** — third-party collections program
- **Community Care billing** — Non-VA care billing
- **Medal of Honor exemption** — automatic copay waiver

---

### Accounts Receivable — `PRCA*4.5`

**Debt collection and management.** AR manages all debts owed to VA — patient copays, insurance
overpayments, employee overpayments, and third-party debts.

**What it does:**
- **Debt recording and tracking** — receives bills from IB for collection follow-up
- **Payment processing** — cash, check, lockbox bank, and electronic payments
- **EDI 835 processing** — auto-posts electronic insurance payments
- **Interest and administrative charges** — accrues per Treasury regulations
- **Repayment plans** — negotiates and tracks structured repayment agreements
- **Treasury offset** — debt offset against federal payments (tax refunds, SS benefits)
- **Collection agency and DMC referral** — delinquent debt escalation
- **Regional Counsel and DOJ** — legal referral for large debts
- **Community Care debt tracking** — Non-VA care debt management
- **FMS integration** — synchronizes with VA Financial Management System

---

### Electronic Claims Management Engine — `ECME`

**Pharmacy claims processing.** ECME processes and transmits pharmacy and medical claims
electronically to insurance carriers via the BPS (Billing Processing System) namespace.

**What it does:**
- Receives billable pharmacy transactions from PSO (outpatient) and PSJ (inpatient)
- Formats and transmits NCPDP-standard pharmacy claims
- Processes electronic remittance from payers
- Integrates with IB for claim status and payment tracking

---

### IFCAP — `PRC*5.1`

**Procurement, inventory, and financial management.** IFCAP (Integrated Funds Distribution,
Control Point Activity, Accounting and Procurement) manages facility-level budgets, purchasing,
inventory, and payment.

**What it does:**
- Budget management and funds control
- Requisition and purchase order processing
- Vendor comparison and selection
- Receipt, inspection, and acceptance
- Inventory management (GIP — Generic Inventory Package; PIP — Prosthetics)
- EDI transmission to vendors
- Government purchase card payment
- eCMS (electronic Contracting Management System) integration
- AEMS/MERS (Automated Engineering Management System) property management

---

## Part X: Enterprise Integration and Viewers

[Back to TOC](#table-of-contents)

These components extend VistA data to non-VistA consumers or aggregate data from multiple sources.

---

### Joint Legacy Viewer — `JLV`

**Multi-source longitudinal viewer.** JLV allows clinicians to view patient records from multiple
VA facilities and DoD sources through a single web interface, without logging into each system.

**What it does:**
- Aggregates patient data across VA VistA instances
- Displays DoD clinical data (labs, medications, encounters) for dual VA/DoD patients
- Provides longitudinal timeline view across all sources
- Read-only — no data entry

*JLV is a web application, not a VistA MUMPS package.*

---

### CAPRI — Compensation and Pension Record Interchange

**VA/VBA integration for disability claims.** CAPRI enables VBA (Veterans Benefits Administration)
rating officials to view VistA clinical records when evaluating disability compensation claims.

**What it does:**
- Provides read access to VistA clinical records for VBA raters
- Generates Compensation and Pension (C&P) exam worksheets
- Transmits C&P exam results back to VBA

*CAPRI is a client application — a consumer of VistA data, not part of VistA.*

---

### VistA Imaging — `MAG`

**Clinical image management.** VistA Imaging (part of the larger VA Imaging system) stores,
retrieves, and displays clinical images linked to patient records.

**What it does:**
- Captures images from radiology (X-ray, MRI, CT, ultrasound), wound care cameras, pathology
  slides, cardiology waveforms, and other sources
- Links images to TIU clinical documents and patient encounters
- Displays images in CPRS
- Archives to long-term storage
- DICOM gateway to PACS systems

*VistA Imaging has both a MUMPS server component (MAG package) and a large Windows client application.
The client is not VistA.*

---

## Part XI: Package Quick Reference

[Back to TOC](#table-of-contents)

### By Namespace

| Namespace | Package Name | Category | Version | Notes |
|---|---|---|---|---|
| DG | ADT / Registration | Admin/Patient | 5.3 | Patient registration, eligibility |
| DI | VA FileMan | Infrastructure | 22.2 | Database foundation |
| ECME/BPS | Electronic Claims Mgmt | Financial | — | Pharmacy claims |
| GMPL | Problem List | Clinical | 2.0 | Active/resolved diagnoses |
| GMRA | Adverse Reaction Tracking | Clinical | 4.0 | Allergies |
| GMRC | Consult/Request Tracking | Clinical | 3.0 | Consult orders/results |
| GMRV | Vitals/Measurements | Clinical | 5.0 | Vital signs |
| GMTS | Health Summary | Clinical | 2.7 | Synthesized patient views |
| HL | HL7 Messaging | Infrastructure | 1.6 | External data exchange |
| IB | Integrated Billing | Financial | 2.0 | Insurance billing |
| LA | Lab Universal Interface | Clinical | 5.2 | Lab equipment interface |
| LR | Laboratory | Clinical | 5.2 | Lab information system |
| MAG | VistA Imaging | Clinical/GUI | — | Image management |
| MPIF | Master Patient Index | Admin | 1.0 | MVI adapter |
| OR | CPRS (server) | Clinical | 3.0 | Order entry engine |
| PRCA | Accounts Receivable | Financial | 4.5 | Debt collection |
| PRC | IFCAP | Admin/Financial | 5.1 | Procurement |
| PSD | Controlled Substances | Pharmacy | — | CS tracking |
| PSJ | Inpatient Pharmacy | Pharmacy | 5.0 | Ward medications |
| PSN | National Drug File | Pharmacy | — | Drug master |
| PSO | Outpatient Pharmacy | Pharmacy | 7.0 | Ambulatory Rx |
| PSS | Pharmacy Data Management | Pharmacy | 1.0 | Drug dictionary |
| PSB/PSU | Pharmacy Benefits Mgmt | Pharmacy | — | National dispensing data |
| PSX | Consolidated Mail Outpatient Pharmacy | Pharmacy | — | Mail-order pharmacy |
| PX | Patient Care Encounter | Clinical | 1.0 | Encounter data |
| PXRM | Clinical Reminders | Clinical/DSS | 2.0 | Decision support |
| RA | Radiology/Nuclear Medicine | Clinical | 5.0 | Imaging services |
| SD | Scheduling | Admin | 5.3 | Appointments |
| SR | Surgery | Clinical | 3.0 | OR management |
| TIU | Text Integration Utilities | Clinical | 1.0 | Clinical documents |
| WEBP | PCMM Web | Admin/Web | — | Care team mgmt (Java, not M) |
| XM | MailMan | Infrastructure | 8.0 | Internal messaging |
| XOBV | VistALink | Infrastructure | 1.6 | Java adapter |
| XT | Kernel Toolkit | Infrastructure | 7.3 | Dev tools |
| XU | Kernel | Infrastructure | 8.0 | Platform foundation |
| XWB | RPC Broker | Infrastructure | 1.1 | Client-server comm |
| YS | Mental Health (legacy) | Clinical | 5.01 | MH legacy package |

### By Functional Category

**Infrastructure (must be installed, everything depends on these):**
Kernel (XU) → FileMan (DI) → MailMan (XM) → RPC Broker (XWB) → HL7 (HL) → VistALink (XOBV) → Kernel Toolkit (XT)

**Patient Administration (identity, eligibility, movement):**
ADT/Registration (DG) → MPI (MPIF) → Scheduling (SD) → PCMM Web (WEBP) → Patient Record Flags (DGPF)

**Clinical Documentation (the core record):**
CPRS-server (OR) → TIU → PCE (PX) → Problem List (GMPL) → Allergies (GMRA) → Health Summary (GMTS)

**Clinical Departments:**
Laboratory (LR/LA) → Radiology (RA) → Surgery (SR) → Pharmacy (PSO/PSJ/PSS/PSD/PSX/PSN) → Mental Health (YS)

**Decision Support and Coordination:**
Clinical Reminders (PXRM) → Consults (GMRC) → Vitals (GMRV)

**Financial:**
Integrated Billing (IB) → Accounts Receivable (PRCA) → ECME → IFCAP (PRC)

**Viewers (not MUMPS, access VistA data):**
JLV · CAPRI · VistA Imaging client · VistAWeb (decommissioned)

---

## Part XII: VistA's Place in the Broader VA Ecosystem

[Back to TOC](#table-of-contents)

### What VistA Is Not Responsible For

| Function | Handled By |
|---|---|
| Veteran identity and benefits eligibility | VBA systems (separate) |
| National patient identity assignment | MVI (separate national service) |
| VA/DoD data sharing | CHDR (separate platform) |
| Veteran-facing web portal | AccessVA / eBenefits / VA.gov (separate) |
| Enterprise authentication (PIV, IAM) | VA IAM services (LDAP, PIV) |
| Financial management accounting | FMS (VA Financial Management System) |
| Human resources | HR Connect (PeopleSoft) |
| Contracting | eCMS |

### The Modernization Context

VistA is being replaced by Oracle Cerner's Millennium EHR under the VA's Electronic Health Record
Modernization (EHRM) program. As of 2026, VistA remains in production at the majority of VA
facilities. The EHRM program has deployed Cerner at a subset of facilities, with ongoing rollout.

During the transition period:
- VistA and Cerner instances must share patient data (interoperability via HL7/FHIR)
- The VDL continues to document both active VistA packages and legacy packages
- Some packages (JLV, VistALink) are EHRM-era components that bridge legacy and modern systems

---

## Appendix: Source Materials

[Back to TOC](#table-of-contents)

This guide is based on the VA VistA Documentation Library (VDL) markdown corpus:
- **44 packages** downloaded and converted from VDL DOCX/PDF
- **~1,500 markdown documents** across clinical, financial, infrastructure, and GUI sections
- **VistA Monograph (July 2023)** — VASI database export of 187 registered VistA packages

Primary source for VistA package definitions and relationships:
- Technical Manuals (TM) — authoritative package design documents
- User Manuals (UM) — clinical workflow documentation
- Release Notes — patch history and change documentation

*All descriptions are derived from VA-published official documentation.*
