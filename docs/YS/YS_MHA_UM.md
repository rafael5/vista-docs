---
app_name: Mental Health (YS)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: YS
patch: 103
patch_gap: null
section: ''
source_file: YS_MHA_UM.docx
status: draft
title: YS MHA UM.docx
---

## MENTAL HEALTH ASSISTANT

<!-- image -->

**User Manual**

#### Version 3 (MHA3)

**April 2012**

#### Revised March 2020

**Version 2.0 Department of Veterans Affairs**

#### Office of Information and Technology (OI&amp;T) Product Development

**Revision History**

| **Date**    |   **Revision** | **Description**                                                                                                                                                                                                                                                               | **Author(s)**       |
|-------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Mar 2020    |            2   | Modified the document retrieval formats to YS\_501\_TM.PDF and  YS\_501\_150\_IG.PDF. Added all instruments to new functionality.                                                                                                                                             | Booz Allen Hamilton |
| Sept 2019   |            1.9 | Updated with Patch 150 information  including 5 new instruments.                                                                                                                                                                                                              | Booz Allen Hamilton |
| July 2019   |            1.8 | Adapted from YS*5.01*138 User Manual. Deactivated RAID for Patch 139.                                                                                                                                                                                                         | Booz Allen Hamilton |
| Feb 2019    |            1.7 | Adapted from YS*5.01*138 User Manual. Changes include 5 new instruments added for Patch 139 and defects fixed for 8  previously released instruments                                                                                                                          | Booz Allen Hamilton |
| Dec 2018    |            1.6 | Adapted from YS*5.01*137 User Manual. Changes include 8 new instruments added                                                                                                                                                                                                 | Booz Allen Hamilton |
| Dec 2018    |            1.5 | Adapted from YS*5.01*123 User Manual.  Changes include 7 new instruments added                                                                                                                                                                                                | Booz Allen Hamilton |
| Nov 2018    |            1.4 | Adapted from YS*5.01*136 User Manual. Changes include new GUI and instrument updates for 123.                                                                                                                                                                                 | Booz Allen Hamilton |
| Sept 2018   |            1.3 | Adapted from YS*5.01*134 User Manual. Changes include revision of Overview section with a list of 6 instruments new to Patch 136, changed file names in references to documentation from  YS501134 to YS501136.                                                               | Booz Allen Hamilton |
| August 2018 |            1.2 | Adapted from YS*5.01*123 User Manual. Changes include revision of Overview section, with a list of 6 instruments new to Patch 134; added VA Orlando VAMC and Milwaukee to list of test sites; changed file  names in references to documentation from YS501123 to YS50110134. | Booz Allen Hamilton |
| June 2018   |            2   | Added content for Patch 134 and 123  details, updated screen shots, added content for “Using Instrument Exchange”.                                                                                                                                                            | Booz Allen Hamilton |
| March 2018  |            1.1 | Updates with changes from patch 121.                                                                                                                                                                                                                                          | REDACTED            |
| April 2017  |            1   | Technical Edit                                                                                                                                                                                                                                                                | REDACTED            |
| April 2017  |            0.5 | Updated to reflect new functionality for YS*5.01*129 and removal of GAF.                                                                                                                                                                                                      | REDACTED            |
| 02/08/16    |            0.4 | With patch YS*5.01*120, updated Appendix E for Windows 7.                                                                                                                                                                                                                     | REDACTED            |

| 9/10/13   |   0.3 | Updated screen shot, page 32 (YSMANA GERmenu), removed references to MHA3 HL7 Utilities. Updated patch version names in Introduction section. Added PCLS - PTSD Checklist Stressor Specific to list of  instruments.                                                                                                             | REDACTED   |
|-----------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| 6/19/13   |   0.2 | Editing review, initiated peer review. Added New Options in VistA for Management of MHA3 section (page 32.)                                                                                                                                                                                                                      | REDACTED   |
| 6/20/12   |   0.1 | Initial Draft.  Adapted from YS*5.01*103 User Manual. Changes include revision of Overview section, with a list of instruments new to Patch 105and information about the change of PCL-SZ to PCLS; added VA New Jersey VAMC to list of test sites; changed file names in references to documentation from  YS501103 to YS501105. | REDACTED   |

**Table of Contents**

Orientation	1

Documentation Retrieval Locations and Formats	1

Retrieval Formats Information 	1 Retrieval Locations: 	1 VistA Website Locations: 	1 Related Manuals 	2

Introduction	2

Overview	2

Specific Instrument Details: 		6 New Functionality	10

Test Sites 	10 Use of the Software	10

Contingency Planning	10

Security Keys	11

Windows Conventions	11

Mental Health Assistant and Section 508 Compliance	11

Mental Health Assistant Temporary Crash Files	11

Mental Health Assistant Results and CPRS Progress Notes	12

Mental Health Assistant Results and CPRS Consults	12

Starting Mental Health Assistant	13

Starting Mental Health Assistant from VistA CPRS Tools Menu	13

Starting Mental Health Assistant from Off-line Mode	15

Mental Health Assistant Main Menu Functions	16

Selected Patient Identification Label 	16 Title Bar 	16 Launch Links 	16 Starting the Instrument Administrator 	17 Starting the Instrument Results Review Functions	18

Starting the Addiction Severity Index (ASI) Manager Function	20

File Menu 		22 Tools Menu 	25 New Options in VistA for Management of MHA3		30

Management of Progress Notes Generated by MHA	31

Managing Time to Save an Incomplete Instrument	31

Removing Patient Data that was Entered in Error	32

Instrument Exchange Utility 	33 Instrument Administrator Functions	33

Orientation 	33 Main Menu 	34 Ordering Instruments 	35 Selecting a Person (other than yourself) for “Instruments Ordered By”	36

Selecting a Person for “Interviewer” 	37

Selecting a Date of Administration 	38 Selecting a Visit Location 	39 Selecting a Consult (Optional) 	40 Choosing One or More Instruments 	42 Restarting Incomplete Administrations	43

Manipulate the list of Instruments Chosen	43

Selecting Display Mode for Data Entry	44

Selecting “Patient Entry” Data-Entry Mode	45

Selecting “Staff Entry” Data-Entry Mode	47

On-form Instructions 	48 Printing a Blank Instrument 	49 Reviewing a Description of the Selected Instrument	55

Instrument Administrator’s Battery Wizard	57

Orientation 	57 Main Menu 	58 Title bar 	58 Available Instruments and Batteries list	58

Instruments in Battery list 	58 Re-sequencing buttons 	58 Context-sensitive Help 	58 Battery Selector 	58 Save Button 	59 Invoking the Battery Wizard 	59 Battery Wizard: Creating a New User-defined Battery	61

Renaming an Existing Battery 		64 Exiting the Battery Wizard 	69 Instrument Administrator’s “One Question at a Time” Input Form		70

Orientation 	70 The Main Menu 	71 The Selected Patient Identification Label	71

The Instrument’s Name 	71 The Introduction Text 	71 The Question Text 	71 The Response Artifact 	71 The Navigation Buttons 	71 The Progress Indicator 	71 The Review Answers Form 	71 Responding to a Multi-choice Question Using a Multiple-Selection List Box          72

Responding to a Single-choice Question Using a Drop-Down List Box	73

Responding to a Question that Asks for a Currency Amount using a Text Box      74

Responding to a Question that Asks for a Date Using a Date-Picker	75

Responding to a Question that Asks for a Line of Text using a Text Box	76

Responding To A Question From A List Of Answers Using A Single-Selection List Box 	77 Responding To A Question Using A Masked Text Box That Pre-Formats Input Data

78

Respond To A Question Using A Spin Box That Asks For An Integer Value	80

Responding To A Question That Asks For A Single Choice From A List Using Option Buttons 	81 Responding To A Question That Asks For A Staff Name From Vista Using A Drop- Down List Box 	82 Responding To A Question That Asks For A Value From A Slider	83

Incomplete Data-Entry Session 	86 Viewing the Next Instrument 	87 Viewing the Prior Question 	88 View Next Question 	89 Review Answers 	90 Exiting Data-Entry Session without Saving the Answers	92

Instrument Administrator’s “All Questions At Once” Input Form	93

Orientation 	93 Main Menu 	94 Selected Patient Identification Label 	94 Instrument’s Name 	94 Section Text 	94 Introduction Text 	94 Question Text 	94 Response Artifact 	94 Navigation Scroll Bar 	94 Instrument Tabs 	94 Navigation 	95 Finish button 	96 Selecting an Instrument within a Series	98

To Review Answers Given: 		99 Change a Previously-given Answer 	100 Suspend Responding To Questions And Save The Administration In An Incomplete State 	101 Exiting Data-Entry Session without Saving the Answers	102

Instrument Results Review Functions	103

Orientation 	103 Main Menu 	108 Selected Patient Identification label 	108 Instrument’s Name 	108 List of Previously-Administered Tests 	108 The Navigation Tabs 	108 Saving a Graph, Report, or a Table to a File	109

Printing a Graph, Report or Table. 	111 Copying a Graph, Report, or Table to the Windows Clipboard	112

Switching Views in Instrument Results Review	113

Appending Comments to an Existing Record	114

Removing Data Entered in Error 	119 Special Results Wizard 	125 Exiting the Instrument Results Review Form	130

<!-- image -->

131

133

Selected Patient Identification Label 	133 Title Bar 	133 List of Previously-Administered ASIs 	133 Report View 	133 Navigation Tabs 	133 ASI Editing Buttons 	133 Days Since Last ASI Label 	133 Determining the Number of Days since the Last ASI for Selected Patient	134

Selecting a Report Type 	136 Restarting an Unsigned ASI 	137 Starting a New ASI 	138 Saving a Report, Graph or Table to a File	141

Copying a Report, Graph, or Table to the Windows Clipboard	144

Navigating through the Different Views on the ASI Manager Form	146

ASI: Data Entry 	147

<!-- image -->

Option Button Groups 	151 Item G12 	154 Item G19 	155 Medical Status Comments 	159 Ending an ASI Data-entry Session 	160 Closing ASI Data-entry Session with “Exit” option	161

Closing ASI data-entry session with “Finish Later” option	162

Closing ASI data-entry session with “Save and sign”	163

ASI: Business Rules	164

ASI : Changing User Preferences	169

Default Form Size/Position 	170

<!-- image -->

Highlight Color 	170 ASI: Help Menu Options	171

Opening the ASI Help File 	171 Using the Help Index 	172 Domain Scores 	173 Item Trends 	174 Graphing a Different Item 	175 Returning to the Narrative Report View	176

User Preferences Functions	177

<!-- image -->

Form Title 	178 Navigation Tabs 	178 Editing Panel 	178 Command Buttons 	178 Changing MHA System Font 	178 Changing the Displayed Highlight Colors on the All-Questions Data-input Form -181

Toggling Visual Feedback On/Off 	182 Toggling Screen Reader On/Off 	182 Toggling Speed Tab On/Off 	183 Toggling The Display Of Images On The Main Menu	184

Toggling: Maintain Original Font on/off	185

Selecting the starting point for MHA 	186

<!-- image -->

Off-line Results Synchronizer 	188

<!-- image -->

Off-line Records List 	190 CPRS Patient Search Panel 	190 Patient Match Panel 	190 Delete Off-line Record Button 	190 Upload Button 	190 Exit button 	190 Starting MHA in Off-line Mode from the Desktop Icon	191

Selecting an Existing Patient from the Drop-Down List Box	192

Adding and Selecting a New Off-line Patient	193

Selecting a Different Off-line Patient from the Instrument Administrator Form     195

Deleting an Existing Off-line Patient 	197 Canceling Selection of an Off-line Patient	198

Closing the Off-line Patient Manager 	199 Recognizing the Availability of Off-line Administrations, and Initiating the Upload Process 	199 Selecting an Off-line Record for Uploading	201

Searching for a Matching CPRS Patient	202

Evaluating the results of a possible match	203

Uploading an Off-line Record to VistA 	206 Deleting an Off-line Record 	208 Exiting the Off-line Results Synchronizer Form	209

Single-Instrument Administrator Functions	210

<!-- image -->

210

211

Selected Patient Identification Label 	211 Instrument’s Name 	211 List of Previously-Administered Tests 	211 Report View 	211 The Navigation Tabs 	211

<!-- image -->

211

211

Graph and Table 	212 Invoking the Single-Instrument Administrator from the CPRS Tools Menu	214

Starting a New Administration 	216 Editing an Existing Editable Administration	220

Exiting the Single Instrument Administrator Form	221

Glossary 	222

Glossary of GUI components used in MHA	224

Component/Terms	224

Descriptions	224

#### Appendix A	228

Shortcut Keys 	228

#### Appendix B	236

How to co-sign a progress note generated by MHA	236

#### Appendix C	237

How to Remove Patient Data That Was Entered In Error: Vista Menu Instructions. 237

#### Appendix D	239

SecureDesktop &amp; Screen Pass: How to correct Windows-Registry problems.	239

Secure desktop: How To Correct Dwlgina2.Dll Problems	240

#### Appendix E	241

Setting up VistA MHA3 on CPRS GUI Tools Menu for SecureDesktop	241

Setting up VistA MHA3 on CPRS GUI Tools Menu for SecureDesktop	241

#### Appendix F	243

How to Add the Name of an Instrument to the CPRS Tools Menu	243

#### Appendix G	244

Using Instrument Exchange	244

## Orientation

#### Documentation Retrieval Locations and Formats

Retrieval Formats Information

| **FILE NAMES**    | **CONTENTS**                                                              | **RETRIEVAL FORMATS**   |
|-------------------|---------------------------------------------------------------------------|-------------------------|
| YS_MHA3_UM.pdf    | Mental Health Assistant Version 3 (MHA3) User  Manual Patch YS*5.01*150   | BINARY                  |
| YS_501_TM.PDF     | Mental Health Assistant Version 3 (MHA3) Tech Manual Patch YS*5.01*150    | BINARY                  |
| YS_501_150_IG.PDF | Mental Health Assistant Version 3 (MHA3) Install  Guide Patch YS*5.01*150 | BINARY                  |

Retrieval Locations:

User Manuals(YS\_MHA3\_UM.pdf, YS\_MHA3\_TM.pdf and YS\_501\_150\_IG.pdf) are available in Portable Document Format (pdf) at the Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directory FTP addresses listed below:

**NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “ *download.vista.med.va.gov* ” (without the quotes) to connect to the first available FTP server where the files are located.

<!-- image -->

| **OI FIELD OFFICE**   | **FTP ADDRESS**   | **DIRECTORY**   |
|-----------------------|-------------------|-----------------|
| REDACTED              | REDACTED          | REDACTED        |
| REDACTED              | REDACTED          | REDACTED        |

VistA Website Locations:

User Manuals(YS\_MHA3\_UM.pdf, YS\_MHA3\_TM.pdf and YS\_501\_150\_IG.pdf) are available in Portable Document Format (pdf) at the REDACTED

Related Manuals

VistA Mental Health (MH) Addiction Severity Index Multimedia Version (ASI-MV) Installation and User Guide (Patch YS*5.01*78).

[http://www.va.gov/vdl/](http://www.va.gov/vdl/)

## Introduction

### Overview

The Mental Health Assistant (MHA) is the graphical user interface (GUI) for the VistA Mental Health Package (MHP). MHA was developed to create an effective and efficient tool for mental health clinicians, primary care clinicians and their patients to use for the administration and scoring of assessment instruments and interviews. Additionally, results are displayed in report and graphical formats. MHA and MHP support mental health instruments (e.g., psychological tests, structured interviews, and staff rating scales), pain assessments, nursing assessments, and additional instruments that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA). MHA has enjoyed widespread usage among mental health clinicians over the past several years, and the current revisions of MHA and MHP initiate steps toward re-engineering VistA Mental Health functionality.

The original revision of MHA created a closer integration with CPRS, by placing the MHA GUI on the CPRS Tools Menu. Additionally, functionality was created to allow a site to place an individual instrument on the CPRS Tools menu, allowing widespread access to that specific instrument without having to issue the menu for the MHP to all clinicians.

Additional functionality that strengthens the tie to the patient’s medical record is the creation of a progress note in CPRS when an instrument is completed through MHA.

Furthermore, MHA maintains and strengthens its ties to the Clinical Reminders program, which allows for the presentation of specific instruments through reminder dialogs to all clinicians who resolve reminders.

To better meet the needs of clinicians and patients in different programs, particularly non- traditional settings, MHA can now run in a stand-alone mode to administer instruments offline for later uploading to VistA.

***Mental Health Patch YS*5.01*103*** added 20 new instruments to the library of instruments. Patch 103 added two retired instruments to active status. Patch 103 also included the following enhancements:

- Improve navigation by providing users a simpler option to go back to a previous screen in the Mental Health Assistant. An example would be something similar to the back arrow in Internet Explorer.

Users are confused with clicking on “X” in upper right-hand corner of form (usually this action would terminate an application) to back up in the current version or the several steps needed to click on the FILE|EXIT menu option.

- Ability for users to select a consult to connect to the instrument’s administration is now supported.

- Users can print a blank instrument suitable for pencil-and-paper completion (except for the ASI and restricted instruments).

- A new tab on the “Instrument Review Results” page presents summary data of important instruments for the clinician.

- MHA can start at one of the four main options, i.e., Instrument Administrator, Instrument Review Results, ASI Manager, or at the traditional Main Menu. The user can select their preference.

***Mental Health Patch YS*5.01*105*** provided enhancements with the addition of 22 new instruments:

Note: This includes one update and three retired instruments.

| **Short Name**   | **Full Name**                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| AAQ-2            | The Acceptance and Action Questionnaire (AAQ-2)                                               |
| BAM-C            | Brief Addiction Monitor - Consumption Items                                                   |
| BAM-IOP          | Brief Addiction Monitor - IOP version                                                         |
| BAM-R            | Brief Addiction Monitor - Revised                                                             |
| BARTHEL INDEX    | Barthel Index of Activities of Daily Living                                                   |
| FFMQ             | Five Facet Mindfulness Questionnaire                                                          |
| GPCOG            | General Practitioner Assessment of Cognition                                                  |
| IADL             | Katz Index of Independence in Activities of Daily Living                                      |
| MBMD             | Millon Behavioral Medicine Diagnostic--Bariatric Norms  *Note: this is an updated instrument* |
| MHLC-C           | Multidimensional Health Locus of Control: Form C                                              |
| MMPI-2-RF        | Minnesota Multiphasic Personality Inventory-2-Restructured Form                               |
| MOCA             | Montreal Cognitive Assessment                                                                 |
| MOCA ALT 1       | Montreal Cognitive Assessment, Alternate 1                                                    |
| MOCA ALT 2       | Montreal Cognitive Assessment, Alternate 2                                                    |
| NEO-PI-3         | NEO Personality Inventory-3                                                                   |
| PCLS             | Post Traumatic Stress Disorder (PTSD) Checklist Stressor Specific                             |
| PHQ-15           | Patient Health Questionnaire 15-Item Somatic Symptom Severity Scale                           |
| QOLI             | Quality of Life Inventory                                                                     |
| SSF              | Status of Suicide Form                                                                        |
| STMS             | Short Test of Mental Status                                                                   |
| VR-12            | Veterans Rand 12 Item Health Survey                                                           |
| VRA              | Veteran Recovery Assessment                                                                   |
| WHODAS 2         | World Health Organization Disability Assessment Schedule 2.0                                  |

***Mental Health Patch YS*5.01*129*** provided support for the mandated security requirement that VistA applications provide two-factor authentication via a Personal Identity Verification (PIV) card. When signing in, you are prompted for your PIV personal identification number (PIN) instead of access/verify codes.

The Global Assessment of Function (GAF) is no longer recommended and has been removed from MHA. In addition, patch 129 inactivates the following instruments:

Alcohol Use Inventory (Revised)	AUIR

Center for Epidemiologic Studies Depression Scale (5-item version)	CESD5 Depression Outcome Module 8.0	DOM80

Depression Outcomes Module: Geriatric Screen	DOMG

Employment Readiness Scale	ERS

Health Locus of Control Scale	HLOC

Rotter Internal-External Scale	IEQ

Rotter Locus of Control	RLOC

Spiritual Assessment Inventory	SAI

Crowne-Marlowe Social Desirability Scale	SDES

Short Michigan Alcoholism Screening Test	SMAST

Validity Scale	VALD

Ward Atmosphere Scale	WAS

***Mental Health Patch YS*5.01*121*** added 17 new instruments, listed below.

| **Short Name**        | **Full Name**                                                                |
|-----------------------|------------------------------------------------------------------------------|
| ASSIST-NIDA           | Alcohol Smoking and Substance Involvement Screening  - NIDA modified version |
| BRS                   | Brief Resiliency Scale                                                       |
| CCSA-DSM5             | Cross-Cutting Symptom Assessment for DSM-5                                   |
| CEMI                  | Client Evaluation of Motivational Interviewing                               |
| CSI                   | Couple Satisfaction Index                                                    |
| CSI-4                 | Couple Satisfaction Index - 4 Item                                           |
| CSI PARTNER VERSION   | Couple Satisfaction Index Partner Version                                    |
| CSI-4 PARTNER VERSION | Couple Satisfaction Index - 4 Item Partner Version                           |
| GAI                   | Geriatric Anxiety Inventory                                                  |
| ISI                   | Insomnia Severity Index                                                      |
| KATZ-ADL-6pt          | Modified Katz Index of ADLs                                                  |
| PSOCQ                 | Pain Stages of Change Questionnaire                                          |
| PSS                   | Perceived Stress Scale                                                       |
| RLS                   | Restless Legs Syndrome Rating Scale                                          |
| SMEQ                  | Smith Morning-Evening Scale                                                  |
| SNQ                   | Sleep Need Questionnaire                                                     |
| STOP                  | Snoring, Tired, Observed, Blood Pressure                                     |

***Mental Health Patch YS*5.01*134*** added 6 new instruments, listed below.

| **Short Name**    | **Full Name**                                                          |
|-------------------|------------------------------------------------------------------------|
| PHQ-2+i9          | Patient Health Questionnaire 2 + Item 9                                |
| PSS3              | Patient Safety Screener 3                                              |
| PC-PTSD-5         | PTSD Screen                                                            |
| PC-PTSD-5+i9      | PTSD Screen + PHQ Item 9                                               |
| C-SSRS            | Columbia Suicide Severity Rating Scale                                 |
| WHODAS 2.0-12item | World Health Organization Disability Assessment Schedule 2.0 – 12-item |

***Mental Health Patch YS*5.01*136*** added 6 new instruments, listed below.

