---
app_name: 'CPRS: Problem List (GMPL)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMPL
patch: null
patch_gap: null
section: ''
source_file: gmpl_2_0_49_tm.docx
status: draft
title: gmpl 2 0 49 tm.docx
---

<!-- image -->

**Problem List**

**Technical Manual**

Version 2.0

September 1994

*Updated: December 2017*


Enterprise Program Management Office

This page left intentionally blank.

## Revision History

| **Date**         | **Page**          | **Change**                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Project Manager/Technical Writer**   |
|------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| December 2017    | 2, 11, 11, 33, 34 | Changes for GMPL*2.0*49:  - Added a summary of the changes involved with patch GMPL*2.0*49. - Added information about the GMPL IMPRT UTIL key. - Added a section on importing National, local, and VISN Problem Selection Lists and how to create local lists. - Changed the items listed under the Create Problem Selection Lists - Removed reference to the GMPL DE-ASSIGN LIST menu item                                                                       | REDACTED                               |
| July 2016        | 3                 | Minor change per review.                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                               |
| June 2016        | 3, 20, 32, 37     | Added descriptions for new functionality provided by GMPL*2.0*40.  - First is a summary of GMPL*2*40. - Added the new options under the Allocations of Options and Menus section. - Added the new options to the list of items on the Problem List Management Menu. - Added a brief description of new options for reporting and correcting SNOMED that should be ICD codes. - Removed the Checksum section. For checksum information, see the patch description. | REDACTED                               |
| February 2016    |                   | Added descriptions for new functionality provided by GMPL*2.0*45                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                               |
| March 2014       |                   | Added descriptions for new functionality provided by GMPL*2.0*42                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                               |
| May 2013         |                   | Updates provided by developer, Joel Russell                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED                               |
| June 2012        | 36                | Added descriptions for new options provided by GMPL*2.0*36.                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED                               |
| June 2012        |                   | Updates per all problem list patches since the 1994 release, including patch GMPL*2.0*36                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                               |
| March-April 2002 |                   | Format changes; updates per all problem list patches since the 1994 release, including patch GMPL*2.0*26                                                                                                                                                                                                                                                                                                                                                          | REDACTED                               |
|                  |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                        |

## Table of Contents

Revision History	iii

Table of Contents	vi

Introduction	1

Functionality	1

Changes Made by GMPL*2*49 – Problem Selection List Enhancements	2

Changes Made by GMPL*2*40 – Erroneous Problem File Cleanup	3

Changes Made by GMPL*2*45 – Changes to Comment Length and a Provider Can Now View, Edit, or Delete Comments Entered by Another Provider	3

Changes Made by GMPL*2*42 - PROBLEM LIST SUPPORT FOR ICD-10-CM	3

Diagnosis Code Search	4

Add/Edit/Store Diagnosis Code	4

Display Diagnosis	5

Print Diagnosis	6

Changes Made by GMPL*2.0*44 - PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS	7

Changes Made by GMPL*2*36 - EXTENSIONS TO ACCOMMODATE SNOMED-CT	7

Problem List NTRT Follow-up Report	8

Problem List Freetext Follow-up Report	8

Related Manuals	8

Implementation and Maintenance	9

Edit PL Site Parameters [GMPL PARAMETER EDIT]	9

Problem List Setup for CPRS	10

Allocation of Security Keys	11

Importing Problem Selection List Content	11

Importing Content Requires a Key	11

Required File Format for the GMPL Import Utility	11

Format for Adding or Deleting Problem Selection List Content	12

Locating Updates to the National Problem List Content	13

Creating Local/VISN Problem Selection List Content for Import	16

Exported Options and Menus	19

Problem List NTRT Follow-up Report	20

Problem List Freetext Follow-up Report	20

SNOMED in Diagnosis Field Error Report	20

SNOMED in Diagnosis Field Cleanup Report	20

Generate SNOMED in Diagnosis Field Err/Cleanup Rpt	20

Routine Descriptions	21

Problem List Files	22

Cross-References	22

Archiving and Purging	30

Callable Routines/Entry Points/Application Program Interfaces (APIs)	31

External Relations	32

Internal Relations	32

Package-Wide Variables	51

How to Generate On-Line Documentation	54

Glossary	56

National Acronym Directory:	56

## Introduction

The Problem List application is used to document and track a patient's problems.  It provides the clinician with a current and historical view of the patient's health care problems across clinical specialties.  It will allow each identified problem to be traced through the VistA health care system in terms of treatment, test results, and outcome.

The Problem List application is designed to be used by primary caregivers such as physicians, nurses, social workers, and others, in both inpatient and outpatient settings, as well as by ward clerks and coding clerks.

Various data entry methods are possible with this application.

### Functionality

- Allows a clinician to view an individual problem list for any given patient.
- Supports a variety of specialized views of a patient's problem list.
- Uses the Lexicon Utility, which permits use of "natural" terminology when selecting a problem.  Each term is well-defined and understandable. A user, site, or application may substitute a preferred synonym.
- May be linked to other sections of the medical record, such as Health Summary and Integrated Billing Encounter Forms.
- If Problem List Health Summary components are used in conjunction with the Computerized Patient Record System (CPRS), then you may view Problem List from other treating facilities within the VA, provided Remote Data Views (RDV) have been implemented (includes Health Summary patched up to GMTS*2.7*29, and Order Entry/Results Reporting patched up to patch OR*3.0*85)
- Supports importation of problem information from other clinical settings outside the immediate VAMC.
- Allows reformulation of a problem.
- Supports multiple forms of data capture: Direct clinician entry, clerk entry, encounter forms, foreign problem lists, scannable encounter forms, hand-held devices, etc.

### Changes Made by GMPL*2*49 – Problem Selection List Enhancements

This patch introduces enhancements to the Problem Selection List feature that may be used as an alternative method to quickly document common and/or frequently used problems by selecting problems from the curated specialty categories containing the top SNOMED CT diagnoses pre-mapped to ICD-10-CM called the VA-National Problem Selection List. This patch includes updates to the Problem Selection List menu items and menu actions to assist in the creation and maintenance of selection lists related to editing and assigning of problem selection lists to users and locations.

<!-- image -->

A CAC, or appropriate person, can assign a Problem Selection List that will display on the left of the Problems tab. If a list is assigned, there will be a listing of categories and when the category is selected, the pane below displays the problems it contains.  This screen capture shows the VA-National Problem Selection List Content.

To support these enhancements, the file structure for #125 and #125.11 were redesigned and the data is migrated with new reports to identify duplicate selection lists and categories and selection list names in mixed/lower case. Because mixed case list names are no longer allowed, this patch converts any lists with mixed case to all upper case. A new class field was added to both #125 and #125.11 files to identify, control, and manage the editing capabilities of national, VISN, or local level lists and categories. In CPRS, the VA-National Problem Selection List will display by default unless users have previously defined their own selection lists. The national selection list will be nationally distributed and maintained but require Clinical Application Coordinators (CAC) to import the updates using new GMPL Selection List Import feature.

This patch works with the OR*3.0*429 patch that migrates existing problem selection list assignments that currently exist into a new parameter setting. The patch migrates the list assignments that will be available after the patch is installed.

### Changes Made by GMPL*2*40 – Erroneous Problem File Cleanup

To correct an issue where SNOMED codes get stored in the DIAGNOSIS field #.01 instead of ICD codes, three new options have been added to the Problem List Mgt Menu [GMPL MGT MENU]:

1. SNOMED in Diagnosis Field Error Report [GMPL DIAG ERROR REPORT]
2. SNOMED in Diagnosis Field Cleanup Report [GMPL DIAG CLEANUP REPORT]
3. Generate SNOMED in Diagnosis Field Err/Cleanup Rpt [GMPL GENERATE DIAG RPTS]

The first two reports identify fields that have the error and where they are cleaned up. The third option enables users with access to this menu to rerun the filescan and cleanup tasks for any potential new errors.

### Changes Made by GMPL*2*45 – Changes to Comment Length and a Provider Can Now View, Edit, or Delete Comments Entered by Another Provider

The length of the comment field has been changed from less than 60 characters (which includes spaces and punctuation) to less than 200.

Also, providers can now view, edit, and delete another provider’s comments on a problem.

### Changes Made by GMPL*2*42 - PROBLEM LIST SUPPORT FOR ICD-10-CM

This is the Problem List patch to support the requirements of ICD-10-CM implementation. The Problem Search function will continue to originate with the Problem List Subset of SNOMED CT and follow the algorithm introduced by the Problem List Data Standardization effort and CPRS v29. Prior to the ICD-10-CM implementation date (1 October 2015), the selected

SNOMED CT code will continue to be resolved to the corresponding ICD-9-CM code(s), and all of the Problem List display and print options will continue to render the diagnostic codes as ICD-9-CM.

Beginning on the ICD-10-CM implementation date, the selected SNOMED CT code will be resolved to the corresponding ICD-10-CM code(s), and all of the Problem List display and print options will render the diagnostic codes as either ICD-9-CM or ICD-10-CM, depending upon the date when the code for the problem was last edited.

#### Diagnosis Code Search

- The Problem List application continues to provide the ability to search for SNOMED CT diagnoses and will assign a generic ICD-10 diagnosis code of R69 upon selection from the Lexicon Utility. When the VA transitioned to ICD-10, the VA did not have a SNOMED CT to ICD-10 map available, therefore R69 (the equivalent to ICD-9-CM 799.9) had to be assigned to each SNOMED CT term upon each problem selection. The Problem List package requires an ICD code along with the SNOMED CT problem upon saving in the patient’s record.
- ICD diagnosis code search is prohibited on the Problems tab.

( ****** **NOTE** : On the Problem List Lexicon Search dialog, the system will display the selected SNOMED CT description and the SNOMED CT concept code. To view the ICD code, click on the problem to open the Problem Details window.)

<!-- image -->

Users may use the following search methods:

- SNOMED CT concept codes
- Text strings (i.e. SNOMED CT descriptions)

#### Add/Edit/Store Diagnosis Code

- If the “Current System Date” is on or after the ICD-10 activation date, the Problem List package will provide the ability to perform the following actions for ICD-10-CM diagnosis codes (problems) through the Action List items on the patient’s problem list.
    - New Problem: Add an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Change: Change an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Inactivate: Inactivate a problem containing a SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Verify: Verify an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Annotate: Annotate and update an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Remove: Remove an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - Restore: Restore an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.
    - View Details: View details of an active SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code of R69.

