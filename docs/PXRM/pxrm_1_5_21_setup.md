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
source_file: pxrm_1_5_21_setup.docx
status: draft
title: pxrm 1 5 21 setup.docx
---

<!-- image -->

## Iraq &amp; Afghan Post-Deployment Screen Reminder

#### PXRM*1.5*21

**SETUP GUIDE**

#### January 2004 Updated: 12/04


**V** *IST* **A** HSD&amp;D

1. Iraq &amp; Afghan Post-Deployment Screen Reminder Setup Guide	12/16/2004

Contents

INTRODUCTION	1

Impact on Sites	3

Potential Issues	5

Use of Questionnaire	5

SETUP AND MAINTENANCE	6

1. Verify correct installation of the reminders definition, terms, and dialog.	7
2. Map local findings to the national Reminder Terms.	9
3. Run the Reminder Test option after term definition mapping is completed.	13
4. Use the Reminder Dialog options to edit the national (exported) dialog.	13
5. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude health factors from the electronic encounter forms.	16
6. Verify that the reminder functions properly.	17
7. Add the nationally distributed reminders to the CPRS Cover Sheet	18
8. Verify that the dialog functions properly	19

Q &amp; A – Helpful Hints	22

APPENDICES	24

Appendix A: Reminder Definition.	25

Appendix B: Reminder Dialog	31

Appendix C: Reminder Terms	37

Appendix D: Health Factors	43

1. Iraq &amp; Afghan Post-Deployment Screen Reminders Setup Guide	12/16/2004

### Introduction

##### Purpose of Project

Distribute a new Clinical Reminder, *Iraq &amp; Afghan Post-Deployment Screen,* which identifies veterans of Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom *,* and tracks and documents when care has been delivered.

##### Background

Shortly after September 11, 2001, military personnel began deploying to Southwest Asia to liberate Afghanistan. In late 2002, additional military personnel were deployed to this region to liberate Iraq. Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom produced a new generation of war veterans, who are at increased risk of both medical and psychological illnesses due to complex deployment-related exposures. It is therefore important to screen these war veterans for unique health risks.

Because VA is in the forefront of electronic medical record keeping, computer-driven “clinical reminders” are an ideal approach to provide targeted health care to the veterans of recent conflicts in Southwest Asia. Clinical reminders are clinical decision support tools that assist healthcare providers in complying with recommended care. VA’s Computerized Patient Record System (CPRS) supports automated clinical reminders that assist clinical decision-making and instruct providers about appropriate care by providing links to educational materials. Electronic clinical reminders additionally improve documentation and follow-up by allowing providers to easily view when certain tests or evaluations were performed, as well as track and document when care has been delivered.

There are a number of benefits to creating nationally mandated clinical reminders. National reminders help standardize health care and ensure that experts have had input into how clinical care is delivered. Furthermore, national reminders facilitate system-wide assessment of performance and quality of care, because of reporting mechanisms built into the CPRS clinical reminder system.

A newly developed national clinical reminder – *Iraq &amp; Afghan Post-Deployment Screen* – is designed to aid VA health care providers who are evaluating veterans of the recent conflicts in Southwest Asia. This clinical reminder will help to provide new combat veterans with ongoing, high quality health care in an environment structured to their unique needs and status. Although Iraqi Freedom veterans are eligible for the Gulf War Registry, clinical registries only assess veterans on the one occasion when they volunteer for a special examination. A much better approach is to assure that all members of a unique group of veterans receive specialized care from the time they first present to a VA health care facility.

##### Guidance

1. Identifying Veterans for the Afghanistan and Iraq Clinical Reminder

Reminders are designed to apply to a given population and appear on a patient’s CPRS screen, based on patient criteria found in a definable data field within CPRS VistA. Once the Afghanistan and Iraq clinical reminder software patch is installed and the reminder is activated at a local facility, it will appear on the CPRS cover sheet for veterans presenting to a VA health care facility who served in the U.S. military after September 11, 2001.

Identified veterans will then be asked specifically whether they served on the ground, nearby coastal waters, or in the air over Afghanistan and/or Iraq after September 11, 2001, when these deployments began. If the veteran answers yes, the rest of the reminder dialog will appear on the computer screen for completion by the health care provider.

1. Preventing duplication

Because of increasingly widespread use of electronic clinical reminders across VA, there is concern that continued implementation of new reminders will cause undue burden to health care providers. To prevent duplication and unnecessary work, a health factor will be available that allows this Afghanistan and Iraq clinical reminder to be completed just once in the lifetime of a veteran. Importantly, the *Iraq &amp; Afghan Post-Deployment Screen* will satisfy current clinical reminders for depression, alcohol abuse, and PTSD until the scheduled interval lapses for re-administration of these reminders. Consequently, veterans will not be asked the same questions again soon after the completion of this clinical reminder.

1. Resolving the *Iraq &amp; Afghan Post-Deployment Screen*

1. Once a reminder is generated, it needs to be resolved or it will remain active. Reminders designate specific tasks or evaluations that need to be done or specific information that needs to be provided, and designate what information, evaluation, or test results will turn off the reminder. Consequently, the reminder may trigger the ordering of additional tests. Alternately, information provided as a result of the reminder may be sufficient to resolve it. This is the case for the Iraq and Afghanistan clinical reminder, which only involves specific screening questions. However, positive responses to these questions should direct the health care provider to perform a more extensive clinical evaluation or, in some cases, to order additional diagnostic tests.

1. For the Iraq and Afghanistan clinical reminder, all questions in the reminder will have to be answered before it is resolved. The questions in this reminder address long-term medical and psychological health risks among veterans of recent conflicts in Afghanistan and Iraq. Reminders are programmed so that when they are resolved, specific information from the reminder is automatically downloaded into a progress note.

##### Patch 21 (PXRM*1.5*21)

