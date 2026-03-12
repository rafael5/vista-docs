---
app_name: Patient Care Encounter (PCE) (PX)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2017-12
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PX
patch: 219
patch_gap: null
section: ''
source_file: pxumappx.docx
status: draft
title: pxumappx.docx
---

**Patient Care Encounter (PCE)**

**User Manual Appendices**

<!-- image -->

**Version 1.0**

**August 1996**

**Revised December 2017**


Product Development

Revision History

Initiated on

| **Date**   | **Description (Patch # if applic.)**                                | **Project Manager**   | **Technical Writer**   |
|------------|---------------------------------------------------------------------|-----------------------|------------------------|
| 12/2017    | PX*1*219 – Added  Appendix A-11 for PCE/SD Debugging Utilities      | REDACTED              | REDACTED               |
| 07/2014    | PX*1*199 – Updates for ICD-10  (pp. 28, 130) Technical Edit         | REDACTED              | REDACTED               |
| 11/2008    | Formatting Edits                                                    | REDACTED              | REDACTED               |
| 11/2004    | Manual updated to comply with SOP 192-352 Displaying Sensitive Data | REDACTED              | REDACTED               |

*(This page included for two-sided copying.)*

Table of Contents

Appendix A - Clinical Reminders Guidelines &amp; Worksheets	1

Appendix A-1   Start-up Process for Implementing Reminders	1

Appendix A-2   Clinical Reminders at a Glance	9

Appendix A-3   Clinical Reminder Definition Worksheet	13

Appendix A-4   PCE Clinical Integration Worksheet	20

Appendix A-5   Designing Encounter Forms based on Preventive Maintenance Guidelines	22

Appendix A-6   Technical Overview of Reminder Logic	26

Appendix A-7   Developer’s Guide: Developing and Customizing Clinical Reminders	32

Appendix A-8   Distributed Reminder Definitions	50

Appendix A-9   Distributed Taxonomies	146

Appendix A-10   Sample Health Summaries	150

Appendix A-11 - PCE/SD Debugging Utilities	158

Appendix B - Orientation of MAS Users to PCE	164

*(This page included for two-sided copying.)*

## Appendix A - Clinical Reminders Guidelines &amp; Worksheets

### Appendix A-1   Start-up Process for Implementing Reminders

***1. Gather copies of the Appendix A worksheets***

Appendix A-2	Clinical Reminders at a Glance

Appendix A-3	Clinical Reminder Definition Worksheet

Appendix A-4	PCE Clinical Integration Worksheet

***2. Review the reminders distributed with PCE.***

1. Use Appendix A-8 to review distributed reminders names, and how they relate to each other.
2. Number of Reminder Items distributed:

* prefixed reminder items - 15

Amb Care EP’s  prefixed reminder items - 22

***3. Become familiar with the distributed taxonomies.***

1. Use Appendix A-9 to review distributed taxonomies.
2. Number of taxonomies distributed:  30

***4. Identify preventive maintenance guidelines to be used for start-up***

1. Identify clinician(s) who want their clinic to be the start-up clinic for the reminders. Ideally, this should be a clinician who uses encounter forms and health summaries and wants to be actively involved with the clinic's encounter form and reminder definition process.

1. Identify the coordinator who defines the clinic's Encounter Form(s). Inform the coordinator about the reminder definition process, and that it could impact the clinicians' encounter form definition. Get a copy of the current encounter form definition used by the clinic.

1. Work with the clinician to identify the category of reminder(s) from the distributed list in Appendix A-8 that the clinician would like to start with. The * and  reminders that are similar are listed next to each other in Appendix A-2.  This gives an overview of the reminders by guideline category and how they relate to each other. Each row in Appendix A-2 contains the reminders that address the same preventive maintenance guideline, each with a little different definition. The last column is reserved for the coordinator for tracking purposes to indicate the local reminder that is being used to satisfy the preventive maintenance guideline.

1. Use Appendix A-4 to identify the appropriate coordinators for resolving the overlap between package managment of PCE table, clinical reminder, Health Summary, and Encounter Form definitions.

**5.** ***Identify how the clinician would like to see preventive maintenance guideline implemented in his/her clinic:***

1. Show the clinician the “*” (NCHP) and “” (Amb Care EP) prefixed detailed definitions of reminders that relate to the category of guidelines the clinician is interested in. For each definition review the following:

**Print Name**

What text does the clinician want to see on the Health Summary to identify this reminder on the Health Summary?

**Age Findings**

What age range(s) (if any) should be in effect for this reminder? How frequently should the reminder be due? Keep in mind that Taxonomy, and Health Factor findings can alter the age range and frequency criteria.

**Target Result Findings Items**

Determine if the items are appropriate for your site.  Check the items content based on your local definitions from the target result findings file. If the Target Result Finding file is one of those in the left column below, answer the question in the right column.

Lab Test (Chemistry &amp;	What are the laboratory test names that should Hematology only)	be looked for to satisfy the reminder?

Radiology Procedure	What are the radiology procedure names that 	should be looked for to satisfy the reminder?

Measurement	What are the measurements that should be 	looked for to satisfy the reminder?

Education	What are the education topics that should be 	looked for to satisfy the reminder?

Immunization	What are the immunizations that should be 	looked for to satisfy the reminder?

Exam	What are the exams that should be looked for 	to satisfy the reminder?

Skin Test	What are the skin tests that should be looked 	for to satisfy the reminder?

Procedure	What are the CPT codes and ICD 	Operation/Procedure codes that should be 	looked for to satisfy the reminder?

**Taxonomy Items**

Get a detailed list of the taxonomy definitions currently defined for the reminder. (See Appendix A-9 for a list of distributed taxonomy definitions. For each taxonomy, review the list with the clinician and decide if it is appropriate. If not, develop a new list and create a taxonomy reflecting the new list. Keep track of these coded values for integration with the Encounter form. (The clinician may already be collecting preferred codes on the encounter form. The clinic's Encounter Form may be useful to have available during this process.)

1. If the patient is found to have a match with the taxonomy:
    - Decide if the age range and/or reminder frequency should be altered and if it is what the rank shound be.
    - Decide if the taxonomy can be used to satisfy the reminder.
    - Decide what (if any) found text message should be displayed on the Clinical Maintenance component. (The date and what was found will be displayed in the Clinical Maintenance component.)
    - Decide if the taxonomy should control whether or not the reminder is applicable.
        1. If the patient is not found to have a match with the taxonomy:
            - Decide what (if any) non-found text message should be displayed on the Clinical Maintenance component.
            1. Is there a generic found text or not-found text that the clinician would like to see if any of the taxonomies were matched, or if none of the taxonomies were matched?
        **Health Factor Findings Items**
            1. What are the health factors that should be looked for to satisfy the reminder?
            1. If the patient has the health factor information on file:
                - Decide if the age range and/or reminder frequency should be altered.
                - Replace the taxonomy with the health factor.
                - Decide what (if any) found text message should be displayed on the Clinical Maintenance component. (The date and what was found will be displayed in the Clinical Maintenance component.)
                - Repeat the taxonomy with the health factor.
                1. If the patient is not found to have the health factor information on file:
                    - Decide what (if any) not-found text message should be displayed on the Clinical Maintenance component.
                    1. Is there a generic found text or not-found text that the clinician would like to see if any of the health factors were found, or if none of the health factors were found?
                Use the Appendix A-3, Clinical Reminder Definition Worksheet, as a tool to map out the desired definitions for the local reminders. Alternatively, if one of the distributed reminders is very close, make the changes on the distributed print of the reminder definitions.
                If answers to any of the questions above were different than the distributed definition, than a local reminder definition must be created for the preventive maintenance guideline.
                ***6. Review and edit Reminder/Maintenance file entries, as needed:***
                    1. For each specified reminder definition, the PCE files may require new entries to support the reminder. For PCE files review the following files and answer the questions in the right column.
                Education Topic	Are the education topics already defined
                in the Education Topics file?
                Immunization	Are the immunizations already defined in
                the Immunization file?
                Exam	Are the exams already defined in the
                Exam file?
                Skin Test	Are the skin tests already defined in the
                Skin Test file?
                Taxonomy	Is there a taxonomy defined that addresses
                the ICD Diagnosis, ICD Operation/
                Procedure and CPT codes that should be
                looked for to satisfy the reminder.
                Keep in mind multiple taxonomies may be
                defined, each with a different emphasis
                on grouping.
                ***7. Resolve integration issues between the clinic's encounter form and reminder definition:***
                    1. For each reminder to be used, determine what items identified as part of the reminder's criteria should be captured off the encounter form?
                    - Vital types for measurement reminders
                    - Education Topics for education reminders
                    - Immunizations for immunization reminders
                    - Exams for Exam reminders
                    - Skin Tests for Skin Test reminders
                    - Taxonomies with CPT codes and ICD Operation/Procedure codes for Procedure reminders
                    - Taxonomies with ICD codes for diagnosis tracking/reminder alteration within the reminder definition
                    - Health Factors for Health Factor tracking/reminder alteration within the reminder definition
                    1. The Clinical Coordinator responsible for the clinics’ Encounter Form(s) definitions needs to make the appropriate changes to begin collecting any new data that is needed to meet the preventive maintenance guidelines.
                ***8. Define a PCE Reminder/Maintenance Item for each unique reminder:***
                    1. Use the PCE Reminder Maintenance Menu option, “Copy reminder Item,” to copy and edit an existing reminder. You may also create a new reminder from scratch, but is is usually easier to start with an existing reminder.**NOTE** : The technical descriptions may be useful for summarizing what your goals are for the reminder and for sharing with other sites.
                ***9. Test the reminder:***
                There are two ways to test a reminder:
                    - Add the reminder to a test Health Summary. Using a test health summary shows how the reminder looks from a user’s perspective.
                    - Use the Reminder Test option, as described in Appendix A-7. The Reminder Test option can be a useful tool to reminder developers for debugging reminders that don’t work as expected.
                To test a reminder using Health Summary:
                1.  Add the Clinical Maintenance and Clinical Reminder components to the reminder health summary type. Select the reminder item(s) to be tested in the selection item’s prompt from Clinical Maintenance and Clinical Reminder components.
                Health Summary reminder components
                | CLINICAL REMINDERS    | This component evaluates patient findings to determine if the reminder is DUE NOW.                                                            |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| CLINICAL MAINTENANCE  | This component evaluates patient  findings and reports the findings or lack of findings used to determine whether or not the reminder is due. |**NOTE** : If you can’t select the PCE Clinical Maintenance or PCE Clinical Reminder components for the Health Summary, the components must be enabled for use, and the “Rebuild Ad Hoc Health Summary Type” option must be run.
                2.  Use the Print Health Summary Menu, “Patient Health Summary” option to begin testing the component for individual patients. Find or create test patients with data in  that match the reminder definitions, as well as some that won’t have data matches. Assess the reminder results:
                    1. Are the age range and frequency evaluation working?
                    1. Are the target findings found or not found as expected?
                    1. Are the taxonomy findings found or not found as expected?
                    1. Are the health factors found or not found as expected?
                    1. If match and no-match are defined, are they being displayed?
                    1. Are alterations of age and frequency criteria working as expected based on taxonomy or health factor findings?
                3.  Use the Print Health Summary Menu, “Hospital Location Health Summary” option to print the reminders for a clinic, based on a recently passed date range, or next week’s date range. Did the Health Summary print run to completion without any errors?
                4.  Contact IRMS if you encounter errors. REDACTED
                5.  Do not add reminders that are causing errors to the clinic’s health summary. Make the reminders inactive until the problem is resolved.
                6.  Once the reminder is working as expected, show the clinician the reminder defintions, samples of the health summary components results and possibly the encounter form. Gather feedback.
                7.  If necessary, make modifications to the reminder defintion, taxonomies, and encounter forms. After the modifications have been made, resume the testing.
                8.  Identify the Health Summary Coordinator for the clinic. Provide the coordinator with the list of selection item reminders that the clinician has selected for their clinic.
                9.  The Health Summary Coordinator must add the Clinical Reminder and/or Clinical Maintenance components to the clinic’s Health Summary Type, adding the selection items for the Reminder/Maintenance Items.
                *(This page included for two-sided copying.)*


### Appendix A-2   Clinical Reminders at a Glance

This is a worksheet to help track a clinic's selected reminders. See instructions on the following page. Make copies of this page for each clinic.

**Clinic\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

| **NCHP REMINDER GUIDELINE**  **(* prefix)**  **A/I**   | **AMB CARE EP/SITE EXAMPLES DISTRIBUTED**  **( prefix)**  **A/I**   | **LOCAL SITE GUIDELINE**  **A/I**   |
|--------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------|
| Breast Cancer Screen                                   | Mammogram                                                           |                                     |
| Cervical Cancer Screen                                 | Pap Smear                                                           |                                     |
| Cholesterol Screen (F)                                 |                                                                     |                                     |
| Cholesterol Screen (M)                                 |                                                                     |                                     |
| Colorectal Cancer Screen  (FOBT)                       | Fecal Occult Blood Test                                             |                                     |
| Colorectal Cancer Screen  (Sig.)                       | Flexisigmoidoscopy                                                  |                                     |
| Fitness and Exercise Screen                            | Exercise Education                                                  |                                     |
| Hypertension Screen                                    | Blood Pressure Check                                                |                                     |
| Influenza Immunization                                 | Influenza Vaccine                                                   |                                     |
| Pneumococcal Vaccine                                   | Pneumovax                                                           |                                     |
| Problem Drinking Screen                                | Alcohol Abuse Education                                             |                                     |
| Seat Belt and Accident Screen                          | Seat Belt Education                                                 |                                     |
| Tetanus Diptheria Immunization                         |                                                                     |                                     |
| Tobacco Use Screen                                     | Tobacco Education                                                   |                                     |
| Weight and Nutrition Screen                            | Nutrition/Obesity Education                                         |                                     |
|                                                        | Advanced Directives Education                                       |                                     |
|                                                        | Breast Exam                                                         |                                     |
|                                                        | Breast Self Exam Education                                          |                                     |
|                                                        | Digital Rectal (Prostate) Exam                                      |                                     |
|                                                        | PPD                                                                 |                                     |
|                                                        | PSA                                                                 |                                     |
|                                                        | Weight                                                              |                                     |

****A/I=Active/Inactive**

**Clinical Reminders at a Glance Worksheet Instructions**

Use the table on the previous page as a worksheet to help track a clinic's selected reminders.  Each row of this table represents variations of the same type of reminder.

1.  Become familiar with the distributed reminder definitions found in A-8. The VA-* prefixed reminders, based on definitions by the National Center for Health Promotion (NCHP), represent a minimum set of reminders which sites must be able to report on yearly to comply with Congressional law.

2.  The VA- reminders are site and Ambulatory Care Expert Panel examples of reminders. When a  reminder is in the column next to a * reminder, the  reminder is an example of an alternative reminder that still addressess the NCHP guideline.

3.  Use Appendix A-3 as a worksheet for developing the local reminders. This includes requirements for taxonomies, health factors, and target findings that are needed to meet your site's preventive maintenance guidelines.

4.  Use the PCE Table Maintenance options to create any new education topics, exams, immunizations, skin tests, and health factors needed by the reminders.

5.  Use the Taxonomy Copy and Add/Edit options to create and modify site taxonomies, if the distributed taxonomies need modifications.

6.  Use the Reminder Copy and Edit options to create and modify site reminders if the distributed reminders need modifications. Make sure that the NCHP Guideline field is filled in if the site reminder is replacing a * version of a reminder.

7.  Add the names of any local site reminders into table A-2.

8.  Use table A-2 to identify the reminders that you will actually use and enter an  A  in the boxes of the A/I column. This will summarize which reminders should be makred active.

9.  Inactivate any reminders which will not be used by your site. As reminders are identified, you can summarize which reminders won’t be used by entering  I  in the A/I boxes.

10.  Test reminders by adding the reminders to a test Health Summary Types' Clinical Maintenance or Clinical Reminder components, or reference the reminders in the AD HOC Health Summary option for the Clinical Maintenance or Clinical Reminder components. You can also test reminders by using the Reminder Test option (see Appendix A-7). Initially, you may want to focus only on the Clinical Maintenance component to ensure that the  data is being evaluated appropriately.

**NOTE** :  If you’re using reminders for performance measures, you may want to create your own table, listing the performance measure being met and the related reminder.

*(This page included for two-sided copying.)*

### Appendix A-3   Clinical Reminder Definition Worksheet

**Clinical Reminder Definition Worksheet			Page 1 of 6**

Clinic Name/Clinician: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Local Site Reminder NAME:(required)	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter the name of a clinical reminder/maintenance item.

REMINDER TYPE:(req)       Check one of the following:

\_\_ Education

\_\_ Examination

\_\_ Immunization

\_\_ Laboratory Test (chemistry &amp; hematology)

\_\_ Measurement

\_\_ Radiology Procedure

\_\_ Procedure

\_\_ Skin Test

PRINT NAME:(opt)		    	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter the name to show up on the Health Summary.

RELATED REMINDER STANDARD:(opt)	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If this local reminder replaces an NCHP related reminder, identify the related NCHP reminder here. The * prefixed reminders are NCHP reminders.

INACTIVE FLAG:(opt)               '1' FOR INACTIVE; or use the @ to reactivate 						a reminder.

REMINDER DESCRIPTION (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This field contains a clinical description the purpose of the clinical

reminder/maintenance item.

TECHNICAL DESCRIPTION (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The technical description is the place to document the reasoning behind the reminder defintion. It may also be useful for sites sharing reminder definitions.

DO IN ADVANCE TIME FRAME (opt):\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter the time period to mark the reminder due in advance (e.g.,7D,1M,6M,1Y).

SEX SPECIFIC (opt): Circle one or leave blank to apply to both.

‘F’ FOR FEMALE      ‘M’ FOR MALE

IGNORE ON N/A (opt): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This is used to prevent display of Non-Applicable messages on the Clinical Reminders component. The allowed codes are A for age and S for sex. More than one code can be selected.

**Clinical Reminder Definition Worksheet			Page 2 of 6**

Reminder Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

======================= TARGET GROUPS (optional- multiple) ==================

BASELINE AGE FINDINGS (opt): This multiple allows the user to define reminder frequencies based on maximum and minimum age ranges. These are called freqeuncy age range sets. These frequency age range sets are the “Baseline” for the reminder. The baseline frequency age range set can be altered by a taxonomy finding, health factor finding, or computed finding.

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MINIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE NO MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MINIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE NO MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MINIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

AGE NO MATCH TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Clinical Reminder Definition Worksheet			Page 3 of 6**

Reminder Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

================== TARGET RESULT FINDINGS (optional-1 entry) =================

Note: Only specify one result findings file in the reminder definition.

The result findings file must be the appropriate file for the Reminder Type identified on page 1. This is required for all reminder types except procedure.

Reminder Type:	Check one of the following:

Education	\_\_	Education Topics

Examination	\_\_	Exam

Immunization	\_\_	Immunization

Lab Test	\_\_	Laboratory Test (chemistry &amp; hematology)

Measurement	\_\_	GMRV Vital Type

Radiology Procedure	\_\_	Radiology Procedures

Procedure	\_\_	leave blank

Skin Test	\_\_	Skin Test

TARGET RESULT DESCRIPTION (opt): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This describes what and why particular target result finding items need to be selected for this reminder.

TARGET RESULT FINDINGS ITEMs (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

These are the item(s) from the Target Result Findings File that should be used to evaluate patient findings for this reminder. These entries are based on a variable pointer definition. Use the PREFIX.? for a list of the currently defined entries for the reminder, and the total items available to select from in the file.

Method to Define Items

FILE 	PREFIX	Description			Not in the file

-----------  ------     ----------------        -----------------------

60    	L        LABORATORY TEST		See Lab Coordinator

(NOTE: Chem &amp; Hem only)

71    	R        RADIOLOGY TEST		See Radiology Coordinator

9999999.09	E        EDUCATION TOPIC		PCE Table Maintenance

9999999.14 	I        IMMUNIZATION		PCE Table Maintenance

9999999.28  	SK       SKIN TEST			PCE Table Maintenance

9999999.15	EX       EXAM				PCE Table Maintenance

120.51	VT       VITAL MEASUREMENT TYPE	See Gen Med Rec - Vitals 								package coordinator

TARGET RESULT FOUND TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TARGET RESULT NOT FOUND TEXT (opt): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Clinical Reminder Definition Worksheet			Page 4 of 6**

Reminder Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

=================== TAXONOMY FINDINGS (optional-multiple) ===================

You will need to fill out one of these sheets for each taxonomy used by the reminder. One General Found and Not Found Text may be defined for all the taxonomies if appropriate.

TAXONOMY (opt): You can define more than one taxonomy in the reminder definition, and alter the reminder criteria based on whether the patient has a match. Enter the Taxonomy name, or just list the ICD Diagnosis, ICD Operation Procedure, or CPT codes which need searched for. If no taxonomy containing these codes exist, you will need to create one.

TAXONOMY ITEM(s): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

or identify standard codes to build taxonomy(s).

ICD Diagnosis codes:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD Operation/Procedures:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CPT procedures:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A match on a taxonomy can alter the reminder criteria or give clinical feedback based on the following fields:

MINIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOUND TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NOT FOUND TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RANK FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN DATE DUE CALC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN APPLY LOGIC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

=========================================================================

TAXON GENERAL FOUND TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAXON GENERAL NOT FOUND TEXT (opt):\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Clinical Reminder Definition Worksheet			Page 5 of 6**

Reminder Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

============== HEALTH FACTOR FINDINGS (optional - multiple) =================

You will need to fill out one of these sheets for each health factor used by the reminder. One General Found and Not Found Text may be defined for all the health factors if appropriate.

HEALTH FACTOR FINDINGS (opt)

These are the health factors that should be evaluated as findings for this reminder. Each health factor is defined in the Health Factor file with a health factor category. A match on the most recent health factor finding item(s) found for a patient represented in the reminder defintion may be used to alter the reminder criteria. Multiple most recent health factor finding item(s) are based on the health factor category the health factor findings item belonged to. If 5 health factor finding items are defined in the reminder, from 2 unique health factor categories, then only the two most recent health factor findings (1 from each category) for a patient will be used by the reminder.

HEALTH FACTOR FINDINGS ITEM (opt): 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A match on a health factor can alter the reminder criteria or give clinical feedback based on the following fields:

MINIMUM AGE (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOUND TEXT (opt):			\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NOT FOUND TEXT (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RANK FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN DATE DUE CALC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN APPLY LOGIC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

=========================================================================

HF GENERAL FOUND TEXT (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

HF GENERAL NOT FOUND TEXT (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Clinical Reminder Definition Worksheet			Page 6 of 6**

Reminder Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

===================== COMPUTED FINDINGS (optional) =========================

You will need to fill out one of these sheets for each computed finding used by the reminder.

COMPUTED FINDINGS (opt): This multiple allows computed findings when the findings criteria are more involved than just checking the existence of an entry in the patient's clinical data. An example might be the calculation of Body Mass Index (BMI) based on the height and weight.

ROUTINE (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

An example of a routine specified would be OBESE;PXRMOBES.

A match on a computed finding can alter the reminder criteria or give clinical feeback based on the following fields:

MINIMUM AGE (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAXIMUM AGE (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REMINDER FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SHORT DESCRIPTION (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FOUND TEXT (opt):			\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NOT FOUND TEXT (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RANK FREQUENCY (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN DATE DUE CALC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USE IN APPLY LOGIC (opt):	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

=========================== APPLY LOGIC (optional) =========================

APPLY LOGIC (opt):		\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

For reminders requiring APPLY LOGIC that cannot be defined using the USE IN APPLY LOGIC field on taxonomies, health factors, and computed findings the APPLY LOGIC can be entered here. For a detailed explanation of how to use this field see Appendix A-7.

========================== END OF REMINDER DEFINITON =========================

### Appendix A-4   PCE Clinical Integration Worksheet

Use this worksheet to coordinate the management of a clinic's PCE Reminder impact on Health Summary, PCE, and Encounter Forms. Successful integration depends on how well the clinical coordinators work with each other and the clinicians they represent.

**Clinic Information:**

Clinic Name:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinicians/Team:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic's Health Summary Types:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Encounter Form #:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ID #:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Coordinators:

PCE Clinical Coordinator 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Health Summary Clinical Coordinator	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Preventive Maintenance Coordinator	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Encounter Form Clinical Coordinator	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Integration Checklist for management of:

| **Reminder/Maintenance Item(s) selected:**   | **PCE Table**  **Review/Update**   | **Reminders**  **\_\_\_\_\_\_\_\_\_\_\_**  **Define &#124; Test**   | **Health**  **Summary**  **\_\_\_\_\_\_\_\_\_\_**  **CM  &#124;  CR**   | **Encounter**  **Form**  **Review/**  **Update**   |
|----------------------------------------------|------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------|
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |

**Clinic Name:**

Integration Checklist for management of:

| **Reminder/Maintenance Item(s) selected:**   | **PCE Table**  **Review/Update**   | **Reminders**  **\_\_\_\_\_\_\_\_\_\_\_**  **Define &#124; Test**   | **Health**  **Summary**  **\_\_\_\_\_\_\_\_\_\_**  **CM  &#124;  CR**   | **Encounter**  **Form**  **Review/**  **Update**   |
|----------------------------------------------|------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------|
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |
|                                              |                                    |                                                                     |                                                                         |                                                    |

### Appendix A-5   Designing Encounter Forms based on Preventive Maintenance Guidelines

The Health Summary provides critical clinical information related to the patient for Ambulatory Care Encounters. The Encounter Form is a means of documenting clinical activity/updates for a patient during the patients encounter. This appendix sub-section gives a brief overview of how PCE, AICS, and Health Summary packages impact the clinician for tracking a patient's preventive maintenance guidelines. The following is a possible scenario for the clinician:

**1** .  A clinician receives the Encounter Form and Health Summary for use during the encounter.

**2** .  The clinician reviews the Clinical Reminder component and/or the Clinical Maintenance component for items that are “DUE NOW.”

**3** .  The Encounter Form is predefined with a format that supports the clinical activity related to the reminders. If the clinician is going to ask about education, the clinician should also be prepared to give the appropriate education and document the information gathered from the inquiry.

**Recommendation:** If a clinician asks about the education needed and finds that education is needed, but isn’t able to give the education, the *screening bubble should not be checked off* on the encounter form. The screening should be filled in when the clinician determines education is not indicated or when the clinician screens *and* gives the education.

Two examples of encounter forms are shown on the following pages with items that might be included to support reminders. These examples are:

- An abbreviated format for a clinic that is not interested in tracking details related to the reminders.

- An example of how detailed a clinic could choose to go with data capture related to the reminders.

If the clinician gives abbreviated education for all facets of the education topic, then the “Alcohol Use Education” header should be the box checked, otherwise check-off the appropriate education given. If the clinician has health factor and diagnosis findings that he or she would like to see documented during the screening process, the appropriate boxes should be checked off.

*a) Minimum Set*

*The following example represents a “minimum set” of information (without bubbles) that we recommend for the encounter form. It satisfies NCHP and can also be captured by PCE based on current PCE definitions. If new education topics are needed to represent the remaining screening items, they can be added.*

| **Screening**                  | **Procedures:**        |
|--------------------------------|------------------------|
| Alcohol  Use Screening         | Immunizations:         |
| Tobacco Use Screening          | Pneumococcal           |
| Nutrition/Obesity Screening    | Influenza              |
| Fitness and Exercise Screening | Tetanus and Diphtheria |
| Seatbelt Use Screening         |                        |
| **Education**                  | Pap Smear              |
| Alcohol Use Education          | FOBT                   |
| Exercise Education             | Sigmoidoscopy          |
| Nutrition/Obesity Education    |                        |
| Seatbelt Use Education         |                        |
| Smoking Cessation Education    |                        |

*b) Sample of Detailed Content (without bubbles)*

| **Alcohol Use Management**           | **Tobacco Use Management for Health Promotion**   |
|--------------------------------------|---------------------------------------------------|
| Alcohol  Use Education               | Tobacco Use                                       |
| Screening/Inquiry                    | Screen/Inquiry                                    |
| Diet                                 | Smoking Education                                 |
| Disease Process                      | Health Factors                                    |
| Complications                        | Lifetime Non-Tobacco User                         |
| Exercise                             | Lifetime Non-smoker                               |
| Follow-up                            | Current Non-smokeless                             |
| Lifestyle Adaptations                | Current Smoker                                    |
| Medications                          | Smokeless Tobacco User                            |
| Alcohol Use Health Factors:          | Current Non-Smokeless                             |
|                                      | Tobacco User                                      |
| Non-Drinker                          | Hx of Chewing Tobacco                             |
| Family Hx of alcohol abuse/addiction | Hx of smoking                                     |
| Heavy Drinker (3 or more/day)        | Hx of  Sec. Smoke Inhal.                          |
| Moderate Drinker                     | Diagnosis: Tobacco Abuse-                         |
| Binge Drinking                       | Continuous                                        |
| Drinking Alone                       | Episodic                                          |
| Hx of Alcohol Treatment              | In Remission                                      |
| Legal Complications                  | Unspecified                                       |
| Driving Under the Influence          | Use Disorder - Unspecified                        |
| Alcohol Use Diagnoses:               |                                                   |
| Delirium Tremens                     |                                                   |
| Cirrhosis of the Liver               |                                                   |
| Alcohol Abuse - Unspecified          |                                                   |
| Alcohol Abuse - Episodic             |                                                   |
| Alcohol Abuse - Continuous           |                                                   |
| Alcohol Abuse - In Remission         |                                                   |
| Alcohol Dependence                   |                                                   |
| Alcohol Dependence - In              |                                                   |
| Remission                            |                                                   |
| Hx of Alcoholism                     |                                                   |

*(This page included for two-sided copying.)*

### Appendix A-6   Technical Overview of Reminder Logic

**NOTE** : This overview is extracted from the PCE REMINDER/ MAINTENANCE ITEM file data dictionary description.

This file contains the defintions of reminders which can be selected for use in the Health Summary package components:

CLINICAL REMINDERS - This component evaluates patient findings

to determine if the reminder is "DUE NOW."

CLINICAL MAINTENANCE - This component evaluates patient

findings and reports the findings or lack of findings used to

determine whether or  not the reminder is due.

Reminder definitions are contained in this  file. Each reminder is categorized by "Reminder Type." Based on the reminder type, a "Target Result Findings File" is specified along with the particular items from that file that should be used. For example, for an immunization reminder the target is the IMMUNIZATION file. The particular items would the the name(s) of the immunizations. For each specified immunization, the V IMMUNIZATION file is searched for patient results. For laboratory reminders, exact names used by the site make up the item list.

Target age groups may be defined for each reminder in this file, based on patient's age. Reminder frequencies may be defined by age ranges in the Baseline Age Findings multiple. The age range and reminder frequency to use for the reminder can be altered based on findings of diagnosis, procedure, or health factor data related to a specific patient. The patient's age from PIMS is used for age findings.

Diagnosis and Procedure findings are based on definitions of coded standard ranges defined in the Taxonomy file. The Taxonomy file is distributed with predefined definitions for all reminders distributed by the PCE package. Facilities may create their own taxonomies to use in locally defined reminders. The taxonomies defined for evaluating patient data for diagnosis and procedure findings for a reminder are defined in the "Taxonomy Findings" fields. Based on the patient taxonomy findings, a reminder's frequency and minimum and maximum age criteria can be changed. Text may be defined which will be displayed in the Health Summary "Clinical Maintenance" component to reflect taxonomy findings found or not found in the patient data.

If a taxonomy definition in the Taxonomy file is defined with ICD Diagnosis code ranges, the following files are checked for findings of a code within the Diagnosis ranges specified:

PROBLEM File (AUPNPROB) in Problem List

V POV File (AUPNVPOV) in PCE (representing problems/diagnosis treated

at encounter)

PTF File (DGPT) in PIMS (Inpatient Diagnosis summary information)

If a taxonomy definition in the Taxonomy file is defined with CPT code ranges, the following patient file is checked for findings of a code within the CPT ranges specified:

V-CPT File (PCE, representing procedures done at patient encounters)

If a taxonomy definition in the Taxonomy file is defined with ICD Operation/

Procedure codes, the following patient file is checked for findings of a code within the ICD Operation/Procedure code ranges specified:

PTF File (PIMS, Inpatient Operation/Procedures summary information)

Health factors are defined in the Health Factors file, and can be used to identify health indicators for use with reminders. These factors are not based on a coded standard. A pre-defined set of health factors distributed by PCE is used by the distributed reminders. Facilities may create their own health factors to use in locally defined reminders. The health factors defined for evaluating patient data for this reminder are defined in the "Health Factor Findings" fields. Based on the patient health factor findings, a reminder's frequency and minimum and maximum age criteria can be changed. Text may be defined which will be displayed in the Health Summary "Clinical Maintenance" component to reflect health factor findings found or not found in the patient data.

PCE's "V HEALTH FACTORS" file represents a patient's health factors recorded as of a given encounter date. All Health factors defined in the reminder are used to evaluate patient information in the "V HEALTH FACTORS" file. Out of all the health factor findings, the most recnet health factor finding within each health factor category will be used for the reminder processing.

Health factors can be used to record “pertinent negative findings” for example “lifetime non-smoker”. Pertinent negative findings can be used to make a reminder non-applicalbe via an “AND NOT” entry in the Use in Apply Logic field. The Health Factor File contains INACTIVATE and ACTIVATE health factors for each NCHP (* prefixed) reminder. The * reminder defintions provide examples of how the INACTIVATE health factor can be used to stop a reminder for a particular patient. This provides a generic mechanism to record pertinent negatives. The Health Factor Comment field can be used to record the reason for inactivating the reminder.

Computed Findings may also be used in the reminder logic. Computed Findings are based on the evaluation of M logic as true or false. The distributed reminders includes an example of computed findings to evaluate patient height and weight information to calculate the Body Mass Index (BMI) and compare it to a national standard of 27 indicating obesity.  Local facilities may program their own computed findings for use with reminders.

A complete description of the elements of this file and how they actually define a reminder can be found in Appendix A-7, Developing and Customizing Clinical Reminders.

Each processing step of the reminder logic can create output. This output is stored in a working array that is built up as the reminder is processed.

**General Reminder Logic**

The general logic is very similar for every reminder. Specific differences for each reminder type can be found in the Reminder Type File.

SEX SPECIFIC - If the reminder is sex specific, the sex of the patient is compared with the reminder sex.  If the patient is the wrong sex, go to step OUTPUT, otherwise continue.

HEALTH FACTORS - If there are health factors associated with the reminder they are compared with the health factors associated with the patient.  These are found in the file AUPNVHF. Any matching health factors are stored in the health factor array HFA.

STANDARD CODED ITEMS - Standard coded items are specified for the reminder by a list of Taxonomies.  The entries in the Taxonomy files specify a range of codes (low to high) and the file the codes come from.  The permissible taxonomy entries are ICD diagnosis (file 80 ICD), ICD operation/procedure (file 80.1 ICD0), and CPT (file 81 ICPT).  For each taxonomy entry, a list of internal entry numbers (iens) corresponding to the codes within the specified range is built.  These lists are ICD9IEN, ICD0IEN, and ICPTIEN.  Next a list of iens is built for the patient.  ICD9 patient entries are searched for in the Problem of Visit File V POV (AUPNVPOV), the Patient Treatment File (DGPT), and the Problem List File (AUPNPROB).  We search for ICD0 entries in DGPT and ICPT entries in V CPT (AUPNVCPT).  The patient entries and taxonomy entries are examined for matches.  The most recent entry is retained.  In the case of ICD9 or ICD10, the most recent entry in each of the possible search files is retained.

COMPUTED FINDINGS - If a computed finding has been defined for the reminder it is evaluated.

BASELINE CRITERIA - The baseline values for minimum age, maximum age, and reminder frequency are established by determining the appropriate age range for the patient.

FINAL CRITERIA - Each computed finding, health factor and taxonomy can have a minimum age, maximum age, and frequency associated with it.  When a particular item is found and it has a minimum age, maximum age, and frequency the baseline values are replaced by these values. In the case where there is more than one applicable computed finding, health factor, or taxonomy, and there are conflicting ages or frequencies the conflict is resolved by 1) using the rank frequency filed to specify the ranking, with number 1 being the highest rank frequency; 2) (when rank frequency not defined) using the frequency and age range that has the frequency that will make the reminder be given most often.

AGE CHECK - After the previous step is complete, final values for minimum age and maximum age are available.  A null value has special significance.  It means that no check is to be made.  Thus if the minimum age is null and the maximum age is 65 then the reminder is applicable to all patients through age 65. If the patient does not meet the age criteria, we go to step OUTPUT, otherwise we continue.

APPLY LOGIC - An optional “apply logic” string can be given as part of the reminder definition. When it is not modified by a user, a default APPLY LOGIC string is created, based on the reminder definition. The string specifies Boolean logical combinations of computed findings, health factors and taxonomies.  This gives us the ability to precisely define when the reminder should be given. For example, we could require that a particular taxonomy be found before the reminder is given. The USE IN APPLY LOGIC field for the taxonomy is defined with “AND”. The default logic looks for all USE IN APPLY LOGIC references to build the APPLY LOGIC string.The string is in the form of a MUMPS logical string.  An example is: (SEX)&amp;(AGE)&amp;TF(5)). SEX and AGE will always be part of the default APPLY LOGIC. The USE IN APPLY LOGIC field for taxonomies, health factors, and computed findings can be defined as “AND”, “OR”, “AND NOT”, “OR NOT”, logic, as needed.

TARGET PATIENT ENTRIES -  A list of all the patient's entries in the target file is built.  The specific targets depend upon the reminder.  They can be found in the Reminder Type file.

MOST RECENT TARGET DATE - The patient list is matched against the entries in the target file for the reminder topic and the date the reminder was last given is determined.

DUE DETERMINATION - The date found in the previous step along with the dates for any taxonomies, health factors, and computed findings that have USE IN DATE DUE CALC marked as YES are compared to find the most recent date. The most recent date, the final reminder frequency, and do in advance time are used to determine when the reminder is due.

OUTPUT - The final step is to take all the information stored in the working array and format it for Health Summary to display.

*(This page included for two-sided copying.)*

### Appendix A-7   Developer’s Guide: Developing and Customizing Clinical Reminders

**Introduction**

The Clinical Reminders/Clinical Maintenance portion of PCE (namespace PXRM) can be called by Health Summary to provide clinical reminder or maintenance information for a patient. The PXRM routines and associated data files have been developed to allow sites maximum flexibility both for customizing reminders and for developing new ones. This appendix section provides detailed information about customizing or developing new reminders.

The easiest way to create a new reminder is to copy an existing one and then edit it.

Menu options to aid the customization and development of new reminders include

*PXRM Reminder Cop* y, *PXRM Reminder Edi* t, *PXRM Taxonomy Cop* y, and *PXRM*

*Taxonomy Edi* t.

**Files associated with PXRM:**

PCE REMINDER/MAINTENANCE ITEM (#811.9)

PCE REMINDER TYPE (#811.8)

PCE TAXONOMY (#811.2)

The contents and use of each of these files are described below.

**Reminder Definition**

The primary file is PCE REMINDER/MAINTENANCE ITEM, which provides the

definition of a reminder item. The other two files provide auxiliary information

required for defining the item. Since the ability to set up or modify an item requires

an understanding of the contents of this file, each of the fields is described below.

**Group 0**

^PXD(811.9,D0,0)= (#.01) NAME [1F] ^ (#1) REMINDER TYPE [2P] ^ (#1.2) PRINT

==&gt;NAME [3F] ^ (#1.3) DO IN ADVANCE TIME FRAME [4F] ^ (#1.4)

==&gt;RELATED REMINDER STANDARD [5P] ^ (#1.6) INACTIVE FLAG [6S]

==&gt;^ ^ (#1.8) IGNORE ON N/A [8F] ^ (#1.9) SEX SPECIFIC [9S] ^

NAME - This is the name of the reminder; examples: VA-BLOOD PRESSURE, VA-MAMMOGRAM, and VA-CHOLESTEROL.

REMINDER TYPE - This is a pointer to the PCE REMINDER TYPE file and

defines the type of reminder. The defined types are EDUCATION, EXAMINATION,

IMMUNIZATION, MEASUREMENT, PROCEDURE, RADIOLOGY, and SKIN

TEST. Every reminder must be one of these types.

PRINT NAME - This is the name that will be used when the reminder is printed in

the Health Summary.

DO IN ADVANCE TIME FRAME - This is a time window used in the due now

calculation. If a reminder was due in 20 days and this parameter had the value

30D, then the reminder would be marked as due now. However, if the reminder was

due in 35 days it would not be marked as due.

See the reminder frequency description in Group 7 for a description of how to enter

time units.

RELATED REMINDER STANDARD - This is a pointer to one of the NCHP

reminders distributed with the Clinical Reminders. It is used to mark a reminder as

meeting or exceeding the requirements of a particular NCHP reminder.

INACTIVE FLAG - This flag marks a reminder as active or inactive for use by

Health Summary. The option (IN)/ACTIVATE REMINDERS can be used to change

this flag.

IGNORE ON N/A - The default behavior of the Clinical Maintenance component is

to give a message that a reminder is non-applicable, N/A, due to the patient’s sex or

age. This field is a string consisting of single letters that will prevent these

messages from being displayed. To prevent the age message from being displayed

this field should contain an “A.” Similarly, for sex it should contain an “S.”

SEX SPECIFIC - This field is used to make a reminder sex-specific. The entry is a

single letter code, F for female and M for male. If it is left blank, then the reminder

is applicable for either sex.

^PXD(811.9,D0,1,0)=^811.92^^ (#2) REMINDER DESCRIPTION

^PXD(811.9,D0,1,D1,0)= (#.01) REMINDER DESCRIPTION [1W] ^

REMINDER DESCRIPTION - This word processing field is used to provide a

description of the reminder. This allows for documentation of the reminder within

the file.

**Group 2**

^PXD(811.9,D0,2,0)=^811.93^^ (#3) TECHNICAL DESCRIPTION

^PXD(811.9,D0,2,D1,0)= (#.01) TECHNICAL DESCRIPTION [1W] ^

TECHNICAL DESCRIPTION—This is the technical description of the reminder.

**Group 3**

^PXD(811.9,D0,3,0)=^811.94P^^ (#4) TARGET RESULT FINDINGS

^PXD(811.9,D0,3,D1,0)= (#.01) TARGET RESULT FINDINGS FILE [1P] ^

^PXD(811.9,D0,3,D1,1,0)=^811.941^^ (#1) TARGET RESULT DESCRIPTION

^PXD(811.9,D0,3,D1,1,D2,0)= (#.01) TARGET RESULT DESCRIPTION [1W] ^

^PXD(811.9,D0,3,D1,2,0)=^811.944V^^ (#4) TARGET RESULT FINDINGS ITEM

^PXD(811.9,D0,3,D1,2,D2,0)= (#.01) TARGET RESULT FINDINGS ITEM [1V] ^

^PXD(811.9,D0,3,D1,3,0)=^811.945^^ (#5) TARGET RESULT FOUND TEXT

^PXD(811.9,D0,3,D1,3,D2,0)= (#.01) TARGET RESULT FOUND TEXT [1W] ^

^PXD(811.9,D0,3,D1,4,0)=^811.946^^ (#6) TARGET RESULT NOT FOUND TEXT

^PXD(811.9,D0,3,D1,4,D2,0)= (#.01) TARGET RESULT NOT FOUND TEXT [1W] ^

TARGET RESULT FINDINGS FILE - This is a pointer to target file. For example

if the reminder was of type education then the target file would be the Education

Topics file.

TARGET RESULT DESCRIPTION - This provides a description of the items

targeted by the reminder.

TARGET RESULT FINDINGS ITEM - This multiple is a variable pointer to the

specific items targeted by the reminder. For example, the targets for education

reminders can be selected from the education topics defined in the Education Topics

file. For immunization reminders, the targets can be selected from immunizations

defined in the Immunization file. See the distributed reminders for further

examples.

TARGET RESULT FOUND TEXT - If there is a record of the patient having

received the target item, for example a particular education topic, then the found

text will be passed to Health Summary for display.

TARGET RESULT NOT FOUND TEXT - If there is no record of the patient having

received the target item, then the Not Found Text will be passed to Health

Summary for display.

**NOTE: FOUND TEXT and NOT FOUND TEXT**

Groups 3, 4, 6, 7 (AGE MATCH TEXT, AGE NO MATCH TEXT), and 10

contain FOUND TEXT and NOT FOUND TEXT entries.

Each of these entries is optional and will only be returned for display by Health

Summary if it is present.

**Group 4**

^PXD(811.9,D0,4,0)=^811.95P^^ (#5) TAXONOMY FINDINGS

^PXD(811.9,D0,4,D1,0)= (#.01) TAXONOMY [1P] ^ (#1) MINIMUM AGE [2N] ^ (#2)

==&gt;MAXIMUM AGE [3N] ^ (#3) REMINDER FREQUENCY [4F] ^ (#6)

==&gt;RANK FREQUENCY [5N] ^ (#7) USE IN DATE DUE CALC [6S] ^

==&gt;(#8) USE IN APPLY LOGIC [7S] ^

^PXD(811.9,D0,4,D1,1,0)=^811.954^^ (#4) FOUND TEXT

^PXD(811.9,D0,4,D1,1,D2,0)= (#.01) FOUND TEXT [1W] ^

^PXD(811.9,D0,4,D1,2,0)=^811.955^^ (#5) NOT FOUND TEXT

^PXD(811.9,D0,4,D1,2,D2,0)= (#.01) NOT FOUND TEXT [1W] ^

^PXD(811.9,D0,4.1,0)=^811.95051^^ (#5.1) TAXON GENERAL FOUND TEXT

^PXD(811.9,D0,4.1,D1,0)= (#.01) TAXON GENERAL FOUND TEXT [1W] ^

^PXD(811.9,D0,4.2,0)=^811.95052^^ (#5.2) TAXON GENERAL NOT FOUND TEXT

^PXD(811.9,D0,4.2,D1,0)= (#.01) TAXON GENERAL NOT FOUND TEXT [1W] ^

TAXONOMY - This is a pointer to the TAXONOMY file. The taxonomy entries have

the form: low^high^file where low and high specify an inclusive range of applicable

codes and file is the number of the file where the codes are located. The file number

can be 80 (ICD diagnosis), 80.1 (ICD operation/procedure), or 81 (CPT).

Taxonomies are defined and given names which are used when setting up a

reminder.

MINIMUM AGE - If the patient is found to have this taxonomy, this minimum age

will override the baseline minimum age. If this is left blank, then the baseline

minimum age will apply. This provides a mechanism to change the age

requirements if a taxonomy is found. (See also Age Findings, Group 7.)

MAXIMUM AGE - This can override the baseline maximum age as with the

minimum age above. (See also Age Findings, Group 7.)

REMINDER FREQUENCY - This can override the baseline reminder frequency as

with the minimum age above. (See also Age Findings, Group 7.)

RANK FREQUENCY - If more than one taxonomy and/or Health Factor is found

for a patient and each of these has its own frequency age range set, then a question

arises concerning which one to use. Rank Frequency is used to answer the

question. The frequency age range set from the finding with the highest Rank

Frequency will be used. (The highest rank is 1.) If no ranking information is

available then the software will use the frequency age range set with the frequency

that will cause the reminder to be given most often.

USE IN DATE DUE CALC - This field can have the value YES, NO, or blank. If it

is YES then finding this taxonomy is equivalent to finding the target item. The

most recent date for any of the coded values found in the taxonomy will be used in

the Date Due calculation.

USE IN APPLY LOGIC - The field specifies how the taxonomy is to be used in the

Apply Logic, see Group 9. The allowed values are AND (&amp;), OR (!), AND NOT (&amp;’),

OR NOT (!’), and blank. When it is blank the taxonomy is not used in the Apply

Logic. When it contains one of the other values, which is a logical operator, it is

included in the Apply Logic preceded by the specified operator.

FOUND TEXT - This text will be returned for display by Health Summary if the

taxonomy is found.

NOT FOUND TEXT - This text will be returned for display by Health Summary if

the taxonomy is not found.

TAXON GENERAL FOUND TEXT - If any of the taxonomies are found then this

text will be returned for display by Health Summary.

TAXON GENERAL NOT FOUND TEXT - If none of the taxonomies are found then

this text will be returned for display by Health Summary.

^PXD(811.9,D0,6,0)=^811.911P^^ (#11) HEALTH FACTOR FINDINGS

^PXD(811.9,D0,6,D1,0)= (#.01) HEALTH FACTOR FINDINGS ITEM [1P] ^ (#1) MINIMUM

==&gt;AGE [2N] ^ (#2) MAXIMUM AGE [3N] ^ (#3) REMINDER

==&gt;FREQUENCY [4F] ^ (#6) RANK FREQUENCY [5N] ^ (#7) USE

==&gt;IN DATE DUE CALC [6S] ^ (#8) USE IN APPLY LOGIC [7S] ^

^PXD(811.9,D0,6,D1,1,0)=^811.9114^^ (#4) FOUND TEXT

^PXD(811.9,D0,6,D1,1,D2,0)= (#.01) FOUND TEXT [1W] ^

^PXD(811.9,D0,6,D1,2,0)=^811.9115^^ (#5) NOT FOUND TEXT

^PXD(811.9,D0,6,D1,2,D2,0)= (#.01) NOT FOUND TEXT [1W] ^

^PXD(811.9,D0,6.1,0)=^811.9110111^^ (#11.1) HF GENERAL FOUND TEXT

^PXD(811.9,D0,6.1,D1,0)= (#.01) HF GENERAL FOUND TEXT [1W] ^

^PXD(811.9,D0,6.2,0)=^811.9110112^^ (#11.2) HF GENERAL NOT FOUND TEXT

^PXD(811.9,D0,6.2,D1,0)= (#.01) HF GENERAL NOT FOUND TEXT [1W] ^

HEALTH FACTOR - This is a pointer to the Health Factors file. Health factors

that are associated with the reminder are included this way.

MINIMUM AGE - Just as with taxonomy, this minimum age can override the

baseline minimum age if the Health Factor is found.

MAXIMUM AGE - The same as for the minimum age above.

REMINDER FREQUENCY - The same as for minimum age above.

RANK FREQUENCY - The same as for taxonomy, see Group 4.

USE IN DATE DUE CALC - The same as for taxonomy, see Group 4.

USE IN APPLY LOGIC - The same as for taxonomy, see Group 4.

FOUND TEXT - This text will be returned for display by Health Summary if the

Health Factor is found.

NOT FOUND TEXT - This text will be returned for display by Health Summary if

the Health Factor is not found.

HF GENERAL FOUND TEXT - If any of the health factors are found then this text

will be returned for display by Health Summary.

HF GENERAL NOT FOUND TEXT - If none of the health factors are found then

this text will be returned for display by Health Summary.

^PXD(811.9,D0,7,0)=^811.97^^ (#7) BASELINE AGE FINDINGS

^PXD(811.9,D0,7,D1,0)= (#.01) REMINDER FREQUENCY [1F] ^ (#1) MINIMUM

==&gt;AGE [2N] ^ (#2) MAXIMUM AGE [3N] ^

^PXD(811.9,D0,7,D1,1,0)=^811.973^^ (#3) AGE MATCH TEXT

^PXD(811.9,D0,7,D1,1,D2,0)= (#.01) AGE MATCH TEXT [1W] ^

^PXD(811.9,D0,7,D1,2,0)=^811.974^^ (#4) AGE NO MATCH TEXT

^PXD(811.9,D0,7,D1,2,D2,0)= (#.01) AGE NO MATCH TEXT [1W] ^

Age findings provides a way to change the reminder frequency based on a patient’s

age. The age ranges are searched and if the patient’s age lies between the minimum

and maximum age these become the baseline frequency age range set. (A frequency

age range set is a frequency and its associated minimum and maximum ages.)

There cannot be any overlap between the age ranges because this gives rise to a

conflict which cannot be resolved.

REMINDER FREQUENCY - The frequency to give the reminder. This is given as

nD, nM, or nY, where D stands for days, M for months, Y for years, and n is a

number. Thus, for a reminder that is to be given once a year, the values 365D, 12M,

or 1Y would all work. (This format is used for all time-related entries.) There are

two special reminder frequencies. The frequency 0Y means that the reminder is

never to be given. This is used to create reminders that are given only to patients

who have certain findings. For example the distributed VA-DIABETIC reminders

are setup up so they are given only to patients who have the VA-DIABETIC

taxonomy. The second special frequency is 99Y. This is used for reminders that are

to be given once in a lifetime.

MINIMUM AGE - The minimum age associated with this reminder frequency.

MAXIMUM AGE - The maximum age associated with this reminder frequency.

AGE MATCH TEXT - If the patient’s age lies in the specified age range, this text

will be returned for display by the Health Summary.

AGE NO MATCH TEXT - If the patient’s age does not lie in the specified age

range, this text will be returned for display by the Health Summary.

^PXD(811.9,D0,9)= (#9) APPLY LOGIC [1F] ^

APPLY LOGIC - This specifies how the findings for a reminder are to be used in

determining if the reminder is applicable for a patient. The findings consist of any

combination of computed findings, health factors, and taxonomies that are

included in the reminder definition.

The Apply Logic used in the reminder evaluation can be created in one of two ways.

If this field is left blank then the software will create an Apply Logic string starting

with a default string of (SEX)&amp;(AGE) appending each finding that has a non-blank

Use in Apply Logic entry with the specified operator. As an example consider a

reminder that contains taxonomy number 28 with a Use in Apply Logic entry of &amp;.

In this case the software will create an Apply Logic string of

(SEX)&amp;(AGE)&amp;(TF(28)).

The other alternative is to specify the Apply Logic directly in the reminder

definition. When this is done the software will use whatever is in the Apply Logic

field ignoring any Use in Apply Logic fields. If this alternative is used care must be

taken that the Apply Logic is written so that it will evaluate to a proper Mumps (M)

logical. In order to do this you need to understand how the Apply Logic is used.

The Apply Logic is based on the M Boolean logical operators, &amp; (AND) , ! (OR) and

their negations &amp;’ (AND NOT), !’ (OR NOT). The &amp; operator requires both items to

be true in order to be true. The ! operator is true if either of the items is true. This is

easiest to understand by looking at some examples.

Consider reminder number X which has the following taxonomy entries:

^PXD(811.9,X,4,1,0)=7

^PXD(811.9,X,4,2,0)=11^40^75^6M^5^^^&amp;

and the following health factor entries:

^PXD(811.9,X,6,1,0)=4^42^^1Y

^PXD(811.9,X,6,2,0)=9

The default logic, which is created automatically if the Apply Logic is left blank,

would be (SEX)&amp;(AGE)&amp;(TF(11)). SEX is evaluated if the reminder is sex-specific.

It is set to true if the patient is the correct sex. If the reminder is not sex-specific,

then SEX is always true. AGE is evaluated after the final frequency age range set

has been established. It is set to true if the patient’s age falls within the age range.

If there is no age range specified for the reminder then AGE is always true. TF(11)

stands for the taxonomy finding for taxonomy number 11. (Similarly HF stands for

health factor finding and CF for computed finding.) Thus the default logic says

that SEX, AGE, and TF(11) must all be true in order for the reminder to be

applicable. Since health factors 4 and 9 have a blank Use in Apply Logic field they

are not is not included in the Apply Logic and are used for information only.

If you require a more complex Apply Logic than the simple appending mechanism

of the Use in Apply Logic provides then you must include the Apply Logic in the

reminder definition. Some examples:

(SEX)&amp;(AGE)&amp;(HF(9)!(TF(7)) - the reminder is applicable if SEX and AGE and

either health factor 9 or taxonomy 7 is true (found).

(SEX)&amp;(AGE)&amp;’(HF(9)&amp;TF(7)) - the reminder is applicable if SEX and AGE are

true and neither health factor 9 or taxonomy 7 is true.

The Reminder Inquiry option can be used to see the Apply Logic string in both the

numeric form and expanded form where the number is replaced by the name of the

finding. This can be used to make sure that the Apply Logic used in the reminder

evaluation is actually what you think it is.

**Group 10**

^PXD(811.9,D0,10,0)=^811.9001^^ (#10) COMPUTED FINDINGS

^PXD(811.9,D0,10,D1,0)= (#.01) ROUTINE [1F] ^ (#1) MINIMUM AGE [2N] ^ (#2)

==&gt;MAXIMUM AGE [3N] ^ (#3) REMINDER FREQUENCY [4F] ^

==&gt;(#4) SHORT DESCRIPTION [5F] ^ (#7) RANK FREQUENCY

==&gt;[6N] ^ (#8) USE IN DATE DUE CALC [7S] ^ (#9) USE IN

==&gt;APPLY LOGIC [8S] ^

^PXD(811.9,D0,10,D1,1,0)=^811.90015^^ (#5) FOUND TEXT

^PXD(811.9,D0,10,D1,1,D2,0)= (#.01) FOUND TEXT [1W] ^

^PXD(811.9,D0,10,D1,2,0)=^811.90016^^ (#6) NOT FOUND TEXT

^PXD(811.9,D0,10,D1,2,D2,0)= (#.01) NOT FOUND TEXT [1W] ^

At this point we can see that reminder definitions are very flexible and easily

customized. However, there may be cases where the requirements are not entirely

met by the mechanisms described above. In these cases, computed findings can be

used. Computed findings are M routines that return 1 for true and 0 for false. They

can be used in the logic just like taxonomies and health factors.

ROUTINE - The name of an M routine that will be executed. For obvious reasons,

only an experienced M programmer should attempt to create a computed factor

routine. Programming details are given in the section Writing a Computed Finding

Routine. This entry is specified in the form ENTRYPOINT;ROUTINE.

MINIMUM AGE - This is the minimum age associated with the computed finding

routine and can be used to override the baseline minimum age.

MAXIMUM AGE - This is the maximum age associated with the computed finding

routine and can be used to override the baseline maximum age.

REMINDER FREQUENCY - This is the reminder frequency associated with the

computed finding routine and can be used to override the baseline reminder

frequency.

SHORT DESCRIPTION - This field can be used to contain a short description of

what the Computed Finding does.

RANK FREQUENCY - The same as for taxonomies, see Group 4.

USE IN DATE DUE CALC - The same as for taxonomies, see Group 4.

USE IN APPLY LOGIC - The same as for taxonomies, see Group 4.

**How is the final frequency age range set determined?**

As we have seen, there can be a minimum age, maximum age, and frequency

associated with computed findings, health factors, and taxonomies that can

override the baseline values. The question is: How is the final set determined?

The baseline values are set from the data in Group 7. The age range in which the

patient’s age falls sets the minimum age, maximum age, and frequency. Leaving a

minimum age blank means that there is no minimum age for the reminder;

therefore, the patient will always meet the minimum age requirement. The same

holds true for maximum age.

Frequency is a different matter since a frequency is required to determine if a

reminder is due. A special frequency of 0Y means that FOUND, NOT FOUND

TEXT can be displayed, but the reminder can never come up as due, based on the

finding associated with the 0Y frequency. Only those findings with a frequency

greater than 0 can be used in the date due calculation. A frequency of 99Y can be

used for reminders that are due once in a lifetime.

Each taxonomy, health factor, or computed finding can have an associated

frequency age range set. If the finding is true¾i.e., the patient has the taxonomy,

health factor, etc.¾ the frequency age range set associated with the finding can

override the baseline values. Generally this is done to widen the coverage of the

reminder. For example, the VA-INFLUENZA IMMUNIZATION is given once a

year to patients 65 and over. The baseline frequency age range set has a minimum

age of 65, no maximum age, and a frequency of 1Y. The VA-HIGH RISK FOR

FLU/PNEUMONIA taxonomy has no minimum age, maximum age, and a

frequency of 1Y. Thus, for patients who have this taxonomy, the baseline frequency

age range set is overridden and the reminder is applicable for all ages.

**Rank Frequency field**

In the case when there is more than one true finding and each has a frequency age

range set, a method is needed to determine which one to use. The Rank Frequency

field was added to meet this need. The frequency age range set with the highest

rank (1 being the highest) will be used. If there are no Rank Frequency values

available, then the frequency age range set that will cause the reminder to be given

most often will be used. For example, if one frequency was 1Y and the other 6M,

then 6M would be used since the reminder would be given every six months instead

of once a year.

**Writing a Computed Finding Routine**

A computed finding routine can be used in those cases when the general reminder

logic does not provide the required functionality. Computed finding routines should

be written as functions that return 1 for true and 0 for false. An example has been

provided with the VA-NUTRITION/OBESITY EDUCATION reminder. The

computed finding routine is PXRMOBES with entry point OBESE. This function

looks up the patient’s most recent height and weight measurements and then

calculates the body mass index. If the BMI is greater than 27 it returns 1, meaning

the patient is considered obese.

In addition to returning true or false, these functions may set INFO nodes of the

working array ^TMP(“PXRM”,$J,”WA”). The information nodes have the format

^TMP(“PXRM”,$J,”WA”,”INFO”,PXRMITEM,RNAME,DESCRIPTION)=TEXT

DESCRIPTION describes the type of information and TEXT is the information.

TEXT will be displayed by the Clinical Maintenance Component of Health

Summary. The routine should set DESCRIPTION and TEXT. The other indices are

already defined.

In PXRMOBES the INFO nodes are used to return information such as no height or

weight measurement available or to return the calculated value of the BMI.

**Applicable Menu Options**

The following menu options can be used to customize and develop new reminders:

PXRM Reminder Copy,

PXRM Reminder Edit,

PXRM Taxonomy Copy,

PXRM Taxonomy Edit,

PXRM Reminder Test.

The easiest way to create a new reminder is to copy an existing one and then edit it.

Reminders that are distributed with PCE all begin with . These are intended for

national distribution and cannot be edited by a site. When a reminder is copied the

user is prompted for a new unique name. A site cannot use the  prefix in their

reminder names.

**PXRM REMINDER TEST**

Before a new or modified reminder is put into production it should be thoroughly

checked. The Reminder Test option provides a convenient tool that can be used as

an aid in setting up new reminders and tracking down problems with existing ones.

It lets a reminder be run without going through Health Summary.

To get the most out of using this option you should be familiar with setting up a

reminder. This is explained in the Clinical Reminders portions of the PCE User

Manual. Relevant sections include Chapter 10 and Appendix A.

**When this option is executed, it prompts the user for a patient and then a**

**reminder.**

***Sample output:***

Select OPTION NAME: **PXRM REMINDER TEST** Reminder Test

Select Patient: **PCEPATIENT,ONE** 04-01-44 000456789 YES SC VETERAN

Select Reminder: **VA-DIABETIC FOOT EXAM**

The elements of the ^TMP(“PXRM”,$J,”DISC”) array are:

^TMP(“PXRM”,$J,”DISC”,”1”)=The following disease screening, immunization and patient

education^TMP(“PXRM”,$J,”DISC”,”2”)=recommendations are offered as guidelines to

assist in your practice.

^TMP(“PXRM”,$J,”DISC”,”3”)=These are only recommendations, not practice standards.

The^TMP(“PXRM”,$J,”DISC”,”4”)=appropriate utilization of these for your individual

patient must be^TMP(“PXRM”,$J,”DISC”,”5”)=based on clinical judgment and the

patient's current status.

The elements of the ^TMP(“PXRM”,$J,”WA”) array are:

^TMP(“PXRM”,$J,”WA”,”DUE”,”43”,”Diabetic Foot Exam”)=No Diabetic Foot Exam on

record^2970304

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”CODE”)=250.01

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”DATE”)=2960926

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”ICD9IEN”)=851

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”PN”)=DIABETES MELLI W/0 COMP TYP I

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”CODE”)=250.13

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”DATE”)=2960918.09

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”ICD9IEN”)=12830

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”MOD”)=

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”PN”)=DIABETES W/ KETOACIDOSIS,TYPE

I[IDDM][JUVENILE TYPE],UNCONTROLLED

^TMP(“PXRM”,$J,”WA”,”INFO”,”43”,”Diabetic Foot Exam”,”VA-DIABETES\_FOUNDB”)=Complete

foot exam required annually for all diabetic patients.

^TMP(“PXRM”,$J,”WA”,”INFO”,”43”,”Diabetic Foot Exam”,”zFREQARNG”)=Final Frequency

and  used: 1 year for all ages.

^TMP(“PXRM”,$J,”WA”,”LOGIC”)=1^(SEX)&amp;(AGE)&amp;(TF(28))^(1)&amp;(1)&amp;(1)

^TMP(“PXRM”,$J,”WA”,”RANK”,”0”,”365.04”,”0”,”0”)=TFIND^28

The elements of the ^TMP(“PXRHM”,$J) array are:

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”)=DUE NOW^2970304^unknown

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”1”)= Problem Diagnosis:

250.01-DIABETES MELLI W/0 COMP TYP I^TMP(“PXRHM”,$J,”43”,”Diabetic Foot

Exam”,”TXT”,”2”)= Encounter Diagnosis: 250.13-DIABETES W/KETOACID. TYPE I

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”3”)=Complete foot exam required

annually for all diabetic patients.^TMP(“PXRHM”,$J,”43”,”Diabetic Foot

Exam”,”TXT”,”4”)=Final Frequency and  used: 1 year for all ages.

Press RETURN to continue...

The output from this option provides a view of the internal workings of the clinical

reminders software and allows you to see what happened as the reminder was

evaluated. Errors and warnings that are not always seen on the Health Summary

are displayed here. When setting up a reminder, it’s a good idea to have test

patients with known clinical data such as examinations, immunizations, ICDs,

CPTs, etc., that are pertinent to the reminder being developed. Using this option to

run the reminder for test patients allows you to see if the reminder operates as

expected.

Found and Not Found Text can be included in a number of places in the reminder

definition. An example is taxonomies. The Found Text will be displayed if the

taxonomy is found and the Not Found Text will be displayed if the taxonomy is not

found. This text is optional and should only be included if you want something

displayed.

The text should be chosen with care because it can give misleading information

within the total context of the findings. For example, consider a skin test reminder.

The reminders software searches the V Skin Test file and for a coded value if there

is a taxonomy. Confusion could arise if the taxonomy Not Found Text was “No skin

test found” and the reminders found an entry in the V Skin Test File but no match

on the taxonomy. The Health Summary would show the date of the skin test and

the message “No skin test found.” A less confusing Not Found Text would be “No

CPT for skin test found.” You should review your output to make sure that it

makes sense.

**Output Explanations**

An explanation of each piece of the [PXRM REMINDER TEST] output follows. This

explanation assumes that you are familiar with the various elements that comprise

a reminder definition.

**Example 1**

The elements of the ^TMP(“PXRM”,$J,”DISC”) array are: ^TMP(“PXRM”,$J,”DISC”,”1”)=The following disease screening, immunization and patient education^TMP(“PXRM”,$J,”DISC”,”2”)=recommendations are offered as guidelines to assist in your practice. ^TMP(“PXRM”,$J,”DISC”,”3”)=These are only recommendations, not practice standards. The^TMP(“PXRM”,$J,”DISC”,”4”)=appropriate utilization of these for your individual patient must be ^TMP(“PXRM”,$J,”DISC”,”5”)=based on clinical judgment and the patient's current status.

^TMP(“PXRM”,$J,”DISC”) is a formatted array containing the disclaimer that is

displayed at the beginning of the Clinical Maintenance or Clinical Reminders

component of Health Summary.

^TMP(“PXRM”,$J,”WA”) is the working array used by the reminders software to

store data during processing. Examining this array provides detailed information

about what was found or not found during the reminder evaluation. The first three

subscripts “PXRM”,$J,”WA” can be ignored, they just provide a unique storage area

in the computer’s memory. The remaining subscripts do contain useful information.

The entries seen in ^TMP(“PXRM”,$J,”WA”, reflect what was found when the

reminder was evaluated for a specific patient. Therefore the subscripts seen and

the order they appear will vary.

^TMP(“PXRM”,$J,”WA”,”DUE”,”43”,”Diabetic Foot Exam”)=No Diabetic Foot Exam on record^2970304

The “DUE” subscript tells us the reminder is due, 43 is the reminder internal entry

number, and “Diabetic Foot Exam” is the name of the reminder. The text on the

right side of the equal sign tells us that no past diabetic foot exam was found and

the second piece is the date the reminder was run and will appear on the Health

Summary as the date due, i.e., the reminder is due on .

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”CODE”)=250.01

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”DATE”)=2960926

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”ICD9IEN”)=851

^TMP(“PXRM”,$J,”WA”,”ICD9PROB”,”28”,”PN”)=DIABETES MELLI W/0 COMP TYP I

This group of lines tells us that an ICD9 entry was found in the Problem List.

(Other file abbreviations for ICD9 entries are DGPT (Patient Treatment File), and

VPOV (V Purpose of Visit File)). The taxonomy containing this code was number

28. The ICD9 code is 250.01, the date in FileMan format is 2960926, the ICD9

internal entry is 851 and the provider narrative is “DIABETES MELLI W/O COMP

TYP I”.

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”CODE”)=250.13

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”DATE”)=2960918.09

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”ICD9IEN”)=12830

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”MOD”)=

^TMP(“PXRM”,$J,”WA”,”ICD9VPOV”,”28”,”PN”)=DIABETES W/ KETOACIDOSIS,TYPE

I[IDDM][JUVENILE TYPE],UNCONTROLLED

This group of lines tells us that an ICD9 entry was found in the V Purpose of Visit

file. The other entries are the same as in the previous group.

^TMP(“PXRM”,$J,”WA”,”INFO”,”43”,”Diabetic Foot Exam”,”VA-DIABETES\_FOUNDB”)=Complete foot exam required annually for all diabetic patients.

This is the Found Text array as defined in the reminder. In this case the Found Text comes from taxonomy 28, “VA-DIABETES”.

^TMP(“PXRM”,$J,”WA”,”INFO”,”43”,”Diabetic Foot Exam”,”zFREQARNG”)=Final Frequency and Age Range used: 1 year for all ages.

This line tells us the final frequency and age range used in the date due calculation.

^TMP(“PXRM”,$J,”WA”,”LOGIC”)=1^(SEX)&amp;(AGE)&amp;(TF(28))^(1)&amp;(1)&amp;(1)

This line is one of the most important in the output. It gives all the information

concerning the APPLY LOGIC. There are three pieces separated by ^. The second

piece is the APPLY LOGIC string used to determine if the reminder should be

given. In order for the reminder to be given, SEX, AGE, and taxonomy finding 28,

TF(28), all have to be true. In this case, the taxonomy finding was true because one

of the codes in the taxonomy was found in the patient’s clinical data. The third

piece shows us the outcome of the finding evaluation; in this example they are all

true. (True is represented by 1 and false by 0.) The first piece is the logical

evaluation of the third piece. In this case, the APPLY LOGIC evaluates to true, so

the reminder will be given. When the APPLY LOGIC evaluates to false, the

reminder is Not Applicable, N/A.

^TMP(“PXRM”,$J,”WA”,”RANK”,”0”,”365.04”,”0”,”0”)=TFIND^28

This line gives information about the ranking process used to determine the final

frequency age range set. The subscript immediately following “RANK” is the rank

value. When no rank value has been defined in the reminder, the value will be “0”.

For this example, there is no “rank” so we determine the frequency age range set to

use based on the frequency which causes the reminder to be given the most often.

The “365.04” is the conversion of the final frequency, one year (1Y) to days. The

smallest value of frequency in days is the one that will cause the reminder to be

given most often. The two subscripts following the frequency correspond to

minimum age and maximum age. A value of “0” for these subscripts has special

significance -- it means that there is no minimum or no maximum age. The value on

the right side of the equal sign indicates that this frequency came from a taxonomy

finding (TFIND) and the internal entry number of the taxonomy was 28.

The elements of the ^TMP(“PXRHM”,$J) array are:

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”)=DUE NOW^2970304^unknown

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”1”)=9/26/96 Problem Diagnosis: 250.01-DIABETES MELLI W/0 COMP TYP I^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”2”)=9/18/96 Encounter Diagnosis: 250.13-DIABETES W/KETOACID. TYPE I

^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”3”)=Complete foot exam required annually for all diabetic patients.^TMP(“PXRHM”,$J,”43”,”Diabetic Foot Exam”,”TXT”,”4”)=Final Frequency and Age Range used: 1 year for all ages.

The ^TMP(“PXRHM”,$J) array is the final information that is passed to Health

Summary for display. The output in the Health Summary will reformat the date

into an external format, display it, and then display the text lines.

**Example 2**

Select Patient: **PCEPATIENT,ONE** 000456789 YES SC

VETERAN

Select Reminder: **VA-MAMMOGRAM**

This is our input to the option.

The elements of the ^TMP(“PXRM”,$J,”DISC”) array are:

^TMP(“PXRM”,$J,”DISC”,”1”)=The following disease screening, immunization and patient education ^TMP(“PXRM”,$J,”DISC”,”2”)=recommendations are offered as guidelines to assist in your practice. ^TMP(“PXRM”,$J,”DISC”,”3”)=These are only recommendations, not practice standards. The ^TMP(“PXRM”,$J,”DISC”,”4”)= appropriate utilization of these for your individual patient must be ^TMP(“PXRM”,$J,”DISC”,”5”)=based on clinical judgment and the patient's current status.

This is the reminder disclaimer.

The elements of the ^TMP(“PXRM”,$J,”WA”) array are:

^TMP(“PXRM”,$J,”WA”,”AF\_FNF”,”2”)=AF 2 FOUND

The “AF\_FNF” subscript corresponds to Age Finding Found Not Found information.

There was a match between the patient’s age and Baseline Age Finding number 2.

^TMP(“PXRM”,$J,”WA”,”HF”,”43”,”DATE”)=2960429

^TMP(“PXRM”,$J,”WA”,”HF”,”43”,”FREQ”)=

^TMP(“PXRM”,$J,”WA”,”HF”,”43”,”MAXAGE”)=

^TMP(“PXRM”,$J,”WA”,”HF”,”43”,”MINAGE”)=

This group of lines provides Health Factor information. The Health Factor with

internal entry number 43 was found and the date was 2960429. There was no

frequency or age range associated with this Health Factor.

^TMP(“PXRM”,$J,”WA”,”ICPT”,”16”,”CODE”)=76092

^TMP(“PXRM”,$J,”WA”,”ICPT”,”16”,”DATE”)=2970221.142333

^TMP(“PXRM”,$J,”WA”,”ICPT”,”16”,”ICPTIEN”)=76092

^TMP(“PXRM”,$J,”WA”,”ICPT”,”16”,”PN”)=MAMM0GRAM, SCREENING

^TMP(“PXRM”,$J,”WA”,”ICPT”,”16”,”SNAME”)=MAMM0GRAM, SCREENING

This group of lines tells us that CPT information was found. The CPT code was

76092 and it came from taxonomy 16. The date was 2970221, the CPT file internal

entry number was 76092, the provider narrative from the V CPT file was

“MAMMOGRAM, SCREENING,” and the CPT short name from the CPT file was

“MAMMOGRAM, SCREENING.”

^TMP(“PXRM”,$J,”WA”,”INFO”,”19”,”Mammogram”,”AF 2 FOUNDB”)=Women ages 50-69 should receive a mammogram every two years.

This is Found Text for the Age Finding 2 defined in the reminder.

^TMP(“PXRM”,$J,”WA”,”INFO”,”19”,”Mammogram”,”HFC1”)=Health Factor comments:  Activate health factor comments

This is a Health Factor comment from the patient’ s V Health Factor findings.

^TMP(“PXRM”,$J,”WA”,”INFO”,”19”,”Mammogram”,”VA-BREAST TUMOR NOT\_FOUNDB”)=No history of breast cancer/tumor on file.

This is Not Found Text for taxonomy 19.

^TMP(“PXRM”,$J,”WA”,”INFO”,”19”,”Mammogram”,”WARNING”,”TAX”)=Taxonomy 18 entry V10.3^V10.3 does not have a source file, assuming file 80.

This is warning information and it will not be displayed on the Health Summary.

The text is self-explanatory once you remember that a taxonomy entry requires a

low coded value, a high coded value, and a source file.

This entry in taxonomy 18 has a low coded value of V10.3, a high coded value of

V10.3 and the source file is missing. To process the reminder a source file is

required. In order to continue, the reminder’s logic assumes that it is file 80, the

ICD diagnosis file. If you really wanted the CPT or ICD operation/procedures file

then you should change the taxonomy.

**Some other warnings you might see:**

“Warning no reminder frequency, cannot calculate date due!”

This means the reminders software was not able to establish a frequency. Most

likely, it was left out of the Baseline Age Findings.

“Warning no do in advance time”

There was no do in advance time in the reminder definition, the reminders software

will use 0 in the date due calculation.

^TMP(“PXRM”,$J,”WA”,”INFO”,”19”,”Mammogram”,”zFREQARNG”)=Final Frequency and Age Range used: 2 years for ages 50 to 69.

This is the final frequency and age range information used in the date due

calculation. This comes from the rank and frequency evaluation discussed above.

^TMP(“PXRM”,$J,”WA”,”LOGIC”)=1^(SEX)&amp;(AGE)&amp;'(HF(42))^(1)&amp;(1)&amp;'(0)

This is the APPLY LOGIC string and provides an example of how the INACTIVATE Health Factors work. The INACTIVATE Health Factor for this reminder is HF(42) so the logical operator is &amp;’. We can see this reminder has not been inactivated for this patient because HF(42) is false. SEX and AGE are true, so the entire APPLY LOGIC string evaluates to true; therefore the reminder will be given.

^TMP(“PXRM”,$J,”WA”,”NOTDUE”,”19”,”Mammogram”)=Mammogram due on^2990221.142333^2970221.142333

This tells that the reminder is not due. It is due on 2990221 and was last given on

2970221.

^TMP(“PXRM”,$J,”WA”,”RAD”,”436”,”CPT”)=76091

^TMP(“PXRM”,$J,”WA”,”RAD”,”436”,”DATE”)=2960826

^TMP(“PXRM”,$J,”WA”,”RAD”,”436”,”NAME”)=MAMMOGRAM BILAT

^TMP(“PXRM”,$J,”WA”,”RAD”,”436”,”SNAME”)=MAMMOGRAM, BOTH BREASTS

These lines tell us that radiology information was found. The number 436 is the

radiology procedure pointer. The CPT code is 76091, the date of the procedure is

2960826, the name of the radiology procedure is “MAMMOGRAM BILAT,” and the

CPT short name is “MAMMOGRAM, BOTH BREASTS.”

^TMP(“PXRM”,$J,”WA”,”RDATE”,”2970221.142333”)=TFDATE^16

This line tells that the date used in the date due calculation was 2970221 and that

it came from a taxonomy finding for taxonomy number 16. Notice that this date is

more recent than the date of the radiology procedure. This is an example of how

the Use in Date Due Calc field works.

The elements of the ^TMP(“PXRHM”,$J) array are:

^TMP(“PXRHM”,$J,”19”,”Mammogram”)=^2990221.142333^2970221.142333

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”1”)= Health Factor: ACTIVATE BREAST CANCER SCREEN

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”2”)= Encounter Procedure: 76092-MAMM0GRAM, SCREENING

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”3”)=Women ages 50-69 should receive

a mammogram every two years.

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”4”)=Health Factor comments: Activate health factor comments

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”5”)=No history of breast cancer/tumor on file. ^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”6”)=Final Frequency and  used: 2 years for ages 50 to 69. ^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”7”)=

Radiology Procedure: 76091-MAMMOGRAM, BOTH BREASTS; MAMMOGRAM

^TMP(“PXRHM”,$J,”19”,”Mammogram”,”TXT”,”8”)=BILAT

Finally, this is the information as it is returned to Health Summary.

### Appendix A-8   Distributed Reminder Definitions

***BREAST CANCER SCREEN**

**-----------------------------------**

Reminder Type:	PROCEDURE

Print Name:	Breast Cancer Screen

Related * Reminder:	*BREAST CANCER SCREEN

Reminder Description:

Mammogram should be given every 2 years to female patients, ages 50-69.

The "*Breast Cancer Screen" reminder is based on the following "Breast

Cancer Detection" guidelines specified in the VHA HANDBOOK 1101.8,

APPENDIX A.

Target Condition: Early detection of breast cancer.

Target Group:     All women ages 50-69.

Recommendation:   All women ages 50-69 should receive a mammogram

every two years.

Goals for FY2000: At least 60% of women ages 50-69 have received a

mammogram within the preceding two years.

Technical Description:

The findings for mammogram screening are based on defining CPT codes and

V-codes from the ICD Diagnosis file that represent mammograms and

mammogram screening in a taxonomy for Mammogram/Screen. The CPT codes

are used to search the Radiology procedures in the Radiology package, as

well as checks for existence of a CPT code in the V CPT file. The

V-codes are used to search the Problem List, V POV (problems of visits),

and Inpatient Diagnosis PTF files.

The reminder will be "DUE NOW" until a procedure or diagnosis (V-code) is

documented to reflect a mammogram/screening done at a current encounter

or a historical encounter within the past two years.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific: FEMALE

Ignore on N/A: S

Frequency for : 2 years for ages 50 to 69

Match Text: All women ages 50-69 should receive a mammogram

every two years.

No Match Text:

Targeted Result Findings for PROCEDURE reminder type:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-MAMMOGRAM/SCREEN (TF(16))

Match freq/age: 2 years for ages 50 to 69

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text: History of mammogram/screen on file.

No Match Text: Date of last mammogram/screen unknown.

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE BREAST CANCER SCREEN (HF(42))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE BREAST CANCER SCREEN (HF(43))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(42))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE BREAST CANCER SCREEN))

***CERVICAL CANCER SCREEN**

**-----------------------------------**

Reminder Type:	PROCEDURE

Print Name:	Pap Smear

Related * Reminder:	*CERVICAL CANCER SCREEN

Reminder Description:

This reminder is based on the "Cervical Cancer Detection" guidelines

specified in the VHA HANDBOOK 1101.8, APPENDIX A.

Target Condition: Early detection of cervical cancer.

Target Group: Women age 65 and under.

Recommendation: Papanicolaou (Pap) smear testing is recommended for

all sexually active women every three years until age 65. Pap testing

may be discontinued after age 65 if previous smears have been consistently normal.

Goal for FY 2000: 95% of women have received at least one Pap test in

their lifetime and 85% of women age 65 and under received one in the

past three years.

Technical Description:

Copy the reminder to a new reminder for your local site modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Wait until actually DUE

Sex Specific: FEMALE

Ignore on N/A: S

Frequency for : 3 years for ages 65 and younger

Match Text: Women ages 65 and younger should receive a

cervical cancer screen every 3 years.

No Match Text: Pap smear screen not indicated for women over 65.

Targeted Result Findings for PROCEDURE reminder type:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-CERVICAL CANCER SCREEN (TF(30))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text: No record of cervical cancer screen taxonomy on

file

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE CERVIX CANCER SCREEN (HF(44))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE CERVIX CANCER SCREEN (HF(47))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(44))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE CERVIX CANCER SCREEN))

***CHOLESTEROL SCREEN (F)**

**-----------------------------------**

Reminder Type:	LABORATORY TEST

Print Name:	Cholesterol Screen (Female)

Related *	Reminder: *CHOLESTEROL SCREEN (F)

Reminder Description:

This Cholesterol screen reminder for females is based on the following

"Hyperlipidemia Detection" guidelines specified in the "VHA HANDBOOK

1101.8, APPENDIX A.

Target Conditions: Cardiovascular Disease.

Target Group: Females 45-65.

Recommendation: Check total cholesterol level within the past

five years.

Goal for FY 2000: 75% of females ages 45-65 Primary Care clinic

patients have had a blood cholesterol level check within the past

five years.

Technical Description:

As distributed, this reminder is based on CPT codes which represent

cholesterol tests the patient has had documented in PCE. These may be

CPT codes for cholesterol done by the Laboratory Service, or a historical

encounter documented to show when the cholesterol test was last given to

the patient.

Copy this reminder to a new reminder for your site. Add the Laboratory

Tests that represent a cholesterol level check in the Result Findings

multiple.

PLEASE NOTE: Your local version of this reminder will include the search

based on the local ancillary Lab package results, it is possible that 5

years’ worth of patient lab history are not on record.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific: FEMALE

Ignore on N/A: S

Frequency for : 5 years for ages 45 to 65

Match Text: Check total cholesterol every 5 years for women

ages 45-65.

No Match Text: Cholesterol not indicated for women under 45,

or over 65.

Targeted Result Findings for LABORATORY TEST reminder type:

LABORATORY TEST

Target Result Match Text:

No Match Text LAB: Date of last cholesterol test unknown.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-CHOLESTEROL (TF(24))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE CHOLESTEROL SCREEN (HF(48))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE CHOLESTEROL SCREEN (HF(46))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(48))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE CHOLESTEROL SCREEN))

***CHOLESTEROL SCREEN (M)**

**-----------------------------------**

Reminder Type:	LABORATORY TEST

Print Name:	Cholesterol Screen (Male)

Related * Reminder:	*CHOLESTEROL SCREEN (M)

Reminder Description:

This Cholesterol screen reminder for males is based on the following

"Hyperlipidemia Detection" guidelines specified in the VHA HANDBOOK

1101.8, APPENDIX A.

Target Conditions: Cardiovascular Disease.

Target Group: Males ages 35-65.

Recommendation: Check total cholesterol level within the past

five years.

Goal for FY 2000: 75% of males ages 35-65 Primary Care clinic patients have had a blood cholesterol level check within the past five years.

Technical Description:

As distributed, this reminder is based on CPT codes which represent

cholesterol tests the patient has had documented in PCE. These may be

CPT codes for cholesterol done by the Laboratory Service, or a historical

encounter documented to show when the cholesterol test was last given to

the patient.

Copy this reminder to a new reminder for your site. Add the Laboratory

Tests that represent a cholesterol level check in the Result Findings

multiple.

PLEASE NOTE: Your local version of this reminder will include the search based on the local ancillary Lab package results, it is possible that 5 years’ worth of patient lab history are not on record.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific: MALE

Ignore on N/A: S

Frequency for : 5 years for ages 35 to 65

Match Text: Check total cholesterol every 5 years for men

ages 35-65.

No Match Text:

Targeted Result Findings for LABORATORY TEST reminder type:

LABORATORY TEST

Target Result Match Text:

No Match Text: LAB: Date of last cholesterol test unknown.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-CHOLESTEROL (TF(24))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE CHOLESTEROL SCREEN (HF(48))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE CHOLESTEROL SCREEN (HF(46))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(48))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE CHOLESTEROL SCREEN))

***COLORECTAL CANCER SCREEN (FOBT)**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Fecal Occult Blood Test

Related * Reminder:	*COLORECTAL CANCER SCREEN (FOBT)

Reminder Description:

Fecal occult blood test due every year for patients ages 50 and older, or

5 years after the last Sigmoidoscopy. The 5 years is a conservative

period recommended by a blue ribbon panel publishing their findings in

the February 1997 issue of "Gastroenterology" magazine.

This *COLORECTAL CANCER SCREEN - FOBT reminder is based on the

"Colorectal Cancer Detection" guidelines specified in the VHA HANDBOOK

1101.8, APPENDIX A.

Target Condition: Early detection of colon cancer or its predecessors.

Target Group: All persons ages 50 and older.

Recommendation: All persons age 50 and older should receive an annual

fecal occult blood test or undergo a sigmoidoscopy examination

(periodicity unspecified).

Goals for FY 2000: For persons age 50 and older: 50 percent of those

enrolled in primary care clinics have received fecal occult blood

testing within the preceding year and 40 percent have received at

least one proctosigmoidoscopy examination in their lifetime.

Technical Description:

This reminder is based on Taxonomy Findings from FOBT, "or" SIG cancer

screening, "and" FOBT exam results recorded from a clinic encounter as an

EXAM. See the definition for *COLORECTAL CANCER SCREEN (SIG.) also.

These two reminders work together for assessing cancer screening.

The FOBT is due annually, unless a SIG is found. The SIG found changes

the frequency to due once in a lifetime (99Y) according to the M-2

document, but a more conservative approach is encouraged by the National

Center for Health Promotion to use 5 years (5Y). The SIG found changes

the frequency to due every 5 years for patients 50 and older (note the

rank of 2). After a SIG has been received by the patient, if the

clinician determines the FOBT should be given to this patient again

annually, the FOBT can be activated again by entering the Health Factor

"ACTIVATE FOBT CANCER SCREEN" for the patient (Note the rank of 1).

Check the Taxonomy Findings entries representing Fecal Occult Blood Test

and VA-FLEXISIGMOIDOSCOPY. The taxonomies represent coded standard

entries in the CPT file and ICD Operation/Procedure file. If one of

these taxonomies need modification, copy the taxonomy to a new taxonomy

for your site, and make the appropriate modifications. THAN, copy the

reminder to a new reminder to add your local sites modifications.

This reminder cannot make use of the Laboratory package data at this time

because the Occult Blood results are Microbiology tests that do not

reflect the Laboratory Test done, or the related CPT code.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for ages 50 and older

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

FOBT(CLINIC)

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-FOBT (TF(27))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-FLEXISIGMOIDOSCOPY (TF(15))

Match freq/age: 5 years for ages 50 and older

Rank Frequency: 2

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text: FOBT due 5 years after the last sigmoidoscopy.

No Match Text:

Taxonomy: VA-COLORECTAL CANCER SCREEN (TF(31))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text: Date of last FOBT or SIG, unknown.

2 Health Factor Findings:

Health Factor: INACTIVATE FOBT CANCER SCREEN (HF(49))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE FOBT CANCER SCREEN (HF(50))

Match Freq/Age: 1 year for ages 50 and older

Rank Frequency: 1

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(49))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE FOBT CANCER SCREEN))

***COLORECTAL CANCER SCREEN (SIG.)**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Flexisigmoidoscopy

Related * Reminder:	*COLORECTAL CANCER SCREEN (SIG.)

Reminder Description:

At least one sigmoidoscopy examination in their lifetime for patients age

50 and older, or a fecal occult blood test yearly. This reminder uses 5

years, rather than 99Y for "ONCE" as originally published in the VA

Guidelines. The 5 years is a conservative period recommended by a blue

ribbon panel publishing their findings in the February 1997 issue of

"Gastroenterology" magazine.

This reminder is based on the "Colorectal Cancer Detection" guidelines

specified in the VHA HANDBOOK, APPENDIX A.

Target Condition: Early detection of colon cancer or its predecessors.

Target Group: All persons ages 50 and older.

Recommendation: All persons age 50 and older should receive an annual

fecal occult blood test or undergo a sigmoidoscopy examination

(periodicity unspecified).

Goals for FY 2000: For persons age 50 and older, 50 percent of those

enrolled in primary care clinics have received fecal occult blood

testing within the preceding year and 40 percent have received at

least one proctosigmoidoscopy examination in their lifetime.

Technical Description:

The next time a SIG is due is 1 year from the last FOBT, or 5 years from

the last SIG.

The reminder type is EXAM, and the  and FREQUENCY is 50 and older and 1Y - so that the SIG will be due a year from the last FOBT done in the clinic. The  and FREQUENCY are modified to 50 and older and 5Y if a prior SIG has been received by the patient. The Rank of 2, on the VA-FLEXISIGMOIDOSCOPY taxonomy match fields, will cause a match of a SIG to take precedence over the FOBT findings to establish when the SIG is due again. If the most recent health factor finding, between INACTIVATE and ACTIVATE is INACTIVATE with its rank of 1, the reminder will be "N/A" (not applicable to the patient), and the frequency is 0Y.

Check the Taxonomy Findings entries representing flexisigmoidoscopy and

FOBT procedures. This represents coded standard entries in the CPT file

and ICD Operation/Procedure file. If the taxonomies need modification,

copy the taxonomy to a new taxonomy for your site, and make the

appropriate modifications. Then, copy this reminder to a new reminder

for your local sites modifications, and change the Taxonomy Findings to

use the new taxonomies.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for ages 50 and older

Match Text: SIG due every 5 years for patients 50 and

older, or FOBT annually.

No Match Text: Flexisigmoidoscopy not indicted for patients

under 50.

Targeted Result Findings for EXAMINATION reminder type:

EXAM

FOBT(CLINIC)

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-FLEXISIGMOIDOSCOPY (TF(15))

Match freq/age: 5 years for ages 50 and older

Rank Frequency: 2

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-FOBT (TF(27))

Match freq/age: 1 year for ages 50 and older

Rank Frequency: 3

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-COLORECTAL CANCER SCREEN (TF(31))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text: Date of last SIG or FOBT unknown.

2 Health Factor Findings:

Health Factor: INACTIVATE SIGMOIDOSCOPY (HF(51))

Match Freq/Age: 0Y - Not Indicated for ages 50 and older

Rank Frequency: 1

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE SIGMOIDOSCOPY (HF(52))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(51))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE SIGMOIDOSCOPY))

***FITNESS AND EXERCISE SCREEN**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Exercise Education

Related *	Reminder: *FITNESS AND EXERCISE SCREEN

Reminder Description:

Exercise education given yearly to all patients.

This *FITNESS AND EXERCISE SCREEN reminder is based on the following

"Physical Activity Counseling" guidelines specified in the VHA HANDBOOK

1101.8, APPENDIX A.

Target Conditions: Cardiovascular disease, physical function.

Target Group: General outpatient population.

Recommendation: Primary care clinicians should encourage all

individuals to engage in a program of physical activity tailored to

their health status and personal life style.

Goals for FY 2000: 50% of primary care providers routinely counsel

their patients regarding frequency, duration, type and intensity of

physical activity. 30% of Veterans engage in regular moderate

physical activity for at least 30 minutes three times a week.

20% of Veterans engage in vigorous activity that promotes

cardiorespiratory fitness.

Technical Description:

To modify this reminder from its distributed definition, copy the

reminder to a new reminder and then make the modifications necessary to

define your sites guideline.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text:

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-EXERCISE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-EXERCISE COUNSELING (TF(32))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE EXERCISE SCREEN (HF(53))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE EXERCISE SCREEN (HF(54))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(53))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE EXERCISE SCREEN))

***HYPERTENSION SCREEN**

**-----------------------------------**

Reminder Type:	MEASUREMENT

Print Name:	Hypertension Detection

Related * Reminder:	*HYPERTENSION SCREEN

Reminder Description:

BP due every two years to detect hypertension.

This *HYPERTENSION SCREEN reminder is defined based on the following

"Hypertension Detection" guidelines specified in the VHA HANDBOOK 1101.8,

APPENDIX A.

Target Condition: Hypertension, Cardiovascular Disease

Target Group: General outpatient population

Recommendation: Check blood pressure at least once every two years

for all Primary Care clinic patients.

Goal for FY2000: 90% of Primary Care clinic patients have had their

blood pressure checked in the past two years.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has received a blood pressure check. As distributed, the reminder checks

for an ICD Diagnosis or a CPT procedure code representing "Hypertension

Screen", or a record of a blood pressure (BP) in the Vitals/Measurements

package.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-BLOOD PRESSURE CHECK" reminder. This reminder

includes an alteration of the blood pressure reminder guidelines when the

patient has a history of hypertension on file.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific:

Ignore on N/A:

Frequency for : 2 years for all ages

Match Text:

No Match Text:

Targeted Result Findings for MEASUREMENT reminder type:

GMRV VITAL TYPE

BLOOD PRESSURE

Target Result Match Text:

No Match Text: Vitals: Date of last Vitals BP Measurement

unknown.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HYPERTENSION SCREEN (TF(23))

Match freq/age: 2 years for all ages

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text: Date of last ICD or CPT coded hypertension

screen unknown.

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

***INFLUENZA IMMUNIZATION**

**-----------------------------------**

Reminder Type:	IMMUNIZATION

Print Name:	Influenza Immunization

Related * Reminder:	*INFLUENZA IMMUNIZATION

Reminder Description:

The "*Influenza Immunization" reminder is based on the following

"Influenza Immunization" guidelines specified in the VHA HANDBOOK 1101.8,

APPENDIX A.

Target Condition: Influenza and its complications.

Target Group: Outpatients age 65 and older.

Recommendation: Influenza vaccine should be administered annually in

the late fall to all persons age 65 and older.

Goal for FY 2000: 60% of those persons over age 65 have received

influenza vaccine in the past year.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has received an influenza immunization. As distributed, the reminder

checks for an "Influenza" immunization in the V Immunization file or its

CPT code equivalent in the V CPT file.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-INFLUENZA VACCINE" reminder. This reminder

includes an alteration of the influenza reminder guidelines when the

patient has a diagnosis which could cause the patient to be at a high

risk for flu or pneumonia.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for ages 65 and older

Match Text: Influenza vaccine due yearly in patients ages

65 and older.

No Match Text: Influenza vaccine not indicated for patients

under 65.

Targeted Result Findings for IMMUNIZATION reminder type:

IMMUNIZATION

INFLUENZA

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-INFLUENZA IMMUNIZATION (TF(33))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE INFLUENZA IMMUNIZATION (HF(55))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE INFLUENZA IMMUNIZATION (HF(56))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(55))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE INFLUENZA IMMUNIZATION))

***PNEUMOCOCCAL VACCINE**

**-----------------------------------**

Reminder Type:	IMMUNIZATION

Print Name:	Pneumovax

Related * Reminder:	*PNEUMOCOCCAL VACCINE

Reminder Description:

This "*PNEUMOCOCCAL VACCINE" reminder is defined based on the

following "Pneumococcal Vaccine" guidelines specified in the VHA HANDBOOK

1101.8, APPENDIX A.

Target Condition: Pneumococcal pneumonia.

Target Group: Outpatients age 65 and older.

Recommendation: All persons age 65 and older should receive one

vaccination with pneumococcal vaccine in their lifetime.

Goal for FY 2000: 80% of individuals 65 and older have received

pneumococcal vaccine.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the

pneumococcal vaccine has been given to the patient.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-PNEUMOVAX" reminder, which includes a check for

diagnoses documented for the patient that would indicate the pneumococcal

vaccine should be given to the patient regardless of the patients age.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific:

Ignore on N/A:

Frequency for : 99Y - Once for ages 65 and older

Match Text: Pneumovax due once for patients 65 and over.

No Match Text:

Targeted Result Findings for IMMUNIZATION reminder type:

IMMUNIZATION

PNEUMOCOCCAL

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-PNEUMOCOCCAL VACCINE (TF(25))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE PNEUMOCOCCAL VACCINE (HF(57))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE PNEUMOCOCCAL VACCINE (HF(58))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(57))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE PNEUMOCOCCAL VACCINE))

***PROBLEM DRINKING SCREEN**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Problem Drinking Screen

Related * Reminder:	*PROBLEM DRINKING SCREEN

Reminder Description:

The "*Problem Drinking Screening" education reminder is based on the

following "Problem Drinking and Alcohol Moderation Counseling" guidelines

specified in the VHA HANDBOOK 1101.8, APPENDIX A.

Target Conditions: Problem drinking, alcohol dependence, medical

complications of alcohol use, accidents and violence.

Target Group: Outpatient experiencing medical or social problems

attributable to alcohol use.

Recommendation: Primary care clinicians should routinely ask their

patients to describe their use of alcohol. High risk patients (3 or more drinks daily) should be referred for counseling.

Goals for FY 2000: 100% of VHA facilities have an alcohol treatment

program or access to one. 75% of primary care providers should screen for alcohol problems yearly and provide counseling and referral as needed.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has been screened for problem drinking. The "VA-ALCOHOL ABUSE SCREENING"

education topic is the result finding that will satisfy this reminder.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-ALCOHOL ABUSE EDUCATION" reminder. This reminder

includes a check for a diagnoses documented for the patient that would

indicate the patient has a problem related to alcohol abuse. It also

references all of the alcohol abuse education topics that are distributed

by PCE, which could satisfy the reminder.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Screen for alcohol problems yearly for all

patients.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-ALCOHOL ABUSE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-ALCOHOLISM SCREENING (TF(34))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE PROBLEM DRINKING SCREEN (HF(59))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE PROBLEM DRINKING SCREEN (HF(60))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(59))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE PROBLEM DRINKING SCREEN))

***SEATBELT AND ACCIDENT SCREEN**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Seatbelt and Accident Screen

Related * Reminder:	*SEATBELT AND ACCIDENT SCREEN

Reminder Description:

Seatbelt and accident education given yearly to all patients.

This "*SEATBELT AND ACCIDENT SCREEN" reminder is based on the

"Seatbelt Use and Accident Avoidance Counseling" guideline specified in

the VHA HANDBOOK 1101.8, APPENDIX A.

Target Condition: Motor vehicle associated injuries.

Target Group: General Outpatient population.

Recommendation: All patients should be urged to use seatbelts in

automobiles, wear helmets when riding bicycles or motorcycles, and to

refrain from driving after drinking.

Goal for FY 2000: 85% of Veterans report regular use of seatbelts in

automobiles. 80% of motorcyclists and 50% of bicyclists report use of

helmets. 50% of primary care providers routinely provide

age-appropriate counseling on safety precautions to prevent

unintentional injury.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has had seatbelt and accident screening. The "VA-SEAT BELT USE

SCREENING" education topic is the result finding that will satisfy this

reminder.

The Ambulatory Care EP recommends a variation on this reminder,

represented in the "VA-SEATBELT EDUCATION" reminder. This reminder

includes a check for seatbelt use education given to the patient, in

addition to the screening.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Seatbelt education due yearly for all patients.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-SEAT BELT USE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-SAFETY COUNSELING (TF(35))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE SEATBELT SCREEN (HF(61))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE SEATBELT SCREEN (HF(62))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(61))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE SEATBELT SCREEN))

***TETANUS DIPHTHERIA IMMUNIZATION**

**-----------------------------------**

Reminder Type:	IMMUNIZATION

Print Name:	Tetanus Diphtheria (TD-Adult)

Related * Reminder:	*TETANUS DIPHTHERIA IMMUNIZATION

Reminder Description:

TD booster given to all adult patients every ten years.

This reminder is based on "Tetanus and Diphtheria Immunization"

guidelines specified in VHA HANDBOOK 1101.8, APPENDIX A.

Target Condition: Infection with tetanus and diphtheria.

Target Group: General outpatient population.

Recommendation: A tetanus and diphtheria (TD) toxoid booster should be

administered every ten years throughout adult life. This is commonly

offered at each half decade (e.g. ages 45,55,65).

Goal for FY 2000: 50% of individuals have received a tetanus immunization booster in the past ten years.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has been screened for tetanus diphtheria immunization. The "TETANUS

DIPHTHERIA (TD-ADULT)" and "TETANUS TOXOID" immunizations or their CPT

equivalent are the result finding that will satisfy this reminder.

The Ambulatory Care EP endorses this reminder as it is defined.

If any modifications to the reminder definition are needed, copy the

reminder to a new reminder for your site's use, and make the appropriate

modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 6 months

Sex Specific:

Ignore on N/A:

Frequency for : 10 years for ages 18 and older

Match Text: TD booster due every ten years throughout

adult life.

No Match Text:

Targeted Result Findings for IMMUNIZATION reminder type:

IMMUNIZATION

TETANUS DIPTHERIA (TD-ADULT)

TETANUS TOXOID

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-TETANUS DIPHTHERIA (TF(29))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE TD IMMUNIZATION (HF(63))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE TD IMMUNIZATION (HF(64))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(63))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE TD IMMUNIZATION))

***TOBACCO USE SCREEN**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Tobacco Use Screen

Related * Reminder:	*TOBACCO USE SCREEN

Reminder Description:

This reminder is based on "Tobacco Use Counseling" guidelines specified

in the VHA HANDBOOK 1101.8, APPENDIX A.

Target Conditions: Cancer, pulmonary and cardiovascular disease.

Target Group: Outpatients who use tobacco.

Recommendation: Tobacco use cessation counseling should be offered

annually to all who use tobacco on a regular basis.

Goals for FY 2000: 100% of VHA facilities have an intensive smoking

cessation program (or access to one) which includes appropriate

pharmacological treatment. 75% of primary care providers routinely

advise cessation and provide assistance and follow-up for all their

patients who use tobacco. Reduce cigarette smoking to a prevalence

of no more than 15% among people age 20 and over.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has received a tobacco use screen. The "VA-TOBACCO USE SCREENING"

education topic is the result finding that will satisfy this reminder.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-TOBACCO EDUCATION" reminder. This reminder

includes a check for smoking cessation education, in addition to the

screening. It also includes target conditions for patients who have

tobacco related diagnoses or health factors on file.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Tobacco use screen due yearly for all ages.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-TOBACCO USE SCREENING

Target Result Match Text:

No Match Text: No history of tobacco use screen on file.

Please evaluate tobacco use and educate if

currently in use.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE TOBACCO USE SCREEN (HF(65))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE TOBACCO USE SCREEN (HF(66))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(65))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE TOBACCO USE SCREEN))

***WEIGHT AND NUTRITION SCREEN**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Weight and Nutrition Screen

Related * Reminder:	*WEIGHT AND NUTRITION SCREEN

Reminder Description:

This *WEIGHT AND NUTRITION SCREEN reminder is based on the following

"Weight Control and Nutrition Counseling" guidelines defined in the VHA

HANDBOOK 1101.8, APPENDIX A.

Target condition: Obesity and associated conditions.

Target Group: General outpatient population.

Recommendation: Primary care clinicians should provide their patients

with periodic counseling or referral for counseling regarding dietary

intake of calories, fat (especially saturated fat), cholesterol, and

fiber. A nutrition counseling service should be available at each VHA

facility.

Goals for FY 2000: Reduce dietary fat intake to an average of 30 of

calories and saturated fats to less than 10%. Increase complex

carbohydrate and fiber-containing foods in the diet to 5 or more

daily servings for vegetables and fruits and 6 or more daily servings for grain products. Reduce overweight to a prevalence of no more than 20% among people age 20 and older. Women should be encouraged to consume

1000 mg/day of calcium until menopause and 1500 mg/day thereafter.

100% of VHA facilities should have formal nutrition counseling

available for outpatients.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient

has received a weight and nutrition screen. The "VA-NUTRITION/WEIGHT

SCREENING" education topic is the result finding that will satisfy this

reminder.

The Ambulatory Care EP recommends a variation on this reminder

represented in the "VA-NUTRITION/OBESITY EDUCATION" reminder. This

reminder includes a check for nutrition education, in addition to the

screening. It also includes target conditions for patients who have

nutrition or obesity related diagnoses or health factors on file.

Please review both of these reminder definitions, choose one of them to

use. If local modifications need to be made, copy the preferred reminder

to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Weight and Nutrition screen due yearly for all

patients.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-NUTRITION/WEIGHT SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-WEIGHT AND NUTRITION SCREEN (TF(36))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE WEIGHT/NUTRITION SCREEN (HF(67))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE WEIGHT/NUTRITION SCREEN (HF(68))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(67))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE WEIGHT/NUTRITION SCREEN))

**VA-ADVANCED DIRECTIVES EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Advanced Directives Education

Related * Reminder:

Reminder Description:

Advanced directives information given to all patients once.

Technical Description:

This reminder is distributed with the PCE package. The source of this

reminder definition is the Ambulatory Care Expert Panel. It is based on

feedback from facilities wanting to track Advanced Directive Education.

This reminder is an education type reminder. It relies on an active

education topic entry representing the Advanced Directives education in

the Education Topics file.

This reminder will be considered "DUE NOW" if there is no patient

education entry for advanced directive education in the "V Patient Ed."

file. The V Patient Ed. File summarizes the patient education provided

by clinicians at an encounter/visit.

By recording the education topic given at an encounter via a scanned

encounter form (or other interface to PCE), the reminder will be

considered "not indicated". Historical patient education for advanced

directives can be recorded in the PCE User Interface to make the reminder

not indicated.

The Clinical Maintenance component in the Health Summary will display the

latest date on record where advanced directive education/screening was

provided to the patient.

Initial installation comment:

The PCE package is distributed with a preliminary set of education

topics, which includes the VA-ADVANCED DIRECTIVES, and VA-ADVANCED

DIRECTIVES SCREENING entries.

The VA-ADVANCED DIRECTIVES education is defined as this reminders

education topic, in lieu of additional/other Advanced Directive education

topics you might want to create and activate at your site.

The VA-ADVANCED DIRECTIVES SCREENING education is defined to help track

the fact that an inquiry or screening was made to determine if the

patient needed Advanced Directive education/counseling.

If this reminder is used at your site, you may want to add at a minimum,

these two education topics on an encounter form for those clinics who

would be addressing this reminder.

Target Groups - Baseline:

Do In Advance Time Frame: 0M - Wait until actually DUE

Sex Specific:

Ignore on N/A:

Frequency for : 99Y - Once for all ages

Match Text:

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-ADVANCED DIRECTIVES

VA-ADVANCED DIRECTIVES SCREENING

Target Result Match Text:

No Match Text: No record of Advanced Directives

education/screening on file.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-ALCOHOL ABUSE EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Alcohol Abuse Education

Related * Reminder:	*PROBLEM DRINKING SCREEN

Reminder Description:

The VA-Alcohol Abuse Education reminder is based on guidelines defined by

the Ambulatory Care Expert Panel. This reminder includes the alcohol

abuse screening criteria to meet the "*Problem Drinking Screening"

reminder and more education criteria and diagnosis evaluation to

determine the need for the reminder.

This reminder is an "education" type reminder. It relies on an active

EDUCATION TOPIC (representing Alcohol Abuse education or screening) and

use of PCE TAXONOMY and HEALTH FACTORS related to alcohol abuse.

Technical Description:

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Alcohol abuse education due yearly for all ages.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-ALCOHOL ABUSE

VA-ALCOHOL ABUSE COMPLICATIONS

VA-ALCOHOL ABUSE DIET

VA-ALCOHOL ABUSE DISEASE PROCE

VA-ALCOHOL ABUSE EXERCISE

VA-ALCOHOL ABUSE FOLLOW-UP

VA-ALCOHOL ABUSE LIFESTYLE

VA-ALCOHOL ABUSE MEDICATIONS

VA-ALCOHOL ABUSE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-ALCOHOL ABUSE (TF(17))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-ALCOHOLISM SCREENING (TF(34))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: HISTORY OF AN ALCOHOL PROBLEM (HF(13))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: DRIVING UNDER THE INFLUENCE (HF(14))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: FAMILY HX OF ALCOHOL ABUSE (HF(15))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: PREV. SCREEN ETOH PROBLEM (HF(16))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: HEAVY DRINKER (3 OR MORE/DAY) (HF(17))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: DRINKING ALONE (HF(18))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: BINGE DRINKING (HF(19))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-BLOOD PRESSURE CHECK**

**-----------------------------------**

Reminder Type:	MEASUREMENT

Print Name:	Blood Pressure Check

Related * Reminder:	*HYPERTENSION SCREEN

Reminder Description:

BP due yearly for patients with no DX of hypertension, any age. BP due

at all visits for patients with DX of hypertension or cardiovascular

disease, any age.

The VA-Blood Pressure Check reminder is based on baseline guidelines

defined by the Ambulatory Care Expert Panel and depends on your site

entering Blood Pressure measurement values into the "Vital Measurement"

file. This reminder is different than the VA-HYPERTENSION SCREEN

reminder which is an Education type reminder which simply checks for the

existence of a Hypertension Screening being asked, and not whether the

Blood pressure value is documented.

Technical Description:

Review the Taxonomy definition for hypertension and cardiovascular

disease in the PCE Taxonomy file. Use the taxonomies as distributed or

copy a new taxonomy for local use and make the appropriate modifications.

Either accept the  reminder definition or create a local reminder

definition by copying the  reminder definition to a local reminder.

BP for Blood Pressure should be named as the Result Findings item from

the Vital Type file.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific:

Ignore on N/A:

Frequency for : 2 years for all ages

Match Text:

No Match Text:

Targeted Result Findings for MEASUREMENT reminder type:

GMRV VITAL TYPE

BLOOD PRESSURE

Target Result Match Text:

No Match Text: Vitals: Date of last Vitals blood pressure

measurement unknown.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HYPERTENSION (TF(1))

Match freq/age: 1 day for all ages

Rank Frequency: 1

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text: History of hypertension on record. BP due every

visit in patients with HTN.

No Match Text: No HX of HTN on file. No HX of hypertension

presumed.

Taxonomy: VA-HYPERTENSION SCREEN (TF(23))

Match freq/age: 2 years for all ages

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-BREAST EXAM**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Breast Exam

Related * Reminder:

Reminder Description:

A breast exam is due yearly for females 40 and older. If the female has a

history of breast cancer, check for ongoing follow-up yearly.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

Review the taxonomy findings definition being used to represent breast

cancer. Use the List Taxonomy Items option to see the coded values

defined for the taxonomy. If a taxonomy needs modifications, copy the

taxonomy and make appropriate modifications to the new taxonomy item.

Check the Exam file entries referenced and make modifications as needed

for local representation of exams.

If any changes to the reminder definition are needed, copy this reminder

to a new reminder for your sites use, and make the appropriate modifications.

Target Groups - Baseline:

Do In Advance Time Frame: 0M - Wait until actually DUE

Sex Specific: FEMALE

Ignore on N/A:

Frequency for : 1 year for ages 40 and older

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

BREAST EXAM

Target Result Match Text:

No Match Text: Date of last breast exam unknown. Please

document last exam or perform today.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-BREAST TUMOR (TF(18))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-BREAST SELF EXAM EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Breast Self Exam Education

Related * Reminder:

Reminder Description:

The breast self exam education is due yearly for females. If the female

has a history of breast cancer, check for ongoing follow-up yearly. If

the female has a history of a mastectomy, check for appropriateness of

breast self exam education.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel.

Technical Description:

The findings for breast self exam are based on the definition of an

education topic in the EDUCATION TOPICS file. Check the result findings

file for breast self exam entry which is distributed with this reminder.

If new education topics need to be added, use the PCE Table Maintenance

options, and then copy this reminder, and make the modifications to the

result findings to reference the education topics defined for your site.

Check the taxonomy findings definitions for breast cancer, breast tumor,

and mastectomy. Copy the taxonomies and make modifications if needed.

If any changes are needed in the findings definitions, copy this reminder

to a site defined reminder item and make the appropriate modifications.

Target Groups - Baseline:

Do In Advance Time Frame: 0M - Wait until actually DUE

Sex Specific: FEMALE

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text:

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-SELF BREAST EXAM

Target Result Match Text:

No Match Text: Date of last breast self exam education not known.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-BREAST TUMOR (TF(18))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient known to have HX of breast tumor or

breast cancer. Please verify appropriate TX

and F/U is ongoing yearly.

No Match Text: No HX breast cancer presumed.

Taxonomy: VA-MASTECTOMY (TF(19))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: This patient has had a mastectomy. If

appropriate for this patient, please provide

Breast Self Exam Education.

No Match Text:

General Match Text: Patient has a HX of breast cancer or other

breast disease that might complicate breast

self exam.

General No Match Text:

2 Health Factor Findings:

Health Factor: HX BREAST CANCER (HF(20))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: FAMILY HX BREAST CANCER (HF(22))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: PREV. BREAST CANCER SCREENING (HF(23))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-DIABETIC EYE EXAM**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Diabetic Eye Exam

Related * Reminder:

Reminder Description:

Patients with the VA-DIABETES taxonomy should have a diabetic eye exam

done yearly.

Technical Description:

This reminder is based on the Diabetic Eye Exam reminder from the New

York VAMC which was designed to meet the guidelines defined by the PACT

panel. Additional input came from the Saginaw VAMC.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 0Y - Not Indicated for all ages

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

DIABETIC EYE EXAM

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-DIABETES (TF(28))

Match freq/age: 1 year for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND

Match Text: Diabetic eye exam required annually for all

diabetic patients.

No Match Text: No history of diabetes on file.

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;(TF(28))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;(TF(VA-DIABETES))

**VA-DIABETIC FOOT CARE ED.**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Diabetic Foot Care Education

Related * Reminder:

Reminder Description:

Patients with the VA-DIABETES taxonomy should have a diabetic foot care

education done yearly.

Technical Description:

This reminder is based on the Diabetic care reminders from the

VAMC which were designed to meet the guidelines defined by the PACT

panel. Additional input came from the Saginaw VAMC.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 0Y - Not Indicated for all ages

Match Text:

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-DIABETES (TF(28))

Match freq/age: 1 year for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND

Match Text: Diabetic foot care education required annually

for all diabetic patients.

No Match Text: No history of diabetes on file.

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;(TF(28))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;(TF(VA-DIABETES))

**VA-DIABETIC FOOT EXAM**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Diabetic Foot Exam

Related * Reminder:

Reminder Description:

Patients with the VA-DIABETES taxonomy should have a complete foot exam

done yearly.

Technical Description:

This reminder is based on the Diabetic Foot Exam reminder from the New

York VAMC which was designed to meet the guidelines defined by the PACT

panel. Additional input came from the Saginaw VAMC.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 0Y - Not Indicated for all ages

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

DIABETIC FOOT EXAM, COMPLETE

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-DIABETES (TF(28))

Match freq/age: 1 year for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND

Match Text: Complete foot exam required annually for all

diabetic patients.

No Match Text: No history of diabetes on file.

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;(TF(28))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;(TF(VA-DIABETES))

**A-DIGITAL RECTAL (PROSTATE) EXAM**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Digital Rectal (Prostate) Exam

Related * Reminder:

Reminder Description:

Digital rectal (Prostate) exam should be given yearly to male patients

ages 40-75 with no DX of prostate cancer.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel.

Technical Description:

Check the Taxonomy Findings entries representing HX of Prostate Cancer.

If this taxonomy needs modification, copy the taxonomy to a new taxonomy

for your site, and make the appropriate modifications.

Check the Result Findings EXAM entry representing Digital rectal exam.

Make modifications to the EXAM file via the PCE Table Maintenance option.

If any modifications were required based on the checks above, then copy

the reminder definition to a new reminder, and make the appropriate

modifications to the reminder to reflect your site's guidelines.

Target Groups - Baseline:

Do In Advance Time Frame: 0M - Wait until actually DUE

Sex Specific: MALE

Ignore on N/A:

Frequency for : 1 year for ages 40 to 75

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

RECTAL EXAM

Target Result Match Text:

No Match Text: Date of last rectal exam not on file.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-PROSTATE CA (TF(8))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient known to have HX of prostate cancer.

Please verify appropriate TX and F/U is ongoing.

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-EXERCISE EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Exercise Education

Related * Reminder:	*FITNESS AND EXERCISE SCREEN

Reminder Description:

Exercise education given yearly to all patients.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel. It also supports the following "Fitness and Exercise

Counseling" guidelines specified in the "Guidelines for Health Promotion

and Disease Prevention",M-2, Part IV, Chapter 9.

Technical Description:

Findings to satisfy this reminder are defined in Education Topics and via

coded values defined in the VA-EXERCISE COUNSELING taxonomy.

This reminder can be inactivated for a patient by using the INACTIVATE

EXERCISE SCREEN health factor.

Check the Education Topics defined in the Results Findings multiple.

Does your site need to identify new education topics in the Education

Topics file to represent Exercise Education?

To update the education topics, use the PCE Table Maintenance options.

To modify this reminder from its distributed definition, copy the

reminder to a new reminder and then make the modifications necessary to

define your sites guideline.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Exercise education due yearly for all ages.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-EXERCISE

VA-EXERCISE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-EXERCISE COUNSELING (TF(32))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE EXERCISE SCREEN (HF(53))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE EXERCISE SCREEN (HF(54))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(53))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE EXERCISE SCREEN))

**VA-FECAL OCCULT BLOOD TEST**

**-----------------------------------**

Reminder Type:	EXAMINATION

Print Name:	Fecal Occult Blood Test

Related * Reminder:	*COLORECTAL CANCER SCREEN (FOBT)

Reminder Description:

Fecal occult blood test due every year for patients ages 50 and older

with no DX of colorectal cancer. This reminder conservatively recommends

that if a sigmoidoscopy was received, the next fecal occult blood test

would be due a year later.

This reminder is based on guidelines provided by the Ambulatory Care

Expert Panel. It also satisfies the "Colorectal Cancer Screen - FOBT"

guidelines specified in the "Guidelines for Health Promotion and Disease

Prevention", M-2, Part IV, Chapter 9.

Technical Description:

This reminder depends on Exam findings where an FOBT is completed in the

clinic, or on Taxonomy Findings representing FOBT.

Check the Taxonomy Findings entries representing HX of Colorectal Cancer.

If this taxonomy needs modification, copy the taxonomy to a new taxonomy

for your site, and make the appropriate modifications.

Check the Taxonomy Findings entries representing Fecal Occult Blood Test.

This represents coded standard entries in the CPT file and ICD

Operation/Procedure file. If this taxonomy needs modification, copy the

taxonomy to a new taxonomy for your site, and make the appropriate

modifications.

Copy the reminder to a new reminder for your local site's modifications.

NOTE: The Laboratory data is not available use in the reminder. When

the lab package begins passing CPT codes for fecal occult blood tests to

PCE, this reminder is ready to make use of the information.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for ages 50 and older

Match Text:

No Match Text:

Targeted Result Findings for EXAMINATION reminder type:

EXAM

FOBT(CLINIC)

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy:  (TF(4))

Match freq/age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Patient known to have HX of colorectal cancer.

Please verify appropriate TX &amp; F/U is ongoing.

No Match Text: No HX of colorectal cancer on file - presumed

no HX.

Taxonomy: VA-FOBT (TF(27))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-FLEXISIGMOIDOSCOPY (TF(15))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE FOBT CANCER SCREEN (HF(49))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE FOBT CANCER SCREEN (HF(50))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(49))&amp;'(TF(4))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE FOBT CANCER SCREEN))&amp;'(TF())

**VA-FLEXISIGMOIDOSCOPY**

**-----------------------------------**

Reminder Type:	PROCEDURE

Print Name:	Flexisigmoidoscopy

Related * Reminder:	*COLORECTAL CANCER SCREEN (SIG.)

Reminder Description:

Flexisigmoidoscopy every 5 years for patients age 50 and older, with no

DX of colorectal cancer.

This reminder is based on guidelines provided by the Ambulatory Care

Expert Panel and satisfies the sigmoidoscopy requirements for the

"Colorectal Cancer Detection" guidelines specified in the "Guidelines for

Health Promotion and Disease Prevention", M-2, Part IV, Chapter 9.

Technical Description:

Check the Taxonomy Findings entries representing HX of Colorectal Cancer.

If this taxonomy needs modification, copy the taxonomy to a new taxonomy

for your site, and make the appropriate modifications.

Check the Taxonomy Findings entries representing flexisigmoidoscopy

procedures. This represents coded standard entries in the CPT file and

ICD Operation/Procedure file. If this taxonomy needs modification, copy

the taxonomy to a new taxonomy for your site, and make the appropriate

modifications.

Copy the reminder to a new reminder for your local sites modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 5 years for ages 50 and older

Match Text:

No Match Text: Flexisigmoidoscopy not indicted for patients

under 50.

Targeted Result Findings for PROCEDURE reminder type:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-FLEXISIGMOIDOSCOPY (TF(15))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text: No flexisigmoidoscopy "CPT" or "ICD O/P" on file.

Taxonomy:  (TF(4))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient has HX of colorectal cancer. More

detailed F/U indicated.

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE SIGMOIDOSCOPY (HF(51))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE SIGMOIDOSCOPY (HF(52))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(51))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE SIGMOIDOSCOPY))

