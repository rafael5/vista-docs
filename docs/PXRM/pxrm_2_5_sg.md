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
source_file: pxrm_2_5_sg.docx
status: draft
title: pxrm 2 5 sg.docx
---

<!-- image -->

**Clinical Reminders**

**OEF/OIF**

### Patch PXRM*2.0*5

**SETUP GUIDE**

### December, 2005

##### Health Data Systems VISTA HSD&amp;D


**Revision History**

| **Revision Date**   | **Page or Chapter**   | **Description**                 | **Author**   |
|---------------------|-----------------------|---------------------------------|--------------|
| December, 2005      |                       | Updates to accommodate Patch 5. |              |

**Table of Contents**

Introduction	1

**Table of Contents**

Purpose of This Guide	1

Target Audience	1

Sources of Information	1

Overview of the Project	2

Post-Installation and Setup Steps	6

1. Verify correct installation of the packed reminder.	6

Setup Steps	10

Term Mapping	10

1. Map local findings to the national Reminder Terms.	11
2. Run the Reminder Test option after term definition mapping is completed.	17
3. Use the Reminder Dialog options to edit the national (exported) dialogs.	18
4. Use ORWPCE EXCLUDE HEALTH FACTORS.	21
5. Verify that the reminders function properly.	22
6. Add the OEF/OIF reminder to the CPRS Cover Sheet.	24

Appendix: Iran &amp; Afghan Post-Deployment Screen Reminder Definition and Dialog Examples	27

Index	47

## Introduction

| **Purpose of This Guide**   | This Setup Guide is designed to help you prepare your site for the implementation of the new OEF/OIF Reminder. It includes detailed information about procedures that will get you up and running with this project.  **Target Audience**  We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:  - Information Resources Management (IRM) - Clinical Application Coordinator (CAC) - Enterprise **V** *IST* **A** Support (EVS) - Software Quality Assurance (SQA)   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sources of Information**  | You can retrieve documentation from the following websites:  [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders)  Clinical Reminders main web page  [http://www.va.gov/vdl](http://www.va.gov/vdl)  **V**  *IST*  **A**  Documentation Library (VDL)                                                                                                                                                                                                                                                                                            |

**Introduction**

| **Overview of the Project**  The Clinical Reminder,  *Iraq &amp; Afghan Post- Deployment Screen,*  was originally released with Patch 21 (PXRM*1.5*21).   | **Operation Enduring Freedom and Operation Iraqi Freedom**  The Clinical Reminder,  *Iraq &amp; Afghan Post-Deployment Screen,*  which identified veterans of Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom  *,*  has  been enhanced to take advantage of capabilities offered by the recent release of Clinical Reminders Version 2.0. The OEF/OIF data will be rolled up for regional and national reporting purposes. Due to the fast track that this project has been placed on, the project will be completed in two phases.  - **Phase I** include modifications and enhancements to the current Afghan/Iraq reminder to better meet the needs of the field and provide the information needed for reporting purposes. In Phase I, the clinical reminder for post- deployment screening will be due for patients whose latest Separation date greater than 09/11/01. It is also due for active duty patients being seen at the VA.  **Phase II Extract Reports &amp; National Rollup of Data**  - Phase II is dependent on changes being made by Management Services to improve the quality and accuracy of a patient’s OEF and OIF combat data. The OEF/OIF Enrollment SRS will define functionality that will manage OEF/OIF Combat Veteran data. Management Systems will require OEF/OIF patients to first be a combat veteran with a combat from and to date, where the combat to date ends after 10/07/01, and secondarily have an OEF or OIF indication if the patient served in the OEF or OIF theatre during the combat service period. Patient combat data will be collected by clerks during enrollment, registration, or the first VA visit. Phase II Reminder development will be coordinated with Enrollment development to use the Combat Veteran data.  - Phase II includes distribution of the national OEF/OIF clinical reminder/dialog again.  - In Phase II, the clinical reminder for post-deployment screening will be due for patients whose latest Separation date greater than 09/11/01, or patients whose latest combat end date was greater than 10/07/01 for service in the OEF or OIF combat theatre. The reminder will continue to also be due for active duty patients being seen at the VA.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Introduction, cont’d**

- Phase II will also include new OEF/OIF national reporting reminders, which will be used for roll-up of OEF/OIF totals to the Austin Automation Center (AAC). The project is restricted to use of existing Reminder Extract and HL7 messaging tools. The national reminder data sent to AAC will be totals only. No patient information will be sent to AAC. The new OEF/OIF transmission will be coordinated with AAC development.

- AAC will store facility results from regularly scheduled automated OEF/OIF national reporting for subsequent evaluation using SAS tools.

- A Clinical Reminder patch (PXRM*2*6) will include changes required to support new reporting extract requirements, as well as Reminder Extract Parameters, and Reporting Reminder definitions.

**Introduction, cont’d**

| **Overview of Patch 5**   | **VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN reminder**  This patch re-releases the VA-IRAQ &amp; AFGHAN POST- DEPLOY SCREEN reminder. Some of the changes to the reminder are:  1. Each section can now be done individually so that one user may do part and someone else may do another piece. This means that someone may do a section and the reminder will remain due until all questions are complete.  1. If a section has been done recently (past 6 months) then it will be displayed in a closed format with a message that this was done recently and the user can click to open and repeat.  1. The clinical maintenance display will always show which pieces are complete and which are still pending.  1. The PTSD screen has been changed to capture the answers to the 4 questions as individual health factors so that the users do not have to do the scoring themselves.  1. The first question has been modified to capture OEF vs. OIF service and when one of these 2 options is chosen then the user has to choose one country for the most recent service.  1. Once the OEF vs. OIF service is captured (first question answered), this question is not asked again if the reminder is re-entered to complete other sections. This section will be displayed in a 'closed' format.  1. There are refusal options for all four sections.  1. There is a new computed finding for VA-PATIENT TYPE. This can be used (if a site chooses) to include active duty personnel in the cohort to be screened. The CF looks at the 'TYPE' field in the patient file.   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Introduction, cont’d**

**Reminder Changes, cont’d**

9.	There is a URL in the reminder dialog that links to a paper copy of the questionnaire that can be used to obtain the information from the patients without having to read the questions to them. If you want to save a copy of this MS Word document on a local server, you can change the URL in the template field to point to your local server.

This reminder will be placed in the REMINDER EXCHANGE file (#811.8). VA-IRAQ &amp; AFGHAN POST- DEPLOY SCREEN

A new Reminder Sponsor "Office of Public Health and Environmental Hazards" is being released with this patch.

A change was made to the Data Dictionary Structure for file #811.6. This change was done to make the structure similar to the other reminder files.

## Post-Installation and Setup Steps

| 1. **Verify correct installation of the packed reminder.**  The post-install routine, PXRMP5I, installs the packed reminders into your Exchange File. If you discover that the reminders didn’t get installed, you can use the Reminders Exchange options on the Reminders Manager Menu to install the “packed” reminders.  1. Using *Inquire about Reminder Definition* on the Reminder Management Menu, ensure that the four reminder definitions have been installed. Review the reminders to become familiar with the definitions and terms.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Reminder Managers Menu Option:  **RM**  Reminder Definition Management  RL	List Reminder Definitions  RI	Inquire about Reminder Definition RE	Add/Edit Reminder Definition  RC	Copy Reminder Definition  RA	Activate/Inactivate Reminders  Select Reminder Definition Management Option:  **RI**  Inquire about Reminder Definition  Select Reminder Definition:  **VA-Iraq&amp;Afghan Post-Deployment**  **Screen**                                                                                                                        |
| You cannot make changes to this national reminder. You may copy the national reminder to a local reminder definition name and make any changes necessary.                                                                                                                                                                                                                                                                                                                                                                                          |

**Post-Installation &amp; Setup (cont’d)**

1. Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:

**Terms**

1. VA-IRAQ/AFGHAN SERVICE NO
2. VA-IRAQ/AFGHAN PERIOD OF SERVICE
3. VA-IRAQ/AFGHAN SERVICE
4. VA-DEPRESSION SCREEN NEGATIVE
5. VA-DEPRESSION SCREEN POSITIVE
6. VA-ALCOHOL USE SCREEN
7. VA-PTSD SCREEN
8. VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)
9. VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
10. VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)
11. VA-PERSISTENT RASH (IRAQ/AFGHANISTAN)
12. VA-PTSD AVOIDANCE ALL
13. VA-PTSD DETACHMENT ALL
14. VA-PTSD NIGHTMARES ALL
15. VA-PTSD ON GUARD ALL
16. VA-REFUSED PTSD SCREEN
17. VA-REFUSED ALCOHOL SCREENING
18. VA-REFUSED DEPRESSION SCREENING
19. VA-REFUSED ID &amp; OTHER SX SCREEN
20. VA-ACTIVE DUTY

