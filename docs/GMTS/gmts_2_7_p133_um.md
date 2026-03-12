---
app_name: 'CPRS: Health Summary (GMTS)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMTS
patch: null
patch_gap: null
section: ''
source_file: gmts_2_7_p133_um.docx
status: draft
title: Chapter 1 – Introduction
---

**Health Summary**

**User Manual**

<!-- image -->

**Version 2.7**

**March 2020**

**Department of Veterans Affairs (VA)**

**Office of Information and Technology (OIT)**

**Preface**

The Health Summary package integrates currently available patient data from Veterans Health Administration Information Systems Architecture (VistA) packages into patient health summaries that can be printed or viewed online.

The *Health Summary User Manual* provides information for three types of users.

Health Summary users who only need to view health summaries on a screen or in printed form. Chapter 2, “Using Health Summary,” describes these basic features.

Health Summary users who can display health summaries and also create customized health summary types for use by others. Chapter 3, “Advanced Features,” describes how to create health summary types.

Health Summary Coordinators who can use all the functions available for other user types, as well as the special Health Summary package features for batch printing nightly summaries and creating customized health summary types. Chapter 4, “Managing Health Summary,” describes batch printing and other management functions.

Revision History

| **Revision Date**   | **Page or Chapter**               | **Description**                                                                                                                                                                                                                                                                                                                          | **Author**   |
|---------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 03/16/2020          | Title, i, ii, Appendix C, all     | GMTS*2.7*133:  Removed the last line of the Prefix that called out the most current patch  Moved the section,  **New Features in Health Summary**  , into  **Appendix C**  for historical purposes  Updated the Title page, Revision History, and Footers                                                                                | REDACTED     |
| 12/31/2020          | Title, i, 37, 49, 71, 72, 81, 156 | GMTS*2.7*129:  Updated Title, TOC, and footers  Removed instances of Social Work                                                                                                                                                                                                                                                         | REDACTED     |
| 06/14/2019          | i, 2, 36, 158, 159                | GMTS*2.7*125:  Added description of GMTS*2.7*125.  Appendix A—Health Summary Component Description List, added descriptions and acronyms for PHARMACY ORDERALE ITEM, VA DRUG CLASS components, RXDC and RXOI Sample Reports.  Updated Title page, TOC, and footers.                                                                      | REDACTED     |
| 09/14/2018          | 2, 36, 41, 69                     | Updated title page, and footers. Added description of GMTS*2.7*94. Added an example of the Check Medication Reconciliation menu item. Added an Allergies/ADRs that uses the MRT5 item in an example.                                                                                                                                     | REDACTED     |
| 11/03/2017          | i, i, ii, iv, 11, 13, 14, and 15  | Updated title page, preface, and footers. Added description of GMTS*2.7*120.                                                                                                                                                                                                                                                             | REDACTED     |
| 09/08/2015          | 3, 22, 133-148                    | Updated title page and footers.  Added description of GMTS*2.7*111. Corrected spacing and typos and removed ICD-9 references for Admission/Discharge, ADT History Expanded, Discharge Diagnosis, ICD Procedures, ICD Surgeries, Outpatient Diagnosis, and Outpatient Encounter in Appendix A, Health Summary Component Description List. | REDACTED     |
| August 2014         | 3, 22                             | Added description of GMTS*2.7*110.                                                                                                                                                                                                                                                                                                       | REDACTED     |
| June 2014           | N/A                               | Edits per Customer Support review for GMTS*2.7*101.                                                                                                                                                                                                                                                                                      | REDACTED     |
| February 2014       | N/A                               | Added description of GMTS*2.7*101 and example.                                                                                                                                                                                                                                                                                           | REDACTED     |
| December 2013       | 3, 22, 103                        | Added description of GMTS*2.7*107and notes describing possible error messages.                                                                                                                                                                                                                                                           | REDACTED     |
| Sept 2012           | iv                                | Edits per Release Coordinators for GMTS*2.7*104.                                                                                                                                                                                                                                                                                         | REDACTED     |
| June 2012           | iv                                | Updated MH Suicide PRF Hx component description for GMTS*2.7*104.                                                                                                                                                                                                                                                                        | REDACTED     |
| May 2012            | iv                                | Added descriptions of GMTS*2.7*104 and new component, MH Suicide PRF Hx                                                                                                                                                                                                                                                                  | REDACTED     |
| November 2011       | 11                                | Added description of GMTS*2.7*102                                                                                                                                                                                                                                                                                                        | REDACTED     |
| August 2011         | 24                                | Added description of GMTS*2.7*88                                                                                                                                                                                                                                                                                                         | REDACTED     |
| April 2011          | 3-4, 17                           | Added description of GMTS*2.7*92.                                                                                                                                                                                                                                                                                                        | REDACTED     |
| November 2010       | 13                                | Added descriptions of recent patches, including GMTS*2.7*90, 91, and 93.                                                                                                                                                                                                                                                                 | REDACTED     |
| August 2008         | Appendix A                        | Corrected spelling and added note to Health Factors & Health Factors Select (GMTS*2.7*82)                                                                                                                                                                                                                                                | REDACTED     |
| August 2007         | 13                                | Added description of changes for printing sensitive data, per patch 85, test v8                                                                                                                                                                                                                                                          | REDACTED     |
| April 2007          | 48, 89, 107                       | Added description of changes for printing sensitive data, per patch 85                                                                                                                                                                                                                                                                   | REDACTED     |
| June 2006           | Page 75                           | Added section on using Health Summary in CPRS GUI                                                                                                                                                                                                                                                                                        | REDACTED     |
| May 2006            | Page 49, and throughout manual.   | Description of changes per patch 81.                                                                                                                                                                                                                                                                                                     | REDACTED     |
| May 2006            | Appendix A                        | Updated Components Description list.                                                                                                                                                                                                                                                                                                     | REDACTED     |
| Oct-Dec 2004        | Throughout manual.                | Patient name and SSN and provider name updates to comply with Patient privacy SOP.                                                                                                                                                                                                                                                       | VA OI&T      |
| December 2002       | Throughout manual.                | Changes based on review by NVS Release Manager.                                                                                                                                                                                                                                                                                          | VA OI&T      |
| October 2002        | Throughout manual.                | Revisions for changes made by patches 56 and 58                                                                                                                                                                                                                                                                                          | VA OI&T      |
| February 2002       | Pg 9                              | Description of changes provided with patch 49                                                                                                                                                                                                                                                                                            | VA OI&T      |
| January 2002        | Pg 26, 92                         | New menu of options enabling managers to control HS types on the reports tab in CPRS                                                                                                                                                                                                                                                     | VA OI&T      |

Table of Contents

Chapter 1: Introduction	1

Health Summary Menus	3

Health Summary Overall Menu [GMTS MANAGER]	3

How to Use This Manual	7

Chapter 2: Using Health Summary – Basic Features	8

Health Summary Menu	9

1. Patient Health Summary Option	10

2. Ad Hoc Health Summary Option	14

3. Range of Dates Patient Health Summary	23

4. Visit Patient Health Summary	24

5. Hospital Location Health Summary	28

6. Information Menu	30

Inquire about a Health Summary Type	30

List Health Summary Types	32

Inquire about a Health Summary Component	33

List Health Summary Components	34

List Health Summary Component Descriptions	37

7.  CPRS Reports Tab “Health Summary Types List” Menu	39

Using Health Summary in CPRS	40

Chapter 3: Advanced Features	44

1.  Health Summary Components	45

Brief, Selected, and Cumulative Selected Components	45

2.  Health Summary Types	47

3.   Health Summary Objects	51

4.  Build Health Summary Type Menu	51

Create/Modify Health Summary Type	53

Delete Health Summary Type	59

Health Summary Objects Menu	60

Create/Modify Health Summary Object	60

Inquire about a Health Summary Object	65

Test a Health Summary Object	65

Delete Health Summary Object	66

Export/Import a Health Summary Object	67

Export a Health Summary Object	67

Mailman Message Sent	68

Import/Install a Health Summary Object	68

Unpack Mailman Message	70

Import/Install Health Summary Object	71

Print Health Summary	72

5.  User Preferences	74

New Health Summary Types distributed by the High Risk Mental Health Patient project:	79

Chapter 4: Managing Health Summary	85

1.  Health Summary Coordinator’s Menu	86

2. Security, Locks, and Keys	87

3. Batch Printing Process	88

Batch Print of All Clinics by Visit Date	88

Set-up Batch Print Locations	88

4.  User Preferences	92

5. Site Preferences	97

Chapter 5: Helpful Hints	102

Glossary	105

Appendices	108

Appendix A—Health Summary Component Description List	109

Sample of RXDC Report	123

Sample of RXOI Report	123

Appendix B—VISTA And Health Summary Conventions	125

Special Keys, Commands, and Symbols	125

Printing Conventions:	126

Appendix C—Historical Documentation Shift from GMTS*2.7*133 (Do Not Update)	127

New Features in Health Summary	127

Released Patches for Health Summary 2.7	160

Packages providing data to Health Summary	162

Index	163

###### 


## Chapter 1: Introduction

**Health Summary Menus**

**How to Use This Manual**

# Chapter 1 – Introduction

A Health Summary is a clinically oriented, structured report that extracts many kinds of data from VistA and displays it in a standard format. The individual patient is the focus of health summaries. Health summaries can also be printed or displayed for groups of patients. The data displayed covers a wide range of health-related information such as demographic data, allergies, current active medical problems, and laboratory results.

Health Summaries can be viewed through VistA options and through the CPRS GUI on the Reports tab.

### Health Summary Menus

### Health Summary Overall Menu [GMTS MANAGER]

The Health Summary Overall Menu contains all four Health Summary menus. IRM staff members or Clinical Coordinator who need access to all menus are assigned the Health Summary Overall Menu [GMTS MANAGER] rather than each menu separately. This User Manual describes the options on the first three menus; options on the Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT] are described in the Health Summary Technical Manual.

**1. Health Summary Menu [GMTS USER]**

This menu is for users who only need to print or display health summaries.

1	Patient Health Summary [GMTS HS BY PATIENT]

2	Ad Hoc Health Summary [GMTS HS ADHOC]

3 	Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 	Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 	Hospital Location Health Summary [GMTS HS BY LOC]

6 	Information Menu ... [GMTS INFO ONLY MENU]

1	Inquire about a Health Summary Type [GMTS TYPE INQ]

2	List Health Summary Types [GMTS TYPE LIST]

3	Inquire about a Health Summary Component [GMTS COMP INQ]

4	List Health Summary Components [GMTS COMP LIST]

5	List Health Summary Component Descriptions [GMTS COMP DESC LIST]

7.    CPRS Reports Tab 'Health Summary Types List' Menu ... [GMTS GUI HS LIST]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST DEFAULTS]

2 Precedence of 'Health Summary Types List [GMTS GUI HS LIST PRECEDENCE]

3 Method of compiling 'Health Summary Types List [GMTS GUI HS LIST METHODS]

4 Edit 'Health Summary Types List' Parameters[ GMTS GUI HS LIST PARAMETERS]

**2. Health Summary Enhanced Menu [GMTS ENHANCED USER]**

This menu is for users who need to create, modify, or delete their *own* health summary types, in addition to printing health summaries.

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Information Menu ... [GMTS INFO ONLY MENU]

1 Inquire about a Health Summary Type [GMTS TYPE INQ]

2 List Health Summary Types [GMTS TYPE LIST]

3 Inquire about a Health Summary Component [GMTS COMP INQ]

4 List Health Summary Components [GMTS COMP LIST]

5 List Health Summary Component Descriptions [GMTS COMP DESC LIST]

7 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

8 Delete Health Summary Type [GMTS TYPE DELETE]

9 CPRS Reports Tab 'Health Summary Types List' Menu ... [GMTS GUI HS LIST]

1     Display 'Health Summary Types List' Defaults

2     Precedence of 'Health Summary Types List

3     Method of compiling 'Health Summary Types List

4     Edit 'Health Summary Types List' Parameters

**3. Health Summary Coordinator’s Menu [GMTS COORDINATOR]**

This menu is for users who need to print or display health summaries, and to create, modify, or delete health summary types, and set up nightly batch printing at specified locations.

1 Print Health Summary Menu ... [GMTS HS MENU]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Batch Print of All Clinics by Visit Date [GMTS HS FOR ALL CLINICS]

2 Build Health Summary Type Menu ... [GMTS BUILD MENU]

1 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

2 Delete Health Summary Type [GMTS TYPE DELETE]

3 Health Summary Objects Menu [GMTS OBJ MENU]

1 Create/Modify Health Summary Object [GMTS OBJ ENTER/EDIT]

2 Inquire about a Health Summary Object [GMTS OBJ INQ]

3 Test a Health Summary Object [GMTS OBJ TEST]

4 Delete Health Summary Object [GMTS OBJ DELETE]

5 Export/Import a Health Summary Object [GMTS OBJ EXPORT/IMPORT]

1 Export a Health Summary Object [GMTS OBJ EXPORT]

2 Import/Install a Health Summary Object [GMTS OBJ IMPORT/INSTALL]

**Health Summary Coordinator’s Menu [GMTS COORDINATOR], cont’d**

4 Information Menu ... [GMTS INFO ONLY MENU]

1 Inquire about a Health Summary Type [GMTS TYPE INQ]

2 List Health Summary Types [GMTS TYPE LIST]

3 Inquire about a Health Summary Component [GMTS COMP INQ]

4 List Health Summary Components [GMTS COMP LIST]

5 List Health Summary Component Descriptions [GMTS COMP DESC LIST]

5 Print Health Summary Menu ... [GMTS HS MENU]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE 							RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Batch Print of All Clinics by Visit Date [GMTS HS FOR ALL CLINICS]

6 Set-up Batch Print Locations [GMTS HS BY LOC PARAMETERS]

7 List Batch Health Summary Locations [GMTS TASK LOCATIONS LIST]

8 CPRS Reports Tab 'Health Summary Types List' Menu ... [GMTS GUI HS LIST]

1 Display 'Health Summary Types List' Defaults

2 Precedence of 'Health Summary Types List

3 Method of compiling 'Health Summary Types List

4 Edit 'Health Summary Types List' Parameters

**4. Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU]**

This menu is for IRM staff or Clinical Coordinators who help implement and maintain Health Summary. Options on this menu are described in the Health Summary Technical Manual.

1 Disable/Enable Health Summary Component [GMTS IRM/ADPAC ENABLE/DISABLE]

2 Create/Modify Health Summary Components [GMTS IRM/ADPAC COMP EDIT]

3 Edit Ad Hoc Health Summary Type [GMTS IRM/ADPAC ADHOC EDIT]

4 Rebuild Ad Hoc Health Summary Type [GMTS IRM/ADPAC ADHOC LOAD]

5 Resequence a Health Summary Type [GMTS IRM/ADPAC TYPE RESEQUENCE]

6 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

7 Edit Health Summary Site Parameters [GMTS IRM/ADPAC PARAMETER EDIT]

8 Health Summary Objects Menu [GMTS OBJ MENU]

1 Create/Modify Health Summary Object [GMTS OBJ ENTER/EDIT]

2 Inquire about a Health Summary Object [GMTS OBJ INQ]

3 Test a Health Summary Object [GMTS OBJ TEST]

4 Delete Health Summary Object [GMTS OBJ DELETE]

5 Export/Import a Health Summary Object [GMTS OBJ EXPORT/IMPORT]

1 Export a Health Summary Object [GMTS OBJ EXPORT]

2 Import/Install a Health Summary Object [GMTS OBJ IMPORT/INSTALL]

**Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU], cont’d**

9 CPRS Reports Tab 'Health Summary Types List' Menu [GMTS GUI REPORTS LIST MENU]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST DEFAULTS]

2 Precedence of 'Health Summary Types List' [GMTS GUI HS LIST PRECEDENCE]

3 Method of compiling 'Health Summary Types List' [GMTS GUI HS LIST METHOD]

4 Edit 'Health Summary Types List' Parameters [GMTS GUI HS LIST PARAMETERS]

10 CPRS Health Summary Display/Edit Site Defaults [GMTS GUI SITE DEFAULTS]

1 Display Site Health Summary List Defaults [GMTS GUI SITE DISPLAY DEFAULTS]

2 Edit 'Health Summary Types List' Parameters [GMTS GUI SITE  ADD/EDIT LIST]

3 Edit Default HS Type List Compile Method [GMTS GUI SITE COMPILE METHOD]

4 Add/Edit Allowable Entities for HS List [GMTS GUI SITE PRECEDENCE]

5 Resequence Allowable Entities for HS List [GMTS GUI SITE RESEQUENCE]

11 Check Medication Reconciliation Configuration [GMTS PS MED RECON CONFIG CHECK]

### How to Use This Manual

If you are new to **V** *IST* **A** and the VA computer system, see Appendix D for guidelines about using the computer.

***Option examples***

Menus and examples of computer dialogue that you’ll see on your terminal are shown here in boxes.

Select Health Summary Type: **OUTPATIENT**

Select Patient: **HSPATIENT,ONE** 10-03-40     666010101     SC VETERAN

Another patient can be selected.

Select Patient: **&lt;Enter&gt;**

DEVICE: HOME// **&lt;Enter&gt;**

***Printed Summary examples***

Printouts (on paper or screen) are depicted here in double-lined boxes.

10/11/94 16:03
****************** CONFIDENTIAL OUTPATIENT SUMMARY **********************

HSPATIENT,ONE	  666-01-0101	      SURG-ICU	            DOB: 10/03/40

------------------------- DEM - Demographics --------------------------

Address: hOLLYWOOD &amp; VINE            Phone: 703-450-8010

PARIS, TEXAS  23077      County: FAIRFAX

***User responses***

In computer dialogues, user responses are in boldface type.

Select NEW PERSON NAME: **HSPATIENT,ONE**

***Explanations***

Special notes in the manual text are preceded by “ **Note:** ” and are in a lower font size. If a special note is needed inside a computer dialogue screen, it is preceded by an arrow (). The following are examples of marked notes.

**Note:** A list must be defined before you can use this option.

OCCURRENCE LIMIT: 10// **&lt;Enter&gt;** *A return entered here causes the default to be accepted!*

***Points of Interest***

Points about a feature that need highlighting are preceded by this flag.


## Chapter 2: Using Health Summary – Basic Features


**1. Patient Health Summary**

**2. Ad Hoc Health Summary**

**3. Range of Dates Patient Health Summary**

**4. Visit Patient Health Summary**

**5. Hospital Location Health Summary**

**6. Information Menu**

**7. CPRS Reports Tab 'Health Summary Types List' Menu**


# Chapter 2 – Using Health Summary – Basic Features

Chapter 2 describes how to use the basic features of the Health Summary package  displaying and printing pre-defined health summaries or ad hoc health summaries.

#### Health Summary Menu

This menu contains the basic Health Summary options that let you display or print Health Summaries. It also contains an Information sub-menu that lets you look up information about Health Summary types, components, or other items.

1	Patient Health Summary

2	Ad Hoc Health Summary

3 	Range of Dates Patient Health Summary

4 	Visit Patient Health Summary

5 	Hospital Location Health Summary

6 	Information Menu ...

7.   CPRS Reports Tab 'Health Summary Types List' Menu…

On the following pages we describe, step-by-step, how to use these options.


### Patient Health Summary Option

**Displaying or Printing a Health Summary** ;

Use the Patient Health Summary option to display or print a health summary for one or more patients, or a group of patients by location, such as the operating room, ward, or clinic. The health summary (in display or print format) contains patient information provided by *components* designated in the health summary *type* .

***Definitions***

*Component* Summarized patient data extracted from various VISTA software packages.

*Type* A structure or template containing defined components and unique characteristics. Contact your Health Summary Coordinator if you need certain components added to a particular health summary type or a specific health summary type created for your needs. You can request creation of a new health summary type by using the form “Request for New Health Summary Type,” in Appendix A of this manual.

*Selected component* Indicates that a user can choose any number of *selection items* (e.g., tests, measurements, or procedures) available in the Laboratory, Nursing (Vital Signs), Radiology, and Patient Care Encounter (PCE) packages.

*Before you use this option* , you need to know the following.

a)	The *health summary type* that will provide the patient information you need. Four SAMPLE types are distributed with the package for sites to use as guidelines in developing their own types. For a list of available types at your site, enter a ? at the “Select Health Summary Type:” prompt (the first prompt when you enter this option, as shown in the example on the next page).

Depending on how a health summary type is defined at your site, sensitive patient data can be suppressed in the printed health summary.

b)	The *patient(s) name* .

**Note:** You may identify a patient by entering information other than the patient’s name. You may also identify patients by entering their Date of Birth, SSN, Ward Location, or Room-Bed, at the Select Patient: prompt. If CPRS is available, you can also select multiple patients from a ward, clinic, treating specialty, attending physician, personal, or team list.

c)	Whether you will print the health summary or display it on your computer terminal.

**Steps to Display a Patient Health Summary**

**1.** Select the Patient Health Summary option from your menu.

**2.** Enter a health summary type name.

**3.** Enter the names of the patients you plan to display health summaries for.

**4.** Press &lt;Enter&gt; at the DEVICE: HOME// prompt to display the health summary or enter a printer name to print the health summary.

***Example of requesting a Health Summary display.***

**Note:** User responses are shown in bold in examples of computer dialogue.

Select Health Summary Type: **OUTPATIENT**

Select Patient: **HSPATIENT,ONE** 10-03-40     666010101     SC VETERAN

Another patient can be selected.

Select Patient **&lt;Enter&gt;**

DEVICE: HOME// **&lt;Enter&gt;**

**5.** A health summary similar to the following is displayed on your screen.

*******************  CONFIDENTIAL OUTPATIENT SUMMARY  **********************

<!-- image -->

This patient data can be suppressed by settings in the HS Type definition.

<!-- image -->

-------------------------- BDEM - Brief Demographics -----------------------

Address: HEARTATTACK &amp; VINE                 Phone: 555 555 2472

LOS ANGELES, CA  94103

Eligibility: SERVICE CONNECTED 50% to 100%      Age: 50

Sex: MALE

----------------------- CVP - Past Clinic Visits ---------------------

10/09/95 08:45      BLUE-ORTHOPEDIC-JC

10/03/95 13:00      GREEN-DERMATOLOGY PM-JC

10/03/95 10:00      PSYCHOLOGY JC

09/19/95 10:00      PSYCHOLOGY JC

09/18/95 09:30      C&amp;L (RICK)

09/12/95 10:00      PSYCHOLOGY JC

---------- BLO - Brief Lab Orders (max 6 occurrences or 1 year) ---------

Collection DT	Test Name	Specimen	Urgency 	Status

09/25/95 	GLUCOSE	SERUM	ROUTINE   	ORDERED

09/13/95 	CHEM 7	SERUM	ROUTINE   	COMPLETED

05/22/95 	CBC	BLOOD	ROUTINE    	PROCESSING

-------- SLT - Lab Tests Selected (max 6 occurrences or 1 year) -----------

Collection DT   Specimen   Test Name        Result     Units     Ref Range

05/03/95 10:51  SERUM      THEOPHYLLINE      11.9      ug/ml     10 - 20

04/29/95 16:51  SERUM      CHLORIDE         100        ug/ml     10 - 20

03/24/95 16:26  SERUM      THEOPHYLLINE       6.6 L    ug/ml     10 - 20

-----------------CLINICAL MAINTENANCE REMINDERS ---------------------------

LAST	NEXT

CHOLESTEROL	9/12/95 	DUE NOW

BLOOD PRESS	9/12/95 	DUE NOW

SMOKING EDU	9/12/95 	DUE NOW

WEIGHT		9/12/95 	DUE NOW

* END *

Press &lt;Enter&gt; to continue, ^ to exit component, or select component: **^**

*Points of Interest*

1. This example uses a fictitious health summary type called OUTPATIENT.

1. The health summary type selected, in this case OUTPATIENT, determines which components are displayed (e.g., Past Clinic Visits), their component order (summary order), and component characteristics.

1. The health summary type also determines *maximum occurrences* , *time limits, Hospital Location Display, ICD Text Display,* and *Provider Narrative Display* . Data within a component is displayed with the most recent data first.

1. The three entries displayed in the Lab Orders component for patient ONE HSPATIENT occur within a one-year period. If there are more than six lab orders, only the six most recent orders are displayed.

1. Selection items are identified for the Lab Tests Selected component and Clinical Maintenance Reminders component. The OUTPATIENT health summary type determines the selection items included.

1. The word CONFIDENTIAL always precedes the name of the health summary type in the display or the printed copy, and the word SUMMARY follows the summary type. *All health summaries display or print in an 80-character format.*

1. As of Patch 85, you can suppress sensitive patient data in Health Summary printouts.

Depending on the response to “SUPPRESS SENSITIVE PATIENT DATA” when defining a Health Summary Type, the SSN/DOB information will be in one of the following formats.

- Full 9 digit SSN and full DOB
- 4 digit SSN and No DOB
- No SSN and No DOB

1. Notifications

You may see a “View Alerts” message while using Health Summary.

HSPATIENT,TWO (T1111): Co-signature required on note(s).

HSPATIENT,THREE(T0000): Unsigned notes.

Enter  "VA   VIEW ALERTS    to review alerts

This feature is used by packages in VISTA to inform health care team members about a patient’s status or that some action needs to be taken. For more information about how to respond to the alerts, refer to the particular package for which the alert is generated.

### Ad Hoc Health Summary Option

This option lets you select any or all health summary components and assign component characteristics for one or more patients. The components selected in this option are **not saved** in a health summary type but are available only while you are using this option. If you want to re-use this ad hoc health summary, you must request creation of a new health summary type. For more information, see Appendix A of this manual.

***Steps to use the Ad Hoc Health Summary option:***

**1.** Select the Ad Hoc Health Summary option from your menu.

Select Health Summary Menu Option: **A** Ad Hoc Health Summary

**2.** A list of components is displayed.

CD    Advance Directive   CY    Cytopathology       RXNV  Non VA Meds

BADR  Brief Adv React/All EM    Electron Microscopy ONC   Oncology

ADR   Adv React/Allerg    MIC   Microbiology        ORC   Current Orders

BNC   BRAND NEW COMPONENT BMIC  Brief Microbiology  ED    Education

CPB   Clin Proc   Brief   LO    Lab Orders          EDL   Education Latest

CMB   Reminder Brief      BLO   Brief Lab Orders    EXAM  Exams Latest

CR    Reminders Due       SP    Surgical Pathology  HF    Health Factors

CF    Reminders Findings  SLT   Lab Tests Selected  SHF   Health Factor Select

CLD   Reminders Last Done MAGI  MAG Imaging         IM    Immunizations

CM    Reminder MaintenanceADC   Admission/Discharge OD    Outpatient Diagnosis

CRS   Reminders Summary   ADT   ADT History         OE    Outpatient Encounter

CW    Clinical Warnings   EADT  ADT History ExpandedST    Skin Tests

CP    Comp. &amp; Pen. Exams  CVF   Fut Clinic Visits   RXIV  IV Pharmacy

CNB   Brief Consults      CVP   Past Clinic Visits  RXOP  Outpatient Pharmacy

CN    Crisis Notes        CON   Patient Contacts    RXUD  Unit Dose Pharmacy

DI    Dietetics           DEM   Demographics        PLA   Active Problems

DCS   Discharge Summary   BDEM  Brief Demographics  PLL   All Problems

BDS   Brief Disch Summary DS    Disabilities        PLI   Inactive Problems

ENV   Full Environment    DD    Discharge Diagnosis       PROBLEM LSIT

FR    Fred                DC    Discharges          PN    Progress Notes

AVC   GEC                 MHFV  MH Clinic Fut VisitsBPN   Brief Progress Notes

Press RETURN to continue or '^' to exit:

GECC  Referral Count      PRC   ICD Procedures      SPN   Selected Prog Notes

GECH  Referral Categories OPC   ICD Surgeries

GAF   Global Assess Funct TR    Transfers           SCD   Spinal Cord Dysfunct

HS    HS Environment      TS    Treating Specialty  NSR   NON OR Procedures

II    Imaging Impression  MEDA  Med Abnormal        SRO   Surgery Only Reports

SII   Sel Image ImpressionMEDB  Med Brief Report    SR    Surgery Rpt (OR/NON)

IP    Imaging Profile     MEDC  Med Full Captioned  BSR   Brief Surgery Rpts

IS    Imaging Status      MEDF  Med Full Report     SNSR  Selected NON OR Proc

MEDS  Med (1 line) Summary

MHPE  MH Physical Exam    URIN  URINALYSIS

BA    Blood Availability  MHRF  MH Suicide PRF Hx   VS    Vital Signs

BT    Blood Transfusions  MHTC  MH Treatment Coor   VSD   Detailed Vitals

CH    Chem &amp; Hematology   MHAL  MHA Admin List      VSO   Vital Signs Outpat.

SCLU  Lab Cum Selected    MHAS  MHA Score           SVS   Vital Signs Selected

SCL1  Lab Cum Selected 1  MHVD  Detail Display      SVSO  Vital Select Outpat.

SCL2  Lab Cum Selected 2  MHVS  Summary Display

SCL3  Lab Cum Selected 3  MRT2  Medication Worksheet

SCL4  Lab Cum Selected 4  NOK   Next of Kin

**Note:** These are all the components distributed with the Health Summary package. If your display of components looks different from this, your site may have modified the component list, or you may not have the necessary version of a supporting package installed.

**Further Note:** These components are listed by “Default Header.” For example, “Blood Availability” is the default header name, whereas the component name is LAB BLOOD AVAILABILITY. If you need a more detailed explanation of this, contact your Clinical Coordinator or IRMS.

**3.** Enter a new set of components. You can enter the abbreviation for that component, the Default Header name, or the actual (Technical) name, as listed above.

Select NEW set of COMPONENT(S): **??**

The Health Summary components you select at this prompt create an ADHOC Health Summary

Select ONE or MORE items from the menu, separated by commas.

ALL items may be selected by typing “ALL”.

EXCEPTIONS may be entered by preceding them with a minus.

For example, "ALL,-THIS,-THAT" selects all but "THIS" and "THAT".

NOTE: Menu items are ordered alphabetically by the Component NAME.

However, the displayed text is the Header Name which generally

is different from the Component Name. Components may be picked

by their abbreviation, Header Name, or Component Name.

Redisplay items? YES// **NO**

Select NEW set of COMPONENT(S): **???**

Navigation OUTSIDE of Health Summary

You may also enter “^^” followed by the name, partial name or synonym for

any of a variety of options OUTSIDE of Health Summary to which you can

jump.  Partial matches will allow you to select from a subset of options.

For example:  ^^?     will list ALL available options.

^^PN    will show you all of the PROGRESS NOTES options, or

^^OR    will show you all of the ORDER ENTRY options.

You may also order a wide variety of LABORATORY tests using this syntax,

e.g., ^^CHEM 7 will allow you to ADD an order for that test.

Redisplay items?  YES// **&lt;Enter&gt;**

Select NEW set of COMPONENT(S): **PN,SPN DCS** PROGRESS NOTES  SELECTED PROGRESS NOTES Discharge Summary

**Note:** If the first three characters of an ABBREVIATION HEADER NAME or Component NAME contain “ALL” (not case-sensitive), you can’t enter “ALL” to select all the items on the Ad Hoc Health Summary menu.

Default Limits and Selection Items

Component              Occ    Time   Hosp  ICD   Prov  Selection

Limit  Limit  Loc   Text  Narr  Item(s)

PN	Progress Notes		10     1Y

SPN Selected Progress Notes    10     1Y

DCS	Discharges			10     1Y

Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD:

**Note** :  Default values are provided for Time and Occurrence Limits, Hospital Location Display, ICD Text Display, Provider Narrative Display, and Display Header Selection Items for most components. To change the component’s defaults, enter the component name(s) at the “Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD:” prompt, and then edit as necessary. You may also add more components at this prompt and edit their defaults.

**4.** Enter time and occurrence limits and Header Name. Where applicable, Hospital Location Display, ICD Text Display, and Provider Narrative Display defaults may also be changed here.

OCCURRENCE LIMIT: 10// **&lt;Enter&gt;** *.*

TIME LIMIT: 1Y// **&lt;Enter&gt;**

HEADER NAME: Progress Notes

**5.** Enter additional components, if desired, with time and occurrence limits for each. Press Enter or &lt;Enter&gt; if you don’t want to enter more components or edit the components you have entered.

Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD: **DC** DISCHARGES

Discharges