| **Short Name**   | **Full Name**                             |
|------------------|-------------------------------------------|
| BPRS-A           | Brief Psychiatric Rating Scale – Anchored |
| PSS3-2  nd       | Patient Safety Secondary Screener         |
| PCL-5 Weekly     | PCL-5 Weekly                              |
| HSI              | Heaviness of Smoking Index                |
| WEMWBS           | Warwick Edinberg Mental Well Being Scale  |
| MHRM             | Mental Health Recovery Measure            |

***Mental Health Patch YS*5.01*123***

The primary purpose of this patch is to move instruments previously scored in the YS\_MHA\_AUX DLL to VistA. The scoring changes result in MHA (Mental Health Assistant) scores being reported in Reminder Dialogs and the Health Summary for these instruments properly. The following instruments are now scored in VistA:

| **Short Name**       | **Full Name**                                         |
|----------------------|-------------------------------------------------------|
| AUDC                 | Alcohol Use Disorders Identification Test Consumption |
| BAI                  | Beck Anxiety Inventory                                |
| BAM-C                | Brief Addiction Monitor - Consumption Items           |
| BAM-R                | Brief Addiction Monitor - Revised                     |
| BASIS-24             | Behavior and Symptom Identification Scale-24          |
| BDI2                 | Beck Depression Inventory – Second Edition            |
| BHS                  | Beck Hopelessness Scale                               |
| BSS (previously BSI) | Beck Scale for Suicide Ideation                       |
| CDR                  | Clinical Dementia Rating                              |
| FAST                 | Functional Assessment Staging                         |

| **Short Name**   | **Full Name**                                                    |
|------------------|------------------------------------------------------------------|
| ISMI             | Internalized Stigma of Mental Illness Inventory                  |
| MINICOG          | Mini-Cog                                                         |
| MMPI-2-RF        | Minnesota Multiphasic Personality Inventory-2- Restructured Form |
| NEOP-I-3         | NEO Personality Inventory-3                                      |
| PC PTSD          | Primary Care PTSD Screen                                         |
| PHQ-2            | Patient Health Questionnaire 2                                   |
| POQ              | Pain Outcomes Questionnaire                                      |
| QOLI             | Quality of Life Inventory                                        |
| STMS             | Short Test of Mental Status                                      |
| VR-12            | Veterans Rand 12 Item Health Survey                              |
| WHODAS 2         | World Health Organization Disability Assessment Schedule 2.0     |
| WHYMPI           | West Haven-Yale Multidimensional Pain Inventory                  |