PXRM*1.5*21 releases one new NATIONAL reminder, dialog, and computed finding required for the Iraq &amp; Afghan project. They will be placed in the REMINDER EXCHANGE file (#811.8).

**Installation of the patch will employ the** Reminder Exchange **functionality to automatically** install these reminders/dialog and their components.

Reminder Exchange will automatically overwrite any identical components. Documentation for related guidelines can be found at:

| **Guideline**                                           | **Address**                                         |
|---------------------------------------------------------|-----------------------------------------------------|
| VA/DOD Guidelines - Office of Quality and Performance   | http://www.oqp.med.va.gov/cpg/cpg.htm               |
| VA/DOD Depression Guideline                             | http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm      |
| VA/DOD Medically Unexplained Symptoms: Pain and Fatigue | http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm |
| Post Deployment Health Evaluation and  Management       | http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm      |
| VA/DOD Substance Abuse Guideline                        | http://www.oqp.med.va.gov/cpg/SUD/SUD_Base.htm      |
| VA Environmental Agents Service                         | http://vaww.va.gov/environagents/                   |

##### Impact on Sites

**Setup and implementation by local team**

The following steps may be required after the reminders patch PXRM*1.5*21 has been installed on the system:

1. Clinicians and CPRS/Reminder CACs will need to be informed about the new reminder and dialog.
2. Reminder CACs may need to map certain national Reminder Terms to identify local processing for documenting the Iraq &amp; Afghan Post Deployment screen.

As with all National Reminders, the Iraq &amp; Afghan Post Deployment screen reminder is built with reminder terms instead of individual health factors or other finding types. This allows a site to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that does not have a local finding can use the nationally distributed health factors to collect data.

1. Edit the reminder dialog, if necessary.

After you have mapped the local findings to the national terms, you can continue to use

your local findings as the data elements that are captured ***or*** use the national findings that are already mapped to the national terms.

To use your local findings, edit the reminder dialog by first identifying the elements that allow that data element to be collected, and then changing the finding item for that element to the local finding. Directions are provided later in this manual.

NOTE: The only way national reminders and dialogs can be modified is by changing the finding items in the nationally distributed elements to use your local finding items instead of the nationally distributed ones. You can also copy and rename the national reminder and dialog, as long as terms are correctly mapped to the national ones.

##### NOTE: It isn’t necessary to autogenerate a dialog for this reminder, as the dialog is included in the packed reminder. You only need to activate/link the dialog.

##### Potential Issues

- On initial intake, these patients will have this reminder and any local reminders for Depression, Alcohol, and PTSD screening also due and displayed.
    - Duplication potential.
- AUDIT-C cannot be made mandatory.
    - If a patient refuses to take the AUDIT C, the reminder will remain due.
- Template field text is deleted by the software if additional reminders are processed after the one with the template field. This is a known bug in the software, which we hope will be fixed soon.
    - In the meantime, clinicians should be instructed to click the Finish Button only and not click on Next or Back. Clicking the Next or Back button is where the text in the progress note gets lost. Do not edit the dialog to remove the template fields unless this becomes a major problem.

##### Use of Questionnaire

- Many sites use paper-based questionnaires to collect data from patients.
- This may be more efficient than having the staff sit with the patient and read questions to the patient.
- A sample is posted on the Clinical Reminders web page.
- Data entry issues – data may be entered before the patient sees the provider, and the provider may not be aware of positive responses.

### Setup and Maintenance

After installing the Iraq &amp; Afghan Post Deployment screen reminder, follow the steps beginning on the next page to implement the reminder and dialog for this project.

##### Reminder Summary

**COHORT:** Veterans with separation date after 9/11/01. This finding is part of the reminder term: IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

**RESOLUTION:** Entry of a health factor for NO IRAQ/AFGHAN SERVICE, which is found in the reminder term IRAQ/AFGHAN SERVICE NO, will resolve the reminder. If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE), then all the other items are required to resolve the reminder:

1. Screen for PTSD,
2. Screen for depression,
3. Screen for alcohol use,
4. All 4 screening questions related to infectious diseases and other symptoms.

An entry of IRAQ/AFGHAN SERVICE on the reminder dialog then requires all of the screening questions to be answered.

All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2-question depression screen are used for the depression screening.

The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year, and the health factor for refusal.

Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder term (PTSD SCREEN) that is exported with this reminder.

The Health Factors for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.

**Setup Steps**

##### 1 Verify correct installation of the reminders definition, terms, and dialog.

1. Using *Inquire about Reminder Definition* on the Reminder Management Menu, ensures that the Iraq &amp; Afghan Post Deployment Screen reminder definition has been installed. Review the reminder. (Reviewing the reminder definition will help you understand how it uses reminder terms.) *Do not make any changes to these reminders.* If necessary for local usage, you may copy the national reminder and create a local reminder; then make any desired changes to the local copy.

Select Reminder Definition Management Option: **RI** Inquire about Reminder Definition

Select Reminder Definition: VA- **Iraq &amp; Afghan Post Deployment screen**

*(reminder definition displayed)*

List Reminder Definitions

Inquire about Reminder Definition Add/Edit Reminder Definition

Copy Reminder Definition Activate/Inactivate Reminders

RL RI RE RC RA

Select Reminder Managers Menu Option: **RM** Reminder Definition Management

1. Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:
2. DEPRESSION SCREEN NEGATIVE
3. DEPRESSION SCREEN POSITIVE
4. GI SYMPTOMS (IRAQ/AFGHANISTAN)
5. IRAQ/AFGHAN PERIOD OF SERVICE
6. IRAQ/AFGHAN SERVICE
7. IRAQ/AFGHAN SERVICE NO
8. OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
9. PERSISTENT RASH (IRAQ/AFGHANISTAN)
10. PTSD SCREEN
11. UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

- ALCOHOL USE SCREEN

Select Reminder Managers Menu Option: **TRM** Reminder Term Management TL	List Reminder Terms

TI	Inquire about Reminder Term TE	Reminder Term Edit

TC	Copy Reminder Term

Select Reminder Term Management Option: **TI** Inquire about Reminder Term Select Reminder Term: **Alcohol Use Screen**

##### VA FileMan Print from the Reminder Term File

You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

##### Example

1. Verify that the reminder dialog is installed on your system. Use CV, Change View, to see dialogs.

| Select Reminder Dialog Management Option:  **DI**  Reminder Dialogs  **Dialog List**  Dec 04, 2003@09:51:20	Page:	12 of	13 REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog Status  14	BLOOD PRESSURE CHECK	COPY OF BLOOD PRESSURE CHEC	Disabled  16	CFTEST	CFTEST	Disabled   |    |      |                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|------|------------------|
| **+	Enter ?? for more actions**                                                                                                                                                                                                                                                                                        |    |      | **&gt;&gt;&gt;** |
| AR	All reminders	LR	Linked Reminders CV	Change View	RN	Name/Print Name Select Item: Next Screen//  **CV**  **Search for: Iraq**  ...searching for 'Iraq'.                                                                                                                                                              | QU | Quit |                  |

| **Dialog List**  Dec 04, 2003@09:51:20	Page:	12 of	13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  +Item Reminder Dialog Name	Source Reminder	Status  1. VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked 2. VA-MST SCREENING	*NONE*	Linked 3. VA-PNEUMOVAX	VA-PNEUMOVAX	Linked 4. VA-PPD	VA-PPD	Disabled 5. VA-PSA	VA-PSA	Disabled 6. VA-SEATBELT EDUCATION	VA-SEATBELT EDUCATION	Disabled 7. VA-WH MAMMOGRAM REVIEW RESULTS	VA-WH MAMMOGRAM REVIEW RE Linked 8. VA-WH MAMMOGRAM SCREENING	VA-WH MAMMOGRAM SCREENING Linked 9. VA-WH PAP SMEAR REVIEW RESULTS	VA-WH PAP SMEAR REVIEW RE Linked 10. VA-WH PAP SMEAR SCREENING	VA-WH PAP SMEAR SCREENING Linked   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Find Next 'Iraq'? Yes// n	NO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**NOTE** : Do not autogenerate dialogs for the reminder. A Dialog is included with the packed reminder installation.