#### Display Diagnosis

- The Problem List allows for the display of problems for the Active View, Inactive View, and Removed View options within the initial Problem List.
    - The Problem List application will display the patient’s list of problems. Problems entered prior to July of 2013  will display in ICD-9-CM and those entered after will be represented in SNOMED CT. Problems added through Reminder Dialogs or Group notes will display problems in an ICD-10 diagnosis short description within the initial Problem List screen and will label whether an ICD diagnosis code is either ICD-9 or ICD-10.
- When user selects the ‘View Details’ action, the CPRS Problem List application will:
    - Display the details of an SNOMED CT diagnosis linked to an ICD-10-CM diagnosis code or the placeholder ICD-10-CM code of R69 with its full descriptions/definitions, or
    - If the problem was updated via the encounter form, it would display the newly linked ICD-10-CM code and not the R69.
    - Print the SNOMED CT to ICD-10-CM diagnosis code audit history
- When using the ‘View Details’ action, the CPRS Problem List application will display the ICD-10 label, ICD-10-CM diagnosis code, and short description within the audit history.

<!-- image -->

<!-- image -->

### Print Diagnosis

- When the user selects the View Details action:
    - If the date the diagnosis code was entered is on or after the ICD-10 activation date, the Problem List application will provide the ability to print the problem represented in SNOMED CT and the a ICD-10-CM diagnosis codes and full descriptions/definitions.
    - The Problem List application will designate whether a diagnosis code is SNOMED CT, ICD-9 or ICD-10.
    <!-- image -->

### Changes Made by GMPL*2.0*44 - PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS

This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

^PXRMINDX (9000011, CODING **SYSTEM,”ISPP”, CODE, STATUS, PRIORITY, DFN, DLM, DAS)**

