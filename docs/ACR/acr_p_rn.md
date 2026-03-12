---
app_name: Ambulatory Care Reporting (ACR)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: release-notes
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: ACR
patch: null
patch_gap: null
section: ''
source_file: acr_p_rn.docx
status: draft
title: acr p rn.docx
---

**Scheduling V. 5.3**

**Ambulatory Care Reporting Project (ACRP)**

**Incomplete Encounter Management Module (IEMM) Release Notes**

**Patches SD*5.3*66, DG*5.3*139, PX*1.0*41**

**January 1998**

**Technical Release Notes**

New Options

New Bulletin

New Protocols

New Background Job

New Print Templates

New Sort Templates

Modified Input Template

Modified Print Template

New Security Keys

Event Handler Changes

Data Dictionary Changes

Database Integration

Routine Mapping

Routine Summary

Scheduling Routines

Registration Routines

PCE Routines

**User Release Notes**

Introduction

Validator

Error Correction Tools

New Menu Options

New Bulletin

New Security Keys

Registration (DG) Changes

Technical Release Notes

**New Options**

SCENI IEMM ERROR CORRECTION   [Correct Incomplete Encounters]

This option allows a user to correct the errors to an encounter or patient demographic.  The correction protocols of this option are locked by the SCENI IEMM EDIT and SCENI ENCOUNTER EDIT security keys.  Please review the New Security Key section for further details.

SCENI IEMM ERROR REPORT   [Incomplete Encounter Error Report]

This option allows the user to obtain a list of incomplete encounters.

SCENI IEMM ERROR SORT   [Incomplete Encounters by Error Code]

This option provides the user with a list of the errors which are in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file (#409.76).

SCENI IEMM MAIN MENU   [Incomplete Encounter Management]

This menu holds the SCENI IEMM REPORTS MENU submenu and the SCENI IEMM ERROR CORRECTION option.

SCENI  IEMM REPORTS MENU   [Incomplete Encounter Reports]

This menu contains the following options.

SCENI IEMM ERROR REPORT [Incomplete Encounter Error Report]

SCENI IEMM ERROR SORT [Incomplete Encounters by Error Code]

SCENI IEMM SUMMARY REPORT [Summary Report - IEMM]

SCENI PT ALPHA LIST [Alpha List of Incomplete Encounters]

SCENI  IEMM SUMMARY BULLETIN   [IEMM Summary Bulletin]

This option can be scheduled to run nightly to produce the summary report.  It will generate a bulletin; thus no output device is needed.  The bulletin produced is SCDX INCOMPLETE ENCOUNTER MGMT.

SCENI  IEMM SUMMARY REPORT   [Summary Report - IEMM]

This option allows a user to gather summary information about the number of encounters sent and accepted.

SCENI OP ENCOUNTER EDIT   [Edit Outpatient Encounter]

This option allows a user to edit actual encounter-specific data.  It is locked by the SCENI ENCOUNTER EDIT security key.  It is located on the [SCENI OP ENCOUNTER EDIT] Supervisor Ambulatory Care menu.

SCENI PT ALPHA LIST   [Alpha List of Incomplete Encounters]

This option allows the user to print a list of all errors found in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) at the time the report is generated.

**New Bulletin**

SCDX INCOMPLETE ENCOUNTER MGMT

This bulletin is used when the Incomplete Encounter report is scheduled as a nightly job.  A mail group must be assigned to this bulletin.

**New Protocols**

SCENI CALL LOAD EDIT	Load/Edit Patient Data

SCENI CHANGE CLINIC	Clinic Change

SCENI CHANGE DATE RANGE	Date Range Change

SCENI CHANGE DIVISION	Change Division

SCENI CHANGE ERROR CODE	Error Code Change

SCENI CHANGE PATIENT	Select Patient

SCENI CHECKOUT INTERVIEW	Check Out

SCENI CORRECT ERROR	Correct Error(s)

SCENI DISPLAY ERRORS	Display Error(s)