Additionally, the scoring algorithm was changed so that every instrument score is persistently stored in the MH RESULTS File (#601.92). Should an instrument need to be rescored for any reason, there has been functionality added to retain previous scores.

Specific Instrument Details:

The **Brief Addiction Monitor (BAM)** has been retired. The BAM-R and BAM-IOP should be used instead. The Primary Care PTSD Screen (PC PTSD) has been retired. The PC-PTSD-5 or PC-PTSD-5-I9 should be used instead.

The **BSI was renamed to the BSS** . Scoring the instrument was also modified.  Prior to this patch all questions were included in the score, now only questions 1-19 are included in the scoring so the maximum score for the instrument is 38. The current scoring rule stipulates that if more than 5 questions are not answered the instrument would not be scored has been removed.

The instrument will now be scored regardless of how many questions are skipped. Skip logic has been added so that if the response to Question 20 is "I have never attempted suicide" (0), question 21 is not asked. The categories of risk have been removed from the report and the following text has been added:

The BSS is intended to assess thoughts, plans and intent to die by suicide or attempt suicide over the past week. Total scores can range from 0-38. There is no specific cut-off score to classify severity or guide patient management, however, increasing scores reflect

greater risk, and any positive response to any item may reflect the presence of suicidal intention and should be investigated further.

The **VR-12** , question 7 had incorrect responses. The responses prior to the modification were:

| 1. All of the time         | 3. A good bit of the time   | 5. A little of the time   |
|----------------------------|-----------------------------|---------------------------|
| 2. Most of the time        | 4. Some of the time         | 6. None of the time       |
| The correct responses are: |                             |                           |
| 1. All of the time         | 3. Some of the time         | 5. None of the time       |
| 2. Most of the time        | 4. A little of the time     |                           |

The responses have been changed to the correct responses. Any previously administered instrument will have response #3 (A good bit of the time) mapped to response #2 (Most of the time) during the patch install.

Additionally, the scoring algorithm for the VR-12 was modified to consider skipped questions in the administration.

The **Beck Depression Inventory--Second Edition (BDI2** ) results review has been changed. If the response to Item 9 (SUICIDAL THOUGHTS OR WISHES) is 1, 2, or 3 the following statement is added to the report after score:

*Responses consistent with the presence of suicidal ideation were endorsed in positive direction (item-9), additional clinical assessment is indicated.*

The **Brief Addiction Monitor - Revised (BAM-R)** was revised to correct a scoring error. Prior to this patch question 17 was included in the Protective Factors Scale score rather than question 16 resulting in an incorrect scale score. Question 16 is now used in the calculation.

The **NEO Personality Inventory-3 (NEO-PI-3)** Instrument Results Review was modified to display messages when it appears that the respondent answered the items in a random fashion resulting in an invalid administration.

The **West Haven-Yale Multidimensional Pain Inventory (WHYMPI** ) was revised to correct a scoring error. The Affective Distress Scale did not properly reverse-score the response to question 6 prior to calculating the score and has been corrected.

The **Patient Health Questionnaire-2 (PHQ-2)** Instrument Results Review was modified. The statement that explains if the screening score indicates a positive or negative result was changed. Additionally, the 2 questions were made required.

Currently an example statement is: A score of 4 or more indicates a positive screen.

The statement has been changed to: The score on this administration is 4, which indicates a positive screen on the Depression Scale over the past two weeks.

**Globally for any instrument with skip logic** : the skip logic did not work correctly when an instrument was administered using the "One question at a time" function in the Instrument Administrator. If the next to last question should be skipped, MHA did not automatically move to the last question, rather it required the user to click on the 'Next Question' button.

Modifications were made so that the user is prompted for the last question.

**Instruments that have a 'checklist' box question** such as the Suicide Behavior Report did not display the last choice in the list box. While a user could select the item, arrow keys had to be used to see the item although it was not intuitive to do so. Modifications were made so that

all items are visible in a left justified list.

***Mental Health Patch YS*5.01*137*** added 7 new instruments, listed below.

| **Short Name**     | **Full Name**                                                     |
|--------------------|-------------------------------------------------------------------|
| AD8                | Ascertain Dementia 8-item Informant Questionnaire                 |
| EPDS               | Edinburgh Postnatal Depression Scale                              |
| FTND               | Fagerström Test for Nicotine Dependence                           |
| CES                | Combat Exposure Scale                                             |
| MPI-PAIN-INTRF     | WHYMPI Pain Interference Scale                                    |
| BASIS-24 PSYCHOSIS | Behavior and Symptom Identification Scale 24 – Psychosis Symptoms |
| IJSS               | Indiana Job Satisfaction Scale                                    |

***Mental Health Patch YS*5.01*138*** added 8 new instruments, listed below.

| **Short Name**   | **Full Name**                                                         |
|------------------|-----------------------------------------------------------------------|
| I9+C-SSRS        | PHQ-Item 9 + Columbia Suicide Severity Rating Scale                   |
| Q-LES-Q-SF       | Quality of Life Enjoyment and Satisfaction Questionnaire – Short Form |
| WHOQOL-BREF      | World Health Organization: Quality of Life – BREF                     |
| MCMI-IV          | Millon Clinical Multiaxial Inventory-IV                               |
| PROMIS 29        | Patient Reported Outcome Measurement Information System               |
| IMRS             | Illness Management and Recovery Scales                                |
| DBAS             | Dysfunctional Beliefs and Attitudes About Sleep                       |
| ISS-2            | Internal State Scale – Version 2                                      |

***Mental Health Patch YS*5.01*139*** added 5 new instruments and addressed defects reported for 8 previously released instruments, listed below.

(5) New Instruments Added

| **Short Name**   | **Full Name**                                             |
|------------------|-----------------------------------------------------------|
| D.ERS            | Difficulties in Emotion Regulation Scale                  |
| CSDD-RS          | Cornell Scale for Depression in Dementia – Response Sheet |
| BBHI-2           | Brief Battery for Health Improvement 2                    |
| COPD             | Chronic Obstruction Pulmonary Disease Assessment Test     |
| RAID             | Rating Anxiety In Dementia                                |

1. Instruments with Defect Fixes
| **Short Name**   | **Defect Fixed**                                                                                                                                                                                                                                                                |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BPRS-A           | - Improve text wrapping on the Progress Note - Capitalize the word ‘withdrawal’ in Question 3 - Capitalize the words ‘frequently’ and ‘constantly in Question 6, response options 3 and 4 - Capitalize the word ‘irritable’ in Question 17, response option 3                   |
| HSI              | Remove extra quotation mark from the instrument description                                                                                                                                                                                                                     |
| PCL-5 Weekly     | Change the Cluster E range from (items 15-22) to (items 15-20)                                                                                                                                                                                                                  |
| PC-PTSD-5+I9     | - Improve text wrapping on the Report - Add ‘PC-PTSD-5+I9’ to the beginning of the PTSD Screen score results on the report - Add ‘PC-PTSD-5+I9’ to the beginning of the Suicide Screen score results on the report - Add the score to the line above the descriptive score text |
| PHQ-2+I9         | Change the word ‘require’ to ‘required’ in the copyright text                                                                                                                                                                                                                   |
| PSS-3 2nd        | Change capitalization on the word ‘patient’ in Question 3 so that it is now lowercase                                                                                                                                                                                           |
| MHRM             | Update graph table to only show the scores once instead of twice                                                                                                                                                                                                                |
| QOLI             | Capitalize the first letter of each word for all the response options throughout the instrument                                                                                                                                                                                 |

### New Functionality

***Mental Health Patch YS*5.01*150*** added 11 new instruments, listed below.

| **Short Name**   | **Full Name**                                       |
|------------------|-----------------------------------------------------|
| CMQ              | Composite Morningness Questionnaire                 |
| SIP-AD-30        | Short Inventory Of Problems - AD                    |
| SIP-AD-START     | Short Inventory Of Problems - AD                    |
| BSL-23           | Borderline Symptom List 23                          |
| NuDESC           | Nursing Delirium Screening Scale                    |
| AD8              | Ascertain Dementia 8                                |
| SWEMWBS          | The Short Warwick–Edinburgh Mental Well-being Scale |
| FOCI             | The Florida Obsessive Compulsive Inventory          |
| MHRM-10          | Mental Health Recovery Measure-10                   |
| EAT26            | Eating Attitudes Test- 26                           |
| ACE              | Adverse Childhood Experiences                       |

Test Sites

Patch YS*5.01*150 will be tested by the following Veteran Affairs Medical Centers (VAMCs) and Healthcare Network Systems (HCS):

| **Test Sites/Integrated**   | **Operating System Platform**   | **Test Site Size**   |
|-----------------------------|---------------------------------|----------------------|
| Orlando                     | Cache/VMS                       | Large/Integrated     |
| Milwaukee                   | Cache/VMS                       | Large/Integrated     |

### Use of the Software

This section describes what is needed to successfully use the new **Mental Health Assistant,** Version 3 (MHA) software application for the following activities:

- Instrument Administrator
- Instrument Results Review
- Addiction Severity Index (ASI) Manager

### Contingency Planning

Each facility using the MHA software application **must** develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan **must** identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

### Security Keys

MHA software application did not release any new security keys. The YSP security key is still required to control access to the results of “non-exempt” instruments. While anyone may administer a “non-exempt” instrument, only psychologists with the YSP security key may view the results. Holders of the YSP security key are determined by the Chief of Psychology or a senior psychologist at a facility that does not have a Chief of Psychology. The Chief of Psychology or senior psychologist also determines which tests are “exempt” (i.e., the results can be seen by anyone), and which are “non-exempt” (i.e., require the YSP key to see the results).

### Windows Conventions

The startup, setup, and assignment functions for MHA use a Graphical User Interface (GUI). The glossary provides examples and explanations of many Window conventions.

**NOTE:** Please see Appendix A, (located in the back of this manual) for a revised list of MHA shortcut keys. The list can be removed from this manual for easy access and viewing.

<!-- image -->

### Mental Health Assistant and Section 508 Compliance

MHA can detect when a screen reader is in use. As a result, many of the operations within MHA are changed to enhance the readability and operations for screen readers. For example, group boxes are given more elaborate captions to explain the functions of the next component that the user will tab in to. Graphs of results are not presented, but the data are available in table form when a screen reader is detected.

Since radio groups, which form most of the multiple-choice questions employed in instruments, are not handled well by screen readers such as JAWS, the radio groups are replaced by list boxes. List boxes are read by screen readers without difficulty. The text of the questions and answers are the same whether presented as a radio group or a list box.

This manual is written so that it can be read by those who use screen readers. However, the screen shots contained in this manual may be different than those displayed in the application when a screen reader is in use.

### Mental Health Assistant Temporary Crash Files

To prevent data loss resulting from MHA being improperly closed (e.g., power outage), MHA creates a **temporary crash file** on the local PC hard drive when instruments are in the process of being administered. This temporary crash-file is updated each time a response is made; therefore,

the temporary crash-file is always current. Upon normal program closure, this temporary crash- file is erased. Each time MHA begins, it looks for the temporary crash-file on the PC hard drive. If it exists, the data in the temporary crash-file are uploaded to the VistA Mental Health Package (MHP) database so the user can restart the incomplete administration. No data that identifies the patient are contained in the crash file (e.g., name, SSN).

### Mental Health Assistant Results and CPRS Progress Notes

Under normal circumstances and proper setup, the results of the instruments administered in MHA will become progress notes in CPRS.

If progress notes are not generated, the Clinical Applications Coordinator should be notified. If it does not already exist, create the progress note title of "Mental Health Diagnostic Study Note" in the progress note hierarchy. This is needed for MHA to automatically pass a note to CPRS from instrument administrations completed within MHA.

Some instruments do not generate progress notes because their results are to be viewed by designated staff; for example, the results of the Minnesota Multiphasic Personality Inventory, version 2, can only be viewed by psychologists who have the YSP key.

**Example:** The interviewer has the option to generate a progress note at completion of the AUDIT administration:

<!-- image -->

### Mental Health Assistant Results and CPRS Consults

You can create a Text Integration Utility (TIU) note within MHA containing the results of the instrument administered to the patient and linking it to a consult for that patient.

The site is required to create a new TIU note title called MENTAL HEALTH CONSULT NOTE. If the user selects a consult from the dropdown list in the ‘Link With Consult (optional)’ box of the **Instrument Administrator** and completes an instrument, the MENTAL HEALTH

CONSULT NOTE will be created and filed with the results of that instrument. The note will be linked to the consult selected. Only open consults are available for this process.

### Starting Mental Health Assistant

There are two ways to start Mental Health Assistant:

- VistA CPRS Tools Menu
- Off-line Mode

#### Starting Mental Health Assistant from VistA CPRS Tools Menu

The CPRS Tools menu is the standard way of connecting to the MHA software application. Since all MHA functionality is started and available to the user via the CPRS Tool menu, the CPRS software application **must** be installed on the PC workstation where Mental Health Assistant functionality is to be administered. The Mental Health Assistant software application is normally used by clinicians at VAMCs and VA satellite clinics where a “live” network connection to VistA is available. Most of the functionality described in this user manual assumes that the user is operating via the CPRS Tools menu.

**NOTE:** When the user’s VistA account is properly configured, there will be a **Mental Health Assistant** menu located on the CPRS Tools menu (as seen in the example below). If the **Mental Health Assistant** menu is missing from the CPRS Tools menu, users should contact their clinical coordinator to have it added.

<!-- image -->

To start the CPRS software application **click** on the CPRS icon located on the Windows Desktop.

**Example:** CPRS icon located on the Windows Desktop.

<!-- image -->

Once the CPRS software application is started **click** on the CPRS drop-down list **Tools** menu to start

###### Mental Health Assistant.

**NOTE:** If **Mental Health Assistant** asks users to logon to VistA again, users may contact their clinical coordinator to inquire about the availability of a Single Sign-on.

<!-- image -->

**Example:** CPRS drop-down list Tools menu displays **Mental Health Assistant** .

<!-- image -->

**Click** on the “ **Mental Health Assistant”** menu item to start MHA. The splash screen is displayed briefly followed by the MHA main menu.

**Example:** The Mental Health Assistant splash screen provides the version number of the Mental Health Assistant application. The red arrow below indicates the updated version number.

<!-- image -->

**Example: Mental Health Assistant main menu**

<!-- image -->

#### Starting Mental Health Assistant from Off-line Mode

Alternatively, off-line mode should be used only when the user and equipment are located at a remote site which has no means of connecting to the VistA network. The off-line mode starts only the smaller subset of the Mental Health Assistant functionality. This functionality handles administering instruments while not connected to VistA. To benefit from the work performed in the off-line mode, the user must eventually reconnect to the VistA network, at which time the off-line mode data is uploaded to the VistA database.

**NOTE:** Specific details about the Off-line mode are discussed later in this manual.

<!-- image -->

To start the **Mental Health Assistant** from the off-line mode **click** on the **Mental Health Assistant 3** icon located on the Windows Desktop.

**Example:** Mental Health Assistant 3 icon.

<!-- image -->

**Click** on the **Yes** command button located on the **Mental Health Assistant** dialog box to start the

**Off-line mode** function.

**Example:** Mental Health Assistant dialog box.

<!-- image -->

### Mental Health Assistant Main Menu Functions

The **Mental Health Assistant** main menu is the starting point for launching the three major activity areas in MHA:

<!-- image -->

- Instrument R esults Review
- A ddiction Severity Index Manager

#### Selected Patient Identification Label

The Selected Patient Identification label displays information about the currently-selected patient within MHA. All functions performed in MHA apply to this patient. This patient is the same as the one selected in CPRS and should remain synchronized with CPRS even when another patient is selected.

#### Title Bar

The Title Bar is used throughout MHA to display information about the context that applies to the current activity.

#### Launch Links

<!-- image -->

##### Instrument Administrator

<!-- image -->

##### Instrument Results Review

The Instrument R esults Review launch link starts the Instrument Review activity, where results of previous administrations are visible.

##### Addiction Severity Index Manager

The A ddiction Severity Index Manager launch link starts the ASI Manager activity where previous administrations and new administrations are handled.

#### Starting the Instrument Administrator

To start the Instrument Administrator, **click** on the launch link “ **I** **nstrument Administrator”** located on the **Mental Health Assistant** main menu. It is also possible to press the “I” key, or the return key (when “Instrument Administrator” is highlighted and underlined) to display the Instrument Administrator form. After a brief pause, the Instrument Administrator form is displayed.

**Example:** Starting the **Instrument Administrator.**

<!-- image -->

**Example:** The **Instrument Administrator** form is used to select an instrument(s) and define administration parameters.

<!-- image -->

#### Starting the Instrument Results Review Functions

To start the **Instrument Results Review** function, click on the **Instrument** **R** **esults Review** text. You can also press the “R” key or the enter key when the text is highlighted. After a brief pause the Instrument Results Review form is displayed.

**Example:** Starting the **Instrument Results Review** form.

<!-- image -->

**Example:** The **Instrument Results Review** form is used to start the Instrument Results Review functions.

<!-- image -->

#### Starting the Addiction Severity Index (ASI) Manager Function

To start the **Addiction Severity Index Manager** , **click** on the text **A** **ddiction Severity Index Manager** or press the “A” key, or press the enter key when the text is highlighted. After a brief pause, the Addiction Severity Index Manager form is displayed.

**Example:** Starting the **Addiction Severity Index Manager** form.

<!-- image -->

**Example:** The **Addiction Severity Index Manager** form.

<!-- image -->

#### File Menu

The **Mental Health Assistant** drop-down list **File menu** contains the following three menu items:

- Select Patient…
- Upload Results…
- Exit

###### Select Patient

**NOTE:** Refer to the CPRS documentation for instructions on patient selection procedures.

<!-- image -->

**Example:** From the main menu **click** on the drop-down **File menu** and **click** on the **Select Patient…** menu item. After a brief pause, the familiar CPRS patient-selection form is displayed. After selecting a different patient, both CPRS and MHA are synchronized and updated to identify the same new patient.

<!-- image -->

**Upload Results**

Clicking on the Upload Results menu item initiates the process for uploading off-line records to VistA.

**Example:** If any off-line administered records remain on this PC, the Upload Results menu item becomes enabled. If no records need to be uploaded to VistA, this menu item is visible, but disabled.

<!-- image -->

##### Exit

**Example:** To exit the **Mental Health Assistant** form and return to the Windows Desktop, **click** on **File** then **Exit** , or **click** on the **Close (X)** icon located at the top-right of the **Mental Health Assistant** form, or **press and hold** the **Alt key** then **press** the **F4 key** .

<!-- image -->

#### Tools Menu

###### METRIC Instrument Reviews…

The **METRIC Instrument Reviews** menu item is located on the MHA main menu (and most forms within MHA for easy access) drop-down **Tools** menu. The **METRIC Instrument Reviews** offers comprehensive information about all sorts of instruments, including Mental Health instruments. This menu item is offered as a courtesy and a quick way to link the METRIC website from **Mental Health Assistant** . This website is not associated in any way with **Mental Health Assistant** .

**Click** on the drop-down list **Tools** and **click** on the **METRIC Instrument Reviews…** menu item to display the METRIC website homepage.

**Example:** The **METRIC Instrument Reviews** menu item is located on the Mental Health Assistant dialog box Tools drop-down menu.

<!-- image -->

**Example:** METRIC website displayed in Internet Explorer.

<!-- image -->

**Options**

Clicking on the Tools Options menu item invokes the User Preferences form, where users can choose from different MHA system properties and behaviors. This is described in detail later in this manual.

**Changing User Preferences**

**Example:** Some system parameters are user-configurable and can be changed by **clicking** on the drop-down **Tools menu** and **Options…** menu item. The User Preferences form appears, allowing the user to make system changes, such as the default display font. The user may optionally abort changes before they are saved.

**Click**

<!-- image -->

**Example:** Mental Health Assistant **User Preferences** form.

<!-- image -->

##### Help Menu

The Mental Health Assistant Help menu contains the following two menu items:

- Online Support
- About

##### Online Support…

MHA Online Support is available via the Mental Health Informatics Section’s website. **Clicking** on the **Help menu** and **Online Support…** menu item will start the default Web browser and loads the following web address into the browser: [http://vaww.mentalhealth.va.gov](http://vaww.mentalhealth.va.gov/) . Online Support appears as a menu item in most forms used in MHA so that access is readily available.

**Example:** Accessing **Online Support.**

<!-- image -->

##### About…

The **About…** menu item contains useful release information about MHA. This menu item is available on most forms used in MHA.

**Example:** How to Access **About i** nformation. Click on **Help | About** . **Example:** The **About Mental Health Assistant** form

<!-- image -->

### New Options in VistA for Management of MHA3

On the MHS Manager Menu (YSMANAGER), new Menu option has been added to support management of the MHA application.

<!-- image -->

Select **Menu Option 7, MHA 3 Utilities** .

The menu provides the following Options for management of MHA3 utilities:

1. Print Test Form (print blank test form, also now available in MHA)
2. Detailed Definition (test description, also available in MHA)
3. Delete Patient Data (option to remove test administration from pt	file)
4. Stop/Re-Start Progress Notes for an Instrument
5. Exempt Test
6. Test Usage
7. XML Output
8. Instrument Exchange

#### Management of Progress Notes Generated by MHA

In this example, the SBR is customized to create a note using the title Suicide Behavior Report rather than the default title. This can be done for any of the instruments that pass notes to CPRS.

Additionally, the parameter can be set to not generate a note for specific instruments. Note—if the instrument is set nationally to not pass a progress note, this cannot be overridden. But, a site can elect to not create a note for an instrument that is defaulted to Yes.

Select Option 4: Stop/Re-Start PN:

Select MHA3 Utilities Option: 4 Stop/Re-Start Progress Notes for an Instrument Select MH TESTS AND SURVEYS NAME: SBR

GENERATE PNOTE: Yes//

TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// SUICIDE

1   SUICIDE BEHAVIOR REORT	TITLE

Std Title: SUICIDE RISK ASSESSMENT NOTE

CHOOSE 1-3: 1 SUICIDE BEHAVIOR REORT	TITLE Std Title: SUICIDE RISK ASSESSMENT NOTE

CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

#### Managing Time to Save an Incomplete Instrument

The national default for saving an instrument that is not finished is two days. Sites can customize this by instrument, and there may be value in setting a larger time frame for some instruments. This option is found under the Exempt Test menu option.

Please note, this option also allows for changing the status of a test from Restricted to Exempt. Please use these features with great care, as making changes to the status of tests may be in violation of copyright agreements, APA guidelines, and clinical practice standards.

&lt;MHS&gt; Select MHA3 Utilities Option:

1. Print Test Form
2. Detailed Definition
3. Delete Patient Data
4. Stop/Re-Start Progress Notes for an Instrument
5. Exempt Test
6. Test Usage
7. XML Output
8. Instrument Exchange

&lt;MHS&gt; Select MHA3 Utilities Option: 5 Exempt Test

*** Exempt Test ***

**Caution:** changing the exempt level of a published test may break copyright agreements. Changes to national tests are at the risk of the changing facility.

Select MH TESTS AND SURVEYS NAME: AUDC

1. AUDC
2. AUDCR

CHOOSE 1-2: 1 AUDC A PRIVILEGE:

R PRIVILEGE:

DAYS TO RESTART: 2//7

#### Removing Patient Data that was Entered in Error

There are two methods to remove the data from an instrument’s administration. The first uses the MHS Manager Functions in VistA and the second is available in MHA’s **Instrument Review Results** form, described previously. In either case, this function can be performed only by individuals who have access to the MHS Manager Functions in VistA, usually a Clinical Application Coordinator (CAC).

**IMPORTANT:** Data removed by either method will only remove the results of the administration of the instrument. Any progress notes, or consult notes, etc., will not be removed.

The process for using the VistA menu options is listed below:

<!-- image -->

*** MENTAL HEALTH *** MHS MANAGER FUNCTIONS

1. Inpatient Features management functions...
2. Mental Health System site parameters...
3. MHA2 Psych test utilities...
4. Move crisis notes and messages
5. Seclusion/Restraint Management Utilities...
6. Decision Tree Shell
7. MHA3 Utilities...

Select MHS Manager Option: 7 MHA3 Utilities

*** Mental Health *** MHA3 Utilities

1. Print Test Form
2. Detailed Definition
3. Delete Patient Data
4. Stop/Re-Start Progress Notes for an Instrument
5. Exempt Test
6. Test Usage
7. XML Output
8. Instrument Exchange

Select MHA3 Utilities Option: 3 Delete Patient Data

<!-- image -->

Delete Patient Data

Select PATIENT NAME:	MHPATIENT,ONE

Delete MHA3 data? No// YES

PHQ-2 on JAN 07, 2009@09:56:27 by MHPROVIDER,ONE

Delete? No// YES

Are you sure? No// YES ***Deleted

AUDC on NOV 26, 2008@14:28 by MHPROVIDER,ONE

Delete? No// ^

#### Instrument Exchange Utility

Patch 121 adds a capability to add and update instruments. This utility is available to those who manage the MHA application. An overview of the Instrument Exchange utility is available in Appendix G. Should sites need to use the utility to install an instrument, complete instructions specific to that instrument will be provided at the time.

### Instrument Administrator Functions

#### Orientation

The **Instrument Administrator** functions allow the user to order new instrument(s) to administer to the selected patient and specify the data entry mode for the instruments. First, the user **must** specify the name of the user who is ordering the instrument to be administered. By default, the user requesting the test to be ordered is identified as the session user. Another user may be specified as the user ordering the instrument, in which case, the name of the original user that requested the test is notified by VistA E-mail that tests were administered in his/her name. The available set of instruments that can be ordered depends on the user access privileges (for example, whether the user ordering the instrument has the YSP key assigned).

**Example:** Mental Health Assistant **Instrument Administrator** form.

<!-- image -->

#### Main Menu

The **Main Menu** offers user functions in the context of the **Instrument Administrator Form** , such as selecting another patient and help.

##### Selected Patient Identification label

The Selected Patient Identification label displays information about who is the currently-selected patient within MHA. All functions performed in the Instrument Administrator will apply to this patient. This patient is the same as the one selected in CPRS and should remain synchronized with CPRS even when another patient is selected.

##### Title bar

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. The left-pointing arrow, when clicked, will return the user to the Main Menu.

##### Visit information

The Visit information group of data-entry controls is used to describe the clinical particulars of a patient’s visit, such as the clinician’s name and the location of the visit and consult to associate the report of results (optional).

##### List filters

The list filters are used to change the number and types of instruments displayed in the Instruments and Batteries list.

##### Available Instruments and Batteries list

The Available Instruments and Batteries list is used to select which instruments will be administered. In some cases there will only be one instrument selected. The Available Instruments and Batteries list also allows for selecting multiple instruments or batteries, or a combination of both.

##### Instruments Chosen list

The Instruments Chosen list is the collection of instruments selected in the Instruments and Batteries list. The instruments are listed here in the order in which they will be administered—from top to bottom.

##### Re-sequencing buttons

The re-sequencing buttons are used to alter the order in which the instruments in the Instruments Chosen list will be administered. Instruments can also be removed from the list.

##### Data-entry mode selection

There are several combinations of data-entry display modes which are selected using the data-entry mode selection buttons.

##### Context-sensitive help

Context-sensitive help tips are displayed in this area and are dependent on where the mouse pointer is resting.

#### Ordering Instruments

###### Instruments can be ordered in three ways:

1. An existing test battery may be selected.

1. An incomplete administration may be restarted if it has not been too long since it was first started. The MMPI2, for example, must be completed within 24 hours; some instruments do not have time limits. Most instruments have a two-day time limit for completion. If the time period has lapsed, the incomplete administration will not be listed.

1. New instruments may be selected individually and their order of administration specified.

###### The Instrument Administrator permits the user to select one of two data-entry Modes:

1. Staff entry, which is optimized for staff data entry when the staff person wishes to see test questions and answers while entering data. This is unsuited for patient entry.

1. Patient entry, which is optimized for on-line administration of instruments to a patient.

**NOTE:** Patient entry invokes special security measures to prevent patients from using the workstation for any other purpose than answering questions. Because security measures are not invoked for the staff entry modes it must not be used for the on-line self-administration of tests to patients. (See Appendix D for more information on SecureDesktop.)

<!-- image -->

#### Selecting a Person (other than yourself) for “Instruments Ordered By”

By default, the current user’s name is selected. It is necessary to select a different name only if the user is not the same person ordering the tests. To select a new person:

1. **Click** on the **drop-down list box** labeled “ **Instruments Ordered By.”**
2. From that list of staff members, select the name of the person ordering the tests.

**Example:** The **Instrument Ordered By** person will receive an email notification in VistA regarding the administration and also appears as the **Instrument Ordered By** person in all reports related to this administration.

<!-- image -->

#### Selecting a Person for “Interviewer”

By default, the current user’s name is selected. It is necessary to select a different name only if the user is not the same person as the interviewer. To select a new person:

1. Click on the Drop-Down List Box labeled **Interviewer**
2. Select a name from the list

**Example:** The selected name also appears as the “Interviewer”, or “Printer” person in all reports related to the administration.

<!-- image -->

#### Selecting a Date of Administration

By default, today’s day is presented in the date field. It is necessary to select a different date only if the date of administration is not the same as the current date. Future dates are not allowed. To select a new date:

1. Click on the Date-Picker labeled **Date of Administration.**
2. Select the administration date from the calendar, or type in the desired date.

**Example:** The selected date also appears as the date in all reports related to this administration.

<!-- image -->

#### Selecting a Visit Location

By default, the previously-selected Visit Location is selected. It is necessary to select a different location only if the location is different from the one displayed. To select a new location:

1. Click on the Drop-Down List Box labeled **Visit Location**
2. Select a different location from the list.

**Example:** The selected location also appears as the location in all reports related to this administration.

<!-- image -->

#### Selecting a Consult (Optional)

The report of the results for the administration of an instrument can be linked to a consult instead of a progress note (as will typically happen).

1. Click on the Drop-Down List Box labeled **Link with Consult**
2. Select a consult from the list (if there are no consults, the list will be blank).

**Example:** The reports related to this administration will be associated with the selected consult.

<!-- image -->

##### Filtering the display of Available Instruments and Batteries List

Which tests appear in the Available Instruments and Batteries list box depends on the user’s access privileges to order tests (i.e., user must hold the YSP security key to be able to order selected instruments). By default, the list of Available Instruments and Batteries displays all instruments and batteries that the user identified as the Ordered By user has permission to administer. However, the list of Available Instruments and Batteries can be filtered in three different ways:

1. All instruments and batteries, in alphabetical order.
2. Batteries only.
3. Restartable instruments only (incomplete administrations which may be resumed, if there are any).

###### To change the lists filter:

1. Click on the Drop-Down List Box labeled Show
2. Select a filter for the list of available instruments.

**Example:** The displayed Instrument List changes to include only the instruments that meet the new filter’s specification.

<!-- image -->

#### Choosing One or More Instruments

By default, nothing is selected on the list of Available Instruments and Batteries. The user must choose one or more instruments to administer during this session. In the case where there are multiple instruments that are administered frequently, the user has an option to create and select instrument battery, which simplifies selecting a group of instruments. The user may select any combination of single instruments and batteries.

To select instruments or batteries, **click** on the check box next to the **Available Instruments and Batteries** list box names found on the **Instrument List** .

**Example:** The **Available Instruments and Batteries** list box.

<!-- image -->

The selected instruments appear in the list of **Instruments Chosen** . These are the instruments selected for administration.

**NOTE:** Instruments are added to the Instruments Chosen list in the order in which they were selected in the Instrument List. This is the same sequence in which the tests will be administered unless the order is changed. The date and time of administration is appended at the end of an incomplete test name.

<!-- image -->

#### Restarting Incomplete Administrations

Whether an incomplete administration of an instrument can be restarted depends on how long ago it was first entered in MHA. The permissible lapse is a local site parameter. It is set using MHS Manager\Psych Test Utilities\Edit Instrument Restart Limit [YSINST RESTART LIMIT] option.

Usually the lapse is two days. Restarting an incomplete administration from the **Instruments Chosen** list box is no different from starting a new test, so that process is not described here. The items that were answered in the first administration are carried over to the next one.

#### Manipulate the list of Instruments Chosen

After two or more instruments are added to the **Instruments Chosen** list, it is possible to rearrange the order in which they will be administered. The re-sequencing buttons may be used to change the order of the instruments in the list, or to remove instruments from the list. The order of administration is always from top to bottom.

To change the order, select the instrument item in the **Instruments Chosen** list. Using the re- sequencing buttons:

- **Click** on the up-arrow button to move the instrument up the list.
- **Click** on the down-arrow button to move the instrument down the list.
- **Click** on the left-arrow button to remove the instrument from the list.

**Example:** The **Instruments Chosen** list box.

<!-- image -->

#### Selecting Display Mode for Data Entry

There are two display modes in MHA: “Display One Question at a Time,” or display “All Questions at Once.”

The **One Question at a Time** display mode is ideal for patient-entry, since it only displays one question in the data-entry form. This allows for a more focused and relaxed approach to responding to questions.

The **All Questions at Once** display mode is ideal for staff-entry, since it displays all the questions in a scrollable window. This allows for rapid navigation between questions, and a faster approach to entering data. It may also be suited for some patients.

In MHA, either **One Question at a Time** or **All Questions at Once** may be used for patient-entry or staff-entry modes. It is a user preference choice.

- To select **One Question at a Time** display mode, click on the **One Question at a Time**

option button.

- To select **All Questions at Once** display mode, click on the **All Questions at Once**

option button.

- At least one test **must** be available in **Instruments Chosen.**

**Example:** Display mode selection.

<!-- image -->

#### Selecting “Patient Entry” Data-Entry Mode

Patient-entry mode supports the on-line testing of patients. **Patient Entry** has added security features to prevent unattended patients from using the workstation for unauthorized purposes. Clicking on the **Patient Entry** command button triggers the activation of the SecureDesktop security functionality.

To start patient entry mode:

1. **Click** on the **Patient Entry** button
2. **Click** on **Yes** in response to the first warning prompt. Click on **No** , to abort invoking SecureDesktop and cancelling patient entry.
3. **Click** on **OK** to respond to the second warning prompt

###### Additional notes about Patient-Entry mode:

- At least one test must be available in the **Instruments Chosen** list **.**
- If the **Patient Entry** button is disabled, this means that the SecureDesktop software is not properly installed on this PC – contact your local IRM for support, if needed.
- Any time Patient Entry mode is invoked, two warning messages are displayed. These messages are an indication that SecureDesktop is about to be activated.
- The **Single-Question** form or the **All-Questions** form is displayed, depending on which option button was selected.
- **Note** : When using Secure Desktop for Patient Entered mode of an MHA test administration, appropriate monitoring is needed. Veterans need to be able to request assistance while completing assessments, and staff should be available to quickly address any technical or clinical issues that may arise.
- Appendix D has further details about the operation of SecureDesktop.

**Example: Patient Entry** button.

<!-- image -->

**Example:** SecureDesktop **WARNING** prompt #1.

<!-- image -->

**Example:** SecureDesktop **WARNING** prompt #2.

<!-- image -->

#### Selecting “Staff Entry” Data-Entry Mode

1. **Click** on the **Staff Entry** button.

###### Additional notes about Staff-Entry mode:

- At least one test must be available in the **Instruments Chosen** list **.**
- Staff-entry mode does not make use of the SecureDesktop functionality, since it is intended for staff use only, not for patients.
- The **Single-Question** form or the **All-Questions** form is displayed, depending on which option button was selected

**Example:** The **Staff Entry** button.

<!-- image -->

#### On-form Instructions

**Example:** The **On-form Instructions** are displayed in the bottom-left corner of the Instrument Administrator form. These are context-sensitive tips that change depending upon which part of the form the mouse pointer is resting on. Not all elements of the form trigger instructions.

<!-- image -->

#### Printing a Blank Instrument

Sometimes it is useful to provide a pencil-and-paper version of an instrument to a patient that they can fill out themselves, in the waiting room, for example. Later the patient’s responses can be entered into MHA by a clerk or clinician.

By opening the **File** menu, and clicking on the option, “ **Print a blank instrument** ,” the user can select an instrument, and define the printer and its settings. The operation of the print function is very standard and familiar to Windows users. The blank form will always have a heading which contains empty lines to gather identifying information on the patient, date, location and staff member. Information on the selected patient will not be printed on the blank form.

**Example:** To print a blank instrument:

<!-- image -->

The Print Assistant provides the means to select the instrument to be printed, to change the font and size of the font, and make adjustments to the printer.

**Example:** The Print Assistant.

<!-- image -->

**Example:** To view the instruments that can be printed, click on the down arrow in the combo box. Select the instrument by clicking on it. Once the instrument is selected, click on the **Print** button to start printing, or the **Set Printer** button to configure the printer.

<!-- image -->

**Example:** This window appears when the **Set Printer** button is clicked.

<!-- image -->

**Example:** To start printing, select the mapped name of the local printer and click on the **OK**

button.

**Select printer from list**

<!-- image -->

Exiting the Instrument Administrator Form

**Example:** To exit from the I **nstrument Administrator** form, **click** on the **File | Exit** menu item. Alternatively, you can click on the “X” in the upper right-hand corner of the window, or press the “ESC” key, or click on the left arrow. The I **nstrument Administrator** form will close and the user is returned to the Mental Health Assistant main menu.

<!-- image -->

#### Reviewing a Description of the Selected Instrument

The clinical and technical features of any particular instrument supported by MHA can be reviewed by clicking on the instrument name followed by clicking on **Help | Instrument Description…** You can right-click on the instrument to perform the same operation.

**Example:** How to view information about an instrument.

<!-- image -->

**Example:** Description of an instrument.

<!-- image -->

#### Instrument Administrator’s Battery Wizard Orientation

The Instrument Administrator’s **Battery Wizard** is a tool for creating and maintaining persistent, re-

usable instrument batteries. User-defined batteries that are created using the **Battery Wizard** are listed in the **Available Instruments and Batteries** list box. When the instruments in a battery are added to the **Instruments Chosen** list, the names of the instruments contained in the battery are listed in **Instruments Chosen** , not the name of the battery.

Creating reusable batteries from frequently administered sets of instruments can reduce the time required to set up a testing session for patients with similar testing needs.

**Example:** The **Battery Wizard** form **.**

<!-- image -->

#### Main Menu

The Main Menu offers user functions in the context of the Battery Wizard, such as additional tools and help.

#### Title bar

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity.

#### Available Instruments and Batteries list

The Available Instruments and Batteries list is used to select which instruments will be administered. In some cases there will only be one instrument selected. This list also allows for selecting multiple instruments or batteries, or a combination of both.

#### Instruments in Battery list

The Instruments in Battery list is the collection of instruments selected to become part of the current battery. The instruments are listed here in the order in which they will be administered—from top to bottom.

#### Re-sequencing buttons

The re-sequencing buttons are used to alter the order in which the instruments in the Battery will be listed in the Instruments Chosen list. Instruments can be removed from the battery also.

#### Context-sensitive Help

Context-sensitive help tips are displayed in this area and are dependent on where the mouse pointer is resting.

#### Battery Selector

The Battery Selector Drop-Down Combo Box is used to type in the name of a new battery, or to select from a list of existing batteries. The battery name indicated here is the currently-selected battery to which all editing actions apply.

#### Save Button

The Save button is used to save to VistA all changes made to the current battery. After a battery is saved, its name will be listed in the list of Available Instruments and Batteries on the Instrument Administrator form.

#### Invoking the Battery Wizard

The Battery Wizard **must** be invoked from the **Instrument Administrator** form. Similarly, all consequences of editing batteries are reflected in the Instrument Administrator, upon closing the **Battery Wizard** form.

**Example:** To start the **Battery Wizard** , **click** on **Tools** | **Battery Wizard** … located on the

###### Instrument Administrator’s Tools menu.

<!-- image -->

**Example:** Mental Health Assistant **Battery Wizard** form.

<!-- image -->

#### Battery Wizard: Creating a New User-defined Battery

New batteries of instruments are created by first assigning a name to the new battery. Next, instruments (and other batteries) are added to the Instruments in Battery list by clicking on the desired instrument names shown in the **Available Instruments and Batteries** list box.

The **Instruments in Battery** list box can be manipulated to change the order of the tests and to add or remove tests. To modify the **Instruments in Battery** list of an existing battery, simply load the battery by selecting the battery name using the Name of Battery Drop-Down Combo Box.

###### Here is an example of creating a new battery:

1. Click on **File | New** menu item.
2. Enter the name “ **Screen Battery”** in the **Name of Battery** box.
3. Select **AUDC** and **PC-PTSD** instruments by clicking on the selection box next to their names.
4. Click on the **Save** button.
5. The new battery is saved after the **Save** button is pressed.
6. The **Battery Wizard** form is closed.
7. The **Instrument Administrator** form is shown and the newly-created battery appears in the list of **Available Instruments and Batteries** .
8. When **Screen Battery** is selected, the two instruments included in the battery are added to the **Instruments Chosen** list on the **Instrument Administrator** form.

**Example:** This is a display of creating a new battery from the **Name of Battery** box.

<!-- image -->

**Example:** The created battery is displayed and is available from the **Instrument Administrator** form under the **Available Instruments and Batteries** list. The two instruments included in the battery are displayed in the **Instruments Chosen** list box.

<!-- image -->

#### Renaming an Existing Battery

1. Go to Battery Wizard
2. Click on **File | Rename** menu item.
3. Select the battery that you wish to rename from the **Available Instruments and Batteries list** .
4. Type the new name for the battery
5. **Click** Ok.

**Example:** Open the **File | Rename** menu.

<!-- image -->

**Example:** Typing in a new name for an existing battery.

<!-- image -->

Once the **OK** button is pressed, the Battery Wizard can be closed (use the “exit” selection in the “File” menu, or click on the “X” in the upper right hand corner of the window, or press the escape key “ESC”). The battery’s new name will appear in the “Instrument Administrator” window.

**Example:** Displaying the **New Name** from the **Available Instruments and Batteries** list box.

<!-- image -->

Deleting an Existing Battery

1. Go to the Battery Wizard
2. Click on **File | Delete** menu item.
3. Select the battery to be deleted from the **Available Instruments and Batteries** list box.
4. Click on **Yes** .
5. The selected battery is deleted from VistA and from the list of **Available Instruments and Batteries** .

**Example:** Deleting an existing battery.

<!-- image -->

**Example: Click** on **File | Delete** menu item. Click on the **OK** button.

<!-- image -->

#### Exiting the Battery Wizard

To exit the **Battery Wizard** form and return to the **Instrument Administrator** form **click** on the drop-down **File | Exit** menu item. You can also press the “ESC” key, or click on the “X” in the upper right-hand corner of the form, or click on the left arrow. The **Battery Wizard** form will close and the user is returned to the **Instrument Administrator** form.

**Example:** Exit the Battery Wizard.

<!-- image -->

### Instrument Administrator’s “One Question at a Time” Input Form

#### Orientation

The **“One Question at a Time”** data-entry form enables the user to answer questions by viewing and responding to one question at a time. This display mode is ideal for patient-entry, since it only displays one question in the data entry form. This allows for a more focused and relaxed approach to responding to questions. This mode is also suitable for staff entry as well. It boils down to a matter of personal preference.

This section lists, in detail, all the various types of visual artifacts that users are likely to interface with while responding to questions during an administration.

Refer to the glossary for a description of the visual elements on these forms, and how they are normally used.

**Example:** Single-question **data-entry** form.

<!-- image -->

#### The Main Menu

The Main Menu offers user functions in the context of the Single-Question form, such as tools and help.

#### The Selected Patient Identification Label

The **Selected Patient Identification** label displays information about who is the currently selected patient within MHA. All functions performed in the **Single-Question** form will apply to this patient.

#### The Instrument’s Name

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. In this case, the Title Bar displays the current instrument’s name.

#### The Introduction Text

Introduction Text is used as narrative introduction to one or more questions. Generally, introductions present instructions on how to respond to questions.

#### The Question Text

The Question Text is the actual question presented to the user.

#### The Response Artifact

A Response Artifact is a visual control that the user will use to respond to the presented question. There are a number of different types of Response Artifacts in MHA, such as Drop-Down Combo Boxes, Text Boxes, Spin Edits and such. On the Single-question form, all response artifacts are displayed on the same area of the form.

#### The Navigation Buttons

The Navigation Buttons are used to display Previous and Next Questions. They are used to navigate through the sequence of all questions contained in the instrument.

#### The Progress Indicator

The Progress Indicator displays the current percentage of questions answered so far, represented by the number of questions answered, compared to the total number of questions in the instrument. If the progress bar is red, it indicates that a question was skipped; when green, all the questions so far have been answered.

#### The Review Answers Form

The Review Answers form is a navigational aid to use with instruments that contain a large number of questions. It presents a simple way to select a question for editing that is not contiguous to the present question.

#### Responding to a Multi-choice Question Using a Multiple-Selection List Box

Multiple-Selection List Boxes allow the user to select one or more of the choices listed. To respond to a question:

1. Select one or more choices from the Multiple-Selection List Box on the form by clicking on the item, or, use the arrow keys to move to the desired item and press the space bar.
2. To go to the next question, click on **Next Question** button, or, press the “Enter” key.

The choices made are recorded and the next question is automatically displayed.

**Example:** Selecting two choices.

<!-- image -->

#### Responding to a Single-choice Question Using a Drop-Down List Box

**NOTE:** Drop-Down List Boxes allow selection of a single choice from a list. This type of question is also called a “combo box.”

<!-- image -->

###### To respond to a question:

1. **Click** on the down-arrow located on the drop-down list box to display the list, or, use the arrow keys to step through the sequence of items.
2. Select a program type from the list by clicking on the item, or, when the desired item is presented in the box, press the “Tab or “Enter” key to select the item. It is also possible to type the number of the item’s designator (“1,” “2,” etc) if they are used.
3. To proceed, click on the **Next Question** button, or press the “Enter” key. Alternately, you can also press the “Tab” key until the **Next Question** button is active, then press the “Enter” key.

**Example:** Data Input form displaying a drop-down list box.

**1. Click**

**2. Click**

<!-- image -->

#### Responding to a Question that Asks for a Currency Amount using a Text Box

Some Text Box artifacts are configured to only accept valid currency values.

###### To respond to a question:

1. Type a currency value in the Text Box
2. Click on **Next Question** button, or press the “Enter” key.

The entered currency value is recorded and the next question is automatically displayed.

**Example:** Entering a currency amount.

**1. Type in a valid currency amount**

**2. Click**

<!-- image -->

#### Responding to a Question that Asks for a Date Using a Date-Picker

Date-Pickers are used to respond to questions requiring a date for an answer. A Date-Picker displays a calendar from which a date is selected. Alternatively, the user may simply type the date in the Text Box portion of the Date-Picker artifact. In MHA, Date-Pickers usually don’t allow for selecting a date in the future. To select a date:

1. Click on the button with the arrow-head to open the Date-Picker calendar component; alternately, you can type the date directly into the date box and skip the next step.
2. Navigate to the desired date and click on its number symbol.
3. Click on **Next Question** button, or, press the “Enter” key.

The selected date value is recorded and the next question is automatically displayed.

**Example:** Selecting a date.

**1. Click to open calendar**

**2. Click on a date**

**3. Click**

<!-- image -->

#### Responding to a Question that Asks for a Line of Text using a Text Box

A Text Box allows entry of a single line of text as a response to a question.

###### To answer a question:

1. Type a line of text in the Text Box.
2. Click on **Next Question** button, or, press the “Enter” key.

The entered text is recorded and the next question is automatically displayed. A Text Box accepts any type of text.

**Example:** Entering text into a Text Box.

<!-- image -->

#### Responding To A Question From A List Of Answers Using A Single- Selection List Box

A Single-Selection List Box is very similar to a Combo Box, except that all available responses are readily visible. There is no drop-down list to trigger. To answer a question:

1. Select one item from the Single-Selection List Box by clicking on it, or use the arrow keys to move to desired item then press the “Tab” or “Enter” key.
2. Click on **Next Question** button, or, press the “Enter” key.

Alternately, if the “Speed Tab” is checked, you can press the number key that corresponds to the item’s designator. That key press will do two functions; it will select that item and display the next question.

The single choice made is recorded and the next question is automatically displayed.

**Example:** Selecting a single response.

**1. Click**

**2. Click**

<!-- image -->

#### Responding To A Question Using A Masked Text Box That Pre- Formats Input Data

Masked Text Boxes automatically format the data entered into them. For instance, a Masked Text Box configured to accept a phone number, or Social Security Number, will automatically position and display the parenthesis and dashes normally found in fully-formed phone numbers or SSN. All that the user must type are the numbers. The rest of the formatting is done automatically.

###### Enter a Social Security Number:

1. Type only the numbers in a SSN in the Masked Text Box.
2. Click on **Next Question** button, or, press the “Enter” key.

**Example:** The Masked Text Box adds formatting to the entered numbers to reflect a standard SSN notation. Only numbers are accepted for input.

<!-- image -->

#### Responding To A Question That Asks For A Long Textual Answer Using A Multiple-Line Text Box

Multiple-Line Text Boxes accept more than one line of text.

###### To answer a question:

1. Type several lines of text in the Multiple-Line Text Box
2. Click on **Next Question** button, or, press the “Enter” key.

**Example:** The entered text is recorded and the next question is automatically displayed. The Multiple-Line Text Box accepts any type of text.

<!-- image -->

#### Respond To A Question Using A Spin Box That Asks For An Integer Value

Spin Boxes are used to select from a list of consecutive integer values. Additionally, an integer value may be typed into the Text Box area of a Spin Box artifact. To answer a question:

1. Type an integer, or use the spin buttons with the arrowheads to enter a value in the Spin Box.
2. Click on **Next Question** button, or, press the “Enter” key.

The entered integer value is recorded and the next question is automatically displayed. The Spin Box only accepts integer values.

**Example:** Entering an integer value.

<!-- image -->

#### Responding To A Question That Asks For A Single Choice From A List Using Option Buttons

Option Buttons are used to answer questions from a list of mutually-exclusive answers. This is also called a radio group. To answer a question:

1. Click on one of the Option Buttons in the group, or, use the arrow keys to move to the desired option and press the “Tab” or “Enter” key to select the option.
2. Click on **Next Question** button, or, press the “Enter” key.

Alternately, if the “Speed Tab” is checked, you can press the number key that corresponds to the item’s designator. That key press will do two functions; it will select that item and display the next question.

The single choice made is recorded and the next question is automatically displayed.

**Example:** Selecting an Option Button (Radio Group) response.

<!-- image -->

#### Responding To A Question That Asks For A Staff Name From Vista Using A Drop-Down List Box

Staff list Drop-Down List Boxes are special list boxes that display a list of staff members from VistA.

###### To select a staff member:

1. Begin typing the first three letters of the last name in the Text Box part of the component.
2. If the complete name is not automatically filled in, select the name from the list of names that “dropped down” in the VistA Drop-Down List Box
3. Click on **Next Question** button, or, press the “Enter” key.

The name choice made is recorded and the next question is automatically displayed.

**Example: S** electing a staff name from a list.

<!-- image -->

#### Responding To A Question That Asks For A Value From A Slider

Sliders simplify visually selecting a value from a range of values. These are sometimes called track bars.

###### To answer a question:

1. **Select** a value on the Slider by moving the choice indicator on the scale to the number of your choice. You can also press the number key for the desired value.
2. Click on **Next Question** button, or, press the “Enter” key.

**Example:** Selecting a point on a scale. The selected Slider value is recorded and the next question is automatically displayed.

<!-- image -->

#### Identifying The End Point Of An Instrument And Finishing The Instrument

The last question in an instrument will trigger a change in the displayed navigational buttons. The **Prior Question** buttons remain enabled and a dialog box will be displayed. Clicking on the **Finish** button will finish the test.

###### To finish a test:

1. Answer every question in the instrument (the progress bar will be green).
2. On the last question, click on the F **inish** button.

**Example:** Finishing an instrument. Since this is the last question, the Information dialog is presented. Click on **OK** and then the **Finish** button.

<!-- image -->

Once the data is saved to VistA, the user is given the choice of 1) saving a standard progress note to VistA that summarizes the data and its score(s), 2) Editing the standard note before saving it and 3) not saving a progress note. See Appendix B for cases where a co-signer is required for signing a progress note.

