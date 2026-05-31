# VDL Inventory Label Gaps — Residual Cases for Human Review

**Generated:** 2026-03-29
**Source:** `vdl_inventory_enriched.csv` (post all four strategy steps)
**Scope:** 154 unique documents with no `doc_code` / `doc_label` after automated processing

---

## Executive Summary

After implementing all four strategy steps (title-pattern expansion, filename-suffix
classification, peer-group inference, and noise tagging), **154 unique documents** remain
unlabelled. These represent ~1.7% of the 8,834-row inventory and cover 306 total rows
(multiple version rows can share the same source document).

| Category | Count | Description |
|----------|------:|-------------|
| **A** — Patch-prefix descriptive | 42 | Patch-layer docs whose titles carry no standard doc-type keyword |
| **B** — Numbered series | 0 | Fully resolved by `^\d{3}:` → SUP pattern in Step 1 |
| **C** — Plain/anchor specialist docs | 57 | Anchor or plain-layer VistA-native docs with idiosyncratic titles |
| **D** — Peripheral / non-VistA apps | 55 | Apps outside the core VistA namespace with non-standard naming |
| **Total** | **154** | |

Many of these can be resolved by reading the document or applying one targeted pattern per
cluster. Quick wins (≤5 patterns to add) are noted under each category.

---

## Category A — Patch-Prefix Descriptive (42 docs)

**Why unlabelled:** These are patch-layer documents. Their titles begin with a patch prefix
(`NS*V*P …`) but the remainder is a description, project name, or topic — no standard
doc-type keyword appears anywhere the classifier can match.

**Adjudication approach:**
1. Read the document (or infer from filename/title) and assign the most appropriate code.
2. If the same title pattern recurs across many patches, add a targeted rule to
   `DOC_TYPE_PATTERNS` in `enrich_inventory.py`.
3. For truly one-off documents, assign manually via a `MANUAL_OVERRIDES` dict keyed by
   `doc_slug`.

**Quick-win patterns that would resolve multiple rows here:**

| Pattern to add | Target code | Would resolve |
|----------------|------------|---------------|
| `\bWorkflow\b` | WF | DVBA workflow docs (but already in Cat D) |
| `\bDIBRO\b` | DIBR | VIAB*1*14 |
| `\bQR\s+Guide\b` | QRG | XU*8*702 |
| `\bSupplement\s+to\s+Patch\b` | SUP | XT*7.3*98, XU*8*283, XU*8*608 |
| `\bReadme\b` | RN | FMDC*1.0*2, XU*8*207 |
| `\bRemediation\b` | SUP | MMRS*1*4 |
| `\bData\s+Definitions?\s+Document\b` | SUP | ECX*3*178 |
| `\bImplementation\s+Plan\b` | IG | LEDI, MPIF*1*63 |
| `\bCore\s+Dataset\b` | SUP | XU*8*512 |

---

