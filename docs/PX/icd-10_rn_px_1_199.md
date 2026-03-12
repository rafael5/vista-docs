---
app_name: Patient Care Encounter (PCE) (PX)
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
package_id: PX
patch: null
patch_gap: null
section: ''
source_file: icd-10_rn_px_1_199.docx
status: draft
title: Patient Care Encounter (PCE)
---

ICD-10 Follow On Class 1 Software Remediation

# Patient Care Encounter (PCE)

# Release Notes

PX*1.0*199


July 2014


Product Development

Table of Contents

1.	Introduction	1

1.1.	Purpose	1

1.2.	Background	1

1.3.	Scope of Changes	2

1.4.	Documentation	3

2.	New Features and Functions	4

2.1.	Differentiating ICD-9 and ICD-10 Diagnosis Codes	4

2.2.	Diagnosis Code Search Function	4

3.	Changes to Existing Software	7

3.1.	Historical Encounters	7

3.2.	Reports	7

3.2.1.	CIDC Missing Data Report	7

3.2.2.	Diagnosis Ranked by Frequency Report	9

*(This page included for two-sided copying.)*

## 1 Introduction

### Purpose

These Release Notes describe new features and functions, as well as changes to existing software, resulting from the International Classification of Diseases, Tenth Revision (ICD-10) software remediation effort for Veterans Health Information Systems and Technology Architecture (VistA) Patient Care Encounter (PCE), patch number PX*1.0*199.

### Background

On January 16, 2009, the Centers for Medicare &amp; Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with ICD-10 Clinical Modification (ICD-10-CM) and ICD-10 Procedure Coding System (ICD-10-PCS) dates of service, or dates of discharge for inpatients, that occur on or after the 
ICD-10 Activation Date (initially October 1, 2013).

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters.  This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care.  ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                                                           | ICD-10-CM                                                                     |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 3-5 characters                                                                     | 3-7 characters (not including the decimal)                                    |
| 1st character is numeric (chapters 1-17) or alpha (E or V) (supplemental chapters) | Character 1 is alpha; character 2 is numeric                                  |
| 2nd, 3rd, 4th and 5th characters are numeric                                       | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters                                                   | Decimal is used after third character                                         |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

### Scope of Changes

NOTE: Existing ICD-9 functionality has not changed.

With implementation of ICD-10 codes, patch PX*1*199 provides differentiation between ICD-9 and ICD-10 diagnosis codes.

Throughout the PCE package, references to ICD-9 are frequently changed to a generic reference such as ICD or Diagnosis. The ICD-9 label is retained in a few places where only ICD-9 codes will be displayed. All reports have been reformatted to accommodate the longer ICD-10 codes and the longer descriptions.  Essentially, though, users should experience very little change. In addition, other VistA packages that use PCE services through Application Program Interface (API) calls should experience no change in functionality. The API parameters for both Input and Output remain the same.

An example of the updated text changes where ICD-9 is now generic to represent ICD-9 or ICD-10 is shown below:

Old

Associated Primary Diagnosis ICD9 Code not in File 80

New

Associated Primary Diagnosis ICD Code not in File 80

Examples of the updated text changes where ICD-9 or ICD-10 will be individually specified based on the transaction date or report date range are shown below:

Select ICD-9 Diagnosis: 100.81

*or*

ICD-10 Diagnosis Code: F17.209

*************************

HELP SCREEN               ALL DIAGNOSES (ICD-9 CODES)

ITEM  CODE      DESCRIPTION

1     001.1     CHOLERA DUE TO VIBRIO CHOLERAE EL TOR

2     001.9     CHOLERA, UNSPECIFIED

3     002.0     TYPHOID FEVER

*or*

HELP SCREEN               ALL DIAGNOSES (ICD-10 CODES)

ITEM  CODE      DESCRIPTION

1     A00.0     CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR CHOLERAE

2     A00.1     CHOLERA DUE TO VIBRIO CHOLERAE 01, BIOVAR ELTOR

3     A00.9     CHOLERA, UNSPECIFIED

*************************

3 Most Frequent ICD9 Diagnoses:

Code                    Description                 Frequency

-------- ------------------------------------------  ---------

1.  280.8    IRON DEFIC ANEMIA NEC                            4

2.  305.79   OTHER SYMPATHOMIMETIC, NEC                       3

3.  812.09   FX UPPER HUMERUS NEC-CL                          2

*or*

3 Most Frequent ICD10 Diagnoses:

Code                    Description                                     Freq.

-------- ------------------------------------------                      ---------

A00.0    Cholera due to Vibrio cholerae 01, biovar cholerae                   4

E08.649  Diabetes due to underlying condition w hypoglycemia w/o coma         3

H21.253  Iridoschisis, bilateral                                              2

The changes documented in the following sections pertain to the Options/Actions within the PCE Coordinator Menu listed below:

PCE COORDINATOR MENU OPTIONS

SUP    PCE Encounter Data Entry - Supervisor

PCE    PCE Encounter Data Entry

DEL    PCE Encounter Data Entry and Delete

NOD    PCE Encounter Data Entry without Delete