**VA FileMan Print from the Reminder Term File**

You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

**Post-Installation &amp; Setup (cont’d)**

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                         | **c. Verify that the VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN dialog is installed on your system.**   |      |                                                     |                                                     |    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------|-----------------------------------------------------|-----------------------------------------------------|----|
| Select Reminder Managers Menu Option:  **DM**  Reminder Dialog Management DP	Dialog Parameters ...  DI	Reminder Dialogs DR	Dialog Reports ...  IA	Inactive Codes Mail Message  Select Reminder Dialog Management Option:  **DI**  Reminder Dialogs  Dialog List	Sep 22, 2005@11:35:09	Page:	1 of	25 REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog Status  1. A A BLOOD EXPOSURE	DIABETIC EXAM DIALOG 2. A NEW REMINDER	A NEW REMINDER	Disabled 3. AGETEST	VA-HEPC AUTOGENERATE TEST 4. ANY CHOLESTEROL SCREEN (M)	ANY CHOLESTEROL SCREEN (M 5. ANY'S ANNUAL FLU SHOOT	ANY'S ANNUAL FLU SHOOT                                                                                                                                                                                                                               |                                                                         |                                                                                                               |      |                                                     |                                                     |    |
| **+**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Enter ?? for more actions**                                           |                                                                                                               |      |                                                     | **&gt;&gt;&gt;**                                    |    |
| AR	All reminders	LR	Linked Reminders	QU	Quit CV	Change View	RN	Name/Print Name  Select Item: Next Screen//  **CV**  Change View	Use CV – Change View to  change to a Dialog view.  Select one of the following:  1. Reminder Dialogs 2. Dialog Elements 3. Forced Values 4. Dialog Groups  P	Additional Prompts  R	Reminders  RG	Result Group (Mental Health) RE	Result Element (Mental Health)  TYPE OF VIEW: R// D	Reminder Dialogs  **Dialog List**  Sep 22, 2005@11:35:09	Page:	1 of	13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  Item Reminder Dialog Name	Source Reminder	Status  1. 571B	SMOKING CESSATION EDUCATI 2. Agetest	Agetest	Disabled 3. BLOOD PRESSURE CHECK	BLOOD PRESSURE CHECK	Linked 4. DIABETIC EXAM DIALOG	A A BLOOD EXPOSURE	Linked 5. Diabetic Foot Inspection Exam	VISN 12 Diabetic Foot Ins Linked 6. EDUTEST	EDUTEST	Disabled |                                                                         |                                                                                                               |      |                                                     |                                                     |    |
| **+**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **+ Next Screen	- Prev Screen	?? More Actions**                         |                                                                                                               |      | **&gt;&gt;&gt;**                                    |                                                     |    |
| AD CV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Add Reminder Dialog PT	List/Print All	QU Change View	RN	Name/Print Name | Add Reminder Dialog PT	List/Print All	QU Change View	RN	Name/Print Name                                       | Quit |                                                     |                                                     |    |
| Select Item: Next Screen//  **SL**  SL  Search for:  **VA-Iraq**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                         |                                                                                                               |      | Use SL-Search List to jump to the reminder dialogs. | Use SL-Search List to jump to the reminder dialogs. |    |

**Post-Installation  &amp; Setup (cont’d)**

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **c. (cont’d) Verify that the Iraq &amp;Afghan dialog is installed on your system.**  **NOTE**  : Do not autogenerate dialogs for the reminders. Dialogs are included with the packed reminder installation.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dialog List	Sep 22, 2005@11:35:34	Page:	14 of	16**  **DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)**  **+Item Reminder Dialog Name	Source Reminder	Status**  1. **VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked** 2. **VA-MST SCREENING	*NONE*	Linked** 3. **VA-PNEUMOVAX	VA-PNEUMOVAX	Linked** 4. **VA-PPD	VA-PPD	Linked** 5. **VA-PSA	VA-PSA	Disabled** 6. **VA-SEATBELT EDUCATION	VA-SEATBELT EDUCATION	Disabled** 7. **VA-WH MAMMOGRAM REVIEW RESULTS	VA-WH MAMMOGRAM REVIEW RE Linked** 8. **VA-WH MAMMOGRAM SCREENING	VA-WH MAMMOGRAM SCREENING Linked** 9. **VA-WH PAP SMEAR REVIEW RESULTS	VA-WH PAP SMEAR REVIEW RE Linked** 10. **VA-WH PAP SMEAR SCREENING	VA-WH PAP SMEAR SCREENING Linked** |                                                                                                                                                                                                                |
| **+	Enter ?? for more actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                |
| Find Next ‘VA Iraq’? Yes//  **no**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                |

