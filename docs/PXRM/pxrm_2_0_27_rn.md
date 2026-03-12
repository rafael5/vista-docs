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
source_file: pxrm_2_0_27_rn.docx
status: draft
title: pxrm 2 0 27 rn.docx
---

**PXRM*2.0*27**

## Clinical Reminders


## An expedited CR Patch release that contains:

**VA-HOMELESSNESS SCREENING and**

**VA-LIPID STATIN RX CVD/DM Clinical Reminders**


## Release Notes

**October 2012**

Product Development


Office of Health Informatics and Analytics


## Contents

Introduction	1

Clinical Reminders PXRM*2*27 Documentation	4

Web Sites	4

Acronyms	5

National Acronym Directory:	5

## Introduction

Patch PXRM*2.0*27 is a patch to the Clinical Reminder package that used the recently-approved expedited patch process. The patch releases two (2) new National reminders to the field, without any changes to routines, data dictionaries, or other package functions – “content” only. The two (2) reminders are the **VA-HOMELESSNESS SCREENING** and **VA-LIPID STATIN RX CVD/DM** reminders.

**VA- HOMELESSNESS SCREENING reminder:**

The President of The United States and The Secretary of the Department of Veterans Affairs have made it a priority (T-21 initiative) to eliminate homelessness in our Veteran population. None of our Nation’s Heroes should be homeless or at risk of becoming homeless, but sadly, studies show that more than 6% of our Veterans and/or families of Veterans nation-wide, are in this situation.

The objective of the VA-Homelessness Screening Clinical Reminder is to:  (a) identify Veterans and their families who are at imminent risk of  homelessness or who have very recently become homeless; (b) ensure that those who are at-risk or who are currently homeless are referred for the

appropriate assistance; and (c) update the current living situation for Veterans. Information collected by the VA-Homelessness Screening reminder will guide staff to refer Veterans for further assessment and the appropriate intervention to prevent or quickly end homelessness.

Efforts should be made to ensure that Veterans who screen positive are not just ***offered*** assistance, but are ***referred*** to the local Homelessness Clinic for assistance with their living situation. This VA-HOMELESSNESS SCREENING reminder is a NATIONALLY-MANDATED reminder – like the VA-TBI SCREENING and VA-IRAQ&amp;AFGHAN POST DEPLOY SCREEN reminders. It ***MUST*** be placed on the Cover Sheet ***for all staff*** at every VAMC. Any staff member may perform the screen by asking the Veteran and recording his/her answers to the few questions. If support staff are screening Veterans, the VAMC may wish to have a Hospital Policy created/altered to allow such staff the ability to order the Consult to Homelessness Services. By screening Veterans, and referring those screening positive for current homelessness or imminent risk of homelessness, we will collectively make strides to end homelessness among our Nation’s Heroes!

The Cohort logic of the reminder excludes Veterans from Homelessness Screening if a visit is found ***in the last 6 months*** in a clinic associated with any of the Stop Codes indicative of homelessness services - **504, 507, 508, 511, 522, 528, 529, 530, 590, 591, or 592.** Selecting the option in the dialog to indicate the patient is currently a resident of a long term care facility will set the frequency to every 2 years.

If the VA Medical Center does not provide Homelessness Services in any clinic with any of the Stop codes mentioned, but the facility does provide Homelessness Services in a clinic using other stop codes (Primary Care, Social Work, etc), the facility MUST have the local CAC or CR Manager ***map NEW TIU Document Titles*** created for this purpose (homelessness services), to the Reminder Term, “VA-HOMELESSNESS - ALREADY RECEIVING SERVICES”. That is done by editing one of the Computed Findings, “VA-PROGRESS NOTE”, and entering the title ***exclusively*** used for Homelessness Services, into the “COMPUTED FINDING PARAMETER” field for one of those findings. Three (3) of the VA-Progress Note computed findings were entered (blank – no title) into the Reminder Term for this purpose – in case more than one title would be used for this ***EXCUSIVE*** purpose. See post install instructions for specific details.

The VA-Homelessness Screening reminder logic is set so that Screening is due annually. Veterans that screen positive (currently homeless or being in imminent danger of homelessness)  are then screened every 6 months. Veterans answering that they currently reside in Long Term Care facilities need only be screened every 2 years.  Once a Veteran has screened negative for homelessness three (3) consecutive times, the frequency changes to every 2 years.

The reminder dialog contains a url to the National Homelessness Program Office site. That can be left as is, or preferably, sites may wish to either: a. Change the url to a local or VISN site that contains patient hand-outs pertaining to

**VA-Assess Statin Use – Lipids (CVD/DM) reminder**

Recent analyses of cardiovascular prevention studies, as well as the growing appreciation of the downsides of aggressive lipid treatment with high dose statins or non-statin cholesterol-lowering medications, have raised concerns about performance measures for lipid management based solely on achieving a target value of Low Density Lipoprotein Cholesterol (LDL-C) (Hayward and Krumholz, 2012).

The use of statin drugs can provide significant patient benefit even if LDL-C values remain above 100.   Professional societies now recommend that the adequacy of lipid management be judged by the appropriateness of the therapy and not solely by LDL value (ACCF/AHA/AMA-PCPI, 2011).  Performance measures that recognize appropriate clinical prescribing provide a better balance of patient benefit and risk and may reduce complications of overzealous drug therapy (e.g., muscle breakdown).

