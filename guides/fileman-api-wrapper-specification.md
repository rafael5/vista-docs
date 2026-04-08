# VA FileMan External API Wrapper — Comprehensive Specification

**Enabling Non-M Language Application Development Against the FileMan Database Engine**

*Version 1.0 — April 2026*
*Audience: Software architects, API engineers, and VistA modernization program leads*

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Background: The Problem of Legacy Database Preservation](#2-background-the-problem-of-legacy-database-preservation)
3. [Industry Methodology: Wrapping Legacy Database Systems](#3-industry-methodology-wrapping-legacy-database-systems)
4. [Case Studies: Successful Major API Wrapper Projects](#4-case-studies-successful-major-api-wrapper-projects)
5. [FileMan as a Wrapping Target: Capabilities and Constraints](#5-fileman-as-a-wrapping-target-capabilities-and-constraints)
6. [Transport Architecture Options](#6-transport-architecture-options)
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

| Strategy | Mechanism | Latency | Co-location Required | Maturity |
|---|---|---|---|---|
| **YottaDB embedded call-in** | C shared library via FFI | Sub-millisecond | Yes — same host | Production (YottaDB 1.x) |
| **VistA RPC Broker (TCP)** | XWB wire protocol, TCP port 9200 | Network round-trip | No | Production since 1993 |
| **Purpose-built gRPC service** | gRPC over TLS, Protocol Buffers | Network round-trip | No | Greenfield |
| **REST/JSON over HTTP** | HTTP/1.1 or HTTP/2 | Network round-trip | No | Greenfield (see MVDM) |
| **FMQL REST service** | HTTP/JSON, GraphQL-like syntax | Network round-trip | No | Research/prototype |

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

### VA FileMan Documentation (VA Software Document Library)

All FileMan documentation is available on the VA VDL under the FileMan application page.

| Document | Format | Direct Link |
|---|---|---|
| VA FileMan Application Page (VDL) | Web | [https://www.va.gov/vdl/application.asp?appid=5](https://www.va.gov/vdl/application.asp?appid=5) |
| FM 22.2 Developer's Guide (Rev 1.14, July 2025) | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2dg.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2dg.pdf) |
| FM 22.2 Developer's Guide | DOCX | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2dg.docx](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2dg.docx) |
| FM 22.2 Technical Manual (Rev 1.6, July 2025) | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2tm.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2tm.pdf) |
| FM 22.2 Technical Manual | DOCX | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2tm.docx](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2tm.docx) |
| FM 22.2 User Manual (Volume 1) | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2um1.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2um1.pdf) |
| FM 22.2 Advanced User Manual (Volume 2) | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2um2.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2um2.pdf) |
| FM 22.2 Data Access Control (DAC) User Guide | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2p8_dac_ug.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2p8_dac_ug.pdf) |
| FM 22.2 Installation, Back-Out, and Rollback Guide | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2ig.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2ig.pdf) |
| FM 22.2 Release Notes | PDF | [https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2rn.pdf](https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2rn.pdf) |
| SQLI DI*21*38 Site Manual | PDF | [https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_sm.pdf](https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_sm.pdf) |
| SQLI DI*21*38 Vendor Guide | PDF | [https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_vendor.pdf](https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_vendor.pdf) |

### VistA RPC Broker (Transport Reference)

| Resource | Link |
|---|---|
| VistA RPC Broker Application Page (VDL) | [https://www.va.gov/vdl/application.asp?appid=47](https://www.va.gov/vdl/application.asp?appid=47) |
| VistA Source Code (OSEHRA GitHub) | [https://github.com/OSEHRA/VistA](https://github.com/OSEHRA/VistA) |

### Related VistA Wrapper Projects

| Project | Repository / Reference |
|---|---|
| FMQL — FileMan Query Language | [https://github.com/caregraf/FMQL](https://github.com/caregraf/FMQL) |
| FMQL — AMIA 2012 Paper | [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540540/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540540/) |
| nodeVISTA / MVDM (OSEHRA) | [https://github.com/vistadataproject/nodeVISTA](https://github.com/vistadataproject/nodeVISTA) |
| VistA Data Project (VDM) | [https://github.com/vistadataproject/VDM](https://github.com/vistadataproject/VDM) |
| VA Lighthouse Developer Portal | [https://developer.va.gov/](https://developer.va.gov/) |
| nodem — YottaDB/GT.M Node.js interface | [https://github.com/dlwicksell/nodem](https://github.com/dlwicksell/nodem) |

### YottaDB (M Runtime and Call-In Interface)

| Resource | Link |
|---|---|
| YottaDB Documentation Home | [https://docs.yottadb.com/](https://docs.yottadb.com/) |
| YottaDB Call-In Interface | [https://docs.yottadb.com/ProgrammersGuide/externalroutines.html](https://docs.yottadb.com/ProgrammersGuide/externalroutines.html) |
| YottaDB Go Wrapper | [https://pkg.go.dev/lang.yottadb.com/go/yottadb](https://pkg.go.dev/lang.yottadb.com/go/yottadb) |
| YottaDB Python Wrapper | [https://pypi.org/project/yottadb/](https://pypi.org/project/yottadb/) |

### Architecture Patterns and Methods

| Reference | Link |
|---|---|
| Evans, E. — *Domain-Driven Design* (2003) — Anti-Corruption Layer | [https://www.domainlanguage.com/ddd/](https://www.domainlanguage.com/ddd/) |
| Fowler, M. — *Patterns of Enterprise Application Architecture* (2002) — Gateway, Repository | [https://martinfowler.com/books/eaa.html](https://martinfowler.com/books/eaa.html) |
| Fowler, M. — Strangler Fig Application Pattern (2004) | [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html) |
| Gamma et al. — *Design Patterns* (1994) — Façade, Adapter | [https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612) |
| gRPC documentation | [https://grpc.io/docs/](https://grpc.io/docs/) |
| Protocol Buffers Language Guide (proto3) | [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/) |
| OpenAPI 3.1 Specification | [https://spec.openapis.org/oas/v3.1.0](https://spec.openapis.org/oas/v3.1.0) |

### Analog Systems (Case Study References)

| System | Reference |
|---|---|
| SAP BAPI / RFC — Python client (pyrfc) | [https://github.com/SAP/PyRFC](https://github.com/SAP/PyRFC) |
| SAP BAPI / RFC — Go client (gorfc) | [https://github.com/SAP/gorfc](https://github.com/SAP/gorfc) |
| InterSystems IRIS REST documentation | [https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GREST](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GREST) |
| IBM z/OS Connect EE documentation | [https://www.ibm.com/docs/en/zosconnect/3.0](https://www.ibm.com/docs/en/zosconnect/3.0) |
| Oracle REST Data Services (ORDS) | [https://www.oracle.com/database/technologies/appdev/rest.html](https://www.oracle.com/database/technologies/appdev/rest.html) |

---

*This specification is grounded in the VA FileMan 22.2 documentation set from the VA Software Document Library. All FileMan API entry points, calling conventions, data structures, and security mechanisms described in this document are sourced from the primary VDL documentation listed in §16. For authoritative technical detail on any FileMan entry point, consult the FM 22.2 Developer's Guide.*

*FileMan namespace: `DI`. VDL application: [https://www.va.gov/vdl/application.asp?appid=5](https://www.va.gov/vdl/application.asp?appid=5)*
