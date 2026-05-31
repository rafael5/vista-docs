# VistA Patch and Package Risk Stratification Heuristic

**Subject:** A two-axis risk-classification framework for VistA patches (per-build) and packages (inherent), derived empirically from the existing DIBRG corpus
**Audience:** Patch developers, SQA engineers, DIBRG authors, OIT install reviewers, and pre-flight tooling implementers
**Mode:** Specification and analytical reference — no executable code
**Status:** Standalone reusable resource; companion to `vista-package-lifecycle-spec-v7.md`, `vista-package-state-audit-plan.md`, and `vdl-query-patterns.md`

---

## 1. Executive summary

Not every VistA patch carries the same operational risk. A read-only registry-update patch and a Patient-file data-conversion patch both pass through KIDS, but the consequences of getting one wrong differ by orders of magnitude. This document specifies a **two-axis risk-stratification framework** that lets developers, reviewers, and pre-flight tools assign a calibrated risk level to any patch or package.

**Axis 1 — Per-patch risk** (varies by build, derived from DIBRG content):
- **L1 — Low** — read-only extractors, new functionality only, trivially reversible
- **L2 — Moderate** — typical maintenance patches with limited blast radius
- **L3 — High** — substantial changes, cross-package or external impact
- **L4 — Critical** — Kernel/FileMan/HL7 layer, infrastructure-wide effect

**Axis 2 — Package inherent risk** (varies by package, derived from package characteristics):
- **P1 — Low** — registries, reports, self-contained extracts
- **P2 — Moderate** — clinical packages with bounded scope
- **P3 — High** — clinical packages with extensive cross-package DBIAs and HL7 traffic
- **P4 — Critical** — infrastructure (Kernel, FileMan, MailMan, HL7, RPC Broker, TaskMan)

**Combined risk = max(L, P).** A low-risk patch on a high-risk package is still high-risk because the package's structural exposure dominates. The framework is conservative by design.

The heuristic is empirically grounded: §3 reports the indicator distribution across all 32 DIBRGs available in the `vistadocs/vdl` markdown corpus; §4 places those 32 patches into the L-strata; §6 places the 128 pure-VistA packages (per the §13 filter of the lifecycle spec) into the P-strata.

---

## 2. Method

### 2.1 Source corpus

- **32 DIBRGs** in the `vistadocs/vdl` markdown corpus — the empirical sample for patch-level (L) classification
- **128 pure-VistA packages** (per `vista-package-lifecycle-spec-v7.md` §13 filter) — the population for package-level (P) classification
- **No content extraction beyond what is in the DIBRG itself** — risk is read off the developer's own statements in the Constraints, Back-Out Strategy, Back-Out Risks, and Back-Out Procedure sections

### 2.2 Scanning method

For each DIBRG, the analysis searched for fourteen risk-indicator phrase patterns covering structural changes (data dictionary, routine modification, cross-references), cross-system entanglement (HL7, external systems, DBIAs), reversibility (no-backout warnings, irreversibility statements), operational impact (TaskMan, journaling, restart requirements), clinical impact (patient care, patient safety), and governance signals (warranty period, security controls, emergency back-out language).

Each indicator's presence is binary (present or absent in the DIBRG text). A simple **composite "danger score"** counts the presence of eight high-impact indicators: routine modification, data conversion, HL7 changes, data dictionary changes, external system entanglement, no-backout warnings, emergency-class language, and patient care impact.

### 2.3 Validation

The ranking produced by composite score was validated by manual inspection of the top 10 and bottom 10 DIBRGs. The patches at the extremes match clinical/operational intuition: ADT (DG\*5.3\*952 family) at the top — patient-record dictionary changes in core registration; ANRV / CHDS / PSA / KAAJEE at the bottom — additive functionality in bounded packages.

---

## 3. Findings — indicator distribution

Across 32 DIBRGs:

| Indicator | Count (of 32) | Percent |
|---|---|---|
| Mentions data dictionary change | 16 | 50% |
| Mentions security control or key | 14 | 44% |
| Mentions patient care or safety | 13 | 41% |
| Mentions "no impact" / "no risks" / new-only language | 12 | 38% |
| Mentions warranty period or support window | 10 | 31% |
| Mentions restart / reboot / recompile | 9 | 28% |
| Mentions emergency-class scenario | 8 | 25% |
| Mentions modifying existing routines | 7 | 22% |
| Mentions external system entanglement | 5 | 16% |
| Mentions HL7 message change | 4 | 12% |
| Mentions data conversion | 4 | 12% |
| Mentions TaskMan dependency | 3 | 9% |
| Mentions journaled-global change | 1 | 3% |
| Mentions irreversibility / "do not back out" | 1 | 3% |

**Interpretation:**

- DD changes are common (~50%); modifying *existing routines* is less common (~22%) — most patches add rather than overwrite
- Patient-care language is present in 41% of DIBRGs — a significant minority where the developer explicitly raises clinical risk
- Cross-system entanglement (external systems + HL7) is rarer (~28% combined) but heavily concentrated in specific packages (financial-administrative, MAG imaging)
- Outright irreversibility statements are rare (3%) — developers almost always claim some path to back-out, even when complex

---

## 4. Per-DIBRG empirical risk classification

The 32 DIBRGs ranked by composite danger score:

### 4.1 High-risk patches (composite score ≥ 4) — 4 DIBRGs

| Pkg | Section | DIBRG | Score | Risk indicators present |
|---|---|---|---|---|
| **ADT** (DG family) | Clinical | DG\*5.3\*952 family DIBRG | 6 | Modifies routines, HL7, DD changes, no-backout warning, emergency, patient care |
| **MAG** | Clinical | MAG\*3.0\*358 (VIX) DIBRG | 4 | DD changes, external system, emergency, patient care |
| **ECME** | Financial-Admin | MCCF EDI TAS Build 5/6 DIBRG | 4 | Modifies routines, DD changes, external system, emergency |
| **IB** | Financial-Admin | MCCF EDI TAS eBilling Build 5/6 DIBRG | 4 | Modifies routines, DD changes, external system, emergency |

**Common pattern:** patient-record or financial-clearinghouse interaction with cross-system dependencies. ADT is the highest because it touches the patient identity layer that every clinical package depends on.

### 4.2 Moderate-to-high risk patches (score 2–3) — 14 DIBRGs

GMRC (Decision Support Tool, Consult Toolbox), PSO (multiple variants), PX (PCE), VIAB, YS (Mental Health Assistant), and several others. Typical pattern: DD changes plus one of (routine modification, external interface, patient care impact).

### 4.3 Low-risk patches (score 0–1) — 14 DIBRGs

| Pkg | Section | DIBRG | Score |
|---|---|---|---|
| **ANRV** | Clinical | Blind Rehabilitation DIBRG | 0 |
| **CHDS** | Clinical | Clinical Health Data Repository DIBRG | 0 |
| **GMRC** | Clinical | Consult Toolbox DIBRG | 0 |
| **PSA** | Clinical | Pharmacy API DIBRG | 0 |
| **KAAJEE** | Infrastructure | KAAJEE SSO/WAP DIBRG | 0 |
| **CDSP** | VistA-GUI | Clinical Decision Support Platform DIBRG | 0 |
| **YS** (one variant), **BMS**, **PRC**, **XU** (one variant) | various | various | 1 |

**Common pattern:** new functionality only, no modification of existing components, self-contained scope, "no known back-out risks" stated. Most explicitly use phrases like "no impact" or "no known risks" in the DIBRG.

### 4.4 What the empirical ranking does *not* capture

The composite score is a starting point, not a verdict. Three known limitations:

1. **DIBRG language is not always candid.** A developer who underestimates risk produces a low-scoring DIBRG even when the actual risk is high. Manual review remains essential for medium-and-above patches.
2. **The 32-DIBRG sample skews modern.** Older DIBRGs (pre-OIT-template) are underrepresented in the markdown corpus. The 956 active DIBRGs not yet markdown-converted may follow different patterns.
3. **No correlation with realized incidents.** This is paper risk — what the DIBRG says — not realized failure rates. A future study should compare DIBRG risk scores against actual back-out rates from NPM "Entered in Error" history.

