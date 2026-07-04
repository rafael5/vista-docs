# VistA Package Lifecycle — Planning Specification (v7)

**Scope:** Pure VistA M applications across all VistA flavors (WorldVistA EHR, vxVistA/OSEHRA, VA production VistA). Excludes Web clients, VA enterprise services, integration middleware, COTS products, VistA+GUI hybrids, and VistA+COTS hybrids — see §13.1 for the precise filter.
**Coverage:** Install · Patch · Back-Out · Rollback · Audit (governance and process; pre-install pre-flight automation in companion plan)
**Mode:** Specification only — no executable commands or scripts
**Population (validated, see §13):** 128 pure-VistA packages · 2,496 unique documents · 6,020 inventory rows
**Primary sources:**
- [`vistadocs/vdl`](https://github.com/vistadocs/vdl) — 1,420 markdown documents (content tier)
- [`vistadocs/vistadocs.github.io`](https://github.com/vistadocs/vistadocs.github.io) — `vdl_inventory_enriched.csv`, 8,834 documents (master index)
- [VA VDL](https://www.va.gov/vdl) — original PDFs/DOCX (institutional source of record)
- VA FORUM / NPM (National Patch Module) — patch governance and distribution

**Companion documents:**
- `vdl-query-patterns.md` — reusable VDL discovery guide (extracted in v6 from this spec's §12)
- `vista-package-state-audit-plan.md` — pre-install pre-flight automation plan (extracted in v7 from this spec's §14, reframed for developer pre-flight rather than IRM post-hoc reconciliation)
- `vdl-search-assessment.md` — current-state assessment of VDL search infrastructure with proposed improvements
- `vista_packages_summary.csv` — 128-package summary derived from the §13 filter
- `vdl_inventory_vista_only.csv` — 6,020-row pre-filtered inventory derived from the §13 filter

**Version history:**
- v1 — Inferred patterns from training data
- v2 — Re-grounded against `vistadocs/vdl` primary sources
- v3 — Empirical validation: §3 template tested against all 32 DIBRGs in markdown corpus (84% exact, 94% with minor variation); §3.1 documents structural variants; §12 adds CSV-based discovery patterns
- v4 — Population scope formally defined and validated; §13 documents 128-package pure-VistA filter, documentation coverage analysis (40/128 DIBRG, 81/128 IG, 36 with neither), data-quality caveats, and filtered CSV deliverables
- v5 — §14 adds patch-state reconciliation and automation. Enumerates the six primary sources of patch state (#9.7, #9.4, routine 2nd lines, checksums, NPM, ^XTMP) plus three secondary; defines an eight-class discrepancy taxonomy; specifies a two-tier automation architecture (M-side extractor + external reconciler); identifies overlap with Build Analyzer (XU\*8.0\*782), VistA Patch Monitor (XT\*7.3\*98), and VPSRT (XT\*7.3\*143)
- v6 — §12 (Discovery and query patterns) extracted to standalone reusable document `vdl-query-patterns.md`. §12 in this spec is now a brief pointer to the external resource. §13.5 (data quality caveats) cross-references the canonical caveats list in the standalone document
- **v7 — §14 extracted to standalone document `vista-package-state-audit-plan.md` and reframed as a pre-install pre-flight automation plan for package developers (rather than post-hoc IRM reconciliation). The reframing introduces an eight-class *blocker* taxonomy (B1–B8, 32 sub-classes) and a three-tier architecture: M-side state extractor + KID file analyzer + external pre-flight engine. §14 in this spec is now a brief pointer with a relationship table back to the standalone plan.**

---

## 1. Foundational concepts

### 1.1 What "package" means

A VistA **package** is a bounded software unit identified by a **2–5 letter namespace** (e.g. `OR`, `XU`, `LR`, `PSO`). The namespace prefixes every routine, option, parameter, security key, RPC, and FileMan file owned by the package.

### 1.2 The three artifacts (corpus-attested)

| Artifact | FileMan file | Authoritative source |
|---|---|---|
| **PACKAGE** | `#9.4` | [Kernel KIDS Systems Mgmt User Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-systems-management-kids-user-guide.md), §"Changes in the Role of the PACKAGE (#9.4) File" |
| **BUILD** | `#9.6` | Same doc, §"Build Entries and the BUILD (#9.6) File" |
| **INSTALL** | `#9.7` | Same doc, §"INSTALL (#9.7) File" |

### 1.3 Patch identifier

`NAMESPACE*VERSION*PATCH_NUMBER` — e.g. `OR*3.0*387`, `XU*8.0*702`.

### 1.4 The institutional answer to "how do I install/uninstall a package?"

**The VA's own answer is: read the package's DIBRG.**

A **Deployment, Installation, Back-Out and Rollback Guide** (DIBRG) is a standardized VA OIT artifact published *per package per release*. The corpus contains DIBRGs for ADT, ANRV, CHDS, GMRC, MAG, PSA, PSO, PX, SD, and the Kernel itself, among others. All four DIBRGs reviewed (ADT, MAG, PSO Inbound eRx, Kernel) follow an identical section template — see §3 below.

**Implication for this spec:** any planning document for VistA install/backout that does not produce or consume a DIBRG is operating outside the institutional norm.

### 1.5 Why "uninstall" is not a primitive (now corpus-attested)

The ADT DIBRG states the canonical VA position: a VistA KIDS build cannot be backed out in totality — only routines are preserved in the backup transport global. Data dictionary changes, components, and post-install side effects are not reversed by any KIDS mechanism. The preferred institutional remedy is a **forward-fix patch**, not a back-out.

The single KIDS-native "uninstall" primitive is the **Edit Install Status** option (`XPD EDIT INSTALL`, added in Kernel patch `XU*8.0*539`), which merely sets the STATUS (#.02) field of an INSTALL (#9.7) record to value `4 = De-Installed`. **It does not undo anything.** It is an audit annotation.

Where the corpus *does* mention "uninstall" (e.g. MAG `*3.0*358` Client Uninstall in the MAG DIBRG), the reference is to **Windows-side client software** (VIX Viewer), which uninstalls via the OS — not to a VistA M-server uninstall. The client/server distinction is critical and is preserved in §8.

---

## 2. The authoritative install mechanism (KIDS)

The Kernel KIDS Systems Management User Guide defines the install as **three phases**:

### Phase 1 — Loading transport globals from a distribution

- Installer uses the `Load a Distribution [XPD LOAD DISTRIBUTION]` option (or, for PackMan messages, `Load PackMan Message [XMPACK]` invoking MailMan's INSTALL/CHECK MESSAGE).
- For each transport global in the distribution, KIDS creates an entry in the INSTALL (#9.7) file.
- KIDS loads the transport globals into the `^XTMP` global.
- KIDS prompts to run the **environment check** for each transport global; if the check fails, the process halts at this phase.
- Installer may print contents, compare against the current system, and verify checksums *before* proceeding.

### Phase 2 — Answering installation questions

- Installer uses the `Install Package(s) [XPD INSTALL BUILD]` option, selecting the entry from the INSTALL (#9.7) file.
- KIDS runs the environment check (which may allow install, cancel that transport global, or cancel the whole distribution).
- Installer answers pre-install questions, then standard KIDS questions, then post-install questions, **per transport global**.
- Installer chooses a device — direct run, queue, or abort.

### Phase 3 — Installation

- KIDS disables specified options/protocols (excluding those marked `USE AS LINK FOR MENU ITEMS`).
- KIDS optionally suspends TaskMan-queued options for the duration.
- For each transport global in sequence: pre-install routine → component installation → post-install routine.
- Disabled options/protocols are re-enabled; suspended TaskMan jobs are released.

### 2.1 INSTALL (#9.7) STATUS values

| Value | Meaning |
|---|---|
| 0 | Loaded from Distribution |
| 1 | Queued for Install |
| 2 | Start of Install |
| 3 | Install Completed |
| 4 | De-Installed |

Editable via the `XPD EDIT INSTALL` option. Setting `4` is an audit-only operation; no rollback is performed.

### 2.2 KIDS utility options for audit and inspection

From the Kernel KIDS Systems Management User Guide, "Utilities" menu:

- Build File Print
- Install File Print
- Edit Install Status (above)
- Display Patches for a Package
- Purge Build or Install Files
- Rollup Patches into a Build
- Update Routine File
- Verify a Build
- **Verify Package Integrity** — the formal post-install integrity check

### 2.3 Patch-level distribution: NPM

The **National Patch Module (NPM)** is the VA's patch governance and distribution system. Patches are released through FORUM as PackMan messages and tracked in NPM. A patch can be assigned status **"Entered in Error"** in NPM — the institutional governance signal that a patch has been formally retracted, used in coordination with site-level back-outs.

---

## 3. The DIBRG template (canonical, empirically validated)

**Empirical basis:** All 32 DIBRGs available in the `vistadocs/vdl` markdown corpus were scanned. Of these, **27 (84%) match the template exactly** and **3 more (9%) match with minor heading-text variations**, for a 94% conformance rate. Two DIBRGs (MD, VIAB) follow non-standard formats — see §3.1.

**Scope caveat:** The DIBRG template is the dominant *modern* artifact, but only **40 of the 128 pure-VistA packages** in the validated population (§13) carry a DIBRG in the index. **81 carry the older-style Install Guide** (`doc_code == 'IG'`); 36 carry neither (typically registries, very-stable packages, or sub-modules whose install is documented in a parent package). The §3 template is therefore authoritative for the modern-template subset — see §13.3 for the full coverage breakdown.

The canonical template:

```
1. Introduction
   1.1 Purpose
   1.2 Dependencies
   1.3 Constraints
2. Roles and Responsibilities
3. Deployment
   3.1 Timeline
   3.2 Site Readiness Assessment
       - Deployment Topology (Targeted Architecture)
       - Site Information (Locations, Deployment Recipients)
       - Site Preparation
   3.3 Resources (Facility · Hardware · Software · Communications)
4. Installation
   4.1 Pre-Installation and System Requirements
   4.2 Platform Installation and Preparation
   4.3 Download and Extract Files
   4.4 Database Creation
   4.5 Installation Scripts
   4.6 Cron Scripts
   4.7 Access Requirements and Skills Needed for the Installation
   4.8 Installation Procedure
   4.9 Installation Verification Procedure
   4.10 System Configuration
   4.11 Database Tuning
5. Back-Out Procedure
   5.1 Back-Out Strategy
   5.2 Back-Out Considerations (Load Testing · User Acceptance Testing)
   5.3 Back-Out Criteria
   5.4 Back-Out Risks
   5.5 Authority for Back-Out
   5.6 Back-Out Procedure
   5.7 Back-Out Verification Procedure
6. Rollback Procedure
   6.1 Rollback Considerations
   6.2 Rollback Criteria
   6.3 Rollback Risks
   6.4 Authority for Rollback
   6.5 Rollback Procedure
   6.6 Rollback Verification Procedure
```

Two structural points worth absorbing:

- **Back-Out and Rollback are separate.** Back-Out reverses the install; Rollback restores prior environment state from independent backups. A site may execute one without the other.
- **Each has its own Authority section.** Back-out authority typically rests with the Portfolio Director, VA Project Manager, and Business Owner (per ADT DIBRG). Rollback authority is similarly governed.

### 3.1 Variants and optional sections

The corpus reveals four real variant patterns plus a set of standardized optional sections. A DIBRG planning effort should treat these as menu items, not deviations.

#### 3.1.1 Multi-tier installation (KAAJEE pattern)

For deployments spanning multiple platform tiers (M-server + web tier + vendor application), the **Installation** section subdivides into per-tier installs. KAAJEE's DIBRG, for example, has separate H1s for `Patch Installation` (the M-server KIDS install) and `WebLogic Installation` (the J2EE tier). Use this variant when:
- The deployment involves more than just a KIDS build
- There are independent install procedures per tier
- Tier-specific back-out paths exist

When this variant is used, **§5 Back-Out Procedure should also subdivide by tier** to maintain symmetry with §4.

#### 3.1.2 Combined Back-Out / Rollback (BMS pattern)

For smaller-scope deployments where back-out and rollback collapse into the same procedure (typically because no platform-level snapshot is taken), §5 and §6 may be combined as a single "Rollback / Back-Out Plan" section. This is observed in older or simpler DIBRGs and is **not recommended for modern VistA deployments** — the separation of concerns in the canonical template is structurally important (see §1.4).

#### 3.1.3 "Artifact Rationale" prefatory section

Five DIBRGs in the corpus include an `Artifact Rationale` section between the title block and §1 Introduction. This is a standardized OIT addition that explains *why* the document exists, what governance authority requires it, and how it relates to other artifacts in the project's documentation set. Optional but recommended for any DIBRG produced under formal OIT governance.

#### 3.1.4 Multi-DIBRG packages (one DIBRG per release)

Several packages have multiple DIBRGs in the corpus, one per significant release:
- **PSO** has separate DIBRGs for "Inbound eRx" and "Pharmacy Operational Updates"
- **GMRC** has DIBRGs for "Consult Toolbox", "Decision Support Tool", and "EHM IFC Order Response"
- **YS (Mental Health)** has 4 distinct DIBRGs

This is the dominant pattern for actively maintained packages: **a DIBRG is an artifact of a release, not of a package**. The package may have many DIBRGs over its lifetime — each tied to a specific multi-build patch release.

#### 3.1.5 Standardized optional appendices

Common appendices found in the corpus, listed in order of frequency:

| Appendix | Frequency | Purpose |
|---|---|---|
| Acronyms / Definitions | 4 | Glossary for the patch's domain terms |
| Troubleshooting | 2 | Known issues and workarounds during install |
| Installation Example | 1 | Annotated transcript of a successful install |
| Post-Install Checksums | 1 | Routine checksums for site verification |
| Install File Print Example | 1 | Sample `Install File Print` output |
| Build File Print Example | 1 | Sample `Build File Print` output |
| Risk and Mitigation Plan | 1 | Operational risk register specific to install |
| Operational Procedures | 1 | Day-after-install runtime adjustments |

Recommended appendices for any non-trivial install: Acronyms, Troubleshooting, Post-Install Checksums.

#### 3.1.6 Legacy / non-standard formats (avoid)

Two DIBRGs in the corpus do not follow the modern template:

- **MD (Clinical Procedures)** combines an Install Guide and DIBRG into one document with version-specific H1s. This is a pre-template legacy format.
- **VIAB** uses a simpler structure (`Introduction` → `System Requirements` → `Patch Description and Installation Instructions` → `Backout and Rollback Procedure`) with no `Roles and Responsibilities` or `Deployment` sections. Suitable only for very small-scope, single-tier patches with no governance overhead.

New DIBRG production should not adopt these formats.

### 3.2 Population and corpus coverage

In the validated pure-VistA population (§13):

- **40 of 128 packages carry a DIBRG** in the master index — these are where the §3 template applies authoritatively
- **81 of 128 carry an older-style Install Guide** (`doc_code == 'IG'`) — pre-DIBRG-era artifacts that follow a different (and less standardized) structure
- **36 carry neither** — registries, deeply stable packages, or sub-modules covered by a parent package's documentation
- The full DIBRG count in the unfiltered VDL master index (including hybrids, Web clients, COTS, etc.) is 988 active across 67 packages — but only the 40 pure-VistA-package DIBRGs are in scope for this spec

Of the 40 pure-VistA DIBRG packages, **32 are markdown-converted in `vistadocs/vdl`** and constitute the empirical sample for §3.1 (94% template conformance). The 8 remaining DIBRGs exist only as PDF/DOCX on the VA VDL — not yet sampled. A complete validation would require pulling those 8 to confirm the conformance rate holds.

A complete *chronological* template-conformance study (using `patch_ver` to identify when the modern template stabilized) is out of scope for this spec but tractable as a follow-on study using the §13.6 filtered CSVs.

---

## 4. Pre-install gates (mapped to DIBRG §4.1–§4.7)

The DIBRG's "Pre-Installation" subsections enumerate the gates a site must close before install:

| Gate | DIBRG section | What it checks |
|---|---|---|
| A — Patch description review | 4.1 + 1.1 | Purpose, dependencies, constraints |
| B — Dependency verification | 1.2 | Required prior patches, related-package versions, file-existence |
| C — Currently-installed state | 4.1 | Drift check against shipped baseline; sequence position in `^XPD(9.7,"B")` |
| D — Environment readiness | 4.2 + 4.4 + 4.11 | Platform prep; `^XTMP` space; journaling; TaskMan state; HL7 link state |
| E — Backup | 4.8 (implicit) | Routine save (KIDS auto-saves to `^XTMP`); independent `^DD(file#)` and data-global save |
| F — Approval / change record | 5.5 | Pre-agreed back-out authority and criteria |

No install proceeds until all six gates close.

---

## 5. Install phase (mapped to KIDS §2 + DIBRG §4.8–§4.9)

The five sub-phases of §4 in v1 of this spec collapse into the canonical three KIDS phases — Load, Answer Questions, Install (see §2 above) — followed by:

### 5.1 Verification (DIBRG §4.9)
- INSTALL (#9.7) entry exists with STATUS `3 = Install Completed` and a populated `INSTALL COMPLETE TIME` (#17).
- Patch appended to `#9.4` PACKAGE patch history.
- Routine second-line patch list updated.
- Functional smoke tests from the patch description pass.
- (Optional but recommended) `Verify Package Integrity` run.

### 5.2 System configuration & DB tuning (DIBRG §4.10–§4.11)
Applies to non-trivial installs that introduce new HL7 links, new TaskMan jobs, or new files requiring journaling.

---

## 6. Back-Out (mapped to DIBRG §5)

### 6.1 Back-Out timing — three official phases

The ADT DIBRG defines three timing phases for any back-out decision:

| Phase | Mechanism | Notes |
|---|---|---|
| **Mirror Testing or Site Production Testing** | New version of the patch with corrections | Pre-national-release; cleanest path |
| **After National Release, During Designated Support Period** | Forward-fix patch (preferred) or detailed backout instructions from dev team | The 90-day warranty window is referenced in the ADT example; verify per-package |
| **After National Release and Warranty Period** | Routed through the VistA Maintenance Program, which produces a corrective or restorative patch | Site cannot back out unilaterally |

### 6.2 What a KIDS back-out can and cannot reverse

| Component | Reversible? | Mechanism |
|---|---|---|
| Routines | ✅ | Backup MailMan message generated at install; restorable per the patch description |
| Data dictionary changes | ❌ | Must be undone manually or via a follow-on patch |
| New FileMan files | ❌ | Removal requires manual data-archive plus DD removal |
| Data conversions of existing fields | ❌ | Forward-fix only |
| Components (options, keys, params, protocols) | ❌ (not auto-reversed) | Requires manual deletion + reinstate from prior backup |
| Cross-references rebuilt with new logic | ❌ | Forward-fix only |
| HL7 messages already transmitted | ❌ | Cannot be unsent |
| Mail messages already delivered | ❌ | Cannot be unsent |

### 6.3 Authority and audit (DIBRG §5.5 + NPM)

A back-out is not a site-level decision in VA-released content. The DIBRG names the authority chain:

- **Portfolio Director**
- **VA Project Manager**
- **Business Owner**
- Coordinated with **Health Product Support (HPS)** and the **development team**.

After the decision: the patch's NPM entry is set to **"Entered in Error"**, and a follow-up patch is published. This is the institutional record-of-truth for that the back-out occurred at the enterprise level.

### 6.4 Back-Out Procedure (the actual sequence)

1. Site logs ticket with Enterprise Service Desk (ESD).
2. Development team and HPS provide patch-specific back-out instructions (because, per §6.2, the procedure varies by what the patch touched).
3. Backup MailMan message identified (for routine restoration).
4. Routines restored from backup MailMan message.
5. Data dictionary components manually reverted (or deferred to a follow-on back-out patch designed for this purpose).
6. INSTALL (#9.7) STATUS set to `4 = De-Installed` via `XPD EDIT INSTALL`.
7. Back-Out Verification Procedure (DIBRG §5.7) executed.

### 6.5 Back-Out Considerations the DIBRG enforces

- **Load Testing** — Can the back-out itself run during business hours, or does it need a maintenance window?
- **User Acceptance Testing** — What functional regression suite must pass post-back-out for the site to declare the system fit for clinical use?
- **Risks** — Functional capabilities lost by reverting (the ADT DIBRG enumerates these explicitly per patch).

---

## 7. Rollback (DIBRG §6) — distinct from Back-Out

**Rollback is environment-level restoration**, not patch-level reversal. Rollback uses platform/database snapshots created independently of KIDS.

A typical rollback strategy from the corpus:
1. At deployment, take a complete system backup before any patch install.
2. If install fails catastrophically, restore the snapshot.
3. After clinical validation, take a second snapshot as the new baseline.
4. Subsequent backups operate against the post-install baseline.

Rollback's authority chain mirrors back-out's. Rollback's risks are different in kind: data loss for any clinical activity since the snapshot.

A site may rollback without backing out (system-level restore covers everything), or back out without rolling back (surgical patch reversal, environment otherwise unchanged).

---

## 8. Flavor-specific notes (corpus-confirmed)

### 8.1 VA production VistA
The DIBRG is the institutional artifact. NPM is the governance system. FORUM is the distribution channel. Authority chains follow OIT structure.

### 8.2 WorldVistA EHR / OSEHRA / vxVistA
The KIDS engine is identical (Kernel 8.0). The DIBRG concept does not have a community equivalent — open-source releases ship release notes plus the KID file. Sites outside VA must construct their own back-out plans; the DIBRG template in §3 is the recommended starting structure.

### 8.3 Client-side software (Windows GUI components)

Distinct from server-side (M) installs. Examples in the corpus:

- **CPRS GUI** — Windows installer
- **BCMA GUI** — Windows installer
- **VIX Viewer** (MAG) — Windows installer with a documented client uninstall path (`MAG*3.0*358 Client Uninstall`)
- **EDIS** — Server + client, two separate install procedures

These have OS-native uninstall paths. Confusing client uninstall with server "uninstall" is a documented hazard — the MAG DIBRG header is the only place "Uninstall" appears prominently in the four DIBRGs sampled, and it refers exclusively to the Windows VIX client.

---

## 9. Audit trail (mapped to KIDS Utilities + DIBRG verification sections)

| Source | What it records | Authoritative VDL section |
|---|---|---|
| `INSTALL (#9.7)` | Per-install: name, timestamp, installer, STATUS (`0`–`4`), INSTALL COMPLETE TIME | KIDS Sys Mgmt UG §"Information Stored in the INSTALL (#9.7) File" |
| `PACKAGE (#9.4)` patch history | Patch list per package version | KIDS Sys Mgmt UG §"Changes in the Role of the PACKAGE (#9.4) File" |
| `BUILD (#9.6)` | Build definition (developer-side) | KIDS Sys Mgmt UG §"Build Entries…" |
| Routine 2nd line | `;;version;package;**patches**;date` | Routine convention |
| `^XTMP("XPD…")` | KIDS auto-backup of overwritten routines | XTMP Global User Guide |
| Backup MailMan message | Site-side routine snapshot for backout | DIBRG §5.6 |
| FORUM / NPM | Released patch metadata; "Entered in Error" status | NPM Operational Summary |
| KIDS Utilities (Build/Install File Print, Display Patches, Verify Package Integrity) | On-demand inspection | KIDS Sys Mgmt UG §"KIDS: System Management—Utilities" |

Reconciliation queries the audit plan must support are unchanged from v1 §7.2.

**Cross-reference (v7):** The pre-install pre-flight extension of this audit framework is specified in the companion document `vista-package-state-audit-plan.md`. §9 enumerates *where evidence lives*; the standalone plan specifies *how to extract and analyze that evidence to predict KIDS pre-install check outcomes ahead of time*.

---

## 10. References (corpus-grounded)

### 10.1 KIDS / Install mechanism (infrastructure)
- [KIDS Systems Management User Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-systems-management-kids-user-guide.md) — installer-side primary source; phases, options, INSTALL #9.7 STATUS values
- [KIDS Developer's Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-developer-s-guide-kids-user-guide.md) — developer-side primary source; build creation and distribution
- [Kernel Technical Manual](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/technical-manual.md) — file structure reference
- [XTMP Global User Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--kernel-8-0-developer-s-guide-xtmp-global-user-guide.md) — backup global semantics
- [Kernel DIBRG](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/deployment-installation-back-out-and-rollback-guide.md) — the meta-example (Kernel installing itself)
- [VistA Build Analyzer Utility (XU*8.0*782) User Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/xu--kernel/user-manual--vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782.md) — drift/integrity inspection tool
- [NPM Installation Guide](https://github.com/vistadocs/vdl/blob/main/infrastructure/npm--national-patch-module/installation-guide.md)
- [NPM Operational Summary](https://github.com/vistadocs/vdl/blob/main/infrastructure/npm--national-patch-module/supplement--operational-summary.md)

### 10.2 DIBRG exemplars (clinical packages)
- [ADT DIBRG](https://github.com/vistadocs/vdl/blob/main/clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md) — most fully fleshed-out back-out strategy section in the sample
- [MAG (Imaging) DIBRG](https://github.com/vistadocs/vdl/blob/main/clinical/mag--vista-imaging-system/deployment-installation-back-out-and-rollback-guide.md) — illustrates client-software uninstall distinction
- [PSO Inbound eRx DIBRG](https://github.com/vistadocs/vdl/blob/main/clinical/pso--pharmacy-outpatient-pharmacy/deployment-installation-back-out-and-rollback-guide--inbound-eprescribing-dibr.md) — large multi-component (Apache, Java, WebLogic, M) install showing the template's flexibility
- Other DIBRGs in corpus: ANRV, CHDS, GMRC (3 variants), PSA, PX, SD, DRM (combined install/DIBRG), LA (autorelease)

### 10.3 v4 deliverables (filtered artifacts, see §13)
- `vdl_inventory_vista_only.csv` — 6,020 rows × 30 cols, the filtered raw inventory
- `vista_packages_summary.csv` — 128 packages × 13 fields, the package-level summary with documentation-coverage flags

### 10.4 Prior versions of this spec (superseded)
v1 (inferred), v2 (corpus-grounded), v3 (empirically validated DIBRG template). Section structure unchanged in v4; population scope formally defined and validated.

### 10.5 Out of scope (unchanged from v2)
- Specific menu navigation paths beyond the named option keywords
- Vendor-specific (Caché/IRIS/GT.M/YottaDB) global save formats
- HL7 logical link management procedures
- TaskMan administration

---

## 11. Open decisions (carried forward; updated)

- [ ] Backup retention policy — `^XTMP` 90-day default vs. extended
- [ ] Back-out window — typically = backup retention; 90-day VA warranty period referenced in ADT DIBRG
- [ ] Drift baseline source — VistA Build Analyzer (`XU*8.0*782`) vs. site-snapshot
- [ ] Audit reconciliation cadence — per-install vs. periodic
- [ ] Whole-package retirement governance (not addressed in DIBRG template; treat as out-of-band)
- [ ] Cross-flavor install policy (VA → WorldVistA, vice versa) — typically prohibited
- [ ] Test patch acceptance policy
- [ ] **NEW — DIBRG production policy:** if this spec is implemented for a non-VA VistA flavor, will the site/project produce a DIBRG per release using the §3 template?
- [ ] **NEW — Authority chain for back-out:** non-VA sites must define their own equivalent of the Portfolio Director / PM / Business Owner trio
- [ ] **NEW v4 — IG-cohort coverage:** 81 of 128 pure-VistA packages use the older Install Guide format. Will this spec be extended with parallel IG-template guidance, or restricted to the modern-template (DIBRG) cohort only?
- [ ] **NEW v4 — Parent-package documentation map:** 36 of 128 packages have neither IG nor DIBRG. Define a policy for how install/back-out is handled for these (typically via a parent package's documentation).
- [ ] **NEW v4 — Validated population refresh cadence:** the §13 filter was applied against a snapshot of `vdl_inventory_enriched.csv`. Define a refresh cadence (quarterly? on-demand?) for re-running the filter and updating the §13 numbers.
- [ ] **NEW v5 — Reconciliation tooling ownership:** the M-side extractor proposed in §14.5 is plausibly an enhancement to existing tooling (Build Analyzer XU\*8.0\*782 or Patch Monitor XT\*7.3\*98). Decide whether to extend an existing tool or namespace a new one (e.g. XPDREC).
- [ ] **NEW v5 — NPM extraction interface:** §14.6 assumes manual export from FORUM until an NPM API exists. Decide whether to track NPM-API requests with VA OIT or build the reconciler around scheduled manual exports.
- [ ] **NEW v5 — Reconciliation cadence:** monthly drift detection vs. on-demand vs. continuous. Each implies a different infrastructure footprint.
- [ ] **NEW v5 — Discrepancy report distribution:** who consumes the §14.7 report — IRM, VISN, national, all of the above? Distribution determines the report's redaction policy and detail level.

---

## 12. Discovery and query patterns

The discovery and query patterns originally drafted in this section (v3) have been extracted to a standalone reusable resource:

**Companion document:** [`vdl-query-patterns.md`](./vdl-query-patterns.md) — *VDL Query Patterns: A Reusable Discovery Guide*

That document is the canonical reference for VDL discovery across all projects, not just this spec. It covers:

- **§2** — The three-tier reference architecture (index / converted content / canonical source)
- **§3** — The master index `vdl_inventory_enriched.csv` — schema, document type taxonomy, document layer taxonomy, system type taxonomy, section taxonomy
- **§4** — The content tier `vistadocs/vdl` — structure, frontmatter conventions, anchor consolidation pattern
- **§5** — Scope filters (active-only, pure-VistA, by section, by namespace, by document type, combinations)
- **§6** — Query recipes A–J
- **§7** — Data quality caveats with mitigations
- **§8** — The discovery workflow
- **§9** — Recommended reusable environment for teams using LLMs / RAG over the corpus
- **§10** — Citation conventions
- **§11** — Companion documents and follow-on work

### How this spec uses the standalone guide

| This spec's section | Uses this from the standalone guide |
|---|---|
| §10 (References) | The §10 citation conventions of the standalone guide; the §6 recipes were used to populate the references |
| §13 (Population scope) | Recipe G — the canonical pure-VistA filter — applied as the spec's scope rule |
| §13.5 (Data quality caveats) | The standalone guide's §7 is the canonical caveats list; §13.5 captures the subset *discovered during this spec's validation* |
| §14 (Reconciliation) | The §8 discovery workflow was used to identify Build Analyzer, NPM, VPSRT, and Patch Monitor as authoritative reconciliation tooling |

When working on a follow-on VistA documentation effort that doesn't share this spec's specific scope, refer to the standalone document directly.

---

## 13. Population scope and coverage validation (new in v4)

This section formally defines what "VistA package" means for the purposes of this spec, applies that definition as a filter against the master VDL index, and reports the resulting validated population. The filter is the canonical scoping rule for any analysis or claim made elsewhere in the spec.

### 13.1 Defining "pure VistA M application"

The VistA Documentation Library is a superset. It indexes documentation for many systems that are *adjacent to* VistA without being VistA themselves: Web clients, VA enterprise services, integration middleware, COTS products, and various hybrid configurations. A spec scoped to "VistA package install/uninstall" must narrow this universe before its claims can be validated.

The CSV's `system_type` column provides the institutional vocabulary. Its 11 distinct values, with row counts, are:

| `system_type` value | Rows | In scope? |
|---|---|---|
| `VistA` | 6,074 | ✅ included |
| `Web client` | 896 | ❌ excluded — not VistA M |
| `VA enterprise service` | 518 | ❌ excluded — not VistA M |
| `Integration middleware` | 361 | ❌ excluded — not VistA M |
| `VistA + GUI` | 316 | ❌ excluded — hybrid |
| `VistA + COTS` | 309 | ❌ excluded — hybrid |
| `VBA system` | 144 | ❌ excluded — Veterans Benefits Admin, distinct from VHA |
| `COTS product` | 102 | ❌ excluded — not VistA |
| `Data patch` | 64 | ❌ excluded — data-only, not an "application" |
| `VistA + middleware` | 35 | ❌ excluded — hybrid |
| `Program documentation` | 15 | ❌ excluded — meta-documentation |

The `section_name` column carries an additional dimension: `VistA/GUI Hybrids (formerly HealtheVet)` is a top-level section housing 780 rows. **54 of those rows have `system_type == 'VistA'`** — they are M-side documents for packages whose overall identity is hybrid. Per the strict scope, these are excluded with the rest of the section.

### 13.2 The canonical filter

> `system_type == 'VistA'` AND `section_name != 'VistA/GUI Hybrids (formerly HealtheVet)'`

This is the rule. Apply it before any package-level analysis claiming "VistA scope."

**Result:** 6,020 rows / 2,496 unique documents (deduped on `doc_slug`) / **128 unique packages**.

Verification: zero packages in the filtered set carry a populated `cots_dependent` column. The filter produces no leakage.

### 13.3 Documentation coverage analysis

Of the 128 pure-VistA packages, the presence of standard document types is:

| Document type | `doc_code` | Packages with at least one | Coverage |
|---|---|---|---|
| Technical Manual | `TM` | 93 / 128 | 73% |
| Install Guide (legacy) | `IG` | 81 / 128 | 63% |
| Release Notes | `RN` | 70 / 128 | 55% |
| DIBRG (modern install/back-out) | `DIBR` | 40 / 128 | 31% |

**Cross-tabulation of install-related coverage:**

- 40 packages have a DIBRG
- 81 packages have an Install Guide
- 36 packages have **neither** an IG nor a DIBRG

The 36-package "neither" bucket is significant. Manual review suggests three explanations:

1. **Registry packages** — many of the `Registry: *` packages (PXRM-AHOBPR, ROEB Breast Cancer, ROEG MS Surveillance, ROEV Eye Vision Injury, etc.) are tightly coupled to their parent package and don't ship independent install docs.
2. **Pharmacy sub-modules** — some pharmacy submodules' installation is folded into PSO, PSJ, or PSS parent-package documentation.
3. **Very stable / decommissioned packages** — packages with no modern release activity often retain only their historical TM and UM, with no current install artifact.

**Implication for §3:** the DIBRG template is authoritative for the 40-package modern-template cohort; the 88-package remainder is covered by either the IG tradition or by parent-package documentation. A complete VistA install/back-out spec would need parallel template guidance for the IG cohort — out of scope for v4 but identified as a follow-on (see §13.7).

### 13.4 Section breakdown of the validated population

| Section | Packages | Documents (deduped) | Active rows | Archive rows | Decommissioned rows |
|---|---|---|---|---|---|
| Clinical | 73 | ~1,800 | ~2,650 | ~1,600 | ~110 |
| Financial-Administrative | 27 | ~450 | ~700 | ~380 | ~3 |
| Infrastructure | 28 | ~250 | ~330 | ~250 | ~1 |
| **Total** | **128** | **2,496** | **3,674** | **2,232** | **114** |

Status reading: the population is healthy — 61% of rows are `active`, 37% `archive`, 2% `decommissioned`. The high `archive` proportion reflects the cumulative-history nature of VistA's documentation (every superseded version is preserved, not deleted), not a fleet of dead packages.

### 13.5 Data quality caveats discovered during validation

Three caveats discovered during this analysis. **The canonical, comprehensive list of VDL data quality caveats lives in `vdl-query-patterns.md` §7** — that companion document is the source of truth for users of the VDL across all projects. The caveats below are the subset *discovered or reaffirmed during this spec's v4 validation work*; they overlap with the canonical list but are framed in this spec's context.

All are stable enough not to block use but should be coded around in any tooling.

#### 13.5.1 `app_name_full` occasionally reflects document subject, not package canonical name

Several rows in the filtered set carry an `app_name_full` that does not match the package's canonical identity. Confirmed examples:

| `app_name_abbrev` | `app_name_full` (in CSV) | Canonical package name |
|---|---|---|
| `OR` | "Group Notes" | Order Entry / CPRS |
| `XU` | "Name Standardization" | Kernel |
| `PXRM` | "Registry: Airborne Hazard Open Burn Pit" | Clinical Reminders |

The `app_name_full` value appears to reflect a *specific document subject* in some rows rather than the package's overall canonical name. **Do not use `app_name_full` as the authoritative package name.** Use `app_name_abbrev` and cross-reference against the markdown-corpus folder names or the official VA package list (e.g. via `pkg_ns` lookup against the Kernel `PACKAGE` file #9.4).

#### 13.5.2 `pkg_ns` is sparsely populated

Roughly 70% of the 128 filtered packages have `pkg_ns` blank. The namespace is recoverable from `app_name_abbrev` for most packages but not all (some abbreviations differ from the M namespace, e.g. `ANRV` for VIST). Tooling that depends on `pkg_ns` must include a fallback inference.

#### 13.5.3 Namespace duplicates from KMP\* consolidation era

Some packages appear under multiple `app_name_abbrev` values reflecting historical naming changes:

- `RUM` and `KMPR` — both Resource Usage Monitor
- `SAGG` and `KMPS` — both Statistical Analysis of Global Growth
- `SSO` and `SSO/UC` — both Single Signon/User Context

These duplicates are an artifact of the KMP\* (Kernel Management Package) consolidation. Dedupe rules should treat these pairs as the same package for any inventory analysis.

#### 13.5.4 PDF/DOCX double-counting (already documented in §12.5.1)

Reaffirmed in the filtered set: the 6,020 rows collapse to 2,496 unique documents after `doc_slug` dedup. Always dedupe before counting documents.

#### 13.5.5 UTF-8 mojibake (already documented in §12.5.2)

Reaffirmed in the filtered set; affects display only.

### 13.6 Filtered deliverables

Two CSV artifacts produced during v4 validation, intended to be reused as authoritative scope-definition inputs for any future VistA-pure analysis:

| Artifact | Rows × cols | Purpose |
|---|---|---|
| `vdl_inventory_vista_only.csv` | 6,020 × 30 | Schema-identical to the source CSV; drop-in for any pipeline that consumes `vdl_inventory_enriched.csv`. |
| `vista_packages_summary.csv` | 128 × 13 | Package-level summary: abbrev, full name, namespace(s), section, status, raw and deduped doc counts, doc-type list, presence flags for DIBRG / IG / TM / RN, patch-doc count. |

Both artifacts were generated from `vdl_inventory_enriched.csv` using Recipe G (§12.4). Regenerate when the source CSV updates.

### 13.7 Out-of-scope items identified during this validation

These are tractable follow-on studies that would extend the spec's authority:

- **Install Guide template study.** Sample IGs across the 81 IG-carrying packages and produce a §3-equivalent template description. Likely shows multiple historical templates corresponding to different documentation eras.
- **Modern-template chronology.** Sort all 988 unfiltered DIBRGs by `patch_ver_major` × `patch_ver_minor` × `patch_num` and identify the patch year at which the §3 template stabilized. Hypothesis: late-2010s OIT standardization.
- **Parent/sub-package install dependency map.** For the 36 packages with no IG and no DIBRG, identify which parent package's documentation actually covers their installation. Likely concentrated in PSO, PSJ, PSS, OR, and a few infrastructure packages.
- **Cross-reference to Kernel `PACKAGE` (#9.4) file.** Compare the 128-package list against an actual VistA instance's `PACKAGE` file to identify any pure-VistA packages that exist in code but lack VDL documentation, or vice versa.

### 13.8 Spec-level claim qualification

In light of §13, the spec's claims should be read with these scope qualifications:

| Spec section | Claim scope after v4 validation |
|---|---|
| §2 (KIDS mechanism) | Universally authoritative — Kernel is in the Infrastructure section of the validated population |
| §3 (DIBRG template) | Authoritative for ~40/128 packages (modern-template cohort) |
| §4–§7 (gates, install, back-out, rollback) | Authoritative for the modern-template cohort; partially applicable for IG-cohort packages |
| §8 (flavor-specific) | Unchanged; the filter applies equally to all flavors |
| §9 (audit trail) | Universally authoritative — the audit primitives (`#9.7`, `#9.4`, NPM, etc.) are package-independent |
| §12 (discovery) | Universally applicable across the entire VDL, with Recipe G as the in-scope filter |
| §13 (this section) | Validated population definition; treat as scope-of-truth for v4 onward |

---

## 14. Patch state and pre-install audit

The patch-state reconciliation framework originally drafted in this section (v5) has been extracted and reframed as a standalone deliverable focused on pre-install pre-flight prediction:

**Companion document:** [`vista-package-state-audit-plan.md`](./vista-package-state-audit-plan.md) — *VistA Package State and Sequence Audit & Reconciliation Automation Plan*

That document specifies how a package developer can predict whether a proposed patch will pass KIDS pre-install check on a target VistA system *without* requiring an OIT engineer to manually load and trial-install the KID file. It covers:

- **§2** — What KIDS pre-install check actually does (the three-phase install sequence and the checks performed in Phase 1 + Phase 2)
- **§3** — The pre-flight problem from a developer perspective and what pre-flight cannot predict
- **§4** — **The eight-class blocker taxonomy** (B1–B8 with 32 sub-classes) covering patch dependency, sequence, structural, drift, component conflict, environment readiness, custom env-check, and authorization blockers
- **§5** — Sources of state needed for the audit (the v5 §14 sources plus the KID file itself)
- **§6** — Three-tier architecture: M-side state extractor + KID file analyzer + external pre-flight engine
- **§7** — Tier 1 (M-side extractor — extends the original v5 §14.6 specification with B3, B5, B6c, B8a/b sources)
- **§8** — Tier 2 (KID file analyzer — new artifact)
- **§9** — Tier 3 (pre-flight engine with severity propagation: green/yellow/red verdict)
- **§10** — The pre-flight blocker report structure
- **§11** — Existing tools to reuse (Build Analyzer XU\*8.0\*782, Patch Monitor XT\*7.3\*98, VPSRT XT\*7.3\*143)
- **§12** — Phased rollout (8 phases, ~3 months for ~78% sub-class coverage)
- **§13** — Out of scope (Phase-3 runtime, performance, multi-site fleet, automated KID modification)
- **§14** — Open decisions
- **§16** — References

### How this spec relates to the standalone plan

| This spec | Standalone plan |
|---|---|
| §1.4 (DIBRG as institutional answer to install/uninstall) | §2 (what KIDS does — informs the blocker classification) |
| §2 (KIDS three-phase install) | §2 (background) — same source material |
| §4 (Pre-install gates A–F) | §4 (blocker taxonomy) — gates are the human-process counterpart of the engine's automated checks |
| §6 (Back-Out) — eight-class discrepancy taxonomy D1–D8 (post-hoc) | §4 — eight-class blocker taxonomy B1–B8 (pre-flight). The two taxonomies are related but distinct; D-classes describe state inconsistencies, B-classes describe install-time refusals. |
| §9 (Audit trail) | §5 (sources of state) — same enumeration extended for pre-flight |
| §13 (Population scope) | §1 / §13 — pre-flight applies to the same 128-package pure-VistA scope |

### When to use which document

- **Use this spec (v7)** for governance, planning, and process work around install/uninstall lifecycle.
- **Use the standalone plan** when implementing or evaluating a pre-flight tooling effort.

The two documents are designed to be read together but each stands alone.
