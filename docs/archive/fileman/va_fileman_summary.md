# VA FileMan API — Executive Summary

*Source: VA Software Document Library (VDL), FileMan Application (appid=5); VA FileMan 22.2 (last updated July 2025)*

---

## What VA FileMan Is

VA FileMan (MUMPS package namespace `DI`, version 22.2) is the **database management system of VistA** — the Veterans Health Information Systems and Technology Architecture. It is a self-contained database engine written entirely in ANSI Standard M (MUMPS) that provides every VistA application with a unified mechanism to define, store, retrieve, update, and manage structured data.

FileMan is not a wrapper around a third-party database. It implements its own:
- Storage model (MUMPS globals)
- Schema language (the Data Dictionary)
- Query and update APIs (Classic and DBS layers)
- Indexing infrastructure (cross-references)
- Forms system (ScreenMan)
- Audit, archiving, and data-export tooling

**All 127 VistA MUMPS packages** use FileMan as their exclusive data store. No package reads or writes MUMPS globals directly — all data access is mediated through FileMan APIs, enforced by the VA's Integration Control Registration (ICR) governance process.

---

## Scope and Role in VistA

```
M Runtime
    └── VA FileMan (DI)          ← universal data substrate
            └── Kernel + MailMan ← operating environment
                    └── 127 Application Packages (ADT, CPRS, Pharmacy, Lab, …)
```

FileMan must be installed on every VistA system before any other package. It is backward-compatible — applications built under prior versions run unchanged on 22.2.

---

## Core Concepts

| Concept | Description |
|---|---|
| **File** | The equivalent of a database table; identified by a unique numeric file number (e.g., `#2` = PATIENT, `#200` = NEW PERSON) |
| **Field** | A column within a file; has a field number, label, data type, and executable input validation (INPUT transform) |
| **Entry** | A row; identified by an Internal Entry Number (IEN) — an auto-incrementing integer primary key |
| **Multiple (Subfile)** | One-to-many child records nested within a parent entry; equivalent to a normalized child table with FK to parent IEN |
| **Data Dictionary (^DD)** | The schema engine — stores all file and field definitions, constraints, help text, transforms, and audit flags; live and runtime-queryable |
| **Cross-Reference (Index)** | A stored lookup path; carries executable M SET/KILL logic — combines B-tree index + trigger + CDC notification in one object |
| **Pointer** | A foreign key field storing the IEN of a record in another file; resolved to display values by FileMan APIs |
| **Variable Pointer** | A polymorphic foreign key that can reference any of a set of files |
| **Key** | A named uniqueness constraint on one or more fields, enforced via a designated uniqueness index |
| **Template** | A named, reusable specification for data entry (INPUT), reports (PRINT/SORT), or screen forms (FORM/BLOCK) |

---

## API Layers

FileMan exposes five distinct API layers, progressing from interactive terminal-mode to modern web services.

### Summary Table

| API Layer | Paradigm | Primary Use | Writable | Device I/O |
|---|---|---|---|---|
| **Classic API** | Interactive terminal | Legacy scroll-mode VistA menus | Yes | Yes — writes to terminal |
| **DBS API (Database Server)** | Programmatic / silent | Application code, GUI clients, batch jobs | Yes | None |
| **ScreenMan Forms API** | Full-screen VT100 forms | Complex multi-file terminal data entry | Yes | VT100 screen |
| **DDE / Entity API** | Declarative mapping | REST/FHIR JSON/XML output | No (read-only) | None |
| **SQLI Projection** | SQL/ODBC | Read-only SQL access for reporting tools | No (read-only) | None |

---

### Classic API (Interactive)

Combines user prompting with database operations. Appropriate for terminal-mode applications only. Not recursive-safe — nested calls must use DBS instead.

| Entry Point | Function |
|---|---|
| `^DIC` / `DIC^DIC` | Lookup entries in a file using the `.B` cross-reference; interactive selection |
| `^DIE` / `FILE^DIE` | Interactive or programmatic data entry and field update |
| `^DIP` / `EN1^DIP` | Print file entries using PRINT and SORT templates |
| `^DIS` / `EN^DIS` | Search file entries against user-specified criteria |
| `^DIR` | Generic response reader — validates and returns user input |
| `^DIK` / `EN^DIK` | Delete entries; rebuild cross-references |
| `FILE^DICN` | Add a new entry silently (no user prompting) |
| `EN^DIQ` | Display a captioned range of data fields |
| `^DIWE` | WORD-PROCESSING field text editor |
| `%DT` / `%DTC` | Date/time validation, conversion, and arithmetic |

---

