---
app_name: Computerized Patient Record System (CPRS)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: CPRS
patch: null
patch_gap: null
section: ''
source_file: OR_3_0_377_setup.docx
status: draft
title: '# Computerized Patient Record System Version 31b'
---

# Computerized Patient Record System Version 31b

Set Up and Configuration Guide

CPRS Version 31b Patches

<!-- image -->

September 2020


Enterprise Program Management Office (EPMO)

**This page left intentionally blank.**

Revision History

| Date      |   Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                  | Author   |
|-----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 8/6/2020  |       1.9 | Section 3.1.1 Install Women’s Health High Risk Medications Content – Changed the section number in two steps from 2.2.1 to 2.2.2.  Section 3.1.2 Install Women’s Health Mammography Tracking Content – Removed a duplicate entry (VA-BREAST TUMOR) under Reminder Taxonomies.                                                                                                                                                | REDACTED |
| 8/6/2020  |       1.8 | Section 3.1.2: In the Install Women’s Health Mammography Tracking Content: Corrected the name of one item.  Section 3.22: Configure Copy/Paste Settings: Added that to disable Copy/Paste for an entire site requires someone with Programmer access. Also, added a note about the ORQQTIU COPY/PASTE IDENT parameter requiring 12 comma-separated values.                                                                   | REDACTED |
| 7/10/2020 |       1.7 | Section 3.5: Added instructions to re-index file 801 post installation.                                                                                                                                                                                                                                                                                                                                                      | REDACTED |
| 7/10/2020 |       1.6 | Section 3.4.4: Removed COMPLETE from the statuses that should be selected for each item.                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 7/8/2020  |       1.5 | Added new Section 3.7: Sites should inactivate a note title that will no longer be used.  Updated Section 3.1: Tasks must complete before proceeding with section 3.5.                                                                                                                                                                                                                                                       | REDACTED |
| 7/7/2020  |       1.4 | Updated Section 3.1: Sites must wait for specific tasks to complete before proceeding with configuration tasks.                                                                                                                                                                                                                                                                                                              | REDACTED |
| 7/2/2020  |       1.3 | Added new Section 3.5: Update Reminder General Findings.                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 6/25/2020 |       1.2 | Section 2.2.2: Made some corrections to this section about who should be performing actions and what the actions are.                                                                                                                                                                                                                                                                                                        | REDACTED |
| 6/23/2020 |       1.1 | Section 3.1.1: Removed an item under the list of Reminder terms to be skipped during installation.  Section 3.3. Removed one item from the table under Link Reminder Dialogs to Document Titles.  Section 3.4.2: Under Map Laboratory Test(s) to Terms, corrected the names of Reminder terms: VA-WH POSITIVE LAB PREGNANCY TEST and VA-WH NEGATIVE LAB PREGNANCY TEST  Section 3.4.5: Corrected the name of a Reminder term | REDACTED |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |
|           |           |                                                                                                                                                                                                                                                                                                                                                                                                                              |          |

Table of Contents

1	Computerized Patient Record System Graphical User Interface	1

1.1	Overview	1

1.2	Recommended Audience	1

1.3	About this Guide	1

1.4	Document Conventions	2

1.5	Related Documents	2

2	Pre-requisites	3

2.1	Installation Checklist	3

2.2	Pre-Installation Steps	4

2.2.1	How to Resolve Duplicate Document Classes or Titles	5

2.2.2	Create or Identify Quick Orders for Reminder Dialogs	15

2.2.3	Prepare for Clinical Reminder Mapping	16

2.2.4	Determine Users of New Reminders	19

2.2.5	Write the TIU Ancillary Data Message Text	19

2.2.6	Review Cover Sheet Customization	20

2.2.7	Register CPRS If Necessary	23

2.2.8	Confirm VistA FileMan Permission	24

3	Post-Installation Tasks	25

3.1	Install Reminder Content	25

3.1.1	Install Women’s Health High Risk Medications Content	25

3.1.2	Install Women’s Health Mammography Tracking Content	33

3.2	Link Reminder Terms to Women’s Health Procedure Type Entries	43

3.3	Link Reminder Dialogs to Document Titles	44

3.4	Clinical Reminder Mapping	45

3.4.1	Map Orderable Item(s) to the VA-WH PREGNANCY TEST ORDERED Term	45

3.4.2	Map Laboratory Test(s) to Terms	47

3.4.3	Map Radiology Parent Procedure(s) to Terms	49

3.4.4	Map Orderable Items to the VA-PENDING BREAST IMAGING ORDERS Term	51

3.4.5	Update Reminder Term Condition Statement	52

3.5	Re-Index Reminder Order Check Items Group File	53

3.6	Update Reminder General Findings	54

3.7	Enable Clinical Reminder Order Check Rules	55

3.8	Inactivate a New Note Title	59

3.9	Configure Women’s Health Site Parameters	63

3.9.1	Step 1: Designate a Case Manager	63

3.9.2	Step 2: Create/Update a WV SITE PARAMETER File Entry	66

3.10	Review Users in the Women’s Health Package	74

3.10.1	Step 1: Review and Update the List of Case Managers	74

3.10.2	Step 2: Transfer Inactive Case Managers’ Patients	77

3.10.3	Step 3: Assign New Case Managers to Patients	78

3.10.4	Step 4: Designate Users as a Maternity Care Coordinator	80

3.10.5	Step 5: Assign Maternity Care Coordinators to Patients	82

3.11	Add the Women’s Health Cover Sheet Panel to Customized Cover Sheets	84

3.12	Add New Clinical Reminders to the Cover Sheet Reminder List	88

3.13	Setup SMART Notifications	88

3.14	Setup a Reminder List Rule to Automatically Update a Team List (Optional)	89

3.14.1	Create a Team List	90

3.14.2	Map the team list to a list rule	91

3.15	Schedule the Update Team List from Reminder List Rule Option	93

3.16	Setup SCHEDULED ALERTS for Tickler Alerts	95

3.17	Confirm TIU TEMPLATE CONSULT LOCK Values	96

3.18	Review Line Length for Consult and Procedure Templates	97

3.19	Review Post-Installation Message GMRA*4*53 CLEAN-UP STATUS	98

3.20	Review Post-Installation Message OUTPATIENT MED QUICK ORDER CONVERSION	98

3.21	Review Post-Installation Message Update to Dietetic Quick Order	99

3.22	Configure Copy/Paste Settings	99

3.23	Configure Exception Parameters	101

3.24	Configure Site Parameter for One-Step Clinic Administration	101

3.25	Configure site parameter OR CPRS HELP DESK TEXT	103

3.26	Convert Existing Pregnancy and Lactation Data	103

4	Worksheets	105

4.1	Worksheet #1	105

4.2	Worksheet #2	107

4.3	Worksheet #3	108


## 2 Computerized Patient Record System Graphical User Interface

### Overview

The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

### Recommended Audience

This guide provides information specifically for those personnel who need to perform set up and configuration steps before and after the install of CPRS v31b. These groups include Information Technology Operations and Support (ITOPS) staff, Clinical Application Coordinator (CAC) personnel, the site’s Women’s Health group, and others who will be needed for pre-installation and post-installation steps so that CPRS v31b will work correctly at sites.

### About this Guide

This set up/configuration guide provides instructions for:

- Pre-installation steps, several of which must be performed before the CPRS v31b installation can proceed.

Performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system

### Document Conventions

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER       Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

## Note:	This is an important point and must not be omitted


Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text

Sample text, Sample text, Sample text, Sample text

Sample text

Informational text about the point of note

<!-- image -->

Sample text, Sample text, Sample text

Sample text, Sample text, Sample text, Sample text, Sample text

### Related Documents

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

*CPRS User Guide*

*CPRS Technical Manual*

*CPRS Technical Manual: GUI Version*

*CPRS v31b Release Notes*

*CPRS v31b Installation Guide*

*CPRS Set Up/Configuration Guide* (this manual)

## 3 Pre-requisites

Before beginning the processes described in this document the tasks outlined in this section must be completed.

### Installation Checklist

|                                                                                                                                                       |                                                                                                                                                       |                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| **TASK**                                                                                                                                              |                                                                                                                                                       | **RESPONSIBLE POC**                                                                                                                                     | **COMMENTS**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |    |
|                                                                                                                                                       |                                                                                                                                                       |                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm that Facility Leadership is aware of CPRS v31b implementation date.                                                                           | Confirm that Facility Leadership is aware of CPRS v31b implementation date.                                                                           | Primary Point of Contact (POC), Health Informatics Specialist/Clinical Applications Coordinators (HIS/CAC), Office of Information and Technology (OI&T) | See the  *Release v31b Wave Schedule*  and  *Release v31b Wave Schedule with Sites*  on the  [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D) |    |
| Review the  *CPRS v31b DIBOR*  .                                                                                                                      |                                                                                                                                                       | OI&T                                                                                                                                                    | Located on the CPRS v31b Training Page                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |    |
| Review the  *CPRS v31b Release Notes*                                                                                                                 |                                                                                                                                                       | HIS/CAC                                                                                                                                                 | Located on the CPRS v31b Training Page                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |    |
| Review the  *CPRS v31b Setup and Configuration Guide*                                                                                                 |                                                                                                                                                       | HIS/CAC and OI&T                                                                                                                                        | Located on the CPRS v31b Training Page                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |    |
| Review the Wave Kickoff Document                                                                                                                      | Review the Wave Kickoff Document                                                                                                                      | HIS/CAC, OI&T, Primary POC, HIM, other stakeholders                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm CPRS v31a COVID-19 Identifier was installed                                                                                                   | Confirm CPRS v31a COVID-19 Identifier was installed                                                                                                   | HIS/CAC, OI&T                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm the necessary HIS/CAC, POC and OI&T staff are available during the assigned Wave dates at your site (i.e. Wave kick off call)                 | Confirm the necessary HIS/CAC, POC and OI&T staff are available during the assigned Wave dates at your site (i.e. Wave kick off call)                 | OI&T, HIS/CAC, other Subject Matter Expert (SME), Health Information Management (HIM), Lab Information Manager, etc.                                    | See the  *Release v31b Wave Schedule*  and  *Release v31b Wave Schedule with Sites*  on the  [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D) |    |
| Confirm that the necessary change order requests, to have the CPRS v31b patches installed, have been submitted to OI&T (Region, VISN and/or facility) | Confirm that the necessary change order requests, to have the CPRS v31b patches installed, have been submitted to OI&T (Region, VISN and/or facility) | HIS/CAC, OI&T                                                                                                                                           | in some Regions the OI&T staff have up to 2 weeks to perform the task.                                                                                                                                                                                                                                                                                                                                                                                                                                 |    |
| Necessary personnel attend the Wave kick-off call/training for CPRS v31b                                                                              | Necessary personnel attend the Wave kick-off call/training for CPRS v31b                                                                              | OI&T, HIS/CAC, other SME (HIM, Lab manager, etc.)                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm that local support personnel are prepared and staffed during and after installation into Live account                                         | Confirm that local support personnel are prepared and staffed during and after installation into Live account                                         | Primary POC, HIS/CAC, OI&T                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Inform all clinical staff of the CPRS v31b production installation date (emails, staff meetings)                                                      | Inform all clinical staff of the CPRS v31b production installation date (emails, staff meetings)                                                      | Primary POC, HIS/CAC, OI&T                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm that training for clinical staff has taken place.                                                                                             | Confirm that training for clinical staff has taken place.                                                                                             | providers, nursing, Health Information Management (HIM), HIS/CAC                                                                                        | Create/modify training tools, reserve training rooms, send announcement to staff for training, enlist "super users" assistance.                                                                                                                                                                                                                                                                                                                                                                        |    |
| Confirm that OI&T staff have the necessary access to install patches.                                                                                 | Confirm that OI&T staff have the necessary access to install patches.                                                                                 | OI&T                                                                                                                                                    | Access to servers, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |    |
| Confirm that the patches have been downloaded                                                                                                         | Confirm that the patches have been downloaded                                                                                                         | OI&T                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| Coordinate with necessary personnel for Citrix updates.                                                                                               | Coordinate with necessary personnel for Citrix updates.                                                                                               | Local site, ITOPS                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |

**CPRS v31B TEST SITE READINESS CHECKLIST**

### Pre-Installation Steps

The following steps need to be taken prior to installing CPRS v31b.

Sites will need to coordinate with several different groups or individuals to discuss decisions that need to be made in preparation for and after the installation process, including how to handle conversions and mappings that will occur.

In order to have a smooth and timely install of CPRS v31b, it is important to have these decisions made and setups complete before the time of the actual installation.

These groups include

Women’s Health

Clinical Reminders manager

TIU managers

Health Information Management Service

Desktop Support

#### How to Resolve Duplicate Document Classes or Titles

**CACs** : The Clinical Application Coordinators (CACs) will perform this step.

As part of the complete CPRS v31b installation, two document classes and six progress note titles are added to your system. Because the new document classes and progress notes would overwrite any existing document classes and note titles with the same name, the installation checks to see if they already exist on your system. If the following items exist on your system, the installation will not proceed until the duplicate items are resolved.

The document classes are:

- WOMEN’S HEALTH NOTES
- SMART NOTES

The progress note titles are:

- HEALTHELIVING ASSESSMENT SUMMARY
- LACTATION STATUS UPDATE REVIEW
- PREGNANCY STATUS UPDATE REVIEW
- SMART BREAST IMAGING FOLLOW-UP
- SMART PATIENT NOTIFICATION
- SMART OUTSIDE BREAST IMAGE RESULTS

**Document Classes**

If one of these document classes exist on the system, sites have two options for handling the duplicate document classes:

Document Class Option 1

Rename the pre-existing class(es) and do nothing with the renamed class(es) after installation. With this option, sites will have two document classes after installation.

Document Class Option 2

Rename the pre-existing class(es) and after installation, move the titles from the renamed class(es) into the appropriate class then delete the renamed class(es). With this option, sites will have one document class after installation.

For both options, perform the following steps:

1. Rename the pre-existing class(es)
2. Activate the title(s) underneath the renamed class(es)

Examples from the TIU IRM MAINTENANCE MENU :

Rename the Pre-Existing Class and Activate the Titles Underneath the Renamed Class

Select TIU Maintenance Menu &lt;TEST ACCOUNT&gt; Option: 2  Document Definitions (Manager)

--- Manager Document Definition Menu ---

1      Edit Document Definitions

2      Sort Document Definitions

3      Create Document Definitions

4      Create Objects

5      Create TIU/Health Summary Objects

6      Create Post-Signature Alerts

Select Document Definitions (Manager) &lt;TEST ACCOUNT&gt; Option: 1  Edit Document Definitions.......

**Edit Document Definitions** Oct 03, 2019@13:50:36          Page:    1 of    1

BASICS

Name                                                                Type

1      CLINICAL DOCUMENTS                                                   CL

2       +PROGRESS NOTES                                                     CL

3       +ADDENDUM                                                           DC

4       +DISCHARGE SUMMARY                                                  CL

5       +CLINICAL PROCEDURES                                                CL

6       +LR LABORATORY REPORTS                                              CL

7       +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Quit// EX   Expand/Collapse

Select Entry:  (1-7): 2........................................................

**Edit Document Definitions** Oct 03, 2019@13:52:12          Page:    2 of    3

BASICS

+      Name                                                                Type

16        +COMMUNITY CARE                                                   DC

17        +COMPENSATION                                                     DC

18        +INFECTIOUS DISEASE                                               DC

19        +INTERDISCIPLINARY                                                DC

20        +INTERDISCIPLINARY CHILD                                          DC

21        +INTERDISCIPLINARY PARENT                                         DC

22        +MEDICINE                                                         DC

23        +MENTAL HEALTH                                                    DC

24        +MISCELLANEOUS TITLES                                             DC

25        +NONVA CARE                                                       DC

26        +SOCIAL WORK SERVICE                                              DC

27        +SUICIDE PREVENTION                                               DC

28        +VETERANS CHOICE PROGRAM/NON-VA CARE                              DC

29        +WOMEN'S HEALTH NOTES                                             DC

+         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Next Screen// DET   Detailed Display/Edit

Select Entry:  (16-29): 29

**Detailed Display** Oct 03, 2019@13:52:35          Page:    1 of    3

Document Class WOMEN'S HEALTH NOTES

Basics            Note: Values preceded by * have been inherited

Name:   WOMEN'S HEALTH NOTES

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:   WOMEN'S HEALTH NOTES

Type:   DOCUMENT CLASS

IFN:   1998

National

Standard:   NO

Status:   ACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection: * NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    Technical Fields          Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

(Boilerplate Text)        Try

Select Action: Next Screen// BAS   Basics

Edit Abbreviation, Owner and Status only; Entry not Inactive

ABBREVIATION:

CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR

STATUS: (A/I): ACTIVE// I  INACTIVE

This will Inactivate ALL DESCENDANTS (except Shared Components).  Before

Inactivating, please note which Descendants are presently Inactive.  This will

help you know which Descendants NOT to reactivate later.

Sure you want to Inactivate? NO// YES ...

Entry and descendants Inactivated

**Detailed Display** Oct 03, 2019@13:53:38          Page:    1 of    3

Document Class WOMEN'S HEALTH NOTES

Basics            Note: Values preceded by * have been inherited

Name:   WOMEN'S HEALTH NOTES

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:   WOMEN'S HEALTH NOTES

Type:   DOCUMENT CLASS