## Setup Steps

| **If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.**   | **Term Mapping**  All of the individual elements of the screening tool are exported with attached health factors and reminder terms.  The national health factors and reminder terms for the 2-question depression screen are used for the depression screening.  The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal.  Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.  The Health Factors for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Mapping terms**

#### 1 Map local findings to the national Reminder Terms.

*Option: Reminder Term Management* on the *Reminder Management Menu.*

Before using the OEF/OIF reminder, map the local findings your site uses to represent the national reminder terms, if necessary.

**Exported Terms**

1. VA-ACTIVE DUTY
2. VA-ALCOHOL USE SCREEN
3. VA-DEPRESSION SCREEN NEGATIVE
4. VA-DEPRESSION SCREEN POSITIVE
5. VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)
6. VA-IRAQ/AFGHAN PERIOD OF SERVICE
7. VA-IRAQ/AFGHAN SERVICE
8. VA-IRAQ/AFGHAN SERVICE NO
9. VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
10. VA-PERSISTENT RASH (IRAQ/AFGHANISTAN)
11. VA-PTSD AVOIDANCE ALL
12. VA-PTSD DETACHMENT ALL
13. VA-PTSD NIGHTMARES ALL
14. VA-PTSD ON GUARD ALL
15. VA-PTSD SCREEN
16. VA-REFUSED ALCOHOL SCREENING
17. VA-REFUSED DEPRESSION SCREENING
18. VA-REFUSED ID &amp; OTHER SX SCREEN
19. VA-REFUSED PTSD SCREEN
20. VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

**Mapping terms**

If desired, add local Health Factors or education topics representing these terms.

| **Term**                          | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-ACTIVE DUTY                    | This new reminder term is available to allow active duty patients to be part of the cohort. This term contains a computed finding for VA-PATIENT TYPE, which can be used to include active duty patients. Sites that do not screen  active duty patients may remove the computed finding from this reminder term.                                                                                                                                                                                                                |
| VA-ALCOHOL USE SCREEN             | Add: Any local health factors for AUDIT-C, refusal of alcohol screening, or no alcohol in the past year.  The Mental Health tests for AUDIT-C and CAGE are already included in this term. If your site uses the 10 question AUDIT, then this should also be added to this term.                                                                                                                                                                                                                                                  |
| VA-DEPRESSION SCREEN NEGATIVE     | Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for negative depression screening should have already been mapped to this term when the national MH reminders were installed.  Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this  term. |
| VA-DEPRESSION SCREEN POSITIVE     | Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for positive depression screening should have already been mapped to this term when the national MH reminders were installed.  Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term.  |
| VA-GI SYMPTOMS (IRAQ/AFGHANISTAN) | This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items  should be added to this term.                                                                                                                   |

**Mapping terms**

| **Term**                               | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA- IRAQ/AFGHAN PERIOD OF SERVICE      | This term contains a computed finding that determines if the patient’s most recent service separation date was after 9/11/01. The computed finding is included to define the cohort of patients who need to be asked about service in the combat  arena.                                                                                                                                                                            |
| VA- IRAQ/AFGHAN SERVICE                | This term contains the health factor that is entered  from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at sea).                                                                                                                                                                                                                                                                 |
| VA- IRAQ/AFGHAN SERVICE NO             | This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air or at sea).  This health factor resolves the reminder.                                                                                                                                                                                                                             |
| VA- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)  | This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered. Separate health factors representing positive and negative answers to the question are included in this term.  Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.         |
| VA- PERSISTENT RASH (IRAQ/AFGHANISTAN) | This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to  this term. |
| VA-PTSD AVOIDANCE ALL                  |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VA-PTSD DETACHMENT ALL                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VA-PTSD NIGHTMARES ALL                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VA-PTSD ON GUARD ALL                   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VA-PTSD SCREEN                         | If your site does PTSD screening, map any local health factors or exams that represent positive or  negative screens for PTSD                                                                                                                                                                                                                                                                                                       |
| VA-REFUSED ALCOHOL SCREENING           |                                                                                                                                                                                                                                                                                                                                                                                                                                     |