OCCURRENCE LIMIT: 10// **4**

TIME LIMIT: 1Y// **2Y**

HEADER NAME: **&lt;Enter&gt;**

Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD: **&lt;Enter&gt;**

Would you like to see Component Limits and Selection Items again?  (Y/N):  N// **&lt;Enter&gt; NO**

**6.** Enter the patient names for this health summary.

**7.** Press &lt;Enter&gt; at the DEVICE: HOME// prompt to display the health summary or enter a printer name to print a paper copy.

Select Patient: HSPATIENT,ONE

Another Patient can be selected

Select Patient: **&lt;Enter&gt;**

Device:  HOME// **&lt;Enter&gt;**

**8.** An ad hoc health summary similar to the following is displayed.

**Example 1: Note the highlighted sections that show the Local Title and Standard Title.**

05/30/2006 16:12

********************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 *********************

HSPATIENT,ONE    666-12-9900     HOSPICE 178-1                  DOB: 12/31/1898

------------- PN - Progress Notes (max 10 occurrences or 1 year) -------------

05/30/2006 16:08  Local Title: OUTPATIENT DISCHARGE INSTRUCTIONS

Standard Title: RN EMERGENCY DEPARTMENT DISCHARGE NOTE

Disposition/Clinic Appointment:

After Care Sheet Given:  \_\_\_\_\_YES      \_\_\_\_\_NO

Followup-Activity-Limitations:

Condition on Discharge: \_\_\_\_\_Improved

\_\_\_\_\_Satisfactory

\_\_\_\_\_Unchanged

Date/Time of Discharge:

Patient Instructions:

A copy of the patient instructions were given to the patient.  The

patient indicated that he/she understood those instructions.

Signed by:  /es/  ONE CPRSPROVIDER

05/30/2006 16:08

05/30/2006 16:07  Local Title: 10-10M NURSING AMB CARE

Standard Title: ADMISSION EVALUATION NOTE

Date/Time:     MAY 30, 2006 16:07

Patient Name:  HSPATIENT,ONE

Age:           107

Sex:           MALE

On Arrival Patient was

Ambulatory:

Stretcher:

Wheelchair:

Phone Number:

Homeless?:

Allergies:     Patient has answered NKA

Weight:        176.1 lb [80.0 kg] (09/25/2004 13:33)

Temperature:   99.8 F [37.7 C] (09/24/2004 19:39)

Pulse:         127 (09/24/2004 19:39)

Respiration:   20 (09/24/2004 19:39)

B/P:           141/73 (09/24/2004 19:39)

Pain Scale:    6 (09/23/2004 18:09)

Due to Injury?:

Current Medications:

Medications administered in Ambulatory Care/ER:

Triage:

Diabetic:  \_\_\_\_Yes  \_\_\_No

Oriented to person, place and time:  \_\_\_Yes \_\_\_No

RN assessment show the patient is self care:  \_\_\_Yes \_\_\_No

Patient verbalizes understanding of information on lodger pamphlet?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

Prescribed medications accompany lodger for self administration?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

History and Physical:

Heparin Lock or IV Infusion of \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ @ \_\_\_\_cc/HR.

Started @ \_\_\_\_am  \_\_\_\_\_pm in \_\_\_\_\_\_\_\_ (site) with # \_\_\_\_\_ needle.

Unsuccessful starts:

Diagnostic Impressions:

Plan:

Signed by:  /es/  ONE CPRSPROVIDER

05/30/2006 16:07

05/16/2006 18:43  Local Title: APPOINTMENT NO SHOW - NUTRITION EDUCATION CONSULT REPORT

Standard Title: EDUCATION CONSULT

Patient was a "no show" for

\_\_\_Reduction Class

\_\_\_Cholesterol Class

\_\_\_Diabetic Class

Plan:

Mailed diet materials with name and phone number for questions.

Signed by:  /es/  ONE HSPROVIDER

05/16/2006 18:43

--------- SPN - Selected Prog Notes (max 10 occurrences or 10 years) ---------

05/30/2006 16:08  Local Title: OUTPATIENT DISCHARGE INSTRUCTIONS

Standard Title: RN EMERGENCY DEPARTMENT DISCHARGE NOTE

Disposition/Clinic Appointment:

After Care Sheet Given:  \_\_\_\_\_YES      \_\_\_\_\_NO

Followup-Activity-Limitations:

Condition on Discharge: \_\_\_\_\_Improved

\_\_\_\_\_Satisfactory

\_\_\_\_\_Unchanged

Date/Time of Discharge:

Patient Instructions:

A copy of the patient instructions were given to the patient.  The

patient indicated that he/she understood those instructions.

Signed by:  /es/  CPRSPROVIDER, ONE

05/30/2006 16:08

05/30/2006 16:07  Local Title: 10-10M NURSING AMB CARE

Standard Title: ADMISSION EVALUATION NOTE

Date/Time:     MAY 30, 2006 16:07

Patient Name:  HSPATIENT,ONE

Age:           107

Sex:           MALE

On Arrival Patient was

Ambulatory:

Stretcher:

Wheelchair:

Phone Number:

Homeless?:

Allergies:     Patient has answered NKA

Weight:        176.1 lb [80.0 kg] (09/25/2004 13:33)

Temperature:   99.8 F [37.7 C] (09/24/2004 19:39)

Pulse:         127 (09/24/2004 19:39)

Respiration:   20 (09/24/2004 19:39)

B/P:           141/73 (09/24/2004 19:39)

Pain Scale:    6 (09/23/2004 18:09)

Due to Injury?:

Current Medications:

Medications administered in Ambulatory Care/ER:

Triage:

Diabetic:  \_\_\_\_Yes  \_\_\_No

Oriented to person, place and time:  \_\_\_Yes \_\_\_No

RN assessment show the patient is self care:  \_\_\_Yes \_\_\_No

Patient verbalizes understanding of information on lodger pamphlet?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

Prescribed medications accompany lodger for self administration?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

History and Physical:

Heparin Lock or IV Infusion of \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ @ \_\_\_\_cc/HR.

Started @ \_\_\_\_am  \_\_\_\_\_pm in \_\_\_\_\_\_\_\_ (site) with # \_\_\_\_\_ needle.

Unsuccessful starts:

Diagnostic Impressions:

Plan:

Signed by:  /es/  ONE CPRSPROVIDER

05/30/2006 16:07

05/30/2006 16:14

********************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 *********************

HSPATIENT,ONE    666-12-9900     HOSPICE 178-1                  DOB: 12/31/1898

--------------------------- DCS - Discharge Summary ---------------------------

09/21/2004  - Present                                   Status: COMPLETED

Local Title: DISCHARGE SUMMARY

Standard Title: DISCHARGE SUMMARY

Last Tr Specialty: HOSPICE                    Dict'd By: CPRSPROVIDER,ONE

Approved By: CPRSPROVIDER,ONE

TESTING

Signed by:  /es/  ONE CPRSPROVIDER

05/23/2006 11:42

09/17/2004  - 09/21/2004                                Status: COMPLETED

Local Title: DISCHARGE SUMMARY

Standard Title: DISCHARGE SUMMARY

Last Tr Specialty: INTERMEDIATE MEDICINE      Dict'd By: HSPROVIDER,TWO

Approved By: CPRSPROVIDER,ONE

DISCHARGE SUMMARY

ADMIT DATE:09/17/04

DISCHARGE DATE:09/21/04

ATTENDING MD:Cassidy

CONSULTANTS:None

DISCHARGE DIAGNOSES:Prostate CA with mets to lumbar spine

********************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 *********************

HSPATIENT,ONE    666-12-9900     HOSPICE 178-1                  DOB: 12/31/1898

------------- PN - Progress Notes (max 10 occurrences or 1 year) -------------

05/30/2006 16:08  Local Title: OUTPATIENT DISCHARGE INSTRUCTIONS

Standard Title: RN EMERGENCY DEPARTMENT DISCHARGE NOTE

Disposition/Clinic Appointment:

After Care Sheet Given:  \_\_\_\_\_YES      \_\_\_\_\_NO

Followup-Activity-Limitations:

Condition on Discharge: \_\_\_\_\_Improved

\_\_\_\_\_Satisfactory

\_\_\_\_\_Unchanged

Date/Time of Discharge:

Patient Instructions:

A copy of the patient instructions were given to the patient.  The

patient indicated that he/she understood those instructions.

Signed by:  /es/  ONE CPRSPROVIDER

05/30/2006 16:08

05/30/2006 16:07  Local Title: 10-10M NURSING AMB CARE

Standard Title: ADMISSION EVALUATION NOTE

Date/Time:     MAY 30, 2006 16:07

Patient Name:  HSPATIENT,ONE

Age:           107

Sex:           MALE

On Arrival Patient was

Ambulatory:

Stretcher:

Wheelchair:

Phone Number:

Homeless?:

Allergies:     Patient has answered NKA

Weight:        176.1 lb [80.0 kg] (09/25/2004 13:33)

Temperature:   99.8 F [37.7 C] (09/24/2004 19:39)

Pulse:         127 (09/24/2004 19:39)

Respiration:   20 (09/24/2004 19:39)

B/P:           141/73 (09/24/2004 19:39)

Pain Scale:    6 (09/23/2004 18:09)

Due to Injury?:

Current Medications:

Medications administered in Ambulatory Care/ER:

Triage:

Diabetic:  \_\_\_\_Yes  \_\_\_No

Oriented to person, place and time:  \_\_\_Yes \_\_\_No

RN assessment show the patient is self care:  \_\_\_Yes \_\_\_No

Patient verbalizes understanding of information on lodger pamphlet?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

Prescribed medications accompany lodger for self administration?

\_\_\_\_Yes  \_\_\_No  \_\_\_NA

History and Physical:

Heparin Lock or IV Infusion of \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ @ \_\_\_\_cc/HR.

Started @ \_\_\_\_am  \_\_\_\_\_pm in \_\_\_\_\_\_\_\_ (site) with # \_\_\_\_\_ needle.

Unsuccessful starts:

Diagnostic Impressions:

Plan:

Signed by:  /es/  ONE CPRSPROVIDER

05/30/2006 16:07

**Example 2: Note the highlighted sections that show the Local Title and Standard Title.**

********************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 *********************

HSPATIENT,TWO    666-14-5397                                     DOB: 10/15/1932

** DECEASED   APR 10,1998@08:10 **

--------------------------- CD - Advance Directive ---------------------------

02/25/1997 12:48  Local Title: ADVANCE DIRECTIVE

Standard Title: ADVANCE DIRECTIVE

LIVING WILL AND DPOAHC COMPLETED ON 2/25/97.

Signed by:  /es/  HSPROVIDER,ONE

MSSW  02/25/1997 12:49

--------------------------- CW - Clinical Warnings ---------------------------

10/11/1991 14:51  Local Title: CLINICAL WARNING

Standard Title: CLINICAL WARNING

Chief of Police and Security Service states that this patient recently

threatened to commit suicide and is known to carry a handgun.  Please be

alert to behavior suggesting suicidal intent, and contact the appropriate

mental health clinicians if you feel he needs to be evaluated.

Signed by:  /es/  HSPROVIDER,ONE

CHIEF OF PSYCHOLOGY  10/11/1991 14:53

Digital Pager:  800 123-4567

------------------------------ CN - Crisis Notes ------------------------------

04/29/1996 20:44  Local Title: CRISIS NOTE

Standard Title: CRISIS INTERVENTION NOTE

CRISIS FOCUS, On-Call Response:

RESPONDED TO THE ER AT THE REQUEST OF THE MOD TO INTERVIEW THIS VETERAN

WHO HAD PRESENTED COMPLAINING OF "CHEST PAIN".  THE MOD WAS CONCERNED

SECONDARY TO ODD BEHAVIORS VETERAN WAS EXHIBITING AND THE FACT THAT HER

RESPONSES TO QUESTIONS WERE VAGUE OR INDEFINITE, AND SOMETIMES NOT

FORTHCOMING AT ALL.

Signed by:  /es/  HSPROVIDER,ONE

Addiction Counselor  04/29/1996 21:10

Analog Pager:  5-678

*** END ************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 ********************

### Range of Dates Patient Health Summary

This option lets you print health summaries of a specified, pre-defined health summary type for multiple patients. After patients are selected, you can pick a date range. Data for summaries is based on the date range. This date range overrides time limits for components which allow this option.

**Steps to print a Range of Dates Patient Health Summary**

**1.** Select the Range of Dates Patient Health Summary option from your menu.

**2.** Enter a health summary type name.

**3.** Enter the names of patients you plan to print a Health Summary for.

**4.** Enter beginning and ending dates.

**5.** Press &lt;Enter&gt; at the DEVICE: HOME// prompt to display the health summary or enter a printer name to print the health summary.

Select Health Summary Menu Option: **?**

1      Patient Health Summary

2      Ad Hoc Health Summary

3      Range of Dates Patient Health Summary

4      Visit Patient Health Summary

5      Hospital Location Health Summary

6      Information Menu ...

7.     CPRS Reports Tab 'Health Summary Types List' Menu…

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Print Health Summary Menu Option: **3** Range of Dates Patient Health Summary

Select Health Summary Type: **SAMPLE 1**

Select Patient: **HSPATIENT,ONE** .       10-03-40     666010101     SC VETERAN

Another patient(s) can be selected.

Select Patient: **&lt;Enter&gt;**

Enter Beginning Date (MM/DD/YY): **T-30**

Enter Ending Date (MM/DD/YY):  TODAY// **&lt;Enter&gt;** (SEP 05, 2001)

DEVICE: HOME// **&lt;Enter&gt;** VAX

A health summary for the specified dates will be displayed on your screen.

### Visit Patient Health Summary

This option lets you print health summaries of a specified, pre-defined health summary type for multiple patients. After a patient is selected, you can pick an outpatient visit or an inpatient hospital admission. If the Patient Care Encounter (PCE) package isn´t installed, you can only choose an inpatient visit. Data for summaries is based on a date range from the outpatient visit or inpatient admission. This date range overrides time limits for components which allow this option.

**Steps to print a Visit Patient Health Summary**

**1.** Select the Visit Patient Health Summary option from your menu.

**2.** Enter a health summary type name.

**3.** Enter the name of the patient you plan to print a health summary for. (You can select other patients after you have specified the visit date for this patient.)

**4.** Specify whether you want an outpatient visit or an admission and then choose the entry.

**5.** Answer yes if you wish to include the Outpatient Pharmacy Action Profile.

**NOTE** : This prompt appears only if the site parameter “Prompt for action profiles” is enabled.

**6.** Press &lt;Enter&gt; at the DEVICE: HOME// prompt to display the health summary or enter a printer name to print the health summary.

Select Health Summary Menu Option: **?**

1      Patient Health Summary

2      Ad Hoc Health Summary

3      Range of Dates Patient Health Summary

4      Visit Patient Health Summary

5      Hospital Location Health Summary

6      Information Menu ...

7.     CPRS Reports Tab 'Health Summary Types List' Menu…

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Print Health Summary Menu Option: **4** Visit Patient Health Summary

Select Health Summary Type: **SAMPLE 1** SAMPLE 1

Select Patient: **HSPATIENT,ONE** 10-03-40     666010101     SC VETERAN

Select one of the following:

1         Outpatient Visit Date

2         Admission Date

Enter response: **2** Admission Date

ADMISSION DATE/TIME           DISCHARGE DATE/TIME

1       8/16/94 8:35 am               8/19/94 3:21:31 pm

2       7/22/91 10:01:23 am           2/17/94 1:00 pm

Enter a number between 1 and 2: **2**

Select Another Patient: **&lt;Enter&gt;**

Include Outpatient Pharmacy Action Profile (Y/N)? NO// **YES**

DEVICE: HOME// **PRINTERNAME**

**Note** : It is preferable to send the Health Summary to a printer rather than your terminal screen when Action Profiles are included.

**Printed Health Summary Example**

Printed for data from 07/22/91 to 02/17/94                     08/23/95 07:37

*********************  CONFIDENTIAL SAMPLE 1 SUMMARY  ************************

HSPATIENT,ONE        666010101                                    DOB: 10/03/40

-------------------------- BDEM - Brief Demographics -------------------------

Address: HEARTATTACK &amp; VINE                 Phone: 555 555 2472

LOS ANGELES, CA  94103

Eligibility: SERVICE CONNECTED 50% to 100%      Age: 50

Sex: MALE

----------------- BLO - Brief Lab Orders (max 10 occurrences) ----------------

Collection DT   Test Name            Specimen      Urgency          Status

04/13/93 11:00  CBC                  BLOOD         ROUTINE          ORDERED

04/13/93 11:00  GLUCOSE              SERUM         ROUTINE          ORDERED

03/16/93 09:35  GLUCOSE              SERUM         ROUTINE          COMPLETED

03/16/93 09:31  CHEM 7               SERUM         ROUTINE          COMPLETED

03/16/93 09:30  GLUCOSE              SERUM         ROUTINE          COMPLETED

03/16/93 09:28  CHEM 7               SERUM         ROUTINE          COMPLETED

03/16/93 09:14  CHEM 7               SERUM         ROUTINE          COMPLETED

03/16/93 09:14  CHEM 7               SERUM         ROUTINE          COMPLETED

03/16/93 08:54  CHEM 7               SERUM         ROUTINE          COMPLETED

03/16/93 08:52  CHEM 7               SERUM         ROUTINE          COMPLETED

--------------- BMIC - Brief Microbiology (max 10 occurrences) ---------------

No data available

---------------- BSR - Brief Surgery Rpts (max 10 occurrences) ---------------

No data available

----------------- RS - Radiology Status (max 10 occurrences) -----------------

Request DT   Status  Procedure                 Scheduled DT      Provider

04/08/93       p     ANKLE 2 VIEWS                               HSPROVIDER,ONE

04/08/93       p     CHEST 2 VIEWS PA&amp;LAT                        HSPROVIDER,ONE

04/01/93       p     CHEST 2 VIEWS PA&amp;LAT                        HSPROVIDER,ONE

03/15/93       p     CHEST 2 VIEWS PA&amp;LAT                        HSPROVIDER,TWO

---------------- SCLU - Lab Cum Selected (max 10 occurrences) ----------------

No selection items chosen for this component.

-------------------- DC - Discharges (max 10 occurrences) --------------------

Date of Discharge: 02/17/94

Bedsection: INTERMEDIATE MEDICINE

Disposition Type: NON-SERVICE CONNECTED (OPT-NSC)

Disposition Place: UNKNOWN

Outpatient Treatment: UNKNOWN

* END *

Press &lt;Enter&gt; to continue, ^ to exit, or select component:

**Action Rx Profile Example**

Action Rx Profile                             Run Date: AUG 23,1995    Page: 1

Sorted by drug classification for Rx's currently active

and for those Rx's that have been inactive less than 45 days.       Site: 5000

------------------------------------------------------------------------------

Instructions to the provider:

A. A prescription blank (VA FORM 10-2577f) must be used for the

following: 1) any new medication

2) any changes in dosage, direction or quantity

3) all class II narcotics.

B. To continue a medication as printed:

1.  If "Remaining Refills" are sufficient to complete

therapy or last until next scheduled clinic appointment,

no action is required.

2.  If "Remaining Refills" are not sufficient to complete

therapy or last until next scheduled clinic appointment,

sign "RENEW/MD" line, enter VA# and date, and circle

total number of refills needed.  This action creates a

new prescription with refills as indicated.

C. To cancel a medication, sign CANCEL/MD line and enter VA# and date.

D. Any medications not acted upon will continue to be available

to the patient until all refills are used or until expiration.

NOTE: '(R)' indicates a fill was returned to stock.

-------------------------------------------------------------------------------------

Name  : HSPATIENT,ONE   ID#: 666-01-0101       Action Date: \_\_\_\_\_ DOB: 10-03-40             Address  : HOLLYWOOD &amp; VINE

LOS ANGELES, CA 94103

Phone    : 555 555 2472

WEIGHT(Kg):                              HEIGHT(cm):

DISABILITIES:

REACTIONS: MILK, AMOXICILLIN, BEER

------------------------------------------------------------------------------

Medication/Supply                                                         Rx#

Status       Expiration  Provider

Date

&gt;&gt;&gt;&gt; NO PRESCRIPTIONS ON FILE &lt;&lt;&lt;&lt;

REACTIONS: MILK, AMOXICILLIN, BEER

------------------------------------------------------------------------------

Instructions to the provider:

A prescription blank (VA FORM 10-2577f) must be used for All Class II NARCOTICS.

------------------------------------------------------------------------------

OTHER MEDICATIONS:

1   Medication: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Outpatient Directions: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_SC\_\_\_NSC    Quantity: \_\_\_\_\_     Days Supply \_\_\_\_\_     Refills:  0  1  2

3  4  5  6  7  8  9  10  11

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Provider's Signature                DEA #          Date AND Time

------------------------------------------------------------------------------


### Hospital Location Health Summary

This option lets you print or display on your screen health summaries for all patients at specific or multiple hospital locations (ward, clinic, or operating room).

You can also include an Outpatient Pharmacy Action Profile print of the patients at any of the locations you select. These profiles are printed in tandem with the selected health summary type for selected patient locations. For example, John Doe’s health summary will print, and then his action profile, etc.

If the hospital location you specify is a clinic or operating room location (for example, Oncology or OR1), you will need to enter both a beginning and ending visit date or surgery date for that clinic or operating room location.

***Steps to use option:***

**1.** Select the Hospital Location Health Summary option from your menu.

Select Health Summary User Menu Option: **Hosp** ital Location Health Summary

**2.** Select the health summary type.

The default is the last summary type you requested. You can enter a new summary type name, title, or owner.

Select Health Summary Type: OUTPATIENT// **&lt;Enter&gt;**

**3.** Select one or more hospital locations.

Enter ? to see a list of hospital locations. Select from the list. You will be prompted sequentially for each location.

Select Hospital Location: **1A**

Select Next Hospital Location: **Orthopedic**

Select Next Hospital Location: **&lt;Enter&gt;**

**4.** Answer yes if you wish to include the Outpatient Pharmacy Action Profile.

**NOTE** : This prompt appears only if the site parameter “Prompt for action profiles” is enabled.

Include Outpatient Pharmacy Action Profile (Y/N)? NO// **&lt;Enter&gt;**

**5.** Enter the beginning and ending visit or surgery dates.

If you enter a clinic or operating room location above, you will get these prompts.

Please enter the beginning Visit or Surgery date:10/19/95// **&lt;Enter&gt;**

(OCT 19, 1995)

Please enter the ending Visit or Surgery date:10/19/95// T+1 (OCT 19, 1995)

No patients found at Clinic Orthopedic on 10/19/95 to 10/20/95.

Select Hospital Location: **&lt;Enter&gt;**

If the system has no record of patients at a selected ward location, a message informs you that no patients were found at that location.

**6.** Enter &lt;Enter&gt; at the DEVICE: prompt to display the health summary on your screen or enter a printer name.

*Points of Interest:*

1.	If there are no patients at the location you enter, you are told there are no patients and returned to the “Select Hospital Location:” prompt for another choice.

2.	Enter a single ^ at the “Select Hospital Location:” prompt to select another health summary type.

3.	If you enter a single ^ at the bottom of the screen in a health summary, you will see the next patient’s health summary at that location. If no other patients exist, you are returned to the “Select Hospital Location:” prompt.

^^ will exit you from viewing the selected Health Summaries.


### Information Menu

This option contains five information options that let you print lists or get information about health summary types and components.

1	Inquire about a Health Summary Type

2	List Health Summary Types

3	Inquire about a Health Summary Component

4	List Health Summary Components

5	List Health Summary Component Descriptions

##### Inquire about a Health Summary Type

This option provides you with a detailed list of components contained in a health summary type. The information in this inquiry includes the component’s abbreviation, component order in the summary (summary order), component name, maximum occurrence limits, time limits, Hospital Location Display, ICD Text Display, Provider Narrative Display, and selection criteria.

***Steps to use option:***

**1.** Select Inquire about a Health Summary Type from your Information Menu.

Select Health Summary Menu Option: **Info** rmation Menu

1	Inquire about a Health Summary Type

2	List Health Summary Types

3	Inquire about a Health Summary Component

4	List Health Summary Components

5	List Health Summary Component Descriptions

Select Information Menu Option: **INQ**

1   Inquire about a Health Summary Type

2   Inquire about a Health Summary Component

CHOOSE 1-2: **1**

**2.** Select the Health Summary Type you want information about.

Select Health Summary Type: **?**

ANSWER WITH HEALTH SUMMARY TYPE LOCATION(S) USING THE SUMMARY, OR

TITLE, OR OWNER

CHOOSE FROM:

SAMPLE 1

SAMPLE 2

SAMPLE 3   GMTS HS ADHOC OPTION

Select Health Summary Type Name: **SAMPLE 2**

**3.** Select the printer you want to print to, or press return if you want a screen display.

DEVICE: **&lt;Enter&gt;**

**4.** A report similar to the following is displayed on your screen.

HEALTH SUMMARY TYPE INQUIRY

Type Name: SAMPLE 2                       Lock:  GMTSMGR

Title:

Owner: POSTMASTER

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

Max       Hosp  ICD   Prov

Abb.  Order  Component Name      Occ  Time Loc   Text  Narr Selection

---------------------------------------------------------------------

DEM    5     Demographics

ADR    10    Adv React/Allerg

CN     15    Crisis Notes

CW     20 ***** Clinical Warnings

LO     25    Lab Orders            10

CH     30    Chem &amp; Hematology     10    1Y

SCLU   35    Lab Cum Selected      10    1Y

SLT    40    Lab Tests Selected    10    1Y

MIC    45    Microbiology          10    1Y

CY     50    Cytopathology         10    1Y

SP     55    Surgical Pathology    10    2Y

BA     60    Blood Availability    10    1Y

BT     65    Blood Transfusions    10    1Y

RXUD   70    Unit Dose Pharmacy          1Y

RXIV   75    IV Pharmacy                 6M

RP     80    Radiology Profile     10    1Y

OPC    85    ICD Surgeries         10    1Y

PRC    90    ICD Procedures        10    1Y

MED    95    Medicine Summary      10    1Y

SR     100   Surgery Reports       10    1Y

PN     105   Progress Notes        10    1Y

ADC    110   Admission/Discharge   10    3Y

TS     115   Treating Specialty    10    1Y

TR     120   Transfers             10    1Y

DC     125   Discharges            10    1Y

***** = Disabled Components

##### List Health Summary Types

This option provides you with a list of all health summary types currently defined on your system, indicates the person designated as the *owner* of a health summary type, and whether a lock is required to edit a health summary type. This list can be displayed on your screen or printed.

The *owner* listing tells you who created a health summary type and the *lock* listing tells you if a key is required for editing/deleting a health summary type.

***Steps to use option:***

**1.** Select List Health Summary Types from your Information Menu.

Select Information Menu Option: **List Health Summary Types**

**2.** Select the printer you want to print to, or press return if you want a screen display.

DEVICE: **&lt;Enter&gt;**

**3.** A list similar to the following is displayed on your screen.

HEALTH SUMMARY TYPE LIST                   JUL 31,2001  12:18    PAGE 1

Health Summary Type             Owner                    Lock

-----------------------------------------------------------------------

AAS                             ACCOUNT,CHIEF

AC CLINICAL SUMMARY             ACCOUNT,CHIEF

ACTIVE PROBLEMS                 ACCOUNT,CHIEF

GMTS HS ADHOC OPTION	        POSTMASTER	             GMTSMGR

SAMPLE 1	                      POSTMASTER	             GMTSMGR

SAMPLE 2	                      POSTMASTER	             GMTSMGR

SAMPLE 3	                      POSTMASTER	             GMTSMGR

SAMPLE 4	                      POSTMASTER	             GMTSMGR

HSPROVIDER2 	               HSPROVIDER,TWO

HTN CLINIC            	         HSUSER,ONE

##### Inquire about a Health Summary Component

This option provides you with details about an individual component, including Abbreviation, Time and Occurrence Limits, Display Name, Hospital Location Display, ICD Text Display, Provider Narrative Display, Selection Item, Disabled message, and a complete description of the information contained in the component.

**1.** Select Inquire about a Health Summary Component from your Information Menu.

Select Information Menu Option: **INQ**

1   Inquire about a Health Summary Type

2   Inquire about a Health Summary Component

CHOOSE 1-2: **2** Inquire about a Health Summary Component

Select Health Summary Component Name: **DEM**

**2.** Select the printer you want to print to, or press return if you want a screen display.

DEVICE:  HOME// **&lt;Enter&gt;**

**3.** A list similar to the following is displayed on your screen.

HEALTH SUMMARY COMPONENT INQUIRY

Component Name:  MAS DEMOGRAPHICS

Display Name:  Demographics

Abbreviation:  DEM

Time Limits Apply:  NO

Max Occurrences Apply:  NO

Hospital Location Display Apply:  NO

ICD Text Display Apply:  NO

Provider Narrative Display Apply:  NO

Component Disabled:  NO

Description:

This component contains the following patient

demographic data (if available) from the MAS package:

address, phone, county, marital status, religion, age,

sex, occupation, period of service, POW status (e.g.,

Y or N), branch of service, combat status (e.g., Y or

N), eligibility code, current (verified) eligibility

status, service connected %, mean test, next of kin

(NOK), NOK phone number and address.

##### List Health Summary Components

This option produces a complete list of all health summary components and indicates each component’s abbreviation, occurrence limit, time limit, hospital location displayed, ICD text displayed, provider narrative displayed, and whether or not the component has been marked as disabled.

**1.** Select List Health Summary Components from the Information Menu.

Select Information Menu Option: **List**

1   List Health Summary Component Descriptions

2   List Health Summary Components

3   List Health Summary Types

CHOOSE 1-3: **2**

**2.** Select the printer you want to print to, or press return if you want a screen display.

DEVICE:  HOME// **&lt;Enter&gt;**

**3.** The following list is displayed on your screen.

HEALTH SUMMARY COMPONENT LIST                  SEP 18,2012  11:24    PAGE 1

Component                     Occur.   Time     Hosp.  ICD    Prov.

Name                   Abbr.  Limits?  Limits?  Loc.?  Text?  Narr.?  Disabled?

-------------------------------------------------------------------------------

Advance Directive      CD

Brief Adv React/All    BADR

Adv React/Allerg       ADR

Allergies/ADRs         MRT5

CLINICAL MAINTENANCE

Reminder Brief         CMB

Reminders Due          CR

Reminders Findings     CF

Reminders Last Done    CLD

Reminder Maintenance   CM

Reminders Summary      CRS    yes      yes

Clinical Warnings      CW

Comp. &amp; Pen. Exams     CP     yes      yes

Brief Consults         CNB    yes      yes

Crisis Notes           CN

Dietetics              DI     yes      yes

Discharge Summary      DCS    yes      yes

Brief Disch Summary    BDS    yes      yes

Referral Count         GECC   yes      yes

Referral Categories    GECH   yes      yes

Global Assess Funct    GAF    yes      yes

Imaging Impression     II     yes      yes

Sel Image Impression   SII    yes      yes

Imaging Profile        IP     yes      yes

Imaging Status         IS     yes      yes

Blood Availability     BA     yes      yes

Blood Transfusions     BT     yes      yes

Chem &amp; Hematology      CH     yes      yes

Lab Cum Selected       SCLU   yes      yes

Lab Cum Selected 1     SCL1   yes      yes

Lab Cum Selected 2     SCL2   yes      yes

Lab Cum Selected 3     SCL3   yes      yes

Lab Cum Selected 4     SCL4   yes      yes

Cytopathology          CY     yes      yes

Electron Microscopy    EM     yes      yes

Microbiology           MIC    yes      yes

Brief Microbiology     BMIC   yes      yes

Lab Orders             LO     yes      yes

Brief Lab Orders       BLO    yes      yes

Surgical Pathology     SP     yes      yes

Lab Tests Selected     SLT    yes      yes

MAG Imaging            MAGI   yes      yes

Admission/Discharge    ADC    yes      yes

ADT History            ADT    yes      yes                            temporary

ADT History Expanded   EADT   yes      yes

Fut Clinic Visits      CVF

Past Clinic Visits     CVP    yes      yes

Patient Contacts       CON

Demographics           DEM

Brief Demographics     BDEM

Disabilities           DS

Discharge Diagnosis    DD     yes      yes

Discharges             DC     yes      yes

MH Clinic Fut Visits   MHFV

ICD Procedures         PRC    yes      yes

