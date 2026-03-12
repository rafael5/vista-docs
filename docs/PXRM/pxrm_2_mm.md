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
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_mm.docx
status: draft
title: Clinical Reminders
---

# Clinical Reminders


# Manager’s Manual

<!-- image -->

(Revised September 2022)

**March 2005**

Product Development


## Preface

### Purpose of Manager’s Manual

This manual provides reference information for Clinical Reminders menus and options. It can serve both as a reference manual and a tutorial for Clinical Application Coordinators (CACs) and Clinical Reminders Managers who are just becoming familiar with Clinical Reminders.

To get further help information, please enter a Remedy ticket or call the National Help Desk.

### Recommended Users

- Clinical Reminders Managers
- Clinical Application Coordinators (CACs)
- Department of Veterans Affairs Medical Center (VAMC) Information Resources Management (IRM) staff

### Related Manuals

Clinical Reminders documentation can also be found in the VistA Software Document Library (VDL).

### Related Web Sites

| **Site**                              | **URL**   |
|---------------------------------------|-----------|
| National HSD&D Reminders site         | REDACTED  |
| Office of Quality, Safety, and Value  | REDACTED  |
| VA Software Document Library          | REDACTED  |
| VA/DoD Clinical Practice Guidelines   | REDACTED  |
| National Clinical Reminders Committee | REDACTED  |

## Revision History

| **Revision Date**     | **Page(s)**                                                                                                                                                                                                                                                                                                                                                                                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Project Authors**            |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| August 2022           | 1,3,17,  20  23-24,26-29,32-34,38  40-41,45,51,56,61,65-71,73-74,76,79-82,84,86-87,90,92,94-100,102-105  118,129,135  152,156  158,159    161-162,164-166,170,172-173,175-176  182,193,198, 203-204  206  208,214,219, 221-222, 227-228,235-236,241  248,255,258, 275-276,278, 280  281-282,284, 291-292, 294, 297, 299  309,388   342,344, 348, 354, 356-357  357,361  370   376  384-388    297-299 | PXRM*2.0*65: Over 25% of this manual was updated.  The following sections were updated:  - Introduction - Reminders Maintenance - Reminder Computed Finding Management - Reminder Definition Management - Reminder Sponsor Management - Value Sets - Reminder Location List Management - Reminder Exchange - Reminder Test - Reminder Information Only Menu - Reminder Dialog Management - CPRS Reminder Configuration Menu - Reminder Reports - Reminder Patient List Management - Reminder Extract Tools - Clinical Reminder Order Checks - Appendix A - Appendix B  Added the Appendix D – Contradictions, Precautions, and Refusals section.  Deleted the GEC Referral Reports Section since the GEC Referral Report is already in the Reminder Reports section. | CPRS Development Team          |
| May 2022              | 1  218                                                                                                                                                                                                                                                                                                                                                                                                | Patch 80 (PXRM*2.0*80) Changes -  This patch changes how Reminder Exchange packs up Reminder Dialogs  Changes made with PXRM*2.0*80 -  This modified Clinical Reminder Exchange functionality to not automatically packed up a reminder dialog under the following condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Department of Veterans Affairs |
| May 2021              | 1  127-135  135                                                                                                                                                                                                                                                                                                                                                                                       | PXRM*2.0*42 – Summary for patch PXRM*2.0*42  (The functionality was implemented in PXRM*2.0*46 but wasn’t documented until the PXRM*2.0*42 release.)  Added the Found Text/Not Found Text Details, CSUB Objects, Text Arguments, and Building Tables sections  Removed the Status List and Computed Finding Parameter descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED                       |
| January 2021          | various                                                                                                                                                                                                                                                                                                                                                                                               | Completed redaction items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                       |
| August 2020           |                                                                                                                                                                                                                                                                                                                                                                                                       | PXRM*2.0*45: Fixed footer issues and made the manual 508-compliant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| June 2020             | 2  v  209  220  221  222  227  232  359, 360                                                                                                                                                                                                                                                                                                                                                          | PXRM*2.0*45 – Summary for patch PXRM*2.0*45  Explanation of the Repack menu item  Added a short summary of items changed in PXRM*2.0*45  Changed Dialog Edit Options capture  Updated the Dialog Overview menu capture  Changed the Reminder Dialog Branching Logic  Added Reminder Dialog CPRS 32 Pre Conversion report to a list of reports  Added items to what is on the dialog checker report  Updated what the Order Check Item Group can contain                                                                                                                                                                                                                                                                                                              | REDACTED                       |
| December 2017         | 20-24                                                                                                                                                                                                                                                                                                                                                                                                 | PXRM*2.0*68 – Removed VA-MHV references.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                       |
| October  2017         | n/a                                                                                                                                                                                                                                                                                                                                                                                                   | PXRM*2.0*47 – Removed reference to Albany download site which has been decommissioned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                       |
| August 2016           | Various, 150                                                                                                                                                                                                                                                                                                                                                                                          | Updates based on review by developers. Minor changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                       |
| August 2016           | 63, 150                                                                                                                                                                                                                                                                                                                                                                                               | Added a comment that running the integrity check monthly or quarterly would be a best practice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                       |
| June 2016             | 150                                                                                                                                                                                                                                                                                                                                                                                                   | Added a section about Value Sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| June 2016             | 76, 76                                                                                                                                                                                                                                                                                                                                                                                                | Added two items under Finding Modifier description: Use Start Date and Include Visit Data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED                       |
| June 2016             | 312                                                                                                                                                                                                                                                                                                                                                                                                   | Made a small change to the section about List Rule Sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                       |
| June 2016             | 70, 81                                                                                                                                                                                                                                                                                                                                                                                                | Added an item about using a STATUS LIST with orderable items. And added to the section referencing using status/condition in searches.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                       |
| June 2016             | **v**  , 36                                                                                                                                                                                                                                                                                                                                                                                           | New Computed Findings: VA – Age Birth Sex List, VA-BIRTH DATE BIRTH SEX LIST,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                       |
| June 2016             | 163, 171                                                                                                                                                                                                                                                                                                                                                                                              | Added that Reminder Exchange files cannot be used from SharePoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED                       |
| June 2016             | 234                                                                                                                                                                                                                                                                                                                                                                                                   | Added to the section about the Dialog Taxonomy Editor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                       |
| June 2015             | 66                                                                                                                                                                                                                                                                                                                                                                                                    | PXRM*2.0*53 – Added that the Custom Due Date might also use the RANK_DATE function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| June 2015             | 3, 227                                                                                                                                                                                                                                                                                                                                                                                                | Added information about the Reminder Dialog Search report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED                       |
| August 2014           | Various                                                                                                                                                                                                                                                                                                                                                                                               | Updates based on developers’ reviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| June 2014             | Various                                                                                                                                                                                                                                                                                                                                                                                               | Updates based on developers’ reviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| April 2014            | 162                                                                                                                                                                                                                                                                                                                                                                                                   | Added changes made by PXRM*2*26 to Reminder Exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| Jan 2014              | 24                                                                                                                                                                                                                                                                                                                                                                                                    | Added changes made by PXRM*2*26 in Computed Findings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| Jan 2014              | 282                                                                                                                                                                                                                                                                                                                                                                                                   | Added changes made by PXRM*2*26 in Reports/Finding Usage Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                       |
| Jan 2014              | 91                                                                                                                                                                                                                                                                                                                                                                                                    | Added changes made by PXRM*2*26 in Function Findings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| Jan 2014              | Error! Bookmark not defined.                                                                                                                                                                                                                                                                                                                                                                          | Added changes made by PXRM*2*26 to Dialog Management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| Jan 2014              | 162                                                                                                                                                                                                                                                                                                                                                                                                   | Added changes made in Reminder Exchange  New Exchange action: Load Web Host File                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED                       |
| Aug 2013              | 246                                                                                                                                                                                                                                                                                                                                                                                                   | Added dialog taxonomy editor description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                       |
| April-June 2013       | 234                                                                                                                                                                                                                                                                                                                                                                                                   | Updated Dialog Management chapter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| April-June 2013       | 112                                                                                                                                                                                                                                                                                                                                                                                                   | Updated Taxonomy chapter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                       |
| February 2013         | 3, 112                                                                                                                                                                                                                                                                                                                                                                                                | Added description of PXRM*2*26 and changed Taxonomy chapter per changes made in PXRM*2*26 for the ICD-10 project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| Apr-Dec 2012          | Various                                                                                                                                                                                                                                                                                                                                                                                               | Added details about changes made for Patch 24 and phase 2 of the HRMHP project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED                       |
| Jan 2012              | App B, 375                                                                                                                                                                                                                                                                                                                                                                                            | Updated Appendix B, Order Check example for PXRM*2*22                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                       |
| Jan 2012              | 359                                                                                                                                                                                                                                                                                                                                                                                                   | Updated Order Check section for PXRM*2*22                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                       |
| Dec 2011              | n/a                                                                                                                                                                                                                                                                                                                                                                                                   | Added description of patch 21 and MSDS project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED                       |
| Dec 2011              | Various                                                                                                                                                                                                                                                                                                                                                                                               | Updates per reviews by Product Support team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                       |
| July 2011             | 95                                                                                                                                                                                                                                                                                                                                                                                                    | Added Function Findings primer by Product Support team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                       |
| Feb 2011              | Various                                                                                                                                                                                                                                                                                                                                                                                               | Added details about changes made for Patch 18 and HRMHP project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                       |
| January 2011          | 359                                                                                                                                                                                                                                                                                                                                                                                                   | Edited Order Check section, per Anthony Puleo and Rob Silverman,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED                       |
| December 2010         | 39                                                                                                                                                                                                                                                                                                                                                                                                    | Added computed finding example for VA-IS INPATIENT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED                       |
| November 2010         | 341                                                                                                                                                                                                                                                                                                                                                                                                   | Added Reminder Extracts section provided by Clinical Product Support                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| June 2010             | n/a                                                                                                                                                                                                                                                                                                                                                                                                   | Added description of Order Check menu and options, introduced in patch 16.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED                       |
| July 2009             | 162                                                                                                                                                                                                                                                                                                                                                                                                   | Updated patch 12 update section and Reminder Exchange section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                       |
| May 2009              | 208, 227                                                                                                                                                                                                                                                                                                                                                                                              | Updated Dialogs and Reports sections, per developer Review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED                       |
| May 2009              | 24                                                                                                                                                                                                                                                                                                                                                                                                    | Updated Computed Findings section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| December 2008         | 162                                                                                                                                                                                                                                                                                                                                                                                                   | Updated Reminder Exchange section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| December 2008         | 180                                                                                                                                                                                                                                                                                                                                                                                                   | Updated Reminder Test section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                       |
| December 2008         | 24                                                                                                                                                                                                                                                                                                                                                                                                    | Updated Computed Findings section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| September 2008        | n/a                                                                                                                                                                                                                                                                                                                                                                                                   | Added new computed findings descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                       |
| July 2008             | 300                                                                                                                                                                                                                                                                                                                                                                                                   | New report, Finding Usage Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED                       |
| October 2007          | 14                                                                                                                                                                                                                                                                                                                                                                                                    | Updated National Reminders list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                       |
| October 2007          | 161                                                                                                                                                                                                                                                                                                                                                                                                   | Added description of new option, Copy Location List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| October 2007          | Error! Bookmark not defined.                                                                                                                                                                                                                                                                                                                                                                          | Added description of new option, TIU Template Reminder Dialog Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                       |
| October 2007          | Error! Bookmark not defined.                                                                                                                                                                                                                                                                                                                                                                          | Updates to description of Mental Health Dialog functionality                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                       |
| October 2007          | 309                                                                                                                                                                                                                                                                                                                                                                                                   | Added description of new option, Edit Number of MH Questions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                       |
| September 2007        | 105                                                                                                                                                                                                                                                                                                                                                                                                   | Added new function finding, NUMERIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| June 2007             | Various                                                                                                                                                                                                                                                                                                                                                                                               | Changes per patch 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| September 2006        | 310-341                                                                                                                                                                                                                                                                                                                                                                                               | Changes to Patient Lists and Extract Management descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                       |
| May-June 2006         | 341                                                                                                                                                                                                                                                                                                                                                                                                   | Extract Management option changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                       |
| March 2006            | N/A                                                                                                                                                                                                                                                                                                                                                                                                   | Added descriptions of new computed findings for appointments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                       |
| February 2006         | 310                                                                                                                                                                                                                                                                                                                                                                                                   | Rewrite of Patient List section, based on changes to software and need for more explanation and clarification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                       |
| February 2006         | Page 341                                                                                                                                                                                                                                                                                                                                                                                              | Rewrite of Extract Management section, based on changes to software and need for more explanation and clarification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| January-February 2006 | Various                                                                                                                                                                                                                                                                                                                                                                                               | Updates, based on changes or corrections in software                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                       |
| July-August 2005      | Various                                                                                                                                                                                                                                                                                                                                                                                               | Changes for Patch 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                       |
| March 2005            | Various                                                                                                                                                                                                                                                                                                                                                                                               | Changes for Version 2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                       |

## Contents

Preface	ii

Purpose of Manager’s Manual	ii

Recommended Users	ii

Related Manuals	ii

Related Web Sites	ii

Revision History	iii

Contents	ix

Introduction	1

Patch 65 (PXRM*2.0*65) Changes	1

Patch 80 (PXRM*2.0*80) Changes	2

Patch 42 (PXRM*2.0*42) Changes	2

Patch 45 (PXRM*2.0*45) Changes	2

Patch 47 (PXRM*2*47) Changes	2

Patch 53 (PXRM*2*53) Changes	3

Patch 26 (PXRM*2*26) Changes	3

Patch 31 (PXRM*2.0*31)- Palliative Care National Clinical Template	6

Patch 36 (PXRM*2*36) Changes - Pneumococcal Reminders and Women’s Health Taxonomy update	6

Patch 24 (PXRM*2*24) Changes	7

Patch 23 (PXRM*2*23) Changes	8

Patch 22 (PXRM*2*22) Changes	8

Patch 21 (PXRM*2*21) Changes (Military Service Data Sharing (MSDS) project)	9

Patch 18 (PXRM*2*18) Changes	9

Patch 16 (PXRM*2*16) Changes	11

Patch 17 (PXRM*2*17) Changes	11

National Reminders	14

Updates to National Reminders in Patch 18	14

Updates to National Reminders in Patch 12	16

Updates to National Reminders in Patch 11	17

National Reminder Content	18

How to Get a List of Patches Released since V2.0	18

Reminders Maintenance	19

Reminder Managers Menu	19

Options not on a menu	20

Security Key	21

Reminder Managers Menu Descriptions	21

Reminder Computed Finding Management	24

Reminder Computed Finding Management Menu	25

National Computed Findings	30

COMPUTED FINDING PARAMETER  FORMULA	38

Reminder Definition Management	41

Patch 45 (PXRM*2*45) Changes to Reminder Definitions	42

Added a new possible value to the Reminder Definition Usage Field: A: Action	42

The “A” will not allow a reminder to be used on the CPRS coversheet unless the value of C is set also in the usage field.	42

Patch 24 (PXRM*2*24) High Risk Mental Health Patient - Reminder and Flag: Changes to Reminder Definitions	42

Patch 18 (PXRM*2*18- High Risk Mental Health Patient - Reminder and Flag-phase 1)  Updates for Reminder Definitions	46

Changes to National Reminder Definitions	46

List Reminder Definitions	52

Inquire About Reminder Item	52

Add/Edit Reminder Definition	57

Copy Reminder Definition	60

Reminder Edit History	61

Integrity Check Options	61

Integrity Check Selected	62

Integrity Check All	63

Reminder Definition Fields	64

Reminder Findings	67

* Changes to Beginning and Ending Date/Time made in Patch 18	75

Function Findings	90

Status List	107

Activate/Inactivate Reminders	109

Reminder Sponsor Management	110

List Reminder Sponsors	110

Reminder Sponsor Inquiry	111

Add/Edit Reminder Sponsor	111

Reminder Taxonomy Management	112

Reminder Taxonomy Management	113

Reminder Taxonomy Management Actions	116

Reminder Taxonomy Actions	117

Add	117

Edit	117

Taxonomy Fields	118

Patient Data Source Keywords	119

Copy	122

Inquire about Taxonomy Item	125

Change Log	128

Code Search	130

Import	132

At this point you will have the option of browsing the list of codes.	133

Use in Dialog Report (UIDR)	146

Code Set Versioning	148

Value Sets	150

Reminder Term Management	152

Reminder Term Management Options	152

List Reminder Terms	153

Inquire about Reminder Term	154

Add/Edit Reminder Term	155

Copy Reminder Term	157

Integrity Check Selected	157

Integrity Check All	157

Term Test	158

Reminder Location List Management	159

National Location Lists	159

Reminder Location List Menu	159

List Location Lists	160

Location List Inquiry	160

Add/Edit Location List	160

Create a new Location List	160

Copy Location List	161

Reminder Exchange	162

Terminology	163

Reminder Test	180

Running Reminder Test	183

Test Option Output for the EDUTEST Reminder	183

Reminder Evaluation in CPRS	203

Other Supporting Menus	206

Reminder Information Only Menu	207

Reminder Dialog Management	208

Changes to Reminder Dialogs in Patch 45	209

Steps to create a dialog	209

Dialog Component Definitions	209

Dialog Parameters	211

Editing Template Fields used in Reminder Dialogs	223

Dialog Reports	227

New Fields	236

CPRS Reminder Configuration Menu	249

Add/Edit Reminder Categories	250

CPRS Lookup Categories	252

CPRS Cover Sheet Reminder List	253

New Reminder Parameters - Edit Cover Sheet Reminder List	253

Cover Sheet Reminder Report	261

Mental Health Dialogs Active	274

Progress Note Headers	275

Reminder GUI Resolution Active	276

TIU Template Reminder Dialog Parameter	276

Evaluate Coversheet List on Dialog Finish	277

Default Outside Location	277

Position Reminder Text at Cursor	278

Link Reminder Dialog to Template	279

CPRS Coversheet Time Test	279

New Reminder Parameters	279

GEC Status Check Active	279

WH Print Now Active	280

Reminder Reports	282

Reminder Reports Menu	282

Reminders Due Report option	285

Reminders Due Report – Patient List Template	288

Reminders Due Report – Patient List	290

Extract EPI Totals	293

Extract QUERI Totals	295

GEC Referral Report	298

Review Date Report	300

Finding Usage Report	300

MST Synchronization Management Project	305

MST Scope of Changes	305

MST System Features	306

Reminder Parameters Menu	308

Edit Site Disclaimer Example	308

Edit Web Sites Example	308

Edit Number of MH Tests Example	309

Reminder Patient List Management	310

List Rules	311

Rule Set Definition	312

Steps to Create a Patient List	316

Patient List Management Option	319

Demographic Report	337

Reminder Extract Tools	341

Reminder Extract Menu	341

Clinical Reminder Extracts Guide	343

Key Components	343

Extract Definitions	353

Running the Extract	354

Understanding your Output	358

FAQ:	358

Access to National Extracts at Austin Information Technology Center (AITC)	358

Clinical Reminder Order Checks	359

Appendix A: Glossary	370

Acronyms	370

Definitions	371

Appendix B: Clinical Reminder Order Checks Example	375

Exiting a Subpage	378

Order Check Example	379

Appendix C: Measurements	384

Appendix D: Contraindications, Precautions, and Refusals	385

## Introduction

The Clinical Reminder system helps caregivers deliver higher quality care to patients for both preventive health care and management of chronic conditions, and helps ensure that timely clinical interventions are initiated.

Reminders assist clinical decision-making and also improve documentation and follow-up, by allowing providers to easily view dates when certain tests or evaluations were performed and to track and document when care has been delivered. They can direct providers to perform certain tests or other evaluations that will enhance the quality of care for specific conditions. The clinicians can then respond to the reminders by placing relevant orders or recording clinical activities on patients’ progress notes.

Clinical Reminders may be used for both clinical and administrative purposes. However, the primary goal is to provide relevant information to providers at the point of care, for improving care for Veterans. The package benefits clinicians by:

- Providing pertinent data for clinical decision-making
- Reducing duplicate documenting activities
- Assisting in targeting patients with particular diagnoses and procedures or site-defined criteria
- Assisting in compliance with VHA performance measures and with Health Promotion and Disease Prevention guidelines

When a reminder definition is used for point of care decision support, the evaluation status will be Not Applicable (N/A) for patients who have a recorded date of death because reminders do not need to be resolved for deceased patients.

When a reminder definition is used for reporting, deceased patients can be included since it may be important to know what reminders were resolved for them when they were alive.

### Patch 65 (PXRM*2.0*65) Changes

Patch 65 supports VistA Immunization Enhancements (VIMM).

A new finding modifier, IMMUNIZATION SEARCH CRITERIA, was added to the findings multiple of reminder definitions and reminder terms. It is a set of codes that controls how a patient’s immunizations are searched during reminder evaluation.

The CPRS v32b release allows users to input immunization contraindications, precautions, and refusals, storing them in the VIMM CONTRA/REFUSAL EVENTS file. Clinical Reminders was modified so that entries from this file can be used in reminder evaluation. As a result, there are two new evaluation statuses: CONTRA and REFUSED. The description for the computed finding, VA-REMINDER DEFINITION was updated to include the two new statuses.

The Patch 65 changes made the V IMMUNIZATION field (#.07) CONTRAINDICATED obsolete.  Thus, it was removed from reminder evaluation.

A new computed finding, VA-IMMUNIZATION AND LOCATION LOT INFO is included in Patch 65. It is only used with a Reminder Dialog to obtain lot information.

The following Patch 65 changes are not related to immunizations:

- The PRINT NAME, MINIMUM VALUE, MAXIMUM VALUE, MAXIMUM DECIMALS, UCUM CODE, PROMPT CAPTION and UCUM DISPLAY fields were added to Reminder Taxonomies. These fields provide the basis for being able to record measurements for codes in a taxonomy. The corresponding CPRS changes will be in a future version.
- Clinical Maintenance output of measurements was changed to use the UCUM DISPLAY field for determining what to display for the units.

### Patch 80 (PXRM*2.0*80) Changes

This patch changes how Reminder Exchange packs up Reminder Dialogs. Reminder Dialogs will no longer get packed if the dialog is attached to a Reminder Definition and that Reminder Definition is used in another Clinical Reminder component such as: Reminder Dialog Branching Logic, Reminder Order Check Rules, Reminder List Rules, or in a Reminder Definition or Reminder Term using the Computed Finding VA-REMINDER DEFINITION.

### Patch 42 (PXRM*2.0*42) Changes

This patch modified Clinical Reminder functionality to support the Coronavirus Disease (COVID) v2.0 updates.

This new functionality, called CSUB Objects, includes the ability to display the data for any finding in Found/Not Found Text.

This functionality was implemented in PXRM*2.0*46.  However, it wasn’t documented until the PXRM*2.0*42 release.

### Patch 45 (PXRM*2.0*45) Changes

This patch modified Reminder Dialog and Reminder Order Check functionality to support the TDrugs and the SMART projects being implemented in CPRS 31.B.

### Patch 47 (PXRM*2*47) Changes

This patch is the follow-up to PXRM*2*26, which was part of the Computerized Patient Record System CPRS v30 project. That project modified the Computerized Patient Record System, Text Integration Utilities, Consults, Health Summary, Problem List, Clinical Reminders, and Order Entry/Results Reporting domains to meet the requirements proposed by the Dept. of Health and Human Services to replace the ICD-9 code set with the ICD-10 code set. It removes the taxonomy fields made obsolete by PXRM*2*26, adds the taxonomy editor actions that could not be completed for the release of PXRM*2*26, and fixes some defects.

One of the bugs that is fixed involves display of the status line when the frequency is in hours. This change adds time to the Date Due and Last Done fields. Because there are a number of Clinical Reminders Health Summary components, a Health Summary patch is required, it is: GMTS*2.7*113.

### Patch 53 (PXRM*2*53) Changes

PXRM*2*53 adds a Reminder Dialog Search Report option to the Reminder Dialog Report menu. The Reminder Dialog Search Report allows sites to find Reminder Dialogs based on search criteria such as Coding Systems, Findings, and Dialog Items.

### Patch 26 (PXRM*2*26) Changes

PXRM*2*26 is part of the ICD-10 project, and the purpose of patch 26 and its related patches (DG*5.3*853 and GMPL*2*43) is to update Clinical Reminders to allow the use of ICD-10 codes. A very general approach has been taken, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon Utility. In addition to adding ICD-10 codes, SNOMED CT codes are being added. After the release of CPRS 29, SNOMED CT codes will be collected by Problem List and Clinical Reminders will be able to search for them.

A new taxonomy management system replaces the previous taxonomy management menu. See the Taxonomy Management chapter for details and examples. Also see the Dialog management chapter for information and examples of the changes made to Dialog options by this patch.

The new system uses a combination of List Manager, ScreenMan, and the Browser. List Manager should already be familiar to users of Clinical Reminders tools such as Dialog Management or Reminder Exchange. ScreenMan and the Browser may not be as familiar, but reviewing Appendix B of this manual or the FileMan documentation should give you enough knowledge to make using the taxonomy management system much easier.

After PXRM*2*26 is installed, users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new called Taxonomy Pick List Display has been  added to the dialog editor. This controls how Taxonomies should display in CPRS.

A simple taxonomy editor that is accessed from Dialog Management (either the element or group view) is available. Codes added in this editor are automatically marked as Use In Dialog. If a code is deleted in this editor, the Use In Dialog designation is removed from the code.

A change to Reminder Exchange was made to add a check of the line length and a warning if a line exceeds 245 characters. The maximum value allowed by Kernel is 255 characters, but for FileMan word-processing fields, it is 245. When a line exceeds this length, there is a very high probability that the Reminder Exchange entry will not install correctly. If the Reminder Exchange entry is transported as a host file, then 255 should work, but if is transported as a MailMan message, then 245 is the limit. The warning was added because previously, when an Reminder Exchange entry would not install correctly due to the line length being exceeded, it was difficult to determine the reason.  The solution was to shorten the length of the field being transported. Detailed information about the field that needs to be shortened is given in the warning.

Example:

Warning the following line exceeds the VistA maximum allowed length of 245.

Therefore this Exchange entry will not transport correctly.

Line: 811.23;+619,+617,;.01~Telephone Assessment/Management by Nonphysician to Established PT/Parent/Guardian not Originating from A/M Provided within Previous

7 Days Nor Leading to A/M Service/Procedure within Next 24 Hrs/Soonest Appt; 11-

20 Mins Medical Discussion

Its length is: 260

Component: REMINDER TAXONOMY

Name: PBM PHARMD PHONE VISIT CPT CODE 98967 V5*1

IEN: 617

Field number: .01

Value: Telephone Assessment/Management by Nonphysician to Established PT/Parent/

Guardian not Originating from A/M Provided within Previous 7 Days Nor Leading to

A/M Service/Procedure within Next 24 Hrs/Soonest Appt; 11-20 Mins Medical Discussion

**Disable/Enable Reminder Evaluation**

The option PXRM INDEX BUILD provides the ability to rebuild selected portions of the Clinical Reminders Index. (For information and details about the Clinical Reminders Index see the Clinical Reminders Index Technical Manual.) While an index is rebuilding, any reminder that uses the data from that index cannot be correctly evaluated –  it will have the status of CNBD (cannot be determined). In the past, a MailMan message was sent to the Clinical Reminders mail group every time a reminder could not be evaluated because an index was rebuilding. Now, when an index is going to be rebuilt, reminder evaluation will be automatically disabled, meaning that any attempt to evaluate a reminder will result in an immediate return of a CNBD status. The Clinical Maintenance display will include text letting the user know that reminder evaluation is disabled and the reason(s). When the index has finished rebuilding, evaluation will be automatically enabled.

The option PXRM DISABLE/ENABLE EVALUATION provides a manual disable/enable function. If for some reason, reminder evaluation needs to be disabled, it can be done through this option. This option should be given to a very limited number of people and can only be used by holders of the PXRM MANAGER key. When the issue that required disabling evaluation has been handled, reminder evaluation can be enabled again using this same option. Note that this option can be used to enable evaluation even if it was not disabled using this option. For example, if reminder evaluation was automatically disabled for an index rebuild, this option could be used to enable evaluation even though the index is still rebuilding.  If that is done, the MailMan messages will start being sent again.

When reminder evaluation is disabled, the following options and protocols will be put out of order.

Options:

PXRM DEF INTEGRITY CHECK ALL

PXRM DEF INTEGRITY CHECK ONE

PXRM ORDER CHECK TESTER

PXRM REMINDERS DUE

PXRM REMINDERS DUE (USER)

Protocols:

PXRM PATIENT LIST CREATE

PXRM EXTRACT MANUAL TRANSMISSION

When reminder evaluation is again enabled, these options and protocols will be put back in order.

Anytime reminder evaluation is disabled, a message with the subject “REMINDER EVALUATION DISABLED” will be sent to the Clinical Reminders mail group. The message will give the date and time that evaluation was disabled, list the reasons for disabling evaluation, and a search will be made for any Clinical Reminders TaskMan jobs that could be affected. There will be a list of those that are found; it will include the job description, the status (pending or running), and the task number. The results of any jobs that are already running will be unreliable and should be discarded. If possible, these jobs should be stopped, so that they don’t waste system resources. None of the pending jobs should be allowed to start until evaluation is enabled again.

When evaluation is enabled, a message with the subject “REMINDER EVALUATION ENABLED” will be sent to the Clinical Reminders mail group. It will contain the date and time evaluation was disabled and when it was enabled. This gives you the exact period of when evaluation was disabled.

Here are examples of disable and enable messages:

MailMan message for CRMANAGER, TWO

Printed at EXAMPLE.ORG.EXAMPLE.VA.GOV  04/16/14@10:32

Subj: REMINDER EVALUATION DISABLED  [#122941] 04/16/14@10:30  58 lines

From: POSTMASTER (Sender: CRMANAGER, ONE)  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Reminder evaluation was disabled on Apr 16, 2014@10:30:42.

Because of this, the following TaskMan jobs can produce erroneous results.

Pending jobs should not be allowed to start until evaluation is enabled.

The results of running jobs should be discarded and if possible, running jobs

should be stopped.

Reason: index rebuild for file #45.

Reminders Due Report Jobs

Task number - 316820

Status - Active: Running

Time - Feb 08, 2012@12:40:28

User - CRCOORDINATOR, TWO

Reminder Patient List Jobs

Task number - 1980022

Status - Active: Running

Time - Apr 16, 2014@08:00

User - TASKMAN,PROXY USER

Task number - 1980207

Status - Active: Pending

Time - Apr 17, 2014@08:00

User - TASKMAN,PROXY USER

Reminder Extract Jobs

Task number - 342256

Status - Active: Pending

Time - Mar 06, 2012@20:04:25

User - CRCOORDINATOR, SIX

Task number - 1867565

Status - Active: Pending

Time - May 17, 2013@16:44:13

User - CRCOORDINATOR, SIX

Task number - 1902474

Status - Active: Pending

Time - Jul 17, 2013@17:16:30

User - CRCOORDINATOR,TEN

Task number - 1945932

Status - Active: Pending

Time - Oct 22, 2013@12:37:23

User - CRCOORDINATOR, THIRTY

Task number - 1946204

Status - Active: Pending

Time - Oct 23, 2013@12:37:35

User - CRCOORDINATOR, TWO

Task number - 1966964

Status - Active: Pending

Time - Feb 05, 2014@07:54:39

User - CRCOORDINATOR,THREE

Enter message action (in IN basket): Ignore//

Subj: REMINDER EVALUATION ENABLED  [#122942] 04/16/14@10:30  2 lines

From: POSTMASTER (Sender: CRMANAGER, ONE)  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Reminder evaluation was enabled on Apr 16, 2014@10:30:49.

It was disabled on Apr 16, 2014@10:30:42.

Enter message action (in IN basket): Ignore//

See the Revision History in this manual and the Release Notes for additional changes made by PXRM*2*26.

### Patch 31 (PXRM*2.0*31)- Palliative Care National Clinical Template

This patch releases the Palliative Care National Clinical Template without any changes to routines, data dictionaries, or other package functions – “content” only. The reminder dialog is VA-PALLIATIVE CARE NATIONAL CLINICAL TEMPLATE (PC-NCT).

There are two Reminder Exchange entries that will be installed as part of this patch.

1. VA-PALLIATIVE CARE CONSULT

2. VA-PATCH 31 POST HS COMPONENTS

The VA Hospice and Palliative Care (HPC) program office has sponsored the development of this reminder dialog template to document provider-based palliative care consultations at all sites within VHA. This template is critical to improving the process and documentation of clinical care, and facilitating high quality palliative care and programmatic quality improvement. It is the intent of the HPC program office that this national template be formally distributed to VA palliative care programs for voluntary use throughout VHA in early 2014.

### Patch 36 (PXRM*2*36) Changes - Pneumococcal Reminders and Women’s Health Taxonomy update

This patch installs two new or modified pneumococcal reminders, two new dialogs, and several new or modified terms and taxonomies, based on new guidelines.

ACIP recommends that adults aged &gt;=19 years with immuno-compromising conditions, functional or anatomic asplenia, CSF leaks, or cochlear implants, and who have not previously received PCV13 or PPSV23, should receive a dose of PCV13 first, followed by a dose of PPSV23 at least 8 weeks later (Table). Subsequent doses of PPSV23 shouldfollow current PPSV23 recommendations for adults at high risk.

See the patch 36 Installation Guide for further details.

Patch 34 (PXRM*2*34) Changes - Teratogenic Medication Reminder Order Check Update

The Teratogenic Medications Order Check Interim Solution was originally released as VistA patch PXRM*2*22 in July 2012.  The interim solution is intended to have regular updates for clinical content, primarily to add newly approved medications with FDA Pregnancy Categories that warrant an order check. This patch, PXRM*2*34 represents the first such update.  Included in this update are new medications, order check text changes consistent with the Notification of Teratogenic Medications project, support for reversal of tubal ligations, and updates to the taxonomies that define a women’s medical inability to conceive a pregnancy.

This patch also includes an update to a single dialog element for the Epilepsy Initial note that was released with PXRM*2.0*30.  That element had a mapped Health Factor Category, instead of a mapped Health Factor.  This element updates that mapped item.

### Patch 24 (PXRM*2*24) Changes

The High Risk Mental Health Patient – Reminder &amp; Flag project was released in two phases; the first phase was released in March 2012 with PXRM*2*18.

Phase 1 of this project provided the following:

1. Two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments,
2. A new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and
3. A new health summary type with MH-specific supporting information.

**Phase 2 of this project provides the following:**

DG*5.3*849 – DGPF New Category 1 Flag and Conversion.

TIU*1*265 – New PRF Category 1 Title -  HIGH RISK FOR SUICIDE

SD*5.3*588 – New proactive reports that list appointments for High Risk for Suicide patients who have appointments for the day. MHTC has been added to these reports and also to the background nightly job no-show reports.

- PXRM*2*24 – New patch that includes an updated reminder (VA-MH HIGH RISK NO-SHOW FOLLOW-UP), a new computed finding (VA-PCMM MHTC), a new dialog that will display the MHTC, two new Reminder Definitions (VA-MH HIGH RISK NO-SHOW ADHOC RPT and VA- MHTC NEEDS ASSIGNMENT), and a new location list, VA-MHTC APPT STOP CODES LL, which is used in the Computed Finding: VA-Appointments for a Patient.  The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.

OR*3*348 – Order Entry changes for the Mental Health Treatment Coordinator - Ability to select a Mental Health Treatment Coordinator as a notification recipient to receive notifications in CPRS. A new notification is also being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE.

GMTS*2.7*104 - modifies two entries in the Health Summary Component file (142.1): MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.  These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH HIGH RISK PATIENT Health Summaries, as well as being available for use in the Health Summary Ad hoc Report.

- Suicide Behavior Report (SBR) instrument – The SBR is a new mental health template and a new entry in the MH TESTS &amp; SURVEYS file (#601.71). It was distributed nationally in YS*5.01*103, as an enhancement to the Mental Health Assistant 3.0 Package.  This instrument can be used by MH professionals to assess and reassess the High Risk for Suicide patient’s behavior.

See the Release Notes, Installation &amp; Setup Guide, and User Manual for more details about PXRM*2*24 enhancements and fixes.

### Patch 23 (PXRM*2*23) Changes

This patch is part of a multi-package build that contains FB*3.5*138 and PXRM*2.0*23. It supports the third increment for Project ARCH **(** Access to Care Received Closer to Home **).**

FB*3.5*138:

This build adds the PROJECT ARCH REMINDER DELAY field (#38) to the FEE BASIS SITE PARAMETERS file (#161.4) that allows sites to customize number of days that the Project ARCH Clinical Reminder will become due again after the patient Declines or Refuses services offered. Two new options are also installed on the Project ARCH Menu. The ARCH

Eligibility Data Upload option allows sites to upload the national Project ARCH data extract files that contain the updates for Project ARCH Eligibility. The ARCH Clinical Reminder Due Delay option sets the value in the new PROJECT ARCH REMINDER DELAY field with a number between 1 and 180 days.

PXRM*2*23:

This build places updated VA-PROJECT ARCH VISN CONTRACT CARE PILOT ELIGIBILITY in the Reminder Exchange file. Updates to this reminder include a new Health Factor ARCH-SERVICE NEEDED THIS VISIT REFUSES. The updates also include a mandatory checkbox indicating that the patient has signed the consent form when the ARCH-SERVICE NEEDED THIS VISIT CONSENTS Health Factor is selected in the Reminder Dialog.

### Patch 22 (PXRM*2*22) Changes

Patch PXRM*2*22  releases two new National Reminder Order Checks for placing Teratogenic Medications in CPRS. A pre-installation routine will identify any previously identified components and rename them correctly, and the patch installation will create or overwrite VA-named, national reminder components

This patch also addresses two bug fixes in the Reminder Order Check setup. To address these fixes, the Reminder Order Check System had to be divided into two files:

- File 801 Reminder Order Check Items Group

File 801 contains the grouping of Orderable Items. This file has also been modified to allow groups to include entries from the Drugs file, file #50, VA Generic file, file #50.6 and VA Drug Class file, file # 50.605.

- File 801.1 Reminder Order Check Rules.

File 801.1 contains the Reminder Order Check Rules.

These changes will allow sites to modify the Active and Testing Fields for National Rules.

This patch also fixes a Mumps error when the select order checks prompt times out.

To support the two-file structures, the existing menu options have been renamed and two new options will be released with this patch: Reminder Order Check Rule Inquiry and Reminder Order Check Test.

### Patch 21 (PXRM*2*21) Changes (Military Service Data Sharing (MSDS) project)

This patch is being released along with patches DG*5.3*797, EAS*1.0*92, IVM*2.0*141,  DVB*4.0*62, in host file DG\_53\_P797.KID, to support technology and business changes that occur with the implementation of the Enrollment System Redesign (ESR) Military Service Data Sharing (MSDS)  project. The MSDS project introduced an MSDS Broker that will be activated in ESR. The Broker will construct a definitive military service data set including data received from the VA/DoD Identity Repository (VADIR), the Beneficiary Identification and Records Locator System (BIRLS), and VistA. Once the MSDS Broker is activated, ESR becomes the authoritative source for Military Service Episode data. The verified data will be shared from ESR to all VistA sites of record for the Veteran. The ESR-verified Military Service Episode data cannot be edited by VistA except to add new episodes. An unlimited number of military service episodes per Veteran will now be supported.

**Clinical Reminders Computed Findings**

One aspect of the Military Service Data Sharing (MSDS) project increases the number of military service episodes from three to an unlimited number. It provides new APIs for Clinical Reminders to use to get this data. These APIs are used to update the computed findings, VA-SERVICE BRANCH and VA-SERVICE SEPARATION DATES, so they can get data for all episodes of service.

NOTE: VA-LAST SEPARATION DATE is being renamed to VA-LAST SEPARATION DATES, because now it will return all service separation dates instead of just the last one.

A new list type computed finding: VA-OEF/OIF SERVICE (LIST) is also included. It can be used to build lists of patients with OEF/OIF service.

### Patch 18 (PXRM*2*18) Changes

The High Risk Mental Health Patient – National Reminder and Flag project includes a national reminder and reminder dialog that mental health professionals can use to follow up on patients with the “High Risk of Suicide” patient record flag ,who missed their Mental Health appointments.  The project also includes reports to facilitate follow-up on these patients by Suicide Prevention Coordinators and other Mental Health professionals.

Veterans Health Administration (VHA) mental health officials estimate that there are 1,000 suicides per year among Veterans receiving care within VHA and as many as 5,000 per year among all living Veterans.  This request supports the Secretary’s Mental Health Strategic Plan that contains several initiatives pertaining to suicide prevention, including “Develop methods for tracking Veterans with risk factors for suicide and systems for appropriate referral of such patients to specialty mental health care.”

Major objectives of this project include:

1. Identifying those Veterans who are at risk for suicide (Sites define this locally in the Patient Record Flag.)
2. Preventing high risk, depressed patients from failing to get appropriate care if they miss appointments.  The plan is to evaluate patients for depression so that appropriate referrals can be made, identify those Veterans with a history of suicide attempt or suicidal ideation who miss an appointment, notify the mental health professional of the missed appointment, and track efforts to reach this Veteran.  If the Veteran is not reached after three attempts, a staff member may need to call other patient contacts or request a welfare check.

The purpose of this project is to release 1) two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments, 2) a new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and 3) provide a health summary type with MH-specific supporting information.

**Phase 1:** The first release of the High Risk Mental Health Patient- Reminder and Flag (HRMHP) project includes five patches, which will be installed as a combined build. The second phase of this project will be released in a future build.

1. SD*5.3*578

This Scheduling patch provides two new MH NO SHOW Scheduling Reports for use by Suicide Prevention Coordinators and other Mental Health professionals.  The reports will support following up with High Risk for Suicide patients that missed a scheduled MH appointment.

1. DG*5.3*836

This Registration – Patient Record Flag patch provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide flag status on a specified date.

1. PXRM*2*18

This patch creates a national reminder to notify clinicians of a patient's risk of suicide and creates a dialog that the clinicians can use to document follow-up with the high risk patients when they miss MH appointments.

- HIGH RISK MH NO-SHOW FOLLOW-UP Reminder Definition
- HIGH RISK MH NO-SHOW Follow-up Reminder Dialog

This Clinical Reminder patch supports the Scheduling patch by providing a national Reminder Location List of Mental Health stop codes used for scheduled appointments.  Additionally, this patch includes miscellaneous clinical reminder maintenance changes. Details of all the Clinical Reminder changes can be found in the Release Notes.

1. GMTS*2.7*99

This patch installs four Health Summary Components and two Health Summary Types, a single Health Summary Object, and a single TIU/Health Summary object.

1. TIU*1*260

The Text Integration Utility patch contains a single Health Summary Object and a single new TIU Health Summary object based on the new VA-MH HIGH RISK PATIENT Health Summary Type from GMTS*2.7*99. The TIU/HS object will be used in the VA-MH HIGH RISK NO  SHOW FOLLOW-UP Reminder Dialog distributed in PXRM*2*18.

***See the Clinical Reminders patch 18 Release Notes for specific details about enhancements and changes in patch 18 and related GMTS, OR, and TIU patches.***

### Patch 16 (PXRM*2*16) Changes

The Clinical Reminders patch PXRM*2*16 and bundled patches (OR*3.0*280, PSJ*5.0*226) released new functionality that enables sites to create their own CPRS Order Checks using Clinical Reminder Definitions or Terms. Both Reminder Exchange and the Review Date Report have been enhanced to support the Clinical Reminder Order Check functionality.

This patch contains a new computed finding, VA-ACTIVE PATIENT RECORD FLAGS.

This computed finding will allow sites to evaluate whether a patient has a specific active record flag on the date of evaluation.

Sites can create local order checks using the Clinical Reminder functionality. These Order Checks will occur at the time the user clicks on the accept button when placing an order in CPRS. This functionality is available with PXRM*2.0*16 and CPRS 28. The set-up of a Clinical Reminders Order Check consists of two parts:

- Creating a group of orderable items that the rules should be applied to.
- Creating the rules that will be applied to the orderable item when accepting an order in CPRS. It will be possible to have the same orderable item in multiple groups. Each rule assigned to the different groups will be evaluated when placing the orderable item in CPRS. The order check groups and the rule will be stored in the Reminder Order Check file, file #801

**Note:** Sites should evaluate all requests to create a Clinical Reminder Order Check to determine the importance of adding it. The more reminders that are used in an order check, the more they could affect the performance of the order check system. This file stores a pointer to an entry in the Orderable Item file, file #101.43. The reminder Order Check file **will not** automatically be updated with changes to the Orderable Item file, such as inactivating an existing orderable item, or if an ancillary package adds an item to the Orderable Item file.. The entries in Reminder Order Check file, file #801 need to be evaluated by the site anytime an update is done to the Orderable Item file, file #101.43. The site will be need to determine if it needs to remove an orderable item from an existing group or if it needs to add an orderable item to existing group.

A new menu Reminder Orderable Item Group Menu ...[ PXRM ORDERABLE ITEM GROUP MENU] has been added to the Reminder Managers Menu [PXRM MANAGERS MENU]

### Patch 17 (PXRM*2*17) Changes

This project released a new national reminder and reminder dialog to be used by Polytrauma Specialty providers to identify potential OEF/OIF Polytrauma patients and mark the patient with a Polytrauma Marker (health factor) when appropriate.

The Polytrauma Marker project includes two patches:

PXRM*2*17 -	Clinical Reminder patch with Polytrauma Marker reminder/dialog

USR*1*33 -	ASU patch with API that checks to see if a user is a member of a specific User Class

This project was requested by the Office of Patient Care Services (PCS) to provide a means of improving care provided to Veterans and active duty patients suffering from blast-related polytrauma (multiple complex injuries). VHA has identified this as one of several initiatives that will support health care of Operation Iraqi Freedom and Operation Enduring Freedom (OIF/OEF) Veterans.

The Polytrauma Assessment reminder definition contains a new national reminder term which will be pre-defined with the new computed finding for the ASU User Class.  Sites will be required to add the Computed Finding Parameter to the national reminder term.  The parameter should specify the local ASU User Class that identifies specialty provider members that focus on Polytrauma and Rehabilitation services at the local facility.

The Polytrauma Assessment reminder uses a series of national Reminder Taxonomies to determine whether the patient has multiple diagnoses that identify the patient as a potential Polytrauma patient.  The combination of the diagnoses found and the user’s ASU user class will determine whether the reminder is applicable to the patient.

If the reminder is applicable to the patient and the patient has not been previously assessed for Polytrauma, the reminder will be DUE and will appear on the cover sheet and in the reminder drawer on the CPRS notes tab.

The reminder will be resolved by the provider responding to reminder dialog responses that result in the assessment that the patient “is” or “is not” an OEF/OIF Polytrauma patient.  The responses will cause Health Factors to be created that make the reminder no longer due.

If the CPRS user views Clinical Maintenance output for the Polytrauma Assessment reminder and the user is not a member of the ASU User Class, then a message will be included in the Patient Cohort section indicating that the ASU User Class was not found.

The new Polytrauma Assessment reminder dialog was created outside the OI Field Office and tested at three sites based on input from Rehabilitation Service stakeholders.

This reminder/dialog includes branching logic that will use the new national reminder term that is defined with the ASU user class used by the reminder definition. The branching logic will check to see if the CPRS user is a member of the ASU user class before continuing with the reminder dialog.  If the CPRS user is not a member of the ASU user class, then the reminder dialog will display text indicating the reminder is not applicable and the user is not the appropriate user to complete the reminder dialog.

Completing the reminder dialog will cause a progress note to be created and Health Factors will be populated in PCE. These health factors will be used by future reminder definition evaluation to indicate the reminder is resolved.

### National Reminders

National reminders are clinical reminders and reminder dialogs that have gone through an approval process for national distribution. Some national reminders are related to statutory, regulatory, or Central Office mandates such as Hepatitis C and MST. Other national reminders are being developed under the guidance of the National Clinical Reminders Workgroup (NCRW).

Guideline-related reminders are developed for two reasons:

1.  To provide reminders for sites that don’t have reminders in place for a specific guideline (e.g., HTN, HIV).

2.  To provide a basic set of reminders to all sites to improve clinical care, and also allow roll-up data for measurement of guideline implementation and adherence (e.g., IHD, Mental Health).

#### Updates to National Reminders in Patch 18

1. Updated branching logic reminders for OEF/OIF screening:
    1. Fix the problem that patients who do not have the required LSSD entry are not having the items show as due when they have been done.
    2. Remove refusals and other exclusions from the branching logic – if not done, then show the item as open and allow the parent reminder to use the exclusions instead of also evaluating them in the branching logic.  This makes all 7 of the branching logic reminders consistent.
2. Updated the URLs for MH screening.
3. Added '0' to the Within Category Rank for EF-NO BLAST/EXPLOSION INJURY and EF-NO BULLET INJURY in the reminder VA-EMBEDDED FRAGMENTS RISK EVALUATION.
4. Added occurrence count of 4 to AUD C in the alcohol screening reminder.
5. Fixed header/info text in AAA reminder.
6. Distributed H1N1 reminders and dialog via patch and distribute and inactivate.
7. Updated VA-ALCOHOL F/U POS AUDIT-C dialog to display the education and advice interventions without a box around both and also to have the results of an AUDIT-10 go into the progress note.
8. Added VA-TB/POSITIVE PPD.

Detailed descriptions:

1. Updated branching logic reminders

VA-BL DEPRESSION SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Resolution: changed to resolve for any entry that is not before the LSSD

Changed the logic from

MRD(VA-DEPRESSION SCREEN NEGATIVE,VA-DEPRESSION SCREEN POSITIVE)&gt;MRD(VA-LAST SERVICE SEPARATION DATE)

To

MRD(VA-DEPRESSION SCREEN POSITIVE,VA-DEPRESSION SCREEN NEGATIVE)'&lt;MRD(VA-LAST SERVICE SEPARATION DATE)

VA-BL ALCOHOL SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: change to due for all

Removed exclusions

Resolution: changed to resolve for any entry that is not before the LSSD

VA-BL PTSD SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: change to due for all

Removed exclusions

Resolution: change to resolve for any entry that is not before the LSSD

Add a '0' to the Within Category Rank for the health factors.

VA-BL OEF/OIF EMBEDDED FRAGMENTS

VA-BL OEF/OIF FEVER

VA-BL OEF/OIF GI SX

VA-BL OEF/OIF SKIN SX

Removed RT.VA-IRAQ/AFGHAN PERIOD OF SERVICE and substitute CF.VA-LAST SERVICE SEPARATION DATE

Removed RT.VA-ACTIVE DUTY

Cohort: change to due for all

Resolution: change to resolve for any entry that is not before the LSSD

2.	Updated URLs

VA-ALCOHOL USE SCREEN (AUDIT-C)

VA-DEPRESSION SCREENING

VA-PTSD SCREENING

1. VA-EMBEDDED FRAGMENTS RISK EVALUATION: Added '0' to the Within Category Rank for EF-NO BLAST/EXPLOSION INJURY and EF-NO BULLET INJURY

1. VA-ALCOHOL USE SCREENING (AUDIT-C)
    1. Added occurrence count of 4 to AUD C in the alcohol screening reminder
    2. Updated the dialog by changing 'Optional open and optional complete (partial complete possible)' to 'Optional open and required complete or cancel before finish'.

1. Fixed grammatical error in VA-TEXT INFO SCREEN FOR AAA

1. Distributes reminders VA-INFLUENZA H1N1 IMMUNIZATION, VA-INFLUENZA H1N1 IMMUNIZATION HIGH RISK, and dialog VA-INFLUENZA H1N1 IMMUNIZATION (DIALOG).  Distribute as INACTIVE.

1. Updated VA-ALCOHOL F/U POS AUDIT-C dialog to display the education and advice interventions without a box around both and also to have the results of an AUDIT-10 go into the progress note.  Add an * to the word 'required' in 2 of the captions.

1. Added VA-TB/POSITIVE PPD. This updates the taxonomy VA-TB/POSITIVE PPD by adding the ICD diagnosis code 795.51

#### Updates to National Reminders in Patch 12

The following Reminder components were updated and redistributed with PXRM*2*12:

| Component   | Name                                  | Change                                                                                                                                                       |
|-------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RD          | VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL  | Added SUD; added text dialog element for local health summary object for prior AUDIT-C display; reversed order of feedback and advice; made nothing required |
| RD          | VA-EMBEDDED FRAGMENTS RISK EVALUATION | New                                                                                                                                                          |
| RD          | VA-IRAQ & AFGHAN POST-DEPLOY SCREEN   | Added a FF to the cohort logic                                                                                                                               |
| RD          | VA-TBI SCREENING                      | Changed dialog to have documentation of discussion of positive screen                                                                                        |
| RL          | VA-OEF/OIF EXCLUSION STOPS            | Added ultrasound stop code                                                                                                                                   |
| RM          | VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL  | Added SUD clinic visit exclusions                                                                                                                            |
| RM          | VA-DEPRESSION SCREEN                  | Updated URLs and description.                                                                                                                                |
| RM          | VA-EMBEDDED FRAGMENTS RISK EVALUATION | New                                                                                                                                                          |
| RM          | VA-IRAQ/AFGHAN POST DEPLOYMENT SCREEN | Uses OEF/OIF in dialog and logic; updated logic, fixed active duty problem                                                                                   |
| RM          | VA-OEF/OIF MONITOR REPORTING          | Removed dialog from this reporting reminder.                                                                                                                 |
| RM          | VA-TBI SCREENING                      | Changes to OEF/OIF in dialog and logic,  fixed active duty issue                                                                                             |
| RT          | VA-ACTIVE DUTY                        | Updated active duty term description                                                                                                                         |
| RT          | VA-ALCOHOL NONE PAST 1YR              | Removed MH test from term VA-ALCOHOL NONE PAST 1YR                                                                                                           |
| RT          | VA-IRAQ/AFGHAN SERVICE                | Updated to include CFs for OEF/OIF service that point to the patient file                                                                                    |
| RX          | VA-OEF/OIF MONITOR                    | New extract                                                                                                                                                  |
| TX          | VA-BREAST TUMOR                       | Changed description to include mass, pain, abnormality                                                                                                       |
| TX          | VA-DEPRESSION                         | Updated to FY09 definition                                                                                                                                   |
| TX          | VA-DEPRESSION OUTPT                   | Updated to FY09 definition                                                                                                                                   |
| TX          | VA-DIABETES                           | Added 250.91-250.93                                                                                                                                          |
| TX          | VA-HIGH RISK FOR FLU                  | New                                                                                                                                                          |
| TX          | VA-HIGH RISK FOR FLU/PNEUMONIA        | Inactivated                                                                                                                                                  |
| TX          | VA-HIGH RISK FOR PNEUMONIA            | New                                                                                                                                                          |

#### Updates to National Reminders in Patch 11

| Reminder                                     | Change                                                                                                                                                                                                                                               |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL         | Fixed logic                                                                                                                                                                                                                                          |
| VA-ALCOHOL USE SCREEN (AUDIT-C)              | Changes to dialog.  Removed date from term and moved to the health factor for “No alcohol in the past 1 year”                                                                                                                                        |
| VA-BL OEF/OIF FEVER                          | Fixed logic                                                                                                                                                                                                                                          |
| VA-BL OEF/OIF GI SX                          | Fixed logic                                                                                                                                                                                                                                          |
| VA-BL OEF/OIF SKIN SX                        | Fixed logic                                                                                                                                                                                                                                          |
| VA-DEPRESSION SCREENING                      | Changes to terms and dialog; verify/report any changes                                                                                                                                                                                               |
| VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN | Multiple changes:  - Added Combat Vet to logic - Excluded those who did not serve from denominator - Added cognitive impairment to exclusions - Added done elsewhere to resolutions - Updated dates of health factors for depression/PTSD to 10/1/08 |
| VA-PTSD SCREENING                            | Added Veteran status  Added Acute Illness to the dialog                                                                                                                                                                                              |

#### National Reminder Content

National Content is released on a frequent basis. These releases can either add or update reminder content. The NAME for all national content starts with VA- and the CLASS is NATIONAL. The names of some national dialog components will start with VAL- and the CLASS will be LOCAL so they can edited by sites.

#### How to Get a List of Patches Released since V2.0

In the Forum Patch module, use the following option to get a list of all V2.0 released patches:

**AD     All Released Patches for a Package, Detailed**

## Reminders Maintenance

This section describes all the major components of the Clinical Reminders application. It describes the menus and options, and provides examples of how to use these to define reminders, create dialogs, and how to modify, troubleshoot, and maintain them for your site.

### Reminder Managers Menu

This is a list of the options and menus on the Reminders Managers Menu.

Reminders Managers Menu [PXRM MANAGERS MENU]

CF     Reminder Computed Finding Management ... [PXRM CF MANAGEMENT]

CRL    Computed Finding List

CFI    Reminder Computed Finding Inquiry

CFE    Add/ Edit Computed Finding

RM     Reminder Definition Management ... [PXRM REMINDER MANAGEMENT]

RL     List Reminder Definitions

RI     Inquire about Reminder Definition

RE     Add/Edit Reminder Definition

RC     Copy Reminder Definition

RA     Activate/Inactivate Reminders

RH     Reminder Edit History

ICS    Integrity Check Selected

ICA    Integrity Check All

SM     Reminder Sponsor Management [PXRM SPONSOR MANAGEMENT]

SL     List Reminder Sponsors

SI     Reminder Sponsor Inquiry

SE     Add/Edit Reminder Sponsor

TXM    Reminder Taxonomy Management ... [PXRM TAXONOMY MANAGEMENT]

TRM    Reminder Term Management ... [PXRM TERM MANAGEMENT]

TL     List Reminder Terms

TI     Inquire about Reminder Term

TE     Add/Edit Reminder Term

TC     Copy Reminder Term

LM     Reminder Location List Management ... [PXRM LOCATION LIST MANAGEMENT]

LL     List Location Lists

LI     Location List Inquiry

LE     Add/Edit Location List

LC     Copy Location List

RX     Reminder Exchange [PXRM REMINDER EXCHANGE]

RT     Reminder Test [PXRM REMINDER TEST]

OS     Other Supporting Menus ... [PXRM OTHER SUPPORTING MENUS]

TM     PCE Table Maintenance ...

PC     PCE Coordinator Menu ...

HS     Health Summary Coordinator's Menu ...

EF     Print Blank Encounter Forms ...

QO     Enter/edit quick orders

INFO   Reminder Information Only Menu ... [PXRM INFO ONLY]

RL     List Reminder Definitions

RI     Inquire about Reminder Definition

TXL    List Taxonomy Definitions

TXI    Inquire about Taxonomy Item

TRL    List Reminder Terms

TRI    Inquire about Reminder Term

SL     List Reminder Sponsors

DM     Reminder Dialog Management ... [PXRM DIALOG MANAGEMENT]

DP     Dialog Parameters ...

RS     Reminder Resolution Statuses

HR     Health Factor Resolutions

FP     General Finding Type Parameters

FI     Finding Item Parameters

TD     Taxonomy Dialog Parameters

DI     Reminder Dialogs

DR     Dialog Reports

OR     Reminder Dialog Elements Orphan Report

ER     Empty Reminder Dialog Report

ALL    Check all active reminder dialogs for invalid items

CH     Check Reminder Dialog for invalid items

**IA	    Inactive Codes Mail Message**

CP     CPRS Reminder Configuration [PXRM CONFIGURATION MANAGEMENT]

CA     Add/Edit Reminder Categories

CL     CPRS Lookup Categories

CS     CPRS Cover Sheet Reminder List

MH     Mental Health Dialogs Active

PN     Progress Note Headers

RA     Reminder GUI Resolution Active

DL     Default Outside Location

PT     Position Reminder Text at Cursor

WH     WH Print Now Active

GEC    GEC Status Check Active

TIU    TIU Template Reminder Dialog Parameter

NP     New Reminder Parameters

RP     Reminder Reports ... [PXRM REMINDER REPORTS]

RD     Reminders Due Report

RDU    Reminders Due Report (User)

RDT    User Report Templates

EPT    Extract EPI Totals

EPF    Extract EPI List by Finding and SSN

EQT    Extract QUERI Totals

GEC    GEC Referral Report

REV    Review Date Report

FUR    Finding Usage Report

MST    Reminders MST Synchronization Management ... [PXRM MST MANAGEMENT]

SYN    Reminders MST Synchronization

REP    Reminders MST Synchronization Report

PL     Reminder Patient List Menu ... [PXRM PATIENT LIST MENU]

LRM    List Rule Management

PLM    Patient List Management

PAR    Reminder Parameters ... [PXRM REMINDER PARAMETERS]

ESD    Edit Site Disclaimer

EWS    Edit Web Sites

MH     Edit Number of MH Questions

ROI	   Reminder Orderable Item Menu

OE     Add/Edit Reminder Orderable Item Group

OI     Reminder Orderable Item Inquiry

OT     Reminder Orderable Item Group Test

XM     Reminder Extract Menu [PXRM EXTRACT MENU]

MA     Reminder Extract Management

EP     Extract Definition Management

EC     Extract Counting Rule Management

EG     Extract Counting Group Management

LR     List Rule Management

GEC    GEC Referral Report  [GEC REFERRAL REPORT]

#### Options not on a menu

The option PXRM DISABLE/ENABLE EVALUATION provides a manual disable/enable function. If for some reason, reminder evaluation needs to be disabled, it can be done through this option. This option should be given to a very limited number of people and can only be used by holders of the PXRM MANAGER key. When the issue that required disabling evaluation has been handled, reminder evaluation can be enabled again using this same option. Note that this option can be used to enable evaluation even if it was not disabled using this option. For example, if reminder evaluation was automatically disabled for an index rebuild, this option could be used to enable evaluation even though the index is still rebuilding.  If that is done, the MailMan messages will start being sent again.

#### Security Key

**PXRM MANAGER**

DESCRIPTION:

Assign this key to people who manage Clinical Reminders.

**Options/actions requiring this key**

**PXRM DISABLE/ENABLE EVALUATION**

(see above description)

**PXRM REMINDERS DUE REPORT   on** the PXRM REMINDER REPORTS menu

- The field called **Owner** is populated when someone creates a reminder report template. This field will be used when someone accesses the template. The user accessing the template must either be the same user who created the template or must hold the PXRM MANAGER key to be able to access the option to edit the template. If the user is not the creator and does not hold the PXRM MANAGER key, they will not see the prompt to edit the template.

**Patient List Management Option**

**Actions**

- Create Patient List

**Secure List? prompt**

If the answer to this prompt is “YES,” the list becomes a private list, which means that the only people who can view the list are the creator, anyone who the creator has given view access, and anyone who holds the PXRM MANAGER KEY.

ED (Edit Patient List) – if you are the creator of the list you can use this action to edit the name and type of list; if you hold the PXRM MANAGER key you can also edit the creator of the list.

USR (View Users) – this action is applicable only to private lists. If you are the creator of the list or hold the PXRM MANAGER key you can use this action to give other users either view only or full access to the patient list. You can also remove a user’s access to the list.

#### Reminder Managers Menu Descriptions

| **Option**                           | **Option Name**               | **Syn**   | **Description**                                                                                                                                                                                           |
|--------------------------------------|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Computed Finding Management | PXRM CF MANAGEMENT            | CF        | This option provides tools for viewing and editing reminder computed findings.                                                                                                                            |
| Reminder Definition Management       | PXRM REMINDER MANAGEMENT      | RM        | This menu contains options for creating, copying, and editing reminder definitions, as well as the options for maintaining the parameters used by CPRS for reminder processing.                           |
| Reminder Sponsor Management          | PXRM SPONSOR MANAGEMENT       | SM        | A Reminder Sponsor is the organization or group that sponsors a Reminder Definition, such as the Office of Quality and Performance. Options on this menu let you view, define, or edit Reminder Sponsors. |
| Reminder Taxonomy Management         | PXRM TAXONOMY MANAGEMENT      | TXM       | This option provides all aspects of taxonomy management including creation, editing, and inquiry.                                                                                                         |
| Reminder Term Management             | PXRM TERM MANAGEMENT          | TRM       | This menu allows you to edit, map, and view reminder terms.                                                                                                                                               |
| Reminder Location List Management    | PXRM LOCATION LIST MANAGEMENT | LM        | Location Lists store locations as stop codes or hospital locations.This option provides tools for viewing and editing location lists.                                                                     |
| Reminder Exchange                    | PXRM REMINDER EXCHANGE        | RX        | This option allows sites to exchange reminder definitions, dialogs, and other reminder components via MailMan messages and host files.                                                                    |
| Reminder Test                        | PXRM REMINDER TEST            | RT        | This utility helps you test and troubleshoot your reminders when you create them or when you have problems.                                                                                               |
| Other Supporting Menus               | PXRM OTHER SUPPORTING MENUS   | OS        | This option contains menus from related packages such as PCE and Health Summary.                                                                                                                          |
| Reminder Information Only Men        | PXRM INFO ONLY                | INFO      | This menu provides information-only options for users who need information about reminders but do not need the ability to make changes.                                                                   |
| Reminder Dialog Management           | PXRM DIALOG MANAGEMENT        | DM        | This menu allows maintenance of the parameters used by CPRS for reminder dialog processing.                                                                                                               |

| **Option**                               | **Option Name**          | **Syn**   | **Description**                                                                                                                                                                                                                                                     |
|------------------------------------------|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Reports                         | PXRM REMINDER REPORTS    | RP        | This is a menu of Clinical Reminder reports that clinicians can use for summary and detailed level information about patients' due and satisfied reminders. This option also contains reports that clinical coordinators can use to assign menus to specific users. |
| Reminders MST Synchronization Management | PXRM MST MANAGEMENT      | MST       | This option provides the Clinical Reminders MST management options. These options give you the ability to synchronize the MST History file #29.11 with MST data recorded elsewhere and to determine when the synchronization was last done.                         |
| Reminder Patient List Menu               | PXRM PATIENT LIST MENU   | PL        | This menu contains options to manage list rules and patient lists.                                                                                                                                                                                                  |
| Reminder Orderable Item Menu             | PXM ORDER                | OI        | This menu contains options to allow sites to create Reminder Order Checks                                                                                                                                                                                           |
| Reminder Parameters                      | PXRM REMINDER PARAMETERS | PAR       | This menu contains the options, Edit Site Disclaimer and Edit Web Sites, which allow you to modify the parameters for these items.                                                                                                                                  |
| Reminder Extract Menu                    | PXRM EXTRACT MENU        | XM        | This option allows management of extract definitions, extract runs, and  extract transmissions.                                                                                                                                                                     |
| GEC Referral Report                      | PXRM GEC REFERRAL REPORT | GEC       | This is the option that is used to generate GEC Reports. GEC (Geriatrics Extended Care) is used for referral of geriatric patients to receive further care                                                                                                          |

### Reminder Computed Finding Management

A computed finding is an M routine that takes a standard set of arguments. The computed finding must be entered into the REMINDER COMPUTED FINDING file #811.4 before it can be used as a finding in a reminder definition or term. When developing a reminder definition, if particular patient data is needed and that data is not available via the standard finding types, a computed finding that searches for and returns the required data can be created and used like a standard finding.

The Clinical Reminders application provides a set of national computed findings. Sites can also create their own.

**Note:** Only programmers who have "@" access can actually write the routine and enter it into the REMINDER COMPUTED FINDINGS file. Once it is in the file, Reminders Managers can use the computed finding in reminder definitions and terms.

**Changes made by PXRM*2*26**

The national computed finding VA-REMINDER DEFINITION evaluates a reminder definition. If it is used recursively (evaluating the same definition that is calling it), it will generate framestack errors. This can wreak havoc with production systems. Remedy ticket #761925. Code was added to prevent this. Also, a check for recursion was added to the Integrity Checker.

The print name of VA-REMINDER DEFINITION was changed from VA-Reminder Definition Computed Finding to VA-Reminder Definition. The variable TEXT was not set before, but is now set to "Reminder: "\_NAME, where NAME is the .01 of the reminder being evaluated. This means that the name of the reminder definition that was evaluated will be displayed in the clinical maintenance output.

The description for VA-FILEMAN DATE was updated to make it clear that the global reminder dates PXRMDOB, PXRMDOD, and PXRMLAD can also be used with this computed finding.

The computed finding inquiry was not displaying the Type; Type was added.

When a computed finding was selected to be used as a finding in a definition or term, the description of the computed finding was displayed on the screen to help the user set it up properly. If Type was not included in the description, then it was not displayed. The computed finding help was upgraded to include Type, Class, and Description, and is now displayed with the Browser instead of just written to the screen.

In the past we have had problems with updated national computed findings being overwritten by outdated versions that were installed via Reminder Exchange. To prevent further occurrences, Reminder Exchange was modified so it will not install national computed findings. From this point on, national computed findings will only be distributed via a KIDS build.

EXPECTED SIGNER and EXPECTED COSIGNER were added as CSUBs to the VA-PROGRESS NOTE computed finding. The description was updated to include these.

When using the special Reminder Location List VA-ALL LOCATIONS in the computed finding VA-APPOINTMENTS FOR A PATIENT, a message was being erroneously displayed (Remedy ticket #916079):

^TMP(NODE,$J,1,0)=Warning Reminder Location List VA-ALL LOCATIONS

^TMP(NODE,$J,2,0)=does not contain or expand to contain any hospital   locations!

#### Reminder Computed Finding Management Menu

| **Syn.**   | **Name**                           | **Option Name**                 | **Description**                                                                                                                                |
|------------|------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| CFE        | Add/Edit Reminder Computed Finding | PXRM COMPUTED FINDING EDIT      | This option provides for editing of computed finding entries in the REMINDER COMPUTED FINDINGS file. This option requires programmer’s access. |
| CFI        | Computed Finding Inquiry           | PXRM COMPUTED FINDING INQUI  RY | Allows a user to display the information about a computed finding in an easy-to-read format.                                                   |
| CFL        | Reminder Computed Finding List     | PXRM COMPUTED FINDING LIST      | This option lists the computed findings that are defined at a site.                                                                            |

##### Steps to Create a Computed finding

NOTE: The person who performs the step is listed in parentheses.

##### Write an M routine (developer).

For a *single occurrence* computed finding, the routine takes the following arguments: (DFN, TEST,DATE,DATA,TEXT). DFN is the patient ien and will be set when the computed finding routine is called. The following variables should be set by the computed finding routine.

- TEST is the logical value of the finding, set to 1 for true and 0 for false. A value for TEST must always be returned.
- DATE is the date of the finding in FileMan format. Set it to null if the finding is false

DATA is a value associated with the finding that can be used by the CONDITION field; when the Condition is evaluated V=DATA. Additional values that can also be used in the CONDITION can be passed back in DATA. This is done using subscripts, i.e., DATA(“COLOR”)=”RED” and the CONDITION could test for color with a statement like I V(“COLOR”)=”BLUE”. The choice of what data is passed back and the associated subscripts are completely up to the programmer, however they should be well documented so the person using the computed finding knows what is available. See the DESCRIPTION field below for information on how to document your computed finding. Setting the DATA array is optional, but it must be set if a CONDITION is going to be used with the computed finding.

TEXT is text to be displayed in the Clinical Maintenance output. Setting this is optional.

Note: Now that multiple occurrence computed findings are available, creation  of new single occurrence computed finding is generally discouraged because single occurrences are less flexible and less powerful.

For a *multiple occurrence* computed finding, the routine takes the following arguments:

(DFN, NGET,BDT,EDT, NFOUND,TEST,DATE,DATA,TEXT).

The following variables will be set when the computed finding routine is called:

- DFN is the patient ien.
- NGET is the number of findings to search for.
- BDT is the beginning date and time for the finding search.
- EDT is the ending date and time for the finding search.

The following variables should be set by the computed finding routine:

NFOUND is the number of findings found in the date range, it should never be larger than NGET. If there are no true findings then NFOUND should be set to 0.

Since this form of the computed finding returns multiple occurrences, each of the following variables is an array with NFOUND entries. Entry number 1 should be the most recent in the date range, entry number 2 the second most recent, and so on up to NFOUND entries. If NGET is negative, then the date ordering should be reversed with entry 1 the oldest in the date range, entry 2 the second oldest, and so on. If there are no true findings, then NFOUND should be 0. NFOUND must have a value when the computed finding routine returns. For the Nth true occurrence, set the following values:

- TEST(N) is the logical value of the finding for occurrence N; this is set to 1 for each occurrence that is found. (Required)
- DATE(N) is the date of the finding in FileMan format for occurrence N.  (Required)
- DATA is an array of values that can be used by the CONDITION field. For the N’th occurrence set DATA(N,”VALUE”)=VALUE. You can also pass back other data using subscripts just as for a single occurrence computed finding, the only difference being the occurrence subscript comes first. For example, DATA(N,”COLOR”)=”RED”.
- TEXT(N) is text to be displayed in the Clinical Maintenance output for occurrence N. (Optional)

There is no need to set the unsubscripted values of TEST and DATE in a multi-occurrence computed finding.

In most cases it makes sense to create any new computed findings as multi-occurrence computed findings. They have more flexibility than single occurrence computed findings and can operate more efficiently. This is especially true with respect to date range searches. The multi-occurrence computed finding is passed the beginning and ending dates as parameters, so it can return results from the specified date range. The original single occurrence computed finding has no provision for passing the beginning and ending dates, so it would just return the most recent occurrence. The computed finding driver must then check the date returned to determine if it is in the date range. If it is not, then there is no way to go back and look for an older result that might be in the date range.

For a *list* computed finding, the routine takes the following arguments:

- (NGET,BDT,EDT, PLIST,PARAM)
- NGET, BDT, and EDT have the same meaning as above. (See below for a discussion of the last argument.) The routine should return the list in a ^TMP global as follows:
- ^TMP($J,PLIST,DFN,N)=DAS^DATE^FILENUM^ITEM^VALUE
- N is a number specifying the number of the occurrence. N=1 is the most recent occurrence, N=2 the second most recent occurrence, and so on. N should never exceed NGET.
- DAS is the DA string.  See the Clinical Reminder Index Technical Manual for an explanation of what a DA string is.

**NOTE** : DAS is optional for a list computed finding, but if it's not set, a NULL should be used; i.e., ^TMP($J,PLIST,DFN,N)=^DATE^FILENUM^ITEM^VALUE

- DATE is the date of the finding.
- FILENUM is the file number where the result was found.
- ITEM is the internal entry number of the item that was found.
- VALUE is the default value, if there is not one then it should be null.

If you want to use a Condition with the computed finding, then you should return the values as follows:

^TMP($J,PLIST,DFN,N,SUB)=DATA(N,”SUB”)

At a minimum, one of the subscripts must be “VALUE”; i.e., DATA(N, “VALUE”); then in the Condition you can use either V or V(“VALUE”), because V is set equal to V(“VALUE”).  If you create other subscripts, you can use them in the Condition. For example:

- ^TMP($J,PLIST,DFN,1,”VALUE”)=5
- ^TMP($J,PLIST,DFN,1,”RATE”)=5
- ^TMP($J,PLIST,DFN,1,”COLOR”)=”RED”

would mean in the Condition you could use V, V(“VALUE”), V(“RATE”) or V(“COLOR”)

The field  COMPUTED FINDING PARAMETER can be used to pass a parameter into the computed finding routine. For single and multiple occurrence computed findings, the value is passed in TEST; for list computed findings, it is passed as PARAM. The COMPUTED FINDING PARAMETER is defined as free-text field with a length of 245 characters so it can be used to pass more than one parameter. If you pass more than one parameter, you should not use “^” as the piece separator, because it will not be properly transported in Reminder Exchange. When this feature is used, it will need to be documented, so that users of the computed findings will know how to properly define the contents of the COMPUTED FINDING PARAMETER field.

Great care should be taken whenever you create a computed finding. If it is poorly written, it could affect system performance, generate errors, and produce incorrect or misleading reminder evaluation results.

Hint: make sure that you “new” all the variables you use, to avoid strange side effects.

##### Enter your computed finding into the Reminders package (developer).

Use the option Reminder Computed Finding Edit (CFE) on the Computed Findings menu to enter/register your computed finding, which makes an entry in the REMINDER COMPUTED FINDINGS file (#811.4).

File #811.4 contains a combination of nationally distributed and local entries. Nationally distributed entry names are prefixed with VA-. Local entry names can’t start with VA-.

Complete each of the following fields:

NAME (#.01 field) – Name of the computed finding. When a computed finding is added as a finding to a reminder definition, it is done using NAME. For example, type CF.VA-BMI to add the exported VA-BMI computed finding to your reminder definition.

ROUTINE (#.02 field)  - Name of the MUMPS routine.

ENTRY POINT (#.03 field) - Entry point in the MUMPS routine (the line tag at which that finding begins).

PRINT NAME (#.04 field) – This field will be displayed on the Clinical Maintenance component as the name of the computed finding. If it is blank, NAME will be used.

TYPE (#5 field) – Set of codes that specifies  the type of computed finding. “S” stands for single occurrence, “M” for multiple occurrence, and “L” for list. If TYPE s blank, single will be assumed.

CF PARAMETER REQUIRED (#6 field) – Set this field to YES, if the computed finding must have parameter(s) passed to it in order for it to work.

DESCRIPTION – Word-processing field that is used to document the computed finding. It is very important to include this field so that the person who is using the computed finding knows how to properly use it. During the definition editing process if a computed finding is selected as a finding the DESCRIPTION will be displayed to the user so the documentation for the computed finding will be right in front of them as they setup the computed finding.

CLASS (#100 field) – Set this field to LOCAL or VISN as appropriate.

The remaining fields are optional.

**Example**

Select Reminder Computed Finding Management Option: **cfe** Reminder Computed Finding Edit

Select Reminder Computed Finding: **AJEY TEST COMPUTED FINDING** ...OK? Yes// **&lt;Enter&gt;** (Yes)

NAME: AJEY TEST COMPUTED FINDING Replace **&lt;Enter&gt;** ROUTINE: **PXRMZC1** ENTRY POINT: **TEST** PRINT NAME: **Test Computed Finding**

**TYPE: ?**

**Choose from:**

**M        MULTIPLE**

**L        LIST**

**S        SINGLE**

**DESCRIPTION:**

**1&gt;**

**CLASS: LOCAL//**

**SPONSOR:**

**REVIEW DATE:**

Example: Computed finding for determining if a patient is an inpatient

If you want it to be true, set TEST to 1.

Set the DATE="" when TEST=0 and set DATE to the date of the finding when TEST=1

Set VALUE to a value that can be tested against in the CONDITION field.

TEXT just goes back as additional info in the Clinical Maintenance view.

So, if you made one that was testing for whether your patient was an inpatient, it might look like this:

INP(DFN,TEST,DATE,VALUE,TEXT)   ;

N VAIN

D INP^VADPT ;IA #10061

I +$P(VAIN(7),U,1) S TEST=1,DATE=$P(VAIN(7),U,1)

E   S TEST=0,DATE=””

D KVA^VADPT

S (TEXT,VALUE)=””

Q

In this example we are not going to use TEXT or VALUE, so they are set to null.

##### (Reminder Manager) Place the finding into your reminder.

Now that the finding is created and entered/registered, you may use it just like any other finding would be used. The prefix for selecting a computed finding is CF.  When a computed finding is selected its description will be displayed and this will provide information on how to use the selected computed finding. This is an example of adding a computed finding to a reminder definition.

Select FINDING: CF.VA-DATE FOR AGE

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

VA-DATE FOR AGE     NATIONAL

...OK? Yes// Y  (Yes)

Computed Finding Description:

This computed finding returns the date on which the patient will

reach the age (in years) specified by the value of the computed

finding parameter. Both the default value and date of the finding

will be the date in FileMan format when the patient reaches the

specified age.

Fractional ages like 59.5 are not allowed and the fractional part

will be ignored.

Editing Finding Number: 1

FINDING ITEM: VA-DATE FOR AGE//

REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

CONDITION:

CONDITION CASE SENSITIVE:

USE STATUS/COND IN SEARCH:

COMPUTED FINDING PARAMETER: 65

FOUND TEXT:

No existing text

Edit? NO//

NOT FOUND TEXT:

No existing text

Edit? NO//

#### National Computed Findings

When the need arises, a new national computed finding will be created and released. This means the list of national computed findings is dynamic, so the best way to find and use national computed findings is by using the online tools. The computed finding management option is on the Reminder Manager’s Menu:

Select OPTION NAME: REMINDER MANAGERS MENU  PXRM MANAGERS MENU     Reminder Managers Menu

CF     Reminder Computed Finding Management ...

RM     Reminder Definition Management ...

SM     Reminder Sponsor Management ...

TXM    Reminder Taxonomy Management

TRM    Reminder Term Management ...

LM     Reminder Location List Management ...

RX     Reminder Exchange

RT     Reminder Test

OS     Other Supporting Menus ...

INFO   Reminder Information Only Menu ...

DM     Reminder Dialog Management ...

CP     CPRS Reminder Configuration ...

RP     Reminder Reports ...

MST    Reminders MST Synchronization Management ...

PL     Reminder Patient List Menu ...

PAR    Reminder Parameters ...

ROC    Reminder Order Check Menu ...

XM     Reminder Extract Menu ...

VS     NLM Value Set Menu

CQM    NLM Clinical Quality Measures Menu

Select Reminder Managers Menu &lt;TEST ACCOUNT&gt; Option: CF  Reminder Computed Findi

ng Management

CFE    Add/Edit Reminder Computed Finding

CFI    Reminder Computed Finding Inquiry

CFL    Reminder Computed Finding List

Reminder Computed Finding List will list all the computed findings in your account, not just the national computed findings, so it is not the best way to get a list of just the national computed findings. The easiest way to get a list of national computed findings is to use Reminder Computed Finding Inquiry and type VA- at the prompt. Because all national content starts with the VA- prefix, this will produce a list of national computed findings.

Select Reminder Computed Finding Management &lt;TEST ACCOUNT&gt; Option: CFI  Reminder

Computed Finding Inquiry

Select COMPUTED FINDING: VA-

1   VA-ACTIVE PATIENT RECORD FLAGS       NATIONAL

2   VA-ADMISSIONS FOR A DATE RANGE       NATIONAL

3   VA-AGE       NATIONAL

4   VA-AGE BIRTH SEX LIST       NATIONAL

5   VA-AGENT ORANGE EXPOSURE       NATIONAL

...

The name of the computed finding is chosen to express the type of data the computed finding will search for. When you see one that looks like it may be what you are looking for, select it to get full details of what the computed finding does and how to set it up. That information is in the Description for all national computed findings. When adding or editing a finding in a reminder definition or term, if the finding is a computed finding, you will be ask if you want to display the help for the computed finding. If you respond YES, a help screen containing the same information shown in the inquiry will open.

A few of the national computed findings will benefit from additional documentation that is not amenable to online presentation in VistA.

**VA-APPOINTMENTS FOR A PATIENT**

This multiple occurrence computed finding returns a list of appointments for a patient in the specified date range from the Scheduling Package.

The Computed Finding Parameter can be used to specify which appointment data fields should be returned from the Scheduling package and filter the results returned based on location and status. The Computed Finding Parameter entry uses FLDS: to specify appointment data fields, STATUS: to filter specific statuses, and LL: to specify a Reminder Location List to filter locations.

FLDS, STATUS, and LL are all optional and can be defined in any order in the computed finding parameter field.

Some examples of how to use FLDS, STATUS and/or LL:

FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

STATUS:CP,CC^FLDS:25

LL:DIABETIC LOCATION

FLDS parameter information:

The appointment data fields are specified as follows:

FLDS:F1,F2,... where F1,F2,... are any of the possible ID values listed in the Available Appointment Data Fields table below.

The F1,F2,... ID values specify what data associated with the appointment will display in the clinical maintenance output. If no FLDS is specified, the default display fields will be 1,2 for APPOINTMENT DATE/TIME and CLINIC.

Additionally, each F1,F2,... specified will be returned as CSUB data that can also be used in the computed finding's CONDITION field. The CONDITION can be used to further screen the filtered appointments, returned by Scheduling, by setting the USE STATUS/CONDIN SEARCH field to YES.

For example, if you only want appointments that were checked out, use FLDS: 1,2,11 to get the APPOINTMENT DATE/TIME, CLINIC, and CHECK-OUT DATE/TIME for display purposes. The FLDS:1,2,11 will return the CSUB data "APPOINTMENT DATE/TIME", "CLINIC" and

"CHECK-OUT DATE/TIME".

CSUB values are used in the CONDITION field to do a comparison to numeric or string values. Using +V causes the CSUB data to be interpreted as as numeric. Strings that cannot be converted to a number are set to zero. For example, a CONDITION such as I +V("CHECK-OUT DATE/TIME")&gt;0 would be true if the appointment had a check-out date/time.

List of Available Appointment Data Fields table with assigned ID

ID      Field Name

--------------------------------------------------------

1     APPOINTMENT DATE/TIME

2     CLINIC

3     APPOINTMENT STATUS

4     PATIENT

5     LENGTH OF APPOINTMENT

6     COMMENTS

7     OVERBOOK

8     ELIGIBILITY OF VISIT

9     CHECK-IN DATE/TIME

10     APPOINTMENT TYPE

11     CHECK-OUT DATE/TIME

12     OUTPATIENT ENCOUNTER IEN

13     PRIMARY STOP CODE

14     CREDIT STOP CODE

15     WORKLOAD NON-COUNT

16     DATE APPOINTMENT MADE

17     DESIRED DATE OF APPOINTMENT

18     PURPOSE OF VISIT and SHORT DESCRIPTION

19     EKG DATE/TIME

20     X-RAY DATE/TIME

21     LAB DATE/TIME

22     STATUS

23     X-RAY FILMS

24     AUTO-REBOOKED APPOINTMENT DATE/TIME

25     NO-SHOW/CANCEL DATE/TIME

26     RSA APPOINTMENT ID

28     DATA ENTRY CLERK

29     NO-SHOW/CANCELED BY

30     CHECK-IN USER

31     CHECK-OUT USER

32     CANCELLATION REASON

33     CONSULT LINK

STATUS information:

STATUS: is used to set a filter on the appointment status; only those appointments with a status that matches the STATUS: values list will be returned. The possible values that the Scheduling

API allows are:

VALUE     Description

--------------------------------------------------------

R      SCHEDULED/KEPT

I      INPATIENT

NS     NO-SHOW

NSR    NO-SHOW, RESCHEDULED

CP     CANCELLED BY PATIENT

CPR    CANCELLED BY PATIENT, RESCHEDULED

CC     CANCELLED BY CLINIC

CCR    CANCELLED BY CLINIC, RESCHEDULED

NT     NO ACTION TAKEN

If STATUS is not specified the default is R,I.

The APPOINTMENT STATUS returned by the API is a summarized list which does not include detailed statuses such as Future, Checked-In, or Checked Out. These  statuses are summarized as SCHEDULED/KEPT.  As a result, a CONDITION may be required to make sure you are getting the correct results. For example, if you are looking for an appointment that was kept you would set STATUS:R combined with a CONDITION of I (+V("OUTPATIENT ENCOUNTER IEN")&gt;0)!(+V("CHECK-OUT DATE/TIME")&gt;0) with USE STATUS/COND IN SEARCH set to YES.

LL information:

LL: Reminder Location List specifies a list of locations so that only appointments for those locations will be returned. If LL is not specified, then appointments for all locations will be returned.

The following table is from the Patient Information Management System (PIMS) Technical Manual. It is documentation for the API SDAPI^SDAMA301, which is used by this computed finding to get a list of a patient’s appointments.

**Available Appointment Data Fields**

|   ID | FIELD NAME                          | DATA TYPE   | Format/Valid Values                                                                                                                                                                                                                                                                   | Description                                                                                                                         | Examples of Returned Data                                                                                                                                                                                                            |
|------|-------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    1 | APPOINTMENT DATE/TIME               | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The scheduled Appointment Date/Time                                                                                                 | 3031215.113  3031201.0815                                                                                                                                                                                                            |
|    2 | CLINIC IEN and NAME                 | TEXT        | ID^name                                                                                                                                                                                                                                                                               | Clinic IEN and name                                                                                                                 | 150;CARDIOLOGY  32;BLOOD DONOR                                                                                                                                                                                                       |
|    3 | APPOINTMENT STATUS                  | TEXT        | **R (**  Scheduled/Kept)  **I**  (Inpatient)  **NS**  (No-Show)  **NSR**  (No-Show, Rescheduled)  **CP**  (Cancelled by Patient)  **CPR**  (Cancelled by Patient, Rescheduled)  **CC**  (Cancelled by Clinic)  **CCR**  (Cancelled by Clinic, Rescheduled)  **NT**  (No Action Taken) | The status of the appointment.                                                                                                      | R;SCHEDULED/KEPT  I;INPATIENT  NS;N0-SHOW  NSR;NO-SHOW &amp; RESCHEDULED  CP;CANCELLED BY PATIENT  CPR;CANCELLED BY PATIENT &amp; RESCHEDULED  CC;CANCELLED BY CLINIC  CCR;CANCELLED BY CLINIC &amp; RESCHEDULED  NT;NO ACTION TAKEN |
|    4 | PATIENT DFN and NAME                | TEXT        | DFN;name                                                                                                                                                                                                                                                                              | Patient DFN and Patient Name                                                                                                        | 34877;REDACTED  455;REDACTED                                                                                                                                                                                                         |
|    5 | LENGTH OF APPOINTMENT               | TEXT        | NNN                                                                                                                                                                                                                                                                                   | The scheduled length of appointment, in minutes                                                                                     | 20  60                                                                                                                                                                                                                               |
|    6 | COMMENTS                            | TEXT        | free text                                                                                                                                                                                                                                                                             | Any comments associated with the appointment                                                                                        | PATIENT NEEDS WHEELCHAIR                                                                                                                                                                                                             |
|    7 | OVERBOOK                            | TEXT        | **Y**  or  **N**                                                                                                                                                                                                                                                                      | “Y” if appointment is an overbook else “N”                                                                                          | Y  N                                                                                                                                                                                                                                 |
|    8 | ELIGIBILITY OF VISIT IEN and NAME   | TEXT        | IEN;name                                                                                                                                                                                                                                                                              | Eligibility code and name associated with the appointment                                                                           | 2;AID &amp; ATTENDANCE  7;ALLIED VETERAN  13;COLLATERAL OF VET.                                                                                                                                                                      |
|    9 | CHECK-IN DATE/TIME                  | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | Date/time the patient checked in for the appointment                                                                                | 3031215.113                                                                                                                                                                                                                          |
|   10 | APPOINTMENT TYPE IEN and NAME       | TEXT        | IEN;name                                                                                                                                                                                                                                                                              | Type of Appointment IEN and name                                                                                                    | 1;COMPENSATION &amp; PENSION  3;ORGAN DONORS  7;COLLATERAL OF VET.                                                                                                                                                                   |
|   11 | CHECK-OUT DATE/TIME                 | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | Date/time the patient checked out of the appointment                                                                                | 3031215.113                                                                                                                                                                                                                          |
|   12 | OUTPATIENT ENCOUNTER IEN            | TEXT        | NNN                                                                                                                                                                                                                                                                                   | The outpatient encounter IEN associated with this appointment                                                                       | 4578                                                                                                                                                                                                                                 |
|   13 | PRIMARY STOP CODE IEN and CODE      | TEXT        | IEN;code                                                                                                                                                                                                                                                                              | Primary Stop code IEN and code associated with the clinic.                                                                          | 301;350                                                                                                                                                                                                                              |
|   14 | CREDIT STOP CODE IEN and CODE       | TEXT        | IEN;code                                                                                                                                                                                                                                                                              | Credit Stop code IEN and code associated with the clinic.                                                                           | 549;500                                                                                                                                                                                                                              |
|   15 | WORKLOAD NON-COUNT                  | TEXT        | **Y**  or  **N**                                                                                                                                                                                                                                                                      | “Y” if clinic is non-count else “N”                                                                                                 | Y  N                                                                                                                                                                                                                                 |
|   16 | DATE APPOINTMENT MADE               | DATE        | YYYMMDD                                                                                                                                                                                                                                                                               | Date the appointment was entered into the Scheduling system                                                                         | 3031215                                                                                                                                                                                                                              |
|   17 | DESIRED DATE OF APPOINTMENT         | DATE        | YYYMMDD                                                                                                                                                                                                                                                                               | The date the clinician or patient desired for the scheduling of this appointment.                                                   | 3031215                                                                                                                                                                                                                              |
|   18 | PURPOSE OF VISIT                    | TEXT        | Code (1, 2, 3, or 4) and short description (C&P, 10-10, SV, or UV)                                                                                                                                                                                                                    | The Purpose of Visit                                                                                                                | 1;C&amp;P  2;10-10  3;SV  4;UV                                                                                                                                                                                                       |
|   19 | EKG DATE/TIME                       | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The scheduled date/time of the EKG tests in conjunction with this appointment                                                       | 3031215.083                                                                                                                                                                                                                          |
|   20 | X-RAY DATE/TIME                     | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The scheduled date/time of the X-RAY in conjunction with this appointment                                                           | 3031215.083                                                                                                                                                                                                                          |
|   21 | LAB DATE/TIME                       | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The scheduled date/time of the Lab tests in conjunction with this appointment                                                       | 3031215.083                                                                                                                                                                                                                          |
|   22 | STATUS                              | TEXT        | Status Code, Status Description, Print Status, Checked In Date/Time, Checked Out Date/Time, and Admission Movement IFN                                                                                                                                                                | Status Information for the Visit.                                                                                                   | 8;INPATIENT APPOINTMENT;INPATIENT/CHECKED OUT;;3030218.1548;145844                                                                                                                                                                   |
|  23  | X-RAY FILMS                         | TEXT        | **Y**  or  **N**                                                                                                                                                                                                                                                                      | “  **Y**  ” if x-ray films are required at clinic else “  **N**  ”                                                                  | Y  N                                                                                                                                                                                                                                 |
|   24 | AUTO-REBOOKED APPOINTMENT DATE/TIME | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The date/time that the appointment was Auto-Rebooked (rescheduled) to.                                                              | 3031215.083                                                                                                                                                                                                                          |
|   25 | NO-SHOW / CANCEL DATE/TIME          | DATE/TIME   | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The date/time that the appointment was No-Showed or Cancelled.                                                                      | 3031215.083                                                                                                                                                                                                                          |
|   26 | RSA APPOINTMENT ID                  | TEXT        | NNN                                                                                                                                                                                                                                                                                   | The unique numeric Oracle ID that identifies a specific RSA appointment.  This field will be null for appointments in legacy VistA. | 34983                                                                                                                                                                                                                                |
|   28 | DATA ENTRY CLERK                    | TEXT        | DUZ;Name                                                                                                                                                                                                                                                                              | The DUZ and name of the clerk who scheduled the appointment.                                                                        | 24569;PERSON,NEW A                                                                                                                                                                                                                   |
|   29 | NO-SHOW / CANCELED BY               | TEXT        | DUZ;Name                                                                                                                                                                                                                                                                              | The DUZ and name of the clerk who no-showed or canceled the appointment.                                                            | 24569;PERSON,NEW A                                                                                                                                                                                                                   |
|   30 | CHECK IN USER                       | TEXT        | DUZ;Name                                                                                                                                                                                                                                                                              | The DUZ and name of the clerk who checked in the appointment.                                                                       | 24569;PERSON,NEW A                                                                                                                                                                                                                   |
|   31 | CHECK OUT USER                      | TEXT        | DUZ;Name                                                                                                                                                                                                                                                                              | The DUZ and name of the clerk who checked out the appointment.                                                                      | 24569;PERSON,NEW A                                                                                                                                                                                                                   |
|   32 | CANCELLATION REASON                 | TEXT        | DUZ;Name                                                                                                                                                                                                                                                                              | IEN and Name of Cancellation Reason.                                                                                                | 11;OTHER                                                                                                                                                                                                                             |
|   33 | CONSULT LINK                        | TEXT        | NNN                                                                                                                                                                                                                                                                                   | The Consult Link IEN associated with the appointment.                                                                               | 23123                                                                                                                                                                                                                                |

**Note: Field 27 is reserved for the 2507 Request IEN that will be available in a future Scheduline release.**

**VA-BMI**

The VA-BMI computed finding calculates the patient's body mass index. The value returned, which can be used in the CONDITION field of the findings, is the body mass index.

Note that date range searching is applied only to the weight and that the date of the finding is the date of the weight measurement used in the BMI calculation. The height used in the calculation will be the height measurement that occurred closest to the date of the weight measurement. This may be before or after the weight measurement.

An example of using the VA-BMI computed finding:

1)  Create a finding in a reminder that is the VA-BMI computed finding;

2)  Add logic in the CONDITION field to check for a particular BMI value: "I V&gt;25";

Example: Changing the Occurrence count in a Reminder Definition using VA-BMI

Select Reminder Definition Management Option: RE  Add/Edit Reminder Definition

Select Reminder Definition: bmi and BSA TEST    PKR BMI AND BSA TEST  LOCAL

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit: f  Findings

Reminder Definition Findings

Choose from:

CF BSA                                                          Finding #   2

CF VA-BMI                                                       Finding #   1

Select FINDING: VA-BMI

Searching for a DRUG, (pointed-to by FINDING ITEM)

Searching for a EDUCATION TOPICS, (pointed-to by FINDING ITEM)

Searching for a EXAM, (pointed-to by FINDING ITEM)

Searching for a REMINDER LOCATION LIST, (pointed-to by FINDING ITEM)

Searching for a HEALTH FACTOR, (pointed-to by FINDING ITEM)

Searching for a IMMUNIZATION, (pointed-to by FINDING ITEM)

Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM)

Searching for a MH TESTS AND SURVEYS, (pointed-to by FINDING ITEM)

Searching for a ORDERABLE ITEM, (pointed-to by FINDING ITEM)

Searching for a RADIOLOGY PROCEDURE, (pointed-to by FINDING ITEM)

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

VA-BMI     NATIONAL

...OK? Yes//   (Yes)

Computed Finding Description:

The VA-BMI computed finding calculates the patient's body mass index. The

value returned, which can be used in the CONDITION field of the findings, is

the body mass index.

An example of using the VA-BMI computed finding:

1)  Create a finding in a reminder that is the VA-BMI computed finding;

2)  Add logic in the CONDITION field to check for a particular BMI value:

"I V&gt;25";

3)  This finding will be evaluated to true for patients with a BMI that is

greater than 25.

This is a multi-occurrence computed finding.

Editing Finding Number: 1

FINDING ITEM: VA-BMI//

REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT: 5// **6      You can change the occurrence count here.**

CONDITION:

CONDITION CASE SENSITIVE:

USE STATUS/COND IN SEARCH:

COMPUTED FINDING PARAMETER:

FOUND TEXT:

No existing text

Edit? NO//

NOT FOUND TEXT:

No existing text

Edit? NO//

Reminder Definition Findings

Choose from:

CF BSA                                                          Finding #   2

CF VA-BMI                                                       Finding #   1

Select FINDING:

**VA-BSA**

This multi-occurrence computed finding returns the patient's body surface area (BSA) as a value that can be used in the CONDITION field. The COMPUTED FINDING PARAMETER can be used to select which formula is used to calculate the BSA.

#### COMPUTED FINDING PARAMETER  FORMULA

M               Mosteller

D                DuBois and Dubois

H                Haycock

G                Gehan and George

B                Boyd

The default is to use the Mosteller formula. Unless there is a reason to use one of the other formulas, the recommendation is to use the default, because it is faster to calculate and the numerical results are very close to those of the other formulas.

Formulas for Body Surface Area Calculator

The Mosteller formula

BSA (m²) = ( [Height(cm) x Weight(kg) ]/ 3600 ) ½ e.g. BSA = SQRT( (cm*kg)/3600 )

or in inches and pounds:     BSA (m²) = ( [Height(in) x Weight(lbs) ]/ 3131 ) ½

The DuBois and DuBois² formula

BSA (m²) = 0.20247 x Height(m) 0.725 x Weight(kg) 0.425

A variation of DuBois and DuBois that gives virtually identical results is:

BSA (m²) = 0.007184 x Height(cm) 0.725 x Weight(kg) 0.425

The Haycock formula

BSA (m²) = 0.024265 x Height(cm) 0.3964 x Weight(kg) 0.5378

The Gehan and George formula

BSA (m²) = 0.0235 x Height(cm) 0.42246 x Weight(kg) 0.51456

The Boyd formula

BSA (m 2 ) = 0.0003207 x Height(cm) 0.3 x Weight(grams) (0.7285 - ( 0.0188 x LOG(grams) )

References

1. Mosteller RD: Simplified Calculation of Body Surface Area. N Engl J Med 1987 Oct 22;317(17):1098 (letter)
2. DuBois D; DuBois EF: A formula to estimate the approximate surface area if height and weight be known. Arch Int Med 1916 17:863-71.
3. Haycock G.B., Schwartz G.J.,Wisotsky D.H.  Geometric method for measuring body surface area: A height weight formula validated in infants, children and adults.   The Journal of Pediatrics 1978  93:1:62-66
4. Gehan EA, George SL, Estimation of human body surface area from height and weight.   Cancer Chemother Rep 1970 54:225-35.
5. Boyd E, The growth of the surface area of the human body. Minneapolis: university of Minnesota Press, 1935.  (I never found the original source. Instead, I copied the formula from: http://www.ispub.com/journals/IJA/Vol2N2/bsa.htm )

Note that the changes to VA-BMI (only applying the date range criteria to the weight) also apply to the VA-BSA computed finding, because it uses the same routine to obtain matched weight and height

**VA-IS INPATIENT**

Print Name:             VA-Is Inpatient

Class:                  NATIONAL

Sponsor:

Review Date:

Description:

This computed finding will be true if the patient was/is an inpatient on the evaluation date. The following "CSUB" values will be available:

ADMISSION DATE/TIME (FileMan format)

ADMISSION TYPE

ATTENDING PHYSICIAN

DATE (FileMan format)

PRIMARY PROVIDER

TREATING SPECIALITY

WARD LOCATION

:

Entry Point: INP        Routine:    PXRMPDEM

**Example** :

**Determining if the inpatient is on ward 7 EAST or 7 WEST** (these are mental health inpatient locations)

I (V("WARD LOCATION")="7 EAST (SEA)")!(V("WARD LOCATION")="7 WEST (SEA)")

--STATUS-- --DUE DATE--  --LAST DONE--

Ment Hlth Inpatient Locations          N/A

Patient is not on an inpatient mental health ward.

Information:

Computed Finding: Is patient admitted as inpatient?

10/01/2010 value - 23^3 EAST (SEA)

==================

--STATUS-- --DUE DATE--  --LAST DONE--

Ment Hlth Inpatient Locations        DUE NOW     DUE NOW       unknown

Cohort:

Computed Finding: Is Inpatient

12/06/2010; Patient is an inpatient; admission date/time:

08/13/2010@10:12:17

Information:

Computed Finding: Is patient admitted as inpatient?

08/13/2010 value - 27^7 EAST (SEA)

### Reminder Definition Management

This menu contains options for creating, editing, copying, activating, and displaying clinical reminder definitions.

National Reminders, identified by having a CLASS of NATIONAL and a name starting with VA-, cannot be edited. If you cannot use a national reminder “as is” then copy to a new name, at which point it becomes local, and then edit the reminder to meet your requirements.

Sites may change anything in a local reminder definition to meet their needs. Findings at each site may require modification to represent local use of clinical data.

| Syn.   | Name                              | Option Name                  | Description                                                                                                                                                                                                                                                                                      |
|--------|-----------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RA     | Activate/Inactivate Reminders     | PXRM (IN)/ACTIVATE REMINDERS | This option is used to make reminders active or inactive.                                                                                                                                                                                                                                        |
| RE     | Add/Edit Reminder Definition      | PXRM DEFINITION EDIT         | This option is used to create or edit Clinical Reminder Definitions. Nationally distributed reminder definitions items all have a "VA-"prefix. VA- for Ambulatory Care EP reminders and VA-* for National Center for Health Promotion reminders.                                                 |
| RC     | Copy Reminder Definition          | PXRM DEFINITION COPY         | This option allows you to copy an existing reminder definition into a new reminder definition in the Clinical Reminder Definition file (#811.9). Once a new name is defined for the new reminder definition, the new reminder definition can be edited to reflect the local reminder definition. |
| RI     | Inquire about Reminder Definition | PXRM DEFINITION INQUIRY      | This option allows you to display a clinical reminder definition in an easy to read format.                                                                                                                                                                                                      |
| RL     | List Reminder Definitions         | PXRM DEFINITION LIST         | This option provides a brief summary of selected Clinical Reminder definitions.                                                                                                                                                                                                                  |
| RH     | Reminder Edit History             | PXRM REMINDER EDIT HISTORY   | This option allows you to display a reminder definition's edit history. Edit history was formerly displayed as part of the Definition Inquiry, but was removed and made available within this option.                                                                                            |
| ICS    | Integrity Check Selected          | PXRM DEF INTEGRITY CHECK ONE | This option lets the user select a reminder definition for integrity checking.                                                                                                                                                                                                                   |
| ICA    | Integrity Check All               | PXRM DEF INTEGRITY CHECK ALL | This option runs the integrity check for all reminder definitions on the system.                                                                                                                                                                                                                 |
| PNE    | Definition Print Name Edit        | PXRM DEF PRINT NAME EDIT     | This option allows editing of the Print Name for national reminder definitions. Sites were often copying national definitions to local definitions just to edit the Print Name, with this option that is no longer necessary.                                                                    |
| PNR    | Definition Print Name Report      | PXRM DEF PRINT NAME REPORT   | This option runs a report than finds all reminder definitions whose Print Name was edited via the option PXRM DEF PRINT NAME EDIT.                                                                                                                                                               |

#### Patch 45 (PXRM*2*45) Changes to Reminder Definitions

#### Added a new possible value to the Reminder Definition Usage Field:
A: Action

#### The “A” will not allow a reminder to be used on the CPRS coversheet unless the value of C is set also in the usage field.

#### Patch 24 (PXRM*2*24) High Risk Mental Health Patient - Reminder and Flag: Changes to Reminder Definitions

1. New Reminder Definitions:
    - VA-MH HIGH RISK NO-SHOW ADHOC RPT
No reminder dialog is associated with this reminder. This new Reminder Definition looks for the first appointment found, given a date and time and looking through the rest of the day. It is resolved if the finding is documented within 1 week. It is used by the SD MH NO SHOW AD HOC REPORT to get Results related to the follow-up reminder for each missed appointment date/time, if results are available.
Example of Results section that prints after the Future Scheduled Appointments:
Future Scheduled Appointments: NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS
Results:
Resolution: Last done 05/14/2012@12:00
Reminder Term: VA-MH NOSHOW PT EMERGENT CARE
Health Factor: MH NOSHOW PT EMERGENT CARE
05/14/2012@12:00
Reminder Term: VA-MH SUICIDE ATTEMPTED
Health Factor: MH SUICIDE ATTEMPTED
05/14/2012@12:00
    - **VA-MHTC NEEDS ASSIGNMENT**
        - This reminder looks for the most recent three completed appointments to MH clinics over the past year and checks to see if an MHTC is currently assigned to the patient. If no MHTC is assigned, the reminder will be due.
        - The reminder definition uses the new VA-PCMM MHTC computed finding.
        - There is no reminder dialog related to this reminder.
        - This reminder can be used from CPRS to show as due on the CPRS GUI Cover Sheet.
        - This reminder can also be used from Reminder Reporting options/Reminder Due Report. Reminder CACs can create a Reminder Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC.
        - Uses Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA-Appointments for a Patient. **The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.**
        1. Changed the dialog info text presented to the user to clarify that the reminder is resolved if a completed encounter is found for  a MH appointment on the same day, or within 72 hours of the missed MH appointment.
    <!-- image -->
        1. Added Category I PRF for HIGH RISK FOR SUICIDE to the Reminder Definition.  The reminder now looks for both the Category I and Category II active PRF for High Risk for Suicide.
    --STATUS-- --DUE DATE--  --LAST DONE--
    High Risk MH No-Show Follow-up       DUE NOW     DUE NOW       unknown
    Frequency: Due every 99Y - Once for all ages.
    Reminder triggered by missed MH appointment and when resolved won't be due
    again until another missed MH appointment occurs.
    The patient has an active High Risk for Suicide Patient Record Flag and missed a MH appointment.
    Cohort:
    Reminder Term: VA-MH NOSHOW MISSED MH CLINIC APPTS
    Computed Finding: VA-Appointments for a Patient
    04/09/2012@12:00 value - Mental Health
    CLINIC: Mental Health
    APPOINTMENT STATUS: NO-SHOW
    Reminder Term: VA-MH HIGH RISK FOR SUICIDE PRF
    Computed Finding: VA-Patient Record Flag Information
    01/31/2012@11:08:45 value - NEW ASSIGNMENT;
    Flag - HIGH RISK FOR SUICIDE(I (NATIONAL)).
    Assigned Jan 31, 2012@11:08:45 by CRPROVIDER,SIX. New record flag
    assignment.
    12/21/2010@15:36:02 value - NEW ASSIGNMENT;
    Flag - HIGH RISK FOR SUICIDE(II (LOCAL)).
    Assigned Dec 21, 2010@15:36:02 by CRPROVIDER,TWO. New record flag assignment.
        1. Change to VA-MH HIGH RISK NO-SHOW FOLLOW-UP reminder definition:
            - Removed Occurrence Count of 5 from RT.VA-MH NOSHOW MISSED MH CLINIC
        APPTS Hospital Location and only defined occurrence at the Reminder Definition level.
        It still looks back 10D and resolves with specific health factors entered from the reminder dialog the same day or a completed MH Appointment within 8 hours before or 72 hours after.
            - Modifies the Reminder Dialog to include the Suicide Behavior Report(SBR) for optional entry.
            - If there are several No-show appointments for a given day, responses to any of the no-show appointments (even the earliest appointment) on that day will resolve all of the no-show follow-ups for that day.
        No-show health factors entered at any time on the date of the missed appointment  resolve all no-show appointment follow-up on that day.
        Example:
        <!-- image -->
        <!-- image -->
        **Example: Clinical Maintenance output after selecting 8am appointment**
            1. Three terms were removed (VA-MH NOSHOW SUPPORT CONTACT, VA-MH NOSHOW INITIATE WELLNESS CHECK, VA-MH NOSHOW UNABLE TO REACH PT) from the reminder definition, since they are no longer valid responses in the related reminder dialog.
            2. New functionality was added that gives Clinical Reminders the ability to send notifications.  The specific notification is SUICIDE ATTEMPTED /COMPLETED.
            3. For list-type reminders, the definition integrity checker was not correctly checking the Baseline Age Findings to make sure that an age range was defined. This was corrected.

#### Patch 18 (PXRM*2*18- High Risk Mental Health Patient - Reminder and Flag-phase 1)  Updates for Reminder Definitions

#### Changes to National Reminder Definitions

Summary:

1. Updated branching logic reminders for OEF/OIF screening:
    1. Fixed the problem that patients who do not have the required LSSD entry are not having the items show as due when they have been done.
    2. Removed refusals and other exclusions from the branching logic – if not done, then show the item as open and allow the parent reminder to use the exclusions instead of also evaluating them in the branching logic.  This makes all 7 of the branching logic reminders consistent.
2. Updated the URLs for MH screening.
3. Added '0' to the Within Category Rank for EF-NO BLAST/EXPLOSION INJURY and EF-NO BULLET INJURY in the reminder VA-EMBEDDED FRAGMENTS RISK EVALUATION.
4. Added occurrence count of 4 to AUD C in the alcohol screening reminder.
5. Fixed header/info text in AAA reminder.
6. Distributed H1N1 reminders and dialog via patch and distribute and inactivate.
7. Updated VA-ALCOHOL F/U POS AUDIT-C dialog to display the education and advice interventions without a box around both and also to have the results of an AUDIT-10 go into the progress note.
8. Distributed the updates to the VA-MHV INFLUENZA VACCINE reminder.

Detailed Descriptions:

1. Updated branching logic reminders

VA-BL DEPRESSION SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Resolution: changed to resolve for any entry that is not before the LSSD

Changed the logic from

MRD(VA-DEPRESSION SCREEN NEGATIVE,VA-DEPRESSION SCREEN POSITIVE)&gt;MRD(VA-LAST SERVICE SEPARATION DATE)

To

MRD(VA-DEPRESSION SCREEN POSITIVE,VA-DEPRESSION SCREEN NEGATIVE)'&lt;MRD(VA-LAST SERVICE SEPARATION DATE)

VA-BL ALCOHOL SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Removed exclusions

Resolution: changed to resolve for any entry that is not before the LSSD

VA-BL PTSD SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Removed exclusions

Resolution: changed to resolve for any entry that is not before the LSSD

Added a '0' to the Within Category Rank for the health factors.

VA-BL OEF/OIF EMBEDDED FRAGMENTS

VA-BL OEF/OIF FEVER

VA-BL OEF/OIF GI SX

VA-BL OEF/OIF SKIN SX

Removed RT.VA-IRAQ/AFGHAN PERIOD OF SERVICE and substitute CF.VA-LAST SERVICE SEPARATION DATE

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Resolution: changed to resolve for any entry that is not before the LSSD

2.	Updated URLs

VA-ALCOHOL USE SCREEN (AUDIT-C)

VA-DEPRESSION SCREENING

VA-PTSD SCREENING

1. VA-EMBEDDED FRAGMENTS RISK EVALUATION: Added '0' to the Within Category Rank for EF-NO BLAST/EXPLOSION INJURY and EF-NO BULLET INJURY

1. VA-ALCOHOL USE SCREENING (AUDIT-C)
    1. Added occurrence count of 4 to AUD C in the alcohol screening reminder
    2. Updated the dialog by changing 'Optional open and optional complete (partial complete possible)' to 'Optional open and required complete or cancel before finish'.

1. Fixed grammatical error in VA-TEXT INFO SCREEN FOR AAA

1. Distributing reminders VA-INFLUENZA H1N1 IMMUNIZATION, VA-INFLUENZA H1N1 IMMUNIZATION HIGH RISK, and dialog VA-INFLUENZA H1N1 IMMUNIZATION (DIALOG).  Distribute as INACTIVE.

1. Updated VA-ALCOHOL F/U POS AUDIT-C dialog to display the education and advice interventions without a box around both and also to have the results of an AUDIT-10 go into the progress note.  Added an * to the word 'required' in 2 of the captions.

1. Distributing the updates to the VA-MHV INFLUENZA VACCINE reminder which update the age range and also the date of the reminder term for vaccination for the '10-'11 flu season.

**Enhancements in Patch 18**

**New options**

Two new options were added to the reminder definition management menu:

- Integrity Check Selected
- Integrity Check All.

These can be used to check the integrity of selected or all reminder definitions. The integrity check will also be made automatically whenever a reminder definition has been edited. Fatal errors (F) that will prevent the reminder from working properly and warnings (W) will be given. The following checks are made:

F – Each finding is checked to make sure it exists

F – If either the Beginning Date/Time or Ending Date/Time contains FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”), the definition is checked to make sure it contains finding M, and if an occurrence is used, the Occurrence Count of finding M is checked to make sure it is greater than or equal to N.

F- Function findings functions of the form FUNCTION(M) and FUNCTION(M,N) are checked to make sure finding M is in the definition and the Occurrence Count of finding M is greater than or equal to N.

F – If a Custom Date Due is defined, it is checked to make sure that the findings used in the Custom Date Due all exist in the definition.

F – Patient Cohort Logic and Resolution Logic are checked to make sure that the findings used in the logic all exist in the definition.

F – Logic strings are checked to make sure their syntax is valid.

F – The definition contains Resolution Logic but does not have a baseline frequency or any findings that will set a frequency.

W – The Usage field contains a “P” and it is not a national reminder

W – The definition contains Resolution Logic but does not have a baseline frequency. It does have findings that will set a frequency. This could be a problem if all findings that set frequency are false.

New functionality was added to allow using the date of one finding to set the date range of another finding. The syntax for the date of a finding is FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”), where M is the finding number and N is the occurrence. This means you can now use dates like FIEVAL(3,”DATE”)-3W as the Beginning or Ending Date/Time of another finding. The global reminder dates PXRMDOB and PXRMLAD can also be used. Note that if FIEVAL(M) is false or PXRMLAD does not exist, then the finding whose date range depends on the date of finding M will be set to false.

In conjunction with allowing FIEVAL(M,N,”DATE”) to be used in Beginning Date/Time or Ending Date/Time, additional frequency units were added. The allowed values are now: H (hours), D (days), W (weeks), M (months), and Y (years). This change applies everywhere that a frequency can be used, including Beginning Date/Time, Ending Date/Time, Reminder Frequency in the Baseline Age Findings multiple, Findings multiple, Function Findings multiple, and Custom Date Due. Custom Date Due will now allow both “+” and “-“; in the past it only allowed “+”.

**Fixes**

Remedy ticket #360708 reported a problem with the incorrect calculation of the resolution date when the resolution logic contains function findings. This was because the resolution date calculation was not properly differentiating between true and false function findings. This was corrected.

Remedy ticket #413731 pointed out a problem with non-VA meds that turned out to be two problems. The first is the existing issue where the Index for non-VA meds has incorrect entries. Remedy ticket #347730 reporting this problem was submitted September 4, 2009 and it still has not been fixed by Pharmacy. The second problem was a display issue. By default, the date of a drug finding is the stop date. If USE START DATE is true, the date of a drug finding is the start date. However, even when USE START DATE was true, the stop date was being displayed as the date of the finding. That has been corrected so that now whichever date is selected for the drug finding will be displayed as its finding date.

The Clin2 support team pointed out that the value for blood pressure can come back in either of the following forms: SYSTOLIC/DIASTOLIC or SYSTOLIC/MEAN/DIASTOLIC ( the second form is not very common). If the second form comes back, then the DIASTOLIC CSUB would have the value for mean, and if $P was used in a Condition, it would also be the mean. The code was changed so that the DIASTOLIC CSUB will always have the correct value. If you are using $P in a Condition, we recommend that you replace it with the appropriate CSUBs. Several national definitions and terms were originally distributed with Conditions using $P; as part of this patch they will be updated to use the SYSTOLIC and DIASTOLIC CSUBs.

The following updates are made:

**Definitions** :

VA-HTN ASSESSMENT BP &gt;=140/90

FI(11)   CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)

changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

FI(13)  CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to  I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

VA-HTN ASSESSMENT BP &gt;=160/100

FI(13) CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

VA-HTN LIFESTYLE EDUCATION

FI(11) CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)  changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

**Terms** :

VA-BP &gt;130/80

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;130!($P(V,"/",2)&gt;80)

changed to I (V("SYSTOLIC")&gt;130)!(V("DIASTOLIC")&gt;80)

VA-BP &gt;130/80 (ANY OF LAST 3)

Mapped item 1: CONDITION: I $P(V,"/",1)&gt;130!($P(V,"/",2)&gt;80)  changed to I (V("SYSTOLIC")&gt;130)!(V("DIASTOLIC")&gt;80)

VA-BP &gt;=140/90

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)

changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

VA-BP &gt;=160/100

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

On the Nov 19, 2010 national reminder call, there was a discussion about frequency being required. If there is no resolution logic, then frequency is not required as long as AGE is not in the cohort logic (because age is associated with a frequency). When there was no frequency, the status was being returned as CNBD even if there was no resolution logic and no age in the cohort logic. This was changed so that as long as there is no AGE in the cohort logic and no resolution logic, the status will be either DUE or N/A.

There were a couple of errors in the description of the **Usage field** .

Original Description:

The Usage field describes how the reminder definition will be used. This field must contain C if the reminder is to be selected in CPRS. The L or the O values will override all other values. For example, if L and C are defined in the usage field, the Reminder will not show on the cover sheet in CPRS, because L is in the Usage field.

This is free text field and can contain any combination of the following codes:

Code  Usage

C     CPRS

L     Reminder Patient List

O     Reminder Order Checks

P     Patient

R     Reminder Reports

X     Reminder Extracts

*     All of the above, except L, and O.

Corrected Description:

The Usage field describes how the reminder definition can be used. This field must contain C or * if the reminder is to be selected in CPRS. The L or the O values will override all other values. For example, if L and C are defined in the Usage field, the Reminder will not show on the cover sheet in CPRS, because L is in the Usage field.

This is free text field and can contain any combination of the following codes:

Code  Usage

C    CPRS

L    Reminder Patient List

O    Reminder Order Checks

P    Patient

R    Reminder Reports

X    Reminder Extracts

*    All of the above, except L, O, and P.

##### Steps to Define a Working Reminder

There are two parts to creating a working clinical reminder.

*Reminder definition:* This describes the patients the reminder applies to, how often it is given, and what resolves or satisfies the reminder.

*Process Issues:* The process issues include who will use the reminder and how the data will be captured. The process issues are extremely important; if they are not worked out, the reminder will never function as intended, even if the definition is correct.

These are the basic steps for defining a reminder. More detailed instructions for creating reminders and dialogs are provided in chapters that follow. As you become more experienced, you will probably develop your own process, but this provides a good starting place.

1. Write the reminder definition in a narrative form that clearly describes what you want the reminder to do. Use this narrative to identify patient data you need and how to capture it. Determine what characteristics the reminder will have (make a list). Which patients will the reminder be applicable for: age ranges, sex, diagnoses, etc. What satisfies the reminder and what makes it not applicable: diagnoses, lab results, x-rays, education, etc.

Reminders provide answers to the questions:

WHO (findings and patient cohort logic)

WHAT resolves the reminder (findings and resolution logic)

WHEN (frequency)

WHERE this reminder will likely be resolved (location/provider)

1. Review existing reminders to see if there is an existing reminder that is close to what you need.

*List Reminder Definitions, Reminder Definition Management Menu*

*Inquire about a Reminder Definition, Reminder Definition Management Menu*

1. Create new findings if they are required. For example, you may need exams or health factors. *Option: PCE Table Maintenance on Other Supporting Menus*
2. Copy the existing reminder and edit it to meet your needs, or define a new reminder. *Copy Reminder Definition or Add/Edit Reminder Definition,*
3. Test your reminder definition by evaluating the reminder for test patients. You should have patients who are in the cohort and who are not in the cohort. For patients who are in the cohort, you should have some who have the reminder resolved and some who do not. *Options: Test Reminder on the Reminder Management Menu, Health Summary Coordinator’s Menu; Clinical Maintenance in CPRS;*
4. Create a reminder dialog (following instructions in the Reminder Dialog section of this manual), if desired, for resolving the reminder in CPRS.
5. Once you are certain the reminder works as intended, set it up in one or more of the following applications:
    - Add it to a health summary
    - Make it available to users through the CPRS GUI**NOTE** : The procedure for making a health summary available in the CPRS GUI is found on page 258 .

#### List Reminder Definitions

This option prints a summary of reminder definitions. You can limit the list by several criteria: all reminders, all national reminders, all local reminders, print name, or .01 name.

#### Inquire About Reminder Item

You can select a specific reminder to see all the details.

Select Reminder Definition Management Option: RI  Inquire about Reminder Definition

Select REMINDER DEFINITION: VA-MH HIGH RISK NO-SHOW FOLLOW-UP       NATIONAL

DEVICE: ;;999  HOME

REMINDER DEFINITION INQUIRY                     Jul 20, 2012 10:02:07 am  Page 1

--------------------------------------------------------------------------------

VA-MH HIGH RISK NO-SHOW FOLLOW-UP                                No. 406

--------------------------------------------------------------------------------

Print Name:             High Risk MH No-Show Follow-up

Class:                  NATIONAL

Sponsor:                Office of Mental Health Services

Review Date:

Rescission Date:

Usage:                  CPRS, DATA EXTRACT, REPORTS

Related VA-* Reminder:

Reminder Dialog:        VA-MH HIGH RISK NO SHOW FOLLOW-UP

Priority:

Description:

This reminder shall determine whether Mental Health (MH) professionals have

followed up on a No-Show MH appointment for a patient with an active High

Risk for Suicide Patient Record Flag.

The reminder requires clinicians to initiate follow-up with the patient to

insure his/her safety and to try to get the patient back into care. The

follow-up results are documented with health factors.

Studies show that individuals that get lost to follow-up have a higher rate

of actual suicide than those that stay connected with care.

If the patient has a completed encounter to a MH appointment on the same

day, or within 72 hours of the missed MH appointment, follow-up will no

longer be necessary.

Technical Description:

Baseline Frequency:

Do In Advance Time Frame:  Do if DUE within 99Y - Once

Sex Specific:

Ignore on N/A:

Frequency for Age Range:  99Y - Once for all ages

Match Text:  Reminder triggered by missed MH appointment

and when resolved won't be due again until

another missed MH appointment occurs.\\

No Match Text:

Findings:

---- Begin: VA-MH NOSHOW MISSED MH CLINIC APPTS (FI(1)=RT(809)) ----------

Finding Type: REMINDER TERM

Use in Patient Cohort Logic: AND

Beginning Date/Time: T-10D

Ending Date/Time: T

Occurrence Count: 5

Computed Finding Parameter: FLDS:1,2,3^STATUS:NS,NSR^LL:VA-MH NO SHOW APPT

CLINICS LL

Mapped Findings: CF.VA-APPOINTMENTS FOR A PATIENT

Computed Finding Parameter: FLDS:1,2,3^STATUS:NS,NSR^LL:VA-MH NO SHOW

APPT CLINICS LL^

---- End: VA-MH NOSHOW MISSED MH CLINIC APPTS ----------------------------

---- Begin: VA-MH HIGH RISK FOR SUICIDE PRF (FI(2)=RT(811)) --------------

Finding Type: REMINDER TERM

Use in Patient Cohort Logic: AND

Beginning Date/Time: FIEVAL(1,1,"DATE")

Ending Date/Time: FIEVAL(1,1,"DATE")+1D

Occurrence Count: 2

Mapped Findings: CF.VA-PATIENT RECORD FLAG

INFORMATION

Computed Finding Parameter: HIGH RISK FOR SUICIDE^L

Mapped Findings: CF.VA-PATIENT RECORD FLAG

INFORMATION

Computed Finding Parameter: HIGH RISK FOR SUICIDE^N

---- End: VA-MH HIGH RISK FOR SUICIDE PRF --------------------------------

---- Begin: VA-MH NOSHOW PT CONTACTED (FI(3)=RT(812)) --------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Occurrence Count: 3

Mapped Findings: HF.MH NOSHOW PT CONTACTED

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW PT CONTACTED --------------------------------------

---- Begin: VA-MH NOSHOW PT EMERGENT CARE (FI(4)=RT(818)) ----------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW PT EMERGENT CARE

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW PT EMERGENT CARE ----------------------------------

---- Begin: VA-MH NOSHOW SUPPORT CONTACT (FI(5)=RT(819)) -----------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW SUPPORT CONTACT

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW SUPPORT CONTACT -----------------------------------

---- Begin: VA-MH NOSHOW PT CALLED 3X UNSUCCESSFUL (FI(6)=RT(821)) -------

Finding Type: REMINDER TERM

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW PT CALLED 3X

UNSUCCESSFUL

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW PT CALLED 3X UNSUCCESSFUL -------------------------

---- Begin: VA-MH NOSHOW PLAN DEVELOPED (FI(8)=RT(827)) ------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW PLAN DEVELOPED

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW PLAN DEVELOPED ------------------------------------

---- Begin: VA-MH NOSHOW INITIATE WELLNESS CHECK (FI(9)=RT(830)) ---------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW INITIATE WELLNESS

CHECK

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW INITIATE WELLNESS CHECK ---------------------------

---- Begin: VA-MH NOSHOW OUTREACH LETTER (FI(10)=RT(832)) ----------------

Finding Type: REMINDER TERM

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW OUTREACH LETTER

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW OUTREACH LETTER -----------------------------------

---- Begin: VA-MH NOSHOW OTHER OUTCOME (FI(11)=RT(831)) ------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW OTHER OUTCOME

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW OTHER OUTCOME -------------------------------------

---- Begin: VA-MH SUICIDE ATTEMPTED (FI(12)=RT(833)) ---------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH SUICIDE ATTEMPTED

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH SUICIDE ATTEMPTED ----------------------------------------

---- Begin: VA-MH SUICIDE COMPLETED (FI(13)=RT(834)) ---------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH SUICIDE COMPLETED

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH SUICIDE COMPLETED ----------------------------------------

---- Begin: VA-MH APPT KEPT (FI(14)=RT(835)) -----------------------------

Finding Type: REMINDER TERM

Use in Resolution Logic: OR

Beginning Date/Time: FIEVAL(1,1,"DATE")-8H

Ending Date/Time: FIEVAL(1,1,"DATE")+72H

Occurrence Count: 4

Found Text: Patient kept a MH appointment within 72 hours

of the missed MH appointment, resolving the

reminder.

Mapped Findings: CF.VA-APPOINTMENTS FOR A PATIENT

Condition: I +V("OUTPATIENT ENCOUNTER

IEN")&gt;0!+V("CHECK-OUT DATE/TIME")&gt;0

Use Status/Cond in Search: YES

Computed Finding Parameter: FLDS:1,2,3,11,12^STATUS:R^LL:VA-MH NO SHOW

APPT CLINICS LL

---- End: VA-MH APPT KEPT ------------------------------------------------

---- Begin: VA-MH NOSHOW UNABLE TO REACH PT (FI(15)=RT(836)) -------------

Finding Type: REMINDER TERM

Beginning Date/Time: FIEVAL(1,1,"DATE")

Mapped Findings: HF.MH NOSHOW UNABLE TO REACH PT

Health Factor Category: MH NOSHOW MANAGEMENT

---- End: VA-MH NOSHOW UNABLE TO REACH PT --------------------------------

Function Findings:

---- Begin: FF(1)---------------------------------------------------------

Function String: MRD(1)&gt;MRD(3,4,5,8,9,11,12,13)

Expanded Function String:

MRD(VA-MH NOSHOW MISSED MH CLINIC APPTS)&gt;MRD(VA-MH NOSHOW PT CONTACTED,

VA-MH NOSHOW PT EMERGENT CARE,VA-MH NOSHOW SUPPORT CONTACT,

VA-MH NOSHOW PLAN DEVELOPED,VA-MH NOSHOW INITIATE WELLNESS CHECK,

VA-MH NOSHOW OTHER OUTCOME,VA-MH SUICIDE ATTEMPTED,

VA-MH SUICIDE COMPLETED)

Use in Patient Cohort Logic: AND

---- End: FF(1) ----------------------------------------------------------

General Patient Cohort Found Text:

The patient has an active High Risk for Suicide Patient Record Flag and

missed a MH appointment.

General Patient Cohort Not Found Text:

This patient has no missed MH appointment pending follow-up.

Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient:

(SEX)&amp;(AGE)&amp;FI(1)&amp;FI(2)&amp;FF(1)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)&amp;FI(VA-MH NOSHOW MISSED MH CLINIC APPTS)&amp;

FI(VA-MH HIGH RISK FOR SUICIDE PRF)&amp;FF(1)

Default RESOLUTION LOGIC defines findings that resolve the Reminder:

FI(3)!FI(4)!FI(5)!FI(8)!FI(9)!FI(11)!FI(12)!FI(13)!FI(14)

Expanded Resolution Logic:

FI(VA-MH NOSHOW PT CONTACTED)!FI(VA-MH NOSHOW PT EMERGENT CARE)!

FI(VA-MH NOSHOW SUPPORT CONTACT)!FI(VA-MH NOSHOW PLAN DEVELOPED)!

FI(VA-MH NOSHOW INITIATE WELLNESS CHECK)!FI(VA-MH NOSHOW OTHER OUTCOME)!

FI(VA-MH SUICIDE ATTEMPTED)!FI(VA-MH SUICIDE COMPLETED)!

FI(VA-MH APPT KEPT)

Web Sites:

Select REMINDER DEFINITION:

#### Add/Edit Reminder Definition

You can define a reminder through this option or through the Copy Reminder Definition.

To edit existing reminders, a sub-menu is displayed that allows selection of specific fields in the reminder definition for edit. Only local or VISN reminders can be edited.

Select Reminder Definition Management Option: **Add/Edit Reminder Definition**

Select Reminder Definition:  JG DIABETIC EYE EXAM     LOCAL

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit: a  All reminder details

NAME: JG DIABETIC EYE EXAM  Replace

PRINT NAME: Diabetic Eye Exam//

CLASS: LOCAL//

SPONSOR:

REVIEW DATE: MAY 3,2000//

USAGE: C//

RELATED REMINDER GUIDELINE:

INACTIVE FLAG:

RESCISSION DATE:

REMINDER DESCRIPTION:

Patients with the VA-DIABETES taxonomy should have a diabetic eye exam

done yearly.

Edit? NO//

TECHNICAL DESCRIPTION:

This reminder is based on the Diabetic Eye Exam reminder from the New

York VAMC which was designed to meet the guidelines defined by the PACT

panel.  Additional input came from the Saginaw VAMC.

Edit? NO//

PRIORITY:

Baseline Frequency

DO IN ADVANCE TIME FRAME: 1M//

SEX SPECIFIC:

IGNORE ON N/A:

Baseline frequency age range set

Select REMINDER FREQUENCY: 0Y//

REMINDER FREQUENCY: 0Y//

MINIMUM AGE:

MAXIMUM AGE:

AGE MATCH TEXT:

No existing text

Edit? NO//

AGE NO MATCH TEXT:

No existing text

Edit? NO//

Select REMINDER FREQUENCY:

Reminder Definition Findings

Choose from:

EX      DIABETIC EYE EXAM

TX      VA-DIABETES

Select FINDING: ex.DIAB

Searching for a EXAM, (pointed-to by FINDING ITEM)

DIABETIC EYE EXAM

...OK? Yes//   (Yes)

FINDING ITEM: DIABETIC EYE EXAM//

MINIMUM AGE:

MAXIMUM AGE:

REMINDER FREQUENCY:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC: OR//

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

CONDITION:

Function Findings

Select FUNCTION FINDING: ?

You may enter a new FUNCTION FINDINGS, if you wish

Enter the number of the function finding you are defining

Select FUNCTION FINDING:

Patient Cohort and Resolution Logic

CUSTOMIZED PATIENT COHORT LOGIC (OPTIONAL):

GENERAL PATIENT COHORT FOUND TEXT:

No existing text

Edit? NO//

GENERAL PATIENT COHORT NOT FOUND TEXT:

No existing text

Edit? NO//

CUSTOMIZED RESOLUTION LOGIC (OPTIONAL):

GENERAL RESOLUTION FOUND TEXT:

No existing text

Edit? NO//

GENERAL RESOLUTION NOT FOUND TEXT:

No existing text

Edit? NO//

Reminder Dialog

LINKED REMINDER DIALOG: JG DIABETIC EYE EXAM//

Web Addresses for Reminder Information

Select URL:

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit:

Input your edit comments.

Edit? NO//

**Editing part of the reminder definition**

This is an example of editing Logic.

Select Reminder Definition Management Option: **RE** Add/Edit Reminder Definition
Select Reminder Definition: **JG-DIABETIC EYE EXAM** Select one of the following:
          A         All reminder details
          G         General
          B         Baseline Frequency
          F         Findings
          FF        Function Findings
          L         Logic
          C         Custom date due
          D         Reminder Dialog
          W         Web Addresses
Select section to edit: Logic

Patient Cohort and Resolution Logic
CUSTOMIZED PATIENT COHORT LOGIC (OPTIONAL): (SEX)&amp;(AGE)&amp;FI(SLC DIABETES)
GENERAL PATIENT COHORT FOUND TEXT:
  1&gt; &lt;Enter&gt;
GENERAL PATIENT COHORT NOT FOUND TEXT:
  1&gt; **&lt;Enter&gt;** CUSTOMIZED RESOLUTION LOGIC (OPTIONAL): **FI(DIABETIC EYE EXAM)** GENERAL RESOLUTION FOUND TEXT:
  1&gt;&lt;Enter&gt;
GENERAL RESOLUTION NOT FOUND TEXT:
  1&gt;&lt;Enter&gt;

#### Copy Reminder Definition

This option allows you to copy an existing reminder definition into a new reminder definition.

Select Reminder Definition Management Option: **copy** Reminder Definition

Select the reminder item to copy: **VA-WH PAP SMEAR SCREENING** NATIONAL

PLEASE ENTER A UNIQUE NAME: **JG-WH PAP SMEAR SCREENING**

The original reminder VA-WH PAP SMEAR SCREENING has been copied into JG-WH PAP SMEAR SCREENING.

Do you want to edit it now? **YES**

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit: General

PRINT NAME: VA-PAP Smear Screening  Replace VA With LOCAL

Replace

LOCAL-PAP Smear Screening

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

USAGE: CR//

RELATED REMINDER GUIDELINE:

INACTIVE FLAG:

REMINDER DESCRIPTION:. . .

. . .

* PCE CPT procedure code

* Completed consult order for outside procedure

The following will resolve this reminder for one week:

* PAP smear obtained at this encounter

* Patient declined PAP smear

* PAP smear deferred

* Health Factor documenting an order related to PAP Smear

screening was placed

Edit? NO//

TECHNICAL DESCRIPTION:. . .

. . .

ordering options for the clinicians. Some sites have clinicians order

a consult to a service that provides PAP smears.  If your site does

this, copy the reminder dialog to a local reminder dialog, then

add the local dialog element for the consult order to the reminder

dialog so this practice can continue.

4.  If your site chooses not to send letters via the WH package, copy

the appropriate national dialog components to local components and

remove the findings related to WH notifications.

Edit? NO//

PRIORITY:

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit:

#### Reminder Edit History

You can display a reminder definition's edit history with this option.

Select Reminder Definition Management Option: RH  Reminder Edit History

Maximum number of occurrences to display :  (2-99): 3//

Select Reminder Definition:    TEST     LOCAL

Edit History for reminder AGP TEST:

Edit date: May 12, 2010@08:30:49    Edit by: CRUSER,TWO

Edit Comments: Exchange Install

Select Reminder Definition: VA-TERATOGENIC MEDICATIONS ORDER CHECK       NATIONAL

Edit History for reminder VA-TERATOGENIC MEDICATIONS ORDER CHECK:

Edit date: Oct 27, 2011@22:05:53    Edit by: CRDEVELOPER,TWO

Edit Comments: Exchange Install

Select Reminder Definition:

#### Integrity Check Options

The Integrity Check Selected and Integrity Check All options can check the integrity of selected or all reminder definitions. The system will also perform an ntegrity check automatically whenever a reminder definition has been edited. Fatal errors (F) that will prevent the reminder from working properly and warnings (W) will be given.

The following checks are made:

F – Each finding is checked to make sure it exists

F – If either the Beginning Date/Time or Ending Date/Time contains FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”), the definition is checked to make sure it contains finding M, and if an occurrence is used, the Occurrence Count of finding M is checked to make sure it is greater than or equal to N.

F- Function findings functions of the form FUNCTION(M) and FUNCTION(M,N) are checked to make sure finding M is in the definition and the Occurrence Count of finding M is greater than or equal to N.

F – If a Custom Date Due is defined, it is checked to make sure that the findings used in the Custom Date Due all exist in the definition.

F – Patient Cohort Logic and Resolution Logic are checked to make sure that the findings used in the logic all exist in the definition.

F – Logic strings are checked to make sure their syntax is valid.

F – The definition contains Resolution Logic but does not have a baseline frequency or any findings that will set a frequency.

W – The Usage field contains a “P” and it is not a national reminder

W – The definition contains Resolution Logic but does not have a baseline frequency. It does have findings that will set a frequency. This could be a problem if all findings that set frequency are false.

NOTE: PXRM*2*26 added new checks:

- When the Usage is 'L', any computed findings that are not list-type are flagged as fatal errors.

- Terms that are used as findings in the definition will now be checked to make sure all the mapped findings exist and mapped computed findings are the proper type.

#### Integrity Check Selected

This option lets the user select a reminder definition for  integrity checking.

Select Reminder Definition Management Option: ICS  Integrity Check Selected

Select Reminder Definition:    VA-TERATOGENIC MEDICATIONS ORDER CHECK     NATIONAL

Warning, there is no Resolution logic.

No fatal errors were found.

#### Integrity Check All

This option runs the integrity check for all reminder definitions on the system. It is good practice to run this on a regular basis such as monthly or quarterly.

Select Reminder Definition Management Option: **ica** Integrity Check All

Check the integrity of all reminder definitions.

DEVICE: HOME//   HOME

Checking 01-DIAB PTS (5Y) W/O DIAB EXAM (1Y) (IEN=256)

Warning, there is no Resolution logic.

No fatal errors were found.

Checking 37-PC-PTSD SCREENING (IEN=331)

No fatal errors were found.

Checking 691 PNT EYE CLINIC (IEN=262)

Warning, there is no Resolution logic.

No fatal errors were found.

Checking AAA SCREENING (IEN=360)

No fatal errors were found.

Checking AGETEST (IEN=660004)

No fatal errors were found.

Checking AGP ABNORMAL WH STUFF (IEN=170)

Finding number 10 uses computed finding VA-PROGRESS NOTE. This computed finding

will not work properly unless the Computed Finding Parameter is defined and in this case it is not.

Finding number 13 uses computed finding VA-ACTIVE PATIENT RECORD FLAGS. This

computed finding will not work properly unless the Computed Finding Parameter

is defined and in this case it is not.

Checking AGP APPOINTMENT (IEN=419)

Finding number 1 uses computed finding VA-APPOINTMENTS FOR A PATIENT. This

computed finding will not work properly unless the Computed Finding Parameter

is defined and in this case it is not.

Etc.

#### Reminder Definition Fields

| **Name**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME                                  | This field is the name of a clinical reminder definition. Nationally distributed reminder definition names are prefixed with "VA-". The VA-prefixed reminder definitions cannot be altered by a site, but may be inactivated so they will not be selectable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRINT NAME                            | This is the name that is used when the results of a reminder evaluation are displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CLASS                                 | This is the class of definition. National definitions cannot be edited or created by sites.  N        NATIONAL  V        VISN  L        LOCAL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SPONSOR                               | This is the name of a group or organization that sponsors the reminder  *.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| REVIEW DATE                           | The review date is used to determine when the definition should be reviewed to verify that it is current with the latest standards and guidelines  *.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| USAGE                                 | This field allows the reminder creator to specify how the reminder can be used. This is a free text field that can contain any combination of the following characters:  A - Action  C - CPRS (the reminder can be used in the CPRS GUI)  L – Reminder Patient List  O – Reminder Order Checks  P – Patient; patients can view “My Health” reminders; the wildcard (*) excludes  P  R - Reminder Reports (the reminder can be used in reminder reports)  X - Reminder Extracts (the reminder is used for data extraction)  * - All of the above, except L, O, and P  This field must contain C or * if the reminder is to be selected in CPRS. The L or the O values will override all other values.  The A will not allow a reminder to be used on the CPRS coversheet unless the value of C is set also in the usage field.  NOTE: To enter more than one code, type the codes with no spaces or punctuation between them.                                                                                                                                                                                         |
| INACTIVE FLAG                         | Reminders that are inactive will not be evaluated. The Clinical Maintenance component will return a message stating the reminder is inactive and the date when it was made inactive.  Other applications that use reminders may use this flag to determine if a reminder can be selected for inclusion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| REMINDER DESCRIPTION                  | This is a description of the clinical purpose of the reminder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TECHNICAL DESCRIPTION                 | This is a description of how the reminder works.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRIORITY                              | The reminder priority is used by the CPRS GUI for sorting purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DO IN ADVANCE TIME FRAME              | This field is used to let a reminder become due earlier than the date determined by adding the frequency to the date when the reminder was last resolved. For example, if the frequency is 1Y (one year) and the DO IN ADVANCE TIME FRAME is 1M (one month) the reminder would have a status of "DUE SOON" 11 months after it was last resolved. After one year has passed the STATUS would be "DUE."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SEX SPECIFIC                          | This field is used to make a reminder sex-specific. If an "F" is entered, the reminder applies only to females. If an "M" is entered, the reminder applies only to males. If it is left blank, then the reminder is applicable to either sex.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IGNORE ON N/A                         | This field allows the user to stop reminders from being printed in the  Clinical Maintenance component if the reminder is N/A. This is a free- text field that can contain any combination of the following codes:  Code Description  A    N/A due to not meeting age criteria.  I     N/A due to inactive reminder.  R    N/A due to the wrong race.  S    N/A due to the wrong sex.  *    N/A for any reason.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FREQUENCY AGE RANGE SET               | The Frequency Age Range set is a multiple that allows you to define different frequencies for different non-overlapping age ranges. The fields in this multiple are:  REMINDER FREQUENCY:  This is the frequency to give the reminder. It is input as nD, nM, or nY, where D stands for days, M for months, Y for years, and n is a number. Thus, for a reminder that is to be given once a year, the values 365D, 12M, or 1Y would all work. If a reminder is only to be given once in a lifetime, use a frequency of 99Y.  MINIMUM AGE:  This field specifies the minimum age for defining an age range associated with a frequency. Leave it blank if there is no minimum age.  MAXIMUM AGE:  This field specifies the maximum age for defining an age range associated with a frequency. Leave it blank if there is no maximum age.  AGE MATCH TEXT:  This text will be displayed in the Clinical Maintenance component if the patient’s age falls in the age range.  AGE NO MATCH TEXT:  This text will be displayed in the Clinical Maintenance component if the patient’s age does not fall in the age range. |
| FINDING                               | The Findings multiple is documented later in this chapter, page  73  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| FUNCTION FINDINGS                     | Function Findings are new in version 2.0. They are called Function Findings because they do a computation on the results from regular findings. Function Findings can be used in both patient cohort logic and resolution logic.  The general form of the function string is:  FUNCTION(finding list) operator FUNCTION(finding list)  where FUNCTION is one of the available functions and finding list is a comma-separated list of regular finding numbers. See page  90  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CUSTOMIZED PATIENT COHORT LOGIC       | This field may be used to define a customized Boolean logic string that defines how and what findings in a reminder are used to determine if the reminder applies to the patient. The customized logic is used when the USE IN PATIENT COHORT LOGIC fields associated with each finding do not provide the ability to create the required logic string. (e.g., grouping various findings within parenthesis)  Tip:  Before defining the Boolean string, review the default logic defined in the DEFAULT PATIENT COHORT LOGIC field using the reminder inquiry option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| GENERAL PATIENT COHORT FOUND TEXT     | This optional text is displayed in the Clinical Maintenance component when the patient is in the cohort and the reminder is applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GENERAL PATIENT COHORT NOT FOUND TEXT | This optional text will be displayed in the Clinical Maintenance component when the patient is not in the cohort and the reminder is not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CUSTOMIZED RESOLUTION LOGIC           | This field may be used to define a customized Boolean logic string that         defines how and what reminder findings are used to determine if the reminder has been resolved. The customized logic is used when the USE IN RESOLUTION LOGIC fields associated with each finding do not provide the ability to create the required logic string. (e.g., grouping various findings within parenthesis).  Tip:  Before defining the Boolean string, review the default logic defined in the DEFAULT RESOLUTION LOGIC field using the reminder inquiry option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| GENERAL RESOLUTION FOUND TEXT         | This optional text will be displayed in the Clinical Maintenance component if the reminder has been resolved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| GENERAL RESOLUTION NOT FOUND TEXT     | This optional text will be displayed in the Clinical Maintenance component if the reminder has not been resolved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CUSTOM DATE DUE                       | When a CUSTOM DATE DUE is defined, it takes precedence over the standard date due calculation. This means the normal date due calculation that is based on the dates of the resolution findings and the final frequency is not done. Only the dates of the findings and the frequencies specified in the Custom Date Due string are used. Any finding that is in the reminder definition can be used in the Custom Date Due string; it is not limited to those defined as resolution findings.  The final age range will still be used to determine if the patient is in the cohort; however, the frequency associated with this age range is not used. Only the frequencies specified in the Custom Date Due String are used. They are added to the date of the associated finding to determine the dates used by the MIN\_DATE, MAX\_DATE, or RANK\_DATE functions.                                                                                                                                                                                                                                                |
| CONTRAINDICATED LOGIC                 | This field is used only for immunization reminders. It is a Boolean logic string, when it evaluates to TRUE, the evaluation status of the reminder is CONTRA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CONTRAINDICATED TRUE TEXT             | This optional text will be displayed in the Clinical Maintenance component when the CONTRAINDICATED LOGIC is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CONTRAINDICATED FALSE TEXT            | This optional text will be displayed in the Clinical Maintenance component when the CONTRAINDICATED LOGIC is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| REFUSED LOGIC                         | This field is used only for immunization reminders. It is a Boolean logic string, when it evaluates to TRUE, the evaluation status of the reminder is REFUSED, as long as the CONTRAINDICATED LOGIC is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| REFUSED TRUE TEXT                     | This optional text will be displayed in the Clinical Maintenance component when the REFUSED LOGIC is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| REFUSED FALSE TEXT                    | This optional text will be displayed in the Clinical Maintenance component when the REFUSED LOGIC is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LINKED REMINDER DIALOG                | This is the Reminder Dialog that will be used when the reminder is processed in the CPRS GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| WEB SITES                             | This multiple contains Web site(s) for information related to this reminder. When processing a reminder in the CPRS GUI you will be able to launch a browser and visit the Web site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| URL                                   | This is the URL for the web site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| WEB SITE TITLE                        | This is the web site title that is used by the CPRS GUI. It will appear after a right-click, allowing you to select the web site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| WEB SITE DESCRIPTION                  | This field contains a description of the Web site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |


#### Reminder Findings

Findings are types of patient data elements in VistA that determine a reminder’s status.  They are used in the PATIENT COHORT LOGIC, RESOLUTION LOGIC, and Function Findings. Each finding is evaluated when a reminder is evaluated for a patient. Findings are either True (1) or False (0)

Findings have three functions in reminder definitions:

To select the applicable patient population (Patient Cohort Logic)

To resolve the reminder (Resolution Logic)

To provide information

**Findings Types**

| Finding Type              |   **Source File Number** | **Abbreviation**   |
|---------------------------|--------------------------|--------------------|
| Drug                      |                   50     | DR                 |
| Education Topic           |                    1e+07 | ED                 |
| Exam                      |                    1e+07 | EX                 |
| Health Factor             |                    1e+07 | HF                 |
| Immunization              |                    1e+07 | IM                 |
| Laboratory Test           |                   60     | LT                 |
| MH Tests and Surveys      |                  601.71  | MH                 |
| Orderable Item            |                  101.43  | OI                 |
| Radiology Procedure       |                   71     | RP                 |
| Reminder Computed Finding |                  811.4   | CF                 |
| Reminder Taxonomy         |                  811.2   | TX                 |
| Reminder Term             |                  811.5   | RT                 |
| Skin Test                 |                    1e+07 | ST                 |
| VA Drug Class             |                   50.605 | DC                 |
| VA Generic                |                   50.6   | DG                 |
| Vital Measurement         |                  120.51  | VM                 |
| Reminder Location List    |                  810.9   | RL                 |

**TIP** : When editing findings in a reminder definition or term, you can save time by giving an exact specification of the name of the finding by using the abbreviation. This tells FileMan exactly where to find it and avoids long searches.

Example

For finding:  VA-DIABETES taxonomy

*Enter: TX.VA-DIABETES*

**Hint** : To add a second occurrence of a finding, enclose it in quotes, i.e., “Prefix.Name”

**Drug** – Drugs are found in the DRUG file #50. Results for individual patients can be found in the Pharmacy Patient file #55 (inpatient), the Prescription file #52 (outpatient), or for non-VA Meds which are stored in the Pharmacy Patient file. The parameter RXTYPE can be used to control which files are searched for patient results; see the description of RXTYPE below.

Each type of drug has an associated start date and stop date. For inpatient drugs, these are the START DATE and the STOP DATE. For outpatient drugs, the start date is the RELEASE DATE and the stop date is the RELEASE DATE + DAYS SUPPLY. For non-VA Meds, the start date is the START DATE or, if there is no START DATE, it is the DOCUMENTED DATE and the stop date is the DISCONTINUED DATE if it exists; otherwise it is today’s date.

**Education Topic** – Education topics are found in the EDUCATION TOPICS file #9999999.09. Results for individual patients are found in the V PATIENT ED file #9000010.16. The default value used for the CONDITION is LEVEL OF UNDERSTANDING. Possible values are:

'1' FOR POOR;

'2' FOR FAIR;

'3' FOR GOOD;

'4' FOR GROUP-NO ASSESSMENT;

'5' FOR REFUSED

If you want to allow only those educations where the LEVEL OF UNDERSTANDING is GOOD to be true, the CONDITION field would be I V=3.

Patch PX*1*211 added functionality that allows a measurement to be associated with an Education Topic. Patch PX*1*217 refined this functionality. Appendix C describes how to use this functionality.

**Exam** – Exams are found in the EXAM file #9999999.15. Results for individual patients are found in the V EXAM file #9000010.13. The default value used for the CONDITION is the RESULT. Possible values are:

'A' FOR ABNORMAL

'N' FOR NORMAL

If you want only those exams where the RESULT is NORMAL to be true, the CONDITION field would be I V=“N”.

Patch PX*1*211 added functionality that allows a measurement to be associated with an Exam. Patch PX*1*217 refined functionaly. Appendix C describes how to use this functionality.

**Health Factor** – Health factors are found in the HEALTH FACTOR file #9999999.64. Results for individual patients are found in the V HEALTH FACTOR file #9000010.23. The default value used for the CONDITION is LEVEL/SEVERITY. Possible values are:

'M' FOR MINIMAL

'MO' FOR MODERATE

'H' FOR HEAVY/SEVERE

If you want only those health factors whose LEVEL/SEVERITY is HEAVY/SEVERE to be true, then the CONDITION field would be I V="H”.

Patch PX*1*211 added functionality that allows a measurement to be associated with a Health Factor Topic. Patch PX*1*217 refined this functionality. Appendix C describes how to use this functionality.

Health Factors have a field called ENTRY TYPE. There are two possible values for this field:  category and factor. Each factor health factor must belong to a category. Categories provide a way to group health factors. Typical examples of categories are alcohol use, breast cancer, and tobacco. When reminders are evaluated, if there is more than one health factor from a category in the definition, only the most recent health factor in the category can be true. This feature can be used to make a reminder applicable or not applicable for a patient.

**Example:**

A reminder for smoking cessation education provides a good example. A health factor of current smoker is used in the PATIENT COHORT LOGIC with the AND Boolean operator. A second health factor of non-smoker is included as an information finding. A patient comes in and is a current smoker so they are given the current smoker health factor; this makes the reminder applicable. The patient has the smoking cessation education; six months later he or she has quit, so is given the non-smoker health factor. Since non-smoker is more recent than current smoker, the reminder is not applicable. Another six months passes and the patient is smoking again, so he is given the current smoker health factor, which makes the reminder applicable again. All the health factors are still in the patient’s record, so you can see the progression of their smoker non-smoker status.

When health factors are mapped to a Term, the categorization is done only for the health factors in the Term. The Term factors are not combined with health factors in the definition for the categorization.

The field WITHIN CATEGORY RANK will let you change this categorization behavior. See that section, page 76 , for a description of how to use it.

Only those Health Factors with an ENTRY TYPE of factor can be used in reminder definitions. However, when you create a packed reminder definition using the reminder Exchange Utility, each factor health factor and its category health factor are included. This is done so that a receiving site can install the factor health factors used in the reminder definition. Factor health factors cannot be installed if their category health factor does not already exist. Category health factors should be installed before factor health factors.

Patch PX*1*211 made a change so that the names of category factors have “ [C]” appended to the name. This makes it easier to recognize category factors.

**Immunization** – Immunizations are found in the IMMUNIZATION file #9999999.14. Results for individual patients are found in the V IMMUNIZATION file #9000010.11. The default value used for the CONDITION is the SERIES. Possible values are:

'P' FOR PARTIALLY COMPLETE

'C' FOR COMPLETE

'B' FOR BOOSTER

'1' FOR SERIES 1

'2' FOR SERIES 2

'3' FOR SERIES 3

'4' FOR SERIES 4

'5' FOR SERIES 5

'6' FOR SERIES 6

'7' FOR SERIES 7

'8' FOR SERIES 8

Patch PXRM*2*65 adds new immunization contraindication, precaution, and refusal functionality.

When an immunization is used as a finding in a definition or a term, there is an automatic search of the V IMM CONTRA/REFUSAL EVENTS file for contraindications, precautions, and refusals for that immunization. Any items that are found will be displayed in the Clinical Maintenance output.

PXRM*2*65 added CONTRAINDICATED LOGIC and REFUSED LOGIC fields. Contraindicated findings and refused findings can be used to define these logic fields. When CONTRAINDICATED LOGIC is true, the reminder will have an evaluation status of CONTRA. When REFUSED LOGIC is true and CONTRAINDICATED LOGIC is false, the reminder will have an evaluation status of REFUSED. This functionality is described in detail in Appendix D. Refer to it when you are ready to add CONTRAINDICATED LOGIC and REFUSED LOGIC to a reminder definition.

**Laboratory Test** – Laboratory tests are found in the LABORATORY TEST file #60. Only individual tests may be selected as a reminder finding; lab panels cannot be used. Test results are found in the LAB DATA file #63.  The default value for the CONDITION is the result of  the lab test. The type of result, text or numerical, the normal range of values, and the units will be a function of the particular test, so you should be aware of what they are before you set up a Condition.

**Orderable Item** –Orderable Items are found in the ORDERABLE ITEMS file #101.43. Results for a patient are found in the ORDER file #100. An order has an associated Start Date and in most – but not all – cases, an associated Stop Date. If the Stop Date does not exist, then reminder evaluation date is used as the Stop Date. By default, Start Date is used as the date of an orderable item finding. If you want the date of the finding to be the Stop Date, set the finding modifier to NO. See the description of the USE START DATE finding modifier to understand how date ranges are used in the finding search.

You can use a STATUS LIST for orderable item findings. If no STATUS LIST is defined, then only orders with a status of active or pending can be true. The default value for the CONDITION is the order status.

Possible order statuses are found in the ORDER STATUS file #100.01:

DISCONTINUED	COMPLETE	HOLD

FLAGGED	PENDING	ACTIVE

EXPIRED	SCHEDULED	PARTIAL RESULTS

DELAYED	UNRELEASED	RENEWED

DISCONTINUED/EDIT	CANCELLED	LAPSED

NO STATUS

**MH Tests and Surveys –** This file defines the interviews, surveys and tests available in the Mental Health Assistant. Attributes of the instruments include authoring credits, target populations, normative samples and copyright information. Actions available including privileging, reporting of full item content and transmission to the Mental Health National Database are also specified.

Entries may be made through the provided Mental Health Authoring software.

Direct entry through FileMan or the programmer prompt is prohibited.

Mental Health Instruments are found in the MH INSTRUMENT file #601.  Results for a patient are found in the PSYCH INSTRUMENT PATIENT file #601.2. The default value for the CONDITION is the result returned by the Mental Health test. The normal range of values and the units will be a function of the particular test. When the user enters answers to a mental health test, the answers are automatically passed to the Mental Health package to calculate a result, which may be referenced as SCORE. For example, CAGE test has a SCORE from 1-4 and GAF has a SCORE from 1-99.

For most Mental Health tests, progress note text that summarizes or includes the results (SCORE) can be automatically genderated. Default text is distributed in the REMINDER DIALOG file #801.41 for sites to use for each Mental Health test processed in the reminder resolution process.

For a Mental Health Instrument to create a score, a Result Group would have to be added to the RESULT GROUP/ELEMENT field within the dialog group/element.  This Result Group contains one or more Result Elements which can define ranges of scores using a condition statement.  These Result Elements are added to the Result Group as sequences.  Text that is specific to the score of the instrument can be automatically added to the progress note.

**Reminder Computed Findings** – Reminder Computed Findings are found in the COMPUTED FINDINGS file #811.4. Computed findings provide the ability to create custom findings for situations when none of the standard findings will work.

See the chapter on Computed Findings  for more details.

**Reminder Taxonomy** – Reminder taxonomies are found in the REMINDER TAXONOMY file #811.2. Reminder taxonomies provide a convenient way to group coded values and give them a name. For example, the VA-DIABETES taxonomy contains a list of diabetes diagnoses.

A taxonomy can contain CPT, HCPCS, ICD0, ICD9, ICD10 and SNOMED CT codes. Clinical Reminders searches in a number of patient data files for code matches.

- For ICD diagnosis codes, it looks in V POV, Problem List, and PTF.
- For CPT codes, it looks in V CPT and Radiology.
- For ICD procedure codes, it looks in PTF.
- For SNOMED CT codes it looks in V Standard Code and Problem List. The PATIENT DATA SOURCE field is used to control where codes are searched for, see below.

There are two dates associated with ICD diagnoses found in Problem List,  the date entered and the date last modified. The PRIORITY field is used to determine if a problem is chronic or acute. If the problem is chronic, Clinical Reminders will use today’s date in its date calculations; otherwise it will use the date last modified.  The default is to only use active problems unless the field USE INACTIVE PROBLEMS is yes or the STATUS LIST contains the status of inactive.

The following are fields that can be specified for each taxonomy finding:

USE INACTIVE PROBLEMS – Normally, Problem List problems that are marked as inactive are ignored during the reminder evaluation. If you want them to be used, give this field a value of “YES.”

PATIENT DATA SOURCE specifies where to search for patient data. It is a string of comma-separated key words. The keywords and their meanings are:

| **KEYWORD**   | **MEANING**                                  |
|---------------|----------------------------------------------|
| IN            | Search in the inpatient data file PTF        |
| INDXLS        | Search in PTF for DXLS only                  |
| INPR          | Search in PTF for principal diagnosis only   |
| EN            | Search encounter (PCE) data                  |
| ENPR          | Search PCE data for primary diagnosis only   |
| PL            | Search for Problem List diagnosis only       |
| RA            | Search in Radiology for radiology CPT codes. |

You may use any combination of these keywords. An example is EN,RA. This would cause the search to be made in V CPT and Radiology for CPT codes. If PATIENT DATA SOURCE is left blank, the search is made in all the possible sources.

See the Reminder Taxonomy Management chapter for more details.

**Reminder Term** – Reminder Terms are found in file #811.5. Reminder Terms provide a way to define a general concept.  For example, a laboratory test, which can be mapped to specific findings. For a laboratory test, the term could be mapped to one or more entries from the Laboratory Test file, and possibly to a health factor used to record an outside result. A Reminder Term must be mapped to at least one finding before it can be used for reminder evaluation. A Reminder Term can be mapped to more than one finding. Reminder Terms can be mapped to any of the findings, except Reminder Terms, that can be used in a Reminder Definition.

Each node of the findings multiple in a term has the following fields:

- BEGINNING DATE/TIME,
- ENDING DATE/TIME,
- USE INACTIVE PROBLEMS,
- WITHIN CATEGORY RANK,
- CONDITION,
- MH SCALE,
- RXTYPE,
- OCCURRENCE COUNT,
- USE START DATE,
- INCLUDE VISIT DATA and
- IMMUNIZATION CRITERIA.

These fields work exactly the same as the fields with the same names in the findings multiple of the reminder definition. If one of these fields is specified at the definition findings level, where the term is the finding, then each finding in the term will inherit the value. If the field is specified at the finding level of the term, then it will take precedence and replace what has been specified at the definition level.

See the Reminder Term Options chapter for more details.

**Skin Test** – Skin Tests are found in the SKIN TEST file #9999999.28. Results for individual patients are found in the V SKIN TEST file #9000010.12. The default value used for CONDITION is RESULTS. Possible values are:

'P' FOR POSITIVE

'N' FOR NEGATIVE

'D' FOR DOUBTFUL

'O' FOR NO TAKE

If you want only those findings to be true for skin tests whose results are positive, the CONDITION would be I V="P".

**VA Drug Class** – VA Drug Class entries are found in the VA DRUG CLASS file #50.605. An entry from the VA Drug Class file points to one or more entries in the Drug file. Each of the corresponding entries in the Drug file is processed as described in the Drug section. The information displayed in the Clinical Maintenance component includes the VA Drug Class and the particular drug that was found.

**VA Generic** – VA Generic entries are found in the VA GENERIC file #50.6. (This was formerly called the National Drug file.) An entry from the VA Generic file points to one or more entries in the Drug file.

Each of the corresponding entries in the Drug file is processed as described in the Drug section. The information displayed in the Clinical Maintenance component includes the VA Generic name and the particular drug that was found.

**Vital Measurement** – Vital Measurement types are found in the GMRV VITAL TYPE file #120.51. Results for individual patients are found in the GMRV VITAL MEASUREMENT file #120.5. The default value used for the CONDITION is RATE, which is the value of the measurement. If you are going to use a CONDITION with this finding, you need to be familiar with how the Vitals package returns the Rate data. For example, if the vital sign is weight, Rate will be a number that is the weight in pounds. If the vital sign is blood pressure, then Rate can have two possible forms: systolic/diastolic or systolic/intermediate/diastolic. If your Condition is to be based only on systolic pressure, then it is straightforward; you always check the first piece. For example, if you want the finding to be true only for systolic pressures greater than 140, then the Condition would be I $P(V,"/",1)&gt;140. Checking the diastolic pressure is not so straightforward because there is no way to know in advance whether the Rate will be returned as systolic/diastolic or systolic/intermediate/diastolic.  Insuring that you are always checking the diastolic requires the complex Condition statement I $S($L(V,”/”)=3:$P(V,”/”,3),1:$P(V,”/”,2)).

NOTE:  Blood pressure is the only Vital measurement for which the Rate can have two possible forms.

**PXRM*2*18 Update:**

If you are using $P in a Condition, we recommend that you replace it with the appropriate CSUBs. Several national definitions and terms were originally distributed with Conditions using $P; as part of this patch, they will be updated to use the SYSTOLIC and DIASTOLIC CSUBs.

SYSTOLIC/MEAN/DIASTOLIC and use of CSUB instead of $P: The Clin2 support team pointed out that the value for blood pressure can come back in either of the following forms: SYSTOLIC/DIASTOLIC or SYSTOLIC/MEAN/DIASTOLIC ( the second form is not very common). If the second form comes back, then the DIASTOLIC CSUB would have the value for mean, and if $P was used in a Condition, it would also be the mean. The code was changed so that the DIASTOLIC CSUB will always have the correct value.

**Reminder Location List** – Reminder Location List entries are found in the REMINDER LOCATION LIST file #810.9. This file contains lists of stop codes and/or hospital locations for use as a reminder finding.  Results for individual patients are found by looking at the patient’s Visit file entries and matching the location associated with a Visit with a location in the location list.

See the chapter in this manual, page 159 , that describes Reminder Location List options.

###### Finding Modifier Fields

There are a number of fields in the Findings multiple that modify how each Finding is used in the reminder evaluation process. Each of these fields is described in detail below. Some fields apply only to specific finding types and you will only be prompted for them if they apply to the selected finding item.

FINDING ITEM

REMINDER FREQUENCY

MINIMUM AGE

MAXIMUM AGE

RANK FREQUENCY

USE IN RESOLUTION LOGIC

USE IN PATIENT COHORT LOGIC

BEGINNING DATE/TIME

ENDING DATE/TIME

OCCURRENCE COUNT

INCLUDE VISIT DATA (applies only to PCE data)

IMMUNIZATION SEARCH CRITERIA (applies only to immunization findings)

USE INACTIVE PROBLEMS (applies only to taxonomies that search Problem List)

WITHIN CATEGORY RANK (applies only to health factors)

MH SCALE (applies only to mental health instruments)

RXTYPE (applies only to drug findings)

CONDITION

CONDITION CASE SENSITIVE

USE STATUS/COND IN SEARCH

FOUND TEXT

NOT FOUND TEXT

STATUS LIST (applies only to findings that have a status)

COMPUTED FINDING PARAMETER (applies only to computed findings)

**Finding Modifiers Description**

REMINDER FREQUENCY, MINIMUM AGE, and MAXIMUM AGE – These are treated as a set that we call a frequency age range set. If a finding is true, then the frequency age range set will override the baseline frequency age range set. This is used when a finding should override the baseline. For example, a patient with a particular health factor needs to get the reminder at an earlier age than normal and it should be done more frequently. The values these fields can take are exactly the same as those that set the baseline frequency and age range.

RANK FREQUENCY – If more than one finding that has a frequency age range set is true, then how do we decide which frequency age range set to use? That is the purpose of the RANK FREQUENCY. The frequency age range set from the finding with the highest RANK FREQUENCY will be used. In the absence of RANK FREQUENCY, the frequency age range set that will cause the reminder to be given the most often will be used. RANK FREQUENCY is a numerical value with 1 being the highest.

USE IN RESOLUTION LOGIC – This field specifies how a finding is used in resolving a reminder. It is a set of codes that can contain the Mumps Boolean operators and their negations. The operators are ! (OR), &amp; (AND), !’ (OR NOT), and  &amp;’ (AND NOT). If a particular finding must be true in order for the reminder to be resolved, then you would use an AND in this field. If the finding is one of a number of findings that will resolve a reminder, then you would use an OR. For those cases where this mechanism does not allow you to describe the exact logical combination of findings you require, you can input the logic directly in the CUSTOM RESOLUTION LOGIC field.

USE IN PATIENT COHORT LOGIC – This field specifies how a finding is used in selecting the applicable patient population; i.e., the patient cohort. It is a set of codes that works exactly like the USE

IN RESOLUTION LOGIC. For those cases where this mechanism does not allow you to describe the exact logical combination of findings you require, you can input the logic directly in the CUSTOM PATIENT COHORT LOGIC field.

BEGINNING DATE/TIME – This is the beginning date/time to search for findings.

1. The date/time cannot be in the future.
2. The date/time can be any of the acceptable FileMan date/time formats or abbreviations.
3. In addition, you may use the abbreviations T-NY or NOW-NY, where N is an integer and Y stands for years.
4. If this is null, then the beginning date/time will correspond with the date/time of the oldest entry.

See the FileMan Getting Started Manual to learn about acceptable FileMan date/time formats and abbreviations.

ENDING DATE/TIME – This is the ending date/time to search for findings.

1. The date/time cannot be before the beginning date/time.
    1. The date/time can be any of the acceptable FileMan date/time formats or abbreviations.
    2. In addition you may use the abbreviations T-NY or NOW-NY, where N is an integer and Y stands for years.
    3. If this is null, then the ending date/time will be the end of today, where today is the reminder evaluation date.
When date range searching is done, a finding with a single date is considered to be in the date range if the date of the finding falls anywhere in the date range defined by the BEGINNING DATE/TIME and ENDING DATE/TIME. The criteria for findings with a start date and a stop date are different. In this case, if there is any overlap between the date range defined by the start date and stop date and the date range defined by the BEGINNING DATE/TIME and the ENDING DATE/TIME, the finding is considered to be in the date range.

#### * Changes to Beginning and Ending Date/Time made in Patch 18

New functionality was added to allow using the date of one finding to set the date range of another finding. The syntax for the date of a finding is FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”), where M is the finding number and N is the occurrence. This means you can now use dates like FIEVAL(3,”DATE”)-3W as the Beginning or Ending Date/Time of another finding. The global reminder dates PXRMDOB and PXRMLAD can also be used. Note that if FIEVAL(M) is false or PXRMLAD does not exist, then the finding whose date range depends on the date of finding M will be set to false.

In conjunction with allowing FIEVAL(M,N,”DATE”) to be used in Beginning Date/Time or Ending Date/Time, additional frequency units were added. The allowed values are now: H (hours), D (days), W (weeks), M (months), and Y (years). This change applies everywhere that a frequency can be used, including Beginning Date/Time, Ending Date/Time, Reminder Frequency in the Baseline Age Findings multiple, Findings multiple, Function Findings multiple, and Custom Date Due. Custom Date Due will now allow both “+” and “-“; in the past it only allowed “+”.

OCCURRENCE COUNT - This is the maximum number of occurrences of the finding in the date range to return. If the OCCURRENCE COUNT is input as a positive number, N, up to N of the most recent occurrences will be returned and the finding will take the value of the most recent occurrence. If the OCCURRENCE COUNT is input as a negative number then this behavior is reversed. Up to N of the oldest occurrences will be returned and the finding will take the value of the oldest occurrence in the list.

USE INACTIVE PROBLEMS – This field applies only to taxonomies containing ICD diagnoses. If the diagnosis is found in the PROBLEM LIST and it is inactive, then the finding cannot be true unless this field is set to YES.

WITHIN CATEGORY RANK – This field applies only to health factors. In order to understand how it works, you need to understand how health factors work in the reminder evaluation process. The default behavior is that all the health factor findings in the definition are grouped by category and only the most recent health factor in a category can be true. A problem can arise if there are two or more health factors in the same category and they have exactly the same date and time. (This can happen if multiple health factors are given during the same encounter.) If the date/times are the same, the health factor with the highest WITHIN CATEGORY RANK will be the true one. This is a numerical value like RANK FREQUENCY with 1 being the highest rank.

In some cases, you may want to have a health factor treated as an individual finding, suppressing the category behavior. To do this, use the special value of 0 for the WITHIN CATEGORY RANK.

MH SCALE – This is applicable only to Mental Health Instrument findings. The scale is used to score the results. Typing a “?” at the MH SCALE prompt will list all the scales that are applicable for the selected mental health test. Select the scale to use by typing its number. If no scale is selected then the first scale for the test will be used.

**Patch 6 Changes:**

To aid sites in making the conversion of Clinical Reminders to use MHA3, the post-init will convert all existing mental health findings to their MHA3 equivalent and MH SCALE values to the appropriate MHA3 scale. If the field MH SCALE is null, then the score for the first scale returned by MHA3 will be displayed in the Clinical Maintenance output.

When MH SCALE has a value, it will set the value of V for use in a Condition. In other words, V will be the score according to the scale stored in MH SCALE. Another change is that score is now returned as raw score^transformed score. Thus, if your Condition uses the raw score, you will use +V or $P(V,U,1) and if it uses the transformed score, use $P(V,U,2). The post-init will convert V to +V in all existing national Conditions for MH findings.

The entire set of scores has been made into a CSUB item in patch PXRM*2*6, so that any score or combination of scores can be used in a Condition. For example, the MH Test AUIR has scales 279 through 329; if you want to use the raw score for scale 300, then you can use +V(“S”,300).

USE START DATE – Some findings such as drugs and orderable items have a Start Date and a Stop Date. When these findings are used in the Resolution Logic, determination of a resolution date requires assigning a single date to these types of findings. For drug findings this defaults to the Stop Date while for orderable items it defaults to the Start Date. For findings that have a date range, the finding will be true if the date range defined by the Start Date to the date of the finding overlaps with the date range defined by the Beginning Date/Time to Ending Date/Time. If USE START DATE is not defined, the date of the finding can be either the Start Date or the Stop Date, as described above. If the date of the finding is set to be the Start Date then the date range for the finding is just Start Date to Start Date.

INCLUDE VISIT DATA – This applies only to the data in the PCE V-files. It includes:

- V CPT,
- V EXAM,
- V HEALTH FACTORS,
- V IMMUNIZATION,
- V PATIENT ED,
- V POV,V SKIN TEST, and
- V STANDARD CODES.

When this is set to YES, additional data from the corresponding Visit File entry is included in the list of CSUB data. The best way to determine what additional data is included is by examining the CSUB list shown in reminder test. Adding this data to the CSUB list requires additional computing overhead, so set this value to YES only when the additional data is needed; accordingly, the default is NO.

IMMUNIZATION SEARCH CRITERIA –    This finding modifier applies only to immunization findings. It is a set of codes that controls how an immunization is searched for in the patient's

record. The codes are:

- CVX - Search for all immunizations that have the same CVX code as the immunization finding;
- IMM – Search only for the immunization finding.  This is the default.
- VGN – Search for all immunizations that are in the same vaccing group as the immunization finding.

RXTYPE - RXTYPE is applicable only to drug findings and controls the search for medications. The possible RXTYPEs are:

A - all

I - inpatient

N - non-VA meds

O - outpatient

You may use any combination of the above in a comma-separated list. For example, I,N would search for inpatient medications and non-VA meds.

The default is to search for all possible types of medications. So a blank RXTYPE is equivalent to A.

CONDITION – Many types of findings have associated values. For example, for Education Topics, the value is Level of Understanding; for Vital Measurement, it is the value of the measurement. More specific information can be found in the detailed section for each finding type. The CONDITION field can be used to make the finding true or false depending on the value of the finding. The contents of this field are a single line of Mumps code that should evaluate to true or false. If the code evaluates to true, then the finding is true; if it evaluates to false, then the finding is false.

The default value for each finding type is given in the following table.

| **Finding Type**          | **Value**                    |
|---------------------------|------------------------------|
| Drug                      | None                         |
| Education Topic           | Level of Understanding       |
| Exam                      | Result                       |
| Health Factor             | Level/severity               |
| Immunization              | Series                       |
| Laboratory Test           | Value                        |
| Mental Health Instrument  | Raw score                    |
| Orderable Item            | Status                       |
| Radiology Procedure       | Exam Status                  |
| Reminder Computed Finding | Determined by the programmer |
| Reminder Taxonomy         | None                         |
| Skin Test                 | Results                      |
| VA Drug Class             | None                         |
| VA Generic                | None                         |
| Vital Measurement         | Rate                         |
| Reminder Location List    | Service Category             |

Some examples of simple CONDITIONS are shown in the following table:

| **Finding Type**               | **Results File**             | **Result Fields that can be used in CONDITION**                                                                                  | **Data example**                                                                                                                                                                                                                                                                                                 | **CONDITION field example**                                                                                |
|--------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Drug (50)                      |                              | NONE – but you can use EFFECTIVE PERIOD of 0D, 0M, OR 0Y in the reminder definition to restrict view to current medications only |                                                                                                                                                                                                                                                                                                                  |                                                                                                            |
| Education Topic (9999999.09)   | V PATIENT ED (9000010.06)    | LEVEL OF UNDER-STANDING                                                                                                          | 1 for Poor  2 for Fair  3 for Good  4 for Group-no Assessment  5 for Refused                                                                                                                                                                                                                                     | I V=1  I V=2  I V=3  I V=4  I V=5                                                                          |
| Exam (9999999.15)              | V EXAM (9000010.13)          | RESULT                                                                                                                           | A for Abnormal  N for Normal                                                                                                                                                                                                                                                                                     | I V="A"  I V="N"                                                                                           |
| Health Factor (9999999.64)     | V HEALTH FACTOR (9000010.23) | LEVEL/SEVERITY                                                                                                                   | M for Minimal  MO for Moderate  H for Heavy/Severe                                                                                                                                                                                                                                                               | I V="M"  I V="MO"  I V="H"                                                                                 |
| Immunization (9999999.14)      | V IMMUNIZATION (9000010.11)  | SERIES                                                                                                                           | P for Partially Complete  C for Complete  B for Booster  1 for Series 1  2 for Series 2  3 for Series 3  4 for Series 4  5 for Series 5  6 for Series 6  7 for Series 7  8 for Series 8                                                                                                                          | I V="P"  I V="C"  I V="B"  I V=1  I V=2  I V=3  I V=4  I V=5  I V=6  I V=7  I V=8                          |
| Laboratory Test (60)           | LAB RESULTS in “CH” node     | Number returned from the Lab API as the lab result                                                                               | 180                                                                                                                                                                                                                                                                                                              | I V>130                                                                                                    |
| Location List                  | VISIT (9000010)              | SERVICE CATEGORY                                                                                                                 | ‘A' for AMBULATORY  'H' for HOSPITALIZATION  ‘I' for IN HOSPITAL  'C' for CHART REVIEW  'T' for TELECOMMUNICATIONS  'N' for NOT FOUND       'S' for DAY SURGERY  'O' for OBSERVATION  'E' for EVENT (HISTORICAL)  'R' for NURSING HOME  'D' for DAILY HOSPITALIZATION DATA  'X' for ANCILLARY PACKAGE DAILY DATA | I V="A"  I V="H"  I V="I"  I V="C"  I V="T"  I V="N"  I V="S"  I V="O"  I V="E"  I V="R"  I V="D"  I V="X" |
| Mental health Instrument (601) |                              | RAW SCORE from API based on a scale                                                                                              | 3 (CAGE)                                                                                                                                                                                                                                                                                                         | I V&gt;2                                                                                                   |
| Orderable Item (101.43)        |                              |                                                                                                                                  |                                                                                                                                                                                                                                                                                                                  |                                                                                                            |

In addition to the values for type of finding shown in the above table, the following global reminder variables can be used in a CONDITION:

PXRMAGE  - patient's age

PXRMDATE – the reminder evaluation date and time, usually the current date and time

PXRMDOB  - patient's date of birth in FileMan format

PXRMLAD – the last admission date in FileMan format, if there is no admission this will be null

PXRMSEX  - patient's sex, in the format M for male or F for female

The use of these variables is very similar to how you use the V variable. For example, if you want the finding to apply only to patients who are 65 and younger, the CONDITION is I PXRMAGE'&gt;65 (in English if AGE is not greater than 65). You can combine these variables and the V in a CONDITION. Let's say we want a finding that is true for all patients whose BMI&gt;25 and were born before 1955. Our finding is the VA-BMI finding, so the CONDITION is (I V&gt;25)&amp;(PXRMDOB&lt;2550101).

When using PXRMSEX in a CONDITION, you can test for male patients with PXRMSEX=”M” and for female patients with PXRMSEX=”F”. If we wanted to make the above example true only for female patients the CONDITION would be (I V&gt;25)&amp;(PXRMDOB&lt;2550101)&amp;(PXRMSEX=”F”).

In addition to the default values for finding type, which are referred to as V in the Condition statement, you can now use subscripted V values.

Examples:

I V("PDX")=["ABNORMALITY"

I (V="COMPLETE")&amp;(V("PDX")["ABNORMALITY")

I V("DATE READ")&lt;V("DATE")

The subscripts that can be used depend on the type of finding; the easiest way to determine what is available is to use the Reminder Test option and examine the FIEVAL array for the finding of interest.

Here is an example where the finding is an Education Topic.

FIEVAL(2)=1

FIEVAL(2,1)=1

FIEVAL(2,1,"COMMENTS")=

FIEVAL(2,1,"CSUB","COMMENTS")=

FIEVAL(2,1,"CSUB","LEVEL OF UNDERSTANDING")=1

FIEVAL(2,1,"CSUB","VALUE")=1

FIEVAL(2,1,"CSUB","VISIT")=3102

FIEVAL(2,1,"DAS")=83

FIEVAL(2,1,"DATE")=2990520.07292

FIEVAL(2,1,"LEVEL OF UNDERSTANDING")=1

FIEVAL(2,1,"VALUE")=1

FIEVAL(2,1,"VISIT")=3102

FIEVAL(2,"COMMENTS")=

FIEVAL(2,"CSUB","COMMENTS")=

FIEVAL(2,"CSUB","LEVEL OF UNDERSTANDING")=1

FIEVAL(2,"CSUB","VALUE")=1

FIEVAL(2,"CSUB","VISIT")=3102

FIEVAL(2,"DAS")=83

FIEVAL(2,"DATE")=2990520.07292

FIEVAL(2,"FILE NUMBER")=9000010.16

FIEVAL(2,"FINDING")=369;AUTTEDT(

FIEVAL(2,"LEVEL OF UNDERSTANDING")=1

FIEVAL(2,"VALUE")=1

FIEVAL(2,"VISIT")=3102

Each array element that contains a “CSUB” (Condition Subscript) element can be used in a Condition statement, so for this finding, we could use V("COMMENTS"), V("LEVEL OF UNDERSTANDING"), V(“VALUE”), or V(“VISIT”) in the Condition.

Some finding types may return multiple values for certain types of data; an example is qualifiers for vitals. In the Reminder Test Option output for a weight finding you might see qualifiers such as:

FIEVAL(1,"QUALIFIER",1)=ACTUAL

FIEVAL(1,"QUALIFIER",2)=STANDING

You could use these in a Condition as follows:

I (V(“QUALIFIER”,1)=”ACTUAL”)&amp;(V(“QUALIFIER”,2)=”STANDING”)&amp;(V&gt;165)

Since you don’t always know what subscript the various qualifiers will be associated with, you can use the wildcard in the Condition as follows:

I (V(“QUALIFIER”,“*”)=”ACTUAL”)&amp;(V(“QUALIFIER”,”**”)=”STANDING”)&amp;(V&gt;165)

Lab results now include specimen, so that specimen can be used in the Condition statement. For example, I V("SPECIMEN")="SERUM. " Again, the best way to find out what is available for a particular finding is to using the Reminder Test option and see what comes back with a "CSUB" subscript.

CONDITION CASE SENSITIVE. When this field is set to "NO" then the CONDITION will not be case-sensitive. The default is "NO".

USE STATUS/COND IN SEARCH - Give this field a value of "YES", the default is “NO”,  if you want the STATUS LIST and/or CONDITION applied to each result found in the date range for this finding. Only results that have a status on the list or for which the CONDITION is true will be retained. The maximum number to retain is specified by the OCCURRENCE COUNT.  For example, if there are 7 occurrences of the finding in the date range, occurrences 1, 3, 6, and 7 have a status on the list, and the OCCURRENCE COUNT is 3 then occurrences 1, 3, and 6 will be returned. If USE STATUS/COND IN SEARCH is NO and the OCCURRENCE COUNT is 3 then findings 1, 2, and 3 will be returned but only finding 1 and 3 will be true.

Note - if the finding has both a STATUS LIST and a CONDITION the status check will be made first; the CONDITION will be applied only if the finding passes the status check.

FOUND TEXT – This is a word-processing field. The contents of this field will be displayed in the Clinical Maintenance component whenever the finding is found (true).

NOT FOUND TEXT – This is a word-processing field. The contents of this field will be displayed in the Clinical Maintenance component whenever the finding is not found (false).

Both FOUND TEXT and NOT FOUND TEXT can contain TIU objects. In both, you can control the output format by using \\ to force a line break.

Both FOUND TEXT and NOT FOUND TEXT can contain TIU objects and CSUB objects. See the **Found Text/Not Found Text Details** section for more information.

STATUS LIST - This field applies to finding types that have an associated status. When the search for patient findings is done, only those findings that have a status on the list can be true. The allowable values depend on the finding type. If no statuses are specified then the default list for each finding type will be used.

COMPUTED FINDING PARAMETER - This field applies only to computed findings and is used to pass a parameter into the computed finding. Acceptable values for this field depend on the computed finding and are documented in the computed finding description.

**Found Text/Not Found Text Details**

Normally, all Found/Not Found Text is formatted before it is output. The formatting includes combining short lines to create output that uses the full available width and the use of  the double backslash (\\) to force a line break. For example, if the Found Text contained this text:

This

shows

how the\\

formatter

combines

lines.\\

When it is formatted for the Clinical Maintenance Output, it becomes:

This shows how the

formatter combines lines.

In some cases, this may not be desirable. (For example, when a TIU Health Summary Object is included in the Found/Not Found Text and you want it displayed exactly like it is in a health summary.) When this is the case, enclose the text that you do not want formatted in a not-format block. The not-format block starts with 'FMT{ and ends with }FMT. You can think of it mnemonically as, “do not format the text that is in the block”.

Here are some examples of how to use the not-format block:

- 'FMT{|TIU Health Summary Object|}FMT
    - ' FMT{Example of non-formatted found text.}FMT
If the text in a not-format block spans multiple lines in the Found/Not Found Text, then it will have the same number of lines in the Clinical Maintenance Output since it is not formatted. An example of where this could happen is if you are using CSUB Objects and each of them has to be on its own line. If you do not want to output text to be on multiple lines, you can force lines to be joined by starting the line you want appended to the previous line with the underscore character.
In the example below:
‘FMT{The lab test $$CSUBTEXT(TEST NAME,6) was last done for the patient on:
\_$$CSUBNUM(DATE,D:5Z,6,)}FMT
After $$CSUBTEXT(TEST NAME,6) and $$CSUBNUM(DATE,D:5Z,6,) are replaced with the test name and date for finding 6, the text will be combined into a single line.
When using TIU and CSUB objects, keep in mind that they cannot be broken across two lines.  If they are broken across two lines, they will not be recognized as objects.
**CSUB Objects**
CSUB Objects have a function similar to TIU Objects.  Like TIU Objects,  they can be used in reminder definitions in the following areas:
    - Age Match Text/Age No Match Text
    - Findings Found Text/Not Found Text
    - Function Findings Found Text/Not Found Text
    - Patient Cohort Logic:
        - General Cohort Found Text/Not Found Text
        - Summary Cohort Found Text/Not Found Text
    - Resolution Logic:
        - General Resolution Found Text/Not Found Text
        - Summary Resolution Found Text/Not Found Text
    - Contraindicated Logic:
        - Contraindicated True Text
        - Contraindicated False Text
    - Refused Logic:
        - Refused True Text
        - Refused False Text
In the Clinical Maintenance Output, the CSUB Object will be replaced by the text created when the CSUB Object is evaluated.
CSUB Objects and TIU Objects can be used together, but you should always test the output to make sure there are no anomalies. For both CSUB Objects and TIU Objects, the entire object must be on one line. If there is text to be followed by an object and there is not enough room for the entire object on the line, place the object on the next line.  When the output text is formatted, the object text will be in the right place.
Originally, CSUB Objects were only going to work for the data elements with the CSUB label you see in the FIEVAL array when doing a reminder test (hence the name), but it was found that they could work for any data in the FIEVAL array.  If you want to know what data is available to use with CSUB Objects, run the reminder test for the definition you are working on and examine what is in the FIEVAL array.
There are four types of CSUB data:
    - Finding dates
    - Internal values
    - Numbers
    - Text
Accordingly, there are four CSUB Object functions:
    - $$CSUBDATE
    - $$CSUBINTE
    - $$CSUBNUM
    - $$CSUBTEXT
The optional CELLFORMAT argument can be used with all the CSUB Object functions. This argument gives these objects a behavior similar to a cell in a spreadsheet.
CELLFORMAT is a letter followed by a number, followed by a colon, followed by a pad character, which is a character used to fill empty space. The letter can be:
    - L-left justify
    - R-right justify
    - C-Center justify
The number is the number of characters in the cell. If the object text has fewer characters than the number, it is filled with the pad character.  If the object text has more characters than the number, it is truncated. In most cases, the pad character will be a space.  If it is not defined, it defaults to space.
Examples of CELLFORMAT are listed below:
    - ‘ **L15:** ’ – A left justified cell, 15 characters wide, the pad character is space
    - ‘ **R22:+** ’ – A right justified cell, 22 characters wide, the pad character is plus
    - ‘ **C7:** ’ – A center justified cell, 7 characters wide, the pad character is space
If the letter is not L, R, or C, cell formatting is not done.See Example 1 at the end of the **Building Tables** section for how the choice of the pad character affects the output.This cell formatting capability provides the ability to create data tables using CSUB Objects.  See Example 1 and Example 2 at the end of the **Building Tables** section.
A detailed description of each of the CSUB Object functions is listed below. In the descriptions, optional arguments are enclosed in square brackets, i.e., [optional argument].**$$CSUBDATE** is used for lists of finding dates.  The arguments are:
    - $$CSUBDATE(Function(Finding List),Format,[Text]) 
where Function can be MRD (most recent date) or MIN\_DATE (oldest date).
Finding List is a list of finding numbers.  There must be at least one finding number in the list.
Format is Date Format[:Cell Format].
Date Format controls how the date is written. The Kernel API: FMTE^XLFDT, which is documented in the Kernel Developer’s Guide, is used to format the date. The allowed values are:
    - If null, return the written-out format
    - If +Format = 1, then return standard VA FileMan format
    - If +Format = 2, then return MM/DD/YY@HH:MM:SS format
    - If +Format = 3, then return DD/MM/YY@HH:MM:SS format
    - If +Format = 4, then return YY/MM/DD@HH:MM:SS format
    - If +Format = 5, then return MM/DD/YYYY@HH:MM:SS format
    - If +Format = 6, then return DD/MM/YYYY@HH:MM:SS format
    - If +Format = 7, then return YYYY/MM/DD@HH:MM:SS format
    - If Format contains a “D”, then date only
    - If Format contains an “F”, then output date with leading spaces
    - If Format contains an “M”, then only output “HH:MM”
    - If Format contains a “P”, then output “HH:MM:SS am/pm”
    - If Format contains an “S”, then force seconds in the output
    - If Format contains a “Z”,  then output date with leading zeroes
Text is optional. It will be returned if none of the findings in the finding list is true.
Examples are shown below:
$$CSUBDATE(MRD(1,3,5),1D) - The most recent date from findings 1, 3, and 5 in standard VA FileMan format with the date only, no time, and no cell formatting.
$$CSUBDATE(MRD(1,3,5),1D,No dates were found) - The most recent date from findings 1, 3, and 5 in standard VA FileMan format with the date only, no time. If findings 1, 3, and 5 are all false, then the text “No dates were found” is returned.
$$CSUBDATE(MIN\_DATE(4),2Z:L20: ) - The date of finding 4 in the format MM/DD/YY@HH:MM:SS with leading zeroes, in a left justified cell 20 characters wide, the Pad Character is space.**$$CSUBINTE** is used to convert data from internal format to external format. This includes sets of codes and pointers. The arguments are:
$$CSUBINTE(Subscript,[Cell Format],File Number,Field Number,Finding Number,[Occurrence],
[Separator],[Piece],[Text]) where
    - Subscript is the data element subscript.
    - [Cell Format] is described in the middle of the CSUB Objects section.
    - File Number is the file number where the data element is stored.
    - Field Number is the field in the file where the data element is stored.
    - Finding Number is the finding number.
    - [Occurrence] is the occurrence, used only if the value for an occurrence is desired. The Occurrence Count in the reminder definition should be set equal to or greater than the number of occurrences you are planning to display.
    - [Separator] Some data elements have multiple pieces of data and this is the character that separates them.
    - [Piece] works in conjunction with Separator.  If there are multiple pieces of data, this specifies which one you want. If Piece is not specified, it defaults to 1. If Separator is not passed, Piece is ignored.
    - [Text]  If the data element does not exist, then Text will be returned.
Examples are listed below:
For a health factor finding, where: FIEVAL(3,"CSUB","LEVEL/SEVERITY")="H"
The corresponding CSUB Object is: $$CSUBINTE(LEVEL/SEVERITY,,9000010.23,.04,3)
9000010.23 is the file number for V Health Factors, .04 is the field number for Level/Severity and the finding number is 3.
The same as above, only now we want the second occurrence of finding number 3.
FIEVAL(3,2,"CSUB","LEVEL/SEVERITY")="MO"
The corresponding CSUB Object is: $$CSUBINTE(LEVEL/SEVERITY,,9000010.23,.04,3,2)
For PCE findings, if INCLUDE VISIT DATA is YES, then data from the Visit file entry will be included.  One of them is SERVICE CATEGORY. which is a set of codes.  An example is:
FIEVAL(4,1,"CSUB","SERVICE CATEGORY")=”X”
The corresponding CSUB Object is: $$CSUBINTE(SERVICE CATEGORY,,9000010,.07,4,1)
Where 9000010 is the file number for the Visit file and .07 is the field number for Service Category.
The example below shows how to convert a pointer to its external value.  A taxonomy finding can find results in V CPT, V POV, V STANDARD CODES and PROBLEM files.  In the example below, we know the result came from PROBLEM, file number 9000011.  Provider Narrative is field number .05 in the PROBLEM file.
FIEVAL(22,1,"CSUB","PROVIDER NARRATIVE")=1166
FIEVAL(22,1,"FILE NUMBER")=9000011
The corresponding CSUB Object is:
$$CSUBINTE(PROVIDER NARRATIVE,L40: ,9000011,.05,22,1)**$$CSUBNUM** is used when the data element is a number. The arguments are:
$$CSUBNUM(Subscript,Format,Finding Number,[OCCURRRENCE],[Separator],[Piece],[Text]) where
    - Subscript is the data element subscript.
    - Format can be one of two forms, depending on whether the number to be formatted is a date or a number.
        - For dates - D:date format:[Cell Format], where date format can be any of the formats used with CSUBDATE. **Note:** This gives you the ability to use dates other than the main finding date, which is used by CSUBDATE.
        - For numbers - N:[FC]:[DEC]:[Cell Format], where FC is a format code used by the MUMPS $FNUMBER function as listed in the next bullet. DEC is the number of digits after the decimal point. If the number has more digits than specified by this argument, the output is rounded. If the number has fewer digits, the output is zero filled.
    - The format code (FC) can be a combination of the following except as noted:
        - +  Forces a "+" for positive values.
        - -   Suppresses the "-" for negative values.
        - ,   Inserts commas every third position to the left of the decimal within the number.
        - T  Represents the number with a trailing, rather than a leading sign; positive numbers have a trailing space unless the expression includes a plus sign (+).
        - P   Represents negative values in parentheses, positive values with a space on either side; combining with any other code except comma (,) causes a run-time error.
    - Finding Number is the finding number.
    - [Occurrence] is the occurrence, used only if the value for a selected occurrence is desired. The Occurrence Count in the reminder definition should be set equal to or greater than the number of occurrences you are planning to display.
    - [Separator] Some data elements have multiple pieces of data and this is the character that separates them.
    - [Piece] Works in conjunction with Separator.  If there are multiple pieces of data, this specifies which one you want. If Piece is not specified, it defaults to 1. If Separator is not passed, Piece is ignored.
    - [Text]  If the data element does not exist, then Text will be returned.
Examples are shown below:
The finding is a vital measurement of temperature.  For example: FIEVAL(4,"CSUB","RATE")=102.3
The corresponding CSUB Object is:
$$CSUBNUM(RATE,N::1,4,,,,No temperature measurement was found)
N in the format specifies it is a number, no format code is passed, and one digit after the decimal will be displayed. If no temperature measurement is found, then the text “No temperature measurement was found.” will be displayed.
For a date other than the main finding date, an example is:
FIEVAL(5,3,"CSUB","DATE")=3170630.094942
The corresponding CSUB Object is:
$$CSUBNUM(DATE,D:5Z,5,3,,A third occurrence of the date was not found.)
D in the format says this is a date and 5Z says display the date as MM/DD/YYYY@HH:MM:SS, with leading zeroes. The finding number is 5 and we are going to show the date for the third occurrence. If the third occurrence does not exist, then the text “A third occurrence of the date was not found.” will be displayed.**$$CSUBTEXT** is used when the data element is text. The arguments are:
$$CSUBTEXT(Subscript,[Cell Format],Finding Number,[OCCURRRENCE],[Separator],[Piece],[Text]) where
    - Subscript is the data element subscript.
    - [Cell Format] is described in the middle of the CSUB Objects section.
    - Finding Number is the finding number.
    - [Occurrence] is the occurrence, used only if the value for an occurrence is desired.  The Occurrence Count in the reminder definition should be set equal to or greater than the number of occurrences you are planning to display.
    - [Separator] Some data elements have multiple pieces of data and this is the character that separates them.
    - [Piece] works in conjunction with Separator.  If there are multiple pieces of data, this specifies which one you want. If Piece is not specified, it defaults to 1. If Separator is not passed, Piece is ignored.
    - [Text] If the data element does not exist, then Text will be returned.
Examples are shown below:
The finding is a lab test. An example is:
FIEVAL(1,1,"CSUB","TEST NAME")=17-HYDROXYCORTICOSTEROIDS
The corresponding CSUB Object is: $$CSUBTEXT(TEST NAME,,1)
Another example is: FIEVAL(3,3,"CSUB","TEST NAME")=ANTI-THYROID ANTIBODIES GROUP
The corresponding CSUB Object is: $$CSUBTEXT(TEST NAME,,3,3)
It displays the test name for the third occurrence of finding number 3.
**Text Argument**
All the CSUB Objects have an optional Text argument that will be returned as the object text if the data element specified by the Subscript argument and optional Occurrence, Separator, and Piece arguments does not exist. The finding may be true but the specified data element you want to display may not have a value. For example, if you want to display the last three blood pressures, but only two were found, the Text for the third occurrence could be something like “A third blood pressure was not found”.
In Finding Found Text, if the data element will not exist unless the finding is true, there is no point in including the Text argument because the Found Text cannot be displayed when the finding is false. That is not necessarily the case for Function Finding Found Text. The function finding can be true while a finding used in the function finding is false. The Text argument could be used to display information that is relevant to the finding being false, such as “No test results were found.”
**Building Tables**
As mentioned earlier, the optional CELLFORMAT argument facilitates building tables. When building a table, you need to determine how wide each column should be. The total width of the table should not exceed 80 characters.
If the occurrence of a CSUB Object does not exist and there is no default text, then it will be set to the number of pad characters in CELLFORMAT. For example, if the CELLFORMAT is “L15:”, then the CSUB Object will be set to 15 spaces. If every CSUB Object in the row ends up being spaces, then you could end up with an unwanted blank line. Enclosing a table, or portions of it, in a Suppress Blank Line (SBL) block will suppress the display of blank lines. An SBL block starts with SBL{ and ends with }SBL. Just like when found/not found text is formatted, lines in an SBL block are concatenated until a “\\” is encountered.  The “\\” marks the end of a line.**Note:** The line numbers in the examples were added to facilitate the discussion and do not exist in the Found Text.
**Example 1**
1.1  Pulse Oximetry\\
1.2  Date             Value Entered By          Hospital Loc       Type\\
1.3  $$CSUBNUM(DATE,D:2M:L14:#,1,1)
1.4  $$CSUBTEXT(RATE,R7:#,1,1)
1.5  $$CSUBTEXT(ENTERED BY,L19:#,1,1)
1.6  $$CSUBTEXT(HOSPITAL LOCATION,L18:#,1,1)
1.7  $$CSUBINTE(LOCATION TYPE,L6:#,44,2,1,1)\\
1.8  SBL{$$CSUBNUM(DATE,D:2M:L14:#,1,2)
1.9  $$CSUBTEXT(RATE,R7:#,1,2)
1.10 $$CSUBTEXT(ENTERED BY,L19:#,1,2)
1.11 $$CSUBTEXT(HOSPITAL LOCATION,L18:#,1,2)
1.12 $$CSUBINTE(LOCATION TYPE,L6:#,44,2,1,2)\\
1.13 $$CSUBNUM(DATE,D:2M:L14:#,1,3)
1.14 $$CSUBTEXT(RATE,R7:#,1,3)
1.15 $$CSUBTEXT(ENTERED BY,L19:#,1,3)
1.16 $$CSUBTEXT(HOSPITAL LOCATION,L18:#,1,3)
1.17 $$CSUBINTE(LOCATION TYPE,L6:#,44,2,1,3)\\
1.18 $$CSUBNUM(DATE,D:2M:L14:#,1,4)
1.19 $$CSUBTEXT(RATE,R7:#,1,4)
1.20 $$CSUBTEXT(ENTERED BY,L19:#,1,4)
1.21 $$CSUBTEXT(HOSPITAL LOCATION,L18:#,1,4)
1.22 $$CSUBINTE(LOCATION TYPE,L6:#,44,2,1,4)\\}SBL
    - Line 1.1 is the overall header for the table.
    - Line 1.2 consists of the column headers.
    - Line 1.3 is the date of the pulse oximetry finding.
    - Line 1.4 is the measured value.  This field is named RATE in the Vitals package.
    - Line 1.5 is the person who entered the measurement.
    - Line 1.6 is the hospital location where the measurement was taken.
    - Line 1.7 is the hospital location type.
    - Lines 1.3-1.7 are combined to make the first row of the table.  The \\ at the end of 1.7 marks the end of the first row, which is for the first occurrence of the finding. If the finding is true, the first occurrence will always exist. Since this is Found Text. it will not be displayed unless the finding is true. Lines 1.8-1.12 make the next row of the table. It is a repeat of the data elements in row 1, but for occurrence two.
    - Lines 1.13-1.17 are the next row for occurrence three.
    - Lines 1.18-1.22 are the next row for occurrence four.
Because the table can display data for up to four occurrences, the Occurrence Count for the finding needs to be at least four. Even though four occurrences have been requested, the patient may not have all four of them. Enclosing the code that creates rows 2 through 4 of the table in an Suppressed Blank Lines (SBL) block will prevent blank lines being added to the table. The SBL block starts on line 1.8 and ends on line 1.22.
This example uses “#” as the pad character to provide a visual representation of how padding works. In most cases, you would not want to see pad characters in a table and your pad character would be a space.
**Example 2**
2.1  $$CSUBNUM(DATE,D:2M:L14: ,1,1) $$CSUBTEXT(RATE,R7: ,1,1)
2.2  $$CSUBTEXT(ENTERED BY,L19: ,1,1) $$CSUBTEXT(HOSPITAL LOCATION,L18: ,1,1)
2.3  $$CSUBINTE(LOCATION TYPE,L6: ,44,2,1,1)\\
2.4  SBL{$$CSUBNUM(DATE,D:2M:L14: ,1,2) $$CSUBTEXT(RATE,R7: ,1,2)
2.5  $$CSUBTEXT(ENTERED BY,L19: ,1,2) $$CSUBTEXT(HOSPITAL LOCATION,L18: ,1,2)
2.6  $$CSUBINTE(LOCATION TYPE,L6: ,44,2,1,2)\\
2.7  $$CSUBNUM(DATE,D:2M:L14: ,1,3) $$CSUBTEXT(RATE,R7: ,1,3)
2.8  $$CSUBTEXT(ENTERED BY,L19: ,1,3) $$CSUBTEXT(HOSPITAL LOCATION,L18: ,1,3)
2.9  $$CSUBINTE(LOCATION TYPE,L6: ,44,2,1,3)\\
2.10 $$CSUBNUM(DATE,D:2M:L14: ,1,4) $$CSUBTEXT(RATE,R7: ,1,4)
2.11 $$CSUBTEXT(ENTERED BY,L19: ,1,4) $$CSUBTEXT(HOSPITAL LOCATION,L18: ,1,4)
2.12 $$CSUBINTE(LOCATION TYPE,L6: ,44,2,1,4)\\}SBL
Example 2 is a repeat of data rows 1-4 in Example 1, with two differences: the pad character is a space and some of the lines in Example 1 have been combined into a single line, so the number of lines for data rows 1-4 has gone from 20 to 12. Some lines contain two CSUB Objects, but no CSUB Object spans two lines.
**A CSUB Object will not be recognized if it is broken across two lines. Each CSUB Object in a row must be separated by a space, even if there is only one object per line. In Example 1, you cannot see the space, but it is there. In Example 2, where there are two objects on a line, you can see the space.**
The following shows what these two examples look like in the Clinical Maintenance output for a patient who has three pulse oximetry occurrences:
Pulse Oximetry
Date             Value Entered By          Hospital Loc       Type
<!-- image -->
5/29/13@11:52# Refused LLLLL,FFF MMMMMMMMM 3 NORTH SURG###### WARD##     Example 1
5/29/13@11:18# #####99 LLLLL,FFF MMMMMMMMM 3 NORTH SURG###### WARD##
###### ####### ################### ################## ######
<!-- image -->
6/21/13@12:00       98 LLLLLLLLL,MMMMMM    3 NORTH SURG       WARD
5/29/13@11:52  Refused LLLLL,FFF MMMMMMMMM 3 NORTH SURG       WARD  	Example 2
5/29/13@11:18       99 LLLLL,FFF MMMMMMMMM 3 NORTH SURG       WARD
In Example 1, the pad character is “#”, so you can see it.  In Example 2, it is space, so it is not visible but it still affects the column widths.  The CELLFORMATs for the columns are described below:
    - Date - The CELLFORMAT is L14, but the date format of 2M produces 13 characters, so one pad character has been appended.
    - Value - The CELLFORMAT is R7. When the value is two digits, 5 pad characters are prepended. “Refused” is exactly 7 characters, so no pad characters are needed.
    - Entered By - The CELLFORMAT is L19. In rows 2 and 3 the last, first and middle name is longer than 19 characters, it is truncated, and no padding is needed.
    - Hospital Loc - The CELLFORMAT is L18 and 6 pad characters are required.
    - Type - The CELLFORMAT is L6 and 2 pad characters are required.
As noted earlier, this patient has three occurrences so there is no data to display in row 4. Consequently, in row 4 of Example 1, all the columns are filled with the pad character. Since the pad character is “#”, the row is not blank, and it is displayed even though it is in SBL block. In Example 2, the pad character is space, row 4 is blank and because it is in an SBL block, it is not displayed.

#### Function Findings

Function Findings (FF) do computations on the results from regular findings. Function Findings can be used just like regular findings with one exception, there is no date associated with an FF which means the Resolution Logic cannot be written so that it is made true solely by FFs.  Besides providing new and expanded functionality, FFs can make custom logic much simpler to understand.

Function Findings expand upon, and are intended to replace, the old-style "Most Recent Date" (MRD) functionality of Reminders 1.5 that could be used in Customized Patient Cohort Logic to return the most recent date from a list of finding items. Old MRD logic released in National Reminders will be converted to Function Findings and the reminders will be redeployed with V.2.0.

Note that this new functionality may be difficult to comprehend. Be advised that you should not attempt to modify existing Function Findings or create new Function Findings unless you understand what they do and test the results thoroughly.

##### Patch 65 changes to Function Findings

The following function finding functions have been enhanced so they can use the data in the FIEVAL(“CONTRA”) and FIEVAL(“REFUSED”) nodes. This provides the mechanism to use C/Rs in the CONTRAINDICATED LOGIC and REFUSED LOGIC.

COUNT

DIFF\_DATE

DTIME\_DIFF

DUR

FI

MAX\_DATE

MIN\_DATE

MRD

VALUE

See Appendix D for details.

##### Patch 26 changes to Function Findings

The executable help for the function string was upgraded by improving the text and using the Browser to display it.

Users reported that the display of function finding true/false values in the Clinical Maintenance output is useful to CACs, but confusing for clinical users. As a result, a change was made so that the function finding true/false values will be displayed only in the Clinical Maintenance output in reminder test.

Remedy ticket #823815 reported an undefined error during function finding evaluation. The function string being evaluated was “UROLOGY PCU”[“URO”. The error was occurring because a unary operator in the function string is flagged as being unary by appending the operator with a ‘U’. The code checking for a unary operator was improperly interpreting the ‘U’ in UROLOGY as a flag for a unary operator which caused the undefined error. The code was corrected. Additional changes: A check was added for division; if none is found, then the logic string is evaluated using indirection; if division is found, then special logic evaluation is used to trap division by zero. This may give a slight improvement in execution speed. The function finding step-by-step output in reminder test was made a little more readable.

Output of function finding true or false values for function findings used in cohort or resolution logic was added in PXRM*2.0*24. The reminder definition VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN has a lot of found and not found text and the display of the function finding values in the Clinical Maintenance output was giving the display of the text a poor appearance. This is an example of how it looks without the function finding values:

Resolution:

1. PTSD Screening completed since service discharge

2. Depression Screening completed since service discharge

3. Alcohol Screening completed since service discharge

Screening for at risk alcohol use using the AUDIT-C screening tool should be

performed yearly for any patient who has consumed alcohol in the past year.

No record of prior screening for alcohol use was found in this patient's

record.

4A. Screen for GI symptoms done or not required.

4A. Screen for GI symptoms done or not required.

Screen for diarrhea or other GI complaints that might suggest giardia,

amoebiasis or other GI infection.

4B. Screen for Fevers done or not required.

Screen for unexplained fevers that might represent occult malaria or

infection with leishmaniasis.

4C. Screen for Skin Rash done or not required.

Screen for persistent rash that might represent infection with leishmaniasis.

This is how it looks with the function finding values displayed:

Resolution:

FF(16)=0

FF(2)=1

1. PTSD Screening completed since service discharge

FF(3)=1

2. Depression Screening completed since service discharge

FF(18)=0

FF(4)=1

3. Alcohol Screening completed since service discharge

Screening for at risk alcohol use using the AUDIT-C screening tool should be

performed yearly for any patient who has consumed alcohol in the past year.

No record of prior screening for alcohol use was found in this patient's

record.

FF(17)=0

FF(5)=1

4A. Screen for GI symptoms done or not required.

FF(5)=1

4A. Screen for GI symptoms done or not required.

Screen for diarrhea or other GI complaints that might suggest giardia,

amoebiasis or other GI infection.

FF(6)=1

4B. Screen for Fevers done or not required.

Screen for unexplained fevers that might represent occult malaria or

infection with leishmaniasis.

FF(7)=1

4C. Screen for Skin Rash done or not required.

Screen for persistent rash that might represent infection with leishmaniasis.

FF(10)=0

The output as of patch 26  looks like this:

Resolution:

1. PTSD Screening completed since service discharge

2. Depression Screening completed since service discharge

3. Alcohol Screening completed since service discharge

Screening for at risk alcohol use using the AUDIT-C screening tool should be

performed yearly for any patient who has consumed alcohol in the past year.

No record of prior screening for alcohol use was found in this patient's

record.

4A. Screen for GI symptoms done or not required.

4A. Screen for GI symptoms done or not required.

Screen for diarrhea or other GI complaints that might suggest giardia,

amoebiasis or other GI infection.

4B. Screen for Fevers done or not required.

Screen for unexplained fevers that might represent occult malaria or

infection with leishmaniasis.

4C. Screen for Skin Rash done or not required.

Screen for persistent rash that might represent infection with leishmaniasis.

FF(2)=1, FF(3)=1, FF(4)=1, FF(5)=1, FF(6)=1, FF(7)=1, FF(10)=0, FF(16)=0,

FF(17)=0, FF(18)=0


##### Patch 24 Changes to Function Findings

Function findings were changed in PXRM*2*18 to allow the MUMPS division operators in the function string, which meant there is the possibility of division by 0. The function finding evaluation code was changed, to trap a division by 0 so it would not generate an error, and the function finding was set to false if there was a division by 0. During testing of PXRM*2*24, it was determined that this behavior was not optimal since only the portion of the function string involving the division by 0 should be set to false. The function finding evaluator was changed to do this and **a new feature was added to reminder test that shows step-by-step how the function string is evaluated. Also the display of the reminder test was moved to the FileMan Browser to make it easier to view.**

A fix was made for a problem reported in Remedy ticket #242214, which reported that reminder tests produced an error when either a patient or a reminder was not selected.


##### Patch 18 Changes to Function Findings

The set of allowed operators in function finding strings was expanded. It now includes: +, -, *, **, /, \, #, !, &amp;, `, &gt;, &lt;, =, ], [. The additions were *, **, /, \, #.

All function findings were improved to handle the case when the findings they use are false. Functions will now return the value “UNDEF” when they cannot be evaluated.

An optional third argument of “NAV” was added to the DIFF\_DATE function. If this argument is present, the actual value instead of the absolute value is returned.

Two new functions, MAX\_VALUE and MIN\_VALUE, were added.

A new function DIFF\_DT which is a generalized version of DIFF\_DATE was added.

There were some CSUBs that could not be used in a function finding because they would not pass the input transform. ”ADMISSION DATE/TIME” is an example of one that could not be used. It was not passing because of the space and the “/”.The input transform was changed to allow all legitimate CSUBs.

Clin2 reported that a list type reminder that used the VALUE function in a function finding failed the validation when creating a reminder rule. This was because the validater was written before functions could have CSUB values as arguments. The validation code was changed to handle those cases.

##### Creating a Function Finding

To define or edit a Function Finding, select the option “FF  Function Finding” from the reminder definition editor (in Add/Edit Reminder Definition or Copy Reminder Definition on the Reminder Definition Management menu).

The name of a Function Finding is a number, so, when prompted to “Select FUNCTION FINDING,” enter a number. Function Finding number 1 is created in the following example:

Select Reminder Definition:    FFTEST     LOCAL

Select one of the following:

A         All reminder details

G         General

B         Baseline Frequency

F         Findings

FF        Function Findings

L         Logic

C         Custom date due

D         Reminder Dialog

W         Web Addresses

Select section to edit: **FF** Function Findings

Function Findings

Select FUNCTION FINDING: 1

**Are you adding '1' as a new FUNCTION FINDINGS** (the 1ST for this REMINDER DEFINITION)? No// **Y**

(Yes)

FUNCTION FINDINGS FUNCTION STRING: MRD(1,3)&gt;MRD(11,8,4)

FUNCTION FINDING NUMBER: **1** // **&lt;Enter&gt;**

FUNCTION STRING: MRD(1,3)&gt;MRD(11,8,4)  Replace **&lt;Enter&gt;**

FOUND TEXT:

No existing text

Edit? NO// &lt;Enter&gt;

NOT FOUND TEXT:

No existing text

Edit? NO// **&lt;Enter&gt;**

USE IN RESOLUTION LOGIC: **&lt;Enter&gt;**

USE IN PATIENT COHORT LOGIC: **&lt;Enter&gt;**

REMINDER FREQUENCY: **&lt;Enter&gt;**

MINIMUM AGE: **&lt;Enter&gt;**

MAXIMUM AGE: **&lt;Enter&gt;**

RANK FREQUENCY: &lt;Enter&gt;

Select FUNCTION FINDING: &lt;Enter&gt;

When prompted, enter the number of the finding you want to create/edit. If the function finding number does not exist, you will be asked to confirm that you want to add a new function finding:

Select FUNCTION FINDING: 1

Are you adding '1' as a new FUNCTION FINDINGS (the 1ST for this REMINDER DEFINITION)? No// Y

(Yes)

Next, you will be prompted to add the Function Finding string.

FUNCTION FINDINGS FUNCTION STRING: MRD(1,3)&gt;MRD(11,8,4)

Then the name and the FUNCTION STRING will be displayed on the screen so you can modify the FUNCTION STRING if you wish to do so:

FUNCTION FINDING NUMBER: 1//

FUNCTION STRING: MRD(1,3)&gt;MRD(11,8,4)  Replace

Lastly, you will be prompted for the following fields, which work the same as they do with regular Findings.

FOUND TEXT:

No existing text

Edit? NO//

NOT FOUND TEXT:

No existing text

Edit? NO//

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

If the FF is true and USE IN RESOLUTION LOGIC and USE IN PATIENT COHORT LOGIC are not specified, the FF found/not found text will appear under the Clinical Maintenance Information heading.

###### Function Findings Primer

Function findings operate on data from standard findings and return computed data. They can be used in Patient Cohort Logic, Resolution Logic, Contraindicated Logic, and Refused Logic or for display as informational text. Function findings functions are stored in file #802.4. This file defines the functions that can be used in function finding strings.

- OPERATORS and GLOBAL VARIABLES
- MRD
- MAX\_DATE
- MIN\_DATE
- COUNT
- FI
- DUR
- DIFF\_DATE
- DTIME\_DIFF
- VALUE
- NUMERIC
- MAX\_VAL
- MIN\_VAL

Operators and Global Variables

The mathematical operators that can be used are as follows:

+ 	 ADD

- 	Subtract

*	Multiply

/	Divide by

\	Integer division (remainder is dropped)

**	Exponential

#	Modulus (remainder)

&gt;	Greater than

&lt;	Less than

=	Equals

The logical operators that can be used are as follows:

&amp;	And

!	Or

' 	Not

[	Contains

]	Follows

Please note that even though all of these operators may be used within function findings, it is not always clinically relevant to use them.  We will list the operators for each function that would clinically apply.

For example, we could multiply the date of FI(1) by the date of FI(2) and do a comparison to some number, but that would not be clinically relevant.

Function string:  MRD(1)*MRD(2)&gt;60

Clinically, there would be no reason to multiply two dates.

Certain **Global Variables** are set every time a reminder is evaluated on a patient. These are as follows:

PXRMAGE – Returns the patient’s age

PXRMDATE – The reminder evaluation date and time

PXRMDOB – Returns the patients date of birth in FileMan format

PXRMDOD – Returns the patients date of death, if it exists, in FileMan format

PXRMLAD – Returns the patients last admission date, if it exists, in FileMan format

PXRMSEX – Returns the patients sex

Global variables may be used in function findings as part of the string.

Example:  MRD(1)&gt;MRD(2)&amp;(PXRMAGE&gt;50)

The Global Variables may NOT be the only part of the string.

MRD

This function returns the most recent date of the finding(s) in the argument list of the MRD string, and then makes a comparison based on the operator used to another MRD string or a reminder global variable.

All mathematical operators may be used with MRD, but the relevant operators include:

Greater than - &gt;

Less than - &lt;

Equals - =

Relevant logical operators include:

Not – '

And - &amp;

Or - !

These may be used in combinations as well; i.e.  ‘&lt;, ‘=, ‘&gt;

Examples:

1. MRD(1)'&gt;MRD(2)   This would be true if the date of finding 1 is less than or equal to the date of finding 2.  This is because of the “NOT GREATER THAN” notation which implies “less than or equal to.”
2. MRD(1,2)&lt;MRD(3)  This would be true if the most recent date of finding 1 and 2 is less than the date of finding 3.  If both finding 1 and 2 are true, the function would return the most recent date of those two for the comparison to finding 3.
3. MRD(1,2)=MRD(3,4)  This would be true if the most recent date of finding 1 and 2 is equal to the most recent date of finding 3 and 4. If both finding 1 and 2 are true, the function would return the most recent date of those two.  The same would hold true for the second part of this string, where, for comparison, the most recent date of finding 3 or 4 would be returned.
4. MRD(1)&gt;PXRMLAD  This would be true if the date of finding 1 is more recent than the patient’s last admission date.
5. (MRD(1,2) &gt;MRD(4))&amp;(PXRMDOB&gt;2500101)  This would be true if the most recent date of findings 1 and  2 is more recent than the date of finding 4, AND the patient’s date of birth is after January 1, 1950.

Be aware that if you have a date range defined by Beginning Date/Time (BDT) and Ending Date/Time (EDT)  set on the finding(s) that is part of the MRD string, it could affect the date returned. For example, your string is MRD(1,2)&gt;MRD(3) and there is no EDT entry on either finding, then the function will work as described above.  If there is an EDTentry, let’s see how the outcome is affected.

FI(1) has ending date/time entry  of T-1Y  and FI(2) has NO EDT:

Dates of findings, and assuming today is 7/29/10 for the example:

FI(1)                               FI(2)

7/24/10			6/18/10

2/3/10			4/8/10

6/1/09			3/20/08

Given these dates with the EDT entry on FI(1), the MRD that would be used to compare to FI(3) would be date of 6/18/10 from FI(2).  Even though the FI(1) dates of 7/24/10 and 2/3/10 exist, because of the ending date/time entry of T-1Y, they are not considered in the evaluation.

Another caveat of the MRD functionality is the use of a finding in the MRD string that has a negative occurrence count.

Example:   MRD(1)&gt;MRD(2)  and Finding 1 has a -1 occurrence count

FI(1)                                FI(2)

7/24/10			8/18/10

2/3/10			4/8/10

6/1/09			3/20/08

With FI(1) having a -1 as occurrence count, the function string MRD(1)&gt;MRD(2) would evaluate to false because the date of FI(1) would be 6/1/09, which is the OLDEST occurrence retrieved by use of the -1 in the occurrence count of FI(1).

MRD can be also combined with other functions and global variables as below:

MRD(1)&gt;MIN\_DATE(2)&amp;(COUNT(2)&gt;3)

MRD(2)&gt;3100510!(PXRMAGE&gt;45)

CLASS: NATIONAL

MAX\_DATE

MAX\_DATE is just another name for MRD so everything in the above discussion of MRD applies to MAX\_DATE.

CLASS: NATIONAL

MIN\_DATE

This function finding returns the oldest date of the finding(s)  in the argument list of the MIN\_DATE string, and then makes a comparison based on the operator used  to another MIN\_DATE string or a global variable.

All mathematical operators may be used with MIN\_DATE but the relevant operators include:

Greater than - &gt;

Less than - &lt;

Equals - =

Relevant logical operators include:

Not – '

And - &amp;

Or - !

These may be used in combinations as well, i.e.  ‘&lt;, ‘=, ‘&gt;

Examples:

1. MIN\_DATE(1)&gt;MIN\_DATE(2)   This would be true if the date of finding 1 is more recent than the date of finding 2
2. MIN\_DATE(1,2)&lt;MIN\_DATE(3)  This would be true if the oldest date of finding 1 and 2 is less than the date of 3.  If both finding 1 and 2 are true, the function would use the oldest date of those two for the comparison to finding 3
3. MIN\_DATE(1,2)=MIN\_DATE(3,4)  This would be true if the oldest date of finding 1 and 2 is equal to the oldest date of finding 3 and 4. If both finding 1 and 2 are true, the function would use the oldest date of those two.    The same would hold true for the second part of this string where for comparison, the oldest date of finding 3 or 4 would be used.
4. MIN\_DATE(1)&gt;PXRMLAD  This would be true if the date of finding 1 is more recent than the patients last admission date.
5. (MIN\_DATE(1,2) &gt;MIN\_DATE(4))&amp;(PXRMDOB&gt;2500101)  This would be true if the oldest date of findings 1 and  2 is more recent than the date of finding 4  AND the patient s date of birth is after January 1, 1950.

Please note that if you have date range defined by Beginning Date/Time (BDT) and Ending Date/Time (EDT) on a finding it may impact your results.  The date range will restrict the dates used for evaluation to only those occurring during the specified date range.  So your oldest finding date will be the oldest one of those within the range.

For example, in the Function Finding of MIN\_DATE(1) &gt; MIN\_DATE(2), below is a list of all the dates for each finding.

**FI(1)                                                       FI(2)**

7/29/10                                                6/26/10

6/15/10                                                4/1/09

3/26/08                                                2/5/08

With no BDT defined on either finding the evaluation of MIN\_DATE(1) &gt; MIN\_DATE(2) would be

7/29/10&gt;6/26/0, thus the finding is TRUE.

If you had a BDT of T-1Y on FI(1) (given today is 7/29/10)  the evaluation of MIN\_DATE(1) &gt; MIN\_DATE(2) would now be 6/15/10&gt; 6/26/10, thus the FF is FALSE.

Another caveat of the MIN\_DATE functionality is the use of a finding in the MIN\_DATE string that has a negative occurrence count.

Example:   MIN\_DATE(1)&gt;MIN\_DATE(2)  and Finding 1 has a -2 occurrence count

FI(1)                                FI(2)

7/24/10			6/18/10

2/3/10			4/8/10

6/1/09			3/20/08

With FI(1) having a -2 as occurrence count, the function string MIN\_DATE(1)&lt;MIN\_DATE(2) would evaluate to true because MIN\_DATE of FI(1) would be 6/1/09 and MIN\_DATE of  FI(2) would be 6/18/10.

MIN\_DATE can be also combined with other functions and global variables as below:

MIN\_DATE(1)&gt;MIN\_DATE(2)&amp;(COUNT(2)&gt;3)

MIN\_DATE(2)&gt;3100510!(PXRMAGE&gt;45)

CLASS: NATIONAL

COUNT

The COUNT  Function Finding checks to see if there are a certain number of true occurrences of a particular finding.  The syntax of this function finding is COUNT(N)&gt;3.  In this example, a check is done to see if there are more than three occurrences of finding number N.  The COUNT function works in conjunction with the Occurrence Count finding modifier of the finding number that COUNT is looking at.  If you have your COUNT string set as COUNT(1)&gt;2, then on FI(1), you will need to ensure the occurrence count is set to at least 3.  There are other factors that come into play as well, such as entries on the following fields:  CONDITION, BEGINNING DATE/TIME, ENDING DATE/TIME, USE STATUS/COND IN SEARCH.  These will be addressed below.

All mathematical operators that may be used with COUNT, but the relevant operators or operator combinations include:

Less than - &lt;

Greater than - &gt;

Equal to - =

NOT – '

AND - &amp;

OR - !

With no entries on the above mentioned fields (CONDITION, BEGINNING DATE/TIME, ENDING DATE/TIME, USE STATUS/COND IN SEARCH), the COUNT works as follows:

FI(N) has occurrence count of 3

FF(N) has string of COUNT(N)&gt;2

The FF(N) will be true if FI(N) has at least 3 occurrences

If FI(N) has dates defined on beginning date/time or ending date/time, then when COUNT is invoked, it will look for the number of occurrences designated by the entry in the occurrence count field within those date ranges and then based on what the string of COUNT is, will make a determination of TRUE or FALSE.

**With Use Status/Condition in Search set to NO**

If FI(N) has a Condition or Status associated, then the number of returned occurrences will be less than or equal to the occurrence count. Each returned occurrence will have the condition applied so they  may be true or false.  Also, if there are entries on beginning date/time and ending date/time, those parameters will also be considered in the evaluation of the FF.  Example:  FI(1) is an A1C  lab test with condition of I V&gt;9.0 and occurrence count of 5.  Given a list of values within the date range specified by beginning date/time and ending date/time are as follows:

8.0, 7.5, **9.1** , **9.2** , 8.8, 8.4, 9.3, 9.4, 7.9, 9.1, 8.5

The value of COUNT(1) will be 2 because only the last five occurrences are considered.  If you had a string of COUNT(1)&gt;2, then the FF would be false.

**With Use Status/Condition in Search set to YES**

Again, assuming occurrence count of 5 on  FI(N) (Lab test) and condition of I V&gt;9.0, up to the last 5 occurrences that **actually meet** the condition within the date range will be returned.  Given the same list of values as above, the number of occurrences up to the occurrence count that meet the condition will be returned.

8.0, 7.5, **9.1** , **9.2** , 8.8, 8.4, **9.3, 9.4** , 7.9, **9.1** , 8.5

The bold values will be returned and if the String of the FF was COUNT(N)=5, then the FF would be TRUE.  Be careful with the use of USE  STATUS/CONDITION in SEARCH as it will affect your outcome.

COUNT can be also combined with other functions and global variables as below:

COUNT(1)&gt;2&amp;(COUNT(3)=1))

COUNT(4)=2!(MRD(2)&gt;MRD(1))

COUNT(3)&lt;5&amp;(PXRMAGE&gt;50!PXRMLAD&gt;3100317)

CLASS: NATIONAL

FI

This function returns the true or false value of a finding. It provides a way to logically string regular findings and/or other functions and/or reminder global variable combinations together in a function string.  Complex strings can be written using parenthesis to group items together.

Below are some examples.  In some of these examples you will see the use of the global variables and other functions:

FI(1)&amp;FI(2)&amp;(FI(3)!FI(4))

F(1)&amp;FF(1)&amp;’FF(2)

FI(2)&amp;FF(1)&amp;(MRD(1)&gt;PXRMLAD)

FI(2)&amp;FI(3)&amp;FI(4)&amp;’FF(1)&amp;(PXRMSEX=”F”)&amp;(PXRMDOB&gt;2500101)

CLASS: NATIONAL

DUR (Duration)

For findings that have a start and stop date (orderable items, medications), DUR will be the number of **days** between the start and stop date of the finding.  For orders/medications that do not have a stop date, the current date is used as the stop date.

DUR(N)&gt;60

Orderable Item example

FI(1)=OI.HEMATOLOGY CONSULT

FF(1)=DUR(1)&gt;60

Here is an excerpt from a reminder test to show how this works for a finding with no stop date:

Orderable Item: HEMATOLOGY CONSULT
  06/20/2006 Status: pending, Start date: 04/02/2004, Stop date:  missing

The DUR would be 809 days:

FIEVAL("FF1","VALUE")=809  if the current date was 6/20/2006.  The reminder calculates the number of days from 04/02/2004 (start date of consult) and stop date, which in this case we are using 06/20/2006 as the current date.

For findings that have only a single date, DUR works in conjunction with the Occurrence Count Field and is the number of days between the first and last occurrence.  If there is only one occurrence, then DUR will be 0.  The default value of the occurrence count field is 1, therefore, if you are using the DUR on a finding that only has 1 as the occurrence count, the DUR will always be 0.   Your Occurrence Count Field setting will determine which findings are evaluated. For example, let’s assume you have a specific Health Factor (HF) that is in a Veterans record 10 times. If your Occurrence Count is set to 5, the DUR will be only evaluated between the most recent date of the HF and that of the 5 th most recent date of the HF.  If your Occurrence Count is set to 99, then the most recent and the oldest dates of the HF are compared to give the DUR. Since the highest numerical value for the occurrence count field is 99, in theory, if you had 200 occurrences (of a blood pressure or pain score), then instead of getting the duration of the most recent occurrence and the 200 th occurrence, you would in actuality get the duration of the most recent and the 99 th occurrence.

Please note that if you have a Beginning Date Time (BDT) or Ending Date Time (EDT) on your finding, the Occurrence Count will only pull the specified number of entries during that time frame and then do the DUR evaluation on the First and Last dates of those "filtered" list of finding items.

Another example showing how your return value for DUR could be affected by occurrence count entry:

Finding 1 is a Health Factor with given entry dates:

3100624 (June 24, 2010)

3090516 (May 16, 2009)

3080516 (May 16, 2008)

If the function finding string is DUR(1)&gt;370 and if the occurrence count of FI(1) is set to a value of 2, then DUR would be true because difference would be 404, which is the difference between the most recent and second most recent entries.  If occurrence count is set to -2, then DUR would be False because difference is 365, which is the difference between the oldest and second oldest entries.

DUR can be also combined with other functions and global variables as below:

DUR(1)&gt;120&amp;(DIFF\_DATE(1,2)&gt;100)

DUR(2)&lt;50&amp;((PXRMAGE&gt;75)&amp;(MRD(1)&gt;3060910))

CLASS:  NATIONAL

DIFF\_DATE

This function returns the difference in days between the dates of the two findings listed as parameters.  The default is to return the absolute value, but if the optional third parameter of “N” is present, the actual value is returned.  If you want the actual value, be aware that if the date of the second parameter is more recent than the date of the first parameter, the result will be negative.

Syntax:   DIFF\_DATE(M,N)&gt; *n* where the “M” and “N” are findings and are also called parameters in this case and *n* is the number of days.

Some examples:

Given dates

FI(1)=3100710 (July 10, 2010)

FI(2)=3100720 (July 20, 2010)

DIFF\_DATE(1,2)&gt;5 This will evaluate as TRUE because there are 10 days (absolute value) between FI(1) and FI(2)

DIFF\_DATE(1,2,"N")&lt;-6 This will evaluate as TRUE because there are negative 10 (-10) days between FI(1) and FI(2).  If we simply change the order of the parameters (FI(1) and FI(2)), it  will change the evaluation as long as the “N” is left as a third parameter.

DIFF\_DATE(2,1,”N”)&lt;-6  This will evaluate as FALSE because there are 10 days between FI(1) and FI(2)

You **cannot** use reminder global variables directly in the DIFF\_DATE function since it only works on dates of regular findings. You **can** use the Computed Finding VA-FILEMAN DATE to create a regular finding with a specific date. For example, if you want to determine if the date of finding 1 occurred more than 20 days after the last admission, set up the computed finding (VA-FILEMAN DATE ) with PXRMLAD in the Computed Finding Parameter field. If finding 2 is the computed finding, the function string would be DIFF\_DATE(1,2)&gt;20. Another example would be to compare the date of FI(1) to today’s date. Again, you would  use the computed finding VA-FILEMAN DATE and enter TODAY or NOW (if you want the time included) into the computed finding parameter field. Then function string would be something like DIFF\_DATE(1,2)&gt;200.

In the above examples, the assumption is made that there are no entries on beginning date/time and ending date/time fields.  Again, as with other functions, having a date range on the finding could affect the dates that are used.  Let’s give an example.

FI(1) dates:

3100501

3090501

FI(2) dates:

3100525

FI(1) has an ENDING DATE/TIME entry of 3100430.  FI(2) has no ENDING DATE/TIME entry.

Given these dates and a DIFF\_DATE string of DIFF\_DATE(1,2)&gt;30, the FF will be TRUE because for FI(1), the date that will be used is 3090501 due to the entry in ENDING DATE/TIME field.

The comparison would be 389&gt;30 which is true.  The 389 value is the number of days between FI(1) and FI(2).  If you remove the ENDING DATE/TIME entry, then the FF will be FALSE because for FI(1), the date that will be used is 3100501. The comparison would be 24&gt;30 which is false. The 24 value is the number of days between FI(1) and FI(2).

DIFF\_DATE can be also combined with other functions and global variables as below:

DIFF\_DATE(1,2)&gt;100&amp;(MRD(1,2)&gt;MRD(3))

DIFF\_DATE(2,4)=0!(PXRMDOB&gt;2450101)

CLASS: NATIONAL

DTIME\_DIFF

This function is a generalized time function that returns the difference in time between the dates of two findings. The difference in time can be displayed down to the second. It can be displayed by Days, Hours, Minutes or Seconds. This function also gives you the ability to look at specific occurrences and CSUB items. Note that if you want to compare an occurrence other than the first, you must set the occurrence count on that finding to be greater than 1. Also, fields such as BEGINNING DATE/TIME, ENDING DATE/TIME, CONDITION, USE STATUS/COND IN SEARCH can change the dates returned by the function.

Syntax: DTIME\_DIFF(F1,O1,C1,F2,O2,C2,U,”A”) where F is finding number, O is occurrence number, C is CSUB item, U is units which can be D for Days, H for Hours, M for Minutes or S for Seconds.  If A is present, then the absolute value of the difference will be returned. If A is omitted, then the result could be calculated as a negative value. The parameters in the DIFF\_DT function that are text must be enclosed in quotes.

Example: DTIME\_DIFF(1,1,”DATE”,2,1,”DATE”,”D”,”A”)

In this example the absolute value, in Days, the difference between finding 1, occurrence 1 DATE CSUB and finding 2, occurrence 1 DATE CSUB

Some examples of DTIME\_DIFF

FI(1) has 3 occurrences and we have the occurrence count set to 3

Dates of occurrences:

3100409

3090409

3080409

**DTIME\_DIFF(1,1,”DATE”,1,2,”DATE”,”D”,”A”)&gt;300** would evaluate to TRUE because the absolute difference in DAYS between the first occurrence of finding 1 date and the second occurrence of finding 1 date is 365 days, so 365&gt;300.

**DTIME\_DIFF(1,1,”DATE”,1,3,”DATE”,”H”)&gt;14400** would evaluate to TRUE because the difference in HOURS between the first occurrence of finding 1 date and the third occurrence  of finding 1 date is 17520 hours, so 17520&gt;14400

**DTIME\_DIFF(1,2,”DATE”,1,1,”DATE”,”D”)&gt;50** would evaluate to FALSE because the difference in DAYS between the second occurrence of finding 1 date and the first occurrence of finding 1 date is -365 days, so -365&gt;50 is FALSE. The reason the result is negative (-365) is because we did not specify the “A” parameter for absolute value.

DTIME\_DIFF can be also combined with other functions and global variables as below:

DTIME\_DIFF(1,1,”DATE”,1,2,”DATE”,”D”)&gt;60&amp;(COUNT(2)=5)

DTIME\_DIFF(1,1,”DATE”,2,1,”DATE”,”D”,”A”)&lt;400&amp;(PXRMAGE&gt;40)

CLASS: NATIONAL

VALUE

The VALUE function returns any of the “CSUB” values of a particular occurrence of a finding for comparison to a different occurrence of the same finding or to an occurrence of a different finding.  The argument list is the finding number, the occurrence and the CSUB of interest. For example, if you wanted to check to see if occurrence 1 of finding 4 was less than occurrence 2 of the same finding, the function string would be VALUE(4,1,”VALUE”)&lt;VALUE(4,2,”VALUE”). If you are comparing multiple occurrences of a particular finding, then you must remember to set the occurrence count on that finding to a value high enough to work in your function string. Note that fields BEGINNING DATE/TIME, ENDING DATE/TIME, CONDITION, USE STATUS/COND IN SEARCH may have significant impact on the data returned by the VALUE function. Also, using a negative number in the occurrence count will/could have a significant impact on the results returned.

Common operators used with the VALUE function are:

Greater than - &gt;

Less than - &gt;

Equals - &gt;

AND - &amp;

OR - !

NOT – '

Examples:

I.  Finding 1 is a lab test with occurrence count set to 3. Values are as follows

6.0

5.5

5.0

VALUE(1,1,”VALUE”)&gt;(VALUE(1,2,”VALUE”))&gt;(VALUE(1,3,”VALUE”))

6.0&gt;5.5&gt;5.0 would evaluate to TRUE which could be clinically significant because the value is trending upwards.

II.  Finding 1 is an education topic with occurrence count set to 2. The CSUB “Level of Understanding” values are as follows:

Occurrence 1 – POOR

Occurrence 2 – POOR

VALUE(1,1,”LEVEL OF UNDERSTANDING”)=”POOR”&amp;(VALUE(1,2,”LEVEL OF UNDERSTANDING”)=”POOR”)) This could be clinically significant because the last two education topics level of understanding was POOR

VALUE can be also combined with other function and global variables as below:

VALUE(1,1,”LEVEL OF UNDERSTANDING”)=”POOR”&amp;(COUNT(2)=2)

VALUE(1,1,”LEVEL OF UNDERSTANDING”)=”POOR”!(PXRMLAD&gt;3100909)

CLASS: NATIONAL

NUMERIC

The NUMERIC function returns the first numeric portion of any CSUB value for a particular finding. For example, if the COMMENT field of a health factor contains a numeric value (i.e. an outside lab result), NUMERIC can be used test it.

Assume finding 1) is a Health Factor for an outside HGB A1C result.  On the reminder dialog, there is a comment field associated with the dialog element. If a numeric value is entered into the comment field as a piece of the comment, then it becomes computable data for the NUMERIC function. This value in this comment field is stored in PCE associated with the health factor, so that when a reminder is evaluated, that value can be used as a possibility for cohort or resolution logic or displayed as informational text.

The syntax of NUMERIC is finding number, occurrence, CSUB.

NUMERIC(1,1,”COMMENT”)&gt;5.0. This essentially says the function will be true if the very first numeric portion of the comment field of finding 1, occurrence 1 is greater than 5.0. Note that if the comment field entry is “A1C: 8.5”, the first number in the string is 1, therefore the NUMERIC function will return 1, not 8.5. It is strongly suggested that if you are using this function, you should provide education to the fact that the first part of the comment should be numeric.

As with all functions, the BEGINNING DATE/TIME, ENDING DATE/TIME, CONDITION, USE STATUS/COND IN SEARCH fields could significantly impact your results, so pay close attention to these entries.

NUMERIC can be also combined with other functions and global variables as below:

NUMERIC(1,1,”COMMENT”)&gt;4.0&amp;’(MRD(2)’&lt;3100909)

NUMERIC(2,2,”COMMENT”)&lt;5&amp;(PXRMAGE&gt;60)

CLASS: NATIONAL

Patch PX*1*211 and CPRS v 32B provide a reliable mechanism to store measurements. It does not depend on the user inputting the comment in a certain format. Therefore, Comments should no longer be used to store measurements. See Appendix C to learn how to use this functionality.

MAX\_VALUE

The MAX\_VALUE function returns the maximum value of *n* number of occurrences of a specific CSUB or multiple CSUB’s of a single finding or multiple findings. The CSUB that is being requested must be a numeric value. Any CSUB requested that is not numeric will be treated as having a value of zero. For instance, if you want to know the largest A1C result a patient has, you can use the MAX\_VALUE function.

The syntax of the function is MAX\_VALUE(N,”CSUB”)&lt;operator&gt;&lt;test value&gt; where N is the finding number.  In the above example with A1C, assume the A1C is FI(1), the function would be written as MAX\_VALUE(1,”VALUE”). Note that you have to set the occurrence count on finding 1 to a value greater than 1 or you will get the latest (most recent) result. If you wanted to look at the last 20 A1C values and see if the largest value is greater than 10, you would set the occurrence count to 20 on the finding and then use the string MAX\_VALUE(1,”VALUE)&gt;10. The function finding will be true if the value returned from MAX\_VALUE is greater than 10.

When using the function with multiple findings and CSUB’s, the syntax is a bit more complex. MAX\_VALUE(X,”CSUB”,Y,”CSUB”,Z,”CSUB”)&lt;operator&gt;&lt;test value&gt;, where X,Y and Z are all separate findings. Again, for each finding, the number of results returned is only up to whatever value is set in the occurrence count of each finding. In this example, the largest value of all findings evaluated is returned and a comparison is made to the test value.

Example: FI(1) is lab test with occurrence count of 5 with the following values:

100

103

98

96

92

The MAX\_VALUE(1,”VALUE”)&gt;100 would be TRUE because the largest value returned from the last 5 occurrences is 103. If you did not set the occurrence count field entry, then the result would be FALSE because the largest value would be 100.

As with all functions, the BEGINNING DATE/TIME, ENDING DATE/TIME, CONDITION, USE STATUS/COND IN SEARCH fields could significantly impact your results so pay close attention to these entries.

MAX\_VALUE can be also combined with other functions and global variables as below:

MAX\_VALUE(1,”VALUE”)&gt;10&amp;(MRD(1,2)&gt;MRD(4))!(COUNT(6)&lt;3)

MAX\_VALUE(1,”VALUE”)&lt;4.0&amp;(PXRMAGE&lt;40)&amp;(PXRMSEX=”F”)

CLASS: NATIONAL

MIN\_VALUE

The MIN\_VALUE function returns the minimum value of *n* number of occurrences of a specific CSUB or multiple CSUB’s of a single finding or multiple findings. The CSUB that is being requested must be a numeric value. Any CSUB requested that is not numeric will be treated as having a value of zero. For instance, if you want to know the smallest A1C result a patient has, you can use the MIN\_VALUE function.

The syntax of the function is MIN\_VALUE(N,”CSUB”)&lt;operator&gt;&lt;test value&gt; where N is the finding number.  In the above example with A1C, assume the A1C is finding 1. The function would be written as MIN\_VALUE(1,”VALUE”). Note that you have to set the occurrence count on FI(1) to a value greater than 1 or you will get the latest (most recent) result. If you wanted to look at the last 20 A1C values and see if the smallest value is greater than 10, you would set the occurrence count to 20 on the finding and then use the string MIN\_VALUE(1,”VALUE)&gt;10. The function finding will be true if the value returned from MIN\_VALUE is greater than 10.

When using the function with multiple findings and CSUB’s, the syntax is a bit more complex. MIN\_VALUE(X,”CSUB”,Y,”CSUB”,Z,”CSUB”)&lt;operator&gt;&lt;test value&gt;, where X,Y and Z are all separate findings. Again, for each finding, the number of results returned is only up to whatever value is set in the occurrence count of each finding. In this example, the smallest value of all findings evaluated is returned and a comparison is made to the test value.

Example: FI(1) is lab test with occurrence count of 5 with the following values:

100

103

98

96

92

The MIN\_VALUE(1,”VALUE”)&gt;99 would be FALSE because the smallest value returned from the last 5 occurrences is 92. If you did not set the occurrence count field entry, then the result would be TRUE because the smallest value would be 100.

As with all functions, the BEGINNING DATE/TIME, ENDING DATE/TIME, CONDITION, USE STATUS/COND IN SEARCH fields could significantly impact your results so pay close attention to these entries.

MIN\_VALUE can be also combined with other functions and global variables as below:

MIN\_VALUE(1,”VALUE”)&gt;10&amp;(MRD(1,2)&gt;MRD(4)!COUNT(6)&lt;3)

MIN\_VALUE(1,”VALUE”)&lt;4.0&amp;(PXRMAGE&lt;40&amp;PXRMSEX=”F”)

CLASS: NATIONAL

#### Status List

Status List applies only to finding types that have a status, they are:

Inpatient pharmacy

Outpatient pharmacy

Orders

Problem List

Radiology

Reminder Taxonomy

Reminder Terms

If no Status List is specified, then certain defaults apply:

| **Finding Type**       | **Default Status**   |
|------------------------|----------------------|
| Inpatient Medications  | ACTIVE               |
| Orderable Item         | ACTIVE, PENDING      |
| Outpatient Medications | ACTIVE, SUSPENDED    |
| Problem List           | ACTIVE               |
| Radiology Procedure    | COMPLETE             |

**Default View** (This example is for a Radiology Procedure as the Finding Item)

Statuses already defined for this finding item:

COMPLETE

Select one of the following:

A         ADD STATUS

D         DELETE A STATUS

S         SAVE AND QUIT

Q         QUIT WITHOUT SAVING CHANGES

Enter response: S// ?

Display when adding a status

Enter response: S// a  ADD STATUS

1 - * (WildCard)

2 - CANCELLED

3 - COM

4 - COMPLETE

5 - EXAMINED

6 - TRANSCRIBED

7 - WAITING FOR EXAM

Select a Radiology Procedure Status or enter '^' to Quit:  (1-7): 2,3,6

Statuses already defined for this finding item:

CANCELLED

COM

COMPLETE

TRANSCRIBED

Select one of the following:

A         ADD STATUS

D         DELETE A STATUS

S         SAVE AND QUIT

Q         QUIT WITHOUT SAVING CHANGES

Enter response: S// ?

View when deleting a status

Enter response: S// d  DELETE A STATUS

1 - CANCELLED

2 - COM

3 - COMPLETE

4 - TRANSCRIBED

Select which status to be deleted:  (1-4): 2,4

Statuses already defined for this finding item:

CANCELLED

COMPLETE

Select one of the following:

A         ADD STATUS

D         DELETE A STATUS

S         SAVE AND QUIT

Q         QUIT WITHOUT SAVING CHANGES

Enter response: S//

**Tip:** Here is a tip that will make it work a little bit faster when you are using a Condition to check the status. The status is checked before the Condition is applied so if your status list does not contain the status you are checking for in the Condition the Condition will never be true. So when you are using a Condition set the status list to the wildcard “*”, this makes the status check faster.

#### Activate/Inactivate Reminders

Use this option to make individual reminders active or inactive.

Select Reminder Definition Management Option: **RA** Activate/Inactivate Reminders

Select REMINDER DEFINITION NAME: **??**

Answer with REMINDER DEFINITION NAME, or REMINDER TYPE, or

PRINT NAME

Choose from:

CHOLESTEROL

LOCAL FOBT

VA-*BREAST CANCER SCREEN

VA-*CERVICAL CANCER SCREEN

VA-*CHOLESTEROL SCREEN (F)

VA-*CHOLESTEROL SCREEN (M)

VA-*COLORECTAL CANCER SCREEN (

VA-*COLORECTAL CANCER SCREEN (

VA-*FITNESS AND EXERCISE SCREE

VA-*HYPERTENSION SCREEN

VA-*INFLUENZA IMMUNIZATION

VA-*PNEUMOCOCCAL VACCINE

VA-*PROBLEM DRINKING SCREEN

Select REMINDER DEFINITION NAME: CHOLESTEROL SCREEN (F)

INACTIVE FLAG: **?**

Enter "1" to inactivate the reminder item.

Choose from:

1        INACTIVE

INACTIVE FLAG: 1

Inactivating a reminder will not remove it from CPRS cover sheet lists or health summaries. However when the cover sheet loads or the health summary is run the reminder will not be evaluated and a message showing the date and time the reminder was inactivated will be displayed.

### Reminder Sponsor Management

This option provides the functions for Reminder Sponsor Management.

| **Syn.**   | **Name**                  | **Option Name**      | **Description**                                         |
|------------|---------------------------|----------------------|---------------------------------------------------------|
| SL         | List Reminder Sponsors    | PXRM SPONSOR LIST    | This option is used to get a list of Reminder Sponsors. |
| SI         | Reminder Sponsor Inquiry  | PXRM SPONSOR INQUIRY | This option is used to do a reminder sponsor inquiry.   |
| SE         | Add/Edit Reminder Sponsor | PXRM SPONSOR EDIT    | The option allows for editing of Reminder Sponsors.     |

#### List Reminder Sponsors

Select Reminder Sponsor Management Option: SL  List Reminder Sponsors

DEVICE:   ANYWHERE    Right Margin: 80//

REMINDER SPONSOR LIST                          JAN 28,2003  10:39    PAGE 1

--------------------------------------------------------------------------------

Name:  A NEW SPONSOR

Class: VISN

Name:  CRPROVIDER,TWO

Class: VISN

Name:  CRPROVIDER,THREE

Class: LOCAL

Name:  Guidelines committee

Class: LOCAL

Name:  HOSPITAL COMMITTEE

Class: LOCAL

Name:  INFECTIOUS DISEASES PROGRAM OFFICE, VAHQ

Class: NATIONAL

Name:  CRPROVIDER,FOUR

Class: NATIONAL

Name:  Mental Health Group

Class: LOCAL

Name:  Mental Health and Behavioral Science Strategic Group

Class: NATIONAL

Name:  Mental Health and Behavioral Science Strategic Group and Women Veterans

Health Program

Class: NATIONAL

Name:  NEW

Class: LOCAL

Name:  Office of Quality &amp; Performance

Class: NATIONAL

Name:  QUERI IHD

Class: NATIONAL

Name:  SLC OIFO DEVELOPMENT

Class: NATIONAL

Name:  Women Veterans Health Program

Class: NATIONAL

#### Reminder Sponsor Inquiry

Select Reminder Sponsor Management Option: SI  Reminder Sponsor Inquiry

Select Reminder Sponsor: ?

Answer with REMINDER SPONSOR NAME, or ASSOCIATED SPONSORS

Do you want the entire REMINDER SPONSOR List? N  (No)

Select Reminder Sponsor: ??

Choose from:

Guidelines committee         LOCAL

HOSPITAL COMMITTEE         LOCAL

INFECTIOUS DISEASES PROGRAM OFFICE, VAHQ         NATIONAL

CRPROVIDER,TEN         NATIONAL

Mental Health Group         LOCAL

Mental Health and Behavioral Science Strategic Group         NATIONAL

Office of Quality &amp; Performance         NATIONAL

QUERI IHD         NATIONAL

SLC OIFO DEVELOPMENT         NATIONAL

Women Veterans Health Program         NATIONAL

Select Reminder Sponsor: Office of Quality &amp; Performance       NATIONAL

DEVICE:   ANYWHERE    Right Margin: 80//

REMINDER SPONSOR INQUIRY                     Jan 28, 2003 10:41:47 am  Page 1

--------------------------------------------------------------------------------

NUMBER: 15

Name:  Office of Quality &amp; Performance

Class: NATIONAL

Associated Sponsors:

Select Reminder Sponsor:

#### Add/Edit Reminder Sponsor

Select Reminder Sponsor Management Option: SE  Enter/Edit Reminder Sponsor

Select Reminder Sponsor:    Office of Quality &amp; Performance     NATIONAL

You cannot edit National Class Sponsors!

Select Reminder Sponsor: A NEW SPONSOR       VISN

NAME: A NEW SPONSOR//

CLASS: VISN//

Select CONTACT:

Select ASSOCIATED SPONSORS:

Select Reminder Sponsor: ?

### Reminder Taxonomy Management

Reminder taxonomies, stored in file #811.2, provide a convenient way to create a set of coded values and give it a name. For example, the VA-DIABETES taxonomy contains a list of ICD diagnosis codes that signify the patient has a diagnosis of diabetes.

**Changes made to Taxonomy Management by Patch 26 (PXRM*2*26)**

***In the past*** , taxonomies were based on pointers to the ICD diagnosis file (#80), the ICD Operation/ Procedure file (#80.1), and the CPT file (#81). Multiple ranges of codes (low code to high code) could be defined for each of these coding systems. When editing was finished, each range of codes was expanded to include all the codes from the low code to the high code. Some coding systems such as SNOMED CT do not assign any meaning to the codes, so they cannot be grouped by code and the concept of a range of codes is meaningless. In some cases, for coding systems that do support the concept of a range, code set updates have inserted an unrelated code into a range.

***New approach:*** For the above reasons, the PXRM*2*26 patch changes taxonomies so that they are Lexicon-based. This is a general approach that allows Clinical Reminders taxonomies to support any coding system defined in Lexicon’s Coding Systems file (#757.03), provided Lexicon maintains the coding system and patient data using the coding system is stored in VistA.

For each coding system it includes, the Coding Systems file defines a three-character abbreviation, nomenclature, source title, and source. Example: ICD, ICD-9-CM, International Classification of Diseases, Diagnosis, 9th Edition, and US Department of Health and Human Services. The three-character abbreviation provides a convenient way to refer to coding systems and is used by Clinical Reminders Taxonomies. The following coding systems are supported by Clinical Reminders:

| Abbreviation   | Nomenclature   |
|----------------|----------------|
| 10D            | ICD-10-CM      |
| 10P            | ICD-10-Proc    |
| CPT            | CPT-4          |
| CPC            | HCPCS          |
| ICD            | ICD-9-CM       |
| ICP            | ICD-9-Proc     |
| SCT            | SNOMED CT      |

**Changes to Reminder Dialogs**

***Before PXRM*2*26*** , users created Reminder Dialogs by adding individual ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog. If the Reminder Dialog was set up to use a Taxonomy, it could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS.

The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter and what prompts should be assigned to the Reminder Dialog in CPRS.

***After PXRM*2*26*** , users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new field named Taxonomy Pick List Display has been added to the dialog data dictionary. This field controls how Taxonomies display in CPRS.

When editing a dialog, a simple taxonomy editor is available. It is accessed from dialog management (either the element or group view). Codes added in this editor are automatically marked as Use In Dialog. If a code is deleted in this editor, the Use In Dialog designation is removed from the code.

See the Dialog Management section (page 234 ) for further explanation of the changes and for examples of using the new Dialog Taxonomy functionality.

#### Reminder Taxonomy Management

A new taxonomy management system replaces the previous taxonomy management menu. The new system uses a combination of List Manager, ScreenMan, and the Browser. List Manager should already be familiar to users of Clinical Reminders tools such as Dialog Management or Reminder Exchange. ScreenMan and the Browser may not be as familiar, but reviewing Appendix A of this manual or the FileMan documentation should give you enough knowledge to make using the taxonomy management system much easier.

**ScreenMan Overview**

ScreenMan is VA FileMan's *screen-oriented* data entry tool. It is an alternative to the Scrolling Mode approach. With ScreenMan, data is entered in *forms* . Each form field occupies a fixed position on the screen (instead of scrolling off!). You can see many data fields at once, and use simple key combinations to edit data and move from field to field on a screen. You can also move from one screen to another like turning through the pages of a book.

If you are not familiar with how to use ScreenMan, see Appendix A of this manual for a brief overview. ***For a detailed explanation of using ScreenMan and the Browser, please refer to the VA FileMan Getting Started manual.***

**Browser Overview**

The Browser lets you view any text *on the screen* instead of *on paper* . Do this by printing your text to the **BROWSER** device instead of the HOME device or a printer.

The Browser makes it very easy to view text on screen. Its main features are:

1. Scroll forwards *and backwards* through the text. This means you don't lose lines of text "off the top" of the screen, like you do when you print to the HOME device.
2. Use the Search feature to find a text string and immediately jump to occurrences of the search string.
3. Copy selected text from to the VA FileMan Clipboard; later, if you're editing a mail message or other WORD-PROCESSING-type field with the Screen Editor, you can paste from the clipboard.

**Shortcuts and Screen setup Tips**

Both the Browser and ScreenMan have shortcuts that can save you a lot of time. Each shortcut begins by pressing the Num Lock (NL) key. (NOTE: some laptops don’t have a NumLock key, so you would need to use Map Keyboard on your Reflections Utility menu to map a terminal key to the PC NumLock key.)

Some Browser actions:

- (NL)B – go to bottom
- (NL)E – exit
- (NL)F – find
- (NL)H – help
- (NL)Q – quit
- (NL)T – go to top

Some ScreenMan shortcuts:

- (NL)C – close a screen
- (NL)E – exit and save changes
- (NL)H – help
- (NL)Q – exit and do not save changes
- (NL)Z – zoom editor

Your Reflections session setup makes a difference in the appearance of the ScreenMan display. The screen element Normal default is a white background and black foreground. Choosing a background color other than white and a foreground color that works well with the background color will provide a more readable ScreenMan display.

<!-- image -->

NOTE: For taxonomy inquiry print to display properly in Reflections, the setup must have Save from Scrolling Regions checked. Sequence is: Setup =&gt; Display =&gt; Screen =&gt; Display Memory Advanced.

<!-- image -->

<!-- image -->

**Reminder Taxonomy Management Main Screen**

When you select Taxonomy Management from the Clinical Reminders Managers Menu, you will go into a List Manager Taxonomy Management screen. It lists all of the taxonomies on your system. You can use the standard List Manager actions to search or scroll through the list.

**Example: Taxonomy Management main screen**

<!-- image -->

#### Reminder Taxonomy Management Actions

| **Synonym**   | **Action**   | **Description**                                                                                                                                                                                |
|---------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD           | Add          | Use this action to create a new taxonomy.                                                                                                                                                      |
| EDIT          | Edit         | Use this action to edit an existing taxonomy.                                                                                                                                                  |
| COPY          | Copy         | This action allows the user to copy an existing taxonomy into a new one. The new taxonomy must have a unique name.                                                                             |
| INQ           | Inquire      | Use this action to obtain a detailed report about a taxonomy. It lists all the codes that have been selected, the code’s status, and shows if the code has been marked as Use In Dialog (UID). |
| CL            | Change Log   | Use this action to display a taxonomy’s change log (edit history).                                                                                                                             |
| CS            | Code Search  | This action can be used to find all taxonomies that include a particular code.                                                                                                                 |
| IMP           | Import       | Use this action to import codes from a CSV file.                                                                                                                                               |
| UIDR          | UID Report   | This action runs the UID report which displays all inactive codes marked as UID.                                                                                                               |

***NOTE – KNOWN ANOMALY:**

For any action that works with a list, you can select the list and then the action, or select the action and then the list. In the first case, the action uses List Manager’s list selection, which returns the list as a string of items. If the list has too many items, it generates a range error.

The workaround is to select the action first.

For example, on the code selection screen, if you do an ICD-10 Lexicon search for diabetes, you will see a list of around 250 codes. If you enter 1-250, you’ll get a range error. However, if you select Add, then you can enter 1-250 and not get the error.

**Lexicon Selection** Nov 14, 2013@11:16:15        Page:   57 of   57

Term/Code: diabetes

253 ICD-10-CM codes were found.

+No. Code      Active     Inactive  Description

Gestational Diabetes

250 P70.2     10/1/2014            Neonatal diabetes mellitus

251 Z13.1     10/1/2014            Encounter for Screening for Diabetes

Mellitus

252 Z83.3     10/1/2014            Family History of Diabetes Mellitus

253 Z86.32    10/1/2014            Personal History of Gestational Diabetes

+ Next Screen   - Prev Screen   ?? More Actions

ADD  Add to taxonomy                    UID  Use in dialog

RFT  Remove from taxonomy               SAVE Save

RFD  Remove from dialog

Select Action: Quit// 1-250

&gt;&gt;&gt;  Range too large: 1-250.

#### Reminder Taxonomy Actions

#### Add

Use this action to add a new taxonomy.

<!-- image -->

When you select Add, you are prompted to enter the Name and Class of the new taxonomy. Once these have been entered you will be taken to the ScreenMan edit form. This is the same form you enter when selecting the Edit action.

Are you adding 'JGTAXONOMY1' as a new REMINDER TAXONOMY (the 148TH)? No// Y

(Yes)

REMINDER TAXONOMY CLASS: LOCAL  LOCAL

#### Edit

Use this action to edit the fields in a taxonomy definition. When you select Edit, a ScreenMan form opens.

<!-- image -->

#### Taxonomy Fields

| **NAME**              | **DESCRIPTION**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME                  | This is the name of the taxonomy. It must be unique. Nationally distributed taxonomies start with “VA-“.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DESCRIPTION           | Use this word-processing field to give a complete description of the taxonomy. Topics to consider including are what the taxonomy represents and its intended usage.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PATIENT DATA SOURCE   | Specifies where to search in VistA for patient data. It is a string of comma-separated key words. The list of key words is given below.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| USE INACTIVE PROBLEMS | Applies only to searches in Problem List. Normally inactive problems are not used. However when this field is set to YES, then both active and inactive problems are used. This field works just like the field with the same name that can be specified for a reminder definition finding or a reminder term finding. If this field is defined in the taxonomy, it will take precedence over the value of the corresponding field at the term or definition level.                                                                                                                            |
| PRIORITY LIST         | This field applies only to Problem List searches. It can be used to limit the problems that are included to those with the listed priorities. The possible values are:  A - acute  C - chronic  U - undefined  Any combination of these letters can be used. For example, 'A' would  limit the search to acute problems. 'CU' would include chronic problems and those whose priority is undefined. If this field is left blank then all priorities will be included.                                                                                                                          |
| INACTIVE FLAG         | Enter "1" to inactivate the taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TERM/CODE (multiple)  | Term/Code and a Coding System are passed to the Lexicon search utility, which returns a list of codes based on the users search criteria. Terms are descriptions for a concept and the code is a unique identifier assigned to that description. A concept can have one or more descriptions to express the concept. An example of this in SNOMED CT is the concept code 271807003 that has a fully specified name of "Eruption of Skin", a preferred name of "Eruption" and several synonyms "Rash", "Skin Eruption", "Skin Rash". For more information, see the Lexicon Utility User Manual. |
| CLASS                 | This is the class of the entry. Entries whose class is National cannot be edited or created by sites.  N - NATIONAL  V - VISN  L -  LOCAL                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SPONSOR               | This is the name of a group or organization that sponsors the taxonomy  *.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MINIMUM VALUE         | MINIMUM VALUE and MAXIMUM VALUE set the inclusive range for the magnitude.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MAXIMUM VALUE         | MINIMUM VALUE and MAXIMUM VALUE set the inclusive range for the magnitude.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MAXIMUM DECIMALS      | The maximum number of decimal digits that can be entered for the magnitude.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| UCUM CODE             | This is the unit for the measurement, it is selected from the Universal Code for                               Units of Measurement (UCUM) file #757.5.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PROMPT CAPTION        | This field stores the prompt that displays in CPRS Reminder Dialogs when the Taxonomy is used as a finding item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| UCUM DISPLAY          | This field specifies how the unit is presented when a measurement is displayed in CPRS, Clinical Reminders, and Health Summary. When the value is C, the UCUM Code is displayed when the value is D, the Description is  displayed. When the value is N, no units are displayed.                                                                                                                                                                                                                                                                                                               |
| REVIEW DATE           | The review date is used to determine when the entry should be reviewed to verify that it is current with the latest standards and guidelines  *.*                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CHANGE LOG            | If changes were made, the date and the name of the user making the changes will be inserted automatically. You can optionally type in a description of the changes made during the editing session.                                                                                                                                                                                                                                                                                                                                                                                            |

#### Patient Data Source Keywords

| **KEYWORD**   | **MEANING**                                               |
|---------------|-----------------------------------------------------------|
| ALL           | All sources (default)                                     |
| EN            | All PCE encounter data (CPT-4 & ICD diagnosis, SNOMED CT) |
| ENPP          | PCE encounter data, principal procedure (CPT-4) only      |
| ENPD          | PCE encounter data, principal diagnosis (ICD) only        |
| IN            | All PTF inpatient data (ICD diagnosis and procedures)     |
| INDXLS        | PTF inpatient DXLS diagnosis (ICD) only                   |
| INM           | PTF inpatient diagnosis (ICD) movement only               |
| INPD          | PTF inpatient principal diagnosis (ICD) only              |
| INPR          | PTF inpatient procedure (ICD) only                        |
| PL            | Problem List (ICD diagnosis and SNOMED-CT)                |
| RA            | Radiology (CPT-4) only                                    |

You may use any combination of these keywords. An example is EN,RA. This would cause the search to be made in V CPT and Radiology for CPT-4 codes. If PATIENT DATA SOURCE is left blank, the search is made in all the possible sources. You can also use a “-” to remove a source from the list; for example, IN,-INM.

It is important to remember that the link between CPT-4 codes and radiology procedures is maintained by sites. If this linkage is not kept current at your site then the recommendation is **do not use RA** in Patient Data Source. It will be much more reliable to use radiology procedures directly as findings.

When you navigate to some of the fields on the form, you may see help in the command area. If more detailed help is needed, type ‘?’ or ‘??’.

Term/Code is a multiple of terms, codes, or code fragments that are used for a Lexicon search. In the above example, the code fragment 250 has been entered. When you press Enter you will be taken to a form where you select the coding system to search.

**Example: Coding System Selection Form**

<!-- image -->

The top line displays the Term/Code that will be used in the search. You can scroll through the list to select a coding system for the search. When the cursor is on a coding system and you press Enter, the Term/Code and the coding system are passed to the Lexicon search engine, which returns a list of matching codes. The codes are displayed in a List Manager screen. At the top it shows you Term/Code and the number of codes found in the selected coding system.

**Example: List Manager Lexicon Selection Screen**

This example shows the results of a search for the Term/Code 250 in the ICD-9-CM coding system. The second line shows the Term/Code and the third line the number of codes found in the selected coding system.

<!-- image -->

At this point, the following actions are available:

| **Synonym**   | **Action**           | **Description**                                                                                                                                    |
|---------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD           | Add to taxonomy      | Adds the selected codes to the taxonomy.                                                                                                           |
| RFT           | Remove from taxonomy | Removes the selected codes from the taxonomy.                                                                                                      |
| RFD           | Remove from dialog   | Removes UID from the selected codes.                                                                                                               |
| UID           | Use in dialog        | Marks the selected codes as Use in Dialog.                                                                                                         |
| SAVE          | Save                 | Saves the results of the other actions. You may do multiple adds, removes, etc., but nothing is actually saved until the Save action is performed. |

**Note:** You may select the action first, then the list of entries it applies to, or the list of entries and then the action. There are a number of ways to specify the selection list.

| Comma separated list of entries   | 1,3,5   |
|-----------------------------------|---------|
| Range of entries                  | 4-8     |
| Combination                       | 3,9-12  |

When you are finished, use the hidden action Quit to return to the coding system selection form. If desired, you can use the same Term/Code for searching another coding system, just move to the next coding system and press Enter. If you want to input another Term/Code then use either shortcut (NL)C (close) or (NL)Q (quit) to exit the coding system selection form and return to the main taxonomy edit form.

To edit some fields, such as Description, you must press Enter, and then a word-processing screen opens:

<!-- image -->

- To exit the word-processing screen, press &lt;PF1&gt;E (or the key you’ve mapped).
- Move down the edit screen by using the down arrow.

#### Copy

Use this action to copy an existing taxonomy definition into a new entry. Once the taxonomy has been copied, you have the option of editing it.

**Example: Copying a taxonomy definition screen**

<!-- image -->

If you choose to edit the taxonomy you’ve copied, you will enter the standard editing form.

**Example: Standard Editing form**

<!-- image -->

<!-- image -->

#### Inquire about Taxonomy Item

Use this action to get the details of a single taxonomy. You may select Condensed or Full.

The condensed displays each code on a single line with a column for code, inactive, UID, and the first 47 characters of the description.

You will also have the option of browsing the output or choosing an output device.

<!-- image -->

**Examples: Browsing Taxonomy Inquiry**

<!-- image -->

<!-- image -->

Example: Browsing Taxonomy Inquiry – Condensed

<!-- image -->

<!-- image -->

**Example: Browsing Taxonomy Inquiry - Full**

#### Change Log

Use this action to see the historical details of a taxonomy; i.e., who created, edited, or copied it, and when. You will have the option of browsing the output or choosing an output device:

Browse or Print? B//

**Example: Browsing Taxonomy Change Log**

<!-- image -->

<!-- image -->

#### Code Search

This lets you find all taxonomies that contain a selected code. When you select this action, you are prompted to input a code from any of the supported coding systems. You only need to enter the code; the coding system will be automatically determined.

**Example: Selecting Code Search screen**

<!-- image -->

<!-- image -->

Example: Code Search Results

#### Import

The Import action provides an easy way to import lists of codes into a taxonomy.

A CSV file (Comma Separated Values) is created from a spreadsheet. The first column is equivalent to the Term/Code, the second column is the three-character coding system abbreviation for one of the supported coding systems, and the rest of the columns are the codes to be imported for the Term/Code, coding system pair. The spreadsheet can have multiple rows, a row for each Term/Code, coding system, set of codes to be imported. The final step is to create a CSV file (comma-delimited text file), using the Save As action.

**NOTE:** The National Library of Medicine (NLM), in collaboration with the Office of the National Coordinator for Health Information Technology and the Centers for Medicare &amp; Medicaid Services has created a Value Set Authority Center (https://vsac.nlm.nih.gov/). These value sets contain lists of terms and their codes and they can be useful for creating taxonomies.

The Import action facilitates their use by allowing import of the codes into a taxonomy. To prepare the data for import, the original spreadsheet should be copied into a new spreadsheet that can be edited.

**Example Spreadsheet**

<!-- image -->

When the Import action is selected, you will be prompted to select a taxonomy to import into, and after it has been selected, you have the following choices:

<!-- image -->

**Import: CSV Host File**

If the CSV file has been saved as a host file, choose the HF option. You will then be prompted for a path. This is the directory/folder that contains the CSV file and it must be accessible from your VistA session. A list of all files with a ‘.CSV’ extension in that directory will be displayed; enter the file name at the prompt, (you do not need to include the .csv extension).

**NOTE:** Special privileges are required to access host file directories, so you may not be able to use this option.

**Example: Importing codes from a CSV host file**

<!-- image -->

#### At this point you will have the option of browsing the list of codes.

**Example: Browsing list of codes screen**

<!-- image -->

<!-- image -->

<!-- image -->

If you are satisfied, then when the Browser is exited, respond yes to this prompt:

**Do you want to save the imported codes? Y//**

If there are problems with any of the codes, error messages will be displayed.

When the codes are imported into the taxonomy, each Term/Code will have “(imported)” appended to it so that you will know the codes were imported.

**Import: CSV Paste**

Another way to import a CSV file is the PA option. When you use this option, you open the CSV file on your workstation and copy it.

1. Create an Excel Spreadsheet. The first column of the new spreadsheet is equivalent to the Term/Code, the second column is the three-character coding system abbreviation for one of the supported coding systems, and the rest of the columns are the codes to be imported for the Term/Code, coding system pair. The spreadsheet can have multiple rows, a row for each Term/Code, coding system, set of codes to be imported. The final step is to create a CSV file (comma-delimited text file), using the Save As action.

<!-- image -->

1. Save the imported files as a CSV.
2. Open the CSV file, as a text file, using a text editor such as Notepad or Microsoft Word. (Select All Files in the Files of type box.)

<!-- image -->

1. Open the desired CSV file and copy the contents so they are ready for pasting.

<!-- image -->

1. In Taxonomy Management, select the action IMP and press enter.
2. At the prompt, enter the number of the Taxonomy that the import file will be imported to.

<!-- image -->

1. Select PA for the import method.

<!-- image -->

1. At the 'Paste the CSV file now prompt, click on Paste from the file menu (or select the Paste icon) and press &lt;enter&gt; to finish.

<!-- image -->

1. Next you will be given the opportunity to browse the list of codes that will be imported. If you are satisfied with the list, respond ‘Y’ to the following prompt to import the codes:

<!-- image -->

1. After browsing, you’ll be asked if you want to save the codes.

**Do you want to save the imported codes? Y//**

1. You can also do an inquiry on the taxonomy you imported the codes into, to verify that these have been entered.

**+         + Next Screen   - Prev Screen   ?? More Actions**

**ADD  Add                                CS   Code Search**

**EDIT Edit                               IMP  Import**

**COPY Copy                               UIDR UID report**

**INQ  Inquire                            OINQ Old Inquire**

**CL   Change Log**

**Select Action: Next Screen// inq   Inquire**

**Display inquiry for which taxonomy?:  (1-254): 105**

<!-- image -->

.

**Import – TAX**

If you choose the TAX option then you will be presented with a list of all the taxonomies on the system and you can create a list of taxonomies to import codes from.

<!-- image -->

<!-- image -->

The SEL action adds a taxonomy to the list and the REM action removes it from the list. Once the list is built use the DONE action. You will then see the following prompt for each selected taxonomy:

**Ready to import codes from taxonomy (taxonomy name here)**

**Select one of the following:**

**ALL       All codes**

**SEL       Selected codes**

**Enter response: ALL//**

ALL will import all the codes and SEL will walk you through each Term/Coding System combination in the taxonomy and allow you to choose whether or not to import it.

**Importing a CSV file from a web site**

<!-- image -->

Hint - If you have the URL copied to the clipboard you can paste it at the Input prompt.

<!-- image -->

<!-- image -->

#### Use in Dialog Report (UIDR)

The Use in Dialog Report option searches all taxonomies for inactive codes that are marked as Use in Dialog. If any of these are found, a Browser window displays the taxonomies and information about the inactive code(s) they contain.

Select UIDR from the Taxonomy Selection screen:

<!-- image -->

**Once the report is built a Browser screen will open displaying the report.**

**Example: Browsing Use in Dialog Report**

<!-- image -->

#### Code Set Versioning

The Health Insurance Portability and Accessibility Act (HIPAA) stipulates that specific code sets used for billing purposes must be versioned based on the date of service. Those code sets must be applicable at the time the service is provided. Clinical Reminders was required to make changes to ensure that users would be able to select codes based upon a date that an event occurred with the Standards Development Organization (SDO)-established specific code and translation that existed on an event date.

Because of this, when reminder dialogs are processed the user can only select codes that are active on the encounter date. For historical entries the user may select a code that is currently inactive, but was active on the date of the historical encounter. In practical terms, this means that you may want to leave codes that have been recently inactivated marked as Use in Dialog (UID), but remove UID from codes that were inactivated some time ago.

Taxonomies are another matter; even though a code has been inactivated, it probably should still be left in the taxonomy, because you will still want to be able to find any patients that were given the code in the past when it was active.

When Lexicon code set updates are installed it triggers the generation of reports which are sent to the Clinical Reminders mail group defined in file #800. In the past, the content of these reports was based upon the use of expansion in taxonomies and the use of individual codes as findings or additional findings in reminder dialogs. Since expansion is no longer used and individual codes are no longer used in dialogs the content has changed and is much simpler. Now, it is very similar to the Use in Dialog Report and lists codes which are marked as Use in Dialog but are now inactive. When you receive the messages, review them to see what action should be taken, if any.

Example : Code Set Update Message

Subj: Clinical Reminder taxonomy updates, ICD global was updated.  [#95437]

11/27/12@15:32  159 lines

From: XXXXX,YYY (Yyy Xxxxxxx)  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

There was an ICD code set update on 11/27/2012@15:32:39.

The following taxonomies contain the listed inactive codes which are marked as

Use in Dialog:

Taxonomy: AGP HYPERTENSION TEST (IEN=219)

Coding system: ICD-9-CM

Code       Inactivation  Brief Description

---------  ------------  -----------------

404.1      10/01/1989    BEN HYPERT HRT/RENAL DIS

Taxonomy: AWAT CPT AND POV (IEN=660013)

Coding system: ICD-9-CM

Code       Inactivation  Brief Description

---------  ------------  -----------------

008.61     01/01/2012    ROTAVIRUS

Taxonomy: BREAST TUMOR (IEN=500011)

Coding system: ICD-9-CM

Code       Inactivation  Brief Description

---------  ------------  -----------------

793.8      10/01/2001    ABNORMAL FINDINGS-BREAST

Taxonomy: DEPRESSION OTHER THAN MDD (IEN=500033)

Coding system: ICD-9-CM

Code       Inactivation  Brief Description

---------  ------------  -----------------

291.8      10/01/1996    ALCOHOLIC PSYCHOSIS NEC

292.21     10/01/1979    DEMENTIA ASSOC W/ETOH, MILD

294.1      10/01/2000    DEMENTIA IN OTH DISEASES

Taxonomy: HF INJECTION OTHER (IEN=200)

Coding system: CPT-4

Code       Inactivation  Brief Description

---------  ------------  -----------------

90772      01/01/2009    THER/PROPH/DIAG INJ, SC/IM

Please review the affected taxonomies and take appropriate action

Enter message action (in IN basket): Ignore//

### Value Sets

The National Library of Medicine has a Value Set Authority Center (VSAC) web site, where value sets can be obtained. From the web site: “Value sets are lists of specific values (terms and their codes) derived from single or multiple standard vocabularies used to define clinical concepts (e.g. patients with diabetes, clinical visit, reportable diseases) used in quality measures and to support effective health information exchange.” These value sets cover many clinical areas of relevance to the VA and since they are very similar to taxonomies they can be used to automatically generate taxonomies.

To introduce value set functionality into VistA, patch PXRM*2*47 added the following files:

NLM QUALITY MEASURE GROUPS (file #802.3),

NLM VALUE SET CODING SYSTEMS (file #802.1),

NLM VALUE SETS (file #802.2).

And on the PXRM MANAGERS MENU it added an option for Value Sets:

Select OPTION NAME: PXRM MANAGERS MENU       Reminder Managers Menu

CF     Reminder Computed Finding Management ...

RM     Reminder Definition Management ...

SM     Reminder Sponsor Management ...

TXM    Reminder Taxonomy Management

TRM    Reminder Term Management ...

LM     Reminder Location List Management ...

RX     Reminder Exchange

RT     Reminder Test

OS     Other Supporting Menus ...

INFO   Reminder Information Only Menu ...

DM     Reminder Dialog Management ...

CP     CPRS Reminder Configuration ...

RP     Reminder Reports ...

MST    Reminders MST Synchronization Management ...

PL     Reminder Patient List Menu ...

PAR    Reminder Parameters ...

ROC    Reminder Order Check Menu ...

XM     Reminder Extract Menu ...

VS     NLM Value Set Menu

CQM    NLM Clinical Quality Measures Menu

GEC    GEC Referral Report

When the VS option is selected it opens a List Manager screen:

<!-- image -->

The List Manger screen lists all the value sets contained in the NLM Value Set file. Since it is List Manager, all the standard List Manager actions such as SL (search list) are available. In addition to the standard List Manager actions, there are these actions:

Create Taxonomy

This action will automatically generate a new taxonomy from a value set. Some value sets contain coding systems that are not supported in taxonomies so when a taxonomy is generated, these coding systems will not be included. When you select the CT action you are prompted for the value set, after it has been selected the value set is scanned for coding systems that can be imported into the taxonomy, they are listed. The default name for the new taxonomy is the name of the value set; you are given the opportunity to change it. The taxonomy is then created and the code list is populated. The description of the taxonomy will be populated with text stating it was automatically generated from a value set.

<!-- image -->

Inquire

This action will display the contents of the selected value set. You have the option of a condensed or full inquiry. Both list all the codes in the value set, but in the condensed only the first 57 characters of the code description are shown while the full inquiry lists the entire description. All the clinical quality measures that use the value set are listed at the end of the inquiry. In the condensed inquiry, only the name of the quality measures is displayed. In the full inquiry, comprehensive information about the quality measures is listed include its name, CMS ID, version number, GUID, NQF number, steward, and description.

Code Search

This action allows you to select from a list of NLM Value Set Coding Systems then input a code from that coding system and it returns a list of all the value sets that contain that code.

In addition to these explicit actions, the standard set of List Manager actions is available, you can see the list by typing “??”. Initially the help for the visible actions is displayed in a FileMan Browser screen, after exiting that screen the hidden action help is displayed. Probably the three most useful actions are:

FS – First Screen

LS – Last Screen

SL – Search List; this is a non-case sensitive search of the text in the List Manager display. It is a convenient way to find value sets that have specified text in their name. You can find all the values sets that contain “mumps” in their name by typing “mumps” at the “Search for:” prompt.

### Reminder Term Management

A reminder term provides a way to group findings under a single name, just as a taxonomy lets you group a set of codes under a single name. Each term has a findings multiple that is just like the findings multiple in the reminder definition. When you add findings to this multiple, we call it “mapping” the term. All the findings that are mapped to the term should represent the same concept. The list of possible findings in a term is the same as in a definition, except that a term cannot have another term as a finding.

When a term is evaluated, the entire list of findings is evaluated and the most recent finding is used for the value of the term. If the most recent finding is false (which could happen as a result of a Condition), then the term is false.

A term’s Class can be:

National (N)

VISN (V)

Local (L)

These options are necessary for national guidelines/reporting. The Reminder Term functionality allows you to map local or VISN-level findings to national terms.

#### Reminder Term Management Options

| Synonym   | Option                             | Option Name                   | Description                                                                                                                                                                 |
|-----------|------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TL        | List Reminder Terms                | PXRM TERM LIST                | This option allows a user to display a list of reminder terms that have been defined.                                                                                       |
| TI        | Inquire about Reminder Term        | PXRM TERM INQUIRY             | This option allows a user to display the contents of a reminder term in an easy-to-read format.                                                                             |
| TE        | Add/ Edit Reminder Term            | PXRM TERM EDIT                | This option is used to edit reminder terms.  NOTE: Name the reminder terms using all capital letters because the names are case- sensitive.                                 |
| TC        | Copy Reminder Term                 | PXRM TERM COPY                | This option allows a user to copy an existing reminder term into a new one. The new term must have a unique name.                                                           |
| TICS      | Integrity check of a selected term | PXRM TERM INTEGRITY CHECK ONE | This option lets the user select a reminder term for integrity checking.                                                                                                    |
| TICA      | Integrity check of all terms       | PXRM TERM INTEGRITY CHECK ALL | This option runs the integrity check for all reminder terms on the system.                                                                                                  |
| TEST      | TERM TEST                          | PXRM TERM TESTER              | This option allows a user to test a reminder term against a patient. The option returns a true/false value. If the term is true the option also writes out the FIEVAL array |

#### List Reminder Terms

This option is used to give a brief listing of reminder terms.

Select Reminder Term Management Option: TL  List Reminder Terms

DEVICE:   ANYWHERE    Right Margin: 80//

REMINDER TERM LIST                             SEP 16,2003  14:17    PAGE 1

-------------------------------------------------------------------------------

ACUTE MEDICAL CONDITION

Class:         NATIONAL

Date Created:

Sponsor:

Review Date:

Description:   Screening for depression may not be possible in patients

with acute medical conditions.  This term represents any

data element that is used to indicate that the patient has

an acute medical condition that prevents screening for

depression.  E.g. delirium, alcohol hallucinosis, florid

psychosis, MI's and other medical emergencies.

Findings:      UNABLE TO SCREEN-ACUTE MED CONDITION (FI(1)=HF(107))

AIM EVALUATION NEGATIVE

Class:         NATIONAL

Date Created:

Sponsor:

Review Date:

Description:   Represents any AIM evaluation that is negative or normal.

Findings:      AIMS (FI(2)=MH(234))

AIM EVALUATION POSITIVE

Class:         NATIONAL

Date Created:

Sponsor:

Review Date:

Description:   Represents any AIM evaluation that is positive or scored

above the cutoff defined as abnormal.  (AIMS greater than

or equal to 7)

Findings:      AIMS (FI(2)=MH(234))

ALANINE AMINO (ALT) (SGPT)

Class:         NATIONAL

Date Created:  MAY 21,2000

Sponsor:       INFECTIOUS DISEASES PROGRAM OFFICE, VAHQ

Review Date:

Description:   This term represents serum glutamic-pyruvic transaminase

or ALT laboratory tests. Enter the finding items from the

Laboratory Test file (#60) that represent the SGPT test.

National terms related to this term.

WKLD CODE file (#64): The national lab test term is

Transferase Alanine Amino  SGPT.

CPT File (#81) procedure:

CPT code: 84460    SHORT NAME: ALANINE AMINO (ALT) (SGPT)

CPT CATEGORY: CHEMISTRY               SOURCE: CPT

EFFECTIVE DATE: JUN 01, 1994          STATUS: ACTIVE

*List Reminder Terms, cont’d*

DESCRIPTION: TRANSFERASE;

DESCRIPTION: ALANINE AMINO (ALT) (SGPT)

Lexicon: The CPT code is in the Lexicon term as a

Laboratory Procedure term.

Findings:

ANTIDEPRESSANT MEDICATIONS

Class:         NATIONAL

Date Created:  DEC 28,2000

Sponsor:

Review Date:

Description:

Findings:      CN600 (FI(1)=DC(86))

CN609 (FI(2)=DC(395))

CN602 (FI(3)=DC(88))

CN601 (FI(4)=DC(87))

BUSPIRONE (FI(5)=DG(1165))

#### Inquire about Reminder Term

This option lets you display the contents of a reminder term in an easy-to-read format.

Select Reminder Term Management Option: TI  Inquire about Reminder Term

Select Reminder Term:    IHD DIAGNOSIS     NATIONAL

...OK? Yes//   (Yes)

DEVICE:   ANYWHERE    Right Margin: 80//

REMINDER TERM INQUIRY                        Jul 03, 2003 11:06:58 am  Page 1

--------------------------------------------------------------------------------

IHD DIAGNOSIS                                                  No.27

----------------------------------------------------------------------------

Class:                  NATIONAL

Sponsor:                Office of Quality &amp; Performance

Date Created:           JUL 23,2001

Review Date:

Description:

This term represents patients diagnosed with Ischemic Heart Disease

(IHD).

This term is distributed pre-mapped to the VA-ISCHEMIC HEART DISEASE

taxonomy. The Active Problem list, Inpatient Primary Diagnosis and

Outpatient Encounter Diagnosis are used to search for IHD ICD9 diagnoses.

Edit History:

Edit Date: JAN 18,2002  16:03       Edit By: CRPROVIDER,ONE

Edit Comments:  Exchange Install

Findings:

Finding Item:  VA-ISCHEMIC HEART DISEASE  (FI(1)=TX(14))

Finding Type:  REMINDER TAXONOMY

Use Inactive Problems:  NO

#### Add/Edit Reminder Term

You can edit terms or add new ones with this option. If the term is National, you can enter new Findings Items, but can't edit other fields. You can edit any fields for VISN or Local terms.

**NOTE:** Dates, Conditions, and other data entered for Reminder Terms take precedence over the same data entered in Reminder Definitions.

Give the field USE STATUS/COND IN SEARCH a value of "YES" if you want the STATUS LIST and/or CONDITION applied to each result found in the date range for this finding. Only results that have a status on the list or for which the CONDITION is true will be retained. The maximum number to retain is specified by the OCCURRENCE COUNT.

If the finding has both a STATUS LIST and a CONDITION, the status check will be made first; the CONDITION will be applied only if the finding passes the status check.

<!-- image -->

##### Reminder Term Edit Example

**NOTE** : In most cases, a finding modifier on a term takes precedence over the modifier in the definition. An exception to this is the Occurrence Count. The reason for this can be understood by looking at an example. Let’s say a term has been mapped to three findings with an Occurrence Count of 1 for finding 1, 2 for finding 2, and 3 for finding 3. If the maximum number of occurrences is found for each finding, then how do you determine how many occurrences to display? In this case, we would have 6 occurrences, so we have the possibility of displaying anywhere between 1 and 6 of them. The solution is to display the number of occurrences specified at the definition level.

#### Copy Reminder Term

This option lets you copy an existing reminder term into a new one. The new term must have a unique name.

Select Reminder Term Management Option: **TC** Copy Reminder Term
Select the reminder term to copy: **EDUTERM** Reminder term to copy: EDUTERM
         ...OK? Yes// **&lt;Enter&gt;** (Yes)
PLEASE ENTER A UNIQUE NAME: **SLC EDUTERM** The original reminder term EDUTERM has been copied into SLC EDUTERM.
Do you want to edit it now? **YES** NAME: SLC EDUTERM// **&lt;Enter&gt;** .

If you choose to edit the copied term, the sequence of prompts is the same as those shown under Reminder Term Edit, shown in the Reminder Term Edit Example screenshot above.

#### Integrity Check Selected

This option lets you select a term for integrity checking.

Select Reminder Term: ANNUAL HEALTH HABITS SCREEN       LOCAL

...OK? Yes//   (Yes)

No fatal term errors were found.

#### Integrity Check All

This option performs an integrity check on all terms in the account.

Select Reminder Term Management &lt;TEST ACCOUNT&gt; Option: TICA  Integrity Check All

Check the integrity of all reminder terms.

DEVICE: HOME//;;999

…

Checking VA-BL DEPRESSION SCREENING (IEN=797)

No fatal term errors were found.

Checking VA-BL ECOE ALCOHOL USE SCREEN (IEN=491)

FATAL: Term finding number 1 uses computed finding VA-REMINDER DEFINITION. The

Computed Finding Parameter is set to ENTER DEFINITION HERE, that reminder does

not exist.

The term is VA-BL ECOE ALCOHOL USE SCREEN (491).

This term has fatal errors and it will not work!

Checking VA-BL ECOE DEPRESSION SCREEN (IEN=488)

FATAL: Term finding number 1 uses computed finding VA-REMINDER DEFINITION. The

Computed Finding Parameter is set to ENTER DEFINITION HERE, that reminder does

not exist.

The term is VA-BL ECOE DEPRESSION SCREEN (488).

This term has fatal errors and it will not work!

Checking VA-BL ECOE OEF/OIF (IEN=490)

No fatal term errors were found.

…

#### Term Test

This option lets you copy an existing reminder term into a new one. The new term must have a unique name.

Select Reminder Term Management &lt;TEST ACCOUNT&gt; Option: TEST  Term Test

Select Patient: ZZZRETSIXEIGHT,PATIENT        4-7-35    666512345

NSC VETERAN             SMB     SMB

Select Reminder Term:    COVID-19 VACCINE BOOSTER - UNDERLYING CONDITIONS     LO

CAL

...OK? Yes//   (Yes)

The term is False

FIEVAL:

FIEVAL(1)=0

### Reminder Location List Management

Location Lists provide a way to give a name to a list of locations just as a Taxonomy provides a way to give a name to a list of codes.

When a Location List finding is evaluated, a search is made for a Visit (an entry in the Visit file #9000010) at one of the locations on the list in the specified date range (BEGINNING DATE/TIME, ENDING DATE/TIME).

A Location List is built from two types of entries: Hospital Location, file #44 and Clinic Stop, file #40.7. There is a multiple for Hospital Locations and a multiple for Clinic Stops in the Location List file, so when you build a list of locations, you can use Hospital Locations and/or Clinic Stops.

Clinic Stops are ultimately resolvable to a list of Hospital Locations, so when the search is done, it is all based on the Hospital Location recorded for the Visit. There is a CREDIT STOP (field #2503) associated with each Hospital Location. If there are certain Credit Stops that you want to exclude from the list of Hospital Locations associated with a Clinic Stop, then you put these in the CREDIT STOP TO EXCLUDE multiple for each Clinic Stop in the Location List. A Location List of Credit Stops to exclude can also be used; it is entered in the field, CREDIT STOPS TO EXCLUDE (LIST). Location with no credit stop can be excluded by setting EXCL LOCS WITH NO CREDIT STOP to YES.

**Examples:**

a) A Location List for primary care clinics can be created that searches for clinics with stop code 323 and excludes any 323 clinic associated with credit stop 710 (Flu shot only).

b) A Location List for Cardiology clinics can be created that searches for clinics with stop code 303 and excludes any 303 clinic associated with credit stop 450 (used for a clinic dedicated to compensation and pension examination).

#### National Location Lists

National Content is released on a frequent basis. These releases can update existing reminder content or add new reminder content. The NAME for all national location lists starts with VA- and the CLASS is NATIONAL. Those two requirements make it easy to locate national location lists.

Reminder Location List Menu

This menu provides options for creating and editing Reminder Location Lists.

| **Syn.**   | **Name**               | **Option Name**            | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------|------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LL         | List Location Lists    | PXRM LOCATION LIST LIST    | This option is used to get a list of Location Lists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LI         | Location List Inquiry  | PXRM LOCATION LIST INQUIRY | This option is used to inquire about a Location List’s details.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| LE         | Add/Edit Location List | PXRM LOCATION LIST EDIT    | This option allows creation and editing of Location Lists                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| LC         | Copy Location List     | PXRM LOCATION LIST COPY    | This option allows the user to copy an existing location list into a new location list; file #810.9.  The original location list to be copied is selected first. The new name must be unique.  If the new name is not unique, the user must enter a unique name for the new location list entry.  If no name is provided, the new entry will not be created.  Once a new  name is defined for the new location list entry, the new location list entry can be edited to reflect the local location list definition. |

#### List Location Lists

This option is used to produce a list of Location Lists.

#### Location List Inquiry

This option is used to inquire about location lists.

#### Add/Edit Location List

Select Reminder Location List Management Option: le  Add/Edit Location List

Select Location List: **TEST** LOCATION LIST       LOCAL

NAME: TEST LOCATION LIST// **&lt;Enter&gt;**

CLASS: LOCAL// &lt;Enter&gt;

DESCRIPTION:

1&gt;test list

EDIT? No//: **&lt;Enter&gt;**

Select CLINIC STOP: CARDIOLOGY// **&lt;Enter&gt;**

Select CREDIT STOP TO EXCLUDE: ALCOHOL SCREENING

// **&lt;Enter&gt;**

Select CLINIC STOP: **&lt;Enter&gt;**

Select HOSPITAL LOCATION: OR 1// **&lt;Enter&gt;**

Select Location List: &lt;Enter&gt;

#### Create a new Location List

Use Add/Edit Location List to create a new list.

Select Reminder Location List Management Option: **le** Add/Edit Location List

Select Location List: **jg-list**

Are you adding 'jg-list' as a new REMINDER LOCATION LIST (the 6TH)? No// **y**

(Yes)

REMINDER LOCATION LIST CLASS: **l** LOCAL

NAME: jg-list// **&lt;Enter&gt;**

CLASS: LOCAL// &lt;Enter&gt;

DESCRIPTION:

No existing text

Edit? NO// **&lt;Enter&gt;**

Select CLINIC STOP: ?

You may enter a new CLINIC STOP LIST, if you wish

Enter a clinic stop code

Answer with CLINIC STOP NAME, or AMIS REPORTING STOP CODE

Do you want the entire 405-Entry CLINIC STOP List

^

Select CLINIC STOP: **alcohol sc** REENING       706

Are you adding 'ALCOHOL SCREENING' as

a new CLINIC STOP LIST (the 1ST for this REMINDER LOCATION LIST)? No// **y**

(Yes)

Select CREDIT STOP TO EXCLUDE: **&lt;Enter&gt;**

Select CLINIC STOP: **alcohol tr**

1   ALCOHOL TREATMENT       81

2   ALCOHOL TREATMENT-GROUP       556

3   ALCOHOL TREATMENT-INDIVIDUAL       508

CHOOSE 1-3: **1** ALCOHOL TREATMENT     81

Are you adding 'ALCOHOL TREATMENT' as

a new CLINIC STOP LIST (the 2ND for this REMINDER LOCATION LIST)? No// **y**

(Yes)

Select CREDIT STOP TO EXCLUDE: **&lt;Enter&gt;**

Select CLINIC STOP: **&lt;Enter&gt;**

Select HOSPITAL LOCATION: ?

You may enter a new HOSPITAL LOCATION LIST, if you wish

Enter a hospital location

Answer with HOSPITAL LOCATION NAME, or ABBREVIATION, or

STOP CODE NUMBER, or CREDIT STOP CODE, or TEAM

Do you want the entire 50-Entry HOSPITAL LOCATION List? **NO**

Select HOSPITAL LOCATION: 8w SUBSTANCE ABUSE

Are you adding '8W SUBSTANCE ABUSE' as

a new HOSPITAL LOCATION LIST (the 1ST for this REMINDER LOCATION LIST)? No// **y** (Yes)

Select HOSPITAL LOCATION: **&lt;Enter&gt;**

#### Copy Location List

Select Reminder Location List Management Option: LC  Copy Location List

Select the reminder location list to copy: CR-LOCATION LIST NEXUS MENTAL HEALTH

CLINICS       LOCAL

PLEASE ENTER A UNIQUE NAME: NEXUS MENTAL HEALTH CLINICS

The original location list CR-LOCATION LIST NEXUS MENTAL HEALTH CLINICS has been

copied into NEXUS MENTAL HEALTH CLINICS.

Do you want to edit it now? YES

NAME: NEXUS MENTAL HEALTH CLINICS  Replace

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

DESCRIPTION:

This location list are the NEXUS Mental Health Clinics.  This list does

not include the original 11 clinics (actually 13) used for EPRP.

Edit? NO//

Select CLINIC STOP: PTSD DAY TREATMENT//

CLINIC STOP: PTSD DAY TREATMENT//

Select CREDIT STOP TO EXCLUDE:

Select CLINIC STOP:

Select HOSPITAL LOCATION:

### Reminder Exchange

The Clinical Reminders Exchange Utility provides a mechanism for sharing reminder definitions and dialogs among sites throughout the VA or among sites within a VISN. It provides the mechanism for distributing national reminder content and eliminates the need for a patch. Exchanging reminders helps to simplify reminder and dialog creation. It also helps to promote standardization of reminders based on local, VISN-wide, and national guidelines.

An effective way to use the Exchange Utility is through VISN web sites. You can put a set of “packed reminders” into a host file, and the host file can be posted on a web site for download.

**NOTE** : Some of the Reminder Exchange options require programmer access (@).

Reminder Exchange allows the exchange of clinical reminders and reminder dialogs from test account to production, between sites, and within VISNs.

**Changes made with PXRM*2.0*80**

This modified Clinical Reminder Exchange functionality to not automatically packed up a reminder dialog under the following condition. If the dialog is attached to a Reminder Definition and that Reminder Definition is used in another Clinical Reminder component such as: Reminder Dialog Branching Logic, Reminder Order Check Rules, Reminder List Rules, or in a Reminder Definition or Reminder Term using the Computed Finding VA-REMINDER DEFINITION.

**Changes made with PXRM*2.0*45**

- Reminder Exchange will now write a string of dots, instead of the reminder component name when installing the component.
    - Reminder Exchange will only display a component if a user needs to take an action on the component.
- Reminder Exchange will remember the user selection for replacing a finding item not included in the Reminder Exchange file entry and automatically use the replacement selection again if the same finding item is used in other reminder components in the Reminder Exchange file entry.
- Repack options allows the Reminder Manager to repack an existing Reminder Exchange file without having to re-select all the selection items again.
- Reminder Exchange re-order the Reminder Components Install Order to prevent the user having to re-install Reminder Dialog Definitions multiple times
- Reminder Exchange will auto-convert Reminder Dialogs that contain branching logic to the new structure if the dialog was packed up before PXRM*2.0*45

**Changes made by patch 26**

- Automatic packing of the source reminder for a dialog was removed.

- Finding lookup in Reminder Exchange was enhanced to handle mnemonic indexes. An example is the Laboratory Test file #60's Synonym field in the 'B' index. If two entries had the same Synonym and the .01 of one of the entries was identical to the Synonym, the lookup would fail and a duplicate warning message was issued. The code was changed to examine all the entries in the 'B' index and compare the .01 for each of them with the name Exchange is trying to find. If there is a single exact match of the name and a .01, the name is resolved and no duplicate warning will be given. If more than one .01 is identical to the name, the warning will still be given. Remedy ticket #783078.

- The selection range for the Reminder Exchange actions CHF, CMM, DFE, and IFE was changed so that it includes all Reminder Exchange file entries, not just those that are visible.

- For some entries in the Reminder Exchange file displaying installation history details for the first install was giving the following undefined error:

&lt;UNDEFINED&gt;DDISP+31^PXRMEXIH ^PXD(811.8,29,130,1,1,"B",0)

This happened for old entries for which the 'B' index on the Component List was never cleaned up. The unused indexes are removed.

- Reminder Exchange was updated to handle dialogs that were packed prior to patch 26. If the dialog contains codes, Reminder Exchange will create a new taxonomy when the dialog is installed. It will also replace the codes in the dialog with the new taxonomy. If the dialog contains a taxonomy, Reminder Exchange will update the new fields in the dialog file with the values from the installing site’s Finding Parameters File. Because of these changes, the checksum of the installed dialog will always be different than the checksum of what is in the Reminder Exchange file.

- In the past, we have encountered problems, especially with Reminder Exchange, caused by using the tilde (~) character in the name of a reminder component. Reminder Exchange was modified to be able to handle the problem, but to prevent unforeseen problems from happening in the future, the input transform used for all the Clinical Reminders .01 fields was modified to not allow “~”.

NOTE: If you think that “~” may have been used in the.01 of a reminder component at your site, you can use FileMan to find any such entries. There are two possible approaches. One is to use the verify fields function on the FileMan utilities menu and the other is to use the search function to search for any .01 fields that contain “~”.

- The ability to load a Reminder Exchange prd file from a web site has been added. This can be used in conjunction with the Import from a Web site feature in Taxonomy Management. SharePoint sites cannot be used because that requires the user’s Windows credentials and they are not available in VistA.

#### Terminology

**Packing:** When you create an Exchange file entry, you select one or more reminder component entries for packing. The packing process consists of going through the selected entries and building a list of everything they need to function. The entire list of items is included in the Exchange file entry. For example, if a reminder definition is being packed everything the definition needs to function is included.

Some of the included components may not be transportable for various reasons such as being standardized, they will be included in the Exchange file entry so that we know they are used but they will not be installable.

**Reminder Exchange file (#811.8):** Stores entries of packed reminders and dialogs with their components

Packed reminders can be exchanged through VistA MailMan or as a Host file. The default host file extension is .PRD (Packed Reminder Definition).

**VistA MailMan** : Allows users to send the packed reminder via a VistA mail message. When sites are collaborating on development of new reminders and dialogs, messages containing reminders, dialogs, or other reminder components may be sent between sites for loading into the Clinical Reminders Exchange file (#811.8).

**Host File:** Often the domains for MailMan transmission for test accounts are closed. In this case, a host file is used to transport the packed reminders. When a host file is created, it is initially stored on the MUMPS server. (Host file is the terminology used in Kernel.) Typically, you would generate a host file for use on a web site. The Host File will have to be moved from the MUMPS server to the web server. Once it is on the web server, it can be downloaded the LWH action.

##### Technical Overview

In the Reminder Exchange utility, entries are packed into the Exchange file (#811.8) in XML format. Host file or MailMan messages can then be created from the Exchange file for distribution to other sites. Each host file or MailMan message may contain several packed entries. When the receiving site loads a host file or MailMan message into its Exchange file, all the packed entries in the host file or MailMan message are put into the Exchange file. Different versions of the same packed entry may be stored in the Exchange file. They are differentiated by the Date Packed.

All the components used in the item selected for packing are included. Whenever an installation is done, a history of the installation details is retained in the Exchange file.

Reminder dialogs are installed with the disabled field set to “DISABLED IN REMINDER EXCHANGE.” (When you edit the dialog, one of the fields is DISABLE. If this field contains any text, then the dialog is disabled. To enable it, delete the text.)

Steps to Use Reminder Exchange

**Summary of Steps**

Detailed steps are provided in the following pages.

**Export Steps**

| **Step**                          | **Action**                                                |
|-----------------------------------|-----------------------------------------------------------|
| 1. Decide which items to pack     | LR – List Reminder Descriptions and RI – Reminder Inquiry |
| 2. Create the Exchange file entry | CFE – Create File Entry                                   |
| 3. Export the packed entries      | CHF – Create Host File or  CMM – Create MailMan Message   |

**Import Steps**

| **Step**                                                                 | **Action**                                                                      |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 1. Import the packed items into your Exchange file                       | LHF – Load Host File or  LMM – Load MailMan Message  LWH – Load from a web site |
| 2. Install the Exchange file entry                                       | IFE – Install File Entry                                                        |
| 3. Review what you have done                                             | IH – Installation History                                                       |
| 4. Remove entries from your Exchange file when they are no longer needed | DFE – Delete File Entry                                                         |

##### Reminder Exchange Main Screen

When you select Reminder Exchange from the Reminder Managers Menu, the Clinical Reminder Exchange main screen opens. It contains a list of Exchange file entries in your system (if any) and all the options (actions) to create and delete Exchange file entries, to load them into host files and MailMan messages for export, to import packed reminders from incoming host files and MailMan messages and to install the components in a Reminder Exchange file entry.

List Reminder Definitions and Reminder Definition Inquiry are also included so that you can review reminders before loading them into the Exchange file.

Clinical Reminder Exchange           Sep 16, 2004@15:20:11         Page: 1 of    1 Exchange File Entries. Entry                     Source                Date Packed 1  CDUE                         CRUSER,ONE@VAMC EIGHT    08/08/2003@10:59:52 
   2  CHA UNVESTED PATIENTS        CRPROVIDER,TWO@VAMC ONE  09/26/2004@13:00:59 
   6  EDUTEST                      CRUSER,ONE@VAMC TEN      06/19/2004@11:59:52 
   8  Hypertension Screen (VHACHS  CRPROVIDER,SIX@VAMC SIX  09/20/2004@10:59:22 **+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

##### A: Steps to Export Reminders

<!-- image -->

###### Detailed Steps to Export Reminders

###### Select an item that you want to exchange.

###### Create Exchange File Entry

Use the action CFE **(** Create Exchange File Entry) to create and load packed entries into the Exchange file (#811.8). This allows selection of a reminder component and entry of a description and keywords to be stored in the Exchange file. If a single item is selected, the description will be initialized with the description from the item. You may edit it as necessary.

Clinical Reminder Exchange    Jan 02, 2009@11:21:47          Page:    1 of    1

Exchange File Entries.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Quit// **CFE** Exchange File Entry Creation

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file:  (1-13):

###### 3a.  CHF-Create Host File

Use this action to create a host file containing selected entries from the Exchange file (#811.8).

A host file is any file that is stored in your site’s local “host” directory or system. A complete host file consists of a path, file name, and extension. A path consists of a device and directory name. The default extension is PRD (Packed Reminder Definition). Your default path is determined by your system manager. If necessary, contact your IRM to learn how host files work at your site.

###### Example of a valid path:

REDACTED

**Clinical Reminder Exchange** Apr 02, 2004@11:21:47          Page:    1 of    1

Exchange File Entries.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Quit// CHF

Select Entry(s):  (1-5): 2

Enter a path: REDACTED

A host file is a file in your host system.

A complete host file consists of a path, file name, and extension

A path consists of a device and directory name.

The default extension is prd (Packed Reminder Definition).

The default path is REDACTED

Enter a path: REDACTED &lt;Enter&gt;

Enter a file name: ?

A file name has the format NAME.EXTENSION, the default extension is PRD

Therefore if you type in FILE for the file name, the host file will be

REDACTED

Enter a file name: **DiabeticEye**

Will save reminder to host file REDACTED: Y// **&lt;Enter&gt;** ES

###### 3b. CMM-Create MailMan Message

Use this action to create a MailMan Message containing selected entries from the Exchange file (#811.8).

**Clinical Reminder Exchange** Apr 02, 2004@11:21:47          Page:    1 of    1

Exchange File Entries.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History		      RP   Repack

Select Action: Quit// cmm   MailMan Message Creation

**NOTE** : The number of packed entries you can send via a MailMan message is limited by the MailMan parameters set locally for the number of lines in a message. Please check with your IRM for the number of lines allowed.

Select Entry(s):  (1-5): 2

Enter a subject: [Enter a description of the Mail Message.]

Forward mail to: ?

Enter the recipient(s) of this message in any of the following formats:

Lastname,first              for a user at this site

Lastname,first@REMOTE-SITE  for a user at another site

(note: DUZ may be used, instead of Lastname,first for local or remote users)

G.&lt;group-name&gt;              for a mail group

D.&lt;device-name&gt;             for a device

*                           for a limited broadcast or broadcast to all users

(must be Postmaster or XMSTAR key holder)

Prefix any user address with 'I:' to send Information only.

'C:' to send Carbon Copy.

'L:' to send Later.

'-'  to delete it.

Enter:

G.?                         for a list of mail groups

D.?                         for a list of devices

Enter '??' for detailed help.

Forward mail to: [Enter a user or Mail Group.]

Select basket to send to: IN//

And Forward to:

**Clinical Reminder Exchange** May 03, 2004@11:27:25          Page:    1 of    1

Successfully stored entries in message 43035.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC1     03/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Quit *//*

##### B. Steps to Import Reminders

NOTE: After the installation of PXRM*2*26, you will also be able to load .prd files from a web site, using LWH – Load Web Host File.

<!-- image -->

###### 1a. LMM – Load MailMan Message

This option lets you load a MailMan message containing packed entries into your site’s Exchange file (811.8).

Clinical Reminder Exchange    Jul 23, 2005@11:40:01          Page:    1 of    2

Entry                       Source                   Date Packed

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Next Screen// **lmm** Load MailMan Message

1   CREX: diabetic eye exam

CRPROVIDER,ONE JUL 23, 2001@11:39:51

2   CREX: pain screening

CRPROVIDER,ONE JUL 23, 2001@11:37:59

CHOOSE 1-2: **1** CREX: diabetic eye exam

CRPROVIDER,ONE JUL 23, 2001@11:39:51

Loading MailMan message number 44024

###### 1b. LHF – Load Host File

This action lets you load a host file containing packed entries into your local Exchange file (#811.8).

**NOTE** : Programmer access may be required to upload local host files, depending on how local file protections are set.

Clinical Reminder Exchange    Apr 02, 2004@11:21:47          Page:    1 of    1

Exchange File Entries.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Quit// **lhf** Load Host File

Enter a path: USER$:[TEMP]// **&lt;Enter&gt;**

The following PRD files were found in USER$:[TEMP]

DIABETICEYE.PRD;1

Enter a file name: **DIABETICEYE**

Loading host file USER$:[TEMP]DIABETICEYE.PRD

Select Action: Quit// **-   -**

**Clinical Reminder Exchange** Jul 23, 2005@11:17:42          Page:    1 of    2

Host file USER$:[SPOOL]DIABETICEYE.PRD successfully loaded.

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History		      RP   Repack

Select Action: Next Screen//

###### 1c. LWH – Load Web Host File

This action lets you load a file containing packed entries from a web site. When you select this action, you are prompted to input the URL for the web site. SharePoint sites cannot be accessed because it requires the user’s Windows credentials and they are not available in VistA.

<!-- image -->

###### 2a. Installing Reminder Components from the Reminder Exchange File

The action IFE allows a packed entry to be selected for installation from the Exchange file (#811.8). Details of the Reminder Exchange file entry are displayed. Individual components are displayed (grouped by type). All or individual components may be selected for installation.

CAUTION: Before starting an installation, you should examine the list of components in the packed entry and determine which ones already exist on your system. You should decide what you are going to do with each component and have a plan of action before proceeding with the installation.

REMINDER TERM entry TERMTEST6 already EXISTS, what do you want to do?

Select one of the following:

C         Create a new entry by copying to a new name

I         Install or Overwrite the current entry

Q         Quit the install

S         Skip, do not install this entry

Enter response: S// C reate a new entry by copying to a new name

Exchange File Components      Aug 24, 2009@11:19:18        Page:    1 of    3

Component                                             Category     Exists

Source:      CRMANAGER@VAMCXXXX

Date Packed: 08/12/2009@11:07:26

Package Version: 2.0P12

Description:

Patient reminder due on anyone with 2 entries of a diagnosis of HTN in

the past 3 years.  This reminder does not resolve.  Additional text is

displayed to the patient if the last 3 BPs were &lt;= 130/80, if the last BP

was &gt;140/90 or if any of the last 3 BPs was &gt;=160/100.

If you use a different taxonomy for HTN or for renal diseases, you can

substitute you local taxonomies into the national reminder term.

Keywords:

Components:

GMRV VITAL TYPE

BLOOD PRESSURE                                                       X

REMINDER SPONSOR

1  VA National Center for Health Promotion and

Disease Prevention (NCP)

2  Office of Quality &amp; Performance                                      X

3  National Clinical Practice Guideline Council                         X

REMINDER TAXONOMY

4  VA-DIABETES                                                          X

5  VA-HYPERTENSION                                                      X

REMINDER TERM

6  VA-BP &gt;130/80 (ANY OF LAST 3)

7  VA-BP &gt;=160/100                                                      X

8  VA-BP &gt;=140/90                                                       X

9  VA-MHV DIABETES OR KIDNEY DISEASE                                    X

10  VA-MHV HYPERTENSION DX                                               X

REMINDER DEFINITION

11  VA-MHV HYPERTENSION                                                  X

The “Exists” column indicates the component’s existence on the system based on identical names. When any component that already exists is selected for installation, a checksum will be computed for the already installed version and it will be compared to the checksum of the component in the Reminder Exchange file. If the checksums are identical, then the components are identical and the component will be automatically skipped.

The “Category” column applies to health factors to indicate whether or not the health factor defines a category. If it does, it must be installed before any health factors that belong to that category.

**NOTE** : Some findings, such as lab tests, are not transportable. These findings will be in the component list, as they are used by the definition or dialog, but you will not be able to select them for installation. Non-selectable findings will not have a number. When you install a definition or a dialog that uses a non-transportable finding, if that finding does not exist in your account, you will be prompted to enter a replacement. If it is a lab test, enter the name of the equivalent lab test at your site. The replacement item must match the finding type. A lab test cannot be replaced with anything but a lab test.

If a component is selected for installation, it may be installed without change, or copied to a new name. When installing reminder definitions or dialogs, if a component contained within the definition or dialog is missing from your system, you will be prompted to supply a replacement.

**NOTE** : Because computed findings contain executable code, programmer access (@) is required to install them.

When installing a reminder term the option looks like this:

REMINDER TERM entry TEST TERM already EXISTS,

what do you want to do?

Select one of the following:

C         Create a new entry by copying to a new name

M         Merge findings

O         Overwrite the current entry

U         Update

Q         Quit the install

S         Skip, do not install this entry

Enter response: S//

The Merge and Update actions apply only to terms. For a term, both Merge and Update will preserve any of the site’s mapped findings that are not in the Exchange entry. Also, findings that are in the Exchange entry, but not already mapped at the site will be added as mapped entries. The difference between Update and Merge is that with Update, for findings that are mapped in the site’s term and in the Exchange entry, all finding modifiers in the site’s entry will be replaced by what is in the Exchange entry. Merge does not change the site’s finding modifiers.

The following table summarizes the differences:

| **MERGE**                                                                                                                      | **UPDATE**                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Applies to terms.                                                                                                              | Applies to terms.                                                                                                                                                          |
| For a term, will preserve any of the site’s mapped findings that are not in the Exchange entry.                                | For a term, will preserve any of the site’s mapped findings that are not in the Exchange entry                                                                             |
| Findings that are in the Exchange entry but not already mapped will be added as mapped entries.                                | Findings that are in the Exchange entry but not already mapped will be added as mapped entries.                                                                            |
| For findings that are mapped in the site’s term and in the Exchange entry, Merge does not change the site’s finding modifiers. | For findings that are mapped in the site’s term and in the Exchange entry, Update will replace all finding modifiers in the site’s entry by what is in the Exchange entry. |

###### 2b. Installing a Reminder Dialog

If a reminder dialog is selected for installation, details of the dialog are displayed. The entire dialog or individual components of the dialog (e.g. dialog groups or sub-groups) may be installed.

**Dialog Components** Jan 26, 2005@12:38:51          Page:    1 of    1

Packed reminder dialog: SMOKING CESSATION EDUCATION

Item  Seq. Dialog Summary                                       Type    Exists

1    1    HF ACTIVATE PNEUMOCOCCAL VACCINE DONE ELSEWHERE      element   X

2    2    MH AIMS                                              element   X

3    3    VM BLOOD PRESSURE DONE                               element   X

4         SMOKING CESSATION EDUCATION                          dialog    X

**+ Next Screen   - Prev Screen   ?? More Actions** DD   Dialog Details       DT   Dialog Text          IS   Install Selected

DF   Dialog Findings      DU   Dialog Usage         QU   Quit

DS   Dialog Summary       IA   Install All

Select Action: Quit//

**NOTE:** Order dialogs (quick orders) will be treated like findings that are not transportable, such as lab tests. They will appear in the list, as they are used by the dialog; however, they will not be selectable for installation. When you install the dialog, you will be given the opportunity to replace the quick order with a local one or to delete it from the dialog.

Other views may be selected:

DD Dialog Details – displays dialog summary plus any PXRM type additional prompts.

DF Dialog Findings – displays the findings associated with each dialog component and if the finding already exists on the system.

DT Dialog Text – displays the dialog question text for each component. This gives a preview of how the dialog will display in CPRS.

DU Dialog Usage – displays any other existing reminder dialogs using these components.

The reminder dialog or dialog component may be installed from any view in the same manner as other reminder components. Dialog components may be installed or copied to a new name.

###### Quick Install of Reminder Dialogs

If the reminder dialog and all components are new (or exist already), you can use a quick install option. If only some of the components exist, you will be stepped through them individually. Note that if a dialog is installed without the reminder definition, the option is given to link the dialog to an existing reminder.

Dialog Components             Jan 26, 2005@12:52:05          Page:    1 of    1 Packed reminder dialog: DEMO REMINDER - SIMPLE Item  Seq. Dialog Summary                                       Type    Exists 1         DEMO REMINDER - SIMPLE                               dialog         
                                                                                
  2    5    IM HEP A DONE                                        element        
                                                                                
  3    10   IM HEP A DONE ELSEWHERE                              element        
                                                                                
  4    15   IM HEP A CONTRA                                      element **+ Next Screen   - Prev Screen   ?? More Actions** DD   Dialog Details       DT   Dialog Text          IS   Install Selected
DF   Dialog Findings      DU   Dialog Usage         QU   Quit
DS   Dialog Summary       IA   Install All
Select Action: Quit// IA   Install All  

All dialog components for DEMO REMINDER - SIMPLE are new.
Install reminder dialog without making any changes: Y// ES
Reminder Dialog DEMO REMINDER - SIMPLE is not linked to a reminder.
Select Reminder to Link: LOCAL HEP A IMMUNIZATION

Dialog Components             Jan 26, 2005@12:52:05          Page:    1 of    1 Packed reminder dialog: DEMO REMINDER - SIMPLE
DEMO REMINDER – SIMPLE (reminder dialog) installed from exchange file. Item  Seq. Dialog Summary                                       Type    Exists 1         DEMO REMINDER - SIMPLE                               dialog         
                                                                                
  2    5    IM HEP A DONE                                        element        
                                                                                
  3    10   IM HEP A DONE ELSEWHERE                              element        
                                                                                
  4    15   IM HEP A CONTRA                                      element **+ Next Screen   - Prev Screen   ?? More Actions** DD   Dialog Details       DT   Dialog Text          IS   Install Selected
DF   Dialog Findings      DU   Dialog Usage         QU   Quit
DS   Dialog Summary       IA   Install All
Select Action: Quit//

###### IH – Installation History

Use this option to review the installation of an Exchange file entry.

Clinical Reminder Exchange    Jul 23, 2004@11:27:15          Page:    1 of    2

Exchange File Entries.

Entry                       Source                   Date Packed

1  A NEW REMINDER               CRPROVIDER,ONE@VAMC1       06/18/2004@11:50:40

2  A**A SG PAIN SCREENING       CRPROVIDER,SIX@VAMC6       07/23/2004@10:55:23

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History

Select Action: Next Screen// IH   Installation History

Select Entry(s):  (1-4): 2

Installation History          Jul 23, 2004@11:27:27          Page:    1 of    1

Entry                         Source                   Date Packed

A**A SG PAIN SCREENING       CRPROVIDER,ONE@VAMC1       07/23/2001@10:55:23

Installation Date       Installed By

-----------------       ------------

1 07/23/2004@10:58:48     CRPROVIDER,ONE

**Enter ?? for more actions**

DH   Delete Install History             ID   Installation Details

Select Action: Quit// ID   Installation Details

A**A SG PAIN SCREENING                 07/23/2001@10:55:23  07/23/2001@10:58:48

Component                         Action  New Name

EDUCATION TOPICS

1 MANAGING PAIN                        S

HEALTH FACTORS

2 REMINDER FACTORS                     S

3 Pain New Category                    S

4 PAIN PATIENT DECLINED TO REPORT PAIN S

5 PATIENT UNABLE TO REPORT PAIN SCORE  S

6 PAIN PATIENT REPORTS NEW PAIN        S

7 PATIENT REPORTS NEW PAIN             S

8 HF.SG PATIENT NEEDS PAIN ASSESSMENT  S

TIU TEMPLATE FIELD

9 S’s   OLD/NEW                        S

Installation Detail           Jul 23, 2004@11:27:39          Page:    2 of    2

+      Entry                             Date Packed         Date Installed

REMINDER DEFINITION

10 A**A SG PAIN SCREENING               S

**Enter ?? for more actions**

Select Action:Quit//

###### Delete Reminder Exchange File Entry

Use this option to delete selected entries from the Reminder Exchange file #811.8.

Select Reminder Managers Menu Option: RX  Reminder Exchange

Clinical Reminder Exchange    Jun 21, 2004@12:09:19          Page:    1 of    3

Exchange File Entries.

Entry                       Source                   Date Packed

1  BLOOD PRESSURE CHECK         CRPROVIDER,ONE@VAMC1     03/28/2004@13:12:26

2  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

3  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

4  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

5  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE Create Exchange File Entry         LHF  Load Host File
CHF Create Host File                   LMM  Load MailMan Message
CMM Create MailMan Message             LWH  Load Web Host File
DFE Delete Exchange File Entry         LR   List Reminder Definitions
IFE Install Exchange File Entry        RI   Reminder Definition Inquiry
IH  Installation History               RP   Repack

Select Action: Next Screen// **DFE** Delete Exchange File Entry

Select Entry(s):  (1-5): **1**

Clinical Reminder Exchange    Jun 21, 2004@12:09:47          Page:    1 of    3

Deleted 1 Exchange File entry.

Entry                       Source                   Date Packed

1  SLC PNEUMOCOCCAL VACCINE     CRPROVIDER,TWO@VAMC2     03/29/2004@11:55:11

2  VA-*CHOLESTEROL SCREEN (M)   CRPROVIDER,SIX@VAMC6     03/27/2004@14:59:42

3  VA-ADVANCED DIRECTIVES EDUC  CRPROVIDER,TEN@VAMC10    3/27/2004@14:54:24

4  VA-HEP C RISK ASSESSMENT     CRPROVIDER,ONE@VAMC1     03/27/2004@14:56:13

**+ Next Screen   - Prev Screen   ?? More Actions** CFE  Create Exchange File Entry         IH   Installation History

CHF  Create Host File                   LHF  Load Host File

CMM  Create MailMan Message             LMM  Load MailMan Message

DFE  Delete Exchange File Entry         LR   List Reminder Definitions

IFE  Install Exchange File Entry        RI   Reminder Definition Inquiry

IH  Installation History                RP   Repack

Select Action: Next Screen//

**NOTE** : This does not delete the Host file or MailMan message from the VistA system. If the Host file or MailMan message are not needed any more, you must delete these separately.

###### Repack

This option allows a user to recreate a Reminder Exchange file entry without re-selecting  all of the selection items. Once a user selects a Reminder Exchange file entry to repack, Reminder Exchange will perform the same checks as creating an Reminder Exchange file entry by hand.

**Clinical Reminder Exchange** Aug 29, 2018@06:11:10          Page:   41 of   44

Exchange File Entries.

+Item  Entry                           Source                   Date Packed

314  VA-WH DISCUSS BREAST CA         CRUSER@VAMC TWENTY       03/28/2013@07:30

SCREEN WOMAN 40-49

315  VA-WH DISCUSS BREAST CA WOMAN   CRUSER@VAMC TWENTY       03/28/2013@07:31

40-49 DIALOG

316  VA-WH MAMMOGRAM REVIEW          CRUSER@VAMC TWENTY       03/28/2013@07:40

RESULTS DIALOG

317  VA-WH MAMMOGRAM SCREENING       CRUSER@VAMC TWENTY       03/28/2013@07:32

318  VA-WH MAMMOGRAM SCREENING       CRUSER@VAMC TWENTY       03/28/2013@07:33

DIALOG

319  VA-WH PAP SMEAR REVIEW RESULTS  CRUSER@VAMC TWENTY       03/28/2013@07:34

+         + Next Screen   - Prev Screen   ?? More Actions                    &gt;&gt;&gt;

CFE  Create Exchange File Entry         LHF  Load Host File

CHF  Create Host File                   LMM  Load MailMan Message

CMM  Create MailMan Message             LR   List Reminder Definitions

DFE  Delete Exchange File Entry         LWH  Load Web Host File

IFE  Install Exchange File Entry        RI   Reminder Definition Inquiry

IH   Installation History               RP   Repack

Select Action: Next Screen// rp   Repack

Enter a list or range of numbers (1-339): 314

Repacking entry: VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49

Checking reminder definition(s) for errors.

Checking reminder definition VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49

No fatal reminder definition errors were found.

No fatal reminder definition problems were found, packing will continue.

Checking reminder dialog(s) for errors..

No fatal dialog problems were found, packing will continue.

Enter the Exchange File entry name: VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49

Replace

**Tips for exchanging reminders**

Try at least one simple reminder exchange first – and check the dialog.

A Category for a health factor must exist to install the health factor.

To use your own finding in a reminder you are importing, use the SKIP option. Then when the reminder is installed, you will be prompted for the finding to use in the reminder.

Review local findings carefully.

Allow dedicated time.

Review the findings (terms, taxonomies).

Document your intent and logic in your reminders.

Remember: When you import a reminder, it is YOURS.

Some sites have Web pages set up for review – use the Web before requesting reminders.

Test the reminder exchange.

**NOTE** : **Reminder Exchange Tip**

If you try to exchange a location list from one system to another and there is an inconsistency or mismatch between systems in the AMIS stop code, you will get the following error message. (In this case the system has two selectable entries for stop code 560, which will need to be corrected.)

REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 is NEW, what do you want to do?

Select one of the following:

C         Create a new entry by copying to a new name

I         Install

Q         Quit the install

S         Skip, do not install this entry

Enter response: i  Install

Name associated with AMIS stop code does not match the one in the

packed reminder:

AMIS=560

Site Name=ZZSUBSTANCE ABUSE - GROUP

Name in packed reminder=SUBSTANCE ABUSE - GROUP

The update failed, UPDATE^DIE returned the following error message:

MSG("DIERR")=1^1

MSG("DIERR",1)=701

MSG("DIERR",1,"PARAM",0)=3

MSG("DIERR",1,"PARAM",3)=GYNECOLOGY

MSG("DIERR",1,"PARAM","FIELD")=.01

MSG("DIERR",1,"PARAM","FILE")=810.90011

MSG("DIERR",1,"TEXT",1)=The value 'GYNECOLOGY' for field CREDIT STOP TO

EXCLUDE

in CREDIT STOPS TO EXCLUDE SUB-FIELD in CLINIC STOP LIST SUB-FIELD in

file REMIN

DER LOCATION LIST is not valid.

MSG("DIERR","E",701,1)=

REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 did not get installed!

Examine the above error message for the reason.

### Reminder Test

Before a new or modified reminder is put into production, it should be thoroughly tested. The Reminder Test option provides a convenient tool that can be used as an aid in setting up new reminders and tracking down problems with existing ones. It lets you run a reminder without going through CPRS or Health Summary.

The output from the Reminder Test option provides a view of the internal workings of the clinical reminders software and allows you to see what happened as the reminder was evaluated. Errors and warnings that are not always seen on the Clinical Reminder Maintenance output are displayed here. When setting up a reminder, it’s a good idea to have test patients with known clinical data such as examinations, immunizations, ICDs, CPTs, etc., that are pertinent to the reminder being developed. Using this option to run the reminder for test patients allows you to see if the reminder operates as expected.

You should have patients who are in the cohort and who are not in the cohort. For patients who are in the cohort, you should have some who have the reminder resolved and some who do not.

It is very useful to have the output from the Reminder Inquiry option available when using the test option.

Here is the inquiry for a reminder called EDUTEST.

Select Reminder Definition Management Option: RI  Inquire about Reminder Definition

Select Reminder Definition:  EDUTEST                  Dec 24, 2008 11:00:10 am  Page 1

--------------------------------------------------------------------------------

EDUTEST                                                          No. 660020

--------------------------------------------------------------------------------

Print Name:             Education Test

Class:                  LOCAL

Sponsor:                NONE

Review Date:

Rescission Date:

Usage:                  CPRS

Related VA-* Reminder:

Reminder Dialog:        EXCHANGE 4

Priority:

Description:

Technical Description:

Baseline Frequency:

Do In Advance Time Frame:  Wait until actually DUE

Sex Specific:

Ignore on N/A:

Frequency for Age Range:  1 month for ages 25 to 60

Match Text:  This is the age match text for age range 25

to 60. Patient is in age range.  Line 2.

No Match Text:  Patient is not in age range.  Line 2

Frequency for Age Range:  1 year for ages 61 to 70

Match Text:  This is match text for 61 to 70. The

patient's age is |AGE|.

No Match Text:  This is no match text for 61 to 70, the

patient's age is |AGE|.

Findings:

---- Begin: VA-SUBSTANCE ABUSE  (FI(1)=ED(1)) ----------------------------

Finding Type: EDUCATION TOPICS

Occurrence Count: -4

---- End: VA-SUBSTANCE ABUSE ---------------------------------------------

---- Begin: VA-EXERCISE SCREENING  (FI(2)=ED(11)) ------------------------

Finding Type: EDUCATION TOPICS

Use in Resolution Logic: OR

Occurrence Count: 2

Found Text: VA-EXERCISE SCREENING FOUND TEXT.  Lets test

out some objects.  The patient was seen on

|VISIT DATE|.  His last blood pressure was

|BLOOD PRESSURE|.  His last weight was

|PATIENT WEIGHT|.

Not Found Text: VA-EXERCISE SCREENING NOT FOUND TEXT.

---- End: VA-EXERCISE SCREENING ------------------------------------------

---- Begin: VA-EXERCISE  (FI(3)=ED(363)) ---------------------------------

Finding Type: EDUCATION TOPICS

Occurrence Count: 2

---- End: VA-EXERCISE ----------------------------------------------------

---- Begin: VA-EXERCISE  (FI(4)=ED(363)) ---------------------------------

Finding Type: EDUCATION TOPICS

Beginning Date/Time: T-5M

---- End: VA-EXERCISE ----------------------------------------------------

---- Begin: VA-DIABETES  (FI(5)=ED(360)) ---------------------------------

Finding Type: EDUCATION TOPICS

---- End: VA-DIABETES ----------------------------------------------------

---- Begin: EDUTEST  (FI(8)=RT(660006)) ----------------------------------

Finding Type: REMINDER TERM

Occurrence Count: 3

Mapped Findings:

Mapped Finding Item: ED.VA-SUBSTANCE ABUSE

Mapped Finding Item: ED.VA-EXERCISE SCREENING

Mapped Finding Item: ED.VA-EXERCISE

Mapped Finding Item: ED.VA-ADVANCE DIRECTIVES

---- End: EDUTEST --------------------------------------------------------

Function Findings:

---- Begin: FF(1)---------------------------------------------------------

Function String: MRD(1,2)&gt;MRD(5)

Expanded Function String:

MRD(VA-SUBSTANCE ABUSE,VA-EXERCISE SCREENING)&gt;MRD(VA-DIABETES)

Use in Resolution Logic: AND

---- End: FF(1) ----------------------------------------------------------

---- Begin: FF(2)---------------------------------------------------------

Function String: FI(1)&amp;(FI(4)!FI(5))

Expanded Function String:

FI(VA-SUBSTANCE ABUSE)&amp;(FI(VA-EXERCISE)!FI(VA-DIABETES))

---- End: FF(2) ----------------------------------------------------------

---- Begin: FF(3)---------------------------------------------------------

Function String: COUNT(2)&gt;1

Expanded Function String:

COUNT(VA-EXERCISE SCREENING)&gt;1

Use in Resolution Logic: AND

---- End: FF(3) ----------------------------------------------------------

---- Begin: FF(4)---------------------------------------------------------

Function String: DIFF\_DATE(1,2)&gt;625

Expanded Function String:

DIFF\_DATE(VA-SUBSTANCE ABUSE,VA-EXERCISE SCREENING)&gt;625

---- End: FF(4) ----------------------------------------------------------

General Patient Cohort Found Text:

This is the general cohort found text.

General Patient Cohort Not Found Text:

This is general cohort not found text. Line two of not found. Line 3 of

not found. Patient's age is |AGE|.

General Resolution Found Text:

This is the general resolution found text. Second line of resolution

found text.

General Resolution Not Found Text:

This is the general resolution not found text. Second line of not found.

Third line of not found.

Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient:

(SEX)&amp;(AGE)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)

Default RESOLUTION LOGIC defines findings that resolve the Reminder:

FI(2)&amp;FF(1)&amp;FF(3)

Expanded Resolution Logic:

FI(VA-EXERCISE SCREENING)&amp;FF(1)&amp;FF(3)

Web Sites:

Web Site URL:   Influenza Directive

Web Site Title:

Description:

#### Running Reminder Test

When you run Reminder Test, you are prompted to input a patient, a reminder definition, and the reminder evaluation date/time. The reminder evaluation date/time defaults to NOW, but it can be a date in the past or the future. When the reminder is evaluated, TODAY is set to the evaluation date/time. For example, if a beginning date/time is T-1Y, T is the reminder evaluation date/time. This “time-travel” ability is useful for testing a reminder. If a patient has a finding and you want to see how the reminder evaluates when they do not have the finding, the evaluation date/time can be outside the date range of the finding.

If the definition contains function findings, you will be ask if you want to display a step-by-step function finding evaluation. When a function finding is not working as expected, this can help track down the cause.

If any of the definition findings are terms, the system will ask if you want to display all term findings. This will show the results for all the findings mapped to the term. This can be useful when the result of a term evaluation is not what you expect and you need to determine why.

Select Patient:    ZZZRETSIXEIGHT,PATIENT        4-7-35    666512345

NSC VETERAN             SMB     SMB

Select Reminder:    INFLUENZA SEASONAL IMMUNIZATION     LOCAL

Enter date for reminder evaluation: Jun 14, 2022//   (JUN 14, 2022)

Display step-by-step function finding evaluation? N// O

Display all term findings? N//

#### Test Option Output for the EDUTEST Reminder

Select Reminder Managers Menu Option: RT  Reminder Test

Select Patient:  CRPATIENT,TWO        10-10-72    666554444     YES     ACTIVE DUTY

Enrollment Priority: GROUP 1    Category: IN PROCESS    End Date:

Select Reminder: edutest       LOCAL

Enter date for reminder evaluation: Dec 24, 2008//   (DEC 24, 2008)

Display all term findings? N// y  YES

The elements of the FIEVAL array are:

FIEVAL(1)=1

FIEVAL(1,1)=1

FIEVAL(1,1,"COMMENTS")=

FIEVAL(1,1,"CSUB","COMMENTS")=

FIEVAL(1,1,"CSUB","DATE")=2980700

FIEVAL(1,1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(1,1,"CSUB","VALUE")=

FIEVAL(1,1,"CSUB","VISIT")=3935

FIEVAL(1,1,"DAS")=200

FIEVAL(1,1,"DATE")=2980700

FIEVAL(1,1,"LEVEL OF UNDERSTANDING")=

FIEVAL(1,1,"VALUE")=

FIEVAL(1,1,"VISIT")=3935

FIEVAL(1,2)=1

FIEVAL(1,2,"COMMENTS")=

FIEVAL(1,2,"CSUB","COMMENTS")=

FIEVAL(1,2,"CSUB","DATE")=3000000

FIEVAL(1,2,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(1,2,"CSUB","VALUE")=

FIEVAL(1,2,"CSUB","VISIT")=3997

FIEVAL(1,2,"DAS")=212

FIEVAL(1,2,"DATE")=3000000

FIEVAL(1,2,"LEVEL OF UNDERSTANDING")=

FIEVAL(1,2,"VALUE")=

FIEVAL(1,2,"VISIT")=3997

FIEVAL(1,3)=1

FIEVAL(1,3,"COMMENTS")=

FIEVAL(1,3,"CSUB","COMMENTS")=

FIEVAL(1,3,"CSUB","DATE")=3000202.15

FIEVAL(1,3,"CSUB","LEVEL OF UNDERSTANDING")=3

FIEVAL(1,3,"CSUB","VALUE")=3

FIEVAL(1,3,"CSUB","VISIT")=3693

FIEVAL(1,3,"DAS")=159

FIEVAL(1,3,"DATE")=3000202.15

FIEVAL(1,3,"LEVEL OF UNDERSTANDING")=3

FIEVAL(1,3,"VALUE")=3

FIEVAL(1,3,"VISIT")=3693

FIEVAL(1,4)=1

FIEVAL(1,4,"COMMENTS")=

FIEVAL(1,4,"CSUB","COMMENTS")=

FIEVAL(1,4,"CSUB","DATE")=3000217.085926

FIEVAL(1,4,"CSUB","LEVEL OF UNDERSTANDING")=3

FIEVAL(1,4,"CSUB","VALUE")=3

FIEVAL(1,4,"CSUB","VISIT")=3720

FIEVAL(1,4,"DAS")=151

FIEVAL(1,4,"DATE")=3000217.085926

FIEVAL(1,4,"LEVEL OF UNDERSTANDING")=3

FIEVAL(1,4,"VALUE")=3

FIEVAL(1,4,"VISIT")=3720

FIEVAL(1,"COMMENTS")=

FIEVAL(1,"CSUB","COMMENTS")=

FIEVAL(1,"CSUB","DATE")=2980700

FIEVAL(1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(1,"CSUB","VALUE")=

FIEVAL(1,"CSUB","VISIT")=3935

FIEVAL(1,"DAS")=200

FIEVAL(1,"DATE")=2980700

FIEVAL(1,"FILE NUMBER")=9000010.16

FIEVAL(1,"FINDING")=1;AUTTEDT(

FIEVAL(1,"LEVEL OF UNDERSTANDING")=

FIEVAL(1,"VALUE")=

FIEVAL(1,"VISIT")=3935

FIEVAL(2)=1

FIEVAL(2,1)=1

FIEVAL(2,1,"COMMENTS")=

FIEVAL(2,1,"CSUB","COMMENTS")=

FIEVAL(2,1,"CSUB","DATE")=3000317.08

FIEVAL(2,1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(2,1,"CSUB","VALUE")=

FIEVAL(2,1,"CSUB","VISIT")=3787

FIEVAL(2,1,"DAS")=214

FIEVAL(2,1,"DATE")=3000317.08

FIEVAL(2,1,"LEVEL OF UNDERSTANDING")=

FIEVAL(2,1,"VALUE")=

FIEVAL(2,1,"VISIT")=3787

FIEVAL(2,2)=1

FIEVAL(2,2,"COMMENTS")=

FIEVAL(2,2,"CSUB","COMMENTS")=

FIEVAL(2,2,"CSUB","DATE")=3000106.131524

FIEVAL(2,2,"CSUB","LEVEL OF UNDERSTANDING")=3

FIEVAL(2,2,"CSUB","VALUE")=3

FIEVAL(2,2,"CSUB","VISIT")=3646

FIEVAL(2,2,"DAS")=119

FIEVAL(2,2,"DATE")=3000106.131524

FIEVAL(2,2,"LEVEL OF UNDERSTANDING")=3

FIEVAL(2,2,"VALUE")=3

FIEVAL(2,2,"VISIT")=3646

FIEVAL(2,"COMMENTS")=

FIEVAL(2,"CSUB","COMMENTS")=

FIEVAL(2,"CSUB","DATE")=3000317.08

FIEVAL(2,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(2,"CSUB","VALUE")=

FIEVAL(2,"CSUB","VISIT")=3787

FIEVAL(2,"DAS")=214

FIEVAL(2,"DATE")=3000317.08

FIEVAL(2,"FILE NUMBER")=9000010.16

FIEVAL(2,"FINDING")=11;AUTTEDT(

FIEVAL(2,"LEVEL OF UNDERSTANDING")=

FIEVAL(2,"VALUE")=

FIEVAL(2,"VISIT")=3787

FIEVAL(3)=1

FIEVAL(3,1)=1

FIEVAL(3,1,"COMMENTS")=

FIEVAL(3,1,"CSUB","COMMENTS")=

FIEVAL(3,1,"CSUB","DATE")=3000317.08

FIEVAL(3,1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(3,1,"CSUB","VALUE")=

FIEVAL(3,1,"CSUB","VISIT")=3787

FIEVAL(3,1,"DAS")=215

FIEVAL(3,1,"DATE")=3000317.08

FIEVAL(3,1,"LEVEL OF UNDERSTANDING")=

FIEVAL(3,1,"VALUE")=

FIEVAL(3,1,"VISIT")=3787

FIEVAL(3,2)=1

FIEVAL(3,2,"COMMENTS")=

FIEVAL(3,2,"CSUB","COMMENTS")=

FIEVAL(3,2,"CSUB","DATE")=3000000

FIEVAL(3,2,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(3,2,"CSUB","VALUE")=

FIEVAL(3,2,"CSUB","VISIT")=3997

FIEVAL(3,2,"DAS")=210

FIEVAL(3,2,"DATE")=3000000

FIEVAL(3,2,"LEVEL OF UNDERSTANDING")=

FIEVAL(3,2,"VALUE")=

FIEVAL(3,2,"VISIT")=3997

FIEVAL(3,"COMMENTS")=

FIEVAL(3,"CSUB","COMMENTS")=

FIEVAL(3,"CSUB","DATE")=3000317.08

FIEVAL(3,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(3,"CSUB","VALUE")=

FIEVAL(3,"CSUB","VISIT")=3787

FIEVAL(3,"DAS")=215

FIEVAL(3,"DATE")=3000317.08

FIEVAL(3,"FILE NUMBER")=9000010.16

FIEVAL(3,"FINDING")=363;AUTTEDT(

FIEVAL(3,"LEVEL OF UNDERSTANDING")=

FIEVAL(3,"VALUE")=

FIEVAL(3,"VISIT")=3787

FIEVAL(4)=0

FIEVAL(4,"FINDING")=363;AUTTEDT(

FIEVAL(5)=1

FIEVAL(5,1)=1

FIEVAL(5,1,"COMMENTS")=

FIEVAL(5,1,"CSUB","COMMENTS")=

FIEVAL(5,1,"CSUB","DATE")=3000317.08

FIEVAL(5,1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(5,1,"CSUB","VALUE")=

FIEVAL(5,1,"CSUB","VISIT")=3787

FIEVAL(5,1,"DAS")=203

FIEVAL(5,1,"DATE")=3000317.08

FIEVAL(5,1,"LEVEL OF UNDERSTANDING")=

FIEVAL(5,1,"VALUE")=

FIEVAL(5,1,"VISIT")=3787

FIEVAL(5,"COMMENTS")=

FIEVAL(5,"CSUB","COMMENTS")=

FIEVAL(5,"CSUB","DATE")=3000317.08

FIEVAL(5,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(5,"CSUB","VALUE")=

FIEVAL(5,"CSUB","VISIT")=3787

FIEVAL(5,"DAS")=203

FIEVAL(5,"DATE")=3000317.08

FIEVAL(5,"FILE NUMBER")=9000010.16

FIEVAL(5,"FINDING")=360;AUTTEDT(

FIEVAL(5,"LEVEL OF UNDERSTANDING")=

FIEVAL(5,"VALUE")=

FIEVAL(5,"VISIT")=3787

FIEVAL(8)=1

FIEVAL(8,1)=1

FIEVAL(8,1,"COMMENTS")=

FIEVAL(8,1,"CSUB","COMMENTS")=

FIEVAL(8,1,"CSUB","DATE")=3000317.08

FIEVAL(8,1,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(8,1,"CSUB","VALUE")=

FIEVAL(8,1,"CSUB","VISIT")=3787

FIEVAL(8,1,"DAS")=201

FIEVAL(8,1,"DATE")=3000317.08

FIEVAL(8,1,"FILE NUMBER")=9000010.16

FIEVAL(8,1,"FINDING")=1;AUTTEDT(

FIEVAL(8,1,"LEVEL OF UNDERSTANDING")=

FIEVAL(8,1,"VALUE")=

FIEVAL(8,1,"VISIT")=3787

FIEVAL(8,2)=1

FIEVAL(8,2,"COMMENTS")=

FIEVAL(8,2,"CSUB","COMMENTS")=

FIEVAL(8,2,"CSUB","DATE")=3000317.08

FIEVAL(8,2,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(8,2,"CSUB","VALUE")=

FIEVAL(8,2,"CSUB","VISIT")=3787

FIEVAL(8,2,"DAS")=214

FIEVAL(8,2,"DATE")=3000317.08

FIEVAL(8,2,"FILE NUMBER")=9000010.16

FIEVAL(8,2,"FINDING")=11;AUTTEDT(

FIEVAL(8,2,"LEVEL OF UNDERSTANDING")=

FIEVAL(8,2,"VALUE")=

FIEVAL(8,2,"VISIT")=3787

FIEVAL(8,3)=1

FIEVAL(8,3,"COMMENTS")=

FIEVAL(8,3,"CSUB","COMMENTS")=

FIEVAL(8,3,"CSUB","DATE")=3000317.08

FIEVAL(8,3,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(8,3,"CSUB","VALUE")=

FIEVAL(8,3,"CSUB","VISIT")=3787

FIEVAL(8,3,"DAS")=215

FIEVAL(8,3,"DATE")=3000317.08

FIEVAL(8,3,"FILE NUMBER")=9000010.16

FIEVAL(8,3,"FINDING")=363;AUTTEDT(

FIEVAL(8,3,"LEVEL OF UNDERSTANDING")=

FIEVAL(8,3,"VALUE")=

FIEVAL(8,3,"VISIT")=3787

FIEVAL(8,"COMMENTS")=

FIEVAL(8,"CSUB","COMMENTS")=

FIEVAL(8,"CSUB","DATE")=3000317.08

FIEVAL(8,"CSUB","LEVEL OF UNDERSTANDING")=

FIEVAL(8,"CSUB","VALUE")=

FIEVAL(8,"CSUB","VISIT")=3787

FIEVAL(8,"DAS")=201

FIEVAL(8,"DATE")=3000317.08

FIEVAL(8,"FILE NUMBER")=9000010.16

FIEVAL(8,"FINDING")=1;AUTTEDT(

FIEVAL(8,"LEVEL OF UNDERSTANDING")=

FIEVAL(8,"TERM")=EDUTEST^^^3001206

FIEVAL(8,"TERM IEN")=660006

FIEVAL(8,"VALUE")=

FIEVAL(8,"VISIT")=3787

FIEVAL("AGE")=1

FIEVAL("AGE",1)=1

FIEVAL("AGE",2)=0

FIEVAL("DFN")=54

FIEVAL("EVAL DATE/TIME")=3081224

FIEVAL("FF1")=0

FIEVAL("FF1","DETAIL")=0^MRD(1,2)&gt;MRD(5)^3000317.08&gt;3000317.08

FIEVAL("FF1","FINDING")=1;PXRMD(802.4,

FIEVAL("FF1","NUMBER")=1

FIEVAL("FF2")=1

FIEVAL("FF2","DETAIL")=1^FI(1)&amp;(FI(4)!FI(5))^1&amp;(0!1)

FIEVAL("FF2","FINDING")=5;PXRMD(802.4,

FIEVAL("FF2","NUMBER")=2

FIEVAL("FF3")=1

FIEVAL("FF3","DETAIL")=1^COUNT(2)&gt;1^2&gt;1

FIEVAL("FF3","FINDING")=2;PXRMD(802.4,

FIEVAL("FF3","NUMBER")=3

FIEVAL("FF4")=0

FIEVAL("FF4","DETAIL")=0^DIFF\_DATE(1,2)&gt;625^625&gt;625

FIEVAL("FF4","FINDING")=7;PXRMD(802.4,

FIEVAL("FF4","NUMBER")=4

FIEVAL("PATIENT AGE")=56

FIEVAL("SEX")=1

Term findings:

Finding 8:

TFIEVAL(8,1)=1

TFIEVAL(8,1,1)=1

TFIEVAL(8,1,1,"COMMENTS")=

TFIEVAL(8,1,1,"CSUB","COMMENTS")=

TFIEVAL(8,1,1,"CSUB","DATE")=3000317.08

TFIEVAL(8,1,1,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,1,1,"CSUB","VALUE")=

TFIEVAL(8,1,1,"CSUB","VISIT")=3787

TFIEVAL(8,1,1,"DAS")=201

TFIEVAL(8,1,1,"DATE")=3000317.08

TFIEVAL(8,1,1,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,1,1,"VALUE")=

TFIEVAL(8,1,1,"VISIT")=3787

TFIEVAL(8,1,2)=1

TFIEVAL(8,1,2,"COMMENTS")=

TFIEVAL(8,1,2,"CSUB","COMMENTS")=

TFIEVAL(8,1,2,"CSUB","DATE")=3000217.085926

TFIEVAL(8,1,2,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,1,2,"CSUB","VALUE")=3

TFIEVAL(8,1,2,"CSUB","VISIT")=3720

TFIEVAL(8,1,2,"DAS")=151

TFIEVAL(8,1,2,"DATE")=3000217.085926

TFIEVAL(8,1,2,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,1,2,"VALUE")=3

TFIEVAL(8,1,2,"VISIT")=3720

TFIEVAL(8,1,3)=1

TFIEVAL(8,1,3,"COMMENTS")=

TFIEVAL(8,1,3,"CSUB","COMMENTS")=

TFIEVAL(8,1,3,"CSUB","DATE")=3000202.15

TFIEVAL(8,1,3,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,1,3,"CSUB","VALUE")=3

TFIEVAL(8,1,3,"CSUB","VISIT")=3693

TFIEVAL(8,1,3,"DAS")=159

TFIEVAL(8,1,3,"DATE")=3000202.15

TFIEVAL(8,1,3,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,1,3,"VALUE")=3

TFIEVAL(8,1,3,"VISIT")=3693

TFIEVAL(8,1,"COMMENTS")=

TFIEVAL(8,1,"CSUB","COMMENTS")=

TFIEVAL(8,1,"CSUB","DATE")=3000317.08

TFIEVAL(8,1,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,1,"CSUB","VALUE")=

TFIEVAL(8,1,"CSUB","VISIT")=3787

TFIEVAL(8,1,"DAS")=201

TFIEVAL(8,1,"DATE")=3000317.08

TFIEVAL(8,1,"FILE NUMBER")=9000010.16

TFIEVAL(8,1,"FINDING")=1;AUTTEDT(

TFIEVAL(8,1,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,1,"VALUE")=

TFIEVAL(8,1,"VISIT")=3787

TFIEVAL(8,2)=1

TFIEVAL(8,2,1)=1

TFIEVAL(8,2,1,"COMMENTS")=

TFIEVAL(8,2,1,"CSUB","COMMENTS")=

TFIEVAL(8,2,1,"CSUB","DATE")=3000317.08

TFIEVAL(8,2,1,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,1,"CSUB","VALUE")=

TFIEVAL(8,2,1,"CSUB","VISIT")=3787

TFIEVAL(8,2,1,"DAS")=214

TFIEVAL(8,2,1,"DATE")=3000317.08

TFIEVAL(8,2,1,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,1,"VALUE")=

TFIEVAL(8,2,1,"VISIT")=3787

TFIEVAL(8,2,2)=1

TFIEVAL(8,2,2,"COMMENTS")=

TFIEVAL(8,2,2,"CSUB","COMMENTS")=

TFIEVAL(8,2,2,"CSUB","DATE")=3000106.131524

TFIEVAL(8,2,2,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,2,2,"CSUB","VALUE")=3

TFIEVAL(8,2,2,"CSUB","VISIT")=3646

TFIEVAL(8,2,2,"DAS")=119

TFIEVAL(8,2,2,"DATE")=3000106.131524

TFIEVAL(8,2,2,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,2,2,"VALUE")=3

TFIEVAL(8,2,2,"VISIT")=3646

TFIEVAL(8,2,3)=1

TFIEVAL(8,2,3,"COMMENTS")=

TFIEVAL(8,2,3,"CSUB","COMMENTS")=

TFIEVAL(8,2,3,"CSUB","DATE")=3000000

TFIEVAL(8,2,3,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,3,"CSUB","VALUE")=

TFIEVAL(8,2,3,"CSUB","VISIT")=3997

TFIEVAL(8,2,3,"DAS")=213

TFIEVAL(8,2,3,"DATE")=3000000

TFIEVAL(8,2,3,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,3,"VALUE")=

TFIEVAL(8,2,3,"VISIT")=3997

TFIEVAL(8,2,"COMMENTS")=

TFIEVAL(8,2,"CSUB","COMMENTS")=

TFIEVAL(8,2,"CSUB","DATE")=3000317.08

TFIEVAL(8,2,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,"CSUB","VALUE")=

TFIEVAL(8,2,"CSUB","VISIT")=3787

TFIEVAL(8,2,"DAS")=214

TFIEVAL(8,2,"DATE")=3000317.08

TFIEVAL(8,2,"FILE NUMBER")=9000010.16

TFIEVAL(8,2,"FINDING")=11;AUTTEDT(

TFIEVAL(8,2,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,2,"VALUE")=

TFIEVAL(8,2,"VISIT")=3787

TFIEVAL(8,3)=1

TFIEVAL(8,3,1)=1

TFIEVAL(8,3,1,"COMMENTS")=

TFIEVAL(8,3,1,"CSUB","COMMENTS")=

TFIEVAL(8,3,1,"CSUB","DATE")=3000317.08

TFIEVAL(8,3,1,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,1,"CSUB","VALUE")=

TFIEVAL(8,3,1,"CSUB","VISIT")=3787

TFIEVAL(8,3,1,"DAS")=215

TFIEVAL(8,3,1,"DATE")=3000317.08

TFIEVAL(8,3,1,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,1,"VALUE")=

TFIEVAL(8,3,1,"VISIT")=3787

TFIEVAL(8,3,2)=1

TFIEVAL(8,3,2,"COMMENTS")=

TFIEVAL(8,3,2,"CSUB","COMMENTS")=

TFIEVAL(8,3,2,"CSUB","DATE")=3000000

TFIEVAL(8,3,2,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,2,"CSUB","VALUE")=

TFIEVAL(8,3,2,"CSUB","VISIT")=3997

TFIEVAL(8,3,2,"DAS")=210

TFIEVAL(8,3,2,"DATE")=3000000

TFIEVAL(8,3,2,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,2,"VALUE")=

TFIEVAL(8,3,2,"VISIT")=3997

TFIEVAL(8,3,3)=1

TFIEVAL(8,3,3,"COMMENTS")=

TFIEVAL(8,3,3,"CSUB","COMMENTS")=

TFIEVAL(8,3,3,"CSUB","DATE")=2990318.100853

TFIEVAL(8,3,3,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,3,"CSUB","VALUE")=

TFIEVAL(8,3,3,"CSUB","VISIT")=2852

TFIEVAL(8,3,3,"DAS")=73

TFIEVAL(8,3,3,"DATE")=2990318.100853

TFIEVAL(8,3,3,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,3,"VALUE")=

TFIEVAL(8,3,3,"VISIT")=2852

TFIEVAL(8,3,"COMMENTS")=

TFIEVAL(8,3,"CSUB","COMMENTS")=

TFIEVAL(8,3,"CSUB","DATE")=3000317.08

TFIEVAL(8,3,"CSUB","LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,"CSUB","VALUE")=

TFIEVAL(8,3,"CSUB","VISIT")=3787

TFIEVAL(8,3,"DAS")=215

TFIEVAL(8,3,"DATE")=3000317.08

TFIEVAL(8,3,"FILE NUMBER")=9000010.16

TFIEVAL(8,3,"FINDING")=363;AUTTEDT(

TFIEVAL(8,3,"LEVEL OF UNDERSTANDING")=

TFIEVAL(8,3,"VALUE")=

TFIEVAL(8,3,"VISIT")=3787

TFIEVAL(8,4)=1

TFIEVAL(8,4,1)=1

TFIEVAL(8,4,1,"COMMENTS")=

TFIEVAL(8,4,1,"CSUB","COMMENTS")=

TFIEVAL(8,4,1,"CSUB","DATE")=3000211.153525

TFIEVAL(8,4,1,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,1,"CSUB","VALUE")=3

TFIEVAL(8,4,1,"CSUB","VISIT")=3716

TFIEVAL(8,4,1,"DAS")=147

TFIEVAL(8,4,1,"DATE")=3000211.153525

TFIEVAL(8,4,1,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,1,"VALUE")=3

TFIEVAL(8,4,1,"VISIT")=3716

TFIEVAL(8,4,2)=1

TFIEVAL(8,4,2,"COMMENTS")=

TFIEVAL(8,4,2,"CSUB","COMMENTS")=

TFIEVAL(8,4,2,"CSUB","DATE")=3000113.160726

TFIEVAL(8,4,2,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,2,"CSUB","VALUE")=3

TFIEVAL(8,4,2,"CSUB","VISIT")=3662

TFIEVAL(8,4,2,"DAS")=132

TFIEVAL(8,4,2,"DATE")=3000113.160726

TFIEVAL(8,4,2,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,2,"VALUE")=3

TFIEVAL(8,4,2,"VISIT")=3662

TFIEVAL(8,4,"COMMENTS")=

TFIEVAL(8,4,"CSUB","COMMENTS")=

TFIEVAL(8,4,"CSUB","DATE")=3000211.153525

TFIEVAL(8,4,"CSUB","LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,"CSUB","VALUE")=3

TFIEVAL(8,4,"CSUB","VISIT")=3716

TFIEVAL(8,4,"DAS")=147

TFIEVAL(8,4,"DATE")=3000211.153525

TFIEVAL(8,4,"FILE NUMBER")=9000010.16

TFIEVAL(8,4,"FINDING")=338;AUTTEDT(

TFIEVAL(8,4,"LEVEL OF UNDERSTANDING")=3

TFIEVAL(8,4,"VALUE")=3

TFIEVAL(8,4,"VISIT")=3716

The elements of the ^TMP(PXRMID,$J) array are:

^TMP(PXRMID,$J,660020,"PATIENT COHORT LOGIC")=1^(SEX)&amp;(AGE)^(1)&amp;(1)

^TMP(PXRMID,$J,660020,"REMINDER NAME")=Education Test

^TMP(PXRMID,$J,660020,"RESOLUTION LOGIC")=0^(0)!FI(2)&amp;FF(1)&amp;FF(3)^(0)!1&amp;0&amp;1

^TMP(PXRMID,$J,660020,"zFREQARNG")=1M^25^60^Baseline

The elements of the ^TMP("PXRHM",$J) array are:

^TMP("PXRHM",$J,660020,"Education Test")=DUE NOW^DUE NOW^unknown

^TMP("PXRHM",$J,660020,"Education Test","TXT",1)=Frequency: Due every 1 month fo

r ages 25 to 60.

^TMP("PXRHM",$J,660020,"Education Test","TXT",2)=This is the age match text for

age range 25 to 60. Patient is in age

^TMP("PXRHM",$J,660020,"Education Test","TXT",3)=range. Line 2.

^TMP("PXRHM",$J,660020,"Education Test","TXT",4)=This is no match text for 61 to

70, the patient's age is 56.

^TMP("PXRHM",$J,660020,"Education Test","TXT",5)=This is the general cohort foun

d text.

^TMP("PXRHM",$J,660020,"Education Test","TXT",6)=This is the general resolution

not found text. Second line of not

^TMP("PXRHM",$J,660020,"Education Test","TXT",7)=found. Third line of not found.

^TMP("PXRHM",$J,660020,"Education Test","TXT",8)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",9)=Resolution:

^TMP("PXRHM",$J,660020,"Education Test","TXT",10)= Education Topic: Exercise Scr

eening

^TMP("PXRHM",$J,660020,"Education Test","TXT",11)=  03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",12)=  01/06/2000 level of understa

nding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",13)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",14)=  VA-EXERCISE SCREENING FOUND

TEXT. Lets test out some objects. The

^TMP("PXRHM",$J,660020,"Education Test","TXT",15)=  patient was seen on 03/17/00

08:00. His last blood pressure was

^TMP("PXRHM",$J,660020,"Education Test","TXT",16)=  Blood Pressure: 120/76 (01/1

1/2001 19:24). His last weight was 233

^TMP("PXRHM",$J,660020,"Education Test","TXT",17)=  lb [105.9 kg] (03/30/2000 14

:15).

^TMP("PXRHM",$J,660020,"Education Test","TXT",18)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",19)=Information:

^TMP("PXRHM",$J,660020,"Education Test","TXT",20)= Education Topic: Substance Ab

use

^TMP("PXRHM",$J,660020,"Education Test","TXT",21)=  07/00/1998

^TMP("PXRHM",$J,660020,"Education Test","TXT",22)=  00/00/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",23)=  02/02/2000 level of understa

nding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",24)=  02/17/2000 level of understa

nding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",25)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",26)= Education Topic: Exercise

^TMP("PXRHM",$J,660020,"Education Test","TXT",27)=  03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",28)=  00/00/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",29)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",30)= Education Topic: Diabetes

^TMP("PXRHM",$J,660020,"Education Test","TXT",31)=  03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",32)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",33)= Reminder Term: EDUTEST

^TMP("PXRHM",$J,660020,"Education Test","TXT",34)=  Education Topic: Substance A

buse

^TMP("PXRHM",$J,660020,"Education Test","TXT",35)=   03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",36)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",37)=  Education Topic: Exercise Sc

reening

^TMP("PXRHM",$J,660020,"Education Test","TXT",38)=   03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",39)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",40)=  Education Topic: Exercise

^TMP("PXRHM",$J,660020,"Education Test","TXT",41)=   03/17/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",42)=

Formatted Output:

--STATUS-- --DUE DATE--  --LAST DONE--

Education Test                       DUE NOW     DUE NOW       unknown

Frequency: Due every 1 month for ages 25 to 60.

This is the age match text for age range 25 to 60. Patient is in age

range. Line 2.

This is no match text for 61 to 70, the patient's age is 56.

This is the general cohort found text.

This is the general resolution not found text. Second line of not

found. Third line of not found.

Resolution:

Education Topic: Exercise Screening

03/17/2000

01/06/2000 level of understanding - GOOD

VA-EXERCISE SCREENING FOUND TEXT. Lets test out some objects. The

patient was seen on 03/17/00 08:00. His last blood pressure was

Blood Pressure: 120/76 (01/11/2001 19:24). His last weight was 233

lb [105.9 kg] (03/30/2000 14:15).

Information:

Education Topic: Substance Abuse

07/00/1998

00/00/2000

02/02/2000 level of understanding - GOOD

02/17/2000 level of understanding - GOOD

Education Topic: Exercise

03/17/2000

00/00/2000

Education Topic: Diabetes

03/17/2000

Reminder Term: EDUTEST

Education Topic: Substance Abuse

03/17/2000

Education Topic: Exercise Screening

03/17/2000

Education Topic: Exercise

03/17/2000

**Reminder Test Explained**

There are three sections in this output. We will go through them individually.

1. The first section is the FIEVAL (Finding EVALuation) array, which corresponds to the findings in the reminder definition. If we look back at our definition inquiry, we see there are 6 findings in this reminder.

Five Education Topics

One Reminder Term

The entries in FIEVAL(1) show us what was found for finding 1:

The elements of the FIEVAL array are:

<!-- image -->

<!-- image -->

<!-- image -->

**NOTE:** When a Reminder Test is run, some elements of the FIEVAL array have a “ *CSUB* ” subscript. Example for an orderable item finding:

FIEVAL(5,"CSUB","DURATION")=1774

FIEVAL(5,"CSUB","ORDER")=3366^CA ULTRA^546;99RAP

FIEVAL(5,"CSUB","RELEASE DATE")=3010917.1625

FIEVAL(5,"CSUB","START DATE")=3010917

FIEVAL(5,"CSUB","STATUS")=PENDING

FIEVAL(5,"CSUB","STOP DATE")=

FIEVAL(5,"CSUB","VALUE")=PENDING

Each of the subscripts following “CSUB” may be used in a Condition (hence the abbreviation Condition SUBscript). For example:

I V(“DURATION”)&gt;90

The use of “CSUB” data has expanded beyond Condition statements.  The other places where they can be used are in function findings and CSUB Objects. For more information, see the CSUB Objects section.

Below is a snippet of how the evaluation appears if “Yes” is entered at the prompt “Display all term findings”. Note that this is not the complete reminder test output. Only the vital parts of the reminder test output are displayed here, to save on space. In a live situation, you will have the entire reminder test output displayed, which can be lengthy.

Display all term findings? N// YES

The elements of the FIEVAL array are:

FIEVAL(1)=1

FIEVAL(1,1)=1

FIEVAL(1,1,"CLINICAL TERM")=

FIEVAL(1,1,"CODEP")=12989

FIEVAL(1,1,"COMMENTS")=

FIEVAL(1,1,"CONDITION")=1

FIEVAL(1,1,"CSUB","CLINICAL TERM")=

FIEVAL(1,1,"CSUB","COMMENTS")=

FIEVAL(1,1,"CSUB","DATE OF INJURY")=

FIEVAL(1,1,"CSUB","MODIFIER")=

FIEVAL(1,1,"CSUB","PRIMARY/SECONDARY")=S

FIEVAL(1,1,"CSUB","PROBLEM LIST ENTRY")=

FIEVAL(1,1,"CSUB","PROVIDER NARRATIVE")=3906

FIEVAL(1,1,"CSUB","VISIT")=5161991

FIEVAL(1,1,"DAS")=3238132

FIEVAL(1,1,"DATE")=3050615.103

FIEVAL(1,1,"DATE OF INJURY")=

FIEVAL(1,1,"FILE NUMBER")=9000010.07

FIEVAL(1,1,"FILE SPECIFIC")=S

FIEVAL(1,1,"FINDING")=52;PXD(811.2,

FIEVAL(1,1,"MODIFIER")=

FIEVAL(1,1,"PRIMARY/SECONDARY")=S

FIEVAL(1,1,"PROBLEM LIST ENTRY")=

FIEVAL(1,1,"PROVIDER NARRATIVE")=3906

FIEVAL(1,1,"VISIT")=5161991

FIEVAL(1,2)=1

FIEVAL(1,2,"CLINICAL TERM")=

FIEVAL(1,2,"CODEP")=2507

FIEVAL(1,2,"COMMENTS")=

FIEVAL(1,2,"CONDITION")=1

FIEVAL(1,2,"CSUB","CLINICAL TERM")=

FIEVAL(1,2,"CSUB","COMMENTS")=

FIEVAL(1,2,"CSUB","DATE OF INJURY")=

FIEVAL(1,2,"CSUB","MODIFIER")=

FIEVAL(1,2,"CSUB","PRIMARY/SECONDARY")=P

FIEVAL(1,2,"CSUB","PROBLEM LIST ENTRY")=

FIEVAL(1,2,"CSUB","PROVIDER NARRATIVE")=1082

FIEVAL(1,2,"CSUB","VISIT")=3970337

FIEVAL(1,2,"DAS")=1896973

FIEVAL(1,2,"DATE")=3020913.131038

FIEVAL(1,2,"DATE OF INJURY")=

FIEVAL(1,2,"FILE NUMBER")=9000010.07

FIEVAL(1,2,"FILE SPECIFIC")=P

FIEVAL(1,2,"FINDING")=52;PXD(811.2,

FIEVAL(1,2,"MODIFIER")=

FIEVAL(1,2,"PRIMARY/SECONDARY")=P

FIEVAL(1,2,"PROBLEM LIST ENTRY")=

FIEVAL(1,2,"PROVIDER NARRATIVE")=1082

FIEVAL(1,2,"VISIT")=3970337

FIEVAL(1,3)=1

FIEVAL(1,3,"CLINICAL TERM")=

FIEVAL(1,3,"CODEP")=2507

FIEVAL(1,3,"COMMENTS")=

FIEVAL(1,3,"CONDITION")=1

FIEVAL(1,3,"CSUB","CLINICAL TERM")=

FIEVAL(1,3,"CSUB","COMMENTS")=

FIEVAL(1,3,"CSUB","DATE OF INJURY")=

FIEVAL(1,3,"CSUB","MODIFIER")=

FIEVAL(1,3,"CSUB","PRIMARY/SECONDARY")=P

FIEVAL(1,3,"CSUB","PROBLEM LIST ENTRY")=

FIEVAL(1,3,"CSUB","PROVIDER NARRATIVE")=1082

FIEVAL(1,3,"CSUB","VISIT")=3967489

FIEVAL(1,3,"DAS")=1893712

FIEVAL(1,3,"DATE")=3020911.131046

FIEVAL(1,3,"DATE OF INJURY")=

FIEVAL(1,3,"FILE NUMBER")=9000010.07

FIEVAL(1,3,"FILE SPECIFIC")=P

FIEVAL(1,3,"FINDING")=52;PXD(811.2,

FIEVAL(1,3,"MODIFIER")=

FIEVAL(1,3,"PRIMARY/SECONDARY")=P

FIEVAL(1,3,"PROBLEM LIST ENTRY")=

FIEVAL(1,3,"PROVIDER NARRATIVE")=1082

FIEVAL(1,3,"VISIT")=3967489

FIEVAL(1,"CLINICAL TERM")=

FIEVAL(1,"CODEP")=12989

FIEVAL(1,"COMMENTS")=

FIEVAL(1,"CONDITION")=1

FIEVAL(1,"CSUB","CLINICAL TERM")=

FIEVAL(1,"CSUB","COMMENTS")=

FIEVAL(1,"CSUB","DATE OF INJURY")=

FIEVAL(1,"CSUB","MODIFIER")=

FIEVAL(1,"CSUB","PRIMARY/SECONDARY")=S

FIEVAL(1,"CSUB","PROBLEM LIST ENTRY")=

FIEVAL(1,"CSUB","PROVIDER NARRATIVE")=3906

FIEVAL(1,"CSUB","VISIT")=5161991

FIEVAL(1,"DAS")=3238132

FIEVAL(1,"DATE")=3050615.103

FIEVAL(1,"DATE OF INJURY")=

FIEVAL(1,"FILE NUMBER")=9000010.07

FIEVAL(1,"FILE SPECIFIC")=S

FIEVAL(1,"FINDING")=52;PXD(811.2,

FIEVAL(1,"MODIFIER")=

FIEVAL(1,"PRIMARY/SECONDARY")=S

FIEVAL(1,"PROBLEM LIST ENTRY")=

FIEVAL(1,"PROVIDER NARRATIVE")=3906

FIEVAL(1,"TERM")=VA-IHD DIAGNOSIS^^^3010723

FIEVAL(1,"TERM IEN")=26

FIEVAL(1,"VISIT")=5161991

FIEVAL(2)=0

FIEVAL(3)=0

FIEVAL(3,"TERM")=VA-OUTSIDE LDL &lt;100^^^3011113

FIEVAL(3,"TERM IEN")=35

FIEVAL(4)=0

FIEVAL(4,"TERM")=VA-OUTSIDE LDL 100-119^^^3010910

FIEVAL(4,"TERM IEN")=34

FIEVAL(5)=0

FIEVAL(5,"TERM")=VA-OUTSIDE LDL 120-129^^^3010925

FIEVAL(5,"TERM IEN")=52

FIEVAL(6)=0

FIEVAL(6,"TERM")=VA-OUTSIDE LDL &gt;129^^^3011113

FIEVAL(6,"TERM IEN")=36

FIEVAL(7)=0

FIEVAL(7,"TERM")=VA-ORDER LIPID PROFILE HEALTH FACTOR^^^3020131

FIEVAL(7,"TERM IEN")=61

FIEVAL(8)=0

FIEVAL(8,"TERM")=VA-REFUSED LIPID PROFILE^^^3011022

FIEVAL(8,"TERM IEN")=40

FIEVAL(9)=0

FIEVAL(9,"TERM")=VA-OTHER DEFER LIPID PROFILE^^^3011022

FIEVAL(9,"TERM IEN")=41

FIEVAL(10)=0

FIEVAL(10,"TERM")=VA-UNCONFIRMED IHD DIAGNOSIS^^^3011017

FIEVAL(10,"TERM IEN")=42

FIEVAL(12)=0

FIEVAL(12,"TERM")=VA-LIPID LOWERING MEDS^^^3011007

FIEVAL(12,"TERM IEN")=54

FIEVAL(14)=0

FIEVAL("AGE")=1

FIEVAL("AGE",1)=1

FIEVAL("DFN")=36167

FIEVAL("EVAL DATE/TIME")=3060125

FIEVAL("FF1")=1

FIEVAL("FF1","FINDING")=1;PXRMD(802.4,

FIEVAL("FF1","NAME")=

FIEVAL("FF1","VALUE")=1

FIEVAL("PATIENT AGE")=86

FIEVAL("SEX")=1

Term findings:

Finding 1:

TFIEVAL(1,1)=1

TFIEVAL(1,1,1)=1

TFIEVAL(1,1,1,"CLINICAL TERM")=

TFIEVAL(1,1,1,"CODEP")=12989

TFIEVAL(1,1,1,"COMMENTS")=

TFIEVAL(1,1,1,"CONDITION")=1

TFIEVAL(1,1,1,"CSUB","CLINICAL TERM")=

TFIEVAL(1,1,1,"CSUB","COMMENTS")=

TFIEVAL(1,1,1,"CSUB","DATE OF INJURY")=

TFIEVAL(1,1,1,"CSUB","MODIFIER")=

TFIEVAL(1,1,1,"CSUB","PRIMARY/SECONDARY")=S

TFIEVAL(1,1,1,"CSUB","PROBLEM LIST ENTRY")=

TFIEVAL(1,1,1,"CSUB","PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,1,"CSUB","VISIT")=5161991

TFIEVAL(1,1,1,"DAS")=3238132

TFIEVAL(1,1,1,"DATE")=3050615.103

TFIEVAL(1,1,1,"DATE OF INJURY")=

TFIEVAL(1,1,1,"FILE NUMBER")=9000010.07

TFIEVAL(1,1,1,"FILE SPECIFIC")=S

TFIEVAL(1,1,1,"FINDING")=52;PXD(811.2,

TFIEVAL(1,1,1,"MODIFIER")=

TFIEVAL(1,1,1,"PRIMARY/SECONDARY")=S

TFIEVAL(1,1,1,"PROBLEM LIST ENTRY")=

TFIEVAL(1,1,1,"PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,1,"VISIT")=5161991

TFIEVAL(1,1,2)=1

TFIEVAL(1,1,2,"CLINICAL TERM")=

TFIEVAL(1,1,2,"CODEP")=2507

TFIEVAL(1,1,2,"COMMENTS")=

TFIEVAL(1,1,2,"CONDITION")=1

TFIEVAL(1,1,2,"CSUB","CLINICAL TERM")=

TFIEVAL(1,1,2,"CSUB","COMMENTS")=

TFIEVAL(1,1,2,"CSUB","DATE OF INJURY")=

TFIEVAL(1,1,2,"CSUB","MODIFIER")=

TFIEVAL(1,1,2,"CSUB","PRIMARY/SECONDARY")=P

TFIEVAL(1,1,2,"CSUB","PROBLEM LIST ENTRY")=

TFIEVAL(1,1,2,"CSUB","PROVIDER NARRATIVE")=1082

TFIEVAL(1,1,2,"CSUB","VISIT")=3970337

TFIEVAL(1,1,2,"DAS")=1896973

TFIEVAL(1,1,2,"DATE")=3020913.131038

TFIEVAL(1,1,2,"DATE OF INJURY")=

TFIEVAL(1,1,2,"FILE NUMBER")=9000010.07

TFIEVAL(1,1,2,"FILE SPECIFIC")=P

TFIEVAL(1,1,2,"FINDING")=52;PXD(811.2,

TFIEVAL(1,1,2,"MODIFIER")=

TFIEVAL(1,1,2,"PRIMARY/SECONDARY")=P

TFIEVAL(1,1,2,"PROBLEM LIST ENTRY")=

TFIEVAL(1,1,2,"PROVIDER NARRATIVE")=1082

TFIEVAL(1,1,2,"VISIT")=3970337

TFIEVAL(1,1,3)=1

TFIEVAL(1,1,3,"CLINICAL TERM")=

TFIEVAL(1,1,3,"CODEP")=2507

TFIEVAL(1,1,3,"COMMENTS")=

TFIEVAL(1,1,3,"CONDITION")=1

TFIEVAL(1,1,3,"CSUB","CLINICAL TERM")=

TFIEVAL(1,1,3,"CSUB","COMMENTS")=

TFIEVAL(1,1,3,"CSUB","DATE OF INJURY")=

TFIEVAL(1,1,3,"CSUB","MODIFIER")=

TFIEVAL(1,1,3,"CSUB","PRIMARY/SECONDARY")=P

TFIEVAL(1,1,3,"CSUB","PROBLEM LIST ENTRY")=

TFIEVAL(1,1,3,"CSUB","PROVIDER NARRATIVE")=1082

TFIEVAL(1,1,3,"CSUB","VISIT")=3967489

TFIEVAL(1,1,3,"DAS")=1893712

TFIEVAL(1,1,3,"DATE")=3020911.131046

TFIEVAL(1,1,3,"DATE OF INJURY")=

TFIEVAL(1,1,3,"FILE NUMBER")=9000010.07

TFIEVAL(1,1,3,"FILE SPECIFIC")=P

TFIEVAL(1,1,3,"FINDING")=52;PXD(811.2,

TFIEVAL(1,1,3,"MODIFIER")=

TFIEVAL(1,1,3,"PRIMARY/SECONDARY")=P

TFIEVAL(1,1,3,"PROBLEM LIST ENTRY")=

TFIEVAL(1,1,3,"PROVIDER NARRATIVE")=1082

TFIEVAL(1,1,3,"VISIT")=3967489

TFIEVAL(1,1,"CLINICAL TERM")=

TFIEVAL(1,1,"CODEP")=12989

TFIEVAL(1,1,"COMMENTS")=

TFIEVAL(1,1,"CONDITION")=1

TFIEVAL(1,1,"CSUB","CLINICAL TERM")=

TFIEVAL(1,1,"CSUB","COMMENTS")=

TFIEVAL(1,1,"CSUB","DATE OF INJURY")=

TFIEVAL(1,1,"CSUB","MODIFIER")=

TFIEVAL(1,1,"CSUB","PRIMARY/SECONDARY")=S

TFIEVAL(1,1,"CSUB","PROBLEM LIST ENTRY")=

TFIEVAL(1,1,"CSUB","PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,"CSUB","VISIT")=5161991

TFIEVAL(1,1,"DAS")=3238132

TFIEVAL(1,1,"DATE")=3050615.103

TFIEVAL(1,1,"DATE OF INJURY")=

TFIEVAL(1,1,"FILE NUMBER")=9000010.07

TFIEVAL(1,1,"FILE SPECIFIC")=S

TFIEVAL(1,1,"FINDING")=52;PXD(811.2,

TFIEVAL(1,1,"MODIFIER")=

TFIEVAL(1,1,"PRIMARY/SECONDARY")=S

TFIEVAL(1,1,"PROBLEM LIST ENTRY")=

TFIEVAL(1,1,"PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,"VISIT")=5161991

Formatted Output:

--STATUS-- --DUE DATE--  --LAST DONE--

IHD Lipid Profile                    DUE NOW     DUE NOW       unknown

Frequency: Due every 1 year

Cohort:

Reminder Term: VA-IHD DIAGNOSIS

Encounter Diagnosis:

06/15/2005 414.00 COR ATHEROSCL UNSP TYP-VES rank: SECONDARY

09/13/2002 414.9 CHR ISCHEMIC HRT DIS NOS rank: PRIMARY

Prov. Narr. - CHRONIC ISCHEMIC HEART DISEASE, UNSPECIFIED

09/11/2002 414.9 CHR ISCHEMIC HRT DIS NOS rank: PRIMARY

Prov. Narr. - CHRONIC ISCHEMIC HEART DISEASE, UNSPECIFIED

Parts of the reminder test have been removed for brevity’s sake. Under the Term Evaluation part of the reminder test, you will notice the TFIEVAL and subscripts. This looks very similar to the results of the FIEVAL, except that it is the results of each mapped finding within the term. There is a minimum of two subscripts for each mapped finding. The first subscript is the number of the actual finding (the term). The second subscript is the number of the mapped finding. In this instance, the evaluation of the mapped finding is “True.”

TFIEVAL(1,1)=1

Sometimes there may be three subscripts. This third subscript is the occurrence of the mapped finding.

In the above example (the complete reminder test output), you will notice there are three occurrences for mapped finding number 1. This is because the reminder term has an occurrence count of 3. This is also displayed in the clinical maintenance section of the reminder test output.

**Note** : The “CSUB” values of an occurrence of a mapped finding can be used in a Condition of a finding just as the “CSUB” values of a regular finding can be.

TFIEVAL(1,1,1)=1

TFIEVAL(1,1,1,"CLINICAL TERM")=

TFIEVAL(1,1,1,"CODEP")=12989

TFIEVAL(1,1,1,"COMMENTS")=

TFIEVAL(1,1,1,"CONDITION")=1

TFIEVAL(1,1,1,"CSUB","CLINICAL TERM")=

TFIEVAL(1,1,1,"CSUB","COMMENTS")=

TFIEVAL(1,1,1,"CSUB","DATE OF INJURY")=

TFIEVAL(1,1,1,"CSUB","MODIFIER")=

TFIEVAL(1,1,1,"CSUB","PRIMARY/SECONDARY")=S

TFIEVAL(1,1,1,"CSUB","PROBLEM LIST ENTRY")=

TFIEVAL(1,1,1,"CSUB","PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,1,"CSUB","VISIT")=5161991

TFIEVAL(1,1,1,"DAS")=3238132

TFIEVAL(1,1,1,"DATE")=3050615.103

TFIEVAL(1,1,1,"DATE OF INJURY")=

TFIEVAL(1,1,1,"FILE NUMBER")=9000010.07

TFIEVAL(1,1,1,"FILE SPECIFIC")=S

TFIEVAL(1,1,1,"FINDING")=52;PXD(811.2,

TFIEVAL(1,1,1,"MODIFIER")=

TFIEVAL(1,1,1,"PRIMARY/SECONDARY")=S

TFIEVAL(1,1,1,"PROBLEM LIST ENTRY")=

TFIEVAL(1,1,1,"PROVIDER NARRATIVE")=3906

TFIEVAL(1,1,1,"VISIT")=5161991

1. This section shows the cohort logic, reminder name, resolution logic, and how the frequency was determined. If contraindicated logic and resolution logic have been defined, they will be displayed in this section.

The elements of the ^TMP(PXRMID,$J) array are:

^TMP(PXRMID,$J,660020,"PATIENT COHORT LOGIC")=1^(SEX)&amp;(AGE)^(1)&amp;(1)

^TMP(PXRMID,$J,660020,"REMINDER NAME")=Education Test

^TMP(PXRMID,$J,660020,"RESOLUTION LOGIC")=0^(0)!FI(2)&amp;FF(1)&amp;FF(3)^(0)!1&amp;0&amp;1

^TMP(PXRMID,$J,660020,"zFREQARNG")=1Y^61^70^Baseline

The first piece of the logic display shows if the logic evaluates to true or false. In this example, the cohort logic is true and the resolution logic is false. The second piece shows the logic string just like it is displayed in the reminder inquiry. The third piece shows the true or false values of the findings in the logic string.

1. The next section shows how the data is returned in ^TMP(“PXRHM”,$J) to the calling application. This is mainly of interest to developers.

The elements of the ^TMP("PXRHM",$J) array are:

^TMP("PXRHM",$J,660020,"Education Test")=DUE NOW^DUE NOW^unknown

^TMP("PXRHM",$J,660020,"Education Test","TXT",1)=Frequency: Due every 1 year for

ages 61 to 70.

^TMP("PXRHM",$J,660020,"Education Test","TXT",2)=Patient is not in age range. Li

ne 2

^TMP("PXRHM",$J,660020,"Education Test","TXT",3)=This is match text for 61 to 70

. The patient's age is 62.

^TMP("PXRHM",$J,660020,"Education Test","TXT",4)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",5)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",6)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",7)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",8)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",9)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",10)=This is the general cohort fou

nd text. The patient's age is 62.

^TMP("PXRHM",$J,660020,"Education Test","TXT",11)=The patient's active medicatio

ns are: Active Outpatient Medications (excluding

^TMP("PXRHM",$J,660020,"Education Test","TXT",12)=Supplies):

^TMP("PXRHM",$J,660020,"Education Test","TXT",13)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",14)=     Pending Outpatient Medica

tions                         Status

^TMP("PXRHM",$J,660020,"Education Test","TXT",15)===============================

===========================================

^TMP("PXRHM",$J,660020,"Education Test","TXT",16)=1)   ACETAMINOPHEN ELIXIR 160M

G/5ML 16OZ TAKE 1 TABLET BY   PENDING

^TMP("PXRHM",$J,660020,"Education Test","TXT",17)=       MOUTH TWICE A DAY

^TMP("PXRHM",$J,660020,"Education Test","TXT",18)=2)   ERGOTAMINE &amp; CAFFEINE SUP

P. INSERT Y SUPPOSITORY(IES)  PENDING

^TMP("PXRHM",$J,660020,"Education Test","TXT",19)=       IN RECTUM

^TMP("PXRHM",$J,660020,"Education Test","TXT",20)=3)   HYDROCHLOROTHIAZIDE 50MG

TAKE ONE TABLET BY MOUTH      PENDING

^TMP("PXRHM",$J,660020,"Education Test","TXT",21)=       EVERY DAY

^TMP("PXRHM",$J,660020,"Education Test","TXT",22)=4)   WARFARIN 2.5MG TAKE ONE T

ABLET BY MOUTH TWICE A DAY    PENDING

^TMP("PXRHM",$J,660020,"Education Test","TXT",23)=       FOR 6 DAYS, THEN TAKE O

NE TABLET EVERY DAY FOR 2

^TMP("PXRHM",$J,660020,"Education Test","TXT",24)=       DAYS

^TMP("PXRHM",$J,660020,"Education Test","TXT",25)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",26)=     Active Non-VA Medications

Status

^TMP("PXRHM",$J,660020,"Education Test","TXT",27)===============================

===========================================

^TMP("PXRHM",$J,660020,"Education Test","TXT",28)=1)   Non-VA ACETAMINOPHEN 325M

G 650MG MOUTH EVERY 4 HOURS   ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",29)=2)   Non-VA ACETAMINOPHEN ELIX

IR 160MG/5ML 16OZ 1 TABLET    ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",30)=       MOUTH

^TMP("PXRHM",$J,660020,"Education Test","TXT",31)=3)   Non-VA ACETAMINOPHEN/CODE

INE TAB  MOUTH                ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",32)=4)   Non-VA ACETAMINOPHEN/PROP

OXYPHENE TAB  MOUTH           ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",33)=5)   Non-VA ACETAZOLAMIDE CAP,

SA  MOUTH                     ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",34)=6)   Non-VA ACETIC ACID OTIC S

OLN 2%, 60ML 2 DROPS RIGHT    ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",35)=       EAR

^TMP("PXRHM",$J,660020,"Education Test","TXT",36)=7)   Non-VA ACETOHEXAMIDE TAB

1JFKDJF MOUTH 6XD             ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",37)=8)   Non-VA ACTICORT LOTION,TO

P  AFFECTED AREA              ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",38)=9)   Non-VA ACYCLOVIR 5% OINT

15GM LEG AFFECTED AREA EVERY  ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",39)=       4 HOURS

^TMP("PXRHM",$J,660020,"Education Test","TXT",40)=10)  Non-VA ACYCLOVIR CAP,ORAL

3M ORAL DAILY                ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",41)=11)  Non-VA LINDANE SHAMPOO  A

FFECTED AREA                  ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",42)=12)  Non-VA TRETINOIN CREAM,TO

P                             ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",43)=13)  Non-VA ZZDOCUSATE CAP,ORA

L TES MOUTH                   ACTIVE

^TMP("PXRHM",$J,660020,"Education Test","TXT",44)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",45)=17 Total Medications

^TMP("PXRHM",$J,660020,"Education Test","TXT",46)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",47)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",48)=This is the general resolution

not found text. Second line of not found. Third

^TMP("PXRHM",$J,660020,"Education Test","TXT",49)=line of not found.

^TMP("PXRHM",$J,660020,"Education Test","TXT",50)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",51)=Resolution:

^TMP("PXRHM",$J,660020,"Education Test","TXT",52)= Education Topic: Exercise Scr

eening

^TMP("PXRHM",$J,660020,"Education Test","TXT",53)=  03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",54)=  01/06/2000@13:15:24 level of

understanding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",55)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",56)=  VA-EXERCISE SCREENING FOUND

TEXT. Lets test out some objects. The patient was

^TMP("PXRHM",$J,660020,"Education Test","TXT",57)=  seen on 03/17/00 08:00. His

last blood pressure was Blood Pressure: 120/76

^TMP("PXRHM",$J,660020,"Education Test","TXT",58)=  (01/11/2001 19:24). Test an

extra pipe The OBJECT . His last height and

^TMP("PXRHM",$J,660020,"Education Test","TXT",59)=  weight was  was NOT found...

Contact IRM.PATIENT HEIGHTThe OBJECT  and  was

^TMP("PXRHM",$J,660020,"Education Test","TXT",60)=  NOT found...Contact IRM.PATI

ENT WEIGHTThe OBJECT . was NOT found...Contact

^TMP("PXRHM",$J,660020,"Education Test","TXT",61)=  IRM.

^TMP("PXRHM",$J,660020,"Education Test","TXT",62)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",63)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",64)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",65)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",66)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",67)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",68)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",69)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",70)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",71)=  FF(1)=0

^TMP("PXRHM",$J,660020,"Education Test","TXT",72)=  Function finding 1 not found

text, patient's age is 62.

^TMP("PXRHM",$J,660020,"Education Test","TXT",73)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",74)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",75)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",76)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",77)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",78)=  FF(3)=1

^TMP("PXRHM",$J,660020,"Education Test","TXT",79)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",80)=Information:

^TMP("PXRHM",$J,660020,"Education Test","TXT",81)= Education Topic: Substance Ab

use

^TMP("PXRHM",$J,660020,"Education Test","TXT",82)=  07/00/1998

^TMP("PXRHM",$J,660020,"Education Test","TXT",83)=  00/00/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",84)=  02/02/2000@15:00 level of un

derstanding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",85)=  02/17/2000@08:59:26 level of

understanding - GOOD

^TMP("PXRHM",$J,660020,"Education Test","TXT",86)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",87)= Education Topic: Exercise

^TMP("PXRHM",$J,660020,"Education Test","TXT",88)=  03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",89)=  00/00/2000

^TMP("PXRHM",$J,660020,"Education Test","TXT",90)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",91)= Education Topic: Diabetes

^TMP("PXRHM",$J,660020,"Education Test","TXT",92)=  03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",93)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",94)= Reminder Term: EDUTEST

^TMP("PXRHM",$J,660020,"Education Test","TXT",95)=  Education Topic: Substance A

buse

^TMP("PXRHM",$J,660020,"Education Test","TXT",96)=   03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",97)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",98)=  Education Topic: Exercise Sc

reening

^TMP("PXRHM",$J,660020,"Education Test","TXT",99)=   03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",100)=

^TMP("PXRHM",$J,660020,"Education Test","TXT",101)=  Education Topic: Exercise

^TMP("PXRHM",$J,660020,"Education Test","TXT",102)=   03/17/2000@08:00

^TMP("PXRHM",$J,660020,"Education Test","TXT",103)=

1. The final section shows the formatted Clinical Maintenance output. This is what you would see in CPRS or Health Summary.

Maintenance Output:

--STATUS-- --DUE DATE--  --LAST DONE--

Education Test                       DUE NOW     DUE NOW       unknown

Frequency: Due every 1 year for ages 61 to 70.

Patient is not in age range. Line 2

This is match text for 61 to 70. The patient's age is 62.

This is the general cohort found text. The patient's age is 62.

The patient's active medications are: Active Outpatient Medications (excluding

Supplies):

Pending Outpatient Medications                         Status

=========================================================================

1)   ACETAMINOPHEN ELIXIR 160MG/5ML 16OZ TAKE 1 TABLET BY   PENDING

MOUTH TWICE A DAY

2)   ERGOTAMINE &amp; CAFFEINE SUPP. INSERT Y SUPPOSITORY(IES)  PENDING

IN RECTUM

3)   HYDROCHLOROTHIAZIDE 50MG TAKE ONE TABLET BY MOUTH      PENDING

EVERY DAY

4)   WARFARIN 2.5MG TAKE ONE TABLET BY MOUTH TWICE A DAY    PENDING

FOR 6 DAYS, THEN TAKE ONE TABLET EVERY DAY FOR 2

DAYS

Active Non-VA Medications                              Status

=========================================================================

1)   Non-VA ACETAMINOPHEN 325MG 650MG MOUTH EVERY 4 HOURS   ACTIVE

2)   Non-VA ACETAMINOPHEN ELIXIR 160MG/5ML 16OZ 1 TABLET    ACTIVE

MOUTH

3)   Non-VA ACETAMINOPHEN/CODEINE TAB  MOUTH                ACTIVE

4)   Non-VA ACETAMINOPHEN/PROPOXYPHENE TAB  MOUTH           ACTIVE

5)   Non-VA ACETAZOLAMIDE CAP,SA  MOUTH                     ACTIVE

6)   Non-VA ACETIC ACID OTIC SOLN 2%, 60ML 2 DROPS RIGHT    ACTIVE

EAR

7)   Non-VA ACETOHEXAMIDE TAB 1JFKDJF MOUTH 6XD             ACTIVE

8)   Non-VA ACTICORT LOTION,TOP  AFFECTED AREA              ACTIVE

9)   Non-VA ACYCLOVIR 5% OINT 15GM LEG AFFECTED AREA EVERY  ACTIVE

4 HOURS

10)  Non-VA ACYCLOVIR CAP,ORAL 3M ORAL DAILY                ACTIVE

11)  Non-VA LINDANE SHAMPOO  AFFECTED AREA                  ACTIVE

12)  Non-VA TRETINOIN CREAM,TOP                             ACTIVE

13)  Non-VA ZZDOCUSATE CAP,ORAL TES MOUTH                   ACTIVE

17 Total Medications

This is the general resolution not found text. Second line of not found. Third

line of not found.

Resolution:

Education Topic: Exercise Screening

03/17/2000@08:00

01/06/2000@13:15:24 level of understanding - GOOD

VA-EXERCISE SCREENING FOUND TEXT. Lets test out some objects. The patient was

seen on 03/17/00 08:00. His last blood pressure was Blood Pressure: 120/76

(01/11/2001 19:24). Test an extra pipe The OBJECT . His last height and

weight was  was NOT found...Contact IRM.PATIENT HEIGHTThe OBJECT  and  was

NOT found...Contact IRM.PATIENT WEIGHTThe OBJECT . was NOT found...Contact

IRM.

FF(1)=0

Function finding 1 not found text, patient's age is 62.

FF(3)=1

Information:

Education Topic: Substance Abuse

07/00/1998

00/00/2000

02/02/2000@15:00 level of understanding - GOOD

02/17/2000@08:59:26 level of understanding - GOOD

Education Topic: Exercise

03/17/2000@08:00

00/00/2000

Education Topic: Diabetes

03/17/2000@08:00

Reminder Term: EDUTEST

Education Topic: Substance Abuse

03/17/2000@08:00

Education Topic: Exercise Screening

03/17/2000@08:00

Education Topic: Exercise

03/17/2000@08:00

#### Reminder Evaluation in CPRS

There are two forms of the Reminder Evaluation option, for use before and after processing reminders.

**Evaluate Reminder**

Before you process a reminder, you can select this option to see if specific reminders in the Other Category folder should be Applicable or should be Due for the selected patient.

For example, in a diabetic clinic, you might see a patient around flu season and evaluate the flu shot reminder in the other category to see if a flu shot is needed.

To evaluate reminders, right-click in a tree view (from the Reminders Button or Drawer) and select Evaluate Reminder.

**Evaluate Processed Reminders**

After you have processed a reminder, you can use this option to see if your actions during the encounter satisfied the reminder.

Satisfying a reminder may require more than you originally think. You may want to evaluate the reminders after you have processed them to make sure you have satisfied the reminder.

**NOTE** : PCE data may take a few minutes to be correctly recorded. Please wait a few minutes after processing a reminder before evaluating it again to ensure that it was satisfied.

To evaluate processed reminders, choose Action in the Available Reminders window, and then click on Evaluate Processed Reminders.

**General Testing of Clinical Reminders**

The accuracy of clinical display of reminders as well as the accuracy of reports is dependent upon creation and implementation of accurate reminders. One critical role of the reminders champion is assisting the clinical informatics specialist in testing the reminder.

In general, when testing a clinical reminder, you want to test the reminder on patients who fit the cohort definition as well as on patients who do NOT fit the cohort definition. Is the reminder applicable when it should be? You also want to test the reminder for patients who are in cohort and have the reminder resolved as well as for patients who are in cohort and do NOT have the reminder resolved. In the first round, this is usually best done using test patients set up by clinical informatics. This is usually done in a test account which is a mirror image of the production account at your site.

Testing can be done by using the reminder test option. Reminder Test is a clinical reminders menu option available in VistA, which gives detailed, technical information on findings, file locations where the data has been found, logic and other highly technical information.

Most clinicians will find using CPRS to determine if the reminder is due most helpful. The information in the Reminder Maintenance can be analyzed during testing as well as troubleshooting to determine why a specific reminder is due for a specific patient and what resolves the reminder.

An important step is testing the reminder Dialog. The clinician should test all groups and elements in a dialog to ensure that the dialog text is clear, concise, and accurate and that the dialog works as expected. Next, the dialog should be carefully tested to ensure that the progress note text which is inserted is clear, concise, and accurate. Checking the spelling is tedious but important.

The dialog should also be tested to analyze if anything is missing. Think like a clinician: When I see patients in the clinic, which patients obviously can’t have this procedure either because it is impossible or it is not indicated. A clear example is the diabetic foot exam. On first pass, most clinicians would say it’s due for ALL patients with diabetes. However, it is technically impossible to perform a monofilament exam on a patient with bilateral amputation. It is also not clinically useful to perform this exam on a diabetic with a spinal cord injury which has resulted in loss of sensation to the lower extremities.

Assuming the reminder passes the testing in the first phase, it is reasonable to move on to a second phase in the test account using reminders reports

Run detailed reports for short interval in a clinic where you would expect to have the reminder due. For example;

- Diabetes clinic for A1C&gt;9 (Many uncontrolled diabetics would expect to be referred to diabetes clinic)
- Comp and Pension Clinic (high likelihood of patients who are not enrolled in primary care and may not have had reminders addressed)

Run a report listing all patients in the clinic. Check CPRS for accuracy for patients who have the reminder due and who do not have the reminder due.

Run summary and/or detailed reports in a clinic where you expect a specific reminder to be resolved. Example:

- There is a high likelihood that close to 100% of all patients seen in Retinal clinic have had a retinal examination done.

Another good clinic to check is a primary care provider whom you know to be diligent in processing clinical reminders who also has stable patient panel and is not seeing a lot of new patients.

Clinically review records as needed.

### Other Supporting Menus

This menu and its options are included on the Clinical Reminders Manager Menu to provide easier access to related tools from other **V** *IST* **A** packages for setting up and maintaining clinical reminders.

| **Syno-nym**   | **Option**                        | **Option Name**                | **Description**                                                                                                                                                                                                                                                                                                                                                                              |
|----------------|-----------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TM             | PCE Table Maintenance             | PXTT TABLE MAINTENANCE         | The options on this menu are used to add or edit the clinical terminology used to represent types of data to be collected by PCE such as Health Factors, Patient Education, Immunizations, Skin Tests, etc.                                                                                                                                                                                  |
| PC             | PCE Coordinator Menu              | PX PCE COORDINATOR MENU        | This menu for PCE ADPACS includes all of the user interface options as well as the options for file maintenance.                                                                                                                                                                                                                                                                             |
| HS             | Health Summary Coordinator's Menu | GMTS COORDINATOR               | This menu includes options for creating Health Summaries, Health Summary Types, and the option to set parameters for nightly batch printing of Health Summaries by Location.  NOTE: When making Clinical Reminder option assignments, consider the assignment of the GMTS COORDINATOR menu option as a separate issue, leaving it or removing it from the Clinical Reminder menu as desired. |
| EF             | Print Blank Encounter Form        | IBDF PRINT BLNK ENCOUNTER FORM | This option allows the user to select a clinic, and if an encounter form is defined for use with an embossed patient card, the form will be printed.                                                                                                                                                                                                                                         |
| QO             | Enter/edit quick orders           | ORCM QUICK ORDERS              | This option lets you create or change quick orders.                                                                                                                                                                                                                                                                                                                                          |

### Reminder Information Only Menu

This menu contains options for users who need information about reminders, but do not need the ability to make changes. Most of the options are described previously in this manual.

| **Syno-nym**   | **Option**                        | **Option Name**         | **Description**                                                                                 |
|----------------|-----------------------------------|-------------------------|-------------------------------------------------------------------------------------------------|
| RL             | List Reminder Definitions         | PXRM DEFINITION LIST    | This option provides a brief summary of selected Clinical Reminder definitions.                 |
| RI             | Inquire about Reminder Definition | PXRM DEFINITION INQUIRY | Allows a user to display a clinical reminder definition in an easy to read format.              |
| TRL            | List Reminder Terms               | PXRM TERM LIST          | This option is used to give a brief listing of reminder terms.                                  |
| TRI            | Inquire about Reminder Term       | PXRM TERM  INQUIRY      | This option allows a user to display the contents of a reminder term in an easy to read format. |
| SL             | List Reminder Sponsors            | PXRM SPONSOR LIST       | This option is used to get a list of Reminder Sponsors.                                         |

### Reminder Dialog Management

Reminder Dialogs are used in CPRS to allow clinicians to select actions that satisfy or resolve reminders for a patient. Information entered through reminder dialogs update progress notes, place orders, and update other data in the patient’s medical record.

A reminder dialog is created by the assembly of elements in groups into an orderly display, which is seen by the user in the CPRS GUI.

**Changes to Reminder Dialogs in Patch 26**

Dialogs Will Now Use Taxonomies Exclusively

- Individual codes will no longer be used as findings or additional findings
- Taxonomies for dialogs will be automatically generated
- Name example:
    - ICD9 250.53
- Description:
    - This taxonomy was automatically generated from Reminder Dialog IEN: 5343

- ***In the past*** , users created Reminder Dialogs containing ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog.
- A Taxonomy could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS. The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter. The controls also determined what prompts were assigned to the Reminder Dialog in CPRS.
    - ***New approach: Users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need*** to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new prompt called Taxonomy Pick List Display has been added to the dialog editor. This controls how Taxonomies should display in CPRS.
- When accessing a reminder dialog that contains an inactive taxonomy or a taxonomy that does not match the dialog structure, the taxonomy will not show in CPRS and a MailMan message will be sent to the Clinical Reminders mail group listing the problems with the dialog and the taxonomy.

- New checking functionality has been added. The checker is run automatically when the taxonomy is saved during an editing session, from the dialog checker report, and when packing up a dialog in Reminder Exchange. It will determine if there is a mismatch between a dialog and the taxonomy that is a finding item.

- Reminder dialogs will now allow taxonomies to be used in a group as a finding item. In a group the Taxonomy Pick List Display field can only be set to None, Procedure Only, or Diagnosis Only.

- The patch init conversion routine has been updated to give more detail when updating the dialog file. The conversion routine will also send pre and post-conversion messages listing the details of the dialogs that are being updated.

- Patch PXRM*2*26 will release updates to national dialogs that contain ICD and CPT codes. This also requires new taxonomies for the dialogs. These items will be installed using Reminder Exchange. The name of the Reminder Exchange file entry is File “PXRM PATCH 26 DIALOGS UPDATES”.

- When the VA-AAA SCREENING reminder dialog was released in patch PXRM*2*17, it included a new local forced value named ADD TO PROBLEM LIST. Patch PXRM*2*26 changes the forced value to national and renames it to PXRM FV ADD TO PROBLEM LIST.

#### Changes to Reminder Dialogs in Patch 45

- Branching Logic functionality has been enhanced to support additional actions, and to allow for multiple evaluations. A conversion routine will update the existing branching logic to the new structure
- Reminder Dialog Tester and Checker options have been added to the Reminder Dialog List Manager
- Performance improvements to Reminder Dialog processing
- Reminder Dialog Error Checking in the Editor

#### Steps to create a dialog

1. First, you create elements, which may include additional prompts, template fields, objects, or orders.

1. Next, organize the elements into groups.

3.   Then add the groups or single elements to the dialog.

4.   Once a dialog is created, you can link it to a reminder.

Reminder dialogs and all their related components are stored in the Reminder Dialog File #801.41. This file is used to define all of the components that work together to define a reminder dialog.

This file contains a combination of nationally distributed entries, local auto-generated entries, site, and VISN exchanged entries, and local manually created entries. Nationally distributed entries have their name prefixed with PXRM, “VA-“, or VA-L. Locally created dialog entries should use local namespacing conventions.

This file is similar to the option file where there are different types of entries (reminder dialog, dialog elements (sentences), prompts, and groups of elements, result elements and groups of result elements). Where an option has menu items, the dialog file has components that are entered with the sequence field as the .01 field.

#### Dialog Component Definitions

**Dialog Elements**

A dialog element is defined primarily to represent sentences to display in the CPRS window with a check box. When the user checks the sentence off, the FINDING ITEM in the dialog element and the ADDITIONAL FINDINGS will be added to the list of PCE updates, orders, vitals, mental health tests, and Women’s Health Notifications. The updates won't occur on the CPRS GUI until the user clicks on the FINISH button. Dialog elements may have components added to them. Auto-generated components will be based on the additional prompts defined in the Finding Type Parameters. Once a dialog element is auto-generated, sites can modify them.

Dialog elements may also be instructional text or a header. The FINDING ITEM and components would not be defined in dialog elements.

**Dialog Groups**

A dialog group is similar to a menu option. It groups dialog elements and dialog groups within its component multiple. The dialog group can be defined with a finding item and check-box. The components in the group can be hidden from the CPRS GUI window until the dialog group is checked off.

**Result Elements**

The result element is only used with mental health test finding items. A result element contains special logic that uses information entered during the resolution process to create a sentence to add to the progress note. The special logic contains a CONDITION that, when true, will use the ALTERNATE PROGRESS NOTE TEXT field to update the progress note. A separate result element is used for each separate sentence needed. Default result elements are distributed for common mental health tests, prefixed with PXRM and the mental health test name. Sites may copy them and modify their local versions as needed.

**Result Groups**

A result group contains all of the result elements that need to be checked to create sentences for one mental health test finding and one MH Scale. The dialog element for the test will have its RESULT GROUP field defined with the result group. Default result groups for mental health tests are distributed with the Clinical Reminders package. Sites may copy them and modify their local versions as needed.

**Prompts**

A prompt is used to have the user enter certain data for the patient. The data that is entered into the prompt will update the progress and the update other files (e.g., PXRM DATE would update the Vist file by creating a new encounter entries for an historical update). Some prompts can be restricted to certain finding items. PXRM WH NOTE TYPE will only work if the finding item or additional finding item is a WH Notification entry.

**Forced Value**

A forced value is way for forcing a certain type of update. A common use for a forced value is to automatically set a diagnosis as the primary diagnosis.

##### Reminder Dialog Management Menu

| **Syn.**   | **Name**          | **Option Name**             | **Description**                                                                                                                                                                                              |
|------------|-------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DP         | Dialog Parameters | PXRM DIALOG PARAMETERS      | This menu allows maintenance of parameters used in dialog generation:  RS - Resolution Statuses  FP - Finding Type Parameters  FI - Finding Item Parameters  HR - Health Factor Resolutions                  |
| DI         | Reminder Dialogs  | PXRM DIALOG/ COMPONENT EDIT | A reminder dialog contains questions (dialog elements) and/or groups of questions (dialog groups) that are related to the reminder findings. Dialog file entries may be created or amended with this option. |
| DR         | Dialog Reports    | PXRM DIALOG TOOLS MENU      | This sub-menu contains three options that can be used as dialog maintenance tools: Reminder Dialog Elements Orphan Report, Empty Reminder Dialog Report, and Check Reminder Dialog for invalid items         |

#### Dialog Parameters

Before you can create dialogs, the entries in the Dialog Parameters must be appropriate for the dialog you are creating. Although the autogeneration process inserts pre-defined elements from entries in the dialog parameters files, these may not all be appropriate for a specific dialog. Therefore, you should review these dialog parameters and edit them, as necessary.

| **Syn.**   | **Name**                        | **Option Name**                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|---------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RS         | Reminder Resolution Statuses    | PXRM RESOLUTION EDIT/INQ       | This option lists the hierarchy of resolution status values used by CPRS.                                                                                                                                                                                                                                                                                                                                                  |
| HR         | Health Factor Resolutions       | PXRM HEALTH FACTOR RESOLUTIONS | For each health factor, one or more resolution statuses may be selected. When generating a reminder dialog for a reminder with a health factor finding, dialog items will only be generated for the resolution statuses selected.                                                                                                                                                                                          |
| FP         | General Finding Type Parameters | PXRM PARAMETER EDIT            | This option lists the finding parameters used by Create Dialog from Reminder Definition.                                                                                                                                                                                                                                                                                                                                   |
| FI         | Finding Item Parameters         | PXRM FINDING ITEM              | If a reminder finding item will always be resolved by the same sentence  (dialog element) or set of sentences (dialog group), an entry should be made in the finding item parameter file linking the reminder finding item to the dialog element or group. When a reminder dialog is generated, it will include the sentences defined in this file  instead of generating a dialog using the FINDING TYPE PARAMETERS file. |

##### Reminder Resolution Statuses

Reminder resolution statuses are maintained using this option. A national set of resolution statuses is released with the reminder package. Local resolution statuses may be defined, but must be linked to a national status.

The first screen in this option displays the existing resolution statuses:

Selection List                      May 05, 2000 15:15:26     Page:    1 of    1

Reminder Resolution Status

Item Reminder Resolution Status        National/Local

1  CONTRAINDICATED                   NATIONAL

2  DONE AT ENCOUNTER                 NATIONAL

3  DONE ELSEWHERE (HISTORICAL)       NATIONAL

4  INACTIVATE                        NATIONAL

5  INFORMATIONAL                     NATIONAL

6  LOCAL                             LOCAL

7  ORDERED                           NATIONAL

8  OTHER                             NATIONAL

9  OTHER - DUE TO CLINICIAN DECISION LOCAL

10  OTHER - DUE TO COHORT AGE         LOCAL

11  PATIENT REFUSED                   NATIONAL

**+ Next Screen   - Prev Screen   ?? More Actions** AD   Add                  PT   List/Print All             QU   Quit

Select Item: Quit//

###### AD - Add a new local resolution status

Selection List              May 05, 2000 12:11:25          Page:    1 of    1

Reminder Resolution Status

Item Reminder Resolution Status        National/Local

1  CONTRAINDICATED                   NATIONAL

2  DONE AT ENCOUNTER                 NATIONAL

3  DONE ELSEWHERE (HISTORICAL)       NATIONAL

4  ORDERED                           NATIONAL

5  OTHER                             NATIONAL

6  PATIENT REFUSED                   NATIONAL

**+ Next Screen   - Prev Screen   ?? More Actions** AD   Add                  PT   List/Print All       QU   Quit

Select Item: Quit// **AD** Add

Select new RESOLUTION STATUS name: ?

Answer with REMINDER RESOLUTION STATUS NAME

Choose from:

CONTRAINDICATED

DONE AT ENCOUNTER

DONE ELSEWHERE (HISTORICAL)

ORDERED

OTHER

PATIENT REFUSED

You may enter a new REMINDER RESOLUTION STATUS, if you wish

Answer must be 3-40 characters in length.

Select new RESOLUTION STATUS name: OTHER-DUE TO LIFE EXPECTANCY

Are you adding 'OTHER-DUE TO LIFE EXPECTANCY' as

a new REMINDER RESOLUTION STATUS (the 7TH)? No// **Y** (Yes)

NAME: OTHER-DUE TO LIFE EXPECTANCY  Replace **&lt;Enter&gt;**

DESCRIPTION:

1&gt; **Other due to life expectancy**

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

ABBREVIATED NAME: **OTHER - LIFE EXPECT**

REPORT COLUMN HEADING: **OTHER - LIFE EXPECT**

INACTIVE FLAG: **&lt;Enter&gt;**

This resolution status must be linked to a national status

SELECT NATIONAL RESOLUTION STATUS: OTHER

...OK? Yes// **&lt;Enter&gt;** (Yes)

Selection List                  May 05, 2000 12:15:50          Page:    1 of    1

Reminder Resolution Status

Item Reminder Resolution Status        National/Local

1  CONTRAINDICATED                   NATIONAL

2  DONE AT ENCOUNTER                 NATIONAL

3  DONE ELSEWHERE (HISTORICAL)       NATIONAL

4  ORDERED                           NATIONAL

5  OTHER                             NATIONAL

6  OTHER-DUE TO LIFE EXPECTANCY      LOCAL

7  PATIENT REFUSED                   NATIONAL

**+ Next Screen   - Prev Screen   ?? More Actions** AD   Add                  PT   List/Print All       QU   Quit

Select Item: Quit// &lt;Enter&gt;

###### ED - Edit resolution status

When you select a specific resolution status (for example, #6 in the list above), details of that status are displayed. You can then perform any of the actions listed below on that status. National statuses may not be added or deleted. Column headings are used in Reminder Activity Reports. Local statuses must be mapped to a national status.

Edit List           May 05, 2000 12:18:05                    Page:    1 of    1

Reminder Resolution Status Name:  OTHER - DUE TO LIFE EXPECTANCY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Resolution Status: OTHER - DUE TO LIFE EXPECTANCY

Resolution Status Description

Other due to life expectancy.

Related National Status:  OTHER

Abbreviated name:  OTHER - LIFE EXPECT

Report Column Headings:  OTHER - LIFE EXPECT

Inactive Flag:

**+ Next Screen   - Prev Screen   ?? More Actions** ED   Edit                 INQ  Inquiry/Print        QU   Quit

Select Action: Quit// ED

Edit List                  May 05, 2000 12:18:05             Page:    1 of    1

REMINDER RESOLUTION STATUS NAME: OTHER-DUE TO LIFE EXPECTANCY

Resolution Status: OTHER-DUE TO LIFE EXPECTANCY

Resolution Status Description

Other due to life expectancy

Related National Status:  OTHER

Abbreviated name:  OTHER - LIFE EXPECT

Report Column Headings:  OTHER - LIFE EXPECT

Inactive Flag:

**+ Next Screen   - Prev Screen   ?? More Actions** ED   Edit                 INQ  Inquiry/Print        QU   Quit

Select Action: Quit// **ED** Edit

NAME: OTHER-DUE TO LIFE EXPECTANCY  Replace **&lt;Enter&gt;**

DESCRIPTION:

1&gt;Other due to life expectancy

EDIT Option: **&lt;Enter&gt;**

ABBREVIATED NAME: OTHER - LIFE EXPECT// **&lt;Enter&gt;**

REPORT COLUMN HEADING: OTHER - LIFE EXPECT// **OTHER - LIFE EXPECT** with **OTHER – LIFE EXP. &lt;Enter&gt;**

INACTIVE FLAG: **&lt;Enter&gt;**

Edit List                  May 05, 2000 12:20:02            Page:    1 of    1

REMINDER RESOLUTION STATUS NAME: OTHER-DUE TO LIFE EXPECTANCY

Resolution Status: OTHER-DUE TO LIFE EXPECTANCY

Resolution Status Description

Other due to life expectancy

Related National Status:  OTHER

Abbreviated name:  OTHER - LIFE EXPECT

Report Column Headings:  OTHER - LIFE EXP.

Inactive Flag:

**+ Next Screen   - Prev Screen   ?? More Actions** ED   Edit                 INQ  Inquiry/Print        QU   Quit

Select Action: Quit// **ED** Edit

NAME: OTHER-DUE TO LIFE EXPECTANCY  Replace **@**

SURE YOU WANT TO DELETE THE ENTIRE 'OTHER-DUE TO LIFE EXPECTANCY' REMINDER R **Y** (Yes)

##### General Finding Type Parameters (FP)

This option allows display of the REMINDER FINDING TYPE PARAMETER file #801.45 used in generating reminder dialogs. There is limited edit on this file to allow customization of prefix and suffix text. Parameters may also be disabled if not required at your site.

The file is structured by finding type and within that resolution status. A generated reminder dialog will include a sentence (dialog element) for each resolution type enabled in the finding type parameter file.

The sentence text is constructed as: prefix\_finding item name\_suffix. Health factors are treated slightly differently. Health factors are linked to resolution statuses by the Health Factor Resolutions option. For reminders with health factors, sentences are only generated if there is a resolution mapping AND an enabled finding type parameter.

The first screen in this option displays the finding types held in this file:

<!-- image -->

Selection List                May 05, 2000 16:06:40          Page:    1 of    1

Finding Type Parameters

Item Finding Type Parameter

1  PROCEDURE (CPT)

2  EDUCATION TOPICS

3  EXAM

4  HEALTH FACTOR

5  IMMUNIZATION

6  ORDERABLE ITEM

7  DIAGNOSIS (POV)

8  SKIN TEST

9  VITAL MEASUREMENT

**+ Next Screen   - Prev Screen   ?? More Actions** PT   List/Print All             QU   Quit

Select Item: Quit//

When you select an item from this screen, all of the finding type parameters for the finding type selected are displayed. The reminder dialog generation process uses this file to create dialog as follows:

For each finding item on the reminder, the REMINDER FINDING TYPE PARAMETER file is checked to see if there are any “enabled” resolution statuses for the finding type. If an enabled resolution status exists, then a dialog element (sentence) is added to the reminder dialog with sentence text generated from the finding name concatenated with prefix and suffix text

Example: Patient had ALCOHOL USE education at this encounter

Clicking on the checkbox displayed with this sentence in CPRS causes the finding item (from the original reminder definition) to be posted to this patient’s record.

Additional prompts are also added to the dialog element as specified in the finding type parameter file.

**Note:** Dialog elements created by reminder dialog generation are given a standard name based on the finding type, finding name, and resolution status (from the REMINDER FINDING TYPE PARAMETER file)

**Example: ED ALCOHOL USE DONE ELSEWHERE**

The dialog elements created are shared by reminder dialogs for reminders with the same finding item.

The example below is the finding type parameter for education findings:

Finding Type Parameter List        May 05, 2000 16:11:10     Page:    1 of    1

Finding Type Parameter Name: ED - EDUCATION TOPIC

Resolution Status         Prefix//Suffix &amp; Prompts/Values/Actions   Status

1 DONE AT ENCOUNTER          Patient had/                            Enabled

/at this encounter

1] PXRM COMMENT

2] PXRM LOU (EDUCATION)

2 DONE ELSEWHERE (HISTORICAL)Patient indicated/                     Disabled

/was received outside the VA

1] PXRM COMMENT

2] PXRM VISIT DATE

3] PXRM OUTSIDE LOCATION

3 PATIENT REFUSED            Patient declined/                      Disabled

/at this encounter

1] PXRM REFUSED (forced value)

2] PXRM COMMENT

**+ Next Screen   - Prev Screen   ?? More Actions** INQ  Inquiry/Print        QU   Quit

Select number of Resolution Status to Edit: Quit//

If a number is entered to select a resolution status, the following fields can be edited:

ED - EDIT FINDING TYPE PARAMETER

Finding Type Parameter Name: ED - EDUCATION TOPIC

RESOLUTION STATUS : DONE AT ENCOUNTER

DISABLE RESOLUTION STATUS: DISABLED// &lt;Enter&gt;

PREFIX TEXT: Patient had// **&lt;Enter&gt;**

SUFFIX TEXT: at this encounter// **&lt;Enter&gt;**

Select ADDITIONAL PROMPTS: PXRM LOU (EDUCATION)// **&lt;Enter&gt;**

DISABLE ADDITIONAL PROMPT: **&lt;Enter&gt;**

OVERRIDE PROMPT CAPTION: **&lt;Enter&gt;**

START NEW LINE: **&lt;Enter&gt;**

EXCLUDE FROM PN TEXT: **&lt;Enter&gt;**

REQUIRED: **&lt;Enter&gt;**

###### Finding Item Parameters (FI)

This file allows reminder finding items to be linked to a specific dialog element (i.e. sentence and prompts) or a group of dialog elements. The reminder dialog generated for a reminder with a finding item entry in this file will include the dialog element or dialog group specified in this file instead of creating a dialog using the REMINDER FINDING TYPE PARAMETER file.

The first screen in this option displays the finding items held in this file:

Selection List                May 05, 2000 10:35:36          Page:    1 of    1

Finding Item Parameters

Item Finding Item Type &amp; Name          Dialog Group/Element           Status

1  HF-ED SUBSTANCE ABUSE (OVERRIDE)  ED SUBSTANCE ABUSE REFUSED     Enabled

2  HF-ALCOHOL                        ALCOHOL DIALOG GROUP           Disabled

**+ Next Screen   - Prev Screen   ?? More Actions** AD   Add                  PT   List/Print All             QU   Quit

Select Item: Quit//

When you select a specific finding item parameter, details of the selected finding item parameter are displayed. You can then edit:

Edit List                    May 05, 2000 10:48:25       Page:    1 of    1

Finding Item Parameter Name:  ALCOHOL  (ENABLED)

Finding Type: HF(6)         Finding Item: ALCOHOL

Dialog Group: ALCOHOL DIALOG GROUP  (ENABLED)

1) Dialog Element: HF BINGE DRINKING OTHER  (ENABLED)

Dialog Text: Binge drinking

Additional Prompts: PXRM COMMENT

2) Dialog Element: HF DRINKING ALONE OTHER  (ENABLED)

Dialog Text: Drinking alone

Additional Prompts: PXRM COMMENT

**+ Next Screen   - Prev Screen   ?? More Actions** ED   Edit                 INQ  Inquiry/Print        QU   Quit

Select Action: Quit//

In the example above, the dialog elements have been previously generated automatically as part of another reminder dialog. A dialog group (ALCOHOL DIALOG GROUP) has then been created in Dialog Edit using these existing dialog elements. Finally an entry has been created in the finding item parameter to link HF(6) to the dialog group.

##### Reminder Dialogs

Use this option to create and edit Dialog file entries. When you first select the option, all of the available reminders at your facility are listed, with linked dialogs, if they exist, and dialog statuses. You can select a reminder by name or number and then autogenerate a dialog for the reminder or link the reminder to an existing dialog. Alternatively, you can select the action CV Change View, which will allow you to select from any of the following:

**Dialog types**

D - Reminder Dialogs

E - Dialog Elements

F - Forced Values

G - Dialog Groups

P - Additional Prompts

R - Reminders

RG - Result Group (Mental Health)

RE - Result Element (Mental Health)

Reminder dialogs are linked to reminders by a field (REMINDER DIALOG) on the reminder definition. The reminder dialog may be executed by CPRS if the reminder is due or applicable.

A reminder dialog contains questions (dialog elements) and/or groups of questions (dialog groups) that are related to the reminder findings.

Dialog groups can contain one or more questions (dialog elements).

Each question (dialog element) may have a number of additional prompts (e.g. date, location) or forced values.

New reminder dialogs can be created using the action, AD - Add Dialog, in the Dialog view.

The reminder dialog may be created manually or autogenerated from the reminder definition using the General Finding Type Parameters.

##### Dialog Edit screen

When you select an existing reminder dialog, the following actions are available:

| **Abbrev**   | **Action Name**                           | **Description**                                                                                                                                                                                 |
|--------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #            | Select Item                               | To copy, edit or delete a component in this dialog.                                                                                                                                             |
| ADD          | Add Element/Group                         | Allows a dialog element or dialog group to be added to the reminder dialog.                                                                                                                     |
| CO           | Copy Dialog                               | Copies this reminder dialog to a new name.                                                                                                                                                      |
| DD           | Detailed Display                          | Displays dialog element names and resolution detail for this reminder dialog.                                                                                                                   |
| DP           | Progress Note Text                        | Displays text that will be entered in the progress note.                                                                                                                                        |
| DS           | Dialog Summary (default)                  | Displays dialog element names.                                                                                                                                                                  |
| DO           | Dialog Overview                           | Displays the top-level dialog groups/elements. This option will not display any nested dialog elements or group                                                                                 |
| DT           | Dialog Text                               | Displays the dialog text as it should appear in CPRS.                                                                                                                                           |
| TEST         | Dialog Test                               | Displays how the dialog will appear in CPRS based on current patient data. This can help you see what happens with branching logic.                                                             |
| CHCK         | Dialog Checker                            | This option checks a selected reminder  dialog for invalid sub dialog items, invalid finding items, invalid TIU  Objects, and/or invalid TIU Template Fields.                                   |
| ED           | Edit/Delete Dialog                        | Edit or delete this reminder dialog. Allows addition and deletion of existing dialog elements from this reminder dialog. Allows the sequence numbers to be changed. Also enable/disable dialog. |
| INQ          | Inquiry/Print (for Reminder Dialogs only) | Print details of this reminder dialog.                                                                                                                                                          |

##### Dialog Edit Options

The edit options allow changes to the selected reminder dialog. When making changes to dialog elements and prompts, it should be remembered that dialog elements and prompts might be used in more than one reminder dialog. Changing one reminder dialog may affect others. When editing any of the sub items, a list is presented that displays any other dialogs, groups, or elements that are using the item that is being edited. Additional prompts, forced values, dialog elements, and dialog groups may be edited or printed.

Dialog Edit List              Dec 15, 2004@14:04:59                Page:    1 of    4

REMINDER DIALOG NAME: VA-DEPRESSION ASSESSMENT [NATIONAL] *LIMITED EDIT*

Item  Seq.    Dialog Summary

1    5   Element: VA-TEXT DEPRESSION EVAL INSTRUCTIONS

2    7   Element: VA-TEXT BLANK LINE WITH TEMPLATE FIELD

3    10  Group: VA-GP DEP MDD CRITERIA DISPLAY

4    10.5   Element: VA-TEXT MDD DSM-IV CRITERIA DISPLAY

5    12  Group: VA-GP PHQ 9

6    12.5   Element: VA-TEXT PHQ 9

7    15  Element: VAA-TEXT BLANK LINE

**8    20  Group: VA-GP DEP ASSESSMENT RESULTS**

**+ Next Screen   - Prev Screen   ?? More Actions** ADD  Add Element/Group    DS   Dialog Summary       CHCK Dialog Checker

CO   Copy Dialog          DO   Dialog Overview      ED   Edit/Delete Dialog

DD   Detailed Display     DT   Dialog Text

DP   Progress Note Text   TEST Dialog Test          QU   Quit

Select Item: Next Screen//

##### Dialog Overview

The action Dialog Overview (DO) allows you to see just the top level of the dialog elements, without the nested items, if the dialog has groups containing elements.

Dialog Edit List              Dec 15, 2004@14:04:59                Page:    1 of    4

REMINDER DIALOG NAME: VA-DEPRESSION ASSESSMENT [NATIONAL] *LIMITED EDIT*

Item  Seq.    Dialog Overview

1    5   Element: VA-TEXT DEPRESSION EVAL INSTRUCTIONS

2    7   Element: VA-TEXT BLANK LINE WITH TEMPLATE FIELD

3    10  Group: VA-GP DEP MDD CRITERIA DISPLAY

4    12  Group: VA-GP PHQ 9

5    15  Element: VAA-TEXT BLANK LINE

6    20  Group: VA-GP DEP ASSESSMENT RESULTS

7    24  Element: VAA-TEXT BLANK LINE

8    30  Element: VA-HF PT FOLLOWED FOR DEPRESSION

**+ Next Screen   - Prev Screen   ?? More Actions**

ADD  Add Element/Group    DS   Dialog Summary       	CHCK Dialog Checker

CO   Copy Dialog          DO   Dialog Overview      	ED   Edit/Delete Dialog

DD   Detailed Display     DT   Dialog Text		INQ  Inquiry/Print

DP   Progress Note Text   TEST Dialog Test	       QU QUIT

Select Item: Next Screen//

**Result Dialogs**

Result dialogs contain progress note text that is added to a progress note, based on the results of dialog processing. NOTE: Only Mental Health Instrument results can be used.

Some reminder definitions have Finding Items for MH Instruments. When dialog entries are generated for these reminders, a dialog element will be created for each MH Instrument finding. If a site doesn’t want to see mental health instrument questions and answers added into the progress note, they can control whether to include the questions and answers by answering Yes to the EXCLUDE MH TEST FROM PN TEXT field in the dialog element. If a site wants the mental health instrument questions and answers added to the progress note text, the reminder manager must answer No at the EXCLUDE MH TEST FROM THE PN TEXT field.

EXCLUDE MH TEST FROM PN TEXT 0;14 SET

'1' FOR YES;

'0' FOR NO;

HELP-PROMPT:    Enter Y to stop test questions and answers from being

added to the note text.

DESCRIPTION:    This flag is used to control whether or not

mental health test questions and answers will be excluded

from the progress note text when the test is taken.

When the user enters answers to a mental health instrument, the answers are automatically passed to the Mental Health package to calculate a result, which may be referenced as SCORE. For example, the CAGE test has a SCORE from 1-4 and GAF has a SCORE from 1-99.

For most Mental Health tests, progress note text can be automatically generated that summarizes or includes the results (SCORE). Default text is distributed in the REMINDER DIALOG file #801.41 for sites to use for each Mental Health instrument processed in the reminder resolution process. This text may be copied and modified to reflect the site’s preferences for text. The default text is defined in Mental Health Result Dialog Elements. The reminder manager must add the Result Dialog Group to the MH Instruments Dialog Element RESULT GROUP SEQUENCE field. This result dialog may define further processing to conditionally generate progress note text based on the SCORE.

The Result Dialog Elements provide a number of fields for flexible use of progress note text.

RESULT CONDITION:	Enter M code which, when evaluated to 1, would generate the progress note text and create finding entries defined in the RESULT DIALOG ELEMENT.  Currently, The logic can only use the value stored in an M local variable called SCORE.

PROGRESS NOTE TEXT:  Enter the word processing text to add to the progress note.  Use a blank space in the first character of a line when you want the line to be printed as it appears in the text.  The "|" (vertical bar) may be used around the M variable SCORE to include the score within the text (MH Tests only).  Response values may be included in the text for the AIMS test only, and limited to the variables specified in the default AIMS text.

**Example of one of the CAGE Result Dialog Elements distributed with the package:**

NAME: CAGE RESULT ELEMENT **1** Replace **&lt;Enter&gt;**

RESULT CONDITION: I SCORE&lt;2// **&lt;Enter&gt;**

PROGRESS NOTE TEXT: **&lt;Enter&gt;**

An alcohol screening test (CAGE) was negative (score=|SCORE|).

**Reminder Dialog Branching Logic**

This functionality allows the Clinical Reminder Manager to setup Reminder Dialogs to change the layout in CPRS based on patient data that is stored in VistA. With PXRM*2.0*45, the Clinical Reminder Manager can setup multiple branching logic statements with a sequence number. The branching logic statements are evaluated in order by sequence number and the first true branching logic statement action will be applied to the Reminder Dialog layout in CPRS. With the new Branching Logic Functionality, if the statement is replacing the existing element/groups and if the new element/group contains branching logic, those branching logic statements will now be evaluated, before PXRM*2.0*45, this did not happen.

Examples of Branching Logic statements:

Replaced by VA-WH SMART BR MALE PROCEDURE DOCUMENT if Reminder Term VA-PATIENT IS MALE evaluates as True

Replaced by VA-WH GP BR REVIEW ALERT OVERALL if Reminder  Definition VA-WH BL BR ALERT WITH NO OPEN PROCEDURE evaluates as Due

Hide if Reminder Term VA-WH BL BREAST CASCADE EXIST evaluates as False

**Branching Logic Sequence:** This field accepts a number and is used to determine the order to evaluate the patient data. The first patient data that evaluates true for the Branching Logic statement will take effect in CPRS. This Sequence is very important when adding multiple Branching Logic statements to a Reminder Dialog Element/Group.

**Evaluation Item:** This is either a Reminder Term or a Reminder Definition to use in the Branching Logic Statement to evaluate the patient’s data on the system.

**Evaluation Status:** This field is used in the Branching Logic statement to determine if the statement is true based on the results of the Reminder Term/Definition defined in the Evaluation Item Field. The possible values are different depending on the type of item selected in the Evaluation Item field.

Evaluation Item is a Reminder Term

- True
- False

Evaluation Item is a Reminder Definition

- Due
- Applicable
- N/A, this includes CONTRA and REFUSED

Action: Is the type of action that should happen in CPRS if the Branching Logic statement is true.

Reminder Dialog Element/Groups support the following actions:

- Hide
- Replace
- Check Checkbox
- Suppress Checkbox and Show

The following Actions are only selectable when the item containing the branching logic is a group. These actions will change the Multiple Selection value of the group if the Branching Logic statement is true.

- No Selection Required
- One Selection Only
- One or More Selections
- None or One Selection
- All Selections are Required

**NOTE:** When using a Reminder Definition as an Evaluation Item, the Evaluation Status of DUE is a subset of the Applicable status. If performing multiple Branching Logic statements against a Reminder, the evaluation is looking for both a Due Status or Applicable. Make sure the DUE status branching statement Branching Logic Sequence value is before the Applicable status Branching Logic Sequence value.

#### Editing Template Fields used in Reminder Dialogs

How to set the TIU parameter that allows a user access to the Options/Edit Template Fields from the CPRS GUI Notes tab:

The Edit Template Fields option can be used to create sets of checkboxes, radio buttons, etc., which can be used in reminder dialogs.

<!-- image -->

<!-- image -->

In order to use the Edit Template Fields option to edit template fields used in Reminder Dialogs, the following are required:

1. New option: TIU Template Reminder Dialog Parameter, on the CPRS Parameter menu on the Reminder Manager Menu
    1. TIU parameter TIU FIELD EDITOR CLASSES
    2. User Class of Clinical Coordinator

##### TIU parameter TIU FIELD EDITOR CLASSES

Select OPTION NAME: **xpar edit**

1   XPAR EDIT BY TEMPLATE       Edit Parameter Values with Template   action

2   XPAR EDIT KEYWORD       Edit Parameter Definition Keyword     edit

3   XPAR EDIT PARAMETER       Edit Parameter Values     action

CHOOSE 1-3: 3  XPAR EDIT PARAMETER     Edit Parameter Values     action

Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: tiu field EDITOR CLASSES     Template Field Ed

itor User Classes

TIU FIELD EDITOR CLASSES may be set for the following:

1   User          USR    [choose from NEW PERSON]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [choose from INSTITUTION]

5   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

6   Package       PKG    [TEXT INTEGRATION UTILITIES]

Enter selection: **u  User** NEW PERSON

Select NEW PERSON NAME: **CRUSER** CRUSER,ONE   OC  SYSTEMS ANALYST/PROGRAMMER

---------- Setting TIU FIELD EDITOR CLASSES  for User: CRUSER,ONE ---------

Select Sequence Number: **1**

Are you adding 1 as a new Sequence Number? **Yes** // y  YES

Sequence Number: 1//    1

User Class: Clin

1   Clinical And Laboratory Immuno  CLINICAL AND LABORATORY IMMUNOLOGIST

2   Clinical Biochemical Geneticis  CLINICAL BIOCHEMICAL GENETICIST

3   Clinical Biochemical Molecular  CLINICAL BIOCHEMICAL MOLECULAR GENETICIST

4   Clinical Clerk  CLINICAL CLERK

5   Clinical Coordinator  CLINICAL COORDINATOR

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 5  CLINICAL COORDINATOR

Select Sequence Number: ?

Sequence Number                      Value

---------------                      -----

1                                    CLINICAL COORDINATOR

Select Sequence Number:

###### User Class of Clinical Coordinator

Select OPTION NAME: TIU Maintenance Menu TIU IRM MAINTENANCE MENU

TIU Maintenance Menu

1      TIU Parameters Menu ...
   2      Document Definitions (Manager) ...
   3      User Class Management ...
   4      TIU Template Mgmt Functions ...
   5      TIU Alert Tools

Select TIU Maintenance Menu Option: 3  User Class Management

--- User Class Management Menu ---

1      User Class Definition

2      List Membership by User

3      List Membership by Class

5      Manage Business Rules

Select User Class Management Option: 2  List Membership by User

Select USER: CRPROVIDER,ONE     CHIEF, MEDICAL SERVICE

Current User Classes          Jan 23, 2003@14:55:15                Page:    1 of    1

CRPROVIDER,ONE                      2 Classes

User Class                                          Effective  Expires

1    Clinical Coordinator                                04/28/00

2    Physician                                           11/16/98   04/11/15

**+ Next Screen   - Prev Screen   ?? More Actions** Add                       Remove                    Quit

Edit                      Change View

###### Add a New Class to an Existing User

Current User Classes          Jan 23, 2003@14:55:15        Page:    1 of    1

CRPROVIDER,ONE                      2 Classes

User Class                                          Effective  Expires

1    CRPROVIDER's Consult Class

2    Business Rule Manager                                  09/22/00

3    Medical Administration Special                         09/11/01

4    Social Worker Supervisor

+ Next Screen  - Prev Screen  ?? More Actions              \_\_\_\_\_\_\_

Add                       Remove                    Quit

Edit                      Change View

Select Action: Quit// add   Add

Select USER CLASS: Clin

1   Clinical And Laboratory Immuno  CLINICAL AND LABORATORY IMMUNOLOGIST

2   Clinical Biochemical Geneticis  CLINICAL BIOCHEMICAL GENETICIST

3   Clinical Biochemical Molecular  CLINICAL BIOCHEMICAL MOLECULAR GENETICIST

4   Clinical Clerk  CLINICAL CLERK

5   Clinical Coordinator  CLINICAL COORDINATOR

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 5  CLINICAL COORDINATOR

EFFECTIVE DATE: t  (JAN 23, 2003)

EXPIRATION DATE: t+1  (JAN 24, 2003)

Select Another USER CLASS:

Rebuilding membership list.

Current User Classes          Jan 23, 2003@14:55:15        Page:    1 of    1

CRUSER,TWO                      2 Classes

User Class                                          Effective  Expires

1    A Consult Class

2    Business Rule Manager                               09/22/00

3    Clinical Coordinator                                01/23/03   01/28/03

4    Medical Administration Special                      09/11/01

5    Social Worker Supervisor

**+ Next Screen   - Prev Screen   ?? More Actions** Add                       Remove                    Quit

Edit                      Change View

#### Dialog Reports

| Option Name                                        |                             | Synonym   | Description                                                                                                                                                                  |
|----------------------------------------------------|-----------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Dialog Elements Orphan Report             | PXRM DIALOG ORPHAN REP  ORT | OR        | This option is used to run the Reminder Dialog Elements Orphan Report.                                                                                                       |
| Reminder Dialog Search Report                      | PXRM DIALOG SEARCH REPORT   | SEA       | This option enables the user to search for Reminder Dialogs containing search criteria define by the user.                                                                   |
| Empty Reminder Dialog Report                       | PXRM DIALOG EMPTY REPORT    | ER        | This Option will run the Empty Reminder Dialog report.                                                                                                                       |
| Check Reminder Dialog for invalid items            | PXRM DIALOG CHECKER         | CH        | This option runs a routine that checks a selected reminder dialog for  invalid sub-dialog items, invalid finding items, invalid TIU Objects, and/or invalid Template Fields. |
| Check All Active Reminder Dialog for invalid items | PXRM DIALOG CHECKER ALL     | ALL       | This option screens all active reminder dialogs for invalid items.                                                                                                           |
| Reminder Dialog CPRS 32 pre conversion report      | PXRM DIALOG VIMM PRE REPORT | 32        | This option provides a report of Reminder Dialog Elements/Groups that need to be reviewed before CPRS 32 is install.                                                         |

##### Reminder Dialog Elements Orphan Report

Select Reminder Managers Menu Option: DM  Reminder Dialog Management

   DP     Dialog Parameters ... 
   DI     Reminder Dialogs
   DR     Dialog Reports ...
   
Select Reminder Dialog Management Option: DR  Dialog Reports

   OR     Reminder Dialog Elements Orphan Report

ER     Empty Reminder Dialog Report
   ALL    Check All Reminder Dialogs for invalid items

SEA	   Reminder Dialog Search Report
   32     Reminder Dialog CPRS 32 pre conversion report
   CH     Check Reminder Dialog for invalid items

Select Dialog Reports Option: **OR** Reminder Dialog Elements Orphan Report
DEVICE: HOME// **;;999999999** ANYWHERE    Right Margin: 80//

Reminder Dialog Elements Orphan Report                                Page: 1

================================================================================

Dialog Elements

===============

A NEW DIALOG ELEMENT FOR IMMUNIZATION

A NEW HEP A ELEMENT

EC HISTORICAL (3)

EC TAXON

ED ADVANCED DIRECTIVE SCREENING DONE (10)

ED ADVANCED DIRECTIVE SCREENING DONE (2)

ED ADVANCED DIRECTIVE SCREENING DONE (3)

.

.

ZZVA-WV PAP SMEAR CLINICAL REVIEW

ZZVA-WV TEST FORCED VALUE

a a new test field

blank

Dialog Groups

=============

DG LEVEL 2 GROUP

EXCLUDE FROM P/N GROUP

GP DEMO GROUP

GP HEP C RISKS

GP IMM PNEUMO

GP SPECIAL

GP TEST TAXONOMY GROUP

GP TOBACCO

GP VITALS

GPZ UNVESTED PXZ MSK VESTING C/O

GPZ VIAGRA INITIATION DOSES

IHD LIPID DONE ELSEWHERE GROUP

IHD LIPID LOWER MANAGE GROUP

PJH TEST GROUP

SP EXERCISE COUNSELING (1)

TEST OF WH GROUP

TEST P/N TEXT

VA-DG GEC ADDL INFO

ZZVA-WH GP PAP FOLLOW-UP TX/HIDE

ZZVA-WH GP PAP SCREENING REPEAT - ABNORMAL PAP

ZZVA-WV GP CERVICAL CARE

ZZVA-WV GP MAM FOLLOW-UP TX

ZZVA-WV GP MAM REVIEW - NOTIFY &amp; F/U XXXXX

ZZVA-WV GP PAP REVIEW F/U W/O NOTIFY

Result Groups

=============

PXRM AIMS RESULT GROUP

PXRM AUDC RESULT GROUP

PXRM AUDIT RESULT GROUP

PXRM BDI RESULT GROUP

PXRM CAGE RESULT GROUP

PXRM DOM80 RESULT GROUP

PXRM DOMG RESULT GROUP

PXRM MISS RESULT GROUP

PXRM ZUNG RESULT GROUP

SLC ZUNG RESULT GROUP

SLC ZUNG2

Additional Prompts

==================

A A PAIN BLANK TEXT PROMPT

A A PAIN ENTER ALL APPLY

A A PAIN FREQ HX

A A PAIN ONSET PROMPT

A A PAIN TXT 3CHR

A A SG PAIN HISTORY LOCATION PROMPT

NEW PROMPT FOR COMMENT

PJH PXRM COMMENT

PR SG PAIN SCREENING NOT DONE

PXRM FORCE VALUE TEST

PXRM WH REVIEW RESULT COMMENT

PXRM*1.5*5 PERSON TYPE

Force Values

============

A A *PAIN TRIGGERS PROMPT

A A ENTER ALL THAT APPLY

A A PAIN ACCEPTABLE PROMPT

A A PAIN NEW HX PROMPT

A ASUSAN'S TEST

PXRM FORCE DATE TEST

PXRM WH NOTIFICATION TYPE

PYRM SERIES FORCED

WH NOTIFICATION FORCE VALUE

a new forced value

Enter RETURN to continue or '^' to exit:

OR     Reminder Dialog Elements Orphan Report

ER     Empty Reminder Dialog Report

CH     Check Reminder Dialog for invalid items

##### Reminder Dialog Search Report

Select Dialog Reports &lt;TEST ACCOUNT&gt; Option: sea  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 5

Search for all or selected MENTAL HEALTHS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED//

Select MENTAL HEALTH: AUDC

1   AUDC

2   AUDCR

CHOOSE 1-2: 1  AUDC

Select MENTAL HEALTH:

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// YES

1 - Division

2 - Location

3 - Service

4 - System

5 - User

6 - User Class

Enter your list for the report:  (1-6): 5

Select User: CPRS,USER            UC          COMPUTER SPECIALIST

Select User:

Display match criteria on the report? N// YES

Browse or Print? B// Print

DEVICE: HOME// ;;999999  TELNET PORT

Clinical Reminders Dialogs search report.

CPRS Cover Sheet Reminder Dialogs for User (CPRS,USER):

Dialog: UC ICD10 TAX

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: AGP AUDC 1

Finding: MH.AUDC

Dialog: UC TEMPL DLG

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: AGP MH

Finding: MH.AUDC

Dialog: VA-ALCOHOL USE SCREENING (AUDIT-C)

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: VA-MH AUDC

Finding: MH.AUDC

Dialog: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: VA-MH AUDC

Finding: MH.AUDC

CPRS Template Dialogs:

Dialog: UC NEW DIALOG TEST

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: UC AUDC 1

Finding: MH.AUDC

Dialog: MH TEST

Match Criteria:

Dialog Element: MH AUDC

Finding: MH.AUDC

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Match Criteria:

Dialog Result Group: PXRM AUDC RESULT GROUP

Finding: MH.AUDC

Dialog Element: VA-MH AUDC

Finding: MH.AUDC

Press ENTER to continue:

##### Empty Reminder Dialog Report

Select Dialog Reports Option: ER  Empty Reminder Dialog Report

DEVICE: HOME// ;;99999999999  ANYWHERE    Right Margin: 80//

Empty Reminder Dialogs Report                                         Page: 1

================================================================================

A COPY OF AGETEST

AGP EMPTY DIALOG TEST

ANOTHER NEW REMINDER

TEST EDIT (1)

TEST EDIT COPY

**Enter RETURN to continue or '^' to exit:**

OR     Reminder Dialog Elements Orphan Report

ER     Empty Reminder Dialog Report

CH     Check Reminder Dialog for invalid items

Select Dialog Reports Option:

##### Check Reminder Dialog for Invalid Items

**This option scans the selected dialog items for invalid sub-items, findings, TIU Objects, and/or TIU Templates. If any invalid items are found in the dialog, the results will be displayed to the user. This option allows for any dialog items to be selected, except for Additional Prompts and Forced Values.**

The dialog checker report will check for the following items.

1. Disabled dialog items in the selected dialog
2. Incomplete sequences in the selected dialog
3. All sub-items in the selected dialog are pointing to valid entry on the system
4. All finding items, additional finding items, and orderable items are pointing to a valid entry on the system
5. Result groups are pointing to a valid MH Test and an MH scale has been defined for the result group
6. An odd number of “|” characters in a dialog text field. If this is the case, it would not be possible to determine which part is a TIU Object
7. Progress Note Text and the Alternate Progress Note text fields have valid TIU Objects and TIU Template Field
8. Dialogs that have recursion errors
9. Incomplete Branching Logic Statements
10. Review the Reminder Definition and Reminder Terms used in Branching Logic for errors

Example of output

Select Reminder Dialog Management &lt;TEST ACCOUNT&gt; Option: DR  Dialog Reports

OR     Reminder Dialog Elements Orphan Report

ER     Empty Reminder Dialog Report

ALL    Check all active reminder dialog for invalid items

CH     Check Reminder Dialog for invalid items

Select Dialog Reports Option: CH  Check Reminder Dialog for invalid items

Select Dialog Definition:    EXCHANGE DIALOG     reminder dialog     LOCAL

...OK? Yes//   (Yes)

EXCHANGE DIALOG contains the following errors.

The dialog element INACTIVE OBJECT contains a reference to a TIU
Object NP TIUHS OBJECT TEST in the Dialog Text field. This TIU Object is
inactive.

##### Check All Reminder Dialogs for Invalid Items

Select Dialog Reports Option: ALL  Check all active reminder dialog for invalid items

COPY OF AGE TEST contains the following errors.

The dialog group HF BINGE DRINKING OTHER is disabled.

AGP INDENT TEST contains the following errors.

The dialog element 123456789 123456789 123456789 123456789 123456789

123456789 123 contains a pointer to an additional finding item that does

not exist on the system.

ZZPJH REMINDER contains the following errors.

The dialog element WH PAP, ANNUAL DUE. contains an a pointer to the

finding item that does not exist on the system.

PHARMACY DISCHARGE MEDICATIONS contains the following errors.

The dialog element PHARMACY DISCHARGE MEDS QUESTIONS contains a reference

to a TIU Object OUTPATIENT MEDS in the Dialog Text field. This TIU Object

does not exist on the system.

The dialog group GRP MOVE! SCREENING 5/2007 contains a reference to a TIU

Object BMI (BODY MASS INDEX %) in the Dialog Text field. This TIU Object

does not exist on the system.

Pap Smear (local) contains the following errors.

The dialog element EX PAP DONE  contains a reference to a TIU Object PAP

SMEAR in the Dialog Text field. This TIU Object does not exist on the

system.

ETC.

**DONE**

##### Dialog Taxonomy Changes

***Before PXRM*2*26*** , users created Reminder Dialogs by adding individual ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog. If the Reminder Dialog was set up to use a Taxonomy, it could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS.

The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter and what prompts should be assigned to the Reminder Dialog in CPRS.

***After PXRM*2*26*** , users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new field called Taxonomy Pick List Display has been added to the dialog editor. This controls how Taxonomies should display in CPRS.

**Dialog Taxonomy Editor**

A simple taxonomy editor that is accessed from the Dialog Management menu (either the element or group view) is available. Codes added in this editor are automatically marked as Use In Dialog (UID). If the code already exists in the Selected Codes multiple, all instances of it are marked as UID. If the code does not already exist, it is added to the Selected Codes multiple with TERM/CODE set to the code and the code is marked as UID. If a code is deleted in this editor, UID is removed from all instances of the code but it is not deleted from the Selected Codes multiple. You must use the regular taxonomy editor to actually delete the code.

Dialog List                   Aug 08, 2013@12:07:04          Page:    1 of   15

REMINDER VIEW (ALL REMINDERS BY NAME)

Item Reminder Name                      Linked Dialog Name &amp; Dialog Status

1  14HTN (TESTING)

2  15 REMINDER DIALOG TESTS           15 TESTING DIALOG

3  15V-DIABETES TX TEST

4  AJM TAXONOMY                       AJM TAXONOMY

5  ARD 00 ANTICOAGULATION AFIB

+         Enter ?? for more actions                                         &gt;&gt;&gt;

AR   All reminders        LR   Linked Reminders     QU   Quit

CV   Change View          RN   Name/Print Name

Select Item: Next Screen// cv   Change View

Select one of the following:

D         Reminder Dialogs

E         Dialog Elements

F         Forced Values

G         Dialog Groups

P         Additional Prompts

R         Reminders

RG        Result Group (Mental Health)

RE        Result Element (Mental Health)

TYPE OF VIEW: R// e  Dialog Elements

<!-- image -->

Select Item: Next Screen// te   Dialog Taxonomy Edit

Select REMINDER TAXONOMY NAME: 1

1   10 EG CPT ONLY       LOCAL

2   10 EG ICD10 AND CPT       LOCAL

3   10 EG ICD10 ONLY       LOCAL

4   10 EG ICD9 AND CPT       LOCAL

5   10 EG ICD9 ONLY       LOCAL

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 2  10 EG ICD10 AND CPT     LOCAL

<!-- image -->

### 1 New Fields

***Taxonomy Pick List Display*** - This field controls if and what pick lists should appear in CPRS. The possible values for the option are based on the setup of the Taxonomy in the Finding Item Field. If a pick list is set to not display, then the active codes marked to be used in a dialog will automatically be filed to PCE for the encounter date for that element when the finish button is clicked. Possible values for this field:

- All = A pick list will display for each code type (ICD/10D and CPT) in taxonomy.
- Diagnosis Only = A pick list will display only for ICD/10D codes
- Procedure Only = A pick list will display only for CPT codes
- Standard Codes Only = A pick list will display only for Standard Codes
- None = Will not display a pick list

***POV (diagnosis) Header*** - This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

***CPT (procedure) Header*** - This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

***STANDARD CODES Header*** - This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

**Also, after PXRM*2.0*26 is installed, users will no longer be able to set one Taxonomy Element to prompt for both Current and Historical Encounter Data. Users will need to create an element for each encounter type, Current and Historical. If the element Resolution Type is set to Done Elsewhere, then the editor will prompt the user to accept the default prompts for the taxonomy which includes prompts for historical data. prompt for historical data. Any other resolution type or no resolution type will prompt data for the current encounter date.**

For the ICD-10 implementation, Reminder Dialogs will display ICD-9-CM or ICD-10-CM in a pick list based on the code set versioning rules. Reminder Dialogs determine what codes to display using the following rules:

- Current encounters= active codes for that encounter date; Addendums will use the parent note Encounter date.
- Historical encounters= active codes for system date

Examples:

An example Taxonomy that is a copy of VA-ADB AORTIC; this example has additional codes set to be used in a dialog.

--------------------------------------------------------------------------------

AAA TAX DEMO                                                            No. 115

--------------------------------------------------------------------------------

Class: LOCAL

Sponsor:

Review Date:

Description:

ICD codes and CPT codes indicating AAA

Inactive Flag:

Patient Data Source:

Use Inactive Problems:

Selected Codes:

**Lexicon Search Term/Code: Abdominal aortic aneurysm**

Coding System: ICD-10-CM

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

I71.3      01/01/2012                X   Abdominal Aortic Aneurysm, Ruptured

I71.4      01/01/2012                X   Abdominal Aortic Aneurysm, without

Rupture

**Lexicon Search Term/Code: Copy from CPT range 34800 to 34805**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

34800      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Aorto-Aortic

Tube Prosthesis

34802      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Modular

Bifurcated Prosthesis (one Docking

Limb)

34803      01/01/2005                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Modular

Bifurcated Prosthesis (two Docking

Limbs)

34804      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Unibody

Bifurcated Prosthesis

34805      01/01/2004                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Aorto-Uniiliac

or Aorto-Unifemoral Prosthesis

**Lexicon Search Term/Code: Copy from CPT range 34825 to 34832**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

34825      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm; Initial

Vessel

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic or Iliac

Aneurysm, False Aneurysm, or

Dissection; Initial Vessel

34826      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm; each

additional Vessel

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic or Iliac

Aneurysm, False Aneurysm, or

Dissection; each additional Vessel

(List Separately in addition to

Code for Primary Procedure)

34830      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair; Tube

Prosthesis

34831      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair;

Aorto-Bi-Iliac Prosthesis

34832      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair;

Aorto-Bifemoral Prosthesis

**Lexicon Search Term/Code: Copy from CPT range 35081 to 35103**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

35081      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with or without Patch

Graft; for Aneurysm and Associated

Occlusive Disease,Abdominal Aorta

35082      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Abdominal

Aorta

35091      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with/without Patch

Graft; for Aneurysm and Associated

Occlusive Disease, Abdominal Aorta

involving Visceral Vessels

(Mesenteric, Celiac, Renal)

35092      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Mesenteric,

Celiac or Renal Arterial Branch of

the Abdominal Aorta

35102      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with/without Patch

Graft; for Aneurysm and Associated

Occlusive Disease, Abdominal Aorta

involving Iliac Vessels (Common,

Hypogastric, External)

35103      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Iliac

Vessels (Common, Hypogastric,

External) of the Abdominal Aorta

**Lexicon Search Term/Code: Copy from CPT range 75952 to 75953**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

75952      01/01/2001                    Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection, Radiological

Supervision and Interpretation

75953      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm,

Radiological Supervision and

Interpretation

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Aortic or Iliac Artery Aneurysm,

Pseudoaneurysm, or Dissection,

Radiological Supervision and

Interpretation

**Lexicon Search Term/Code: Copy from ICD range 441.3 to 441.4**

Coding System: ICD-9-CM

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

441.3      10/01/1978  01/01/2012    X   Abdominal aneurysm, ruptured

441.4      10/01/1978  01/01/2012    X   Abdominal aneurysm without mention

of rupture

This taxonomy includes the following numbers of codes:

ICD-10-CM: 2

CPT-4: 18

ICD-9-CM: 2

Total number of codes: 22

Below are screen shots of how CPRS will display the taxonomy using different values.

**Example 1**

**Setting a Taxonomy as a finding item to display pick lists for both ICD-9, ICD-10, and CPT codes, for current encounters only.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: TX.AAA  AAA TAX DEMO     LOCAL

...OK? Yes//   (Yes)

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List Display: A// ll

Select one of the following:

C         CURRENT ENCOUNTER

H         HISTORICAL ENCOUNTER

B         BOTH CURRENT AND HISTORICAL ENCOUNTERS

Diagnosis Header: Diagnosis recorded at encounter.  Replace

Procedure Header: done.//

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM VISIT DATE

Required: Yes

Prompt: PXRM OUTSIDE LOCATION

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

Edit? NO// Select the correct AAA codes.

With these settings, the user is able to pick from a pick list of diagnoses and procedure codes to add to the current encounter.

<!-- image -->

**Example 2**

**Setting a Taxonomy as a finding item to display pick lists for both ICD-10 and CPT codes for historical encounters only.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE: DONE ELSEWHERE (HISTORICAL)

ORDERABLE ITEM:

Finding item: TX AAA TAX DEMO

FINDING ITEM: AAA TAX DEMO//

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List Display: A// ll

Diagnosis Header: History of Diagnosis.  Replace

Procedure Header: previously done.//DIALOG/PROGRESS NOTE TEXT:

Select the correct AAA codes.

Edit? NO//

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user is able to assign diagnosis and/or procedure codes to a historical encounter. The historical date will be created based on the Date prompt for the diagnosis, procedure, and standard codes checkboxes.

<!-- image -->

**Example 3**

**Setting a Taxonomy as a finding item to display pick lists for only ICD-10 codes for the current encounters.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

Finding item: TX AAA TAX DEMO

FINDING ITEM: AAA TAX DEMO//

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List Display: A// d  ICD Diagnoses Only

Diagnosis Header: Diagnosis recorded at encounter.

Replace

DIALOG/PROGRESS NOTE TEXT:

Select the correct AAA codes.

Edit? NO//

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user will be able to pick diagnosis codes to add to the current encounter. The active procedure codes that were marked to be used in a dialog will automatically be filed to the current encounter. No historical data will be stored for this element.

<!-- image -->

**Example 4**

**Setting a Taxonomy as a finding item to display pick lists for CPT codes only for the current encounters.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

Finding item: TX AAA TAX DEMO

FINDING ITEM: AAA TAX DEMO//

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List Display: D// p  CPT Procedures Only

Procedure Header: done.// Procedure done at this encounter.

DIALOG/PROGRESS NOTE TEXT:

Select the correct AAA codes.

Edit? NO//

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user will be able to pick the Procedure codes to assign to the current encounter. The active diagnosis codes marked to be used in the dialog will automatically be assigned to the encounter. No historical data will be stored for this element.

<!-- image -->

**Example 5**

**Setting a Taxonomy as a finding item to display no pick list set to display.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

Finding item: TX AAA TAX DEMO

FINDING ITEM: AAA TAX DEMO//

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List Display: P// n  None

DIALOG/PROGRESS NOTE TEXT:

Select the correct AAA codes.

Edit? NO//

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With this setting, all active diagnosis/procedure codes marked to be used in a dialog will automatically be filed to the current encounter.

<!-- image -->

Note: In the first example the software added the following prompts to the dialog element.

Prompt: PXRM COMMENT

Prompt: PXRM VISIT DATE

Prompt: PXRM OUTSIDE LOCATION

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

In examples 2-5, the prompts were not changed. CPRS will determine which prompts to show, based on the prompts assigned to the element, the codes in the taxonomy, and the Resolution Status Field. However, it is good practice to remove prompts that are not being used by the dialog.

**Taxonomy Editor**

A simple taxonomy editor that is accessed from dialog management (either the element or group view) is also available. Codes added in this editor are automatically marked as Use In Dialog. If a code is deleted in this editor, the Use In Dialog designation is removed from the code.

Dialog List                   Aug 08, 2013@12:07:04          Page:    1 of   15

REMINDER VIEW (ALL REMINDERS BY NAME)

Item Reminder Name                      Linked Dialog Name &amp; Dialog Status

1  14HTN (TESTING)

2  15 REMINDER DIALOG TESTS           15 TESTING DIALOG

3  15V-DIABETES TX TEST

4  AJM TAXONOMY                       AJM TAXONOMY

5  ARD 00 ANTICOAGULATION AFIB

+         Enter ?? for more actions                                         &gt;&gt;&gt;

AR   All reminders        LR   Linked Reminders     QU   Quit

CV   Change View          RN   Name/Print Name

Select Item: Next Screen// cv   Change View

Select one of the following:

D         Reminder Dialogs

E         Dialog Elements

F         Forced Values

G         Dialog Groups

P         Additional Prompts

R         Reminders

RG        Result Group (Mental Health)

RE        Result Element (Mental Health)

TYPE OF VIEW: R// e  Dialog Elements

<!-- image -->

Select Item: Next Screen// te   Dialog Taxonomy Edit

Select REMINDER TAXONOMY NAME: 1

1   10 EG CPT ONLY       LOCAL

2   10 EG ICD10 AND CPT       LOCAL

3   10 EG ICD10 ONLY       LOCAL

4   10 EG ICD9 AND CPT       LOCAL

5   10 EG ICD9 ONLY       LOCAL

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 2  10 EG ICD10 AND CPT     LOCAL

### CPRS Reminder Configuration Menu

This menu contains options to maintain reminder categories and to set up reminder dialogs within CPRS.

| **Syn**   | **Option**                                | **Option Name**               | **Description**                                                                                                                                                                                                                                                                                                |
|-----------|-------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CA        | Add/Edit Reminder Categories              | PXRM CATEGORY EDIT/INQUIRE    | A reminder category may contain a list of reminders and/or other sub-categories. Use this option to edit the list.                                                                                                                                                                                             |
| CL        | CPRS Lookup Categories                    | PXRM CPRS LOOKUP CATEGORIES   | Reminder Categories to be displayed in the Other Categories folder of the note tab are entered here.                                                                                                                                                                                                           |
| CS        | CPRS Cover Sheet Reminder List            | PXRM CPRS COVER SHEET LIST    | Use this option to enter reminders that will be displayed on the CPRS cover sheet if the New Reminders Parameter is NOT set to Yes.                                                                                                                                                                            |
| CSR       | Cover Sheet Reminder Report               | PXRM COVER SHEET REMINDER RPT | This option runs the Cover Sheet Reminder Report. It provides the ability to determine what reminders are in a cover sheet list.                                                                                                                                                                               |
| MH        | Mental Health Dialogs Active              | PXRM MENTAL HEALTH ACTIVE     | This option allows a user to modify the "Mental Health Dialogs Active" CPRS parameter. You can activate Mental Health reminder resolution processing at a user, service, division, or system level. When activated for one of these levels, mental health tests can be performed in a reminder dialog.         |
| PN        | Progress Note Headers                     | PXRM PN HEADER                | The header inserted into the progress note when processing a reminder may be modified for user, location, or service. The default header is Clinical Reminders Activity.                                                                                                                                       |
| RA        | Reminder GUI Resolution Active            | PXRM GUI REMINDERS ACTIVE     | This option allows a user to modify the "Reminders Active" CPRS parameter. You can activate GUI reminder resolution processing at a user, service, division, or system level. When activated for one of these levels, a reminders drawer is available on the notes tab for selecting and processing reminders. |
| DL        | Default Outside Location                  | PXRM DEFAULT LOCATION         | Allows the default outside location for reminder dialogs to be specified at user, service, division, or system level.                                                                                                                                                                                          |
| PT        | Position Reminder Text at Cursor          | PXRM TEXT AT CURSOR           | Allows the position reminder note text at cursor feature to be enabled at user, service, division, or system level.                                                                                                                                                                                            |
| WH        | WH Print Now Active                       | PXRM WH PRINT NOW             | This option allows sites to include the Print Now button on Women’s Health dialogs for notification letters.                                                                                                                                                                                                   |
| GEC       | GEC Status Check Active                   | PXRM GEC STATUS CHECK         | A GEC Status Indicator may be added to the CPRS GUI Tools drop-down menu, to be viewed at any time and used to close the referral if needed. It may be set at the User or Team level through this option.                                                                                                      |
| TIU       | TIU Template Reminder Dialog Parameter    | PXRM TIU DIALOG TEMPLATE      | This option lets users edit the TIU TEMPLATE REMINDER DIALOG parameter.                                                                                                                                                                                                                                        |
| DEVL      | Evaluate Coversheet List on Dialog Finish | PXRM EVALUATE COVERSHEET      | This option let the users edit the PXRM DIALOG EVAL DEFINITION parameter, This parameter is used to determine if the CPRS coversheet reminder list should automatically be re-evaluated after the completing a Reminder Dialog                                                                                 |
| NP        | New Reminder Parameters                   | PXRM NEW REMINDER PARAMETERS  | This option allows a user to modify the ORQQPX NEW REMINDER PARAMS parameter, which controls usage and management of the cover sheet reminder list.                                                                                                                                                            |
| LINK      | Link Reminder Dialog to Template          | PXRM DIALOG LINK TO TEMPLATE  | This option is used to link a Reminder Dialog to a TIU Template and the ability to link the TIU Template to a TIU Note Title                                                                                                                                                                                   |
| TEST      | CPRS Coversheet Time Test                 | PXRM CPRS TESTER              | This option is used to run the Reminder Coversheet list and report the time of the reminder evaluation                                                                                                                                                                                                         |

#### Add/Edit Reminder Categories

Reminder categories are maintained with this option. A category defines a group of reminders and may include other sub-categories.

To activate categories so that they appear in the reminders window in CPRS (under Other Categories), use the option CPRS Lookup Categories on page 252 .

The first screen in this option displays the existing reminder categories:

Selection List                Aug 18, 1999 15:04:41         Page:  1 of    1

Reminder Categories

Item Reminder Category

1  DIABETES CLINIC REMINDERS

2  WEIGHT AND NUTRITION

**+ Next Screen   - Prev Screen   ?? More Actions** AD   Add                  PT   List/Print All             QU   Quit

Select Item: Quit//

##### Actions

**AD** - Add a new reminder category.

**PT** - List or print all reminder categories

**QU -** Return to menu

**#** - Enter the item number to be edited.

If you select a reminder category, a description and related reminders are displayed. You can then edit the category.

Edit List                  Apr 18, 2000 15:04:41           Page:    1 of  1

Reminder Category Name: SLC DEMO CATEGORY

Category Description:

This is the text for that summarizes what this category represents. A

category may contain reminders and/or a number of sub-categories.

Sequence:  1   Reminder: SLC CANCER SCREEN

Sequence:  2   Reminder: SLC DIABETIC EYE EXAM

Sequence:  3   Reminder: SLC LIFE STYLE EDUCATION

Sequence:  4   Reminder: SLC PNEUMOCOCCAL VACCINE

Sequence: 90   Reminder: SLC DIABETIC FOOT CARE ED

Sequence: 99   Reminder: MHTEST

Sub-category: SUBSTANCE ABUSE                     Sequence: 3

Sequence:  1   Reminder: TOBACCO EDUCATION

Sequence:  2   Reminder: TOBACCO USE SCREEN

Sequence:  3   Reminder: VA-*PROBLEM DRINKING SCREEN **+ Next Screen   - Prev Screen   ?? More Actions** ED   Edit                     INQ   Inquiry/Print                QU   Quit

Select Action: Quit//ED

##### Actions

**ED** - Edit/Delete this reminder category

**INQ** - List or print this reminder category

**QU -** Return to previous screen.

#### CPRS Lookup Categories

Enter the Reminder Categories that you wish to be displayed on the reminder tree section of the note tab. These will appear in the “Other Categories” folder.

Select CPRS Reminder Configuration Menus Option: CL  CPRS Lookup Categories

Reminder Categories for Lookup may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Location      LOC    [choose from HOSPITAL LOCATION]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [ISC SALT LAKE]

5   System        SYS    [Example.notURL.VA.GOV]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** jg

------- Setting Reminder Categories for Lookup  for User: CRPROVIDER,ONE -------

Select Display Sequence: ?

Display Sequence                     Value

----------------                     -----

1                                    SUBSTANCE ABUSE

5                                    HEPATITIS C

10                                   WEIGHT AND NUTRITION

15                                   SLC REMINDER CATEGORY

20                                   Usability Test Reminders

Select Display Sequence: **25**

Are you adding 25 as a new Display Sequence? Yes// **&lt;Enter&gt;** YES

Display Sequence: 25// **&lt;Enter&gt;** 25

Reminder Category: **??**

Choose from:

Acute Pain

Cancer Pain

Chronic Pain

HEPATITIS C

Pain Management

SLC REMINDER CATEGORY

SUBSTANCE ABUSE

USH POLICY

Usability Test Reminders

WEIGHT AND NUTRITION

Reminder Category: **CRPROVIDER'S** REMINDER CATEGORY

...OK? Yes// **&lt;Enter&gt;** (Yes)

Select Display Sequence: &lt;Enter&gt;

#### CPRS Cover Sheet Reminder List

Use this option to enter reminders that will be displayed on the CPRS cover sheet if the New Reminder Parameter option is set to No. If the New Reminders Parameter is set to Yes (ORQQPX NEW REMINDER PARAMS; see the description on the next page), you won’t use this option; instead you will manage the cover sheet list through the CPRS GUI.

Select CPRS Reminder Configuration Menus Option: CS  CPRS Cover Sheet Reminder List

Clinical Reminders for Search may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Location      LOC    [choose from HOSPITAL LOCATION]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [ISC SALT LAKE]

5   System        SYS    [Example.notURL.VA.GOV]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** jg

-------- Setting Clinical Reminders for Search  for User: CRPROVIDER,ONE --------

Select Display Sequence: ?

Display Sequence                     Value

----------------                     -----

1                                    VA-DIABETIC FOOT CARE ED.

2                                    VA-TOBACCO EDUCATION

5                                    VA-*PNEUMOCOCCAL VACCINE

10                                   VA-INFLUENZA VACCINE

15                                   VA-*BREAST CANCER SCREEN

25                                   TOBACCO USE SCREEN

30                                   VA-*CHOLESTEROL SCREEN (M)

35                                   VA-*COLORECTAL CANCER SCREEN (FOBT)

40                                   VA-*HYPERTENSION SCREEN

Select Display Sequence: **20**

Display Sequence: 20// **&lt;Enter&gt;** 20

Clinical Reminder: MENTAL HEALTH TESTS

Select Display Sequence: **&lt;Enter&gt;**

#### New Reminder Parameters - Edit Cover Sheet Reminder List

This option lets you set the parameter ORQQPX NEW REMINDER PARAMS for editing cover sheet reminders. **If this option is set to YES, you won’t use the option CPRS Cover Sheet Reminder List.**

##### New Reminder Parameters Example

Select CPRS Reminder Configuration Option: NP  New Reminder Parameters

Use New Reminder Parameters may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    [Example.notURL.VA.GOV]

5   Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** OC

--------- Setting Use New Reminder Parameters  for User: CRPROVIDER,ONE ---------

USE NEW REMINDER PARAMS: YES

There are two possible cover sheet lists for a user, one when ORQQPX NEW REMINDER PARAMS is “NO” and one when it is “YES.” Determining the value of ORQQPX NEW REMINDER PARAMS for a user is not always a straightforward exercise. For a basic understanding of how parameters work in CPRS, see the CPRS Technical Manual or Kernel Toolkit documentation.

The precedence for ORQQPX NEW REMINDER PARAMS is shown in the above example.

If it is defined at the User level, then that takes precedence.

If is not defined at the User level, then a check is made at the Service level.

If it is not defined at the Service level, then a check is made at the Division level, and so on until a value is determined.

If the checking proceeds all the way to the Package level and nothing is defined at that level, then it defaults to “NO.”

There are two kinds of users with respect to the management of cover sheet lists.

Regular users

Reminder managers

A reminder manager is anyone who has PXRM MANAGERS MENU as a primary or secondary menu option. A regular user can only edit their own cover sheet list, while a reminder manager can edit and manage cover sheet lists at all levels.

We recommend that ORQQPX NEW REMINDER PARAMS be set to “YES” for all users, because of the enhanced functionality that it makes available.

It is possible that a site may choose to use the old cover sheet list functionality, so we will start with a discussion of how things work when ORQQPX NEW REMINDER PARAMS is “NO.”

If your site is using the new cover sheet list functionality, then you can skip the following section.

##### ORQQPX NEW REMINDER PARAM set to “NO”

A regular user accesses the editing form by clicking on Options under the tools menu

<!-- image -->

Then click on Clinical Reminders to get to the editing form.

<!-- image -->

Highlight an item in the **Reminders not being displayed** field and then click the Add arrow “&gt;” to add it to the **Reminders being displayed** field. You may hold down the Control key and select more than one reminder at a time. When you have all of the desired reminders in the **Reminders being displayed** field, you may highlight a reminder and use the up and down buttons on the right side of the dialog to change the order in which the reminders will be displayed on the Cover Sheet.

**Sort by**

Select Display Order to display the reminders in the order that you choose. Click Alphabetical to have the reminders displayed in alphabetic order.

This list is the list defined at the user level and takes precedence over any lists defined at higher levels, i.e. Location, Service, Division, System, or Package. A regular user cannot edit the list at any of these higher levels. A reminder manager can edit the list at these higher levels through the CPRS Cover Sheet Reminder List (CS) option described in the CPRS Cover Sheet Reminder List section.

##### ORQQPX NEW REMINDER PARAM set to “YES”

The new type of cover sheet list provides a great deal of flexibility, allowing the reminder manager to build lists at the User, User Class, Location, Service, Division, and System levels. Note that these levels are not exactly the same as with the old type of list, where they were User, Location, Service, Division, and Package.

An important distinction between the new type of list and the old type is the new list is cumulative and removable. For example, if a list is defined at the system level, reminders can be added to or removed from the list at the User level. There may be certain reminders that should be on all users’ coversheet lists and these can be locked by the reminder manager.

The reminder manager accesses this functionality by clicking on the reminder button next to the CWAD button in the upper right hand corner of the CPRS GUI.

Click on Action then click on Edit Cover Sheet Reminder List.

##### Edit Cover Sheet Reminder List

<!-- image -->

This reminder manager form provides very extensive cover sheet list management capabilities. It consists mainly of three large list areas.

Cover Sheet Reminders (Cumulative List) displays selected information on the Reminders that will be displayed on the Cover Sheet.

Available Reminders &amp; Categories lists all available Reminders and serves as a selection list.

User Level Reminders displays the Reminders that have been added to or removed from the cumulative list.

You may sort the Reminders in *Cover Sheet Reminders (Cumulative List)* by clicking on any of the column headers. Click on the Seq (Sequence) column header to view the Reminders in the order in which they will be displayed on your cover sheet.

##### Icon Legend

An icon legend is displayed to the right of *Cover Sheet Reminders (Cumulative List)* .

Folder icon represents a group of reminders

Red alarm clock represents an individual reminder.

Plus sign in the first column means a reminder has been added to the list

Minus sign in the first column means a reminder has been removed from the list

Padlock icon means you can’t remove reminder (mandatory)

###### Cover Sheet Reminders (Cumulative List)

The Level column of the Cover Sheet Reminders (Cumulative List) field displays the originating authority of the Reminder, which can include System, Division, Location, User Class, and User. Reminders on this list that display a small gray padlock icon at the beginning of the line cannot be removed. These Reminders are mandatory. The Seq (Sequence) column defines the order in which the Reminders will be displayed on the Cover Sheet. If there are two or more Reminders with the same sequence number, the Reminders are listed by level (System, Division, Service, Location, User class, User).

###### Available Reminders &amp; Categories

This area displays all of the Reminders and Categories available to the user. Categories are groups of related reminders that can be added as a group. Individual reminders within a category can be removed from the User Level Reminders field. Highlight a Reminder or Category from the field and click the right arrow to add them to the User Level Reminders field.

###### Select Cover Sheet Parameter Level to Display / Edit

This section has radio buttons for System, Division, Service, Location, User Class, and User. When one of the radio buttons is clicked, the list of reminders included at that parameter level appears in the box on the lower right-hand side of the form. You can then perform any of the following editing actions:

To add a reminder, highlight the desired reminder in the Available Reminders &amp; Categories field and click the right arrow button.

To delete a reminder, highlight the reminder and click the left arrow.

To make a reminder mandatory, select a reminder and then click on the Lock button.

To make a mandatory reminder no longer mandatory, click on either the Add or Remove buttons, depending on if you want it to remain on the list or be removed.

To determine the order in which the reminders will be displayed on the Cover Sheet, change the reminder’s Sequence number. To do this click on the reminder and then change its sequence number in the sequence number box.

###### View Cover Sheet Reminders

Since the cover sheet list is cumulative and removable, it is not always easy to determine exactly which reminders will be on a user’s cover sheet list. Clicking on the **View Cover Sheet Reminders** button will display the final list for the user that has been selected at the User parameter level.

<!-- image -->

###### User level Cover Sheet Reminder Screen

A user level editing form is also available by clicking on the Tools menu, then options, then Clinical Reminders. This is the same sequence as shown in the previous section for getting to the user editing form.

This form lets the user add or remove reminders (with the exception of locked reminders) to their cover sheet list. The functionality is basically the same as that described above.

<!-- image -->

##### Setting User and System Levels

The following Forum dialog might clarify some issues about setting levels:

Subj: CPRS COVERSHEET REMINDERS SETUP THRU GUI

-------------------------------------------------------------------------------

We are having some problems with appropriate clinical reminders showing on coversheet when set up at SYSTEM or SERVICE level in GUI. Reminders set for SYSTEM are also showing for a user in a service that is also set up (EX: Medical). In other words, all of the reminders set for Medical Service show on coversheet as well as those set under SYSTEM. When I completely remove the GUI setup for SYSTEM, users no longer have those clinical reminders show on coversheet. I need the SYSTEM setting for those not set up in a service.

Per NOIS CAH-1003-31162, site had a similar problem and resolution stated there was a specific hierarchy (that seems to be different from others). I thought that if there was something set at USER level, that would take precedence over SERVICE or SYSTEM, but that doesn't seem to be true in this case.

MY QUESTION IS THIS: Can someone explain what the hierarchy is when setting clinical reminders in GUI vs VistA. Should we only have setup in one or the other? I cannot find anything on this in documentation.

1. The hierarchy for reminders displaying on the GUI cover sheet is cumulative, so there is really no hierarchy, only the ability to add to the list at different levels. System displays to all users, division adds to system for users in that division, service adds to division and/or system for users in that service, etc.

There use to be a hierarchy but that changed some time ago.

1. Check out HUN-0701-20018    RESTRICTED REMINDERS

You can have it both ways - Cumulative and Restricted.

1. You just have to remember you have two different set-ups if you add or subtract reminders.
2. You have to have the parameter for using the new reminder parameters set to yes to take advantage of this:

Select CPRS Reminder Configuration Option: NP  New Reminder Parameters

Use New Reminder Parameters may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    [Example.notURL.VA.GOV]

Enter selection: 4  System   [Example.notURL.VA.GOV]

-- Setting Use New Reminder Parameters  for System: Example.notURL.VA.GOV ----

USE NEW REMINDER PARAMS: YES//

**HUN-0701-20018     RESTRICTED REMINDERS**

Description:

Our mental health providers should only see certain reminders due on a patient. I have them set under service to see:

Setting ORQQPX COVER SHEET REMINDERS  for Service: MENTAL HEALTH ------

Select Display Sequence: ?

Display Sequence                     Value

----------------                     -----

10                                   LR1006

20                                   LR581016

30                                   LR581011

40                                   LR581002

50                                   LR581007

They are seeing all reminders set at SYSTEM level + the additional reminders. Is something set up wrong or is this now cumulative? Is there a way so that they will only see the reminders relative to their service?

(12) Jul 05, 2001@09:43:26        CRSUPPORT,ONE

Well, we took a look at the parameters and the following...

Select  CPRS Reminder Configuration Option: np  New Reminder Parameters

Use New Reminder Parameters may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [VAMC TWO PIA]

4   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

5   Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: 4  System   EXAMPLE.NOTURL.VA.GOV

-- Setting Use New Reminder Parameters  for System: EXAMPLE.NOTURL.VA.GOV ---

USE NEW REMINDER PARAMS: NO//

These can be set to YES or NO at any of the levels. I suggested they set the Mental Health and Optometry service to NO. Hopefully, now they will only see their DUE reminders and not everyone else’s.

The other alternative is to set the ORQQPX REMINDER FOLDERS to Other Categories for these services. Then within the Other Categories, set up specific category names for the service's specific reminders. This would group the reminders together.

#### Cover Sheet Reminder Report

This option lets you run the cover sheet reminder report.

There are old and new methods for building the cover sheet list of reminders. When the parameter ORQQPX NEW REMINDER PARAM is set to “YES” the list of reminders evaluated on a user’s cover sheet is built in a cumulative manner.

The new type of cover sheet list provides a great deal of flexibility, allowing the reminder manager to build lists at the User, User Class, Location, Service, Division, and System levels. Note that these levels are not exactly the same as with the old type of list, where they were User, Location, Service, Division, and Package. The new reminder parameters system is much more flexible, that is why it use is recommended and the vast majority of sites are using it.

An important distinction between the new type of list and the old type is the new list is cumulative and removable. For example, if a list is defined at the system level, reminders can be added to or removed from the list at the User level. There may be certain reminders that should be on all users’ coversheet lists and these can be locked by the reminder manager.

Because the final list for a user is built cumulatively, it can be difficult to determine how a user’s list is arrived at. The cover sheet reminder report can help make that determination. The cumulative list is built in the order: System, Division, Service, Location, User Class, and User. This report will show you what reminders are added or removed at each level.

When the report starts you are given the option to view the Cover Sheet List using the new reminder parameters or the original parameters. Since most sites use the new reminder parameters that is the default.

Clinical Reminders Cover Sheet Reminder List Report

Do you want to use the new reminder parameters?

Select one of the following:

1         YES

2         NO

Enter response: YES//YES

Select from the following levels:

1 - PACKAGE

2 - SYSTEM

3 - DIVISION

4 - SERVICE

5 - LOCATION

6 - USER CLASS

7 - USER

8 - CPRS

Enter your list for the report:  (1-8):

You can choose one of more of these, note that if your choice includes CPRS, only the CPRS list is built. That is because the CPRS list is a result of complex accumulation and mixing in other levels would skew the results. Because the API used to determine the CPRS cover sheet list has two inputs: user and location, you are prompted for these. Once it has these inputs, the report then accumulates in the following order of levels: Package, System, Division, Service (see below for details), Location, User Class (see below for details), and User.

Service - the value of field #29, Service/Section, in file #200 for the user.

User Class – a list of User Classes and associated reminders is defined in the parameter ORQQPX COVER SHEET REM CLASSES. For each User Class in the list, a check is made to determine if the user is a member, and if they are, the reminders defined for that user class are added to the list.

When the CPRS level is selected the report, header shows the User and Location that were input, the user’s Service, and cover sheet User Classes the user is a member of.

Enter your list for the report:  (1-8): 8

Select the user:    XXXXXX,YYYY     XY

Select the location:    PULMONARY CLINIC

Browse or Print? B//

Report Criteria

Use new cover sheet parameters: YES

Selected levels:

CPRS

User - XXXXX,YYYY

Location - PULMONARY CLINIC

Service - IRM

User Class - PHYSICIAN

The report first displays the basic parameter list. In the basic parameter list, the first piece is the sequence (display order), the second piece starts with two characters, the first character can be: L = locked, N = normal, R = remove. The second character can be: C= category, R = reminder. The number is the category or reminder internal entry number (IEN). The status of the reminder is shown in the third piece. The basic list is processed using the information in the second and third pieces to determine the final list. When it is a reminder category, the reminders in the category are added to the list. Each reminder on the list is checked to make sure it exists, is active, and its Usage allows for display on the Cover Sheet. If it fails any of these tests it is not included on the display list.

When the list contains a category, it is expanded to show the reminders in the category, e.g., LIST(21) below.

If there are two or more Reminders with the same sequence number, the Reminders are listed by level (System, Division, Service, Location, User Class, User).

Reminder list at CPRS level

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

LIST(9)=104000^NR310

LIST(10)=105000^NR4^INACTIVE

LIST(11)=106000^NR355^

LIST(12)=206000^NR298^

LIST(13)=306000^NR342^

LIST(14)=406000^NR292^

LIST(15)=506000^NR315^

LIST(16)=606000^NR306^

LIST(17)=706000^NR305^

LIST(18)=806000^NR363^

LIST(19)=107000^NR104

LIST(20)=207000^NR128

LIST(21)=307000^NC27

LIST(21.000001)=307000.000001^121

LIST(21.000002)=307000.000002^124

LIST(22)=507000^NR93

LIST(23)=607000^NR568022

Reminders in Display Order

Name - XYZ MIXED TERM  (IEN=310)

Print Name - Mixed Term

Name - XYZ ACSUB TEST  (IEN=355)

Print Name - XYZ ACSUB test with drugs

Name - VA-DEPRESSION SCREENING  (IEN=104)

Print Name - Depression Screening

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - XYZ AIMS 1  (IEN=298)

Print Name - XYZ AIMS 1

Name - VA-WH MAMMOGRAM SCREENING  (IEN=128)

Print Name - Mammogram Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - XYZ ART TEST  (IEN=342)

Print Name - XYZ ART test

Name - VA-WH PAP SMEAR SCREENING  (IEN=121)

Print Name - PAP Smear Screening

Name - VA-WH PAP SMEAR REVIEW RESULTS  (IEN=124)

Print Name - PAP Smear Review Results

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - XYZ ASI TEST  (IEN=292)

Print Name - XYZ ASI

Name - XYZ AUDIT  (IEN=315)

Print Name - XYZ AUDIT 1

Name - ZZANTHONY MENTAL  (IEN=93)

Print Name - AGP MENTAL HEALTH TEST

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - XYZ AUIR  (IEN=306)

Print Name - XYZ AUIR

Name - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN  (IEN=568022)

Print Name - Iraq&amp;Afghan Post-Deployment Screen

Name - XYZ BDI2  (IEN=305)

Print Name - XYZ BDI2

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

Name - XYZ BLOOD PRESSURE  (IEN=363)

Print Name - XYZ Blood Pressure

There are 20 reminders on the list.

If you select other levels and do not include CPRS, the list of accumulated reminders for each level is displayed. This provides great flexibility, you can see what reminders are on the list for a selected level. For example, you can see what is defined at the System level or for a particular User Class. You can also see how the accumulation works for any set of selected levels. As an illustration, in this example levels 2-7 have been selected.

Enter your list for the report:  (1-8): 2-7

Select the division:    SALT LAKE CITY HCS  UT  VAMC  660

Select the service:    MEDICINE

Select the location:    PULMONARY CLINIC

Select the user class:    CLINICAL COORDINATOR

Select the user:    XXXXX,YYYY

Browse or Print? B// B

Report Criteria

Use new cover sheet parameters: YES

Selected levels:

SYSTEM

DIVISION

Value - SALT LAKE CITY HCS

SERVICE

Value - MEDICINE

LOCATION

Value - PULMONARY CLINIC

USER CLASS

Value - CLINICAL COORDINATOR

USER

Value - XXXXX,YYYY

Under the new reminder parameters, the list is processed in the order: System, Division, Service, Location, User Class, and User, with the ability to add or remove reminders at each level. The final list is the result of processing each of the selected levels in the above order.

Reminder list at SYSTEM level.

LIST(1)=102000^NR660004

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

When the above list is processed it becomes:

Reminders in Display Order

Name - AGETEST  (IEN=660004)

Print Name - AGETEST

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 7 reminders on the list.

The following shows how the list changes as the selected levels are processed:

Reminder list at SYSTEM, DIVISION levels.

LIST(1)=102000^NR660004

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

Reminders in Display Order

Name - AGETEST  (IEN=660004)

Print Name - AGETEST

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 7 reminders on the list.

Reminder list at SYSTEM, DIVISION, SERVICE levels.

LIST(1)=102000^NR660004

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

LIST(9)=204000^NR2^INACTIVE

LIST(10)=304000^NC6

LIST(10.000001)=304000.000001^660027

LIST(10.000002)=304000.000002^660026

LIST(10.000003)=304000.000003^2^INACTIVE

LIST(10.000004)=304000.000004^9^INACTIVE

LIST(10.000005)=304000.000005^31^INACTIVE

LIST(11)=504000^NR568022

Reminders in Display Order

Name - AGETEST  (IEN=660004)

Print Name - AGETEST

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - TOBACCO EDUCATION  (IEN=660027)

Print Name - Tobacco Cessation Education

Name - TOBACCO USE SCREEN  (IEN=660026)

Print Name - JG TOBACCO USE SCREEN

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN  (IEN=568022)

Print Name - Iraq&amp;Afghan Post-Deployment Screen

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 10 reminders on the list.

Reminder list at SYSTEM, DIVISION, SERVICE, LOCATION levels.

LIST(1)=102000^NR660004

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

LIST(9)=204000^NR2^INACTIVE

LIST(10)=304000^NC6

LIST(10.000001)=304000.000001^660027

LIST(10.000002)=304000.000002^660026

LIST(10.000003)=304000.000003^2^INACTIVE

LIST(10.000004)=304000.000004^9^INACTIVE

LIST(10.000005)=304000.000005^31^INACTIVE

LIST(11)=504000^NR568022

LIST(12)=105000^NR4^INACTIVE

Reminders in Display Order

Name - AGETEST  (IEN=660004)

Print Name - AGETEST

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - TOBACCO EDUCATION  (IEN=660027)

Print Name - Tobacco Cessation Education

Name - TOBACCO USE SCREEN  (IEN=660026)

Print Name - JG TOBACCO USE SCREEN

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN  (IEN=568022)

Print Name - Iraq&amp;Afghan Post-Deployment Screen

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 10 reminders on the list.

Reminder list at SYSTEM, DIVISION, SERVICE, LOCATION, USER CLASS levels.

LIST(1)=102000^NR660004

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

LIST(9)=204000^NR2^INACTIVE

LIST(10)=304000^NC6

LIST(10.000001)=304000.000001^660027

LIST(10.000002)=304000.000002^660026

LIST(10.000003)=304000.000003^2^INACTIVE

LIST(10.000004)=304000.000004^9^INACTIVE

LIST(10.000005)=304000.000005^31^INACTIVE

LIST(11)=504000^NR568022

LIST(12)=105000^NR4^INACTIVE

LIST(13)=106000^NC7^

LIST(13.000001)=106000.000001^27

LIST(13.000002)=106000.000002^62

LIST(13.000003)=106000.000003^124

Reminders in Display Order

Name - AGETEST  (IEN=660004)

Print Name - AGETEST

Name - VA-HEPATITIS C RISK ASSESSMENT  (IEN=27)

Print Name - Hepatitis C Risk Assessment

Name - PJH TEST 2  (IEN=62)

Print Name - Patch5 VA-Pain Screening

Name - VA-WH PAP SMEAR REVIEW RESULTS  (IEN=124)

Print Name - PAP Smear Review Results

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - TOBACCO EDUCATION  (IEN=660027)

Print Name - Tobacco Cessation Education

Name - TOBACCO USE SCREEN  (IEN=660026)

Print Name - JG TOBACCO USE SCREEN

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN  (IEN=568022)

Print Name - Iraq&amp;Afghan Post-Deployment Screen

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 13 reminders on the list.

Reminder list at SYSTEM, DIVISION, SERVICE, LOCATION, USER CLASS, USER levels.

LIST(2)=202000^NR793

LIST(3)=302000^NR311

LIST(4)=402000^NR360

LIST(5)=502000^NR485

LIST(6)=602000^NR87

LIST(7)=702000^NR453^INACTIVE

LIST(8)=802000^NR406

LIST(9)=204000^NR2^INACTIVE

LIST(10)=304000^NC6

LIST(10.000001)=304000.000001^660027

LIST(10.000002)=304000.000002^660026

LIST(10.000003)=304000.000003^2^INACTIVE

LIST(10.000004)=304000.000004^9^INACTIVE

LIST(10.000005)=304000.000005^31^INACTIVE

LIST(11)=504000^NR568022

LIST(12)=105000^NR4^INACTIVE

LIST(13)=106000^NC7^

LIST(13.000001)=106000.000001^27

LIST(13.000002)=106000.000002^62

LIST(13.000003)=106000.000003^124

LIST(14)=107000^NR104

LIST(15)=207000^NR128

LIST(16)=307000^NC27

LIST(16.000001)=307000.000001^121

LIST(16.000002)=307000.000002^124

LIST(17)=507000^NR93

Note that LIST(1) has been removed, so at the User level reminder 660004 is marked for removal.

Reminders in Display Order

Name - VA-HEPATITIS C RISK ASSESSMENT  (IEN=27)

Print Name - Hepatitis C Risk Assessment

Name - PJH TEST 2  (IEN=62)

Print Name - Patch5 VA-Pain Screening

Name - VA-WH PAP SMEAR REVIEW RESULTS  (IEN=124)

Print Name - PAP Smear Review Results

Name - VA-DEPRESSION SCREENING  (IEN=104)

Print Name - Depression Screening

Name - VA-TBI SCREENING  (IEN=793)

Print Name - TBI Screening

Name - VA-WH MAMMOGRAM SCREENING  (IEN=128)

Print Name - Mammogram Screening

Name - DT-EXAMPLE FOR PL  (IEN=311)

Print Name - IHD Lipid Profile - DT PL example

Name - TOBACCO EDUCATION  (IEN=660027)

Print Name - Tobacco Cessation Education

Name - TOBACCO USE SCREEN  (IEN=660026)

Print Name - JG TOBACCO USE SCREEN

Name - VA-WH PAP SMEAR SCREENING  (IEN=121)

Print Name - PAP Smear Screening

Name - AAA SCREENING  (IEN=360)

Print Name - AAA Risk Screen

Name - SCREEN FOR AAA  (IEN=485)

Print Name - Screen for Abd Aortic Aneurysm

Name - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN  (IEN=568022)

Print Name - Iraq&amp;Afghan Post-Deployment Screen

Name - ZZANTHONY MENTAL  (IEN=93)

Print Name - AGP MENTAL HEALTH TEST

Name - ZZ-IHD ASPIRIN AND BETA-BLOCKER  (IEN=87)

Print Name - IHD Aspirin and Beta-Blocker

Name - VA-MH HIGH RISK NO-SHOW FOLLOW-UP  (IEN=406)

Print Name - High Risk MH No-Show Follow-up

There are 16 reminders on the list.

If you choose the old parameters then list of levels is:

Select from the following levels:

1 - PACKAGE

2 - SYSTEM

3 - DIVISION

4 - SERVICE

5 - LOCATION

6 - USER

7 - CPRS

Enter your list for the report:  (1-7):

You can choose one of more of these, note that if your choice includes CPRS only the CPRS list is displayed. That is because the CPRS list is built for a selected user and location. If you select other levels and do not include CPRS  the list of reminders for each selected level is displayed.

In this example Service, Location, and User were selected. The selection criteria are displayed at the beginning of the report.

Report Criteria

Use new cover sheet parameters: NO

Selected levels:

SERVICE

Value - MEDICINE

LOCATION

Value - PULMONARY CLINIC

USER

Value - XXXXX,YYYYY

For each selected level, the basic parameter list is first displayed. The first piece on the right side of the equal side is the display order, the second piece is the internal entry number (IEN) of the reminder definition, and the status of the reminder is shown in the third piece.  This list is processed to create the actual list, each reminder is checked to determine if it exists, is active, and its Usage allows display on the Cover Sheet. Note both reminders on this list are inactive so there are 0 reminders on the display list.

Reminder list at the SERVICE level.

LIST(1)=1^28^INACTIVE

LIST(2)=2^26^INACTIVE

There are 0 reminders on the list.

Reminder list at the LOCATION level.

LIST(1)=1^660027

LIST(2)=2^660056

LIST(3)=3^660039

Name - TOBACCO EDUCATION  (IEN=660027)

Print Name - Tobacco Cessation Education

Name - JG BREAST CANCER SCREEN  (IEN=660056)

Print Name - Breast Cancer Screen

Name - SLC DIABETIC EYE EXAM  (IEN=660039)

Print Name - SLC Eye Exam

There are 3 reminders on the list.

Reminder list at the USER level.

LIST(1)=1^8^INACTIVE

LIST(2)=2^660066^DOES NOT EXIST

LIST(3)=3^70

LIST(4)=4^73

LIST(5)=5^66

LIST(6)=6^245

Name - VA-IHD LIPID PROFILE  (IEN=70)

Print Name - IHD Lipid Profile

Name - VA-IHD ELEVATED LDL  (IEN=73)

Print Name - IHD Elevated LDL

Name - VA-PAIN SCREENING  (IEN=66)

Print Name - PAIN SCREENING

Name - XYZ BREAST EXAM  (IEN=245)

Print Name - XYZ Breast Exam Dialog Test

There are 4 reminders on the list.

Under the old parameter system, the levels are processed left to right and the last level on the list is used, thus in this example the Final Reminder List is the same as the list at the User level.

Final Reminder List

Name - VA-IHD LIPID PROFILE

Print Name - IHD Lipid Profile

Name - VA-IHD ELEVATED LDL

Print Name - IHD Elevated LDL

Name - VA-PAIN SCREENING

Print Name - PAIN SCREENING

Name - XYZ BREAST EXAM

Print Name - XYZ Breast Exam Dialog Test

There are 4 reminders on the list.

#### Mental Health Dialogs Active

This option lets you modify the “Mental Health Active” CPRS parameter. You can activate mental health dialogs for reminder resolution processing at a user, service, division, or system level. When activated, mental health tests in a reminder dialog can be performed.

Select CPRS Reminder Configuration Option: MH  Mental Health Dialogs Active

Mental Health Active may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    EXAMPLE.NOTURL.VA.GOV

Enter selection: 1  User   NEW PERSON

Select NEW PERSON NAME: CRPROVIDER,SIX     sc

---------- Setting Mental Health Active  for User: CRPROVIDER,SIX -------

MENTAL HEALTH ACTIVE: YES// &lt;Enter&gt;

CA     Add/Edit Reminder Categories

CL     CPRS Lookup Categories

CS     CPRS Cover Sheet Reminder List

MH     Mental Health Dialogs Active

PN     Progress Note Headers

RA     Reminder GUI Resolution Active

DL     Default Outside Location

PT     Position Reminder Text at Cursor

NP     New Reminder Parameters

Select CPRS Reminder Configuration Option: &lt;Enter&gt;

#### Progress Note Headers

This option lets you modify the header inserted into the progress note when processing a reminder. It can be modified for user, location, or service. The default header is Clinical Reminders Activity.

Select CPRS Reminder Configuration Menus Option: **PN** Progress Note Headers

Progress Note Header may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Location      LOC    [choose from HOSPITAL LOCATION]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [REGION 5]

5   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

6   Package       PKG    [CLINICAL REMINDERS]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** jg

------------ Setting Progress Note Header  for User: CRPROVIDER,ONE -------

PROGRESS NOTE HEADER: **?**

This response can be free text.

PROGRESS NOTE HEADER: **GREEN NOTES**

<!-- image -->

#### Reminder GUI Resolution Active

This option lets you activate GUI reminder resolution processing at a user, service, division, or system level. When activated, a reminders drawer is available on the notes tab for selecting and processing reminders.

Select CPRS Reminder Configuration Menus Option: RA  Reminder GUI Resolution Active

Reminders Active may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** jg

-------------- Setting Reminders Active  for User: CRPROVIDER,ONE --------------

REMINDERS ACTIVE: YES// &lt;Enter&gt;

TIU Template Reminder Dialog Parameter

This option lets users edit the TIU TEMPLATE REMINDER DIALOG parameter.

Select CPRS Reminder Configuration Option: tiu  TIU Template Reminder Dialog Parameter

Reminder Dialogs allowed as Templates may be set for the following:

1   User          USR    [choose from NEW PERSON]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [choose from INSTITUTION]

5   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

Enter selection: 1  User   NEW PERSON

Select NEW PERSON NAME:    CRPROVIDER,TWO     tc

---- Setting Reminder Dialogs allowed as Templates  for User: CRCOORDINATOR,ONE ----

Select Display Sequence: ??

Contains Reminder Dialogs that are allowed to be used as TIU Templates.

This parameter is different than most others in that each level is

cumulative, so all Reminder Dialogs at the System, Division, Service

and User levels can be used in Templates.

Select Display Sequence: 1

Are you adding 1 as a new Display Sequence? Yes//   YES

Display Sequence: 1//    1

Clinical Reminder Dialog:  JG DIABETIC EYE EXAM     reminder dialog     LOCAL

Select Display Sequence:

#### Evaluate Coversheet List on Dialog Finish

If this is set to YES, when clicking finish on a reminder dialog the entire coversheet list of reminders will be evaluated. The default is NO.

##### Example

Select CPRS Reminder Configuration &lt;TEST ACCOUNT&gt; Option:  Evaluate Coversheet L

ist on Dialog Finish

Evaluate Definition On Dialog Finish may be set for the following:

1   User          USR    [choose from NEW PERSON]

7   System        SYS    [CPRS32.FO-SLC.MED.VA.GOV]

Enter selection: 1  User   NEW PERSON

Select NEW PERSON NAME:    PROVIDER,CPRS T            CTP

-- Setting Evaluate Definition On Dialog Finish  for User: PROVIDER,CPRS T --

Evaluate coversheet on dialog finish: YES

#### Default Outside Location

Within portions of a reminder dialog where historical encounter information is entered, a new parameter, ORQQPX DEFAULT LOCATIONS, can be set up to define default outside locations for the PXRM OUTSIDE LOCATION prompt. Each free-text entry in this multi-valued parameter will appear at the top of the list of locations in the drop-down list in CPRS. If a number is entered as the free-text value, CPRS will attempt to locate an entry in the Institution file (#4) with the same internal entry number.

##### Example

Select CPRS Reminder Configuration Option: dl  Default Outside Location

Default Outside Locations may be set for the following:

1   User          USR    [choose from NEW PERSON]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [choose from INSTITUTION]

5   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

6   Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,TWO** TC

---------- Setting Default Outside Locations  for User: CRPROVIDER,ONE ----------

Select Display Sequence: 1

Display Sequence: 1//    1

Outside Location (Text or Pointer): 663

Select Display Sequence: 2

Are you adding 2 as a new Display Sequence? Yes// &lt;Enter&gt;  YES

Display Sequence: 2// **&lt;Enter&gt;**

Outside Location (Text or Pointer): **Local Pharmacy**

Select Display Sequence: **3**

Are you adding 3 as a new Display Sequence? Yes// **&lt;Enter&gt;** YES

Display Sequence: 3// **&lt;Enter&gt;** 3

Outside Location (Text or Pointer): **640**

Select Display Sequence: **4**

Are you adding 4 as a new Display Sequence? Yes// **&lt;Enter&gt;** YES

Display Sequence: 4// **&lt;Enter&gt;** 4

Outside Location (Text or Pointer): **Outside Physician's Office**

Select Display Sequence: **???**

Display Sequence                     Value

----------------                     -----

1                                    663

2                                    Local Pharmacy

3                                    640

4                                    Outside Physician's Office

Default Location as it appears in CPRS:

Note that Seattle, WA and Palo Alto are entries in the institution file with internal entry numbers of 663 and 640, respectively.

#### Position Reminder Text at Cursor

The default behavior of reminder dialogs is to insert any text generated by the reminder dialog at the bottom of the current note. When the ORQQPX REMINDER TEXT AT CURSOR parameter is set, text will be inserted at the current cursor location.

Select CPRS Reminder Configuration Option: PT  Position Reminder Text at Cursor

Position Reminder Text at Cursor may be set for the following:

1   User          USR    [choose from NEW PERSON]

3   Service       SRV    [choose from SERVICE/SECTION]

4   Division      DIV    [choose from INSTITUTION]

5   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **&lt;Enter&gt;** CRPROVIDER,ONE    OC

------ Setting Position Reminder Text at Cursor  for User: CRPROVIDER,ONE ------

REMINDER TEXT AT CURSOR: ?

Insert Reminder Dialog Generated Text at Cursor Location.

Select one of the following:

0         NO

1         YES

REMINDER TEXT AT CURSOR: YES

#### Link Reminder Dialog to Template

This automatically links a reminder dialog to a shared template and/or progress note title.

Select Dialog Definition: VA-DEPRESSION SCREEN

Enter template name: Depression Screen Template

Link template to Document Title? YES  Select No to not attach to a note title and link to  a new entry in shared  templates

Select Document Definition: C&amp;P MENTAL DISORDERS     TITLE

Template Depression Screen Template created

Template Depression Screen Template added to Shared Folder.

Template Depression Screen Template link to note title C&amp;P MENTAL DISORDERS

#### CPRS Coversheet Time Test

If a site is experiencing long load times for coversheet reminders, the Coversheet Time Test can be used to see if there is an issue with a particular reminder definition

Select User: CPRSPROVIDER,THREE              TR          TEST PHYSICIAN

Select Location 20 MINUTE

Browse or Print? B// Print

DEVICE: HOME// ;;99999  PSUEDO-TERMINAL

Total time to build reminder list: 0 seconds

Reminder: DIABETES CREATININE (IEN=33)

Reminder CPU evaluation time: 1 milliseconds

Reminder wall clock evaluation time: 0 seconds

Total number of reminders evaluated: 20

Elapsed wall clock time: 0 seconds

Total CPU coversheet evaluation time: 30 milliseconds

Longest CPU evaluation time

Reminder: VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN (IEN=568022)

Reminder CPU evaluation time: 7 milliseconds

Longest wall clock evaluation time

Reminder: DIABETES CREATININE (IEN=33)

Reminder wall clock evaluation time: 0 seconds

#### New Reminder Parameters

This option allows a user to modify the ORQQPX NEW REMINDER PARAMS parameter, which controls usage and management of the Coversheet\_Reminder\_Report.

#### GEC Status Check Active

A GEC Status Indicator may be added to the CPRS GUI Tools drop-down menu, to be viewed at any time and used to close the referral if needed. It may be set at the User or Team level through this option. See the GEC Referral Report section for more details.

Select CPRS Reminder Configuration Option: GEC  GEC Status Check Active

Gec Status Check may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Team          TEA    [choose from TEAM]

Enter selection: **1** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** OC

-------------- Setting Gec Status Check  for User: CRPROVIDER,ONE -------------

GEC Status Check: YES// &lt;Enter&gt;

#### WH Print Now Active

The “Print Now” button on the Women’s Health review reminders is optional. A parameter can be set (at the system level) to allow the “Print Now” button to be added to the dialog. By default, “Print Now” is turned off: the CPRS Reminder Configuration Option called WH Print Now Active is released with a Value of NO. If the value is changed to YES, the “Print Now” button will appear on the dialog. Whether the “Print Now” button is added to the dialog or not, the default will always be that the letter is queued to the WH package.

The text in the progress note will be one of the following:

Print Now Active/ **Yes** **: Letter queued to print at Device Name on finish Date/Time**

Print Now Active/ **No** : Letter queued to WH package Date/Time

Select CPRS Reminder Configuration Option: WH  WH Print Now Active

WH Print Now Option Active may be set for the following:

1   System        SYS    [EXAMPLE.NOTURL.VA.GOV]

2   Division      DIV    [choose from INSTITUTION]

3   Location      LOC    [choose from HOSPITAL LOCATION]

4   Service       SRV    [choose from SERVICE/SECTION]

5   Team (OE/RR)  OTL    [choose from OE/RR LIST]

6   User          USR    [choose from NEW PERSON]

Enter selection: **6** User   NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** OC

--------- Setting WH Print Now Option Active  for User: CRPROVIDER,ONE --------

Value: ?

Enter either 'Y' or 'N'.

Value: YES

<!-- image -->

### Reminder Reports

The Reports menu contains Clinical Reminder reports that Clinical Reminders Managers and/or clinicians can use for summary and detailed information about patients' due and satisfied reminders. This menu also contains reports that clinical coordinators can use to review extracted data, based on reminder definitions.

The EPI extract finding list and total options are specific to the Hepatitis C Extract project. The extracted data is based on the following reminders: VA-HEP C RISK ASSESSMENT, VA-NATIONAL EPI LAB EXTRACT, and VA-NATIONAL EPI RX EXTRACT.

The Extract QUERI totals option reports reminder and finding totals from extract summaries created by automatic QUERI extract runs.

The GEC Referral Report option is used to generate GEC Reports. Clinical Reminders V.2.0 includes a nationally standardized computer instrument called VA Geriatric Extended Care (GEC), which replaces paper forms for evaluating Veterans for extended care needs.

**Changes made by PXRM*2*42**

The data from the EPI, VA-IHD QUERI, and VA-MH QUERI extracts is no longer needed ,so these extracts were shutdown. If you use the EPT, EPF, or EQT options (see below), there will not be any data after the date when PXRM*2*42 was installed on your system.

**Changes made by PXRM*2*26**

**Finding Usage Report**

The finding multiple in file #801.41 had the pointer to file #811.2 defined as Taxonomy instead of Reminder Taxonomy. The caused the finding usage report to have selections for Reminder Taxonomy and Taxonomy. It was renamed to Reminder Taxonomy and the problem was eliminated.

The Finding Usage Report did not have the ability to search for reminder definitions and reminder terms that are used in a Reminder List Rule. That ability was added. There was a bug in the Order Check term search that was corrected. Also, the ability to search Order Check rules for definitions was added. Previously, when the report was run, the user had the option to have it delivered as a MailMan message or have it written to the screen. That was changed, so that the user has the option to browse or print it, and then has the option to have it delivered as a MailMan message.

#### Reminder Reports Menu

| **Syn.**   | **Display Name**                            | **Option Name**               | **Description**                                                                                                                                                                                                                                                |
|------------|---------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D          | Reminders Due Report                        | PXRM REMINDERS DUE            | For a selected patient and reminder(s), the report lists any reminders that are currently due.                                                                                                                                                                 |
| DRU        | Reminders Due Report (User)                 | PXRM REMINDERS DUE (USER)     | Reminders Due Reports may be run from any report template allocated to a specific user.                                                                                                                                                                        |
| DRT        | User Report Templates                       | PXRM REPORT TEMPLATE (USER)   | This option allows you to modify the PXRM REPORT TEMPLATE (USER) parameter. This parameter defines which reminder report templates are available to a restricted user.                                                                                         |
| EPT        | Extract EPI Totals                          | PXRM EXTRACT EPI TOTALS       | This option is used to summarize total counts for each type of finding item that was extracted for the target date range of the LREPI extract option run.                                                                                                      |
| EPF        | Extract EPI List by Finding and SSN         | PXRM EXTRACT EPI FINDING LIST | This option allows you to print extract results. Extracted data is listed by finding item and social security number.                                                                                                                                          |
| EQT        | Extract Queri Totals                        | PXRM EXTRACT QUERI TOTALS     | This option prints reminder and finding totals for extract summaries created by automatic extracts.                                                                                                                                                            |
| REV        | Review Date Report                          | PXRM REVIEW DATES             | The Review Date Report may be run for the following files: Computed Findings, Reminder Definition, Reminder Dialogs, and Reminder Taxonomies. A cutoff date may be entered and all review dates prior or equal to that date in the file selected are reported. |
| FUR        | Finding Usage Report                        | PXRM FINDING USAGE REPORT     | This provides a report of where selected Clinical Reminder findings are used in reminder definitions, reminder terms, and reminder dialogs.                                                                                                                    |
| GEC        | GEC Referral Report                         | PXRM GEC REFERRAL REPORT      | This is the option that is used to generate GEC Reports. GEC (Geriatrics Extended Care) are used for referral of geriatric patients to receive further care.                                                                                                   |
| HT         | HT Previous Enrollment Health Factor Search | PXRM HT HEALTH FACTOR         | This option will search the Clinical Reminders Index for any  occurrences of the HT  ENROLLMENT-START DATE (PREV ENROLL) health factor.  For any occurrence found,  the report will output the patient name, SSN, and visit date.                              |
| CSR        | Cover Sheet Reminder Report                 | PXRM COVER SHEET REMINDER RPT | This option is used to run the Cover Sheet Reminder Report.                                                                                                                                                                                                    |

##### Multiple Uses for Reminders Due Reports

Reminder reports can be used for a variety of purposes:

Patient care:

- Future Appointments
- Which patients need an intervention?

Past Visits

- Which patients missed an intervention?
- Action Lists

Inpatients

- Which patients need an intervention prior to discharge?

##### Identify patients for case management

- Diabetic patients with poor control
- Identify patients with incomplete problem lists
- Patients with (+) Hep C test but no PL entry
- Identify high risk patients; e.g., on warfarin, amiodarone, etc.
- Track annual PPD due (Employee Health)

##### Quality Improvement

- Provide feedback (team/provider)
- Identify *(and share)* best practices
- Identify under-performers *(develop action plan)*
- Track performance
- Implementation of new reminders or new processes
- Identify process issues early (mismatch of workload growth versus staffing)
- Provide data for external review (JCAHO)

##### Management Tool

- Aggregate reports
- Facility / Service
- Team (primary care team)
- Clinic / Ward
- Provider-specific reports
- Primary Care Provider
- Encounter location
- If one provider per clinic location

##### Employee Performance &amp; Evaluation

- Re-credentialing data for providers
- Annual Proficiency - Nursing
- Support for Special Advancement
- Support for Bonuses
- Employee Rewards &amp; Recognition

**How date range searching works**

- Any of the FileMan date formats are acceptable
- May 14, 2003, T-1Y, T-2M, T-3D
- Beginning date default is beginning of data
- Ending date default is today

As noted above, you can use dates like T-3M for the beginning date/time and T for the ending date/time. Since T stands for today, this tells Clinical Reminders to search between today and 3 months ago for results. When you run a reminder report, one of the prompts is for EFFECTIVE DUE DATE, and when a reminder report is run, “today” becomes whatever date is input in response to the EFFECTIVE DUE DATE prompt.

For example, if the beginning date/time was T-3M and the ending date/time was T and the effective due date was April 1, 2004, Clinical Reminders would search for results between January 1, 2004 and April 1, 2004. If you use an actual, as opposed to a symbolic, date/time, then it is never affected by what is input for EFFECTIVE DUE DATE. Each finding in the definition can have different values for beginning date/time and ending date/time, so you can search in different date ranges, as appropriate.

The key thing to remember is that “T” in a symbolic date is set to the value input for EFFECTIVE DUE DATE.

#### Reminders Due Report option

For a selected reminder, the report lists any reminders that are currently due.

Available report options are:

- Individual Patient
- Reminder Patient List
- Hospital Location (all patients with encounters)
- OE/RR Team (all patients in team)
- PCMM Provider (all practitioner patients)
- PCMM Team (all patients in team)

A SUMMARY report displays totals of how many patients of those selected have reminders due.

A DETAILED report displays patients with reminders due in alphabetical order. The report displays for each patient the date the reminder is due, the date the reminder was last done, and next appointment date. The detailed report can also list all future appointments.

A DETAILED report may be saved as a local patient list.

If a report is going to run more than once, it can be saved as a report template, eliminating the need to input the report criteria every time the report is run. The following examples show how to save the template and use it. Look for the prompts:

Create a new report template: N//

Select an existing REPORT TEMPLATE or return to continue:

**Example**

Select Reminder Managers Menu Option: rp  Reminder Reports

D      Reminders Due Report

DRU    Reminders Due Report (User)

DRT    User Report Templates

EPT    Extract EPI Totals

EPF    Extract EPI List by Finding and SSN

EQT    Extract QUERI Totals

GEC    GEC Referral Report

REV    Review Date Report

FUR    Finding Usage Report

HT     HT Previous Enrollment Health Factor Search

CSR    Cover Sheet Reminder Report

Select Reminder Reports Option: Rd  Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue:

Select one of the following:

I         Individual Patient

R         Reminder Patient List

L         Location

O         OE/RR Team

P         PCMM Provider

T         PCMM Team

PATIENT SAMPLE: L// Select Reminder Reports Option: d  Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue:

Select one of the following:

I         Individual Patient

R         Reminder Patient List

L         Location

O         OE/RR Team

P         PCMM Provider

T         PCMM Team

PATIENT SAMPLE: L// o  OE/RR Team

Select TEAM: CRPROVIDER1         teamqa

Select another TEAM:

Enter EFFECTIVE DUE DATE: Aug 25, 2009//   (AUG 25, 2009)

Select one of the following:

D         Detailed

S         Summary

TYPE OF REPORT: S// ummary

Select one of the following:

I         Individual Teams only

R         Individual Teams plus Totals by Facility

T         Totals by Facility only

REPORT TOTALS: I// r  Individual Teams plus Totals by Facility

Print locations with no patients? YES//

Print percentages with the report output? NO// y  YES

Select a REMINDER CATEGORY: CRWH REPORTS

...OK? Yes//   (Yes)

Select another REMINDER CATEGORY: CR TEST

...OK? Yes//   (Yes)

Select another REMINDER CATEGORY:

Select individual REMINDER:

VA-WH PAP SMEAR SCREENING     NATIONAL

Select another REMINDER:

Create a new report template: N// y  YES

STORE REPORT LOGIC IN TEMPLATE NAME: CR-wh

Are you adding 'jg-wh' as a new REMINDER REPORT TEMPLATE (the 109TH)? No// y

(Yes)

REMINDER REPORT TEMPLATE REPORT TITLE: CR-wh

Changes to template 'CR-wh' have been saved

Print delimited output only: N// O

Include deceased patients on the list? N// O

Include test patients on the list? N// y  YES

Save due patients to a patient list: N// O

DEVICE: HOME//   HOME

Collecting patients from OE/RR List -

Evaluating Reminders /

Evaluating reminders /

Elapsed time for reminder evaluation: 4 secs

Aug 25, 2009 9:42:34 am  Page 1

Clinical Reminders Due Report - Summary Report

Report Title:         cr1-wh

Patient Sample:       OE/RR Team

OE/RR Team:           teamqa

Reminder Category:    CRWH REPORTS

Individual Reminder:  WH SCREEN

VA-MAMMOGRAM

VA-WH PAP SMEAR SCREENING

Effective Due Date:   8/25/2009

Date run:             8/25/2009 9:38:35 am

Template Name:        CR-wh

Summary report:       Individual Teams plus Totals by Facility

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter RETURN to continue or '^' to exit:

Aug 25, 2009 9:42:37 am  Page 2

Clinical Reminders Due Report - Summary Report

Reminders due for TEAM\_1A+2B for 8/25/2009

# Patients with Reminders

Applicable     Due       %Appl   %Due   %Done

----------     ---       -----   ----   -----

1    MST Screening

37      31          87     84      16

2    Breast Cancer Screen

9       9          21    100       0

3    Breast Cancer Screen

9       9          21    100       0

4    Mammogram

9       9          21    100       0

5    ITC 2001 Mammogram Example

9       9          21    100       0

6    CR MAM

0       0           0      0       0

7    NONVA test DFN=37

43      43         100    100       0

8    Pap Smear-Screening

13      13          31    100       0

9    Pap Smear-Review of Results

6       2          14     34      66

10   Pap Smear-F/U of Abnormal Results

0       0           0      0       0

11   WH SCREEN

41      41          96    100       0

12   PAP Smear Screening

13      13          31    100       0

Report run on 43 patients.

End of the report. Press ENTER/RETURN to continue...

#### Reminders Due Report – Patient List Template

Select Reminder Reports Option: d  Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue: jgtest       HEP C

...OK? Yes//   (Yes)

Report Title:         HEP C

Report Type:          Summary Report

Patient Sample:       Location

Facility:             VAMC SIX HCS

Location:             All Outpatient Locations (Prior Encounters)

Print Locations without Patients:YES

Print percentages with the output:NO

Reminder:             1  LABTEST

2  VA-NATIONAL EPI LAB EXTRACT

3  VA-NATIONAL EPI RX EXTRACT

Template Name:        jgtest

Date last run:        AUG 04, 2001@18:39:04

Service categories:   A,I

A - AMBULATORY

I - IN HOSPITAL

Enter ENCOUNTER BEGINNING DATE:  t-2Y

This must be a past date. For detailed help type ??.

Enter ENCOUNTER BEGINNING DATE:  T-3Y  (AUG 25, 2006)

Enter ENCOUNTER ENDING DATE: T  (AUG 25, 2009)

Enter EFFECTIVE DUE DATE: Aug 25, 2009//   (AUG 25, 2009)

Select one of the following:

I         Individual Locations only

R         Individual Locations plus Totals by Facility

T         Totals by Facility only

REPORT TOTALS: I// R  Individual Locations plus Totals by Facility

Print delimited output only: N// O

Include deceased patients on the list? N// O

Include test patients on the list? N// YES

Save due patients to a patient list: N// O

DEVICE: HOME//   HOME

Building hospital locations list -

Elapsed time for building hospital locations list: 0 secs

Building patient list /

Elapsed time for building patient list: 0 secs

Removing invalid encounter(s) /

Elapsed time for removing invalid encounter(s): 0 secs

Evaluating Reminders |

Evaluating reminders /

Elapsed time for reminder evaluation: 0 secs

Aug 25, 2009 12:36:04 pm  Page 1

Clinical Reminders Due Report - Summary Report

Report Title:         HEP C

Patient Sample:       Location

Location:             All Outpatient Locations (Prior Encounters)

Date Range:           8/25/2006 to 8/25/2009

Effective Due Date:   8/25/2009

Date run:             8/25/2009 12:34:40 pm

Template Name:        jgtest

Summary report:       Individual Locations plus Totals by Facility

Service categories:   A,I

A - AMBULATORY

I - IN HOSPITAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter RETURN to continue or '^' to exit:

Aug 25, 2009 12:36:08 pm  Page 2

Clinical Reminders Due Report - Summary Report

Facility: SALT LAKE CITY HCS  660

Reminders due 8/25/2009 - CARDIOLOGY for 8/25/2006 to 8/25/2009

# Patients with Reminders

Applicable         Due

----------         ---

1    LABTEST                                               3           3

2    National Hepatitis Lab Extract                        3           3

3    National Hepatitis Med Extract                        3           3

Report run on 3 patients.

Enter RETURN to continue or '^' to exit:

Aug 25, 2009 12:36:16 pm  Page 3

Clinical Reminders Due Report - Summary Report

Facility: SALT LAKE CITY HCS  660

Reminders due 8/25/2009 - TOTAL REPORT for 8/25/2006 to 8/25/2009

# Patients with Reminders

Applicable         Due

----------         ---

1    LABTEST                                               3           3

2    National Hepatitis Lab Extract                        3           3

3    National Hepatitis Med Extract                        3           3

Report run on 3 patients.

Report timing data:

Elapsed time for building hospital locations list: 0 secs

Elapsed time for building patient list: 0 secs

Elapsed time for reminder evaluation: 0 secs

Elapsed time for removing invalid encounter(s): 0 secs

End of the report. Press ENTER/RETURN to continue...

...

#### Reminders Due Report – Patient List

Select Reminder Managers Menu Option: RP  Reminder Reports

RD     Reminders Due Report

RDU    Reminders Due Report (User)

RDT    User Report Templates

EPT    Extract EPI Totals

EPF    Extract EPI List by Finding and SSN

EQT    Extract QUERI Totals

GEC    GEC Referral Report

REV    Review Date Report

FUR    Finding Usage Report

Select Reminder Reports Option:  Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue:

Select one of the following:

I         Individual Patient

R         Reminder Patient List

L         Location

O         OE/RR Team

P         PCMM Provider

T         PCMM Team

PATIENT SAMPLE: L// r  Reminder Patient List

Select REMINDER PATIENT LIST:

CRPROVIDER,ONE

Select another PATIENT LIST:

Enter EFFECTIVE DUE DATE: Aug 25, 2009//   (AUG 25, 2009)

Select one of the following:

D         Detailed

S         Summary

TYPE OF REPORT: S// ummary

Print locations with no patients? YES//

Print percentages with the report output? NO//

Select a REMINDER CATEGORY:    AGP TEST

...OK? Yes//   (Yes)

Select another REMINDER CATEGORY: ??

: slc REMINDER CATEGORY

...OK? Yes//   (Yes)

Select another REMINDER CATEGORY: iRAQ\_AFGHAN

...OK? Yes//   (Yes)

Select another REMINDER CATEGORY:

Select individual REMINDER:    VA-WH PAP SMEAR SCREENING     NATIONAL

Select another REMINDER: va-depRESSION SCREENING       NATIONAL

Select another REMINDER: VA-WH MAMMOGRAM SCREENING     NATIONAL

Select another REMINDER:

Create a new report template: N// O

Print delimited output only: N// O

Include deceased patients on the list? N// O

Include test patients on the list? N// y  YES

Save due patients to a patient list: N// O

DEVICE: HOME//   HOME

Collecting patients from Reminder Patient List /

Evaluating reminders /

Elapsed time for reminder evaluation: 6 secs

Aug 25, 2009 12:43:46 pm  Page 1

Clinical Reminders Due Report - Summary Report

Patient Sample:       Patient List

Patient List:         CRPROVIDER,ONE

Reminder Category:    AGP TEST

Individual Reminder:  VA-WH PAP SMEAR SCREENING

VA-DEPRESSION SCREENING

VA-WH MAMMOGRAM SCREENING

Effective Due Date:   8/25/2009

Date run:             8/25/2009 12:41:18 pm

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter RETURN to continue or '^' to exit:

Aug 25, 2009 12:43:57 pm  Page 3

Clinical Reminders Due Report - Summary Report

Patient List: CRPROVIDER,ONE for 8/25/2009

# Patients with Reminders

Applicable         Due

----------         ---

1    AGP ERROR                                             0           0

2    NONVA test DFN=37                                    14          14

3    Pap Smear-Screening                                   3           3

4    Pap Smear-Review of Results                           2           0

5    Pap Smear-F/U of Abnormal Results                     0           0

6    PAIN SCREENING                                        0           0

7    ITC Pneumovax                                        13          13

8    SLC Life style Education                              6           6

9    new reminder                                          0           0

10   Hepatitis C Risk Assessment                          14          12

11   Influenza Vaccine                                    12          12

12   Smoking Cessation Education                           4           4

13   Pheumovax                                            13          10

14   ITC 2001 diabetes example                             1           1

15   ITC 2001 Mammogram Example                            3           3

16   SLC Diabetic Foot Care Education                     14          14

17   Diabetic Eye Exam                                    14          14

18   SLC Cancer Screen                                     5           5

19   Ischemic HD/Post MI Follow Up                         0           0

20   Breast Exam                                           4           4

21   Advanced Directives Education                        14          13

22   LTC Oversight Visit                                  14          14

23   Weight and Nutrition Screen                          13          13

24   IHD Lipid Profile                                     2           2

25   EXCHANGE CHANGES                                      0           0

26   Tobacco Cessation Education                          11          11

27   JG TOBACCO USE SCREEN                                14          14

28   Problem Drinking Screen                              14          14

29   Weight and Nutrition Screen                          13          13

30   Alcohol Abuse Education                              14          14

31   Weight                                               14          14

32   Exercise Education                                   14          14

33   JG-Weight                                            14          14

34   Taxonomy Test                                        14          14

35   Patch5 VA-Pain Screening                             14          14

36   PAP Smear Review Results                              2           2

37   Iraq&amp;Afghan Post-Deployment Screen                    1           1

38   PAP Smear Screening                                   3           3

39   Depression Screening                                 14          14

40   Mammogram Screening                                   2           2

Report run on 14 patients.

Report timing data:

Elapsed time for reminder evaluation: 6 secs

End of the report. Press ENTER/RETURN to continue...

##### Future Appointments

If you run a report based on future appointments and select a detailed report, you can choose to display all future appointments and the appointment location.

Select one of the following:

P         Previous Encounters

F         Future Appointments

PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Future Appointments

Enter APPOINTMENT BEGINNING DATE AND TIME: Jun 23, 2022// T+1  (JUN 24, 2022)

Enter APPOINTMENT ENDING DATE AND TIME: T+30  (JUL 23, 2022)

Enter EFFECTIVE DUE DATE: Jun 23, 2022//   (JUN 23, 2022)

Select one of the following:

D         Detailed

S         Summary

TYPE OF REPORT: S// Detailed

Combined report for all Locations : Y// ES

Display All Future Appointments: N// YES

Display Appointment Location: N// YES

If you answer Y to the Display Appointment Location prompt, the clinic name will appear with the future appointment date/time. If you enter N, only the date/time will display.

If the patient is an outpatient, it will sort by next appointment date. If the patient is a currently an inpatient and has an outpatient appointment schedule, it will sort by the Room-Bed location.

When displaying the next appointment, if the patient is an inpatient, the Room-Bed will be displayed followed by (Inp.). Then the next appointment will display under this data. If you select Display All future appointments, the appointment will display under the patient name.

#### Extract EPI Totals

The data from the EPI extract is no longer needed so it was shutdown by patch PXRM*2*42. If you run this report there will not be any data after the date when PXRM*2*42 was installed on your system.

Extract EPI Total reports are generated each month by a Lab package, LREPI run that processes the following national reminders related to Hepatitis C:

VA-NATIONAL EPI DB UPDATE

VA-NATIONAL EPI LAB EXTRACT

VA-NATIONAL EPI RX EXTRACT.

Select Reminder Reports Option:  Extract EPI Totals

START WITH NAME: FIRST// ??

The NAME is the combination of a unique abbreviation for the type of

extract. The file contains different extract types:

1) EPI - Hep C Extract

Extracts of this type are prefixed LREPI. The following is an example

of EPI lookup information:

160          LREPI 00/05 061500     Jun 15,2000@14:52:36

161          LREPI 00/06 073100     Jul 15,2000@14:55:40

162          LREPI 00/07 081500     Aug 15,2000@15:42:24

The YY/MM represents the ending year and month of the extract date

range, and the run date in the format YYMMDD. The date and time of the

run is an identifier.

2) QUERI (IHD and MH)

Extracts of this type are prefixed VA-IHD or VA-MH. The following is an

example of IHD lookup information:

1   VA-IHD QUERI 2000 M2     Nov 27,2002@13:20:26

2   VA-IHD QUERI 2000 M3     Nov 27,2002@13:24:08

3   VA-IHD QUERI 2000 M4     Nov 27,2002@13:25:13

The year and month of the extract are included in the extract name. The

date and time of the run is an identifier.

START WITH NAME: FIRST// LREPI 05/02

GO TO NAME: LAST//

DEVICE: ;;999  TCP    Right Margin: 80//

REMINDER EXTRACT TOTALS                        JAN  6,2006  16:30    PAGE 1

--------------------------------------------------------------------------------

LREPI 05/02 031505               Date Range: FEB  1,2005-FEB 28,2005

Extract Date: MAR 15,2005  22:16

Total Patients Evaluated:        766

Total Patients with Findings:    718

Totals by Finding Item               Finding  Unique Patient

Count       Count

INTERFERON ALFA-2B                    1           1

HEPATITIS C ANTIBODY                207         207

TOT. BILIRUBIN                      190         190

RIBAVIRIN                            35          35

AST                                 192         192

ALT                                 198         198

VA-HEPATITIS C INFECTION            127         127

INTERFERON BETA-1B                    4           4

INTERFERON BETA-1A                   18          18

INTERFERON ALFACON-1                  5           5

RISK FACTOR FOR HEPATITIS C         110         110

NO RISK FACTORS FOR HEP C           319         319

DECLINED HEP C RISK ASSESSMENT        8           8

LREPI 05/03 041505               Date Range: MAR  1,2005-MAR 31,2005

Extract Date: APR 15,2005  22:12

Total Patients Evaluated:        841

Total Patients with Findings:    802

Totals by Finding Item               Finding  Unique Patient

Count       Count

INTERFERON ALFA-2B                    2           2

HBSAG                                 1           1

HEPATITIS C ANTIBODY                446         223

RIBAVIRIN                            47          47

VA-HEPATITIS C INFECTION            119         119

INTERFERON BETA-1B                    9           9

INTERFERON BETA-1A                   16          16

INTERFERON ALFACON-1                  8           8

HBSAB                                33          33

RISK FACTOR FOR HEPATITIS C         132         132

NO RISK FACTORS FOR HEP C           372         372

DECLINED HEP C RISK ASSESSMENT        3           3

Press RETURN to continue...

#### Extract QUERI Totals

The data from the VA-IHD QUERI and VA-MH QUERI extracts is no longer needed, so these extracts were shutdown by patch PXRM*2*42. If you use this report, there will not be any data after the date when PXRM*2*42 was installed on your system.

D      Reminders Due Report

DRU    Reminders Due Report (User)

DRT    User Report Templates

EPT    Extract EPI Totals

EPF    Extract EPI List by Finding and SSN

EQT    Extract QUERI Totals

GEC    GEC Referral Report

REV    Review Date Report

FUR    Finding Usage Report

Select Reminder Reports Option: E **QT** Extract QUERI Totals

START WITH NAME: FIRST// **??**

The NAME is the combination of a unique abbreviation for the type of

extract (e.g., LREPI), the YY/MM representing the ending year and

month of the extract date range, and the run date in the format

YYMMDD. The date and time of the run is an identifier.  The following

is an example of lookup information.

160          LREPI 00/05 061500     Jun 15,2000@14:52:36

161          LREPI 00/06 073100     Jul 15,2000@14:55:40

162          LREPI 00/07 081500     Aug 15,2000@15:42:24

163          LREPI 00/05 082200     Aug 22,2000@02:44:54

164          LREPI 00/08 082500     Aug 25,2000@14:24:59

START WITH NAME: FIRST// **&lt;Enter&gt;**

START WITH NAME: FIRST// **164**

GO TO NAME: LAST// **&lt;Enter&gt;**

DEVICE:   ANYWHERE    Right Margin: 80// **&lt;Enter&gt;**

REMINDER EXTRACT SUMMARY LIST                 JAN 10,2003  09:14    PAGE 1

--------------------------------------------------------------------------

VA MH QUERI 2000 M2              Date Range: FEB  1,2000-FEB 28,2000

Extract Date: JAN  3,2003

Extract Sequence: 001

Reminder:         VA-DEPRESSION SCREENING

Station:          CRSITE ONE

Patient List:     VA-MH QUERI 2000 M2 QUALIFYING VISIT

Reminder Totals:     Total      Applicable       N/A       Due   Not Due

1000            899       101       200       699

Finding Totals:

Sequence:      001

Finding Group: VA-DEPRESSION SCREEN NON APPLICABLE

Term:          DEPRESSION DIAGNOSIS

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

20             20         0        20         0

Sequence:      002

Finding Group: VA-DEPRESSION SCREEN NON APPLICABLE

Term:          PSYCHOTHERAPY

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      003

Finding Group: VA-DEPRESSION SCREEN NON APPLICABLE

Term:          ANTIDEPRESSANT MEDICATION

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      004

Finding Group: VA-DEPRESSION SCREEN RESULT

Term:          DEPRESSION SCREEN NEGATIVE

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  APPLICABLE PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      005

Finding Group: VA-DEPRESSION SCREEN RESULT

Term:          DEPRESSION SCREEN POSITIVE

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  APPLICABLE PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      006

Finding Group: VA-REFUSED DEPRESSION SCREEN

Term:          REFUSED DEPRESSION SCREENING

Group Type:    MOST RECENT FINDING COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Extract Sequence: 002

Reminder:         VA-POS DEPRESSION SCREEN FOLLOW UP

Station:          CRSITE HCS

Patient List:     VA-MH QUERI 2000 M2 QUALIFYING VISIT

Reminder Totals:     Total      Applicable       N/A       Due   Not Due

1000            300       700        10       690

Finding Totals:

Sequence:      001

Finding Group: VA-POS DEPRESSION SCREEN FOLLOW UP

Term:          DEPRESSION SCREEN NEGATIVE

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      002

Finding Group: VA-POS DEPRESSION SCREEN FOLLOW UP

Term:          DEPRESSION ASSESS INCONCLUSIVE (?MDD)

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      003

Finding Group: VA-POS DEPRESSION SCREEN FOLLOW UP

Term:          REFERRAL TO MENTAL HEALTH

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      004

Finding Group: VA-POS DEPRESSION SCREEN FOLLOW UP

Term:          DEPRESSION TO BE MANAGED IN PC

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Extract Sequence: 003

Reminder:         VA-ANTIPSYCHOTIC MED SIDE EFF EVAL

Station:          CRSITE HCS

Patient List:     VA-MH QUERI 2000 M2 QUALIFYING VISIT

Reminder Totals:     Total      Applicable       N/A       Due   Not Due

1000              3       997         1         2

Finding Totals:

Sequence:      001

Finding Group: VA-ANTIPSYCHOTIC DRUGS

Term:          AIM EVALUATION NEGATIVE

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      002

Finding Group: VA-ANTIPSYCHOTIC DRUGS

Term:          AIM EVALUATION POSITIVE

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

Total      Applicable       N/A       Due     Not Due

Sequence:      003

Finding Group: VA-ANTIPSYCHOTIC DRUGS

Term:          REFUSED ANTIPSYCHOTICS

Group Type:    MOST RECENT FINDING PATIENT COUNT

Group Status:  TOTAL PATIENTS

Finding Count by Reminder Status:

#### GEC Referral Report

GEC Referral Reports display the percentage of patients referred to select GEC programs who meet the eligibility criteria as outlined in the Under Secretary for Health’s Information Letter IL 10-2003-005 and VHA Handbook 1140.2.

VA GEC Reports provide quarterly statistical reports on the following VA-funded programs.

- Homemaker/Home Health Aide, when Funding Source=VA
- Adult Day Health Care, when Funding Source=VA
- VA In-Home Respite, when Funding Source=VA
- Care Coordination, when Funding Source=VA

When sites submit their quarterly reports, the national office will be able to generate a report for the General Accounting Office/Office of Inspector General that demonstrates compliance with the standards for assessing patients prior to placement in VA-funded programs.

These same reports can be used at the local level to evaluate how well a site is performing in meeting compliance standards for placement of patients in VA funded GEC programs.

**Changes in Patch 4**

- An undefined error, &lt;UNDEFINED&gt;CALCMON+12&lt;&gt;PXRMG2M1, occurred when the scheduled event fired off at the beginning of each month. That has now been repaired.

- Several of the GEC Reports were not showing a complete list of patients or providers. This has now been corrected. The division and age of the patient has been added to some reports to help in identifying the patient.

- There is a new choice in the GEC reports menu that will give the sites the option to open a closed referral, merge two referrals, or close an open referral.

- The GEC Care Recommendation Dialog has been modified to allow more than one selection when a person wants to refer a patient to more than one location.

- A problem with the user being able to take some editing actions on GEC dialogs have been corrected, so the user is not able to copy or delete dialog groups from the GEC dialogs.
- Geriatric Extended Care Reports were not collecting the correct data. This was corrected.
- The email addresses of the remote members of mail group GEC NATIONAL ROLLUP are updated.
- As requested by the primary GEC stakeholder, several reminder dialog entries were moved from the Nursing Assessment GEC dialog to the Care Recommendation GEC dialog. A post-install routine changes several Health Factors from one GEC dialog to another.

**Example**

Select Reminder Reports Option: **GEC** GEC Referral Report

All Reports will print on 80 Columns

Select one of the following:

1         Category

2         Patient

3         Provider by Patient

4         Referral Date

5         Location

6         Referral Count Totals

7         Category-Referred Service

8         Summary (Score)

9         'Home Help' Eligibility

10        Restore or Merge Referrals

Select Option or ^ to Exit: 8// **&lt;Enter&gt;** Summary (Score)

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:  (1/1/1988 - 6/30/2004): T-60// **&lt;Enter&gt;** (MAY 01, 2004)

Select Ending Date.

ENDING date or ^ to exit:  (5/1/2004 - 6/30/2004): T// **&lt;Enter&gt;** (JUN 30, 2004)

Select one of the following:

A         All Patients

M         Multiple Patients

Select Patients or ^ to exit: A// **&lt;Enter&gt;** ll Patients

Select one of the following:

F         Formatted

D         Delimited

Select Report Format or ^ to exit: F// **&lt;Enter&gt;** ormatted

DEVICE: HOME// **&lt;Enter&gt;** ANYWHERE    Right Margin: 80// **&lt;Enter&gt;**

==============================================================================

GEC Patient-Summary (Score)

Data on Complete Referrals Only

From: 05/01/2004 To: 06/30/2004

Finished        Basic Skilled Patient   TOTAL

Name                  SSN        Date       IADL ADL   Care    Behaviors ACROSS

==============================================================================

CRPATIENT,ONE        (666809999) 06/15/2004   0    0     2       4         6

CRPATIENT,ONE        (666809999) 06/15/2004   0    7     9       5        21

CRPATIENT,TWO        (666809990) 05/04/2004   0    0     0       0         0

CRPATIENT,SIX        (666009999) 05/11/2004   0    0     0       0         0

CRPATIENT,SIX        (666009999) 05/11/2004   0    0     0       0         0

CRPATIENT,SIX        (666009999) 05/11/2004   0    0     0       0         0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Totals &gt; &gt;   0    7    11       9        27

Means &gt; &gt; 0.0  1.2   1.8     1.5       4.5

Standard Deviations &gt; &gt; 0.0  3.1   4.1     2.9       9.8

Enter RETURN to continue or '^' to exit: **&lt;Enter&gt;**

Review Date Report

All of the Clinical Reminders files contain a REVIEW DATE field. This report lets you input a date and search for entries whose review date is prior to this date. When you run the report, you select one of the Clinical Reminder’s files and enter the Review Cutoff Date.

Select Reminder Reports &lt;TEST ACCOUNT&gt; Option: REV  Review Date Report

Select one of the following:

C         Computed Finding

D         Reminder Dialog

L         Reminder Location List

O         Reminder Orderable Item Groups

U         Reminder Order Check Rules

R         Reminder Definition

S         Reminder Sponsor

T         Reminder Term

X         Reminder Taxonomy

Select File to Review: Reminder Definition

Enter Review Cutoff Date: Jun 24, 2022//   (JUN 24, 2022)

DEVICE: ;;999  TELNET PORT    Right Margin: 80//

REMINDERS TO REVIEW (up to Jun 24, 2022)             JUN 24, 2022@11:15   PAGE 1

NAME

REVIEW DATE

--------------------------------------------------------------------------------

PH DIABETIC RETINAL EXAM                                   JAN 24,2006

ZZVA-MHV INFLUENZA VACCINE                                 AUG 31,2009

SETH REMINDER 1                                            JAN 2,2011

RFR FINDING ITEM XX IV                                     JUL 30,2012

ML ASPLENIC PATIENT                                        APR 17,2013

ML TAX #1 REMINDER DEF                                     APR 22,2013

ML ICD DX ONLY                                             MAY 23,2013

ML TAXONOMY#1 AS FINDING ITEM NONE                         JUN 3,2013

ML TAX1 ALL SINGLE CURRENT REMDEF                          AUG 1,2013

ML TAX1 PX HIST REMDEF                                     AUG 15,2013

ML TAX2 ICD ALL REMDEF                                     AUG 15,2013

ML TAX3 PX  NONE REMDEF                                    AUG 15,2013

ML TAX4 ICD10 ALL REM DEF                                  AUG 15,2013

MSL ALTERNATE TEXT TEST                                    DEC 11,2013

ML INACTIVE TAX RD TEST                                    JAN 28,2014

ML DOSAGE/ALTERNATE TEXT TEST                              JAN 31,2014

Finding Usage Report

This report provides a listing of the reminder definitions, reminder terms, and reminder dialogs in which selected Clinical Reminder findings are used. This can help you troubleshoot when new reminders and dialogs are distributed to replace existing ones.

The report can be sent as a mail message to designated recipients.

**Changes made by PXRM*2*26:**

- The finding multiple in file #801.41 had the pointer to file #811.2 defined as Taxonomy instead of Reminder Taxonomy. The caused the finding usage report to have selections for Reminder Taxonomy and Taxonomy. It was renamed to Reminder Taxonomy and the problem was eliminated.
- The Finding Usage Report did not have the ability to search for reminder definitions and reminder terms that are used in a Reminder List Rule. That ability was added.
- There was a bug in the Order Check term search that was corrected.
- The ability to search Order Check rules for definitions was added.
- Previously, when the report was run, the user had the option to have it delivered as a MailMan message or have it written to the screen. That was changed, so that the user has the option to browse or print it, and then has the option to have it delivered as a MailMan message.

Select Reminder Reports Option:  Finding Usage Report

Clinical Reminders Finding Usage Report

Select from the following reminder findings (* signifies standardized):

1 - DRUG

2 - EDUCATION TOPICS

3 - EXAM

4 - HEALTH FACTOR

5 - ICD9 DIAGNOSIS

6 - IMMUNIZATION *

7 - LABORATORY TEST

8 - MENTAL HEALTH

9 - MH TESTS AND SURVEYS

10 - ORDER DIALOG

11 - ORDERABLE ITEM

12 - PROCEDURE

13 - RADIOLOGY PROCEDURE

14 - REMINDER COMPUTED FINDING

15 - REMINDER DEFINITION

16 - REMINDER LOCATION LIST

17 - REMINDER TAXONOMY

18 - REMINDER TERM

19 - SKIN TEST *

20 - TAXONOMY

21 - VA DRUG CLASS *

22 - VA GENERIC *

23 - VITAL MEASUREMENT *

24 - VITAL TYPE *

25 - WH NOTIFICATION PURPOSE

Enter your list for the report.:  (1-21): **5**

Search for all or selected ICD9 DIAGNOSIS

Select one of the following:

1         ALL

2         SELECTED

Enter response: ALL// 1

SORT DONE

Browse or Print? B// **Print**

DEVICE: HOME//   HOME

Clinical Reminders finding usage report.

The following ICD DIAGNOSIS(s) are used as follows:

=======================================================

ICD DIAGNOSIS - 100.9 (IEN=3)

Is used in the following Reminder Dialog(s):

Dialog element POV DIAG 1 (IEN=660113), used in the

Finding Item field

=======================================================

ICD DIAGNOSIS - 103.3 (IEN=15)

---------------------------------

Is used in the following Reminder Dialog(s):

Dialog element CODE SET ICD9 FIND (IEN=336), used in the

Finding Item field

=======================================================

ICD DIAGNOSIS - 174.1 (IEN=335)

---------------------------------

Is used in the following Reminder Dialog(s):

Dialog element POV 174.1 DONE (IEN=441), used in the

Finding Item field

Dialog element POV 174.1 DONE ELSEWHERE (IEN=581), used in the

Finding Item field

.

.

.

Etc.

Press ENTER to continue:

Deliver the report as a MailMan message? Y// y

**MailMan Report**

Subj: Clinical Reminders Finding Usage Report  [#49717] 05/08/09@16:02  70 lines

From: POSTMASTER (Sender: CRUSER,THIRTEEN)  In 'IN' basket.   Page 1  *New*

-----------------------------------------------------------------------------

Clinical Reminder finding usage report.

The following IMMUNIZATIONs are used as Clinical Reminder findings:

=======================================================

IMMUNIZATION - INFLUENZA (IEN=12)

INFLUENZA is used in the following Definitions:

----------------------------

VA-*INFLUENZA IMMUNIZATION (IEN=8)

Finding number 1

----------------------------

VA-INFLUENZA VACCINE (IEN=26)

Finding number 1

----------------------------

IMMTEST1 (IEN=71)

Finding number 14

----------------------------

MHV INFLUENZA VACCINE (IEN=208)

Finding number 1

----------------------------

jg FLU VACCINE (IEN=209)

Finding number 1

----------------------------

MHV INFLUENZA VACCINE2 (IEN=246)

Finding number 1

----------------------------

INFLUENZA GOOD (IEN=264)

Finding number 1

----------------------------

INFLUENZA BAD (IEN=265)

Finding number 1

----------------------------

ERROR (IEN=275)

Finding number 14

----------------------------

AGP IMMUNIZATION (IEN=361)

Finding number 1

----------------------------

IMMTEST (IEN=660008)

Finding number 14

INFLUENZA is used in the following Terms:

----------------------------

INFLUENZA IMMUNIZATION (IEN=491)

Finding number 3

----------------------------

PKR LONG IMM TEST (IEN=766)

Finding number 3

INFLUENZA is used in the following Dialogs:

----------------------------

Dialog element ZZPJH TIME DONE (IEN=496), used in the

Finding Item field

----------------------------

Dialog element AGP INSTALL ELEMENT (IEN=1060), used in the

Finding Item field

----------------------------

Dialog element IM INFLUENZA DONE ELSEWHERE (IEN=660065), used in

the

Finding Item field

----------------------------

Dialog element IM INFLUENZA CONTRA (IEN=660066), used in the

Finding Item field

----------------------------

Dialog element CONTRAINDICATION TEST (IEN=660000137), used in the

Finding Item field

----------------------------

Dialog element TEST PLAN IMMUNIZATION (IEN=660000139), used in the

Finding Item field

----------------------------

Dialog element DEMO ELEMENT 1 (IEN=660000173), used in the

Finding Item field

Enter message action (in IN basket): Ignore//

**HT Previous Enrollment Health Factor Search**

This option will search the Clinical Reminders Index for any occurrences of the HT ENROLLMENT-START DATE (PREV ENROLL) health factor.  For any occurrence found, the report will output the patient name, SSN, and visit date.

**Cover Sheet Reminder Report**

This option runs the Cover Sheet Reminder Report. It provides the ability to determine what reminders are in a cover sheet list.

### MST Synchronization Management Project

The Millennium Healthcare and Benefit Act, Public Law 106-117, Section 115, Counseling and Treatment for Veterans Who Have Experienced Sexual Trauma, includes provisions to develop a formal mechanism for reporting on outreach activities, and to require the VA to provide counseling and appropriate care and services for treatment of Military Sexual Trauma (MST). As a result, the Women Veterans Health Program (WVHP) has requested VistA enhancements to support the screening of all Veterans (men and women) for MST, the identification of non-VA workload associated with MST, and enhanced national reporting of MST data. Veterans Health Administration (VHA) Directive 2000-008 and VHA Directive 99-039 has provided guidance in the screening, tracking, and documentation of MST for all enrolled Veterans who utilize VHA. Additionally, a “Best Practice” manual has provided field guidance on creating local Implementation Support Teams (IST), developing MST screening processes, and documenting screening results using the VistA Military Sexual Trauma database within the Patient Registration Package.

In FY1999, VistA enhancements provided the ability to record or edit Veterans’ MST status in VistA and also created an MST “outpatient classification code” similar to Agent Orange. Once a Veteran has reported MST, the classification code triggers the staff via VistA prompts when they are checking out an encounter to be prompted for whether it is related to MST. VistA began including the MST status and classification code in Patient Care Encounter (PCE) transmissions in May 2000. The Patient Treatment File (PTF) patch was released to sites on March 6, 2001.

#### MST Scope of Changes

The effort for implementing the MST section of the Millennium Healthcare and Benefits Act (Mill Bill) impacted Fee Basis, Women Health (WH), Health Eligibility Center (HEC/Enrollment), Clinician Desktop, Patient Information Management Systems (PIMS), the Corporate Databases, and VistA software packages.

The enhancements provided a means for identifying non-VA MST workload in the Fee Basis application, clinical reminders to clinicians, and specifications for the VA and non-VA workload reports to be generated at the Austin Automation Center (AAC). Also, PIMS and HEC will manage the MST status sharing between sites to minimize the instances in which a veteran is repeatedly asked about MST status. HEC will act as the authoritative database source.

The data for MST will be entered locally in the VistA system and will be shared with the HEC as part of the current HL7 messaging capabilities. The information entered in the VistA system is sent to the HEC so that it can be transmitted to other VA health care facilities of record. Locally, MST-related, non-VA care will be entered into the Fee Basis system. This information will be sent to Central Fee, where Outpatient non-VA data will be used for national reporting. Inpatient non-VA care is sent to PTF. The system requirements, identified in this document, include additions and modifications to existing field entries on the VistA, HEC, Fee Basis, and Central Fee. There will be no changes to the NPCD or PTF database. NPCD will continue to accept and store MST data.

#### MST System Features

There are multiple objectives with Mill Bill MST. To determine the amount of care being provided to Veterans who have experienced MST, the Fee Basis system will locally keep track of MST related non-VA care. This information will be sent to Central Fee so that reports reflecting the national experience can be generated. In order to improve data quality, redundant fields in the WVH application and PIMS will be synchronized. Legislation mandates that all Veterans be screened for MST. To reduce the number of times a Veteran would be screened for MST, VAMCs, via PIMS, will provide the HEC with MST status as it is derived. The HEC will be the authoritative database source for MST status and be able to provide other VAMCs with a Veteran’s MST status upon request. **Clinical reminders provides a mechanism to screen Veterans who do not have an MST status and assists with the entry of MST information** . VHA wants to have reports from the National Databases (NPCD and Central Fee) that will look at the population and trending of MST across VHA.

##### CLINICAL REMINDERS MST FUNCTIONALITY (Patch PXRM*1.5*7)

This patch, released in January 2002, provided new functionality for Clinical Reminders to help sites meet the mandate to collect Military Sexual Trauma (MST) data.

The patch included:

A new reminder definition, VA-MST SCREENING, and the findings used by the definition. The findings include:

Three reminder terms: VA-MST DECLINES REPORT, VA-MST NEGATIVE REPORT, and VA-MST POSITIVE REPORT

A computed finding: VA-MST STATUS

Four health factors: MST CATEGORY, MST DECLINES TO ANSWER, MST NO DOES NOT REPORT, and MST YES REPORTS

A reminder dialog: VA-MST SCREENING.

The reminder dialog has three elements that update PCE with health factor findings (MST NO DOES NOT REPORT, MST YES REPORTS and MST DECLINES TO ANSWER). You will be able to capture data directly to the MST HISTORY file, #29.11, using this reminder dialog.

If your site is already capturing MST data via health factors, education topics, or exams, there is functionality in this patch that will help you synchronize this data with the data in the MST HISTORY file, #29.11. Before the synchronization can be done, you must map your local findings to the appropriate VA-MST reminder term. If you have been using health factors that are similar to those listed above, you may consider renaming your health factors to match the names listed above. The renaming must be done BEFORE the patch is installed. If you choose not to do this, or your site has been using education topics or exams, you will need to map your findings to these terms before the initial synchronization can be done.

If your site is already capturing MST data via local health factors, education topics, and exams, the national dialog and component elements and groups may be copied to local dialogs, which may then be modified to use local findings. ***The national dialog and component elements and groups may not be edited.*** Alternatively, if you already have reminder dialogs for MST, you may continue to use these if the findings in these dialogs are mapped to the new VA-MST terms.

###### Reminders MST Synchronization Management Menu

This patch also included a new option on the Reminder Managers Menu called Reminders MST Synchronization Management. There are two options on this menu: one for doing the synchronization (Reminders MST Synchronization), and another for checking on the synchronization (Reminders MST Synchronization Report). The first option will allow you to schedule a background job that does the synchronization. The report option will give you data on the initial synchronization and the last daily synchronization.

| **Syn.**   | **Name**                             | **Option Name**          | **Description**                                                                                                                                                           |
|------------|--------------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYN        | Reminders MST Synchronization        | PXRM MST SYNCHRONIZATION | This option is used to run the Clinical Reminders MST synchronization.  The synchronization should not be run until the site has finished mapping the MST reminder terms. |
| REP        | Reminders MST Synchronization Report | PXRM MST REPORT          | This option runs the Clinical Reminders MST synchronization report.                                                                                                       |

###### Reminders MST Synchronization Example

Select Reminder Managers Menu Option: MST  Reminders MST Synchronization Management

SYN    Reminders MST Synchronization

REP    Reminders MST Synchronization Report

Select Reminders MST Synchronization Management Option: SYN  Reminders MST Synchronization

Queue the Clinical Reminders MST synchronization.

Enter the date and time you want the job to start.

It must be after 09/11/2001@09:01:33 **T@1**

Do you want to run the MST synchronization at the same time every day? Y// **NO**

Task number 594549 queued.

###### Reminders MST Synchronization Report

The report option gives you data on the initial synchronization and the last daily synchronization.

Example

Select Reminders MST Synchronization Management Option: rep

Reminders MST Synchronization Report

Clinical Reminders MST Synchronization Report

---------------------------------------------

Initial synchronization date: Aug 28, 2001@15:12:15

Number of updates made: 4

Elapsed time: 4:00:34

Last daily synchronization date: Sep 05, 2001@08:45:48

Number of updates made: 0

Elapsed time:  3:57:34

### Reminder Parameters Menu

This menu contains three options: Edit Site Disclaimer, Edit Web Sites, and Edit Number of MH Questions.

Edit Web Sites was created in response to the NOIS, MAC-1000-60473 - Web site shows in all reminders. Sites were unable to get websites to show for an individual reminder – a default URL and website text overrides individual entries. In Version 1.5, the only way to edit or delete the default website was through VA FileMan. It was recommended that developers create an easier way for a user edit the default URL Web addresses.

| Syn.   | Name                        | Option Name               | Description                                                                                                            |
|--------|-----------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------|
| ESD    | Edit Site Disclaimer        | PXRM EDIT SITE DISCLAIMER | This option allows the site disclaimer used in Health Summary components to be modified.                               |
| EWS    | Edit Web Sites              | PXRM EDIT WEB SITES       | This option allows the reminder web sites used in CPRS GUI to be modified.                                             |
| MH     | Edit Number of MH Questions | PXRM MH QUESTIONS         | This option allows the site to select the maximum number of MH questions to  be used as Reminder Dialog Finding Items. |

#### Edit Site Disclaimer Example

Select Reminder Parameters Option: esd  Edit Site Disclaimer

SITE REMINDER DISCLAIMER:

No existing text

Edit? NO// y  YES

==[ WRAP ]==[ REPLACE ]=====&lt; SITE REMINDER DISCLAIMER &gt;=====[ &lt;PF1&gt;H=Help ]====

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards.  The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

Press RETURN to continue...

#### Edit Web Sites Example

Select Reminder Parameters Option: ews  Edit Web Sites

Choose from:

http://example.notreal.va.gov/reminders

http://secondexample.va.gov/cpg/cpg.htm

Select URL: ?

Answer with WEB SITES URL

Choose from:

http://example.notreal.va.gov/reminders

You may enter a new WEB SITES, if you wish

Enter the URL for the web site.

Select URL: http://example.notreal.va.gov/reminders

#### Edit Number of MH Tests Example

This option allows the site to select the Maximum number of MH questions to be used as a Reminder Dialog Finding Items. If the number of question in the selected MH test exceed the number in this parameter than the MH test cannot be used in the reminder dialog.

Select Reminder Managers Menu Option: PAR  Reminder Parameters

ESD    Edit Site Disclaimer

EWS    Edit Web Sites

MH     Edit Number of MH Questions

Select Reminder Parameters Option: MH  Edit Number of MH Questions

MAXIMUM NUMBER OF MH QUESTIONS: 100//

ESD    Edit Site Disclaimer

EWS    Edit Web Sites

MH     Edit Number of MH Questions

Select Reminder Parameters Option:

### Reminder Patient List Management

New tools for creating and managing reminder patient lists were introduced with Clinical Reminders V2.0. The patient list functionality provides a way to identify patients with specific findings or combinations of findings, without having to search one-by-one through every patient registered on the system.

***Patient List summary (from REDACTED, Puget Sound HCS)***

Clinical Reminder patient lists and extracts represent a watershed advance in VA’s clinical information armamentarium. Before their creation, front-line clinicians wishing to search for clinical data (for evidence-based medicine, process improvements, or clinical research) were limited to VA FileMan. While powerful, FileMan is too esoteric and resource-intensive for many clinicians. Alternatively, several VISNs have data warehouses and allow clinicians to write SQL scripts to search them; but again, the learning curve is steep and the data can be historical and, therefore, not useful for time-sensitive searches.

Because FileMan and SQL are difficult to learn, clinicians are often reliant on technical intermediaries and are subject to their availability. In contrast, the clinical reminder patient list functionality is relatively accessible and comprehensible (with minimal training) to front-line clinicians, allowing any clinician to become an informaticist, avoiding the risk of clinical questions being diluted or lost in translation. With the number of VA clinicians nationwide finally able to access the rich VA database, the potential for advances in patient safety, patient therapy, and processes that realize time and budget savings is boundless. Reminder indexes make the queries fast and consume relatively few computer resources. The searchable database is up-to-date, making patient lists useful for daily patient safety surveillance reporting. Lists can be auto-tasked to run monthly, quarterly, and annually and rolled up into a message for possible transmission to regional patient registries or county health departments.

The patient list functionality was originally created to support reminder extract reports. Reminder extract reports rely on the patient list tools to build patient lists that meet specific finding criteria. The numbers of patients on the patient lists created and used for extract reports are often referred to as patient denominators. The lists of patients are used to evaluate specific reminders to calculate compliance totals and finding totals.

Patient lists can also be created and used independently of extract reporting.

This patient list-building tool uses the Clinical Reminders Index global; consequently, it can build patient lists very quickly. The Clinical Reminders Index provides indexes that support finding all patients with a particular finding (also known as “across-patient look-ups”). The Index global also supports rapidly accessing finding data for a specific patient.

**Example** : At a medium-sized site, the Index global was used to build a list of all patients with a diabetic diagnosis in the last five years in about two minutes. There were approximately 10,000 patients on the list.

Once a patient list has been created by the reminder patient list tools, it can be stored and used for a number of purposes: a base list for building other patient lists, reminder extract reports, input to reminder due reports, input to health summaries, and creation of mailing lists and personalized form letters.

The reminder patient lists are stored in the Reminder Patient List file (#810.5). The Reminder Patient List Menu (PXRM PATIENT LIST MENU) provides access to the patient list management and list rule management functionality.

#### List Rules

List rules are the basic building blocks for constructing patient lists. A list rule may be defined using a reminder term, the patient cohort from a reminder definition, or an existing reminder patient list. Before a list rule can be created, the corresponding reminder term, reminder definition, or reminder patient list must already exist. Each list rule is defined independently. Once a list rule is defined, it can be combined with other list rules to build Rule Sets.

There are four types of list rules.

Type of List Rule		Abbreviation

Finding Rule 			     FR

Reminder Rule 			     RR

Patient List Rule 		     PL

Rule Set 			     RS

**TIP:** These four types of list rules are all stored in the same file, REMINDER LIST RULE (#810.4). A naming convention can be useful for ease of identifying list rule entries by type of list rule. One suggested convention is to use the abbreviations above as a prefix or suffix in the list rule name identifying the type of list rule. We will use this suggested naming convention for the examples of list rules in the List Rule Management Section.

**1.  Finding rules** are used to build lists of patients based on reminder terms. Reminder patient list tools will find patients with the finding(s) defined in the reminder term.

Most of the types of findings that can be defined in a reminder term have a Global Index for across-patient look-ups. However, the Global Index is not used for computed findings linked to a reminder term, unless the computed finding has hard-coded logic to access the Global Index. The typical computed finding assumes the patient is already selected and does not support across-patient look-up. However, with V2.0, a computed finding can be specifically created for list-building purposes by defining the Type field in the computed finding definition as “List.” The List type computed finding can be used as the first rule, or any subsequent rule in a rule set where the ADD PATIENT Operation is used. When a computed finding is used to SELECT or REMOVE patients from an existing patient list, a “single” or “multiple” type computed finding may be used.

**2.  Reminder rules** are used to build lists of patients based on a reminder definition and its patient cohort logic. Before a reminder definition is used to build a patient list, the cohort logic is checked to make sure it meets certain criteria. If it doesn’t, a warning message will be issued. This is done to make sure that building the list is computationally feasible. The criteria for using a reminder definition are:

The cohort logic cannot start with a logical not

The cohort logic cannot contain a logical or not

If AGE is used in the cohort logic, then a baseline age range must be defined

If SEX is used in the cohort logic the reminder must be sex-specific

SEX cannot be the first element in the cohort logic unless it is followed by AGE

If a finding sets the frequency to 0Y, which effectively removes the patient from the cohort, it can’t have an associated age range

The USAGE field must be specified as “L” for Patient List

**3.  Patient List rules** are used to build a new reminder patient list based on the patients in an existing reminder patient list. An existing patient list can be used to create a new list, add patients to a list, remove patients from a list if they are defined in the specified list, and remove patients from a list if they are not defined in the specified list.

**4.  List Rule Sets**

A rule set combines list rules and logical operations into a series of steps which are processed to build a patient list. The steps are processed in a numerical order that is based on the value of the SEQUENCE field, which is a three-digit number, i.e., 1 to 999. The first step initializes the list and subsequent steps can add patients (ADD PATIENT) to the list or remove (REMOVE or SELECT) them from it. Since the first step initializes the list, its operation must be ADD PATIENT. Subsequent steps may also use the ADD PATIENT operation to merge patients.

Logical operators (i.e., AND, AND NOT, OR), similar to those used in a reminder definition, are represented by the Rule Set Operations:

ADD PATIENT –  this works like a Boolean OR; any patient for which the finding is true will be added to the list. This should always be the operation for the first sequence in a rule set. Patient lists may be merged using the ADD PATIENT operation.

REMOVE – this works like a Boolean AND NOT; any patient for which the finding is true will be removed from the list.

SELECT –  this works like a Boolean AND; any patient for whom the finding is true will remain on the list and those for which the finding is false will be removed from the list.

One additional operation is available that is not related to Boolean logic:

INSERT FINDING – this is a special operation that lets you store patient data in the patient list. If the finding rule is based on the term VA-IHD STATION code or VA-PCMM INSTITUTION the patient’s PCMM institution will be stored with the list and when the patient list is displayed there will be a column that lists the PCMM Institution. The patient’s PCMM institution is determined by finding the patient’s PCMM team and then the Institution for the team. When the finding rule is based on any other terms, the “CSUB” data for the term will be stored with the list and can be used in the Patient Demographic Report.

#### Rule Set Definition

- Each rule set has a unique Name. National rule sets will have a name prefixed with “VA-“ or “VA-*“, and cannot be edited.
- Each rule set has a Class. Rule sets defined by a local site must be defined with the LOCAL or VISN Class. Nationally distributed rules sets will be have a NATIONAL class.
- Sequence: This three-digit number defines the order in which the list rules in the rule set will be evaluated.
- The ADD PATIENT operation is always used in the first sequential step, typically 001, to build the initial list of patients which can then be modified by subsequent rules. The ADD PATIENT operation can also be used on subsequent steps to add patients with a particular finding to an existing list of patients.
- Each sequential step uses the patient list from the prior step as the starting list to be added to or deleted from.
- It is good practice to initialize the list with the list rule that produce the smallest number of patients. For example if you need a list of patients with a certain diagnosis seen at specific locations you should initialize the list with the smaller of the two. If a finding list rule is defined with a reminder term that is defined with a computed finding, some special considerations need to be taken. If the computed finding is being used to select from or remove a patient from an existing list, than the typical computed finding can be used. If the computed finding will be used with the ADD PATIENT operation, then the computed finding must be defined with a “List” type.
- Each sequence may include Beginning Date/Time and Ending Date/Time.
- Beginning and Ending date/times are optional fields that can be defined in the List Rule which further restrict the criteria for building the patient list. Alternatively, the reminder term can contain the beginning and ending dates.
- The Patient List field is used for patient list rules. It defines the name of a patient list to be used as the patient source. If this field is defined, it overrides the Extract Patient List Name field.
- Extract Patient List Name field provides a mechanism to automatically generate patient list names for patient lists that are built on a recurring basis by extract runs. The name specified should contain “yyyy” for year and “Qnn” for quarter or “Mnn” for month. The string “yyyy” is automatically replaced by the four digit year and the “nn” is replaced by the number of the quarter or the number of the month. For example, one of the national IHD QUERI rule sets contains the extract patient list VA-*IHD QUERI yyyy Mnn PTS WITH QUALIFY AND ANCHOR VISIT; if an extract was run for November 2005 the resulting patient list would have the name VA-*IHD QUERI 2005 M11 PTS WITH QUALIFY AND ANCHOR VISIT.

In current national rule sets, the Beginning Date and Ending Date/time information is not defined at the Sequence level. It is defined in the Finding Rule, instead of the reminder term. The finding rule (FR) name reflects the dates or the period of time represented by the beginning and ending dates. The national extract patient list name is sent to Austin with related total counts. The patient list names reflect enough information for Austin users to understand which patients the counts are related to. The number of patients on the patient list typically represent one of the patient denominators used for extract reports. **Simple Rule Set definition with one List Rule**

This rule set only has one step and it is used to build a list of all patients who had a diabetic diagnosis in the last five years.

Name:  RS-DIABETIC PATIENTS

Number:  20

Class:  LOCAL

Description:

Rule Type:  RULE SET

Component Rules

---------------

Sequence: 001

Seq Beginning Date: BDT-5Y

Seq Ending Date: BDT

Operation: ADD PATIENT

List Rule: FR-DIABETIC DIAGNOSIS

Description: This is a taxonomy for diabetic diagnosis.

Rule Type: FINDING RULE

Reminder Term: DIABETIC DIAGNOSIS

**Expanded Rule Set  with two List Rules**

An example of a more complex rule set builds a list of all diabetic patients who have not had a diabetic eye exam.

Display/Edit Rule             Jun 08, 2006@12:29:21          Page:    2 of    3

+

Name:  RS-DIAB PTS W/O DIAB EYE EXAM

Number:  27

Class:  LOCAL

Description:

Rule Type:  RULE SET

Component Rules

---------------

Sequence: 001

Operation: ADD PATIENT

List Rule: FR-DIABETIC DIAGNOSIS

Description: This is a taxonomy for diabetic diagnosis.

Rule Type: FINDING RULE

Reminder Term: DIABETIC DIAGNOSIS

Sequence: 002

Operation: REMOVE

List Rule: FR-DIABETIC EYE EXAM

Description:

Rule Type: FINDING RULE

Reminder Term: DIABETIC EYE EXAM

Step 001 initializes the list with all patients who have a diabetic diagnosis and step 002 removes any patients who have had a diabetic eye exam. The result is a list containing all diabetic patients who have **not** had a diabetic eye exam.

Note: The name of the Rule Set is summarized text representing the combination of the List Rules.

**National Rule Set Example**

Below is an example of one of the nationally released rule sets for the IHD QUERI extract. The rule set contains four finding rules.

Display/Edit Rule             Jun 01, 2006@10:21:39          Page:    1 of    4

Name:  VA-*IHD QUERI PTS WITH QUALIFY VISIT

Number:  7

Class:  NATIONAL

Description:  IHD patients with a qualifying visit.

Rule Type:  RULE SET

Component Rules

---------------

Sequence: 001

Operation: ADD PATIENT

List Rule: VA-*IHD QUERI DIAGNOSIS

Description: Patients with IHD diagnosis in past 5 years.

Rule Type: FINDING RULE

Reminder Term: VA-IHD DIAGNOSIS

LR Beginning Date: BDT-5Y

Sequence: 002

Operation: SELECT

List Rule: VA-*IHD QUERI QUALIFYING VISIT

Description: Patients with visit to EPRP locations in report period.

Rule Type: FINDING RULE

Reminder Term: VA-IHD QUERI QUALIFYING ENCOUNTER

LR Beginning Date: BDT

LR Ending Date: T

Sequence: 003

Operation: REMOVE

List Rule: VA-*IHD QUERI AMI DIAGNOSIS WITHIN 60 DAYS

Description: Patients with Inpatient AMI Diagnosis within 60 days.

Rule Type: FINDING RULE

Reminder Term: VA-IHD AMI DIAGNOSIS WITHIN 60 DAYS

Sequence: 004

Operation: INSERT FINDING

List Rule: VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION

Description: Associate primary facility.

Rule Type: FINDING RULE

Reminder Term: VA-IHD STATION CODE

This rule set gets all patients with an IHD Diagnosis documented within 5 years prior to the report start date. This list of patients is modified in sequence 002 to remove all patients that have not had a visit documented for an EPRP clinic location during the reporting month, where T in the Beginning Date represents the report start date and T in the Ending Date represents the report ending date.This list is further modified in sequence 003 to remove patients that have an AMI diagnosis documented within the past 60 days. The patient list after sequence 003 is further modified by associating each patient’s primary care station and storing the station with each patient in the patient list.

National list rules cannot be modified.

#### Steps to Create a Patient List

This is the sequence of steps to create a patient list:

1. Create list rules (FR, RR, or PLR)
2. Create rule sets
3. Create patient list

You must create list rules first. Once list rules are defined, they can be referenced in a rule set. Once the rule set is defined, the patient list tools can use the rule set to create a patient list.

NOTE: The Reminder Definition that is used in a Reminder Rule must have “L” (Reminder Patient List) in the Usage field or it will not be able to be used in a Reminder Rule.

Prior to creating list rules and rule sets, it is a good idea to write down the criteria clearly enough so that anyone else will know exactly how the patient list should be built.

- What patient finding(s) should be used to build the list of patients?
- What finding should be used to create the first list of patients?
- Should this list be modified to remove patients with a particular finding?
- Should this list be modified to remove patients that do not have a particular finding?
- For each finding, what are the appropriate beginning and ending dates?
- What sequence will have the least impact on computer system resources?
- Who should be able to see the patient list?

The criteria for building a reminder patient list can be documented in the description field of the rule set. The criteria should take into consideration the most efficient sequence in which patient extracts should occur, to limit unnecessary impacts on system operations.

##### Patient List Menu

The Patient List Menu option on the PXRM MANAGERS MENU provides the following options for creating and managing list rules and patient lists.

| Syn.   | Name                    | Option Name               | Description                                                                                                                                                                                                                                                                                                                            |
|--------|-------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LRM    | List Rule Management    | PXRM LIST RULE MANAGEMENT | This option allows creation of list rules, which build patient lists and test rule set criteria. Nationally released list rules are used by nationally released extract definitions for national extract runs.  There are four types of list rules: Finding Rule, Reminder Rule, Patient List Rule, and Rule Set.                      |
| PLM    | Patient List Management | PXRM EXTRACT PATIENT LIST | This option manages reminder patient lists. Local patient lists may be created from list rules, copied to OE/RR teams, copied to other patient lists, or deleted.  Local patient lists and national patient lists (from the extract process) are listed. Individual lists may be displayed or printed or used to run health summaries. |

##### List Rule Management Option

The List Rule Management option presents a list of existing reminder rule file entries. The possible actions available for each type of entry are presented in the bottom portion of the screen.

**List Rule Management screen example:**

List Rule Management          Jun 01, 2006@08:44:21          Page:    1 of    1 

 Item  Rule Set Name                                                 Class 1  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT           NATIONAL   
    2  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT ON LLA M  NATIONAL   
    3  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT               NATIONAL   
    4  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT ON LLA MEDS   NATIONAL   
    5  VA-*IHD QUERI PTS WITH QUALIFY VISIT                          NATIONAL   
    6  VA-*MH QUERI QUALIFYING PC VISIT                              NATIONAL   
    7  VA-*MH QUERY QUALIFYING MH VISIT                              NATIONAL **+ Next Screen   - Prev Screen   ?? More Action** CV   Change View                        TEST Test Rule Set
CR   Create Rule                        QU   Quit
DR   Display/Edit Rule
Select Item: Quit//

The default view is Rule Set; this screen is used to create, edit, and test rule sets. The Test Rule Set action applies only to rule sets. It can be used to test a rule set before it is used to build a patient list. When you use this action you enter list build beginning and ending dates, and then the rule set processes list rules in the sequential order defined in the rule set. For each sequence/step in the rule set, it shows you the list rule, and if the list rule uses a term or a definition, it shows all the findings and the final dates used for each finding.

**Test Rule Set example**

Rule Set Test         Oct 17, 2005@10:05:06          Page:    1 of    2 Rule Set Test
                                                                                
List Build Beginning Date: 10/17/2000                                           
List Build Ending Date: 10/17/2005                                              

SEQUENCE 1 FR-DIABETIC DIAGNOSIS                                              
 TERM DIABETIC DIAGNOSIS                                                        
  FINDING 1-TX.VA-DIABETES                                                      
   Beginning Date/Time: 06/01/2003                                              
   Ending Date/Time:    07/25/2004@23:59:59                                     
  FINDING 2-HF.OUTSIDE DIABETIC DIAGNOSIS                                       
   Beginning Date/Time: 02/28/1999                                              
   Ending Date/Time:    08/29/2001@23:59:59                                     

SEQUENCE 2 VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION                       
 TERM VA-IHD STATION CODE                                                       

SEQUENCE 3 FR-BMI   
TERM BMI                                                                       
  FINDING 1-CF.VA-BMI                                                           
   Beginning Date/Time: 10/17/2000                                              
   Ending Date/Time:    10/17/2005@23:59:59                                     

SEQUENCE 004 FR-FINGERSTICK                                                     
 TERM FINGERSTICK, GLUCOSE                                                      
  FINDING 1-OI.FINGERSTICK,GLUCOSE(WARD)                                        
   Beginning Date/Time: 10/17/2000                                              
   Ending Date/Time:    10/17/2005@23:59:59 **+ Next Screen   - Prev Screen   ?? More Action** Select Action:Next Screen//

Note that a local rule set can use national list rules, mixed with local list rules. Sequence 002 specifies a List Rule that identifies the facility that should receive the counts for the patient in a list.

The Change View (CV) action is used to select the screens for other types of list rules.

Select Item: Quit// CV   Change View  

     Select one of the following:

          F         Finding Rule
          P         Patient List Rule
          R         Reminder Rule
          S         Rule Set

TYPE OF VIEW: F//F

If we select the finding rule view, then the display changes to show the newly selected view.

List Rule Management          Jun 01, 2006@08:55:48          Page:    1 of    1 

 Item  Finding Rule Name                                             Class 1  FR-BMI                                                        LOCAL

2  FR-DIABETIC DIAGNOSIS                                         LOCAL

3  VA-*IHD QUERI 412 DIAGNOSIS                                   NATIONAL   
    4  VA-*IHD QUERI AMI DIAGNOSIS WITHIN 60 DAYS                    NATIONAL   
    5  VA-*IHD QUERI ANCHOR VISIT                                    NATIONAL   
    6  VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION                  NATIONAL   
    7  VA-*IHD QUERI DIAGNOSIS                                       NATIONAL   
    8  VA-*IHD QUERI LIPID LOWERING MEDS                             NATIONAL   
    9  VA-*IHD QUERI QUALIFYING VISIT                                NATIONAL   
    10 VA-*MH QUERI QUALIFY MH VISIT                                 NATIONAL   
    11 VA-*MH QUERI QUALIFY PC VISIT                                 NATIONAL **+ Next Screen   - Prev Screen   ?? More Action** CV   Change View                        TEST Test Rule Set
CR   Create Rule                        QU   Quit
DR   Display/Edit Rule
Select Item: Quit//

When you are in the desired view, the CR (Create Rule) action is used to create a new list rule and the DR (Display/Edit Rule) action is used to display/edit an existing rule. Note that typing the item number is the same as selecting the DR action.

#### Patient List Management Option

The Patient List Management option presents a list of available reminder patient lists. The patient lists displayed will include local and national patient lists that you have access to.

**Note on national patient lists** : The example below includes several national patient lists created by the monthly VA-IHD QUERI extract runs. Each month the VA-IHD QUERI extract was run, there were five different national patient lists created. Each patient list has a unique name with abbreviated text in the patient title to reflect the criteria used to create the list. Each of the five patient lists was used by extract reporting tools to evaluate reminders and create compliance and finding totals. See the section called National Reminder Extract Reporting for more information on Reminder Extract Report processing.

**Patient List Management screen example**

Reminder User Patient List    Jun 01, 2006@12:08:18          Page:    1 of    7 Available Patient Lists. Item  Reminder Patient List Name                     Created          Patients 1  VA-*IHD QUERI 2000 M4 412 PTS WITH QUALIFY AN  4/27/04@11:55:43        0 
    2  VA-*IHD QUERI 2000 M4 412 PTS WITH QUALIFY AN  4/27/04@11:55:43        0 
    3  VA-*IHD QUERI 2000 M4 PTS WITH QUALIFY AND AN  4/27/04@11:55:43        0 
    4  VA-*IHD QUERI 2000 M4 PTS WITH QUALIFY AND AN  4/27/04@11:55:43        0 
    5  VA-*IHD QUERI 2000 M4 PTS WITH QUALIFY VISIT   4/27/04@11:55:43        0 
    6  VA-*IHD QUERI 2001 M10 412 PTS WITH QUALIFY A  7/20/04@08:28:08        2 
    7  VA-*IHD QUERI 2001 M10 412 PTS WITH QUALIFY A  7/20/04@08:28:09        0 
    8  VA-*IHD QUERI 2001 M10 PTS WITH QUALIFY AND A  7/20/04@08:28:08        4 
    9  VA-*IHD QUERI 2001 M10 PTS WITH QUALIFY AND A  7/20/04@08:28:08        0 
   10  VA-*IHD QUERI 2001 M10 PTS WITH QUALIFY VISIT  7/20/04@08:28:07        5 
   11  VA-*IHD QUERI 2001 M11 412 PTS WITH QUALIFY A  7/20/04@08:31:23        0 
   12  VA-*IHD QUERI 2001 M11 412 PTS WITH QUALIFY A  7/20/04@08:31:23        0 
   13  VA-*IHD QUERI 2001 M11 PTS WITH QUALIFY AND A  7/20/04@08:31:23        0 
   14  VA-*IHD QUERI 2001 M11 PTS WITH QUALIFY AND A  7/20/04@08:31:23        0 
   15  VA-*IHD QUERI 2001 M11 PTS WITH QUALIFY VISIT  7/20/04@08:31:23        0 
   16  VA-*IHD QUERI 2001 M12 412 PTS WITH QUALIFY A  7/20/04@08:35:47        0 **+ Next Screen   - Prev Screen   ?? More Action** CO   Copy Patient List    DE   Delete Patient List  CV   Change View 
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   Quit
Select Item: Next Screen//

The actions on this screen are:

CO (Copy Patient List) – copy an existing patient list to a new patient list

COE (Copy to OE/RR Team) – copy a patient list to an OE/RR Team list

CR (Create Patient List) – create a new patient list

DE (Delete Patient List) – delete selected patient list(s)

DCD (Display Creation Doc) – display the documentation on how a patient list was created

DSP (Display Patient List) – display the contents of a patient list

CV(Change View) – toggles the display order of the list between one sorted by list name and one sorted by list type

LRM (List Rule Management) – this action takes you to the List Rule Management screen

When creating a local patient list, you are given the option to secure the list or to make it public for all to use. The type of security on the list is available by scrolling the list to the right.

When viewing the list of patient lists, there are two symbols: “&lt;&lt;&lt;”and “&gt;&gt;&gt;” on the action line. These are standard List Manager symbols that mean you can scroll the view to the left using the left arrow key and to the right using the right arrow key. If the view is scrolled to the right, you can see the “Type” of list, public (PUB) or private (PVT), and your “Access” to the list full (F) or view (V).

If the list has a Type of PUB, then the list can be used by all users with access to the Patient List Management option. The level of Access may be restricted to View (Read Only), or Full access (Delete, and Update actions).

For any secure list, the creator of the patient list can add additional users to the list and assign one of two permissions to the user; view only or full access.

This is an example of a screen that has been scrolled to the right. Note that the sequence number and patient list name are still displayed on the left side of the column with the Type and Access columns.

Reminder User Patient List    Sep 27, 2005@09:36:05          Page:    1 of    8 Available Patient Lists.
+Item  Reminder Patient List Name                      Type  Access             
    5  AGP IHD EXTRACT WITH QUALIFY VISIT               PVT    F                
    6  AGP IHD QUERI PTS WITH QUALIFY AND ANCHOR VIS    PVT    F                
    7  AGP OE/RR TEAM 1                                 PUB    F                
    8  AGP OERR TEAM LIST                               PUB    F                              
    9  CRPATIENT                                        PUB    F                
   10  CRPATIENT2                                       PUB    F                
   11  DIAB PTS W/O DIAB EYE EXAM                       PUB    F                          
   12  PJH EXTRACT 2004 M10 BP                          PVT    V **+ Next Screen   - Prev Screen   ?? More Action** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   Quit
Select Item: Next Screen//

##### Patient List Creation Action

When you select the CR (Create Patient List) action, there are a number of prompts that must be answered before the patient list can be created. The following is a detailed explanation of each of these prompts.

**Secure List?**

If the answer to this prompt is “YES,” the list becomes a private list, which means that the only people who can view the list are the creator, anyone who the creator has given view access, and anyone who holds the PXRM MANAGER KEY.

**Purge Patient List after 5 years?**

The response to this prompt sets the value of the Patient List file field AUTOMATICALLY PURGE. Whenever an automatic extract is run, if a patient list is more than 5 years old, AUTOMATICALLY PURGE is checked, and if its value is “YES,” the patient list is deleted.

**Select LIST RULE SET**

This is the rule set that is used to construct the list.

**Enter Patient List BEGINNING DATE**

This prompt is used to enter the values for the list build beginning date. The value entered can be:

standard Clinical Reminders symbolic dates like T-5Y,

an actual date like 09/30/2005; any of the standard FileMan date formats are acceptable.

**Enter Patient List ENDING DATE**

This prompt is used to enter the values for the list build beginning date. The value entered can be:

standard Clinical Reminders symbolic dates like T-5Y,

an actual date like 09/30/2005; any of the standard FileMan date formats are acceptable.

**Include deceased patients on the list? N//** The default is to not include deceased patients in patient lists. If the answer to this prompt is “YES,” then deceased patients will be included.

**Include test patients on the list? N//** The default is to not included test patients in patient lists. If the answer to this prompt is “YES,” then test patients will be included.

##### Dates in Patient Lists

When you build a patient list, you are prompted to enter a Beginning Date and an Ending Date; for the purposes of this discussion we will call these the Patient List Beginning Date (PL BDT) and the Patient List Ending Date (PL EDT). There can also be a beginning date and ending date specified for each sequence in a rule set, for a finding rule, and for each finding in a term or definition.

These dates specify the period of time in which to search for patient data so it is important to understand the relationships between the BDT and EDT values at each level. For discussion purposes, the Beginning Date at the sequence, finding rule, and reminder term level is referred to as BDT, and Ending Date is referred to as EDT. For each level, the BDT and EDT values represent the date range that will be used to search for the findings.

The following is the hierarchy of date ranges and options for values that can be defined in the BDT and EDT fields at each level.

**1)  Patient List BDT and EDT (required)**

- Patient List BDT and EDT values are entered by the person creating the patient list.
- The Patient List BDT is represented symbolically by “BDT” and may be used in any of the list rule dates.
- The Patient List EDT is represented symbolically by “T” and may be used in any of the list rule dates. If “T” is used in the term or definition date fields it will take the value of the patient list EDT.

**2)  Sequence BDT and EDT for each rule in the rule set (optional)**

- Dates defined at the sequence level override those defined at the patient list level.
- Actual dates are used directly.
- Symbolic values can be used for both the BDT and EDT. The symbol “BDT” is equal to the PL BDT so a date such as “BDT-6M” is PL BDT minus 6 months. The symbol “T” is equal to the PL EDT.
- When 0 is entered for BDT it means start at the beginning of patient data and 0 for EDT means ignore PL EDT and use the end of today for the end of the search range.

3)  Finding Rule BDT and EDT (optional)

- Dates defined in the finding rule override those defined at the sequence.
- Actual dates are used directly.
- Symbolic values can be used for both BDT and EDT. The symbol “BDT” is equal to the PL BDT so a date such as “BDT-6M” PL BDT minus 6 months. The symbol “T” is equal to the PL EDT.
- When 0 is entered for BDT it means start at the beginning of patient data and 0 for EDT means ignore PL EDT and use the end of today for the end of the search range.

**4) Reminder Term and Definition BDT and EDT (optional)**

- Each finding can optionally be defined with BDT and EDT values and these will override those defined at the finding rule and/or sequence level.
- Actual dates are used directly.
- Symbolic dates can only use “T” which is equal to PL BDT.

**Summary of date range overrides when searching for a particular finding**

- The patient list BDT and EDT define the default date range to use to search for a particular finding unless the BDT or EDT is defined for the Rule Set Sequence, Finding Rule, or Reminder Term or Definition Finding.

- For each sequence in the rule set, you can override the Patient List’s BDT or EDT by adding a BDT and EDT for each sequence in the Rule Set.

- For each Finding rule defined in a rule set sequence, you can override the Rule Set Sequence BDT and EDT value and the Patient List’s BDT or EDT value by adding a BDT and EDT for the Finding Rule.

- For each Finding defined in a Reminder Term, you can override the BDT and EDT values at the Finding Rule, Rule Set Sequence and Patient List levels by adding a BDT and EDT for each finding in the Reminder Term or Definition.

- The following table summarizes the possible interactions between the various dates based on a Patient List Beginning Date of Sep 01, 2005 and Ending Date of Sep 30, 2005. This example is creating a patient list for the month of September 2005.

The table columns are as follows:

Date Range # represents the various examples of how to define the Beginning Date Time (abbreviated in the Date Fields column as BDT) and Ending Date Time (abbreviated in the Date Fields column as EDT) in the four columns (List Build Date Range, Rule Set Sequence, Finding Rule, and Reminder Term Findings

The Date Fields column shows BDT or EDT to represent the beginning date/time or ending date/time for each level that beginning and ending dates can be defined (List Build, Rule Set Sequence, Finding Rule, and Reminder Term Finding.

The List Build column represents the dates you are prompted for when building a patient list. If run from an extract, this column is the extract’s reporting period.

The Rule Set Sequence column represents date values defined at the sequence level in a rule set.

The Finding Rule column represents date field values defined in the list Finding Rule.

The Reminder Term Finding column represents date field values defined at the finding level for a reminder term.

The Search Date Range for Finding column shows the dates that will be used for each scenario when the list is actually built.

Times can optionally be specified, but if they are not, the beginning date/time defaults to the start of the day and the ending date/time defaults to the end of the day.

Whenever T is used in the Rule Set Sequence, Finding Rule, or Reminder Term Finding columns, T will always be equal to the List Build Ending Date/time.

Whenever BDT is used in the Rule Set Sequence, Finding Rule, or Reminder Term Finding columns, BDT will always be equal to the List Build Beginning Date/time.

| **Date Range**  **#**   | **Date Fields**   | **List Build**   | **Rule Set Sequence**   | **Finding Rule**   | **Reminder Term Finding**   | **Search Date Range for Finding**                           |
|-------------------------|-------------------|------------------|-------------------------|--------------------|-----------------------------|-------------------------------------------------------------|
| 1                       | BDT               | Sep 01, 2005     | Blank                   |                    |                             | Sep 01, 2005                                                |
|                         | EDT               | Sep 30, 2005     | Blank                   |                    |                             | Sep 30, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 2                       | BDT               | Sep 01, 2005     | T-2Y                    |                    |                             | Sep 30, 2003                                                |
|                         | EDT               | Sep 30, 2005     | Blank, same as T or EDT |                    |                             | Sep 30, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 3                       | BDT               | Sep 01, 2005     | BDT-2Y                  |                    |                             | Sep 01, 2003                                                |
|                         | EDT               | Sep 30, 2005     | T-1Y                    |                    |                             | Sep 30, 2004                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 4                       | BDT               | Sep 01, 2005     | BDT-6M                  |                    |                             | Mar 01, 2005                                                |
|                         | EDT               | Sep 30, 2005     | BDT                     |                    |                             | Sep 01, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 5                       | BDT               | Sep 01, 2005     | 0 (zero)                |                    |                             | No beginning date                                           |
|                         | EDT               | Sep 30, 2005     | Mar 28, 2003            |                    |                             | Mar 28, 2003                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 6                       | BDT               | Sep 01, 2005     | Apr 09, 2001            |                    |                             | Apr 09, 2001                                                |
|                         | EDT               | Sep 30, 2005     | Mar 28, 2003            |                    |                             | Mar 28, 2003                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 7                       | BDT               | Sep 01, 2005     | Apr 09, 2001            |                    |                             | Apr 09, 2001                                                |
|                         | EDT               | Sep 30, 2005     | 0 (zero)                |                    |                             | End of day on date the list is built.                       |
|                         |                   |                  |                         |                    |                             |                                                             |
| 8                       | BDT               | Sep 01, 2005     |                         | T-2Y               |                             | Sep 30, 2003                                                |
|                         | EDT               | Sep 30, 2005     |                         | T-1Y               |                             | Sep 30, 2004                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 9                       | BDT               | Sep 01, 2005     |                         | BDT-2Y             |                             | Sep 01, 2003                                                |
|                         | EDT               | Sep 30, 2005     |                         | Blank or T         |                             | Sep 30, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 10                      | BDT               | Sep 01, 2005     |                         | BDT-6M             |                             | Mar 01, 2005                                                |
|                         | EDT               | Sep 30, 2005     |                         | BDT                |                             | Sep 01, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 11                      | BDT               | Sep 01, 2005     |                         | 0 (zero)           |                             | No beginning date                                           |
|                         | EDT               | Sep 30, 2005     |                         | Mar 28, 2003       |                             | Mar 28, 2003                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 12                      | BDT               | Sep 01, 2005     |                         | Apr 09, 2001       |                             | Apr 09, 2001                                                |
|                         | EDT               | Sep 30, 2005     |                         | Mar 28, 2003       |                             | Mar 28, 2003                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 13                      | BDT               | Sep 01, 2005     |                         | Apr 09, 2001       |                             | Apr 09, 2001                                                |
|                         | EDT               | Sep 30, 2005     |                         | 0 (zero)           |                             | End of day on date the list is built.                       |
|                         |                   |                  |                         |                    |                             |                                                             |
| 14                      | BDT               | Sep 01, 2005     |                         |                    | T-2Y                        | Sep 30, 2003                                                |
|                         | EDT               | Sep 30, 2005     |                         |                    | T-1Y                        | Sep 30, 2004                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 15                      | BDT               | Sep 01, 2005     |                         |                    | 0 (zero)                    | No beginning date                                           |
|                         | EDT               | Sep 30, 2005     |                         |                    | BDT                         | Sep 30, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 16                      | BDT               | Sep 01, 2005     |                         |                    | Apr 09, 2001                | Apr 09, 2001                                                |
|                         | EDT               | Sep 30, 2005     |                         |                    | Mar 28, 2003                | Mar 28, 2003                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 17                      | BDT               | Sep 01, 2005     | T-2Y                    | T-1Y               |                             | Sep 30, 2004                                                |
|                         | EDT               | Sep 30, 2005     | T-1Y                    | T-6M               |                             | Mar 28, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 18                      | BDT               | Sep 01, 2005     | Jun 01, 2003            | BDT                |                             | Sep 1, 2005 (BDT &gt; EDT;  no finding match will be found) |
|                         | EDT               | Sep 30, 2005     | Jul 25, 2004            | T-6M               |                             | March 30, 2005                                              |
|                         |                   |                  |                         |                    |                             |                                                             |
| 19                      | BDT               | Sep 01, 2005     | T-1Y                    | BDT-6M             | T-1Y                        | Sep 30, 2004                                                |
|                         | EDT               | Sep 30, 2005     | T                       | BDT                | T-6M                        | Mar 31, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 20                      | BDT               | Sep 01, 2005     | Apr 09, 2001            |                    | T-2Y                        | Sep 30, 2003                                                |
|                         | EDT               | Sep 30, 2005     | Feb 28, 2002            |                    | Blank or T                  | Sep 30,2005                                                 |
|                         |                   |                  |                         |                    |                             |                                                             |
| 21                      | BDT               | Sep 01, 2005     | T-2Y                    |                    | T-1Y                        | Sep 30, 2004                                                |
|                         | EDT               | Sep 30, 2005     | 0 (zero)                |                    | T-6M                        | Mar 31, 2005                                                |
|                         |                   |                  |                         |                    |                             |                                                             |
| 22                      | BDT               | Sep 01, 2005     |                         | Apr 09, 2001       | Jun 01, 2003                | Jun 01, 2003                                                |
|                         | EDT               | Sep 30, 2005     |                         | Feb 28, 2002       | Jul 25, 2004                | Jul 25, 2004                                                |

Date Range #1 shows that if no dates are defined at the sequence, finding rule, or reminder term finding level, the List Build dates are used to search for the finding defined in the reminder term.

Date Range #2-7 are examples of the Rule Set Sequence BDT and EDT overriding the List Build BDT and EDT. The Rule Set Sequence BDT and EDT dates are used to determine the date range to use for the finding in the reminder term.

Date Range #2 shows symbolic dates defined at the sequence level using “T”. T is the List Build ending date/time.

Date Range #3 shows symbolic dates defined at the sequence level using ”BDT” (the List Build Beginning Date/time) and “T” (the List Build Ending Date Time).

Date Range #4 shows symbolic dates defined at the sequence level using “BDT” (the List Build Beginning date/time) in both the Rule Set Sequence BDT and EDT fields.

Date range #5 shows 0 (zero) entered as the sequence level beginning date with an actual date specified as the sequence level ending date. The 0 will cause the search for the finding to not limit how far back in history a reminder finding will be looked for, which is similar to the way a finding works in a reminder definition when the finding has a blank beginning date. The actual date entered as the ending date will be used directly, overriding the List Build end date.

Date range #6 shows that when actual dates are defined at the sequence level, they take precedence and are used directly.

Date range #7 shows an actual date specified as the sequence level beginning date, and “0” (zero) entered as the sequence level ending date. The actual date entered as the beginning date will be used directly, overriding the List Build beginning date. The “0” in the Sequence ending date will cause the search for the Reminder Term finding to use the end of the day on the day the patient list is created, overriding the List Build ending date. The actual date specified will be the beginning date, and TODAY@11:59pm will be used as the ending date.

Date Range #8-13 are examples of the Finding Rule BDT and EDT overriding the List Build BDT and EDT. The Finding Rule BDT and EDT dates are used to search for the findings defined in the finding rule’s reminder term.

Date Range #8 shows symbolic dates defined at the finding rule level using “T” (the List Build ending date/time).

Date Range #9 shows symbolic dates defined at the finding rule level using ”BDT” (List Build Beginning date/time) and “T”(List Build Ending date/time. If there is no EDT value defined in the Finding Rule EDT, then the List Build Ending date/time is used.

Date Range #10 shows symbolic dates defined at the finding rule level using ”BDT” (the Patient List Beginning date/time).

Date range #11 shows “0” (zero) entered as the finding rule level beginning date and an actual date specified as the finding rule level ending date. The “0” will cause the search for the finding to not limit how far back in history the finding will be looked for, which is similar to the way a finding works in a reminder definition when the finding has a blank beginning date. The actual date entered as the ending date will be used directly, overriding the List Build ending date.

Date range #12 shows that when actual dates are defined in the BDT and EDT fields at the finding rule level, they override the List Build BDT and EDT.

Date range #13 shows an actual date specified as the finding rule level beginning date, and “0” (zero) entered as the finding rule level ending date. The actual date entered as the beginning date will be used directly, overriding the Patient List beginning date. The “0” (zero) in the finding rule ending date will use the end of the day on the day the patient list is created, overriding the List Build ending date. The date range used to search for the reminder term findings becomes the actual beginning date through the end of the day on the date the list is built(TODAY@11:59pm).

Date Range #14-17 are examples of the Reminder Term Finding BDT and EDT overriding the List Build BDT and EDT. The BDT and EDT dates are used to search for the findings defined in the finding rule’s reminder term.

Date Range #14 shows symbolic dates defined at the finding rule level using “T” (the List Build ending date/time).

Date range #15 shows “0” (zero) entered as the finding rule level beginning date and uses the symbolic BDT (List Build Beginning date/time) as the ending date. actual date specified as the finding rule level ending date. The “0” will cause the search for the finding to not limit how far back in history the finding will be looked for, which is similar to the way a finding works in a reminder definition when the finding has a blank beginning date. .

Date range #16 shows that when actual dates are defined in the BDT and EDT fields at the finding rule level, they override the List Build BDT and EDT.

Date range #17 and 18 are examples of what happens when Beginning and Ending date/time values are defined at the List Rule Sequence level and Finding Rule level. The Finding Rule level’s beginning and ending date values will override the List Rule Sequence level’s beginning and ending date values. BDT values are replaced with the List Build beginning date/time and T values are replaced with the Lit Build Ending date/time.

Date range #19 is an example of beginning and ending date values defined at every level, and where the Reminder Term Finding Beginning date/time and Ending date/time override all other levels.

Date range #20-22 is an example of the Reminder Term Findings beginning and ending date/times overriding miscellaneous other levels of beginning and ending date/time definitions.

##### Creating a Simple Patient List

As an example, let’s build a list of all our diabetic patients.

**1. Create a Reminder rule using a reminder term**

The first thing we must do is find or create a reminder term that identifies diabetes patients. If you are not familiar with how to do this, see the Reminder Term Management section of this manual. The examples below assume the following Reminder Term defines the criteria to identify diabetes patients.

**Diabetic Diagnosis term:**

DIABETIC DIAGNOSIS                                             No.606
----------------------------------------------------------------------------
Class:                  LOCAL
Sponsor:                
Date Created:           
Review Date:            

Description:

Edit History:

    Edit Date: JUN  3,2005  09:54       Edit By:
    Edit Comments:

Findings:   

                  Finding Item:  VA-DIABETES  (FI(1)=TX(28))
                  Finding Type:  REMINDER TAXONOMY

The Reminder Term called DIABETIC DIAGNOSIS is defined to use the Finding Item VA-DIABETES to identify whether a patient has a diabetic diagnosis.

**Use the Reminder Term to build a List Rule**

1a. Select the List Rule Management option.

List Rule Management                Jun 03, 2005@10:41:29 Page: 1 of 1

Item  Rule Set Name                                                 Class 1  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT           NATIONAL   
    2  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT ON LLA M  NATIONAL   
    3  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT               NATIONAL   
    4  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT ON LLA MEDS   NATIONAL   
    5  VA-*IHD QUERI PTS WITH QUALIFY VISIT                          NATIONAL   
    6  VA-*MH QUERI QUALIFYING PC VISIT                              NATIONAL   
    7  VA-*MH QUERY QUALIFYING MH VISIT                              NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        TEST Test Rule Set
CR   Create Rule                        QU   Quit
DR   Display/Edit Rule
Select Item: Quit// CV   Change View

1b. Select CV to change the view

Select one of the following:

F         Finding Rule

P         Patient List Rule

R         Reminder Rule

S         Rule Set

TYPE OF VIEW: F// Finding Rule

1c.  Press Enter to accept the default of Finding Rule

1d.  Select CR to create the rule.

List Rule Management          Jun 03, 2005@10:41:33          Page:    1 of    1 
 Item  Finding Rule Name                                             Class 1  VA-*IHD QUERI 412 DIAGNOSIS                                   NATIONAL   
    2  VA-*IHD QUERI AMI DIAGNOSIS WITHIN 60 DAYS                    NATIONAL   
    3  VA-*IHD QUERI ANCHOR VISIT                                    NATIONAL   
    4  VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION                  NATIONAL   
    5  VA-*IHD QUERI DIAGNOSIS                                       NATIONAL   
    6  VA-*IHD QUERI LIPID LOWERING MEDS                             NATIONAL   
    7  VA-*IHD QUERI QUALIFYING VISIT                                NATIONAL   
    8  VA-*MH QUERI QUALIFY MH VISIT                                 NATIONAL   
    9  VA-*MH QUERI QUALIFY PC VISIT                                 NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        TEST (Test Rule Set)
CR   Create Rule                        QU   Quit
DR   Display/Edit Rule
Select Item: Quit// CR   Create Rule

1e. Respond to the prompts as indicated below to define the local rule.

Select FINDING RULE to add: FR-DIABETIC DIAGNOSIS
  Are you adding 'FR-DIABETIC DIAGNOSIS' as 
    a new REMINDER LIST RULE (the 19TH)? No// Y  (Yes)

NAME: FR-DIABETIC DIAGNOSIS  Replace 
SHORT DESCRIPTION: 
CLASS: L  LOCAL
REMINDER TERM:    DIABETIC DIAGNOSIS     LOCAL
         ...OK? Yes// Y  (Yes)

LIST RULE BEGINNING DATE/TIME: 
LIST RULE ENDING DATE/TIME: 
Input your edit comments.
Edit? NO//

1f.  The new finding rule is now displayed in the list of Finding Rules.

List Rule Management  Jun 03, 2005@10:42:11          Page:    1 of    1 
 Item  Finding Rule Name                                             Class 1  FR-DIABETIC DIAGNOSIS                                         LOCAL      
    2  VA-*IHD QUERI 412 DIAGNOSIS                                   NATIONAL   
    3  VA-*IHD QUERI AMI DIAGNOSIS WITHIN 60 DAYS                    NATIONAL   
    4  VA-*IHD QUERI ANCHOR VISIT                                    NATIONAL   
    5  VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION                  NATIONAL   
    6  VA-*IHD QUERI DIAGNOSIS                                       NATIONAL   
    7  VA-*IHD QUERI LIPID LOWERING MEDS                             NATIONAL   
    8  VA-*IHD QUERI QUALIFYING VISIT                                NATIONAL   
    9  VA-*MH QUERI QUALIFY MH VISIT                                 NATIONAL   
   10  VA-*MH QUERI QUALIFY PC VISIT                                 NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        TEST (Test Rule Set)
CR   Create Rule                        QU   Quit
DR   Display/Edit Rule
Select Item: Quit//

**2. Create the rule set.**

Now that the finding rule has been created, we need to create the rule set.

2a. Select the List Rule Management option.

2b. Select CV to change the view to Rule Set.

List Rule Management          Jun 03, 2005@11:08:58          Page:    1 of    1 
 Item  Finding Rule Name                                             Class 1  FR-DIABETIC DIAGNOSIS                                         LOCAL      
    2  VA-*IHD QUERI 412 DIAGNOSIS                                   NATIONAL   
    3  VA-*IHD QUERI AMI DIAGNOSIS WITHIN 60 DAYS                    NATIONAL   
    4  VA-*IHD QUERI ANCHOR VISIT                                    NATIONAL   
    5  VA-*IHD QUERI ASSOCIATE PRIMARY CARE STATION                  NATIONAL   
    6  VA-*IHD QUERI DIAGNOSIS                                       NATIONAL   
    7  VA-*IHD QUERI LIPID LOWERING MEDS                             NATIONAL   
    8  VA-*IHD QUERI QUALIFYING VISIT                                NATIONAL   
    9  VA-*MH QUERI QUALIFY MH VISIT                                 NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        TEST (Test Rule Set)
CR   Create Rule                        QU   Quit
DR   Display/Edit RuleSelect Item: Quit// CV   Change View

2c. Select S for Rule Set.

Select one of the following:

          F         Finding Rule
          P         Patient List Rule
          R         Reminder Rule
          S         Rule Set

TYPE OF VIEW: F// S  Rule Set

2d. Select CR for Create Rule.

List Rule Management          Jun 03, 2005@11:09:03          Page:    1 of    1 

 Item  Rule Set Name                                                 Class 1  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT           NATIONAL   
    2  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT ON LLA M  NATIONAL   
    3  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT               NATIONAL   
    4  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT ON LLA MEDS   NATIONAL   
    5  VA-*IHD QUERI PTS WITH QUALIFY VISIT                          NATIONAL   
    6  VA-*MH QUERI QUALIFYING PC VISIT                              NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        DR   Display/Edit Rule
CR   Create Rule                        QU   Quit
Select Item: Quit// CR   Create Rule

2e. Respond to the prompts as indicated, to define the Rule Set.

Select RULE SET to add: RS-DIABETIC PATIENTS
  Are you adding 'RS-DIABETIC PATIENTS' as 
    a new REMINDER LIST RULE (the 20TH)? No// Y  (Yes)
NAME: RS-DIABETIC PATIENTS  Replace 
SHORT DESCRIPTION: 
CLASS: L  LOCAL
Select SEQUENCE: 1
  Are you adding '1' as a new SEQUENCE (the 1ST for this REMINDER LIST RULE)? Y
  (Yes)
   SEQUENCE LIST RULE: FR-DIABETIC DIAGNOSIS       FINDING RULE
  LIST RULE: FR-DIABETIC DIAGNOSIS// 
  OPERATION: ADD  ADD PATIENT
  SEQUENCE BEGINNING DATE/TIME: 
  SEQUENCE ENDING DATE/TIME: 
Select SEQUENCE: 
Input your edit comments.
Edit? NO//

2f.  The new rule set is now displayed in the Rule Set list view of the Finding Rules.

List Rule Management          Jun 03, 2005@11:09:52          Page:    1 of    1 

 Item  Rule Set Name                                                 Class 1  RS-DIABETIC PATIENTS                                          LOCAL      
    2  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT           NATIONAL   
    3  VA-*IHD QUERI 412 PTS WITH QUALIFY AND ANCHOR VISIT ON LLA M  NATIONAL   
    4  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT               NATIONAL   
    5  VA-*IHD QUERI PTS WITH QUALIFY AND ANCHOR VISIT ON LLA MEDS   NATIONAL   
    6  VA-*IHD QUERI PTS WITH QUALIFY VISIT                          NATIONAL   
    7  VA-*MH QUERI QUALIFYING PC VISIT                              NATIONAL   
    8  VA-*MH QUERY QUALIFYING MH VISIT                              NATIONAL **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CV   Change View                        DR   Display/Edit Rule

CR   Create Rule                        QU   QuitSelect Item: Quit//

**3.  Build the Patient List**

Once the rule set has been created, the patient list can be built via the patient list management option.

3a. Select the Patient List Management option from the Patient List Menu.

Reminder User Patient List    Aug 10, 2005@15:02:21          Page:    1 of    1 Available Patient Lists.
 Item  Reminder Patient List Name                     Created          Patients 
    1  VA-*IHD QUERI 2001 M01 412 PTS WITH QUALIFY A  8/5/05@11:12:16         0 
    2  VA-*IHD QUERI 2001 M01 412 PTS WITH QUALIFY A  8/5/05@11:12:16         0 
    3  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY AND A  8/5/05@11:12:16         0 
    4  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY AND A  8/5/05@11:12:16         0 
    5  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY VISIT  8/5/05@11:12:16         0 
    6  VA-*IHD QUERI 2005 M1 412 PTS WITH QUALIFY AN  8/5/05@11:19:42         0 
    7  VA-*IHD QUERI 2005 M1 412 PTS WITH QUALIFY AN  8/5/05@11:19:43         0 
    8  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY AND AN  8/5/05@11:19:42         0 
    9  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY AND AN  8/5/05@11:19:42         0 
   10  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY VISIT   8/5/05@11:19:42         0 **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   Quit
Select Item: Quit// CR   Create Patient List

3b. Select the CR action to Create the Patient List.

Select PATIENT LIST name: DIABETIC PATIENTS 5Y
  Are you adding 'DIABETIC PATIENTS 5Y' as 
    a new REMINDER PATIENT LIST? No// Y  (Yes)

Secure list?: N// O

Purge Patient List after 5 years?: N// O

Select LIST RULE SET: RS-DIABETIC PATIENTS       RULE SET

Enter Patient List BEGINNING DATE: T-5Y  (AUG 10, 2000)
Enter Patient List ENDING DATE: T  (AUG 10, 2005)

Include deceased patients on the list? N// O

Include test patients on the list? N// O
Queue the  CREATE PATIENT LIST for DIABETIC PATIENTS 5Y: 
Enter the date and time you want the job to start.
It must be on or after 08/10/2005@15:02:49 N
Task number 236638 queued.

**3c. Respond to the prompts** as shown to queue a task job that will create the patient list and add the patient list to the REMINDER PATIENT LIST file. Note that the Patient List Name reflects the date range of 5Y. The Name of the Patient List needs to be as specific as possible to understand which patients are in the list.

**Note:** If the desire is to create a new patient list each month with diabetic patients seen during each month, then Beginning Date and Ending Date would reflect the month period, and the name would include the month and year.

Reminder User Patient List    Aug 10, 2005@15:02:53          Page:    1 of    1 Available Patient Lists. Item  Reminder Patient List Name                     Created          Patients 1  DIABETIC PATIENTS 5Y                           8/10/05@15:02:52        2 
    2  VA-*IHD QUERI 2001 M01 412 PTS WITH QUALIFY A  8/5/05@11:12:16         0 
    3  VA-*IHD QUERI 2001 M01 412 PTS WITH QUALIFY A  8/5/05@11:12:16         0 
    4  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY AND A  8/5/05@11:12:16         0 
    5  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY AND A  8/5/05@11:12:16         0 
    6  VA-*IHD QUERI 2001 M01 PTS WITH QUALIFY VISIT  8/5/05@11:12:16         0 
    7  VA-*IHD QUERI 2005 M1 412 PTS WITH QUALIFY AN  8/5/05@11:19:42         0 
    8  VA-*IHD QUERI 2005 M1 412 PTS WITH QUALIFY AN  8/5/05@11:19:43         0 
    9  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY AND AN  8/5/05@11:19:42         0 
   10  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY AND AN  8/5/05@11:19:42         0 
   11  VA-*IHD QUERI 2005 M1 PTS WITH QUALIFY VISIT   8/5/05@11:19:42         0 **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   QuitSelect Item: Quit//

**3d.  The new Patient List entry is added to the list of patient lists.** When the tasked job has completed successfully, the new Patient List created by the job is displayed in the Reminder User Patient List with the date/time created and the number of patients included in the list.

##### Create Patient List - Expanded example

Reminder User Patient List    Aug 11, 2005@14:22:31                                        Page:    1 of    8 
Available Patient Lists. Item  Reminder Patient List Name                     Created          Patients 1  AGP 1                                          7/10/05@19:55:43       24 
    2  AGP CREATED REMINDER REP                       7/26/05@13:48:23       25 
    3  AGP EXTRACT TEST                                                       0 
    4  AGP IHD EXTRACT WITH QUALIFY VISIT             7/1/05@11:03            0 
    5  AGP IHD QUERI PTS WITH QUALIFY AND ANCHOR VIS  7/1/05@11:03:02         0 
    6  AGP OE/RR TEAM 1                               7/10/05@20:51:42       16 
    7  AGP OERR TEAM LIST                             7/10/05@20:47:17       16 
    8  AGP REMINDER TEST                              7/25/05@11:17:24       25 
    9  AGP REPORT TEST OF PURGE                       7/19/05@16:06:35        3 
   10  AGP T4                                         7/10/05@20:05:02       24 
   11  AGP TEST REMINDER 1                            7/25/05@11:48:36       23 
   12  AGP TEST REMINDERS 2                           7/25/05@12:01:46       47 
   13  FINGERSTICK                                    6/28/05@11:15:35       13 
   14  FINGERSTICK (DEF)                              7/6/05@09:51:42        15 
   15  PJH EXTRACT 2004 M10 BP                        11/2/04@15:58:14        1 
   16  PKR PUB                                        8/9/05@11:33           22 **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   Quit
Select Item: Next Screen// CR   Create Patient List

Select PATIENT LIST name: DIAB PTS W/O DIAB EYE EXAM
  Are you adding 'DIAB PTS W/O DIAB EYE EXAM' as 
    a new REMINDER PATIENT LIST? No// Y  (Yes)

Secure list?: N// O

Purge Patient List after 5 years?: N// O

Select LIST RULE SET: RS-DIAB
     1   RS-DIAB PTS W/O DIAB EYE EXAM       RULE SET
     2   RS-DIABETIC PATIENTS       RULE SET
CHOOSE 1-2: 1  RS-DIAB PTS W/O DIAB EYE EXAM     RULE SET

Enter Patient List BEGINNING DATE: T-5Y  (AUG 11, 2000)
Enter Patient List ENDING DATE: T  (AUG 11, 2005)

Include deceased patients on the list? N// O

Include test patients on the list? N// O
Queue the  CREATE PATIENT LIST for DIAB PTS W/O DIAB EYE EXAM: 
Enter the date and time you want the job to start.
It must be on or after 08/11/2005@14:23:04 N
Task number 237005 queued.

Reminder User Patient List    Aug 11, 2005@14:23:08          Page:    1 of    8 
Available Patient Lists. Item  Reminder Patient List Name                     Created          Patients 1  AGP 1                                          7/10/05@19:55:43       24 
    2  AGP CREATED REMINDER REP                       7/26/05@13:48:23       25 
    3  AGP EXTRACT TEST                                                       0 
    4  AGP IHD EXTRACT WITH QUALIFY VISIT             7/1/05@11:03            0 
    5  AGP IHD QUERI PTS WITH QUALIFY AND ANCHOR VIS  7/1/05@11:03:02         0 
    6  AGP OE/RR TEAM 1                               7/10/05@20:51:42       16 
    7  AGP OERR TEAM LIST                             7/10/05@20:47:17       16 
    8  AGP REMINDER TEST                              7/25/05@11:17:24       25 
    9  AGP REPORT TEST OF PURGE                       7/19/05@16:06:35        3 
   10  AGP T4                                         7/10/05@20:05:02       24 
   11  AGP TEST REMINDER 1                            7/25/05@11:48:36       23 
   12  AGP TEST REMINDERS 2                           7/25/05@12:01:46       47 
   13  DIAB PTS W/O DIAB EYE EXAM                     8/11/05@14:23:08       19 
   14  FINGERSTICK                                    6/28/05@11:15:35       13 
   15  FINGERSTICK (DEF)                              7/6/05@09:51:42        15 **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   Quit

List number 13 is our newly created list and we see that it has 19 patients.

##### Working with Patient Lists

You can work with a patient list by selecting the DSP (Display Patient List) action. Here is an example:

Reminder User Patient List    Sep 29, 2005@10:25:44          Page:  1 of    8 
Available Patient Lists. Item  Reminder Patient List Name                    Created         Patients 6  AGP IHD QUERI PTS WITH QUALIFY AND ANCHOR VIS 7/1/05@11:03:02        0 
    7  AGP OE/RR TEAM 1                              7/10/05@20:51:42       6 
    8  AGP OERR TEAM LIST                            7/10/05@20:47:17      16 
    9  AGP REMINDER TEST                             7/25/05@11:17:24      25 
   10  AGP REPORT TEST OF PURGE                      7/19/05@16:06:35       3 
   11  AGP T4                                        7/10/05@20:05:02      24 
   12  AGP TEST REMINDER 1                           7/25/05@11:48:36      23 
   13  AGP TEST REMINDERS 2                          7/25/05@12:01:46      47 
   14  CRPATIENT                                     8/11/05@14:56:11      14 
   15  CRPATIENT2                                    8/11/05@15:16:44      14 
   16  DIAB PTS W/O DIAB EYE EXAM                    8/11/05@14:23:08      19 
   17  FINGERSTICK                                   6/28/05@11:15:35      13 
   18  FINGERSTICK (DEF)                             7/6/05@09:51:42       15 
   19  PJH EXTRACT 2004 M10 BP                       11/2/04@15:58:14       1 
   20  PKR PUB                                       9/29/05@10:19:51       2 
   21  PKR PVT                                       6/17/05@12:13:15      26 **+ Next Screen   - Prev Screen   ?? More Actions                 &gt;&gt;&gt;** CO   Copy Patient List    DE   Delete Patient List  CV   Change View
COE  Copy to OE/RR Team   DCD  Display Creation Doc LRM  List Rule Management
CR   Create Patient List  DSP  Display Patient List QU   QuitSelect Item: Next Screen// DSP   Display Patient List  
Select (s):  (6-21): 20

Enter DSP, and select the item number next to the patient list you want to view.

Reminder Patient List         Sep 29, 2005@15:08:17          Page:  1 of    1 List Name: PKR PUB (22 patients)
 Created: 09/29/2005@10:19:51           Creator: CRPROVIDER,THREE
 Class: Local                           Type: PUBLIC
 Source: List Rule - RS-DIABETIC PATIENTS

Patient Name                      DFN              PCMM Institution

1  AWHPATIENT,THREE                  40               NONE                  
    2  CRPATIENT,EIGHT                   39               NONE                  
    3  CRPATIENT,FIVE                    24               SALT LAKE CITY        
    4  CRPATIENT,FOUR                    10               NONE                  
    5  CRPATIENT,ONE                  91290               NONE                  
    6  CRPATIENT,SEVEN                   54               NONE                  
    7  CRPATIENT,TEN           912345678906               NONE **+ Next Screen   - Prev Screen   ?? More Actions                        &gt;&gt;&gt;** CV   Change View          DEM  Demographic Report   QU   Quit
HSA  Health Summary All   ED   Edit Patient List
HSI  Health Summary Ind   USR  (View Users)Select Item: Quit//

Notice that this patient list includes a column with PCMM Institution. This information will be included when the rule set includes a list rule with the INSERT FINDING operation and a finding rule based on the reminder term VA-PCMM INSTITUTION or VA-IHD STATION CODE. This list rule should be added as the last step in the sequence of list rules in a rule set to ensure all patients in the final list are associated with a facility.

**List Manager actions on the Reminder Patient List screen**

CV (Change View) – this lets you toggle between a view of the patient list sorted by PCMM Institution and patient name or sorted only by patient name

HSA (Health Summary All) – this lets you run a selected health summary for all the patients on the list

HSI – (Health Summary Ind) this lets you run a selected health summary for selected patients from a patient list.

DEM (Demographic Report) – this lets you run a patient demographic report

ED (Edit Patient List) – if you are the creator of the list you can use this action to edit the name and type of list; if you hold the PXRM MANAGER key you can also edit the creator of the list.

USR (View Users) – this action is applicable only to private lists. If you are the creator of the list or hold the PXRM MANAGER key you can use this action to give other users either view only or full access to the patient list. You can also remove a user’s access to the list.

#### Demographic Report

The Demographic Report can be used for a number of purposes, one of which is to facilitate contacting patients to make sure they receive the proper care. You can get a list of the patients and their phone numbers and addresses. The Demographic Report can produce output in a delimited format so that the information can be imported into another application to create personalized letters. If the output is imported into a spreadsheet, further analysis and sorting can be done.

**Example**

Demographic Report

Reminder Patient List         Feb 22, 2006@18:14:03          Page:    1 of    2

List Name: Diabetic Eye Exam (7 patients)

Created: 08/11/2005@15:16:44           Creator: CRPROVIDER,ONE

Class: Local                           Type: PUB

Source: Reminder Due Report

Patient Name                      DFN

1  AWHPATIENT,THREE                  40

2  CRPATIENT,EIGHT                   39

3  CRPATIENT,FIVE                    24

4  CRPATIENT,FOUR                    10

5  CRPATIENT,ONE                  91290

6  CRPATIENT,SEVEN                   54

7  CRPATIENT,TEN           912345678906

**+         + Next Screen   - Prev Screen   ?? More Actions                    &gt;&gt;&gt;**

CV   Change View           DEM  Demographic Report   QU   Quit

HSA  Health Summary All    ED   Edit Patient List

HSI  Health Summary Ind   USR  (View Users)

Select Item: Next Screen// DEM   Demographic Report

Select the items to include on the report.

Select from the following address items:

1 - CURRENT ADDRESS

2 - PHONE NUMBER

Enter your selection(s):  (1-2): 1

Select from the following future appointment items:

1 - APPOINTMENT DATE

2 - CLINIC

Enter your selection(s):  (1-2): 1-2

Maximum number of appointments to display:  (1-25): 1// 2

Select from the following demographic items:

1 - SSN

2 - DATE OF BIRTH

3 - AGE

4 - SEX

5 - DATE OF DEATH

6 - REMARKS

7 - HISTORIC RACE

8 - RELIGION

9 - MARITAL STATUS

10 - ETHNICITY

11 - RACE

Enter your selection(s):  (1-11): 1-4

Print full SSN: N// O

Include the patient's preferred facility? N// O

Select from the following eligibility items:

1 - PRIMARY ELGIBILITY CODE

2 - PERIOD OF SERVICE

3 - % SERVICE CONNECTED

4 - VETERAN

5 - TYPE

6 - ELIGIBILITY STATUS

7 - CURRENT MEANS TEST

Enter your selection(s):  (1-7):

Select from the following inpatient items:

1 - WARD LOCATION

2 - ROOM-BED

3 - ADMISSION DATE/TIME

4 - ATTENDING PHYSICIAN

Enter your selection(s):  (1-5): 4

Include due status information for the following reminder(s):

1 - Breast Exam

2 - Problem Drinking Screen

3 - Weight and Nutrition Screen

4 - Cholesterol Screen (Male)

5 - Hepatitis C Risk Assessment

6 - Pheumovax

7 - Alcohol Abuse Education

8 - Exercise Education

9 - Advanced Directives Education

10 - Weight

11 - IHD Lipid Profile

12 - MST Screening

13 - Smoking Cessation Education

14 - Diabetic Eye Exam

Enter your selection(s):  (1-14): 30

Delimited Report:? Y// ES

DEVICE: HOME// ;;999  HOME

Patient Demographic Report

Patient List: CRPROVIDER,ONE

Created on Aug 11, 2005@15:16:44

PATIENT^STREET ADDRESS #1^STREET ADDRESS #2^STREET ADDRESS #3^CITY^STATE^ZIP^APP

OINTMENT DATE1^CLINIC1^APPOINTMENT DATE2^CLINIC2^SSN^DOB^AGE^SEX^ATTENDING^REMIN

DER30^STATUS30^DUE DATE30^LAST DONE30^\\

AWHPATIENT,THREE^123 SESAME ST^^^SALT LAKE CITY^UTAH^84101^^^^^0003^JAN 1,

1951^55^FEMALE^WHPROVIDER,THREE^Diabetic Eye Exam^DUE NOW^DUE NOW^unknown^\\

CRPATIENT,EIGHT^^^^^^^^^^^7892^MAY 19,1952^53^FEMALE^^Diabetic Eye Exam^DUE NOW^DUE NO

W^unknown^\\

CRPATIENT,FIVE^^^^^^^^^^^3242^MAR 3,1914^91^MALE^^Diabetic Eye Exam^DUE NOW^DUE N

OW^unknown^\\

CRPATIENT,FOUR^^^^^^^^^^^3242^OCT 23,1927^78^^^Diabetic Eye Exam^DUE NOW^DUE NOW^

unknown^\\

CRPATIENT,ONE^^^^^^^^^^^8828^APR 19,1967^38^MALE^^Diabetic Eye Exam^DUE NOW^DU

E NOW^unknown^\\

CRPATIENT,SEVEN^RON^^^RUBY RIDGE^IDAHO^85098^^^^^1239^MAY 5,1952^53^MALE^^Diabetic

Eye Exam^DUE NOW^3010501^3000500^\\

CRPATIENT,TWO^^^^^^^^^^^3284^APR 4,1914^91^MALE^^Diabetic Eye Exam^DUE NOW^DUE NOW^

unknown^\\

Enter RETURN to continue or '^' to exit:

If the rule set used to create the patient list contains a finding rule and the operation is INSERT then the “CSUB” data for the term’s finding will be available for use with the Demographic Report. This could be used to include lab test results in letters that are sent to patients.

##### Demographic Report /Mail Merge Patient Data

This option can be used to generate letters to send to all patients on a list. Follow the steps below to create personalized letters from the Demographic Report.

**Summary of steps:**

1. Run a demographic report against a patient list.
2. Run the report in a delimited output
3. Capture the output in Notepad
4. Clean up the report output
5. Import the Notepad document into MS Excel
6. Import the Excel document into MS Word

##### Patient Lists Created by Reminders Due Reports

Creation of Patient Lists is not limited to the Patient List Management option.

The Reminders Due Report option on the Reminder Reports menu also provides the ability to save patients evaluated by the Reminders Due Report into a new Patient List that is stored in the Reminder Patient List file.

When you run a Reminders Due Report, you are given the option to save the list of patients to a patient list. Since this requires reminder evaluations for every selected patient, this method of generating a patient list will not be as efficient as generating a patient list from a rule set. Therefore, whenever possible, it is preferable to generate a patient list from a rule set.

Before V.2.0, when you ran a Reminders Due Report, you entered a set of criteria, such as visits to specific locations, which was used to generate a list of patients for which the list of reminders was evaluated. Now an existing patient list can be used directly in a Reminders Due Report, eliminating the requirement to generate the initial list of patients. This lets you target a Reminders Due Report to a very specific cohort of patients. For example, you could create a list of diabetic patients and then run a Reminders Due Report for this list of patients.

##### Patient Lists Created by Reminder Extract Reports

National patient lists created by the Reminder Extract Reporting functionality are named with a prefix of “VA-” or “VA-*”. These patient lists are created when a national Reminder Extract Parameter definition is used to schedule and run a job. Each national extract parameter is set up so that IRM staff can schedule the job once, and then monthly extract reports will automatically be scheduled for the next month when the current months job is completed. This automated feature is only possible if the IRM staff initiates a job for the first month to be reported.

Alternatively, a Clinical Application Coordinator (CAC) can start the job using options available in the Reminder Extract Management (PXRM EXTRACT MANAGEMENT) option.

##### Advantages of Reminder Patient Lists vs Reminder Due Report Lists

The national reminder patient lists don’t need any setup and are created automatically from the national rule sets defined in the extract parameter criteria. When a national patient list is created, it remains on the computer system for five years, and is deleted automatically after 5 years. The national patient list is available to run with health summaries, or for extract validation.

Local patient lists can be generated using the Reminders Due option, where the report criteria specifies date ranges and locations or providers. However, the only output available is the due report (albeit condensed, if required).

The patient list management option provides health summary reporting from existing patient lists.

The patient list management option allows patients to be identified by finding. If you want a list of diabetic patients who smoke, then the patients are extracted directly from the Reminder Index Global rather than by parsing the Visit file. The downside is that list rules and rule sets identifying findings to be collected must be created before a new list can be created. The biggest plus is that since the patient list doesn't involve reminder evaluation, it is quick.

Once a reminder patient list is created, the patient list can be copied to an OE/RR Patient List.

To sum up, the patient list management option provides a way to run health summaries on patient lists, copy them to team lists, and quickly build lists for patients with specific finding combinations.

### Reminder Extract Tools

Clinical Reminders V.2.0 includes extract tools that enable sites to create extract summary reports based on an extract definition. An extract definition defines extract criteria similar to performance measure criteria. The extract definition specifies what patient lists should be created, which reminders should be run against each patient list, and what kind of totals should be accumulated. An extract run uses the extract definition to create extract totals and stores these results in the Reminder Extract Summary file.

The extract tools were developed to meet generic extract report and transmission needs. The tools provide options to:

- Manage extract criteria
- Manage extract runs (manual and automated)
- Manage transmissions to AAC
- View extract reporting results
- View the list of patients making up the patient denominator

The functionality supports corporate level management analysis by providing reports that:

- Summarize patient reminder compliance totals (not applicable, applicable, due, not due), similar to Reminder Due summary reports
- Summarize finding total counts that reflect the most recent findings resulting from reminder evaluation
- Summarize finding total counts that reflect site activities during the reporting month.

#### Reminder Extract Menu

The Reminder Extract Menu was new with Clinical Reminders V2.0. This menu uses List Manager functionality to help reminder managers or clinical application coordinators (CACs) track and manage the national, VISN, and local level extract transmissions.

| Syn   | Option                            | Option Name                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------|-----------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MA    | Reminder Extract Management       | PXRM EXTRACT MANAGEMENT     | This option uses List Manager to view an extract definition, examine and schedule an extract run or transmission run, view extract summary results and view extract patient lists.                                                                                                                                                                                                                                                                                  |
| D     | Extract Definition Management     | PXRM EXTRACT DEFINITION     | This option allows creation/editing of extract definitions for use in extract processing. Each extract definition identifies what list rules should be used to create patient lists, what reminders should be run against each patient list, and what counting rules should be used to count true findings found during reminder evaluation.                                                                                                                        |
| EC    | Extract Counting Rule Management  | PXRM EXTRACT COUNTING RULES | This option allows creation/editing of extract counting rules used in the extract process. The counting rules define how to count the findings  defined in an extract counting group (most recent for each finding, most recent finding in the group, utilization counts for the reporting period).                                                                                                                                                                 |
| EG    | Extract Counting Group Management | PXRM EXTRACT GROUPS         | This option allows creation/editing of extract counting groups. Each group defines reminder terms. Counting groups are used when an extract  definition is defined to accumulate COMPLIANCE and FINDING TOTALS (TYPE OF TOTALS).  The counting groups are used in a counting rule during the extract process to count findings within a group. The reminder term, related counting group, and finding total counts are stored in the Extract Reminder Summary file. |
| LR    | List Rule Management              | PXRM LIST RULE MANAGEMENT   | This option allows creation/editing of list rules which are used to build patient lists.                                                                                                                                                                                                                                                                                                                                                                            |

LR List Rule Management is discussed in detail in the Reminder Patient List/List Rule section.

### Clinical Reminder Extracts Guide

*By REDACTED, Clinical Product Support*

The purpose of this section is to help you learn the mechanics of extracts and how all the pieces fit together to give you the desired results.

What is an extract?

By definition, the word extract simply means to get, pull, or draw out, usually with special effort, skill, or force. Hopefully we will not need the “force” part or maybe we should “use the force” to help us . So, this means that we want to draw out results from VistA by use of our extract definition. Why should we use an extract? One reason is that we are able to get more precise data due to the flexibility that we have with dates inside the extract definition. This allows you to be able to report almost exact results to your management on performance measure data or whatever type of data is expected of you. Reminder reports definitely have their place for reporting data, but the accuracy you can obtain from extracts is more exact.  Another reason is that these can be automatically tasked to run each month, quarter, or year leaving you only to worry about slicing and dicing the data. We will discuss how to do this later on.

#### Key Components

This section of the guide will give us information on all the components that make up an extract definition and how they work together. We will give examples of each one as we complete the components.

Finding Rules

*Finding Rules* – this type of list rule uses a reminder term to achieve the desired result. Let’s look at an example from VistA. You have to use a little forethought when creating a finding rule. It is always best to already have the term that you will use created as you will not be able to create the finding rule without the term embedded. Just like all terms, you may have mapped findings with any number of combinations of beginning date/time(s), ending date/times, or conditions associated with the mapped findings.

The menu option that is used to navigate to creating list rules is as follows:

1. From the Reminder Managers Menu, choose **PL** , then choose **LRM** .
2. This will take you to a window that is very similar to dialogs.
3. When you access these menus, the screen that is displayed is the window that displays all of your rule sets.
4. To change to the window that contains your finding rules, at the “Select Item” prompt, type **CV** for change view (exactly like dialog windows) and press Enter.
5. To access your finding rules, take the default of “F” at the “Type of View” prompt. This will take you to the finding rules. Anytime you want to change from one type of list rule to another, i.e. finding rule to patient list rule, you will use the CV option. This same navigation is used to access the other types of list rules and I will not ask you to have to read this again for each section. Just remember for the next sections how to navigate to the type of list rule you are wanting.
6. After you are in the window you want to be in, choose **CR** to create a new finding rule.

Select FINDING RULE to add: **FR DIABETIC PATIENTS**

Are you adding 'FR DIABETIC PATIENTS' as a new REMINDER LIST RULE (the 344TH)? No// **Y  (Yes)**

Used by: Not used by any rule set

NAME: FR DIABETIC PATIENTS  Replace

SHORT DESCRIPTION:

CLASS: **L  LOCAL**

REMINDER TERM: **TUS DIABETES DIAGNOSIS (Extract)** LOCAL         ...OK? Yes//   (Yes)

*The reminder term must already exist at time of entering into the field.  Cannot be created on the fly.*

LIST RULE BEGINNING DATE/TIME:

LIST RULE ENDING DATE/TIME:

Input your edit comments.     Edit? NO//

Most of the types of findings that can be defined in the reminder term have a Global Index (^PXRMINDX) for across-patient look-ups. However, the Global Index (^PXRMINDX) is not used for computed findings linked to a reminder term, unless the computed finding has hard-coded logic to access the Global Index. The typical computed finding assumes that the patient is already selected and does not support across-patient look-up. However, with V2.0, a computed finding can be specifically created for list-building purposes by defining the Type field in the computed finding definition as “List.” The List type computed finding can be used as the first rule or any subsequent rule in a rule set where the ADD PATIENT Operation is used. When a computed finding is used to SELECT or REMOVE patients from an existing patient list, a “single” or “multiple” type computed finding may be used.

What does all this actually mean to the user?

1. Any type of finding can be used as a mapped item of a term inside of a Finding Rule as the first sequence, except for Computed Findings (CF)
    1. One exception to the above is a CF of a LIST type. LIST type CF’s can only have the ADD PATIENT operator function; therefore, it *can* be used as the first sequence of a rule set.
    2. If you are using a CF in any other sequence than the first, you may use SINGLE, MULTIPLE, or LIST types of CF. Just remember, if you use the LIST type, the operator must be ADD PATIENT. If you use the SINGLE or MULTIPLE as any sequence but the first, you may use any operator. How do I find out what type of CF I have?

A finding rule will evaluate as TRUE if any mapped finding in the reminder term contained within the finding rule is true. If the Finding rule is true, then the logical operator associated with that finding rule will be invoked within the rule set which it is contained in, i.e. ADD PATIENT, SELECT, REMOVE.

<!-- image -->

**Reminder Rules**

*Reminder Rules* – This type of list rule uses an embedded existing reminder definition to achieve the desired results. Some important things to know about a reminder rule.

1. The embedded reminder definition must be an “L” usage type
2. In a reminder rule, *ONLY* the cohort logic is evaluated. If you have resolution logic, it will not be evaluated, but it will not cause problems
3. The cohort string cannot start with a logical “NOT”
4. The cohort string cannot contain a logical “OR NOT”
5. If AGE is used in the cohort logic string, then a baseline age range must be defined
6. If SEX is used in the cohort logic string, the reminder must be sex-specific
7. SEX cannot be the first element of the cohort logic string unless it is followed by AGE
8. If a finding sets the frequency to 0Y, which effectively removes the patient from the cohort, it can’t have an associated age range.

Reminder rules have their place, but they are not used as often as finding rules.

From the List Rule Management options, choose the Change View option ( **CV** ) and then select “ **R** ” for reminder rules, then select **CR** to create a rule

VistA example of creating a reminder rule:

Select REMINDER DEFINITION RULE to add: **RR FLU HIGH RISK**

Are you adding 'RR FLU HIGH RISK' as

a new REMINDER LIST RULE (the 345TH)? No// **Y  (Yes)**

Used by: Not used by any rule set

NAME: RR FLU HIGH RISK//

SHORT DESCRIPTION:

CLASS: L  LOCAL

REMINDER DEFINITION: AM HIGH RISK FLU       LOCAL

LIST RULE ENDING DATE/TIME:

Input your edit comments.

Edit? NO//

Again, the reminder definition AM HIGH RISK FLU must meet all the criteria outlined above for reminder rules for it to function.

The LIST RULE ENDING DATE/TIME field is essentially the evaluation date, similar to using the reminder test option’s evaluation date/time. If you leave this blank, TODAY will be assumed.

To sum all the above up, when using a reminder rule in a rule set as a sequence, the results obtained from the reminder rule will be the cohort logic only of the reminder definition being used. Again, all of the other constraints on reminder rules will apply.

**Patient List Rules**

*Patient List Rules-* Patient list rules are rules that are based on an existing patient list. When using patient list rules in extracts, you can create a patient list rule that will be used by the extract that is based on a patient list that doesn’t exist *yet* , but will exist when the patient list rule is used. We. will cover this idea of using a patient list rule based on a list that doesn’t exist in just a bit.

A patient list can be created three ways:

1. Creating a patient list when running a reminders due report (there is a prompt to create a patient list
2. Creating the patient list from a rule set within a Patient List Management option
3. Creating a patient list when a rule set is invoked within an extract run

From the List Rule Management options, choose the Change View option ( **CV** ) and then select “ **P** ” for reminder rules, then select **CR** to create a rule

Select PATIENT LIST RULE to add: AJM EXTRACT

Are you adding 'AJM EXTRACT' as a new REMINDER LIST RULE (the 417TH)? No// Y

(Yes)

Used by: Not used by any rule set

NAME: AJM EXTRACT//

SHORT DESCRIPTION:

CLASS: L  LOCAL

USE EXISTING PT LIST: AJM EXTRACT LIST

Input your edit comments.

Edit? NO//

As stated above, once a patient list exists, then it may be used as a sequence of a rule set as a patient list rule. Any of the logical operators (mentioned in the Rule Set section) may be used in conjunction with the patient list rule within the rule set.

Let’s now discuss the anomaly of using a patient list that doesn’t exist, but will exist at the time of evaluation. This will only happen when using rule sets within extracts. This is an advanced concept and may take a while to totally grasp….

When a rule set which is composed of finding rules, reminder rules, and patient list rules (not necessarily all of them, but at least one or a combination) is invoked within an extract definition set to run, by design, a patient list will be created. In the example below, you will see the field within the extract sequence that asks the user for the name of the patient list that will be created. Other fields are listed, but disregard these at this point.

Select EXTRACT SEQUENCE: 8// 1       RS NEXUS COHORT (Extract)

EXTRACT SEQUENCE: 1//

LIST RULE SET: RS NEXUS COHORT (Extract)//

EXTRACT PT LIST NAME: NEXUS COHORT Mnn yyyy  Replace

INCLUDE DECEASED PATIENTS: YES//

INCLUDE TEST PATIENTS: NO//

Select REMINDER SEQUENCE:

So, you have the concept that when the extract runs, each sequence within the extract will invoke a rule set and will create a patient list. Let’s say, for example, that sequence one in our hypothetical extract is a rule set to create a Nexus Cohort and sequence two would be to create a diabetic cohort which is a smaller subset of the Nexus Cohort group….again, without understanding what a “Nexus Cohort” is, let’s put this in general terms.

Once the rule set for Nexus Cohort runs and creates a patient list (let’s say that that list has 1500 patients) we would like to use that patient list (1500 patients) as a starting point to create a separate refined list that only contains diabetics, and let’s say that list has 750 patients.

At this point, our cohort would be patients that met the nexus definition AND who are diabetic (750 of 1500 patients). Since extracts process in sequence, our first sequence is to create the nexus cohort (and create a patient list, of 1500 patients, by using a rule set) and then the second sequence would use THAT patient list of 1500 as a starting point to further refine down to the diabetic cohort, 750 of 1500 patients.

The way that this is accomplished is that the second sequence of the extract uses a rule set that starts out using a patient list rule that is based on the patient list created in the first sequence of the extract. In essence, immediately following the creation of the patient list for Nexus Cohort, we use that patient list within a patient list rule to start out creating our diabetic cohort.

Maybe a picture will be worth a thousand words:

Extract Definition

Sequence 1: Nexus Cohort rule set

A patient list of patients is created who meet the criteria of the rules in the rule set

Sequence 2: Diabetic cohort rule set

This rule set begins with a patient list rule that is based on the patient list created from sequence one.

<!-- image -->

**Extract Definition in VistA**

EXTRACT SEQUENCE: 1//

LIST RULE SET: RS NEXUS COHORT (Extract)//   This is the rule set to build nexus cohort

EXTRACT PT LIST NAME: NEXUS COHORT Mnn yyyy  This is the patient list that will be created when the rule set is completed.  Don’t worry about the Mnn yyyy for now.

INCLUDE DECEASED PATIENTS: YES//

INCLUDE TEST PATIENTS: NO//

Select REMINDER SEQUENCE:

Here is the breakdown of the RS NEXUS COHORT (Extract) rule set:

Name:  RS NEXUS COHORT (Extract)

Number:  110

Class:  LOCAL

Description:

Rule Type:  RULE SET

Component Rules

---------------

Sequence: 1

Operation: ADD PATIENT

List Rule: &lt;some list rule&gt;

Sequence: 2

Operation: &lt;some logical operator&gt;

List Rule: &lt;some list rule

Sequence: 3

Operation: &lt;some logical operator&gt;

List Rule: &lt;some list rule&gt;

Next, the second sequence of the extract runs after the first is completed.  Here is the second sequence:

Select EXTRACT SEQUENCE: 2       RS FACILITY DM MEASURES

EXTRACT SEQUENCE: 2//

LIST RULE SET: RS FACILITY DM MEASURES// This is the rule set to build diabetes cohort

EXTRACT PT LIST NAME: FACILITY DM MEASURES Mnn yyyy  This is the patient list that will be created when the rule set is completed.  Again, don’t worry about the Mnn yyyy for now.

INCLUDE DECEASED PATIENTS: NO//

INCLUDE TEST PATIENTS: NO//

Select REMINDER SEQUENCE:

Here is the expansion of the RS FACILITY DM MEASURES rule set:

Name:  RS FACILITY DM MEASURES

Number:  281

Class:  LOCAL

Description:

Rule Type:  RULE SET

Component Rules

---------------

Sequence: 1

Operation: ADD PATIENT

List Rule: PL NEXUS COHORT  Here is the patient list rule that is based on Nexus list created from sequence 1 of the extract

Description:

Rule Type: PATIENT LIST RULE

Use Extract PT List Named: NEXUS COHORT Mnn yyyy Here is the key connection! If you can understand this, you are well on your way to understanding the complete process! In the set-up of the patient list rule, the field USE EXTRACT PT LIST NAMED entry must be the name of the patient list created from sequence 1 of the extract. Look above in that field of extract sequence 1 and see that entry is the same as what you see in the patient list rule EXTRACT PT LIST NAMED field.

Sequence: 2: Whatever happens based on the operator (ADD PATIENT, SELECT, REMOVE) of this sequence will start with the patients that met the NEXUS COHORT (patients who are “in” the nexus list)

Operation: &lt;some logical operator&gt;

List Rule: &lt;Some List Rule&gt;

Sequence: 3

Operation: &lt;some logical operator&gt;

List Rule: &lt;Some List Rule&gt;

Each patient list has a unique name and is stored in file #810.5 (REMINDER PATIENT LIST). These can be overwritten with a subsequent run of an extract or a reminder report.

**Rule Sets**

Rule sets are a sequence of steps that are made up of list rules that are connected together with a logical operator. The three types of list rules are:

1. Finding Rule
2. Reminder Rule
3. Patient List Rule

To create/Edit any of the above, you must be in LIST RULE MANAGEMENT which is a sub menu of PATIENT LIST MANAGEMENT from the main reminders menu. Take a look here and notice all the options you have available at the bottom of the screen.

The types of logical operators that connect each sequence within the rule set are as follows:

1. Add Patient (like the Boolean “OR”)
2. Select (like the Boolean “AND”)
3. Remove (like the Boolean “AND NOT”)

Let’s think about it like a train that is connected together, except that trains usually are not in a logical sequence whereas we hope our rule set is. For this example, we will use generic names for our list rules.

Example: &lt;ADDPATIENT&gt;FINDING RULE 1&lt;SELECT&gt;FINDING RULE 2&lt;REMOVE&gt;REMINDER RULE 1

<!-- image -->

Now let’s use a real-life example to further illustrate a rule set and see what are result is from the rule set.

Finding Rule for Diabetic Patients –FR DIABETES

Finding Rule for A1C Lab test &gt;9.0 – FR HGBA1C&gt;9.0

Finding Rule for age &gt;75 – FR AGE&gt;75

*&lt;ADD PATIENT&gt;* FR DIABETES&lt; *SELECT* &gt;FR HGBA1C&gt;9.0&lt; *REMOVE* &gt;FR AGE&gt;75

<!-- image -->

So, what are the results of this rule set? Diabetic patients who have a lab test of HGBA1C greater than 9.0 and who are 75 years of age or younger. Is that what you came up with? If not, stop a minute and think about the results. The first sequence (FR DIABETES) found our diabetic patients; then from those patients, we used sequence two (FR HGBA1C&gt;9.0) to select (AND) the ones who had a HGBA1C greater than 9.0. Next we used sequence three (FR AGE&gt;75) to remove (AND NOT) patients who were over the age of 75.

**Using Reminders to obtain data in the extract**

So far, all we have from the Extract is nothing but a list of patients. We will continue to use the diabetes example. Our list now contains diabetic patients who have met the Nexus Cohort restrictions. Now what?? This list of patients is the APPLICABLE or our denominator. How do we get our numerator?

To obtain our numerator, we need to run reminder definition(s) against this patient list. To do this, we have to add in reminders to our extract definition. Reminders that already exist can be used for this, but most of the time, you will want to make a copy of an existing reminder and make edits or create a new one from scratch. The main reason to not use an existing reminder is that you will normally not need any cohort logic because your cohort has been built within the rule sets of the extract definition. This makes for faster evaluation of the reminders leading to quicker availability to data. Also, a lot of reminders have a DUE IN ADVANCE TIME FRAME entry and this would affect your data.

Let’s discuss some rules that will apply to the reminders that will be used in the extract.

1. The USAGE filed needs to have an * or an X.
2. Cohort logic must contain something. If your rule set has entirely built your cohort, your reminder still must have something. I would suggest using a customized logic string of SEX
3. All other things about reminders would apply as normal when they are evaluated in the extract

How do I enter the reminder definitions into my extract definitions?

When you go back and edit your extract definition, you choose the appropriate sequence number. For this example, it would be the sequence number dealing with the diabetes section. As you scroll through the fields, you will see a field named ‘Select REMINDER SEQUENCE’. Here you would enter a sequence number, then enter in the .01 name of the reminder definition (not the print name). More than one reminder can be entered for each sequence of the extract definition. You would just need to give each reminder that you add a distinct sequence number. You will notice in the example below that the reminder definition has an (X) at the end. This is actually part of the reminder definition given by the person who created the reminder definition.

Select EXTRACT SEQUENCE: 2       RS FACILITY DM MEASURES

EXTRACT SEQUENCE: 2//

LIST RULE SET: RS FACILITY DM MEASURES//

EXTRACT PT LIST NAME: **FACILITY DM MEASURES Mnn yyyy**

Replace

INCLUDE DECEASED PATIENTS: NO//

INCLUDE TEST PATIENTS: NO//

Select REMINDER SEQUENCE: 145// **100** DM A1C W/I LAST YEAR (X)

REMINDER SEQUENCE: 100//   Reminder Sequence number (arbitrary number)

REMINDER: **DM A1C W/I LAST YEAR (X)** // Reminder definition

COUNTING RULE

Select REMINDER SEQUENCE:

**Dates and how they affect your data**

Remember that the patient lists are created from a rule set. The RULE SET TEST option within LIST RULE MANAGEMENT (specifically within RULE SETS area) is a great tool to let you know what your dates actually will be for your rule set, once it starts running. An example of the RULE SET TEST will be shown later.

There is a logical hierarchy within extracts. Within an extract, there exist many pieces and within these pieces, there are possibilities for date entries along the way. For example:

-Extract runs MUST have a beginning date/time and ending date/time

-A Rule Set has the possibility for entry of a beginning date/time and ending date/time

-A finding rule within a rule set has the possibility for entry of a beginning date/time and ending

date/time

-A reminder term in a finding rule has the possibility for entry of a beginning date/time and ending

date/time

-Within the reminder term, the mapped findings have the possibility for entry of a beginning 
                    date/time and ending date/time

So, if you had different dates in more than one place, which date would be used? The answer to this question is the date at the lowest level would trump a date at a higher level. Some things to think about when adding dates:

1. If you are using a reminder term in an extract, remember if you add dates at the term level or mapped item level within the term, they will also affect how that term is used any other place.
2. If a finding rule has dates, and it is used in more than one rule set, the dates may need to be different in each rule set within which they are used. This is a possible place for errors.
3. My inclination would be to put my dates at the highest level possible unless a piece at a lower level is specific to that one rule set.

Below is an example of using RULE SET TEST option. This example was testing the RS NEXUS COHORT rule set using the month of June. You can see that not all dates are 6/1-6/30. This means that there was a different date entered at a lower level within the rule set.

Enter Patient List BEGINNING DATE: 0601  (JUN 01, 2010)

Enter Patient List ENDING DATE: 0630  (JUN 30, 2010)

List Build Beginning Date: 06/01/2010

List Build Ending Date: 06/30/2010

SEQUENCE 1 FR NEXUS COHORT

Operation: ADD PATIENT

TERM TUS NEXUS CLINIC (Extract)

FINDING 1-RL.NEXUS CLINIC COHORT FY08

Beginning Date/Time: 06/01/2010

Ending Date/Time:    06/30/2010@23:59:59

SEQUENCE 2 FR ANCHOR VISIT

Operation: SELECT

TERM TUS ALL LOCATIONS (Extract)

FINDING 1-RL.VA-ALL LOCATIONS

Beginning Date/Time: 06/01/2008

Ending Date/Time:    05/02/2009@23:59:59

SEQUENCE 3 VA-FR-DATE OF DEATH

Operation: REMOVE

TERM VA-DATE OF DEATH

FINDING 1-CF.VA-DATE OF DEATH

Beginning Date/Time: 0

Ending Date/Time:    05/31/2010@23:59:59

SEQUENCE 4 FR VA VETERAN

Operation: SELECT

TERM TUS VA VETERAN

FINDING 1-CF.VA-VETERAN

Beginning Date/Time: 06/01/2010

Ending Date/Time:    06/30/2010@23:59:59

## Extract Definitions

This section of the guide will help you learn how to set up your extract definition. It is important to have all your pieces ready (rule sets, reminder definitions) to add into your extract definitions. Some good advice would be to create a “map” before you even start building any pieces of the extract, i.e. reminder terms, finding rules, reminder rules, patient list rules, etc.

Once you have your rule sets complete and have tested them to ensure that you will get the proper data returned by the dates you have entered along the way, it is time to add them to your extract definition. You may be creating your extract definition from scratch or you may be editing an already existing definition.  Think about the sequential order that your extract needs to run – which rule set needs to run first. If you have a rule set that depends on something to be created (a patient list) to make it work, then the rule set that creates needs to be prior, sequentially.

**To add a new extract or edit an existing one** :

1. Use the **XM** menu option from the Reminder Managers menu,
2. Choose **ED** option.
3. Choose **CR** or **DE,** depending on what you need to do.

Below is a screen shot from VistA on creating a new extract definition. It includes all the field entries and responses you will need to know about at this time. Also, don’t be concerned at this point about the **Mnn yyyy** that you see below. This will be explained later.

Select EXTRACT DEFINITION to add: **EXTRACT FOR GUIDE**

Are you adding 'EXTRACT FOR GUIDE' as

a new REMINDER EXTRACT DEFINITION (the 20TH)? No// **Y** (Yes)

NAME: EXTRACT FOR GUIDE//

CLASS: **L  LOCAL**

TYPE OF TOTALS: ?

Choose from:

CT       COMPLIANCE TOTALS ONLY

CF       COMPLIANCE AND FINDING TOTALS

TYPE OF TOTALS **: CT  COMPLIANCE TOTALS ONLY**

DESCRIPTION:

No existing text

Edit? NO//

REPORT FREQUENCY: ?

Enter the report frequency.

Choose from:

Q        QUARTERLY

M        MONTHLY

Y        YEARLY

REPORT FREQUENCY: **M  MONTHLY**

Select EXTRACT SEQUENCE: **5  This is an arbitrary number**

Are you adding '5' as a new EXTRACT SEQUENCE (the 1ST for this REMINDER EXTRA

( **Yes)**

EXTRACT SEQUENCE LIST RULE SET: RS NEX

1   RS NEXUS COHORT (Extract)       RULE SET

2   RS NEXUS COHORT (LIST)       RULE SET

3   RS NEXUS IMMUNIZATION REPORT FY08       RULE SET

4   RS NEXUS WITH DM OR IHD AND VETERAN       RULE SET

CHOOSE 1-4: 1 **RS NEXUS COHORT (Extract)** RULE SET

LIST RULE SET: RS NEXUS COHORT (Extract)//

EXTRACT PT LIST NAME: **PATIENT LIST FOR NEXUS COHORT Mnn yyyy**

INCLUDE DECEASED PATIENTS: **n  NO**

INCLUDE TEST PATIENTS **: n  NO**

Select REMINDER SEQUENCE:   No reminder added at this point

Select EXTRACT SEQUENCE: **10**

Are you adding '10' as a new EXTRACT SEQUENCE (the 2ND for this REMINDER EXTR

**(Yes)**

EXTRACT SEQUENCE LIST RULE SET: RS FACILITY

1   RS FACILITY CANCER MEASURES       RULE SET

2   RS FACILITY CANCER MEASURES (Q)       RULE SET

3   RS FACILITY CARDIOVASCULAR MEASURES       RULE SET

4   RS FACILITY CARDIOVASCULAR MEASURES (Q)       RULE SET

5   RS FACILITY DM MEASURES       RULE SET

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **5  RS FACILITY DM MEASURES** RULE SET

LIST RULE SET: RS FACILITY DM MEASURES//

EXTRACT PT LIST NAME: **DIABETIC COHORT Mnn yyyy**

INCLUDE DECEASED PATIENTS **: N** NO

INCLUDE TEST PATIENTS: **N** NO

Select REMINDER SEQUENCE: **5**

Are you adding '5' as a new REMINDER SEQUENCE (the 1ST for this EXTRACT RULES

**(Yes)**

REMINDER SEQUENCE REMINDER: DM

1   DM A1C W/I LAST YEAR (X)       LOCAL

2   DM A1C&lt;7.0 (X)       LOCAL

3   DM A1C&gt;9.0 (X)       LOCAL

4   DM BP &lt;130&amp;&lt;80 (X)       LOCAL

5   DM BP &lt;140&amp;&lt;90 (X)       LOCAL

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 **DM A1C W/I LAST YEAR (X)** LOCAL

REMINDER: DM A1C W/I LAST YEAR (X)//

COUNTING RULE: No entry at this point

Select REMINDER SEQUENCE: **10** arbitrary number

Are you adding '10' as a new REMINDER SEQUENCE (the 2ND for this EXTRACT RULE

**(Yes)**

REMINDER SEQUENCE REMINDER: DM A1C

1   DM A1C W/I LAST YEAR (X)       LOCAL

2   DM A1C&lt;7.0 (X)       LOCAL

3   DM A1C&gt;9.0 (X)       LOCAL

4   DM A1C DONE    ZTUS DM AND A1C DONE (RPT)     LOCAL

5   DM A1C&gt;9.0    HGBA1C&gt;9.0     LOCAL

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **2  DM A1C&lt;7.0 (X)** LOCAL

REMINDER: DM A1C&lt;7.0 (X)//

COUNTING RULE: No entry at this point

Select REMINDER SEQUENCE:

To summarize the extract definition:

1. Extract definition is made up of rule set(s) which are processed in sequence and a patient list is created when each rule set completes. This list of patients makes up your applicable group or denominator for the specific rule set. Another way to say this is that if you have 5 rule sets, you will have 5 patient lists, therefore 5 applicable groups.
2. Reminder definitions can optionally be evaluated against the patient list created from each sequence of the extract definition. Once the reminder definitions are evaluated, the DUE patients make up your numerator.

## Running the Extract

There are two ways to create or start an extract:

1. Manual
2. Automatic

**Manual Method**

This makes the extract start processing the rule sets in the sequence that is contained within the extract definition.

1. Again, you will access the **XM** menu from the reminder managers menu,
2. then choose the **MA** menu option,
3. then choose the **VSE** action. When you choose the **VSE** action, you need to make sure your extract definition appears in the list to be able to choose it. Choose your extract definition, then choose the **ME** action for “manual extract”.

1. At the Select EXTRACT PERIOD (Mnn/yyyy): // prompt, choose your reporting month and year in the syntax of Mnn/yyyy. So, if your reporting month was June of 2010, at the prompt, you would enter M06/2010.

At this point, you may be thinking about the Mnn yyyy in the extract definition. What happens when you choose your month and year for the manual extract to run? Anywhere you have defined Mnn yyyy in the name of the patient lists created from the rule set, M06 2010 will be substituted for the Mnn yyyy. After your extract completes, you can go to the patient list management section of reminders and you will NOT see a list with a literal Mnn yyyy in the name, but you *will* see M06 2010 instead.

Now you just have to let the extract complete. The time it takes will depend on how many rule sets, how many reminders you are evaluating, and the complexity of the reminders.

After the extract completes, if you are a member of your local reminders mail group, you will receive a VistA mail message that the extract is complete.

1. To view your results, access the **XM** menu, the **MA** menu and then choose the **VSE** action. You will see your completed extract on the screen. Choose the number that corresponds to your extract and you will be able to view your results.
2. At the Select Action prompt, take the default of **ES.** You should see data for the reminders that you defined in your extract in the format of TOTAL, APPL., N/A, DUE and NOT DUE.

Below is a screen shot from VistA to demonstrate what you should see.

Extract Summary Name: FACILITY MH PM 2010 M06

Extract Period: 06/01/2010 - 06/30/2010   Created: 07/28/2010@22:49:15

Item  Patient List/Station/Reminder        Total      Appl.    N/A    Due     Not Due

679/DM A1C W/I LAST YEAR                 807      807       0      74        733

679/DM A1C&gt;9.0                           807      807       0      732        75

You may be wondering why there is 0 in the N/A column. This is because we used the rule set for our cohort, not the reminder definition. This is one of the reasons extracts are more efficient because there is less evaluation time due to the fact that everybody on the patient list is in the cohort.

**Automating the extract process**

This will involve your IRM department. They will have to create an option, set that option in TaskMan Management Options and queue it to run monthly. Then in FileMan, your IRM will have to set a field to make sure the correct reporting period is being accessed. We will discuss this in detail below.

Step 1.  Create the new option in VistA. You can give it a unique name to your system.

- Access the XUMAINT option from the programmer prompt or another way would be to access MENU MANAGEMENT option from the EVE menu.
- At the Select Menu Management Option, choose EDIT.

Select Menu Management Option: EDIT options

Select OPTION to edit: **TUS MONTHLY PM** MONTHLY PC PM  unique name for your site, you will be asked to add this as a new option (since my option already existed, I was not prompted to add as new)

NAME: TUS MONTHLY PM//

MENU TEXT: **MONTHLY PC PM** // Choose a name for the MENU TEXT

PACKAGE **: CLINICAL REMINDERS** // Choose CLINICAL REMINDERS as the PACKAGE

OUT OF ORDER MESSAGE:

LOCK:

REVERSE/NEGATIVE LOCK:

DESCRIPTION: enter some descriptive text for this option

This option is for use within Clinical Reminder extracts.  This option is

tasked monthly by taskman utility

Edit? NO//

TYPE: **run routine** //

HEADER:

ENTRY ACTION: D AUTO^PXRMETX("FACILITY MONTHLY PM","Y")

Replace    The yellow highlighted text is the NAME of your extract definition you want to run

EXIT ACTION:

ROUTINE:

CREATOR: CRPROVIDER, ONE// This field will be automatically filled in by the creator

HELP FRAME:

PRIORITY:

Select TIMES PROHIBITED:

Select TIME PERIOD:

RESTRICT DEVICES?:

Select PERMITTED DEVICE:

Step 2:  Go to TaskMan and set this option to run monthly.

- Access the menu option XUTM MGR from the programmer prompt or the TASKMAN MANAGEMENT option from the EVE menu.
- Then choose Schedule/Unschedule Options.

- Select TaskMan Management Option: schedule/Unschedule Options

Select OPTION to schedule or reschedule: tus monthlY PM       MONTHLY PC PM  choose the option created from step 1

...OK? Yes//   (Yes)

(R)

Edit Option Schedule

Option Name: TUS MONTHLY PM

Menu Text: MONTHLY PC PM                             TASK ID: 8824177

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUL 3,2010@03:00    set the date to run after the first of the next  month.  Make sure it doesn’t conflict with any other tasks

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1M     Set the option’s frequency to monthly

TASK PARAMETERS:

SPECIAL QUEUEING:

Step 3: Give FileMan a starting month to start the automatic extract. This will be a one-time entry. Once you create your extract definition, it will be visible in the file.

- From the FileMan Menu, choose “Enter or Edit file entries”
- Choose file #810.2 (REMINDER EXTRACT DEFINITION)
- Then choose your extract definition.
- Then you will need to add an entry to the “NEXT REPORTING PERIOD/YEAR” field. The NEXT REPORTING PERIOD would be the month immediately preceding the month that is defined as your report queue date in TaskMan. For example, if your beginning report queue date in TaskMan is July 3, 2010, your NEXT REPORTING PERIOD would be June 2010 (M06/2010).

Once you have completed steps 1-3, your extract will be set up to automatically run each month, NO MAINTENANCE NECESSARY. You will only need to get the results from the Extract menus, as described above

Even though you have set the extract to run automatically, you can still make manual runs of your extract at any time. Do remember that these can be system-intensive, so take care to run this at off times. If your extract is small, then this will not be an issue.

## Understanding your Output

Now that you have data, what does it all mean? We mentioned earlier about the Applicable number being your denominator and the DUE number being your numerator. Once you have those numbers, it is as simple as doing the math, or having a spreadsheet do the math for you!

So, for an example, let’s say for HGB A1C&gt;9.0 for diabetics performance measure you have 1000 applicable patients from the extract and you have 100 patients that have A1C&gt;9.0 lab value. Then you are 90% compliant on diabetic patients having A1C&lt;9.0.

## FAQ:

1. Q.   How do I know what type of Computed Finding I have, i.e. Single, Multiple or List?
    1. One way is to use the CFL option from the CF management menu option from the Reminder Managers menu. Enter the name of the specific CF and check the TYPE field entry. Another way is to look this up in FileMan from file #811.4 and check the TYPE field entry.
    1. Q.  Reminder rules require the use of a reminder definition which must be “L” type. How do I find out what usage type my reminder definition is?
        1. From the Reminder Managers menu, choose RM, then RI, and look for the entry in the USAGE field.

### Access to National Extracts at Austin Information Technology Center (AITC)

1) Go to REDACTED, which will require you to enter your national access username e.g:

User: VHAXXXXXX\vhaisxxxxx

Password: enter your national password

2) Register for access to Austin system to get customer ID and initial logon password

Go to the Austin Information Technology Center web page.

Select Publications and Forms on the service desk webpage

Under the Forums category: Select VA FORM 9957

## Clinical Reminder Order Checks

Changes with PXRM*2.0*45

The orderable item multiple has been removed in order check groups.

The pharmacy item multiple has been renamed to order check item groups. The patch will automatically add your existing items to the order check item group.

Two new order check types were added

Imaging Type

VA Product

Sites can create their own CPRS Order Checks using Clinical Reminder Definitions or Terms.

Sites will be able to create local order checks using the Clinical Reminder Order Check functionality. These Order Checks will occur at the time the user clicks on the accept button when placing an order in CPRS. The set-up of a Clinical Reminder Order Check consists of two parts:

- Creating an Order Check Item Group that can contain Orderable Items, Imaging types, or entries from the Drug #50, VA Drug Class #50.605, VA Generic #50.6, or VA Product #50.68 files. (For the purpose of this document entries for Drug, VA Drug Class, VA Product, or VA Generic will be referred to as Pharmacy Items).
- Creating the rules that will be applied to the orderable item when accepting an order in CPRS. It is possible to have the same orderable item or pharmacy items in multiple groups. Each rule assigned to the different groups will be evaluated when placing the orderable item in CPRS.

The Order Check Items are stored in file #801. The Order Check Rules are stored in file 801.1.

**When an order is placed in CPRS, the reminder order check will find all order check item groups that contain the orderable item. It will also find all reminder order check item groups that contain a pharmacy item that the orderable item is part of.**

**Note:** Sites should evaluate all requests to create a Clinical Reminder Order Check to determine the importance of adding it. Using many reminders in an order check could affect performance in the order check system.

File #801stores a pointer to an entry in the Orderable Item file (#101.43). The reminder Order Check file **will not** automatically be updated with changes to the Orderable Item file, such as inactivating an existing orderable item, or if an ancillary package adds an item to the Orderable Item file.

The entries in Reminder Order Check Items Group file (#801) need to be evaluated by the site anytime an update is done to the Orderable Item file, file #101.43. The site will need to determine if it needs to remove an orderable item from an existing group or if it needs to add an orderable item to existing group. The pharmacy items assigned to entries in the Reminder Order Item Group file will be automatically evaluated at the time of ordering.

The Reminder Order Check Menu...[ PXRM ORDER CHECK MENU] contains five options:

| Abbr   | Option name                               | File Name                       | Description                                                                                                                                                                              |
|--------|-------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GE     | Add/Edit Reminder Order Check Items Group | PXRM ORDER CHK ITEMS GROUP EDT  | This option is used to create a new order check items group and rules or to edit an existing order check items group and the corresponding rules.                                        |
| GI     | Reminder Order Check Items Inquiry        | PXRM ORDER CHK ITEMS GROUP INQ  | This option is used to display the details of a reminder orderable item group.                                                                                                           |
| RE     | Add/Edit Reminder Order Check Rule        | PXRM ORDER CHECK ITEMS RULE EDT | This option is used to create/edit a reminder order check rule.                                                                                                                          |
| RI     | Reminder Order Check Rule Inquiry         | PXRM ORDER CHECK RULE INQ       | This option is used to display the details of a reminder order check rule.                                                                                                               |
| TEST   | Reminder Order Check Test                 | PXRM ORDER CHECK TESTER         | This option allows the user to run a test against a patient and an orderable item. This allows them to evaluate the results of a reminder order check rule before turning it on in CPRS. |

When entering the editor or the inquiry options, you are presented with options to look up the order check item group or the rules by the name or the components that make up rules or the order check items group:

**For Order Check Items Group**

N:  ORDER CHECK ITEM GROUP NAME

C:  VA DRUG CLASS

D:  DRUG

G:  VA GENERIC

I:   IMAGING TYPE

O:  ORDERABLE ITEM

P: VA PRODUCT

R:  ORDER CHECK RULE

Q:  QUIT

**For Order Check Rules**

N:  ORDER CHECK RULE NAME

R:  REMINDER DEFINITION

T:  REMINDER TERM

Q:  QUIT

**Reminder Order Check Items Group Test [PXRM ORDERABLE ITEM TESTER]**

This option provides a way for the user to test the order check functionality in VistA. The option requires the selection of a patient and either an orderable item or a drug from file 50. This duplicates the process of placing an order in CPRS or finishing a medication in backdoor pharmacy. The output shows the results for all the appropriate reminder rules. In addition, the output shows some internal results that are not displayed in CPRS. The internal results are the evaluation results of a reminder definition or a reminder term. The evaluation result will start with "INTERNAL:". It also specifies if no rules are found for the different values in the testing flag and the severity fields. If a rule is found and it evaluates as false, the TESTER will display “RULE FAILED.”

**Description of the setup fields for Reminder Order Check Items Group:**

- Group Name: This is the name of the Orderable Group
- Description: Sites should use this field to describe the types of Orderable Items that should be defined in this Group.
- Order Check Item Group: This field will allow sites to store a list of orderable items, imaging types, Drug, VA Drug Class, VA Products and/or VA Generic entries. When an order is placed in CPRS, the orderable item will be expanded to determine the drug, drug class, or the generic that it is associated with. If one of these items is found in one or more Order Check Items Groups, then the corresponding rules will be evaluated.
- Each Order Check Items Group can have multiple rules defined.

**Description of the setup fields for Reminder Order Check Rule:**

- Rule Name: This is the internal name of the rule.
- Display Name: This is the external name; the value in this field appears in the order check form in CPRS, if the rule triggers an order check.
- Status Flag: This field determines if the rule is inactive, set for production use, or for testing use. If the rule is set to INACTIVE, then the rule will not be evaluated for the orderable item list. The value should be set to TESTING when a rule is first created so the creator of the rule can test it before turning it on for the entire facility. To turn it on for the entire facility, this field must be set to PRODUCTION.

- CPRS Order Check Flags
    - Clinical Reminder Live: This rule allows all users access to the Clinical Reminder Order Checks.
    - Clinical Reminder Test: This rule should only be assigned to a smaller group of users. This order check rule and the testing field are used to allow the users to test the rule before allowing every user at the site access to the rule
    <!-- image -->

- Severity Flag: This field determines if the rule should require an override reason in the order check dialog. The three options are Low, Medium, and High. A severity of High will require the user enter an override reason for the order check when signing the order.
- Rules can either be defined to run against a reminder term or a reminder definition. A reminder term is beneficial when the request is to evaluate the presence of specific data. (See Example #1). A reminder definition is beneficial if you need the full functionality of a reminder definition to determine if the rule should show in the order check form (See Example #2). The user can only define one or the other. If users define a reminder term, they will be prompted to answer the fields that are for a reminder term. If users do not select a reminder term, they need to select a reminder definition and the associated fields.
- Reminder Term: This is a pointer value to the reminder term.
    - Term Evaluation Status: Reminder Term evaluation results are either True or False. This field lets the user determine if the rule should display in the order check form by selecting which reminder term status should be used.
    - Order Check Text: This is the order check text that will display in CPRS.
- Reminder Definition: This field will show if a reminder term is not defined. This is a pointer to the reminder definition.
    - Definition Evaluation Status: This field determines which reminder evaluation results cause the rule to appear in the order check form. The three possible values are:
        - Due: A selection of DUE will cause the rule to appear in the order check form if the reminder has a status of DUE NOW or DUE SOON.
        - Applicable: A selection of APPLICABLE will cause the rule to appear in the order check form if the reminder has a status of DUE NOW, DUE SOON, or RESOLVED.
        - N/A: A selection of N/A will cause the rule to appear in the order check form if the reminder has a status of N/A or NEVER. This includes CONTRA and REFUSED.

- Output Text: This field controls which text should appear in the order check form. This field can have one of three possible values:
- Definition Text Only: This value will display the text of the reminder evaluation. This text is similar to the Clinical Maintenance Output except it will not include the Status Line and the Frequency line in the output.
- Both Order Check and Definition Text: This value will display the Order Check Text followed by the definition evaluation text.

**Example #1**

***Problem:*** Order Check needed for the interaction between timolol ophthalmic (used to treat glaucoma) and OTC antihistamines (which should not be used in the more rare narrow angle glaucoma).

**Setup:**

1. Create a reminder term that looks for the presence of a diagnosis of narrow angle glaucoma. (May need to look at multiple files depending on your site practice)
2. Create an Order Check Items Group that contains all orderable items for any OTC Antihistamines.
3. Create a Rule that contains the term created in step 1.
4. Set the rule to trigger the order check if the reminder term is evaluated as True.
5. Create the text that should appear in the order check window.

**Example of the Output in CPRS.**

<!-- image -->

**Description of solution** : A reminder term was used in the setup because the presence of Glaucoma was all that is needed to determine if the rule should trigger an order check. In the screen shot above, the text "Diagnosis of Glaucoma" was defined in the Display Name field. The rest of the text was defined in the Order Check Text field.

**Example #2:**

***Problem:*** An Order Check is needed when ordering Glyburide for patients age 65 or greater and serum Cr 2.0 or greater.

**Setup:**

1. Create a reminder definition that is applicable to the patient if the patient’s age is 65 or greater and the patient has a CR serum 2.0 or greater.
2. Create an Order Check Items Group that contains all orderable items for the Glyburide.
3. Create a Rule that contains the definition created in step 1.
4. Set the rule to trigger the order check if the reminder definition is applicable to the patient.
5. Create the text that should appear in the order check window. Set the order text to display the finding output in the order check text.

**Example of the output in CPRS**

<!-- image -->

**Description of solution:** We needed a reminder definition to match patients older than 64 who had a lab test with the results greater than 2. In this example we set the rule up to display both the order check text and the definition evaluation text. The text "Glyburide Contraindicated" is defined in Display Name field. The text "Avoid glyburide in patients with a calculated creatinine clearance &lt; 50 ml/min or a creatinine 2 or greater. If an oral sulfonylurea is required, consider glipizide,” is defined in the order check text field. The rest of the text is returned from the reminder definition evaluation.

**Example #3**

***Problem:***

Order check desired to remind providers that the recommended dose of dabigatran (Pradaxa®) is reduced in the presence of declining renal function.

**Setup:**

1. Create a reminder term that will identify patients with reduced renal clearance. The package insert for Pradaxa ® suggests a threshold of 30 mL/min creatinine clearance, but a serum creatinine level above 2.0 mg/dL approximates the same degree of renal function.

1. Create a reminder order check rule that calls the reminder term created in step 1 when its status is TRUE. The rule also contains the text that will appear in the order check window.

1. Create an order check item group for the dabigatran pharmacy item. You can do this at the VA GENERIC level (e.g., DG.DABIGATRAN) at the DRUG level (e.g., DABIGATRAN 75MG CAP) or at the ORDERABLE ITEM level (e.g., DABIGATRAN CAP, ORAL). Note that even if you use a specific strength at the drug level, all strengths will be order checked because CPRS actually uses the Orderable Item to perform the checks.

1. Connect the rule to the order check item group using the Add/Edit Reminder Order Check Items Group option.

**Example of the Output in CPRS:**

<!-- image -->

**Description of the setup fields for reminder order check rule**

For testing purposes, the status flag needs to be set to T.

| Status   | Result                                                                                                                        |
|----------|-------------------------------------------------------------------------------------------------------------------------------|
| T        | Only Testing order checks display in CPRS and in the testing rules section of the reminder order check test option (VistA)    |
| P        | Only Production order checks display in CPRS and the production rules section of the reminder order check test option (VistA) |
| I        | No order checks display in CPRS or in the testing/ production rules section of the reminder order check test option (VistA)   |

**Reminder Order Check Items Inquiry Example: VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT X)**

Select Reminder Managers Menu Option: ROC  Reminder Order Check Menu

GE     Add/Edit Reminder Order Check Items Group

GI     Reminder Order Check Items Inquiry

RE     Add/Edit Reminder Order Check Rule

RI     Reminder Order Check Rule Inquiry

TEST   Reminder Order Check Test

Select Reminder Order Check Menu Option: GI  Reminder Order Check Items Inquiry

Select Reminder Order Check Items Group by one of the following:

N:  ORDER CHECK ITEMS GROUP NAME

C:  VA DRUG CLASS

D:  DRUG

G:  VA GENERIC

O:  ORDERABLE ITEM

R:  ORDER CHECK RULE

Q:  QUIT

Select Reminder Order Check Items Group by:  (N/C/D/G/O/R/Q): N//   ORDER CHECK ITEM GROUP NAME

Reminder Order Check Item Group: VA

1   VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP

2   VA-TERATOGENIC MEDICATIONS (CAT X) GROUP

CHOOSE 1-2: 2  VA-TERATOGENIC MEDICATIONS (CAT X) GROUP

DEVICE: ;;999  HOME

REMINDER ORDER CHECK RULE INQUIRY          Jan 05, 2012 10:18:38 am  Page 1

-----------------------------------------------------------------------------

VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT X)                   No. 6

-----------------------------------------------------------------------------

Display Name:           Potentially Teratogenic Medication (FDA Category X)

Class:                  NATIONAL

Sponsor:

Review Date:

Description: Teratogenic Medications Order Check - Category X Meds

Due for: women of childbearing age (12-50) Exclusions: documented

hysterectomy, documented placement of IUD more recent than documented

removal of IUD

Reminder Term:

Term Evaluation Status:

Reminder Definition     VA-TERATOGENIC MEDICATIONS ORDER CHECK

Reminder Evaluation Status:

APPLICABLE

Output Text:            BOTH ORDER CHECK AND DEFINITION TEXT

Order Check Text

The ordered medication is in FDA pregnancy category X.

1) Pregnancy must be excluded prior to receiving the medication

2) The patient must be provided contraceptive counseling on potential risk

vs. benefit of taking this medication if she were to become pregnant.

**Reminder Order Check Items Inquiry Example: VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP**

REMINDER ORDER CHECK ITEMS GROUP INQUIRY     Feb 02, 2012 10:11:31 am  Page 1

-----------------------------------------------------------------------------

VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP                    No. 8

-----------------------------------------------------------------------------

Class:                  NATIONAL

Sponsor:

Review Date:

Group Description:

Pharmacy Item List:

DG.ACETAMINOPHEN/BUTALBITAL

.

.

Orderable Item List:

Reminder Rule List:

Rule Name: VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D)

Display Name: Potentially Teratogenic Medication (FDA Category D or C)

Class: National

Sponsor:

Review Date:

Active Flag: Yes

Testing Flag: Yes

Severity: Medium

Reminder Definition: VA-TERATOGENIC MEDICATIONS ORDER CHECK

Definition Status: Applicable

Output Text: Both Order Check and Definition Text

Order Check Text:

Concern has been raised about use of this medication

during pregnancy.

1) Pregnancy status should be determined. Discuss

use of this medication on the context of risks to

the mother and child of untreated disease. Potential

benefits may warrant use of the drug in pregnant

women despite risks.

2) The patient must be provided contraceptive

counseling on potential risk vs. benefit of taking

this medication if she were to become pregnant.

Rule Description:

Teratogenic Medications Order Check - Category D and

selected C Meds

Due for: women of childbearing age (12-50)

Exclusions: documented hysterectomy, documented

placement of IUD more recent than documented removal

of IUD

Select Reminder Order Check Items Group by one of the following:

N:  ORDER CHECK ITEMS GROUP NAME

C:  VA DRUG CLASS

D:  DRUG

G:  VA GENERIC

O:  ORDERABLE ITEM

R:  ORDER CHECK RULE

Q:  QUIT

## Appendix A: Glossary

### Acronyms

| AITC       | Austin Information Technology Center (formerly AAC - Austin Automation Center)   |
|------------|----------------------------------------------------------------------------------|
| AIMS       | Abnormal Involuntary Movement Sca                                                |
| API        | Application Programmer Interface                                                 |
| CAC        | Clinical Application Coordinator                                                 |
| CDCO       | Corporate Data Center Operations                                                 |
| CNBD       | Cannot be Determined (frequency)                                                 |
| CPRS       | Computerized Patient Record System                                               |
| CSV        | CSV is the file extension for a Comma-separated data value file                  |
| DBIA       | Database Integration Agreement                                                   |
| EPRP       | External Peer Review Program                                                     |
| GUI        | Graphical User Interface                                                         |
| HSR&D      | Health Services Research and Development                                         |
| HL7        | Health Level 7                                                                   |
| HRMHP      | High Risk Mental Health Patient                                                  |
| ICD-9, CM  | International Classification of Disease, 9  th  Edition, Clinical Modifications  |
| ICD-10, CM | International Classification of Disease, 10  th  Edition, Clinical Modifications |
| IHD        | Ischemic Heart Disease                                                           |
| IVMH       | Improve Veterans Mental Health                                                   |
| MDD        | Major Depressive Disorder                                                        |
| MHTC       | Mental Health Treatment Coordinator                                              |
| NLM        | National Library of Medicine                                                     |
| OEF/OIF    | Operation Enduring Freedom/Operation Iraqi Freedom                               |
| OQP        | Office of Quality and Performance                                                |
| PD         | Product Development                                                              |
| QUERI      | Quality Enhancement Research Initiative                                          |
| SAS        | Statistical Analysis System                                                      |
| SRS        | Software Requirements Specification                                              |
| VHA        | Veterans Health Administration                                                   |
| VIMM       | VistA Immunization Enhancements                                                  |
| VISN       | Veterans Integrated Service Networks                                             |
| VistA      | Veterans Health Information System and Technology Architecture                   |

### Definitions

| **Term**                | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Applicable              | A reminder is applicable when the Patient Cohort Logic is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Boolean Logic Operators | Boolean operators are used to write logic strings such as CUSTOMIZED COHORT LOGIC. The operators are: ! (OR), & (AND), !’ (OR NOT), and &’ (AND NOT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CNBD                    | Reminder evaluation status of Cannot Be Determined. If a frequency can’t be determined for a patient, the Status and Due Date will both be CNBD and the frequency display that follows the status line will be “Frequency: Cannot be determined for this patient.” When reminder evaluation is disabled the status will be CNBD.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Clinical Reminder       | A clinical reminder is a software decision support tool that defines who the reminder applies to: cohort logic, and what resolves the reminder: resolution logic, for a given clinical activity. The logic uses VistA patient data including the presence or absence of specified criteria such as diagnoses, procedures, health factors, medications, or demographic variables (e.g., age, gender).  A reminder may or may not require provider resolution, depending on its purpose and design, through a user interface, also known as a reminder dialog.  Also, in accordance with the underlying logic, reminders may be used to collect specified patient information that may or may not be related to the dialog.                                                                                                                                                                                                   |
| Cohort                  | Patient Cohort  A group of patients that meet the defined criteria (Patient Cohort Logic) for a reminder. In other words, if the reminder is applicable, the patient is in the cohort.  Patient Cohort Logic  This is the logic that specifies how findings are used to select the applicable patient population; i.e., the patient cohort. It is based on MUMPS Boolean operators and their negations. The operators are: ! (OR), &amp; (AND),  !’ (OR NOT), and &amp;’ (AND NOT).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Component               | A component represents the module that is presented in any given template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Computed Findings       | A custom MUMPS routine used to find some specific patient characteristic.  Computed findings are used when none of the standard findings will work. Sites can create their own computed findings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CSUB                    | CSUB values are used in the CONDITION field to do a comparison to numeric or string values. Using +V causes the CSUB data to be interpreted as numeric. Strings that cannot be converted to a number are set to zero. For example, a CONDITION such as I +V("CHECK-OUT DATE/TIME")&gt;0 would be true if the appointment had a check-out date/time.  When a Reminder Test is run, some elements of the FIEVAL array will have a “CSUB” subscript. Example for an orderable item finding:  FIEVAL(5,"CSUB","DURATION")=1774  FIEVAL(5,"CSUB","ORDER")=3366^CA ULTRA^546;99RAP  FIEVAL(5,"CSUB","RELEASE DATE")=3010917.1625  FIEVAL(5,"CSUB","START DATE")=3010917  FIEVAL(5,"CSUB","STATUS")=PENDING  FIEVAL(5,"CSUB","STOP DATE")=  FIEVAL(5,"CSUB","VALUE")=PENDING  Each of the subscripts following “CSUB” may be used in a Condition (hence the abbreviation Condition SUBscript); for example:  I V(“DURATION”)&gt;90 |
| Dialog Element          | A dialog element is defined primarily to represent sentences to display in the CPRS window with a check-box. When the user checks the sentence off, the FINDING ITEM in the dialog element and the ADDITIONAL FINDINGS will be added to the list of PCE updates, orders, Mental Health Notification Purposes, and mental health tests. The updates won't occur on the CPRS GUI until the user clicks on the FINISH button. Dialog elements may have components added to them. Auto-generated components will be based on the additional prompts defined in the Finding Type Parameters. Once a dialog element is auto-generated, the sites can modify them. Dialog elements may also be instructional text or a header. The FINDING ITEM and components would not be defined in dialog elements.                                                                                                                            |
| Dialog Group            | A dialog group is similar to menu options. It groups dialog elements and dialog groups within its component. The dialog group can be defined with a finding item and a check-box. The components in the group can be hidden from the CPRS GUI window until the dialog group is checked off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Due                     | A reminder is DUE for a patient if the patient is in the cohort, and has not yet had the treatment, medication, education, etc., or if the last time the reminder was resolved has exceed the frequency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Finding Item            | A Finding Item is a piece of patient data that can be searched for by the reminder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Function Findings       | Function Findings (FF) do computations on the results from regular findings. Function Findings can be used just like regular findings with one exception, there is no date associated with an FF, which means the Resolution Logic cannot be written so that it is made true solely by FFs. Besides providing new and expanded functionality, FFs can make custom logic much simpler to understand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Health Factors          | A health factor is a computerized component that captures patient information for which no standard code exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Mental Health Assistant | The Mental Health Assistant is a national VA software package that is used for administration and scoring of standardized of both self-reported and professionally administered questionnaires and tests. It is integrated with clinical reminders in that some mental health assistant instruments can be administered through a reminder dialog. Also the results of a specific instrument overall score, scale score, or specific item response can be used as a finding in reminder logic. This is the mechanism, for presenting questionnaires for screening for common mental health issues such as the AUDIT-C for alcohol misuse.                                                                                                                                                                                                                                                                                   |
| Prompt                  | An aid on the screen in the form of a question or statement indicating the options available. Prompts are defined for PCE, MH Notification Purpose, or as locally created comment check-boxes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PXRM                    | Clinical Reminder package namespace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Reminder Component      | A reminder component is any element, or part thereof, of a reminder, including the reminder’s definitions, dialogs, findings, terms, cohort logic or resolution logic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Reminder Definition     | The reminder definition is the internal logic of the reminder. It describes the patients the reminder applies to, how often it is given, and what resolves or satisfies the reminder. It is comprised of the predefined set of finding items used to identify patient cohorts and reminder resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Reminder Dialog         | The reminder dialog is the display, which is seen by the user in the CPRS Graphical User Interface (GUI), when opening a reminder. Reminder dialogs are used in CPRS to allow clinicians to select actions that satisfy or resolve reminders for a patient. Information entered through reminder dialogs updates progress notes, places orders, and updates other data in the patient’s medical record. A reminder dialog is created by the assembly of components in groups into an orderly display.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Reminder Exchange       | The Clinical Reminders Exchange Utility provides a mechanism for sharing entries from any the the Clinical Reminders files including reminder definitions and dialogs among sites throughout the VA or among sites within a VISN. Exchanging reminders helps to simplify reminder and dialog creation. It also helps to promote standardization of reminders based on local, VISN-wide, and national guidelines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Reminder Extracts       | This Clinical Reminders application provides extract tools that enable sites to create extract summary reports based on an extract definition. An extract definition defines extract criteria similar to performance measure criteria. The extract definition specifies what patient lists should be created, which reminders should be run against each patient list, and what kind of totals should be accumulated. An extract run uses the extract definition to create extract totals and stores these results in the Reminder Extract Summary file.                                                                                                                                                                                                                                                                                                                                                                    |
| Reminder Finding        | A reminder finding is a data element in the Veterans Health Information and Technology Architecture (VistA). Findings include data elements in files such as the files for Drugs, Education Topics, Exams, Health Factors, Immunizations, Laboratory Tests, Mental Health Instruments, Orderable Items, Radiology Procedures, Reminder Computed Findings, Reminder Taxonomies, Reminder Terms, Skin Tests, VA Drug Class, VA Generic, and Vital Measurements.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Reminder Location List  | Location Lists provide a way to give a name to a list of locations.  A Location List is built from two types of entries: Hospital Location, file #44 and Clinic Stop, file #40.7. There is a multiple for Hospital Locations and a multiple for Clinic Stops in the Location List file, so when you build a list of locations, you can use Hospital Locations and/or Clinic Stops.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Reminder Patient List   | A list of patients that is created from a set of List Rules and/or as a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.                                                                                                                                                                                                                                                                                                                                                         |
| Reminder Term           | A reminder term is a finding item that groups other findings. They can be used to map local findings to national findings, providing a method to standardize these findings for national use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Reminder Test           | The Reminder Test option provides a convenient tool that can be used as an aid in setting up and testing new reminders and tracking down problems with existing ones. It lets you evaluate a reminder without going through CPRS or Health Summary. Reminder Test now allows a Browser view, which improves some viewing of details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Resolution              | A reminder is considered RESOLVED (or SATISFIED) if the conditions defined by the reminder resolution logic have been met. For example, if a reminder exists for influenza immunization, giving a flu vaccine satisfies or resolves that reminder. Likewise, ordering lab tests or drugs or giving patient education can resolve a reminder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Result Element          | A result element contains special logic that uses information entered during the resolution process to create a sentence to add to the progress note. The special logic contains a CONDITION that, when true, will use the ALTERNATE PROGRESS NOTE TEXT field to update the progress note. A separate result element is used for each separate sentence needed. The result element is only used with mental health test finding items. Default result elements are distributed for common mental health tests, prefixed with PXRM and the mental health test name. Sites may copy them and modify their local versions as needed.                                                                                                                                                                                                                                                                                           |
| Result Group            | A result group contains all of the result elements that need to be checked to create sentences for one mental health test finding. The dialog element for the test will have its RESULT GROUP/ELEMENT field defined with the result group. Default result groups for mental health tests are distributed with the Clinical Reminders package. Sites may copy them and modify their local versions as needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TIU                     | Text Integration Utilities (TIU) simplifies the access and use of clinical documents for both clinical and administrative VAMC personnel, by standardizing the way clinical documents are managed.  TIU accepts document input from a variety of data capture methodologies. Those initially supported are transcription and direct entry. TIU allows upload of ASCII formatted documents into VistA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Appendix B: Clinical Reminder Order Checks Example

**NOTE** : PXRM*2*22 changed the method for creating Order Checks, by using ScreenMan functionality. For those not familiar with ScreenMan, a brief overview follows.

**ScreenMan Overview**

The redesigned Reminder Order Check functionality uses ScreenMan. ScreenMan is VA FileMan's *screen-oriented* data entry tool. It is an alternative to the Scrolling Mode approach. With ScreenMan, data is entered in *forms* . Each form field occupies a fixed position on the screen (instead of scrolling off!). You can see many data fields at once, and use simple key combinations to edit data and move from field to field on a screen. You can also move from one screen to another like turning through the pages of a book. ***For a detailed explanation of using ScreenMan, please refer to the VW FileMan Getting Started manual.***

**Example of a ScreenMan Screen**

<!-- image -->

**ScreenMan Descriptions**

<!-- image -->

Fields are usually composed of a *data element* and a *caption* . ScreenMan displays data elements in high intensity (boldface) and other text in regular intensity. Text that identifies a data element is called a *caption* and is usually followed by a colon ( **:** ). A caption and its associated data element are together called a *field* . Captions of *required* fields are underlined; to save any changes you make on the form, required fields *must* contain data.

**How to Navigate Between Fields and Pages**

There are a number of ways you can move the cursor from field to field on a form (i.e., navigate). This is to provide you with as much flexibility as possible so that you can work quickly and efficiently with forms.

You can use the keystrokes listed in the following table to move the cursor to various fields located on a ScreenMan form:

| To                                                       | Press                                             |
|----------------------------------------------------------|---------------------------------------------------|
| Move to the next field (to right or below).              | <Tab>                                             |
| Move to the previous field (to left or above).           | <PF4>                                             |
| Move to the field above.                                 | <ArrowUp>                                         |
| Move to the field below.                                 | <ArrowDown>                                       |
| Move to the next field in the pre-defined edit sequence. | <Enter>                                           |
| Edit a WORD-PROCESSING field.                            | At field, press <Enter>                           |
| Select a Subrecord in a Multiple.                        | At field, press <Enter>                           |
| Move to the next block on current page.                  | <PF1><PF4>                                        |
| Jump to a specific field.                                | ^ followed by Caption of field and <Enter>        |
| Jump to the Command Line.                                | ^<Enter>                                          |
| Move to next page                                        | &lt;PF1&gt;&lt;ArrowDown&gt; or  &lt;PageDown&gt; |
| Move to previous page                                    | &lt;PF1&gt;&lt;ArrowUp&gt; or  &lt;PageUp&gt;     |
| Move to a page you specify                               | <PF1>P                                            |

**Saving and Exiting**

To SAVE or EXIT the form, you need to reach ScreenMan's command line. It's reachable from any ScreenMan screen. To reach the command line, do any one of the following:

1. Enter a caret ("^") at any field prompt.
2. Press **&lt;Enter&gt;** , **&lt;Tab&gt;** , or **&lt;PF4&gt;** to move from field to field until you reach the command line.
3. Press **&lt;ArrowDown&gt;** or **&lt;ArrowUp&gt;** to move the cursor from field to field downwards or upwards, until you reach the command line.

Then you can enter SAVE or EXIT at the command line (see below).

Some very useful shortcuts are:

Pressing Num Lock then C will close a screen.

Pressing Num Lock then E will save and exit.

Pressing Num Lock then Q will quit, no changes are saved.

Note that &lt;PF1&gt;  means press Num Lock.

**Word-Processing Fields**

To edit or display a WORD-PROCESSING field, press the Enter/Return key at the WORD-PROCESSING field. This clears the screen and passes control to your Preferred Editor to edit the field. If you do not have a Preferred Editor, the Screen Editor is used. When you exit the editor, you return to the ScreenMan screen.

**Multiples Linked to "Pop-Up" Subpages**

A Multiple field can appear on a page and be linked to a regular or "pop-up" subpage. When you navigate to the Multiple field, select a Subrecord, and press the Enter/Return key, you are taken to the subpage, which contains the fields within the Multiple.

In the following illustration, the Multiple is the field with the caption "Select EMPLOYMENT HISTORY:". When you enter "FEB 1,1950" at this field, you are taken into a "pop-up" subpage, where you can edit the fields for that particular Subrecord:

### Exiting a Subpage

While in a subpage, your only Command Line options are CLOSE and REFRESH. You cannot EXIT, Quit, or SAVE until you return to the parent page. You can return to the parent page by pressing **&lt;PF1&gt;C** or issuing the CLOSE command at the Command Line. From there, you can select another Subrecord to edit or navigate to another field.

### Order Check Example

**Purpose** : Design an Order Check for dabigatran (Pradaxa®) to remind providers about dose reduction when creatinine clearance is less than 30 mL/min

This example uses serum creatinine values greater than 2 mg/dL to focus more on the order check than on the lab result

1. **Create a reminder term that will identify patients with reduced renal clearance. (Patients with Cr &gt; 2 mg/dL)**

Select Reminder Term Management Option: **TE** Add/Edit Reminder Term

Select Reminder Term: **ZZ CREATININE &gt; 2 (TERM)**

Are you adding 'ZZ CREATININE &gt; 2 (TERM)' as

a new REMINDER TERM (the 1215TH)? No// **Y** (Yes)

REMINDER TERM CLASS: **L** LOCAL

NAME: ZZ CREATININE &gt; 2 (TERM)  Replace

CLASS: LOCAL//

Reminder Term has no findings!

Select Finding: **LT. CREATININE**

Are you adding ' CREATININE' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// **Y** (Yes)

Editing Finding Number: 1

FINDING ITEM:  CREATININE//

CONDITION: **I V&gt;2**

1. **Create a reminder order check rule that calls the reminder term created in step 1 when its status is TRUE.  The rule also contains the text that will appear in the order check window.**
    - Each RULE exists as a part of the OI Group
    - That allows you to set up multiple rules that apply to the same list of drugsSelect Reminder Managers Menu Option: **ROC** Reminder Order Check MenuSelect Reminder Order Check Menu Option: **RE** Add/Edit Reminder Order Check Rule
Select Reminder Order Check Items Group by one of the following:
N:  ORDER CHECK ITEMS GROUP NAME
C:  VA DRUG CLASS
D:  DRUG
G:  VA GENERIC
O:  ORDERABLE ITEM
R:  ORDER CHECK RULE
Q:  QUITSelect Reminder Order Check Items Group by:  (N/C/D/G/O/R/Q): N// **R** ORDER CHECK RULESelect REMINDER ORDER CHECK RULES RULE NAME: **DABIGATRAN AND RENAL FUNCTION**
Are you adding 'DABIGATRAN AND RENAL FUNCTION' asa new REMINDER ORDER CHECK RULES (the 4TH)? No// **Y** (Yes)RULE NAME: DABIGATRAN AND RENAL FUNCTIONDISPLAY NAME : **DABIGATRAN AND RENAL FUNCTION**ACTIVE FLAG : **YES**TESTING FLAG : **YES**SEVERITY : **MEDIUM**TERM : **&lt;Enter&gt;**
**When you press Enter after Term:, a box pops up and prompts you for the Term name and Term Evaluation Status.**REMINDER TERM: ZZ CREATININE &gt; 2 (TERM)TERM EVALUATION STATUS: **TRUE** .
**Either a Term or a Definition must be defined; if you don’t enter a Term, the prompt appears for DEFINITION.**DEFINITION **&lt;Enter&gt;**
REMINDER DEFINITION:                                                     DEFINITION EVALUATION STATUS:                                            OUTPUT TEXT:
**When you press Enter after Term:, a box pops up and prompts you for the Term name**
ORDER CHECK TEXT:
**Order Check Text and Rule Description are word-processing fields. When you press Enter, a word-processing screen opens up.**
==[ WRAP ]==[ INSERT ]======&lt; ORDER CHECK TEXT &gt;========[ &lt;PF1&gt;H=Help ]
The dose of dabigatran should be reduced to 75mg PO BID when the
patient's creatinine clearance is estimated to be less than
30 mL/min.
&lt;=====T=======T====T======T=======T=======T=======T=======T=======T&gt;===
RULE DESCRIPTION: &lt;Enter&gt;RULE NAME : **DABIGATRAN AND RENAL FUNCTION**DISPLAY NAME : **DABIGATRAN AND RENAL FUNCTION**ACTIVE FLAG : **YES**TESTING FLAG : **YES**SEVERITY : **MEDIUM**TERM: ZZ **CREATININE &gt; 2 (TERM)**TERM EVALUATION STATUS: TRUE
ORDER CHECK TEXT: The dose of dabigatran should be reduced to 75mg PO BID wh ...
RULE DESCRIPTION:CLASS : **LOCAL**
**SPONSOR:**
**REVIEW DATE:**
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Exit     Save     Refresh
Enter a command or '^' followed by a caption to jump to a specific field.
COMMAND:                              Press &lt;PF1&gt;H for help    Insert
    1. **Create an Order Check Item Group**
Got to here Similar ScreenMan actions and word-processing fields shown in the example above apply in this option.
Select Reminder Managers Menu Option: ROC  Reminder Order Check Menu
Select Reminder Order Check Menu Option: GE  Add/Edit
Reminder Order Check Items GroupSelect reminder order check items group by:  (N/C/D/G/O/R/Q): N// &lt;Enter&gt;
ORDER CHECK ITEM GROUP NAME
Reminder Order Check Item Group: DABIGATRAN AND RENAL FUNCTION
Are you adding 'DABIGATRAN RENAL FUNCTION' as
a new REMINDER ORDER CHECK ITEMS GROUP (the 4TH)? No// Y  (Yes)
-- ORDER CHECK ITEM LIST --------------------------------------------------------
. DR.DABIGATRAN ETEXILATE 150MG ORAL CAP               Word-
processing field                 .
-----------------------------------------------------------------------
Word-processing
field
--REMINDER ORDER CHECK RULE--------------------------------------------
. DABIGATRAN AND RENAL FUNCTION                                           .
-----------------------------------------------------------------------
GROUP NAME: DABIGATRAN
ORDER CHECK ITEM LIST (0 entry)
REMINDER ORDER CHECKS RULES LIST (1 entry)
CLASS: LOCAL
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Select reminder order check items group by:  (N/C/D/G/O/R/Q): N// QUIT
    1. **Connect the rule to the order check item group using the Add/Edit Reminder Order Check Items Group option.**
    1. **In CPRS, turn off the Clinical Reminders Live Order Check.**
<!-- image -->
    - Set the rule’s testing flag to True.
    - Set the group’s Active Flag to True.
    - Run the Reminder Order Check Test option to validate that the active rule shows for each patient.
    - In CPRS, place a corresponding order for the order group for each test patient.
        - Validate that only the active rule shows in the order check form.
    **Result**
    <!-- image -->

<!-- image -->

## Appendix C: Measurements

A measurement consists of two parts, a number and units. Patch PX*1*211 added measurement definition fields to Education Topics, Exams, and Health Factors. Patch PX*1*217 added additional fields that facilitate storing and displaying measurements. When a measurement is recorded in a V-file, the number is stored in the MAGNITUDE field and the unit is stored in the UCUM CODE field. The measurement definition fields are:

**MINIMUM VALUE** – When a measurement is defined, MINIMUM VALUE and MAXIMUM VALUE sets                                 the inclusive range for the magnitude.

**MAXIMUM VALUE** - When a measurement is defined, MINIMUM VALUE and MAXIMUM VALUE sets                                 the inclusive range for the magnitude.

**MAXIMUM DECIMALS** - The maximum number of decimal digits that can be entered for the magnitude.

**UCUM CODE** – This is the unit for the measurement, it is selected from the Universal Code for                               Units of Measurement (UCUM) file #757.5. From the UCUM website:

"The Unified Code for Units of Measure (UCUM) is a code system intended to include all units of measures being contemporarily used in international science, engineering, and business. The purpose is to facilitate unambiguous electronic communication of quantities together with their units. The focus is on electronic communication, as opposed to communication between humans. A typical application of The Unified Code for Units of Measure are electronic data interchange (EDI) protocols, but there is nothing that prevents it from being used in other types of machine communication."

Because UCUM is an international standard, using it facilitates interoperability of measurement data.

**PROMPT CAPTION** - This field stores the prompt that displays in CPRS Reminder Dialogs when the Education Topic, Exam, Health Factor, or Reminder Taxonomy is used as a finding item.

**UCUM DISPLAY** - This field specifies how the unit is presented when a measurement is displayed in                                CPRS, Clinical Reminders, and Health Summary. When the value is C, the UCUM Code is displayed                                when the value is D, the Description is  displayed. When the value is N, no units are displayed. When you are setting UCUM DISPLAY, typing a “?”, will list the UCUM code and description to help you decide which to use.

When defining a measurement, all of these fields must be set.

Patch PX*1*211 added the fields MAGNITUDE and UCUM CODE to the V Exam, V Health Factors, and V Patient Ed files. When a measurement is recorded that is where it is stored. If a measurement has been recorded in one of these V-files, it will be returned as a CSUB named “MEASUREMENT”. The first ^ separated piece is the magnitude and the second piece is the pointer to the UCUM Codes file #757.5.

As of CPRS v 32B, measurements can be entered through Reminder Dialogs and Encounter Forms. They can also be entered using the PCE List Manager interface in VistA. When a user enters a measurement, the only field they enter is magnitude and the value they enter must be in the inclusive range defined by minimum value and maximum value, with no more decimal digits than maximum decimals. The unit is set automatically to the UCUM code in the definition.

## Appendix D: Contraindications, Precautions, and Refusals

**Introduction**

When a reminder definition containing immunization findings is evaluated, the VIMM CONTRA/REFUSAL EVENTS file, #9000010.707, is automatically queried for active contraindications, refusals, and precautions (C/R), for each immunization finding in the definition.

Possible active C/R statuses for an immunization finding are CONTRA, PRECAUTION, and REFUSED. A C/R is active until its WARN UNTIL DATE has been passed. If there is no WARN UNTIL DATE, the C/R is permanent. For computational purposes, the WARN UNTIL DATE of permanent C/Rs is represented as a 0.

For terms mapped to immunization findings:

- If at least one of the mapped findings does not have an active C/R, the term will not have a C/R status.
- If all the mapped findings have an active contraindication, the C/R status of the term is CONTRA.
- If all the mapped findings have an active refusal, the C/R status of the term is REFUSED.
- If some of the mapped findings have an active contraindication, while the rest have an active refusal, the C/R status of the term is REFUSED.
- If the term does not have a C/R status of either CONTRA or REFUSED, but there are mapped findings with a C/R status of PRECAUTION, the term will have a C/R status of PRECAUTION

When there are immunization findings with active C/Rs, the finding evaluation array, FIEVAL, can have CONTRA, PRECAUTION, and REFUSED nodes, depending on what active C/Rs were found. The FIEVAL C/R nodes will exist only when active C/Rs are found. The first number following the C/R subscript is the finding number and the second number is the occurrence.

When there is an active contraindication, it will look like this in Reminder Test:

FIEVAL("CONTRA",1)=1

FIEVAL("CONTRA",1,1,"COMMENTS")=

FIEVAL("CONTRA",1,1,"DATE")=3210514.09

FIEVAL("CONTRA",1,1,"REASON")=SEVERE REACTION PREVIOUS DOSE

FIEVAL("CONTRA",1,1,"WUDT")=0

In the example above, the WARN UNTIL DATE, "WUDT", is 0, meaning the contraindication is permanent.

When there is an active precaution, it will look like this in Reminder Test:

FIEVAL("PRECAUTION",1,1)=1

FIEVAL("PRECAUTION",1,1"COMMENTS")=

FIEVAL("PRECAUTION",1,1"DATE")=3181022.090211

FIEVAL("PRECAUTION",1,1"REASON")=CURRENT FEVER

FIEVAL("PRECAUTION",1,1"WUDT")=3181023

When there is an active refusal, it will look like this in Reminder Test:

FIEVAL("REFUSED",2)=1

FIEVAL("REFUSED",2,1,"COMMENTS")=

FIEVAL("REFUSED",2,1,"DATE")=3220111.09

FIEVAL("REFUSED",2,1,"GROUP REFUSAL")=Patient has refused all vaccines in the group.

FIEVAL("REFUSED",2,1,"REASON")=PATIENT DECISION

FIEVAL("REFUSED",2,1,"WUDT")=0

FIEVAL("REFUSED",2,2,"COMMENTS")=

FIEVAL("REFUSED",2,2,"DATE")=3220210.07

FIEVAL("REFUSED",2,2,"GROUP REFUSAL")=Patient has refused all vaccines in the group.

FIEVAL("REFUSED",2,2,"REASON")=PATIENT DECISION

FIEVAL("REFUSED",2,2,"WUDT")=0

In the REFUSED example above, finding 2 has two refusals, the first one on January 11, 2022 and the other on February 10, 2022.

The subscripts are:

DATE - the date the C/R was recorded.

REASON – the reason for the C/R. For contraindications this is an entry from file #920.4, IMM CONTRAINDICATION REASONS. For refusals this is an entry from file #920.5, IMM REFUSAL REASONS.

COMMENTS – comments added by the provider when they recorded the C/R.

GROUP REFUSAL – if there was a group refusal for the immunization, this subscript is set with the text “Patient has refused all vaccines in the group.”

WUDT – the warn until date, the C/R is active until the WUDT has been passed. If the WUDT is 0 the C/R is permanent. Note, that when recording a C/R in CPRS, the label for WARN UNTIL DATE is “Cancel Series and Stop Forecasting”, this is because the Office of Nursing Services wanted the same label as in Cerner.

A section for displaying contraindications, precautions, and refusals has been added to the Clinical Maintenance output. This is how they appear for the above FIEVAL arrays:

Contraindications

Immunization: HEP A, ADULT

05/14/2021@09:00 Reason: SEVERE REACTION PREVIOUS DOSE, is permanent.

Precautions

Immunization: HEP A, ADULT

10/22/2018@09:02:11 Reason: CURRENT FEVER, expires 10/23/2018.

Refusals

Immunization: INFLUENZA, INJECTABLE, QUADRIVALENT

01/11/2022@09:00 Reason: PATIENT DECISION, is permanent.

Patient has refused all vaccines in the group.

02/10/2022@07:00 Reason: PATIENT DECISION, is permanent.

Patient has refused all vaccines in the group.

**CONTRAINDICATED LOGIC and REFUSED LOGIC**

A CONTRAINDICATED LOGIC string and a REFUSED LOGIC string have been added, they are used to determine if the evaluation status should be CONTRA or REFUSED. They work just like the CUSTOMIZED PATIENT COHORT LOGIC and CUSTOMIZED RESOLUTION LOGIC. If the CONTRAINDICATED LOGIC is true, the evaluation status is CONTRA. If the CONTRAINDICATED LOGIC is false and the REFUSED LOGIC is true, the evaluation status is REFUSED.

Note that precautions cannot be used in the CONTRAINDICATED LOGIC or REFUSED LOGIC; therefore, they will not change the evaluation status. Their purpose is to provide patient information, to the provider, that should be taken into consideration when deciding whether or not the immunization should be given to the patient.

**Contraindications and Refusals in Function Findings**

The following function finding functions have been enhanced so they can use the data in the FIEVAL(“CONTRA”) and FIEVAL(“REFUSED”) nodes. This provides the mechanism to use C/Rs in the CONTRAINDICATED LOGIC and REFUSED LOGIC.

COUNT

DIFF\_DATE

DTIME\_DIFF

DUR

FI

MAX\_DATE

MIN\_DATE

MRD

VALUE

For these functions, when you want to use CONTRA or REFUSED data, precede the finding number with a C or R, respectively.

In this example: DTIME\_DIFF(C1,1,"DATE",R2,2,"DATE","M"), the first date is the when the first contraindication for finding 1 was recorded. The second date is when the second refusal for finding 2 was recorded.

The following functions are only applicable for numeric values, so they were not changed and cannot use CONTRA or REFUSED data.

MAX\_VALUE

MIN\_VALUE

NUMERIC

**CONTRAINDICATED LOGIC and REFUSED LOGIC Examples**

Consider the simple case of a reminder that is resolved by a single immunization, let’s say it is finding 2. To determine if it is contraindicated:

The function string for function finding 1 is: FI(C2)

The CONTRAINDICATED LOGIC is: FF(1)

To determine if it is refused:

The function string for function finding 1 is: FI(R2)

The REFUSED LOGIC is: FF(2)

The way sites want refusals for FLU to work requires more complex logic than in the simple examples shown above.

1. During flu season, it takes 2 recorded refusals in a 30-day period to resolve the reminder until the 30 days had elapsed from the first entry
2. At the end of flu season, which is usually in April or May, and the sites record that date in a term in the reminder, then after that date, any prior single refusal during flu season resolves the reminder until the date that the new flu season starts.

For this example, we assume finding 1 is the immunization finding that resolves the reminder, the date of finding 2 is the flu season start date, and the date of finding 3 is the flu season end date. PXRMDATE is the global reminder variable equal to the reminder evaluation date and time. The REFUSED LOGIC can be written using two function findings, one for during flu season and one for after flu season.

The function finding for during flu season (assume it is FF10) is:

(PXRMDATE'&gt;FLU END)&amp;(PXRMDATE'&lt;FLU START)&amp;(COUNT(R1)&gt;1)

&amp;(DTIME\_DIFF(R1,1,"DATE",R1,2,"DATE","D","A")&lt;31)

Replacing FLU START and FLU END with the corresponding findings:

(PXRMDATE'&gt;MRD(3))&amp;(PXRMDATE'&lt;MRD(2))&amp;(COUNT(R1)&gt;1)

&amp;(DTIME\_DIFF(R1,1,"DATE",R1,2,"DATE","D","A")&lt;31)

The function finding for after flu season (assume it is FF11) is:

(MRD(R1)'&gt;MRD(3))&amp;(MRD(R1)'&lt;MRD(2))&amp;(PXRMDATE&gt;MRD(3))&amp;(COUNT(R1)&gt;0)

The REFUSED LOGIC is FF(10)!FF(11)

**DUE DATE When CONTRAINDICATED LOGIC or REFUSED LOGIC is True**

When the C/R is permanent, then the DUE DATE is NEVER.

When the C/R is not permanent:

If the calculated due date is after the C/R has expired, The DUE DATE is the calculated due date.

If the C/R expiration date is after the calculated due date, then the DUE DATE is the date the C/R is no longer active.

**How Contraindications and Refusals are Applied to Immunizations**

Some contraindications apply to more than one immunization. The immunizations a contraindication applies to can be found by examining the IMMUNIZATIONS LIMITED TO multiple in the IMM CONTRAINDICATION REASONS FILE, #920.4. For example, the contraindication LATEX ALLERGY applies to the following immunizations:

IMMUNIZATIONS LIMITED TO: HEP B, ADOLESCENT OR PEDIATRIC

IMMUNIZATIONS LIMITED TO: DTAP

IMMUNIZATIONS LIMITED TO: ANTHRAX

IMMUNIZATIONS LIMITED TO: HEP B, ADULT

IMMUNIZATIONS LIMITED TO: HEP B, DIALYSIS

IMMUNIZATIONS LIMITED TO: HIB (PRP-OMP)

IMMUNIZATIONS LIMITED TO: HEP A, ADULT

IMMUNIZATIONS LIMITED TO: HEP A, PED/ADOL, 2 DOSE

IMMUNIZATIONS LIMITED TO: HEP A-HEP B

IMMUNIZATIONS LIMITED TO: DTAP-HEP B-IPV

IMMUNIZATIONS LIMITED TO: TD (ADULT), 5 LF TETANUS TOXOID, PRESERVATIVE FREE, AD

SORBED

IMMUNIZATIONS LIMITED TO: TDAP

IMMUNIZATIONS LIMITED TO: ROTAVIRUS, MONOVALENT

IMMUNIZATIONS LIMITED TO: DTAP-IPV

If a patient has a LATEX ALLERGY contraindication recorded for HEP A, ADULT they will have a LATEX ALLERGY contraindication for all the immunizations shown above, even though the contraindication was recorded only for HEP A, ADULT.

A refusal can be for a single immunization or for all the immunizations in the vaccine group. When there is a group refusal then all immunizations in the vaccine group will also be refused. The HepA group contains the following immunizations:

HEP A, UNSPECIFIED FORMULATION

HEP A, ADULT

HEP A, PED/ADOL, 2 DOSE

HEP A, PED/ADOL, 3 DOSE

HEP A-HEP B

HEP A, PEDIATRIC, UNSPECIFIED FORMULATION

HEP A-HEP B, PEDIATRIC/ADOLESCENT

If the patient has a group refusal recorded for HEP A, UNSPECIFIED FORMULATION, they will have a refusal for all the other immunizations in this group.

The vaccine groups an immunization belongs to can be found in the VACCINE GROUP NAME multiple of the IMMUNIZATION FILE, #9999999.14.

Some immunizations belong to more than one group. The immunization DTP-HIB belongs to the groups: HIB and DTAP. There are 14 immunizations in the HIB vaccine group and 14 in the DTAP vaccine group. A group refusal for DTP-HIB will apply to all the vaccines in both the HIB and DTAP vaccine groups.

The IMMUNIZATION FILE, #9999999.14 and the IMM CONTRAINDICATION REASONS FILE, #920.4 are both standardized and locked down, they are updated by NTRT data pushes. Therefore, both the Vaccine Group(s) an immunization belongs to can change as well as the immunizations in the IMMUNIZATIONS LIMITED TO multiple for a contraindication. The examples given above were current when this is written, but they could be changed at some point by an NTRT push.

- Order Check Text Only: This value will only display the text defined by the user in the order check text field.