| **Term**                             | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-REFUSED DEPRESSION SCREENING      |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VA-REFUSED ID & OTHER SX SCREEN      |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VA-REFUSED PTSD SCREEN               |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) | This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered. Separate health factors representing positive and negative answers to the question are included in this term.  Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term. |

**Mapping terms**

| **Example**   | **2. Map local findings to the national Reminder Terms (cont’d).**  *Option: Add/Edit Reminder Term on Reminder Term Management Menu.*   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|

to by FINDING ITEM)

**Example: Mapping a Local Health Factor Finding to the National Reminder Term**

| Select Reminder Term Management Option:  **te**  Add/Edit Reminder Term  Select Reminder Term:  **VA-ALCOHOL USE SCREEN**  NATIONAL  ...OK? Yes//	(Yes)                                                                                                                                                                                           |                                                                                                                     |    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----|
| Select FINDING ITEM:  **10-Question Audit**                                                                                                                                                                                                                                                                                                       | Enter local health factors or exams that your site uses to represent positive or negative  screens for alcohol use. |    |
| Searching for a MENTAL HEALTH INSTRUMENT, (pointed-  Searching for a MENTAL HEALTH INSTRUMENT TENS                                                                                                                                                                                                                                                |                                                                                                                     |    |
| ...OK? Yes//	(Yes)  Are you adding 'TENS' as a new FINDINGS (the 6TH for this REMINDER TERM)? No//  **Y**  (Yes)  Editing Finding Number: 6	FINDING ITEM:  **10-Question Audit**  EFFECTIVE PERIOD:  USE INACTIVE PROBLEMS: WITHIN CATEGORY RANK: EFFECTIVE DATE:  MH SCALE: CONDITION:  CONDITION CASE SENSITIVE: RX TYPE:  Select FINDING ITEM: |                                                                                                                     |    |

**Mapping terms**

**Example**

**2. Map local findings to the national Reminder Terms (cont’d).**

Select Reminder Managers Menu Option: TRM	Reminder Term Management

*Option: Add/Edit Reminder Term on Reminder Term Management Menu.*

Removing computed finding from VA-Active Duty term.

The VA-Active Duty term is included in the OEF/OIF Post- Deployment Reminder in order to allow sites to screen active duty patients. The computed finding VA-PATIENT TYPE is included in this term and has a condition set to find active duty patients. If a pati is listed as active duty in the TYPE field in the patient file (field 391) then this finding will be true and the reminder will be due.

TL	List Reminder Terms

TI	Inquire about Reminder Term TE	Add/Edit Reminder Term

If a site chooses not to screen active duty personnel, this CF should be removed from the reminder term.

TC	Copy Reminder Term

Select Reminder Term Management Option: TE	Add/Edit Reminder Term

Select Reminder Term: **VA-ACTIVE DUTY** NATIONAL

...OK? Yes// **&lt;Enter&gt;** (Yes) Choose from:

CF	VA-PATIENT TYPE	Finding #: 1

Select Finding: **VA-PATIENT**

Computed Finding Description:

This computed finding is a single value computed finding. If a patient type is found for the patient the computed finding will be true and type will be returned as the Value.

Example: I V="ACTIVE DUTY"

Possible Values that can be returned from this computed finding are: ACTIVE DUTY

ALLIED VETERAN COLLATERAL EMPLOYEE MILITARY RETIREE

NON-VETERAN (OTHER) NSC VETERAN

SC VETERAN TRICARE

Editing Finding Number: 1

FINDING ITEM: VA-PATIENT TYPE// **@**

SURE YOU WANT TO DELETE THE ENTIRE FINDING ITEM? **Y** (Yes)

Reminder Term has no findings

Select Finding:

ent

,

**Testing the Reminder**

| **Test the reminder**                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **3. Run the Reminder Test option after term definition mapping is completed.**  **Review the results of patient data with each of the findings mapped to the term.**  *Option: Reminders Test*  on the  *Reminder Managers Menu*  Select Reminder Managers Menu Option:  **RT**  Reminder Test Select Patient:  **CRPATIENT,SIX**  4-30-44  666809999	YES	EMPLOYEE  Enrollment Priority: GROUP 5	Category: IN PROCESS End Date:  Select Reminder: VA-Iraq&amp;Afghan Post-deployment Screen |

**Editing the Dialog**

1. **Use the Reminder Dialog options to edit the national (exported) dialogs.**

After mapping local findings to the national terms, determine whether to use local findings as the data elements that are captured, or the national findings that are already mapped to the national terms. Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs. Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.

- If using local findings, edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding.

Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.

- Add local dialog elements with local Order Dialogs for additional ordering options for the clinicians. Some sites have clinicians order a consult to a service that provides PAP smears. If your site does this, copy the reminder dialog to a local reminder dialog and then add the local dialog element for the consult order to the reminder dialog so this practice can continue.

The national reminders and dialogs can ***only*** be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

**Editing the Dialog**

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Steps to add or edit dialog elements:**  a. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI) and Change View (CV) to see the Dialog view:   |                                                   |    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----|
| Select Reminder Managers Menu Option:  **DM**  Reminder Dialog Management DP	Dialog Parameters ...  DI	Reminder Dialogs DR	Dialog Reports ...  IA	Inactive Codes Mail Message  Select Reminder Dialog Management Option:  **DI**  Reminder Dialogs  Dialog List	Mar 24, 2004@08:52:46	Page:	1 of	18 REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog Status  1. A BLOOD EXPOSURE	DIABETIC EXAM DIALOG 2. A NEW REMINDER	A NEW REMINDER	Disabled 3. AGP ABNORMAL WH STUFF                                                                                                                                                                                                                              |                                                                                                                                                                                     |                                                   |    |
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                     | **&gt;&gt;&gt;**                                  |    |
| AR	All reminders	LR	Linked Reminders	QU	Quit CV	Change View	RN	Name/Print Name  Select Item: Next Screen//  **CV**  Select one of the following:	Select Change View (CV) to change to the  1. Reminder Dialogs	Dialog View 2. Dialog Elements 3. Forced Values 4. Dialog Groups  P	Additional Prompts  R	Reminders  RG	Result Group (Mental Health) RE	Result Element (Mental Health)  TYPE OF VIEW: R//  **D**  Reminder Dialogs  AD	Add Reminder Dialog	PT	List/Print All	QU	Quit  Dialog List	Mar 24, 2004@08:47	Page:	1 of	14 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  Item Reminder Dialog Name	Source Reminder	Status  1. A NEW BP CHECK	*NONE*	Disabled 2. A NEW REMINDER	*NONE*	Disabled 3. A NEW REMINDER DIALOG	*NONE* |                                                                                                                                                                                     |                                                   |    |
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                     | **&gt;&gt;&gt;**                                  |    |
| CV	Change View	RN	Name/Print Name Select Item: Next Screen//  **SL**  SL  Search for:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                     | Select SL (Search List) to jump to the WH dialogs |    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                     |                                                   |    |

