# VA FileMan External API Wrapper — Comprehensive Specification

**Enabling Non-M Language Application Development Against the FileMan Database Engine**

*Version 1.4 — April 2026*
*Audience: Software architects, API engineers, and VistA modernization program leads*

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Background: The Problem of Legacy Database Preservation](#2-background-the-problem-of-legacy-database-preservation)
3. [Industry Methodology: Wrapping Legacy Database Systems](#3-industry-methodology-wrapping-legacy-database-systems)
4. [Case Studies: Successful Major API Wrapper Projects](#4-case-studies-successful-major-api-wrapper-projects)
5. [FileMan as a Wrapping Target: Capabilities and Constraints](#5-fileman-as-a-wrapping-target-capabilities-and-constraints)
6. [Transport Architecture Options](#6-transport-architecture-options)
   - 6.4 [InterSystems IRIS Embedded Transport](#64-intersystems-iris-embedded-transport)
7. [API Surface Specification — Complete FileMan Coverage](#7-api-surface-specification--complete-fileman-coverage)
   - 7.1 [DBS API — Core Read Operations](#71-dbs-api--core-read-operations)
   - 7.2 [DBS API — Core Write Operations](#72-dbs-api--core-write-operations)
   - 7.3 [DBS API — Validation](#73-dbs-api--validation)
   - 7.4 [DBS API — Schema Introspection](#74-dbs-api--schema-introspection)
   - 7.5 [Classic API — Wrappable Subset](#75-classic-api--wrappable-subset)
   - 7.6 [DDE / Entity API](#76-dde--entity-api)
   - 7.7 [SQLI Projection Layer](#77-sqli-projection-layer)
   - 7.8 [Cross-Reference Management](#78-cross-reference-management)
   - 7.9 [Lock Management](#79-lock-management)
   - 7.10 [Auditing Utilities](#710-auditing-utilities)
   - 7.11 [Archiving and Filegrams](#711-archiving-and-filegrams)
   - 7.12 [Import and Export Utilities](#712-import-and-export-utilities)
   - 7.13 [Statistics Utilities](#713-statistics-utilities)
   - 7.14 [Date and Time Services](#714-date-and-time-services)
   - 7.15 [Security and Context Management](#715-security-and-context-management)
   - 7.16 [Data Dictionary Administration](#716-data-dictionary-administration)
8. [Data Type Mapping Specification](#8-data-type-mapping-specification)
9. [Error Surface Specification](#9-error-surface-specification)
10. [Wire Protocol and Serialization Specification](#10-wire-protocol-and-serialization-specification)
11. [Security Model Specification](#11-security-model-specification)
12. [Concurrency and Transaction Specification](#12-concurrency-and-transaction-specification)
13. [Strategic Implementation Roadmap](#13-strategic-implementation-roadmap)
14. [Language-Specific SDK Design Guidelines](#14-language-specific-sdk-design-guidelines)
15. [Governance and Compatibility Obligations](#15-governance-and-compatibility-obligations)
16. [References](#16-references)
17. [API Priority Classification: Essential vs. Background](#17-api-priority-classification-essential-vs-background)
18. [Wrapper Ecosystem Integration: RPC Broker, VistALink, MVDM, and FMQL](#18-wrapper-ecosystem-integration-rpc-broker-vistalink-mvdm-and-fmql)
19. [Rationale: Why gRPC + Protocol Buffers as the Two-Layer Foundation](#19-rationale-why-grpc--protocol-buffers-as-the-two-layer-foundation)
20. [Industrial Scale: Vendors Who Use This Pattern at Massive Scale](#20-industrial-scale-vendors-who-use-this-pattern-at-massive-scale)
21. [IRIS Implementation Guide: Building the Wrapper on InterSystems IRIS](#21-iris-implementation-guide-building-the-wrapper-on-intersystems-iris)
22. [YottaDB Implementation Guide: Building the Wrapper on YottaDB](#22-yottadb-implementation-guide-building-the-wrapper-on-yottadb)

---

## 1. Executive Summary

VA FileMan (package namespace `DI`, version 22.2) is the universal database engine of VistA — the Veterans Health Information Systems and Technology Architecture. Every one of VistA's 127 application packages stores its data exclusively in FileMan files and accesses that data exclusively through FileMan APIs. FileMan is not a wrapper around any third-party database; it is a self-contained database management system implemented entirely in ANSI Standard M (MUMPS).

This specification defines the complete design for a **FileMan External API Wrapper** — a language-neutral service and a set of idiomatic client SDKs in Python, Go, Rust, and JavaScript/TypeScript — that exposes the full operational surface of FileMan to non-M application developers. The wrapper is not a replacement for FileMan; it is an **Anti-Corruption Layer** (in the Domain-Driven Design sense) that preserves the full semantics of every FileMan operation while translating those operations into idioms native to modern programming languages.

The strategic objective is to enable a generation of VistA application development in languages with broad developer communities, modern tooling, strong type systems, cloud deployment models, and active open-source ecosystems — without requiring those developers to understand MUMPS, the M global storage model, or the VistA RPC Broker wire protocol.

The foundational documentation for all specifications in this document is the VA FileMan 22.2 documentation set published by the VA Office of Information and Technology on the VA Software Document Library (VDL).

---

## 2. Background: The Problem of Legacy Database Preservation

### 2.1 The Preservation Challenge

Institutional data systems that predate relational databases, the internet, and modern programming languages face a common structural problem: the data they manage is irreplaceable and actively in use, but the programming model required to access it is inaccessible to the current developer workforce. The system itself continues to perform its core function with exceptional reliability — it is the access model, not the data, that has become the bottleneck.

The canonical responses to this challenge are:

- **Full replacement** — Migrate data and logic to a modern platform. High risk, high cost, long timeline, frequent failure. The VA has attempted and abandoned multiple full-replacement efforts for VistA, including the Oracle Health (Cerner) EHRM contract.
- **Incremental strangling** — Progressively replace subsystems while the legacy system continues to operate. Viable for systems with clear module boundaries; difficult for tightly integrated systems like VistA where FileMan mediates nearly all inter-package data exchange.
- **API wrapping** — Expose the legacy system through a modern interface layer without modifying the core system. Lower risk, incremental delivery, preserves the battle-tested data layer while enabling modern application development.

API wrapping is the dominant strategy in production use at major healthcare systems, financial institutions, government agencies, and telecommunications companies that operate legacy COBOL, MUMPS, RPG, and PL/I systems. The approach is well-understood, has a decades-long production track record, and maps well to the specific characteristics of FileMan.

### 2.2 Why FileMan Is Particularly Well Suited to API Wrapping

FileMan has structural properties that make it an exceptionally good candidate for API wrapping:

1. **Existing programmatic API layer (DBS API).** FileMan already distinguishes between its interactive terminal API (Classic) and its silent programmatic API (DBS). The DBS API was explicitly designed for GUI clients and batch jobs — it accepts parameters, performs operations without writing to a terminal, and returns results in structured arrays. A wrapper does not need to reverse-engineer or screen-scrape anything; it simply needs to call the DBS API through a transport mechanism and translate the results.

2. **Self-describing schema.** The Data Dictionary (`^DD` global) is a live, runtime-queryable schema. A wrapper can introspect any FileMan file at runtime — field names, types, validation rules, pointer targets, cross-reference definitions — without any static schema compilation step. This enables dynamic, late-bound language SDKs that do not require code generation from a schema snapshot.

3. **Stable API contract.** The DBS API entry points (`FILE^DIE`, `GETS^DIQ`, `FIND^DIC`, etc.) have been stable across FileMan versions since at least version 22.0. FileMan is backward-compatible by design. An API wrapper built against these entry points will remain valid through future FileMan patches.

4. **Existing transport infrastructure.** The VistA RPC Broker (`XWB` package) already provides a TCP socket server that marshals M routine calls from external processes. The Broker has been in production use since the early 1990s and currently serves every CPRS GUI client at every VA medical center. The wire protocol is documented and has multiple open-source client implementations.

5. **Clear security model.** FileMan's security model is well-documented and parameterizable: file-level access codes, field-level access codes, and the Data Access Control (DAC) policy engine all operate on the `DUZ` and `DUZ(0)` variables set at session initialization. A wrapper can enforce this model without modification.

### 2.3 The Opportunity

The VistA ecosystem has produced decades of clinical knowledge encoded in data structures, cross-references, input transforms, and business logic embedded in FileMan files. A well-designed API wrapper would make this knowledge accessible to applications written in Python, Go, Rust, and JavaScript — the languages of modern data science, cloud services, and web development — without any risk to the underlying data or any modification of the core VistA system.

---

## 3. Industry Methodology: Wrapping Legacy Database Systems

### 3.1 Architectural Patterns

The software architecture community has developed several well-tested patterns for isolating legacy systems behind modern interfaces. The following patterns are directly applicable to FileMan wrapping:

**Anti-Corruption Layer (ACL)**
Defined by Eric Evans in *Domain-Driven Design* (2003). The ACL is a translation layer between a legacy system and a modern domain model. Its purpose is to prevent the legacy system's internal concepts (data structures, naming conventions, type systems, error codes) from "corrupting" the modern application's model. The ACL speaks the legacy system's language inward and the modern application's language outward. For FileMan, this means the ACL accepts IENs, IENS strings, FDA arrays, and FileMan date encoding internally, while presenting typed domain objects, ISO 8601 dates, and standard error types outward.

**Gateway Pattern**
A single point of entry through which all access to the legacy system flows. The Gateway encapsulates the transport mechanism (TCP socket, call-in interface, HTTP), handles authentication and session lifecycle, and presents a clean interface to callers. Callers have no knowledge of the underlying transport. The Gateway pattern maps directly to the connection and session management layer of a FileMan wrapper.

**Repository Pattern**
Popularized by Martin Fowler's *Patterns of Enterprise Application Architecture* (2002). A Repository provides collection-like access to domain objects (find by ID, find by criteria, add, remove) while hiding all persistence details. For FileMan, a per-file Repository wraps `GETS^DIQ`, `FIND^DIC`, `FILE^DIE`, and `UPDATE^DIE` behind a typed interface specific to each file's fields.

**Strangler Fig Pattern**
Described by Martin Fowler (2004). New functionality is implemented in the modern system; calls to the legacy system are progressively intercepted by the wrapper and either forwarded or handled natively. The legacy system "strangles" as more of its surface is covered by the wrapper. For VistA, this pattern supports a migration strategy where new application modules call the FileMan wrapper API from day one, while existing MUMPS routines continue to operate unchanged.

**Façade Pattern**
From the Gang of Four *Design Patterns* (1994). A Façade provides a simplified interface to a complex subsystem. The FileMan DBS API has significant complexity in its calling conventions (FDA arrays, IENS strings, M array result structures) that can be hidden behind a higher-level Façade that accepts and returns native language types.

### 3.2 Design Principles for Legacy Wrapping

The following principles are drawn from production experience at major institutions and from published literature on legacy modernization:

**Do not modify the legacy system.** The wrapper should require zero changes to FileMan, to VistA, or to any VistA MUMPS package. Any approach requiring patches to the core system introduces risk, requires VA approval through the ICR governance process, and creates a maintenance burden. The wrapper operates at the boundary, not inside.

**Preserve all semantics.** The wrapper must expose the full behavior of the wrapped API, not just the common cases. FileMan's INPUT transform validation, cross-reference trigger behavior, pointer resolution, audit logging, and key uniqueness enforcement are not implementation details — they are the system's business logic. A wrapper that silently bypasses them creates an inconsistent system.

**Type explicitly.** M is an untyped language. The wrapper is an opportunity to introduce explicit types (dates, enumerations, pointer types, numeric precision) that FileMan enforces through runtime transforms but never expresses as static types. Strongly typed wrapper SDKs reduce application-layer bugs and improve developer experience.

**Fail loudly and specifically.** FileMan's error model (the `DIERR` array) is rich but opaque to non-M developers. The wrapper must translate DIERR codes into typed, language-native exceptions with human-readable messages and sufficient context to diagnose the root cause without inspecting M globals.

**Layer the abstraction.** A two-tier design — a low-level thin wire adapter (calling FileMan DBS entry points directly) and a high-level typed SDK (presenting domain objects) — gives application developers the ergonomic interface they need while preserving the ability to drop to the low-level API when necessary. Do not collapse the two tiers.

**Document every divergence.** Where the wrapper's behavior diverges from raw FileMan (e.g., date encoding, null handling, empty-string semantics), the divergence must be explicitly documented. Undocumented divergences become bugs.

### 3.3 Transport Strategy Options

| Strategy | M Runtime | Mechanism | Latency | Co-location Required | Maturity |
|---|---|---|---|---|---|
| **YottaDB embedded call-in** | YottaDB | C shared library (`libyottadb.h`) via FFI; call-in table for routine dispatch | Sub-millisecond | Yes — same host | Production (YottaDB r1.34+) |
| **IRIS embedded call-in** | InterSystems IRIS | C shared library (`irisdb.h`) via FFI; push-invoke model for routine dispatch | Sub-millisecond | Yes — same host | Production (IRIS 2022.1+) |
| **IRIS TCP SuperServer** | InterSystems IRIS | IRIS wire protocol over TCP port 1972; `intersystems-irispython` or Java binding | LAN: 2–5 ms per call | No — remote host supported | Production (VA standard) |
| **VistA RPC Broker (TCP)** | Either | XWB wire protocol, TCP port 9200; dispatches named RPCs | Network round-trip | No | Production since 1993 |
| **Purpose-built gRPC service** | Either | gRPC over TLS, Protocol Buffers; gateway runs co-located with M runtime | Network round-trip | Gateway only | Greenfield |
| **REST/JSON over HTTP** | Either | HTTP/1.1 or HTTP/2; OpenAPI 3.1 specification | Network round-trip | No | Greenfield (see MVDM) |
| **FMQL REST service** | Either | HTTP/JSON, GraphQL-like syntax; read-only | Network round-trip | No | Research/prototype |

The recommended architecture uses **two complementary transports**:

1. A **gRPC service** (implemented in Go, running co-located with YottaDB) that calls FileMan DBS routines via YottaDB call-in and exposes a Protocol Buffer–typed API over mTLS. This service is the single authoritative server-side implementation of the wrapper.
2. A set of **language-native SDKs** (Python, Go, Rust, JavaScript/TypeScript) that are gRPC clients of the service, presenting an idiomatic API in each target language.

This architecture separates the transport concern (gRPC) from the language concern (idiomatic SDKs), enables a single server-side implementation to serve all client languages, and produces a strongly typed, self-documenting API contract (`.proto` files).

---

## 4. Case Studies: Successful Major API Wrapper Projects

The following projects represent production-scale, widely-deployed API wrapper implementations of legacy database and application systems. Each demonstrates specific patterns applicable to the FileMan wrapper.

### 4.1 VistA RPC Broker and CPRS GUI (VA, 1993–present)

**System wrapped:** VA FileMan / VistA MUMPS application logic
**Wrapper technology:** TCP socket server (`XWBTCPL` listener), Delphi `TRPCBroker` client component, later ported to .NET and JavaScript
**Scale:** ~170 VA medical centers, ~60,000 concurrent clinical users at peak
**Pattern:** Gateway + Façade. The RPC Broker provides a generic transport; CPRS registers specific RPCs in the REMOTE PROCEDURE file (#8994) that wrap targeted FileMan and application logic

**Lesson:** A generic, stable transport protocol (the XWB wire format) can support decades of application development without modification. The bottleneck in this design is not the transport but the requirement to register each new operation as a named RPC in a MUMPS file — a governance process that slows iteration. A more general DBS API transport would remove this bottleneck.

**Reference:** [VistA RPC Broker documentation (XWB package) — VDL appid=47](https://www.va.gov/vdl/application.asp?appid=47)

---

### 4.2 nodeVISTA / MVDM (VA/OSEHRA, 2015–2020)

**System wrapped:** VA FileMan / VistA MUMPS packages
**Wrapper technology:** Node.js server running on the VistA host, YottaDB call-in via the `nodem` npm package, JSON REST API
**Pattern:** Anti-Corruption Layer + Repository. MVDM defined a "Master VistA Data Model" — a set of JSON schemas mapping VistA FileMan concepts to modern domain objects. The wrapper translated between the MVDM JSON representation and the underlying FileMan data.
**Scale:** Prototype/research; deployed at OSEHRA test environments

**Lesson:** The data model design (what domain objects to expose and how to map FileMan fields to them) is the hardest part of the wrapper — not the transport. MVDM invested heavily in data modeling and produced the most semantically correct VistA API wrapper to date, but the project was discontinued before production deployment.

**Reference:** [OSEHRA VistA GitHub — nodeVISTA](https://github.com/vistadataproject/nodeVISTA) | [MVDM documentation](https://github.com/vistadataproject/VDM)

---

### 4.3 FMQL — FileMan Query Language (George Leal, 2010–2018)

**System wrapped:** VA FileMan (read-only)
**Wrapper technology:** Python/M hybrid service; HTTP/JSON REST; query language modeled on SPARQL for graph traversal of FileMan pointer relationships
**Pattern:** Query façade with graph semantics. FMQL exposed FileMan's pointer/cross-reference graph as a navigable linked-data structure, enabling full data-dictionary-driven traversal without prior knowledge of individual file schemas.
**Scale:** Used in research and in the VA's vistadataproject data analysis work

**Lesson:** FileMan's pointer model maps naturally to a graph data model. A wrapper that exposes this graph natively (rather than flattening it to relational tables) enables query patterns impossible with SQL.

**Reference:** [FMQL GitHub repository](https://github.com/caregraf/FMQL) | [FMQL paper — AMIA 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540540/)

---

### 4.4 VA Lighthouse / Benefits Intake API (VA OIT, 2018–present)

**System wrapped:** VistA data, Benefits and Enrollment systems
**Wrapper technology:** REST/JSON APIs, OAuth 2.0 / OpenID Connect, OpenAPI specification, hosted on VA Enterprise Cloud (AWS GovCloud)
**Pattern:** Strangler Fig + Gateway. Lighthouse APIs provide modern REST access to VistA data, progressively abstracting away the legacy transport. Internally, most Lighthouse APIs call VistA RPCs or query CDW (Corporate Data Warehouse).
**Scale:** Production; used by hundreds of VSO (Veteran Service Organization) applications and VA.gov

**Lesson:** A public API gateway with OpenAPI documentation, OAuth 2.0 authentication, and SLA-backed availability transforms a legacy system into a platform other organizations can build products on. The quality of the API specification (OpenAPI) is as important as the implementation.

**Reference:** [VA Lighthouse Developer Portal](https://developer.va.gov/) | [VA API Platform Strategy](https://github.com/department-of-veterans-affairs/va.gov-team/tree/master/products/lighthouse)

---

### 4.5 InterSystems IRIS REST and GraphQL Adapters (InterSystems, 2019–present)

**System wrapped:** Caché/IRIS ObjectScript applications and globals (M-family runtime)
**Wrapper technology:** REST API framework built into IRIS, Protocol Buffer / gRPC support, GraphQL adapter, Python/Java/Node gateways via `%Net.HttpRequest` and embedded Python
**Pattern:** Platform-native API layer. InterSystems built REST and gRPC directly into the IRIS runtime, enabling M-family global data to be exposed as first-class REST or gRPC services without a separate gateway process.
**Scale:** Production at thousands of healthcare and financial institutions worldwide

**Lesson:** When the M runtime vendor provides official API bridge tooling, that tooling is the correct first choice. For VistA/YottaDB, this is the YottaDB call-in interface — the direct equivalent of InterSystems' embedded Python and gRPC support.

**Reference:** [InterSystems IRIS REST documentation](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GREST) | [InterSystems IRIS for Health FHIR](https://docs.intersystems.com/irisforhealth20231/csp/docbook/DocBook.UI.Page.cls?KEY=HXFHIR)

---

### 4.6 SAP BAPI / RFC Wrapper (SAP, open-source clients, 1990s–present)

**System wrapped:** SAP R/3 and S/4HANA application server (ABAP runtime)
**Wrapper technology:** RFC (Remote Function Call) protocol over TCP; open-source clients in Java (`JCo`), Python (`pyrfc`, `python-sapjco3`), Go (`gorfc`), JavaScript (`node-rfc`)
**Pattern:** Gateway + typed SDK. SAP defines all external-facing business logic as BAPIs (Business Application Programming Interfaces) — named functions registered in the SAP function library. External clients call these functions via RFC. Language-specific SDKs wrap the RFC client library.
**Scale:** Used by every major SAP installation globally; billions of RFC calls per day in aggregate

**Lesson:** This is the closest structural analog to the FileMan/RPC Broker pattern. SAP BAPI/RFC is: a proprietary runtime (ABAP) + a wire protocol (RFC) + named callable functions (BAPIs) + language SDKs. The open-source language client ecosystem grew up around the official SAP RFC library. The FileMan wrapper should follow this model: a stable transport protocol + named callable operations + language SDKs.

**Reference:** [SAP BAPI Reference](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/0f18dddf28764651bc57024e79c2bcc4/4de08bfca7e2de61e10000000a42189b.html) | [Python RFC client (pyrfc)](https://github.com/SAP/PyRFC) | [Go RFC client (gorfc)](https://github.com/SAP/gorfc)

---

### 4.7 IBM CICS / COBOL REST Bridge (IBM z/OS Connect EE, 2015–present)

**System wrapped:** IBM CICS transaction programs (COBOL, PL/I, Assembler) on z/OS mainframes
**Wrapper technology:** IBM z/OS Connect Enterprise Edition — generates REST/JSON APIs from CICS transaction definitions; uses WSBIND data mappings to translate between JSON and COBOL copybooks
**Pattern:** Schema-driven Anti-Corruption Layer. The wrapper consumes CICS COMMAREA definitions (the COBOL equivalent of FileMan's IENS/FDA calling convention) and auto-generates REST API endpoints with OpenAPI 3.0 documentation.
**Scale:** Production at major banks, airlines, and insurance companies. COBOL processes an estimated $3 trillion per day globally.

**Lesson:** Schema-driven code generation from the legacy system's own type definitions produces correct wrappers at scale. For FileMan, the Data Dictionary (`^DD`) is the authoritative schema — the wrapper should generate typed client code from the DD, just as z/OS Connect generates REST APIs from CICS COMMAREA definitions.

**Reference:** [IBM z/OS Connect EE documentation](https://www.ibm.com/docs/en/zosconnect/3.0) | [IBM CICS REST API documentation](https://www.ibm.com/docs/en/cics-ts/6.1?topic=services-cics-as-restful-service-provider)

---

### 4.8 Oracle E-Business Suite REST APIs (Oracle, 2018–present)

**System wrapped:** Oracle EBS application logic and FND (Foundation) framework
**Wrapper technology:** Oracle REST Data Services (ORDS) + Oracle EBS Integration Repository REST APIs; internally calls Oracle Forms and PL/SQL APIs
**Pattern:** Façade over a multi-layer legacy application. Like FileMan, Oracle EBS has both an interactive forms layer and a programmatic PL/SQL API layer. The REST wrapper exposes only the programmatic layer, not the forms.

**Lesson:** When a legacy system has both an interactive UI layer and a silent programmatic API layer (like FileMan Classic vs. DBS), the wrapper should target only the programmatic layer. The interactive layer cannot be meaningfully wrapped for non-interactive callers.

**Reference:** [Oracle EBS Integration Repository](https://docs.oracle.com/en/applications/ebusiness/index.html) | [Oracle REST Data Services (ORDS)](https://www.oracle.com/database/technologies/appdev/rest.html)

---

## 5. FileMan as a Wrapping Target: Capabilities and Constraints

### 5.1 What CAN Be Fully Wrapped

The following FileMan API surfaces can be completely and faithfully wrapped for non-M callers:

| API Surface | Wrappability | Notes |
|---|---|---|
| **DBS API — full CRUD** | Full | `GETS^DIQ`, `FILE^DIE`, `UPDATE^DIE`, `FIND^DIC`, `$$FIND1^DIC`, `LIST^DIC` |
| **DBS API — validation** | Full | `CHK^DIE`, `VAL^DIE`, `VALS^DIE` |
| **DBS API — schema read** | Full | `FIELD^DID`, `FILE^DID`, `$$ROOT^DILFD` |
| **DBS API — lock management** | Full | `LOCK^DILF`, `UNLOCK^DILF` |
| **Classic API — silent add** | Full | `FILE^DICN` |
| **Classic API — date/time** | Full | `%DT`, `%DTC`, `$$DT^XLFDT`, `$$HTFM^XLFDT` |
| **DDE / Entity API** | Full (read) | `GET^DDE`, `$$GET1^DDE` |
| **SQLI projection** | Via direct SQL | Use ODBC/JDBC or direct SQL against the SQLI schema |
| **Auditing query** | Full | `CHANGED^DIAUTL` with date/field/user parameters |
| **Auditing control** | Full | `TURNON^DIAUTL`, `TURNOFF^DIAUTL` |
| **Import/Export** | Full (batch) | `DI^%ZIPM` import, FOREIGN FORMAT export operations |
| **Statistics** | Full | `EN^DISTAT` numeric field statistics |
| **Filegrams — generate** | Full | `^DIFG` serialization to MailMan message |
| **Data dictionary modification** | Full | `CREIXN^DDMOD`, `FILESEC^DDMOD` |
| **Security context setup** | Full | `DUZ`, `DUZ(0)` initialization via session setup call |

### 5.2 What CANNOT Be Meaningfully Wrapped

| API Surface | Reason | Alternative |
|---|---|---|
| **ScreenMan forms** (`^DDS`, `^DDGF`) | Requires VT100 terminal I/O; inherently interactive | Expose the underlying data via DBS API; build a separate UI framework |
| **Classic interactive API** (`^DIC`, `^DIE`, `^DIP`) | Writes directly to the M device (terminal); not parameterizable | Use DBS equivalents; these exist for every Classic call |
| **WORD-PROCESSING field editor** (`^DIWE`) | VT100 editor; screen I/O | Read/write WP field content via DBS `GETS^DIQ` / `FILE^DIE` without the editor |
| **Browser** (`EN^DIBU`) | VT100 scrolling viewer | Read WP content as text via `GETS^DIQ` |
| **Interactive print** (`^DIP`) | Writes to M device | Use `FIND^DIC` + `GETS^DIQ` and format output in the calling application |
| **DIFROM** | M-to-M package transfer mechanism; no external equivalent | N/A — managed by VistA DBA |

### 5.3 Constraints and Obligations

**Cross-reference trigger fidelity.** When the wrapper calls `FILE^DIE` or `UPDATE^DIE`, FileMan executes all cross-reference SET/KILL logic defined for the modified fields. This behavior occurs inside the M runtime and is not visible to the wrapper. The wrapper must guarantee that all writes go through FileMan APIs (never bypass to raw global manipulation) so that triggers, bulletins, and derived fields fire correctly.

**ICR (Integration Control Registration) obligation.** The VistA ICR governance process requires that any inter-package use of FileMan APIs be registered. A FileMan wrapper used by external applications is functionally equivalent to a new VistA package using FileMan APIs. If the wrapper is deployed in a VA-governed VistA instance, the applicable ICR registrations must be in place. DBIA #10012 (the global FileMan DBS API ICR) covers programmatic use of the DBS entry points.

**No direct global access.** The wrapper must never read or write MUMPS globals (`^DPT`, `^PS`, `^OR`, etc.) directly. All data access must go through FileMan DBS API calls. This is both a design principle and a VA governance requirement.

---

## 6. Transport Architecture Options

### 6.1 Recommended Architecture: gRPC Service + Language SDKs

```
┌─────────────────────────────────────────────────────────────────┐
│  Client Applications                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐ │
│  │  Python  │  │   Go     │  │  Rust    │  │ JavaScript/TS  │ │
│  │  SDK     │  │  SDK     │  │  SDK     │  │    SDK         │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───────┬────────┘ │
│       │              │              │                │          │
│       └──────────────┴──────────────┴────────────────┘          │
│                              │                                   │
│                    gRPC (Protocol Buffers / mTLS)                │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│  FileMan gRPC Gateway Service (Go)                              │
│  - Session management (DUZ context per connection)              │
│  - Request validation                                           │
│  - FDA serialization / IENS encoding                            │
│  - Error translation (DIERR → typed errors)                     │
│  - Observability (metrics, tracing, structured logging)         │
│  - Connection pool to YottaDB call-in                           │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                    YottaDB call-in (libyottadb.h)
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│  YottaDB M Runtime                                              │
│  - VA FileMan 22.2 (DI package)                                 │
│  - Kernel (XU package)                                          │
│  - All VistA application packages                               │
│  - M globals (^DPT, ^PS, ^OR, ^TIU, ...)                        │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Alternative: RPC Broker Adapter

For remote deployments where co-location with YottaDB is not possible, the gRPC Gateway can be replaced with an **RPC Broker Adapter** — a service that speaks the XWB wire protocol to an existing VistA Broker listener (TCP port 9200) and translates incoming gRPC calls to RPC Broker RPCs. The language SDKs remain unchanged; only the server-side implementation differs.

This path requires registering FileMan DBS wrapper RPCs in the REMOTE PROCEDURE (#8994) file on the VistA instance — a one-time setup step governed by the ICR process.

### 6.3 Alternative: REST/JSON Gateway

A REST/JSON gateway (OpenAPI 3.1 specification, HTTP/2) can be offered as an alternative transport for clients that cannot consume gRPC. The REST gateway should be a thin adapter over the gRPC service, not a separate implementation. All semantic validation and error translation should remain in the gRPC layer.

---

### 6.4 InterSystems IRIS Embedded Transport

InterSystems IRIS (and its predecessor, Caché) is the other major production M-family runtime. The VA FileMan Technical Manual explicitly states that FileMan is installed against a Caché/IRIS system in VA production, and the Technical Manual's KIDS distribution documentation assumes Caché/IRIS as the target platform. IRIS and YottaDB share the same fundamental M global storage model — both are compliant ANSI Standard M implementations — making the FileMan API wrapper equally applicable to IRIS-hosted VistA deployments.

#### IRIS vs. YottaDB: What Differs for the Wrapper

| Aspect | YottaDB | InterSystems IRIS |
|---|---|---|
| C call-in header | `libyottadb.h` | `irisdb.h` |
| Embedded library | `libyottadb.so` | `libirisdb.so` / `irisdb.dll` |
| Session init | `ydb_init()` | `IRISStart()` / `IRIS_CALLIN` environment |
| M function call | `ydb_ci()` / `ydb_cip()` | `IRISExStrCallA()` / `IRISPushStr()` + `IRISInvokeFunctionA()` |
| Global read | `ydb_get_s()` | `IRISGlobalGet()` |
| Global write | `ydb_set_s()` | `IRISGlobalSet()` |
| Global kill | `ydb_delete_s()` | `IRISGlobalKill()` |
| Subscript iteration | `ydb_subscript_next_s()` | `IRISGlobalOrder()` |
| Session shutdown | `ydb_exit()` | `IRISEnd()` |
| Environment config | `YOTTADB`, `gtmroutines`, `gtmgbldir` | `IRISDIR`, `ISC_PACKAGE_INSTALLDIR`, `[Startup]` config section |
| Python binding | `yottadb` (PyPI) | `iris` (PyPI — `intersystems-irispython`) |
| Go binding | `lang.yottadb.com/go/yottadb` | IRIS Go binding (via `irisdb.h` + cgo) |
| TCP SuperServer port | N/A (no built-in TCP listener) | 1972 (IRIS SuperServer) |
| Native REST/JSON | No — external wrapper required | Yes — IRIS %REST framework built-in |

#### IRIS Call-In Model

IRIS provides two embedded call-in mechanisms:

**1. IRIS C Binding (`irisdb.h`)** — The direct equivalent of YottaDB's `libyottadb.h`. The wrapper initializes an IRIS connection with `IRISStart()`, sets the M process context (equivalent to setting `DUZ` and `DUZ(0)`), then calls FileMan DBS entry points using `IRISExStrCallA()` for extrinsic functions (`$$FIND1^DIC`, `$$GET1^DIQ`) and a push-invoke sequence for procedure calls (`GETS^DIQ`, `FILE^DIE`, `UPDATE^DIE`). Results are read back via `IRISGlobalGet()` and `IRISGlobalOrder()` for traversing result arrays.

The IRIS C binding is the most direct path — it gives sub-millisecond call latency identical to YottaDB call-in and requires no network socket.

**2. IRIS Python Gateway (`iris` package)** — `pip install intersystems-irispython`. Provides `iris.cls()` for ObjectScript class calls and `iris.ref()` for global access. The `iris.gref()` object supports `get()`, `set()`, `kill()`, and `order()` operations that map directly to the YottaDB Python equivalents. FileMan DBS calls are invoked using `iris.system.Process.CallM()` or through the `%Library.Routine` interface.

**3. IRIS TCP SuperServer (port 1972)** — IRIS runs a persistent TCP listener (the SuperServer) on port 1972. External processes connect via the IRIS protocol (not RPC Broker). The IRIS Python, Java, and .NET bindings use this path when not embedded. For the FileMan wrapper, this is the remote IRIS equivalent of the RPC Broker path — it requires IRIS-side M wrapper routines that accept calls and invoke FileMan DBS APIs.

#### Implementing the IRIS Transport in the gRPC Gateway

The gRPC Gateway service (§6.1) uses a pluggable **MRuntime** interface with two concrete implementations:

```
MRuntime (interface)
  ├── YDBRuntime    — calls libyottadb.h
  └── IRISRuntime   — calls irisdb.h
```

The `FileManClient` layer in the gateway service is runtime-agnostic — it calls `MRuntime.CallFunction()`, `MRuntime.GetGlobal()`, `MRuntime.SetGlobal()`, etc. regardless of which M implementation is underneath. Only the concrete runtime implementation differs.

This design means the gRPC Gateway, and all four language SDKs, work identically against both YottaDB and IRIS deployments. Operators choose the runtime at deployment time through configuration; no application code changes are required.

#### IRIS-Specific Considerations

**Session context:** IRIS uses a `$NAMESPACE` concept to switch between databases. FileMan globals must be in the correct namespace (typically `%SYS` or the VistA application namespace). The IRIS runtime must `SET $NAMESPACE = "VISTA"` (or equivalent) before making FileMan calls.

**Global mapping:** IRIS supports global mapping across namespaces. In a standard VA IRIS deployment, FileMan globals (`^DPT`, `^PS`, `^OR`, etc.) may be mapped from the application namespace to a data namespace. The wrapper must confirm the global root returned by `$$ROOT^DILFD` resolves correctly in the active namespace.

**License model:** InterSystems licenses IRIS per-CPU or per-user. The wrapper's connection pooling strategy must account for IRIS license limits — each concurrent connection consumes a license unit. Pool size must be bounded by the site's IRIS license capacity.

**Embedded Python vs. call-in:** For Python-based gateway implementations targeting IRIS, the `iris` Python package (intersystems-irispython) provides the most ergonomic embedded path. The package wraps the IRIS C binding and handles session lifecycle, namespace management, and error translation, equivalent to the `yottadb` package for YottaDB.

---

## 7. API Surface Specification — Complete FileMan Coverage

The following sections specify the full operational surface that the wrapper must expose. Each section maps FileMan DBS entry points to wrapper API operations, defines the input and output contracts, and notes required translation work.

All FileMan DBS entry point documentation is from the *VA FileMan 22.2 Developer's Guide* (see [References](#16-references)).

---

### 7.1 DBS API — Core Read Operations

#### 7.1.1 `GetEntry` — Retrieve fields for one entry

**FileMan DBS:** `GETS^DIQ(file#, iens, fields, flags, msg, result)`

**Wrapper operation:** `GetEntry(file, ien, fields, options) → Entry`

**Input contract:**

| Parameter | Type | Description |
|---|---|---|
| `file` | string (file number) | Target FileMan file number, e.g. `"2"` |
| `ien` | string or integer | Internal Entry Number of the target record |
| `fields` | string or list | Semicolon-delimited field numbers, `"*"` for all, `"**"` for all including multiples |
| `options.include_external` | bool (default true) | Include external (display) values in result |
| `options.include_internal` | bool (default true) | Include internal (stored) values in result |
| `options.no_nulls` | bool (default false) | Omit fields with null/empty values |

**Output contract:**

```
Entry {
  file:     string              // file number
  ien:      string              // IEN of the retrieved entry
  fields:   map<string, FieldValue>   // field# → value pair
}

FieldValue {
  internal: string | null       // stored value (IEN for pointers, FileMan date, etc.)
  external: string | null       // display value (resolved pointer, formatted date, etc.)
  word_processing: list<string> | null  // for WP fields only
  multiple: list<SubEntry> | null       // for multiple (subfile) fields only
}
```

**Translation obligations:**
- IENS construction: the wrapper appends trailing comma(s) — `"100,"` for a top-level entry
- The `"E"` flag in `GETS^DIQ` flags returns external values; the `"I"` flag returns internal
- WP (WORD-PROCESSING) fields are returned as a list of lines from the WP sub-nodes
- Multiple-valued fields (sub-files) are returned as nested `SubEntry` lists when `"**"` is specified

---

#### 7.1.2 `GetField` — Retrieve a single field value

**FileMan DBS:** `$$GET1^DIQ(file#, iens, field, flag, msg, node)`

**Wrapper operation:** `GetField(file, ien, field, format) → string`

**Input contract:** file, ien, field number, format (`"internal"` or `"external"`)

**Output contract:** single string value; empty string if field is null

---

#### 7.1.3 `FindOne` — Find a single matching entry

**FileMan DBS:** `$$FIND1^DIC(file, screen, index, value, flags)`

**Wrapper operation:** `FindOne(file, value, options) → string | null`

**Input contract:**

| Parameter | Type | Description |
|---|---|---|
| `file` | string | FileMan file number |
| `value` | string | Lookup value |
| `options.index` | string (default `"B"`) | Cross-reference index name |
| `options.flags` | string | Lookup flags (`"O"` = exact match only) |

**Output contract:** IEN string if found; null if not found; error on ambiguous match

---

#### 7.1.4 `Find` — Find multiple matching entries

**FileMan DBS:** `FIND^DIC(file, screen, index, value, count, flags, from, result)`

**Wrapper operation:** `Find(file, value, options) → FindResult`

**Input contract:**

| Parameter | Type | Description |
|---|---|---|
| `file` | string | FileMan file number |
| `value` | string | Lookup value (prefix match on index) |
| `options.index` | string (default `"B"`) | Cross-reference index name |
| `options.max_results` | integer (default 200) | Maximum number of results |
| `options.from_ien` | string | Resume pagination from this IEN |
| `options.screen` | string | M code expression for filtering results |
| `options.part` | string | `"B"` = begins-with, `"P"` = partial, `""` = exact |

**Output contract:**

```
FindResult {
  iens:     list<string>    // matched IENs in index order
  more:     bool            // true if max_results was hit (pagination available)
  next_ien: string | null   // resume token for next page
}
```

---

#### 7.1.5 `ListEntries` — Retrieve a sorted range of entries

**FileMan DBS:** `LIST^DIC(file, screen, index, from, part, flags, max, result)`

**Wrapper operation:** `ListEntries(file, options) → ListResult`

**Output contract:**

```
ListResult {
  entries: list<{ien: string, value: string}>  // IEN + .01 value
  more:    bool
}
```

---

### 7.2 DBS API — Core Write Operations

#### 7.2.1 `File` — Create or update entries (no audit)

**FileMan DBS:** `FILE^DIE(flags, fda, errors)`

**Wrapper operation:** `File(fda, options) → FileResult`

**Input contract:**

```
FDA (FileMan Data Array) {
  entries: list<FDAEntry>
}

FDAEntry {
  file:   string         // FileMan file number
  iens:   string         // IENS: "+1," for new; "42," for existing
  fields: map<string, string>   // field# → value to file
}
```

**Notes on IENS for new entries:**
- Use `"+1,"` for the first new top-level entry
- Use `"+2,"`, `"+3,"` etc. for multiple new entries in the same FDA transaction
- For new sub-entries: `"+1,42,"` = new sub-entry in parent IEN 42
- FileMan replaces `"+N,"` with the assigned IEN in the FDA after filing

**Output contract:**

```
FileResult {
  ien_map:  map<string, string>  // "+1," → "42" (new IEN assigned)
  errors:   list<FileManError>   // empty if successful
}
```

**Flags supported by `FILE^DIE`:**

| Flag | Meaning |
|---|---|
| `""` (empty) | Default: no special behavior |
| `"S"` | Suppress cross-reference triggers (use with caution) |
| `"E"` | Input values are in external (display) format; FileMan will look them up |
| `"T"` | Perform a test run — validate without filing |

---

#### 7.2.2 `Update` — Update with audit and key validation

**FileMan DBS:** `UPDATE^DIE(flags, fda, errors)`

**Wrapper operation:** `Update(fda, options) → FileResult`

`UPDATE^DIE` differs from `FILE^DIE` in that it:
- Performs full audit logging (`^DIA`, file #1.1) for every modified field
- Enforces KEY uniqueness constraints before filing
- Validates all INPUT transforms before modifying the database
- Does not support the `"S"` (suppress cross-reference) flag

The wrapper must use `UPDATE^DIE` for all normal application writes. `FILE^DIE` should be reserved for bulk loading, data migration, and cases where the caller has explicitly opted out of audit.

---

#### 7.2.3 `Delete` — Delete a file entry

**FileMan DBS:** `EN^DIK(file#, ien)` (Classic, but no DBS equivalent for full delete)

**Wrapper operation:** `Delete(file, ien, options) → DeleteResult`

FileMan does not have a single DBS-layer delete call. Deletion requires:
1. Setting the `.01` field to `@` (the FileMan delete sentinel) via `FILE^DIE`
2. Calling `EN^DIK` to process the deletion and fire KILL cross-references
3. The wrapper must implement this two-step sequence atomically (with `LOCK^DILF` protecting the entry during the sequence)

**This operation requires special attention:** deletion in FileMan triggers all KILL cross-references, which may cascade into other files. The wrapper must document this behavior explicitly.

---

#### 7.2.4 `BatchFile` — File multiple FDA entries in a single call

**FileMan DBS:** `FILE^DIE` with a multi-entry FDA array

**Wrapper operation:** `BatchFile(batch, options) → BatchResult`

FileMan's `FILE^DIE` and `UPDATE^DIE` natively accept FDA arrays with multiple files and IENS strings in a single call. The wrapper's batch operation maps directly to this: a single FDA array containing multiple entries across potentially multiple files is filed in one M call. FileMan does not provide true ACID transaction semantics across multiple files; the batch operation should be documented accordingly.

---

### 7.3 DBS API — Validation

#### 7.3.1 `ValidateField` — Validate a value without filing

**FileMan DBS:** `CHK^DIE(file, iens, field, value, result)`

**Wrapper operation:** `ValidateField(file, ien, field, value) → ValidationResult`

**Output contract:**

```
ValidationResult {
  valid:    bool
  internal: string | null    // what FileMan would store internally if valid
  external: string | null    // external display value if valid
  error:    string | null    // error message if invalid
}
```

---

#### 7.3.2 `ValidateEntry` — Validate multiple field values

**FileMan DBS:** `VALS^DIE(file, iens, fda, errors)`

**Wrapper operation:** `ValidateEntry(file, ien, fields) → ValidationResult`

Validates a set of field values for a single entry without modifying the database.

---

### 7.4 DBS API — Schema Introspection

#### 7.4.1 `GetFileDef` — Retrieve file data dictionary attributes

**FileMan DBS:** `FILE^DID(file, field_list, flags, result)`

**Wrapper operation:** `GetFileDef(file) → FileDef`

**Output contract:**

```
FileDef {
  file_number:    string
  name:           string       // file name (e.g., "PATIENT")
  global_root:    string       // M global root (e.g., "^DPT(")
  field_count:    integer
  security_codes: SecurityCodes { read, write, delete, laygo }
  description:    string | null
}
```

---

#### 7.4.2 `GetFieldDef` — Retrieve field data dictionary attributes

**FileMan DBS:** `FIELD^DID(file, field, flags, result)`

**Wrapper operation:** `GetFieldDef(file, field) → FieldDef`

**Output contract:**

```
FieldDef {
  field_number:   string
  label:          string
  data_type:      DataType    // see Section 8 for type enumeration
  required:       bool
  max_length:     integer | null
  pointer_target: string | null    // file number if POINTER TO A FILE
  variable_pointer_targets: list<string> | null
  computed:       bool
  audit_enabled:  bool
  security_code:  string | null
  input_help:     string | null
  description:    string | null
  cross_references: list<CrossRefDef>
}
```

---

#### 7.4.3 `ListFiles` — List all files on this VistA instance

**Source:** FILE (#1) file via `FIND^DIC`

**Wrapper operation:** `ListFiles(options) → list<FileSummary>`

Queries the FILE (#1) file to return all defined FileMan files. Optionally filtered by number range, name prefix, or owning package.

---

#### 7.4.4 `GetGlobalRoot` — Resolve file global root

**FileMan DBS:** `$$ROOT^DILFD(file, sub_array_of, flags)`

**Wrapper operation:** `GetGlobalRoot(file) → string`

Returns the M global root for a given file number (e.g., `"^DPT("` for file `2`).

---

### 7.5 Classic API — Wrappable Subset

Most Classic API calls are interactive and cannot be meaningfully wrapped. The following subset can be wrapped:

#### 7.5.1 `AddEntry` — Add new entry silently

**FileMan Classic:** `FILE^DICN` (add-new without prompting)

**Wrapper operation:** `AddEntry(file, name_value, options) → AddResult`

Adds a new entry with the specified `.01` (name) field value. Equivalent to `FILE^DIE` with a `"+1,"` IENS and only the `.01` field set; exposed separately for its ergonomic convenience.

---

#### 7.5.2 `DateConvert` — Convert between FileMan and external date formats

**FileMan Classic:** `%DT`, `%DTC`, `$$DT^XLFDT`, `$$HTFM^XLFDT`

**Wrapper operations:**

| Operation | Function |
|---|---|
| `ExternalToFM(date_string)` | Convert human-readable date string to FileMan internal format |
| `FMToExternal(fm_date)` | Convert FileMan internal date to ISO 8601 string |
| `FMArithmetic(fm_date, expression)` | Add/subtract days/months/years from a FileMan date |
| `FMNow()` | Return current date/time in FileMan internal format |

This is one of the most critical translation services the wrapper provides. FileMan's internal date format (`YYYMMDD.HHMMSS` where YYY = year - 1700) must never be exposed directly to client applications. All dates crossing the API boundary must be in ISO 8601 format (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ`).

---

### 7.6 DDE / Entity API

#### 7.6.1 `GetEntity` — Retrieve a single entity record

**FileMan DBS:** `$$GET1^DDE(entity_name, ien, format)`

**Wrapper operation:** `GetEntity(entity, ien, format) → string`

Returns the JSON or XML representation of a FileMan entity as defined in the ENTITY (#1.5) file.

---

#### 7.6.2 `GetEntities` — Retrieve multiple entity records

**FileMan DBS:** `GET^DDE(entity_name, iens_array, format, result)`

**Wrapper operation:** `GetEntities(entity, iens, format) → list<string>`

Returns a JSON or XML array of entity records. Used by the VPR and FHIR exposure pipelines.

---

#### 7.6.3 `ListEntities` — List defined entities

**Source:** ENTITY (#1.5) file via `FIND^DIC`

**Wrapper operation:** `ListEntities() → list<EntityDef>`

Enumerates all defined entities on this VistA instance, with their name, mapped file, and field mapping summary.

---

### 7.7 SQLI Projection Layer

The SQLI layer projects FileMan files as SQL tables accessible via ODBC. The wrapper should expose this through a dedicated operation:

#### 7.7.1 `GetSQLISchema` — Retrieve SQLI table definitions

**Source:** SQLI_SCHEMA (#1.521) file and related SQLI files

**Wrapper operation:** `GetSQLISchema(file) → SQLITableDef`

Returns the SQLI projection for a given FileMan file — table name, column definitions, foreign key relationships, and index definitions.

This enables client applications to understand the SQL representation of FileMan data for reporting and analytics use cases.

---

### 7.8 Cross-Reference Management

#### 7.8.1 `ReIndex` — Rebuild cross-references for a file or entry

**FileMan DBS:** `EN^DIK(file, ien)` / `^DIK`

**Wrapper operation:** `ReIndex(file, options) → ReIndexResult`

Rebuilds all cross-references for the specified file or for a single entry. This is an administrative operation; it should require elevated access codes and be rate-limited.

---

#### 7.8.2 `CreateCrossReference` — Create a new-style cross-reference

**FileMan DBS:** `CREIXN^DDMOD(parameters_array)`

**Wrapper operation:** `CreateCrossReference(file, xref_def) → CrossRefResult`

Programmatically creates a new-style cross-reference (INDEX file #0.11). Requires DBA-level access. The wrapper must require explicit confirmation and validate the M SET/KILL code for syntax before submitting.

---

### 7.9 Lock Management

#### 7.9.1 `Lock` — Acquire a FileMan lock

**FileMan DBS:** `LOCK^DILF(file, ien, timeout)`

**Wrapper operation:** `Lock(file, ien, options) → LockResult`

Acquires a MUMPS `LOCK` on the specified file entry for concurrency control. Used before multi-step operations (e.g., read-modify-write sequences) that must be atomic with respect to other processes.

**Output contract:**

```
LockResult {
  acquired:  bool
  lock_token: string    // opaque token used to release the lock
}
```

---

#### 7.9.2 `Unlock` — Release a FileMan lock

**FileMan DBS:** `UNLOCK^DILF(file, ien)` / MUMPS `LOCK -`

**Wrapper operation:** `Unlock(lock_token) → void`

Releases a previously acquired lock. The lock_token from `Lock` is required. Locks must be released by the same session that acquired them; the wrapper must enforce this.

---

### 7.10 Auditing Utilities

#### 7.10.1 `GetAuditHistory` — Query audit trail for a field

**FileMan:** `CHANGED^DIAUTL(file, ien, field, from_date, to_date, result)`

**Wrapper operation:** `GetAuditHistory(query) → list<AuditEntry>`

**Input contract:**

```
AuditQuery {
  file:       string
  ien:        string | null     // null = all entries
  field:      string | null     // null = all fields
  from_date:  ISO 8601 string | null
  to_date:    ISO 8601 string | null
  user_ien:   string | null     // filter by user (NEW PERSON IEN)
}
```

**Output contract:**

```
AuditEntry {
  file:        string
  ien:         string
  field:       string
  field_label: string
  changed_by:  string    // NEW PERSON IEN
  changed_at:  ISO 8601 string
  old_value:   string | null
  new_value:   string | null
}
```

---

#### 7.10.2 `SetAudit` — Enable or disable field-level auditing

**FileMan:** `TURNON^DIAUTL(file, field)` / `TURNOFF^DIAUTL(file, field)`

**Wrapper operation:** `SetAudit(file, field, enabled) → void`

Requires `XUAUDITING` security key.

---

### 7.11 Archiving and Filegrams

#### 7.11.1 `ExportFilegram` — Serialize entries to Filegram format

**FileMan:** `^DIFG` archive/export invocation

**Wrapper operation:** `ExportFilegram(file, iens, options) → FilegamPayload`

Returns a Filegram-formatted serialization of the specified entries — suitable for inter-site transfer or long-term archival. The Filegram is returned as a structured string (the same format used by MailMan for inter-site transport).

---

#### 7.11.2 `ImportFilegram` — Install a Filegram into FileMan

**FileMan:** `^DIFG` install invocation

**Wrapper operation:** `ImportFilegram(filegram_payload) → ImportResult`

---

### 7.12 Import and Export Utilities

#### 7.12.1 `ImportFromTemplate` — Import external data using an IMPORT TEMPLATE

**FileMan:** `DI^%ZIPM` or IMPORT TEMPLATE (`^DIST(.46,`) processing

**Wrapper operation:** `ImportFromTemplate(template_name, data_rows) → ImportResult`

Imports an array of external data rows using a named IMPORT TEMPLATE, applying the template's field mappings and INPUT transforms.

---

#### 7.12.2 `ExportForeignFormat` — Export entries using a FOREIGN FORMAT

**FileMan:** FOREIGN FORMAT (`^DIST(.44,`) processing

**Wrapper operation:** `ExportForeignFormat(file, format_name, iens) → string`

Returns the formatted export output (CSV, fixed-width, or other) for the specified entries.

---

### 7.13 Statistics Utilities

#### 7.13.1 `ComputeStatistics` — Descriptive statistics over a numeric field

**FileMan:** `EN^DISTAT(file, field, screen, result)`

**Wrapper operation:** `ComputeStatistics(file, field, options) → StatsResult`

**Output contract:**

```
StatsResult {
  count:    integer
  min:      number
  max:      number
  mean:     number
  std_dev:  number
  histogram: list<HistogramBin> | null
}
```

---

### 7.14 Date and Time Services

This section is a dedicated expansion of §7.5.2, because date handling is the single most common source of integration bugs with FileMan systems.

#### FileMan Date Encoding

FileMan stores dates as `YYYMMDD` where `YYY = year − 1700`. Examples:

| FileMan Date | Calendar Date |
|---|---|
| `3240408` | April 8, 2024 |
| `3260101` | January 1, 2026 |
| `2600115` | January 15, 1960 |
| `3240408.143022` | April 8, 2024, 14:30:22 |

**The wrapper must:**
- Accept ISO 8601 dates on all inbound calls
- Return ISO 8601 dates on all outbound calls
- Never expose the `YYYMMDD` format to client applications
- Provide explicit conversion utilities for client code that must convert between formats

#### Date Operation Specification

| Wrapper Operation | FileMan Entry Point | Description |
|---|---|---|
| `ParseFMDate(fm_date)` | `$$HTFM^XLFDT` | FM date → ISO 8601 string |
| `FormatFMDate(iso_date)` | `$$FMTH^XLFDT` / `%DT` | ISO 8601 → FM internal |
| `FMNow()` | `$$NOW^XLFDT` | Current date/time in FM format |
| `FMToday()` | `$$TODAY^XLFDT` | Current date (no time) in FM format |
| `FMDateAdd(fm_date, days)` | `%DTC` with `"D"` flag | Add/subtract days from FM date |
| `FMDateDiff(fm1, fm2)` | `%DTC` with `"D"` flag | Difference in days between two FM dates |
| `ValidateFMDate(fm_date)` | `$$FMCHK^XLFDT` | Validate FM internal date value |

---

### 7.15 Security and Context Management

#### 7.15.1 `CreateSession` — Establish an authenticated FileMan session

**Mechanism:** Kernel XUS SIGNON RPC (via Broker) or YottaDB embedded DUZ initialization

**Wrapper operation:** `CreateSession(credentials) → Session`

**Input contract:**

```
Credentials {
  // For Kernel authentication (production VistA):
  access_code:   string    // encrypted in transit
  verify_code:   string    // encrypted in transit

  // For service account (automated processes):
  service_duz:   string    // pre-provisioned DUZ for the service account
  service_key:   string    // shared secret or certificate
}
```

**Output contract:**

```
Session {
  session_id:   string      // opaque token; required on all subsequent calls
  duz:          string      // user IEN in NEW PERSON file (#200)
  user_name:    string      // display name
  access_codes: string      // DUZ(0) value — determines file permissions
  expires_at:   ISO 8601 string
}
```

---

#### 7.15.2 `CheckAccess` — Verify access to a file

**FileMan:** Access code comparison against file security code in `^DIC`

**Wrapper operation:** `CheckAccess(file, operation, session) → AccessResult`

Returns whether the current session has read, write, delete, or add access to the specified file.

---

#### 7.15.3 `EvaluatePolicy` — Evaluate a DAC policy

**FileMan:** `$$CANDO^DIAC1(action, ien, parameters)`

**Wrapper operation:** `EvaluatePolicy(action, ien, parameters) → bool`

Evaluates a Data Access Control (DAC) policy action. Returns true if the current session's context satisfies the policy. Added in FileMan 22.2 patch DI*22.2*8.

---

### 7.16 Data Dictionary Administration

#### 7.16.1 `SetFileSecurity` — Set file-level security codes

**FileMan DBS:** `FILESEC^DDMOD(file, security_array)`

**Wrapper operation:** `SetFileSecurity(file, codes) → void`

Requires programmer access (`DUZ(0)="@"`).

---

#### 7.16.2 `GetDDAudit` — Query data dictionary change audit

**Source:** DD AUDIT (#0.6) file (`^DDA`)

**Wrapper operation:** `GetDDAudit(file, from_date, to_date) → list<DDAuditEntry>`

Returns a history of data dictionary modifications (schema changes) for the specified file.

---

## 8. Data Type Mapping Specification

FileMan's type system (defined in the DATA TYPE file #0.81) must be mapped to native types in each target language. The following table defines the canonical mapping.

| FileMan Type | FileMan Storage | Wrapper Canonical Type | Python | Go | Rust | TypeScript |
|---|---|---|---|---|---|---|
| FREE TEXT | String ≤ 245 chars | `string` | `str` | `string` | `String` | `string` |
| NUMERIC | Numeric string | `decimal` | `Decimal` | `float64` | `Decimal` | `number` |
| SET OF CODES | Code string from set | `enum` (string-backed) | `str` (enum class) | `string` (const) | `enum` | `string` (union type) |
| DATE | `YYYMMDD` | `date` (ISO 8601) | `datetime.date` | `time.Time` | `chrono::NaiveDate` | `string` (ISO 8601) |
| DATE/TIME | `YYYMMDD.HHMMSS` | `datetime` (ISO 8601 with tz) | `datetime.datetime` | `time.Time` | `chrono::DateTime` | `string` (ISO 8601) |
| POINTER TO A FILE | IEN integer | `Reference { file, ien, display }` | `FileManRef` | `Reference` | `Reference` | `FileManRef` |
| VARIABLE POINTER | File#+IEN | `VariableRef { file, ien, display }` | `VarFileManRef` | `VariableRef` | `VariableRef` | `VarFileManRef` |
| WORD-PROCESSING | Multi-line sub-nodes | `list<string>` (lines) | `list[str]` | `[]string` | `Vec<String>` | `string[]` |
| MULTIPLE | Sub-file entries | `list<SubEntry>` | `list[Entry]` | `[]SubEntry` | `Vec<SubEntry>` | `SubEntry[]` |
| COMPUTED | M expression result | `string` (always external) | `str` | `string` | `String` | `string` |
| BOOLEAN | `1`/`0` or `Y`/`N` | `bool` | `bool` | `bool` | `bool` | `boolean` |
| MUMPS | Executable M code | `string` (opaque) | `str` | `string` | `String` | `string` |

### Notes on Type Mapping

**NUMERIC precision:** FileMan stores numerics as strings to avoid M's imprecise floating-point behavior. The wrapper must use `Decimal` (Python), or `decimal.Decimal`-equivalent representations, never `float`, for financial and clinical numeric fields.

**SET OF CODES:** The valid codes and their internal/external mappings are defined in the field's DD (`DATA TYPE` and `SET` attributes). The wrapper should expose these as string enumerations in strongly typed languages. Code generation from the DD (§13.4) can produce typed enum definitions.

**POINTER resolution:** `GetEntry` with `include_external=true` resolves pointers via the `"E"` flag of `GETS^DIQ`. The wrapper returns both the IEN (internal value) and the display name (external value) in a `Reference` object. Callers must not store IENs across system boundaries — IENs are local to a specific VistA instance and are not globally unique.

**NULL semantics:** FileMan represents null (absent field value) as an empty string. The wrapper must translate empty strings to language-native null types (`None`, `nil`, `Option::None`, `null`) in all output paths.

---

## 9. Error Surface Specification

### 9.1 FileMan DIERR Array

FileMan signals errors through the `DIERR` array:

```
DIERR          = number of errors
DIERR(n)       = error code
DIERR(n,"TEXT",1) = primary error message text
DIERR(n,"TEXT",2) = secondary message text (if any)
DIERR(n,"PARAM",m) = substitution parameters for message formatting
```

### 9.2 Wrapper Error Taxonomy

The wrapper must translate all DIERR codes into a typed error hierarchy:

```
FileManError (base)
  ├── NotFoundError           // File or entry does not exist
  ├── ValidationError         // INPUT transform rejected the value
  │     fields: list<FieldError { field, value, message }>
  ├── KeyViolationError       // Key uniqueness constraint violated
  │     key_name: string
  │     duplicate_ien: string
  ├── AccessDeniedError       // Insufficient access codes
  │     required: string
  │     held: string
  ├── LockTimeoutError        // LOCK not acquired within timeout
  ├── SchemaError             // Data dictionary / file structure error
  ├── PolicyDeniedError       // DAC policy evaluation rejected the operation
  │     action: string
  │     policy: string
  └── TransportError          // Connection, timeout, or protocol error
```

### 9.3 Common DIERR Codes

| DIERR Code | Wrapper Error Type | Meaning |
|---|---|---|
| 1 | `NotFoundError` | Field not found in data dictionary |
| 2 | `NotFoundError` | File not found |
| 4 | `ValidationError` | Invalid value for field (INPUT transform failed) |
| 5 | `ValidationError` | Required field missing |
| 6 | `ValidationError` | Value exceeds maximum length |
| 7 | `KeyViolationError` | Key uniqueness constraint violated |
| 8 | `ValidationError` | Field is read-only (computed or locked) |
| 501 | `AccessDeniedError` | Insufficient file-level access code |
| 502 | `AccessDeniedError` | Insufficient field-level access code |

---

## 10. Wire Protocol and Serialization Specification

### 10.1 gRPC / Protocol Buffers

The canonical wire format is Protocol Buffers 3 over gRPC. A single `.proto` file defines the complete FileMan API surface:

**Service definition structure (`.proto` outline — not code):**

- `FileManService` — the primary service
  - `GetEntry`, `GetField`, `Find`, `FindOne`, `ListEntries` — read RPCs
  - `File`, `Update`, `Delete`, `BatchFile` — write RPCs
  - `ValidateField`, `ValidateEntry` — validation RPCs
  - `GetFileDef`, `GetFieldDef`, `ListFiles` — schema RPCs
  - `GetEntity`, `GetEntities`, `ListEntities` — DDE RPCs
  - `Lock`, `Unlock` — lock management RPCs
  - `GetAuditHistory`, `SetAudit` — audit RPCs
  - `ExportFilegram`, `ImportFilegram` — filegram RPCs
  - `ComputeStatistics` — statistics RPC
  - `CreateSession`, `DestroySession`, `CheckAccess` — session RPCs
  - `DateConvert` — date utility RPCs

- `FindStream` — server-streaming RPC for large result sets (cursor-based pagination)
- `BatchFile` — client-streaming RPC for bulk write operations

### 10.2 REST/JSON Supplement

A REST/JSON API must be provided as a secondary transport for clients that cannot consume gRPC. The REST API must conform to OpenAPI 3.1 and provide the same semantic operations as the gRPC API. Implemented as a gRPC-Gateway transcoding layer (not a separate implementation).

URL structure:

```
GET    /files/{file}/entries/{ien}                  → GetEntry
GET    /files/{file}/entries?value=X&index=B        → Find
POST   /files/{file}/entries                        → File (create)
PUT    /files/{file}/entries/{ien}                  → Update
DELETE /files/{file}/entries/{ien}                  → Delete
GET    /files/{file}/schema                         → GetFileDef
GET    /files/{file}/fields/{field}/schema          → GetFieldDef
GET    /files/{file}/audit?ien=X&from=Y&to=Z        → GetAuditHistory
GET    /entities/{entity}/records/{ien}             → GetEntity
GET    /sessions/current/access/{file}              → CheckAccess
```

### 10.3 Authentication

All connections must authenticate. The wrapper supports:

- **mTLS** (mutual TLS) for service-to-service gRPC connections using X.509 certificates
- **Bearer tokens** (JWT, signed HS256 or RS256) for REST API access
- **Kernel signon** (access/verify code pair) for connections requiring VistA user identity (required when `DUZ` must map to a specific NEW PERSON entry)

---

## 11. Security Model Specification

### 11.1 FileMan Security at the Wrapper Boundary

The wrapper must preserve, not bypass, all FileMan security mechanisms:

| FileMan Mechanism | Wrapper Responsibility |
|---|---|
| File-level access codes (RD/WR/DL/LA) | Established by `DUZ(0)` at session creation; wrapper must not override |
| Field-level security codes | Enforced by FileMan DBS calls; wrapper surfaces `AccessDeniedError` |
| `DUZ(0)="@"` programmer access | Must not be available to non-DBA sessions; session creation API must reject this unless the calling identity has the DBA role |
| DAC policy evaluation | Wrapper exposes `EvaluatePolicy` operation; application code is responsible for calling it before sensitive operations |
| Kernel security keys | Checked by FileMan for utility operations (XUAUDITING, XUPROGMODE, etc.); wrapper surfaces `AccessDeniedError` on key check failures |

### 11.2 Wrapper-Layer Security Additions

Beyond FileMan's own security model, the wrapper must add:

- **Operation-level authorization:** The wrapper service may define additional access control policies (beyond FileMan's own) at the gRPC method level, enforced before the call reaches the YottaDB layer
- **Rate limiting:** Per-session rate limits on read and write operations to prevent denial-of-service against the VistA instance
- **Input validation:** All input must be validated against expected formats (file number patterns, IEN format, field number format) before being passed to FileMan to prevent injection attacks
- **Audit logging at the transport layer:** Every API call must be logged with session ID, operation, file, IEN, and timestamp — independent of FileMan's own audit system

### 11.3 Prohibition on Bypass

The wrapper must not provide any mechanism to read or write MUMPS globals directly, to execute arbitrary M code on the server (except for carefully scoped administrative operations requiring explicit DBA authentication), or to bypass the FileMan DBS API for any data access operation. The `DUZ(0)="@"` programmer access level must be unavailable to automated application sessions.

---

## 12. Concurrency and Transaction Specification

### 12.1 FileMan Concurrency Model

FileMan does not provide ACID transactions in the modern sense. Its concurrency model is:

- **Optimistic by default:** No locking occurs on reads. Writes use YottaDB's MUMPS `SET` command, which is atomic at the global node level
- **Explicit locking via `LOCK^DILF`:** Applications requiring multi-step atomicity must explicitly acquire and release MUMPS LOCKs around the critical section
- **Cross-reference triggers are synchronous:** When `FILE^DIE` sets a field, all cross-reference SET/KILL logic executes synchronously before the call returns. This provides write consistency within a single `FILE^DIE` call

### 12.2 Wrapper Transaction Semantics

The wrapper must document the following semantics clearly:

- **Single-entry writes (`File` / `Update`)** are atomic at the FileMan level — either all specified fields for a given entry are set, or none are (on validation failure)
- **Multi-entry `BatchFile`** calls are NOT transactional across entries. If the third entry in a batch fails validation, entries 1 and 2 may already have been filed. The `BatchResult` object reports the status of each entry individually
- **Lock acquire before multi-step operations:** The `Lock` operation must be called before any read-modify-write sequence to prevent lost updates
- **Lock timeouts:** Locks must always have a timeout (default: 30 seconds). The wrapper must release locks when a session ends, even abnormally

### 12.3 Session Isolation

Each wrapper session operates with its own `DUZ` context. Multiple concurrent sessions can read and write the same FileMan files. The wrapper does not provide inter-session isolation beyond what FileMan's LOCK mechanism provides. Applications requiring serialized updates to shared records must acquire explicit locks.

---

## 13. Strategic Implementation Roadmap

The following phased approach is recommended for implementing the FileMan API Wrapper. The phases are ordered to deliver usable capability early while building toward full API coverage.

### Phase 0: Foundation (Weeks 1–4)

**Objective:** Establish the server-side infrastructure and the basic read path.

**Deliverables:**
1. YottaDB call-in integration: a Go process that can successfully call `GETS^DIQ` and return results
2. Session management: `CreateSession` / `DestroySession` with DUZ initialization
3. `GetEntry` operation (single file, no multiples, external values only)
4. `GetField` operation
5. Error handling: DIERR array parsing and typed error hierarchy
6. Date conversion utilities: FileMan ↔ ISO 8601
7. Unit test harness with a fake YottaDB backend

**Validation:** Can retrieve a patient name from the PATIENT file (#2) via a Go test client.

---

### Phase 1: Core CRUD (Weeks 5–10)

**Objective:** Complete the DBS read/write surface for single-file, flat-record operations.

**Deliverables:**
1. `Find` and `FindOne` operations
2. `ListEntries` operation with pagination
3. `File` (create) operation with new-IEN return
4. `Update` (modify) operation with audit
5. `ValidateField` and `ValidateEntry` operations
6. `Lock` / `Unlock` operations
7. Python SDK (generated from `.proto` + idiomatic wrapper layer)
8. Go SDK

**Validation:** Can create a new entry in a test FileMan file, retrieve it, update a field, validate the update, and confirm audit trail — using both Python and Go clients.

---

### Phase 2: Schema Introspection and Type System (Weeks 11–16)

**Objective:** Full schema introspection, type-aware field handling, and code generation.

**Deliverables:**
1. `GetFileDef`, `GetFieldDef`, `ListFiles` operations
2. Full data type mapping for all FileMan data types (§8)
3. POINTER field resolution (both internal IEN and external display value)
4. SET OF CODES field handling
5. WORD-PROCESSING field read/write
6. MULTIPLE (sub-file) read/write — `GETS^DIQ` with `"**"` and sub-file FDA writes
7. Schema-driven code generator: reads `^DD` via the wrapper and generates typed file/field classes in Python, Go, Rust, TypeScript
8. Rust SDK
9. TypeScript/JavaScript SDK

**Validation:** Generated typed classes for PATIENT (#2) and DRUG (#50) files pass round-trip create/read/update tests.

---

### Phase 3: Advanced Operations (Weeks 17–24)

**Objective:** Cover audit, security, DDE, statistics, import/export, and administrative operations.

**Deliverables:**
1. `GetAuditHistory` and `SetAudit` operations
2. `CreateSession` with full Kernel access/verify code authentication
3. `CheckAccess` and `EvaluatePolicy` (DAC) operations
4. `GetEntity`, `GetEntities`, `ListEntities` (DDE API)
5. `ExportForeignFormat` and `ImportFromTemplate`
6. `ComputeStatistics`
7. `ExportFilegram` and `ImportFilegram`
8. `GetGlobalRoot`, `GetSQLISchema`
9. `Delete` operation (two-step DIK sequence)
10. REST/JSON gateway over gRPC (OpenAPI 3.1)

**Validation:** Full integration test suite against FOIA VistA covering all implemented operations.

---

### Phase 4: Hardening and Production Readiness (Weeks 25–32)

**Objective:** Production-ready service with observability, rate limiting, and documentation.

**Deliverables:**
1. mTLS for gRPC, JWT for REST
2. Rate limiting per session and per operation type
3. Prometheus metrics (request rate, latency, error rate, lock contention)
4. Distributed tracing (OpenTelemetry)
5. Structured logging (JSON, correlated with trace IDs)
6. OpenAPI 3.1 specification published with complete documentation
7. SDK documentation and worked examples for all four languages
8. Performance benchmarks: `GetEntry` and `Find` at 1,000 req/s target
9. RPC Broker adapter (Phase 0–3 delivered YottaDB embedded only; this adds the remote path)

---

### Phase 5: Ecosystem and Developer Experience (Weeks 33–48)

**Objective:** Transform the wrapper into a developer platform.

**Deliverables:**
1. Interactive API explorer (Swagger UI / gRPC reflection)
2. Schema browser: web UI for exploring the FileMan Data Dictionary via the wrapper
3. FileMan Query Language (FMQL-inspired) query interface for ad-hoc data exploration
4. Data model catalog: all entities, files, and cross-reference relationships in a searchable index
5. Migration guides: patterns for rewriting common MUMPS DBS call patterns in Python, Go, Rust, TypeScript
6. CI/CD pipeline: automated integration tests against FOIA VistA on every commit

---

## 14. Language-Specific SDK Design Guidelines

### 14.1 Common SDK Principles

All language SDKs share these design obligations:

- **Two-tier design:** A low-level transport client (thin gRPC stub wrapper) and a high-level typed client (ergonomic, idiomatic API). Application code should use only the high-level client.
- **Connection management:** The high-level client manages connection lifecycle (creation, pooling, session refresh) transparently. Application code should not manage connections directly.
- **Type fidelity:** All FileMan dates must be language-native date types. All FileMan `POINTER` fields must be `Reference` objects containing both IEN and display name. Never return raw MUMPS-encoded values.
- **Async support:** All I/O operations must be available in both synchronous and asynchronous forms.
- **Error hierarchy:** Typed exceptions/errors matching §9.2, never raw strings.

### 14.2 Python SDK

- Idiomatic client: `FileManClient` class with methods matching the operation names in §7
- Type annotations throughout: `mypy`-compatible, `py.typed` marker present
- `async`/`await` support via `asyncio` (the async client is the primary implementation; the sync client wraps it)
- FileMan date fields map to `datetime.date` / `datetime.datetime`
- POINTER fields map to a `FileManRef` dataclass with `.ien`, `.file`, `.display` attributes
- `Entry` objects support dict-like access (`entry["PATIENT NAME"]` by field label) in addition to field-number access
- Installable via PyPI: `pip install fileman-client`

### 14.3 Go SDK

- Idiomatic client: `Client` struct with methods using standard Go error returns
- Context propagation: all methods accept `context.Context` as the first argument
- Strong typing: generated structs per file (via the §13.2 code generator) implement a common `FileManRecord` interface
- FileMan dates map to `time.Time`; the SDK handles all FileMan date encoding internally
- Published as a Go module: `go get github.com/va-fileman/fileman-go`

### 14.4 Rust SDK

- Idiomatic client: `FileManClient` struct with async methods using Tokio
- Error handling via `Result<T, FileManError>` — never panics
- Zero-copy deserialization where possible using `serde`
- FileMan dates map to `chrono::NaiveDate` / `chrono::DateTime<Utc>`
- Strong typing: generated structs per file implement `serde::Serialize` / `serde::Deserialize`
- Published as a crate: `cargo add fileman-client`

### 14.5 JavaScript / TypeScript SDK

- TypeScript-first: full `.d.ts` definitions; the JavaScript distribution is a compiled output
- Promise-based API throughout; `async`/`await` compatible
- FileMan dates map to ISO 8601 strings (TypeScript has no native Date-without-time type)
- Generated types per file: TypeScript interfaces with all field names as string literal union types
- Node.js and browser builds (browser build excludes YottaDB call-in transport)
- Published to npm: `npm install @va-fileman/client`

---

## 15. Governance and Compatibility Obligations

### 15.1 ICR / DBIA Compliance

Any deployment of the FileMan API Wrapper within a VA-governed VistA instance must comply with the VA's Integration Control Registration (ICR) process. The key applicable ICR is:

- **DBIA #10012** — Covers programmatic use of the DBS API entry points (`FILE^DIE`, `GETS^DIQ`, `FIND^DIC`, etc.) by any package. The wrapper, as a caller of these entry points, must be registered under this ICR or an appropriate descendant.

Deployments outside the VA governance process (open-source VistA, WorldVistA, OSEHRA VistA) are not subject to ICR requirements but should follow the same design discipline.

### 15.2 Backward Compatibility Policy

The FileMan API Wrapper must maintain backward compatibility at two levels:

1. **FileMan compatibility:** The wrapper must remain compatible with all FileMan 22.x versions. It must not use any entry point or global structure not documented in the official FileMan documentation.
2. **SDK API stability:** Once a version of the SDK is released, its public API must not change in a breaking way without a major version increment (following Semantic Versioning). The gRPC service API must follow Protocol Buffers backward-compatibility rules (add fields only, never remove or renumber).

### 15.3 FileMan Patch Tracking

The VA releases patches to FileMan 22.2 as named KIDS builds (`DI*22.2*N`). The wrapper maintainers must review each patch's release notes for changes to DBS API behavior, new entry points, and changed calling conventions. The wrapper version notes must document which FileMan patch level each version was tested against.

---

## 16. References

### Primary Source: VA FileMan Documentation — Local Processed Markdown

All FileMan-specific technical claims in this specification are sourced from the VA FileMan 22.2 documentation set as ingested, converted, and stored in the local pipeline data directory. These files contain VDL-sourced content converted to Markdown with YAML frontmatter by the vista-docs ingest pipeline. Use these local files as the authoritative reference — they eliminate the need to re-download and re-analyze from the VDL website.

| Local File | Content | Word Count |
|---|---|---|
| `~/data/vista-docs/publish/infrastructure/di--fileman/developer-guide.md` | FM 22.2 Developer's Guide (Rev 1.14, July 2025) — full DBS API, Classic API, ScreenMan, DDE, DILF, DDMOD, cross-references, templates, security | 192,021 words |
| `~/data/vista-docs/publish/infrastructure/di--fileman/technical-manual.md` | FM 22.2 Technical Manual — global structure, MUMPS OS file, KIDS installation, Caché/IRIS system assumptions | ~25,000 words |
| `~/data/vista-docs/publish/infrastructure/di--fileman/user-manual--fm-22-2.md` | FM 22.2 User Manual (Vol 1) — interactive operations, data entry, lookup, templates | ~35,000 words |
| `~/data/vista-docs/publish/infrastructure/di--fileman/user-manual--fm-22-2-advanced.md` | FM 22.2 Advanced User Manual (Vol 2) — auditing, archiving, statistics, import/export, Filegrams | ~30,000 words |
| `~/data/vista-docs/publish/infrastructure/di--fileman/user-manual--fm-22-2-data-access-control-dac-user-guide.md` | FM 22.2 DAC User Guide (DI*22.2*8) — POLICY file, APPLICATION ACTION file, `$$CANDO^DIAC1` | ~10,000 words |
| `~/data/vista-docs/publish/infrastructure/di--fileman/supplement--fm-key-and-index-tutorial.md` | FM Key and Index Tutorial — new-style cross-references, compound indexes, uniqueness keys | tutorial |
| `~/data/vista-docs/publish/infrastructure/di--fileman/supplement--fm-screenman-tutorial-for-developers.md` | FM ScreenMan Tutorial — FORM/BLOCK files, `^DDS`, form editor | tutorial |
| `~/data/vista-docs/publish/infrastructure/di--fileman/supplement--va-fileman-dde-utility-tutorial.md` | FM DDE Utility Tutorial — ENTITY file, `GET^DDE`, `$$GET1^DDE`, JSON/XML output | tutorial |
| `~/data/vista-docs/publish/infrastructure/xwb--remote-procedure-call-rpc-broker/supplement.md` | M-to-M Broker XWB*1.1*34 — RPC Broker wire protocol, TCP listener, REMOTE PROCEDURE #8994, M-to-M architecture | 12,090 words |
| `~/data/vista-docs/publish/infrastructure/xobv--vistalink/developer-guide.md` | VistALink 1.6 Developer Guide — J2EE Connector Architecture, RPC calls from Java, connection pooling | full guide |

**Specific sections cited in this specification:**

| Claim | Local File | Section / Keyword |
|---|---|---|
| DBS API design intent: separation of data access from I/O | `developer-guide.md` | §"Database Server (DBS) API" line 6663 |
| IENS format and placeholder codes | `developer-guide.md` | §"IENS: Identify Entries and Subentries" line 6709 |
| FDA format and WORD-PROCESSING fields | `developer-guide.md` | §"FDA: Format of Data Passed to and from VA FileMan" line 6735 |
| FileMan requires Caché/IRIS in VA production KIDS install | `technical-manual.md` | §KIDS distribution, line ~4167 |
| InterSystems SDA as DDE consumer | `technical-manual.md` | line ~702 |
| RPC Broker is a bridge between workstation and M server | `xwb--rpc-broker/supplement.md` | line 266 |
| M-to-M Broker uses XML wrapping and TCP/IP | `xwb--rpc-broker/supplement.md` | line 335 |
| VistALink is a J2CA 1.5 resource adapter for Java ↔ M | `xobv--vistalink/developer-guide.md` | line 403 |
| DDE ENTITY (#1.5) file maps VistA data to SDA/FHIR | `developer-guide.md` | §"Entity Mapping API" line ~20031 |

### VistA Source and Related Wrapper Projects

| Resource | Link |
|---|---|
| VistA Source Code (OSEHRA GitHub) | [https://github.com/OSEHRA/VistA](https://github.com/OSEHRA/VistA) |
| FMQL — FileMan Query Language | [https://github.com/caregraf/FMQL](https://github.com/caregraf/FMQL) |
| FMQL — AMIA 2012 Paper | [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540540/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540540/) |
| nodeVISTA / MVDM (OSEHRA) | [https://github.com/vistadataproject/nodeVISTA](https://github.com/vistadataproject/nodeVISTA) |
| VistA Data Project (VDM) | [https://github.com/vistadataproject/VDM](https://github.com/vistadataproject/VDM) |
| VA Lighthouse Developer Portal | [https://developer.va.gov/](https://developer.va.gov/) |
| nodem — YottaDB/GT.M Node.js interface | [https://github.com/dlwicksell/nodem](https://github.com/dlwicksell/nodem) |

### M Runtimes

| Resource | Link |
|---|---|
| YottaDB Documentation Home | [https://docs.yottadb.com/](https://docs.yottadb.com/) |
| YottaDB Call-In Interface | [https://docs.yottadb.com/ProgrammersGuide/externalroutines.html](https://docs.yottadb.com/ProgrammersGuide/externalroutines.html) |
| YottaDB Go Wrapper | [https://pkg.go.dev/lang.yottadb.com/go/yottadb](https://pkg.go.dev/lang.yottadb.com/go/yottadb) |
| YottaDB Python Wrapper | [https://pypi.org/project/yottadb/](https://pypi.org/project/yottadb/) |
| InterSystems IRIS Python (intersystems-irispython) | [https://pypi.org/project/intersystems-irispython/](https://pypi.org/project/intersystems-irispython/) |
| InterSystems IRIS C Binding reference | [https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=BXCI_ref](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=BXCI_ref) |
| InterSystems IRIS REST documentation | [https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GREST](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GREST) |

### Architecture Patterns and Methods

| Reference | Link |
|---|---|
| Evans, E. — *Domain-Driven Design* (2003) — Anti-Corruption Layer | [https://www.domainlanguage.com/ddd/](https://www.domainlanguage.com/ddd/) |
| Fowler, M. — *Patterns of Enterprise Application Architecture* (2002) | [https://martinfowler.com/books/eaa.html](https://martinfowler.com/books/eaa.html) |
| Fowler, M. — Strangler Fig Application Pattern (2004) | [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html) |
| Google API Design Guide | [https://cloud.google.com/apis/design](https://cloud.google.com/apis/design) |
| gRPC documentation | [https://grpc.io/docs/](https://grpc.io/docs/) |
| Protocol Buffers Language Guide (proto3) | [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/) |
| OpenAPI 3.1 Specification | [https://spec.openapis.org/oas/v3.1.0](https://spec.openapis.org/oas/v3.1.0) |

### Analog Systems

| System | Reference |
|---|---|
| SAP BAPI / RFC — Python client (pyrfc) | [https://github.com/SAP/PyRFC](https://github.com/SAP/PyRFC) |
| SAP BAPI / RFC — Go client (gorfc) | [https://github.com/SAP/gorfc](https://github.com/SAP/gorfc) |
| IBM z/OS Connect EE documentation | [https://www.ibm.com/docs/en/zosconnect/3.0](https://www.ibm.com/docs/en/zosconnect/3.0) |
| Oracle REST Data Services (ORDS) | [https://www.oracle.com/database/technologies/appdev/rest.html](https://www.oracle.com/database/technologies/appdev/rest.html) |
| Google Cloud client libraries (language SDK layer) | [https://cloud.google.com/apis/docs/client-libraries-explained](https://cloud.google.com/apis/docs/client-libraries-explained) |
| Oracle Cloud Infrastructure SDK pattern | [https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm) |

---

## 17. API Priority Classification: Essential vs. Background

One of the most consequential design decisions for the FileMan wrapper is which APIs to implement first and with what depth. Treating all 30+ FileMan entry points as equally important leads to a specification that is hard to prioritize, hard to test, and hard to deliver incrementally.

This section classifies every FileMan API surface into three tiers based on its necessity for a **non-M application that reads and writes VistA data**. The DBS API Developer's Guide defines the DBS API explicitly as the mechanism enabling "the construction of alternative front-ends to the VA FileMan database" and "data access by applications running outside M" (`developer-guide.md`, line 6667). That design intent drives this classification.

---

### Tier 1 — Essential: Must Wrap for Any Read/Write Application

These are the operations without which a non-M application cannot function. They are the operational minimum. An application can be built, deployed, and used with only these operations — nothing else is required.

| FileMan Entry Point | Wrapper Operation | Why Essential |
|---|---|---|
| `GETS^DIQ` | `GetEntry` | The only way to retrieve multiple fields from an entry. Every read-oriented application needs this. |
| `$$GET1^DIQ` | `GetField` | Single-field retrieval; needed for lightweight lookups and pointer resolution. |
| `$$FIND1^DIC` | `FindOne` | The primary lookup path: find an entry IEN by name or cross-reference value. Virtually every application starts here. |
| `FIND^DIC` | `Find` | Multi-entry search; required for any list or grid view. |
| `FILE^DIE` | `File` | The only way to create new entries or update existing ones without audit overhead. Required for all writes. |
| `UPDATE^DIE` | `Update` | Write path with audit logging and key enforcement; required for all production writes where traceability matters. |
| `CHK^DIE` | `ValidateField` | Validate a value against a field's INPUT transform before filing; required for any form validation flow. |
| `FIELD^DID` | `GetFieldDef` | Retrieve field type, label, pointer target; required for dynamic UI generation and type-safe mapping. |
| `FILE^DID` | `GetFileDef` | Retrieve file name, global root, security codes; required for schema discovery. |
| `LOCK^DILF` / `UNLOCK^DILF` | `Lock` / `Unlock` | Required for any read-modify-write operation to prevent lost updates. |
| `%DT` / `$$DT^XLFDT` | `DateConvert` / `FMNow` | Required for all date field handling; FileMan dates are not standard and cannot be naively passed or stored. |
| `DUZ` / `DUZ(0)` setup | `CreateSession` | Required to establish the security context before any FileMan call. Without this, FileMan has no user identity and cannot enforce access codes. |
| DIERR array parsing | `FileManError` hierarchy | Required to surface meaningful errors to application code. Raw DIERR codes are opaque without translation. |

**Implementation note:** The FileMan Developer's Guide states that `DUZ` and `DT` (today's date) are *not* passed in DBS call parameter lists but are expected to be defined in the local symbol table (line 6688). The wrapper must set these in the M process context before every call — they are session-scoped prerequisites, not per-call parameters.

---

### Tier 2 — Important: Required for Production Completeness

These operations are needed for a production deployment but are not required for the wrapper to be functional in development or for initial application code. Implement these in Phase 2–3.

| FileMan Entry Point | Wrapper Operation | Why Important (But Not Tier 1) |
|---|---|---|
| `LIST^DIC` | `ListEntries` | Sorted range browsing; useful for autocomplete and list views, but `FIND^DIC` covers most query needs. |
| `VALS^DIE` | `ValidateEntry` | Multi-field validation; important for form submission but `CHK^DIE` covers field-by-field validation. |
| `UPDATE^DIE` with `"T"` flag | `TestFile` | Dry-run without actual write; important for pre-flight validation of bulk operations. |
| `GETS^DIQ` with `"**"` (all multiples) | `GetEntryWithMultiples` | Sub-file traversal; essential for files with complex nested records (ORDER #100, LAB DATA #63). |
| Sub-file FDA writes | `FileSubEntry` | Required once any application needs to write to multiple-valued fields. |
| `TURNED^DIAUTL` / `CHANGED^DIAUTL` | `GetAuditHistory` | Required for any compliance or change-tracking feature. |
| `$$CANDO^DIAC1` | `EvaluatePolicy` | Required when the target system uses DAC policies (DI*22.2*8 or later). |
| `CREIXN^DDMOD` | `CreateCrossReference` | Required for DBA-level tooling; not required for application reads/writes. |
| `$$ROOT^DILFD` | `GetGlobalRoot` | Required for low-level debugging and for tools that need to inspect global structure. |
| `FILE^DICN` | `AddEntry` | Convenience wrapper for new-entry creation; `FILE^DIE` with `"+1,"` IENS covers the same need. |

---

### Tier 3 — Background: Read-Only, Analytical, or Legacy Context Only

These APIs are documented here for completeness and background understanding. They are **not required** for a non-M read/write application. Wrapping them is optional and low-priority. For teams building production applications, time is better spent on Tier 1 and 2 hardening than on implementing Tier 3.

| FileMan API | Category | Why Background Only |
|---|---|---|
| **SQLI Projection Layer** (`^DMSQ`) | Read-only analytics | Projects FileMan as SQL tables for ODBC reporting tools. Useful for data analysts and BI tools but not for application CRUD. A non-M application that needs SQL access should use SQLI directly via ODBC, not through the wrapper. |
| **DDE / Entity API** (`GET^DDE`, `$$GET1^DDE`) | Read-only, FHIR/SDA | Retrieves pre-defined entity mappings as JSON/XML. Primarily used by VPR and FHIR pipelines. A general-purpose wrapper does not need to re-implement this; the VistA FHIR Adaptor or the VA Lighthouse API already exposes it. |
| **FMQL REST Service** | Read-only graph query | FMQL is a separate running service, not a FileMan API call. A wrapper that calls the gRPC service does not interact with FMQL. FMQL is background context for understanding how others have read FileMan data. |
| **Classic API — interactive** (`^DIC`, `^DIE`, `^DIP`, `^DIS`) | Terminal I/O, not wrappable | These write to the current M device (terminal). They cannot be called from a non-M process without a VT100 terminal. Background understanding only — never wrap these. |
| **ScreenMan** (`^DDS`, `^DDGF`) | Terminal forms UI, not wrappable | VT100 full-screen forms. Inherently interactive. Background understanding of how VistA data-entry worked historically. |
| **WORD-PROCESSING field editor** (`^DIWE`) | Terminal editor | VT100 screen editor for WP fields. Not wrappable. Read and write WP field content via `GETS^DIQ` / `FILE^DIE` instead. |
| **DIFROM** | M-to-M package export | Bundles M routines and data for inter-site distribution. Has no external application use case. |
| **Statistical utilities** (`EN^DISTAT`) | Batch analytics | FileMan's built-in histogram/scattergram. Useful for DBA analytics but superseded by SQL analytics tools for external applications. Low implementation priority. |
| **Filegrams** (`^DIFG`) | Inter-site data transfer | MailMan-based serialization for inter-VistA transfer. Relevant only for sites doing direct VistA-to-VistA data migrations. |
| **Archiving utilities** | DBA operations | Moves entries to offline storage. DBA function, not an application API. |
| **Import templates / Foreign formats** | Batch data loading | Useful for one-time data migration projects. Not needed for ongoing read/write application development. |
| **DD Audit** (`^DDA`, file #0.6) | Schema change history | Tracks data dictionary modifications. Rarely needed by application developers; more relevant to DBA tooling. |

**Key principle from the FileMan documentation:** The Developer's Guide explicitly describes the DBS API as the mechanism that enables non-interactive, non-M application access (line 6667). Every other FileMan API layer was designed for different purposes — terminal interaction, batch reporting, DBA administration, inter-site transfer — that do not apply to the core application-development use case this wrapper serves.

---

## 18. Wrapper Ecosystem Integration: RPC Broker, VistALink, MVDM, and FMQL

The FileMan gRPC wrapper does not exist in isolation. Every production VistA system already runs several services that mediate access to FileMan data. This section specifies precisely how the new wrapper relates to each existing service: whether it replaces, complements, depends on, or is independent of each one.

---

### 18.1 VistA RPC Broker (XWB)

**What it is:** The RPC Broker (package XWB) is a TCP socket server (`XWBTCPL` listener, port 9200) that dispatches named Remote Procedure Calls registered in the REMOTE PROCEDURE (#8994) file. As documented in the local XWB M-to-M supplement: *"It establishes a common and consistent foundation for Client/Server applications"* and *"enables client applications to communicate and exchange data with M Servers"* (xwb supplement, line 264). It is the transport layer currently used by CPRS, JLV, and every other GUI VistA client.

**Relationship to the new wrapper:** The new gRPC wrapper is a **replacement transport** for the RPC Broker on the client-application side, not a consumer of it. The two coexist on the same VistA system:

```
CPRS / JLV / legacy GUI clients
        │ RPC Broker wire protocol (TCP 9200)
        ▼
XWB Broker listener (XWBTCPL)
        │ M DO/$$
        ▼
VistA MUMPS routines

New Python/Go/Rust/JS applications
        │ gRPC (Protocol Buffers / mTLS)
        ▼
FileMan gRPC Gateway (Go process)
        │ YottaDB call-in / IRIS C binding
        ▼
FileMan DBS API (same M routines)
```

The two paths converge at the FileMan DBS layer — both the RPC Broker and the gRPC gateway ultimately call `FILE^DIE`, `GETS^DIQ`, `FIND^DIC`, etc. The difference is the transport and the API contract exposed to the client.

**Why not just use the RPC Broker?** The RPC Broker requires every new operation to be registered as a named RPC in MUMPS (#8994 file), reviewed, approved through the ICR process, and deployed as a KIDS patch. This governance overhead is appropriate for the VA's production environment but creates a weeks-to-months latency for each new API capability. The gRPC wrapper encodes the full DBS API surface in a single `.proto` file and requires no MUMPS changes per new operation. For development and open-source VistA deployments, the gRPC wrapper is dramatically faster to iterate.

**Interoperability scenario:** For deployments where the gRPC Gateway uses the RPC Broker Adapter (§6.2 rather than §6.1), the wrapper becomes a **consumer** of the RPC Broker rather than a replacement. In this configuration, the gRPC gateway translates incoming gRPC calls into XWB wire protocol requests to the existing broker listener. This path requires registering a small set of generic FileMan DBS wrapper RPCs in #8994 — one per DBS entry point category — rather than one per business operation.

---

### 18.2 VistALink (XOBV)

**What it is:** VistALink (package XOBV, version 1.6) is the VA's J2EE resource adapter for Java applications. As the local VistALink Developer's Guide states: *"VistALink 1.6 is a transport layer that provides communication between Health eVet Java applications and VistA/Mumps (M) servers... It allows Remote Procedure Calls (RPCs) to execute on the VistA/M system and return results to the Java enterprise system"* (xobv developer-guide, line 401). VistALink implements the J2EE Connector Architecture (J2CA 1.5) specification.

**Relationship to the new wrapper:** VistALink is the **Java-specific predecessor** of what the gRPC wrapper generalizes. VistALink only serves Java J2EE applications running on WebLogic. The gRPC wrapper serves Python, Go, Rust, TypeScript, and Java — in any runtime environment, not just J2EE. For Java applications, the gRPC wrapper replaces VistALink.

**API model comparison:**

| Aspect | VistALink | gRPC Wrapper |
|---|---|---|
| Transport | J2CA 1.5 connector over XWB wire protocol | gRPC over TLS |
| Languages supported | Java (J2EE / WebLogic only) | Python, Go, Rust, TypeScript, Java, any gRPC client |
| Operation model | Named RPCs registered in #8994 | Full DBS API surface in `.proto` |
| Schema exposure | None — callers must know RPC names | `.proto` file + introspection API |
| Authentication | Kernel access/verify codes via XUS SIGNON RPC | mTLS + Kernel signon |
| Async support | J2EE work managers | Native gRPC streaming |
| Active development | No (last release 2020) | Yes |

**Migration path:** A Java application using VistALink can migrate to the gRPC wrapper's Java SDK without changing its data model or business logic. Only the connection initialization and RPC call syntax changes. The wrapper's Java SDK exposes the same logical operations (GetEntry, File, Find) with idiomatic Java types.

---

### 18.3 nodeVISTA / MVDM

**What it is:** The Master VistA Data Model (MVDM) project, developed under the OSEHRA nodeVISTA initiative, is a Node.js service that runs co-located with YottaDB and wraps VistA data as JSON domain objects. MVDM was the most semantically ambitious VistA wrapper project to date — it defined a complete data model mapping FileMan files to domain objects (Patient, Medication, Problem, etc.) and exposed these via a REST/JSON API.

**Relationship to the new wrapper:** MVDM and the gRPC wrapper are **complementary but independent**. They address different layers of the wrapping problem:

| Layer | MVDM | gRPC Wrapper |
|---|---|---|
| Transport | HTTP/JSON REST | gRPC + optional REST |
| API grain | Domain objects (Patient, Medication) | Raw FileMan files and fields |
| Schema | Hard-coded domain model | Live Data Dictionary from `^DD` |
| Write support | Yes (limited) | Full DBS API |
| Languages | Node.js only | Python, Go, Rust, TypeScript, Java |
| Status | Discontinued (~2020) | New (this specification) |

The gRPC wrapper operates at the **FileMan level** — it exposes files, fields, IENs, and DBS operations. MVDM operated at the **domain object level** — it knew that file #2 was a Patient and that field .03 was a date of birth. The gRPC wrapper does not encode domain knowledge; that belongs in application code or in a domain layer built on top of the wrapper's SDK.

**Coexistence:** A VistA system can run both MVDM (if still in use) and the gRPC wrapper simultaneously. Both call the same underlying FileMan DBS API. The gRPC wrapper does not interfere with MVDM's operation.

**Migration path for MVDM users:** Applications using MVDM's REST API can migrate to the gRPC wrapper by replacing MVDM's domain-object calls with wrapper calls to the underlying FileMan files that MVDM was reading. The gRPC wrapper's schema introspection API (`GetFileDef`, `GetFieldDef`) enables the same runtime field discovery that MVDM performed during its initialization.

---

### 18.4 FMQL (FileMan Query Language)

**What it is:** FMQL is an HTTP/JSON service (implemented in Python/M) that exposes FileMan data through a graph-oriented query language modeled loosely on SPARQL. FMQL treats FileMan's pointer relationships as a navigable graph — a query like `DESCRIBE 2-9` returns the full record for PATIENT IEN 9 with all pointer values resolved and all multiples expanded. FMQL is **read-only** — it has no write capability.

**Relationship to the new wrapper:** FMQL is a **read-only predecessor** that the gRPC wrapper supersedes for new development. The key differences:

| Aspect | FMQL | gRPC Wrapper |
|---|---|---|
| Write support | None | Full (FILE^DIE, UPDATE^DIE) |
| Query model | Graph traversal | Indexed lookup + field retrieval |
| Schema access | Full — generates schema from `^DD` at startup | Full — live `^DD` introspection per call |
| Languages | HTTP client in any language | Typed SDK in 4 languages |
| Pointer resolution | Automatic, graph-style | Explicit, via `"E"` flag in `GETS^DIQ` |
| Active development | No | Yes |
| Transport | HTTP/REST | gRPC + optional REST |

**What FMQL does better:** FMQL's graph traversal model is genuinely superior for **exploratory data access** — navigating from a patient record through all its related files, following pointers automatically without knowing the target file numbers in advance. The gRPC wrapper does not replicate this pattern; callers must know which file and field they are querying. For data discovery and schema exploration, FMQL's approach remains a useful reference.

**What the gRPC wrapper does that FMQL cannot:** Write operations. Any application that needs to create or update VistA records cannot use FMQL. The gRPC wrapper is the first comprehensive read/write wrapper with typed language SDKs.

**Coexistence:** FMQL and the gRPC wrapper can run on the same VistA system without interference. A migration from FMQL to the gRPC wrapper requires replacing FMQL's DESCRIBE queries with `GetEntry` calls and its SELECT queries with `Find` + `GetEntry` sequences.

---

### 18.5 Summary: Relationship Map

```
                    VistA M Runtime (YottaDB or IRIS)
                              │
                    FileMan DBS API (GETS^DIQ, FILE^DIE, ...)
                    ┌─────────┼──────────┬──────────┬────────┐
                    │         │          │          │        │
              XWB Broker   gRPC        FMQL      MVDM    VistALink
              (TCP 9200)   Gateway    (HTTP)    (Node)    (J2CA)
                    │         │          │          │        │
              CPRS/JLV   Python      Any HTTP   Node.js   Java
              Delphi GUI    Go        client    apps      J2EE
                          Rust
                          TypeScript

Legend:
  XWB Broker  — production CPRS transport; keep running; wrapper coexists
  gRPC Gateway — new general-purpose read/write wrapper (this spec)
  FMQL        — read-only graph query; superseded for new development
  MVDM        — domain-object REST; discontinued; migrate to gRPC wrapper
  VistALink   — Java J2EE connector; superseded by gRPC Java SDK
```

---

## 19. Rationale: Why gRPC + Protocol Buffers as the Two-Layer Foundation

This section documents the reasoning behind the two-layer design in detail — both why gRPC was chosen over alternatives for the wire layer and why a separate language SDK layer above it is necessary rather than simply distributing raw gRPC stubs.

### 19.1 Why a Two-Layer Design at All

The naive alternative to a two-layer design is to expose the FileMan DBS API directly through the M runtime via a language-native binding (YottaDB Python package, YottaDB Go package, etc.) and let application developers call `GETS^DIQ` and `FILE^DIE` directly. This approach has several fatal problems:

**Problem 1: Language proliferation.** YottaDB has a Python wrapper and a Go wrapper. It has no Rust wrapper and no browser-compatible JavaScript wrapper. Any language without a YottaDB binding gets no access. The two-layer design solves this: the gRPC server (written once) serves all languages via generated stubs.

**Problem 2: Deployment coupling.** A language-native binding requires the application process to run on the same host as YottaDB, with the same OS, with `YOTTADB` and `gtmroutines` set correctly. This locks applications to the VistA server. The gRPC layer decouples client deployment from server deployment — Python applications can run in Kubernetes pods, Rust services can run in AWS Lambda, TypeScript frontends can run in a browser (via gRPC-Web).

**Problem 3: No typed contract.** Neither YottaDB's Python package nor its Go package defines any type contract for FileMan data. A caller passing the wrong file number, an integer IEN where a string is expected, or a raw MUMPS date string where an ISO date is expected will get a confusing M runtime error. The `.proto` file defines the complete type contract in a machine-verifiable form.

**Problem 4: M runtime knowledge required.** Calling `GETS^DIQ` from Python via YottaDB requires understanding IENS strings, FDA arrays, M global indirection, the `DIERR` array, and FileMan date encoding. These are opaque to non-M developers. The language SDK layer translates all of this into idiomatic types and methods.

### 19.2 Why gRPC Specifically (Not REST, Not GraphQL, Not Thrift)

**vs. REST/JSON:** REST is the obvious choice for familiarity, but it has important weaknesses for this use case:

- **No streaming.** FileMan searches can return thousands of entries. HTTP/1.1 REST requires pagination with multiple round-trips. gRPC server-streaming sends results as they are produced, with a single connection setup cost.
- **No type enforcement at the wire level.** JSON has no notion of FileMan-specific types. A date field, a pointer field, and a free-text field are all JSON strings. The gRPC `.proto` file defines each operation's exact input and output types — the server rejects malformed requests before they reach M.
- **No bidirectional streaming.** Bulk write operations (filing hundreds of FDA entries) benefit from client-streaming gRPC: the client sends entries as they are ready, the server files them and streams back results. This is awkward to implement cleanly in REST.
- **Code generation for free.** `protoc` generates server stubs and client stubs in 10+ languages from the same `.proto`. REST SDKs must be written manually or generated from OpenAPI, which requires additional tooling and produces less type-safe output.

**vs. GraphQL:** GraphQL is well-suited for read-heavy graph traversal — which is exactly what FMQL already implements. The FileMan wrapper's primary value is write access (`FILE^DIE`, `UPDATE^DIE`) and typed field-level CRUD. GraphQL has no natural model for mutations that carry complex audit semantics (audit trail, key enforcement, DIERR error surface). gRPC's explicit operation model maps more cleanly to FileMan's DBS entry points.

**vs. Apache Thrift:** Thrift predates gRPC and has a smaller community. Protocol Buffers 3 has better tooling, broader language support, more active development, and is the de facto standard for new API design at Google, cloud vendors, and the CNCF ecosystem.

**The decisive advantage of gRPC for this use case:** The FileMan DBS API has a well-defined, stable set of operations with explicit input/output contracts (described formally in the FileMan Developer's Guide). This maps perfectly to gRPC's service-and-method model. Each FileMan DBS call becomes a gRPC method with a typed request message and a typed response message. The `.proto` file is both the specification and the implementation contract — it generates correct client and server stubs with no ambiguity.

### 19.3 Why a Language SDK Layer Above gRPC

Generated gRPC stubs are correct but not ergonomic in any language. They expose the protobuf type system directly — `StringValue`, `Int64Value`, repeated message fields — rather than native types. A developer calling the wrapper should not need to know what a `StringValue` is.

The language SDK layer performs five transformations that the raw gRPC stub cannot:

**1. Type translation.** FileMan dates arrive as `string` in the protobuf. The Python SDK converts them to `datetime.date`. The Go SDK converts them to `time.Time`. The Rust SDK converts them to `chrono::NaiveDate`. The application developer never sees the FileMan date string.

**2. Connection management.** The raw gRPC stub requires the caller to manage a `grpc.ClientConn` (Go), a `Channel` (Python), or a `GrpcChannel` (C#). The SDK creates, pools, and refreshes connections transparently. Application code calls `FileManClient.get_entry()`, not `FileManStub(channel).GetEntry(request)`.

**3. Session lifecycle.** The raw stub has no concept of a FileMan session (DUZ context, access/verify code). The SDK's `FileManClient` initializes a session at construction and includes the session token in every request via a gRPC interceptor. Application code never constructs or passes session tokens.

**4. Error translation.** The raw gRPC stub surfaces gRPC status codes (`INVALID_ARGUMENT`, `NOT_FOUND`, `PERMISSION_DENIED`). The SDK maps these to the typed FileMan exception hierarchy (`ValidationError`, `NotFoundError`, `AccessDeniedError`) with the specific DIERR message text as the exception message. Application code catches `ValidationError`, not `RpcError(StatusCode.INVALID_ARGUMENT)`.

**5. Idiomatic patterns.** Each language has conventions for how to express collection operations, optional values, and async I/O. The Go SDK uses `(result, error)` return patterns. The Python SDK uses `Optional[str]` for nullable fields and `asyncio` for async calls. The Rust SDK uses `Result<T, FileManError>` and `tokio` for async. The TypeScript SDK uses `Promise<T>` and TypeScript union types. None of these patterns are expressible in a protobuf-generated stub without the SDK wrapper layer.

### 19.4 The Two-Layer Contract

The two layers have a strict contract boundary:

```
Application Code
      │ calls idiomatic SDK methods with native types
      ▼
Language SDK (Python / Go / Rust / TypeScript)
      │ translates native types to protobuf messages
      │ manages connection, session, interceptors
      │ translates protobuf errors to typed exceptions
      ▼
gRPC Stub (generated from .proto)
      │ Protocol Buffers serialization over HTTP/2
      ▼
gRPC Gateway Service (Go)
      │ deserializes protobuf, validates, calls FileMan
      │ translates DIERR to gRPC status codes
      │ handles LOCK/UNLOCK lifecycle
      ▼
MRuntime (YottaDB or IRIS C binding)
      │ calls GETS^DIQ, FILE^DIE, FIND^DIC, etc.
      ▼
FileMan DBS API
```

**The `.proto` file is the only contract between Layer 1 (SDK) and Layer 2 (Gateway).** It evolves according to Protocol Buffers backward-compatibility rules. The SDK implementation is free to change as long as it correctly serializes to and deserializes from the protobuf contract. The Gateway implementation is free to change its internal M call strategy as long as it correctly handles all protobuf request types and produces correct responses.

---

## 20. Industrial Scale: Vendors Who Use This Pattern at Massive Scale

The two-layer pattern (typed wire protocol + language-specific SDK) is not a theoretical design choice. It is the de facto standard for every major cloud and enterprise API platform that modernized legacy infrastructure while leaving transactional systems intact. The following examples are all in production at scales orders of magnitude larger than any VistA deployment.

---

### 20.1 Google Cloud APIs — The Canonical Example

**Scale:** 200+ APIs, billions of API calls per day, tens of millions of developers worldwide.

**Pattern:** Every Google Cloud API is defined in a `.proto` file in the `googleapis` repository. A single gRPC service definition generates: server stubs (Go, C++), client stubs for 8+ languages, REST/JSON transcoding layer (grpc-gateway), API reference documentation, and SDK code. Google publishes language-specific client libraries (Python `google-cloud-storage`, Go `cloud.google.com/go/storage`, Java `google-cloud-storage`, TypeScript `@google-cloud/storage`) that wrap the raw gRPC stubs with idiomatic types, connection management, retry logic, and authentication.

**Legacy preservation:** Google Cloud Storage's backend is the Colossus distributed file system — Google's internal infrastructure, not publicly documented. The gRPC API is the stable external contract that hides all internal storage implementation details. Colossus has been rewritten multiple times while the GCS API has remained stable. This is the precise pattern the FileMan wrapper uses: M globals and the FileMan DBS layer are the "Colossus" — the stable internal storage that is never exposed; the gRPC API is the stable external contract.

**Reference:** [https://cloud.google.com/apis/design](https://cloud.google.com/apis/design) — Google's full API design guide, which documents this two-layer pattern in detail, including why gRPC is chosen and how language SDKs relate to the wire protocol.

---

### 20.2 Oracle Cloud Infrastructure (OCI) — Legacy Enterprise at Scale

**Scale:** 40+ cloud services, global deployment, used by enterprise customers running workloads migrated from Oracle Database, Oracle E-Business Suite, and Oracle Exadata.

**Pattern:** OCI uses a REST/JSON wire protocol (not gRPC) with an OpenAPI specification as the contract. Language SDKs — Python (`oci`), Go (`oracle/oci-go-sdk`), Java, TypeScript, .NET, Ruby — each wrap the same REST API with idiomatic types, credential management, retry logic, and pagination. The SDK layer is substantial: each SDK adds type-safe request/response objects, automatic pagination for list operations, and waiters for async operations — none of which are expressible in the raw OpenAPI spec.

**Legacy preservation:** OCI's internal storage, networking, and database services are built on Oracle's proprietary infrastructure. The REST API wrapper layer is the modernization interface — customers use modern cloud tooling without any knowledge of the underlying Oracle infrastructure. This mirrors the FileMan wrapper's role: expose modern language APIs over a proprietary M runtime.

**Reference:** [https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm)

---

### 20.3 AWS SDK (Smithy) — The Hidden Wire Protocol Beneath the SDK

**Scale:** 300+ AWS services, trillions of API calls per day, the world's largest cloud platform.

**Pattern:** AWS services are defined in Smithy model files (AWS's IDL, similar to Protocol Buffers). The AWS SDK generator consumes Smithy models and produces language SDKs (Python `boto3`, Go `aws-sdk-go-v2`, Java `aws-sdk-java-v2`, TypeScript `@aws-sdk/client-*`, Rust `aws-sdk-rust`). Each SDK provides typed request and response objects, connection pooling, retry with exponential backoff, credential providers, endpoint resolution, and pagination — all invisible to application code.

**Legacy preservation:** DynamoDB is built on Amazon's Dynamo key-value store; S3 is built on internal object storage infrastructure; RDS wraps PostgreSQL/MySQL/Oracle with additional management infrastructure. The SDK layer hides all of this. Application code using `boto3.client('s3').get_object()` has no knowledge of the underlying S3 storage architecture. The FileMan wrapper achieves the same result: application code calling `fm.get_entry("2", "100")` has no knowledge of M globals, MUMPS runtime, or FileMan API conventions.

**Reference:** [https://smithy.io/2.0/](https://smithy.io/2.0/) — Smithy IDL specification (AWS's Protocol Buffers equivalent)

---

### 20.4 Stripe — Legacy Payment Infrastructure Behind a Clean API

**Scale:** $1 trillion+ in payments processed, used by millions of merchants.

**Pattern:** Stripe exposes a REST/JSON API (its own specification, not OpenAPI). Language SDKs — Python `stripe`, Ruby `stripe-ruby`, Go `stripe-go`, Node `stripe-node`, Java `stripe-java`, .NET `stripe-dotnet` — all wrap the same REST wire protocol with idiomatic types, automatic retry, idempotency key management, and webhook handling. Stripe's internal infrastructure includes legacy payment processing systems, banking connections, and regulatory compliance systems that are completely hidden behind the API.

**Legacy preservation:** Stripe's original payment processing was built on existing banking infrastructure (ACH, card networks, legacy systems). The API layer wraps all of this. Merchants writing `stripe.PaymentIntent.create(amount=1000, currency='usd')` have no knowledge of what happens internally — which card network is engaged, which acquiring bank processes the transaction, which compliance system validates it. The FileMan wrapper provides the same opacity: `fm.file(fda)` has no visible coupling to the M global storage, the cross-reference triggers, or the audit system that executes behind the scenes.

**Reference:** [https://stripe.com/docs/api](https://stripe.com/docs/api) | [https://github.com/stripe/stripe-python](https://github.com/stripe/stripe-python)

---

### 20.5 SAP (Extended) — gRPC Inside a Legacy ERP System

**Scale:** 440,000+ SAP customers, the world's largest ERP system, running the financial and operational backbone of most Fortune 500 companies.

**Pattern (extended from §4.6):** SAP's architecture evolution is the most direct analog to the FileMan situation. SAP R/3 and S/4HANA run on the ABAP runtime — a proprietary language with its own database abstraction layer (Open SQL over SAP HANA or DB2 or Oracle). Business logic in ABAP is callable via RFC (Remote Function Call) and BAPI (Business Application Programming Interface). SAP's language SDKs — `pyrfc` (Python), `gorfc` (Go), `node-rfc` (Node.js), `nwrfcsdk` (C/C++) — all wrap the RFC library with idiomatic types. **SAP has also shipped gRPC support** in its Business Technology Platform (SAP BTP), using Protocol Buffers to expose ABAP services as gRPC endpoints with generated stubs.

**Why this matters for FileMan:** SAP and VistA share a structural DNA: a proprietary language (ABAP / MUMPS), a proprietary database abstraction (Open SQL / FileMan DBS), and a call-based integration mechanism (RFC / RPC Broker). SAP's 30-year evolution from RFC to BAPI to REST to gRPC is a roadmap the FileMan wrapper is compressing into a single generation of tooling by choosing gRPC from the start.

**Reference:** [https://github.com/SAP/PyRFC](https://github.com/SAP/PyRFC) | [https://github.com/SAP/gorfc](https://github.com/SAP/gorfc) | [https://community.sap.com/topics/btp](https://community.sap.com/topics/btp)

---

### 20.6 The Common Pattern: What All of These Share

Every system above preserves its transactional database and business logic layer intact while adding a typed API contract (gRPC, REST+OpenAPI, Smithy) as the new external interface, with idiomatic language SDKs as the developer-facing layer. None of them modified their core data storage. None of them required application developers to understand the internal data model. All of them achieved language portability, cloud deployment, and developer ecosystem growth without touching the storage layer.

**This is precisely the goal of the FileMan gRPC wrapper.** FileMan's global storage, cross-reference triggers, INPUT transform validation, and audit system are the transactional core that must not be modified. The `.proto` file is the new API contract. The Python, Go, Rust, and TypeScript SDKs are the developer-facing layer. The M runtime (YottaDB or IRIS) is the implementation detail that no application developer ever sees.

---

---

## 21. IRIS Implementation Guide: Building the Wrapper on InterSystems IRIS

For implementation details, code examples, and a step-by-step deployment guide for building the FileMan gRPC Gateway on InterSystems IRIS, see the dedicated guide:

**[fileman-iris-implementation-guide.md](fileman-iris-implementation-guide.md)**

That guide covers IRIS architecture fundamentals (namespaces, global mapping), prerequisites and environment setup, the `irisdb.h` C binding, the `intersystems-irispython` Python binding, the TCP SuperServer remote path, the `IRISRuntime` interface implementation, error handling, a four-test test suite, and a ten-step deployment checklist.

## 22. YottaDB Implementation Guide: Building the Wrapper on YottaDB

For implementation details, code examples, and a step-by-step deployment guide for building the FileMan gRPC Gateway on YottaDB, see the dedicated guide:

**[fileman-yottadb-implementation-guide.md](fileman-yottadb-implementation-guide.md)**

That guide covers YottaDB architecture fundamentals (global directory, process model, multi-threaded call-in), prerequisites and environment setup, the `libyottadb.h` C binding and call-in table, the `yottadb` Python binding, the Go binding, the `YDBRuntime` interface implementation, error handling, a four-test test suite, and a ten-step deployment checklist.


*This specification, Version 1.4, is grounded exclusively in the VA FileMan 22.2 documentation set as ingested, processed, and stored in `~/data/vista-docs/publish/infrastructure/di--fileman/` by the vista-docs pipeline. All FileMan API entry points, calling conventions, data structures, and security mechanisms are sourced from those local files. See §16 for the specific local file paths and cited line numbers.*

*FileMan namespace: `DI`. Local processed documentation: `~/data/vista-docs/publish/infrastructure/di--fileman/`*
