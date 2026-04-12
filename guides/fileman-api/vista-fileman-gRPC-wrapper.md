# VistA Fileman gRPC Wrapper Guide

**Project:** `rafael5/vista-grpc`
**Purpose:** gRPC wrapper for VistA FileMan via YottaDB C API in Go
**Host machine:** minty (Linux Mint 22.3 "Zena")
**Guide version:** 9.0 — April 2026
**Spec status:** Complete — ready for implementation

---

## Table of Contents

1. [Introduction](#introduction)
2. [Background — Prior Art and Lessons Learned](#background--prior-art-and-lessons-learned)
3. [Architecture Rationale](#architecture-rationale)
4. [Architecture Overview](#architecture-overview)
5. [Development Methodology](#development-methodology)
6. [Base Docker Image](#base-docker-image)
7. [Repository Structure](#repository-structure)
8. [Portability Design](#portability-design)
9. [Developer Toolkit](#developer-toolkit)
10. [Phase 0 — Corpus Analysis](#phase-0--corpus-analysis)
11. [Phase 1 — Characterization](#phase-1--characterization)
12. [Phase 2 — Contract Definition](#phase-2--contract-definition)
13. [Phase 3 — Implementation](#phase-3--implementation)
14. [Phase 4 — Continuous Verification](#phase-4--continuous-verification)
15. [Golden File Strategy](#golden-file-strategy)
16. [Three Test Layers](#three-test-layers)
17. [Dockerfile Layers](#dockerfile-layers)
18. [Dev User](#dev-user)
19. [Go Toolchain and TDD Stack](#go-toolchain-and-tdd-stack)
20. [Proto Toolchain](#proto-toolchain)
21. [Dev Container Configuration](#dev-container-configuration)
22. [Makefile](#makefile)
23. [Linter Configuration](#linter-configuration)
24. [Pre-commit Hooks](#pre-commit-hooks)
25. [Container Entrypoint](#container-entrypoint)
26. [CI Pipeline](#ci-pipeline)
27. [Self-Documentation Strategy](#self-documentation-strategy)
28. [Claude Code CLI Integration](#claude-code-cli-integration)
29. [FileMan Knowledge Sources](#fileman-knowledge-sources)
30. [MVDM / FMQL Lessons Learned](#mvdm--fmql-lessons-learned)
31. [Open Items](#open-items)
32. [Implementation Order](#implementation-order)

---

## Introduction

### What This Project Is

`vista-grpc` is a production-quality, read-write, semantically faithful
gRPC wrapper for VA VistA's FileMan database API, implemented in Go,
running against a YottaDB backend, and designed for portability to
InterSystems IRIS.

It exposes VistA's FileMan data — the entire clinical, administrative,
and operational record of the US Veterans Health Administration's
electronic health record system — through a typed, versioned, modern
gRPC interface. Every FileMan file, every field, every pointer
relationship, every nested subfile is accessible through a single
coherent API surface with full bidirectional read-write semantics.

---

### Why FileMan Needs a Modern Wrapper

VistA is the largest integrated healthcare information system in the
world. It serves nearly 9 million veterans across 170 VA medical
centers and 1,000+ outpatient clinics. It has been in continuous
clinical operation since 1985.

At its core, every piece of VistA clinical data — patient demographics,
medications, lab results, orders, notes, allergies, vital signs,
appointments, diagnoses — is stored in and managed by FileMan, a
database management system written in M/MUMPS in 1978. FileMan is
not a curiosity. It is the operational data engine of the largest
national healthcare system in the United States, still processing
millions of clinical transactions daily.

FileMan has no modern programmatic interface. Its only external access
mechanism — the RPC Broker — was designed for Delphi desktop clients
in 1994. It returns opaque delimited strings. It has no schema.
It has no typed contract. It has no introspection. Accessing VistA
data requires deep M/MUMPS expertise, knowledge of FileMan's internal
global structure, and manual interpretation of undocumented return
formats.

This project solves that problem.

---

### Project Goals

**Primary goal:** Provide a complete, typed, read-write, semantically
faithful gRPC API over VistA's FileMan database that any Go, Python,
JavaScript, Java, or other gRPC-capable application can use without
M/MUMPS expertise.

**Secondary goals:**

*Semantic fidelity:* The API must preserve the full meaning of
FileMan data — not flatten it into lowest-common-denominator strings.
Dates must be timestamps. Sets of codes must be enums. Pointer fields
must carry both their internal IEN and their resolved display value.
Nested subfiles must be `repeated` typed messages. Nothing clinically
significant must be silently lost in translation.

*Full read-write:* Every prior VistA wrapper project that achieved
production deployment was read-only or read-heavy. This project wraps
FileMan's write APIs (`FILE^DIE`) with the same rigor as its read
APIs (`DIQ^DIQ`, `FIND^DIC`). A read-only VistA API is a viewer,
not an integration platform.

*Portability:* VistA runs on two backends — YottaDB (open source)
and InterSystems IRIS (commercial). The `fileman.Interface` abstraction
boundary ensures that wrapping one backend does not preclude the other.

*Self-documenting:* FileMan's own documentation is decades old,
inconsistently maintained, and full of gaps. Every FileMan API
behavior this project wraps is characterized against the live system,
recorded as golden test fixtures, documented in structured discovery
notes, and locked as regression tests. This project becomes the
authoritative reference for FileMan API behavior.

*Production quality:* The wrapper is built with the same engineering
rigor as production financial or medical software — TDD, linting,
vulnerability scanning, CI, pre-commit gates, characterization testing,
and integration test coverage. No shortcuts because the data is
clinical.

---

### The FileMan Problem in Detail

FileMan stores all data as global variables in M's native
multidimensional array store. A patient record is not a row in a
table — it is a sparse, hierarchically nested global subtree with
hundreds of potential fields, nested subfiles (Multiples), pointer
relationships to dozens of other files, and computed fields that
cannot be written. The data dictionary describing all of this lives
in a parallel set of globals (`^DD`, `^DIC`) that are themselves
FileMan files.

This creates five distinct technical challenges that every prior
wrapper project encountered:

**1. No formal schema.** FileMan's schema lives in `^DD` globals, not
in any machine-readable format recognizable by modern tooling.
Extracting and normalizing it requires querying the live system.

**2. Inconsistent naming across 40+ years.** The same concept
appears under different field names across different files
(`PATIENT NAME`, `PT NAME`, `NAME OF PATIENT`). The same field
type is used inconsistently across packages developed independently
over decades.

**3. Complex type system.** FileMan has eight distinct field types —
Free Text, Numeric, Date/Time, Set of Codes, Pointer, Multiple
(subfile), Word Processing, and Computed — each with different
storage formats, retrieval mechanisms, and write semantics. None
map cleanly to proto scalar types without transformation.

**4. Dates are not timestamps.** FileMan stores dates as a numeric
`YYYMMDD.HHMMSS` format where YYY = years since 1700. External
display is `DEC 31, 1998`. Neither format is ISO 8601. Active
transformation with epoch arithmetic is required for every date field.

**5. Multiples are nested files.** FileMan's Multiple type (`M`) is
not an array field — it is a recursively nested file with its own
IEN structure, its own `^DD` entries, and its own field inventory.
Every prior wrapper project underestimated the depth and prevalence
of Multiples and produced incomplete or incorrect representations
of the most clinically important FileMan data structures.

---

### Key Architectural Decisions and Their Motivations

Each of the following architectural decisions was made in direct
response to a specific failure mode in prior VistA wrapper projects.
Each is explained fully in the [Architecture Rationale](#architecture-rationale)
section.

| Decision | Motivation |
|---|---|
| Go + CGo + `lang.go.yottadb` | Type safety + native YottaDB C API — replaces Node.js/nodem instability |
| gRPC + proto | Typed contracts replace opaque RPC Broker strings |
| `fileman.Interface` portability boundary | YottaDB + IRIS portability from day one |
| Characterization-first methodology | No test infrastructure was MVDM's fatal flaw |
| Golden file ground truth | Hermetic tests — no live database in CI |
| Phase 0 corpus analysis | Normalize once at the corpus level, not once per file |
| `cmd/analyze` two-pass normalization | Heuristics for obvious cases; Claude API for ambiguous |
| Recursive Multiple traversal | Multiples are the most prevalent and most underestimated FileMan structure |
| `dates.go` epoch transformation | Every prior project lost date precision silently |
| `wordproc.go` separate retrieval | WP fields require a different call-in path — not a string |
| Explicit `resolve_pointers` flag | Eager resolution caused cascade performance failures in FMQL and MVDM |
| V1 scope lock by pointer graph centrality | MVDM stalled under unbounded scope creep |
| Delegate to FileMan M routines (Phase 1) | FileMan internals are complex; proven M code is safer than reimplementation |
| Self-documenting `docs/` structure | FileMan documentation is poor; this project becomes the reference |

---

### What This Project Is Not

**Not a FHIR server.** FHIR's general-purpose resource model loses
clinically significant VistA-specific semantics. This project preserves
FileMan's native semantic model in proto types, not a standards mapping.

**Not an ORM.** Mapping FileMan's hierarchical graph model to ActiveRecord
or any relational ORM pattern is the wrong abstraction. FileMan is not
relational. This project wraps FileMan's own APIs.

**Not a read-only viewer.** Every prior production VistA API was read-only
or read-mostly. Full bidirectional read-write is a first-class requirement.

**Not a replacement for FileMan.** FileMan's cross-references, input
transforms, and referential integrity enforcement run in M. This project
delegates to FileMan's own APIs rather than reimplementing FileMan
semantics in Go. FileMan's data integrity guarantees are preserved.

**Not a one-size-fits-all interoperability standard.** gRPC is the
transport. The API is FileMan-native. Consumers that need FHIR can
build a translation layer on top.

---

## Background — Prior Art and Lessons Learned

Every significant attempt to build a programmatic wrapper over VistA's
FileMan data dictionary has failed to achieve full coverage, full
read-write access, semantic fidelity, and production scale simultaneously.
Understanding why each project failed — and what it did correctly — is
the foundation for every architectural decision in this project.

Eight prior projects are documented here in order of increasing semantic
fidelity. Each is analyzed for technology, read/write coverage, semantic
fidelity, and primary failure modes. The final section maps each failure
mode to a concrete decision in this project's design.

---

### Project 1 — RPC Broker (XWB) — The Original Layer

**Technology:** Delphi/Pascal client, TCP socket, custom wire protocol,
M server-side routines
**Era:** 1994 — present (CPRS still uses it today)
**Read/Write:** Full read-write
**Semantic fidelity:** None

The RPC Broker is the original VistA remote access layer. CPRS, the
primary clinical interface used by VA clinicians for decades, is built
entirely on top of it.

**Failure mode:**
The only API available via the RPC Broker required VistA experience
to use. VistA knowledge was needed to understand the data coming back
— there was no abstraction above the M routine level. Every consumer
had to understand FileMan internals. The wire protocol returns opaque
delimited strings. No typed contracts. No schema. No semantic meaning.

This is not a failure so much as a design that never intended to be
a general-purpose API. It is a remote procedure call mechanism, not
a data model.

**What it got right:**
Full read-write. Battle-tested at scale across 130 VA sites for 30+
years. The RPC Broker proves that VistA's M layer can sustain high
throughput production workloads.

**Lesson for this project:**
The RPC Broker is what this project replaces for programmatic FileMan
access. gRPC provides the typed contract the RPC Broker never had.
The M layer's proven reliability is preserved — this project calls
into it via `lang.go.yottadb`, not around it.

---

### Project 2 — VPR (Virtual Patient Record)

**Technology:** M routines, RPC calls, XML and JSON output
**Era:** 2011 — present (still actively maintained as of 2024)
**Read/Write:** Read-only — by explicit design
**Semantic fidelity:** Medium — domain-normalized field names,
common data structures across domains, but patient-centric only

VPR provides a cached view of the patient chart with normalized
fields and common field names across clinical domains. It includes
four RPCs that extract data from VistA as XML or JSON. It maps
VistA files and fields to other data models and extracts that data
as XML or JSON objects.

**Failure modes:**

*Read-only:* VPR has no write path. It was designed solely for
data extraction to feed downstream systems (InterSystems HealthShare,
Joint Legacy Viewer, eHMP). Any application that needs to create or
modify VistA records must bypass VPR entirely and call VistA RPCs
directly.

*Patient-centric only:* VPR only covers clinical domains for a
specific patient IEN. Administrative files, configuration files,
non-patient-centric data, and cross-patient queries are all out
of scope.

*M-side normalization:* The normalization logic lives in M routines.
It cannot be extended or modified without M expertise. The abstraction
is opaque to external developers.

*RPC transport dependency:* VPR still requires the RPC Broker for
transport. It is not a standalone API layer — it is a normalization
layer on top of an existing transport.

**What it got right:**
VPR proved that domain-normalized field names and common data structures
across VistA's clinical domains are achievable and valuable. Its
normalized JSON output influenced every subsequent project.

**Lesson for this project:**
VPR's read-only constraint, patient-centric scope, and M-side
implementation are exactly the constraints this project is designed
to overcome. The normalization approach — common field names across
domains — directly informs the shared type library produced by
`cmd/corpus` in Phase 0.

---

### Project 3 — FMQL (FileMan Query Language) — Caregraf

**Technology:** Python, M call-in via RPC, SPARQL-inspired query
language, REST/JSON linked data endpoint
**Era:** 2010 — ~2016
**Read/Write:** Read-only — by explicit design
**Semantic fidelity:** Highest of any read-only project — full `^DD`
schema exposure, complete pointer graph traversal, linked data model

FMQL delivered one uniform mechanism for extracting all FileMan data
and metadata. It treated FileMan as a semantic web graph — every file
was a node, every pointer was a directed edge. The FMQL Rambler
browser let developers navigate the full FileMan graph interactively.

FMQL proved that the `^DD` global is fully queryable programmatically
and that the complete FileMan corpus can be systematically introspected.
This is the closest prior art to the `cmd/corpus` Phase 0 pipeline
in this project.

**Failure modes:**

*Read-only:* FMQL was explicitly designed as a query language. No
write path was ever built. Any application needing to modify VistA
data had to bypass FMQL entirely.

*SPARQL complexity:* The query language was too complex for most
consumers. Adoption was limited to specialists who already understood
both SPARQL and FileMan. A typed contract (like proto) would have
been more accessible.

*Eager pointer resolution at scale:* The linked data model resolved
pointer chains eagerly to return display values inline. A single
complex query could trigger dozens of transitive pointer lookups,
causing cascade performance degradation.

*No production deployment:* FMQL remained a research and demo tool.
It was never deployed in production at a VA site.

**What it got right:**
FMQL proved that programmatic `^DD` introspection is feasible at
corpus scale. Its linked data model correctly identified the pointer
graph as the central structural concern in FileMan normalization.
The FMQL Rambler remains the best tool for interactive FileMan
exploration.

**Lesson for this project:**
`cmd/introspect` and `cmd/corpus` are a Go reimplementation of
FMQL's schema extraction, targeted at proto generation rather than
SPARQL queries. FMQL's read-only constraint and query language
complexity are the problems gRPC's typed contracts solve. FMQL's
eager pointer resolution failure directly informs the explicit
`resolve_pointers: bool` flag in this project's proto API design.

---

### Project 4 — ActiveFileMan (JRuby vista-adapter)

**Technology:** JRuby, Java/MUMPS bridge via OVID
**Era:** ~2012
**Read/Write:** Partial read-write
**Semantic fidelity:** Low-medium — ActiveRecord ORM pattern mapped
over FileMan files

ActiveFileMan provided access to FileMan files in a similar fashion
to ActiveRecord providing access to tables in a relational database.
It used OVID to access data in VistA and provided Ruby objects for
working with patients, medications, and vital signs.

**Failure modes:**

*ORM impedance mismatch:* Mapping FileMan's hierarchical/graph model
to ActiveRecord's relational assumptions was fundamentally leaky.
FileMan's Multiple (subfile) type — nested files within files — has
no ActiveRecord equivalent. Cross-references, computed fields, and
input transforms break the ORM abstraction entirely. The mismatch
was not a tooling problem — it was a conceptual category error.
FileMan is not relational.

*JRuby/OVID bridge fragility:* The OVID bridge between Java and M
was brittle and version-sensitive. The runtime dependency chain was
complex: JVM + JRuby + OVID + GT.M/YottaDB. Each layer introduced
compatibility surface area.

*Abandoned early:* Very limited file coverage. Never reached
production use. The ORM mismatch problem was likely recognized
before the project could demonstrate value.

**What it got right:**
The observation that FileMan files could be treated as domain objects
(patients, medications, vital signs) — even if the ORM abstraction
was wrong — prefigured the domain-centric approach of MVDM.

**Lesson for this project:**
The ActiveRecord pattern for FileMan is the wrong abstraction.
`fileman.Interface` is deliberately not an ORM. It wraps FileMan's
own APIs (`DIQ`, `FILE^DIE`, `FIND^DIC`) rather than reimplementing
relational access patterns on top of a graph store. FileMan's own
APIs already encode the correct access semantics — delegate to them.

---

### Project 5 — MVDM / nodeVISTA (VistA Data Project)

**Technology:** Node.js, nodem (YottaDB/GT.M Node.js binding),
REST/JSON, JavaScript full-stack
**Era:** 2014 — ~2019
**Read/Write:** Full read-write — the first project to achieve this
**Semantic fidelity:** Highest of all projects — domain-normalized,
semantic overlay, shared type model across VistA domains

MVDM aimed to comprehensively expose VistA's internal operational
data model in a modern computable form, then incrementally normalize
it across all 130 VA VistA systems into a single national Master
Veteran Data Model. It was the most ambitious and technically
sophisticated VistA wrapper project ever attempted.

**Failure modes:**

The five core technical failure modes are documented in detail in
the [MVDM / FMQL Lessons Learned](#mvdm--fmql-lessons-learned)
section of this guide. They are:
1. Multiple/Subfile type underestimated
2. FileMan date format treated as a string
3. Pointer resolution strategy undefined (defaulted to eager)
4. Word Processing fields treated as scalars
5. Scope creep without pointer graph centrality guidance

Additional failure modes beyond the five technical lessons:

*Node.js runtime mismatch:* The single-threaded event loop created
subtle concurrency issues with YottaDB's locking model. Node.js was
not designed for the write pattern of a clinical database — sustained
high-throughput, lock-heavy, transactional M operations.

*nodem binding instability:* The Node.js-to-YottaDB/GT.M binding
was maintained by a small community and had version compatibility
issues as Node.js evolved rapidly through major versions during the
project's lifetime.

*No test infrastructure:* The project had minimal automated testing.
No golden file strategy, no characterization tests, no integration
test harness. Bugs in normalization logic were hard to detect,
reproduce, or confidently fix. This was the technical failure that
compounded every other problem — changes broke things silently.

*Organizational discontinuity:* MVDM was a VA-funded contract effort.
When funding ended the GitHub organization went dark (repositories
are now private), the project website was hijacked, and institutional
knowledge was lost. The project had no community sustainability plan.

*Political cancellation:* The VA prohibited further modernization of
VistA when it awarded the Cerner replacement contract in 2018,
eliminating promising technology including MVDM even when it was
already in beta testing.

**What it got right:**
MVDM achieved full read-write access — the first project to do so.
Its domain-normalized shared type model was architecturally correct.
The `^DD`-based corpus analysis approach was proven. The semantic
overlay concept — abstracting FileMan's internal structure into
clinical domain objects — is the right design. Every subsequent
project has built on MVDM's conceptual foundation.

**Lesson for this project:**
MVDM's conceptual architecture is correct. Its implementation
substrate was wrong. Go + CGo + `lang.go.yottadb` replaces Node.js
+ nodem with a runtime that is type-safe, concurrent, and natively
suited to high-throughput database operations. The characterization
testing methodology directly addresses MVDM's fatal lack of test
infrastructure. The V1 scope lock via pointer graph centrality
directly addresses the scope creep that stalled MVDM.

---

### Project 6 — eHMP (Enterprise Health Management Platform)

**Technology:** Node.js (RDK — Resource Development Kit), Java
(Spring Boot + HAPI FHIR), VxSync (data synchronization service),
JDS (JSON Data Store — MongoDB cache), M KIDS patches (VistA-side)
**Era:** 2013 — 2018 (cancelled by VA)
**Read/Write:** Read-heavy, limited write
**Semantic fidelity:** Medium — FHIR R4 output, but VistA-to-FHIR
mapping was structurally lossy

eHMP was the VA's most ambitious internal modernization effort —
intended to replace CPRS as VA's primary point-of-care application.
It included VistA Exchange, a clinical practice environment, and
FHIR APIs. The VistA REST API read data from VistA and returned
it as delimited text or JSON. A Java FHIR API called the REST API
and translated the output into FHIR R4.

**Failure modes:**

*Architectural complexity:* eHMP required five services running
simultaneously — VistA (M), RDK (Node.js), VxSync (sync service),
JDS (MongoDB), and the UI — just to serve a single patient record
read. Installation documentation described VxSync configuration as
"very finicky." The operational burden of keeping five services
synchronized was substantial.

*JDS sync cache inconsistency:* VxSync maintained a MongoDB cache
of VistA data. Cache staleness created subtle data consistency bugs
in production — a record written to VistA was not immediately
visible through the FHIR API because the sync had not yet propagated.
Real-time clinical applications cannot tolerate this.

*FHIR structural lossiness:* Key issues included resolving differences
in assumptions around medication order workflow, fitting VA's
specialized vocabularies developed over decades into FHIR's
high-level general-purpose categories, and managing different access
control models. FHIR's resource model could not cleanly represent
VistA's domain-specific structures without information loss.
Clinically significant nuance was silently dropped in translation.

*Read-mostly design:* The FHIR layer was optimized for read. Write
operations required bypassing the FHIR layer and calling VistA RPCs
directly, defeating the abstraction for any application that needed
to create or modify records.

*Political cancellation:* The VA prohibited further VistA
modernization when it awarded the Cerner contract in 2018,
eliminating eHMP even when it was already in beta testing at
VA sites.

**What it got right:**
eHMP demonstrated that a comprehensive multi-domain clinical API
layer over VistA is operationally feasible. Its FHIR output approach
influenced the VA Lighthouse platform that followed.

**Lesson for this project:**
eHMP's sync-cache architecture is the wrong model for a wrapper that
needs data consistency. This project uses direct call-in to FileMan
via `lang.go.yottadb` — no intermediate cache. Consistency is
guaranteed because reads and writes go directly to the authoritative
YottaDB store. eHMP's FHIR lossiness confirms that a FileMan-native
proto API preserves more semantic fidelity than mapping to a
general-purpose interoperability standard.

---

### Project 7 — IRIS FileMan Mapping Utility (InterSystems)

**Technology:** ObjectScript, IRIS SQL engine, computed properties,
`%Library.FilemanDate` and `%Library.FilemanTimeStamp` data types
**Era:** 2000s — present (available in current IRIS)
**Read/Write:** Full read-write via SQL
**Semantic fidelity:** Medium — SQL projection of FileMan, pointer
expansion as computed properties, proprietary date types

InterSystems IRIS provides a utility to convert FileMan files into
IRIS classes, providing object and SQL access to the data. The
utility generates IRIS class definitions that map FileMan globals.
Date fields are mapped to proprietary `%Library.FilemanDate` types.
Pointer fields can optionally generate computed properties that
expand the pointer to the referenced record's name field.

InterSystems explicitly recommends against starting new projects
with FileMan and positions the mapping utility as a migration tool
rather than a production wrapper.

**Failure modes:**

*IRIS-only:* The mapping utility is a proprietary InterSystems
feature. It is not portable to YottaDB or GT.M. Any application
built on it is locked to the IRIS runtime.

*SQL impedance mismatch:* The relational SQL projection of FileMan's
hierarchical model has the same fundamental mismatch problem as
ActiveFileMan. Multiples become child tables requiring JOIN queries.
The hierarchical nature of FileMan IEN structures does not map
cleanly to SQL primary/foreign key relationships.

*Eager pointer computed properties:* The optional computed property
expansion of pointer fields uses the same eager resolution strategy
that caused performance problems in FMQL and MVDM.

*Migration tool positioning:* The utility is designed to help
organizations migrate away from FileMan, not to expose FileMan
as a long-term API surface. InterSystems' own guidance is to move
off FileMan.

**What it got right:**
IRIS's `%Library.FilemanDate` and `%Library.FilemanTimeStamp`
proprietary data types confirm that FileMan date handling is a
first-class concern requiring dedicated implementation — not just
a type annotation. This directly validates the `dates.go` module
in this project. IRIS also correctly handles Word Processing fields
as lists (`wpIsList` setting), confirming that WP fields require
special list-oriented handling rather than scalar string treatment.

**Lesson for this project:**
IRIS's date type approach confirms the `dates.go` module design.
Its WP list handling confirms the `wordproc.go` separate retrieval
path. Both lessons are already incorporated into this project's
spec via the MVDM lessons section. The IRIS utility's failure to
achieve portability (IRIS-only) directly motivates this project's
`fileman.Interface` portability boundary designed to support both
YottaDB and IRIS implementations.

---

### Project 8 — VA Lighthouse API Platform

**Technology:** Java, Spring Boot, HAPI FHIR, Swagger/OpenAPI,
OAuth 2.0
**Era:** 2018 — present
**Read/Write:** Read-only externally; limited write for authorized
clinical applications
**Semantic fidelity:** Medium — FHIR R4, limited to specific
clinical domains

Lighthouse is the VA's current external developer API platform.
It exposes read-only FHIR APIs to third-party developers and
authorized applications. It calls VistA RPCs and VPR — not FileMan
directly. It is an API gateway over existing VistA APIs, not a new
FileMan access layer.

Key issues in building Lighthouse included resolving differences in
assumptions around medication order workflow, fitting VA's specialized
vocabularies into FHIR's high-level categories, and managing different
access control models between VistA and OAuth.

**Failure modes:**

*Read-only externally:* Lighthouse exposes read-only FHIR APIs to
third-party developers. Write access is not exposed publicly and
requires special authorization even for internal VA applications.

*Coverage gaps:* Only covers a subset of VistA clinical domains
(Patient, Condition, Observation, Medication, Appointment, etc.).
Does not expose FileMan's full scope — administrative files,
configuration tables, and cross-patient operational data are
all out of scope.

*FHIR vocabulary lossiness:* VA's specialized clinical vocabularies
developed over decades — drug formularies, procedure codes, clinical
reminder logic, problem list classifications — do not map cleanly
to FHIR's general-purpose resource model.

*Not a FileMan wrapper:* Lighthouse calls VistA RPCs and VPR, not
FileMan directly. It inherits all the limitations of those underlying
layers, including VPR's read-only constraint and the RPC Broker's
lack of typed schema.

**What it got right:**
Lighthouse demonstrated that there is genuine, sustained third-party
developer demand for programmatic VistA data access. Its OAuth 2.0
security model and OpenAPI documentation approach are the right
developer experience patterns.

**Lesson for this project:**
Lighthouse's read-only external constraint and FHIR lossiness
represent the market gap this project addresses. A full read-write,
FileMan-native, typed gRPC API preserves semantic fidelity that
FHIR cannot. The developer experience lessons from Lighthouse —
typed contracts, versioned APIs, clear documentation — are built
into this project's proto-first design and self-documentation
strategy.

---

### Comparative Summary

| Project | Tech | Era | R/W | Semantic Fidelity | Primary Failure Mode |
|---|---|---|---|---|---|
| RPC Broker (XWB) | Delphi/M | 1994–now | Full | None | No abstraction — raw M calls, opaque strings |
| VPR | M/RPC/JSON | 2011–now | Read-only | Medium | Read-only; patient-centric; M-side logic unextendable |
| FMQL | Python/REST | 2010–2016 | Read-only | High | Read-only; SPARQL complexity; no production scale |
| ActiveFileMan | JRuby/OVID | ~2012 | Partial | Low | ORM mismatch; bridge fragility; abandoned |
| MVDM/nodeVISTA | Node.js/nodem | 2014–2019 | Full | Highest | JS runtime mismatch; no test infra; scope creep; org failure |
| eHMP | Node.js/Java/MongoDB | 2013–2018 | Read-heavy | Medium | Sync cache inconsistency; 5-service complexity; cancelled |
| IRIS FM Mapping | ObjectScript/SQL | 2000s–now | Full | Medium | IRIS-only; SQL mismatch; migration tool not wrapper |
| VA Lighthouse | Java/HAPI FHIR | 2018–now | Read-only external | Medium | Read-only; FHIR lossiness; RPC-based not FileMan-direct |

---

### How This Project Addresses Each Failure Mode

| Failure Mode | All Prior Projects | This Project's Response |
|---|---|---|
| Read-only | VPR, FMQL, Lighthouse — no write path | Full read-write via `FILE^DIE` call-in from Phase 1 |
| No test infrastructure | None had characterization tests | Golden files + three test layers + `make test-characterization` |
| Scope creep | All grew uncontrolled past sustainability | V1 scope locked by pointer graph centrality after Phase 0 |
| Wrong runtime | JS (MVDM/eHMP), Java (eHMP/Lighthouse), Ruby (ActiveFileMan) | Go + CGo — native YottaDB C API, type-safe, concurrent |
| Sync cache inconsistency | eHMP's JDS/MongoDB cache | Direct call-in — no cache, no staleness |
| IRIS-only portability | IRIS mapping utility | `fileman.Interface` boundary — YottaDB + IRIS implementations |
| ORM mismatch | ActiveFileMan's ActiveRecord model | Interface wraps FileMan's own APIs — no ORM reimplementation |
| FHIR lossiness | eHMP, Lighthouse — clinical nuance dropped | FileMan-native proto API — no semantic loss in translation |
| Multiples ignored | All handled poorly or not at all | Recursive `^DD` traversal + `repeated` proto messages |
| Date handling | All treated as strings or proprietary types | Dedicated `dates.go` with FileMan epoch transformation |
| Eager pointer resolution | FMQL, MVDM — cascade performance failure | Explicit `resolve_pointers: bool` request flag |
| Word Processing as scalar | All failed silently on WP fields | Separate `wordproc.go` retrieval path + `repeated string` proto |
| Organizational dependency | All required VA/contractor funding | Standalone open-source project with self-contained documentation |
| No formal schema | RPC Broker, VPR — opaque responses | Proto-first design — typed contracts before implementation |
| Corpus-level normalization | None achieved cross-file normalization | Phase 0 `cmd/corpus` — semantic clustering across all files |

---

## Architecture Rationale

This section explains each major architectural decision — what it is,
why it was chosen, and which specific prior project failure mode it
addresses. Every decision has a reason grounded in the prior art
record documented in the Background section.

---

### Go + CGo + `lang.go.yottadb`

**Decision:** The Go toolchain runs inside the Docker container.
YottaDB is accessed via CGo through the official `lang.go.yottadb`
Go wrapper over the YottaDB C API.

**Why Go:**
Go is statically typed, compiles to native binaries, has first-class
concurrency primitives, and a mature gRPC ecosystem. It is suited
to high-throughput database wrapper services in a way that Node.js
(single-threaded event loop, dynamic typing) and JRuby (JVM overhead,
dynamic typing) are not.

MVDM used Node.js + nodem. Node.js's single-threaded event loop
created concurrency issues with YottaDB's locking model during
sustained write workloads. The `nodem` binding was maintained by
a small community and had version compatibility fragility as Node.js
evolved rapidly. Go's goroutine-based concurrency model and its stable
CGo interface to C libraries eliminates both problems.

**Why CGo + `lang.go.yottadb` rather than raw CGo:**
`lang.go.yottadb` is the official YottaDB-maintained Go binding.
It provides an idiomatic Go interface over the YottaDB C API,
handles M data type conversions, and manages the YottaDB call-in
environment setup. Writing raw CGo bindings to `libyottadb.so`
directly would be equivalent to reimplementing `lang.go.yottadb`
from scratch — a significant, risky investment in a problem already
solved by the YottaDB team.

**Why inside the container:**
The YottaDB C API requires `libyottadb.so` to be present at compile
time. The shared library, C headers, and the live VistA environment
are all inside the `yottadb/octo-vehu` container. Go must co-locate
with YottaDB to compile CGo-linked code.

---

### gRPC + Protocol Buffers

**Decision:** The external API is gRPC with proto-defined message
and service types. Proto files are the source of truth for the API
contract. Code is generated from proto, not the reverse.

**Why gRPC over REST/JSON:**
Every prior VistA wrapper used REST/JSON — FMQL, MVDM, eHMP,
Lighthouse. REST/JSON has no schema enforcement at the transport
layer. Consumers receive whatever the server sends. Type mismatches
are discovered at runtime, not at compile time.

gRPC enforces the proto contract at the transport layer. A client
compiled against version 1.0 of the proto cannot accidentally receive
a field added in version 2.0 without an explicit schema migration.
Breaking changes are detected by `buf breaking` before deployment.
This is the typed contract the RPC Broker never had and that MVDM's
REST API could not enforce.

**Why proto-first:**
The proto files define what the API does before any implementation
is written. This inverts the typical legacy wrapper pattern —
where the implementation defines what gets exposed — and forces
explicit API design decisions before encountering FileMan's complexity.
Every field in every proto message is a deliberate choice, not an
accidental reflection of FileMan internals.

**Why `buf` over raw `protoc`:**
`buf` manages plugin versions, enforces proto lint rules, detects
breaking changes automatically, and generates code with a single
command. Raw `protoc` requires manual flag management, separate
plugin installation, and has no built-in lint or breaking change
detection. The operational overhead of `protoc` at scale is not
justified when `buf` solves all the same problems more reliably.

---

### `fileman.Interface` — The Portability Boundary

**Decision:** All FileMan access — read, write, query, call-in —
goes through a single Go interface. No code outside
`internal/fileman/yottadb/` or `internal/fileman/iris/` is permitted
to import `lang.go.yottadb` directly.

**Why:**
VistA runs on both YottaDB and IRIS. Both run the same FileMan code.
Both speak FileMan's M APIs. The database access layer differs;
the FileMan semantics are identical.

IRIS is the commercial runtime used by many VA-adjacent healthcare
organizations and by InterSystems' own healthcare products. A wrapper
that is YottaDB-only eliminates a significant portion of the potential
deployment base from day one.

The IRIS stub — a compile-time interface check that returns
`ErrNotImplemented` for all methods — costs almost nothing to
maintain and enforces portability structurally. If the interface
compiles, the portability contract is upheld.

**Phase 1 vs Phase 2:**
Phase 1 (now) delegates all FileMan operations to proven M routines
via `lang.go.yottadb` call-in. FileMan's own APIs encode the correct
semantics — `DIQ^DIQ`, `FILE^DIE`, `FIND^DIC` have been production-
tested for decades. Reimplementing FileMan semantics in Go without
deep FileMan knowledge is high-risk.

Phase 2 (later) moves FileMan semantics into Go after deep
understanding is established through Phase 1 development,
characterization testing, and the `docs/fileman/` discovery corpus.
The interface boundary does not change between phases — only the
implementation behind it moves.

---

### Phase 0 — Corpus Analysis Before Any Wrapping

**Decision:** Before wrapping a single FileMan file, run a full
corpus analysis of the entire `^DD` data dictionary — all files,
all fields, all pointer relationships — and establish a normalized
shared type library.

**Why:**
MVDM started wrapping files ad-hoc, domain by domain, without a
corpus-level view. It discovered naming inconsistencies, pointer
dependencies, and type ambiguities per-file as it went. By the time
the scope of the normalization problem was visible, hundreds of
per-file decisions had already been made inconsistently.

Phase 0 inverts this. The full `^DD` is introspected first. A
semantic clustering pipeline (heuristic + Claude API embedding)
identifies concepts that appear across multiple files under different
names. A shared type library (`api/proto/common/types.proto`) is
generated from the corpus before the first per-file proto is written.
Every subsequent file wrapping starts from a consistent type
foundation rather than discovering consistency problems retroactively.

**The threshold parameter:**
The shared type threshold — how many files a concept must appear in
to qualify as a shared type — is configurable (`make corpus THRESHOLD=N`).
Running at multiple thresholds and comparing the resulting domain
review documents allows deliberate scope decisions before any code
is committed.

---

### Characterization-First Development

**Decision:** Before writing any wrapper implementation, record
actual FileMan API behavior against the live VistA instance as
golden test fixtures. Implementation is written to match the
golden files, not assumptions about what FileMan does.

**Why:**
MVDM had no characterization testing. Normalization logic was written
based on developer assumptions about FileMan behavior. When those
assumptions were wrong — and they frequently were, because FileMan
has 40 years of undocumented edge cases — bugs were silent. There
was no ground truth to compare against.

The golden file approach (pioneered at Google for hermetic testing)
records actual system behavior as the ground truth. A failing
characterization test means FileMan changed — not that the wrapper
is wrong. A failing unit test means the wrapper does not match its
golden file — not that FileMan is doing something unexpected.
The two failure modes are separated cleanly.

**Why hash-named files + `index.json`:**
Hash naming (`DIQ-DIQ-a3f2c891.json`) makes golden file names
deterministic and collision-free. The same call always produces
the same filename. `index.json` provides the human-readable
description alongside each hash, so the corpus is navigable
without decoding filenames. This is the production pattern used
by large-scale hermetic test suites.

---

### Three Test Layers

**Decision:** Three distinct test layers — unit tests (golden files,
no YottaDB, always runs in CI), characterization tests (live YottaDB,
call-in only, container only), integration tests (live YottaDB,
full gRPC stack, container only).

**Why:**
Every prior VistA wrapper conflated test concerns. If a test failed,
the cause was ambiguous — was it a wrapper bug, a FileMan behavior
misunderstanding, or a stack integration problem?

Three layers with build tags enforces explicit test classification:

- Unit test fails → wrapper translation bug
- Characterization test fails → FileMan behavior changed
- Integration test fails (unit passes) → stack integration issue

This clarity is not academic — it directly reduces debugging time
on a system where the source of failure (FileMan vs. wrapper vs.
stack) is genuinely ambiguous without it.

**Why golden files in CI, not live YottaDB:**
CI environments cannot run YottaDB. Every prior project that required
a live database for testing had fragile CI — tests that passed locally
and failed in CI for environmental reasons, not code reasons. Golden
files make the unit test suite hermetic. CI is fast, reliable, and
requires no VistA infrastructure.

---

### Recursive Multiple (Subfile) Handling

**Decision:** `cmd/introspect` recursively traverses `^DD` to capture
the full nested subfile structure of Multiple fields. Proto generation
produces `repeated` typed messages for every Multiple.

**Why:**
Multiples are FileMan's most clinically important structures.
Medication schedules, lab result panels, allergy reactions, visit
histories — all are stored as Multiples. Every prior wrapper project
either ignored Multiples, treated them as opaque arrays, or handled
only the first level of nesting.

The MVDM codebase shows evidence of Multiple handling being patched
in retroactively as the team discovered which clinical data was
inaccessible. By handling Multiples recursively from the first
introspection pass, this project avoids the same discovery-in-
production problem.

**Depth guard:**
Recursive traversal requires a depth limit to prevent infinite
recursion on pathological `^DD` structures. Maximum depth 5 is
the conservative safe default — no clinically significant FileMan
file has Multiple nesting deeper than 3-4 levels in practice.

---

### `dates.go` — FileMan Date Transformation

**Decision:** A dedicated Go module handles all FileMan date
conversion with epoch-aware arithmetic. Date fields are never
returned as raw FileMan format strings.

**Why:**
FileMan stores dates as `YYYMMDD.HHMMSS` where YYY = years since
1700. A date of `3010101` means January 1, 2001 — not 3,010,101.
Every prior project that treated FileMan dates as strings silently
returned wrong values to consumers who expected ISO 8601. The
IRIS FileMan Mapping Utility's dedicated `%Library.FilemanDate`
and `%Library.FilemanTimeStamp` types confirm that this is a
first-class concern requiring dedicated implementation.

FileMan also supports partial dates — year-only (`301` = 2001) and
year-month-only (`30101` = January 2001). The transformation module
must handle partial dates without guessing at missing precision.
Write-path transformation must convert ISO 8601 inputs back to
FileMan internal format for `FILE^DIE` calls.

---

### `wordproc.go` — Word Processing Separate Retrieval Path

**Decision:** Word Processing fields have a dedicated retrieval
function using `$$GET1^DIQ` with the `Z` flag. They are never
retrieved via the same code path as scalar fields.

**Why:**
Word Processing fields are multi-line text stored as numbered M
array nodes (`WP(1,0)`, `WP(2,0)`, etc.), not as scalar strings.
Retrieving them with the standard `DIQ^DIQ` call returns nothing —
or worse, silently returns an empty string where content exists.
The IRIS FileMan Mapping Utility's `wpIsList` setting confirms
that WP fields require list-oriented handling.

Clinical notes, discharge summaries, and other narrative content
live in WP fields. A wrapper that silently loses WP field content
is clinically dangerous.

---

### Explicit Pointer Resolution Semantics

**Decision:** Every read RPC accepts a `resolve_pointers: bool`
parameter. When false (default), pointer fields return only the
IEN. When true, pointer fields return both IEN and resolved
display value. No eager resolution by default.

**Why:**
FMQL and MVDM both defaulted to eager pointer resolution — following
pointer chains to return display values inline. A single PATIENT
record (File 2) has pointers to NEW PERSON (File 200), INSTITUTION
(File 4), and a dozen other files. Each of those files has further
pointers. Eager resolution of a patient record triggers dozens of
transitive database lookups. At scale, this caused cascade performance
degradation in both FMQL and MVDM.

Lazy resolution (IEN only) is the correct default. Consumers that
need display values can request them explicitly with `resolve_pointers:
true`. Consumers that need performance — bulk exports, background
processing, analytical queries — get it by default without needing
to know to request it.

---

### V1 Scope Lock by Pointer Graph Centrality

**Decision:** After Phase 0 corpus analysis, V1 scope is explicitly
locked to the highest-degree nodes in the pointer graph. No file
is added to V1 scope without a deliberate decision documented in
`CHANGES.md`. The `make corpus-scope` command provides the
centrality-ranked recommendation.

**Why:**
MVDM started with arbitrary domain selections (Patient, Allergy,
Vitals). The pointer graph of FileMan means that wrapping any one
file creates visible pressure to wrap its pointer targets — you
can wrap PATIENT but you can't return useful data without also
wrapping NEW PERSON and INSTITUTION. Without explicit scope
management, each wrapped file adds 3-5 more candidates. MVDM
grew its scope faster than it could deliver working wrappers and
eventually stalled.

Pointer graph centrality is the right heuristic. The files with the
highest in-degree (most other files pointing to them) are the shared
foundations. Wrapping File 2 (PATIENT), File 200 (NEW PERSON), and
File 4 (INSTITUTION) — the three highest in-degree nodes in VistA's
pointer graph — provides the type foundation for the vast majority
of clinical data access. Everything else builds on top.

---

### Self-Documenting Project Structure

**Decision:** Every FileMan API behavior characterized and wrapped
is documented in structured markdown files in `docs/fileman/apis/`,
cross-referenced from Go doc comments, and enforced by a pre-commit
hook. The `docs/` directory grows into the authoritative FileMan
API reference.

**Why:**
FileMan's official documentation is inconsistently maintained.
The VA FileMan Technical Manual is the most important missing
document in the VDL corpus (known gap #1). Existing documentation
describes intended behavior, not actual behavior — subtle production
edge cases are undocumented everywhere.

MVDM discovered FileMan behavior empirically but did not systematically
record it. When developers left the project, that institutional
knowledge left with them. The project's organizational failure was
amplified by the absence of a knowledge capture system.

This project makes knowledge capture a technical discipline enforced
by tooling. A pre-commit hook blocks commits that add a new wrapper
function without a corresponding `docs/fileman/apis/` entry. Code
review enforces documentation quality. Over time, `docs/fileman/`
becomes more authoritative than the VA's official documentation —
because it describes what FileMan actually does, verified against
the live system, with tests that prove it.

---

## Architecture Overview

```
minty (Linux Mint 22.3 host)
├── ~/projects/vista-grpc/
├── Docker Engine
└── VS Code + Dev Containers
    └── Container
        ├── yottadb/octo-vehu:latest-master (base)
        │   ├── VistA VEHU globals + routines
        │   ├── YottaDB runtime + libyottadb.so + C headers
        │   └── Octo SQL layer
        ├── Go toolchain + CGo + lang.go.yottadb
        ├── Developer toolkit
        │   ├── cmd/corpus       ← Phase 0: full corpus analysis
        │   ├── cmd/introspect   ← per-file ^DD → JSON
        │   ├── cmd/analyze      ← per-file normalization (corpus-informed)
        │   ├── cmd/scaffold     ← normalized schema → .proto + common types
        │   └── cmd/fileman      ← scriptable CLI + --record flag
        ├── gRPC toolchain (buf, grpcurl, Evans)
        ├── Three test layers (unit, characterization, integration)
        └── Claude Code CLI (3 roles via .claude/CLAUDE.md)
```

### Key Architectural Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Container base | `yottadb/octo-vehu` | VistA + YottaDB pre-loaded, Debian-based |
| Go + CGo | Inside container | `libyottadb.so` at compile time |
| Provider boundary | `fileman.Interface` | Both YottaDB and IRIS speak FileMan |
| Development methodology | Characterization-first | Record actual behavior before writing wrappers |
| Ground truth | Golden files | Hash-named, committed to git, never auto-updated |
| Test layers | Unit + characterization + integration | Each catches different bug classes |
| Stub generation | Separate from recording | Recording is iterative; test writing is deliberate |
| Golden file naming | Hash-based + index.json | Deterministic, collision-free, human-readable via index |
| Contract definition | Lightweight (no Pact) | Proto + annotated test cases; no framework overhead |
| Phase 0 | Corpus analysis first | Domain structure before any characterization |
| Common proto types | Scaffold-generated | `cmd/scaffold --common` from corpus |
| Documentation | Self-documenting | Capture at point of discovery |

---

## Development Methodology

Based on proven approaches from large production API wrapper projects
(Google internal APIs, Stripe SDK, AWS SDK, Thoughtworks contract testing).

### The Core Problem with Wrapping Legacy APIs

When wrapping a complex external API you don't own — like FileMan —
you face three distinct failure modes:

1. **Misunderstanding** — you think the API does X, it actually does Y
2. **Translation error** — you correctly understand the API but your wrapper misrepresents it
3. **Drift** — the API behavior changes and your wrapper silently diverges

Each failure mode requires a different test strategy. Using only
integration tests conflates all three and makes failures hard to diagnose.

### The Four-Phase Methodology

```
Phase 0 — Corpus Analysis
  Understand the full FileMan data dictionary structure
  before touching any individual API.
  One-time. Never repeated unless VistA version changes.

Phase 1 — Characterization
  Record actual FileMan API behavior against the live instance.
  Golden files become the ground truth.
  Done before writing any wrapper code.

Phase 2 — Contract Definition
  Design the gRPC API based on characterized behavior.
  Proto files reflect what FileMan actually does, not assumptions.

Phase 3 — Implementation (TDD)
  Write unit tests against golden files (hermetic, CI-safe).
  Implement wrapper until tests pass.
  Red → green against locked ground truth.

Phase 4 — Continuous Verification
  Characterization tests verify golden files still match live system.
  Integration tests verify full gRPC stack end-to-end.
  Smoke tests verify health continuously.
```

### Why This Works

**Characterization before implementation** (Feathers, "Working
Effectively with Legacy Code") means you understand what the system
does before you try to wrap it. A characterization test that fails
means FileMan changed — not that your wrapper is wrong.

**Golden files as ground truth** (Google's hermetic testing approach)
means unit tests and CI never need a live YottaDB instance. Tests
are fast, deterministic, and reproducible. A golden file change is
a visible, reviewable contract change.

**Separated test layers** means a failing test points immediately
to its cause:
- Unit test fails → wrapper translation bug
- Characterization test fails → FileMan behavior changed
- Integration test fails → stack integration issue
- Smoke test fails → runtime/deployment issue

---

## Base Docker Image

**Image:** `yottadb/octo-vehu:latest-master`
**Registry:** `download.yottadb.com`
**Size:** ~1.9 GB

### What it contains
- VistA VEHU instance — globals + routines pre-loaded
- YottaDB runtime + `libyottadb.so` + C headers
- Octo SQL layer + ROcto on port 1338
- YottaDB GUI on ports 8089-8092

### Run command (reference)
```bash
docker run -d \
  -p 2222:22 -p 1338:1338 \
  -p 8089-8092:8089-8092 -p 9430:9430 \
  --name=octo-vehu \
  download.yottadb.com/yottadb/octo-vehu:latest-master
```

### YottaDB Environment Variables
```
ydb_dist        # YottaDB installation dir
ydb_gbldir      # Path to vehu.gld
ydb_tmp         # Temp directory
ydb_routines    # M routine search path
vista_home      # VistA home directory
ydb_lct_stdnull=1
ydb_lvnullsubs=2
ydb_zquit_anyway=1
ydb_sysid=vehu
```

```bash
# First-run: find env file path
docker exec -it octo-vehu su - vehu -c 'cat ~/.bashrc'
```

---

## Repository Structure

```
vista-grpc/
├── .claude/
│   └── CLAUDE.md
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
├── cmd/
│   ├── server/main.go
│   ├── corpus/main.go          # Phase 0: full corpus analysis
│   ├── introspect/main.go      # per-file ^DD → raw JSON
│   ├── analyze/main.go         # per-file normalization
│   ├── scaffold/main.go        # proto generation + common types
│   └── fileman/main.go         # scriptable CLI + --record + --force-update
├── internal/
│   ├── fileman/
│   │   ├── interface.go
│   │   ├── yottadb/
│   │   │   ├── provider.go
│   │   │   └── provider_test.go  # golden-file-driven unit tests
│   │   └── iris/
│   │       └── provider.go       # compile-time stub
│   ├── schema/
│   │   ├── types.go
│   │   ├── introspect.go
│   │   ├── heuristics.go
│   │   ├── embeddings.go
│   │   ├── analyze.go
│   │   └── corpus.go
│   ├── golden/
│   │   ├── golden.go            # load/compare/update golden files
│   │   └── golden_test.go
│   ├── callin/
│   │   ├── callin.go
│   │   └── callin_test.go
│   └── server/
│       ├── server.go
│       └── server_test.go
├── pkg/
│   └── vista/
├── api/
│   └── proto/
│       ├── common/
│       │   └── types.proto       # shared canonical types (scaffold-generated)
│       └── fileman/              # per-file service definitions
├── gen/
│   └── fileman/
├── schema/
│   ├── raw/
│   ├── domains/
│   ├── normalized/
│   ├── corpus.json
│   └── overrides/
│       └── schema.override.json
├── test/
│   ├── golden/
│   │   └── fileman/
│   │       ├── index.json        # hash → human description map
│   │       ├── read/
│   │       │   ├── DIQ-DIQ-a3f2c891.json
│   │       │   ├── DIQ-DIQ-b7d4e102.json
│   │       │   └── DIQ-DIQ-c9a1f334.json
│   │       ├── write/
│   │       │   └── FILE-DIE-d4b2a771.json
│   │       ├── query/
│   │       │   └── FIND-DIC-e5c3b882.json
│   │       └── fields/
│   │           └── FIELDLST-DID-f6d4c993.json
│   ├── fileman/
│   │   ├── read_characterization_test.go
│   │   ├── write_characterization_test.go
│   │   └── query_characterization_test.go
│   └── integration/
│       ├── main_test.go
│       ├── read_test.go
│       ├── write_test.go
│       ├── grpc_test.go
│       └── fixtures/
│           └── test_records.go
├── docs/
│   ├── fileman/
│   │   ├── overview.md
│   │   ├── domains/
│   │   ├── shared-types.md
│   │   ├── pointer-graph.md
│   │   ├── apis/
│   │   ├── files/
│   │   └── gotchas.md
│   ├── yottadb/
│   └── grpc/
├── scripts/
│   ├── entrypoint.sh
│   ├── check-docs.sh
│   └── clean_test_records.go
├── config/
│   └── provider.yaml
├── .golangci.yml
├── .pre-commit-config.yaml
├── buf.yaml
├── buf.gen.yaml
├── go.mod
├── go.sum
├── Makefile
├── CHANGES.md
└── README.md
```

### New Directory Rationale

| Directory | Rationale |
|---|---|
| `internal/golden/` | Shared golden file load/compare/update logic. Used by all test layers. |
| `test/golden/fileman/` | Golden file corpus. Hash-named files + `index.json`. Committed to git. |
| `test/golden/fileman/index.json` | Human-readable map from hash to call description. Auto-updated by `--record`. |
| `test/fileman/` | Characterization tests. Build-tagged `characterization`. Live YottaDB, no gRPC. |

---

## Portability Design

### fileman.Interface — Portability Boundary

```go
type Interface interface {
    ReadRecord(ctx context.Context, file float64, ien string) (Record, error)
    WriteRecord(ctx context.Context, file float64, record Record) (string, error)
    ListFields(ctx context.Context, file float64) ([]Field, error)
    Query(ctx context.Context, file float64, filter Filter) ([]Record, error)
    CallRoutine(ctx context.Context, routine string, args ...string) (string, error)
}
```

### Phase 1 → Phase 2 Transition

```
Phase 1 (Now):   gRPC server → fileman.Interface → lang.go.yottadb call-in to M routines
Phase 2 (Later): gRPC server → fileman.Interface → Go reimplementation of FileMan semantics
```

Interface boundary unchanged in both phases. Golden files from Phase 1
characterization become the regression suite for Phase 2 reimplementation.

### IRIS Stub

```go
var _ fileman.Interface = (*Provider)(nil) // compile-time check
```

### Provider Config (config/provider.yaml)

```yaml
provider: yottadb
yottadb:
  env_file: ""
iris:
  host: ""
  port: 0
  namespace: ""
```

---

## Developer Toolkit

Five binaries. All share `internal/schema/` logic.

```
Phase 0:  cmd/corpus → schema/corpus.json + schema/domains/
Phase 1:  cmd/fileman --record → test/golden/fileman/
          cmd/fileman --gen-stubs → test/fileman/ stubs
Phase 2:  cmd/scaffold → api/proto/
Per-file: cmd/introspect → cmd/analyze → cmd/scaffold
          cmd/fileman (exploration at any stage)
```

---

## Phase 0 — Corpus Analysis

One-time. Run before characterization. Results committed to git.

### Four-Stage Pipeline

```
Stage 1 — Bulk introspection (pure YottaDB, no API)
  All files → schema/raw/file-N.json

Stage 2 — Package namespace mapping
  File numbers → VistA namespaces (DG, LR, OR, PSO, etc.)

Stage 3 — Intra-domain heuristic analysis (no API)
  Per-domain Pass 1 clustering → preliminary domain JSON

Stage 4 — Cross-domain semantic clustering (Claude API, batched)
  Batch A: by field type (Set of Codes, Pointer, Date)
  Batch B: by domain (intra-namespace groups)
  Batch C: by heuristic pre-cluster (cross-domain confirmation)
  → schema/corpus.json + schema/domains/*.json
```

### Threshold Parameter

```bash
make corpus                # default threshold (5 files)
make corpus THRESHOLD=3    # aggressive sharing
make corpus THRESHOLD=10   # conservative sharing
```

Threshold stored in `corpus.json` for traceability.

### corpus.json Shape

```json
{
  "generated": "2026-04-10",
  "vista_version": "VEHU latest-master",
  "threshold": 5,
  "stats": {
    "total_files": 342,
    "total_fields": 8741,
    "domains": 29,
    "shared_type_candidates": 87
  },
  "domains": {
    "DG": {
      "name": "Registration",
      "files": [2, 3, 43],
      "shared_types": ["PersonName", "ClinicalDate", "SexCode"]
    }
  },
  "shared_types": [
    {
      "canonical_name": "PersonName",
      "proto_type": "PersonName",
      "appears_in_files": [2, 3, 52, 200],
      "appears_in_domains": ["DG", "OR"],
      "confidence": "high",
      "source": "semantic_cluster",
      "loose_exceptions": {
        "52": "formatted display name — override to string"
      }
    }
  ],
  "pointer_graph": {
    "2": ["200", "4", "13"]
  }
}
```

### Phase 0 Human Review

After `make corpus`:
1. Review `docs/fileman/domains/` — Claude-drafted domain docs
2. Review `docs/fileman/shared-types.md` — shared type library
3. Review `docs/fileman/pointer-graph.md` — dependency map
4. Edit `schema/overrides/schema.override.json` — corrections
5. Re-run with different thresholds if needed
6. `make scaffold-common` → `api/proto/common/types.proto`
7. Review + finalize common types
8. Commit Phase 0 artifacts

---

## Phase 1 — Characterization

Characterization happens before writing any wrapper code.
Record actual FileMan behavior. Lock it as ground truth.
Understand what the API really does.

### `cmd/fileman --record` Flag

Records actual FileMan API response to a golden file.
Two steps — recording and stub generation — are deliberately separate:

**Step 1 — Record (iterative, exploratory)**

```bash
# Standard read — all fields, external format
fileman read --file=2 --ien=1 --record

# Internal format (flags="I")
fileman read --file=2 --ien=1 --flags=I --record

# Non-existent IEN — records empty map response
fileman read --file=2 --ien=99999 --record

# Required field missing on write
fileman write --file=2 --data='{"0.02":"M"}' --record

# Query
fileman query --file=2 --field=".01" --value="ZZZRETIRED%" --record

# Direct call-in
fileman call --routine="DIQ^DIQ" --args="2^1^*^" --record
```

Each call:
1. Executes the FileMan operation against live VistA
2. Captures full input + output
3. Computes `sha256(canonical_params)[:8]` as filename
4. Writes `test/golden/fileman/{op}/{API}-{hash}.json`
5. Updates `test/golden/fileman/index.json`

**Step 2 — Stub generation (deliberate, after review)**

After recording a set of golden files and reviewing them:

```bash
# Generate stub characterization + unit test files for an API
make gen-stubs API=DIQ-DIQ
# Writes test/fileman/DIQ_DIQ_characterization_test.go (stubs)
# Writes internal/fileman/yottadb/DIQ_DIQ_unit_test.go (stubs)
# Stubs reference golden files by hash
# Developer fills in assertions
```

Separation rationale: recording is fast and iterative — you record
many variants before knowing which cases matter. Test writing is
deliberate — you decide which behaviors need assertions after
reviewing the recordings. Coupling them produces unwanted stubs
during exploration.

### Golden File Shape

```json
{
  "recorded": "2026-04-10",
  "vista_version": "VEHU latest-master",
  "api": "DIQ^DIQ",
  "hash": "a3f2c891",
  "input": {
    "file": 2,
    "ien": "1",
    "fields": "*",
    "flags": ""
  },
  "output": {
    "fields": {
      "0.01": "ZZZRETIRED,PATIENT",
      "0.02": "M",
      "0.03": "1930101"
    },
    "error": null
  },
  "notes": "Standard read — all fields, external format"
}
```

### index.json — Human-Readable Key

```json
{
  "DIQ-DIQ-a3f2c891": {
    "description": "file 2, IEN 1, all fields, external format",
    "api": "DIQ^DIQ",
    "file": 2,
    "ien": "1",
    "fields": "*",
    "flags": "",
    "recorded": "2026-04-10"
  },
  "DIQ-DIQ-b7d4e102": {
    "description": "file 2, IEN 1, all fields, internal format",
    "api": "DIQ^DIQ",
    "file": 2,
    "ien": "1",
    "fields": "*",
    "flags": "I",
    "recorded": "2026-04-10"
  },
  "DIQ-DIQ-c9a1f334": {
    "description": "file 2, IEN 99999, non-existent — empty map",
    "api": "DIQ^DIQ",
    "file": 2,
    "ien": "99999",
    "fields": "*",
    "flags": "",
    "recorded": "2026-04-10"
  }
}
```

`index.json` is auto-updated by every `--record` call.
It is the human-readable window into the golden file corpus.

### Golden File Discipline

Golden files are **never automatically updated**.
A change requires:
1. Deliberate `make golden-update` command (see Makefile)
2. Diff reviewed in code review
3. Reason documented in `CHANGES.md`

A golden file change = a contract change.
Treated with same seriousness as a proto breaking change.

If a characterization test fails:
- FileMan behavior has changed (VistA update)
- OR your recording environment was wrong
- Either way — understand the change before updating

### Characterization Workflow Per API

```
1. make characterize-record FILE=2 API=read
   → records standard cases to golden files

2. make characterize-record FILE=2 API=read FLAGS=I
   → records internal format case

3. make characterize-record FILE=2 API=read IEN=99999
   → records non-existent IEN case (empty map — not error)

4. Review golden files in test/golden/fileman/read/
   → understand actual FileMan behavior
   → note surprises and edge cases

5. Document findings in docs/fileman/apis/DIQ.md

6. make gen-stubs API=DIQ-DIQ
   → generates stub test files

7. Fill in assertions in stubs
   → characterization tests describe FileMan behavior
   → unit test stubs describe wrapper behavior
```

---

## Phase 2 — Contract Definition

Design the gRPC API from characterized behavior.
Proto files reflect what FileMan actually does.

### Post-Phase 0 + Phase 1 Scaffold

```bash
make scaffold FILE=2
# Uses: schema/normalized/file-2-patient.json (corpus-informed)
#       test/golden/fileman/ (characterized edge cases noted as comments)
# Writes: api/proto/fileman/file_2_patient.proto
```

Generated proto includes characterization-informed annotations:

```protobuf
// FileMan File: 2 (PATIENT)
// Characterized: 2026-04-10
// Key characterization findings:
//   - ReadRecord returns empty message (not error) for non-existent IEN
//   - All field values returned as strings regardless of ^DD type
//   - Pointer fields return internal IEN, not display value
//   - WriteRecord requires field .01 (NAME) — returns error if missing

service PatientService {
  // GetPatient returns empty PatientRecord (not error) for unknown IEN.
  // See golden: DIQ-DIQ-c9a1f334.json
  rpc GetPatient(GetPatientRequest) returns (PatientRecord);

  rpc WritePatient(WritePatientRequest) returns (WritePatientResponse);
  rpc ListPatientFields(ListFieldsRequest) returns (ListFieldsResponse);
  rpc QueryPatients(QueryRequest) returns (QueryResponse);
}
```

---

## Phase 3 — Implementation

TDD against golden files. Unit tests are hermetic and CI-safe.

### Characterization Test Pattern

```go
// test/fileman/read_characterization_test.go
//go:build characterization

// TestCharacterize_DIQ_Read_File2_IEN1 verifies live FileMan behavior
// matches the golden file recorded on 2026-04-10.
//
// If this test fails:
//   - FileMan behavior has changed — understand why before updating golden
//   - Update golden deliberately with: make golden-update HASH=a3f2c891
//   - Document the change in CHANGES.md
func TestCharacterize_DIQ_Read_File2_IEN1(t *testing.T) {
    golden := golden.Load(t, "read/DIQ-DIQ-a3f2c891.json")

    result, err := callIn("DIQ^DIQ",
        golden.Input.File,
        golden.Input.IEN,
        golden.Input.Fields,
        golden.Input.Flags)

    require.NoError(t, err)
    assert.Equal(t, golden.Output.Fields, result.Fields,
        "Live FileMan differs from golden DIQ-DIQ-a3f2c891 — "+
            "update deliberately if FileMan changed")
}

// TestCharacterize_DIQ_Read_NonExistentIEN verifies FileMan returns
// empty map (not error) for a non-existent IEN.
// This is a characterization of actual FileMan behavior — not
// an assumption. See golden: DIQ-DIQ-c9a1f334.json
func TestCharacterize_DIQ_Read_NonExistentIEN(t *testing.T) {
    golden := golden.Load(t, "read/DIQ-DIQ-c9a1f334.json")

    result, err := callIn("DIQ^DIQ", 2, "99999", "*", "")

    require.NoError(t, err)
    assert.Empty(t, result.Fields,
        "FileMan returns empty map for non-existent IEN — not error")
    assert.Equal(t, golden.Output.Fields, result.Fields)
}
```

### Unit Test Pattern (golden-file-driven)

```go
// internal/fileman/yottadb/provider_test.go

func TestReadRecord_MatchesGolden_StandardRead(t *testing.T) {
    g := golden.Load(t, "read/DIQ-DIQ-a3f2c891.json")
    mock := newMockCallIn(g)
    provider := NewProvider(mock)

    record, err := provider.ReadRecord(ctx, 2, "1")

    require.NoError(t, err)
    assert.Equal(t, g.Output.Fields["0.01"], record.Fields["0.01"])
}

// This test encodes a key characterization finding:
// DIQ^DIQ returns empty map for non-existent IEN — not an error.
// Golden: DIQ-DIQ-c9a1f334.json
func TestReadRecord_ReturnsEmptyRecord_WhenIENNotFound(t *testing.T) {
    g := golden.Load(t, "read/DIQ-DIQ-c9a1f334.json")
    mock := newMockCallIn(g)
    provider := NewProvider(mock)

    record, err := provider.ReadRecord(ctx, 2, "99999")

    require.NoError(t, err)
    assert.Empty(t, record.Fields,
        "Wrapper must propagate FileMan empty-map behavior — not convert to error")
}

func TestReadRecord_WrapsError_WhenCallInFails(t *testing.T) {
    mock := newMockCallInError(errors.New("YDB call failed"))
    provider := NewProvider(mock)

    _, err := provider.ReadRecord(ctx, 2, "1")

    require.Error(t, err)
    assert.Contains(t, err.Error(), "ReadRecord",
        "Errors must be wrapped with context at the FileMan boundary")
}
```

### TDD Loop

```
make gen-stubs API=DIQ-DIQ   ← generate stubs from golden files
# fill in assertions
make test-watch              ← red — wrapper not yet written
# implement wrapper
make test-watch              ← green — matches golden file behavior
make lint                    ← quality gate
```

---

## Phase 4 — Continuous Verification

### Characterization Verification

```bash
make test-characterization
# Runs test/fileman/ against live YottaDB
# Verifies golden files still match FileMan behavior
# Failure = FileMan changed — investigate before updating golden
```

### Integration Verification

```bash
make test-integration
# Full gRPC stack against live VistA
# Read-write with ZZZTEST fixture cleanup
```

### Smoke Verification

```bash
make smoke
# grpcurl health check against running server
# Fast, runs against deployed container
```

### Golden File Update (deliberate)

```bash
# Update a specific golden file after understanding a FileMan change
make golden-update HASH=a3f2c891
# Runs live FileMan call, overwrites golden file
# Shows diff, requires confirmation
# Always document in CHANGES.md
```

---

## Golden File Strategy

### Naming Convention

```
{API}-{sha256(canonical_params)[:8]}.json
```

Hash is computed from canonicalized call parameters (sorted keys,
normalized values). Deterministic — same call always produces same hash.

Examples:
```
DIQ-DIQ-a3f2c891.json    # file=2, ien=1, fields=*, flags=""
DIQ-DIQ-b7d4e102.json    # file=2, ien=1, fields=*, flags="I"
DIQ-DIQ-c9a1f334.json    # file=2, ien=99999, fields=*, flags=""
FILE-DIE-d4b2a771.json   # write file=2, data={.01:NAME,.02:M}
FIND-DIC-e5c3b882.json   # query file=2, field=.01, value=ZZZ%
```

### Location

```
test/golden/fileman/
├── index.json             # hash → human description (auto-updated)
├── read/                  # DIQ^DIQ responses
├── write/                 # FILE^DIE responses
├── query/                 # FIND^DIC responses
└── fields/                # FIELDLST^DID responses
```

### internal/golden/ — Shared Helper Package

```go
// Load a golden file for use in tests
func Load(t *testing.T, path string) *GoldenFile

// Compare result against golden output — fails test with clear message
func Compare(t *testing.T, golden *GoldenFile, actual interface{})

// Update golden file (called by make golden-update only)
func Update(path string, actual interface{}) error
```

Used by all three test layers — characterization tests, unit tests,
and integration tests all load the same golden files.

---

## Three Test Layers

```
Layer 1 — Unit tests
  File:      internal/fileman/yottadb/provider_test.go
  Build tag: none (always compiles and runs)
  Fixture:   golden files (loaded from disk, no live YottaDB)
  Verifies:  wrapper correctly translates golden file input → output
  Runs in:   everywhere — local, CI, container
  Speed:     fast (milliseconds)
  Catches:   wrapper translation bugs

Layer 2 — Characterization tests
  File:      test/fileman/*_characterization_test.go
  Build tag: //go:build characterization
  Fixture:   live YottaDB via lang.go.yottadb call-in (no gRPC)
  Verifies:  golden files still match live FileMan behavior
  Runs in:   container only, manually
  Speed:     medium (seconds)
  Catches:   FileMan behavioral drift from golden files

Layer 3 — Integration tests
  File:      test/integration/*_test.go
  Build tag: //go:build integration
  Fixture:   live YottaDB + full gRPC stack + ZZZTEST records
  Verifies:  end-to-end gRPC wrapper correctness
  Runs in:   container only, manually
  Speed:     slower (tens of seconds)
  Catches:   stack integration issues, gRPC translation errors
```

### Test Layer Decision Matrix

| I see this failure | Root cause |
|---|---|
| Unit test fails | Wrapper translation bug |
| Characterization test fails | FileMan behavior changed |
| Integration test fails, unit passes | Stack integration issue |
| All tests pass, smoke fails | Deployment / runtime issue |

---

## Dockerfile Layers

```dockerfile
FROM download.yottadb.com/yottadb/octo-vehu:latest-master

# Layer 1 — System essentials
RUN apt-get update && apt-get install -y \
    gcc make libc6-dev git curl wget unzip \
    ca-certificates sudo python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Layer 2 — Create dev user
RUN useradd -m -s /bin/bash dev \
    && usermod -aG vehu dev \
    && echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Layer 3 — Go toolchain (official binary)
ARG GO_VERSION
RUN wget -q https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz \
    && rm go${GO_VERSION}.linux-amd64.tar.gz

# Layer 4 — Go environment
ENV PATH="/usr/local/go/bin:/home/dev/go/bin:${PATH}"
ENV GOPATH="/home/dev/go"

# Layer 5 — Go dev tools
USER dev
RUN go install golang.org/x/tools/gopls@latest \
    && go install github.com/go-delve/delve/cmd/dlv@latest \
    && go install mvdan.cc/gofumpt@latest \
    && go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest \
    && go install gotest.tools/gotestsum@latest \
    && go install github.com/vektra/mockery/v2@latest \
    && go install golang.org/x/vuln/cmd/govulncheck@latest

# Layer 6 — buf
USER root
RUN wget -q \
    https://github.com/bufbuild/buf/releases/latest/download/buf-Linux-x86_64 \
    -O /usr/local/bin/buf && chmod +x /usr/local/bin/buf

# Layer 7 — grpcurl
RUN wget -q \
    https://github.com/fullstorydev/grpcurl/releases/latest/download/grpcurl_linux_amd64.tar.gz \
    -O /tmp/grpcurl.tar.gz \
    && tar -C /usr/local/bin -xzf /tmp/grpcurl.tar.gz grpcurl \
    && rm /tmp/grpcurl.tar.gz

# Layer 8 — Evans
RUN wget -q \
    https://github.com/ktr0731/evans/releases/latest/download/evans_linux_amd64.tar.gz \
    -O /tmp/evans.tar.gz \
    && tar -C /usr/local/bin -xzf /tmp/evans.tar.gz evans \
    && rm /tmp/evans.tar.gz

# Layer 9 — Node.js via nvm + Claude Code CLI
USER dev
ENV NVM_DIR="/home/dev/.nvm"
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh \
    | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install --lts && nvm use --lts \
    && npm install -g @anthropic-ai/claude-code

# Layer 10 — pre-commit
USER root
RUN pip3 install pre-commit --break-system-packages

# Layer 11 — dev user shell environment
USER dev
RUN echo 'source ${VEHU_ENV_FILE:-/usr/local/etc/ydb_env_set}' \
        >> /home/dev/.bashrc \
    && echo 'export PATH="/usr/local/go/bin:/home/dev/go/bin:${PATH}"' \
        >> /home/dev/.bashrc \
    && echo 'export GOPATH="/home/dev/go"' >> /home/dev/.bashrc \
    && echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' \
        >> /home/dev/.bashrc

WORKDIR /workspace
```

---

## Dev User

| Property | Value |
|---|---|
| Username | `dev` |
| Home | `/home/dev` |
| Shell | `/bin/bash` |
| Groups | `dev`, `vehu` |
| sudo | Passwordless (dev only) |
| GOPATH | `/home/dev/go` |

---

## Go Toolchain and TDD Stack

### Core Toolchain

| Tool | Purpose |
|---|---|
| Go (official binary) | Runtime + compiler |
| `lang.go.yottadb` | YottaDB Go wrapper |
| `gopls` | Language server — VS Code IntelliSense |
| `dlv` | Debugger — VS Code breakpoints |
| `gofumpt` | Strict formatter |

### TDD Stack

| Tool | Purpose |
|---|---|
| `go test` + `-race` | Runner + race detector |
| `testify` (go.mod) | Assertions + suites |
| `gotestsum` | Watch mode + JUnit XML |
| `mockery v2` | Mocks from `fileman.Interface` |
| `internal/golden` | Golden file load/compare/update |

### gRPC Testing

| Tool | Purpose |
|---|---|
| `grpcurl` | Scriptable smoke tests |
| Evans | Interactive REPL exploration |

Server reflection required on gRPC server.

---

## Proto Toolchain

### buf.yaml
```yaml
version: v2
modules:
  - path: api/proto
lint:
  use:
    - DEFAULT
breaking:
  use:
    - FILE
```

### buf.gen.yaml
```yaml
version: v2
plugins:
  - remote: buf.build/protocolbuffers/go
    out: gen
    opt: paths=source_relative
  - remote: buf.build/grpc/go
    out: gen
    opt: paths=source_relative
```

`gen/` checked into git — CI builds without proto toolchain.

---

## Dev Container Configuration

```json
{
  "name": "vista-grpc",
  "build": {
    "dockerfile": "./Dockerfile",
    "args": { "GO_VERSION": "1.22.x" }
  },
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspace,type=bind",
  "workspaceFolder": "/workspace",
  "remoteUser": "dev",
  "forwardPorts": [50051],
  "remoteEnv": {
    "ANTHROPIC_API_KEY": "${localEnv:ANTHROPIC_API_KEY}"
  },
  "postStartCommand": "bash scripts/entrypoint.sh",
  "customizations": {
    "vscode": {
      "extensions": [
        "golang.go",
        "zxh404.vscode-proto3",
        "bufbuild.vscode-buf",
        "ms-vscode.makefile-tools",
        "eamodio.gitlens"
      ],
      "settings": {
        "go.useLanguageServer": true,
        "go.formatTool": "gofumpt",
        "go.lintTool": "golangci-lint",
        "go.testFlags": ["-race"],
        "go.coverOnSave": true,
        "editor.formatOnSave": true
      }
    }
  }
}
```

---

## Makefile

```makefile
.PHONY: build test test-watch lint fmt vuln \
        proto proto-lint proto-breaking mock smoke ci \
        corpus introspect analyze review scaffold scaffold-common \
        characterize-record gen-stubs \
        test-characterization test-integration test-integration-clean \
        golden-update verify

THRESHOLD ?= 5

# Build
build:
	go build ./...

# Unit tests — golden files, no YottaDB, CI-safe
test:
	gotestsum --format=testname -- -race ./...

test-watch:
	gotestsum --watch -- -race ./...

# Quality
lint:
	golangci-lint run ./...

fmt:
	gofumpt -l -w .

vuln:
	govulncheck ./...

# Proto
proto:
	buf generate

proto-lint:
	buf lint

proto-breaking:
	buf breaking --against '.git#branch=main'

# Mocks
mock:
	mockery --all

# Smoke — requires running gRPC server
smoke:
	grpcurl -plaintext localhost:50051 list
	grpcurl -plaintext localhost:50051 grpc.health.v1.Health/Check

# Full local CI pass
ci: fmt lint test vuln proto-lint

# Phase 0 — full corpus analysis
# Usage: make corpus
#        make corpus THRESHOLD=3
corpus:
	go run cmd/corpus/main.go --threshold=$(THRESHOLD)
	@echo "==> Review docs/fileman/domains/ and schema/corpus.json"
	@echo "==> Edit schema/overrides/schema.override.json if needed"
	@echo "==> Then: make scaffold-common"

# Generate api/proto/common/types.proto from corpus
scaffold-common:
	go run cmd/scaffold/main.go --common
	@echo "==> Review api/proto/common/types.proto then run make proto"

# Per-file introspection
introspect:
	go run cmd/introspect/main.go --file=$(FILE)

# Per-file normalization (corpus-informed)
analyze:
	go run cmd/analyze/main.go --file=$(FILE)

analyze-local:
	go run cmd/analyze/main.go --file=$(FILE) --local-only

# Full per-file upstream review pipeline
review:
	make introspect FILE=$(FILE)
	make analyze FILE=$(FILE)
	@echo "==> Review docs/fileman/files/ for file $(FILE)"
	@echo "==> Then: make scaffold FILE=$(FILE)"

# Per-file proto scaffolding
scaffold:
	go run cmd/scaffold/main.go --file=$(FILE)

# Phase 1 — record FileMan API behavior to golden file
# Usage: make characterize-record FILE=2 OP=read IEN=1
#        make characterize-record FILE=2 OP=read IEN=1 FLAGS=I
#        make characterize-record FILE=2 OP=read IEN=99999
characterize-record:
	go run cmd/fileman/main.go \
	  $(OP) --file=$(FILE) --ien=$(IEN) --flags="$(FLAGS)" --record
	@echo "==> Golden file written. Review test/golden/fileman/index.json"

# Generate stub test files from all golden files for an API
# Usage: make gen-stubs API=DIQ-DIQ
# Run after recording and reviewing golden files.
gen-stubs:
	go run cmd/fileman/main.go --gen-stubs --api=$(API)
	@echo "==> Stubs written. Fill in assertions before running tests."

# Deliberately update a golden file after understanding a FileMan change
# Usage: make golden-update HASH=a3f2c891
# Always review the diff. Always document in CHANGES.md.
golden-update:
	go run cmd/fileman/main.go --update-golden --hash=$(HASH)
	@echo "==> Golden file updated. Review diff carefully."
	@echo "==> Document the change in CHANGES.md before committing."

# Characterization tests — verify golden files match live FileMan
test-characterization:
	gotestsum --format=testname -- \
	  -tags=characterization -race ./test/fileman/...

# Integration tests — full gRPC stack, live VistA
test-integration:
	gotestsum --format=testname -- \
	  -tags=integration -race ./test/integration/...

# Force-clean ZZZTEST records after crashed integration run
test-integration-clean:
	go run scripts/clean_test_records.go

# Full verification pipeline (container only)
verify: test-characterization test-integration smoke
```

---

## Linter Configuration

```yaml
linters:
  enable:
    - errcheck
    - staticcheck
    - gosec
    - unparam
    - gocritic
    - gofumpt
    - misspell
    - exhaustive
    - wrapcheck

linters-settings:
  errcheck:
    check-type-assertions: true
  gofumpt:
    extra-rules: true
  wrapcheck:
    ignoreSigs:
      - .Errorf(

issues:
  exclude-rules:
    - path: _test\.go
      linters: [gosec]
    - path: internal/fileman/iris/
      linters: [unparam]
    - path: test/integration/
      linters: [gosec]
    - path: test/fileman/
      linters: [gosec]
```

---

## Pre-commit Hooks

```yaml
repos:
  - repo: local
    hooks:
      - id: gofumpt
        name: gofumpt
        entry: gofumpt -l .
        language: system
        types: [go]
        pass_filenames: false

      - id: golangci-lint
        name: golangci-lint
        entry: golangci-lint run
        language: system
        types: [go]
        pass_filenames: false

      - id: buf-lint
        name: buf lint
        entry: buf lint
        language: system
        files: \.proto$
        pass_filenames: false

      - id: check-docs
        name: FileMan API doc coverage
        entry: scripts/check-docs.sh
        language: script
        types: [go]
        pass_filenames: false

      - id: go-test
        name: go test
        entry: gotestsum -- -race ./...
        language: system
        types: [go]
        pass_filenames: false
        stages: [push]

      - id: govulncheck
        name: govulncheck
        entry: govulncheck ./...
        language: system
        types: [go]
        pass_filenames: false
        stages: [push]
```

---

## Container Entrypoint

```bash
#!/bin/bash
set -euo pipefail

VEHU_ENV_FILE="${VEHU_ENV_FILE:-/usr/local/etc/ydb_env_set}"

if [ ! -f "$VEHU_ENV_FILE" ]; then
  echo "ERROR: VEHU env file not found at $VEHU_ENV_FILE"
  echo "Run: docker exec -it octo-vehu su - vehu -c 'cat ~/.bashrc'"
  exit 1
fi

source "$VEHU_ENV_FILE"

REQUIRED_VARS=(ydb_dist ydb_gbldir ydb_routines)
for var in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!var:-}" ]; then
    echo "ERROR: Required env var '$var' not set after sourcing $VEHU_ENV_FILE"
    exit 1
  fi
done

echo "==> YottaDB environment verified:"
echo "    ydb_dist:     $ydb_dist"
echo "    ydb_gbldir:   $ydb_gbldir"
echo "    ydb_routines: $ydb_routines"
echo "==> Dev environment ready."
```

---

## CI Pipeline

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version-file: go.mod
      - name: Install tools
        run: |
          go install mvdan.cc/gofumpt@latest
          go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
          go install gotest.tools/gotestsum@latest
          go install golang.org/x/vuln/cmd/govulncheck@latest
          wget -q \
            https://github.com/bufbuild/buf/releases/latest/download/buf-Linux-x86_64 \
            -O /usr/local/bin/buf && chmod +x /usr/local/bin/buf
      - run: test -z "$(gofumpt -l .)"
      - run: golangci-lint run ./...
      - run: gotestsum --format=testname -- -race ./...
      - run: govulncheck ./...
      - run: buf lint
```

**CI constraints:**
- Unit tests run against golden files — no YottaDB needed
- Characterization tests never run in CI
- Integration tests never run in CI
- Corpus analysis never runs in CI

---

## Self-Documentation Strategy

### Six Layers

**Layer 1 — Structured Go doc comments** (per wrapper function)
Includes: FileMan API, file context, gotchas, golden file references,
discovery date.

```go
// ReadRecord retrieves a record from a FileMan file by IEN.
//
// FileMan API: DIQ^DIQ
// Characterized: 2026-04-10
//
// Key behaviors (from characterization):
//   - Returns empty Record (not error) for non-existent IEN
//     See golden: DIQ-DIQ-c9a1f334.json
//   - All field values returned as strings regardless of ^DD type
//   - Pointer fields return internal IEN, not display value
//
// docs/fileman/apis/DIQ.md
```

**Layer 2 — docs/fileman/apis/** (per FileMan API)
Summary, call signature, parameters, return values, gotchas, VDL refs.
Updated with characterization findings before wrapper implementation.

**Layer 3 — docs/fileman/files/** (per FileMan file, post-corpus)
Claude-drafted, human-verified. Full field inventory, write constraints,
pointer dependencies, normalization decisions.

**Layer 4 — docs/fileman/domains/** (per VistA namespace, Phase 0)
Claude-drafted, human-verified. Domain boundary, shared types,
pointer dependencies across all domain files.

**Layer 5 — test/golden/fileman/index.json** (golden file registry)
Auto-maintained. Human-readable key to the entire characterization
corpus. The index itself is a documentation artifact.

**Layer 6 — CHANGES.md** (project journal)
One entry per session. Every golden file update documented here.

---

## Claude Code CLI Integration

### .claude/CLAUDE.md

Self-contained. Initialized from VistA VDL skill (axioms, file-index,
packages). Updated as project evolves.

After Phase 1 characterization adds:
- Confirmed FileMan API behaviors (from golden files)
- Known edge cases and gotchas (empty map on missing IEN, etc.)
- Golden file naming conventions
- Test pattern conventions

### Three Roles

**Role 1 — Project-Aware Coding Assistant**
Full context of golden file patterns, three-layer test architecture,
error wrapping conventions, doc comment format.

**Role 2 — Scaffolding Assistant**
After `make gen-stubs API=DIQ-DIQ`:
```
"Fill in characterization test assertions from golden file DIQ-DIQ-a3f2c891"
"Implement ReadRecord wrapper matching golden file behavior"
"Generate integration test stubs for ReadRecord"
```

**Role 3 — Documentation Assistant**
After characterization recordings:
```
"Generate docs/fileman/apis/DIQ.md from these golden files"
"Update CLAUDE.md with characterization findings for DIQ^DIQ"
```

---

## FileMan Knowledge Sources

### Priority Order

1. **`test/golden/fileman/`** — ground truth. Verified against live VistA.
2. **`.claude/CLAUDE.md`** — confirmed behaviors + project conventions.
3. **`docs/fileman/domains/`** — Phase 0 domain review docs.
4. **`docs/fileman/apis/`** — per-API discovery notes.
5. **`rafael5/claude` VistA VDL skill** — bootstrap. Gap: `fm22_0tm.docx`.
6. **YottaDB documentation** — `lang.go.yottadb`, call-in.
7. **VA FileMan Developer's Guide** — API signatures.

---

## MVDM / FMQL Lessons Learned

The VistA Data Project (Caregraf / nodeVISTA) built the closest prior art
to this project — a semantic overlay over FileMan's `^DD`, exposing VistA
data as JSON/REST via the FileMan Query Language (FMQL). Their goal was
a Master Veteran Data Model (MVDM) normalizing all 130 VA VistA systems
into a single model-driven interface.

The project stalled before achieving full coverage. The technical record —
from Caregraf's public writing, FMQL source code, and nodeVISTA forks —
reveals five specific failure modes directly relevant to this project.
Each has a remediation strategy applied to this spec.

---

### Lesson 1 — Multiples (Subfiles) Were Underestimated

**What happened:**
MVDM's biggest technical challenge was FileMan's Multiple field type.
Multiples are nested files-within-files, recursive, and widely used
throughout VistA. They don't map cleanly to any modern data model.
MVDM treated them as JSON arrays but underestimated their structural
complexity — Multiples have their own `^DD` entries, their own IEN
structure, their own field inventory, and can be nested multiple
levels deep.

**The problem for this project:**
The current schema types treat `^DD` fields as flat scalars. The
Multiple (`M`) type is not yet handled. This means the most structurally
complex FileMan data — medication schedules, visit history, allergy
reactions, lab results — is invisible to the current `cmd/introspect`
and `cmd/analyze` pipeline.

**Remediation:**

`internal/schema/types.go` — add Multiple as a first-class type:

```go
// FieldType represents a FileMan field type code
type FieldType string

const (
    FieldTypeFreeText    FieldType = "F"
    FieldTypeNumeric     FieldType = "N"
    FieldTypeSetOfCodes  FieldType = "S"
    FieldTypePointer     FieldType = "P"
    FieldTypeDateTime    FieldType = "D"
    FieldTypeWordProc    FieldType = "W"
    FieldTypeComputed    FieldType = "C"
    FieldTypeMultiple    FieldType = "M"   // ← nested subfile
    FieldTypeUnknown     FieldType = "*"
)

// FieldDef represents a single FileMan field definition
type FieldDef struct {
    Number          float64
    Name            string
    Type            FieldType
    Required        bool
    Computed        bool
    PointerTarget   *float64
    SetValues       map[string]string
    HasInputXform   bool
    CrossRefs       []string
    // Multiple-specific — nil for non-Multiple fields
    SubfileNumber   *float64    // ^DD(file,field,0) subfile number
    SubfileSchema   *FileSchema // recursively populated
}
```

`cmd/introspect` — recursive Multiple traversal:

```
For each field with type "M":
  1. Read ^DD(file,field,0) to get subfile number
  2. Recursively introspect the subfile as a nested FileSchema
  3. Attach as SubfileSchema on the parent FieldDef
  4. Track depth to prevent infinite recursion (max depth: 5)
```

`cmd/scaffold` — Multiple → proto `repeated` message:

```protobuf
// Multiple field: DIAGNOSIS (file 2, field 10)
// Subfile: 2.01
message DiagnosisEntry {
  string ien = 1;
  string diagnosis = 2;           // .01 — diagnosis name
  google.protobuf.Timestamp date = 3; // .02 — date entered
}

message PatientRecord {
  // ...
  repeated DiagnosisEntry diagnoses = 10;  // Multiple field
}
```

**Golden file implications:**
Characterization of Multiple fields requires separate recording
of subfile entries. `make characterize-record` needs a `--subfile`
flag for recording nested subfile data.

---

### Lesson 2 — FileMan Date Format Requires Active Transformation

**What happened:**
MVDM spent significant engineering effort on date normalization.
FileMan stores dates internally as a numeric `YYYMMDD.HHMMSS` format
where YYY = years since 1700 (e.g. 2981231 = December 31, 1998).
Externally, FileMan renders them as `DEC 31, 1998`. Neither format
is ISO 8601. The external format cannot be parsed reliably. The
internal format requires a known epoch offset. MVDM had to handle
partial dates (year-only, year-month-only), the `T` (today) shorthand,
and the `T+N`/`T-N` relative date syntax on write.

**The problem for this project:**
The current spec flags Date fields as `// TODO: consider Timestamp`.
This is insufficient. Every Date field requires an active transformation
— not just a type annotation. Without this, the wrapper silently returns
wrong data on every date read and silently writes garbage on every
date write.

**Remediation:**

Add dedicated date normalization to `internal/schema/heuristics.go`:

```go
// FileMan internal date format: YYYMMDD.HHMMSS (YYY = years since 1700)
// FileMan epoch: January 1, 1700
// Example: 3010101 = January 1, 2001
// Example: 2981231 = December 31, 1998
// Partial dates: 301 = year 2001 only, 30101 = January 2001
const FileManEpochYear = 1700

// DateNormalization describes how to transform a FileMan date field
type DateNormalization struct {
    InternalFormat  string   // "YYYMMDD.HHMMSS"
    ExternalFormat  string   // "MMM DD, YYYY@HH:MM"
    SupportsPartial bool     // year-only or year-month-only dates
    ProtoType       string   // "google.protobuf.Timestamp" or "string"
    Notes           string
}
```

Add to `cmd/analyze` Pass 1 heuristics:
- All `D` type fields → `DateNormalization` annotation
- Flag partial date support (year-only dates common in older records)
- Flag write-path transformation requirement

Add `internal/fileman/yottadb/dates.go`:
- `ParseFileManDate(internal string) (time.Time, bool, error)` — bool = isPartial
- `FormatFileManDate(t time.Time, partial bool) string`
- Unit tested against golden files recording both `I` and external formats

**Characterization requirement:**
For every Date field, record two golden files:
```bash
make characterize-record FILE=2 OP=read IEN=1           # external format
make characterize-record FILE=2 OP=read IEN=1 FLAGS=I   # internal format
```
Both golden files required before implementing any date wrapper.

---

### Lesson 3 — Pointer Resolution Strategy Must Be an Explicit API Decision

**What happened:**
MVDM defaulted to eager pointer resolution — following pointer chains
to return display values inline. This created cascading performance
problems at scale. A single patient record could trigger dozens of
transitive pointer lookups. The PATIENT file (2) alone has pointers
to NEW PERSON (200), INSTITUTION (4), and many others, each of which
has further pointers.

The eventual lesson was that pointer resolution is a consumer choice,
not a default behavior. Some consumers want IENs for subsequent lookups.
Some want resolved display values for display. Some want both.
Embedding the resolution decision in the wrapper hard-coded the wrong
default for many consumers.

**The problem for this project:**
The current spec notes pointer fields with `// TODO: consider typed
reference` but doesn't define resolution semantics. This decision must
be made during Phase 2 contract definition — not deferred to
implementation.

**Remediation:**

Define explicit pointer resolution semantics in the proto API:

```protobuf
// PointerField carries both the IEN and optionally the resolved
// display value. Callers request resolution via GetPatientRequest.
message PointerField {
  string ien = 1;           // always present — the raw IEN
  string display = 2;       // present only if resolve=true in request
  float file_number = 3;    // the target file number — enables typed lookups
}

message GetPatientRequest {
  string ien = 1;
  bool resolve_pointers = 2;  // if true, populate display values
                               // if false (default), IEN only — fast path
}
```

Add to `cmd/analyze` normalization:
- All pointer fields → `PointerNormalization` annotation
- Record target file number
- Flag pointer depth (how many hops to a terminal value)
- Flag high-degree pointer targets (File 200, File 4) as shared types

**Characterization requirement:**
For pointer fields, record three golden files:
```bash
# IEN only (no resolution)
make characterize-record FILE=2 OP=read IEN=1 FLAGS=I

# External display value
make characterize-record FILE=2 OP=read IEN=1

# Follow pointer to target file
make characterize-record FILE=200 OP=read IEN=<resolved-ien>
```

Add `pointer_graph` depth analysis to `cmd/corpus` output:
```json
"pointer_graph": {
  "2": {
    "targets": ["200", "4", "13"],
    "max_depth": 3,
    "high_degree_targets": ["200", "4"]
  }
}
```

---

### Lesson 4 — Word Processing Fields Require a Separate Retrieval Path

**What happened:**
MVDM discovered that Word Processing fields cannot be retrieved with
the same API call as scalar fields. They require `$$GET1^DIQ` with the
`Z` flag, which returns a numbered M array (`WP(1,0)`, `WP(2,0)`, etc.)
rather than a scalar string. MVDM joined these lines with newlines and
returned a single string, which lost the line structure and created
subtle rendering differences across VistA sites.

**The problem for this project:**
The current spec maps Word Processing fields to `string` with a `// TODO`.
But the retrieval path is fundamentally different from scalar fields —
requiring a separate API call and multi-line array handling. A wrapper
that treats WP fields as scalars will silently fail on every WP field read.

**Remediation:**

Add to `internal/schema/types.go`:
```go
// WordProcNormalization describes Word Processing field handling
type WordProcNormalization struct {
    RetrievalAPI   string   // "$$GET1^DIQ with Z flag"
    ReturnFormat   string   // "numbered M array WP(N,0)"
    ProtoType      string   // "repeated string" or "string" (joined)
    JoinSeparator  string   // "\n" for joined representation
    Notes          string
}
```

All `W` type fields in `cmd/analyze` → `WordProcNormalization` annotation.

Add `internal/fileman/yottadb/wordproc.go`:
- `ReadWordProcessing(file float64, ien string, field float64) ([]string, error)`
- Separate from scalar `ReadRecord` — different call-in path
- Returns `[]string` (one element per line) — caller decides join strategy

Proto representation:
```protobuf
// Word Processing fields use repeated string to preserve line structure
message NoteText {
  repeated string lines = 1;  // one element per WP array line
}

message PatientRecord {
  // ...
  NoteText clinical_notes = 42;  // WP field
}
```

**Characterization requirement:**
WP fields need dedicated golden files:
```bash
make characterize-record FILE=2 OP=read-wp IEN=1 FIELD=42
# Records the full WP array structure, not just the scalar value
```

---

### Lesson 5 — Scope Creep Under Per-Domain Wrapping

**What happened:**
MVDM started with per-domain API wrapping (Patient, Allergy, Vital Signs,
Medications). Each domain worked well individually but the cumulative
scope was unsustainable. FileMan has hundreds of files. The pointer graph
means wrapping one domain exposes dependencies on five others. The project
accumulated coding debt faster than it delivered working APIs and
eventually stalled before reaching meaningful coverage of VistA's
clinical data.

**The problem for this project:**
Without an explicit v1 scope boundary, the same failure mode is likely.
The corpus Phase 0 analysis will reveal the full pointer graph — without
a deliberate scope decision, the temptation to follow pointers will
expand scope indefinitely.

**Remediation:**

Use pointer graph centrality from Phase 0 to define v1 scope explicitly.
The highest-degree nodes in the pointer graph are the files that unblock
the most other files. Start there, not with arbitrary domain boundaries.

Add to `cmd/corpus` output:
```json
"scope_recommendations": {
  "v1_candidates": [
    {
      "file": 2,
      "name": "PATIENT",
      "rationale": "Highest in-degree — pointed to by 31 files",
      "unblocks_domains": ["DG", "OR", "LR", "PSO"]
    },
    {
      "file": 200,
      "name": "NEW PERSON",
      "rationale": "Second highest in-degree — pointed to by 47 files",
      "unblocks_domains": ["all"]
    },
    {
      "file": 4,
      "name": "INSTITUTION",
      "rationale": "Third highest in-degree — pointed to by 23 files",
      "unblocks_domains": ["DG", "SD", "OR"]
    }
  ],
  "v1_scope_note": "Wrapping files 2, 200, and 4 provides the shared
    type foundation for 80%+ of VistA clinical data access."
}
```

Add `make corpus-scope` Makefile target:
```makefile
# Print v1 scope recommendations from corpus pointer graph analysis
corpus-scope:
	go run cmd/corpus/main.go --scope-only
```

**Discipline rule:**
V1 scope is locked after Phase 0 review. Any expansion requires an
explicit `CHANGES.md` entry with rationale. The pointer graph is
available but following it is a deliberate decision, not a default.

---

### Summary Table

| Lesson | MVDM Failure Mode | Remediation in This Spec |
|---|---|---|
| 1 — Multiples | Nested subfiles invisible or poorly handled | Recursive `^DD` traversal; `repeated` proto messages; `--subfile` characterization flag |
| 2 — Dates | Silent wrong data on every date field | Dedicated date normalization module; epoch-aware transformation; characterize both `I` and external formats |
| 3 — Pointer resolution | Eager resolution caused cascade performance failures | Explicit `resolve_pointers` request flag; `PointerField` carrying IEN + display; pointer depth in corpus |
| 4 — Word Processing | WP fields silently failed when treated as scalars | Separate `wordproc.go` retrieval path; `repeated string` proto type; dedicated WP characterization |
| 5 — Scope creep | Per-domain wrapping accumulated unbounded debt | Pointer graph centrality defines v1 scope; explicit lock after Phase 0; `make corpus-scope` |

### Impact on Implementation Order

These lessons add four new components to the implementation order:

- `internal/fileman/yottadb/dates.go` — after `provider.go` scaffold
- `internal/fileman/yottadb/wordproc.go` — after `provider.go` scaffold
- `cmd/corpus` scope recommendation output — part of Stage 4
- V1 scope lock decision — after Phase 0 review, before Phase 1

And expand `internal/schema/types.go` to include:
- `FieldTypeMultiple` with recursive `SubfileSchema`
- `DateNormalization` struct
- `WordProcNormalization` struct
- `PointerNormalization` struct with depth tracking

---

## Open Items

| Item | Action | Command |
|---|---|---|
| VEHU env file path | Find on first run | `docker exec -it octo-vehu su - vehu -c 'cat ~/.bashrc'` |
| `libyottadb.so` path | Confirm `$ydb_dist` | `docker exec -it octo-vehu su - vehu -c 'echo $ydb_dist'` |
| YottaDB C headers | Find header files | `find $ydb_dist -name '*.h'` |
| `dev` group access | Confirm vehu group | `docker exec -it octo-vehu id vehu` |
| Go version pin | Latest stable | https://go.dev/dl/ |
| `lang.go.yottadb` version | Pin in go.mod | YottaDB GitLab latest |
| Corpus total file count | Determined at runtime | Stage 1 of `make corpus` |
| Initial threshold | Start with 5, explore 3 + 10 | Compare domain outputs |
| VEHU env file in entrypoint | Update default | After first-run verification |
| Multiple max recursion depth | Confirm safe depth | Inspect deepest subfile chains in VEHU `^DD` |
| FileMan date epoch verification | Confirm 1700 epoch in VEHU | `make characterize-record FILE=2 OP=read IEN=1 FLAGS=I` on a known DOB |
| V1 scope lock | Decide after Phase 0 | Review `make corpus-scope` output |

---

## Implementation Order

### Dev Environment Setup
1. Docker install script — Docker Engine on Linux Mint 22.3
2. First-run verification — env vars, lib paths, group access
3. Dockerfile — all layers
4. `devcontainer.json`
5. `Makefile`
6. `.golangci.yml`
7. `buf.yaml` + `buf.gen.yaml`
8. `.pre-commit-config.yaml`
9. `scripts/entrypoint.sh`
10. `scripts/check-docs.sh`
11. `config/provider.yaml`

### Core Libraries
12. `internal/golden/golden.go` — load/compare/update golden files
13. `internal/schema/types.go` — all schema + corpus types
14. `internal/schema/introspect.go` — `^DD` query logic
15. `internal/schema/heuristics.go` — Pass 1 normalization rules
16. `internal/schema/embeddings.go` — Claude API batching
17. `internal/schema/analyze.go` — per-file normalization pipeline
18. `internal/schema/corpus.go` — corpus pipeline orchestration
19. `internal/callin/callin.go` — YottaDB call-in helpers
20. `internal/fileman/interface.go` — portability boundary
21. `internal/fileman/iris/provider.go` — compile-time stub

### Toolkit Binaries
22. `cmd/introspect/main.go`
23. `cmd/corpus/main.go` — Phase 0 binary
24. `cmd/analyze/main.go`
25. `cmd/fileman/main.go` — includes `--record`, `--gen-stubs`,
    `--update-golden`, `--force-update` flags
26. `cmd/scaffold/main.go` — includes `--common` flag

### Phase 0 — Corpus Analysis
27. `make corpus THRESHOLD=5`
28. Human reviews domain docs + shared types
29. Edit `schema/overrides/schema.override.json`
30. Explore `THRESHOLD=3` and `THRESHOLD=10`
31. `make scaffold-common` → `api/proto/common/types.proto`
32. Human reviews + finalizes common types
33. Commit Phase 0 artifacts

### Phase 1 — Characterization (first target file: PATIENT file 2)
34. `make characterize-record FILE=2 OP=read IEN=1`
35. `make characterize-record FILE=2 OP=read IEN=1 FLAGS=I`
36. `make characterize-record FILE=2 OP=read IEN=99999`
37. `make characterize-record FILE=2 OP=write` (various cases)
38. `make characterize-record FILE=2 OP=query` (various cases)
39. Review golden files + `index.json`
40. Document findings in `docs/fileman/apis/`
41. `make gen-stubs API=DIQ-DIQ`
42. `make gen-stubs API=FILE-DIE`
43. Fill in assertions in stub test files

### Phase 2 — Contract Definition
44. `make review FILE=2` — corpus-informed per-file analysis
45. `make scaffold FILE=2` — characterized + corpus-informed proto
46. Review + finalize proto

### Phase 3 — Implementation
47. `internal/fileman/yottadb/provider.go` — YottaDB implementation
48. Claude scaffolds unit tests from golden stubs
49. `make test-watch` — TDD loop

### Phase 4 — Verification
50. `test/integration/main_test.go` — TestMain + cleanup guard
51. Write integration tests
52. `make test-characterization`
53. `make test-integration`
54. `make smoke`

### Project Context
55. `.claude/CLAUDE.md` — VDL skill + Phase 0 + Phase 1 findings
56. Repo scaffold — `go.mod`, `CHANGES.md`, `README.md`, stub `main.go`

---

*Guide version: 9.0 — April 2026*
*Spec status: Complete — ready for implementation*