| App | Patch ID | Filename | Title | Suggested Code | Notes |
|-----|----------|----------|-------|---------------|-------|
| ASU | USR*1*33 | usr_1_33rn.docx | USR*1*33 Show User Class Name in ASU Options | RN | Filename ends in `rn`; title says "show user class name" — patch option doc, likely release note |
| DRG | ICD*18.0*57 | icd_18_57_disk_req.docx | ICD*18.0*57/LEX*2.0*80 ICD Disk Requirements | SUP | Disk requirements specification; supplement to DIBR |
| DVBA | DVBA*2.7*237 | 508_workflow_v3.docx | DVBA*2.7*237 Workflow — DBQ Transmission Errors | WF | Workflow document (compare Cat D CAPRI workflow series) |
| ECX | ECX*3*178 | ecx_3_178_ddd.docx | ECX*3*178 DSS FY21 Data Definitions Document | SUP | Data definitions document; supplement/reference |
| ES | ES*1*46 | es_1_p46_retire.docx | ES*1*46 Retirement of VistA Police and Security Data Entry/Edit Option | SUP | Retirement notice / patch supplement |
| FMDC | FMDC*1.0*2 | FMDC1_0P2RM.docx | FMDC Patch FMDC*1.0*2 README file (includes Delphi 5 instructions) | RN | Explicit "README file" in title |
| GMRC | GMRC*3*57 | cons3_p57_rn.docx | GMRC*3*57 Suicide Hotline Consult Setup | IG | Setup document; filename `_rn` is a mislabel — content is a setup/install guide |
| IVMB | IVMB*2*395 | ivmb_2_p395_hec.docx | IVMB*2*395 Means Test Sharing (MTS) Manual | UM | "Manual" in title; describes user-facing MTS process |
| IVMB | IVMB*2*865 | ivmb_2_p865_rn.docx | IVMB*2*865 Operation Enduring Freedom Operation IRAQI Freedom Phase II | RN | Filename suffix `_rn`; OEF/OIF phase release note |
| LEDI | LA*5.2*64 | ldsi_implementation_plan_v1.10.docx | LA*5.2*64/LR*5.2*286 LDSI National Implementation Plan V.1.10 | IG | "Implementation Plan" — install-class document |
| LR | LA*5.2*68 | la_5_2hl7spec_68.docx | LA*5.2*68 Laboratory HL7 Specification | BASE_HL7 | HL7 interface specification |
| LR | LR*5.2*468 | la_1_ig.docx | LR*5.2*468 Laboratory NDS Installation Back out Plan | DIBR | "Installation Back out Plan" = DIBR component; filename `_ig` |
| MD | MD*1*72 | md1_0p72term.docx | MD*1*72 CliO Terminology Dictionary & Clinical Data Model Revised | SUP | Dictionary/data model reference |
| MHV | MHV*1*24 | emergency_patch_mhv_backup_n_rollback_plan.docx | MHV*1*24 Emergency Patch Instructions | DIBR | "backup … rollback plan" in filename |
| MMRS | MMRS*1*4 | vle_micro_mmrs_1_0_4_remediation_guide.docx | MMRS*1*4 Remediation Guide | SUP | Remediation guide; supplement |
| MON | *(none)* | vista_monograph_0723_r.docx | Vista Monograph July 2023 | SUP | Monograph = informational/overview supplement |
| MPIF | MPIF*1*63 | mpif_1_63_ig.docx | MPI MPIF*1*63 Installation, Back-Out, and Rollback Guide | DIBR | "Installation, Back-Out, and Rollback" in title; filename `_ig` |
| PECS | PREC*6*516 | prec_6_0_tg_r0516.docx | PREC*6*516 TROUBLE SHOOTING GUIDE | SUP | Troubleshooting guide; filename `_tg` = Training Guide by corpus, but content is troubleshooting |
| PECS | PREC*6.1*717 | prec_6_1_tg_r0717.docx | PREC*6.1*717 TROUBLE SHOOTING GUIDE | SUP | Same as above (series sibling) |
| PSB | PSB*3*47 | psb_3_p47_pss_1_p141_ig.docx | PSB*3*47/PSS*1*141 BCMA Version 3 Immunizations Documentation | IG | Filename `_ig`; immunizations installation documentation |
| PSB | PSB*3*84 | psb_3_p84_bcbu_sg.docx | PSB*3*84 BCBU Version 3 Securing the Cache Cube for BCMA Backup | SG | "Securing … Backup" — security guide; filename `_sg` |
| PSO | PSO*7*522 | pso_7_p522_opai_dibrg.docx | PSO*7*522 Health Connect/Outpatient Pharmacy Automated Interface (OPAI) | DIBR | Filename `_dibrg` |
| PSS | PSS*1*127 | pss_1_p127_drug_exceptions_list.docx | PSS*1*127 Pharmacy Data Management Drug Exception List | SUP | Reference list; supplement |
| PXRM | PXRM*2*54 | pxrm_2_0_54_cds.docx | PXRM*2*54 Using The Ebola Risk Triage Tool Template | UM | "Using The … Tool" — user/operational guide |
| PXRM | PXRM*2*74 | pxrm_va_covid_19_cprs_status_version_5_ig.docx | PXRM*2*74 COVID-19 CPRS Status Version 5 | IG | Filename ends `_ig` |
| RMPR | RMPR*3*61 | lessons_learned.docx | RMPR*3*61 Prosthetics Inventory Package (PIP) Lessons Learned | SUP | Lessons learned = supplement/internal review doc |
| SD | DG*5.3*887 | dg_5_3_887_implement_guide.docx | DG*5.3*887 Meaningful Use New VistA Data Elements (MUNVDE) Preferred List | IG | Filename `_implement_guide`; implementation guide |
| SQLI | DI*21*38 | sqli_sm.docx | DI*21*38 Site Manual | SM | "Site Manual" in title; filename `_sm` |
| SQLI | DI*21*38 | sqli_vendor.docx | DI*21*38 Vendor Guide DRAFT | UG | Vendor guide → USER_MANUAL class |
| SR | SR*3*164 | sr_3_p164_rn.docx | SR*3*164 Surgery CICSP - CT Surgery Consult Date 2007 Release | RN | Filename `_rn`; "Release" in title |
| TIU | TIU*1*254 | tiu_1_357_util.docx | TIU*1*254 Additional Signer Utility Guide | UG | "Utility Guide" → User Guide |
| VIAB | VIAB*1*14 | viab_1_14_installation_back-out_rollback_plan_release_notes.docx | VIAB*1*14 DIBRO | DIBR | Title is literally "DIBRO"; filename contains "installation_back-out_rollback" |
| XM | XM*8*25 | tcpip_service_for_mailman.docx | XM*8*25 TCP/IP Service for Mailman | TM | Technical specification for TCP/IP service; technical manual |
| XOBW | XOBW*1*4 | xobw_1_0_p4_ig.docx | XOBW*1*4 Installation, Back-Out, and Rollback Guide | DIBR | "Installation, Back-Out, and Rollback" in title; filename `_ig` |
| XT | XT*7.3*98 | xt7_3p98sp.docx | XT*7.3*98 VistA Patch Monitor, Supplement to Patch Desc | SUP | "Supplement to Patch" — filename `_sp` |
| XU | XU*8*105 | state_patch_follow_up_xu_8_105.docx | XU*8*105 VistA State Patch Follow-Up | SUP | Patch follow-up document; supplement |
| XU | XU*8*207 | kdc1_0rm.docx | XU*8*207 KDC Readme | RN | Filename `_rm` (readme); "Readme" in title |
| XU | XU*8*283 | krn8_0p283sp.docx | XU*8*283/288 DEA/VA Public Key Infrastructure (PKI) Pilot Project Supplement | SUP | "Supplement" in title; filename `_sp` |
| XU | XU*8*512 | xu8_0p512sp.docx | XU*8*512 Trainee Registration Core Dataset | SUP | Dataset reference doc; filename `_sp` |
| XU | XU*8*608 | xu_8_0_608_sp.docx | XU*8*608/607/672 Lock Manager Supplement to Patch | SUP | "Supplement to Patch" in title; filename `_sp` |
| XU | XU*8*702 | xu_8_0_702_qr.docx | XU*8*702 Quick Reference (QR) Guide | QRG | "Quick Reference (QR) Guide" in title; filename `_qr` |
| XU | XU*999*3 | vista_state_patch_xu_999_3.docx | XU*999*3 VISTA STATE file (5) Information Patch | SUP | Informational patch note; data-file reference supplement |