**VA-INFLUENZA VACCINE**

**-----------------------------------**

Reminder Type:	IMMUNIZATION

Print Name:	Influenza Vaccine

Related * Reminder:	*INFLUENZA IMMUNIZATION

Reminder Description:

Influenza vaccine given yearly for patients ages 65 and older, and for

patients of any age with a history of any of the following: asthma, COPD,

DM, ASVCD, CHG, chronic bronchitis, HIV positive or AIDS, renal

transplant, or cancer chemotherapy.

This reminder is defined based on guidelines from the Ambulatory Care

Expert Panel. It also supports the "Influenza Immunization" guidelines

specified in the "Guidelines for Health Promotion and Disease

Prevention", M-2, Part IV, Chapter 9.

Technical Description:

Check the Taxonomy Findings representing High Risk for Flu/Pneumonia. If

this taxonomy needs modification, copy the taxonomy to a new taxonomy for

your site, and make the appropriate modifications.

Copy the reminder to a new reminder for your local sites modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for ages 65 and older

Match Text: Influenza vaccine due yearly in patients ages

65 and older.

No Match Text:

Targeted Result Findings for IMMUNIZATION reminder type:

IMMUNIZATION

INFLUENZA

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HIGH RISK FOR FLU/PNEUMONIA (TF(9))