IFN:   1998

National

Standard:   NO

Status:   INACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection: * NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    Technical Fields          Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

(Boilerplate Text)        Try

Select Action: Next Screen// BAS   Basics

NAME: WOMEN'S HEALTH NOTES  Replace NOTES With NOTES LOCAL

Replace

WOMEN'S HEALTH NOTES LOCAL

ABBREVIATION:

PRINT NAME: WOMEN'S HEALTH NOTES  Replace

TYPE: (CL/DC): DC//   DOCUMENT CLASS

CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR

SUPPRESS VISIT SELECTION: NO//   NO

STATUS: (A/I): INACTIVE// A  ACTIVE Entry Activated.

**Detailed Display** Oct 03, 2019@13:53:56          Page:    1 of    3

Document Class WOMEN'S HEALTH NOTES LOCAL

Basics            Note: Values preceded by * have been inherited

Name:   WOMEN'S HEALTH NOTES LOCAL

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:   WOMEN'S HEALTH NOTES

Type:   DOCUMENT CLASS

IFN:   1998

National

Standard:   NO

Status:   ACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection:   NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    Technical Fields          Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

(Boilerplate Text)        Try

Select Action: Next Screen// Q   Quit

**Edit Document Definitions** Oct 03, 2019@13:54:27          Page:    2 of    3

BASICS

+      Name                                                                Type

16        +COMMUNITY CARE                                                   DC

17        +COMPENSATION                                                     DC

18        +INFECTIOUS DISEASE                                               DC

19        +INTERDISCIPLINARY                                                DC

20        +INTERDISCIPLINARY CHILD                                          DC

21        +INTERDISCIPLINARY PARENT                                         DC

22        +MEDICINE                                                         DC

23        +MENTAL HEALTH                                                    DC

24        +MISCELLANEOUS TITLES                                             DC

25        +NONVA CARE                                                       DC

26        +SOCIAL WORK SERVICE                                              DC

27        +SUICIDE PREVENTION                                               DC

28        +VETERANS CHOICE PROGRAM/NON-VA CARE                              DC

29        +WOMEN'S HEALTH NOTES LOCAL                                       DC

+         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Next Screen//

**Activate Title**

**Edit Document Definitions** Oct 03, 2019@13:54:27          Page:    2 of    3

BASICS

+      Name                                                                Type

16        +COMMUNITY CARE                                                   DC

17        +COMPENSATION                                                     DC

18        +INFECTIOUS DISEASE                                               DC

19        +INTERDISCIPLINARY                                                DC

20        +INTERDISCIPLINARY CHILD                                          DC

21        +INTERDISCIPLINARY PARENT                                         DC

22        +MEDICINE                                                         DC

23        +MENTAL HEALTH                                                    DC

24        +MISCELLANEOUS TITLES                                             DC

25        +NONVA CARE                                                       DC

26        +SOCIAL WORK SERVICE                                              DC

27        +SUICIDE PREVENTION                                               DC

28        +VETERANS CHOICE PROGRAM/NON-VA CARE                              DC

29        +WOMEN'S HEALTH NOTES LOCAL                                       DC

+         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Next Screen// EX   Expand/Collapse

Select Entry:  (16-29): 29

**Edit Document Definitions** Oct 03, 2019@13:54:49          Page:    3 of    3

BASICS

+      Name                                                                Type

29         WOMEN'S HEALTH NOTES LOCAL                                       DC

30           PREGNANCY OR LACTATION STATUS UPDATE                           TL

31           VA-MATERNITY CARE COORDINATION                                 TL

32        +TBI/POLYTRAUMA DOCUMENTS                                         DC

33        +HOME TELEHEALTH NOTES                                            DC

34      +ADDENDUM                                                           DC

35      +DISCHARGE SUMMARY                                                  CL

36      +CLINICAL PROCEDURES                                                CL

37      +LR LABORATORY REPORTS                                              CL

38      +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Quit// DET   Detailed Display/Edit

Select Entry:  (29-38): 30

**Detailed Display** Oct 03, 2019@13:55:29          Page:    1 of    3

Title PREGNANCY OR LACTATION STATUS UPDATE

Basics            Note: Values preceded by * have been inherited

Name:   PREGNANCY OR LACTATION STATUS UPDATE

VHA Enterprise

Standard Title:   WOMENS HEALTH NOTE

Abbreviation:

Print Name:   PREGNANCY OR LACTATION STATUS UPDATE

Type:   TITLE

IFN:   258

National

Standard:   NO

Status:   INACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection: * NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    Technical Fields          Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

Boilerplate Text          Try

Select Action: Next Screen// BAS   Basics

NAME: PREGNANCY OR LACTATION STATUS UPDATE  Replace

ABBREVIATION:

PRINT NAME: PREGNANCY OR LACTATION STATUS UPDATE  Replace

EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

Direct Mapping to Enterprise Standard Title...

Your LOCAL Title is: PREGNANCY OR LACTATION STATUS UPDATE

NOTE: Only ACTIVE Titles may be selected...

The LOCAL Title: PREGNANCY OR LACTATION STATUS UPDATE

is already mapped to

VHA Enterprise Title: WOMENS HEALTH NOTE

Do you want to RE-MAP it? NO//

... OK, No Harm Done!

TYPE: (TL): TL//   TITLE

CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR

SUPPRESS VISIT SELECTION: NO//   NO

STATUS: (A/I/T): INACTIVE// A  ACTIVE Entry Activated.

**Detailed Display** Oct 03, 2019@13:55:41          Page:    1 of    3

Title PREGNANCY OR LACTATION STATUS UPDATE

Basics            Note: Values preceded by * have been inherited

Name:   PREGNANCY OR LACTATION STATUS UPDATE

VHA Enterprise

Standard Title:   WOMENS HEALTH NOTE

Abbreviation:

Print Name:   PREGNANCY OR LACTATION STATUS UPDATE

Type:   TITLE

IFN:   258

National

Standard:   NO

Status:   ACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection:   NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    Technical Fields          Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

Boilerplate Text          Try

Select Action: Next Screen// Q   Quit

**Edit Document Definitions** Oct 03, 2019@13:57:08          Page:    3 of    3

BASICS

+      Name                                                                Type

29         WOMEN'S HEALTH NOTES LOCAL                                       DC

30           PREGNANCY OR LACTATION STATUS UPDATE                           TL

31           VA-MATERNITY CARE COORDINATION                                 TL

32        +TBI/POLYTRAUMA DOCUMENTS                                         DC

33        +HOME TELEHEALTH NOTES                                            DC

34      +ADDENDUM                                                           DC

35      +DISCHARGE SUMMARY                                                  CL

36      +CLINICAL PROCEDURES                                                CL

37      +LR LABORATORY REPORTS                                              CL

38      +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Quit//    QUIT

**Titles**

None of the Progress Note titles should exist on the system, but if they do, sites will need to handle these titles appropriately.

If a site already has documents under a TITLE, they should do the following:

1. Create a new TITLE.
2. MOVE documents from the existing TITLE name to the new TITLE.
3. Delete the existing TITLE.
4. Install 31B.  They may keep their existing documents under the new TITLE if they choose.  Otherwise, continue…
5. Optional but recommended.  MOVE documents from new TITLE they created back to the newly installed “old” TITLE.  The DOCUMENT CLASS they’re moving to/from MUST be in the SAME CLASS (usually PROGRESS NOTES).  You can’t move documents to a DIFFERENT CLASS, different DOCUMENT CLASS is ok.
6. Delete the new TITLE name.

Example from the TIU IRM MAINTENANCE MENU:

3      Create Document Definitions

**Create Document Definitions** Sep 27, 2019@07:52:28          Page:    1 of    1

BASICS

+      Name                                                                 Type

2        PROGRESS NOTES                                                     CL

3 **SMART NOTES** DC

4            SMART BREAST IMAGING FOLLOW-UP                                 TL

5            SMART PATIENT NOTIFICATION                                     TL

6            SMART OUTSIDE BREAST IMAGE RESULTS                             TL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                  &gt;&gt;&gt;

(Class/DocumentClass)     Next Level                Detailed Display/Edit

Title                     Restart                   Status...

(Component)               Boilerplate Text          Delete

Select Action: Title// title   Title

Enter the Name of a new SMART NOTES: SMART PATIENT NOTIFICATION TEMPORARY

1      Edit Document Definitions

**Edit Document Definitions** Sep 27, 2019@07:55:06          Page:    4 of    5

BASICS

+      Name                                                                 Type

44        +SECURE MESSAGING DOCUMENTS                                       DC

45        +CPRS TEST                                                        DC

46         LEIF                                                             CL

47         LEIF TITLE                                                       CL

48        +WOMEN'S HEALTH NOTES                                             DC

49         SMART NOTES                                                      DC

50           SMART BREAST IMAGING FOLLOW-UP                                 TL

51           SMART PATIENT NOTIFICATION                                     TL

52           SMART PATIENT NOTIFICATION TEMPORARY                           TL

53           SMART OUTSIDE BREAST IMAGE RESULTS                             TL

54      +ADDENDUM                                                           DC

55      +DISCHARGE SUMMARY                                                  CL

56      +CLINICAL PROCEDURES                                                CL

57      +SURGICAL REPORTS                                                   CL

+         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                  &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Next Screen// copy   Copy/Move

Select Copy/Move Action:  (MT/MD/C/U): MT// MD  MOVE DOCUMENTS

WARNING: This action affects inheritance and can CHANGE DOCUMENT BEHAVIOR.  It

DISREGARDS ownership.  It may take awhile if the Title has many documents.

Please use caution and DON'T TOUCH entries you are not responsible for.

Press RETURN to continue or '^' or '^^' to exit:

Select Title whose documents you want to Move:  (44-57): 51

Selecting target Title.  Enter '??' for a list of selectable ones.

You may not select PRF Flag Titles or Titles outside the original Class.

Select TIU TITLE NAME to Move documents to: SMART PATIENT NOTIFICATION TEMPORARY

TITLE

Std Title: WOMENS HEALTH NOTE

Moving documents from title

SMART PATIENT NOTIFICATION

to title  SMART PATIENT NOTIFICATION TEMPORARY.

Are you sure? YES//

OLD Title inactivated.  Moving documents....

...done.  All documents Moved to Title SMART PATIENT NOTIFICATION TEMPORARY.

Parent Document Type updated as necessary for all documents.

If you want users to be able to enter more documents on the OLD TITLE,

please reactivate it.

**Edit Document Definitions** Sep 27, 2019@07:59:36          Page:    4 of    5

BASICS

+      Name                                                                 Type

44        +SECURE MESSAGING DOCUMENTS                                       DC

45        +CPRS TEST                                                        DC

46         LEIF                                                             CL

47         LEIF TITLE                                                       CL

48        +WOMEN'S HEALTH NOTES                                             DC

49         SMART NOTES                                                      DC

50           SMART BREAST IMAGING FOLLOW-UP                                 TL

51           SMART PATIENT NOTIFICATION                                     TL

52           SMART PATIENT NOTIFICATION TEMPORARY                           TL

53           SMART OUTSIDE BREAST IMAGE RESULTS                             TL

54      +ADDENDUM                                                           DC

55      +DISCHARGE SUMMARY                                                  CL

56      +CLINICAL PROCEDURES                                                CL

57      +SURGICAL REPORTS                                                   CL

+         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                  &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit     Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                 Delete

Boilerplate Text          Name/Owner/PrintName...   Copy/Move

Select Action: Next Screen// DEL

Processing Entry 51...

Entry 51 is not presently used by any documents.  If entry is deleted,

any items UNDER it will be Orphans.  I will delete entry as an item under its

parent AND as a Document Definition.  It will no longer exist. OK? NO// YES

... Entry 51 Deleted!

#### Create or Identify Quick Orders for Reminder Dialogs

**CAC:** Clinical Applications Coordinators (CACs) will perform this task.

Option: *Enter/edit quick orders* on the *Order Menu Management* menu on the *CPRS Configuration (Clin Coord)* menu.

During content installation, the CAC or reminders manager is prompted for the name of these quick orders so that the software can link the quick orders with the new high-risk medications and Mammogram Result Tracking reminder dialogs. While the content installation does not require the CAC or reminders manager to specify these quick orders, creating or identifying the quick orders before installation and specifying them during content installation will prevent you from having to manually link them to the reminder dialogs later. Without linking the quick orders to the reminder dialogs, providers will not be able to order a pregnancy test nor an emergency contraceptive while completing the new high-risk medications reminder dialogs or place orders from the reminder dialogs for breast treatment needs.

| BREAST TREATMENT MENU               | This Order menu is used throughout the Mammogram SMART Dialogs. Sites will need to determine the order dialog/menu/qo/order set for each Reminder Dialog Item. Site should select a dummy install Quick Orders that CACs can used to find the dialog items that should be updated   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EMERGENCY CONTRACEPTIVE QUICK ORDER | Define a Quick Order for a clinic medication for emergency contraceptive                                                                                                                                                                                                            |
| PREGNANCY TEST QUICK ORDER          | Define a Quick Order for a laboratory test for pregnancy                                                                                                                                                                                                                            |

#### Prepare for Clinical Reminder Mapping

**CAC/Radiology ADPAC/Laboratory ADPAC:** Clinical Applications Coordinators (CACs), the radiology ADPAC and the laboratory ADPAC will perform this task together.

During the post-installation section, you will need to map items that your site uses to new clinical reminder terms. These mappings are essential to the proper functioning of the Women’s Health high risk medications and mammography results tracking functionality. This section will walk you through the steps to identify the items that you will map.

##### Identify Laboratory Tests

Option: *Inquiry to LAB TEST file* on the *Supervisor menu* , which is on the *Laboratory DHCP Menu* .

1. Using the Inquiry to LAB TEST file option, complete the Laboratory Tests table in Worksheet #1 at the end of this guide. In the TEST NAME column, enter the laboratory test name. In the SITE/SPECIMEN column, enter the SITE/SPECIMEN value(s), with one value per row. In the Patient is Pregnant column, record the value or range of values that denote the patient is pregnant for each SITE/SPECIMEN value. In the Patient is Not Pregnant column, record the value or range of values that denote the patient is not pregnant for each SITE/SPECIMENT value. You may add or remove rows from the table depending on how many tests your site uses to determine pregnancy and how many SITE/SPECIMEN values there are for each test.

1. Complete the Patient is Pregnant Condition Statements table in Worksheet #1. For each laboratory test listed in the Laboratory Tests table, use the value in the Patient is Pregnant column and the instructions in the Clinical Reminders Manager’s Manual on how to populate the CONDITION STATEMENT cells. For the CASE SENSITIVE column, answer NO if the value representing the result is non-numeric (i.e., text within double quotes). For example, if the CONDITION STATEMNT is I V[“POS”, then put the word NO into the corresponding CASE SENSITIVE cell. Leave the CASE SENSITIVE cell blank if the value representing the result is numeric. For example, if the CONDITION STATEMENT is I V&gt;5, then leave the corresponding CASE SENSITIVE cell blank.

##### Identify Radiology Procedures

Option: *Active Procedure List (Short)* on the *Procedure File Listings* menu, which is on the *Maintenance Files Print Menu* , which is on the *Supervisor Menu* , which is on the *Rad/Nuc Med Total System Menu*

1. Use the option *Active Procedure List (Short)* to generate a list of mammography, ultrasound and magnetic resonance imaging (MRI) procedures used at your site.

**Example: Generating a list of imaging procedures**

Select Procedure File Listings &lt;TEST ACCOUNT&gt; Option: Active Procedure List (Short)

Select Imaging Type: All// MAMMOGRAPHY

Another one (Select/De-Select): ULTRASOUND

Another one (Select/De-Select): MAGNETIC RESONANCE IMAGING

Another one (Select/De-Select):

This report requires a 132 column output device.

You may select any device that can accommodate 132 columns.

<!-- image -->

DEVICE: HOME// SPOOL  SPOOLER

Requested Start Time: NOW//  (APR 27, 2017@14:34:54)

Request Queued, Task #: 94180

Press RETURN to continue...

1. The output from step #1 contains all active procedures regardless of their type. For the purposes of this step, you are only interested in parent procedures. Parent procedures are differentiated from the other procedure types by the listing of their descendant detailed or series procedures. For example, the following procedure is a parent procedure:

-------------------------------------------------------------------------------

P/D SCREEN MAMMOGRAM, BILAT

Type of Imaging  :  MAMMOGRAPHY

Descendants      :  MM BILAT SCR BREASTS W CAD

+ BILAT SCR BREASTS TOMO

-------------------------------------------------------------------------------

When reviewing the procedures whose type of imaging is either ultrasound or MRI, you are only interested in those procedures that are related to breast imaging.

Complete the Radiology Parent Procedures table in Worksheet #2 at the end of this guide using the list of imaging procedures generated in step #1. In the PARENT PROCEDURE NAME column, enter the name of the parent procedure. In the CPT CODES column, enter the CPT code associated with each of the descendent procedures. You may add or remove rows as needed depending on the number of parent procedures used at your site. Leave the TAXONOMY NAME column blank; you will populate this column when you complete the post-install tasks.

1. For the purposes of this step, you are only interested in non-biopsy detailed and series procedures.

When reviewing the procedures whose type of imaging is either ultrasound or MRI, you are only interested in those procedures that are related to breast imaging.