---

## 5. The patch-level risk heuristic (Axis 1)

### 5.1 Seven risk dimensions

Each dimension is scored independently across four levels: **None / Low / Medium / High / Critical**. The aggregate L-stratum is determined by combining dimension scores (see §5.2).

#### D1 — Code impact

| Level | Indicator |
|---|---|
| None | No routine changes |
| Low | New routines only |
| Medium | Modifies routines owned by this package |
| High | Modifies routines that other packages call via DBIA |
| Critical | Modifies Kernel / FileMan / HL7 / RPC Broker / TaskMan core routines |

#### D2 — Data dictionary impact

| Level | Indicator |
|---|---|
| None | No DD changes |
| Low | New file(s) only; no changes to existing |
| Medium | Adds fields to existing files; no type changes |
| High | Changes existing field types or removes fields; modifies cross-references on populated data |
| Critical | DD changes to clinical data files (#2 PATIENT, #44 HOSPITAL LOCATION, #50 DRUG, #63 LAB DATA, #200 NEW PERSON, #355.1–#356 IB-billing files) |

#### D3 — Cross-package impact

| Level | Indicator |
|---|---|
| None | Self-contained |
| Low | Consumer-side DBIA usage only |
| Medium | Modifies DBIA contracts the package is custodian of (Supported / Controlled) |
| High | Modifies DBIA contracts that have many consumer packages |
| Critical | Changes core ambient APIs (XUSER, VADPT, DBS APIs in DI, XPAR) |

#### D4 — External / cross-system impact

| Level | Indicator |
|---|---|
| None | No external interface touched |
| Low | Internal HL7 traffic only (intra-VistA) |
| Medium | External HL7 traffic to a single trading partner |
| High | External HL7 traffic to multiple partners; cross-organizational interfaces |
| Critical | National-scale external interfaces (FSC, HCCH, eRx network, PBM, NDF) |

#### D5 — Reversibility

| Level | Indicator |
|---|---|
| None | No state changed |
| Low | Pure additive — back-out by removing new components |
| Medium | Routine restoration only (KIDS-standard back-out works) |
| High | Some side-effects are irreversible (data created, messages sent) |
| Critical | Multiple irreversible side-effects; back-out is forward-fix only |

#### D6 — Clinical impact

| Level | Indicator |
|---|---|
| None | Non-clinical (financial, administrative, infrastructure) |
| Low | Reports and extracts only |
| Medium | Configuration / workflow changes affecting clinical users |
| High | Direct clinical decision support changes; medication/order pathway changes |
| Critical | Direct patient-record modification logic (PSO/PSJ dispensing, ADT registration, PX encounters, OR ordering) |

#### D7 — Operational impact

| Level | Indicator |
|---|---|
| None | No operational changes required |
| Low | No restart; KIDS install completes in normal window |
| Medium | Routine recompile required; brief operational degradation |
| High | Service restart required; HL7 link bounce; user notification needed |
| Critical | Full maintenance window required; downtime exceeds normal patch install duration |

### 5.2 Aggregation into L-strata

| Stratum | Aggregation rule |
|---|---|
| **L1 — Low** | All dimensions ≤ Low; OR at most one dimension at Medium with all others ≤ Low |
| **L2 — Moderate** | Multiple dimensions at Medium; no dimension at High or Critical |
| **L3 — High** | One or more dimensions at High; no dimension at Critical |
| **L4 — Critical** | Any dimension at Critical |

The rule is conservative — the highest-risk dimension dominates. This is intentional: a single critical dimension (e.g. modifying core Kernel routines) makes the patch critical regardless of how clean the other six dimensions are.

### 5.3 Worked examples

**ADT DG\*5.3\*952 family DIBRG** (empirical score 6):
- D1 Code impact: Medium (modifies own routines)
- D2 DD impact: **Critical** (modifies #2 PATIENT and #27.11 PATIENT ENROLLMENT)
- D3 Cross-package: High (every clinical package depends on PATIENT)
- D4 External: None
- D5 Reversibility: High (DD changes are irreversible, must use forward-fix patch per DIBRG)
- D6 Clinical: **Critical** (direct patient-record modification logic)
- D7 Operational: Medium

→ Aggregate: **L4 (Critical)** — driven by D2 and D6.

**ANRV Blind Rehabilitation DIBRG** (empirical score 0):
- D1 Code impact: Low (new routines only)
- D2 DD impact: Low (new file(s) only)
- D3 Cross-package: None
- D4 External: None
- D5 Reversibility: Low (additive)
- D6 Clinical: Low (reports/extracts in a bounded specialty domain)
- D7 Operational: None

→ Aggregate: **L1 (Low)**.

**MAG\*3.0\*358 (VIX) DIBRG** (empirical score 4):
- D1 Code impact: Medium
- D2 DD impact: Medium
- D3 Cross-package: Medium
- D4 External: High (DICOM, image network)
- D5 Reversibility: High (back-out "would significantly impact patient care")
- D6 Clinical: High (image viewer used in clinical decisions)
- D7 Operational: Medium

→ Aggregate: **L3 (High)** — driven by D4, D5, D6.

---

## 6. The package-level inherent risk classification (Axis 2)

Some packages are inherently riskier to patch than others, regardless of what the patch does. A trivial-looking patch to FileMan is still inherently a Critical-package patch.

### 6.1 Package characteristics that confer inherent risk

- **Files owned** — does the package own clinical-core files (#2 PATIENT, #44 HOSPITAL LOCATION, #50 DRUG)?
- **DBIA participation** — how many consumer packages depend on this package via DBIA?
- **Ambient API exposure** — does the package provide APIs that every other package calls?
- **HL7 traffic** — does the package send/receive HL7 messages?
- **External-system contracts** — does the package have institutional interfaces (FSC, HCCH, eRx, PBM)?
- **Patient identity dependence** — does the package read/write `^DPT` (PATIENT)?
- **Infrastructure layer** — is the package in the Kernel / FileMan / Toolkit / HL7 / RPC Broker layer?

### 6.2 P-strata and 128-package classification

Of the 128 pure-VistA packages (per the §13 filter):

#### P4 — Critical infrastructure (~8 packages)

Patches to these are always at minimum L3, often L4. Touching them affects every other package on the system.

| Pkg | Why Critical |
|---|---|
| **XU** (Kernel) | Owns DUZ, security keys, options, patch governance itself |
| **DI** (FileMan) | Schema layer — every package depends on FileMan |
| **XM** (MailMan) | Async messaging substrate; backup MailMan messages depend on it |
| **HL** / **HL7** | HL7 engine; every async cross-package message flows through |
| **XT** (Kernel Toolkit) | Checksums, integrity tools, build verification |
| **XWB** (RPC Broker) | Sync client transport; CPRS depends on it |
| **VALM** (List Manager) | UI substrate for list-based interactions |
| **MPIF** (Master Patient Index) | Patient identity reconciliation |

#### P3 — High-risk clinical / financial packages (~25 packages)

Inherent risk from cross-package DBIAs, HL7 traffic, or financial-clearinghouse interfaces. Patches here are typically L2–L3, occasionally L4.

| Pkg | Why High |
|---|---|
| **ADT / DG** (Admission Discharge Transfer) | Owns #2 PATIENT registration logic |
| **OR** (Order Entry / CPRS) | Owns ordering pathway; CPRS GUI dependency |
| **PX** (Patient Care Encounter) | Encounter recording for billing and clinical reporting |
| **LR** (Laboratory) | Owns lab results files; HL7 ingest from instruments |
| **RA** (Radiology) | Imaging order/result; cross-system DICOM/MAG |
| **PSO** (Outpatient Pharmacy) | Owns prescription dispensing logic; eRx external |
| **PSJ** (Inpatient Medications) | Inpatient medication administration |
| **PSB** (BCMA) | Bedside medication safety; HL7 RAS^O17 outbound |
| **PSD** (Controlled Substances) | DEA-regulated; ePCS external |
| **PSN** (NDF) | National Drug File; reference data dependency |
| **PSS** (Pharmacy Data Mgmt) | Cross-pharmacy data dictionary |
| **TIU** (Text Integration) | Clinical document storage |
| **GMRC** (Consults) | Cross-package consult tracking |
| **GMRA** (Adverse Reaction) | Allergy / adverse reaction tracking |
| **GMRV** (Vitals) | Vitals/measurements |
| **PXRM** (Clinical Reminders) | Cross-package reminder evaluation |
| **MAG** (Imaging) | DICOM, VIX viewer; cross-organizational |
| **MD** (Clinical Procedures) | Procedure flow sheets |
| **YS** (Mental Health) | Sensitive clinical assessments |
| **NUR** (Nursing) | Nursing workflow |
| **SR** (Surgery) | Surgical case logic |
| **IB** (Integrated Billing) | FSC / HCCH external |
| **PRCA** (Accounts Receivable) | Financial billing |
| **ECME** (eClaims Mgmt Engine) | eRx / PBM external |
| **SD** (Scheduling) | Cross-package appointment logic |

#### P2 — Moderate-risk clinical packages (~50 packages)

Inherent risk from clinical workflow involvement, but with bounded scope and limited cross-package surface. Patches typically L1–L2.

Examples: HBPC (Home Based Primary Care), AMT (Anticoagulation), FH (Nutrition), MMRS (MRSA), MC (Medicine), DGBT (Beneficiary Travel), DGJ (Incomplete Records), most Quality Management packages (QAC, QAM, QAN, QAO, QMIM), most Engineering and administrative modules.

#### P1 — Low inherent risk packages (~45 packages)

Self-contained registries, reporting, and extract-only packages. Patches almost always L1.

| Category | Examples |
|---|---|
| Registries | ROEB (Breast Cancer), ROEG (MS Surveillance), ROEV (Eye/Vision Injury), ROES (Remote Order Entry), ROR (Clinical Case), NCR (Clozapine), ONC (Oncology), TBI (Traumatic Brain Injury), EFR (Embedded Fragments) |
| Reports / extracts | ECX (DSS Extracts), ACR (Ambulatory Care Reporting), QAP (Survey Generator), KMPS (SAGG Statistical Analysis), KMPR (Resource Usage Monitor), KMPV (System Monitor) |
| Self-contained tools | E3R (Error/Enhancement Reporting), VAQ (Patient Data Exchange), VPR (Virtual Patient Record), CRHD (Shift Handoff Tool) |
| Reference / lookup | LEX (Lexicon Utility), IFR (Institution File Redesign), HL (Standard Files) |

### 6.3 Combined risk = max(L, P)

The patch's effective risk for governance, testing, and pre-flight purposes:

| Effective risk | Patch L-stratum × Package P-stratum |
|---|---|
| **Critical** | L4 OR P4 (any package, any patch — Kernel/FileMan/MPIF always treated as Critical) |
| **High** | L3 (any non-Critical package) OR P3 with L≥L2 |
| **Moderate** | L2 (any package P1–P3) OR P2/P3 with any patch |
| **Low** | L1 + P1 only — must be a low-risk patch on a low-risk package |

The asymmetry is deliberate: a low-risk-looking patch on a high-risk package does not earn the package a discount. The package's structural exposure dominates.

---

## 7. Application use cases

### 7.1 Pre-flight blocker severity (informs `vista-package-state-audit-plan.md` §4)

The blocker taxonomy in the pre-flight audit plan classifies blockers by severity (`error` / `warn` / `info`). The patch's L-stratum (and the package's P-stratum) modulates that severity:

- **L4 / P4 patches:** any `warn` is escalated to `error`. The bar for clean install is highest.
- **L3 / P3 patches:** standard severity application.
- **L2 / P2 patches:** standard severity application.
- **L1 / P1 patches:** `warn`-level B4 (drift) blockers may be accepted with documentation; expedited review acceptable.

This makes the heuristic operational in the pre-flight engine: high-stratum patches get more conservative blocker handling.

### 7.2 DIBRG governance level

The depth and rigor of DIBRG production should track risk:

| Stratum | DIBRG production rigor |
|---|---|
| Effective Critical | Full §3 template; Artifact Rationale; Acronyms appendix; explicit irreversibility section; mandatory peer review by another package's developer; OIT-level governance signoff |
| Effective High | Full §3 template; Artifact Rationale; Troubleshooting appendix; cross-package DBIA review; peer review |
| Effective Moderate | Full §3 template; standard appendices; standard peer review |
| Effective Low | §3 template may collapse §5+§6 (Back-Out Procedure / Rollback Procedure) per §3.1.2 (BMS variant) — acceptable for additive-only patches |

This formalizes existing practice: ADT DIBRGs are dense and detailed; ANRV DIBRGs are slim. The heuristic makes the variation principled rather than ad-hoc.

### 7.3 Backout planning

| Stratum | Backout plan must include |
|---|---|
| Effective Critical | Detailed forward-fix-only plan; explicit list of irreversible operations (§14.6.3 of the lifecycle spec); OIT escalation path; patient-care impact assessment |
| Effective High | Forward-fix preferred; routine backup verification; cross-package consumer notification |
| Effective Moderate | KIDS-standard back-out (routine restore); manual DD reversal procedure if applicable |
| Effective Low | KIDS-standard back-out only; component removal sufficient |

### 7.4 Test depth

| Stratum | Test requirements |
|---|---|
| Effective Critical | Mirror site testing (multiple sites); regression suite across all consumer packages; HL7 partner system testing; load testing |
| Effective High | Mirror site testing (at least one site); regression suite for consumer packages |
| Effective Moderate | Test-account testing; targeted regression |
| Effective Low | Developer-account testing sufficient; minimal regression |

### 7.5 NPM verifier review

| Stratum | NPM verifier path |
|---|---|
| Effective Critical | Senior verifier; multi-stakeholder review; explicit acknowledgment of irreversibility |
| Effective High | Standard verifier with peer second-review |
| Effective Moderate | Standard verifier |
| Effective Low | Expedited verifier |

This maps the heuristic onto the NPM operational summary's three-role workflow (Developer → Verifier → IRM/Support). The verifier role's depth scales with risk.

---

## 8. Caveats and limitations

### 8.1 The empirical sample is partial

Only 32 of an estimated 988 active DIBRGs were available in the markdown corpus at scan time. The sample may overrepresent recent OIT-template DIBRGs and underrepresent older or simpler patches. A complete recalibration should be done when the markdown corpus expands (or when the CSV → markdown linking proposed in `vdl-search-assessment.md` makes sampling easier).

### 8.2 Indicator scanning is text-based, not semantic

Phrase-pattern matching catches presence of risk language but not absence of risk that the developer simply didn't mention. A DIBRG that omits the Back-Out Risks section gets a low score by default; a DIBRG that thoroughly enumerates risks gets a high score even if the patch is actually safe. Manual review is essential at the Moderate-and-above level.

### 8.3 The L-strata and P-strata are not independent

A high-risk patch (L4) is more likely on a high-risk package (P4) — Kernel patches are typically larger and more invasive than registry patches. Treating L and P as independent and combining via max is conservative but loses some signal. A future refinement could use a 2D risk matrix instead of a max.

### 8.4 Heuristic, not policy

This document specifies a heuristic — a structured way to think about risk. It is not a binding policy. Patches that score Low may still warrant Critical-grade review when site-specific context warrants. Patches that score Critical may proceed with reduced rigor when site-specific governance permits. The heuristic is decision support, not decision authority.

### 8.5 No incident-rate validation

The heuristic was constructed from documents (paper risk), not from realized failure data (incident rate, back-out rate, NPM "Entered in Error" frequency). A future calibration should compare predicted strata against realized incidents from NPM history, with the heuristic adjusted to fit observed risk.

---

## 9. Open questions

- [ ] **Calibration against realized incidents.** Pull NPM "Entered in Error" history for the past five years; compute back-out rate per package per year; correlate with the heuristic's package-level strata. Adjust strata boundaries to fit observation.
- [ ] **DIBRG sampling expansion.** When the markdown corpus expands beyond the current 32 DIBRGs (or when CSV → markdown linking makes sampling cheap), re-run the §3 indicator scan against a stratified sample of older DIBRGs to test whether the heuristic generalizes.
- [ ] **Per-DIBRG rubric integration.** Should DIBRG authors be asked to fill in a structured §5.1 dimension rubric as part of DIBRG production, alongside the existing Constraints and Back-Out Risks sections? This would shift risk assessment from post-hoc text scanning to author-stated declaration.
- [ ] **P-stratum boundaries for borderline packages.** Some packages are arguably P2 or P3 depending on site-specific use (e.g. SR Surgery is P3 at surgical sites, P2 at non-surgical sites). Should P-strata be site-specific?
- [ ] **Cross-flavor calibration.** This heuristic was developed from VA-OIT DIBRGs. WorldVistA / vxVistA / OSEHRA may have different package risk profiles (e.g. fewer external-system entanglements). A flavor-aware heuristic may be warranted.
- [ ] **GUI / Web tier coverage.** This heuristic addresses pure-VistA M packages only (per the §13 filter). A parallel heuristic for VistA-GUI hybrids (CPRS, BCMA, MAG VIX, EDIS) should be developed if those become in-scope.

---

## 10. Worked package roster — quick reference

For ease of reference, the 128 pure-VistA packages collapsed into the four P-strata (approximate counts; some borderline cases noted):

| P-stratum | Count | Examples (not exhaustive) |
|---|---|---|
| **P4 — Critical** | ~8 | XU, DI, XM, HL/HL7, XT, XWB, VALM, MPIF |
| **P3 — High** | ~25 | ADT/DG, OR, PX, LR, RA, PSO, PSJ, PSB, PSD, PSN, PSS, TIU, GMRC, GMRA, GMRV, PXRM, MAG, MD, YS, NUR, SR, IB, PRCA, ECME, SD |
| **P2 — Moderate** | ~50 | HBPC, AMT, FH, MMRS, MC, DGBT, DGJ, QAC, QAM, QAN, QAO, QMIM, EN, ES, FB, GEN, IBD, IVMB, LBR, OOPS, PRC, PRCN, PRPF, PRS, RT, VSS, WII, NUPA, FIM, ASCD, GMPL, GMTS, ASU, CCRA, EHM, EPI, EPSI, ETS, ICR, PCMM, ROES, RMDS, SOW, SPN, SRA, VBECS, WV, …  |
| **P1 — Low** | ~45 | ROEB, ROEG, ROEV, ROR, NCR, ONC, TBI, EFR, ACKQ, AMT, AR/WS, CRHD, ECX, ACR, QAP, KMPD, KMPR, KMPS, KMPV, RUM, SAGG, NOIS, E3R, VAQ, VPR, LEX, IFR, FFP, HDI, HL (data files only), MJCF, ORRC, PAIT, POC, PPP, PREA, PSU, PSX, ROES, SQLI, MXML, XOB, XQOR, ZSLOT, … |

Note that the P-classification is necessarily approximate; some packages lie at boundaries. The intent is governance support, not pixel-precise classification.

---

## 11. References

### 11.1 Empirical source (DIBRGs scanned)
- All 32 DIBRGs in the `vistadocs/vdl` markdown corpus as of analysis date (see `vdl-query-patterns.md` §6 Recipe A for re-discovery)

### 11.2 Methodological sources
- `vista-package-lifecycle-spec-v7.md` — particularly §3 (DIBRG template), §3.1 (variants), §13 (population scope)
- `vista-package-state-audit-plan.md` — §4 (eight-class blocker taxonomy that this heuristic informs)
- `vdl-query-patterns.md` — §3.3 (doc_code taxonomy), §6 (query recipes used to enumerate DIBRGs)

### 11.3 Companion artifacts
- `vista_packages_summary.csv` — 128-package coverage flags (used as input to §6 P-classification)
- `vdl_inventory_vista_only.csv` — pre-filtered pure-VistA inventory

### 11.4 Future calibration sources
- NPM "Entered in Error" patch history (FORUM IRM/Support reports) — for §8.5 incident-rate validation
- VA OIT change-management records — for cross-validation of P-strata boundaries