Match freq/age: 1 year for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Flu shot due yearly in patients any age that

have a high risk for flu or pneumonia.

No Match Text:

Taxonomy: VA-INFLUENZA IMMUNIZATION (TF(33))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE INFLUENZA IMMUNIZATION (HF(55))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE INFLUENZA IMMUNIZATION (HF(56))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(55))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE INFLUENZA IMMUNIZATION))

**VA-MAMMOGRAM**

**-----------------------------------**

Reminder Type:	RADIOLOGY PROCEDURE

Print Name:	Mammogram

Related * Reminder:	*BREAST CANCER SCREEN

Reminder Description:

Mammogram should be given every 2 years to female patients, ages 50-69

with no DX of breast cancer, and yearly for women with a history of

breast cancer or breast tumors, ages 35 - 69.

This reminder is based on guidelines provided by the Ambulatory Care

Expert Panel. The expert panel recommends a study for patients with

"high risk for breast cancer" to occur every 1 to 2 years. A conservative

1 year is defined in this reminder definition.

This reminder also supports the "Breast Cancer Detection" reminder

defined in the "Guidelines for Health Promotion and Disease Prevention",

M-2, Part IV, Chapter 9.

Technical Description:

The findings for mammogram are based on defining the CPT codes

representing mammograms in a taxonomy for Mammograms. The CPT codes are