SCENI DISPLAY ERRORS MENU	Display Errors

SCENI ENCOUNTER INFORMATION	Encounter Information

SCENI EXPAND ENCOUNTER	Expand Encounter

SCENI INCOMPLETE ENC MGMT MENU	Incomplete Encounter Management Menu

SCENI PATIENT DEMOGRAPHICS	Patient Demographics

SCENI REFLAG ERROR	Retransmit Error

SCENI VIEW EXPANDED	View Expanded

**New Background Job**

SCENI IEMM SUMMARY BULLETIN

This is a new background job that may be scheduled.  It will report the same information as the SCENI IEMM SUMMARY REPORT menu option.

**New Print Templates**

Template SCENI ERROR LIST has been added to the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75).  This template is used to print errors sorted by error code.

Template SCENI PAT ALPHA PRINT has been added to the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75).  This template is used to print errors sorted by patient.

Template SCENI ERROR TABLE has been added to the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file (#409.76).  This template is used to print the error codes and their descriptions.  At this time, it may only be accessed through FileMan.

**New Sort Templates**

Template SCENI ERROR SORT has been added to the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75).  This template is used to sort errors by error code.

Template SCENI PT ALPHA SORT has been added to the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75).  This template is used to sort errors by patient.

**Modified Input Template**

Input template SDB, which is used in the clinic setup, has been modified to ask the new clinic parameter - WORKLOAD VALIDATION AT CHK OUT.

**Modified Print Template**

Print template SCDX Transmitted Error List, which is used to display the errors in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75), has been modified to print the source of the error.

**New Security Keys**

New security keys, SCENI IEMM EDIT, SCENI ENCOUNTER EDIT, and SCENI MEANS TEST EDIT lock the following protocols and options.  Because of the nature of the data which can be edited through the Edit Outpatient Encounter option, it is highly recommended that the SCENI ENCOUNTER EDIT security key not be given to all users.

SCENI IEMM EDIT

Patient Demographics	[SCENI PATIENT DEMOGRAPHICS]

Retransmit Error	[SCENI REFLAG ERROR]

Check Out	[SCENI CHECKOUT INTERVIEW]

Load/Edit Patient Data	[SCENI CALL LOAD EDIT]

SCENI ENCOUNTER EDIT

Edit Outpatient Encounter	[SCENI OP ENCOUNER EDIT]

Encounter Information	[SCENI ENCOUNTER INFORMATION]

SCENI MEANS TEST EDIT

This key is used to limit the users who can complete a Means Test through Load/Edit when using the IEMM correction tool.

**Event Handler Changes**

The Ambulatory Care event handler, SCDX AMBCARE EVENT, currently exists as an item on the PIMS event driver, SDAM APPOINTMENT EVENTS.  The post init routine will remove it from the item list and add it to the exit action of that same protocol.  This is to ensure that the capturing and validation of workload data is the last event to be processed.

**Data Dictionary Changes**

1. TRANSMITTED OUTPATIENT ENCOUNTER ERROR file  [^SD(409.75)]

Four new cross references have been added.

