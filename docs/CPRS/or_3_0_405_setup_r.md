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
source_file: or_3_0_405_setup_r.docx
status: draft
title: '# Computerized Patient Record System (CPRS)'
---

# Computerized Patient Record System (CPRS) 
Version 32b Build (OR*3.0*405)

Setup and Configuration Guide


<!-- image -->

October 2022


Enterprise Program Management Office (EPMO)

Table of Contents

1	CPRS v32b (OR*3.0*405)	1

1.1	Overview	1

1.2	Recommended Audience	1

1.3	About this Guide	1

1.4	Document Conventions	1

1.5	Related Documents	1

2	Pre-requisites	2

2.1	Pre-requisite Patches	2

3	Reporting Issues	2

4	Pre- and Post-Installation Checklist	2

5	Pre-Installation Steps	2

5.1	Ensure that All Immunization Lot Numbers Have Been Entered into the System	3

5.2	Determine Current Coversheet Settings	3

5.3	Determine Note Titles for the CoverSheet Immunization functionality	4

5.4	Back Up National Reminder Immunization Dialogs Immunization Entries	5

5.5	Run the Reminder Dialog CPRS 32 Pre-Conversion Report	5

5.6	Review local Reminder Definition for Immunization and Skin Test	8

5.7	Ensure That Appropriate Recipients Belong to the OR CACS Mailgroup	8

6	Post-Installation Steps	9

6.1	Install Reminder Content	10

6.2	Map local note titles to the CPRS CoverSheet Immunization Form	10

6.3	Assign Local Clinical Reminder Definition to the Immunization/Skin Test form (optional)	11

6.4	Update the CPRS Coversheet Settings to Show the Immunization Section	12

6.5	Update Any Local Reminder Dialogs	14

6.6	Update Quick Orders for Indication Prompt and Titration	14

6.7	Review the CLINIC PICKUP QUICK ORDER CONVERSION MailMan Message	18