**Example:** Save a progress note query.

<!-- image -->

#### Incomplete Data-Entry Session

1. Click on the **Finish** button.
2. Click on the **YES** button of the “Confirm” dialog. The Confirm dialog will list the questions that have not been answered and will inform the user of the permitted delay to finish the administration. The Confirm dialog will also allow the user to return to the instrument.

<!-- image -->

**Example:** When the **Finish** button is clicked, the confirm dialog is displayed. Click **Yes** to save the administration as “incomplete.”

**2. Click**

**1. Click**

#### Viewing the Next Instrument

Within the context of a series of instruments, it is possible to jump to different instruments.

**Example:** Jumping to the next instrument. Click on the tab of the desired instrument. The responses are not lost on the current administration when you return.

**Click**

<!-- image -->

#### Viewing the Prior Question

To view the question that is prior in order to the currently-selected question, click on the **Prior Question** button.

**Example:** The displayed question becomes the prior question within the current instrument.

**Click**

<!-- image -->

#### View Next Question

To view the question that is next in order to the currently-selected question, **click** on the **Next Question** button.

**Example:** The displayed question becomes the next question within the current instrument.

**Click**

<!-- image -->

#### Review Answers

In the case where navigating through the questions in an instrument using the **Next Question** and **Prior Question** buttons is too cumbersome due to a large number of questions, the **Review Answers** offers a quicker way to move around. To start the Review Answers form, **click** on the **Review Answers** button.

**Example:** Starting the Review Answers form.

**Click**

<!-- image -->

##### Changing Answers

To change a given answer, it is first necessary to return to that answer. There are two ways to navigate back to a previously-answered question: the question navigation buttons or the **Review Answers** form. Once the answer is again displayed in the form, simply choose or type in a different answer.

###### To change an answer using the Review Answers form:

1. Click on any of the previously-answered questions listed in the table, to select the question.
2. Click on the **Change Answer** button.

To return to the Single-Question input form, without making any changes, **click** on the **Exit** button, or press the escape key “ESC”, or the **FILE | Exit** .

###### After clicking on the Change Answer button:

1. The Single-Question input form is displayed and the selected question is shown with the previously-entered response.
2. User can change the response to this question.

**Example:** Selecting a question to change.

**1. Click**

**2. Click**

<!-- image -->

#### Exiting Data-Entry Session without Saving the Answers

**Example:** To abort saving any of the given answers to an administration, **click** on the **Cancel** button. The editing session ends and no answers are saved.

<!-- image -->

#### Instrument Administrator’s “All Questions At Once” Input Form

**Orientation**

The “ **All Questions at Once”** data-entry form allows the user to answer questions by viewing and responding to any or all of the instrument questions at any time. All questions are displayed at once on a scrollable form, much like a pencil-and-paper version of the instrument. The “ **All Questions at Once”** data-entry form does not make use of a Review Answers form, or navigation buttons, since they would be redundant with the functions already offered by this form.

**NOTE:** The previous section described the visual elements used in MHA and will not be repeated here.

<!-- image -->

**Example: “All-questions at once”** data entry form.

<!-- image -->

#### Main Menu

The Mental Health Assistant Main Menu offers user functions in the context of the All Questions at Once form, such as tools and help.

#### Selected Patient Identification Label

The Selected Patient Identification label displays information about who is the currently-selected patient within MHA.

#### Instrument’s Name

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. In this case, the Title Bar displays the current instrument’s name.

#### Section Text

Sometimes, instrument designers may group questions into sections. In this case, existing section titles are displayed in the form, just above any introduction or question text.

#### Introduction Text

The Introduction Text is used as narrative introduction to one or more questions. Generally, introductions present instructions on how to respond to questions.

#### Question Text

The Question Text is the actual question presented to the user.

#### Response Artifact

A Response Artifact is a visual control that the user will use to respond to the presented question. There are a number of different types of Response Artifacts in MHA, such as Drop-Down Combo Boxes, Text Boxes, Spin Edits and such.

#### Navigation Scroll Bar

The Navigation Scroll Bar is used to display any questions on the form which may be hidden below or above the current view.

#### Instrument Tabs

When the user is responding to a series of instruments, each individual instrument is indicated as a tab at the bottom of the form. These tabs are used to navigate among the different instruments in the series.

#### Navigation

The data-entry visual artifacts on this form respond in the same way that they do on the Single- Question form, the difference being that all questions are presented at once and that navigation to the different questions is done differently.

To navigate using the mouse, simply use the scroll bar until the desired question is within view. To navigate using the keyboard, use the **Tab** key to jump to the next question in the sequence. **Shift-Tab** causes a reverse jump to the previous question in the sequence.

Additionally, to automate the tabbing effect, there is the **Speed Tab** option that automatically tabs to the next question once a question is answered. However, the **Speed Tab** option has no effect on Multiple-Line Text Boxes, Single-Line Text Boxes, Date-Pick boxes and Spin Boxes.

###### While answering questions:

1. All questions pertaining to the current instrument are available on the current form.
2. The scroll bar permits navigation to all the instrument’s questions on the form.
3. Using the Tab key for navigation performs as described above.
4. All data-entry visual artifacts respond in the same way as they do on the Single-Question form.
5. After saving the administration, the answers given will match the ones listed in the Instrument Results Review report.

#### Finish button

An instrument administration is finished once all questions have been answered. To end an Instrument Administration:

1. Answer every question in the instrument (the progress bar will be green).
2. **Click** on the **Finish** button.
3. If a question has not been answered (the progress bar will be red), a warning message is displayed and the user can either return to the form, or save the instrument as incomplete .
4. All responses are saved to VistA.
5. The instrument saved message is displayed and user is returned to the MHA main menu.

**Example: AUDIT** instrument is saved by clicking on the **Finish** button.

**Click**

<!-- image -->

Once the answers are saved, the user is given the three options below concerning the progress note. See Appendix B for cases where a co-signer is required for signing a progress note.

**Example:** Progress Note dialog.

<!-- image -->

#### Selecting an Instrument within a Series

The instruments are listed in the tabs at the bottom of the form. These tabs are used to navigate to any of these instruments.

###### To change the current instrument:

1. If the desired instrument tab is not the selected tab (in the foreground) **click** on the tab to bring the instrument to the foreground. **Or** …
2. Use the **View** menu option, **click** on the instrument’s name in the View list.

**Example:** Selecting a different instrument.

<!-- image -->

#### To Review Answers Given:

**Example:** Use the scroll bar to review every answer given. Moving the scroll bar permits all questions and answers to be viewed.

<!-- image -->

#### Change a Previously-given Answer

To change a previously-given answer, navigate to the question and change the answer.

**Example:** Question #7 with answer changed to the second item.

<!-- image -->

#### Suspend Responding To Questions And Save The Administration In An Incomplete State

To suspend responding to questions, **click** on the **Finish** button.

1. The “All questions at once” data-entry form closes and the user is returned to the **Instrument Administrator** form
2. The instrument administration is automatically saved as an incomplete administration in VistA. No data is lost.
3. The instrument appears in the list of available instruments as an incomplete administration, which can be selected for resumption.

**Example: BOMC** saved as an incomplete administration **.**

**Click**

<!-- image -->

**Example:** Warning given upon exiting an incomplete administration.

<!-- image -->

#### Exiting Data-Entry Session without Saving the Answers

To abort saving any of the given answers to an administration, **click** on the **Cancel** button. The session ends and no answers are saved.

#### Instrument Results Review Functions

**Orientation**

All previous tests completed by the selected patient are listed on the Instrument Results Review form, and one of those tests is always highlighted (by default, the first test in the list is highlighted when the user first accesses this form). A text-based report for the highlighted test is shown. If the highlighted instrument has a scale or scales, a graphical display of those scores is presented on the Graph &amp; Table tab. There is also a Special Results tab which displays graphs of results from various instruments.

**Example:** The **Instrument Results Review** form offers functions to print, save and copy-paste reports, tables and graphs, as well as enables the user to append comments to the results of the highlighted test.

<!-- image -->

**Example:** Graph and table views.

<!-- image -->

**Example:** Multi-scale instrument table and graph, in this case the MBMD. Click on the group of scales name (in this case the bold **Psychiatric Indicators** ) to see only those scales.

<!-- image -->

**Example:** If you click on one of the scales this table and graph is presented.

<!-- image -->

**Example: Special Results** view.

<!-- image -->

The Special Results Tab can be tailored by the user. Most instruments with scales can be displayed, the order of the instruments displayed can be changed by the user, and the patient’s responses can be displayed for each administration. The colors used in the Special Results tab are green (normal range), yellow (borderline range), maroon (serious range) and red (severe range). The Special Results tab, because of the extensive reliance on visual cues, is not present when a screen reader is in use.

#### Main Menu

The Main Menu offers user functions, such as tools and help.

#### Selected Patient Identification label

The Selected Patient Identification label displays information about who is the currently-selected patient within MHA.

#### Instrument’s Name

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. In this case, the Title Bar displays the current instrument’s name.

#### List of Previously-Administered Tests

This is the list of all tests that have been administered to the selected patient. The list is also used for selecting which administration to process. The list may be sorted by date or by instrument name.

#### The Navigation Tabs

These tabs are used to switch between report, graph/table and Special Results views.

##### The Reports View:

The Report View displays an administration report in textual form, based on the patient’s data stored in VistA for the selected administration.

##### The Graph and Table View:

The graph and table view displays both a table and graphical representation of test data values over time.

##### The Special Results View:

Special Results displays the results, over time, for selected instruments. Whereas the other two tabs display information on a single instrument, the Special Results view can present information on several instruments over time for the patient. The user can select the instruments displayed on the Special Results tab (see “Special Results Wizard” for instructions). This feature is not available for screen readers due to the intense visual representation of the data; the same information, however, is provided in the two previous tabs.

#### Saving a Graph, Report, or a Table to a File

To save a graph, report, or table, **click** on the drop-down **File Menu | Save As…** menu item and then **click** on Graph, Report, or Table. To save a graph or a table, the “Graph and Table” tab must be selected first.

**Example:** A message dialog appears that asks the user to enter a filename and storage location for the table, report or graph file to be saved. A graph is saved as a bitmap, a table is saved as an Excel file and a report is saved as a text file.

<!-- image -->

**Example:** Save As form

<!-- image -->

#### Printing a Graph, Report or Table.

To print a graph, report, or table, **click** on the drop-down **File Menu | Print…** menu item and then

**click** on Graph, Report, or Table menu item.

A copy of the table, report or graph is sent directly to the default printer.

**Example:** Printing a graph, report, or table.

<!-- image -->

#### Copying a Graph, Report, or Table to the Windows Clipboard.

To copy a report, graph, or table to the Windows clipboard, **click** on drop-down **Edit | Copy…** menu item and then **click** on Graph, Report, or Table. A copy of the table, report or graph is sent to the Clipboard. The contents of the Clipboard can then be pasted onto an MS Word or Excel document.

**Example:** Copying a report the Windows clipboard.

<!-- image -->

**Example:** Message displayed after copying to the clipboard

<!-- image -->

#### Switching Views in Instrument Results Review

**Example:** There are two ways to switch between views on the **Instrument Results Review** form; click on the navigation tabs at the bottom-left of the form (using the key strokes ALT-R, ALT-G or ALT-S will also work), or, open the **View** menu option and select from one of the three views.

<!-- image -->

#### Appending Comments to an Existing Record

###### Comments can be appended to existing reports in VistA:

1. Select the instrument to which to append comments
2. **Click** on the **Tools | Append comments…** menu item or right click on the highlighted administration.
3. The Comments Editor Form is displayed.
4. Type a new comment in the Comments Editor
5. **Click** on **Save and Exit** button in the Comments Editor
6. Comment appears appended to the administration’s report text

###### Example: Tools | Append Comments…item

<!-- image -->

**Example:** Right click on the desired administration to append.

<!-- image -->

**Example: Comments Editor** form displays **previous** and **new** comments.

<!-- image -->

**Example:** Save Comment and Exit.

<!-- image -->

**Example:** Comment added to a report.

<!-- image -->

#### Removing Data Entered in Error

This function can be performed only by individuals who have access to the MHS Manager Functions in VistA, usually a Clinical Application Coordinator (CAC). The removal of data entered in error can be accomplished by the traditional roll-and-scroll method in VistA, or using MHA. This section describes the latter method; see Appendix C for the VistA instructions.

**IMPORTANT:** Data removed by either method will only remove the results of the administration of the instrument. Any progress notes, consult notes, etc., will not be removed.

Select the administration of the instrument you wish to remove. The instrument’s name and the date of the administration will be highlighted, and its report will appear in the right window. In this example, notice that there are two administrations of the WHYMPI on 4/14/2011.

**Example:** An instrument’s report is to be removed.

**Administration to be deleted**

<!-- image -->

There are three ways to initiate the deletion process:

1. Select **Tools | Delete administration** from the menu.
2. Press the delete “DEL” key once an administration is highlighted.
3. Right click on the highlighted instrument, then select “Delete” from the pop-up menu.

These three methods are illustrated below.

**Example:** Use the menu option to delete an administration.

<!-- image -->

**Example:** Right click on the mouse to see the **Delete** command in the pop-up window.

<!-- image -->

Once you press the delete “DEL” key, or one of the above methods, a warning dialog will appear.

**Example:** Warning dialog for deleting an administration.

<!-- image -->

