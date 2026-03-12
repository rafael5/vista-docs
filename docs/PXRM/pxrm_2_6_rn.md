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
source_file: pxrm_2_6_rn.docx
status: draft
title: pxrm 2 6 rn.docx
---

**Clinical Reminders**

PXRM*2.0*6

**Release Notes**

**December 2007**


##### Table of Contents

Release Notes	1

Clinical Reminders PXRM*2*6 Documentation	1

Modified National Reminders	1

General Functionality Changes in PXRM*2*6 and GMTS*2.7*77	2

Health Summary	2

Reminder Definitions/Terms	3

Reminder Dialog Changes (VistA)	5

Reminder Dialog Changes (CPRS)	7

Reminder Exchange	9

Reminder Extracts and Patient Lists	10

Reminder Reports	12

Reminder Taxonomies	13

Miscellaneous	13

GEC	13

Summary of Mental Health Instruments in Reminder Dialogs	14


## Release Notes

This manual describes enhancements and fixes included in the combined build of Clinical Reminders patch PXRM*2*6 - MH Integration and GMTS*2.7*77 - Mental Health Components.

### Clinical Reminders PXRM*2*6 Documentation

| **Documentation**       | **Documentation File name**   |
|-------------------------|-------------------------------|
| Release Notes           | PXRM_2_6_RN.PDF               |
| Install and Setup Guide | PXRM_2_6_IG.PDF               |
| User Manual             | PXRM_2_6_UM.PDF               |
| Manager Manual          | PXRM_2_6_MM.PDF               |

Patch PXRM*2*6 contains modifications to integrate the Clinical Reminders package with the new version of the Mental Package called MHA3.  The Clinical Reminders package will support use of new mental health surveys, instruments, and forms for clinical collection, reminder evaluation, patient list building and reporting. These modifications will be distributed at the same time as YS*5.01*85.

This functionality is needed so that Clinical Reminders can be used to help sites meet the Performance Measure requirements related to a standardized set of Mental Health Instruments that will be available in the YS*5.01*85 patch.  The standardized instruments are AUDC, BDI2, PHQ-2, PHQ9, and PC-PTSD.

### Modified National Reminders

### 1 VA-Depression Screening

### 2 PHQ-2 &amp; PHQ-9 in the dialog

### 3 VA-Iraq &amp; Afghan Post Deploy Screen

### 4 Use all MH tests (AUDC, PHQ-2, PC PTSD)

### 5 Added more detailed branching logic

### 6 VA-TBI Screening

### 7 Fixed selection problem; added done elsewhere

### 8 VA-MHV Influenza Vaccine

### 9 Updated date for FY08

###### New National Reminders

### 10 VA-PTSD SCREENING

### 11 Uses PC PTSD

### 12 VA-ALCOHOL ABUSE SCREEN (AUDIT-C)

### 13 Uses AUDIT-C for all alcohol screens

### 14 VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL

### 15 Provides a standard tool for education and counseling

### 16 Multiple branching logic reminders


**NOTE: In order to use all of the dialog functionality available with MHA3 and PXRM*2*6, Version 27 of the CPRS GUI will need to be installed. This version isn’t scheduled for release until later in the year.**


Version 27 adds the ability to use a Mental Health DLL when a MH test is invoked from a reminder dialog. (YS\_MHA.DLL is included with YS*5.01*85 and must be installed in the folder \Program Files\vista\ Common Files on all workstations.)

- Additional dialog features available via CPRS 27 and MH DLL:
    - Result group messages
    - Require all items in a group
    - Improved MH test required functionality
- Improves progress note text over CPRS V26 for MH tests

See the section on Dialogs, later in the Release Notes, for more information about use of the Reminder Dialogs and Mental Health tests with CPRS 26 or CPRS 27 and the MH DLL.

### General Functionality Changes in PXRM*2*6 and GMTS*2.7*77

The following changes have been made in Clinical Reminders and Health Summary.

### Health Summary