On the Transmitted Encounter field (#.01):  AEDT  AECL  AER  ACOD

On the Error Code field (#.02):  AER2  ACOD2

1. TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file  [^SD(409.76)]

Four new fields and one cross reference have been added.

SOURCE OF ERROR (#.02)

CORRECTIVE ACTION DESCRIPTION (#21)

VALIDATION LOGIC (#31)

CORRECTION LOGIC (#41)

The D cross reference has been added.  It is a standard cross reference used to aid in the look up process.

The ERROR CODE DESCRIPTION field is also now an identifier for lookups on this file.

1. HOSPITAL LOCATION file  [^SC(44)]

A new field has been added - WORKLOAD VALIDATION AT CHK OUT (#30).

This field is used to determine if the validation software is to be executed at the completion of a successfully checked-out encounter.

**Database Integration**

Integration Agreement #872 covers the request to manipulate the entries in the item list and exit action of the PROTOCOL file (#101).

**Routine Mapping**

Unless you are currently mapping the routines, there are no routines to map.

**Routine Summary**

The following is a list of the routine(s) included in this patch.  The  second line of each of these routine(s) will look like:

&lt;tab&gt;;;5.3;Registration;**[patch list]**;Aug 13, 1993

CHECK^XTSUMBLD results

Scheduling Routines

Routine Name	Before Patch	After Patch	Patch List

SCDDI1	N/A	1745670	66

SCDXFU02	3122563	3741860	44,110,128,66

SCDXHLDR	6080400	10017200	44,99,126,66

SCDXMSG	9634867	10056881	44,56,70,77,85,96,121,128,66

SCDXMSG0	5570217	5622096	44,59,66

SCDXMSG1	6668616	7196075	44,55,70,77,85,66

SCDXMSG2	10585313	7971963	44,121,128,66

SCDXUTL0	8295487	8316543	44,55,69,77,85,110,122,94,66

SCDXUTL2	896233	1124319	44,66

SCENI0	N/A	9483994	66

SCENI01	N/A	3843218	66

SCENIA0	N/A	4111816	66

SCENIA1	N/A	5640756	66

SCENIA2	N/A	9548930	66

SCENIB0	N/A	1081801	66

SCMSP66	N/A	8192827	44

SCMSVDG1	1982971	2186034	44,57,66,68,77,85,95

SCMSVEVN	957290	1032621	44,66

SCMSVPID	3689679	4228445	44,66

SCMSVPR1	3326948	2939469	44,66

SCMSVPV1	2010769	1967926	44,55,66,91

SCMSVUT0	5348371	6909193	44,55,66

SCMSVUT1	N/A	3244871	66

SCMSVUT2	N/A	2887929	66

SCMSVZCL	1411790	2176494	44,66

SCMSVZEL	1260997	1554752	44,66

SCMSVZIR	1192416	1406995	44,55,66

SCMSVZPD	1035893	1467475	44,66

SCMSVZSC	1517977	1327159	44,66

SCMSVZSP	1333076	1327622	44,66

SCRPI01	N/A	8982029	66

SCRPI01A	N/A	8791303	66

SCRPI02	N/A	6382407	66

SCRPI02A	N/A	9189721	66

SCRPIUT1	N/A	1394343	66

SCUTIE1	N/A	1851598	66

SCUTIE2	N/A	3269018	66

SDCO6	3447088	3488991	27,66

SDCOAM	9105467	9352374	1,20,27,66

Registration Routines

Routine Name	Before Patch	After Patch	Patch List

DG10	3605485	6200881	32,109,139

DGRPE	17405601	17674346	32,114,139

DGRPU1	1362026	1392644	139

PCE Routines

Routine Name	Before Patch	After Patch	Patch List

PXKMASC	4861775	4911140	22,41

PXKCO	973622	3403563	28,41

User Release Notes

**Introduction**

This patch installs the Incomplete Encounter Management Module (IEMM), part of the Ambulatory Care Reporting Project (ACRP) Phase II.  The patch will provide the data validation tools necessary for sites to maintain the correctness of outpatient data being transmitted to the Austin Automation Center.

Validator

The validation logic is a new piece of functionality installed with this patch.  The previous Ambulatory Care software only checked to ensure that a value was present in each data field sent to Austin.  It did not check the validity of that data.  This new software will perform the same validation checks as the Austin database to identify errors before they are transmitted.  The validator (or edit checker) will review the entire encounter rather than stopping after the first error is found.  All errors are stored for later reporting and correction.

This validation will continue to be performed during the nightly background job.  It can also be performed when there is a complete check out for an appointment.  This is provided if the parameter WORKLOAD VALIDATION AT CHK OUT for the respective clinic is set to YES, and an entry exists in the TRANSMITTED OUTPATIENT ENCOUNTER file.  The validation software will also be executed as part of the Correct Incomplete Encounters menu option.

Error Correction Tools

Tools have been developed to help users correct the errors that are found in encounters.  The Correct Incomplete Encounters option allows a user to select, display, and correct errors using a List Manager display format.  After an attempt is made to correct the error, the validator will be run for that encounter to check for any additional errors.  If an error is found it will be presented to the user.  The correction actions of this option are locked with the SCENI IEMM EDIT security key except for the Encounter Information action which is locked with the SCENI ENCOUNTER EDIT security key.

The Edit Outpatient Encounter option allows a user with the SCENI ENCOUNTER EDIT security key to correct specific data for an encounter.  Four data items for the encounter are available for correction:  appointment type, division, clinic stop code, and eligibility.

**New Menu Options**

The Incomplete Encounter Management menu has been added to the Ambulatory Care Reporting menu.  This new menu contains the Incomplete Encounter Reports submenu and the Correct Incomplete Encounters option.

Incomplete Encounter Reports

These reports will only display those errors remaining in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file since the **last** running of the encounter validation software.  This file is dynamic and is updated each time the validator runs.

Alpha List of Incomplete Encounters - This report provides a list of all errors found in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) at the time the report is generated.

Incomplete Encounter Error Report - This report provides a detailed report of errors by patient with a wide range of selection criteria and encounter identifying information.

Incomplete Encounters by Error Code - This report provides a list of the errors which are in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file (#409.76).

Summary Report – IEMM - This report prints a summary showing total encounters for a date range and the number and percentage of incomplete encounters.  The report may be printed as summary only or summary with detail.

Correct Incomplete Encounters - This option allows a user to select, display, and correct errors using a List Manager display format.

The Edit Outpatient Encounter option has been added to the Supervisor Ambulatory Care menu.  It allows you to change four fields which are set by the software and are normally uneditable.

**New Bulletin**

This patch installs a new bulletin, SCDX INCOMPLETE ENCOUNTER MGMT.  This bulletin provides the same information as the Summary Report - IEMM option, but in a bulletin format.  The bulletin is sent to a user-defined mail group.

The nightly bulletin from the processing of the encounters to Austin currently contains all of the encounters with errors.  This has been changed so that the bulletin only contains a summary report.  The individual errors can be viewed through the new report options.

Bulletin Example

Subj: Transmission of data to NPCDB completed  [#4287] 20 Jan 98 13:17  7

Lines

From: POSTMASTER (Sender: Smith,James)  in 'IN' basket.   Page 1  **NEW**

---------------------------------------------------------------------------

Transmission of data to the National Patient Care Database has completed.

A total of 55 Outpatient Encounters were sent.

A total of 41 Outpatient Encounters were not sent.

Please review the IEMM Error listing for further detail.

Select MESSAGE Action: IGNORE (in IN basket)//

**New Security Keys**

New security keys, SCENI IEMM EDIT, SCENI ENCOUNTER EDIT, and SCENI MEANS TEST EDIT lock the following protocols and options.

SCENI IEMM EDIT

Patient Demographics	[SCENI PATIENT DEMOGRAPHICS]

Retransmit Error	[SCENI REFLAG ERROR]

Check Out	[SCENI CHECKOUT INTERVIEW]

Load/Edit Patient Data	[SCENI CALL LOAD EDIT]

SCENI ENCOUNTER EDIT

Edit Outpatient Encounter	[SCENI OP ENCOUNER EDIT]

Encounter Information	[SCENI ENCOUNTER INFORMATION]

SCENI MEANS TEST EDIT

This key is used to limit the users who can complete a Means Test through Load/Edit when using the IEMM correction tool.

**Registration (DG) Changes**

The Load/Edit Patient Data option [DG LOAD PATIENT DATA] has been changed.  The system determines a patient’s need for Means Testing and Copay Testing and, if necessary, now allows you to complete the required test through this option.  For the Copay Test, the veteran has to request the test be completed.

If the user is accessing Load/Edit through the IEMM correction tool, the SCENI MEANS TEST EDIT key will be used to restrict users from completing the Means Test.