##### 2 Map local findings to the national Reminder Terms.

*Option: Reminder Term Management* on the *Reminder Management Menu.*

Before using the reminder, map the local findings your site uses to represent the national reminder terms, if necessary.

- Prepare a list of your local findings – health factors, taxonomies, etc. that you use to represent terms.
- Review the national term definitions (see Appendix C or use the options on the Reminder Term Management menu), to compare these to what you are using locally to represent terms.

**Purpose of National Terms**

- Terms are used to define a general concept that can be used on a national level
- Terms allow sites the ability to link existing local or VISN findings to the national term.

##### Term Mapping

These are the only terms that are included in the reminders and all of the exported health factors and education topics fall into one of these terms.

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

If desired, add local Health Factors or education topics representing these terms.

| **Term**                       | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALCOHOL USE SCREEN             | Add: Any local health factors for AUDT-C, refusal of alcohol screening, or no alcohol in the past year.  The Mental Health tests for AUDIT-C and CAGE are already included in this term. If your site uses the 10 question AUDIT, then this should also be added to this term.                                                                                                                                                                                                                                                  |
| DEPRESSION SCREEN NEGATIVE     | Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for negative depression screening should have already been mapped to this term when the national MH reminders were installed.  Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term. |
| DEPRESSION SCREEN POSITIVE     | Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for positive depression screening should have already been mapped to this term when the national MH reminders were installed.  Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term. |
| GI SYMPTOMS (IRAQ/AFGHANISTAN) | This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this  term.                                                                                                                  |

| **Term**                             | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IRAQ/AFGHAN PERIOD OF SERVICE        | This term contains a computed finding that determines if the patient’s most recent service separation date was after 9/11/01. The computed finding is included to define the cohort of patients who need to be asked about service in the combat arena.                                                                                                                                                                             |
| IRAQ/AFGHAN SERVICE                  | This term contains the health factor that is entered from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at  sea).                                                                                                                                                                                                                                                                 |
| IRAQ/AFGHAN SERVICE NO               | This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air or at sea).  This health factor resolves the reminder.                                                                                                                                                                                                                             |
| OTHER SYMPTOMS (IRAQ/AFGHANISTAN)    | This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered.  Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.         |
| PERSISTENT RASH (IRAQ/AFGHANISTAN)   | This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or  items should be added to this term. |
| PTSD SCREEN                          | If your site does PTSD screening, map any local health factors or exams that represent positive or  negative screens for PTSD                                                                                                                                                                                                                                                                                                       |
| UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) | This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional  health factors or items should be added to this term.                |

NOTE: It isn’t necessary to enter an Effective Period when mapping terms, as this is already in the reminder definition. **Entry of an Effective Period on a Reminder Term will override the Effective Period defined on the Reminder Definition.**

##### Example: Mapping a Local Health Factor Finding to the National Reminder Term

Enter local health factors or exams that your site uses to represent positive or negative screens for PTSD.

...OK? Yes//	(Yes)

Select FINDING ITEM: PTSD SCREEN POSITIVE//

FINDING ITEM: (your health factor is displayed) EFFECTIVE PERIOD:

USE INACTIVE PROBLEMS: WITHIN CATEGORY RANK: EFFECTIVE DATE:

MH SCALE: CONDITION:

CONDITION CASE SENSITIVE: RX TYPE:

Select FINDING ITEM:

NATIONAL

Select Reminder Term: **PTSD SCREEN**

Select Reminder Term Management Option: **te** Reminder Term Edit

1. **Run the Reminder Test option after term definition mapping is completed. Review the results of patient data with each of the findings mapped to the term.** *Option: Reminders Test* on the *Reminder Managers Menu*

Select Reminder Managers Menu Option: **RT** Reminder Test

Select Patient: **CRPATIENT,ONE** 4-30-44	666680999	YES	EMPLOYEE

Enrollment Priority: GROUP 5	Category: IN PROCESS	End Date:

Select Reminder: **Iraq &amp; Afghan Post Deployment Screen**

**NOTE: See the Clinical Reminders Manager Manual for descriptions of the different elements of the test output.**

##### 3 Use the Reminder Dialog options to edit the national (exported) dialog.

Once you have mapped the local findings to the national terms, you can then decide if you want to continue to use your local findings as the data elements that are captured, or if you want to use the national findings that are already mapped to the national terms.

If you want to continue to use your local findings, then be sure to edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding. The national reminders and dialogs can ***only*** be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

##### Steps to add or edit dialog elements:

1. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):

Select Reminder Managers Menu Option: **DM** Reminder Dialog Management

DP	Dialog Parameters ... DI	Reminder Dialogs

Select Reminder Dialog Management Option: **DI** Reminder Dialogs

| **Dialog List	Nov 20, 2003@08:40:01	Page:**  REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog  1. 757 NUR ALCOHOL USE SCREEN	757 ALCOHOL USE SCREEN 2. 757 NUR SEATBELT &amp; ACCIDENT AVOID	757 SEATBELT AND ACCIDENT A 3. A A BLOOD EXPOSURE 4. A A PAIN VITAL SIGN	VA-PAIN SCREEN AND HX   |    |      | **1 of**  Status   | **21**   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|------|--------------------|----------|
| **+	Enter ?? for more actions**                                                                                                                                                                                                                                                                                                        |    |      | **&gt;&gt;&gt;**   |          |
| AR	All reminders	LR	Linked Reminders CV	Change View	RN	Name/Print Name  Select Item: Next Screen//                                                                                                                                                                                                                                     | QU | Quit |                    |          |

1. Change the view (CV) to Reminder Dialogs.

