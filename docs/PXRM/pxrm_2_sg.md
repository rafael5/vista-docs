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
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_sg.docx
status: draft
title: pxrm 2 sg.docx
---

<!-- image -->

**Clinical Reminders**

**Version 2**

**SETUP GUIDE**

**February 2005**

Updated: July 2005

Health Data Systems

**V** *IST* **A** HSD&amp;D

##### Department of Veterans Affairs

**Table of Contents**

Part I:  Introduction to Clinical Reminders V. 2.0	1

**Table of Contents**

Introduction	2

New Functionality in Clinical Reminders V. 2.0	2

Clinical Reminders V. 2.0 and This Guide	10

Purpose of This Guide	10

Other Sources of Information	10

Impact on Sites	12

Pre and Post-Installation Preparation and Setup	12

Part II: Setup Procedures	16

Chapter 1: IHD and MH Phase 2 Setup	17

1. Map local findings to the national Reminder Terms.	20
2. Run the Reminder Test option after term definition mapping is completed.	27
3. Enter data through reminder dialogs to have information  to test the extract functionality	27
4. Run a Reminders Due Report for a test period of time	27
5. Initiate a manual run from Reminder Extract Management – without transmitting.	27
6. Review the content of the Extract Summary	29
7. Run a reminder report for the patient lists created from the extract	30
8. Turn on the logical Link in the HL7 package.	30
9. Initiate the production account run of the Automatic QUERI Extracts/ Transmission.	32
10. Examine patient lists from first auto extract; run Health Summary or Reminder Reports	33
11. Review the Transmission History	33
12. After the first run is completed, review the content of the mail messages created	33

Chapter 2: GEC Setup	36

GEC Referral Reports	54

Chapter 3: CSV Changes in Reminders	56

Chapter 4: My HealtheVet	65

APPENDIX A: Hints and Tips	74

APPENDIX B: Glossary	82

Acronyms	82

National Acronym Directory	82

APPENDIX C: National Reminders Rescission	85

Appendix D: Status List Enhancements	89

Index	95

**Revision History**

| **Revision Date**   | **Page or Chapter**   | **Description**         | **Author**   |
|---------------------|-----------------------|-------------------------|--------------|
| May 2005            | Page 21               | Correction to condition |              |
|                     |                       |                         |              |

| **Introduction**   | **New Functionality in Clinical Reminders V. 2.0**  Clinical Reminders V. 2.0 (PXRM*2\_0) adds four  *new*  Ischemic Heart Disease (IHD) reminder definitions, two  *modified*  reminder definitions, modified reminder dialogs, reminder taxonomies, and reminder terms and health factors to support Phase II of the IHD project. It also redistributes three Mental Health (MH) reminder definitions, along with the reminder dialogs, reminder taxonomies, and reminder terms, and health factors to support Phase II of the MH project.  Phase II contains compliance reporting and rollup functionality for the reminders distributed in Phase I.  Also included in Version 2.0:  - Functionality for VA-GEC (Geriatric Extended Care) - Functionality for My Health *e* Vet Phase III Reminders  **Overview of Major Changes**  - **Compliance reporting and rollup functionality**  **New menus and options:**  Reminder Patient List Menu [PXRM PATIENT LIST MENU] This menu contains options for creation of term-based list rules that can be used in both extract processing and patient list creation.  Reminder Extract Menu [PXRM EXTRACT MENU]  This menu contains options that allow display and edit of extract finding rules used in the extract process and of extract parameters for use in extract processing.   |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Overview of Major Changes**   | - **Reminder Definition Enhancements**  1. Expanded and improved output format for Clinical Maintenance 2. Expanded output format in Reminder Inquiry 3. Changes to finding date search (BEGINNING DATE and ENDING date) 4. New finding modifiers 5. New finding types 6. Custom Date Due capabilities 7. More information in the Reminder Test option output  1. Occurrence Count 2. Status list (See Appendix D.) 3. CONDITION Enhancements  4. Location List finding 5. Function findings 6. Computed findings enhancements  **Other changes:**  - Historical entries are no longer flagged with an "E" following their date in the test option output, and are not shown as historical in the clinical maintenance output. - The Lab test names that are displayed now come directly from the Laboratory Test file. In V. 1.5, the national lab test name was displayed, so what you see for the name of the test may no longer match. - With the global indexes (installed with PXRM*1.5*12), we are able to make a more thorough search of the Patient Treatment File (PTF), plus we have included movement nodes for the first time. This means that for a taxonomy finding, you may find a result from PTF instead of the result from V POV or Problem List that is in your archived finding. As long as the PTF result is valid and newer than the archived result, this is okay. - In an effort to speed up taxonomy evaluation in v2.0, taxonomy expansions are loaded into memory. The upper limit for memory storage seems to be around 5,000 codes. If a large taxonomy is necessary, it could be split into pieces and included in a Reminder term. - All the national reminders that used the old MRD have been converted to use a function finding and the updated definitions are distributed in V. 2.0. Sites will need to convert their locally defined reminders. See Appendix E in the Install Guide for a detailed example.  **Example**  :  Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient:  FI(2)&amp;FI(11)&amp;(MRD(FI(2)))&gt;(MRD(FI(9)))&amp;'FI(13)  First define function finding 1 to be MRD(2)&gt;MRD(9) then change the customized cohort logic to: FI(2)&amp;FI(11)&amp;FF(1)&amp;’FI(13)   |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

- **Reminder Dialog Enhancements**
    1. New options on the Reminder Dialog Management menu: Dialog Reports ... [PXRM DIALOG TOOLS MENU]
        1. Reminder Dialog Elements Orphan Report [PXRM DIALOG ORPHAN REPORT]
        2. Empty Reminder Dialog Report [PXRM DIALOG EMPTY REPORT]
    1. Dialog overview and Dialog Summary actions added on the Dialog Edit screen on the Reminder Dialog (DI) option. These actions are available after a specific dialog is selected.
    1. New Branching/conditional logic added to dialog editing options that allows display of alternate checkboxes in dialogs, depending on whether defined conditions meet certain criteria.
- **Reminder Reports Enhancements**

Select Reminder Reports Option: d	Reminders Due Report Select an existing REPORT TEMPLATE or return to continue:

New reports on the Reminder Reports menu or changes to report functionality in Clinical Reminders V. 2.0:

Select one of the following:

- Extract Queri Totals [PXRM EXTRACT QUERI TOTALS] This option prints reminder and finding totals for extract summaries created by the automatic QUERI extracts.

I	Individual Patient

R	Reminder Patient List

- GEC Referral Report, [PXRM GEC REFERRAL REPORT] This option is used to generate GEC Reports. GEC (Geriatrics Extended Care) is used for referral of geriatric patients to receive further care.

L	Location

1. OE/RR Team
    - New type of report, Reminder Patient List, on Reminders Due [PXRM REMINDERS DUE] option. Also CR V. 2.0 will allow you to save the patient from a due report to the a patient list. From a patient list, you can print a report that display the address in a delimited format for import/export to Word labels.
        1. PCMM Provider
    T	PCMM Team
    - **Overview of Major Changes**
| **Overview of Major Changes**   | - **NOIS fixes**  More than 75 NOIS and several E3Rs have been resolved by Clinical Reminders V. 2.0.  - **E3R Enhancements**  E3R 15489	CHANGES TO REMINDER REPORT SELECTION CRITERIA  E3R #18249	NEED DESIGNATION OF PATIENT REMINDERS  “P” for patient has been added to the Usage field. This is intended for use by MyHealtheVet, but it can also be used by other packages that want to display patient reminders.  NOTE: “L” for List has also been added to the Usage field. This is intended for patient list use, and overrides other entries; i.e., if L is entered, the reminder will not show on the cover sheet in CPRS.   |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
<!-- image -->

## 1 

