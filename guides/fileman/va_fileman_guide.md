# VA FileMan: Architecture and Technical Reference Guide

*VA Office of Information and Technology — VistA Infrastructure*

---

## Table of Contents

1. [Introduction](#introduction)
   1. [What Is VA FileMan?](#what-is-va-fileman)
   2. [Role in the VistA Ecosystem](#role-in-the-vista-ecosystem)
   3. [Versioning and Distribution](#versioning-and-distribution)
   4. [Public Domain Status](#public-domain-status)
2. [Architecture](#architecture)
3. [Core Concepts](#core-concepts)
   1. [Files, Fields, and Entries](#files-fields-and-entries)
   2. [The Data Dictionary (^DD)](#the-data-dictionary-dd)
   3. [Cross-References and Indexes](#cross-references-and-indexes)
   4. [Pointers and Relationships](#pointers-and-relationships)
   5. [Templates](#templates)
   6. [Keys](#keys)
4. [API Layers](#api-layers)
   1. [Classic API (Interactive)](#classic-api-interactive)
   2. [Database Server (DBS) API (Silent)](#database-server-dbs-api-silent)
   3. [ScreenMan Form API](#screenman-form-api)
   4. [Data Mapping / Entity (DDE) API](#data-mapping--entity-dde-api)
   5. [SQLI Projection Layer](#sqli-projection-layer)
5. [Security and Access Control](#security-and-access-control)
6. [Utilities](#utilities)
7. [How VistA Packages Depend on FileMan](#how-vista-packages-depend-on-fileman)
8. [Modern Technology Equivalent — Comparative Analysis](#modern-technology-equivalent--comparative-analysis)
9. [Key System Files Reference](#key-system-files-reference)
10. [References](#references)

---

## Introduction

### What Is VA FileMan?

VA FileMan is the **database management system (DBMS)** of the Veterans Health Information Systems and Technology Architecture (VistA). It is a complete database engine, written entirely in ANSI Standard M (MUMPS), that provides every VistA application package with a unified mechanism to define, store, retrieve, and manage structured data.

FileMan is not a wrapper around a third-party database. It implements its own storage model, its own schema language (the Data Dictionary), its own query and update APIs, its own indexing infrastructure, its own forms system (ScreenMan), its own report writer, and its own auditing, archiving, and data-export tools — all within M globals.

> **VA FileMan is the universal data substrate of VistA. Every clinical, administrative, and infrastructure package in the VistA ecosystem stores its data in FileMan files and reads and writes that data through FileMan APIs.**

FileMan was originally developed in the 1970s at the VA's Data Processing Center under the name "Disc-Based File Handler" and has been continuously evolved. The current production version is **VA FileMan 22.2**, maintained by the VA Office of Information and Technology (OIT) Product Delivery Service (PDS), last updated July 2025.

### Role in the VistA Ecosystem

FileMan sits immediately above the M runtime and below every application package:

- **All 127 VistA MUMPS packages** use FileMan files as their primary data store.
- **Kernel** provides the operating environment (user security, device management, menu system, task queuing) that FileMan depends on for multi-user operations.
- **MailMan** provides messaging infrastructure that FileMan uses for bulletins and Filegrams.
- **Application packages** (ADT, CPRS, Pharmacy, Lab, etc.) define their own FileMan files and interact with them exclusively through FileMan APIs.

No application package in VistA reads or writes its M globals directly in production code — data access is mediated through FileMan's API layer. This architectural constraint is enforced by the VA's Database Administration (DBA) process through Integration Control Registrations (ICRs).

### Versioning and Distribution

FileMan itself is a KIDS-deployed M package (namespace `DI`). It must be present on every VistA system before any other package can be installed. The KIDS build for FileMan 22.2 loads all system files, routines, and data dictionary definitions as part of initialization. Once installed, FileMan is backward-compatible: files and applications developed under prior versions remain usable without modification.

### Public Domain Status

VA FileMan is public domain software, developed by employees and contractors of the U.S. Federal Government in the course of their official duties under Title 17 Section 105 of the United States Code. It is not subject to copyright protection. The VA is the sole developer and maintainer; all documentation and code are released to the public domain.

---

## Architecture

The VistA system is layered as follows, bottom to top: M runtime → VA FileMan → Kernel + MailMan → 127 application packages. FileMan is the universal data substrate; every package stores its data in FileMan files and accesses it exclusively through FileMan APIs.

FileMan's internal layers are: M globals (storage) → schema engine (data dictionary) → API layer (Classic, DBS, ScreenMan, DDE, SQLI) → utilities (auditing, archiving, Filegrams, statistics, import/export).

---

## Core Concepts

### Files, Fields, and Entries

The fundamental unit in FileMan is a **file** — the equivalent of a database table. Each file is identified by a unique **file number** (e.g., `2` for the PATIENT file, `200` for NEW PERSON). A file is described by its **data dictionary** entry in `^DD(file_number)`.

Each file contains **fields** (columns). Fields have a field number, a label, a data type, and validation rules (the INPUT transform). Data is stored as **entries** (rows), each identified by an **Internal Entry Number (IEN)** — an auto-incrementing positive integer that serves as the primary key.

A special data type called a **Multiple** (or subfile) allows one-to-many nested records within a parent file entry — equivalent to a child table linked by a foreign key to the parent IEN.

### The Data Dictionary (^DD)

The data dictionary is the schema engine. Stored in the `^DD` global, it defines every file and field across all of VistA. It contains:

- Field numbers, labels, data types, input/output transforms
- Cross-reference definitions (traditional and new-style)
- Key definitions
- Audit flags and conditions
- Help text and executable help
- Trigger cross-reference code
- Screen-level security codes

The data dictionary is itself a self-describing system: the FILE (#1) file and its structure are defined within FileMan. Developers define new files and modify schemas using FileMan's interactive utilities or programmatic APIs (`CREIXN^DDMOD`, `FILESEC^DDMOD`).

The **Meta Data Dictionary** (`^DDD`, file #0.9) provides a second-level catalog: a flattened snapshot of all file and field definitions across the entire VistA instance, used for cross-package schema discovery.

### Cross-References and Indexes

A **cross-reference** (or index) is a stored, sorted alternate lookup path into a file. FileMan supports two styles:

- **Traditional cross-references** — stored in `^DD(file,field,1)` nodes; defined per-field; fire SET and KILL logic when a field value changes.
- **New-style indexes** — stored in the INDEX (#0.11) file; support compound multi-field indexes, custom SET/KILL M code, and trigger-like behavior; created and managed via the `CREIXN^DDMOD` API.

The default `.B` cross-reference on the `.01` (name) field of most files enables fast alphabetic lookup. Additional cross-references enable efficient range queries, sorted reports, and integrity enforcement.

Uniqueness indexes implement **key** uniqueness constraints at the database level.

### Pointers and Relationships

Fields of type **POINTER TO A FILE** are the equivalent of foreign keys — they store the IEN of a record in another file. FileMan resolves pointer values through lookup calls and displays the external (human-readable) value when printing or browsing data.

A **VARIABLE POINTER** field can point to any of a named set of files, implementing a polymorphic foreign key. The file number is stored alongside the IEN to identify which file the reference belongs to.

Pointer fields are fully tracked by the `Map Pointer Relations` utility, which generates a complete dependency graph of file-to-file references across the entire VistA instance.

### Templates

FileMan uses stored **templates** to define reusable input, print, and sort specifications:

| Template Type | Global | Purpose |
|---|---|---|
| INPUT template | `^DIE` | Named set of fields to prompt for during data entry |
| PRINT template | `^DIPT` | Named report format — fields, headers, formatting |
| SORT template | `^DIBT` | Named search/sort criteria — used by Print and Search options |
| FORM (ScreenMan) | `^DIST` | Full-screen form layout (pages, blocks, fields) |
| IMPORT template | `^DIST` | Field mapping for importing external data |

Templates are exportable with KIDS builds, allowing application developers to ship pre-defined input forms and reports with their packages.

### Keys

A **key** is a named set of one or more fields that uniquely identifies a record. FileMan enforces key uniqueness through a designated uniqueness index. The KEY (#0.31) file stores key definitions. Keys may be primary or secondary; all key fields must be non-null.

---

## API Layers

### Classic API (Interactive)

The Classic API consists of callable M entry points that combine user interaction (prompting, display) with database operations. They are the original FileMan calling convention, appropriate for interactive terminal-mode applications.

| Entry Point | Function |
|---|---|
| `^DIC` | Lookup/add with "B" cross-reference; interactive selection |
| `^DIE` | Data input: prompt user for field values and file entry |
| `^DIP` / `EN1^DIP` | Print file entries with sort and format templates |
| `^DIS` / `EN^DIS` | Search file entries with criteria |
| `^DIR` | Generic response reader — validates and returns user input |
| `^DIK` | Delete entries; reindex cross-references |
| `FILE^DICN` | Add new entry silently (no user interaction) |
| `EN^DIQ` | Display a captioned range of data fields |
| `^DIWE` | Word-processing field text editor |
| `%DT` / `%DTC` | Date/time validation, conversion, and arithmetic |

Classic calls perform `WRITE` operations to the current device. They are *not* recursive-safe; nested calls (e.g., from within cross-references) must use DBS calls instead.

### Database Server (DBS) API (Silent)

The DBS API separates data access from user interaction. DBS calls accept parameters, perform database operations without writing to the device, and return results in M arrays. They are the correct API for application code that manages its own UI — the foundation for GUI clients, web services, and batch jobs.

| Entry Point | Function |
|---|---|
| `FIND^DIC` | Query: find entries matching criteria; returns result array |
| `$$FIND1^DIC` | Query: find single matching entry; returns IEN |
| `LIST^DIC` | Lister: retrieve a sorted list of entries |
| `FILE^DIE` | Update: file one or more field values for an entry |
| `UPDATE^DIE` | Update with full auditing and key validation |
| `CHK^DIE` | Validate field value without filing |
| `GETS^DIQ` | Retrieve: get field values for one or more entries |
| `$$GET1^DIQ` | Retrieve single field value |
| `FIELD^DID` | Retrieve data dictionary attribute for a field |
| `FILE^DID` | Retrieve data dictionary attributes for a file |
| `$$ROOT^DILFD` | Resolve file global root from file number |
| `LOCK^DILF` | Lock a global reference (concurrency control) |
| `CREIXN^DDMOD` | Create a new-style cross-reference programmatically |
| `FILESEC^DDMOD` | Set file-level security codes |

The DBS API uses the **FDA (FileMan Data Array)** convention to pass field values: `FDA(file_number, IENS, field_number) = value`. IENS (Internal Entry Number String) identifies entries and sub-entries in a hierarchical parent-child structure.

### ScreenMan Form API

ScreenMan is FileMan's full-screen, cursor-positioned forms engine for VT100-compatible terminals. It separates a data-entry form from its underlying files, enabling multi-file forms, computed display-only fields, and relational navigation (forward and backward pointer traversal) within a single form.

| Entry Point | Function |
|---|---|
| `^DDS` | Invoke ScreenMan to run a named form |
| `^DDGF` | Invoke the Form Editor (interactive form designer) |
| `$$GET^DDSVAL` | Retrieve the current value of a data dictionary field from within a form |
| `PUT^DDSVAL` | Set a data dictionary field value from within a form |
| `REFRESH^DDSUTL` | Refresh the screen display |

ScreenMan forms are stored in the FORM (#0.403) and BLOCK (#0.404) files (`^DIST`) and shipped with KIDS builds, enabling application developers to deliver complete data-entry interfaces.

### Data Mapping / Entity (DDE) API

The Entity (#1.5) file and DDE API (added in FileMan 22.2) provide a declarative mapping layer that translates FileMan file structures into structured objects suitable for RESTful APIs, FHIR resources, or any other external data model.

An **entity** defines a set of properties, each mapped to a FileMan field (or a computed expression). The DDE API serializes these entities as JSON or XML arrays, enabling web services to retrieve VistA data in standard formats without writing custom extraction code.

| Entry Point | Function |
|---|---|
| `GET^DDE` | Retrieve multiple entity records as JSON/XML array |
| `$$GET1^DDE` | Retrieve single entity record as JSON/XML string |

The Virtual Patient Record (VPR) and clinical data exposure initiatives (FHIR, SDA) are primary consumers of the DDE layer.

### SQLI Projection Layer

FileMan includes a built-in **SQLI** (SQL Interface) subsystem that projects the FileMan data model as a relational schema. The SQLI tables (`^DMSQ`) describe FileMan files as SQL tables, fields as columns, pointers as foreign keys, and cross-references as indexes. This enables read-only SQL access to VistA data through ODBC-compliant tools.

SQLI is a projection layer only — it does not replace the FileMan storage model. Updates to VistA data must continue to use FileMan APIs.

---

## Security and Access Control

FileMan provides multiple layers of data protection:

**File-level security codes** — Each file carries read (`RD`), write (`WR`), delete (`DL`), and laygo-add (`LA`) access codes. A user's access codes (stored in `DUZ(0)`) are compared at runtime to determine permitted operations.

**Field-level security** — Individual fields can require additional access codes, restricting visibility or editability to privileged users.

**Programmer access** — Setting `DUZ(0)="@"` grants unrestricted access to all FileMan files and data dictionaries. This is the VistA developer/DBA privilege level and bypasses all security checks.

**Data Access Control (DAC)** — Added in FileMan 22.2 patch DI*22.2*8, DAC provides a policy-based access control engine. Application actions (read, cancel, sign, etc.) are defined in the APPLICATION ACTION (#1.61) file and linked to POLICY (#1.6) entries. Policies are evaluated at runtime by `$$CANDO^DIAC1`. This enables fine-grained, rule-based security beyond the traditional letter-code system.

**Kernel integration** — When running with Kernel, file access is further governed by Kernel's File Access Security system, linking FileMan access codes to Kernel user profiles in the NEW PERSON (#200) file.

**Auditing** — FileMan auditing tracks every change to a field value (stored in `^DIA`, file #1.1) and every change to the data dictionary itself (stored in `^DDA`, file #0.6). Audits record the user (`DUZ`), date/time, and old/new values.

---

## Utilities

| Utility | Description |
|---|---|
| **Auditing** | Turn on field-level audit logging; query audit history by field, file, user, or date range. API: `TURNON^DIAUTL`, `CHANGED^DIAUTL`. |
| **Archiving** | Select and move file entries to offline storage (Filegram-based). Preserves data outside the active database with full retrieval capability. |
| **Filegrams** | Serialize file entries into a structured MailMan message (Filegram) for transfer to another VistA system. The receiving system installs the Filegram via `^DIFG`. Used for inter-site data sharing. |
| **Extract Tool** | Copy selected file entries from a source file to a destination FileMan file. Supports template-based field mapping. |
| **Import / Export** | Import data from external flat files using IMPORT TEMPLATEs; export VistA data to foreign formats (CSV, fixed-width, etc.) using FOREIGN FORMAT definitions. |
| **Statistics** | Compute descriptive statistics, histograms, and scattergrams over numeric fields in a file. |
| **Browser** | Full-screen viewer for WORD-PROCESSING fields — scroll, search, and navigate long text documents. |
| **DIFROM** | Package export tool that bundles data dictionaries, data, templates, and routines into init routines for distribution. Superseded by KIDS in the VA environment but retained for backward compatibility. |
| **Transfer / Merge** | Transfer or merge entries between files; Namespace Compare utility identifies differences between two VistA instances. |

---

## How VistA Packages Depend on FileMan

Every VistA MUMPS package stores its clinical, administrative, and configuration data in FileMan files. The dependency is architectural, not optional: no VistA package accesses its M globals directly in production code. The interaction patterns fall into four categories:

**1. Data storage** — Each package defines one or more FileMan files in its own numeric range (e.g., PATIENT file #2 belongs to Registration/ADT; ORDER file #100 to CPRS; PRESCRIPTION file #52 to Outpatient Pharmacy). File definitions are shipped as part of the KIDS build and installed by FileMan's `DINIT` process.

**2. CRUD operations** — Application routines call FileMan DBS APIs (`FILE^DIE`, `FIND^DIC`, `GETS^DIQ`) to create, read, update, and delete records. Classic APIs (`^DIC`, `^DIE`, `^DIP`) drive the legacy scroll-mode user interfaces.

**3. Cross-reference–driven integrity and notifications** — Packages use cross-references (both traditional and new-style) to maintain derived data, enforce referential integrity, send MailMan bulletins on field changes, and trigger downstream updates across related files.

**4. Schema extensions** — Packages add fields to FileMan files owned by other packages through a DBA-governed process (ICR — Integration Control Registration). For example, Kernel adds fields to the NEW PERSON (#200) file; CPRS adds order-related fields to patient-level files.

**Key inter-package files mediated by FileMan:**

| File | Number | Owner | Used By |
|---|---|---|---|
| PATIENT | 2 | Registration (DG) | Every clinical package |
| NEW PERSON | 200 | Kernel (XU) | All packages — user identity |
| OPTION | 19 | Kernel (XU) | All packages — menu structure |
| INSTITUTION | 4 | Kernel (XU) | All packages — site identity |
| ORDER | 100 | CPRS (OE/RR) | Pharmacy, Radiology, Lab, Nursing |
| DRUG | 50 | Pharmacy (PS) | Outpatient, Inpatient, Bcma, CPRS |
| LAB DATA | 63 | Laboratory (LR) | CPRS, Health Summary |
| PROTOCOL | 101 | Kernel (XU) | All packages — HL7 and event processing |

---

## Modern Technology Equivalent — Comparative Analysis

VA FileMan predates relational databases in mainstream deployment and was designed to operate in resource-constrained, terminal-based clinical environments. The table below translates each FileMan concept and layer into the equivalent combination of modern technologies.

**Key observation:** FileMan bundles in a single package what modern technology stacks typically deliver through five or more separate products. The comparison intentionally uses generic terms (not specific vendor products) and maps to the closest functional equivalent.

| FileMan Concept / Layer | FileMan Term | Modern Generic Equivalent | Notes |
|---|---|---|---|
| **Persistent data store** | M Global (`^XXX`) | Database storage engine (InnoDB, B-tree pages, WAL files) | FileMan globals are persistent, hierarchical key-value stores; RDBMS storage engines provide the same durability guarantee through a different physical structure |
| **Table definition** | File | Table / Relation | FileMan "file" = RDBMS table; stored in `^DD` and `^DIC` |
| **Column definition** | Field | Column | Field number, label, data type, constraints |
| **Row / record** | Entry | Row / Record | Identified by IEN (surrogate primary key) |
| **Auto-increment primary key** | IEN (Internal Entry Number) | Auto-increment integer PK / UUID surrogate key | Every FileMan file entry has an IEN; analogous to `SERIAL` / `IDENTITY` / `AUTO_INCREMENT` |
| **One-to-many child records** | Multiple (Subfile) | Child table with FK to parent PK | FileMan multiples are stored as sub-nodes of the parent global; equivalent to a normalized child table |
| **Schema definition language** | Data Dictionary (^DD) | DDL (CREATE TABLE, ALTER TABLE) + Information Schema | FileMan DD is richer: contains validation logic, display transforms, help text, and audit flags inline |
| **Schema catalog / metadata store** | FILE (#1), META DATA DICTIONARY (#0.9) | `information_schema` / system catalog / data catalog tool | FileMan's schema is self-describing and runtime-queryable; MDD provides a flattened snapshot |
| **Data type system** | DATA TYPE file (#0.81), INPUT transform | Column data types (VARCHAR, INTEGER, DATE) + CHECK constraints + domain types | FileMan INPUT transform is executable M code — more powerful than SQL CHECK, closer to a stored validation function |
| **Index / lookup path** | Cross-Reference (traditional or new-style) | CREATE INDEX (B-tree, hash, functional) | FileMan indexes store arbitrary M code for SET/KILL logic — closer to a functional index plus triggers combined |
| **Compound index** | New-style compound cross-reference | Composite index (CREATE INDEX ON t(a,b)) | New-style indexes support multi-field compound keys |
| **Uniqueness constraint** | Key + Uniqueness Index | PRIMARY KEY / UNIQUE constraint | FileMan KEY file defines uniqueness; enforced via the uniqueness index |
| **Foreign key reference** | Pointer to a File | FOREIGN KEY REFERENCES | FileMan stores the IEN of the referenced record; lookup APIs resolve the display value |
| **Polymorphic foreign key** | Variable Pointer | Polymorphic association (FK + discriminator column) or `UNION` pattern | No direct SQL equivalent; requires application-level pattern or JSON type columns in modern SQL |
| **Computed / derived column** | Computed Field, Computed Multiple | Computed column (AS expression) / virtual column / ORM `@property` | FileMan computed fields contain M code executed on read |
| **Trigger** | Trigger Cross-Reference (SET/KILL logic) | Database trigger (AFTER INSERT/UPDATE/DELETE) + application hook | FileMan triggers fire on field-value change; can update other fields or other files |
| **Notification on change** | Bulletin cross-reference | Change Data Capture (CDC) / message broker event (Kafka, SNS) | FileMan bulletins send MailMan messages; modern equivalent is event stream or webhook |
| **CRUD API — interactive** | Classic API (`^DIC`, `^DIE`, `^DIP`) | ORM active record pattern (Rails ActiveRecord, Django Model) + CLI admin interface | Classic API combines UI prompting with database operations — no clean separation |
| **CRUD API — programmatic / silent** | DBS API (`FILE^DIE`, `FIND^DIC`, `GETS^DIQ`) | ORM / DAO / repository pattern (Hibernate, SQLAlchemy, Spring Data) | DBS API is the clean programmatic layer: parameters in, result arrays out, no device I/O |
| **Record validation** | VAL^DIE, CHK^DIE, VALS^DIE | ORM validation layer (validators, constraints, `clean()` methods) | FileMan separates validation from filing; comparable to `validate()` before `save()` |
| **Scrolling data entry UI** | Classic roll-and-scroll prompts (^DIE, ^DIC) | Command-line form / terminal UI (curses, readline) | Legacy VT100 scroll-mode interaction |
| **Full-screen forms** | ScreenMan (^DDS, ^DDGF) | Web form framework / GUI form builder (Django forms, React forms, WinForms) | ScreenMan is a complete VT100 full-screen form engine with pages, blocks, and relational navigation |
| **Report writer** | PRINT templates, EN1^DIP, Sort templates | BI / reporting tool (Crystal Reports, SSRS, Metabase) + parameterized SQL queries | FileMan's report writer is embedded in the DBMS; modern equivalents are separate products |
| **Ad-hoc query** | Search File Entries (^DIS), FIND^DIC | SQL SELECT + WHERE clause / query builder | FileMan search supports field criteria, boolean combinations, range queries |
| **Saved query / view** | SORT template, PRINT template | Saved query / SQL VIEW | FileMan templates are named, reusable search+sort+format specifications |
| **Text / BLOB storage** | WORD-PROCESSING field | TEXT / BLOB column | FileMan WP fields store multi-line text in a sub-node array |
| **Audit log** | Data Audit (`^DIA`), DD Audit (`^DDA`) | Audit table / temporal table (AS OF / SYSTEM_TIME) / CDC | FileMan audit tracks field-level changes with user and timestamp; comparable to a change-data-capture system |
| **Row-level access control** | File security codes (RD/WR/DL/LA) | Role-based access control (RBAC) / ACL on table | FileMan's letter-code system predates SQL GRANT/REVOKE; semantically similar to table-level permissions |
| **Fine-grained access policy** | Data Access Control (DAC) — Policy/Action files | Row-level security (RLS) / policy-based authorization (OPA, XACML) | DAC policies evaluate M conditions at runtime; closer to attribute-based access control (ABAC) |
| **Schema migration tooling** | DIFROM / KIDS init routines | Schema migration tool (Flyway, Liquibase, Alembic) | FileMan KIDS builds deploy both schema changes and data together; modern tools separate schema migrations from code deploys |
| **SQL/ODBC projection** | SQLI layer (`^DMSQ`) | ODBC/JDBC driver + read-only SQL views | SQLI projects FileMan tables as SQL relations; enables reporting tools to query VistA data via SQL |
| **REST / FHIR entity mapping** | DDE / Entity file (#1.5), `GET^DDE` | ORM entity → DTO / REST resource serializer (Jackson, marshmallow, FHIR-kit) | DDE declaratively maps FileMan fields to JSON/XML output for REST APIs and FHIR resources |
| **Internationalization / message catalog** | DIALOG file (#0.84), LANGUAGE file (#0.85) | i18n library (gettext, ICU, resource bundles) | FileMan dialog and language files provide multi-language message storage for all user-facing text |
| **Inter-system data transfer** | Filegrams | ETL pipeline / data replication (Kafka Connect, AWS DMS) | Filegrams serialize FileMan entries to MailMan messages for manual or automated inter-site transfer |
| **Data archival** | Archiving utility | Data tiering / archive storage (cold storage, S3 Glacier) | FileMan archiving moves entries to Filegram-based offline storage while maintaining retrieval capability |
| **Statistics and analytics** | Statistics utility (histogram, scattergram) | SQL aggregates + BI/OLAP tools (GROUP BY, window functions, Tableau) | FileMan statistics are basic descriptive analytics; modern equivalents are far more capable |
| **Package self-description** | PACKAGE file (#9.4), DIFROM | Package registry / dependency manifest (package.json, pyproject.toml) | FileMan tracks package versions and file ownership in the PACKAGE file |

**Summary of tooling equivalence:**

| FileMan Layer | Modern Stack Required |
|---|---|
| Storage + schema + DDL | RDBMS (PostgreSQL, Oracle, MySQL) |
| Schema catalog + metadata management | `information_schema` + data catalog tool (Apache Atlas, Collibra) |
| ORM / DAO / repository | ORM framework (SQLAlchemy, Hibernate, ActiveRecord) |
| Validation | Application validation layer (class validators, form validators) |
| Full-screen forms | Web framework / form builder (React, Django, Rails) |
| Report writer | BI tool (SSRS, Metabase, Tableau) |
| Audit trail | CDC tool or temporal table extension |
| Access control | RBAC library + optional RLS / ABAC engine |
| Schema migration | Migration tool (Flyway, Liquibase, Alembic) |
| ODBC/SQL access | ODBC/JDBC driver + SQL views |
| REST/FHIR serialization | DTO/serializer library + FHIR SDK |
| Inter-system data transfer | ETL / messaging platform |
| i18n / message catalog | i18n library (gettext, ICU) |

**What makes FileMan architecturally distinctive** (not merely equivalent to a modern combination):

1. **Self-describing at runtime** — The data dictionary is live and queryable. Schema changes are reflected immediately without recompilation. No modern SQL database natively exposes DDL at this level of introspection during application execution.
2. **Embedded validation logic** — INPUT transforms are executable M code stored in the schema itself, not in a separate application layer. Every FileMan application inherits this validation without separate configuration.
3. **Cross-reference as first-class object** — Indexes in FileMan carry executable SET/KILL logic. A single cross-reference can update derived fields, send notifications, and maintain denormalized data — combining what modern systems implement as triggers, materialized views, and event hooks.
4. **Universal API contract** — Every VistA package uses the same API layer. There is no impedance mismatch between packages: a cross-reference or trigger in one package's file can safely invoke FileMan APIs to read another package's file using the same calling conventions.

---

## Key System Files Reference

The following system files are foundational to FileMan's operation. They exist on every VistA system.

| File # | Name | Global | Description |
|---|---|---|---|
| 0.11 | INDEX | `^DD("IX",` | New-style cross-reference definitions |
| 0.31 | KEY | `^DD("KEY",` | Key (uniqueness constraint) definitions |
| 0.4 | PRINT TEMPLATE | `^DIPT(` | Saved report format definitions |
| 0.401 | SORT TEMPLATE | `^DIBT(` | Saved search/sort criteria |
| 0.402 | INPUT TEMPLATE | `^DIE(` | Saved data-entry field sets |
| 0.403 | FORM | `^DIST(.403` | ScreenMan form definitions |
| 0.404 | BLOCK | `^DIST(.404` | ScreenMan block definitions |
| 0.44 | FOREIGN FORMAT | `^DIST(.44` | External data format specifications |
| 0.46 | IMPORT TEMPLATE | `^DIST(.46,` | Import field-mapping definitions |
| 0.5 | FUNCTION | `^DD("FUNC"` | Computed expression library |
| 0.6 | DD AUDIT | `^DDA(` | Data dictionary change audit trail |
| 0.7 | MUMPS OPERATING SYSTEM | `^DD("OS"` | OS-specific M code configurations |
| 0.81 | DATA TYPE | `^DI(.81` | Field data type definitions |
| 0.84 | DIALOG | `^DI(.84` | User message / error message catalog |
| 0.85 | LANGUAGE | `^DI(.85` | ISO 639 language table |
| 0.9 | META DATA DICTIONARY | `^DDD(` | Flattened schema snapshot — all files and fields |
| 1 | FILE | `^DIC(` | Registry of all FileMan files on this system |
| 1.1 | AUDIT | `^DIA(` | Data field change audit trail |
| 1.11 | ARCHIVAL ACTIVITY | `^DIAR(1.11` | Archive operation status log |
| 1.5 | ENTITY | `^DDE(` | DDE entity-to-FileMan field mappings (FHIR, SDA) |
| 1.521 | SQLI_SCHEMA | `^DMSQ("S",` | SQLI relational projection schema |
| 1.6 | POLICY | `^DIAC(1.6,` | DAC access control policies |
| 1.61 | APPLICATION ACTION | `^DIAC(1.6,` | DAC application action definitions |

---

## References

All source documents are from the VA Software Document Library (VDL), FileMan application (appid=5):

| Document | Version | Date |
|---|---|---|
| VA FileMan Developer's Guide | 22.2 (Rev 1.14) | July 2025 |
| VA FileMan Technical Manual | 22.2 (Rev 1.6) | July 2025 |
| VA FileMan User Manual | 22.2 | July 2025 |
| VA FileMan Data Access Control (DAC) User Guide | 22.2 Patch DI*22.2*8 | August 2017 |
| VA FileMan Key and Index Tutorial | 22.0 | September 2001 |
| VA FileMan ScreenMan Tutorial for Developers | 22.0 | — |
| VA FileMan DDE Utility Tutorial | 22.2 | April 2023 |
| VA FileMan Installation, Back-Out, and Rollback Guide | 22.2 | — |
| VA FileMan Release Notes | 22.2 | — |

**Analysis methodology:** This guide was compiled by systematic AI-assisted analysis of all 10 VA FileMan documentation files in the VistA Documentation Library markdown corpus (combined: 270,348 words, 68 pages to 784 pages per document). Source materials were read in full; all statements are grounded in the primary documentation.

---

*This guide covers VA FileMan 22.2. FileMan namespace: DI. VDL application page: `va.gov/vdl/application.asp?appid=5`*