used to search the Radiology procedures in the Radiology package, as well

as checks for existence of a CPT code in the V CPT file.

Check the taxonomy findings definition for breast cancer and breast

tumor. Copy the taxonomies and make modifications if needed.

If any changes were needed in the findings, copy this reminder to a site

defined reminder item and make the appropriate modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific: FEMALE

Ignore on N/A: S

Frequency for : 2 years for ages 50 to 69

Match Text: Women ages 50-69 should receive a mammogram

every two years.

No Match Text:

Targeted Result Findings for RADIOLOGY PROCEDURE reminder type:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-MAMMOGRAM/SCREEN (TF(16))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Taxonomy: VA-BREAST TUMOR (TF(18))

Match freq/age: 1 year for ages 35 to 69

Rank Frequency:

Use in Date Due Calc: NO

Use in Apply Logic:

Match Text: History of breast cancer or breast tumor on

file. Due yearly for patients ages 35-69.

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE BREAST CANCER SCREEN (HF(42))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE BREAST CANCER SCREEN (HF(43))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(42))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE BREAST CANCER SCREEN))

**VA-NUTRITION/OBESITY EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Nutrition/Obesity Education

Related * Reminder:	*WEIGHT AND NUTRITION SCREEN

Reminder Description:

Given yearly to patients of any age who have a history of a nutrition

