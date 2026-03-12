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
source_file: pxrm_2_12_rn.docx
status: draft
title: pxrm 2 12 rn.docx
---

<!-- image -->

**PXRM*2*12 GMTS*2.7*89 OR*3.0*295 TIU*1.0*249**

**Release Notes**

**October 2009**

Office of Enterprise Development Department of Veterans Affairs

### Contents

INTRODUCTION	1

Clinical Reminders PXRM*2*12 Documentation	1

Web Sites	1

1. Clinical Reminders Enhancements in PXRM*2*12	2

Drug Class Updates	2

New options	2

Reminder Component Inquiry	2

Reminder Component Updates	2

General	3

Reminder Computed Findings	3

Reminder Definitions and Terms	4

Reminder Dialogs	4

Reminder Evaluation	5

Reminder Exchange	6

Reminder List Rules	7

Reminder Reports	7

Reminder Taxonomies	8

1. Bug fixes in PXRM*2*12	8

Remedy tickets addressed:	8

1. GMTS*2.7*89 Description	11
2. OR*3*295 Description	11
3. TIU*1*249 Description	12

APPENDIX A: EXAMPLE OF DRUG CLASS UPDATE MESSAGES	13

APPENDIX B: EXAMPLE OF DIALOG EXCHANGE ERRORS	14

ii	Clinical Reminder Setup Guide	11/10/2009

### Introduction

The Clinical Reminders patch PXRM*2*12 and bundled patches (GMTS*2.7*89, OR*3*295, TIU*1*249) contain modifications to improve reminder exchange tools, reminder due reports, and National Drug Class standardization. They also include changes to support pharmacy encapsulation so the reminder package will no longer have direct access to Pharmacy data. Initial changes to support standardization of reminder findings are incorporated.

The PXRM*2.0*12 build is bundled with the following builds:

OR*3.0*295 – Contains OR bug fixes and changes to an API used by reminders. GMTS*2.7*89 – Supports new Reminder Exchange functionality, new Reminders components, and an enhancement to the TIU/HS Functionality

<!-- image -->

TIU*1.0*249 – Supports new Reminder Exchange functionality, changes to reminder dialogs, and improves the TIU ListManager Health Summary Object display.

#### Clinical Reminders PXRM*2*12 Documentation

| **Documentation**   | **Documentation File name**   |
|---------------------|-------------------------------|
| Installation Guide  | PXRM_2_12_IG.PDF              |
| Manager Manual      | PXRM_2_12_MM.PDF              |
| Release Notes       | PXRM_2_12_RN.PDF              |

#### Web Sites

| **Site**                              | **URL**                                                  | **Description**                                                                             |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                        | Contains manuals, PowerPoint  presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | http://vaww.portal.va.gov/sites/ncrcpub lic/default.aspx | This new committee will direct the development of new and revised national reminders        |
| VistA Document Library                | http://www.va.gov/vdl/                                   | Contains manuals for Clinical Reminders  and                                                |

#### 1 Clinical Reminders Enhancements in PXRM*2*12

#### Drug Class Updates

Similarly to what was done for code set versioning, a new mechanism was created that will be triggered whenever a national drug class update takes place. All reminder definitions, dialogs, and terms will be searched to determine if any of them can potentially be affected by the drug class changes in the update. A MailMan message that describes what was found will be delivered to the Reminders mail group.

#### New options

Reminder Computed Finding Inquiry Check Reminder Dialog for invalid items Expand all Taxonomies

Verify all taxonomy Expansions Finding Usage Report

#### Reminder Component Inquiry

The formatting for the various reminder component inquiries was made as consistent as possible and a computed finding inquiry was added.

#### Reminder Component Updates

The following national Clinical Reminders components are new or updated and redistributed:

| **Component**   | **Name**                                 | **Change**                                                                                                                                                    |
|-----------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RD              | VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL     | Added SUD; added text dialog element for local health summary object for prior AUDIT-C display; reversed order of feedback and advice; made nothing  required |
| RD              | VA-EMBEDDED FRAGMENTS RISK  EVALUATION   | New*                                                                                                                                                          |
| RD              | VA-IRAQ &amp; AFGHAN POST-DEPLOY  SCREEN | Added a FF to the cohort logic                                                                                                                                |
| RD              | VA-TBI SCREENING                         | Changed dialog to have documentation of  discussion of positive screen                                                                                        |
| RL              | VA-OEF/OIF EXCLUSION STOPS               | Added ultrasound stop code                                                                                                                                    |
| RM              | VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL     | Added SUD clinic visit exclusions                                                                                                                             |
| RM              | VA-DEPRESSION SCREEN                     | Updated URLs and description.                                                                                                                                 |
| RM              | VA-EMBEDDED FRAGMENTS RISK  EVALUATION   | New *                                                                                                                                                         |
| RM              | VA-IRAQ/AFGHAN POST  DEPLOYMENT SCREEN   | Uses OEF/OIF in dialog and logic; updated  logic, fixed active duty problem                                                                                   |
| RM              | VA-MHV BMI                               | Removed >, added text changes from NCP                                                                                                                        |
| RM              | VA-MHV COLORECTAL CANCER  SCREEN         | Added upper age limit                                                                                                                                         |

| RM   | VA-OEF/OIF MONITOR REPORTING    | Removed dialog from this reporting  reminder.                              |
|------|---------------------------------|----------------------------------------------------------------------------|
| RM   | VA-TBI SCREENING                | Changes to OEF/OIF in dialog and logic,  fixed active duty issue           |
| RT   | VA-ACTIVE DUTY                  | Updated active duty term description                                       |
| RT   | VA-ALCOHOL NONE PAST 1YR        | Removed MH test from term VA-  ALCOHOL NONE PAST 1YR                       |
| RT   | VA-IRAQ/AFGHAN SERVICE          | Updated to include CFs for OEF/OIF  service that point to the patient file |
| RT   | VA-MHV HIGH RISK FOR FLU        | Updated to use new taxonomy                                                |
| RT   | VA-MHV HIGH RISK FOR  PNEUMONIA | Updated to use new taxonomy                                                |
| RX   | VA-OEF/OIF MONITOR              | New extract                                                                |
| TX   | VA-BREAST TUMOR                 | Changed description to include mass, pain,  abnormality                    |
| TX   | VA-DEPRESSION                   | Updated to FY09 definition                                                 |
| TX   | VA-DEPRESSION OUTPT             | Updated to FY09 definition                                                 |
| TX   | VA-DIABETES                     | Added 250.91-250.93                                                        |
| TX   | VA-HIGH RISK FOR FLU            | New                                                                        |
| TX   | VA-HIGH RISK FOR  FLU/PNEUMONIA | Inactivated                                                                |
| TX   | VA-HIGH RISK FOR PNEUMONIA      | New                                                                        |