VIEW    PCE Encounter Viewer

PCE provides the ability to add, edit, store and search on ICD-10-CM diagnosis codes. PCE displays ICD-10-CM diagnosis codes and short descriptions/definitions.

Note:  If the encounter or appointment date is prior to the ICD-10 Activation Date, PCE retains the current search functionality for ICD-9 diagnosis codes and descriptions/definitions.

### Documentation

The following manuals are updated with changes for PX*1*199:

PCE User Manual

PCE User Manual Appendices

PCE Technical Manual

The following manuals do not contain changes relating to PX*1*199:

PCE Installation Guide

The following manual does not exist for this package/application:

Security Guide


## 3 New Features and Functions

The following enhancements allow for entry, display, lookup (search), print, storage, and internal and/or external transmissions of the ICD-10-CM code sets:

ICD-10-CM replaces ICD-9-CM as the diagnostic coding system for outpatient encounters with an encounter date on or after the ICD-10 Activation Date.

There will be a period of time when dual code sets (ICD-9-CM and ICD-10-CM) are used to accommodate outpatient encounter dates of service prior to and following the ICD-10 Activation Date, as well as for reporting and research purposes.

### Differentiating ICD-9 and ICD-10 Diagnosis Codes

If the encounter or appointment date is prior to the ICD-10 Activation Date, the PCE package adds an ICD-9 label following diagnosis prompts within PCE: DX, ED, CP, IM, ST, IN.

If the encounter or appointment date is on or after the ICD-10 Activation Date, the PCE package adds an ICD-10 label to the following diagnosis prompts within PCE: DX, ED, CP, IM, ST, IN.

PCE ENCOUNTER ACTIONS

UE  Update Encounter

AD  Add Standalone Enc.

HI  Make Historical Encounter

IN  Checkout Interview

ED  Edit an Item

IM  Immunization

ST  Skin Test

DD  Display Detail

DX  Diagnosis (ICD)

EP  Expand Appointment

CP  CPT (Procedure)

### Diagnosis Code Search Function

The PCE ICD-10 diagnosis code search functionality allows you to select a single, valid ICD-10 diagnosis code and display its description. The user interface prompts you for input, invokes the Lexicon utility to get data, and then presents that data.

This search method provides a “decision tree” type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes. A dash after a number indicates that it contains a sub-category.

ICD-10-CM diagnosis code search highlights include:

The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined is the process of selecting the correct valid ICD-10 diagnosis code.

You are presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, you are prompted to refine the search.

You can “drill down” through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.

Short descriptions for the valid ICD-10-CM codes display.

Partial code searches are possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

The PCE package provides the ability to search on ICD-10-CM diagnosis codes at the following prompts:

ICD-10 Diagnosis Code:

Primary ICD-10 Diagnosis:

1st Secondary ICD-10 Diagnosis:

ICD-10 Diagnosis:

ICD-10 Diagnosis 2:

Enter ICD-10 Diagnosis :

Enter NEXT ICD-10 Diagnosis:

What is ICD-10 DIAGNOSIS 1 for this procedure:

Example of ICD-10 Diagnosis Code Search

Select Action: Quit// DX   Diagnosis (ICD)

Patient's Service Connection and Rated Disabilities:

Service Connected: No

Rated Disabilities: None Stated

ICD-10 Diagnosis Code: **S62**

7 matches found

1.  S62.0-     Fracture of navicular [scaphoid] bone of wrist

(147)

2.  S62.1-     Fracture of other and unspecified carpal bone(s)

(357)

3.  S62.2-     Fracture of first metacarpal bone (231)

4.  S62.3-     Fracture of other and unspecified metacarpal

bone (560)

5.  S62.5-     Fracture of thumb (105)

6.  S62.6-     Fracture of other and unspecified finger(s)

(490)

7.  S62.9-     Unspecified fracture of wrist and hand (21)

Select 1-7: **1**

4 matches found

1.  S62.00-    Unspecified fracture of navicular [scaphoid]

bone of wrist (21)

2.  S62.01-    Fracture of distal pole of navicular [scaphoid]

bone of wrist (42)

3.  S62.02-    Fracture of middle third of navicular [scaphoid]

bone of wrist (42)

4.  S62.03-    Fracture of proximal third of navicular

[scaphoid] bone of wrist (42)

Select 1-4: **4**

42 matches found

1.  S62.031A   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Initial Encounter

for closed Fracture

2.  S62.031B   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Initial Encounter

for open Fracture

3.  S62.031D   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Subsequent

Encounter for Fracture with Routine Healing

4.  S62.031G   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Subsequent

Encounter for Fracture with Delayed Healing

5.  S62.031K   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Subsequent

Encounter for Fracture with Nonunion

6.  S62.031P   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Subsequent

Encounter for Fracture with Malunion

7.  S62.031S   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of right Wrist, Sequela

8.  S62.032A   Displaced Fracture of Proximal third of

Navicular [Scaphoid] Bone of left Wrist, Initial Encounter

for closed Fracture

Press &lt;RETURN&gt; for more, "^" to exit, or Select 1-8: **1**