disorder or a history of obesity. Also given to patients who are

considered obese based on a Body Mass Index greater than 27, which

represents weight greater than 120% of Ideal Body Weight.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel. This reminder also supports the "Weight Control and

Nutrition Counseling" guidelines defined in the "Guidelines for Health

Promotion and Disease Prevention", M-2, Part IV, Chapter 9.

Technical Description:

The most recent taxonomy finding within a taxonomy is presented for

clinical information.

The most recent health factor finding within a health factor category is

presented for clinical information. If all 6 of the health factors that

are from the NUTRITION health factor category were found for the patient,

only the most recent health factor within the "NUTRITION" health factor

category would be used by the reminder. Since the activate and

inactivate health factors are defined under the "REMINDER CATEGORY" they

are evaluated and the most recent of these two factors would also be used

by the reminder.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Weight and Nutrition education due yearly for

all ages.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-NUTRITION/OBESITY

VA-NUTRITION/WEIGHT SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-OBESITY (TF(20))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient has a history of obesity.

No Match Text: No HX of obesity on file.

Taxonomy: VA-NUTRITION (TF(21))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient has a history of a nutrition disorder.

No Match Text: No HX of nutrition disorder on file.

Taxonomy: VA-WEIGHT AND NUTRITION SCREEN (TF(36))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: HX NUTRITIONAL DISORDER (HF(25))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: PREV. SCREEN NUTR. DISORDER (HF(26))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: IRREGULAR MEALS (HF(27))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: FREQUENT DIETING (HF(28))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: FOOD CRAVINGS (HF(29))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: CURRENTLY PREGNANT (HF(30))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: INACTIVATE WEIGHT/NUTRITION SCREEN (HF(67))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE WEIGHT/NUTRITION SCREEN (HF(68))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Short Description: Calculate BMI&gt;27