| Select Item: Next Screen// cv                                                                                                                                  | Select Item: Next Screen// cv                                          | Select Item: Next Screen// cv                                          | Select Item: Next Screen// cv                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Select one of the following:                                                                                                                                   | Select one of the following:                                           | Select one of the following:                                           | Select one of the following:                                           |
| D	Reminder Dialogs                                                                                                                                             | D	Reminder Dialogs                                                     | D	Reminder Dialogs                                                     | D	Reminder Dialogs                                                     |
| E	Dialog Elements                                                                                                                                              | E	Dialog Elements                                                      | E	Dialog Elements                                                      | E	Dialog Elements                                                      |
| F	Forced Values                                                                                                                                                | F	Forced Values                                                        | F	Forced Values                                                        | F	Forced Values                                                        |
| G	Dialog Groups                                                                                                                                                | G	Dialog Groups                                                        | G	Dialog Groups                                                        | G	Dialog Groups                                                        |
| P	Additional Prompts                                                                                                                                           | P	Additional Prompts                                                   | P	Additional Prompts                                                   | P	Additional Prompts                                                   |
| R	Reminders                                                                                                                                                    | R	Reminders                                                            | R	Reminders                                                            | R	Reminders                                                            |
| RG	Result Group (Mental Health)                                                                                                                                | RG	Result Group (Mental Health)                                        | RG	Result Group (Mental Health)                                        | RG	Result Group (Mental Health)                                        |
| RE	Result Element (Mental Health)                                                                                                                              | RE	Result Element (Mental Health)                                      | RE	Result Element (Mental Health)                                      | RE	Result Element (Mental Health)                                      |
| TYPE OF VIEW: R// d	Reminder Dialogs                                                                                                                           | TYPE OF VIEW: R// d	Reminder Dialogs                                   | TYPE OF VIEW: R// d	Reminder Dialogs                                   | TYPE OF VIEW: R// d	Reminder Dialogs                                   |
| **Dialog List**  Dec 04, 2003@09:51:20	Page:	12 of	13                                                                                                          |                                                                        |                                                                        |                                                                        |
| DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)                                                                                                          |                                                                        |                                                                        |                                                                        |
| Item Reminder Dialog Name	Source Reminder	Status                                                                                                               | Item Reminder Dialog Name	Source Reminder	Status                       | Item Reminder Dialog Name	Source Reminder	Status                       | Item Reminder Dialog Name	Source Reminder	Status                       |
| 1	571B	SMOKING CESSATION EDUCATI                                                                                                                               | 1	571B	SMOKING CESSATION EDUCATI                                       | 1	571B	SMOKING CESSATION EDUCATI                                       | 1	571B	SMOKING CESSATION EDUCATI                                       |
| 2	571a	SMOKING CESSATION EDUCATI                                                                                                                               | 2	571a	SMOKING CESSATION EDUCATI                                       | 2	571a	SMOKING CESSATION EDUCATI                                       | 2	571a	SMOKING CESSATION EDUCATI                                       |
| 3	757 ALCOHOL USE SCREEN	757 NUR ALCOHOL USE SCREE Linked                                                                                                      | 3	757 ALCOHOL USE SCREEN	757 NUR ALCOHOL USE SCREE Linked              | 3	757 ALCOHOL USE SCREEN	757 NUR ALCOHOL USE SCREE Linked              | 3	757 ALCOHOL USE SCREEN	757 NUR ALCOHOL USE SCREE Linked              |
| 4	757 SEATBELT AND ACCIDENT AVOIDANCE	757 NUR SEATBELT & ACCIDE Linked                                                                                         | 4	757 SEATBELT AND ACCIDENT AVOIDANCE	757 NUR SEATBELT & ACCIDE Linked | 4	757 SEATBELT AND ACCIDENT AVOIDANCE	757 NUR SEATBELT & ACCIDE Linked | 4	757 SEATBELT AND ACCIDENT AVOIDANCE	757 NUR SEATBELT & ACCIDE Linked |
| 5	A A PAIN SCREEN AND INTERVENTION	*NONE*                                                                                                                      | 5	A A PAIN SCREEN AND INTERVENTION	*NONE*                              | 5	A A PAIN SCREEN AND INTERVENTION	*NONE*                              | 5	A A PAIN SCREEN AND INTERVENTION	*NONE*                              |
| 6	A A SG PAIN HISTORY DIA	ZZPJH REMINDER                                                                                                                       | 6	A A SG PAIN HISTORY DIA	ZZPJH REMINDER                               | 6	A A SG PAIN HISTORY DIA	ZZPJH REMINDER                               | 6	A A SG PAIN HISTORY DIA	ZZPJH REMINDER                               |
| **+	Enter ?? for more actions**                                                                                                                                |                                                                        |                                                                        | **&gt;&gt;&gt;**                                                       |
| AD	Add Reminder Dialog	PT	List/Print All CV	Change View	RN	Name/Print Name  **Select Item: Next Screen// SL**  Search for:  **Iraq**  ...searching for ‘Iraq’. | QU                                                                     | Quit                                                                   |                                                                        |

1. Enter SL for Search List, to jump to the Iraq dialog. Select the dialog number to see details.

| **Dialog List**  Dec 04, 2003@09:51:20	Page:	12 of	13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  +Item Reminder Dialog Name	Source Reminder	Status  1. VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked 2. VA-MST SCREENING	*NONE*	Linked 3. VA-PNEUMOVAX	VA-PNEUMOVAX	Linked 4. VA-PPD	VA-PPD	Disabled 5. VA-PSA	VA-PSA	Disabled 6. VA-SEATBELT EDUCATION	VA-SEATBELT EDUCATION	Disabled 7. VA-WH MAMMOGRAM REVIEW RESULTS	VA-WH MAMMOGRAM REVIEW RE Linked 8. VA-WH MAMMOGRAM SCREENING	VA-WH MAMMOGRAM SCREENING Linked 9. VA-WH PAP SMEAR REVIEW RESULTS	VA-WH PAP SMEAR REVIEW RE Linked 10. VA-WH PAP SMEAR SCREENING	VA-WH PAP SMEAR SCREENING Linked   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Find Next 'Iraq'? Yes//  **n**  NO Select Item: Next Screen  **// 179**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| **Dialog Edit List**  Dec 16, 2003@10:01:04	Page:	1 of	5  REMINDER DIALOG NAME: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN [NATIONAL] *L  Item	Seq.	Dialog Details/Findings	Type  1. 5	TEXT OIF INTRO AND WEB	element Finding: *NONE*  1. 20	GP OIF COMBAT SERVICE YES/NO	group Finding: *NONE* 2. 20.5	GP OIF COMBAT SERVICE NO	group Finding: NO IRAQ/AFGHAN SERVICE (HEALTH FACTOR) 3. 20.10 GP OIF COMBAT SERVICE YES	group Finding: IRAQ/AFGHAN SERVICE (HEALTH FACTOR) 4. 20.10.25 GP OIF PTSD	group  Finding: *NONE*  1. 20.10.25.15 GP OIF PTSD QUESTIONS	group Finding: *NONE* 2. 20.10.25.15.5 TEXT OIF PTSD QUESTIONS	element Finding: *NONE* 3. 20.10.25.15.10 GP OIF PTSD SCREEN RESULTS	group   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CO	Copy Dialog	DT	Dialog Text	RI	Reminder Inquiry DD	Detailed Display	ED	Edit/Delete Dialog	QU	Quit  DP	Progress Note Text	INQ	Inquiry/Print Select Sequence: Next Screen//  **&lt;Enter&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

1. Make edits, as needed, by entering the dialog element number.