---

## Category B — Numbered Series (0 docs)

All LR numbered-procedure documents (`001: …`, `002: …`, etc.) were resolved in Step 1
by the pattern `^\d{3}:` → SUP. **No remaining Category B cases.**

---

## Category C — Plain/Anchor Specialist Docs (57 docs)

**Why unlabelled:** These are anchor-layer (versioned, non-patch) or plain (no version, no
patch) documents from VistA-native packages. Their titles use non-standard terminology
that does not match any current pattern — project-specific names, memo-style headings,
or highly abbreviated labels.

**Adjudication approach:**
1. For series (e.g., the 13 SD VSE User Guide Addenda), apply one pattern or one
   `MANUAL_OVERRIDES` block to resolve the whole group.
2. For singleton oddities (test docs, archive placeholders), use noise_type tagging
   rather than force-fitting a doc_code.
3. For tutorials and quick-start content (DI, FMDC, XM), add targeted patterns or
   overrides.

**Quick-win clusters:**

| Cluster | Count | Resolution |
|---------|------:|-----------|
| SD VSE GUI `User_Guide_Addendum` series | 13 | Add `\bAddendum\b` → UG or override by filename pattern `_addendum` |
| DI FM tutorials | 4 | Add `\bTutorial\b` → TRG (already in QRG list; reconsider mapping) |
| NOIS training docs (Cat D) | — | See Cat D |
| RA ADPAC/HL7 supplements | 2 | `ADPAC Supplement` → UG; `HL7 Setup` → BASE_HL7 |
| LA Universal Interface install docs | 3 | "Installation … Guide" — should already match; check title encoding |

---