Complete the Radiology Detailed and Series Procedures table in Worksheet #2 at the end of this guide using the list of imaging procedures generated in step #1. In the PROCEDURE NAME column, enter the name of the detailed or series procedure.

**!!IMPORTANT!!** Do not include parent procedures in this table. Do not include biopsy procedures in this table.

#### #### Determine Users of New Reminders

**CAC/Women’s Health Office/Primary Care:** Clinical Applications Coordinators (CACs) in consultation with the Women’s Health office and Primary Care should perform this task

There are two new clinical reminders with this release of CPRS: Pregnancy/Intentions/Contraception and Update Lactation Status. These reminders provide one way to document a patient’s pregnancy and breastfeeding statuses (the other way is through the Women’s Health panel on the Cover Sheet tab). Before users can use either reminder and their associated dialog, sites must add the clinical reminders to the appropriate users’ Reminder Cover Sheet List. The Reminder Cover Sheet List can be set for specific users, classes of users, specific locations, specific services, entire divisions or the complete VistA system.

Create a list of users and/or classes of users and/or specific locations and/or specific services and/or divisions that should have access to the new reminders.

During the post-installation tasks, you are given instructions on how to modify the Reminder Cover Sheet List to add these new reminders.

#### Write the TIU Ancillary Data Message Text

**CAC/HIMS/Women’s Health Office:** CAC personnel will perform after consulting with Health Information Management Service (HIMS) and the site’s Women’s Health Office. After the HIMS/Women’s Health Office decide on the message, the CAC will have the access to enter the information in the parameter.

The TIU ANCILLARY DATA MESSAGE is a new CPRS v31b parameter. The text stored in this parameter is shown to the user of the Text Integration Utilities (TIU) software package when a document is retracted or reassigned and that document has pregnancy or lactation status data associated with it. This message will appear in both the CPRS GUI and in the roll and scroll TIU options.

When users receive this message, a chart review is necessary to ensure that the status data in the Women’s Health software package is accurate. This message text should include instructions to the user on how to initiate that chart review. You will need to contact your site’s Women’s Health office to identify an email address and/or phone number that users will use to initiate that chart review. Keep in mind that the message text is limited to 79 characters in length.

During the post-installation tasks, you are given instructions on how to set this parameter.

#### Review Cover Sheet Customization

**ITOPS/CAC:** This step is performed by the site’s local/regional OI&amp;T support and the Clinical Applications Coordinators (CACs).

The CPRS Cover Sheet is customizable for specific users, specific divisions at a site or everyone on the VistA system. There is a new Women’s Health panel with this release of CPRS. This panel is added to the default Cover Sheet configuration automatically when CPRS v31b is installed, but it is NOT added to any customized Cover Sheet configurations.

Sites should review all customized Cover Sheet configurations and decide if the new Women’s Health panel should be added to those configurations.

ITOPS personnel should execute the List Values for a Selected Parameter [XPAR LIST BY PARAM] option to display the customized Cover Sheet configurations. Then, capture that display and send it to the site’s CACs for review.

**Example of executing the List Values for a Selected Parameter option**

Select Core Applications &lt;TEST ACCOUNT&gt; Option: CPRS Manager Menu

CL     Clinician Menu ...

NM     Nurse Menu ...

WC     Ward Clerk Menu ...

PE     CPRS Configuration (Clin Coord) ...

IR     CPRS Configuration (IRM) ...

Select CPRS Manager Menu &lt;TEST ACCOUNT&gt; Option: IR  CPRS Configuration (IRM)

OC     Order Check Expert System Main Menu ...

TI     ORMTIME Main Menu ...

UT     CPRS Clean-up Utilities ...

XX     General Parameter Tools ...

DBG    RPC DEBUG REPORT

HD     HealtheVet Desktop Configuration ...

RD     Remote Data Order Checking Parameters

Select CPRS Configuration (IRM) &lt;TEST ACCOUNT&gt; Option: XX  General Parameter Tools

LV     List Values for a Selected Parameter

LE     List Values for a Selected Entity

LP     List Values for a Selected Package

LT     List Values for a Selected Template

EP     Edit Parameter Values

ET     Edit Parameter Values with Template

EK     Edit Parameter Definition Keyword

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: LV  List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: ORWCV1 COVERSHEET LIST     List of coversheet

reports

Values for ORWCV1 COVERSHEET LIST

Parameter                      Instance             Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 1                    ORCV ACTIVE PROBLEMS

PKG: ORDER ENTRY/RESULTS REPOR 2                    ORCV ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 3                    ORCV POSTINGS

PKG: ORDER ENTRY/RESULTS REPOR 4                    ORCV ACTIVE MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 5                    ORCV CLINICAL REMINDERS

PKG: ORDER ENTRY/RESULTS REPOR 6                    ORCV RECENT LAB RESULTS

PKG: ORDER ENTRY/RESULTS REPOR 7                    ORCV VITALS

PKG: ORDER ENTRY/RESULTS REPOR 8                    ORCV APPOINTMENTS

USR: PROVIDER,ONE              1                    ORCV ALLERGIES

USR: PROVIDER,ONE              2                    ORCV ACTIVE MEDICATIONS

USR: PROVIDER,ONE              3                    ORCV CLINICAL REMINDERS

USR: PROVIDER,ONE              4                    ORCV VITALS

Type &lt;Enter&gt; to continue or '^' to exit:

LV     List Values for a Selected Parameter

LE     List Values for a Selected Entity

LP     List Values for a Selected Package

LT     List Values for a Selected Template

EP     Edit Parameter Values

ET     Edit Parameter Values with Template

EK     Edit Parameter Definition Keyword

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option:

When reviewing the display, the following information is helpful:

- Entries that begin with PKG: represent the default Cover Sheet configuration and should be ignored.
- Panels on the Cover Sheet tab are displayed in a left-to-right, top-to-bottom fashion on the Cover Sheet tab. The Instance value determines the order of appearance. An instance value of 1 signifies this panel as the first panel, a value of 2 signifies the next panel to appear to the right of panel #1, and so on.

Record the customized Cover Sheet configurations that need the new Women’s Health panel in Worksheet #3 at the end of this document using the following instructions:

1. In the USER/DIVISION/SYSTEM column, copy the value from the display output’s Parameter column. For example, after reviewing the display output above, you determine that ONE PROVIDER needs the new panel on his customized Cover Sheet, so you put “USR: PROVIDER,ONE” in the USER/DIVISION/SYSTEM column in Worksheet #3.
2. You have two options for where on the Cover Sheet tab to add the new panel.
    1. Option #1: In the lower-right corner of the Cover Sheet tab. In the SEQUENCE column in Worksheet #3, enter a whole number that does not already appear in the display output’s Instance column. This number should be greater than all the other values in the Instance column. Continuing the example for ONE PROVIDER, since 5 does not appear in the display output’s Instance column and 5 is greater than 1, 2, 3 and 4 for ONE PROVIDER, record 5 in the SEQUENCE column in Worksheet #3.
    2. Option #2: Somewhere other than the lower-right corner of the Cover Sheet tab. You will need to renumber all the panels to the right of and below the panel after which the Women’s Health panel should appear. In the SEQUENCE column in Worksheet #3, first record the Instance value of the panel that resides in the spot where you want to place the new panel. Then, copy that panel and the remaining list of panels into the SEQUENCE column and increase each panel’s Instance value by one.  Continuing the example for ONE PROVIDER, the Women’s Health panel should appear before the ORCV ACTIVE MEDICATIONS panel, so you will need to renumber the ORCV ACTIVE MEDICATIONS, ORCV CLINICAL REMINDERS and ORCV VITALS panels. Record “2; 3 ORCV MEDICATIONS; 4 ORCV CLINICAL REMINDRS; 5 ORCV VITALS” in the SEQUENCE column in Worksheet #3.

#### Register CPRS If Necessary

Note:	You may not need to do this step if your site does not use COM objects or if CPRS is already registered on the workstations.

**Client Technologies:** The Client Technologies group should perform this task.

If your site uses COM objects, you may need to register CPRS on the workstations on which CPRS is used at your site. During testing, several sites reported that they have experienced some issues running CPRS if they use COM objects. Registering CPRS on individual workstations has resolved these issues. CPRS may need to be registered on workstations even if CPRS is launched from a server.

Sites only need to do this if:

- Your site uses COM objects
- CPRS is not already registered on the workstation (This is more prevalent on newer machines but can be on older ones as well.)

Note:	Administrative Privileges are required to register CPRS.

Registering CPRS as a COM object can be done from the command line or from putting a parameter in the desktop icon’s properties.

Registering from the command line:

1. At the command line, type cprschart.exe -regserver and press &lt;Enter&gt;.

Registering from the desktop icon:

1. Create a new CPRS shortcut.
    1. Open the CPRS shortcut properties dialog.
    2. In the target field, enter the following parameter to register CPRS (where *path* represents where the executable is located, see example below): .\ *path* \CPRSChart.exe -REGSERVER
    1. Run the application from the icon.
    2. When CPRS has been registered, delete the new icon you created.

#### Confirm VistA FileMan Permission

**CAC/ITOPS** : This step is performed by the site’s CAC and/or the site’s assigned ITOPS VistA installer