If you are sure that the deletion is proper, click on the **Yes** button. If the data are removed successfully, the following prompt will appear. In addition, the list of instruments will have been refreshed.

**Example** : Instruments results screen refreshed and the successful delete message is presented.

<!-- image -->

Notice that only one administration of the WHYMPI is listed for 4/14/2011.

#### Special Results Wizard

The Special Results tab can be modified by the user. The order of the results of instruments can be arranged by the user. Also, responses to questions for a given instrument can be displayed.

**Example:** Opening the Special Results Wizard.

<!-- image -->

**Example:** Special Results Wizard form.

<!-- image -->

The Special Results Wizard provides a simple method to add or remove the results of an instrument viewed in the Special Results tab; simply click on the instrument to toggle the check box.

**Example:** Adding the results of COWS administrations.

<!-- image -->

**Changing the order of the results**

The order of the results of the instruments can be changed using the up and down arrows. Click on the instrument’s name in the “Instruments in Special Results” so that it is highlighted, then click on the up or down arrow to move it in the list.

##### Displaying the results with or without the questions and answers

By double-clicking on the name of the instrument in the “Instruments in Special Results” window, the results of the instrument will be displayed with or without the questions and answers.

**Example:** Double-clicking on the COWS in the “Instruments in Special Results” window.

<!-- image -->

By clicking on the **Save** button the changes will be saved. To **cancel** the session with the Special Results Wizard, close the form by using the **File | Exit** menu option, or click on the left arrow, or, click on the “X” in the upper right-hand corner, or press the escape key “ESC.”

**Example:** COWS administrations are added to Special Results tab.

<!-- image -->

By clicking on the bar on the graph, the questions and answers for that date will appear below the graph. In the example above, the results from 05/01/2011 are presented.

#### Exiting the Instrument Results Review Form

To exit the Instruments Results Review form, **click** on the **File | Exit** menu item. The Instrument Results Review form will close and the user is returned to the MHA Main form. Alternately, you can press the “ESC” key, or click on the “X” in the upper right-hand corner of the form, or click on the left arrow.

**Example:** Exiting the **Instruments Results Review** form.

<!-- image -->

Addiction Severity Index Manager Functions

#### Orientation

The ASI Manager lists all previous interviews and makes it easy to view either the item report or narrative report for a selected interview.

Additional views of ASI data are provided. Both the **Domain Scores** and **Item Trends** functions present graphical and tabular data across multiple interviews. The Domain Scores option gives the user the opportunity to see either problem severity ratings or evaluation factor scores (see Alterman, et al., [1998] "New scales to assess change in the Addiction Severity Index for the opioid, cocaine, and alcohol dependent", *Psychology of Addictive Behavior,* 12, 233-246). The **Item Trends** option displays responses to selected individual items. It is hoped that these data views will help with treatment planning and treatment outcome monitoring.

A user-friendly interface for entering interview data is provided.  This "New ASI" option enables staff to quickly enter data, to easily jump from one item to another, and to enter free text comments at any time. This option should greatly reduce data entry time, whether transcribing interview results from a paper form or entering them on-line during an interview. It is not a self-administered version of the ASI, though, and should not be used for patient entry of ASI responses.

<!-- image -->

**Example:** Addiction Severity Index Manager form

#### Main Menu

The Main Menu offers user functions in the context of the ASI Manager form, such as tools and help.

#### Selected Patient Identification Label

The Selected Patient Identification label displays information about who is the currently-selected patient within MHA. All functions performed in the ASI Manager form will apply to this patient.

#### Title Bar

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. In this case, the Title Bar displays the current instrument’s name.

#### List of Previously-Administered ASIs

This is the list of all ASIs that have been administered to the selected patient. The list is also used for selecting which ASI to process.

#### Report View

The Report View displays an administration report in textual form, based on the patient’s data stored in VistA for the selected administration.

#### Navigation Tabs

These tabs are used to switch between the various views of the data.

#### ASI Editing Buttons

The ASI Editing Buttons are used to create new ASIs or edit existing ones.

#### Days Since Last ASI Label

The Days Since Last ASI label is a reminder about how long ago the current patient had an ASI.

#### Determining the Number of Days since the Last ASI for Selected Patient

To determine when the last ASI was administered to the current patient, observe towards the middle- left of the ASI Manager form. Read the text label that states **“** “ **x” days since last ASI** .”

**Example:** The last ASI for this patient was administered 10 days ago.

<!-- image -->

##### Selecting a Previous Interview

To select from previously administered interviews, click on the row for the desired interview from the table that lists all previous interviews (upper section of form). The clicked row will be highlighted, and the corresponding report type (Item or Narrative) will be shown below the table.

**Example:** The ASI interview dated 4/22/2011 is selected, and the Narrative Report is shown below.

<!-- image -->

#### Selecting a Report Type

To select a report type, click on a navigation tab at the bottom of the form. Switch between **Narrative Report** and **Item Report.** The selected report type will be shown for the selected (highlighted) interview.

**Example:** The Item Report for the 4/22/2011 interview is shown. Note that more than one ASI record must be available for displaying the Domain Scores or Item Trends tabs.

<!-- image -->

#### Restarting an Unsigned ASI

**NOTE:** This option can be used to complete, edit, or sign an unsigned ASI.

<!-- image -->

**Example:** To restart an unsigned ASI, select an unsigned ASI in the table that lists previous ASIs on

the ASI Manager. Click on the **Edit** button. The data entry form will appear, and previous answers will be inserted.

<!-- image -->

#### Starting a New ASI

To start a New ASI, **click** on the **New ASI** button, and then **click** on the **Full** menu item. There are two types of New ASI data which can be entered: **Full** or **Lite** . The ASI data entry form will appear, and will be formatted corresponding to the choice made by the user: Full or Lite.

**Example:** File | New ASI… menu item

<!-- image -->

###### Example: The Addiction Severity Index Manager form.

<!-- image -->

When the ASI data entry form first begins, it highlights the first item. The first item, G3, is automatically set to the user's last selection. In addition, the fields “G4. Date of Admission” and “G5. Date of Interview,” contains today’s date as defaults; field “G9. Contact Type” is set to “1. In person” and “G11. Interviewer” and “G11a. Ordered By” are set to the staff member who logged on to MHA; field “G12. Special” is set to “N. Interview completed.”

| **ASI Type**   | **Items with default values**          |
|----------------|----------------------------------------|
| Full           | G4, G5, G8, G9, G11, G11a and G12.     |
| Lite           | G3, G4, G5, G8, G9, G11 and G11a.      |
| Follow-up      | G3, G4, G5, G8, G9, G11, G11a and G12. |

**Example:** G8 is “grayed-out” because it is not modifiable. However, G8 displays the selected ASI type.

<!-- image -->

#### Saving a Report, Graph or Table to a File

To save a graph, report or table, **click** on **File | Save As…** menu item and then click on Graph, Report or Table. To save a graph or a table, the “Graph &amp; Table” tab must be selected first.

The following types of reports are available:

- Narrative Report
- Item Report
- Item Trends Report
- Items Trends Graph
- Domain Scores Report
- Domain Scores Graph

Select the report or graph types by clicking on each of the four tabs at the bottom of the form.

**Example:** A message dialog appears that asks the user to enter a filename and storage location for the table, report or graph file to be saved. A graph is saved as a bitmap, a table is saved as an Excel file and a report is saved as a text file.

<!-- image -->

**Example: Save As** form.

<!-- image -->

##### Printing a Report, Graph, or Table

To print a graph, report, or table, **click** on **File | Print** menu item and then **click** on Graph, Report, Table item. A copy of the table, report, or graph is sent directly to the default printer.

The following types of reports are available:

- Narrative Report
- Item Report
- Item Trends Report
- Items Trends Graph
- Domain Scores Report
- Domain Scores Graph

**Example:** Printing a Report, Graph, or Table.

<!-- image -->

#### Copying a Report, Graph, or Table to the Windows Clipboard

To copy a report, graph, or table to the Windows clipboard, click on **Edit | Copy** menu item and then click on Graph, Report or Table. A copy of the table, report or graph is sent to the Clipboard. The contents of the Clipboard can then be pasted onto an MS Word or Excel document.

The following types of reports are available:

- Narrative Report
- Item Report
- Item Trends Report
- Items Trends Graph
- Domain Scores Report
- Domain Scores Graph

**Example:** Copying a Report, Graph, or Table to the Windows Clipboard.

<!-- image -->

**Example: M** essage displayed after copying to the clipboard.

<!-- image -->

#### Navigating through the Different Views on the ASI Manager Form

To navigate, **click** on **View** and then **click** on any of the following **menu entries:**

- Narrative Report
- Item Report
- Item Trends
- Domain Scores

**Example:** The four tabs at the bottom of the form do the same thing.

<!-- image -->

#### ASI: Data Entry

This section of the guide illustrates the action of different types of form components such as combo boxes, option button groups, etc. Not every instance of each type of component is shown, but the user can learn from these examples how every component of the data entry form is to be used.

##### Combo Boxes

**Navigation** and **Selection:** To navigate this list with the keyboard, use the up and down keys, or type the first few letters of program type. Using the mouse, slide the scroll bar or click on the up and down arrows on the scroll bar. To select a program type using the keyboard, press the “tab” or “enter”. The highlighted item is selected. Using the mouse, left click on the desired program type and the list will disappear.

**Example:** From the ASI Data Entry Form, **click** on the down arrow of Item **G3. Program Type** , (light colored arrow above). A list of 21 ASI Program types will be displayed, eight at a time. Status bar will have context sensitive hints.

<!-- image -->

#### Date Fields

**Navigation and Selection:** To navigate this calendar using the keyboard, press the left and right keys to change days and shift-left and shift-right to change months. Pressing the "home" key moves to the 1 st day of the month. Press the "tab" or "enter" key to select the date and close the calendar. Clicking the mouse on a day will select the day and close the calendar. Clicking on the left and right arrows will change the month.

**Example:** From the ASI Data Entry Form, **click** on the down arrow of Item G4, Date of Admission. A calendar is displayed. The status bar will update its hint.

<!-- image -->

**Example:** The date can be typed directly in the edit box. The following formats are accepted: 4/14/2012, 4-14-12, 4.14.12, and 4,14,2012. Notice that the year can be entered as last two digits or four digits. Acceptable delimiters are the backslash, period, comma and dash. Dates in the future are not accepted.

<!-- image -->

#### Option Button Groups

Press the keys "1", "2", or "3" and the appropriate box will be checked and the user will be taken to the next item. While mouse input is effective, experienced users find keyboard entry to be quicker and easier. If an incorrect key is pressed, an error message will appear.

**Example:** From the ASI Data Entry Form, **click** on one of the boxes in item **G17** . By clicking on a box or its text a check will appear in that box and other checks will be removed from other boxes.

<!-- image -->

##### Spin Edit

Type the number of years—an acceptable number is from 0 to 99—and then press either the "tab" or "enter" key. The "Months:" will then become the active item and will be highlighted. If an incorrect number is entered, an error message will appear.

**Example:** From the ASI Data Entry Form, type in the year and press tab or enter key. The next item will then be highlighted, ready for input.

**Click on field and type in # value**

<!-- image -->

The spin-edit field can be increased by one when the up arrow receives a mouse click, or when the up-arrow key is pressed. To decrease the value, click on the down arrow or press the down arrow key. A number will not increase beyond the limit of the acceptable range. To move to the next item, press the "tab" or "enter" key.

**Example:** From the ASI Data Entry Form, **click** on the up or down arrows of the spin-edit field of G14. The number in the spin-edit box will increase or decrease by one.

<!-- image -->

#### Item G12

From the ASI Data Entry Form, click on

###### 1 Patient Terminated or

1. **Patient Refused** or
2. **Patient unable to respond** " on Item G12.

A dialog-message will appear indicating that default values will not be set for the user.

<!-- image -->

#### Item G19

The edit box is active only when item G19 has response "6. Other (specify)" checked. Otherwise the edit box is disabled (user cannot write to it).

**Example:** From the ASI Data Entry Form, click on **6. Other (Specify)** on Item G19. The edit box below will become active.

<!-- image -->

By clicking on “1. No” the edit box becomes disabled as does item G20. Item G20 will have a response of “N.” This will also occur with “X. Not Answered” and “N. Not Applicable.”

From the ASI Data Entry Form on Item G19, click on

**1. No** or

###### 2 Not Answered

**Example:** The edit box below will, if active, become inactive and G20 will also become inactive with a value of “N”.

<!-- image -->

**Medical Tab**

The Medical Status page has a unique color on its title bar.

**Example:** From the ASI Data Entry Form, click on the tab, **Medical** . The form will move to the Medical Status page.

<!-- image -->

##### Item M1

If the patient has never been hospitalized in his or her life, it follows that the last hospitalization queried in M2 is not applicable.

**Example:** From the ASI Data Entry Form, type an “N” (case insensitive) in the spin-edit field for M1. The spin-edit fields for M2 will be changed to “N” and will become inactive.

<!-- image -->

#### Medical Status Comments

The medical status Comments field is an edit field that accepts free text.

**Example:** From the ASI Data Entry Form, type comments in **Medical Status Comments** field. The memo field will accept free text.

<!-- image -->

#### Ending an ASI Data-entry Session

**Example:** To end an ASI session, click on the **File | Exit** menu option on the ASI data-entry form to invoke the **Close ASI** form. The **Close ASI** form is displayed

<!-- image -->

**Example:** ASI Close form.

<!-- image -->

#### Closing ASI Data-entry Session with “Exit” option.

**Example:** To exit a session, ignoring all changes made, **click** on **Exit,** then in the next dialog box, select **YES.**

<!-- image -->

**Example:** Message box warning that ASI has not been saved.

<!-- image -->

#### Closing ASI data-entry session with “Finish Later” option

**Example:** To finish a session “later”, click on **Finish Later** option on the **Close ASI** form. Work in progress is saved and the data-entry form is closed. No messages are displayed. The ASI is listed on the ASI Manager form as an incomplete ASI.

<!-- image -->

#### Closing ASI data-entry session with “Save and sign”

**Example:** To save and sign an ASI, **click** on **Save and sign** option on the **Close ASI** form.

<!-- image -->

**Example:** Electronic signature form contains the option to sign ASI.

<!-- image -->

**Example:** Option to save a progress note.

<!-- image -->

### ASI: Business Rules

Business rules check to see whether pairs of responses are logically consistent. The table below lists all of these rules and their actions.

| **Item #'s**   | **Coding Error**                               | **Cross Check Message**                                                                                                                                                                                                                                                                                           | **Yes/No OK**   | **Cursor movement**                                                                                          |
|----------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| G19 and G20    | G19>1, and G20=0,00, or N                      | In the last question (G19), you recorded that the patient has been in a controlled environment in the past 30 days, this question, (G20) how many days, should be greater than 0.                                                                                                                                 | OK              | Pop-up after G20 is entered. Cursor doesn't move.                                                            |
| G19 and M1     | G19=4, and M1=0, 00, N.                        | You recorded in the general information section (G19), that the patient had been hospitalized for medical problems in the past 30 days. This hospitalization would usually be coded in this question. Do you want to recode M1?                                                                                   | Yes/No          | Pop-up after M1 is entered. If  **"Yes"**  , the cursor doesn't move. If  **"No"**  , cursor moves to M3.    |
| G19 and M2     | G19=4 and M2 years or months  &gt;0, 00, or N. | In the general information section (G19), you recorded that the patient had been hospitalized this month for medical problems. The correct coding in M2 is usually 00 00 in this case. Do you want to recode M2?                                                                                                  | Yes/No          | After M2 is entered. If  **"Yes"**  , the cursor doesn't move. If  **"No"**  , cursor moves  to M3.          |
| M6 and M7      | M6>0, and M7=0.                                | In the last question, you recorded that the patient experienced some medical problems in the past 30 days. If this were true, then we would expect that the patient would be at least slightly bothered by these problems. Do you want to recode M7?                                                              | Yes/No          | After M7 is entered. If  **"Yes"**  , the cursor doesn't move. If  **"No"**  , cursor moves to M8.           |
| M6, M7  and M8 | M6=0 or 00, and M7 or M8>0.                    | In question M6, you recorded that the patient experienced no medical problems in the past 30 days, since they report being troubled or wanting treatment (M7 or M8), it is fair to expect that they had some problem days. Go back to M6 and identify the number of days the problem has bothered them.           | OK              | After M8 is entered. Cursor moves back to M6.                                                                |
| E1a            | E1a<4                                          | You are reporting that the patient has had less than 4 years of education, this is rare. Please review this, did you include home schooling, grade school, etc.? Do you want to change E1?                                                                                                                        | Yes/No          | Pop-up after E1b is entered. If  **"Yes"**  , the cursor moves to E1a. If  **"No"**  , cursor moves to E2.   |
| E4 and E5      | E4=0 and E5=1                                  | If the client does not have a driver's license, E5 is always coded as  **"No"**  . This is because E5 asks about the car as a way of evaluating ability to travel to and from a job. If the client does not have a license, they cannot "get credit" for having a car! The computer has made this change for you. | OK              | Pop-up after E5 is entered.  This is a forced change – there is not an option to leave E5=1 if E4=0.         |
| E8 and E9      | E8=0 and E9=1                                  | In the last question (E8), you said no one contributes to the client's support, and in this question, you are saying the client gets most of his or her support from someone. Do you want to change your answer in E8?                                                                                            | Yes/No          | Pop-up after E9 is entered. If  **"Yes"**  , the cursor moves to E8. If  **"No"**  , cursor moves to E10.    |
| E11 and E12    | E11=0 or 00 and E12>0                          | In the last question (E11), you recorded that the patient was not paid for working at all in the past month. If this is the case, E12 is generally $ 0. Do you want to change E11?                                                                                                                                | Yes/No          | Pop-up after E12 is entered. If  **"Yes"**  , the cursor moves to E11. If  **"No"**  , cursor  moves to E13. |
| E11 and E12    | E11&gt;0 and E12=0, 00, 000,  or 0000          | In the last question (E11), you recorded that the patient was paid for working this month.  If this is the case, E12 is generally not $ 0, unless the patient has collected no money for their work. Do you want to change E12?                                                                                   | Yes/No          | Pop-up after E12 is entered. If  **"Yes"**  , the cursor doesn’t move. If  **"No"**  , cursor moves to E13.  |

| **Item #'s**     | **Coding Error**                          | **Cross Check Message**                                                                                                                                                                                                                                       | **Yes/No OK**   | **Cursor movement**                                                                                           |
|------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------|
| E15 and M5       | E15=0, 00, 000,  0000, or 00000  and M5=1 | You recorded earlier (M5), that the patient receives a pension for a medical problem. This income is generally recorded in E15 unless they did not receive any cash this month. Do you want to change E15?                                                    | Yes/No          | Pop-up after E15 is entered. If  **"Yes"**  , the cursor doesn’t move. If  **"No"**  , cursor moves to E16.   |
| E19 and E20      | E19>0 and E20=0                           | In E19, you recorded that the patient experienced some employment problems in the past 30 days. If this were true, then we would expect that the patient would be at least slightly bothered by these problems. Do you want to recode E20?                    | Yes/No          | Pop-up after E20 is entered. If  **"Yes"**  , the cursor doesn’t move. If  **"No"**  , cursor moves to E21.   |
| D1a and D2a      | D2a >D1a                                  | You recorded that the patient drank "to intoxication" (D2) more  days than total number of days drinking any alcohol at all (D1). Probe and recode D1. Remember D2 is a sub-set of D1.                                                                        | OK              | After D2a is entered.  Cursor moves to D1a.                                                                   |
| D1b and D2b      | D2b > D1b                                 | You recorded that the patient drank "to intoxication" (D2) more  years than total number of years drinking any alcohol at all (D1). Probe and recode D1. Remember D2 is a sub-set of D1.                                                                      | Ok              | After D2b is entered.  Cursor moves to D1b.                                                                   |
| D1-D12  and G20  | G20>0 and any item D1a- D12a=30           | You recorded in the general information section that the patient had been in a controlled environment in the past month, yet they used either drugs or alcohol every day. Please review this. Do you want to change any information in the drug/alcohol grid? | Yes/No          | Pop-up after D12a is entered. If  **"Yes"**  , the cursor moves to D1a. If  **"No"**  , cursor moves to D12b. |
| D14 and D1-D12   | D14=3 - 12 or 16  and D1a&gt;15           | You report that the patient's problem does not include alcohol, however, the patient used alcohol at least 15 days in the past month. Please review this and consider option "Alcohol and one or more drugs" for question D14. Do you want to change D14?     | Yes/No          | Pop-up after D14 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  , cursor moves to D15.  |
| D16 and D1a-D12a | D16=0 or 00 and D1a-D12a>0                | You recorded that the patient is "still sober", however, drug or alcohol use in the past 30 days is documented in the drug and alcohol grid. Please review this. Do you want to change D16?                                                                   | Yes/No          | Pop-up after D16 is entered. If  **"Yes"**  , the cursor does not  move. If  **"No"**  , cursor moves to D17. |
| D17              | D17>5                                     | You recorded more than 5 episodes of DT's for this patient. This is extremely rare, please review the definition of DT's if you are unsure. Do you want to change it?                                                                                         | Yes/No          | Pop-up after D17 is entered. If  **"Yes"**  , the cursor does not  move. If  **"No"**  , cursor moves to D18. |
| D19 and D21      | D19=0 or 00 and D21>00                    | You recorded that the patient never had any treatments for alcohol abuse, so # of detox treatments is not applicable. Do you want to recode (D19), the total number of treatments received?                                                                   | Yes/No          | Pop-up after D21 is entered. If  **"Yes"**  , the cursor moves to  D19. If  **"No"**  , cursor moves to D23.  |
| D19 and D21      | D19>0, and D21>D19                        | You recorded that the patient had more detox treatments than the total number of treatments received for alcohol abuse. Remember D21 is a sub-set of D19. Do you want to recode D19?                                                                          | Yes/No          | Pop-up after D21 is entered. If  **"Yes"**  , the cursor moves to  D19. If  **"No"**  , cursor moves to D23.  |
| D20 and D22      | D20>0, and D22>D20                        | You recorded that the patient had more detox treatments that the total number of treatments received for drug abuse. Remember D22 is a sub-set of D20. Do you want to recode D20?                                                                             | Yes/No          | Pop-up after D22 is entered. If  **"Yes"**  , the cursor moves to D20. If  **"No"**  , cursor moves to D24.   |
| D20 and D22      | D20=0 or 00 and D22>00                    | You recorded that the patient never had any treatments for drug abuse, so # of detox treatments is not applicable. Do you want to recode (D20), the total number of treatments received?                                                                      | Yes/No          | Pop-up after D22 is entered. If  **"Yes"**  , the cursor moves to D20. If  **"No"**  , cursor moves to D24.   |