| App | Layer | Filename | Title | Suggested Code | Notes |
|-----|-------|----------|-------|---------------|-------|
| ACKQ | anchor | ackq3_0p13_tm.docx | QUASAR Version 3 Technical/Pkg Security (Updated ACKQ*3*13) | TM | "Technical" in title and filename `_tm`; security TM hybrid |
| BMS | anchor | bms_5_0_ag.docx | Bed Management Solution Version 5.0 Admin Guide | AG | "Admin Guide" in title; filename `_ag` |
| DI | anchor | fm22_2ig.docx | FM 22.2 Installation, Back-Out, and Rollback Guide | DIBR | "Installation, Back-Out, and Rollback" in title; filename `_ig` |
| DI | plain | fm22_tutorial.docx | FM Key and Index Tutorial | TRG | "Tutorial" in title |
| DI | plain | scrn_tut.docx | FM ScreenMan Tutorial for Developers | TRG | "Tutorial" in title |
| DI | plain | fm22_krn8_file_security.docx | FM and Kernel File Access Security | SG | Security-focused reference doc |
| DI | plain | dde_tutorial.docx | VA FileMan DDE Utility Tutorial | TRG | "Tutorial" in title |
| ECX | anchor | ecx_3_ddd.docx | Decision Support System Version 3.0 Data Definitions Document | SUP | Data definitions; reference supplement |
| EN | anchor | rtls_ese_interfaces_technical_manual.docx | EN Version 7 RTLS Enhancement Interfaces Manual | TM | "Interfaces … Manual" → Technical Manual; filename has `_technical_manual` |
| FB | plain | FB_PM.docx | Fee Basis Annual Patch Manual | SUP | Filename `_PM` (Production Operations Manual by corpus rule, but content is annual patch manual); ambiguous — read doc |
| FMDC | plain | fmdc1_0gs.docx | FMDC Getting Started Guide | QRG | "Getting Started" → Quick Ref |
| HMP | plain | eHMP_ICR_Status_MFR_20180312.docx | eHMP Integration Control Registrations (ICRs) Status: Memorandum for Record | SUP | Memo for Record / status update — supplement |
| IBD | plain | aics3_0modifcations.docx | AICS Modification for Code Set Versioning | SUP | Modification notice / supplemental doc |
| ICR | anchor | imr_read-me.doc | Note regarding the decommissioning of ICR 2.1 | SUP | Decommission notice; informational supplement |
| LA | anchor | labautorelease1_0installationguidewarranty.docx | Laboratory: Universal Interface AutoRelease Version 1 Installation Back-out Guide Warranty | DIBR | "Installation … Back-out … Guide" in title |
| LA | anchor | labautorelease_1_0_installationguide.docx | Laboratory: Universal Interface AutoRelease Version 1 Installation Back-out Guide | DIBR | "Installation Back-out Guide" in title |
| LA | anchor | lab_ui_specs_lab_micro_interface_rel_1_0.docx | Laboratory: Universal Interface Micro Interface Version 1 Lab UI HL7 Specifications | BASE_HL7 | "HL7 Specifications" in title |
| LR | anchor | vista_blood_bank_v5_2_package_status_july_18_2011.docx | Laboratory: Blood Bank v5.2 Package Status July 18 2011 | SUP | Package status memo; supplement |
| LR | plain | nlt_wkld_code_request_form.docx | Laboratory NLT Workload Code Request Form | SUP | Request form — adjunct/supplement doc |
| MPI | anchor | mpi_psim_implementation_plan_v1.docx | MPI/PSIM Implementation Plan V1 | IG | "Implementation Plan" → Installation Guide class |
| NPM | plain | pmuser.docx | NPM Operational Summary | POM | Operational summary → Production Operations Manual |
| NPM | plain | patch_module_enhancements.docx | NPM Patch Module Enhancements | SUP | Enhancement notes; supplement |
| PCMM | plain | pcmmugappx.docx | Primary Care Management Module (PCMM) Mass Discharge Scenarios | SUP | Scenarios document; supplement/appendix |
| PPP | plain | ppp_1_message.docx | Retiring Pharmacy Prescription Practices Message | SUP | Retirement notice — supplement |
| PRC | anchor | ifcp5_1pou_manual.docx | IFCAP Version 5.1 Point of Use Manual | UM | "Point of Use Manual" — user manual; filename `_pou_manual` |
| PRCA | plain | archive_placeholder.docx | AR Archive demo | NOISE | Test/placeholder document — tag as noise |
| PXRM | plain | ahobpr_clinicalportal_manual_v2.pdf | AHOBP Clinical Portal Manual | UM | "Clinical Portal Manual" — user manual |
| QAC | anchor | pats_1_1_datamigrationguide.docx | PATS Data Migration Guide | IG | "Data Migration Guide" pattern added in Step 1 — investigate why still unlabelled |
| QAC | plain | pats_notificationsfornonadvocates.docx | PATS Notification Presentation for NonAdvocates | SUP | Presentation/handout — supplement |
| RA | anchor | ra_5_aa_s_1.docx | Radiology Version 5 ADPAC Supplement | SUP | "ADPAC Supplement" — supplemental ADPAC material |
| RA | anchor | ra5_0hl7.docx | Radiology Version 5 HL7 Setup Manual | BASE_HL7 | "HL7 Setup Manual" — HL7 interface spec |
| RMDS | plain | rai-mds_electronic_transmission_training_manual.docx | RAI/MDS Electronic Transmission Manual | TRG | "Training Manual" suffix implied by filename `_training_manual` |
| SD | anchor | vs_gui_1_7_0_2_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.0.2 User_Guide_Addendum | UG | Series: "User Guide Addendum" = supplement to main UG; assign UG |
| SD | anchor | vs_gui_1_7_1_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.1_User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_10_1_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.10.1 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_11_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.11 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_12_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.12 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_14_1_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.14.1 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_15_0_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.15.0 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_16_2_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.16.2 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_17_2_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.17.2 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_20_1_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.20.1 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_21_0_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.21.0 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_22_0_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.22.0 User_Guide_Addendum | UG | (series sibling) |
| SD | anchor | vs_gui_1_7_23_0_user_guide_addendum.docx | VistA Scheduling Enhancement (VSE) GUI 1.7.23.0 User_Guide_Addendum | UG | (series sibling) |
| SD | plain | Test_document_VDL.docx | Test Document VDL | NOISE | Explicit test document — tag as noise |
| SPN | anchor | spn_2_conversion_information.docx | SPN Version 2 Conversion Notes | SUP | Conversion notes; adjunct supplement |
| STS | anchor | sts_vets_10_setup_guide.docx | STS Version 2 VETS 10 Set Up Guide | IG | "Set Up Guide" — installation/config guide; BASE_SETUP |
| TIU | anchor | tiu_util.docx | Additional Signer Utility Guide (TIU*1.0*357) | UG | "Utility Guide" → User Guide |
| VDEF | plain | vistamessagingoverview_vdef_100105.docx | VDEF VistA Messaging Overview 100105 | TM | Technical overview — Technical Manual class |
| VSS | plain | ese_vss_kiosk_baseline_resource_document.docx | ESE VSS Kiosk Baseline Resource Document | SUP | Baseline resource document; supplement |
| XM | anchor | xm_8_0_getstartguide.docx | MailMan Version 8 Getting Started Guide | QRG | "Getting Started Guide" → Quick Ref |
| XT | plain | README.docx | Kernel Toolkit ReadMe File: Toolkit documentation to be absorbed by Kernel | RN | "ReadMe File" in title |
| XU | anchor | krn_8_0_dg_binder.pdf | Kernel 8.0 Developer's Guide: Binder | DG | "Developer's Guide" — filename `_dg_binder`; encoding issue hides apostrophe |
| XU | anchor | krn8_0st.docx | Kernel 8.0 Security Tools Manual | SG | "Security Tools Manual" — security guide |
| XU | plain | xtmp_rules.docx | Kernel XTMP Global Description Rules of Use | SUP | Rules of use; supplement/reference |
| ZSLOT | plain | zslot_mg.docx | Slotmaster Management Guide | SM | "Management Guide" → Site Manual / SM; filename `_mg` |