^PXRMINDX (9000011, CODING SYSTEM,”PSPI”, DFN, STATUS, PRIORITY, CODE, DLM, DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Manual (PXRM\_INDEX\_TM).

The post-install routine will start a background job to rebuild the file #9000011 index in the new format.

### Changes Made by GMPL*2*36 - EXTENSIONS TO ACCOMMODATE SNOMED-CT

The purpose of this patch is to accommodate the use of the Systematic Nomenclature of Medicine -- Clinical Terms (SNOMED CT) for selection of Patient Problems, and to dovetail with the efforts of Standard Terminology Service (STS) to implement SNOMED CT on both the Enterprise Terminology Server and the Clinical Lexicon, using the New Term Rapid Turnaround (NTRT) strategy for vetting and deployment of novel clinical expressions.

This patch introduces changes required by CPRS v29 for selection of Patient Problems using SNOMED CT.

A new bulletin, GMPL PROBLEM NTRT BULLETIN, is added by the patch. This bulletin is sent to members of the FORUM mail group g.PROBLEM LIST NTRT when a SNOMED CT Concept is selected by the user for which no ICD-9-CM codes are mapped. The mail group is populated with members of OI&amp;T’s Standards and Terminology Service. When approved by the Domain Steward for Problem List, new standardized mappings will be deployed using the New Term Rapid Turnaround capability.

**Note:** This bulletin has been disabled.

Two new options are included in the patch:

#### Problem List NTRT Follow-up Report

This report allows sites to evaluate problems with valid SNOMED CT Concept codes, which were unmapped to ICD at the time of entry.

The report may be filtered by Medical Center Division, Provider(s), and Time Interval.

#### Problem List Freetext Follow-up Report

This report allows sites to evaluate uncoded free text problems that have been entered by one or more providers over a specified time interval.

### Related Manuals

Problem List Installation Guide

Problem List User Manual

Lexicon Utility v. 2.0 Technical Manual

Automated Information Collection System (AICS) v 3.0 Technical/User Manual

List Manager v 1.0 Technical Manual

Patient Care Encounter (PCE) v. 1.0 Technical Manual

Kernel v 8.0/Unwinder (XQOR) v. 7.1 Technical Manual

## Implementation and Maintenance

Implementation and maintenance of Problem List occur several ways:

1.	By integration with other applications:

- Lexicon Utility (which uses the Multi-term Lookup utility - MTLU - part of the Kernel Toolkit 7.3).  The Lexicon Utility can be modified to meet local site needs, to make Problem List fit your hospital's preferences.
- Encounter Form (part of Integrated Billing)
- Health Summary
- Patient Care Encounter (PCE)
- CPRS

Management of Problem List includes coordinating with these other entities. This linkage should remain transparent to users, but will require setup and coordination by the IRM office and Clinical Coordinators. See the technical and user manuals of those packages for implementation instructions.

2.	By setting site parameters with the GMPL PARAMETER EDIT option.

3.	By allocating menus and options (see page 7).

By user customization either through GMPL USER PREFS MENU or GMPL BUILD LIST MENU (see the Problem List User Manual for descriptions of these).

### Edit PL Site Parameters [GMPL PARAMETER EDIT]

This option lets you toggle four site parameters for the Problem List; these parameters are stored in the Problem List Site Parameters file #125.99.

To modify these parameters, use the menu option GMPL MGT MENU - Edit PL Site Parameters. Changes made to these settings will affect ALL users. The settings included are as follows:

VERIFY TRANSCRIBED PROBLEMS. Does your site require verification of problems entered by holders of the OREMAS key?

PROMPT FOR CHART COPY. This setting is not used by the GUI version.

USE CLINICAL LEXICON. Does your site use the Clinical Lexicon for problem lookup and entry, or should only free-text entries be used?

DISPLAY ORDER. C:  Chronological; R:  Reverse chronological

SCREEN DUPLICATE ENTRIES. Not used by the GUI Problems tab. If a duplicate entry is found when a new problem is being entered, the user is warned, and given the choice of whether or not to continue.

A flag can be placed on problems that are entered by clerks so that a clinician must review the problems and verify them.

You can choose whether the users will be prompted to have a chart copy printed when they exit the patient's problem list (if it has changed).

You can choose whether to display the patient problem list in chronological or reverse chronological order.

At the “Screen duplicate entries”: prompt, type Y and press &lt;Enter&gt;.

Select Problem List Mgt Menu Option: **Edit** PL Site Parameters

VERIFY TRANSCRIBED PROBLEMS: YES// **?**

Enter YES to flag transcribed entries for clinician verification.

CHOOSE FROM:

1        YES

0        NO

VERIFY TRANSCRIBED PROBLEMS: YES// **NO**

PROMPT FOR CHART COPY: YES, ASK// **?**

Enter YES to be prompted to print a new copy before exiting the patient's

list, if it has been updated.

CHOOSE FROM:

1        YES, ASK

0        NO, DON'T ASK

PROMPT FOR CHART COPY: YES, ASK// **&lt;RET&gt;**

DISPLAY ORDER: CHRONOLOGICAL// **?**

Enter the order in which the problems should be displayed for your site,

according to the date each problem was recorded.

CHOOSE FROM:

C        CHRONOLOGICAL

R        REVERSE-CHRONOLOGICAL

DISPLAY ORDER: CHRONOLOGICAL// **&lt;RET&gt;**

Select Problem List Mgt Menu Option: **&lt;RET&gt;**

### Problem List Setup for CPRS

Patch GMPL*2*10 created APIs to provide data to CPRS. See the sections on APIs and Remote Procedure Calls under External Relations in this manual. No other setup is required.

### Allocation of Security Keys

**GMPL IMPRT UTIL:** The GMPL IMPRT UTIL key is used to access the new Import Utility menu option. Users with this access will be responsible for performing the National Problem Selection List updates and for creating/maintaining VISN or Local Problem Selection lists/categories if requested.

**GMPL ICD CODE:** The GMPL ICD CODE security key is used to determine if the current user is trained and authorized to code provider text relating to the ICD Diagnosis codes. Recommended allocation: PIMS Coding Clerks.

### Importing Problem Selection List Content

With patch GMPL*2.0*49, authorized users can now import Problem Selection List content by using the Import Problem Selection List menu option. To provide their users with this content, sites can use the National Problem Selection List content available from a web site ( [Problem List Content](http://vista.med.va.gov/cprs/html/PL_select_list_updates.html) ) or sites can define Local or VISN lists with problem selection list content. One advantage of National Problem Selection List content is that it has SNOMED CT codes that are linked to ICD-10-CM codes for the same problem.

Sites can also create local or VISN content that can be imported if it is in the correct format. In addition, Local or VISN lists can be built in the Problem List’s List Manager interface using the Lexicon search to add each problem individually.  Problems added to lists in this way will have a SNOMED CT code assigned to an ICD-10-CM code of R69.

The lists can then be edited, removing or adding categories and problems. When lists are completed, CACs can assign the lists at the User, Location, Division, or System level.

Importing lists provides several benefits:

The ability to add SNOMED CT to ICD10 mappings into the Problem List (for example, GERD – Gastro-Esophageal Reflux Disease  -&gt; K21.9)

The ability to use SNOMED CT alternate descriptions

- **HTN – Hypertension** instead of **Hypertensive Disorder**
- **Rash** instead of **Eruption**

Provides a quicker national content distribution mechanism compared to the patch method

#### Importing Content Requires a Key

Access to this option is controlled by the GMPL IMPRT UTIL key. Only users holding this key may access the Import Utility option.

#### Required File Format for the GMPL Import Utility

To import a problem selection list content file, the content must be in a very specific format. An example of the format for the National file is shown below. Instructions for creating a local or VISN file are given in the Creating Local Problem List Content for Import section.

The format of the national, VISN, or local files is very similar. The differences are the value in the class of Selection List and value in the Class of Category. National content will be maintained by a national group. Local personnel who create local or VISN lists must maintain their lists when there are changes released by the Standard Development Organizations for SNOMED CT and ICD-10-CM.

#### Format for Adding or Deleting Problem Selection List Content

Below, CACs can see that they will have the ability to add or delete content using the Import Utility. For CACs, this applies only to Local or VISN lists. To add a selection list, category, or problem using the import utility, the user places a pound sign (#) in the first column of the spreadsheet. To delete, the user instead places an @ symbol in the first column. The correct format is shown below.

**Note:** CACs can also use the menu options to delete items from local or VISN lists, but not from national lists.

**Warning:** If a user deletes an entire list, all categories in that list will also be deleted. The same applies to a category. If the user deletes a category, all problems under the chosen category will also be deleted.

**CSV file format legend:**

|   **Excel rows or columns** | **A**                   | **B**                  | **C**                                  | **D**                           | **E**                 |
|-----------------------------|-------------------------|------------------------|----------------------------------------|---------------------------------|-----------------------|
|                           1 | #=ADD or @=Delete       | Name of Selection List | Class of Selection List  (Local, VISN) | Class of Category (Local, VISN) |                       |
|                           2 | #=ADD or @=Delete       | Category Sequence      | Name of Category                       | CPRS Display Name               |                       |
|                           3 | Problem sequence number | Problem text           | ICD-10-CM code (s)                     | SNOMED Concept ID               | SNOMED Designation ID |

<!-- image -->

#### Locating Updates to the National Problem List Content

To find the URL for the Problem Selection national list, please go to the CPRS National Selection List Updates web page located at:

[http://vista.med.va.gov/cprs/html/PL\_select\_list\_updates.html](http://vista.med.va.gov/cprs/html/PL_select_list_updates.html)

**Users with the GMPL IMPRT UTIL key can import National updates and create Local or VISN Problem Selection Lists. The following steps illustrate how to import a problem list content file:**

1. In VistA, go to the Problem List Management [GMPL MGT MENU] menu.

Select the Create Problem Selection Lists [GMPL BUILD LIST MENU] option, by typing 3 and pressing &lt;Enter&gt;.

Select the Import Problem Selection List option by typing 6 and pressing &lt;Enter&gt;.

At the Select the Import Method prompt, select the either

- HF (to import a host file from a server)
- WEB (to import it from the web) and press &lt;Enter&gt;.
    1. At the Import URL for the CSV file: prompt, enter the appropriate information
        - URL for the web location of the CSV file
        - Location of a file on a local server
    and then press &lt;Enter&gt;.
        1. If you would like to review the content, at the Do you want to review the problem selection list contents? Prompt, type Y and press &lt;Enter&gt;. If not, type N and press &lt;Enter&gt;. It is recommended to review all content to ensure content is correct before the data is saved into the files.
    To save the list, at the Do you want to save the imported list contents? prompt type Y and press &lt;Enter&gt;. If you do not wish to save this list, type N and press &lt;Enter&gt;.
    Select OPTION NAME: GMPL MGT MENU       Problem List Mgt Menu
    1      Patient Problem List
    2      Edit PL Site Parameters
    3      Create Problem Selection Lists ...
    4      List Patients with Problem List data
    5      Search for Patients having selected Problem
    6      Replace Removed Problem(s) on Patient's List
    7      Problem List NTRT Follow-up Report
    8      Problem List Freetext Follow-up Report
    9      SNOMED in Diagnosis Field Error Report
    10     SNOMED in Diagnosis Field Cleanup Report
    11     Generate SNOMED in Diagnosis Field Err/Cleanup Rpt
    &lt;CPM&gt; Select Problem List Mgt Menu &lt;TEST ACCOUNT&gt; Option: 3  Create Problem
    Selection Lists
    1      Build Problem Selection List(s)
    2      Copy Selection List from IB Encounter Form
    **&gt; Out of order:  This option has been disabled due to the Problem
    List SNOMED CT implementation.
    3      Assign/Remove Problem Selection List
    4      Delete Problem Selection List
    5      Check Problem Selection List Problem Codes
    6      Import Problem Selection List
    &lt;CPM&gt; Select Create Problem Selection Lists &lt;TEST ACCOUNT&gt; Option: 6  Import
    Problem Selection List
    Select one of the following:
    HF        CSV host file
    WEB       CSV file from a web site
    Select the import method: WEB  CSV file from a web site
    Input the URL for the CSV file: http://vista.med.va.gov/cprs/docs/pl\_content\_updates/GMPL249\_Import\_14August2017\_NatUpdate1.csv
    Starting the import process ...
    Do you want to review the problem selection list contents? Y// n  NO
    Do you want to save the imported list contents? N// y  YES
    Import process completed successfully.

#### Creating Local/VISN Problem Selection List Content for Import

1. Obtain the Local/VISN Problem Selection List name, problem category name (s), and list of common problems for that category  from the requester
2. Use Microsoft Excel to build the Local/VISN Problem Selection List spreadsheet by entering the information based on the steps below

Enter # to add or @ to delete in (A1)

Enter the name of the Selection List in (B1)

Enter the Class (Local/VISN) of the Selection List (C1)

Enter the Class (Local/VISN) of the Problem Category (D1)

Enter # to add or @ to delete (A2) Problem Category

Enter the sequence number of the Problem Category (B2)

Enter the Name of the Problem Category (C2)

Enter the name of the Problem Category’s CPRS Display Name (D2)

Enter the sequence number of the Problem Sequence (B3-n)

Enter the text of the Problem (SCT CONCEPT CODE) (B3-n)

Enter the linked ICD-10 code to the SNOMED term (C3-n)

Enter the SNOMED CT Concept ID with the letter ‘C’ prefixing the concept ID (D3-n)

Enter the SNOMED CT Description ID with the letter ‘D’ prefixing the description ID associated with the Problem Selection List text in step j (E3-n)

1. How to find the SNOMED CT concept ID, description ID, and the Problem text in SNOMED CT:

Recommend using NLM SNOMED CT Browser. VA has an enterprise license, but each user must apply for the **NLM** UMLS license and set up a UMLS account before it will allow users to use the SNOMED CT browser.

[https://uts.nlm.nih.gov//license.html](https://uts.nlm.nih.gov/license.html) Then access the UMLS Terminology Services SNOMED CT Browser [https](https://uts.nlm.nih.gov/snomedctBrowser.html) [://](https://uts.nlm.nih.gov/snomedctBrowser.html) [uts.nlm.nih.gov/snomedctBrowser.html](https://uts.nlm.nih.gov/snomedctBrowser.html)

Click SNOMED CT in the banner and select SNOMED CT Browser from the drop down list

1. Access the NLM SNOMED CT Browser and enter the problem in the search box to get a list of returned matches. Select the best matched term to represent the Problem. Only ACTIVE concepts from the Clinical Finding, Events, or Situation with Explicit Context hierarchies are appropriate for documentation in the Problem List package. This terms will be shown with the tags of (Finding), (Disorder), (Events), or (Situation) at the end of the description.

SNOMED CT Concept ID

<!-- image -->

The Fully Specified Name with the (Disorder) hierarchy tag.  Do not use this description type

<!-- image -->

The description ID with text

<!-- image -->

1. From the list of returned matches, click on the term that best represents the problem requested. The system displays the concept in the top panel showing the Concept ID. Copy and paste the Concept ID.

Next look at the list of descriptions and choose the description that best matches the problem requested. Do Not select the Fully Specified Name as your description or the British spelling description; select one of the synonyms. Copy the description into the Selection List text cell or Column (B3-n) and the associated description ID for that SNOMED CT description and paste it into Column E.

Repeat for each problem entry.

1. Prepare the spreadsheet for saving.
    1. Run spellcheck and make corrections as needed.
Ensure wrap text is not enabled on the Microsoft ribbon, if so uncheck and verify each row the wrap text is NOT enabled.
Review column A, the Problem Sequence, is listed sequentially.
Review column B, the Category Sequence, is listed sequentially.
Review column B, the Problem text and that it is in the required format CAD - Coronary Artery Disease (SCT 53741008).
Review column C, the ICD code, verify each 3 digit code has a decimal point and is using the forward slash when there are more than one ICD codes.
Review column D and verify the letter ‘C’ precedes the SNOMED CT concept ID.
Review column E and verify the letter ‘D’ precedes the SNOMED CT designation ID.
    1. Save the spreadsheet In Microsoft Excel AND  in CSV formats
        - Save the spreadsheet as Microsoft Excel XLSX for a readable copy
        - **IMPORTANT:** Save the spreadsheet as a Comma Delimited (CSV) to use with the Import Utility but follow the steps below to do so.From the Tool Bar select **File** | **Save As.**Change the file type from xlsx to csv by selecting the **Comma Delimited** option from the drop down.Select **Save** .The system displays a message, “the selected file type does not support workbooks that contain multiple sheets”, select **OK** .The system displays another message; &lt;File Name&gt; may contain features that are not compatible with CSV. Do you want to keep the workbook in this format? Select **Yes** .Close the spreadsheet with using the File | Close menu item or clicking on the red x in the upper right corner. The system displays another message; “do you want to save the changes you made to &lt;File Name&gt;?” Select **Don’t Save.**Perform a check to verify the CSV file does not contain any errors due to saving; **Open the CSV file by right clicking and open with Notepad from the menu.**
    Review the row that contains the Problem category and verify at the end of the line it does not contain two commas.(i.e. *#,T4 No Category Sequence,Local,Local,,).* If necessary remove one comma so that only one remains.
    Only the first line and each category should contain a comma at the end of the line.
    Select Edit | Find to search the Selection text field for double quotes and remove any that are found.
    Scan to see if there any additional spaces in the Selection text field. Remove any preceding, trailing, or extra spaces between text. There should only be one space between the selection text and the SCT label (i.e.: Asthma (SCT 195967001)).
    Resave the CSV file (repeat steps 3-7 above until a clean file is created).

## Exported Options and Menus

The three menus exported with Problem List are:

Problem List Mgt Menu

Create Problem Selection List (contained on the Management menu)

Problem List User Preferences Menus.

**Allocation of Menus and Options**

IRMS or the Clinical Coordinator can allocate the Problem List menus and options to clinical and clerical users, as appropriate.  Only one set-up option (described on the next page) exists for setting site parameters. Several options can help customize the Problem List for users.

| **Menu or Option Name**                            | **Technical Name**       | **Who**                                           |
|----------------------------------------------------|--------------------------|---------------------------------------------------|
| Assign ICD Diagnoses to  Problem List              | GMPL CODE LIST           | PIMS Clerks,  Clinical Coordinators               |
| Create Problem Selection  List                     | GMPL BUILD LIST  MENU    | IRMS, Clinical  Coordinators                      |
| Patient Problem List                               | GMPL CLINICAL USER       | Clinicians, Nurses,  Clinical Coordinators        |
| Problem List Data Entry                            | GMPL DATA ENTRY          | PIMS Clerks, Clinical  Coordinators               |
| Problem List Mgt Menu                              | GMPL MGT MENU            | IRMS, Clinical  Coordinators                      |
| Problem List User  Preferences Menu                | GMPL USER PREFS  MENU    | IRMS, Clinical  Coordinators, Clinicians,  Nurses |
| Problem List NTRT Follow-up Report                 | GMPL NTRT F/U RPT        | Clinical  Coordinators, Clinicians,  Nurses       |
| Problem List Freetext Follow-up Report             | GMPL FREETEXT F/U REPORT | Clinical  Coordinators, Clinicians,  Nurses       |
| SNOMED in Diagnosis Field Error Report             | GMPL DIAG ERROR REPORT   | Clinical Coordinators                             |
| SNOMED in Diagnosis Field Cleanup Report           | GMPL DIAG CLEANUP REPORT | Clinical Coordinators                             |
| Generate SNOMED in Diagnosis Field Err/Cleanup Rpt | GMPL GENERATE DIAG RPTS  | Clinical Coordinators                             |

The options listed below will need to be added to clinician or user menus:

Patient Problem List [GMPL CLINICAL USER]

Problem List Data Entry GMPL DATA ENTRY]

Assign ICD Diagnoses to Problem List [GMPL CODE LIST]

**Note:** This option is still on the menu, but has been marked out of order.

Problem List User Preferences Menu IIGMPL USER PREFS MENU]

See the Problem List User Manual for further descriptions of Problem List options.

## Routine Descriptions

**Namespace:** *GMPL*

XUPRROU (List Routines) prints a list of any or all of the Problem List routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **list Routines**

Routine Print

Want to start each routine on a new page: No// **[ENTER]**

routine(s) ?   &gt; **GMPL***

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each GMPL subset routine.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?   &gt; **GMPL***

## Problem List Files

The following is a short list of files that problem lists uses and a brief description of what the file contains or changes that have been implemented with the release of patches GMPL*2.0*49 and OR*3.0*429.

PROBLEM SELECTION LIST (#125) - The selection list name, associated class, and associated categories/headers/sequences. The CLINIC field is still there but it is no longer utilized.

PROBLEM SELECTION LIST CONTENTS (#125.1) – This has now been moved to be a subfile of 125 and is no longer used.

PROBLEM SELECTION CATEGORY (#125.11) - category names.

PROBLEM SELECTION CATEGORY CONTENTS (#125.12) - With GMPL*49, this becomes a subfile of file #125.11 and will no longer be utilized.

NEW PERSON (#200), “125.1” field PROBLEM SELECTION LIST  - With GMPL*49, this also will no longer be utilized. The User setting/entity of ORQQPL SELECTION LIST parameter takes its place.

## Cross-References

The Problem List files contain the following MUMPS-type cross-references:

#125 - PROBLEM SELECTION LIST FILE

**B** Cross Reference:  125^ **B** ^REGULAR

1)	S ^GMPL(125,"B",$E(X,1,65),DA)=""

2)	K ^GMPL(125,"B",$E(X,1,65),DA)

**Allows for the look up and sorting of selection list names. A primary key is created to ensure uniqueness in the selection list names.**

**The indexes are stored as follows: ^GMPL(125,"B",NAME,DA),**

**where NAME is the selection list name and DA is the IEN of**

**File #125 or the record number of the selection list.**

#125.01 - PROBLEM SELECTION LIST SUBFILE

**AC** Cross Reference:  125^ **AC** ^MUMPS

1)	S ^GMPL(125,"AC",X(1),DA(1))=""

2)	K ^GMPL(125,"AC",X(1),DA(1))

**Allows the retrieval of categories in a sequential order of a list. The indexes are stored as follows: ^GMPL(125,"AC", CAT, DA(1)).**

**DA(1) is the IEN of File #125 or the record number of the list the category is associated with. CAT is the category within that list.**

**AD** Cross Reference:  125^ **AD** ^MUMPS

1)	S ^GMPL(125,"AD",DA(1),X(1),DA)=""

2)	K ^GMPL(125,"AD",DA(1),X(1),DA)

**Allows the retrieval of the list categories in a sequential order. The indexes are stored as follows: ^GMPL(125,"AD", DA(1), CSEQ, DA).**

**DA(1) is the IEN of File #125 or the record number of the list. CSEQ is the sequence number of the categories associated with that list. DA is the sub-record number for those categories.**

#125.1 - PROBLEM SELECTION LIST CONTENTS FILE

**C** Cross Reference:  125.1^ **C** ^MUMPS

1)	S:$P(^GMPL(125.1,DA,0),U,2)

^GMPL(125.1,"C",X,$P(^(0),U,2),DA)=""

2)	K:$P(^GMPL(125.1,DA,0),U,2)

^GMPL(125.1,”C”,X,$P(^(0),U,2),DA)

**Allows retrieval of list contents in sequenced order.**

**Note:** This cross reference is still valid, but it will no longer be used with GMPL*2.0*49.

#125.11 - PROBLEM SELECTION CATEGORY FILE

**B** Cross Reference:  125.11^ **B** ^REGULAR

1)	S ^GMPL(125.11,"B",$E(X,1,65),DA)=""

2)	K ^GMPL(125.11,"B",$E(X,1,65),DA)