| **Dialog Edit List**  Dec 16, 2003@10:01:04	Page: REMINDER DIALOG NAME: IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN  +Item	Seq.	Dialog Summary  1. 20.10.25.15.10.5	Element: VA-HF OIF PTSD NEGATIVE  1. 20.10.25.15.10.10	Element: VA-HF OIF PTSD POSITIVE  1. 20.10.35	Group: VA-GP OIF DEPRESSION SCREEN  1. 20.10.35.10	Group: VA-GP DEP SCREEN PRIME MD  1. 20.10.35.10.5	Element: VA-HF DEP 2 QUESTION NEG  1. 20.10.35.10.10	Element: VA-HF DEP 2 QUESTION POS  1. 20.10.45	Group: VA-GP OIF ALCOHOL SCREEN   |                                                            |                                                            |                                                            | 2                                                          | of                                                         | 5                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **+**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **+ Next Screen**                                          | **- Prev Screen**                                          | **?? More Actions**                                        | **&gt;&gt;&gt;**                                           |                                                            |                                                            |
| ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  | ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print  |
| CO	Copy Dialog	DO	Dialog Overview	QU	Quit                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  | CO	Copy Dialog	DO	Dialog Overview	QU	Quit                  |
| DD	Detailed Display	DT	Dialog Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         | DD	Detailed Display	DT	Dialog Text                         |
| DP	Progress Note Text	ED	Edit/Delete Dialog                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                | DP	Progress Note Text	ED	Edit/Delete Dialog                |
| Select Item: Next Screen//  **9**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                            |                                                            |                                                            |                                                            |                                                            |                                                            |
| Select one of the following:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Select one of the following:                               | Select one of the following:                               | Select one of the following:                               | Select one of the following:                               | Select one of the following:                               | Select one of the following:                               |
| E	Edit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | E	Edit                                                     | E	Edit                                                     | E	Edit                                                     | E	Edit                                                     | E	Edit                                                     | E	Edit                                                     |
| C	Copy and Replace current element                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | C	Copy and Replace current element                         | C	Copy and Replace current element                         | C	Copy and Replace current element                         | C	Copy and Replace current element                         | C	Copy and Replace current element                         | C	Copy and Replace current element                         |
| D	Delete element from this dialog                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | D	Delete element from this dialog                          | D	Delete element from this dialog                          | D	Delete element from this dialog                          | D	Delete element from this dialog                          | D	Delete element from this dialog                          | D	Delete element from this dialog                          |
| Select Dialog Element Action: E//  **&lt;Enter&gt;**  dit                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                            |                                                            |                                                            |                                                            |                                                            |                                                            |
| Dialog Element Type: E//  **&lt;Enter&gt;**  lement                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                            |                                                            |                                                            |                                                            |                                                            |                                                            |
| Current dialog element/group name: VA-HF OIF PTSD NEGATIVE                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE | Current dialog element/group name: VA-HF OIF PTSD NEGATIVE |
| Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      | Used by:	VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)      |

FINDING ITEM: PTSD SCREEN NEGATIVE// ZZPTSD

Searching for a EDUCATION TOPICS Searching for a IMMUNIZATION Searching for a SKIN TEST Searching for a EXAM

Searching for a HEALTH FACTOR ZZPTSD SCREEN NEGATIVE

...OK? Yes// &lt;Enter&gt;	(Yes) Select ADDITIONAL FINDINGS:

Input your edit comments.

Edit? NO// &lt;Enter&gt;

##### 4 Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude health factors from the electronic encounter forms.

Enter the Health Factors for all of the screens in the site parameters as ones that cannot be added outside of a reminder dialog. Entry of these health factors should ONLY occur during reminder dialog use.

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

This parameter is on the general parameter tool menu (XPAR), available on the CPRS Configuration (IRM) option.

NOTE: Since this is a Kernel option, some sites assign the menu separately from CPRS, or it may only be available to IRM staff. If you don’t have access to it, check with your IRM office.

List Values for a Selected Parameter List Values for a Selected Entity List Values for a Selected Package List Values for a Selected Template Edit Parameter Values

Edit Parameter Values with Template

LV LE LP LT EP ET

Select CPRS Configuration (IRM) Option: **XX** General Parameter Tools

Enter selection: **5** System	MARTINEZ.MED.VA.GOV

--- Setting ORWPCE EXCLUDE HEALTH FACTORS	for System: SLC.MED.VA.GOV ---

Select Sequence: ?

There are currently no entries for Sequence. Select Sequence: **1**

Are you adding 1 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 1// **&lt;Enter&gt;** 1

Health Factor: **NO IRAQ/AFGHAN SERVICE**

Select Sequence: **2**

Are you adding 2 as a new Sequence? Yes// **&lt;Enter&gt;** YES Sequence: 2// **&lt;Enter&gt;**

Health Factor: **IRAQ**

1. IRAQ/AFGHAN SERVICE
2. IRAQ/AFGHANISTAN

CHOOSE 1-2: **1** IRAQ/AFGHAN SERVICE

[choose from NEW PERSON] [choose from HOSPITAL LOCATION] [choose from SERVICE/SECTION] [choose from INSTITUTION] [MARTINEZ.MED.VA.GOV]

USR LOC SRV DIV SYS

1. User
2. Location
3. Service
4. Division
5. System

Select General Parameter Tools Option: **ep** Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: **ORWPCE EXCLUDE HEALTH FACTORS** Excluded

Health Factors

ORWPCE EXCLUDE HEALTH FACTORS may be set for the following:

##### 5 Verify that the reminder functions properly.

2. Run a Reminders Due Report to determine if the Iraq Clinical Reminder statuses reported are correct.

*Option: Reminders Due* on the *Reminder Reports menu*

This report can be displayed at the beginning of the day for patients being seen that day.

- The reminder can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder.
- Reports can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved.
- Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.

1. Use the Reminder Test option to test the reminders.

*Option: Reminders Test* on the *Reminder Management menu*

1. Use the clinical maintenance view in the CPRS GUI to ensure that the status of the reminder is appropriate.

##### 6 Add the nationally distributed reminders to the CPRS Cover Sheet

2. Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”

1. When the Cover Sheet Reminder List opens, set the Cover sheet parameter level.

1. Locate the Iraq &amp; Afghan Post Deployment Screen reminder and click the Add button (or double-click the reminder).

##### 7 Verify that the dialog functions properly

Test the Iraq &amp; Afghan Post Deployment Screen Reminder dialog in CPRS, using either the exported dialog or your locally created dialog. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.

***Steps to test dialogs:***

1. On the cover sheet, click on the Reminders icon.
2. Click on reminders in the Reminders box to see details of a reminder
3. Open the Notes tab and select New Note. Enter a title.
4. Open the Reminders drawer and review the contents.
5. Locate the Iraq &amp; Afghan Post Deployment Screen reminder dialog and open it.
6. Check all the boxes, in different combinations, to see what happens.

<!-- image -->

1. Perform as many of the following as possible:

- Click on the boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive depression screen.
- Enter a positive alcohol screen.
- Perform the AUDC, checking appropriate boxes.
- Click Finish.
- Verify that all elements are required.
- Click on the Refresh button in the Action menu.
- Verify that entry of the alcohol screen and the depression screen in the Iraq/Afghan reminder dialog also resolves any local reminders for depression screening and alcohol screening.
- Verify that any local reminders for f/u of positive screens for depression or alcohol became due.
- If the national depression screening reminder was not applicable for the patient above, select a new patient who has a status of Due or Applicable for depression screening.
- Open the dialog IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN.