**Note on QAC PATS Data Migration Guide:** The title should have matched the `data\s+migration`
→ INSTALLATION_GUIDE pattern added in Step 1. Investigate whether the title in the CSV
has unexpected whitespace or encoding; the fix may be a title normalization step rather
than a new pattern.

---

## Category D — Peripheral / Non-VistA Apps (55 docs)

**Why unlabelled:** These applications sit outside the core VistA namespace. Their document
naming conventions differ from the VDL standard (some use Java/web-app conventions, some
use plain English release-note style, some are VA benefit-system docs). The classifier
was not designed for them (Axiom 7 in `classify/rules.py`).

**Adjudication approach:**
1. Apply app-specific bulk rules. For example, NOIS training series → TRG; VBECS Known
   Defects series → SUP; CAPRI Workflow series → WF.
2. Add app-specific overrides to `_APP_SPECIFIC_SUFFIX` in `enrich_inventory.py`, or
   create a per-app prefix rule: `(app_abbrev, title_prefix) → (doc_code, doc_label)`.
3. For TMP, treat each document individually — the naming is inconsistent enough that
   bulk rules do not apply cleanly.

**App-level bulk assignments:**

| App | Count | Bulk assignment | Rationale |
|-----|------:|-----------------|-----------|
| CAPRI (DVBA*2.7* workflows) | 11 | WF | All titled "Workflow — [condition]"; Compensation & Pension DBQ workflows |
| CAPRI (other) | 1 | IG | `capri_gui_isg.docx` — "Installation Supplemental Guide" |
| EDIS | 2 | SUP | Both are titled "Glossary" — Supplement |
| HL7 | 4 | SUP | All titled "… Supplement" |
| KAAJEE | 2 | DIBR | Both are rollback instruction docs |
| KAAJEE | 1 | RN | `kaajee_1_0_1_readme.docx` — "ReadMe File" |
| KAAJEE | 1 | IG | `KAAJEE_CLASSIC_8_DEPG.doc` — "Classic Deploy Guide" |
| MAG | 2 | QRG | VistARAD Shortcut List; VistARad Quick Start Guide |
| MAG | 1 | AG | VIX Admin Guide |
| MAG | 1 | SUP | VistA Imaging Error Message Guide |
| MAG | 1 | SUP | VistA Imaging System TeleReader Configuration (FileMan) |
| MAG | 1 | TM | Profiles for HL7 Messages from VistA to Commercial PACS (HL7 spec) |
| NOIS | 6 | TRG | All titled "NOIS Training — [role]" |
| NOIS | 1 | RN | "NOIS Version 1.1 — Overview of New Features" |
| NOIS | 1 | TM | NOIS Technical Reference |
| NOIS | 1 | SUP | NOIS Using NOIS GUI with Forum |
| TMP | 2 | TM | "PIMS TM" in title — explicit Technical Manual label |
| TMP | 1 | DIBR | "TMP Release 5.2.4" — `TMP_5_2_4_DIBR.docx` |
| TMP | 1 | DIBR | "TMP Version 1.5 Release 4.6 DIBRO" |
| TMP | 1 | RS | "TMP Version 1.5 Release 4.6 Requirements Specifications" |
| TMP | 1 | RS | "TMP Version 2.0 Release 4.8 Requirements" |
| TMP | 1 | RN | "TMP VistA Patch 879" — `sd_5_3_879_dibrg.docx` — release note |
| VBECS | 7 | SUP | All "VBECS Version X.Y.Z Known Defects and Anomalies" — defect log supplement |
| VBECS | 1 | SUP | "VBECS Product Information Pamphlet" — informational supplement |
| XWB | 1 | TM | XWB*1.1*35 and XWB*1.1*44 TCP/IP Supplement (`_um` filename oddity — content is technical) |
| XWB | 2 | RN | XWB*1.1*72 and XWB*1.1*73 Readme Files |