GMTS*2.7*77, bundled with PXRM*2.0*6, provides two new Health Summary Components to view administered mental health tests and scores:

- MHAL - MHA Administration List
- MHAS - MHA Score

**Example: Health Summary with MHAL and MHAS components**

10/29/2007 10:03

************************  CONFIDENTIAL AD HOC SUMMARY  *************************

CRPATIENT,FIVE    000-00-0005                            DOB: 04/18/1985

1A(1&amp;2)

---------------------------- MHAL - MHA Admin List ----------------------------

Date                Instrument           Ordered by          Location

05/14/07 15:08      AUDC                 CRPROVIDER,THREE     1A(1&amp;2)

05/14/07 15:08      PHQ9                 CRPROVIDER,THREE     1A(1&amp;2)

05/14/07 15:08      PHQ-2                CRPROVIDER,THREE     1A(1&amp;2)

-------------------- MHAS - MHA Score (max 10 occurrences) --------------------

Date                           Instrument   Raw    Trans Scale

05/14/2007 15:08                     PHQ-2    5          Total

05/14/2007 15:08                     PHQ9    10          Total

05/14/2007 15:08                     AUDC     2          Total

- END *


### Reminder Definitions/Terms

- To aid sites in making the conversion of Clinical Reminders to use MHA3, the post-init will convert all existing mental health findings to their MHA3 equivalent and MH SCALE values to the appropriate MHA3 scale. If the field MH SCALE is null, then the score for the first scale returned by MHA3 will be displayed in the Clinical Maintenance output.

When MH SCALE has a value, it will set the value of V for use in a Condition. In other words, V will be the score according to the scale stored in MH SCALE. Another change is that score is now returned as raw score^transformed score. Thus, if your Condition uses the raw score, you will use +V or $P(V,U,1) and if it uses the transformed score, use $P(V,U,2). The post-init will convert V to +V in all existing national Conditions for MH findings.

The entire set of scores has been made into a CSUB item in patch PXRM*2*6, so that any score or combination of scores can be used in a Condition. For example, the MH Test AUIR has scales 279 through 329; if you want to use the raw score for scale 300, then you can use +V(“S”,300).

NOTE:  Typing a “?” at the MH SCALE prompt will give you a list of all the scales available for the MH Test you have selected. It shows you both the scale number and the scale name. Because the scale number is much easier to use, it is the way we refer to scales in reminder definitions and terms.

Responses to individual questions can also be used in a Condition. For example, if you want to test the response to question number 7, you would use V(“R”,7).

NOTE **:** No national reminder definitions use MH findings, but those national terms that use MH findings will have correct values set for MH SCALE, and where applicable, the Condition will be updated also. These terms will be redistributed in patch PXRM*2*6.

- A new function finding function, NUMERIC, was added.

DESCRIPTION: The NUMERIC function returns the first numeric portion of any of the "CSUB" values for a finding. For example, if the COMMENT field of a health factor contains a numerical value, this function can be used to test it. If you want to check to see if the first numeric portion in the COMMENT field of finding 1 occurrence 1 is greater than 2, then the function finding would be:

NUMERIC(1,1,"COMMENTS")&gt;2

Note: OCCURRENCE COUNT for the finding must be equal to or greater than the occurrence(s) you want to use.

- The primary provider DUZ was added to the data returned for a Visit file entry. If there is no primary provider, the value will be null. TYPE, HOSPITAL LOCATION, STOP CODE, and ENTERED BY were also added to the data returned for a Vitals entry.

- Clinical Reminders normally treats partial dates as follows: if the day is missing, it is assumed to be the first; if the month is missing, it is assumed to be January. When a Custom Date Due was used, this convention was not being followed. The code was changed to follow this convention.