| **Item #'s**            | **Coding Error**                                             | **Cross Check Message**                                                                                                                                                                                                                                                                                                        | **Yes/No OK**   | **Cursor movement**                                                                                           |
|-------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------|
| D1a and D23             | D1a=0 or 00 and D23>0                                        | You recorded no days of drinking in the past 30, but recorded the client has spent money on alcohol. This is unlikely. Please review. Do you want to change D23?                                                                                                                                                               | Yes/No          | Pop-up after D23 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  ,  cursor moves to D20. |
| D1a, D2a,  andD23       | D1a+D2a&gt;0 and D23=0, 00, 000,  0000, or 00000             | You recorded the client's drinking in the past 30 days (D1 and D2), but no money spent on alcohol. Please review this, do you want to change D23?                                                                                                                                                                              | Yes/No          | Pop-up after D23 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  , cursor moves to D20.  |
| D3a-D12a,  and D24      | All items D3a through D12a = 0 or 00 and D24 >0              | You recorded zero days of drug use in the past 30, but the patient acknowledges spending money on drugs this month. Please review, and coded those drugs used in the past 30 days. Do you want to change # of days of drug use in the drug grid?                                                                               | Yes/No          | Pop-up after D24 is entered. If  **"Yes"**  , the cursor moves to D3a. If  **"No"**  , cursor  moves to D25.  |
| D3a-D12a,  andD24       | Any item D3a- D12a&gt;0 and D24=0, 00, 000,  0000, or 00000. | You recorded days of drug use in the past 30 days, but no money spent on drugs, please review this. Do you want to change D24?                                                                                                                                                                                                 | Yes/No          | Pop-up after D24 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  , cursor moves to D25.  |
| D26, D28,  and D30      | D26&gt;0 and D28  and/or D30=0                               | In an earlier question (D26), you recorded that the patient had experienced some days with alcohol problems in the past 30 days. If this is true, then we would expect the patient would be at least slightly bothered or slightly in need of treatment for these problems. Do you want to change your code on D28 and/or D30? | Yes/No          | Pop-up after D30 is entered. If  **"Yes"**  , the cursor moves to D28. If  **"No"**  , cursor moves to D27.   |
| D26, D28,  and D30      | D26=0 or 00 and D28 or D30>0.                                | In an earlier question (D26), you recorded that the patient had no alcohol problems in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to D26 and identify the number of days the problem has bothered them.                            | OK              | Pop-up after D30 is entered. Cursor moves to D26.                                                             |
| D27, D29,  and D31      | D27&gt;0 and D29  and/or D31=0                               | In an earlier question (D27), you recorded that the patient had experienced some days with drug problems in the past 30 days. If this is true, then we would expect the patient would be at least slightly bothered or slightly in need of treatment for these problems. Do you want to change your code on D2 and/or D31?     | Yes/No          | Pop-up after D31 is entered. If  **"Yes"**  , the cursor moves to D29. If  **"No"**  , cursor moves to D32.   |
| D27, D29,  and D31      | D27=0 and D29 or D31>0.                                      | In an earlier question (D27), you recorded that the patient had no problems with drugs in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to D27 and identify the number of days the problem has bothered them.                         | OK              | Pop-up after D31 is entered. Cursor moves to D27.                                                             |
| L3-L16  and L17         | L3 through L16 total > L17                                   | You recorded the patient had more convictions than the total number of times they were arrested and charged (L3 to L16). This is unusual. Do you want to change L17?                                                                                                                                                           | Yes/No          | Pop-up after L17 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  , cursor moves to L18.  |
| L2 and L3-L16, L18-L20. | L2=1 and all L3- L16 and L18- L20=0 or 00.                   | In an earlier question (L2), you indicated the patient is on probation or parole. However, no arrests or charges are documented in items L3-L20. Do you want to recode any legal charges?                                                                                                                                      | Yes/No          | Pop-up after L20 is entered. If  **"Yes"**  , the cursor moves to L3. If  **"No"**  , cursor  moves to L21.   |
| L24 and L3-L16, L18-L20 | L24=1, and L3- L16 and L18- L20=0 or 00                      | You recorded the patient is awaiting charges, trial or sentence (L24), but no arrests and/or charges are coded in L3-L16 or L18- L20. Do you want to recode any of the charges?                                                                                                                                                | Yes/No          | Pop-up after L24 is entered. If  **"Yes"**  , the cursor moves to L3. If  **"No"**  , cursor  moves to L25.   |

| **Item #'s**       | **Coding Error**                                             | **Cross Check Message**                                                                                                                                                                                                                                                                                                 | **Yes/No OK**   | **Cursor movement**                                                                                                 |
|--------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| L24 and L25        | L24=0, and L25>0                                             | You recorded the patient was not awaiting charges, trial or sentence (L24), yet you coded a charge in L25 (which would be not applicable). Do you want to recode L24?                                                                                                                                                   | Yes/No          | Pop-up after L25 is entered. If  **"Yes"**  , the cursor moves to L24. If  **"No"**  , cursor moves to L26.         |
| L26 and G19        | G19=2 and L26=0 or 00                                        | In the general information section, you recorded that the patient had been in jail in the past 30 days, this is usually also represented in L26. Do you want to change your code on L26?                                                                                                                                | Yes/No          | Pop-up after L26 is entered. If  **"Yes"**  , the cursor does not move. If  **"No"**  , cursor moves to L27.        |
| L27 and E17        | E17>0 and L27=00                                             | In the employment section, you recorded that the patient had illegal income in the past 30 days, this is usually also documented in L27. Do you want to change your code on L27?                                                                                                                                        | Yes/No          | Pop-up after L27 is entered. If  **"Yes"**  , the cursor does not  move. If  **"No"**  , cursor moves to L28.       |
| F30, F32,  and F34 | F30&gt;0 and F32  and/or F34=0                               | In an earlier question (F30), you recorded that the patient had some family conflicts in the past 30 days. If this is true, then we would expect that the patient would be at least slightly bothered or slightly in need of treatment. Do you want to recode F32 or F34?                                               | Yes/No          | Pop-up after F34 is entered. If  **"Yes"**  , the cursor moves to F32. If  **"No"**  , cursor moves to F31.         |
| F30, F32,  and F34 | F30=0 or 00 and F32 and/or F34>0.                            | In an earlier question (F30), you recorded that the patient had no family conflicts in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Do you want to go back to F30 and identify the number of days the problem has bothered them?      | Yes/No          | Pop-up after F34 is entered. Cursor moves to F30.                                                                   |
| F31, F33,  and F35 | F31&gt;0 and F33  and/or F35=0                               | In an earlier question (F31), you recorded that the patient had some conflicts with others in the past 30 days. If this is true, then we would expect that the patient would be at least slightly bothered or slightly in need of treatment for this recent problem. Do you want to recode F33 or F35?                  | Yes/No          | Pop-up after F35 is entered. If  **"Yes"**  , the cursor moves to F33. If  **"No"**  , cursor moves to F36.         |
| F31, F33,  and F35 | F31=0 and F33 or F35>0.                                      | In an earlier question (F31), you recorded that the patient had no conflicts with others in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Do you want to go back to F31 and identify the number of days the problem has bothered them? | Yes/No          | Pop-up after F35 is entered. Cursor moves to F31.                                                                   |
| P1, P2 and P10a/b  | P1 + P2=0 or 00  and P10 a or b (past 30 days or lifetime)=1 | You recorded that the patient has not had inpatient or outpatient treatment for psychiatric problems (P1 and P2), yet they have attempted suicide. Please review treatment they may have received for the suicide attempt. Do you want to recode P1 or P2?                                                              | Yes/No          | Pop-up after P10a and b are entered. If  **"Yes"**  , the cursor moves to P1. If  **"No"**  , cursor moves to P11a. |
| P1, P2 and P11a/b  | P1 + P2=0 or 00  and P11 a or b (past 30 days or lifetime)=1 | You recorded that the patient has not had inpatient or outpatient treatment for psychiatric problems (P1 and P2), yet they have been prescribed medications for psychiatric problems. Please review treatment they may have received. Do you want to recode P1 or P2?                                                   | Yes/No          | Pop-up after P11a and b are entered. If  **"Yes"**  , the cursor moves to P1. If  **"No"**  , cursor moves to P12.  |
| P3 and E15         | E15=0, 00, 000,  0000, or 0000  and P3=1                     | You recorded that the patient receives a pension for a psychiatric problem (P3). Unless they did not receive any cash this month, this income is generally recorded in the employment question about pension money received (E15). Go back and change E15 in the Employment section.                                    | OK              | Pop-up after P3 is entered.  Cursor doesn’t move.                                                                   |

| **Item #'s**       | **Coding Error**                        | **Cross Check Message**                                                                                                                                                                                                                                                            | **Yes/No OK**   | **Cursor movement**                                                                                        |
|--------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------|
| P4a-P10a  and P12  | P4a through P10a=0 or 00,  and P12&gt;0 | You report that the patient has had problems in the past 30 days, but none are recorded in the psychiatric symptom list P4 through P10. Please review P4 through P10, do you want to go back and change the code of any of the symptoms?                                           | Yes/No          | Pop-up after P12 is entered. If  **"Yes"**  , the cursor moves to P4. If  **"No"**  , cursor moves to P13. |
| P4a-P10a  and P12  | P4a through P10a>0 and P12=0            | You report that the patient has had no problems in the past 30 days, but problems are evident from the psychiatric symptom list P4 through P10, please probe about the number of days these symptoms bothered the client and recode P12.                                           | OK              | Pop-up after P12 is entered. Cursor does not move.                                                         |
| P9a and P10a       | P9a and/or P10a=1                       | You report that the client has said they have either suicidal ideation or have attempted suicide in the past 30 days. Probe further for a plan for the suicide and/or dates of the suicide attempt. Notify your supervisor of these responses.                                     | OK              | After P10a is entered.  **Cursor moves to P10b.**                                                          |
| P12, P13,  and P14 | P12&gt;0 and P13  and/or P14=0.         | You report that the patient had psychiatric problems in the past 30 days, (P12). Given these problems, we would expect that the patient would be at least slightly bothered or slightly in need of treatment for this recent problem, please recode P13 and/or P14.                | OK              | After P14 is entered. Cursor moves to P12.                                                                 |
| P12, P13,  and P14 | P12=0 or 00 and P13 or P14>0.           | You report that the patient had no psychiatric problems in the past 30 days (P12). If they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to P12 and identify the number of days the symptoms have bothered the client. | OK              | After P14 is entered. Cursor moves to P12.                                                                 |

### ASI : Changing User Preferences

User preferences can be changed in the **Tools | Options…** menu.

**Example:** Some system parameters are user-configurable and can be changed by clicking on the

**Tools | Options…** menu item.

<!-- image -->

#### Default Form Size/Position

When the **Default Form Size/Position option** is checked, this function is used. If it is **not** checked, the Default Form Size/Position that was true when the MHA session was closed the last time is used. The status of the **Default Form Size/Position** option (i.e., checked or not checked) is saved from one MHA session to another, so the Default Form Size/Position settings or the user-preferred settings can always be used. The first time a MHA session is started, the **Default Form Size/Position option** is checked and the default settings are used.

From the Mental Health Assistant window, **click on Tools,** and **click** on **Default Form Size/Position** . The check-mark symbol displayed beside the **Default Form Size/Position option** toggles on and off and the window size will adjust accordingly.

**Speed Tab**

The Speed Tab is provided to make data entry faster. ASI Items that require a simple click (or single keystroke) will move to the next item without the user pressing the **Tab** or **Enter** keys. This is particularly helpful on the Social and Psychiatric sections of the ASI.

**Highlight Color**

The colors depicting the highlighted items on the ASI form can be modified by the user. The default colors are black lettering on a yellow background. To change the foreground or background, use the combo box to select the desired colors. If the user selects the same color for both foreground and background, the item would not be visible and an error message would appear. No checks are conducted for tasteless color choices.

**Example:** Highlight color-selection form.

<!-- image -->

### ASI: Help Menu Options

#### Opening the ASI Help File

**Click** on **Help** | **Contents** … on the help menu, to access the ASI Help file, from the ASI Data Entry Form. The help file for the clinician is opened. This is from the University of Pennsylvania/Veterans Administration Center for Studies of Addiction (1977).

**Example:** ASI help file.

<!-- image -->

<!-- image -->

#### Using the Help Index

From the ASI Data Entry form, **click** on **Help Index** from the help menu to access the Help Index. The help file will be opened. This file has information concerning the operation of the program.

**Example:** ASI Help Index.

<!-- image -->

#### Domain Scores

**Example:** To view the Domain Scores, **click** on **Domain Scores** tab. The ASI domain results will be displayed in graph and text form.

<!-- image -->

#### Item Trends

To view the Items Trend, click on **Item Trends** tab. Item-level data will be presented in tabular and graphical form across interviews.

<!-- image -->

#### Graphing a Different Item

To graph a different item, click on different row in table of item data. The new row will be highlighted and the data for that item will be graphed.

**Example:** The item was changed from E12 (previous example) to M6 by clicking on the M6 row. M6 data are graphed.

<!-- image -->

#### Returning to the Narrative Report View

**Example:** To return to the Narrative Report View, Click on the **Narrative Report** tab. The original view of the ASI tab is restored.

<!-- image -->

### User Preferences Functions

#### Orientation

**Example:** The User Preferences form enables the user to customize the manner in which several functions are performed and displayed in MHA. Additionally, the font and display functions are an attempt to comply with Section 508 requirements in MHA’s user interface.

<!-- image -->

#### Form Title

The Form Title simply identifies the form.

#### Navigation Tabs

The Navigation Tabs are used to access the various functions that are distributed across four panels.

#### Editing Panel

The Editing Panel displays the various artifacts that the user manipulates to make adjustments to preferences. There are four panels, but only one of them is visible at any one time.

#### Command Buttons

The Command Buttons are used to either cancel all actions or close the window and save the changes made.

#### Changing MHA System Font

There are three types of fonts that the user may select to provide the best viewing comfort possible: The CPRS Font, the Windows Font, or a New Font. Selecting the CPRS Font will change MHA’s font to match that with CPRS uses. If the user is comfortable with the CPRS font, then this may be a good choice. The Windows Font is the “default” Windows font. This font is used by the other programs on the system too. The New Font option enables the user to select from any of the fonts found on the PC. With this option it is possible to change font characteristics, such as size and bold, etc. In most cases, the font will not need to be changed from the one offered initially by MHA. To change Font options:

1. Click on any of the three font Option Buttons.
2. Click on the **Done** button

**Example:** Font tab. Clicking on **Cancel** ignores any choices made.

**1. Click**

**2. Click**

<!-- image -->

**Example:** If the **New Font** button is selected, the New Font selection prompt is displayed.

<!-- image -->

**2. Click**

<!-- image -->

As a navigational aide, the selected question on the All-Questions form is highlighted with a different color from the form’s color. This color can be changed by choosing the Highlight Color tab and selecting colors from the artifacts on the Editing Panel.

**Example:** Highlight Color tab. Clicking on **Cancel** ignores any choices made.

**1. Click**

<!-- image -->

#### Toggling Visual Feedback On/Off

Visual Feedback displays error messages in addition to sound beeps. A dialog would be presented to identify the error the user made, for example, the dialog message says the wrong key had been pressed.

1. Click on the **Miscellaneous tab**
2. Click on the **“Provide visual feedback…”** button, so that a checkmark is displayed.

**Example:** Miscellaneous tab. **Clicking** on **Cancel** button ignores any choices made.

**1. Click**

**2. Click**

<!-- image -->

#### Toggling Screen Reader On/Off

MHA has the ability to detect when a screen reader is in use. MHA will automatically change many of its forms so that a screen reader can accurately and intelligently present information to the listener. Sometimes it is useful to run MHA as if a screen reader is in use, usually for testing purposes, and this toggle provides that ability.

###### To toggle Screen Reader:

1. Click on the **Miscellaneous tab**
2. Click on the **“Screen Reader…”** button, so that a checkmark is displayed
3. Click on the **Done** button

#### Toggling Speed Tab On/Off

Speed Tab is a feature to increase data entry speed. Speed Tab is actually an automatic “Tab” key press that is triggered after the user makes a choice from a question with multiple choice answers. This saves the user from having to press the Tab key to move on to subsequent questions on the form. However, the Speed Tab option has no effect on Multiple-Line Text Boxes, Single-Line Text Boxes and Spin Boxes. A check box to toggle the Speed Tab is also located on the data-entry form.

###### To toggle Speed Tab:

1. Click on the **Miscellaneous tab**
2. Click on the **“Speed Tab…”** button, so that a checkmark is displayed
3. Click on the **Done** button
4. Speed Tab functions are enabled in the data-entry forms, based on whether the checkmark was visible at the time of clicking on the **Done** button.

**Example:** Miscellaneous tab. clicking on **Cancel** , ignores any choices made.

**1. Click**

**2. Click**

<!-- image -->

**Toggling The Display Of Images On The Main Menu** The images on the Main Menu can be turned off or on by checking the box. **Example:** Miscellaneous tab. clicking on **Cancel** , ignores any choices made.

**1. Click**

**2. Click**

<!-- image -->

#### Toggling: Maintain Original Font on/off

When an instrument is designed for MHA there are sometimes design characteristics that are based on the size and type of font so that questions and answers are displayed in a readable manner. Every effort is made to accommodate larger or smaller fonts should that be the user’s preference. Since the readability of an instrument is based on many factors (e.g., screen resolution, DPI settings, size of form), not just the font’s size and type, this toggle provides a means to ensure the instrument will be readable in its original design. The Original Font is maintained, based on whether the checkmark is set for this toggle. To set this toggle:

1. **Click** on the **Miscellaneous tab.**
2. **Click** on the **“Maintain Original font…”** button, so that a checkmark is displayed.

**Example:** Miscellaneous tab. Clicking on **Cancel** ignores any choices made.

**1. Click**

**2. Click**

<!-- image -->

#### Selecting the starting point for MHA

When MHA is started, it usually presents the Main Menu initially. This is the depiction throughout this manual. However, it is possible to bypass the Main Menu and present the “Instrument Administrator” instead. The user is able to select from the following starting points:

Main Menu

Instrument Administrator Instrument Results

ASI

Special Results.

To change the initial display in MHA:

1. **Click** on the **Menu tab.**
2. **Click** on one of the possible menu options.

**Example:** Menu tab. Clicking on **Cancel** ignores any choices made.

<!-- image -->

Off-line Administration Functions

#### Orientation

Most users are likely to use MHA in the standard way, that is, by administering instruments while their computer is connected to a VistA system. However, MHA offers “off-line” testing features for users needing such functionality, such as at CBOCs. Off-line testing enables the user to administer an instrument when the user’s computer is not able to connect to a VistA system, temporarily saving the administration’s results in an encrypted local file. When a user returns to the office and resumes a connection to VistA, the user is asked to match the off-line patient information for a selected administration with the VistA patient information. If the user is satisfied with the match, the results can be uploaded to VistA, at which time the temporary local file is deleted.

The only way that MHA can connect to VistA is by being “launched” from the CPRS Tools menu. This is different from previous versions of MHA. So, to invoke MHA for off-line use, users will need to double-click on the Mental Health Assistant icon on the desktop.

Stored Off-line administrations are not useful until they are uploaded to VistA, at which time they become part of the patient’s official record.

**Example:** There are two principal forms that are used for processing off-line administrations. The Off-line Patient Manager is used while disconnected to VistA, while the Off-line Results Synchronizer is used once a connection to VistA is restored.

<!-- image -->

##### Patient Selector

The Patient Selector Drop-Down List Box is used to choose from a list of existing off-line patients.

##### Patient Edit Area

The Patient Edit Area contains the input artifacts that are used to edit and display patient information.

##### New button

The New button is used to prepare the form for entering information about a new patient.

##### Delete button

The Delete button removes the selected patient from the list of patients and deletes the local record.

##### Cancel button

The Cancel button closes the Off-line Patient Manager without selecting a patient.

##### Ok button

The Ok button selects the current patient for processing of off-line administrations.

#### Off-line Results Synchronizer

To use the Off-line Results Synchronizer, the following must be true:

- The PC is connected to VistA.
- MHA is launched from the CPRS Tools menu.
- The user has previously administered at least one off-line instrument that has not yet been uploaded to VistA.

The following functionality is restored once connected to VistA:

- Instruments Ordered-by selection
- Interviewer selection
- Visit Location selection
- Online Support

**Example:** Off-line Results Synchronizer

<!-- image -->

#### Main Menu

The Main Menu offers user functions in the context of the Off-line Results Synchronizer form, such as file and help.

#### Off-line Records List

This is the list of all tests that have been administered off-line, which haven’t been uploaded to VistA yet. The list is used to select which administration to process.

#### CPRS Patient Search Panel

This group of artifacts is used to search for, and list, CPRS (VistA) patients which closely match the off-line patient that is selected in the Off-line Records List.

#### Patient Match Panel

This panel displays a table on which both the off-line and CPRS patient information is shown side- by-side to aid in determining the possibility of a match. All of the off-line patient information is assumed to come from the patient during an interview. In most cases, the information provided will be a perfect match to the information in VistA for the same patient. This matching scheme is a way for the clinician to verify that it is the same patient and to make any adjustments for typos and other minor errors.

#### Delete Off-line Record Button

This button triggers the deletion of the currently-selected off-line administration record. A confirmation prompt is displayed before deleting the record.

#### Upload Button

This button starts the process of uploading to VistA the currently-selected record.

#### Exit button

The Exit button closes the Off-line Results Synchronizer form.

#### Starting MHA in Off-line Mode from the Desktop Icon

To start MHA for off-line use:

1. Locate the **Mental Health Assistant 3** icon, as pictured below, on the Windows Desktop
2. Double-click the icon
3. Click on the **Yes** button on the “ **Do you want to work off-line”** prompt.
4. Clicking on **Yes** causes the Off-line Patient Manager form to display.

Clicking on the **No** button aborts MHA.

**Example:** The Mental Health Assistant icon on the Windows Desktop.

<!-- image -->

**Example:** “Do you want to work off-line” prompt

<!-- image -->

#### Selecting an Existing Patient from the Drop-Down List Box

###### To select an existing off-line patient record:

1. **Click** on the down-arrowhead to open up the Drop-Down List Box (Combo box).
2. **Click** on the name of the desired patient.

**Example:** The patient selected becomes the active patient on the Drop-Down List Box. Demographic information belonging to the selected patient fills the form.

<!-- image -->

#### Adding and Selecting a New Off-line Patient

###### To add a new patient to the list of off-line patients:

1. **Click** on the **New** button.
2. **Enter** the new patient information in the corresponding fields.
3. **Click** on the **Ok** button.