- Check the appropriate boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive depression screen.
- Click Finish.
- Verify that the national depression screening reminder is resolved.
- If the national alcohol screening reminder was not applicable for the patient above, select a new patient who has a status of Due or Applicable for alcohol screening.
- Open the dialog IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN.
- Check the appropriate boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive alcohol screen.
- Click Finish.
- Verify that the national alcohol screening reminder is resolved.
- Repeat any of the steps above to try different dialog entries and to observe the results in the progress note text and reminder statuses.
- Select a new patient with a separation date before 9/11/01.
- Check the Cover Sheet and Clinical Maintenance box to verify that the reminder is not due or applicable.

##### NOTE: Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately.

#### Q &amp; A – Helpful Hints

**Q: What is a National Reminder?**

**A:** National reminders are clinical reminders and reminder dialogs that have gone through an approval process for national distribution. Some national reminders are related to statutory, regulatory, or Central Office mandates such as Hepatitis C, MST, or Pain. Other national reminders are being developed under the guidance of the VA National Clinical Practice Guideline Council (NCPGC).

Guideline-related reminders are being developed for two reasons:

1. To provide reminders for sites that don’t have reminders in place for a specific guideline (e.g., HTN, HIV).
2. To provide a basic set of reminders to all sites to improve clinical care, and also allow roll-up data for measurement of guideline implementation and adherence (e.g., IHD, Mental Health).

##### Q: Can national reminders or dialogs ever be locally modified?

**A:** The only way national reminders and dialogs can be modified is by changing the finding item in the nationally distributed dialog elements to use your local finding item instead of the nationally distributed one. You can copy the national reminder to create a local reminder, but you should map your health factors, education topics, and other findings to the national exported terms.

##### Q: Is the Iraq &amp; Afghan Post Deployment Screen national reminder mandated for use? A: No.

**Q: What should we do if we already have Depression Screening, Alcohol Screening, or PTSD reminders?**

**A:** If you choose to continue using your local reminder and dialog, you need to make sure that your local reminder is consistent with the VA/DOD National Clinical Practice Guideline. You should map your local findings to the national reminder terms in case you want to use the National reminders in the future for display in CPRS or for reporting.

There are currently no plans to use these reminders to roll up data to any national reports on Iraq.

**Q:** This patch contains template fields in the PTSD screen—if providers using this reminder click next or back, they lose the text in the progress note. What do you suggest...should we edit the dialog to remove the template fields?

**A:** This is a long-standing problem with reminders; it is on our list to fix after the release of CRv2.0. In the meantime, clinicians should be instructed to click the Finish Button only and not click on Next or Back. Clicking the Next or Back button is where the text in the progress

note gets lost. Do not edit the dialog to remove the template fields unless this becomes a major problem.

##### Q: How can we check parameters to see if anyone sees the reminders?

**A:** The simplest way to view whether an individual is seeing the reminders is to open the reminder cover sheet editor by clicking on the reminder clock in CPRS, picking Action, and then choosing “Edit Cover Sheet Reminders.” A button on the dialog allows you to view the entire list of reminders that are seen by an individual user.

## Appendices

##### Appendix A: Iraq &amp; Afghan Post Deployment Reminder Definition Appendix B: Iraq &amp; Afghan Post Deployment Reminder Dialog Appendix C: Reminder Term Descriptions

**Appendix D: Reminder Health Factors**

##### Appendix A: Reminder Definition

REMINDER DEFINITION INQUIRY	Dec 19, 2003 12:26:28 pm	Page 1

VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN No.	568022

Print Name:	Iraq&amp;Afghan Post-Deployment Screen

Class:	NATIONAL

Sponsor:

Review Date:

Usage:	CPRS, REPORTS

Related VA-* Reminder:

Reminder Dialog:	VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Priority:

Reminder Description:

Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service.	Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

COHORT: veterans with separation date after 9/11/01.	This finding is part of the reminder term: IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

RESOLUTION: entry of a health factor for NO IRAQ/AFGHAN SERVICE which is found in the reminder term IRAQ/AFGHAN SERVICE NO will resolve the reminder.	If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE) then all the other items are required to resolve the reminder:

1. screen for PTSD,
2. screen for depression,
3. screen for alcohol use,
4. all 4 screening questions related to infectious diseases and other symptoms.

An entry of IRAQ/AFGHAN SERVICE on the reminder dialog then requires all of the screening questions to be answered.

All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2 question depression screen are used for the depression screening.	The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal. Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening.	If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder term (PTSD SCREEN) that is exported with this reminder.

The HFs for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog.	Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms.	Entry of these health factors should ONLY occur during reminder dialog use.

Technical Description:

Baseline Frequency:

Do In Advance Time Frame:	Wait until actually DUE Sex Specific:

Ignore on N/A:

Frequency for Age Range:	99Y - Once for all ages Match Text:

No Match Text:

Findings:

---- Begin: IRAQ/AFGHAN SERVICE NO	(FI(1)=RT(489)) ----------------------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Mapped Findings:

Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE

End: IRAQ/AFGHAN SERVICE NO

---- Begin: IRAQ/AFGHAN PERIOD OF SERVICE	(FI(2)=RT(490)) ---------------

Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

Beginning Date/Time: SEP 11, 2001

Mapped Findings:

Mapped Finding Item: CF.VA-IRAQ &amp; AFGHAN SEP. DATE Beginning Date/Time: SEP 11, 2001

End: IRAQ/AFGHAN PERIOD OF SERVICE

---- Begin: IRAQ/AFGHAN SERVICE	(FI(3)=RT(568012)) ----------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE

End: IRAQ/AFGHAN SERVICE

---- Begin: DEPRESSION SCREEN NEGATIVE	(FI(4)=RT(80)) -------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.DEP SCREEN 2 QUESTION NEG

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

End: DEPRESSION SCREEN NEGATIVE

---- Begin: DEPRESSION SCREEN POSITIVE	(FI(5)=RT(81)) -------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.DEP SCREEN 2 QUESTION POS

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

End: DEPRESSION SCREEN POSITIVE

---- Begin: ALCOHOL USE SCREEN	(FI(6)=RT(488)) --------------------------

Finding Type: REMINDER TERM

Not Found Text: Screening for at risk alcohol use using the AUDIT-C screening tool should be performed yearly for any patient who has consumed alcohol in the past year. No record of prior screening for alcohol use was found in this patient's record.

Mapped Findings:

| Mapped   | Finding   | Item:   | MH.AUDC                               |
|----------|-----------|---------|---------------------------------------|
| Mapped   | Finding   | Item:   | MH.CAGE                               |
| Mapped   | Finding   | Item:   | HF.NON-DRINKER (NO ALCOHOL FOR >1 YR) |
| Mapped   | Finding   | Item:   | HF.REFUSED ALCOHOL USE SCREENING      |
| Mapped   | Finding   | Item:   | MH.AUDIT                              |