ICD Surgeries          OPC    yes      yes

Transfers              TR     yes      yes

Treating Specialty     TS     yes      yes

Med Abnormal           MEDA   yes      yes

Med Brief Report       MEDB   yes      yes

Med Full Captioned     MEDC   yes      yes

Med Full Report        MEDF   yes      yes

Med (1 line) Summary   MEDS   yes      yes

MH Physical Exam       MHPE   yes      yes

MH Suicide PRF Hx      MHRF

MH Treatment Coor      MHTC

MHA Admin List         MHAL   yes      yes

MHA Score              MHAS   yes      yes

Detail Display         MHVD

Summary Display        MHVS

Med Reconciliation     MRR1

Med Reconciliation     MRT1

Medication

Reconciliation     MRP

Medication Worksheet   MRT2

Medication Worksheet   MRT2

Next of Kin            NOK

Non VA Meds            RXNV   yes      yes

Oncology               ONC

Current Orders         ORC             yes

Education              ED     yes      yes

Education Latest       EDL             yes

Exams Latest           EXAM            yes

Health Factors         HF     yes      yes

Health Factor Select   SHF    yes      yes

Immunizations          IM

Location of Home       LH                                             permanent

Outpatient Diagnosis   OD     yes      yes      yes    yes    yes

Outpatient Encounter   OE     yes      yes      yes    yes    yes

Skin Tests             ST

Treatments Provided    TP     yes      yes                            permanent

IV Pharmacy            RXIV            yes

Outpatient Pharmacy    RXOP            yes

Unit Dose Pharmacy     RXUD            yes

Active Problems        PLA                             yes    yes

All Problems           PLL                             yes    yes

Inactive Problems      PLI                             yes    yes

Progress Notes         PN     yes      yes

Brief Progress Notes   BPN    yes      yes

Selected Prog Notes    SPN    yes      yes

Remote Active Meds

