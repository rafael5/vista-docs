# VistA Package Documentation Corpus Guide

*Generated: 2026-03-28. Covers 139 packages and 2,874 documents.*

## Table of Contents

- [ACKQ](#ackq), [ACR](#acr), [ADT](#adt), [AFJX](#afjx), [AMT](#amt), [ANRV](#anrv), [AR/WS](#ar/ws), [ASCD](#ascd), [ASU](#asu), [BMS](#bms), [CAPRI](#capri), [CCRA](#ccra)
- [CDSP](#cdsp), [CHDS](#chds), [CISS](#ciss), [CPRS](#cprs), [CPT](#cpt), [CRHD](#crhd), [DGBT](#dgbt), [DGJ](#dgj), [DI](#di), [DRM+](#drm+), [DVBA](#dvba), [EAS](#eas)
- [EC](#ec), [ECME](#ecme), [EDIS](#edis), [EFR](#efr), [EHM](#ehm), [EN](#en), [EPI](#epi), [EPSI](#epsi), [ETS](#ets), [FB](#fb), [FFP](#ffp), [FH](#fh)
- [FIM](#fim), [FMDC](#fmdc), [GEN](#gen), [GMPL](#gmpl), [GMRA](#gmra), [GMRC](#gmrc), [GMRV](#gmrv), [GMTS](#gmts), [HBPC](#hbpc), [HINQ](#hinq), [HL7](#hl7), [IB](#ib)
- [IBD](#ibd), [IFR](#ifr), [IVM](#ivm), [IVMB](#ivmb), [KAAJEE](#kaajee), [KMPD](#kmpd), [KMPR](#kmpr), [KMPS](#kmps), [KMPV](#kmpv), [LA](#la), [LEDI](#ledi), [LEX](#lex)
- [LHS](#lhs), [LR](#lr), [MAG](#mag), [MC](#mc), [MD](#md), [MED](#med), [MMRS](#mmrs), [MON](#mon), [MPIF](#mpif), [NCR](#ncr), [NPM](#npm), [NUMI](#numi)
- [NUPA](#nupa), [NUR](#nur), [ONC](#onc), [OOPS](#oops), [PAIT](#pait), [PCMM](#pcmm), [PECS](#pecs), [POC](#poc), [PRC](#prc), [PRCA](#prca), [PRCN](#prcn), [PREA](#prea)
- [PRED](#pred), [PREM](#prem), [PRF](#prf), [PRPF](#prpf), [PRS](#prs), [PSA](#psa), [PSB](#psb), [PSD](#psd), [PSJ](#psj), [PSN](#psn), [PSO](#pso), [PSS](#pss)
- [PSU](#psu), [PSX](#psx), [PX](#px), [PXRM](#pxrm), [QAC](#qac), [QAM](#qam), [QAO](#qao), [QAP](#qap), [RA](#ra), [RMPR](#rmpr), [ROES](#roes), [ROEV](#roev)
- [ROR](#ror), [RT](#rt), [SD](#sd), [SPN](#spn), [SQLI](#sqli), [SR](#sr), [SRA](#sra), [STS](#sts), [TBI](#tbi), [TIU](#tiu), [TMP](#tmp), [VALM](#valm)
- [VAP](#vap), [VAQ](#vaq), [VDEF](#vdef), [VES](#ves), [VHIC](#vhic), [VIAB](#viab), [VPFS](#vpfs), [VPR](#vpr), [WII](#wii), [WV](#wv), [XM](#xm), [XOBE](#xobe)
- [XOBV](#xobv), [XOBW](#xobw), [XQOR](#xqor), [XT](#xt), [XU](#xu), [XWB](#xwb), [YS](#ys)

---

## Corpus Overview

This guide covers the VistA Documentation Library (VDL) corpus as crawled and enriched from the VA VDL. It spans 140 VistA application packages with a total of 2,874 documents, 189,011 pages, and approximately 20,635,147 words of technical content. Documents range from release notes and installation guides to comprehensive user manuals and technical references.

### Corpus Summary Statistics

| Metric | Value |
|--------|-------|
| Total Packages | 139 |
| Total Documents | 2,874 |
| Total Pages | 189,011 |
| Total Figures | 18,616 |
| Total Tables | 43,009 |
| Total Appendices | 1,842 |
| Total Words | 20,635,147 |
| Total Revision Entries | 6,895 |

### Document Type Distribution

| Type | Count | % of Corpus |
|------|-------|-------------|
| installation-guide | 857 | 29.8% |
| release-note | 735 | 25.6% |
| user-manual | 563 | 19.6% |
| technical-manual | 318 | 11.1% |
| change-page | 163 | 5.7% |
| supplement | 68 | 2.4% |
| base-dev | 46 | 1.6% |
| base-security | 26 | 0.9% |
| unknown | 25 | 0.9% |
| base-hl7 | 24 | 0.8% |
| base-setup | 22 | 0.8% |
| base-impl | 22 | 0.8% |
| quick-ref | 19 | 0.7% |

### Document Type Definitions

The VDL taxonomy collapses VA doc codes (RN, DIBR, IG, UM, UG, TM, etc.) into the 13 canonical types used throughout this guide. **Unique knowledge** refers to durable, non-redundant content — concepts, procedures, reference data, and design decisions that do not appear in any other document in the corpus.

| Type | VA Codes | Description | Unique Knowledge |
|------|----------|-------------|-----------------|
| **installation-guide** | IG, DIBR, IG-IMP | Step-by-step instructions for installing, deploying, configuring, rolling back, or converting a package. Includes the modern combined Deploy/Install/Back-out/Rollback (DIBR) format. Patch-specific install guides repeat the same procedure with minor variations across releases. | **Low** — Highly repetitive across patch versions; the install procedure is structurally identical from one patch to the next. Unique content is limited to patch-specific pre/post steps. |
| **release-note** | RN | Patch-level change log describing what changed, why, and any operational impact. One document per patch. | **Low** — Each release note is brief and patch-specific. Aggregate value is high for audit trails, but individual documents carry minimal unique knowledge. |
| **user-manual** | UM, UG, SG, SMG, TG | End-user and operational reference covering workflows, menu options, data entry, and reports. Includes User Guide, User's Guide, Administrator's Guide, and Systems Management Guide variants. Anchor versions are comprehensive; patch-updated versions often differ only in a few sections. | **High** — Anchor (non-patch) user manuals contain the definitive operational reference for a package. Patch-updated versions are lower-value due to overlap with prior versions. |
| **technical-manual** | TM, VDD | Design, architecture, data dictionary, global layout, file structure, and cross-package interface documentation. The primary reference for programmers, DBAs, and integration developers. | **High** — Contains unique structural and architectural knowledge not found elsewhere in the corpus. Often the only source for global layouts, file definitions, and cross-reference logic. |
| **change-page** | CP | A targeted page-level correction to an existing manual — replaces specific pages in a printed document. Common in older packages before electronic distribution became standard. | **Low** — Superseded by the manual it amends. Retains marginal value only for historical reconstruction of document versions. |
| **supplement** | SUP, SP, POM, TRG | Adjunct material that extends or supports a primary document. Includes: Production Operations Manual (POM / ops runbook), Training Guide, Glossary, Troubleshooting Guide, Workflow diagrams, Checklist, and Flowchart. | **Medium** — POMs and troubleshooting guides contain operationally unique content. Training guides and glossaries may duplicate content from user manuals. |
| **base-dev** | API, BASE-DEV | Programmer manual, API specification, or developer guide. Documents the M/MUMPS routines, entry points, callable APIs, and integration interfaces exposed by the package. | **High** — Unique low-level technical content; the primary (often only) source for programmatic integration with a package. |
| **base-security** | — | Security guide documenting access controls, encryption, audit logs, role-based permissions, and STIG compliance for the package. | **High** — Security configuration is package-specific and not duplicated elsewhere. |
| **base-hl7** | INT | HL7 interface specification documenting message formats, trigger events, segment definitions, and field mappings for inbound and outbound HL7 interfaces. | **High** — Interface specifications are unique per package and essential for integration work. |
| **base-setup** | CFG, SG-SET | Setup or configuration guide covering site parameters, option assignments, file initialization, and environment-specific settings. Distinct from an installation guide in that it covers ongoing configuration rather than one-time install steps. | **Medium** — Contains unique site configuration detail, but often overlaps with the installation guide and user manual. |
| **base-impl** | IG-IMP | Implementation guide covering the planning, workflow redesign, and organizational steps required to operationalize a package at a VHA site — beyond the purely technical install steps. | **Medium** — Unique process and change-management content, but limited audience (implementation teams only). |
| **quick-ref** | QRG, QR, REF | Condensed reference card, cheat sheet, Getting Started guide, Tutorial, FAQ, or Brochure. Designed for quick lookup rather than comprehensive coverage. | **Low–Medium** — Distills content from longer manuals; rarely introduces new information. Useful as an access layer but not a primary knowledge source. |
| **unknown** | — | Documents whose type could not be determined from filename or title. Typically atypical titles (menus, demos, scenario documents, patch follow-ups) that do not match any standard VA doc type pattern. | **Variable** — Requires case-by-case review. |

### Package Summary Table

| Package | Docs | Date Range | Pages | Words | Tables | Figs | Appendices | Update Density | Knowledge Ratio | Top Doc Types |
|---------|------|------------|-------|-------|--------|------|------------|----------------|-----------------|---------------|
| [SD](#sd) | 345 | September 2009 → March 2026 | 5,044 | 662,108 | 2,548 | 1,292 | 59 | 8.5 docs/yr | 59% | technical-manual (133), release-note (72) |
| [IB](#ib) | 152 | February 1994 → March 2026 | 9,588 | 545,913 | 809 | 19 | 25 | 4.4 docs/yr | 8% | installation-guide (98), release-note (42) |
| [PSO](#pso) | 141 | December 1997 → September 2025 | 7,127 | 2,054,517 | 1,890 | 783 | 110 | 3.2 docs/yr | 40% | installation-guide (55), user-manual (47) |
| [ADT](#adt) | 137 | August 1993 → December 2025 | 4,101 | 644,263 | 568 | 4,502 | 29 | 3.3 docs/yr | 22% | release-note (87), user-manual (29) |
| [PRCA](#prca) | 105 | March 1995 → December 2025 | 2,262 | 445,581 | 561 | 208 | 27 | 2.8 docs/yr | 19% | installation-guide (67), user-manual (18) |
| [PSJ](#psj) | 96 | December 1997 → August 2025 | 47,268 | 960,459 | 2,499 | 198 | 16 | 2.8 docs/yr | 19% | change-page (52), release-note (20) |
| [VES](#ves) | 95 | March 2018 → December 2025 | 928 | 161,452 | 428 | 504 | 0 | 8.6 docs/yr | 29% | release-note (67), user-manual (21) |
| [CPRS](#cprs) | 92 | April 2003 → February 2026 | 4,352 | 887,620 | 554 | 47 | 96 | 3.2 docs/yr | 22% | release-note (41), installation-guide (31) |
| [YS](#ys) | 78 | December 1994 → July 2025 | 11,039 | 283,415 | 569 | 301 | 66 | 2.1 docs/yr | 17% | installation-guide (55), release-note (10) |
| [PSS](#pss) | 77 | September 1997 → August 2025 | 6,199 | 632,308 | 719 | 66 | 131 | 2.3 docs/yr | 19% | change-page (31), release-note (20) |
| [PXRM](#pxrm) | 76 | May 2002 → September 2022 | 9,774 | 732,166 | 1,159 | 80 | 154 | 2.4 docs/yr | 34% | installation-guide (38), user-manual (15) |
| [XU](#xu) | 71 | April 1995 → August 2025 | 2,609 | 739,225 | 1,156 | 1,380 | 56 | 0.4 docs/yr | 77% | base-dev (31), user-manual (10) |
| [CAPRI](#capri) | 68 | June 2001 → January 2026 | 1,862 | 379,258 | 683 | 213 | 6 | 2.0 docs/yr | 26% | release-note (47), supplement (12) |
| [MAG](#mag) | 63 | March 2002 → January 2025 | 8,182 | 776,974 | 1,502 | 1,136 | 108 | 0.8 docs/yr | 71% | user-manual (29), installation-guide (17) |
| [MD](#md) | 63 | April 2004 → July 2025 | 3,136 | 716,322 | 764 | 34 | 34 | 1.7 docs/yr | 40% | installation-guide (23), user-manual (9) |
| [TMP](#tmp) | 56 | August 2019 → July 2025 | 2,126 | 324,322 | 1,347 | 223 | 43 | 4.4 docs/yr | 48% | installation-guide (24), technical-manual (14) |
| [PSB](#psb) | 46 | February 2004 → February 2026 | 1,707 | 110,628 | 736 | 78 | 35 | 1.6 docs/yr | 22% | installation-guide (16), change-page (11) |
| [ANRV](#anrv) | 35 | June 1998 → March 2026 | 746 | 124,241 | 174 | 61 | 22 | 0.9 docs/yr | 29% | installation-guide (14), release-note (11) |
| [ECME](#ecme) | 35 | October 2004 → December 2025 | 655 | 161,454 | 217 | 0 | 1 | 1.6 docs/yr | 6% | installation-guide (23), release-note (10) |
| [PSD](#psd) | 35 | March 1997 → December 2021 | 820 | 111,672 | 189 | 100 | 4 | 1.0 docs/yr | 26% | change-page (21), user-manual (6) |
| [SR](#sr) | 34 | July 1993 → July 2024 | 4,879 | 398,671 | 1,707 | 0 | 10 | 0.9 docs/yr | 18% | change-page (16), release-note (12) |
| [KAAJEE](#kaajee) | 32 | April 2009 → May 2024 | 93 | 248,712 | 1,526 | 9 | 23 | 2.0 docs/yr | 6% | installation-guide (20), release-note (10) |
| [BMS](#bms) | 31 | January 2020 → February 2026 | 4,912 | 528,382 | 1,775 | 37 | 25 | 1.0 docs/yr | 81% | user-manual (14), technical-manual (11) |
| [RA](#ra) | 30 | April 1998 → January 2026 | 790 | 260,637 | 512 | 55 | 9 | 0.7 docs/yr | 33% | release-note (19), base-hl7 (4) |
| [PECS](#pecs) | 29 | July 2012 → May 2025 | 812 | 133,101 | 231 | 203 | 41 | 1.6 docs/yr | 31% | installation-guide (12), release-note (8) |
| [GMRC](#gmrc) | 28 | April 2002 → January 2026 | 1,506 | 242,460 | 309 | 958 | 18 | 0.7 docs/yr | 54% | installation-guide (15), user-manual (9) |
| [FB](#fb) | 27 | January 1995 → December 2025 | 446 | 298,614 | 238 | 0 | 32 | 0.7 docs/yr | 22% | release-note (13), installation-guide (8) |
| [RMPR](#rmpr) | 27 | December 1995 → October 2024 | 1,120 | 25,597 | 2,214 | 0 | 25 | 0.5 docs/yr | 48% | user-manual (11), release-note (8) |
| [PRC](#prc) | 26 | August 1999 → March 2026 | 2,922 | 364,340 | 2,014 | 409 | 26 | 0.2 docs/yr | 85% | user-manual (17), installation-guide (4) |
| [PSX](#psx) | 24 | April 1997 → August 2024 | 8,949 | 112,596 | 163 | 8 | 22 | 0.7 docs/yr | 17% | release-note (8), installation-guide (6) |
| [PRED](#pred) | 23 | June 2012 → May 2025 | 693 | 111,729 | 66 | 102 | 42 | 1.8 docs/yr | 0% | installation-guide (18), release-note (5) |
| [EDIS](#edis) | 21 | September 2010 → April 2025 | 1,376 | 180,090 | 411 | 276 | 2 | 0.5 docs/yr | 62% | installation-guide (7), technical-manual (6) |
| [LR](#lr) | 21 | October 1994 → October 2024 | 1,241 | 591,541 | 155 | 86 | 6 | 0.3 docs/yr | 62% | user-manual (8), release-note (4) |
| [PREM](#prem) | 20 | September 2013 → May 2025 | 347 | 72,296 | 80 | 41 | 17 | 1.5 docs/yr | 10% | installation-guide (13), release-note (5) |
| [PSN](#psn) | 20 | October 1998 → August 2025 | 821 | 182,681 | 188 | 0 | 3 | 0.5 docs/yr | 35% | change-page (6), release-note (4) |
| [GMRV](#gmrv) | 19 | October 2002 → January 2021 | 135 | 91,756 | 93 | 8 | 11 | 0.7 docs/yr | 37% | installation-guide (8), release-note (4) |
| [IVMB](#ivmb) | 17 | September 1999 → September 2006 | 156 | 27,169 | 146 | 0 | 6 | 1.6 docs/yr | 35% | release-note (7), installation-guide (4) |
| [HL7](#hl7) | 16 | October 1995 → May 2006 | 647 | 221,090 | 779 | 25 | 23 | 0.3 docs/yr | 81% | supplement (5), base-hl7 (4) |
| [PSU](#psu) | 16 | June 2005 → April 2016 | 524 | 47,149 | 108 | 48 | 0 | 1.0 docs/yr | 31% | change-page (5), release-note (4) |
| [LA](#la) | 15 | October 1995 → April 2017 | 349 | 72,811 | 261 | 22 | 5 | 0.3 docs/yr | 60% | installation-guide (7), base-hl7 (4) |
| [NUMI](#numi) | 15 | April 2021 → March 2026 | 1,776 | 293,177 | 443 | 1,344 | 90 | 0.0 docs/yr | 100% | user-manual (10), base-setup (5) |
| [PX](#px) | 15 | August 1996 → March 2026 | 568 | 127,601 | 124 | 0 | 15 | 0.4 docs/yr | 27% | release-note (6), installation-guide (5) |
| [ROR](#ror) | 14 | May 2017 → June 2024 | 312 | 39,785 | 365 | 0 | 4 | 1.8 docs/yr | 7% | release-note (13), user-manual (1) |
| [XOBV](#xobv) | 13 | May 2006 → March 2022 | 226 | 132,243 | 340 | 24 | 15 | 0.4 docs/yr | 46% | release-note (4), base-dev (3) |
| [DRM+](#drm+) | 12 | April 1989 | 0 | 14,902 | 80 | 0 | 0 | 12.0 docs/yr | 0% | installation-guide (8), release-note (4) |
| [TIU](#tiu) | 12 | July 1997 → December 2025 | 974 | 143,559 | 188 | 7 | 13 | 0.2 docs/yr | 58% | installation-guide (4), user-manual (3) |
| [DI](#di) | 11 | June 1996 → July 2025 | 1,709 | 348,231 | 523 | 1,048 | 8 | 0.1 docs/yr | 82% | user-manual (3), base-dev (2) |
| [EAS](#eas) | 11 | March 2001 → September 2021 | 264 | 51,851 | 64 | 19 | 27 | 0.3 docs/yr | 45% | release-note (3), installation-guide (3) |
| [PRF](#prf) | 11 | September 2003 → March 2019 | 256 | 59,955 | 153 | 3 | 7 | 0.4 docs/yr | 36% | release-note (5), user-manual (3) |
| [HBPC](#hbpc) | 10 | November 1993 → August 2021 | 103 | 64,016 | 70 | 25 | 0 | 0.1 docs/yr | 60% | release-note (2), installation-guide (2) |
| [PCMM](#pcmm) | 10 | September 1998 → December 2012 | 135 | 52,385 | 59 | 0 | 4 | 0.4 docs/yr | 30% | release-note (4), user-manual (3) |
| [PRS](#prs) | 10 | August 1995 → March 2018 | 626 | 108,913 | 700 | 3 | 2 | 0.3 docs/yr | 30% | release-note (4), installation-guide (2) |
| [PSA](#psa) | 10 | October 1997 → January 2025 | 407 | 78,174 | 100 | 14 | 3 | 0.2 docs/yr | 40% | installation-guide (4), user-manual (3) |
| [VHIC](#vhic) | 10 | May 2012 → May 2024 | 258 | 35,439 | 44 | 361 | 0 | 0.4 docs/yr | 50% | user-manual (5), release-note (4) |
| [XM](#xm) | 10 | August 2002 → June 2017 | 176 | 211,197 | 728 | 60 | 7 | 0.2 docs/yr | 60% | user-manual (3), quick-ref (2) |
| [XWB](#xwb) | 9 | October 1997 → September 2021 | 459 | 99,369 | 188 | 161 | 1 | 0.1 docs/yr | 67% | user-manual (3), release-note (2) |
| [DGBT](#dgbt) | 8 | April 2002 → February 2024 | 189 | 36,723 | 20 | 0 | 4 | 0.2 docs/yr | 38% | release-note (3), user-manual (2) |
| [DVBA](#dvba) | 8 | April 1995 → July 2022 | 188 | 48,458 | 12 | 0 | 2 | 0.1 docs/yr | 62% | installation-guide (2), user-manual (2) |
| [FH](#fh) | 8 | February 2005 → March 2019 | 1,093 | 125,649 | 356 | 0 | 0 | 0.4 docs/yr | 38% | change-page (3), user-manual (2) |
| [GMRA](#gmra) | 8 | August 2005 → January 2024 | 326 | 85,729 | 124 | 16 | 0 | 0.3 docs/yr | 25% | release-note (4), installation-guide (2) |
| [IVM](#ivm) | 8 | October 1994 → February 2019 | 212 | 25,325 | 162 | 0 | 6 | 0.2 docs/yr | 25% | release-note (5), installation-guide (1) |
| [MMRS](#mmrs) | 8 | January 2010 → April 2017 | 332 | 60,126 | 144 | 151 | 14 | 0.3 docs/yr | 62% | user-manual (3), installation-guide (2) |
| [NUR](#nur) | 8 | April 1997 → May 2018 | 34 | 157,996 | 253 | 0 | 0 | 0.3 docs/yr | 25% | change-page (3), release-note (2) |
| [ACKQ](#ackq) | 7 | February 2000 → August 2014 | 229 | 45,044 | 57 | 0 | 10 | 0.2 docs/yr | 57% | technical-manual (3), release-note (2) |
| [ACR](#acr) | 7 | January 1998 → October 2018 | 562 | 60,199 | 146 | 0 | 2 | 0.1 docs/yr | 14% | unknown (3), release-note (2) |
| [CRHD](#crhd) | 7 | June 2008 → August 2024 | 117 | 17,594 | 37 | 6 | 0 | 0.3 docs/yr | 29% | installation-guide (4), technical-manual (1) |
| [EC](#ec) | 7 | September 2022 → May 2025 | 277 | 41,606 | 23 | 252 | 10 | 1.9 docs/yr | 29% | installation-guide (5), technical-manual (1) |
| [EPI](#epi) | 7 | July 2014 → September 2015 | 848 | 147,503 | 168 | 10 | 14 | 2.5 docs/yr | 57% | user-manual (4), release-note (2) |
| [IBD](#ibd) | 7 | April 1997 → April 2014 | 214 | 54,052 | 143 | 0 | 13 | 0.2 docs/yr | 43% | release-note (2), base-impl (1) |
| [LEDI](#ledi) | 7 | December 2004 → September 2013 | 628 | 146,917 | 166 | 150 | 5 | 0.2 docs/yr | 71% | base-impl (2), installation-guide (2) |
| [MED](#med) | 7 | June 2010 → December 2025 | 188 | 29,815 | 93 | 97 | 4 | 0.3 docs/yr | 29% | installation-guide (5), technical-manual (1) |
| [PREA](#prea) | 7 | August 2023 → January 2026 | 261 | 36,926 | 32 | 485 | 3 | 0.4 docs/yr | 86% | quick-ref (2), supplement (2) |
| [TBI](#tbi) | 7 | July 2015 → May 2018 | 346 | 29,455 | 214 | 0 | 10 | 0.7 docs/yr | 57% | user-manual (3), unknown (1) |
| [XOBW](#xobw) | 7 | February 2011 → August 2020 | 95 | 34,030 | 45 | 43 | 6 | 0.4 docs/yr | 43% | installation-guide (3), base-dev (1) |
| [XT](#xt) | 7 | April 1995 → April 2021 | 275 | 59,269 | 162 | 111 | 3 | 0.1 docs/yr | 71% | technical-manual (2), supplement (2) |
| [EN](#en) | 6 | August 1993 → October 2024 | 419 | 163,980 | 325 | 0 | 3 | 0.1 docs/yr | 67% | technical-manual (3), installation-guide (2) |
| [MPIF](#mpif) | 6 | April 1999 → November 2016 | 171 | 99,941 | 329 | 9 | 11 | 0.1 docs/yr | 83% | technical-manual (2), base-hl7 (1) |
| [NUPA](#nupa) | 6 | April 2012 → January 2014 | 402 | 32,643 | 38 | 0 | 6 | 0.6 docs/yr | 83% | user-manual (4), installation-guide (1) |
| [OOPS](#oops) | 6 | June 2002 → September 2008 | 222 | 31,259 | 18 | 0 | 0 | 0.5 docs/yr | 50% | release-note (2), installation-guide (1) |
| [PAIT](#pait) | 6 | March 2004 → March 2010 | 1,296 | 30,367 | 158 | 0 | 4 | 0.5 docs/yr | 50% | release-note (3), supplement (1) |
| [QAC](#qac) | 6 | March 2007 → April 2013 | 327 | 59,215 | 168 | 0 | 7 | 0.5 docs/yr | 33% | installation-guide (3), user-manual (2) |
| [VPFS](#vpfs) | 6 | July 2020 | 214 | 44,359 | 245 | 0 | 19 | 2.0 docs/yr | 67% | user-manual (4), release-note (1) |
| [AR/WS](#ar/ws) | 5 | January 1994 | 336 | 61,670 | 2 | 0 | 1 | 2.0 docs/yr | 60% | user-manual (2), installation-guide (1) |
| [GEN](#gen) | 5 | August 1992 → March 1995 | 164 | 24,003 | 211 | 0 | 0 | 0.8 docs/yr | 60% | installation-guide (1), base-security (1) |
| [GMTS](#gmts) | 5 | December 2019 → November 2023 | 517 | 118,077 | 79 | 0 | 16 | 0.3 docs/yr | 80% | technical-manual (2), user-manual (2) |
| [HINQ](#hinq) | 5 | March 1992 → November 2005 | 141 | 22,268 | 22 | 0 | 1 | 0.1 docs/yr | 60% | technical-manual (1), user-manual (1) |
| [ROES](#roes) | 5 | October 2003 → June 2019 | 209 | 44,593 | 46 | 10 | 6 | 0.1 docs/yr | 60% | installation-guide (2), base-security (1) |
| [AFJX](#afjx) | 4 | February 1996 | 0 | 16,634 | 83 | 0 | 0 | 2.0 docs/yr | 50% | installation-guide (1), release-note (1) |
| [ASCD](#ascd) | 4 | August 1996 → September 2007 | 242 | 51,442 | 37 | 0 | 3 | 0.1 docs/yr | 75% | user-manual (2), release-note (1) |
| [CDSP](#cdsp) | 4 | October 2023 → February 2024 | 24 | 7,525 | 36 | 0 | 0 | 4.0 docs/yr | 0% | installation-guide (4) |
| [CHDS](#chds) | 4 | January 2022 → July 2025 | 50 | 10,027 | 22 | 0 | 1 | 1.1 docs/yr | 0% | installation-guide (4) |
| [CPT](#cpt) | 4 | May 1997 | 0 | 6,789 | 0 | 0 | 0 | 2.0 docs/yr | 50% | installation-guide (1), release-note (1) |
| [FMDC](#fmdc) | 4 | March 1998 → July 1999 | 24 | 11,256 | 36 | 0 | 0 | 1.5 docs/yr | 50% | quick-ref (1), installation-guide (1) |
| [GMPL](#gmpl) | 4 | September 1994 → April 2025 | 197 | 17,638 | 9 | 0 | 2 | 0.1 docs/yr | 50% | installation-guide (1), release-note (1) |
| [MC](#mc) | 4 | September 1996 → July 2014 | 341 | 64,445 | 50 | 0 | 1 | 0.1 docs/yr | 50% | release-note (1), installation-guide (1) |
| [POC](#poc) | 4 | June 2005 → June 2018 | 188 | 43,734 | 49 | 1 | 0 | 0.1 docs/yr | 75% | user-manual (2), base-hl7 (1) |
| [PRCN](#prcn) | 4 | June 1996 | 146 | 24,757 | 57 | 0 | 0 | 1.0 docs/yr | 75% | installation-guide (1), base-security (1) |
| [PRPF](#prpf) | 4 | February 1989 | 597 | 34,884 | 30 | 0 | 2 | 0.0 docs/yr | 100% | user-manual (3), technical-manual (1) |
| [QAM](#qam) | 4 | September 1993 | 217 | 34,281 | 213 | 0 | 6 | 1.0 docs/yr | 75% | user-manual (2), installation-guide (1) |
| [QAO](#qao) | 4 | September 1993 | 155 | 22,732 | 235 | 0 | 0 | 1.0 docs/yr | 75% | user-manual (2), release-note (1) |
| [RT](#rt) | 4 | November 1991 | 222 | 49,388 | 12 | 0 | 1 | 2.0 docs/yr | 50% | installation-guide (1), release-note (1) |
| [VDEF](#vdef) | 4 | December 2004 → June 2019 | 45 | 17,620 | 48 | 8 | 9 | 0.1 docs/yr | 25% | installation-guide (2), technical-manual (1) |
| [VIAB](#viab) | 4 | June 2016 → May 2019 | 48 | 9,747 | 7 | 3 | 0 | 1.0 docs/yr | 25% | installation-guide (3), user-manual (1) |
| [AMT](#amt) | 3 | March 2010 → February 2026 | 97 | 17,998 | 24 | 0 | 2 | 0.1 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [ASU](#asu) | 3 | July 1997 → May 2010 | 84 | 14,041 | 35 | 0 | 2 | 0.1 docs/yr | 67% | user-manual (1), technical-manual (1) |
| [DGJ](#dgj) | 3 | April 2002 | 543 | 14,267 | 11 | 0 | 0 | 1.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [FIM](#fim) | 3 | May 2003 | 152 | 12,977 | 159 | 0 | 5 | 1.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [KMPD](#kmpd) | 3 | September 2012 → December 2015 | 116 | 29,620 | 69 | 61 | 0 | 0.3 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [KMPR](#kmpr) | 3 | June 2003 | 0 | 13,738 | 104 | 0 | 0 | 1.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [KMPV](#kmpv) | 3 | July 2020 → January 2024 | 83 | 17,230 | 35 | 34 | 1 | 0.3 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [LEX](#lex) | 3 | September 1996 | 1,435 | 61,484 | 282 | 0 | 3 | 1.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [NPM](#npm) | 3 | December 1992 | 34 | 8,927 | 2 | 0 | 0 | 1.0 docs/yr | 0% | unknown (2), installation-guide (1) |
| [SPN](#spn) | 3 | February 2011 → May 2011 | 163 | 33,636 | 30 | 0 | 5 | 2.0 docs/yr | 33% | installation-guide (1), release-note (1) |
| [SRA](#sra) | 3 | June 2024 | 178 | 15,694 | 76 | 0 | 4 | 1.0 docs/yr | 67% | release-note (1), technical-manual (1) |
| [STS](#sts) | 3 | December 2010 → August 2011 | 103 | 17,231 | 65 | 48 | 4 | 0.0 docs/yr | 100% | technical-manual (1), user-manual (1) |
| [VAQ](#vaq) | 3 | November 1993 → August 2018 | 163 | 31,109 | 67 | 65 | 8 | 0.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [VPR](#vpr) | 3 | September 2011 → January 2024 | 208 | 20,662 | 108 | 38 | 1 | 0.1 docs/yr | 67% | base-dev (1), installation-guide (1) |
| [WV](#wv) | 3 | September 1998 → May 2023 | 159 | 40,577 | 8 | 0 | 3 | 0.0 docs/yr | 67% | installation-guide (1), technical-manual (1) |
| [XOBE](#xobe) | 3 | November 2006 | 71 | 11,935 | 56 | 0 | 2 | 1.0 docs/yr | 67% | base-dev (1), installation-guide (1) |
| [EHM](#ehm) | 2 | March 2026 | 140 | 30,758 | 46 | 2 | 0 | 0.0 docs/yr | 100% | technical-manual (1), user-manual (1) |
| [EPSI](#epsi) | 2 | April 2023 → February 2026 | 15 | 1,983 | 11 | 2 | 5 | 0.7 docs/yr | 50% | installation-guide (2), user-manual (1) |
| [KMPS](#kmps) | 2 | December 2015 | 25 | 7,049 | 12 | 5 | 0 | 0.0 docs/yr | 100% | technical-manual (1), user-manual (1) |
| [NCR](#ncr) | 2 | April 2024 | 27 | 3,927 | 13 | 0 | 2 | 1.0 docs/yr | 50% | installation-guide (1), technical-manual (1) |
| [ONC](#onc) | 2 | JUNE 2014 | 95 | 18,200 | 17 | 0 | 2 | 0.0 docs/yr | 100% | technical-manual (1), user-manual (1) |
| [QAP](#qap) | 2 | June 1995 → APRIL 2024 | 120 | 19,575 | 1 | 0 | 0 | 0.0 docs/yr | 100% | user-manual (2) |
| [SQLI](#sqli) | 2 | October 1997 | 14 | 28,765 | 87 | 0 | 2 | 0.0 docs/yr | 100% | user-manual (2) |
| [VAP](#vap) | 2 | August 2018 → August 2020 | 272 | 46,850 | 89 | 266 | 4 | 0.0 docs/yr | 100% | user-manual (2) |
| [WII](#wii) | 2 | February 2009 | 46 | 6,848 | 9 | 1 | 5 | 0.0 docs/yr | 100% | technical-manual (1), user-manual (1) |
| [XQOR](#xqor) | 2 | August 1994 | 29 | 6,177 | 4 | 0 | 0 | 1.0 docs/yr | 50% | installation-guide (1), technical-manual (1) |
| [CCRA](#ccra) | 1 | August 2018 | 88 | 8,904 | 15 | 115 | 2 | 0.0 docs/yr | 100% | user-manual (1) |
| [CISS](#ciss) | 1 | N/A | 33 | 6,602 | 11 | 0 | 0 | 0.0 docs/yr | 200% | supplement (2) |
| [EFR](#efr) | 1 | August 2013 | 281 | 22,015 | 198 | 0 | 7 | 0.0 docs/yr | 100% | user-manual (1) |
| [ETS](#ets) | 1 | June 2017 | 33 | 6,446 | 6 | 30 | 0 | 0.0 docs/yr | 100% | technical-manual (1) |
| [FFP](#ffp) | 1 | September 2021 | 14 | 2,460 | 2 | 0 | 0 | 0.0 docs/yr | 100% | user-manual (1) |
| [IFR](#ifr) | 1 | June 2001 | 0 | 29,050 | 181 | 0 | 2 | 0.0 docs/yr | 100% | supplement (1) |
| [LHS](#lhs) | 1 | August 2021 | 17 | 3,415 | 9 | 0 | 0 | 1.0 docs/yr | 0% | installation-guide (1) |
| [MON](#mon) | 1 | October 2013 | 239 | 79,328 | 3 | 0 | 1 | 0.0 docs/yr | 0% | — |
| [ROEV](#roev) | 1 | August 2015 | 44 | 5,378 | 12 | 0 | 0 | 0.0 docs/yr | 100% | user-manual (1) |
| [VALM](#valm) | 1 | March 2025 | 70 | 16,484 | 13 | 16 | 1 | 0.0 docs/yr | 100% | base-dev (1) |

---

## Package Chapters

<a id="ackq"></a>
## ACKQ — Quality Audiology and Speech Analysis and Reporting

[Back to TOC](#table-of-contents)

Quality Audiology and Speech Analysis and Reporting (QUASAR) is a VistA software package written for the Audiology and Speech Pathology Service. QUASAR is used to enter, edit, and retrieve data for each episode of care.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | February 2000 → August 2014 |
| Total Pages | 229 |
| Total Words | 45,044 |
| Total Tables | 57 |
| Total Figures | 0 |
| Total Appendices | 10 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 57% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 3 |
| release-note | 2 |
| installation-guide | 1 |
| user-manual | 1 |

### Notable Documents

- **QUASAR Version 3 User Manual (Updated ACKQ*3*21)** (user-manual, 33,022 words)
- **QUASAR Version 3 Technical/Pkg Security (Updated ACKQ*3*13)** (technical-manual, 8,446 words)
- **ACKQ*3*12 Audiometric Exam Module Technical Manual** (technical-manual, 8,403 words)
- **ACKQ*3*13 QUASAR Audiogram Module Install/Implement Guide** (installation-guide, 3,403 words)
- **QUASAR Version 3 Technical Manual (Updated ACKQ*3*21)** (technical-manual, 2,584 words)

---

<a id="acr"></a>
## ACR — Ambulatory Care Reporting

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | January 1998 → October 2018 |
| Total Pages | 562 |
| Total Words | 60,199 |
| Total Tables | 146 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 14% |

### Document Types

| Type | Count |
|------|-------|
| unknown | 3 |
| release-note | 2 |
| technical-manual | 1 |
| installation-guide | 1 |

### Notable Documents

- **Ambulatory Care Reporting Technical Manual** (technical-manual, 66,115 words)
- **Ambulatory Care Reporting Menu** (unknown, 13,382 words)
- **Appendix - IEMM Error Table** (unknown, 9,316 words)
- **ACRP Interface Toolkit** (unknown, 9,097 words)
- **SD*5.3*593 ACR Release Notes** (release-note, 2,976 words)

---

<a id="adt"></a>
## ADT — Admission, Discharge, Transfer / Registration

[Back to TOC](#table-of-contents)

The Admission, Discharge, Transfer (ADT) module provides a comprehensive range of software dedicated to the support of administrative functions related to patient admission, discharge, transfer, and registration.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 137 |
| Date Range | August 1993 → December 2025 |
| Total Pages | 4,101 |
| Total Words | 644,263 |
| Total Tables | 568 |
| Total Figures | 4,502 |
| Total Appendices | 29 |
| Update Density | 3.3 docs/yr |
| Knowledge Ratio | 22% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 87 |
| user-manual | 29 |
| installation-guide | 20 |
| technical-manual | 1 |

### Notable Documents

- **PIMS Version 5.3 ADT Technical Manual** (technical-manual, 69,983 words)
- **PIMS Version 5.3 User Manual - Registration Menu** (user-manual, 56,609 words)
- **PIMS Version 5.3 Release Notes** (release-note, 31,802 words)
- **PIMS Version 5.3 User Manual - PTF Menu** (user-manual, 31,295 words)
- **Integrated Scheduling Solution (ISS) Release 1.22.3 User Guide** (user-manual, 22,114 words)

---

<a id="afjx"></a>
## AFJX — Network Health Exchange

[Back to TOC](#table-of-contents)

Network Health Exchange (NHE) is a Veterans Health Information Systems and Technology Architecture (VistA) module that provides clinicians quick and easy access to patients' information from any VA medical facility where a patient has received care.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | February 1996 |
| Total Pages | 0 |
| Total Words | 16,634 |
| Total Tables | 83 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Network Health Exchange Version 5 User Manual** (user-manual, 9,374 words)
- **Network Health Exchange Version 5 Installation Guide** (installation-guide, 6,967 words)
- **Network Health Exchange Version 5 Technical Manual** (technical-manual, 6,760 words)
- **Network Health Exchange Version 5 Release Notes** (release-note, 697 words)

---

<a id="amt"></a>
## AMT — Automated Medical Information Exchange

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | March 2010 → February 2026 |
| Total Pages | 97 |
| Total Words | 17,998 |
| Total Tables | 24 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Anticoagulation Management Tool Installation/Implementation Guide** (installation-guide, 11,391 words)
- **Anticoagulation Management Tool User Manual** (user-manual, 7,796 words)
- **Anticoagulation Management Tool Technical Manual** (technical-manual, 3,624 words)

---

<a id="anrv"></a>
## ANRV — Blind Rehabilitation/VIST

[Back to TOC](#table-of-contents)

The Blind Rehabilitation Service program consists of the following four elements: VA Headquarters, Blind Rehab Centers (BRC), Visual Impairment Service Teams (VIST), and Blind Rehabilitation Outpatient Specialists (BROS).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 35 |
| Date Range | June 1998 → March 2026 |
| Total Pages | 746 |
| Total Words | 124,241 |
| Total Tables | 174 |
| Total Figures | 61 |
| Total Appendices | 22 |
| Update Density | 0.9 docs/yr |
| Knowledge Ratio | 29% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 14 |
| release-note | 11 |
| user-manual | 7 |
| technical-manual | 3 |

### Notable Documents

- **Blind Rehab Version 5 User Manual** (user-manual, 46,693 words)
- **Blind Rehab Version 5.1.9 User Manual** (user-manual, 26,447 words)
- **Blind Rehab Version 5.1.10 User Manual** (user-manual, 26,364 words)
- **Blind Rehab Version 5.1.3 User Manual** (user-manual, 23,998 words)
- **Blind Rehab Version 5.1.2 User Manual** (user-manual, 22,207 words)

---

<a id="ar/ws"></a>
<a id="arws"></a>
## AR/WS — Pharmacy: Automatic Replenishment/Ward Stock

[Back to TOC](#table-of-contents)

The Automatic Replenishment/Ward Stock (AR/WS) package provides a method to track drug distribution and inventory management within a medical center.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 5 |
| Date Range | January 1994 |
| Total Pages | 336 |
| Total Words | 61,670 |
| Total Tables | 2 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **Automatic Replenishment/Ward Stock Version 2.3 User Manual** (user-manual, 47,766 words)
- **Automatic Replenishment/Ward Stock Version 2.3 Technical Manual** (technical-manual, 12,087 words)
- **Automatic Replenishment/Ward Stock Version 2.3 Installation Guide** (installation-guide, 3,039 words)
- **Automatic Replenishment/Ward Stock Version 2.3 Release Notes** (release-note, 880 words)
- **PSGW*2.3*13 Automatic Replenishment/Ward Stock User Manual Change Pages** (user-manual, 629 words)

---

<a id="ascd"></a>
## ASCD — Automated Safety Incident Surveillance Tracking System

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | August 1996 → September 2007 |
| Total Pages | 242 |
| Total Words | 51,442 |
| Total Tables | 37 |
| Total Figures | 0 |
| Total Appendices | 3 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 75% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **ASCD User Manual (PCE)** (user-manual, 30,133 words)
- **ASCD Technical Manual** (technical-manual, 9,524 words)
- **ASCD Release Notes** (release-note, 8,954 words)
- **ASCD User Manual (Scheduling)** (user-manual, 8,070 words)

---

<a id="asu"></a>
## ASU — CPRS: Authorization/Subscription

[Back to TOC](#table-of-contents)

The Authorization/Subscription Utility (ASU) provides a method for identifying who is authorized to perform various actions on clinical documents. These actions include signing, co-signing, and amending.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | July 1997 → May 2010 |
| Total Pages | 84 |
| Total Words | 14,041 |
| Total Tables | 35 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 1 |
| technical-manual | 1 |
| release-note | 1 |

### Notable Documents

- **ASU Clinical Coordinator Manual** (user-manual, 13,182 words)
- **ASU Technical Manual** (technical-manual, 3,889 words)
- **USR*1*33 Show User Class Name in ASU Options** (release-note, 521 words)

---

<a id="bms"></a>
## BMS — Bed Management Solution

[Back to TOC](#table-of-contents)

Bed Management Solution (BMS) is a real-time, user-friendly, web-based Veterans Health Information Systems and Technology Architecture (VistA) and Electronic Health Record Management (EHRM) interface for tracking patient movement, bed status, and bed availability to support daily operations for Veteran access, pandemic response, and emergency management operations.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 31 |
| Date Range | January 2020 → February 2026 |
| Total Pages | 4,912 |
| Total Words | 528,382 |
| Total Tables | 1,775 |
| Total Figures | 37 |
| Total Appendices | 25 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 81% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 14 |
| technical-manual | 11 |
| installation-guide | 6 |

### Notable Documents

- **Bed Management Solution Version 3.8 User Guide** (user-manual, 67,132 words)
- **Bed Management Solution Version 3.7.2 User Guide** (user-manual, 65,236 words)
- **Bed Management Solution Version 3.7 User Guide** (user-manual, 64,965 words)
- **Bed Management Solution Version 3.3 User Guide** (user-manual, 64,368 words)
- **Bed Management Solution Version 2.11 User Guide** (user-manual, 63,868 words)

---

<a id="capri"></a>
## CAPRI — Compensation and Pension Record Interchange

[Back to TOC](#table-of-contents)

CPS National provides allPharmaceutical, Nutritional, Surgical, and Supplemental prescriptions to Veterans, approved dependents, and Indian Health Services (IHS) patients nationally. Over 500K daily prescriptions are processed, and over 350K daily packages are processed.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 68 |
| Date Range | June 2001 → January 2026 |
| Total Pages | 1,862 |
| Total Words | 379,258 |
| Total Tables | 683 |
| Total Figures | 213 |
| Total Appendices | 6 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 26% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 47 |
| supplement | 12 |
| user-manual | 3 |
| technical-manual | 3 |
| installation-guide | 3 |

### Notable Documents

- **CAPRI GUI User Manual (Updated DVBA*2.7*254)** (user-manual, 46,730 words)
- **CAPRI GUI User Manual (Updated DVBA*2.7*250)** (user-manual, 46,703 words)
- **CAPRI GUI User Manual (Updated DVBA*2.7*255)** (user-manual, 46,111 words)
- **DVBA*2.7*175 Release Notes** (release-note, 33,900 words)
- **CAPRI System Administration and Technical Guide (Updated DVBA*2.7*250)** (technical-manual, 27,061 words)

---

<a id="ccra"></a>
## CCRA — Clinical Case Registries Administration

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | August 2018 |
| Total Pages | 88 |
| Total Words | 8,904 |
| Total Tables | 15 |
| Total Figures | 115 |
| Total Appendices | 2 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 1 |

### Notable Documents

- **HealthShare Referral Manager (HSRM) VA Employee User Guide** (user-manual, 13,021 words)

---

<a id="cdsp"></a>
## CDSP — Controlled Drug Subscription Prevention

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | October 2023 → February 2024 |
| Total Pages | 24 |
| Total Words | 7,525 |
| Total Tables | 36 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 4.0 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 4 |

### Notable Documents

- **OR*3*614 Deployment, Installation, Back-out, and Rollback Guide** (installation-guide, 3,237 words)
- **CDSP*1*0 Deployment, Installation, Back-out, and Rollback Guide** (installation-guide, 2,774 words)
- **OR*3*614 Deployment, Installation, Back-out, and Rollback Guide Word Doc** (installation-guide, 2,660 words)
- **CDSP*1*0 Deployment, Installation, Back-out, and Rollback Guide Word Doc** (installation-guide, 2,407 words)

---

<a id="chds"></a>
## CHDS — Consolidated Health Data Storage

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | January 2022 → July 2025 |
| Total Pages | 50 |
| Total Words | 10,027 |
| Total Tables | 22 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 1.1 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 4 |

### Notable Documents

- **CHDR Installation Guide (CHDS*2.2*1)** (installation-guide, 5,338 words)
- **CHDS*2.2*1 DIBR** (installation-guide, 3,136 words)
- **CHDS*2.2*9 DIBR** (installation-guide, 1,064 words)
- **CHDS*2.2*8 DIBR** (installation-guide, 1,057 words)

---

<a id="ciss"></a>
## CISS — Clinical Information Support System

[Back to TOC](#table-of-contents)

As discussed at the VTWG on 03-23-21, this product is no longer used, and the URL will be inactive. This product was a portal to OHRS (1467) application which is also being decommissioned and was replaced by OHRS 2.0 (2675).

Clinical Information Support System (CISS) is a web-based portal application that provides a framework of services for the VA enterprise and supplies an integration point for its partner systems.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | N/A |
| Total Pages | 33 |
| Total Words | 6,602 |
| Total Tables | 11 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 200% |

### Document Types

| Type | Count |
|------|-------|
| supplement | 2 |

### Notable Documents

- **Clinical Information Support System Production Operations Manual  (POM) Version 1.4** (supplement, 7,789 words)
- **Clinical Information Support System Production Operations Manual (POM) Version 1.4** (supplement, 7,789 words)

---

<a id="cprs"></a>
## CPRS — Computerized Patient Record System

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 92 |
| Date Range | April 2003 → February 2026 |
| Total Pages | 4,352 |
| Total Words | 887,620 |
| Total Tables | 554 |
| Total Figures | 47 |
| Total Appendices | 96 |
| Update Density | 3.2 docs/yr |
| Knowledge Ratio | 22% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 41 |
| installation-guide | 31 |
| base-setup | 6 |
| technical-manual | 6 |
| user-manual | 6 |
| quick-ref | 2 |

### Notable Documents

- **CPRS User Manual: GUI Version (Updated OR*3.0*626)** (user-manual, 162,608 words)
- **CPRS User Manual: GUI Version (Updated OR*3.0*499)** (user-manual, 162,608 words)
- **CPRS Technical Manual: List Manager Version (Updated OR*3.0*636)** (technical-manual, 159,881 words)
- **CPRS Technical Manual: GUI Version (Updated OR*3.0*636)** (technical-manual, 155,892 words)
- **CPRS Technical Manual: GUI Version (Updated OR*3.0*499)** (technical-manual, 151,280 words)

---

<a id="cpt"></a>
## CPT — CPT/HCPCS Codes

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | May 1997 |
| Total Pages | 0 |
| Total Words | 6,789 |
| Total Tables | 0 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **CPT Version 6 Technical Manual** (technical-manual, 2,650 words)
- **CPT Version 6 Installation Guide** (installation-guide, 2,217 words)
- **CPT Version 6 User Manual** (user-manual, 1,755 words)
- **CPT Version 6 Release Notes** (release-note, 568 words)

---

<a id="crhd"></a>
## CRHD — Shift Handoff Tool

[Back to TOC](#table-of-contents)

The Shift Handoff Tool standardizes information exchanged between clinicians as they transfer patient care responsibilities incidental to changes of shifts.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | June 2008 → August 2024 |
| Total Pages | 117 |
| Total Words | 17,594 |
| Total Tables | 37 |
| Total Figures | 6 |
| Total Appendices | 0 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 29% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 4 |
| technical-manual | 1 |
| release-note | 1 |
| user-manual | 1 |

### Notable Documents

- **Shift Handoff Tool Version 1 Implementation Guide & Technical Manual** (technical-manual, 5,199 words)
- **Shift Handoff Tool Version 1 User Manual** (user-manual, 5,058 words)
- **CRHD*1*11 Deployment, Installation, Back-Out, and Rollback Guide** (installation-guide, 3,546 words)
- **CRHD*1*7 Install Guide** (installation-guide, 3,475 words)
- **CRHD*1*8 Install Guide** (installation-guide, 3,251 words)

---

<a id="dgbt"></a>
## DGBT — Beneficiary Travel

[Back to TOC](#table-of-contents)

The Beneficiary Travel module provides the ability to perform the functions involved in issuing beneficiary travel pay. Travel reimbursement is provided to specified categories of eligible veterans. It is also provided to non-employee attendants who are eligible for such reimbursement. These attendants will be issued travel pay under the veteran's name.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | April 2002 → February 2024 |
| Total Pages | 189 |
| Total Words | 36,723 |
| Total Tables | 20 |
| Total Figures | 0 |
| Total Appendices | 4 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 38% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 3 |
| user-manual | 2 |
| installation-guide | 2 |
| technical-manual | 1 |

### Notable Documents

- **Beneficiary Travel Version 1 Dashboard Installation Guide** (installation-guide, 17,463 words)
- **Beneficiary Travel Version 1 User Manual (Updated with DGBT*1*41)** (user-manual, 10,331 words)
- **Beneficiary Travel Version 1 Technical Manual (Updated with DGBT*1*41)** (technical-manual, 5,287 words)
- **Beneficiary Travel  Version 1 Dashboard User Manual** (user-manual, 4,754 words)
- **DGBT*1*20 Release Notes** (release-note, 2,275 words)

---

<a id="dgj"></a>
## DGJ — Incomplete Records Tracking

[Back to TOC](#table-of-contents)

The Incomplete Records Tracking (IRT) package provides the medical center the ability to monitor incomplete records. Interim summaries, discharge summaries, and both inpatient and outpatient operation reports are tracked. Records may be incomplete or deficient for one or more of the following reasons - not dictated, not transcribed, not signed, or not reviewed.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | April 2002 |
| Total Pages | 543 |
| Total Words | 14,267 |
| Total Tables | 11 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Incomplete Records Tracking (IRT) Version 1 Technical Manual** (technical-manual, 10,060 words)
- **Incomplete Records Tracking (IRT) Version 1 User Manual** (user-manual, 4,298 words)
- **Incomplete Records Tracking (IRT) Version 1 Installation Guide** (installation-guide, 1,443 words)

---

<a id="di"></a>
## DI — VA FileMan

[Back to TOC](#table-of-contents)

VA FileMan is the VistA database management system (DBMS). It runs in any American National Standards Institute (ANSI) environment. The majority of VHA clinical data is stored in VA FileMan files and is retrieved and accessed through VA FileMan Application Program Interfaces (API) and user interfaces.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 11 |
| Date Range | June 1996 → July 2025 |
| Total Pages | 1,709 |
| Total Words | 348,231 |
| Total Tables | 523 |
| Total Figures | 1,048 |
| Total Appendices | 8 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 82% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| base-dev | 2 |
| quick-ref | 2 |
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |
| base-security | 1 |

### Notable Documents

- **FM 22.2 Developer's Guide** (base-dev, 184,526 words)
- **FM 22.2 Advanced User Manual** (user-manual, 98,316 words)
- **FM 22.2 User Manual** (user-manual, 41,579 words)
- **FM Key and Index Tutorial** (quick-ref, 35,584 words)
- **FM ScreenMan Tutorial for Developers** (base-dev, 20,711 words)

---

<a id="drm+"></a>
<a id="drm"></a>
## DRM+ — Drug Accountability

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 12 |
| Date Range | April 1989 |
| Total Pages | 0 |
| Total Words | 14,902 |
| Total Tables | 80 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 12.0 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 8 |
| release-note | 4 |

### Notable Documents

- **DENT*1.2*93 DRM Plus Deployment, Installation, Backout and Rollback Guide** (installation-guide, 4,104 words)
- **DENT*1.2*91 DRM Plus Deployment, Installation, Backout and Rollback Guide** (installation-guide, 4,087 words)
- **DENT*1.2*92 DRM Plus Deployment, Installation, Backout and Rollback Guide** (installation-guide, 3,922 words)
- **DENT*1.2*90 DRM Plus Deployment, Installation, Backout and Rollback Guide** (installation-guide, 3,089 words)
- **DENT*1.2*91 DRM Plus Installation Guide** (installation-guide, 1,846 words)

---

<a id="dvba"></a>
## DVBA — Compensation and Pension

[Back to TOC](#table-of-contents)

The Automated Medical Information Exchange (AMIE) module facilitates the electronic interchange of veteran information between Veteran Benefits Administration (VBA) Regional Offices (ROs) and VA medical facilities.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | April 1995 → July 2022 |
| Total Pages | 188 |
| Total Words | 48,458 |
| Total Tables | 12 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 62% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 2 |
| user-manual | 2 |
| technical-manual | 2 |
| release-note | 1 |
| supplement | 1 |

### Notable Documents

- **AMIE Version 2.7 Medical Admin Service User Manual (UM)** (user-manual, 12,319 words)
- **AMIE Version 2.7 Regional Office User Manual** (user-manual, 9,927 words)
- **AMIE Version 2.7 Installation Guide 2019** (installation-guide, 6,304 words)
- **AMIE Version 2.7 Installation Guide 1995** (installation-guide, 6,284 words)
- **AMIE Version 2.7 Technical Manual (TM)** (technical-manual, 5,663 words)

---

<a id="eas"></a>
## EAS — Enrollment Application System

[Back to TOC](#table-of-contents)

Enrollment Application System (EAS) facilitates the processing of the 10-10EZ Application for Health Benefits, which has been transmitted to the VHA site from the On-Line 10-10EZ web-based software.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 11 |
| Date Range | March 2001 → September 2021 |
| Total Pages | 264 |
| Total Words | 51,851 |
| Total Tables | 64 |
| Total Figures | 19 |
| Total Appendices | 27 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 45% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 3 |
| installation-guide | 3 |
| user-manual | 3 |
| technical-manual | 2 |

### Notable Documents

- **EAS Version 1 User Manual** (user-manual, 19,975 words)
- **EAS*1*106 LOCAL Signed Means Test Application (ROSSIO 22) User Manual** (user-manual, 12,845 words)
- **EAS Version 1.1 Long Term Care Copayment User Manual** (user-manual, 10,526 words)
- **EAS Version 1 Health Connect / ESR-MVR Deployment, Installation, Back-Out, and Rollback Guide** (installation-guide, 5,546 words)
- **EAS*1*106 LOCAL Signed Means Test Application (ROSSIO 22) Technical Manual** (technical-manual, 4,263 words)

---

<a id="ec"></a>
## EC — Event Capture System

[Back to TOC](#table-of-contents)

The Event Capture System (ECS) provides a mechanism to track and account for procedures and delivered services that are not handled in any other VistA package. The procedures and services tracked through Event Capture are associated with (1) the patient to whom they were delivered, (2) the provider requesting the service or procedure and (3) the Decision Support System (DSS) Unit responsible for delivering the service.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | September 2022 → May 2025 |
| Total Pages | 277 |
| Total Words | 41,606 |
| Total Tables | 23 |
| Total Figures | 252 |
| Total Appendices | 10 |
| Update Density | 1.9 docs/yr |
| Knowledge Ratio | 29% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 5 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Event Capture Version 2.0 GUI User Guide (Updated EC*2*170)** (user-manual, 38,335 words)
- **Event Capture Version 2.0 GUI Technical Manual (Updated EC*2*170)** (technical-manual, 10,837 words)
- **ECS DIBRG (EC*2.0*159)** (installation-guide, 5,261 words)
- **ECS DIBRG (EC*2.0*161)** (installation-guide, 5,168 words)
- **ECS DIBRG (EC*2.0*158)** (installation-guide, 5,158 words)

---

<a id="ecme"></a>
## ECME — Electronic Claims Management Engine

[Back to TOC](#table-of-contents)

The Electronic Claims Management Engine (ECME) package provides the ability to create and distribute electronic Outpatient Pharmacy claims to insurance companies on behalf of VHA Pharmacy prescription beneficiaries in a real-time environment. The application does not impact first party co-payments and minimizes the impact on legacy pharmacy workflow.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 35 |
| Date Range | October 2004 → December 2025 |
| Total Pages | 655 |
| Total Words | 161,454 |
| Total Tables | 217 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 1.6 docs/yr |
| Knowledge Ratio | 6% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 23 |
| release-note | 10 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **ECME User Manual** (user-manual, 49,152 words)
- **ECME Technical Manual/Security Guide** (technical-manual, 16,770 words)
- **BPS Version 1 (Dormant Release) Installation Guide** (installation-guide, 8,966 words)
- **BPS*1*10 ECME ePharmacy Phase V Release Notes** (release-note, 8,083 words)
- **BPS*1*1 ECME HIPAA NCPDP Installation Guide** (installation-guide, 6,372 words)

---

<a id="edis"></a>
## EDIS — Emergency Department Integration Software

[Back to TOC](#table-of-contents)

Emergency Department Integration Software (EDIS) incorporates several Web-based views that extend the current Computerized Patient Record System (CPRS) to help healthcare professionals track and manage the flow of patient care in the emergency-department setting.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 21 |
| Date Range | September 2010 → April 2025 |
| Total Pages | 1,376 |
| Total Words | 180,090 |
| Total Tables | 411 |
| Total Figures | 276 |
| Total Appendices | 2 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 62% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 7 |
| technical-manual | 6 |
| user-manual | 5 |
| supplement | 2 |
| release-note | 1 |

### Notable Documents

- **Emergency Dept Integration Software (EDIS) Version 1.0 User Guide** (user-manual, 26,564 words)
- **Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 User Guide** (user-manual, 24,838 words)
- **Emergency Dept Integration Software (EDIS) Version 2.1.1 Increment 3 User Guide** (user-manual, 24,834 words)
- **Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Technical Manual** (technical-manual, 21,665 words)
- **Emergency Dept Integration Software (EDIS) Version 2.1.1 Increment 3 Technical Manual** (technical-manual, 21,111 words)

---

<a id="efr"></a>
## EFR — Electronic Fee Basis Remote

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | August 2013 |
| Total Pages | 281 |
| Total Words | 22,015 |
| Total Tables | 198 |
| Total Figures | 0 |
| Total Appendices | 7 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 1 |

### Notable Documents

- **Embedded Fragments Version 1 User Manual** (user-manual, 55,516 words)

---

<a id="ehm"></a>
## EHM — Event Monitoring

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | March 2026 |
| Total Pages | 140 |
| Total Words | 30,758 |
| Total Tables | 46 |
| Total Figures | 2 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Electronic Health Modernization Technical Manual** (technical-manual, 20,007 words)
- **Electronic Health Modernization User Manual** (user-manual, 18,130 words)

---

<a id="en"></a>
## EN — Engineering

[Back to TOC](#table-of-contents)

Engineering, also known as Automated Engineering Management System/Medical Equipment Reporting System (AEMS/MERS), facilitates the management of information needed to effectively discharge key operational responsibilities normally assigned to VA engineering organizations, such as Work Orders, Equipment Management, Program Management and Space/Facility Management.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | August 1993 → October 2024 |
| Total Pages | 419 |
| Total Words | 163,980 |
| Total Tables | 325 |
| Total Figures | 0 |
| Total Appendices | 3 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 3 |
| installation-guide | 2 |
| user-manual | 1 |

### Notable Documents

- **EN Version 7 User Manual** (user-manual, 112,991 words)
- **EN Version 7 RTLS Enhancement Technical Manual** (technical-manual, 36,257 words)
- **EN Version 7 Technical Manual** (technical-manual, 35,596 words)
- **EN Version 7 RTLS Enhancement Interfaces Manual** (technical-manual, 9,459 words)
- **EN Version 7 RTLS Enhancement Installation Guide** (installation-guide, 7,427 words)

---

<a id="epi"></a>
## EPI — Emerging Pathogens Initiative

[Back to TOC](#table-of-contents)

VTWG on 4/20/2021, per request component of VistA - Laboratory (VistA-LAB) - #1381,Assists in tracking infectious diseases. It establishes a SAS data set which is used by the Office of Infectious Diseases (OID).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | July 2014 → September 2015 |
| Total Pages | 848 |
| Total Words | 147,503 |
| Total Tables | 168 |
| Total Figures | 10 |
| Total Appendices | 14 |
| Update Density | 2.5 docs/yr |
| Knowledge Ratio | 57% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 4 |
| release-note | 2 |
| installation-guide | 1 |

### Notable Documents

- **Laboratory Version 5.2 EPI Roll Up Modifications Technical and User Manual** (user-manual, 77,008 words)
- **Laboratory Version 5.2 Hepatitis C and EPI Technical and User Guide** (user-manual, 31,420 words)
- **Laboratory Version 5.2 EPI Search/Extract Technical and User Guide** (user-manual, 28,766 words)
- **Laboratory Version 5.2 EPI Technical and User Guide** (user-manual, 22,436 words)
- **LR*5.2*442 ICD-10 PTF Modifications Installation Guide** (installation-guide, 9,825 words)

---

<a id="epsi"></a>
## EPSI — Enterprise Precision Scanning and Indexing

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | April 2023 → February 2026 |
| Total Pages | 15 |
| Total Words | 1,983 |
| Total Tables | 11 |
| Total Figures | 2 |
| Total Appendices | 5 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 2 |
| user-manual | 1 |

### Notable Documents

- **Enterprise Precision Scanning and Indexing (EPSI) User Guide** (user-manual, 18,740 words)
- **Enterprise Precision Scanning and Indexing (EPSI) Deployment, Installation, Back-Out, and Rollback Guide v1.2.5** (installation-guide, 3,193 words)
- **Enterprise Precision Scanning and Indexing (EPSI) Deployment, Installation, Back-Out, and Rollback Guide v1.3.0** (installation-guide, 3,193 words)

---

<a id="ets"></a>
## ETS — Education Tracking System

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | June 2017 |
| Total Pages | 33 |
| Total Words | 6,446 |
| Total Tables | 6 |
| Total Figures | 30 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |

### Notable Documents

- **ETS*1*1 Technical Manual/Security Guide** (technical-manual, 6,954 words)

---

<a id="fb"></a>
## FB — Fee Basis

[Back to TOC](#table-of-contents)

The Fee Basis package supports VHA’s Fee for Service program, which is care authorized for veterans who are legally eligible and in need of care that cannot feasibly be provided by a VA facility.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 27 |
| Date Range | January 1995 → December 2025 |
| Total Pages | 446 |
| Total Words | 298,614 |
| Total Tables | 238 |
| Total Figures | 0 |
| Total Appendices | 32 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 22% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 13 |
| installation-guide | 8 |
| user-manual | 4 |
| base-security | 1 |
| technical-manual | 1 |

### Notable Documents

- **Fee Basis Version 3.5 User Manual (1995)** (user-manual, 141,203 words)
- **Fee Basis Version 3.5 User Manual** (user-manual, 128,388 words)
- **Fee Basis Version 3.5 Technical Manual/Security Guide (1995)** (technical-manual, 36,741 words)
- **Fee Basis Annual Patch Manual** (user-manual, 8,645 words)
- **FB*3.5*154 Release Notes** (release-note, 6,423 words)

---

<a id="ffp"></a>
## FFP — Fugitive Felon Program

[Back to TOC](#table-of-contents)

The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the VA Austin Information Technology Center (AITC). The FIM is an 18-item, 7-level functional assessment designed to evaluate the amount of assistance required by a person with a disability to perform basic life activities safely and effectively.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | September 2021 |
| Total Pages | 14 |
| Total Words | 2,460 |
| Total Tables | 2 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 1 |

### Notable Documents

- **Fugitive Felon Program (FFP) User Manual** (user-manual, 2,985 words)

---

<a id="fh"></a>
## FH — Dietetics

[Back to TOC](#table-of-contents)

The Nutrition and Food Service (N&FS) software integrates the automation of many Clinical Nutrition, Food Management, and Management Reports functions. The Clinical N&FS activities of Nutrition Screening, Nutrition Assessment, Diet Order Entry, Tube Feeding and Supplemental Feeding Orders, Patient Food Preferences, Specific Diet Pattern Calculations,Nutrient Analysis of meals, Consult Reporting, Encounter Tracking, and Quality Care Monitoring are all available in this program.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | February 2005 → March 2019 |
| Total Pages | 1,093 |
| Total Words | 125,649 |
| Total Tables | 356 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 38% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 3 |
| user-manual | 2 |
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **Nutrition & Food Services Version 5.5 Manager/ADPAC Guide (Revised Sept 2007)** (user-manual, 91,798 words)
- **Nutrition & Food Services Version 5.5 User Manual (Revised Sept 2007)** (user-manual, 77,789 words)
- **Nutrition & Food Services Version 5.5 Technical Manual and Security Guide** (technical-manual, 13,112 words)
- **Nutrition & Food Services Version 5.5 Installation/Implementation Guide** (installation-guide, 6,342 words)
- **FH*5.5*43 User Manual Change Pages** (change-page, 1,670 words)

---

<a id="fim"></a>
## FIM — Functional Independence Measures

[Back to TOC](#table-of-contents)

The Functional Independence Measures (FIM) Version 1.0 provides an integration of FIM assessments into the Computerized Patient Record System (CPRS) and into the Functional Status and Outcomes Database (FSOD) at the VA Austin Information Technology Center (AITC). The FIM is an 18-item, 7-level functional assessment designed to evaluate the amount of assistance required by a person with a disability to perform basic life activities safely and effectively.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | May 2003 |
| Total Pages | 152 |
| Total Words | 12,977 |
| Total Tables | 159 |
| Total Figures | 0 |
| Total Appendices | 5 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Functional Independence Measurement (FIM) Version 1 User Manual** (user-manual, 11,718 words)
- **Functional Independence Measurement (FIM) Version 1 Technical and Security Guide** (technical-manual, 11,496 words)
- **Functional Independence Measurement (FIM) Version 1 Installation Guide** (installation-guide, 3,427 words)

---

<a id="fmdc"></a>
## FMDC — FileMan Delphi Components

[Back to TOC](#table-of-contents)

VA FileMVA FileMan is Veterans Health Information Systems and Technology Architecture s (VistA) database management system (DBMS). It runs in any American National Standards Institute (ANSI) environment. The majority of Veterans Health Administration (VHA) clinical data is stored in VA FileMan files and is retrieved and accessed through VA FileMan Application Programmer Interfaces (API) and user interfaces.It runs in any American National Standards Institute (ANSI) environment.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | March 1998 → July 1999 |
| Total Pages | 24 |
| Total Words | 11,256 |
| Total Tables | 36 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.5 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| quick-ref | 1 |
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **FMDC Getting Started Guide** (quick-ref, 9,502 words)
- **FMDC Technical Manual and Security Guide** (technical-manual, 2,549 words)
- **FMDC Installation Guide** (installation-guide, 2,504 words)
- **FMDC Patch FMDC*1.0*2 README file (includes Delphi 5 instructions)** (release-note, 1,270 words)

---

<a id="gen"></a>
## GEN — Generic Code Sheet

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 5 |
| Date Range | August 1992 → March 1995 |
| Total Pages | 164 |
| Total Words | 24,003 |
| Total Tables | 211 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.8 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| base-security | 1 |
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **GCS Version 2 User Manual** (user-manual, 20,622 words)
- **GCS Version 2 Technical Manual** (technical-manual, 3,106 words)
- **GCS Version 2 Installation Guide** (installation-guide, 2,511 words)
- **GCS Version 2 Package Security Guide** (base-security, 977 words)
- **GCS Version 2 Release Notes** (release-note, 427 words)

---

<a id="gmpl"></a>
## GMPL — Problem List

[Back to TOC](#table-of-contents)

The Problem List application is used to document and track a patient’s problems. It provides the clinician with a current and historical view of patient's health care problems and allows each identified problem to be traced in terms oftreatment, test results, and outcome.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | September 1994 → April 2025 |
| Total Pages | 197 |
| Total Words | 17,638 |
| Total Tables | 9 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Problem List User Manual Version 2 (GMPL*2*60)** (user-manual, 19,578 words)
- **Problem List Technical Manual Version 2 (updated with GMPL*2*49)** (technical-manual, 13,870 words)
- **GMPL*2*49 and OR*3*429 Problem Selection List Enhancements Deployment, Installation, Back-Out, and Rollback Guide** (installation-guide, 5,390 words)
- **GMPL*2*49 and OR*3*429 Problem Selection List Enhancements Release Notes** (release-note, 528 words)

---

<a id="gmra"></a>
## GMRA — Adverse Reaction Tracking

[Back to TOC](#table-of-contents)

The Adverse Reaction Tracking (ART) program provides a common and consistent data structure for adverse reaction data. This module has options for data entry and validation, supported references for use by external software modules, and the ability to report adverse drug reaction data to the Food and Drug Administration (FDA).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | August 2005 → January 2024 |
| Total Pages | 326 |
| Total Words | 85,729 |
| Total Tables | 124 |
| Total Figures | 16 |
| Total Appendices | 0 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 25% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 4 |
| installation-guide | 2 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Adverse Reaction Tracking User Manual** (user-manual, 46,794 words)
- **Adverse Reaction Tracking Technical Manual** (technical-manual, 25,439 words)
- **GMRA*4*26 Release Notes** (release-note, 8,689 words)
- **Adverse Reaction Tracking Installation Manual** (installation-guide, 3,682 words)
- **GMRA*4*20 Release Notes** (release-note, 3,491 words)

---

<a id="gmrc"></a>
## GMRC — Consult / Request Tracking

[Back to TOC](#table-of-contents)

The Consult/Request Tracking package provides an efficient way for clinicians to order consultations and procedures from other providers or services within the VHA system, at their own facility or another facility. It also provides a framework for tracking consults and procedures and reporting the results. It uses a patient's computerized patient record to store information about consult and procedure requests and results.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 28 |
| Date Range | April 2002 → January 2026 |
| Total Pages | 1,506 |
| Total Words | 242,460 |
| Total Tables | 309 |
| Total Figures | 958 |
| Total Appendices | 18 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 54% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 15 |
| user-manual | 9 |
| technical-manual | 2 |
| supplement | 2 |
| release-note | 1 |
| base-impl | 1 |
| base-dev | 1 |

### Notable Documents

- **Consult/Request Tracking Technical Manual (GMRC*3.0*189)** (technical-manual, 48,921 words)
- **Consult Toolbox v2.0 User Guide** (user-manual, 44,778 words)
- **Consult Toolbox User Guide** (user-manual, 33,506 words)
- **Consult Toolbox User Guide Version 1.9.0076** (user-manual, 33,506 words)
- **Consult/Request Tracking User Manual (GMRC*3.0*206)** (user-manual, 29,445 words)

---

<a id="gmrv"></a>
## GMRV — Vitals / Measurements

[Back to TOC](#table-of-contents)

The Vitals/Measurements application is designed to store, in the patient's electronic health record, all vital signs and various measurements associated with a patient's hospital stay or outpatient clinic visit. Data entered can be accessed by several VistA (Veterans Health Information Systems and Technology Architecture) applications (e.g., Health Summary) that interface with the Vitals/Measurements application.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 19 |
| Date Range | October 2002 → January 2021 |
| Total Pages | 135 |
| Total Words | 91,756 |
| Total Tables | 93 |
| Total Figures | 8 |
| Total Appendices | 11 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 37% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 8 |
| release-note | 4 |
| technical-manual | 3 |
| user-manual | 3 |
| base-hl7 | 1 |

### Notable Documents

- **GMRV*5*23 Technical Manual change pages** (technical-manual, 18,101 words)
- **Vitals Version 5 Technical Manual and Package Security Guide** (technical-manual, 17,942 words)
- **Vitals Version 5 User Manual** (user-manual, 16,578 words)
- **GMRV*5*23 User Manual change pages** (user-manual, 13,144 words)
- **GMRV*5*22 Technical Manual change pages** (technical-manual, 7,858 words)

---

<a id="gmts"></a>
## GMTS — Health Summary

[Back to TOC](#table-of-contents)

A Health Summary is a clinically oriented and structured report that extracts many kinds of data from VistA and displays it in a defined and standard format.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 5 |
| Date Range | December 2019 → November 2023 |
| Total Pages | 517 |
| Total Words | 118,077 |
| Total Tables | 79 |
| Total Figures | 0 |
| Total Appendices | 16 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 80% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 2 |
| user-manual | 2 |
| installation-guide | 1 |

### Notable Documents

- **Health Summary Version 2.7 User Manual** (user-manual, 42,294 words)
- **GMTS*2.7*133 Health Summary - User Manual** (user-manual, 41,079 words)
- **Health Summary Version 2.7 Technical Manual** (technical-manual, 20,339 words)
- **GMTS*2.7*133 Health Summary - Technical Manual** (technical-manual, 19,990 words)
- **Health Summary Version 2.7 Installation Guide** (installation-guide, 8,869 words)

---

<a id="hbpc"></a>
## HBPC — Home Based Primary Care

[Back to TOC](#table-of-contents)

The Home-Based Primary Care (HBPC) module is designed to allow for the local entry and verification and data management of HBPC patient-related data. HBPC was previously referred to as Hospital Based Home Care (HBHC).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | November 1993 → August 2021 |
| Total Pages | 103 |
| Total Words | 64,016 |
| Total Tables | 70 |
| Total Figures | 25 |
| Total Appendices | 0 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 2 |
| installation-guide | 2 |
| base-security | 2 |
| technical-manual | 2 |
| user-manual | 2 |

### Notable Documents

- **HBPC User Manual** (user-manual, 29,711 words)
- **Hospital Based Primary Care (former HBHC) Version 1 User Manual** (user-manual, 27,233 words)
- **HBH*1*32 HBPC Deployment, Installation, Back-out, and Rollback Guide** (installation-guide, 7,414 words)
- **HBPC Technical Manual** (technical-manual, 6,588 words)
- **Hospital Based Primary Care (former HBHC) Version 1 Technical Manual** (technical-manual, 6,498 words)

---

<a id="hinq"></a>
## HINQ — Hospital Inquiry

[Back to TOC](#table-of-contents)

INACTIVE per 5/17/2022 VTWG. VistA - Hospital Inquiry System (HIS) is no longer an active VistA package and can be marked inactive. The functionality was replaced by VA Profile using the Veterans Health Administration Enrollment System (VES) VASI #1231 and Veterans Benefits Management System (VBMS) VASI #1728

VistA - Hospital Inquiry System (HINQ) is a request that is sent to the VBA (Veterans Benefits Administration) from the authorized staff at VA Medical Centers (VAMCs) for information perta...

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 5 |
| Date Range | March 1992 → November 2005 |
| Total Pages | 141 |
| Total Words | 22,268 |
| Total Tables | 22 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |
| installation-guide | 1 |
| release-note | 1 |
| supplement | 1 |

### Notable Documents

- **DVB Version 4 User Manual (Revised 3/27/12)** (user-manual, 12,493 words)
- **DVB Version 4 Technical Manual** (technical-manual, 10,306 words)
- **DVB*4*49 Training Guide** (supplement, 4,097 words)
- **DVB*4*49 Release Notes** (release-note, 2,082 words)
- **DVB*4*49 Installation Guide** (installation-guide, 1,162 words)

---

<a id="hl7"></a>
## HL7 — Health Level Seven Infrastructure

[Back to TOC](#table-of-contents)

Health Level Seven (HL7) is an American National Standards Institute (ANSI) standard messaging protocol that specifies the set of transactions and encoding rules for electronic data exchange between health care computer systems.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 16 |
| Date Range | October 1995 → May 2006 |
| Total Pages | 647 |
| Total Words | 221,090 |
| Total Tables | 779 |
| Total Figures | 25 |
| Total Appendices | 23 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 81% |

### Document Types

| Type | Count |
|------|-------|
| supplement | 5 |
| base-hl7 | 4 |
| installation-guide | 2 |
| technical-manual | 2 |
| base-security | 1 |
| release-note | 1 |
| user-manual | 1 |

### Notable Documents

- **HL7 V. 1.6*56 Site Manager Developer Manual** (base-hl7, 60,754 words)
- **HL7 V. 1.6*161 Site Manager Developer Manual** (base-hl7, 59,952 words)
- **HL7 HL*1.6*126 Technical Manual** (technical-manual, 59,658 words)
- **HL7 HL*1.6 HLO VMS Developer Manual** (base-hl7, 41,389 words)
- **HL7 HL*1.6 HLO System Manager Manual** (base-hl7, 23,105 words)

---

<a id="ib"></a>
## IB — Integrated Billing

[Back to TOC](#table-of-contents)

The Integrated Billing (IB) software provides all the features necessary to create first party (patient) and third party (insurance carriers/Medicare) bills.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 152 |
| Date Range | February 1994 → March 2026 |
| Total Pages | 9,588 |
| Total Words | 545,913 |
| Total Tables | 809 |
| Total Figures | 19 |
| Total Appendices | 25 |
| Update Density | 4.4 docs/yr |
| Knowledge Ratio | 8% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 98 |
| release-note | 42 |
| user-manual | 9 |
| technical-manual | 2 |
| change-page | 1 |
| base-security | 1 |

### Notable Documents

- **IB*2 Integrated Billing Version 2 User Manual** (user-manual, 101,872 words)
- **IB*2 Integrated Billing Version 2 Technical Manual** (technical-manual, 68,918 words)
- **IB*2 EDI User Guide** (user-manual, 59,499 words)
- **IB*2 Electronic Insurance Verification (eIV) and Interfacility Insurance Update (IIU) Technical Manual/Security Guide** (technical-manual, 28,522 words)
- **IB*2 Electronic Insurance Verification (EIV) and Interfacility Insurance Update (IIU) User Guide** (user-manual, 28,522 words)

---

<a id="ibd"></a>
## IBD — Integrated Billing EDI (Electronic Data Interchange)

[Back to TOC](#table-of-contents)

The Automated Information Collection System (AICS) software supports outpatient clinical efforts through the creation and printing of encounter forms that display relevant clinical information and provides for the entry of clinical encounter data for local and national needs.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | April 1997 → April 2014 |
| Total Pages | 214 |
| Total Words | 54,052 |
| Total Tables | 143 |
| Total Figures | 0 |
| Total Appendices | 13 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 43% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 2 |
| base-impl | 1 |
| unknown | 1 |
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **AICS Version 3 User Manual** (user-manual, 26,680 words)
- **AICS Implementation Guide** (base-impl, 10,731 words)
- **AICS Version 3 Installation Guide** (installation-guide, 8,260 words)
- **AICS Version 3 Release Notes** (release-note, 8,027 words)
- **IBD*3.0*63 Release Notes** (release-note, 6,007 words)

---

<a id="ifr"></a>
## IFR — Incomplete Records Tracking

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | June 2001 |
| Total Pages | 0 |
| Total Words | 29,050 |
| Total Tables | 181 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| supplement | 1 |

### Notable Documents

- **IFR XU*8*206-416 Supplement to Patch Description** (supplement, 48,865 words)

---

<a id="ivm"></a>
## IVM — Income Verification Match

[Back to TOC](#table-of-contents)

The Income Verification Match (IVM) module is designed to extract patient-reported data and transmit it to the Enrollment System (ES). IVM facilitates bidirectional communication between the VistA systems and the Enrollment System. IVM allows the Veterans Health Administration (VHA) to accurately assess a patient’s eligibility for health care and other benefits to which they are entitled.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | October 1994 → February 2019 |
| Total Pages | 212 |
| Total Words | 25,325 |
| Total Tables | 162 |
| Total Figures | 0 |
| Total Appendices | 6 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 25% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 5 |
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **IVM Version 2 Technical Manual** (technical-manual, 41,686 words)
- **IVM Version 2 User Manual** (user-manual, 8,954 words)
- **IVM Version 2 Release Notes** (release-note, 5,992 words)
- **IVM Version 2 Installation Guide** (installation-guide, 2,782 words)
- **IVM*2*174 Release Notes** (release-note, 1,984 words)

---

<a id="ivmb"></a>
## IVMB — Income Verification Match Billing

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 17 |
| Date Range | September 1999 → September 2006 |
| Total Pages | 156 |
| Total Words | 27,169 |
| Total Tables | 146 |
| Total Figures | 0 |
| Total Appendices | 6 |
| Update Density | 1.6 docs/yr |
| Knowledge Ratio | 35% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 7 |
| installation-guide | 4 |
| technical-manual | 4 |
| user-manual | 2 |

### Notable Documents

- **IVMB*2*395 Means Test Sharing (MTS) Manual** (user-manual, 15,848 words)
- **IVMB*2*453 Priority Letters Phase 1 Technical Manual** (technical-manual, 5,856 words)
- **IVMB*2*601 Error Processing Phase 2 Technical Manual** (technical-manual, 3,340 words)
- **IVMB*2*686 Geographic Means Test (GMT) Release Notes** (release-note, 3,313 words)
- **IVMB*2*463 Error Processing Phase 1 Installation Guide** (installation-guide, 3,201 words)

---

<a id="kaajee"></a>
## KAAJEE — Kernel Authentication & Authorization for J2EE

[Back to TOC](#table-of-contents)

Kernel Authentication & Authorization for Java 2 Enterprise Edition (KAAJEE) addresses the Authentication & Authorization (AA) needs of VistA Web-based applications in the J2EE environment.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 32 |
| Date Range | April 2009 → May 2024 |
| Total Pages | 93 |
| Total Words | 248,712 |
| Total Tables | 1,526 |
| Total Figures | 9 |
| Total Appendices | 23 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 6% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 20 |
| release-note | 10 |
| base-setup | 2 |

### Notable Documents

- **KAAJEE 1.2.0 Deployment Guide (Weblogic 10.3.6)** (installation-guide, 38,618 words)
- **KAAJEE Classic Deployment Guide 1.2 (WebLogic 10.3.6 and WebLogic 12.1)** (installation-guide, 38,374 words)
- **KAAJEE 1.1.0 Deployment Guide (WebLogic 9.2 and higher)** (installation-guide, 37,913 words)
- **KAAJEE Classic Deploy Guide** (installation-guide, 36,782 words)
- **KAAJEE SSOWAP Deployment Guide (8.0*791)** (installation-guide, 34,313 words)

---

<a id="kmpd"></a>
## KMPD — Capacity Management Tools

[Back to TOC](#table-of-contents)

The Capacity Management (CM) Tools software is a fully automated support tool developed by Capacity Planning (CP) Service. CM Tools are designed for Information Resource Management (IRM) and system administrators responsible for the capacity planning functions at their site, as well as (VistA) software developers.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | September 2012 → December 2015 |
| Total Pages | 116 |
| Total Words | 29,620 |
| Total Tables | 69 |
| Total Figures | 61 |
| Total Appendices | 0 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Capacity Management Tools Version 3 User Manual** (user-manual, 20,911 words)
- **Capacity Management Tools Version 3 Technical Manual** (technical-manual, 12,527 words)
- **Capacity Management Tools Version 3 Installation Guide** (installation-guide, 7,330 words)

---

<a id="kmpr"></a>
## KMPR — Resource Usage Monitor

[Back to TOC](#table-of-contents)

The Resource Usage Monitor (RUM) software is intended for use by staff responsible for the capacity planning functions at their respective facilities. RUM software provides Veterans Health Information Systems and Technology Architecture (VistA) option workload information. The Resource Usage Monitor (RUM) is a component of Capacity Management's suite of monitoring tools.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | June 2003 |
| Total Pages | 0 |
| Total Words | 13,738 |
| Total Tables | 104 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **KMPR Version 2 Technical Manual** (technical-manual, 9,508 words)
- **KMPR Version 2 User Manual** (user-manual, 6,679 words)
- **KMPR Version 2 Installation Guide** (installation-guide, 6,481 words)

---

<a id="kmps"></a>
## KMPS — Statistical Analysis of Global Growth

[Back to TOC](#table-of-contents)

The Veterans Health Administration (VHA) developed the Statistical Analysis of Global Growth (SAGG) software to obtain more accurate information regarding the current and future Veterans Health Information Systems and Technology Architecture (VistA) database growth rates at the VA Medical Centers (VAMCs).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | December 2015 |
| Total Pages | 25 |
| Total Words | 7,049 |
| Total Tables | 12 |
| Total Figures | 5 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **SAGG Version 2 Technical Manual** (technical-manual, 5,359 words)
- **SAGG Version 2 User Manual** (user-manual, 4,508 words)

---

<a id="kmpv"></a>
## KMPV — Kernel Management Platform — Vertical

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | July 2020 → January 2024 |
| Total Pages | 83 |
| Total Words | 17,230 |
| Total Tables | 35 |
| Total Figures | 34 |
| Total Appendices | 1 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **VSM Version 4 Technical Manual** (technical-manual, 13,999 words)
- **VSM Version 4 User Manual** (user-manual, 6,290 words)
- **VSM Installation, Back-out, and Rollback Guide (DIBRG)** (installation-guide, 5,203 words)

---

<a id="la"></a>
## LA — Laboratory LEDI (LabLinks)

[Back to TOC](#table-of-contents)

Moved to System Component/Application for 1381: VistA - Laboratory

The Laboratory Universal Interface (UI) is designed to make the process of interfacing automated instruments easier, faster, and more reliable.

The purpose of the VistA Laboratory Universal Interface (UI) Health Level (HL) v1.6 Upgrade Patch LA*5.2*66 software release is to improve the transmission of laboratory test results from clinical analyzers to the VistA system.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 15 |
| Date Range | October 1995 → April 2017 |
| Total Pages | 349 |
| Total Words | 72,811 |
| Total Tables | 261 |
| Total Figures | 22 |
| Total Appendices | 5 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 7 |
| base-hl7 | 4 |
| user-manual | 2 |
| base-impl | 2 |
| technical-manual | 1 |

### Notable Documents

- **LA*5.2*17/LR*5.2*65 Laboratory: Universal Interface Installation Guide** (installation-guide, 17,688 words)
- **Laboratory: Universal Interface Micro Interface Version 1 Lab UI HL7 Specifications** (base-hl7, 15,855 words)
- **Laboratory: Universal Interface HL V1.6 Upgrade Interface Specifications Document** (base-hl7, 11,246 words)
- **Laboratory: Universal Interface AutoRelease  Version 1 User Guide** (user-manual, 8,099 words)
- **LA*5.2*66 Laboratory: Universal Interface HL V1.6 Upgrade Installation and User Guide** (installation-guide, 7,386 words)

---

<a id="ledi"></a>
## LEDI — Laboratory Electronic Data Interchange

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | December 2004 → September 2013 |
| Total Pages | 628 |
| Total Words | 146,917 |
| Total Tables | 166 |
| Total Figures | 150 |
| Total Appendices | 5 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 71% |

### Document Types

| Type | Count |
|------|-------|
| base-impl | 2 |
| installation-guide | 2 |
| base-setup | 1 |
| base-hl7 | 1 |
| user-manual | 1 |

### Notable Documents

- **LA*5.2*80/LR*5.2*427 LDSI/LEDI IV Update User Manual** (user-manual, 38,954 words)
- **LA*5.2*64/LR*5.2*286 LEDI III Implementation and User Guide** (base-impl, 36,367 words)
- **LA*5.2*80/LR*5.2*427 LDSI/LEDI IV Update HL7 Interface Specification** (base-hl7, 29,736 words)
- **LA*5.2*80/LR*5.2*427 LDSI/LEDI IV AP MICRO Configuration Guide** (base-setup, 23,535 words)
- **LA*5.2*64/LR*5.2*286 LEDI III Installation Guide** (installation-guide, 15,985 words)

---

<a id="lex"></a>
## LEX — Lexicon Utility

[Back to TOC](#table-of-contents)

The VistA Lexicon Utility Version 2.0 is a dictionary of medical terms which can be used by all clinical areas. It provides the basis for a common language of terminology so that all members of a health care team may communicate with each other. It provides a variety of coding schemes and the ability to update these coding systems.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | September 1996 |
| Total Pages | 1,435 |
| Total Words | 61,484 |
| Total Tables | 282 |
| Total Figures | 0 |
| Total Appendices | 3 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Clinical Lexicon Version 2 Technical Manual  Developer's Guide** (technical-manual, 78,659 words)
- **Clinical Lexicon Version 2 User Manual** (user-manual, 8,940 words)
- **Clinical Lexicon Version 2 Installation Guide** (installation-guide, 6,492 words)

---

<a id="lhs"></a>
## LHS — Laboratory Hybrid Worklist

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | August 2021 |
| Total Pages | 17 |
| Total Words | 3,415 |
| Total Tables | 9 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |

### Notable Documents

- **LHS*1*0 Lighthouse Deployment, Installation, Back-out, and Rollback Guide** (installation-guide, 4,005 words)

---

<a id="lr"></a>
## LR — Laboratory

[Back to TOC](#table-of-contents)

VTWG on 4/20/2021, per request component of VistA - Laboratory (VistA-LAB) - #1381,Assists in tracking infectious diseases. It establishes a SAS data set which is used by the Office of Infectious Diseases (OID).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 21 |
| Date Range | October 1994 → October 2024 |
| Total Pages | 1,241 |
| Total Words | 591,541 |
| Total Tables | 155 |
| Total Figures | 86 |
| Total Appendices | 6 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 62% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 8 |
| release-note | 4 |
| installation-guide | 4 |
| base-impl | 2 |
| base-hl7 | 1 |
| base-security | 1 |
| technical-manual | 1 |

### Notable Documents

- **Laboratory Version 5.2 Planning Implementation Guide (LR*5.2*569)** (base-impl, 190,156 words)
- **Laboratory Planning Implementation Guide (LR*5.2*547)** (base-impl, 188,961 words)
- **Laboratory Version 5.2 Technical Manual (Current LR*5.2*570)** (technical-manual, 74,546 words)
- **Laboratory Version 5.2 User Manual** (user-manual, 49,637 words)
- **Laboratory Version 5.2 Release Notes** (release-note, 27,482 words)

---

<a id="mag"></a>
## MAG — VistA Imaging

[Back to TOC](#table-of-contents)

VistA Imaging facilitates medical decision-making by delivering complete multimedia patient information to the clinician’s desktop in an integrated manner. Windows-based workstations are interfaced to the main hospital system in a client-server architecture to always make images and associated text data available anywhere in the hospital or across VA.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 63 |
| Date Range | March 2002 → January 2025 |
| Total Pages | 8,182 |
| Total Words | 776,974 |
| Total Tables | 1,502 |
| Total Figures | 1,136 |
| Total Appendices | 108 |
| Update Density | 0.8 docs/yr |
| Knowledge Ratio | 71% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 29 |
| installation-guide | 17 |
| supplement | 7 |
| base-setup | 3 |
| quick-ref | 3 |
| base-hl7 | 1 |
| release-note | 1 |
| base-security | 1 |
| technical-manual | 1 |

### Notable Documents

- **VistA Imaging DICOM Gateway User Guide** (user-manual, 74,302 words)
- **VistA Imaging System Technical Manual** (technical-manual, 60,842 words)
- **Profiles for HL7 Messages from VistA to Commercial PACS** (base-hl7, 55,102 words)
- **VistA Imaging Clinical Display Workstation User Manual** (user-manual, 50,823 words)
- **VistA Imaging System Installation Guide** (installation-guide, 49,473 words)

---

<a id="mc"></a>
## MC — Medicine

[Back to TOC](#table-of-contents)

The Medicine module serves clinical services and maximizes the use of the data within VistA. VAMC database. The module allows entry, edit, and viewing of data for many medical tests and procedures.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | September 1996 → July 2014 |
| Total Pages | 341 |
| Total Words | 64,445 |
| Total Tables | 50 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 1 |
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Medicine Version 2.3 User Manual** (user-manual, 43,039 words)
- **Medicine Version 2.3 Technical Manual** (technical-manual, 19,200 words)
- **Medicine Version 2.3 Release Notes and Installation Guide** (installation-guide, 14,578 words)
- **MC*2.3*43/44 Release Notes** (release-note, 1,925 words)

---

<a id="md"></a>
## MD — Clinical Procedures

[Back to TOC](#table-of-contents)

Clinical Procedures (CP) passes final patient results, using Health Level 7 (HL7) messaging, between vendor clinical information systems (CIS) and VistA. Patients’ test results or reports are displayed through the Computerized Patient Record System (CPRS).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 63 |
| Date Range | April 2004 → July 2025 |
| Total Pages | 3,136 |
| Total Words | 716,322 |
| Total Tables | 764 |
| Total Figures | 34 |
| Total Appendices | 34 |
| Update Density | 1.7 docs/yr |
| Knowledge Ratio | 40% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 23 |
| user-manual | 9 |
| technical-manual | 8 |
| base-impl | 7 |
| release-note | 7 |
| change-page | 7 |
| unknown | 1 |
| supplement | 1 |

### Notable Documents

- **MD*1*72 CliO Terminology Dictionary & Clinical Data Model Revised** (supplement, 195,592 words)
- **MD*1*23 Technical Manual (CP Flowsheets)** (technical-manual, 41,697 words)
- **MD*1*12 Technical Manual (CP Flowsheets)** (technical-manual, 41,174 words)
- **MD*1*16 Technical Manual (CP Flowsheets)** (technical-manual, 41,166 words)
- **Clinical Procedures Version 1 Implementation Guide** (base-impl, 37,028 words)

---

<a id="med"></a>
## MED — Medication Reconciliation

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | June 2010 → December 2025 |
| Total Pages | 188 |
| Total Words | 29,815 |
| Total Tables | 93 |
| Total Figures | 97 |
| Total Appendices | 4 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 29% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 5 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **TIU*1*374 Mobile Electronic Documentation (MED) User Manual** (user-manual, 12,251 words)
- **TIU*1*374 Mobile Electronic Documentation (MED) Technical Manual** (technical-manual, 10,671 words)
- **TIU*1*262 Mobile Electronic Documentation (MED) Installation Guide** (installation-guide, 6,322 words)
- **TIU*1*244 Mobile Electronic Documentation (MED) Installation Guide** (installation-guide, 5,774 words)
- **TIU*1*315 Mobile Electronic Documentation (MED) Installation Guide** (installation-guide, 3,867 words)

---

<a id="mmrs"></a>
## MMRS — Methicillin Resistant Staphylococcus Aureus Program Tools

[Back to TOC](#table-of-contents)

The MRSA Program Tools (MRSA-PT) application provides a method to extract data related to MRSA Nares screening, clinical cultures, and patient movements within the selected facility.

The MRSA Program Tools (MRSA-PT) was replaced by MDRO -PT. MDRO- PT is planned to be replaced by Cerner’s Infection Control.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | January 2010 → April 2017 |
| Total Pages | 332 |
| Total Words | 60,126 |
| Total Tables | 144 |
| Total Figures | 151 |
| Total Appendices | 14 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 62% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| installation-guide | 2 |
| technical-manual | 2 |
| unknown | 1 |

### Notable Documents

- **MMRS*1*4 User Guide** (user-manual, 25,106 words)
- **MMRS*1*5 User Guide** (user-manual, 23,191 words)
- **MRSA Program Tools Version 1 Installation Manual** (installation-guide, 20,306 words)
- **MRSA Program Tools Version 1 User Manual** (user-manual, 18,974 words)
- **MRSA Program Tools Version 1 Technical Manual** (technical-manual, 7,987 words)

---

<a id="mon"></a>
## MON — VistA Monograph

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | October 2013 |
| Total Pages | 239 |
| Total Words | 79,328 |
| Total Tables | 3 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 0% |

---

<a id="mpif"></a>
## MPIF — Master Patient Index / Patient Demographics

[Back to TOC](#table-of-contents)

The Master Veteran Index (MVI) database (formerly known as the Master Patient Index [MPI]) is the primary vehicle for assigning and maintaining unique patient identifiers. A gateway in VistA establishes connectivity between VA Medical Center (VAMC) systems and patient registration processes and links to the MVI for message processing and patient identification.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | April 1999 → November 2016 |
| Total Pages | 171 |
| Total Words | 99,941 |
| Total Tables | 329 |
| Total Figures | 9 |
| Total Appendices | 11 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 83% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 2 |
| base-hl7 | 1 |
| installation-guide | 1 |
| base-dev | 1 |
| user-manual | 1 |

### Notable Documents

- **MPI HL7 Interface Specification** (base-hl7, 73,952 words)
- **MPI/PD Version 1 VISTA User Manual** (user-manual, 68,601 words)
- **MPI/PD Version 1 VISTA Technical Manual** (technical-manual, 57,529 words)
- **MPI/PD Version 1 VISTA Programmer Manual** (base-dev, 45,758 words)
- **MPI MPIF*1*63 Installation, Back-Out, and Rollback Guide** (installation-guide, 3,777 words)

---

<a id="ncr"></a>
## NCR — National Clinician Reminders

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | April 2024 |
| Total Pages | 27 |
| Total Words | 3,927 |
| Total Tables | 13 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |

### Notable Documents

- **National Clozapine Registry Technical Manual (YS*5.01*227)** (technical-manual, 4,349 words)
- **National Clozapine Registry Deployment, Installation, Back-out, and Rollback Guide (YS*5.01*227)** (installation-guide, 2,280 words)

---

<a id="npm"></a>
## NPM — National Patch Module

[Back to TOC](#table-of-contents)

The National Patch Module Guide describes the purpose, roles, responsibilities, and steps for the initiation, development, creation, and release of patches to VHA Information Systems and Technology Architecture (VistA) products via the National Patch Module (NPM). NPM resides on FORUM and is a software package that provides a database for the distribution of software patches and updates.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | December 1992 |
| Total Pages | 34 |
| Total Words | 8,927 |
| Total Tables | 2 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| unknown | 2 |
| installation-guide | 1 |

### Notable Documents

- **NPM Release Notes Installation Guide** (installation-guide, 4,490 words)
- **NPM Operational Summary** (unknown, 3,961 words)
- **NPM Patch Module Enhancments** (unknown, 732 words)

---

<a id="numi"></a>
## NUMI — National Utilization Management Integration

[Back to TOC](#table-of-contents)

The National Utilization Management Integration (NUMI) application is a web-based solution that automates utilization review assessment and outcomes. The Utilization Management (UM) Process is a tool used to help ensure that patients are receiving the right care, at the right time, and in the right place. UM is both a quality and efficiency tool, as it is used to move patients efficiently through the VA system to maximize use of resources.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 15 |
| Date Range | April 2021 → March 2026 |
| Total Pages | 1,776 |
| Total Words | 293,177 |
| Total Tables | 443 |
| Total Figures | 1,344 |
| Total Appendices | 90 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 10 |
| base-setup | 5 |

### Notable Documents

- **NUMI User Guide Version 15.15** (user-manual, 49,490 words)
- **NUMI User Guide** (user-manual, 48,488 words)
- **NUMI User Guide Version 15.10** (user-manual, 48,316 words)
- **NUMI User Guide Version 15.9** (user-manual, 48,311 words)
- **NUMI User Guide Version 15.11** (user-manual, 48,248 words)

---

<a id="nupa"></a>
## NUPA — National Utilization Performance Analytics

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | April 2012 → January 2014 |
| Total Pages | 402 |
| Total Words | 32,643 |
| Total Tables | 38 |
| Total Figures | 0 |
| Total Appendices | 6 |
| Update Density | 0.6 docs/yr |
| Knowledge Ratio | 83% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 4 |
| installation-guide | 1 |
| technical-manual | 1 |

### Notable Documents

- **PADP Version 1 Technical Manual** (technical-manual, 26,201 words)
- **PADP Version 1 RN Reassessment User Manual** (user-manual, 11,387 words)
- **PADP Version 1 Admission-RN Assessment User Manual** (user-manual, 11,343 words)
- **PADP Version 1 Interdisciplinary Plan of Care User Manual** (user-manual, 4,555 words)
- **PADP Version 1 Admission-Nursing Data Collection User Manual** (user-manual, 4,247 words)

---

<a id="nur"></a>
## NUR — Nursing

[Back to TOC](#table-of-contents)

The Nursing application is a component of the Department of Veterans Affairs VistA program. It is comprised of multiple modules (i.e., Administration, Clinical, Education, Performance Improvement, and Research).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 8 |
| Date Range | April 1997 → May 2018 |
| Total Pages | 34 |
| Total Words | 157,996 |
| Total Tables | 253 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 25% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 3 |
| release-note | 2 |
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Nursing Version 4 User Manual** (user-manual, 148,746 words)
- **Nursing Version 4 Technical Manual and Package Security Guide** (technical-manual, 44,991 words)
- **Nursing Version 4 Installation Guide** (installation-guide, 4,657 words)
- **Nursing Version 4 Release Notes** (release-note, 1,557 words)
- **NUR*4*43 PAID Enhancements for VANOD Release Notes** (release-note, 1,094 words)

---

<a id="onc"></a>
## ONC — Oncology

[Back to TOC](#table-of-contents)

OncoTraX Cancer Registry is an integrated collection of computer programs and routines, which work together in assisting the Cancer Registrars to create and maintain a cancer patient database. The software creates case listings and registry reports for Cancer Boards (Cancer Conferences), special studies, and the Annual Report recommended by the American College of Surgeons (ACoS).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | JUNE 2014 |
| Total Pages | 95 |
| Total Words | 18,200 |
| Total Tables | 17 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Oncology Version 2.2 User Manual (Updated ONC*2.2*22)** (user-manual, 19,177 words)
- **Oncology Version 2.2 Technical Manual and Package Security Guide (Updated ONC*2.2*22)** (technical-manual, 8,469 words)

---

<a id="oops"></a>
## OOPS — Automated Safety Incident Surveillance Tracking System

[Back to TOC](#table-of-contents)

Effective January 1, 2019, ASISTS is decommissioned. Patch OOPS*2*32 retired the ASISTS (OOPS) v2 package.ASISTS has been replaced by Joint Patient Safety Reporting Web (JPSR-Web), but VistA data remains available with read-only access to employees, supervisors, unions, & occupational health. Access to Safety [OOPS GUI SAFETY OFFICER MENU] menu & Workers' Comp [OOPS GUI WORKERS' COMP MENU] menu is still allowed for designated users.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | June 2002 → September 2008 |
| Total Pages | 222 |
| Total Words | 31,259 |
| Total Tables | 18 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 2 |
| installation-guide | 1 |
| base-security | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **ASISTS GUI Version 2 User Manual** (user-manual, 10,761 words)
- **ASISTS GUI Version 2 Technical Manual** (technical-manual, 9,982 words)
- **ASISTS GUI Version 2 Release Notes** (release-note, 5,296 words)
- **ASISTS GUI Version 2 Installation Guide** (installation-guide, 3,963 words)
- **OOPS*2*15 Release Notes** (release-note, 3,242 words)

---

<a id="pait"></a>
## PAIT — Patient Assessment Instrument

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | March 2004 → March 2010 |
| Total Pages | 1,296 |
| Total Words | 30,367 |
| Total Tables | 158 |
| Total Figures | 0 |
| Total Appendices | 4 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 3 |
| supplement | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **PAIT Version 1 Technical Manual** (technical-manual, 36,201 words)
- **SD*5.3*333 PAIT Release Notes** (release-note, 21,389 words)
- **PAIT Version 1 User Manual** (user-manual, 6,757 words)
- **SD*5.3*376 PAIT Release Notes** (release-note, 3,423 words)
- **SD*5.3*349 PAIT Release Notes** (release-note, 3,101 words)

---

<a id="pcmm"></a>
## PCMM — Primary Care Management Module

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | September 1998 → December 2012 |
| Total Pages | 135 |
| Total Words | 52,385 |
| Total Tables | 59 |
| Total Figures | 0 |
| Total Appendices | 4 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 30% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 4 |
| user-manual | 3 |
| installation-guide | 2 |
| unknown | 1 |

### Notable Documents

- **Primary Care Management Module (PCMM) User Manual** (user-manual, 39,368 words)
- **PCMM Mental Health Treatment Coordinator (MHTC) User Manual** (user-manual, 8,362 words)
- **SD*5.3*264/277 PCMM Enhancements for Direct Primary Care User Guide** (user-manual, 6,415 words)
- **SD*5.3*297 Unassigned Inactive Primary Care Physician Release Notes** (release-note, 5,451 words)
- **SD*5.3*177 PCMM Install Guide/Release Notes** (release-note, 4,548 words)

---

<a id="pecs"></a>
## PECS — Pharmacy: Pharmacy Enterprise Customization System

[Back to TOC](#table-of-contents)

PECS allows users to customize the contents of several pharmacy-related information sets.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 29 |
| Date Range | July 2012 → May 2025 |
| Total Pages | 812 |
| Total Words | 133,101 |
| Total Tables | 231 |
| Total Figures | 203 |
| Total Appendices | 41 |
| Update Density | 1.6 docs/yr |
| Knowledge Ratio | 31% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 12 |
| release-note | 8 |
| supplement | 5 |
| user-manual | 4 |

### Notable Documents

- **PREC*7*2 PECS User Guide** (user-manual, 36,524 words)
- **PREC*6*516 USER GUIDE** (user-manual, 36,251 words)
- **PECS Version 6.2 User Guide** (user-manual, 36,147 words)
- **PREC*6.1*717 USER GUIDE** (user-manual, 35,942 words)
- **PREC*7*1 PECS Troubleshooting Guide** (supplement, 14,973 words)

---

<a id="poc"></a>
## POC — Point of Care

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | June 2005 → June 2018 |
| Total Pages | 188 |
| Total Words | 43,734 |
| Total Tables | 49 |
| Total Figures | 1 |
| Total Appendices | 0 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 75% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |
| base-hl7 | 1 |
| release-note | 1 |

### Notable Documents

- **Laboratory:  POC Interface Installation and User Guide** (user-manual, 20,351 words)
- **Laboratory: POC Interface Installation and User Guide (LR*5.2*548)** (user-manual, 20,351 words)
- **LA*5.2*67/LR*5.2*290 Laboratory: POC HL7 Interface Specifications Document** (base-hl7, 7,410 words)
- **LA*5.2*87 Laboratory: POC VHIC Card Update Release Notes** (release-note, 618 words)

---

<a id="prc"></a>
## PRC — IFCAP (Integrated Funds Distribution, Control Point Activity)

[Back to TOC](#table-of-contents)

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) module automates a spectrum of VA financial activities. VA employees use IFCAP to manage budgets, order goods and services, maintain records of available funds, determine the status of a request, compare vendors and items to determine the best purchase, record the receipt of items into the warehouse, and pay vendors.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 26 |
| Date Range | August 1999 → March 2026 |
| Total Pages | 2,922 |
| Total Words | 364,340 |
| Total Tables | 2,014 |
| Total Figures | 409 |
| Total Appendices | 26 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 85% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 17 |
| installation-guide | 4 |
| technical-manual | 2 |
| base-hl7 | 2 |
| base-security | 1 |

### Notable Documents

- **IFCAP Version 5.1 Technical Manual** (technical-manual, 323,830 words)
- **IFCAP Version 5.1 Technical Manual (PRC*5.1*225)** (technical-manual, 290,366 words)
- **IFCAP Version 5.1 Purchasing Agent User's Guide** (user-manual, 52,833 words)
- **IFCAP Version 5.1 Generic Inventory User's Guide** (user-manual, 51,786 words)
- **IFCAP Version 5.1 Control Point Clerk User's Guide** (user-manual, 46,190 words)

---

<a id="prca"></a>
## PRCA — Accounts Receivable

[Back to TOC](#table-of-contents)

The Accounts Receivable (AR) package is a system of accounting and receivables management. The AR package automates the debt collection process, and a billing module is available to create statements for non-medical care debts. Functionality is available to establish, follow-up on, collect against and track all medical facility debts.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 105 |
| Date Range | March 1995 → December 2025 |
| Total Pages | 2,262 |
| Total Words | 445,581 |
| Total Tables | 561 |
| Total Figures | 208 |
| Total Appendices | 27 |
| Update Density | 2.8 docs/yr |
| Knowledge Ratio | 19% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 67 |
| user-manual | 18 |
| release-note | 18 |
| supplement | 1 |
| technical-manual | 1 |
| unknown | 1 |

### Notable Documents

- **Accounts Receivable Version 4.5 ePayments User Manual (EDI Lockbox)** (user-manual, 62,005 words)
- **PRCA*4.5*375 Accounts Receivable ePayments User Manual (EDI) Lockbox** (user-manual, 50,139 words)
- **Accounts Receivable Version 4.5 Technical Manual/Security Guide** (technical-manual, 48,849 words)
- **Accounts Receivable Version 4.5 User Manual - Cross Servicing Menu** (user-manual, 34,765 words)
- **Accounts Receivable Version 4.5 Debt Management Center (DMC) Referral Process User Guide** (user-manual, 28,864 words)

---

<a id="prcn"></a>
## PRCN — Equipment /Turn-In Request

[Back to TOC](#table-of-contents)

The Equipment/Turn-In Request software provides additional functionality within the Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP) package, including the ability to enter an electronic request for new, non-expendable equipment and replacement equipment.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | June 1996 |
| Total Pages | 146 |
| Total Words | 24,757 |
| Total Tables | 57 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 75% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| base-security | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **PRCN Version 1 User Manual** (user-manual, 19,327 words)
- **PRCN Version 1 Technical Manual** (technical-manual, 7,661 words)
- **PRCN Version 1 Installation Guide Release Notes** (installation-guide, 2,420 words)
- **PRCN Version 1 Package Security Guide** (base-security, 330 words)

---

<a id="prea"></a>
## PREA — Pharmacy Reengineering — Advanced

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | August 2023 → January 2026 |
| Total Pages | 261 |
| Total Words | 36,926 |
| Total Tables | 32 |
| Total Figures | 485 |
| Total Appendices | 3 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 86% |

### Document Types

| Type | Count |
|------|-------|
| quick-ref | 2 |
| supplement | 2 |
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **AMPL User Guide** (user-manual, 18,050 words)
- **AMPL Frequently Asked Questions Guide** (quick-ref, 8,773 words)
- **AMPL Frequently Asked Questions** (quick-ref, 6,917 words)
- **AMPL Production Operations Manual** (supplement, 4,674 words)
- **AMPL Production Operations Manual (POM)** (supplement, 4,347 words)

---

<a id="pred"></a>
## PRED — Pharmacy Reengineering — Electronic Data

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 23 |
| Date Range | June 2012 → May 2025 |
| Total Pages | 693 |
| Total Words | 111,729 |
| Total Tables | 66 |
| Total Figures | 102 |
| Total Appendices | 42 |
| Update Density | 1.8 docs/yr |
| Knowledge Ratio | 0% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 18 |
| release-note | 5 |

### Notable Documents

- **DATUP Version 2 National Installation Guide** (installation-guide, 11,731 words)
- **DATUP Version 1.0.00.003 National Install Guide** (installation-guide, 10,521 words)
- **DATUP Version 1.1 Install Guide** (installation-guide, 10,468 words)
- **DATUP Version 1.0.00.003 Local Install Guide** (installation-guide, 9,513 words)
- **PRED*4*3 DATUP Version 4.0.3 Installation Guide** (installation-guide, 9,368 words)

---

<a id="prem"></a>
## PREM — Pharmacy: Medication Order Check Healthcare Application

[Back to TOC](#table-of-contents)

Medication Order Checks for Healthcare Applications (MOCHA) provides enhanced order checking functionality in the Computerized Patient Record System (CPRS) and in the Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy packages.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 20 |
| Date Range | September 2013 → May 2025 |
| Total Pages | 347 |
| Total Words | 72,296 |
| Total Tables | 80 |
| Total Figures | 41 |
| Total Appendices | 17 |
| Update Density | 1.5 docs/yr |
| Knowledge Ratio | 10% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 13 |
| release-note | 5 |
| supplement | 2 |

### Notable Documents

- **PREM*4*2 MOCHA Server Installation Guide** (installation-guide, 9,822 words)
- **PREM*4*1 MOCHA Server Version 4 Installation Guide** (installation-guide, 9,474 words)
- **MOCHA Server Version 3 Installation Guide** (installation-guide, 8,686 words)
- **MOCHA Server Version 3.2.1 Installation Guide** (installation-guide, 8,523 words)
- **MOCHA Server Version 3.1 Installation Guide** (installation-guide, 8,494 words)

---

<a id="prf"></a>
## PRF — Patient Record Flags

[Back to TOC](#table-of-contents)

The Patient Record Flags (PRF) software provides users with the ability to create, assign, inactivate, edit flags, produce reports on, and view patient record flag alerts. PRF is related toVistA - Computerized Patient Record System (CPRS), VASI#1849. Patient Record Flags are Alerts within Patient Records.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 11 |
| Date Range | September 2003 → March 2019 |
| Total Pages | 256 |
| Total Words | 59,955 |
| Total Tables | 153 |
| Total Figures | 3 |
| Total Appendices | 7 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 36% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 5 |
| user-manual | 3 |
| base-hl7 | 1 |
| installation-guide | 1 |

### Notable Documents

- **DG*5.3*869/892/951/960_TIU*1*279 Patient Record Flags User Guide** (user-manual, 21,391 words)
- **DG*5.3*864 Patient Record Flags User Guide - HRMHP** (user-manual, 16,040 words)
- **DG*5.3*554/TIU*1*184/USR*1*27 Patient Record Flags Phase II Release Notes** (release-note, 8,025 words)
- **DG*5.3*425/951 Patient Record Flags HL7 Interface Specification** (base-hl7, 6,760 words)
- **DG*5.3*650 Patient Record Flags Phase III User Guide** (user-manual, 6,614 words)

---

<a id="prpf"></a>
## PRPF — Patient Record Flags

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | February 1989 |
| Total Pages | 597 |
| Total Words | 34,884 |
| Total Tables | 30 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| technical-manual | 1 |

### Notable Documents

- **PFOP Version 3 User Manual for Patient Funds Supervisor** (user-manual, 14,034 words)
- **PFOP Version 3 User Manual for Patient Funds Clerk** (user-manual, 12,665 words)
- **PRPF*3*15 PFOP Data Diagnostic Patch User Guide** (user-manual, 8,116 words)
- **PFOP Version 3 Technical Manual for Site Manager** (technical-manual, 7,677 words)

---

<a id="prs"></a>
## PRS — Personnel and Accounting Integrated Data

[Back to TOC](#table-of-contents)

PAID is a mainframe-based system which was retired in January of 2022 and is now awaiting decommissioning. FormerPAID functionalityhas been provided by HR-PAS.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | August 1995 → March 2018 |
| Total Pages | 626 |
| Total Words | 108,913 |
| Total Tables | 700 |
| Total Figures | 3 |
| Total Appendices | 2 |
| Update Density | 0.3 docs/yr |
| Knowledge Ratio | 30% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 4 |
| installation-guide | 2 |
| user-manual | 2 |
| technical-manual | 1 |
| change-page | 1 |

### Notable Documents

- **PAID Version 4 User Manual** (user-manual, 100,425 words)
- **PAID Version 4 Technical Manual** (technical-manual, 16,115 words)
- **PRS*4*93 User Manual - Part-Time Physicians** (user-manual, 7,839 words)
- **PAID Version 4 Installation Guide** (installation-guide, 2,642 words)
- **PRS*4*132 Release Notes-Telework** (release-note, 2,216 words)

---

<a id="psa"></a>
## PSA — Pharmacy Automatic Dispensing Equipment

[Back to TOC](#table-of-contents)

The Drug Accountability/Inventory Interface works toward perpetual inventory for each VA medical facility pharmacy by tracking all drugs through pharmacy locations.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | October 1997 → January 2025 |
| Total Pages | 407 |
| Total Words | 78,174 |
| Total Tables | 100 |
| Total Figures | 14 |
| Total Appendices | 3 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 40% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 4 |
| user-manual | 3 |
| release-note | 2 |
| technical-manual | 1 |

### Notable Documents

- **Drug Accountability/Inventory Interface Version 3 User Manual (Updated PSA*3*79)** (user-manual, 24,741 words)
- **Drug Accountability/Inventory Interface Version 3 User Manual** (user-manual, 24,623 words)
- **Drug Accountability/Inventory Interface Version 3 User Manual (PSA*3*85)** (user-manual, 24,566 words)
- **Drug Accountability/Inventory Interface Version 3 Technical Manual/Security Guide (Updated PSA*3*69)** (technical-manual, 11,918 words)
- **Drug Accountability/Inventory Interface Version 3 Release Notes** (release-note, 3,070 words)

---

<a id="psb"></a>
## PSB — Barcode Medication Administration

[Back to TOC](#table-of-contents)

Bar Code Medication Administration (BCMA) software provides a real-time, point-of- care solution for validating the administration of Unit Dose (UD) and Intravenous (IV) medications to inpatients and outpatients in Veterans Administration Medical Centers (VAMCs).

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 46 |
| Date Range | February 2004 → February 2026 |
| Total Pages | 1,707 |
| Total Words | 110,628 |
| Total Tables | 736 |
| Total Figures | 78 |
| Total Appendices | 35 |
| Update Density | 1.6 docs/yr |
| Knowledge Ratio | 22% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 16 |
| change-page | 11 |
| user-manual | 8 |
| release-note | 8 |
| technical-manual | 2 |
| unknown | 1 |

### Notable Documents

- **PSB*3*155 BCMA GUI User Manual** (user-manual, 45,127 words)
- **BCMA Version 3 Manager's User Manual (PSB*3*142)** (user-manual, 17,503 words)
- **BCMA Version 3 Technical Manual / Security Guide (PSB*3*142)** (technical-manual, 12,949 words)
- **BCMA Version 3 Technical Manual / Security Guide ( PSB*3*131)** (technical-manual, 12,848 words)
- **BCMA Version 3 Nursing CHUI User Manual** (user-manual, 11,290 words)

---

<a id="psd"></a>
## PSD — Controlled Substances

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 35 |
| Date Range | March 1997 → December 2021 |
| Total Pages | 820 |
| Total Words | 111,672 |
| Total Tables | 189 |
| Total Figures | 100 |
| Total Appendices | 4 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 26% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 21 |
| user-manual | 6 |
| installation-guide | 3 |
| release-note | 2 |
| technical-manual | 2 |
| base-security | 1 |

### Notable Documents

- **Controlled Substances Version 3 Technical Manual (Updated PSD*3*89)** (technical-manual, 22,618 words)
- **Controlled Substances Version 3 Technical Manual (Updated PSD*3*84)** (technical-manual, 21,543 words)
- **PSD*3*89 Controlled Substance DIRB** (installation-guide, 20,179 words)
- **Controlled Substances Version 3 Supervisor's User Manual (Updated PSD*3*89)** (user-manual, 11,665 words)
- **Controlled Substances Version 3 Supervisor's User Manual (Updated PSD*3*84)** (user-manual, 11,445 words)

---

<a id="psj"></a>
## PSJ — Inpatient Medications

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 96 |
| Date Range | December 1997 → August 2025 |
| Total Pages | 47,268 |
| Total Words | 960,459 |
| Total Tables | 2,499 |
| Total Figures | 198 |
| Total Appendices | 16 |
| Update Density | 2.8 docs/yr |
| Knowledge Ratio | 19% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 52 |
| release-note | 20 |
| user-manual | 11 |
| installation-guide | 6 |
| technical-manual | 4 |
| supplement | 1 |
| base-impl | 1 |
| base-hl7 | 1 |

### Notable Documents

- **Inpatient Medications Pharmacist's User Manual (PSJ*5*423)** (user-manual, 129,221 words)
- **Inpatient Medications Pharmacist's User Manual (Updated PSJ*5*399)** (user-manual, 126,346 words)
- **Inpatient Medications Pharmacist's User Manual (PSJ*5*447)** (user-manual, 126,021 words)
- **Inpatient Medications Version 5 Pharmacist's User Manual (Updated PSJ*5*364)** (user-manual, 125,104 words)
- **Inpatient Medications Nurse's User Manual (PSJ*5*423)** (user-manual, 74,898 words)

---

<a id="psn"></a>
## PSN — National Drug File

[Back to TOC](#table-of-contents)

The National Drug File (NDF) package provides standardization of the local drug files in all VA medical facilities. Standardization includes the adoption of new drug nomenclature and drug classification, as well as linking the local drug file entries to data in the National Drug files.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 20 |
| Date Range | October 1998 → August 2025 |
| Total Pages | 821 |
| Total Words | 182,681 |
| Total Tables | 188 |
| Total Figures | 0 |
| Total Appendices | 3 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 35% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 6 |
| release-note | 4 |
| user-manual | 3 |
| installation-guide | 3 |
| technical-manual | 3 |
| base-dev | 1 |

### Notable Documents

- **API Manual - Pharmacy Reengineering (PRE) (Updated PSN*4.0*576)** (base-dev, 47,096 words)
- **National Drug File Version 4 User Manual (Updated PSN*4*218)** (user-manual, 28,723 words)
- **National Drug File - User Manual (Updated PSN*4.0*576)** (user-manual, 27,771 words)
- **National Drug File - User Manual (Updated PSN*4.0*575)** (user-manual, 27,701 words)
- **National Drug File Version 4 Technical Manual (Updated PSN*4*575)** (technical-manual, 17,911 words)

---

<a id="pso"></a>
## PSO — Outpatient Pharmacy

[Back to TOC](#table-of-contents)

Outpatient Pharmacy provides a method for managing the medications given to Veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 141 |
| Date Range | December 1997 → September 2025 |
| Total Pages | 7,127 |
| Total Words | 2,054,517 |
| Total Tables | 1,890 |
| Total Figures | 783 |
| Total Appendices | 110 |
| Update Density | 3.2 docs/yr |
| Knowledge Ratio | 40% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 55 |
| user-manual | 47 |
| release-note | 35 |
| technical-manual | 5 |
| base-impl | 3 |
| base-dev | 1 |
| quick-ref | 1 |

### Notable Documents

- **Outpatient Pharmacy Version 7 Manager's User Manual (updated PSO*7*795)** (user-manual, 198,020 words)
- **Outpatient Pharmacy Version 7 Manager's User Manual (updated PSO*7*774)** (user-manual, 190,944 words)
- **Outpatient Pharmacy Version 7 Manager's User Manual (Updated PSO*7.0*653)** (user-manual, 178,812 words)
- **Outpatient Pharmacy Version 7 Manager's User Manual (Updated PSO*7.0*647)** (user-manual, 176,041 words)
- **Outpatient Pharmacy (PSO) Version 7 Manager's User Manual (PSO_7_p622) ARCHIVE** (user-manual, 173,830 words)

---

<a id="pss"></a>
## PSS — Pharmacy Data Management

[Back to TOC](#table-of-contents)

The Pharmacy Data Management (PDM) package provides tools for managing site configurable data in pharmacy files.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 77 |
| Date Range | September 1997 → August 2025 |
| Total Pages | 6,199 |
| Total Words | 632,308 |
| Total Tables | 719 |
| Total Figures | 66 |
| Total Appendices | 131 |
| Update Density | 2.3 docs/yr |
| Knowledge Ratio | 19% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 31 |
| release-note | 20 |
| installation-guide | 12 |
| user-manual | 6 |
| technical-manual | 5 |
| base-impl | 2 |
| supplement | 1 |
| unknown | 1 |
| base-hl7 | 1 |

### Notable Documents

- **Pharmacy Data Management Version 1 User Manual  (PSS*1*262)** (user-manual, 87,065 words)
- **Pharmacy Data Management Version 1 User Manual (updated PSS*1*187)** (user-manual, 84,749 words)
- **Pharmacy Data Management Version 1 User Manual (updated PSS*1*252)** (user-manual, 83,964 words)
- **Pharmacy Data Management User Manual (PSS 1_0_P247)** (user-manual, 82,490 words)
- **Pharmacy Data Management Version 1 User Manual (updated PSS*1*259)** (user-manual, 78,610 words)

---

<a id="psu"></a>
## PSU — Pharmacy Benefits Management

[Back to TOC](#table-of-contents)

The Pharmacy Benefits Management (PBM) package extracts medication dispensing data elements from numerous locations and makes reports available allowing projections of local drug usage and identification of potential accountability problem areas.The extracted data is transmitted to the PBM using VA Mailman.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 16 |
| Date Range | June 2005 → April 2016 |
| Total Pages | 524 |
| Total Words | 47,149 |
| Total Tables | 108 |
| Total Figures | 48 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 31% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 5 |
| release-note | 4 |
| user-manual | 3 |
| technical-manual | 2 |
| installation-guide | 2 |

### Notable Documents

- **Benefits Management Version 4 User Manual** (user-manual, 29,528 words)
- **PSU*4*19 User Manual Change Pages** (change-page, 8,881 words)
- **Ask A Pharmacist User Manual (Mobile Applications Phase 2)** (user-manual, 6,815 words)
- **Benefits Management Version 4 Release Notes-Extract Enhancements Phases I thru II** (release-note, 5,703 words)
- **Benefits Management Version 4 Technical Manual/Security Guide** (technical-manual, 3,911 words)

---

<a id="psx"></a>
## PSX — Consolidated Mail Outpatient Pharmacy

[Back to TOC](#table-of-contents)

The Consolidated Mail Outpatient Pharmacy (CMOP) package provides a regional system resource to expedite the distribution of mail-out prescriptions to veteran patients.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 24 |
| Date Range | April 1997 → August 2024 |
| Total Pages | 8,949 |
| Total Words | 112,596 |
| Total Tables | 163 |
| Total Figures | 8 |
| Total Appendices | 22 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 17% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 8 |
| installation-guide | 6 |
| change-page | 6 |
| user-manual | 2 |
| base-security | 1 |
| technical-manual | 1 |

### Notable Documents

- **CMOP Version 2 Technical Manual (Updated PSX*2*91)** (technical-manual, 35,564 words)
- **CMOP Version 2 User Manual (Updated PSX*2*91)** (user-manual, 31,143 words)
- **CMOP Version 2 User Manual (Updated PSX*2*98)** (user-manual, 30,166 words)
- **CMOP Version 2 Installation Guide** (installation-guide, 8,282 words)
- **PSX*2*48 Release Notes - HIPAA NCPDP Connection for EDI Pharmacy** (release-note, 5,608 words)

---

<a id="px"></a>
## PX — PCE Patient Care Encounter

[Back to TOC](#table-of-contents)

Patient Care Encounter (PCE) captures clinical data resulting from ambulatory care patient encounters.The data includes captured clinical data documents ("encounters") and related encounter information, problems treated during the encounter, procedures done, immunizations, patient education, service connection, and skin tests.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 15 |
| Date Range | August 1996 → March 2026 |
| Total Pages | 568 |
| Total Words | 127,601 |
| Total Tables | 124 |
| Total Figures | 0 |
| Total Appendices | 15 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 27% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 6 |
| installation-guide | 5 |
| user-manual | 2 |
| technical-manual | 1 |
| quick-ref | 1 |

### Notable Documents

- **Patient Care Encounter Technical Manual** (technical-manual, 38,492 words)
- **Patient Care Encounter Version 1 User Manual Appendices** (user-manual, 34,007 words)
- **Patient Care Encounter Version 1 User Manual (Updated PX*1*241)** (user-manual, 30,616 words)
- **Patient Care Encounter Version 1 Installation Guide** (installation-guide, 12,383 words)
- **PX*1*211 PCE Standardization Deployment, Installation, Back-Out and Rollback Guide** (installation-guide, 9,734 words)

---

<a id="pxrm"></a>
## PXRM — Clinical Reminders

[Back to TOC](#table-of-contents)

Clinical Reminders may be used for both clinical and administrative purposes. However, the primary goal is to provide relevant information to providers at the point of care, for improving care for veterans.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 76 |
| Date Range | May 2002 → September 2022 |
| Total Pages | 9,774 |
| Total Words | 732,166 |
| Total Tables | 1,159 |
| Total Figures | 80 |
| Total Appendices | 154 |
| Update Density | 2.4 docs/yr |
| Knowledge Ratio | 34% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 38 |
| user-manual | 15 |
| release-note | 11 |
| technical-manual | 3 |
| quick-ref | 3 |
| base-setup | 3 |
| supplement | 2 |
| unknown | 1 |

### Notable Documents

- **PXRM*2*21 Manager's Manual** (user-manual, 116,495 words)
- **Clinical Reminders Version 2 Manager's Manual** (user-manual, 115,297 words)
- **PXRM*2*22 Manager's Manual** (user-manual, 114,729 words)
- **PXRM*2*19 Home Telehealth Install and Setup Guide** (installation-guide, 46,083 words)
- **PXRM*2*26 ICD-10 Update Installation Guide** (installation-guide, 29,837 words)

---

<a id="qac"></a>
## QAC — Patient Representative

[Back to TOC](#table-of-contents)

PATREP is no longer identified asa system. Itwas replaced by PATS, VASI ID #1492.

The purpose of the Patient Representative module is to ensure VA medical facilities respond to patient needs. The software tracks and trends compliments and complaints and measures the facility’s types of complaints as they relate to the Customer Services Standards and the National Patient Satisfaction Survey.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | March 2007 → April 2013 |
| Total Pages | 327 |
| Total Words | 59,215 |
| Total Tables | 168 |
| Total Figures | 0 |
| Total Appendices | 7 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 33% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 3 |
| user-manual | 2 |
| unknown | 1 |

### Notable Documents

- **PATS User Guide** (user-manual, 34,412 words)
- **PATS System Management Guide** (user-manual, 21,714 words)
- **PATS Data Migration Guide** (installation-guide, 18,776 words)
- **PATS Installation Guide for EIE group** (installation-guide, 7,578 words)
- **PATS Installation Guide for IRM Staff** (installation-guide, 4,504 words)

---

<a id="qam"></a>
## QAM — Clinical Monitoring System

[Back to TOC](#table-of-contents)

VTWG 8/10/2021, per request after an internal review, it was discovered that VistA-CMS - #1785 is a module within VistA - Quality Integration #1947. Please mark as NOT A System.The Clinical Monitoring System (VistA-CMS), formerly known as CMS, allows the user to design monitors that capture patient data in support of quality management efforts.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | September 1993 |
| Total Pages | 217 |
| Total Words | 34,281 |
| Total Tables | 213 |
| Total Figures | 0 |
| Total Appendices | 6 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 75% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |
| installation-guide | 1 |
| technical-manual | 1 |

### Notable Documents

- **Clinical Monitoring System Version 1 ADPAC Guide** (user-manual, 21,385 words)
- **Clinical Monitoring System Version 1 User Manual** (user-manual, 11,099 words)
- **Clinical Monitoring System Version 1 Technical Manual** (technical-manual, 7,356 words)
- **Clinical Monitoring System Version 1 Installation Guide** (installation-guide, 6,452 words)

---

<a id="qao"></a>
## QAO — Occurrence Screen

[Back to TOC](#table-of-contents)

VTWG on 8/10/2021 per request After an internal review, it was discovered that VistA-QAO- #1826 is a module within VistA - Quality Integration #1947. Please mark as NOT A System. The Occurrence Screen (VistA-QAO) module supports VHA policy by providing for the identification of events requiring follow-up review. It generates worksheets used by clinical, peer, management, and committee-level reviewers and identifies practitioner, systems, and equipment-related problems and results.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | September 1993 |
| Total Pages | 155 |
| Total Words | 22,732 |
| Total Tables | 235 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 75% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **Occurrence Screen Version 3 ADPAC Guide** (user-manual, 9,747 words)
- **Occurrence Screen Version 3 User Manual** (user-manual, 9,573 words)
- **Occurrence Screen Version 3 Release Notes Installation Guide** (release-note, 5,417 words)
- **Occurrence Screen Version 3 Technical Manual** (technical-manual, 4,751 words)

---

<a id="qap"></a>
## QAP — Survey Generator

[Back to TOC](#table-of-contents)

The Survey Generator is a software package which allows creation and maintenance of computerized survey forms.

03/21/2019, changed System Status to Inactive as the functionality is no longer in use. Survey Generator is aSystem Component/Application for 1465: VistA - Nursing

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | June 1995 → APRIL 2024 |
| Total Pages | 120 |
| Total Words | 19,575 |
| Total Tables | 1 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |

### Notable Documents

- **Survery Generator User Guide** (user-manual, 10,228 words)
- **Survey Generator User Guide** (user-manual, 10,173 words)

---

<a id="ra"></a>
## RA — Radiology / Nuclear Medicine

[Back to TOC](#table-of-contents)

Radiology/Nuclear Medicine is a comprehensive software package designed to assist with the functions related to processing patients for imaging examinations.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 30 |
| Date Range | April 1998 → January 2026 |
| Total Pages | 790 |
| Total Words | 260,637 |
| Total Tables | 512 |
| Total Figures | 55 |
| Total Appendices | 9 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 33% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 19 |
| base-hl7 | 4 |
| user-manual | 3 |
| supplement | 2 |
| technical-manual | 1 |
| installation-guide | 1 |

### Notable Documents

- **Radiology Version 5 User Manual (Updated RA*5*216)** (user-manual, 118,872 words)
- **Radiology Version 5 ADPAC Guide** (user-manual, 72,676 words)
- **HL7 Interface Specification (Updated RA*5*203)** (base-hl7, 32,801 words)
- **RA5*158 HL7 Interface Specification** (base-hl7, 31,296 words)
- **Radiology Version 5 Technical Manual** (technical-manual, 27,017 words)

---

<a id="rmpr"></a>
## RMPR — Prosthetics

[Back to TOC](#table-of-contents)

The VistA Prosthetics package automates purchasing.The Prosthetics module enhances patient care by determining what prosthetic services and devices have been provided to the Veteran in the past, and decreasing the time required for the order, delivery, and/or repair of devices.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 27 |
| Date Range | December 1995 → October 2024 |
| Total Pages | 1,120 |
| Total Words | 25,597 |
| Total Tables | 2,214 |
| Total Figures | 0 |
| Total Appendices | 25 |
| Update Density | 0.5 docs/yr |
| Knowledge Ratio | 48% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 11 |
| release-note | 8 |
| installation-guide | 5 |
| base-security | 1 |
| technical-manual | 1 |
| unknown | 1 |

### Notable Documents

- **Prosthetics Version 3 VistA Suite (GUI) User Manual (Updated RMPR*3*136)** (user-manual, 30,604 words)
- **RMPR*3*61 Prosthetics Inventory Package (PIP) User Manual** (user-manual, 29,574 words)
- **Prosthetics Version 3 Basic User Manual (Updated RMPR*3*178)** (user-manual, 22,793 words)
- **RMPR*3*182 Purchase Cards User Manual** (user-manual, 14,469 words)
- **Home Oxygen Module User Manual (Updated RMPR*3*168)** (user-manual, 12,922 words)

---

<a id="roes"></a>
## ROES — Remote Order Entry System

[Back to TOC](#table-of-contents)

The Remote Order Entry System (ROES) is the front-end of the DenverLogistics Center (DLC) supply chain/order fulfillment production system. ROES is used by VA clinicians to place orders for certain types of medical products and services that are maintained under contract by the DLC.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 5 |
| Date Range | October 2003 → June 2019 |
| Total Pages | 209 |
| Total Words | 44,593 |
| Total Tables | 46 |
| Total Figures | 10 |
| Total Appendices | 6 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 2 |
| base-security | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **ROES Version 3 User Manual** (user-manual, 31,024 words)
- **ROES Version 3 Installation Guide** (installation-guide, 5,810 words)
- **ROES Version 3 Technical Manual** (technical-manual, 4,993 words)
- **ROES Version 3 Security Guide** (base-security, 4,346 words)
- **TIU*1*325 DIBR** (installation-guide, 4,019 words)

---

<a id="roev"></a>
## ROEV — Release of Information — Electronic Verification

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | August 2015 |
| Total Pages | 44 |
| Total Words | 5,378 |
| Total Tables | 12 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 1 |

### Notable Documents

- **Military Eye Vision Injury Version 1 User Guide** (user-manual, 7,413 words)

---

<a id="ror"></a>
## ROR — VistA Cancer Registry

[Back to TOC](#table-of-contents)

The Clinical Case Registries (CCR) application obtains demographic and clinical data on VHA patients with specific clinical conditions.CCR is designed to search and provide reports on patient data in multiple registries.This assists clinical staff in supporting a variety of clinical conditions or disease states in VHA patients.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 14 |
| Date Range | May 2017 → June 2024 |
| Total Pages | 312 |
| Total Words | 39,785 |
| Total Tables | 365 |
| Total Figures | 0 |
| Total Appendices | 4 |
| Update Density | 1.8 docs/yr |
| Knowledge Ratio | 7% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 13 |
| user-manual | 1 |

### Notable Documents

- **ROR*1.5*42 User Manual** (user-manual, 84,886 words)
- **ROR*1.5*31 Release Notes** (release-note, 2,865 words)
- **ROR*1.5*33 Release Notes** (release-note, 2,655 words)
- **ROR*1.5*34 Release Notes** (release-note, 2,454 words)
- **ROR*1.5*32 Release Notes** (release-note, 2,307 words)

---

<a id="rt"></a>
## RT — Record Tracking

[Back to TOC](#table-of-contents)

The Record Tracking module provides for the maintenance and control of hardcopy health records and x-ray films to facilitate availability to a variety of users.The system offers a wide range of individual site-definable parameters so that it may be custom-tailored to specific needs and used in any type of file setting.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | November 1991 |
| Total Pages | 222 |
| Total Words | 49,388 |
| Total Tables | 12 |
| Total Figures | 0 |
| Total Appendices | 1 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Record Tracking Version 1 User Manual** (user-manual, 37,027 words)
- **Record Tracking Version 1 Technical Manual** (technical-manual, 7,486 words)
- **Record Tracking Version 1 Release Notes** (release-note, 2,820 words)
- **Record Tracking Version 1 Installation Guide** (installation-guide, 2,648 words)

---

<a id="sd"></a>
## SD — Scheduling

[Back to TOC](#table-of-contents)

Legacy Primary Care Management Module (PCMM GUI) is no longer in use and has been replaced by Patient Centered Management Module (PCMM Web), VASI 1530.

Legacy PCMM and PCMM Web both share the same VASI Identification number of 1530.

PCMM allows users to create, manage, and define teams and assign staff to these teams. This function helps in maintaining accurate listings for primary care teams and panels.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 345 |
| Date Range | September 2009 → March 2026 |
| Total Pages | 5,044 |
| Total Words | 662,108 |
| Total Tables | 2,548 |
| Total Figures | 1,292 |
| Total Appendices | 59 |
| Update Density | 8.5 docs/yr |
| Knowledge Ratio | 59% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 133 |
| release-note | 72 |
| installation-guide | 69 |
| user-manual | 68 |
| base-setup | 1 |
| unknown | 1 |
| base-security | 1 |

### Notable Documents

- **SD PIMS Version 5.3 Technical Manual** (technical-manual, 120,080 words)
- **PIMS Version 5.3 Registration Menu User Manual (Updated DG*5.3*858)** (user-manual, 44,260 words)
- **VistA Scheduling Enhancement (VSE) GUI 1.6 User Guide Addendum** (user-manual, 41,000 words)
- **VistA Scheduling Enhancement (VSE) GUI 1.6 Technical Manual** (technical-manual, 34,963 words)
- **Integrated Scheduling Solution (ISS) User Guide** (user-manual, 23,528 words)

---

<a id="spn"></a>
## SPN — Surgery Wait List

[Back to TOC](#table-of-contents)

SCIDO was decommissioned on Jan 28, 2016.

The Spinal Cord Injury and Disorders Outcomes (SCIDO) 3.0 application converts the Spinal Cord Dysfunction (SCD) Registry from a legacy command line system to a client server platform with a graphical user interface (GUI) and enhanced capabilities.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | February 2011 → May 2011 |
| Total Pages | 163 |
| Total Words | 33,636 |
| Total Tables | 30 |
| Total Figures | 0 |
| Total Appendices | 5 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 33% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| release-note | 1 |
| user-manual | 1 |

### Notable Documents

- **SCIDO Version 3 User Manual** (user-manual, 35,668 words)
- **SCIDO Version 3 Installation Guide** (installation-guide, 6,465 words)
- **SCIDO Version 3 Release Notes** (release-note, 3,736 words)

---

<a id="sqli"></a>
## SQLI — Structured Query Language Interface

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | October 1997 |
| Total Pages | 14 |
| Total Words | 28,765 |
| Total Tables | 87 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |

### Notable Documents

- **DI*21*38 Site Manual** (user-manual, 19,565 words)
- **DI*21*38 Vendor Guide DRAFT** (user-manual, 18,989 words)

---

<a id="sr"></a>
## SR — Surgery

[Back to TOC](#table-of-contents)

The Surgery package is designed to be used by Surgeons, Surgical Residents, Anesthetists, Operating Room Nurses, and other surgical staff. The Surgery package is part of the patient information system that stores data on the Department of Veterans Affairs (VA) patients who have, or are about to undergo, surgical procedures. This package integrates booking, clinical, and patient data to provide a variety of administrative and clinical reports.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 34 |
| Date Range | July 1993 → July 2024 |
| Total Pages | 4,879 |
| Total Words | 398,671 |
| Total Tables | 1,707 |
| Total Figures | 0 |
| Total Appendices | 10 |
| Update Density | 0.9 docs/yr |
| Knowledge Ratio | 18% |

### Document Types

| Type | Count |
|------|-------|
| change-page | 16 |
| release-note | 12 |
| user-manual | 3 |
| technical-manual | 2 |
| supplement | 1 |

### Notable Documents

- **Surgery Version 3 User Manual (Updated SR*3*184)** (user-manual, 116,832 words)
- **Surgery User Manual (SR*3.0*205)** (user-manual, 116,514 words)
- **Surgery User Manual (SR*3.0*200)** (user-manual, 112,677 words)
- **SR*3*175 Surgery VASQIP 2011 User Manual Change Pages** (change-page, 32,582 words)
- **SR*3*184 Surgery User Manual Change Pages** (change-page, 28,640 words)

---

<a id="sra"></a>
## SRA — Spinal Cord Dysfunction

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | June 2024 |
| Total Pages | 178 |
| Total Words | 15,694 |
| Total Tables | 76 |
| Total Figures | 0 |
| Total Appendices | 4 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Surgery Risk Assessment Version 3 Technical Manual** (technical-manual, 33,064 words)
- **Surgery Risk Assessment Version 3 User Manual** (user-manual, 9,203 words)
- **Surgery Risk Assessment SRA*3.0*9 Release Notes** (release-note, 1,287 words)

---

<a id="sts"></a>
## STS — Standards and Terminology Services

[Back to TOC](#table-of-contents)

STS is the authoritative source for clinical and administrative data standards for VHA.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | December 2010 → August 2011 |
| Total Pages | 103 |
| Total Words | 17,231 |
| Total Tables | 65 |
| Total Figures | 48 |
| Total Appendices | 4 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |
| base-setup | 1 |

### Notable Documents

- **STS Version 11 VETS 11 User Guide** (user-manual, 12,025 words)
- **STS Version 1 Technical Manual** (technical-manual, 7,451 words)
- **STS Version 2 VETS 10 Set Up Guide** (base-setup, 6,035 words)

---

<a id="tbi"></a>
## TBI — Traumatic Brain Injury

[Back to TOC](#table-of-contents)

[Per the VTWG on 1/26/2021 per VASI IO and Business Owner to make this system a component of Registries Platform (VIRP) - #2188.]Traumatic Brain Injury (TBI) Registry allows identification and tracking of Veterans who sustained head injuries during active duty.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | July 2015 → May 2018 |
| Total Pages | 346 |
| Total Words | 29,455 |
| Total Tables | 214 |
| Total Figures | 0 |
| Total Appendices | 10 |
| Update Density | 0.7 docs/yr |
| Knowledge Ratio | 57% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| unknown | 1 |
| installation-guide | 1 |
| release-note | 1 |
| technical-manual | 1 |

### Notable Documents

- **TBI Version 4.2 User Manual** (user-manual, 36,667 words)
- **TBI Version 4.2 Polytrauma User Manual** (user-manual, 28,669 words)
- **TBI Version 4.2 Instruments User Manual** (user-manual, 14,670 words)
- **TBI Version 4.2 Release Notes** (release-note, 1,949 words)
- **TBI Version 4.2 Installation Guide** (installation-guide, 1,596 words)

---

<a id="tiu"></a>
## TIU — Text Integration Utilities

[Back to TOC](#table-of-contents)

Text Integration Utilities (TIU) simplifies the use and management of clinical documents for both clinical and administrative medical facility personnel. Along with Authorization/Subscription Utility (ASU), a facility can set up policies and practices for determining who is responsible or has the privilege for performing various actions on required documents.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 12 |
| Date Range | July 1997 → December 2025 |
| Total Pages | 974 |
| Total Words | 143,559 |
| Total Tables | 188 |
| Total Figures | 7 |
| Total Appendices | 13 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 58% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 4 |
| user-manual | 3 |
| base-hl7 | 1 |
| quick-ref | 1 |
| technical-manual | 1 |
| release-note | 1 |
| base-impl | 1 |

### Notable Documents

- **TIU Technical Manual (TIU*1.0*372)** (technical-manual, 70,220 words)
- **TIU Clinical Coordinator and User Manual (TIU*1.0*364)** (user-manual, 62,802 words)
- **TIU/ASU Implementation Guide** (base-impl, 49,995 words)
- **TIU Generic HL7 Interface Handbook** (base-hl7, 27,185 words)
- **TIU/ASU Installation Guide** (installation-guide, 7,258 words)

---

<a id="tmp"></a>
## TMP — Telehealth Management Platform

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 56 |
| Date Range | August 2019 → July 2025 |
| Total Pages | 2,126 |
| Total Words | 324,322 |
| Total Tables | 1,347 |
| Total Figures | 223 |
| Total Appendices | 43 |
| Update Density | 4.4 docs/yr |
| Knowledge Ratio | 48% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 24 |
| technical-manual | 14 |
| user-manual | 13 |
| unknown | 3 |
| release-note | 2 |

### Notable Documents

- **TMP Version 8.0 VistA Patch 812 PIMS Technical Manual** (technical-manual, 90,903 words)
- **TMP Version 7.0 VistA Patch 810 PIMS Technical Manual** (technical-manual, 86,473 words)
- **TMP Version 6.0 Release 4.9.0.9 PIMS TM** (unknown, 86,472 words)
- **TMP Version 5.0 VistA Patch 806 PIMS Technical Manual** (technical-manual, 85,618 words)
- **TMP Version 4.0 Release 4.9.0.8 PIMS TM** (technical-manual, 84,990 words)

---

<a id="valm"></a>
## VALM — List Manager

[Back to TOC](#table-of-contents)

The List Manager was developed to provide an efficient way for applications to present a list of items to the user for action.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 1 |
| Date Range | March 2025 |
| Total Pages | 70 |
| Total Words | 16,484 |
| Total Tables | 13 |
| Total Figures | 16 |
| Total Appendices | 1 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| base-dev | 1 |

### Notable Documents

- **List Manager 1.0 Developer's Guide** (base-dev, 19,264 words)

---

<a id="vap"></a>
## VAP — Vendor Access Portal

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | August 2018 → August 2020 |
| Total Pages | 272 |
| Total Words | 46,850 |
| Total Tables | 89 |
| Total Figures | 266 |
| Total Appendices | 4 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 2 |

### Notable Documents

- **VAP Version 1 User Guide** (user-manual, 50,772 words)
- **VHIE Portal User Guide** (user-manual, 10,230 words)

---

<a id="vaq"></a>
## VAQ — Patient Data Exchange

[Back to TOC](#table-of-contents)

Patient Data Exchange (PDX) is a VistA module designed to electronically request and receive patient demographics, episodes of care, medications, and diagnostic evaluations from other VA facilities.Data is retrieved from files at the remote site and is assembled into a coherent, composite record, greatly enhancing the quality of care provided for the patient.

PDX has been moved to System Component/Application for VASI #1806: VistA - Integrated Billing; 1800: VistA - Health Summary

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | November 1993 → August 2018 |
| Total Pages | 163 |
| Total Words | 31,109 |
| Total Tables | 67 |
| Total Figures | 65 |
| Total Appendices | 8 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **PDX V. 1.5 User Manual** (user-manual, 31,220 words)
- **PDX V. 1.5 Release Notes Installation Guide** (installation-guide, 9,232 words)
- **PDX V. 1.5 Technical Manual** (technical-manual, 6,163 words)

---

<a id="vdef"></a>
## VDEF — VistA Data Extraction Framework

[Back to TOC](#table-of-contents)

VistA Data Extraction Framework (VDEF) is a VistA package that uses hard-coded M routines to create and deliver Health Level 7 (HL7) messages.VDEF isa data-driven scripting tool for automated HL7 message generation.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | December 2004 → June 2019 |
| Total Pages | 45 |
| Total Words | 17,620 |
| Total Tables | 48 |
| Total Figures | 8 |
| Total Appendices | 9 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 25% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 2 |
| technical-manual | 1 |
| unknown | 1 |

### Notable Documents

- **VDEF Version 1 Installation and User Configuration Guide** (installation-guide, 8,327 words)
- **VDEF Version 1 Technical Manual** (technical-manual, 6,280 words)
- **VDEF*1*15 HDR/CHDR Deployment, Installation, Back-Out, and Rollback** (installation-guide, 4,970 words)
- **VDEF VistA Messaging Overview 100105** (unknown, 1,764 words)

---

<a id="ves"></a>
## VES — Veterans Enrollment System

[Back to TOC](#table-of-contents)

Enrollment System (ES) defines health benefit plans for which a client (Veteran, Service member, and beneficiary) is eligible and ties them to the authority for care. Eligibility is derived from Client enrollment applications, Military Service Information, rating decisions, financial information, and other factors.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 95 |
| Date Range | March 2018 → December 2025 |
| Total Pages | 928 |
| Total Words | 161,452 |
| Total Tables | 428 |
| Total Figures | 504 |
| Total Appendices | 0 |
| Update Density | 8.6 docs/yr |
| Knowledge Ratio | 29% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 67 |
| user-manual | 21 |
| supplement | 7 |

### Notable Documents

- **VES Version 5.10 Production Operations Manual** (supplement, 7,060 words)
- **VES Version 5.9 Production Operations Manual** (supplement, 6,866 words)
- **VES Version 5.8 Production Operations Manual** (supplement, 6,846 words)
- **VES Version 5.3 Production Operations Manual** (supplement, 6,828 words)
- **VES Version 5.7 Production Operations Manual** (supplement, 6,799 words)

---

<a id="vhic"></a>
## VHIC — Veteran Health Identification Card

[Back to TOC](#table-of-contents)

The VHIC serves as an identification mechanism for Veterans enrolled in the VA Healthcare system and supports efficiencies at VA medical facilities throughout the United States. Although not required by Veterans to receive medical care at a VA facility, it does enable Veterans to check in for VA appointments more quickly.The VHIC system is a web-based application that is used to issue VHICs to enrolled Veterans.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | May 2012 → May 2024 |
| Total Pages | 258 |
| Total Words | 35,439 |
| Total Tables | 44 |
| Total Figures | 361 |
| Total Appendices | 0 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 5 |
| release-note | 4 |
| installation-guide | 1 |

### Notable Documents

- **VHIC 4.29 User Guide Vol 2 Reports** (user-manual, 15,114 words)
- **VHIC 4.29 User Guide Vol 1 Card Requests - All Users** (user-manual, 13,895 words)
- **VHIC 4.29 User Guide Vol 4 Troubleshooting** (user-manual, 5,445 words)
- **VHIC 4.29 User Guide Vol 6 Self Service Processing** (user-manual, 4,193 words)
- **VISTA VIC 4.0 Patch Installation Guide** (installation-guide, 2,129 words)

---

<a id="viab"></a>
## VIAB — VistA Integration Adapter Broker

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 4 |
| Date Range | June 2016 → May 2019 |
| Total Pages | 48 |
| Total Words | 9,747 |
| Total Tables | 7 |
| Total Figures | 3 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 25% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 3 |
| user-manual | 1 |

### Notable Documents

- **VistA Integration Adapter (VIAB) Version 1 VIP User Guide** (user-manual, 3,288 words)
- **VIAB*1*14 DIBRO** (installation-guide, 2,522 words)
- **VIAB*1*9 DIBR** (installation-guide, 2,434 words)
- **VIAB*1*15 DIBR** (installation-guide, 2,372 words)

---

<a id="vpfs"></a>
## VPFS — Pharmacy Point of Sale

[Back to TOC](#table-of-contents)

The Integrated Patient Funds software automates the "bank-like" functionality that VA provides for patients to manage their personal funds while hospitalized in a VA medical facility.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 6 |
| Date Range | July 2020 |
| Total Pages | 214 |
| Total Words | 44,359 |
| Total Tables | 245 |
| Total Figures | 0 |
| Total Appendices | 19 |
| Update Density | 2.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 4 |
| release-note | 1 |
| installation-guide | 1 |

### Notable Documents

- **VPFS VistAMigrate Data Migration Version 1.2 Users Guide** (user-manual, 31,283 words)
- **VPFS Version 1.2 User Guide** (user-manual, 20,989 words)
- **VPFS Version 1.2 Systems Management Guide** (user-manual, 15,052 words)
- **VPFS Version 1.2 Install Guide** (installation-guide, 9,988 words)
- **PRPF*4*4 Data Diagnostics Patch User Guide** (user-manual, 7,751 words)

---

<a id="vpr"></a>
## VPR — Virtual Patient Record

[Back to TOC](#table-of-contents)

Virtual Patient Record (VPR) is a foundation software package component of the Health Management Platform architecture. This architecture is part of the scope of the Health Informatics Initiative. VPR is not a product but a routine to extract data for Virtual Patient Record (VPR) to retrieve VistA data to support the HealthShare (HS) interface engine.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | September 2011 → January 2024 |
| Total Pages | 208 |
| Total Words | 20,662 |
| Total Tables | 108 |
| Total Figures | 38 |
| Total Appendices | 1 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| base-dev | 1 |
| installation-guide | 1 |
| technical-manual | 1 |

### Notable Documents

- **Virtual Patient Record (VPR) Developer's Guide** (base-dev, 42,354 words)
- **Virtual Patient Record (VPR) Technical Manual** (technical-manual, 9,016 words)
- **Virtual Patient Record (VPR) Installation Guide** (installation-guide, 1,088 words)

---

<a id="wii"></a>
## WII — Wounded, Injured and Ill Veterans

[Back to TOC](#table-of-contents)

Wounded Injured and Ill Warriors (WII) module was developed to provide accurate and timely personnel and health related data to the Department of Defense/Defense Finance and Accounting Service (DoD/DFAS) supporting adequate maintenance of pay and entitlements for all wounded warriors.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | February 2009 |
| Total Pages | 46 |
| Total Words | 6,848 |
| Total Tables | 9 |
| Total Figures | 1 |
| Total Appendices | 5 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 100% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **WII Version 1.1 Technical Manual** (technical-manual, 10,885 words)
- **WII Version 1.1 User Manual** (user-manual, 8,247 words)

---

<a id="wv"></a>
## WV — Women's Health

[Back to TOC](#table-of-contents)

The Women's Health (WH) application provides tracking functionality for procedures of particular interest to women patients (e.g., screening mammogram). The application provides a full range of breast and gynecologic cancer screening and tracking functions.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | September 1998 → May 2023 |
| Total Pages | 159 |
| Total Words | 40,577 |
| Total Tables | 8 |
| Total Figures | 0 |
| Total Appendices | 3 |
| Update Density | 0.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |
| user-manual | 1 |

### Notable Documents

- **Women's Health Version 1 User Manual** (user-manual, 35,834 words)
- **Women's Health Version 1 Technical Manual and Package Security Guide** (technical-manual, 7,917 words)
- **Women's Health Version 1 Installation Guide** (installation-guide, 1,701 words)

---

<a id="xm"></a>
## XM — MailMan

[Back to TOC](#table-of-contents)

The VistA Mailman software is designed to allow users to send and receive mail from individuals or groups electronically through communication lines, modems, and other networks.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 10 |
| Date Range | August 2002 → June 2017 |
| Total Pages | 176 |
| Total Words | 211,197 |
| Total Tables | 728 |
| Total Figures | 60 |
| Total Appendices | 7 |
| Update Density | 0.2 docs/yr |
| Knowledge Ratio | 60% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| quick-ref | 2 |
| release-note | 2 |
| installation-guide | 1 |
| technical-manual | 1 |
| unknown | 1 |

### Notable Documents

- **MailMan Version 8 User Guide** (user-manual, 111,555 words)
- **MailMan Version 8 Technical Manual** (technical-manual, 51,602 words)
- **MailMan Version 8 Systems Management Guide** (user-manual, 37,334 words)
- **MailMan Version 8 Network Reference Guide** (user-manual, 26,832 words)
- **MailMan Version 8 Getting Started Guide** (quick-ref, 25,147 words)

---

<a id="xobe"></a>
## XOBE — Enterprise Service Bus Adapter

[Back to TOC](#table-of-contents)

The Electronic Signature (ESig) service provides an interim solution for the use of electronic codes during certain VistA security infrastructure and architecture evolutions. Changed to System Component of 1973: VistA.Contains the M-side portion of the electronic signature methods for rehosted applications that validate, store, and retrieve electronic signature data.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 3 |
| Date Range | November 2006 |
| Total Pages | 71 |
| Total Words | 11,935 |
| Total Tables | 56 |
| Total Figures | 0 |
| Total Appendices | 2 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| base-dev | 1 |
| installation-guide | 1 |
| user-manual | 1 |

### Notable Documents

- **Electronic Signature (ESig) Version 1 Developer's Guide** (base-dev, 8,515 words)
- **Electronic Signature (ESig) Version 1 Installation Guide** (installation-guide, 4,457 words)
- **Electronic Signature (ESig) Version 1 Systems Management Guide** (user-manual, 4,348 words)

---

<a id="xobv"></a>
## XOBV — VistALink Systems Management

[Back to TOC](#table-of-contents)

VistALink enables applications to communicate with VistA/M systems. It provides a synchronous communication mechanism from Java-based applications to M.

VistALink is now a System Component/Service for VASI #1778: ADT; and VASI#1525: VBECS

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 13 |
| Date Range | May 2006 → March 2022 |
| Total Pages | 226 |
| Total Words | 132,243 |
| Total Tables | 340 |
| Total Figures | 24 |
| Total Appendices | 15 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 46% |

### Document Types

| Type | Count |
|------|-------|
| release-note | 4 |
| base-dev | 3 |
| installation-guide | 3 |
| user-manual | 3 |

### Notable Documents

- **VistALink Version 1.6 System Management Guide** (user-manual, 23,305 words)
- **VistaLink Version 1.6.7 System Management Guide** (user-manual, 23,218 words)
- **VistALink Version 1.5 Installation Guide** (installation-guide, 18,770 words)
- **VistALink Version 1.6 Developer Guide** (base-dev, 18,304 words)
- **VistaLink Version 1.6.7 Developer Guide** (base-dev, 18,225 words)

---

<a id="xobw"></a>
## XOBW — Web Services Client

[Back to TOC](#table-of-contents)

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | February 2011 → August 2020 |
| Total Pages | 95 |
| Total Words | 34,030 |
| Total Tables | 45 |
| Total Figures | 43 |
| Total Appendices | 6 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 43% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 3 |
| base-dev | 1 |
| user-manual | 1 |
| release-note | 1 |
| base-security | 1 |

### Notable Documents

- **HealtheVet Web Services Client (HWSC) Version 1 Developer's Guide** (base-dev, 14,384 words)
- **HealtheVet Web Services Client (HWSC) Version 1 Installation Guide** (installation-guide, 7,910 words)
- **HealtheVet Web Services Client (HWSC) Version 1 Systems Management Guide** (user-manual, 5,741 words)
- **XOBW*1*4 Installation, Back-Out, and Rollback Guide** (installation-guide, 5,552 words)
- **XOBW*1*4 Security Configuration Guide** (base-security, 4,618 words)

---

<a id="xqor"></a>
## XQOR — Order Checking

[Back to TOC](#table-of-contents)

The Kernel Unwinder is a utility that is used in conjunction with the Protocol file (#101) to create modular building blocks for applications. This is an application module underVistA - Kernel (Kernel) - VASI#2364

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 2 |
| Date Range | August 1994 |
| Total Pages | 29 |
| Total Words | 6,177 |
| Total Tables | 4 |
| Total Figures | 0 |
| Total Appendices | 0 |
| Update Density | 1.0 docs/yr |
| Knowledge Ratio | 50% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 1 |
| technical-manual | 1 |

### Notable Documents

- **XQOR Technical Manual** (technical-manual, 6,136 words)
- **XQOR Installation Guide** (installation-guide, 277 words)

---

<a id="xt"></a>
## XT — Toolkit

[Back to TOC](#table-of-contents)

Kernel Toolkit (also referred to as "Toolkit") supplements the Kernel software package. It provides Development and Quality Assessment Tools and System Management Utilities.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 7 |
| Date Range | April 1995 → April 2021 |
| Total Pages | 275 |
| Total Words | 59,269 |
| Total Tables | 162 |
| Total Figures | 111 |
| Total Appendices | 3 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 71% |

### Document Types

| Type | Count |
|------|-------|
| technical-manual | 2 |
| supplement | 2 |
| release-note | 1 |
| installation-guide | 1 |
| user-manual | 1 |

### Notable Documents

- **VistA Package Size Reporting Tool (VPSRT) User Guide (XT*7.3*143)** (user-manual, 27,285 words)
- **Kernel Toolkit Technical Manual: Currently being absorbed by Kernel Technical Manual** (technical-manual, 23,744 words)
- **XT*7.3*98 VistA Patch Monitor, Supplement to Patch Desc** (supplement, 15,126 words)
- **XT*7.3*26 Parameter Tools Supplement to Patch Description** (supplement, 8,668 words)
- **VistA Package Size Reporting Tool (VPSRT) Technical Manual (XT*7.3*143)** (technical-manual, 8,493 words)

---

<a id="xu"></a>
## XU — Kernel

[Back to TOC](#table-of-contents)

A common service and a project of HealtheVet Security Services, Fat Client Kernel Authentication and Authorization (FatKAAT) provides user authentication and authorization for J2EE applications with a rich client user interface.

2/4/16 - Per VASI OOR TF, changed to System Component of 1973: VistA

FatKAAT is for rich-client HealtheVet applications like CPRS-R, HealtheVet Desktop, and RSA.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 71 |
| Date Range | April 1995 → August 2025 |
| Total Pages | 2,609 |
| Total Words | 739,225 |
| Total Tables | 1,156 |
| Total Figures | 1,380 |
| Total Appendices | 56 |
| Update Density | 0.4 docs/yr |
| Knowledge Ratio | 77% |

### Document Types

| Type | Count |
|------|-------|
| base-dev | 31 |
| user-manual | 10 |
| installation-guide | 9 |
| base-security | 7 |
| supplement | 5 |
| release-note | 4 |
| unknown | 3 |
| technical-manual | 1 |
| quick-ref | 1 |

### Notable Documents

- **Kernel 8.0 Developerâ€™s Guide: Binder** (base-dev, 194,822 words)
- **Kernel 8.0 Systems Management: Binder** (user-manual, 165,826 words)
- **Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual** (technical-manual, 93,447 words)
- **XU*8*671 Assigning Person Class to Providers User Guide** (supplement, 51,143 words)
- **Kernel 8.0 Systems Management: Utilities User Guide** (user-manual, 37,072 words)

---

<a id="xwb"></a>
## XWB — RPC Broker

[Back to TOC](#table-of-contents)

The Veterans Health Administration uses CCOW to share patient and user context between applications. Clinical Context Management is a method used to synchronize multiple GUI clinical computer applications to one subject, for example, the same patient.

Per VHA SIM POCs, this is not a system.CCOW is the HL7 standard for clinical context management.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 9 |
| Date Range | October 1997 → September 2021 |
| Total Pages | 459 |
| Total Words | 99,369 |
| Total Tables | 188 |
| Total Figures | 161 |
| Total Appendices | 1 |
| Update Density | 0.1 docs/yr |
| Knowledge Ratio | 67% |

### Document Types

| Type | Count |
|------|-------|
| user-manual | 3 |
| release-note | 2 |
| installation-guide | 1 |
| base-dev | 1 |
| technical-manual | 1 |
| supplement | 1 |

### Notable Documents

- **XWB*1.1*73 Developer's Guide** (base-dev, 60,973 words)
- **XWB*1.1*73 User Guide** (user-manual, 17,375 words)
- **XWB*1.1*73 Technical Manual** (technical-manual, 15,377 words)
- **XWB*1.1*73 Systems Management Guide** (user-manual, 12,889 words)
- **M-to-M Broker XWB*1.1*34 Supplement to Patch Description** (supplement, 12,822 words)

---

<a id="ys"></a>
## YS — Mental Health

[Back to TOC](#table-of-contents)

VTWG on 10/20/2020 the system is marked INACTIVE per request. Interface for historical lookup of Medical Opinions on Mental Health Claims. Business is considering discontinuing service. TheMental Health module provides computer support for both clinical and administrative patient care activities associated with mental health care.

### Documentation Statistics

| Metric | Value |
|--------|-------|
| Total Documents | 78 |
| Date Range | December 1994 → July 2025 |
| Total Pages | 11,039 |
| Total Words | 283,415 |
| Total Tables | 569 |
| Total Figures | 301 |
| Total Appendices | 66 |
| Update Density | 2.1 docs/yr |
| Knowledge Ratio | 17% |

### Document Types

| Type | Count |
|------|-------|
| installation-guide | 55 |
| release-note | 10 |
| user-manual | 8 |
| technical-manual | 2 |
| base-security | 1 |
| base-dev | 1 |
| supplement | 1 |

### Notable Documents

- **Mental Health Assistant Phase 3 User Manual** (user-manual, 33,301 words)
- **Mental Health Assistant Phase 3 Security Technical Manual/Security Guide** (technical-manual, 26,149 words)
- **YS*5.01*76 Mental Health Assistant Phase 2 User Manual** (user-manual, 25,035 words)
- **Mental Health Version 5.01 Installation Guide  Release Notes** (installation-guide, 18,487 words)
- **High Risk Mental Health Patient - Patient Record Flags User Guide** (user-manual, 17,894 words)

---