**Example:** The data entry fields are cleared and appear blank and ready for input. After clicking on the **Ok** button, the user is presented in the **Instrument Administrator** form

<!-- image -->

**Example:** Off-line **Instrument Administrator** form.

<!-- image -->

Since off-line administrations of instruments mean that the connection to VistA is not present, there are several features of MHA that are disabled:

- Instruments Ordered-by selection
- Interviewer selection
- Visit Location selection
- METRIC Instruments Reviews
- Battery Wizard
- Instrument Description
- Online Support

#### Selecting a Different Off-line Patient from the Instrument Administrator Form

###### To select another off-line patient from the Instrument Administrator form:

1. From the **Instrument Administrator** form, **click** on **File | Select Patient…** menu option.
2. The **Off-line Patient Manager** form is displayed, offering an opportunity to choose a different existing or new patient.
3. Choose a different off-line patient from the **Off-line Patient Manager** form. After selecting another patient, and clicking **Ok** , the new selected patient is identified.

**Example:** Selecting a patient on the **Instrument Administrator** form.

<!-- image -->

**Example:** Selecting an existing patient on the **Off-line Patient Manager** form.

<!-- image -->

#### Deleting an Existing Off-line Patient

###### To delete an off-line patient:

1. **Select** the name of an off-line patient using the Drop-Down List Box.
2. **Click** on the **Delete** button.
3. The delete warning message is displayed
4. Click on **Yes** to delete the selected patient from the list OR **click** on the **No** tab to abort the deletion.

**Example:** Selecting the name of an off-line patient using the Drop-Down List Box.

**1. Click**

**2. Click**

<!-- image -->

**Example:** Delete warning message.

<!-- image -->

#### Canceling Selection of an Off-line Patient

###### To exit the Off-line Patient Manager without selecting a patient:

1. Click on the **Cancel** button, or press the escape key “ESC”.
2. The cancel warning message is displayed.
3. Respond with **Yes** to the cancel warning message prompt.
4. Clicking on **Yes** closes the **Off-line Patient Manager** form.
5. Clicking on **No** returns to the **Off-line Patient Manager** form.

**Example:** Exiting the **Off-line Patient Manager** without selecting a patient.

**Click**

<!-- image -->

**Example:** Cancel warning message prompt

<!-- image -->

#### Closing the Off-line Patient Manager

When the Patient Off-Line Patient Manager is closed, and patient data have been entered, a prompt will appear that says the data can be uploaded to VistA the next time the user connects the computer to the VA network.

**Example:** Exit reminder prompt.

<!-- image -->

#### Recognizing the Availability of Off-line Administrations, and Initiating the Upload Process

If any records exist on the PC that were administered off-line, the user is reminded about them once MHA is launched from the CPRS Tools bar. A notification prompt is displayed and the user is offered a choice to upload these records at this time.

###### To upload existing off-line records:

1. Start CPRS.
2. Invoke MHA from the CPRS Tools menu.
3. If any off-line administration files are found on the PC, the “Do you want to upload to VistA…” prompt is presented. Otherwise, uploading functionality is bypassed and MHA starts up in normal VistA mode.
4. Uploading the confirmation prompt.

**Example: Click** on the **Yes** button, on the “Do you want to upload to VistA…” prompt. After clicking on **Yes** , the Off-line Results Synchronizer form is displayed.

<!-- image -->

**Example:** Off-line Results Synchronizer form.

<!-- image -->

#### Selecting an Off-line Record for Uploading

To select a record for uploading to VistA, click on the desired record from those presented on the

**Off-line Records** list.

1. The clicked-on record becomes the selected record
2. The left column of the **Results of Match** grid is populated with demographic information from the selected off-line patient’s record.
3. A search in the CPRS database is automatically triggered, to find and list the closest matching CPRS patient(s) on the **CPRS Patient Search Panel**
4. The right column of the **Results of Match** grid is populated with demographic information from the selected CPRS patient’s record.
5. If more than one CPRS patient match is found, the first one in the list is automatically selected, although it may not necessarily be the best match.

**Example:** Off-line Records list containing three records.

<!-- image -->

#### Searching for a Matching CPRS Patient

There are two kinds of search methods available for finding a matching CPRS patient: the automatic initial search and a manual search.

The automatic initial search uses a text filter that is built from the selected off-line patient’s first letter of the last name, followed by the last four of the SSN—the same way it is done in VistA. This text filter is automatically placed in the “ **Search for** ” Text Box, and is used for the initial search, which is triggered automatically.

Occasionally, the automatic initial search returns no results or returns poor matching results. In this case, the search text filter may be changed to customize a new result set. To start a manual search, replace the text in the **Search for** Text Box, and click on the **Go** button to trigger a new search, and a refreshed listing of possible matches.

Any text may be entered into the **Search for** Text Box, however, the patient’s last name or the default search text typically works best.

**Example:** The CPRS Patient Search Panel with search results.

**2. Click**

**1. Enter custom search filter**

**List of possible matches**

<!-- image -->

#### Evaluating the results of a possible match

After a search, hopefully the off-line patient’s demographic information results in an obvious match to the CPRS Patient, based on information stored in VistA. However, there will be exceptions, in which case the user is forced to make a judgment of whether there is a valid match or not. To aid in making this decision, the “Results of Match” grid displays information about the Off-Line Patient and the selected CPRS Patient.

**Example:** Results of Match grid.

<!-- image -->

**Example:** A poor match: No patient was found in the VistA database that matches the search text. The “Search for” text filter must be changed, and a new search initiated. Try the last name.

<!-- image -->

**Example:** A good match: Three out of four fields match perfectly, and the search results list a single patient. It’s possible that the unmatched field is the result of a typo or other type of data-entry mistake.

<!-- image -->

#### Uploading an Off-line Record to VistA

###### To upload a record to VistA:

1. Verify that the patient on the selected record is one that matches the CPRS patient.
2. **Click** on the **Upload** button.
3. **Click Yes** on the upload confirmation prompt
4. The additional required information prompt is displayed.
5. Enter the additional required information at the prompt, and then **click Ok** . The upload confirmation prompt is displayed.
6. The selected administration record is uploaded to VistA.
7. After uploading the record, the record is removed from the list of off-line records, which means that the record was deleted from the local file system too.

**Example:** To upload a record to VistA.

<!-- image -->

**Example:** Upload confirmation prompt. Responding with “No” will abort the upload.

<!-- image -->

**Example:** Additional required information prompt requesting Ordered By, Interviewer and Visit Location data. Change accordingly and then click Ok.

<!-- image -->

**Click**

#### Deleting an Off-line Record

WARNING: Off-line records, by definition, have not been uploaded to VistA. Deleting a record cannot be undone.

To delete an off-line record:

1. **Select** the record to be deleted.
2. **Click** on the **Delete off-line Record** button.
3. The delete confirmation prompt is displayed.
4. **Click** on the **Yes** button on the delete confirmation prompt.

**Example:** The selected record is removed from the list of records and from the local file system.

<!-- image -->

**Example:** Delete confirmation prompt. Clicking on No will abort deleting the record.

<!-- image -->

#### Exiting the Off-line Results Synchronizer Form

**Example:** To exit the **Off-line Results Synchronizer** form, **click** on the **Exit** button, or select **File| Exit** from the main menu, or press the escape key “ESC.” The Off-line Results Synchronizer form is closed and the MHA main form is displayed.

<!-- image -->

### Single-Instrument Administrator Functions

#### Orientation

The **Single-Instrument Administrator** is useful when the goal is to quickly and frequently administer only one instrument and there is no need to select from a list of other instruments or batteries.

Using the **Single-Instrument Administrator** bypasses the MHA Main form and the Instrument Administrator, proceeding directly to administering the instrument.

The **Single-Instrument Administrator** can only be invoked from the CPRS Tools menu and requires the Clinical Applications Coordinator to configure the Tools menu in VistA. See the Appendix E for instructions on how to add the name of the instrument to the CPRS Tools menu. **Example:** The CAGE as viewed from the **Single-Instrument Administrator** .

<!-- image -->

#### Main Menu

The Main Menu offers user functions in the context of the Single-Instrument form, such as tools and help.

#### Selected Patient Identification Label

The Selected Patient Identification label displays information about who is the currently-selected patient within MHA. All functions performed in the Single-Question form will apply to this patient.

#### Instrument’s Name

The Title Bar is a visual artifact that is used throughout MHA to display information about the context that applies to the current activity. In this case, the Title Bar displays the current instrument’s name.

#### List of Previously-Administered Tests

This is the list of all tests that have been administered to the selected patient. The list is also used for selecting which administration to process.

#### Report View

The Report View displays an administration report in textual form, based on the patient’s data stored in VistA for the selected administration.

#### The Navigation Tabs

These tabs are used to switch between report and graph/table view.

#### New button

The New button is used to start a new administration for the selected patient.

#### Edit Button

In the case that the selected administration is “editable”, based on how long ago it was administered, the Edit button becomes enabled and can be used to trigger editing of the selected administration.

#### Graph and Table

##### Graph View

**Example:** The **Graph View** displays a graphical representation of test data values over time.

<!-- image -->

##### Table View

The **Table View** represents the same data as the Graph View, except that it is in table format. The Table View also functions as a means for selecting which administrations and characteristics to represent on the graph.

**Example:** The **Splash** screen is shown upon start up.

<!-- image -->

#### Invoking the Single-Instrument Administrator from the CPRS Tools Menu

The only way to invoke the **Single-Instrument Administrator** is from the CPRS Tools menu. In addition to the Mental Health Assistant, individual instrument types may be added to the CPRS tools menu, from which the **Single-Instrument Administrator** is started for any particular instrument type. To configure single instruments on the CPRS Tools menu, The Clinical Applications Coordinator needs to add a set of parameters to the user’s VistA CPRS GUI Tools menu. See Appendix E for instructions.

In the following example, to start CAGE, start CPRS first. Then, once CPRS has settled, click on the

**Tools** menu item, followed by a click on the **CAGE** menu item.

If CAGE starts normally, the “splash” form is displayed briefly, followed by the **Single-Instrument Administrator** form, as shown below.

**Example:** The CAGE instrument is started from the CPRS Tools menu.

<!-- image -->

**Example:** The **Single-Instrument Administrator** form for the CAGE.

<!-- image -->

The **Single-Instrument Administrator** form is designed for a single instrument. This form combines the **Instrument Administrator** and the **Instrument Results Review** functions on a single form. All of the functions on this form have been described in previous sections of this manual; for example, how to copy and paste reports, graphs, how to print results, append comments to a report, and so forth.

#### Starting a New Administration

**Example:** To start a new administration, **click** on **File | New…**

<!-- image -->

**Example:** To start a new administration click on the **New** button.

<!-- image -->

Once a new administration is selected, the identifying information for the administration is gathered by the next form. This is the same information needed for the administration of any instrument. The format is the same as that used by the **Instrument Administrator** .

**Example:** Identifying information for an administration of the CAGE.

<!-- image -->

**Switching to MHA Main Menu**

**Example:** While the Single-Instrument Administrator initially bypasses MHA Main form, it offers a way to return to the Main form. **Click** on the **Action | MHA Main Menu** item.

**Click**

<!-- image -->

#### Editing an Existing Editable Administration

###### To edit an administration:

1. If the selected administration is editable the **Edit** button will be enabled.
2. Find and select an editable administration.
3. **Click** on the **Edit** button.
4. Administrations older than twenty-four hours are not editable.

**Example:** Editing an administration.

**Click**

<!-- image -->

#### Exiting the Single Instrument Administrator Form

**Example:** To exit the **Single-Instrument Administrator** form, **click** on **File | Exit** menu item. The Single Instrument Administrator form closes and the user is returned to the MHA Main form.

<!-- image -->

#### Glossary

The following terms are associated with the Mental Health Assistant 3 software application release:

| **TERMS**             | **DESCRIPTIONS**                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **API**               | Application Programmer Interface                                                                                                                                                                                                                                                                                                                                                                |
| **ASI**               | Addiction Severity Index                                                                                                                                                                                                                                                                                                                                                                        |
| **CLIENT**            | A computer that accesses shared network resources provided by another computer (called a server).                                                                                                                                                                                                                                                                                               |
| **CLOSE**             | Closes the window. If there are any changes that have not been saved, you will get a confirmation message asking you if you want to continue without saving; save before exiting; or cancel the close action and return to the window.                                                                                                                                                          |
| **CPRS**              | Computer Patient Record System                                                                                                                                                                                                                                                                                                                                                                  |
| **DBIA**              | Database Integration Agreement                                                                                                                                                                                                                                                                                                                                                                  |
| **desktop**           | The background on your monitor, on which windows, icon, and dialog boxes appear.                                                                                                                                                                                                                                                                                                                |
| **EDIT BOX**          | This is a box where the user can type in free text using the keyboard.                                                                                                                                                                                                                                                                                                                          |
| **Element Name**      | Globally unique descriptive name for the field.                                                                                                                                                                                                                                                                                                                                                 |
| **Enhancement**       | An ‘enhancement’ to an already existing Class I software package is the introduction of new or improved functionality.                                                                                                                                                                                                                                                                          |
| **FTP**               | File Transfer Protocol                                                                                                                                                                                                                                                                                                                                                                          |
| **Group**             | In User Manager, an account containing other accounts that are called members. The permissions and rights granted to a group are also provided to its members, which makes groups a convenient way to grant common capabilities to collections of user accounts. For Windows NT, groups are managed with User Manager. For Windows  NT Server, groups are managed with User Manager of Domains. |
| **GUI**               | Graphical User Interface.                                                                                                                                                                                                                                                                                                                                                                       |
| **HL7**               | Health Level 7                                                                                                                                                                                                                                                                                                                                                                                  |
| **IRM**               | Information Resources Management                                                                                                                                                                                                                                                                                                                                                                |
| **Length (LEN)**      | The maximum number of characters that one occurrence of the data field may occupy.                                                                                                                                                                                                                                                                                                              |
| **LIST BOX**          | Box that shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Selecting an entry from a list box requires either double clicking the entry or single  clicking the entry and pressing the spacebar.                                                                                                                             |
| **MHP**               | Mental Health Package                                                                                                                                                                                                                                                                                                                                                                           |
| **OK COMMAND BUTTON** | Adds the new entry after the data has been entered.                                                                                                                                                                                                                                                                                                                                             |
| **OPTION BUTTON**     | A small round button that appears in a dialog box. Within a group of  related option buttons, you can select only one button at time.                                                                                                                                                                                                                                                           |
| **PACKAGE**           | An icon that represents an embedded or linked object. When you choose the package, the application that was used to create the  object either plays the object (such as sound file) or opens and displays the object.                                                                                                                                                                           |

| **TERMS**                           | **DESCRIPTIONS**                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PASSWORD**                        | A unique string of characters that must be entered before a logon or an access is authorized. A password is a security measure used to restrict logons to user accounts and access to computer systems and resources. For Windows NT, a password for a user account can be  up to 14 characters long and is case-sensitive.                 |
| **PATH**                            | Specifies the location of a file within the directory tree. For example, to specify the path of a file named README.WRI located in the WINDOWS directory on drive C, you would type  **c:\windows\readme.wri.**                                                                                                                             |
| **PID**                             | Patient Identification                                                                                                                                                                                                                                                                                                                      |
| **PREVIOUS**                        | Previous enable the user to return to a previously answered question so the answer can be changed.                                                                                                                                                                                                                                          |
| **PSYCHOLOGIST**                    | Performs patient care duties in accordance with Clinical Privileges as assigned or granted by the appropriate governing committee in the area of Psychology and Mental Health. This may include individuals,  family and group counseling and psychotherapy, assertiveness, and other behavior training, etc.                               |
| **RADIO BUTTON**                    | Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. For example, MALE or FEMALE may be offered as choices through two  radio buttons. Click in the button to select it.                                                                                      |
| **RIGHT MOUSE BUTTON or SHIFT F10** | You may click the right mouse button or press Shift F10 for a popup box of menu items.                                                                                                                                                                                                                                                      |
<!-- rpc-table -->
| **RPC BROKER**                      | Remote Producers Call Broker                                                                                                                                                                                                                                                                                                                |
<!-- rpc-table -->
| **RPC**                             | Remote Producers Call, a message-passing facility that allows a distributed application to call services available on various computers in a network. Used during remote administration of computers.                                                                                                                                       |
| **Save to File (Save AS)**          | This is a standard feature of Microsoft applications where the user can type the name of the file to be saved. The user can also define the drive and directory where the file is to be saved. In some cases  the file name presented in the edit box is sufficient and the user merely needs to click on the “Ok” button to save the file. |
| **SHARE**                           | To make resources, such as directories, printers, and ClipBook pages, available to network users.                                                                                                                                                                                                                                           |
| **Status Bar**                      | A line of information related to the application running in the window. Usually located at the bottom of a window. Not all windows have a  status bar.                                                                                                                                                                                      |
| **Task List**                       | A window that shows all running applications and enables you to switch between them. You can open Task List by choosing Switch To from the Control menu or by pressing CTRL=ESC.                                                                                                                                                            |
| **Tab Key**                         | Use the TAB key or the mouse to move between fields. Do not use the RETURN key. The RETURN key is usually reserved for the  default command button or action (except in menu fields).                                                                                                                                                       |
| **TCP/IP**                          | Transmission Communication Protocol/Internet Protocol                                                                                                                                                                                                                                                                                       |
| **TEXT BOX**                        | Type the desired characters into the edit box. The selected entry will not be effective until you tab off or exit from the text box.                                                                                                                                                                                                        |

| **TERMS**           | **DESCRIPTIONS**                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TOOLBAR**         | A series of shortcut buttons providing quick access to commands. Usually located directly below the menu bar. Not all windows have a toolbar.                                                                                                                                                                                                                        |
| **TRANSPORT LAYER** | The fourth layer of the OSI model. It ensures that messages are delivered error-free, in sequence, and with no losses or duplications. This layer repackages messages for their efficient transmission over the network. At the receiving end, the Transport layer unpacks the  message, reassembles the original messages, and sends an acknowledgement of receipt. |
| **UID**             | Unique Identifier                                                                                                                                                                                                                                                                                                                                                    |
| **VA**              | Veterans Administration                                                                                                                                                                                                                                                                                                                                              |
| **VHA**             | Veterans Health Administration                                                                                                                                                                                                                                                                                                                                       |
| **VAMC**            | Department of Veterans Affairs Medical Center                                                                                                                                                                                                                                                                                                                        |
| **VERA**            | Veterans Equitable Resource Allocation                                                                                                                                                                                                                                                                                                                               |
| **VISN**            | Veterans Integrated Service Network                                                                                                                                                                                                                                                                                                                                  |
| **VistA**           | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                                      |
| **WORKSTATION**     | In general, a powerful computer having considerable calculating and graphics capability. For Windows NT, computers running the windows NT operating systems are called workstations, as distinguished from computers running Windows NT Server, which are called servers.                                                                                            |

### Glossary of GUI components used in MHA

Each component/term contains a sample screen capture of how each component displays in MHA following the component/term. A description of each item is provided in the second column of the table.

| **Component/Terms**                         | **Descriptions**                                                                                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple-Selection List Box  <!-- image --> | A Multiple-Selection List Box permits selection of one or more choices from a list of choices. Simply click on the little boxes next to the selection’s text and a check- mark symbol appears in the box, indicating your selection. |

| **Component/Terms**                       | **Descriptions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drop-Down Combo Box  <!-- image -->       | A Drop-Down Combo Box contains a “hidden” list that is not visible until the user clicks on the button with the down-arrow icon. Then, the list appears and an item can be selected from the list. Click on the item that you wish to select. Drop-Down Combo Boxes also accept typed text in the component’s Text Box. Some Drop-Down Combo Boxes are used to display data directly from VistA files, such as a list of staff members.                                                                                                  |
| Drop-Down List Box  <!-- image -->        | A Drop-Down List Box contains a “hidden” list that is not visible until the user clicks on the button with the down-arrow icon. Then, the list appears and an item can be selected from the list. Click on the item that you wish to select. Unlike Drop-Down  Combo Boxes, no text can be entered into the Text Box part of the component.                                                                                                                                                                                              |
| Text Box  <!-- image -->                  | Text Boxes allow for typing a relatively small amount of text—generally, the length of a single line of text, or less. Normally, Text Boxes accept any text characters typed into them. However, in some cases, Text Boxes are restricted to accept only a pre-defined group of characters. For instance, only accepting integer or  currency values.                                                                                                                                                                                    |
| Date-Picker  <!-- image -->               | A Date-Picker component offers two ways of entering date information. The first is to type in the date in the Text Box part of the component while observing the displayed format. Another way to pick a date is to click on the button with the down-arrow icon, which triggers the display of the visual calendar. By default the calendar displays the current month. Other dates can be navigated to by clicking on the name of the month, the year, and the side- arrows. To pick a date, click on the day  number on the calendar. |
| Single-Selection List Box  <!-- image --> | A Single-Selection List Box displays all available choices at once, from which only one of the mutually-exclusive selections may be made.                                                                                                                                                                                                                                                                                                                                                                                                |

| **Component/Terms**                          | **Descriptions**                                                                                                                                                                                                                                                                                       |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Masked Text Box  <!-- image -->              | A Masked Text Box is a special kind of Text Box in that it adds pre-configured formatting to the data entered into the component. In this example, the “( ) –“ formatting elements were correctly placed and automatically added to the phone number as the user typed in only the  numbers.           |
| Multiple-Line Text Box  <!-- image -->       | A Multiple-Line Text Box functions in the same manner as a single-line Text Box, but provides enough space for entering large amounts of text.                                                                                                                                                         |
| Spin Box  <!-- image -->                     | Spin Boxes provide for the quick entry and verification of integer data. The buttons with the up and down arrowheads respectively increase or decrease the value of the displayed integer. Additionally, an integer value can be typed into the Text  Box holding the integer value.                   |
| Option Buttons (Radio Group)  <!-- image --> | Option Buttons display all available choices at once, from which one of the mutually-exclusive selections may be made. This is the most commonly-used component in Mental Health Assistant. To make a selection, click on one of the white circles, which will then display a black dot in its center. |
| Slider (Track bar)  <!-- image -->           | A Slider is a visual way of displaying a range from which to select a single value. The accompanying labels offer information about what the range limits mean.                                                                                                                                        |
| Progress Indicator  <!-- image -->           | Indicates the amount of progress transpired during time-consuming events.                                                                                                                                                                                                                              |
| Command Button  <!-- image -->               | A button that executes a specific function when pressed.                                                                                                                                                                                                                                               |

| **Component/Terms**         | **Descriptions**                                           |
|-----------------------------|------------------------------------------------------------|
| Menu Button  <!-- image --> | A button with more than one choice                         |
| Tabs  <!-- image -->        | A navigation method similar to tabs on a writing notebook. |