The person responsible for completing section 3.2 Link Reminder Terms to Women’s Health Procedure Type Entries must have FileMan read/write access to the WV PROCEDURE TYPE file (#790.2). This person may be the site’s CAC, it may be the site’s ADPAC for Women’s Health (if the site is actively using the Women’s Health package) or it may be the assigned ITOPS VistA patch installer. All sites must identify who will complete section 3.2 in the post-install and verify that person can edit entries in the WV PROCEDURE TYPE file. If you cannot identify such a person, enter a Service Now ticket requesting the appropriate access.

## 4 Post-Installation Tasks

### Install Reminder Content

**Clinical Reminders Manager:** This step is performed by the site’s Clinical Reminders Manager.

The following two exchange file entries need to be installed:

PXRM*2.0*45 HI RISK MEDS CONTENT

PXRM*2.0*45 SMART CONTENT

Update to Dietetic Quick Orders

Update to Outpatient Meds Quick Orders

Update to Radiology Quick Orders

The task number for each of the above tasks is displayed during the installation of the CPRS V31B Required bundle of patches.

#### Install Women’s Health High Risk Medications Content

#### Install Women’s Health Mammography Tracking Content

1. Search and locate an entry titled PXRM*2.0*45 SMART CONTENT in reminder exchange.
<!-- image -->
    1. At the **Select Action:** prompt, enter **IFE** for Install Exchange File Entry.

## Note: 	You may receive multiple warnings that there are multiple RAD/NUC MED PROCEDURES and ORDERABLE ITEMS with the same name. You may safely ignore these warnings.

1. Enter the number that corresponds with your entry **PXRM*2.0*45 SMART CONTENT** (in this example, it is entry 29). It will vary by site. Make sure you select the exchange entry dated 02/04/2020@07:14.
<!-- image -->
2. At the Select Action prompt, enter **IA** for Install All Components.

The general rules for installation are as follows:

1. If a component does not exist (it is NEW), select the Install action.
2. If a component does exist (it is DIFFERENT), select the Overwrite the current entry action.
3. For the following reminder taxonomies, select the Skip, do not install this entry action:
    1. VA-MASTECTOMY
    2. VA-BREAST TUMOR
    3. VA-MAMMOGRAM/SCREEN
    4. VA-WH BILATERAL MASTECTOMY
    5. VA-TERMINAL CANCER PATIENTS

1. For the following reminder terms, select the Skip, do not install this entry action:
    1. VA-WH MAMMOGRAM ORDER
    2. VA-BL AGE&gt;74
    3. VA-WH BR CA 40-49 WANTS SCREENING
    4. VA-WH BILATERAL MASTECTOMY
    5. VA-TERMINAL CANCER PATIENT
    6. VA-WH MAMMOGRAM SCREEN IN WH PKG
    7. VA-WH MAMMOGRAM SCREEN IN RAD PKG
    8. VA-WH MAMMOGRAM SCREEN DONE
    9. VA-WH BREAST CARE ORDER HEALTH FACTOR
    10. VA-WH MAMMOGRAM SCREEN NOT INDICATED
    11. VA-WH MAMMOGRAM SCREEN DEFER
    12. VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG
    13. VA-WH MAMMOGRAM SCREEN FREQ - 4M
    14. VA-WH MAMMOGRAM SCREEN FREQ - 6M
    15. VA-WH MAMMOGRAM SCREEN FREQ - 1Y
    16. VA-WH MAMMOGRAM SCREEN FREQ - 2Y
    17. VA-WH HX BREAST CANCER/ABNORMAL MAM
    18. VA-WH MAMMOGRAM ORDER
    19. VA-WH BR CA 40-44 BEGIN AGE 45

At this point, the dialog installations begin.

You are prompted to install the FIRST reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH SMART PT NOTIFICATION.
2. At the **Install reminder dialog and all components with no further changes: Y//** prompt, enter **Yes**

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** to quit.

You are prompted to install the SECOND reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH SMART BREAST IMAGING FOLLOW-UP.
2. At the **Install reminder dialog and all components with no further changes: Y//** prompt, enter **Yes**

You are prompted for how you want to handle the non-existent finding Q. BREAST TREATMENT MENU.

1. At the **Enter response:** prompt, enter **P** for Replace with an existing entry.
2. At the **Select ORDER DIALOG NAME:** prompt, enter the name of the breast treatment order menu you identified or created in section 2.2.2.

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** to quit.

You are prompted to install the THIRD reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH SMART BR OUTSIDE REPORT.
2. At the **Install reminder dialog and all components with no further changes: Y//** prompt, enter **Yes**

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** to quit.

You are prompted to install the FOURTH reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH MAMMOGRAM SCREENING.
2. At the **Install reminder dialog and all components with no further changes: Y//** prompt, enter **Yes**

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** to quit.

You are then returned to the Exchange File Components screen.

<!-- image -->

1. At the **Select Action:** prompt, enter **Q** for Quit.

**Installation of the Women’s Health Mammography Tracking reminder content is now complete.**

### Link Reminder Terms to Women’s Health Procedure Type Entries

**CAC/ITOPS** : This step is performed either by the site’s CAC or the site’s ITOPS VistA installer, depending on who as FileMan read/write access to the WV PROCEDURE TYPE file (#790.2).

**Note:** Skip this section if the system (test or live) you are working in has a previous version of CPRS v31b installed.

1. In FileMan, select the **ENTER OR EDIT FILE ENTRIES [DIEDIT]** option.
2. At the Input to what File: prompt, select **790.2**
3. At the EDIT WHICH FIELD: prompt, select **Reminder Term** .
4. At the THEN EDIT FIELD: prompt, press the &lt;enter&gt; key.
5. Enter the Reminder Term value for the corresponding Women’s Health Procedure entries
| WV Procedure Type   | Reminder Term                           |
|---------------------|-----------------------------------------|
| BREAST MRI          | VA-WH MRI OF THE BREASTS CODES          |
| BREAST ULTRASOUND   | VA-WH ULTRASOUND OF THE BREAST CODES    |
| MAMMOGRAM DX BILAT  | VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES  |
| MAMMOGRAM DX UNILAT | VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES |
| MAMMOGRAM SCREENING | VA-WH MAMMOGRAM SCREENING CODES         |

Example

VA FileMan 22.2

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: IMAGING TYPE// 790.2  WV PROCEDURE TYPE

(31 entries)

EDIT WHICH FIELD: ALL// reminder term

THEN EDIT FIELD:

Select WV PROCEDURE TYPE: BREAST MRI

REMINDER TERM: VA-WH MRI OF THE BREASTS CODES       NATIONAL

...OK? Yes//   (Yes)

### Link Reminder Dialogs to Document Titles

**Reminder Manager/CAC** : This step is performed by the site’s clinical reminder manager or Clinical Applications Coordinator (CAC).

**Note:** Skip this section if the system (test or live) you are working in has a previous version of CPRS v31b installed.

From the Clinical Reminder Manager Menu, go to the CPRS Reminder Configuration menu, then go to the Link Reminder Dialog to Template option. Do the following for each reminder dialog using the table below:

1. At the Select Dialog Definition prompt, select one of the Reminder Dialogs from the template.
2. At the Enter template name prompt, enter a free text value.
3. At the Link template to Document Title prompt, select **Y.**
4. At the Select Document Definition prompt, select the corresponding TIU Note Title from the table below.
| Reminder Dialog                      | Template Name                      | Document Title                 |
|--------------------------------------|------------------------------------|--------------------------------|
| VA-WH SMART PT NOTIFICATION          | Patient Notification Follow-up     | SMART PATIENT NOTIFICATION     |
| VA-WH SMART BREAST IMAGING FOLLOW-UP | Breast Imaging Follow-up           | SMART BREAST IMAGING FOLLOW-UP |
| VA-WH UPDATE PREGNANCY STATUS        | Pregnancy/Intentions/Contraception | PREGNANCY STATUS UPDATE REVIEW |
| VA-WH UPDATE LACTATION STATUS        | Update Lactation Status            | LACTATION STATUS UPDATE REVIEW |

**Example: Linking a reminder dialog to a document title**

Select CPRS Reminder Configuration &lt;TEST ACCOUNT&gt; Option: LINK  Link Reminder Dialog to Template

Select Dialog Definition: VA-WH SMART PT NOTIFICATION       reminder dialog

NATIONAL

...OK? Yes//   (Yes)

Enter template name: Patient Notification Follow-up

Link template to Document Title? YES

Select Document Definition: SMART PATIENT NOTIFICATION       TITLE

Std Title: WOMENS HEALTH NOTE

Template Patient Notification Follow-up created

Template Patient Notification Follow-up added to Shared Folder.

Template Patient Notification Follow-up link to note title SMART PATIENT NOTIFICATION

### Clinical Reminder Mapping

**Reminder Manager/CAC:** A Reminder Manager or CAC should perform the tasks in this section.

#### Map Orderable Item(s) to the VA-WH PREGNANCY TEST ORDERED Term

Option: *Add/Edit Reminder Term* on the *Reminder Term Management* menu, which is on the *Reminder Managers Menu*

For every laboratory test you listed in the Laboratory Tests table in Worksheet #1 at the end of this document, add its corresponding orderable item as a finding to the VA-WH PREGNANCY TEST ORDERED term.

**Note** : It is critical that you prepend ‘OI.’ (without the quotes) before each laboratory test name at the Select Finding prompt. Again, you must enter the capital letter O, followed by the capital letter I, followed by a period, followed by the laboratory test name at the Select Finding prompt.

At the USE STATUS/COND IN SEARCH prompt, respond with YES. Also, ensure that the ACTIVE, COMPLETE and PENDING statuses are selected for each orderable item.

**Example: Mapping an orderable item to the national reminder term**

Select Reminder Term Management Option: TE  Add/Edit Reminder Term

Select Reminder Term: VA-WH PREGNANCY TEST ORDERED       NATIONAL

...OK? Yes//   (Yes)

Reminder Term has no findings!

Enter 'OI.' (without the quotes) followed by the laboratory test name.

<!-- image -->

Searching for a ORDERABLE ITEMS, (pointed-to by FINDING ITEM)

Searching for a ORDERABLE ITEMS

1   HCG

2   HCG BETA, QUANT.

CHOOSE 1-2: 1  HCG

Are you adding 'HCG' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// YES  (Yes)

Editing Finding Number: 1

FINDING ITEM: HCG//

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

USE START DATE:

CONDITION:

CONDITION CASE SENSITIVE:

USE STATUS/COND IN SEARCH: YES  YES

No statuses defined for this finding item

Select one of the following:

A         ADD STATUS

D         DELETE A STATUS

S         SAVE AND QUIT

Q         QUIT WITHOUT SAVING CHANGES

Enter response: S// ADD STATUS

1 - * (WildCard)

2 - ACTIVE

3 - CANCELLED

4 - COMPLETE

5 - DELAYED

6 - DISCONTINUED

7 - DISCONTINUED/EDIT

8 - EXPIRED

9 - FLAGGED

10 - HOLD

11 - LAPSED

12 - NO STATUS

13 - PARTIAL RESULTS

14 - PENDING

15 - RENEWED

16 - SCHEDULED

17 - UNRELEASED

Select a Order Status from or enter '^' to Quit:  (1-17): 2,4,14

Statuses already defined for this finding item:

ACTIVE

COMPLETE

PENDING

Select one of the following:

A         ADD STATUS

D         DELETE A STATUS

S         SAVE AND QUIT

Q         QUIT WITHOUT SAVING CHANGES

Enter response: S// AVE AND QUIT

Choose from:

OI HCG                                                          Finding #   1

Select Finding:

#### Map Laboratory Test(s) to Terms

Option: *Add/Edit Reminder Term* on the *Reminder Term Management* menu, which is on the *Reminder Managers Menu*

For every laboratory test listed in the Patient is Pregnant Condition Statements table in Worksheet #1 at the end of this document, add it as a finding to the VA-WH POSITIVE LAB PREGNANCY TEST term. Then, for every laboratory test listed in the Patient is Not Pregnant Condition Statements table in Worksheet #1, add it as a finding to the VA-WH NEGATIVE LAB PREGNANCY TEST term.

**Note:** It is critical that you prepend ‘LT.’ (without the quotes) before each laboratory test name at the Select Finding prompt. Again, you must enter the capital letter L, followed by the capital letter T followed by a period, followed by the laboratory test name at the Select Finding prompt.

Use the following table to answer various prompts that will appear when you add the test(s) to the terms. If a prompt is not listed in the table, leave it blank.

| **Field**                 | **Value**                                                                                  |
|---------------------------|--------------------------------------------------------------------------------------------|
| OCCURRENCE COUNT          | 1                                                                                          |
| CONDITION                 | CONDITION column in the appropriate table in Worksheet 1 at the end of this document.      |
| CONDITION CASE SENSITIVE: | CASE SENSITIVE column in the appropriate table in Worksheet 1 at the end of this document. |
| USE STATUS/COND IN SEARCH | YES                                                                                        |

**Example: Mapping a laboratory test to the national reminder term**

Select Reminder Term Management Option: TE  Add/Edit Reminder Term

Select Reminder Term: VA-WH POSITIVE LAB PREGNANCY TEST       NATIONAL

...OK? Yes//   (Yes)

Reminder Term has no findings!

Enter 'LT.' (without the quotes) followed by the laboratory test name.

<!-- image -->

Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM)

Searching for a LABORATORY TEST

1   HCG

2   HCG BETA, QUANT.

CHOOSE 1-2: 1  HCG

Are you adding 'HCG' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// YES

(Yes)

Editing Finding Number: 1

FINDING ITEM: HCG//

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT: 1

CONDITION: I V["POS"

CONDITION CASE SENSITIVE: NO  NO

USE STATUS/COND IN SEARCH: YES  YES

Choose from:

LT HCG                                                          Finding #   1

Select Finding:

#### Map Radiology Parent Procedure(s) to Terms

Options: *Add/Edit Reminder Term* on the *Reminder Term Management* menu and *Reminder Taxonomy Management* , both of which are on the *Reminder Managers Menu*

1. Determine which term to map your site’s parent procedures to. Execute the Code Search command within the option Reminder Taxonomy Management for every descendent CPT code listed in the Radiology Parent Procedures table in Worksheet #2 at the end of this document. In the TAXONOMY NAME column in that table, enter the name of the taxonomy containing that CPT code. Only record those names that appear in the list below:
    - VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
    - VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
    - VA-WH MRI BREAST PROCEDURE CODES
    - VA-WH ULTRASOUND BREAST PROCEDURE CODES
    - VA-WH MAMMOGRAM SCREENING CODES
Note that the terms you will map to have the same name as the taxonomies that you identify in this step.
**Example: Searching reminder taxonomies for a CPT code****Taxonomy Management** Jan 08, 2020@11:43:33          Page:    1 of   45
Taxonomy File Entries.No. Taxonomy                        Description \_
1 GP IM PNEUMOC PCV13 PREVNAR     This taxonomy was automatically gener...
2 GP IM PNEUMOC PPSV23 PNEUMOVAX  This taxonomy was automatically gener...
3 HF LIPID LDL 120-129            This taxonomy was automatically gener...
4 HF LIPID LDL 71-99              This taxonomy was automatically gener...
5 HF LIPID LDL &gt;190               This taxonomy was automatically gener...
6 PALLI CONS DYSPNEA MILD (E)     This taxonomy was automatically gener...
7 PALLI CONS DYSPNEA SEVERE (E)   This taxonomy was automatically gener...
8 PALLI CONS INPT 99251 (E)       This taxonomy was automatically gener...
9 PALLI CONS INPT 99252 (E)       This taxonomy was automatically gener...
10 PALLI CONS INPT 99253 (E)       This taxonomy was automatically gener...
+         + Next Screen   - Prev Screen   ?? More Actions                     \_
ADD  Add                                CL   Change Log
EDIT Edit                               CS   Code Search
UIDE UID Edit                           IMP  Import
COPY Copy                               UIDR UID report
INQ  Inquire                            VSC  VS Compare
Select Action: Next Screen// CS   Code Search
Input a code to search for: 77067
Searching for CPT-4 code 77067
CPT-4 77067 is used in the following taxonomies:
VA-MAMMOGRAM/SCREEN
VA-WH MAMMOGRAM SCREENING CODES
Input a code to search for:
    1. For every radiology procedure you listed in the Radiology Parent Procedures table in Worksheet #2 at the end of this document, add it as a finding to the reminder term with the same name as the taxonomy name you listed in that table.**Note:** It is critical that you prepend ‘RP.’ (without the quotes) before each radiology procedure name at the Select Finding prompt. Again, you must enter the capital letter R, followed by the capital letter P followed by a period, followed by the radiology procedure name at the Select Finding prompt.
Leave all prompts that appear blank.
**Example: Mapping a radiology procedure to the national reminder term**
Select Reminder Term Management Option: TE  Add/Edit Reminder Term
Select Reminder Term: VA-WH MAMMOGRAM SCREENING CODES       NATIONAL
...OK? Yes//   (Yes)
Choose from:
TX VA-WH MAMMOGRAM SCREENING CODES                              Finding #   1
Enter ‘RP.’ (without the quotes) followed by the radiology procedure name.
<!-- image -->
Select Finding: Select Finding: RP.P/D SCREEN MAMMOGRAM, BILAT
Searching for a RAD/NUC MED PROCEDURES, (pointed-to by FINDING ITEM)
Searching for a RAD/NUC MED PROCEDURES
P/D SCREEN MAMMOGRAM, BILAT                                 (MAM  Parent  )
...OK? Yes//   (Yes)
Are you adding P/D SCREEN MAMMOGRAM, BILAT' as a new FINDINGS? No// YES  (Yes)
Editing Finding Number: 2
FINDING ITEM: P/D SCREEN MAMMOGRAM, BILAT//
BEGINNING DATE/TIME:
ENDING DATE/TIME:
OCCURRENCE COUNT:
CONDITION:
CONDITION CASE SENSITIVE:
USE STATUS/COND IN SEARCH:
No statuses defined for this finding item
Select one of the following:
A         ADD STATUS
D         DELETE A STATUS
S         SAVE AND QUIT
Q         QUIT WITHOUT SAVING CHANGES
Enter response: S// QUIT WITHOUT SAVING CHANGES
Choose from:
RP P/D SCREEN MAMMOGRAM, BILAT                                  Finding #   2
TX VA-WH MAMMOGRAM SCREENING CODES                              Finding #   1
Select Finding:

#### Map Orderable Items to the VA-PENDING BREAST IMAGING ORDERS Term

Option: *Add/Edit Reminder Term* on the *Reminder Term Management* menu, which is on the *Reminder Managers Menu*

For every radiology procedure you listed in both the Radiology Parent Procedures and Radiology Detailed and Series Procedures tables in Worksheet #2 at the end of this document, add its corresponding orderable item as a finding to the VA-PENDING BREAST IMAGING ORDERS term.

**Note** : It is critical that you prepend ‘OI.’ (without the quotes) before each radiology procedure name at the Select Finding prompt. Again, you must enter the capital letter O, followed by the capital letter I, followed by a period, followed by the radiology procedure name at the Select Finding prompt.

At the USE STATUS/COND IN SEARCH prompt, respond with YES. Also, ensure that the ACTIVE and PENDING statuses are selected for each orderable item.

#### Update Reminder Term Condition Statement

Option: *Add/Edit Reminder Term* on the *Reminder Term Management* menu, which is on the *Reminder Managers Menu*

Change the condition statement for Reminder Term VA-WH NEXT BREAST PROCEDURE from

I V("Procedure")="Mammogram, Screening" to I V("Procedure")["Mammogram"

**Example: Editing the Reminder Term Condition Statement**

Select Reminder Term Management &lt;TEST ACCOUNT&gt; Option: TE  Add/Edit Reminder Ter

m

Select Reminder Term: VA-WH NEXT BREAST PROCEDURE       NATIONAL

...OK? Yes//   (Yes)

Choose from:

CF VA-WH NEXT PROCEDURE                                         Finding #   1

Select Finding: `1  VA-WH NEXT PROCEDURE

Computed Finding Description:

This computed finding returns the Next Procedure Name and the Next

Procedure Date from the Women's Health Patient File. This computed

finding will either return information related to the Breast or the

Cervical treatments based off the Computed Finding Parameter.

Computer Parameter

BR: Breast Procedure

CX: Cervical Procedure

Return Value

DATA("Procedure")=the name of the appropriate next treatment need field

Editing Finding Number: 1

FINDING ITEM: VA-WH NEXT PROCEDURE//

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

COMPUTED FINDING PARAMETER: BR//

CONDITION: I V("Procedure")="Mammogram, Screening"

Replace ="Mammogram, Screening" With ["Mammogram"

Replace

I V("Procedure")["Mammogram"

CONDITION CASE SENSITIVE:

USE STATUS/COND IN SEARCH:

Choose from:

CF VA-WH NEXT PROCEDURE                                         Finding #   1

Select Finding:

### Re-Index Reminder Order Check Items Group File

**ITOPS:** This step is performed by the site’s local/regional OI&amp;T support.

All indices in the REMINDER ORDER CHECK ITEMS GROUP file (#801) should be rebuilt. Use option *Re-Index File,* which is on the *Utility Functions* menu. That menu is on the *VA FileMan* menu option. You must wait for the site to complete section 3.1 Reminder Content Installation before completing this section.

**Example: Re-Indexing File #801**

Select UTILITY OPTION: RE-INDEX FILE

Modify what File: OPTION// 801  REMINDER ORDER CHECK ITEMS GROUP

(15 entries)

THERE ARE 10 INDICES WITHIN THIS FILE

DO YOU WISH TO RE-CROSS-REFERENCE ONE PARTICULAR INDEX? No//   (No)

OK, ARE YOU SURE YOU WANT TO KILL OFF THE EXISTING 10 INDICES? No// YES  (Yes)

DO YOU THEN WANT TO 'RE-CROSS-REFERENCE'? Yes//   (Yes)

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

FILE WILL NOW BE 'RE-CROSS-REFERENCED'........

Select UTILITY OPTION:

### Update Reminder General Findings

**ITOPS:** This step is performed by the site’s local/regional OI&amp;T support.

Change the value in the VALUE field for the general findings in the table below. Use option *Enter or Edit File Entries* , which is on the *VA FileMan* menu option to change the VALUE field’s value. You must wait for the site to complete section 3.1 Reminder Content Installation before completing this section.

| **General Finding**                 | **New VALUE Field Value**             |
|-------------------------------------|---------------------------------------|
| BR BIRAD 1, RETURN TO AGE SCREENING | BR BIRAD 1, next MAM AGE AT START AGE |
| BR BIRAD 2, RETURN TO AGE SCREENING | BR BIRAD 2, next MAM AGE AT START AGE |

**Example: Editing General Findings**

Select VA FileMan &lt;TEST ACCOUNT&gt; Option: ENTER or Edit File Entries

Input to what File: INSTALL// REMINDER GENERAL FINDINGS

(246 entries)

EDIT WHICH FIELD: ALL// VALUE

1   VALUE

2   VALUE FIEVAL SUBSCRIPT

3   VALUE SUBSCRIPT

CHOOSE 1-3: 1  VALUE

THEN EDIT FIELD:

Select REMINDER GENERAL FINDINGS FINDING TEXT: BR BIRAD 1, RETURN TO AGE SCREENING

WOMEN'S HEALTH

VALUE: BR BIRAD 1, RETURN TO AGE SCREENING  Replace ... With BR BIRAD 1, next MAM AGE AT START AGE

Replace

BR BIRAD 1, next MAM AGE AT START AGE

Select REMINDER GENERAL FINDINGS FINDING TEXT: BR BIRAD 2, RETURN TO AGE SCREENING

WOMEN'S HEALTH

VALUE: BR BIRAD 2, RETURN TO AGE SCREENING  Replace ... With BR BIRAD 2, next MAM AGE AT START AGE

Replace

BR BIRAD 2, next MAM AGE AT START AGE

Select REMINDER GENERAL FINDINGS FINDING TEXT:

### Enable Clinical Reminder Order Check Rules

**Clinical Reminder Manager:** This step is performed by the Clinical Reminder Manager.

Several new clinical reminder order check rules are included in this release of CPRS. These order check rules are distributed in an inactive state. Sites must activate the following order check rules:

- VA-WH HIRISK IMAGING (MRI) PREG RULE
- VA-WH HIRISK IMAGING (NON MRI) PREG RULE
- VA-WH HIRISK MEDS (EXTREME RISK) NO PREG DOC RULE
- VA-WH HIRISK MEDS (EXTREME RISK) NOT PREG RULE
- VA-WH HIRISK MEDS (EXTREME RISK) PREG RULE
- VA-WH HIRISK MEDS (LACT 1) EXPIRED DOC RULE
- VA-WH HIRISK MEDS (LACT 1) RULE
- VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE
- VA-WH HIRISK MEDS (LACT 2) RULE
- VA-WH HIRISK MEDS (MODERATE/HIGH RISK) NO PREG DOC RULE
- VA-WH HIRISK MEDS (MODERATE/HIGH RISK) NOT PREG RULE
- VA-WH HIRISK MEDS (MODERATE/HIGH RISK) PREG RULE

Use option *Add/Edit Reminder Order Check Rule* on the *Reminder Order Check Menu* , which is on the *Reminder Managers Menu* option to activate each of the above rules.

**Example: Activating a Clinical Reminder Order Check Rule**

Select Reminder Order Check Rule by one of the following:

N:  ORDER CHECK RULE NAME

R:  REMINDER DEFINITION

T:  REMINDER TERM

Q:  QUIT

Select Reminder Order Check Rule by:  (N/R/T/Q): N//   ORDER CHECK RULE NAME

Select Reminder Order Check Rule: VA-WH HIRISK IMAGING (MRI) PREG RULE

RULE NAME: VA-WH HIRISK IMAGING (MRI) PREG RULE

DISPLAY NAME: Known or Potential Teratogen (MR Study)

STATUS: P

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

I=INACTIVE, P=PRODUCTION, T=TESTING

Press &lt;PF1&gt;H for help  Insert

RULE NAME: VA-WH HIRISK IMAGING (MRI) PREG RULE

DISPLAY NAME: Known or Potential Teratogen (MR Study)

STATUS: PROD

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: S                                       Press &lt;PF1&gt;H for help  Insert

RULE NAME: VA-WH HIRISK IMAGING (MRI) PREG RULE

DISPLAY NAME: Known or Potential Teratogen (MR Study)

STATUS: PROD

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E                                       Press &lt;PF1&gt;H for help  Insert

Edit History

Edit by: ADPAC,ONE on 01/13/2020@09:40:03

Press the Enter key.

<!-- image -->

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press enter to add a description of the changes made.

Press &lt;PF1&gt;H for help  Insert

==[ WRAP ]==[INSERT ]=============&lt; EDIT COMMENTS &gt;==[Press &lt;PF1&gt;H for help]===

Changed the rule's status to production.

After entering your comment, press the keyboard key that is mapped to PF1 (usually the NUM LOCK key on the key pad) then press the E key to exit the text editor.

<!-- image -->

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;=====

Edit History

Edit by: ADPAC,ONE on 01/13/2020@09:40:03

EDIT COMMENTS: Changed the rule's status to active.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E                                       Press &lt;PF1&gt;H for help  Insert

### Inactivate a New Note Title

**CAC** : This step is performed by the site’s Clinical Application Coordinators (CACs).

Option: *Edit Document Definitions* on the *Document Definitions (Manager)* menu, which is on the *TIU Maintenance Menu* .

A new note title, SMART OUTSIDE BREAST IMAGE RESULTS, is no longer needed for the mammography tracking enhancements to function correctly. Sites should inactivate this note title using the *Edit Document Definitions* option [TIUFH EDIT DDEFS MGR].

**Example: Inactivating a Note Title**

**Edit Document Definitions** Jul 08, 2020@05:01:17          Page:    1 of    1

BASICS

Name                                                                Type

1      CLINICAL DOCUMENTS                                                   CL

2       +PROGRESS NOTES                                                     CL

3       +ADDENDUM                                                           DC

4       +DISCHARGE SUMMARY                                                  CL

5       +CLINICAL PROCEDURES                                                CL

6       +LR LABORATORY REPORTS                                              CL

7       +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit    Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                Delete

Boilerplate Text          Name/Owner/PrintName...  Copy/Move

Select Action: Quit// Jump   Jump to Document Def

Select TIU DOCUMENT DEFINITION NAME: SMART OUTSIDE BREAST IMAGE RESULTS       TITLE

Std Title: WOMENS HEALTH NOTE.............................................

**Edit Document Definitions** Jul 08, 2020@05:02:07          Page:    3 of    4

BASICS

+      Name                                                                Type

41           SMART OUTSIDE BREAST IMAGE RESULTS                             TL

42        +WOMEN'S HEALTH NOTES                                             DC

43      +ADDENDUM                                                           DC

44      +DISCHARGE SUMMARY                                                  CL

45      +CLINICAL PROCEDURES                                                CL

46      +LR LABORATORY REPORTS                                              CL

47      +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit    Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                Delete

Boilerplate Text          Name/Owner/PrintName...  Copy/Move

Select Action: Quit// Detailed   Detailed Display/Edit

Enter the number from the list of definitions that corresponds to the SMART OUTSIDE BREAST IMAGE RESULTS title at this prompt. Your number may not match the number in this example.

<!-- image -->

Entry is National; Limited Actions

Press RETURN to continue or '^' or '^^' to exit:

Basics                    (Technical Fields)        Find

**Detailed Display** Jul 08, 2020@05:02:30          Page:    1 of    3

Title SMART OUTSIDE BREAST IMAGE RESULTS

\_

Basics            Note: Values preceded by * have been inherited

Name:   SMART OUTSIDE BREAST IMAGE RESULTS

VHA Enterprise

Standard Title:   WOMENS HEALTH NOTE

Abbreviation:

Print Name:   SMART OUTSIDE BREAST IMAGE RESULTS

Type:   TITLE

IFN:   3532

National

Standard:   YES

Status:   ACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection: * NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Items: Seq Mnem MenuTxt   Edit Upload               Quit

Boilerplate Text          Try

Select Action: Next Screen// Basics   Basics

Edit Abbreviation and Status only: Entry is National Title.

ABBREVIATION:

STATUS: (A/I/T): ACTIVE// INACTIVE

Entry (&amp; any nonShared Components) Inactivated

**Detailed Display** Jul 08, 2020@05:02:53          Page:    1 of    3

Title SMART OUTSIDE BREAST IMAGE RESULTS

Basics            Note: Values preceded by * have been inherited

Name:   SMART OUTSIDE BREAST IMAGE RESULTS

VHA Enterprise

Standard Title:   WOMENS HEALTH NOTE

Abbreviation:

Print Name:   SMART OUTSIDE BREAST IMAGE RESULTS

Type:   TITLE

IFN:   3532

National

Standard:   YES

Status:   INACTIVE

Owner:   CLINICAL COORDINATOR

In Use:   NO

Suppress Visit

Selection: * NO

+         ? Help       +, - Next, Previous Screen     PS/PL

Basics                    (Technical Fields)        Find

Items: Seq Mnem MenuTxt   Edit Upload               Quit

Boilerplate Text          Try

Select Action: Next Screen// Quit

**Edit Document Definitions** Jul 08, 2020@05:03:34          Page:    3 of    4

BASICS

+      Name                                                                Type

41           SMART OUTSIDE BREAST IMAGE RESULTS                             TL

42        +WOMEN'S HEALTH NOTES                                             DC

43      +ADDENDUM                                                           DC

44      +DISCHARGE SUMMARY                                                  CL

45      +CLINICAL PROCEDURES                                                CL

46      +LR LABORATORY REPORTS                                              CL

47      +SURGICAL REPORTS                                                   CL

?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-                 &gt;&gt;&gt;

Expand/Collapse           Detailed Display/Edit    Items: Seq Mnem MenuTxt

Jump to Document Def      Status...                Delete

Boilerplate Text          Name/Owner/PrintName...  Copy/Move

Select Action: Quit//

### Configure Women’s Health Site Parameters

**Women’s Health ADPAC/CAC:** This step is performed by the ADPAC for the Women’s Health package or designee in coordination with the site’s Clinical Applications Coordinators (CACs).

The Women’s Health package may not be used at some sites, so the Women’s Health ADPAC or designee may need assistance with this section from the CACs. The Women’s Health ADPAC or designee will need access to the *Manager’s Functions* menu option [WV MENU-MANAGER'S FUNCTIONS] to complete this section and the next section.

Before providers can document a patient’s pregnancy and lactation status or utilize the new mammography results tracker, the site must have a minimally configured entry in the WV SITE PARAMETER file (#790.02). Configuring an entry does not mean that sites must start using the Women’s Health package. Use of this package is still optional, however, a minimally configured entry in the WV SITE PARAMETER file is required.

Creating or updating an entry in the WV SITE PARAMETER file is a two-step process. The first step is to designate an active user as a Women’s Health Case Manager. The second step is to create and/or update an entry in the WV SITE PARAMETER file.

#### Step 1: Designate a Case Manager

Option: *Add/Edit Case Managers* on the *File Maintenance Menu* , which is on the *Manager's Functions* menu.

At least one active user must be designated as a default case manager. An active user is a user that can log onto VistA, is someone who works in women’s health, and is responsible for coordinating and managing female-specific care for female patients. A default case manager is the case manager that is assigned to new patients when the user adding the patient to the Women’s Health package does not specify a case manager for that patient.

For multidivisional sites, you may choose to use the same user as a default case manager for all divisions or choose to use a different user as a default case manager for each division. If you choose to use a different user, you will need to repeat this step for each user that you need to designate as a default case manager.

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *                  SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: FM  File Maintenance Menu

<!-- image -->

<!-- image -->

**Example (continued): Designating a Women’s Health Case Manager**

* * *  WOMEN'S HEALTH: ADD/EDIT CASE MANAGERS  * * *

Select CASE MANAGER: ??

Choose from:

TESTMASTER,USER

You may enter a new WV CASE MANAGER, if you wish

This field contains the name(s) of WH case manager(s) assigned to manage

women's health needs.

Choose from:

ADPAC,ONE        OA          ADPAC

ANRVAPPLICATION,PROXY USER

AUTHORIZER,IB MRA        MRA

AUTHORIZER,IB REG

AUTOUPDATE,IBEIV        MRA

CENTRAL,PAID

CLINICAL,DEVICE PROXY SERVICE

CREDENTIALCLERK,ONE        OC          CREDENTIALLING CLERK

EDILOCKBOX,AUTOMATIC        EDI

EDPTRACKING,PROXY

Type &lt;Enter&gt; to continue or '^' to exit: ^

<!-- image -->

If the Choose from list contains an active user and that user should be the default case manager for all new patients, then note that person’s name.

If the Choose from list does not contain any users or all the users listed are no longer active, then designate an active user as a case manager:

<!-- image -->

#### Step 2: Create/Update a WV SITE PARAMETER File Entry

Option: *Edit Site Parameters* on the *File Maintenance Menu* , which is on the *Manager's Functions* menu.

Each site must have a minimally configured entry in the WV SITE PARAMETER file. For multidivisional sites, each division must have its own minimally configured entry. You will need to repeat this step for each active division setup on the VistA system.

Each entry should have the following fields set:

- Default Case Manager (value was identified in step #1)
- Update Result/Dx Field? (value should be YES)
- Update Treatment Needs? (value should be YES)
- Import Mammograms from Radiology (value should be YES)
- Status Given to Imported Mammograms (value should be OPEN)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

**Note:** For multi-divisional sites, each division should have its own entry.

**Example (continued): Adding a site parameter entry in the Women’s Health package**

If this field does not contain the name of an active user, enter the name of the user you identified or designated in step #1.

* * *  EDIT SITE PARAMETERS FOR **SAMPLE VAMC** * * *

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Default Case Manager: WHCOORDINATOR,ONE**

**Ask Case Manager:**

Autoqueue Normal PAP Letters:

PAP Result Normal Letter:

Autoqueue Normal MAM Letters:

MAM Result Normal Letter:

Default #days to print letter:

Update Result/Dx Field?: YES

Update Treatment Needs?: YES

(PAGE 1 OF 7)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Next Page     Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: N                                     Press &lt;PF1&gt;H for help    Insert

<!-- image -->

These fields are not required.

<!-- image -->

These fields are required and should be set to YES.

<!-- image -->

<!-- image -->

**Example (continued): Adding a site parameter entry in the Women’s Health package**

<!-- image -->

These fields are required and should be set to the values shown here.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

These fields are not required.

<!-- image -->

* * *  EDIT SITE PARAMETERS FOR **SAMPLE VAMC** * * *

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RADIOLOGY:  Import Mammograms from Radiology: **YES**

Status Given to Imported Mammograms: **OPEN**

**Include ALL Non-Veterans(Y/N)?:**

**ELIGIBILITY CODE(S):**

**LABORATORY: Import Tests from Laboratory:**

**Include ALL Non-Veterans(Y/N)?:**

**ELIGIBILITY CODE(S):**

(PAGE 2 OF 7)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Next Page    Previous Page    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: **N                                      Press &lt;PF1&gt;H for help  Insert**

<!-- image -->

Continue entering the N command to move to the next page until you arrive at the last page, number seven.

**Example (continued): Adding a site parameter entry in the Women’s Health package**

* * *  EDIT SITE PARAMETERS FOR **CAMP MASTER** * * *

-----------------------------------------------------------------------------

Default reasons why pregnancy or lactation status data was entered in error:

<!-- image -->

<!-- image -->

----------  --------------------------------------------------

**1        SAMPLE 1**

**2        SAMPLE 2**

TIU Ancillary Data Message:

<!-- image -->

(PAGE 7 OF 7)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter the site’s/division’s message text from section 2.2.5 here; this field is not required.

<!-- image -->

COMMAND: S **Press &lt;PF1&gt;H for help  Insert**

* * *  EDIT SITE PARAMETERS FOR **CAMP MASTER** * * *

-------------------------------------------------------------------------------

Default reasons why pregnancy or lactation status data was entered in error:

Sequence #  Reason

----------  --------------------------------------------------

TIU Ancillary Data Message:

(PAGE 7 OF 7)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: E **Press &lt;PF1&gt;H for help  Insert**

**Example (continued): Adding a site parameter entry in the Women’s Health package**

Select OPTION NAME: WOMEN'S HEALTH MENU  WVMENU     Women's Health Menu

Women's Health Main Menu v1.0                       CAMP MASTER

PM     Patient Management ...

MR     Management Reports ...

MF     Manager's Functions ...

&lt;CPM&gt; Select Women's Health Menu &lt;ONEBCE&gt; Option: MAN

1    Management Reports

2    Manager's Functions

CHOOSE 1-2: 2  Manager's Functions

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         CAMP MASTER

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

&lt;CPM&gt; Select Manager's Functions &lt;ONEBCE&gt; Option: FILE Maintenance Menu

WOMEN'S HEALTH:       *  FILE MAINTENANCE MENU  *        CAMP MASTER

AEP    Add/Edit a Notification Purpose &amp; Letter

PPL    Print Notification Purpose &amp; Letter File

ESN    Edit Synonyms for Notification Types

OUT    Add/Edit Notification Outcomes

ESP    Edit Site Parameters

EPP    Edit Package Parameters

CM     Add/Edit Case Managers

MCC    Add/Edit Maternity Care Coordinators

TRCM   Transfer a Case Manager's Patients

TRMC   Transfer a Maternity Care Coordinator's Patients

AUTO   Automatically Load Patients

RAD    Import Radiology/NM Exams

PRD    Print Results/Diagnosis File

ESR    Edit Synonyms for Results/Diagnoses

PSR    Print Synonyms for Results/Diagnoses

EDX    Edit Diagnostic Code Translation File

PDX    Print Diagnostic Code Translation File

RS     Add/Edit to Referral Source File

PAP    Link Pap Smear with SNOMED Codes

&lt;CPM&gt; Select File Maintenance Menu &lt;ONEBCE&gt; Option: EPP  Edit Package Parameters

CPRS Parameters for Package: WOMEN'S HEALTH

------------------------------------------------------------------------------

Cover Sheet Websites         U. S. MEC for Contraceptive Use http://www.cdc.gov

/reproductivehealth/unintendedpregnancy/usmec.htm

This field is not required.

<!-- image -->

<!-- image -->

------------------------------------------------------------------------------

For  Cover Sheet Websites -

Select Hyperlink Name:

### Review Users in the Women’s Health Package

**Women’s Health ADPAC/CAC:** This step is performed by the ADPAC for the Women’s Health package or designee in coordination with the site’s Clinical Applications Coordinators (CACs).

Three new notifications are introduced with this release of CPRS v31b: pregnancy status conflict, lactation status conflict and pregnancy/lactation status review. The status conflict notifications are generated when either a diagnosis code is added to the patient’s chart or when a pregnancy laboratory test is resulted indicating a pregnancy or lactation status that is different from what is stored in the Women’s Health package. The status review notification is generated when a signed note that is associated with pregnancy or lactation status data is retracted from the patient’s medical record. Women’s Health case managers, along with maternity care coordinators and for the status conflict notifications in certain critical situations the patient’s primary care provider are recipients of these notifications.

Ensuring the proper users receive these notifications is a five step process: review the list of case managers and update as needed, transfer patients from inactive case managers to active case managers as needed, assign new case managers to patients, designate users as a maternity care coordinator and assign maternity care coordinators to patients. This is an ongoing process that should repeat whenever there is a change in staff. Not documented here is an option to transfer patients from one maternity care coordinator to another maternity care coordinator; refer to the Women’s Health User Guide for how to use this option.

#### Step 1: Review and Update the List of Case Managers

Option: *Add/Edit Case Managers* on the *File Maintenance Menu* , which is on the *Manager's Functions* menu.

Before assigning a user as a patient’s case manager, that user must be designated as a case manager in the Women’s Health package. Additionally, users who are no longer case managers should be inactivated.

**Example: Reviewing the List of Women’s Health Case Managers**

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: FM  File Maintenance Menu

WOMEN'S HEALTH:       *  FILE MAINTENANCE MENU  *        WEST PALM BEACH VAMC

AEP    Add/Edit a Notification Purpose &amp; Letter

PPL    Print Notification Purpose &amp; Letter File

ESN    Edit Synonyms for Notification Types

OUT    Add/Edit Notification Outcomes

ESP    Edit Site Parameters

EPP    Edit Package Parameters

CM     Add/Edit Case Managers

MCC    Add/Edit Maternity Care Coordinators

TRCM   Transfer a Case Manager's Patients

TRMC   Transfer a Maternity Care Coordinator's Patients

AUTO   Automatically Load Patients

RAD    Import Radiology/NM Exams

PRD    Print Results/Diagnosis File

ESR    Edit Synonyms for Results/Diagnoses

PSR    Print Synonyms for Results/Diagnoses

EDX    Edit Diagnostic Code Translation File

PDX    Print Diagnostic Code Translation File

RS     Add/Edit to Referral Source File

PAP    Link Pap Smear with SNOMED Codes

Select File Maintenance Menu &lt;TEST ACCOUNT&gt; Option: CM  Add/Edit Case Managers

**Example (continued): Reviewing the List of Women’s Health Case Managers**

* * *  WOMEN'S HEALTH: ADD/EDIT CASE MANAGERS  * * *

Select CASE MANAGER: ??

Choose from:

TESTMASTER,USER              DATE INACTIVATED:  FEB 18, 2020

WHCOORDINATOR,ONE

WHCOORDINATOR,TWO

You may enter a new WV CASE MANAGER, if you wish

This field contains the name(s) of WH case manager(s) assigned to manage

women's health needs.

Choose from:

ADPAC,ONE        OA          ADPAC

ANESTHESIOLOGIST,ONE        OA          ANESTHESIOLOGIST

ANRVAPPLICATION,PROXY USER

AUTHORIZER,IB MRA        MRA

AUTHORIZER,IB REG

AUTOUPDATE,IBEIV        MRA

CENTRAL,PAID

CLINICAL,DEVICE PROXY SERVICE

CREDENTIALCLERK,ONE        OC          CREDENTIALLING CLERK

DEPARTMENT OF DEFENSE,USER        UDOD

Type &lt;Enter&gt; to continue or '^' to exit: ^

Select CASE MANAGER:

The current list of case managers appears before the text “You may enter a new WV CASE MANAGER, if you wish”. Those users that are no longer case managers have the text “DATE INACTIVATED” next to their name.

At the Select CASE MANAGER prompt, you can select a user to inactivate or designate as a new case manager.

**Example: Inactivating a Women’s Health Case Manager**

Select CASE MANAGER: WHCOORDINATOR,ONE       OW          PHYSICIAN

...OK? Yes//   (Yes)

DATE INACTIVATED: T  (FEB 18, 2020)

**Example: Designating a Women’s Health Case Manager**

* * *  WOMEN'S HEALTH: ADD/EDIT CASE MANAGERS  * * *

Select CASE MANAGER: WHCOORDINATOR,THREE       TW          PHYSICIAN

Are you adding 'WHCOORDINATOR,THREE' as a new WV CASE MANAGER (the 4TH)? No// YES  (Yes)

DATE INACTIVATED:

#### Step 2: Transfer Inactive Case Managers’ Patients

Option: *Transfer a Case Manager's Patients* on the *File Maintenance Menu* , which is on the *Manager's Functions* menu.

If any Women’s Health case manager was inactivated in step one, the patients assigned to that manager must be transferred to an active Women’s Health case manager.

**Example: Transferring a Case Manager’s Patients**

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: FM  File Maintenance Menu

WOMEN'S HEALTH:       *  FILE MAINTENANCE MENU  *        SAMPLE VAMC

AEP    Add/Edit a Notification Purpose &amp; Letter

PPL    Print Notification Purpose &amp; Letter File

ESN    Edit Synonyms for Notification Types

OUT    Add/Edit Notification Outcomes

ESP    Edit Site Parameters

EPP    Edit Package Parameters

CM     Add/Edit Case Managers

MCC    Add/Edit Maternity Care Coordinators

TRCM   Transfer a Case Manager's Patients

TRMC   Transfer a Maternity Care Coordinator's Patients

AUTO   Automatically Load Patients

RAD    Import Radiology/NM Exams

PRD    Print Results/Diagnosis File

ESR    Edit Synonyms for Results/Diagnoses

PSR    Print Synonyms for Results/Diagnoses

EDX    Edit Diagnostic Code Translation File

PDX    Print Diagnostic Code Translation File

RS     Add/Edit to Referral Source File

PAP    Link Pap Smear with SNOMED Codes

Select File Maintenance Menu &lt;TEST ACCOUNT&gt; Option: TRCM  Transfer a Case Manager's Patients

**Example (continued): Transferring a Case Manager’s Patients**

* * *  WOMEN'S HEALTH: TRANSFER A CASE MANAGER'S PATIENTS  * * *

The purpose of this utility is to aid in the transfer of all of one

Case Manager's patients to another Case Manager, such as when there

is a turnover in staff.  The program will ask you for an "OLD" Case

Manager and then for a "NEW" Case Manager.  All patients who were

previously assigned to the "OLD" Case Manager will be reassigned to

the "NEW" Case Manager.

If the "NEW" Case Manager you are looking for cannot be selected,

that person must first be added to the file of Case Managers by

using the "Add/Edit Case Managers" option.

Select OLD CASE MANAGER: WHCOORDINATOR,ONE       OW          PHYSICIAN    DATE INACTIVATED:  FEB 18, 2020

Select NEW CASE MANAGER: WHCOORDINATOR,THREE     TW          PHYSICIAN

All patients currently assigned to: WHCOORDINATOR,ONE

will be reassigned to.............: WHCOORDINATOR,THREE

Do you wish to proceed?

Enter Yes or No? YES

4 patients transferred from WHCOORDINATOR,ONE to WHCOORDINATOR,THREE.

Type &lt;Enter&gt; to continue or '^' to exit:

#### Step 3: Assign New Case Managers to Patients

Option: *Edit/Print Patient Case Data* on the *Manager's Patient Management* , which is on the *Manager's Functions* menu.

If any user was newly designated as a Women’s Health case manager in step one, you need to assign that case manager to one or more patients.

**Example: Assigning a Women’s Health Case Manager**

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: MPM  Manager's Patient Management

**Example (continued): Assigning a Women’s Health Case Manager**

WOMEN'S HEALTH:    *  MANAGER'S PATIENT MANAGEMENT  *    SAMPLE VAMC

PPE    Patient Profile Including Errors

PC     Edit/Print Patient Case Data

HIS    Add an HISTORICAL Procedure

DUP    Browse Procedures for Possible Duplicates

PAL    Edit PAP Regimen Log

PRL    Edit Pregnancy/Lactation Status Data

Select Manager's Patient Management &lt;TEST ACCOUNT&gt; Option: PC  Edit/Print Patient Case Data

* * *  WOMEN'S HEALTH: EDIT PATIENT CASE DATA  * * *

Select the patient you wish to add or edit.

Select PATIENT NAME: WVPATIENT,TWO,TWO  WVPATIENT,TWO        3-10-95    66604000

2     NO     NSC VETERAN

Enrollment Priority: GROUP 5    Category: IN PROCESS    End Date:

If this prompt appears, answer YES.

<!-- image -->

<!-- image -->

is not currently in the Women's Health database.

Do you wish to add her to the Women's Health Database?

Enter Yes or No? YES

* * *  EDIT PATIENT CASE DATA  * * *

Patient Name: WVPATIENT,TWO(24y/o)                    SSN: XXX-XX-XXXX

Street: XXXXXXXXXXXXXXXXXXXXXXXXXXXX  Patient Phone: XXX-XXX-XXXX

Cty/St/Zip: XXXXXXXXXXXXXXXXXXXXXXXXXX      Pr Provider: UNKNOWN

Elig Code: NSC                                 Veteran: Yes

MST: Unknown, not screened

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Case Manager: WHCOORDINATOR,THREE           Inactive Date:

Breast Tx Need: ↓Undetermined              Cervical Tx Need: Undetermined

Breast Tx Due Date: ↓                      Cervical Tx Due Date:

Breast Tx Facility: ↓                      Cervical Tx Facility:

PAP Regimen: ↓Undetermined                           CST:

PAP Regimen Start Date: ↓                            Notes (WP):

Family Hx of Breast CA: ↓                          DES Daughter:

Maternity Care Coordinator: ↓

Date of 1st Encounter: ↓JAN 13,2020                Referral Source:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: S                                       Press &lt;PF1&gt;H for help  Insert

**Example (continued): Assigning a Women’s Health Case Manager**

* * *  EDIT PATIENT CASE DATA  * * *

Patient Name: WVPATIENT,TWO(24y/o)                    SSN: XXX-XX-XXXX

Street: XXXXXXXXXXXXXXXXXXXXXXXXXXXX  Patient Phone: XXX-XXX-XXXX

Cty/St/Zip: XXXXXXXXXXXXXXXXXXXXXXXXXX      Pr Provider: UNKNOWN

Elig Code: NSC                                 Veteran: Yes

MST: Unknown, not screened

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Case Manager: WHCOORDINATOR,THREE          Inactive Date:

Breast Tx Need: Undetermined              Cervical Tx Need: Undetermined

Breast Tx Due Date:                       Cervical Tx Due Date:

Breast Tx Facility:                       Cervical Tx Facility:

PAP Regimen: Undetermined                           CST:

PAP Regimen Start Date:                             Notes (WP):

Family Hx of Breast CA:                           DES Daughter:

Maternity Care Coordinator:

Date of 1st Encounter: JAN 13,2020                Referral Source:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E                                       Press &lt;PF1&gt;H for help  Insert

Do you wish to PRINT this patient's Case Data?

Enter Yes or No: NO//

#### Step 4: Designate Users as a Maternity Care Coordinator

Option: *Add/Edit Maternity Care Coordinators* on the *File Maintenance Menu* , which is on the *Manager's Functions* menu.

Before assigning a user as a patient’s maternity care coordinator, that user must be designated as a maternity care coordinator in the Women’s Health package. Execute this option to designate all maternity care coordinators at your site.

**Example: Designating a Women’s Health Maternity Care Coordinator**

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: FM  File Maintenance Menu

**Example (continued): Designating a Women’s Health Maternity Care Coordinator**

WOMEN'S HEALTH:       *  FILE MAINTENANCE MENU  *        SAMPLE VAMC

AEP    Add/Edit a Notification Purpose &amp; Letter

PPL    Print Notification Purpose &amp; Letter File

ESN    Edit Synonyms for Notification Types

OUT    Add/Edit Notification Outcomes

ESP    Edit Site Parameters

EPP    Edit Package Parameters

CM     Add/Edit Case Managers

MCC    Add/Edit Maternity Care Coordinators

TRCM   Transfer a Case Manager's Patients

TRMC   Transfer a Maternity Care Coordinator's Patients

AUTO   Automatically Load Patients

RAD    Import Radiology/NM Exams

PRD    Print Results/Diagnosis File

ESR    Edit Synonyms for Results/Diagnoses

PSR    Print Synonyms for Results/Diagnoses

EDX    Edit Diagnostic Code Translation File

PDX    Print Diagnostic Code Translation File

RS     Add/Edit to Referral Source File

PAP    Link Pap Smear with SNOMED Codes

Select File Maintenance Menu &lt;TEST ACCOUNT&gt; Option: MCC  Add/Edit Maternity Care Coordinators

* * *  WOMEN'S HEALTH: ADD/EDIT MATERNITY CARE COORDINATORS  * * *

Select MATERNITY CARE COORDINATOR: MCCOORDINATOR,ONE       OM          MATERNITY CARE COORDINATOR

Are you adding 'MCCOORDINATOR,ONE' as

a new WV MATERNITY CARE COORDINATOR (the 1ST)? No// YES  (Yes)

DATE INACTIVATED:

#### Step 5: Assign Maternity Care Coordinators to Patients

Option: *Edit/Print Patient Case Data* on the *Manager's Patient Management* , which is on the *Manager's Functions* menu.

Once a user is designated as a maternity care coordinator, you can assign that user to one or more patients.

**Example: Assigning a Women’s Health Maternity Care Coordinator**

WOMEN'S HEALTH:        *  MANAGER'S FUNCTIONS  *         SAMPLE VAMC

FM     File Maintenance Menu ...

PQ     Print Queued Letters

MPM    Manager's Patient Management ...

LDE    Lab Data Entry Menu ...

Select Manager's Functions &lt;TEST ACCOUNT&gt; Option: MPM  Manager's Patient Management

WOMEN'S HEALTH:    *  MANAGER'S PATIENT MANAGEMENT  *    SAMPLE VAMC

PPE    Patient Profile Including Errors

PC     Edit/Print Patient Case Data

HIS    Add an HISTORICAL Procedure

DUP    Browse Procedures for Possible Duplicates

PAL    Edit PAP Regimen Log

PRL    Edit Pregnancy/Lactation Status Data

Select Manager's Patient Management &lt;TEST ACCOUNT&gt; Option: PC  Edit/Print Patient Case Data

* * *  WOMEN'S HEALTH: EDIT PATIENT CASE DATA  * * *

Select the patient you wish to add or edit.

Select PATIENT NAME: WVPATIENT,TWO,TWO  WVPATIENT,TWO        3-10-95    66604000

2     NO     NSC VETERAN

Enrollment Priority: GROUP 5    Category: IN PROCESS    End Date:

If this prompt appears, answer YES.

<!-- image -->

<!-- image -->

is not currently in the Women's Health database.

Do you wish to add her to the Women's Health Database?

Enter Yes or No? YES

**Example (continued): Assigning a Women’s Health Maternity Care Coordinator**

* * *  EDIT PATIENT CASE DATA  * * *

Patient Name: WVPATIENT,TWO(24y/o)                    SSN: XXX-XX-XXXX

Street: XXXXXXXXXXXXXXXXXXXXXXXXXXXX  Patient Phone: XXX-XXX-XXXX

Cty/St/Zip: XXXXXXXXXXXXXXXXXXXXXXXXXX      Pr Provider: UNKNOWN

Elig Code: NSC                                 Veteran: Yes

MST: Unknown, not screened

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Case Manager: ↓WHCOORDINATOR,ONE            Inactive Date:

Breast Tx Need: ↓Undetermined              Cervical Tx Need: Undetermined

Breast Tx Due Date: ↓                      Cervical Tx Due Date:

Breast Tx Facility: ↓                      Cervical Tx Facility:

PAP Regimen: ↓Undetermined                           CST:

PAP Regimen Start Date: ↓                            Notes (WP):

Family Hx of Breast CA: ↓                          DES Daughter:

Maternity Care Coordinator: MCCOORDINATOR,ONE

Date of 1st Encounter: ↓JAN 13,2020                Referral Source:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: S                                       Press &lt;PF1&gt;H for help  Insert

* * *  EDIT PATIENT CASE DATA  * * *

Patient Name: WVPATIENT,TWO(24y/o)                    SSN: XXX-XX-XXXX

Street: XXXXXXXXXXXXXXXXXXXXXXXXXXXX  Patient Phone: XXX-XXX-XXXX

Cty/St/Zip: XXXXXXXXXXXXXXXXXXXXXXXXXX      Pr Provider: UNKNOWN

Elig Code: NSC                                 Veteran: Yes

MST: Unknown, not screened

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Case Manager: WHCOORDINATOR,ONE            Inactive Date:

Breast Tx Need: Undetermined              Cervical Tx Need: Undetermined

Breast Tx Due Date:                       Cervical Tx Due Date:

Breast Tx Facility:                       Cervical Tx Facility:

PAP Regimen: Undetermined                           CST:

PAP Regimen Start Date:                             Notes (WP):

Family Hx of Breast CA:                           DES Daughter:

Maternity Care Coordinator: MCCOORDINATOR,ONE

Date of 1st Encounter: JAN 13,2020                Referral Source:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit    Save    Refresh    Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E                                       Press &lt;PF1&gt;H for help  Insert

Do you wish to PRINT this patient's Case Data?

Enter Yes or No: NO//

### Add the Women’s Health Cover Sheet Panel to Customized Cover Sheets

**CAC:** A CAC should perform this task.

## In section 2.2.7, you identified which users, divisions or your VistA system have a customized Cover Sheet configuration that you need to add the new Women’s Health panel to and recorded them in Worksheet #3 at the end of this document. You will now add the Women’s Health panel to those customized Cover Sheet configurations.

In VistA, go to the CPRS MANAGER (ORMGR) menu.

Go to the CPRS Configuration (Clin Coord) ... menu by typing PE and pressing &lt;Enter&gt;.

Select GUI PARAMETERS… by typing GP and pressing &lt;Enter&gt;.

Select GUI Cover Sheet Display Parameters ... by typing CS and pressing &lt;Enter&gt;.

The GUI Cover Sheet Display Parameters menu gives the different levels for which users can view the display parameters: User, Location, Service, Division, and System. Below is a capture of the menu.

&lt;CPM&gt; Select GUI Parameters &lt;TEST ACCOUNT&gt; Option: CS  GUI Cover Sheet Display Parameters

SY     GUI Cover Sheet System Display Parameters

DI     GUI Cover Sheet Division Display Parameters

SE     GUI Cover Sheet Service Display Parameters

LO     GUI Cover Sheet Location Display Parameters

US     GUI Cover Sheet User Display Parameters

If the USER/DIVISION/SYSTEM value in Worksheet #3 begins with USR, type US and press &lt;Enter&gt;.

If the USER/DIVISION/SYSTEM value in Worksheet #3 begins DIV, type DI and press &lt;Enter&gt;.

If the USER/DIVISION/SYSTEM value in Worksheet #3 begins with SYS, type SY and press &lt;Enter&gt;.

After you select a Level, a list of current values for the Cover Sheet display parameters will appear. The following example shows the display for an example user.

Select GUI Cover Sheet Display Parameters &lt;TEST ACCOUNT&gt; Option: US  GUI Cover Sheet User Display Parameters

Select NEW PERSON NAME: PROVIDER,ONE       OP          PHYSICIAN

GUI Cover Sheet - User for User: PROVIDER,ONE

------------------------------------------------------------------------------

Inpatient Lab Number of Days to Display

Outpatient Lab Number of Days to Display

Enc Appt Range Start Offset

Enc Appt Range Stop Offset

Future Days Limit For PCE Selection

Cover Sheet Visit Range Start

Cover Sheet Visit Range Stop

Clinical Reminders for Search

List of coversheet reports    1                   ORCV ALLERGIES

2                   ORCV ACTIVE MEDICATIONS

3                   ORCV CLINICAL REMINDERS

4                   ORCV VITALS

Press &lt;Enter&gt; until the For List of coversheet reports – Select sequence: prompt appears.

Enter the first number in the SEQUENCE column in Worksheet #3 at the Select sequence: prompt.

1. If the Are you adding # as a new Sequence? Yes// prompt appears, press &lt;Enter&gt;.

Press &lt;Enter&gt; at the Sequence: prompt.

Type ORCV WOMEN'S HEALTH and press &lt;Enter&gt;.

If you need to renumber the remaining panels on the Cover Sheet, repeat the following steps as needed:

1. Enter the next number in the SEQUENCE column in Worksheet #3 at the Select sequence: prompt.
3. Type the name of the panel that corresponds with the number you entered in step 11a.

**Example: Adding the Women’s Health panel to an example user’s Cover Sheet and resequencing three of the panels**

Select OPTION NAME: ORMGR       CPRS Manager Menu

CL     Clinician Menu ...

NM     Nurse Menu ...

WC     Ward Clerk Menu ...

PE     CPRS Configuration (Clin Coord) ...

&lt;CPM&gt; Select CPRS Manager Menu &lt;TEST ACCOUNT&gt; Option: PE  CPRS Configuration (Clin Coord)

AL     Allocate OE/RR Security Keys

KK     Check for Multiple Keys

DC     Edit DC Reasons

GP     GUI Parameters ...

GA     GUI Access - Tabs, RPL

MI     Miscellaneous Parameters

NO     Notification Mgmt Menu ...

OC     Order Checking Mgmt Menu ...

MM     Order Menu Management ...

LI     Patient List Mgmt Menu ...

FP     Print Formats

PR     Print/Report Parameters ...

RE     Release/Cancel Delayed Orders

US     Unsigned orders search

EX     Set Unsigned Orders View on Exit

NA     Search orders by Nature or Status

CI     Consults Clinically Indicated Date Default

CM     Care Management Menu ...

DO     Event Delayed Orders Menu ...

LO     Lapsed Orders search

PM     Performance Monitor Report

&lt;CPM&gt; Select CPRS Configuration (Clin Coord) &lt;TEST ACCOUNT&gt; Option: GP  GUI Parameters

CS     GUI Cover Sheet Display Parameters ...

HS     GUI Health Summary Types

TM     GUI Tool Menu Items

MP     GUI Parameters - Miscellaneous

UC     GUI Clear Size &amp; Position Settings for User

RE     GUI Report Parameters ...

NV     GUI Non-VA Med Statements/Reasons

EX     GUI Expired Orders Search Hours

RM     GUI Remove Button Enabled

NON    GUI Remove Button Enabled for Non-OR Alerts

CLOZ   GUI Edit Inpatient Clozapine Message

COAG   GUI Anticoagulation Parameters ...

DEA    GUI ePCS Management Menu ...

EIE    GUI Mark Allergy Entered in Error

&lt;CPM&gt; Select GUI Parameters &lt;TEST ACCOUNT&gt; Option: CS  GUI Cover Sheet Display Parameters

SY     GUI Cover Sheet System Display Parameters

DI     GUI Cover Sheet Division Display Parameters

SE     GUI Cover Sheet Service Display Parameters

LO     GUI Cover Sheet Location Display Parameters

US     GUI Cover Sheet User Display Parameters

Select GUI Cover Sheet Display Parameters &lt;TEST ACCOUNT&gt; Option: US  GUI Cover Sheet User Display Parameters

Select NEW PERSON NAME: PROVIDER,ONE       OP          PHYSICIAN

GUI Cover Sheet - User for User: PROVIDER,ONE

------------------------------------------------------------------------------

Inpatient Lab Number of Days to Display

Outpatient Lab Number of Days to Display

Enc Appt Range Start Offset

Enc Appt Range Stop Offset

Future Days Limit For PCE Selection

Cover Sheet Visit Range Start

Cover Sheet Visit Range Stop

Clinical Reminders for Search

List of coversheet reports    1                   ORCV ALLERGIES

2                   ORCV ACTIVE MEDICATIONS

3                   ORCV CLINICAL REMINDERS

4                   ORCV VITALS

------------------------------------------------------------------------------

Inpatient Lab Number of Days to Display:

Outpatient Lab Number of Days to Display:

Enc Appt Range Start Offset:

Enc Appt Range Stop Offset:

Future Days Limit For PCE Selection:

CS Visit Search Start:

CS Visit Search Stop:

For Clinical Reminders for Search -

Select Display Sequence:

For List of coversheet reports -

Select Sequence: 2

Sequence: 2//    2

Coversheet Report: ORCV ACTIVE MEDICATIONS// ORCV WOMEN'S HEALTH       Women's Health     Women's Health Data

For List of coversheet reports -

Select Sequence: 3

Sequence: 3//    3

Coversheet Report: ORCV CLINICAL REMINDERS// ORCV ACTIVE MEDICATIONS       Active Medications

For List of coversheet reports -

Select Sequence: 4

Sequence: 4//    4

Coversheet Report: ORCV VITALS// ORCV CLINICAL REMINDERS       Clinical Reminders                                        Due Date

For List of coversheet reports -

Select Sequence: 5

Are you adding 5 as a new Sequence? Yes//   YES

Sequence: 5//    5

Coversheet Report: ORCV VITALS       Vitals

For List of coversheet reports -

Select Sequence:

### Add New Clinical Reminders to the Cover Sheet Reminder List

**Reminder Manager/CAC:** A Reminder Manager or CAC should perform this task.

Follow the instructions in the ORQQPX NEW REMINDER PARAM set to “YES” section of the Clinical Reminders Manager’s Manual or in the New Cover Sheet Reminder List section in the Computerized Patient Record System (CPRS) Technical Manual: GUI Version to add the Pregnancy/Intentions/Contraception and Update Lactation Status reminders to the appropriate users’ Reminder Cover Sheet List. You identified this list of users in section 2.2.4.

### Setup SMART Notifications

**CAC/Local Women’s Health Office:** A CAC should perform this task in consultation with the site’s Women’s Health Office.

There are three notifications that are exported with CPRS Version 31b related to SMART. They are:

- SMART ABNORMAL IMAGING RESULTS
- SMART NON-CRITICAL IMAGING RES
- SCHEDULED ALERTS

## Note:	The SMART notifications give similar information as the Mammogram Results notification. Sites that implement the SMART notifications should turn off the Mammogram Results notification.

These notifications exported with the patch are turned off at the package level. As with all CPRS notifications, these SMART notifications can be enabled at the following levels ( **Note:** Highest precedence wins in this list which means user level settings would override lower precedence levels, such as service or system):

1. User
2. Team (OE/RR)
3. Service
4. Location
5. Division
6. System

These settings can be altered in the following option: Enable/Disable Notifications  [ORB3 PROCESSING FLAG]

Recipients of these SMART notifications must be determined through staff discussions of how to best utilize the SMART functionality at your local site.  A user can become a recipient in multiple ways:

- As a default recipient of all alerts of that notification type – use option Set Default Recipient(s) for Notifications [ORB3 DEFAULT RECIPIENTS]
- As a provider recipient – use option Set Provider Recipients for Notifications [ORB3 PROVIDER RECIPIENTS]
    - Options for provider recipients are as follows
        - P (Primary Provider): deliver notification to the patient's Primary Provider.
        - A (Attending Physician): deliver notification to the patient's Attending Physician.
        - T (Patient Care Teams): deliver notification to the patient's OE/RR Teams (personal patient and team lists are evaluated for potential recipients) and to devices on an OE/RR team.
        - O (Ordering Provider): deliver notification to the provider who placed the order which trigger the notification.
        - M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.
        - E (Entering User): deliver notification to the user/provider who entered the order's most recent activity.
        - R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.
        - S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.
        - C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.

### Setup a Reminder List Rule to Automatically Update a Team List (Optional)

**CAC/Reminder Manager:** The Clinical Applications Coordinators (CACs) or the reminder manager complete this section.

## Note:	Sites must consult with their Women’s Health group to determine if they will set up this rule and how it should be configured for your specific site.

New options are being released that allow a reminder list rule to be setup to run on a set schedule and update a team list with the patients that meet the criteria defined in the list rule. The following new national list rules need to be configured to update a team list:

- VA-WH RS MAMMOGRAM DUE
- VA-WH RS ORDERS PENDING GREATER 60 DAYS
- VA-WH RS PATIENTS WITHOUT A NOTIFICATION

There is a two-step process to do this:

1. A team list needs to be created for each list rule (if filtering by division, you will need to create multiple team lists; one for each division and one to be used as a catch-all).
2. The team list needs to be mapped to the list rule, and the update frequency needs to be defined.

#### Create a Team List

Option: *Create/Add to Team List* on the *Team List Mgmt Menu* .

This step is performed by the site’s Clinical Applications Coordinators (CACs).

Create a team list for each list rule and assign the clinicians that should be associated with the list. If filtering by division (see next step), you will need to create multiple team lists for each list rule; one for each division and one to be used as a catch-all. (The team list name shown in the example below is just an example; assign a name per local preference and conventions).

Select Team List Mgmt Menu Option: CR  Create/Add to Team List

A team list is a list containing patients related to several providers.

These providers are the list's users.  You may now create a new team list

or add autolinks, users and/or patients to an existing team list.  Autolinks

automatically add or remove patients with ADT movements.  Users on the list

may receive notifications regarding patients on the same list.  Please prefix

your list name with 'TEAM' or 'SERVICE' (e.g. TEAM7B, SERVICECARDIOLOGY.)

Enter team list name: MAMMOGRAM DUE PATIENTS

Are you adding 'MAMMOGRAM DUE PATIENTS' as a new OE/RR LIST (the 154TH)? No// Y  (Yes)

Enter type: TM  TEAM PATIENT MANUAL

to enter additional patients. (? for help):

<!-- image -->

Select one of the following:

N         NAME

W         WARD

C         CLINIC

P         PROVIDER

T         TREATING SPECIALTY

to enter additional patients. (? for help):

Enter team provider/user: PROVIDER,ONE              OP

Enter team provider/user:

Enter device:

Select Team List Mgmt Menu Option:

<!-- image -->

#### Map the team list to a list rule

Option: *Automate List Rule to Update List* on the *Team List Mgmt Menu* .

This step is performed by the site’s Clinical Applications Coordinators (CACs).

Map the team list to a list rule. If desired, the patients can be filtered by division.

If selected to not filter by division, all patients found by the list rule will be added to the mapped team list.

**Example: Mapping team list to a list rule - not filtering by division**

<!-- image -->

However, if you want to filter the patients by division, and have patients from division A added to one team list and patients from division B added to another team list, then enter ‘Yes’ to the prompt ‘Do you want to filter patients by Division’, and for each division enter the team list to use. Even when filtering by division, you will still need to define a “catch-all” team list to be used in cases where it cannot be determined which division a patient belongs to.

1. If the patient’s Primary Care Provider is assigned only one division, that division will be used.
2. If the patient’s Primary Care Team is linked to a division, that division will be used.
3. If the patient has a Preferred Facility defined, that division will be used.

Select Team List Mgmt Menu Option: LR  Automate           List Rule to Update List

**List Rule to Update Team List** May 01, 2017@13:30:23          Page:    1 of    1

&lt;&lt; Option ORLP TEAM LIST FROM REM is next scheduled to run: 5/1/17@23:00. &gt;&gt;

#  Rem List Rule                Last Run Time   Freq  Division   Team List

&gt;&gt; There are currently no mappings.

+          Enter ?? for more actions                                       &gt;&gt;&gt;

AD  Add an Entry          DL  Delete an Entry       RF  Refresh

ED  Edit an Entry         RN  Run Now

Select Action: Quit// AD   Add an Entry

Select REMINDER LIST RULE NAME: VA-WH RS MAMMOGRAM DUE       RULE SET

Do you want to filter patients by Division? NO// YES

&gt;&gt; First, you will need to select a team list to be used in cases

&gt;&gt; where it cannot be determined which division a patient belongs to.

Select OE/RR LIST: MAMMOGRAM DUE PATIENTS (CATCH-ALL)

&gt;&gt; Now, you can select the team lists to be used for each division.

Select DIVISION: CAMP MASTER    NY  VAMC     500

Select OE/RR LIST: MAMMOGRAM DUE PATIENTS (CMP)

Select DIVISION: CENTRAL CITY (CCC)    KY  OC  995

Select OE/RR LIST: MAMMOGRAM DUE PATIENTS (CCC)

Select DIVISION: [ENTER]

Enter the frequency (in days) the team list should be updated:  (1-365): 30

Should the Rem Patient List be overwritten when updating a Team List? YES//

<!-- image -->

<!-- image -->

## Note:	The system will try to determine the patient’s division using the following criteria (the first true condition from the list below would stop the search, and that division will be used for filtering the patient):

### Schedule the Update Team List from Reminder List Rule Option

**ITOPS:** This step is performed by the site’s local/regional OI&amp;T support.

Schedule the Update Team List From Reminder List Rule option [ORLP TEAM LIST FROM REM] to run as a tasked option. It should be scheduled to run during non-peak hours, with a rescheduling frequency of “1D”.

**Example:** Scheduling the Update Team List From Reminder List Rule option

<!-- image -->

### Setup SCHEDULED ALERTS for Tickler Alerts

**CAC:** This task should be performed by a CAC.

The SCHEDULED ALERTS notification enables users to set up tickler alerts to remind them to perform some function in the future.

The SCHEDULED ALERTS notification is exported as disabled at the package level. To use tickler alerts, sites will need to enable the SCHEDULED ALERTS notification.

SCHEDULED ALERTS can be enabled at the following levels ( **Note:** Highest precedence wins in this list which means user level settings would override lower precedence levels, such as service or system):

1. User
2. Team (OE/RR)
3. Service
4. Location
5. Division
6. System

These settings can be altered in the following option: Enable/Disable Notifications  [ORB3 PROCESSING FLAG].

### Confirm TIU TEMPLATE CONSULT LOCK Values

**CAC:** This step should be performed by a CAC.

Option: *Set consult templates to read-only* , which is on the *TIU Template Mgmt Functions* menu.

The post-install process for the TIU*1.0*290 patch attempts to automatically add any TIU templates that are linked to a consult service and where the NAME begins with “NON VA CARE HCPS”. This approach was used as some integrated facilities use station identifier suffixes on the consult services/templates. The templates automatically added to this parameter are those used when sending consults to the Referral Authorization System (RAS) for Non-VA care covered under the Dialysis National Contract (DNC).

Sites should review the values assigned to this parameter. If any unused/unwanted templates have been assigned to the parameter, use the Remove action to delete these values from the parameter. If the post-install failed to add templates used for RAS consults, use the Add action to add those values to the parameter.

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

7      TIUHL7 Message Manager

Title Mapping Utilities ...

6      Active Title Cleanup Report

Text Event Edit

&lt;CPM&gt; Select TIU Maintenance Menu &lt;TEST ACCOUNT&gt; Option: 4  TIU Template Mgmt Functions

1      Delete TIU templates for selected user.

2      Edit auto template cleanup parameter.

3      Delete templates for ALL terminated users.

4      Set consult templates to read-only.

&lt;CPM&gt; Select TIU Template Mgmt Functions &lt;TEST ACCOUNT&gt; Option: 4  Set consult templates to read-only.

TIU TEMPLATE CONSULT LOCK may be set for the following:

NUMBER         TEMPLATE

======         ========

1              NON VA CARE HCPS HEMODIALYSIS

2              NON VA CARE HCPS PERITONEAL DIALYSIS

Remove existing template or Add new entry?:  (R/A): REMOVE

Select NUMBER to remove: 1

... Deleted.

1      Delete TIU templates for selected user.

2      Edit auto template cleanup parameter.

3      Delete templates for ALL terminated users.

4      Set consult templates to read-only.

&lt;CPM&gt; Select TIU Template Mgmt Functions &lt;TEST ACCOUNT&gt; Option:

### Review Line Length for Consult and Procedure Templates

**CAC:** This step should be performed by a CAC and can be completed after users are allowed to use CPRS.

During testing of CPRS v31b, an issue was identified with consult and procedure templates. Consult and procedure templates that contain lines with more than 74 characters may not wrap correctly in CPRS. Sites must manually correct those templates that do not warp correctly.

A post-install routine will create the PATCH TIU*1*290 TEMPLATE CHECK RESULTS report that will identify which consult and procedure templates contain lines with more than 74 characters that should be reviewed for wrapping issues.

Example report

Subj: TIU*1*290 TEMPLATE CHECK RESULTS  [#17762] 05/11/20@12:16  11 lines

From: TIU TEMPLATE CHECKER  In 'IN' basket.   Page 1  *New*

-------------------------------------------------------------------------------

The following templates contain text that is more than 74 characters in

length. Please review each template in CPRS to ensure that the text is

wrapped correctly.

Consult Reasons for Request

---------------------------

LOCAL TEMPLATE

Caregiver

CAREGIVER SUPPORT PROGRAM OUTPT

Caregiver &gt; Caregiver Subfolder

LOCAL CAREGIVER TEMPLATE

In the example above, the LOCAL TEMPLATE template, the CAREGIVER SUPPORT PROGRAM OUTPT template in the Caregiver folder, and the LOCAL CAREGIVER TEMPLATE template in the Caregiver Subfolder folder in the Caregiver folder all contain one or more lines that are more than 74 characters in length.

The report is sent to the OR CACS mail group and the installer.

### Review Post-Installation Message GMRA*4*53 CLEAN-UP STATUS

When finishing a pharmacy order for a patient with an adverse reaction that has a sign/symptom of OTHER REACTION and the free text value contains a trailing comma, a subscript error is generated during the drug-allergy order check.

The post-install routine schedules a background task that will remove leading, trailing, and repeated commas from the free text value of OTHER REACTION. Once this task completes, the report GMRA*4*53 CLEAN-UP STATUS is generated that contains all the free text values that were modified.

The report is sent as an email to the OR CACS mail group and to the installer.

This report will assist sites in confirming that the scheduled task did its job properly.

Here is an example of part of a report.

Subj: GMRA*4*53 CLEAN-UP STATUS  [#17780] 05/13/20@15:13  11 lines

From: GMRA, CLEAN-UP  In 'IN' basket.   Page 1  *New*

-------------------------------------------------------------------------------

PATIENT NAME                   REACTANT

ORIGINAL VALUE

--------------

NEW VALUE

=============================================================================

OUTPATIENT,ONE                 PENICILLIN

RASH,,

------

RASH

NUMBER OF REACTIONS CHANGED: 1

CACs are responsible for reviewing the report and correcting any issues identified. For those reactants whose sign/symptoms was not properly cleaned up, enter a ServiceNOW ticket for assistance in manually adjusting the OTHER REACTION value.

### Review Post-Installation Message OUTPATIENT MED QUICK ORDER CONVERSION

As part of the changes included with CPRS v31b, the Except conjunction has been removed from prescriptions.

A post-install routine was added to update existing Outpatient Med Quick Orders and remove any EXCEPT conjunctions.

An email report will be sent to the patch installer and the OR CACS mail group with the subject OUTPATIENT MED QUICK ORDER CONVERSION.

### Review Post-Installation Message Update to Dietetic Quick Order

As part of the changes included with CPRS v31b, the Stop Date and Cancel Late Tray conjunction has been removed from Dietetic Quick Order.

A post-install routine was added to update existing Dietetic Quick Orders.

An email report will be sent to the patch installer and the OR CACS mail group with the subject DIETETIC QUICK ORDER CONVERSION.

### Configure Copy/Paste Settings

**CAC:** The personnel responsible for setting the TIU DOCUMENT PARAMETERS and the TIU BASIC PARAMETERS may want to change the default settings of the new Copy/Paste fields.  Also, if needed, the CAC can use the GENERAL PARAMETER TOOLS (XPAR EDIT TOOLS) menu item to edit the ORQQTIU COPY/PASTE IDENT and ORQQTIU COPY/PASTE EXCLUDE APP parameters. The CAC should consult with HIMS Manager and facility leadership to discuss and determine the settings.

## Note: 	Once the settings are established, sites should review the copy/paste data to ensure that the settings produce the results sites need.  Sites may need to adjust these settings to get the best results for their site.

Below is some helpful guidance as to these settings.

You may use the Basic TIU Parameters [TIU BASIC PARAMETER EDIT] option to edit the following fields in TIU PARAMETERS (#8925.99) file:

MINIMUM COPY WORDS (#4.1)

This field defaults to 5 words if no value is set.  As this determines what is captured as copied text, this value can play a significant role in what is tracked.  The smaller this number, the more copy actions will be captured.  Each site will need to determine the appropriate level of capture that is ideal for their individual needs.

COPY/PASTE VERIFY PERCENTAGE (#4.2)

This field defaults to 90% if no value is set.  This field plays a significant part in determining when pasted text is identified as originating from a previously captured copy action.  The higher the percentage, the less likely pasted text will be identified as originating from copied text.  Each site will need to determine the appropriate level of percentage match that is ideal for their individual needs.

COPY/PASTE USERCLASS (#4.4)

This field is empty to begin.  The copy/paste software will always provide the “CHIEF, HIMS”, "CHIEF, MIS", and the "PRIVACY ACT OFFICER" user classes as having the ability to view copy/paste highlighting in CPRS.  If sites wish to provide another user class these rights, then they should add an existing user class to this entry.

You may use the Document Parameter Edit [TIU DOCUMENT PARAMETER EDIT] option to edit the following fields in TIU DOCUMENT PARAMETERS (#8925.95) file:

EXCLUDE FROM COPY/PASTE (#10.1)

This field defaults to NO (0) if no value is set for a specific document.  This should be a rarely used field as most documents should allow tracking of copy/paste data.  Each site will need to determine if they use any special TIU notes which should/need to be excluded based on pre-existing policies/procedures that emphasize the re-use of text that cannot be accomplished via templates or other mechanisms.

You may use the General Parameters Tools [XPAR MENU TOOLS] option to edit the following parameters:

ORQQTIU COPY/PASTE IDENT

This parameter determines how copy/paste text displays in CPRS, such as highlighting, bolding, etc. It is defaulted to “-1;Visual Disable Override” if no values are set.  This will cause the visual component to be disabled for most users.  Users can enable user level settings through the Copy/Paste tab of the Options dialog in the CPRS GUI.

CACs or similar personnel can also set the identifiers by entering values for the parameter.

## Note: 	When setting the identifiers by parameter, the prompt incorrectly states that the user should input 11 comma-separated values. Setting the parameter actually requires 12 comma-separated values.

One of the options is also a way to turn off copy/paste entirely for the whole site. To completely turn off Copy/Paste tracking, someone with Programmer access would set this parameter to “-2;CP Disable Override” without the quotation marks at the Package level. This can only be set at the package level. **Only someone with Programmer access can make a change at the Package level.**

ORQQTIU COPY/PASTE IDENT may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Division      DIV    [choose from INSTITUTION]

3   System        SYS    [CPRS32.FO-SLC.MED.VA.GOV]

4   Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: 4  Package   ORDER ENTRY/RESULTS REPORTING

Parameters set for 'Package' may be replaced if ORDER ENTRY/RESULTS REPORTING

is installed in this account.

Setting ORQQTIU COPY/PASTE IDENT  for Package: ORDER ENTRY/RESULTS REPORTING

COPY/PASTE IDENTIFIER: -2;CP Disable Override  Replace

ORQQTIU COPY/PASTE EXCLUDE APP

This parameter allows sites to designate applications (.exe) that will not be considered copy/paste if encountered in the Windows copy clipboard. This feature allows a site to filter out some applications that utilize the Windows copy clipboard as part of their functionality. This will prevent text from being mistakenly identified as copied by the user when the user did not actually copy any text. One application (natspeak.exe) was preloaded at the Package level with the install of the copy/paste functionality.

### Configure Exception Parameters

**CAC:** This step should be performed by Clinical Application Coordinator (CAC) or similar personnel at the site.

Three CPRS parameters help to give teams information if an exception, such as an access violation (AV) occurs. This information can help individuals supporting CPRS to troubleshoot any possible exception issues.

- OR CPRS EXCEPTION EMAIL: Enter the Outlook email addresses for those individuals who should receive an email detailing any exceptions that occur. This is a list of people for the email button.  Multiple individual email address can be added here.
- OR CPRS EXCEPTION LOGGER: Set this parameter to “Yes”.  Setting to “YES” enables the ability to email AV information to the individuals listed in the OR CPRS EXCEPTION EMAIL parameter.
- OR CPRS EXCEPTION PURGE: Enter the number of days to keep exception log files. When an error occurs and the Exception Logger is enabled (OR CPRS EXCEPTION LOGGER), an exception log file is created on the user’s machine when this type of error occurs. The files will be deleted after the number of days set in this parameter. If nothing is entered here, the files are removed after 60 days by default.

### Configure Site Parameter for One-Step Clinic Administration

**CAC:** This step is performed by the site’s CACs.

A new parameter, OR ONE STEP CLINIC ADMIN OFF, allows sites to enable or disable the One-Step Clinic Administration option on the Action menu on the Orders tab.

This parameter is exported with a Package level default value of NO that enables the ‘One Step Clinic Admin’ menu item on the Action menu of the Orders tab.

Setting this parameter at the System, Division or User level to YES will disable the menu item. It will still display on the Action menu, but users will not be able to select it.

Use option *Edit Parameter Values* on the *General Parameter Tools* menu, which is on the *CPRS Configuration (IRM)* menu, which is on the *CPRS Manager Menu* (this option is restricted to those with programmer access) to change the value of this parameter.

**Example: Disabling the One-Step Clinic Admin menu item for the entire system**

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: EP  Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR ONE STEP CLINIC ADMIN OFF     ONE STEP CLIN

IC ADMIN Menu Disable

OR ONE STEP CLINIC ADMIN OFF may be set for the following:

2   User          USR    [choose from NEW PERSON]

4   Division      DIV    [SAMPLE VAMC]

6   System        SYS    [PLA.SAMPLE.MED.VA.GOV]

10  Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: 6  System   PLA.SAMPLE.MED.VA.GOV

- Setting OR ONE STEP CLINIC ADMIN OFF  for System: PLA.SAMPLE.MED.VA.GOV -

Yes/No: YES

OR ONE STEP CLINIC ADMIN OFF may be set for the following:

2   User          USR    [choose from NEW PERSON]

4   Division      DIV    [SAMPLE VAMC]

6   System        SYS    [PLA.SAMPLE.MED.VA.GOV]

10  Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection:

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME:

### Configure site parameter OR CPRS HELP DESK TEXT

**C** AC: The step is performed by the CAC.

A new parameter, OR CPRS HELP DESK TEXT, allows sites to modify the text in the message box that appears when the CPRS GUI attempts to use the incorrect version of a DLL.

This parameter is exported with a Package level default value of “your local CPRS help desk”, which causes the message box to contain the text “Please contact your local CPRS help desk to obtain the updated version of the DLL”.

If desired, sites can choose to set this text at the system level.

Use option *Edit Parameter Values* on the *General Parameter Tools* menu, which is on the *CPRS Configuration (IRM)* menu, which is on the *CPRS Manager Menu* (this option is restricted to those with programmer access) to change the value of this parameter.

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: EP  Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR CPRS HELP DESK TEXT     Help text used by C

PRS

---- Setting OR CPRS HELP DESK TEXT  for System: PLA.WEST-PALM.MED.VA.GOV ----

Value: the help desk at extension 9999

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME:

<!-- image -->

### Convert Existing Pregnancy and Lactation Data

**CAC/Local Women’s Health Office:** This step is performed by the site’s Clinical Applications Coordinators (CACs) in conjunction with the local Women’s Health office.

During the post-installation process, pregnancy status data that was entered directly into the Women’s Health software package is converted into the new data format without any further action needed. However, sites may have used patient record flags, health factors, postings or the problem list to document when a patient is pregnant or breastfeeding. With the installation of CPRS v31.b, using these features to document when a patient is pregnant or breastfeeding is now obsolete and no longer recommended. Sites must cease using these features to document when a patient is pregnant or breastfeeding and must instead use either the Women’s Health panel on the Cover Sheet tab or the Pregnancy/Intentions/Contraception and Update Lactation Status reminder dialogs to document a patient’s pregnancy status (including when a patient is not pregnant) and lactation status (including when a patient is not breastfeeding).

If your site uses patient record flags, health factors, postings or the problem list to document when a patient is pregnant or breastfeeding, you need to follow the steps below to convert your existing data into the new format:

1. Determine which patients are currently pregnant and/or breastfeeding.
2. For patients that are currently pregnant, review each patient’s chart to determine the expected due date and note that date on your list.
3. Open CPRS.
4. For each patient:
    1. Select the patient in the Patient Selection dialog.
    2. Navigate to the Cover Sheet tab.
    3. Right-click in the Women’s Health panel then select the Add New Data… item from the menu that appears (see section 3.7 if the Women’s Health panel does not appear on the Cover Sheet tab).
    4. In the Women’s Health – Pregnancy and Lactation Status Update dialog that appears:
        1. For currently pregnant patients, select the Able to conceive then the Pregnant options and then enter the expected due date. **Note:** The Lactation Status section is optional and may be left blank.
        2. For currently breastfeeding patients, select the Currently lactating option. **Note:** The Medically Able to Conceive and Pregnancy Status sections are optional and may be left blank.
        3. Click on the Save button.

## 5 Worksheets

### Worksheet #1

Laboratory Tests:

| **TEST NAME**   | **SITE/SPECIMEN**   | **Patient is Pregnant**   | **Patient is Not Pregnant**   |
|-----------------|---------------------|---------------------------|-------------------------------|
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |
|                 |                     |                           |                               |

Patient is Pregnant Condition Statements:

| **TEST NAME**   | **CONDITION STATEMENT**   | **CASE SENSITIVE**   |
|-----------------|---------------------------|----------------------|
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |

Patient is Not Pregnant Condition Statements:

| **TEST NAME**   | **CONDITION STATEMENT**   | **CASE SENSITIVE**   |
|-----------------|---------------------------|----------------------|
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |
|                 |                           |                      |

### Worksheet #2

Radiology Parent Procedures:

| **PARENT PROCEDURE NAME**   | **DESCENDENT CPT CODES**   | **TAXONOMY NAME**   |
|-----------------------------|----------------------------|---------------------|
|                             |                            |                     |
|                             |                            |                     |
|                             |                            |                     |
|                             |                            |                     |

Radiology Detailed and Series Procedures:

| **PROCEDURE NAME**   |
|----------------------|
|                      |
|                      |
|                      |
|                      |

### Worksheet #3

Customized Cover Sheet Configurations Needing the Women’s Health Panel

| **USER/DIVISION/SYSTEM**   | **SEQUENCE**   |
|----------------------------|----------------|
|                            |                |
|                            |                |
|                            |                |
|                            |                |

### ## Note: 	It is imperative that you wait for the post-install TaskMan jobs to complete before beginning work on this section. Specifically, have your installer verify that the following tasks have successfully completed before continuing:

1. Search for the text PXRM*2.0*45 HI RISK MEDS then locate an entry titled PXRM*2.0*45 HI RISK MEDS CONTENT in reminder exchange.
<!-- image -->
2. At the **Select Action:** prompt, enter **IFE** for Install Exchange File Entry.
3. Enter the number that corresponds with your entry **PXRM*2.0*45 HI RISK MEDS CONTENT** (in this example, it is entry 28). It will vary by site. Make sure you select the exchange entry dated 01/23/2020@09:44.

<!-- image -->

1. At the Select Action prompt, enter **IA** for Install All Components.

**The general rules for installation are as follows:**

1. If a component does not exist (it is NEW), select the Install action.
2. If a component does exist (it is DIFFERENT), select the Overwrite the current entry action.

At this point, the dialog installations begin.

You are prompted to install the FIRST reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH UPDATE LACTATION STATUS.
2. At the Install reminder dialog and all components with no further changes: Y// prompt, enter Yes
3. At the Reminder Dialog VA-WH UPDATE LACTATION STATUS is not linked to a reminder. Select Reminder to Link: VA-WH UDPATE LACTATION STATUS// prompt, press the ENTER key to accept the default value.

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** for Quit.

You are prompted to install the SECOND reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog VA-WH UPDATE PREGNANCY STATUS.
2. At the Install reminder dialog and all components with no further changes: Y// prompt, enter Yes
3. At the Reminder Dialog VA-WH UPDATE PREGNANCY STATUS is not linked to a reminder. Select Reminder to Link: VA-WH UDPATE PREGNANCY STATUS// prompt, press the ENTER key to accept the default value.

You are prompted for how you want to handle the first non-existent finding Q.EMERGENCY CONTRACEPTIVE QUICK ORDER.

1. At the **Enter response:** prompt, enter **P** for Replace with an existing entry.
2. At the **Select ORDER DIALOG NAME:** prompt, enter the name of the emergency contraceptive quick order you identified or created in section 2.2.2.

You are prompted for how you want to handle the second non-existent finding Q.PREGNANCY TEST QUICK ORDER.

1. At the **Enter response:** prompt, enter **P** for Replace with an existing entry.
2. At the **Select ORDER DIALOG NAME:** prompt, enter the name of the pregnancy test quick order you identified or created in section 2.2.2.

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** to quit.

You are prompted to install the THIRD reminder dialog:

<!-- image -->

1. At the **Select Action:** prompt, enter **IA** for Install All; this will install the dialog PXRM PATCH 45 TIU/HS OBJECTS.
2. At the **Install reminder dialog and all components with no further changes: Y//** prompt, enter **Yes**

<!-- image -->

1. After the dialog installation completes, you are returned to the Dialog Components screen; at the **Select Action:** prompt, enter **QU** for Quit.

You are then returned to the Exchange File Components screen.

<!-- image -->

1. At the **Select Action:** prompt, enter **Q** for Quit.

**Installation of the Women’s Health High Risk Medications reminder content is now complete.**

1. If the Are you adding # as a new Sequence? Yes// prompt appears, press &lt;Enter&gt;.