**Editing the Dialog**

1. **E**

**Exclude Health Factors from Encounter Forms**

**Testing the Reminder**

| **Test Reminder**   | 1. **Verify that the reminders function properly.**  1. Run a Reminders Due Report to determine if the statuses reported are correct.  *Option: Reminders Due*  on the  *Reminder Reports menu*  This report can be displayed at the beginning of the day for patients being seen that day. Reminder reports offer a way to review how the mapping and the local data will potentially be viewed by the extracts that will be sent to the Austin database from the reminders.  - The reminder can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder. - The report can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved. - Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.  1. Use the Reminder Test option to test the reminder.  *Option: Reminders Test*  on the  *Reminder Management menu*  1. Select a patient who had a screening done within the past year. Run the Reminder Test option on the VA-IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREENING reminder definition. The status of the reminder should be “RESOLVED.” Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “RESOLVED.”   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Test Reminder**

| **Test Reminder**   | 3. Select a patient whose most recent screening took place within the past year and the results have been recorded.  Run the Reminder Test option on VA- Iraq &amp; Afghan Post- Deployment Screen reminder definition.  The status of the reminder should be “Applicable.”  Use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “Applicable.”   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Add Reminder to Cover Sheet**

| **Add Reminder to CPRS Cover Sheet**  NOTE: Make sure that New Reminders Parameter on the CPRS Configuration Menu is set to Yes. This is a prerequisite for using the “Edit Cover Sheet Reminder List” functionality.   | 1. **Add the OEF/OIF reminder to the CPRS Cover Sheet.**  1. Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Edit Cover Sheet Reminder List option

Action option

Reminders Clock

**CRPROVIDE**

**RPROVIDER,ONE**

**PROVIDER,ONE**

**CRPROVIDER,ONE**

**R,ONE**

**CRUSER,**

**CRUSER, CRUSER,**

**CRUSER,**

**Setup Guide**

| **Add Reminder to CPRS Cover Sheet**   | **Adding Reminder to Cover Sheet, cont’d**  1. When the Cover Sheet Reminder List opens, set the Cover sheet parameter level. Click on the System, Division, Service, User Class, and/or User buttons, as appropriate for your site.  1. Locate and click on the VA-IRAQ &amp; AFGHAN DEPLOY SCREENING reminder; click the Add button (or double-click the reminder).   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **CRPROVIDER,ONE**   |    |
|----------------------|----|
| **C CRPROVIDER,ONE** |    |
| **C CRPROVIDER,ONE** |    |
| **CRCRPROVIDER,ONE** |    |

**Setup Guide**

| **Add Reminder to CPRS Cover Sheet**   | **Adding Reminder to Cover Sheet, cont’d**  d. Click on the VA-IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREEN reminder and click the Add button (or double-click the reminder).   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

CRUSER,ONE

## Appendix: Iran &amp; Afghan Post-Deployment Screen Reminder Definition and Dialog Examples

**Reminder Definition**

REMINDER DEFINITION INQUIRY	Sep 20, 2005 10:39:39 am	Page 1

VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN No.	568022

Print Name:	Iraq&amp;Afghan Post-Deployment Screen

Class:	NATIONAL

Sponsor:

Review Date:

Rescission Date:

Usage:	CPRS, REPORTS

Related VA-* Reminder:

Reminder Dialog:	VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Priority:

Reminder Description:

Patients who served in combat in either Operation Iraqi Freedom (Iraq, Kuwait, Saudi Arabia, Turkey) or in Operation Enduring Freedom (Afghanistan, Georgia, Kyrgyzstan, Pakistan, Tajikistan, Uzbekistan, The Philippines) should be screened for illnesses related to their service. Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

COHORT: veterans with separation date after 9/11/01.	This finding is part of the reminder term: VA-IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

An additional reminder term VA-ACTIVE DUTY is also available to cause patients to be part of the cohort.	This term contains a computed finding for VA-PATIENT TYPE which can be used to include active duty patients.

Sites that do not screen active duty patients may remove the computed finding from this reminder term.

RESOLUTION: entry of a health factor for NO IRAQ/AFGHAN SERVICE which is found in the reminder term IRAQ/AFGHAN SERVICE NO will resolve the reminder.	If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE) then

1. the area of service by country must be answered and 2. all the other items are required to resolve the reminder and must be completed after the date of the most recent service separation:
    1. screen for PTSD,

1. screen for depression,
2. screen for alcohol use,
3. all 4 screening questions related to infectious diseases and other symptoms.

The clinical maintenance will display information on which portions of the screen are not yet completed.

All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2 question depression screen are used for the depression screening.	The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal. Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening.	If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.