(Tool #4)          MRT4

Spinal Cord Dysfunct   SCD    yes      yes

NON OR Procedures      NSR    yes      yes

Surgery Only Reports   SRO    yes      yes

Surgery Rpt (OR/NON)   SR     yes      yes

Brief Surgery Rpts     BSR    yes      yes

Selected NON-OR Proc   SNSR   yes      yes

URINALYSIS             URIN   yes      yes

Vital Signs            VS     yes      yes

Detailed Vitals        VSD    yes      yes

Vital Signs Outpat.    VSO    yes      yes

Vital Signs Selected   SVS    yes      yes

Vital Select Outpat.   SVSO   yes      yes

HEALTH SUMMARY COMPONENT LIST                  JUL 31,2001  12:27    PAGE 1

Component                     Occur.   Time     Hosp.  ICD    Prov.

Name                   Abbr.  Limits?  Limits?  Loc.?  Text?  Narr.?  Disabled?

-------------------------------------------------------------------------------

Selected Prog Notes    SPN    yes      yes

Spinal Cord Dysfunct   SCD    yes      yes

NON OR Procedures      NSR    yes      yes

Surgery Only Reports   SRO    yes      yes

Surgery Rpt (OR/NON)   SR     yes      yes

Brief Surgery Rpts     BSR    yes      yes

Selected NON-OR Proc   SNSR   yes      yes

URINALYSIS             URIN   yes      yes

Vital Signs            VS     yes      yes

Detailed Vitals        VSD    yes      yes

Vital Signs Outpat.    VSO    yes      yes

Vital Signs Selected   SVS    yes      yes

Vital Select Outpat.   SVSO   yes      yes

Select Information Menu Option: &lt;Enter&gt;

##### List Health Summary Component Descriptions

This option provides you a detailed list of all health summary components.

**Note** : Although this list can be displayed, it is most beneficial if printed and used as reference material. *Only a small portion of the list is shown in the example belowa complete copy is in Appendix C of this manual* .

**1.** Select List Health Summary Component Descriptions from the Information Menu.

Select Information Menu Option: **?**

1      Inquire about a Health Summary Type

2      List Health Summary Types

3      Inquire about a Health Summary Component

4      List Health Summary Components

5      List Health Summary Component Descriptions

CHOOSE 1-5: **5**

**2.** Select the printer you want to print to, or press &lt;Enter&gt; for a screen display.

DEVICE: **PRINTERNAME**

**3.** A list similar to the following is printed.

HEALTH SUMMARY COMPONENT DESCRIPTION LIST      JUL 31,2001  12:31    PAGE 1

Component

Name                              Abbrev.

Description

-------------------------------------------------------------------------------

Advance Directive                 CD

This component contains advance directive notes entered using the Text

Integration Utilities (TIU).  Advance Directives are a type a progress

note which includes clinical information that clinicians need to be

alerted to.  Time and maximum occurrent limits apply to this component.

If this component is printed to either a CRT or another device type,

information will include title, text of note, electronic signature block,

and date/time posted.

Brief Adv React/All               BADR

This component provides patient allergy/adverse reaction information from

the Allergy Tracking System. It provides a brief patient list of all known

food, drug and environmental allergies or adverse reactions (e.g., hay

fever).

Adv React/Allerg                  ADR

This component provides patient allergy/adverse reaction information from

the Allergy Tracking System. It provides a list of all known food, drug

and environmental allergies or adverse reactions (e.g., hay fever). Data

element included are type of reaction, mechanism of reaction, causative

agent, verification status, signs/symptoms for the reaction, the

originator, and comments.

Reminder Brief                    CMB

This is a brief version of the CLINICAL REMINDERS MAINTENANCE component.

Reminders Due                     CR

This component lists only clinical reminders that are due now. If the date

the reminder was last satisfied is known it is listed under LAST.

Otherwise the word unknown is printed.

Reminder Maintenance              CM

This component lists reminders that are due and not due as does the CRS

component. In addition it shows why the reminder is due or not due.

Reminders Summary                 CRS

This component is similar to PCE CLINICAL REMINDERS DUE except that it

shows all reminders not just those that are due. The information will

include the NEXT due date, or N/A, and the LAST DATE. N/A reminders will

be displayed unless the IGNORE ON N/A field is set.

### CPRS Reports Tab “Health Summary Types List” Menu

Use the options in the CPRS Reports Tab “Health Summary Types List” Menu to select the Health Summary Types to list on the Reports Tab, arrange the order of these Health Summaries on the list, and to the users’ preferences.

The CPRS Reports Tab ‘Health Summary Types List’ Menu contains four options.

1      Display 'Health Summary Types List' Defaults

2      Precedence of 'Health Summary Types List'

3      Method of compiling 'Health Summary Types List'

4      Edit 'Health Summary Types List' Parameters

*See Chapter 3, section 4 for more complete descriptions of these options.*

#### Using Health Summary in CPRS

**To display a Health Summary, follow these steps.**

1. Select a patient after you enter the CPRS system.
2. Select the Reports tab.
3. Under the Available Reports box on the left side of the screen, click the “+” sign in order to expand the Health Summary heading.
4. Select a Health Summary by clicking on the summary that you would like to see. After you have selected a summary, the appropriate data is displayed on the right side of the screen.
5. If you select Ad Hoc Report, you will be presented with a window for selecting the Health Summary types you wish to see.
6. Use the scroll bar on the right to scroll through the different sections of the Health Summary.

<!-- image -->

**AD HOC Report Selection Window**

<!-- image -->

**Health Summary Display (Note the Local Title and Standard Title display, as a result of patch 81)**

TWO HSPROVIDER

HSPROVIDER,TWO

<!-- image -->

**Example: Display of Outpatient Diagnosis and Outpatient Encounter Components – as a result of GMTS*2.7*101**

**ICD-9 Example**

<!-- image -->

**ICD-10 Example**

## Chapter 3: Advanced Features

**1. Health Summary Components**

**2. Health Summary Types**

**3. Health Summary Objects**

**4. Build Health Summary Options**

**5.  User Preferences**

**6.  Site Preferences**

# Chapter 3 – Health Summary Advanced Features

Chapter 3 contains information about creating and modifying Health Summary Types, Components, Objects and setting User Preferences.

### Health Summary Components

A health summary is made up of a series of data groupings called *components.*

A health summary component is summarized patient data extracted from various VISTA software packages. Health summary components contain a variety of patient data, ranging from Allergies to Vital Sign information. Each of the components represents a major class of VISTA data. The health summary component contains pre-determined information, but users who are given the Enhanced Menu can set occurrence and time limits, hospital location, ICD text, provider narrative, selection items, briefness, and the header name.

#### Brief, Selected, and Cumulative Selected Components

Health summary has several kinds of specialized components that give narrower views of data. Three of these are *brief* , *selected,* or *cumulative selected* .

A *brief* component is a shortened compilation of data (e.g., Brief Demographics (BDEM)).

A *selected* component indicates that a user can choose any number of selection items (e.g., tests, measurements, or procedures) available in the Laboratory, Nursing (Vital Signs), Radiology, and Patient Care Encounter (PCE) packages. For example, the Selected Lab Tests (SLT) component allows you to select any number of Lab tests, and presents collection date/time, specimen, test name, result, units, and reference range in a vertical format.

Lab Tests Selected, Vital Signs Selected, Radiology Impression Selected, Health Factors Select, and Measurement Selected are the current *selected* components in Health Summary as defined and exported by the package developers.

A *cumulative selected* component allows you to choose cumulative Lab tests, displayed in a horizontal, columnar format. The Lab Cumulative Selected (SCLU) component lets you choose an *unlimited* number of cumulative Lab tests. The Lab Cumulative Selected 1 through Lab Cumulative Selected 4 (SCL1, SCL2, SCL3, SCL4) components limit you to choosing seven cumulative tests each.

**Note:** If a VistA package is unavailable at your facility, your IRM staff may disable the corresponding components. The following components are available in this version of Health Summary (but may not necessarily be available at your site).

CD    Advance Directive   CY    Cytopathology       RXNV  Non VA Meds

BADR  Brief Adv React/All EM    Electron Microscopy ONC   Oncology

ADR   Adv React/Allerg    MIC   Microbiology        ORC   Current Orders

BNC   BRAND NEW COMPONENT BMIC  Brief Microbiology  ED    Education

CPB   Clin Proc   Brief   LO    Lab Orders          EDL   Education Latest

CMB   Reminder Brief      BLO   Brief Lab Orders    EXAM  Exams Latest

CR    Reminders Due       SP    Surgical Pathology  HF    Health Factors

CF    Reminders Findings  SLT   Lab Tests Selected  SHF   Health Factor Select

CLD   Reminders Last Done MAGI  MAG Imaging         IM    Immunizations

CM    Reminder MaintenanceADC   Admission/Discharge OD    Outpatient Diagnosis

CRS   Reminders Summary   ADT   ADT History         OE    Outpatient Encounter

CW    Clinical Warnings   EADT  ADT History ExpandedST    Skin Tests

CP    Comp. &amp; Pen. Exams  CVF   Fut Clinic Visits   RXIV  IV Pharmacy

CNB   Brief Consults      CVP   Past Clinic Visits  RXOP  Outpatient Pharmacy

CN    Crisis Notes        CON   Patient Contacts    RXUD  Unit Dose Pharmacy

DI    Dietetics           DEM   Demographics        PLA   Active Problems

DCS   Discharge Summary   BDEM  Brief Demographics  PLL   All Problems

BDS   Brief Disch Summary DS    Disabilities        PLI   Inactive Problems

ENV   Full Environment    DD    Discharge Diagnosis       PROBLEM LSIT

DC    Discharges          PN    Progress Notes

AVC   GEC                 MHFV  MH Clinic Fut VisitsBPN   Brief Progress Notes

Press RETURN to continue or '^' to exit:

GECC  Referral Count      PRC   ICD Procedures      SPN   Selected Prog Notes

GECH  Referral Categories OPC   ICD Surgeries

GAF   Global Assess Funct TR    Transfers           SCD   Spinal Cord Dysfunct

HS    HS Environment      TS    Treating Specialty  NSR   NON OR Procedures

II    Imaging Impression  MEDA  Med Abnormal        SRO   Surgery Only Reports

SII   Sel Image ImpressionMEDB  Med Brief Report    SR    Surgery Rpt (OR/NON)

IP    Imaging Profile     MEDC  Med Full Captioned  BSR   Brief Surgery Rpts

IS    Imaging Status      MEDF  Med Full Report     SNSR  Selected NON OR Proc

MEDS  Med (1 line) SummaryTC    TRAINING COMPONENT

MHPE  MH Physical Exam    URIN  URINALYSIS

BA    Blood Availability  MHRF  MH Suicide PRF Hx   VS    Vital Signs

BT    Blood Transfusions  MHTC  MH Treatment Coor   VSD   Detailed Vitals

CH    Chem &amp; Hematology   MHAL  MHA Admin List      VSO   Vital Signs Outpat.

SCLU  Lab Cum Selected    MHAS  MHA Score           SVS   Vital Signs Selected

SCL1  Lab Cum Selected 1  MHVD  Detail Display      SVSO  Vital Select Outpat.

SCL2  Lab Cum Selected 2  MHVS  Summary Display     ZW    ZW HS ENVIRONMENT

SCL3  Lab Cum Selected 3  MRT2  Medication Worksheet

SCL4  Lab Cum Selected 4  NOK   Next of Kin

**Note:** Use the *Information Menu option* (available in all Health Summary menus) to get online lists of the information contained in each health summary component or health summary type.

### Health Summary Types

A health summary *type* is a structure similar to a template, composed of health summary components. The Health Summary package exports four demonstration health summary types (SAMPLE 1, SAMPLE 2, SAMPLE 3, and SAMPLE 4) for use in training and for informational purposes. The package also exports the national type GMTS AD HOC OPTION.

Anyone with the Enhanced Menu or Coordinator’s Menu can create customized health summary types for personal use or for use by others.

**Note:** You can make temporary changes to *selected* components of any health summary type at any time during the display process. Enter a health summary component abbreviation equal to C (e.g., ADR=C) to temporarily change a component’s Occurrence Limit, Time Limit, Hospital Location Display, ICD Text Display, Provider Narrative Display, and Selection Items. Any components added to an existing health summary type or any changes to the defined time and occurrence limits do not create a permanent change to the health summary type.

**Demonstration Health Summary Types**

SAMPLE 1

SAMPLE 2

SAMPLE 3

SAMPLE 4

**Nationally Exported Health Summary Type**

**GMTS HS ADHOC OPTION**

This type is maintained by the sites using Health Summary options.

GMTS IRM ADHOC LOAD            Rebuild Ad Hoc Health Summary Type

GMTS IRM ADHOC SUMMARY EDIT    Edit Ad Hoc Health Summary Type

**Remote Data View Types**

Health Summary Patch 29 (GMTS*2.7*29) exports Health Summary Types for using Remote Data Views. Once these are in place and the proper parameters have been set, you can access remote data from other VA facilities.

You can view remote clinical data using any Health Summary Type that has an identically named Health Summary Type installed at both the local and remote sites. However, for non-nationally exported health summary reports, the content of the report is subject to the report structure and configuration defined at the remote site.

**Example scenarios:**

**Locally Developed Health Summary Types**

Both your site and the remote site have a health summary report called “SURGERY.” As a minimum, that is all that is required to ask for the remote data. Your site has set up the SURGERY health summary report to include the health summary component “Surgery Rpt (OR/NON)” with a time limit of 4 years and an occurrence limit of 10. The remote site has set up the SURGERY health summary report to include the “Surgery Only Reports” component with a time limit of 1 year or 10 occurrences. You will be expecting a report containing both OR Procedures and non-OR Procedures for the last 4 year (or 10 occurrences). You will only receive the OR Procedures for the past year (or 10 occurrences). You will not receive any non-OR Procedures in the remote report. You will get the report as defined at the remote site. If the remote site has assigned the security key SROREP to the health summary report SURGERY, then you will not be able to retrieve any surgical data from the remote site using the “SURGERY” report. This is because you do not own any security keys at the remote site.

**Nationally Exported Health Summary Types (RDV)**

It is much different for health summary types exported nationally in support of remote data views. Nationally exported health summary types only contain those health summary components that do not require input other than a date range. Selection items are not allowed for remote data views. For the nationally exported types, not only do the names match exactly from site to site, but the report structure and configuration will also match exactly from site to site. The report format you observe at the local site will be identical to the remote site. The nationally exported health summary types help remove the guesswork and possible frustration of gathering information from other sites.

**Exported Remote Data View Types**

Patch 29 (GMTS*2.7*29) adds the following Remote Data Views types.

REMOTE DEMO/VISITS/PCE (3M)

REMOTE MEDS/LABS/ORDERS (3M)

REMOTE TEXT REPORTS (3M)

REMOTE CLINICAL DATA (3M)

REMOTE CLINICAL DATA (1Y)

REMOTE DEMO/VISITS/PCE (1Y)

REMOTE MEDS/LABS/ORDERS (1Y)

REMOTE TEXT REPORTS (1Y)

REMOTE CLINICAL DATA (4Y)

REMOTE LABS LONG VIEW (12Y)

REMOTE LABS ALL (1Y)

REMOTE LABS ALL (3M)

REMOTE DIS SUM/SURG/PROD (12Y)

REMOTE OUTPATIENT MEDS (6M)

**Placing RDV types on the Parameters List**

Add the nationally exported Remote Data View Health Summary Types to the Health Summary GUI reports list in a sequence desirable to the site, using the CPRS Manager Menu [ORMGR].

Select CPRS Manager Menu Option: **PE** CPRS Configuration (Clin Coord)

Select CPRS Configuration (Clin Coord) Option: **GP** GUI Parameters

Select GUI Parameters Option: **HS** GUI Health Summary Types

Allowable Health Summary Types may be set for the following:

2   User          USR    [choose from NEW PERSON]

4   System        SYS    [DEVCUR.REDACTED]

Enter selection: **4**

------- Setting Allowable Health Summary Types for System: -------

Select Sequence: **6**

Are you adding 6 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 6// **&lt;Enter&gt;** 6

Health Summary: **REMOTE**

Health Summary: REM CM for VA-// REMOTE

1   REMOTE CLINICAL DATA (1Y)

2   REMOTE CLINICAL DATA (3M)

3   REMOTE CLINICAL DATA (4Y)

4   REMOTE DEMO/VISITS/PCE (1Y)

5   REMOTE DEMO/VISITS/PCE (3M)

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5:

6   REMOTE DIS SUM/SURG/PROD (12Y)

7   REMOTE LABS ALL (1Y)

8   REMOTE LABS ALL (3M)

9   REMOTE LABS LONG VIEW (12Y)

10  REMOTE MEDS/LABS/ORDERS (1Y)

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-10:

11  REMOTE MEDS/LABS/ORDERS (3M)

12  REMOTE OUTPATIENT MEDS (6M)

13  REMOTE TEXT REPORTS (1Y)

14  REMOTE TEXT REPORTS (3M)

CHOOSE 1-14: **1** REMOTE CLINICAL DATA (1Y)

Select Sequence: **7**

Are you adding 7 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 7// **&lt;Enter&gt;** 7

Health Summary: **REMOTE MEDS**

1   REMOTE MEDS/LABS/ORDERS (1Y)

2   REMOTE MEDS/LABS/ORDERS (3M)

CHOOSE 1-2: **1** REMOTE MEDS/LABS/ORDERS (1Y)

***Etc.***

**Warning:** If you set up *user* parameters (#2 above), the user parameters will overwrite all settings previously set in the system settings, and the user will not see the remote data views set in the system settings.

**How Do I Know a Patient Has Remote Medical Data?**

As part of opening a patient record, CPRS checks in the Treating Specialty file to see if the selected patient has been seen in other VA facilities. If the patient has remote data, the words on the Remote Data button turn blue as shown in the image below. If there is no remote data for the selected patient, the letters are gray. When you click on the Remote Data button, you see a list of treatment facilities and the last date the selected patient was seen at those facilities.

<!-- image -->

*For more information about setting up and using Remote Data Views, see CPRS documentation.*

### Health Summary Objects

Health Summary Objects are Health Summary Types saved in a temporary array for insertion into another electronic document. The primary user of Health Summary Objects is Text Integration Utility (TIU). Patch TIU*1.0*135 provides a method for creating TIU objects associated with Health Summary Objects. Health Summary Objects are stored in file 142.5, along with a series of flags that determine how a Health Summary Object will be displayed.

The following items can be controlled when displaying an object.

Object Label				If a Health Summary Object was given a label, then this label may be either printed or suppressed in the parent document.

Report Period				The object can have a different time limit from the Health Summary Object it uses. Examples:   2D, 3W, 6M

Suppress Component w/o Data	You can choose not to display Health Summary Components that do not have data.

Suppress Header			You can choose not to display the standard Health Summary Header when using the object in another document. If you choose to suppress the standard Health Summary Header, then you may include any single portion/line of the Health Summary Header; these include:

Report Date and Time

Confidentiality Banner

Report Header

Deceased Patient Information

Component Header			You can choose to suppress the standard component header. If you do not use the standard component header, then the component name will be used. If you choose to use the standard component header, you may also include the time and occurrence limits with the header, or underline the header, and/or print a blank line after the component header.

### Build Health Summary Type Menu

Use the options in the Build Health Summary Type menu (on the Health Summary Coordinator's Menu) to create health summary types consisting of the components you designate or have been asked to create by a health summary user. *Remember* : It is the health summary *type* that determines what information is included on a health summary.

The Build Health Summary Type menu contains five options of which three of these are menus.

1  Create/Modify Health Summary Type

2  Delete Health Summary Type

3  Health Summary Objects Menu

1  Create/Modify Health Summary Object

2  Inquire about a Health Summary Object

3  Test a Health Summary Object

4  Delete Health Summary Object

5  Export/Import a Health Summary Object

1  Export a Health Summary Object

2  Import/Install a Health Summary Object

4  Information Menu

1  Inquire about a Health Summary Type

2  List Health Summary Types

3  Inquire about a Health Summary Component

4  List Health Summary Components

5  List Health Summary Component Descriptions

5  Print Health Summary Menu

1  Patient Health Summary

2  Ad Hoc Health Summary

3  Range of Dates Patient Health Summary

4  Visit Patient Health Summary

5  Hospital Location Health Summary

6  Batch Print of All Clinics by Visit Date

Options 1 and 2 are used to create, modify, and delete health summary *types* .

Option 3 is a menu used to create, modify, delete, test, display, export or import Heath Summary Objects.

Option 4 consists of six information options that provide detailed information on health summary types and components.

Option 5 is included for your convenience, so you don’t have to leave the menu to get patient health summary information.

Options 1, 2 and 3 are explained in detail on the following pages.

#### Create/Modify Health Summary Type

Use this option to:

1. Create a new health summary type by *copying* all or a few components from an existing health summary type.

1. Create a new health summary type from *scratch* , by selecting components one at a time and defining the occurrences, time limits, and selection items.

1. Modify an existing health summary type.

***Create Health Summary Type Example***

Two examples follow. In the first example, a health summary type is created by copying components from an existing health summary type. In the second example, a new health summary type is built from scratch.

***Example 1*** ***— Creating a health summary type by copying from an existing summary (assuming you have the GMTSMGR key):***

**1.** Select Create/Modify Health Summary Type from the Build Health Summary Type Menu on the Health Summary Coordinator’s Menu.

Select Build Health Summary Menu Option: **Create** /Modify Health Summary Type

**2.** Select a new name for a Health Summary Type.

Select Health Summary Type: **ICU ZZTEST**

ARE YOU ADDING ‘ICU ZZTEST’ AS A NEW HEALTH SUMMARY TYPE? **Y** (Yes)

NAME:  ICU ZZTEST// **&lt;Enter&gt;**

ICU ZZTEST is the NAME of the Health Summary Type. This name will appear in the health summary header. The word “CONFIDENTIAL” will appear in front of this name and the word “SUMMARY” will appear at the end to complete the header.

Name entered:  ICU ZZTEST

Generated Health Summary header: CONFIDENTIAL ICU ZZTEST SUMMARY.

**3.** Enter a title if you wish to replace NAME with the title in the health summary header. For example, if you enter the Name as ICU, and the Title as INTENSIVE CARE UNIT, the header that will be shown will be CONFIDENTIAL INTENSIVE CARE UNIT SUMMARY.

TITLE: **INTENSIVE CARE**

**4.** Enter yes or no to the prompt about whether to suppress components’ headings when those components don’t contain data. For health summary types that are displayed on the screen, this component will still be displayed with a “No data available” message. This is done to eliminate confusion that may occur when jumping between components.

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **Y** YES

**5.** Enter  0 **,** 1, or 2 to the prompt about suppressing sensitive print data. Depending on the response to this question, the SSN/DOB information will appear in one of the following formats on printed Health Summaries.

0. 4 digit SSN and No DOB

1. Full 9 digit SSN and full DOB

2. No SSN and No DOB

SUPPRESS SENSITIVE PRINT DATA: **0** 4 DIGIT SSN

**6.** Enter Lock and Owner, if appropriate. Enter a LOCK if you wish to restrict edit/delete access to your health summary type. You must hold the GMTSMGR security key to enter a lock. You are automatically considered the owner, unless you hold the GMTSMGR key. If you hold the GMTSMGR key you have to designate yourself or someone else as the owner.

LOCK: **&lt;Enter&gt;**

OWNER: **&lt;Enter&gt;**

**7.** If you want to copy components from an existing Health Summary Type, accept the default at that question and then enter the name of the Type to copy from. The components for that Type are then listed.

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// &lt;Enter&gt;

Select Health Summary Type to copy from: SAMPLE 1

The Following Components are Available:

BDEM	Brief Demographics	RS	Radiology Status

BLO	Brief Lab Orders		SCLU 	Lab Cum Selected

BMIC	Brief Microbiology	DC	Discharges

BSR	Brief Surgery Rpts

**8.** Select the components you want to include in your new type. You can only select components to copy from the SAMPLE 1 health summary type. If you need to add a component NOT in the SAMPLE 1 health summary type, you can do so at the second Select COMPONENT: prompt, shown below. You can enter “ALL” at this prompt to select all the components in the Brief Clinical health summary type.

Select COMPONENT(S): **vs,blo,dc,sclu**

VS is not a valid selection.

For entry “VS” re-enter: **&lt;Enter&gt;**

**9.** You will then see a list of the parameters you have chosen, followed by a list of the components and their selection items.

Type Name: ICU ZZTEST

Title:

Owner: HSUSER,ONE

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

SUPPRESS SENSITIVE PRINT DATA: 1

Max        Hosp  ICD   Prov

Abb.  Order  Component Name     Occ  Time  Loc   Text  Narr   Selection

------------------------------------------------------------------------

BLO	   5	  Brief Lab Orders	  10   1Y

DC	   10	  Discharges    	  10

SCLU      15	  Lab Cum Selected	  10   1Y 				  SODIUM

POTASSIUM

CHLORIDE

CALCIUM

AMYLASE

CREATININE

UREA NITRO

GLUCOSE

**10.** You can now enter components not in the SAMPLE 1 Health Summary Type. You will also be prompted to enter SUMMARY ORDER, OCCURRENCE LIMIT, TIME LIMIT, and HEADER NAME, and then asked if you wish to review the Summary Type structure.

Select COMPONENT: **VS** VITAL SIGNS  VS *Re-enter the “VS” component here.*

SUMMARY ORDER: **20**

OCCURRENCE LIMIT: **5**

TIME LIMIT: **1Y**

HEADER NAME:  Vital Signs// **&lt;Enter&gt;**

Select COMPONENT: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **Y** YES

Type Name: ICU ZZTEST

Title:

Owner: HSUSER,ONE

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

SUPPRESS SENSITIVE PRINT DATA:

Max        Hosp  ICD   Prov

Abb.  Order  Component Name     Occ  Time  Loc   Text  Narr   Selection

------------------------------------------------------------------------

BLO	   5	 Brief Lab Orders	  10   1Y

DC	  10	 Discharges    	  10

SCLU     15	 Lab Cum Selected	  10   1Y 				  SODIUM

POTASSIUM

CHLORIDE

CALCIUM

AMYLASE

CREATININE

UREA NITRO

GLUCOSE

VS	20	 Vital Signs	  5    1Y

Select COMPONENT: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;Enter&gt;**

Please hold on while I resequence the summary order....

Select Health Summary Type: **&lt;Enter&gt;**

***Example 2 —*** *Creating a Health Summary Type from scratch:*

Select Health Summary Type: **CCU ZZTEST**

ARE YOU ADDING ‘CCU ZZTEST’ AS A NEW HEALTH SUMMARY TYPE? **Y** (YES)

NAME:  CCU ZZTEST// **&lt;Enter&gt;**

TITLE: **&lt;Enter&gt;**

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **&lt;Enter&gt;**

SUPPRESS SENSITIVE PRINT DATA: **1** 4 DIGIT SSN

LOCK: **&lt;Enter&gt;**

OWNER: **&lt;Enter&gt;**

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// **NO**

Select COMPONENT: **DEM** MAS DEMOGRAPHICS  DEM

SUMMARY ORDER:  5// **&lt;Enter&gt;** *This is the component order default assigned by the program.*

HEADER NAME:  Demographics// **&lt;Enter&gt;**

Select COMPONENT: **LO** LAB ORDERS   LO

SUMMARY ORDER:  10// **&lt;Enter&gt;**

OCCURRENCE LIMIT: **20**

TIME LIMIT: **1Y**

HEADER NAME: Lab Orders// **&lt;Enter&gt;**

**Select COMPONENT:  &lt;Enter&gt;**

***Continue building the health summary type with more components until it is completed.***

Do you wish to review the Summary Type structure before continuing? NO//

**&lt;Enter&gt;**

Please hold on while I resequence the summary order..

Select Health Summary Type: **&lt;Enter&gt;**

***Modify (Edit) Health Summary Type Example***

Health summary types can be edited or deleted only by the owner, by holders of the GMTSMGR key, or holders of a lock associated with the type to be edited. Alteration of any health summary type is restricted to its owner.

***Example 1 —*** *Editing the Summary Component Order:*

Select Health Summary Coordinator Menu Option: **Create** /Modify Health Summary Type

Select Health Summary Type: **ICU ZZTEST**

NAME:  ICU ZZTEST// **&lt;Enter&gt;**

TITLE: **ICU PATIENT INFO**

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **&lt;Enter&gt;**

SUPPRESS SENSITIVE PRINT DATA: 1 4 DIGIT SSN

LOCK: **&lt;Enter&gt;**

OWNER: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **Y**

YES

HEALTH SUMMARY TYPE INQUIRY

Type Name: ICU ZZTEST

Title:

Owner: HSUSER,TWO

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

SUPPRESS SENSITIVE PRINT DATA: 1 4 DIGIT SSN

Max        Hosp  ICD   Prov

Abb.  Order  Component Name     Occ  Time  Loc   Text  Narr   Selection

------------------------------------------------------------------------

BLO	   5	 Brief Lab Orders	  10   1Y

DC	  10	 Discharges    	  10

SCLU  15	 Lab Cum Selected	  10   1Y 				  SODIUM

POTASSIUM

CHLORIDE

CALCIUM

AMYLASE

CREATININE

UREA NITRO

GLUCOSE

VS	20	 Vital Signs	  5    1Y

Select COMPONENT: **VS** VITAL SIGNS  VS

VITAL SIGNS is already a component of this summary.

Select one of the following:

E	Edit component parameters

D	Delete component from summary

Select Action: **Edit**

SUMMARY ORDER: 20// **15**

LAB CUMULATIVE SELECTED Already exists at SUMMARY ORDER 15

Select one of the following:

O         Overwrite

I         Insert Before

A         Append After

Select Action: **Insert** Before

Inserted as SUMMARY ORDER: 12 VITAL SIGNS   “ *12 VITAL SIGNS” was entered*

*by the program.*

HEADER NAME:  Vital Signs// **&lt;Enter&gt;**

OCCURRENCE LIMIT: **&lt;Enter&gt;**

TIME LIMIT: **&lt;Enter&gt;**

Select COMPONENT: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **N**

NO

Please hold on while I resequence the summary order........ *The package*

*automatically resequences the summary order in multiples of five.*

Select Health Summary Type: **&lt;Enter&gt;**

**Example 2 —** *Editing the Maximum Occurrences, Time Limit, Header Name, and Selection Items:*

Select Health Summary Enhanced Menu Option: **Create** /Modify Health Summary Type

Select Health Summary Type: **ICU ZZTEST**

NAME:  ICU ZZTEST// **&lt;Enter&gt;**

TITLE: ICU PATIENT INFO// **&lt;Enter&gt;**

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **&lt;Enter&gt;**

SUPPRESS SENSITIVE PRINT DATA: 1 4 DIGIT SSN

LOCK: **&lt;Enter&gt;**

OWNER: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO//

**&lt;Enter&gt;** *.*

Select COMPONENT: **SCLU** LAB CUMULATIVE SELECTED   SCLU

LAB CUMULATIVE SELECTED is already a component of this summary.

Select one of the following:

E	Edit component parameters

D	Delete component from summary

Select Action: **EDIT**

SUMMARY ORDER:  20// **&lt;Enter&gt;**

OCCURRENCE LIMIT:  10// **5**

TIME LIMIT:  1Y// **6M**

HEADER NAME: Lab Cum Selected// **&lt;Enter&gt;** *Or enter a new name for the component.*

Current selection items are:  SODIUM

POTASSIUM

CHLORIDE

CALCIUM

AMYLASE

CREATININE

UREA NITROGEN

GLUCOSE

Select new items one at a time in the sequence you want them displayed.

You may select any number of items.

Select SELECTION ITEM: **GLUCOSE** *You may add or delete selection*

*items at this prompt.  To delete “Calculated*

*Osmolality” enter the at-sign @ at this*

*prompt.  To add any valid Lab test, enter the*

*test name at this prompt.*

Select SELECTION ITEM: **&lt;Enter&gt;**

Select COMPONENT: **&lt;Enter&gt;** *You may enter another component name for editing.*

***Example 3:*** *Deleting a health summary component from a health summary type.*

Select Health Summary Coordinator Menu Option: **Create** /Modify Health Summary Type

Select Health Summary Type: **ICU ZZTEST**

NAME:  ICU ZZTEST// **&lt;Enter&gt;**

TITLE: ICU PATIENT INFO// **&lt;Enter&gt;**

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **&lt;Enter&gt;**

SUPPRESS SENSITIVE PRINT DATA: **&lt;Enter&gt;**

LOCK: **&lt;Enter&gt;**

OWNER: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing?NO//&lt;Enter&gt;

***Or you could answer YES to refresh your memory on the components to edit.***

Select COMPONENT: **VS** VITAL SIGNS      VS

VITAL SIGNS is already a component of this summary.

Select one of the following:

E	Edit component parameters

D	Delete component from summary

Select Action: **DEL** ETE *Before pressing the return key you should be sure*

*you want to delete this component. After you identify*

*a component, it will be deleted with NO second chance*

*when you press the return key.*

Deleting Summary Order 15 VITAL SIGNS

Select COMPONENT: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;Enter&gt;**

Please hold on while I resequence the summary order.......

#### Delete Health Summary Type

This option lets you delete a health summary type.

**Note:** You must have the GMTSMGR key to delete health summary types.

Select Health Summary Enhanced Menu Option: **Delete** Health Summary Type

Select Health Summary Type: **ICU ZZTEST**

Are you sure you want to delete the ICU ZZTEST Health Summary type? NO// **Y** YES

Health Summary Type ICU ZZTEST Deleted!

Select Health Summary Type: **&lt;Enter&gt;** *You may enter another summary type for*

*deletion. Pressing return takes you back to*

*the Health Summary Coordinator’s menu.*

#### Health Summary Objects Menu

1	Health Summary Objects Menu [GMTS OBJ MENU]

1	Create/Modify Health Summary Object [GMTS OBJ ENTER/EDIT]

2	Inquire about a Health Summary Object [GMTS OBJ INQ]

3	Test a Health Summary Object [GMTS OBJ TEST]

4	Delete Health Summary Object [GMTS OBJ DELETE]

5	Export/Import a Health Summary Object [GMTS OBJ EXPORT/IMPORT]

1	Export a Health Summary Object [GMTS OBJ EXPORT]

2 	Import/Install a Health Summary Object [GMTS OBJ IMPORT/INSTALL]

#### Create/Modify Health Summary Object

**[GMTS OBJ ENTER/EDIT]**

This option allows the user to create or modify a Health Summary Object.  Objects are Health Summaries that may have their headers suppressed so they may be inserted into another document.

Select Build Health Summary Type Menu Option: **3** Health Summary Objects Menu

1      Create/Modify Health Summary Object

2      Inquire about a Health Summary Object

3      Test a Health Summary Object

4      Delete Health Summary Object

5      Export/Import a Health Summary Object ...

You have PENDING ALERTS

Enter  "VA to jump to VIEW ALERTS option

Select Health Summary Objects Menu Option: **1** Create/Modify Health Summary Object

Select HEALTH SUMMARY OBJECT: **MY TEST OBJECT**

Are you adding 'MY TEST OBJECT' as

a new HEALTH SUMMARY OBJECTS? No// **Y** (Yes)

Select Health Summary Type: **??** ***Enter ?? for a list of HS Types.***

Choose from:

4A PATIENT

AC CLINICAL SUMMARY               AC Clinical Data Summary

ACTIVE PROBLEMS                   Active Problems

AMBULATORY CARE

CLINICAL MAINTENANCE

CNH REFERRAL SUMMARY/PACKET

Clinical Procedures               Clin Proc

Current Orders                    Current Orders

DEMOGRAPHICS                      Demographics

DEMOGRAPHICS BRIEF                ADDRESS

DIABETES (1)

DIETITIAN

DISCHARGE SUMMARY                 Discharge Summary

DISPLAY APPOINTMENTS              PATIENT'S FUTURE APPOINTMENT

INITIAL ASSESSMENT

Medicine (Brief)                  Medicine, Brief Report

PCE EXTRACTS (SELECTED)           PCE EXTRACTS SELECTED

PCE IMMUNIZATIONS

PERIOPERATIVE ASSESS

RADIOLOGY PROFILE                 RADIOLOGY PROFILE

REMINDERS DUE

SAMPLE 1

SAMPLE 2

SAMPLE 3

SAMPLE 4

SURGERY

SURGERY REPORTS                   Surgery Reports

SURGICAL CASE REVIEW              SCR

SURGICAL PATH

SURGICAL-REPORT

Selected Labs (Diabetes)

VITALS (DETAILED)                 Detailed Vitals

Answer with Health Summary Type name, title, owner or hospital

location using the summary.  Your response must be at least 2

characters and no more than 30 characters and must not contain

an embedded up arrow

Select Health Summary Type: **SURGICAL PATH**

Do you want to overwrite the TIME LIMITS in the Health

Summary Type 'SURGICAL PATH'?  N// **??**

Example of Health Summary Type component TIME LIMITS

Abbr  Component Name                Max Occurrences  Time Limits

----------------------------------------------------------------

SP    Lab Surgical Pathology              10             2Y

Entering a new TIME LIMIT for the Health Summary Object will

overwrite the TIME LIMITS set the for individual components.

It must be alpha numeric and can not exceed 5 characters.

Examples:  3D, 6W, 3M, 1Y

Do you want to overwrite the TIME LIMITS in the Health

Summary Type 'SURGICAL PATH'?  N// **&lt;Enter&gt;** O

Print standard Health Summary Header with the Object?  N// **??**

Print the following lines from the standard Health Summary

Header with the Object?

1                                                  12/30/2002 13:54

2 *****************  CONFIDENTIAL HEALTH SUMMARY ******************

3 PATIENT NAME    000-00-0000     WARD/LOCATTION     DATE OF BIRTH

4 &lt;blank&gt;

5 PN - Progress Notes (max 10 occurrences or 1 year)

6 &lt;blank&gt;

Print standard Health Summary Header with the Object?  N// **&lt;Enter&gt;** O

Partial Header:

Print Report Date?  N// **??**

Print the report date/time with Health Summary Objects?

&gt;&gt;&gt;&gt;&gt;  1                                            DATE/TIME  &lt;&lt;&lt;&lt;&lt;

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

5 PN - Progress Notes (max 10 occ or 1 yr)

6 &lt;blank&gt;

Print Report Date?  N// **&lt;Enter&gt;** O

Print Confidentiality Banner?  N// **??**

Print the confidentiality banner with Health Summary Objects?

1                                             DATE/TIME

&gt;&gt;&gt;&gt;&gt;  2 *********** CONFIDENTIAL HEALTH SUMMARY ************  &lt;&lt;&lt;&lt;&lt;

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

5 PN - Progress Notes (max 10 occ or 1 yr)

6 &lt;blank&gt;

Print Confidentiality Banner?  N// **&lt;Enter&gt;** O

Print Report Header?  N// **??**

Print the report header with Health Summary Objects?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

&gt;&gt;&gt;&gt;&gt;  3 PATIENT NAME   000-00-0000   WARD/LOCATION       DOB  &lt;&lt;&lt;&lt;&lt;

&gt;&gt;&gt;&gt;&gt;  4 &lt;blank&gt;                                               &lt;&lt;&lt;&lt;&lt;

5 PN - Progress Notes (max 10 occ or 1 yr)

6 &lt;blank&gt;

Print Report Header?  N// **&lt;Enter&gt;** O

Print the standard Component Header?  Y// **??**

Print the standard component header with Health Summary Objects?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

&gt;&gt;&gt;&gt;&gt;  5 PN - Progress Notes (max 10 occ or 1 yr)              &lt;&lt;&lt;&lt;&lt;

|-------------------|

Print the standard Component Header?  Y// **&lt;Enter&gt;** ES

Use report time/occurrence limits?  N// **??**

Print report time and occurrence limits with the component header?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

&gt;&gt;&gt;&gt;&gt;  5 PN - Progress Notes (max 10 occ or 1 yr)              &lt;&lt;&lt;&lt;&lt;

|--------------------|

Use report time/occurrence limits?  N// **&lt;Enter&gt;** O

Underline Component Header?  N// **??**

Underline the standard component header with a single line of dashes?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

5 PN - Progress Notes

&gt;&gt;&gt;&gt;&gt;    -------------------                                   &lt;&lt;&lt;&lt;&lt;

Underline Component Header?  N// **&lt;Enter&gt;** O

Add a Blank Line after the Component Header?  N// **??**

Print a Blank Line after the Component Header?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

5 PN - Progress Notes

&gt;&gt;&gt;&gt;&gt;  6 &lt;blank&gt;                                               &lt;&lt;&lt;&lt;&lt;

Add a Blank Line after the Component Header?  N// **&lt;Enter&gt;** O

Print the date a patient was deceased?  N// **??**

Print the date deceased with Health Summary Objects?

1                                             DATE/TIME

2 ***********  CONFIDENTIAL HEALTH SUMMARY ************

3 PATIENT NAME    000-00-0000   WARD/LOCATION       DOB

4 &lt;blank&gt;

5 PN - Progress Notes (max 10 occ or 1 yr)

6 &lt;blank&gt;

*   &gt;&gt;&gt;&gt;&gt;  7              **  DECEASED  DATE/TIME  **              &lt;&lt;&lt;&lt;&lt;

* This is a conditional line of the Health Summary report

header which is only printed for deceased patients

Print the date a patient was deceased?  N// **&lt;Enter&gt;** O

Print a LABEL before the Health Summary Object?  N// **??**

Do you want to print a label before printing a Health Summary Object?

Both the label and object will be embedded in another document.

&lt;document text&gt;

&lt;object label&gt;

&lt;Health Summary object&gt;

&lt;document text continued&gt;

Print a LABEL before the Health Summary Object?  N// **YES**

Enter LABEL: **JG TEST OBJECT**

Suppress Components without Data?  N// **??**

If this field is set to 1 (YES) and a Health Summary component does

not have any data, the component will be suppressed.

If this field is NOT set to 1 (Null or 0 = NO) and the component does

not have any data, then the component will print with the statement

"No data available"

Example:

PN - Progress Notes

No data available

Suppress Components without Data?  N// **&lt;Enter&gt;**

OBJECT DESCRIPTION:

No existing text

Edit? NO// **YES**

==[ WRAP ]==[ INSERT ]=====&lt; OBJECT DESCRIPTION &gt;======[&lt;PF1&gt;H=Help ]====

**JG TEST OBJECT**

#### Inquire about a Health Summary Object

**[GMTS OBJ INQ]**

Display a Health Summary Object from file 142.5, to include an example of the object.

Select Health Summary Objects Menu Option: **2** Inquire about a Health Summary Object

Select Health Summary Object: **MY TEST OBJECT**

OBJECT NAME: MY TEST OBJECT

HEALTH SUMMARY TYPE:   SURGICAL PATH

REPORT PERIOD: UNSPECIFIED         PRINT REPORT DATE/TIME: NO

LABEL: UNSPECIFIED                 PRINT CONFIDENTIALITY BANNER: NO

PRINT LABEL: NO                  PRINT REPORT HEADER: NO

BLANK LINE AFTER LABEL: NO       PRINT COMPONENT HEADER: YES

SUPPRESS COMPONENTS W/O DATA: YES  PRINT TIME-OCCURRENCE LIMITS: NO

SUPPRESS HEADER: YES               UNDERLINE COMPONENT HEADER: NO

SUPPRESS DECEASED INFORMATION: YES BLANK LINE AFTER HEADER: NO

CREATOR: HSPROVIDER,ONE               CREATED: 12/30/2002 13:53

LAST MODIFIED: 12/30/2002 13:58

EXAMPLE:

SP - Surgical Pathology

&lt;component data&gt;

Press &lt;Return&gt; to Continue

<!-- image -->

**[GMTS OBJ TEST]**

This option allows the user to test a Health Summary Object by displaying the Object to the screen exactly as it would appear.

<!-- image -->

**[GMTS OBJ DELETE]**

This option is used to delete a Health Summary Object that you created.  You may not delete Health Summary Objects created by other people.

Select Health Summary Objects Menu Option: **4** Delete Health Summary

Object

Select Health Summary Object to Delete: **MY TEST OBJECT**

OBJECT: MY TEST OBJECT              HS TYPE: SURGICAL PATH

REPORT PERIOD: 8Y                 PRINT REPORT DATE/TIME: NO

LABEL: SURGICAL PATHOLOGY         PRINT CONFIDENTIALITY BANNER: NO

PRINT LABEL: YES                PRINT REPORT HEADER: NO

BLANK LINE AFTER LABEL: NO      PRINT COMPONENT HEADER: YES

SUPPRESS COMPONENTS W/O DATA: NO    PRINT TIME-OCCURRENCE LIMITS: NO

SUPPRESS HEADER: YES                UNDERLINE COMPONENT HEADER: YES

SUPPRESS DECEASED INFORMATION: YES  BLANK LINE AFTER HEADER: NO

CREATOR: HSUSER,ONE                CREATED: 09/24/2002 12:36

LAST MODIFIED: 09/24/2002 13:47

Delete Health Summary Object "MY TEST OBJECT"?  NO// **&lt;RET&gt;** YES

&lt;deleted&gt;

<!-- image -->

#### Export/Import a Health Summary Object

**[GMTS OBJ EXPORT/IMPORT]**

This menu contains options used to either export a Health Summary Object to a Mailman message or import a Health Summary Object by reading the data unpacked from a Mailman message using the Packman Utilities.  The options are described below.

#### Export a Health Summary Object

**[GMTS OBJ EXPORT]**

This option will allow a user to export a Health Summary Object and its corresponding Health Summary Type to a Mailman message, which can be sent to other accounts/sites for import.

<!-- image -->

##### Mailman Message Sent

<!-- image -->

**Note:** You will get an error message (Can not export a Health Summary Object using a Health Summary Type that contains Health Summary Components with Selected Items Health Summary Type ‘xxx’ contains Health Summary Component ‘xxx’ with Selected Items) if you attempt to export a Health Summary object whose type has locally created components.

#### Import/Install a Health Summary Object

**[GMTS OBJ IMPORT/INSTALL]**

This option is used to install a Health Summary Object exported using the GMTS OBJ EXPORT option. **The incoming Object must first be unpacked (using Packman utilities) from the incoming Mailman message.** Then this option is used.

If there is a Health Summary Type with the same name as the Health Summary being imported, you will be prompted to either use the existing Health Summary Type or to rename the incoming Health Summary Type. At no time will an existing Health Summary Type be overwritten.

##### Unpack Mailman Message

. . . Message

;Surgical Path

;0;SURGICAL PATH^^^^

;1,0;^142.01IA^5^1

;1,5,0;5^46^10^2Y^Surgical Pathology

;1,"B",5,5;

;1,"C",46,5;

;99;59071,51531

;"T";Surgical Path

Q

OBJ ; Health Summary Object

;MY TEST OBJECT

;0;MY TEST OBJECT^SURGICAL PATHOLOGY  ^^8Y^0^1^1^0^0^0^0^1^1^0^0^0^^^^0

Q

$END ROU GMTSOBX

Enter message action (in IN basket): Ignore// **X** tract PackMan

Select PackMan function: **6** INSTALL/CHECK MESSAGE

Warning:  Installing this message will cause a permanent update of globals and routines.

Do you really want to do this? NO// **&lt;RET&gt;** YES

Routines are the only parts that are backed up.  NO other parts

are backed up, not even globals.  You may use the 'Summarize Message'

option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately

if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// **NO**

No backup message built.

Line 18   Message #1108      Unloading Routine   GMTSOBX

Select PackMan function:

Enter message action (in IN basket): Ignore// **&lt;RET&gt;**

<!-- image -->

##### Import/Install Health Summary Object

<!-- image -->

**Note:** You will get an error message (Object not Found) if you haven’t unpacked the Object message before trying to install it. Also, If you try to install an object with the same name as one already in the file, an error message appears: “Can not install Health Summary Object ‘xxx’. A Health Summary Object with the same name already exists.”

### Print Health Summary

The Print Health Summary Menu (GMTS HS MENU) includes all of the various print options available for Health Summaries, allowing the user to generate Health Summaries by Patient, by Patient and a date range, by patient and an outpatient visit or an admission, by Location, for patients at all clinics, and on an Ad Hoc basis.

The Patient Health Summary option generates a Health Summary of a specified pre-defined Health Summary Type for a specified patient.

Depending on the response to the question about suppressing sensitive print data, the SSN/DOB information will appear in one of the following formats on your printed Health Summaries.

1. 4 digit SSN and No DOB

2. Full 9 digit SSN and full DOB

3. No SSN and No DOB

Select Build Health Summary Type Menu Option: 5  Print Health Summary Menu

1      Patient Health Summary

2      Ad Hoc Health Summary

3      Range of Dates Patient Health Summary

4      Visit Patient Health Summary

5      Hospital Location Health Summary

6      Batch Print of All Clinics by Visit Date

Select Print Health Summary Menu Option: 1  Patient Health Summary

Select Health Summary Type: JG1//    JG1

Select Patient(s): CPRS

1   CPRSPATIENT, F   (6680) ~

2   CPRSPATIENT, T   (8668) ~

CHOOSE 1-2: 2    CPRSPATIENT, T   (8668) ~

Another patient(s) can be selected.

Include Outpatient Pharmacy Action Profile (Y/N)? NO//

DEVICE: HOME//   HOME

05/29/2007 08:36

*************************  CONFIDENTIAL TEST SUMMARY  **************************

CPRSPATIENT,THREE    0000       1A(1&amp;2)

--------------------------- ADR - Adv React/Allerg ---------------------------

Title: ALLERGY/ADVERSE REACTION (AR)

No known allergies

Assessment date:   05/26/2005

Assessed by:   HSPROVIDER,TWO

Title:   Chief of Surgery

-------------------------- BDEM - Brief Demographics --------------------------

Address: Not available                    Phone:

Eligibility: SERVICE CONNECTED  0% to 50%       Age: 62

Sex: MALE

Race:

Inpat. Provider: HSPROVIDER,ONE                   Phone:

CPRSPATIENT,THREE    0000    1A(1&amp;2)

-------------------------- BDEM - Brief Demographics --------------------------

(continued)

Inpat. Attending: HSPROVIDER,ONE                   Phone: 47368

Digital Pager: 9993422

---------------- BDS - Brief Disch Summary (max 2 occurrences) ----------------

Admitted   Disch'd     Dictated By    Approved By    Cosigned   Status

12/20/2002 Present     HSPROVIDER,ONE HSPROVIDER,ONE            COMPLETED

12/20/2002 Present     HSPROVIDER,ONE HSPROVIDER,ONE            COMPLETED

### User Preferences

**CPRS Reports Tab 'Health Summary Types List' Menu**

Use the options in the CPRS Reports Tab ‘Health Summary Types List’ Menu to select the Health Summary Types to list on the Reports Tab, arrange the order of these Health Summaries on the list, and to the user’s preferences.

The CPRS Reports Tab ‘Health Summary Types List’ Menu contains four options.

1      Display 'Health Summary Types List' Defaults

2      Precedence of 'Health Summary Types List'

3      Method of compiling 'Health Summary Types List'

4      Edit 'Health Summary Types List' Parameters

**Display 'Health Summary Types List' Defaults**

Use this option to display the list of Health Summary Types that will be contained in the ‘Health Summary Types’ box on the Reports Tab in CPRS.

The display includes the precedence of parameters, the method for building the list, and finally the list that will appear on the Reports Tab in CPRS.

**Precedence of Parameters** - Health Summary Types can be established for the system and for the users.  Additionally, there are Nationally exported Health Summary Types.  This precedence indicates the order in which these types will be displayed (i.e., display user defined types before system defined types).

**Method** - The list can be built either by overwriting the list with each higher precedence of Health Summary Types or by appending each level of precedence to the list (prior to this option, the only choice was overwriting the list).

**List** - A list of Health Summary Types that will appear in the ‘Health Summary Types’ box on the Reports Tab will be listed.

**Note:** If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to display the 'Health Summary Types List' defaults.

*Without the GMTSMGR Key:*

Health Summary Types list for CPRS Reports Tab              JUL 17, 2001

------------------------------------------------------------------------

Precedence of Parameters:        USR;SYS;NAT

1  User preferences

2  System defined

3  National Health Summary Types

Method for building the List:    Append

Add User Defined Summary Types to the list, then

Append with System Defined Summary Types (if found), then

Add National Defined Summary Types (if found)

The Health Summary Types box will list the following Health Summary Types:

User defined types        1  GMTS HS ADHOC OPTION

2  SURGERY

3  RADIOLOGY

System defined types      4  DIABETES (1)

5  AC CLINICAL SUMMARY

6  PAIN MANAGEMENT

National types            7  REMOTE CLINICAL DATA (1Y)

8  REMOTE CLINICAL DATA (3M)

9  REMOTE CLINICAL DATA (4Y)

10  REMOTE DEMO/VISITS/PCE (1Y)

11  REMOTE DEMO/VISITS/PCE (3M)

12  REMOTE LABS ALL (1Y)

13  REMOTE LABS ALL (3M)

14  REMOTE LABS LONG VIEW (12Y)

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user preference.

**Precedence of 'Health Summary Types List'**

Use this option to select the defined Health Summary Types to include on the list and arrange them in the order (precedence) that they should appear on the list.

Currently there are three groups of Health Summary Types that may be predefined and made available on the Reports Tab of CPRS.

SYS	Health Summary Types may be defined for all users on the system.

USR	Health Summary Types may be defined for a single user on the system.

NAT	Nationally exported Health Summary Types (NAT) defined for system users or a single user are treated independently to keep them together in the list box.

In this option, you must first select those Health Summary Type groups (SYS, USR, or NAT) to include on the Reports Tab, then specify the order in which they will appear on the Reports Tab.

**Note:** If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to edit the precedence.

*Without the GMTSMGR Key:*

GUI Reports Tab, Health Summary Type List (Contents)

Include User Preferred Health Summary Types:  (Y/N)  Y// **&lt;Enter&gt;** ES

System Defined Health Summary Types:  (Y/N)  Y// **&lt;Enter&gt;** ES

National Types  (Remote Data Views):  (Y/N)  Y// **&lt;Enter&gt;** ES

You have selected multiple Health Summary types to be listed on the CPRS

reports tab, in the Health Summary Types box.  Now you must select the

order in which you want these to be displayed.

Order to Display Included Health Summary Types

1  User Preferred Health Summary Types

2  System Level Health Summary Types

3  Nationally Exported Health Summary Types

Select the 1st to be listed:  1// **&lt;Enter&gt;**

1  System Level Health Summary Types

2  Nationally Exported Health Summary Types

Select the 2nd to be listed:  1// **&lt;Enter&gt;**

You have selected three Health Summary Types, arranged

in the following order:

1    User Preferred Health Summary Types

2    System Level Health Summary Types

3    Nationally Exported Health Summary Types

Is this correct?  (Y/N)  Y// **y**

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user preference.

**Method of compiling ‘Health Summary Types List’**

Use this option to see how the list of Health Summary Types is to be built.

**Overwrite** - System-defined Health Summary Types are added to the list.  If there are User-defined Health Summary Types, then they will replace the System defined Health Summary Types already on the list.

**Append** – System-defined Health Summary Types are added to the list.  If there are User-defined Health Summary Types, then they will be added to the list along with the System-defined types.

**Note:** If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to edit the method.

*Without the GMTSMGR Key:*

CPRS Reports Tab, Health Summary Type List (Order)

Append selected Health Summary Types to the list

Overwrite selected Health Summary Types to the list

Select Append/Overwrite (A/O):  A// **&lt;Enter&gt;** append

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user method.

**Edit 'Health Summary Types List' Parameters**

Use this option to add, edit or delete a Health Summary Type from the list of Health Summary Types defined by the user.  If you are a holder of the GMTSMGR Key, you can also use this option to edit the Health Summary Types defined for the System.  Also, if you are the holder of the GMTSMGR key, you will be prompted for the name of the user to edit their list of preferred Health Summary Types.

*Without the GMTSMGR Key:*

Adding the Health Summary Type ‘REMOTE CLINICAL DATA (1Y)’ to the list of preferred Health Summary Types to be displayed for the user on the CPRS Reports Tab.

Edit the CPRS Health Summary Types list on the reports tab

--------- Setting GUI Health Summary Type List  for User: USER,LOCAL ---------

Select Sequence: **15**

Are you adding 15 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 15// **&lt;Enter&gt;** 15

Health Summary: REMOTE CLIN

1   REMOTE CLINICAL DATA (1Y)

2   REMOTE CLINICAL DATA (3M)

3   REMOTE CLINICAL DATA (4Y)

CHOOSE 1-3: **1** REMOTE CLINICAL DATA (1Y)

Select Sequence: **&lt;Enter&gt;**

*With the GMTSMGR Key:*

Adding the Health Summary Type ‘REMOTE CLINICAL DATA (1Y)’ to the list of preferred Health Summary Types to be displayed for all users on the **system** on the CPRS Reports Tab.

Allowable Health Summary Types may be set for the following:

2   User          USR    [choose from NEW PERSON]

4   System        SYS    [DEVCUR. REDACTED]

Enter selection: **4** System   DEVCUR. REDACTED

- Setting Allowable Health Summary Types  for System: DEVCUR. REDACTED -

Select Sequence: **8**

Are you adding 8 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 8// **&lt;Enter&gt;** 8

Health Summary: REMOTE CLIN

1   REMOTE CLINICAL DATA (1Y)

2   REMOTE CLINICAL DATA (3M)

3   REMOTE CLINICAL DATA (4Y)

CHOOSE 1-3: **1** REMOTE CLINICAL DATA (1Y)

Select Sequence:

### New Health Summary Types distributed by the High Risk Mental Health Patient project:

The two HEALTH SUMMARY TYPEs, VA-HIGH RISK PATIENT and REMOTE MH

HIGH RISK PATIENT were originally released in GMTS*2.7*99.

In order to view these HEALTH SUMMARY TYPES from within CPRS GUI, they

must be added to the CPRS GUI Reports tab selection list. This can be set up from one of the following menu options.

- GMTS COORDINATOR

CPRS Reports Tab 'Health Summary Types List' Menu

Edit 'Health Summary Types List' Parameters

- CPRS MANAGER MENU  ORMGR     CPRS Manager Menu

PE     CPRS Configuration (Clin Coord) ...

GP     GUI Parameters ...

HS     GUI Health Summary Types

Allowable Health Summary Types may be set for the following.

2   User          USR    [choose from NEW PERSON]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    [DVF. REDACTED]

5   Service       SRV    [choose from SERVICE/SECTION]

Add the new REMOTE MH HIGH RISK PATIENT - HEALTH SUMMARY TYPE to the  appropriate list based on your local practice and procedures.6. Site Preferences

**CPRS Health Summary Display/Edit Site Defaults Menu**

Use the options in the CPRS Health Summary Display/Edit Site Defaults Menu

to display the site defaults, select the Health Summary Types to list on the Reports Tab, edit the method of building the list (append/overwrite), edit allowable entities for the list (i.e., User, System, Division, etc.), or resequence the allowable entities in the order they should be appear on the list.

The CPRS Health Summary Display/Edit Site Defaults Menu contains five options.

1	Display Site Health Summary List Defaults

2	Edit ‘Health Summary Type List’ Parameters

3	Edit Default HS Type List Compile Method

4	Add/Edit Allowable Entities for HS List

5	Resequence Allowable Entities for HS List

**Display Site Health Summary List Defaults**

Use this option to display the site defaults for building the list of Health Summary Types on the Reports Tab in CPRS. The display includes the method for building the list and the precedence of parameters. These default values will be used in the event that the user has not established user preferences. This option is similar to the option GMTS GUI HS LIST DEFAULTS (Display 'Health Summary Types List' Defaults), which allows the user to display user preferences.

**Method** - The list can be built either by overwriting the list with each higher precedence of Health Summary Types or by appending each level of precedence to the list (prior to this option, the only choice was overwriting the list).

**Precedence of Parameters** - Health Summary Types can be established for the system and for the users. Additionally, there are Nationally exported Health Summary Types. This precedence indicates the order in which these types will be displayed (i.e., display user defined types before system defined types).

Display default Health Summary Type list for SALT LAKE CITY OIFO

DEVICE: HOME// **;;9999** ANYWHERE

SALT LAKE CITY OIFO Defaults for CPRS Reports Tab           JAN 14, 2002

------------------------------------------------------------------------

Precedence of Parameters:        DIV;USR;CLS;SYS

1  Division defined

2  User preferences

3  Class defined

4  System defined

Method for building the List: **Append**

Add Division Defined Summary Types to the list, then

Append with User Defined Summary Types (if found), then

Append with Class Defined Summary Types (if found), then

Append with System Defined Summary Types (if found)

**Edit 'Health Summary Types List' Parameters**

Use this option to add, edit or delete a Health Summary Type from the list of Health Summary Types defined for a given entity (System, Division, User, etc.).    This option is similar to the option GMTS GUI HS LIST PARAMETERS (Edit 'Health Summary Types List' Parameters), which allows the user to add/edit Health Summary Types for the ‘User’ entity.

Select CPRS Health Summary Display/Edit Site Defaults Option:

**Edit** 'Health Summary Types List' Parameters

Allowable Health Summary Types may be set for the following:

2   Division      DIV    [choose from INSTITUTION]

3   User          USR    [choose from NEW PERSON]

8   Class         CLS    [choose from USR CLASS]

9   System        SYS    [DEVCUR. REDACTED]

Enter selection: **2** Division   INSTITUTION

Select INSTITUTION NAME: **SALT LAKE CITY OIFO** UT  ISC

- Setting Allowable Health Summary Types for Division: SALT LAKE CITY OIFO

Select Sequence: **9**

Are you adding 9 as a new Sequence? Yes// **y** YES

Sequence: 9// **&lt;Enter&gt;** 9

Health Summary: **rad**

1   RAD

2   RAD NAN

3   RADIOLOGY

4   RADIOLOGY ONLY

5   RADIOLOGY PROFILE

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 3  RADIOLOGY

Select Sequence: **?**

Sequence                    Value

--------                    -----

1                         GMTS HS ADHOC OPTION

2                         DEMOGRAPHICS

3                         SURGERY

9                         RADIOLOGY

**Edit Default HS Type List Compile Method**

Use this option to see how the list of Health Summary Types is to be built.  This method will be used for all users who do not have user preferences set.  This option is similar to the option GMTS GUI HS LIST METHOD (Method of compiling 'Health Summary Types List'), which allows the user to define their Health Summary List compile method preference.

**Overwrite** – System-defined Health Summary Types are added to the list. If there are User-defined Health Summary Types, then they will replace the System defined Health Summary Types already on the list.

**Append** – System-defined Health Summary Types are added to the list. If there are User-defined Health Summary Types, then they will be added to the list along with the System defined types.

Site Default Method for building 'Health Summary Types'

List on the CPRS Reports Tab

Append selected Health Summary Types to the list

Overwrite selected Health Summary Types to the list

Select Append/Overwrite (A/O):  A// **&lt;Enter&gt;** Append

**Add/Edit Allowable Entities for HS List**

Use this option to add or delete an entity (System, Division, User, etc.) from the list of allowable entities for the parameter 'ORWRP HEALTH SUMMARY TYPE LIST' used on the CPRS Reports Tab to display the Health Summary Types List.

ORWRP HEALTH SUMMARY TYPE LIST' ALLOWABLE ENTITIES

elect ALLOWABLE ENTITIES PRECEDENCE: **?**

Answer with ALLOWABLE ENTITIES PRECEDENCE

Choose from:

2        INSTITUTION

3        NEW PERSON

8        USR CLASS

You may enter a new ALLOWABLE ENTITIES, if you wish

Type a Number between 0 and 999.99, 2 Decimal Digits

elect ALLOWABLE ENTITIES PRECEDENCE: **9**

Are you adding '9' as a new ALLOWABLE ENTITIES (the 4TH for

this PARAMETER DEFINITION)? No// **y** (Yes)

elect PARAMETER ENTITY NAME: **?**

Answer with PARAMETER ENTITY FILE NUMBER, or NAME, or PREFIX

Do you want the entire PARAMETER ENTITY List? **y** (Yes)

Choose from:

4            DIVISION

4.2          SYSTEM

49           SERVICE

100.21       TEAM (OE/RR)

200          USER

8930         CLASS

Select PARAMETER ENTITY NAME: **sys** TEM

**Resequence Allowable Entities for HS List**

Use this option to resequence the order in which the allowable entities for parameter  'ORWRP HEALTH SUMMARY TYPE LIST' are used in building the list of Health Summary Types for the CPRS Reports Tab.  This order is used for any user who does not have user preferences set.

Parameter "ORWRP HEALTH SUMMARY TYPE LIST" has 4 allowable entities

which may have the Health Summary Types on the CPRS reports tab

and are used in the following order:

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Division level defined Health Summary Types

4  Class defined Health Summary Types

Are these in the correct order for your site?  Y// **NO**

Please select the order in which you want these to be entities

to be used.

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Division level defined Health Summary Types

4  Class defined Health Summary Types

Select the 1st entity to be used:  1// **3**

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Class defined Health Summary Types

Select the 2nd entity to be used:  1// **1**

1  User defined Health Summary Types

2  Class defined Health Summary Types

Select the 3rd entity to be used:  1// **2**

You have selected to resequenced the Health Summary Type

entities in the following order:

FROM (Current)      TO (Resequenced)

----------------    ----------------

1  System              Division

2  User                System

3  Division            Class

4  Class               User

Is this OK?  Y// **&lt;Enter&gt;** YES


## Chapter 4: Managing Health Summary

**1. Health Summary Coordinator’s Menu**

**2. Security, Locks, and Keys**

**3. Batch Printing Options**

**4. CPRS Reports Tab 'Health Summary Types List' Menu**


# Chapter 4 – Managing Health Summary

Chapter 4 provides information to help Health Summary Coordinators manage the package. It includes a description and examples of how to use the batch printing process. The *Health Summary Installation Guide* and *Health Summary Technical Manual* contain more detailed information about setting up the package and IRM/ADPAC Maintenance options .

#### Health Summary Coordinator’s Menu

This menu is for Clinical Coordinators who use the special Health Summary package features for batch printing nightly summaries and building customized health summary types. It also provides all the user functions of the other two user menus described  in the previous sections.

Only the batch printing options are described in this chapter.

1	Print Health Summary Menu ...

2	Build Health Summary Type Menu ...

3	Set-up Batch Print Locations

4 	List Batch Health Summary Locations

5    CPRS Reports Tab 'Health Summary Types List' Menu ...


### Security, Locks, and Keys

A health summary type may be used by several different people and should not be changed indiscriminately. Therefore, editing health summary types has been restricted in several ways. *First* , a user must have access to the Health Summary Coordinator’s or Enhanced menus to edit or create a health summary type. *Second* , edit access to a particular health summary is restricted unless the user  is the owner of that health summary type or holds certain security keys (e.g., GMTSMGR).

*Owner*

The owner of a health summary type is designated when a health summary type is created and has edit access to that health summary type. Usually the creator of a health summary type is automatically designated as its owner. However, if the creator of the health summary type holds the GMTSMGR key, the creator may designate another person as the owner. If you are assigned the GMTSMGR key, you are *not* automatically designated as the owner. You must still enter your name as “owner.”

*Lock*

A lock may also be designated when a health summary type is created. The lock gives edit access for that health summary type to anyone who holds the matching security key. For example, someone creating a Pathology Health Summary Type may want to enter LRSUPER as the lock, thereby giving edit access to any holder of the LRSUPER security key. The four health summary types included with the Health Summary package SAMPLE 1, SAMPLE 2, SAMPLE 3, and GMTS HS ADHOC OPTIONhave the GMTSMGR lock.

*Keys*

*GMTS VIEW ONLY*

The GMTS VIEW ONLY security key allows you to view a health summary only on your terminal screen. You cannot print a paper copy of the health summary.

*GMTSMGR*

The GMTSMGR security key allows you to edit health summary types which are locked with the GMTSMGR key. It also provides master edit access to all other health summary types. This key should be issued with caution by the IRM Service or Clinical Coordinator.


### Batch Printing Process

The Health Summary package allows coordinators to schedule nightly batch processing of health summaries for patients in a particular ward, patients in outpatient clinics, or patients scheduled for operating room surgeries the following day or up to ten days ahead. The advantages of Batch processing are 1) it enables the clinic to have the most current clinical information available when the patient arrives for the appointment, and 2) processing can take place in non-peak computer hours.

The nightly batch job recognizes non-workdays (weekends and holidays). Data will not be printed out on non-workdays. For example, if you want a Health Summary type printed out for Monday clinics one day in advance, it will now print on the previous Friday rather than on Sunday.

#### Batch Print of All Clinics by Visit Date

This option allows Coordinators to interactively designate the batch print of all health summaries for patients with appointments at all outpatient clinics on a selected day. Summaries can be printed at the print device designated for the clinic in the Location Parameters. This option is an alternate method for designating when summaries should be printed for all clinics, rather than using the batch print option available for queuing nightly batch print jobs. The option used for printing nightly batch job summaries for wards, clinics, or operating room locations should be disabled if the user wishes to use this option on a daily basis.

*Steps to use Batch Print:*

**1.** Select the Batch Print of All Clinics by Visit Date option from your menu.

Select Print Health Summary Menu Option: **6** Batch Print of All Clinics by Visit Date

This option will queue Health Summaries for a specified Visit Date

for all Outpatient Clinics with Appointments on that Visit Date.

**2.** Select the Visit date.

Please enter the Visit date:  12/19/94// **&lt;Enter&gt;** (DEC 19, 1994)

Date and Time to Queue this Job to run:  NOW// **&lt;Enter&gt;**

#### Set-up Batch Print Locations

This option allows you to set, edit, or delete parameters that will be used to print batches of health summaries of a specific  type, in a particular hospital location. Only one set of parameters exists for a particular location and patient.

*Steps to use Set-up Batch Print Location:*

**1.** Select the Set-up option from the Health Summary Coordinator’s Menu.

Select Health Summary Coordinator’s Menu Option: **3** Set-up Batch Print Location

If you select the Set-up Batch Print Locations option and receive the message in the first box shown below, contact your IRM office and ask them to turn on the GMTS TASK STARTUP option.

** Alert **

Health Summary batches have not been queued to print. Please ask your site manager to queue the option GMTS TASK STARTUP to run nightly. Parameters may be set now but will not produce health summaries until option is queued.

**2.** Type in a hospital location name (for example, eye clinic, C Ward, NHCU, etc.).

Select HOSPITAL LOCATION NAME: **C WARD**

If parameters are set for the location you chose, the following message appears.

At present the following Health Summary Types are printed for C WARD:

Type	Device	Days Ahead 	Action Profile

Dr. HSPROVIDER	WORK	1		Yes

***** OUTPATIENT		2		No

***** This Type will not print since Device has not been set

You may edit a Health Summary Type from the list or enter a new Type

Select HEALTH SUMMARY TYPE NAME: **SAMPLE 1**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;Enter&gt;**

**3.** Enter the name of the printer you want the summary printed at. If you enter a ?, you will see the message shown.

DEVICE FOR NIGHTLY PRINT: **?**

Please specify the printer nearest LOCATION

ANSWER WITH DEVICE NAME, OR LOCAL SYNONYM, OR $I, OR VOLUME SET 	
	  (CPU), OR SIGN-ON SYSTEM DEVICE.

DO YOU WANT THE ENTIRE DEVICE LIST? **No**

DEVICE FOR NIGHTLY PRINT: WORK

**4.** If you want an action profile to print with the Health Summary, answer yes.

PRINT ACTION PROFILE: NO// **&lt;Enter&gt;**

PRINT DAYS AHEAD:  2// **&lt;Enter&gt;**

**Note:  “** PRINT DAYS AHEAD:” is only prompted for if the location you selected is a clinic or operating room.

*Delete Batch Printing Set Up*

To discontinue a batch printing set-up of health summaries at a location, delete the health summary type using the same option you used to set up batch printing.

*Steps to Delete Batch Printing Set-up :*

**1.** Select Set-up Batch Print Locations from the Health Summary Coordinator’s Menu.

Select Health Summary Coordinator’s Menu Option: **3** Set-up Batch Print Location

**2.** Enter the hospital location and the Health Summary Type you want to delete the batch printing for.

Select Hospital Location: **ONCOLOGY**

At present the following Health Summary Types are printed for ONCOLOGY:

Action

Type                      Device           Days Ahead      Profile

SAMPLE 1                    WORK                2             No

You may edit a Health Summary Type from the list or enter a new Type

Select Health Summary Type: **SAMPLE 1**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;Enter&gt;**

Do you wish to delete this Health Summary Type from the nightly print? NO// **Y** YES

**Print for Health Summary Type deleted**

Select Hospital Location: **&lt;Enter&gt;**

*List Batch Health Summary Locations*

This option lets you view the hospital locations requesting nightly batch printing of health summaries. The listing shows the hospital location, the device designated for printing, the number of days in the future the print will occur, whether an Outpatient Pharmacy Action Profile will be appended, and the health summary type.

*Steps to use option:*

**1.** Select List Batch Health Summary Locations from the Health Summary Coordinator’s Menu.

Select Health Summary Coordinators Menu Option: **List** Batch Health Summary Locations

**2.** Type the name of the printer or press return if you want the list displayed online.

DEVICE:  HOME// **&lt;Enter&gt;**

**3.** The list of locations is printed on your screen.

Batch Health Summary Locations List	 OCT 17, 1990	     PAGE 1

Print  	Print

Days   	Action

Location	Device	Ahead  	Profile  	Health Summary Type

EYE CLINIC	C-WARD LASER  	0	yes      	BRIEF CLINICAL

EYE CLINIC	C-WARD LASER  	2	yes      	HSPROVIDER1

HYPERTENSION	HALLPTR	1      	no       	EMERGENCY


### User Preferences

**CPRS Reports Tab 'Health Summary Types List' Menu**

Use the options in the CPRS Reports Tab ‘Health Summary Types List’ Menu to select the Health Summary Types to list on the Reports Tab, arrange the order of these Health Summaries on the list, and to the user’s preferences.

The CPRS Reports Tab ‘Health Summary Types List’ Menu contains four options.

1      Display 'Health Summary Types List' Defaults

2      Precedence of 'Health Summary Types List'

3      Method of compiling 'Health Summary Types List'

4      Edit 'Health Summary Types List' Parameters

**Display 'Health Summary Types List' Defaults**

Use this option to display the list of Health Summary Types that will be contained in the ‘Health Summary Types’ box on the Reports Tab in CPRS.

The display includes the precedence of parameters, the method for building the list, and finally the list that will appear on the Reports Tab in CPRS.

**Precedence of Parameters** - Health Summary Types can be established for the system and for the users.  Additionally, there are Nationally exported Health Summary Types.  This precedence indicates the order in which these types will be displayed (i.e., display user-defined types before system-defined types).

**Method** - The list can be built either by overwriting the list with each higher precedence of Health Summary Types or by appending each level of precedence to the list (prior to this option, the only choice was overwriting the list).

**List** - A list of Health Summary Types that will appear in the ‘Health Summary Types’ box on the Reports Tab will be listed.

**Note:** If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to display the 'Health Summary Types List' defaults.

*Without the GMTSMGR Key:*

Health Summary Types list for CPRS Reports Tab              JUL 17, 2001

------------------------------------------------------------------------

Precedence of Parameters:        USR;SYS;NAT

1  User preferences

2  System defined

3  National Health Summary Types

Method for building the List:    Append

Add User Defined Summary Types to the list, then

Append with System Defined Summary Types (if found), then

Add National Defined Summary Types (if found)

The Health Summary Types box will list the following Health Summary Types:

User defined types        1  GMTS HS ADHOC OPTION

2  SURGERY

3  RADIOLOGY

System defined types      4  DIABETES (1)

5  AC CLINICAL SUMMARY

6  PAIN MANAGEMENT

National types            7  REMOTE CLINICAL DATA (1Y)

8  REMOTE CLINICAL DATA (3M)

9  REMOTE CLINICAL DATA (4Y)

10  REMOTE DEMO/VISITS/PCE (1Y)

11  REMOTE DEMO/VISITS/PCE (3M)

12  REMOTE LABS ALL (1Y)

13  REMOTE LABS ALL (3M)

14  REMOTE LABS LONG VIEW (12Y)

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user preference.

**Precedence of 'Health Summary Types List'**

Use this option to select the defined Health Summary Types to include on the list and arrange them in the order (precedence) that they should appear on the list.

Currently there are three groups of Health Summary Types that may be predefined and made available on the Reports Tab of CPRS.

SYS	Health Summary Types may be defined for all users on the system.

USR	Health Summary Types may be defined for a single user on the system.

NAT	Nationally exported Health Summary Types (NAT) defined for system users or a single user are treated independently to keep them together in the list box.

In this option, you must first select those Health Summary Type groups (SYS, USR, or NAT) to include on the Reports Tab, then specify the order in which they will appear on the Reports Tab.

NOTE:  If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to edit the precedence.

*Without the GMTSMGR Key:*

GUI Reports Tab, Health Summary Type List (Contents)

Include User Preferred Health Summary Types:  (Y/N)  Y// **&lt;Enter&gt;** ES

System Defined Health Summary Types:  (Y/N)  Y// **&lt;Enter&gt;** ES

National Types  (Remote Data Views):  (Y/N)  Y// **&lt;Enter&gt;** ES

You have selected multiple Health Summary types to be listed on the CPRS

reports tab, in the Health Summary Types box.  Now you must select the

order in which you want these to be displayed.

Order to Display Included Health Summary Types

1  User Preferred Health Summary Types

2  System Level Health Summary Types

3  Nationally Exported Health Summary Types

Select the 1st to be listed:  1// **&lt;Enter&gt;**

1  System Level Health Summary Types

2  Nationally Exported Health Summary Types

Select the 2nd to be listed:  1// **&lt;Enter&gt;**

You have selected three Health Summary Types, arranged

in the following order:

1    User Preferred Health Summary Types

2    System Level Health Summary Types

3    Nationally Exported Health Summary Types

Is this correct?  (Y/N)  Y// **y**

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user preference.

**Method of compiling ‘Health Summary Types List’**

Use this option to see how the list of Health Summary Types is to be built.

**Overwrite** - System-defined Health Summary Types are added to the list.  If there are User-defined Health Summary Types, then they will replace the System defined Health Summary Types already on the list.

**Append** – System-defined Health Summary Types are added to the list.  If there are User-defined Health Summary Types, then they will be added to the list along with the System-defined types.

NOTE:  If you are a holder of the GMTSMGR Key, you will be prompted for the name of the user to edit the method.

*Without the GMTSMGR Key:*

CPRS Reports Tab, Health Summary Type List (Order)

Append selected Health Summary Types to the list

Overwrite selected Health Summary Types to the list

Select Append/Overwrite (A/O):  A// **&lt;Enter&gt;** append

*With the GMTSMGR Key:*

Same as above, except the additional prompt for the name of the user to edit the user method.

**Edit 'Health Summary Types List' Parameters**

Use this option to add, edit, or delete a Health Summary Type from the list of Health Summary Types defined by the user.  If you are a holder of the GMTSMGR Key, you can also use this option to edit the Health Summary Types defined for the System.  Also, if you are the holder of the GMTSMGR key, you will be prompted for the name of the user to edit their list of preferred Health Summary Types.

*Without the GMTSMGR Key:*

Adding the Health Summary Type ‘REMOTE CLINICAL DATA (1Y)’ to the list of preferred Health Summary Types to be displayed for the user on the CPRS Reports Tab.

Edit the CPRS Health Summary Types list on the reports tab

--------- Setting GUI Health Summary Type List  for User: USER,LOCAL ---------

Select Sequence: 15

Are you adding 15 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 15// **&lt;Enter&gt;** 15

Health Summary: REMOTE CLIN

1   REMOTE CLINICAL DATA (1Y)

2   REMOTE CLINICAL DATA (3M)

3   REMOTE CLINICAL DATA (4Y)

CHOOSE 1-3: **1** REMOTE CLINICAL DATA (1Y)

Select Sequence: **&lt;Enter&gt;**

*With the GMTSMGR Key:*

Adding the Health Summary Type ‘REMOTE CLINICAL DATA (1Y)’ to the list of preferred Health Summary Types to be displayed for all users on the **system** on the CPRS Reports Tab.

Allowable Health Summary Types may be set for the following:

2   User          USR    [choose from NEW PERSON]

4   System        SYS    [DEVCUR.REDACTED]

Enter selection: **4** System   DEVCUR.REDACTED

- Setting Allowable Health Summary Types  for System: DEVCUR.REDACTED -

Select Sequence: **8**

Are you adding 8 as a new Sequence? Yes// **&lt;Enter&gt;** YES

Sequence: 8// **&lt;Enter&gt;** 8

Health Summary: REMOTE CLIN

1   REMOTE CLINICAL DATA (1Y)

2   REMOTE CLINICAL DATA (3M)

3   REMOTE CLINICAL DATA (4Y)

CHOOSE 1-3: **1** REMOTE CLINICAL DATA (1Y)

Select Sequence:

### Site Preferences

**CPRS Health Summary Display/Edit Site Defaults Menu**

Use the options in the CPRS Health Summary Display/Edit Site Defaults Menu

to display the site defaults, select the Health Summary Types to list on the Reports Tab, edit the method of building the list (append/overwrite), edit allowable entities for the list (i.e., User, System, Division, etc.), or resequence the allowable entities in the order they should be appear on the list.

The CPRS Health Summary Display/Edit Site Defaults Menu contains five options.

1	Display Site Health Summary List Defaults

2	Edit ‘Health Summary Type List’ Parameters

3	Edit Default HS Type List Compile Method

4	Add/Edit Allowable Entities for HS List

5	Resequence Allowable Entities for HS List

**Display Site Health Summary List Defaults**

Use this option to display the site defaults for building the list of Health Summary Types on the Reports Tab in CPRS. The display includes the method for building the list and the precedence of parameters. These default values will be used in the event that the user has not established user preferences. This option is similar to the option GMTS GUI HS LIST DEFAULTS (Display 'Health Summary Types List' Defaults), which allows the user to display user preferences.

**Method** - The list can be built either by overwriting the list with each higher precedence of Health Summary Types or by appending each level of precedence to the list (prior to this option, the only choice was overwriting the list).

**Precedence of Parameters** - Health Summary Types can be established for the system and for the users. Additionally, there are Nationally exported Health Summary Types. This precedence indicates the order in which these types will be displayed (i.e., display user-defined types before system-defined types).

Display default Health Summary Type list for SALT LAKE CITY OIFO

DEVICE: HOME// **;;9999** ANYWHERE

SALT LAKE CITY OIFO Defaults for CPRS Reports Tab           JAN 14, 2002

------------------------------------------------------------------------

Precedence of Parameters:        DIV;USR;CLS;SYS

1  Division defined

2  User preferences

3  Class defined

4  System defined

Method for building the List:    Append

Add Division Defined Summary Types to the list, then

Append with User Defined Summary Types (if found), then

Append with Class Defined Summary Types (if found), then

Append with System Defined Summary Types (if found)

**Edit 'Health Summary Types List' Parameters**

Use this option to add, edit or delete a Health Summary Type from the list of Health Summary Types defined for a given entity (System, Division, User, etc.).  This option is similar to the option GMTS GUI HS LIST PARAMETERS (Edit 'Health Summary Types List' Parameters), which allows the user to add/edit Health Summary Types for the ‘User’ entity.

Select CPRS Health Summary Display/Edit Site Defaults Option:

Edit 'Health Summary Types List' Parameters

Allowable Health Summary Types may be set for the following:

2   Division      DIV    [choose from INSTITUTION]

3   User          USR    [choose from NEW PERSON]

8   Class         CLS    [choose from USR CLASS]

9   System        SYS    [DEVCUR.REDACTED]

Enter selection: **2** Division   INSTITUTION

Select INSTITUTION NAME: **SALT LAKE CITY OIFO  UT  ISC**

- Setting Allowable Health Summary Types for Division: SALT LAKE CITY OIFO

Select Sequence: **9**

Are you adding 9 as a new Sequence? Yes// **y** YES

Sequence: 9// **&lt;Enter&gt;** 9

Health Summary: **rad**

1   RAD

2   RAD NAN

3   RADIOLOGY

4   RADIOLOGY ONLY

5   RADIOLOGY PROFILE

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 3  RADIOLOGY

Select Sequence: **?**

Sequence                    Value

--------                    -----

1                         GMTS HS ADHOC OPTION

2                         DEMOGRAPHICS

3                         SURGERY

9                         RADIOLOGY

**Edit Default HS Type List Compile Method**

Use this option to see how the list of Health Summary Types is to be built.  This method will be used for all users who do not have user preferences set.  This option is similar to the option GMTS GUI HS LIST METHOD (Method of compiling 'Health Summary Types List') which allows the user to define their Health Summary List compile method preference.

**Overwrite** – System-defined Health Summary Types are added to the list. If there are User-defined Health Summary Types, then they will replace the System-defined Health Summary Types already on the list.

**Append** – System-defined Health Summary Types are added to the list. If there are User-defined Health Summary Types, then they will be added to the list along with the System-defined types.

Site Default Method for building 'Health Summary Types'

List on the CPRS Reports Tab

Append selected Health Summary Types to the list

Overwrite selected Health Summary Types to the list

Select Append/Overwrite (A/O):  A// **&lt;Enter&gt;** Append

**Add/Edit Allowable Entities for HS List**

Use this option to add or delete an entity (System, Division, User, etc.) from the list of allowable entities for the parameter 'ORWRP HEALTH SUMMARY TYPE LIST' used on the CPRS Reports Tab to display the Health Summary Types List.

ORWRP HEALTH SUMMARY TYPE LIST' ALLOWABLE ENTITIES

Select ALLOWABLE ENTITIES PRECEDENCE: **?**

Answer with ALLOWABLE ENTITIES PRECEDENCE

Choose from:

2        INSTITUTION

3        NEW PERSON

8        USR CLASS

You may enter a new ALLOWABLE ENTITIES, if you wish

Type a Number between 0 and 999.99, 2 Decimal Digits

Select ALLOWABLE ENTITIES PRECEDENCE: **9**

Are you adding '9' as a new ALLOWABLE ENTITIES (the 4TH for

this PARAMETER DEFINITION)? No// **y** (Yes)

Select PARAMETER ENTITY NAME: **?**

Answer with PARAMETER ENTITY FILE NUMBER, or NAME, or PREFIX

Do you want the entire PARAMETER ENTITY List? **y** (Yes)

Choose from:

4            DIVISION

4.2          SYSTEM

49           SERVICE

100.21       TEAM (OE/RR)

200          USER

8930         CLASS

Select PARAMETER ENTITY NAME: **sys** TEM

**Resequence Allowable Entities for HS List**

Use this option to resequence the order in which the allowable entities for parameter  'ORWRP HEALTH SUMMARY TYPE LIST' are used in building the list of Health Summary Types for the CPRS Reports Tab.  This order is used for any user who does not have user preferences set.

Parameter "ORWRP HEALTH SUMMARY TYPE LIST" has 4 allowable entities

which may have the Health Summary Types on the CPRS reports tab

and are used in the following order:

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Division level defined Health Summary Types

4  Class defined Health Summary Types

Are these in the correct order for your site?  Y// **NO**

Please select the order in which you want these to be entities

to be used.

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Division level defined Health Summary Types

4  Class defined Health Summary Types

Select the 1st entity to be used:  1// **3**

1  System level defined Health Summary Types

2  User defined Health Summary Types

3  Class defined Health Summary Types

Select the 2nd entity to be used:  1// **1**

1  User defined Health Summary Types

2  Class defined Health Summary Types

Select the 3rd entity to be used:  1// **2**

You have selected to resequenced the Health Summary Type

entities in the following order:

FROM (Current)      TO (Resequenced)

----------------    ----------------

1  System              Division

2  User                System

3  Division            Class

4  Class               User

Is this OK?  Y// **&lt;Enter&gt;** YES


## Chapter 5: Helpful Hints


# Chapter 5 – Helpful Hints—Q &amp; A

**Q.** ***How Can I Create New Component*** **s?**

**A.** We encourage sites to submit NSR’s (New Service Requests) for new components (or enhancements to existing components) that they believe will be useful on a national basis. The Health Summary Expert Panel evaluates these requests, and if approved, they will be provided as patches or in a future version of Health Summary, depending on the priority given to the request.

Sites also may modify existing components or create new components for their local needs, such as enhancements to one of the components that Health Summary provides, a totally new one that accesses VISTA data that Health Summary currently doesn’t provide a component for, or a component to access non-VISTA supported (Class III software) packages.

**Note:** The national Office of Information &amp; Technology does not provide support for locally developed components.

A Health Summary basket has been set up on SHOP,ALL where sites can put their locally developed component routines, in order to share this information with the rest of the VISTA community. We encourage you to take a look at what has already been done, as this may save you some time.

To access SHOP,ALL from FORUM:

1. Enter SHOP,ALL at your menu prompt and you’ll be “logged” on to SHOP,ALL
2. Enter SURROGATE NAME: **SHOP,ALL**
3. Select Mailman Option: **Read Mail**
4. Enter the Health Summary mail basket.

**Q.** ***Why doesn’t the up-arrow (^) always take me out of Health Summary when I enter it as described on the screen (and in the manual)?***

**A.** Normally, you can exit the Health Summary program by entering an ^ at a prompt. However, if you have selected more than one patient to print Health Summaries for, a single up-arrow will take you to the next patient’s Health Summary. To exit the program in these circumstances, enter double up-arrows (^^).

**Q.** ***Can I schedule nightly batch jobs to print before weekends or holidays?***

**A.** The nightly batch job has been enhanced to recognize non-workdays (weekends and holidays). Data will not be printed out on non-workdays. For example, if you want a Health Summary type printed out for Monday clinics one day in advance, it will now print on the previous Friday rather than on Sunday.

**Q.** ***Why doesn’t the component list display in alphabetical order on the Ad Hoc menu?***

**A.** Components are displayed by “Default Header”  an order that doesn’t appear to be alphabetical. The order is based on the *actual* (technical *)* component name. For example, “Blood Availability” is the default header name, whereas the component name is LAB BLOOD AVAILABILITY. If you need a more detailed explanation of this, contact your Clinical Coordinator or IRMS.

**Q.** ***Is there a way for us to have Health Summaries print with encounter forms for certain clinics or appointments?***

**A.** The Integrated Billing Package (Encounter Form Utilities) includes a Print Manager that lets sites define reports to print along with encounter forms for specific clinics, divisions, and appointments. See the *IB Encounter Form Utilities User Manual* for further information.

**Q** . ***Can I print bar codes on my Action Profiles that are scheduled to print in tandem with Health Summary?***

**A.** Yes, a site parameter has been added to allow sites to specify whether or not to print bar codes on Action Profiles which are queued to print with Health Summaries (dependent on whether the printer is set up to print bar codes).

**Q.** ***When our site created Health Summary types and entered names thus: HSPROVIDER,ONE, why couldn’t we review existing components through the option, “Create/Modify Health Summary Type”?***

**A.** For technical reasons involving FileMan conventions, commas can’t be used in certain fields. We recommend that you avoid using commas in names of Health Summary types.

**Q.** ***Why do I get the error message “Object not Found (routine GMTSOBX)” when I try to Import/Install a Health Summary object?***

**A.** Check to see if the MailMan message has been unpacked; you have to unpack it before you can import the object. You may also get an error message if you try to install an object with the same name as an existing one.


## Glossary


# Glossary

**Ad Hoc Health** A temporary health summary that lets you

**Summary** select health summary components, time and occurrence limits, and selection items for a particular patient.

**Components** Elements of data from **V** *IST* **A** packages that make up the health summary report (e.g., Demographics).

**Default** Prompts that have an answer followed by double slashes (//) are called defaults; this means a response has been pre-selected, based on the most likely response or the previous response to this prompt. For example, the prompt “Time Limit:” may have a default of 1 year for Lab Orders and would appear as: Time Limit: 1Y//.

**Device** A printer or computer terminal screen. See the *DHCP User’s Guide to Computing* for information about basic VISTA computer skills, including printing information.

**Hospital Location** For some PCE components, when this flag is

**Displayed** enabled, the Hospital Location abbreviation will be displayed.

**ICD Text Displayed** For some components, Diagnosis Text can be customized (e. g., long form, short form, code only, or no form of ICD Diagnosis).

**Lock** Restricts edit access for a given health summary type to the holders of any valid security key. For example, the GMTSMGR key is required to edit summary types that are locked by the GMTSMGR lock. A lock may also be designated when a health summary type is created. For example, someone creating a Pathology Health Summary Type may want to enter LRSUPER as the lock, thereby giving edit access to any holder of the LRSUPER security key.

**Non-destructive** In the Health Summary package, non-destructive means that Health Summary does not edit the data from the **V** *IST* **A** package from which it extracts its information.

**Object** Health Summary Objects are Health Summary Types saved in a temporary array for insertion into another electronic document.

**Occurrence Limits** The number of past occurrences that will be reported on a health summary (e.g., the last five occurrences).

**Owner** The creator of a health summary type. Owners and holders of the GMTSMGR security key have sole access to modify their health summary type(s).

**Provider Narrative** For some components, when this flag is enabled

**Displayed** and a provider enters narrative text, the text will be displayed.

**Selection Items** For some components (e.g., Lab Tests Selected, Vital Signs Selected), you can specify the data elements to be included in the components, such as occurrence and time limits.

**Summary Order** The order in which components appear in a health summary, as defined by the creator of a Summary Type.

**Summary Type** The structure or template containing defined components and their unique characteristics with occurrence and time limits, and selection items. Used to print health summaries for patients.

**Time Limits** The time period of reference included on a health summary for a particular component (e.g., 2D, 1M, 1Y for two days, one month and one year).

**V** *IST* **A** The VA computer system in VA facilities.


## Appendices


**Appendix A - Health Summary Component Description List**

**Appendix B - VISTA &amp; Health Summary Conventions**

**Appendix C - Historical Documentation shift from GMTS*2.7*133 (Do Not Update)**


## Appendix A—Health Summary Component Description List

The following list can be produced (displayed online or printed) from the “List Health Summary Component Descriptions” option on the Information Menu.

Select Information Menu Option:  List Health Summary Component Descriptions

DEVICE: ;;999  HOME

HEALTH SUMMARY COMPONENT DESCRIPTION LIST      SEP 18,2012  14:09    PAGE 1

Component

Name                              Abbrev.

Description

-------------------------------------------------------------------------------

Advance Directive                 CD

This component contains advance directive notes entered using the Text

Integration Utilities (TIU).  Advance Directives are a type a progress

note which includes clinical information that clinicians need to be

alerted to.  Time and maximum occurrent limits apply to this component.

If this component is printed to either a CRT or another device type,

information will include title, text of note, electronic signature block,

and date/time posted.

Brief Adv React/All               BADR

This component provides patient allergy/adverse reaction information from

the Allergy Tracking System. It provides a brief patient list of all known

food, drug and environmental allergies or adverse reactions (e.g., hay

fever).

Adv React/Allerg                  ADR

This component provides patient allergy/adverse reaction information from

the Allergy Tracking System. It provides a list of all known food, drug

and environmental allergies or adverse reactions (e.g., hay fever). Data

element included are type of reaction, mechanism of reaction, causative

agent, verification status, signs/symptoms for the reaction, the

originator, and comments.

Allergies/ADRs                    MRT5

This component displays local facility and remote facility allergy and

adverse data information using the Remote Data Interoperability features

of the Health Data Repository.  Data from the local facility is merged

into a single table with remote facility allergy/adverse reaction data.

CLINICAL MAINTENANCE

Reminder Brief                    CMB

This is a brief version of the CLINICAL REMINDERS MAINTENANCE component.

Reminders Due                     CR

This component lists only clinical reminders that are due now. If the date

the reminder was last satisfied is known it is listed under LAST.

Otherwise the word unknown is printed.

Reminders Findings                CF

This component lists reminders findings for reminders that are due and not

due as does the CRS component.

Reminders Last Done               CLD

This component shows reminders with the Last Done Date if it is defined.

Reminder Maintenance              CM

This component lists reminders that are due and not due as does the CRS

component. In addition it shows why the reminder is due or not due.

Reminders Summary                 CRS

This component is similar to PCE CLINICAL REMINDERS DUE except that it

shows all reminders, not just those that are due. The information will

include the NEXT due date, or N/A, and the LAST DATE. N/A reminders will

be displayed unless the IGNORE ON N/A field is set.

Clinical Warnings                 CW

This component contains clinical warning notes entered using the Text

Integration Utility (TIU).  Clinical Warnings are a type of progress note

which includes clinical information which clinicians need to be alerted

to.  No time or maximum occurrence limits apply to this component.

If this component is printed out on a CRT, information will include title,

text of note, electronic signature block, and date posted.  If the

printout is to another device type; information will include electronic

signature block and date posted to ensure security of information.

Comp. &amp; Pen. Exams                CP

This component prints all compensation and pension exams for a given

patient by user-specified time and occurrence limits.

Brief Consults                    CNB

This component displays Consults in a brief format, to include the consult

number, request date, requesting service, last action, last action date,

and the consult "TO" service.

Crisis Notes                      CN

This component contains crisis notes entered using the Text Integration

Utility (TIU).  Crisis Notes are a type of progress note which contains

important information for anyone who deals with a patient.  No time or

maximum occurrence limits apply to this component.

If this component is printed out on a CRT, information will include title,

text of note, electronic signature block, and date posted. If the printout

is to another device type, information will include electronic signature

block and date posted to insure security of information.

Dietetics                         DI

This component contains information from the Dietetics package.  Time and

occurrence limits apply to this component.  Data presented include: diet

orders, start/stop dates, type of service (tray, e.g.); nutritional

status, date assessed; supplemental feedings, start/stop dates; tube

feedings, start/stop dates, strength of product, quantity ordered, and

daily dosages.

Note:  When a time limit is selected, the data presented reflects orders

initiated within the time period.

Discharge Summary                 DCS

This component prints all discharge summaries (including report text) for

user-specified time and occurrence limits.

Brief Disch Summary               BDS

This component prints the admission, discharge and cosignature dates, as

the dictating and approving provider names, and signature status of all

discharge summaries for user-specified time and occurrence limits.

Referral Count                    GECC

Referral Categories               GECH

Global Assess Funct               GAF

This component displays the GAF score taken from the Global Assessment

Functioning scale to evaluate the psychological, social, and occupational

functioning on a hypothetical continuum of mental health/illness.  Also

displayed is the date of the assessment and the name of the health care

professional who provided the assessment.

HS Environment                    ENV

Imaging Impression                II

This component contains impressions from the Radiology/Nuclear Medicine

package.  Time and maximum occurrence limits apply.  Data presented

include:  study date, procedure(s), status, diagnostic text and

radiologist's or nuclear med physician's impression (narrative).

Only imaging impressions which have been verified are reported.

Sel Image Impression              SII

This component contains impressions from the Radiology/Nuclear Medicine

package.  Time and occurrence limits apply.  Data presented include: study

date, procedure(s), status, diagnostic text, and radiologist's or nuclear

med physician's impression (narrative) for the procedures selected by the

user (e.g., CHEST 2 VIEWS - PA &amp; LAT).

Only imaging impressions which have been verified are reported.

Imaging Profile                   IP

This component contains information from the Radiology/Nuclear Medicine

package.  Time and maximum occurrence limits apply.  Data presented

include:  study date, procedure(s) with status(es), report status, staff

and resident interpreting physicians, and the narrative fields modifier,

history, report, diagnostic text and impression.

Only imaging profiles which have been verified are reported.

Imaging Status                    IS

This component contains procedure statuses from the Radiology/Nuclear

Medicine package. Time and maximum occurrence limits apply. Data presented

include: request date/time, status, procedure, scheduled date/time, and

provider name.

Blood Availability                BA

This component contains information from the Blood Bank module of the Lab

Package. Time and occurrence limits apply to this component. Data

presented include: patient blood type (whether or not units have been

assigned), unit expiration date, unit ID#, blood product(s), cross-match

results, last known location, and a flag for autologous units.

Note:  An asterisked date (e.g., * 10/10/90) indicates that the unit is

due to expire within the next 48 hours.

Blood Transfusions                BT

This component contains information from the Blood Bank module of the Lab

Package.  Time and occurrence limits apply to this component.  Data

presented include:  transfusion date and abbreviated blood products (with

total number of units transfused for each, e.g., RBC (2)).  A key of the

abbreviations is presented at the bottom of the display to help identify

any unfamiliar blood products.

Chem &amp; Hematology                 CH

This component contains information extracted from the Lab package.  Time

and maximum occurrence limits apply to this component. Data presented

include:  collection date/time, specimen, test name, results (w/ref flag:

High/Low/Critical), units, and Reference range.  Comments will also be

conditionally displayed, depending on the value of the DISPLAY COMMENTS ON

LABS Health Summary Site Parameter.  Results which include comments will

be indicated with the symbol !!, in the event that the parameter is set to

0 or NO.

Lab Cum Selected                  SCLU

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select any number of atomic Lab tests. Data

presented include:  collection date/time, specimen, test names with

results and reference flags in columnar (horizontal) format. Comments will

also be conditionally displayed, depending on the value of the DISPLAY

COMMENTS ON LABS Health Summary Site Parameter. When comments are

displayed, a lower case letter will be displayed to the left of the date

for entries with comments. Comments will be displayed after all the

results are displayed with comments being linked by the lower case letter.

Up to 26 comments can be included.

Lab Cum Selected 1                SCL1

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select as many as seven atomic Lab tests. Data

presented include: collection date/time, specimen, test names with results

and reference flags in columnar (horizontal) format. Comments will also be

conditionally displayed, depending on the value of the DISPLAY COMMENTS ON

LABS Health Summary Site Parameter. When comments are displayed, a lower

case letter will be displayed to the left of the date for entries with

comments. Comments will be displayed after all the results are displayed

with comments being linked by the lower case letter. Up to 26 comments can

be included.

Lab Cum Selected 2                SCL2

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select as many as seven atomic Lab tests. Data

presented include: collection date/time, specimen, test names with results

and reference flags in columnar (horizontal) format. Comments will also be

conditionally displayed, depending on the value of the DISPLAY COMMENTS ON

LABS Health Summary Site Parameter. When comments are displayed, a lower

case letter will be displayed to the left of the date for entries with

comments. Comments will be displayed after all the results are displayed

with comments being linked by the lower case letter. Up to 26 comments can

be included.

Lab Cum Selected 3                SCL3

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select as many as seven atomic Lab tests. Data

presented include: collection date/time, specimen, test names with results

and reference flags in columnar (horizontal) format. Comments will also be

conditionally displayed, depending on the value of the DISPLAY COMMENTS ON

LABS Health Summary Site Parameter. When comments are displayed, a lower

case letter will be displayed to the left of the date for entries with

comments. Comments will be displayed after all the results are displayed

with comments being linked by the lower case letter. Up to 26 comments can

be included.

Lab Cum Selected 4                SCL4

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select as many as seven atomic Lab tests. Data

presented include: collection date/time, specimen, test names with results

and reference flags in columnar (horizontal) format. Comments will also be

conditionally displayed, depending on the value of the DISPLAY COMMENTS ON

LABS Health Summary Site Parameter. When comments are displayed, a lower

case letter will be displayed to the left of the date for entries with

comments. Comments will be displayed after all the results are displayed

with comments being linked by the lower case letter. Up to 26 comments can

be included.

Cytopathology                     CY

This component contains information extracted from the Cytopathology

module of the Lab package. Time and maximum occurrence limits apply.  Data

presented include:  collection date/time, accession number, specimen,

gross description, microscopic exam, brief clinical history, and

Cytopathology Diagnosis.

Electron Microscopy               EM

This component contains information extracted from the Electron Microscopy

module of the Lab package. Time and maximum occurrence limits apply. Data

presented include:  collection date/time, accession number, specimen,

gross description, microscopic exam, supplementary report description,

brief clinical history, and EM Diagnosis.

Microbiology                      MIC

This component contains information extracted from the Microbiology module

of the Lab Package.  Time and maximum occurrence limits apply. Data

include:  collection date/time, collection sample, site/specimen, specimen

comment, tests, urine screen, sputum screen, sterility control, sterility

results, comments for reports, smear/prep, acid fast stain Parasite

Report, organism(s), Mycology Report, Bacteriology Report,

Mycobacteriology Report, Gram Stain Result, Culture and Susceptibility,

Antibiotic Serum Level, and remarks.

Brief Microbiology                BMIC

This component contains information extracted from the Lab package. Time

and maximum occurrence limits apply to this component in addition to

collection date/time, test names, specimen, report status, Culture and

Susceptibility, Smear/Prep, Acid Fast Stain, Antibiotic Serum Level, and

test results.

Lab Orders                        LO

This component contains information extracted from the Lab package.  Time

and maximum occurrence limits apply. Data presented include: collection

date (either actual or expected), lab test, provider, accession, date/time

ordered, specimen, and date/time results available.

Brief Lab Orders                  BLO

This component contains information extracted from the Lab package.  Time

and maximum occurrence limits apply. Data presented include: collection

date/time, lab test name, specimen, urgency, and order status (e.g.,

ORDERED, COLLECTED, PROCESSING, COMPLETE).

Surgical Pathology                SP

This component contains information extracted from the Surgical Pathology

module of the Lab package. Time and maximum occurrence limits apply. Data

presented include:  collection date/time, accession number, specimen,

gross description, microscopic description, brief clinical history,

supplementary report description, frozen section and surgical path

diagnosis.

Lab Tests Selected                SLT

This component contains information extracted from the Lab package. Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select any number of atomic Lab tests. Data

includes: collection date/time, specimen, test name, result, units and

reference range. Comments will also be conditionally displayed, depending

on the value of the DISPLAY COMMENTS ON LABS Health Summary Site

Parameter. Results which include comments will be indicated with the

symbol !!, in the event that the parameter is set to 0 or NO.

Note: This component corresponds to the vertical format for the Lab

package's cumulative reports.

MAG Imaging                       MAGI

This component lists the available images along with the procedure name

and short description.

Admission/Discharge               ADC

This component contains information from the MAS package.  Time and occurrence limits apply to this component.  Data presented include: date range of admission, ward, length of stay (LOS), last treating specialty, last provider, admitting diagnosis text, bedsection, principal diagnosis, diagnosis for longest length of stay (DXLS), and secondary ICD diagnoses.

ADT History                       ADT

This component contains information extracted from the MAS package.  It

can only be used with MAS Version 5 and up.

Time and maximum occurrence limits apply.  Data presented include:

movement date, movement type (ADM=Admission, TR=Transfer, TS= Treating

Specialty, DC=Discharge), movement description, specialty, and provider.

ADT History Expanded              EADT

This component contains information extracted from the MAS package. It is a consolidated view of all the MAS components. It can only be used with MAS Version 5 and up.

Time and maximum occurrence limits apply. Data presented includes patient eligibility and rated disabilities. Movement data then follows with movement date, movement type (ADM=Admission, TR=Transfer, TS= Treating Specialty, DC=Discharge), movement description, specialty, and provider. Admissions include the admission diagnosis if the patient hasn't been discharged. Transfers include ward location and transfer facility. Treating specialties include Specialty Transfers Diagnosis. Discharges include the data in the Discharge Diagnosis and Discharges components. Following the data for each admission, ICD Procedures and ICD Surgeries will be included, if present.

Fut Clinic Visits                 CVF

This component provides a listing from the MAS scheduling module that

contains future clinic visit dates, the clinic visited, and the

appointment type.

Past Clinic Visits                CVP

This component contains information from the MAS scheduling module.  Time

and occurrence limits apply to this component.  Data presented include:

past clinic visits, dates, and a visit status (e.g., NO SHOW, INPATIENT

VISIT).  Note: Cancellations and Unscheduled Visits are shown.

Patient Contacts                  CON

This component lists (if available) the following patient contact

information: Patient Phone (Cell, Home, Work) Name, Relationship, and

Phone Number of the: Emergency Contact, Secondary Emergency Contact, and

Secondary NOK Contact

Demographics                      DEM

This component contains the following patient demographic data (if

available) from the MAS package: address, phone, county, marital status,

religion, age, sex, race, ethnicity, occupation, period of service, POW

status (e.g., Y or N), branch of service, combat status (e.g., Y or N),

eligibility code, current (verified) eligibility status, service connected

%, mean test, primary and secondary next of kin (NOK), NOK phone number

and address.

Brief Demographics                BDEM

This component contains information from the MAS package.  It provides

brief patient demographic information including: address, phone number,

age, sex, race, ethnicity, mean test, and eligibility code (e.g., service

connected 50-100%).

Disabilities                      DS

This component provides information from the MAS package about a patient's

eligibility code and eligibility status (Verified), and rated

disabilities, including the disability percentage and whether the

disability is service connected or non-service connected.

Discharge Diagnosis               DD

This component contains information extracted from the MAS package. Time and occurrence limits apply to this component.  Data presented include: Date range of admission through discharge, length of stay (LOS), Principal diagnosis, diagnosis for longest length of stay (DXLS), and secondary ICD discharge diagnoses.

Note: This component provides discharge diagnoses coded in the MAS PTF file. The occurrence limits are determined by the occurrence of admissions.

Discharges                        DC

This component contains information extracted from the MAS package. Time

and occurrence limits apply to this component.  Data presented include:

date of discharge, DXLS, bedsection, disposition type, disposition place,

and outpatient treatment flag.

Note: The occurrence limits are determined by the occurrence of

admissions.

MH Clinic Fut Visits              MHFV

This component displays the next scheduled appointment(s) to any MH

clinic.  MH Clinics are identified using the VA-MH NO SHOW APPT CLINICS LL

Reminder Location List.

ICD Procedures                    PRC

This component contains MAS coded procedures, by admission, extracted from the MAS package.  Time and occurrence limits apply to this component. Data presented include:  procedure date, procedure name, and ICD procedure codes.

Note: The occurrence limits are determined by the occurrence of admissions.

ICD Surgeries                     OPC

This component contains MAS coded surgeries, by admission, extracted from the MAS package.  Time and occurrence limits apply to this component. Data presented include:  surgery date, procedure name, and ICD procedure codes.

Note: The occurrence limits are determined by the occurrence of admissions.

Transfers                         TR

This component contains information extracted from the MAS package.  Time

and occurrence limits apply to this component.  Data presented include:

transfer date, type, destination, and provider (when available).

Note: The occurrence limits are determined by the occurrence of

admissions.

Treating Specialty                TS

This component contains information extracted from the MAS package.  Time

and occurrence limits apply to this component.  Data presented include:

treating specialty change date/time, new treating specialty, (admission

date), and provider.

Note: The occurrence limits are determined by the occurrence of

admissions.

Med Abnormal                      MEDA

This component contains information extracted from the Medicine package.

Data presented include:  procedure date/time, medical procedure name, and

result (e.g., normal, abnormal, borderline).  Time and maximum occurrence

limits apply.

Med Brief Report                  MEDB

This is the brief procedure view defined by the Medicine View file.  This

output can be managed by the local IRM staff.  Time and maximum occurrence

limits apply.

Med Full Captioned                MEDC

This prints the full set of results which are present in each procedure.

No labels will be included which have no values associated with them.

Time and maximum occurrence limits apply.

Med Full Report                   MEDF

This component provides a full report of procedures as defined by the

Medicine View file.  This report includes labels which have no value

associated with them.  Time and maximum occurrence limits apply.

Med (1 line) Summary              MEDS

This component provides a one line summary view of Medicine procedures

which is extracted from the Medicine package. Time and maximum occurrence

limits apply.  Data presented include: procedure date/time, medical

procedure name, and result (e.g., normal, abnormal, borderline).  Note:

This component is a summary of procedure statuses.

MH Physical Exam                  MHPE

The Mental Health Physical Exam component contains the results of the

physical examination concerning patient's overall condition associated

with the systems identified. This data is being extracted from the Medical

Record (# 90) file.

MH Suicide PRF Hx                 MHRF

This component displays the assignment status and history for the Category

I (National) HIGH RISK FOR SUICIDE Patient Record Flag.  Any assignment

history found for the Category II (Local) High Risk for Suicide flag will

also be displayed.

MH Treatment Coor                 MHTC

This component displays Mental Health Treatment Coordinator (MHTC)

assigned to this patient.

MHA Admin List                    MHAL

This component displays all administrations of instruments in the mental

health package for the specified patient. All administrations from MH

Administrations (file #601.84) are shown.  Date ranges and maximum

occurrences apply.

MHA Score                         MHAS

This component displays the administration and scoring of instruments in

the mental health package. Tests, interviews and surveys from MH TESTS and

SURVEYS (file # 601.71) must be selected.  Date ranges and maximum

occurrences apply.

Detail Display                    MHVD

This component display the detail description of all Clinical Reminders

that are define for MyHealtheVet.

Summary Display                   MHVS

This component display the summary description of all Clinical Reminders

that are define for HealtheVet.

Med Reconciliation                MRR1

This component generates a list of the patient's complete medication

profile, including Outpatient Rx's, Inpatient Medication Orders, Clinic

Orders, Non-VA Medications, and Remote Active Medications.  It is sorted

alphabetically by drug name, creating groups of outpatient/inpatient

orders for the same item in order to facilitate medication reconciliation.

Med Reconciliation                MRT1

This component generates a list of the patient's complete medication

profile, including Outpatient Rx's, Inpatient Medication Orders, Clinic

Orders, Non-VA Medications, and Remote Active Medications.  It is sorted

alphabetically by drug name, creating groups of outpatient/inpatient

orders for the same item in order to facilitate medication reconciliation.

Medication Worksheet              MRT2

This component displays a list of the patient's active and pending

outpatient prescriptions in a patient-friendly worksheet format with space

intended for written notes by the patient, provider or caregiver.

Medication Worksheet              MRT2

This component displays a list of the patient's active and pending

outpatient prescriptions in a patient-friendly worksheet format with space

intended for written notes by the patient, provider or caregiver.

Next of Kin                       NOK

Displays the name, relation, address, phone number of the Next of Kin.  If

a Secondary Next of Kin exist, then it will be printed too.

Non VA Meds                       RXNV

This component displays the non-VA medications taken or reported as used

by a patient.

Oncology                          ONC

This component will extract selected data items from the ONCOLOGY PRIMARY

file.

Current Orders                    ORC

This component contains current orders from the OE/RR package.  Since the

OE/RR package integrates all orders for the ancillary services, the orders

will be reported in most recent orders first sequence without concern for

the ancillary package the order originated from/for. Current orders are

defined as those orders with an OE/RR order status other than discontinued

or expired.

The component information includes item ordered, OE/RR order status, start

date, and stop date. OE/RR order status abbreviations include

"blank"=Active, "c"=Complete, "dc"=Discontinued, "e"= expired,

"?"=Flagged, "h"=Hold, "i"=incomplete, "p"=pending, "s"=scheduled.

Education                         ED

This component lists the patient education topics and a brief assessment

of the patient's understanding of the topic for a particular patient for

user-specified time and occurrence limits. Some examples of topics are

complications, diet, disease process, exercise, follow-up care, general

information, lifestyle adaptations, medications, nutrition, smoking, etc.

Education Latest                  EDL

This component lists the latest patient education for each topic and a

brief assessment of the patient's understanding of the topic for a

particular patient for a user-specified time limit. Some examples of

topics are complications, diet, disease process, exercise, follow-up care,

general information, lifestyle adaptations, medications, nutrition,

smoking, etc.

Exams Latest                      EXAM

This component lists the latest examination information and results for a

particular patient for a user-specified time limit. Some examples of exam

types are eye exams, ear exams, neurological exams, pelvis exams, etc.

Health Factors                    HF

This component lists all the health factors associated with a particular

patient for user-specified time and occurrence limits. The list will

display health factors by category and include a level of severity for

each health factor including Minimal(M), Moderate(MO), and

Heavy/Severe(H).

Set the occurrence limit to 1 to list the latest unique health factors

within each category.  (E.g. If there were 12 "Non-Smoker" health factor

entries, only the latest "Non-Smoker" entry would display.)

Note: Health Factors have a DISPLAY ON HEALTH SUMMARY option that

determines whether or not they will show on a Health Summary report.

Health Factor Select              SHF

This component allows a user to select specific health factors by category

and then lists the health factors, which apply to a particular patient for

user-specified time and occurrence limits.

Set the occurrence limit to 1 to list the latest unique health factors for

each selected category. (E.g. If there were 12 "Non-Smoker" health factor

entries, only the latest "Non-Smoker" entry would display.

Note: Health Factors have a DISPLAY ON HEALTH SUMMARY option that

determines whether or not they will show on a Health Summary report.

Immunizations                     IM

This component lists the immunizations (e.g., Rubella, Smallpox, etc.) and

information about each immunization administered to a particular patient.

Location of Home                  LH

This component lists directions to a particular patient's home.

Outpatient Diagnosis              OD

This component lists outpatient diagnosis (ICD) for a particular patient.  The user can specify time and occurrence limits, whether hospital location should be displayed or not, the format of ICD data (e.g. code only, long text, short text or no ICD data), and whether the provider narrative should be displayed or not.

Outpatient Encounter              OE

This component lists outpatient diagnosis (ICD) and procedure (CPT) for a particular patient. The user can specify item and occurrence limits, whether hospital location should be displayed or not, the format of ICD data (e.g. code only, long text, short text or no ICD data), and whether the provider narrative should be displayed or not.

Skin Tests                        ST

This component lists the skin tests and the results (e.g. positive,

negative, doubtful, or no take) for a particular patient. Some examples of

skin tests are cocci, mon-vac, PPD, schick, tine, etc.

Treatments Provided               TP

This component lists treatments provided that are not covered in the

IDC-9-CM procedures for a particular patient for user specified time and

occurrence limits. Some example of treatment types include nursing

activities such as ear irrigation, dental care instructions, or preventive

health care counseling.

IV Pharmacy                       RXIV

This component contains IV orders extracted from the Pharmacy package.

Only time limits apply.  Data presented include:  start date, stop date,

drug (additives), dose, status, solutions and infusion rates.

Note: If no time limit is defined, only active IV orders are reported.  If

a time limit is defined, all IV orders which have an expiration or cancel

date within the time limit range are reported.

Outpatient Pharmacy               RXOP

This component contains information from the Outpatient Pharmacy package.

Only time limits apply.  Data presented include:  drug, prescription

number, status expiration/cancellation date (when appropriate), quantity,

issue date, last fill date, refills remaining, provider, and cost/fill

(when available).

Note: If no time limit is defined, only active outpatient orders are

reported. If a time limit is defined, all outpatient pharmacy orders which

have an expiration or cancel date within the time limit range are

reported.

Unit Dose Pharmacy                RXUD

This component contains Unit Dose information extracted from the Pharmacy

package.  Only time limits apply.  Data presented include:  Drug, dose,

pharmacy status, start date, stop date, and sig (which includes schedule

instructions and route).

NOTE: If no time limit is defined, all active orders are reported.  If a

time limit is defined, all unit dose orders which have an expiration or

cancel date within the time limit range are reported.

Active Problems                   PLA

This component lists all known active problems for a patient. Information

displayed: ICD data (based on ICD Text Display parameter), provider

narrative (unless Provider Narrative Display parameter is set to NO), date

of onset, date last modified, the responsible provider, and all active

comments.

All Problems                      PLL

This component lists all known problems, both active and inactive, for a

patient. Information displayed: ICD data (based on ICD Text Display

parameter), provider narrative (unless Provider Narrative Display

parameter is set to NO), date of onset (if problem is active), date

problem resolved (if inactive), date last modified, the responsible

provider, and all active comments for the problems.

Inactive Problems                 PLI

This component lists all known inactive problems for a patient.

Information displayed: ICD data (based on ICD Text Display parameter),

provider narrative (unless Provider Narrative Display parameter is set to

NO), date problem resolved, date last modified, the responsible provider,

and all active comments for the problem.

Progress Notes                    PN

This component contains progress notes entered using the Text Integration

Utilities (TIU) and Mental Health packages.  Time and maximum occurrence

limits apply to this component.  Data presented include:  Progress note

date/time written, title, text of note, electronic signature block

(including possible cosignature and cosigner comments), and the note's

correction text and correction date/time.

Only those notes which have been signed with an electronic signature or

electronically marked signed on chart will be reported.

Brief Progress Notes              BPN

This component contains limited information from progress notes entered

using the Text Integration Utility (TIU) or the Mental Health packages.

Time and maximum occurrence limits apply.  Data presented includes:

Progress note date/time, title, author and last correction date/time.

Only those notes which have been signed with an electronic signature or

electronically marked signed on chart will be listed.

Selected Prog Notes               SPN

This component allows for the selection of specific progress notes by

document title.  These progress notes were entered using the Text

Integration Utilities (TIU).  Data presented include:  Progress note

date/time written, title, text of note, electronic signature block

(including possible cosignature and cosigner comments), and the note's

correction text and correction date/time.

Only those notes which have been signed with an electronic signature or

electronically marked signed on chart will be reported.

Spinal Cord Dysfunct              SCD

This component provides patient data from the Spinal Cord Dysfunction

package. A patient's registration status, highest level of injury,

information source for SCD, completeness of injury and extent of paralysis

will be displayed. The following data will be displayed with time and

maximum occurrence limits applied:  date of onset, etiology, onset of SCD

caused by trauma, date recorded, motor score, cognitive score, total score

and record type.

NON OR Procedures                 NSR

This component will print out data for NON-OR procedures only.  Time and

maximum occurrence limits apply.  The data presented will be: provider

specialty, provider, procedure status, attending, principal diagnosis,

procedures performed, principal anesthesiologist, indication for

procedure, and operative findings.

Surgery Only Reports              SRO

This component will return surgery procedures only and will NOT include

NON-OR procedures.  Time and maximum occurrence limits apply.  For

Surgical procedures the data presented will be: surgery date, surgeon,

surgery report status, pre-operative diagnosis, post-operative diagnosis,

surgeon's dictation, current procedural terminology operation code and

text, and principal anesthesiologist.

Surgery Rpt (OR/NON)              SR

This component contains information from the Surgery package.  Time and

maximum occurrence limits apply.  It includes NON-OR procedures as well as

Surgical procedures.  The data returned will differ for surgical and

NON-OR procedures.

For Surgical procedures the data presented will be: surgery date, surgeon,

surgery report status, pre-operative diagnosis, post-operative diagnosis,

surgeon's dictation, current procedural terminology operation code and

text, and principal anesthesiologist.

For NON-OR procedures the data presented will be: provider specialty,

provider, procedure status, attending, principal diagnosis, procedures

performed, principal anesthesiologist, and indications for procedure.

Brief Surgery Rpts                BSR

This component contains surgery report statuses extracted from the Surgery

package.  Time and maximum occurrence limits apply.  Data presented

include: surgery date, surgical procedure, and report status (e.g.,

COMPLETE).

Selected NON-OR Proc              SNSR

This component will return selected NON-OR procedures.  The user will be

allowed to select one or more CPT codes to search for.  The NON-OR

procedures will be displayed if the selected CPT code(s) match the

principal procedure code.  Time and maximum occurrence limits apply.  The

data presented will be: provider specialty, provider, procedure status,

attending, principal diagnosis, procedures performed, principal

anesthesiologist, indication for procedure, and operative findings.

URINALYSIS                        URIN

This component contains information extracted from the Lab package.  Not

only do time and maximum occurrence limits apply to this component, but

the user is allowed to select as many as seven atomic Lab tests.  Data

presented include:  collection date/time, specimen, test names with

results and reference flags in columnar (horizontal) format.

Vital Signs                       VS

This component contains vital measurements extracted from the Vital Signs

module of the Nursing package.  Time and maximum occurrence limits apply.

Data presented include:  measurement date/time, blood pressure (as

SBP/DBP), pulse, temperature, height, weight, and respiratory rate.

Detailed Vitals                   VSD

This component contains vital measurements extracted from the Vital Signs

module, and differs from other Health Summary Vital Signs displays by

including the Vital Signs Qualifiers (sitting, standing, left arm, etc.)

with the vitals measurement.  Time and maximum occurrence limits apply.

Data presented includes measurement date and time, temperature, blood

pressure, pulse, height, weight, respiratory rate,CVP, PO2, circumference

and girth, and pain.

Vital Signs Outpat.               VSO

This component contains outpatient vital measurements extracted from the

Vital/Measurements (Gen. Med. Rec. - Vitals) package.  Time and maximum

occurrence limits apply.  Data presented includes: measurement date/time,

blood pressure, (as SBP/DBP), pulse, temperature, height, weight, and

respiratory rate.  Metric values will be displayed for temperature, height

and weight.  If there are no outpatient measurements, a message will be

displayed and the last non-outpatient measurements will be shown.

Vital Signs Selected              SVS

This component contains selected vital measurements extracted from the

Vital Signs module of the Nursing package.  Time and maximum occurrence

limits apply, and the user is allowed to select any of the vital

measurement types defined in the Vital Type file (e.g., pulse, blood

pressure, temperature, height, weight, and respiration rate).  Data

presented include: measurement date/time, measurement type and measurement

value.  Note: Formatted display is horizontal.

Vital Select Outpat.              SVSO

This component contains selected outpatient vital measurements extracted

from the Vital/Measurements (Gen. Med. Rec. - Vitals) package.  Time and

maximum occurrence limits apply, and the user is allowed to select any of

the vital measurement types defined in the GMRV Vital Type file (e.g.,

pulse, blood pressure, temperature, height, weight, and respiration rate).

Data presented includes: measurement date/time, measurement type and

measurement value, and metric values for temperature, height and weight.

If there is no outpatient measurements, a message will be shown and the

last selected non-outpatient measurements will be shown.  Note: Formatted

display is horizontal.

MH HIGH RISK PRF HX

This component displays the assignment status and history for the Category I (National)and Category II (Local) HIGH RISK FOR SUICIDE Patient Record Flag.

MH TREATMENT COORDINATOR

This component displays the Mental Health Treatment Team, Mental Health Treatment

Coordinator (MHTC), and the MHTC contact information.

PHARMACY ORDERABLE ITEM	RXOI

This component returns Pharmacy Orderable Item file (#50.7) information. It also distributes the data dictionary for the Pharmacy Orderable Item file (#50.7 in order to make it available for Health Summary Component file selection.

VA DRUG CLASS	RXDC

This component allows the selection of Outpatient prescriptions by drug class (VA classification). It returns the VA DRUG CLASS file (50.605) contents.

- **Note:** For the components RXOI and RXDC, drug classes or orderable items that are selected will display in the header. If any of the items were not ordered for the patient, the item would still display in the header but would not be in the list.

Sample output from the updated components:

#### Sample of RXDC Report

<!-- image -->

#### Sample of RXOI Report

<!-- image -->

## Appendix B—VISTA And Health Summary Conventions

#### Special Keys, Commands, and Symbols

To use the Health Summary package you need to know how to log on, navigate among menus, and respond to prompts for entry of information. If you need help, ask a coordinator or IRM staff member to give you training or training materials on these topics.

The Health Summary package follows Kernel and VA FileMan user conventions. A few package-specific symbols, keys, and option responses are briefly described here and fully described throughout this manual at appropriate places.

**&lt;Enter&gt;** Enter return (indicated by &lt;Enter&gt; in this manual) after every response or when you wish to bypass a prompt, accept a default, or return to a previous action.

**Comp=C** Enter a health summary component abbreviation equal to C (e.g., ADR=C) to temporarily change a component’s Occurrence Limit, Time Limit, Hospital Location Display, ICD Text Display, Provider Narrative Display, and Selection Items (if it’s a selected component and these items are used).

**?** Enter a question mark after a prompt to see valid instructions for responding to that prompt.

**??** Enter two question marks to see more detailed instructions or a list of choices.

**//** Double slashes indicate a default response has been provided by Health Summary to speed up the entry process. This is either the most likely choice, the safest response (e.g., Do you really want to delete this .....? NO//), or a previously entered response (for example, Select Health Summary Type: INPATIENT//). If you wish to select the default response INPATIENT, press the return key. Otherwise, type the name of a different summary type.

**^** A single up-arrow (also called a caret or circumflex) functions several ways in this package depending on where you are and what you’re doing. The up-arrow can terminate a series of questions and return you to a previous level. It can also exit you from the health summary and take you to the Select Patient: prompt.

**^^** A double up-arrow exits you out of the menu option you’re in and returns you to the menu.

**+** Enter a plus sign (+) after the "Press &lt;Enter&gt; to continue, ^ to exit, or select component:" prompt to advance to the beginning of the next component when viewing an online health summary.

**-** Enter a minus sign (-) at the "Press &lt;Enter&gt; to continue, ^ to exit, or select component: prompt returns you to the beginning of the previously displayed component when viewing an online health summary.

#### Printing Conventions:

When you are prompted for Device: you have the following choices.

&lt;Enter&gt; 	Accepts the default causing the summary to be displayed on your CRT screen.

LASER	Enter a valid printer name (LASER is an example).

?	Lists printers from which you can select one.

Q or q	Allows you to queue the health summary task (meaning

it will print at a later time and place). When queuing a

task make sure you enter a *time* in addition to a date;

for example: DO YOU WANT YOUR OUTPUT QUEUED? NO// **Y** YES

Requested Start Time: NOW// **T+1@1500** ( **T** oday **+ 1** day, (meaning tomorrow) **at 1500** ).

## Appendix C—Historical Documentation Shift from GMTS*2.7*133 (Do Not Update)

### New Features in Health Summary

Patches 101, 107, 102, 95, 93, 90, 91, 88, 85, and some of the other more recent patches are described below. For complete descriptions of all changes in Health Summary since the release of version 2.7 in 1994, please refer to the patches (described briefly on page 6 and in more detail in the Patch module on Forum).

**New Components**

See Appendix A for a complete list of Health Summary components.

Patch GMTS*2.7*125 Updates for Health Summary Components

GMTS*2.7*125 is installed with patches PSN*4.0*567 and PSS*1.0*234 to release two new national Health Summary components that can be used to create objects or in Ad-Hoc reporting.

The components allow the selection of Outpatient prescriptions by drug class (VA Classification) or by Pharmacy Orderable Item name.

HEALTH SUMMARY COMPONENTS affected:

RXDC	Meds Op/Drug Class

RXOI	Meds Op/Rx Ord Item

Patch GMTS*2.7*94 Updates for the Essential Med List for Review

GMTS*2.7*94 will be installed with PSO*7*314  to correct issues reported with the Tool #1: Medication Reconciliation.  The Health Summary patch GMTS*2.7*94 will create a national entry in the HEALTH SUMMARY COMPONENT file (#142.1) for Tool #1: Med. Reconciliation (the abbreviation is MRT1).

Furthermore, a replica of the Tool #1 Medication Reconciliation called Medication Reconciliation No Glossary Tool #1 (the abbreviation is MRR1) will be created. The only difference between the two components is whether the Health Summary has a glossary. In the Essential Med List for Review Health Summary type, the site can use either the MRT1 component if they want the glossary at the end of the Health Summary, or if the site uses the MRR1 component, the same Health Summary will be displayed without the glossary at the end of the report.

Another feature recently added was to include all Dispense Drug data, including BCMA Last Action, into the report for Inpatient Medication data which incorporates Dosage information as well.

The GMTS*2.7*94 patch changes include the following:

Usage of data from other VA pharmacies via Remote Data Interoperability

(RDI) updated to include prescriptions where the status is “HOLD.”

1. The Essential Med List for Review was upated to retrieve all necessary BCMA actions, particularly for large volume IVs.

1. Corrected the service for Clinic Medications that used to show the service as “INPT,” The service for Clinic Medications now reads “CLIN.”

1. Ensured that the most recent order information was being correctly gathered. The change involved looking at the correct field in the prescription information and no longer infer that the latest expiration date implied the latest prescription.

1. The tool was modified to display multiple line provider comments in a more readable fashion.

1. The program was updated to assume that DoD prescriptions with an issue date more than 1 year in the past must be, by definition, now expired or discontinued and will no longer be considered “ACTIVE” even though that is precisely what is returned by the CHDR data.

1. The section of the report that showed “Other medications previously dispensed in the last year” was misleading. For example, prescriptions with no refills that were over 120 days old would not display at all. In some cases, this led to the belief that the Sig that was displaying was incorrect. The section in question has been removed from the report and the medications needed for the report were incorporated into the main body of the report.

1. The code was modified to recognize the On Call property flag for IV types of admixtures.

1. The following changes were also made:
    - Introductory text changed to describe what the report contains, what is does not contain, and that it specify what remote data is shown
    - Remote data warnings that give some information about why remote data may not display
    - Changes in the status names (Hold changed to On Hold, Suspended changed to Active/Suspended, etc)
    - Rx# added to active outpatient prescriptions
    - QTY added to days supply for outpatient
    - Status added to inpatient entries
    - Additive strength added to Intravenous Piggyback (IVPB) orders
    - Added pending orders to inpatient and outpatient
    - INP changed to INPT and OPT changed to OUTPT
    - Added additive strength and bags/day to inpatient IV Adm
    - Added status, admin rate, dose and freq to IVPBs, including number of bags per order
    - Added volume and rate of infusion to IV Adms
    - Supplies now separated from medications list
**Example of the Essential Med List for Review with the medication reconciliation information, allergy information, and the glossary of terms**
08/16/2018 11:01
*********  CONFIDENTIAL Essential Med List for Review SUMMARY   pg. 1 **********
PLJH,YDJEXALT    000-00-6671                                    DOB: 00/08/1957
---------------------------- MRT5 - Allergies/ADRs ----------------------------
FACILITY                                ALLERGY/ADR
--------                                -----------
*** WARNING: Remote Data from HDR not available ***
-------------------------- MRT1 - Med Reconciliation --------------------------
INCLUDED IN THIS LIST:  Alphabetical list of active outpatient
prescriptions dispensed from this VA (local) and dispensed from another
VA or DoD facility (remote) as well as inpatient orders (local pending and
active), local clinic medications, locally documented non-VA medications,
and local prescriptions that have expired or been discontinued in the past
90 days.
Non-VA Meds Last Documented On: ** Data not found **
************************************************************************
***NOTE*** The display of VA prescriptions dispensed from another VA or
DoD facility (remote) is limited to active outpatient prescription entries
matched to National Drug File at the originating site and may not include
some items such as investigational drugs, compounds, etc.
NOT INCLUDED IN THIS LIST: Medications self-entered by the patient into
personal health records (i.e. My HealtheVet) are NOT included in this
list. Non-VA medications documented outside this VA, remote inpatient
orders (regardless of status) and remote clinic medications are NOT
included in this list. The patient and provider must always discuss
medications the patient is taking, regardless of where the medication was
dispensed or obtained.
------------------------------------------------------------------------
OUTPT AMITRIPTYLINE HCL 10MG TAB (Status = Active)
TAKE TWO TABLETS BY MOUTH AT BEDTIME *MAY CAUSE DROWSINESS-AVOID
ALCOHOL*
Rx# 1002453 Last Released:              Qty/Days Supply: 60/30
Rx Expiration Date: 8/15/19             Refills Remaining: 11
OUTPT CEPHALEXIN 250MG CAP (Status = Active/Suspended)
TAKE SIX CAPSULES MOUTH BEFORE MEALS AND AT BEDTIME ** TAKE ON AN
EMPTY STOMACH **
Rx# 1002437 Last Released:              Qty/Days Supply: 720/30
Rx Expiration Date: 8/25/18             Refills Remaining: 0
OUTPT DIAZEPAM 5MG TAB (Status = Pending)
TAKE ONE-HALF TABLET BY MOUTH TWICE A DAY *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Login Date: 8/15/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
OUTPT DIGOXIN TAB (Status = Pending)
TAKE 0.25MG BY MOUTH DAILY
Login Date: 1/3/18                      Qty/Days Supply: 30/30
Refills Ordered: 3
OUTPT DIPHENHYDRAMINE HCL 50MG CAP (Status = Pending)
TAKE 1 CAPSULE subcutaneous EVERY EVENING *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Login Date: 4/26/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
OUTPT FENTANYL 25UG/H PATCH (Status = Active)
APPLY 1 PATCH AS DIRECTED EVERY THIRD DAY *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Rx# 1002452 Last Released:              Qty/Days Supply: 10/30
Rx Expiration Date: 9/13/18             Refills Remaining: 0
OUTPT GABAPENTIN 300MG CAP (Status = Pending)
TAKE 2 CAPSULES subcutaneous TWICE A DAY
Login Date: 4/26/18                     Qty/Days Supply: 120/30
Refills Ordered: 0
OUTPT GLIPIZIDE 10MG TAB (Status = Pending)
TAKE ONE TABLET BY MOUTH TWICE A DAY
Login Date: 1/3/18                      Qty/Days Supply: 60/30
Refills Ordered: 0
OUTPT MONTELUKAST NA 10MG TAB (Status = Pending)
TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY
Login Date: 1/3/18                      Qty/Days Supply: 120/30
Refills Ordered: 0
OUTPT SIMVASTATIN 20MG TAB (Status = Pending)
TAKE ONE TABLET subcutaneous DAILY AT BEDTIME
Login Date: 4/26/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
------------------------------------------------------------------------
SUPPLIES
------------------------------------------------------------------------
==========PHARMACY TERMS AND POSSIBLE PATIENT ACTIONS===========
INPT = VA inpatient order
IV = VA intravenous medication
OUTPT = VA outpatient prescription
PHARMACY                                       POSSIBLE PATIENT
TERMS        EXPLANATION                       ACTIONS
--------     -------------------------------   -----------------
ACTIVE       A prescription that can be        If you have refills,
filled at the local VA pharmacy.  you may request a
refill of this
prescription from
your VA pharmacy.
CLINIC       A medication you received during  If you have questions
a visit to a VA clinic or         about this medication
emergency department.             contact your VA
healthcare team.
DISCONTINUED A prescription your provider has  Contact your VA
stopped. It is no longer          healthcare team if you
available to be sent to you or    need more of this
picked up at the VA pharmacy      medication.
window.
EXPIRED      A prescription which is too old   Contact your VA
to fill. This does not refer to   healthcare team if you
the expiration date of the        need more of this
medication in the container.      medication.
NON-VA       A medication that came from       If this medication is
someplace other than a VA         medication information
pharmacy. This may be a           is incorrect or out of
prescription from either the VA   date, please tell your
other providers that was filled   VA healthcare team.
outside the VA. Or, it may be an
over-the-counter (OTC), herbal,
dietary supplement or sample
medication.
ON HOLD      An active prescription that will  Contact your VA
not be filled until pharmacy      pharmacy when you need
resolves the issue.               more of this
medication.
PENDING      This prescription order has been  If you have been
sent to the pharmacy for review   instructed to start the
and is not ready yet.             this medication now,
contact your VA
pharmacy.
SUSPENDED    An active prescription that is    Contact your VA
not scheduled to be filled yet.   pharmacy if you need
You should receive it before you  this medication
run out.                          now.
==================================================================
*** END *  CONFIDENTIAL Essential Med List for Review SUMMARY   pg. 1 *********
<!-- image -->
Example of the Essential Med List for Review showing Rx# for existing and renewed medications
**Example of the Essential Med List for Review showing an active/suspended medication and more information for IVPB for both Clinic and Inpatient medications. The second item that is highlighted is a medication with a long SIG.**
<!-- image -->
**Example of the Essential Med List for Review showing several medications from different sources, such as Inpatient (INPT), Non-VA, Oupatient (OUTPT), and Clinic (CLIN). The report shows medication statuses of Pending and Active. The report now provides more information for Non-VA meds.**
<!-- image -->
**Example of the Essential Med List for Review showing a remote medication on hold**
<!-- image -->
**Example of the Essential Med List for Review showing a new inpatient and outpatient medication status abbreviations and how there is additional information for IV Infusions**
<!-- image -->
Patch GMTS*2.7*120 – HEALTH SUMMARY UPDATE FOR Medication Reconciliation Tool #2 (MRT2)
This patch will resolve the following issues in the Health Summary package.
    1. MRT2 non-VA medications do not display in the same manner as VA-prescribed medications
    1. Problem
The problem occurs when a patient-facing report is generated from the Health Summary data. The document used currently does not display non-VA medication information as thoroughly as it does VA medications. Even when all information is available, the MRT2 report does not present the Non-VA meds consistently. In fact, there is no 'worksheet space' available for the non-VA medications. Also, note that the non-VA medication orders are not required to have all the same fields as a VA prescribed medication.
    1. Resolution
Patch GMTS*2.7*120 removes the inconsistencies in the display on the patient-facing report generated from the Health Summary data and given to the patient when admitted, discharged, or transferred.
An example of a complete patient-facing report using health summary information is as follows:
*********** CONFIDENTIAL Medication Worksheet SUMMARY pg. 1 ***********
BCMA,FIFTEEN-PATIENT   666-33-0015                      DOB: 04/07/1935
3 NORTH GU
---------------- MWS - Medication Worksheet (Tool #2) -----------------
Date: Jul 24, 2017        PATIENT MEDICATION INFORMATION        Page: 1
PRINTED BY THE VA MEDICAL CENTER AT: CAMP MASTER
FOR PRESCRIPTION REFILLS CALL (518) 472-4307
Name: BCMA,FIFTEEN-PATIENT     PHARMACY - ALBANY DIVISION
|---------------------------------------------------------------------|
|           |MORNING| NOON    |EVENING|BEDTIME|      COMMENTS         |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**PENDING**  ACARBOSE  25MG  TAB                                     |
|     TAKE ONE TABLET BY MOUTH 3XW                                    |
|     Quantity: 5 Refills: 0                                          |
|---------------------------------------------------------------------|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**PENDING**  ACETAMINOPHEN 325MG                                     |
|     TAKE ONE TABLET BY MOUTH EVERY 4 HOURS AS NEEDED                |
|     Quantity: 180 Refills: 0                                        |
|---------------------------------------------------------------------|
| UNITS PER DOSE: |       |       |       |       |                   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**NON-VA** ACARBOSE 25MG TAB                                         |
|     TAKE ONE TABLET BY MOUTH 3ID Do not take medication when        |
|     consuming alcohol. Take with a full glass of water only. Take on|
|     a full stomach. Do not mix with aspirin. Contact your provider  |
|     if you experience dizziness, excessive thirst, or hunger.       |
|---------------------------------------------------------------------|
| UNITS PER DOSE: |       |       |       |       |                   |
|---------------------------------------------------------------------|
Any medication items listed as "pending" are those that have just been written by your provider(s). These medication orders will be reviewed by your pharmacist, prior to the prescription(s) being dispensed. When you receive your new prescription(s), by mail or from the pharmacy window,be sure to follow the instructions on the prescription label. If you have any question about your medication, please call your provider or your pharmacist.
Any medication items listed as "NON-VA" are Medications you do not get from a VA pharmacy that your provider recorded in your medical record. This includes medication prescribed by VA or non-VA providers, over the counter medications, herbals, samples or other medications you take.
The screenshot below shows an example of a new and improved ‘NON-VA’ medication. It now has any entered comments listed with the medication.
<!-- image -->
Software and Documentation Retrieval Instructions
Documentation describing the new functionality introduced by this patch is available.
The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.
Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Office:
Hines:  REDACTED
Salt Lake City: REDACTED
Documentation can also be found on the VA Software Documentation Library at:
http://www4.va.gov/vdl/
Patch Installation Instructions
    - Pre/Post Installation Overview
    - Pre-Installation Instructions
    - Installation Instructions
    - Backout/Rollback Strategy
    - Routine Information
Pre/Post Installation Overview
There are no special pre/post installation steps required.
Pre-Installation Instructions
This patch may be installed with users on the system although it is  recommended that it be installed during non-peak hours to minimize  potential disruption to users. This patch should take less than 5 minutes to install.
Installation Instructions
Perform the following steps to install this patch:
    1. Choose the PackMan message containing this patch.
    2. Choose the INSTALL/CHECK MESSAGE PackMan option.
    3. From the Kernel Installation and Distribution System Menu, select  the Installation Menu.  From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch # GMTS*2.7*120:
        1. Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
        2. Compare Transport Global to Current System - This option will (allow you to view all changes that will be made when this patch is installed. It compares all components of this patch routines, DDs, templates, etc.).
        3. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
            1. From the Installation Menu, select the Install Package(s) option and choose the patch to install.
            2. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//'
            3. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'
            4. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//'
            5. If prompted 'Delay Install (Minutes):  (0 - 60): 0//' respond 0.
        Post-Installation Instructions
        N/A
        Backout/Rollback Strategy
        In the event of a catastrophic failure, the Facility CIO may make the decision to back-out the patch. It is imperative that you have performed a backup of the routine included in this patch prior to installation.
        The back-out plan is to restore the routine from the backup created. No data was modified by this patch installation and, therefore, no rollback strategy is required. To verify the back-out completed successfully, ensure the checksum matches the pre-patch checksum from the patch descriptions.
        Routine Information
        The second line of each of these routines now looks like:
        ;;2.7;Health Summary;**[Patch List]**;Oct 20, 1995;Build 11
        The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.
        Routine Name:  GMTSPST2
        Before: B66514696   After: B97679179  **92,100,120**
        Routine list of preceding patches:  100
        Patch GMTS*2.7*111 – HEALTH SUMMARY UPDATE FOR ICD-10 PTF PROJECT
        Patch GMTS*2.7*111 updates the following Health Summary Components (#142.1) to include an expanded number of diagnosis codes (1 primary and up to 24 secondary diagnoses), operation/surgery codes (up to 25), and procedure codes (up to 25) that may be present in the Patient Treatment File (PTF):
            - MAS ADMISSIONS/DISCHARGES
            - MAS ADT HISTORY EXPANDED
            - MAS DISCHARGE DIAGNOSIS
            - MAS PROCEDURES ICD CODES
            - MAS SURGERIES ICD CODESAny of the following **locally created** items will also be affected by the newly updated display capability included in this patch **if** those items leverage any of the affected components to generate output:
            - Health Summary Types
            - Health Summary Objects
            - TIU/Health Summary Objects
            - OE/RR Reports
        Objects may be of particular interest as the newly expanded display would be more noticeable when an object is embedded in areas such as boilerplate text, note templates, and reminder dialog templates.
        Patch GMTS*2.7*111 also updates the following reports that utilize one or more of the aforementioned Health Summary Components and will therefore now display the expanded data fields as appropriate:
            - HEALTH SUMMARY (#142)
                - REMOTE DEMO/VISITS/PCE (1Y)
                - REMOTE DEMO/VISITS/PCE (3M)
                - REMOTE DIS SUM/SURG/PROD (12Y)**Note:** This patch enables the Health Summary reports to display the entire ICD code description.
            - OE/RR REPORT (#101.24)
                - ORRPW ADT ADM DC
                - ORRPW ADT DC DIAG
                - ORRPW ADT EXP
                - ORRPW ADT ICD PROC
                - ORRPW ADT ICD SURG
                - ORRPW DOD ADT EXP
        Patch GMTS*2.7*110 – Health Factor Component Header Change and Health Summary AdHoc report
        INC000000601000 - PCE HEALTH FACTOR COMPONET ISSUE
        Problem
        Health summary for health factor says "Visit Date" but is displaying either the event date or the visit date.
        Resolution
        Modify the program to have the column header read "Event/Visit Date" located at HDR+3^GMTSPXFP.
        Patch GMTS*2.7*101 - ICD-10 - Health Summary Updates
        This patch is part of the Computerized Patient Records System CPRSv30 project. This project will modify the Computerized Patient Record System, Text Integration Utilities, Consults, Health Summary, Problem List, Clinical Reminders, and Order Entry/Results Reporting to meet the requirements proposed by the Dept. of Health and Human Services
        to adopt ICD-10 code set standards Clinic Orders. This patch makes all changes to Health Summary that are required to move from the ICD-9 coding version to ICD-10.
        Health Summary reports will differentiate between ICD-9 and ICD-10 diagnosis and procedure codes for diagnosis information that was coded using the ICD-9 or ICD-10 code set (not entered via free text) in CPRS. ADHOC reports allow the user to choose the Health Summary Components to include in the report. These reports can also display diagnosis information that users entered via other CPRS packages.
        Health Summary Reports will print the ICD-9 or ICD-10 diagnosis or procedure diagnosis that was captured for the patient at the time the diagnosis was entered in CPRS and in the online report users entered via other CPRS packages.
        **Example: Display of Outpatient Diagnosis and Outpatient Encounter Components**
        **ICD-9 Example**
        <!-- image -->
        **ICD-10 Example**
        Patch GMTS*2.7*107 – BUG FIXES - iMED NOTE, IMPORT HS OBJECT, VITALS TEXT
        This patch will resolve the following issues in the Health Summary package.
            1. INC000000418117 - Imed Consent note shows as unsigned
            1. Problem
        The problem occurs when the user selects either Heath summary component "SPN" (Selected Progress notes) or "PN" (Progress notes). If the user selects a "scanned document," VistA will append the text "&lt;  THE ABOVE NOTE IS UNSIGNED  &gt;" and "* DRAFT COPY *" to the bottom of the report even though scanned documents do not require a signature and are not drafts.
            1. Resolution
        Stopped the text from being appended on scanned documents that have an administrative closure date.
        Routine GMTSPN2 has been modified to check the TIU Document File. If the "ADMINISTRATIVE CLOSURE MODE" (1613) field is set to 'S' FOR scanned document, and "ADMINISTRATIVE CLOSURE DATE" (1606) has a value, the note will be excluded from having the unwanted text appended.
            1. INC000000752225 - ADHOC HS Vital Signs Detailed Display issue
            1. Problem
        When pain value of 99 is entered in vitals, the ADHOC Health Summary components ([VS] "Vital Signs," [VSD] "Vital Signs Detailed Display," and [SVS] "Vital Signs Selected") show the text "No Response.” When you view the same info via the Vitals Cumulative report, it correctly shows the text as "Unable to Respond.” No response to pain and unable to respond are two clinically different things.
            1. Resolution
        Changed the components to display "Unable to Respond"
        Routines GMTSVS, GMTSVSD, and GMTSVSS have been modified to write "Unable to Respond." GMTSVS was also modified to move Pain score to a new third line. GMTSVSS was also modified to allot more space (18 characters) for Pain score.
            1. INC000000784073 - Importing HS Object Questions
            1. Problem
        When using the [GMTS OBJ EXPORT] option in VistA, if one of the components used in the Health Summary type is a local component or has selected Items, the process completes with no error reported. However, when the receiving CAC  tries to use the imported object, it fails to work. If VistA identifies the component as a local component or one that has selected Items, it simply omits the component without any type of error or warning.
            1. Resolution
        Modified VistA to return an error message and abort the export if the CAC tries to export a Health Summary Object that is associated with a Health Summary Type with a local component or selected items component. The following error messages were approved by the CPRS Clinical Workgroup.
            - "Cannot export a Health Summary Object using a Health Summary Type that contains Local Health Summary Components"
            - "Health Summary Type &lt;TYPE&gt; contains Local Health Summary Component &lt;COMPONENT&gt;"
        Patch GMTS*2.7*104 – MHTC &amp; CAT 1 PRF UPDATE TO HIGH RISK MH PATIENT HEALTH SUMMARY REPORT
        This patch is in support of Phase II of the Improve Veteran Mental Health (IVMH) initiative, High Risk Mental Health Patient (HRMHP) - National Reminder &amp; Flag project.
        This patch will modify two entries in the Health Summary Component file (142.1): MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.
        These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH HIGH RISK PATIENT Health Summaries as well as being available for use in the Health Summary Adhoc Report. Additionally, the VA-MH HIGH RISK PATIENT Health Summary is also embedded in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog released in Phase I of this project.
        The MH HIGH RISK PRF HX component will now include the assignment history for the newly created Category I Patient Record Flag (HIGH RISK FOR SUICIDE). The assignment history in Health Summary will display both Category II (local) and Category I (national) assignments for High Risk for Suicide until all local entries have been converted to the national flag.
        The MH TREATMENT COORDINATOR component will now be fully functional and display the mental health treatment team, mental health treatment coordinator (MHTC), and the MHTC contact information.
        Sample output from the updated components:
        -------------------- MHRF - MH Suicide PRF Hx ----------------
        CATEGORY I (NATIONAL) PRF: HIGH RISK FOR SUICIDE
        Date Assigned: Jan 18, 2012@08:49:28
        Next Review Date: APR 17, 2012
        Assignment History:
        Date: JAN 18, 2012@08:49:28
        Action: NEW ASSIGNMENT
        Approved By: CPRSPROVIDER,TWENTY-SIX
        CATEGORY II (LOCAL) PRF: HIGH RISK FOR SUICIDE
        Date Assigned: Dec 08, 2011@09:28:23
        Next Review Date:
        Assignment History:
        Date: DEC 08, 2011@09:28:23
        Action: NEW ASSIGNMENT
        Approved By: CPRSPROVIDER,TWENTY-SIX
        Date: JAN 12, 2012@15:46:32
        Action: INACTIVATE
        Approved By: CPRSPROVIDER,TWENTY-SIX
        -------------------- MHTC - MH Treatment Coor -------------------
        MH Treatment Team:  HRMH TEST TEAM
        MH Treatment Coordinator:  MHPROVIDER,TWENTY-SEVEN
        Office Phone:  555-123-4567
        Analog Pager:  12345
        Digital Pager:  98765
        **CPRS Example**
        <!-- image -->
        Patch GMTS*2.7*105 – SUBSCRIPT, SPELLING, &amp; DISPLAY ERRORS
        This patch resolves the following issues in the Health summary package.
            - A subscript error occurs when editing an AD HOC report.
            - The descriptions of the "MHA Administration List" &amp; "MHA Score" health summary components contain spelling errors.
            - CPRS is not displaying the correct name for nationally released health summary reports
        Patch GMTS*2.7*102 – MENTAL HEALTH CLEANUP
        The Mental Health package version 5.01 patch 60 (YS*5.01*60) removes functionality from the Mental Health package that is no longer in use.
        Specifically, patch YS*5.01*60 removes the MEDICAL RECORD file (file #90), which the MENTAL HEALTH PHYSICAL EXAM health summary component relies upon. Patch GMTS*2.7*102 will accomplish the following.
        Deactivate the MENTAL HEALTH PHYSICAL EXAM health summary component.
        Rebuild the Health Summary Adhoc Report (the GMTS HS ADHOC OPTION health summary type).
        Email a usage report containing the following listings.
        Health summary types that contain the MENTAL HEALTH PHYSICAL EXAM health summary component
        Health summary objects that contain the health summary types listed in (a)
        Patch GMTS*2.7*100 -PROBLEM WITH NEW MED WORKSHEET REPORT
        The Medication Worksheet report in CPRS displays a patient’s previous prescription Patient Instruction Signature comments in subsequent prescriptions, displaying incorrect Patient Instruction Signature comments for that prescription.
        Routine GMTSPST2 has been modified to clear a prescription's signature lines before displaying a subsequent prescription.
        Patch GMTS*2.7*95 – CORRECT B CROSS-REFERENCE
        The NAME field (.01) of the HEALTH SUMMARY OBJECTS file (#142.5) had a 'B' cross-reference that only stored the first 30 characters of the name. When attempting to install a TIU/HS Object in Clinical Reminder Exchange, a FileMan error: "The update failed, UPDATE^DIE returned the following error message" would occur when the receiving site has multiple Health Summary Object entries that are not unique until after the 30 character length.
        This patch corrects this problem by modifying the 'B' cross-reference to store the full 60 characters.
        Patch GMTS*2.7*93 - COMBINE UNITS ON TRANSFUSION REPORT
        This patch fixes a problem with the Blood Transfusion Report when using the report on a system running VBECS (Vista Blood Establishment Computer Software). The problem reported is that multiple units transfused on the same day were not being totaled but were rather displayed as separate lines for each transfused unit.
        This patch corrects the problem by correctly totaling the units the way it did prior to VBECS.
        This patch also adds Legacy Vista Data to the Blood Transfusion report. Prior to this change only transfusion data newly entered into VBECS were showing in the report. To see Legacy Vista Data, on the report, the parameter OR VBECS LEGACY REPORT has to be set to YES.
        GMTS*2.7*92 - CORRECTIONS TO MEDICATION WORKSHEET (TOOL #2)
        This patch will correct a defect in the HEALTH SUMMARY COMPONENT file (#142.1) and creates a national entry for Tool #2: Medication Worksheet. Hard-coding of patient Social Security number has been removed and now all control of patient identifiers are controlled by the parameters set at the Health Summary Type level, consistent with other Class I software.
        This patch also resolves the issue of the wrong pharmacy division printing on report headers by modifying internal programming. The internal programming that selects the name of the pharmacy division shown at the top of the worksheet and the pharmacy phone number associated with it has been revised. At facilities where there are multiple entries in OUTPATIENT SITE file (#59) that share the same SITE NUMBER, the Medication Worksheet is unable to distinguish between these entries in order to choose the correct pharmacy name and phone number for display in the report header. In these cases, the result may be that the displayed name and phone number are for a division other than the pharmacy’s preferred phone number for patient calls.
        It also corrects a known issue from the initial release of Medication Reconciliation by adding status of HOLD to the Medication Worksheet.
        GMTS*2.7*91 - MHAL AND MHAS COMPONENTS NOT SHOWING ALL ADMININISTRATIONS
        This patch corrects a defect in the MHAL and MHAS Health Summary components where all Mental Health instruments administered through the CPRS GUI do not display.
        Patch GMTS*2.7*90 - ADD EARLIEST APPROPRIATE DATE TO HS ADHOC REPORT
        Addition of the EARLIEST APPROPRIATE DATE (New Service Request 20051008) to the Health Summary Adhoc CNB - Brief Consults Report.
        The EARLIEST APPROPRIATE DATE is the earliest appropriate date that the patient should be seen. This data field was added with CPRS v28.
        Patch GMTS*2.7*88 - LAB REFORMAT/142.1 UPDATE/SII COMP/HS BY LOC REPORT
        Display column headers of TIU-Health Summary (HS) Object components when pulled up in succession.
        Update Lab references range displays on HS reports to coincide with format introduced by LR*5.2*356 .
        Update default value of fields TIME LIMITS and MAXIMUM OCCURRENCES for HS components MHA Admin List [MHAL] and MHA Score [MHAS] HS components.
        Add new field, SHORT HS BY LOCATION COVER to the HEALTH SUMMARY
        PARAMETERS FILE (#142.99) to change the number of times each location prints on the cover sheet from 6 to 1.
        Patch GMTS*2.7*85 - Restrict Sensitive Data On Health Summary Print
        This patch implements an urgent request from the CPRS Clinical Workgroup.
        Patients are often given printed Health Summaries for items such as a formatted list of medications. Because these items are Health Summaries, they also contain a standard header which displays the patient’s name, DOB and full 9-digit SSN.
        Patients, not recognizing that such sensitive information is present, may improperly dispose of the list. To help protect this sensitive information, this patch adds a new field (SUPPRESS SENSITIVE PRINT DATA) to the HEALTH SUMMARY TYPE file (#142) to allow control over the level of information displayed on a hard copy print of a predefined health summary type.
        Depending on the value found in the new field, the SSN/DOB information will be in one of the following formats.
            - Full 9-digit SSN and full DOB
            - 4- digit SSN and No DOB
            - No SSN and No DOB
        **Affected functionality**
        Predefined health summary type printouts produced from CPRS GUI, List Manager, and print menus within the Health Summary package.
        **Table of interface used, action taken, and expected output**
        | **Action**            | **Interface**      | **Output**                  |
|-----------------------|--------------------|-----------------------------|
| View report on screen | CPRS GUI           | Full SSN/DOB info           |
|                       | GMTS print options | Full SSN/DOB info           |
|                       | List Manager       | SSN/DOB based on flag value |
| Hard copy print       | CPRS GUI           | SSN/DOB based on flag value |
|                       | GMTS print options | SSN/DOB based on flag value |
|                       | List Manager       | SSN/DOB based on flag value |
        Additionally, the display of a health summary object will be affected by this patch. Information displayed from a health summary object is controlled by the choices made during object creation/modification and the underlying health summary type. Unless otherwise suppressed during object creation/modification, health summary objects will respect the value of SUPPRESS SENSITIVE PRINT DATA found for each object's health summary type. This applies to viewing objects in electronic AND hard copy format.
        Usage note regarding List Manager.
        The patient information header in List Manager is separate from the header found on health summary reports. Any changes to the patient information header are outside the scope of this patch. As a result, any hard copy print of a predefined health summary via the List Manager interface will still have viewable patient SSN and DOB data.
        Note - In an effort to address the urgency of this effort, Ad Hoc health summaries were excluded from this request.
        Patch GMTS*2.7*83 - DIETETICS COMPONENT UPDATE
        This patch makes use of new fields made available by the Nutrition and Food Service Package for use in the DIETETICS Health Summary Component. The fields that are added to the component display are:
        FOLLOW UP DATE
        PATIENT FOOD ALLERGY
        COMMENTS
        Patch GMTS*2.7*81 - VHA Enterprise Standard Title Display in Health Summary Components
        This patch exports changes to the displays for the Progress Notes (PN), Selected Progress Notes (SPN), and Discharge Summary (DCS) components. Both the Local TIU Title and VHA Enterprise Standard Title will be displayed in these components, with captions of Local Title and Standard Title.
        This patch accompanies TIU*1*211, which includes a mapping utility to assist CACs with the process of mapping local document titles to VHA Enterprise standard titles, in preparation for the upcoming unified Clinical Data Repository/Health Data Repository of computable patient data.
        Changes to the Selected Progress Notes (SPN) and Discharge Summary (DCS) components are not included in this patch, as these components use the same print routines that are contained in the Progress Notes (PN) component.**Example** : The highlighted section shows the Local Title and Standard Title.
        05/30/2006 16:12
        ********************  CONFIDENTIAL AD HOC SUMMARY   pg. 1 *********************
        HSPATIENT,ONE    666-12-9900     HOSPICE 178-1                  DOB: 12/31/1898
        ------------- PN - Progress Notes (max 10 occurrences or 1 year) -------------
        05/30/2006 16:08  Local Title: OUTPATIENT DISCHARGE INSTRUCTIONS
        Standard Title: RN EMERGENCY DEPARTMENT DISCHARGE NOTE
        **CPRS GUI Display**
        TWO HSPROVIDER

HSPROVIDER,TWO
        <!-- image -->
        GMTS*2.7*80 – PHARMACY ENCAPSULATION
        The changes in this patch are related to the Pharmacy Encapsulation effort.
        With this effort, all direct reads on Pharmacy Package files must be changed to API calls.
        HEALTH SUMMARY COMPONENTS affected
        RXOP - PHARMACY OUTPATIENT
        GMTS*2.7*79   CORRECT REFERENCE RANGES ON REPORT TABS
        Health summary was modified to use a new Lab API to collect the correct data for
        test results from the Lab package.
        GMTS*2.7*78   NEW VITALS API AND OUTPATIENT PHARMACY API
        This patch added a new Vitals API call to several Vital Signs Health Summary Components and corrects a couple of these components to display data as intended.
        GMTS*2.7*77 – MENTAL HEALTH COMPONENTS
        The purpose of this patch is to send out two new Health Summary Components
        related to the Mental Health Package:
        MHAL - MHA Administration List
        MHAS - MHA Score
        This patch accompanies Clinical Reminders patch PXRM*2*6, which updates reminder definitions and dialogs to be compatible with Mental Health patch YS*4*85, also known as MHA3, in support of new national performance measures.
        GMTS*2.7*76   ALPHA MODIFIERS NOT SHOWING AND COMMENTS PRINTING TWICE
        This patch addressed 2 issues.
        1) The issue of the CPT/Procedure code non-numeric modifiers not displaying on Health Summary Reports.
        2) The double printing of the comments for Health Summary Report.
        GMTS*2.7*75   RESTORE DISPLAY OF CLINICAL REMINDERS DISCLAIMER
        This patch in conjunction with patch PXRM*2*4 restored the display of the Clinical Reminders disclaimer for the Clinical Reminders Maintenance, Brief, and Due Health Summary components.
        GMTS*2.7*74   HEALTH SUMMARY GAF COMPONENT
        This patch updates the routine which is invoked for the AD HOC HEALTH SUMMARY component, the Global Access Function to report GAF scores graphically, so that a report generated on the last day of the month will produce a valid listing rather than showing "No data available.”
        GMTS*2.7*73   CORRECT BRANCH OF SERVICE IN DEMOGRAPHIC DISPLAY
        This patch corrects the display of the Branch of Service line in the Health Summary display of the Patient Demographics.
        GMTS*2.7*72   ONCOLOGY FORDS IMPLEMENTATION
        Routines were added/modified to update the Oncology Health Summary to reflect changes to the FORDS (Facility Oncology Registry Data Standards) and to add AJCC (American Joint Committee on Cancer) Collaborative Staging.
        GMTS*2.7*71   CTD - HS Code Text Descriptors
        This patch is part of the Code Text Descriptors (CTD) Project. It modified selected data extract routines to take advantage of the Text Versioning APIs exported by ICPT/HCPCS and the DRG Grouper packages.
        GMTS*2.7*70   GMTS SCHEDULING REPLACEMENT UPDATE
        This patch converted Health Summary code to use the APIs provided by the Scheduling Replacement team. Any Health Summary code that made direct reads to Scheduling globals has been replaced by APIs that are backed by Integration Agreements.
        A new Health Summary Parameter has been added. The new parameter is ERROR MESSAGE RECIPIENT. The purpose of this parameter is to let the Health Summary Package know who to send a mail message to when a queued option fails. With this patch, queued tasks could be aborted due to failed calls to the Scheduling package. If this parameter is not set, then no mail message will be sent.
        GMTS*2.7*69   Health Summary Resequencing/Medicine Correction
        This patch addresses the following three (3) issues in the Health Summary Application.
        1) Resequencing of a Health Summary Component's Selection Items was introduced in patch GMTS*2.7*62. An error has been reported as occurring during the resequencing process. This error occurs when the Component has Selection Items that gather data from certain types of global roots. This patch corrects the resequencing so that it now works with these type of global roots.
        2) Since patch GMTS*2.7*62, Medicine Health Summary Components were not displaying results for any patients regardless of Procedure data being available or not. This patch corrects the Medicine HS Components so that they now display results properly.
        3) The Selected Health Factors Component was not displaying the Health Factors in the sequence set up in the Health Summary Component. Instead the Health Factors were grouped by Category and then displayed alphabetically by the Category. This patch corrects the display so that the Selected Health Factors are displayed in the sequence set up in the Component.
        GMTS*2.7*67   NOT USED
        GMTS*2.7*66   CPRS HS REPORT ALLOCATION ERRORS
        This patch updated the API's in Health Summary, used by CPRS to get the list of possible Health Summary reports available on the Reports Tab The API's have been changed to use ^TMP globals instead of local arrays to reduce the possibility of allocation errors.
        GMTS*2.7*68   TRANSITIONAL PHARMACY HS OBJECT/TYPE
        This patch contains a new Health Summary Object and Type for use with the Transitional Pharmacy Benefit Program.
        GMTS*2.7*65   Non VA Medications
        This patch adds a new Health Summary Component to display a patient's Non VA medications documented by health care facilities as required by the Joint Commission for Accreditation.
        GMTS*2.7*64   TWEAK TO STANDARD REMOTE HEALTH SUMMARIES
        This patch addresses a problem reported by several sites when trying to access remote data using the Health Summary Remote Reports on the CPRS Reports Tab. Some of the Remote Reports on some patients contain more data than can be returned within the timeout period set by the remote broker, which can range from 10-20 minutes. Users become impatient and either CTRL-ALT-DEL out of CPRS or continually click on the report, causing more remote processes to begin, which further exacerbates the problem. The network and the remote site becomes inundated with remote queries that does nothing but clog the system.
        We have determined that any report that contains Progress Notes has the potential to create this problem. This patch is being released to add an occurrence limit of 50 to the Progress Notes Health Summary component for the following reports.
        REMOTE CLINICAL DATA (1Y)
        REMOTE CLINICAL DATA (3M)
        REMOTE CLINICAL DATA (4Y)
        REMOTE TEXT REPORTS (1Y)
        REMOTE TEXT REPORTS (3M)
        We have done some testing at some of the sites reporting this problem and found that setting this limit higher than 50 tends to overload the system. Users should be instructed to use the Progress Notes option(s) under Clinical Reports when there is a need to get more than 50 Notes. Progress Notes under Clinical Reports has greater flexibility to return data within user specified time ranges and occurrence limits.
        GMTS*2.7*63   Selection of Individual Health Factors
        This patch will release two new National Health Summary Components required by the VA Geriatric Extended Care (GEC) Referral project.
        GECC - GEC Completed Referral Count
        GECH - GEC Health Factor Category
        The GEC Completed Referral Count component will display the total number of completed GEC referrals done on a patient. Each completed referral will show the date the referral was started, the date the referral was completed and the associated Health Factors. The GEC Health Factor Category component is identical to the current Selected Health Factor component except for the selection items. This component will only display a list of Health Factors that are associated with the GEC project.
        For more documentation on VA Geriatric Extended Care project please see the Clinical Reminders 2.0 Setup guide and the User Manual found under the Clinical Reminders section of the VistA Documentation Library (http://www.va.gov/vdl).
        This patch also supports Clinical Reminders changes for MyHealtheVet
        To support MyHealtheVet we are releasing two new Components.
        MHV REMINDERS DETAIL DISPLAY
        MHV REMINDERS DETAIL DISPLAY
        And two new Remote Data Views.
        REMOTE MHV REMINDERS DETAIL
        REMOTE MHV REMINDERS SUMMARY
        These components will now search through file 811.9 and evaluate any Clinical Reminder definition that is defined for patient use and display the results of the evaluation in Health Summary. These four new components are stored in file #142.1 and the two new Remote Data Views are stored in file #142.
        E3R #17227, CONFIGURE INDIV HF WITH 'SHF' COMPONENT
        Also included in this patch is a change to the Selected Health Factor component by allowing the user to select either a Health Factor Category or an individual Health Factor. The Selected Health Factor component will display "(category) or (factor)" after the name of the item. For the output data to be correct, patch PX*1.0*123 must be installed.
        Misc. Fixes
        This patch fixes a problem discovered while testing TIU*1.0*135. Currently, if you have a TIU HS object that displays data from a Health Summary type with no assigned components, you will receive an error in CPRS. This patch fixes this problem by displaying "No Health Summary Components" in the TIU HS Object display text.
        GMTS*2.7*62   MED/RXIV/HF/Miscellaneous
        Various fixes to printing errors.
        Modified column header in Health Factors component from "Date" to "Visit Date" to reduce ambiguity. Removed a blank line that is printed in Health Summary Objects when no data was available for the component used in the object.
        Added the ability to resequence/re-order 'Selection Items' (such as lab test) during Health Summary Type edit session.
        Fixed Relationship in Next of Kin component. (Routine GMTSDEM2)
        Removed text code which references test software in Routine GMTSXAR.
        GMTS*2.7*61   Remote Medicine Report Fix
        This patch is part of a coordinated two patch fix for a problem reported on Remote Data Views of Medicine Health Summary Components. Prior to this patch, the Medicine Health Summary components used Mailman to process the reports. Mailman required that the users have an Access and Verify code at the "remote" site. Since the user did not have Access and Verify codes on the remote system, the component would fail to return
        data from the remote site. This fix requires both this patch and a companion patch from the Medicine package, MC*2.3*36
        GMTS*2.7*60   Race and Ethnicity (Demographics)
        This patch added the patient's race and ethnicity data to both the MAS DEMOGRAPHIC and MAS DEMOGRAPHICS BRIEF components using either the existing (old) RACE field (.06) or the new field’s RACE INFORMATION (field #2) and ETHNICITY INFORMATION (field #6) added to the patient file (#2) with patch DG*5.3*415.
        GMTS*2.7*59   BLOOD BANK COMPONENTS
        This patch modifies the Blood Bank Health Summary Components "Blood Transfusion" and "Blood Availability" in support of the Blood Bank Modernization Project. Health Summary code found in routines GMTSLRT and GMTSLRB has been modified to call the new Blood Bank APIs to extract Transfusion and Availability data. Health Summary users will not see any change in how the Blood Bank components display.
        Patch GMTS*2.7*58   HS Objects and CNB/ADR/NOK/SII Components
        A menu of options was added, “Health Summary Objects Menu” that allows IRM/Managers to create Health Summary Objects to be used inside other documents. This menu also includes the ability to view, test, and export/import the Health Summary Objects. This patch also exports the new file HEALTH SUMMARY OBJECTS field #142.5, to store the Health Summary Object characteristics, and exports entry points for other applications to embed the HS objects into other text and/or documents. Also, blank lines between column headers and component data have been suppressed. E3R 17305
        Several other fixes are included, in response to NOISes CON-0902-10901, FAV-0902-70871, LAH-1102-61005, HWH-1002-40090, PUG-0702-51903, BUT-0702-23160, WPB-0202-31624 , CPH-0302-40541, BUT-0701-20825, and E3R 17409.
        Patch GMTS*2.7*56   DIVISION PARAMETER/DEMOGRAPHICS AND OTHER FIXES
        Changed the logic for setting up parameters for Multi-Division sites using DUZ(2).
        Removed the display of the global array from the MEDB - MEDICINE BRIEF component.
        Fixed a QUIT WITHOUT VALUE error in routine GMTSXAW3.
        Fixed an infinite loop which occurs when formatting a user's name for Lab components when the user has a numeric first name. NOIS POR-0602-50811
        Added a line feed after the Treating Facilities' in the Brief Demographic component so the "Source of Information" statement which is given with remote data views statement is not pushed off the screen. NOIS SHE-0502-53189, BUT-0702-21121 and HUN-0702-20308
        Added Health Insurance information to the Demographics component. E3R 4756
        Modified the printing of report and component headers so that calling applications can better control the suppression of headers. E3R 17305 (partial)
        Patch GMTS*2.7*55  Demographics/Progress Note Fixes
        This patch fixed the occurrence limit problem with the Progress Notes components. If no limit was set, the report would default to 10 occurrences. After installing this patch, removing the occurrence will result in the report printing all progress notes for the patient within the time limit. NOIS CPH-0302-41402, MIN-0302-42259, ALB-0302-50476, COA-0302-22983 and DUB-0402-32340.
        Fixed a problem of the Treating Facilities not appearing in the Demographic components of the Health Summary when the patient did not have a PCMM Team, PCMM provider, PCMM associate provider or an inpatient attending physician. After installing this patch, Treating Facilities should display (when available) regardless of provider assignments. NOIS AUG-0302-32435
        Fixed a problem with multiple patient selection left over from OERR 2.5. This only affected users who still have OERR 2.5 preferences set in the New Person file. NOIS HUN-0202-22784
        The prompt for Hospital Location in the option GMTS HS BY LOC (Hospital Location Health Summary) has been fixed so that it will accept a partial text entry. NOIS CPH-0302-42497, DUB-0302-32599 and NOP-0302-12911
        Patch GMTS*2.7*54  Oncology ICD-O-3 Implementation
        This patch modifies the Oncology Health Summary display to include Histology and implements ICD-O-3, International Classification of Diseases for Oncology, third edition.
        Patch GMTS*2.7*52 Problem List HNC/MST Changes
        This patch is in response to the Veterans Millennium Health Care and Benefits Act, Copayment Exemptions. It requires Health Summary Problem List Component to display Head and Neck Cancer for veterans diagnosed with cancer of the head and/or neck related to nose and throat radium treatment and to display MST for veterans diagnosed with military sexual trauma.
        Patch GMTS*2.7*49  Demographics/HS Types List
        A menu of options has been added, “CPRS Health Summary Display/Edit Site Defaults,” that allows IRM/Managers to control which Health Summary Types are on the reports tab and the order that the Health Summary Types appear in for the site. These site defaults will be used for users who do not have personal preferences set. This menu has four menu items to edit and display defaults for the site.
        This patch also contains several fixes to problems reported by NOIS or E3Rs. The following is a list of the problems fixed by this patch.
            - The Outpatient Encounters (OE) component has been modified to display the correct CPT Modifier.
            - PCMM information and Treating Facilities has been added to Demographics and Brief Demographics components
            - Modified Date Range processing for the Imaging Profile component to prevent missing imaging reports for the date of the beginning date of the date range.
            - Modified the method of building the list of Health Summary Types for the Reports Tab so that division and user parameters are not over-written by the system parameters.
            - Modified the GMTS TYPE INQ P  E34  16528rint Template to allow for 132 column output, preventing the truncation of selection items in the display.
            - Several routines were found to be inappropriately setting the package-wide variable GMTSNDM (Occurrence Limits), causing components that followed to error on occurrence limits. This was discovered while researching CPH-1001-43354 (Adhoc GAF Score Not Displaying Data).
            - Modified 'Hospital Location Health Summary' so that the check for patients at a hospital location is conducted at the time the queued task is run instead of when the option is invoked.
            - Modified 'Outpatient Encounter' component so that the hospital location in the Outpatient Encounter in the Clinical Reports on the Reports Tab matches the Hospital Location in the Health Summary Ad Hoc.
            - Modified Medicine Health Summary components so that the message text is removed from the S.MCHL7SERVER server basket.
            - Modified Discharge Summary print routines so package-wide variables (beginning date and ending date) do not get reset preventing other components from printing.
            - Post-Init correctly renames Radiology components in the VAQ - DATA SEGMENT file (#394.71).
            - Modified GAF component to allow multiple providers to enter varying GAF scores on the same visit date/time.
            - Pre-Init removes test versions of GUI Site Default options.
            - As part of an on-going project to document all of the entry points and DBIAs in Health Summary, the following routines are being re-issued with minor documentation changes.
        GMTS      GMTS1     GMTSADH2  GMTSADH3  GMTSADH5
        GMTSALG   GMTSALGB  GMTSCI    GMTSCM    GMTSDCB
        GMTSDD    GMTSDGA   GMTSDGA1  GMTSDGA2  GMTSDGC2
        GMTSDGD   GMTSDGH   GMTSDGP   GMTSDVR   GMTSLOAD
        GMTSLREM  GMTSLRMX
        Patch GMTS*2.7*48 REMOTE ONCOLOGY VIEW
        Health Summary patches 29 and 48 export components for using Remote Data Views. With all the proper patches installed, you may view remote patient data through CPRS. Before you can do this, you must have Master Patient Index/Patient Demographics (MPI/PD) and several other patches installed. Once these are in place and the proper parameters have been set, you can access remote data from other VA facilities.
        Currently, remote data views are limited to predefined, nationally exported Health Summary Types. Remote data may not be viewed by either the Ad Hoc Health Summary type or locally/user developed Health Summary types.
        You can view remote clinical data using any Health Summary Type that has an identically named Health Summary Type installed at both the local and remote sites. However, for non-nationally exported health summary reports, the content of the report is subject to the report structure and configuration defined at the remote site.
        Patch 29 (GMTS*2.7*29) added the following Remote Data Views types.
        REMOTE DEMO/VISITS/PCE (3M)
        REMOTE MEDS/LABS/ORDERS (3M)
        REMOTE TEXT REPORTS (3M)
        REMOTE CLINICAL DATA (3M)
        REMOTE CLINICAL DATA (1Y)
        REMOTE DEMO/VISITS/PCE (1Y)
        REMOTE MEDS/LABS/ORDERS (1Y)
        REMOTE TEXT REPORTS (1Y)
        REMOTE CLINICAL DATA (4Y)
        REMOTE LABS LONG VIEW (12Y)
        REMOTE LABS ALL (1Y)
        REMOTE LABS ALL (3M)
        REMOTE DIS SUM/SURG/PROD (12Y)
        REMOTE OUTPATIENT MEDS (6M)
        REMOTE ONCOLOGY VIEW
        See Chapter 3, section 2 for more information on using Remote Data Views.
        Patch GMTS*2.7*47  CPRS Report Tab/NDBI/Misc Fixes
        A menu of options has been added, CPRS Reports Tab “Health Summary Types List,” that allows users to control the Health Summary Types and the order that the Health Summary Types are listed in the Health Summary Types box on the Reports Tab of CPRS. This menu option has four menu items to edit and display the users’ preferences.
        GMTS*2.7*45  Interdisciplinary Progress Notes
        The purpose of this patch is to allow the Health Summary components Progress Notes and Selected Progress Notes to display the new interdisciplinary progress notes and all of the entries associated with the interdisciplinary note. The interdisciplinary note and all of the associated entries will be marked in the progress note components as follows.
        **Note Type              	Marked as**
        Primary Note:          	Interdisciplinary Note
        Addendum to Primary   	Interdisciplinary Note (addendum)
        Child Note             	Interdisciplinary Note Entry
        Addendum to Child     	Interdisciplinary Note Entry (addendum)

### Released Patches for Health Summary 2.7

- GMTS*2.7*1	Syntax Error in GMTS
- GMTS*2.7*2	Visit Dates, Task &amp;
- GMTS*2.7*3	LAB Anatomic Path Ac
- GMTS*2.7*4	Medicine Data w/ Quo
- GMTS*2.7*5	CVP, EADT, Nightly T
- GMTS*2.7*6	Patient Selection
- GMTS*2.7*7	HS Utilities, MXSTR
- GMTS*2.7*8	HS - PCE Components
- GMTS*2.7*9	Lab Orders/Surgical
- GMTS*2.7*10	PCE Components
- GMTS*2.7*11	SURGERY COMPONENT FI
- GMTS*2.7*12	TIU-COMPATIBLE COMPO
- GMTS*2.7*13	Spinal Cord Dysfunct
- GMTS*2.7*14	Updated Rad/Nuc Med
- GMTS*2.7*15	Pharmacy &amp; Current O
- GMTS*2.7*16	Health Summary Fixes
- GMTS*2.7*17	Blood Bank Component
- GMTS*2.7*18	Code change to accom
- GMTS*2.7*19	Duplicates on CVP co
- GMTS*2.7*20	UPDATED COMPONENTS f
- GMTS*2.7*21	Report headings and
- GMTS*2.7*22	Reminders-historical
- GMTS*2.7*23	NEW REMINDER COMPONE
- GMTS*2.7*24	Patient selection &amp;
- GMTS*2.7*25	Component fixes
- GMTS*2.7*26	Imaging Component
- GMTS*2.7*27	Y2K COMPLIANCE CHANG
- GMTS*2.7*28	Y2K, NKA, LAB, VITAL
- GMTS*2.7*29	Remote Data View/Pri
- GMTS*2.7*30	HS Type Lookup/Concu
- GMTS*2.7*31	Inactive Clinics
- GMTS*2.7*32	Fix HS Type Lookup
- GMTS*2.7*33	Progress Notes by Vi
- GMTS*2.7*34	Clinical Reminder Di
- GMTS*2.7*35	Vitals/GAF/Oncology/
- GMTS*2.7*36	Oncology/Lab/Ad Hoc
- GMTS*2.7*37	CPT Modifiers and RX
- GMTS*2.7*40	Undefined Variable D
- GMTS*2.7*42	Oncology Component C
- GMTS*2.7*43	HFS/Window Print Fix
- GMTS*2.7*44	Error in GAF Score
- GMTS*2.7*45	Interdisciplinary Pr
- GMTS*2.7*46	Consults Brief Compo
- GMTS*2.7*47	CPRS Report Tab/NDBI
- GMTS*2.7*48	Remote Oncology View
- GMTS*2.7*50	Spinal Cord Dysfunct
- GMTS*2.7*49 	Demographics/HS Type
- GMTS*2.7*51	Radiology fixes
- GMTS*2.7*54	Oncology ICD-O-3 Impleme
- GMTS*2.7*55	Demographics/Progress No
- GMTS*2.7*52	Problem List HNC/MST Cha
- GMTS*2.7*56	Division Parameter/Demog
- GMTS*2.7*58	HS Objects and Components
- GMTS*2.7*59	BLOOD BANK COMPONENTS
- GMTS*2.7*60	Race and Ethnicity (Demographics)
- GMTS*2.7*61	Remote Medicine Report Fix
- GMTS*2.7*62	MED/RXIV/HF/Miscellaneous
- GMTS*2.7*63	Selection of Individual Health Factors
- GMTS*2.7*64	TWEAK TO STANDARD REMOTE HEALTH SUMMARIES
- GMTS*2.7*65	Non VA Medications
- GMTS*2.7*66	CPRS HS REPORT ALLOCATION ERRORS
- GMTS*2.7*67	NOT USED
- GMTS*2.7*68	TRANSITIONAL PHARMACY HS OBJECT/TYPE
- GMTS*2.7*69	Health Summary Resequencing/Medicine Correction
- GMTS*2.7*70	GMTS SCHEDULING REPLACEMENT UPDATE
- GMTS*2.7*71	CTD - HS Code Text Descriptors
- GMTS*2.7*72	ONCOLOGY FORDS IMPLEMENTATION
- GMTS*2.7*73	CORRECT BRANCH OF SERVICE IN DEMOGRAPHIC DISPLA
- GMTS*2.7*74	HEALTH SUMMARY GAF COMPONENT
- GMTS*2.7*75	RESTORE DISPLAY OF CLINICAL REMINDERS DISCLAIMER
- GMTS*2.7*76	ALPHA MODIFIERS NOT SHOWING AND COMMENTS PRINTING
- GMTS*2.7*78	NEW VITALS API AND OUTPATIENT PHARMACY API
- GMTS*2.7*79	CORRECT REFERENCE RANGES ON REPORT TABS
- GMTS*2.7*81	VHA Enterprise Standard Title Display in Health Summary Components
- GMTS*2.7*82	E-SIG BLOCK/HEALTH FACTORS/CLINICAL REMINDERS F
- GMTS*2.7*83	DIETETICS COMPONENT UPDATE
- GMTS*2.7*84	ADDING REASON FOR STUDY DISPLAY TO RADIOLOGY RE
- GMTS*2.7*85	RESTRICT SENSITIVE DATA ON HEALTH SUMMARY PRINT
- GMTS*2.7*87	NATIONAL HEALTH SUMMARY TYPES FOR SKIN RISK ASSESSMENT
- GMTS*2.7*88	LAB REFORMAT/142.1 UPDATE/SII COMP/HS BY LOC REPORT
- GMTS*2.7*89	SUPPORT OF CLINICAL REMINDERS ENHANCEMENTS
- GMTS*2.7*91	MHAL AND MHAS COMPONENTS NOT SHOWING ALL ADMINISTRATIONS
- GMTS*2.7*92	CORRECTIONS TO MEDICATION RECONCILIATION WORKSHEET (TOOL #2)
- GMTS*2.7*93	COMBINE UNITS ON TRANSFUSION REPORT
- GMTS*2.7*94	UPDATES FOR THE ESSENTIAL MED LIST FOR REVIEW
- GMTS*2.7*95	CORRECT B CROSS-REFERENCE
- GMTS*2.7*107	BUG FIXES - iMED NOTE, IMPORT HS OBJECT, VITALS TEXT
- GMTS*2.7*110	HEALTH FACTOR COMPONENT HEADER CHANGE AND ADHOC REPORT
- GMTS*2.7*111 HEALTH SUMMARY UPDATE FOR ICD-10 PTF PROJECT
- GMTS*2.7*125 HEALTH SUMMARY UPDATE FOR 2 NEW COMPONENTS

### Packages providing data to Health Summary

Automated Med Info Exchange (AMIE)

Adverse Reaction Tracking (ART)

Blood Bank

Clinical Reminders

Clinical Procedures

Consults

Dietetics

Discharge Summary

GEC

Inpatient Medications

Laboratory

Medicine

Mental Health

My Health *e* Vet

Nursing (Vital Signs)

OE/RR

Oncology

Outpatient Pharmacy

Patient Care Encounter (PCE)

Problem List

Progress Notes

Radiology

Registration

Scheduling

Surgery

VistA Imaging

Vitals

Health Summary users can also print an Outpatient Pharmacy Action Profile with bar codes in tandem with a health summary. For complete details on printing a patient’s profile, read the section that describes the “Hospital Location Health Summary” option.

## Index

## 謋

**-** , 150

## /

**//** , 149

## ?

**?** , 149

**??** , 149

## ^

**^** , 149

**^^** , 150

## +

**+** , 150

## &lt;

**&lt;RET&gt;** , 149

## A

action profile, 113

**Action Rx Profile** , 50

Ad Hoc Health Summary, 37

Ad Hoc Health Summary option, 37

**Ad Hoc Summary** , 130

***Add New Component*** , 127

Appendix C—Health Summary Component, 133

Appendix D—DHCP And Health Summary Conventions, 149

## B

bar codes, 25

Batch Print of All Clinics by Visit Date, 111

Batch Printing Process, 111

Brief component, 68

Build Health Summary Type option, 75

## C

**COMP=C** , 149

*Component* , 33

**Components** , 130

Conventions, 149

CPRS, 63

create new components, 127

Create/Modify Health Summary Type, 75

Create/Modify Health Summary Type option, 76

Cumulative Selected component, 69

## D

**Default** , 130

Default Header, 38

Default values, 39

*Delete Batch Printing Set Up* , 113

Deleting a Health Summary Component, 82

Deleting a health summary type, 82

**Device** , 130, 150

disable, 69

**Displaying or Printing a Health Summary** , 33

## E

E3Rs, 127

Encounter Form Utilities, 128

Evening Batch Printing, 112

## G

Glossary, 130

GMTS TASK STARTUP option, 112

*GMTS VIEW ONLY* , 110

GMTSMGR, 82

***GMTSMGR key*** , 76, 110

## H

**Health Summary** , 63

Health Summary Component Description List, 133

Health Summary Components, 68

Health Summary Coordinator’s Menu, 109

Health Summary Menu, 32

Health Summary Overall Menu [GMTS MANAGER], 26

health summary type, 70

hospital location, 114

**Hospital Location** , 130

Hospital Location Health Summary option, 51

How to Use This Manual, 30

## I

**ICD Text Displayed** , 130

Information Menu option, 53, 69

Inquire about a Health Summary Component, 56

Inquire about a Health Summary Type, 53

Integrated Billing Package, 128

Introduction, 1

IRM/ADPAC Maintenance options, 109

## K

Kernel, 149

Keys, 110

## L

*List Batch Health Summary Locations* , 114

List Batch Health Summary Locations option, 114

List Health Summary Component Descriptions, 60

List Health Summary Components, 57

List Health Summary Type, 55

List Health Summary Types, 55

locations, 114

lock, 55

*Lock* , 110, 130

Locks and Security, 110

## M

Modify Health Summary Type, 80

## N

nightly batch processing, 111

**Non-destructive** , 130

non-workdays, 111

Notifications, 36

## O

Occurrence limits, 35

**Occurrence Limits** , 131

OE/RR V. 2.5, 33

options, 32

Outpatient Pharmacy Action Profile, 25

owner, 55

Owner, 110, 131

## P

Patient Health Summary Option, 33

PRINT ACTION PROFILE, 113

PRINT DAYS AHEAD, 113

Print Manager, 128

Printing Conventions:, 150

**Provider Narrative** , 131

## Q

Q &amp; A, 127

## R

Reports, 63

Reports tab, 63

## S

Security, 110

security keys, 110

*Selected component* , 33, 68

selection items, 33

*Selection items* , 36

**Selection Items** , 131

Set-up Batch Print Locations, 111

Special Keys, Commands, and Symbols, 149

summary order, 35

**Summary Order** , 131

**Summary Type** , 131

## T

task job, 111

TASK STARTUP, 112

Time limits, 35

**Time Limits** , 131

*Type* , 33, 74

## U

***User responses*** , 30

## V

VA FileMan, 149

VISTA packages, 12