## Appendix A

This is a list of shortcut keys used by the Mental Health Assistant (MHA), organized by the form that has focus.

**Shortcut Keys**

| **Main Menu**                |                                  |
|------------------------------|----------------------------------|
| Alt-F                        | **File Menu**                    |
| S                            | Select Patient                   |
| U                            | Upload Results                   |
| X                            | Exit, close application          |
| Alt-T                        | Tools Menu                       |
| M                            | Metric Instrument Reviews        |
| O                            | Options                          |
| Alt-H                        | Help Menu                        |
| O                            | Online Support                   |
| A                            | About                            |
| Alt-I or I                   | Instrument Administrator         |
| Alt-R or R                   | Instrument Results Review        |
| Alt-A or A                   | Addiction Severity Index Manager |
| Alt-F4                       | Exit, close application          |
| **Instrument Administrator** |                                  |
| Alt-F                        | **File Menu**                    |
| S                            | Select Patient                   |
| P                            | Print a blank instrument         |
| X                            | Exit                             |
| Alt-T                        | Tools Menu                       |
| M                            | METRIC Instrument Reviews        |
| B                            | Battery Wizard                   |
| O                            | Options                          |
| Alt-H                        | Help Menu                        |
| I                            | Instrument Description           |
| O                            | Online Support                   |
| A                            | About                            |
| Alt-B                        | Instruments Ordered By           |
| Alt-I                        | Interviewer                      |
| Alt-D                        | Date of Administration           |
| Alt-L                        | Visit Location                   |

| Alt-W                         | Link with consult                   |
|-------------------------------|-------------------------------------|
| Alt-A                         | Available Instruments and Batteries |
| Alt-C                         | Instruments Chosen                  |
| Alt-O                         | One Question at a Time              |
| Alt-Q                         | All Questions at Once               |
| Alt-P                         | Patient Entry                       |
| Alt-S                         | Staff Entry                         |
| ESC                           | Exit (returns to Main Menu)         |
| **Instrument Results Review** |                                     |
| Alt-F                         | **File Menu**                       |
| S                             | Select Patient                      |
| A                             | Save As sub-menu                    |
|                               | R	Report                                     |
|                               | T	Table                                     |
|                               | G	Graph                                     |
| P                             | Print sub-menu                      |
|                               | R	Report                                     |
|                               | T	Table                                     |
|                               | G	Graph                                     |
| X                             | Exit                                |
| Alt-E                         | **Edit Menu**                       |
| C                             | Copy sub-system                     |
|                               | R	Reports                                     |
|                               | T	Table                                     |
|                               | G	Graph                                     |
| Alt-V                         | **View Menu**                       |
| R                             | Reports                             |
| G                             | Graph and Table                     |
| S                             | Special Results                     |
| V                             | Show values on graph                |
| Alt-T                         | **Tools Menu**                      |
| A                             | Append Comments                     |
| D                             | Delete administration               |
| M                             | METRIC Instrument Reviews           |
| S                             | Special Results Wizard              |
| O                             | Options                             |
| Alt-H                         | **Help Menu**                       |
| O                             | Online Support                      |
| A                             | About                               |
| Alt-R                         | Reports                             |
| Alt-G                         | Graph and Table                     |
| Alt-S                         | Special Results                     |
| ESC                           | Exit (returns to Main Menu)         |

| **About**                  |                                                            |
|----------------------------|------------------------------------------------------------|
| Alt-O                      | OK, exit                                                   |
| ESC                        | Exit                                                       |
| **Battery Wizard**         |                                                            |
| Alt-F                      | **File Menu**                                              |
| N                          | New                                                        |
| R                          | Rename                                                     |
| D                          | Delete                                                     |
| X                          | Exit                                                       |
| Alt-H                      | **Help Menu**                                              |
| I                          | Instrument Description                                     |
| O                          | Online Support                                             |
| A                          | About                                                      |
| Alt-A                      | Available Instruments and Batteries                        |
| Alt-N                      | Name of Battery                                            |
| Alt-I                      | Instrument in Battery                                      |
| Alt-S                      | Save                                                       |
| ESC                        | Exit                                                       |
| **One Question at a Time** |                                                            |
| Alt-F                      | **File Menu**                                              |
| B                          | Print blank                                                |
| C                          | Cancel                                                     |
| Alt-V                      | View Menu  *Varies based on instruments being administered |
| Alt-T                      | **Tools Menu**                                             |
| M                          | METRIC Instrument Reviews                                  |
| O                          | Options                                                    |
| Alt-H                      | **Help Menu**                                              |
| O                          | Online Support                                             |
| A                          | About                                                      |
| Alt-P                      | Prior Question                                             |
| Alt-Q                      | Next Question                                              |
| Alt-R                      | Review Answers                                             |
| Alt-C                      | Cancel                                                     |
| Alt-N                      | Finish                                                     |
| Alt-U                      | Use Speed Tab                                              |
| ESC                        | Exit                                                       |

| **Battery Wizard**         |                                                                     |
|----------------------------|---------------------------------------------------------------------|
| Alt-F                      | **File Menu**                                                       |
| N                          | New                                                                 |
| R                          | Rename                                                              |
| D                          | Delete                                                              |
| X                          | Exit                                                                |
| Alt-H                      | Help Menu                                                           |
| I                          | Instrument Menu                                                     |
| O                          | Online Support                                                      |
| A                          | About                                                               |
| Alt-A                      | Available Instruments and Batteries                                 |
| Alt-N                      | Name of Battery                                                     |
| Alt-I                      | Instruments in Battery                                              |
| Alt-S                      | Save                                                                |
| ESC                        | Exit                                                                |
| **One Question at a Time** |                                                                     |
| Alt-F                      | **File Menu**                                                       |
| B                          | Print Blank                                                         |
| C                          | Cancel                                                              |
| Alt-V                      | **View Menu**  *Menu varies based on Instruments being administered |
| Atl-T                      | **Tools Menu**                                                      |
| M                          | METRIC Instrument Review                                            |
| O                          | Options                                                             |
| Alt-H                      | **Help**                                                            |
| O                          | Online Help                                                         |
| A                          | About                                                               |
| Alt-P                      | Prior Question                                                      |
| Alt-Q                      | Next Question                                                       |
| Alt-R                      | Review Question                                                     |
| Alt-C                      | Cancel                                                              |
| Alt-N                      | Finish                                                              |
| Alt-U                      | Use Speed Tab                                                       |
| ESC                        | Exit                                                                |
| **Review Answers**         |                                                                     |
| Alt-F                      | **File Menu**                                                       |
| X                          | Exit                                                                |
| Alt-V                      | View Menu  *Menu varies based on Instruments being administered     |
| Alt-T                      | **Tools Menu**                                                      |
| M                          | METRIC Instrument Reviews                                           |

| O                        | Options                        |
|--------------------------|--------------------------------|
| Alt-H                    | **Help Menu**                  |
| O                        | Online Support                 |
| A                        | About                          |
| Alt-C                    | Cancel                         |
| Alt-N                    | Finish                         |
| Alt-U                    | Use Speed Tab                  |
| ESC                      | Exit                           |
| **User Preferences**     |                                |
| Alt-F                    | **Font tab**                   |
| Alt-O                    | CPRS Font                      |
| Alt-W                    | Windows Font                   |
| Alt-N                    | New Font                       |
| Alt-H                    | **Highlight Color Tab**        |
| Alt-M                    | **Miscellaneous tab**          |
| Alt-V                    | Provide visual feedback        |
| Alt-R                    | Screen reader                  |
| Alt-S                    | Speed tab                      |
| Alt-I                    | Display image                  |
| Alt-O                    | Maintain original font         |
| Alt-U                    | **Menu tab**                   |
| Alt-C                    | Cancel                         |
| Alt-D                    | Done                           |
| ESC                      | Exit                           |
| **Append Test Comments** |                                |
| Alt-F                    | **File Menu**                  |
| S                        | Save                           |
| X                        | Exit                           |
| Alt-H                    | **Help Menu**                  |
| I                        | Instrument Description         |
| O                        | Online Support                 |
| A                        | About                          |
| Alt-A                    | Available Instruments          |
| Alt-I                    | Instruments in Special Results |
| Alt-S                    | Save                           |
| ESC                      | Exit                           |

| **ASI Main Menu**   |                              |
|---------------------|------------------------------|
| Alt-F               | **File Menu**                |
| N                   | New ASI sub-menu             |
|                     | F	Full                              |
|                     | L	Lite                              |
|                     | U	Follow-up                              |
| S                   | Select Patient               |
| A                   | Save As sub-menu             |
|                     | R	Report/Table                              |
|                     | G	Graph                              |
| P                   | Print sub-menu               |
|                     | R	Report/Table                              |
|                     | G	Graph                              |
| X                   | Exit                         |
| Alt-E               | **Edit Menu**                |
| C                   | Copy sub-menu                |
|                     | R	Report/Table                              |
|                     | G	Graph                              |
|                     | A	ASI                              |
| Alt-V               | **View Menu**                |
| N                   | Narrative Report             |
| I                   | Item Report                  |
| R                   | Item Trends                  |
| D                   | Domain Scores                |
| Alt-T               | **Tools Menu**               |
| O                   | Options                      |
| Alt-H               | **Help Menu**                |
| O                   | Online Support               |
| A                   | About                        |
| ESC                 | Exit (returns to Main Menu)  |
| **ASI Data Entry**  |                              |
| Alt-F               | **File Menu**                |
| E                   | Exit                         |
| Alt-T               | **Tools Menu**               |
| O                   | Options sub-menu             |
|                     | H	Highlight Color                              |
|                     | T	Speed Tab                              |
|                     | S	Show hints                              |
| D                   | Default Window Size/Position |
| Alt-F4              | Exit                         |
| ESC                 | Exit                         |

| F1                  | Help for the highlighted item       |
|---------------------|-------------------------------------|
| Alt-H               | **Help Menu**                       |
| C                   | Contents                            |
| I                   | Index                               |
| O                   | Online Support                      |
| A                   | About                               |
| Alt-A               | Family History Section              |
| Alt-D               | Drug/Alcohol Use Section            |
| Alt-E               | Employment/Support Section          |
| Alt-G               | General Information Section         |
| Alt-I               | Spiritual Comments Section          |
| Alt-L               | Legal Status Section                |
| Alt-M               | Medical Status Section              |
| Alt-P               | Psychiatric Status Section          |
| Alt-R               | Leisure Comments Section            |
| Alt-S               | Family/Social Relationships Section |
| **ASI Options**     |                                     |
| Alt-C               | Cancel                              |
| Alt-D               | Done                                |
| ESC                 | Exit                                |
| **ASI Signatures**  |                                     |
| Alt-C               | Cancel                              |
| Alt-O               | OK                                  |
| ESC                 | Exit                                |
| **ASI Termination** |                                     |
| Alt-R               | Return to ASI                       |
| Alt-E               | Exit                                |
| Alt-F               | Finish later                        |
| Alt-S               | Save and Sign                       |
| Alt E               | **Edit Menu**                       |
| C                   | Copy sub-menu                       |
| G                   | Graph                               |
| T                   | Table                               |
| Alt-V               | View Menu                           |
| S                   | Show values on graph                |
| Alt-A               | **Action Menu**                     |
| S                   | Save New Rating                     |
| R                   | Mark Rating “Entered in Error”      |
| Alt-T               | **Tools Menu**                      |
| O                   | Options                             |

| Alt-H                             | **Help Menu**                                           |
|-----------------------------------|---------------------------------------------------------|
| O                                 | Online Support                                          |
| A                                 | About                                                   |
| C                                 | Copyright Info                                          |
| Alt-R                             | Mark Rating “Entering in Error” or Change Delete Rating |
| Alt-D                             | Delete Rating                                           |
| Alt-D                             | Evaluation Date                                         |
| Alt-S                             | Save New Rating                                         |
| ESC                               | Exit (returns to Main Menu)                             |
| **Off-line Results Synchronizer** |                                                         |
| Alt-F                             | **File Menu**                                           |
| E                                 | Exit                                                    |
| Alt-H                             | **Help Menu**                                           |
| O                                 | Online Support                                          |
| A                                 | About                                                   |
| Alt-S                             | Search for                                              |
| Alt-G                             | Go (Start search)                                       |
| Alt-D                             | Delete Off-Line record                                  |
| Alt-U                             | Upload                                                  |
| Alt-X                             | Exit                                                    |

## Appendix B

### How to co-sign a progress note generated by MHA

The following conditions are needed to generate a co-signer in TIU notes:

1. A progress note needs to be generated. (Some instruments do not generate progress notes.)
2. The person who is using MHA must be someone who needs a co-signer, like a student.

When an instrument is completed in MHA, and the two conditions are met, this dialog will appear:

<!-- image -->

Select the person to co-sign the progress note from the drop-down list presented in the combo box. Once selected, press the button to either save the standard progress note, or edit the progress note before saving it.

## Appendix C

### How to Remove Patient Data That Was Entered In Error: Vista Menu Instructions

There are two methods to remove the data from an instrument’s administration. The first uses the MHS Manager Functions in VistA and the second is available in MHA’s **Instrument Review Results** form, described previously. In either case, this function can be performed only by individuals who have access to the MHS Manager Functions in VistA, usually a Clinical Application Coordinator (CAC).

**IMPORTANT:** Data removed by either method will only remove the results of the administration of the instrument. Any progress notes, or consult notes, etc., will not be removed. Here are the steps to follow in the “roll-and-scroll” version (the user responses are shown in red):

<!-- image -->

*** MENTAL HEALTH ***

MHS MANAGER FUNCTIONS

1. Inpatient Features management functions...
2. Mental Health System site parameters...
3. MHA2 Psych test utilities...
4. Move crisis notes and messages
5. Seclusion/Restraint Management Utilities...
6. Decision Tree Shell
7. MHA3 Utilities...

Select MHS Manager Option: **7 MHA3 Utilities**

*** Mental Health *** MHA3 Utilities

1. Print Test Form
2. Detailed Definition
3. Delete Patient Data
4. Stop/Re-Start Progress Notes for an Instrument
5. Exempt Test
6. Test Usage
7. XML Output
8. MHA3 HL7 Utilities...

Select MHA3 Utilities Option: 3 Delete Patient Data

<!-- image -->

Delete Patient Data

Select PATIENT NAME:	MHPATIENT,ONE	*SENSITIVE*	*SENSITIVE* NO	EMPLOYEE

***WARNING***

***RESTRICTED RECORD***

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

- This record is protected by the Privacy Act of 1974 and the Health	*
- Insurance Portability and Accountability Act of 1996. If you elect	*

- to proceed, you will be required to prove you have a need to know.	*
- Accessing this patient is tracked, and your station Security Officer *
- will contact you for your justification.	*

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Do you want to continue processing this patient record? No// Y (Yes) Message(s) are on file for MHPATIENT,ONE

Last message was entered on DEC 15, 1992

Enter RETURN to continue or '^' to exit:

Delete MHA3 data? No// YES

PHQ-2 on JAN 07, 2009@09:56:27 by MHPROVIDER,ONE

Delete? No// YES

Are you sure? No// YES ***Deleted

AUDC on NOV 26, 2008@14:28 by MHPROVIDER,ONE

Delete? No// ^

## Appendix D

Some sites have reported difficulty installing SecureDesktop as the Windows registry is blocked by McAfee HIPS. Uninstalling HIPs allowed the installation to occur normally.

**SecureDesktop &amp; Screen Pass: How to correct Windows-Registry problems.**

According to the Birch Grove Software site:

“Screen Pass is a screen locking system for Windows® that extends the capability of the standard workstation lock and gives network administrators complete control over idle workstations.

With Screen Pass, network administrators can enforce screensaver password use, screensaver timeout, and screen saver selection. Advanced features include automatic logout, automatic shutdown, customizable administrator override, and auditing of all logon/logoff and lock/unlock events.

Intended primarily for workstations connected to Novell Netware or Microsoft networks, Screen Pass can be distributed and managed remotely with or without group policy. The central management feature makes Screen Pass ideal for small, medium, and large networks - anywhere that security of idle workstations is a concern.”

Screen Pass installs its own version of a gina.dll and it may take precedence over the one used by Secure Desktop. If SecureDesktop does operate properly these changes may be necessary in the Windows Registry:

HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVer **s** ion\Winlogon\GinaDLL=dwlgina2.dll

HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GinaDLL\_ScreenPass=msgina2.dll

See Remedy Ticket # HD0000000278953.

**Secure desktop: How To Correct Dwlgina2.Dll Problems**

A dwlGina2.dll error problem may occur when a non-administrator uninstalls MHA without an administrator first de-activating SecureDesktop.

Here is how to fix it:

1. Turn off defective PC, if on.
2. Start the PC and Windows in SAFE mode.
3. Logon as Administrator.
4. Find the file YS\_MHA\_SD\_UNINSTALLGINA.exe. These files are typically found at C:\Program Files\Vista\YS\MHA3.
5. Run YS\_MHA\_SD\_UNINSTALLGINA.exe. Click **Yes** , to uninstall it.
6. Reboot in normal mode.

If this doesn’t work, then modify step five by first finding and running YS\_MHA\_SD\_INSTALLGINA.exe. Click **Yes** , to install it. Then follow the remainder of step five.

## Appendix E

### Setting up VistA MHA3 on CPRS GUI Tools Menu for SecureDesktop

**Setting up VistA MHA3 on CPRS GUI Tools Menu for SecureDesktop**

If your site uses an APPLICATION SERVER for access MHA3, you will need to create a 2 nd instance under CPRS tools. SecureDesktop MUST access MHA3 from the LOCAL MACHINE that SecureDesktop is loaded. You cannot use MHA3 from an application server for SecureDesktop

**Example:** Setting up VistA MHA3 on the CPRS Tools menu for SecureDesktop, GUI Parameters [ORW PARAM GUI]

Select GUI Parameters Option: **tm GUI&lt;ENTER&gt;** Tool Menu Items CPRS GUI Tools Menu may be set for the following: **&lt;ENTER&gt;**

1. User USR [choose from NEW PERSON]
2. Location LOC [choose from HOSPITAL LOCATION] 3 Division DIV [REGION 5]

4 System SYS [OEX.ISC-SLC.VA.GOV]

Enter selection: **1&lt;ENTER&gt;** User NEW PERSON

Select NEW PERSON NAME: **MHPROVIDER,ONE&lt;ENTER&gt;** CPF

------------- Setting CPRS GUI Tools Menu for User: MHPROVIDER,ONE----------

Sequence: **? &lt;ENTER&gt;**

Enter the sequence in which this menu item should appear. Select Sequence: **2**

Are you adding 2 as a new Sequence? Yes// **&lt;ENTER&gt; YES**

Sequence: 2// **&lt;Enter&gt;**

Name=Command: **MHA3\_Patient Entry=C:\Progra~1\Vista\YS\MHA3\YS\_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF**

From the previous example, adjust according to your own system’s settings, such as New Person Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered exactly as shown, in a single line—no line-breaks allowed, including all the % parameters that follow the filename and path to the MHA3 executable file.

**ALL five parameters must be included as shown above, in the precise order in which they are found in the example.** Here is what the Name=Command line should look like:

**Example:** MHA3\_Patient Entry=C:\Progra~1\Vista\YS\MHA3\YS\_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine. (Sometimes when cutting and pasting, unseen control characters can be included in the text and will cause the command line to malfunction.)

**The Entry parameter must be set to the exact directory path to the YS\_MHA.exe.** The exact directory path will be different between Windows XP computers and Windows 7 computers.

For a Windows XP computer the Entry parameter would be: Entry=C:\Prog~1\Vista\YS\MHA3\YS\_MHA.exe

For a Windows 7 computer the Entry parameter would be: Entry=”C:\Program Files (x86)\Vista\YS\MHA3\YS\_MHA.exe”

The directory path must be enclosed in quotes due to the embedded spaces in the directory path.

After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “MHA3\_Patient Entry”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS and if SecureDesktop is installed on that machine, the Patient Entry Button will be enabled.

## Appendix F

### How to Add the Name of an Instrument to the CPRS Tools Menu

This is done in VistA; an example for the AUDC is provided below:

Select GUI Parameters Option: **tm GUI&lt;ENTER&gt;** Tool Menu Items CPRS GUI Tools Menu may be set for the following: **&lt;ENTER&gt;**

1. User USR [choose from NEW PERSON]
2. Location LOC [choose from HOSPITAL LOCATION]
3. Division DIV [REGION 5]
4. System SYS [OEX.ISC-SLC.VA.GOV]

Enter selection: **1&lt;ENTER&gt;** User NEW PERSON

Select NEW PERSON NAME: **MHPROVIDER,ONE&lt;ENTER&gt;** CPF

------------- Setting CPRS GUI Tools Menu for User: MHPROVIDER,ONE----------

Sequence: **? &lt;ENTER&gt;**

Enter the sequence in which this menu item should appear. Select Sequence: **2**

Are you adding 2 as a new Sequence? Yes// **&lt;ENTER&gt; YES**

Sequence: 2// **&lt;Enter&gt;**

Name=Command: **AUDC =C:\Progra~1\Vista\YS\MHA3\YS\_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF AUDC**

## Appendix G

### Using Instrument Exchange

If a new or updated Mental Health instrument needs to be sent to your site, MHA Instrument Exchange provides a mechanism that allows you to load and install the instrument. It operates very similarly to Clinical Reminder Exchange. When you select Instrument Exchange from the MHA3 Utilities menu, you will see an interface that looks something like this:

<!-- image -->

The following screens provide a brief overview of how the available actions operate. Should an instrument need to be updated, specific instructions will be provided at that time.

**Instrument Exchange Actions**

***Create New Entry, Rebuild Entry, Create Host File*** are reserved for use by MHA developers. These options are used in the master account that contains instrument specifications (similar to the national reminders account).

***Load Host File*** prompts for a file name that contains instrument specifications in exchange format. These are saved in the MH INSTRUMENT EXCHANGE file.

<!-- image -->

***Load from URL*** prompts for an HTTP address that contains instrument specifications in exchange format. The file is retrieved and saved in the MH INSTRUMENT EXCHANGE file.

<!-- image -->

***Trial Install*** performs a dry run install of an instrument exchange entry. No database changes are actually made, but the changes that would be made are displayed.

<!-- image -->

***Install Exchange Entry*** uses the instrument specification stored in an exchange entry and updates the MHA database to match the specification. In this example, one record is updated.

<!-- image -->

***Delete Entry*** removes the selected entry from the MH INSTRUMENT EXCHANGE file.

<!-- image -->

***Browse Specification*** allows you to view the exchange entry. This is primarily for use by programmers.

<!-- image -->