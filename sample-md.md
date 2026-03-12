# PXRM install guide — different structure from user manuals
head -120 vista-docs/docs/PXRM/pxrm_2_19_ig.md
---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
library_max_patch: null
package_id: PXRM
patch: 176
patch_gap: null
section: ''
source_file: pxrm_2_19_ig.docx
status: draft
title: pxrm 2 19 ig.docx
---

<!-- image -->

**Home Telehealth (HT)**

**PXRM*2*19 TIU*1*258 GMTS*2.7*98**

**INSTALLATION and SETUP GUIDE**

**July 2017**

**Department of Veterans Affairs Office of Information &amp; Technology (OI&amp;T)**

**Enterprise Program Management Office (EPMO)**

Contents

INTRODUCTION    1

Web Sites       11

Getting Help    11

PRE-INSTALLATION        12

Required Software for PXRM*2*19 12

Estimated Installation Time: approximately 20 minutes   12

NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them. 12

INSTALLATION    14

1. Retrieve host file containing the multi-package build and zip file containing new TXML templates.14 2. Install the build first in a training or test account    14

1. Load the distribution.       14
    1. Backup a Transport Global        14
    2. Compare Transport Global to Current System       15
    3. Verify Checksums in Transport Global     15
    4. Print Transport Global (optional)        15
2. Install the build.   15
3. Install File Print   15
4. Build File Print     16
5. Post-Install Routines        16
6. Deletion of init routines    17

SET-UP  18

Setup Instructions – Summary Steps      21

Setup Instructions – Detailed Steps     26

1. Create a new user class in for your HT clinicians    26
2. Edit your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be HT TEMPLATES     26
3. Expand the HT\_TXML\_TEMPLATES.ZIP file to a known location. 26
4. Create GUI dialogs for the HT reminder dialogs       26
5. Verify that the four new HT clinical reminders launch (reminder dialogs linked) from the Reminders drawer    29
6. Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT      31
7. Configure two new Health Summary types for the CPRS GUI Reports tab. 33
8. Assign the TIU HT MENU and (optional) PXRM HT DEFINITION EDIT to CAC(s)      33
9. Link the HT templates to NOTE TITLES 33
10. (Optional for all sites) If you need to change the FREQUENCY of the HT PERIODIC EVALUATION. 35
11. Build the 5 reminder report templates and do sample runs of each, with a short date range.  36

APPENDIX A: FILE ENTRY DELETE AND POINTER UPDATE        51

APPENDIX B: CROSSWALK FROM CCHT PILOT TO NATIONAL RELEASE       57

APPENDIX C: HT QUEUED MAILMAN REPORT    69

APPENDIX D: CONTENTS OF THE PACKED REMINDER EXPORT HT TEMPLATES/REMINDERS SET   86

APPENDIX E: CLINIC CROSSWALK    96

APPENDIX F: INSTALLATION EXAMPLE        99

APPENDIX G: FILEMAN SEARCHES FOR HT PILOT SITES 105

APPENDIX H: HEALTH FACTORS      119

7/12/2017       Home Telehealth Templates Installation Guide    iii

APPENDIX I: HEALTH FACTORS (ALPHA SORT W/ CATEGORY)     123

APPENDIX J: EDUCATION TOPICS    126

APPENDIX K: ACRONYMS AND GLOSSARY       127

ACRONYMS        128

Glossary        129

##### Introduction

The purpose of this project is to release new national reminders and reminder dialogs that will be used by Care Coordinators (Nurses, Social Workers, Rehab Specialists, Dietitians, Pharmacists and Psychologists) managing patients enrolled in HT programs.

The National Office of Connected Care (10P8) wishes to have a comprehensive, integrated template set in use at all VA facilities caring for Home Telehealth patients.

####### NOTE: These national patches and subsequent template set originated as the Care Coordination Home Telehealth (CCHT) Phase III Pilot program executed over several years at a small number of VA Medical Centers. As such, there are some steps in this document that should only apply to former pilot sites and some steps that apply only to non-pilot sites. These steps are marked accordingly.








 # GMRV change pages — patch-era partial doc