The HFs for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog.	Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms.	Entry of these health factors should ONLY occur during reminder dialog use.

Technical Description:

Baseline Frequency:

Do In Advance Time Frame:	Wait until actually DUE Sex Specific:

Ignore on N/A:

Frequency for Age Range:	99Y - Once for all ages Match Text:

No Match Text:

Findings:

---- Begin: VA-IRAQ/AFGHAN SERVICE NO	(FI(1)=RT(489)) -------------------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Mapped Findings:

Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

End: VA-IRAQ/AFGHAN SERVICE NO

---- Begin: VA-IRAQ/AFGHAN PERIOD OF SERVICE	(FI(2)=RT(490)) ------------

Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

Beginning Date/Time: SEP 11, 2001

Mapped Findings:

Mapped Finding Item: CF.VA-DISCHARGE DATE Beginning Date/Time: SEP 11, 2001

---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

---- Begin: VA-IRAQ/AFGHAN SERVICE	(FI(3)=RT(568012)) -------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

End: VA-IRAQ/AFGHAN SERVICE

---- Begin: VA-DEPRESSION SCREEN NEGATIVE	(FI(4)=RT(80)) ----------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.DEP SCREEN 2 QUESTION NEG Health Factor Category: MENTAL HEALTH

Mapped Finding Item: MH.DOM80

Condition: I V=0

Mapped Finding Item: MH.DOMG

Condition: I V&lt;4

Mapped Finding Item: MH.CRS

MH Scale: 1 Condition: I V&lt;10

Mapped Finding Item: MH.BDI

MH Scale: 1 Condition: I V&lt;10

Mapped Finding Item: MH.ZUNG

MH Scale: 1 Condition: I V&lt;33

End: VA-DEPRESSION SCREEN NEGATIVE

---- Begin: VA-DEPRESSION SCREEN POSITIVE	(FI(5)=RT(81)) ----------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.DEP SCREEN 2 QUESTION POS Health Factor Category: MENTAL HEALTH

Mapped Finding Item: MH.DOM80

Condition: I V=1

Mapped Finding Item: MH.DOMG

Condition: I V&gt;3

Mapped Finding Item: MH.CRS

MH Scale: 1 Condition: I V&gt;9

Mapped Finding Item: MH.BDI

MH Scale: 1 Condition: I V&gt;9

Mapped Finding Item: MH.ZUNG

MH Scale: 1 Condition: I V&gt;32

End: VA-DEPRESSION SCREEN POSITIVE

---- Begin: VA-ALCOHOL USE SCREEN	(FI(6)=RT(488)) -----------------------

Finding Type: REMINDER TERM

Not Found Text: Screening for at risk alcohol use using the AUDIT-C screening tool should be performed yearly for any patient who has consumed alcohol in the past year. No record of prior screening for alcohol use was found in this patient's record.

\\

Mapped Findings:

Mapped Finding Item: MH.AUDC

Mapped Finding Item: MH.CAGE Ending Date/Time: 10/1/03

Mapped Finding Item: HF.NON-DRINKER (NO ALCOHOL FOR &gt;1 YR)

Health Factor Category: ALCOHOL USE

Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

Health Factor Category: ALCOHOL USE

Mapped Finding Item: MH.AUDIT

End: VA-ALCOHOL USE SCREEN

---- Begin: VA-PTSD SCREEN	(FI(7)=RT(568013)) ---------------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN NEGATIVE Health Factor Category: MENTAL HEALTH

Mapped Finding Item: HF.PTSD SCREEN POSITIVE Health Factor Category: MENTAL HEALTH

End: VA-PTSD SCREEN

---- Begin: VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)	(FI(8)=RT(568015)) --

Finding Type: REMINDER TERM

Not Found Text: Screen for unexplained fevers that might

represent occult malaria or infection with leishmaniasis.

\\

Mapped Findings:

Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN NEGATIVE

Health Factor Category: IRAQ/AFGHANISTAN

Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN POSITIVE

Health Factor Category: IRAQ/AFGHANISTAN

---- End: VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) ------------------------

---- Begin: VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN)	(FI(9)=RT(568017)) -----

Finding Type: REMINDER TERM

Not Found Text: Screen for symptoms of fatigue, headaches, muscle or joint pains, or forgetfulness that have lasted 3 months or longer and have interfered with daily activities.

\\

NEGATIVE

Mapped Findings:

Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

Health Factor Category: IRAQ/AFGHANISTAN

POSITIVE

Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

Health Factor Category: IRAQ/AFGHANISTAN

---- End: VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN) ---------------------------

---- Begin: VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)	(FI(10)=RT(568014)) -------

Finding Type: REMINDER TERM

Not Found Text: Screen for diarrhea or other GI complaints that might suggest giardia, amoebiasis or other GI infection.

\\

Mapped Findings:

Mapped Finding Item: HF.GI SYMPTOMS SCREEN NEGATIVE Health Factor Category: IRAQ/AFGHANISTAN

Mapped Finding Item: HF.GI SYMPTOMS SCREEN POSITIVE Health Factor Category: IRAQ/AFGHANISTAN

---- End: VA-GI SYMPTOMS (IRAQ/AFGHANISTAN) ------------------------------

---- Begin: VA-PERSISTENT RASH (IRAQ/AFGHANISTAN)	(FI(11)=RT(568016)) ---

Finding Type: REMINDER TERM

Not Found Text: Screen for persistent rash that might

represent infection with leishmaniasis.

\\

Mapped Findings:

Mapped Finding Item: HF.SKIN LESION SCREEN NEGATIVE Health Factor Category: IRAQ/AFGHANISTAN

Mapped Finding Item: HF.SKIN LESION SCREEN POSITIVE Health Factor Category: IRAQ/AFGHANISTAN

---- End: VA-PERSISTENT RASH (IRAQ/AFGHANISTAN) --------------------------