* Please provide the Embedded Fragment Surveillance Center (TEFSC) with contact information for the veteran's primary healthcare provider, or enter contact information for the VA medical center staff member deemed appropriate by your VA facility. The point of contact is the person that TEFSC will contact to help arrange for follow-up activities such as biomonitoring.

#### General

<!-- image -->

The right margin for Clinical Maintenance output was increased from 70 to 72. This prevents unnecessary wrapping that was sometimes occurring.

#### Reminder Computed Findings

<!-- image -->

New option: CFI - Reminder Computed Finding Inquiry

o	This new option allows a user to display the information about a computed finding in an easy-to- read format.

<!-- image -->

A new version of VA-BMI is included. The new version is a multi-occurrence computing finding, in contrast with the old version which was a single occurrence computed finding. It provides for more efficient date range searching and the ability to get more than one occurrence. The new multiple occurrence version of the computed finding VA-BMI was applying the date range criteria to both height and weight, in contrast to the single occurrence version which only applied it to weight. A change was made to only apply the date range criteria to the weight. The description was updated to include this information. Display of the date of the height date used in the calculation was added to the output.

<!-- image -->

Note that the changes to VA-BMI (only applying the date range criteria to the weight) also apply to the VA-BSA computed finding, because it uses the same routine to obtain matched weight and height measurements.

<!-- image -->

Note: Sites using the Bar Code Expansion handheld devices from Care Fusion will need to install Vitals patch GMRV*5*25 and the fix from Care Fusion to remove bad dates from the GMRV VITAL MEASUREMENT file before using these computed findings. Because these bad dates can cause problems with the VA-BMI and VA-BSA computed findings, GMRV*5.0*25 is a required build.

<!-- image -->

The description for the VA-COMBAT VET ELIGIBILITY computed finding was incorrect and has been corrected.

<!-- image -->

The VA-PROGRESS NOTE computed finding was changed so it can use either the TIU DOCUMENT DEFINITION title or IEN in the computed finding parameter.

<!-- image -->

VA-DATE FOR AGE is a new computed finding that uses the COMPUTED FINDING PARAMETER to pass an age in years and returns the date the patient will be that age as the date of the computed finding.

<!-- image -->

VA-EMPLOYEE is a new computed finding that returns true if the patient is an employee.

<!-- image -->

VA-ADMISSIONS FOR A DATE RANGE is a list type computed finding that can be used to build a list of patients who have been admitted in the specified date range.

<!-- image -->

VA-DISCHARGES FOR A DATE RANGE is a list type computed finding that can be used to build a list of patients who have been discharged in the specified date range.

<!-- image -->

VA-CURRENT INPATIENTS is a list type computed finding that can be used to build a list of all current inpatients.

<!-- image -->

CF VA-IS INPATIENT- This new computed finding will be true if the patient was/is an inpatient on the evaluation date. The following "CSUB" values will be available:

- ADMISSION DATE/TIME (FileMan format)
- ADMISSION TYPE
- ATTENDING PHYSICIAN
- DATE (FileMan format)
- PRIMARY PROVIDER
- TREATING SPECIALTY
- WARD LOCATION

#### Reminder Definitions and Terms

<!-- image -->

A hint was added on how to add a second occurrence of a finding. The hint will be displayed when a double question mark is typed when editing the findings in a definition or a term.

<!-- image -->

Because of questions about checking for valid usage of TIU Objects, additional checking was added for anyplace a TIU Object can be used in a reminder definition. If an odd number of ―|‖ characters is found, a warning will be issued. Note: an odd number of ―|‖ characters in the text will cause TIU Object expansion to fail.

#### Reminder Dialogs

<!-- image -->

A new option "Check Reminder Dialog for invalid items" has been added to the Dialog Report Menu. This option scans the selected reminder dialog and all of its sub-components for possible problems that could affect the use of the reminder dialog in CPRS. The user can select every dialog type except Additional Prompts and Forced Values. The dialog checker report will check for the following items.

- Disabled dialog items in the selected dialog.
- Incomplete sequences in the selected dialog.
- All sub-items in the selected dialog are pointing to a valid entry on the system.
- All finding items, additional finding items, and orderable items are pointing to a valid entry on the system.
- Result groups are pointing to a valid MH Test and an MH scale has been defined for the result group.
- An odd number of ―|‖ characters in a dialog text field. If this is the case it would not be possible to determine which part is a TIU Object.
- Progress Note Text and the Alternate Progress Note text fields have valid TIU Objects and TIU Template Fields.

Example of output

Select Dialog Reports Option: CH Check Reminder Dialog for invalid items Select Dialog Definition:	EXCHANGE DIALOG	reminder dialog	LOCAL

...OK? Yes//	(Yes)

EXCHANGE DIALOG contains the following errors.

The dialog element INACTIVE OBJECT contains a reference to a TIU

Object NP TIUHS OBJECT TEST in the Dialog Text field. This TIU Object is inactive.

<!-- image -->

A new cross-reference was added to file #801.41: ^PXRMD(801.41,‖RG‖,X,DA(1),DA).

<!-- image -->

A problem was found with the dialog orphan report incorrectly displaying a dialog element only used as a replacement item. Result Groups were also showing in the dialog orphan report when the result group was assigned to a parent element.

<!-- image -->

It was possible for a user to delete a dialog element if it was only used as a replacement item. The user was also able to delete a result group even when it was being used. This has been fixed and the user should not be able to delete an element or a result group if it is assigned to another dialog element/group.

<!-- image -->

The dialog inquiry will now display the value for the patient specific field.

<!-- image -->

Changes were made to reminder dialog functionality to support data standardization of findings, the first of which will be Immunizations and Skin Tests:

o	The DISABLE field has been changed from a free-text field to a set of codes: 0 for NO

1. for DISABLE AND SEND MESSAGE
2. for DISABLE AND DO NOT SEND MESSAGE

These codes will be used when loading a reminder dialog in CPRS. If an item is marked as DISABLE AND SEND MESSAGE, a MailMan message will be sent to the Clinical Reminder mail group.

#### Reminder Evaluation

<!-- image -->

Pharmacy reengineering requires that direct reads of the various pharmacy files be replaced by APIs.