| **Overview of Major Changes**  During the installation of  V. 2.0, existing national reminders are rescinded, in part by renaming them ZZ*. ZZ is reserved for use as a scratch namespace (defined on FORUM, Package File). As such, sites may already have copied a reminder and used the prefix ZZ. Sites should review their local reminders, to ensure that this installation doesn’t write over any reminders.   | **Rescission of National Reminders**  The following national reminders are rescinded by changing VA to ZZVA in the name and replacing the Print Name with ZZ Print Name.  VA-*BREAST CANCER SCREEN VA-*CERVICAL CANCER SCREEN VA-*CHOLESTEROL SCREEN (F) VA-*CHOLESTEROL SCREEN (M)  VA-*COLORECTAL CANCER SCREEN (FOBT) VA-*COLORECTAL CANCER SCREEN (SIG.) VA-*FITNESS AND EXERCISE SCREEN  VA-*HYPERTENSION SCREEN VA-*INFLUENZA IMMUNIZATION VA-*PNEUMOCOCCAL VACCINE  VA-*PROBLEM DRINKING SCREEN  VA-*SEATBELT AND ACCIDENT SCREEN  VA-*TETANUS DIPHTHERIA IMMUNIZATION VA-*TOBACCO USE SCREEN  VA-*WEIGHT AND NUTRITION SCREEN  VA-ADVANCED DIRECTIVES EDUCATION VA-ALCOHOL ABUSE EDUCATION  VA-BLOOD PRESSURE CHECK VA-BREAST EXAM  VA-BREAST SELF EXAM EDUCATION VA-DIABETIC EYE EXAM  VA-DIABETIC FOOT CARE ED. VA-DIABETIC FOOT EXAM  VA-DIGITAL RECTAL (PROSTATE) EXAM VA-EXERCISE EDUCATION  VA-FECAL OCCULT BLOOD TEST VA-FLEXISIGMOIDOSCOPY  VA-INFLUENZA VACCINE VA-MAMMOGRAM  VA-NUTRITION/OBESITY EDUCATION VA-PAP SMEAR  VA-PNEUMOVAX VA-PPD  VA-PSA  VA-SEATBELT EDUCATION VA-TOBACCO EDUCATION VA-WEIGHT   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Overview of Major Changes**   | **CPRS GUI V25 Reminder Dialog Changes**  - PSI-04-001: Template field data not in final note when processing multiple dialogs. - Fixed the problem introduced with CPRS 24 that caused multiple checkboxes showing for a single element. - Reminder Dialogs will remember their last position and size. - Changed reminder dialogs to only look at the Indent Progress Note field when checking to Indent the Progress Note Text. Users will no longer have to set the “PUT A BOX AROUND THE GROUP” to yes to Indent the Progress Note text - Fixed the problem with certain historical data not updating PCE. Functional Change: changed the OR call to DATA2PCE to not sync Historical Encounter data.  Sites will need to perform clean-up to files with any historical data that has not been filed.  - Removed the Delphi code that requires users to enter Encounter data for a visit. (i.e. Service Connection)  Users can still enter encounter data in a Reminder Dialog by clicking on the Visit Info button.  - New flag added to Reminders 2.0 to control who can access the Print Now functionality for the Women’s Health Review Reminders. When Patch 1 of Clinical Reminders 2.0 is installed, the Print Now functionality will be turned off. To turn it on, the site can use the WH Print Now Active OPTION on the CPRS Reminder Configuration menu.   |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Purpose of This Guide**        | **Purpose of Clinical Reminders Setup Guide**  This Setup Guide is designed to help you prepare your site for the implementation of Clinical Reminders V. 2.0. It includes detailed information such as term mapping and extract/transmission of IHD and MH reminder data with Clinical Reminders V. 2.0.  **Our Target Audience**  We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:  - Clinical Application Coordinator (CAC) - Clinical Reminders Manager - Enterprise **V** *IST* **A** Support (EVS) - Software Quality Assurance (SQA)                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Other Sources of Information** | Refer to the Web sites listed below when you want to receive more background and technical information about PXRM V. 2.0, and to download this manual and related documentation.  **Background/Technical Information about Clinical Reminders**  From your Intranet, enter  [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders)  in the Address field to access the Clinical Reminders Main Web page.  **This Manual and Related Documentation**  From your Intranet, enter  [http://www.va.gov/vdl](http://www.va.gov/vdl)  in the Address field to access this manual, and those listed below, from the  **V**  *IST*  **A**  Documentation Library (VDL).  - Install Guide - Clinician Guide |

| **Documentation Retrieval Process**   | Your site can also retrieve the Clinical Reminders V. 2.0 documentation listed below from the following FTP addresses. The preferred method is to “FTP” the files from  [**download.vista.med.va.gov**](ftp://ftp.fo-slc.med.va.gov/)  . This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. (See the order listed below under the FTP Address column).  **Note:**  If you prefer, you can retrieve the software  *directly*  from one of the FTP Servers, listed below, under the FTP Address column.   |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

###### FTP Addresses Available for Downloading Clinical Reminders V. 2.0 Documentation

| **OI Field Office**   | **FTP Address**   | **Directory**   |
|-----------------------|-------------------|-----------------|
| Albany                | REDACTED          | REDACTED        |
| Hines                 | REDACTED          | REDACTED        |
| Salt Lake City        | REDACTED          | REDACTED        |

**Clinical Reminders V. 2.0 Documentation and Related File names**

| **Manual**                                                             | **Documentation File name**   |
|------------------------------------------------------------------------|-------------------------------|
| Installation Guide                                                     | PXRM\_2\_IG.PDF               |
| Clinician Guide                                                        | PXRM\_2\_UM.PDF               |
| Setup Guide                                                            | PXRM\_2\_SG.PDF               |
| Manager’s Manual (available within a few weeks after software release) | PXRM\_2\_MM.PDF               |

| **Impact on Sites**  Following release of the Clinical Reminders Index and Clinical Reminders 2.0, weekly support calls will be held for one month with HSD&amp;D, EVS and test sites to answer any questions field facilities may have regarding setup and installation.  NOTE: Data rollup is based on how you map your local findings to the national terms.   | **Pre and Post-Installation Preparation and Setup**  - National Reminder Rescission: Existing national reminders are renamed as part of V. 2.0 installation, using the ZZ- prefix. If you have used this prefix for local reminders, please review them to see if you will need to rename any.  - Locally created computed findings may need to be updated.  For a Computed Finding in Clinical Reminders V. 1.5 to work in Clinical Reminders V. 2.0, if a computed reminder returns a TRUE, it must also return a date.  Any sites experiencing computed finding errors with Clinical Reminders V. 1.5, should identify and fix the problems prior to installing Clinical Reminders  V. 2.0 into production.  - In V. 2.0 the Most Recent Date (MRD) functionality has been replaced with Function Findings (FF). Facilities should review their locally developed reminders and replace MRD with the new FF functionality. See the example in the Install Guide.  - Four additional reporting IHD clinical reminders are distributed in version two of Clinical Reminders (PXRM*2.0). The installation installs the reminders into the host system through the reminder exchange utility. Four GEC reminders are also installed.  - Other changes made in V. 2.0 may require modifications to some reminder definitions, related to the following:  - Statuses - Computed Findings - Conditions  - Term Mapping: As with all National Reminders, the IHD reminders are all built with reminder terms instead of individual health factors or other finding types. This allows a site to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that does not have a local finding can use the nationally distributed health factors to collect data. A detailed description of each distributed reminder’s term is included in the reminder description.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Impact on Sites**   | **Pre and Post-Installation, cont’d**  - **Term Mapping, cont’d**  Phase II reminders includes all the terms released in Phase 1, as well as four new terms introduced for the reporting reminders. The new terms will require mapping, and if your site didn’t map terms for Phase 1, many of those will also require mapping.  - Review patient lists and extract reports for reporting compliance totals using Reminder Patient List and Extract Management options.  - Set up VA Geriatric Extended Care Referral (GEC) reminders and dialogs.  - Review Code Set Versioning messages, when they are received, and determine if modifications need to be made to Reminder Taxonomies.  - QUERI extracts and transmissions  **What sites will need to do to catch up to date on the QUERI extracts and transmissions if 2.0**  **is not**  **installed into production in January 2005.**  The first extract period is January 2005, so sites have until the first 10 days to run the extract through TaskMan to be okay.  The extract parameters for VA-IHD QUERI and VA-MH QUERI will be released with the next reporting period for January 2005. So when sites run the extract for the first time using TaskMan to schedule the option, it will run the extract for January 2005. When this job is completed, the extract code will automatically change the next reporting period to February 2005. And when sites run the extract again using TaskMan to schedule the PXRM extract options, the extract will run against the month of February. So for every month that sites miss running the extract, they will need to schedule an auto-run using TaskMan and the PXRM extract options to schedule the job. They will need to do this for each month that they miss, to get caught up.   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Impact on Sites**   | **Pre and Post-Installation, cont’d**  - QUERI extracts and transmissions, cont’d  **Catching up on the QUERI extracts and transmissions: Example**  Site A - to start running extract in March  They will need to schedule the extract option using FileMan for one time before running the March job. Once the first job is completed, they will then need to schedule the recurring extract option to run once a month, starting at the beginning of March. The first job will run the extract for the month of January; when that job is completed, the extract will then be set to run for the month of February. The first job will get them caught up.  Site B - to start running extract in April,  This site will need to run two TaskMan jobs for the extract option; this will then get them caught up to start recurring jobs.  Site C – to start running extract in May  This site will need to run three TaskMan jobs for the extract option; this will then get them caught up to start recurring jobs.  If a site needs to run the extract for multiple periods to get caught up, we recommend that the site schedule the extract to run one a day for the number of days to get caught up. Once the site is caught up. the site can then reschedule the extract option to run monthly. The option to schedule a task for an option is: 'Schedule/Unschedule Options'  Option name: XUTM SCHEDULE   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Part II: Setup Procedures

| **Chapter 1: IHD and MH Phase 2 Setup**   | **Overview**  **IHD Reminder Definitions**  The following IHD reminder definitions are distributed with Version  2.0 of Clinical Reminders:  **VA-IHD LIPID PROFILE**  This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have not had a serum lipid panel within the last year. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-IHD ELEVATED LDL**  This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last year, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-*IHD LIPID PROFILE REPORTING**  This national IHD Lipid Profile Reporting reminder is used monthly to roll up LDL compliance totals for IHD patients. This reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD) who have not had a serum lipid panel/LDL (calculated or direct lab package LDL) or documented outside LDL within the last two years. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-*IHD ELEVATED LDL REPORTING**  This national IHD Elevated LDL Reporting reminder is used monthly to roll up compliance totals for management of IHD patients whose most recent LDL is greater than or equal to 120mg/dl. This national reminder identifies patients with known IHD (i.e., a documented  ICD-9 code) who have had a serum lipid panel within the last two years, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient. These compliance reminders are not for use in the Computerized Patient Record System (CPRS), so there are no related reminder dialogs.   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| NOTE: There are still discrepancies between the guidelines in these reminders and the EPRP guidelines. The QUERI group and the Reminder Definition developers are striving to reconcile the differences, as more information becomes available.   | **IHD Reminders, cont’d**  **VA-*IHD 412 LIPID PROFILE REPORTING**  This national IHD 412 Lipid Profile Reporting reminder is used monthly to roll up LDL compliance totals for IHD 412 patients. This reminder identifies patients with known IHD 412.nn (i.e., a documented ICD-9 code for IHD 412.nn) who have not had a serum lipid panel/LDL (calculated or direct lab package LDL or documented outside LDL) within the last two years. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-*IHD 412 ELEVATED LDL REPORTING**  This national IHD 412 Elevated LDL Reporting reminder is used quarterly to roll up compliance totals for management of IHD (412.nn) patients whose most recent LDL is greater than or equal to 120mg/dl. This reminder identifies patients with known IHD (i.e., a documented 412.nn ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last two years, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **Mental Health Reminders**  The following MH reminder definitions are re-distributed with Version 2 of Clinical Reminders:  **VA-ANTIPSYCHOTIC MED SIDE EFF EVAL**  The AIMS reminder has been designed to be due on all patients who are on any one of the antipsychotic medications (excluding ones like Compazine). The taxonomy for Schizophrenia is included in the reminder, but will not be part of the cohort logic. By leaving the taxonomy in the reminder, data roll-up can use the Report Extracts functionality in version 2, either with or without information on patients with Schizophrenia.  **VA-DEPRESSION SCREENING**  Screening for Depression using a standard tool should be done on a yearly basis. The yearly screening is satisfied by entry of a health factor indicating positive or negative results for the 2 question MacArthur screening tool or by entry of negative or positive results in the MH package. The reminder is also resolved by entry of information indicating that the patient is already being  treated/evaluated in a Mental Health clinic.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Mental Health Definitions (cont’d)**

**VA-DEPRESSION SCREENING, cont’d**

Patients are automatically excluded from the cohort if they have a recent diagnosis of depression (ICD code in the past 1 year) and have either a CPT code for psychotherapy in the past 3 months or are on antidepressant medication (current supply of medication in the past 3 months).

###### VA-POS DEPRESSION SCREEN FOLLOWUP

The reminder is applicable if the patient has positive depression screen in the past 1 year (VA-DEPRESSION SCREEN POSITIVE). If a more recent negative depression screen is entered, then the reminder becomes not applicable (VA- DEPRESSION SCREEN NEGATIVE).

| **Setup Steps**  **TIP:**  		See the Clinical Reminders V. 2.0  Installation Guide for install and post-install steps; for example, verifying that reminders and dialogs were installed.   | **1. Map local findings to the national Reminder Terms.**  *Option: Reminder Term Edit on the Reminder Term Management menu*  on the  *Reminder Management Menu.*  Before using IHD and MH reminders, map the local findings your site uses to represent the national reminder terms.  Phase II reminders include all the terms released in Phase I. If your site hasn’t mapped these terms, several will require mapping, and others can be mapped if needed, to use local health factors. See the examples on following pages, if you need instructions.  **a. IHD reminder terms**  Four new terms that will require mapping are introduced for the IHD reporting reminders: VA-LDL&gt;129, VA-LDL &lt;100, VA- LDL 100-119, VA-LDL 120-129  The IHD reminders use reminder terms instead of individual health factors or other finding types, which lets you continue to use findings that may already exist in your system as data elements. These local findings can then be mapped to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that doesn’t have local findings can use the nationally distributed health factors to collect data.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**IHD terms that** ***must*** **be mapped (no mapping included with distributed terms).**

| **Term**                | **Mapping Instructions**                                                                                                                                                                                                                                                                                                                                                                                               | **Local Lab Tests or Orderables to Map**   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| **VA-LDL**              | Enter the Laboratory Test names from the Lab  Package for calculated LDL and direct LDL.                                                                                                                                                                                                                                                                                                                               |                                            |
| **VA LDL**  **&lt;100** | Enter the Laboratory Test names from the Lab  Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &lt;100.                                                                                                                                                                                                                                                                               |                                            |
| **VA LDL 100- 119**     | Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a  CONDITION to identify LDL values from 100- 119.                                                                                                                                                                                                                                                                         |                                            |
| **VA-LDL &gt;119**      | Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &gt; 119. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for uses that don't involve the reminder definition. If your site uses comments frequently you may want to  change the condition to check for specific text. |                                            |

###### IHD terms that must be mapped (no mapping included with distributed terms):

| **Term**                       | **Mapping Instructions**                                                                                                                                                                                                                                                                                                                                                                                                   | **Local Lab Tests or Orderables to Map**   |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| **VA-LDL &lt; 120**            | Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &lt;120.  Although the condition is defined in the reminder, also define the condition in the term so the term can be used for purposes that don't involve the reminder definition. If your site uses comments frequently you may want to change the condition to check for  specific text. |                                            |
| **VA-LDL &gt;129**             | Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a  CONDITION to identify LDL values &gt; 129.                                                                                                                                                                                                                                                                                  |                                            |
| **VA-LDL 120-**  **129**       | Enter the Laboratory Test names from the Lab  Package for calculated LDL and direct LDL with a CONDITION to identify LDL values 120-129.                                                                                                                                                                                                                                                                                   |                                            |
| **VA-LIPID PROFILE ORDERABLE** | Add local orderable items that your site uses to order direct LDL and calculated LDL lab tests (including lipid profiles with an LDL). Add the  order dialog item to the reminder dialog definition.                                                                                                                                                                                                                       |                                            |

**Pre-mapped Terms (additional mapping optional)**

If desired, add local Health Factors or findings representing these terms.

| **Term**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                          | **Local Health Factors to Map**   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| **VA-IHD DIAGNOSIS**       | No mapping is necessary. This term is distributed pre-mapped to the VA-ISCHEMIC HEART DISEASE taxonomy. The Active Problem list, Inpatient Primary Diagnosis and  Outpatient Encounter Diagnosis are used to search for ICD9 diagnoses.                                                                                                                                                                                  |                                   |
| **VA-LIPID LOWERING MEDS** | This term is distributed pre-mapped to VA Generic Drug Names. Add any investigational drug names that are used but not mapped to the VA-Generic Drug. Enter the formulary drug names for investigation drugs.  Mapping non-investigative formulary drugs to the VA-GENERIC drugs in the Pharmacy Package will ensure the lipid lowering agents are found. The medications are informational  findings for this reminder. |                                   |

###### Pre-mapped Terms (additional mapping optional), cont’d

| **Term**                                 | **Description**                                                                                                                                                                                                                                                                                                  | **Local Health Factors to Map**   |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| **VA-LIPID LOWERING THERAPY MGMT – 2M**  | The LIPID LOWERING MEDS INITIAL ORDER and LIPID LOWERING MEDS  ADJUSTED health factors are distributed pre- mapped to this term. If necessary, add local health factors representing these terms. Do not add orders or pharmacy medications as findings for  this term.                                          |                                   |
| **VA-LIPID LOWERING THERAPY MGMT – 6M**  | The NO CHANGE IN IHD LIPID TREATMENT, OTHER DEFER ELEVATED LDL THERAPY, and LIPID MGMT  PROVIDED OUTSIDE health factors are distributed pre-mapped to this term. Add any local health factors, such as life expectancy &lt; 6 months, which your site is using that should defer  the lipid lowering management. |                                   |
| **VA-LIPID MEDS CONTRAINDI-CATED**       | Use the LIPID MEDS CONTRAINDICATED  health factor distributed with this term or add any local health factors representing contraindication to lipid lowering medications                                                                                                                                         |                                   |
| **VA-ORDER LIPID PROFILE HEALTH FACTOR** | Distributed with Health Factor: ORDER LIPID PROFILE. Add any local health factor representing the order action. Do not add orderable items to this reminder term (see VA-LIPID  PROFILE ORDERABLE).                                                                                                              |                                   |
| **VA-OTHER DEFER LIPID PROFILE**         | Distributed with Health Factor: OTHER DEFER LIPID PROFILE                                                                                                                                                                                                                                                        |                                   |
| **VA-OUTSIDE LDL &lt;100**               | Distributed with Health Factor: OUTSIDE LDL  &lt;100                                                                                                                                                                                                                                                             |                                   |
| **VA-OUTSIDE LDL &gt;129**               | Distributed with Health Factor: OUTSIDE LDL  &gt;129                                                                                                                                                                                                                                                             |                                   |
| **VA-OUTSIDE LDL 100-**  **119**         | Distributed with Health Factor: OUTSIDE LDL 100-119                                                                                                                                                                                                                                                              |                                   |
| **VA-OUTSIDE LDL 120-**  **129**         | Distributed with Health Factor: OUTSIDE LDL 120-129                                                                                                                                                                                                                                                              |                                   |
| **VA-REFUSED**  **ELEVATED LDL THERAPY** | Distributed with Health Factor: REFUSED ELEVATED  LDL THERAPY                                                                                                                                                                                                                                                    |                                   |
| **VA-REFUSED LIPID PROFILE**             | Distributed with Health Factor: REFUSED LIPID PROFILE                                                                                                                                                                                                                                                            |                                   |
| **VA-TRANSFERASE (AST) (SGOT)**          | This term was distributed originally with the Hepatitis C Risk Assessment reminder. AST tests  should already be mapped at your site.                                                                                                                                                                            |                                   |
| **VA-UNCONFIRMED IHD DIAGNOSIS**         | Use the UNCONFIRMED IHD DIAGNOSIS  health factor distributed with this term or add any  local health factor representing an unconfirmed or incorrect IHD diagnosis.                                                                                                                                              |                                   |

| **Setup Steps**   | **Example: Mapping a Local Finding to the LDL Reminder Term**  Determine all labs tests that mean “LDL” LDL (CALCULATED) DIRECT LDL  NOTE: You can’t map panels -- only individual tests. Examples:  LDL CHOLESTEROL  LDL CHOLESTEROL, PASCO LDL, DIREC  NOTE: The reminder definition “LDL” finding contains the condition "I +V&gt;0." The “+” causes the result to be treated as a number. If it’s only text, it will treat it as a zero. This condition can be added to the reminder term also, if desired, but it isn’t necessary.   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Mapping a local finding to an LDL Term**

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR CHOOSE 1-5: **4** LDL &lt;100	NATIONAL

Select Finding: **LT.LDL**

Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM) Searching for a LABORATORY TEST

1. LDL CHOLESTEROL
2. LDL-CHOL CALCULATION
3. LDL/HDL RATIO

CHOOSE 1-3: **1** LDL CHOLESTEROL

Are you adding 'LDL CHOLESTEROL' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// **Y** (Yes)

FINDING ITEM: LDL CHOLESTEROL// **&lt;Enter&gt;**

BEGINNING DATE/TIME: **&lt;Enter&gt;**

ENDING DATE/TIME: **&lt;Enter&gt;**

NATIONAL NATIONAL

NATIONAL NATIONAL

LDL 100-119

LDL 120-129

LDL &lt;100

LDL &lt;120

1

2

3

4

5

**Enter the CONDITION here,**

**if desired.**

**This is the local finding that is mapped to the national term. Note that the example uses a prefix (LT for Lab test, HF for Health Factor, etc.), which speeds up the lookup time.**

USE COND IN FINDING SEARCH: &lt;Enter&gt;

Choose from:

LT	LDL CHOLESTEROL	Finding #:

Select Finding: **&lt;Enter&gt;** Input your edit comments. Edit? NO// **&lt;Enter&gt;**

NO

OCCURRENCE COUNT: **&lt;Enter&gt;** CONDITION: I (+V&lt;100)&amp;(+V&gt;0) CONDITION CASE SENSITIVE: N

NATIONAL

LDL

Select Reminder Term Management Option: **TE** Reminder Term Edit Select Reminder Term: **LDL**

| **Setup Steps**   | **1. Map local findings to the national Reminder Terms (cont’d).**  1. **Mental Health Reminder Terms**  - VA-DEPRESSION SCREENING Terms  Sites that use a different screening tool than the 2-question MacArthur screening tool will need to create local health factors to indicate a positive or negative result and will need to map those local health factors to the national terms:  - VA-DEPRESSION SCREEN NEGATIVE - VA-DEPRESSION SCREEN POSITIVE  Reminder terms are included in this reminder to indicate if patients cannot be screened due to an acute or chronic medical condition.  - VA-ACUTE MEDICAL CONDITION - VA-CHRONIC MEDICAL CONDITION  The health factors for these terms are:  - UNABLE TO SCREEN-ACUTE MED CONDITION (resolves the reminder for 3M) - UNABLE TO SCREEN-CHRONIC MED CONDITION (resolves the reminder for1Y).  The reminder term, DEPRESSION SCREEN DONE RESULT UNKNOWN, is included for sites where a health factor or exam is being collected to indicate that depression screening is being done using an appropriate tool, but the result (positive or negative) is not being recorded. This term is included ONLY to allow sites to make the conversion to collecting positive and negative screens—any health factors or exams that a site maps to this term should NOT be included for use on any dialog or on an encounter form and should not be used in the future.   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Setup Steps**

**Map local findings to the national Reminder Terms (cont’d)**

**b. Mental Health Reminder Terms, cont’d**

- **VA-POS DEPRESSION SCREEN FOLLOWUP**

The following reminder terms are included in this reminder.

VA-ANTIDEPRESSANT MEDICATIONS VA-DEPRESSION DIAGNOSIS

VA-DEPRESSION ASSESS COMPLETED IN MHC VA-DEPRESSION ASSESS INCONCLUSIVE (? MDD) VA-DEPRESSION ASSESS NEGATIVE (NOT MDD) VA-DEPRESSION ASSESS POSITIVE (MDD)

VA-DEPRESSION SCREEN NEGATIVE VA-DEPRESSION SCREEN POSITIVE VA-DEPRESSION THERAPY

VA-DEPRESSION TO BE MANAGED IN PC VA-PSYCHOTHERAPY

VA-REFERRAL TO MENTAL HEALTH

VA-REFUSED DEPRESSION ASSESSMENT

VA-REFUSED DEPRESSION RX/INTERVENTION VA-NO DEPRESSIVE SX NEED INTERVENTION

- **VA-ANTIPSYCHOTIC MED SIDE EFF EVAL Terms**

This national reminder contains reminder terms for the positive negative evaluation for abnormal involuntary movements. If a site use a local health factor or exam or use the Simpson-Angus an record the results as a health factor, then those sites will need map the findings to the terms and add appropriate entries to the dialog to match:

VA-AIM EVALUATION NEGATIVE VA-AIM EVALUATION POSITIVE

The only findings in these reminder terms that are exported are results of the AIMS from the Mental Health package.

The reminder term VA-ANTIPSYCHOTIC MEDICATIONS contains a health factor for recording that the patient is on a de antipsychotic that is being administered in clinic from ward stock

If the medication is not dispensed from the pharmacy, then no is available to the reminder to determine that the patient is on antipsychotic unless this health factor is used.

#### MH Term Mapping

If desired, add local Health Factors, orderables, or findings representing these terms.

| **Term**                                  | **Mapping**   |
|-------------------------------------------|---------------|
| VA-ACUTE MEDICAL CONDITION                |               |
| VA-AIM EVALUATION NEGATIVE                |               |
| VA-AIM EVALUATION POSITIVE                |               |
| VA-ANTIDEPRESSANT MEDICATIONS             |               |
| VA-ANTIPSYCHOTIC DRUGS                    |               |
| VA-CHRONIC MEDICAL CONDITION              |               |
| VA-DEPRESSION ASSESS COMPLETED IN MHC     |               |
| VA-DEPRESSION ASSESS INCONCLUSIVE (? MDD) |               |
| VA-DEPRESSION ASSESS NEGATIVE (NOT MDD)   |               |
| VA-DEPRESSION ASSESS POSITIVE (MDD)       |               |
| VA-DEPRESSION DIAGNOSIS                   |               |
| VA-DEPRESSION SCREEN DONE RESULT UNKNOWN  |               |
| VA-DEPRESSION SCREEN NEGATIVE             |               |
| VA-DEPRESSION SCREEN POSITIVE             |               |
| VA-DEPRESSION THERAPY                     |               |
| VA-DEPRESSION TO BE MANAGED IN PC         |               |
| VA-NO DEPRESSIVE SX NEED INTERVENTION     |               |
| VA-PSYCHOTHERAPY                          |               |
| VA-REFERRAL TO MENTAL HEALTH              |               |
| VA-REFUSED AIM EVALUATION                 |               |
| VA-REFUSED ANTIPSYCHOTICS                 |               |
| VA-REFUSED DEPRESSION ASSESSMENT          |               |
| VA-REFUSED DEPRESSION RX/INTERVENTION     |               |
| VA-REFUSED DEPRESSION SCREENING           |               |
| VA-SCHIZOPHRENIA DIAGNOSIS                |               |

#### Example: Mapping a local finding to a Depression Screening Term

Select Reminder Term Management Option: **TE** Reminder Term Edit Select Reminder Term: VA- **DEPRESSION ASSESS POSITIVE (MDD)**

Select Finding: **HF.DEPRESSION 1+**

Are you adding ' **HF.DEPRESSION 1+** ' as a new FINDINGS (the 4th for this REMINDER TERM)? No// **Y** (Yes)

FINDING ITEM: **DEPRESSION 1+** // **&lt;Enter&gt;**

BEGINNING DATE/TIME: **&lt;Enter&gt;** ENDING DATE/TIME: **&lt;Enter&gt;** OCCURRENCE COUNT: **&lt;Enter&gt;** CONDITION: &lt;Enter&gt;

CONDITION CASE SENSITIVE: &lt;Enter&gt; USE COND IN FINDING SEARCH: &lt;Enter&gt; WITHIN CATEGORY RANK: 0//

Choose from:

HF	DEPRESSION ASSESS INCONCLUSIVE (?MDD)

Select Finding: **&lt;Enter&gt;** Input your edit comments. Edit? NO// **&lt;Enter&gt;**

Select Reminder Term: **&lt;Enter&gt;**

**This is where you enter the local finding that will be mapped to the national term. Note that the example uses a prefix (HF for Health Factor, OI for Orderable Item, etc.) for a more efficient look-up.**

| **Setup Steps, cont’d**   | 1. **Run the Reminder Test option after term definition mapping is completed.**  Review the results of patient data with each of the findings mapped to the term.  *Option: Reminder Test*  on the  *Reminder Managers Menu*  1. **Enter data through reminder dialogs to have information that can be used to test the extract functionality.**  You may also enter data through the List Manager version of CPRS or other VISTA applications, such as Lab.  1. **Run a Reminders Due Report for a test period of time to determine if the patients who are reported are appropriate.**  The report could be run for a national reminder, or create local reminders with one reminder term defined as a patient cohort finding item, then run the report to get findings by individual reminder term.  *Option: Reminders Due Report on the Reminder Reports menu*  1. **Initiate a manual run from Reminder Extract Management**  **– without transmitting.**   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

###### Example: Manual Extract

| Select Reminder Managers Menu Option:  **XM**  Reminder Extract Menu                                                                                                    |          |    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----|
| MA	Reminder Extract Management                                                                                                                                          |          |    |
| EP	Extract Parameter Management                                                                                                                                         |          |    |
| EF	Extract Finding Management                                                                                                                                           |          |    |
| EG	Extract Finding Group Management                                                                                                                                     |          |    |
| LR	List Rule Management                                                                                                                                                 |          |    |
| Select Reminder Extract Menu Option:  **MA**  Reminder Extract Management                                                                                               |          |    |
| **Extract/Transmissions Mgmt**  .	May 24, 2004@10:41:35	Page:                                                                                                           | 1 of     |  1 |
| Available Extract Parameters:                                                                                                                                           |          |    |
| Item	Extract Type                                                                                                                                                       | Class    |    |
| 1	BP READING                                                                                                                                                            | LOCAL    |    |
| 2	VA-IHD QUERI                                                                                                                                                          | NATIONAL |    |
| 3	VA-MH QUERI                                                                                                                                                           | NATIONAL |    |
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                         |          |    |
| EPM	Extract Parameter Management	QU	Quit VSE	View/Schedule Extract  Select Item: Quit// 2  Select Action:	(EPM/VSE): VSE//  **&lt;Enter&gt;**  Examine/Schedule Extract |          |    |

*Example continued next page*

| **Setup Steps, cont’d**   | **5. (cont’d) Initiate a manual run from Reminder Extract Management – without transmitting**  .   |
|---------------------------|----------------------------------------------------------------------------------------------------|

###### Example: Manual Extract

| **Examine/Schedule Extract**  May 24, 2004@10:41:48	Page:	1 of	4  Extract Type: VA-IHD QUERI Next Extract Period: M6/2001  Scheduled to Run:	View: Creation Date Order  Item	Extract Summary	Date Created	Transmission Date	Auto 1 VA-IHD QUERI 2001 M1/08	05/14/2004@15:00:42	Not Transmitted		N  3 VA-IHD QUERI 2001 M6/14	04/27/2004@11:58:53	Not Transmitted	N  7 VA-IHD QUERI 2004 M2	02/18/2004@15:04:14	03/03/2004@11:41:19	N  9 VA-IHD QUERI 2001 M6/12	02/17/2004@16:00:02	Not Transmitted	N  11 VA-IHD QUERI 2001 M6/10	12/08/2003@16:23:20	Not Transmitted	N   |    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |    |
| CV	Change View	ME	Manual Extract	TH	Transmission History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |    |
| ES	Extract Summary	MT	Manual Transmission	QU	Quit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |    |
| Select Item: Quit//  **me**  Manual Extract                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |    |
| Select EXTRACT PERIOD (Mnn/yyyy): M6/2001//  **&lt;Enter&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
| Are you sure you want to run a VA-IHD QUERI extract for M6 2001: N//  **YES**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |    |
| Transmit extract results to AAC : N//  **&lt;Enter&gt;**  O                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |    |
| Queue a Reminder Extract VA-IHD QUERI for M6/2001                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |    |
| Enter the date and time you want the job to start.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| It must be on or after 05/24/2004@14:03:36  **05/24/2004@14:04**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |    |
| Task number 5352505 queued.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |    |
| **Extract/Transmissions Mgmt.**  May 24, 2004@14:04:36	Page:	1 of                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  1 |
| Available Extract Parameters:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |    |
| Item	Extract Type	Class                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    |
| 1	BP READING	LOCAL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    |
| 2	VA-IHD QUERI	NATIONAL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    |
| 3	VA-MH QUERI	NATIONAL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |    |
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |    |
| EPM	Extract Parameter Management	QU	Quit VSE	View/Schedule Extract  Select Item: Quit// 2  Select Action:	(EPM/VSE): VSE//  **&lt;Enter&gt;**  Examine/Schedule Extract                                                                                                                                                                                                                                                                                                                                                                                                   |    |

| **Setup Steps, cont’d**   | **6. Review the content of the Extract Summary.**  Use the Reminder Extract Management option, to review extracted findings based on the reminder definitions  Check to see if the numbers match those for step 4. Alternatively, run the Reminder Report option Extract QUERI Totals or a Health Summary to review the findings extracted.   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Examine/Schedule Extract**

| Extract/Transmissions Mgmt.	May 24, 2004@14:04:47	Page:	1 of	1  Available Extract Parameters:  Item	Extract Type	Class  1. VA-IHD QUERI	NATIONAL 2. VA-MH QUERI	NATIONAL   |                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                            |                                                                      |
| EPM	Extract Parameter Management	QU	Quit                                                                                                                                   |                                                                      |
| VSE	View/Schedule Extract                                                                                                                                                  |                                                                      |
| Select Item: Quit// 1                                                                                                                                                      |                                                                      |
| Select Action:	(EPM/VSE): VSE//	Examine/Schedule Extract                                                                                                                   |                                                                      |
| Examine/Schedule Extract	May 24, 2004@14:04:47	Page:	1 of                                                                                                                  | 4                                                                    |
| Extract Type: VA-IHD QUERI                                                                                                                                                 |                                                                      |
| Next Extract Period: M6/2001                                                                                                                                               |                                                                      |
| Scheduled to Run:	View: Creation Date Order                                                                                                                                |                                                                      |
| Item	Extract Summary	Date Created	Transmission Date                                                                                                                        | Auto                                                                 |
| 1 VA-IHD QUERI 2001 M6/15	05/24/2004@14:04:19	Not Transmitted                                                                                                              | N                                                                    |
| 3 VA-IHD QUERI 2001 M1/07	04/27/2004@13:05:32	Not Transmitted                                                                                                              | N                                                                    |
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                            |                                                                      |
| CV	Change View	ME	Manual Extract	TH	Transmission History                                                                                                                   | CV	Change View	ME	Manual Extract	TH	Transmission History             |
| ES	Extract Summary	MT	Manual Transmission	QU	Quit                                                                                                                          | ES	Extract Summary	MT	Manual Transmission	QU	Quit                    |
| Select Item: Next Screen// 1                                                                                                                                               | Select Item: Next Screen// 1                                         |
| Select Action:	(ES/MT/TH): ES//	Extract Summary                                                                                                                            | Select Action:	(ES/MT/TH): ES//	Extract Summary                      |
| Extract Summary	May 24, 2004@14:05:18	Page:	1 of	2                                                                                                                         | Extract Summary	May 24, 2004@14:05:18	Page:	1 of	2                   |
| Extract Summary Name: VA-IHD QUERI 2001 M6/15                                                                                                                              | Extract Summary Name: VA-IHD QUERI 2001 M6/15                        |
| Extract Period: 06/01/2001 - 06/30/2001	Created: 05/24/2004@14:04:19                                                                                                       | Extract Period: 06/01/2001 - 06/30/2001	Created: 05/24/2004@14:04:19 |
| Item	Patient List/Station/Reminder	Total	Appl.	N/A	Due	Not Due                                                                                                             | Item	Patient List/Station/Reminder	Total	Appl.	N/A	Due	Not Due       |
| 1 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY VISIT                                                                                                                             | 1 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY VISIT                       |
| 660/VA-IHD LIPID PROFILE	2	2	0	0	2                                                                                                                                         | 660/VA-IHD LIPID PROFILE	2	2	0	0	2                                   |
| 660/VA-IHD ELEVATED LDL	2	2	0	1	1                                                                                                                                          | 660/VA-IHD ELEVATED LDL	2	2	0	1	1                                    |
| 6028/VA-IHD LIPID PROFILE	2	2	0	0	2                                                                                                                                        | 6028/VA-IHD LIPID PROFILE	2	2	0	0	2                                  |
| 6028/VA-IHD ELEVATED LDL	2	0	2	0	0                                                                                                                                         | 6028/VA-IHD ELEVATED LDL	2	0	2	0	0                                   |
| 2 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY AND ANCHOR VISIT                                                                                                                  | 2 VA-*IHD QUERI 2001 M6 PTS WITH QUALIFY AND ANCHOR VISIT            |
| 660/VA-*IHD LIPID PROFILE REPORTING	2	2	0	0	2                                                                                                                              | 660/VA-*IHD LIPID PROFILE REPORTING	2	2	0	0	2                        |
| 660/VA-*IHD ELEVATED LDL REPORTING	2	2	0	2	0                                                                                                                               | 660/VA-*IHD ELEVATED LDL REPORTING	2	2	0	2	0                         |
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                            |                                                                      |
| DPL	Display Patient List	QU	Quit DSF	Display/Suppress Finding Totals                                                                                                       | DPL	Display Patient List	QU	Quit DSF	Display/Suppress Finding Totals |

| **Setup Steps, cont’d**   | 1. **Run a reminder report for the patient lists created from the extract and compare due totals to the extract summary.**  For example, run a report for reminder VA-IHD ELEVATED LDL against patient list VA-*IHD QUERI yyyy Mnn PTS WITH QUALIFY VISIT  1. **Turn on the logical Link in the HL7 package.**  Before the IHD HL7 messages can be transmitted to Austin, each site most turn on the logical Link in the HL7 package in their production account. Enter PXRM7 at the HL LOGICAL LINK prompt, and accept the default of “Background” as the method for running the receiver.   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Setting HL Logical Link**

Method for running the receiver: B// **&lt;Enter&gt;** ACKGROUND Job was queued as 5282278.

FOREGROUND BACKGROUND QUIT

F B Q

Select HL7 Main Menu Option: **Filer** and Link Management Options

Select Filer and Link Management Options Option: **SL** Start/Stop Links

This option is used to launch the lower level protocol for the appropriate device.	Please select the node with which you want to communicate

Select HL LOGICAL LINK NODE: **PXRM7** -RECO

The LLP was last shutdown on DEC 03, 2003 15:07:47.

Select one of the following:

menu

HL7 Main Menu

Select OPTION NAME: **HL MAIN MENU**

| **Setup Steps, cont’d**   | **8. Editing the Logical Link in the HL7 package.**  If the link goes down for some reason (such as after standalone backups), check with your IRM service. You can re-set the link using the option shown on the previous page.  If you need to edit the link or reset the link to Autostart, use the “Link Edit” option, on the Interface Developer Options menu, as shown below:  For more information about Logical Links, see the VistA Health Level Seven (Hl7) Site Manager &amp; Developer Manual.   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Setup Procedures (cont’d)

| **Setup Steps, cont’d**  **TIP:**  		Programmer access is usually  required to use Taskman options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **9.	Initiate the production account run of the Automatic**  **QUERI Extracts/ Transmission.**  The automatic monthly extract of QUERI information is initiated from the options PXRM EXTRACT VA-IHD QUERI and PXRM VA-MH QUERI. These are activated through TaskMan options.  Use Schedule/Unschedule Options on the Taskman Management menu to schedule the PXRM VA-IHD QUERI and PXRM VA-MH QUERI options.  **Example: Scheduling the PXRM VA-IHD QUERI option**   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select OPTION NAME:  **XUTM MGR**  Taskman Management	menu  Schedule/Unschedule Options One-time Option Queue  Taskman Management Utilities ... List Tasks  Dequeue Tasks Requeue Tasks Delete Tasks  Print Options that are Scheduled to run Cleanup Task List  Print Options Recommended for Queueing  Select Taskman Management Option:  **Schedule/Unschedule Options**  Select OPTION to schedule or reschedule:  **PXRM EXTRACT VA-IHD QUERI**  VA-IHD QUERI Extract	run routine  Are you adding 'PXRM EXTRACT VA-IHD QUERI' as  a new OPTION SCHEDULING (the 50TH)? No//  **Y**  (Yes)  Edit Option Schedule Option Name: PXRM EXTRACT VA-IHD QUERI  Menu Text: VA-IHD QUERI Extract	TASK ID:  QUEUED TO RUN AT WHAT TIME: JAN 10,2005@00:01  DEVICE FOR QUEUED JOB OUTPUT:	Add note about what month to  QUEUED TO RUN ON VOLUME SET:	start with; also about manually running Jan, if v2 not installed  RESCHEDULING FREQUENCY: 1M	until Feb  TASK PARAMETERS:  SPECIAL QUEUEING:  **COMMAND:	Press &lt;PF1&gt;H for help	Insert** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| **Setup Steps, cont’d**  **TIP:**  	You can also get a list of the  extract totals with a new report on the Reminder Reports menu, Extract QUERI Totals.   | 1. **Examine the patient lists from the first auto extract and run either Health Summary or Reminder Reports from them.**  Check to see if the numbers match those for step 4 and step 8.  1. **Review the Transmission History.**  This displays the transmission times and individual HL7 messages and statuses for the selected extract summary.  1. **After the first run is completed, review the content of the mail messages created**  Use the “Display/Suppress Findings Totals” action on the Reminder Extract Management option to review the findings extracted based on the reminder definitions.  Make sure that the mail messages and the findings include all the correct information from the IHD and MH reminder definitions.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Display Finding Totals**

| Examine/Schedule Extract	May 24, 2004@14:53:20	Page:	1 of  Extract Type: VA-MH QUERI Next Extract Period:  Scheduled to Run:	View: Creation Date Order  Item	Extract Summary	Date Created	Transmission Date  1 VA-MH QUERI 2003 M11/04	12/18/2003@18:00:20	12/18/2003@18:00:27  2 VA-MH QUERI 2001 M10	11/26/2003@12:37:30	Not Transmitted  3 VA-MH QUERI 2003 M11/02	11/26/2003@09:43:37	Not Transmitted  4 VA-MH QUERI 2000 M2/01	09/08/2003@15:49	Not Transmitted   |                                                                      | 2  Auto N N N  N                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                      |                                                                      |
| CV	Change View	ME	Manual Extract	TH	Transmission History                                                                                                                                                                                                                                                                                                                                                                                                               | CV	Change View	ME	Manual Extract	TH	Transmission History             | CV	Change View	ME	Manual Extract	TH	Transmission History             |
| ES	Extract Summary	MT	Manual Transmission	QU	Quit                                                                                                                                                                                                                                                                                                                                                                                                                      | ES	Extract Summary	MT	Manual Transmission	QU	Quit                    | ES	Extract Summary	MT	Manual Transmission	QU	Quit                    |
| Select Item: Next Screen//  **ES**  Extract Summary                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                      |                                                                      |
| Select (s):	(1-11):  **1**                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                      |                                                                      |
| Extract Summary	May 24, 2004@14:53:35	Page:	1 of	1                                                                                                                                                                                                                                                                                                                                                                                                                     | Extract Summary	May 24, 2004@14:53:35	Page:	1 of	1                   | Extract Summary	May 24, 2004@14:53:35	Page:	1 of	1                   |
| Extract Summary Name: VA-MH QUERI 2003 M11/04                                                                                                                                                                                                                                                                                                                                                                                                                          | Extract Summary Name: VA-MH QUERI 2003 M11/04                        | Extract Summary Name: VA-MH QUERI 2003 M11/04                        |
| Extract Period: 11/01/2003 - 11/30/2003	Created: 12/18/2003@18:00:20                                                                                                                                                                                                                                                                                                                                                                                                   | Extract Period: 11/01/2003 - 11/30/2003	Created: 12/18/2003@18:00:20 | Extract Period: 11/01/2003 - 11/30/2003	Created: 12/18/2003@18:00:20 |
| Item	Patient List/Station/Reminder	Total	Appl.	N/A	Due	Not Due                                                                                                                                                                                                                                                                                                                                                                                                         | Item	Patient List/Station/Reminder	Total	Appl.	N/A	Due	Not Due       | Item	Patient List/Station/Reminder	Total	Appl.	N/A	Due	Not Due       |
| 1 VA-*MH QUERI 2003 M11 QUALIFYING PC VISIT                                                                                                                                                                                                                                                                                                                                                                                                                            | 1 VA-*MH QUERI 2003 M11 QUALIFYING PC VISIT                          | 1 VA-*MH QUERI 2003 M11 QUALIFYING PC VISIT                          |
| 660/VA-DEPRESSION SCREENING	4	4	0	2	2                                                                                                                                                                                                                                                                                                                                                                                                                                  | 660/VA-DEPRESSION SCREENING	4	4	0	2	2                                | 660/VA-DEPRESSION SCREENING	4	4	0	2	2                                |
| 660/VA-POS DEPRESSION SCREEN FOLLOWU	4	1	3	1	0                                                                                                                                                                                                                                                                                                                                                                                                                         | 660/VA-POS DEPRESSION SCREEN FOLLOWU	4	1	3	1	0                       | 660/VA-POS DEPRESSION SCREEN FOLLOWU	4	1	3	1	0                       |
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                      |                                                                      |
| DPL	Display Patient List	QU	Quit                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                      |                                                                      |
| DSF	Display/Suppress Finding Totals                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                      |                                                                      |
| Select Item: Quit//  **DSF**                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                      |                                                                      |
| DSF	Display/Suppress Finding Totals                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                      |                                                                      |
| 1 VA-MH QUERI 2000 M2 QUALIFYING VISIT                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                      |                                                                      |
| 660/VA-DEPRESSION SCREENING	1000	899	101                                                                                                                                                                                                                                                                                                                                                                                                                               | 200                                                                  | 699                                                                  |
| Finding Group: VA-DEPRESSION SCREEN NON APPLICABLE                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                      |                                                                      |
| Most recent finding patient counts for TOTAL patients                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                      |                                                                      |
| DEPRESSION DIAGNOSIS	20	20	0                                                                                                                                                                                                                                                                                                                                                                                                                                           | 20                                                                   | 0                                                                    |
| PSYCHOTHERAPY	0	0	0                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 0                                                                    | 0                                                                    |
| ANTIDEPRESSANT MEDICATION	0	0	0                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0                                                                    | 0                                                                    |
| Finding Group: VA-DEPRESSION SCREEN RESULT                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                      |                                                                      |
| Most recent finding patient counts for APPLICABLE patients                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                      |                                                                      |
| DEPRESSION SCREEN NEGATIVE	0	0	0                                                                                                                                                                                                                                                                                                                                                                                                                                       | 0                                                                    | 0                                                                    |
| DEPRESSION SCREEN POSITIVE	0	0	0                                                                                                                                                                                                                                                                                                                                                                                                                                       | 0                                                                    | 0                                                                    |
| DSF	Display/Suppress Finding Totals                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                      |                                                                      |
| Select Item: Next Screen//	NEXT SCREEN                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                      |                                                                      |
| Finding Group: VA-REFUSED DEPRESSION SCREEN                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                      |                                                                      |
| Most recent finding counts for TOTAL patients                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |                                                                      |
| REFUSED DEPRESSION SCREENING	0	0	0                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0                                                                    | 0                                                                    |

660/VA-DEPRESSION SCREEN FOLLOW UP

1000

300	700

10

690

Finding Group: VA-POS DEPRESSION SCREEN FOLLOW UP

Most recent finding patient counts for TOTAL patients

**Example: Display Finding Totals, CONT’D**

| DEPRESSION SCREEN NEGATIVE                                                                                                                                                                                                             | 0     | 0        | 0   | 0   | 0   | 0   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|----------|-----|-----|-----|-----|
| DEPRESSION ASSESS INCONCLUSIVE                                                                                                                                                                                                         | 0     | 0        | 0   | 0   | 0   | 0   |
| REFERRAL TO MENTAL HEALTH                                                                                                                                                                                                              | 0     | 0        | 0   | 0   | 0   | 0   |
| DEPRESSION TO BE MANAGED IN PC                                                                                                                                                                                                         | 0     | 0        | 0   | 0   | 0   | 0   |
| 660/VA-ANTIPSYCHOTIC MED SIDE EFF EV                                                                                                                                                                                                   | 1000  | 3        | 997 | 1   | 2   |     |
| DSF	Display/Suppress Finding Totals Select Item: Next Screen//	NEXT SCREEN  Extract Summary	Jan 08, 2003@09:49:15	Page:	3 of	3  Extract Summary Name: VA MH QUERI 2000 M2  Extract Period: 02/01/2000 - 02/28/2000	Created: 01/03/2003 |       |          |     |     |     |     |
| +Item	Patient List/Station/Reminder                                                                                                                                                                                                    | Total | Appl.    | N/A | Due | Not | Due |
| Finding Group: VA-ANTIPSYCHOTIC DRUGS  Most recent finding patient counts for                                                                                                                                                          | TOTAL | patients |     |     |     |     |
| AIM EVALUATION NEGATIVE                                                                                                                                                                                                                | 0     | 0        | 0   | 0   |     | 0   |
| AIM EVALUATION POSITIVE                                                                                                                                                                                                                | 0     | 0        | 0   | 0   |     | 0   |
| REFUSED ANTIPSYCHOTICS                                                                                                                                                                                                                 | 0     | 0        | 0   | 0   |     | 0   |
| REFUSED AIM EVALUATION                                                                                                                                                                                                                 | 0     | 0        | 0   | 0   |     | 0   |

**+ Next Screen	- Prev Screen	?? More Actions**

Select Item: Quit//	Quit

QU	Quit

DPL	Display Patient List

DSF	Display/Suppress Finding Totals

**Chapter 2: GEC Setup**

**Setting up VA-Geriatric Extended Care (GEC) Referral**

Clinical Reminders V. 2.0 includes a nationally standardized computer instrument called VA Geriatric Extended Care (GEC), which replaces paper forms for evaluating veterans for extended care needs. Paper forms that facilities use include VA Form 10-7108, VA Form 10064a- Patient Assessment Instrument (PAI), and VA Form 1204-Referral for Community Nursing Home Care (others sites use various instruments including consults).

**NOTE** : GEC Referral is a screening tool for the purpose of evaluating a patient’s needs for extended care and is not to be used as the document to refer or place a patient. The document should be part of a packet of information obtained when placing a patient. Therefore, it will not provide all of the information needed for referrals.

**Setup Summary Steps**

Four different disciplines should complete the screening, making it less burdensome on any one individual.

1. Create a GEC Consult Service or identify which existing consult service will be used for GEC.
2. Add the GEC Consult to ALL SERVICES
3. Create a GEC Quick Order
4. Set the parameter TIU TEMPLATE REMINDER DIALOGS.
5. Create a Parent Note Title
6. Create four Child Note Titles
7. Associate the four note titles with the GEC dialogs
8. Set GEC Status Check parameter.

***See detailed descriptions on the following pages.***

1. 

| **Chapter 2: GEC Setup, cont’d**  NOTES:  - Dialog elements that have an order associated as a finding item will continue to be editable fields using the dialog editor. - Any local changes to the GEC dialogs will not be included with the reports or future national extracts. - GEC health factors are populated with a synonym for identification. - Although it’s technically possible, sites should not use the GEC health factors elsewhere. Phase II of the GEC project will involve national roll-up. Potential extraction rules may not be able to distinguish the data source. - Users should not enter GEC health factors from the Encounter form. While it is possible to do so, Patient Care Encounter only allows one instance of a combination of the health factor, patient, and visit IEN. If one is entered via the Encounter, any subsequent entry of that health factor from the reminder dialog will not be available for the GEC reports. This is a consequence of the GEC report routines relying on the health factor’s Data Source.   | **Overview of VA-Geriatric Extended Care (GEC)**  **Basics**  The GEC Referral is comprised of four reminder dialogs: VA-GEC SOCIAL SERVICES, VA-GEC NURSING ASSESSMENT, VA- GEC CARE RECOMMENDATIONS, and VA-GEC CARE  COORDINATION. These dialogs are designed for use as TIU templates to enter data regarding the need for extended care. Data entered via the dialogs are captured as health factors to be used for local and national reporting.  The software also includes a new report menu that may be used for local analysis.  **GEC Health Factors**  The GEC Referral project distributes a large set of national health factors. They may be identified by the GEC namespace and constitute the foundation of the GEC Referral project. They establish a standard set of screening data, to be used across the Veterans Health Administration, and will be rolled-up nationally.  The Health Factor files include factors and categories. All factors must belong to a category. For this project, each section of the Referral is correlated to a health factor category. Once entered, the data is stored in the Patient Care Encounter files. The structure of these underlying files has a direct impact on the design of the GEC software. Extracting, viewing, and managing this set of data requires the GEC dialogs to remain as they are released.  Consequently, the Clinical Reminders package has been modified to prevent the GEC national reminders from being copied. This change was made to the Reminder Dialog, Dialog Group, and Dialog Element levels. To accommodate local business practices, sites will be permitted to add locally created health factors to the GEC dialogs. The LM Dialog Editor (Dialog Edit List) will display differently when editing national dialogs that have been locked.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Overview, cont’d**  **TIP:**  	NOTE: The Supply section of the VA-GEC  NURSING ASSESS-  MENT dialog does not have health factors associated. As a result, they will not be available on the GEC Report menu options.  Sites can modify dialogs to accommodate local business practices. Sites may add locally created health factors to the GEC dialogs.   | **GEC Referral Reminders and Dialogs**  The GEC reminders are comprised of dialogs and health factors only. They have neither cohort nor resolution logic, and will not become due. They are intended only as TIU templates and do not need to be assigned to the CPRS Cover Sheet. Due to potential complications with reporting and duplicate entries, it is recommended that the GEC dialogs not be added to the Reminders drawer/Cover sheet. The Referral was designed for inter-disciplinary use with dialogs created for separate services. However, a single user may perform them all. With only a few exceptions, each section of the dialogs is mandatory and is marked with an asterisk (*). The completion of all four dialogs constitutes a discrete episode of the GEC Referral.  The VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC  REFERRAL CARE RECOMMENDATIONS dialogs comprise the clinical screening. The VA-GEC REFERRAL CARE COORDINATION dialog is used administratively to record the arrangement of and funding for extended care services. These dialogs may be performed in any order that local practices dictate. However, it is expected the screening portion will be completed prior to the coordination of services. When the screen is complete, a consult order should be placed to the service responsible for arranging services.  **GEC Consult Order**  Most sites have either an individual or a service responsible for arranging and coordinating extended care services. To accommodate local business practices and flexibility, sites may associate any consult service (or menu) they already have in place. If none exist, the sites may create a consult or establish some alternative practice to ensure that services are arranged and that the VA-GEC REFERRAL CARE COORDINATION dialog is  completed.  A placeholder for this consult is included at the end of the VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC REFERRAL CARE  RECOMMENDATIONS dialogs. It must be substituted or deleted at the time of installation.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Overview, cont’d**  **TIP:**  	If a consult quick order isn’t available  at the time of the installation of Clinical Reminders V. 2.0, the installer will need to enter a dummy, placeholder name.   | **Overview, cont’d Setup Steps**  **1. Set up a GEC Consult Service**  - Determine if a Consult Service exists for the management of extended care services. - Create a consult quick order using the “Enter/Edit Quick Orders” option on the Order Management Menu [ORCM MENU]. This order should be associated to the Consult Service in the Consult to Service/Specialty field of the quick order.  1. If it exists, this service can be used for the quick order and you can proceed to step 2. 2. If one does not exist, create a Consult Service by using the [GMRC Manager] option [GMRC SETUP REQUEST SERVICES]. After creating the consult service, add the new consult service to ALL SERVICES. 3. Recipients of the consult notifications should be GEC staff responsible for coordinating extended care service (or any appropriate tester).  - Provide the name of the consult quick order to the installer. The installer will then perform the installation and enter the name of the order at the prompt as above.  - Sites will need to review the privileging status of those performing the GEC Referral. The staff assigned to place the consult order associated with the GEC dialogs will require the ability to place a consult order. (signature or release).  NOTE: If this consult quick order isn’t available at the time of the installation of Clinical Reminders V2.0, the installer will need to enter a dummy name as a placeholder.  ***See the examples on the following pages for creating a consult service and a consult quick order.***   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Consult Tracking Reports ... Set up Consult Services Service User Management Consult Service Tracking Pharmacy TPN Consults

Print Test Page

Group update of consult/procedure requests Determine users' update authority

Determine if user is notification recipient Determine notification recipients for a service Test Default Reason for Request

List Consult Service Hierarchy Setup procedures

Copy Prosthetics services Duplicate Sub-Service

IFC Management Menu ...

RPT SS SU CS RX TP GU UA UN NR TD LH PR CP DS IFC

| **Chapter 2: GEC Setup, cont’d**   | **1. (cont’d) Set up Consult Services**  Follow the example below to set up a consult service.   |
|------------------------------------|--------------------------------------------------------------------------------------------------|

CO

DEFAULT REASON FOR REQUEST:

No existing text Edit? NO// **&lt;Enter&gt;**

RESTRICT DEFAULT REASON EDIT: **&lt;Enter&gt;**

Inter-facility information IFC ROUTING SITE: **&lt;Enter&gt;** IFC REMOTE NAME: **&lt;Enter&gt;** Select IFC SENDING FACILITY:

SERVICE INDIVIDUAL TO NOTIFY: **CRPROVIDER,ONE** Select SERVICE TEAM TO NOTIFY: **&lt;Enter&gt;** Select NOTIFICATION BY PT LOCATION: **&lt;Enter&gt;** PROCESS PARENTS FOR NOTIFS: **&lt;Enter&gt;**

Select UPDATE USERS W/O NOTIFICATIONS: **&lt;Enter&gt;** Select UPDATE TEAMS W/O NOTIFICATIONS: **&lt;Enter&gt;** Select UPDATE USER CLASS W/O NOTIFS: **&lt;Enter&gt;** Select ADMINISTRATIVE UPDATE USER: **&lt;Enter&gt;** Select ADMINISTRATIVE UPDATE TEAM: **&lt;Enter&gt;** PROCESS PARENTS FOR UPDATES: **&lt;Enter&gt;**

| **Chapter 2: GEC Setup, cont’d**   | **Set Up Consult Services, cont’d**   |
|------------------------------------|---------------------------------------|

| **Chapter 2: GEC Setup, cont’d**   | **2. Add the GEC Consult Service to ALL SERVICES**  When you create a new service, it is  *not*  automatically linked into the Consults hierarchy. You must explicitly group each service under ALL SERVICES or under another service that in turn is grouped under ALL SERVICES. Until this is done, the new service is not visible in the service hierarchy and cannot be selected for any action.  Use the Set Up Consult Services (SS) action to group services   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Grouping the Extended Care service under ALL SERVICES**

RPT	Consult Tracking Reports ... SS	Set up Consult Services

SU	Service User Management CS	Consult Service Tracking RX	Pharmacy TPN Consults

TP	Print Test Page

GU	Group update of consult/procedure requests UA	Determine users' update authority

UN	Determine if user is notification recipient

NR	Determine notification recipients for a service TD	Test Default Reason for Request

LH	List Consult Service Hierarchy PR	Setup procedures

CP	Copy Prosthetics services DS	Duplicate Sub-Service

IFC	IFC Management Menu ...

Select Consult Management Option: **ss** Set up Consult Services Select Service/Specialty: **ALL SERVICES** GROUPER ONLY

SERVICE NAME: ALL SERVICES// **&lt;Enter&gt;** ABBREVIATED PRINT NAME (Optional): **&lt;Enter&gt;** INTERNAL NAME: **&lt;Enter&gt;**

Select SYNONYM: ALL// **&lt;Enter&gt;**

SERVICE USAGE: GROUPER ONLY// **&lt;Enter&gt;**

SERVICE PRINTER: **&lt;Enter&gt;** NOTIFY SERVICE ON DC: **&lt;Enter&gt;** REPRINT 513 ON DC: **&lt;Enter&gt;** PREREQUISITE:

No existing text Edit? NO// **&lt;Enter&gt;**

PROVISIONAL DX PROMPT: **&lt;Enter&gt;** PROVISIONAL DX INPUT: **&lt;Enter&gt;** DEFAULT REASON FOR REQUEST:

No existing text Edit? NO// **&lt;Enter&gt;**

RESTRICT DEFAULT REASON EDIT: **&lt;Enter&gt;**

Inter-facility information IFC ROUTING SITE: **&lt;Enter&gt;** IFC REMOTE NAME: **&lt;Enter&gt;**

Select IFC SENDING FACILITY: **&lt;Enter&gt;**

menu

GMRC MGR	Consult Management

| **Chapter 2: GEC Setup, cont’d**   | **Set Up Consult Services – linking to ALL SERVICES, cont’d**   |
|------------------------------------|-----------------------------------------------------------------|

| **Chapter 2: GEC Setup, cont’d**   | **3. Create Consult Order**  Use the Order Menu Management option on the CPRS Configuration menu to create a consult order.   |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

**Example: Creating Consult Order**

Select CPRS Manager Menu Option: **PE** CPRS Configuration (Clin Coord)

AL	Allocate OE/RR Security Keys KK	Check for Multiple Keys

DC	Edit DC Reasons

GP	GUI Parameters ...

GA	GUI Access - Tabs, RPL MI	Miscellaneous Parameters

NO	Notification Mgmt Menu ... OC	Order Checking Mgmt Menu ... MM	Order Menu Management ...

LI	Patient List Mgmt Menu ... FP	Print Formats

PR	Print/Report Parameters ... RE	Release/Cancel Delayed Orders US	Unsigned orders search

EX	Set Unsigned Orders View on Exit NA	Search orders by Nature or Status DO	Event Delayed Orders Menu ...

PM	Performance Monitor Report

Select CPRS Configuration (Clin Coord) Option: **MM** Order Menu Management OI	Manage orderable items ...

PM	Enter/edit prompts

GO	Enter/edit generic orders QO	Enter/edit quick orders ST	Enter/edit order sets

AC	Enter/edit actions

MN	Enter/edit order menus

AO	Assign Primary Order Menu CP	Convert protocols

SR	Search/replace components LM	List Primary Order Menus

DS	Disable/Enable order dialogs CU	Manage Consult Order Urgencies

CS	Review Quick Orders for Inactive ICD9 Codes

Select Order Menu Management Option: **QO** Enter/edit quick orders Select QUICK ORDER NAME: **GMRCT GEC REFERRAL**

Are you adding 'GMRCT GEC REFERRAL' as a new ORDER DIALOG? No// **Y** (Yes) TYPE OF QUICK ORDER: **CONSULTS**

NAME: GMRCT GEC REFERRAL// **&lt;Enter&gt;**

DISPLAY TEXT: **GEC REFERRAL**

VERIFY ORDER: **&lt;Enter&gt;**

| **Chapter 2: GEC Setup, cont’d**   | **Create Consults Order, cont’d**   |
|------------------------------------|-------------------------------------|

###### Example, cont’d

DESCRIPTION:

No existing text Edit? NO// **YES**

**“TO PLACE GEC REFERRAL CONSULT.”**

ENTRY ACTION:

Consult to Service/Specialty: **GEC REFERRAL**

Consult Type: **&lt;Enter&gt;**

Reason for Request: No existing text Edit? No// **Y** (Yes)

Please evaluate referral and make appropriate arrangements for care. Category: **&lt;Enter&gt;**

Urgency: ROUTINE// **&lt;Enter&gt;** Place of Consultation: **&lt;Enter&gt;** Attention: **&lt;Enter&gt;**

Provisional Diagnosis: **&lt;Enter&gt;**

Consult to Service/Specialty: GEC REFERRAL

Reason for Request: Please evaluate referral and make approp ...

Urgency: ROUTINE

(P)lace, (E)dit, or (C)ancel this quick order? PLACE// **&lt;Enter&gt;**

Auto-accept this order? NO// **&lt;Enter&gt;**

| **Chapter 2: GEC Setup, cont’d**   | 1. **Set the parameter TIU TEMPLATE REMINDER DIALOGS**  - To use a GEC dialog as a TIU template, use TIU TEMPLATE REMINDER DIALOGS on the General Parameter Tools menu (XPAR) - Add the dialog name to be associated with the template   |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Select Systems Manager Menu Option: **^TOOL** General Parameter Tools

LV	List Values for a Selected Parameter LE	List Values for a Selected Entity

LP	List Values for a Selected Package LT	List Values for a Selected Template EP	Edit Parameter Values

ET	Edit Parameter Values with Template EK	Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP	Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: TIU TEMPLATE REMINDER DIALOGS	Reminder Dialogs

allows as Templates

TIU TEMPLATE REMINDER DIALOGS may be set for the following:

|   1 | User     | USR   | [choose from NEW PERSON]      |
|-----|----------|-------|-------------------------------|
|   3 | Service  | SRV   | [choose from SERVICE/SECTION] |
|   4 | Division | DIV   | [choose from INSTITUTION]     |
|   5 | System   | SYS   | [XSYSTEM.MED.VA.GOV]          |

Enter selection: 5	System	XSYSTEM.MED.VA.GOV

Select Display Sequence: ? Display Sequence	Value

5	VA-GEC REFERRAL SOCIAL SERVICES

10	VA-GEC REFERRAL NURSING ASSESSMENT

15	VA-GEC REFERRAL CARE RECOMMENDATION

Select Display Sequence: 20

Are you adding 20 as a new Display Sequence? Yes// **&lt;Enter&gt;** YES

Display Sequence: 20// **&lt;Enter&gt;** 20

Clinical Reminder Dialog: VA-GEC REFERRAL CARE COORDINATION	reminder dialog NATIONAL

| **Chapter 2: GEC Setup, cont’d**  **TIP:**  	Refer to Appendix  C in the TIU/ASU  Implementation Guide for complete instructions for creating &amp; implementing Interdisciplinary Notes   | 1. **Create a Parent Note Title**  **GEC Interdisciplinary Notes**  The GEC Referral dialogs are intended for use as TIU templates. It is also expected that they will be used as part of a TIU Interdisciplinary (ID) note. This will require new TIU Document Definitions or the association of existing titles to the dialogs. This project does not stipulate the titles to be used, preferring to allow the sites to use those titles that would best suit their business practices. However, the Office of Geriatrics Extended Care strongly recommends that the parent ID note title be:  “GEC EXTENDED CARE REFERRAL”  Set up a standard parent note title for use as an interdisciplinary note for GEC. For guidance on interdisciplinary notes and business rules to support them, see the  *TIU/ASU Implementation Guide*  , Appendix C, Interdisciplinary Notes Setup Guide.  1. **Create four Child Note Titles**  Make up four note titles and associate them with each new clinical reminder template. These will be child note titles. Child note titles in support of GEC are completely at the discretion of the local site.  This screen shot shows the titles used in the development account.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Example: GEC Note Titles

**CRPROVIDER,ONE,MD**

| **Chapter 2: GEC Setup, cont’d**   | 1. **Associate the four note titles with the GEC dialogs** (NOTE: requires membership in the Clinical Application Coordinator User Class.)  To associate a dialog with a note title:  1. Open the Notes tab 2. Click on the Options menu 3. Select Edit Shared Templates 4. Highlight “Document Titles” 5. Click New Template 6. Enter name 7. Select reminder dialog as Type 8. Enter dialog name 9. Enter note title in Associated Title field.   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Associating Dialog with Note Title**

| **Chapter 2: GEC Setup, cont’d**   | 1. **(cont’d ) Associate note titles with the GEC dialogs**  When you get to the template editor, choose Document Titles from the Shared Template hierarchy:  <!-- image -->  Select New Template and create a new template. Enter or select the following:  - Name - Select Reminder Dialog as the Template Type. - Select the GEC Reminder dialog from the drop-down list  <!-- image -->   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Setup, cont’d**  NOTE: The VA-GEC Referral Care Coordination dialog will be distributed with a TIU Object. The object, &#124;VA-GEC STATUS&#124;, will provide the user a real-time view of the current Referral’s dialog- completion status. It will present information similar to that found on the GEC Referral Status Display and can be used to determine if the Referral can be finalized. The object has been placed into a dialog element and can be viewed by clicking the checkbox.   | **8. Set the GEC Status Check**  There is no limit to the entry of GEC Referral data. Since there may be multiple entries of the same health factors over time, and since the data is entered via separate dialogs, extraction and viewing requires the data to be discretely identified. The GEC software depends upon the user to indicate when the data from a given referral should be concluded. The referral is finalized using a new feature called the GEC Status Indicator. This indicator is presented to the user as a modal dialog at the conclusion of the VA-GEC CARE COORDINATION dialog. It will prompt the user to indicate the conclusion of the Referral with a Yes or No response and will list any missing dialogs. If Yes is selected, the data for the current episode of the Referral is closed. If No is selected, the Indicator is displayed and the data entered will be included with the current episode of the Referral. The Indicator will then be displayed with each succeeding GEC dialog until Yes is selected.  To assist the ongoing management of completing GEC Referrals, the GEC Status Indicator may be added to the CPRS GUI Tools drop-down menu. It may be set at the User or Team level. If added to the drop-down menu, the Indicator may be viewed at any time and used to close the referral if needed. GEC Status Check has been added to the CPRS Reminder Configuration menu on the Reminder Management Menu.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

###### Example: Adding Status Indicator to CPRS Tools Menu

WH	WH Print Now Active

Select CPRS Reminder Configuration Option: **gec** GEC STATUS CHECK ACTIVE

GEC STATUS CHECK may be set for the following:

1. User	USR	[choose from NEW PERSON]
2. Team	TEA	[choose from TEAM]

Enter selection: **1** User	NEW PERSON

Select NEW PERSON NAME: **CRPROVIDER,ONE** PO

---------- Setting PXRM GEC STATUS CHECK	for User: CRPROVIDER,ONE ----------

GEC Status Check: YES// **&lt;Enter&gt;**

Add/Edit Reminder Categories CPRS Lookup Categories

CPRS Cover Sheet Reminder List Mental Health Dialogs Active Progress Note Headers

Reminder GUI Resolution Active Default Outside Location Position Reminder Text at Cursor New Reminder Parameters

GEC Status Check Active

CA CL CS MH PN RA DL PT NP GEC

Select Reminder Managers Menu Option: **cp** CPRS Reminder Configuration

| **Chapter 2: GEC Setup, cont’d**  **TIP:**  	NOTE: The Indicator is used  to control the bundling of GEC data for reporting purposes and does not alter the behavior or actions of either Text Integration Utility or Patient Care Encounter.   | **Setting up VA-Geriatric Extended Care (GEC) Referral**  **GEC Status Check, cont’d Status Indicator Instructions**  This section is provided to illustrate the purpose and use of the GEC Status Indicator.  A GEC referral consists of four dialogs and is considered complete when all four are finished. Since a referral may be performed more than once, over time, using the same health factors, responses must be collected as discrete episodes in order to create meaningful reports. The software requires the user to finalize the referral and indicate that it is complete. The referral is finalized using the GEC Status Indicator. This Indicator is available to users upon completion of the GEC Care Coordination dialog. It is also available from the Tools drop-down menu if assigned.  The standard and expected course of events is for a user(s) to perform the Social Services, Nursing Assessment and Care Recommendations dialogs before the Care Coordination dialog. In that case, the Status Indicator first appears after the user has clicked the FINISH button on the Care Coordination dialog. It will prompt the user to indicate that the referral is complete.  If all the dialogs have been completed, the user may select Yes and the current episode of the referral will be closed to any additional data. If any of the other dialogs are missing, the user should select No. This will inform the system to continue collecting responses entered from the dialogs. Each subsequent selection of the FINISH button on the GEC dialogs will display the Status Indicator again, providing the opportunity to close the current episode of the referral. Any entry of a GEC dialog after the Yes button is selected initiates a new episode of the referral.  Alternatively, if the user selects Yes, then deletes the note and performs the dialog again, a new episode of the referral will be initiated. The same result will occur if a GEC dialog is performed from the Reminders drawer. (Due to the risks associated with this process, it is recommended that the GEC dialogs not be added to the Reminders drawer in CPRS).   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Setup, cont’d**  **TIP:**  	NOTE: The Indicator is used  to control the bundling of GEC data for reporting purposes and does not alter the behavior or actions of either Text Integration Utility or Patient Care Encounter.   | **Setting up VA-Geriatric Extended Care (GEC) Referral**  **GEC Status Check**  **Status Indicator Instructions, cont’d**  The Yes button should only be selected if the user is certain no changes are needed and they are ready to commit to the note’s authentication.  The Status Indicator does not update after the referral has been completed. Put another way, once a referral has been closed, it cannot be reopened. This same risk exists if a note is deleted after the Yes button has been selected and the user then reenters the dialog.  Users should  *always*  check the Status Indicator when a new referral is initiated on a patient. Doing so will provide the opportunity of closing any previous referral inadvertently left open.  **Example of Status Indicator when all dialogs are complete.**  <!-- image -->   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Setup, cont’d**   | **Setting up VA-Geriatric Extended Care (GEC) Referral**  **GEC Status Check**  **Status Indicator Instructions, cont’d**  **Example of Status Indicator when some dialogs are missing.**  <!-- image -->  **GEC Referral Ad hoc Health Summaries**  Two new health summary components are distributed with this software:  - GEC Completed Referral Count (GECC) - GEC Health Factor Category (GECH)  The first displays all GEC referral data according to the occurrence and time limits identified. The GEC Health Factor Category component, in conjunction with PX*1*123 and GMTS*2.7*63, permits GEC data to be viewed by health factor or health factor category. If a user should have access to these GEC reports, they must have access to the Ad Hoc Health Summary type. (This can be set using GMTS GUI HS LIST PARAMETERS.)   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: GEC Setup, cont’d**   | **GEC Referral Reports**  The software includes a new set of reports that provide a variety of GEC health factor perspectives. The reports are released as an option within the Clinical Reminder namespace and may be assigned as necessary. The option is GEC Referral Report [PXRM GEC REFERRAL REPORT] and is on the PXRM MANAGERS  MENU. The reports capture data elements for reporting and tracking use of the GEC Referral Screening Tool. The reports may be generated in formatted or delimited output. The Summary (Score) report provides summary (calculated) totals from specific sections of the screening tool identified by the Office of Geriatrics Extended Care.  **GEC Reminder Terms**  Phase I of the GEC Referral project distributes a set of terms that will be used with Phase II. Since Phase II has not yet been initiated, the functional requirements and design have not been identified.  However, it is expected to include the national roll-up of GEC screening data using the Generic Extract Utility released concurrently with Clinical Reminders V. 2.0. To allow the greatest degree of flexibility in design, one reminder term is released for each GEC Referral health factor. The terms are mapped to the health factors on the VA-GEC REFERRAL reminder dialogs. The terms will be installed silently and reside dormant until Phase II of the GEC Referral project is implemented. The Reminder Definitions used to install these terms will be deleted after installation.  **Training**  The Office of Geriatric Extended Care (OGEC) will establish a web site to provide training on the GEC screening tool. This training module is being developed with assistance from Employee Education Service and built by ImageITS, a private firm. The module will consist of an interactive tutorial and reference material. OGEC will coordinate the training initiative and serve as the custodian of the web site’s content. Facilities may contact Employee Education Service or its website’s URL or for more information (vaww.ees.aac.va.gov).  The catalog # is PTCAR-EES-G152. The title is “Geriatric Referral Form.”   |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: Code Set Versioning**   | **Chapter 3: CSV Changes in Reminders**  Several changes and enhancements are included in Clinical Reminders  V. 2.0 in support of Code Set Versioning, mandated under the Health Information Portability and Accountability Act (HIPAA). The changes will insure that active ICD9, ICD0, and CPT codes are selectable in the CPRS GUI application while using Clinical Reminder Dialogs. It will also produce several email messages to the site users to help in deciding the correct usage of these codes in the Taxonomies and Dialogs.  PXRM*1.5*18, which contained the CSV changes, was previously released in conjunction with CSV\_UTIL V. 1, Code Set Versioning, which contains routines, globals, and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD-9-CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, the Lexicon will allow translation of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO) established specific code that existed on that event date.  Version 2 of Clinical Reminders includes all of the CSV changes contained in patch 18.   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: CSV, cont’d**  **Code Text Descriptors**  At the time that CSV I was developed, a request was made to defer applicable text versioning to the next iteration, since many of the existing code set databases were not designed to store more than one description for each code. The current processes allow textual descriptions to be overwritten in the files. The follow-up project, Code Text Descriptors, adds the functionality of date-sensitive versioning for all applicable code text descriptors for the four code sets, effective with all textual changes occurring since October 1, 2002. Consistent with the new HIPAA requirements, this project will include expanding the storage of more than one description for each code in the HIPAA code set along applicable versioned dates when the code change occurs.   | **What do sites need to do?**  No setup is required initially for the CSV changes. The Clinical Reminders application has been modified so that Clinical Application Coordinators (CACs) can identify ranges of codes where the adjacent values have changed because of a code set versioning update. A new option and several wording and format changes appear in taxonomy and dialog options.  **Changes in Clinical Reminders:**  **1. Mail Messages (List Manager and GUI)**  After Version 2 of Reminders is installed, you will start receiving mail messages about taxonomy/code updates and Reminder Dialog ICPT Code changes.  Those individuals assigned to the Reminders mail group at your site will receive the messages.  ***NOTE: This mail group must be designated as Public***  .  These updates normally occur quarterly, so you shouldn’t receive these continuously.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: CSV, cont’d**   | **CSV Changes in Reminders**  **2. Taxonomy option changes**  :  - New Reminder Taxonomy Inquiry  The following is an example of the new inquiry format (using the option “Inquire about Taxonomy Item”). The ranges for a code set will only be displayed if the taxonomy has a code range defined in the selected taxonomy. Highlighted portions of the inquiry display the changes that will be displayed for each code set category (ICD9, ICD0, and CPT). Other new fields are also highlighted:  Activation Dates	(for ICD9, ICD0, and CPT) Inactivation Dates	(for ICD9, ICD0, and CPT)  Selectable flag (for ICD9 and CPT; ICD0 are not selectable)   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

REMINDER TAXONOMY INQUIRY

May 08, 2003 2:10:49 am	Page 1

NUMBER: 30

VA-CERVICAL CANCER SCREEN

Brief Description:

Cervical cancer screen codes

Class: Sponsor:

Review Date:

Edit History: Patient Data Source:

Use Inactive Problems:

NATIONAL

ICD9 Codes:

Range V76.2-V76.2	Adjacent Lower-V76.19	Adjacent Higher-V76.3

Code

ICD Diagnosis

Activation	Inactivation Selectable

V76.2	SCREEN MAL NEOP-CERVIX

ICD0 Codes:

Range 91.46-91.46	Adjacent Lower-91.45	Adjacent Higher-91.49

CPT Codes:

Range Q0091-Q0091	Adjacent Lower-Q0086	Adjacent Higher-Q0092

CPT Short Name

Q0091	Obtaining screen pap smear

06/01/1994

X

Range Q0060-Q0061	Adjacent Lower-Q0059	Adjacent Higher-Q0062

10/01/1978	X

**Example: Inquire about Reminder Taxonomy Item – New Display Format**

|   Code | ICD Operation/Procedure   |    | Activation	Inactivation   |
|--------|---------------------------|----|---------------------------|
|  91.46 | CELL BLK/PAP-FEMALE GEN   |    | 10/01/1978                |

| **Chapter 3: CSV, cont’d**   | **2. Taxonomy option changes, cont’d**  :  **Edit Taxonomy Item**  This is an example of using the Edit Taxonomy Item option to edit the ICD0 Low Value and ICD0 High Value codes. When a code is entered here, it must be a code that exists and may be active or inactive. No Text names may be entered. The 91.44 -  91.46 range will be the only edit we will retain from the testing that follows. After testing the prompt for different test scenarios, the “@” at the ICD0 LOW CODE can be used to delete each range of codes entered.   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Edit Taxonomy Item’s ICD0 Low and High Code Example**

List Taxonomy Definitions Inquire about Taxonomy Item Edit Taxonomy Item

Copy Taxonomy Item

TL TI TE TC

Select Reminder Taxonomy Management Option: Edit Taxonomy Item

Select Reminder Taxonomy: **COPY CSV CERVICAL CANCER SCREEN** Cervical cancer screen codes	LOCAL

...OK? Yes// **&lt;Enter&gt;** (Yes) General Taxonomy Data

NAME: COPY CSV CERVICAL CANCER SCREEN	Replace **&lt;Enter&gt;**

BRIEF DESCRIPTION: Cervical cancer screen codes	Replace **&lt;Enter&gt;**

CLASS: LOCAL// **&lt;Enter&gt;** SPONSOR: **&lt;Enter&gt;** REVIEW DATE: **&lt;Enter&gt;**

PATIENT DATA SOURCE: **&lt;Enter&gt;** USE INACTIVE PROBLEMS: **&lt;Enter&gt;** INACTIVE FLAG: **&lt;Enter&gt;**

ICD0 Range of Coded Values

Select ICDO LOW CODE: 91.46// **&lt;Enter&gt;**

ICDO LOW CODE: 91.46// **91.44**

ICD0 HIGH CODE: 91.46// **91.49**

Select ICDO LOW CODE: **&lt;Enter&gt;**

ICD9 Range of Coded Values

Select ICD9 LOW CODE: V76.2// **&lt;Enter&gt;**

ICD9 LOW CODE: V76.2// **V76.1**

ICD9 HIGH CODE: V76.2// **V76.12**

Select ICD9 LOW CODE: **&lt;Enter&gt;**

CPT Range of Coded Values

Select CPT LOW CODE: 88150// **Q0091**

CPT LOW CODE: Q0091// **Q0085**

CPT HIGH CODE: Q0091// **Q0092**

Select CPT LOW CODE: **&lt;Enter&gt;**

Input your edit comments. Edit? NO// Yes

ICD0 Range of Coded Values

Select ICDO LOW CODE: 91.46// **&lt;Enter&gt;**

ICDO LOW CODE: 91.46// **91.44**

ICD0 HIGH CODE: 91.46// **91.49**

Select ICDO LOW CODE: **&lt;Enter&gt;**

| **Chapter 3: CSV, cont’d**   | **2. Taxonomy option changes, cont’d**  :  **Edit Taxonomy Item**  This is an example of editing the ICD0 Low Value and ICD0 High Value codes using common codes (various active and inactive codes).   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Editing the ICD0 Low Value and ICD0 High Value codes using common codes**

| **Chapter 3: CSV, cont’d**  **TIP:**  	The mail group must be  designated as “Public.”   | **3. Dialog Management option changes**  You can now define dialog elements with active or inactive diagnosis or procedure codes in the element’s FINDING ITEM and ADDITIONAL FINDING ITEMS multiple fields. The activation periods related to these codes are passed to the CPRS GUI. The CPRS GUI will only update PCE with diagnosis or procedure codes that are active on the patient’s encounter date. This will address those situations where a code is still active until the effective date is passed, and a new code won’t be active until after the effective date.  **New Reminders Dialog Management option**  **Inactive Codes Mail Message [PXRMCS INACTIVE DIALOG CODES]**  This option is used to search the Dialog File #801.41 for ICD and CPT Codes that have become inactive, and to send the report in a mail message to the Clinical Reminders mail group.   |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Inactive Codes Mail Message option**

Select Codes or All of the codes or "^" to exit: 3//	ALL Codes Check Mail for results.....

ICPT Codes ICD9 Codes ALL Codes

1

2

3

You have PENDING ALERTS

Enter	"VA to jump to VIEW ALERTS option

Select Reminder Dialog Management Option: IA	Inactive Codes Mail Message Select one of the following:

Dialog Parameters ... Reminder Dialogs

Inactive Codes Mail Message

DP DI IA

Select Reminder Managers Menu Option: DM	Reminder Dialog Management

| **Chapter 3: CSV, cont’d**   | 1. **Dialog Management option changes, cont’d**  **Changes to Dialog Taxonomy display in Dialog Edit**  To see the taxonomy changes:  1. Select DI, Reminder Dialog, from the Dialog Management menu 2. Change View, CV, to Reminder Dialogs 3. Select a dialog with taxonomy elements from the list that appears 4. Select Dialog Text when the Dialog is displayed   |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Dialog Edit List**  Mar 16, 2004@10:10:05	Page:	1 of REMINDER DIALOG NAME: VA-*INFLUENZA IMMUNIZATION [NATIONAL] *LIMITED EDIT*  Item Seq.	Dialog Overview  1. 5	Element: IM INFLUENZA DONE  1. 10 Element: IM INFLUENZA CONTRA  1. 15 Element: TX INFLUENZA IMMUNIZATION CODES  1. 19 Element: SP OTHER TEXT  1. 30 Group: GP IM REFUSAL   | 1                                                          | 1                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                               | **&gt;&gt;&gt;**                                           |                                                            |
| CO	Copy Dialog	DO	Dialog Overview	QU	Quit                                                                                                                                                                                                                                                                                                     |                                                            |                                                            |
| DD	Detailed Display	DT	Dialog Text                                                                                                                                                                                                                                                                                                            |                                                            |                                                            |
| DP	Progress Note Text	ED	Edit/Delete Dialog                                                                                                                                                                                                                                                                                                   |                                                            |                                                            |
| Select Item: Quit//  **DT**  Dialog Text                                                                                                                                                                                                                                                                                                      |                                                            |                                                            |
| Dialog Edit List	Mar 16, 2004@10:10:16	Page:	1 of                                                                                                                                                                                                                                                                                             | 4                                                          |                                                            |
| REMINDER DIALOG NAME: VA-*INFLUENZA IMMUNIZATION [NATIONAL] *LIMITED EDIT*                                                                                                                                                                                                                                                                    |                                                            |                                                            |
| Item Seq.	Dialog Text                                                                                                                                                                                                                                                                                                                         |                                                            |                                                            |
| 1	5	Element: IM INFLUENZA DONE                                                                                                                                                                                                                                                                                                                |                                                            |                                                            |
| Text: Patient received influenza at this encounter.                                                                                                                                                                                                                                                                                           |                                                            |                                                            |
| Add. Finding: IMMUNIZATION ADMIN [90471] (PROCEDURE)                                                                                                                                                                                                                                                                                          |                                                            |                                                            |
| Selectable codes:	Activation Periods                                                                                                                                                                                                                                                                                                          |                                                            |                                                            |
| 90471	IMMUNIZATION ADMIN	Jan 01, 1999                                                                                                                                                                                                                                                                                                         |                                                            |                                                            |
| Add. Finding: FLU VACCINE, 3 YRS, IM [90658] (PROCEDURE)                                                                                                                                                                                                                                                                                      |                                                            |                                                            |
| Selectable codes:	Activation Periods                                                                                                                                                                                                                                                                                                          |                                                            |                                                            |
| 90658	FLU VACCINE, 3 YRS, IM	Jan 01, 1999                                                                                                                                                                                                                                                                                                     |                                                            |                                                            |
| Add. Finding: VACCIN FOR INFLUENZA [11266] (DIAGNOSIS)                                                                                                                                                                                                                                                                                        |                                                            |                                                            |
| Selectable codes:	Activation Periods                                                                                                                                                                                                                                                                                                          |                                                            |                                                            |
| V04.8	VACCIN FOR INFLUENZA	Oct 01, 1978-Oct 01, 2003                                                                                                                                                                                                                                                                                          |                                                            |                                                            |
| Prompts: Series:                                                                                                                                                                                                                                                                                                                              |                                                            |                                                            |
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                             |                                                            | **&gt;&gt;&gt;**                                           |
| ADD Add Element/Group	DS	Dialog Summary	INQ  Inquiry/Print                                                                                                                                                                                                                                                                                    | ADD Add Element/Group	DS	Dialog Summary	INQ  Inquiry/Print | ADD Add Element/Group	DS	Dialog Summary	INQ  Inquiry/Print |
| CO	Copy Dialog	DO	Dialog Overview	QU	Quit                                                                                                                                                                                                                                                                                                     | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  |
| DD	Detailed Display	DT	Dialog Text                                                                                                                                                                                                                                                                                                            | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         |
| DP	Progress Note Text	ED	Edit/Delete Dialog                                                                                                                                                                                                                                                                                                   | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                |

| **Chapter 3: CSV, cont’d**  Two-step process:  1. Create element 2. Add element to dialog   | **3. Dialog Management option changes, cont’d**  **Adding new taxonomy dialog elements to a dialog**  To add new taxonomy dialog elements to a reminder dialog, first create a new dialog element, and then add the element to the dialog.  NOTE: Remember to “Change View” to Dialog Elements.  Use the Add (AD) action to create a new dialog element to represent the taxonomy finding.   |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Create New Dialog Element**

| Dialog List	Mar 09, 2004@00:00:12	Page:	1 of 132 DIALOG VIEW (DIALOG ELEMENTS)  Item Dialog Name	Dialog type	Status  1. 00 TIU ELEMENT	Dialog Element 2. 00 TIU ELEMENT SUPPRESS	Dialog Element 3. 01 TIU ELEMENT	Dialog Element 4. 02 TIU ELEMENT	Dialog Element 5. 03 TIU ELEMENT	Dialog Element 6. 04 TIU ELEMENT	Dialog Element 7. A A  PAIN ASSESS MEMBER REPORTS	Dialog Element                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AD	Add	CV	Change View	INQ Inquiry/Print CO	Copy Dialog	PT	List/Print All	QU	Quit  Select Item: Next Screen//  **AD**  Add  Select DIALOG to add:  **TEST CSV CERVICAL CANCER TAX**  Are you adding 'TEST CSV CERVICAL CANCER TAX' as  a new REMINDER DIALOG (the 3388TH)? No//  **Y**  (Yes) Not used by any other dialog  NAME: TEST CSV CERVICAL CANCER TAX Replace DISABLE:  CLASS:  **L**  LOCAL SPONSOR:  REVIEW DATE:  RESOLUTION TYPE:  ORDERABLE ITEM:  FINDING ITEM: TX.COPY  COPY CSV CERVICAL CANCER SCREEN	Cervical cancer screL  ...OK? Yes// Y (Yes) DIALOG/PROGRESS NOTE TEXT:  No existing text Edit? NO// YES  ==[ WRAP ]==[ INSERT ]=====&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]====  Click here to test Cervical Cancer taxonomy selection.  &lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===== ALTERNATE PROGRESS NOTE TEXT:  No existing text Edit? NO//  EXCLUDE FROM PROGRESS NOTE: SUPPRESS CHECKBOX:  Select ADDITIONAL FINDINGS: RESULT GROUP/ELEMENT:  Select SEQUENCE:  Input your edit comments. Edit? NO//  Select DIALOG to add: |

| **Chapter 3: CSV, cont’d**   | **3. Dialog Management option changes, cont’d**  **Adding new taxonomy dialog elements to a dialog**   |
|------------------------------|--------------------------------------------------------------------------------------------------------|

**Example: Add new dialog element to a Reminder Dialog definition**

| **Dialog Edit List**  Mar 09, 2004@00:50:41	Page:	1 of	1  REMINDER DIALOG NAME: Pap Smear (local)  Sequence	Dialog Details	Disabled  10	Dialog group: GPZ PAP SMEAR DIALOG Dialog elements:	1 EX PAP DONE  1. EX PAP DONE ELSEWHERE 2. HF PAP SMEAR CONTRAINDICATED 3. HF PATIENT REFUSED (PAP)   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                    |
| ADD Add Element/Group	DS	Dialog Summary	INQ  Inquiry/Print                                                                                                                                                                                                                                        |
| CO	Copy Dialog	DO	Dialog Overview	QU	Quit                                                                                                                                                                                                                                                         |
| DD	Detailed Display	DT	Dialog Text                                                                                                                                                                                                                                                                |
| DP	Progress Note Text	ED	Edit/Delete Dialog                                                                                                                                                                                                                                                       |
| Select Sequence: Quit// ED	Edit/Delete Dialog                                                                                                                                                                                                                                                     |
| NAME: Pap Smear (local)//                                                                                                                                                                                                                                                                         |
| DISABLE:                                                                                                                                                                                                                                                                                          |
| CLASS: LOCAL//                                                                                                                                                                                                                                                                                    |
| SPONSOR:                                                                                                                                                                                                                                                                                          |
| REVIEW DATE:                                                                                                                                                                                                                                                                                      |
| SOURCE REMINDER: Pap Smear-Screening (VHACHS)//                                                                                                                                                                                                                                                   |
| Select SEQUENCE: 10// 20                                                                                                                                                                                                                                                                          |
| DIALOG ELEMENT/GROUP: TEST CSV                                                                                                                                                                                                                                                                    |
| 1	TEST CSV ACTIVE AND INACTIVE CODES	dialog element	LOCAL                                                                                                                                                                                                                                         |
| 2	TEST CSV CERVICAL CANCER TAX	dialog element	LOCAL                                                                                                                                                                                                                                               |
| 3	TEST CSV WITH ONLY INACTIVE CODE	dialog element	LOCAL                                                                                                                                                                                                                                           |
| CHOOSE 1-3: 2  TEST CSV CERVICAL CANCER TAX	dialog element	LOCAL                                                                                                                                                                                                                                  |
| Select SEQUENCE:                                                                                                                                                                                                                                                                                  |
| **Dialog Edit List**  Mar 09, 2004@00:51:55	Page:	1 of	3                                                                                                                                                                                                                                          |
| REMINDER DIALOG NAME: Pap Smear (local)                                                                                                                                                                                                                                                           |
| Sequence	Dialog Details	Disabled                                                                                                                                                                                                                                                                  |
| 10	Dialog group: GPZ PAP SMEAR DIALOG                                                                                                                                                                                                                                                             |
| Dialog elements:	1 EX PAP DONE                                                                                                                                                                                                                                                                    |
| 2 EX PAP DONE ELSEWHERE                                                                                                                                                                                                                                                                           |
| 3 HF PAP SMEAR CONTRAINDICATED                                                                                                                                                                                                                                                                    |
| 4 HF PATIENT REFUSED (PAP)                                                                                                                                                                                                                                                                        |
| 20	Dialog element: TEST CSV CERVICAL CANCER TAX                                                                                                                                                                                                                                                   |
| Finding type: REMINDER TAXONOMY                                                                                                                                                                                                                                                                   |
| Finding item: COPY CSV CERVICAL CANCER SCREEN [TX(60)]                                                                                                                                                                                                                                            |
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                    |
| ADD Add Element/Group	DS	Dialog Summary	INQ  Inquiry/Print                                                                                                                                                                                                                                        |
| CO	Copy Dialog	DO	Dialog Overview	QU	Quit                                                                                                                                                                                                                                                         |
| DD	Detailed Display	DT	Dialog Text                                                                                                                                                                                                                                                                |
| DP	Progress Note Text	ED	Edit/Delete Dialog                                                                                                                                                                                                                                                       |
| Select Sequence: Next Screen//                                                                                                                                                                                                                                                                    |

**Chapter 4: MHV**

**Chapter 4: My Health** ***e*** **Vet**

My Health ***e*** Vet is a new online environment where veterans, family members, and clinicians may come together to optimize veterans` healthcare. Web technology combines essential health record information with online health resources to enable and encourage veteran/clinician collaboration.

**Overview**

Participating veterans are given copies of key portions of their electronic health records. This record is stored in a secure and private environment called an *e* **VA** ult. The *e* **VA** ult will be personalized with appropriate links to useful explanatory material, to help veterans understand what is in their record, and what they can do to improve their health condition. Veterans can also add structured medical information in the “self-entered” section of their *e* **VA** ult.

**Benefits to the veterans include the following:**

- My Health ***e*** Vet project will allow veterans to review their own medical records, to better understand their state of health, and to explore actions they can take to improve their health.

- Participating veterans will be able to own a copy of their health record, and thus be a partner with their caregivers in creating an “epidemic” of health.

- It will be easier for non-VA health care providers to access (with patient permission) historical information on a patient’s care.

**Benefits to VA include the following:**

- An educated, empowered patient can participate more fully in his/her health decisions.

- As more data is gathered (from VA and non-VA care) in a consolidated form, it will be easier to review this data, with permission, and recommend actions that will improve the overall health of the patient.

**NOTE:**

- It will allow VA to reach out and supply services to veterans who are not currently enrolled in the system.

The veteran’s private health record will be securely stored and only accessible by the veteran and others they have identified.

- It may reduce health care delays caused by the need for follow- up phone calls, fax, and re-keying information.
- It will allow the clinical care team to better work together in providing timely and quality health care to our veterans.

| **Chapter 4: MHV, cont’d**  NOTE: The components will display the results or reminder evaluation for all reminders that have a "P" in the Usage field. See the example below that shows the new P for Patient Usage entry.   | **My Health**  ***e***  **Vet, cont’d**  Reminders are being developed for veterans to view in their My Health  *e*  Vet record. The veteran will be able to click on a “Details” button to see the details of a reminder – comparable to the Clinical Maintenance screens in CPRS and Health Summary.  A patch (PXRM*2.0*2) will provide the functionality to display and view My Health Reminders that show as DUE, to remind the veteran of primary health care needs that should be addressed.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 4: MHV, cont’d**  NOTE: The components display the results for all reminders that have a "P" in the Usage field.  The new Health Summary types each contain just one component, the one with the same name as the type.   | **My Health**  ***e***  **Vet Health Summary Types**  Clinical Reminders V.2.0 contains new health summary components to support the My HealtheVet project. These components eliminate much of the technical text and code information that is contained in the CM component, and will display summary or detailed information on individual patient reminders to the patients.  Two new national Health Summary types were created to include the new health summary components: REMOTE MHV REMINDERS DETAIL and REMOTE MHV REMINDERS SUMMARY. These will  be available in health summaries on the reports tab in CPRS.  The health summary types will also be available to clinicians even if the patient is being seen at a different site.  **Example: MHVD Health Summary - Detail Display**   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 4: MHV, cont’d**   | **My HealtheVet Health Summary**   |
|------------------------------|------------------------------------|

**Example: MHVS Health Summary, cont’d**

********************	CONFIDENTIAL AD HOC SUMMARY	pg. 1 ********************* CRPATIENT,ONE	666-31-9898	1A(1&amp;2)		DOB: 07/13/1950

MHVD - Detail Display

--STATUS-- --DUE DATE--	--LAST DONE--

Flu vaccine	DUE NOW	DUE NOW	unknown All patients over the age of 50 should receive influenza vaccination unless they are allergic to eggs.

Influenza or "flu" is a serious disease that spreads easily. It causes fever, chills, cough, fatigue, aches, or loss of appetite. It can progress to bronchitis, pneumonia and death. Flu causes thousands of deaths each year in the US that could be prevented if the flu shot or vaccine was received.

The flu shot is recommended yearly for those who are at a higher risk to have severe flu if they catch the flu. They include:

- Anyone age 50 older.
- Anyone with long-term health problems of the lungs, heart, or kidney, asthma, or diabetes.
- Anyone who has a weak immune system from HIV/AIDs, steroid treatment, or cancer treatment.
- Residents of nursing homes or other long-term care facilities.

The flu shot is not recommended for people who are allergic to eggs, had a severe reaction to flu shot in the past, allergic to thiomerosol, a history of Guillian-Barre Syndrome (GBS), or currently have a high fever.

The flu shot or vaccine protects most people from the flu. Some may still catch the flu after having the shot but are likely to have a milder case.

The flu shot does NOT cause the flu. It protects one from the flu. The vaccine is safe and it works. Most people will not have side effects. A few may feel sore at the site where the shot was given. Fewer may have fever, chills, headaches, or muscle aches. The best time to get

a flu shot is in October or November. However, getting the flu shot later in December thru March will still give very good protection. VA Clinics usually offer flu shots from September thru March.

Our records show that you have not received your flu shot for this season. Please get your flu shot soon or tell us if you already got one.

| **Chapter 4: MHV, cont’d**   | **My HealtheVet Health Summary**  **Example: MHVD Health Summary - Detail Display, cont’d**   |
|------------------------------|-----------------------------------------------------------------------------------------------|

Please check these web sites for more information: Web Site: CDC Influenza Home Page

URL: [http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm](http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm)

Web Site: Weekly Update on Influenza Rates

URL: [http://www.cdc.gov/ncidod/diseases/flu/weekly.htm](http://www.cdc.gov/ncidod/diseases/flu/weekly.htm)

CDC Site for weekly updates on the current influenza activity in the community.

Web Site: Dept HHS Information on Influenza Vaccination

URL: [http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt](http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt)

Web Site: California Influenza Information

URL: [http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm](http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm)

Web Site: Patient Handout for Influenza Vaccine

URL: [http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf](http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf)

Flu vaccine Due Now	DUE NOW	DUE NOW	unknown All patients over the age of 50 should receive influenza vaccination unless they are allergic to eggs.

Influenza or "flu" is a serious disease that spreads easily. It causes	fever, chills, cough, fatigue, aches, or loss of appetite. It can	progress to bronchitis, pneumonia and death.	Flu causes thousands of	deaths each year in the US that could be prevented if the flu shot or	vaccine was received.

The flu shot is recommended yearly for those who are at a higher risk to	have severe flu if they catch the flu. They include: *	Anyone age 50 older. *			Anyone with long-term health problems of the lungs, heart, or		kidney, asthma, or diabetes.	*	Anyone who has a weak immune system from HIV/AIDs, steroid	treatment, or cancer treatment. *	Residents of nursing homes or other long-term care facilities.

The flu shot is not recommended for people who are allergic to eggs, had	a severe reaction to flu shot in the past, allergic to thiomerosol, a	history of Guillian-Barre Syndrome (GBS), or with high fever at the	time.	The flu shot or vaccine protects most people from the flu. Some may still	catch the flu after having the shot but are likely to have a milder one.

| **Chapter 4: MHV, cont’d**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **My HealtheVet Health Summary**  **Example: MHVD Health Summary - Detail Display, cont’d**   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| The flu shot does NOT cause the flu. It protects one from the flu. The vaccine is safe and it works. Most people will not have side effects. A few may feel sore at the site where the shot was given. Fewer may have fever, chills, headaches, or muscle aches. The best time to get  a flu shot is in October or November. However, getting the flu shot later in December thru March will still give very good protection. VA Clinics offer flu shots usually from September thru March.  Our records show that you have not received your flu shot for this season.	Please get your flu shot soon or tell us if you already got one.  Please check these web sites for more information: Web Site: CDC Influenza Home Page  URL:  [http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm](http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm)  Web Site: Weekly Update on Influenza Rates  URL:  [http://www.cdc.gov/ncidod/diseases/flu/weekly.htm](http://www.cdc.gov/ncidod/diseases/flu/weekly.htm)  CDC Site for weekly updates on the current influenza activity in the community.  Web Site: Dept HHS Information on Influenza Vaccination  URL:  [http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt](http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt)  Web Site: California Influenza Information  URL:  [http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm](http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm)  Web Site: Patient Handout for Influenza Vaccine  URL:  [http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf](http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf)  Influenza Vaccine		DUE NOW	12/10/2000	12/10/1999 Immunization: INFLUENZA =	(12/10/1999)  Encounter Procedure = INFLUENZA IMMUNIZATION (12/10/1999)  Flu shot due yearly in patients any age that have a high risk for flu or pneumonia.  Encounter Diagnosis = DIABETES MELLI W/0 COMP TYP I (09/10/2001)  MENTAL TESTS ZZCOPYRIGHT	DUE NOW	DUE NOW	unknown  Age match text for inquiry purposes |                                                                                               |

CRPROVIDER,ONE

| **Chapter 4: MHV, cont’d**   | **My HealtheVet Health Summary**  **Example: MHVS Health Summary - Summary Display**   |
|------------------------------|----------------------------------------------------------------------------------------|

| **Chapter 4: MHV, cont’d**   | **Adding My HealtheVet Health Summary to a User’s Health Summary in CPRS**  **The example below shows the sequence for adding the MHV health summary types to the CPRS Reports tab for a user**   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Health Summary: Remote **MHV**

1. Remote Mhv Reminders Detail
2. Remote Mhv Reminders Summary

CHOOSE 1-2: **2** Remote MHV REMINDERS SUMMARY

Select Sequence:

Display 'Health Summary Types List' Defaults Precedence of 'Health Summary Types List' Method of compiling 'Health Summary Types List' Edit 'Health Summary Types List' Parameters

Select CPRS Reports Tab 'Health Summary Types List' Menu Option: **4** Edit 'Health Summary Types List' Parameters

Edit the CPRS Health Summary Types list on the reports tab

--- Setting GUI Health Summary Type List for User: **CRPROVIDER,ONE**

Select Sequence: **1**

Are you adding 1 as a new Sequence? Yes//	YES

Sequence: 1//	1

Health Summary: Remote **MHV**

1. Remote Mhv Reminders Detail
2. Remote Mhv Reminders Summary

CHOOSE 1-2: **1** MHV REMINDERS DETAIL DISPLAY

Select Sequence: **2**

Are you adding 2 as a new Sequence? Yes//	YES

Sequence: 2// **2**

1

2

3

4

Select Health Summary Maintenance Menu Option: **9** CPRS Reports Tab 'Health Summary Types List' Menu

Disable/Enable Health Summary Component Create/Modify Health Summary Components Edit Ad Hoc Health Summary Type

Rebuild Ad Hoc Health Summary Type Resequence a Health Summary Type Create/Modify Health Summary Type Edit Health Summary Site Parameters Health Summary Objects Menu ...

CPRS Reports Tab 'Health Summary Types List' Menu ... CPRS Health Summary Display/Edit Site Defaults ...

5

6

7

8

9

10

Health Summary Coordinator's Menu ... Health Summary Enhanced Menu ...

Health Summary Menu ...

Health Summary Maintenance Menu ...

Select Health Summary Overall Menu Option: **4** Health Summary Maintenance Menu

Health Summary Overall Menu

Select OPTION NAME: **GMTS MANAGER**

### APPENDIX A: Hints and Tips

**Q:** Is there any way to do a reminder report on an individual finding item?

We want to add a check box that indicates depression is a new diagnosis. Is there a way to do a reminder report just on that one finding that will tell us how many of the patients that were seen that this was applicable for?

**A** : Set up a local reminder with that one finding as a resolution finding. Define the reminder USAGE field as Reports, and then it will not appear on the cover sheet.

Additional trick:

Make the frequency to be 1 day, and put an OR for the resolution logic and AND for the COHORT logic. That then gives you output in the CM or health summary that gives the date it was last done so not only do you get a list of folks who have the finding but you also can tell when it was entered.

**Q: (NOIS)** Need routine to print labels

The site would like to print address labels for reminders that are due, to mail to the patients. Do you know of a site that my have this in place?

**A:** CR V. 2.0 will allow you to save a patient from a due report to a patient list. From a patient list, you can print a report that displays the address in a delimited format for import/export to Word labels.

**Q:** I have a couple of medication reminders that I have edited so that if the provider writes a new prescription, the reminder will be resolved temporarily by the pending medication order and not have to wait for the released date. I have the orderable items set to resolve the reminder if the status of the orderable item is pending. The order shows on the orders tab as pending and DOES NOT resolve the reminder. The reminder test output suggests to me that the pending order is not being used in the reminder evaluation.

**A:** The future date needs to be added to the reminder at the Ending Date/Time prompt. The default is the end of the current day. If you want this to be further in the future, you need to enter something like T+3M.

###### Forced Value in Dialogs

**Q:** I have an element that has a single ICD code in it and whenever this template is used, I want this ICD code to be entered and for it to automatically go in as the primary diagnosis.

I can get the ICD code to be automatically entered but I cannot seem to create a forced value prompt from the PXRM PRIMARY DIAGNOSIS prompt that works correctly. If I set the forced value to PRIMARY or to PRIMARY DIAGNOSIS, it does not seem to work and the diagnosis is always recorded as the secondary diagnosis.

Here is the element:

NAME: TX V CODE FOR TB SCREEN Replace DISABLE:

CLASS: LOCAL// SPONSOR: REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: V74.1// DIALOG/PROGRESS NOTE TEXT:

Enter ICD Code for "Screening for TB" (V code for checkout) Edit? NO// y YES

ICD Code for "Screening for TB" (V code for checkout)

ALTERNATE PROGRESS NOTE TEXT:

No existing text Edit? NO//

EXCLUDE FROM PROGRESS NOTE: YES// SUPPRESS CHECKBOX: SUPPRESS// Select ADDITIONAL FINDINGS:

RESULT GROUP/ELEMENT:

Select SEQUENCE: 5// SEQUENCE: 5//

ADDITIONAL PROMPT/FORCED VALUE: PXRM PRIMARY DIAGNOSIS

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT: YES// REQUIRED: NO//

Select SEQUENCE:

Input your edit comments. Edit? NO//

Here is the forced value that does not work:

Forced value NAME: ICD PRIMARY DIAGNOSIS Replace DISABLE Forced value:

CLASS: LOCAL// SPONSOR:

REVIEW DATE:

FORCED VALUE: PRIMARY// RESTRICTED TO FINDING TYPE: POV//

**A:** Here's an undocumented feature. If you want the Primary diagnosis to automatically be populated, define a Prompt as below and apply it to the appropriate dialog element

Forced value NAME: FORCE PRIMARY DIAGNOSIS Replace DISABLE Forced value:

CLASS: LOCAL// SPONSOR:

REVIEW DATE:

FORCED VALUE: 1// **&lt;&lt; Value of 1 will set the field TRUE** . RESTRICTED TO FINDING TYPE: POV//

**Q:** When Clinical Maintenance is run on a reminder that is applicable due to a problem list entry, why is today's date pulled rather than the date of problem list entry?

**A:** There are two dates associated with ICD9 diagnoses found in PROBLEM LIST. There is the date entered and the date last modified. The PRIORITY field is used to determine if a problem is chronic or acute. ***If the problem is chronic, Clinical Reminders will use today’s date in its date calculations; otherwise it will use the date last modified.*** Problems that are “chronic” can never expire. Note that it only uses active problems unless the field USE INACTIVE PROBLEMS is yes.

**Q:** Flu vaccine reminder

Last year our flu vaccine reminder worked well, but now we are getting the following: This is how the reminder dialog is set up:

Additional Finding: VACCIN FOR INFLUENZA [11266] Additional Finding: IMMUNIZATION ADMIN [90471] Additional Finding: FLU VACCINE, 3 YRS, IM [90658]

Additional Finding: OFFICE/OUTPATIENT VISIT, EST [99211]

I just put in a vaccine using the reminder and found the following show (the computer is automatically adding codes):

1. CPT Code: 90471 IMMUNIZATION ADMIN
2. CPT Code: 90658 FLU VACCINE, 3 YRS, IM
3. CPT Code: 99211 OFFICE/OUTPATIENT VISIT, EST
4. CPT Code: 90659 FLU VACCINE, WHOLE, IM &lt;-------
5. Immunization: INFLUENZA	&lt;-------
6. Immunization:  FLU,3 YRS
7. Immunization: FLU,WHOLE	&lt;------

Any ideas as to why this is happening would be appreciated.

**A:** Your Encounter Form for that specific clinic may have that code (90659) as a choice. If so, it's most probably being entered by either:

1. The provider who checks out the appointment themselves. standalone. Clicking on the encounter

button, brings up the encounter form codes that are on that EF for that clinic; or

1. The checkout clerk may be just entering codes checked-off on the EF by the provider.

###### Q: How can I make reminder dialogs WYSIWYG for short lines of text?

**A:** The new text formatter lets you format dialogs, as well as progress note text. Define your element like this, using the backslashes as shown:

Example Output in CPRS Reminder Dialog:

<!-- image -->

NOTE: You can also use &lt;br&gt; for line breaks.

**Q:** When I try to edit the Cover Sheet list in CPRS, it does not give me the option for System, location, service, division. I was assigning reminder folders to physicians and nurses through the GUI and now the Edit Cover Sheet Reminder List is grayed out for me. It will not allow me to edit for System, Division, Location, etc. I can only edit for myself (user). Where do we change this, so I can assign reminders through the GUI?

**A:** Check to see if you have the PXRM CPRS CONFIGURATION menu. You may have it as part of the Eve menu. If you add it to your secondary menu, the option should no longer be grayed out on your Edit Cover Sheet Reminder list in GUI.

###### Q: Computed Finding – Location

We would like to build a reminder that is applicable only to patients in specific locations (Domiciliary). These patients are followed by Primary Care providers in clinics where patients in an outpatient status are also seen.	so simply displaying the reminder according to hospital location is

not an option.

Has anyone created a computed finding that would make my reminder applicable only to Dom patients? Or can anyone think of something besides a computed finding that will allow me to do this?

**A:** Here’s one, which you might need to customize just a little for your site.

First possibility. This is the one we use to check for patients in a NHCU, but really it's just hard coded to the location names of our two long-term care areas. I've changed the references to an NHCU to read "DOM,” but it would work no matter what location you are trying to find, as long as it is specific. Something like "11E" might not work.

DOM(DFN,TEST,DATE,VALUE,TEXT)	;;LOCAL TO HINES - IS PATIENT IN DOM?

N VAIN

D INP^VADPT

S TEST=0,DATE=""

I $P(VAIN(4),"^",2)["ECC" S TEST=1,DATE=DT

I $P(VAIN(4),"^",2)["RCF" S TEST=1,DATE=DT Q

NAME: AJEY DOM PATIENT (local) ROUTINE:&lt;&lt;WHATEVER YOU NAME YOUR ROUTINE&gt;&gt;

ENTRY POINT: DOM	PRINT NAME: Is Patient in a DOM Location?

You would want to change ECC to match something that your DOM locations had in their name, presumably "DOM".

The other possibility is instead of looking in VAIN(4), which contains the patient location, to look in VAIN(3), if the treating specialty might be specific for something like a domiciliary.

###### Drug for patient cohort logic

**Q:** Can I use a drug for patient cohort logic? I thought that I could, but then I tried the drug and use the logic of and it shows that the patient is not applicable for this reminder.	Can anyone help me?

**A:** You can use a DC or Drug Class as a finding as I've done on the reminder for Beta Blocker after an acute MI. Here's what it looks like:

Select Reminder Definition Management Option: re	Add/Edit Reminder Definition Select Reminder Definition: v1-beta BLOCKER AFTER MI	LOCAL

Select one of the following:

A	All reminder details

G	General

B	Baseline Frequency

F	Findings

L	Logic

D	Reminder Dialog

W	Web Addresses Select section to edit: f	Findings Findings

Choose from:

DC	CV100 **&lt;----	That one right there!!!!**

HF	ACTIVE OUTSIDE RX FOR BETA BLOCKER

HF	INACTIVATE BETA BLOCKER AFTER ACUTE MI RT	LOW PULSE

RT	LOW SYSTOLIC BP

TX	ASTHMA

TX	HEART BLOCKS

TX	PRO-ACUTE MYOCARDIAL INFARCTION

Select FINDING:

###### Q: Allocation Errors

Why did the user error out while running a clinical reminder in CPRS?

$ZE= ETRAP+4^XWBTCPC:1, %DSM-E-ALLOC, allocation failure

S XWBERC=$$EC^%ZOSV,XWBERR=$C(24)\_"M	ERROR="\_XWBERC\_$C(13,10)\_"LAST REF="\_$$LG

R^%ZOSV\_$C(4)

Last Global Ref: ^PXRMD(801.41,570,1)

**A:** Probably two nodes were configured below the standard partition size. Once the partition size parameters were updated and the nodes re-booted, errors stopped.

**Q:** Why is this Reminder not Due as Expected? The Rank Frequency (as relates to this problem) appears to be correct...

1. Colonoscopy taxonomy	(resolves 10 yr)
2. Colonoscopy Done Elsewhere (resolves 10 yr)

6	FOBT taxonomy (for lab test)	(resolves 1 yr)

**************************************************************** This particular patient shows:

STATUS	--DUE DATE--	--LAST DONE--

Resolved	8/13/2011	8/13/2001

****************************************************************

8/13/2001	Laboratory test:	Blood Occult feces; value - Neg 11/10/1999 (E) Health Factor:	COLONOSCOPY ELSEWHERE

***************************************************************

We expect to see a DUE DATE of 11/10/2009 - 10 yrs from the Colonoscopy. Instead, he shows 10 years from the Lab Test date of 8/13/2001.

**A:** For each item that had a Rank Frequency within the Reminder, it was suggested to make sure there was an Effective Period. I did, but it still didn't work. Then, I went back and for each element with Rank Frequency, I put in the Minimum Age field. I didn't think this was necessary because it was the same as the Baseline Frequency. But, once those were entered, it works beautifully, calculating the correct date.

So, now we know to enter all the fields applicable if a Rank Frequency is entered, even if it appears to be duplication of information.

**Q:** We've been having trouble getting this reminder to turn off. Could you look at my logic and tell me what I've done wrong?

Baseline Frequency:

Do In Advance Time Frame:	Do if DUE within 1 month Sex Specific:

Ignore on N/A:

Frequency for Age Range:	1 year for all ages Match Text:

No Match Text:

Findings:

---- Begin: VA-TOBACCO USE	(FI(1)=TX(22))

Finding Type: REMINDER TAXONOMY Use in Patient Cohort Logic: OR

Beginning Date/Time: T-1Y

---- End: VA-TOBACCO USE

---- Begin: SMOKING CESSATION	(FI(2)=ED(663020))

Finding Type: EDUCATION TOPIC Occurrence Count: 3

---- End: SMOKING CESSATION

---- Begin: CURRENT TOBACCO USER	(FI(3)=HF(663091))

Finding Type: HEALTH FACTOR Use in Patient Cohort Logic: OR

---- End: CURRENT TOBACCO USER

---- Begin: FORMER TOBACCO USER	(FI(4)=HF(663090))

Finding Type: HEALTH FACTOR Use in Patient Cohort Logic: AND NOT

Beginning Date/Time: T-1Y

---- End: FORMER TOBACCO USER

---- Begin: LIFE EXPECTANCY &lt; 1 YR	(FI(5)=HF(663080))

Finding Type: HEALTH FACTOR Use in Patient Cohort Logic: AND NOT

---- End: LIFE EXPECTANCY &lt; 1 YR

---- Begin: CURRENT SMOKER	(FI(6)=HF(2))

Finding Type: HEALTH FACTOR Use in Patient Cohort Logic: OR

---- End: CURRENT SMOKER

---- Begin: PREVIOUS SMOKER	(FI(7)=HF(4))

Finding Type: HEALTH FACTOR Use in Resolution Logic: OR

Beginning Date/Time: T-1Y

---- End: PREVIOUS SMOKER

Function Findings:

---- Begin:

FF(1)---------------------------------------------------------

Function String: COUNT(2)&gt;2 Expanded Function String:

COUNT(SMOKING CESSATION)&gt;2

Match Frequency/Age: 1 year for all ages Use in Resolution Logic: AND

---- End: FF(1)

Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient:

(SEX)&amp;(AGE)&amp;FI(1)!FI(3)&amp;'FI(4)&amp;'FI(5)!FI(6)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)&amp;FI(VA-TOBACCO USE)!FI(CURRENT TOBACCO USER)&amp;'

FI(FORMER TOBACCO USER)&amp;'FI(LIFE EXPECTANCY &lt; 1 YR)!FI(CURRENT SMOKER)

Customized RESOLUTION LOGIC defines findings that resolve the Reminder: FF(1)

Expanded Resolution Logic: FF(1)

**A:** The problem is function findings do not have a date, so if they are the sole resolution finding, a resolution date cannot be determined. Try changing your resolution logic to FI(2)&amp;FF(1). The resolution date would then be the most recent date for the Smoking Cessation Education but it would not be resolved unless at least three educations were done.

**Q:** Which takes precedence: finding modifiers on terms or finding modifiers in the reminder definition?

**A:** In most cases a finding modifier on a term takes precedence over the modifier in the definition. An exception to this is the Occurrence Count. The reason for this can be understood by looking at an example. Let’s say a term has been mapped to three findings with an Occurrence Count of 1 for finding 1, 2 for finding 2, and 3 for finding 3. If the maximum number of occurrences is found for each finding then how do you determine how many occurrences to display? In this case we would have 6 occurrences so we have the possibility of displaying anywhere between 1 and 6 of them. The solution is to display the number of occurrences specified at the definition level.

**Q:** We have one user who can only see the "other" folder when he tries to process clinical reminders.

What do we have to do so he can see the due and applicable folders?

**A:** Have the user click on the red reminder clock and then click on the 'VIEW' command. Make sure that all the categories (DUE, APPLICABLE, etc.) have been checked.

###### Reminder Exchange Tip

If you try to exchange a reminder containing a location list from one system to another and there is an inconsistency or mismatch between systems in the AMIS stop code, you will get the following error message. (in this case the system has two selectable entries for stop code 560.)

REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 is NEW,

what do you want to do?

Select one of the following:

C	Create a new entry by copying to a new name I	Install

Q	Quit the install

S	Skip, do not install this entry

Enter response: i	Install

Name associated with AMIS stop code does not match the one in the packed reminder:

AMIS=560

Site Name=ZZSUBSTANCE ABUSE - GROUP

Name in packed reminder=SUBSTANCE ABUSE - GROUP

The update failed, UPDATE^DIE returned the following error message: MSG("DIERR")=1^1

MSG("DIERR",1)=701 MSG("DIERR",1,"PARAM",0)=3 MSG("DIERR",1,"PARAM",3)=GYNECOLOGY MSG("DIERR",1,"PARAM","FIELD")=.01

MSG("DIERR",1,"PARAM","FILE")=810.90011

MSG("DIERR",1,"TEXT",1)=The value 'GYNECOLOGY' for field CREDIT STOP TO EXCLUDE

in CREDIT STOPS TO EXCLUDE SUB-FIELD in CLINIC STOP LIST SUB-FIELD in

file REMINDER LOCATION LIST is not valid. MSG("DIERR","E",701,1)=

REMINDER LOCATION LIST entry NEXUS STOP CODES FY05 did not get installed! Examine the above error message for the reason.

### APPENDIX B: Glossary

#### Acronyms

AAC	Austin Automation Center

AIMS	Abnormal Involuntary Movement Scale API	Application Programmer Interface.

CAC	Clinical Application Coordinator CPRS	Computerized Patient Record System. DBIA	Database Integration Agreement.

EPRP	External Peer Review Program

GUI	Graphical User Interface.

HSR&amp;D	Health Services Research and Development HL7	Health Level 7

IHD	Ischemic Heart Disease

MDD	Major Depressive Disorder

OQP	Office of Quality and Performance QUERI	Quality Enhancement Research Initiative SAS	Simple Authentication and Security

SRS	Software Requirements Specification

VHA	Veterans Health Administration. VISN	Veterans Integrated Service Networks.

**V** IS *T* **A** Veterans Health Information System and Technology Architecture.

#### National Acronym Directory

**Definitions**

AAC SAS Files	AAC SAS files contain data that is equivalent to data stored in

the Reminder Extract Summary entry in the Reminder Extract Summary file. AAC manages SAS files for use by specifically defined users.

Applicable	The number of patients whose findings met the patient cohort

reminder evaluation.

Due	The number of patients whose reminder evaluation status is due.

Extract Parameter	Parameters that define how to identify the patient cohort. A

national extract entry is defined for each extract process. This entry defines an extract name, how often to automatically run the named extract process, the rules used to identify target patients, what reminders should be run against what patient list, what type of finding counts to accumulate, and where to transmit results.

Extract Summary	An extract summary containing the results of an extract process

is created by this process in the Extract Summary File. This Extract Summary entry will help coordinators track the extract process through successful transmission processing by AAC.

Extract Run	A periodic extract job based on the Extract Parameter definition.

The extract job creates an entry in the Reminder Extract Summary file. The extract job automatically starts a transmission job to transmit the extract summary data to a queue at the AAC. The successful completion of the Extract Run schedules the next periodic Extract Run.

Finding Count Rules	A Finding Count Rule defines the group of findings to

accumulate, the type of finding total, and whether to use the TOTAL or APPLICABLE patient cohorts to calculate finding counts.

Finding Group	Group of Reminder Terms within the Extract Parameter File

used for counting purposes.

Finding Totals	Totals derived using Finding Count Rules.

HL7 Transmissions	HL7 transmission packages contain HL7 messages that are

processed between the transmitting system and AAC.

List Rules		A List Rule is a set of rules that define which findings shall be used to determine whether a patient should be added or removed from a patient list.

National Database	All sites running Mental Health QUERI software transmit their

data to a new compliance totals database at the AAC.

Not Applicable	The number of patients whose findings did not meet the patient

cohort reminder evaluation.

Not Due		The number of patients whose reminder evaluation status is not due.

Reminder Definitions	Reminder Definitions comprise the predefined set of finding

items used to identify patient cohorts and reminder resolutions. Reminders are used for patient care and/or report extracts.

Reminder Dialog	Reminder Dialogs comprise a predefined set of text and findings

that together provide information to the CPRS GUI, which collects and updates appropriate findings while building a progress note.

Reminder Patient List	A list of patients that is created from a set of List Rules and/or as

a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.

Reminder Terms	Predefined finding items that are used to map local findings to

national findings, providing a method to standardize these findings for national use.

Reminder Totals	Totals that are accumulated from the reminder evaluation

process based on the APPLICABLE, NOT APPLICABLE, DUE, AND NOT DUE statuses.

Report Reminders	Reminders may be defined specifically for national reporting.

Report Reminders do not have a related Reminder Dialog in CPRS and are not used by clinicians for patient care. However, clinical reminders that are used in CPRS may also be used for national reminder reporting. All reminders targeted for national reporting are defined in Extract Parameters.

Reporting Period Extract	The extracts may be for monthly, quarterly, or yearly processing.

The extracts are formatted and transmitted to the national database via HL7 messaging using a report format.

Total	The total number of patients in a patient list (denominator) based on the criteria defined in the Reminder List Rule file.

Transmission Run	The Transmission Run is started automatically by the Extract

Run, but may also be manually scheduled. The extract process starts the Transmission Run just before completing the Extract Run. The Transmission Run transmits extract summary data to an AAC queue via HL7 transmissions. This data updates the Reminder Extract Summary entry for the reporting period.

### APPENDIX C: National Reminders Rescission

See [VHA Notice 2004-04](http://vaww1.va.gov/vhapublications/ViewPublication.asp?pub_ID=1159) for more information about rescission of national reminders.

When Clinical Reminders V.2.0 is installed, the following reminders are rescinded by:

1. Setting the inactive flag.
2. Setting the RESCISSION DATE field.
3. Changing the name of the reminder.
4. Changing the data in the PRINT NAME field

NOTE: ZZ is reserved for use as a scratch namespace (defined on FORUM, Package File). As such, sites may already have copied a reminder and used the prefix ZZ. Sites should review their local reminders, to ensure that this installation doesn’t over-write any reminders.

| **Reminder Name**                    | **New Name**                           | **Print Name**                | **New Print Name**               |
|--------------------------------------|----------------------------------------|-------------------------------|----------------------------------|
| VA-*BREAST CANCER  SCREEN            | ZZVA-*BREAST  CANCER SCREEN            | Breast Cancer  Screen         | ZZ Breast Cancer  Screen         |
| VA-*CERVICAL CANCER SCREEN           | ZZVA-*CERVICAL CANCER SCREEN           | Pap Smear                     | ZZ Pap Smear                     |
| VA-*CHOLESTEROL  SCREEN (F)          | ZZVA-*CHOLESTEROL  SCREEN (F)          | Cholesterol Screen  (Female)  | ZZ Cholesterol Screen  (Female)  |
| VA-*CHOLESTEROL  SCREEN (M)          | ZZVA-*CHOLESTEROL  SCREEN (M)          | Cholesterol Screen  (Male)    | ZZ Cholesterol Screen  (Male)    |
| VA-*COLORECTAL CANCER SCREEN (FOBT)  | ZZVA-*COLORECTAL CANCER SCREEN  (FOBT) | Fecal Occult Blood Test       | ZZ Fecal Occult Blood Test       |
| VA-*COLORECTAL  CANCER SCREEN (SIG.) | ZZVA-*COLORECTAL  CANCER SCREEN (SIG.) | Flexisigmoidoscopy            | ZZ  Flexisigmoidoscopy           |
| VA-*FITNESS AND EXERCISE SCREEN      | ZZVA-*FITNESS AND EXERCISE SCREEN      | Exercise Education            | ZZ Exercise Education            |
| VA-*HYPERTENSION                     | ZZVA-*HYPERTENSION                     | Hypertension                  | ZZ Hypertension                  |
| VA-*INFLUENZA  IMMUNIZATION          | ZZVA-*INFLUENZA  IMMUNIZATION          | Influenza  Immunization       | ZZ Influenza  Immunization       |
| VA-*PNEUMOCOCCAL VACCINE             | ZZVA-*PNEUMOCOC- CAL VACCINE           | Pneumovax                     | ZZ Pneumovax                     |
| VA-*PROBLEM DRINKING  SCREEN         | ZZVA-*PROBLEM  DRINKING SCREEN         | Problem Drinking  Screen      | ZZ Problem Drinking  Screen      |
| VA-*SEATBELT AND  ACCIDENT SCREEN    | ZZVA-*SEATBELT AND  ACCIDENT SCREEN    | Seatbelt and Accident  Screen | ZZ Seatbelt and  Accident Screen |
| VA-*TETANUS DIPHTHERIA  IMMUNIZATION | ZZVA-*TETANUS DIPHTHERIA  IMMUNIZATION | Tetanus Diphtheria (TD-Adult) | ZZ Tetanus Diphtheria (TD-Adult) |
| VA-*TOBACCO USE  SCREEN              | ZZVA-*TOBACCO USE  SCREEN              | Tobacco Use  Screen           | ZZ Tobacco Use  Screen           |
| VA-*WEIGHT AND NUTRITION SCREEN      | ZZVA-*WEIGHT AND NUTRITION SCREEN      | Weight and Nutrition Screen   | ZZ Weight and Nutrition Screen   |
| VA-ADVANCED DIRECTIVES EDUCATION     | ZZVA-ADVANCED DIRECTIVES  EDUCATION    | Advanced Directives Education | ZZ Advanced Directives Education |
| VA-ALCOHOL ABUSE EDUCATION           | ZZVA-ALCOHOL ABUSE EDUCATION           | Alcohol Abuse Education       | ZZ Alcohol Abuse Education       |

#### National Reminder Rescission and Renaming

| **Reminder Name**             | **New Name**                    | **Print Name**             | **New Print Name**            |
|-------------------------------|---------------------------------|----------------------------|-------------------------------|
| VA-BLOOD PRESSURE  CHECK      | ZZVA-BLOOD  PRESSURE CHECK      | Blood Pressure  Check      | ZZ Blood Pressure  Check      |
| VA-BREAST EXAM                | ZZVA-BREAST EXAM                | Breast Exam                | ZZ Breast Exam                |
| VA-BREAST SELF EXAM EDUCATION | ZZVA-BREAST SELF EXAM EDUCATION | Breast Self-Exam Education | ZZ Breast Self-Exam Education |

| **Reminder Name**                 | **New Name**                         | **Print Name**                 | **New Print Name**                |
|-----------------------------------|--------------------------------------|--------------------------------|-----------------------------------|
| VA-DIABETIC EYE  EXAM             | ZZVA-DIABETIC EYE  EXAM              | Diabetic Eye  Exam             | ZZ Diabetic Eye  Exam             |
| VA-DIABETIC FOOT CARE ED.         | ZZVA-DIABETIC FOOT CARE ED.          | Diabetic Foot Care Education   | ZZ Diabetic Foot Care Education   |
| VA-DIABETIC FOOT  EXAM            | ZZVA-DIABETIC FOOT  EXAM             | Diabetic Foot  Exam            | ZZ Diabetic Foot  Exam            |
| VA-DIGITAL RECTAL (PROSTATE) EXAM | ZZVA-DIGITAL  RECTAL (PROSTATE) EXAM | Digital Rectal (Prostate) Exam | ZZ Digital Rectal (Prostate) Exam |
| VA-EXERCISE  EDUCATION            | ZZVA-EXERCISE  EDUCATION             | Exercise Education             | ZZ Exercise  Education            |
| VA-FECAL OCCULT  BLOOD TEST       | ZZVA-FECAL OCCULT  BLOOD TEST        | Fecal Occult Blood  Test       | ZZ Fecal Occult  Blood Test       |
| VA- FLEXISIGMOIDOSCOPY            | ZZVA- FLEXISIGMOIDOSCOPY             | Flexisigmoidoscopy             | ZZ  Flexisigmoidoscopy            |
| VA-INFLUENZA  VACCINE             | ZZVA-INFLUENZA  VACCINE              | Influenza  Vaccine             | ZZ Influenza Vaccine              |
| VA-  MAMMOGRAM                    | ZZVA-MAMMOGRAM                       | Mammogram                      | ZZ Mammogram                      |
| VA-NUTRITION/OBESITY EDUCATION    | ZZVA- NUTRITION/OBESITY  EDUCATION   | Nutrition/Obesity Education    | ZZ Nutrition/Obesity Education    |
| VA-PAP SMEAR                      | ZZVA-PAP SMEAR                       | Pap Smear                      | ZZ Pap Smear                      |
| VA-PNEUMOVAX                      | ZZVA-PNEUMOVAX                       | Pheumovax                      | ZZ Pheumovax                      |
| VA-PPD                            | ZZVA-PPD                             | PPD                            | ZZ PPD                            |
| VA-PSA                            | ZZVA-PSA                             | PSA                            | ZZ PSA                            |
| VA-SEATBELT EDUCATION             | ZZVA-SEATBELT EDUCATION              | Seat Belt Education            | ZZ Seat Belt Education            |
| VA-TOBACCO  EDUCATION             | ZZVA-TOBACCO  EDUCATION              | Tobacco Cessation  Education   | ZZ Tobacco Cessation  Education   |
| VA-WEIGHT                         | ZZVA-WEIGHT                          | Weight                         | ZZ Weight                         |

**Exported National Reminders**

##### 1 VA-*IHD 412 ELEVATED LDL REPORTING

1. VA-*IHD 412 LIPID PROFILE REPORTING
2. VA-*IHD ELEVATED LDL REPORTING
3. VA-*IHD LIPID PROFILE REPORTING
4. VA-ANTIPSYCHOTIC MED SIDE EFF EVAL
5. VA-DEPRESSION SCREENING
6. VA-GEC REFERRAL CARE COORDINATION
7. VA-GEC REFERRAL CARE RECOMMENDATION
8. VA-GEC REFERRAL NURSING ASSESSMENT
9. VA-GEC REFERRAL SOCIAL SERVICES
10. VA-GEC REFERRAL TERM SET (CC)
11. VA-GEC REFERRAL TERM SET (CR)
12. VA-GEC REFERRAL TERM SET (NA)
13. VA-GEC REFERRAL TERM SET (SS)
14. VA-HEP C RISK ASSESSMENT

1. VA-HTN ASSESSMENT BP &gt;=140/90
2. VA-HTN ASSESSMENT BP &gt;=160/100
3. VA-HTN LIFESTYLE EDUCATION
4. VA-IHD ELEVATED LDL
5. VA-IHD LIPID PROFILE
6. VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN
7. VA-MST SCREENING
8. VA-NATIONAL EPI LAB EXTRACT
9. VA-NATIONAL EPI RX EXTRACT
10. VA-POS DEPRESSION SCREEN FOLLOWUP
11. VA-QUERI REPORT IHD ELEVATED LDL
12. VA-QUERI REPORT LIPID STATUS
13. VA-WH MAMMOGRAM REVIEW RESULTS
14. VA-WH MAMMOGRAM SCREENING
15. VA-WH PAP SMEAR REVIEW RESULTS
16. VA-WH PAP SMEAR SCREENING

**Exported National Dialogs**

1. VA-AIMS
2. VA-DEPRESSION ASSESSMENT
3. VA-DEPRESSION SCREEN
4. VA-GEC REFERRAL CARE COORDINATION
5. VA-GEC REFERRAL CARE RECOMMENDATION
6. VA-GEC REFERRAL NURSING ASSESSMENT
7. VA-GEC REFERRAL SOCIAL SERVICES
8. VA-HEP C RISK ASSESSMENT
9. VA-HTN ELEVATED BP&gt;140/90
10. VA-HTN ELEVATED BP&gt;160/100
11. VA-HTN LIFESTYLE EDUCATION
12. VA-IHD ELEVATED LDL
13. VA-IHD LIPID PROFILE
14. VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREENING
15. VA-MST SCREENING
16. VA-WH MAMMOGRAM REVIEW RESULTS
17. VA-WH MAMMOGRAM SCREENING
18. VA-WH PAP SMEAR REVIEW RESULTS
19. VA-WH PAP SMEAR SCREENING

**Appendix D: Status Enhancements**

The status field in the reminder definition has been modified to work with Reminder terms. Assumptions for the rules for this prompt:

1. The status field will not appear if the term has different types of finding items (e.g., Radiology procedure and a drug finding item)
2. If the term contains drug finding items or taxonomies, the user will see the status field, but they will not be able to edit the field if the values in the RX TYPE are different or the Taxonomy types are different.
3. If the Reminder Term contains drugs finding items, the only status that will display will be the status that corresponds to the RX TYPE at the term level. And a blank RX TYPE will be considered as if the user enters “ALL” at the RX TYPE.
4. The Reminder Definition RX TYPE will override the term RX TYPE. So if the user has set up multiple drug finding items in the term and the RX TYPE is set to Inpatient and then they set the RX TYPE at the definition level to Outpatient, the user will only be able to select statuses that correspond to a RX TYPE of Outpatient.

RXTYPE controls the search for medications. The possible RXTYPEs are: A - All

I - Inpatient

N - Non-VA meds O - Outpatient

You may use any combination of the above in a comma-separated list.

For example I,N would search for inpatient medications and non-VA meds.

The default is to search for all possible types of medications. So a blank RXTYPE is equivalent to A.

###### Default Statuses

| **Finding Type**    | **Status**        |
|---------------------|-------------------|
| Inpatient Pharmacy  | active            |
| Outpatient Pharmacy | active, suspended |
| Orderable Item      | active            |
| Problem List        | active            |
| Radiology           | active            |

Non-VA meds

Changes in the RXTYPE field were made to support the use of non-VA meds in Reminders.

“A” replaces the previous “B”. During the installation of V. 2.0, all “B” values will be changed to “A”. If RXTYPE is null, then it will be treated like an “A”. If RXTYPE includes non-VA meds, they will be searched for automatically, with no changes to the definition or term. This works as follows: Non-VA meds are stored by Pharmacy Orderable item and not by dispense drug; however, a dispense drug entry can have a pointer to the Pharmacy Orderable Item. If the pointer exists and RXTYPE allows it, then a search for the corresponding non-VA med will be made.

#### Status list

Version 2 provides a Status List for finding types that have a status:

- Inpatient pharmacy
- Outpatient pharmacy
- Orders
- Problem List
- Radiology

To be true, a finding has to have a status on the list, which is a change from V. 1.5, where status was not used for drugs. Your reminders that use these finding types may work differently in V. 2.0

###### Pharmacy Statuses

| **#**   | **Status**                   | **Description**                                                                                                                                            |
|---------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *       | Wildcard                     |                                                                                                                                                            |
| 1       | ACTIVE (NOI)                 | Rx is active – edit, renewal, D/C, copy, refill, partial etc., could be done                                                                               |
| 2       | DATE OF DEATH  ENTERED (N)   |                                                                                                                                                            |
| 3       | DELETED (O)                  | Manual delete by the supervisor – same as Rx does not exist; never shown in the profile or reports                                                         |
| 4       | DISCONTINUED (NOI)           | Any D/C via the backdoor –Manual D/C, D/C due to  Renewal, D/C due to duplicate drug, D/C due to Drug- Drug interaction                                    |
| 5       | DISCONTINUED (EDIT) (OI)     | Any edit through the backdoor for an active Rx that results in a new Rx will have this set. This will be displayed in the patient profile with status ‘DE’ |
| 6       | DISCONTINUED  (RENEWAL) (I)  |                                                                                                                                                            |
| 7       | DISCONTINUED BY PROVIDER (O) | D/C via CPRS by the provider                                                                                                                               |
| 8       | DONE (O)                     | Not used                                                                                                                                                   |
| 9       | DRUG INTERACTIONS (O)        | Pending due to Drug Interactions                                                                                                                           |
| 10      | EXPIRED (OI)                 | Expired Rx, copy, partials, D/C are allowed                                                                                                                |
| 11      | HOLD (OI)                    | When a Rx is put on hold, no action is allowed except D/C until it is taken off hold                                                                       |
| 12      | NON-VERIFIED (I)             | CPRS orders completed by a pharmacy tech. (not holding PSORPH key), need verification by a  Pharmacist (holder of PSORPH key)                              |
| 13      | NON-VERIFIED (O)             |                                                                                                                                                            |
| 14      | ON CALL (I)                  |                                                                                                                                                            |
| 15      | PROVIDER HOLD (O)            | On hold via CPRS by the provider                                                                                                                           |
| 16      | PURGE (I)                    |                                                                                                                                                            |
| 17      | REFILL (O)                   | Not used                                                                                                                                                   |
| 18      | REINSTATED (I)               |                                                                                                                                                            |
| 19      | RENEWED (I)                  |                                                                                                                                                            |

| 20   | SUSPENDED (O)   | An active Rx that has a future fill date   |
|------|-----------------|--------------------------------------------|

N=Non-VA Meds; O=Outpatient; I=Inpatient

**Editing a Status List**

You are prompted for a status only for those findings that have a status.

Select section to edit: **Findings**

Reminder Definition Findings Choose from:

DR	A AND D OINTMENT 2OZ RT	AGP LDL

Finding #: 2

Finding #: 1

Select FINDING: DR.A

Searching for a DRUG, (pointed-to by FINDING ITEM) A AND D OINTMENT 2OZ	DE350	TUBE

...OK? Yes//	(Yes) Editing Finding Number: 2

FINDING ITEM: A AND D OINTMENT 2OZ// REMINDER FREQUENCY:

MINIMUM AGE:

MAXIMUM AGE:

RANK FREQUENCY:

USE IN RESOLUTION LOGIC:

USE IN PATIENT COHORT LOGIC:

BEGINNING DATE/TIME:

ENDING DATE/TIME:

OCCURRENCE COUNT:

RXTYPE: A// CONDITION:

CONDITION CASE SENSITIVE:

USE COND IN FINDING SEARCH:

FOUND TEXT:

No existing text Edit? NO//

NOT FOUND TEXT:

No existing text Edit? NO//

Statuses already defined for this finding item: ACTIVE

DATE OF DEATH ENTERED

Select one of the following:

5

6

7

8

9

10

11

12

DISCONTINUED (EDIT) (OI) DISCONTINUED (RENEWAL) (I) DISCONTINUED BY PROVIDER (O) DONE (O)

DRUG INTERACTIONS (O) EXPIRED (OI)

HOLD (OI)

NON VERIFIED (I)

###### Example: (under Reminder Definition Management Option/RE Add/Edit Reminder Definition)

|   * | WildCard              |     |
|-----|-----------------------|-----|
|   1 | ACTIVE (NOI)          |     |
|   2 | DATE OF DEATH ENTERED | (N) |
|   3 | DELETED (O)           |     |
|   4 | DISCONTINUED (NOI)    |     |

1. NON-VERIFIED (O)
2. ON CALL (I)
3. PROVIDER HOLD (O)
4. PURGE (I)
5. REFILL (O)
6. REINSTATED (I)
7. RENEWED (I)
8. SUSPENDED (O)

Select a Medication Status from the status list or enter '^' to Quit: **1** ACTIVE (NOI)

Statuses already defined for this finding item: ACTIVE

Select one of the following:

A	ADD STATUS

D	DELETE A STATUS

DA	DELETE ALL STATUSES

S	SAVE AND QUIT

Q	QUIT WITHOUT SAVING CHANGES

Enter response: **a** ADD STATUS

Select one of the following:

*	WildCard

1. ACTIVE (NOI)
2. DATE OF DEATH ENTERED (N)
3. DELETED (O)
4. DISCONTINUED (NOI)
5. DISCONTINUED (EDIT) (OI)
6. DISCONTINUED (RENEWAL) (I)
7. DISCONTINUED BY PROVIDER (O)
8. DONE (O)
9. DRUG INTERACTIONS (O)
10. EXPIRED (OI)
11. HOLD (OI)
12. NON VERIFIED (I)
13. NON-VERIFIED (O)
14. ON CALL (I)
15. PROVIDER HOLD (O)
16. PURGE (I)
17. REFILL (O)
18. REINSTATED (I)
19. RENEWED (I)
20. SUSPENDED (O)

Select a Medication Status from the status list or enter '^' to Quit: **2** DATE OF DEATH ENTERED (N)

Statuses already defined for this finding item: ACTIVE

DATE OF DEATH ENTERED

Select one of the following:

A	ADD STATUS

D	DELETE A STATUS

DA	DELETE ALL STATUSES

S	SAVE AND QUIT

Q	QUIT WITHOUT SAVING CHANGES

Enter response:

ADD STATUS DELETE A STATUS

DELETE ALL STATUSES SAVE AND QUIT

QUIT WITHOUT SAVING CHANGES

A D DA S Q

Select one of the following:

Enter response: **S** SAVE AND QUIT Removing old Statuses from the file Adding current status list to the file

Statuses already defined for this finding item: ACTIVE

DATE OF DEATH ENTERED

#### New reminder status:

##### CNBD for CanNot Be Determined. Clinical Maintenance display.

The “Information about the reminder evaluation:” section is new.

A warning message will be sent when the status can’t be determined.

Example:

Subj: Reminder evaluation warnings	[#37193] 10/25/04@10:55	5 lines From: POSTMASTER (Sender: CRPROVIDER,ONE G)	In 'IN' basket.		Page

1	*New*

The following warnings were encountered:

No reminder frequency - cannot compute due date! While evaluating reminder JG-DEMO REMINDER

For patient DFN=54

The time of the evaluation was 10/25/2004@10:55:18

Enter message action (in IN basket): Ignore//

### Index

AAC SAS Files, 79

Acronyms, 79

Action, 39

Allocation Errors, 75

APPENDIX B: Glossary— Acronyms and Definitions, 79

APPENDIX A: Hints and Tips, 71 APPENDIX C: NATIONAL REMINDERS

RESCISSION, 82

APPENDIX D: Status Enhancements, 86 Applicable, 79

Automatic QUERI Extracts/ Transmission, 29

Chapter 1: IHD and MH Phase 2 Setup, 15 Chapter 2: Set up VA-Geriatric Extended

Care (GEC) Referral, 33, 48, 49, 50 Chapter 3: Code Set Versioning Changes in

Reminders, 53

Chapter 4: My HealtheVet, 62 Child Note Titles, 44

Code Set Versioning Changes in Reminders, 53

Computed Finding – Location, 74 CONDITION Enhancements, 2

CPT, 53

Custom Date Due, 2 Default Statuses, 86

Definitions, 79

Dialog Taxonomies, 59

Drug for patient cohort logic, 74 Due, 79

Edit Taxonomy Item’s ICD0 Low and High Code Example, 56

Exported National Dialogs, 85 Exported National Reminders, 84 Extract Parameter, 79

Extract Run, 80

Extract Summary, 27, 79 Finding Count Rules, 80 finding date search, 2 Finding Group, 80

Forced Value in Dialogs, 71 GEC, 33, 34, 48, 49, 50

GEC Consult Order, 35 GEC Health Factors, 34

GEC Interdisciplinary Notes, 44 GEC Referral Ad hoc Reports, 50

GEC Referral Reminders, 35 GEC Referral Reports, 51 GEC Reminder Terms, 51

GEC Status Check, 46, 47, 48, 49, 50

Glossary, 79

Health Information Portability and Accountability Act (HIPAA), 53

HIPAA, 53

HL LOGICAL LINK, 28

HL7 Transmissions, 80

ICD0, 53

ICD9, 53

IHD Reminder Definitions, 15

IHD terms that *must* be mapped, 18, 19 Impact on Sites, 11, 12, 13

Inactive Codes Mail Message, 58 List Rules, 80

Location List finding, 2

logical Link in the HL7 package, 28 mail messages, 30

manual run, 25, 26

Map local findings, 18, 22, 23

Mental Health Reminder Terms, 22, 23 Mental Health Reminders, 16

MH Term Mapping,  24 National Acronym Directory, 79 National Dialogs, 85

National Reminders, 84

NATIONAL REMINDERS RESCISSION, 82

Not Applicable, 80

Outpatient Pharmacy Statuses, 87 Patient List, 80

patient lists, 28

Pre-mapped Terms, 19, 20

Print labels, 71

PXRM EXTRACT MANAGEMENT, 25, 26

PXRMCS INACTIVE DIALOG CODES, 58

Rank Frequency, 76

Reminder Definitions, 80

Reminder Dialog, 25, 80 Reminder Patient List, 80

Reminder report on an individual finding item, 71

Reminder Terms, 80

Reminder Test, 25

Reminder Totals, 80 Reminders Due Report, 25 Report Reminders, 81 Reporting Period Extract, 81

Set Up Consult Services (SS), 39 Standards Development Organization

(SDO), 53

Status list, 2, 87

Statuses, 87

Taxonomy option changes, 55, 56, 57

Test option, 2

TIU Document Definitions, 44 TIU Interdisciplinary (ID) note, 44 Transmission History, 30

Transmission Run, 81

VA-*IHD 412 ELEVATED LDL REPORTING, 16

VA-*IHD 412 LIPID PROFILE REPORTING, 16

VA-*IHD ELEVATED LDL REPORTING, 15

VA-*IHD LIPID PROFILE REPORTING, 15

VA-ANTIPSYCHOTIC MED SIDE EFF

EVAL Terms, 23

VA-DEPRESSION SCREENING Terms, 22

VA-Geriatric Extended Care, 33, 34, 48, 49,

50

VA-IHD ELEVATED LDL, 15 VA-IHD LIPID PROFILE, 15

VA-POS DEPRESSION SCREEN FOLLOWUP Terms, 23

WYSIWYG, 73