---

**Full Category D row listing:**

| App | Layer | Filename | Title | Suggested Code | Notes |
|-----|-------|----------|-------|---------------|-------|
| CAPRI | patch | dvba_27_p150_audio_wf.docx | DVBA*2.7*150 Workflow - Audio | WF | Workflow document |
| CAPRI | patch | dvba_27_p151_a_and_a_wf.docx | DVBA*2.7*151 Workflow - Aid and Attendance | WF | Workflow document |
| CAPRI | patch | dvba_27_p151_tbi_wf.docx | DVBA*2.7*151 Workflow - Traumatic Brain Injury (TBI) | WF | Workflow document |
| CAPRI | patch | dvba_27_p159_dbq_parkinsons_wf.docx | DVBA*2.7*159 Workflow - Parkinson's Disease | WF | Workflow document |
| CAPRI | patch | dvba_27_p161_dbq_eatingdisorders_wf.docx | DVBA*2.7*161 Workflow - DBQ Eating Disorders | WF | Workflow document |
| CAPRI | patch | dvba_27_p161_dbq_ihd_wf.docx | DVBA*2.7*161 Workflow - DBQ Ischemic Heart Disease | WF | Workflow document |
| CAPRI | patch | dvba_27_p163_dbq_malereproductive_wf.docx | DVBA*2.7*163 Workflow - Male Reproductive System Conditions | WF | Workflow document |
| CAPRI | patch | dvba_27_p163_dbq_prostatecancer_wf.docx | DVBA*2.7*163 Workflow - Prostate Cancer | WF | Workflow document |
| CAPRI | patch | dvba_27_p163_dbq_hemicandlymphatic_wf.docx | DVBA*2.7*163 Workflow-Hematologic and Lymphatic Conditions | WF | Workflow document |
| CAPRI | patch | dvba_27_p163_dbq_kidneyconditions_wf.docx | DVBA*2.7*164 Workflow - Kidney Conditions (Nephrology) | WF | Workflow document |
| CAPRI | patch | dvba_27_p159_dbq_leukemia_wf.docx | DVBA*2.7*169 Workflow - Leukemia | WF | Workflow document |
| CAPRI | plain | capri_gui_isg.docx | CAPRI GUI Installation Supplemental Guide | IG | "Installation Supplemental Guide" |
| EDIS | anchor | edis_2_2_glossary_r.docx | Emergency Department Integration Software Glossary | SUP | Glossary |
| EDIS | anchor | edis_2_1_2_glossary.docx | Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Glossary | SUP | Glossary |
| HL7 | anchor | hl71_6p109sp.docx | HL7 HL*1.6*109 Event Monitoring Supplement | SUP | Supplement |
| HL7 | anchor | hl71_6p118_sp2.docx | HL7 HL*1.6*118 Message Parsing Utilities Supplement | SUP | Supplement |
| HL7 | anchor | hl71_6p84sp.docx | HL7 HL*1.6*84 Multi-Listeners Using TCP/IP Svcs for OpenVMS | SUP | Supplement (filename `_sp`) |
| HL7 | anchor | hl71_6p93sp.docx | HL7 HL*1.6*93 MSH Segment Control (Dynamic Routing) | SUP | Supplement (filename `_sp`) |
| KAAJEE | anchor | kaajee_1_0_1_readme.docx | KAAJEE 1.0.1 ReadMe File (WebLogic 8.1) | RN | "ReadMe File" in title |
| KAAJEE | patch | KAAJEE_SSPI_XU_8_781_BCKOUT.docx | KAAJEE SSPI 8.0.781 Rollback Instructions (WebLogic 12.2) | DIBR | "Rollback Instructions"; filename `_BCKOUT` |
| KAAJEE | patch | KAAJEE_SSPI_8_748_BCKOUT.docx | KAAJEE SSPI Rollback Instructions (WebLogic 12.2) | DIBR | "Rollback Instructions"; filename `_BCKOUT` |
| KAAJEE | plain | KAAJEE_CLASSIC_8_DEPG.doc | KAAJEE Classic Deploy Guide | IG | "Deploy Guide"; filename `_DEPG` |
| MAG | plain | vista_pacs_hl7_profile_1_2.docx | Profiles for HL7 Messages from VistA to Commercial PACS | TM | HL7 message profiles — technical spec |
| MAG | plain | vix_admin_guide.docx | VIX Admin Guide | AG | "Admin Guide" |
| MAG | plain | mag_imgerrormsg.docx | VistA Imaging Error Message Guide | SUP | Error message guide — supplement |
| MAG | plain | MAG_TELEREADER_CONFIGURATION.docx | VistA Imaging System TeleReader Configuration (FileMan) | IG | Configuration guide — install/setup class |
| MAG | plain | vistarad_shortcut_list.docx | VistARAD Shortcut List | QRG | Shortcut list → Quick Ref |
| MAG | plain | VistARad_Quick_Start_Guide.docx | VistARad Quick Start Guide | QRG | "Quick Start Guide" |
| NOIS | anchor | nois_1_1_adpac.docx | NOIS Training - Application Coordinator | TRG | Training series |
| NOIS | anchor | nois_1_1_getting_started.docx | NOIS Training - Getting Started | TRG | Training series |
| NOIS | anchor | nois_1_1_irms.docx | NOIS Training - Information Resource Manager | TRG | Training series |
| NOIS | anchor | nois_1_1_manager.docx | NOIS Training - Manager / Analyst | TRG | Training series |
| NOIS | anchor | nois_1_1_dev.docx | NOIS Training - Referral Specialist | TRG | Training series (filename `_dev` is misleading) |
| NOIS | anchor | nois_1_1_support.docx | NOIS Training - Support Specialist | TRG | Training series |
| NOIS | anchor | nois_1_1_overview.docx | NOIS Version 1.1 - Overview of New Features | RN | Version overview = release note |
| NOIS | plain | noistm.docx | NOIS Technical Reference | TM | "Technical Reference" → Technical Manual; filename `_tm` |
| NOIS | plain | instructions.docx | NOIS Using NOIS GUI with Forum | SUP | Usage notes — supplement |
| TMP | anchor | TMP_5_2_4_DIBR.docx | TMP Release 5.2.4 | DIBR | Filename `_DIBR` |
| TMP | anchor | tmp_deployment_installation_rollback_backout_guide_tmp_4-6.docx | TMP Version 1.5 Release 4.6 DIBRO | DIBR | "DIBRO"; full filename is "deployment_installation_rollback_backout_guide" |
| TMP | anchor | tmp_4-6_rs.docx | TMP Version 1.5 Release 4.6 Requirements Specifications | RS | "Requirements Specifications"; filename `_rs` |
| TMP | anchor | tmp_4-8_requirements_signed.docx | TMP Version 2.0 Release 4.8 Requirements | RS | "Requirements"; `_signed` suffix (TMP context → RS) |
| TMP | anchor | pims_tm.docx | TMP Version 4.0 Release 4.9.0.8 PIMS TM | TM | "PIMS TM" in title; filename `pims_tm` |
| TMP | anchor | pims_tm_4909.docx | TMP Version 6.0 Release 4.9.0.9 PIMS TM | TM | (series sibling) |
| TMP | patch | sd_5_3_879_dibrg.docx | TMP VistA Patch 879 | RN | Filename `_dibrg` despite TMP context; content is patch release note |
| VBECS | anchor | vbecs_2_3_0_kda.docx | Laboratory: VBECS Version 2.3.0 Known Defects and Anomalies | SUP | Defect/anomaly log; filename `_kda` |
| VBECS | anchor | vbecs_2_3_1_kda.docx | Laboratory: VBECS Version 2.3.1 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | anchor | VBECS_2_3_2_kda.docx | Laboratory: VBECS Version 2.3.2 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | anchor | vbecs_2_3_3_kda.docx | Laboratory: VBECS Version 2.3.3 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | anchor | vbecs_2_3_4_kda.docx | Laboratory: VBECS Version 2.3.4 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | anchor | vbecs_2_4_0_kda.docx | Laboratory: VBECS Version 2.4.0 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | anchor | vbecs_2_4_1_kda.docx | Laboratory: VBECS Version 2.4.1 Known Defects and Anomalies | SUP | (series sibling) |
| VBECS | plain | vbecs_product_information.docx | Laboratory: VBECS Product Information Pamphlet | SUP | Informational pamphlet — supplement |
| XWB | patch | xwb1_1P44um.docx | XWB*1.1*35 and XWB*1.1*44 TCP/IP Supplement | TM | "TCP/IP Supplement" — technical; filename `_um` is misleading |
| XWB | patch | xwb_1_1_72_rm_r.docx | XWB*1.1*72 Readme File | RN | "Readme File" in title |
| XWB | patch | xwb_1_1_73_rm_r.docx | XWB*1.1*73 Readme File | RN | "Readme File" in title |