<!-- image -->

Radiology patch RA*5.0*56 was released. This patch adds report status to the data returned by the radiology API Clinical Reminders uses, so the Clinical Maintenance output was changed so it now displays the report status. RA*5.0*56 was added as a required build.

<!-- image -->

Finding date was added as a CSUB data for all reminder finding types.

<!-- image -->

SYSTOLIC AND DIASTOLIC were added as CSUB data for the blood pressure finding.

<!-- image -->

RANK\_DATE was added as a new function that can be used in a Custom Date Due.

#### Reminder Exchange

<!-- image -->

Major enhancements were made to Reminder Exchange. The main change visible to users is the ability to select individual reminder file entries for packing. Now when the Create Exchange File Entry (CFE) action is selected, the user will be presented with the following selection list:

Select from the following reminder files:

REMINDER COMPUTED FINDINGS REMINDER COUNTING GROUP REMINDER DEFINITION REMINDER DIALOG

REMINDER EXTRACT COUNTING RULE REMINDER EXTRACT DEFINITION REMINDER LIST RULE

REMINDER LOCATION LIST REMINDER SPONSOR REMINDER TAXONOMY REMINDER TERM

<!-- image -->

Multiple items of different types can be selected for packing into a single Exchange File entry. In previous versions of Reminder Exchange, only reminder definitions could be selected; the packing included everything the definition needed to function, such as sponsor, findings, and dialog. In this new version of Reminder Exchange, this functionality has been extended. When a reminder file entry is selected from the above list, everything it needs to function will be included in the packed entry. For example, an extract definition could include reminder definitions and rule sets, which in turn have their own dependencies. Because of this, an Exchange file entry may contain components that were not expected. To help the user know what is being included as it is packing up an entry, Reminder Exchange will list every single component that is being included.

<!-- image -->

For reminder dialogs, selection of individual dialog items is now allowed; the user is no longer limited to packing up the entire dialog.

<!-- image -->

TIU/Health Summary Objects will be packed up if they are used in a reminder dialog that is being packed. The Health Summary Type will also be packed up if it does not contain local components and it does not contain the PROGRESS NOTES SELECTED component. A normal TIU Object will not be packed. If a TIU Object or Health Summary Type is not packed up, these items will appear in the list of components in the reminder exchange entries, but they will not be installable. Because of the packing order these items will be installed on the system after the dialog is installed on the system.

<!-- image -->