## 4 Changes to Existing Software

Existing software was enhanced to accommodate Historical Encounters. Reports were updated to display ICD-10 information.

### Historical Encounters

PCE is able to accommodate Historical Encounters in the ICD-9 environment with the use of the HI menu option, as shown below:

Current ICD-9 Functionality for Historical Encounters

UE  Update Encounter      CD  Change Date Range     VC  View by Clinic

LI  List by Appointment   CC  Change Clinic         DD  Display Detail

AD  Add Standalone Enc.   IN  Check Out Interview   GF  GAF Score

**HI  Make Historical Enc.** PC  PC Assign or Unassign

TI  Display Team Info     QU  Quit

SP  Select New Patient

Select Action: Quit//HI {RETURN}

Select Action: Quit// HI   Make Historical Enc.

This will create a historical encounter for documenting a clinical encounter

only and will not be used by Scheduling, Billing or Workload credit.

Enter RETURN to continue or '^' to exit: '

All other types of VISIT records use the Visit Date to determine whether the diagnoses associated with the record will come from the ICD-9 code set or the ICD-10 code set. The historical encounter records, also known as historic event records, must allow entry of ICD-10 codes when **Data Entry Date** is on or after the ICD-10 Activation Date.

Therefore, when the system’s date is on or after the ICD-10 Activation Date, PCE provides the ability to assign an ICD-10 code to a historic patient encounter and then add, edit, store, display, and search for the ICD-10 code on a historic patient encounter.

### Reports

Reports documented below pertain to the following Options within the PCE Coordinator and PCE Clinical Reports menus:

MENU OPTIONS

PCE Coordinator Menu:

MDR    CIDC Missing Data Report

PCE Clinical Reports Menu:

CP     Caseload Profile by Clinic

DX     Diagnosis Ranked by Frequency

#### CIDC Missing Data Report

The Missing Data Report sort selection now lists DIAGNOSIS as selection 3 rather than ICD9.

CIDC Missing Data Report

| PCE Missing Data Report  Would you like to include ALL Data Sources? YES//  **Y**  ****  Selection ****  Beginning date:  **9/29/2013**  (SEPTEMBER 29, 2013)  Ending date:  **10/2/2013**  (OCTOBER 2, 2013)  *** Report Sort Selection ***  (1)  DATA SOURCE  (2)  CPT  (3)  DIAGNOSIS  (4)  PATIENT  (5)  ELIGIBILITY  Enter number between 1 and 5:  **3**  Select one of the following:  D         DETAILED REPORT  S         STATISTICS ONLY  Select report type: DETAILED REPORT//  **D  DETAILED REPORT**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCE MISSING DATA REPORT  OCT 2,2013@07:25:32  By Clinic, Provider, and Date  SEP 29, 2013 through OCT 2,2013  Page 1  =================================================================================  BARKER DENTAL  Unknown  SORT VALUE:  DIAGNOSIS  ICD9 = 130.5  SEP 29, 2013:  Patient   SSN          Date/Time           Enc. ID    Created by User   Defect  Test, PT  000-00-0000  SEP 29, 2013@9:00   00XXX-YYY  PROVIDER,ONE      Procedure: 11308 missing assoc. DXs  TOTAL DEFECTS FOR 00XXX-YYY:  1  TOTAL DEFECTS FOR SEP 29, 2013:  1  TOTAL ENCOUNTERS FOR SEP 29, 2013:  1  TOTAL DEFECTS FOR SORT VALUE - 130.5: 1  TOTAL ENCOUNTERS FOR SORT VALUE - 130.5: 1  =================================================================================  ICD10 = I13.1  OCT 1, 2013:  Test, PT  000-00-0000  OCT 1, 2013@9:00   00XXX-YYY  TOTAL DEFECTS FOR 58PQG-CHY:  1  TOTAL DEFECTS FOR OCT 1, 2013:  1  TOTAL ENCOUNTERS FOR OCT 1, 2013:  1  TOTAL DEFECTS FOR SORT VALUE – I13.1: 1  TOTAL ENCOUNTERS FOR SORT VALUE – I13.1: 1  ================================================================================= |

#### Diagnosis Ranked by Frequency Report

The date of the report determines whether ICD-9 or ICD-10 codes and descriptions are printed.

CPE Diagnosis Ranked by Frequency Report

****************************************************************************

8  Most Frequent ICD10 Diagnoses:

Code      Description                                                     Freq.

--------  ------------------------------------------------------------  -------

A00.0     Cholera due to Vibrio cholerae 01, biovar cholerae                 3

E08.649   Diabetes due to underlying condition w hypoglycemia w/o coma       2

W54.0XXA  Bitten by dog, initial encounter                                   1

I11.0     Hypertensive heart disease with heart failure                      1

I10.      Essential (primary) hypertension                                   1

H21.253   Iridoschisis, bilateral                                            1

E11.319   Type 2 diabetes w unsp diabetic rtnop w/o macular edema            1

A01.00    Typhoid fever, unspecified                                         1

*****************************************************************************

*(This page included for two-sided copying.)*