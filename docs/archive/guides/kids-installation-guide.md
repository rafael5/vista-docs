---
title: KIDS Installation & Uninstallation Guide
source: Kernel 8.0 Systems Management — KIDS User Guide (Aug 2025, rev 1.2)
software: Kernel 8.0 / Toolkit 7.3
audience: VistA package coordinators (ADPAC), system managers, IRMS staff
scope: Site-side install/uninstall workflow for KIDS distributions
---

# KIDS Installation & Uninstallation Guide

KIDS — the **Kernel Installation and Distribution System** — is the Kernel
8.0 facility used to package, transport, install, and recover VistA software
applications and patches. It replaced the legacy `DIFROM` export utility and
the `INIT` routines DIFROM produced. This guide condenses the site-facing
install and uninstall workflow into discrete phases, with every menu option,
file, and routine called out.

---

## Table of Contents

1. [Concepts and Terminology](#1-concepts-and-terminology)
2. [Files Touched by KIDS](#2-files-touched-by-kids)
3. [Menus and Security](#3-menus-and-security)
4. [The Three Installation Phases — Overview](#4-the-three-installation-phases--overview)
5. [Phase 1 — Pre-Installation (Loading the Distribution)](#5-phase-1--pre-installation-loading-the-distribution)
   - 5.1 Load a Distribution
   - 5.2 Verify Checksums
   - 5.3 Print Transport Global
   - 5.4 Compare Transport Global to Current System
   - 5.5 Backup a Transport Global *(critical for uninstall capability)*
   - 5.6 Recovering from an Aborted Load
6. [Phase 2 — Intra-Installation (Answering Questions)](#6-phase-2--intra-installation-answering-questions)
   - 6.1 Environment Check
   - 6.2 Pre-Install Questions
   - 6.3 Standard KIDS Questions (disabling options/protocols, queue suspense, delay)
   - 6.4 Post-Install Questions
   - 6.5 Device Selection / Queueing
   - 6.6 Re-answering Questions on a Queued Install
7. [Phase 3 — Installation Execution](#7-phase-3--installation-execution)
   - 7.1 Disable options/protocols and TaskMan suspense
   - 7.2 Pre-install routine
   - 7.3 Component install
   - 7.4 Post-install routine
   - 7.5 Re-enable options/protocols, release TaskMan
   - 7.6 Progress display and checkpoints
8. [Phase 4 — Post-Installation Verification](#8-phase-4--post-installation-verification)
   - 8.1 Verify completion via INSTALL (#9.7)
   - 8.2 Verify Package Integrity (checksums)
   - 8.3 Display Patches for a Package
9. [Restarting an Aborted Installation](#9-restarting-an-aborted-installation)
10. [Global Distributions (Special Case)](#10-global-distributions-special-case)
11. [Uninstalling a VistA Package — The Backup-Build Workflow](#11-uninstalling-a-vista-package--the-backup-build-workflow)
    - 11.1 Why KIDS has no direct "uninstall" command
    - 11.2 Pre-uninstall: create the backup build
    - 11.3 Intra-uninstall: install the backup
    - 11.4 Post-uninstall: mark status De-Installed
12. [Patch Sequencing — How KIDS Manages Order](#12-patch-sequencing--how-kids-manages-order)
    - 12.1 Why sequencing matters
    - 12.2 Mechanism A — Version-number guard at load time
    - 12.3 Mechanism B — Required Builds (declarative dependency in BUILD #9.6)
    - 12.4 Mechanism C — `$$PATCH^XPDUTL` in the environment check (programmatic dependency)
    - 12.5 Mechanism D — Multi-package distribution ordering
    - 12.6 Mechanism E — National Patch Module (NPM) sequence numbers
    - 12.7 Mechanism F — Patch Application History on PACKAGE (#9.4)
    - 12.8 Mechanism G — Rollup Patches into a Build
    - 12.9 Mechanism H — Patchman & Patch Monitor (out of scope but referenced)
    - 12.10 Site-side checklist for ordering a patch queue
13. [Programmatic Install, Backup, and Rollback](#13-programmatic-install-backup-and-rollback)
    - 13.1 What is and isn't an officially supported API
    - 13.2 Programmatic install — the `EN^XPDIJ` pattern
    - 13.3 Programmatic load — no API; three workable approaches
    - 13.4 Programmatic backup — no API; what to do instead
    - 13.5 Programmatic rollback — install backup + FileMan edit
    - 13.6 Helper APIs you'll use along the way
    - 13.7 Patchman — the supported end-to-end automation path
    - 13.8 Worked example — fully scripted patch round-trip
    - 13.9 What can go wrong
14. [Bringing a Site Current — Programmatic Patch Campaigns](#14-bringing-a-site-current--programmatic-patch-campaigns)
    - 14.1 Recommendation up front — use Patchman if you can
    - 14.2 Operating principles
    - 14.3 Five-layer architecture
    - 14.4 Layer 1 — Catalog (mirror of FORUM NPM)
    - 14.5 Layer 2 — State (read PACKAGE #9.4 patch history)
    - 14.6 Layer 3 — Planner (gap, topo-sort by SEQ # + Required Builds)
    - 14.7 Layer 4 — Executor (per-patch state machine)
    - 14.8 Layer 5 — Verifier (per-patch + end-of-campaign)
    - 14.9 Hard parts no automation handles
    - 14.10 Pre-flight checklist
15. [Utilities Reference](#15-utilities-reference)
16. [Alpha/Beta Tracking](#16-alphabeta-tracking)
17. [Quick Cheat-Sheet](#17-quick-cheat-sheet)
18. [VistA Packages and Routines Involved](#18-vista-packages-and-routines-involved)
19. [References](#19-references)

---

## 1. Concepts and Terminology

| Term | Definition |
|------|------------|
| **Transport Global** | An exported software application stored in `^XTMP`. Built from a build entry; also carries the build entry itself and (if linked) the `PACKAGE (#9.4)` entry. |
| **Build Entry** | An entry in `BUILD (#9.6)` that defines what to export — files, data, components, install questions, pre/post-install routines. |
| **Component** | Template (PRINT/SORT/INPUT), Form, Function, Bulletin, Help Frame, Routine, Option, Security Key, or Protocol. |
| **Distribution** | A Host File Server (HFS) file that contains one or more transport globals. A multi-transport-global distribution installs as a single unit. |
| **Standard Distribution** | Carries files, data, and components — i.e. a "package" or a patch. |
| **Global Distribution** | Contains exactly one transport global, which exports M globals only. Installs immediately at load time (no separate Install step). |
| **PackMan Message** | A KIDS distribution wrapped in a MailMan message (loaded via `XMPACK`). |
| **Checkpoint** | A KIDS-internal restart marker in `INSTALL (#9.7)`. Standard checkpoints exist for pre-install completion, each component type, and post-install completion; developers may define additional checkpoints inside pre/post-install routines. |

---

## 2. Files Touched by KIDS

| File # | Name | Role |
|--------|------|------|
| `9.6`  | **BUILD** | Definition of every build the developer/installer has on the system. Holds component lists, install questions, and routine checksums. Field `TRANSPORT BUILD NUMBER (#63)` (added by `XU*8.0*393`) increments every time a build is made. |
| `9.7`  | **INSTALL** | One entry per attempted install. Holds: `STATUS (#.02)`, `INSTALL COMPLETE TIME (#17)`, `INSTALL ANSWERS (#50)` multiple, `MESSAGES` word-processing field (full install log), and per-checkpoint timing. |
| `9.4`  | **PACKAGE** | Now mostly static. KIDS auto-updates only the `VERSION` multiple and, for patches, the `PATCH APPLICATION HISTORY` multiple inside it. |
| `9.8`  | **ROUTINE** | Inventory of routines on the system. Required so KIDS can store routine references as pointers rather than namespace strings. Field `CHECKSUM REPORT (#6)` flags a routine as "National" so it survives the cleanup pass of `XPD ROUTINE UPDATE`. |
| `^XTMP("XPD…")` | (global, not a FM file) | Where loaded transport globals live until installed or unloaded. |

`STATUS (#.02)` values in `INSTALL (#9.7)`:

| Code | Meaning |
|------|---------|
| 0 | Loaded from Distribution |
| 1 | Queued for Install |
| 2 | Start of Install |
| 3 | Install Completed |
| 4 | De-Installed |

---

## 3. Menus and Security

Path to KIDS: `EVE` → `Programmer Options [XUPROG]` → `Kernel Installation & Distribution System [XPD MAIN]`.

| Menu | Option Name | Lock |
|------|-------------|------|
| `[XPD MAIN]` | KIDS — Kernel Installation & Distribution System | `XUPROG` |
| `[XPD DISTRIBUTION MENU]` | Edits and Distribution (developer-side) | — |
| `[XPD UTILITY]` | Utilities | — |
| `[XPD INSTALLATION MENU]` | Installation | `XUPROGMODE` |
| `[XPD AUTOMATIC PATCHING MENU]` | Patchman | — |
| `[XTPM PATCH MONITOR MAIN MENU]` | Patch Monitor | — |

Required security keys: `XUPROG` (KIDS menu), `XUPROGMODE` (Installation submenu), `XUMGR` (some manager-only options).

---

## 4. The Three Installation Phases — Overview

KIDS installs a standard distribution in three discrete phases:

1. **Phase 1 — Load** transport globals from the distribution into `^XTMP`.
2. **Phase 2 — Answer** installation questions for each transport global.
3. **Phase 3 — Install** each transport global (pre-install → components → post-install).

Adding a verification step at the end gives a clean four-phase mental model:
load → answer → install → verify.

---

## 5. Phase 1 — Pre-Installation (Loading the Distribution)

### 5.1 Load a Distribution `[XPD LOAD DISTRIBUTION]`

The mandatory starting point. This option:

1. Opens the HFS file (or, for PackMan delivery, MailMan's `INSTALL/CHECK MESSAGE` under `Load PackMan Message [XMPACK]` does the equivalent).
2. Lists every transport global in the distribution and asks `Want to Continue with Load? YES//`.
3. Creates an `INSTALL (#9.7)` entry per transport global.
4. Loads each transport global into `^XTMP`.
5. Prompts `Want to RUN the Environment Check Routine? YES//` and runs the developer's environment check routine for each transport global. A failed check may purge the transport global from `^XTMP`.
6. Compares the version number of the incoming software to the resident version. If incoming ≤ resident, KIDS aborts that transport global.
7. Echoes the **install name** to use for Phase 2: *"Use INSTALL NAME: `<name>` to install this Distribution."* This is always the first transport global to pass its environment check.

Diskette-spanned distributions: KIDS prompts `Insert the next diskette, #2, and Press the return key` and stitches the parts together.

### 5.2 Verify Checksums in Transport Global `[XPD PRINT CHECKSUM]`

Verifies the checksum of every routine in the loaded transport global against the value in the build. Reports any mismatch. Underlying integrity API: `CHECK1^XTSUMBLD` (Toolkit), which since `XU*8.0*369` also drives the `XU CHECKSUM REPORT` site report. Since `XU*8.0*393`, the FORUM-side `ROUTINE (#9.8)` file is the gold-standard source for "before" checksums.

### 5.3 Print Transport Global `[XPD PRINT INSTALL]`

Dumps the full transport global definition — every routine, file, template, option, install question — so the installer can audit what is about to enter the system before committing.

### 5.4 Compare Transport Global to Current System `[XPD COMPARE TO SYSTEM]`

Diffs the transport global against resident equivalents. Marks differences as `* OLD *` / `* NEW *` and additions as `* ADD *`. A columnar routine compare was added by `XU*8.0*393` (requires Toolkit `XT*7.3*93`). FileMan pointer fields are exported as FREE TEXT, so they will surface as differences — these can be ignored.

### 5.5 Backup a Transport Global `[XPD BACKUP]` — *critical for uninstall capability*

Creates a build that captures the **current** state of every file, field, routine, option, protocol, template, etc. that the incoming patch is about to touch. Two flavors:

- `B` — Build (including Routines): produces a full backup build. A single-build backup is delivered as a PackMan email; a multi-package backup is delivered as a Host File. The new build's name is the original with `b` appended.
- `R` — Routines Only: produces a PackMan email containing just the existing routine source.

> **This is the only KIDS-native mechanism for "uninstall."** Run it *before* the install, save the resulting message/file, and you can restore the prior state by simply installing the backup build. See [§ 11](#11-uninstalling-a-vista-package--the-backup-build-workflow).

### 5.6 Recovering from an Aborted Load — Unload a Distribution `[XPD UNLOAD DISTRIBUTION]`

If a load fails partway through, you cannot reload until the partial state is removed. `Unload a Distribution` deletes the `INSTALL (#9.7)` entries and purges the transport globals from `^XTMP`. Enter the **first** transport global name from the original load. If the install has already started, first edit `INSTALL (#9.7)` and set `STATUS (#.02)` back to `0` (Loaded From Distribution) before unloading.

---

## 6. Phase 2 — Intra-Installation (Answering Questions)

Triggered by `Install Package(s) [XPD INSTALL BUILD]`. Use the install name KIDS reported at the end of Phase 1.

### 6.1 Environment Check

KIDS re-runs each transport global's environment check routine. The routine can:
- allow the install to proceed,
- cancel that transport global, or
- cancel the entire distribution.

### 6.2 Pre-Install Questions

Developer-defined questions read from the build's `INSTALL QUESTIONS` multiple. Typical examples: *"Run the pre-install conversion?"*, environment toggles, site identifiers.

### 6.3 Standard KIDS Questions

Asked for every transport global:

- **Disable options/protocols** — `???` lists what KIDS proposes to disable. `YES` disables them all; you may add or remove entries. **Options/protocols whose Action is `USE AS LINK FOR MENU ITEMS` are never disabled.** All scheduled options are disabled.
- **Suspend queued options in TaskMan** — yes/no.
- **Delay Install (Minutes): (0-60): 0//** — grace period after disabling, so users in disabled options can finish.

### 6.4 Post-Install Questions

Same shape as pre-install — developer-defined questions read from the build.

### 6.5 Device Selection / Queueing

Final prompt:
- pick a device → install runs immediately on that device; or
- queue it (TaskMan task `EN^XPDIJ`); or
- enter `^` to abort.

### 6.6 Re-answering Questions on a Queued Install

To re-answer questions for an install that is already queued, first delete the TaskMan task, then rerun `[XPD INSTALL BUILD]`. Your previous answers come back as defaults. Aborting an install with `^` after answering also preserves the answers as defaults for the next attempt.

All answers are stored in `INSTALL ANSWERS (#50)` of `INSTALL (#9.7)`.

---

## 7. Phase 3 — Installation Execution

Driven by `EN^XPDIJ` (the KIDS install entry point). Sequence per transport global:

1. **Disable** options/protocols requested in Phase 2 (skipping menu-link entries).
2. **Wait** the user-specified delay (0–60 min).
3. **Suspend** TaskMan-queued options if the installer chose to.
4. Run the **pre-install routine** declared in the build (e.g. `ZXGPRE`).
5. **Install all components** — files (with progress bar on VT100+), data dictionaries, data, templates, forms, help frames, bulletins, routines, options, security keys, protocols. Compiled cross-references and compiled INPUT/PRINT templates are listed as they are (re)built.
6. Run the **post-install routine** declared in the build (e.g. `ZXGPOS`).
7. Repeat steps 4–6 for each remaining transport global in the distribution.
8. **Re-enable** options/protocols.
9. **Release** suspended TaskMan-queued options.

### Progress display

On a VT100 (or higher) terminal, KIDS shows a virtual install window with a percentage progress bar. Other devices get dots. **No progress is reported for data installs or for pre/post-install routines** — only for files and components.

### Checkpoints

Every checkpoint write goes to `INSTALL (#9.7)`. Standard checkpoints: pre-install start/complete, each component-type complete, post-install start/complete. Developers may add their own checkpoints inside pre/post routines, which lets a restart resume mid-routine instead of from scratch.

---

## 8. Phase 4 — Post-Installation Verification

### 8.1 Confirm completion via INSTALL (#9.7)

Use `Install File Print [XPD PRINT INSTALL FILE]`.

- `STATUS = "Install Completed"` → success.
- `STATUS = "Install Started"` → install errored out. Read the `MESSAGES` word-processing field for the error and proceed to [§ 9](#9-restarting-an-aborted-installation).

If options/protocols were disabled, KIDS should have re-enabled them on success — verify.

### 8.2 Verify Package Integrity `[XPD VERIFY INTEGRITY]`

Compares current routine checksums against the checksums that were stored in `BUILD (#9.6)` when the software was transported. Currently routines only. **If the most recent `BUILD (#9.6)` entry has been purged, this option cannot verify** — so do not purge the latest build entry for installed software (see [§ 12](#12-utilities-reference) Purge).

### 8.3 Display Patches for a Package `[XPD PRINT PACKAGE PATCHES]`

Confirms the patch is recorded in `PACKAGE (#9.4)` `PATCH APPLICATION HISTORY` (within `VERSION` multiple). Lists patch number, install date, and installer.

After verification, follow any package-specific post-install instructions in the patch description (key activations, journaling, schedule rebuild, taskman restart, etc.).

---

## 9. Restarting an Aborted Installation

`Restart Install of Package(s) [XPD RESTART INSTALL]` resumes from the last completed checkpoint stored in `INSTALL (#9.7)` — KIDS does not restart from scratch. Procedure:

1. Use `[XPD PRINT INSTALL FILE]` to read the `MESSAGES` field and identify the failure cause.
2. Fix the underlying problem.
3. Run `[XPD RESTART INSTALL]`.

Restart works for both queued and direct installs.

---

## 10. Global Distributions (Special Case)

A global distribution carries one transport global that exports M globals only. Differences from standard install flow:

- Loaded **and installed** by `[XPD LOAD DISTRIBUTION]` in a single step — no separate Phase 2/3.
- No queueing.
- KIDS displays *"This is a Global Distribution. It contains Global(s) that will update your system at this time."*
- Each global is marked `OVERWRITE` (load over the existing global) or `REPLACE` (purge the site's global first, then load).
- Two confirmation prompts; either can abort.

---

## 11. Uninstalling a VistA Package — The Backup-Build Workflow

### 11.1 Why KIDS has no direct "uninstall" command

The KIDS Installation menu deliberately ships **no** "uninstall" or "remove package" option. The supported uninstall pattern is to install a backup build that captures the pre-install state. `Unload a Distribution` is *not* an uninstall — it only purges a loaded-but-not-yet-installed distribution from `^XTMP` and `INSTALL (#9.7)`.

The full lifecycle therefore looks like:

```
[load original]  →  [BACKUP a transport global]  →  [install original]
                                                         ↓ (later)
                                          [load + install backup build]
                                                         ↓
                                          [Edit Install Status → De-Installed]
```

### 11.2 Pre-uninstall: create the backup build (do this *before* installing the original)

1. Load the incoming distribution: `[XPD LOAD DISTRIBUTION]`.
2. Run `Backup a Transport Global [XPD BACKUP]`.
   - **Backup Type `B`** — full Build backup (recommended for any patch that touches files, options, protocols, templates, etc.). Yields a PackMan email for single-build backups, a Host File for multi-package backups. Backup name = original name + `b`.
   - **Backup Type `R`** — Routines-only backup as a PackMan email (use only if the patch is routine-only).
3. Save the resulting message/file in a safe location (PackMan basket or the Host file system).

### 11.3 Intra-uninstall: install the backup

To roll back:

1. **Load** the saved backup build via `[XPD LOAD DISTRIBUTION]` (or, for PackMan, `XMPACK` → `INSTALL/CHECK MESSAGE`).
2. Optional pre-install due diligence (matches Phase 1):
   - `[XPD PRINT INSTALL]` — review what is about to be restored.
   - `[XPD COMPARE TO SYSTEM]` — confirm the diff matches the patch you are reversing.
   - `[XPD PRINT CHECKSUM]` — confirm transport integrity.
3. Run **`Install Package(s) [XPD INSTALL BUILD]`** against the backup install name. Phases 2 and 3 proceed exactly as for a normal install.
4. The result is a system whose files, fields, routines, options, protocols, and templates are at their pre-patch state.

### 11.4 Post-uninstall: mark status De-Installed

1. Run `Edit Install Status [XPD EDIT INSTALL]` (released in `XU*8.0*539`).
2. Select the **original** patch's `INSTALL (#9.7)` entry — *not* the backup's.
3. Set `STATUS (#.02)` to `4` (De-Installed). Optionally update `INSTALL COMPLETE TIME (#17)`.
4. Verify the rollback succeeded:
   - `[XPD PRINT INSTALL FILE]` — confirm the new status.
   - `[XPD VERIFY INTEGRITY]` — confirm routine checksums match the prior build.
   - `[XPD PRINT PACKAGE PATCHES]` — confirm `PACKAGE (#9.4)` patch history reflects the rollback context.

> **Caveats.** A backup build only captures items the patch *touches*; downstream side effects of pre/post-install routines (data conversions, deletions, journaled global writes) cannot necessarily be reversed by re-installing the backup. Some patches ship explicit reversal instructions; always read the patch description before rolling back.

---

## 12. Patch Sequencing — How KIDS Manages Order

KIDS does not have a single "sequencer." Instead it composes order from **eight cooperating mechanisms** spread across build authoring, transport, environment check, install, and the national patch module on FORUM.

### 12.1 Why sequencing matters

Patches commonly modify the work of earlier patches — same routines, same fields, same options. If they install out of order:

- Pre/post-install conversions can run on data that is in the wrong shape.
- Routine source can regress (an older patch overwrites a newer one's lines).
- `PACKAGE (#9.4)` patch history becomes non-monotonic and `$$LAST^XPDUTL` no longer reflects truth.
- `[XPD VERIFY INTEGRITY]` finds checksum mismatches that have nothing to do with corruption.

KIDS therefore enforces order through a layered defense — some checks are at load time, some at environment check, some are advisory metadata that the installer is expected to honor.

### 12.2 Mechanism A — Version-number guard at load time

`Load a Distribution [XPD LOAD DISTRIBUTION]` compares the incoming software version number against the resident version. **If the incoming version is not greater than the resident version, KIDS aborts that transport global.** This is a coarse guard: it stops you from installing v1.0 over v2.0, but says nothing about patches inside the same version line.

### 12.3 Mechanism B — Required Builds (declarative dependency in BUILD #9.6)

The strongest site-side enforcement. Set on the developer side via `Edit a Build [XPD EDIT BUILD]`, screen 4 → `Required Builds` (`REQUIRED BUILD (#11)` multiple in `BUILD (#9.6)`). At install time KIDS checks the installing site's `PACKAGE (#9.4)` `VERSION (#22)` multiple and the `PATCH APPLICATION HISTORY (#9.49,1105)` multiple inside it to verify each declared prerequisite is present.

Three actions are available:

| Action | Behavior when prereq is missing |
|--------|---------------------------------|
| `WARNING ONLY` | Installer sees `**WARNING**`, install continues. |
| `DON'T INSTALL, LEAVE GLOBAL` | Install is blocked. Transport global stays in `^XTMP` so the installer can install the prereq, then resume from `[XPD INSTALL BUILD]` without re-loading. |
| `DON'T INSTALL, REMOVE GLOBAL` | Install is blocked **and** the transport global is unloaded — installer must reload from the source distribution after applying the prereq. |

For prerequisites that were *not* delivered via KIDS, the developer must still create a `BUILD (#9.6)` placeholder entry on the developer system so the comparison has something to match.

### 12.4 Mechanism C — `$$PATCH^XPDUTL` in the environment check (programmatic dependency)

Used during the **environment check phase only** (Phase 1, `Load a Distribution`). The developer's environment-check routine calls:

```
$$PATCH^XPDUTL("XU*8.0*28")  →  1 (installed) | 0 (not installed)
```

The patch name **must** include the full version with decimal point. The check works with or without sequence numbers. Companion APIs in the same family — `$$VER^XPDUTL`, `$$VERSION^XPDUTL` — let the env-check compare version numbers; `$$LAST^XPDUTL` returns the most recently applied patch number, optionally restricted to released patches (`z=1` parameter, added by `XU*8.0*559`).

Example pattern (developer side):

```mumps
I '$$PATCH^XPDUTL("XU*8.0*28") W !,"You must install patch XU*8*28" S XPDQUIT=2
```

Setting `XPDQUIT=2` cancels installation of all transport globals in the distribution; `XPDQUIT=1` cancels just the current one; `XPDABORT=1` aborts immediately. (See *Table 6 — KIDS: Actions Based on Environment Check Conclusions* in the Developer's Guide.)

This is more flexible than Required Builds because the environment check can express conditional logic: e.g. "patch X required *only if* file #200 has the FOOBAR field," or "either patch X or patch Y, not both."

### 12.5 Mechanism D — Multi-package distribution ordering

When a developer bundles multiple packages into one distribution via `Transport a Distribution [XPD TRANSPORT PACKAGE]`, the prompt is explicit:

> *"Enter the Package Names to be transported. **The order in which they are entered will be the order in which they are installed.**"*

KIDS treats the bundle as a single installation unit. At install time:

- Phase 2 (questions) runs left-to-right across the transport globals — the installer answers pre/standard/post questions for each in turn.
- Phase 3 (execute) runs each transport global's pre-install → components → post-install in order, repeating for the next.
- An environment-check failure on transport global *N* can cancel just *N* (`XPDQUIT=1`) or the entire bundle (`XPDQUIT=2`).

This is how patch chains are commonly shipped: a single distribution with patches in dependency order, so a site cannot apply them out of sequence even if they wanted to.

### 12.6 Mechanism E — National Patch Module (NPM) sequence numbers

Released VistA patches are assigned a **sequence number** by the National Patch Module on FORUM at release time. The sequence number is the canonical chronological position of that patch within its package/version line — it is what makes `KERNEL 8.0 SEQ #543` meaningful as "the 543rd released Kernel 8.0 patch."

KIDS exposes the sequence number in three places:

- **`XPDNM("SEQ")`** — KIDS key variable, available during environment check and pre/post-install. Set to the NPM sequence number for the build being installed (NULL if not a released patch). Released by `XU*8.0*559`. Companion: `XPDNM("TST")` for test numbers.
- **`PATCH APPLICATION HISTORY (#9.49,1105)`** — KIDS records the sequence number alongside the patch name when the patch installs. (Behavior added by `XU*8.0*30`; patches installed before `XU*8.0*30` show no sequence number in this multiple.)
- **`$$LAST^XPDUTL`** — returns `nnn Seq #nnn^yyymmdd` for released patches, `nnn^yyymmdd` for unreleased.

`Display Patches for a Package [XPD PRINT PACKAGE PATCHES]` then prints patches with their `SEQ #` so the installer can see whether their site is current and whether anything was skipped:

```
PATCH #          INSTALLED          INSTALLED BY
VERSION: 8.0     JUL 29, 2004       XUUSER,TEN
28               APR 25, 2004       XUUSER,NINE
20  SEQ #23      FEB 09, 2004       XUUSER,NINE
32  SEQ #24      MAY 15, 2004       XUUSER,NINE
23  SEQ #25      MAY 17, 2004       XUUSER,TEN
...
```

> **Sequence number ≠ patch number.** Patch `XU*8.0*20` may have sequence #23; patch `XU*8.0*32` may have sequence #24. Patches are issued one number at a time as they are *opened*; sequence numbers are assigned as they are *released*. Always order by sequence number, not by patch number.

### 12.7 Mechanism F — Patch Application History on PACKAGE (#9.4)

`PATCH APPLICATION HISTORY (#9.49,1105)` is the authoritative record of what has been applied at this site, in what order, by whom. It lives inside the `VERSION (#22)` multiple of the site's `PACKAGE (#9.4)` entry. Required Builds (§ 12.3) and `$$PATCH^XPDUTL` (§ 12.4) both consult this multiple. Fields written per entry:

- `PATCH APPLICATION HISTORY (#9.4901,.01)` — patch name (with sequence #).
- `DATE APPLIED (#.02)`
- `APPLIED BY (#.03)`
- `DESCRIPTION (#1)`

KIDS only writes here if the build's `PACKAGE FILE LINK` field (build screen 4) points at a `PACKAGE (#9.4)` entry. Patches that ship without a package-file link will install fine but **leave no patch history trail** — meaning subsequent patches that depend on them via `$$PATCH^XPDUTL` will get a false negative. This is the most common reason a "should be installed" patch reports as missing.

### 12.8 Mechanism G — Rollup Patches into a Build

`Rollup Patches into a Build [XPD ROLLUP PATCHES]` collapses every KIDS patch matching a software/version pair into a single `BUILD (#9.6)` definition. Useful when re-deploying a known-good baseline to a new system: instead of replaying 200 patches in order, install one rollup that contains the union of all their components.

Caveats taken from the User Guide:

- Patches in the displayed list are **not** necessarily in sequence order — verify before accepting.
- Rollups include only KIDS patches.
- **Pre/post-install routines are *not* carried into the rollup.** Patches that depended on data conversions in their post-install will not have those conversions applied if installed via the rollup. Use `Edit a Build [XPD EDIT BUILD]` to add additional patches or hook routines if needed.

### 12.9 Mechanism H — Patchman & Patch Monitor (out of scope but referenced)

The KIDS main menu (`[XPD MAIN]`) hangs two patch-orchestration submenus:

- `Patchman [XPD AUTOMATIC PATCHING MENU]` — automated patching machinery.
- `Patch Monitor Main Menu [XTPM PATCH MONITOR MAIN MENU]` — Toolkit `XT` patch-tracking dashboard.

Neither is described in the *KIDS User Guide* or the *KIDS Developer's Guide* — they are documented separately under the Patchman and Toolkit Patch Monitor user guides. Mentioned here for completeness because they are the menu entries an installer will encounter, and because Patchman is the layer that automates the sequence-driven application of multiple released patches drawn from FORUM.

### 12.10 Site-side checklist for ordering a patch queue

1. **Read each patch's description first.** Patch descriptions on FORUM (NPM) declare prerequisites in plain text — this is the canonical source of truth, ahead of any KIDS metadata.
2. **Sort by sequence number, not patch number.** Use `[XPD PRINT PACKAGE PATCHES]` to see what is already applied (with `SEQ #`) and to deduce gaps.
3. **Trust Required Builds, but verify.** A patch with `DON'T INSTALL, REMOVE GLOBAL` will protect you against a missing prereq; a patch with no required-builds entries does not mean none exist — re-read the description.
4. **Do not skip sequence numbers within a version line** unless the patch description explicitly says it is an alternative to a prior patch.
5. **Install bundled distributions in the order shipped.** Multi-package distributions are pre-ordered by the developer; do not unpack and re-order them.
6. **After each install,** run `[XPD PRINT PACKAGE PATCHES]` and confirm the new entry shows the expected `SEQ #`. Missing SEQ # means the patch was installed without a `PACKAGE FILE LINK` and will not satisfy downstream `$$PATCH^XPDUTL` checks.
7. **Use `[XPD VERIFY INTEGRITY]` after each batch** to catch a routine that a later patch silently regressed.
8. **For mass restores** (rebuilding a system), prefer a NPM-driven rollup over a hand-ordered patch queue, but be aware the rollup loses pre/post-install effects (§ 12.8).

---

## 13. Programmatic Install, Backup, and Rollback

The standard KIDS workflow is menu-driven, but every step ultimately calls M code, and parts of it are documented as APIs. This section maps what is officially supported, what isn't, and what to do for a fully unattended round-trip.

### 13.1 What is and isn't an officially supported API

| Step | API Status | Entry Point | ICR |
|------|-----------|-------------|-----|
| Run install on an already-loaded build | **Supported** | `EN^XPDIJ(XPDA)` | 2243 (Controlled Subscription) |
| Update install progress bar | Supported | `UPDATE^XPDID(n)` with `XPDIDTOT` | 2172 |
| Update PACKAGE patch history | Supported | `$$PKGPAT^XPDIP`, `$$PKGVER^XPDIP` | 2067 |
| Pre/post-install helpers (checkpoints, option/protocol toggle, messaging, version/patch checks) | Supported | `XPDUTL` family | 10141 |
| **Load a distribution** from HFS or PackMan | **No documented API** | (`^XPDIA*` routines exist, but unsupported) | — |
| **Backup a transport global** | **No documented API** | (`^XPDIB*` routines, unsupported) | — |
| **Verify checksums / Compare to system** | No documented API | option-driven only | — |
| **Edit Install Status** (mark De-Installed) | No documented API | option-driven, but it's just a FileMan edit on `INSTALL (#9.7)` | — |
| **Unload a distribution** | No documented API | option-driven only | — |

> **Rule of thumb.** Anything that produces a *new* artifact (load, backup) lacks a public API. Anything that *consumes* an existing artifact (install, history update) has one.

### 13.2 Programmatic install — the `EN^XPDIJ` pattern

`EN^XPDIJ(XPDA)` is the entry point KIDS itself queues to TaskMan when an installer chooses "queue" at the device prompt. From the *KIDS Developer's Guide*:

> *"The `EN^XPDIJ` API can be used with `XPDA` and is defined to task off a KIDS install. … the cleanup runs in the background under KIDS and makes use of KIDS checkpoints, restart upon failure, and message logging that can later be accessed in the Install File Print."*

Pattern:

```mumps
; XPDA = IEN of the loaded build's INSTALL (#9.7) entry
; (obtained after the load step — see §13.3)
N XPDA S XPDA=$O(^XPD(9.7,"B","SOME PACKAGE 1.0",0))
D EN^XPDIJ(XPDA)
```

The install runs Phase 3 unattended:
- Pre-install routine fires.
- All components install.
- Post-install routine fires.
- Disabled options/protocols are re-enabled.
- TaskMan-suspended options resume.
- Status in `INSTALL (#9.7)` advances `0 → 2 → 3` with checkpoint timing.

What it does **not** do for you:
- It does not re-prompt Phase 2 questions. The answers must already be in the `INSTALL ANSWERS (#50)` multiple — write them with FileMan (`FILE^DIE`) before calling.
- It does not load the distribution — the build must already be in `^XTMP` and `INSTALL (#9.7)`.
- It does not run the environment check; that ran during load.

To wrap it as a TaskMan job (the same way the menu does):

```mumps
N ZTRTN,ZTDESC,ZTSAVE,ZTIO,ZTDTH,ZTSK
S ZTRTN="EN^XPDIJ",ZTDESC="KIDS install of "_$P($G(^XPD(9.7,XPDA,0)),U)
S ZTSAVE("XPDA")=""
S ZTIO="",ZTDTH=$H
D ^%ZTLOAD
```

### 13.3 Programmatic load — no API; three workable approaches

You need to get the distribution into `^XTMP("XPDI"…)` and create the `INSTALL (#9.7)` skeleton. Pick one:

1. **Scripted I/O against the menu.** Drive `[XPD LOAD DISTRIBUTION]` (or `[XMPACK]` → `INSTALL/CHECK MESSAGE` for PackMan) with pre-canned answers. Standard `expect` / `send` pattern from a shell harness against the M shell, or M-side using a captured `READ` driver. This is the path most site automation actually uses because it is robust to internal `^XPDI*` refactors across patches.

2. **Call the underlying `^XPDIA*` routines directly.** They exist (`D ^XPDIA` is what the option calls), but they are **not** ICR'd — they can change between Kernel patches without notice. Acceptable for a throwaway job, dangerous for production.

3. **Skip the load phase entirely.** If you are constructing the build *on the source system* (e.g. CI builds from source), you can build it directly into the local `BUILD (#9.6)` via `Edit a Build [XPD EDIT BUILD]` and then call `EN^XPDIJ` against the local build IEN — no transport global needed. This bypasses the load mechanic but requires the build to be assembled in place.

After the load, capture `XPDA = $O(^XPD(9.7,"B",<install name>,0))` and proceed to § 13.2.

### 13.4 Programmatic backup — no API; what to do instead

`[XPD BACKUP]` produces a regular KIDS build (or a routines-only PackMan message). The build's contents are determined by introspecting the *incoming* build to discover every file/field/routine/option/protocol/template it touches, and capturing the *current* state of each.

Three options, ordered by realism:

1. **Scripted I/O against `[XPD BACKUP]`** — the same approach as load. Pre-answer `Backup Type` (`B` or `R`), recipient (mail destination or HFS path), etc. Output is a regular KIDS distribution that can be installed via `EN^XPDIJ`.

2. **Call the unsupported entry point.** The backup option resolves to a routine in the `^XPDIB*` family (varies by Kernel patch level). Same caveat as § 13.3 #2 — works, unsupported.

3. **Build your own backup driver.** Walk the incoming `BUILD (#9.6)` entry, enumerate every component, and synthesise a new build entry that captures the current state. This is essentially re-implementing `[XPD BACKUP]`. Avoid unless you have a specific reason — you are now maintaining KIDS-internal logic.

Whichever you pick, the *output* is a normal KIDS distribution, so the rollback step downstream uses `EN^XPDIJ` like any install.

### 13.5 Programmatic rollback — install backup + FileMan edit

Two parts:

**Part A — Install the backup build.** Same as § 13.2:

```mumps
N XPDA S XPDA=$O(^XPD(9.7,"B","SOME PACKAGE 1.0b",0))   ; "b" suffix = backup
D EN^XPDIJ(XPDA)
```

**Part B — Mark the original install De-Installed.** `[XPD EDIT INSTALL]` is a FileMan ScreenMan form on `INSTALL (#9.7)` — reproduce it with `FILE^DIE`:

```mumps
N FDA,XPDORIG
S XPDORIG=$O(^XPD(9.7,"B","SOME PACKAGE 1.0",0))   ; the original, NOT the backup
S FDA(9.7,XPDORIG_",",.02)=4                       ; STATUS = De-Installed
S FDA(9.7,XPDORIG_",",17)=$$NOW^XLFDT              ; INSTALL COMPLETE TIME
D FILE^DIE("","FDA")
```

That gives you an audit trail consistent with what `[XPD EDIT INSTALL]` would have written.

For the patch-history side, **do not** try to remove the original patch from `PATCH APPLICATION HISTORY (#9.4901)` — KIDS is append-only on that multiple by design, and downstream `$$PATCH^XPDUTL` checks rely on its monotonic growth. The De-Installed status on `INSTALL (#9.7)` is the correct rollback signal.

### 13.6 Helper APIs you'll use along the way

All `XPDUTL`/`XPDID`/`XPDIP`/`XPDIJ` family — ICRs noted above where they exist.

| API | Purpose |
|-----|---------|
| `$$PATCH^XPDUTL(patch)` | Was patch `XU*8.0*28` installed? Returns 1/0. |
| `$$LAST^XPDUTL(pkg[,ver][,1])` | Last patch applied; with `z=1` (per `XU*8.0*559`), last *released* patch only. |
| `$$VER^XPDUTL(buildname)` / `$$VERSION^XPDUTL(pkg)` | Version parsing/lookup. |
| `$$INSTALDT^XPDUTL(pkg,ver)` | Returns all install dates/times — useful for verifying a rollback's effect. |
| `$$NEWCP^XPDUTL` / `$$COMCP` / `$$CURCP` / `$$PARCP` / `$$UPCP` / `$$VERCP` | Checkpoint API — same restart machinery the menu uses. Lets a custom driver survive aborts. |
| `$$OPTDE^XPDUTL(name,action)` / `$$PRODE^XPDUTL(name,action)` | Disable/enable an option or protocol from M without going through the standard KIDS Q&A. |
| `$$RTNUP^XPDUTL` | Tell KIDS to skip a routine or mark it `DELETE AT SITE` during install. |
| `MES^XPDUTL(text)` / `BMES^XPDUTL(text)` | Append a line into the install's `MESSAGES` field — same audit trail KIDS would write. Always emit progress messages here so `[XPD PRINT INSTALL FILE]` reflects what your driver did. |
| `$$PKGPAT^XPDIP(pkg_ien,version,.x)` | Update `PATCH APPLICATION HISTORY (#9.49,1105)`. ICR #2067. |
| `$$PKGVER^XPDIP(pkg_ien,[.]version)` | Update `VERSION (#22)` multiple. ICR #2067. |
| `UPDATE^XPDID(n)` (with `XPDIDTOT`) | Drive the progress bar from inside a custom install loop. ICR #2172. |
| `EN^XPDIJ(XPDA)` | Run install on an `INSTALL (#9.7)` IEN. ICR #2243. |

Set the standard install context variables in any custom driver: `XPDA` (install IEN), `XPDNM` (build name), `XPDQUIT`/`XPDABORT` for abort signalling, `XPDDIQ("XPI1")` to suppress install-question prompts.

### 13.7 Patchman — the supported end-to-end automation path

`[XPD AUTOMATIC PATCHING MENU]` is Kernel's official automation layer:

- Polls FORUM for released patches.
- Honors NPM sequence numbers (§ 12.6) when ordering installs.
- Queues installs through TaskMan.
- Logs everything to the standard `INSTALL (#9.7)` audit trail.

Patchman is documented in its own user guide — neither the *KIDS User Guide* nor the *KIDS Developer's Guide* covers it. If your goal is *"keep this site current with released patches without operator intervention,"* Patchman is the supported answer; you should **not** roll your own driver for that use case.

If your goal is *"wrap KIDS in CI/CD-style build → install → rollback for in-house builds,"* Patchman doesn't help — assemble it from `EN^XPDIJ` + scripted I/O for load/backup + FileMan edits for status.

### 13.8 Worked example — fully scripted patch round-trip

End-to-end pattern for an unattended install with rollback safety. Steps marked **(I/O)** require scripted I/O against the menu; everything else is supported M.

```text
1. (I/O)  Drive [XPD LOAD DISTRIBUTION] against the patch HFS file.
          Capture XPDA from ^XPD(9.7,"B",<install name>).

2. (I/O)  Drive [XPD BACKUP] with Backup Type = B against XPDA.
          Capture the backup HFS path or PackMan basket entry.

3.  M     Pre-populate INSTALL ANSWERS (#50) on XPDA via FILE^DIE
          with the answers your install needs (disable options? Y/N,
          delay minutes, pre/post-install Qs).

4.  M     D EN^XPDIJ(XPDA)        ; the actual install

5.  M     Verify completion:
          I $P($G(^XPD(9.7,XPDA,0)),U,2)'=3 D ROLLBACK   ; status != Install Completed

6.  M     ROLLBACK:
          ; (I/O) load the backup HFS file via [XPD LOAD DISTRIBUTION]
          ; M     XPDB = $O(^XPD(9.7,"B",<backup install name>,0))
          ; M     pre-populate INSTALL ANSWERS (#50) on XPDB
          ; M     D EN^XPDIJ(XPDB)
          ; M     FILE^DIE: set INSTALL (#9.7) STATUS (#.02)=4 on XPDA
```

Each `EN^XPDIJ` invocation gets full checkpoint/restart support, so a transient failure inside the install or rollback can be retried via `Restart Install of Package(s) [XPD RESTART INSTALL]` (or by calling `EN^XPDIJ` again — it picks up at the last completed checkpoint).

### 13.9 What can go wrong

- **Missing answers.** `EN^XPDIJ` does not prompt. If `INSTALL ANSWERS (#50)` is empty for a question the developer asked, the install will fail or use blank input. Always pre-populate.
- **Missing PACKAGE FILE LINK.** As in § 12.7, an install that doesn't link to `PACKAGE (#9.4)` writes no entry to `PATCH APPLICATION HISTORY` — downstream `$$PATCH^XPDUTL` checks return 0 even though the patch is installed.
- **Backup doesn't capture pre/post-install side effects.** A driver that assumes "install backup = full rollback" will leave data conversions, deletions, and journaled global writes in their post-install state. Read the patch description.
- **Unsupported entry-point drift.** `^XPDIA*`, `^XPDIB*`, `^XPDIK*` change between Kernel patches. Direct calls work today and break tomorrow. Scripted I/O against the menu options is more durable.
- **TaskMan suspense.** `EN^XPDIJ` can suspend queued options around the install (per the answers in `INSTALL ANSWERS`). If a driver crashes mid-install, you may need to manually release suspended options — check `[XUTM SCHEDULE]` and the `MESSAGES` field.
- **`STATUS = 2` ("Install Started") forever.** A killed driver leaves the install in started state. Either restart with `EN^XPDIJ(XPDA)` (idempotent via checkpoints) or, if you've decided to abandon it, `FILE^DIE` the status back to `0` before unloading.

---

## 14. Bringing a Site Current — Programmatic Patch Campaigns

This section composes everything from § 12 (sequencing) and § 13 (programmatic primitives) into a real-world workflow: take a VistA site at some unknown patch level and bring it up to the latest released patch state across all packages, safely and unattended.

### 14.1 Recommendation up front — use Patchman if you can

If the site has FORUM connectivity, **use `Patchman [XPD AUTOMATIC PATCHING MENU]`**. It exists for exactly this problem:

- Polls FORUM for newly released patches in packages the site has installed.
- Honors NPM sequence numbers (§ 12.6) when ordering installs.
- Honors `REQUIRED BUILD (#11)` declarative dependencies (§ 12.3).
- Queues installs through TaskMan with full `INSTALL (#9.7)` audit trail.

Patchman is documented in its own user guide — neither the *KIDS User Guide* nor the *KIDS Developer's Guide* covers it in detail. The reason to *not* use Patchman is one of: no FORUM connectivity (air-gapped, mirrored, training, foreign installs), in-house builds outside the FORUM release stream, or a need for CI-style automation around custom builds. Everything below targets those cases.

### 14.2 Operating principles

These are non-negotiable. Violations will eventually corrupt patch history, leave a half-applied patch in production, or both.

1. **NPM sequence number is the only correct ordering key** — not patch number, not date applied, not lexical sort. Each `(package, version)` line has a single monotonic SEQ # series.
2. **One patch at a time.** Each install must complete and update `PATCH APPLICATION HISTORY (#9.49,1105)` before the next environment check runs — otherwise downstream `$$PATCH^XPDUTL` checks return false negatives (§ 12.7).
3. **Test account before production** (VA "alpha → beta" lifecycle, § 13/§ 16). Anything that touches data conversions runs in a Test account first.
4. **Roll-forward-only by default.** Auto-rollback on failure is unsafe — a half-applied patch usually requires diagnosis, not reversal. Stop, log, page a human.
5. **Per-patch backup, not per-campaign.** `[XPD BACKUP]` *before* each install, captured to a stable HFS path. Granular rollback beats "rewind to baseline."
6. **M-database snapshot before the campaign starts.** Patchman / KIDS do not snapshot globals. Use the M implementation's facility (YottaDB `mupip backup`, Caché external backup, etc.) so you have a hard-stop recovery path independent of KIDS.

### 14.3 Five-layer architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. CATALOG    Mirror of FORUM NPM: (pkg, patch#, seq#,          │
│               released_date, prereqs[], hfs_path, sha256)       │
├─────────────────────────────────────────────────────────────────┤
│ 2. STATE      Read PACKAGE(#9.4) PATCH APPLICATION HISTORY      │
│               for every installed package → currently-applied   │
│               (pkg, patch#, seq#) tuples                        │
├─────────────────────────────────────────────────────────────────┤
│ 3. PLANNER    gap = CATALOG \ STATE                             │
│               topo-sort by (pkg, seq#) + REQUIRED BUILD graph   │
│               output: ordered install plan                      │
├─────────────────────────────────────────────────────────────────┤
│ 4. EXECUTOR   for each patch in plan:                           │
│                 load → backup → install (EN^XPDIJ) → verify     │
│               stop on first failure                             │
├─────────────────────────────────────────────────────────────────┤
│ 5. VERIFIER   per-patch + end-of-campaign integrity sweep       │
│               reconcile local PATCH APPLICATION HISTORY ↔ NPM   │
└─────────────────────────────────────────────────────────────────┘
```

### 14.4 Layer 1 — Catalog (mirror of FORUM NPM)

Two acceptable sources of ground truth:

- **FORUM NPM** if you have it — directly authoritative.
- **Manually curated catalog file** if not — JSON/CSV per package, updated out of band.

Per-row schema, minimum:

| Field | Source |
|-------|--------|
| `package_namespace` (e.g. `XU`, `XT`, `OR`) | NPM |
| `version` (with decimal, e.g. `8.0`) | NPM |
| `patch_number` | NPM |
| `sequence_number` | NPM (assigned at release) |
| `released_date` | NPM |
| `path_to_KIDS_distribution` | site-local HFS path |
| `sha256` of HFS file | computed at mirror time |
| `required_patches` (list) | each KIDS build's `REQUIRED BUILD (#11)` multiple |
| `description_prereq_text` | scraped from patch description, free text |

The last two fields capture **declared** prereqs (machine-readable, from the build) and **implicit** prereqs from prose. The latter is the gap you cannot fully automate — Patchman handles it because FORUM is the source.

### 14.5 Layer 2 — State (read PACKAGE #9.4 patch history)

Walk every `PACKAGE (#9.4)` entry → `VERSION (#22)` multiple → `PATCH APPLICATION HISTORY (#9.49,1105)` multiple inside it. For each row:

- patch name (`.01`) — parse the `SEQ #` if present
- date applied (`.02`)
- applied by (`.03`)

Sanity-check via `$$LAST^XPDUTL(pkg,ver,1)` — the API's `nnn Seq #nnn^yyymmdd` return summarises the same multiple. If they disagree, trust the multiple.

> **Trap.** Patches installed without a `PACKAGE FILE LINK` on the build are missing from `PATCH APPLICATION HISTORY` entirely (§ 12.7). Cross-check against `INSTALL (#9.7)` `STATUS = 3` entries and flag any install-completed entry with no patch-history row — those are the false negatives that will trip later `$$PATCH^XPDUTL` checks. Add them to STATE manually if confirmed.

### 14.6 Layer 3 — Planner (gap, topo-sort by SEQ # + Required Builds)

Per package, independently:

1. Find the highest applied `seq_number` in STATE for `(pkg, version)`.
2. Find every CATALOG row with `seq_number > that_max` for the same `(pkg, version)`.
3. Sort ascending by `seq_number`.

Then **merge across packages** by walking the Required Builds graph — an `XU` patch may declare a required `XT` patch and vice versa. A topological sort over the union graph yields a single install order.

- Detect cycles. They shouldn't exist; if they do, your catalog is wrong.
- Flag patches whose required-builds entries are `WARNING ONLY` (§ 12.3) — they won't hard-stop at install time, so the planner must enforce them.
- Flag patches whose `description_prereq_text` mentions a prereq not present as a `REQUIRED BUILD` — these need operator review before the campaign starts.

Output a plan file: ordered list of `(seq_index, pkg, patch#, seq#, hfs_path, sha256)`. Make it human-reviewable before the executor touches it.

### 14.7 Layer 4 — Executor (per-patch state machine)

For each patch in the plan, in order:

```text
A. PRECHECK
   - sha256 of HFS file matches catalog
   - $$PATCH^XPDUTL says it's NOT already installed (idempotency)
   - all REQUIRED BUILD prereqs satisfied per current state
   - prior patch's INSTALL (#9.7) STATUS = 3 (not 2)
   if any fail → HALT campaign, emit diagnostic

B. LOAD
   - drive [XPD LOAD DISTRIBUTION] via scripted I/O against the HFS file
     (or [XMPACK] → INSTALL/CHECK MESSAGE for PackMan delivery)
   - capture XPDA = $O(^XPD(9.7,"B",<install name>,0))
   - confirm environment check passed (status logged in INSTALL #9.7)
   if fail → HALT

C. BACKUP
   - drive [XPD BACKUP] (Type B) against XPDA
   - emit backup HFS path to a campaign-local artifact directory
   - verify the backup is parseable as a KIDS distribution
   if fail → HALT  (do NOT install without a backup)

D. PRE-POPULATE ANSWERS
   - FILE^DIE on INSTALL ANSWERS (#50) for known questions
   - default: do NOT disable options (Y/N), delay 0 minutes
   - patch-specific: load from per-patch answers file if it exists

E. INSTALL
   - D EN^XPDIJ(XPDA)
   - poll INSTALL (#9.7) STATUS until 3 (Install Completed)
   - timeout: 30 minutes per patch unless catalog overrides

F. POSTCHECK
   - INSTALL (#9.7) STATUS = 3                      ; not 2
   - $$PATCH^XPDUTL("<patch name>") = 1             ; round-trip
   - PATCH APPLICATION HISTORY contains new entry with SEQ #
   - [XPD VERIFY INTEGRITY] reports no checksum drift for this build
   if any fail → HALT

G. LOG
   - append (timestamp, patch, status, INSTALL #9.7 IEN, backup path)
     to campaign log
```

**Halt-on-first-failure is deliberate.** Continuing past a failed patch corrupts every dependency check downstream. The campaign log + the per-patch backup gives an operator everything they need to diagnose, fix, and resume from the failed patch number.

### 14.8 Layer 5 — Verifier (per-patch + end-of-campaign)

Per-patch checks live in step F above. At end of campaign:

1. Re-read STATE; assert it matches CATALOG up to the planned target SEQ # for every package touched.
2. `[XPD VERIFY INTEGRITY]` on each touched package — full routine checksum sweep against the latest `BUILD (#9.6)` entries. (Reminder from § 12.7 / Utilities: don't purge the latest BUILD entry, or this becomes impossible.)
3. `$$LAST^XPDUTL(pkg,ver,1)` per package — should report the highest planned SEQ #.
4. Spot-check `INSTALL (#9.7)` `MESSAGES` for any installed patch that emitted warnings — they install successfully but may need follow-up.
5. (If FORUM-connected.) Reconcile local patch history against FORUM's view; flag anything where the site believes a patch is installed but FORUM disagrees (or vice versa).

### 14.9 Hard parts no automation handles

- **Patch descriptions with prose-only prereqs.** *"Install KIDS XU\*8.0\*450 only after IRMS has rebuilt the AKMOXREF cross-reference."* No metadata captures this. Either curate it into your catalog manually or use Patchman.
- **Sequence holes.** A patch can be issued, withdrawn, and re-issued under a different number. NPM tracks this; an offline catalog must be updated manually.
- **Site-specific data conversions.** A patch's post-install may run a one-shot data fix that isn't safe to re-run. Track non-idempotent patches in the catalog and require explicit operator confirmation per install.
- **Locked options/protocols mid-install.** If the campaign disables menu options for each install, users get repeatedly kicked out. Either schedule one maintenance window for the whole campaign with options disabled at the campaign level, or run during a quiet window with `Disable = NO` per patch (riskier).
- **MailMan-delivered patches.** If patches arrive as PackMan messages instead of HFS files, the load step uses `[XMPACK]` → `INSTALL/CHECK MESSAGE` instead of `[XPD LOAD DISTRIBUTION]`. The downstream pipeline is identical.
- **Cross-package post-install ordering.** Some patches assume a sibling patch in another package has already run its post-install (not just been declared in `PATCH APPLICATION HISTORY`). The Required Builds graph captures install ordering, not post-install ordering. For these, sequence them adjacent in the plan and watch the campaign log carefully.

### 14.10 Pre-flight checklist

Before kicking off any campaign:

- [ ] M-database snapshot taken (independent of KIDS) and verified restorable
- [ ] Catalog refreshed within last 24h (or operator has signed off on staleness)
- [ ] Plan reviewed by a human; cycles, prose-prereq flags, non-idempotent flags resolved
- [ ] Test account has run the same plan to completion successfully
- [ ] Maintenance window scheduled and users notified
- [ ] Disk space for per-patch backups confirmed (`N × avg_backup_size + 50%` headroom)
- [ ] TaskMan idle or controllable (no long-running scheduled jobs in the window)
- [ ] Operator on-call for halt-on-failure response
- [ ] Campaign log destination writable
- [ ] FORUM connectivity verified (if catalog refresh or post-campaign reconciliation depends on it)

When in doubt: install fewer patches per campaign, more campaigns. SEQ # ordering is preserved either way; smaller campaigns mean smaller blast radius if anything goes wrong.

---

## 15. Utilities Reference

All under `[XPD UTILITY]`.

| Option Name | Tag | Purpose |
|-------------|-----|---------|
| Build File Print | `[XPD PRINT BUILD]` | Print a `BUILD (#9.6)` entry — full software definition. |
| Install File Print | `[XPD PRINT INSTALL FILE]` | Print an `INSTALL (#9.7)` entry — status, timing, install log, answers. |
| Edit Install Status | `[XPD EDIT INSTALL]` | Edit `STATUS (#.02)` and `INSTALL COMPLETE TIME (#17)` in `INSTALL (#9.7)`. Used to mark a patch De-Installed (`XU*8.0*539`). |
| Convert Loaded Package for Redistribution | `[XPD CONVERT PACKAGE]` | Take loaded transport globals and prepare them for re-export. With `XU*8.0*44`, answer `YES` to *"Want to make the Transport Globals Permanent?"* to keep them in `^XTMP` ("Gold" library). |
| Display Patches for a Package | `[XPD PRINT PACKAGE PATCHES]` | Reads `PACKAGE (#9.4)` and lists installed patches with date and installer. |
| Purge Build or Install Files | `[XPD PURGE FILE]` | Purge old `BUILD (#9.6)` or `INSTALL (#9.7)` entries. Recency order: Released > Beta (`V`) > Alpha (`T`). **Do not purge the most recent BUILD entry** — `[XPD VERIFY INTEGRITY]` needs it, and rollup/sequence reasoning (see [§ 12](#12-patch-sequencing--how-kids-manages-order)) depends on it. |
| Rollup Patches into a Build | `[XPD ROLLUP PATCHES]` | Merges all KIDS patches for a software/version into a single BUILD definition. Excludes pre/post-install routines. |
| Update Routine File | `[XPD ROUTINE UPDATE]` | Reconciles `ROUTINE (#9.8)` with routines actually on the system, namespace by namespace. Cleanup pass preserves entries marked "National" in `CHECKSUM REPORT (#6)` (`XU*8.0*393`). |
| Verify a Build | `[XPD VERIFY BUILD]` | Confirms every component listed in a `BUILD (#9.6)` entry actually exists on the system. Developer pre-export gate. |
| Verify Package Integrity | `[XPD VERIFY INTEGRITY]` | Compares current routine checksums to those stored when the build was transported. |

---

## 16. Alpha/Beta Tracking

Distinct from the install workflow but lives on the KIDS conceptual map. VA terminology:

- **Alpha** — test software in a site's *Test* account.
- **Beta** — test software in a site's *Production* account.

Menu: `Alpha/Beta Test Option Usage Menu [XQAB MENU]`, hung off `Operations Management [XUSITEMGR]`. Options:

- `Errors Logged in Alpha/Beta Test (QUEUED) [XQAB ERROR LOG XMIT]`
- `Actual Usage of Alpha/Beta Test Options [XQAB ACTUAL OPTION USAGE]`
- `Low Usage of Alpha/Beta Test Options [XQAB LIST LOW USAGE OPT]`
- `Print Alpha/Beta Errors (Date/Site/Num/Rou/Err) [XQAB ERR DATE/SITE/NUM/ROU/ERR]`
- `Send Alpha/Beta Usage to Programmers [XQAB AUTO SEND]`

Tracking starts/stops are described in the *Kernel 8.0 Developer's Guide: KIDS Developer Tools User Guide*.

---

## 17. Quick Cheat-Sheet

**Install a standard distribution**

```
EVE → XUPROG → XPD MAIN → XPD INSTALLATION MENU
1. XPD LOAD DISTRIBUTION
2. (optional) XPD PRINT CHECKSUM
3. (optional) XPD PRINT INSTALL
4. (optional) XPD COMPARE TO SYSTEM
5. XPD BACKUP            ← create rollback artifact NOW
6. XPD INSTALL BUILD     ← Phase 2 (Q&A) + Phase 3 (execute)
7. XPD PRINT INSTALL FILE → confirm STATUS = Install Completed
8. XPD VERIFY INTEGRITY  → confirm routine checksums
```

**Aborted load**

```
XPD UNLOAD DISTRIBUTION
   (set INSTALL (#9.7) STATUS to 0 first if install was started)
```

**Aborted install**

```
XPD PRINT INSTALL FILE → diagnose
fix root cause
XPD RESTART INSTALL
```

**Uninstall**

```
(load + install the backup build created at step 5 above via XPD BACKUP)
XPD LOAD DISTRIBUTION  → backup file
XPD INSTALL BUILD      → backup install name
XPD EDIT INSTALL       → set original install STATUS = 4 (De-Installed)
```

---

## 18. VistA Packages and Routines Involved

### Packages (by namespace)

| Namespace | Package | Role in KIDS install/uninstall |
|-----------|---------|---------------------------------|
| `XU` / `XPD` | **Kernel 8.0** | Hosts KIDS itself. `XPD*` is the KIDS namespace; `XU*` covers Kernel security, options, TaskMan integration. |
| `XT` | **Toolkit 7.3** | Provides the checksum integrity routines `CHECK^XTSUMBLD` / `CHECK1^XTSUMBLD`, the `XU CHECKSUM REPORT` option backbone, and the columnar compare added in `XT*7.3*93`. |
| `XM` | **MailMan** | PackMan transport (`Load PackMan Message [XMPACK]`, `INSTALL/CHECK MESSAGE`). Delivery channel for routine-only backup messages and small distributions. |
| `XU` (TaskMan subsystem) | **TaskMan** | Queues installs (`EN^XPDIJ` is the queued task entry), suspends/releases queued options around installs. |
| `DI` | **VA FileMan** | Underlying data engine for `BUILD (#9.6)`, `INSTALL (#9.7)`, `PACKAGE (#9.4)`, `ROUTINE (#9.8)`. Legacy `DIFROM` lives here (deprecated for KIDS; retained for standalone FileMan sites). |
| `XQ` | **Menu Manager** | Owns the option/protocol enable/disable mechanics KIDS drives during Phase 3. |

### Key routines and entry points

| Routine / Tag | Purpose |
|---------------|---------|
| `EN^XPDIJ(XPDA)` | **Documented programmatic install entry point** (ICR #2243, Controlled Subscription). Runs install on the `INSTALL (#9.7)` IEN supplied. The same entry point KIDS queues to TaskMan when the menu installer chooses "queue." |
| `UPDATE^XPDID(n)` | Drives the install progress bar (ICR #2172). Caller sets `XPDIDTOT` to the total item count, then calls `UPDATE^XPDID(currentN)` from the work loop. |
| `$$PKGPAT^XPDIP(pkg_ien,version,.x)` | Update `PATCH APPLICATION HISTORY (#9.49,1105)` from a pre/post-install routine (ICR #2067). |
| `$$PKGVER^XPDIP(pkg_ien,[.]version)` | Update `VERSION (#22)` multiple from a pre/post-install routine (ICR #2067). |
| `$$INSTALDT^XPDUTL(pkg,ver)` | Returns all install dates/times for a package/version. Useful for verifying a rollback's effect. |
| `$$NEWCP / $$COMCP / $$CURCP / $$PARCP / $$UPCP / $$VERCP^XPDUTL` | Checkpoint API — create / complete / get-current / get-parameter / update / verify. Same restart machinery the menu uses; lets a custom install driver survive aborts. |
| `$$OPTDE^XPDUTL(name,action)` | Disable/enable an option from M (action: 1=enable, 2=disable). Bypasses the standard KIDS Q&A. |
| `$$PRODE^XPDUTL(name,action)` | Disable/enable a protocol from M (action: 1=enable, 2=disable). |
| `$$RTNUP^XPDUTL` | Tell KIDS to skip a routine or mark it `DELETE AT SITE` during install. |
| `MES^XPDUTL(text)` / `BMES^XPDUTL(text)` | Append a line into the install's `MESSAGES` field — same audit trail KIDS would write. Custom drivers should emit progress here so `[XPD PRINT INSTALL FILE]` reflects what they did. |
| `XPDA` / `XPDDIQ("XPI1")` | Standard install context variables. `XPDA` = current install IEN; `XPDDIQ("XPI1")` suppresses the install-question prompts. |
| `^XPDI*` | KIDS install support routines (load, install, restart, unload). |
| `^XPDD*` | KIDS distribution-side (build, transport) routines. |
| `^XTMP("XPD…")` | Scratch global where loaded transport globals live until installed or unloaded. |
| `CHECK^XTSUMBLD` / `CHECK1^XTSUMBLD` | Toolkit checksum APIs used by `[XPD PRINT CHECKSUM]` and `[XPD VERIFY INTEGRITY]`. `CHECK1^XTSUMBLD` (post `XU*8.0*369`) drives the local `[XU CHECKSUM REPORT]` option. |
| `XMPACK` | MailMan PackMan-message loader — KIDS-equivalent of `[XPD LOAD DISTRIBUTION]` for messaged distributions. |
| `DIFROM` | Legacy export entry point, *deprecated for KIDS*; supported only for standalone FileMan sites. |
| `ZXGENV` / `ZXGPRE` / `ZXGPOS` | Sample build's environment-check / pre-install / post-install routines from the User Guide examples. Real builds substitute their own namespaced equivalents. |
| `$$PATCH^XPDUTL` | Environment-check API: returns 1/0 for whether a named patch is installed. Drives programmatic dependency checks (§ 12.4). ICR #10141. |
| `$$LAST^XPDUTL` | Returns the most recent patch applied to a software/version, with sequence # for released patches. ICR #10141. `z=1` parameter (released-only) added by `XU*8.0*559`. |
| `$$VER^XPDUTL` / `$$VERSION^XPDUTL` | Parse version from a build name / report current version of a package — used in environment checks for version comparisons. |
| `XPDNM` / `XPDNM("SEQ")` / `XPDNM("TST")` | KIDS key variables exposing current build name, NPM sequence number, and NPM test number to env-check, pre-install, and post-install routines. `("SEQ")` and `("TST")` added by `XU*8.0*559`. |
| `XPDQUIT` / `XPDABORT` | Environment-check abort flags. `XPDQUIT=1` cancels current transport global, `=2` cancels all in distribution; `XPDABORT=1` aborts immediately. |

### Notable patches that shaped the current behavior

| Patch | What it changed |
|-------|-----------------|
| `XU*8.0*30` | KIDS began saving NPM sequence numbers alongside patch names in `PATCH APPLICATION HISTORY (#9.49,1105)`. Patches installed before this patch show no sequence number in the multiple. |
| `XU*8.0*44` | Added the *"Want to make the Transport Globals Permanent?"* prompt to `[XPD CONVERT PACKAGE]`. |
| `XU*8.0*369` | `CHECK1^XTSUMBLD` now backs the `[XU CHECKSUM REPORT]` option. |
| `XU*8.0*393` | Auto-sends checksum messages to FORUM on HFS transport; FORUM `ROUTINE (#9.8)` becomes the gold standard; added `TRANSPORT BUILD NUMBER (#63)` to `BUILD (#9.6)`; added columnar compare (with Toolkit `XT*7.3*93`); preserves "National" routines during `[XPD ROUTINE UPDATE]` cleanup. |
| `XU*8.0*539` | Added `Edit Install Status [XPD EDIT INSTALL]` so installers can mark a patch De-Installed. |
| `XU*8.0*559` | Released `XPDNM("SEQ")` / `XPDNM("TST")` key variables and the `z` parameter of `$$LAST^XPDUTL` (last released-patch only). Together these expose NPM sequence/test numbers to env-check and pre/post-install code. |
| `XT*7.3*93` | Toolkit support for the columnar routine compare in `[XPD COMPARE TO SYSTEM]`. |

---

## 19. References

Primary source for this guide:

- **Kernel 8.0 Systems Management: KIDS User Guide** — VA Office of Information & Technology, Product Delivery Service. August 2025, revision 1.2.
  PDF: <https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf>
  DOCX: <https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.docx>
  Local mirror: `~/data/vista-docs/md-img/XU/kernel-8-0-systems-management-kids-user-guide.md`

Companion documents (cross-referenced inside the User Guide):

- **Kernel 8.0 Developer's Guide: KIDS Developer Tools User Guide** — covers build authoring, the Distribution menu (`[XPD DISTRIBUTION MENU]`), and Alpha/Beta tracking from the developer's perspective.
  PDF: <https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf>
  Local mirror: `~/data/vista-docs/md-img/XU/kernel-8-0-developer-s-guide-kids-user-guide.md`
- **Kernel 8.0 Systems Management: Main Directory User Guide** — Orientation and Glossary referenced in the KIDS User Guide.
  PDF: <https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf>
- **VA FileMan Developer's Guide** — for the deprecated `DIFROM` export path used by standalone FileMan sites.
- **National Patch Module (NPM) on FORUM** — current authoritative source for patch history and gold-standard routine checksums (`ROUTINE (#9.8)` on FORUM).

VDL application landing page:

- Kernel: <https://www.va.gov/vdl/application.asp?appid=10>

Local skills (in this workspace) with related domain knowledge:

- `~/claude/skills/vista-system/` — VistA package architecture and namespaces.
- `~/claude/skills/vista-fileman/` — FileMan APIs and global conventions, useful when reading `BUILD (#9.6)` / `INSTALL (#9.7)` / `PACKAGE (#9.4)` / `ROUTINE (#9.8)` directly.
