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
source_file: pxrm_2_0_26_rn.docx
status: draft
title: pxrm 2 0 26 rn.docx
---

## Clinical Reminders

**PXRM*2*26**

## Release Notes

**July 2014**


Product Development

Contents

Introduction	1

Patches included in bundle	1

Related Documentation	2

Web Sites	2

Release Notes	3

Project Overview/Background	3

Project Features	4

Functional Specifications	6

Other new features in Clinical Reminders	11

Remedy Tickets	21

Acronyms	23

## Introduction

The purpose of this patch is to update Clinical Reminders to allow the use of ICD-10 codes. A very general approach has been taken, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon Utility. In addition to adding ICD-10 codes, SNOMED CT codes are being added. Since the release of CPRS 29, SNOMED CT codes are being collected by Problem List and Clinical Reminders will be able to search for them.

**NOTE: This project does not add ICD-10 codes or convert ICD-9 codes to ICD-10 codes.**

### Patches included in bundle

**PXRM*2.0*26**

This build changes Clinical Reminders taxonomies from being pointer-based to being Lexicon- based. A number of things are done to accomplish this. The Reminder Taxonomy data dictionary (file #811.2) is restructured, a new taxonomy management system is introduced, and taxonomy evaluation is changed to accommodate the new structure. See the taxonomy section of the Clinical Reminders Manager's Manual for details of the taxonomy management system.

Under the Lexicon-based structure, codes are no longer entered as a range, eliminating the need for taxonomy expansion. The post-install routine will convert all existing taxonomies to the new structure.

**DG*5.3*862**

This build updates the Clinical Reminders Index cross-references in the PTF file (#45) to accommodate ICD-10 diagnosis and procedure codes. It restructures the PTF portion of the Clinical Reminders Index to a generic format that can support all ICD coding systems. This format is:

^PXRMINDX(45,CODING SYSTEM,"INP",CODE,NODE,DFN,DATE,DAS)

^PXRMINDX(45,CODING SYSTEM,"PNI",DFN,NODE,CODE,DATE,DAS)

where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Guide/Programmer's Manual (PXRM\_INDEX\_TM).

The post-install routine will start a background job to rebuild the file #45 index in the new format.

**GMPL*2.0*44**

This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-9 and ICD-10 CM diagnosis codes and SNOMED CT codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

^PXRMINDX(9000011,CODING SYSTEM,"ISPP",CODE,STATUS,PRIORITY,DFN,DLM,DAS)

^PXRMINDX(9000011,CODING SYSTEM,"PSPI",DFN,STATUS,PRIORITY,CODE,DLM,DAS)

where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Guide/Programmer's Manual.

The post-install routine will start a background job to rebuild the file #9000011 index in the new format.

### Related Documentation

**Clinical Reminders PXRM*2*26 Documentation**

| **Documentation**                         | **Documentation File name**   |
|-------------------------------------------|-------------------------------|
| Installation and Setup Guide              | PXRM_2_0_26_IG.PDF            |
| Release Notes                             | PXRM_2_0_26_RN.PDF            |
| User Manual                               | PXRM_2_0_26_UM.PDF            |
| Technical Manual                          | PXRM_2_0_TM.PDF               |
| Manager’s Manual                          | PXRM_2_0_MM.PDF               |
| Clinical Reminders Index Technical Manual | PXRM_INDEX_TM.PDF             |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and related applications.                          |

## Release Notes


### Project Overview/Background

The International Classification of Diseases (ICD) is a clinical coding system developed, monitored, and copyrighted by the World Health Organization (WHO). In the United States (US), the National Center for Health Statistics (NCHS), part of the Centers for Medicare and Medicaid Services (CMS), is the agency responsible for overseeing of the clinical modification to the ICD code set.

On January 16, 2009, the Department of Health and Human Services (HHS) published the 45 CFR Part 162 Final Rule for the Health Insurance Portability and Accountability Act (HIPAA) Administrative Simplification: Modifications to Medical Data Code Set Standards to Adopt the International Classification of Diseases, 10 th Revision Clinical Modification and Procedure Coding System (ICD-10-CM and ICD-10-PCS) for all healthcare organizations currently using the 9 th Edition of the Clinical Modification code set, or ICD-9-CM (also just referred to as “ICD-9”). Presently, ICD-9-CM encompasses both Clinical Modification and Procedure Coding System code sets. On August 24, 2012, the Secretary for HHS published final ruling officially changing the ICD-10 compliance date to October 1, 2014; this was later changed by Congress to not prior to October 1, 2015.

**VA’s Transition to ICD-10:** Implementation of ICD-10-CM and PCS is an immense undertaking, requiring system and business changes throughout all HIPAA-covered entities of the health care industry, including the U.S. Department of Veterans Affairs (VA). All inpatient discharges and outpatient encounter dates on or after the compliance date will require ICD-10 codes as the standard code set for recording and reporting diagnosis and inpatient procedures.  This transition will impact Information Technology (IT) systems, secondary data stores, forms and business processes and stakeholders at all levels of the organization.


### Project Features

The purpose of the Clinical Reminders ICD-10 Update project is to update Clinical Reminders to allow the use of ICD-10 codes. In addition to adding ICD-10 codes, SNOMED CT codes are being added. Since the release of CPRS 29, SNOMED CT codes will be collected by Problem List and Clinical Reminders will be able to search for them.

PXRM*2.0*26

This build changes Clinical Reminders taxonomies from being pointer-based to being Lexicon- based. A number of things are done to accomplish this. The Reminder Taxonomy data dictionary (file #811.2) is restructured, a new taxonomy management system is introduced, and

taxonomy evaluation is changed to accommodate the new structure. See the taxonomy section of the Clinical Reminders Manager's Manual for details of the taxonomy management system.

You can also take advantage of the on-demand training available on the MyVeHU campus ( [www.myvehucampus.com](http://www.myvehucampus.com/) ) to learn more about the new taxonomy management system and changes to how reminder dialogs work. The course number is 14089 and the title is “ICD-10 and Clinical Reminders”.

Under the Lexicon-based structure, codes are no longer entered as a range, eliminating the need for taxonomy expansion. The post-install routine will convert all existing taxonomies to the new structure.

**PXRM*2*26 Taxonomy Conversion**

How do we define “Conversion”?

- **What the Conversion IS:**
    - Converting the file structure in VistA from pointer-based structure to a new structure that will accept multiple coding systems to include:
        - SNOMED CT
        - ICD-9
        - ICD-10
        - CPT-4
        - HCPCS
- **What the Conversion is NOT:**
    - Will not add ICD-10 codes to your current local taxonomies
    - Will not convert current ICD-9 codes in your local taxonomies to ICD-10 codes
    - Will preserve all codes in your local taxonomies
    - Will not delete current taxonomies with ICD9 codes
- **Local sites will need to identify and add ICD-10 codes that mean the same thing as the ICD-9 codes contained within their local taxonomies**
- **This “identifying” of ICD-10 codes must be started now so your local taxonomies will be ready for use by 10/1/2015**

- During the post-install, a number of conversions are performed:

All taxonomies are converted to the new taxonomy management structure.

For all existing taxonomies, any text in the obsolete field, Brief Description, is copied to the new word-processing field, Description.

Under the Lexicon-based structure, ranges of codes cannot be used, so all the codes in each existing range are copied to the new Selected Codes structure. Term/Code becomes “Copy from ABC range LLL to HHH” where:

ABC – three-character coding system abbreviation

LLL – low code

HHH – high code

Example: Copy from ICD range 250.00 to 250.93

- If the numbers of codes in the expansion does not equal the number in the new structure, an error message is issued.
- Active selectable diagnosis and selectable procedure codes are copied into the Selected Codes multiple and marked as Use In Dialog

- All reminders are converted (regardless of whether active or inactive) to the new Lexicon-based structure. Copy ranges will exist after the conversion, which will allow users to edit/delete/add as necessary.
- Taxonomies are automatically generated for all dialogs that use ICD-9 diagnosis codes or CPT codes as a finding or additional finding.

- Dialogs with preexisting taxonomies will pull the prompts in from the appropriate entry in file #801.45.Dialogs with codes only will generate new taxonomies and the codes will be replaced with taxonomies.
- Dialogs elements/groups that are updated will have the edit history updated with the changes due to the data conversion.
- Three MailMan messages will be generated due to the data conversion:
    - A pre-install message lists pre-patched dialogs, elements, and groups to be updated.
    - A post- install message lists dialogs, elements, and groups with the new structure.
    - A message listing of the active dialogs that are affected by the elements and groups that are updated. Using this list, users can find the dialogs for a quick review.

###### Functional Specifications


##### General Requirements

This project includes a new taxonomy management utility that uses a combination of List Manager, FileMan’s ScreenMan *,* and Browser for improved usability. Taxonomies have been restructured to make it possible to use any coding system supported by the Lexicon Utility. Currently taxonomies can be built using codes from ICD-9-CM/PCS, ICD-10-CM/PCS, CPT, HCPCS, and SNOMED CT code systems.

Reminder Dialogs *have* been *modified to use taxonomies as* Finding Items and Additional Finding Items *. They have* been enhanced to add controls to determine if and what pick lists display in CPRS, what prompts are assigned to reminder Dialogs in CPRS, and if a taxonomy should assign codes to Current or Historical Encounters.

**Modifications to Clinical Reminders**

The Reminder Taxonomy Management Utility contains the following actions: add, edit, copy, inquire, view the change log, code search, import, and generate a UID report; it replaces the taxonomy management menu.

Each taxonomy contains metadata describing its purpose and allows users to add codes from one or more coding systems to a taxonomy.

1. The Reminder Taxonomy Management utility provides the ability to add a new taxonomy or edit an existing taxonomy; following are new or modified changes:

- The system allows the user to enter a Description longer than 63 characters and indicate there is additional associated text. (Modified by using ScreenMan)

- After the user enters a term/code, the system displays a list of standard code systems to return a list of Lexicon's search results.(New)

- The system allows the user to select from one or more Standard Code Systems to receive the Lexicon's search results from. (New)

- If the user has already selected terms from the Lexicon's search results, the system indicates those terms/codes that have been selected.(New)

- The system allows users to select active and inactive codes from the Lexicon’s search results. (New)

- The system allows the user to select one, multiple, or a range of codes from the Lexicon's search results to be added to a taxonomy. (New)

- After code selection, the system displays the code system abbreviation, the number of codes selected from that standard code system, and the number of codes set to be used in a dialog under the Selected Codes column. (Modified)

- If no codes are selected, the system displays the text ‘None’ under the Selected Codes column.(Modified)

- The system will not impose any limit of Terms/Codes when adding to taxonomy. (New)

- The system displays the Lexicon's search results from the latest SDO's version and with the following data elements: (New)
    1. Number sequence
    2. Code
    3. Active Date
    4. Inactive Date
    5. Description
    2. ICD9 Lexicon expression
    3. CPT
    4. HCPCS
    5. SNOMED CT Preferred name
    - The system displays all the selected terms/codes that the user has selected for that taxonomy. (New)
    - The system allows the user to import active and inactive codes from one or more standard coding system to one or more taxonomies. (New)
    - The system displays an error message if an error is found after validating the import file. (New)
    - The system allows a user to run a report displaying all inactive codes marked as Used In a Dialog. (New)
    - The Reminder Taxonomy Management no longer supports the following obsolete actions for managing of taxonomies: TX- Selected Taxonomy Expansion, TXV-Verify all Taxonomy Expansions, and TXS-Search Taxonomies for Codes. (New)
    - The Reminder Taxonomy Management Utility provides “Help” text for each standard code systems. (Modified)
    - The Reminder Taxonomy Management utility displays an error message if a user tries to edit a National taxonomy.
    - The Reminder Taxonomy Management utility, while in the Lexicon selection screen, provides the following capabilities for managing taxonomies.
    1. The system allows the user to add a list or range of codes to taxonomy.
    1. The system indicates the codes that have been selected by the user.
    1. The system allows the user to remove one or more codes of the selected codes by entering a single code or list of codes or range of codes.
    1. The system allows the user to mark codes to be used in a dialog.
    1. The system allows the user to remove a code that has been marked to use in dialog.
###### Modifications to VistA Reminder Dialogs

1. The Reminder Dialogs Editor has been modified to use the new centralized taxonomy code and allow users to continue to set up Reminder Dialogs, Dialogs Elements, and Dialog Groups.
2. The Reminder Dialogs Editor no longer allows individual codes from ICD-9 and CPT to be added to an element or a group as a Finding Item or Additional Finding Item.
3. Reminder Dialogs moves the display instructions from a global Taxonomy level to the dialog element level.
    1. The default modifier values come from global taxonomy values
    2. The user has the capability to override the default values
        1. The Reminder Dialogs Editor  manages how taxonomies display in CPRS and allows the user to set the controls based on the following:
            1. The system prompts the user to set the taxonomy selection types that defines if and what pick list displays in CPRS. The possible values for selection types:
                1. All = A pick list displays for active ICD9/10 and CPT codes
                2. Diagnosis Only=A pick list displays only activeICD9/10 codes
                3. Procedure Only=A pick list displays only active CPT codes
                4. None = If no pick list is defined then all active diagnosis or procedure codes on the encounter date is filed to VistA.
                    1. The system prompts the user to set the Diagnosis/Procedure Encounter type, which defines if the codes should be assigned to the current encounter and/or an historical encounter. The system prompt the user to set the Encounter Type:
                        1. Current Encounter
                        2. Historical Encounter
                        3. Both Current and Historical Encounters
                            1. The Reminder Dialog Editor allows:
                                1. Creation of a dialog group and a taxonomy as a Finding Item
                                2. Creation of a dialog group and a taxonomy as an Additional Finding Item.
                                3. Display of an error message when an inactive taxonomy is linked to a Reminder Dialog.
                                4. Display of an error message due to a set up mismatch between taxonomy and a dialog.
                                5. Display of the change from the local Forced Value, Add to Problem List to PXRM FV Add to Problem List and is set to National


###### Graphical User Interface (GUI) Specifications

**Modifications to Clinical Reminders**

**ICD-10 CM codes will become active and ICD-9 CM codes will become inactive on the industry activation date; accordingly:**

1. The CPRS Clinical Reminders GUI application displays ICD-9-CM and ICD-9-PCS codes within the Clinical Maintenance screen if the Date of Interest is **prior** to industry activation date:
2. The CPRS Clinical Reminders GUI application displays ICD-10-CM and ICD-10-PCS codes within the Clinical Maintenance screen if the Date of Interest is **on or after** the industry activation date.
3. A usage check was added for taxonomies that have been inactivated. When you exit the taxonomy edit screen, if the taxonomy has been inactivated, a check will be made to see if the taxonomy is used in any definitions, terms, or dialogs. If it is, a warning will be given and a list of the places it is used will be displayed.

**Modifications to Reminder Dialogs**

1. The CPRS Clinical Reminders GUI application allows users to select and display ICD diagnosis codes based on the following dates of Interest:
    1. Current encounters  use active codes for that Encounter date
    2. Historical encounters use active codes based on system date.
        1. If the reminder dialog is set up for diagnosis code selection and the encounter date is prior the industry activation date, the CPRS Clinical Reminders GUI application allows the user to select ICD-9-CM diagnosis codes
        2. If the reminder dialog is set up for diagnosis code selection and the Encounter date is on or after the industry activation date, the CPRS Clinical Reminder GUI application allows the user to select ICD-10-CM diagnosis codes.
        3. If the Encounter type is set to Current Encounter Only or Both Current Encounter and Historical Encounter, the Current Encounter header text displays as a checkbox.
        4. If the Encounter type is set to Historical Encounter only or Both Current Encounter and Historical Encounter, the Historical Encounter header   text display as a checkbox.
    ################################ Other new features in Clinical Reminders

In addition, the following changes to Clinical Reminders are made in PXRM*2.0*26.

**General:**

In the past, we have encountered problems, especially with Reminder Exchange, caused by using the tilde (~) character in the name of a reminder component. Reminder Exchange was modified to be able to handle the problem, but to prevent unforeseen problems from happening in the future, the input transform used for all the Clinical Reminders .01 fields was modified to not allow “~”.

**NOTE:** If you think that “~” may have been used in the.01 of a reminder component at your site, you can use FileMan to find any such entries. There are two possible approaches. One is to use the verify fields function on the FileMan utilities menu and the other is to use the search function to search for any .01 fields that contain “~”.

**Finding Usage Report:**

The finding multiple in 801.41 had the pointer to 811.2 defined as Taxonomy instead of Reminder Taxonomy. The caused the finding usage report to have selections for Reminder Taxonomy and Taxonomy. It was renamed to Reminder Taxonomy and the problem was eliminated.

The Finding Usage Report did not have the ability to search for reminder definitions and reminder terms that are used in a Reminder List Rule. That ability was added. There was a bug in the Order Check term search that was corrected. Also, the ability to search Order Check rules for definitions was added. Previously, when the report was run, the user had the option to have it delivered as a MailMan message or have it written to the screen. That was changed, so that the user has the option to browse or print it, and then has the option to have it delivered as a MailMan message.

**Reminder Computed Findings:**

The national computed finding VA-REMINDER DEFINITION evaluates a reminder definition. If it is used recursively (evaluating the same definition that is calling it), it will generate framestack errors. This can wreak havoc with production systems. Remedy ticket #761925. Code was added to prevent this. Also, a check for recursion was added to the Integrity Checker.

The print name of VA-REMINDER DEFINITION was changed from VA-Reminder

Definition Computed Finding to VA-Reminder Definition. The variable TEXT was not set before, but is now set to "Reminder: "\_NAME, where NAME is the .01 of the reminder being evaluated. This means that the name of the reminder definition that was evaluated will be displayed in the clinical maintenance output.

The description for VA-FILEMAN DATE was updated to make it clear that the global reminder dates PXRMDOB, PXRMDOD, and PXRMLAD can also be used with this computed finding.

The computed finding inquiry was not displaying the Type; Type was added.

When a computed finding was selected to be used as a finding in a definition or term, the description of the computed finding was displayed on the screen to help the user set it up properly. If Type was not included in the description, then it was not displayed. The computed finding help was upgraded to include Type, Class, and Description, and is now displayed with the Browser instead of just written to the screen.

In the past we have had problems with updated national computed findings being overwritten by outdated versions that were installed via Reminder Exchange. To prevent further occurrences, Reminder Exchange was modified so it will not install national computed findings. From this point on, national computed findings will only be distributed via a KIDS build.

EXPECTED SIGNER and EXPECTED COSIGNER were added as CSUBs to the VA-PROGRESS NOTE computed finding. The description was updated to include these.

When using the special Reminder Location List VA-ALL LOCATIONS in the computed finding VA-APPOINTMENTS FOR A PATIENT, a message was being erroneously displayed:

^TMP(NODE,$J,1,0)=Warning Reminder Location List VA-ALL LOCATIONS

^TMP(NODE,$J,2,0)=does not contain or expand to contain any hospital   locations!

This was corrected. Remedy ticket #916079.

**Reminder Definitions:**

Remedy ticket #718406 reported the following undefined error:

&lt;UNDEFINED&gt;FIEVAL+31^PXRMINDX *FIEVD("VISIT")

^TMP(NODE,$J,1,0)=The following error occurred:

^TMP(NODE,$J,2,0)=&lt;UNDEFINED&gt;FIEVAL+31^PXRMINDX *FIEVD("VISIT")

^TMP(NODE,$J,3,0)=While evaluating reminder PKR DEPRESSION SCREENING

^TMP(NODE,$J,4,0)=For patient DFN=30

^TMP(NODE,$J,5,0)=The time of the error was 01/07/2013@14:25:29

^TMP(NODE,$J,6,0)=See the error trap for complete details.

This occurred when a term was used as a finding in a definition, the field Include Visit Data was set to YES, and the true term finding was not PCE data. This has been corrected.

In reminder definition edit, if the user exited by typing "^" instead of Enter then the edit history was not being set and the integrity check was skipped; Remedy ticket #810582. The code was changed so that if any changes are made to the definition, the integrity check is run and the edit history is set, regardless if the user exits by typing "^" or Enter.

Remedy ticket #623745 reported that incorrect resolution logic such as FI(2)&amp;FF1, should be FF(1), passed the input transform, but caused an undefined error in the definition integrity checker. The input transform was modified to catch incorrect logic elements such as FF1. Also, we added verification of the cohort and resolution logic strings via the input transform, as part of the definition integrity check.  The warning and fatal messages from the integrity checker now all have a consistent format. All fatal messages start “FATAL: “ and all warning messages start “WARNING: “.

**Reminder Definition Integrity Checker:**

The following check was added: When the Usage is 'L', any computed findings that are not list-type are flagged as fatal errors.

Terms that are used as findings in the definition will now be checked to make sure all the mapped findings exist and mapped computed findings are the proper type.

**Reminder Dialogs**

Reminder Dialogs will no longer allow the user to select the following:

-either ICD or CPT codes as findings or additional findings

- an inactive taxonomy

-a taxonomy that does not contain codes marked as Use In Dialog

When accessing a reminder dialog that contains an inactive taxonomy or a taxonomy that does not match the dialog structure, the taxonomy will not show in CPRS and a MailMan message will be sent to the Clinical Reminders mail group listing the problems with the dialog and the taxonomy.

New checking functionality has been added. The checker is run automatically when the taxonomy is saved during an editing session, from the dialog checker report, and when packing up a dialog in Reminder Exchange. It will determine if there is a mismatch between a dialog and the taxonomy that is a finding item.

Reminder dialogs will now allow taxonomies to be used in a group as a finding item. For this to work, the Taxonomy Selection Field must be set to “None”. When converting a dialog element to a group, the Taxonomy Selection Field will be set to “None”.

The patch init conversion routine has been updated to give more detail when updating the dialog file. The conversion routine will also send pre and post-conversion messages listing the details of the dialogs that are being updated.

Patch PXRM*2*26 will release updates to national dialogs that contain ICD and CPT codes. This also requires new taxonomies for the dialogs. These items will be installed using Reminder Exchange. The name of the Exchange file entry is File “PXRM PATCH 26 DIALOGS UPDATES”.

When the VA-AAA SCREENING reminder dialog was released in patch PXRM*2*17, it included a new local forced value named ADD TO PROBLEM LIST. Patch PXRM*2*26 changes the forced value to national and renames it to PXRM FV ADD TO PROBLEM LIST.

**Reminder Evaluation:**

All locks were changed to be compliant with the SAC.

In the Clinical Maintenance Output, the findings are output in the order: cohort, resolution, and information. The results for a true finding were only being output once, which means if a finding was used in both cohort and resolution logic, it was only shown under the cohort findings list. In the few cases where a finding is used for both cohort and resolution logic, this could be confusing because the resolution header can be present with no findings or an incomplete list, because the finding was only listed under the cohort heading. The restriction to only list a finding once was removed.

The true or false value of function findings has not been displayed in the Clinical Maintenance output. It was added if the FF is part of the cohort or resolution logic. FFs that are only for information purposes will not be displayed.

When there was no last done date, it was flagged as a -1. Therefore, the display in the clinical maintenance was:

Resolution: Last done -1.

Users found this confusing, so it was changed to:

Resolution: Last done – None

**Disable/Enable Reminder Evaluation**

The option PXRM INDEX BUILD provides the ability to rebuild selected portions of the Clinical Reminders Index. (For information and details about the Clinical Reminders Index, see the Clinical Reminders Index Technical Manual.) While an index is rebuilding, any reminder that uses the data from that index cannot be correctly evaluated – it will have the status of CNBD (cannot be determined). In the past, a MailMan message was sent to the Clinical Reminders mail group every time a reminder could not be evaluated because an index was rebuilding. Now, when an index is going to be rebuilt, reminder evaluation will be automatically disabled, meaning that any attempt to evaluate a reminder will result in an immediate return of a CNBD status. The Clinical Maintenance display will include text letting the user know that reminder evaluation is disabled and the reason(s). When the index has finished rebuilding, evaluation will be automatically enabled.

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

Any time reminder evaluation is disabled, a message with the subject “REMINDER EVALUATION DISABLED” will be sent to the Clinical Reminders mail group. The message will give the date and time that evaluation was disabled, list the reasons for disabling evaluation, and a search will be made for any Clinical Reminders TaskMan jobs that could be affected. There will be a list of those that are found; it will include the job description, the status (pending or running), and the task number. The results of any jobs that are already running will be unreliable and should be discarded. If possible, these jobs should be stopped, so that they don’t waste system resources. None of the pending jobs should be allowed to start until evaluation is enabled again.

When evaluation is enabled, a message with the subject “REMINDER EVALUATION ENABLED” will be sent to the Clinical Reminders mail group. It will contain the date and time evaluation was disabled and when it was enabled. This gives you the exact period of when evaluation was disabled.

Examples of disable and enable messages:

MailMan message for CRMANAGER, TWO

Printed at CPRS30.FO-SLC.MED.VA.GOV  04/16/14@10:32

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

**Reminder Exchange:**

Automatic packing of the source reminder for a dialog was removed.

Finding lookup in Reminder Exchange was enhanced to handle mnemonic indexes. An example is the Laboratory Test file #60's Synonym field in the 'B' index. If two entries had the same Synonym and the .01 of one of the entries was identical to the Synonym, the lookup would fail and a duplicate warning message was issued. The code was changed to examine all the entries in the 'B' index and compare the .01 for each of them with the name Exchange is trying to find. If there is a single exact match of the name and a .01, the name is resolved and no duplicate warning will be given. If more than one .01 is identical to the name, the warning will still be given. Remedy ticket #783078.

The selection range for the Reminder Exchange actions CHF, CMM, DFE, and IFE was changed so that it includes all Exchange file entries, not just those that are visible.

For some entries in the Reminder Exchange file displaying installation history details for the first install was giving the following undefined error:

&lt;UNDEFINED&gt;DDISP+31^PXRMEXIH ^PXD(811.8,29,130,1,1,"B",0)

This happened for old entries for which the 'B' index on the Component List was never cleaned up. The unused indexes are removed.

Reminder Exchange was updated to handle dialogs that were packed prior to patch 26. If the dialog contains codes, Reminder Exchange will create a new taxonomy when the dialog is installed. It will also replace the codes in the dialog with the new taxonomy. If the dialog contains a taxonomy, Reminder Exchange will update the new fields in the dialog file with the values from the installing site’s Finding Parameters File. Because of these changes, the checksum of the installed dialog will always be different than the checksum of what is in the Exchange file.

The ability to load a Reminder Exchange prd file from a web site has been added.

Example:

Another change to Reminder Exchange was adding a check of the line length and a warning if a line exceeds 245 characters. The maximum value allowed by Kernel is 255 characters but for FileMan word-processing fields it is 245. When a line exceeds this length there is a very high probability that the Exchange entry will not install correctly. If the Exchange entry is transported as a host file, then 255 should work, but if is transported as a MailMan message, then 245 is the limit. The warning was added because previously, when an Exchange entry would not install correctly due to the line length being exceeded, it was difficult to determine the reason.  The solution is to shorten the length of the field being transported. Detailed information about the field that needs to be shortened is given in the warning; for example:

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

**Reminder Function Findings:**

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

Amoebiasis or other GI infection.

FF(6)=1

4B. Screen for Fevers done or not required.

Screen for unexplained fevers that might represent occult malaria or

infection with leishmaniasis.

FF(7)=1

4C. Screen for Skin Rash done or not required.

Screen for persistent rash that might represent infection with leishmaniasis.

FF(10)=0

The output was changed to look like this:

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

**Reminders Miscellaneous:**

The routine PXRMLPOE is changed in PXRM*2*40, which is going to be released as an emergency patch, to fix a problem with MHV secure messaging. Since PXRM*2*40 should be released before PXRM*2*26, the changes to PXRMLPOE made in PXRM*2.0*40 must be incorporated in the PXRM*2.0*26 version.

**National Reminder Exchange Entries:**

The nationally released taxonomy dialog elements in VA-PALLIATIVE CARE NATIONAL CLINICAL TEMPLATE (PXRM*2*31)and VA-ECOE FOLLOW UP (PXRM*2*30) are replaced with updated ones that work correctly after PXRM*2.0*26 is installed.

###### Remedy Tickets

623745

718406

761925

783078

810582

823815

862866

867073

868728

896951

916079

946668

***NOTE – KNOWN ANOMALY:**

For any action that works with a list, you can select the list and then the action, or select the action and then the list. In the first case, the action uses List Manager’s list selection, which displays the list as a string of items. If the list has too many items, it generates an error. The workaround is to select the action first.

For example, on the code selection screen if you do an ICD-10 Lexicon search for diabetes, you will see a list of around 250 codes. If you enter 1-250, you’ll get a range error. However, if you select Add, then you can enter 1-250 and not get an error.

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

**+ Next Screen   - Prev Screen   ?? More Actions**

ADD  Add to taxonomy                    UID  Use in dialog

RFT  Remove from taxonomy               SAVE Save

RFD  Remove from dialog

Select Action: Quit// 1-250

&gt;&gt;&gt;  Range too large: 1-250.


## AcronymsThe OIT Master Glossary is available at [http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)
| Term       | Definition                                                           |
|------------|----------------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                                   |
| Clin4      | National Customer Support team that supports Clinical Reminders      |
| CPRS       | Computerized Patient Record System                                   |
| DBA        | Database Administration                                              |
| DG         | Registration and Enrollment Package namespace                        |
| ESM        | Enterprise Systems Management (ESM)                                  |
| FIM        | Functional Independence Measure                                      |
| GUI        | Graphic User Interface                                               |
| HRMH/HRMHP | High Risk Mental Health Patient                                      |
| IAB        | Initial Assessment & Briefing                                        |
| ICD10      | International Classification of Diseases, 10th Edition               |
| ICR        | Internal Control Number                                              |
| IOC        | Initial Operating Capabilities                                       |
| IVMH       | Improve Veteran Mental Health, one of the Secretary’s 21 initiatives |
| LSSD       | Last Service Separation Date                                         |
| MHTC       | Mental Health Treatment Coordinator                                  |
| OHI        | Office of Health Information                                         |
| OI         | Office of Information                                                |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom                   |
| OIT/OI&T   | Office of Information Technology                                     |
| OMHS       | Office of Mental Health Services                                     |
| ORT        | Operational Readiness Testing                                        |
| PCS        | Patient Care Services                                                |
| PD         | Product Development                                                  |
| PIMS       | Patient Information Management System                                |
| PMAS       | Program Management Accountability System                             |
| PRF        | Patient Record Flag                                                  |
| PTM        | Patch Tracker Message                                                |
| PXRM       | Clinical Reminder Package namespace                                  |
| RSD        | Requirements Specification Document                                  |
| SD         | Scheduling Package Namespace                                         |
| SQA        | Software Quality Assurance                                           |
| USR        | ASU package namespace                                                |
| VA         | Department of Veteran Affairs                                        |
| VHA        | Veterans Health Administration                                       |
| VISN       | Veterans Integrated Service Network                                  |
| VistA      | Veterans Health Information System and Technology Architecture       |

1. ICD10 long description