---

## Noise Candidates — Tag Rather Than Classify

Two documents in Cat C should be tagged with `noise_type` rather than assigned a doc_code:

| App | Filename | Title | Recommended noise_type |
|-----|----------|-------|----------------------|
| PRCA | archive_placeholder.docx | AR Archive demo | `test_document` |
| SD | Test_document_VDL.docx | Test Document VDL | `test_document` |

---

## Implementation Priority

To resolve the maximum number of rows with minimum effort:

1. **Add `\bAddendum\b` → UG** — resolves all 13 SD VSE User Guide Addendum series in one pattern.
2. **Add `\bWorkflow\b` → WF** — resolves 12 CAPRI docs (Cat D) and 1 DVBA doc (Cat A).
3. **Add `\b_kda\b` suffix to `_SLUG_SUFFIX_MAP`** — resolves all 7 VBECS Known Defects series.
4. **Add `\bTutorial\b` → TRG** — resolves 4 DI FM tutorial docs (if not already covered by QRG).
5. **Add `NOIS Training` prefix rule** → TRG for 6 NOIS training docs.
6. **Add `Supplement to Patch\b`** → SUP — resolves 3 XU Supplement docs.
7. **Add `\bRemediation\b`** → SUP — resolves MMRS*1*4.
8. **Add `\bMonograph\b`** → SUP — resolves Vista Monograph.
9. **Noise-tag 2 test documents** (PRCA archive placeholder; SD test document VDL).
10. **Resolve QAC PATS Data Migration Guide** — debug why `data\s+migration` pattern did not fire.