### DBS API — Database Server (Programmatic / Silent)

The correct API for any code that manages its own UI. Accepts parameters, performs operations without device writes, returns results in M arrays. Uses the **FDA (FileMan Data Array)** convention: `FDA(file#, IENS, field#) = value`.

| Entry Point | Function |
|---|---|
| `FIND^DIC` | Query: find entries matching criteria; returns result array |
| `$$FIND1^DIC` | Query: find a single matching entry; returns IEN |
| `LIST^DIC` | Retrieve a sorted list of entries |
| `FILE^DIE` | Update: file one or more field values for an entry |
| `UPDATE^DIE` | Update with full auditing and key validation |
| `CHK^DIE` | Validate a field value without filing |
| `GETS^DIQ` | Retrieve field values for one or more entries |
| `$$GET1^DIQ` | Retrieve a single field value |
| `FIELD^DID` | Retrieve data dictionary attributes for a field |
| `FILE^DID` | Retrieve data dictionary attributes for a file |
| `$$ROOT^DILFD` | Resolve a file's global root from its file number |
| `LOCK^DILF` | Lock a global reference (concurrency control) |
| `CREIXN^DDMOD` | Create a new-style cross-reference programmatically |
| `FILESEC^DDMOD` | Set file-level security codes |

**IENS** (Internal Entry Number String) is the hierarchical entry identifier used throughout the DBS API to address both top-level entries and sub-entries within multiples.

---

### ScreenMan Forms API

