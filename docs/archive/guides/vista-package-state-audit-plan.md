# VistA Package State and Sequence Audit & Reconciliation Automation Plan

**Subject:** Pre-installation audit of a target VistA system to predict whether a proposed patch will pass KIDS pre-install check, before submission for OIT-led installation
**Audience:** VistA package developers, patch authors, and SQA engineers
**Purpose:** Enable a developer to run a "pre-flight check" against a target VistA system *without* requiring an OIT engineer to manually load and trial-install the KID file
**Mode:** Specification only — no executable commands or scripts
**Status:** Companion document to `vista-package-lifecycle-spec-v6.md` (extracted from spec §14 in v7); reusable across patch-development efforts

---

## 1. Executive summary

When a VistA package developer proposes a new patch, the patch must eventually pass KIDS' pre-installation check on each target system. Today, that check is typically run by an OIT engineer after the developer submits the KID file — and any blocker discovered there is a round-trip: the developer fixes, resubmits, OIT re-tries.

This is wasteful. **Most KIDS pre-install blockers are predictable from a static analysis of the KID file plus a snapshot of the target system's state.** This document specifies how to perform that prediction automatically, so the developer can iterate to a clean patch *before* OIT is involved.

The proposal is a three-tier architecture:

| Tier | What it does | Who runs it | When |
|---|---|---|---|
| **1. State extractor** | M-side routine that walks `#9.4`, `#9.7`, routine 2nd lines, checksums, `^XTMP` and emits a structured snapshot of the target system | Once per refresh, by an authorized site engineer with `XUPROG` access | Periodic (weekly/monthly) or on-demand before a campaign |
| **2. KID analyzer** | External parser that reads the developer's proposed `.KID` file and extracts components, dependencies, environment-check routine references | Developer | Per patch revision |
| **3. Pre-flight engine** | External engine that consumes (snapshot + KID analysis + optional NPM data) and produces a blocker report | Developer | Per patch revision |

Output: a structured **blocker report** classifying every issue by the eight-class taxonomy (§4), with severity, evidence source, and recommended remediation. A patch with zero `error`-severity blockers is predicted to pass KIDS pre-install check; a patch with `warn`-severity blockers may pass but should be reviewed.

The state extractor is the same artifact described in `vista-package-lifecycle-spec-v6.md` §14 (originally specified for post-hoc patch-state reconciliation). This document repurposes that extractor for pre-flight prediction and adds the two missing pieces: the KID analyzer and the pre-flight engine.

**No automated remediation.** The pre-flight engine is advisory. It identifies blockers; humans fix them.

---

## 2. Background — what KIDS pre-install check actually does

To predict KIDS' pre-install check, we need to know what it does. The Kernel Systems Management KIDS User Guide (XU\*8.0) specifies the install as three phases:

### 2.1 Phase 1 — Loading transport globals