Routine: OBESE;PXRMOBES

Match Freq/Age:

Match Text:

No Match Text:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(67))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE WEIGHT/NUTRITION SCREEN))

**VA-PAP SMEAR**

**-----------------------------------**

Reminder Type:	PROCEDURE

Print Name:	Pap Smear

Related * Reminder:	*CERVICAL CANCER SCREEN

Reminder Description:

Pap smear/pelvic exam every three years for female patients, age 65 and

under, with no DX of cervical cancer or abnormal pap smear and no

previous abnormal pap smear lab test.

If patient has had hysterectomy for benign disease, no pap smear is

indicated.

This reminder is based on the Ambulatory Care EP and supports the

"Cervical Cancer Screen" guidelines specified in the "Guidelines for

Health Promotion and Disease Prevention", M-2, Part IV, Chapter 9.

Technical Description:

Check the Taxonomy Findings representing history of hysterectomy for

benign disease, and history of cervical cancer or abnormal PAP. If these

taxonomies need modifications, copy each to a new taxonomy for your local

site, and make the appropriate modifications.

Define Health Factors that may represent Sexual Activity. To add new

Health Factors use the PCE Table Maintenance option.

Copy the reminder to a new reminder for your local site modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Wait until actually DUE

Sex Specific: FEMALE

Ignore on N/A: S

Frequency for : 3 years for ages 65 and younger

Match Text: Pap smear/pelvic exam due every 3 years for

women ages 65 and younger.

No Match Text: Pap smear screen not indicated for women over 65.

Targeted Result Findings for PROCEDURE reminder type:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HYSTERECTOMY (TF(6))

Match freq/age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Pap not indicated in women with HX hysterectomy

for benign disease.

No Match Text: No HX of hysterectomy - presumed no such HX.

Taxonomy: VA-CERVICAL CA/ABNORMAL PAP (TF(5))

Match freq/age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Patient has HX of cervical cancer. Please

verify appropriate TX &amp; F/U is ongoing.

No Match Text: No HX of cervical cancer on file - no HX

cervical cancer presumed.

Taxonomy: VA-CERVICAL CANCER SCREEN (TF(30))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text: Date of last cervical cancer screen taxonomy

unknown.

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE CERVIX CANCER SCREEN (HF(44))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE CERVIX CANCER SCREEN (HF(47))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(44))&amp;'(TF(6))&amp;'(TF(5))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE CERVIX CANCER SCREEN))&amp;'(TF(

HYSTERECTOMY))&amp;' (TF(VA-CERVICAL CA/ABNORMAL PAP))

**VA-PNEUMOVAX**

**-----------------------------------**

Reminder Type:	IMMUNIZATION

Print Name:	Pneumovax

Related * Reminder:	*PNEUMOCOCCAL VACCINE

Reminder Description:

Pneumovax given once to patients 65 and over, and to patients of any age

with a history of any of the following diagnoses: asthma, COPD, DM,

ASCVD, CHG, chronic bronchitis, HIV positive or AIDS, renal transplant,

or cancer chemotherapy.

This reminder is defined based on guidelines from the Ambulatory Care

Expert Panel. It also supports the "Pneumococcal Vaccine" guidelines

specified in the "Guidelines for Health Promotion and Disease

Prevention", M-2, Part IV, Chapter 9.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

Check the Taxonomy Findings representing High Risk for Flu/Pneumonia. If

the taxonomy needs modification, copy the taxonomy to a new taxonomy for

your site, and make the appropriate modifications.

Copy the reminder to a new reminder for your local sites modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 3 months

Sex Specific:

Ignore on N/A:

Frequency for : 99Y - Once for ages 65 and older

Match Text: Pneumovax due once for patients 65 and over.

No Match Text:

Targeted Result Findings for IMMUNIZATION reminder type:

IMMUNIZATION

PNEUMOCOCCAL

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HIGH RISK FOR FLU/PNEUMONIA (TF(9))

Match freq/age: 99Y - Once for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Pneumovax due once in high risk patients.

No Match Text: No high risk DX for flu/pneumonia on file.

Presumed low risk.

Taxonomy: VA-PNEUMOCOCCAL VACCINE (TF(25))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE PNEUMOCOCCAL VACCINE (HF(57))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE PNEUMOCOCCAL VACCINE (HF(58))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(57))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE PNEUMOCOCCAL VACCINE))

**VA-PPD**

**-----------------------------------**

Reminder Type:	SKIN TEST

Print Name:	PPD

Related * Reminder:

Reminder Description:

PPD given yearly to patients of any age who have a "High risk DX for TB";

such as HIV positive or AIDS, homelessness, or alcohol abuse who do not

have a DX of tuberculosis and no prior positive TB skin test.

This reminder is based on guidelines provided by the Ambulatory Care

Expert Panel.

Technical Description:

Check the Taxonomy Findings representing High Risk for TB. If this

taxonomy needs modification, copy the taxonomy to a new taxonomy for your

site, and make the appropriate modifications.

Define health factors which may represent high risk for TB in the Health

Factors file via the PCE Table Maintenance options.

Copy the reminder to a new reminder for your local site modifications.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 0Y - Not Indicated for all ages

Match Text:

No Match Text:

Targeted Result Findings for SKIN TEST reminder type:

SKIN TEST

PPD

Target Result Match Text:

No Match Text: Last date of PPD not known.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-HIGH RISK FOR TB (TF(11))

Match freq/age: 1 year for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND

Match Text: Patient has high risk for TB diagnosis, PPD due

yearly.

No Match Text: Patient may be low risk for TB, where PPD may

not be indicated.

Taxonomy: VA-TB/POSITIVE PPD (TF(10))

Match freq/age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Patient has HX of TB or positive PPD diagnosis.

No Match Text: No HX of TB or positive PPD diagnosis on file.

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;(TF(11))&amp;'(TF(10))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;(TF(VA-HIGH RISK FOR TB))&amp;'(TF(VA-TB/POSITIVE PPD))

**VA-PSA**

**-----------------------------------**

Reminder Type:	LABORATORY TEST

Print Name:	PSA

Related * Reminder:

Reminder Description:

Prostate specific antigen, PSA, due yearly for men ages 50-75, who do not

have a history of prostate cancer.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel.

Technical Description:

Check the Taxonomy Findings entries representing HX of prostate cancer.

If this taxonomy needs modification, copy the taxonomy to a new taxonomy

for your site, and make the appropriate modifications.

Copy the reminder to a new reminder for your local sites modifications.

Use the new reminder to update the Result Findings Laboratory Test entry

representing PSA tests.

Target Groups - Baseline:

Do In Advance Time Frame: 0M - Wait until actually DUE

Sex Specific: MALE

Ignore on N/A:

Frequency for : 1 year for ages 50 to 75

Match Text:

No Match Text:

Targeted Result Findings for LABORATORY TEST reminder type:

LABORATORY TEST

Target Result Match Text:

No Match Text: Date of last PSA not on file. Please order

test or document historical encounter activity.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-PROSTATE CA (TF(8))

Match freq/age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient known to have HX of prostate cancer.

Please verify appropriate TX and follow-up is

ongoing.

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

**VA-SEATBELT EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Seat Belt Education

Related * Reminder:	*SEATBELT AND ACCIDENT SCREEN

Reminder Description:

Seat belt education given yearly to all patients.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel and is further supported by the "Seatbelt Use and Accident

Avoidance Counseling" guideline specified in the "Guidelines for Health

Promotion and Disease Prevention", M-2, Part IV, Chapter 9.

Target Condition: Motor vehicle associated injuries.

Target Group: General Outpatient population.

Recommendation: All patients should be urged to use seatbelts in

automobiles, wear helmets when riding bicycles or motorcycles, and to

refrain from driving after drinking.

Goal for FY 2000: 85% of Veterans report regular use of seatbelts in

automobiles. 80% of motorcyclists and 50% of bicyclists report use of

helmets. 50% of primary care providers routinely provide

age-appropriate counseling on safety precautions to prevent

unintentional injury.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE

FLAG should be set to inactive.

The VA-SEAT BELT EDUCATION" reminder is a variation of the "VA-SEAT BELT

AND ACCIDENT SCREEN" reminder. The VA-SEAT BELT EDUCATION" reminder is

recommended by the Ambulatory Care EP to check for seat belt use

education given to the patient, in addition to the screening.

Please review both of these related reminder definitions, choose one of

them to use. If local modifications need to be made, copy the preferred

reminder to a new reminder and make your reminder modifications.

It may be useful to add Health Factors that indicate whether the patient

is still driving, rides motorcycles, or rides bicycles for local site

use. This would involve adding new Health Factors to the Health Factor

file (#9999999.64) and then adding the Health Factors to a local site

definition of the seat belt reminder.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text: Seat belt education due yearly for all ages.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-SEAT BELT USE

VA-SEAT BELT USE SCREENING

Target Result Match Text:

No Match Text:

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-SAFETY COUNSELING (TF(35))

Match freq/age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: INACTIVATE SEATBELT SCREEN (HF(61))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

Health Factor: ACTIVATE SEATBELT SCREEN (HF(62))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(61))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE SEATBELT SCREEN))

**VA-TOBACCO EDUCATION**

**-----------------------------------**

Reminder Type:	EDUCATION

Print Name:	Tobacco Cessation Education

Related * Reminder:	*TOBACCO USE SCREEN

Reminder Description:

Tobacco use cessation education should be offered annually to any patient

who has a diagnosis or health factor associated with chronic tobacco use.

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel and satisfies the "Smoking and Tobacco Use Counseling"

guidelines specified in the "Guidelines for Health Promotion and Disease

Prevention",M-2, Part IV, Chapter 9.

Modifications to these guidelines for your local site may be reflected in

a new reminder definition.

Technical Description:

Check the ICD Diagnosis entries defined in the PCE Taxonomy file for

VA-TOBACCO USE. Reflect any changes in a new taxonomy definition.

Check/Modify the health factors defined within the Tobacco category in

the Health Factors file. The Health Factors file can be modified using

the PCE Table Maintenance options.

If the reminder needs modifications, copy it and modify the new reminder

to meet local site guidelines.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text:

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-TOBACCO USE SCREENING

VA-SMOKING CESSATION

Target Result Match Text:

No Match Text: No history of tobacco education/screen on file.

Please evaluate tobacco use and educate if

currently in use.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy: VA-TOBACCO USE (TF(22))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text: Patient has a history of tobacco use.

No Match Text: No history of tobacco use found. Presumed to be

former or current smoker. Please indicate via

health factor (Lifetime non-smoker, or other

health factor) if the tobacco education is not

indicated.

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor: HISTORY OF SMOKING (HF(31))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text: No history of smoking found.

Health Factor: HX OF SEC. SMOKE INHALATIION (HF(32))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text: Patient has no history of secondary smoke

inhalation.

Health Factor: LIFETIME NON-SMOKER (HF(5))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Patient is lifetime non-smoker, tobacco

education not indicated.

No Match Text:

Health Factor: CURRENT SMOKER (HF(2))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: CURRENT NON-SMOKER (HF(3))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: LIFETIME NON-TOBACCO USER (HF(37))

Match Freq/Age: 0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text: Patient is lifetime non-tobacco user, tobacco

education not indicated.

No Match Text:

Health Factor: SMOKELESS TOBACCO USER (HF(38))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: HX OF CHEWING TOBACCO (HF(33))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: CURRENT SMOKELESS TOBACCO USER (HF(39))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc: YES

Use in Apply Logic:

Match Text:

No Match Text:

Health Factor: INACTIVATE TOBACCO USE SCREEN (HF(65))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic: AND NOT

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(5))&amp;'(HF(37))&amp;'(HF(65))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(LIFETIME NON-SMOKER))&amp;'(HF(LIFETIME NON-TOBACCO USER))&amp;'