For TIU Objects, Health Summary Objects, Health Summary Types, and/or entries from the Order Dialog file (#101.41) that are not packed up, descriptive text has been added to the reminder exchange entry summary field, describing what is in the items that were not packed up. This should help the receiving sites re-create these items as needed.

<!-- image -->

Automated dialog error checking has been added. All dialogs that are on the list to be packed will be checked. Two levels of severity will be reported: WARNING and FATAL ERROR. Each error will give a detailed description of the problems that are found. A FATAL ERROR prevents the dialog from being packed; therefore the packing will abort. A WARNING will allow the packing to proceed.

FATAL errors mean the dialog will not work and are caused by things such as a pointer to an item that does not exist.

WARNING means the dialog will function, but possibly not as expected. For example, if the dialog contains a disabled item, a warning will be generated.

The dialog checker will also check to make sure that dialog components contain items and will generate a fatal packing error if none exist.

***See Examples in Appendix B.***

<!-- image -->

For dialogs that are auto-generated from a reminder definition, a check was added that will disable a dialog element/group if the finding item is inactive as a result of Data Standardization.

<!-- image -->

The formatting of the Exchange file entry installation display during a KIDS install was improved. It now shows the number, and if the text is too long to fit on one line, it will be broken into multiple lines instead of just wrapping.

<!-- image -->

Because hospital locations are not standardized, they are not transportable. A list of hospital locations that will not be transported is included in the Exchange file entry description.

#### Reminder List Rules

- There are four possible views in list rule management: finding rule, patient list rule, reminder rule, and rule set. When switching between the views, the screen position was being carried over. For example, if you were in the rule set view and line 10 was at the top of the display and you switched into the reminder rule view, it would start at line 10. If there were less than 10 reminder rules, then the display would be blank. The code was changed to save the current position for each view, so that when a particular view is selected, the display will start at the last screen position of that view.

#### Reminder Reports

- A generalized finding usage report was created. The user inputs a list of findings to search for, and definitions, terms, and dialogs are searched to report where the findings are used. For findings that are from a standardized file, status and mapping information are included. A new option PXRM FINDING USAGE REPORT was created. It was added as an item to the PXRM REMINDER REPORTS menu.
- A new prompt called "Clinic Stops output" was added to reminder due reports. This prompt allows the user to select what type of output to display when running a reminder due report against selected clinic stops. For a detailed report, the user will have the option to display output either by Clinic Stops only (current output) or by Individual Clinics belonging to the clinic stops. For a summary report with the report totals set to either to "Individual Locations" or by Individual locations plus Totals by Facility," the user will have the same options as the detailed report and a third option of reporting the output by Clinic Stops and Individual Clinic(s).

- Another new option "Print percentages with the report output" has been added. If the user replies

―Y,‖ the following percentages will be displayed:

%Applicable = Number Applicable/Total patient * 100

%Due = Number of Due/Number Applicable * 100

%Done = 100-%Due

This field has also been added to the Reminder Report template functionality.

- A new field named Creator was added to report templates. This field is automatically populated when someone creates a reminder report template. It will be used to control edit accesses to the template. In order to edit a template a user must either be the creator or hold the PXRM MANAGER security key. If the user is not the creator or does not hold the PXRM MANAGER security key, they will not see the prompt to edit the template.
- When running a reminder report against multiple patient lists, the results of the report were printed out without the patient list name. Reminder reports were changed to display the patient list name with the patient list results.

#### Reminder Taxonomies

<!-- image -->

##### Two new options

- Verify all taxonomy Expansions (PXRM TAXONOMY EXPANSION VERIFY)

Option for verifying the correctness of all taxonomy expansions

- Expand all Taxonomies (PXRM TAXONOMY EXPANSION ALL)

This option can be used to rebuild all taxonomy expansions (Note the user must hold the PXRM MANAGER security key to use this option.)

<!-- image -->

As a result of problems reported with taxonomy expansion, listing of UPDATE^DIE error messages in taxonomy expansion was changed to use MES^XPDUTL so errors will be included in the Install file if taxonomy expansion is done as part of a KIDS install. Also the name and IEN of the taxonomy will be listed.

<!-- image -->

An error in taxonomy expansion was found and corrected. For CPT codes associated with a radiology procedure the expansion assumed there could only be one radiology procedure per CPT code. This is not the case; the same CPT code can be used with multiple radiology procedures.

The expansion was changed to allow for multiple procedures per CPT code.

#### 2 Bug fixes in PXRM*2*12 Remedy tickets addressed:

231908 - PXRM*2*6 question

239704 - Display Inconsistent for VA-IRAQ&amp;AFGHANISTAN POST DEPLOYMENT 239705- Documentation Conflict

240564 - Incorrect headers appearing in reports.	pulling from incorrect field info from PCMM

Associated Clinics

254537 - EDUC TOPIC with LINKED SUBTOPICS fails to take MAIN ed topic with IMPORT 270130 - TYPO in health factor name (Nat'l GEC IADL section)

287087 - TBI - OEF/OIF Reminders not resolving 288411 - OEF/OIF and TBI reminder not satisfying 291337 - OEF/OIF Report erroring

294762 - TBI won't turn off when NO IRAQ/AFGHAN svc entered 310801 - TBI Dialog slow.

312303 - BMI CF is not evaluating correctly when date range is entered and another BMI is calculated outside the Date Range

319821- Pt is "due" on OEF/OIF report but reminder does not show due for providers on cover sheet. 324324 - Branching logic problem in Iraq Reminder

335776 - When running a reminder report against multiple patient lists, the results of the report are printed out without the patient list name

<!-- image -->

If Installation History was selected for an entry that had never been installed and then Installation Details was selected, it generated an undefined error. This was fixed and now the user will see a ―no dates to select‖ message.

<!-- image -->

The main Reminder Exchange display was truncating seconds on date packed, so the right margin of the list template was increased from 80 to 84.

<!-- image -->

There was a bug in Reminder Exchange where occasionally the checksum of a packed component did not match the checksum of the file entry, even though the packed component came from that exact file entry. This was corrected.

<!-- image -->

If a Location List had a value in the field CREDIT STOPS TO EXCLUDE (LIST), the Location List referenced by this field was not automatically being packed-up. The packing routine was changed so it will be automatically be included.

<!-- image -->

Under certain conditions deletion of a Clinic Stop from a Location List was generating an extraneous node. The cross-references on CLINIC STOP and CREDIT STOP TO EXCLUDE were modified to eliminate this problem. Code was added to the post-init to clean up any bad nodes that may already exist.

<!-- image -->

<!-- image -->

The misspelling ―overwite‖ was corrected to ―overwrite‖.    A prompt in the patient demographic report was incorrect:

Select from the following inpatient items:

1. - WARD LOCATION
2. - ROOM-BED
3. - ADMISSION DATE/TIME
4. - ATTENDING PHYSICIAN

Enter your selection(s): (1-5):

It was corrected to the following:

Select from the following inpatient items:

1. - WARD LOCATION
2. - ROOM-BED
3. - ADMISSION DATE/TIME
4. - ATTENDING PHYSICIAN

Enter your selection(s): (1-4):

<!-- image -->

It was reported with PXRM*2*6 that when running a detailed PCMM Provider report, the output was no longer reporting by provider, but by associated clinic. This has been changed to report by Provider instead of reporting by associated clinic.

<!-- image -->

A problem was found when running a reminder summary report against multiple locations and multiple facilities. If the report was set to report the output by each facility and if there was a location with the same name as each facility and the patient was seen at the different location, the patient would not be included in the count for the location after the first location was counted.

<!-- image -->

The display of the final frequency and age range in reminder test was modified to include what set the final frequency. It could be either from the baseline or a finding. Example:

^TMP(PXRMID,$J,660004,"zFREQARNG")=0Y^^^Finding 1

<!-- image -->

When routine PXRMETCO was distributed in patch PXRM*2*6, it mistakenly had patch 4 on the second line; this was corrected.

<!-- image -->

The second line of PXRMEXLM was erroneously marked with patch 4 when it was released in patch

6. The 4 has been removed.

<!-- image -->

Remedy Ticket 247577 highlighted some confusion with the meaning of a phrase in the code set expansion message. The phrase:

The following are **new CPT codes** in the expansion for this taxonomy:

was changed to:

The following **CPT codes** were not in the previous expansion for this taxonomy:

<!-- image -->

There was a typo in the name of a GEC health factor GEC RECENT CHANGE IN IADL RX-NO. It was changed to GEC RECENT CHANGE IN IADL FX-NO. Remedy ticket # HD0000000270130.

<!-- image -->

The variable pointer setup for reminder definitions and reminder terms incorrectly used the name EDUCATION TOPIC; it was changed to the correct name EDUCATION TOPICS.

<!-- image -->

For a number of years there have been reports that the output from Reminder Due Reports occasionally didn't show up. This problem was not reproducible and a number of things were done to try to find the cause. It appears that a possible cause might be that some sites have created aggressive cleanup routines to delete tasks that are not scheduled. This discovery led to a restructuring of reminder due reports. Previously, two tasks were created: the first assembled the data and the second produced the output. In order to not tie up the output device while the data was being assembled, the print job was not scheduled to run until the assembly job finished. In the new structure, the assembly and print job are combined, but the output device is not opened until the output is ready to print.

<!-- image -->

A problem with incorrect date ordering for multiple occurrences of a location list finding was corrected.

<!-- image -->

In the patient demographics report when only the phone number was selected and the patient had a confidential address in effect, the following error occurred: $ZE=

&lt;UNDEFINED&gt;GETPDATA+53^PXRMPDR *DDATA("ADD",22,"LEN"). The problem was

corrected.

<!-- image -->

A hard error was generated in reminder term inquiry if a health factor finding did not have a category. A change was made so that instead of the hard error, the category will be listed as UNDEFINED. The print template was updated so there is a space after ―No.‖

<!-- image -->

A problem was reported where if an active dialog element/group branched to a disabled dialog element, the original active dialog element/group was still showing in CPRS. To fix this, a national element named VA-DISABLE BRANCHING LOGIC REPLACEMENT ELEMENT will be distributed with patch 12. This element will be used as the replacement element if the branched-to element/group is marked disabled. This new element will display the following text in CPRS:

"You have branched to a disabled element/group. Please contact the reminder manager to fix this dialog."

#### 3 GMTS*2.7*89 Description

<!-- image -->

This patch contains an enhancement to Health Summary Objects. Sites will now be able to overwrite the "No Data Available" message in the TIU/HS Object if the Health Summary Type does not return any data. This was done by adding a new field, OVERWRITE NO DATA, to the Health Summary Object file, file 142.5.

<!-- image -->

To override the no data available message, the SUPPRESS COMPONENTS WITHOUT DATA field must be set to "YES" and text must be defined in the OVERWRITE NO DATA AVAILABLE field. This text will replace the default message.

<!-- image -->

A new API (EN^GMTSDESC) has been created to display the definition of a Health Summary Type, Health Summary Object, and a Health Summary Component in a readable output. This API was created to support Clinical Reminders in posting a description of a Health Summary Type and Health Summary Objects when packing up a reminder dialog that contains a TIU/HS Object.

<!-- image -->

Two new national Health Summary Components are being released with this patch: Clinical Reminders Findings

Clinical Reminders Last Done

The Clinical Reminders Findings component works like the Clinical Maintenance components. However, it only lists the name of the reminder and the findings evaluation for the reminder. It does not display the status line and it does not list the frequency line.

Clinical Reminders Last Done components display the reminder name and the last done date if the last done date is defined. If the last done date is unknown, the last done date will be blank.

Neither of these components will list the header line

―--STATUS--  --DUE DATE       LAST DONE—

<!-- image -->

Remedy ticket #332249

It was reported that a Health Summary Object or a Health Summary Type could not be modified if the user was not the owner and was trying to edit these files in the TIU/HS Object editor.

Resolution: The TIU/HS Object editor was changed so that a user who holds the GMTSMGR security key can edit a Health Summary Object or a Health Summary Type, regardless of the owner.

#### 4 OR*3*295 Description

<!-- image -->

This patch fixes a problem with encounter data not being deleted when the user deletes an unsigned note. This problem was caused when the user wrote a note and entered encounter data for this note. If the user did not sign the note, then worked on other patient records in CPRS, and then went back to the patient with the unsigned note and deleted the note, the note would be deleted from the system.

However, the encounter data would still show in PCE.

<!-- image -->

Remedy 276466: Custom Order View Not Working as Expected. After installation of CPRS 27, one site reported that the Custom Order View "Unverified by Clerk-All Services" was not working properly. The Outpatient Med Orders were not showing up even though they were within the specified date range. This patch fixes this issue so that the Outpatient Med Orders will show up properly.

#### 5 TIU*1*249 Description

<!-- image -->

Several new APIs have been created to display the definition of TIU Object and TIU Template fields.

These APIs will be used by the Clinical Reminder Exchange functionality.

<!-- image -->

A change was made to the TIU/HS List Manager Interface to display a Health Summary Object field OVERWRITE NO DATA MESSAGE. See the GMTS*2.7*89 patch description for more information on this field.

<!-- image -->

The parameter TIU TEMPLATE REMINDER DIALOGS was updated to work with the changes made to Reminder Dialogs in patch PXRM*2*12.

<!-- image -->

Remedy ticket #332249

It was reported that a Health Summary Object or a Health Summary Type could not be modified if the user was not the owner and was trying to edit these files in the TIU/HS Object editor.

Resolution: The TIU/HS Object editor was changed so that a user who holds the GMTSMGR security key can edit a Health Summary Object or a Health Summary Type, regardless of the owner.

## Appendix A: Example of Drug Class Update Messages

Since the reminders package can use drug classes in reminder definitions and terms, a change to a national drug class could impact the accuracy of reminder evaluation and potentially patient care. The Clinical Reminder Manager needs to be informed of potential impacts on existing reminders files that use drug classes whenever changes to drug classes are made. The National Drug File package has a new mechanism, similar to what was done for code set versioning, to update national drug classes. As part of this, the National Drug file package has created a protocol event point that will be triggered whenever a national drug class update takes place. The Reminders package has built a new protocol, which is distributed in PXRM*2*12, that will be attached to the National Drug file drug class update protocol event. Therefore, whenever a drug class update is made, Clinical Reminders will search for all definitions and terms that use the affected drug classes and send a MailMan message listing them to the Reminders mail group.

Setup before testing: In order to receive the Mailman message, the user must be a member of the Clinical Reminders Mail Group established in the Clinical Reminders parameters.

Example of the Pharmacy Package and Reminders Package Mailman messages triggered:

Subj: Products with changed classes [#5726] 03/19/09@13:45 4 lines From: NDF MANAGER In 'IN' basket. Page 1 *New*

Product: LEVALBUTEROL 45MCG/SPRAY INHL,ORAL,15GM

Old Class: GA900 New Class: RE102

Subj: Clinical Reminder Drug Class Update from National Drug File [#5727] 03/19/09@13:45 27 lines

From: POSTMASTER In 'IN' basket. Page 1 *New*

NDF Drug Class update

Review each of the entries to determine if you need to:

- Add the new drug class to the reminder definition/term
- Change the finding to use the new drug class instead
- In some cases, no change will be clinically necessary

VA PRODUCT: LEVALBUTEROL 45MCG/SPRAY INHL,ORAL,15GM (IEN=121)

Has moved from drug class GA900, GASTRIC MEDICATIONS,OTHER, (IEN=121)

to drug class RE102, BRONCHODILATORS,SYMPATHOMIMETIC,INHALATION, (IEN=187)

VA GENERIC LEVALBUTEROL (IEN=3567) is represented by its original drug class GA900, GASTRIC MEDICATIONS,OTHER

in the following reminder definitions:

None

and the following reminder terms: None

VA GENERIC LEVALBUTEROL is used directly in the following reminder definitions:

None

and the following reminder terms:

## Appendix B: Example of Dialog Exchange Errors

As described earlier in the Release Notes, automated dialog error checking has been added as part of Reminder Exchange. All dialogs that are on the list to be packed will be checked. Two levels of severity will be reported: WARNING and FATAL ERROR. Each error will give a detailed description of the problems that are found. A FATAL ERROR prevents the dialog from being packed; therefore the packing will abort. A WARNING will allow the packing to proceed.

FATAL errors mean the dialog will not work; they are caused by things such as a pointer to an item that does not exist.

WARNING means the dialog will function, but possibly not as expected. For example, if the dialog contains a disabled item, a warning will be generated.

##### Example 1

In this example a single reminder dialog is selected for packing. This dialog contains branching logic with the VA-REMINDER DEFINITION computed finding and it includes a TIU/HS OBJECT with the Clinical Reminder Due Health Summary Component.

Select from the following reminder files:

1. REMINDER COMPUTED FINDINGS
2. REMINDER COUNTING GROUP
3. REMINDER DEFINITION
4. REMINDER DIALOG
5. REMINDER EXTRACT COUNTING RULE
6. REMINDER EXTRACT DEFINITION
7. REMINDER LIST RULE
8. REMINDER LOCATION LIST
9. REMINDER SPONSOR
10. REMINDER TAXONOMY
11. REMINDER TERM

Select a file:	(1-11): 4

Select REMINDER DIALOG NAME: EXCHANGE1 DIALOG	reminder dialog	LOCAL

...OK? Yes//	(Yes)

Enter another one or just press enter to go back to file selection. Select REMINDER DIALOG NAME:

Select from the following reminder files:

1. REMINDER COMPUTED FINDINGS
2. REMINDER COUNTING GROUP
3. REMINDER DEFINITION
4. REMINDER DIALOG
5. REMINDER EXTRACT COUNTING RULE
6. REMINDER EXTRACT DEFINITION
7. REMINDER LIST RULE
8. REMINDER LOCATION LIST
9. REMINDER SPONSOR
10. REMINDER TAXONOMY
11. REMINDER TERM Select a file:	(1-11):

Packing components ... Adding routine PXRMCDEF

Adding VA GENERIC COLESEVELAM, IEN=3662 Adding VA GENERIC CERIVASTATIN, IEN=3505

Adding VA GENERIC FENOFIBRATE, IEN=3489 Adding VA GENERIC ATORVASTATIN, IEN=3382 Adding VA GENERIC FLUVASTATIN, IEN=3184 Adding VA GENERIC SIMVASTATIN, IEN=2708 Adding VA GENERIC PRAVASTATIN, IEN=2689 Adding VA GENERIC LOVASTATIN, IEN=2116 Adding VA GENERIC CHOLESTYRAMINE, IEN=1160 Adding VA GENERIC NIACIN, IEN=1080

Adding VA GENERIC GEMFIBROZIL, IEN=968 Adding VA GENERIC CLOFIBRATE, IEN=795 Adding VA GENERIC COLESTIPOL, IEN=406

Adding ORDER DIALOG ZZJM LIPID PROFILE, IEN=1348 Adding GMRV VITAL TYPE BLOOD PRESSURE, IEN=1 Adding MH TESTS AND SURVEYS AUDC, IEN=5

Adding TIU TEMPLATE FIELD A A PAIN HX CAUSE, IEN=765 Adding EDUCATION TOPICS VA-EXERCISE, IEN=363

Adding EDUCATION TOPICS VA-EXERCISE SCREENING, IEN=11 Adding EDUCATION TOPICS VA-DIABETES FOLLOW-UP, IEN=358 Adding EDUCATION TOPICS VA-DIABETES FOOT CARE, IEN=359 Adding EDUCATION TOPICS VA-DIABETES MEDICATIONS, IEN=357 Adding EDUCATION TOPICS VA-DIABETES EXERCISE, IEN=356 Adding EDUCATION TOPICS VA-DIABETES DIET, IEN=362

Adding EDUCATION TOPICS VA-DIABETES LIFESTYLE ADAPTATIONS, IEN=361 Adding EDUCATION TOPICS VA-DIABETES COMPLICATIONS, IEN=355

Adding EDUCATION TOPICS VA-DIABETES DISEASE PROCESS, IEN=354 Adding EDUCATION TOPICS VA-DIABETES, IEN=360

Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE FOLLOW-UP, IEN=8 Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE MEDICATIONS, IEN=7 Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE EXERCISE, IEN=6 Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE DIET, IEN=5

Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE COMPLICATIONS, IEN=4 Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE DISEASE PROCESS, IEN=3

Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE LIFESTYLE ADAPTATIONS, IEN=2 Adding EDUCATION TOPICS VA-SUBSTANCE ABUSE, IEN=1

Adding EDUCATION TOPICS VA-NUTRITION/WEIGHT SCREENING, IEN=12 Adding EDUCATION TOPICS VA-ADVANCE DIRECTIVES SCREENING, IEN=9 Adding EDUCATION TOPICS VA-ADVANCE DIRECTIVES, IEN=338

Adding EDUCATION TOPICS VA-ALCOHOL ABUSE SCREENING, IEN=10 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE FOLLOW-UP, IEN=352 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE MEDICATIONS, IEN=351 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE EXERCISE, IEN=350 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE DIET, IEN=349

Adding EDUCATION TOPICS VA-ALCOHOL ABUSE COMPLICATIONS, IEN=348 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE DISEASE PROCESS, IEN=347

Adding EDUCATION TOPICS VA-ALCOHOL ABUSE LIFESTYLE ADAPTATIONS, IEN=340 Adding EDUCATION TOPICS VA-ALCOHOL ABUSE, IEN=339

Adding EXAM FOBT(CLINIC), IEN=660001 Adding HEALTH FACTORS ALCOHOL USE, IEN=12

Adding HEALTH FACTORS BINGE DRINKING, IEN=19

Adding HEALTH FACTORS PT EDUCATION NEEDS/BARRIERS, IEN=612096 Adding HEALTH FACTORS BARRIERS LACK OF SUPPORT SYSTEM, IEN=612108 Adding HEALTH FACTORS REMINDER FACTORS, IEN=41

Adding HEALTH FACTORS ACTIVATE SIGMOIDOSCOPY, IEN=52 Adding HEALTH FACTORS INACTIVATE SIGMOIDOSCOPY, IEN=51

Adding HEALTH FACTORS ACTIVATE BREAST CANCER SCREEN, IEN=43 Adding HEALTH FACTORS INACTIVATE BREAST CANCER SCREEN, IEN=42 Adding HEALTH FACTORS BRADEN SCALE, IEN=612715

Adding HEALTH FACTORS BRADEN SCALE 9 OR LOWER, IEN=612903 Adding HEALTH FACTORS BRADEN SCALE 10-12, IEN=612902  Adding HEALTH FACTORS BRADEN SCALE 13-14, IEN=612901  Adding HEALTH FACTORS BRADEN SCALE 19 OR HIGHER, IEN=612716 Adding HEALTH FACTORS BRADEN SCALE 15-18, IEN=612714  Adding HEALTH FACTORS LIPID MED INTERVENTIONS, IEN=660077

Adding HEALTH FACTORS ORDER LIPID PROFILE, IEN=660070 Adding HEALTH FACTORS OUTSIDE LDL, IEN=660069

Adding HEALTH FACTORS OUTSIDE LDL 120-129, IEN=80 Adding HEALTH FACTORS UNCONFIRMED DIAGNOSIS, IEN=660084

Adding HEALTH FACTORS UNCONFIRMED IHD DIAGNOSIS, IEN=660085 Adding HEALTH FACTORS LIPID PROFILE INTERVENTIONS, IEN=660074 Adding HEALTH FACTORS OTHER DEFER LIPID PROFILE, IEN=83 Adding HEALTH FACTORS REFUSED LIPID PROFILE, IEN=85

Adding HEALTH FACTORS OUTSIDE LDL &gt;129, IEN=82 Adding HEALTH FACTORS OUTSIDE LDL &lt;100, IEN=81 Adding HEALTH FACTORS OUTSIDE LDL 100-119, IEN=79

Adding HEALTH FACTORS A A PAIN HX OUTSIDE, IEN=660013

Adding HEALTH FACTORS A A PAIN AM OUTSIDE ASSESSMENT, IEN=660017 Adding REMINDER SPONSOR NONE, IEN=19

Adding REMINDER SPONSOR Office of Quality &amp; Performance, IEN=15 Adding REMINDER COMPUTED FINDINGS VA-REMINDER DEFINITION, IEN=35 Adding REMINDER TAXONOMY VA-COLORECTAL CANCER SCREEN, IEN=31 Adding REMINDER TAXONOMY VA-FOBT, IEN=27

Adding REMINDER TAXONOMY VA-FLEXISIGMOIDOSCOPY, IEN=15 Adding REMINDER TAXONOMY VA-MAMMOGRAM/SCREEN, IEN=16 Adding REMINDER TAXONOMY VA-ISCHEMIC HEART DISEASE, IEN=14 Adding REMINDER TERM EDUTEST, IEN=660006

Adding REMINDER TERM VA-ORDER LIPID PROFILE HEALTH FACTOR, IEN=61 Adding REMINDER TERM VA-LIPID LOWERING MEDS, IEN=54

Adding REMINDER TERM VA-OUTSIDE LDL 120-129, IEN=52 Adding REMINDER TERM VA-UNCONFIRMED IHD DIAGNOSIS, IEN=42 Adding REMINDER TERM VA-OTHER DEFER LIPID PROFILE, IEN=41 Adding REMINDER TERM VA-REFUSED LIPID PROFILE, IEN=40 Adding REMINDER TERM VA-LIPID PROFILE ORDERABLE, IEN=39 Adding REMINDER TERM VA-OUTSIDE LDL &gt;129, IEN=36

Adding REMINDER TERM VA-OUTSIDE LDL &lt;100, IEN=35 Adding REMINDER TERM VA-OUTSIDE LDL 100-119, IEN=34 Adding REMINDER TERM VA-LDL, IEN=32

Adding REMINDER TERM VA-IHD DIAGNOSIS, IEN=27 Adding REMINDER TERM	BRANCHING LOGIC TERM, IEN=527 Adding REMINDER DEFINITION EDUTEST, IEN=660020 Adding REMINDER DEFINITION	EDUTEST, IEN=223

Adding REMINDER DEFINITION	DVF REMINDER, IEN=365 Adding REMINDER DEFINITION	AUDC, IEN=318

Adding REMINDER DEFINITION VA-*COLORECTAL CANCER SCREEN (SIG.), IEN=15 Adding REMINDER DEFINITION VA-*BREAST CANCER SCREEN, IEN=4

Adding REMINDER DEFINITION VA-IHD LIPID PROFILE, IEN=70 Adding REMINDER DIALOG PXRM COMMENT, IEN=1

Adding REMINDER DIALOG PXRM REFUSED, IEN=86

Adding REMINDER DIALOG ED EXERCISE REFUSED, IEN=660006 Adding REMINDER DIALOG PXRM OUTSIDE LOCATION, IEN=41 Adding REMINDER DIALOG PXRM VISIT DATE, IEN=40

Adding REMINDER DIALOG ED EXERCISE DONE ELSEWHERE, IEN=660043 Adding REMINDER DIALOG PXRM LEVEL OF UNDERSTANDING, IEN=2 Adding REMINDER DIALOG ED EXERCISE DONE, IEN=660005

Adding REMINDER DIALOG ED EXERCISE SCREENING REFUSED, IEN=660004

Adding REMINDER DIALOG ED EXERCISE SCREENING DONE ELSEWHERE, IEN=660042 Adding REMINDER DIALOG HF BARRIER TO LEARNING, IEN=660169

Adding REMINDER DIALOG ED EXERCISE SCREENING DONE, IEN=660003 Adding REMINDER DIALOG ED SUBSTANCE ABUSE REFUSED, IEN=660002 Adding REMINDER DIALOG ED DIABETES FOOT CARE REFUSED, IEN=660118

Adding REMINDER DIALOG ED DIABETES FOOT CARE DONE ELSEWHERE, IEN=660117 Adding REMINDER DIALOG ED DIABETES FOOT CARE DONE, IEN=660084

Adding REMINDER DIALOG ED NUTRITION/WEIGHT SCREENING REFUSED, IEN=660053

Adding REMINDER DIALOG ED NUTRITION/WEIGHT SCREENING DONE ELSEWHERE, IEN=660286 Adding REMINDER DIALOG ED SUBSTANCE ABUSE DONE ELSEWHERE, IEN=660041

Adding REMINDER DIALOG ED NUTRITION/WEIGHT SCREENING DONE, IEN=660051 Adding REMINDER DIALOG ED SUBSTANCE ABUSE FOLLOW-UP REFUSED, IEN=660282

Adding REMINDER DIALOG ED SUBSTANCE ABUSE FOLLOW-UP DONE ELSEWHERE, IEN=660278 Adding REMINDER DIALOG ED SUBSTANCE ABUSE FOLLOW-UP DONE, IEN=660205

Adding REMINDER DIALOG ED DIABETES REFUSED, IEN=660008

Adding REMINDER DIALOG ED DIABETES DONE ELSEWHERE, IEN=660044 Adding REMINDER DIALOG ED DIABETES DONE, IEN=660007

Adding REMINDER DIALOG ED SUBSTANCE ABUSE DONE, IEN=660001 Adding REMINDER DIALOG EXCHANGE 4, IEN=660000158

Adding REMINDER DIALOG MH AUDC, IEN=1509 Adding REMINDER DIALOG	AUTO AUDC, IEN=1510

Adding REMINDER DIALOG	INACTIVE OBJECT, IEN=1710 Adding REMINDER DIALOG	OBJECT TEST, IEN=1516 Adding REMINDER DIALOG	ORDER ELEMENT, IEN=1049 Adding REMINDER DIALOG	RGP4 ELEMENT 2, IEN=1536 Adding REMINDER DIALOG	RGP4 ELEMENT 1, IEN=1535 Adding REMINDER DIALOG	RESULT GROUP 4, IEN=1534 Adding REMINDER DIALOG	RGP1 ELEMENT 2, IEN=1520 Adding REMINDER DIALOG	RGP1 ELEMENT 1, IEN=1519 Adding REMINDER DIALOG	RESULT GROUP 1, IEN=1529 Adding REMINDER DIALOG	GP1 ELEMENT 2, IEN=1515 Adding REMINDER DIALOG	RGP2 ELEMENT 2, IEN=1522 Adding REMINDER DIALOG	RESULT ELEMENT 1, IEN=1537 Adding REMINDER DIALOG	RGP3 ELEMENT 2, IEN=1526 Adding REMINDER DIALOG	RGP3 ELEMENT 1, IEN=1525 Adding REMINDER DIALOG	RESULT GROUP 3, IEN=1533 Adding REMINDER DIALOG	RGP2 ELEMENT 1, IEN=1521 Adding REMINDER DIALOG	RESULT GROUP 2, IEN=1530

Adding REMINDER DIALOG VA-IHD LIPID OTHER DEFER, IEN=390 Adding REMINDER DIALOG VA-IHD SPACER, IEN=397

Adding REMINDER DIALOG VA-IHD LIPID 120-129 DONE ELSE, IEN=392 Adding REMINDER DIALOG VA-IHD LIPID &gt;129 DONE ELSE, IEN=281 Adding REMINDER DIALOG VA-IHD LIPID 100-119 DONE ELSE, IEN=280 Adding REMINDER DIALOG VA-IHD LIPID &lt;100 DONE ELSE, IEN=279 Adding REMINDER DIALOG VA-IHD LIPID DONE ELSEWHERE GROUP, IEN=404 Adding REMINDER DIALOG VA-IHD UNCONFIRMED DIAGNOSIS, IEN=276 Adding REMINDER DIALOG VA-IHD LIPID REFUSED, IEN=270

Adding REMINDER DIALOG VA-IHD DIRECT LDL ORDERED, IEN=278 Adding REMINDER DIALOG VA-IHD FASTING LIPID ORDERED, IEN=277 Adding REMINDER DIALOG VA-IHD LIPID ORDER GROUP, IEN=272 Adding REMINDER DIALOG VA-IHD LIPID PROFILE HEADER, IEN=209 Adding REMINDER DIALOG VA-IHD LIPID PROFILE, IEN=269

Adding REMINDER DIALOG	GP1 ELEMENT 1, IEN=1514 Adding REMINDER DIALOG	GROUP 1,  IEN=1527 Adding REMINDER DIALOG EXCHANGE DIALOG, IEN=1709

Adding HEALTH SUMMARY COMPONENT PCE HEALTH FACTORS ALL, IEN=204 Adding HEALTH SUMMARY COMPONENT CLINICAL REMINDERS DUE, IEN=202 Adding HEALTH SUMMARY COMPONENT TEST, IEN=5000147

Adding HEALTH SUMMARY COMPONENT PCE HEALTH FACTORS SELECTED, IEN=203 Adding HEALTH SUMMARY TYPE NP NEW HS TYPE, IEN=223

Adding HEALTH SUMMARY TYPE	TEST PROGESS, IEN=208 Adding HEALTH SUMMARY TYPE VA-BRADEN SCALE 30D, IEN=104

Adding HEALTH SUMMARY OBJECTS NP TIUHS OBJECT TEST (TIU), IEN=6600090 Adding HEALTH SUMMARY OBJECTS	LAB TEST (TIU), IEN=6600003

Adding HEALTH SUMMARY OBJECTS VA-BRADEN SCALE 30D (TIU), IEN=6600082 Adding TIU DOCUMENT DEFINITION PATIENT SEX, IEN=74

Adding TIU DOCUMENT DEFINITION PATIENT RACE, IEN=75

Adding TIU DOCUMENT DEFINITION NP TIUHS OBJECT TEST, IEN=1647 Adding TIU DOCUMENT DEFINITION	TIU TEST, IEN=1337

Adding TIU DOCUMENT DEFINITION BRADEN SCALE 30D, IEN=1332

Packing is complete.Notice the above list contains an extensive set of items even though only a single reminder dialog was selected for packing. Everything in the dialog was checked for dependencies and each dependency was automatically included. In turn, each of these was checked for dependencies and so on. This recursive dependency inclusion may generate a list of items that is far larger than originally

##### Example 2

In this example a reminder dialog is selected and the dialog checking generates a warning.

Because only a warning is generated, packing is allowed to proceed.

##### Example 3

In this example, a reminder dialog is selected and the dialog checking generates a fatal error.

Enter another one or just press enter to go back to file selection. Select REMINDER DIALOG NAME:

Select from the following reminder files:

1. REMINDER COMPUTED FINDINGS
2. REMINDER COUNTING GROUP
3. REMINDER DEFINITION
4. REMINDER DIALOG
5. REMINDER EXTRACT COUNTING RULE
6. REMINDER EXTRACT DEFINITION
7. REMINDER LIST RULE
8. REMINDER LOCATION LIST
9. REMINDER SPONSOR
10. REMINDER TAXONOMY
11. REMINDER TERM Select a file:	(1-11):

Checking reminder dialog(s) for errors....

**FATAL ERROR**

EXCHANGE3 DIALOG contains the following errors.

The dialog element	BAD OBJECT contains a reference to a TIU Object OBJECT NOT EXIST in the Dialog Text field. This TIU Object does not exist on the system.

The dialog element	INACTIVE OBJECT contains a reference to a TIU

Object NP TIUHS OBJECT TEST in the Dialog Text field. This TIU Object is inactive.

Cannot create the packed file. Please correct the above fatal error(s).

LOCAL

reminder dialog

Select REMINDER DIALOG NAME: EXCHANGE3 DIALOG

...OK? Yes//	(Yes)

In this example, two errors were found. The first error is considered a Fatal Error, because there is a TIU Object "OBJECT NOT EXIST" in the dialog that does not exist on the system. The second error is the same error as in Example 2. The Fatal Error prevents the dialog from being packed up.