head -120 vista-docs/docs/GMRV/vitl_5_p23_um_change_pages.md
---
app_name: Vitals/Measurements (GMRV)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
library_max_patch: null
package_id: GMRV
patch: null
patch_gap: null
section: ''
source_file: vitl_5_p23_um_change_pages.docx
status: draft
title: vitl 5 p23 um change pages.docx
---

#### September 2009

This distribution contains change pages for patch GMRV*5.0*23 of the Vitals / Measurements User Manual.

The change pages for Vitals / Measurements Patch 22 (GMRV*5.0*22, revised June 2008) should be inserted before the change pages for GMRV Patch 23.

File Name:      Patch:

VITL\_5\_P22\_UM.PDF    GMRV*5.0*22

Patch GMRV*5.0*23 pages:

Replace Pages:  With Pages:

Title Page      Title Page

Revision History        Revision History

Table of Contents       Table of Contents

1-1 to 1-4      1-1 to 1-4

2-1 to 2-10     2-1 to 2-10

3-3 to 3-6      3-3 to 3-6

4-3 to 4-20     4-3 to 4-22

5-1 to 5-4      5-1 to 5-4

6-1 to 6-4      6-1 to 6-6

8-5 to 8-8      8-5 to 8-8

Index   Index

<!-- image -->

# Vitals / Measurements User Manual

**Version 5.0**

**October 2002**

Revised September 2009 GMRV*5.0*23

Department of Veterans Affairs Office of Information &amp; Technology Office of Enterprise Development

## Revision History

| **Date**           |   **Revision** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Author**   |
|--------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 1  September  2009 |           5.23 | Sections updated for Patch 23 (GMRV*5.0*23):  - updated Title Page - updated Revision History - updated Table of Contents - updated Introduction, page 1-2 and 1-4 - updated Using Vitals Manager, pages 2-2, 2-3, 2-4, 2-5, 2-7,  2-8, and 2-9  - updated Using Vitals, pages 3-3, and 3-4 - updated Entering Vitals Data, pages 4-3, 4-4, 4-6, 4-7, 4-10,  4-12, 4-14, 4-15, 4-16, and 4-21  - added ―Enter Vitals Menu Bar‖ section, page 4-8. - updated Reports, pages 5-2, 5-3, 5-4 - updated Appendix A – Access Key Listing, pages 6-2 - updated Appendix C – Using Vitals in CPRS, pages 8-5, 8-6, and 8-7             | REDACTED     |
| April 2006         |           5.3  | Sections updated for Patch 3 (GMRV*5.0*3):  - updated Title Page - updated Revision History - updated Table of Contents, all pages - updated Introduction, page 1-i, 1-2 - removed Implementation and Maintenance chapter - updated Using Vitals Manager, pages 2-2, 2-5, 2-6 - removed Package Operation chapter; replaced with new Using Vitals chapter, updated all pages - updated Entering Vitals Data, all pages - updated Reports, all pages - updated Appendix A, all pages - updated Appendix B, page 7-3, 7-4 - added Appendix C – Using Vitals in CPRS v26 - updated Glossary, all pages - updated Index, all pages | REDACTED     |
| October 2003       |           5.1  | Sections updated for Patch 1 (GMRV*5.0*1): Revision History  Table of Contents Site Files  Entering Vitals Data  Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED     |
| January 2002       |           5    | Initial Publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED     |

<!-- image -->

1 Patch GMRV*5.0*23 September 2009 Patch 23 release added.

*This page intentionally left blank for double-side printing.*

## Table of Contents

1. Introduction 1-1

Functionality   1-1

Information on GUI software     1-2

Adding Vitals to the Tools Menu in CPRS 1-5

1. Using Vitals Manager 2-1

Getting Started with Vitals Manager     2-1

Managing Vitals Categories and Qualifiers       2-2

Printing a Qualifiers Table     2-3

Editing Abnormal Values 2-3

Editing System Parameters       2-4

Creating/Editing a Template     2-6

1. Using Vitals 3-1

Getting Started with Vitals     3-1

Overview of the Vitals window   3-2

Editing User Options    3-3

About CCOW      3-4

Joining a Clinical Context      3-5