End: ALCOHOL USE SCREEN

---- Begin: PTSD SCREEN	(FI(7)=RT(568013)) ------------------------------

Finding Type: REMINDER TERM Not Found Text: Screen for PTSD.

Mapped Findings:

Mapped Finding Item: HF.PTSD SCREEN NEGATIVE

Mapped Finding Item: HF.PTSD SCREEN POSITIVE

End: PTSD SCREEN

---- Begin: UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)	(FI(8)=RT(568015)) -----

Finding Type: REMINDER TERM

Not Found Text: Screen for unexplained fevers that might

represent occult malaria or infection with leishmaniasis.

Mapped Findings:

Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN NEGATIVE

Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN POSITIVE

---- End: UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) ---------------------------

---- Begin: OTHER SYMPTOMS (IRAQ/AFGHANISTAN)	(FI(9)=RT(568017)) --------

Finding Type: REMINDER TERM

Not Found Text: Screen for symptoms of fatigue, headaches, muscle or joint pains, or forgetfulness that have lasted 3 months or longer and have interfered with daily activities.

NEGATIVE

Mapped Findings:

Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

POSITIVE

---- End: OTHER SYMPTOMS (IRAQ/AFGHANISTAN) ------------------------------

---- Begin: GI SYMPTOMS (IRAQ/AFGHANISTAN)	(FI(10)=RT(568014)) ----------

Finding Type: REMINDER TERM

Not Found Text: Screen for diarrhea or other GI complaints that might suggest giardia, amoebiasis or other GI infection.

Mapped Findings:

Mapped Finding Item: HF.GI SYMPTOMS SCREEN NEGATIVE

Mapped Finding Item: HF.GI SYMPTOMS SCREEN POSITIVE

End: GI SYMPTOMS (IRAQ/AFGHANISTAN)

---- Begin: PERSISTENT RASH (IRAQ/AFGHANISTAN)	(FI(11)=RT(568016)) ------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.SKIN LESION SCREEN NEGATIVE Mapped Finding Item: HF.SKIN LESION SCREEN POSITIVE

---- End: PERSISTENT RASH (IRAQ/AFGHANISTAN) -----------------------------

General Patient Cohort Found Text:

Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service.	Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

General Patient Cohort Not Found Text:

General Resolution Found Text:

General Resolution Not Found Text:

Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&amp;(AGE)&amp;FI(2)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)&amp;FI(IRAQ/AFGHAN PERIOD OF SERVICE)

Customized RESOLUTION LOGIC defines findings that resolve the Reminder: FI(1)!((FI(4)!FI(5))&amp;FI(6)&amp;FI(7)&amp;FI(8)&amp;FI(9)&amp;FI(10)&amp;FI(11))

Expanded Resolution Logic:

FI(IRAQ/AFGHAN SERVICE NO)!((FI(DEPRESSION SCREEN NEGATIVE)! FI(DEPRESSION SCREEN POSITIVE))&amp;FI(ALCOHOL USE SCREEN)&amp;FI(PTSD SCREEN)&amp; FI(UNEXPLAINED FEVER (IRAQ/AFGHANISTAN))&amp;

FI(OTHER SYMPTOMS (IRAQ/AFGHANISTAN))&amp;FI(GI SYMPTOMS (IRAQ/AFGHANISTAN))&amp; FI(PERSISTENT RASH (IRAQ/AFGHANISTAN)))

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

<!-- image -->

##### Appendix B: Reminder Dialog Opening Screen

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

**Appendix C: Reminder Terms**

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

REMINDER TERM INQUIRY	Nov 21, 2003 9:59:48 am	Page 1

**ALCOHOL USE SCREEN	No.133**

Class:	LOCAL

Sponsor:

Date Created:

Review Date:

Description:

Any local health factors for AUDT-C, refusal of alcohol screening, or no alcohol in the past year.

The Mental Health tests for AUDIT-C and CAGE are already included in this term.	If your site uses the 10 question AUDIT, then this should also be added to this term.

Findings:

Finding Item:	AUDC	(FI(1)=MH(208)) Finding Type:	MENTAL HEALTH INSTRUMENT

Finding Item:	CAGE	(FI(2)=MH(226)) Finding Type:	MENTAL HEALTH INSTRUMENT

**DEPRESSION SCREEN NEGATIVE	No.82**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

Any health factors or MH instrument scores that indicate that depression screening has been done and is negative should be mapped to this reminder term.

Depression Screen Neg (PRIME-MD, CES-D, DOM80, Ham-D) MH: DOM80=0

MH: DOMG&lt;4 MH: CRS&lt;10 MH: BDI&lt;10 MH:Zung&lt;33

Findings:

Finding Item:	DEP SCREEN 2 QUESTION NEG	(FI(1)=HF(105))

Finding Type:	HEALTH FACTOR

Finding Item:	DOM80	(FI(2)=MH(229)) Finding Type:	MENTAL HEALTH INSTRUMENT

Condition:	I V=0

Finding Item:	DOMG	(FI(3)=MH(232)) Finding Type:	MENTAL HEALTH INSTRUMENT

Condition:	I V&lt;4

Finding Item:	CRS	(FI(4)=MH(19)) Finding Type:	MENTAL HEALTH INSTRUMENT

MH Scale:	1 Condition:	I V&lt;10

Finding Item:	BDI	(FI(5)=MH(223)) Finding Type:	MENTAL HEALTH INSTRUMENT

MH Scale:	1 Condition:	I V&lt;10

Finding Item:	ZUNG	(FI(6)=MH(87)) Finding Type:	MENTAL HEALTH INSTRUMENT

MH Scale:	1 Condition:	I V&lt;33

**DEPRESSION SCREEN POSITIVE	No.83**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

Any health factors or MH instrument scores that indicate that depression screening has been done and is positive should be mapped to this reminder term.

Depression Screen Pos (PRIME-MD, CES-D, DOM80, Ham-D) MH: DOM80=1

MH: DOMG&gt;3 MH: CRS&gt;9 MH: BDI&gt;9

MH:Zung&gt;32

| Findings:       |                                                   |                                                           |                 |
|-----------------|---------------------------------------------------|-----------------------------------------------------------|-----------------|
|                 | Finding Item: Finding Type:                       | DEP SCREEN 2 QUESTION POS HEALTH FACTOR                   | (FI(1)=HF(106)) |
|                 | Finding Item: Finding Type: Condition:            | DOM80	(FI(2)=MH(229)) MENTAL HEALTH INSTRUMENT I V=1      |                 |
|                 | Finding Item: Finding Type: Condition:            | DOMG	(FI(3)=MH(232)) MENTAL HEALTH INSTRUMENT I V>3       |                 |
|                 | Finding Item: Finding Type:  MH Scale: Condition: | CRS	(FI(4)=MH(19)) MENTAL HEALTH INSTRUMENT 1  I V&gt;9   |                 |
|                 | Finding Item: Finding Type:  MH Scale: Condition: | BDI	(FI(5)=MH(223)) MENTAL HEALTH INSTRUMENT 1  I V&gt;9  |                 |
|                 | Finding Item: Finding Type:  MH Scale: Condition: | ZUNG	(FI(6)=MH(87)) MENTAL HEALTH INSTRUMENT 1  I V&gt;32 |                 |
| **GI SYMPTOMS** | **(IRAQ/AFGHANISTAN)**                            |                                                           | **No.568014**   |

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered.	Separate health factors representing positive and negative answers to the question are included in this term.	Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