**Allows for the look up and sorting of selection list category names. A primary key is created to ensure uniqueness in the selection list category names.**

**The indexes are stored as follows: ^GMPL(125.11,"B",NAME,DA),**

**where NAME is the selection list category name and DA is the IEN of**

**File #125.11 or the record number of the selection list category.**

**APSQ** Cross Reference:  125.11^ **APSQ** ^MUMPS

1)	S ^GMPL(125.11,"C",DA(1),X(1),DA)=""

2)	K ^GMPL(125.11,"C",DA(1),X(1),DA)

**Allows the retrieval of category problems in a sequenced order. The indexes are stored as follows: ^GMPL(125.11,"C", DA(1), PSEQ, DA).**

**DA(1) is the IEN of File #125.11 or the pointer value of the Category for which the problems are grouped under. PSEQ is the sequence number of the problem under a specific category. DA is the sub-record number associated with the problem entry.**

#125.12 - PROBLEM SELECTION CATEGORY CONTENTS FILE

**C** Cross-reference:  125.12^ **C** ^MUMPS

1)	S:$P(^GMPL(125.12,DA,0),U,2)

^GMPL(125.12,"C",X,$P(^(0),U,2),DA)=""

2)	K:$P(^GMPL(125.12,DA,0),U,2)

^GMPL(125.12,"C",X,$P(^(0),U,2),DA)

**Allows retrieval of problem categories in sequenced order** .

Cross-reference:  125.12^ **C1** ^MUMPS

1)	S ^GMPL(125.12,"C",$P(^GMPL(125.12,DA,0),U),X,DA)=""

2)	K ^GMPL(125.12,"C",$P(^GMPL(125.12,DA,0),U),X,DA)

**Allows retrieval of problem categories in sequenced order.**

**Note:** This cross reference is still valid, but it will no longer be used with GMPL*2.0*49.

#125.8 - PROBLEM LIST AUDIT FILE

**AD** Cross-reference:  125.8^ **AD** ^MUMPS

1)	S:+$P(^GMPL(125.8,DA,0),U,3)

^GMPL(125.8,"AD",X,(9999999-$P(^(0),U,3)),DA)=""

2)	K ^GMPL(125.8,"AD",X,+(9999999-

$P(^GMPL(125.8,DA,0),U,3)),DA)

**Used to retrieve a problem's audit trail in reverse-chronological order.**

Cross-reference:  125.8^ **AD1** ^MUMPS

1)	S ^GMPL(125.8,"AD",$P(^GMPL(125.8,DA,0),U),

(9999999-X),DA)=""

2)	K ^GMPL(125.8,"AD",$P(^GMPL(125.8,DA,0),U),

(9999999-X),DA)

**Used to retrieve a problem's audit trail in reverse-chronological order.**

#9000011 - PROBLEM FILE

**AA** Cross-reference: 9000011^ **AA** ^"MUMPS

1)	S ^AUPNPROB("AA",$P(^AUPNPROB(DA,0),U,2),

$P(^(0),U,6)," "\_$E("000",1,4-$L($P(X,".",1))-1)\_

$P(X,".",1)\_"."\_$P(X,".",2)\_$E("00",1,3-$L(

$P(X,".",2))-1),DA)=""

2)	K ^AUPNPROB("AA",$P(^AUPNPROB(DA,0),U,2),

$P(^(0),U,6)," "\_$E("000",1,4-$L($P(X,".",1))-1)\_

$P(X,".",1)\_"."\_$P(X,".",2)\_$E("00",1,3-$L(

$P(X,".",2))-1),DA)

**Allows problem retrieval by patient, facility, and problem number (Nmbr); the number is used as a string in " 000.00" format to assure a consistent ordering.**

Cross-reference:  9000011^ **AATOO** ^MUMPS

1)	I $P(^AUPNPROB(DA,0),U,6)]"",$P(^(0),U,7)]""

S X1=$P($P(^(0),U,7),"."),X2=$P($P(^(0),U,7),

".",2),^AUPNPROB("AA",X,$P(^(0),U,6)," "\_$E("000",

1,4-$L(X1)-1)\_X1\_"."\_X2\_$E("00",1,3-$L(X2)-1

),DA)="" K X1,X2

2)	I $P(^AUPNPROB(DA,0),U,6)]"",$P(^(0),U,7)]""

S X1=$P($P(^(0),U,7),"."),X2=$P($P(^(0),U,7),

".",2) K ^AUPNPROB("AA",X,$P(^(0),U,6)," "\_$E("000",

1,4-$L(X1)-1)\_X1\_"."\_X2\_$E("00",1,3-$L(X2)

-1),DA),X1,X2

**Allows problem retrieval by patient, facility, and problem number (Nmbr); the number is used as a string in " 000.00" format to assure a consistent ordering.**

Cross-reference:	9000011^ **AATOO2** ^MUMPS

1)	I $P(^AUPNPROB(DA,0),U,2)]"",$P(^(0),U,7)]""

S X1=$P($P(^(0),U,7),"."),X2=$P($P(^(0),U,7),".",2),

^AUPNPROB("AA",$P(^(0),U,2),X," "\_$E("000",1,

4-$L(X1)-1)\_X1\_"."\_X2\_$E("00",1,3-$L(X2)-1),DA)=""

K X1,X2

2)	I $P(^AUPNPROB(DA,0),U,2)]"",$P(^(0),U,7)]""

S X1=$P($P(^(0),U,7),"."),X2=$P($P(^(0),U,7),".",2)