Triggered by the `Load a Distribution [XPD LOAD DISTRIBUTION]` option. KIDS:
- Creates an entry in INSTALL (#9.7) for each transport global in the distribution
- Loads transport globals into `^XTMP`
- Prompts to run the **environment check routine** for each transport global (developer-provided; if it returns failure, KIDS halts here)
- Allows the installer to print contents, compare against the current system, verify checksums

**Pre-install checks performed in Phase 1:**
- Custom environment check routine (developer-supplied)
- Optional checksum verification against published values

### 2.2 Phase 2 — Answering installation questions

Triggered by the `Install Package(s) [XPD INSTALL BUILD]` option. KIDS:
- Re-runs the environment check (which can now allow / cancel that build / cancel all builds in the distribution)
- Asks pre-install questions, standard KIDS questions, post-install questions
- Allows queue-or-direct decision

**Pre-install checks performed in Phase 2:**
- Re-runs the custom environment check
- Implicit dependency check: KIDS verifies required prior patches are installed (refuses if not)
- Implicit sequence check: KIDS detects duplicate or out-of-sequence installs
- Component conflict check: warns about options/keys/protocols already owned by a different package

### 2.3 Phase 3 — Installation

Only reached after Phase 1 and 2 pass. Components are filed; pre-install routine runs; post-install routine runs.

### 2.4 What "pre-install check" means in this document

For the purposes of this pre-flight specification, **"pre-install check" means the union of all checks performed in Phase 1 and Phase 2** — i.e. everything KIDS verifies before it begins actually filing components. This is the surface area the pre-flight engine must replicate.

A patch that gets to Phase 3 but fails there (e.g. a post-install routine errors) is *not* covered by pre-flight prediction. Those failures are runtime, not predictable from static analysis.

---

## 3. The pre-flight problem

### 3.1 From a developer's perspective

A patch developer has:
- The proposed KID file (their own work product)
- Knowledge of the package(s) the patch modifies
- Access to development VistA instances they control

But typically *not*:
- Direct programmer access to target production-like systems (test, mirror, or production)
- Authority to run `Load a Distribution` against those systems
- The ability to wait for OIT-mediated install attempts

The developer's question is: **"Will my KID install cleanly on target system X?"** Today, the path to an answer is:
1. Submit the KID
2. Wait for OIT to attempt install
3. If blocked, receive the failure reason
4. Fix and resubmit

Each round-trip is days. A typical patch goes through 3–5 round-trips before it lands cleanly. **Pre-flight prediction collapses this to seconds per iteration on the developer's side, with one upstream snapshot extraction per target system.**

### 3.2 Why "submit and see" is unacceptable

For trivial patches, "submit and see" is fine. For non-trivial patches — those touching cross-package dependencies, large data dictionary changes, or environment-sensitive logic — the iteration cost is prohibitive. Pre-flight is most valuable for exactly the patches where iteration is most painful.

There's also a governance dimension: the OIT engineer's time is the institutional bottleneck. Reducing round-trips frees OIT capacity for the actual install + verification work, where their judgment matters.

### 3.3 What pre-flight cannot predict

Pre-flight is static analysis plus state lookup. It cannot predict:
- **Phase 3 runtime failures** — pre-install routine bugs, post-install errors, data conversion crashes
- **Site-specific local code interactions** — the target's locally modified routines that the patch doesn't touch but depends on transitively
- **Performance-related failures** — install takes longer than the maintenance window
- **Operational coordination failures** — HL7 link state at install time, TaskMan job collisions, etc.

These remain risks that warrant the OIT trial-install. Pre-flight catches the predictable 80%; OIT catches the contextual 20%.

---

## 4. The eight-class blocker taxonomy

This is the core classification: every KIDS pre-install blocker falls into one of these eight classes. Pre-flight detection logic is organized around them.

### B1 — Patch dependency blockers

KIDS refuses to install if required prior patches are absent.

| Sub-class | Description | Detection (pre-flight) |
|---|---|---|
| B1a | Required prior patch in same namespace not installed | Compare KID's "Required Build" list to target's `#9.7`/`#9.4` |
| B1b | Required external patch (different namespace) not installed | Same — KID's required builds may cross namespaces |
| B1c | Required version of related package not present | Compare KID's required-package version to target `#9.4` PACKAGE version |

**Severity:** `error` — KIDS will refuse to begin installation.
**Where in the KID:** `BUILD` entry's `REQUIRED BUILD` multiple (#9.6,9).

### B2 — Patch sequence blockers

KIDS refuses to install if the patch is out of sequence.

| Sub-class | Description | Detection |
|---|---|---|
| B2a | Patch already installed (duplicate) | Look for `patch_id` in target `#9.7` with STATUS = 3 |
| B2b | Higher-numbered patch already installed (regression attempt) | Find max `patch_num` in target `#9.7` for same namespace+version; reject if KID's `patch_num` is lower |
| B2c | Test patch sequence violation — proposed test version is lower than installed test | Same logic with test designators (T1, T2…) |

**Severity:** `error` (B2b), `warn` (B2a — KIDS warns but allows re-install in some cases), `error` (B2c).

### B3 — Structural blockers

KIDS' standard checks plus the custom environment check usually verify these.

| Sub-class | Description | Detection |
|---|---|---|
| B3a | Required file (`#X`) does not exist | Compare KID's referenced file numbers to target `#1` (file of files) |
| B3b | Required field (`#X.YY`) does not exist or has wrong type | Compare KID's pre-install field references to target `^DD` |
| B3c | Required routine does not exist | Compare KID's `$$` external calls to target's routine inventory |
| B3d | Required cross-reference does not exist | Inspect target `^DD(file#, field, 1)` for indexed cross-refs |
| B3e | Required DBIA partner package not present | Compare patch's declared DBIA dependencies to target `#9.4` |

**Severity:** typically `error` — patch logic depends on these structures.
**Where in the KID:** environment check routine source code; pre-install / post-install routine source.

### B4 — Drift blockers (local modifications)

The most operationally significant class. Local modifications to routines being replaced by the patch will be silently overwritten unless detected.

| Sub-class | Description | Detection |
|---|---|---|
| B4a | Routine being replaced has been locally modified | Compute current checksum of each KID-shipped routine on target; compare to the routine's published checksum from its most recent installed patch (or from the Kernel Build Analyzer XU\*8.0\*782 reference) |
| B4b | DD being modified has had local field additions | Compare target `^DD(file#)` field count to baseline |
| B4c | Component (option/key/protocol) has been locally modified | Compare target component definition to baseline package definition |

**Severity:** `warn` (KIDS will overwrite without blocking), `error` if site policy requires preservation.
**Note:** KIDS itself does not block on B4 — it overwrites. Pre-flight should *flag* B4 because it represents a coordination requirement: the developer needs to know whether the target has local mods that will be lost.

### B5 — Component conflict blockers

KIDS detects when a component named in the patch is already owned by a different package.

| Sub-class | Description | Detection |
|---|---|---|
| B5a | Option name in patch already exists, owned by different package | Compare KID's option list to target `#19 OPTION` lookup-by-B-cross-ref |
| B5b | Security key name conflict | Same logic, `#19.1` |
| B5c | Protocol name conflict | Same logic, `#101` |
| B5d | Mail group name conflict | Same logic, `#3.8` |
| B5e | Parameter name conflict | Same logic, `#8989.51` |
| B5f | Help frame name conflict | Same logic, `#9.2` |
| B5g | List template name conflict | Same logic, `#409.61` |

**Severity:** `error` (component would be hijacked) or `warn` (KIDS may allow with override).
**Where in the KID:** `BUILD` entry's component multiples.

### B6 — Environment readiness blockers

Conditions that prevent KIDS from running mechanically.

| Sub-class | Description | Detection |
|---|---|---|
| B6a | Insufficient `^XTMP` space for the patch's backup transport global | Inspect target's `^XTMP("XPD")` size and free space; estimate patch backup footprint from KID size |
| B6b | Required global not journaled (when post-install needs journaling) | Inspect target's journaling configuration |
| B6c | TaskMan not running (post-install queues a task) | Inspect target's TaskMan status (`%ZTSK`) |
| B6d | HL7 logical link state incompatible with install | Inspect target's HL7 link configuration if patch touches HL7 |
| B6e | Insufficient routine compile workspace | Inspect target's M implementation parameters |

**Severity:** `error` for B6a, B6b, B6c when the patch needs them; `info` otherwise.
**Note:** B6 is partially environmental — some checks are KIDS-internal, some are external. Pre-flight covers the predictable subset.

### B7 — Custom environment-check blockers

The patch developer's own environment-check routine. KIDS calls it and aborts if it returns failure (sets `XPDQUIT`).

| Sub-class | Description | Detection |
|---|---|---|
| B7a | Patch-specific environment check routine sets `XPDQUIT` to abort | Statically analyze the environment check routine; identify the conditions under which it aborts; verify those conditions are not met on target |
| B7b | Environment check routine errors out (M-level error) | Same — static analysis for unhandled error paths |

**Severity:** `error` when triggered; `info` otherwise.
**Note:** B7 is the hardest to predict statically because it requires understanding M control flow in the patch's environment-check routine. Pre-flight should at minimum identify *what conditions the env check tests*, even if it can't always verify them.

### B8 — Authorization / scope blockers

These are flavor-specific and typically not encoded in the KID itself.

| Sub-class | Description | Detection |
|---|---|---|
| B8a | Installer lacks `XUPROG` key on target | Inspect target's `^XUSEC("XUPROG",DUZ)` for the planned installer |
| B8b | Installer lacks programmer access | Same logic |
| B8c | Patch is VA-OIT-only and target is non-VA flavor (WorldVistA / vxVistA) | Compare KID's distribution metadata to target's flavor declaration |
| B8d | Patch is locked to specific site list and target not on list | Compare KID's site-restriction metadata, if any |

**Severity:** `error`.
**Note:** B8 is rarely triggered in practice — most patches are not site-restricted — but pre-flight should still check.

### Summary table

| Class | Count of sub-classes | Severity range | KIDS detection phase |
|---|---|---|---|
| B1 — Patch dependency | 3 | error | Phase 2 (implicit) |
| B2 — Patch sequence | 3 | error / warn | Phase 2 (implicit) |
| B3 — Structural | 5 | error | Phase 1+2 (env check) |
| B4 — Drift | 3 | warn / error (site policy) | (KIDS does not block; pre-flight flags) |
| B5 — Component conflict | 7 | error / warn | Phase 2 (component check) |
| B6 — Environment readiness | 5 | error / info | Phase 1 + operational |
| B7 — Custom environment-check | 2 | error / info | Phase 1+2 (env check) |
| B8 — Authorization / scope | 4 | error | Phase 2 (auth) |
| **Total** | **32 sub-classes** | | |

The pre-flight engine must implement at minimum one detector per sub-class. Coverage is the metric: a pre-flight engine that handles all 32 sub-classes has reached parity with KIDS' pre-install check. Below 32, the engine has known blind spots that should be documented.

---

## 5. Sources of state needed for the audit

The pre-flight engine consumes three input streams. Sources 5.1–5.3 carry forward from the post-hoc reconciliation use case (see `vista-package-lifecycle-spec-v6.md` §14); 5.4 is unique to pre-flight.

### 5.1 Target VistA system state (six primary + three secondary)

Same enumeration as `vista-package-lifecycle-spec-v6.md` §14.2–§14.3:

| # | Source | Authoritative for | Pre-flight blocker classes that need it |
|---|---|---|---|
| 1 | `#9.7` INSTALL (`^XPD(9.7,)`) | Installed patches with STATUS, complete time, installer | B1, B2 |
| 2 | `#9.4` PACKAGE PATCH HISTORY multiple | Per-package patch index | B1, B2 |
| 3 | Routine 2nd line | Code physically present | B3c, B4a |
| 4 | Routine checksums | Code integrity vs published | B4a |
| 5 | NPM (FORUM) | National released-patch state | B1 (via dependency check), B8c |
| 6 | `^XTMP("XPD"…)` | Recent KIDS install activity, free space | B6a |
| 7 | `#9.6` BUILD | Build component definitions | B5 (cross-check component ownership) |
| 8 | `#1` (file of files), `^DD` | Files, fields, types | B3a, B3b, B3d |
| 9 | `#19`, `#19.1`, `#101`, `#3.8`, `#8989.51`, `#9.2`, `#409.61` | Component lookups for conflict detection | B5 |
| 10 | `^XUSEC(...)` | Security-key holders | B8a, B8b |
| 11 | `^%ZTSK` | TaskMan state | B6c |

### 5.2 NPM (FORUM) data

Used for B1 (cross-namespace dependencies — does the target have all patches the KID's required builds depend on?) and B8c (is the patch flagged VA-only, and is the target a VA flavor?).

### 5.3 Build Analyzer / published checksums

Used for B4a — comparing target routines against the canonical baseline to detect drift. The Build Analyzer (XU\*8.0\*782) is the existing tool that publishes routine checksums; the pre-flight engine should consume those.

### 5.4 The proposed KID file (NEW for pre-flight)

This is the new input class unique to the pre-install pre-flight use case.

A KID file declares everything KIDS needs to install. The pre-flight engine must extract:

| KID element | Source within the KID | Drives blocker check |
|---|---|---|
| Build identifier (`patch_id_full`) | `BUILD` entry .01 + version | B2 (sequence comparison) |
| Required builds | `BUILD` `REQUIRED BUILD` multiple | B1 |
| Environment check routine | `BUILD ENVIRONMENT CHECK` field | B7 (static analysis target) |
| Pre-install routine | `BUILD PRE-INSTALL ROUTINE` field | (informational — runtime blockers only) |
| Post-install routine | `BUILD POST-INSTALL ROUTINE` field | (informational — runtime blockers only) |
| Routine list | `BUILD` `ROUTINE` multiple | B4a (drift detection on each routine) |
| File list | `BUILD` `FILE` multiple | B3a, B3b (DD changes) |
| Component lists (options, keys, protocols, mail groups, parameters, list templates, help frames) | Per-component multiples in BUILD | B5 (conflict detection) |
| Distribution metadata (flavor restrictions, site lists) | Distribution header | B8c, B8d |

The KID is a structured but human-readable text file; the analyzer is a parser, not a heavy ETL.

---

## 6. Architecture — three tiers

```
┌──────────────────────────────────────────┐
│ TIER 1: M-side State Extractor            │
│                                           │
│ Runs ON TARGET VistA system               │
│ Walks #9.7, #9.4, ^XTMP, routines,        │
│ #DD, ^XUSEC, components                   │
│ Restricted to XUPROG-key holders          │
│                                           │
│ Output: target_state.json (HFS)            │
│ Cadence: weekly/monthly                    │
└────────────┬─────────────────────────────┘
             │ snapshot
             ▼
┌──────────────────────────────────────────┐    ┌─────────────────────────┐
│ TIER 3: Pre-flight Engine (external)      │ ◀── │ TIER 2: KID Analyzer     │
│                                           │    │                          │
│ Consumes target_state.json + KID analysis │    │ Parses developer's KID    │
│ Applies §4 blocker taxonomy detectors     │    │ Extracts components,      │
│ Optionally cross-checks NPM               │    │ dependencies, env-check   │
│                                           │    │ Output: kid_analysis.json │
│ Output: blocker_report.md + .csv          │    │ Cadence: per KID revision │
└──────────────────────────────────────────┘    └─────────────────────────┘
                  │
                  ▼
            Blocker report
            (developer-readable)
```

Three tiers because three concerns are genuinely orthogonal:

- Tier 1 needs M access; Tiers 2 and 3 don't
- Tier 2 needs the KID; doesn't need target state
- Tier 3 needs both Tier 1 output and Tier 2 output, plus optionally NPM data

The split is deliberate: a single developer can run Tiers 2+3 on their workstation against a state snapshot pulled by an authorized engineer at a regular cadence. This is the minimum-coordination design.

---

## 7. Tier 1 — M-side state extractor

This is identical to the extractor specified in `vista-package-lifecycle-spec-v6.md` §14.6, with two additions for pre-flight coverage.

### 7.1 Existing scope (carries from §14.6)

- Per-package: name, abbrev, namespace, version
- `#9.4` PATCH HISTORY
- `#9.7` INSTALL records (status, time, installer)
- Routine inventory: name, 2nd-line patch list, current checksum
- `^XTMP("XPD"…)` recent activity

### 7.2 Pre-flight additions

For pre-flight to detect B3, B5, B6c, B8a/b, the extractor must additionally capture:

| Additional capture | Source | Drives blocker check |
|---|---|---|
| File catalog (file numbers, names, global roots) | `#1`, `^DD` headers | B3a |
| Field catalog per file (fields used in DBIAs and patches) | `^DD(file#)` | B3b, B3d |
| Component inventory: options, security keys, protocols, mail groups, parameter definitions, list templates, help frames — name + owning package | `#19`, `#19.1`, `#101`, `#3.8`, `#8989.51`, `#9.2`, `#409.61` | B5 |
| `^XTMP` free-space estimate | M `$$` system call for global size | B6a |
| TaskMan state | `^%ZTSK` head node | B6c |
| Security-key holdings for nominated installer DUZ | `^XUSEC("XUPROG", DUZ)`, `^XUSEC("XUPROGMODE", DUZ)` | B8a, B8b |

Output: structured JSON. Suggested filename pattern `XPDREC_<site>_<YYYYMMDD>_<HHMMSS>.json`. Same as v6 §14.6.

### 7.3 Estimated runtime impact

The pre-flight additions roughly double the original extractor's runtime (from "hours on a large system" to "longer hours"). Mitigation: snapshot caching — if the pre-flight additions change less frequently than the patch state, two extracts can be on different cadences (state weekly, components monthly).

---

## 8. Tier 2 — KID file analyzer

A new artifact. Pure parsing of the KID's declarative content.

### 8.1 Implementation surface

KID files are PackMan messages with a structured but human-readable format. A parser extracts:

| Element | Format pattern | Pre-flight use |
|---|---|---|
| `BUILD` header | First line block with name/version/patch | Identifies the patch under analysis |
| `REQUIRED BUILD` multiple | Sub-block with prerequisite builds | B1 dependency list |
| `ENVIRONMENT CHECK` routine reference | Single field referencing routine name | B7 source-code analysis target |
| `PRE-INSTALL ROUTINE` reference | Single field | Informational; flagged for OIT review |
| `POST-INSTALL ROUTINE` reference | Single field | Informational |
| `ROUTINE` multiple | List of routine names + checksums | B4a drift comparison list |
| `FILE` multiple | List of file numbers + change classes (data dictionary update / data update / both) | B3a, B3b context |
| Component multiples (`OPTION`, `SECURITY KEY`, `PROTOCOL`, etc.) | Per-component list | B5 conflict check list |
| Distribution metadata | Header / footer flags for site restriction, version restriction | B8c, B8d |

### 8.2 Output format

`kid_analysis.json`:

```
{
  "build_id": "DG*5.3*1057",
  "required_builds": ["DG*5.3*1047", "DG*5.3*1052"],
  "env_check_routine": "DG531057E",
  "pre_install_routine": "DG531057P",
  "post_install_routine": "DG531057PO",
  "routines": [
     { "name": "DGADD", "shipped_checksum": "B12345678" },
     ...
  ],
  "files": [
     { "file_num": 2, "change_class": "DD+data" },
     ...
  ],
  "components": {
     "options": [...],
     "security_keys": [...],
     "protocols": [...],
     ...
  },
  "distribution_flags": {
     "va_only": false,
     "site_restricted_to": null
  }
}
```

### 8.3 Implementation language

External tool, runs on the developer's workstation. Python suggested for ecosystem alignment. No M dependency — KID files are text and can be parsed anywhere.

### 8.4 Difficulty estimate

The bulk of the parser is straightforward — KID format is line-oriented and well-documented in the KIDS Developer Guide. The hardest piece is **B7 (custom environment-check routine analysis)** because it requires reading the patch's M source code to extract conditions. A Phase-1 implementation can flag the env-check routine for human review without parsing it.

---

## 9. Tier 3 — Pre-flight engine

Consumes `target_state.json` + `kid_analysis.json` (+ optional NPM data) → emits `blocker_report.md` + `blocker_report.csv`.

### 9.1 Detector logic per blocker class

| Class | Detector logic |
|---|---|
| B1 | For each `required_build` in KID, look up `patch_id_full` in target's `#9.7` and `#9.4`. Missing → error. |
| B2 | Compare KID's `build_id` against max installed patch number in target for same namespace+version. |
| B3 | For each file/field referenced by KID, look it up in target's file catalog and `^DD` snapshot. |
| B4a | For each routine in KID, compute (target current checksum) vs (Build Analyzer published baseline). Mismatch → drift warning. |
| B5 | For each component in KID, look up its name in target's component-by-name index. If found and owned by a different package → error. |
| B6a | Estimate KID footprint (sum of routine sizes + DD size); compare to target's `^XTMP` free space. |
| B6b–B6e | Targeted checks per environmental requirement of the patch. |
| B7 | Flag env-check routine for review. Phase-2: source analysis where possible. |
| B8a/b | Compare nominated installer's `^XUSEC` against `XUPROG`, `XUPROGMODE`. |
| B8c | Compare KID's `va_only` flag against target flavor declaration. |
| B8d | Compare target site identifier against KID's `site_restricted_to`. |

### 9.2 Severity propagation

The blocker report aggregates per-class severities into a single overall verdict:

- **green** — zero error-severity blockers, zero warn-severity blockers → predicted clean install
- **yellow** — zero error-severity blockers, ≥1 warn-severity blockers → predicted to install but with caveats (typically B4 drift)
- **red** — ≥1 error-severity blocker → predicted to fail KIDS pre-install check

The developer iterates until green.

### 9.3 Cross-checking against NPM (optional)

If NPM data is available (manual export or future API), Tier 3 additionally checks:
- Are the KID's required builds themselves released in NPM (not "Entered in Error")?
- Is the proposed KID's `build_id` a sequence-allowed addition (no later test patches in NPM)?

These checks add governance-level pre-flight beyond what KIDS itself does.

---

## 10. The pre-flight blocker report

A standardized markdown document plus a machine-readable CSV.

### 10.1 Report structure

#### Section 1 — Verdict
`green` / `yellow` / `red` with a one-line summary.

#### Section 2 — Patch summary
- KID build_id, declared dependencies, component counts
- Target system identifier, snapshot date

#### Section 3 — Blockers
For each detected blocker:
- Blocker class (B1–B8 with sub-class letter)
- Severity (`error` / `warn` / `info`)
- Specific evidence (which routine, file, component, etc.)
- Source of evidence (which target-state field or KID field)
- Recommended remediation

#### Section 4 — Coverage statement
Which sub-classes the engine evaluated, which it skipped (e.g. B7 routine analysis if not implemented). Documenting blind spots is essential.

#### Section 5 — Audit metadata
Engine version, snapshot date, KID file hash, run timestamp.

### 10.2 Companion CSV

One row per blocker, suitable for ingestion into a developer's ticketing or CI system.

---

## 11. Existing tools to reuse

| Tool | Use in pre-flight | Notes |
|---|---|---|
| **VistA Build Analyzer (XU\*8.0\*782)** | B4a baseline checksums; B5 component analysis on the KID | Already does much of the structural KID analysis; the Tier-2 analyzer should call it where possible rather than reimplement |
| **`Verify Package Integrity` option** | Single-package target state snapshot | Pattern source for the Tier-1 extractor's package-level walk |
| **`Display Patches for a Package` option** | `#9.4` reading | Reference implementation |
| **VPSRT (XT\*7.3\*143)** | Routine inventory walking | Reuse routine-walking patterns |
| **VistA Patch Monitor (XT\*7.3\*98)** | Possibly already implements patch-state extraction | **Investigate before building Tier 1** — may obviate part of the implementation |
| **NPM IRM/Support reports** | NPM data ingestion | Manual export until an API exists |

The pre-flight engine **wraps and extends** these — does not replace them.

---

## 12. Phased rollout

| Phase | Scope | Output | Dependency |
|---|---|---|---|
| **0** | Investigate Build Analyzer + Patch Monitor source for existing capability | Decision: extend or build new | None |
| **1** | Tier 1 pre-flight extensions (B3, B5, B6c, B8a/b sources) on top of v6 §14 extractor | Extended state snapshot | v6 §14 Tier 1 prototype |
| **2** | Tier 2 KID analyzer — basic (everything except B7 env-check source analysis) | `kid_analysis.json` per KID | Independent of Tier 1 |
| **3** | Tier 3 pre-flight engine — covers B1, B2, B3, B5, B6, B8 | `blocker_report.md` for non-B4, non-B7 classes | Tiers 1 + 2 |
| **4** | B4 drift detection via Build Analyzer integration | Drift warnings in report | Tier 3 + Build Analyzer access |
| **5** | B7 environment-check routine analysis (statically — pattern matching, control-flow rules) | B7 detection (partial) | Tier 3 + custom analyzer |
| **6** | NPM cross-check integration | Governance-level checks | Tier 3 + NPM data ingestion |
| **7** | CI integration: pre-flight runs on every KID commit | Continuous pre-flight | Tier 3 stable |

A working pre-flight engine covering 25+ of the 32 sub-classes is plausible within ~3 months of focused work for a developer pair (one M, one Python). Full coverage (especially B7) is a longer-tail effort.

---

## 13. Out of scope (for this plan)

- **Phase-3 runtime blockers** — pre-install routine bugs, post-install errors. Not predictable from static analysis.
- **Performance prediction** — install duration vs maintenance window. Heuristic at best.
- **Cross-site fleet pre-flight** — running the engine against all sites in a region. Multi-site is a roll-up problem on top of single-site pre-flight.
- **Automated KID modification** — the engine is read-only on the KID. Developer fixes; engine re-checks.
- **Live target VistA queries** — Tier 3 always operates on a snapshot. Live coupling is rejected for governance reasons (no engine should hold authenticated programmer access to production systems).
- **Non-VistA pre-flight** — client-side installers (CPRS GUI, BCMA), web-tier installs, COTS components are not in scope. This is an M-server pre-flight tool.
- **Patch backout pre-flight** — predicting whether a back-out would succeed. Different problem; deferred.

---

## 14. Open decisions

- [ ] **Tooling ownership.** Is Tier 1 an extension of Build Analyzer (XU\*8.0\*782), Patch Monitor (XT\*7.3\*98), or a new namespace (e.g. XPDPRE)?
- [ ] **Snapshot cadence.** Weekly is sufficient for most patch-state changes; monthly may suffice for component inventory. Define per-target.
- [ ] **Snapshot governance.** Who is authorized to extract Tier 1 snapshots from production-like systems and distribute them to developers? The snapshot contains no PHI but does carry security-key holdings (B8a/b detection).
- [ ] **B7 ambition.** Phase-5 environment-check source analysis is open-ended. Decide whether to invest in M static analysis or accept B7 as a "human-review-required" flag.
- [ ] **NPM API request.** Same as v6 §14 open decision — institutional governance issue. Pre-flight increases the value of an NPM API because it makes it part of every developer's daily workflow.
- [ ] **Coverage threshold for "production-ready."** At what sub-class coverage percentage is the engine declared production-ready? Suggest 25+/32 (78%) as a working threshold.
- [ ] **CI integration model.** Should pre-flight run on every KID commit, on every PR, or only on tagged release candidates? CI cost vs developer feedback latency trade-off.

---

## 15. Relationship to companion documents

| Companion | Relationship |
|---|---|
| `vista-package-lifecycle-spec-v6.md` (and later) | This plan extends the v6 §14 reconciliation framework (post-hoc) into pre-flight prediction. The Tier 1 extractor is shared. |
| `vdl-query-patterns.md` | The discovery workflow used to identify KIDS, Build Analyzer, Patch Monitor, and VPSRT as in-scope tooling. Use the §6 recipes there to discover relevant docs when extending this plan. |
| `vdl-search-assessment.md` | Identifies the documentation infrastructure improvements that would make this plan easier to maintain (especially CSV → markdown linking). |

---

## 16. References

- [Kernel KIDS Systems Management User Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-systems-management-kids-user-guide.md) — installer-side authority for what KIDS pre-install actually does
- [Kernel KIDS Developer's Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-developer-s-guide-kids-user-guide.md) — KID format authority
- [VistA Build Analyzer Utility User Guide (XU\*8.0\*782)](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782.md) — drift detection authority
- [NPM Operational Summary](https://github.com/vistadocs/vdl/blob/main/infrastructure/npm--national-patch-module/supplement--operational-summary.md) — NPM workflow and IRM/Support reports
- [Kernel Toolkit VPSRT TM (XT\*7.3\*143)](https://github.com/vistadocs/vdl/blob/main/infrastructure/xt--kernel-toolkit/technical-manual--vista-package-size-reporting-tool-vpsrt-xt-7-3-143.md) — routine-walking patterns
- VistA Patch Monitor (XT\*7.3\*98) — supplement-only in vdl markdown corpus; full doc on VA VDL