| Findings:   |                 |             |                                  |          |                 |
|-------------|-----------------|-------------|----------------------------------|----------|-----------------|
|             | Finding Finding | Item: Type: | GI SYMPTOMS SCREEN HEALTH FACTOR | NEGATIVE | (FI(1)=HF(127)) |
|             | Finding         | Item:       | GI SYMPTOMS SCREEN               | POSITIVE | (FI(2)=HF(126)) |
|             | Finding         | Type:       | HEALTH FACTOR                    |          |                 |

**IRAQ/AFGHAN PERIOD OF SERVICE	No.135**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term contains a computed finding that determines if the patient's most recent service separation date was after 9/11/01.	The computed finding is included to define the cohort of patients who need to be asked about service in the combat arena.

Findings:

Finding Item:	VA-IRAQ &amp; AFGHAN SEP. DATE	(FI(1)=CF(578006)) Finding Type:	REMINDER COMPUTED FINDING

**IRAQ/AFGHAN SERVICE	No.568012**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term contains the health factor that is entered from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at sea).

Findings:

Finding Item:	IRAQ/AFGHAN SERVICE	(FI(1)=HF(125))

Finding Type:	HEALTH FACTOR

**IRAQ/AFGHAN SERVICE NO	No.134**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description: This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air

or at sea).	This health factor resolves the reminder.

Findings:

Finding Item:	NO IRAQ/AFGHAN SERVICE	(FI(2)=HF(122))

Finding Type:	HEALTH FACTOR

**OTHER SYMPTOMS (IRAQ/AFGHANISTAN)	No.568017**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered. Separate health factors representing positive and negative answers to the question are included in this term.	Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

Findings:

(FI(1)=HF(131))

(FI(2)=HF(130))

Finding Item:	OTHER PHYSICAL SYMPTOMS SCREEN NEGATIVE

Finding Type:	HEALTH FACTOR

Finding Item:	OTHER PHYSICAL SYMPTOMS SCREEN POSITIVE

Finding Type:	HEALTH FACTOR

**PERSISTENT RASH (IRAQ/AFGHANISTAN)	No.568016**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered.	Separate health factors representing positive and negative answers to the question are included in this term.	Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

| Findings:                                   |                 |             |                                  |          |                 |                 |
|---------------------------------------------|-----------------|-------------|----------------------------------|----------|-----------------|-----------------|
|                                             | Finding Finding | Item: Type: | SKIN LESION SCREEN HEALTH FACTOR | NEGATIVE | (FI(1)=HF(132)) | (FI(1)=HF(132)) |
|                                             | Finding Finding | Item: Type: | SKIN LESION SCREEN HEALTH FACTOR | POSITIVE | (FI(2)=HF(124)) | (FI(2)=HF(124)) |
| **PTSD SCREEN**                             |                 |             | **No.568013**                    |          |                 |                 |
| Class: Sponsor:  Date Created: Review Date: | NATIONAL        | NATIONAL    |                                  |          |                 |                 |
| Description:                                |                 |             |                                  |          |                 |                 |

If your site does PTSD screening, map any local health factors or exams that represent positive or negative screens for PTSD

Findings:

Finding Item:	PTSD SCREEN NEGATIVE	(FI(1)=HF(612599))

Finding Type:	HEALTH FACTOR

Finding Item:	PTSD SCREEN POSITIVE	(FI(2)=HF(612598))

Finding Type:	HEALTH FACTOR

**UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)	No.568015**

Class:	NATIONAL

Sponsor:

Date Created:

Review Date:

Description:

This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered.

Separate health factors representing positive and negative answers to the question are included in this term.	Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

Findings:

Finding Item:	UNEXPLAINED FEVERS SCREEN NEGATIVE	(FI(1)=HF(129))

Finding Type:	HEALTH FACTOR

Finding Item:	UNEXPLAINED FEVERS SCREEN POSITIVE	(FI(2)=HF(128))

Finding Type:	HEALTH FACTOR

##### Appendix D: Health Factors

| **Health Factor Group**   | **Health Factor**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALCOHOL USE               | BINGE DRINKING DRINKING ALONE  DRIVING UNDER THE INFLUENCE FAMILY HX OF ALCOHOL ABUSE HEAVY DRINKER (3 OR MORE/DAY) HISTORY OF AN ALCOHOL PROBLEM LEGAL COMPLICATIONS  MODERATE DRINKER NON-DRINKER  NON-DRINKER (NO ALCOHOL FOR &gt;1 PREV. SCREEN ETOH PROBLEM REFUSED ALCOHOL ABUSE SCREENIN REFUSED ALCOHOL USE SCREENING                                                                                                                                                                                                                             |
| IRAQ/AFGHAN               | GI SYMPTOMS SCREEN NEGATIVE GI SYMPTOMS SCREEN POSITIVE IRAQ/AFGHAN SERVICE  NO IRAQ/AFGHAN SERVICE  OTHER PHYSICAL SYMPTOMS SCREEN OTHER PHYSICAL SYMPTOMS SCREEN SKIN LESION SCREEN NEGATIVE  SKIN LESION SCREEN POSITIVE  UNEXPLAINED FEVERS SCREEN NEGA UNEXPLAINED FEVERS SCREEN POSI                                                                                                                                                                                                                                                                |
| MENTAL HEALTH             | CURRENT F/U OR RX FOR DEPRESSI DEP SCREEN 2 QUESTION NEG  DEP SCREEN 2 QUESTION POS DEPRESSION ASSESS INCONCLUSIVE DEPRESSION ASSESS NEGATIVE (NO DEPRESSION ASSESS POSITIVE (MD DEPRESSION TO BE MANAGED IN PC NO DEPRESSIVE SX NEED INTERVEN PT REFUSES TO TAKE ANTIPSYCHOT PTSD SCREEN NEGATIVE  PTSD SCREEN POSITIVE REFERRAL TO MENTAL HEALTH REFUSED AIM EVALUATION  REFUSED DEPRESSION ASSESSMENT REFUSED DEPRESSION RX/INTERVEN REFUSED DEPRESSION SCREENING UNABLE TO SCREEN-ACUTE MED CON UNABLE TO SCREEN-CHRONIC MED C ZZPTSD SCREEN NEGATIVE |