K ^AUPNPROB("AA",$P(^(0),U,2),X," "\_$E("000",1,

4-$L(X1)-1)\_X1\_"."\_X2\_$E("00",1,3-$L(X2)-1),DA),X1,X2

**Allows problem retrieval by patient, facility, and problem number (Nmbr); the number is used as a string in " 000.00" format to assure a consistent ordering.**

**ACTIVE** Cross-reference: 9000011^ **ACTIVE** ^"MUMPS

1)	S:$P(^AUPNPROB(DA,0),U,2) ^AUPNPROB("ACTIVE",

+$P(^(0),U,2),X,DA)=""

2)	K ^AUPNPROB("ACTIVE",+$P(^AUPNPROB(DA,0),U,2),X,DA)

**Allows problem retrieval by patient and status, in order of entry.**

**ASCT** Cross-reference:  9000011^ASCT

1)= S ^AUPNPROB("ASCT",$E(X,1,30),DA)=""

2)= K ^AUPNPROB("ASCT",$E(X,1,30),DA)

3)= ** DO NOT DELETE **

**This REGULAR FileMan cross-reference on SNOMED CT Concept**

**will help to automate the updating of problems when SNOMED**

**Concepts are mapped or re-mapped to ICD-9-CM codes.**

**AV9** Cross-reference:  9000011^ **AV9** ^MUMPS

1)	S:$D(APCDLOOK) DIC("DR")=""

2)	Q

**Controls the behavior of the input templates used by IHS to populate and maintain this file.**

Cross-reference:9000011.1111^ **AV9** ^MUMPS

1)	S:$D(APCDLOOK) DIC("DR")=""

2)	Q

**Controls the behavior of the input templates used by IHS to populate and maintain this file.**

## Archiving and Purging

Archiving and purging utilities, as such, are not provided in the distributed files for version 2.0.

However, the PROBLEM LIST AUDIT FILE, #125.8, holds an audit trail of all changes made to the Problem List file entries including the old and new values, who made the change, and why.

## Callable Routines/Entry Points/Application Program Interfaces (APIs)

APIs, callable routines, and entry points can be viewed by first choosing the *DBA* menu option on FORUM and then choosing the *Integration Agreement* s *Menu* option:

IAs INTEGRATION CONTROL REGISTRATIONS ...

## External Relations

The Problem List package is dependent upon the following VistA packages to function correctly.

| **Package**             | **Minimum Version for**  **initial Installation**   | **Recommended Version**  **as of Patch 49**   |
|-------------------------|-----------------------------------------------------|-----------------------------------------------|
| ICD-10  Lexicon Utility | N/A  1.0                                            | ICD*18*67  2*112                              |
| Kernel                  | 7.1                                                 | 8.0                                           |
| Toolkit (MTLU)          | 7.2                                                 | 7.3                                           |
| List Manager            | 1.0                                                 | 1.0                                           |
| OE/RR                   | 2.5                                                 | 3.0                                           |
| PCE                     | 1.0                                                 | 1.0                                           |
| PIMS/MAS                | 5.3                                                 | 5.3                                           |
| Fileman                 | 20.0                                                | 22.2                                          |
| Unwinder                | 7.1                                                 | Kernel 8.0                                    |

## Internal Relations

All options may be independently invoked.

***Menus***

**GMPL MGT MENU**

Problem List Mgt Menu

1      Patient Problem List [GMPL CLINICAL USER]

2      Edit PL Site Parameters [ROUTINE]

3      Create Problem Selection Lists ... [GMPL BUILD LIST MENU]

4      List Patients with Problem List data [GMPL PATIENT LISTING]

5      Search for Patients having selected Problem [GMPL PROBLEM LISTING]

6      Replace Removed Problem(s) on Patient's List [GMPL REPLACE PROBLEMS]

7      Problem List NTRT Follow-up Report [GMPL NTRT F/U RPT]

8      Problem List Freetext Follow-up Report [GMPL FREETEXT F/U REPORT]

9      SNOMED in Diagnosis Field Error Report [GMPL DIAG ERROR REPORT]

10     SNOMED in Diagnosis Field Cleanup Report [GMPL DIAG CLEANUP REPORT]

11     Generate SNOMED in Diagnosis Field Err/Cleanup Rpt [GMPL GENERATE DIAG

RPTS]

**GMPL BUILD LIST MENU**

Create Problem Selection Lists

1      Build Problem Selection List(s) [GMPL BUILD SELECTION LIST]

2      Copy Selection List from IB Encounter Form [GMPL BUILD ENC FORM LIST]

**&gt; Out of order:  This option has been disabled due to the Problem

List SNOMED CT implementation.

3      Assign/Remove Problem Selection List [GMPL ASSIGN LIST]

4      Delete Problem Selection List [GMPL DELETE LIST]

5      Check Problem Selection List Problem Codes [GMPL SELECTION LIST CSV CHECK]

6      Import Problem Selection List [GMPL SELECTION LIST IMPORT]

**&gt; Locked with GMPL IMPRT UTIL

**GMPL USER LOOK-UP DEFAULTS**

Problem Look-up Defaults

1      Filter [GMPL USER LOOK-UP FILTER]

2      Display [GMPL USER LOOK-UP DISPLAY]

3      Vocabulary [GMPL USER LOOK-UP VOCABULARY]

4      Shortcuts [GMPL USER LOOK-UP SHORTCUTS]

5      List Current Defaults [GMPL USER LOOK-UP LIST]

**GMPL USER PREFS MENU**

Problem List User Preferences Menu

1      Problem List Preferred View [GMPL USER VIEW]

2      Problem Look-up Defaults ... [GMPL USER LOOK-UP DEFAULTS]

3      Preferred Problem Selection List [GMPL USER LIST]

***Options***

**GMPL CLINICAL USER				Patient Problem List**

This option allows clinical users access to the Problem List application; control is passed to the List Manager utility.

**GMPL DATA ENTRY				Problem List Data Entry**

This option allows data entry/maintenance access to the Problem List application; the List Manager utility is invoked here.

**GMPL USER VIEW				Problem List Preferred View**

This option allows an individual user to define his/her own default view of patient problem lists.  Rather than displaying all active problems for a patient, the application will show active problems associated with only selected services or clinics, as defined here.  A user may choose to see a different view of the problem list from within the application by selecting the "Change View" action, including all problems.

**GMPL PATIENT LISTING			List Patients with Problem List data**

This option will generate a listing of all patients having data in the Problem file #9000011.

**GMPL PROBLEM LISTING		Search for Patients having selected Problem**

This option will generate a listing of all patients identified as having a particular problem in the Problem file #9000011; the user is first prompted for the problem, then the file is searched for patients having this problem.

**GMPL BUILD SELECTION LIST		Build Problem Selection List(s)**

This option allows access to utilities to facilitate the creation and maintenance of problem menus, i.e. lists of commonly selected problems.  Categories of problems may be defined, and lists created from linking categories together; categories may be reused in multiple lists.

**GMPL ASSIGN LIST			Assign/Remove Problem Selection List**

This option allows a user to assign or remove selection lists from certain entities using the accustomed General Parameter Tools interface. If a list is specified in the Default Problem Selection List Display [ORQQPL SELECTION LIST] parameter, then the Add New Problem(s) option will present this list of problems to select from. If there are no user defined lists, then a default clinic list will be presented. Searching the Lexicon Utility for a problem not on this list is always an option from these menus as well.

**GMPL BUILD ENC FORM LIST		Copy Selection List from IB Encounter Form**

**Note:** This option has been placed Out of order. This option has been disabled due to the Problem List SNOMED CT implementation.

This option will allow creating a new selection list by copying a list already created through the Encounter Form utility (Integrated Billing package) into a new entry in file #125.  This list will then be available for editing further (only the new list will be altered - the list saved in the Integrated Billing pkg with the form will not be changed here), or for use to select from when entering new problems to a patient's list.

**GMPL CODE LIST				Assign ICD Diagnoses to Problem List**

**Note:** This option has been taken out of service.

This option allows access to a patient's problem list to add, review, or edit the ICD Code assigned to each problem.  A detailed display of problem data is available, as well as searching capability into both the ICD Diagnosis file and the Lexicon Utility to facilitate the coding process.

**GMPL DELETE LIST				Delete Problem Selection List**

This option will allow the user to delete a problem selection list and its contents that is no longer in use.  A list can only be deleted if it is not currently assigned to a User, Clinic, Division, or System entity. This option also checks for any user list assignments in the NEW PERSON file and removes the deleted list appropriately.

**GMPL REPLACE PROBLEMS			Replace Removed Problem(s) on Patient's List**

This option will allow the user to list all of the problems that have been removed from a selected patient's problem list, and optionally place any of them back on the problem list.

**GMPL USER LOOK-UP FILTER		Filter**

This option lets the user either select or create a filter to use while searching the Lexicon.

**GMPL USER LOOK-UP DISPLAY		Display**

This option lets the user either select or create a display format to be used in presenting the selection list during search of the Lexicon.

**GMPL USER LOOK-UP VOCABULARY		Vocabulary**

This option lets the user select a default vocabulary (subset) of the Lexicon to be used during searches (i.e., Nursing, Social Work, etc.).

**GMPL USER LOOK-UP SHORTCUTS		Shortcuts**

This options lets the user select default set of shortcuts to use to rapidly access the Lexicon without conducting an extensive word search.

**GMPL USER LOOK-UP LIST			List Current Defaults**

This option lets a user list their current look-up defaults to a device (terminal or printer).

**GMPL USER LIST 				Preferred Problem Selection List**

This option allows an individual user to define his/her own default list of commonly selected problems; this list will be displayed when the action 'Add New Problem(s)' is invoked, and the user may either choose to add a problem from the menu (selected by display number) or search the Lexicon for a problem not listed.  The same prompts will asked per problem to complete the entry.

**GMPL NTRT FOLLOWUP REPORT**

This report allows sites to evaluate problems with valid SNOMED CT Concept codes, which were unmapped to ICD at the time of entry.

The report may be filtered by Medical Center Division, Provider(s), and Time Interval.

**GMPL FREETEXT FOLLOWUP REPORT**

This report allows sites to evaluate uncoded freetext problems that have been entered by one or more providers over a specified time interval.

**GMPL DIAG ERROR REPORT 		SNOMED in Diagnosis Field Error Report**

This report goes back to the last Problem file cleanup runtime. This report allows sites to identify any occurrences where SNOMED codes have been saved in the Diagnosis field #.01 where an ICD code should be.