---- Begin: VA-PTSD AVOIDANCE ALL	(FI(12)=RT(617)) ----------------------

Finding Type: REMINDER TERM Within Category Rank: 0

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN - AVOIDANCE Health Factor Category: PTSD AVOIDANCE

Mapped Finding Item: HF.PTSD SCREEN - NO AVOIDANCE Health Factor Category: PTSD AVOIDANCE

End: VA-PTSD AVOIDANCE ALL

---- Begin: VA-PTSD DETACHMENT ALL	(FI(13)=RT(620)) ---------------------

Finding Type: REMINDER TERM Within Category Rank: 0

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN - DETACHED Health Factor Category: PTSD DETACHMENT

Mapped Finding Item: HF.PTSD SCREEN - NO DETACHMENT Health Factor Category: PTSD DETACHMENT

End: VA-PTSD DETACHMENT ALL

---- Begin: VA-PTSD NIGHTMARES ALL	(FI(14)=RT(618)) ---------------------

Finding Type: REMINDER TERM Within Category Rank: 0

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN - NIGHTMARES Health Factor Category: PTSD NIGHTMARES

Mapped Finding Item: HF.PTSD SCREEN - NO NIGHTMARES Health Factor Category: PTSD NIGHTMARES

End: VA-PTSD NIGHTMARES ALL

---- Begin: VA-PTSD ON GUARD ALL	(FI(15)=RT(619)) -----------------------

Finding Type: REMINDER TERM Within Category Rank: 0

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN - ON GUARD Health Factor Category: PTSD ON GUARD

Mapped Finding Item: HF.PTSD SCREEN - NO ON GUARD Health Factor Category: PTSD ON GUARD

End: VA-PTSD ON GUARD ALL

---- Begin: VA-REFUSED PTSD SCREEN	(FI(16)=RT(631)) ---------------------

Finding Type: REMINDER TERM Beginning Date/Time: T-6M

Found Text: Refused PTSD Screen

Mapped Findings:

Mapped Finding Item: HF.REFUSED PTSD SCREEN Health Factor Category: MENTAL HEALTH

End: VA-REFUSED PTSD SCREEN

---- Begin: VA-REFUSED ALCOHOL SCREENING	(FI(17)=RT(568018)) ------------

Finding Type: REMINDER TERM

Beginning Date/Time: T-6M

Found Text: Refused Alcohol Screening

Mapped Findings:

Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

Health Factor Category: ALCOHOL USE

End: VA-REFUSED ALCOHOL SCREENING

---- Begin: VA-REFUSED DEPRESSION SCREENING	(FI(18)=RT(73)) -------------

Finding Type: REMINDER TERM Beginning Date/Time: T-6M

Found Text: Refused Depression Screening

Mapped Findings:

Mapped Finding Item: HF.REFUSED DEPRESSION SCREENING

Health Factor Category: MENTAL HEALTH

---- End: VA-REFUSED DEPRESSION SCREENING --------------------------------

---- Begin: VA-ACTIVE DUTY	(FI(19)=RT(568019)) --------------------------

Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

Mapped Findings:

Mapped Finding Item: CF.VA-PATIENT TYPE Condition: I V="ACTIVE DUTY"

End: VA-ACTIVE DUTY

---- Begin: VA-REFUSED ID &amp; OTHER SX SCREEN	(FI(20)=RT(568020)) ---------

Finding Type: REMINDER TERM Beginning Date/Time: T-6M

Within Category Rank: 0

Found Text: The patient declined to answer some or all of the infectious disease and other symptom questions.	Please ask these screening questions again if they remain unaddressed.

Mapped Findings:

Mapped Finding Item: HF.REFUSED ID &amp; OTHER SX SCREEN Health Factor Category: IRAQ/AFGHANISTAN

---- End: VA-REFUSED ID &amp; OTHER SX SCREEN --------------------------------

Function Findings:

---- Begin: FF(1)---------------------------------------------------------

Function String: MRD(1)&gt;MRD(2) Expanded Function String:

MRD(VA-IRAQ/AFGHAN SERVICE NO)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Not Found Text: The patient's most recent service separation date is more recent than their last screening

- rescreening is needed after any new period of service.

End: FF(1)

---- Begin: FF(2)---------------------------------------------------------

Function String: MRD(7,12,13,14,15)&gt;MRD(2) Expanded Function String:

MRD(VA-PTSD SCREEN,VA-PTSD AVOIDANCE ALL,VA-PTSD DETACHMENT ALL, VA-PTSD NIGHTMARES ALL,VA-PTSD ON GUARD ALL)&gt;MRD(

VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 1. PTSD Screening completed Not Found Text: 1. PTSD Screen NEEDED

End: FF(2)

---- Begin: FF(3)---------------------------------------------------------

Function String: MRD(4,5)&gt;MRD(2) Expanded Function String:

MRD(VA-DEPRESSION SCREEN NEGATIVE,VA-DEPRESSION SCREEN POSITIVE)&gt;MRD( VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 2. Depression Screening completed Not Found Text: 2. Depression Screening NEEDED

End: FF(3)

---- Begin: FF(4)---------------------------------------------------------

Function String: MRD(6)&gt;MRD(2) Expanded Function String:

MRD(VA-ALCOHOL USE SCREEN)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 3. Alcohol Screening completed Not Found Text: 3. Alcohol Screening NEEDED

End: FF(4)

---- Begin: FF(5)---------------------------------------------------------

Function String: MRD(10,20)&gt;MRD(2) Expanded Function String:

MRD(VA-GI SYMPTOMS (IRAQ/AFGHANISTAN),VA-REFUSED ID &amp; OTHER SX SCREEN)&gt; MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 4A. Screen for GI symptoms completed Not Found Text: 4A. Screen for GI symptoms NEEDED

End: FF(5)

---- Begin: FF(6)---------------------------------------------------------

Function String: MRD(8,20)&gt;MRD(2) Expanded Function String:

MRD(VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN),

VA-REFUSED ID &amp; OTHER SX SCREEN)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 4B. Screen for Fevers completed Not Found Text: 4B. Screen for Fevers NEEDED

End: FF(6)

---- Begin: FF(7)---------------------------------------------------------

Function String: MRD(11,20)&gt;MRD(2) Expanded Function String:

MRD(VA-PERSISTENT RASH (IRAQ/AFGHANISTAN),

VA-REFUSED ID &amp; OTHER SX SCREEN)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 4C. Screen for Skin Rash completed Not Found Text: 4C. Screen for Skin Rash NEEDED

End: FF(7)

---- Begin: FF(8)---------------------------------------------------------

Function String: MRD(9,20)&gt;MRD(2)

Expanded Function String:

MRD(VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN),

VA-REFUSED ID &amp; OTHER SX SCREEN)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Found Text: 4D. Screen for Other Symptoms completed Not Found Text: 4D. Screen for Other Symptoms NEEDED