This national clinical reminder has been created to address the concerns outlined above and to support updated VHA Performance Measures for FY 12 and FY 13 (ihd18hns and dmg25hs) that assess LDL-C values in patients with cardiovascular disease or with diabetes mellitus or whether the patient is on at least a moderate dose of a statin medication.  The reminder replaces previous national lipid reminders that were based on threshold LDL-C values.  It was created by the VHA National Clinical Reminders Committee with input from multiple national VA experts on lipid management, diabetes mellitus, ischemic heart disease and quality measurement.  The reminder is intended to be used by providers with prescribing privileges.

The eligible cohort for the reminder includes patients ages 18-75 with ICD-9 codes indicating any type of cardiovascular disease or diabetes (based on EPRP diagnostic criteria), as well as patients on specific medications utilized in the management of diabetes.  More specifically, the reminder includes patients who meet the following criteria:

1. CVD: any diagnosis of CVD in the past 2 years that is more recent than

any entry of incorrect diagnosis of CVD and age 18-75.

1. Diabetes: 2 diagnoses in the past 2 years, or a problem list entry, or

a prescription of medication for diabetes that was active in the previous 9

months and the diagnosis or prescription is more recent than any entry of

an incorrect diagnosis.

At this time, the reminder triggers for patients ages 18-75 based on current EPRP criteria.  However, it is anticipated that these age ranges may be modified, particularly for patients with diabetes mellitus.

The reminder evaluates whether there is an LDL-C value in the past two years and whether that value is below 100.  If not, the reminder evaluates whether the patient has an active prescription for at least a moderate dose statin as defined below:

- atorvastatin  10 mg/day or higher
- fluvastatin 80 mg/day or higher
- lovastatin 40 mg/day or higher
- pravastatin 40 mg/day or higher
- rosuvastatin 5 mg/day or higher
- simvastatin 20 mg/day or higher

Patients are excluded from the reminder cohort if they have documentation of limited life expectancy or of specific types of terminal cancers.

The reminder can also be resolved for varying times if any of the following are documented:

1. Contraindication to statin use (either temporary – off for one year; or permanent – resolves permanently)
2. Documentation of moderate dose statin use (e.g. non-VA medication) – resolves for one year
3. Documentation that the patient is on the highest tolerated dose of a statin – resolves for one year
4. Documentation that the patient has had an adverse drug reaction to all available statins – resolves for one year)
5. Documentation that the patient has had an adverse drug reaction to all available statins and there is an allergy/ADR documented in the allergy package of CPRS – resolves permanently
6. Non-adherence to statin therapy – resolves for 2 months
7. Outside LDL-C value &lt; 100 – resolves for one year from date of LDL-C
8. Dosage adjustment – resolves for 2 months
9. Patient declination – resolves for 2 months
10. Order for LDL-C – resolves for  t-14 days to t+2 months
11. Incorrect diagnosis of CVD or DM – resolves for 6 months

Sites that have created risk calculators for CVD may choose to include patients with a CHD risk &gt;20% in the eligible cohort by mapping their local health factors to the CHD RISK&gt;20% reminder term.

The reminder provides a list of moderate dose statins for provider reference, allows the provider to view the most recent lipid panel results, and includes information regarding current guidance on lipid management.  It is recommended that sites continue to utilize local or national reminders for annual LDL-C assessment as long as this continues to be a performance measure.  The reminder evaluates for an LDL-C within the last two years in order to focus attention on statin therapy since this is the most important intervention and treating to goal is now felt to be less critical.

**Remedy Tickets fixed – NONE.**

**Patient Safety Issues Addressed - NONE**


### Clinical Reminders PXRM*2*27 Documentation

| **Documentation**   | **Documentation File name**   |
|---------------------|-------------------------------|
| Installation Guide  | PXRM_2_0_27_IG.PDF            |
| Release Notes       | PXRM_2_0_27_RN.PDF            |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and CPRS (OR).                                     |

## Acronyms

The OIT Master Glossary is available at: [http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)


#### National Acronym Directory:

[http://vaww1.va.gov/Acronyms/](http://vaww1.va.gov/Acronyms/)

| Term    | Definition                                                     |
|---------|----------------------------------------------------------------|
| ASU     | Authorization/Subscription Utility                             |
| CPRS    | Computerized Patient Record System                             |
| ESM     | Enterprise Systems Management (ESM)                            |
| FIM     | Functional Independence Measure                                |
| GUI     | Graphical User Interface                                       |
| IAB     | Initial Assessment & Briefing                                  |
| MH      | Mental Health                                                  |
| MHA3    | Mental Health Assistant Version 3                              |
| MHV     | My Healthy Vet                                                 |
| MST     | Military Sexual Trauma                                         |
| OIT     | Office of Information and Technology                           |
| OIF/OEF | Operation Iraqi Freedom/Operation Enduring Freedom             |
| OR      | Order Entry namespace                                          |
| PCS     | Patient Care Services                                          |
| PD      | Product Development                                            |
| PTSD    | Post Traumatic Stress Syndrome                                 |
| PXRM    | Clinical Reminder Package namespace                            |
| RSD     | Requirements Specification Document                            |
| TIU     | Text Integration Utility                                       |
| VA      | Department of Veteran Affairs                                  |
| VHA     | Veterans Health Administration                                 |
| VistA   | Veterans Health Information System and Technology Architecture |
| WV      | Women’s Health package namespace                               |
| YS      | Mental Health package namespace                                |