DATE LAST      PRIMARY                          SNOMED

IEN               MODIFIED       DIAGNOSIS   SECONDARY DIAGNOSIS  CONCEPT

---------------   ------------   ---------   ---------------------------

351913            Apr 01, 2014   739.3                             20369

**GMPL DIAG CLEANUP REPORT           SNOMED in Diagnosis Field Cleanup Report**

This report goes back to the last Problem file cleanup runtime .This report allows sites to identify any corrections where SNOMED codes in the Diagnosis field #.01 were corrected to ICD codes.

**GMPL GENERATE DIAG RPTS              Generate SNOMED in Diagnosis Field**

**Err/Cleanup Report**

This option allows a user to rerun the file scan and cleanup tasks for any potential new errors.

**GMPL SELECTION LIST CSV CHECK		Check Problem Selection List Problem Codes**

This option will produce a report related to Problem Selection Lists. The report will contain a list of any Problem Selection Lists that contain problems with inactive SNOMED and/or ICD codes attached. It will also determine if any attached ICD codes are due to be inactivated in the future and a report of those findings is also included.

Check Problem Selection List Problem Codes scans all the current selection lists in the system for any problems that have inactive SNOMED and/or ICD codes. The following sample report is displayed to the user. It has been updated to display the problems with inactive codes, as well as the corresponding category and list it is under. Problems with inactive SNOMED concept codes will be identified with &lt;INACTIVE SCT CODE&gt;, inactive ICD codes will be identified with &lt;INACTIVE ICD CODE&gt;, and if both SNOMED &amp; ICD codes are inactive: &lt;INACTIVE SCT/ICD CODE&gt;.

Code Set Version Review of Problem Selection Lists                 Page: 1

--------------------------------------------------------------------------

The following Problem Selection List(s) contain one or more problems that

have inactive SNOMED and/or ICD codes attached to them. Any current users

or clinics using these Selection Lists, will not be able to add the

problems with inactive codes, until the list and the inactive codes are

updated. The list may not be assigned to any additional users or clinics

until updated.

TEST LIST:

CARDIO:

Acute Myocardial Infarction (ICD-9-CM 410.9)   &lt;INACTIVE ICD CODE&gt;

Coronary Artery Disease (ICD-9-CM 414.9)   &lt;INACTIVE ICD CODE&gt;

Angina Pectoris, Unstable (ICD-9-CM 411.1)   &lt;INACTIVE ICD CODE&gt;

Chest Pain (ICD-9-CM 786.50)   &lt;INACTIVE ICD CODE&gt;

Angina Pectoris (ICD-9-CM 413.9)   &lt;INACTIVE ICD CODE&gt;

Dyspnea (ICD-9-CM 786.09)   &lt;INACTIVE ICD CODE&gt;

GENERAL:

Headache (ICD-9-CM 784.0)   &lt;INACTIVE ICD CODE&gt;

Fever (ICD-9-CM 780.6)   &lt;INACTIVE ICD CODE&gt;

UROLOGY:

Bladder Carcinoma (ICD-9-CM 188.9)   &lt;INACTIVE ICD CODE&gt;

Impotence (ICD-9-CM 302.72)   &lt;INACTIVE ICD CODE&gt;

Type &lt;Enter&gt; to continue or '^' to exit:

**GMPL SELECTION LIST IMPORT			Import Problem Selection List**

LOCK: GMPL IMPRT UTIL			PACKAGE: PROBLEM LIST

This patch also introduces a new import utility that will assist in the addition and distribution of National problem selection list content. This utility or menu option is locked with the new GMPL IMPRT UTIL security key and should only be assigned to CAC users. The utility allows CACs to import external list content to the VistA system using two import methods:

HF        	CSV host file

WEB       CSV file from a web site

Both methods require the selection list content to be in a specific spreadsheet format and saved as a comma separated value (.CSV) file. If utilizing the "HF" method, the CSV host file must reside on an accessible host system. If utilizing the "WEB" method, the CSV host file must reside on an accessible website.

This patch will also install the first version of the VA-NATIONAL PROBLEM SELECTION LIST which comprises of the following national selection list categories:

VA-PRIMARY CARE

VA-CARDIOLOGY

VA-DENTAL

VA-DERMATOLOGY

VA-DIABETES

VA-EARS NOSE THROAT

VA-EMERGENCY DEPARTMENT

VA-ENDO METAB EXCEPT DIABETES

VA-GASTROENTEROLOGY

VA-GENERAL SURGERY

VA-GYNECOLOGY

VA-HEMATOLOGY

VA-INFECTIOUS DISEASE

VA-MENTAL HEALTH

VA-NEUROLOGY

VA-NEUROSURGERY

VA-ONCOLOGY

VA-OPHTHALMOLOGY

VA-ORTHOPEDICS

VA-PAIN

VA-PLASTIC SURGERY

VA-POLYTRAUMA

VA-PULMONARY

VA-RENAL NEPHROLOGY

VA-RHEUMATOLOGY

VA-UROLOGY

Once installed, commonly used diagnoses under these categories will be available for CAC's to copy and utilize when building local problem selection lists for their site users/clinics.

***Protocols***

**GMPL ANNOTATE				Comment on a Problem**

This action will append a brief comment(s) to a problem entry, up to 200 characters in length.

**GMPL CODE ICD SEARCH			Search ICD Diagnoses for Codes**

This option allows the user to search the ICD Diagnosis file for the selected problem's text; for this option it is recommended that the Multi-Term Lookup utility be setup to operate on this file (#80).

**GMPL CODE LIST				Problem List ICD Codes**

This menu uses the List Manager utility to display all of a patient's problems with data relevant to a billing clerk/coder.  Only the ICD code may be edited, but a detailed display of all information stored about a problem is available to facilitate the assignment of a code.

**GMPL DATA ENTRY				Problem List Data Entry**

This menu uses the List Manager utility to display a patient's problem list with data relevant to the needs of a clinic or billing clerk.  Various actions may be taken here such as adding, removing, editing, and printing problems.

**GMPL DELETE				Remove Problems**

This action will remove an entry from a patient's problem list; the problem is not physically deleted from the file, but flagged as "removed" and, except for historical purposes, generally ignored.

**GMPL DETAILED DISPLAY			Detailed Display**

This action will present an expanded display of each problem selected from the patient's problem list.  All available information will be shown, including comments by all authors and an audit trail of changes made to the problem.

**GMPL DT CONTINUE			Continue to Next Selected Problem**

If multiple problems were selected for review under the "Detailed Display" action, this will allow retrieval of the data from the next problem of those selected.

**GMPL DT MENU				Detailed Display**

This menu contains actions available for navigating the problems selected to review in the "Detailed Display" action.  The user may go on to the next selected problem when finished reviewing, or exit and return to the problem list.

**GMPL EDIT ICD				ICD Code**

This action allows a user with the GMPL ICD CODE key to assign a [new] ICD Code to a problem.

**GMPL EDIT MENU				Edit Problem Values**

This protocol is for use with the List Manager utility, to display the current editable values of the selected problem entry in a list format for editing.

**GMPL EDIT NEW NOTE			Append a new note to problem**

This action will allow appending additional comment(s) to the currently selected problem.

**GMPL EDIT NOTES				Edit Existing Note(s)**

This action will allow editing of comments that have previously been appended to a problem entry.  Notes will be displayed for editing only if the current user is the author of the note; accessing this action through the Manager's Menu will set a flag allowing all notes for the current problem to be displayed and edited.

**GMPL EDIT ONSET				Onset**

This action allows the entry/editing of the date of onset of a problem.

**GMPL EDIT PROBLEM			Edit a Problem**

This option allows editing of select fields of a problem entry; all changes made to a patient's problem are recorded in the Problem Audit file.  A problem is selected, and control is transferred to the List Manager and GMPL EDIT MENU protocol.

**GMPL EDIT PROVIDER			Primary Provider**

This action allows the entry/editing of the primary provider of care for this problem.

**GMPL EDIT RECORDED			Date Recorded**

This action allows editing of the date the problem was originally recorded; date will default to NOW when entering a new problem, but may be changed to an earlier date to reflect entry in the paper chart.

**GMPL EDIT REFORMULATE			Reformulate Problem Description**

This action allows limited reformulation of the current problem.  If new problem text is entered, the narrative is passed to the Lexicon Utility to find a match; both the user's narrative and the new Clinical term will be stored, as with a new problem entry.  If the new problem selected from the LU is already an entry on the patient's list, the user will be alerted.

**GMPL EDIT REMOVE				Remove Problem from List**

This action will remove the current entry from the patient's list; the problem is not physically deleted from the file, but flagged as "removed" and, except for historical purposes, generally ignored.  The user is then returned to the entire problem list.

**GMPL EDIT SAVE				Save Changes and Exit**

This action allows the user to save any changes made to the current problem, and return to the entire problem list.  If this action is not selected and the problem has been changed, the user will be asked when exiting if s/he wishes to save the changes.

**GMPL EDIT SC				Service Connection**

This action allows editing the service connection status of the current problem; if the service connection of this problem was previously unknown, it may be entered here.  Data will only be asked for if the patient has service connection indicated in the Patient file.  MCCR will be using this data for billing purposes.

**GMPL EDIT SERVICE				Service or Clinic**

This action allows the entry/editing of the service primarily responsible for the care of this problem.  This data will be used for screening and grouping the problems displayed in the user's selected view of the list.

**GMPL EDIT SP				Special Exposure**

This action allows editing the special exposures associated with the current problem; if exposures related to this problem were previously unknown, it may be entered here.  Data will only be asked for if the patient is indicated for Agent Orange, Ionizing Radiation, or Persian Gulf exposures in the Patient file.  MCCR will be using this data for billing.

**GMPL EDIT STATUS				Status**

This action allows editing the status assigned to a problem; if the problem is inactivated, the user will be asked for Date Resolved also.

**GMPL EDIT VERIFY				Verify**