(HF(INACTIVATE TOBACCO USE SCREEN))

**VA-WEIGHT**

**-----------------------------------**

Reminder Type:	MEASUREMENT

Print Name:	Weight

Related * Reminder:

Reminder Description:

The patient's weight should be documented yearly.

Technical Description:

This reminder is based on guidelines defined by the Ambulatory Care

Expert Panel.

Target Groups - Baseline:

Do In Advance Time Frame: Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for : 1 year for all ages

Match Text:

No Match Text:

Targeted Result Findings for MEASUREMENT reminder type:

GMRV VITAL TYPE

WEIGHT

Target Result Match Text:

No Match Text: No weight measurement on record, please record

now.

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

General Match Text:

General No Match Text:

2 Health Factor Findings:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)

Expanded Apply Logic:

(SEX)&amp;(AGE)

*(This page included for two-sided copying.)*

### Appendix A-9   Distributed Taxonomies

PCE TAXONOMY LIST                        APR 21,1997              PAGE 1

NAME

LOW	HIGH

CODED	CODED

VALUE	VALUE	SOURCE FILE

-----------------------------------------------------------------------------

VA-ALCOHOLISM SCREENING

V79.1 	V79.1 	ICD DIAGNOSIS

VA-BREAST TUMOR

174 	174.9 	ICD DIAGNOSIS

198.81 	198.81 	ICD DIAGNOSIS

238.3 	238.3 	ICD DIAGNOSIS

239.3 	239.3 	ICD DIAGNOSIS

233.0 	233.0 	ICD DIAGNOSIS

217 	217 	ICD DIAGNOSIS

610 	610.9 	ICD DIAGNOSIS

611 	611 	ICD DIAGNOSIS

611.	5 611.5 	ICD DIAGNOSIS

611.71 	611.72 	ICD DIAGNOSIS

611.9 	611.9 	ICD DIAGNOSIS

675.1 	675.14 	ICD DIAGNOSIS

757.6 	757.6 	ICD DIAGNOSIS

922.0 	922.0 	ICD DIAGNOSIS

793.8 	793.8 	ICD DIAGNOSIS

V10.3 	V10.3 	ICD DIAGNOSIS

VA-CERVICAL CA/ABNORMAL PAP

180 	180.9 	ICD DIAGNOSIS

198.82 	198.82 	ICD DIAGNOSIS

233.1 	233.3 	ICD DIAGNOSIS

795.0 	795.0 	ICD DIAGNOSIS

VA-CERVICAL CANCER SCREEN

Q0091 	Q0091 	CPT

V76.2	V76.2 	ICD DIAGNOSIS

Q0060 	Q0061 	CPT

P3000 	P3001 	CPT

88150 	88150 	CPT

91.46 	91.46 	ICD OPERATION/PROCEDURE

VA-CHOLESTEROL

G0054 	G0054 	CPT

83718 	83721 	CPT

80061 	80061 	CPT

82465 	82470 	CPT

83700 	83705 	CPT

VA-COLORECTAL CA

154.0 	154.8 	ICD DIAGNOSIS

197.5 	197.5 	ICD DIAGNOSIS

230.3 	230.4 	ICD DIAGNOSIS

PCE TAXONOMY LIST                        APR 21,1997 10:58             PAGE 2

NAME

LOW	HIGH

CODED	CODED

VALUE	VALUE	SOURCE FILE

-----------------------------------------------------------------------------

VA-COLORECTAL CANCER SCREEN

V76.41 	V76.41 	ICD DIAGNOSIS

VA-DIABETES

250 	250.9 	ICD DIAGNOSIS

VA-EXERCISE COUNSELING

V65.41 	V65.41 	ICD DIAGNOSIS

VA-FLEXISIGMOIDOSCOPY

45.24 	45.24 	ICD OPERATION/PROCEDURE

45330 	45385 	CPT

VA-FOBT

82270 	82273 	CPT

VA-HIGH RISK FOR FLU/PNEUMONIA

493.0 	493.91 	ICD DIAGNOSIS

496 	496 	ICD DIAGNOSIS

250.00 	250.9 	ICD DIAGNOSIS

429.2 	429.2 	ICD DIAGNOSIS

428.0 	428.9 	ICD DIAGNOSIS

491.0 	491.9 	ICD DIAGNOSIS

044.9 	044.9 	ICD DIAGNOSIS

042.0 	043.9 	ICD DIAGNOSIS

V42.0 	V42.0 	ICD DIAGNOSIS

585 	585 	ICD DIAGNOSIS

V58.1 	V58.1 	ICD DIAGNOSIS

V66.2 	V66.2 	ICD DIAGNOSIS

99.52 	99.52 	ICD OPERATION/PROCEDURE

V67.2 	V67.2 	ICD DIAGNOSIS

VA-HIGH RISK FOR TB

044.9 	044.9 	ICD DIAGNOSIS

042.0 	043.9 	ICD DIAGNOSIS

V60.0 	V60.0 	ICD DIAGNOSIS

303.0 	304.90 	ICD DIAGNOSIS

305.0 	305.0 	ICD DIAGNOSIS

VA-HYPERTENSION

401.0 	405.99 	ICD DIAGNOSIS

VA-HYPERTENSION SCREEN

V81.1 	V81.1 	ICD DIAGNOSIS

80060 	80060 	CPT

VA-HYSTERECTOMY

68.3 	68.9 	ICD OPERATION/PROCEDURE

PCE TAXONOMY LIST                        APR 21,1997 10:58             PAGE 3

NAME

LOW	HIGH

CODED	CODED

VALUE	VALUE	SOURCE FILE

-----------------------------------------------------------------------------

VA-INFLUENZA IMMUNIZATION

V04.8	V04.8 	ICD DIAGNOSIS

90724 	90724 	CPT

Q0034 	Q0034 	CPT

G0008 	G0008 	CPT

VA-MAMMOGRAM/SCREEN

76090 	76092 	CPT

V76.1 	V76.1 	ICD DIAGNOSIS

VA-MASTECTOMY

85.23 	85.23 	ICD OPERATION/PROCEDURE

85.41 	85.48 	ICD OPERATION/PROCEDURE

19140 	19140 	CPT

19160 	19160 	CPT

19162 	19162 	CPT

19180 	19180 	CPT

19182 	19182 	CPT

19200 	19200 	CPT

19220 	19220 	CPT

T1950 	T1999 	CPT

VA-NUTRITION

260 	260 	ICD DIAGNOSIS

261 	261 	ICD DIAGNOSIS

263 	263.2 	ICD DIAGNOSIS

263.8	263.8 	ICD DIAGNOSIS

263.9 	263.9 	ICD DIAGNOSIS

264 	264.9 	ICD DIAGNOSIS

265 	265.2 	ICD DIAGNOSIS

266 	266.9 	ICD DIAGNOSIS

267 	267 	ICD DIAGNOSIS

268 	268.9 	ICD DIAGNOSIS

269 	269.9 	ICD DIAGNOSIS

281.1 	281.11 	ICD DIAGNOSIS

783.0 	783.4 	ICD DIAGNOSIS

377.33 	377.33 	ICD DIAGNOSIS

425.7 	425.7 	ICD DIAGNOSIS

760.4 	760.4 	ICD DIAGNOSIS

783.6 	783.9 	ICD DIAGNOSIS

V69.1 	V69.1

VA-OBESITY

278.0 	278.01 	ICD DIAGNOSIS

783.1 	783.1 	ICD DIAGNOSIS

43842 	43842 	CPT

43846 	43846 	CPT

44131 	44131 	CPT

99078 	99078 	CPT

PCE TAXONOMY LIST                        APR 21,1997 10:58             PAGE 4

NAME

LOW	HIGH

CODED	CODED

VALUE	VALUE	SOURCE FILE

-----------------------------------------------------------------------------

VA-PNEUMOCOCCAL VACCINE

99.55 	99.55 	ICD OPERATION/PROCEDURE

99.59 	99.59 	ICD OPERATION/PROCEDURE

G0009 	G0009 	CPT

90732 	90732 	CPT

V06.6 	V06.6 	ICD DIAGNOSIS

VA-PROSTATE CA

185 	185 	ICD DIAGNOSIS

198.82 	198.82 	ICD DIAGNOSIS

233.4 	233.4 	ICD DIAGNOSIS

VA-PSA

84153 	84153 	CPT

VA-SAFETY COUNSELING

V65.43 	V65.43 	ICD DIAGNOSIS

VA-TB/POSITIVE PPD

010.0 	018.9 	ICD DIAGNOSIS

795.5 	795.5 	ICD DIAGNOSIS

VA-TETANUS DIPHTHERIA

90700 	90703 	CPT

90711 	90711 	CPT

90718	90721 	CPT

99.36 	99.38 	ICD OPERATION/PROCEDURE

V03.5 	V03.5 	ICD DIAGNOSIS

V03.7 	V03.7 	ICD DIAGNOSIS

V06.1 	V06.5 	ICD DIAGNOSIS

VA-TOBACCO USE

305.1 	305.1 	ICD DIAGNOSIS

305.10 	305.11 	ICD DIAGNOSIS

V15.82 	V15.82 	ICD DIAGNOSIS

VA-WEIGHT AND NUTRITION SCREEN

V65.3 	V65.3 	ICD DIAGNOSIS

V77.8 	V77.9 	ICD DIAGNOSIS

### Appendix A-10   Sample Health Summaries

10:28

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,THREE      666-78-7654                           DOB:

-------------------------- CM - Clinical Maintenance ------------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT-- --LAST--

Cholesterol Screen (Male)          N/A

Patient's age (72) is greater than reminder maximum age of 65.

LAB: Date of last cholesterol test unknown.

Fecal Occult Blood Test            07/02/97 07/02/96

Health Factor: ACTIVATE FOBT CANCER SCREEN

Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

Encounter Procedure: 82270-TEST FECES FOR BLOOD

FOBT due 5 years after the last sigmoidoscopy.

Final Frequency and  used: 1 year for ages 50 and older.

Flexisigmoidoscopy                 N/A

Health Factor: INACTIVATE SIGMOIDOSCOPY

Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

Encounter Procedure: 82270-TEST FECES FOR BLOOD

Final Frequency and  used: 0Y - Not Indicated for ages 50

and older.

Exercise Education                 DUE NOW  unknown

Final Frequency and  used: 1 year for all ages.

Hypertension Detection             DUE NOW  unknown

Vitals: Date of last Vitals BP Measurement unknown.

Date of last ICD or CPT coded hypertension screen unknown.

Final Frequency and  used: 2 years for all ages.

Influenza Immunization             07/02/97 07/02/96

Encounter Procedure: 90724-INFLUENZA IMMUNIZATION

Influenza vaccine due yearly in patients ages 65 and older.

Final Frequency and  used: 1 year for ages 65 and older.

Pneumovax                          DONE

Encounter Procedure: 90732-PNEUMOCOCCAL IMMUNIZATION

Pneumovax due once for patients 65 and over.

Final Frequency and  used: 99Y - Once for ages 65 and older.

Problem Drinking Screen            DUE NOW  unknown

Screen for alcohol problems yearly for all patients.

Final Frequency and  used: 1 year for all ages.

10:28

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,THREE      666-78-7654                           DOB:

Seatbelt and Accident Screen       DUE NOW  unknown

Seatbelt education due yearly for all patients.

Final Frequency and  used: 1 year for all ages.

Tobacco Use Screen                 DUE NOW  unknown

Tobacco use screen due yearly for all ages.

No history of tobacco use screen on file. Please evaluate tobacco

use and educate if currently in use.

Final Frequency and  used: 1 year for all ages.

Weight and Nutrition Screen        DUE NOW  unknown

Weight and Nutrition screen due yearly for all patients.

Final Frequency and  used: 1 year for all ages.

Advanced Directives Education      DUE NOW  unknown

No record of Advanced Directives education/screening on file.

Final Frequency and  used: 99Y - Once for all ages.

Alcohol Abuse Education            DUE NOW  unknown

Alcohol abuse education due yearly for all ages.

Final Frequency and  used: 1 year for all ages.

Blood Pressure Check               DUE NOW  unknown

Vitals: Date of last Vitals blood pressure measurement unknown.

No HX of HTN on file. No HX of hypertension presumed.

Final Frequency and  used: 2 years for all ages.

Breast Exam                        N/A

Patient is the wrong sex for this reminder.

Breast Self Exam Education         N/A

Patient is the wrong sex for this reminder.

Digital Rectal (Prostate) Exam     DUE NOW  unknown

Date of last rectal exam not on file.

Final Frequency and  used: 1 year for ages 40 to 75.

Exercise Education                 DUE NOW  unknown

Exercise education due yearly for all ages.

Final Frequency and  used: 1 year for all ages.

Fecal Occult Blood Test            07/02/97 07/02/96

Health Factor: ACTIVATE FOBT CANCER SCREEN

Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

Encounter Procedure: 82270-TEST FECES FOR BLOOD

No HX of colorectal cancer on file - presumed no HX.

Final Frequency and  used: 1 year for ages 50 and older.

Flexisigmoidoscopy                 N/A

Health Factor: INACTIVATE SIGMOIDOSCOPY

Encounter Procedure: 45330-SIGMOIDOSCOPY, DIAGNOSTIC

Final Frequency and  used: 0Y - Not Indicated for all ages.

10:28

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,THREE      666-78-7654                           DOB:

Influenza Vaccine                  07/02/97 07/02/96

Encounter Procedure: 90724-INFLUENZA IMMUNIZATION

Influenza vaccine due yearly in patients ages 65 and older.

Final Frequency and  used: 1 year for ages 65 and older.

PPD                                N/A

Last date of PPD not known.

Patient may be low risk for TB, where PPD may not be indicated.

No HX of TB or positive PPD diagnosis on file.

Final Frequency and  used: 0Y - Not Indicated for all ages.

PSA                                DUE NOW  unknown

Date of last PSA not on file. Please order test or document

historical encounter activity.

Final Frequency and  used: 1 year for ages 50 to 75.

Seat Belt Education                DUE NOW  unknown

Seat belt education due yearly for all ages.

Final Frequency and  used: 1 year for all ages.

Tobacco Cessation Education        DUE NOW  unknown

No history of smoking found.

Patient has no history of secondary smoke inhalation.

No history of tobacco education/screen on file. Please evaluate

tobacco use and educate if currently in use.

No history of tobacco use found. Presumed to be former or current

smoker. Please indicate via health factor (Lifetime non-smoker, or

other health factor) if the tobacco education is not indicated.

Final Frequency and  used: 1 year for all ages.

Weight                             DUE NOW  unknown

No weight measurement on record, please record now.

Final Frequency and  used: 1 year for all ages.

DIABETIC FOOT EXAM                 N/A

--------------------------- CR - Clinical Reminders -------------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT-- --LAST--

Advanced Directives Education      DUE NOW  unknown

Alcohol Abuse Education            DUE NOW  unknown

Exercise Education                 DUE NOW  unknown

Seat Belt Education                DUE NOW  unknown

Tobacco Cessation Education        DUE NOW  unknown

* END *

10:31

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,ONE        000-45-6789                        DOB:

-------------------------- CM - Clinical Maintenance ------------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT-- --LAST--

Breast Cancer Screen               02/21/99 02/21/97

Health Factor: ACTIVATE BREAST CANCER SCREEN

Encounter Procedure: 76092-MAMM0GRAM, SCREENING

Health Factor comments: Activate health factor comments

History of mammogram/screen on file.

Final Frequency and  used: 2 years for ages 50 to 69.

Pap Smear                          DUE NOW  unknown

Women ages 65 and younger should receive a cervical cancer screen

every 3 years.

No record of cervical cancer screen taxonomy on file

Final Frequency and  used: 3 years for ages 65 and younger.

Cholesterol Screen (Female)        DUE NOW  unknown

Check total cholesterol every 5 years for women ages 45-65.

LAB: Date of last cholesterol test unknown.

Final Frequency and  used: 5 years for ages 45 to 65.

Fecal Occult Blood Test            08/09/01 08/09/96

Encounter Procedure: 45333-SIGMOIDOSCOPY &amp; POLYPECTOMY

Examination: FOBT(CLINIC)

FOBT due 5 years after the last sigmoidoscopy.

Final Frequency and  used: 5 years for ages 50 and older.

Flexisigmoidoscopy                 08/09/01 08/09/96

Encounter Procedure: 45333-SIGMOIDOSCOPY &amp; POLYPECTOMY

Examination: FOBT(CLINIC)

Final Frequency and  used: 5 years for ages 50 and older.

Exercise Education                 DUE NOW  unknown

Final Frequency and  used: 1 year for all ages.

Hypertension Detection             08/13/98 08/13/96

Measurement: BLOOD PRESSURE; results - 132/72

Date of last ICD or CPT coded hypertension screen unknown.

Final Frequency and  used: 2 years for all ages.

Influenza Immunization             N/A

Encounter Procedure: 90724-INFLUENZA IMMUNIZATION

Influenza vaccine not indicated for patients under 65.

Patient's age (53) is less than reminder minimum age of 65.

10:31

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,ONE        000-45-6789                        DOB:

-------------------------- CM - Clinical Maintenance ------------------------

Pneumovax                          N/A

Encounter Procedure: 90732-PNEUMOCOCCAL IMMUNIZATION

Patient's age (53) is less than reminder minimum age of 65.

Problem Drinking Screen            DUE NOW  unknown

Screen for alcohol problems yearly for all patients.

Final Frequency and  used: 1 year for all ages.

Seatbelt and Accident Screen       DUE NOW  unknown

Seatbelt education due yearly for all patients.

Final Frequency and  used: 1 year for all ages.

Tobacco Use Screen                 DUE NOW  unknown

Tobacco use screen due yearly for all ages.

No history of tobacco use screen on file. Please evaluate tobacco

use and educate if currently in use.

Final Frequency and  used: 1 year for all ages.

Weight and Nutrition Screen        DUE NOW  unknown

Weight and Nutrition screen due yearly for all patients.

Final Frequency and  used: 1 year for all ages.

Advanced Directives Education      DONE

Education: Advanced Directive Screening

Final Frequency and  used: 99Y - Once for all ages.

Alcohol Abuse Education            09/12/97 09/12/96

Encounter Diagnosis: 571.3-ALCOHOL LIVER DAMAGE NOS

Alcohol abuse education due yearly for all ages.

Education: Alcohol Abuse

Final Frequency and  used: 1 year for all ages.

Blood Pressure Check               DUE NOW

Problem Diagnosis: 405.99-SECOND HYPERTENSION NEC

Encounter Diagnosis: 401.9-HYPERTENSION NOS

Measurement: BLOOD PRESSURE; results - 132/72

History of hypertension on record. BP due every visit in patients

with HTN.

Final Frequency and  used: 1 day for all ages.

Breast Exam                        DUE NOW  unknown

Date of last breast exam unknown. Please document last exam or

perform today.

Final Frequency and  used: 1 year for ages 40 and older.

Breast Self Exam Education         DUE NOW  unknown

Date of last breast self exam education not known.

No HX breast cancer presumed.

Final Frequency and  used: 1 year for all ages.

10:31

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,ONE        000-45-6789                        DOB:

-------------------------- CM - Clinical Maintenance ------------------------

Digital Rectal (Prostate) Exam     N/A

Patient is the wrong sex for this reminder.

Exercise Education                 DUE NOW  unknown

Exercise education due yearly for all ages.

Final Frequency and  used: 1 year for all ages.

Fecal Occult Blood Test            08/09/97 08/09/96

Encounter Procedure: 45333-SIGMOIDOSCOPY &amp; POLYPECTOMY

Examination: FOBT(CLINIC)

No HX of colorectal cancer on file - presumed no HX.

Final Frequency and  used: 1 year for ages 50 and older.

Flexisigmoidoscopy                 06/13/00 06/13/95

Encounter Procedure: 45333-SIGMOIDOSCOPY &amp; POLYPECTOMY

Final Frequency and  used: 5 years for ages 50 and older.

Influenza Vaccine                  02/21/98 02/21/97

Problem Diagnosis: 250.01-DIABETES MELLI W/0 COMP TYP I

Encounter Diagnosis: 250.13-DIABETES W/KETOACID. TYPE I

Encounter Procedure: 90724-INFLUENZA IMMUNIZATION

Flu shot due yearly in patients any age that have a high risk for flu

or pneumonia.

Final Frequency and  used: 1 year for all ages.

Mammogram                          02/21/99 02/21/97

Health Factor: ACTIVATE BREAST CANCER SCREEN

Encounter Procedure: 76092-MAMM0GRAM, SCREENING

Women ages 50-69 should receive a mammogram every two years.

Health Factor comments: Activate health factor comments

No history of breast cancer/tumor on file.

Final Frequency and  used: 2 years for ages 50 to 69.

Radiology Procedure: 76091-MAMMOGRAM, BOTH BREASTS; MAMMOGRAM

BILAT

PPD                                N/A

Skin test: PPD

Patient may be low risk for TB, where PPD may not be indicated.

No HX of TB or positive PPD diagnosis on file.

Final Frequency and  used: 0Y - Not Indicated for all ages.

PSA                                N/A

Patient is the wrong sex for this reminder.

Seat Belt Education                DUE NOW  unknown

Seat belt education due yearly for all ages.

Final Frequency and  used: 1 year for all ages.

10:31

*********************** CONFIDENTIAL REMTEST SUMMARY ************************

PCEPATIENT,ONE        000-45-6789                        DOB:

-------------------------- CM - Clinical Maintenance ------------------------

Tobacco Cessation Education        DUE NOW unknown

Encounter Diagnosis: 305.1-TOBACCO USE DISORDER

No history of smoking found.

Patient has no history of secondary smoke inhalation.

No history of tobacco education/screen on file. Please evaluate

tobacco use and educate if currently in use.

Patient has a history of tobacco use.

Final Frequency and  used: 1 year for all ages.

Weight                             08/13/97 08/13/96

Measurement: WEIGHT; results - 103

Final Frequency and  used: 1 year for all ages.

DIABETIC FOOT EXAM                 DUE NOW  unknown

Problem Diagnosis: 250.01-DIABETES MELLI W/0 COMP TYP I

Encounter Diagnosis: 250.13-DIABETES W/KETOACID. TYPE I

Final Frequency and  used: 1 year for all ages.

--------------------------- CR - Clinical Reminders -------------------------

The following disease screening, immunization and patient education

recommendations are offered as guidelines to assist in your practice.

These are only recommendations, not practice standards. The

appropriate utilization of these for your individual patient must be

based on clinical judgment and the patient's current status.

--NEXT--  --LAST--

Exercise Education                 DUE NOW   unknown

Seat Belt Education                DUE NOW   unknown

Tobacco Cessation Education        DUE NOW   unknown

Breast Self Exam Education         DUE NOW   unknown

* END *

*(This page included for two-sided copying.)*

### Appendix A-11 - PCE/SD Debugging Utilities

The PCE/SD Debugging Utilities menu [PXQ PCE/SD DEBUGGING UTILITIES] is available from the PCE IRM Main Menu [PX IRM MAIN MENU].

Select Option: PCE IRM Main Menu  PX IRM MAIN MENU

SP     PCE Site Parameter Menu ...

TBL    PCE Table Maintenance ...

DE     PCE/SD Debugging Utilities ...

INFO   PCE Information Only ...

RM     Reminder Managers Menu ...

CR     PCE Clinical Reports ...

HOME   Directions to Patient's Home Add/Edit

CO     PCE Coordinator Menu ...

CL     PCE Clinician Menu ...