- A typo in error message text for Vitals findings was corrected. The name of the global was GMRV(120.5; it was corrected to GMR(120.5.

- Processing of Location List findings was originally based on the AET Visit file index which includes Encounter Type. Encounter Type is not a required field; consequently any Visit file entries that do not have an Encounter Type will not be in this index and would be missed. The code was changed to use the AA index so no entries will be missed. As an added bonus, it turned out that using AA is faster than AET.

- When BEGINNING DATE/TIME and ENDING DATE/TIME were input as FileMan dates including time, the time was not being displayed in reminder inquiry. This was corrected.

- The MHV output for non-VA meds was producing an error when there was no stop date. This was corrected.

- There was a bug when editing terms in national reminder definitions. A list of terms to edit is presented and the user selects which term to edit. If the user selected terms 3, 5, and 7, they would actually get terms 1, 2, and 3 to edit. This was corrected.

- If a term contained multiple drug findings, the name of the most recent drug was being displayed for all the findings, even though the rest of the information such as start date and days supply was correct. The code was changed so that the correct drug name is displayed for each finding.

- For drug class or VA Generic findings that contain many drugs, it is possible that different drugs on the list may have the same pharmacy orderable item. When this was the case and non-VA meds were included in the search, multiple instances of the same non-VA med were being put on the list. To prevent this, a check was added to make sure the same instance was not already on the list before adding it.

- An undefined error associated with the status list when adding a reminder taxonomy as a finding item to either a reminder definition or a reminder term was fixed. To test this, the user would need to create a taxonomy that contains both Radiology CPT Codes and ICD9 Codes and the Patient Data Source is set to “All”. Remedy #168830 and #177389.

- Building the drug status list was changed to use a new pharmacy encapsulation API instead of FileMan calls.

- Plus and minus were inadvertently left out of the list of permissible operators in Function Findings; they were added to the list.

- The selection display in reminder definition edit was changed to show if a definition has been inactivated.

- A site had a problem with a reminder because their default resolution logic (built from USE IN RESOLUTION LOGIC fields on the findings) allowed the reminder to be resolved solely by a function finding. Checking during reminder definition edit was added that will notify the user when this situation occurs.

- The definition and term inquiries displayed the old name of the field USE STATUS/COND IN SEARCH. These were corrected to use the new name.

### Reminder Location Lists

- A new option, Copy Location List, was added to the Reminder Location List Management menu.

### Reminder Dialog Changes ()

- **Data Dictionary Changes**

The variable pointer for the Finding Item field was changed to point to the new MH file 601.71 instead of File #601.

PXRM*2*6 adds three new fields to the DD for 801.41. These fields will be used by Result Group/Elements and Dialog Elements.

^PXRMD(801.41,D0,50)= (#119) MH TEST [1P:601.71] ^ (#120) MH SCALE [2N] ^

^PXRMD(801.41,D0,51,0)=^801.41121P^^  (#121) RESULT GROUP SEQUENCE

^PXRMD(801.41,D0,51,D1,0)= (#.01) RESULT GROUP SEQUENCE [1P:801.41] ^

- MH Test is defined when creating/editing a Result Group. As of PXRM*2*6, all Result Groups must be mapped to a MH Test.

MH Scale is defined when creating/editing a Result Group. The list of possible scales is based on the MH Test defined in field #119. As of PXRM*2*6, all Result Groups need to be mapped to a MH Scale.

Result Group Sequence is replacing the Result Group/Element field used when creating/editing a Dialog Element for a MH Test. With the new MH DLL in CPRS 27, it is now possible to evaluate multiple scores for each MH Test that contains multiple scales. In the past, we could only evaluate one score per test. With PXRM*2*6, only a Result Group can be assigned to a Dialog Element.

Field (#55) RESULT GROUP/ELEMENT [15P:801.41] will be deleted from the 801.41 DD.

Maximum Number of MH Questions has been added as a new field to file 800.

^PXRM(800,D0,MH)= (#17) MAXIMUM NUMBER OF MH QUESTIONS [1N] ^

- **Pre and Post-Install**

All the National Result Groups and Result Elements will be re-released with PXRM*2*6. These have been updated to use the correct MH Test and the MH Scale.

Seven new result groups will be released with PXRM*2*6.

PXRM BRADEN RESULT GROUP

PXRM MORSE FALL RESULT GROUP

PXRM PCLC RESULT GROUP

PXRM PCLM RESULT GROUP

PXRM PHQ2 RESULT GROUP

PXRM PHQ9 RESULT GROUP

PXRM PTSD RESULT GROUP

The PXRM AIMS RESULT ELEMENT 1 Progress note text has been modified to only display the total score of the AIMS test.

The PXRM BDI RESULT GROUP has been marked disabled. Sites should use the PXRM BDI II RESULT GROUP instead of this result group.

NOTE: The MH instrument BDI is being discontinued. The Beck Depression Inventory is an instrument in the Mental Health Assistant that has long been used for evaluating and monitoring depression.  For several years, MHA carried both the original version (BDI) and a newer, enhanced version (BDI2).  With the release of patch YS*5.01*85, the BDI will be inactivated, as the BDI2 is now the preferred version of this instrument. During the pre-init, any dialog elements using BDI will be changed to use BDI2.

National Result Groups assigned to a dialog element will be moved to the new multiple "RESULT GROUP SEQUENCE" if the test assigned to the Result Group matches the MH Finding Item in the element. These items will be stored as the first position. Local Result Groups will not be moved because of the lack of MH Tests defined for the Result Groups. Any Result Group that is not moved should be displayed in a MailMan message stating the name of the Result Group and the Element.

- **Result Element Editor**

A new field was added to the Result Group Editor “Informational Text”; this field allows the sites to add text to a pop-up warning in CPRS. (CPRS 27 and the MH DLL are needed to support this functionality). When CPRS is evaluating the Result Element progress note text, if the Result Element is true, the Informational Text defined in the Result Element will be returned to CPRS 27.

- **Result Group Editor**

In the Result Group Editor, sites will be able to disable a Result Group. Sites will also be able to assign the MH Test and the MH Scale to the Result Group. Both an MH Test and a MH Scale are required before the Result Group can be used in CPRS. A disabled Result Group will not be used in CPRS.

Several enhancements were made to result group editing. Result groups are screened to make sure they match the MH test. If the MH test is changed, any existing result groups are checked and if they do not match the MH finding, they are deleted.

- **Dialog Element Editor**

When defining an MH finding item in a dialog element, the user will be able to assign multiple result groups to a dialog element. This is done to support the enhanced functionality of the MH DLL in CPRS 27. The list of Result Groups should be limited to Result Groups that have the same MH test as the MH finding Item, an MH Scale defined, and the Result Group is not disabled. When an MH test is defined in a dialog element, a check will be done to see if the test requires a license. If the test requires a license, a message will be displayed to the user stating “The question text will not appear in the progress note.”

**New Dialog Option**

- A new option, Edit Number of MH Questions, has been added to the Reminder Parameters menu. This option allows the site to set the maximum number of questions an MH test can have and be administered via a Reminder Dialog. The default value when PXRM*2*6 is installed is 35. The user will not be able to select a MH test with a number of questions that exceeds the value defined in this option.


### Reminder Dialog Changes (CPRS)

YS\_MHA.DLL is a new tool included with YS*5.01*85 that provides an interface to Clinical Reminders functions in CPRS27. As described in the YS*5.01*85 Installation Guide, this DLL must be deployed to \Program Files\vista\ Common Files.

This DLL will replace the current MH functionality in reminder dialogs. The DLL will allow Reminder Dialogs to process *all* MH tests with no more than 100 questions. The maximum number of questions can be set by sites using the option “Edit Number of MH Questions” described in the preceding section. The question and answer text for the progress note, along with the score and scale for each MH test, will be returned by the MH DLL.

CPRS 26 has additional checks to avoid forcing the user to answer all the questions in the MH test if the test is considered resolved without answering all of the questions. This requires installation of PXRM*2*6 and YS*5.01*85 to work.

- **Result Group Evaluation**

How this works will depend on what combination of software you have installed:

- *CPRS 26 and PXRM*2*6* . PXRM*2*6 can contain multiple Result Groups; however, CPRS 26 is only expecting one Result Group per element. If the dialog element contains more than one dialog result group in the Result Group Sequence Multiple, only the first Result Group in the multiple will be sent to CPRS 26. The informational message can be defined in the Result Element; however, the Informational message will not display in CPRS 26. The Reminder Manager will be able to set up a dialog with MH Tests that do not work in CPRS 26. An error message "Error encountered loading MH Test Name" will be displayed in CPRS. The MH Test BOMC is an example of a test that can be defined in PXRM*2*6, but will not function correctly until CPRS 27 and the MH DLL.

- *CPRS 27 and PXRM*2*6 are installed, but the MH DLL is not running.* CPRS 27 will be able to handle a list of Result Groups. However, the original Result Group evaluation code will not be able to support dialog elements for Result Groups. The Result Group evaluation code will take the first Result Group in the list and will process this Result Group as the only Result Group for the dialog element. The informational message can be defined in the Result Element; however, the Informational message will not display in CPRS 26. The Reminder Manager will be able to set up a dialog containing MH Tests that do not work in CPRS 26. An error message "Error encountered loading MH Test Name" will be displayed in CPRS. The MH Test BOMC is an example of a test that can be defined in PXRM*2*6, but will not function correctly until CPRS 27 and the MH DLL.

- *CPRS 27, PXRM*2*6, and the MH DLL are running* . Once CPRS 27 is released and the MH DLL is running, everything is in place to support the new functionality. Each Result Group per dialog element will be evaluated against the score(s) for each scale returned from the DLL. The Informational Message will appear in CPRS 27, and MH Tests such as the BOMC will work with CPRS 27 and the MH DLL.

A new parameter to toggle the MH DLL on or off will be released with CPRS 27.

Select CPRS Configuration (IRM) Option:  XX  General Parameter Tools

List Values for a Selected Parameter

LE     List Values for a Selected Entity

LP     List Values for a Selected Package

LT     List Values for a Selected Template

EP     Edit Parameter Values

ET     Edit Parameter Values with Template

EK     Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP  Edit Parameter Values

Select OPTION NAME: XPAR EDIT PARAMETER       Edit Parameter Values
Edit Parameter Values
                         --- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME:    OR USE MH DLL   Use MH DLL?

-------- Setting OR USE MH DLL  for System: CPRS27.FO-SLC.MED.VA.GOV --------
Use MH DLL?: YES//

When CPRS 27 is released nationally, this parameter will be set to Y.


### Reminder Exchange

- A problem in Reminder Exchange was reported where a definition would not install and it was giving an error in a FileMan routine. The problem was tracked to the input screen on field 1.4 in file #811.9; on examination of the data dictionary the input screen was corrupted. The solution was to remove the screen.

- A problem with replacement elements/group not installing if a reminder dialog contains branching logic was fixed.

- A problem with a new sponsor entry not installing when the entry is only defined as a sub-item in a reminder dialog was fixed. Remedy #169122.

- A problem with Reminder Exchange not allowing sites to install Result Group/Elements was fixed. Result Group/Elements will be handled similarly to how dialog prompts are handled.

- An “X” in the “Exists” column means that an entry with an identical name already exists on the system. Even though the names are identical, the contents of the packed component could be different than what is on the system. For example, a new code could have been added to a taxonomy or new finding added to a term. The use of checksums was added to Reminder Exchange to provide a way to determine if packed and installed components with identical names also have identical contents. When a component is selected for installation and it already exists on the system, the checksum for the installed version will be computed and compared with the checksum of the packed version. If the checksums match, then the component will automatically be skipped. From now on, when components are packed, their checksums will be stored. Checksums will be calculated for components that were packed before this change was made so the checksum test will work in all cases.

- Reminder Exchange was changed so that it will not attempt to reinstall a dialog element that has already been installed. When a dialog element was used more than once in the dialog, an attempt was made to install it again when it was encountered a second time on the list of dialog elements. Because of the key, the duplicate entry was not installed and an error message was displayed. The dialog was not corrupted –  the only problem was the display of unnecessary error messages.

### Reminder Extracts and Patient Lists

- The format of the “Scheduled to Run:” date in Extract Summary was changed from a FileMan date to an external date.

- The List Manager Extract Summary display was changed to use the reminder print name if it exists. If it does not exist, then the .01 is used. This makes the name display in Extracts consistent with Clinical Maintenance and Reminder Reports.

- Previously, when a patient list was created, the first step was to initialize a stub in the Patient List file; the stub contained only the NAME and the CLASS. If there was an error populating the list and the stub was left, then only someone holding the PXRM MANAGER key could delete it. The stub initialization was changed so that it also inserts the CREATOR and sets the initial TYPE to be public. This makes it possible for the person who created the list to delete it if an error occurs that prevents normal completion of the list-building process.

- If a patient is on a patient list and for some reason the patient is later deleted from the Patient File, then running a Patient Demographic Report or a Health Summary would generate an error. Code was added to handle this problem.

- Dates shown in patient list creation documentation did not always match those displayed by the rule set test action. To correct this, a new routine was created, to be used for all patient list date calculation. Some of the basic date utility functions used throughout Clinical Reminders were optimized to get better performance.

- The setting of date ranges when building a patient list from a reminder definition was made consistent with the way it is done for terms.

- Code was added to catch problems with patient list build dates. The problems will be displayed in the list creation documentation.

- The list template PXRM PATIENT LIST PATIENTS had a bottom margin of 19 and consequently it could not display two of the actions. The bottom margin was changed to 18 so these actions would display.

- The display of Extract Definitions didn’t show the fields INCLUDE DECEASED PATIENTS and INCLUDE TEST PATIENTS. If the value is NULL, then the display will show “NO.”

- Changes were made so that if deceased and/or test patients are included on a patient list, they will be marked with a “D” or “T.”

- When patient demographic report output was queued to p-message or a printer, the output never appeared. This was traced to incorrectly calling a Kernel queuing routine, which was corrected. Work on this also uncovered a problem in some VADPT routines that were not properly protecting variables, in particular % which is also used in the Kernel queuing routines. This may explain why some reminder report outputs have disappeared in the past. A Remedy ticket, #183747, was filed for VADPT.

- All sequences in patient lists and extracts were converted from three-character free-text to a number between 1 and 999. Existing entries will be converted by the post-init.

- The display of patient list creation documentation was improved. The header was expanded to two lines so the entire name of the patient list can be seen. The list template right margin was changed to 132 so the entire display can be seen. The number of patients was moved to a separate line.

- The extract summary display was changed to make it easier to read.

- The list template PXRM PATIENT LIST is obsolete, so it was added to the build as “delete at site.”

- The list template PXRM PATIENT LIST USER had incorrect caption information; it was corrected.

- Two problems that arose when running an extract against a reminder definition were repaired: 1) an undefined error when the reminder definition did not have a print name and 2) the reminder output was not stored in the correct sequence order.

- Extracts were changed to increment the patient list name created from an extract, if the extract is re-run for a previous period. The number at the end of the patient list will match the number at the end of the extract.

- Display of the operation was added to output for Rule Set Test.

- It was found that the SEQUENCE fields in Reminder Extract Definitions, Reminder Extract Counting Rules, Reminder Counting Groups, and Reminder List Rule Sets did not enforce uniqueness. In other words, there was nothing to prevent creation of a Rule Set with two number 1 sequences. A key that enforces uniqueness was added to each of these fields.

- The following list rule changes were made:

*IHD QUERI 412 DIAGNOSIS

Changed LIST RULE ENDING DATE from null to T

*IHD QUERI LIPID LOWERING MEDS

Changed LIST RULE ENDING DATE from null to T

*IHD QUERI PTS WITH QUALIFY VISIT

Changed LIST RULE ENDING DATE from T to BDT


### Reminder Reports

- Timing data was added to the output of Reminder Due Reports.

- The code to build location lists for reminder due reports was replaced with a call to the standard location list builder used for evaluating location list findings. This makes location list building consistent throughout the package and provides improved performance.

- A problem with historical reports including patients whose Visit date was past the end of the report ending date was corrected.

- After patch PXRM*2*4, the list of clinics without patients when running reports against all outpatient locations was more accurate and this caused it to be greatly expanded. To make the list more manageable, two things were done.

- First, when building the clinic list, if the clinic’s inactive date is before the beginning date of the report, the clinic will not be added to list.
- Second, a new prompt “Print locations with no patients” was added. If the answer is affirmative, the list of locations without patients will be displayed at the end of the report. This field will be stored in a reminder report template. Remedy # 168443 and #168399.

- The same help text for the Service Category field will be used when creating a new report or editing a report template. Remedy #171186.

- An undefined error that occurred when running a detailed PCMM provider report was corrected. Remedy #175319.

- When reports were run on a future date and the future date was the first day of the month, any patients that had visits on that date were missed. This was corrected. Remedy #169086 and #176643.

- An undefined error that occurred when saving a reminder due report output to a patient list was fixed.

- Due to changes made elsewhere, a call to a Scheduling API to get appointment data was no longer needed for a historical summary report so it was removed. This should speed up summary reports.

### Reminder Taxonomies

CPT codes 58290-58294, 58951, and 58552-58554 were added to the national taxonomy VA-WH HYSTERECTOMY W/CERVIX REMOVED.  The CPT code 90715 was added to the VA-TETANUS DIPHTHERIA taxonomy.


### Miscellaneous

- The option, TIU Template Reminder Dialog Parameter, was added to the CPRS Configuration menu on the Reminder Managers Menu. It lets users edit the TIU TEMPLATE REMINDER DIALOG parameter while in Reminders options rather than going through the Parameters Menu.

### GEC

- As requested by the primary GEC stakeholder, several reminder dialog entries were moved from the Nursing Assessment GEC dialog to the Care Recommendation GEC dialog. A post-install routine changes several Health Factors from one GEC dialog to another.

### Summary of Mental Health Instruments in Reminder Dialogs

- Instruments with free-text responses can be administered in reminder dialogs once CPRS v27 is released (won’t work in CPRS v26)
- With CPRS v27, pop-up messages can be added to provide directions based on result of MH instrument; for example, if PHQ-2 is positive, you need to complete a PHQ-9 now
- Clinical reminders includes a parameter that determines the length of a test that can be administered through reminder dialogs—defaults to 35 items
- Tests in reminder dialogs will follow restrictions set with MH security keys
- Tests that are restricted or require a license won’t display questions/responses in progress note text
- Completing long tests through reminder dialogs is not recommended
- Patient-administered testing should be completed using the Secure Desktop functionality in MHA.

How does MHA help Integrated Care?

- Need Outcomes, using standardized tools, such as PHQ9
- Can begin using MHA to access and record assessment data for veterans in integrated care programs
- Can use MHA and clinical reminders to identify those patients in a “watchful waiting” phase, needing regular assessment
    - How many veterans in integrated care clinics over the age of 65 endorsed suicidal ideation on PHQ9?
    - Which veterans presenting with cardiac complaints have positive scores on Beck Anxiety Scale?
    - What is the severity of depression seen in veterans enrolled in the pain clinic?
For Secure Patient Testing
    - Patients can complete testing on computer, using Secure Desktop functionality
    - Logs computer off network when testing is completed.  No other application can be accessed
    - Secure Desktop must be installed on the PC (not run from server)
        - Secure Desktop should only be installed on PC’s that veterans will use to complete assessments in MHA