6.8	Review the ORDER REASON file (#100.03) and the OR DC REASON LIST parameter	18

6.9	Review the OR RTN PROCESSED ALERTS parameter	19

6.10	Review the PSO PARK ON parameter	19

7	Verify Successful Installation	19

## 1 CPRS v32b (OR*3.0*405)

### Overview

The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This document describes how to perform setup and configuration steps before and after the CPRS v32b installation, which includes several patches in a combined build, and a graphical user interface (GUI) executable.

### Recommended Audience

This guide provides information specifically for those personnel who need to perform set up and configuration steps before and after the CPRS v32b installation. These groups include Information Technology Operations and Support (ITOPS) staff, Clinical Application Coordinator (CAC) personnel, the site’s Women’s Health group, and others who will be needed so that the CPRS v32b will work correctly at sites.

### About this Guide

This set up/configuration guide provides instructions for:

- Pre-installation steps, which must be performed before the CPRS v32b installation can proceed.

Post-installation tasks that require knowledge of the underlying VistA system.

### Document Conventions

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER       Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

## NOTE:	  This is an important point and must not be omitted.

### Related Documents

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

*CPRS User Guide: GUI Version*

*CPRS Technical Manual*

*CPRS Technical Manual: GUI Version*

*CPRS Release Notes: v32b*

*CPRS v32b Follow-Up Build Deployment, Installation, Back Out and Rollback Guide*

## 2 Pre-requisites

N/A

### Pre-requisite Patches

N/A

## 3 Reporting Issues

To report issues with CPRS v32b, please enter a ticket with the National Help Desk.

## 4 Pre- and Post-Installation Checklist

The following activities should be completed in order. Use this checklist and the following sections for both your test/mirror system as well as your production system.

Table 1 Installation Checklist

| ## No.   | ## Task                                                                                                                                     | ## Done   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|          | Complete the pre-installation steps. (See Section 5.)                                                                                       |           |
|          | Notify your ITOPS regional installer that your site is ready for installation.                                                              |           |
|          | Make sure that the installation was completed.  (See the “CPRS v32b Follow-Up Build Deployment, Installation, Back Out and Rollback Guide”) |           |
|          | Complete the post-installation steps. (See Section 6.)                                                                                      |           |
|          | Verify the installation was successful. (See Section 7.)                                                                                    |           |

## 5 Pre-Installation Steps

There are six steps in the pre-installation:

| **Step**                                                                    | **Responsible Point of Contact (POC)**                                                  |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Ensure that All Immunization Lot Numbers Have Been Entered into the System. | Pharmacy Administrator                                                                  |
| Determine Current Coversheet Settings.                                      | Clinical Application Coordinator (CAC) and IT Operations and Services (ITOPS) personnel |
| Determine Note Titles for the Coversheet Immunization Functionality.        | CAC or Clinical Reminder Manager                                                        |
| Back Up National Reminder Dialogs Immunization Entries.                     | CAC or Clinical Reminder Manager                                                        |
| Run the Reminder Dialog CPRS 32 Pre-Conversion Report.                      | CAC or Clinical Reminder Manager                                                        |
| Review Local Reminder Definition for Immunization and Skin Text.            | CAC or Clinical Reminder Manager                                                        |
| Ensure that the Appropriate Recipients Belong to the OR CACS Mailgroup.     | CAC                                                                                     |

### Ensure that All Immunization Lot Numbers Have Been Entered into the System

In CPRS v32b, a user must select a lot number from a pre-populated list when documenting a VA-administered immunization. A pharmacy administrator must populate the immunization lots BEFORE CPRS v32b is installed.

For more information on how to pre-populate vaccine lots, refer to Sections 6.2 (‘LOT Immunization Lot Add/Edit/Display’) and 6.3 (‘Key Concepts’) in the Patient Care Encounter (PCE) User Manual on the [VA Software Document Library (VDL)](http://www.va.gov/vdl) .

**WARNING:** If the vaccine lots are not pre-populated, a user will not be able to document VA-administered immunizations in CPRS.

### Determine Current Coversheet Settings

The CAC needs to see the List of Values for the ORWCV1 COVERSHEET LIST parameter. CACs who do not have access to the General Parameters Menu can submit a YourIT ticket for ITOPS to provide the information.

1. On the General Parameter Tools screen, at the “Select General Parameter Tools Option” prompt, enter “LV” for List Values for a Selected Parameter. **Example – Select List Values for a Selected Parameter**

Select OPTION NAME: XPAR MENU TOOLS       General Parameter Tools

LV     List Values for a Selected Parameter

LE     List Values for a Selected Entity

LP     List Values for a Selected Package

LT     List Values for a Selected Template

EP     Edit Parameter Values

ET     Edit Parameter Values with Template

EK     Edit Parameter Definition Keyword

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: LV  List Values for a Sele

cted Parameter

1. At the “Select Parameter Definition Name” prompt, enter “ORWCV1 COVERSHEET LIST” for List of Coversheet Reports.

**Example – List of Coversheet Reports**

Select PARAMETER DEFINITION NAME:    ORWCV1 COVERSHEET LIST   List of coversheet

reports

Values for ORWCV1 COVERSHEET LIST

Parameter                      Instance             Value

----------------------------------------------------------------------------

USR: CPRS,PROVIDER             1                    ORCV ACTIVE PROBLEMS

USR: CPRS,PROVIDER             2                    ORCV ALLERGIES

USR: CPRS,PROVIDER             2.1                  ORCV WOMEN'S HEALTH

USR: CPRS,PROVIDER             3                    ORCV POSTINGS

USR: CPRS,PROVIDER             4                    ORCV ACTIVE MEDICATIONS

USR: CPRS,PROVIDER             5                    ORCV CLINICAL REMINDERS

USR: CPRS,PROVIDER             6                    ORCV RECENT LAB RESULTS

USR: CPRS,PROVIDER             7                    ORCV VITALS

USR: CPRS,PROVIDER             8                    ORCV APPOINTMENTS

USR: CPRS,PROVIDER             9                    ORCV IMMUNIZATIONS

PKG: ORDER ENTRY/RESULTS REPOR 1                    ORCV ACTIVE PROBLEMS

PKG: ORDER ENTRY/RESULTS REPOR 2                    ORCV ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 3                    ORCV POSTINGS

PKG: ORDER ENTRY/RESULTS REPOR 4                    ORCV ACTIVE MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 5                    ORCV CLINICAL REMINDERS

PKG: ORDER ENTRY/RESULTS REPOR 6                    ORCV WOMEN'S HEALTH

PKG: ORDER ENTRY/RESULTS REPOR 7                    ORCV RECENT LAB RESULTS

PKG: ORDER ENTRY/RESULTS REPOR 8                    ORCV VITALS

PKG: ORDER ENTRY/RESULTS REPOR 8.1                  ORCV IMMUNIZATIONS
PKG: ORDER ENTRY/RESULTS REPOR 9

1. If the site’s CACs can’t access the ORWCV1 COVERSHEET LIST, then IT will send it to them.

**NOTE:** For the CAC, if any items do not start with the “PKG:” value, the site will need to add the ORCV IMMUNIZATION section to the CPRS coversheet at the System level.  

Updating the local CPRS coversheet settings can be done either before or after the patch is installed at the site.  Instructions for updating the coversheet settings are in Section 6.3 (Map local note titles to the CPRS CoverSheet Immunization Form).

### Determine Note Titles for the CoverSheet Immunization functionality

For the CPRS CoverSheet Immunization functionality to work, a local Note Title must be defined. CPRS v32b allows an authorized user to define a Note Title at the System and/or Division levels.

The site CAC should create a new Note Title or determine if an existing note title can be used.

### Back Up National Reminder Immunization Dialogs Immunization Entries

To install the updated national reminder content for immunizations, follow the pre-install instructions located in the guide below:

REDACTED

### Run the Reminder Dialog CPRS 32 Pre-Conversion Report

CPRS v32b runs a conversion routine that updates local and National Dialogs elements/groups for Immunization and Skin Test Finding.

Sites should run the CPRS 32 pre-conversion report to find a list of dialog items that will need to be reviewed after the patch is installed. The report can be found by running this option:

Reminder Dialog CPRS 32 pre conversion report on the DIALOG REPORT menu.

**WARNING:** After the national release of CPRS GUI v32b, it was reported that some sites have encountered an error when running the pre-conversion report. The error prevents the report from running to completion.

If you encounter this error, please send an email to REDACTED.  A member of the team will work with your facility to correct the underlying data issue(s) causing the error. This error must be corrected before installing CPRS v32b.

1. On the Reminders Managers Menu screen, at the “Select Action” prompt, enter “DM” for Reminder Dialog Management. **Example – Reminder Managers Menu screen**

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

**DM     Reminder Dialog Management ...**

CP     CPRS Reminder Configuration ...

RP     Reminder Reports ...

MST    Reminders MST Synchronization Management ...

PL     Reminder Patient List Menu ...

PAR    Reminder Parameters ...

VS     NLM Value Set Menu

ROC    Reminder Order Check Menu ...

CQM    NLM Clinical Quality Measures Menu

XM     Reminder Extract Menu ...

&lt;CPM&gt; Select Reminder Managers Menu &lt;TEST ACCOUNT&gt; Option: DM  Reminder Dialog 
Management

1. At the “Select Reminder Dialog Management Option” prompt, enter “DR” for Dialog Report. **Example – Reminder Dialog Management Option menu**

DP     Dialog Parameters ...

DI     Reminder Dialogs

**DR     Dialog Reports ...**

&lt;CPM&gt; Select Reminder Dialog Management &lt;TEST ACCOUNT&gt; Option: DR  Dialog Reports

1. At the “Select Dialog Reports Option” prompt, enter “32” for 32 pre conversion report.

**NOTE** : 	Each local dialog element/group in the RESOLUTION TYPE, DIALOG/PROGRESS NOTE TEXT report and the ALTERNATE PROGRESS NOTE TEXT fields needs to be reviewed for possible changes. Local dialogs that contains these elements and groups for other modifications that may be needed must also be reviewed. Removed elements for VIS sheet, contraindications and locations will no longer be necessary in your local reminder dialogs.

**Example – 32 pre conversion report**

OR     Reminder Dialog Elements Orphan Report
   ER     Empty Reminder Dialog Report

CH     Check Reminder Dialog for invalid items

ALL    Check all active reminder dialog for invalid items

SEA    Reminder Dialog Search Report

**32     Reminder Dialog CPRS 32 pre conversion report**

&lt;CPM&gt; Select Dialog Reports &lt;TEST ACCOUNT&gt; Option: 32  Reminder Dialog CPRS 32 p

re conversion report

The following dialog items will automatically be converted with the install

of CPRS 32 to only contain Immunization or Skin Test findings.

Each section describes what will happen to the dialog definitions when

CPRS 32 is installed

After CPRS 32, dialog definitions cannot contain both an immunization AND

a skin test finding. The following dialog definitions will be

disabled upon patch install. Please review and update this section

before installing CPRS 32. To avoid that action, please review and

update items listed in this section before installing CPRS 32.

-------------------------------------------------------------------

dialog element: IMM AND SK

For dialog definitions that contain immunization/skin test findings and

another type of finding (i.e, Health Factor, Taxonomy, exams, etc...),

the NON immunization/skin test findings will be removed from the following

dialog definitions.

-------------------------------------------------------------------

dialog group: VA-GP IM PNEUMOC PPSV23 PNEUMOVAX

dialog group: IM PNEUMOC NR

dialog element: IM AND HF

dialog element: HF AND ST

dialog group: IM PNEUMOC

dialog element: IMMUNIZATION FLU DEMO

dialog element: VA-IM FLU H1N1 OUTSIDE (1 DOSE)

dialog element: VA-IM FLU H1N1 DONE (1 DOSE)

dialog element: VA-IM FLU HIGH DOSE DONE

dialog element: VA-IM FLU HIGH DOSE OUTSIDE

dialog group: VA-GP IM PNEUMOC PCV13 PREVNAR

dialog group: GP IM TDAP ADMINISTERED

dialog group: GP IM TD PRESERV FREE ADMINISTERED

dialog group: GP IM TD ADSORBED GENERIC ADMINISTERED

dialog group: GP HERPES ZOSTER ADMIN TODAY

Any prompts assigned to the dialog definitions that contain

immunization/skin test finding will be removed when CPRS 32 is installed.

-------------------------------------------------------------------

dialog element: IM HEP B DONE ELSEWHERE 2ND DOSE NURSE DIALOG

dialog element: IM HEP B DONE ELSEWHERE NURSE DIALOG

dialog element: IM HEP B DONE INJ DIALOG

dialog element: IM HEP B DONE 2ND DOSE INJ DIALOG

dialog element: IM HEP B DONE 3RD DOSE INJ DIALOG

dialog element: IM HEP B DONE ELSEWHERE 3RD DOSE NURSE DIALOG

dialog element: IM TETANUS DONE PREVIOUSLY NURSE DIALOG

dialog element: IM PNEUMOVAX DONE ELSEWHERE NURSE DIALOG

dialog element: IM FLU DONE ELSEWHERE NURSE DIALOG

dialog element: IMMUNIZATION

dialog element: SKIN TEST

dialog element: PPD

dialog element: VA-IM OUTSIDE PNEUMO PCV13

dialog element: VA-IM OUTSIDE PNEUMO PCV13 (1)

dialog element: VA-IM OUTSIDE TDAP

dialog element: VA-IM OUTSIDE TD

dialog element: VA-IM OUTSIDE PNEUMO PPSV23

dialog element: VA-HERPES ZOSTER HISTORICAL DETAILS

dialog element: IM PNEUMO-VAC DONE

dialog element: IM PNEUMO-VAC CONTRA

dialog element: IM PNEUMO-VAC DONE ELSEWHERE

dialog element: ST PPD DONE

dialog element: ST PPD DONE ELSEWHERE

dialog element: IM PNEUMO-VAC DONE ELSEWHERE (1)

dialog element: EX DIABETIC EYE EXAM DONE ELSEWHERE

dialog element: ST PPD

dialog element: IM HEP A DONE ELSEWHERE 2ND DOSE NURSE DIALOG

dialog element: IM HEP A DONE ELSEWHERE NURSE DIALOG

dialog element: IM HEP A 2ND DOSE DONE INJ D

dialog element: IM HEP A DONE INJ DIALOG

dialog element: IM PNEUMOVAX BOOSTER NURSE DIALOG

### Review local Reminder Definition for Immunization and Skin Test

The new Immunization/Skin Test functionality provides a quick way for a user to see what immunization/skin test reminders are due for a patient. The patch will map the appropriate National Clinical Reminder Definitions to the Immunization/Skin Test form.

**NOTE:** Sites will need to add any local Clinical Reminder Definition they want to see in the Immunization/Skin Test form after the patch has been installed.

**NOTE:** Sites should review their local Clinical Reminder Definition to determine which local Clinical Reminder Definition to assign to the form after the patch has been installed.

### Ensure That Appropriate Recipients Belong to the OR CACS Mailgroup

If needed, add recipients to the OR CACS Mailgroup so that they can receive the CLINIC PICKUP QUICK ORDER CONVERSION message after the installation and the related task job has completed. (See post-install instruction 6.7 - Review the CLINIC PICKUP QUICK ORDER CONVERSION MailMan Message for more details.)

## 6 Post-Installation Steps

Post-Installation steps are:

| **Step**                                                                                   | **Responsible POC**                                                      |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Install the Reminder Content.                                                              | Reminders Manager                                                        |
| Reinstall Backup Reminder Exchange File from the Pre-Install Step.                         | Reminders Manager                                                        |
| Map Local Note Titles to the CPRS Coversheet Immunization Form.                            | CAC                                                                      |
| Assign a Local Clinical Reminder Definition to the Immunization/Skin Test Form (optional). | Reminders Manager and CAC (Reminders Manager gives the list to the CAC.) |
| Update the CPRS Coversheet Settings to Show the Immunization Section.                      | CAC                                                                      |
| Review and Update Any Local Reminder Dialogs.                                              | Reminders Manager                                                        |
| Update Quick Orders for Indication Prompt and Titration.                                   | CAC                                                                      |
| Review the CLINIC PICKUP QUICK ORDER CONVERSION MailMan message.                           | CAC                                                                      |
| Review both the ORDER REASON file (#100.03) and the OR DC REASON LIST parameter            | CAC                                                                      |
| Review the OR RTN PROCESSED ALERTS parameter                                               | CAC                                                                      |
| Review the PSO PARK ON parameter                                                           | CAC                                                                      |

### Install Reminder Content

To install the updated national reminder content for immunizations, follow the install instructions located in the guide below:

REDACTED

### Map local note titles to the CPRS CoverSheet Immunization Form

Under the CPRS Configuration (Clin Coord) menu, there is a new option:  Immunization/Skin Test Data Entry parameters. This option allows you to assign information for the Immunization/Skin Test Form.

1. At the “CPRS Manager Menu Option” prompt, enter “PE” for CPRS Configuration (Clin Coord).

**Example – CPRS Manager Menu screen**

Select OPTION NAME: ORMGR       CPRS Manager Menu

CL     Clinician Menu ...

NM     Nurse Menu ...

WC     Ward Clerk Menu ...

PE     CPRS Configuration (Clin Coord) ...

IR     CPRS Configuration (IRM) ...

Select CPRS Manager Menu &lt;TEST ACCOUNT&gt; Option: **PE  CPRS Configuration (Clin Coord)**

1. On the CPRS Configuration (Clin Coord) screen, at the “Select CPRS Configuration (Clin Coord) Option” prompt, enter “IS” for Immunization/Skin Test Data Entry parameters.

**Example – CPRS Configuration (Clin Coord) Menu screen**

AL     Allocate OE/RR Security Keys

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

CS     Controlled Substance Order Anomalies

IS     Immunization/Skin Test Data Entry parameters ...

CI     Consults Clinically Indicated Date Default

DL     Default Locations Administration

DO     Event Delayed Orders Menu ...

KK     Check for Multiple Keys

LO     Lapsed Orders search

PM     Performance Monitor Report

Select CPRS Configuration (Clin Coord) &lt;TEST ACCOUNT&gt; Option: **IS  Immunization/Skin Test Data Entry parameters**

1. At the “Select Immunization/Skin Test Data Entry parameters Option” prompt, enter “NT” for Immunization Note Title.
2. At the “Enter selection” for Immunization CoverSheet Document Title prompt, enter the appropriate selection.  In the example below, the user entered “6” (System). **Example – Immunization/Skin Test Data Entry parameters Option screen**

NT     Immunization Note Title

IM     Immunization Reminder Definitions

ST     Skin Test Reminder Definitions

SEQ    Edit Sequence for Immunization Forms

Select Immunization/Skin Test Data Entry parameters &lt;TEST ACCOUNT&gt; Option: **NT  Immunization Note Title**

Immunization CoverSheet Document Title may be set for the following:

5   Division      DIV    [choose from INSTITUTION]

6   System        SYS    [REDACTED]

Enter selection: 6  System   REDACTED

Setting Immunization CoverSheet Document Title  for System: REDACTED

Document Title: IMMUNIZATION NOTE       TITLE   This is the note title from the preinstall step

Std Title: IMMUNIZATION PROGRESS NOTE

### Assign Local Clinical Reminder Definition to the Immunization/Skin Test form (optional)

The Immunization/Skin Test Data Entry menu option allows a site to add a local Clinical Reminder Definition to the Immunization/Skin Test form.

1. Verify that you have executed all the steps in Section 6.2 (Map local note titles to the CPRS CoverSheet Immunization Form).
2. At the “Select Immunization/Skin Test Data Entry parameters Option”, enter “IM” for Immunization Reminder Definitions.
3. At the “Enter Selection” prompt, enter the appropriate selection.  In the example below, the user entered “6” for System. **Example – Immunization Reminder Definitions screen**

Setting Immunization CoverSheet Document Title  for System: REDACTED

Document Title: IMMUNIZATION NOTE       TITLE

Std Title: IMMUNIZATION PROGRESS NOTE

NT     Immunization Note Title

IM     Immunization Reminder Definitions

ST     Skin Test Reminder Definitions

SEQ    Edit Sequence for Immunization Forms

Select Immunization/Skin Test Data Entry parameters &lt;TEST ACCOUNT&gt; Option: im  Immunization Reminder Definitions

Immunization Reminders may be set for the following:

1   User          USR    [choose from NEW PERSON]

4   Location      LOC    [choose from HOSPITAL LOCATION]

5   Division      DIV    [choose from INSTITUTION]

6   System        SYS    [REDACTED]

7   Package       PKG    [ORDER ENTRY/RESULTS REPORTING]

Enter selection: 6  System   REDACTED

---- Setting Immunization Reminders  for System: REDACTED ----

### Update the CPRS Coversheet Settings to Show the Immunization Section

Sites can add the Immunization form to the CPRS Coversheet by adding the ORCV IMMUNIZATION section to the local coversheet from the pre-install steps.

1. On the CPRS Configuration (Clin Coord) menu, at the “CPRS Configuration (Clin Coord) Option” prompt, enter “gp” for GUI Parameters. **Example – Immunization Reminder Definitions screen**

CPRS Configuration (Clin Coord) menu

AL     Allocate OE/RR Security Keys

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

CS     Controlled Substance Order Anomalies

IS     Immunization/Skin Test Data Entry parameters ...

CI     Consults Clinically Indicated Date Default

DL     Default Locations Administration

DO     Event Delayed Orders Menu ...

KK     Check for Multiple Keys

LO     Lapsed Orders search

PM     Performance Monitor Report

Select CPRS Configuration (Clin Coord) &lt;TEST ACCOUNT&gt; Option: **gp  GUI Parameters**

1. At the “Select GUI Parameters Option” prompt, enter “CS” for GUI Cover Sheet Display Parameters **Example – GUI Parameters screen**

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

OTH    GUI Add/Edit Local Message for OTH Button

CLOZ   GUI Edit Inpatient Clozapine Message

COAG   GUI Anticoagulation Parameters ...

DEA    GUI ePCS Management Menu ...

DST    GUI Consults DST/CTB Configuration ...

EIE    GUI Mark Allergy Entered in Error

OF     GUI Order Flagging/Unflagging Setup ...

Select GUI Parameters &lt;TEST ACCOUNT&gt; Option: **cs  GUI Cover Sheet Display Parameters**

1. At the “Select GUI Cover Sheet Display Parameters Option” prompt, enter the appropriate selection.  In the example below, the user entered “sy” for GUI Cover Sheet System Display Parameters.
2. The Cover Sheet Parameters will display.  List of coversheet reports is the only section that should be modified.
3. At the “Select Sequence” prompt, enter the appropriate sequence number.  In the example below, the user entered “9”. **Example – GUI Cover Sheet Display Parameters screen**

SY     GUI Cover Sheet System Display Parameters

DI     GUI Cover Sheet Division Display Parameters

SE     GUI Cover Sheet Service Display Parameters

LO     GUI Cover Sheet Location Display Parameters

US     GUI Cover Sheet User Display Parameters

Select GUI Cover Sheet Display Parameters &lt;TEST ACCOUNT&gt; Option: **sy  GUI Cover Sheet System Display Parameters**

GUI Cover Sheet - System for System: REDACTED

------------------------------------------------------------------------------

Inpatient Lab Number of Days to Display           60

Outpatient Lab Number of Days to Display          120

Enc Appt Range Start Offset

Enc Appt Range Stop Offset

Future Days Limit For PCE Selection

Cover Sheet Visit Range Start

Cover Sheet Visit Range Stop

Clinical Reminders for Search

List of coversheet reports

Cover Sheet Retrieval Mode    ORCV ACTIVE PROBLEMS NO

ORCV ALLERGIES      NO

ORCV POSTINGS       NO

ORCV ACTIVE MEDICATIONS NO

ORCV RECENT LAB RESULTS NO

ORCV VITALS         NO

ORCV APPOINTMENTS   NO

------------------------------------------------------------------------------

Inpatient Lab Number of Days to Display: 60//

Outpatient Lab Number of Days to Display: 120//

Enc Appt Range Start Offset:

Enc Appt Range Stop Offset:

Future Days Limit For PCE Selection:

CS Visit Search Start:

CS Visit Search Stop:

For Clinical Reminders for Search -

Select Display Sequence:

For List of coversheet reports -

Select Sequence: 9  Enter Sequence Number

Sequence: 9//    9

Coversheet Report: ORCV IMMUNIZATIONS     Select ORCV IMMUNIZATION

### Update Any Local Reminder Dialogs

At this stage in the post-install process, sites should update any local Reminder Dialogs that need to be updated.

### Update Quick Orders for Indication Prompt and Titration

Two new Quick Orders conversion options have been added to Order Menu Management:

- Update Meds Quick Orders for indication prompt
- Update Outpatient Complex Meds QO for titration

Both options provide a fast way to find Quick Orders that need to be reviewed and updated for the changes in CPRS v32b.

An example of updating Quick Orders for indication prompt and titration is listed below.

1. On the Order Menu Management screen, at the “Select Order Menu Management Option” prompt, enter “RPTS” for Quick Order report/conversion utilities. **Example – Order Menu Management screen**

Select OPTION NAME: ORDER MENU MANAGEMENT  ORCM MGMT     Order Menu Management

OI     Manage orderable items …
   PM     Enter/edit prompts
   GO     Enter/edit generic orders
   QO     Enter/edit quick orders
   QU     Edit personal quick orders by user
   ST     Enter/edit order sets
   AC     Enter/edit actions
   MN     Enter/edit order menus
   AO     Assign Primary Order Menu
   CP     Convert protocols
   SR     Search/replace components
   LM     List Primary Order Menus
   DS     Disable/Enable order dialogs
   AP     Update AP Order Dialogs
   RPTS   Quick Order report/conversion utilities ...

Select Order Menu Management &lt;TEST ACCOUNT&gt; Option: **RPTS  Quick Order report/conversion utilities**

1. At the “Select Quick Order Report/Conversion Utilities” prompt, enter “IN” for Update Meds Quick Orders for indication prompt. **Example – Quick Order Report/Conversion Utilities screen**

CS     Review Quick Orders for Inactive ICD9 Codes
   MR     Medication Quick Order Report
   IN     Update Meds Quick Orders for indication prompt
   TI     Update Outpatient Complex Meds QO for titration
   CA     Quick Order Mixed-Case Report
   CO     Create Clinic Order QOs from Inpatient QOs
   CV     Convert IV Inpatient QO to Infusion QO
   DF     Quick Order Free-Text Report
   FR     IV Additive Frequency Utility
   SP     SUPPLY COVERSION UTILITY MENU ...

Select Quick Order report/conversion utilities &lt;TEST ACCOUNT&gt; Option: **IN Update Meds Quick Orders for Indication prompt**

1. At the “Select which quick orders to convert” prompt, enter a value from the list.  In the example below, the user entered “1 All medication and supplies Quick Orders”. **Example – “Select which quick orders to convert” option**

This option provides a quick way to update Quick Orders for the new indication prompt. This option will prompt filtering questions to help decrease the number of Quick Orders to  review in a session. For each Quick Orders that is found the user will automatically enter the Quick Order Editor.

Select one of the following:

1         All medication and supplies Quick Orders
          2         Clinic Medications
          3         Clinic Infusions
          4         Infusion
          5         Non-VA Meds (Documentation)
          6         Out. Meds
          7         Supplies
          8         Inpt. Meds

Select which quick orders to convert: **1  All medication and supplies Quick Orders**

1. At the “Select prompt conditions” prompt, enter a value from the list.  In the example below, the user entered “B Both populated comment and no Indication field defined”. **Example – “Select prompt conditions” prompt**

Select one of the following:

B         Both populated comment and no Indication field defined
          C         Populated Comment Only
          I         No Indication field defined

Select prompt conditions: **B Both populated comment and no Indication field defined**

1. At the “Which QO to convert?” prompt, enter a value from the list and at the “Skip disable quick orders?” prompt, enter Yes.  In the example below, the user entered “M QO Assigned to Order Menus, Order Sets, or Reminder Dialogs”. **Example – “Select prompt conditions” prompt**

Select one of the following:

A         ALL (excluding personal quick order)
          M         QO ASSIGNED TO ORDER MENUS, ORDER SETS, OR REMINDER DIALOGS
          N         QO NOT ASSIGNED TO ANY OF THESE ITEMS
          P         PERSONAL QUICK ORDER REPORT
          S         SPECIFIC QUICK ORDER
          R         REPORT OUTPUT ONLY
          Q         QUIT THE UPDATE UTILITY

Which QO to convert?: **M  QO ASSIGNED TO ORDER MENUS, ORDER SETS, OR REMINDER DIALOGS** Skip Disable Quick Orders? Yes//

1. Update a quick order.  In the example below, the user entered “E Edit This Quick Order” at the “Select the Action” prompt and edited the Comments. **Example – Updating a Quick Order**

Collecting Quick Order List, this may take some time

Finding Quick Orders \

Searching Reminder Dialogs /

Processing Quick Order List

Before value:

-------------------------------------------------------------------------------

Name: PSJQ182 CIMETIDINE
                        Type: Quick Order
                Display Text: CIMETIDINE 400MG QHS
               Display Group: UNIT DOSE MEDICATIONS
                     Package: INPATIENT MEDICATIONS
                  Medication: CIMETIDINE TAB  400MG
                Instructions: 400MG ORAL QHS
                    Priority: ROUTINE
                    Comments:   ...

------------------------------------------------------------------------------

Select one of the following:

E         EDIT THIS QUICK ORDER
          K         SKIP THIS QUICK ORDER
          Q         QUIT THE CONVERSION UTILITY

Select the action: E// EDIT THIS QUICK ORDER

NAME: PSJQ182 CIMETIDINE// 
DISPLAY TEXT: CIMETIDINE 400MG QHS  Replace 
VERIFY ORDER: YES// 
DESCRIPTION:
Take medicine at bedtime.

Edit? NO// 
ENTRY ACTION:

Medication: CIMETIDINE TAB // 
Complex dose? NO// 
Dose: 400MG// 
Route: ORAL// 
Schedule: QHS// 
Give additional dose NOW? NO// 
Priority: ROUTINE// 
Indication: 
Comments: 
  Edit? No// **Y  (Yes)**

1. Place and auto-accept a quick order and then, process the next quick order. In the example below, the user edited the comments and entered “Place” at the “(P)lace, (E)dit, or (C)ancel this quick order?” prompt.  At the “Auto-accept this quick order? YES” prompt, the user clicked the Enter key and at the “Process next Quick Order?” prompt, the user entered “Yes”.

**Example – Placing and auto-accepting a quick order**

==[ WRAP ]==[INSERT ]===============&lt; Comments &gt;=====[Press &lt;PF1&gt;H for help]====

TAKE MEDICINE WITH FOOD.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

-------------------------------------------------------------------------------

Medication: CIMETIDINE TAB  400MG

Instructions: 400MG ORAL QHS

Priority: ROUTINE

Comments:  TAKE MEDICINE WITH FOOD.

-------------------------------------------------------------------------------

(P)lace, (E)dit, or (C)ancel this quick order? PLACE// **PLACE**

Auto-accept this order? YES//

After value:

-------------------------------------------------------------------------------

Name: PSJQ182 CIMETIDINE

Type: Quick Order

Display Text: CIMETIDINE 400MG QHS

Display Group: UNIT DOSE MEDICATIONS

Package: INPATIENT MEDICATIONS

Medication: CIMETIDINE TAB  400MG

Instructions: 400MG ORAL QHS

Priority: ROUTINE

Comments:  TAKE MEDICINE WITH FOOD.

-------------------------------------------------------------------------------

Process next Quick Order? Yes// **YES**

1. Edit the next quick order, skip the next quick order or quit the conversion utility.  In the example below, the user entered “Q Quit the Conversion Utility” at the “Select one of the following” prompt. **Example – Quitting the Conversion Utility**

Before value:

-------------------------------------------------------------------------------

Name: PSJQ264 MAALOX
                        Type: Quick Order
                Display Text: MAALOX XS+ Q4H PRN
               Display Group: UNIT DOSE MEDICATIONS
                     Package: INPATIENT MEDICATIONS
                  Medication: MAALOX EXTRA STRENGTH SUSP,ORAL
               Dispense Drug: ALOH/MGOH/SIMTH EXTRA STRENGTH 30ML U/D
                Instructions: 15ML OF ALOH/MGOH/SIMTH EXTRA STRENGTH 30ML U/D OR AL Q4H PRN
                    Priority: ROUTINE
                    Comments: FOR GI UPSET
-------------------------------------------------------------------------------

Select one of the following:

E         EDIT THIS QUICK ORDER
          K         SKIP THIS QUICK ORDER
          Q         QUIT THE CONVERSION UTILITY

Select the action: E// **Q**

1. Update outpatient complex meds quick orders for titration by repeating steps #1 through #7.

### Review the CLINIC PICKUP QUICK ORDER CONVERSION MailMan Message

Review the CLINIC PICKUP QUICK ORDER CONVERSION MailMan message to determine if any quick orders need a new default Pickup value.

If needed, update the Pickup value to a new routing (MAIL, WINDOW or PARK) by using the Enter/Edit Quick Orders [ORCM QUICK ORDERS] option.

### Review the ORDER REASON file (#100.03) and the OR DC REASON LIST parameter

CPRS v32b distributes a new order reason: Allergy/Adverse Drug Reaction.

It is possible that a site may already have an order reason in either the ORDER REASON file (#100.03) or the parameter, OR DC REASON LIST.

Please review both the ORDER REASON file (#100.03) and the OR DC REASON LIST parameter to ensure you don't have any duplicate reasons.

### Review the OR RTN PROCESSED ALERTS parameter

Verify that OR RTN PROCESSED ALERTS is set to “Yes”.  If your site starts to have latency issues because too many processed alerts are loading, set OR RTN PROCESSED ALERTS to “No” and no processed alerts will be returned.

### Review the PSO PARK ON parameter

Verify that the PSO PARK ON parameter is set to “No”.  The Park parameter should stay disabled until downstream systems can handle the Park status.

## 7 Verify Successful Installation

At this point, sites may use a locally developed smoke test script to verify that the installation and configuration were successful.