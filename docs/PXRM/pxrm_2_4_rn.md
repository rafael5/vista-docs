---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
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
package_id: PXRM
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_4_rn.docx
status: draft
title: pxrm 2 4 rn.docx
---

**Clinical Reminders**

PXRM*2.0*4

**Release Notes**

**October 2006**

HSD&amp;D


## Table of Contents

Clinical Reminders V. 2.0 Patch 4 Documentation	1

Installation Notes	1

Reminder Disclaimer/Health Summary Patch	2

CSUB Explanation	2

General Functionality Changes	3

Reminder Computed Findings	4

Reminder Definitions	6

Reminder Dialogs	9

Reminder Evaluation	9

Reminder Exchange	12

Reminder Extracts	12

Reminder Location Lists	14

Reminder Patient Lists	14

Reminder Reports	20

Reminder Sponsor	25

Reminder Taxonomies	25

Reminder Terms	25

Geriatric Extended Care (GEC)	27

MyHealtheVet	27

CPRS V26 Reminder Changes	28

Remedy Tickets resolved with Patch 4	30

E3Rs Resolved	30

Appendix A: Appointment Computed Findings	32

Appendix B:  HL7 Logical Link Set-up	39


## Patch 4 Release Notes

Summary of fixes and enhancements (details are provided in the following pages):

- Removal of support for the old-style MRD findings
- Restoration and updates of the disclaimer in the Clinical Reminders Health Summary output
- New versions of the VA-HTN ASSSSMENT BP &gt;= 140/90, VA-HTN ASSESSMENT BP &gt;=160/100 reminder definition, and VA-MHV INFLUENZA reminders
- Six new computed findings
- Error trapping enhancements
- New function finding (DIFF\_DATE)
- Changes to the frequency display for CANNOT BE DETERMINED (CNBD)
- New finding modifiers, INCLUDE VISIT DATA and USE START DATE
- USE COND IN FINDING SEACH changed to USE STATUS/COND IN SEARCH
- Major changes to the user interface for patient lists
- A new key, PXRM MANAGER, for patient list options
- Many improvements to Reminder Reports, including expanded types of patient data that can be included in the Demographic Report
- Corrections and enhancements to GEC dialogs and reports, including a new option, Restore or Merge Referrals, in the GEC reports menu
- Name and description changes for Reminder Extract Management options

### Clinical Reminders V. 2.0 Patch 4 Documentation

| **Documentation**   | **Documentation File name**   |
|---------------------|-------------------------------|
| Release Notes       | PXRM_2_4_RN.PDF               |
| Technical Manual    | PXRM_2_4_TM.PDF               |
| Clinician Guide     | PXRM_2_4_UM.PDF               |
| Manager Manual      | PXRM_2_4_MM.PDF               |

### Installation Notes

- PXRM*2*4 disables old-style MRDs. The pre-init for patch 4 checks all reminder definitions to see if any still use the old-style MRD. If so, the build won’t install and a MailMan message is sent to the Clinical Reminders mail group, listing the reminder definitions containing the old-style MRDs. ***Replace any usage of old-style MRDs with Function Findings before proceeding with the installation.***

**Example Install Error Message:**

Patch PXRM*2*4 cannot be installed because some reminders are still using

the old-style MRD. A message is being sent to the reminders mailgroup that

lists the reminders still using the old-style MRD. Please replace the old-style

MRD with a function finding.

PXRM*2.0*4 Build will not be installed, Transport Global deleted!

Oct 10, 2006@15:33:29

- Several file names are changed in patch 4. During the installation of PXRM*2.0*4, KIDS will point out that these files already exist with a different name:

810.2     REMINDER EXTRACT DEFINITION

*BUT YOU ALREADY HAVE 'REMINDER EXTRACT PARAMETER' AS FILE #810.2!

Shall I write over your REMINDER EXTRACT PARAMETER File? YES//

810.7     REMINDER EXTRACT COUNTING RULE

*BUT YOU ALREADY HAVE 'REMINDER EXTRACT FINDING RULE' AS FILE #810.7!

Shall I write over your REMINDER EXTRACT FINDING RULE File? YES//

810.8     REMINDER COUNTING GROUP

*BUT YOU ALREADY HAVE 'REMINDER FINDING GROUP' AS FILE #810.8!

Shall I write over your REMINDER FINDING GROUP File? YES//

Take the default of "YES" for each of the "Shall I write over your xxx " questions.

### Reminder Disclaimer/Health Summary Patch

The disclaimer was not being displayed on the Clinical Reminders Health Summary output, so changes were made to restore and improve the display of the disclaimer.

- A package that calls the Clinical Reminder evaluation API passes an argument that requests the return of the Disclaimer; a change to the way this argument works was made and this required a change to the Health Summary routine that calls for Clinical Reminder evaluation, requiring creation of Health Summary patch GMTS*2.7*75.
- The FileMan text formatter was replaced with the Clinical Reminders text formatter so that “\\” can be used to force line breaks. In the past, the text was formatted every time a Health Summary was run. A new field was added to the Clinical Reminders Parameter file that stores the formatted disclaimer, eliminating the need to format it each time a Health Summary is run.

### CSUB Explanation


When a Reminder Test is run, some elements of the FIEVAL array have a “CSUB” subscript. Example for an orderable item finding:

FIEVAL(5,"CSUB","DURATION")=1774

FIEVAL(5,"CSUB","ORDER")=3366^CA ULTRA^546;99RAP

FIEVAL(5,"CSUB","RELEASE DATE")=3010917.1625

FIEVAL(5,"CSUB","START DATE")=3010917

FIEVAL(5,"CSUB","STATUS")=PENDING

FIEVAL(5,"CSUB","STOP DATE")=

FIEVAL(5,"CSUB","VALUE")=PENDING

Each of the subscripts following “CSUB” may be used in a Condition (hence the abbreviation Condition SUBscript), such as: I V(“DURATION”)&gt;90

The use of “CSUB” data has expanded beyond Condition statements –  the new places where it may be used are described in this document.

### General Functionality Changes

- When Clinical Reminders V.2.0 was released, it was announced that support for the old-style MRD would be removed in a patch; this is the patch that removes it. The pre-init will check all reminder definitions to see if any of them are still using the old-style MRD. If any of them are, the build will not install and a MailMan message listing the reminders that are still using the old-style MRD will be sent to the Clinical Reminders mail group. These will need to be removed before the build can be installed. Replace any usage of the old-style MRD with a Function Finding.

- The installation instructions for PXRM*1.5*18 did not contain instructions to delete PXRMP18E and PXRMP18I, so we are deleting them in this patch.

- A bug which made it impossible to exit from the option PXRM EDIT WEB SITES was fixed.

- “Edit” was changed to “Add/Edit” in the menu text for the following options:

| **Option**                 | **Old Menu Text**              | **New Menu Test**                  |
|----------------------------|--------------------------------|------------------------------------|
| PXRM COMPUTED FINDING EDIT | Reminder Computed Finding Edit | Add/Edit Reminder Computed Finding |
| PXRM SPONSOR EDIT          | Edit Reminder Sponsor          | Add/Edit Reminder Sponsor          |
| PXRM TAXONOMY EDIT         | Edit Taxonomy Item             | Add/Edit Reminder Taxonomy         |
| PXRM TERM EDIT             | Reminder Term Edit             | Add/Edit Reminder Term             |
| PXRM LOCATION LIST EDIT    | Edit Location List             | Add/Edit Reminder Location List    |

- CLASS, SPONSOR, REVIEW DATE, and EDIT HISTORY are standard fields and are stored in standard locations across the Clinical Reminders files. When the Location List file #810.9 was created in V.2.0, only the CLASS field was created and it was not put in the standard location. To correct this, the data dictionary was changed to add the fields in the standard locations. The pre-init saves the original class values, and a post-init puts them in the correct location. The Location List editor and the print template for Location List Inquiry were changed to include all the fields.

The same changes as described above were made for CLASS and REVIEW DATE fields of the SPONSOR file, #811.6.

The pre-init for PXRM*2.0*4 stores any existing CLASS and SPONSOR CLASS values in ^XTMP(“PXRMLLCS”) and ^XTMP(“PXRMSPCS”) so they can be restored to the correct location by the post-init. These ^XTMP globals can be deleted after a successful installation.

- When submitting jobs to TaskMan, the following prompt was used:

Enter the date and time you want the job to start.

It must be on or after 03/09/2006@06:49:14

This was changed to:

Enter the date and time you want the job to start.

It must be on or after 03/09/2006@06:49:14

Start the task at:

- When a reminder mail group was defined, the line count for the error message was not being set. This was corrected. Remedy ticket #136439.

### Reminder Computed Findings

- “RACE” was added as a CSUB subscript to the VA-RACE 2003 computed finding; this will give a list of all the races found for a patient, up to the number for OCCURRENCE COUNT. This list can be used in the CONDITION; for example:

I (V("RACE","*")["WHITE")&amp;(V("RACE","**")["INDIAN")

- If a document class and a note title were exactly the same and the document class had an IEN lower than the title IEN, then the progress note computed finding (VA-PROGRESS NOTE) used the document class IEN to look for a note which did not exist. This was changed so that it makes sure the IEN is for a title.

- The following additional CSUB data was added to the VA-PROGRESS NOTE computed finding:
- V("DISPLAY NAME")=Display name of TIU title.

- V("EPISODE BEGIN DATE/TIME")=String\_":"\_EPISODE BEGIN DATE/TIME

where String is "Adm" for ward locations and "Visit" for all other location types. Date/time is in MM/DD/YY format.

- V("EPISODE END DATE/TIME")=String\_" "\_EPISODE END DATE/TIME where string is null if no date/time or "Dis: " if date/time exists. Date/time is in MM/DD/YY format

- V("HOSPITAL LOCATION")=External format of HOSPITAL LOCATION from TIU DOCUMENT file

- V("NUMBER OF IMAGES")=Number of images associated with TIU DOCUMENT Entry

- V("REQUESTING PACKAGE")=REQUESTING PACKAGE REFERENCE field from TIU DOCUMENT file (internal format)

- V("SUBJECT")=SUBJECT (OPTIONAL description) field from TIU DOCUMENT file (note that characters are limited to ensure that the returned string is not longer than 255 characters). (This piece was added with TIU*1*63)

- A number of national computed findings were setting the date of the finding to Today and this caused a problem when a reminder report was run with the Effective Date in the past. In this situation, the date of the computed finding should be the date entered for the Effective Date. The following computed findings were changed to correct this: VA-AGE, VA-DATE OF BIRTH, VA-DATE OF DEATH, VA-ETHNICITY, VA-RACE 2003, VA-RACE PRE 2003, VA-SEX, VA-VETERAN, VA-WH MAMMOGRAM IN WH PKG, VA-WH MAMMOGRAM ABNORMAL IN WH PKG, VA-PAP SMEAR ABNORMAL IN WH PKG, VA-WH PAP SMEAR IN LAB PKG, and VA-WH PAP SMEAR IN WH PKG.

- To make its function clearer, the computed finding VA-DISCHARGE DATE was renamed to VA-LAST SERVICE SEPARATION DATE.

- VA-DATE OF DEATH was changed so that the date of the finding is the date of death; previously the date of the finding was the evaluation date.

- The following new national computed findings are included in this patch:

- VA-APPOINTMENTS FOR A PATIENT (multiple) - Returns a list of appointments for a patient. The appointments can be filtered by a number of criteria which are documented in the Clinical Reminder Manager Manual.

- VA-PATIENTS WITH APPOINTMENTS (list) – Returns a list of patients with appointments; used for patient list-building. The appointments can be filtered using the same criteria as for VA-APPOINTMENTS FOR A PATIENT.

- VA-PATIENT TYPE (single) - Returns true if the TYPE field in the Patient file (file #2) has a value and returns the Type of Patient (e.g. Active Duty, Veterans) as the value, which can be used in a Condition.

- VA-PTF HOSPITAL DISCHARGE DATE (multiple) - Returns a list of discharge dates from the PTF file. By default, fee basis and census records are not included, but can be included through the computed finding parameter.

- VA-REMINDER DEFINITION (single) - Evaluates a reminder definition and returns the reminder status as the value, which can be used in a Condition. The Status, Due Date, and the Last Done Date are returned as CSUB items so they can be used in a Condition.

- VA-TREATING FACILITY LIST (multiple) – Returns a list of treating facilities, i.e., systems that store data related to a patient.

### Reminder Definitions

**Editing**

- Extensive changes were made to the STATUS LIST editing functionality; these are described in the updated Clinical Reminders Manager Manual.

- Editing of IGNORE ON N/A was moved from the Baseline section to the General Section.

- A change was made that allows term editing in Add/Edit Reminder Definition. In the past, this could only be done if the term was national.

- Checking for baseline age range overlap was moved from reminder evaluation to definition editing, to make reminder evaluation more efficient. This checking will still be done during reminder evaluation when the reminder test option is used. The post-init for PXRM*2*4 will check all reminder definitions for overlapping age ranges. Any definitions found to have overlapping age ranges will be listed during the install.

- Reminder edit was changed so that an age range can be entered for a frequency of 0Y.

- When a sponsor is added, a check is made to see if the sponsor class and the class of the file to which the sponsor is being added are the same. If they are different, a message to this effect is displayed. There was a bug in the output that caused the class to be displayed as null. This was corrected.

- A bug occurred when editing the CUSTOM DATE DUE string that would allow the string to be stored with lower-case characters, which could cause the date calculation to fail. This was corrected by making sure the string is always stored in upper-case, no matter what case the user has entered

**Finding Modifiers**

- A new finding modifier, INCLUDE VISIT DATA, was added. This modifier applies only to V file findings. The default value is “NO,” but when it is set to “YES,” the following CSUB data will be returned: COMMENTS, DATE VISIT CREATED, DFN, DSS ID, HLOC, HOSPITAL LOCATION, LOC. OF ENCOUNTER, OUTSIDE LOCATION, SERVICE CATEGORY, STATUS, STOP CODE, and VISIT.

- The finding modifier, USE COND IN FINDING SEARCH, was renamed to USE STATUS/COND IN SEARCH. When this field has a value of “YES,” the STATUS LIST and/or CONDITION will be applied to each result in the date range. Only results that have a status on the list or for which the CONDITION is true will be retained. The maximum number to retain is specified by the OCCURRENCE COUNT.

NOTE: If a finding has both a STATUS LIST and a CONDITION, the status check is made first; the CONDITION will be applied only if the finding passes the status check.

- A new finding modifier called USE START DATE was added; it applies only to findings that have a Start Date and a Stop Date. When USE START DATE is true, the Start Date will be used as the date of the finding. The default behavior for drug findings is to use the Stop Date as the date of the finding, while for orderable item findings, the default is to use the Start Date as the date of the finding. When USE START DATE is “YES,” date-matching is now done based solely on the Start Date being in the date range defined by Beginning Date/Time and Ending Date/Time. When USE START DATE is “NO,” date-matching is based on any overlap between the date range defined by Start Date and Stop Date and the date range defined by Beginning Date/Time and Ending Date/Time.

**Function Findings**

- The check of the subscripts used in Function Finding functions was enhanced. When the user types in a function string, the arguments for each function in the string are checked to make sure there are the correct number of arguments and the arguments are of the correct type.

- The following new functions were added:
- DIFF\_DATE - Returns the absolute value of the difference in days between two findings.

- VALUE  - Allows the comparison of  CSUB values between different occurrences of the same finding and between different findings. It has the form VALUE(FINDING,OCCURRENCE,”CSUB”), where FINDING is the finding number, OCCURRENCE is the occurrence, and “CSUB” is the particular CSUB subscript to check. Using the orderable item example from above, you could check that the first occurrence had a duration greater than 30 days with the function string VALUE(5,1,”DURATION”)&gt;30.

- A change was made so that any of the Clinical Reminder global variables (PXRMAGE, PXRMDOB, PXRMDOD, PXRMLAD, and PXRMSEX) can be used in a Function Finding.

**Miscellaneous**

- The input transform for Lab findings was allowing all types of Lab findings. This was changed so that it does not allow BB and WK data which are not indexed and cannot be used as reminder findings.

- The phrase “wildcard fist” was corrected to read “wildcard first.” This is seen when working with status lists.

- The status check was changed to make it more efficient.

- Duration was added to the “CSUB” data list for orderable item and drug findings.

- At any prompt for a reminder definition, such as in reminder due reports or reminder list rules, if users typed “?” they saw the prompt:

Answer with REMINDER DEFINITION NAME, or PRINT NAME, or USAGE, or FINDING ITEM”

This was corrected so that now the prompt is:

Answer with REMINDER DEFINITION NAME, or PRINT NAME

**Definitions Distributed in PXRM*2*4**

- The general resolution not found text in the VA-MST SCREENING reminder had a spelling error. The line:

All veterans should be screened at least once **is** their lifetime for

was changed to:

All veterans should be screened at least once in their lifetime for

- The two national reminders, VA-HTN ASSESSMENT BP &gt;=140/90 and VA-HTN ASSESSMENT BP &gt;=160/100, were originally distributed with findings 19 through 26 as drug classes that were informational findings. Because these are drug classes, they add considerable processing time to the reminder evaluation. To speed up the reminder evaluation, these findings were removed.

- Also for VA-HTN ASSESSMENT BP &gt;=160/100, the reminder description was updated and Beginning Date was changed from T-3M to T-2Y for finding items 27 and 28. Finding item 28 was removed from the resolution logic.


### Reminder Dialogs

- A misspelling in dialog help text was fixed:

element/group should be replace or suppress

was changed to:

element/group should be replaced or suppressed

- The following informational message:

Cannot modified lock group from a higher level view

was changed to:

Cannot modify lock group from a higher level view

- A problem with the user being able to delete dialog groups/elements from a National Reminder dialog was fixed.

- M errors occurred when adding a sequence number less than 0 or when adding an invalid sequence number such as “10-“. Code to handle these cases was added so the M errors no longer occur.

- An undefined error that occurred when deleting a Replacement Element/Group from a Dialog element/group was fixed.

- If a term used in branching logic had a Condition that used one of the PXRM special variables, such as PXRMSEX, it would fail because the special variables were not being defined. The code was changed to make sure they are defined.

### Reminder Evaluation

- In V.2.0, error trapping was added so that if a request to evaluate a non-existent reminder is made, a message is sent to the reminders mail group. The only information available to Clinical Reminders is the IEN of the non-existent reminder, so that is all that can be included in the message. In order to make it easier to track down what application is requesting the evaluation of a non-existent reminder; code was added to put an entry in the error trap. The error trap entry will contain the complete symbol table which should help in determining what application is calling for the evaluation of a non-existent reminder.

- For findings that have a Start Date and Stop Date, if the Stop Date is missing, then for evaluation purposes, the Stop Date is set to Today. The Duration function was using 0 instead of Today. This was corrected.

- A bug was found when building lists of orderable items that could have caused some orderable items without a Stop Date to be missed. This would occur if there was an orderable item that had a Stop Date immediately before or after the orderable item that did not have a Stop Date. This was corrected.

- The date range overlap calculation used for findings that have a start and stop date had an error: it would not correctly determine if the date ranges defined by beginning date-ending date and start date-stop date overlapped when BDT &gt; START DATE. This was corrected.

- The code for evaluation of drug class findings was rewritten to speed it up.

- For orderable items and non-VA meds that may not have a stop date, you could get a different result, depending on the value of the OCCURRENCE COUNT, because the search was not looking at all possible entries (as a result of the missing stop date). This was corrected.

- Drug class findings were only allowing for one occurrence of each drug in a drug class, even when the OCCURRENCE COUNT was greater than 1. This was corrected. Remedy ticket #134199

- The output for VA Generic drug findings was adding an extra blank line; the extra blank line was removed.

- The evaluation date was always getting set to Today when an Effective Date other than today was entered. This was corrected.

- Symbolic date handling was changed so that it properly handles time.

- Reminder Test was changed to take an Effective Date so the user can easily see the results of an evaluation on a past date.

- Redundant display of cohort logic in the test option output was corrected.

- The reminder test option allowed the selection of reminders whose usage is “Reminder Patient List.” Regular evaluation of patient list reminders generates errors, so a screen was added to prevent selection of patient list reminders.

- When there was a date of death for a patient, the reminder was still showing as applicable. This was corrected so that reminders are N/A for dead patients.

- When a CUSTOM DATE DUE was used, no age range information was being displayed in the Clinical Maintenance output. Display of age range information was added. Also, a check was added so that age range information is displayed only if the Patient Cohort Logic contains AGE. This applies both when a CUSTOM DATE DUE is used and when a regular date due calculation is done.

- A problem with the resolution date calculation was reported in Remedy ticket #106498. This would happen if a regular finding was “anded” with a function finding in the resolution logic and the regular finding was true while the function finding was false. This was corrected.

- There was a bug in the resolution date calculation that caused it to return 0 instead of a non-zero date when the operator was “&amp;” and one of the two dates was 0. It now returns the non-zero date.

- The general and summary resolution not found text was being displayed even if the reminder was N/A. This was corrected.

- The phrase “Frequency 0Y Not Indicated” was changed to “Frequency 0Y Not indicated.”

- Several changes were made in response to PSI-05-099:

If a frequency cannot be determined for a patient, the Status and Due Date will both be CNBD (CanNot Be Determined) and the frequency display that follows the status line will be:

Frequency: Cannot be determined for this patient.

- The date due calculation was restructured and streamlined.

- The output code for a lab test was expecting the specimen to exist, which may not be true for a micro test. The code was changed to check for the existence of a specimen before trying to print it.

- During testing, the following situation was encountered: a test site had a reminder definition with a finding that is a term; the term is mapped to a taxonomy and a health factor, and a status list is defined at the definition level. During reminder evaluation, the status list was being applied to all the term findings, which was generating an error for the health factor, since health factors do not have a status. This code was changed to properly handle this situation.

- Store errors in FPDAT^PXRMVCPT were reported in Remedy ticket #87364. The code was changed to prevent this. All the routines used in taxonomy evaluation were changed to make sure that a similar store error would not occur in them.

- When there were multiple occurrences in a taxonomy the output was not correct for the second and higher occurrence. In some cases, this would cause an undefined subscript error; this was corrected. Remedy ticket #109645.

- The API used to get Mental Health data does not understand “*” for the number of occurrences, so when USE STATUS/COND IN SEARCH was true, the lookup was failing. To get around this, a check was made for the limit being “*” and if it occurs, it is replaced by 99.

### Reminder Exchange

- During exchange install, a check was being made for a lab finding by doing a [“60”; this caused problems because file #50.605 also contains “60” so the test for a lab panel was inappropriately being applied to a VA Drug Class finding. This was corrected by changing the test to “=60”.

- Patch PSN*4*99 created several VA Drug Class entries with exactly the same name. When there were multiple entries with the same name, installation of a definition, term, or dialog via Reminder Exchange would fail, because FileMan could not resolve the pointer. Exchange has been changed so that now when there are multiple entries, the user is presented with the Name, the IEN, and any identifiers, and is asked to select the appropriate one to use. Whenever a packed reminder is selected for the  action, a warning will be issued for each component that does not have a unique .01.

- A display problem with Reminder dialogs that contain Branching Logic was fixed. The display of replacement elements was changed so that they will appear at the end of the list.

### Reminder Extracts

- The original version of extracts included test patients in the patient list and total count. This has been changed, so when the patient list is built, test patients will not be included unless the user specifies that they be included. This will make the extract counts slightly different; test patients were included in the N/A count, so this will change.

- The reminder evaluation loop used in extracts was restructured to make it run faster. Two test extracts run in approximately 2/3 of the time they previously required.

- The Hep C. EPI extract summary will now automatically be deleted from the local system after five years.

- The utilization count functionality was changed to count historical entries that were entered within the reporting period, even if the date of the visit is outside the reporting period. It was also changed to count all occurrences of every finding in a reminder term.

- The status for the Reminder Extracts was not showing up in the screen display for the Transmission History because the ACK messages coming from the  were not correctly formatted;  corrected the format. The original storage location for Transmission Status is purged on a regular basis so Transmission Status was moved to a permanent location.

- In conjunction with the date changes described in the Patient List section symbolic beginning dates were changed from T to BDT in the following finding rules that are used for the QUERI extracts:

VA-*IHD QUERI 412 DIAGNOSIS

VA-*IHD QUERI ANCHOR VISIT

VA-*IHD QUERI DIAGNOSIS

VA-*IHD QUERI LIPID LOWERING MEDS

VA-*IHD QUERI QUALIFYING VISIT

VA-*MH QUERI QUALIFY MH VISIT

VA-*MH QUERI QUALIFY PC VISIT

- To make reminder extracts easier to understand, these changes were made:
    1. Extensive new descriptions were added to the data dictionaries used for reminder extracts.
    2. Some of the options, protocols, and List Manager templates were renamed.
    3. A number of the fields were renamed.
    4. The help text was updated.
    5. The display of list rules was changed to make it easier to read.
    6. The following file names were changed:

|   **File #** | **Old Name**                  | **New Name**                   |
|--------------|-------------------------------|--------------------------------|
|        810.2 | REMINDER EXTRACT PARAMETER    | reminder extract definition    |
|        810.7 | REMINDER EXTRACT FINDING RULE | REMINDER EXTRACT COUNTING RULE |
|        810.8 | REMINDER FINDING GROUP.       | REMINDER COUNTING GROUP        |

- During the install, KIDS will point out that these files already exist with a different name:

810.2     REMINDER EXTRACT DEFINITION

*BUT YOU ALREADY HAVE 'REMINDER EXTRACT PARAMETER' AS FILE #810.2!

Shall I write over your REMINDER EXTRACT PARAMETER File? YES//

810.7     REMINDER EXTRACT COUNTING RULE

*BUT YOU ALREADY HAVE 'REMINDER EXTRACT FINDING RULE' AS FILE #810.7!

Shall I write over your REMINDER EXTRACT FINDING RULE File? YES//

810.8     REMINDER COUNTING GROUP

*BUT YOU ALREADY HAVE 'REMINDER FINDING GROUP' AS FILE #810.8!

Shall I write over your REMINDER FINDING GROUP File? YES//

Take the default of “YES” for each of the questions.

- Reminder Extract output was changed, so that the prompt “Transmit results to AAC” will not be displayed when running a local or a VISN level extract.

### Reminder Location Lists

- Location List Inquiry was not displaying the list of Credit Stops to Exclude. They were added.

- Location List Edit was changed so the user cannot “^” out when the class of the Location List and class of the sponsor do not match. Jumping back to the previous field is now allowed during location list editing.

- Location List findings were modified to check the status of the appointment associated with the visit, to make sure it is valid. Only those visits with valid statuses are kept on the list. Statuses that are considered invalid are: CANCELLED BY CLINIC, CANCELLED BY CLINIC &amp; AUTO RE-BOOK, CANCELLED BY PATIENT, CANCELLED BY PATIENT &amp; AUTO-REBOOK, DELETED, NO ACTION TAKEN, NO-SHOW, and NO-SHOW &amp; AUTO RE-BOOK. The same check is now used in reminder due reports, so lists made either way should be consistent.

- A new “special” Location List called VA-ALL LOCATIONS was created. When this Location List is used, the "AHL" index of the Visit file is searched to create a list of every hospital location for which one or more visits have been recorded. The list can be filtered, using a Condition, with things such as service category, stop code, and hospital location. Any of the “CSUB” data that is seen when INCLUDE VISIT FILE DATA is true may be used.

- The print template used for displaying the entire list of Location Lists was changed to make the output easier to read.

### Reminder Patient Lists

- Major changes were made to the user interface for patient lists. Now when the Patient List option is selected, the user will see all the Patient Lists that they have access to. Additionally, the type of list (public or private) and the user’s access (full or view) are displayed.

- In the past, a patient list was marked as private by storing the creator. This meant that no creator was stored for public lists. Several changes were made affecting this:

1. A new field, TYPE, was added to file #810.5. It is used to mark a list as public or private.
2. The creator is now always stored and displayed.

A user’s access to a particular list is now determined by first checking the TYPE field to see if it is public or private. If it is public, then the user has full access. If it is private and the user is the creator, the user has full access. If the user is not the creator, then the list of authorized users is checked, and if the user is on the list, he or she has view access.

- Changes were made so that all the date input used when building a patient list can be in symbolic form like T-1Y.

- Beginning Date/time and Ending Date/time were added to the rule set sequence multiple, so each sequence in a rule set can have its own date range. The precedence of dates is as follows: term or definition &gt; list rule &gt; rule set.

- Changes were made to the way that dates are handled in patient list-building. Dates will be overridden according to the following order of precedence:

List Build (LB) &lt; Rule Set (RS) &lt; Finding Rule (FR) &lt; Term/Definition (T/D)

This is in contrast to the previous method in which the changes were cumulative.

- Symbolic dates that can be used in RSs and FRs are BDT=LBBDT and T=LBEDT. In terms and definitions only T can be used.

- If RS, FR, or T/D dates are null, they will be replaced by LB dates. RS, FR, or T/D dates are considered to be null if both the beginning and ending dates are null.

- If BDT is defined and EDT is null, then EDT will be set to T@23:59.

- If EDT is defined and BDT is null, then BDT will be set to the beginning of data.

- Whenever T is used in a reminder rule, it will take the value of the final ending date/time that is determined according to the order of precedence list above. Only the ending date applies to reminder rules, so a change was made so that only the ending date is prompted for when editing list rules that are reminder rules and rule sets, where the sequence finding is a reminder rule.

- The rule set display was changed so that when the rule is a reminder rule, only the ending date is displayed.

- A new action, TEST, was added to the List Rule Management Screen. This action applies only to rule sets; it shows how the rule set will be processed and the beginning and ending dates used for each of the findings in the terms or definitions used in the rule set.

- There was a logical error in term evaluation during rule set processing; if any of the findings mapped to the term were true, the term was being set to true. This violates the way terms normally work, where the term takes on the value of the most recent finding whether it is true of false. This was corrected

- Accumulation and building of the list of patient lists was moved from local arrays to globals to prevent store errors in the future as the number of lists at sites grows.

- A new key, PXRM MANAGER, was created. Holders of this key will have full access to all patient lists, including editing, deletion, and adding users.

- A list edit function was added to the Patient List Patients screen. The list creator can edit NAME and TYPE. Holders of the PXRM MANAGER KEY can edit NAME, CREATOR, and TYPE.

- The list delete functionality was changed so the user must either be the creator or hold the PXRM MANAGER key in order to delete a list.

- Code was added to ask the user whether or not to include dead and test patients on a patient list. The default is to not include them.

- Extensive changes were made to how patient list-building handles deceased patients, to bring it into complete alignment with the handling of deceased patients in reminder due reports.

- Now if the “Include deceased patients on the list?” prompt is answered affirmatively, deceased patients will be included on the list.
- If the response is “NO”, the default, no deceased patients, will be included on the list.
- QUERI extracts require that deceased patients who were alive sometime during the reporting period are included on the extract patient list. To be able to continue to support this requirement, in view of the above change, several additional changes were required. Two new fields, INCLUDE DECEASED PATIENTS and INCLUDE TEST PATIENTS, were added to the Extract Sequence Multiple of the Reminder Extract Definition file. The post-init sets INCLUDE DECEASED PATIENTS to true and INCLUDE TEST PATIENTS to false for all the QUERI extracts.
- The national computed finding VA-DATE OF DEATH was changed so that the date of the finding is the date of date; previously the date of the finding was the evaluation date.
- A new national term VA-DATE OF DEATH that is mapped to this computed finding was created. This term is used in the new national finding rule VA-FR-DATE OF DEATH. This finding rule can be used to remove patients who died before the start of the reporting period. This finding rule was added to all the QUERI rule sets. The computed finding VA-DATE OF BIRTH was changed so the date of the finding is the date of birth. The updated rule sets will be distributed via Reminder Exchange as part of patch 4. The name of the Exchange entry is *QUERI LIST RULE UPDATES.

- In the past, when a patient list was overwritten or deleted, the patients on the list were removed one at a time. This was replaced with a more efficient operation that kills the entire list of patients at once.

- A mechanism to document how a list was created was added. A word-processing field, CREATION DOCUMENTATION, was added to file #810.5 as a place to store the information. Creation Documentation is viewable by selecting the DCD action on the main patient list screen. When a patient list is created by an extract, the Creation Documentation will be created automatically. Note that patient lists created prior to installing PXRM*2.0*4 will not have any information in this field.

- There was a bug in the display of reminder rules; it was not displaying the correct name for the reminder. This was corrected.

- The rule set error-checking that takes place before the rule set is evaluated was enhanced to look for more possible problems.

- The Copy Patient List action code was made more efficient.

- The Patient List menu was changed to display parentheses around the View User action, which signifies it is not selectable, if the patient list is a public list.

- Originally, when the Health Summary Individual action was selected, the user was prompted to select a list of patients, and then for each patient selected, was prompted to select the health summary to use. This was changed so that the user selects a list of patients and then selects a single health summary that will be used for all the selected patients.

- When a patient list was copied into an OE/RR Team, there was a bug that caused the wrong patients to be copied. This was fixed.  Remedy ticket #85633.

- A new field, AUTOMATICALLY PURGE, was added to Reminder Extract Summary file #810.3 and Reminder Patient List file #810.5. Each entry where this field is true will be automatically deleted whenever it is more than five years old. The init for PXRM*2.0*4 will set this field to true for all national Extract Summaries and Patient Lists. When users create a manual extract or a patient list, they will be prompted to enter a value for this field. All national extracts and patient lists created after installing PXRM*2.0*4 will have this field set to “YES”.

- The field PRIMARY STATION in the patient list multiple of file #810.5 was renamed to PCMM INSTITUTION to reflect what is really stored in the field.

- All references to Facility in the patient list display were changed to Institution. This better reflects what is actually stored; it is the Institution  which is determined by finding the patient’s PCMM Team and then the Institution for that Team. The display now will show the Institution name. It will continue to display the Institution IEN for lists built before PXRM*2*4.

- A print template was being used to display rule sets, which meant if a sequence was added out of order, it would display out of order. For example, a rule set with four steps has sequence 2 deleted and then added back. This display would look like this:

Sequence:  001

List Rule:  FR-DIABETIC DIAGNOSIS

Description: This is a taxonomy for diabetic diagnosis.

Rule Type: FINDING RULE

Reminder Term: DIABETIC DIAGNOSIS

Operation:  ADD PATIENT

Sequence:  003

List Rule:  FR-BMI

Description: Patient's BMI

Rule Type: FINDING RULE

Reminder Term: BMI

Operation:  INSERT FINDING

Sequence:  004

List Rule:  FR-FINGERSTICK

Description:

Rule Type: FINDING RULE

Reminder Term: FINGERSTICK, GLUCOSE

Operation:  INSERT FINDING

Sequence:  002

List Rule:  *IHD QUERI ASSOCIATE PRIMARY CARE STATION

Description: Associate primary facility.

Rule Type: FINDING RULE

Reminder Term: VA-IHD STATION CODE

Operation:  INSERT FINDING

- The print template was replaced with a routine, so the rule set will always be displayed in sequence order.

- If a reminder rule was selected for display/edit, there was a hard error; this was corrected. Here is an example of the error:

Display/Edit Rule    Sep 23, 2005@15:03:11          Page:    0 of

S BEG=$S($D(@VALMAR@(BEG,0)):BEG,1:0)

^

&lt;SUBSCRIPT&gt;PAGE+1^VALM4

- There was a hard error when listing a rule set if one of the sequences did not have a list rule. This was corrected.

- A change was made to the date check to allow future dates. In conjunction with the new appointment computed findings described above, patient lists can be built based on future appointments.

- There was a bug for list-building, based on Problem List entries. When a list was built with the ending date in the past, chronic problems were not being included. This was corrected.

- There were several bugs for building patient lists for non-CH lab findings. These were corrected.

- The help for list rules and patient lists was improved.

- Toggling between sorting patient lists by name and by type (public or private) was not working, this was corrected.

- Deleting a list rule from a sequence in a rule set generated a subscript error. This was corrected.

- The Demographic Report was rewritten and the types of patient data that can be included were expanded; this includes most of the data that can be obtained from the following VADPT calls: ADD, DEM, ELIG, and IN, the choices now include:

Select from the following address items:

1 - CURRENT ADDRESS

2 - PHONE NUMBER

Select from the following future appointment items:

1 - APPOINTMENT DATE

2 – CLINIC

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

11 – RACE

Include the patient's preferred facility? N//

Select from the following eligibility items:

1 - PRIMARY ELGIBILITY CODE

2 - PERIOD OF SERVICE

3 - % SERVICE CONNECTED

4 - VETERAN

5 - TYPE

6 - ELIGIBILITY STATUS

7 - CURRENT MEANS TEST

Select from the following inpatient items:

1 - WARD LOCATION

2 - ROOM-BED

3 - ADMISSION DATE/TIME

4 - ATTENDING PHYSICIAN

- If a finding rule is added to a rule set with the insert operation, then any of the CSUB data associated with the term’s finding will be available for inclusion on a demographic report. The name of the finding (FINDING NAME) will also be available.

- For patient lists created from a Reminder Due Report, the Patient Demographic Report can include reminder status, due date, and last done date for each reminder used in the report.

- Two problems with the display of patient names were identified:
    1. If there are two patients with exactly the same name, only one shows on the demographic report - the other is missing.
    2. If two patients have exactly the same name except for the middle initial (one with no MI and the other with one), then the order in which they display is different in the patient list and in the patient list with the demographics.
Both of these problems were corrected.
    - The delimited Patient Demographic Report was changed to allow the user to choose the delimiter.

### Reminder Reports

- In support of the Scheduling redesign, Reminder Reports were changed to use a new Scheduling API to gather appointment data. At some point in the future, this API will be changed, so that instead of getting appointment data from the local  system, it will go across the VA WAN to get appointment data from a national Scheduling database. When this happens, users will probably see a slow-down in the reminder report processing. Also, the Scheduling API may return an error code stating that it could not gather data from the national database. If this happens, the reminder report will be canceled, the print task will be removed from TaskMan, and an error message will either display on the screen or be sent via MailMan to the requestor of the report, giving the error returned from the Scheduling API.

- Because of the potential for delay when the Scheduling API starts going across the VA network to retrieve appointment data, several changes were made in how Reminder Reports were evaluated. One of the major changes was to no longer do the prior encounter look-up by date range and then by location. The new code will build a list of appropriate locations and then use an index in the Visit file that is by location and date range. This change may affect the total number of patients on the report. The reason is the original report code used the facility assigned to the visit directly, while the new report code is using the facility assigned to the clinic that is associated with the visit. Over time, if a clinic moves from one facility to another facility, the report will evaluate the current facility that the clinic belongs to. This will definitely affect reports run against a service category of “E.” This happens because when entering historical data in PCE, a clinic cannot be entered; instead the facility is picked by the user and is assigned to the visit. If that is the case, the historical visit will not be picked up for the report. This change should not have any effect on the actual evaluation process.

- The new Scheduling API is also used for detailed reports that display next appointments and for the previous encounter reports to check for no-shows.

- A problem with detailed retrospective reports returning the next appointment date based on the report end date and not the report run date was corrected. This could cause the next appointment date to be after the report end or before the report run date. For historical reports, the next appointment date is based on the date the report was run.

- Before patch 4, a deceased patient and/or test patient would be counted in the total number the report was run against. The evaluation status would always be N/A for these patients. With patch 4, there are two new prompts:

“Include deceased patients on the list?” and

“Include test patients on the list?”

Unless the user answers yes for these prompts, deceased and test patients will not be included in the total number of patients the report is run against.

- Normally when a patient is deceased, the status of the reminder is automatically set to “N/A.” A new flag for use in Reminder Reports was added that can be used to override this behavior and cause the status to be determined as usual. This change was made so that if the “Include deceased patients on the list?” prompt on a Reminder Due Report was answered as “yes,” normal evaluation can be done.

- The problem with Reminder Due Reports freezing for an individual patient who is deceased was fixed.

- The Effective Date/Time was added to queued delimited reports.

- The following text was changed:

WARNING - REMINDER COULD NOT BE DETERMINE; REPORT RESULTS MAY BE INCORRECT!

Reminder: REMINDER NAME had a total of 1 evaluation errors.

to

WARNING - REMINDER STATUS COULD NOT BE DETERMINED; RESULTS MAY BE INCORRECT!

Reminder:  REMINDER NAME had a total of 1 CNBD errors.

- To satisfy the concerns of the Database Administrator, the method of storing the list of service categories in a report template was changed from a set of codes to free text. The list of service categories that can be used was expanded to include all the service categories allowed in the Visit file. The post-init will automatically change the service categories in all existing Reminder Report Templates to the new format. ***Please check the templates you regularly use to make sure the list of service categories is correct. Note that in the past the list was just letters, now it is a comma-separated list of letters.***

- When multiple hospital locations are selected and some of them do not have patients, the list of locations that do not have patients is displayed in this format:

The following Location(s) had no patients selected

OLDDOM (SALT  CITY HCS)

RAD ROOM (SALT  CITY HCS)

ULTRASOUND CLINIC (SALT  CITY HCS)

This information was not being displayed when the report was queued. The problem has been corrected.

- Location Lists and Sponsors were added to the Review Date Report.

- The misspelling “Efffective” in the prompt “Enter EFFECTIVE DUE DATE:” was corrected.

- There was a subscript error at MULT+32^PXRMXT, trying to setup service category, when a report template was based on future appointments. This was corrected.

- The prompt “Select an existing REPORT TEMPLATE or return to continue:” needed a space after the colon, the space was added.

- The problem with no patients being found for Reminder Due Reports, based on future appointments at selected hospital locations, was fixed.

- When the list of patients was based on an OE/RR team, patients who were not on the list were being included. This was corrected.

- The total number of patients on a summary individual patient report with multiple reminders was being calculated incorrectly. This was corrected.

- When a reminder due report was run by selected locations (hospital locations or clinic stops), the output of the selected list of locations was skipping the first entry in the list. Additionally, for stop codes, only the stop code was being printed. The output was changed so that the first entry is no longer skipped and the name of the clinic stop as well as the stop code is printed.

- When a Reminders Due Report was run using Clinic Groups and a Clinic Group did not have any patients, the output looked like this:

The following Clinic Group(s) had no patients selected

1 A GROUP

The number preceding the name is not necessary, so it was removed and the output now looks like this:

The following Clinic Group(s) had no patients selected

A GROUP

- In Reminders Due Reports, the check for duplicate facilities from file #4 (Institution file) was being made based on the .01 name field, which is incorrect because there can be more than one entry with the exactly the same name. The duplicate check was changed to use the internal entry number.

- In Reminders Due Reports, when the number of applicable patients and the number of patients the report was run on was displayed, if there were no patients, the output was “0 patient.” This was corrected to “0 patients.”

- In the detailed report output, the line “patients have reminder due” was changed to “have the reminder due” since a detailed report has only one reminder.

- In a detailed report, when the Combined Facility prompt was answered “N” and the Combined Locations prompt was answered “Y”, the next appointment would not display if the appointment location was not the same as the encounter location. This was corrected.

- The Reminders Due Detailed Report lists a count of patients on the output. If the number of patients exceeded 999, then the number ran into the patient’s name

1834CRPATIENT,TEN          (0666)           DUE NOW     N/A         None

1835CRPATIENT,FIFTEEN      (6661)           DUE NOW     N/A         None

1836CRPATIENT,SIXTEEN      (6666)           DUE NOW     N/A         None

Room was made for the counter to go to 9999. When it gets to 10000, then it resets to 0 and starts over. The reset was used because of space issues.

Date Due     Last Done   Next Appt

--------     ---------   ---------

9997 CRPATIENT,TEN        (0666)          DUE NOW     N/A         None

9998 CRPATIENT,TWENTY     (6661)          DUE NOW     N/A         None

9999 CRPATIENT,FORTY      (6666)          DUE NOW     N/A         None

0 CRPATIENT,FIFTY      (6663)          DUE NOW     N/A         None

1 CRPATIENT,FIFTYFIVE  (6661)          DUE NOW     N/A         None

- “Disappearing” queued reminder reports continues to be a problem, so code was added to send a MailMan message if the report gets to the point where it is ready to start printing and the print task can’t be started. This message will be sent to the Clinical Reminders mail group with information about what happened. This information should help in determining what is going wrong. If any sites get these messages, please send a copy to the Clinical Reminders developers.

- A check to look for patient lists and OE/RR Teams that do not contain patients when running a report from a template was added. Reminder reports will no longer allow the user to select patient lists and OE/RR Teams that do not contains patients.

- Reminder reports will now scan the reminders in a reminder category for reminders that do not exist on the system; a warning will be given if there are no reminders in the category. This check will happen when running a report from a template.

- In a delimited summary report “NONE” was sometimes appearing at the end of the line:

1;ABCDEF,GHIJK (000001234);DUE NOW;N/A;;NONE

This signified that the patient is not an inpatient. This was changed, so now if the patient is an inpatient, the inpatient location is listed; otherwise it is blank.

- The intermediate data storage location for reminder due reports is made unique by using the date and time, to the second, when the report is started. When running a set of reminder due reports from report templates, a user was pasting answers to the input that is not stored in the report template so quickly that, in some cases, the time down to the second was identical for two of the reports in the set. This caused the two reports to use the same intermediate storage location, and the second report to destroy the intermediate data for the first report, causing errors that would prevent it from finishing. To prevent this problem, a one-second pause was added just before the time stamp is acquired, guaranteeing the uniqueness of the time stamps.

- A problem with incorrect patient counts for each location, when running a summary report against clinic locations, was corrected.

- As an aid in tracking down CNBD problems, a MailMan message with the subject “COULD NOT BE DETERMINED PATIENTS” will be generated and sent to the user who requested the report. The message will contain a list of patients who have a reminder evaluation status of CNBD. The file #800 parameter MAXIMUM NUMBER OF INDEX ERRORS will be used to determine the maximum number of patients to display on the list.

### Reminder Sponsor

**7**

- There was a bug that would let a site create a Sponsor whose class was national and also produced a hard error when a Sponsor was deleted. These were both corrected.

### Reminder Taxonomies

- Some incorrect CPT codes were removed from the taxonomy VA-WH BILATERAL MASTECTOMY; the corrected version is distributed as part of PXRM*2.0*4.

- When PATIENT DATA SOURCE was set to ALL, the search was not being done in all possible sources. This was corrected.

- An undefined error was occurring when trying to “^” jump during taxonomy editing. The undefined error was happening because jumping to an arbitrary field is not possible during taxonomy editing. The call to the FileMan routine used to do the editing was changed so that “^” is not allowed for jumping, but a single “^” will go back to the previous field.

- There was bug in taxonomy evaluation where it was trying to get Visit file information for Problem List entries. This was corrected.

### Reminder Terms

- When editing a term, if the term has a sponsor, a check is made to ensure that the class of the term and the class of the sponsor are the same; if not, then the user is prompted again for the class and sponsor until the classes match. There was a bug where even if the class of the term and the class of the sponsor were the same, it was saying they did not match. This bug was corrected.

- Term edit was changed so that the user cannot “^” out when the Class of the term and Class of the sponsor do not match.

- A change was made so that if a term contains only drugs or orderable items, the field USE START DATE can be edited. Note that USE START DATE is available in both definitions and terms for all drug findings and orderable items.

- A new national term, VA-PCMM INSTITUTION, was created to be used as a finding rule. It serves the same function as VA-IHD STATION CODE, but its name makes it easier to understand its function. Whenever a finding rule using either of these terms is included in a rule set with the Insert operation, the patient’s PCMM Institution will be included with the patient list. The PCMM Institution is determined by first finding the Institution (file #4) entry for the patient’s PCMM Team. If the Institution cannot be determined, the word NONE will be displayed.

- A site entered a Remedy ticket about a reminder not evaluating as expected. The finding in question was a term, so the debugger was used to see the details of how the term evaluated and it was found that everything was correct. Since the average Clinical Reminder Manager does not have programmer access, they cannot use the debugger to determine what is happening with a term. Therefore, an option was added to Reminder Test to show how all the findings for a term evaluated.

- The term finding modifier editing sequence was rearranged so it matches the sequence for definitions and term inquiry.

- In V.2.0, a change was made so that for terms used as findings in national reminders, the user could select a term and edit the findings on the term. This change introduced a bug that allowed the user to edit any of the findings in the reminder. The bug was corrected.

- The cross-reference on term findings for building the “enode” was never updated to the new form that was developed in V.2.0. (The enode is used for processing the term’s findings.) This resulted in the enode not being built correctly for non-CH lab findings; other finding types were not affected. This was corrected. A section was added to the post-init to make sure all the definition and term lab enodes are set correctly.

- The computed finding parameter in reminder terms was not allowing the “^” character. This was fixed.

- There was a bug in term output when multiple occurrences of the same type of mapped finding were found. For example, if three occurrences were found, it would write three sets of output:

Line 1

Line 1

Line 2

Line 1

Line 2

Line 3

This was corrected.


### Geriatric Extended Care (GEC)

- An undefined error, &lt;UNDEFINED&gt;CALCMON+12&lt;&gt;PXRMG2M1, occurred when the scheduled event fired off at the beginning of each month. That has now been repaired.

- Several of the GEC Reports were not showing a complete list of patients or providers. This has now been corrected. The division and age of the patient has been added to some reports to help in identifying the patient.

- There is a new choice in the GEC reports menu that will give the sites the option to open a closed referral, merge two referrals, or close an open referral.

- The GEC Care Recommendation Dialog has been modified to allow more than one selection when a person wants to refer a patient to more than one location.

- A problem with the user being able to take some editing actions on GEC dialogs have been corrected, so the user is not able to copy or delete dialog groups from the GEC dialogs.

- Geriatric Extended Care Reports were not collecting the correct data. This was corrected.

- The email addresses of the remote members of mail group GEC NATIONAL ROLLUP are updated.

- As requested by the primary GEC stakeholder, several reminder dialog entries were moved from the Nursing Assessment GEC dialog to the Care Recommendation GEC dialog. A post-install routine changes several Health Factors from one GEC dialog to another.

### MyHealtheVet

- MyHealtheVet requested a new combined output that returns both the summary and detailed output in a single call. A new routine, PXRMMHV, was created to support this.

- HealthGate was replaced with Healthwise in the web site URL information for the following reminders:

VA-MHV CERVICAL CANCER SCREEN

VA-MHV DIABETES FOOT EXAM

VA-MHV DIABETES RETINAL EXAM

VA-MHV HYPERTENSION

VA-MHV INFLUENZA VACCINE

VA-MHV MAMMOGRAM SCREENING

- The VA-MHV INFLUENZA reminder required two changes:
    - a frequency of 0Y for 49 and younger was added to the baseline and
    - a frequency of 1Y for all ages was added to the high-risk finding.

Two Remedy tickets associated with this: #118893 and #113219.


### CPRS V26 Reminder Changes

**Reminder Error Trapping**

With Clinical Reminders 2.0, CPRS will display an error message for any reminders that have an M error in the evaluation process.

**Reminder Logic Error Trapping**

With Clinical Reminders 2.0, CPRS will display an error for any reminders for which it can’t determine the status.

**Skin Test Changes**

The PXRM Reading Prompt was changed to accept a Null Value.

NOIS UNY-0304-12585

**Vital Date/Time**

Reminder Dialogs was changed to use the time a Vital was entered into a Dialog instead of the Appointment Time.  NOIS HUN-0304-21713

CPRSPROVIDER,TEN

**Mental Health Test Dialogs**

- Certain MH tests do not require a response to all questions, based on the patient’s response to some of the questions. For example, in an AUDC test if the patient responds that she/he never drank, the other two questions do not need to be answered. If the patient answers “Never” to question one, the reminder dialog will evaluate the test as complete.

### Remedy Tickets resolved with Patch 4

68948,  84724,  85633,  85695,  87364,  89146,  89401,  89472, 89627,  90449,  90823,  90992,  91471,  91682,  92187,  92570,  92761, 92790,  92795,  92802,  92807,  92992,  93292,  93633,  94630,  95523, 98203, 100670, 101723, 105304, 106443, 106498, 109645, 111210, 111345, 113060, 113346, 118893, 122050, 122458, 123240, 123779, 124911, 125171, 127184, 131755, 132065, 132998, 133356, 133774, 134199, 136399, 136439, 138761, 142078, 149570, 153731

### E3Rs Resolved

15246 NEW FINDING TYPE - SCHEDULED APPOINTMENT

15489 CHANGES TO REMINDER REPORT SELECTION CRITERIA (PXRM*1.5*6)

15491 REPORTS:SELECT PAST DATE AS EFFECTIVE DATE

15493 ADD MANAGEMENT OPTIONS FOR REMINDER REPORTS

15533 ADD NEW FIELD TO REMINDER DEFN--REMINDER 'NOTES'

15741 COLLAPSE/EXPAND RELATED DIALOG ELEMENTS AND GROUPS

15758 SUPPRESS CHECKBOX &amp; SEND TEXT TO NOTE (OR*3*173)

15998 DUE REPORT BY PROVIDER

16010 INCREASED DETAIL TO REPORTS

16011 NEED FOR TIME AS A FINDING ATTRIBUTE

16133 START STOP DATES

16149 UTILIZE REMINDER DIALOGS AS COMPONENTS

16675 UPDATE NATIONAL TAXONOMIES ANNUALLY

16832 TEXT INPUT TO JUMP TO SELECTION ITEM

16833 ADD CHOICE FOR 'ALL REQUIRED'--DIALOG GROUPS (OR*3*243)

16929 COMBINED TEAM LIST REPORTS

17158 ADDITIONAL REPORT

17278 ENHANCE USE OF MRD

17307 COLLATERALS SHOWING UP ON REPORTS

17408 PRINT OPTION FOR DIALOG HIERARCHY ()

17742 ALLERGY AS FINDING TYPE

18024 FUTURE PENDING ORDERS

18131 PATIENT LETTER-REMINIDER REPORTS

18224 ADD PATIENT DEMOGRAPHIC OPTIONS TO REPORTS

18248 PPD CHANGES FOR REMINDER DIALOGS

18627 ASSIGN CLINICAL REMINDERS BY STOP CODE

19360 RETAIN REMINDER INFO UPON PATIENT DEATH

19485 CHANGE GEC REFERRAL DIALOG

19488 OPEN CLOSED GEC REFERRAL

19508 LIST FOREIGN ORDERABLE ITEMS IN REMINDER INSTALL

19540 PATIENT LIST AND SS#

19843 ADD ELIGIBILITY TO PATIENT DEMOGRAPHICS REPORT

## Appendix A: Appointment Computed Findings

The following computed findings are being exported with Patch 4 (PXRM*2.0*4). They allow more detailed or specific appointment information to be used in cohort or resolution logic in reminder definitions. Use the COMPUTED FINDING PARAMETER in the findings editor to filter the results. See the descriptions and examples that follow for instructions on how to use these computed findings.

- VA-APPOINTMENTS FOR A PATIENT
- VA-PATIENTS WITH APPOINTMENTS
- VA-TREATING FACILITY LIST

**NAME: VA-APPOINTMENTS FOR A PATIENT**

ROUTINE: PXRMRDI

ENTRY POINT: PAPPL                    PRINT NAME: Appointments for a patient

TYPE: MULTIPLE

DESCRIPTION:   This multiple occurrence computed finding returns a list of appointments for a patient in the specified date range. The COMPUTED FINDING PARAMETER can be used to filter the results. The values that can be used in the parameter are:

FLDS:F1,F2,... where F1,F2 are any of the possible integer ID values listed in the Available Appointment Data Fields table in the Computed Findings section of the Clinical Reminders Managers Manual. These specify what data associated with the appointment is to be returned;  this data can be used in a CONDITION statement. Field number n will be the nth piece of the value. For example FLDS:1,16 would return the Appointment Date/Time in piece 1 and Date Appointment Made in piece 16. A condition such as I $P(V,U,16)&gt;3060301 would be true if  the date the appointment was made was after . If FLDS is not specified then the value will be ID=1 (Appointment Date/Time) and ID=2 (Clinic IEN and Name).

STATUS sets a filter on the appointment status; only those  appointments with status on the list will be returned. The possible values for STATUS are R (Scheduled/Kept), I (Inpatient), NS  (No-show), NSR (No-show, Rescheduled), CP (Cancelled by Patient),  CPR (Cancelled by Patient, Rescheduled), CC (Cancelled by Clinic),  CCR (Cancelled by Clinic, Rescheduled), NT (No Action Taken).

If STATUS is not specified, the default is R,I.

LL:Reminder Location List specifies a list of locations so that only  appointments for those locations will be returned. If LL is not specified, then appointments for all locations will be returned.

FLDS, STATUS, and LL are all optional and can be given in any order.  Some examples:

FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

STATUS:CP,CC^FLDS:25

LL:DIABETIC LOCATION parameter is FLDS:F1,F2,...^STATUS:S1,S2,...^LL:LOCATION LIST.

CLASS: NATIONAL

**NAME: VA-PATIENTS WITH APPOINTMENTS**

ROUTINE: PXRMRDI

ENTRY POINT: APPL                     PRINT NAME: Patients with appointments

TYPE: LIST                            CLASS: NATIONAL

**NAME: VA-TREATING FACILITY LIST**

ROUTINE: PXRMRDI

ENTRY POINT: TFL                      PRINT NAME: Treating facility list

TYPE: MULTIPLE

DESCRIPTION:   This multi-occurrence computed finding returns a list of treating facilities i.e., systems that store data related to a patient. The value for each entry is:

STATION NUMBER^NAME^DATE LAST TREATED^ADT/HL7 EVENT   REASON^FACILITY TYPE

STATION NUMBER, NAME, and FACILITY TYPE are from the Institution file.

FACILITY TYPE is one of the entries found in the FACILITY TYPE file. ADT/HL7

EVENT REASON is a code from the ADT/HL7 EVENT REASON file. If there is no

ADT/HL7 EVENT REASON then DATE LAST TREATED will also be null.

Some examples of values that are returned:

"516^BAY PINES VAMC^^^VAMC"

"537^JESSE BROWN VAMC^3041122.110926^3^VAMC"

"552^^3001113.092056^3^VAMC"

"556^ VAMC^3050406.13^3^VAMC"

"578^ VAMC^3020919.2324^3^VAMC"

"589^VA HEARTLAND - WEST, VISN 15^^^VAMC"

"636^VA NWIHS, OMAHA DIVISION^^^VAMC"

"673^TAMPA VAMC^3001215.1327^3^VAMC"

"695^MILWAUKEE VAMC^3030328.13^3^VAMC"

A CONDITION can be written that uses any of the pieces of the value.  For example, a CONDITION to check that the FACILITY TYPE is VAMC would be: I $P(V,U,5)="VAMC"

Since no date can be associated with an entry, the date of evaluation will be used.

CLASS: NATIONAL


**Available Appointment Data Fields**

|   **ID** | **FIELD NAME**                    | **DATA TYPE**   | **Format/Valid Values**                                                                                                                                                                                                                                                               | **Description**                                                                   | **Examples of Returned Data**                                                                                                                                                                                                        |
|----------|-----------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1 | APPOINTMENT DATE/TIME             | DATE/TIME       | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | The scheduled Appointment Date/Time                                               | 3031215.113  3031201.0815                                                                                                                                                                                                            |
|        2 | CLINIC IEN and NAME               | TEXT            | ID^name                                                                                                                                                                                                                                                                               | Clinic IEN and name                                                               | 150;CARDIOLOGY  32;BLOOD DONOR                                                                                                                                                                                                       |
|        3 | APPOINTMENT STATUS                | TEXT            | **R (**  Scheduled/Kept)  **I**  (Inpatient)  **NS**  (No-Show)  **NSR**  (No-Show, Rescheduled)  **CP**  (Cancelled by Patient)  **CPR**  (Cancelled by Patient, Rescheduled)  **CC**  (Cancelled by Clinic)  **CCR**  (Cancelled by Clinic, Rescheduled)  **NT**  (No Action Taken) | The status of the appointment.                                                    | R;SCHEDULED/KEPT  I;INPATIENT  NS;N0-SHOW  NSR;NO-SHOW &amp; RESCHEDULED  CP;CANCELLED BY PATIENT  CPR;CANCELLED BY PATIENT &amp; RESCHEDULED  CC;CANCELLED BY CLINIC  CCR;CANCELLED BY CLINIC &amp; RESCHEDULED  NT;NO ACTION TAKEN |
|        4 | PATIENT DFN and NAME              | TEXT            | DFN;name                                                                                                                                                                                                                                                                              | Patient DFN and Patient Name                                                      | 34877;REDACTED  455; REDACTED                                                                                                                                                                                                        |
|        5 | LENGTH OF APPOINTMENT             | TEXT            | NNN                                                                                                                                                                                                                                                                                   | The scheduled length of appointment, in minutes                                   | 20  60                                                                                                                                                                                                                               |
|        6 | COMMENTS                          | TEXT            | free text                                                                                                                                                                                                                                                                             | Any comments associated with the appointment                                      | PATIENT NEEDS WHEELCHAIR                                                                                                                                                                                                             |
|        7 | OVERBOOK                          | TEXT            | **Y**  or  **N**                                                                                                                                                                                                                                                                      | “Y” if appointment is an overbook else “N”                                        | Y  N                                                                                                                                                                                                                                 |
|        8 | ELIGIBILITY OF VISIT IEN and NAME | TEXT            | IEN;name                                                                                                                                                                                                                                                                              | Eligibility code and name associated with the appointment                         | 2;AID &amp; ATTENDANCE  7;ALLIED VETERAN  13;COLLATERAL OF VET.                                                                                                                                                                      |
|        9 | CHECK-IN DATE/TIME                | DATE/TIME       | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | Date/time the patient checked in for the appointment                              | 3031215.113                                                                                                                                                                                                                          |
|       10 | APPOINTMENT TYPE IEN and NAME     | TEXT            | IEN;name                                                                                                                                                                                                                                                                              | Type of Appointment IEN and name                                                  | 1;COMPENSATION &amp; PENSION  3;ORGAN DONORS  7;COLLATERAL OF VET.                                                                                                                                                                   |
|       11 | CHECK-OUT DATE/TIME               | DATE/TIME       | YYYMMDD.HHMM                                                                                                                                                                                                                                                                          | Date/time the patient checked out of the appointment                              | 3031215.113                                                                                                                                                                                                                          |
|       12 | OUTPATIENT ENCOUNTER IEN          | TEXT            | NNN                                                                                                                                                                                                                                                                                   | The outpatient encounter IEN associated with this appointment                     | 4578                                                                                                                                                                                                                                 |
|       13 | PRIMARY STOP CODE IEN and CODE    | TEXT            | IEN;code                                                                                                                                                                                                                                                                              | Primary Stop code IEN and code associated with the clinic.                        | 301;350                                                                                                                                                                                                                              |
|       14 | CREDIT STOP CODE IEN and CODE     | TEXT            | IEN;code                                                                                                                                                                                                                                                                              | Credit Stop code IEN and code associated with the clinic.                         | 549;500                                                                                                                                                                                                                              |
|       15 | WORKLOAD NON-COUNT                | TEXT            | **Y**  or  **N**                                                                                                                                                                                                                                                                      | “Y” if clinic is non-count else “N”                                               | Y  N                                                                                                                                                                                                                                 |
|       16 | DATE APPOINTMENT MADE             | DATE            | YYYMMDD                                                                                                                                                                                                                                                                               | Date the appointment was entered into the Scheduling system                       | 3031215                                                                                                                                                                                                                              |
|       17 | DESIRED DATE OF APPOINTMENT       | DATE            | YYYMMDD                                                                                                                                                                                                                                                                               | The date the clinician or patient desired for the scheduling of this appointment. | 3031215                                                                                                                                                                                                                              |

|   **ID** | **FIELD NAME**   | **DATA TYPE**   | **Format/Valid Values**                                                                                                | **Description**                                                               | **Examples of Returned Data**                                      |    |
|----------|------------------|-----------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------|----|
|       18 | PURPOSE OF VISIT | TEXT            | Code (1, 2, 3, or 4) and short description (C&P, 10-10, SV, or UV)                                                     | The Purpose of Visit                                                          | 1;C&amp;P  2;10-10  3;SV  4;UV                                     |    |
|       19 | EKG DATE/TIME    | DATE/TIME       | YYYMMDD.HHMM                                                                                                           | The scheduled date/time of the EKG tests in conjunction with this appointment | 3031215.083                                                        |    |
|       20 | X-RAY DATE/TIME  | DATE/TIME       | YYYMMDD.HHMM                                                                                                           | The scheduled date/time of the X-RAY in conjunction with this appointment     | 3031215.083                                                        |    |
|       21 | LAB DATE/TIME    | DATE/TIME       | YYYMMDD.HHMM                                                                                                           | The scheduled date/time of the Lab tests in conjunction with this appointment | 3031215.083                                                        |    |
|       22 | STATUS           | TEXT            | Status Code, Status Description, Print Status, Checked In Date/Time, Checked Out Date/Time, and Admission Movement IFN | Status Information for the Visit.                                             | 8;INPATIENT APPOINTMENT;INPATIENT/CHECKED OUT;;3030218.1548;145844 |    |
|      23  | X-RAY FILMS      | TEXT            | **Y**  or  **N**                                                                                                       | “  **Y**  ” if x-ray films are required at clinic else “  **N**  ”            | Y  N                                                               |    |

### Example:

If you want to limit the patient cohort for a reminder to APPOINTMENT DATE/TIME, CLINIC IEN and NAME, and DATE APPOINTMENT MADE,  patients who kept their appointments, and were seen in a Diabetic clinic, you could specify this in the COMPUTED FINDING PARAMETER, as shown here.

Select Reminder Definition Management Option: **Add/Edit Reminder Definition**

Select Reminder Definition: diaB PTS (5Y) W/O DIAB EXAM (1Y)       LOCAL

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

EX   DIABETIC EXAM                                               Finding #: 2

TX   VA-DIABETES                                                 Finding #: 1

Select FINDING: VA-APPOINTMENTS FOR A PATIENT

Searching for a DRUG, (pointed-to by FINDING ITEM)

Searching for a EDUCATION TOPIC, (pointed-to by FINDING ITEM)

Searching for a EXAM, (pointed-to by FINDING ITEM)

Searching for a REMINDER LOCATION LIST, (pointed-to by FINDING ITEM)

Searching for a HEALTH FACTOR, (pointed-to by FINDING ITEM)

Searching for a IMMUNIZATION, (pointed-to by FINDING ITEM)

Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM)

Searching for a MENTAL HEALTH INSTRUMENT, (pointed-to by FINDING ITEM)

Searching for a ORDERABLE ITEM, (pointed-to by FINDING ITEM)

Searching for a RADIOLOGY PROCEDURE, (pointed-to by FINDING ITEM)

Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

Searching for a REMINDER TAXONOMY, (pointed-to by FINDING ITEM)

Searching for a REMINDER TERM, (pointed-to by FINDING ITEM)

Searching for a SKIN TEST, (pointed-to by FINDING ITEM)

Searching for a VA DRUG CLASS, (pointed-to by FINDING ITEM)

Searching for a VA GENERIC, (pointed-to by FINDING ITEM)

Searching for a VITAL MEASUREMENT, (pointed-to by FINDING ITEM)

Searching for a DRUG

Searching for a EDUCATION TOPIC

Searching for a EXAM

Searching for a REMINDER LOCATION LIST

Searching for a HEALTH FACTOR

Searching for a IMMUNIZATION

Searching for a LABORATORY TEST

Searching for a MENTAL HEALTH INSTRUMENT

Searching for a ORDERABLE ITEM

Searching for a RADIOLOGY PROCEDURE

Searching for a REMINDER COMPUTED FINDING

VA-APPOINTMENTS FOR A PATIENT     NATIONAL

...OK? Yes//   (Yes)

Are you adding 'VA-APPOINTMENTS FOR A PATIENT' as

a new FINDINGS (the 3RD for this REMINDER DEFINITION)? No// Y  (Yes)

Computed Finding Description:

This multiple occurrence computed finding returns a list of

appointments for a patient in the specified date range. The COMPUTED

FINDING PARAMETER can be used to filter the results. The values that

can be used in the parameter are:

FLDS:F1,F2,... where F1,F2 are any of the possible integer ID values

listed in the Available Appointment Data Fields table in the

Computed Finding section of the Clinical Reminders Managers Manual.

These specify what data associated with the appointment is to be

returned; this data can be used in a CONDITION statement. Field

number n will be the nth piece of the value. For example FLDS:1,16

would return the Appointment Date/Time in piece 1 and Date

Appointment Made in piece 16. A condition such as I

$P(V,U,16)&gt;3060301 would be true if the date the appointment was

made was after . If FLDS is not specified then the

value will be ID=1 (Appointment Date/Time) and ID=2 (Clinic IEN and

Name).

STATUS sets a filter on the appointment status; only those

appointments with status on the list will be returned. The possible

values for STATUS are R (Scheduled/Kept), I (Inpatient), NS

(No-show), NSR (No-show, Rescheduled), CP (Cancelled by Patient),

CPR (Cancelled by Patient, Rescheduled), CC (Cancelled by Clinic),

CCR (Cancelled by Clinic, Rescheduled), NT (No Action Taken).

If STATUS is not specified the default is R,I.

LL:Reminder Location List specifies a list of locations so that only

appointments for those locations will be returned. If LL is not

specified, then appointments for all locations will be returned.

FLDS, STATUS, and LL are all optional and can be given in any order.

Some examples:

FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

STATUS:CP,CC^FLDS:25

LL:DIABETIC LOCATION

Editing Finding Number: 3

FINDING ITEM: VA-APPOINTMENTS FOR A PATIENT//

REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

CONDITION: I $P(V,U,16)&gt;3060301

CONDITION CASE SENSITIVE: N  NO

USE COND IN FINDING SEARCH: Y  YES

COMPUTED FINDING PARAMETER: FLDS:1,2,16^STATUS:R^LL:DIABETIC LOCATIONS

FOUND TEXT:

No existing text

Edit? NO//

NOT FOUND TEXT:

No existing text

Edit? NO//

Reminder Definition Findings

Choose from:

CF   VA-APPOINTMENTS FOR A PATIENT                               Finding #: 3

EX   DIABETIC EXAM                                               Finding #: 2

TX   VA-DIABETES                                                 Finding #: 1

## Appendix B:  HL7 Logical Link Set-up

**Turn on the Logical Link in the HL7 package**

Before an HL7 message can be transmitted to , each site must turn on the Logical Link in the HL7 package in their production account. Enter PXRM7 at the HL LOGICAL LINK prompt, and accept the default of “Background” as the method for running the receiver.

Select OPTION NAME: **HL MAIN MENU** HL7 Main Menu     menu

Select HL7 Main Menu Option: **Filer** and Link Management Options

Select Filer and Link Management Options Option: **SL** Start/Stop Links

This option is used to launch the lower level protocol for the appropriate device. Select the node with which you want to communicate

Select HL LOGICAL LINK NODE: PXRM7-RECO

The LLP was last shutdown on DEC 03, 2003 .

Select one of the following:

F         FOREGROUND

B         BACKGROUND

Q         QUIT

Method for running the receiver: B// **&lt;Enter&gt;** ACKGROUND

Job was queued as 5282278.

**Restart HL7 Logical Link**

1. HL Main Menu
2. Filer and Link Management Options …
3. SL Start/Stop Links
4. Enter “PXRM7-RECO”
5. Select “B” Background
6. Monitor with System Link Monitor

**Task Monthly Extracts**

- The automatic monthly extract of QUERI information is initiated from the options PXRM EXTRACT VA-IHD QUERI and PXRM VA-MH QUERI. These are activated through TaskMan options.
- Use Schedule/Unschedule Options on the Taskman Management menu to schedule the PXRM VA-IHD QUERI and PXRM VA-MH QUERI options.

Task Automated Monthly Extracts

Select OPTION NAME: **XUTM MGR** Taskman Management     menu

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: PXRM EXTRACT VA-IHD QUERI       VA-IHD QUERI Extract     run routine

Are you adding 'PXRM EXTRACT VA-IHD QUERI' as

a new OPTION SCHEDULING (the 50TH)? No// Y  (Yes)

Edit Option Schedule

Option Name: PXRM EXTRACT VA-IHD QUERI

Menu Text: VA-IHD QUERI Extract                      TASK ID:

**Catch up on Prior Extracts**

1. Run a manual extract or manual transmission for each month from Feb 2005 to the present to catch up
2. Manual Catch-up of Missed Roll-Ups
3. Use the Reminder Extract Management option to see what extract months have not run between February 2005 and November 2005 (the next automated run)
4. Use the Manual Extract action to task each month not reported since 02/2005
5. Use the Manual Transmission action to transmit extracts that have a “Not Transmitted” status

**What automated extract period will run next?**

**Catch-up Method A**

This means that you run one extract after the other and that you need to wait for one to complete to run the next one – to keep updating the next extract period

1. Run the prior extracts using the manual extract option
2. Answer ‘NO’ to the prompt “Does this extract replace the scheduled extract?”
3. Transmit the extracts manually
4. Update the Next Monthly Period/Year in Fileman to be correct – e.g. update to M11/2005.

**Catch-up Method B**

- Using this method, you could run all your extracts at one time by queuing them
    - Then update the next scheduled extract to the appropriate one; e.g., M11/2005