A VT100 full-screen forms engine that separates data entry forms from underlying files. Supports multi-file forms, computed display-only fields, and relational pointer traversal within a single form. Forms are stored in FORM (#0.403) and BLOCK (#0.404) files and shipped with KIDS builds.

| Entry Point | Function |
|---|---|
| `^DDS` | Invoke ScreenMan to run a named form |
| `^DDGF` | Interactive form designer (Form Editor) |
| `$$GET^DDSVAL` | Retrieve a field value from within a running form |
| `PUT^DDSVAL` | Set a field value from within a running form |
| `REFRESH^DDSUTL` | Refresh the screen display |

---

### Data Mapping / Entity (DDE) API

Added in FileMan 22.2. Provides a declarative mapping layer translating FileMan files into structured objects for RESTful APIs and FHIR resources. Entities are defined in the ENTITY (#1.5) file. Primary consumers: Virtual Patient Record (VPR), FHIR exposure initiatives.

| Entry Point | Function |
|---|---|
| `GET^DDE` | Retrieve multiple entity records as a JSON/XML array |
| `$$GET1^DDE` | Retrieve a single entity record as a JSON/XML string |

---

### SQLI Projection Layer

Projects the FileMan data model as a read-only relational schema accessible via ODBC-compliant tools. Tables, columns, foreign keys, and indexes mirror the FileMan file/field/cross-reference model. Schema stored in `^DMSQ`. Updates to VistA data must still use FileMan APIs — SQLI is a projection only.

---

## Security and Access Control

| Mechanism | Description |
|---|---|
| **File-level access codes** | Each file carries RD (read), WR (write), DL (delete), LA (laygo/add) codes compared against `DUZ(0)` at runtime |
| **Field-level security** | Individual fields may require additional access codes beyond the file-level codes |
| **Programmer access** | `DUZ(0)="@"` grants unrestricted access to all files and data dictionaries; bypasses all security checks |
| **Data Access Control (DAC)** | Added in DI*22.2*8; policy-based engine using POLICY (#1.6) and APPLICATION ACTION (#1.61) files; evaluated at runtime by `$$CANDO^DIAC1` — equivalent to ABAC |
| **Kernel integration** | FileMan access codes linked to Kernel NEW PERSON (#200) user profiles when running under Kernel |
| **Data Auditing** | Field-level change audit (`^DIA`, file #1.1) — records user (`DUZ`), date/time, old and new values |
| **DD Auditing** | Data dictionary change audit (`^DDA`, file #0.6) — tracks schema modifications |

**Security Keys (FileMan-defined):**

| Key | Purpose |
|---|---|
| `XUAUDITING` | Audit trail utilities |
| `XUFILEGRAM` | Filegram export/import |
| `XUMGR` | VistA Manager access |
| `XUPROGMODE` | Programmer mode |
| `XUSCREENMAN` | ScreenMan form editor |
| `DDXP-DEFINE` | Define data dictionary exports |
| `DIEXTRACT` | Data extraction utilities |

---

## Utility Functions

| Utility | Function |
|---|---|
| **Auditing** (`TURNON^DIAUTL`, `CHANGED^DIAUTL`) | Enable/query field-level audit logs by field, file, user, or date range |
| **Archiving** | Select and move file entries to offline Filegram-based storage with full retrieval |
| **Filegrams** (`^DIFG`) | Serialize entries to MailMan messages for inter-site data transfer |
| **Extract Tool** | Copy entries between FileMan files using template-based field mapping |
| **Import / Export** | Import from external flat files via IMPORT TEMPLATEs; export to CSV/fixed-width via FOREIGN FORMAT definitions |
| **Statistics** | Descriptive statistics, histograms, and scattergrams over numeric fields |
| **Browser** | Full-screen viewer for WORD-PROCESSING fields |
| **DIFROM** | Legacy package bundler (superseded by KIDS; retained for backward compatibility) |
| **Map Pointer Relations** | Generates a complete file-to-file dependency graph across the VistA instance |
| **Transfer / Merge** | Move or merge entries between files; Namespace Compare identifies differences between two VistA instances |

---

## Key Cross-Package Files Mediated by FileMan

| File # | Name | Owner Package | Used By |
|---|---|---|---|
| 2 | PATIENT | Registration (DG) | Every clinical package |
| 200 | NEW PERSON | Kernel (XU) | All packages — user identity |
| 19 | OPTION | Kernel (XU) | All packages — menu structure |
| 4 | INSTITUTION | Kernel (XU) | All packages — site identity |
| 100 | ORDER | CPRS (OE/RR) | Pharmacy, Radiology, Lab, Nursing |
| 50 | DRUG | Pharmacy (PS) | Outpatient, Inpatient, BCMA, CPRS |
| 63 | LAB DATA | Laboratory (LR) | CPRS, Health Summary |
| 101 | PROTOCOL | Kernel (XU) | All packages — HL7/event processing |

---

## Modern Technology Equivalents

| FileMan Layer | Modern Generic Equivalent |
|---|---|
| M Global storage + schema + DDL | RDBMS storage engine (PostgreSQL, Oracle) |
| Data Dictionary (`^DD`) | `information_schema` + DDL + inline validation + data catalog |
| Classic API (`^DIC`, `^DIE`, `^DIP`) | ORM active-record pattern + CLI admin interface |
| DBS API (`FILE^DIE`, `FIND^DIC`, `GETS^DIQ`) | ORM / DAO / repository pattern (SQLAlchemy, Hibernate) |
| Cross-reference (index + trigger) | Composite index + database trigger + CDC notification combined |
| ScreenMan forms (`^DDS`) | Web form framework / GUI form builder |
| PRINT/SORT templates | BI / reporting tool (SSRS, Metabase) |
| DDE / Entity API | REST DTO / FHIR serializer (marshmallow, FHIR-kit) |
| SQLI projection | ODBC/JDBC driver + read-only SQL views |
| Audit (`^DIA`, `^DDA`) | Change-data-capture (CDC) / temporal tables |
| DAC policies | Attribute-based access control (ABAC / OPA) |
| Filegrams | ETL / data replication pipeline (Kafka Connect, AWS DMS) |
| DIFROM / KIDS init routines | Schema migration tool (Flyway, Liquibase, Alembic) |

---

## VDL Documentation Coverage

FileMan has **16 documents** in the VDL (appid=5), all active, spanning:

| Document Type | Examples |
|---|---|
| Developer's Guide (base-dev) | VA FileMan Developer's Guide 22.2 (Rev 1.14, July 2025) |
| Technical Manual | VA FileMan Technical Manual 22.2 (Rev 1.6, July 2025) |
| User Manual | VA FileMan User Manual 22.2 |
| Security Guide | VA FileMan Data Access Control (DAC) User Guide (DI*22.2*8) |
| Tutorials | Key and Index Tutorial (22.0); ScreenMan Tutorial for Developers |

All source documents: `https://www.va.gov/vdl/application.asp?appid=5`

---

## Key Architectural Observations

1. **Self-describing at runtime** — The Data Dictionary is live and queryable. Schema changes take effect immediately without recompilation. No modern SQL database offers this level of DDL introspection during application execution.

2. **Validation embedded in schema** — INPUT transforms are executable M code stored in `^DD`. Every FileMan application inherits this validation automatically — no separate configuration layer required.

3. **Cross-reference as a first-class object** — A single FileMan index carries B-tree lookup, executable SET/KILL triggers, derived-field maintenance, and notification logic. Modern systems require separate products to match this combination.

4. **Universal API contract** — All 127 VistA packages use the same API layer with no impedance mismatch. Any package's cross-reference or trigger can safely read another package's data using identical calling conventions.