# PXRM multi-module user manual — largest category
head -120 vista-docs/docs/PXRM/pxrm_2_um.md
---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
library_max_patch: null
package_id: PXRM
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_um.docx
status: draft
title: pxrm 2 um.docx
---

<!-- image -->

**Clinical Reminders**

**High Risk Mental Health Patient – National Reminder and Flag**

## Patch 24

**User Manual**

### April 2013

Department of Veterans Affairs Office of Information and Technology (OIT)

Product Development

### Revision History

| **Date**     | **Page #**   | **Description**                                                                                 | **Project Manager**   | **Technical Writer**   |
|--------------|--------------|-------------------------------------------------------------------------------------------------|-----------------------|------------------------|
| March 2013   | Throughout   | Updates to include most recent examples                                                         | REDACTED              | REDACTED               |
| Oct 2012     | 7            | Added note about changing parameter for # of days in future  for nightly background job report. | REDACTED              | REDACTED               |
| Sept 2012    | 8            | Updates to Reminder dialogs                                                                     | REDACTED              | REDACTED               |
| Aug 2012     | 86           | Added Hints, Tips, and FAQs                                                                     | REDACTED              | REDACTED               |
| July 2012    | 59           | Added info about PRF Transmission Menu                                                          | REDACTED              | REDACTED               |
| July 2012    | 44           | Added info about MHTC Needs Assignment Reminder Definition                                      | REDACTED              | REDACTED               |
| May 2012     | 41           | Updated Scheduling No-Show and Ad Hoc reports                                                   | REDACTED              | REDACTED               |
| May 2012     | 8            | Updated dialog screenshots (to  include other dialog changes) for Phase 2 of HRMH project       | REDACTED              | REDACTED               |
| May 2012     | 44           | Added Health Summary info re MHTC and PRF                                                       | REDACTED              | REDACTED               |
| May 2012     | 4            | Added PRF information for Phase 2 of HRMH project                                               | REDACTED              | REDACTED               |
| January 2012 | 8 - 16       | Updated dialog screenshots                                                                      | REDACTED              | REDACTED               |
| Dec 2011     | 6, 41        | Edited Scheduling reports, per developer changes and product  support review.                   | REDACTED              | REDACTED               |
| Sep-Nov 11   | 41           | Added revised Scheduling Reports                                                                | REDACTED              | REDACTED               |
| June 2011    | Throughout   | Completely revised, to document High Risk Mental Health Patient  Reminder and Dialog project.   | REDACTED              | REDACTED               |

April 2013      High Risk Mental Health Patient – National Reminder &amp; Flag  ii

User Manual

## Table of Contents

Introduction    1

Related Documentation   2

Background      3

High Risk MH Patient Process Flow Overview      4

High Risk Mental Health Scheduling Reports      6

Documenting Results of Follow-up in a Reminder Dialog   9

High Risk MH No Show Follow-up Reminder 9

VA-MHTC Needs Assignment Reminder Definition    29

High Risk Mental Health Ad Hoc Scheduling Report Example        41

High Risk Mental Health Health Summary Components and Types     44

New Health Summary Types distributed by the High Risk Mental Health Patient project     48

Order Entry (OR) MHTC Notification      49

Scheduling Report Examples      53

Example of the High Risk Mental Health NO Show Ad Hoc report    56

Patient Record Flag Category I HIGH RISK FOR SUICIDE    59

Appendix A: Clinical Reminders and CPRS Overview        64

Processing/ Resolving Clinical Reminders        72

Appendix B: Glossary    75

Acronyms        75

Definitions     77

Appendix C: Edit Cover Sheet Reminder List      80

Appendix D: Creating a Mental Health Test button for use in a Reminder Dialog   84

Appendix E: Tips, Tricks, and FAQs      86

Table of Figures

Figure 1: Patient with a high risk for suicide Patient Record Flag      4

Figure 2- CPRS opened to Notes screen, with Clinical Reminders drawers showing  15

Figure 3: High Risk MH No-Show Follow-up Dialog Opening Screen  16

Figure 4: High Risk MH No-Show Follow-up Additional Information Screen  17

Figure 5: High Risk MH No-Show Follow-up Dialog, with Patient Contact selected  18