Select PCE IRM Main Menu &lt;TEST ACCOUNT&gt; Option: De PCE/SD Debugging Utilities

U      User's Visit Review

V      PCE V File Cross Reference Repair

Select PCE/SD Debugging Utilities &lt;TEST ACCOUNT&gt; Option:

The main menu for the PCE/Scheduling Debugging Utilities contains these two options. Below is a description of the options.

PXQ USER REVIEW – User’s Visit Review

This is a report of the visits and the files that store the visit-related information.

PX V File Repair – PCE V File Cross Reference Repair

This option provides a number of options that allow the user to both report on and fix broken V File Cross References.

**Note:** Caution should be exercised when using this option. Only those experienced with programming should attempt to use the PCE V File Cross Reference Repair.

Here is the User's Visit Review option and menu:

Select PCE IRM Main Menu &lt;TEST ACCOUNT&gt; Option: De PCE/SD Debugging Utilities

U      User's Visit Review

V      PCE V File Cross Reference Repair

Select PCE/SD Debugging Utilities &lt;TEST ACCOUNT&gt; Option: **U** User's Visit Review

Select one of the following:

P         Patient List of Visits

I         Internal Entry Number of VISIT

Enter '^' to exit

Select by (P)atient or (I)en: I// Patient List of Visits

Patient Name: PCEPATIENT,THIRTEEN

Enter Starting Date (eg. T-4) : JAN 1,2005//

Enter Ending Date : JAN 1,2015//

Example output:

**PAT/SEX/AGE/SSN:** PCEPATIENT,THIRTEEN **MALE    77 Years       999-99-9999**

ENCOUNTERS: ...Select an ENCOUNTER .....

**- - 28  E N C O U N T E R S - -**

No. DATE           TIME      HOSPITAL LOCATION     CATEGORY    UNIQUE I D

1   MAR 22, 2006   10:05     CHY RECORD REVIEW-X   PRIMARY         4KDF1-CHY

2   MAR 10, 2005   22:00     ZZCHY PROSTH SERVIC   PRIMARY         3X198-CHY

3   FEB 03, 2005   22:00     ZZCHY PROSTH SERVIC   PRIMARY         3V661-CHY

4   JAN 27, 2005   10:00     CHY OT EDDY           PRIMARY         3TT6T-CHY

5   JAN 10, 2005   22:00     ZZCHY PROSTH SERVIC   PRIMARY         3T08C-CHY

6   JAN 09, 2005   23:26     C MEDICINE            PRIMARY         3V0DH-CHY

7   JAN 09, 2005   10:45     C MEDICINE            PRIMARY         3V0DF-CHY

8   JAN 08, 2005   12:26     C MEDICINE            PRIMARY         3V0DB-CHY

9   JAN 07, 2005   20:38     C MEDICINE            PRIMARY         3V0D7-CHY

10  JAN 07, 2005   09:00     CHY PT ROTH           PRIMARY         3RVV5-CHY

'RETURN' to continue or '-' for previous screen

Select Encounter by entering the ITEM No. : 9

After selecting the item, select from this menu (D, A, or C):

Expanded Profile    Jul 26, 1996 08:52:10   Page:  3 of  5

Select one of the following:

D         Default (first field of each file/subfile)

A         All fields in a file/subfile (except 'NULL')

C         Customized by User (Default plus added fields)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To Customize your display use VA Fileman to add entries in file

PCE CUSTOMIZE REPORT, with your NAME, FILE/SUBFILE#s, and FIELD#s

that you want to have included in the report.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enter '^^' to exit option

Format of Print out: D// efault (first field of each file/subfile)

DEVICE: HOME// ;132;444  HOME  (CRT)

**************************************************************

***  R E C O R D    O F    R E L A T E D    E N T R I E S  ***

The Following is the VISIT file entry and

ALL records pointing back to this entry.

VISIT RECORD    --- #2022565

DATE/TIME --- JAN 07, 2005@20:38

PATIENT   --- KLANG,RODOLFO BURRI

LOCATION  --- C MEDICINE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FILE = VISIT #9000010  RECORD #2022565

VISIT/ADMIT DATE&amp;TIME       = JAN 07, 2005@20:38

DATE VISIT CREATED          = FEB 01, 2005@08:02:32

TYPE                        = VA

PATIENT NAME                = PCEPATIENT,THIRTEEN

LOC. OF ENCOUNTER           = CHEYENNE VAMC

SERVICE CATEGORY            = IN HOSPITAL

DSS ID                      = GENERAL MEDICAL

DEPENDENT ENTRY COUNT       = 3

DELETE FLAG                 =

PARENT VISIT LINK           =

DATE LAST MODIFIED          = FEB 04, 2005@10:01:34

CHECK OUT DATE&amp;TIME         =

ELIGIBILITY                 = NSC

HOSPITAL LOCATION           = C MEDICINE

CREATED BY USER             = PCECREATOR, THIRTEEN

OPTION USED TO CREATE       = PXCE ENCOUNTER ENTRY SUPER

PROTOCOL                    = PXCE SDAM STANDALONE

PFSS ACCOUNT REFERENCE      =

OUTSIDE LOCATION            =

VISIT ID                    = 3V0D7-CHY

PATIENT STATUS IN/OUT       = IN

ENCOUNTER TYPE              = PRIMARY

SERVICE CONNECTED           =

AGENT ORANGE EXPOSURE       =

IONIZING RADIATION EXPOSURE =

SW ASIA CONDITIONS          =

MILITARY SEXUAL TRAUMA      =

HEAD AND/OR NECK CANCER     =

COMBAT VETERAN              =

PROJ 112/SHAD               =

SERVICE CONNECTION EDIT FLAG =

AGENT ORANGE EDIT FLAG      =

IONIZING RADIATION EDIT FLAG =

SW ASIA CONDITIONS EDIT FLAG =

MST EDIT FLAG               =

HEAD AND NECK CANCER EDIT FLAG =

COMBAT VETERAN EDIT FLAG    =

PROJ 112/SHAD EDIT FLAG     =

COMMENTS                    =

PACKAGE                     = PCE PATIENT CARE ENCOUNTER

DATA SOURCE                 = PXCE DATA ENTRY

3M TOTAL REIMBURSEMENT      =

3M STATUS                   =

3M BILL TYPE                =

3M APG CODE                 =

3M APG TEXT                 =

3M APG WEIGHT               =

3M APC COPAY AMOUNT         =

3M APC CLAIM TYPE           =

3M APC TOTAL WEIGHT         =

3M APC HCFA AMT             =

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FILE = V PROVIDER #9000010.06  RECORD #1528925

PROVIDER                    = PCEPROVIDER,THIRTEEN

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FILE = V POV #9000010.07  RECORD #1475570

POV                         = 332.0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FILE = V CPT #9000010.18  RECORD #2557396

CPT                         = 99231

QUANTITY                    = 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The Following is the SCHEDULING VISITS file.

This is where Scheduling stores the CPT codes.

THERE ARE PROCEDURES IN PCE BUT NO RECORD IN SCHEDULING **

END OF DISPLAY

Note: the D, A, or C options produce a similar report, as does the selecting by IEN instead of Patient Name.

Now showing the PCE V File Cross Reference Repair selections:

Select PCE/SD Debugging Utilities &lt;TEST ACCOUNT&gt; Option: **V** PCE V File Cross Reference Repair

NOTES CONCERNING THIS OPTION

These options will check for broken cross-references in all of

the PCE visit files. It is interactive.

'S' will go through ONLY the 'B' X-REF of each file looking for problems.

To EXIT the program, you can enter an '^' at any prompt.

At about 1 minute intervals a message will come up telling you

how much work has already been done.

Select one of the following:

S         Screen of 4 'MAIN' files

P         Provider V PROVIDER FILE

D         Diagnosis V POV FILE

C         CPT V CPT FILE

V         Visit VISIT FILE

O         Other 6 V Files

R         Repair 4 'MAIN' V Files without prompting (automatic)

F         Fix ALL files without prompting (automatic)

Which file do you need to fix : P// **Screen** of 4 'MAIN' files

Screening the V PROVIDER file

...

- - M O N I T O R  AT 1 MINUTE- - DEC 11, 2017@12:12:11

FILE                TOTAL          #FINISHED      %COMPLETED

V PROVIDER          10342557       28002          .2707%

V POV               14562656       0              0%

V CPT               22134716       0              0%

VISIT               40190715       0              0%

NONE                4465635        0              0%.....

Looking at the Visit file:

Select PCE/SD Debugging Utilities &lt;TEST ACCOUNT&gt; Option: **V** PCE V File Cross Reference Repair

NOTES CONCERNING THIS OPTION

These options will check for broken cross-references in all of

the PCE visit files. It is interactive.

'S' will go through ONLY the 'B' X-REF of each file looking for problems.

To EXIT the program, you can enter an '^' at any prompt.

At about 1 minute intervals a message will come up telling you

how much work has already been done.

Select one of the following:

S         Screen of 4 'MAIN' files

P         Provider V PROVIDER FILE

D         Diagnosis V POV FILE

C         CPT V CPT FILE

V         Visit VISIT FILE

O         Other 6 V Files

R         Repair 4 'MAIN' V Files without prompting (automatic)

F         Fix ALL files without prompting (automatic)

Which file do you need to fix : P// **Visit** VISIT FILE

Eliminate Prompting for Confirmation?  NO//

Checking the VISIT FILE #9000010 (VISITS)

Select one of the following:

AA        AA X-REF

AAH       AAH X-REF

AD        AD X-REF

ADEL      ADEL X-REF

AET       AET X-REF

AHL       AHL X-REF

B         B X-REF

C         C X-REF

VID       VID X-REF

ALL       ALL X-REFERENCES

Select a VISIT Cross-reference: : B//

The Visit file selection (for another example):

Select PCE/SD Debugging Utilities &lt;TEST ACCOUNT&gt; Option: **V** PCE V File Cross Reference Repair

NOTES CONCERNING THIS OPTION

These options will check for broken cross-references in all of

the PCE visit files. It is interactive.

'S' will go through ONLY the 'B' X-REF of each file looking for problems.

To EXIT the program, you can enter an '^' at any prompt.

At about 1 minute intervals a message will come up telling you

how much work has already been done.

Select one of the following:

S         Screen of 4 'MAIN' files

P         Provider V PROVIDER FILE

D         Diagnosis V POV FILE

C         CPT V CPT FILE

V         Visit VISIT FILE

O         Other 6 V Files

R         Repair 4 'MAIN' V Files without prompting (automatic)

F         Fix ALL files without prompting (automatic)

Which file do you need to fix : P// **Visit** VISIT FILE

Eliminate Prompting for Confirmation?  NO//

Checking the VISIT FILE #9000010 (VISITS)

Select one of the following:

AA        AA X-REF

AAH       AAH X-REF

AD        AD X-REF

ADEL      ADEL X-REF

AET       AET X-REF

AHL       AHL X-REF

B         B X-REF

C         C X-REF

VID       VID X-REF

ALL       ALL X-REFERENCES

Select a VISIT Cross-reference: : B//

Caution should be exercised when using this option. Only those experienced with programming should attempt to use the PCE V File Cross Reference Repair.

## Appendix B - Orientation of MAS Users to PCE

Orient your MAS users to changes in their Appointment Management and Disposition functionality resulting from PCE/Scheduling integration.

Dispositions

Create a DISPOSITION CLINIC for each division in your facility using the "Set Up a Clinic" option on the Scheduling Supervisor Menu.

1. If you are a multi-divisional facility and you want to credit disposition workload for each division, set up a DISPOSITION CLINIC for each division. Make sure you define each DISPOSITION CLINIC so that it is easily associated with the division for which you want to credit workload.

1. If you are a single-division facility, you should define only one DISPOSITION CLINIC.

1. The DISPOSITION CLINICS are *only* used with Dispositions.

1. PCE recommends creating a clinic defined as Disposition, with a Stop Code number of 102. This clinic should be used with all dispositions.

1. Use "PCE Edit Disposition Clinics" option located on the "PCE Site Parameter Menu" to enter the DISPOSITION CLINICs defined for use with Dispositions for your facility. The purpose of this is to restrict the Hospital Location for a Disposition to DISPOSITION CLINICs only.

1. In single-division facilities, the hospital location for Dispositions will be stuffed automatically, and you will not be prompted to select a DISPOSITION HOSPITAL LOCATION.

***PCE Edit Disposition Clinics Example***

Select PCE Site Parameter Menu Option: PCE Edit Disposition Clinics

Select PCE PARAMETERS ONE: **1**

Select DISPOSITION HOSPITAL LOCATIONS: **?**

Answer with DISPOSITION HOSPITAL LOCATIONS

Choose from:

DISPOSITION 1

DISPOSITION 2

You may enter a new DISPOSITION HOSPITAL LOCATIONS, if you wish

Answer with HOSPITAL LOCATION NAME, or ABBREVIATION

Do you want the entire 58-Entry HOSPITAL LOCATION List? **n**

Select DISPOSITION HOSPITAL LOCATIONS: **DISPOSITION 1**

**Checkout Interview**

Checkout and Add/Edit on the Appointment Manager menu have been changed by PCE to comply with new requirements that every encounter must have a provider, diagnosis, and procedure associated with it. You will still enter the checkout information through the same menu and options, but the appearance on your computer screen changes when you get to the prompts relating to the new requirements.

You are prompted to enter Provider, Service-connection status, Diagnosis (and designate a primary diagnosis), and Procedure (or CPT codes). You may also specify if the Diagnosis is added to the patient's Problem List.

A provider key isn't required for the providers entered here.

REMEMBER: Entering one or two question marks provides help (including lists of acceptable CPT codes, Diagnoses, and Stop Codes) on how to respond to prompts.

*Steps to use the Checkout Interview:*

**1. Select Checkout Interview from the Appointment Manager Menu and select the appointment you want to check out.**

**Appt Mgt Module                       Page: 1 of  2**

Patient: PCEPATIENT,ONE (6789)                              Outpatient

Total Appointment Profile                         thru

Clinic             Appt Date/Time       Status

1   Cardiology               No Action Taken

2   Diabetes Clinic          Action Req/Checked Out

3   Old                      Checked Out

4   Cardiology               Checked Out

5   Diabetes Clinic          Checked Out

6   Cardiology               No Action Taken

**+         Enter ?? for more actions**

CI  Check In            PT  Change Patient      CO  Check Out

UN  Unscheduled Visit   CL  Change Clinic       EC  Edit Classification

MA  Make Appointment    CD  Change Date Range   PR  Provider Update

CA  Cancel Appointment  EP  Expand Entry        DX  Diagnosis Update

NS  No Show             AE  Add/Edit            DE  Delete Check Out

DC  Discharge Clinic    RT  Record Tracking     CP  Procedure Update

Appointment Lists   PD  Patient Demographics

Select Action: Next Screen// **CO=6** Check Out

**NOTE:** The response CO=6 above is a shortcut to selecting the action Check-Out (CO) and then selecting which appointment to do the Checkout on. If you only entered CO, you would then be prompted to select an appointment.

2. Answer prompts about follow-up appointment, check-out date and time, and classification.

6   Cardiology                 No Action Taken

Do you wish to make a follow-up appointment? YES// **NO**

Check out date and time:  NOW//   (JUL 29, 1996@17:54)

--- Classification --- [Required]

<!-- image -->

Was treatment related to Agent Orange Exposure? **NO**

Was treatment related to Ionizing Radiation Exposure? **NO**

Was treatment related to Environmental Contaminant Exposure? **NO**

Was treatment related to Military Sexual Trauma? **NO**

Was treatment related to Head nad/or Neck Cancer? **NO**

***You now see the new screens from PCE.***

**3. Enter all providers associated with this encounter.**

One primary provider must be designated for each encounter.

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 23, 1996@09:00        CARDIOLOGY**

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

Previous Entry:   PCEPROVIDER,ONE

**- - E N C O U N T E R  P R O V I D E R S - -**

No. PROVIDER

1   PCEPROVIDER,ONE*             PRIMARY

Enter PROVIDER: **PCEPROVIDER,TWO**

**4. Enter the diagnoses. Specify which is the primary diagnosis for this encounter, and if it should be added to the Problem List.**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 23, 1996@09:00          CARDIOLOGY**

ICD9 CODE: V70.3 --MED EXAM NEC-ADMIN PURP      PRIMARY

**- - E N C O U N T E R  D I A G N O S I S  (ICD9 CODES) - -**

No.  ICD     DESCRIPTION                                   PROBLEM LIST

**No DIAGNOSIS for this Encounter.**

Enter Diagnosis : **V70.3** --MED EXAM NEC-ADMIN PURP

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES// **[ENTER]**

Enter NEXT Diagnosis: **[ENTER]**

Would you like to add this Diagnosis to the Problem List? NO// **YES**

Enter PROVIDER associated with PROBLEM: PCEPROVIDER,ONE// **[ENTER]**

**NOTE:** If more than one diagnosis is entered, you are only prompted once, at the end, to add any of them to the Problem List.

**PAT/APPT/CLINIC:PCEPATIENT,ONE JUL 29, 1996@18:08 ADMITTING AND SCREEN**

ICD9 CODE: ...There is 1 PROVIDER associated with this encounter.

Previous Entry:   557.9

**- - E N C O U N T E R  D I A G N O S I S  (ICD9 CODES) - -**

No.  ICD     DESCRIPTION                                   PROBLEM LIST

1    446.1*  MUCOCUTAN LYMPH NODE SYN

2    557.9*  VASC INSUFF INTEST NOS

3    227.0*  BENIGN NEOPLASM ADRENAL        PRIMARY

Enter NEXT Diagnosis: [ENTER]

Would you like to add any Diagnoses to the Problem List? NO// **YES**

Select 1 or several Diagnoses (eg 1,3,4,7,3-6,2-5): 1

Enter PROVIDER associated with PROBLEM: PCEPROVIDER,TEN // **[ENTER]**

**5. Next enter the procedure(s) performed.**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 23, 1996@09:00        CARDIOLOGY**

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

**- - E N C O U N T E R  P R O C E D U R E S (CPT CODES) - -**

No. CPT CODE  QUANTITY   DESCRIPTION                   PROVIDER

Enter PROCEDURE (CPT CODE): **22600** -- NECK SPINE FUSION

How many times was this procedure performed: 1// **[ENTER]**

Enter PROVIDER associated with PROCEDURE: PCEPROVIDER,ONE // **PCEPROVIDER,TEN**

**You may enter more procedures, along with the associated provider.**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 23, 1996@09:00        CARDIOLOGY**

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT: ...There is 1 PROCEDURE associated with this encounter.

**- - E N C O U N T E R  P R O C E D U R E S (CPT CODES) - -**

No. CPT CODE  QUANTITY   DESCRIPTION                   PROVIDER

1   22600*     1         NECK SPINE FUSION             PCEPROVIDER,TEN

Enter NEXT PROCEDURE (CPT CODE): **[ENTER]**

**NOTE:** To delete Provider, Diagnosis, or Procedure entries, type @ and the number of the entry (for example, @1 would delete the NECK SPINE FUSION procedure shown above).

**6. You are then be taken back to the Scheduling screens you're familiar with.**

**Check Out                          Page:  1 of    2**

Patient: PCEPATIENT,ONE (6789)                    Clinic: ADMITTING AN

Disposition Date/Time:                Checked Out: YES

**CLASSIFICATION** [Required]

1      Treatment for SC Condition: YES

2           Agent Orange Exposure: Not Applicable

3     Ionizing Radiation Exposure: Not Applicable

4      Environmental Contaminants: Not Applicable

**PROVIDER** [Required] **DIAGNOSIS** [Required]

1  PCEPROVIDER,TEN               1  446.1     MUCOCUTAN LYMPH NODE SYN

2  557.9     VASC INSUFF INTEST NOS

3  227.0     BENIGN NEOPLASM ADRENAL

+         Enter ?? for more actions

CD  (Check Out Date)  EC  Edit Classification   PD  Patient Demographics

AP  Appointment       PR  Provider Update       RT  Record Tracking

DC  Discharge Clinic  DX  Diagnosis Update      CP  Procedure Update

AE  Add/Edit          IN  Interview

Select Action: Next Screen// DX   Diagnosis Update

NOTE: If you don't answer the Procedure prompt when you're using the Add/Edit action to add a Standalone Encounter, you will be prompted for Stop Code. If you don't enter anything at the Procedure or Stop Code prompt , you are prompted to delete the encounter.

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 29, 1996@13:00       HAND**

PROVIDER: ...Enter the provider associated with the CPT'S.....

CPT: ...There are 0 PROCEDURES associated with this encounter.

**- - E N C O U N T E R  P R O C E D U R E S (CPT CODES) - -**

No. CPT CODE  QUANTITY   DESCRIPTION                   PROVIDER

**No CPT CODES for this Encounter.**

Enter PROCEDURE (CPT CODE): **[ENTER]**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 29, 1996@13:00                HAND**

STOP CODE: ..There are 0 STOP CODES associated with this ENCOUNTER

**- - E N C O U N T E R   S T O P   C O D E S - -**

No. CODE     DESCRIPTION

**No STOP CODE for this ENCOUNTER.**

Enter a STOP CODE: **[ENTER]**

Must have a STOP CODE or a PROCEDURE to complete this action.

Do you want to delete this encounter? NO// **YES**

**Online Help for Checkout Interview**

Extensive help is available at all prompts within the Checkout Interview. The examples below demonstrate the layered structure for getting more detailed help.

NOTE that the help appears above the prompt.

**Examples of help at the Provider prompt**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 29, 1996@13:00         HAND**

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

**- - E N C O U N T E R  P R O V I D E R S - -**

No. PROVIDER

1   PCEPROVIDER,ONE              PRIMARY

Enter a PROVIDER associated with this patient ENCOUNTER.

You can enter partial names to receive a short list.

Above is a list of PROVIDERS already entered. If there are any

additional ones, they should be entered at this time.

* indicates that the entry has been visited during this session.

For more detailed HELP and selection lists enter ??

Enter PROVIDER: **?**

**- - E N C O U N T E R  P R O V I D E R S - -**

To receive detailed help for ADD or DELETE enter the following:

A   to get help on how to ADD providers.

D   to get help on how to DELETE providers.

E   to get help on how to EDIT providers.

To receive more SELECTION LISTS enter the following:

1   to get a list of ALL active providers.

2   to get a list of CLINIC providers.

3   to get a list of ENCOUNTER FORM providers.

Enter '^' to leave

Enter a letter or number for additional help: **A**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 29, 1996@13:00        HAND**

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

- - E N C O U N T E R  P R O V I D E R S - -

To ADD a PROVIDER enter one of the following:

PROVIDER NAME (eg. PCEPROVIDER,SIX)

PARTIAL LAST NAME of the PROVIDER (eg. PCE or PCEPRO)

Enter '^' to leave

Enter a letter or number for additional help: **1**

**PAT/APPT/CLINIC:  PCEPATIENT,ONE  JUL 29, 1996@13:00        HAND**

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

HELP SCREEN   - - A L L  P R O V I D E R S - -

ITEM  NAME

1     PCEPROVIDER,THREE

2     PCEPROVIDER,FOUR

3     PCEPROVIDER,FIVE

4     PCEPROVIDER,EIGHT

5     PCEPROVIDER,NINE

6     PCEPROVIDER,ELEVEN

7     PCEPROVIDER,SIX

8     PCEPROVIDER,TWELVE

9     PCEPROVIDERA,ONE

10    PCEPROVIDERA,TWO

Enter '^' to quit,  '-' for previous page.

Select a single 'ITEM NUMBER' or 'RETURN' to continue: **^**