End: FF(8)

---- Begin: FF(9)---------------------------------------------------------

Function String: MRD(2)&gt;MRD(1,3) Expanded Function String:

MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)&gt;MRD(VA-IRAQ/AFGHAN SERVICE NO, VA-IRAQ/AFGHAN SERVICE)

Found Text: The patient's most recent service separation date is more recent than their last screening

- rescreening is needed after any new period of service.

End: FF(9)

General Patient Cohort Found Text:

Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service.	Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&amp;(AGE)&amp;FI(2)!FI(19)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)&amp;FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY)

Customized RESOLUTION LOGIC defines findings that resolve the Reminder: (FI(1)&amp;FF(1))!(FI(3)&amp;(FF(2)!FI(16))&amp;(FF(3)!FI(18))&amp;(FF(4)!FI(17))&amp;FF(5)&amp; FF(6)&amp;FF(7)&amp;FF(8))

Expanded Resolution Logic:

(FI(VA-IRAQ/AFGHAN SERVICE NO)&amp;FF(1))!(FI(VA-IRAQ/AFGHAN SERVICE)&amp; (FF(2)!FI(VA-REFUSED PTSD SCREEN))&amp;(FF(3)!

FI(VA-REFUSED DEPRESSION SCREENING))&amp;(FF(4)!

FI(VA-REFUSED ALCOHOL SCREENING))&amp;FF(5)&amp;FF(6)&amp;FF(7)&amp;FF(8))

Web Sites:

Web Site URL: [http://www.oqp.med.va.gov/cpg/cpg.htm](http://www.oqp.med.va.gov/cpg/cpg.htm)

Web Site Title:	VA/DOD Guidelines - Office of Quality and Performance

Web Site URL: [http://www.oqp.med.va.gov/cpg/MDD/MDD\_Base.htm](http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm)

Web Site Title:	VA/DOD Depression Guideline

Web Site URL: [http://www.oqp.med.va.gov/cpg/cpgn/mus/mus\_base.htm](http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm)

Web Site Title:	VA/DOD Medically Unexplained Symptoms: Pain and Fatigue

Web Site URL: [http://www.oqp.med.va.gov/cpg/PDH/PDH\_base.htm](http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm)

Web Site Title:	Post Deployment Health Evaluation and Management

Web Site URL: [http://www.oqp.med.va.gov/cpg/SUD/SUD\_Base.htm](http://www.oqp.med.va.gov/cpg/SUD/SUD_Base.htm)

Web Site Title:	VA/DOD Substance Abuse Guideline

Web Site URL: [http://vaww.va.gov/environagents/](http://vaww.va.gov/environagents/)

Web Site Title:	VA Environmental Agents Service

#### Reminder Dialog Screens

1. If the first question is answered “yes,” then the rest of the dialog opens up. If the first question is answered “no,” then the user is done.

<!-- image -->

1. When the dialog opens for a ‘yes’ answer, the first question prompts for the location of service. OIF options are on the first screen below and OEF options are on the next screen.

<!-- image -->

<!-- image -->

1. If the first question has already been answered “yes,” then it does not need to be answered again if subsequent users open the dialog to complete other sections. Note the radio button in front of the PTSD screen. This is necessary to allow the user to choose between doing the screen and entering a refusal (next slide).

<!-- image -->

The refusal options for PTSD, depression and alcohol are now present and consistent. The alcohol section is closed because it has been completed in the past six months.

<!-- image -->

1. Note that questions 4B and 4D are “closed” – they have been completed in the past six months. The refusal option is available for this section.

Entering a refusal option for any one of the sections will satisfy that section for one month. However, it will not cause that section of the dialog to be “closed” – the section will remain open but the reminder would no longer be due if all four refusal options are chosen.

<!-- image -->

1. The hyperlinks have been moved to the bottom of the dialog display.

<!-- image -->

1. If a user would like to re-enter data on a closed section, they would click on the checkbox for that section – PTSD in this example

<!-- image -->

After choosing the closed PTSD section, it opens to allow completion.

<!-- image -->

This is what the dialog would look like if a user did PTSD screening, Alcohol screening and depression screening and then clicked on FINISH – and THEN opened the OEF/OIF reminder dialog

– those sections would be closed.

<!-- image -->

Clicking on clinical maintenance shows which sections are needed. The display here is based on the completion of each section AFTER the service separation date. If the dates of all seven pieces listed above 1-3, 4A-D are later than the last service separation date, then the reminder is resolved.

<!-- image -->

## Index

Add Reminders to CPRS Cover Sheet, 24 Editing Dialogs, 18

Mapping, 11, 15, 16

Overview, 2

packed reminders, 6

POST^PXRMWHP, 6

Reminder Term Management, 11, 15, 16

Reminder Test, 17

terms, 7

Testing Reminders, 23

VA FileMan Print from the Reminder Term File, 7