If the parameter "Verify Transcribed Problems" is turned on in the Problem List Site Parameters file (#125.99), this action will allow a clinician to mark the current problem as verified.  A "$" will appear immediately in front of the problem text if the current problem was transcribed in by a clerk and the above described parameter is on; entering a "$" at the "Select Item" prompt will invoke this action.

**GMPL HIDDEN MENU			Problem List Hidden Actions**

This menu contains the List Manager functions relevant to the operation of the Problem List application; it is accessible from any "Select Action" prompt by entering "??".

**GMPL INACTIVATE				Inactivate Problems**

This action allows a problem to be inactivated.

**GMPL LIST CLU				Add a Problem not on the Menu**

This action will allow selection of a problem not listed in the displayed menu, to be added to the current patient's problem list.  The code invoked here is the same as for the regular 'Add' action, possibly allowing a look-up into the Clinical Lexicon Utility.

**GMPL LIST MENU				List Commonly Seen Problems**

This protocol is for use with the List Manager utility, to display the user's preferred list of commonly seen problems to facilitate selection and addition to the patient's problem list.

**GMPL LIST SELECT ITEM			Select Item from Menu**

This action will allow selection of a problem listed in the displayed menu, to be added to the current patient's problem list.  The same prompts will be stepped through for each problem selected as if it had been entered through the regular 'Add' action.  If the item selected is a category heading, the list will be expanded to include all the problems included in that category for selection.

**GMPL MENU ADD GROUP			Add Category to List**

This action allows adding one or more problem categories to a selection list.

**GMPL MENU ADD PROBLEM			Add Problems to Category**

This action allows adding one or more problems to a problem category.

**GMPL MENU ASSIGN LIST			Assign List**

This action allows the user to assign this list to a clinic or to user(s).  Linking a list to a clinic will invoke the list whenever a user selects that clinic as the location where the patient was seen, when adding new problems.  If a list is linked to a user, this is the list that will always be invoked when that user is adding new problems, regardless of the clinic specified that the patient was seen in.

**GMPL MENU BUILD GROUP			Build Problem Categories**

This menu allows the creation of categories of problems, to facilitate selecting a new problem to add to a patient's problem list.  Categories may then be linked together to form lists, in which they may be ordered and titled.  Categories may be reused in multiple lists, as well.

**GMPL MENU BUILD LIST			Build Problem Selection List**

This menu allows the creation of lists of problems, to facilitate selecting a new problem to add to a patient's problem list.  Problems are added or removed in categories, which may also be ordered or titled for clarity.

**GMPL MENU COPY GROUP		Copy to New Category**

This menu action allows the user to copy an existing category to a new category. Local/VISN categories may not be copied into a National category. However National categories may be adopted/copied into a Local/VISN category for local modifications.

**GMPL MENU CREATE GROUP 		Enter/Edit Category**

This action transfers control to the List Manager utility, to bring up a new screen allowing the entry/editing of any problem category.  The user will be asked for the category s/he wishes to review and edit, and a screen similar to the 'Build List' menu will be shown allowing similar actions to edit the contents of the selected category.  A new category may be entered here, which will be available to add to the current list upon return to the 'Build List' screen when finished.

**GMPL MENU DELETE GROUP		Delete Category**

This action allows the user to delete a problem category; it will be completely removed from the Problem Selection Category file, if no list currently contains it.

**GMPL MENU EDIT GROUP DISPLAY		Edit Category Display**

This action allows the user to change the text that appears as the subheader of a category of problems, and whether or not to display the problems in the category automatically on entry to the list.

**GMPL MENU EDIT PROBLEM			Edit Problems**

This action allows the user to edit the problem and its associated code; if no code is currently assigned to the problem, one may be entered.

**GMPL MENU NEW GROUP			Change Categories**

This action allows the user to switch to editing a new problem category.

**GMPL MENU NEW LIST			Change Selection Lists**

This action allows the user to switch to editing a new problem selection list.

**GMPL MENU REMOVE GROUP		Remove Category from List**

This action allows the user to remove a problem category from the current list; it remains in the Problem Selection Category file for future use.

**GMPL MENU REMOVE PROBLEM		Remove Problem from Category**

This action allows the user to remove a problem from the current category.

**GMPL MENU RESEQUENCE GROUPS		Resequence Categories**

This action allows the user to place the problem categories on the current list in a different order; problems will be automatically renumbered.

**GMPL MENU RESEQUENCE PROBLEMS	Resequence Problems**

This action allows the user to place the problems in the current category in a different order; problems will be automatically renumbered for display and selection purposes.

**GMPL MENU SAVE GROUP			Save Category and Quit**

This action allows the user to save any changes that have been made to the current category and exit the utility.

**GMPL MENU SAVE LIST			Save List and Quit**

This action allows the user to save any changes that have been made to the current list and exit the utility.

**GMPL MENU VIEW GROUP			View w/wo Seq Numbers**

This action allows the user to toggle between displaying the sequence numbers assigned to each problem for ordering, or the display numbers only.

**GMPL MENU VIEW LIST			View w/wo Seq Numbers**

This action allows the user to toggle between displaying the sequence numbers assigned to each category for ordering, or the display numbers only.

**GMPL NEW PROBLEM			Add New Problems**

This action will allow the addition of a new entry to a patient's problem list.  The user will be asked to select a term from the Clinical Lexicon Utility describing the problem, and to enter other relevant information.

**GMPL OE DATA ENTRY			Patient Problem List**

This action will allow entry to the Problem List application from the OE/RR Ward Clerk menu.  The variable ORVP is checked for the current patient, and then control is passed to the PL.

**GMPL OE PROBLEM LIST			Patient Problem List**

This action will allow entry to the Problem List application from the OE/RR Clinician and Nurse menus.  The variable ORVP is checked for the current patient, and then control is passed to the PL.

**GMPL PATIENT				Select New Patient**

This allows selection of a new patient from within the Problem List application; a new list will be generated and displayed for review.

**GMPL PRINT				Print Problem List**

This action allows printing a copy of the problem list, either the currently displayed view (which may be abbreviated) or the complete list in chartable format.

**GMPL PRINT LIST				Print Problem List**

This action will generate a complete listing of the patient's problem list in chartable format.  Active and inactive problems will appear here in this listing.

**GMPL PROBLEM LIST			Problem List**

This menu uses the List Manager utility to display a patient's problem list with data relevant to the needs of a clinician.  Various actions may be taken here such as adding, removing, editing, inactivating, and appending comments; the user may also see a detailed display of selected problem(s) or change which problems appear on the displayed view of the list.  A new patient's list may be selected or a printout of the list generated.

**GMPL UP ADD ITEM				Add Items to View**

This action allows the user to include additional service(s) in his/her preferred view of patient problem lists.

**GMPL UP DELETE VIEW			Delete Preferred View &amp; Exit**

This action allows the user to delete his/her preferred view and exit the utility.  The user will again see all active problems, when initially displaying a patient's problem list.

**GMPL UP REMOVE ITEM			Remove Items from View**

This action allows the user to remove service(s) from his/her preferred view of patient problem lists.

**GMPL UP SAVE VIEW				Save Preferred View &amp; Exit**

This action allows the user to save any changes made to his/her preferred view of patient problem lists; control is passed back to the User Preferences menu.

**GMPL UP SWITCH				Select New View of Problems**

This action allows the user to switch to a different preferred view.  If one is currently editing a service view of problem lists, this action will clear the current view and bring up a list of clinics from which to select a view, and vice-versa from clinic to service list.  NOTE:  Each user may have only ONE preferred view at a time!

**GMPL USER PREFS				Preferred View of Problem List**

This menu contains actions allowing a user to change his/her preferred view of patient problem lists.  A set of services may be defined here that will be used as a default screen when displaying patient problem lists for this user; the view may be changed dynamically within the Problem List application through the "Change View" action, but it will not be stored as a new default unless updated here.

**GMPL VERIFY				Verify Problems**

If the parameter "Verify Transcribed Problems" is turned on in the Problem List Site Parameters file (#125.99), this action will allow a clinician to mark the selected problem(s) as verified.  A "$" will appear immediately in front of the problem text for problems that were transcribed in by a clerk and the above described parameter is on; entering a "$" at the "Select Action" prompt will invoke this action.

**GMPL VIEW					Select View of List**

This allows the user to change the problems displayed onscreen in the patient's list, on-the-fly.  Various attributes are presented for selection such as status, provider, and clinic (or service if the patient is currently admitted).

**GMPL VIEW ACTIVE				Active only**

This action will screen the problems from the current patient's list for only those that are currently active.

**GMPL VIEW ALL CLIN			All Clinics**

This action will remove any current screen on clinics associated with problems, and include problems being followed by all clinics.

**GMPL VIEW ALL PROV			All Providers**

This action will remove any current screen on primary providers of care for problems, and include problems being treated by all providers.

**GMPL VIEW ALL SERV			All Services**

This action will remove any current screen on services associated with problems, and include problems being treated by all services.

**GMPL VIEW BOTH				Active &amp; Inactive**

This action will remove any current screen on problem status and include problems that are both active and inactive on the display.

**GMPL VIEW CLINIC				Selected Clinic(s)**

This action will screen the problems from the current patient's list for only those associated with the selected clinic(s) for care.

**GMPL VIEW INACTIVE			Inactive only**

This action will screen the problems from the current patient's list for only those that are currently inactive.

**GMPL VIEW INCLUDE INACTIVE		Show All Problems**

This action will include problems that are both active and inactive on the list of problems displayed; active problems will appear first, followed by the inactive problems.

**GMPL VIEW INPAT				Inpatient View Menu**

This menu contains actions allowing the user to change his/her current view of the patient's problem list.  The problems displayed onscreen may be changed by selecting the status, service, and/or provider from which the user wishes to see problems listed.  The number of problems listed and the total number of problems will be shown in the upper right-hand corner of the screen.

**GMPL VIEW OUTPAT				Outpatient View Menu**

This menu contains actions allowing the user to change his/her current view of the patient's problem list.  The problems displayed onscreen may be changed by selecting the status, clinic, and/or provider from which the user wishes to see problems listed.  The number of problems listed and the total number of problems will be shown in the upper right-hand corner of the screen.

**GMPL VIEW PROVIDER			Selected Provider**

This action will screen the problems from the current patient's list for only those listed as being treated by the selected provider.

**GMPL VIEW RESTORE			Preferred View**

This action will replace the currently specified view with the user's pre-defined preferred view.

**GMPL VIEW SERVICE			Selected Service(s)**

This action will screen the problems from the current patient's list for only those associated with the selected service(s) for care.

**GMPL VIEW SWITCH				Inpatient View**

This action will allow the user to switch from displaying the problems in an outpatient mode to an inpatient mode, or vice-versa.  If clinic information is currently being displayed, service and provider will now be displayed after selecting this action; likewise, if service and provider information are currently displayed, clinic will now be shown.

## Package-Wide Variables

**Patient Variables**

GMTSAGTOR	Flag; if patient was exposed to Agent Orange,

1 = Y, 0 = N

GMPDFN	Holds pointer to the current patient,  = pointer ^ patient name

GMPGULF	Flag; if patient was in the Persian Gulf and exposed to environmental contaminants, 1 = Y, 0 = N

GMPHNC	Flag; if patient is diagnosed with Head and/or Neck Cancer

from exposure to Nose or Throat Radium treatments,

1 = Y, 0 = N

GMPION	Flag; if patient was exposed to ionizing radiation,

1 = Y, 0 = N

GMPMST	Flag; if patient was victim to Military Sexual Trauma,

1 = Y, 0 = N

GMPSC	Flag; patient is service connected or not (PIMMS),

1 = service connected, 0 = not service connected.

**Current View of List Variables**

GMPLVIEW(“ACT”)	Status of the currently displayed view of the Problem List,

= A if active only, I if inactive only, and “” (null) if all

problems are included.

GMPLVIEW(“CLIN”)	Contains all of the clinics included in the currently displayed view of the list, as pointers to the Hospital Location file (#44) in the form of “ptr/ptr/ptr...” or “” (null) if all are included.

GMPLVIEW(“PROV”)	Provider of the currently displayed list,

= ptr (file #200) ^ Name, or 0 if all providers

GMPLVIEW(“SERV”)	Contains all of the Services included in the currently displayed

view of the list, as pointers to the Service/Section field (#49) in the form of “ptr/ptr/ptr...” or “” (null) if all are included.

**Site Parameter Variables**

GMPARAM(“CLU”)	Flag; based on parameter, to allow user to search the Lexicon Utility for a problem.

GMPARAM(“PRT”)	Flag; based on parameter, to prompt for a new printout.

GMPARAM(“REV”)	Flag; based on parameter, determine if list will display in chronological or reverse chronological order by date recorded.

GMPARAM(“VER”)	Flag; transcribed problems flagged for verification (based on parameter) 1 = Yes, 0 = No

**Other Variables**

GMPCOUNT	Total number of problems in currently displayed list

GMPLUSER	Flag; if user entered package through clinical or data entry interface = $D if clinical, ‘$D if clerical

GMPRINT	Flag; if patient’s list has changed during user’s session, need to print new problem list.

GMPROV	Requesting Provider of action on Problem List defaults to current user (DUZ) if clinician = prt (to #200) ^ Name

GMPVA	Flag; if site is a VAMC (1) or non-VA (0).

Set based on DUZ(“AG”)

GMPVAMC	User’s station/facility = DUZ(2) = ptr to Institution file (#4)

## How to Generate On-Line Documentation

**Routines**

To get a list or printout of any or all of the Problem List routines, use the Kernel option XUPRROU (List Routines).  This option is on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

To get a list of all Problem List routines, type GMPL* after you are prompted for routines.

The first line of each routine contains a brief description of the general function of the routine.  Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to get a list of just the first line of each Problem List routine.

**Globals**

The globals exported by Problem List are ^GMPL( and ^AUPNPROB(.  To get a printout of these global, use the Kernel option XUPRGL (List Global) on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

**Files/Data Dictionary**

The number-spaces for Problem List files are 125 to 125.99.  Use the VA Fileman option DILIST (List File Attributes) to get a list of these files.  Depending on the Fileman template used to print the list, this option will print out all or part of the data dictionary for the Problem List files.

**Menus/Options**

The menus and options exported by the Problem List package all begin with the GMPL name space.  You can view individual options by using the Kernel option XUINQUIRE (Inquire).  This option is on the menu XUMAINT (Menu Management), which is a sub-menu of the EVE (Systems Manager Menu) option.

You can produce a diagram of the structure of the Problem List menus and their options with the Kernel option XQDIAGMENU (Diagram Menus).  Choosing XQDIAGMENU allows you to further select XUUSERACC for a diagram of the menus, XUUSERACC1 for a detailed diagram of the menus with entry and exit actions, or XUUSERACC2 for an abbreviated diagram of the menu and options.

**XINDEX**

XINDEX is a routine that produces a report called the VA Cross-Referencer, a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what sub-routine they are referenced in, and a listing of internal and external references (both routine calls and global references).

When prompted to select routines, select GMPL* for Problem List application routines.  You can de-select the Problem initialization routines by selecting -GMPLI* and -GMPLO*.

## Glossary

The OIT Master Glossary is available at: [http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

#### National Acronym Directory:

[http://vaww1.va.gov/Acronyms/](http://vaww1.va.gov/Acronyms/)


Action	A functional process a user takes within the Problem List option that affects the end result or what is actually accomplished by the option. *Examples* : Edit a problem, print a problem, list, add a comment to a problem.

Audit	A feature that provides an ongoing chronological listing of who made what changes to the Problem List.

Clinical Term	Names used for problems, diagnosis, procedures, etc.

Clinician	A doctor or other health care provider in the medical center who is authorized to enter problems onto a patient’s chart.

CPRS	Computerized Patient Record System is an umbrella term used to refer to clinical packages accessed by health care providers, to include Adverse Reaction Tracking System, Clinical Reminders, Consults/Request Tracking, Health Summary, Order Entry/Results Reporting, ***Problem List*** , and Text Integration Utility.

CPT	Clinical Procedures Terminology is a coding and classification system for procedures used for billing purposes, and published by the American Medical Association.

Data Dictionary	This is a file that defines a file's structure, to include a file's fields and relationship to other files. This is sometimes called schema.

DSM-IVR	Diagnostic and Statistical Manual of Mental Disorders is a coding and classification system used by mental health professionals, and published by the American Psychiatric Association.

Encounter Form	A paper form (which can be created by a form generator utility) for use with Problem List to print a patient’s problems on, for the clinician to edit and/or add new problems, then used by clerks to enter new problems and/or edit existing problems.

Health Summary	A VistA clinical module that allows users to compile summaries of a patient’s health care by combining various components of data drawn from other VistA modules such as Laboratory, Pharmacy, Radiology and Problem List.

ICD-9-CM	International Classification of Diseases, 9 th Revision, Clinical Modification, is a coding and classification system for diagnostic terms used for billing purposes, and published by the Centers for Medicare and Medicaid Services (CMS), formerly the Health Care Financing Administration (HCFA).

ICD-10-CM	International Classification of Diseases, 10 th Revision, Clinical Modification. There is a nationwide mandate by the Centers for Medicare &amp; Medicaid Services (CMS) that all healthcare coding is done using the International Classification of Diseases Tenth Revision (ICD-10) code sets, effective October 1, 2013.

IHS (Indian Health Service)	The Indian Health Service has a computerized system comparable to VistA, called the Resource and Patient Management System (RPMS).  Patient Care Component (PCC) is a clinical capture module of RPMS that captures outpatient data and contains tools for query and management reports.  Problem List uses some of IHS’s files as part of a joint-sharing between federal agencies.

Kernel	Kernel provides the computing environment for VistA software.

Lexicon	A terminology utility developed in conjunction with Problem List that can also be used by other applications; it was originally seeded with terminology from UMLS, and is supplemented by terms used within the VA Health Care System. When adding a problem to the Problem List, a clinician may be asked to select a term from the Lexicon.

MCCR	Medical Care Cost Recovery, a VistA module that contains various data entry methods to be used with clinical modules such as Problem List.

Menu	A particular type of Option or Protocol that leads the user to other Options or Protocols.

MTLU	Multi-Term Look-Up is part of the Kernel Toolkit and is used to by the Lexicon to conduct a “word search” of clinical terminology.

NTRT	New Term Rapid Turnaround (NTRT) is the process to distribute standard reference files to VistA and to HealtheVet environments.

OE/RR	Order Entry/Results Reporting is a module for managing orders (lab, radiology, etc.) and reporting back the results of such orders.  OE/RR was the predecessor for CPRS.

Option	An option is a part of the menu system that performs a function (action, print, edit, runs a routine, etc.).

PCE	Patient Care Encounter provides methods for capturing encounter data, so that clinicians, management, and Quality Assurance staff can benefit from the data.  The PCE package consists of a data capture module, links to VistA ancillary packages, V-files, and a Visit File.

PIMS	The VistA Patient Information Management System (PIMS) package provides a comprehensive range of software supporting the administrative functions of patient registration, admission, discharge, transfer, appointment scheduling, and beneficiary travel.  It provides service connection and special condition exposure support to the Problem List.

Problem	The term that the clinician gives to a patient’s complaint or diagnosis.

Progress Note	A VistA module, as well as a non-computerized form for maintaining text about a patient’s conditions.  The Text Integration Utility (TIU) provides the support for storing and retrieving the Progress Notes, and for the management of the notes.

Protocol	Similar to an option, a protocol contains the actions and methods required for accomplishing an order and orderables within List Manager versions of CPRS, Problem List, and other applications.  Once invoked, it will lead a user through a process to complete the order.

Remote Procedure Call	A Remote Procedure Call (RPC) is a procedure invoked by a client workstation to be executed by the server and the results will be returned to the client application.  RPCs are used to move Problem List data between the server and CPRS GUI.

Remote Data View	Remote Data View is the ability to view Problem List on a patient from the patient record at a remote treating facility by using Health Summary Problem List components.  This is only available after patches OR*3*85 and GMTS*2.7*29.

Security Key	Security Keys define the characteristic(s), authorization(s), or privilege(s) of the person exercising the Problem List.

SNOMED-CT	Systematic Nomenclature of Medicine Clinical Terms is a standardized, highly specialized vocabulary used to represent clinical information consistently and comprehensively as part of the electronic health record. In the United States, SNOMED CT is one of the US national standard for categories of information in electronic health records and for health information exchange transactions. It was originally created by the College of American Pathologists

TIU	The Text Integration Utility is a VistA module designed to manage the capture, retention, retrieval and processing of any patient-visit-oriented document (i.e., Discharge Summaries, Progress Notes, Consult Results, etc.).

UMLS	Unified Medical Language System, published by the National Institute of Health (NIH), National Library of Medicine (NLM).

Unwinder	The Unwinder is part of the Kernel VistA module. It allows hierarchical traversing of menus (as found in Menu Management) and the structuring of order protocols into reusable modules.

VA Fileman	VA FileMan is a database management system that maintains the data dictionary and provides utilities for input and output of data.