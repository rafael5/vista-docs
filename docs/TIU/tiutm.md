---
app_name: 'CPRS: Text Integration Utility (TIU)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: TIU
patch: null
patch_gap: null
section: ''
source_file: tiutm.docx
status: draft
title: 'of Unused Titles  :       1319'
---

## Department of Veterans Affairs
Text Integration Utilities (TIU)
Technical Manual

<!-- image -->

December 2025


Revision History

| Date           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Author/Project Manager   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| December 2025  | Patch TIU*1.0*372:  Added TIU*1.0*372 to the list of Recently Released Patches  Updated Creating Additional Medications Objects section for text, tables, and examples  Updated headings globally per 508 compliance                                                                                                                                                                                                                                                                                      | CPRS Development Team    |
| March 2025     | Patch TIU*1.0*360:  Added TIU*1.0*360 to Recently Released Patches  Added temporary protocols:  - TIU AVATAR MDM EVENT - TIU AVATAR MDM SUB                                                                                                                                                                                                                                                                                                                                                               | CPRS Development Team    |
| August 2024    | Patch TIU*1.0*318:  Added TIU*1.0*318 to the list of Recently Released Patches  Added TIU GET PRF ACTIONS to the Remote Procedure Calls table                                                                                                                                                                                                                                                                                                                                                             | CPRS Development Team    |
| December 2023  | Patch TIU*1.0*357:  Added TIU*1.0*357 to the list of Recently Released Patches  Added Appendix C: Additional Signer Utility Guide                                                                                                                                                                                                                                                                                                                                                                         | CPRS Development Team    |
| October 2023   | Patch TIU*1.0*359:  Under Recently Released Patches, added  TIU*1.0*359 functionality                                                                                                                                                                                                                                                                                                                                                                                                                     | CPRS Development Team    |
| May 2023       | Patch TIU*1.0*343:  Under Recently Released Patches, added TIU*1.0*343 functionality                                                                                                                                                                                                                                                                                                                                                                                                                      | CPRS Development Team    |
| March 2023     | Patch TIU*1.0*355:  Added TIU*1.0*355 to the list of Recently Released Patches  Added and updated example of Help Text in Basic TIU Parameters  Updated title page, footers, TOC, and index                                                                                                                                                                                                                                                                                                               | CPRS Development Team    |
<!-- rpc-table -->
| September 2022 | Patch TIU*1.0*289:   Under Recently Released Patches, added TIU*1*289 functionality.  Added descriptions for two Remote Procedure Calls (RPC)  - TIU NEED TO SIGN - TIU ONE VISIT NOTE                                                                                                                                                                                                                                                                                                                    |                          |
| November 2021  | Patch TIU*1.0*341:   Added the Troubleshooting the TIU ACTIONS RESOURCE Device section.                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |
| November 2021  | Patch TIU*1.0*338:  Under 1.3.1 Recently Released Patches, added Patch TIU*1.0*338 functionality  Under 2.2 Setting Up TIU/4  TIU Template Mgmt Functions, added lines 4 and 5  Under 4. Menu and Option Assignment/Text Integration Utilities (MIS Manager), revised naming of 16 Copy/Paste Tracking Report Export  Updated TOC and dates on Title page and in footers.                                                                                                                                 |                          |
| April 2021     | Patch TIU*1.0*330:  Under Section 1.3.1, Recently Released Patches:  - Added description of Patch TIU*1.0*330 which adds a new Document Class (EHRM CUTOVER (PARENT FACILITY NAME) and two new note titles - Complete 508 accessibility  Globally updated dates on Title page and in footers                                                                                                                                                                                                              |                          |
| November 2020  | Patch TIU*1*336  Corrected the oversight in ALLMEDS parameter #1: Added Clinic Meds to it,  iii  This correction, related to TIU*1.0*290, was incorporated into the TIU*1.0*336 release..  Made the manual 508-compliant.                                                                                                                                                                                                                                                                                 |                          |
| November 2020  | Patch TIU*1*328  Under Section 1.3.1, Recently Released Patches, added paragraph describing Patch TIU*1*328 update.  Under Section 11, Glossary, added Prescription Drug-Monitoring Program PDMP acronym.                                                                                                                                                                                                                                                                                                 |                          |
| October 2020   | Patch TIU*1.0*333  This patch fixes an issue with HL7 message for the OEHRM project. Specifically, when an addendum is signed it was previously completing the parent consult when the parent document was not yet completed. This was remedied to complete only the addendum.  See Recently Released Patches – October 2020 update                                                                                                                                                                       |                          |
| September 2020 | Patch TIU*1*290 – Added to the entry about ALLMEDS,  iii  Added a Protocols section, including some information regarding what to do if the TIU ACTIONS RESOURCE device becomes backed up, 175  Added an overview of changes for TIU under Recently Released Patches: page 5                                                                                                                                                                                                                              |                          |
| June 2020      | Patch TIU*1*290 – Updated Copy/Paste Tracking information for Basic TIU Parameters on page 15, Document Parameter Edit on page  56  , and Copy/Paste Tracking Reports ... [TIU COPY/PASTE REPORTS MENU] on page  124  Added information about setting Consult templates to read only on page86. Also under Menu Option Assignment on page 126.  Added an entry for TIU TEMPATE file definition.  Added an overview of changes for TIU under Recently Released Patches: page  7                            |                          |
| Oct 2019       | Patch TIU*1.0*324  Addresses functionality issues found with patch TIU*1.0*296, TIU TEXT EVENTS.  Updates:  - Recently Released Patches - May 2019 Update - Notes under March 2016 &amp; Setting Up TIU Text Events.  TIU File Descriptions: 8925.71 TIU TEXT EVENTS                                                                                                                                                                                                                                      |                          |
| January 2019   | Patch TIU*1*305 – Additional information provided about the Downtime Bookmark progress note boilerplate text  Updated Page  9                                                                                                                                                                                                                                                                                                                                                                             |                          |
| December 2018  | Patch TIU*1*305 – Enables sites to add a Downtime Bookmark progress note to the electronic record of all inpatients and outpatients who were seen during computer system downtime, and enables clinicians to create progress notes that automatically generate an alert to designated recipients based on the progress note title.  Updated Pages  5  ,  15  ,  16  ,  66  ,  69  -  72  ,  77  ,  79  ,  99  ,  108  ,  110  ,  114  ,  127  ,  228  ,  232  ,  **Error! Bookmark not defined.**  ,  261 |                          |
| July 2018      | Patch TIU*1*321 – Corrected the appropriate “April” entries to “may”                                                                                                                                                                                                                                                                                                                                                                                                                                      |                          |
| April 2017     | Patch TIU*1*309 – This patch will add a new coding system field (sub-multiple) to the following file: TIU VHA ENTERPRISE STANDARD TITLE file (#8926.1) (field #2). Updates applied to Sections: “Recently Released Patches” sub section “April 2017 Updates.” Page 3, and “Cross-references” sub section “8926.1 TIU VHA ENTERPRISE STANDARD TITLE File“ page 150 of the current version.                                                                                                                 |                          |
| March 2017     | With patch TIU*1*308, the reference to File 8625 changed to 8925 on Page 25. Also fixed potential PII changes on Page 84.  Updated Pages 25, 84.                                                                                                                                                                                                                                                                                                                                                          |                          |
| April 2016     | Patch TIU*1*291 – This patch introduces the new Crisis Notes, Warnings Notes, Allergies and/or Adverse Reactions, and Advance Directives (CWAD) auto-demotion functionality.  Updated Pages 2, 124, and 128                                                                                                                                                                                                                                                                                               |                          |
| March 2016     | Patch TIU*1*296 –  Modifies the TIU application to send a TIU alert to the appropriate service providers immediately after a staff member screens a patient and signs the associated note.  Updated Pages  11  ,  16  , 108, 110, 113, 126                                                                                                                                                                                                                                                                |                          |
| March 2014     | TIU*1*263 – ICD-10 Remediation                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                          |
| November 2013  | Updated with Missing Patient, Patient Record Flag patch information (Recently Released Patches section.) Added text about Patch TIU*1*279 to November 2013 update in recently release patches section. Page 3                                                                                                                                                                                                                                                                                             |                          |
| February 2013  | Added text about TIU parameters. Page 21                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                          |
| November 2012  | Added text re adding owner to TIU HS Object  Page 77                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                          |
| June 2012      | Patch 265 (PRF CAT I - HIGH RISK FOR SUICIDE)  Page 12                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                          |
| January 2012   | Patch 252 (GET TIU TEMPLATE INFORMATION)  Page 166  Error! Bookmark not defined.                                                                                                                                                                                                                                                                                                                                                                                                                          |                          |
| May 2011       | Patch 241 (TIU Nightly Task) Pages 14 , 173                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                          |
| May 2011       | Patch 248 (Missing Text Cleanup) Pages  207                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                          |
| June 2010      | Patch 250 (Line Count) Pages 92, 94, 122, & 128                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                          |
| August 2007    | Patch 222 (Work Copy Footer) Page 47                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                          |
| November 2006  | Patch 211 (Data Standardization VUID Patch)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                          |
| September 2006 | Patch 200 (HL7 Generic Interface)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                          |
| September 2006 | Patch 214 (Mismatched ID Notes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                          |
| June 2006      | Patch 218 (Active Title Cleanup Clarification)                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                          |
| April 2006     | Patch 189 (Expected Cosigner Report)                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                          |
| April 2006     | Patch 209 (Active Title Cleanup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                          |
| Aug 2005       | Patch 186 (Note Retention)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                          |
| Apr 2005       | Patches 180 (Signed/Unsigned Note Report & Update)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                          |
| Apr 2005       | Patch 173 (Unknown Addenda Cleanup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                          |
| March 2005     | Patch 157 (Additional Signer Changes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                          |
| Nov 2004       | Patches 174 & 177 (Blank Note)                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                          |
| August 2004    | Patch 185 (Reassign Report)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                          |
| March 2004     | Patch 112 (Surgery)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                          |
| February 2004  | Patch 113 (Multidivisional)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                          |
| October 2003   | Patch 159 (WRISC)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                          |
| June 2003      | Patch 158 (Alert Tools)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                          |
| May 2003       | Patch 135                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                          |
| July 2002      | Patch 131                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                          |
| November 2001  | Patches 122 & 126                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                          |
| August 2001    | Patch 110                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                          |
| April 2001     | Patches 61, 95, 100 & 105                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                          |
| June 2000      | Miscellaneous patches                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                          |
| July 1997      | Originally released                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                          |

Table of Contents

Introduction	1

Purpose of TIU	1

Functional Overview	1

Recently Released Patches	2

Implementation &amp; Maintenance	14

Pre-Implementation Considerations	14

Setting Up TIU	15

Document Definition Terminology	73

Matrix of Actions allowed per Status and Ownership	74

Creating Objects	75

Authorization/Subscription Utility (ASU)	83

Progress Notes Print Options	89

Exported Routines	96

TIU*1*211 TIU Data Standardization Vuid Patch	96

Menu and Option Assignment	121

Suggested Clinical Coordinator Menu	127

Menu Assignment	127

Actions/Functions Across Applications	129

TIU File Descriptions	139

Cross-References	143

TIU DOCUMENT File (#8925)	143

8925.1TIU DOCUMENT DEFINITION File	152

8925.2TIU UPLOAD BUFFER File	154

8925.3TIU UPLOAD ERROR DEFINITION File	154

8925.4TIU UPLOAD LOG File	154

8925.5TIU AUDIT TRAIL File	154

8925.6TIU STATUS File	155

8925.7TIU MULTIPLE SIGNATURE File	155

8925.8TIU SEARCH CATEGORIES File	155

8925.9TIU PROBLEM LINK File	156

8925.91TIU LINK File	156

8925.93TIU PRINT PARAMETERS File	156

8925.94TIU DIVISION PRINT PARAMETERS File	156

8925.95TIU DOCUMENT PARAMETERS File	157

8925.97TIU CONVERSIONS File	157

8925.98TIU PERSONAL DOCUMENT TYPE LIST File	157

8925.99TIU PARAMETERS File	157

8926TIU PERSONAL PREFERENCES File	157

8926.1TIU VHA ENTERPRISE STANDARD TITLE File	158

8926.2TIU LOINC SUBJECT MATTER DOMAIN File	159

8926.3TIU LOINC ROLE File	159

8926.4TIU LOINC SETTING File	160

8926.6TIU LOINC DOCUMENT TYPE File	161

8926.72TIU LOINC SMD SYNONYMS File	161

8926.73TIU LOINC ROLE SYNONYMS File	162

8926.74 TIU LOINC SETTING SYNONYMS File	162

8926.75 TIU LOINC SERVICE SYNONYMS File	162

8926.76TIU LOINC DOCUMENT TYPE SYNONYMS File	162

8927TIU TEMPLATE File	162

8927.1TIU TEMPLATE FIELD FILE File	163

Archiving and Purging	164

External Relations, RPCs, and APIs	165

Database Integration Agreements	166

Package-Wide Variables	176

Online Documentation	177

Intranet WWW Documentation	177

KIDS Install Print Options	177

Print Results of the Installation Process	178

XINDEX	180

Data Dictionaries/ Files	180

Glossary	181

NAME	185

OBJECT NAME	186

TYPE	186

SHARED	189

NATIONAL STANDARD	190

Troubleshooting &amp; Helpful Hints	204

FAQs (Frequently Asked Questions)	204

Facts Helpful information	213

ASU and User Class Information	223

Amount of Set-up for User Class &amp; Business Rules	224

Appendix A: TIU Package Security	226

Security Key	226

User Class Assignment and Document Definition Ownership	226

Menu Assignment	227

Appendix B: Creating an Object	228

Create a very simple Object.	228

Testing the Object	232

Making the Object More Realistic	237

Testing the More Realistic Object	240

Activating the object	243

Entering a Progress Note using the Object	244

Action Descriptions	249

Creating Additional Medications Objects	252

Creating an Object Based on Health Summary	259

Appendix C: Additional Signer Utility Guide	272

Introduction	272

Version 2.0	272

General Information	274

Options	276

Importing into Excel	281

Terminal Settings – Logging and Terminal Display	282

Index	285

### Introduction

#### Purpose of TIU

Text Integration Utilities (TIU) is a set of software tools designed to handle clinical documents in a standardized manner, with a single interface for viewing, entering, editing, and signing clinical documents. The initial release of TIU will incorporate the Discharge Summary and Progress Notes packages.

#### Functional Overview

Although TIU was released initially with Discharge Summary and Progress Notes, it has been designed to meet the needs of other clinical applications that address document handling.

TIU supports the following:

- Upload of ASCII formatted documents into V *IST* A
- Uniform file structure for storage of documents

Clinical documentation resides in a single location within the database. This permits ease of inquiry for such uses as Incomplete Record Tracking, quality management, results reporting, order checking, research, etc.

- Consistent file structure for defining elements and parameters of a document
- Expanded user actions; integrated user interface for various document types, if desired
- Management of document types
    - Entry, edit, deletion, printing, and viewing of the Document Definition hierarchy structure and its elements
    - Definition of components
    - Shared components
    - Ownership (personal or class) of document definitions
    - “Locking” and National Standard of document definitions
    - Boilerplate Text functionality
    - Interdisciplinary Notes consisting of a main note (parent) with related notes (children) attached to it.
    - Management functions
    - Amendment
    - Deletion
    - Identification of signature
    - Re-assignment
    - Purge
- Support of various Health Summary components
- Flexibility

The utility has been designed to accept document input from a variety of data capture methodologies. Those initially supported are transcription and direct entry.

- **Linkages**

TIU has interfaces with such applications as Problem List, Patient Care Encounter/Visit Tracking, Incomplete Record Tracking, and the Computerized Patient Record System (CPRS).

#### Recently Released Patches

##### December 2025 Update

- Patch TIU*1*372 deprecates the TIULMED routine(s) and provides support for the new TIUMOBJ routine(s). The Creating Additional Medication Objects section has the following updates:
    - Updated routine information and parameters table
    - New Medication Object Utility
    - Examples of Object Creation

##### March 2025 Update

- Patch TIU*1*360 makes the following changes:
    - Modified the TIU interface to capture dispensing information from Methadone Opioid Treatment Program (OTP) systems. The dispense information captured will be filed in the OTP MEDICATION DISPENSE file (#101.22).
    - Adds new temporary Protocols:
        - TIU AVATAR MDM EVENT
        - TIU AVATAR MDM SUB

##### August 2024 Update

- Patch TIU*1*318 is released in conjunction with the Computerized Record System (CPRS) v33 updates. The following change is being made with these patches:
    - Modified the RPC call TIU GET PRF ACTIONS. This allows the addition of the “Originating Facility” data to the call so that it can be displayed by CPRS in Progress Notes Properties.

**Note** : This RPC call was originally added in a prior patch but was left out of the manual.

##### December 2023 Update

- Patch TIU*1*357 makes the following changes:
    - Adds the Additional Signer Utility in an appendix, and updates the utility to include a version 2.0.

##### October 2023 Update

- Patch TIU*1*359 makes the following changes:
    - Adds a new API – CRTIUHS^TIUCROBJ – that will allow programmatic creation of a TIU object that calls a Health Summary object, commonly known as a TIU/Health Summary object.
    - Creates the following TIU/Health Summary objects:
        - VA-MAS DEM GENDER IDENTITY
        - VA-MAS DEM PRONOUNS
        - VA-MAS DEM SEXUAL ORIENTATION

##### April 2023 Update

- Patch TIU*1*343 makes the following changes:
    - Provides conditional auditing to the TIU DOCUMENT file along with new functionality to access audit information for a document. Auditing will be performed on signed (legally authenticated) documents.
    - A new Option, TIU FM AUDIT VIEWER has been added. This will be assigned to whatever Health Information Management (HIM) staff that will be performing a periodic check of this audit.

##### March 2023 Update

- Patch TIU*1.0*355  is released in conjunction with the Computerized Patient Record System (CPRS) patch OR*3.0*596. The following changes are released with these patches:
    - Update in 3 Remote Procedure Calls (RPC) in CPRS for NEW PERSON lookups
        - ORWU NEWPERS
        - ORWTPP GETCOS
        - ORWU2 COSIGNER
    - Help Text is added to select division-wide parameters

##### September 2022 Update

- Patch  TIU*1*289 makes the following changes:
    - When a document is reassigned, the process used to be tasked, but it is no longer tasked
    - A new Remote Procedure Call (RPC) TIU NEED TO SIGN was added to check whether a user’s signature is required when the notification is processed. If the signature is not required AT THIS TIME, CPRS will delete the notification, which may be regenerated.
    - Added the status of ACTIVE/PARKED to the National TIU Object for Medications.
    - Modified the TIU ONE VISIT NOTE RPC that checks the ALLOW &gt; 1 NOTE PER VISIT parameter is ignored for any title in the DISCHARGE SUMMARY class and document class and will always return 0 (NO).

##### November 2021 Update

- Patch TIU*1*338 releases new Copy/Paste Tracking functionality, as well as a corresponding report to assist with review processes based on the Copy/Paste Tracking data available. The patch also provides a new option that delivers the functionality for users to analyze, report, and fix entries in the TIU TEMPLATE (#8927) file for long lines that may cause wrapping issues when placed into a document. The new option TIU ANALYZE/UPDATE FILE 8927 has been added to the "TIU Template Mgmt Functions" [TIU IRM TEMPLATE MGMT] menu.

The patch fixes an issue when resolving filing errors that occur when uploading transcribed progress notes. Previously, certain filing errors were not able to be easily resolved from the view alert. This issue has been resolved with this patch.

- Patch TIU*1*341 enables users to clear the backlog if the TIU ACTIONS RESOURCE is backed up with numerous tasks.  For more information, see the Troubleshooting the TIU ACTIONS RESOURCE Device section.

##### April 2021 Update

- Patch  TIU*1*330 creates a new document class, EHRM CUTOVER (DOCUMENT CLASS) and two new note titles during the post-installation of this patch:
    - EHRM CUTOVER &lt;Site Name&gt;
    - EHRM CUTOVER REMINDERS &lt;Site Name&gt;

##### November 2020 Update

- Patch TIU*1*328 will install a new Document Class PDMP TITLES and a new Document Title STATE PRESCRIPTION DRUG MONITORING PROGRAM in ACTIVE state and mapped to VHA ENTERPRISE STANDARD TITLE “MEDICATION MGT NOTE.” If either the Document Class or Title already exist, no changes will be made to them.

##### October 2020 Update

- To support Spokane, Go-Live with Cerner as part of Office of Electronic Health Modernization (OEHRM) project, VistA patch TIU*1.0*333 fixes an issue with HL7 message for the OEHRM project. Specifically, when an addendum is signed it was previously completing the parent consult when the parent document was not yet completed. This was remedied to complete only the addendum. The change was made to routine TIURS.

##### June 2020 Update

**Patch 290** (TIU*1*290 - CPRS V31.B - NOTE TITLES, COPY/PASTE AND BUG FIXES) updated the rules for national medication Patient Data Objects as follows:

Clinic medications are no longer grouped with inpatient medications.  An object that only displays inpatient medications will no longer display any clinic medications.

Existing objects that currently display both inpatient and outpatient medications will now display clinic medications in their own sub-heading.

National PDOs affected are:

ACTIVE MEDICATIONS

ACTIVE MEDS COMBINED

DETAILED ACTIVE MEDS

DETAILED RECENT MEDS

RECENT MEDICATIONS

RECENT MEDS COMBINED

##### October 2019 Update

- TIU*1.0*324 addresses bugs reported with TIU TEXT EVENT functionality added with patch TIU*1.0*296.
- When the first IEN in file 8925.71 has INCLUDE SPACES = NO and the corresponding search text is not found in the note text, then no other TIU Events' search text will work. The 'Include Spaces' functionality is also flawed in that when it was set to NO, spaces were only stripped from the TIU Note text and not from the search text. This patch removes the prompt for INCLUDE SPACES from the option TIU TEXT EVENT EDIT and spaces will now be removed from both search text as well as TIU note text during the text search comparison.

- The Case Sensitivity functionality was not fully programmed and will be removed since case sensitivity would increase the odds of an alert not being sent due only to a case mismatch. This patch removes the prompt for CASE SENSITIVE from the option TIU TEXT EVENT EDIT and the search will not be case sensitive.

- When an addendum was signed it did not search for any text in that addendum because the parent IEN was passed to the routine instead of the addendum's IEN. After the installation of this patch, post signature code will now need to be set to ‘D TASK^TIUTIUS($S($G(DAORIG):DAORIG,1:DA))’ in order to correctly search either a parent note or addendum when each is signed.

##### March 2019 Update

This patch is released in conjunction with the Computerized Patient Record System (CPRS) version 31b release. It is bundled along with OR*3.0*377.  Please refer to the install guide referenced later in this

description for specific installation instructions.

This patch installs the following document class and note titles:

###### System for Mammogram Tracking (SMART) Notifications

SMART is a new optional alert processing system for breast imaging exam follow-up. It assists providers in documenting the results of breast imaging exams, communicating those results to the patient, and scheduling follow-up and/or future exams. The note titles below are used to capture the follow-up documentation.

**TIU DOCUMENT DEFINITION (8925.1)**

The new titles are attached to the new document class.

NAME                                            TYPE

----                                            ----

SMART NOTES                                     DOCUMENT CLASS

SMART BREAST IMAGINE FOLLOW-UP                  TITLE

SMART PATIENT NOTIFICATION                      TITLE

###### Women's Health High Risk Medications

The high risk medications functionality enables providers to document a patient's pregnancy and lactation status in the Women's Health software package. One feature of that functionality tracks the pregnancy and lactation status in other VistA software packages (such as Laboratory and Patient Care Encounter). When there is a mismatch, an alert is generated notifying case managers of such and will assist them in updating the status in the Women's Health software package. The note titles below are

used to capture this status change.

**TIU DOCUMENT DEFINITION (8925.1)**

The new titles are attached to the WOMEN'S HEALTH NOTES* document class.

*The WOMEN'S HEALTH NOTES document class should already be present in

File #8925.1.  If it is not present, the installation will abort so that

it may be added.

NAME                                            TYPE

----                                            ----

PREGNANCY STATUS UPDATE REVIEW                  TITLE

LACTATION STATUS UPDATE REVIEW                  TITLE

##### December 2018 Update

TIU*1.0*305 provides the following enhancements to VistA:

- Enables sites to add a progress note to the electronic record of all inpatients and outpatients who were seen during computer system downtime using the new option Contingency Downtime Bookmark Progress Notes [TIU DOWNTIME BOOKMARK PN] in the TIU Maintenance Menu [TIU IRM MAINTENANCE MENU]. The note must use a locally-approved title that has been mapped to the Veterans Health Administration (VHA) enterprise-standard COMPUTER DOWNTIME title. When creating the note, users can enter: the note title; whether the computer downtime was scheduled or unscheduled; outage start/end times; the author of the note; a date/time stamp to sequence the note in the note tree; clinics to which the outage applies; users to receive an email notification listing the patients affected and whether the note was successfully appended to each patient's record; an option to edit the TIU note text; and an electronic signature to perform an administrative closure of the note to enter it into the medical record. The progress note states that a computer outage occurred, and alerts the user to search the patient's paper records for non-electronic documentation created during the outage. The set-up and note content should be coordinated with the Chief, Health Information Management at each site. Only one progress note is filed for any patient with multiple appointments (whether inpatient, outpatient, or both) at different clinics during the outage period.

The patch deletes a site’s existing text in the BOILERPLATE TEXT field (#3) in the TIU DOCUMENT DEFINITION file (#8925.1) and replaces it with new standard TIU note text. This new text can be modified by users when creating downtime bookmark progress notes. The installation history for the patch will capture the data from the BOILERPLATE TEXT field so that local OIT personnel can retrieve the previous boilerplate text, if needed. The installation history can be reviewed using the Install File Print [XPD PRINT INSTALL FILE] option under the KIDS UTILITIES sub-menu.

**NOTE:** The use of this functionality is optional; therefore, the boilerplate text will not initially be stored in the document definition until the first use of the option to implement the functionality.  After the first use, the boilerplate text will be stored and can be edited via the usual TIU document definition edit options.

- Enables clinicians and providers to create progress notes that automatically generate a post-signature alert to designated recipients based on the progress note title. The new option Create Post-Signature Alerts [TIUFPC CREATE POST-SIGNATURE] in the Document Definitions (Manager) [TIUF DOCUMENT DEFINITION MGR] menu allows Clinical Application Coordinators (CACs) or other supervisors to define who is alerted when a specific progress note title is used. The note title to define is selected at the "Select TIU DOCUMENT DEFINITION NAME:" prompt. The option then enables entry of the recipients to be notified (individual, mail group, or team list), whether to alert the Primary Care Provider, whether to print a chart copy at the patient's location, and to optionally select an output device for printing at another location. This data is used to populate a MUMPS subroutine name in the POST-SIGNATURE ACTION field (#4.9) for a document definition in the TIU DOCUMENT DEFINITION file (#8925.1). The notification is made through VistA Kernel Alerts and is sent to recipients immediately upon a clinician's entry of an electronic signature for the note.

##### April 2017 Update

Patch TIU*1*309 will add a new field CODING SYSTEM (#2) SUB-multiple to the TIU VHA ENTERPRISE STANDARD TITLE file (#8926.1) for the purpose of interoperability. The TIU VHA ENTERPRISE STANDARD TITLE file (#8926.1) shall be updated to include a new field to store LOINC code field from the respective Standards Development Organizations.

This patch also fixes the &lt;UNDEFINED&gt;BULL+9^TIUDD61 error reported in Remedy Ticket #241480, which occurs when a New Term Rapid Turnaround (NTRT) deployment doesn't modify the ACTIVATION STATUS (subset of EFFECTIVE DATE/TIME (#99.991)) of any of the VHA ENTERPRISE STANDARD TITLE (# 8926.1) in the target VistA system (e.g., a deployment is sent to the same VistA domain more than once, or a deployment which changes properties without activating or inactivating any titles). This Patch is from the Text Integration Utilities Package.

Patch XU*8.0*675 distributes the parameters required by Master File Server (MFS) to support data standardization messaging.

1. Updates the entry TIU Titles (#8926.1) on the MASTER FILE PARAMETERS file (#4.001).

2. Updates the entry TIU Titles (#8926.1) on the MD5 Signature file (#4.005).

TIU VHA Enterprise Standard Title File Update. Patch TIU*1.0*309 will add a new field Coding System multiple to files TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) for the purpose of interoperability. TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) file shall be updated to include a new field to store LOINC code field from the respective Standards Development Organizations. This field will be added to the TIU Enterprise Standard Title File (#8926.1).

##### April 2016 Update

Patch TIU*1*291 introduces the new Cautions, Warnings, Adverse Reactions, and Directives (CWAD) notes auto demotion functionality. CWAD is a section of CPRS used for posting progress notes, which are more important than standard level notes. These progress notes are made more easily available throughout CPRS. The postings dialog box can become full of CWAD notes, resulting in important notes from being easily distinguishable from less important notes. The requested enhancement is to demote previously designated notes from the CWAD postings to a regular note status when a newer note, of a particular title, is written which supersedes the existing CWAD note. This is accomplished by converting an existing Class III application to Class I. A new parameter definition (TIU CWAD EXCLUDED TITLES) and three default parameter entries are included in this release as well as one new option (CWAD/Postings Auto-Demotion Setup [TIU CWAD AUTO-DEMOTION]) Two new routines will drive this new functionality.

The TIU CWAD EXCLUDED TITLES parameter is used to prevent specific CWAD titles from being selected for auto-demotion. What is entered is the VHA Enterprise Standard Title from TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) file. Any CWAD related title in the TIU DOCUMENT DEFINITION (#8925.1) file which is mapped to an excluded VHA Enterprise Standard Title will not be selectable as an auto-demotion CWAD title. At the guidance of the National Center for Ethics in Health Care, we are defaulting three VHA Enterprise Standard Titles to be excluded from the CWAD Auto-Demotion functionality. These are ADVANCE DIRECTIVE, ADVANCE DIRECTIVE DISCUSSION, and RESCINDED ADVANCE DIRECTIVE. These titles should not be removed without prior guidance.

The CWAD/Postings Auto-Demotion Setup [TIU CWAD AUTO-DEMOTION] option is added as a new menu item of the Text Integration Utilities (MIS Manager) [TIU MAIN MENU MGR] menu option.

##### March 2016 Update

Patch TIU*1*296 modifies the TIU application to send a TIU alert to the appropriate service provider(s) immediately after a staff member screens a patient and signs the associated note. The service provider(s) will be alerted prior to the note being co-signed by the licensed clinician responsible for reviewing and approving the note. Prior to this modification, TIU alerts were not sent to all service providers. This resulted in missed opportunities to provide needed services for patients while the patients are on site, and forced staff to take time to contact patients and reschedule needed services.

This patch utilizes one new file (TIU TEXT EVENTS (#8925.71)) used to define the words or phrase that will be searched for in a TIU document (progress note, consult, etc.). If the words or phrase are found in the TIU document, then an alert is sent to the team(s) specified in the TIU TEXT EVENTS file. A Text Event Edit [TIU TEXT EVENT EDIT] menu option was added to the TIU Maintenance Menu [TIU IRM MAINTENANCE MENU]. This option is used to set up a text event in the TIU TEXT EVENTS file.

**NOTE:** Any TIU document that is to be used to trigger these alerts must have the MUMPS code D TASK^TIUTIUS($S($G(DAORIG):DAORIG,1:DA)) entered in the POST-SIGNATURE CODE field (#4.9) in the TIU DOCUMENT DEFINITION file (#8925.1).

##### March 2014 Update

Patch TIU*1*263 patch is part of the Computerized Patient Records System CPRSv30  project. This project will modify the Computerized Patient Record  System, Text Integration Utilities, Consults, Health Summary, Problem List, Clinical Reminders, and Order Entry/Results Reporting to meet the requirements proposed by the Dept. of Health and Human Services to adopt ICD-10 code set standards for Clinic Orders.

This patch makes all changes to TIU that are required to move from the ICD-9 coding version to ICD-10.  The patch is being distributed as a host file.

##### November 2013 Update

Patch TIU*1*279 installs a new TIU DOCUMENT DEFINITION (file #8925.1) title: PATIENT RECORD FLAG CATEGORY I – MISSING PATIENT to be used with the new MISSING PATIENT, Patient Record Flag. The patch links this new title to the existing document class PATIENT RECORD FLAG CAT I.

##### December 2012 Update

Patch TIU*1*265 installs a new TIU DOCUMENT DEFINITION (file #8925.1) title: PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE to be used with the new Patient Record Flag. The patch links this new title to the existing document class PATIENT RECORD FLAG CAT I.

- Remedy ticket **#781752** reported that Imported TIU-HS OBJECT won’t preview – problem of “NO OWNER.” Since a national coding solution can’t easily be made, instructions have been added to the TIU Technical Manual to describe how to resolve this at local sites.

##### January 2012 Update

- Patch TIU*1*252 supports the Dental Package and is released in conjunction with patch DENT*1.2*59.
- Patch TIU*1*252 provides Remote Procedure Call (RPC) TIU TEMPLATE GET TEMPLATE which is used in DENT*1.2*59. It returns basic information about a given template in the TIU TEMPLATE FILE [#8927].
- Patch TIU*1*261, which was released in March 2012, supports Imaging patch MAG*3.0*121. Patch MAG*3.0*121 provides the ability to watermark images "RESCINDED."
- Patch TIU*1*261 permits an authorized user to rescind an Advance Directive document by changing the title to RESCINDED ADVANCE DIRECTIVE.
- MAG*3.0*121 takes it from there and watermarks any linked images "RESCINDED."

### Implementation &amp; Maintenance

See the *Text Integration Utilities Implementation Guide* for more detailed instructions about planning and setting up TIU.

#### Pre-Implementation Considerations

The TIU package contains many site-configurable features which should be considered before implementing it at your site. We recommend that each site consult a multidisciplinary committee composed of MAS and clinical service representatives, as well as individual services or product lines to define site parameters which reflect hospital-wide and service policies and practices. Some of the site-configurable features which must be addressed before implementation are:

- Conversion of Progress Notes and Discharge Summaries
- Document definition hierarchy
- User Class definition
- Document upload specifications
- Interdisciplinary Notes
- Signature, signature block, and electronic signature considerations
- Purging specifications
- Printer and printing definitions
- Clinician, MAS, and transcriptionist review/release issues

The following pages describe implementation processes.

#### Setting Up TIU

Options on the IRM Maintenance Menu let IRM Staff set and modify the various parameters controlling the behavior of the Text Integration Utilities Package, as well as the definition of TIU documents. These options are described in the following pages of this section.

TIU Maintenance Menu [TIU IRM MAINTENANCE MENU].

1    TIU Parameters Menu...[TIU SET-UP MENU]

1  Basic TIU Parameters [TIU BASIC PARAMETER EDIT]

2  Modify Upload Parameters [TIU UPLOAD PARAMETER EDIT]

3  Document Parameter Edit [TIU DOCUMENT PARAMETER EDIT]

4  Progress Notes Batch Print Locations [TIU PRINT PN LOC PARAMS]

5  Division - Progress Notes Print Params [TIU PRINT PN DIV PARAMS]

2    Document Definitions (Manager)...[TIUF DOCUMENT DEFINITION MGR]

1  Edit Document Definitions [TIUFH EDIT DDEFS MGR]

2  Sort Document Definitions/Objects [TIUFA SORT DDEFS MGR]

3  Create Document Definitions [TIUFC CREATE DDEFS MGR]

4  Create Objects  [TIUFO CREATE OBJECTS MGR]

5 Create TIU/Health Summary Objects

6 Create Post-Signature Alerts

3    User Class Management ...[USR CLASS MANAGEMENT MENU]

1  User Class Definition [USR CLASS DEFINITION]

2  List Membership by User [USR LIST MEMBERSHIP BY USER]

3  List Membership by Class [USR LIST MEMBERSHIP BY CLASS]

4  Edit Business Rules [USR EDIT BUSINESS RULES]

5  Manage Business Rules [USR MANAGE BUSINESS RULES]

4    TIU Template Mgmt Functions ... [TIU IRM TEMPLATE MGMT]

1  Delete TIU templates for selected user. [TIU TEMPLATE CAC USER DELETE]

2  Edit auto template cleanup parameter. [TIU TEMPLATE USER DELETE PARAM]

3  Delete templates for ALL terminated users. [TIU TEMPLATE DELETE TERM A

4  Set Consult templates to Read Only

5  Analyze/Update the TIU template file

5    TIU Alert Tools [TIU ALERT TOOLS]

6    Active Title Cleanup Report [TIU ACTIVE TITLE CLEANUP]

7    TIUHL7 Message Manager [TIUHL7 MSG MGR]

8      Title Mapping Utilities ...

9      Text Event Edit [TIU TEXT EVENT EDIT]

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13      Contingency Downtime Bookmark Progress Notes [TIU DOWNTIME BOOKMARK PN]

##### Setting TIU Parameters TIU Parameters Menu [TIU SET-UP MENU]

This menu contains options for setting up the basic parameters and upload parameters.

| Option                                     | Option Name                 | Description                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basic TIU Parameters                       | TIU BASIC PARAMETER EDIT    | This option allows you to enter the basic or general parameters that govern the behavior of the Text Integration Utilities.                                                                                                                                                                                                                                  |
| Modify Upload Parameters                   | TIU UPLOAD PARAMETER EDIT   | This option allows the definition and modification of parameters for the batch upload of documents into V  *IST*  A.                                                                                                                                                                                                                                         |
| Document Parameter Edit                    | TIU DOCUMENT PARAMETER EDIT | This option lets you enter the parameters which apply to specific documents (i.e., Titles), or groups of documents (i.e., Classes, or Document Classes).                                                                                                                                                                                                     |
| Division - Progress Notes Print Parameters | TIU PRINT PN DIV PARAM      | These parameters are used by the [TIU PRINT PN BATCH INTERACTIVE] and [TIU PRINT PN BATCH SCHEDULED] options. If the site desires a header other than what is returned by $$SITE^ VASITE the .02 field of the 1st entry in this file will be used.  For example, Waco-Temple-Marlin can have the institution of their progress notes as “CENTRAL TEXAS HCF.” |
| Progress Notes Batch Print Locations       | TIU PRINT PN LOC PARAMS     | Option for entering hospital locations used for [TIU PRINT PN OUTPT LOC] and [TIU PRINT PN WARD] options. If locations are not entered in this file they will not be selectable from these options.                                                                                                                                                          |

##### Basic TIU Parameters

This option allows you to enter the basic or general parameters which govern the behavior of the Text Integration Utilities.

**Example**

Select TIU Maintenance Menu Option: **1** TIU Parameters Menu

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

Select TIU PARAMETERS Menu Option **: BASIC TIU PARAMETERS** Basic TIU PARAMETERS

First edit Division-wide parameters:

Select INSTITUTION: **&lt;YOUR INSTITUTION NAME&gt;**

ENABLE ELECTRONIC SIGNATURE: YES// **??**

When set to 1, electronic signature will be enabled.  Prior to enabling

electronic signature, it will be assumed that signatures are to be

written on the chart copy of VAF 10-1000.

Choose from:

1        YES

0        NO

ENABLE ELECTRONIC SIGNATURE: YES// **&lt;Enter&gt;**

ENABLE NOTIFICATIONS DATE:// **??**

Examples of Valid Dates:

or  or  or 012057

T   (for TODAY),  T+1 (for TOMORROW),  T+2,  T+7,  etc.

T-1 (for YESTERDAY),  T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

When set to a valid date, notifications of Documents which

are available or overdue for signature will be sent to the user whose

signature is missing (i.e., either author or attending physician).

ENABLE NOTIFICATIONS DATE: // **&lt;Enter&gt;**

GRACE PERIOD FOR SIGNATURE: 7// **??**

This is the number of days following transcription before an author or

Attending Physician will be notified of a deficiency.

GRACE PERIOD FOR SIGNATURE: 7// **&lt;Enter&gt;**

GRACE PERIOD FOR PURGE: 100// **??**

This is the number of days following transcription for which a report

will be kept, prior to purge.

GRACE PERIOD FOR PURGE: 100// **&lt;Enter&gt;**

CHARACTERS PER LINE: 60// **??**

This value (default 60) will be divided into the total number of

'actual' characters in a given Documents to derive the line

count for that document.  By 'actual' characters, we mean all

printable ASCII characters, with multiple white space characters

stripped.

CHARACTERS PER LINE: 60// **&lt;Enter&gt;**

OPTIMIZE LIST BUILDING FOR: performance// ??

This parameter specifies for the institution in question whether the

list building functions of TIU should invoke Authorization/

Subscription to determine whether documents which the user is not yet

authorized to see should be excluded from the list (i.e., whether the

list building should be optimized for security). This is the default

behavior of TIU. If the impact of this "filtering" becomes

unacceptable to users at your site, you may wish to set this parameter

to optimize for Performance, which will bypass the record-wise

evaluation of view privilege, and allow all records satisfying the

search criteria to be included in the list.  Of course, when the user

attempts to view documents from the resulting lists before he is

authorized to do so, he will be prevented from doing so, with an

explanatory message that looks like this:

Reviewing Item #1

You may not VIEW this UNSIGNED NURSE'S NOTE.

RETURN to continue... **&lt;Enter&gt;**

This feature is offered as a means of balancing the demands for rapid

response with the concerns of many facilities for control of access to

confidential information.

Choose from:

P        performance

S        security

OPTIMIZE LIST BUILDING FOR: performance// **&lt;Enter&gt;**

SUPPRESS REVIEW NOTES PROMPT: YES// ??

If this parameter is set to yes, TIU will suppress the prompt

indicating how many notes are available to the user, when entering a

indicating Progress Note.

Choose from:

1        YES

0        NO

SUPPRESS REVIEW NOTES PROMPT: YES// **&lt;Enter&gt;**

ENABLE CHART COPY PROMPT: **??**

This parameter is used to enable Medical Record Technicians and MIS

managers to be prompted whether prints of summaries are chart copies

or not. If not enabled, when MR Techs and MIS Mgr print summaries,

they will be chart copies.

Choose from:

1        YES

0        NO

ENABLE CHART COPY PROMPT: **&lt;Enter&gt;**

DEFAULT PRIMARY PROVIDER: DEFAULT, BY LOCATION// **?**

Please indicate the source of the default for Primary Provider.

Choose from:

0        NONE, DON'T PROMPT

1        DEFAULT, BY LOCATION

2        AUTHOR (IF PROVIDER)

DEFAULT PRIMARY PROVIDER: DEFAULT, BY LOCATION// **&lt;Enter&gt;**

BLANK CHARACTER STRING: **??**

This is a special string of characters which should be used by the

transcriptionist to represent a "blank."  i.e., a word or phrase in

the dictation which could not be understood and included in the

transcription.

BLANK CHARACTER STRING: **@@@**

START OF ADD SGNR ALERT PERIOD: **??**

This is the start date for evaluating documents that have overdue

Additional signatures. The value must be in a FileMan date range format

such as 6D, 3W or 4M. If this field is left blank, all documents

evaluated that have a date less and the END OF ADD SGNR ALERT PERIOD

date will be included.

Since the addition of the LENGTH OF SIGNR ALERT PERIOD parameter this

Field should be set to the same value as that field. If LENGTH OF

SIGNER ALERT PERIOD is left blank then set this field to 12M, the

default value of the LENGTH OF SIGNER ALERT PERIOD when no value is

entered.  LENGTH OF SIGNER ALERT PERIOD determines how far back in time

Documents are evaluated.

START OF ADD SGNR ALERT PERIOD: **12M**

END OF ADD SGNR ALERT PERIOD: **??**

This is the length in time from the current date that the TIU NIGHTLY

TASK will stop regenerating alert for overdue additional signatures.

The value must be in a FileMan date range format such as 6D, 3W or 4M.

If no value is entered, the TIU Nightly TASK will search for documents

in the TIU DOCUMENT file (8926) up to the current date.

END OF ADD SGNR ALERT PERIOD: 2M

LENGTH OF SIGNER ALERT PERIOD: ??

This is the length of time that the TIU NIGHTLY TASK will go back prior

to "today" when searching for documents that have overdue signatures.

The value must be in a FileMan date range format such as 6D, 3W or 4M.

If no value is entered, the TIU NIGHTLY TASK will begin searching for

Document staring at 1 year prior to "today" in the DIT DOCUMENTS file (8925).

END OF ADD SGNR ALERT PERIOD: **12M**

ENABLE DICTATION CONTROL: **??**

A YES in this field will turn on dictation functionality introduced by

patch TIU*1*297.  A NO or lack of entry will turn off this dictation

functionality.

When dictation functionality is turned on and a progress note is started

and the phrase "TO BE DICTATED" is entered in the very first line by an

author who holds the TIUDCT security key, the entire note will be replaced

with dictation instructions taken from the DICTATION INSTRUCTIONS

Field (#6).

Choose from:

0        NO

1        YES

ENABLE DICTATION CONTROL: **&lt;Enter&gt;**

MINIMUM COPY WORDS: 10// **??**

This field defaults to 5 words if no value is set. As this determines

what is captured as copied text, this value can play a significant

role in what is tracked. The smaller this number, the more copy

actions will be captured. Each site will need to determine the

appropriate level of capture which is ideal for their individual

needs.

MINIMUM COPY WORDS: 10// **&lt;Enter&gt;**

COPY/PASTE VERIFY PERCENTAGE: 90// **??**

This field defaults to 90% if no value is set. This field plays a

significant part in determining when pasted text is identified as

originating from a previously captured copy action.  The higher the

percentage, the less likely pasted text will be identified as

originating from copied text.  Each site will need to determine the

appropriate level of percentage match which is ideal for their

individual needs.

COPY/PASTE VERIFY PERCENTAGE: 90// **&lt;Enter&gt;**

Select USERCLASS TO VIEW COPY/PASTE: CHIEF, MIS// **??**

Choose from:

CHIEF, MIS

CLINICAL COORDINATOR

You may enter a new COPY/PASTE USERCLASS, if you wish

This field is empty to begin. The copy/paste software will always

provide the "CHIEF, HIMS", "CHIEF, MIS", and the "PRIVACY ACT

OFFICER" userclasses as having the ability to view copy/paste

highlighting in CPRS. If sites wish to provide another userclass

these rights, then they should add an existing userclass to this

entry.

Choose from:

ALLERGIST

ANESTHESIOLOGIST

ASSOCIATE CHIEF OF STAFF

ATTENDING PHYSICIAN

AUDIOLOGIST

CARDIOLOGIST

CHAPLAIN

CHIEF RESIDENT

CHIEF, HIMS

CHIEF, MEDICAL SERVICE

CHIEF, MIS

CHIEF, PSYCHIATRY SERVICE

CHIEF, SURGICAL SERVICE

CLINICAL CLERK

CLINICAL COORDINATOR

CLINICAL DIETITIAN

CLINICAL PHARMACIST

Type &lt;Enter&gt; to continue or '^' to exit: **^**

Select USERCLASS TO VIEW COPY/PASTE: CHIEF, MIS// **&lt;Enter&gt;**

Press RETURN to continue... **&lt;Enter&gt;**

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select TIU Parameters Menu Option:

NOTE on *some* of the parameters discussed above:

Although these parameters are set at the division level, the TIU NIGHTLY TASK which determines when OVERDUE alerts are sent recognizes the parameters set for one division only: the division of the person who scheduled the Nightly Task.  This applies to the following parameters:

- **GRACE PERIOD FOR SIGNATURE:**
- START OF ADD SGNR ALERT PERIOD:
- **END OF ADD SGNR ALERT PERIOD** :
- **LENGTH OF SIGNER ALERT PERIOD** :

Help text has been added to the below division-wide parameters.

Select TIU Parameters Menu Option: 1  Basic TIU Parameters

First edit Division-wide parameters:

Select INSTITUTION:    CAMP MASTER

ENABLE ELECTRONIC SIGNATURE: YES//

ENABLE NOTIFICATIONS DATE: JAN 1,1996//

GRACE PERIOD FOR SIGNATURE: 5// ?

Enter the number of days to wait before notifying physician of an overdue

signature (1 to 10 days). Default is TODAY.

GRACE PERIOD FOR SIGNATURE: 5//

LENGTH OF SIGNER ALERT PERIOD: ?

This parameter determines how far back the TIU NIGHTLY TASK will look for

OVERDUE signatures.  Must be 1-4 NUMBERS followed by "D", "W", or "M".

Default is 12M.

LENGTH OF SIGNER ALERT PERIOD:

START OF ADD SGNR ALERT PERIOD: ?

Equivalent to LENGTH OF SIGNER ALERT PERIOD but for ADDITIONAL SIGNATURES.

Must be 1-4 NUMBERS followed by "D", "W" or "M". Default is 7D.

START OF ADD SGNR ALERT PERIOD:

END OF ADD SGNR ALERT PERIOD: ?

This is equivalent to the GRACE PERIOD FOR SIGNATURE for additional

signature.  Must be 1-4 NUMBERS followed by "D", "W", or "M". Default is

TODAY.

##### Implement Upload Utility

There are two steps to enable uploading of reports into **V** IST **A** .

###### Step 1: Set up your Terminal Emulator

###### Step 2: Enter Upload Utility Parameters

Examples of these two steps are given on the following pages. Two examples are shown for entering upload parameters—ASCII and Kermit. If you are using a commercial word-processing program, documents must be saved to ASCII format.

***Host File Server*** :

If the ASCII upload source is defined as (H)ost, data will be an ASCII host file such as VMS or DOS.

###### Remote Computer:

If the ASCII upload source is defined as (R)emote, data will be read from an ASCII stream coming to **V** IST **A** from a terminal emulator. You will select either a Kermit or RAW ASCII transfer protocol for your station. However, we strongly recommend that you use Kermit, as it provides for error correction and handles line noise much more effectively than the RAW ASCII.  If you plan to use the Kermit Protocol, skip to the set-up dialog..

NOTE:	If your site has chosen to have clinicians enter the documents directly into V *IST* A, then you needn’t implement the upload utility.

###### Step 1.  Set up a Terminal Emulator

Determine which type of terminal emulator your site plans to use.

###### Raw ASCII file transfer protocol

This example shows possible combinations of terminal and ASCII transfer options using the appropriate configuration utilities provided by your terminal emulation software.

TERMINAL OPTIONS

A - Terminal emulation . . . . . **VT100** K - EGA/VGA true underline . . . **ON**

B - Duplex . . . . . . . . . . . **FULL** L - Terminal width . . . . . . . **80**

C - Soft flow control (XON/XOFF) **ON** M - ANSI 7 or 8 bit commands . . **8 BIT**

D - Hard flow control (RTS/CTS). **OFF**

E - Line wrap. . . . . . . . . . **ON**

F - Screen Scroll. . . . . . . . **ON**

G - CR translation . . . . . . . **CR**

H - BS translation . . . . . . . **DESTRUCTIVE**

I - Break length (milliseconds). **2000**

J - Enquiry (ENQ). . . . . . . . **OFF**

A - Echo locally . . . . . . . . **NO** K - CR translation (download). . **NONE**

B - Expand blank lines . . . . . **YES** L - LF translation (download). . **NONE**

C - Expand tabs. . . . . . . . . YES

D - Character pacing (millisec). **0**

E - Line pacing (1/10 sec) . . . . **0**

F - Pace character . . . . . . . . **62** [ **NOTE:** This **MUST** correspond to the

PACE CHARACTER defined in the upload

utility parameter edit dialog below]

G - Strip 8th bit. . . . . . . . **NO**

H - ASCII download timeout . . . **60 seconds**

I - CR translation (upload). . . **NONE**

J - LF translation (upload). . . **OFF**

Also, be sure that the ASCII transfer option to “abort transfer if carrier detect (CD) is lost” is set to “NO.”

Because of the significantly greater reliability of the Kermit file transfer protocol, we recommend that you use it rather than the Raw ASCII protocol. Try using the default settings for packet size, timeout, start and end of packet characters, and checksum size, as provided by your terminal emulation software. The **V** IST **A** Kermit server should work properly with these settings.

###### Step 2.  Enter Upload Utility Parameters

Use the *Modify Upload Parameters* option located on the TIU Parameters menu to enter the upload utility’s parameters.

###### Modify Upload Parameters—ASCII Protocol Example

In this example, the ASCII upload source is a remote computer and the upload protocol is defined as an ASCII Protocol. To optimize reliability and functionality when using the ASCII Protocol, we recommend a direct line rather than a modem for transfer of data.

**Example**

Select TIU Maintenance Menu Option: **1** TIU Parameters Menu

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

Select TIU Parameters Menu Option: **2** Modify Upload Parameters

First edit Institution-wide upload parameters:

Select INSTITUTION: **YOUR HOSPITAL**

ASCII UPLOAD SOURCE: remote computer// **&lt;Enter&gt;**

UPLOAD PROTOCOL: **??**

This is the preferred upload protocol.

Choose from:

a        ASCII

k        KERMIT

UPLOAD PROTOCOL: **ASCII &lt;Enter&gt;**

PACE CHARACTER: **??**

This is the ASCII value of the character which VISTA will send to the

remote computer to acknowledge receipt of the last text line transmitted

and to prompt the remote to transmit another line.  If you are using the

same remote to upload both MailMan messages and textual reports, then we

PACE CHARACTER: **62**

END OF MESSAGE SIGNAL: **??**

This is the free text signal to the upload process that the entire

transmission is successfully finished, and no more lines of data need to

be read from the input stream.

END OF MESSAGE SIGNAL: **$END**

UPLOAD HEADER FORMAT: **??**

This field determines whether the ASCII protocol upload/router/filer will

expect delimited string or captioned formats for the header of each

report.


Choose from:

C        captioned

D        delimited string

UPLOAD HEADER FORMAT: **captioned**

RECORD HEADER SIGNAL: **??**

This is a free text signal to the upload process that a new report record

header has been encountered.  It will be as simple as the three-character

string "MSH" or as complex as "HEADERBEGIN". The signal used by the

Surgery Package option to transmit operative notes (i.e., "@@@") will

also

RECORD HEADER SIGNAL: MSH

BEGIN REPORT TEXT SIGNAL: ??

This is the signal to the upload processor that the fixed-field header

for a given report record has been fully read, and that the body of the

narrative report follows.

BEGIN REPORT TEXT SIGNAL: **$TXT**

RUN UPLOAD FILER IN FOREGROUND: **??**

This parameter specifies whether the filer for the upload process should

be run in the foreground, rather than in the background (i.e., as a

Task).

If no preference is specified the default will be to run the filer as a

BACKGROUND task.

Choose from:

1        YES

0        NO

RUN UPLOAD FILER IN FOREGROUND: **NO**

Now Select upload error alert recipients:

Select ALERT RECIPIENT: **CPRSRECIPIENT,ONE**

Are you adding 'CPRSRECIPIENT,ONE' as  a new UPLOAD ERROR ALERT RECIPIENT (the

1ST for this TIU PARAMETERS)? **Y** (Yes)

Select ALERT RECIPIENT: **&lt;Enter&gt;**

Now edit the DOCUMENT DEFINITION file:

Select DOCUMENT DEFINITION: **Discharge Summary**

1   Discharge Summary  DISCHARGE SUMMARY        TITLE

2   Discharge Summary  DISCHARGE SUMMARY        DOCUMENT CLASS

CHOOSE 1-2: **1** DISCHARGE SUMMARY

ABBREVIATION: **DCS**

LAYGO ALLOWED?: **??**

This Boolean field indicates whether or not a new entry can be created in

the TARGET FILE for this document type.

Choose from:

0        NO

1        YES

LAYGO ALLOWED?: **YES**

UPLOAD TARGET FILE: **??**

Enter the VA FileMan file in which the fixed-field header information and

associated text will be stored.

NOTE:  Only files which include the TIU Application Group will be

selected.

NOTE:  Upload fields (fields 1.01, 1.02, 1.03, 1.04, 4, 4.5, 4.6, 4.7,

4.8 and multiple fields 1 and 2) apply to Document Definitions of Type

Class, Document Class, and Title.

Choose from:

70              RAD/NUC MED PATIENT

74              RAD/NUC MED REPORTS

8925            TIU DOCUMENT

8925.1          TIU DOCUMENT DEFINITION

8925.97         TIU CONVERSIONS

UPLOAD TARGET FILE: **TIU DOCUMENT** 8925  TIU DOCUMENT

*Modify Upload Parameters—ASCII Protocol Example cont’d*

Select TARGET TEXT FIELD: **??**

Choose from:

These are field #s, which is why there isn’t a #1.

<!-- image -->

3               EDIT TEXT BUFFER

Select TARGET TEXT FIELD: **REPORT TEXT**

UPLOAD LOOK-UP METHOD: D LOOKUP^TIUPUTU// **&lt;Enter&gt;**

NOTE:

Some of these prompts and defaults only appear if you have programmer access.

<!-- image -->

Replace **&lt;Enter&gt;**

UPLOAD FILING ERROR CODE: D GETPAT^TIUCHLP// **&lt;Enter&gt;**

Select CAPTION: **??**

Choose from:

ATTENDING PHYSICIAN

DATE OF ADMISSION

DICTATED BY

DICTATION DATE

PATIENT SSN

TRANSCRIPTIONIST

URGENCY

This is the caption to be associated with a given field in the message

header and the target file (e.g., Patient Name:).

Select CAPTION: **PATIENT SSN**

CAPTION: PATIENT SSN// **&lt;Enter&gt;**

ITEM NAME: **SSN**

FIELD NUMBER: .02// **&lt;Enter&gt;**

LOOKUP LOCAL VARIABLE NAME: **??**

This field specifies the local variable name required by the lookup

routine into which this item will be set.

Enter the required local variable into which this item will be set.

LOOKUP LOCAL VARIABLE NAME:

TRANSFORM CODE: S:X?3N1P2N1P4N.E X=$TR(X,"-/","")

Replace **&lt;Enter&gt;**

EXAMPLE ENTRY: PRIORITY// **&lt;Enter&gt;**

CLINICIAN MUST DICTATE: YES// **&lt;Enter&gt;**

REQUIRED FIELD?: YES// **??**

This field is used to determine whether a given header item is required

by the application (e.g., Author and Attending Physician will be

required for the ongoing processing of a Discharge Summary).  Records

lacking required fields WILL be entered into the target file, if

possible, but will generate Missing Field Error Alerts.

Choose from:

1        YES

0        NO

Select CAPTION: **&lt;Enter&gt;** CAPTION: DATE OF ADMISSION// **&lt;Enter&gt;**

ITEM NAME: ADMISSION DATE// **&lt;Enter&gt;**

FIELD NUMBER: .07// **&lt;Enter&gt;**

LOOKUP LOCAL VARIABLE NAME: TIUADT// **&lt;Enter&gt;**

EXAMPLE ENTRY: 03/30/97// **&lt;Enter&gt;**

CLINICIAN MUST DICTATE: YES// &lt;Enter&gt;

REQUIRED FIELD?: YES// **&lt;Enter&gt;**

*Modify Upload Parameters—ASCII Protocol Example cont’d*

Select CAPTION: DATE OF DISCHARGE

ITEM NAME: DISCHARGE DATE

FIELD NUMBER: .08

LOOKUP LOCAL VARIABLE NAME: &lt;Enter&gt;

TRANSFORM CODE:  &lt;Enter&gt;

EXAMPLE ENTRY: &lt;Enter&gt;

CLINICIAN MUST DICTATE: Y  YES

REQUIRED FIELD?: Y  YES

Select CAPTION: DICTATED BY

CAPTION: DICTATED BY// &lt;Enter&gt;

ITEM NAME: DICTATING PROVIDER// &lt;Enter&gt;

FIELD NUMBER: 1202// &lt;Enter&gt;

LOOKUP LOCAL VARIABLE NAME: &lt;Enter&gt;

TRANSFORM CODE:  &lt;Enter&gt;

EXAMPLE ENTRY: CPRSPROVIDER,ONE, M.D.  Replace &lt;Enter&gt;

CLINICIAN MUST DICTATE: YES// &lt;Enter&gt;

REQUIRED FIELD?: Y  YES

Select CAPTION: DICTATION DATE

CAPTION: DICTATION DATE// &lt;Enter&gt;

ITEM NAME: DICTATION DATE// &lt;Enter&gt;

FIELD NUMBER: 1307// &lt;Enter&gt;

LOOKUP LOCAL VARIABLE NAME: TIUDICDT// &lt;Enter&gt;

TRANSFORM CODE:  &lt;Enter&gt;

EXAMPLE ENTRY: 04/03/97// &lt;Enter&gt;

CLINICIAN MUST DICTATE: YES// &lt;Enter&gt;

REQUIRED FIELD?: Y  YES

Select CAPTION: ATTENDING PHYSICIAN

CAPTION: ATTENDING PHYSICIAN// &lt;Enter&gt;

ITEM NAME: ATTENDING PHYSICIAN// &lt;Enter&gt;

FIELD NUMBER: 1209// &lt;Enter&gt;

LOOKUP LOCAL VARIABLE NAME: &lt;Enter&gt;

TRANSFORM CODE:  &lt;Enter&gt;

EXAMPLE ENTRY: CPRSPROVIDER,TWO, M.D.  Replace &lt;Enter&gt;

CLINICIAN MUST DICTATE: YES// &lt;Enter&gt;

REQUIRED FIELD?: Y  YES

Select CAPTION: TRANSCRIPTIONIST

CAPTION: TRANSCRIPTIONIST// &lt;Enter&gt;

ITEM NAME: TRANSCRIPTIONIST ID/ &lt;Enter&gt;/

FIELD NUMBER: 1302// &lt;Enter&gt;

LOOKUP LOCAL VARIABLE NAME: &lt;Enter&gt;

TRANSFORM CODE:  &lt;Enter&gt;

EXAMPLE ENTRY: T1212// &lt;Enter&gt;

CLINICIAN MUST DICTATE: NO// &lt;Enter&gt;

REQUIRED FIELD?: NO

Select CAPTION: &lt;Enter&gt;

The header for the Discharge Summary Document Definition is now defined as:

$HDR:                                   DISCHARGE SUMMARY

SOCIAL SECURITY NUMBER:                 000-00-0001

DATE OF ADMISSION:

DICTATED BY:                            CPRSPROVIDER,ONE, M.D.

DICTATION DATE:

ATTENDING PHYSICIAN:                    CPRSPROVIDER,TWO, M.D.

TRANSCRIPTIONIST:                       T0001

URGENCY:                                PRIORITY

$TXT

DISCHARGE SUMMARY Text

*** File should be ASCII with width no greater than 80 columns.

*** Use "@@@" for "BLANKS" (word or phrase in dictation that isn't

*** understood).

###### Kermit Protocol Example

This example demonstrates the ASCII upload source as a remote computer and the upload protocol is defined as a Kermit Protocol. Experience at sites suggests that the Kermit Protocol is the preferred protocol to transfer data because of its simple set-up and reliable functionality.

Select TIU Parameters Menu Option: **2** Modify Upload Parameters

First edit Institution-wide upload parameters:

Select INSTITUTION: **660**

1   660  SALT LAKE CITY       UT                              660

2   660AA  SALT LAKE DOM      UT                    VAMC      660AA

CHOOSE 1-2: **1** SALT LAKE CITY

...OK? Yes// **&lt;Enter&gt;** (Yes)

ASCII UPLOAD SOURCE: **r** remote computer

UPLOAD PROTOCOL: **k** KERMIT

UPLOAD HEADER FORMAT: **c** captioned

RECORD HEADER SIGNAL: **$HDR**

BEGIN REPORT TEXT SIGNAL: **$TXT**

RUN UPLOAD FILER IN FOREGROUND: NO// **NO**

Now Select upload error alert recipients:

Select ALERT RECIPIENT: **CPRSRECIPIENT,TWO**

Are you adding 'CPRSRECIPIENT,TWO' as a new UPLOAD ERROR ALERT RECIPIENT (the 1ST for

this TIU PARAMETERS)? **Y** (Yes)

Select ALERT RECIPIENT: **CPRSRECIPIENT,THREE**

Are you adding 'CPRSRECIPIENT,THREE' as a new UPLOAD ERROR ALERT RECIPIENT (the

2ND for this TIU PARAMETERS)? **Y** (Yes)

Select ALERT RECIPIENT: **&lt;Enter&gt;**

Now edit the DOCUMENT DEFINITION file:

DOCUMENT DEFINITION: **^**

*Modify Upload Parameters cont’d*

When configured this way, report text with the following format can be successfully uploaded and routed to the appropriate records in the TIU DOCUMENT File (#8925):

$HDR:			DISCHARGE SUMMARY

NAME OF PATIENT:		CPRSPATIENT,ONE

SOCIAL SECURITY NUMBER:	000-00-0001

DATE OF ADMISSION:

DATE OF DISCHARGE:

ATTENDING PHYSICIAN:	CPRSPROVIDER,THREE, M.D.

$TXT

DISCHARGE DIAGNOSIS:

1. Acute Ischemic Heart Disease.

2. Congestive Heart Failure.

3. Tachycardia.

PROCEDURES:		Cardiac Catheterization, Echocardiogram,

12-lead EKG.

.

.

$HDR:			DISCHARGE SUMMARY

NAME OF PATIENT:		CPRSPATIENT,TWO

SOCIAL SECURITY NUMBER:	000-00-0002

DATE OF ADMISSION:

DATE OF DISCHARGE:

ATTENDING PHYSICIAN:	CPRSPROVIDER,THREE, M.D.

URGENCY:			PRIORITY

$TXT

DISCHARGE DIAGNOSIS:

1. Acute abdominal pain of unknown etiology.

2. Diabetes mellitus type II.

3. Tachycardia.

PROCEDURES:		There were no invasive procedures done

during this hospitalization.

$END

##### Applying the Upload Utility to New Document Types

With the emergence of new types of documents, TIU from time to time extends the TIU Upload Utility for use in uploading new types of documents.  This section describes some of the steps involved in extending the TIU Upload Utility.

There are two main parts to the process.  The first part is determining what header data should be included in transcribed reports of the given document type and defining the upload header accordingly.  The second involves writing new code for several parts of the upload process, namely, for document lookup, and for filing error resolution.

Lookup Method code identifies the record the report should be uploaded into, in the target file, or perhaps creates a new record.  Upload Filing Error code gathers information from users alerted when a report fails to file, and attempts to re-file the report, after corrections are made.  A new, document type-specific Lookup Method is *required* for new document types.  New Upload Filing Error Code is *recommended* but not required.

###### Lookup Methods

In the absence of a document type-specific Lookup Method, the TIU Upload Utility performs a generic lookup, using just the document internal file number.  Experience has shown that this generic lookup is not reliable:  a single error in dictation or transcription of header data can cause the report to upload into the wrong record.  New types of documents therefore *must have* their own, document type-specific Lookup Method code, rather than relying on the generic lookup.

Lookup Methods are written in conjunction with an upload header definition for the given document type. They must be tested prior to use to make sure they deal adequately with potential user errors in dictation and transcription by cross-checking data for consistency and completeness. They should also deal with the possibility of sites erroneously setting field numbers in upload header definitions, for captions which should not have field numbers. Routine TIUPUTSX is well documented and provides a model for writing upload Lookup Methods when uploading into files other than the TIU Document file [#8925]. See routine TIUPUTCN for an example of a lookup method for documents uploaded into the TIU Document file.

###### Upload Filing Error Code

In the absence of custom filing error resolution code, the TIU Upload Utility attempts to resolve filing errors by permitting the user to edit the temporary buffer record.  The user is then asked if they wish to re-file the record.  If the user chooses to re-file, the same process used to attempt to file the document in the first place is called again.

Custom filing error resolution code, in contrast to the utility’s generic process, generally prompts the user for all the information necessary to file the record, and then proceeds automatically to file the record, without further user activity.  If the document still fails to file, the user is given the opportunity to revert to the generic filing error resolution process.  Since custom filing error resolution code generally does its own filing, it requires the writing of new filing code for the particular type of document, with checks for data consistency similar to those performed in the Lookup Method.  Although the generic error resolution process can be considered technically reliable, custom filing error resolution code is generally written as a convenience for users, who will not otherwise have access to the information needed to correct the buffer record.

Experience has shown that it is *not* advisable to call Filing Error Upload code written for a different document type.  If new code cannot be written, the generic process should be used, rather than calling code for a different document type.  For an example of the serious problems caused by using Filing Error Upload Code written for a different document type, see patch TIU*1*131, on FORUM.  If the generic process is used, care must be exercised to ensure that the document type does not inherit custom error resolution code from an ancestor in the document definition hierarchy.

Routines TIUPNFIX and TIUCNFIX contain filing error resolution code for Progress Notes and for Consults.  They are well documented and will serve as models when writing filing error resolution code for other document types.  Further information on those routines is provided, below.

An alternative, intermediate approach to filing error resolution code is modeled in routine TIUPUTSX. This approach prompts the user for necessary information, redisplays the selected data, but then relies on the user to make the necessary corrections and to refile the document. Such code is simpler to write than the usual full-blown filing error resolution code, and still provides the user with the information needed to correct the document.

###### Models for TIU Upload Filing Error Code

With patch TIU*1*131, the Upload Filing Error Code for Progress Notes and for Consults has been restructured to permit cross-checks on transcribed data.  This new code can be used as a model when writing filing error resolution code for other types of documents.

The new filing error resolution code subroutines for Progress Notes and for Consults, PNFIX^TIUPNFIX, and CNFIX^TIUCNFIX have the same basic structure. They:

1. Call generic* module LOADHDR^TIUFIX2 to load header data from the upload buffer record into an array, TIUFLDS.
2. Call document-type specific module GETCHECK (GETCHECK^TIUPNFIX for Progress Notes or GETCHECK^TIUCNFIX for Consults). This module prompts the user for data and validates that the data is consistent and complete.
3. Call generic* module MAKE^TIUFIX1, which creates a document (or uses an existing stub) and uploads into the document.

*In more detail:*

###### LOADHDR^TIUFIX2

Header data from the transcribed buffer record are loaded at the beginning of the filing error resolution process so that they can be used as default values when prompting the user for data in GETCHECK, and so that the header data array TIUFLDS can be updated in GETCHECK before its data are filed in MAKE^TIUFIX1. If a caption has no transcribed data, and the caption is listed in the upload header definition as REQUIRED, the corresponding node of TIUFLDS is loaded with the value, ** REQUIRED FIELD MISSING FROM UPLOAD**, so that it (along with any other invalid data) will fail to file later in MAKE^TIUFIX1, thus generating a missing field error.  LOADHDR is intended to apply generically* to document types beyond Progress Notes and Consults; the target file need not be the TIU DOCUMENT file (#8925).

###### GETCHECK—GETCHECK^TIUPNFIX for Progress Notes or GETCHECK^TIUCNFIX for Consults

GETCHECK prompts the user for all data needed to look up or create a document of the given type.  GETCHECK also prompts for any additional data which must be checked before being filed in the document. User-supplied data are either collected in a manner which enforces consistency, or cross-checked for consistency.  GETCHECK modules must be written specifically for each type of document.

###### MAKE^TIUFIX1:

MAKE^TIUFIX1 receives all data needed to either look up or create a TIU document.  That is, it either receives the internal file number (IFN) for an existing stub document, or it receives the document title, patient DFN, and a visit array TIU.  If no stub IFN is received, title, patient, and visit data are used to create a new TIU document.  A newly created document is then stuffed with data derived from the visit, and with other data already known, such as Method of Capture. For both newly created documents and for existing stubs, all received nodes of array TIUFLDS are then filed, and all fields which fail to file create missing field errors.  The text is then uploaded from the buffer record into the document.

Note that the error resolution process essentially ignores those data from the buffer record which are used in the initial upload process to create or look up a document.  Since the document failed to file, one or more of these data elements must be faulty.  Therefore, for filing error resolution, these data are taken directly from the user, and the document is created with user-supplied data rather than with transcribed, buffer data.  Those nodes of buffer array TIUFLDS which contain document creation/lookup data are killed before TIUFLDS is passed to MAKE^TIUFIX1, to prevent transcribed data from overwriting fields filed during the document creation process. Any nodes of TIUFLDS which contain fields *not* filed during the document creation process, but which *are supplied* by the user (so they can be checked in GETCHECK), are updated.  Remaining nodes of TIUFLDS are then filed after the document is created, in MAKE^TIUFIX1.  Lastly, the buffer record is used to file the text of the report.

MAKE is intended to apply generically* to document types beyond Progress Notes and Consults, but only to types which upload into the TIU DOCUMENT file (#8925).

Routines TIUFIX, TIUFIX1, and TIUFIX2 also contain other sub-modules intended for generic* use in resolving filing errors.

###### *Generic modules:

These modules are intended to apply to document types other than just Progress Notes and Consults.  Some will be useful only for documents uploaded into the

TIU DOCUMENT file (#8925). Others will be used regardless of target file.

None of these generic modules have been tested against document types other than Progress Notes and Consults; further use requires further testing.

Note:	The generic modules are subject to change by the TIU development staff without notice. Use these routines with caution.

##### Upload Menu for Transcriptionists

The Upload Menu contains sub-options that allow the transcriptionist to upload a batch of documents or get help about the header formats expected for each document type, by the upload process, as defined for your site.

| Option                  | Option Name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upload Documents        | TIU UPLOAD DOCUMENTS | This option lets transcriptionists upload transcribed ASCII documents in batch mode, either from remote microcomputers, using ASCII or KERMIT protocol upload, or from Host Files (i.e., DOS or VMS ASCII files) on the host system. Your site will define the preferred file transfer protocol and the destination within V  *IST*  A to which each report type (e.g., discharge summary, progress notes, Operative Report, etc.) should be routed. |
| Help for Upload Utility | TIU UPLOAD HELP      | This option displays information on the formats of headers for dictated documents that are transcribed off-line and uploaded into V  *IST*  A. It also displays “blank” character, major delimiter, and end of message signal as defined by your site.                                                                                                                                                                                               |

The upload utility permits mixed report types within a single batch. This allows the transcriptionist to enter each report in arrival sequence into a single ASCII file on the remote computer (e.g., using a proprietary word-processing program), and to transmit the text to the VistA host system as a one-step process. As this ASCII data arrives at the VistA host, it is read into a “buffer” file, and stored for subsequent “filing” by a special background process, called the “Router/filer.”

##### Router/Filer Notes

Each record in the batch file is preceded by a captioned header, the first line of which MUST begin with the MESSAGE HEADER SIGNAL as defined for your site (in this case $HDR), followed by a colon, followed by the document type name.

All other captioned fields will appear in any sequence, provided that the captions are appropriately spelled, followed by colons, followed by the values of the corresponding fields. Tabs will be used (they will be stripped), but all other non-ASCII characters (including formatting commands) must be omitted (i.e., the batch file MUST be saved as TEXT ONLY WITH LINE FEEDS, with no boldface or underlining, and NO PAGE BREAKS, PAGE HEADERS, or PAGE FOOTERS).

Notice that the first record lacked an URGENCY value, and that the format defined in file 8925.1 excludes captions for TYPE OF RELEASE and WARD NUMBER. The upload utility will simply ignore such missing or irrelevant data (i.e., the release type and ward at discharge are already known to **V** IST **A** and will be displayed on the 10-1000, whether the author dictates them, and the transcriptionist includes them or not).

The Router/filer is queued upon completion of transmission of a given batch of reports, and will proceed to “read” each line of the buffer file, looking for a header. When a header is encountered, the filer will determine whether the record corresponds to a known document type, as defined by your site, and if so, it will attempt to direct the record to the appropriate file and fields in **V** IST **A** .

On occasion, the Router/filer will not be able to identify the appropriate record in the target file, and will therefore be unable to file the record. When this happens, the process will leave the record in the buffer file and send an alert to a group of users identified by the site as being able to respond to such filing errors.

When ***any*** of the alert recipients chooses to act on one of these alerts (by entering “VA” at any menu prompt, and choosing the alert on which they wish to act), they will be shown the header of the failed report, and offered an opportunity to inquire to the patient record. They will then be presented with their preferred **V** IST **A** editor, and will then be allowed to edit the buffer (e.g., correct a bad social security number, admission date, etc.) and retry the filer.

With each attempt to correct the buffered data and retry the filer, all alerts associated with that record will be deleted (and if the condition remains uncorrected, re-sent), until all records are successfully filed.

You may also use the Review Upload Filing Events option on the MRT menu to correct such filing errors.

###### Batch Upload Reports

###### Kermit Protocol Upload

If your site is using the upload option to transfer batches of discharge summaries from a remote computer using the Kermit transfer protocol, start the upload process by following the sequence below:

###### 1 Choose UP from your Upload Menu.

UP     Batch upload reports

HLP    Display upload help

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select Upload menu Option: **UP** Batch upload reports

K E R M I T   U P L O A D

Now start a KERMIT send from your system.

Starting KERMIT receive.

**#N3**

###### 2 When you see the #N3 prompt, initiate the Kermit file transfer from your computer.

Try the default settings for the Kermit protocol as provided by your terminal emulation software. If you have problems, consult your terminal emulator user manual or contact your local IRM Service.

###### 3 When the transfer is complete, you’ll see this message:

File transfer was successful.  (1515 bytes)

Filer/Router Queued!

Press RETURN to continue... **&lt;Enter&gt;**

UP     Batch upload reports

HLP    Display upload help

Select Upload menu Option: **&lt;Enter&gt;**

ASCII Protocol Upload

If your site is using the upload option to transfer batches of discharge summaries from a remote computer using the ASCII transfer protocol, start the upload process by following the example shown below:

1. Choose UP from your Upload Menu.

UP     Batch upload reports

HLP    Display upload help

Select Upload menu Option: **UP** Batch upload reports

A S C I I   U P L O A D

1. When the “Initiate upload procedure:” prompt appears, initiate the ASCII file transfer from your computer.

NOTE:  If you have problems, consult your local IRM Service to see if the Terminal and Protocol Set-up parameters have been set up as shown earlier in this section, or check the user manual for your terminal emulator.

Initiate upload procedure:

$HDR:                                   DISCHARGE SUMMARY

&gt;PATIENT NAME:                           CPRSPATIENT,ONE

&gt;SOC SEC NUMBER:                         000-00-0001

&gt;ADMISSION DATE:

&gt;DISCHARGE DATE:

&gt;DICTATED BY:                            CPRSPROVIDER,FOUR M.D.

&gt;DICTATION DATE:

&gt;ATTENDING PHYSICIAN:                    CPRSPROVIDER,TWO, M.D.

&gt;TRANSCRIPTIONIST ID:                    T0001

&gt;URGENCY:                                PRIORITY

&gt;DIAGNOSIS:

&gt;1.  Acute pericarditis.

&gt;2.  Status post transmetatarsal amputation, left foot.

&gt;3.  Diabetes mellitus requiring insulin.

&gt;4.  Diabetic neuropathy.

&gt;

&gt;Operations/Procedures performed during current admission:

&gt;1.  Status post transmetatarsal amputation of left foot on .

&gt;2.  Echocardiogram done .

.

.

.

$END

Filer/Router Queued!

Press RETURN to continue... **&lt;Enter&gt;**

###### Handling upload errors

ASCII protocol upload / with alert

--- Transcriptionist Menu ---

1      Enter/Edit Discharge Summary

2      Enter/Edit Document

3      Upload Menu ...

CPRSPATIENT,THREE(T0003): 07/22/91 DISCHARGE SUMMARY is missing fields.

Enter  "VA   VIEW ALERTS     to review alerts

Select Text Integration Utilities (Transcriptionist) Option: **VA**

1.FILING ERROR: DIABETES EDUCATION  Record could not be found or created

2.FILING ERROR: ~3 DISCHARGE SUMMARY Invalid Report Type encountered.

3.FILING ERROR: PROGRESS NOTES  Record could not be found or created.

4.CPRSPATIENT,THREE(T0003): 07/22/91 DISCHARGE SUMMARY is missing fields.

5.CPRSPATIENT,FOUR (F0004): 08/14/95 ADVERSE REACTION/ALLERGY is missing fields.

Select from 1 to 5

or enter ?, A I, F, P, M, R, or ^ to exit: **1**

The header of the failed record looks like this:

$HDR: PROGRESS NOTES

TITLE: DIABETES EDUCATION

PATIENT: CPRSPATIENT,THREE

SSN: 000000003

VISIT/EVENT DATE: 04/18/96@10:00

AUTHOR: CPRSPROVIDER,ONE

TRANSCRIBER: SCRIPTION

DATE/TIME OF DICT: T

LOCATION: NUCLEAR MED

$TXT

Inquire to patient record? YES// **&lt;Enter&gt;**

Select PATIENT NAME: CPRSPATIENT,THREE    09-12-44     000000003     YES

SC VETERAN

(7 notes)  C:  17:01

(1 note )  W:  09:19

A: Known allergies

(3 notes)  D:  10:52

This patient is not currently admitted to the facility...

Is this note for INPATIENT or OUTPATIENT care? OUTPATIENT// **&lt;Enter&gt;**

The following VISITS are available:

1&gt;  MAY 21, 1997@08:30                 PULMONARY CLINIC

2&gt;  APR 11, 1997@08:00                 DIABETIC EDUCATION-INDIV-MOD B

3&gt;  APR 18, 1996@10:00                 GENERAL MEDICINE

4&gt;  FEB 21, 1996@08:40                 PULMONARY CLINIC

5&gt;  FEB 20, 1996@10:00  NO-SHOW        ONCOLOGY

CHOOSE 1-5

&lt;RETURN&gt; TO CONTINUE

OR '^' TO QUIT: 3  APR 18 1996@10:00

CHOOSE 1-5

&lt;RETURN&gt; TO CONTINUE

OR '^' TO QUIT: **3** APR 18 1996@10:00

Progress Note Identifiers...

Patient Name:  CPRSPATIENT,THREE

Patient SSN:  000-00-0003

Patient Location:  GENERAL MEDICINE

Date/time of Visit:  04/18/96 10:00

...OK? YES// &lt;Enter&gt;

TITLE: ADV

1   ADVANCE DIRECTIVE          TITLE

2   ADVERSE REACTION/ALLERGY          TITLE

CHOOSE 1-2: 2

Filing Record/Resolving Error...Done.

Opening Adverse React/Allergy record for review...

**Browse Document** Page:    1 of    1

Adverse React/Allergy

CPRSPATIENT,THREE 000-00-0003 GENERAL MEDICINE Visit Date: 04/18/96@10:00

DATE OF NOTE:          ENTRY DATE: JUN 13, 1997@15:56:16

AUTHOR: CPRSPROVIDER,ONE   EXP COSIGNER:

URGENCY:                          STATUS: UNVERIFIED

The new antihistamine is working.

**+ Next Screen  - Prev Screen  ?? More actions**

Find                      Edit                      Copy

Verify/Unverify           Send Back                 Print

On Chart                  Reassign                  Quit

Select Action: Quit// **V** Verify/Unverify

Do you want to edit this Adverse React/Allergy? NO// **&lt;Enter&gt;**

VERIFY this Adverse React/Allergy? NO// **YES**

ASCII protocol upload / with alert, cont’d

Adverse React/Allergy VERIFIED.

1.   FILING ERROR: ~3 DISCHARGE SUMMARY Invalid Report Type encountered.

2.   FILING ERROR: PROGRESS NOTES  Record could not be found or created.

3.   PATIENT,THREE(T0003): 07/22/91 DISCHARGE SUMMARY is missing fields.

4.   PATIENT,FOUR (A3456): 08/14/95 ADVERSE REACTION/ALLERGY is missing fields.

Select from 1 to 4

or enter ?, A I, F, P, M, R, or ^ to exit: **3**

You may now enter the correct information:

PATIENT,THREE (T0003): 07/22/91 DISCHARGE SUMMARY is missing fields.

Display ENTIRE existing record? NO// **YES**

DOCUMENT TYPE: Discharge Summary        PATIENT: CPRSPATIENT,THREE

VISIT: JUL 22, 1991@11:06

PARENT DOCUMENT TYPE: DISCHARGE SUMMARIES

STATUS: UNVERIFIED

EPISODE BEGIN DATE/TIME: JUL 22, 1991@11:06

EPISODE END DATE/TIME: FEB 12, 1996@13:56:50

LINE COUNT: 73                        VISIT TYPE: H

ASCII protocol upload / with alert, cont’d

ENTRY DATE/TIME: JUN 13, 1997@15:55:31

AUTHOR/DICTATOR: CPRSPROVIDER,ONE      EXPECTED SIGNER: CPRSPROVIDER,ONE

HOSPITAL LOCATION: 1A                  EXPECTED COSIGNER: CPRSPROVIDER,FIVE

ATTENDING PHYSICIAN: CPRSPROVIDER,FIVE VISIT LOCATION: 1A

REFERENCE DATE: FEB 12, 1996@13:56:50  ENTERED BY: BS

CAPTURE METHOD: upload                 RELEASE DATE/TIME: JUN 13, 1997@15:55:40

DICTATION DATE:

PATIENT MOVEMENT RECORD: JUL 22, 1991@11:06

TREATING SPECIALTY: SURGERY            COSIGNATURE NEEDED: YES

VISIT ID: 11HR-TEST

REPORT TEXT:

Enter RETURN to continue or '^' to exit: **&lt;Enter&gt;**

DIAGNOSIS:

1.  Status post head trauma with brain contusion.

2.  Status postcerebrovascular accident.

3.  End stage renal disease on hemodialysis.

4.  Coronary artery disease.

5.  Congestive heart failure.

6.  Hypertension.

7.  Non insulin dependent diabetes mellitus.

8.  Peripheral vascular disease, status post thrombectomies.

9.  Diabetic retinopathy.

10. Below knee amputation.

11. Chronic anemia.

OPERATIONS/PROCEDURES:

1. MRI.

2. CT SCAN OF HEAD.

HISTORY OF PRESENT ILLNESS: Patient is a 49-year-old, white male with past

medical history of end stage renal disease, peripheral vascular disease,

status post BKA, coronary artery disease, hypertension, non-insulin

dependent diabetes mellitus, diabetic retinopathy, congestive heart failure,

status post CVA, status post thrombectomy admitted from Anytown VA after a

fall from his wheelchair in the hospital.  He had questionable short lasting

loss of consciousness but patient is not very sure what has happened.  He

denies headache, vomiting, vertigo.  On admission patient had CT scan which

showed a small area of parenchymal hemorrhage in the right temporal lobe

which is most likely consistent with hemorrhagic contusion without mid line

shift or incoordination.

ACTIVE MEDICATIONS:  Isordil 20 mgs p.o. t.i.d., Coumadin 2.5 mgs p.o. qd,

ferrous sulfate 325 mgs p.o. b.i.d., Ativan 0.5 mgs p.o. b.i.d., Lactulose

15 ccs p.o. b.i.d., Calcium carbonate 650 mgs p.o. b.i.d. with food,

Betoptic 0.5% ophthalmologic solution gtt OU b.i.d., Nephrocaps 1 tablet

p.o. qd,  Pilocarpine 4% solution 1 gtt OU b.i.d., Compazine 10 mgs p.o.

t.i.d. prn  nausea, Tylenol 650 mgs p.o. q4 hours prn.

Patient is on hemodialysis, no known drug allergies.

PHYSICAL EXAMINATION:  Patient had stable vital signs, his blood pressure

was 160/85, pulse 84, respiratory rate 20, temperature 98 degrees.  Patient

was alert, oriented times three, cooperative.  His speech was fluent,

understanding of spoken language was good.  Attention span was good.  He had

moderate memory impairment, no apraxia noted.  Cranial nerves patient was

blind, pupils are not reactive to light, face was asymmetric, tongue and

palate are mid line.  Motor examination showed muscle tone and bulk without

significant changes.  Muscle strength in upper extremities 5/5 bilaterally,

ASCII protocol upload / with alert, cont’d

sensory examination revealed intact light touch, pinprick and vibratory

sensation.  Reflexes 1+ in upper extremities, coordination finger to nose

test  within normal limits bilaterally.  Alternating movements without

significant  changes bilaterally.  Neck was supple.

LABORATORY:  Showed sodium level 135, potassium 4.6, chloride 96, CO2 26,

BUN 39, creatinine 5.3, glucose level 138.  White blood cell count was 7,

hemoglobin 11, hematocrit 34, platelet count 77.

HOSPITAL COURSE:  Patient was admitted after head trauma with multiple

Enter RETURN to continue or '^' to exit: **&lt;Enter&gt;**

medical problems.  His coumadin was held.  Patient had cervical spine x-rays

which showed definite narrowing of C5, C6 interspace, slight retrolisthesis

at this level, prominent spurs at this level as well as above and below.  CT

scan on admission showed a moderate amount of scalp thinning with

subcutaneous air overlying the left frontal lobe.  A small area of left

parenchymal hemorrhage adjacent to the right petros bone in the temporal

lobe which most likely represents a hemorrhagic contusion.  The basal

cisterns are patent and there is no mid line shift or uncal herniation.

Patient has also a remote left  posterior border zone infarct with

hydrocephalus ex vaccuo of the left occipital horn, a rather large remote

infact in the inferior portion of the left cerebellar hemisphere.  Repeated

CT scan on  didn't show any  progressive changes.  Patient remained

in stable condition.  He had  hemodialysis q.o.d.  He restarted treatment

with Coumadin.  His last PT was  11.9, PTT 31.  Patient refused before

hemodialysis new blood tests.  His  condition remained stable.

DISCHARGE MEDICATIONS:  Isordil 20 mgs p.o. t.i.d., Ferrous sulfate 325 mgs

p.o. b.i.d., Ativan 0.5 mgs p.o. b.i.d., Lactulose 15 ccs p.o. b.i.d.,

Calcium carbonate 650 mgs p.o. b.i.d., Compazine 10 mgs p.o. t.i.d. prn

nausea,  Betoptic 0.5% OU b.i.d., Nephrocaps 1 p.o. qd, Pilocarpine 4%

solution 1 gtt OU b.i.d., Coumadin 2.5 mgs p.o. qd, Tylenol 650 mgs p.o. q6

hours prn pain.

DISPOSITION/FOLLOW-UP: Recommend follow PT/PTT.  Patient is on coumadin and

CBC with differential because patient has chronic anemia and

thrombocytopenia.

Patient will be transferred to Anytown VA in stable condition on .

URGENCY: ~0 PRIORITY// **P** priority

1.   FILING ERROR: ~3 DISCHARGE SUMMARY Invalid Report Type encountered.

2.   FILING ERROR: PROGRESS NOTES  Record could not be found or created.

3.   CPRSPATIENT,FOUR (F0004): 08/14/95 ADVERSE REACTION/ALLERGY is missing fie

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit: **&lt;Enter&gt;**

--- Transcriptionist Menu ---

1      Enter/Edit Discharge Summary

2      Enter/Edit Document

3      Upload Menu ...

Select Text Integration Utilities (Transcriptionist) Option: **&lt;Enter&gt;**

In the example above, notice that patient CPRSPATIENT,THREE had no admission on 11/17/96, and so the filer could not create a record in the target file for this discharge summary record. The user acts on the alert to correct the admission date as , and retries the filer, which is now able to file the record appropriately, and the alerts are removed for all recipients.

Display Upload Help

Transcriptionists may select this sub-option in the Upload Menu to display the formats expected by the upload process for the report types defined at your site.

The captioned headers may be captured as ASCII data and used to build macros using commercial word-processors (e.g., Word Perfect or Microsoft Word), and thereby avoid retyping the captioned headers, while minimizing the risk of spelling errors or inconsistencies with the formats expected by the host system.

UP     Batch upload reports

HLP    Display upload help

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select Upload menu Option: **HLP** Display upload help

Select REPORT TYPE: DISCHARGE SUMMARY// **&lt;Enter&gt;** Discharge Summary

$HDR:                                   DISCHARGE SUMMARY

SOC SEC NUMBER:                         555-12-1212

ADMISSION DATE:

DISCHARGE DATE:

DICTATED BY:                            CPRSPROVIDER,FOUR, M.D.

DICTATION DATE:

ATTENDING:                              CPRSPROVIDER,TWO, M.D.

TRANSCRIPTIONIST ID:                    T0003

URGENCY:                                PRIORITY

$TXT

DISCHARGE SUMMARY Text

$END

*** File should be ASCII with width no greater than 80 columns.

*** Use "\_\_\_" for "BLANKS" (word or phrase in dictation that isn’t understood).

Press RETURN to continue... **&lt;Enter&gt;**

##### Document Parameter Edit

###### [TIU DOCUMENT PARAMETER EDIT]

This option allows the Clinical Coordinator or IRM Application Specialist to set up either the Basic or Upload Parameters for Text Integration Utilities (TIU). In the example that follows note the explanation of each parameter displayed when double question marks (??) are entered. As TIU parameters are added these explanations will be kept up-to-date.

###### Example

Select TIU Maintenance Menu Option: **1** TIU Parameters Menu

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select TIU Parameters Menu Option: **3** Document Parameter Edit

First edit Institution-wide parameters:

Select DOCUMENT: **PROGRESS NOTES** CLASS

...OK? Yes// **&lt;Enter&gt;** (Yes)

DOCUMENT NAME: PROGRESS NOTES// &lt;Enter&gt;

REQUIRE RELEASE: NO// **??**

This parameter determines whether the person entering the

document will be required (and prompted) to release

the document from a draft state, upon exit from the

entry/editing process.

Though designed for Discharge Summaries, release may be used for any

kind of TIU document.

Choose from:

1        YES

0        NO

REQUIRE RELEASE: NO// **&lt;Enter&gt;**

REQUIRE MAS VERIFICATION: UPLOAD ONLY // **??**

This parameter determines whether verification by MAS is

required, prior to public access, and signature of the

document.

Though designed for Discharge Summaries, verification may be used for any

kind of TIU document, and is particularly helpful for documents that are

uploaded from a transcription service.

Allowable values are:  0       NO

1       YES, ALWAYS

2       UPLOAD ONLY

3       DIRECT ENTRY ONLY

where 1 indicates that these documents require verification regardless of

how they originate; 2 indicates that verification is required only when

only when documents are entered directly into VISTA.

Choose from:

1        YES, ALWAYS

0        NO

2        UPLOAD ONLY

3        DIRECT ENTRY ONLY

REQUIRE MAS VERIFICATION: UPLOAD ONLY// **&lt;Enter&gt;**

REQUIRE AUTHOR TO SIGN: YES// **??**

Currently applies only to Discharge Summaries. This field indicates

whether or not the author should sign the document before the expected

cosigner (attending).

If parameter is set to NO, only the expected cosigner is alerted for

signature. Although the unsigned document appears in the author's unsigned

list, and he is ALLOWED to sign it, his signature is not REQUIRED.

If set to YES, then the author is alerted for signature, and if the

expected cosigner should attempt to sign the document first, he is

informed that the author has not yet signed.

Choose from:

1        YES

0        NO

REQUIRE AUTHOR TO SIGN: YES// &lt;Enter&gt;

ROUTINE PRINT EVENT(S): **??**

A document of the given type, and of ROUTINE urgency, is automatically

printed whenever one of these events occurs.

For example, a site may specify that ROUTINE documents print only upon

Completion (i.e., signature or cosignature), while STAT documents print

upon Release from Transcription, MAS Verification, or both, in addition to

printing upon completion.

If print events are not specified, and a CHART COPY DEVICE is defined for

the Medical Center Division, then the document will be auto-printed only

upon completion.

If field MANUAL PRINT AFTER ENTRY is set to YES, then auto-print is

ignored entirely.

If urgency is not specified for some document, then its urgency is

considered to be routine, and the document prints when a routine print

event occurs.

Choose from:

R        release

V        verification

B        both

ROUTINE PRINT EVENT(S): **&lt;Enter&gt;**

STAT PRINT EVENT(S): **??**

This field is identical to ROUTINE PRINT EVENT(S), except that it applies

to documents of STAT urgency rather than ROUTINE urgency.

Choose from:

R        release

V        verification

B        both

STAT PRINT EVENT(S): **&lt;Enter&gt;**

MANUAL PRINT AFTER ENTRY: YES// ??

This parameter is used for documents where a manually-printed hard copy

is desired following document entry. If the parameter is set to YES, the

user is prompted to print a copy on exit from their preferred editor, and

auto-printing (as described in fields ROUTINE/STAT PRINT EVENT(S)) is

ignored.

Choose from:

1        YES

0        NO

MANUAL PRINT AFTER ENTRY: YES// &lt;Enter&gt;

ALLOW CHART PRINT OUTSIDE MAS: YES// ??

This field determines whether non-MAS users (for example, providers) are

asked if they want WORK copies or CHART copies when they print a document.

If the field is NOT set to YES, they are not asked, and the printout is a

WORK copy.

Generally, this is set to YES for PROGRESS NOTES, which are likely to be

printed on the Ward or in the Clinic for immediate inclusion in the chart.

For DISCHARGE SUMMARIES, which are typically printed centrally, it is

usually set to NO, since duplicate CHART COPIES are a particular problem.

Choose from:

1        YES

0        NO

ALLOW CHART PRINT OUTSIDE MAS: YES// &lt;Enter&gt;

ALLOW &gt;1 RECORDS PER VISIT: YES// ??

For example, it is often appropriate to enter

multiple PROGRESS NOTES for a single HOSPITALIZATION or CLINIC VISIT, whereas

only one DISCHARGE SUMMARY is usually entered per HOSPITALIZATION.

Choose from:

1        YES

0        NO

ALLOW &gt;1 RECORDS PER VISIT: YES//&lt;Enter&gt;

ENABLE IRT INTERFACE: ??

This enables TIU's interface with Incomplete Record Tracking, (IRT)

which updates IRT’s deficiencies when transcription, signature,

or cosignature (review) events are registered for a given

document.

NOTE: IRT is designed for DISCHARGE SUMMARIES, and is appropriate only for

types of documents where only one document is expected per patient

movement. We therefore ask you to leave this parameter undefined (or set

it to NO) for PROGRESS NOTES.

Choose from:

0        NO

1        YES

ENABLE IRT INTERFACE: &lt;Enter&gt;

SUPPRESS DX/CPT ON NEW VISIT: NO// **??**

This parameter applies only to documents for outpatient care. Together

with parameter ASK DX/CPT ON ALL OPT VISITS, it determines whether or not

a user is prompted for diagnoses and procedures after signing or editing a

document.

If this parameter is set to YES (for suppress), the user is not prompted

for this information.

If this parameter is set to NO or is blank, the user may or may not be

prompted, depending on the type of visit and on parameter ASK DX/CPT ON

ALL OPT VISITS.

If a site elects to suppress diagnoses and procedures, the site must

capture this information by some other means (such as an AICS encounter

form), in order to receive workload credit for these visits.

Choose from:

1        YES

0        NO

SUPPRESS DX/CPT ON NEW VISIT: NO// **&lt;Enter&gt;**

FORCE RESPONSE TO EXPOSURES: **??**

When set to YES, this parameter forces the user to respond when

asked to specify a veteran's Service Connection Classification

(AO, IR, or EC),when creating a standalone visit.

Choose from:

1        YES

0        NO

FORCE RESPONSE TO EXPOSURES: **&lt;Enter&gt;**

ASK DX/CPT ON ALL OPT VISITS: **??**

This parameter applies only to documents for outpatient care,

and is IGNORED if SUPPRESS DX/CPT ON ENTRY is set to YES.

If DX/CPT prompts are NOT suppressed, and ASK DX/CPT ON ALL

OPT VISITS is set to YES, the user is prompted for DX/CPT

information for scheduled as well as unscheduled (stand-alone)

visits.

If DX/CPT prompts are NOT suppressed, and ASK DX/CPT ON ALL OPT

VISITS is set to NO, the user is prompted for DX/CPT information

for unscheduled visits ONLY.

Choose from:

1        YES

0        NO

ASK DX/CPT ON ALL OPT VISITS: **&lt;Enter&gt;**

SEND ALERTS ON ADDENDA: **??**

This parameter determines whether AUTHORS and COSIGNERS of a

document of this kind (and any of its descendent types) will

receive an informational alert when addenda are added by other

persons. Like all document parameters, it may be overridden at

descendent levels of the Document Definition Hierarchy. DEFAULT

is NO.

Choose from:

1        YES

0        NO

SEND ALERTS ON ADDENDA: **&lt;Enter&gt;**

ORDER ID ENTRIES BY TITLE: **??**

This prompt applies only to notes with interdisciplinary entries

Under them.

When an ID note is displayed or printed, the child entries are

Normally ordered by reference date under the parent entry. In some

cases it May be preferable to order them alphabetically by title.

If this parameter is set to YES, child entries are displayed by

title rather than by date.

The default order is by date.

Choose from:

1        YES

0        NO

ORDER ID ENTRIES BY TITLE: **&lt;Enter&gt;**

SEND ALERTS ON NEW ID ENTRY: YES// **??**

This parameter applies only to interdisciplinary parent notes.

If this parameter is set to YES, the signer (cosigner) of an

interdisciplinary parent note is alerted when a new entry is added

to the note.

The default is NO.

Choose from:

1        YES

0        NO

SEND ALERTS ON NEW ID ENTRY: YES// **&lt;Enter&gt;**

EDITOR SET-UP CODE: ??

This is M code which is executed prior to invoking the user's preferred

editor.  It ordinarily sets local variables, which are then used in the

editor's header, etc.

For example, code written at Boston VAMC sets a local array containing

patient demographics.  An M-based editor used at the site can then display

demographic information in a fixed header when a user edits a document.

EDITOR SET-UP CODE: **&lt;Enter&gt;**

If document is to be uploaded, specify Filing Alert Recipients:

If your site wishes to route alerts for filing errors to different recipients by document type (Discharge Summary alerts to one MRT, Operative Report alerts to another, etc.), this is where to specify that.

<!-- image -->

// **??**

CPRSRECIPIENT,ONE

You May enter a new FILING ERROR ALERT RECIPIENTS, if you wish

These persons receive alerts from the upload filer process when a document

of the given type cannot be filed/located, or has a missing field.

If a document being uploaded has a missing/bad title, then alert

recipients defined at the title level cannot be found.  In this case,

recipients named at the class level are alerted. For example, if a

Progress Note is being uploaded and has a missing/bad title, then Progress

Note-level recipients are alerted.

If recipients are not specified, then alert recipients named in parameter

UPLOAD ERROR ALERT RECIPIENTS in the TIU PARAMETER file are alerted as

defaults.

Choose from:

CPRSPROVIDER,ONE     OC            PHYSICIAN

CPRSPROVIDER,TWO     TC

CPRSPROVIDER,THREE   TC

. . .

'^' TO STOP: ^

Select FILING ERROR ALERT RECIPIENTS: **CPRSRECIPIENT,ONE**

// **&lt;Enter&gt;**

Now enter the USER CLASSES for which cosignature will be required:

Select USERS REQUIRING COSIGNATURE: INTERN// **??**

Choose from:

INTERN

PAYROLL TECHNICIAN

STUDENT

You may enter a new USERS REQUIRING COSIGNATURE, if you wish

Applies to all types of documents EXCEPT DISCHARGE SUMMARIES.

Please indicate which groups of users (i.e., User Classes) require

cosignature for the type of document in question.  For example, STUDENTS,

INTERNS, LPNs, and other user classes may be identified as requiring a

cosignature for PROGRESS NOTES.

NOTE: Independent of this parameter, DISCHARGE SUMMARIES ALWAYS require

cosignature by the ATTENDING PHYSICIAN, EXCEPT when the ATTENDING

PHYSICIAN dictates the summary himself.

Choose from:

ACCOUNTANT

ACCOUNTS PAYABLE EMPLOYEE

.

.

.

'^' TO STOP: ^

Select USERS REQUIRING COSIGNATURE: INTERN// **&lt;Enter&gt;**

Now enter the DIVISIONAL parameters:

Select DIVISION: SALT LAKE CITY// **?**

Answer with DIVISION:

SALT LAKE CITY

You may enter a new DIVISION, if you wish

Please indicate the Medical Center Division

Answer with MEDICAL CENTER DIVISION NUM, or NAME, or FACILITY NUMBER:

1               SALT LAKE CITY      660

Select DIVISION: SALT LAKE CITY// **&lt;Enter&gt;**

CHART COPY PRINTER: **??**

This parameter is primarily useful for DISCHARGE SUMMARIES, or other

documents where automatic central printing of chart copies on site-

configurable events are most useful (e.g., INTERIM SUMMARIES or

OPERATIVE REPORTS at some point in the future).

When defined along with a STAT CHART COPY PRINTER, this is the device to

which chart copies of documents with ROUTINE urgencies will be sent

automatically.  If no STAT CHART COPY PRINTER is defined, then ALL

documents of the current type will be sent to this device, regardless of

their urgencies.

Note: If field MANUAL PRINT AFTER ENTRY is set to YES, then auto-print

is ignored.

Choose from:

AFJX RESOURCE     IRM      AFJX RESOURCE

BROKER DEVICE     SYSTEM      \_BG

HFS     Host File Server      DSA4:[MUMPS.OERMGR]

HOME     HOME      \_LTA:

INTERMEC 4100     LABEL TABLE      \_LTA370:

S-DJ     Slaved Deskjet      0

'^' TO STOP: ^

CHART COPY PRINTER: &lt;Enter&gt;

STAT CHART COPY PRINTER: ??

This parameter is primarily useful for DISCHARGE SUMMARIES, or other

documents where automatic central printing of chart copies on site-

configurable events are most useful (e.g., INTERIM SUMMARIES or

OPERATIVE REPORTS at some point in the future).

When defined along with a CHART COPY PRINTER, this is the device to

which chart copies of documents with STAT urgencies will be sent

automatically.

Note: If field MANUAL PRINT AFTER ENTRY is set to YES, then auto-print

is ignored.

Choose from:

AFJX RESOURCE     IRM      AFJX RESOURCE

BROKER DEVICE     SYSTEM      \_BG

HFS     Host File Server      DSA4:[MUMPS.OERMGR]

HOME     HOME      \_LTA:

INTERMEC 4100     LABEL TABLE      \_LTA370:

S-DJ     Slaved Deskjet      0

'^' TO STOP: ^

STAT CHART COPY PRINTER: &lt;Enter&gt;

Select DIVISION: &lt;Enter&gt;

If document is to be uploaded, specify Filing Alert Recipients:

Select FILING ALERT RECIPIENT: TRANSCRIPTION,USER

// ??

TRANSCRIPTION,USER

You may enter a new FILING ERROR ALERT RECIPIENTS, if you wish

These persons receive alerts from the upload filer process when a

document of the given type cannot be filed/located, or has a missing

field.

If a document being uploaded has a missing/bad title, then alert

recipients defined at the title level cannot be found.  In this case,

recipients named at the class level are alerted. For example, if a

Progress Note is being uploaded and has a missing/bad title, then

Progress Note-level recipients are alerted.

If recipients are not specified, then alert recipients named in

parameter UPLOAD ERROR ALERT RECIPIENTS in the TIU PARAMETER file are

alerted as defaults.

Choose from:

ACCESS,NEW                    IRM

ALBANY,VAMC               VA     136     FEE BASIS CLERK

AMIE,VACO               VA

ANRVAPPLICATION,PROXY USER

ATL,STUDENT             GEORGIA

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

ATL,STUDENT

Type &lt;Enter&gt; to continue or '^' to exit: ^

Select FILING ALERT RECIPIENT: TRANSCRIPTION,USER

// &lt;Enter&gt;

EXCLUDE FROM COPY/PASTE: ??

This field defaults to NO (0) if no value is set for a specific

document. This should be a rarely used field as most documents

should allow tracking of copy/paste data. Each site will need to

determine if they use any special TIU notes which should/need to be

excluded based on pre-existing policies/procedures which emphasize

the re-use of text which cannot be accomplished via templates or

other mechanisms.

Choose from:

1        YES

0        NO

EXCLUDE FROM COPY/PASTE: &lt;Enter&gt;

Press RETURN to continue...&lt;Enter&gt;

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

Select TIU Parameters Menu Option:&lt;Enter&gt;

Form Letter

The new parameters with patch TIU*1*222 expand the 'Document Parameter Edit' option [TIU DOCUMENT PARAMETER EDIT] when the document is in the FORM LETTERS document class.

When a note whose title is in the FORM LETTERS document class is printed the regular TIU header is suppressed and the contents of the form letter parameters are added to the beginning and end of the letter. Also, the signature block is suppressed.

Note:	Form letters can be printed before being signed as a draft copy. Caution should be used because there is no indication of completion status on the printed draft. You should destroy all drafts made in this manner.

All templates and TIU objects are supported for form letters—the same as with other TIU documents. Additionally, TIU objects are supported in header and footer fields.

Note:	Caution should be exercised so that no personally identifiable information, such as Social Security Number or Date of Birth, is included in form letters. Sending this sort of information through mail is a potential patient safety issue. Consult with your facilities Privacy Officer with questions about what would violate the privacy of your patients.

When a form letter includes addenda, the letter and addenda are each to be printed starting on a separate page with the header and footer as specified in the parameters. A parent Interdisciplinary Note (ID Note), if in the FORM LETTER document class, prints as a form letter but without its child notes. When the opposite is true (i.e., the parent note is not a form letter, but the child notes are) then the parent note prints with the usual TIU header information, and each child note prints as a form letter.

Note:	Form letters are designed to be used with Progress Notes and any use of form letters outside of this document class is not supported. The original charter for the FORM LETTERS document class, and the functionality that goes along with it, is to provide a form letter feature with minimized probability of violating the patient’s privacy. The use of form letters functionality for other types of progress notes circumvents this safeguard.

Note that the entire beginning parameter sequence is included for example purposes only and that the actual settings for each parameter should be set according to your site's requirements:

The FOOTER is printed at the bottom of every page.

Select where to print heading; LEFT JUSTIFY is the default.

Prints at the top of the first page.

If no heading is wanted, blank lines may be added to help text placement with envelope windows.

Select where to print the footer. LEFT JUSTIFY is the default.

<!-- image -->

PAGE NUMBERS: YES// **&lt;Enter&gt;** JUSTIFY PAGE NUMBERS: RIGHT JUSTIFIED// **&lt;Enter&gt;** Press RETURN to continue...

When printing a document title from the new document class, CHART or WORK copy is ignored and will print as a FORM LETTER omitting the standard header and footer.

The use of TIU OBJECTS/PATIENT DATA objects is supported in the new fields and should be used with care to avoid including any sensitive patient data if the document is to be printed and/or mailed to that patient.  Objects that return either a single line or multiple lines of data are supported.

The HEADING will print at the top of THE FIRST PAGE.  A blank line follows the heading to separate it from the note body.

The FOOTER will print at the bottom of EVERY PAGE.  A blank line precedes the footer to separate it from the note body.

The CLOSING will print at the END of the document.  One blank line precedes the closing to separate it from the note body.

PAGE NUMBERS will be displayed in the format 'Page X of X'.  It will print immediately after the footer (if present).

The default placement for all new segments is LEFT JUSTIFIED if left blank.

When viewing titles in the FORM LETTERS class in the CPRS GUI, the heading, closing and footer will be displayed giving an indication of what the document will look like when printed.  Page numbers are not displayed, but will display during printing if selected.

The finished note looks like this:

<!-- image -->

Note:	Form letters are displayed in CPRS as they will be printed with the header and footer information in place.

##### Progress Notes Batch Print Locations

###### [TIU PRINT PN LOC PARAMS]

These parameters are used by the [TIU PRINT PN BATCH INTERACTIVE] and [TIU PRINT PN BATCH SCHEDULED] options. If the site wants a header other than what is returned by $$SITE^ VASITE the .02 field of the 1st entry in this file will be used.  For example, Town1-Town2-Town3 can have the institution of their progress notes as “CENTRAL ANYWHERE HCF.”

Select TIU Maintenance Menu Option: **1** TIU Parameters Menu

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

Select TIU Parameters Menu Option: **4** Progress Notes Batch Print Locations

Select Clinic or Ward: **TELEPHONE TRIAGE** - PSYCHIATRY

PROGRESS NOTES DEFAULT PRINTER: LASERJET 4SI// **&lt;Enter&gt;**

EXCLUDE FROM PN BATCH PRINT: **?**

Set to '1' progress notes for this location will not be included

in the progress notes outpatient batch print job [TIU PRINT PN

BATCH].You would do this if you wanted to print the CHART copies

of the notes for this location in the clinic and not in the file

room.

Choose from:

1        YES

##### Division - Progress Notes Print Params

###### [TIU PRINT PN DIV PARAMS]

Use this option for entering hospital locations used for [TIU PRINT PN OUTPT LOC] and [TIU PRINT PN WARD] options. If locations are not entered in this file they will not be selectable from these options.

Select TIU Maintenance Menu Option: 1  TIU Parameters Menu

1      Basic TIU Parameters

2      Modify Upload Parameters

3      Document Parameter Edit

4      Progress Notes Batch Print Locations

5      Division - Progress Notes Print Params

Select TIU Parameters Menu Option: 5  Division - Progress Notes Print Params

Select Division for PNs Outpatient Batch Print: ?

Answer with TIU DIVISION PRINT PARAMETERS, or NUMBER:

1               SALT LAKE CITY

You may enter a new TIU DIVISION PRINT PARAMETERS, if you

wish. Select the DIVISION these print parameters apply to.

Answer with MEDICAL CENTER DIVISION NUM, or NAME:

1               SALT LAKE CITY      660

Select Division for PNs Outpatient Batch Print: YOUR HOSPITAL

...OK? Yes// &lt;Enter&gt;  (Yes)

LOCATION TO PRINT ON FOOTER: ??

The name of this division as it should appear in the footer

of the progress notes and forms printed using the terminal

outpatient sort.  This is useful for sites that want

digit something other than what the external value of

this division returned by $$SITE^VASITE.  For example, the

TxTown1 division of the Central Anywhere Health Care System may

want Central Anywhere HCS- TxTown1 to appear in the footer instead

of TXTOWN1 VAMC.

LOCATION TO PRINT ON FOOTER: CENTRAL ANYWHERE

PROGRESS NOTES BATCH PRINTER: WARD LASERJET 4SI

##### Document Definitions

###### [TIUF DOCUMENT DEFINITION MGR]

Whenever a provider enters a TIU document (such as a report, a progress note, a discharge summary, or other documentation), that document is linked to a Document Definition in the Document Definition hierarchy. This Document Definition stores the behavior of the document (for example, signature requirements) and is called a Title. It also stores boilerplate/ overprint text, if desired.

Plan the Document Definition Hierarchy your site or service will use before installing TIU and converting Progress Notes. Patch GMRP*2.5*44 helps you do this, by cleaning up and organizing your files before the conversion.

For more detailed information describing the hierarchy, see the field descriptions for the Document Definition File in the data dictionary.

###### Document Definition Layers:

<!-- image -->

The layer linked to individual documents is the *Titles* layer, which is the lowest of the Hierarchy. Titles can be composed of Components (e.g., a SOAP note is composed of the components Subjective, Objective, Assessment, and Plan).

The two higher layers of definition are *Document Class* and *Class* . These layers group Document Definitions within a meaningful organization. These two layers also store some behaviors, which are inherited by associated Titles.

TIU permits nested levels of Class. TIU allows only one Document Class level beneath a Class level. This level, however, can contain as many Document Classes as necessary. TIU allows only one level of Titles beneath a Document Class. This level however, can contain as many Titles as necessary.

##### Document Definition Options

| ## Option  ## Text           | ## Option Name               | ## Description  ## Document Definition Terminology &amp; Rules  This section describes the terms and rules used in the Document Definition system.  #### NAME  - Plus (+) indicates that the entry has Items under it and can be expanded. - The name of a Document Definition entry (.01 field) must be between three and 60 characters long and may not begin with a punctuation character. Although names can be entered in upper or lower case, they are transformed to upper case before being stored. - Name functions as the Technical Name of the entry. Some sites have put KWIC cross references on it to get, say, all Titles from a given Service. - Name can be used when entering documents as the name of the Title being entered. Print Name and Abbreviation will also be accepted. - Since it is the Technical, .01 Name, TIU uses this name throughout. - The .01 name differs from the Print Name, which appears in lists of documents and functions as the Title of the document. - It also differs from Item Menu Text (1-26 characters), which is used when selecting documents from three-column menus. - The order of names in the options *Edit Document Definitions* and *Create Document Definitions* is by Item Sequence under the parent. The order is alphabetic by Menu Text if an Item has no Item Sequence. - When a new entry is added to file 8925.1 the default Print Name is entered. The Print Name can be edited if a different Print Name is desired. - File 8925.1 permits more than one entry with the same name if they are different Types. In that sense, Names are reusable. However, Entries are not reusable (except specially marked Components); an entry is not allowed to be an item under more than one parent unless it is a Shared Component. (See Component.)  #### OBJECT NAME  - Object Names, like any other names are 3-60 characters, not starting with punctuation. Sites may want to namespace object names, use the object Print Name as a more familiar name, and use the object Abbreviation as a short name to embed in boilerplate text. Unlike other Types, Object Abbreviation and Print Name as well as Name must be uppercase. - Object Name, Abbreviation, or Print Name can be embedded in boilerplate text.  Since TIU must be able to determine from this which object is intended, object Names, Abbreviations, and Print Names must be unique. In fact, an object Name must differ not only from every other object name, but also from every other object Abbreviation and from every other object Print Name. Same for Abbreviations and Print Names. For example, if some object has the abbreviation CND, then CND cannot be used for any other object Name, Abbreviation, or Print Name.  #### TYPE  - Type determines the nature of the entry and what sort of items the entry may have. There are five possible types:  **Class (CL)** :  Classes group documents.  - Example: “Progress Notes” is a class with many kinds of progress notes under it.     - Classes may themselves be subdivided into items under a Class and/or may have items of Document Class if no further subdivisions are desired.     - If a hierarchy deeper than Class-Document Class-Title is desired, Class is the place to insert another level into the hierarchy: Class-Class-Document Class-Title.     - *Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.***Document Class (DC)** : Document Classes group documents. Document Class is the lowest level of class, and has items of the Title Type under it.     - Example: “Day Pass Note” could be a Document Class under class Progress Note.     - Document Classes also store behavior which is then inherited by lower entries.  ##### Document Definition Terminology cont’d  **Title (TL):** Titles are used to enter documents. They store the behavior of the documents which use them.  - Titles may have predefined boilerplate (Overprint) text. They may have Components as items. Boilerplate Text can have Objects in it. - Examples: “Routine Day Pass Note” could be a Title under document class Day Pass Note. Another example might be “Exceptional Circumstances Day Pass Note.” - Titles store their own behavior. They also inherit behavior from higher levels of the hierarchy. However, behavior stored in the Title itself always overrides inherited behavior.  **Component (CO):** Components are “sections” or “pieces” of documents. In the Hierarchy, Components are organized as items under Titles.  - Examples: “Reason for Pass” could be a component of Routine Day Pass Note. Subjective is a component of a SOAP Note.     - Components may have (sub)Components as items. They may have Boilerplate Text. Components may be designated Shared (see field description for Shared). Shared Components are shown in Document Definition Utility displays as Type “CO S”.     - There are advantages and disadvantages in splitting a document up into separate components (rather than writing sections into the Boilerplate Text of the Title). Since Components are stored as separate file entries, they are inherently accessible and even “movable.” Using FileMan, sites can access components of documents the same way they can access documents for reports, etc. Also, in the future, TIU may have options to move or copy certain components from one document into another. The disadvantage is speed. Components make the structure more complex and, therefore, slow down processing.  ##### Document Definition Terminology cont’d  **Object (O):** Objects are names which may be embedded in the predefined boilerplate text of Titles. Example: “PATIENT AGE.” Objects are typed into the boilerplate text of a Title, enclosed by ‘&#124;’s.  For example, suppose a Title has the following boilerplate text:  Patient is a healthy &#124;PATIENT AGE&#124; year old &#124;PATIENT SEX&#124; ...  Then when you enter such a note for a patient known by the system to be 56 years old and male, you would be presented with the text:  Patient is a healthy 56 year old male ...  - You can then add to the text and/or edit the text, including the age (56) of the patient. From this point on, the patient age (56) is regular text and is not updated in this note. - Objects must always have uppercase names, abbreviations, and print names. When embedding objects in boilerplate text, you may embed any of these three (name, abbreviation, print name) in boilerplate text, enclosed by an “&#124;” on both sides.  Objects must always be embedded in uppercase. - Objects are stored in the DOCUMENT DEFINITION File, but are not part of the Hierarchy. They are accessible through the options *Create Objects* and *Sort Document Definitions (* by selecting Sort by Type and selecting Type Object). - TIU exports a small library of Objects. Sites can also create their own. - Only an owner can edit an object and should do so only after consulting with others who use it. The object must be Inactive for editing. It should be thoroughly tested. (See Object Status, under Status.) - Entries of type Object cannot be changed to any other type.  Entries of type Class, Document Class, Title, or Component cannot be changed to type Object. - Type is a BASIC field.  #### SHARED  Components may be designated SHARED by Owners who have the Manager menu. This means the Component can be an item under multiple parents, and anyone who owns a Title can add it as an item.  - Shared Components are the *only* members of the Document Definition hierarchy which can appear in more than one place in the hierarchy. (Objects can be used in multiple entries, but are not members of the hierarchy.) - Shared Components are intended for broad use across the site, such as a Privacy Act Component. Since a Shared Component may be used in many different Document Definitions, its Owner is essentially the caretaker for it, hospital wide, and must consider all users before editing it. Users who disagree with a proposed change can choose to create and use their own copy instead of using the Shared Component. - Parents of a Shared Component are listed on the Detailed Display screen. - Shared Field values are 1 for YES and 0 for NO, with a default value of 0 for NO if the field is empty.  ##### Document Definition Terminology cont’d  - An entry may not be designated Shared unless it is a Component. Only a Manager or an Owner can designate a Component as Shared. Only an *owner* can edit it. (Normally Managers can override ownership and edit entries. Manager options do *not* override Ownership for editing Shared Components). - Shared Components can only be edited from *the Sort Document Definitions* option. - Shared Components can’t be deleted. If they don’t have multiple parents, they can, however, be edited to *not* shared and *then* deleted, assuming they are not In Use by documents and the parent is Inactive. - Shared Components don’t have a Status. They can be edited only if all parent Titles are Inactive. This ensures that parent Titles are offline for entering documents while their components are being edited. Parents are listed on the Detailed Display Screen. - If a Shared Component has subcomponents, they are automatically Shared, since they, with their parents, can be used in more than one place in the hierarchy.  *Sharing of Document Definitions other than Components is not permitted because it unduly restricts the owner’s right to edit or delete the Document Definition and adds undue complexity to the Hierarchy*  #### NATIONAL STANDARD  - Some Document Definitions such as CWADs are developed nationally and sent out as standardized entries across the nation. TIU and other packages depend on their standard definition, and they must not be edited by sites, but only by the persons who are nationally responsible for them. - Such entries are marked NATIONAL STANDARD (the field has a value of 1 for YES), which prevents sites from editing the entry. - Sites can’t edit National Standard entries, except for the Item Multiple. - If a National Standard entry is a Class or Document Class, sites can add or delete non-National items as they please, and can edit all items as items (e.g., Item Sequence, etc.). Sites cannot add or delete National items. - If a National Standard entry is a Title or Component, sites can’t add or delete items, but they can still edit items as Items. - Sites cannot add National Standard entries as Items to parents except for adding National Shared Components to non-National titles. Sites can delete National Standard Items from any non-National parents. (Unless there has been a mistake, such items will be limited to Shared Components.) - Field is NOT heritable. If field has no value for an entry, its value is 0 by default. This means that entries created by sites are *not* National Standard.  Technical Note: National entries (except for Shared Components) must have National ancestors; if a National entry has a non-National ancestor, TIU doesn’t permit it to be activated. (Shared Components need not have National ancestors, and do not have a Status.)  National Standard is a basic field.  ##### Document Definition Terminology cont’d  ###### STATUS  - Status provides a way of making Document Definitions “Offline” to documents. Document Definitions need to be offline if they are new and not ready for use, if they are being edited, or if they are retired from further use. - Status is limited to those Statuses in the STATUS File which apply to Document Definitions: Inactive, Test, and Active. TIU further limits the Status to those appropriate for the entry Type (see below), limits the Status of entries with Inactive ancestors to Inactive, and limits the Status of faulty entries to Inactive. - Status applies to all Document Definitions, but its meaning and possible values vary somewhat with the Document Definition Type. Object Status differs significantly from status of other Types. See Object Status, at the end of this description. Also see Component Status below, to see how Shared Components differs.  ##### TITLE STATUS  - Status has its most basic meaning for Titles. - A Title can have a Status of Inactive, Test, or Active. If its Status is Inactive, it can’t be used to enter Documents ( *except* through the Try Action, which deletes the document when done). If its Status is Test, only its Owner can can enter documents. Titles should be tested using *test patients only* . If a Title’s Status is Active, anyone with access and authorization can enter documents.  NOTE on Availability: Although Status affects availability for entering documents, there are other factors which also affect availability: A Document Definition is not available to a given user for entering documents (except throught the Try action) unless all of the following three criteria are met:  1. It is a Title. 2. It has a Status of Active or Test. If its Status is Test, the user entering a document must own the Title. 3. If authorization for using the Title to enter documents is restricted through the Authorization/Subscription Utility (Business Rules), the user must be a member of the authorized user class.  - Unless these criteria are all met, users trying to enter documents will not see the Document Definition. Therefore, it is wise to warn users when taking definitions offline for edit to do so at non-peak hours for entering documents. - When you are changing a Title’s Status to Test or Active, the Title is examined for rudimentary completeness and must be judged OK before the change takes place. You can perform the same examination by selecting the action Try. For Titles, the Try action also lets you enter a document on the entry. The document is deleted immediately after the check. - Although availability for entering documents is the central meaning of Status, Status also controls edit and deletion of Document Definitions. A Title can be edited *only* if its Status is Inactive, ensuring that no one is using it to enter a document while its behavior is changing. Titles can be deleted only if their Status is Inactive.  NOTE: 	Although Status affects Editing ability, it is not the only factor affecting editing. If an entry is already IN USE by documents, editing or deletion is restricted to aspects which will not harm existing documents.  - Components under a Title have the same status as the Title. When a Title’s status is changed, the statuses of its descendant Components are automatically changed with it.  ##### CLASS AND DOCUMENT CLASS STATUS  - Classes or Document Classes can have Active or Inactive Statuses. - “Basics” for a Class or Document Class can’t be edited (except for Owner and Status) unless it is Inactive. Since Inactivating a Class or Document Class automatically inactivates its descendants, this ensures that all Titles which inherit behavior from it are neither Active nor Test and are thus Offline while inherited behaviors are edited. - In contrast to Basics, the ability to add or edit items of a Class or Document Class depends on the Status of the item, not its parent; it is not necessary to Inactivate a Class such as Progress Notes in order to edit or add items. - Activating a Class or Document Class differs from Inactivating the Class or Document Class. When a Class/Document Class is activated, its descendants may have any Status which their Type permits; they are not required to be Active. Hence, they are not automatically Activated when the parent is Activated.  ##### COMPONENT STATUS  - A Component has the same status as its parent. Its status can be changed only by changing the Status of its Parent, if it has one. Components without parents are always Inactive.  NOTE: 	The above also means that Test or Active Titles can’t have Inactive Components. In other words, Inactivating a Component is *not* a way of retiring it. If a Component is no longer a useful section of a Title, it should be edited so as to make it useful, or it should be deleted *as an item* from the Title of which it is a part. As with all retired Document Definitions, it should *not* be deleted from the file if it has been used by documents.  - Components can be edited only if their status is Inactive. This ensures that all Titles using them are offline while they are being edited. - Shared Components are a special case since they can have multiple parents. *They do not have a status.* They can be edited only when all parent Titles have a Status of Inactive. (The Detailed Display screen shows parents.) This ensures that all parent Titles of Shared Components are offline while the components are being edited. Edit of Shared Components is permitted only through the option *Sort Document Definition.*  ###### Document Definition Terminology cont’d  - Editing Shared Components is severely restricted by Ownership, since they may be used multiple times and across the site. Even an Inactive Status does not permit those with the Manager menu to override ownership and edit a Shared Component they don’t own. See the description of Shared Components under Type.  ##### OBJECT STATUS  - Objects can have Inactive or Active Statuses. Only Active objects function.  That is, if you enter a document on a Title with boilerplate text containing an inactive object, the object doesn’t do anything. You see the name of the object and an error message in place of the object data. - Only Active objects should be embedded in boilerplate text.  Exception: when objects are being created or edited. Otherwise, you should NOT embed inactive objects in boilerplate text since they may not be ready for use and since they do not function when users enter documents against them. Titles whose boilerplate text contains inactive objects can’t be activated. (This doesn’t imply that active titles never have inactive objects embedded in them, since users can, after a warning, inactivate objects even when they are embedded in active titles.) - Only Inactive objects can be edited (and only by an owner).  Only an owner can activate or inactivate an object. (Exception: if you own an object and edit the owner to someone else, then you are not prevented from going on to edit the status in the same edit session, since you were the owner a few seconds ago.) Active objects are assumed to be ready for use in any boilerplate text. - Since the owner is essentially the caretaker of the object for the entire site, the owner should consult with all who use it before editing it.  An object can be tested by embedding it in the boilerplate text of a Title and selecting the action “Try” for the Title.  It need not have an Active status for this testing (and should not have an Active status until testing is complete). Owners who inactivate objects for editing should make sure to reactivate them if they are being used. - Sites should either inactivate relevant Titles before editing objects or edit objects only when users are not likely to be entering documents since Inactive objects do not function. - *If a site changes the name or behavior of an Object, it is up to the site to change the name wherever it has already been embedded in Boilerplate Text, and to inform users of the change.* - An object which is no longer wanted for future documents can be removed  from the boilerplate text of all Titles and Components and then deleted from file 8925.1.. Only an owner can delete it. All of the documents that used it have already got it in hard words so there is no need to keep it for their sake. Old Objects should be edited so they are useful, or deleted, not kept around forever as Inactive.  ###### Document Definition Terminology cont’d  ##### PERSONAL OWNER  - Document Definition Ownership has nothing to do with who can *use* the entry  to enter a document. It determines responsibility for the Document  Definition itself. - An entry can be edited by its owner. The Manager menu permits override of ownership so that ownership can be assigned to a clinician who can then fill in boilerplate text, while the Manager can still edit the entry, since there are many fields the clinician doesn’t have access to. Exception: the Manager menu doesn’t allow override of Object or Shared Component ownership. Only owners can edit Objects and Shared Components, regardless of menu. - If a Title owner edits the boilerplate text of the Title, that person can edit the boilerplate text of all components of the Title as well, without regard to component ownership. In order to edit components individually, however, the user must own the component. This allows users to assign ownership of components to different people, for example, for future multidisciplinary documents. - A Personal Owner is a person who uniquely owns the entry. An entry may have a Personal Owner *or* a Class Owner but not both. When entering a Personal Owner, be sure to delete any existing Class Owner. - TIU uses the term “Individual Owner.” Someone is an Individual Owner of an entry if s/he is the personal owner or if the entry is CLASS Owned, if s/he belongs to the Owner Class. - When you enter a new entry, you are entered as the Personal Owner if you don’t assign ownership. You can then reassign ownership if desired. Copying an entry makes you the personal owner of the copy. - If the person responsible for an entry plays a role corresponding to a User Class, e.g. Clinical Coordinator, it may be more efficient to assign  ownership to the class rather than to the person. Owners are then automatically updated as the class is updated. - Editing privilege is affected not only by Owner but also by Status, by Shared, by In Use, and by menu access. Manager menus, for example, provide fuller editing capabilities than Clinician menus.  ###### CLASS OWNER  - Document Definition Ownership has nothing to do with who can USE the entry to enter a document. It determines responsibility for the Document Definition itself. - An entry can be EDITED by its owner.  (The Manager menu permits override of ownership so that ownership can be assigned to a clinician (person with Clinician Menu) who can then fill in boilerplate text, while the manager can still edit the entry, since there are many fields the clinician does not have access to.)  Exception: the Manager menu does NOT override ownership of Objects or of Shared Components. These can ONLY be edited by an owner, regardless of menu. - If a Title owner edits the boilerplate text of the Title, that person can edit the boilerplate text of all components of the title as well, without regard to component ownership. However, the user must own the component in order to edit it individually, permitting separate ownership of components. - A Class Owner is a User Class from the USR CLASS file whose members may edit the entry.  An entry may have a Personal OR a Class Owner (not both). TIU doesn’t prompt for Class Owner if the entry has a Personal Owner. To change to Class Owner, first delete the Personal Owner by entering '@' at the Personal Owner prompt. - For new entries, you are prompted to enter the Class Owner Clinical Coordinator as the default. To enter a different Class Owner, enter the appropriate class after the //'s.  If there are no //'s and the Replace...with editor is being used, enter ... to replace the whole class and then enter the appropriate class. - Class Owner is a BASIC field.  ###### IN USE  - IN USE applies to all entries except Objects.  It can’t be edited since it gets its value automatically. - IN USE may have values of “Yes,” “No,” or “?.” - Titles or Components are IN USE (Yes) if there are entries in the TIU Document file which store it as their Document Definition. If not, it is *not* used (No).  NOTE: 	It is possible for Document Definitions to be used by documents in files other than the TIU Document File and still be *Not In Use,* since In Use means in use by documents in the TIU Document file..  - Classes or Document Classes are IN USE (Yes) if they have children which are Titles which are IN USE. That is, it is Used by Documents (Yes) if there are entries in the TIU Document file which inherit behavior from it. If not, it is *not* used (No). - In Use has a value of ? for a DOCUMENT DEFINITION File entry if the routine TIUFLF is missing or if the program encounters a nonexistent item and the entry is not IN USE so far as the check has been able to go.  NOTE: 	Since Shared Components can be items of more than one Title, a Shared Component may be IN USE even when a particular parent Title is *not* IN USE. This simply means that it is also a Component of another Title which *is* IN USE.  - If IN USE is “No” for a particular Document Definition entry, the entry can be deleted by the owner without harming documents in the TIU DOCUMENT File #8925. Deleting it will, however, orphan any descendant Document Definitions.  NOTE: 	If a site is using TIU to upload documents into a file other than the TIU DOCUMENT file, it may create Document Definition entries to store upload information. For example, it may create an Operative Reports title containing instructions for uploading documents into the Surgery file. These document definitions will be orphans and will be not In Use. They must NOT be deleted from the Document Definition file.  - Deleting Objects will not harm existing documents, but *will harm* future documents if the Object is embedded in existing Document Definition Boilerplate Text. - If IN USE has a value of “Yes” or “?,”TIU doesn’t permit the entry to be deleted. Deleting the entry would cause documents in file 8925 not to function. This is true even if the entry has an Inactive status and documents are no longer being written on the entry.  **Technical Note:** A Document Definition of Type Title or Component is IN USE only if it appears in file 8925’s ‘B’ Cross Reference.  - IN USE is a Basic field.  ###### HAS BOILTXT  - Applies to Title and Component only. This field can’t be edited since its value is automatic. A Document Definition Has Boiltxt if it or its descendant Components have Boilerplate Text (Field 3).  ###### PRINT NAME  - Print Name is the name used in lists of documents.  For Titles, Print Name is used as the document Title in the Patient Chart.  ###### ORPHAN  - Orphan applies to Document Definitions of all Types except Objects and Shared Components. - Orphan is not editable since it gets its value automatically. - Document Definitions are Orphans if they do not belong to the Clinical Documents Hierarchy, i.e., they cannot trace their ancestry all the way  back to the Class Clinical Documents. If an Orphan is not In Use, it may be “dead wood” which should be deleted from the file. Orphans not In Use which should not be deleted include those being kept for later possible use, those temporarily orphaned in order to move them around in the hierarchy, and those used for uploading documents into files other than the TIU Document file. (Orphan doesn’t apply to Objects since they don’t ever belong to the hierarchy. Orphan doesn’t apply to Shared Components since they may have more than one line of ancestry.) - Orphan doesn’t apply to Objects since they don’t ever belong to the hierarchy. Orphan doesn’t apply to Shared Components since they may have more than one line of ancestry.  NOTE: 	The DOCUMENT DEFINITION file may contain orphan entries which are not used by documents in the TIU DOCUMENT file but which contain upload instructions for storing documents somewhere else.  For example, if a site is uploading Operative Reports into the Surgery file, there may be an orphan Operative Report Document Definition in the DOCUMENT DEFINITION file. These should NOT be deleted just because they are orphans. Such entries can be identified by viewing them through Detailed Display in the Sort Option and looking for Upload fields.  NOTE: 	Orphan, as used in TIU, doesn’t mean having no parents. For example, suppose Exceptional Day Pass Note has a parent named Day Pass Note. If Day Pass Note has no parent, then Exceptional Day Pass Note can’t trace its ancestry back to Clinical Documents and is an Orphan even though it has a parent.  - Orphans are invisible to TIU users and can’t be used to enter documents. - When an item under a non-orphan is deleted as an item, it becomes an orphan. TIU doesn’t permit non-orphan entries to become orphaned if they are In Use. Titles already used but being retired from further use should be Inactivated, NOT orphaned. Components are a different story. Components being retired from further use can and should be orphaned  (deleted as items from the Title).  This Is because Titles inherit attributes and therefore require a complete ancestry in order to process existing documents. Since components, on the other hand, do not inherit attributes, they do NOT require a complete ancestry to process existing documents (although they must remain in the file.) - Since Orphans don’t belong to the hierarchy, they do *not* appear on the *Edit Document Definitions* option. They can be accessed through the *Sort Document Definitions* option.  NOTE ON DISPLAY OF HERITABLE FIELDS:  Most Technical fields are heritable, and Basic field Suppress Visit   Selection is heritable. Upload fields are heritable as a group. The display does not show inheritance for Upload fields.)  The Document Definition Detailed Display action displays the EFFECTIVE value of inherited fields. If an inherited field does not have its own  explicit value, its effective value is its inherited value. If it doesn’t have an inherited value, its effective value is the default value for the field. If the field doesn’t have a default value, it doesn’t have an  effective value and the field display is blank. Values marked with * have been inherited.  For EDITING heritable fields, see the Technical field Edit Template.  ###### ABBREVIATION  Abbreviation can be entered at the “Select Title” prompt when entering a document. Since all Titles with the given abbreviation will then be listed, Abbreviation can serve to group Titles.  ###### IFN  The Internal File Number is the number of the entry in the TIU Document Definition File. IFN is included in the display to help programmers with debugging.  ###### Items  Items are Document Definitions listed under other Document Definitions in the hierarchy; e.g., Progress Notes and Discharge Summary are items under Clinical Documents. The Type of the parent entry determines what Types of items it has. A Class parent entry has items of Classes or Document Classes. A Document Class entry has Titles as items. If a Title entry has more than a single section, it has  items of Components. Components may also be multi-sectioned with Component items. Objects do not have items.  ###### Mnemonic  Mnemonic is a 1-4 character shortcut for selecting Classes or Document Classes from a menu. Mnemonics are usually numeric with the same value as the Sequence. Alpha mnemonics are also permitted.  ###### Sequence  Sequence, if entered, determines an item’s order under its parent. If items have no sequence, item order is alphabetic by Menu Text. Sequence is a number between .01 and 999, with two decimal places allowed.  ###### Menu Text  Menu Text is the short name (1 - 20 characters) you see for Classes and Document Classes when selecting them from 3- column menus which are seen when viewing documents across many patients and when viewing many kinds of documents at the same time (e.g. Progress  Notes and Discharge Summaries).  You can edit Menu Text for selected items. Menu Text can affect the item order under a parent, since order is alphabetic  by menu text if items don’t have sequence numbers. To edit NAME (rather than Menu Text), go back to the previous screen.  ###### BOILERPLATE TEXT  - Sites can preload the text field of a document with default text, default format, overprint data which is presented to you when you enter the document. You can then edit and/or add to the boilerplate text. - If a document is formatted into columns, you should use replace mode rather than insert mode (or Find/Replace Text) to preserve the columns. - Field may be used as an alternative to components to split a document up into sections, but such sections are stored together and can’t be separately accessed the way components can.  See Component, under Basic field Type. - Boilerplate Text is the place to embed objects which get data from the relevant package (e.g., the Laboratory package). See Object, under Basic field Type. - A document with multiple components can have boilerplate text in the entry itself and/or in any component. Boilerplate text in the entry itself appears first.  ### Troubleshooting &amp; Helpful Hints  #### FAQs (Frequently Asked Questions)  (based on questions from TIU/ASU test sites)  **Q:** Under very extreme conditions, such as a workstation disconnect while a document is being saved, documents are lost. How can we recover?  **A:** A Patient Safety Issue (PSI-04-016) has been opened for this problem and patch TIU*1*186 has been issued to correct this problem. With this patch both the original note and any corrections recorded by the main computer are kept in the Document File #8925. You can recover the document if you access the global before an attempt is made to edit the note again.  In this example document number 550 is being accessed for recovery purposes:  &gt;D ^%G  Global ^TIU(8925,550,  TIU(8925,550,  ^TIU(8925,550,0) = 158^23^699^107^7^^2970618.073722^^^0^^^H  ^TIU(8925,550,12) = 2981110.072632^4546^^4546^4^^^^^^3  ^TIU(8925,550,13) = 2981110.072632^4546^D^2981110.072636  ^TIU(8925,550,14) = ^^^1043  ^TIU(8925,550,15) = 2981110.072639^4546^e!'0A)/sULz^.]LZlo!^E  ^TIU(8925,550,150) = 119W-TEST  ^TIU(8925,550,"TEXT",0) = ^^1^1^2981110^  ^TIU(8925,550,"TEXT",1,0) = Here is the document text.  ^TIU(8925,550,"TEMP",0) = ^^1^1^2981120^  ^TIU(8925,550,"TEMP",1,0) = Here is the temporary text.  Global ^  **Explanation:**  Before patch TIU*1*186, when CPRS began to pass an edited document back to the server, TIU would immediately delete the original document (the TEXT global). The copy on the client (CPRS) machine was then the only existing version of the document. If the client/server lost connection for any reason before the resave proceeded, the entire document was lost. If the client/server lost connection during a resave, whatever text that was transferred before the lost connection would be stored in the TEMP global.  When a user reconnected and viewed the document (only via CPRS, LM did NOT do this), all the TEMP information was automatically placed back into the TEXT global.  This was transparent to the user.  Whatever information made it to the server would be there, whatever didn’t was irretrievably lost.  Now with patch TIU*1*186, it waits until the entire document (all pages) are transferred back before touching the TEXT node. If the client/server loses connection for any reason, the original is intact and untouched. If the client/server loses the connection in the middle of a resave, all the contents that were successfully transferred are stored in the TEMP global—whatever edits didn’t make it are lost.  When the user reconnects and views the document in CPRS, the original document is still there fully intact and the data in the TEMP global remains untouched **as long as the user does NOT attempt another edit** .  The server replaces the original with the edited copy only when all pages of an edit are transferred completely. This information may be retrieved by the IRM staff if needed as shown in the example above.  The two major changes are:  1. The original document remains intact up until the entire edited new version is fully transferred to the server. 2. The edited contents that were previously saved in the TEMP global no longer automatically replace the TEXT node until after the complete transfer is complete.  **Q:** We just entered all of our Providers into the Person Class File #8932.1 (when the Ambulatory Care Reporting Project came out). Do we have to do this all over again for the User Class file in ASU? Why can’t TIU and ASU just use the Person Class?  **A:** The Provider Class in ASU fulfills a different function, and therefore its database design is a different kind of hierarchy.  A patch to ASU in the near future will help assure that your efforts in populating the Person Class Membership at your site are not lost, or repeated. We are developing a mapping between a subset of the exported User Classes and the Person Class File (i.e., for each Person Class, there will be a corresponding User Class), which will help you “autopopulate” User Class Membership, assure that future changes to an individual’s Person Class Membership are reflected automatically in his User Class Membership, and allow resolution of privileges for inter-facility access to data. We recommend that you initially implement TIU and ASU by populating only the most essential User Classes (i.e., Provider; MRT; Chief, MIS; and Transcriptionist), and use the forthcoming patch to assist you in autopopulating more specific User Classes when you have become acquainted with the two products.  **Q:** Do we have to delete or sign unsigned notes before we can convert them?  **A:** No, you don’t have to delete or sign the unsigned notes.  The conversion will move them as is.  However, you probably don’t want to be moving old, irrelevant notes from one package to the other. By the way, notes for test patients are NOT movedthey are ignored.  **Q:** Can we require a Cosignature for a particular note?  **A.** Yes, you can set Cosignature requirements for document classes or titles. Use the option *Document Parameter Edit* , as described on page 30 in this manual. Individual clinicians can designate an expected Cosigner through their *Personal Preferences* option.  **Q:** Can we allow surrogates for alerts to sign notes.  A.  Yes. The following business rule will allow this:  A COMPLETED (TITLE) "Any\_Title" MAY BE SIGNED by a SURROGATE  This rule can be added at any level in the TIU Document Definitions Hierarchy.  **Q:** Why do we have to enter Visits and encounter data for Progress Notes? What are “Historical Visits”?  **A:** Visit data is now required for every patient encounter. The vast majority of Progress Notes are already linked to an admission and don’t require additional visit information to be added.  A historical visit or encounter is a visit that occurred at some time in the past or at some other location (possibly non-VA). Although these are not used for workload credit, they can be used for setting up the PCE reminder maintenance system, or other non-workload-related reasons.  NOTE: 	If month or day isn’t known, historical encounters will appear on encounter screens or reports with zeroes for the missing dates; for example, 01/00/95 or 00/00/94.  **Q:** Are there any terminal settings that we need to be aware of for TIU?  On the VT400 setting in Smart Term, the bottom half of the Create Document Definitions screen was not scrolling properly. It was writing over previous lines and got very confusing!  **A:** Various terminal emulators can affect applications using the List Manager interface.  The VT220 and 320  work very well with List Manager.  **Q:** I have gotten my 600 clinic and ward locations set up, but when I try to print by ward I am only allowed to print to a printer. This is not true under the Print by Hospital Location, where I can print to the screen. What is the difference?  **A:** Print by Ward is designed to support batch printing. It has the unique ability to determine when the last note was printed so that sites can now capture the infamous “orphan” note which was a problem under Progress Notes 2.5. You might consider adding a message on entry into the option to inform users that they can only print to a printer (not on screen).  **Q:** Can we share business rules with other sites.  **A:** It isn’t yet known how appropriate or desirable it is to share business rules amongst sites. The package is exported with all the business rules needed to run the standard package. The differences are usually on a medical center basis.  For example, one site wants all users to be able to see all UNSIGNED notes. ON the flip side, another site doesn’t want any users to be able to print or view UNCOSIGNED notes until the cosigner has signed.  Two very different views. Just because you are in the same VISN doesn’t mean you would view these issues in the same light. Another example is the hospital that wants to restrict the entering/viewing/ printing of every Progress Note by TITLE. You can do this, but it is not something we would recommend.  **We strongly recommend that you work with the exported business rules for a while before making any changes.**  **Q:** When I read my Discharge Summaries after they come back from the transcriptionist, there are dashes (or other funny characters) sprinkled throughout; what do these mean and what am I supposed to do?  **A:** These characters (your site determines whether they will be dashes, hyphens or some other character) indicate words or phrases that the transcriptionist was unable to understand. You need to replace these with the intended word or phrase before you’ll be able to sign the document.  **Q:** What is the best editing/word-processing program and how can I learn how to use it?  **A:** This is partly a matter of personal preference and partly a matter of what’s available at your site. Commercial word-processors are available at some sites. The FileMan line editor and Screen Editor are available at all sites. Of these two, most Discharge Summary users prefer the Screen Editor. Your IRM office or ADPACs can help you get set up with the appropriate editor and provide training. The Clinician Quick Reference Card summarizes the FileMan Screen Editor functions.  **Q:** Why should a site require “release from transcription”?  **A:** Release from transcription is required to prevent a discharge summary from becoming visible to other users before the person entering the summary has completed the entry. For example, if a transcriptionist needed to leave the terminal, the summary would not be available for anyone else to look at until the summary is “released from transcription.”  **Q:** Why can’t we use extended ASCII characters (e.g., °, ≥, ∆, etc.) in our documents to be uploaded?  **A:** These alternate character sets are not standardized across operating systems and your MUMPS system may not be set up to store them.  ##### Questions about Reports and Upload  **Q:** At present we put all discharges in the Discharge Summary package.  We do allow Spinal Cord Injury to put “interim” summaries in on their patients every 6 months or annually. These reports stack up under the admission date and are all under that one date upon discharge.  When patients are transferred to the Intensive Care Units, they may have a very long/complicated summary to describe the care while in the unit. This should be an interward transfer note, but some of our physicians feel that due to the complexity of care delivered in the unit, this should be included in their Discharge Summary, BUT should have its own date (episode of care).  I realize that the interward transfer note is a progress note and very few of our physicians are using progress notes. Our physicians seem to want to have that interward transfer information in these complex cases attached to the Discharge Summary.  My question is will TIU offer us anything different that will satisfy our physicians? I still do not have a mental picture of what it will look like when I go to look up a DCS or PN from the TIU package. Will the documents be intermingled and arranged by date? I am a firm believer in calling things what they are and putting them where they belong when it comes to organizing our electronic record. I hate to see the DSC and interward transfers go together now in the DCS package as it does create a problem when the patient is actually discharged and Incomplete Record Tracking (IRT) thinks he was discharged when the interim was written. Does anyone have any thoughts and can someone show me how it looks when I get TIU and look up documents on a patient?  **A:** From: Joel Russell, TIU Developer  Interim Summaries may be easily defined in TIU, and linked with the corresponding IRT deficiency.  Parameters determining their processing requirements, as well as the format of a header for uploading them in mixed batches with Discharge Summaries, Operative Reports, C&amp;P exams, and Progress Notes can all be defined without modifying any code. A patch will be necessary to link them to a specific transfer movement, and to introduce a chart copy of the appropriate Standard Form. This involves a modest programming effort, but will have to be prioritized along with a number of other requests.  **Q:** We need the help of the user community to try to sort out the relative priorities of each of these tasks, along with your patience, as we work to deliver as many of them as possible, as timely as possible...  **A:** From a user/coordinator  A possible solution to the problem of rotating residents is to set up your summary package with the author not needing to sign the summary.  This allows the attending physician to sign the report. While the residents may rotate in and out, the attending usually remains the same through the course of the patient’s stay.  **Q.** What are sites doing with C&amp;Ps, &amp; op notes?  It is my understanding that C&amp;Ps are a type of discharge summary.  I’ve tried creating “C&amp;P EXAM” as a title underneath the “DISCHARGE SUMMARY” document class. I get TYPE errors when uploading test documents. The document parameters are defined for the upload fields.  **A:** *From a user/coordinator:* OP reports and C&amp;P exams reside in their appropriate packages. You can use the TIU upload utility to put them there.  As for OP notes, we have several titles (i.e. Surgeon’s Post-OP note).  Do you have TIU in the APPLICATION GROUP field of the Surgery and C&amp;P file?  Our FILE File has this for our Surgery file:  NUMBER: 130                             NAME: SURGERY  APPLICATION GROUP: GMRD  APPLICATION GROUP: TIU  **Q:** Can we do batch upload of Progress Notes by vendor through TIU?  **A:** Yes, you may now batch upload Progress Notes through TIU. See instructions earlier in this manual (under Setting Parameters) or in the TIU Technical Manual.  **Q:** Currently our Radiology reports are uploaded by the vendor. Can this functionality be built into TIU?  **A:** You may upload Radiology Reports, but it will be necessary to write a LOOKUP METHOD to store several identifying fields in the Radiology Patient File. The remainder are stored in the Radiology Reports File, along with the Impression and Report Text. (The TIU and Radiology development teams will work together on a lookup method, as development priorities allow.)  **Q:** We have hundreds of entries in file 128 to be cleaned up, because many duplicate discharge summaries were mistakenly uploaded by the transcriptionists of our vendor. How can we clean up these files?  **A:** You can use the *Individual Patient Document* option on the GMRD MAIN MENU MGR menu, along with VA FileMan, to clean up the Discharge Summary files.  ##### Questions about Document Definition (Classes, Document Classes, Titles, Boilerplate text, Objects)  **Q:** After the initial document definition hierarchy is built and used, can we modify the hierarchy structure if we feel it is incorrectly built? How flexible is this file?  **A:** Once entries in the hierarchy are in use, you can’t move them around. It would be wise to think your hierarchy through before installation. Don’t rush the process. If necessary, create new classes, document classes, and titles (the Copy function streamlines creating new titles), and deactivate the old ones. The users won’t be aware of the change if the Print Name is the same, but the .01 Name is new.  **Q:** Who creates titles and boilerplates at a site?  **A:** Many test sites restrict the creation of titles and boilerplates as much as possible. At one site, users submit a request for a title or boilerplate. IRMS or the clinical coordinator create the boilerplate and/or title and forward it to the Chairman of the Medical Records Committee for approval. Once approved it is made available for use. Titles are name-spaced by service and the use of titles is restricted by user class. With the ability to search by title, keeping the number of titles small and their use specific can be very useful;. e.g. patient medication education is documented on an electronic progress note and can be reviewed easily.  Some of the other sites allow the ADPACs to create boilerplates without going through such a formal review process. Another site restricts this function to the Clinical Coordinator. It was designed so that sites can do whatever they are most comfortable with.  **Q:** The root Class supplied with the package is CLINICAL DOCUMENTS. Can a peer class level be made using our configuration options?  Ex: ADMINISTRATIVE DOCUMENTS  **A:** You cannot enter a class on the same level as Clinical Documents. In TIU Version 1.0, entries can only be created under Clinical Documents.  **Q:** I’ve changed the technical and print names for a Document Class, but it doesn’t seem to have changed when I select documents across patients. What am I doing wrong?  **A:** When you select documents across patients, you are presented with a three-column menu. The entries in this menu are from the Menu Text subfield of the Item Multiple. To make a consistent change, you must update Menu Text as well as Print Name when you change a Document Definition name.  **Q:** How can I print when I’m in Document Definitions options?  **A:** All Document Definitions printing is done using the hidden actions Print Screen and Print List. First, locate the data to be printed so that it shows on the screen and then select either the action PS or PL. To locate the appropriate data use the Edit, Sort, or Create option to list appropriate entries.  To print a list, select the PS or PL action at this point. To print information on a single given entry, first locate the entry in one of the above lists, then select either the Detailed Display action or the Edit Items action. Edit View shows all available information for a given  entry. Edit Items shows the items of a given entry. Then select PS or PL. Enter PS for Print Screen to print the current display screen. It *only* prints what is currently visible on the screen, ignoring information that can be moved to horizontally or vertically (pages), so you should move left/right and up/down to the desired information before printing.  Enter PL for Print List to print more than one visible screen of information. Print List prints the entire vertical list of entries and information, including entries and information not currently visible but which are displayed when you move up or down. If the action is selected from the leftmost position of the screen, you’re asked whether to print ALL columns or only those columns visible on the current leftmost position of the screen. If you select the action after scrolling to the right, only the currently visible left/right columns are printed.  **Q:** Is it possible for sites to share objects they create locally?  **A:** As sites develop their own Objects, they can be shared with other sites through a mailbox entitled TIU OBJECTS in SHOP,ALL (reached via FORUM).  #### Facts Helpful information  ##### TIU NIGHTLY TASK  **Text Integration Utility Nightly Task**  This option should be scheduled to run nightly.  The task performs several maintenance functions and sends alerts on overdue signatures.  If a Discharge Summary has no discharge date the options checks the Patient Movement File and if it has a discharge date, it updates the discharge date for the Discharge Summary note in file 8925 with that date.  If the TIU Upload buffer (8925.2) contains records that are older than 30 days the nightly task deletes the entry in file 8925.2 and the alert associated with it.  The option generates alerts for past due signatures, cosigners and additional signers.  NOTE: Although the following parameters are set at the division level, the TIU NIGHTLY TASK which determines when OVERDUE alerts are sent recognizes the parameters set for one division only: the division of the person who scheduled the Nightly Task.  - **GRACE PERIOD FOR SIGNATURE:** - START OF ADD SGNR ALERT PERIOD: - **END OF ADD SGNR ALERT PERIOD** : - **LENGTH OF SIGNER ALERT PERIOD** :  ##### Mnemonics on List Manager screens  The TIU and ASU packages don’t use mnemonics (abbreviations or numbers) for actions (protocols) on List Manager screens, partly because it’s difficult to make them consistent with other packages and with what users expect. Sites, however, can feel free to add whatever their users would like to have (e.g., $ for Sign).  ##### Shortcuts  At any “Select Action” prompt, you can type the action abbreviation, then the = sign and the entry number (e.g., E=4).  Jump to Ddef in the Edit Document Definition option takes you directly to a document definition (Class, Document Class, or Title) if you know the name.  ##### Visit Information  When you enter a Progress Note for an outpatient, this Progress Note now needs to be associated with a “visit.” For the majority of Progress Notes, this visit association is done in the background, based on Scheduling or Encounter Form data.  If a visit has already been recorded for the date your Progress Note refers to, but the Progress Notes wasn’t linked (e.g., for standalone visits such as telephone or walk-in visits), you can select a visit from the choices presented to you during the PN dialogue. If no visit has been recorded, you must create a new visit. See the example below.  Other information, such as background, definitions, and other information about visits follow the example.  ###### Example: Entry of Progress Note  Select Patient(s): **CPRSPATIENT** ,THREE          09-12-44        000000003       YES      SC VETERAN  A: Known allergies  For Patient CPRSPATIENT,THREE  TITLE: **Adverse React** Adverse React/Allergy  This patient is not currently admitted to the facility...  Is this note for INPATIENT or OUTPATIENT care? OUTPATIENT// **&lt;Enter&gt;**  The following VISITS are available:  1&gt;  FEB 24, 1997@09:00                       DIABETES CLINIC  2&gt;  SEP 05, 1996@10:00                       CARDIOLOGY  CHOOSE 1-2 or &lt;N&gt;EW VISIT  &lt;RETURN&gt; TO CONTINUE  OR '^' TO QUIT: **N**  Creating new progress note...  Patient Location:  NUR 1A  Date/time of Visit:   14:29  Date/time of Note:  NOW  Author of Note:  CPRSPROVIDER,SIX  ...OK? YES// **&lt;Enter&gt;**  SERVICE: MEDICINE// **&lt;Enter&gt;** 111  SUBJECT (OPTIONAL description):  Enter a brief description (3-80 characters) of the contents  of the document.  SUBJECT (OPTIONAL description): **Blue Note**  Calling text editor, please wait...  1&gt;Treatment for allergic reaction to injury.  2&gt;&lt;Enter&gt;  EDIT Option: **&lt;Enter&gt;**  Save changes? YES// **&lt;Enter&gt;**  Saving General Note with changes...  Please Indicate the Diagnoses for which the Patient was Seen:  1      Abdominal Pain  A list of diagnoses  relating to the hospital location (as defined in the AICS package) is presented for you to choose from.  <!-- image -->  3      Abrasion  <!-- image -->  5      Adverse Drug Reaction  6      AIDS/ARC  7      Alcoholic, intoxication  8      Alcoholism, Chronic  9      Allergic Reaction  10     Anemia  ANGINA:  11     Stable  12     Unstable  13     Anorexia  14     Appendicitis, Acute  15     Arthralgia  ARTHRITIS  16     Osteo  17     Rheumatoid  18     Ascites  19     ASHD  20     OTHER Diagnosis  A list of procedures  relating to the hospital location (as defined in the AICS package) is presented for you to choose from.  <!-- image -->  Please Indicate the Procedure(s) Performed:  <!-- image -->  1      Cardioversion  2      EKG  3      Pericardiocentesis  4      Thoracotomy  MISCELLANEOUS  5      Abcess  6      Less than 2.5 cm  7      2.6 - 7.5 cm  8      Greater than 7.5 cm  9      Burns 1 * Local Treatment  10     Dressings Medium  11     Dressings Small  12     Transfusion  13     Venipuncture  UROLOGY  14     Foley Catheter  ENT  15     Removal Impacted Cerumen  16     Anterior, Simple  17     Anterior, complex  18     Posterior  EYE  19     Foreign Body Removal  20     OTHER Procedure  Select Procedure:  (1-20): **19**  You have indicated the following data apply to this visit:  DIAGNOSES:  (ICD-9-CM 995.3)   Allergic Reaction  &lt;&lt;&lt; PRIMARY  PROCEDURES:  65205    Foreign Body Removal  ...OK? YES// **&lt;Enter&gt;**  Posting Workload Credit...  at SCDX AMBCARE EVENT  57033,30772  at SCDX AMBCARE EVENT  57033,30774Done.  ##### Visit Orientation  ###### Rationale  Why associate Progress Notes with Visits? The answer is quite simple:  an event (clinical or otherwise) may be fully described by five key attributes or parameters: Who, what, when, where, and why. Three of these (i.e., who, when, and where), are all encoded in the Visit File entry itself. The remaining two parameters (what, and why), are generally included in the content of the document. This alone would be sufficient justification to adopt a visit orientation, but there are several other benefits.  ###### Benefits  - **The VHA Operations Manual, M-1, Chapter 5** requires that every ambulatory visit have at least one Progress Note. Deficiencies with respect to this requirement can *only* be identified if Progress Notes are associated with their corresponding Visits. - **Inter-facility data transfer** requires identification of the Facility from which the data originated. Because the Facility is an attribute of the Visit file entry, it is not necessary to maintain a reference to the facility with every clinical document. - **Workload Capture,** particularly for telephone and standalone encounters, where the only record of the encounter is frequently a Progress Note, can be easily accommodated, provided that notes are associated with visits.  **“Roll-up” of documentation by Care Episode.** To allow access to all information pertaining to a given episode of care (e.g., for close-out of a hospitalization), a visit orientation is essential.  **Integration with PCE, Ambulatory Care Data Capture, and CIRN.** To accommodate an interface with other clinical data repositories, which may allow query and report generation, based on the existence of a variety of coded data elements, the visit orientation provides a useful associative entity (e.g., a search of PCE to identify all patients with AIHD who were discharged without a prescription for aspirin prophylaxis might identify a cohort of patients for further evaluation. The visit orientation also provides the ability to call for all the cardiology notes entered during the corresponding care episodes could revolutionize retrospective chart review).  ###### Mechanics  The process of associating a TIU document with a visit has been refined to be as simple as possible, and may be modified for any given TITLE, DOCUMENT CLASS, or CLASS by reprogramming the VISIT LINKAGE METHOD for that level of the TIU Document Definition Hierarchy. The existing methods for linking either Discharge Summaries or Progress Notes with visits are outlined below:  ####### Discharge Summaries  *Interactive* Present the user with a list of the selected patient’s admissions, from the Patient Movement File, most recent first, five-at-a-time, in a manner modeled after the Detailed Patient Inquiry, from the PIMS Bed Control Menu. When a given admission is selected, DATA2PCE^PXAPI is called to match or create a corresponding Visit File entry of type Hospitalization.  *Upload* :  Accept a Patient SSN and Admission Date/Time as transcribed in the header of the uploaded summary.  Look-up the corresponding admission from the Patient Movement File (on failure, alert a named group of recipients to correct the header and re-try the filer), and call DATA2PCE^PXAPI to match or create the corresponding Hospitalization Visit as necessary.  **Progress Notes**  *Interactive*  **Current Inpatients:** Default to the current admission and last recorded hospital location. On override, follow procedure described for patients not currently admitted to the hospital.  **Patients not currently admitted:** Ask user whether the note is for Inpatient or Outpatient care. For *Inpatient* care, present the user with a list of the selected patient’s admissions, from the Patient Movement File, most recent first, five-at-a-time, in a manner modeled after the Detailed Patient Inquiry, from the PIMS Bed Control Menu. When a given admission is selected, DATA2PCE^PXAPI is called to match or create a corresponding Visit File entry of type Hospitalization.  For *Outpatient* care, present the user with a list of scheduled appointments from scheduling, most recent first, five-at-a-time. When a given appointment is selected, call DATA2PCE^PXAPI to match or create an AMBULATORY Visit File Entry. If the user indicates he would like to create a new visit, prompt for location, visit date/time, and Visit Type (AMBULATORY, TELEPHONE, or EVENT (HISTORICAL).  Then call DATA2PCE^PXAPI to create a visit as described by the user.  When the user creates such a standalone visit for entry of a note, the program will prompt the user for diagnoses, procedures, and service connection (when appropriate) upon signature, and DATA2PCE^PXAPI will again be called to post the workload data for Ambulatory Care Data Capture.  ##### How many visits are created?  Each TIU document is associated with one and only one visit. To the extent possible, Visit File entries are only created for TIU when absolutely necessary. At the present time, since Registration is not interfaced with Visit Tracking, a Hospitalization type visit will be created with the first inpatient note, and used by every subsequent note associated with that admission, as well as the Discharge Summary, when it is transcribed or uploaded. Since Scheduling is interfaced with Visit Tracking, with Visit entries created on check-out of the appointment, a visit will only be created for scheduled clinic appointments when the note is entered prior to check-out (and Scheduling will match to that visit when check-out does occur). When the user indicates a desire to create a new visit for the note, a standalone visit of the type indicated will be created for the note.  ###### Historical Visits  When Progress Notes are being converted, historical visits are created (since no hospital location is frequently available for notes from either Mental Health V 6.0, or Generic Progress Notes V 2.5). When multiple notes are written for the same day for a given patient, each note will be associated with the same daily historical visit (so not every converted note requires the creation of a new visit record).  PCE uses Historical Visits to record encounters of uncertain dates or ones that occurred at non-VA facilities. They are used for various clinical purposes, including to calculate Clinical Reminders/Clinical Maintenance items for Health Summaries.  ##### Troubleshooting &amp; Helpful Hints for Document Definitions  1. If a particular person should be able to do something governed by a particular Business Rule, but can’t, check the following:  - Make sure he/she is in the referenced User Class. - Check the business rule for the proper status. - Check that the document to be acted on is the one referenced by the rule or is a descendant of the document referenced by the rule. If the rule involves a User Role, make sure the person actually plays that role for the document. - Check to see if the rule has been overridden. If the same rule (same action and same status) is defined for a lower-level document, the lower level rule OVERRIDES the rule at the higher level. For example, suppose you are checking the rule, An UNDICATATED PROGRESS NOTE can be ENTERED by a PROVIDER. Suppose you are wondering why CPRSPROVIDER,SEVEN can’t enter a Nurse Practitioner Note, which is a descendant of Progress Notes. If there is a rule, An UNDICTATED NURSE PRACTITIONER NOTE can be ENTERED by a NURSE PRACTITIONER, the rule you are checking has been overridden for Undictated Nurse Practitioner Notes. Any User Classes who can enter Nurse Practitioner Notes must have their own explicit Business Rule at the Nurse Practitioner Note level. The easiest way to check for overriding rules is to do a FileMan print by the same Action and the same Status.  1. If a particular person should NOT be able to do something, but CAN, check the following:     - That the person doesn’t have inappropriate menus.     - They are not members of inappropriate User Classes.     - The document involved is in the correct place in the document definition hierarchy.     - Check any business Rules for the given action, status, user role, and document or ancestors of the document.     - Check to see if they have somehow been given an inappropriate role in relation to the document. For example, the person might mistakenly have been made the author when he/she isn’t the author.     1. If you want to change document behavior, but are not sure how, try the following:         - Use the Edit Document Definitions, Create Document Definitions, or Sort Document Definitions option, and then select the action Edit/View.         - Check TIU document parameters, on the IRM Maintenance Menu.         - Check Personal Preferences.         - Check ASU Business Rules under User Class Management on the IRM Maintenance Menu.         1. *Document Definition Order* . If you can’t get Document Definitions to appear in the order you want, note where this occurs. You can control the order in some places and not in others, depending on whether it’s FileMan controlling the order or TIU.     **FileMan control:**         1. When you type a few letters and are presented with the list of entries starting with those letters.         2. When you enter a ? to get a list of orders.     TIU control:         - You are in the Document Definition Utility and the list part of the screen is in the wrong order.         - The components of a Title appear in the wrong order when you enter or print a document.         - When you look at documents across several patients or are viewing more than one type of document (e.g., Progress Notes and Discharge Summaries) at the same time.         - When you choose which documents to view from a three-column menu.             - In the situations under TIU control, you can define the order in which items appear. Go into Document Definitions Edit or Sort options and Edit the Items (Document Classes or Titles) of the parent (Class or Document Class). Edit the item sequence. If you want the items to appear in alphabetic order, delete all the sequences, and they will then appear in alphabetic order by Menu Text (shown on the screen when you scroll right).             - The order of Titles in your personal list is determined by the sequence entered in the Personal Preferences option.         5. When trying to activate a Document Class or Title, you get the following message: “Faulty Entry: No [Visit Linkage Method, Edit Template, Print Method, Validation Method].”         These fields are inherited from a parent or ancestor. Check to make sure your entry is a descendant of an entry which has those fields. For example, the Progress Notes Class has all of these fields and all descendants of Progress Notes inherit these field values automatically.         6. When trying to activate a Document Class or Title, you get a message, “Faulty Entry: No [Print Form Header, Print Form Number, Print Group].”         These fields are necessary only if the Parent of the entry allows Custom Form Headers. If the parent allows custom headers, the descendants must have values for these fields, either inherited or explicit values. Check to make sure your entry is a descendant of an entry which has those fields, or fill in your own explicit values if the inherited values are not appropriate.         7. If you are asked in TIU for the name of a Document Definition (for example at the Jump to Document Def prompt), you can enter the number (IFN) of the entry, its Abbreviation, its Print Name, or just the Name. You don’t have to precede the IFN with a single quote mark.  ##### Troubleshooting the TIU ACTIONS RESOURCE Device  If the TIU ACTIONS RESOURCE device is backed up with numerous tasks, this is how to clear the backlog:  TIU sends notifications to subscribers of the TIU DOCUMENT ACTION EVENT protocol alerting them when a document deletion/retraction or reassignment occurs. To ensure that the notifications are sent in the same order in which the actions occurred, the notifications are sent via TaskMan jobs that are queued to the TIU ACTIONS RESOURCE device with a sync flag of TIUDAN. This device should only have one resource slot, ensuring that notifications are sent sequentially.  If this device becomes backed up, it’s most likely due to a TaskMan job that errored and ended prematurely. To restart processing of tasks queued to this device, use the TaskMan option SYNC flag file control [XUTM SYNC] to start the next task with the TIUDAN sync flag.  #### ASU and User Class Information  ##### Relationship between User Class file and Person Class file  Although there are a number of superficial similarities between the User Class File (#8930) and Kernel’s Person Class File (#8932.1), the files are structurally dissimilar, with completely different applications which they are designed to serve. In fact, the roles of the two files are analogous to those of the LABORATORY TEST File (#60) and the WKLD CODE File (#64).  The *User Class File* provides for the definition of a hierarchy of User Classes, flexible enough to describe the organizational structure of the local facility.  To that end, it is designed to be both *general* and *extensible* , much in the same way that file 60 can be viewed as a “model” of the local laboratory’s “catalogue” of tests and panels.  The *Person Class File* , in contrast, is designed to accommodate the HCFA National Provider System Taxonomy of Professionals/Occupations, which is an emerging industry standard for identifying the Occupations, Specialties, and Subspecialties to which Health Care Providers belong.  This file is standardized across VHA, and cannot be extended to accommodate differences in local organizational structure. It is very useful, however, for inter-facility data transfer, where enterprise-wide consistency is the name of the game. The same role is fulfilled, in the case of laboratory tests, by file 64. This combination of locally extensible files which help to model the differences between facilities, mapped to national “nomenclature” files which help to impose a standard reference frame, has proven to be most useful on many occasions throughout **V** IST **A** .  ***Other Differences between User Class and Person Class***  User Class is *general* , allowing for identification of an array of non-Providers whose access to clinical applications must be accommodated and controlled (e.g., transcribers, file clerks, ward clerks, unit secretaries, hospital directors, etc.).  The HCFA Taxonomy (and therefore the Person Class file) currently offers a very restricted subset of the administrative or clerical occupations required by the applications which ASU is designed to serve.  User Class may be dynamically extended or revised to accommodate a wide variety of common organizational changes (e.g., product line reorganizations, site consolidations, etc.), with their attendant local variations.  The User Class file accommodates a true “object-class” hierarchy, which allows the definition of a set of locally controlled business rules, conferring privileges which may be defined for any level in the hierarchy, and “inherited” by members of all subordinate classes. For example, one such rule states that a User may view a completed Clinical Document, where User is the “root class” of the User Class Hierarchy, and Clinical Document is the root class of TIU’s Document Definition hierarchy.  #### Amount of Set-up for User Class &amp; Business Rules  ##### Initial Population of Basic User Classes  In the initial implementation of TIU and ASU, it is ***NOT*** necessary to populate all of the exported user classes, or to allocate *every* **V** IST **A** user membership in *any* of the exported classes. Any users who are not allocated to a specific class will be treated as members of the root class USER.  An option is provided to “seed” the PROVIDER class based on ownership of the PROVIDER Security Key.  NOTE: 	If your site has allocated the PROVIDER key to non-Providers in order to accommodate the requirements of the Ambulatory Care Data Capture package, we suggest that you review the holders of the key and de-allocate it from such users as necessary.  In the set-up section of the *TIU Implementation Guide* , we illustrate how to allocate members to the Medical Records Technician, Chief, MIS, and Transcriptionist classes. These are the only user classes whose membership must be allocated for basic implementation of TIU.  **Creation of Business Rules**  TIU and ASU are exported with a very general set of business rules, which should be sufficient for initial implementation. As stated earlier in this Guide, we recommend that you *keep the User Class file, TIU Document Definition Hierarchy, and Business Rule base as simple as possible* in your initial implementation.  Once you have grown acquainted with the basic operation of these two complex packages, you might then begin to explore the more advanced levels of control that are possible in accordance with your site’s HIM by-laws and concerns for the trade-off between access and confidentiality. Instructions for creating Business Rules are also provided earlier in this Guide.  ### Appendix A: TIU Package Security  TIU security is maintained through a security key, menu assignment, User Class assignment, Document Definition ownership, and VA FileMan protection.  #### Security Key  ##### TIU AUTOVERIFY  If your site requires verification of one or more TIU Documents, but you have one or more particularly adept transcriptionists for whom verification should NOT be required, you may allocate the TIU AUTOVERIFY key to them, and verification will be bypassed for their transcribed documents.  ##### TIU MISSING TEXT CLEAN  This key allows the holder to run the option MISSING TEXT CLEANUP. It should only be assigned to some that holds Chief, MIS or Chief, HIMS class in the AUTHORIZAITON/SUSCRITPTION package (USR).  #### User Class Assignment and Document Definition Ownership  See the Implementation and Management section in this manual about setting up User Classes and Document Definition. Also refer to the *Text Integration Utilities (TIU) Implementation Guide.*  #### Menu Assignment  TIU menus and options are not exported on a single big menu, but as smaller menus directed at categories of users. Sites may rearrange these as needed.  ##### Recommended Assignments  Option Name Menu Text Description Assign to: TIU MAIN MENU  TRANSCRIP-TION Text Integration Utilities (Transcription-ist) Main Text Integration Utilities menu for transcriptionists. Transcrip-tionists TIU MAIN MENU MRT Text Integration Utilities (MRT) Main Text Integration Utilities menu for Medical Records Technicians. Medical Records Technicians. TIU MAIN MENU MGR Text Integration Utilities (MIS Manager) Main Text Integration Utilities menu for MIS Managers. MIS Managers. TIU MAIN MENU CLINICIAN Progress Notes(s)/ Discharge Summary [TIU]  Main Text Integration Utilities menu for Clinicians.  Clinicians TIU MAIN MENU REMOTE Text Integration Utilities (Remote User) This option allows remote users (e.g., VBA RO personnel) to access only those documents which have been completed ), to facilitate processing of claims on a need-to-know basis. VBA RO personnel, etc. TIU PRINT PN USER MENU Progress Notes Print Options Menu for printing Progress Notes. ADPACs, managers TIUF DOCUMENT DEFINITION Document Definitions Document Definition        (Clinician) Document Definition       (Manager)  Clinicians  Clinical Coordinator IRM staff TIU CONVERSIONS MENU  TIU Conversions Menu Options used during installation and conversion IRM staff GMRP TIU TIU Conversion Clean-up Menu A menu of options for getting the Progress Notes package ready for conversion to TIU  ADPACs, IRM, or Clinical Coordinator  ### Appendix B: Creating an Object  To create an object, you must be familiar with M code at least well enough to read and copy it.  In this example, we create a very simple object, test it, make it more realistic, and then re-test it. After that, we’ll present further issues to consider.  #### Create a very simple Object.  We’ll create an object called PATIENT RELIGION which inserts the patient’s religion into the text of a document.  - Go into the option *Document Definition Manager,* select Create Objects, and then select the action Create:  Select TIU Maintenance Menu Option: **2** Document Definitions (Manager)  --- Manager Document Definition Menu ---  1      Edit Document Definitions  2      Sort Document Definitions  3      Create Document Definitions  4      Create Objects  5      Create TIU/Health Summary Objects  6      Create Post-Signature Alerts  Select Document Definitions (Manager) Option: **4** Create Objects  START WITH OBJECT: FIRST// **&lt;Enter&gt;** .........................................  **Objects** Mar 09, 1997 16:10:12       Page:    1 of    3  Objects  +											Status  1      ACTIVE MEDICATIONS                                             A  2      ALLERGIES/ADR                                                  A  3      BASELINE LIPIDS                                                A  4      BLOOD PRESSURE                                                 A  5      CURRENT ADMISSION                                              A  6      FASTING BLOOD GLUCOSE                                          A  7      HEMOGLOBIN A1C                                                 A  8      INR VALUE                                                      A  9      LABS ADMISSION ABNORMAL                                        A  10     LABS ADMISSION ALL                                             A  11     NOW                                                            A  12     PATIENT AGE                                                    A  13     PATIENT DATE OF BIRTH                                          A  14     PATIENT DATE OF DEATH                                          A  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-         &gt;&gt;&gt;  Find                      Detailed Display          Copy  Change View               Try                       Quit  Create                    Owner  Select Action: Next Screen// **&lt;Enter&gt;**  **Objects** Mar 09, 1997 16:13:44      Page:   2 of    3  Objects  +                                                             Status  15     PATIENT HEIGHT                                              A  16     PATIENT NAME                                                A  17     PATIENT RACE                                                A  18     PATIENT RELIGION                                            A  19     PATIENT SEX                                                 A  20     PATIENT SSN                                                 A  21     PATIENT WEIGHT                                              A  22     PROTHROMBIN TIME                                            A  23     PROTHROMBIN TIME COLLECTED                                  A  24     PULSE                                                       A  25     RESPIRATION                                                 A  26     SGOT                                                        A  27     TEMPERATURE                                                 A  28     TODAY'S DATE                                                A  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Find                      Detailed Display          Copy  Change View               Try                       Quit  Create                    Owner  Select Action: Next Screen// **??**  - Select the action Create.  **Objects** Mar 05, 1997 15:03:12             Page:    1 of    3  Objects  Status  1      ACTIVE MEDICATIONS                                              A  2      ALLERGIES/ADR                                                   A  3      BASELINE LIPIDS		                                      A  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Find                      Detailed Display          Copy  Change View               Try                       Quit  Create                    Owner  Select Action: Next Screen// **CR** Create  - Enter the PATIENT RELIGION.     - Delete the default owner CLINICAL COORDINATOR with an @ sign and enter your own name as the personal owner. This enables you to continue editing the object.Enter Document Definition Name to add as New Entry: **PATIENT RELIGION** CLASS OWNER: CLINICAL COORDINATOR  Replace @ PERSONAL OWNER: CPRSPROVIDER,EIGHT          MAM Entry added     - The new object appears at the top of the list.     - Scroll right (&gt;) to see that you are the owner.     - Select the action Detailed Display and select your new entry. NOTE: You can do this in one step by entering DET=(entry number):**Objects** Mar 05, 1997 15:03:12          Page:  2  of  3 Objects Status 18     PATIENT RELIGION                                               I 19     PATIENT SEX                                                    A PATIENT SSN                                                    A +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt; Find                      Detailed Display          Copy Change View               Try                       Quit Create                    OwnerSelect Action: Next Screen// **DET=18** Detailed Display     - The Detailed Display screen appears, showing your entry.     - Select the action Technical Fields.**Detailed Display** Mar 05, 1997 15:03:58              Page:   1 of    1 Object PATIENT RELIGION Basics Name:   PATIENT RELIGION Abbreviation: Print Name:   PATIENT RELIGION Type:   OBJECT IFN:   599 National Standard:   NO Status:   INACTIVE Owner:   CPRSPROVIDER,EIGHT Technical Fields Object Method: +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt; Find                        Detailed Display        Delete Basics                      Technical Fields        Find (Items: Seq Mnem MenuTxt) 	 (Upload)                Quit (Boilerplate Text)        	 TrySelect Action: Quit// **TE** TECHNICAL FIELDS     - Enter the object method:  S X=”TESTING123” OBJECT METHOD:  S X=”TESTING123”  #### Testing the Object  Now that we have a new object, let’s try it out.  - Quit all the way out of Create Objects. - Go into the option *Create Document Definitions* :  --- Manager Document Definition Menu ---  1      Edit Document Definitions  2      Sort Document Definitions  3      Create Document Definitions  4      Create Objects  5      Create TIU/Health Summary Objects  6      Create Post-Signature Alerts  Select Document Definitions (Manager) Option: **3** Create Document Definitions  - Find or create a  title you wish to embed the new object in.     - If it’s active, make a copy rather than inactivating the original, which takes it offline to users.     - Use an item under an active document class so that later you can change its status to “Test.”     - Use a Title under Progress Notes so that it inherits from Progress Notes.     - Make its status Inactive so you can edit it.     - Check it using the action Try to make sure it works properly before continuing this process (do a Detailed Display and select TRY).         - We’ll use the Title DEMOGRAPHIC NOTE, under the Document Class DEMOGRAPHIC NOTE, under Progress Notes.             - When you have your title, select the action Boilerplate Text and your title:**Create Document Definitions** Mar 05, 1997 15:05:23          Page: 1 of  1 \_         BASICS         +      Name                                                           Type \_         2       PROGRESS NOTES                          		            CL         3         DEMOGRAPHIC NOTE					            DC         **4            DEMOGRAPHIC NOTE					            TL**         +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;         (Class/DocumentClass)   Next Level           Detailed Display         Title                   Restart              Status...         (Component)             Boilerplate Text     DeleteSelect Action: Title// **BO=4**             - The Boilerplate Text screen is displayed. At present, there is no text.             - Select Boilerplate Text again, this time to edit it (rather than display it):**Boilerplate Text** Mar 05, 1997 15:05:37           Page:    1 of    1 \_         Title DEMOGRAPHIC NOTE \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_         +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;         Find                      Detailed Display          Copy         Change View               Try                       Quit         Status                    FindSelect Action: Quit// **B** Boilerplate Text             - Your preferred editor appears. Type in the following:         ======[WRAP]==[INSERT]=&lt;DEMOGRAPHIC NOTE&gt;===[&lt;PF1&gt;H=HELP]=========         Patient’s religious preference: &#124;PATIENT RELIGION&#124;. Patient’s home address: ……         =====T=====T=====T=====T=====T=====T=====T=====T=====T=====T         NOTE: 	Be sure to spell the object name correctly, use upper case, and enclose it in vertical bars:             - Exit out of the editor. The screen displays our new boilerplate text.             - Select the action TRY:         #########   Saving text ...  **Boilerplate Text** Mar 05, 1997 15:05:37           Page:    1 of    1  Title DEMOGRAPHIC NOTE \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Patient’s religious preference: &#124;PATIENT RELIGION&#124;. Patient’s home address: …  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Boilerplate Text          Try                       Quit  Status                    Find  Select Action: Quit// **Try**  Entry Checks out OK for rudimentary completeness  - The entry checks out OK. - Select a TEST patient. (Since it’s a title, you are given the opportunity to try it on a patient.) - Accept the defaults for location, etc. - You are presented with the boilerplate text, just as if you had entered a document Demographic Note on the patient:  Object &#124;PATIENT RELIGION&#124; is not active.  Press RETURN to continue or ‘^’ or ‘^^’ to exit: **&lt;Enter&gt;**  Checking Title on a document.  You will not be permitted to sign the document, and the document will be deleted at the end of the check.  Be sure to select a TEST PATIENT since the document will show up on Unsigned lists while you are editing it.  Select PATIENT NAME: **CPRSPATIENT,THREE** 09-12-44     000000003     YES  SC VETERAN  (2 notes)  C: 02/24/97 08:44  (1 note )  W: 02/21/97 09:19  A: Known allergies  Creating new progress note...  Patient Location:  UNKNOWN  Date/time of Visit:  03/05/97 15:07  Date/time of Note:  NOW  Author of Note:  CPRSPROVIDER,NINE  ...OK? YES// **&lt;Enter&gt;**  Calling text editor, please wait…  ======[WRAP]==[INSERT]=&lt; &gt;===[&lt;PF1&gt;H=HELP]===================  Patient’s religious preference: TESTING123.  Patient’s home address: …  ======T=====T=====T=====T=====T=====T=======T=======T=======T========T  - The trial document looks all right. The data we set X to is inserted in the text.  NOTE: 	If there are errors in the object other than the status, we may receive any of the following messages:  Object &#124;PATIENT RELIGION&#124; cannot be found. User uppercase and use object’s exact name, print name, or abbreviation. Objects’ name/print name/abbreviation may have changed since this was embedded.  Object &#124;PATIENT RELIGION&#124; is not active.  Object &#124;PATIENT RELIGION&#124; lacks an object method.  Object &#124;PATIENT RELIGION&#124; is ambiguous. Can’t tell which object is intended.  Object split between lines, rest of line not checked.  The split line message refers to lines such as:  This is a test of Object &#124;PATIENT RELIGION&#124;. Patient’s Home address: . . .  But none of these messages apply to us.  - Exit the editor.  The document is deleted:  Saving text ...  &lt;NOTHING ENTERED. DEMOGRAPHIC NOTE DELETED&gt;  #### Making the Object More Realistic  Now that we have the basic idea, we’ll write an object method that actually gets the patient’s religion. We’ll imitate the PATIENT AGE object, which has the object method:  S X=$$AGE^TIULO(DFN)  Note that, again, the object method sets the variable X. This time the object depends on the patient. The variable DFN is the internal entry number in the Patient File ^DPT. Its value is known to the system at the time a document is entered on a particular patient.  This object method calls the TIULO routine, exported with the TIU package, and sets X equal to the value of the function $$AGE^TIULO.  That code looks like this:  TIULO	; SLC/JER - Embedded Objects ;9/28/95 16 :26  ;;1.0;TEXT INTEGRATION UTILITIES;;Mar 05, 1997  AGE(DFN)	; Patient AGE  I '$D(VADM(4)) D DEM^TIULO(DFN,.VADM)  Q $S(VADM(4)]"":VADM(4),1:"AGE UNKNOWN")  ;  DEM(DFN,VADM)	; Calls DEM^VADPT  D DEM^VADPT  Q  If the VADM array hasn’t been defined for subscript 4, the age subscript, the code calls module DEM, passing array VADM by reference. DEM calls the VADPT patient demographics utility, and passes patient demographics back. We can copy this and only need to understand that it puts demographic information for patient DFN in the VADM array as described in the VADPT utility.  Note that AGE is a function and quits with the value VADM(4) if VADM(4) has a value. Otherwise, it quits with the value “AGE UNKNOWN.”  We’ll write similar code for religion.  - Quit out of the Manager Menu and get into programmer mode. - Write a similar function for religion. Looking up the VADPT utility, we find that patient religion is returned in VADM(9), so we have:  MYROUTIN	; HERE/ME - Embedded Objects ; 9/28/96 16:26  ;  RELIG (DFN)	; Patient RELIGION  I '$D(VADM(9)) D DEM^TIULO(DFN,.VADM)  Q $S(VADM(9)]"":VADM(9),1:"Religious Preference UNKNOWN")  - To test the code, set DFN to a known patient. (To find the DFN of a patient, do a Fileman Inquiry to the PATIENT file, enter the name of a patient, and enter R at the Include COMPUTED fields prompt to get the record number. Set DFN to this record number.). - Set X= $$RELIG^MYROUTIN(DFN). - WRITE !,X:  W !,X  OTHER  This patient’s religion is listed as “OTHER.”  - When the code has been thoroughly tested on several different patients, including some who have no religion in the patient file, go back to the option Create Objects. - Select the action Detailed Display for object PATIENT RELIGION, - Select the action Technical Fields - Edit the object method to:  S X=$$RELIG^MYROUTIN(DFN)  **Detailed Display** Mar 05, 1997 15:03:58           Page:    1 of   1  Object PATIENT RELIGION        \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Basics  Name:   PATIENT RELIGION  Abbreviation:  Print Name:   PATIENT RELIGION  Type:   OBJECT  IFN:   599  National  Standard:   NO  Status:   INACTIVE  Owner:   CPRSPROVIDER,EIGHT  Object Method: S X=$$RELIG^MYROUTIN(DFN)  Technical  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Basics                    Technical Fields          Find  Items: Seq Mnem MenuTxt   Upload                    Quit  Boilerplate Text          Try  - While we’re here, let’s go in, put in an abbreviation for the object, and namespace the print name. To do so, we select the action Basics:  Select Action: Quit// **BA** BASICS  NAME: Since objects are embedded by name, abbreviation, or print name, NOT by file number, your edit of name, abbreviation, or print name may affect which titles have the object embedded in them. You may want to note the list of titles NOW before it changes.  Press RETURN to continue or ‘^’ or ‘^^’ to exit: **&lt;Enter&gt;**  Since our object is new and we know it’s only in DEMOGRAPHIC NOTE, we’ll disregard the warning and enter a new Name and an abbreviation.  We’ll keep the old print name and up-arrow out:  NAME: DEM PATIENT RELIGION// **&lt;Enter&gt;**  ABBREVIATION: **RELI**  PRINT NAME: PATIENT RELIGION// **^**  **Detailed Display** Mar 05, 1997 15:03:58       Page:  1 of  1  Object PATIENT RELIGION                       \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Basics  Name:   DEM PATIENT RELIGION  Abbreviation:   RELI  Print Name:   PATIENT RELIGION  Type:   OBJECT  IFN:   599  National  Standard:   NO  Status:   INACTIVE  Owner:   CPRSPROVIDER,NINE  Technical Fields  Object Method: S X=$$RELI^MYROUTIN (DFN)  Object is embedded in Title(s)       Status   Owner   IFN  DEMOGRAPHIC                            I        ME    567  ? Help       +, - Next, Previous Screen     	PS/PL  Basics                Try           Delete  Technical Fields      Find          Quit  Select Action: Quit// **&lt;Enter&gt;**  #### Testing the More Realistic Object  When the Object Method, Name, Abbreviation, and Print Name are all as we wish, we again test the Object. Before trying our title DEMOGRAPHICS as we did before, we will try the object itself.  - While still in the above Object Detailed Display screen, select the action TRY. We get the message:  Select Action: Quit// **T**  Entry checks out OK for rudimentary completeness  This is an important step. If there were problems, we might have gotten any or all of the following messages:  Faulty Entry: No Object Method  Faulty Entry: Object Name finds multiple/wrong object(s)  Faulty Entry: Object Abbreviation finds multiple/wrong object(s)  Faulty Entry: Object Print Name finds multiple/wrong object(s)  The first message appears if the object has no Object Method.  Unfortunately, this doesn’t tell us whether the Object Method functions correctly. It only tells us the entry has or doesn’t have an Object Method. We know it functions correctly because we tested the code.  We get one or more of the other messages if our object has a duplicate Name, Abbreviation, or Print Name with some other object. This would cause our object not to be found when that Name, Abbreviation, or Print Name is used in boilerplate text. We also get such a message if, for example, our object Abbreviation is the same as the Name of another object. In that case we would get the message:  Faulty entry: Object Abbreviation finds multiple/wrong object(s).  If this happens, our object might find and insert the WRONG object into boilerplate text. We must change the abbreviation so it doesn’t match the name, abbreviation, or print name for another object.  Once we have thoroughly tested the Object Method code, put in Name, Abbreviation, and Print Name as desired, and gotten a clean TRY when we tried the OBJECT, we can now try our title containing the object.  - Quit out of Create Objects - Go into the option Create Document Definitions - Use the action Next Level to drill down to our title - Select the action Boilerplate Text - Select the title  **Create Document Definitions** Mar 05, 1997 15:05:23          Page:  1 of  1  BASICS  +      Name			                                            Type  2      PROGRESS NOTES                          		           CL  3       DEMOGRAPHIC NOTE					                  DC  4       DEMOGRAPHIC NOTE					                  TL  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  (Class/DocumentClass)     	Next Level          Detailed Display  Title                    	Restart             Status...  (Component)             	Boilerplate Text    Delete  Select Action: Title// **BO=4**  - The Boilerplate Text that we entered previously is displayed.  We changed the name of the object, but we don’t need to make that update here since the Print Name is PATIENT RELIGION, and the Print Name will do just as well as the name.  - Select the action Try.  **Boilerplate Text** Mar 05, 1997 15:05:37       Page:    1 of  Title DEMOGRAPHIC NOTE  Patient’s religious preference: &#124;PATIENT RELIGION&#124;. Patient’s home address:…  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Boilerplate Text          		Try                       Quit  Status                   		Find  Select Action: Quit// **Try**  - Enter a test patient - Accept the defaults - The following text appears:  Object &#124;PATIENT RELIGION&#124; is not active.  .  .  Calling text editor, please wait…  ================[WRAP]==[INSERT]=&lt; &gt;===[&lt;PF1&gt;H=HELP]===================  Patient’s religious preference: UNITARIAN; UNIVERSALIST.  Patient’s home ad  ======T======T======T======T======T======T=====T======T======T=======T  - This allows you to check out the formatting of the boilerplate text when the object is being used. - In this case the line continues beyond 80 characterswe haven’t left enough room in the line for the object. - If there isn’t enough room for the object data, or it doesn’t print out in the right format, we change the Object Method and/or the Boilerplate text until it looks right. - Go into Boilerplate text and move the next sentence to the next line:  ==============[WRAP]==[INSERT]=&lt; &gt;===[&lt;PF1&gt;H=HELP]===================  Patient’s religious preference &#124;PATIENT RELIGION&#124;.  Patient’s home address:…  =======T=======T=======T=======T=====T=====T=====T=====T=====T=====T=====  - Exit the editor. - In the Boilerplate screen, use the TRY action again:  ======[WRAP]==[INSERT]=&lt; &gt;===[&lt;PF1&gt;H=HELP]===================  Patient’s religious preference: UNITARIAN; UNIVERSALIST.  Patient’s home address: …  =====T=====T=====T=====T=====T=====T=====T=====T=====T=====T  This time the formatting looks fine.  We have tested the Object Method code, TRIED the object, and TRIED a title with the object in it. Everything looks good, so we proceed to activate the object.  #### Activating the object  - Quit out of the Detailed Display screen. - In the Objects screen, select the Status action. - Select A for Active status:  **Detailed Display** Mar 05, 1997 15:03:58          	Page:    1 of    1  Object PATIENT RELIGION                             \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Basics  Name:   DEM PATIENT RELIGION  Abbreviation:   RELI  Print Name:   PATIENT RELIGION  Type:   OBJECT  IFN:   599  National  Standard:   NO  Status:   INACTIVE  Owner:   CPRSPROVIDER,NINE  Technical Fields  Object Method: S X=$$RELI^MYROUTIN (DFN)  +         ?Help   &gt;ScrollRight   PS/PL PrintScrn/List   +/-             &gt;&gt;&gt;  Basics                   Try              Delete  Technical Fields         Find             Quit  Select Action: Quit// **BA** Basics  NAME: DEM PATIENT RELIGION// **&lt;Enter&gt;**  ABBREVIATION: RELI// **&lt;Enter&gt;**  PRINT NAME: PATIENT RELIGION// **&lt;Enter&gt;**  PERSONAL OWNER: ME// **&lt;Enter&gt;**  STATUS: (a/I): INACTIVE// **A** ACTIVE  Activating an object communicates to users that it is ready for embedding in boilerplate text. It also causes the object to execute its object method code rather than to write an inactive message when documents are entered on it through the regular options (as opposed to the action Try). If the object TRY action had not been clean, we would not have been able to activate the object.  The Active object is now ready for entering documents. One last test, and we’ll be done.  To enter documents (rather than just TRY them), the title also must have a status of Active or Test.  - Quit out of the option *Create Objects* and - Go into the option Create Document Definitions. - Edit the status of the test title to Test. - Check to make sure that you own it. - Quit out of the Document Definition menu - Go into the Clinician menu. - Select *Entry of Progress Note* from the Clinician’s Progress Notes Menu  --- Clinician's Progress Notes Menu ---  1      Entry of Progress Note  2      Review Progress Notes by Patient  2b     Review Progress Notes  3      All MY UNSIGNED Progress Notes  4      Show Progress Notes Across Patients  5      Progress Notes Print Options ...  6      List Notes By Title  7      Search by Patient AND Title  8      Personal Preferences ...  Select Progress Notes User Menu Option: **1** Entry of Progress Note  #### Entering a Progress Note using the Object  - Select a TEST PATIENT - Select the title:  Select PATIENT NAME: **CPRSPATIENT** ,THREE       09-12-44     000000003    YES  SC VETERAN  (2 notes)  C: 02/24/97 08:44  (1 note )  W: 02/21/97 09:19  A: Known allergies  Available note(s):  11/07/96 thru 03/05/97  (23)  Do you wish to review any of these notes? NO// **&lt;Enter&gt;**  Personal PROGRESS NOTES Title List for ME  1    CRISIS NOTE  2    ADVANCE DIRECTIVE  3    Other Title  TITLE:  (1-3): 1// **3**  TITLE: CRISIS NOTE// **DEMOGRAPHICS NOTE** TITLE  Creating new progress note...  Patient Location:  2B  Date/time of Visit:  04/18/96 10:00  Date/time of Note:  NOW  Author of Note:  CPRSPROVIDER,NINE  ...OK? YES// **&lt;Enter&gt;**  Calling text editor, please wait...  =========[ WRAP ][ INSERT ]=&lt; Patient: CPRSPATIENT,THREE &gt;[ &lt;PF1&gt;H=Help]=======  Patient’s religious preference: UNITARIAN; UNIVERSALIST.  Patient’s home address: …  T=======T=======T=======T=======T=======T=======T=======T=======T=======T  - Exit your editor:  Saving text ...  No changes made...  - Don’t sign it. You’ll want to delete it later since it’s a test note:  Enter your Current Signature Code: **&lt;Enter&gt;**  NOT SIGNED.  Press RETURN to continue... **&lt;Enter&gt;**  Print this note? No// **&lt;Enter&gt;** NO  You may enter another Progress Note. Press RETURN to exit.  Select PATIENT NAME: &lt;Enter&gt;  ##### Troubleshooting:  If you have problems with this note:  - Make sure its status is Active or Test. - If its status is Test, make sure you own it. - Make sure the embedded object PATIENT RELIGION has an active status.  ##### Using the Object  When the note works properly, the object is finished and available for any user with a Document Definition menu to embed it in boilerplate text. Unless you assign ownership to someone else, you are the site-wide caretaker for this object. Any questions or requests should be addressed to you.  ##### Further Considerations  ###### Using the option Sort Document Definitions to create Objects  - Once you are comfortable creating objects, it is actually easier to use the option *Sort Document Definitions* than the option *Create Objects* . To use the Sort option, select ALL, and select a narrow alphabetic range which includes both the object name and the name of a test title. - Another possibility is to enter yourself as the Personal Owner. This assumes you are the personal owner of both the object and test title. *Sort Document Definitions* permits the object to be edited and tested (except for the code itself) without switching options.  ###### Activating/Inactivating/Editing Objects  - Objects must be inactive before they can be edited. Before inactivating an object that has already been used in boilerplate text, you should inactivate all Titles which use it. This takes those titles offline for entering documents. If a title containing an inactive object is not offline and someone enters a document on it, the object will not function and the user will see an “Object Inactive”  error message where the object data should appear. - Objects can be tested using the Try action when they are inactive, but must be activated before they will function for the option *Entry of Progress Note* . So, when you have finished editing an object, be sure to reactivate it. - Objects should not be activated until they have been thoroughly tested both by TRYing the object and by TRYing a test title with the object embedded in its boilerplate text.  ###### Ownership of Objects  - When creating a new object, make yourself an owner, at least until you have finished testing it. Only the owner can edit an object, even with the Manager menu. - Persons with the Manager menu are permitted to edit the owner of objects they don’t own. This allows reassignment of object owner in those rare cases when reassignment is necessary. It should be done only by high-level managers. In general, users are expected to respect object ownership and edit only objects they own. If an object needs changing, contact its owner. When you own an object, you are caretaker of it for the entire site since it is available across the site for use in boilerplate text. Consult with all users before changing it.  ###### Naming Objects  - Although TIU doesn’t enforce any rules regarding which name of the object to embed in boilerplate text, sites may want to maintain the convention of embedding print name or abbreviation only, leaving the .01 name to be a longer, technical, namespaced name. Then Print Name must be long enough to be unique, but otherwise as short as possible for typing convenience.  Abbreviation is 2 to 4 letters. - Objects must always have uppercase names, abbreviations, and print names. When embedding objects in boilerplate text, users may embed any of these three (name, abbreviation, print name) in boilerplate text, enclosed by an “&#124;” on both sides.  Objects must always be embedded in uppercase. - As for namespacing, sites will want to share ideas among themselves as to what works best. Some possibilities are by service or product, like the Document Definition Hierarchy, and/or by the site where the object originated. Sites can post objects to share on SHOP,ALL  ###### Creating more complex objects  For ideas on creating more complex, longer objects, look at the object methods of some other exported objects. Look at the associated routines.  Copy an exported object, put a break in the copy’s object method, embed the copy in a title and try the title.  #### Action Descriptions  Actions are not selectable when they are enclosed in parentheses.  ##### FIND  Finds text in a list of entries/information displayed. The program  searches all pages of list/information (except for unexpanded entries in the Edit Document Definitions Option). Can be a quick way to get to the  right page.  Enter F  ##### CHANGE VIEW  Changes the view to a different list of Document Definitions.  ##### CREATE  This action can be used to create either Objects or non-object Document Definitions in TIU Document Definition file 8925.1. After it is created, a non-object entry must be explicitly added as an Item to a parent in the hierarchy before it can be used. (The Create Document Definitions Option does this automatically.)  File 8925.1 cannot have two entries of the same type with the same name.  ##### DETAILED DISPLAY  Detailed Display displays the selected entry and permits edit if appropriate. Edit is limited if the entry is National. Shared Components can be VIEWED via the Edit Document Definitions Option but can be EDITED   only via the Sort Option.  The DETAILED DISPLAY action lets you edit all aspects of an entry,  including Items. The Items action, in contrast, looks at the entry ONLY as an Item under its parent and permits edit of Item characteristics ONLY. Managers (anyone assigned the Manager menu) need not own the entry in order to edit it. You can edit Basics, Items, Boilerplate Text, Technical Fields and Upload Fields.  ##### TRY  TRY examines the selected entry for basic problems.  For titles and components with boilerplate text, this includes checking any Embedded objects to make sure the object is embedded correctly. If the entry is a title and checks out OK (or if its only problem is an inactive Object), you can test the boilerplate text by choosing a patient and entering a document using the entry. TRY doesn’t require any particular status for the Title, since documents entered during the trial function even if inactive, in order to permit testing of objects. (Ordinarily, object data are not retrieved unless the object is active, so be sure to activate the object when it’s ready for use.) Since the trial document shows up on Unsigned lists during the time it’s being edited, we recommend that you select *test patients only.*  If TRY is selected from the Boilerplate Text Screen, TRY shows which objects are badly embedded and why. Checks include whether the object as written exists in the file, whether it is active, whether it is split between lines, and whether the object as written is ambiguous as to which object is intended. If the entry is OK, you can enter a trial document.  For objects, TRY checks the object Name, Abbreviation and Print Name to make sure they are not ambiguous. That is, it makes sure the utility can decide which object to invoke when given the Name, Abbreviation, or Print Name and that it does not get the wrong object. TRY checks that the object has an Object Method, but does NOT check that the Object Method functions correctly.  ##### OWNER  You can select multiple entries and edit Owner, Personal and/or Class. To change from Personal to Class Owner or vice versa, you must delete the unwanted entry before you are prompted for the other.  ##### COPY  Copy can be done from the *Edit Document Definitions* option or from the Sort option, but not from the *Create Document Definitions* option. Titles,  Components, or Objects may be copied.  Copy can be used to "jump start" new entries by copying an old entry and then editing it.  Copy *could* be used to change the behavior of an entry (i.e. change the behavior of the copy and inactivate the original), but most behavior can be edited even when the entry is in use by documents. Edit is better than copy/inactivate since it does not clutter up the hierarchy with inactive entries.  Copy can be used to "move" entries once they are in use by documents. (This is not a true "move", but is the only possibility once an entry has been used by documents. If the entry is not yet in use by documents, it is better to delete it as an item from the old parent, and add it to the new parent, a true move).  The Copy action prompts for an entry to copy and a Name to copy into. This name must be different from the name of the entry being copied. The action then creates a new entry with the chosen name and copies the fields in the Document Definition File 8925.1 into the new entry. The copier is made the personal owner of the copy.  If the copying is being done through the *Edit Document Definitions* option, the copy is then added as an item to the parent. If the copying is done through the *Sort Document Definitions* option, the copy is NOT added as an item to the parent. Since items must not be added to Active or Test Titles, components of Active or Test Titles can only be copied through the Sort option. Objects are copied from the Sort option or the Create Objects option.  Several fields are NOT copied as is. If the original is a National Standard, the entry may be copied, but the copy is not National Standard. If the original is Shared, it may be copied but the copy is not Shared. The other exceptional field is the Items field. If the entry has items, the action prompts for item names to copy into, creates NEW entries for the items, and adds the NEW items to the copy.  Exception to the Items field Exception: if a nonshared entry has a Shared item, the action does NOT copy the Shared item but merely adds the Shared item to the copy. If the entry being copied is itself a Shared component, the copy is not shared, and NEW items are added to the copy rather than reusing shared items.  If the copying is being done through the Edit Document Definitions option, the user is asked which parent to add the copy to, and the copy is added as an item to this parent.  If the copy is a Title and the user has chosen a new parent rather than the same parent, the user is asked whether to activate the copy and inactivate the original.  If the copying is done through the Sort Document Definitions option, the copy action does NOT add the copy to any parent.  Such orphan copies can be added to any parent using action Items for the parent.  Objects are copied from the Sort Option or the Create Objects Option.  ##### QUIT  Allows user to quit the current menu level.  #### Creating Additional Medications Objects  **Patch 365 and 372** (TIU*1.0*365 UPDATE MEDICATION ROUTINE/OBJECT w/TIU*1.0*372 FOLLOW-UP) deprecated the existing TIULMED* routine(s) and provided support to display the new “Indication” data with the new TIUMOBJ* routine(s).  Existing medication objects are compatible with the updated routines and do not need to be edited or updated.  **Patch 73** (TIU*1*73 - NEW MEDICATION OBJECT OPTIONS) provided expanded capabilities for customizing TIU medication objects.  **Patch 290** (TIU*1*290 - CPRS V31.B - NOTE TITLES, COPY/PASTE AND BUG FIXES) updated the rules for national medication Patient Data Objects.  The following variables and values are now supported:  Parameter Description Values DFN Internal entry number (IEN) of the desired patient. Valid DFN TARGET Return location of the medication data. Default is local variable OUTPUT. Global locations must be ^TMP(with at least 1 subscript. Applications are responsible for cleaning up returned data. OUTPUT [default] Local variable name ^TMP( A Active and/or recently expired medications. 0 Active & recently expired     [default] 1 Active only 2 Recently expired only D Display standard or detailed medication information. 0 Standard output [default] 1 Detailed output M Medication types: Inpatient, Outpatient & Non-VA, and Clinic medications.  Non-VA medications will always be displayed with outpatient medications. The new parameter value supports the display of non-VA medications only.* 0 Inpatient or outpatient [default     -- based on patient status] 1 Inpatient, outpatient, & clinic 2 Inpatient only 3 Outpatient only 4 Clinic only 5 Clinic & inpatient only 6 Clinic & outpatient only 7 Non-VA only* O Display medications in one list or separated by status: Active, Pending, and Inactive.  0 Separate based on status     [default] 1 Combines into one list per     type SC Sort medications by drug class. 0 Sort alphabetically [default] 1 Sort by class, alphabetically 2 Sort by class and display drug      class in header SU Include or exclude supplies. 0 Exclude supplies 1 Include supplies [default] MR Med/Rec TIUDATE Fix 0 Exclude TIUDATE 1 Include TIUDATE [default]  #### Creating an Object Based on Health Summary  Starting with patch TIU*1*135, you can create a TIU object that will display a Health Summary Type. This patch can work in conjuction with GMTS*2.7*58. With Health Summary Patch 58, you can use the Health Summary Objects Menu to create custom Health Summary Objects for use as TIU Objects. Alternately you can use default values to create a TIU Health Summary Object directly from TIU.  Health Summary patch 58 creates a new file, the Health Summary Object file [#142.5], which contains information about how the Health Summery type is displayed as an object in TIU. This file contains a pointer to the Health Summary Type file [#142] associating each named Health Summary Object (HS Object) with an existing Health Summary Type (HS Type). To make the HS Object useable as a TIU object, the TIU Document Definition file [#8925.1] must contain a pointer to the HS Objects file. The existence of this pointer in the technical field of this file is how VistA distinguishes TIU HS Objects from other entries in the TIU Document Definition file. This pointer is set by the Create TIU/Health Summary Objects [TIUHS LIST MANAGER] command of the Document Definitions (Manager) menu.  The following image  illustrates the relationship of records in files to the existing Health Summary Type file:  <!-- image -->  Note:	You may only change objects that you originally created. Each file contains information about who created each object or type. If you try to change an object or type that you do not own, the system will display an error message.  ##### Example  In the following example we use the Create TIU/Health Summary Objects option of the Document Definitions (Manager) menu [TIUF DOCUMENT DEFINITION MGR] to create a new TIU Object when a Health Summary Object already exists:  Select Document Definitions (Manager) Option: **?**  1      Edit Document Definitions  2      Sort Document Definitions  3      Create Document Definitions  4      Create Objects  5      Create TIU/Health Summary Objects  6      Create Post-Signature Alerts  Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.  Select Document Definitions (Manager) Option: **5** Create TIU/Health Summary Objects  TIU Health Summary Object     Dec 24, 2003@11:10:26          Page:    1 of    2 .  TIU Object Name                   Health Summary Type                      .  1    AJB TEST OBJECT                   ANEHEIM  2    A TEST 9                          ZZ HEALTH SUMMARY  3    A TEST DATE/HEAD                  ZZ HEALTH SUMMARY  4    A TEST OBJ                        VISITS  5    A TEST OBJECT                     ZZ HEALTH SUMMARY  6    A TEST4                           XRAY  7    BDV EDUCATION                     ZZ HEALTH SUMMARY  8    BDV LABS                          VISITS  9    CLINICAL MAINTENANCE              CLINICAL MAINTENANCE  10   HS TEST IMPORT                    XRAY  11   LAB SEL 1                         Selected Labs (Diabetes)  12   MY RESP                           DEM  13   PODIATRY                          AC CLINICAL SUMMARY  14   PODIATRY OBJECT                   AC CLINICAL SUMMARY  +         Enter ?? for more actions  Create New TIU Object                   Find  Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object  Quit  Select Action: Next Screen// **CR** Create New TIU Object  --- Create TIU/Health Summary Object ---  Enter a New TIU OBJECT NAME: **KR MED BRIEF**  Object Name: KR MED BRIEF  Is this correct? YES// **&lt;Enter&gt;** YES  Use a pre-existing set of Health Summary Object? NO// **YES**  Enter the name of the Health Summary Object: KR MED BRIEF  Create a TIU Object named: KR MED BRIEF  Ok? YES// &lt;Enter&gt;  TIU Object created successfully.  Enter RETURN to continue... **&lt;Enter&gt;**  TIU Health Summary Object     Jan 03, 2003@11:20:10          Page:    1 of    2 .  TIU Object Name                   Health Summary Type                      .  1    AJB TEST OBJECT                   ANEHEIM  2    A TEST 9                          ZZ HEALTH SUMMARY  3    A TEST DATE/HEAD                  ZZ HEALTH SUMMARY  4    A TEST OBJ                        VISITS  5    A TEST OBJECT                     ZZ HEALTH SUMMARY  6    A TEST4                           XRAY  7    BDV EDUCATION                     ZZ HEALTH SUMMARY  8    BDV LABS                          VISITS  9    CLINICAL MAINTENANCE              CLINICAL MAINTENANCE  10   HS TEST IMPORT                    XRAY  **11   KR MED BRIEF                      Medicine (Brief)**  12   LAB SEL 1                         Selected Labs (Diabetes)  13   MY RESP                           DEM  14   PODIATRY                          AC CLINICAL SUMMARY  +         Enter ?? for more actions  Create New TIU Object                   Find  Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object  Quit  Select Action: Next Screen//  ##### Second Example:  In the following example we use the Create TIU/Health Summary Objects option of the Document Definitions (Manager) menu [TIUF DOCUMENT DEFINITION MGR]  to create a new TIU Object when a Health Summary Object does not exist:  TIU/Health Summary Objects    Mar 27, 2003@08:20:33          Page:    1 of    2  TIU Object Name                   Health Summary Type                    .  1    AJB TEST OBJECT                   ANEHEIM  2    A TEST 9                          ZZ HEALTH SUMMARY  3    A TEST DATE/HEAD                  ZZ HEALTH SUMMARY  4    A TEST OBJ                        VISITS  5    A TEST OBJECT                     ZZ HEALTH SUMMARY  6    A TEST4                           XRAY  7    BDV EDUCATION                     ZZ HEALTH SUMMARY  8    BDV LABS                          VISITS  9    CLINICAL MAINTENANCE              CLINICAL MAINTENANCE  10   HS TEST IMPORT                    XRAY  11   KR MED BRIEF                      Medicine (Brief)  12   LAB SEL 1                         Selected Labs (Diabetes)  13   MY RESP                           DEM  14   PODIATRY                          AC CLINICAL SUMMARY  +         Enter ?? for more actions  Create New TIU Object                   Find  Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object  Quit  Select Action: Next Screen// **CR** Create New TIU Object  --- Create TIU/Health Summary Object ---  Enter a New TIU OBJECT NAME: **VISITS**  Object Name: VISITS  This is where the two examples start to differ. In this case, we take the default of NO.  <!-- image -->  Use a pre-existing set of Health Summary Object? NO// **&lt;Enter&gt;**  Checking VISITS (TIU) with Health Summary...  Creating Health Summary Object 'VISITS (TIU)'  TIU adds (TIU) to the name to distinguish objects created in TIU. It also adds (CONVERTED) to objects created by test versions 1 through 6.  <!-- image -->  Select Health Summary Type: **?**  Answer with Health Summary Type name, title, owner or hospital  location using the summary.  Your response must be at least 2  characters and no more than 30 characters and must not contain  an embedded uparrow  Select Health Summary Type: VISITS  2 Health Summary Types found  1.  Visits  2.  Future Visits  Select 1-2: **2**  Do you want to overwrite the TIME LIMITS in the Health  Summary Type 'FUTURE VISITS'?  N// **&lt;Enter&gt;**  Print standard Health Summary Header with the Object?  N// **&lt;Enter&gt;**  Partial Header:  Print Report Date?  N// **&lt;Enter&gt;**  Print Confidentiality Banner?  N// **&lt;Enter&gt;**  Print Report Header?  N// **&lt;Enter&gt;**  Print the standard Component Header?  Y// **&lt;Enter&gt;**  Use report time/occurence limits?  N// **&lt;Enter&gt;**  Underline Component Header?  N// O  Add a Blank Line after the Component Header?  N// **&lt;Enter&gt;**  Print the date a patient was deceased?  N// **&lt;Enter&gt;**  Print a LABEL before the Health Summary Object?  N// **&lt;Enter&gt;**  Suppress Components without Data?  N// **&lt;Enter&gt;**  OBJECT DESCRIPTION:  1&gt;Current visits.  2&gt;  EDIT Option:  Create a TIU Object named: VISITS  Ok? YES// **&lt;Enter&gt;**  TIU Object created successfully.  Enter RETURN to continue...  TIU/Health Summary Objects    Mar 27, 2003@08:20:33          Page:    1 of    2.  TIU Object Name                   Health Summary Type                     .  1    AC CLINICAL SUMMARY               CLINICAL MAINTENANCE  2    AJB TEST OBJECT                   VISITS  3    TEST 9                            XRAY  4    LAB TEST DATE/HEAD                BDV LABS  5    TEST OBJ                          VISITS  6    TEST OBJECT                       XRAY  7    TEST4                             XRAY  8    BDV EDUCATION                     HEALTH SUMMARY  9    BDV LABS                          VISITS  10   CLINICAL MAINTENANCE              CLINICAL MAINTENANCE  11   HS TEST IMPORT                    XRAY  12   KR MED BRIEF                      Medicine (Brief)  13   LAB SEL 1                         Selected Labs (Diabetes)  14   MY RESP                           DEM  +         Enter ?? for more actions  Create New TIU Object                   Find  Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object  Quit  Select Action: Next Screen// **&lt;Enter&gt;** NEXT SCREEN  TIU/Health Summary Objects    Mar 27, 2003@08:26:15          Page:    2 of    2.  TIU Object Name                   Health Summary Type                     .  15   PODIATRY                          Podiatry  16   PODIATRY OBJECT                   Podiatry  17   SELECTED LABS                     Selected Labs (Diabetes)  18   SURGERY REPORTS                   SURGERY REPORTS  19   OBJECT DEMO                       MICRO  20   VISITS                            FUTURE VISITS  Enter ?? for more actions  Create New TIU Object                   Find  Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object  Quit  Select Action: Quit//  ##### Actions Descriptions  The two actions that are the most useful are Edit HS Object and Edit HS Type. The first allows you to change the display parameters in the Health Summary Objects file (provided you own them). The second action allows you to change the Health Summary Type components. These actions are only available from the HS OBJECT DISPLAY screen accessed with the Detailed Display/Edit HS Object action.  Create TIU/Health Summary Objects [TIUHS LIST MANAGER]  &#124;  -----Create New TIU Object  &#124;  -----Detailed Display/Edit TIU Object  &#124;   &#124;  &#124;   &#124;-----Change HS Object  &#124;   &#124;  &#124;   &#124;-----Change Health Summary Type  &#124;   &#124;  &#124;   &#124;-----Detailed Display/Edit HS Object  &#124;        &#124;  &#124;        &#124;-----Edit HS Object  &#124;        &#124;  &#124;        &#124;-----Change HS Type  &#124;        &#124;  &#124;        &#124;-----Inquire about a HS Type  &#124;        &#124;  &#124;        &#124;-----Edit HS Type  &#124;  -----Detailed Display/Edit HS Object  &#124;   &#124;  &#124;   &#124;-----Edit HS Object  &#124;   &#124;  &#124;   &#124;-----Change HS Type  &#124;   &#124;  &#124;   &#124;-----Inquire about a HS Type  &#124;   &#124;  &#124;   &#124;-----Edit HS Type  &#124;  -----Find  -----Quit  ###### Create New TIU Object  This action creates a new TIU Health Summary Object in the TIU Document Definition file and establishes a pointer to the HS Object.  ###### Find  This action allows you to quickly locate a TIU Health Summary Object. If there are more than 14 TIU HS Object names in the TIU Document Definition file, then you can use this action to quickly locate the name you want to examine or modify.  ###### Detailed Display/Edit TIU Object  The Detailed Display/Edit TIU Object allows you to view and make adjustments to  a TIU Health Summary Object. The display appears as follows:  TIUHS Detailed Display/Edit   Jan 03, 2003@15:47:08          Page:    1 of    1 .  .  TIU Object Name: PODIATRY  Owner: CPRSPROVIDER,TEN  Status: ACTIVE  HS Object: PODIATRY OBJECT (TIU)  HS Type: AC CLINICAL SUMMARY  Technical Field: S X=$$TIU^GMTSOBJ(DFN,6600042)  Enter ?? for more actions  Change HS Object                  Detail Display/Edit HS Parameters  Change Health Summary Type  Select Item(s): Quit//  ###### Change HS Object  This action changes the item in the Health Summary Objects file that is pointed to by this TIU HS Object. You cannot use this command unless you are on record as the creator of the TIU Health Summary Object. See the discussion on file relationships at the beginning of this section.  You may only change the HS Object if you own the (originally created) the TIU Object. If you attempt to change any part of a TIU object that you did not originally create, the system will display the following message:  Can't edit this HS Object:  Only the owner can edit this HS Object  ###### Change Health Summary Type  This action changes the item in the Health Summary Types file that is pointed to by the HS Object. You cannot use this command unless you are on record as the creator of the HS Object. See the discussion of file relationships at the beginning of this section.  You may only edit a TIU Health Summary Object that you own (originally created). If you attempt to edit an object created by another,  the system will display the following message:  Can't edit this HS object:  Only the owner can edit this HS object.  ###### Detail Display/Edit HS Object  This action provides a detailed display of the contents of the Health Summary Object file for this TIU HS Object. Here is an example of this display:  HS OBJECT DISPLAY             Jan 03, 2003@16:13:21          Page:    1 of    1 .  Detailed Display for PODIATRY  .  HS Object: PODIATRY OBJECT (TIU)  Health Summary Type: AC CLINICAL SUMMARY  Report Period:  Creator: CPRSPROVIDER,TEN  HS Object  Print Label: NO         Print Report Date and Time: NO  Print Blank Line after Label: NO       Print Confidentiality Banner: NO  Customized Header: YES        Print Report Date and Time: NO  Suppress Components w/o Data: NO             Print Component Header: YES  Print Deceased Information: NO       Print Time-Occurrence Limits: NO  National Object: NO         Underline Component Header: NO  Blank Line After Header: NO  Enter ?? for more actions  Edit HS Object                          Inquire about a HS Type  Change HS Type                          Edit HS Type  Select Action: Quit//  ###### Edit HS Object  This action allows you to change the HS display parameters as stored in the Health Summary Object file. This action takes you into code that is accessible from Health Summary menus, specifically Create/Modify Health Summary Object [GMTS OBJ ENTER/EDIT]. For complete information on the actions, see Create/Modify Health Summary Object in the *Health Summary User Manual* V.2.7 updated January, 2003.  Note: 	You must page through each parameter for your changes to be effective. You cannot ^ out of this action and have any changes you make take effect.  You may only edit a Health Summary Object that you own (originally created). If you attempt to edit an object created by another,  the system will display the following message:  Can't edit this HS Object:  Only the owner can edit this HS Object  ###### Change HS Type  This action changes the HS Type that is pointed to by the Health Summary Object. You must own (have created) the object to use this action.  In this example, we change the HS Type associated with a HS Object:  Select Action: Quit// **CH** Change HS Type  ***WARNING*** By changing the HS Type this will change the output data.  Continue? NO// **Y** YES  Enter HEALTH SUMMARY TYPE: ?  Answer with HEALTH SUMMARY TYPE NAME, or TITLE, or OWNER, or  LOCATION(S) USING THE SUMMARY  Do you want the entire HEALTH SUMMARY TYPE List? N  (No)  Enter HEALTH SUMMARY TYPE: **DISPLAY APP** OINTMENTS  HS OBJECT DISPLAY             Apr 24, 2003@08:49:53          Page:    1 of    1.  Detailed Display for VISITS  .  HS Object: VISITS (TIU)  Health Summary Type: DISPLAY APPOINTMENTS  Report Period:  Creator: CPRSPROVIDER,TEN  HS Object  Print Label: NO         Print Report Date and Time: NO  Print Blank Line after Label: NO       Print Confidentiality Banner: NO  Customized Header: YES        Print Report Date and Time: NO  Suppress Components w/o Data: NO             Print Component Header: YES  Print Deceased Information: NO       Print Time-Occurrence Limits: NO  National Object: NO         Underline Component Header: NO  Blank Line After Header: NO  Enter ?? for more actions  Edit HS Object                          Inquire about a HS Type  Change HS Type                          Edit HS Type  Select Item(s): Quit//  If you do not own (did not create) the HS Object, then the program will not allow you to change the HS type and you will receive the following message:  Can't edit this HS Object:  Only the owner can edit this HS Object  ###### Inquire about a HS Type  This action allows you to view on the screen any Health Summary Type. To do this, you need to supply the name of the HS Type as in the following example:  Select Action: Quit// **IN** Inquire about a HS Type  Select Health Summary Type: **GASTRO-1** GASTRO-1  Gastro-1  OK?  YES// **&lt;Enter&gt;**  DEVICE:   ANYWHERE    Right Margin: 80//  HEALTH SUMMARY TYPE INQUIRY  Type Name:  GASTRO-1  Title:  Owner:  CPRSPROVIDER,ELEVEN  SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:  yes  Max        Hos  ICD   Pro  CPT  Abb   Ord    Component Name        Occ  Time  Loc  Text  Nar  Mod  Selection  ------------------------------------------------------------------------------  DCS   5       Discharge Summary         1Y  II    10      Radiology Impression      1Y  CH    15      Chem &amp; Hematology         1Y  CY    20      Cytopathology             1Y  SR    25      Surgery Reports           1Y                    YES  SP    30      Surgical Pathology        1Y  * = Disabled Components  Enter RETURN to continue or '^' to exit:  Note: 	This action is only available from the HS Object Display screen. It is provided so that you can explore Health Summary types while working with HS Objects.  ###### Edit HS Type  This action is the same as Create/Modify Health Summary Type in the Health Summary package. See the *Health Summary User Manual* for details.  You may only edit a Health Summary Type that you own (originally created). If you attempt to edit a type created by another, the system will display the following message:  You cannot edit a Health Summary Type you don't own.  ### Appendix C: Additional Signer Utility Guide  Text Integration Utilities (TIU) is a set of software tools designed to handle clinical documents in a standardized manner, with a single interface for viewing, entering, editing, and signing clinical documents.  This appendix describes how to use the Additional Signer Utility.  #### Introduction  Additional Signer is a communication tool used to alert a clinician about information pertaining to the patient. This functionality is designed to allow clinicians to call attention to specific documents and the recipient to acknowledge receipt of the information. Being identified as an additional signer does not constitute a co-signature. This nomenclature in no way implies responsibility for the content of, or concurrence with the note.  #### Version 2.0  Version 2.0 is released with patch TIU*1.0*357. Additional Signer reports created with version 1.0 of the utility are not compatible with version 2.0 and must be removed before the new version may be used.  If you would like to save any old reports, you must view them and save them to a host file or screen capture them with logging **BEFORE** installing TIU*1.0*357.  At the prompt, “Remove the old reports now? NO//”, you must enter YES to continue.  ** WARNING **  Reports generated with v1 are NOT compatible and must be removed before use.  Additional Signer data in TIU MULTIPLE SIGNATURE [File #8925.7] will not be  altered.  This process may take a few minutes and only needs to be completed once.  Remove the old reports now? NO// YES  Removing entries in ^XTMP...done.  Press &lt;Enter&gt; to continue.  **Note** :  If there are no outstanding additional signatures or reports to view, the utility will display that information before exiting.  No outstanding signatures or reports to view.  The utility’s menu is dynamically generated based on the following criteria:  - Outstanding Additional Signatures - Additional Signature report(s) available to view  If there are outstanding signatures but no reports to view, the default behavior is GENERATE and the menu will display the following:  Additional Signer Utility  1  GENERATE a Report  2  REMOVE Additional Signer(s)  3  BOTH [Generate a Report &amp; Remove Additional Signer(s)]  4  QUIT  What would you like to do? GENERATE//  If there are outstanding signatures and reports to view, the default behavior is GENERATE and the menu will display the following:  Additional Signer Utility  1  GENERATE a Report  2  REMOVE Additional Signer(s)  3  BOTH [Generate a Report &amp; Remove Additional Signer(s)]  4  VIEW Generated Report(s)  5  QUIT  What would you like to do? GENERATE//  If there are no outstanding signatures and one or more reports to view, the default behavior is VIEW and the menu will display the following:  1  VIEW Generated Report(s)  2  QUIT  What would you like to do? VIEW//  #### General Information  Additional Signer data is stored in the TIU MULTIPLE SIGNATURE File (#8925.7). For additional signers, this file maintains data on the following fields:  - TIU Document Number - Additional Signer IEN - Signature Date/Time - Signature Block Name &amp; Title - Signature Mode - Signed by Surrogate  **Important:** TIU does not track who assigns an additional signer to a document or when the additional signer was added. Typically, an expected signer or co-signer would be the user who assigns additional signers. However, any user in the appropriate user class permitted by business rules may assign additional signers to a document. There is also no tracking of a removed additional signer other than the reports generated by this utility.  The Additional Signer Utility allows a user to perform the following actions on the TIU MULTIPLE SIGNATURE File (#8925.7):  - Generate a report of outstanding additional signatures for a date range or a specific user. - Remove outstanding additional signers for a date range or a specific user. - Both actions above simultaneously. - View a report and output to a user entered device.  Reports are generated via a task and the user will receive an email when the task has been completed and the report is ready.  The email message contains the following information:  - Mode report was generated - Total number of outstanding signatures - Date range or Additional Signer - Elapsed time to gather report data  **Note:** VIEW the Report will be available only after one or more reports have been completed and ready to display. Report data is stored in the ^XTMP global and is purged automatically 7 days after the utility was last used. All reports need to be printed if there is a need to EVER see them.  The new option, TIU ADD SIGN UTIL (Additional Signer Utility), should be added to the desired user’s secondary menu option and should not be made available on an existing TIU menu.  The introductory display for the utility:  VHA HANDBOOK 1907.01 defines the additional signer role as follows:  "Additional signer" is a communication tool used to alert a clinician about  information pertaining to the patient.  This functionality is designed to  allow clinicians to call attention to specific documents and the recipient to  acknowledge receipt of the information.  Being identified as an additional  signer does not constitute a co-signature.  This nomenclature in no way implies  responsibility for the content of, or concurrence with, the note."  This utility provides options to report and/or remove outstanding additional  signers and the associated alerts by either date range or additional signer.  ** WARNING **  Removing additional signers from a document is PERMANENT and cannot be undone.  ** WARNING **  Press &lt;Enter&gt; to continue.  The main display for the utility:  Additional Signer Utility  1  GENERATE a Report                         2  REMOVE Additional Signer(s)                         3  BOTH (Generate &amp; Remove)                         4  VIEW Report(s)                         5  QUIT  What would you like to do? GENERATE a Report// ?  Enter a code from the list.  Select one of the following:  1         GENERATE a Report  2         REMOVE Additional Signer(s)  3         BOTH (Generate &amp; Remove)  4         VIEW Report(s)  5         QUIT  What would you like to do? GENERATE a Report//  **Note:** If there are no outstanding additional signers or generated reports to view, the utility will display:  No outstanding signatures or reports to view.  Press &lt;Enter&gt; to continue.  #### Options  There are 4 options” GENERATE a Report, REMVOE Additional Signer(s), BOTH [Generate a Report and Remove Additional Signer(s)] and VIEW Generated Report(s).  ##### GENERATE a Report  This option gathers data based on the user entered date range or user. No data is altered by this action.  What would you like to do? GENERATE// 1  GENERATE a Report  Select SEARCH CRITERIA:  1 Date Range            2 Additional Signer      3 Service/Section  4 Division              5 Document Status        6 DISUSER'D  7 Terminated  Enter SELECTION: 1//  The SEARCH CRITERIA is selectable by list or range, e.g., 1,3,5 or 2-4,7.  You may select any combination of criteria. By default, if you select any criteria without selecting date range, the utility will search ALL outstanding additional signatures for the entire date range available. All SEARCH CRITERIA is inclusive of each other for a given search and all entries must meet each criteria selected.  Date Range The default STARTING DATE is the oldest date with at least 1 outstanding additional signature.  The default ENDING DATE is TODAY Additional Signer The NEW PERSON that must be identified as the additional signer if entered. Service/Section All additional signers must be assigned to the entered Service/Section if entered. Division All additional signers must be a member of the Division if entered. Document Status The TIU DOCUMENT STATUS of the document to be included in the report. DISUSER’D If selected, additional signers must DISUSER’D (Disabled User=YES). Terminated If selected, additional signers must be terminated as of TODAY.  **Note** :  Additional Signer Report results must meet ALL entered criteria. Conflicting criteria that will yield no results will be displayed prior to initiating the search.  ##### REMOVE Additional Signer(s)  This option will permanently remove/delete additional signers from the TIU MULTIPLE SIGNATURE File that meet the entered SEARCH CRITERIA. The search function performs identically to GENERATE a Report. Once removed, the additional signer will no longer appear in the document body in CPRS and any pending alerts will be removed:  The following will no longer appear in CPRS for additional signers removed by the utility:  Receipt Acknowledged By:  * AWAITING SIGNATURE *       PROVIDER,ONE  **Note:** This action can NOT be undone or recovered.  ##### BOTH [Generate a Report &amp; Remove Additional Signer(s)]  This option creates a report of outstanding additional signers that meets the search criteria and permanently removes the entries from the TIU MULTIPLE SIGNATURE File. The report output adds information to the REMOVED and REMOVED BY columns indicating that the entries in the report were removed from the TIU DOCUMENT(s) during report creation.  ##### VIEW the Report  This option is only available after a task running in GENERATE or BOTH modes have completed for the same user session (by Kernel Job #). This option will only be visible if there are pending or existing report(s) to view. If there is one or more reports being generated but not yet complete, the utility will display the following:  Report          Generated          # Additional                   Date Range  #  Generated By    Date@Time            Signatures        [Additional Criteria]  No completed report to view.  [Report(s) currently in progress.]  Press &lt;Enter&gt; to continue.  Once one or more report(s) have been completed, the utility will display the available report(s) for selection.  Select the report by entering the desired number in the # column.  Example:  VIEW Generated Report(s) display  Report          Generated          # Additional                  Date Range  #  Generated By    Date@Time            Signatures       [Additional Criteria]  1  REPORT,USER     06/14/23@08:26            53088    Mar 30, 1998-Jun 14, 2023  Which report would you like to display?  The additional signer reports are designed for a 255-character wide-column display in a comma separated value (CSV) format.  If your session is not configured to display 255 characters per row, see     0 Terminal Settings – Logging and Terminal Display.  Example DEVICE setting:  &lt;device&gt;; Right Margin  The utility will prompt for DEVICE:  This output is designed for 255 characters per row.  Example DEVICE setting:  ;255  DEVICE: HOME// ?  Specify a device with optional parameters in the format  Device Name;Right Margin;Page Length  or  Device Name;Subtype;Right Margin;Page Length  Or in the new format  Device Name;/settings  or  Device Name;Subtype;/settings  For example  HOME;80;999  or  HOME;C-VT320;/M80L999  Enter ?? for more information  Before displaying &amp; capturing a report, ensure that your terminal is setup for 255-character wide output and logging.  There are instructions following this section provided for information purposes.  **Note:** If screen capture is enabled via logging, you do not need to resize your terminal window to log the data output.  After selecting a report to view, enter the desired setting for the DEVICE.  After pressing &lt;Enter&gt;, the report will pause so that you may capture the output via logging:  At the following prompt, start logging to a text file:  This output is designed for 255 characters per row.  Example DEVICE input:  ;255;9999999  DEVICE: HOME// ;255  HOME  To capture the report output, start logging now and press &lt;Enter&gt; to begin.  When the display is complete, stop logging at the prompt:  9932761,"PROVIDER,ONE","BAY PINES TEST LAB","CLEVELAND VAMC",,,"AA LAD,LAKXUM (A1033)","ADDENDUM","AJB NOTE TITLE",01/17/2023,UNSIGNED,06/06/2023,06/06/2023,"BAKKE,ANDREW J",,,  [stop logging before you...] Press &lt;Enter&gt; to continue.  The text output is now ready to import for viewing the results.  #### Importing into Excel  In Excel, from a new sheet:  Data &gt; From Text/CSV &gt; Locate &amp; Select the Log File.  At the data window, click “Load”:  <!-- image -->  You may sort by the following fields/columns:  Field/Column Definition  IEN Internal Entry Number.  TIU DOCUMENT # in detailed view of CPRS. ADDITIONAL SIGNER* NEW PERSON in the TIU MULTIPLE SIGNATURE file. SERVICE/SECTION* Service/Section of the Additional Signer [optional]. DIVISION* Division of the Additional Signer [optional]. DISUSER YES indicates the Additional Signer is currently disabled [optional]. TERMINATED Termination Date of the Additional Signer [optional]. PATIENT* LASTNAME,FIRSTNAME (L####) – last/first limited to 22 characters (30 total). LOCAL TITLE* TIU DOCUMENT TITLE (File #8925.1). PARENT TITLE* TIU DOCUMENT TITLE if LOCAL TITLE is addendum [conditionally optional]. PARENT DATE REFERENCE DATE of PARENT TITLE [conditionally optional]. STATUS DOCUMENT STATUS. ENTRY DATE Actual date document is created. REFERENCE DATE This date may differ from the ENTRY DATE.  Used for sorting in CPRS. EXPECTED SIGNER* File #8925, Field #1204. EXPECTED COSIGNER* File #8925, Field #1208. REMOVED Date additional signer entry was removed. REMOVED BY* NEW PERSON responsible for creating & removing the additional signer entry. * Indicates this field may be truncated if the length of the data exceeds the 255-character limit. * Indicates this field may be truncated if the length of the data exceeds the 255-character limit.  **Note:** Fields are dynamically truncated in this order only as needed:  REMOVED BY, EXPECTED COSIGNER, EXPECTED SIGNER, PARENT TITLE, LOCAL TITLE, DIVISION, SERVICE/SECTION, ADDITIONAL SIGNER.  Once the length of data no longer exceeds 255 characters, fields will no longer be truncated.  #### Terminal Settings – Logging and Terminal Display  These instructions are for the Reflection Workspace software.  Depending on your appearance configuration, your menus/options may not appear exactly as shown but the configuration pages should be the same.  **Logging:** Select File&gt;Logging, at the “Logging Settings” window, select “Disk” and browse to a file location &amp; name you can easily find later.  <!-- image -->  <!-- image -->  **255-character display:** Select Setup&gt;Terminal&gt; From the Terminal Window, select Display:  <!-- image -->  <!-- image -->  From the “Set Up Display Settings” Window, under “Dimensions”, “Number of characters per row:”, enter 255.:  <!-- image -->  ### Index  128, 216  8925, 36, 39, 40, 144, 148, 174, 204, 209  8925.1, 43, 144, 157, 174, 190, 201, 254, 256, 267  8925.2, 145, 159  8925.3, 145, 159  8925.4, 145, 159  8925.5, 145, 159  8925.6, 145, 160  8925.7, 145, 160  8925.8, 145, 160  8925.9, 145, 161  8925.91, 146, 161  8925.93, 95, 96, 98, 146, 161  8925.94, 96, 146, 161  8925.95, 146, 162  8925.97, 146, 162  8925.98, 146, 162  8925.99, 146, 162  8925-8926, 185  8926, 146, 162, 163, 164, 165, 166, 167  8927, 167  8927.1, 168  8932.1, 210  abort transfer, 24  action, 186  **actions** , 79, 274  Actions Across Applications, 134  Active Title Cleanup, 104  Add/Edit Local Synonyms, 112  Admission- Prints all PNs for Current Admission, 95  ambulatory, 223  Ambulatory Care Data Capture, 222  APIs, 171  Archiving and Purging, 169  ASCII, 1, 23  ASCII Protocol, 25  ASCII Protocol Upload, 45  ASCII protocol upload / with aler, 47  ASU, 88, 186, 228  Author Print Progress Notes, 94  Authorization/Subscription/Utility, 88  authorized, 88  Automated Mapping of Titles, 115  Basic TIU Parameters, 17  Batch Print Outpt PNs by Division, 95  batch printing, 98, 212  batch upload of Progress Notes, 215  Batch Upload Reports, 45  boilerplate, 1, 186  boilerplate text, 78, 208  Build File Print, 182  business rules, 212  Business Rules, 230  C&amp;Ps, 215  captioned headers, 52  Change Health Summary Type, 276  Change HS Object, 275  Change HS Type, 277  chart, 99  CIRN, 222  class, 78, 191  class owner, 202  Clinical Coordinator Menu, 132  clinical documents, 217  clinician, 186  component, 78, 186, 192  contiguous, 99  cosignature, 211  CPRS, 2  Create Document Definitions, 71  Create New TIU Object, 275  Create Objects, 71  Create Post-Signature Alerts, 71  Create TIU/Health Summary Objects, 267  Creating an Object, 233, 280  Creating an Object Based on Health Summary, 267  creating objects, 80  Creation of Business Rules, 230  Cross-References, 148  Data Dictionaries, 185  Data Standardization Background, 101  DBIA, 171  default printer, 98  Delete TIU templates, 91  Direct Mapping Note Titles, 109  Discharge Summaries, 88, 222  Discharge Summary, 1, 187  Display Upload Help, 52  DIVISION, 153  Division - Progress Notes Print Parameters, 16, 68  document class, 78, 187, 191  Document Definition, 187  Document definition hierarchy, 14  Document DefinitionOptions, 71  Document Definition Terminology, 78  Document Defintion Terminology &amp; Rules, 190  Document Definitions, 69  Document Definitions (Manager) menu, 267  Document File #8925, 209  Document Parameter Edit, 16, 53, 211  Document upload, 14  DUPLEXing, 99  Edit Business Rules, 90  Edit Document Definitions, 71  Edit HS Object, 277  Edit HS Type, 279  electronic signature, 14  embedded text, 78  Enter Upload Utility Parameters, 25  Enterprise Standard Title, 119  EPNs, 98  EXCLUDE FROM PN BATCH PRINT, 98  Exported Routines, 101  External Relations, 170  FAQs, 209  File #128, 216  File #8925, 36, 39, 40, 144, 148, 174, 204, 209  File #8925.1, 43, 144, 157, 174, 190, 201, 254, 256, 267  File #8925.2, 145, 159  File #8925.3, 145, 159  File #8925.4, 145, 159  File #8925.5, 145, 159  File #8925.6, 145, 160  File #8925.7, 145, 160  File #8925.8, 145, 160  File #8925.9, 145, 161  File #8925.91, 146, 161  File #8925.93, 95, 96, 98, 146, 161  File #8925.94, 96, 146, 161  File #8925.95, 146, 162  File #8925.97, 146, 162  File #8925.98, 146, 162  File #8925.99, 146, 162  File #8926, 146, 162, 163, 164, 165, 166, 167  File #8927, 167  File #8927.1, 168  File #8932.1, 210  files, 144  Files 8925-8926, 185  Frequently Asked Questions, 209  Functional Overview, 1  Functions Across Applications, 134  Globals, 184  Glossary, 186  GMTS OBJ ENTER/EDIT, 277  handling upload errors, 47  HAS BOILTXT, 204  HCFA, 228  Health Summary Objects, 267  Health Summary Objects file, 268  Health Summary Type file, 268  Help for Upload Utility, 42  helpful hints, 209  heritable, 206  hidden actions, 217  historical, 223  historical visits, 211, 224  Host File Server, 23  How to Get Online Documentation, 182  Implement Upload Utility, 22  Implementation &amp; Maintenance, 14  *Implementation Guide* , 14  IN USE, 203  inpatients, 223  Inquire about a HS Type, 278  Inter-facility data transfer, 221  interim, 213  interward transfers, 214  Intranet WWW Documentation, 182  Introduction, 1  IRT deficiency, 214  Items, 207  Kermit, 23  Kermit file transfer protocol,, 24  Kermit Protocol, 33  Kermit Protocol Upload:, 45  Kernel Print Options, 184  KIDS Install Print Options, 182  line editors, 213  Linkages, 2  List Membership by Class, 90  List Membership by User, 90  Location Print Progress Notes, 94  lost documents, 209  macros, 52  Manage Business Rule, 90  **Map Active Local Titles** , 115  **Mapping and Reporting Standard Titles** , 101  Mapping Workbench, 109  MAS Options to Print Progress Notes, 95  MAS Print Options, 96  Matrix of Actions, 79  Menu and Option Assignment, 126  Menu Assignment, 132, 232  Menu Text, 207  message header, 43  MIS, 187  **MIS Manager** , 187  Missing Text Cleanup, 129  Missing Text Report, 129  Mnemonic, 207  Mnemonics on List Manager screens, 219  Modify Upload Parameters, 16, 25  MRT, 188  multidisciplinary, 14  **Namespace** , 101  national standard, 195  New Term Rapid Turnaround Process, 119  **NTRT Website** , 119  number-spaces for TIU, 185  object, 78, 188, 193, 233, 280  Object Inactive, 251  Online Documentation, 182  OP reports, 215  orphan, 205  Other Kernel Print Options, 184  outpatient care, 223  Outpatient Location- Print Progress Notes, 95  owner, 79, 201  Package-Wide Variables, 181  Patient Care Encounter, 2  patient encounter, 211  Patient Print  Progress Notes, 94  PCE, 222  Person Class File (#8932.1), 210, 228  personal owner, 201  print by ward, 212  Print List, 217  print name, 204  Print Screen, 217  Printing Data Dictionaries, 185  Problem List, 2  Progress Notes, 1, 88, 188, 222  Progress Notes Batch Print Locations, 17, 67  Progress Notes Print Options, 94, 96, 98  Provider Class, 210  Provider Security Key, 229  PSI-04-016, 209  Purging, 14  Radiology reports, 215  Raw ASCII file transfer, 23  Reassignment Document Report, 127  recover, 209  release from transcription, 213  Remote Computer, 23  rotating residents, 215  Router/Filer Notes, 43  Routines, 101, 184  RPCs, 171  Screen Editor, 213  security, 231  security key, 88, 231  **Selected Title Map** , 117  Setting Up TIU, 15  Set-up for User Class &amp; Business Rules, 229  share objects, 218  shared, 194  Shortcuts, 219  Signature, 14  signature block, 14  site-configurable, 14  site-configurable features, 14  Smart Term, 212  Sort Document Definitions/ Objects, 71  standalone visit, 223  status, 79, 196  Status Report of your Unmapped Titles, 118  subscribe, 88  surrogate, 211  telephone, 223  TEMP global, 209  template, 78  template cleanup parameter, 91  Template Management, 91  terminal and ASCII transfer options, 23  terminal emulation software, 23  Terminal Emulator, 23  terminal settings, 212  terminology, 78  TEXT global, 209  **Text Integration Utility Nightly Task** , 218  title, 78, 188, 192  TIU Autoverify, 231  TIU BASIC PARAMETER EDIT, 16  TIU CONVERSIONS MENU, 133  TIU DIVISION PRINT PARAMETERS FILE #8925.94, 96  TIU Document Definition file, 268  TIU DOCUMENT PARAMETER EDIT, 16  TIU File Descriptions, 144  TIU MAIN MENU, 132  TIU MAIN MENU CLINICIAN, 132  TIU MAIN MENU MGR, 132  TIU MAIN MENU MRT, 132  TIU MAIN MENU PN CLINICIAN, 132  TIU MAIN MENU REMOTE, 133  TIU MAINTENANCE MENU, 133  TIU NIGHTLY TASK, 218  TIU PRINT PARAMETERS FILE, 96  TIU PRINT PN ADMISSION, 95, 98  TIU PRINT PN BATCH INTERACTIVE, 67, 95  TIU PRINT PN BATCH SCHEDULED, 67  TIU PRINT PN DIV PARAM, 16  TIU PRINT PN DIV PARAMS, 68  TIU PRINT PN LOC PARAMS, 17, 67  TIU PRINT PN MAS MENU, 95, 133  TIU PRINT PN OUTPT LOC, 68, 95, 98  TIU PRINT PN USER MENU, 133  TIU PRINT PN WARD, 68, 95  TIU Security, 231  TIU TEMPLATE CONSULT LOCK, 91, 131  TIU UPLOAD DOCUMENTS, 42  TIU UPLOAD HELP, 42  TIU UPLOAD PARAMETER EDIT, 16  TIU*, 185  **TIU*1*211** , 102  TIUF DOCUMENT DEFINITION MGR, 69, 268  TIUFA SORT DDEFS, 71  TIUFC CREATE DDEFS, 71  TIUFH EDIT DDEFS, 71  TIUFJ CREATE OBJECTS MGR, 71  TIUFJ VIEW OBJECTS CLIN, 71  TIUFLAG, 99  TIUFPC CREATE POST-SIGNATURE, 71  TIUHS LIST MANAGER, 267  transcription, 213  transcriptionist, 14, 212  troubleshooting, 209  Troubleshooting &amp; Helpful Hints for Document Definitions, 224  type, 191  Unmapped Titles, 118  Unsigned/Uncosigned Report, 127  Upload Documents, 42  upload errors, 47  Upload Menu, 41  Upload Parameters, 25  user, 79  User Class, 189  User Class Assignment, 231  User Class definition, 14  User Class Definition, 90  User Class File (#8930), 228  User Class Information, 228  User Class Management, 89, 91  USR BUSINESS RULE MANAGEMENT, 90  USR CLASS DEFINITION, 90  USR CLASS MANAGEMENT MENU, 89  USR EDIT BUSINESS RULES, 90  USR LIST MEMBERSHIP BY CLASS, 90  USR LIST MEMBERSHIP BY USER, 90  VA Cross-Referencer, 185  View Objects, 71  Visit Information, 219  Visit Orientation, 221  Visit Tracking, 2  visits, 211  VT220, 212  Ward- Print Progress Notes, 95  word-processing program, 23, 213  work copy, 99  Workload Capture, 221  WWW, 182                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create Document Definitions  | TIUFC CREATE DDEFS           | The Create Document Definitions option lets you create new entries of any type (Class, Document Class, Title, Component) except Object, placing them where they belong in the hierarchy. Although entries can be created using the Edit and Sort options, the Create option streamlines the process. The Create option permits you to view, edit, and create entries ( if the entry is not marked National Standard). The Create Option doesn’t let you copy an entry. |
| Edit Document Definitions    | TIUFH EDIT DDEFS             | The Edit Document Definitions Option lets you view and edit entries. Since Objects don’t belong to the hierarchy, they can’t be viewed or edited using the Edit Option.                                                                                                                                                                                                                                                                                                |
| Sort Document Definitions    | TIUFA SORT DDEFS             | The Sort Document Definitions option lets you view and edit entries by selected sort criteria (displayed in alphabetic order by name rather than in hierarchy order). Entries can include Objects.                                                                                                                                                                                                                                                                     |
| Create Objects               | TIUFJ CREATE OBJECTS MGR     | This option lets you create new objects or edit existing objects. Existing objects are displayed for you within a selected alphabetical range.                                                                                                                                                                                                                                                                                                                         |
| View Objects                 | TIUFJ VIEW OBJECTS CLIN      | This option lets you review existing objects within a selected alphabetical range.                                                                                                                                                                                                                                                                                                                                                                                     |
| Create Post-Signature Alerts | TIUFPC CREATE POST-SIGNATURE | This option allows clinicians and providers to create progress notes that automatically generate a notification (alert) to designated recipients based on the progress note title. This enables immediate communication of time-sensitive patient information to designated people.                                                                                                                                                                                    |

Setting Up TIU Text Events

Patch TIU*1*296 modifies the TIU application to send a TIU alert to the appropriate service provider(s) immediately after a staff member screens a patient and signs the associated note. The service provider(s) will be alerted prior to the note being co-signed by the licensed clinician responsible for reviewing and approving the note. Prior to this modification, TIU alerts were not sent to all service providers. This resulted in missed opportunities to provide needed services for patients while the patients are on site, and forced staff to take time to contact patients and reschedule needed services.

A new Text Event Edit [TIU TEXT EVENT EDIT] option is available in the TIU Maintenance menu.

Select the **Text** Event Edit menu option to set up a “text event” in the TIU TEXT EVENTS file (#8925.71). Complete all fields, including the trigger text to be searched for in a TIU document (progress note, consult note, etc.). If the trigger text is found in the TIU document, then an alert is sent to the team(s) specified in the file.

The following example shows “ab color blindness” as the trigger text [TEXT TO SEARCH]. The alert message [ALERT MESSAGE] patient has ab color blindness will be sent to the specified service provider [CPRS TEAM]. An alert [SIGNER ALERT MESSAGE] is also sent to the individual who signed the note.

Select TIU Maintenance Menu &lt;TEST ACCOUNT&gt; Option: txt	Text Event Edit

Select TIU TEXT EVENTS NAME: test 5

Are you adding 'test 5' as a new TIU TEXT EVENTS (the 8TH)? No// yes	(Yes) NAME: test 5//

STATUS: ?

Enter a 0 for inactive or a 1 for active Choose from:

0	INACTIVE

1	ACTIVE

STATUS: 1	ACTIVE TEXT TO SEARCH: ?

Answer must be 3-200 characters in length.

TEXT TO SEARCH: ab color blindness CASE SENSITIVE: ?

Enter a 0 for NO or a 1 for YES. Choose from:

0	NO

1	YES

CASE SENSITIVE: no	 INCLUDE SPACES: yes	YES

<!-- image -->

TEXT TO SEARCH:  ab color blindness

ALERT MESSAGE: patient has ab color blindness SIGNER ALERT MESSAGE: ?

Answer must be 1-6 characters in length.

SIGNER ALERT MESSAGE: ab

Select CPRS TEAM: team test Select CPRS TEAM: TEST TEAM ?? Select CPRS TEAM: TEAM TEST

...OK? Yes// YES	(Yes)

CPRS TEAM: TEAM TEST//

Select CPRS TEAM:

Select TIU TEXT EVENTS NAME:

<!-- image -->

 **Note:** Any TIU document that is to be used to trigger these alerts must have the MUMPS code ‘D TASK^TIUTIUS($S($G(DAORIG):DAORIG,1:DA))’ entered in the POST-SIGNATURE CODE field (#4.9) in the TIU DOCUMENT DEFINITION file (#8925.1). This field can only be edited by IRM personnel.

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 
TIU DOCUMENT DEFINITION// EDIT WHICH FIELD: 
ALL// 4.9POST-SIGNATURE CODE THEN EDIT FIELD:

Select TIU DOCUMENT DEFINITION NAME:  NURSING PROGRESS NOTE     TITLE

Std Title: NURSING NOTE

POST-SIGNATURE CODE: D TASK^TIUTIUS($S($G(DAORIG):DAORIG,1:DA))//

<!-- image -->

##### Creating Post-Signature Alerts Based on Progress Note Title

The Create Post-Signature Alerts [TIUFPC CREATE POST-SIGNATURE] option in the Document Definitions (Manager) [TIUF DOCUMENT DEFINITION MGR] menu allows clinicians and providers to create progress notes that automatically generate a notification (alert) to designated recipients based on the progress note title. This enables immediate communication of time-sensitive patient information to designated individuals or groups. These alerts are specific to each VA Medical Center.

To create or edit a Post-Signature Alert:

1. Select the Create Post-Signature Alerts [TIUFPC CREATE POST-SIGNATURE] option in the Document Definitions (Manager) [TIUF DOCUMENT DEFINITION MGR] menu.
2. At the "Select TIU DOCUMENT DEFINITION NAME" prompt, enter the progress note title that will generate the alert. Typing “??” and then pressing Enter provides a list of titles already available in VistA.

If an alert is already associated with this title, then the existing Post-Signature code is displayed—continue to Step 0. If there is no existing alert associated with the title, skip to Step 3.

If an alert is already associated with the selected title, then the Post-Signature code is displayed and the "Do you want to change the Code? (YES or NO)? NO// " prompt is displayed.

Enter “YES” if you wish to change the code, and then complete the remaining steps in this procedure. Enter "NO" to retain the current code. The "Enter &lt;RETURN&gt; for another TIU Document Definition Name or '^' to exit" prompt displays and you have the option to enter another title (returning you to Step 2) or exit "Enter Post-Signature Code for Alert."

Enter Post-Signature Code for Alert

===================================

Select TIU DOCUMENT DEFINITION NAME: RESTRAINT

1   RESTRAINT PROGRESS NOTE AND EVERY TWO HOUR FLOW SHEET       TITLE

Std Title: SECLUSION RESTRAINT NOTE

2   RESTRAINT  12-8 RESTRAINT DOCUMENTATION 1:1 OR SOFT - 12-8     TITLE

3   RESTRAINT  8-4 RESTRAINT DOCUMENTATION 1:1 OR SOFT - 8-4     TITLE

4   RESTRAINT  4-12 RESTRAINT DOCUMENTATION 1:1 OR SOFT 4-12     TITLE

5   RESTRAINT  BEHAVIOR RESTRAINT DOCUMENT 12-8     TITLE

Std Title: NURSING SECLUSION RESTRAINT NOTE

Press &lt;Enter&gt; to see more, '^' to exit this list,  OR

CHOOSE 1-5: 1  RESTRAINT PROGRESS NOTE AND EVERY TWO HOUR FLOW SHEET     TITLE

Std Title: SECLUSION RESTRAINT NOTE

The POST-SIGNATURE Code in 'RESTRAINT PROGRESS NOTE AND EVERY TWO HOUR FLOW SHEE

T' was created by this option.

It is --&gt; D EN^TIUPSCA("G.BCMA DUE LIST ERRORS","AUTOPRT","")

Do you want to change the Code? (YES or NO)? NO// YES

<!-- image -->

1. At the "Choose RECIPIENTS to receive the alert (N/I/G/T) or '^' to exit" prompt, select the recipients who will receive the alert every time this note title is used. Choosing I, G, or T enables you to define which individual(s) or group(s) will receive the alert.

N/A – Select if you do not want to specify an Individual User, Mailgroup, or Team List to receive the alert.

Individual User – A single defined person will receive the alert.

Mailgroup – An established mailgroup will receive the alert.

Team List – An established team list will receive the alert.

**Note** : Do not use mailgroup or team list names containing special characters other than parentheses "( )" or asterisks "*". Use of other special characters might result in an alert not being received by the intended recipients.

Select one of the following:

N         N/A

I         INDIVIDUAL USER

G         MAILGROUP

T         TEAM LIST (OE/RR with Queued Alert)

Choose RECIPIENTS to receive the alert (N/I/G/T) or '^' to exit: G  MAILGROUP

Select MAIL GROUP NAME: BCMA DUE LIST ERRORS

<!-- image -->

1. At the "Choose an alert ROUTINE from the above listing:" prompt, set the alert routine to run when this title is used.
    - N/A – Use when no conditional alert is needed; the alert will be sent only to the recipients designated in Step 4.**Note** : If you select N/A both here and in Step 4, then you will be provided with an option to delete the Post-Signature code associated with this title (including pre-existing code) or to cancel this code change (which retains any pre-existing code).
    - PCP – Sends the alert to the Primary Care Provider designated for each patient.
    - AUTOPRT – Use to auto-print to the printer designated as the chart copy print device at the patient's location.
        1. The “DEVICE NAME (Optional) for Paper Alert:” prompt displays if either PCP or AUTOPRT was selected in the previous step. This is an option to generate a printout containing the patient's name and the progress note title, which is useful to notify clinicians who are not at their computer when the note is entered. Pressing Enter sends the printout to a default printer.**Note** : Do not use device names containing special characters other than parentheses "( )" or asterisks "*". Use of other special characters might result in an alert not being received by the intended recipients.
    1) N/A- No Conditional Alert is needed

2) PCP- Include patient's Primary Care Provider from PCMM as a recipient

3) AUTOPRT- Generate message to chart copy printer at encounter location

Choose an alert ROUTINE from the above listing:  (1-3): 3

DEVICE NAME (Optional) for Paper Alert:
    <!-- image -->
        1. The code that will be generated based on your selections is displayed for confirmation. Type YES to accept the code. Type NO to return to the initial Create Post-Signature Alert screen—this will discard your previously entered selections.
    The Post-Signature code for 'RESTRAINT PROGRESS NOTE AND EVERY TWO HOUR FLOW SHE

ET' will be set as follows...

POST-SIGNATURE CODE: D EN^TIUPSCA("G.BCMA DUE LIST ERRORS","AUTOPRT","")

Do you want to update Post-Signature Code into 'RESTRAINT PROGRESS NOTE AND EVER

Y TWO HOUR FLOW SHEET'? NO// YES

The Post-Signature code for 'RESTRAINT PROGRESS NOTE AND EVERY TWO HOUR FLOW SHE

ET' has been updated as follows...

POST-SIGNATURE CODE: D EN^TIUPSCA("G.BCMA DUE LIST ERRORS","AUTOPRT","")
    <!-- image -->
    The progress note title with the defined parameters to create an alert is now available. When a user creates and signs a new progress note using this title, the designated recipients will receive an alert.

#### Document Definition Terminology

| ## Term          | ## Definition                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLASS            | A group of groups which may contain one or more CLASSES or DOCUMENT CLASSES. For example: Progress Notes, Discharge Summary, and History and Physical Examinations.                                                                                                                                                                                                                                                        |
| DOCUMENT CLASS   | A grouping which may contain one or more TITLES; for example: Medical Service Notes, Nursing Service Notes, Surgical Service Notes,                                                                                                                                                                                                                                                                                        |
| TITLE            | A single entity at the lowest level. For example: Endocrinology Note, OPC/Psychology, Primary Care Note, etc.                                                                                                                                                                                                                                                                                                              |
| BOILERPLATE TEXT | Template-like blocks of text that use OBJECTS and embedded text to allow quick creation of notes.                                                                                                                                                                                                                                                                                                                          |
| COMPONENT        | A reusable block of text that is predefined for a specific purpose, such as a SOAP components (Subjective, Objective, Assessment, Plan).                                                                                                                                                                                                                                                                                   |
| OBJECT           | A predefined placeholder that allows patient-specific text to be inserted into a document when a user enters a TIU document.  Objects are names representing executable M code, which may be "embedded" in the Default Text of either a component or a document, to produce an effect (e.g., the Object "Patient AGE" may be invoked to insert the value of the patient's age at an arbitrary location within a document). |

#### Matrix of Actions allowed per Status and Ownership

**User** : 	For Document Definition, IRM, Clinical Coordinators, or service managers authorized to maintain the Document Definition Hierarchy. Only programmers can create objects or edit Technical Fields.

**Owner** : Either Personal Owner or Class Owner; the person who creates or is assigned responsibility for the document type being acted on. Items under the relevant type may have separate owners (that is, A may own the Document Class, but B could own a Title under the Document Class.

**Status** : A=Active, I = Inactive, T=Test

| ## Type               | ## Status   | ## User   | ## Actions                                                                                                     | ## Limitations                                                                |
|-----------------------|-------------|-----------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Class, Document Class | A           | Any       | Edit Status, Owner  Add new items to Class  *(Class or Document Class),*  or to Document Class (  *Titles*  ). | Nat’l Standards can’t be edited.  Must own the  *items.*                      |
|                       | I           | Any       | Edit Basics and Upload Fields.                                                                                 |                                                                               |
|                       | I           | Owner     | Delete as entry from file.                                                                                     | Entry can’t be In Use.                                                        |
| Title                 | A, T        | Any       | Edit Status and the Owner.                                                                                     |                                                                               |
|                       | I           | Any       | Add items (  *components*  ).  Edit Basics and Boilerplate Text .                                              | Only owners can add non-Shared Components.  Item can’t already have a parent. |
|                       | I           | Owner     | Delete file entry.                                                                                             | If not In Use.                                                                |
| Component             | A,T         | Any       | Edit the Owner.                                                                                                |                                                                               |
|                       | I           | Any       | Add new items (  *components*  ).  Edit or delete its items.  Edit Basics and Boilerplate Text.                | Users must own items.                                                         |
|                       | I           | Owner     | Delete entry from file.                                                                                        | If not In Use.                                                                |
| **Shared Component**  | **N/A**     | **Any**   | **Add entry as an item to a Title or Component**                                                               |                                                                               |
|                       |             | Owner     | Edit Basics and Boilerplate Text                                                                               | All parents must be inactive.                                                 |
| Object                |             | Any       | Embed Object in Boilerplate Text.                                                                              |                                                                               |
|                       | I           | Any       | Edit Owner.                                                                                                    | Component or Title must be Inactive.                                          |
|                       | I           | Owner     | Edit Object Basics and Technical Fields.                                                                       | Only programmers can edit Technical Fields.                                   |

#### Creating Objects

Objects are predefined placeholders that allow patient-specific text to be inserted into a document when a user enters a TIU document.

Objects are names representing executable M code, which may be “embedded” in the Default Text of either a component or a document, to produce an effect (e.g., the Object “Patient AGE” may be invoked to insert the value of the patient’s age at an designated location within a document).

Note: 	Besides objects created by each site, there are a set of national objects supplied by the VistA developments team. Information on these is maintained on the TIU web page at REDACTED.

##### General Information

Objects must always have uppercase names, abbreviations, and print names. When embedding objects in boilerplate text, users may embed any of these three (name, abbreviation, print name) in boilerplate text, enclosed by an “|” on both sides.  Objects must always be embedded in uppercase.

Objects are stored in the Document Definition File, but are not part of the Hierarchy. They are accessible through the options *Create Objects* and *Sort Document Definitions (* by selecting Sort by Type and selecting Type Object).

TIU exports a small library of Objects. Sites can also create their own. Future versions of TIU are expected to export a much more extensive library of nationally supported objects.

Only an owner can edit an object and should do so only after consulting with others who use it. The object must be Inactive for editing. It should be thoroughly tested. (See Object Status, under Status.)

Objects must initially be written by programmers. Once defined, Objects may be used any number of times within an unlimited number of different titles.

As sites develop their own Objects, they can be shared with other sites through a mailbox entitled TIU OBJECTS in SHOP,ALL (reached via FORUM).

NOTE: 	Object routines used from SHOP,ALL are *not* supported by the Field Offices. Use at your own risk!

**See Appendix B in this manual for an example of creating an object.**

**Adding yourself as owner of a TIU-Health Summary object.**

TIU-Health Summary objects that are exchanged between sites will always import in with “NO OWNER” (field #.05-PERSONAL OWNER in file #8925.1 TIU DOCUMENT DEFINITION).  The system software cannot be made to automatically use the importing user’s name during the installation process. The TIU-HS objects will work fine in reminder dialogs, but you may find a problem with not being able to VIEW the object in the CPRS GUI Template Editor due to “no owner” being designated after installing.

When you try to select an object in the CPRS Template editor, you may get an error such as this:

<!-- image -->

To fix this, the CAC must go into the VISTA option *Sort Document Definitions* [TIUFA SORT DDEFS MGR], via the TIU Maintenance Menu/Document /Definitions Manager.

See the steps below as an example of how to add yourself as owner of a TIU-Health Summary object.

**Step 1: Go into the Document Definitions Manager menu on the TIU Maintenance Menu.**

TIU IRM MAINTENANCE MENU     TIU Maintenance Menu     menu

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

6      Active Title Cleanup Report

7      TIUHL7 Message Manager

8      Title Mapping Utilities ...

9      Text Event Edit

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13     Contingency Downtime Bookmark Progress Notes

Select TIU Maintenance Menu &lt;TEST ACCOUNT&gt; Option: **Document Definitions (Manager)**

**Step 2: Select the Create TIU/Health Summary Objects option**

--- Manager Document Definition Menu ---

1      Edit Document Definitions

2      Sort Document Definitions

3      Create Document Definitions

4      Create Objects

5      Create TIU/Health Summary Objects

6      Create Post-Signature Alerts

Select Document Definitions (Manager) &lt;TEST ACCOUNT&gt; Option: 5 **Create TIU/Health Summary Objects**

**Step 3: Select the object you’re interested in and select Detailed Display, and you’ll see that the Owner is Unknown.**

TIU Health Summary Object     Nov 28, 2012

+    TIU Object Name                   Health Summary Type

62   AUDIT-C                           V20 AUDIT-C (OBJ)

Create New TIU Object                   Find

Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object

Quit

Select Action: Next Screen// 62

TIUHS Detailed Display/Edit   Nov 28, 2012

TIU Object Name: AUDIT-C

Owner: &lt;UNKNOWN&gt; OR 0

Status: ACTIVE

HS Object: V20 AUDIT-C

HS Type: V20 AUDIT-C (OBJ)

Technical Field: S X=$$TIU^GMTSOBJ(DFN,6630809)

-----------------------------------------------------------------------------

**Step 4: Go back to the Document Definitions (Manager) option and select Sort Document Definitions. Select T as the Attribute and O as the Type. Select the name of your object at the START WITH DOCUMENT DEFINITION**

Select Document Definitions (Manager) Option: tiuf  Document Definitions (Manager)

Select Document Definitions (Manager) Option: 2  Sort Document Definitions

Select Attribute:  (T/O/S/U/P/A):  Owner// t   Type

Select TYPE: (CL/DC/TL/CO/O/N): O  OBJECT

START WITH DOCUMENT DEFINITION: FIRST// AUDIT

GO TO DOCUMENT DEFINITION: LAST// AUDITZ

**Step 5: Select Detailed Display/Edit, select the object, and then select Basics.**

Sort by TYPE                  Nov 28, 2012

Entries of Type OBJECT from AUDI to AUDIZ

Name                                                          Type

1      AUDIT-C                                                         O

2      AUDIT-C POSITIVE PAST YR                                        O

Select Action: Quit// DET   Detailed Display/Edit

Select Entry:  (1-2): 1

Detailed Display              Nov 28, 2012

Object AUDIT-C

Basics

Name:   AUDIT-C

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:   AUDIT-C

Type:   OBJECT

IFN:   3232

National

Standard:   NO

Status:   ACTIVE

Owner:   None

Technical Fields

Object Method:   S X=$$TIU^GMTSOBJ(DFN,6630809)

Select Action: Quit// **B** Basics

**Step 6: Enter the @ sign at THE CLASS OWNER prompt and enter your name at the PERSONAL OWNER prompt.** Edit Owner only: only an Owner can edit an Object.

CLASS OWNER: CLINICAL COORDINATOR// @

PERSONAL OWNER: YOURNAME     CAC-CLINICAL APPL COORDINATOR

&lt;&lt; the screen refreshes &gt;&gt;&gt;

Detailed Display            Nov 28, 2012@02:43:59          Page:    1 of    1

Object AUDIT-C

Basics

Name:   AUDIT-C

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:   AUDIT-C

Type:   OBJECT

IFN:   3232

National

Standard:   NO

Status:   ACTIVE

Owner:   YOURNAME       (You are now the owner and can preview the

object in the Template Editor)

Technical Fields

Object Method:   S X=$$TIU^GMTSOBJ(DFN,6630809)

Select Action: Quit//

#### Authorization/Subscription Utility (ASU)

The Authorization/Subscription Utility (ASU) implements a User Class Hierarchy which is useful for identifying the roles that different users play within the hospital. It also provides tools for creating business rules that apply to documents used by members of such groups. ASU provides a method for identifying who is AUTHORIZED to do something (for example, sign and order). Future versions of ASU will provide tools for identifying a group of persons who SUBSCRIBE to receive something (for example, the Medical House Staff Officer may receive an alert to cosign all Schedule II narcotic orders, etc.).

ASU originated in response to the long recognized demand for a “Scope of Practice” model, which was first discussed during the analysis and design of OE/RR. The immediate driving force behind ASU’s development was the complexity of Text Integration Utilities’ (TIU’s) document definition needs. Current security key capabilities were unable to efficiently manage the needs of clinical documentation (Discharge Summaries, Progress Notes, etc.).

##### Hierarchy Example:

<!-- image -->

##### User Class Management [USR CLASS MANAGEMENT MENU]

This is a menu of options for management of User Class Definition and Membership. See the *Authorization/Subscription Utility (ASU) Technical Manual* for information on using these options. TIU uses ASU to help manage clinical documents.

| ## Option                | ## Option Name               | ## Description                                                                                                                                                                                                                                                                     |
|--------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Class Definition    | USR CLASS DEFINITION         | This option allows review, addition, editing, and removal of User Classes.                                                                                                                                                                                                         |
| List Membership by User  | USR LIST MEMBERSHIP BY USER  | This option allows review, addition, editing, and removal of individual members to and from User Classes.                                                                                                                                                                          |
| List Membership by Class | USR LIST MEMBERSHIP BY CLASS | This option allows review, addition, editing, and removal of individual members to and from User Classes.                                                                                                                                                                          |
| Edit Business Rules      | USR EDIT BUSINESS RULES      | This option allows the user to enter Business Rules authorizing specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an UNSIGNED PROGRESS NOTE may be EDITED by a PROVIDER who is also the EXPECTED SIGNER of the note, etc.). |
| Manage Business Rule     | USR BUSINESS RULE MANAGEMENT | This option allows you to list the Business rules defined by ASU, and to add, edit, or delete them, as appropriate.                                                                                                                                                                |

##### Template Management [TIU IRM TEMPLATE MGMT]

This is a menu option that contains other options providing TIU template management functions.

Template Cleanup - When a user's access is terminated or deactivated, certain cleanup actions are desirable.  If the terminated user possessed TIU templates, a site may wish to remove them upon termination, either automatically or manually.  To allow flexibility at individual site locations, a new parameter will allow the site to specify that non-shared templates for a terminated user may be automatically removed - or the site may disable such automatic action and manually remove templates for the user.

| ## Option                                  | ## Option Name                 | ## Description                                                                                                                                                                       |
|--------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delete TIU templates for selected user.    | TIU TEMPLATE CAC USER DELETE   | Removes all templates created by a selected user. This option performs the delete at the time the option is executed.                                                                |
| Edit auto template cleanup parameter.      | TIU TEMPLATE USER DELETE PARAM | Sets a parameter indicating whether or not a template cleanup should be automatically performed at the any user is deactivated.                                                      |
| Delete templates for ALL terminated users. | TIU TEMPLATE DELETE TERM ALL   | Removes all templates created by deactivated users. This option performs the delete at the time the option is executed.                                                              |
| Set consult templates to read-only         | TIU TEMPLATE CONSULT LOCK      | Adds a template to the TIU TEMPLATE CONSULT LOCK parameter. This action will prevent any edit to the template and all associated template fields when using the CPRS Template Editor |

The first three options allow the CAC to delete non-shared templates for any individual user, to toggle automatic cleanup of non-shared templates for terminated users ON or OFF (based on Kernel's User terminate event [XU USER TERMINATE] option), and to delete all existing non-shared templates for users who have been terminated previous to the current date.

NOTE: 	The third option above traverses the TIU TEMPLATE (file# 8927) file's AROOT x-ref recursively and can take a while to complete.  Before using the option, CAC's are advised to disable TIU template editing options and assure that the process is implemented at an off-peak time.

A new OPTION named Delete user's TIU templates. [TIU TEMPLATE USER DELETE] is installed, but is used to link the call KUSER^TIUSRVT3 to Kernel's User terminate event [XU USER TERMINATE] event option, and hence the new option does not appear on any menus.

NOTE 	Users terminated with future dates are not handled by Kernel or by this patch unless the Kernel Automatic Deactivation of Users [XUAUTODEACTIVATE] option is activated and scheduled at the local site. A related issue is that users terminated from the Edit a User's Options [EDIT A USER'S OPTIONS] option rather than the Deactivate a User [XUSERDEACT] option will also require the option [XUAUTODEACTIVATE] to be activated and scheduled.  To assure reliable cleanup upon termination, sites should schedule the [XUAUTODEACTIVATE] option to run nightly, or should confirm that it is in fact already so scheduled.

A new Parameter, Y/N auto cleanup upon termination [TIU TEMPLATE USER AUTO DELETE], has been created for toggling the automatic TaskMan cleanup of non-shared templates for terminated users ON or OFF.  Editing is provided at the SYSTEM, DIVISION, and PACKAGE levels via the new Edit auto template cleanup parameter. [TIU TEMPLATE USER DELETE PARAM] menu option as described above.

The fourth option, TIU TEMPLATE CONSULT LOCK, provides a mechanism for sites to make a consult template read-only. This action prevents any edit to the template or its associated template fields when using the GUI Template Editor. Certain consult services depend on template content that should not be edited at the local facility. For example, the NON VA CARE HCPS HEMODIALYSIS and NON VA CARE HCPS PERITONEAL DIALYSIS templates should never be edited at the facility. These templates are used in HL7    transmissions to the Referral &amp; Authorization System (RAS) and those transmissions may be disrupted if the template has been edited.

When using this option, the user is prompted for the name of a TIU Template. The selected template must have already been linked to a consult service via the Template Editor. Unlinked templates are not available for selection. Adding or removing templates via this option is actually setting/removing values into the TIU TEMPLATE CONSULT LOCK parameter. These parameter values are set at the System level.

NOTE 	     The TIU TEMPLATE CONSULT LOCK parameter should only be edited via the TIU

TEMPLATE CONSULT LOCK option. Do not use the General Parameter Tools [XPAR MENU TOOLS] option as doing so will not correctly lock all associated templates and template fields for a top-level template entry.

#### Progress Notes Print Options

| ## Option                     | ## Option Name      | ## Description                                                                                                                                                                                                                                                                                    |
|-------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Author Print Progress Notes   | TIU PRINT PN AUTHOR | This option produces chart or work copies of progress notes for an author, for a selected date range.                                                                                                                                                                                             |
| Location Print Progress Notes | TIU PRINT PN LOC    | This option prints chart or work copies of progress notes for all patients who were at a specific location when the notes were written. The patients whose progress notes are printed on this report may not still be at that location. If chart is selected, each note will start on a new page. |
| Patient Print  Progress Notes | TIU PRINT PN PT     | This option prints or displays progress notes for a selected patient by selected date range.                                                                                                                                                                                                      |
| Ward Print Progress Notes     | TIU PRINT PN WARD   | This option lets you print progress notes for all patients who are now on a ward for a selected date range. This option is only forward locations.                                                                                                                                                |

| ## Option                                       |                                | ## Description                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Admission- Prints all PNs for Current Admission | TIU PRINT PN ADMISSION         | This option prints all progress notes for a selected patient for the current admission if patient is an inpatient or LAST admission if the patient has been discharged.                                                                                                                                                |
| Batch Print Outpt PNs by Division               | TIU PRINT PN BATCH INTERACTIVE | This option batch prints outpatient progress notes in terminal digit order by division. Sites can exclude Locations from this job by editing field #3 in file #8925.93. Locations not entered in file #8925.93 will be included in the batch print.                                                                    |
| Outpatient Location- Print Progress Notes       | TIU PRINT PN OUTPT LOC         | This option is designed to be used primarily by MAS.  It produces CHARTABLE notes and tracks the last note printed for the selected outpatient location.  Output is sorted in alphabetical by patient order.                                                                                                           |
| Ward- Print Progress Notes                      | TIU PRINT PN WARD              | This option will allow the printing of Progress Notes for ALL patients on the ward at the time the job is queued to print. All of the notes for a selected date range (regardless of the location of the note) will print. This option is only for WARD locations and  *only prints to printers (not to your screen).* |

*Progress Notes Print Options cont’d*

Clinical users can print progress notes, but the more complex printing is geared towards MAS and managing this function on a medical center level. The software also supports a hybrid approach.

1. LIST MANAGERUsers may print all types of documents using a variety of methods from the List Manager interface for TIU, including Forms, Progress Notes, Discharge Summaries, Consults, etc. Work and Chart copies are possible. Chart copies are the recommended type of printed copy, but many sites still want to print Work copies. For example, you may want to print WORK copies of UNSIGNED notes.

Other than the above List Manager printing, all other print options are on print menus. Only SIGNED notes are available from these options.

2. [TIU PRINT PN USER MENU]All of the options on this menu support the printing of CHART or WORK copies. Patient, Author, and Location are the current choices. TITLE sorts will be added. It should be noted that this LOCATION print is an option that will print for any location there is a signed note entered for it doesn't track anything.

**MAS Print Options**

Two files drive the CHART printing process:

TIU PRINT PARAMETERS FILE #8925.93

TIU DIVISION PRINT PARAMETERS FILE #8925.94 (supports batch printing outpatient Progress Notes)

In order to use any of the MAS print options (except ADMISSION), the location will have to be entered in one (inpatient locations) or both (outpatient locations) of the above files.

File #8925.93 TIU PRINT PRAMETERS FILE is used for the [TIU PRINT PN WARD] and [TIU PRINT PN OUTPT LOC] options. Field #1.02 tracks the last note that was printed for a selected location. This will be presented as the default PRINT FROM THIS POINT ON: YES//. The user may select another date/time to initialize.

FUN FACTS:  This field is in an interesting format. FileMan DATE/TIME ';' IEN of Note. Although it is possible to reset this using FM, it is much easier to just pick the date/time you want to go forward from.

*Progress Notes Print Options contd*

The PROGRESS NOTES DEFAULT PRINTER field brings this device up as the default for the user when queuing notes for this location. At the present time these print options are not automated to queue up without user interaction.

Field #3 EXCLUDE FROM PN BATCH PRINT is a flag designed to be used for those outpatient locations the site doesn't want to auto-print in the batch print job.

Options keyed off file #8925.93:

[TIU PRINT PN WARD]This option is usually used by the night ward clerk. The output is in RM/BED order to facilitate filing. It will print all notes after the last time they were printed. This option will print the notes for ALL current inpatients on the ward, regardless of whether the location of the note is that warda nice feature for transferred patients or patients with outpatient clinic appointment notes.

There is also an option [TIU PRINT PN ADMISSION] that will print all the patient's note for the last admission; done on discharge, to consolidate the chart.

[TIU PRINT PN OUTPT LOC]Unlike the user's LOC print, this option does track the last note printed. This option is designed for sites that have specific clinics on electronic progress notes (EPN) and don't want to batch print in the file room. The clerk can print all the notes and file them in the clinic. This would work best for mental health-type clinics where patients are seen frequently.

This option was intended to support the transition to electronic progress notesit has a specific place. Remember to turn on field #3 if you want to take this approach with a clinic. It should be noted that if a patient is seen in other clinics and those other clinics are batch-printed, the notes from the flagged clinic will also be printed in that batch. This is to preclude gaps in sequenceclinical information overlooked because it fits in between two other notes.

BATCH PRINTING OUTPATIENT PROGRESS NOTES

There are two new batch print options [TIU PRINT PN BATCH INTERACTIVE] and [TIU PRINT PN BATCH SCHEDULED]. These options are identical except the latter is set up in file 19.2 to run unaccompanied. The batch print is sorted in terminal digit order for the file room. It prints out a page of possible problems and what to check if no notes print. In theory, the MAS person would bring this to IRM to have them troubleshoot. You wouldn't want to do this every night—most test sites do it once a month. Inpatient notes *will not* print in this option. Inpatient and outpatient notes are supposed to be filed in different sections of the charts. Progress Notes V. 2.5 did not support this.

**Helpful Hints**

CHART vs. WORK copies There are certain situations when only a WORK copy is appropriate, such as when the document is not signed. The current version has an easy way of disallowing anyone other than MAS from printing progress notes. This is only feasible for those sites that are almost completely electronic. Otherwise, users will be asked if they want a WORK or a CHART copy. The WORK copy has the patient phone number on it and doesn't have a form number (a nifty little trick to keep MAS from filing them in the CHART!). The WORK copy is clearly marked as NOT FOR MEDICAL RECORD.

CONTIGUOUS vs. SEPARATE PAGESThis is where clairvoyant prowess comes into play. Users are sometimes mystified as to why they sometimes get asked the question and sometimes not. If users have selected a sort that will only produce CHART copies if the notes are on separate pages (location, title (when avail), author) there wouldn't be any point in asking them if that is how they want them. If they want WORK copies, they can only have them in CONTIGUOUS (save trees wherever possible) format. Also, if there is only one note, it wouldn't make sense to ask if they want it on a separate page.

DUPLEXing It makes sense that you would want to print notes all through the patient's admission and then print them again upon discharge, duplexing them to save paper. Actually it does make the chart thinner.

**TECHNICAL TIDBITS**

Avoid trying to change the paging of Progress Notes. Just for your information, TIUFLAG controls CHART/WORK and TIUSPG does CONTIGUOUS/ SEPARATE. These variables are sometimes hard-set and passed in by the option. Other times it's an interactive thing.

Notes are not set in the print cross-references until they are signed. ALOCP, AAUP, and APTP give all the possible sorts. Soon we will need an ATITP for the TITLE print.

In order to run all the Progress Notes printing off the same print driver, there had to be some peculiar setting of ^TMP. The first subscript TIUI contains both a '$' delimiter as well as a ';' delimiter. This gives you the print group and header in the '$' piece and the terminal digit, alpha name or room/bed in the 1st semi-colon piece and the DFN in the second semicolon piece. This allows the paging to be controlled when a hodgepodge of Forms and notes is thrown at it. It is also how you get the form number and header on the FORMS.

### Exported Routines

**Namespace:** TIU

XUPRROU (List Routines) prints a list of any or all of the TIU routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: list Routines

Routine Print

Want to start each routine on a new page: No// [ENTER]

routine(s) ?   &gt; TIU*

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each xxx subset routine.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: First Line Routine Print

PRINTS FIRST LINES

routine(s) ?   &gt;TIU*

#### TIU*1*211 TIU Data Standardization Vuid Patch

**Instructions for Mapping and Reporting**

##### TIU Clinical Document and Data Standardization Background

Data Standardization is the foundation for data sharing. Standardization ensures that data can be shared across systems and that it will retain the same meaning in each system. Standardization will enable the exchange of clinically-relevant health data between the VA and its health partners, and other federal entities such as the Department of Defense (DoD), Health &amp; Human Services (HHS), and the Indian Health Service (IHS). Standardization will also support development of an integrated, longitudinal patient record that will give providers access to the veteran’s complete health record. The result will be a safer, higher-quality and more cost-effective provision of care for veterans across all federal facilities. Standardization of data will also assist with DoD interoperability efforts by supporting a seamless transition of care for individuals moving from active-duty to veteran status.

As a result of a Congressional Mandate requiring a consolidated database of *all* veteran patient results, the VHA Office of Information and DoD were tasked with implementing a method to communicate entire patient records between the respective agencies. To accomplish this, VHA and DoD will use the standard recommended by Consolidated Health Informatics (CHI) for Clinical Document names **—** Logical Observation Identifier Names and Codes (LOINC®).

CHI is a collaborative effort to adopt health information interoperability standards, particularly health vocabulary and messaging standards, for implementation in Federal Government Systems. About 20 departments and agencies, including the DoD, HHS, and VHA, are active in the CHI governance process. The CHI initiative is one of the Office of Management and Budget’s (OMB) eGov initiatives.

**After installation of TIU*1*211, follow the steps below to complete the clinical document title mapping process.**

1. Active Title Cleanup and Direct Mapping. Follow instructions on page 99 in Method A.
2. Local Synonym Entry. Next you have the option of setting up local synonyms terms from your local titles. Follow instructions on page 107 in Method B for Local Synonym entry. Note:  This is optional and not required.
3. Automated Title Mapping. Follow instructions on page 110 in Method C for Automated Title mapping.
4. Status Report of Unmapped Titles. Submit a status report of your unmapped titles to your HDR Implementation Manager. Follow instructions on page 113 in Method D. You can locate a list of HDR Implementation managers REDACTED.
5. Mapping Support. For assistance with titles that you cannot map to a standard title send an exchange message to VHA OI HDI STS TIU TITLES.
6. New Term Rapid Turnaround (NTRT). To submit a request for a new Standard Title and/or Term follow instructions on page 114 in Method E for New Term Rapid Turnaround.

##### Method A:  Active Title Cleanup

###### Site Checklist

- Patch TIU*1*209 and TIU*1*218 TIU Active Title Cleanup Report should be installed at the site. The report and cleanup utility will analyze the TIU Document Definition File (8925.1) and provide an automated process to inactivate the appropriate TIU titles.
- From the TIU Active Title Cleanup Report print list of all local active titles from VistA Menu TIU IRM Maintenance Menu

It is important to inactivate unused titles before performing the link to Standardized Titles. Additionally, reviewing titles to determine which should be inactivated will assist you in understanding the titles at your site.

**To run the Active Title Cleanup (from TIU*1*218, TIU*1*209 is similar but less complete):**

TIU Maintenance Menu

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

6      Active Title Cleanup Report

7      TIUHL7 Message Manager

8      Title Mapping Utilities ...

9      Text Event Edit

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13     Contingency Downtime Bookmark Progress Notes

Select TIU Maintenance Menu Option: **Title** Active Title Cleanup Report

Inactivate the unused Document Titles at this time? NO// **?**

Entering 'YES' will inactivate all titles unused in the past year;

their STATUS will be changed to INACTIVE.

Entering 'NO' will create the report without making any changes.

Inactivate the unused Document Titles at this time? NO// **YES**

All active titles that have not been used in the previous 365 days

will be set to INACTIVE.

You may select individual DOCUMENT TITLES that will NOT be set

to INACTIVE by this cleanup.

Are you sure you want to change their status to INACTIVE? NO// **?**

Entering 'YES' will inactivate all titles unused in the past year;

their STATUS will be changed to INACTIVE.

Entering 'NO' will create the report without making any changes.

Are you sure you want to change their status to INACTIVE? NO// **&lt;Enter&gt;**

DEVICE: HOME// **&lt;Enter&gt;** TCP

Elapsed Time:    0 minute(s) 31 second(s)

Only appears if the count is greater than zero. Details are given at the end of the report.

<!-- image -->

# of Unused Titles  :       1319

<!-- image -->

<!-- image -->

# of Total Titles  :       1347

# of Docs  :        293

# of Docs Incorrect .01 Field  :         10 (See End of Report)

# of Docs Zero/Null .01 Field  :          2 (See End of Report)

----------

# of Total Docs Searched  :        305

Current User:  TIUUSER,SEVEN

Current Date:  Jun 01, 2006@11:41:41

Date range searched:  Jun 01, 2005 - Jun 01, 2006

# of

Document Title                          Docs  Last DT Used  Author/Dictator

--------------                          ----  ------------  ---------------

410 S PROGRESS NOTE                       15  Nov 04, 2005  TIUUSER,ONE

ADDENDUM                                  37  Mar 29, 2006  TIUUSER,ONE

ADVANCE DIRECTIVE RESCINDED                1  April 23, 2006  TIUUSER,TWO

ADVERSE REACTION/ALLERGY                  55  April 25, 2006  TIUUSER,THREE

ANDREWS TEST NOTE                          5  April 16, 2006  TIUUSER,ONE

AUDIOLOGY CONSULT RESULT                   1  Feb 23, 2006  TIUUSER,ONE

C&amp;P EXAM NOTE                              5  Oct 12, 2005  TIUUSER,FOUR

CARDIAC POST-PROCEDURE NOTE                1  Jan 10, 2006  TIUUSER,FIVE

CARE COORDINATION HOME TELEHEALTH          5  April 17, 2006  TIUUSER,ONE

EVALUATION TREATMENT PLAN

CARE COORDINATION HOME TELEHEALTH         11  Apr 24, 2006  TIUUSER,SIX

SCREENING CONSULT

CARE COORDINATION HOME TELEHEALTH          2  Mar 01, 2006  TIUUSER,SEVEN

SUBSEQUENT EVAL CNSLT 2 [Inactive]

CARE COORDINATION HOME TELEHEALTH          3  Mar 03, 2006  TIUUSER,SEVEN

SUBSEQUENT EVAL CONSULT

CARE COORDINATION HOME TELEHEALTH         21  Mar 03, 2006  TIUUSER,SEVEN

SUMMARY OF EPISODE CONSULT

CARE COORDINATION HOME TELEHEALTH          1  Nov 09, 2005  TIUUSER,EIGHT

TELEPHONE ENCOUNTER NOTE

DERMATOLOGY CONSULT RESULT [Inactive]      3  Mar 28, 2006  TIUUSER,ONE

DIABETIC INPATIENT FOLLOW UP               1  Dec 09, 2005  TIUUSER,ONE

DISCHARGE SUMMARY                         25  Mar 16, 2006  TIUUSER,ONE

GENERIC NOTE                               2  Mar 06, 2006  TIUUSER,EIGHT

IMMUNIZATION PROGRESS NOTE                10  Oct 27, 2005  TIUUSER,NINE

NURSE INTRAOPERATIVE REPORT               17  Feb 15, 2006  TIUUSER,ONE

OPERATION REPORT                          19  Feb 08, 2006  TIUUSER,TEN

PM&amp;R CONSULT RESULTS                      14  Jan 31, 2006  TIUUSER,ONE

PODIATRY CONSULT RESULT                    8  April 31, 2006  TIUUSER,ONE

PRIME CARE CLINIC                          1  Oct 11, 2005  TIUUSER,ELEVEN

PROGRESS NOTE [Inactive]                  27  April 16, 2006  TIUUSER,ONE

RESCINDED ADVANCE DIRECTIVE                1  April 23, 2006  TIUUSER,THREE

These entries are to assist IRM in correcting errors in the file.

<!-- image -->

UROLOGY CONSULT                            8  Jan 03, 2006  TIUUSER,ONE

The following IENs from File #8925.1 have an invalid #.01 Field.

<!-- image -->

<!-- image -->

The following IENs from File #8925.1 have an incorrect #.04 Field.

569   GENERIC NOTE [CLASS]

557   UROLOGY CONSULT [DOCUMENT CLASS]

The following DOCUMENT IENs have an incorrect (null or zero) #.01 Field.

4957690

4957697

Note that at the end of the report the specific IENs are given for records that the utility could not handle. Someone at your site must correct these records before running the actual inactivations.

This report should be run at least twice. Once to get an idea of which titles may be inactivated, then again to actually do the inactivations.

Note:	Numbers in this report may be different between runs—even if you run within a few minutes.

If there are titles you do not want inactivated even though they are unused, you may exclude some titles. This is an example:

Select TIU Maintenance Menu Option: **6** Active Title Cleanup Report

Inactivate the unused Document Titles at this time? NO// YES

All active titles that have not been used in previous 365 days will be

set to INACTIVE.

You may select individual DOCUMENT TITLES that will NOT be set

to INACTIVE by this cleanup.

Are you sure you want to change their status to INACTIVE? NO// **YES**

Enter the DOCUMENT TITLE(S) that will NOT be INACTIVATED

during the cleanup process.

Enter RETURN or ‘^’ to finish selections.

Enter DOCUMENT TITLE: **ADV**

1 ADVANCE DIRECTIVE     TITLE

2 ADVANCE DIRECTIVE – EDUCATION    TITLE

3 ADVANCE DIRECTIVE CONSULT REPORT       TITLE

4 ADVERSE REACTION/ALLERGY       TITLE

CHOOSE 1-4: **2** ADVANCE DIRECTIVE – EDUCATION  TITLE

And

The following DOCUMENT TITLE will NOT be INACTIVATED:

ADVANCE DIRECTIVE - EDUCATION

Is this correct? YES// **&lt;Enter&gt;**

DEVICE: HOME// &lt;Enter&gt;   TELNET TERMINAL

Elapsed Time:    0 minute(s) 9 second(s)

# of Used Titles  :         52

# of Unused Titles  :        690

----------

# of Total Titles  :        742

# of Docs  :        293

Current User:  IRMUser,One

Current Date:  Mar 30, 2006@13:55

Date range searched:  Mar 30, 2005 - Mar 30, 2006

# of

Document Title                           Docs  Last DT Used  Author/Dictator

--------------                           ----  ------------  ---------------

10-10M MEDICAL PROGRESS NOTE             0     Sep 27, 2004  CPRSProvider,Six

10-10M OP DISCHARGE INSTRUCTIONS         0     Sep 25, 2004  CPRSProvider,One

21 DAY CERTIFICATION                     0     May 21, 2002  CPRSProvider,Six   ABBREVIATED MEDICAL RECORD               0     Jun 30, 2004  CPRSProvider,Two

ABSENT SICK IN HOSPITAL/OTHER FACILITIES 0     Apr 30, 2003  CPRSProvider,Ten

ADMISSION PAIN TOOL                      0     Aug 29, 2000  CPRSProvider,Three     ADVANCE DIRECTIVE - EDUCATION            0     Sep 24, 2004  CPRSProvider,Nine

. . .

###### Site Checklist

- Print list of standard titles from TIU Communications Website link below.
    - REDACTED.
    - Select the Standards Title Tab at the bottom of the spreadsheet.
    - Print hard copy.
- Review list of your local active titles against the standard titles and determine which standard title your local title can be mapped to. You will probably only determine a portion of your titles which is fine. This will narrow down the list of your titles that have to be mapped by the mapping tool search engine.

###### Direct Mapping Note Titles

The following is an example of the Mapping Workbench using the Direct Mapping action:

1      Map ACTIVE LOCAL Titles

2      Selected Active Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Select Title Mapping Utilities Option: **3** Mapping Workbench

Select Mapping Status: unmapped (ACTIVE)// **&lt;Enter&gt;**

Searching for the events.......................

**Title Mapping Workbench** Jul 20, 2006@10:17:48        Page:   1 of   16

UNMAPPED (ACTIVE) Titles

LOCAL Title

VHA Enterprise Title                   Attempted        User Name

1    ALL BAD PUL CONSULTS                     07/07/06 18:53   TUIPROVIDER, SE

2    ANDREWS TEST NOTE                        N/A              UNKNOWN

3    ANOTHER NOTE                             N/A              UNKNOWN

4    ANTHONY TEST OBJECT                      N/A              UNKNOWN

5    AUDIT TEST NOTE                          07/07/06 18:58   TUIPROVIDER, SE

6    CARDIOLOGY-OUTPATIENT-CONSULTS           N/A              UNKNOWN

7    CHRONIC LOWER BACK PAIN                  N/A              UNKNOWN

+         + Next Screen  - Prev Screen  ?? More Actions                  &gt;&gt;&gt;

Find                      Direct Mapping            Quit

Map Title(s)              Change view

Select Action: Next Screen// **???**

Valid selections are:

FIND

Allows users to search list of Documents for a text string (word, phrase,

or partial word) from current position to the end of the list. Upon

reaching the end of the last page of the list, the user will be asked

whether to continue the search from the beginning of the list through the

origin of the search.

MAP TITLE(S)

Allows mapping of Local TIU Titles to VHA Enterprise Standard Titles using

the full features of the Mapper utility to assist in the choice.

DIRECT MAPPING

Allows users who know which VHA Enterprise Standard Title should be

associated with a given local title to map the Local Title directly,

without the assistance of the Mapper.

CHANGE VIEW

Allows modification of the current list of mapped or unmapped titles to

include either UNMAPPED, MAPPED, FAILED attempts, or ALL Active Titles for

a specified user and time range (where applicable).

QUIT

Allows user to quit the current menu level.

The following actions are also available:

Press RETURN to continue or '^' to exit:

+    Next screen          DN   Down a Line          PL   Print List

-    Previous Screen      &lt;    Shift View to Left   ADPL Auto Display(On/Off)

FS   First Screen         &gt;    Shift View to Right  CWAD CWAD Display

LS   Last Screen          GO   Go to Page

UP   Up a Line            RD   Re Display Screen

Enter RETURN to continue or '^' to exit: **&lt;Enter&gt;**

**Title Mapping Workbench** Jul 20, 2006@10:17:48        Page:    1 of  16

UNMAPPED (ACTIVE) Titles

LOCAL Title

VHA Enterprise Title                   Attempted        User Name

1    ALL BAD PUL CONSULTS                     07/07/06 18:53   TIUUSER,ONE

2    ANDREWS TEST NOTE                        N/A              UNKNOWN

3    ANOTHER NOTE                             N/A              UNKNOWN

4    ANTHONY TEST OBJECT                      N/A              UNKNOWN

5    AUDIT TEST NOTE                          07/07/06 18:58   TUIPROVIDER, SE

6    CARDIOLOGY-OUTPATIENT-CONSULTS           N/A              UNKNOWN

7    CHRONIC LOWER BACK PAIN                  N/A              UNKNOWN

+         + Next Screen  - Prev Screen  ?? More Actions                 &gt;&gt;&gt;

Find                      Direct Mapping            Quit

Map Title(s)              Change view

Select Action: Next Screen// 6

**Title Mapping Workbench** Jul 20, 2006@10:17:48        Page:    1 of  16

UNMAPPED (ACTIVE) Titles

LOCAL Title

VHA Enterprise Title                   Attempted        User Name

1    ALL BAD PUL CONSULTS                     07/07/06 18:53   TUIPROVIDER, SE

2    ANDREWS TEST NOTE                        N/A              UNKNOWN

3    ANOTHER NOTE                             N/A              UNKNOWN

4    ANTHONY TEST OBJECT                      N/A              UNKNOWN

5    AUDIT TEST NOTE                          07/07/06 18:58   TUIPROVIDER, SE

6    CARDIOLOGY-OUTPATIENT-CONSULTS           N/A              UNKNOWN

7    CHRONIC LOWER BACK PAIN                  N/A              UNKNOWN

+         + Next Screen  - Prev Screen  ?? More Actions                  &gt;&gt;&gt;

Find                      Direct Mapping            Quit

Map Title(s)              Change view

Select Action: Next Screen// **DIR** Direct Mapping

Mapping Title #6

Direct Mapping to Enterprise Standard Title...

Your LOCAL Title is: CARDIOLOGY-OUTPATIENT-CONSULTS

NOTE: Only ACTIVE Titles may be selected...

Select VHA ENTERPRISE STANDARD TITLE: CARDIOLOGY OUT

1   CARDIOLOGY OUTPATIENT CONSULT

2   CARDIOLOGY OUTPATIENT NOTE

3   CARDIOLOGY OUTPATIENT PROGRESS NOTE

CHOOSE 1-3: **1** CARDIOLOGY OUTPATIENT CONSULT

I found a match of: CARDIOLOGY OUTPATIENT CONSULT

... OK? Yes// **&lt;Enter&gt;** YES

Ready to map LOCAL Title: CARDIOLOGY-OUTPATIENT-CONSULTS to

VHA Enterprise Standard Title: CARDIOLOGY OUTPATIENT CONSULT.

... OK? Yes// **&lt;Enter&gt;** YES

Done.

Refreshing the list.

**Title Mapping Workbench** Jul 20, 2006@10:17:48       Page:    1 of   16

UNMAPPED (ACTIVE) Titles

LOCAL Title

VHA Enterprise Title                Attempted        User Name

1    ALL BAD PUL CONSULTS                  07/07/06 18:53   TUIPROVIDER, SE

2    ANDREWS TEST NOTE                     N/A              UNKNOWN

3    ANOTHER NOTE                          N/A              UNKNOWN

4    ANTHONY TEST OBJECT                   N/A              UNKNOWN

5    AUDIT TEST NOTE                       07/07/06 18:58   TUIPROVIDER, SE

6    CARDIOLOGY-OUTPATIENT-CONSULTS        07/20/06 10:18   TUIPROVIDER, SE

CARDIOLOGY OUTPATIENT CONSULT

7    CHRONIC LOWER BACK PAIN                  N/A              UNKNOWN

+         + Next Screen  - Prev Screen  ?? More Actions                 &gt;&gt;&gt;

Find                      Direct Mapping            Quit

Map Title(s)              Change view

Select Action: Quit// **&lt;Enter&gt;** Quit

##### Method B: Add/Edit Local Synonyms

The matching program uses a file of synonyms to aid it in determining potential matches of local titles to national titles. In many cases a site will have terms in their titles that describe situations that occur only at that site. To accommodate this a file of local synonyms can be created. An example of this is when colors were assigned to general clinics. These colors are different at every site, so they cannot be included in the file of national synonyms, but if you put them into the local synonym file the mapping utility will run faster and smoother. Another example is NSG for nursing. Many sites use this abbreviation for Nursing, but it is not found in the national synonym file.

The spreadsheet of national terms is posted on the TIU web site at REDACTED. If you compare the terms in the Synonym List with terms you commonly use at your site and update the local synonym list accordingly, title matching will go much faster.

**Example of Add/Edit Synonyms:**

1      Map ACTIVE LOCAL Titles

2      Selected Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Select Title Mapping Utilities Option: **ADD/Edit Synonyms**

1      Subject Matter Domain Synonyms

2      Role Synonyms

3      Setting Synonyms

4      Service Synonyms

5      Document Type Synonyms

Select Add/Edit Synonyms Option: **1** Subject Matter Domain Synonyms

Please Enter SMD Synonym: **EKG** CLINICAL CARDIAC ELECTROPHYSIOLOGY

SYNONYM: EKG//

SUBJECT MATTER DOMAIN: CLINICAL CARDIAC ELECTROPHYSIOLOGY

//

Please Enter SMD Synonym: **EEG**

Are you adding 'EEG' as a new TIU LOINC SMD SYNONYMS (the 898TH)? No// **Y**

(Yes)

TIU LOINC SMD SYNONYMS SUBJECT MATTER DOMAIN: **NEURO**

1   NEUROLOGICAL SURGERY

2   NEUROLOGY

3   NEUROLOGY NEURODEVELOPMENTAL DISABILITIES

4   NEUROLOGY WITH SPECIAL QUALIFICATIONS IN CHILD NEUROLOGY

5   NEUROTOLOGY

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **2** NEUROLOGY

SYNONYM: EEG// **&lt;Enter&gt;**

SUBJECT MATTER DOMAIN: NEUROLOGY// **&lt;Enter&gt;**

Please Enter SMD Synonym: &lt;Enter&gt;

1      Subject Matter Domain Synonyms

2      Role Synonyms

3      Setting Synonyms

4      Service Synonyms

5      Document Type Synonyms

Select Add/Edit Synonyms Option: **&lt;Enter&gt;**

1      Map ACTIVE LOCAL Titles

2      Selected Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Select Title Mapping Utilities Option: **&lt;Enter&gt;**

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

6      Active Title Cleanup Report

7      TIUHL7 Message Manager

8      Title Mapping Utilities ...

9      Text Event Edit

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13     Contingency Downtime Bookmark Progress Notes

Select TIU Maintenance Menu Option:

##### Method C: Automated Mapping of Titles

To assist sites with *automated* mapping of TIU Clinical Document Titles, Standards and Terminology Services (STS) is providing a set of instructions to assist you. This document outlines the *automated* mapping process of mapping one local clinical document title to a standard title. This document is intended to assist Clinical Applications Coordinators (CACs), Health Information Managers (HIMS) and Implementation Managers.

**Example of Map Active Local Titles:**

Select OPTION NAME: **TIU IRM MAIN** TENANCE MENU     TIU Maintenance Menu

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

6      Active Title Cleanup Report

7      TIUHL7 Message Manager

8      Title Mapping Utilities ...

9      Text Event Edit

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13     Contingency Downtime Bookmark Progress Notes

Select TIU Maintenance Menu Option: Title Mapping Utilities

1      Map ACTIVE LOCAL Titles

2      Selected Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Select Title Mapping Utilities Option: **1** Map ACTIVE LOCAL Titles

****************************************************************

*                   Good EVENING CHARLIE!                      *

*       And WELCOME BACK for ANOTHER ride on the MTA!!!        *

*                                                              *

*       So far, 44 of 63 Active Titles have been mapped!       *

*             You're at Brigham Circle Station...            *

*                                                              *

*  In preparation for migration to the HDR, ALL LOCAL titles   *

* MUST be mapped to Standard Titles BEFORE transmittal of TIU  *

*               Documents to the HDR can begin.              *

*                                                              *

*  You may quit mapping titles at any time, and continue your  *

*    work from the last successfully mapped title. The only    *

*  catch is that any ACTIVE LOCAL Titles that are not mapped   *

*      when transmission to the HDR is initiated will be       *

* INACTIVATED, so please finish this process expeditiously... *

****************************************************************

... Are you READY to map? NO// **Y** ES

For the LOCAL Title: NUTRITION ECU QUARTERLY

Attempting to map NUTRITION ECU QUARTERLY

to a VHA Enterprise Standard Title...

Is "NUTRITION" a Subject Matter Domain?  DIETETICS

I found a match of: NUTRITION DIETETICS

... OK? Yes// **&lt;Enter&gt;** YES

Is "ECU" a LOINC Role? No.

Is "ECU" a SYNONYM for a LOINC Role? No.

Is "QUARTERLY" a LOINC Role? No.

Is "QUARTERLY" a SYNONYM for a LOINC Role? No.

Is "ECU" a Setting? No.

Is "ECU" a SYNONYM for a Setting? No.

Is "QUARTERLY" a Setting? No.

Is "QUARTERLY" a SYNONYM for a Setting? No.

Is "ECU" a Service? No.

Is "ECU" a SYNONYM for a Service? No.

Enter RETURN to continue or '^' to exit:

Remember, your LOCAL title is: NUTRITION ECU QUARTERLY

Is "QUARTERLY" a Service? No.

Is "QUARTERLY" a SYNONYM for a Service? No.

Is "ECU" a Document Type? No.

Is "ECU" a SYNONYM for a Document Type? No.

Is "QUARTERLY" a Document Type? No.

Is "QUARTERLY" a SYNONYM for a Document Type? No.

Now, we'll query the VHA Enterprise Standard Titles for an entry with:

LOCAL Title: NUTRITION ECU QUARTERLY

Subject Matter Domain: NUTRITION DIETETICS

First, we'll try an EXCLUSIVE match (i.e., ALL conditions met):

1   NUTRITION DIETETICS ADMINISTRATIVE NOTE

2   NUTRITION DIETETICS CONSULT

3   NUTRITION DIETETICS DIAGNOSTIC INTERVENTION PROCEDURE REPORT

4   NUTRITION DIETETICS DISCHARGE NOTE

5   NUTRITION DIETETICS E &amp; M CONSULT

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5:

6   NUTRITION DIETETICS E &amp; M NOTE

7   NUTRITION DIETETICS EDUCATION CONSULT

8   NUTRITION DIETETICS EDUCATION NOTE

9   NUTRITION DIETETICS EDUCATION REPORT

10  NUTRITION DIETETICS GROUP COUNSELING NOTE

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-10: 6  NUTRITION DIETETICS E &amp; M NOTE

I found a match of: NUTRITION DIETETICS E &amp; M NOTE

... OK? Yes// **&lt;Enter&gt;** YES

Ready to map LOCAL Title: NUTRITION ECU QUARTERLY to

VHA Enterprise Standard Title: NUTRITION DIETETICS E &amp; M NOTE.

... OK? Yes// **&lt;Enter&gt;** YES

Done.

For the LOCAL Title: NUTRITION FOLLOWUP NOTE

**Example of Selected Title Map:**

Enter RETURN to continue or '^' to exit: **^**

1      Map ACTIVE LOCAL Titles

2      Selected Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Select Title Mapping Utilities Option: **2** Selected Title Map

Select TITLE: **MEDICAL SERV**

1   MEDICAL SERVICE CONSULT       TITLE

2   MEDICAL SERVICE DERMATOLOGY PROGRESS NOTE       TITLE

3   MEDICAL SERVICE ECU - AIMS       TITLE

4   MEDICAL SERVICE ENDOSCOPY       TITLE

5   MEDICAL SERVICE INPATIENT PROGRESS NOTE       TITLE

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **4** MEDICAL SERVICE ENDOSCOPY     TITLE

For the LOCAL Title: MEDICAL SERVICE ENDOSCOPY

Attempting to map MEDICAL SERVICE ENDOSCOPY

to a VHA Enterprise Standard Title...

Is "MEDICAL" a Subject Matter Domain?

1   MEDICAL GENETICS

2   MEDICAL TOXICOLOGY

3   MEDICAL  PH.D. MEDICAL GENETICS

CHOOSE 1-3: **&lt;Enter&gt;** No.

Is "MEDICAL" a SYNONYM for a Subject Matter Domain?  SERVICE       INTERNAL MEDI

CINE

I found a match of: MEDICAL SERVICE

Subject Matter Domain: INTERNAL MEDICINE

... OK? Yes// **&lt;Enter&gt;** YES

Enter RETURN to continue or '^' to exit: &lt;Enter&gt;

Remember, your LOCAL title is: MEDICAL SERVICE ENDOSCOPY

Is "SERVICE" a LOINC Role? No.

Is "SERVICE" a SYNONYM for a LOINC Role? No.

Is "ENDOSCOPY" a LOINC Role? No.

Is "ENDOSCOPY" a SYNONYM for a LOINC Role? No.

Is "SERVICE" a Setting? No.

Is "SERVICE" a SYNONYM for a Setting? No.

Is "ENDOSCOPY" a Setting? No.

Is "ENDOSCOPY" a SYNONYM for a Setting? No.

Is "SERVICE" a Service? No.

Is "SERVICE" a SYNONYM for a Service? No.

Is "ENDOSCOPY" a Service? No.

Is "ENDOSCOPY" a SYNONYM for a Service?     DIAGNOSTIC INTERVENTIONAL PROCEDURE

I found a match of: ENDOSCOPY

Service: DIAGNOSTIC INTERVENTIONAL PROCEDURE

... OK? Yes// **&lt;Enter&gt;** YES

Enter RETURN to continue or '^' to exit: **&lt;Enter&gt;**

Remember, your LOCAL title is: MEDICAL SERVICE ENDOSCOPY

Is "SERVICE" a Document Type? No.

Is "SERVICE" a SYNONYM for a Document Type? No.

Now, we'll query the VHA Enterprise Standard Titles for an entry with:

LOCAL Title: MEDICAL SERVICE ENDOSCOPY

Subject Matter Domain: INTERNAL MEDICINE

Service: DIAGNOSTIC INTERVENTIONAL PROCEDURE

First, we'll try an EXCLUSIVE match (i.e., ALL conditions met): DIAGNOSTIC INTER

VENTION PROCEDURE NOTE

I found a match of: INTERNAL MEDICINE DIAGNOSTIC INTERVENTION PROCEDURE NOTE

... OK? Yes// **&lt;Enter&gt;** YES

Ready to map LOCAL Title: MEDICAL SERVICE ENDOSCOPY to

VHA Enterprise Standard Title: INTERNAL MEDICINE DIAGNOSTIC INTERVENTION PROCEDU

RE NOTE.

... OK? Yes// **&lt;Enter&gt;** YES

Done.

##### Method D:  Status Report of your Unmapped Titles.

In this example we create a report of all unmapped active titles at our medical center. Then we send the report to ourselves via email. To print the report we use the hidden action PL (for Print List). When we are prompted for a device, we send it to the mail server:

**Example of getting a report of Unmapped Titles:**

Select Title Mapping Utilities Option: **&lt;Enter&gt;**

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

6      Active Title Cleanup Report

7      TIUHL7 Message Manager

8      Title Mapping Utilities ...

9      Text Event Edit

10     Unauthorized Abbreviations (Enter/Edit)

11     List Unauthorized Abbreviations

13     Contingency Downtime Bookmark Progress Notes

Select TIU Maintenance Menu Option: **Title** Title Mapping Utilities

1      Map ACTIVE LOCAL Titles

2      Selected Active Title Map

3      Mapping Workbench

4      Add/Edit Synonyms ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Title Mapping Utilities Menu Option: **3**

Select Mapping Status: unmapped (ACTIVE)// **&lt;Enter&gt;**

. . .

Title Mapping Workbench       Sep 22, 2006@13:26:46        Page:    1 of   9

UNMAPPED (ACTIVE) Titles

LOCAL Title

VHA Enterprise Title                   Attempted        User Name

1    10-10M NURSING AMBULATORY CARE           N/A              UNKNOWN

2    10-10M OP DISCHARGE INSTRUCTIONS         N/A              UNKNOWN

3    21 DAY CERTIFICATION                     N/A              UNKNOWN

4    ADDENDUM                                 N/A              UNKNOWN

5    ADVANCE DIRECTIVE                        N/A              UNKNOWN

6    AMBULATORY CARE EMPLOYEE HEALTH NOTE     N/A              UNKNOWN

7    AMBULATORY CARE PATIENT TRANSFER         N/A              UNKNOWN

+         + Next Screen  - Prev Screen  ?? More Actions                 &gt;&gt;&gt;

Find                      Direct Mapping            Quit

Map Title(s)              Change view

Select Action: Next Screen// PL   PL

DEVICE: HOME// P-M  P-MESSAGE-HFS  HFS FILE =&gt; MESSAGE

Subject: CHEYENNE UNMAPPED TITLES

Select one of the following:

M         Me

P         Postmaster

From whom: Me//

Send mail to: ENTER YOUR HDR IMPLEMENTATION MANAGER EMAIL ADDRESS HERE

##### Method E:  New Term Rapid Turnaround (NTRT) Process

**Using the NTRT Website for Clinical Documents**

When you find that you need a new Enterprise Standard Title or Title Term in order to effectively map your local titles, you can request what you need from the NTRT website. Requesting new titles and title terms is a simple process, and there is plenty of help and support should you run into any difficulty along the way. The following steps will guide you through the process of submitting a new request, and will help to familiarize you with the website at the same time. Screen shots have been added for additional visual reference.

1. Go to the NTRT VistA Web Portal at REDACTED.
<!-- image -->
2. Click on the *Access the New Term Rapid Turnaround (NTRT) Request Website* link to access the NTRT Login page.
3. Log in with your Login Name and Password.
<!-- image -->
4. Click on the *Clinical Doc Title* link in the left-side navigation bar to Request a new Clinical Document Title.
<!-- image -->
5. Before entering the information for a new Clinical Document Title, click on the HELP button to see explanations about the Clinical Document information model and additional information about using the web site. Close the window when convenient.

1. Now you can see how you would go about entering a request for a new title. Each Document Axis is represented here by a select control that contains every currently approved term for that axis. The default value for each is UNASSIGNED, which is the appropriate value for a title that does not contain a term from that axis. At the very bottom of each list is additionally an entry that starts with, “Add new,” that causes a new text box to appear in which you can enter a request for a new axis term. Shown here is an example of the Service select control.
<!-- image -->
2. When you have selected the axis terms that comprise your title, you can click the Submit button and see a summary for the title you just entered. Note that each of the axes is optional with the exception of the Document Type, which is required for every request. Also note that while Comments are not required, they do help the reviewers of your requests to better understand your intentions in making the request. Not every request will be approved, and some may be modified so as to better fit into the Enterprise Standard. But you will be kept informed of each step along the way.
<!-- image -->
3. Click on the *Printer Friendly Version* link to see the report formatted for printing. Close the window when convenient.
4. Now click on the *Search* link in the left-side navigation bar to Search for requested titles.
5. In the Select control labeled, “Domain,” choose Clinical Doc Title.
<!-- image -->
6. Click “Search.” Note the error message that appears because the radio button, “Tracking Number,” was selected but no Tracking Number was entered. Search can be accomplished by either selecting a specific Tracking Number or by selecting the radio button, “Show All.” Be aware additionally that if you enter a Tracking Number, it must belong to the specific domain in which you are searching, or you will get no results.
7. Select the “Show All” radio button and click “Search.” Observe the results returned by the search and take a moment to note the additional search parameters. You can display any request status that you like, and can sort the results as you like.
<!-- image -->
8. Note the Tracking Numbers for the two titles you entered. Click on one to review its summary report.
9. Click the *&lt;&lt;Back* link to return to the search page.
10. Now copy one of the Tracking Numbers into the Tracking Number text box and select its radio button. Search again.
11. You can observe any changes by of a request’s Status by checking the “Show History” checkbox when searching.

The information about the changes being made by NTRT can be viewed on the NTRT Web site, under “NTRT Deployment Log.”   Those interested can also join the NTRT listserv which provides the same information as the NTRT Deployment log that is automatically sent to the recipients. Join by going to REDACTED and clicking the link in the middle of the screen called "NTRT Notification Listserv."  This listserv is specific to NTRT deployments and only generates one message per week.

An Automated Notification Report (ANR) is sent out through the National Help Desk by e-mail messages that alert sites/recipients about the changes that are being made and the times the weekly NTRT deployment is deployed to sites. If you are not currently receiving ANR messages and would like to in the future, please submit a Remedy ticket to be added to VHA OI Software Announcement and you can be added to the distribution list for future information. The ANR list is not specific to NTRT deployments and you will also receive e-mails for many other purposes (sometimes as many as 20 per day).

### Menu and Option Assignment

TIU menus and options are not exported on a single big menu, but as smaller menus directed at categories of users. These are described in earlier sections of this manual and also depicted below. Sites may rearrange these as needed.

Recommended assignments are also listed on the following pages. Since many sites may wish to create a Clinical Coordinator’s Menu, we have included an example of a possible one.

Text Integration Utilities (Transcriptionist) (TIU MAIN MENU TRANSCRIPTION)

|

----1 Enter/Edit Discharge Summary [TIU ENTER/EDIT DS]

----2 Enter/Edit Document [TIU ENTER/EDIT TRANSCRIBER]

----3 Upload Menu [TIU UPLOAD MENU]

|

|--------1 Upload Documents [TIU UPLOAD DOCUMENTS]

|

|--------2 Help for Upload Utility [TIU UPLOAD HELP]

----4 List Documents for Transcription [TIU REVIEW UNTRANSCRIBED DOCS]

----5 Review/Edit Documents [TIU BROWSE DOC TRANSCRIPTION]

----6 Transcription Billing Verification Report [TIU VBC LINE COUNT REPORT]

Text Integration Utilities (MRT) (TIU MAIN MENU MRT)

|

----1 Individual Patient Document [TIU BROWSE DOCUMENT MRT]

----2 Multiple Patient Documents [TIU REVIEW SCREEN MRT]

----3 Review Upload Filing Events [TIU REVIEW FILING EVENTS]

----4 Print Document Menu [TIUP PRINT MENU]

|

|--------1 Discharge Summary Print [TIUP PRINT DISCHARGE SUMMARIES]

|

|--------2 Progress Note Print [TIUP PRINT PROGRESS NOTES]

|

|--------3 Clinical Document Print [TIUP PRINT DOCUMENTS]

-----5 Released/Unverified Report [TIU RELEASED/UNVERIFIED REPORT]

-----6 Search for Selected Documents [TIU SEARCH LIST MRT]

-----7 Unsigned/Uncosigned Report [TIU UNSIGNED/UNCOSIGNED REPORT]

-----8 Reassignment Document Report  [TIU REASSIGNMENT REPORT]

-----9 Review unsigned additional signatures [TIU REVIEW MRT ADD SGNR

Progress Notes/Discharge Summary [TIU] (TIU MAIN MENU CLINICIAN)

|

----1 Progress Notes ---------1 Entry of Progress Note [TIU ENTER/EDIT PN]

User Menu [TIU

MAIN MENU PN

CLINICIAN]

|

|-------------------2 Review Progress Notes by Patient [TIU BROWSE PN

|                                               CLINICIAN]

|

|-------------------2B Review Progress Notes [TIU OE/RR REVIEW PROG NOTES]

|

|-------------------3 All MY UNSIGNED Progress Notes [TIU REVIEW PN

|                                               UNSIGNED]

|

|-------------------4 Show Progress Notes Across Patients [TIU REVIEW PN

|                                               CLINICIAN]

|

|-------------------5 Progress Notes ------PNPA Author- Print

|                     Print Options             Progress Notes

|                     [TIU PRINT PN             [TIU PRINT PN

|                     USER MENU]                AUTHOR]

|                         |

|                         |----------------PNPL Location- Print

|                         |                     Progress Notes

|                         |                     [TIU PRINT PN

|                         |                     LOC]

|                         |

|                         |----------------PNPT Patient- Print

|                         |                     Progress Notes

|                         |                     [TIU PRINT PN PT]

|                         |

|                         |----------------PNPW Ward- Print

|                                               Progress Notes

|                                               [TIU PRINT PN WARD]

|

|--------------------6 List Notes By Title [TIU LIST NOTES BY TITLE]

|

|--------------------7 Search by Patient AND Title [TIU SEARCH BY

|                                               PATIENT/TITLE]

|

|------------------- 8 Personal ---------------1 Personal

|                      Preferences [TIU          Preferences [TIU

|                      PERSONAL                  PERSONAL

|                      PREFERENCE MENU]          PREFERENCES]

|                         |

|                         |-------------------2 Document List

|                                               Management [TIU

|                                               PREFERRED

|                                               DOCUMENT LIST]

|

|------------------- 9 ALL Documents requiring my Additional

Signature [TIU REVIEW UNSIGNED ADDSIG]

----2 Discharge Summary------- 1 Individual Patient Discharge Summary

|     User Menu [TIU MAIN        [TIU BROWSE DS CLINICIAN]

|     MENU DS CLINICIAN]

|                              2 All MY UNSIGNED Discharge Summaries

|                                [TIU REVIEW DS UNSIGNED]

|

|                              3 Multiple Patient Discharge Summaries

|                                [TIU REVIEW DS CLINICIAN]

|

----3 Integrated Document----- 1 Individual Patient Document

|     Management [TIU MAIN       [TIU BROWSE DOCUMENT CLINICIAN]

|     MENU MIXED CLINICIAN]

|                              2 All MY UNSIGNED Documents [TIU REVIEW UNSIGNED]

|

|                              3 All MY UNDICTATED Documents

|                                [TIU REVIEW UNDICTATED DOCS]

|

|                              4 Multiple Patient Documents

|                                [TIU REVIEW SCREEN CLINICIAN]

|

|                              5 Enter/edit Document [TIU ENTER/EDIT]

|

|                              6  ALL Documents requiring my Additional Signature

|                                 [TIU REVIEW UNSIGNED ADDSIG]

|

----4 Personal Preferences---- 1 Personal Preferences [TIU PERSONAL PREFERENCES]

[TIU PERSONAL

PREFERENCE MENU]         2 Document List Management

[TIU PREFERRED DOCUMENT LIST

Text Integration Utilities (MIS Manager) (TIU MAIN MENU MGR)

|

|

----1 Individual Patient Document [TIU BROWSE DOCUMENT MGR]

----2 Multiple Patient Documents [TIU REVIEW SCREEN MIS MANAGER]

----3 Print Document Menu [TIUP ------------1 Discharge Summary Print [TIUP

PRINT MENU]                             PRINT DISCHARGE SUMMARIES]

|---------------------------------2 Progress Note Print [TIUP

|                                   PRINT PROGRESS NOTES]

|---------------------------------3 Clinical Document Print [TIUP

PRINT DOCUMENTS]

----4 Search for Selected Documents [TIU SEARCH LIST MGR]

----5 Statistical Reports [TIU ------------TR TRANSCRIPTIONIST Line Count

STATISTICAL REPORTS]                    Statistics [TIU DS LINE COUNT

|                                   BY TRANSCR]

|--------------------------------AU AUTHOR Line Count Statistics

|                                   [TIU DS LINE COUNT BY AUTHOR]

|-------------------------------SVC SERVICE Line Count Statistics

[TIU DS LINE COUNT BY SERVICE]

----6 Unsigned/Uncosigned Report [TIU UNSIGNED/UNCOSIGNED REPORT]

----7 Missing Text Report [TIU MISSING TEXT NODE]

----8 Missing Text Cleanup [TIU MISSING TEXT CLEAN]

----9 UNKNOWN Addenda Cleanup [TIU UNK ADDENDA MENU]

----10 Signed/unsigned PN report and update [TIU SIGNED/UNSIGNED PN]

----11 Missing Expected Cosigner Report [TIU MISSING EXPECTED COSIGNER]

----12 Mark Document as 'Signed by Surrogate' [TIU MARK SIGNED BY SURROGATE]

----13 Mismatched ID Notes [TIU MISMATCHED ID NOTES]

----14 TIU 215 ANALYSIS ... [TIU 215 ANALYSIS]

----15 Transcription Billing Verification Report [TIU VBC LINE COUNT REPORT]

----16 Copy/Paste Tracking Report Export [TIU COPY/PASTE REPORT]

----17 CWAD/Postings Auto-Demotion Setup [TIU SET UP CWAD/POSTINGS FOR AUTO DEMOTION

Text Integration Utilities (Remote User) (TIU MAIN MENU REMOTE USER)

|

|

----1 Individual Patient Document [TIU BROWSE DOCUMENT READ ONLY]

----2 Multiple Patient Documents [TIU REVIEW SCREEN READ ONLY

Progress Notes Print Options (TIU PRINT PN)

|

|

---PT Patient- Print Progress Notes [TIU PRINT PN PT]

----- Author- Print Progress Notes [TIU PRINT PN AUTHOR]

----- Location- Print Progress Notes [TIU PRINT PN LOC

MAS Progress Notes Print Options (TIU PRINT PN MAS MENU)

|

|

----- Admission- Prints all PNs for Current Admission [TIU PRINT PN ADMISSION]

----- Batch Print Outpt PNs by Division [TIU PRINT PN BATCH INTERACTIVE]

----- Outpatient Location- Print Progress Notes [TIU PRINT PN OUTPT LOC]

----- Ward- Print Progress Notes [TIU PRINT PN WARD

Document Definitions (Clinician) (TIUF DOCUMENT DEFINITION CLIN)

|

|

----1 Edit Document Definitions [TIUFH EDIT DDEFS CLIN]

----2 Sort Document Definitions [TIUFA SORT DDEFS CLIN]

----3 View Objects [TIUFJ VIEW OBJECTS CLIN]

TIU Conversions Menu (TIU CONVERSIONS MENU)

|

|

----1 Convert Discharge Summaries (*** BE CERTAIN ***) [TIU DISCHARGE SUMMARY CONVERT]

|

|-------CV Run/Restart DS Conversion (*** BE CERTAIN ***)[TIU DISCHARGE

|                                             SUMMARY CONVERT]

|-------SG Single Discharge Summary Conversion [TIU GMRD CONVERT SINGLE]

----2 Progress Note Conversion [TIU GMRPN CONVERSION]

|

|-------CV Convert Progress Notes [TIU GMRPN CONVERT]

|

|-------PM Monitor Progress Note Conversion [TIU GMRPN MONITOR]

|

|-------HC Halt Progress Note Conversion [TIU GMRPN HALT]

|

|-------RS Restart Progress Note Conversion [TIU GMRPN RESTART]

|

|-------SG Single Progress Note Conversion [TIU GMRPN SINGLE]

|

|-------FC Final Pass Progress Notes Conversion [TIU GMRPN FINAL]

-----3 Initialize Membership of User Classes [USR INITIALIZE MEMBERSHIP

TIU Maintenance Menu (TIU IRM MAINTENANCE MENU)

|

|

----1 TIU Parameters Menu [TIU -------------1 Basic TIU Parameters [TIU

SET-UP MENU]                            BASIC PARAMETER EDIT]

|

|---------------------------------2 Modify Upload Parameters [TIU

|                                   UPLOAD PARAMETER EDIT]

|

|---------------------------------3 Document Parameter Edit [TIU

|                                   DOCUMENT PARAMETER EDIT]

|

|---------------------------------4 Progress Notes Batch Print

|                                   Locations [TIU PRINT PN LOC

|                                   PARAMS]

|

|---------------------------------5 Division - Progress Notes

Print Params [TIU PRINT PN DIV

PARAMS]

----2 Document Definitions (Manager) -------1 Edit Document Definitions

[TIUF DOCUMENT DEFINITION MGR]          [TIUFH EDIT DDEFS MGR]

|

|---------------------------------2 Sort Document

|                                   Definitions/Objects [TIUFA

|                                   SORT DDEFS MGR]

|

|---------------------------------3 Create Document Definitions

|                                   [TIUFC CREATE DDEFS MGR]

|

|---------------------------------4  Create Objects

|                                    [TIUFA CREATE OBJECTS]

|

|---------------------------------5  Create TIU/Health Summary Objects

[TIUHS LIST MANAGER]

|---------------------------------6 Create Post-Signature Alerts

|                                   [TIUFPC CREATE POST-SIGNATURE]

----3 User Class Management [USR -----------1 User Class Definition [USR

CLASS MANAGEMENT MENU]                  CLASS DEFINITION]

|

|---------------------------------2 List Membership by User [USR

|                                   LIST MEMBERSHIP BY USER]

|

|---------------------------------3 List Membership by Class [USR

|                                   LIST MEMBERSHIP BY CLASS]

|

|---------------------------------5 Manage Business Rules [USR

BUSINESS RULE MANAGEMENT]

----4 TIU Template Management Functions ----1 Delete TIU templates for selected user.

[TIU IRM TEMPLATE MGMT]                 [TIU TEMPLATE CAC USER DELETE]

|

|---------------------------------2 Edit auto template cleanup parameter.

|                                   [TIU TEMPLATE USER DELETE PARAM]

|

|---------------------------------3 Delete templates for ALL terminated

|                                   users. [TIU TEMPLATE DELETE TERM ALL]

|---------------------------------4 Set consult templates to read-

|                                   only. [TIU TEMPLATE CONSULT LOCK]

----5   TIU Alert Tools [TIU ALERT TOOLS]

----6   Active Title Cleanup Report [TIU ACTIVE TITLE CLEANUP]

----7   TIUHL7 Message Manager

----8      Title Mapping Utilities ...

----9      Text Event Edit

----10     Unauthorized Abbreviations (Enter/Edit)

----11     List Unauthorized Abbreviations

----13     Contingency Downtime Bookmark Progress Notes

#### Suggested Clinical Coordinator Menu

TIU doesn’t export a Clinical Coordinator Menu. However, sites may wish to create one that includes most of the other menus and options, except possibly the IRM options that require programmer access, depending on the Coordinator’s knowledge of M and FileMan.

Text Integration Utilities (Transcriptionist) ...

Text Integration Utilities (MRT) ...

Progress Notes(s)/Discharge Summary [TIU] ...

Text Integration Utilities (MIS Manager) ...

Text Integration Utilities (Remote User) ...

Progress Notes Print Options ...

Document Definitions (Clinician) ...

1    Edit Document Definitions

2    Sort Document Definitions/Objects

TIU Parameters Menu...

User Class Management ...

The Document Definitions (Clinician) menu could be assigned (with due caution, of course) to Clinicians who are particularly interested in setting up personal Titles with boilerplate text, or who want to edit boilerplate text.

#### Menu Assignment

We recommend assignment of TIU menus and options as described below:

| ## Option                                     | ## Option Name                        | ## Description                                                                                                                                                                            | ## Assign to:                                                      |
|-----------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Text Integration Utilities (Transcriptionist) | TIU MAIN MENU  TRANSCRIPTION          | Main Text Integration Utilities menu for transcriptionists.                                                                                                                               | Transcrip-tionists                                                 |
| Text Integration Utilities (MRT)              | TIU MAIN MENU MRT                     | Main Text Integration Utilities menu for Medical Records Technicians.                                                                                                                     | Medical Records Technicians.                                       |
| Text Integration Utilities (MIS Manager)      | TIU MAIN MENU MGR                     | Main Text Integration Utilities menu for MIS Managers.                                                                                                                                    | MIS Managers.                                                      |
| Progress Notes/ Discharge Summary [TIU]       | TIU MAIN MENU CLINICIAN               | Main Text Integration Utilities menu for Clinicians.                                                                                                                                      | Clinicians                                                         |
| Progress Notes User Menu                      | TIU MAIN MENU PN CLINICIAN            | Main Progress Notes menu, for staff who primarily use Progress Notes and don’t use Discharge Summary or other clinical documents that might be accessed through TIU.                      | Clinicians, nurses, psychologists, social workers, etc.            |
| Text Integration Utilities (Remote User)      | TIU MAIN MENU REMOTE                  | This option allows remote users (e.g., VBA RO personnel) to access only those documents which have been completed ), to facilitate processing of claims on a need-to-know basis.          | VBA RO personnel, etc.                                             |
| Progress Notes Print Options                  | TIU PRINT PN USER MENU                | Menu for printing Progress Notes.                                                                                                                                                         | ADPACs,  Managers, clinicians                                      |
| MAS Progress Notes Print Options              | TIU PRINT PN MAS MENU                 | Menu for printing Progress Notes by individual or by batch for specified locations.                                                                                                       | MAS personnel                                                      |
| Document Definition  (Clinician)              | TIU DOCUMENT DEFINITION CLIN          | Document Definition menu for Clinicians. Lets you view any entry, and edit an entry if you own it. In particular, lets you enter/edit boilerplate text for an entry you own.              | Clinical Coordinators,  Selected Clinicians                        |
| TIU Maintenance Menu                          | TIU MAINTENANCE MENU                  | Options on this menu allow IRM Staff to set/modify the various parameters controlling the behavior of the Text Integration Utilities Package, as well as the definition of TIU documents. | IRM; some of the options to some Clinical Coordinators             |
| TIU Conversions Menu                          | TIU CONVERSIONS MENU                  | A menu of options for running Progress Notes and Discharge Summary conversions to TIU                                                                                                     | IRM                                                                |
| TIU MIS Managers Menu                         | TIU CWAD/POSTINGS AUTO-DEMOTION SETUP | This option on the menu allows Clinical Application Coordinators and/or site designated personnel to configure CWAD notes for auto demotion using the CWAD/Postings Auto-Demotion Setup.  | Clinical Application Coordinators and/or site designated personnel |

#### Actions/Functions Across Applications

KEY: NA: Not Available

Menus:

DDEF: Document Definitions menu

IRM: Maintenance menu

MAS: MAS Progress Note Print Options menu

MD: Progress Note/Discharge Summary menu

MGR: MIS Manager menu

MRT: MRT menu

PRINT: Progress Notes Print Options menu

REM: Remote User menu

TR: Transcriptionist menu

Options:

AMUD: All MY UNSIGNED Documents

AMUDS: All MY UNSIGNED Discharge Summaries

EED: Enter/Edit Document

EEDS: Enter/Edit Discharge Summary

EPN: Entry of Progress Note

IPD: Individual Patient Document

IPDS: Individual Patient Discharge Summary

LNT: List Notes by Title

MPD: Multiple Patient Documents

MPDS: Multiple Patient Discharge Summaries

RPN: Review Progress Notes

RPNP:  Review Progress Notes by Patient

SPNAP: Show Progress Notes Across Patients

SPT: Search by Patient and Title

SSD: Search for Selected Documents

| ## ACTION/FUNCTION                                                                                                                                | ## TIU LMGR                                                                                                                                                                                                                                                                                                                                                                                                                     | ## OE/RR LMGR                                                                                                                                                                                                                                                                                                 | ## CPRS GUI V15.10                                                                                                                                                                                                                      |                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add to Signature List                                                                                                                             | Options (can exit note without signing, and sign via another action or alert):  TR: EED, EEDS  MD: EED, MPD, MPDS, EPN, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                       | Can exit note without signing, and sign via another action or alert:  Clinician  Nurse  Ward Clerk                                                                                                                                                                                                            | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Amend                                                                                                                                             | Options:  MGR: IPD, MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                                    | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      |                                                                                                                                                                                           |
| Browse                                                                                                                                            | Options:  MRT: MPD, SSD  REM: MPD  MGR: MPD, SSD  MD: MPD, MPDS, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                              | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs:  Basically, the pane is  “browsing”                                                                                                                                                                          |                                                                                                                                                                                           |
| Change Ordering Info  (can change patient location, requesting clinician)                                                                         | Can change hospital location with Edit action (same thing?)                                                                                                                                                                                                                                                                                                                                                                     | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | All tabs: File Menu: Update Provider/Location                                                                                                                                                                                           |                                                                                                                                                                                           |
| Change Title                                                                                                                                      | Options:  MRT: IPD, MPD, SSD  REM: IPD  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                              | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes & D/C Summ tabs: Action Menu: Edit Progress Note                                                                                                                                                                                  |                                                                                                                                                                                           |
| Change View  (can change by: status, clinical document types, start/end dates, and  *italicized*  by search category also)                        | Options:  MRT: MPD, SSD  REM: MPD  MGR: IPD, MPD, SSD  MD: MPD, MPDS, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                              | See: Select Search &amp; Check for my unsigned  Also: Notes, Consults, D/C Summ chart contents                                                                                                                                                                                                                | See: Select Search &amp; Check for my unsigned  Also: Notes, Consults, D/C Summ tabs                                                                                                                                                    |                                                                                                                                                                                           |
| Check for my unsigned                                                                                                                             | Options:  MD: AMUD, AMUDS, AMUPN                                                                                                                                                                                                                                                                                                                                                                                                | Change View: my unsigned, my uncosigned  Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                         | Notes tab: View Menu: unsigned notes, uncosigned notes  See Select Search  Can also view only signed list in pane                                                                                                                       |                                                                                                                                                                                           |
| Check grammar/spelling                                                                                                                            | XTENSIBLE editor (PF4-S)                                                                                                                                                                                                                                                                                                                                                                                                        | XTENSIBLE editor (PF4-S)                                                                                                                                                                                                                                                                                      | Notes & D/C Summ tabs: Pop-up Menu                                                                                                                                                                                                      |                                                                                                                                                                                           |
| Complete Note(s) (Sign/Edit/Delete)                                                                                                               | Options:  MD: RPN                                                                                                                                                                                                                                                                                                                                                                                                               | Can sign/edit/delete with:  Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                      | Can sign/edit/delete with a number of options                                                                                                                                                                                           |                                                                                                                                                                                           |
| Copy  (note to another note)                                                                                                                      | Options:  MRT: IPD, MPD, SSD  MGR: MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                  | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | NA                                                                                                                                                                                                                                      |                                                                                                                                                                                           |
| CWAD                                                                                                                                              | Options:  MRT: IPD, MPD, SSD  REM: IPD, MPD  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                         | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | All tabs: Postings CWAD button                                                                                                                                                                                                          |                                                                                                                                                                                           |
| Delete                                                                                                                                            | Options:  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, AMUD                                                                                                                                                                                                                                                                                                                                           | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Detailed Display                                                                                                                                  | Options:  MRT: IPD, MPD, SSD  REM: IPD, MPD  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                         | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes & D/C Summ tabs: View Menu: Details                                                                                                                                                                                               |                                                                                                                                                                                           |
| Document Definitions                                                                                                                              | Options:  DDEF: Create/edit/sort, Create objects  IRM: Create/edit/sort, Create objects                                                                                                                                                                                                                                                                                                                                         | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      |                                                                                                                                                                                           |
| Edit                                                                                                                                              | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                             | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs: Action &amp; Pop-up menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Encounter Edit                                                                                                                                    | Options:  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, AMUD                                                                                                                                                                                                                                                                                                                                                               | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Encounter Drawer                                                                                                                                                                                                                        |                                                                                                                                                                                           |
| ACTION/FUNCTION                                                                                                                                   | TIU LMGR                                                                                                                                                                                                                                                                                                                                                                                                                        | OE/RR LMGR                                                                                                                                                                                                                                                                                                    | CPRS GUI V15.10                                                                                                                                                                                                                         | CPRS GUI V15.10                                                                                                                                                                           |
| Expand/Collapse Entry                                                                                                                             | Options:  MRT: MPD, SSD  MGR: MPD, SSD  MD: MPD, MPDS, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                        | NA                                                                                                                                                                                                                                                                                                            | Notes & D/C Summ tabs: Pop-up Menu (expand all, expand selected, collapse all, collapse selected)                                                                                                                                       | Notes & D/C Summ tabs: Pop-up Menu (expand all, expand selected, collapse all, collapse selected)                                                                                         |
| Find                                                                                                                                              | Options:  MRT: IPD, MPD, SSD  REM: IPD, MPD  MGR: IPD, MPD, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                         | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes & D/C Summ tabs: Pop-up Menu                                                                                                                                                                                                      | Notes & D/C Summ tabs: Pop-up Menu                                                                                                                                                        |
| Identify Signers / Identify Additional Signers                                                                                                    | Options:  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, AMUD                                                                                                                                                                                                                                                                                                                                                               | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Interdisciplinary Note                                                                                                                            | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD  MD: IPD, MPD, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                    | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes tab: Action &amp; Pop-up Menus: Add New Entry to Interdisciplinary Note, Detach from Interdisciplinary Note                                                                                                                       |                                                                                                                                                                                           |
| Link  (Problem(s), Patient/Visit, with Request)  See also: Reassign (for Patient/Visit Link)                                                      | Options:  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                                     | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | See Link with Request                                                                                                                                                                                                                   |                                                                                                                                                                                           |
| Link with Request                                                                                                                                 | Options (also see Link):  MRT: MPD, SSD  MGR: MPD, SSD                                                                                                                                                                                                                                                                                                                                                                          | See: Link                                                                                                                                                                                                                                                                                                     | Consults tab: Action Menu: Consult Results: Complete/Update Results                                                                                                                                                                     | Consults tab: Action Menu: Consult Results: Complete/Update Results                                                                                                                       |
| Make Addendum                                                                                                                                     | Options:  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                                | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| New Note / New Document / Add Document / Write New Note / New Discharge Summary                                                                   | Options:  TR: EED, EEDS  MD: EED, MPD, MPDS, EPN, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                             | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes  &amp; D/C Summ tabs: Action Menu  New Note Drawer                                                                                                                                                                                |                                                                                                                                                                                           |
| On Chart                                                                                                                                          | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Parameters                                                                                                                                        | Options:  IRM: Basic, Upload, Document Parameter, Batch Print Locations, Division Print Params                                                                                                                                                                                                                                                                                                                                  | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Personal Preferences                                                                                                                              | Options:  MD: Personal Preferences  Document List Management (document list and default document)  Personal Preferences (DEFAULT LOCATION, REVIEW SCREEN SORT FIELD, REVIEW SCREEN SORT ORDER, DISPLAY MENUS,  PATIENT SELECTION PREFERENCE, ASK 'Save changes?' AFTER EDIT, ASK SUBJECT FOR PROGRESS NOTES, NUMBER OF NOTES ON REV SCREEN,  SUPPRESS REVIEW NOTES PROMPT, DEFAULT COSIGNER, DAY OF WEEK for HOSPITAL LOCATION) | Clinician  Nurse  Ward Clerk  GUI Parameters – General (Auto-Save Interval, Verify Default Title)  Tab Default Chart Preferences (Notes tab: Begin Date, End Date, Status, Author, Occurrence Limit, Show/Hide Subject)  Tab Default Chart Preferences (D/C Summ tab: Begin Date,  End Date, Status,  Author) | All tabs: Tools Menu: Options (document list, default document, autosave, default cosigner, ask subject, verify note title)                                                                                                             | All tabs: Tools Menu: Options (document list, default document, autosave, default cosigner, ask subject, verify note title)                                                               |
| Print Copy/Print  (single patient)                                                                                                                | Options:  MRT: IPD, MPD, Discharge Summary, Progress Note, Clinical Document, SSD  REM: IPD, MPD  MAS: Admission  MGR: IPD, MPD, Discharge Summary, Progress Note, Clinical Document, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                               | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | All tabs: File Menu                                                                                                                                                                                                                     | All tabs: File Menu                                                                                                                                                                       |
| Personal Preferences                                                                                                                              | Options:  MD: Personal Preferences  Document List Management (document list and default document)  Personal Preferences (DEFAULT LOCATION, REVIEW SCREEN SORT FIELD, REVIEW SCREEN SORT ORDER, DISPLAY MENUS,  PATIENT SELECTION PREFERENCE, ASK 'Save changes?' AFTER EDIT, ASK SUBJECT FOR PROGRESS NOTES, NUMBER OF NOTES ON REV SCREEN,  SUPPRESS REVIEW NOTES PROMPT, DEFAULT COSIGNER, DAY OF WEEK for HOSPITAL LOCATION) | Clinician  Nurse  Ward Clerk  GUI Parameters – General (Auto-Save Interval, Verify Default Title)  Tab Default Chart Preferences (Notes tab: Begin Date, End Date, Status, Author, Occurrence Limit, Show/Hide Subject)  Tab Default Chart Preferences (D/C Summ tab: Begin Date,  End Date, Status,  Author) | All tabs: Tools Menu: Options (document list, default document, autosave, default cosigner, ask subject, verify note title)                                                                                                             | All tabs: Tools Menu: Options (document list, default document, autosave, default cosigner, ask subject, verify note title)                                                               |
| Print Copy/Print  (single patient)                                                                                                                | Options:  MRT: IPD, MPD, Discharge Summary, Progress Note, Clinical Document, SSD  REM: IPD, MPD  MAS: Admission  MGR: IPD, MPD, Discharge Summary, Progress Note, Clinical Document, SSD  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                               | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | All tabs: File Menu                                                                                                                                                                                                                     | All tabs: File Menu                                                                                                                                                                       |
| Print  (multiple patients)                                                                                                                        | Options:  PRINT: Author, Location, Patient, Ward  MAS: Batch Print, Outpatient Location, Ward  MD: Author, Location, Patient, Ward                                                                                                                                                                                                                                                                                              | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Print List                                                                                                                                        | Options:  MRT: MPD, SSD  MGR: MPD, SSD  MD: MPD, MPDS, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                        | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Reassign                                                                                                                                          | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Released/Unverified Report                                                                                                                        | Option:  MRT: Released/Unverified Report                                                                                                                                                                                                                                                                                                                                                                                        | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Reload Boilerplate Text                                                                                                                           | NA                                                                                                                                                                                                                                                                                                                                                                                                                              | NA                                                                                                                                                                                                                                                                                                            | Notes & D/C Summ tabs: Action Menu: Edit Progress Note                                                                                                                                                                                  | Notes & D/C Summ tabs: Action Menu: Edit Progress Note                                                                                                                                    |
| Reset to All Signed                                                                                                                               | Options (see Select Search also):  MD: RPN                                                                                                                                                                                                                                                                                                                                                                                      | See Select Search                                                                                                                                                                                                                                                                                             | See Select Search  Can also view only signed list in pane                                                                                                                                                                               |                                                                                                                                                                                           |
| Save without Signature                                                                                                                            | Options (not a specified action):  TR: EED, EEDS  MD: EED, MPD, MPDS, EPN, RPN, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                    | Can exit note without signing, and sign via another action or alert:  Clinician  Nurse  Ward Clerk                                                                                                                                                                                                            | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Search List  (See also: Find)                                                                                                                     | NA                                                                                                                                                                                                                                                                                                                                                                                                                              | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Select New Patient                                                                                                                                | Options:  MD: RPN                                                                                                                                                                                                                                                                                                                                                                                                               | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | All tabs: File Menu                                                                                                                                                                                                                     | All tabs: File Menu                                                                                                                                                                       |
| Select Search / Change View  (signed notes/summaries (all), signed notes/summaries /author, signed notes/summaries /dates)  see also: Change View | Select Search Options: (in addition, has: unsigned notes, uncosigned notes)  MD: RPN                                                                                                                                                                                                                                                                                                                                            | Change View: (in addition, has: my unsigned, my uncosigned, Show/Hide Subject, Save as Preferred View, Remove Preferred View):  Clinician  Nurse  Ward Clerk                                                                                                                                                  | Notes & D/C Summ tabs: View & Pop-up Menus: (in addition, has: Unsigned Notes/Summaries (my), Uncosigned Notes/Summaries (my), Custom View, Save as Default View, Return to Default View)                                               | Notes & D/C Summ tabs: View & Pop-up Menus: (in addition, has: Unsigned Notes/Summaries (my), Uncosigned Notes/Summaries (my), Custom View, Save as Default View, Return to Default View) |
| Send Back                                                                                                                                         | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Show Reassignment History                                                                                                                         | Options:  MGR: MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                                         | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Sign/Cosign / Sign Note Now                                                                                                                       | Options:  MD: IPD, MPD, IPDS, MPDS, EPN, RPNP, AMUPN, SPNAP, LNT, SPT, AMUD                                                                                                                                                                                                                                                                                                                                                     | Clinician  Nurse  Ward Clerk                                                                                                                                                                                                                                                                                  | Notes &amp; D/C Summ tabs: Action &amp; Pop-up Menus                                                                                                                                                                                    |                                                                                                                                                                                           |
| Statistical Reports                                                                                                                               | Options:  MGR: Transcriptionist, Service, Author Line Counts                                                                                                                                                                                                                                                                                                                                                                    | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Templates (user)                                                                                                                                  | NA                                                                                                                                                                                                                                                                                                                                                                                                                              | NA                                                                                                                                                                                                                                                                                                            | Notes &amp; D/C Summ tabs: Options Menu: Edit Templates, Create New Template, Edit Shared Templates, Create New Shared Template, Edit Template Fields  Notes &amp; D/C Summ tabs: Pop-up Menu: Copy into New Template  Templates Drawer |                                                                                                                                                                                           |
| Templates (mgr)                                                                                                                                   | Options:  IRM: Delete for selected user, Delete for all terminated users, Edit parameter                                                                                                                                                                                                                                                                                                                                        | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Upload (misc.)                                                                                                                                    | Options:  TR: Upload Documents, Help for Upload Utility  MRT: Review Upload Filing Events                                                                                                                                                                                                                                                                                                                                       | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| User Class Membership                                                                                                                             | Options:  IRM: Definition, List by User, List by Class, Manage Business Rules                                                                                                                                                                                                                                                                                                                                                   | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |
| Verify/Unverify                                                                                                                                   | Options:  MRT: IPD, MPD, SSD  MGR: IPD, MPD, SSD                                                                                                                                                                                                                                                                                                                                                                                | NA                                                                                                                                                                                                                                                                                                            | NA                                                                                                                                                                                                                                      | NA                                                                                                                                                                                        |

### TIU File Descriptions

|   ## File # | ## File Name                      | ## Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     8925    | TIU DOCUMENT                      | This file stores textual information for the clinical record database. It is designed to initially accommodate Progress Notes, Consult Reports, and Discharge Summaries, and now also supports Surgery. The file intended to be sufficiently flexible to accommodate textual reports or provider narrative of any length or type, and to potentially accommodate such data transmitted from remote sites, which may be excluded from the corresponding local  **V**  *IST*  **A**  Package databases (e.g., Radiology Reports, Pathology Reports, etc.) to avoid confusion with local workload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     8925.1  | TIU DOCUMENT DEFINITION           | This file stores Document Definitions, which identify and define behavior for documents stored in the TIU DOCUMENTS FILE (#8925). For consistency with the V-file schema, it may be viewed as the "Attribute Dictionary" for the Text Integration Utilities.  It also stores Objects, which can be embedded in a Document Definition's Boilerplate Text (Overprint). Objects contain M code which gets a piece of data and inserts it in the document's Boilerplate Text when a document is entered.  Some entries in this file are developed Nationally and exported across the country.  Others are created by local sites. Entries in the first category are marked National Standard and are not editable by sites.  This file does  *not*  allow multiple entries  *of the same type*  with the same name. That is, within a given Type, there are no duplicate names. (This refers to the .01 field, the Technical name of the entry.)  This file does not allow a parent to have items with the same name, even if the items have different internal file numbers (i.e. are different file entries). Again, this refers to the .01 Technical name of the entry.  Because of ownership considerations, the file does  *not*  allow an entry to be an item under more than 1 parent. If the same item is desired under more than one parent, the item must be copied into a new entry. There is one exception: Document Definitions of Type Component that have been marked Shared may have more than one parent. |
|     8925.1  | TIU DOCUMENT DEFINITION cont’d    | Users are expected to use the Document Definition Utility TIUF to enter, edit, and delete file entries. In fact, the file prohibits the deletion of entries through generic FileMan Options. It also prohibits the edit through generic FileMan of a few critical fields: Type, Status, Shared, and National Standard. Adding and Deleting (but not editing) Items is also prohibited through generic FileMan options.  This does NOT imply that it is  *safe*  to use generic Fileman to edit other fields.  Users are cautioned that edit through generic Fileman bypasses many safeguards built in to the Document Definition Utility and can create havoc unless the user  *thoroughly understands*  the File and its uses. If users find needs which are not met through TIUF, please communicate them to the TIU development team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     8925.2  | TIU UPLOAD BUFFER                 | This file buffers uploaded ASCII reports during the upload process, until they can be successfully routed to their respective destinations within  **V**  *IST*  **A**  . It will support the development of tools for responding to error messages (e.g., the correction of errors experienced during routing/filing) by the appropriate users, so as to avoid the necessity of making all edits on the client system and re-initiating the upload in response to an error condition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     8925.3  | TIU UPLOAD ERROR DEFINITION       | This file defines allowable error codes, and their corresponding names and textual messages for the error handler module of the ASCII upload process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     8925.4  | TIU UPLOAD LOG                    | This file is used by the filer module of the upload process to log both successfully filed records and non-fatal errors which may occur during routing/ filing of one or more records in a given batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     8925.5  | TIU AUDIT TRAIL                   | This file maintains an audit trail of TIU transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     8925.6  | TIU STATUS  (including data)      | This file contains the allowable statuses which may be applied to a TIU document during its path through the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     8925.7  | TIU MULTIPLE SIGNATURE            | This file is intended to accommodate the case where multiple cosignatures are applied to a document (e.g., team or multidisciplinary notes, discharge planning check-lists, etc.). Rather than adding a multiple to the TIU Document file, this file supports a 3NF decomposition, allowing multiple cosignatures to be applied to the same document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     8925.71 | TIU TEXT EVENTS                   | This file was introduced with Patch TIU*1*296 (see overview on page 5), and is used to define the words or phrase that will be searched for in a TIU document. If the words or phrase are found in the TIU document, then an alert is sent to the team(s) specified in this file.  A new Text Event Edit [TIU TEXT EVENT EDIT] menu option was added to the TIU Maintenance Menu [TIU IRM MAINTENANCE MENU]. Use this option to set up a text event in the TIU TEXT EVENTS file.  Any TIU document that is to be used to trigger these text alerts must have the MUMPS code ‘D TASK^TIUTIUS($S($G(DAORIG):DAORIG,1:DA))’ entered in the POST-SIGNATURE CODE field (#4.9) in the TIU DOCUMENT DEFINITION file (#8925.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     8925.8  | TIU SEARCH CATEGORIES             | This file stores parameters which modify the processing requirements of individual document types, and their descendants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     8925.9  | TIU PROBLEM LINK                  | This file allows a many-to-many relationship between TIU Documents and Problems to be maintained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     8925.91 | TIU EXTERNAL DATA LINK FILE       | This file is intended to allow the definition of many-to-one linkages between TIU Documents and external data objects (i.e., non-MUMPS data) such as Images or BLOBs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     8925.93 | TIU PRINT PARAMETERS              | This file describes the parameters for controlling the Printing of Progress Notes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     8925.94 | TIU DIVISION PRINT PARAMETERS     | This file describes the parameters for the batch printing of progress notes for filing by Medical Center Division.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     8925.95 | TIU DOCUMENT PARAMETERS           | This file stores parameters which modify the processing requirements of individual document types, and their descendants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     8925.97 | TIU CONVERSIONS                   | This file contains information concerning the conversion of legacy files such as ^GMR(121, Generic Progress Note File, to ^TIU(8925, TIU Document File.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     8925.98 | TIU PERSONAL DOCUMENT TYPE LIST   | This file is used to store "pick-lists" of documents (by class), for selection by users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     8925.99 | TIU PARAMETERS                    | This file contains the site-configurable parameters for TIU. It will have one entry for each division, to support variable definition of package behavior at multidivisional facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     8926    | TIU PERSONAL PREFERENCES          | This file allows the definition of Personal Preferences with respect to a variety of TIU's functions (e.g., Review Screen sort field and order, Default cosigner, default locations, location by day-of-week, suppression of review notes prompt on Progress note entry, etc.).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     8926.1  | TIU VHA ENTERPRISE STANDARD TITLE | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the VHA Enterprise Standard Document Title Ontology, a multi-axial coding scheme, based on LOINC, which will support migration of TIU Documents to the Health Data Repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     8926.2  | TIU LOINC SUBJECT MATTER DOMAIN   | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the Subject Matter Domain Axis of the VHA Enterprise Standard Document Title Ontology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     8926.3  | TIU LOINC ROLE                    | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the Role Axis of the VHA Enterprise Standard Document Title Ontology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     8926.4  | TIU LOINC SETTING                 | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the Setting Axis of the VHA Enterprise Standard Document Title Ontology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     8926.5  | TIU LOINC SERVICE                 | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the Service Axis of the VHA Enterprise Standard Document Title Ontology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     8926.6  | TIU LOINC DOCUMENT TYPE           | Per VHA Directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to the VHA Directive's 2005-044 effective date shall not be supported.  This file supports the instantiation, within VistA, of the Document Type Axis of the VHA Enterprise Standard Document Title Ontology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     8926.72 | TIU LOINC SMD SYNONYMS            | This file supports and facilitates the mapping of local titles to LOINC Standard Titles, by simplifying the correct association between partial names and the LOINC Standard Subject Matter Domains. Unlike the TIU LOINC SUBJECT MATTER DOMAIN File (#8926.2), this file may be locally extended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     8926.73 | TIU LOINC ROLE SYNONYMS           | This file supports and facilitates the mapping of local titles to LOINC Standard Titles, by simplifying the correct association between partial names and the LOINC Standard Roles. Unlike the TIU LOINC ROLE File (#8926.3), this file may be locally extended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     8926.74 | TIU LOINC SETTING SYNONYMS        | This file supports and facilitates the mapping of local titles to LOINC Standard Titles, by simplifying the correct association between partial names and the LOINC Standard Settings. Unlike the TIU LOINC SETTING File (#8926.4), this file may be locally extended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     8926.75 | TIU LOINC SERVICE SYNONYMS        | This file supports and facilitates the mapping of local titles to LOINC Standard Titles, by simplifying the correct association between partial names and the LOINC Standard Services. Unlike the TIU LOINC SERVICE File (#8926.5), this file may be locally extended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     8926.76 | TIU LOINC DOCUMENT TYPE SYNONYMS  | This file supports and facilitates the mapping of local titles to LOINC Standard Titles, by simplifying the correct association between partial names and the LOINC Standard Document Types. Unlike the TIU LOINC DOCUMENT TYPE File (#8926.6), this file may be locally extended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     8927    | TIU TEMPLATE                      | This file stores TIU templates, which are on-the-fly boilerplates that can be added to any not eor addendum in the CPRS GUI.  All shared and personal templates, as well as the template hierarchy, are stored within this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     8927.1  | TIU TEMPLATE FIELD FILE           | Contains advanced template objects such as Edit Boxes and Radio Buttons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Cross-References

The following cross-references are included in this package (listed here by file and field number).

#### TIU DOCUMENT File (#8925)

| ## Field #   |                               | ## Field Name                 | ## X-ref                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ## Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------|-------------------------------|-------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | .01                           | DOCUMENT TYPE                 | B  APT  AAU  ASUP  AV  ATS  ATC  ALL                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Regular cross-reference  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/ DICTATION DATE facilitates look-ups by patient.  This MUMPS-type, multi-field cross-reference by AUTHOR, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE facilitates look-ups by author.  This multi-field, MUMPS-type cross-reference by (EXPECTED COSIGNER), DOCUMENT TYPE, STATUS, INVERSE ENTRY/DICTATION DATE/TIME is used for look-ups and queries.  This MUMPS-type cross-reference by patient, document type, and visit number will allow for a candidate key to determine whether a given document exists for a particular patient visit.  This multi-field, MUMPS-type cross-reference by DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/TIME facilitates look-ups by treating specialty.  This multi-field, MUMPS-type cross-reference by TRANSCRIPTIONIST ID, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/TIME will facilitate look-ups by transcriptionist.  This multi-field cross-reference is used for building the review screen across all categories (Author, Attending Physician, Patient, Transcriptionist, or treating specialty).                                                                                                                                                                                                                                                                                                                                                                              |
| Field #      | Field Name                    | Field Name                    | X-ref                                                                                   | X-ref                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .01          | DOCUMENT TYPE                 | DOCUMENT TYPE                 | ASUB  ASVC  AE  ALOC  APRB  AVSIT  APTCL  ACLPT  ACLAU  ACLEC                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This MUMPS-style multi-field cross-reference is used for queries by subject.  This MUMPS-type, multi-field cross-reference by SERVICE, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE facilitates look-ups by service.  This multi-field, MUMPS-type cross-reference by Patient, inverse Date, and Report Type is to optimize searching by entity, time, and attribute.  This MUMPS-type, multi-field cross-reference is optimized for searching hospital location, document type, status, and date range.  This multi-field, MUMPS-type cross-reference by Problem, Document Type, Status, and Inverse Reference Date  facilitates query for documents by problem.  This MUMPS-type, multi-field cross-reference by VISIT, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE facilitates look-ups by visit.  This MUMPS-type, multi-field cross-reference by  PATIENT, CLINICAL DOCUMENT CLASS, and INVERSE  REFERENCE DATE facilitates look-ups by patient.  This multi-field, MUMPS-type cross-reference on CLASS, PATIENT, INVERSE REFERENCE DATE/TIME, and RECORD # is designed to support rapid queries by patient.  This multi-field, MUMPS-type cross-reference on CLASS, AUTHOR (or ENTERED BY), PATIENT, INVERSE  REFERENCE DATE/TIME, and RECORD # is designed  to facilitate rapid access to the current users  unsigned notes about a patient.  This multi-field, MUMPS-type Cross-reference on CLASS, EXPECTED COSIGNER, PATIENT, INVERSE  REFERENCE DATE/TIME, and RECORD # is useful for  finding the uncosigned notes by the current user for a given patient. |
| Field #      | Field Name                    | Field Name                    | X-ref                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .01          | DOCUMENT TYPE                 | DOCUMENT TYPE                 | ACLSB  APTLD                                                                            | This cross-reference by CLASS, SIGNED BY, PATIENT, INVERSE REFERENCE DATE/TIME, and RECORD # will facilitate finding records signed by a given user about the current patient.  This MUMPS type Multi-field index by  PT,TITLE,"LOC;VDT;VTYP",DA is used for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .02          | PATIENT                       | PATIENT                       | AA  APT  AE  C  AV  APTP  ADCPT                                                         | This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, STATUS, and INVERSE VISIT/DATE will help to identify documents by patient and time.  This multi-field, MUMPS-type cross-reference by Patient, Document Type, Status, and Inverse Entry/Dictation Date will facilitate look-up by Patient.  This multi-field, MUMPS-type cross-reference by Patient, Inverse Visit Date, and Report Type is to optimize searching by entity, time, and attribute.  This REGULAR FileMan type cross-reference is used for look-up by patient.  This MUMPS-type, multi-field cross-reference by patient, document type, and visit record number will serve as a candidate key to determine whether a given document exists for a particular patient visit.  This MUMPS-type, multi-field cross-reference by Patient and REGULAR Signature Date/Time is used to maintain the daily print queue for batch printing of documents (currently, just Progress Notes) on signature.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT CLASS, STATUS, and INVERSE REFERENCE DATE facilitates look-ups by PATIENT and DOCUMENT CLASS (e.g., all SIGNED Violence Postings for patient CPRSPATIENT,ONE)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Field #      | Field Name                    | Field Name                    | X-ref                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .02          | PATIENT                       | PATIENT                       | APTCL  2270  ACLAU  ACLSB  APTLD                                                        | This MUMPS-type, multi-field cross-reference by PATIENT, CLINICAL DOCUMENT CLASS, and INVERSE REFERENCE DATE facilitates look-ups by patient.  This x-ref is used to extract lists based on context.  This x-ref is used to extract lists based on context.  This x-ref is used to extract lists based on context.  This MUMPS-type Multi-field index by PT, TITLE, “LOC;VDT;VTYP” is used for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .03          | VISIT                         | VISIT                         | AA  AE  AV  AVSIT  V  APTLD                                                             | This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, and INVERSE VISIT DATE is optimized for searches by entity, attribute, and time.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, and INVERSE VISIT DATE will optimize searching by entity, attribute, and time.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, and Visit Record number serves as a candidate key to determine whether a given document exists for a particular patient visit.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, STATUS, and INVERSE VISIT/DICTATION DATE facilitates look-ups by visit.  This REGULAR FileMan Cross-reference by VISIT is used to help identify dependent entries.  This MUMPS-type Multifield cross-reference by PT, TITLE, “LOC;VDT;VTYP”,DA is used for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .04          | PARENT DOCUMENT TYPE          | PARENT DOCUMENT TYPE          | ADCPT                                                                                   | This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT CLASS, STATUS, and INVERSE REFERENCE DATE facilitates look-ups by PATIENT AND DOCUMENT CLASS (e.g., all SIGNED Violence Postings for patient CPRSPATIENT,ONE).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT CLASS, STATUS, and INVERSE REFERENCE DATE facilitates look-ups by PATIENT AND DOCUMENT CLASS (e.g., all SIGNED Violence Postings for patient CPRSPATIENT,ONE).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .05          | STATUS                        | STATUS                        | ASUP  AAU  APT  ATC  ATS  ALL  ASUB  ASVC                                               | This MUMPS-type, multi-field cross-reference by (EXPECTED COSIGNER), DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference by AUTHOR/DICTATOR, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference by AUTHOR/DICTATOR, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference by ENTERED BY DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference by TREATING SPECIALTY, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference by DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.  This MUMPS-type, multi-field cross-reference is used in queries by subject.  This MUMPS-type, multi-field cross-reference by SERVICE, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .05          | STATUS                        | STATUS                        | ALOC  APRB  AVSIT  ADCPT                                                                | This MUMPS-type, multi-field cross-reference is optimized for searching hospital location, document type, status, and date range.  This MUMPS-type, multi-field cross-reference by PROBLEM, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME facilitates queries by problem.  This MUMPS-type, multi-field cross-reference by SERVICE, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME facilitates queries by visit.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME facilitates look-ups by PATIENT and DOCUMENT CLASS (e.g., all SIGNED violence Postings for patient CPRSPATIENT,ONE).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .06          | PARENT                        | PARENT                        | DAD                                                                                     | Cross-Reference on parent to help find addenda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Cross-Reference on parent to help find addenda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .07          | EPISODE BEGIN DATE/TIME       | EPISODE BEGIN DATE/TIME       | APTLD                                                                                   | This MUMPS-type Multifield cross-reference by PT, TITLE, “LOC;VDT;VTYP”,DA is used for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This MUMPS-type Multifield cross-reference by PT, TITLE, “LOC;VDT;VTYP”,DA is used for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .12          | MARK DISCH DT FOR CORRECT-ION | MARK DISCH DT FOR CORRECT-ION | FIX                                                                                     | This regular FileMan Cross-reference is used by the nightly daemon to identify those records which require evaluation/correction of their discharge dates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This regular FileMan Cross-reference is used by the nightly daemon to identify those records which require evaluation/correction of their discharge dates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .13          | VISIT TYPE                    | VISIT TYPE                    | APTLD                                                                                   | This MUMPS type Multi-field index by PT,TITLE,"LOC;VDT;VTYP",DA is used  for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | This MUMPS type Multi-field index by PT,TITLE,"LOC;VDT;VTYP",DA is used  for optimizing checks for documents for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 1201         | ENTRY DATE/TIME               | ENTRY DATE/TIME               | F  VBC                                                                                  | This regular FileMan Cross-reference on Entry Date/time supports the Nightly background task, by helping to identify the subset of records which is overdue for either signature or purging.  This multi-field cross-reference by Entry Date/Time and VBC Line Count is included to optimize verification of billing for transcription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1212         | DIVISION                      | DIVISION                      | ADIV                                                                                    | This Regular New style-type, multi-field cross-reference is optimized for searching division, document type, status, and reference date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This Regular New style-type, multi-field cross-reference is optimized for searching division, document type, status, and reference date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 1202         | AUTHOR/ DICTATOR              | AUTHOR/ DICTATOR              | CA  AAU  AAUP  ACLAU                                                                    | This REGULAR, whole-file cross-reference by Author/ Dictator will facilitate both look-ups and sorting by author.  This MUMPS-type, multi-field cross-reference by AUTHOR, DOCUMENT TYPE, STATUS, and INVERSE DICTATION DATE/TIME is intended to facilitate look-up by author for the review process.  This MUMPS-type, multi-field cross-reference by Author and REGULAR Signature Date/Time is used to maintain the daily print queue for batch  printing of documents (currently, just Progress Notes) on signature.  This x-ref is used to extract lists based on context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1205         | HOSPITAL LOCATION             | HOSPITAL LOCATION             | ALOC  ALOCP                                                                             | This MUMPS-type, multi-field cross-reference is optimized for searching hospital location, document type, status, and date range.  This MUMPS-type, multi-field cross-reference by Hospital Location and  REGULAR Signature Date/Time is used to maintain the daily print queue for batch printing of documents (currently, just Progress Notes) on signature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1208         | EXPECTED COSIGNER             | EXPECTED COSIGNER             | CS  ASUP                                                                                | This REGULAR, FileMan type cross-reference by supervisor (expected cosigner) will be used to optimize FM Sorts and searches.  This MUMPS-type, multi-field cross-reference by (EXPECTED COSIGNER), DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/ TIME will be used for look-ups and queries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1211         | VISIT LOCATION                | VISIT LOCATION                | APTLD                                                                                   | This MUMPS-type, Multi-field index by PT,TITLE,"VLOC;VDT;VTYP",DA is used to optimize the check for documents of a given title for a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1301         | REFERENCE DATE                | REFERENCE DATE                | AAU  ASUP                                                                               | This MUMPS-type, multi-field cross-reference is used for look-ups by author, document type, status, and date range.  This MUMPS-type, multi-field cross-reference by EXPECTED COSIGNER), DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE/TIME will  be used for look-ups and queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1301         | REFERENCE DATE                | REFERENCE DATE                | APT  ATS  ATC  ALL  ASUB  ASVC  APRB  AVSIT  ADCPT  D  APTCL  ALOC  ACLPT  ACLAU  ACLSB | This MUMPS-type, multi-field cross-reference is used for look-ups by patient, document type, status, and date range.  This MUMPS-type, multi-field cross-reference is used for look-ups by Treating Specialty, document type, status, and date range.  This MUMPS-type, multi-field cross-reference is used for look-ups by Entry person, document type, status, and date range.  This MUMPS-type, multi-field cross-reference is used for look-ups by Entry person, document type, status, and date range.  This MULTI-fields, MUMPS-type cross-reference is used for queries by subject.  This MUMPS-type, multi-field cross-reference is used for look-ups by SERVICE, document type, status, and date  This MUMPS-type, multi-field cross-reference by Problem, Document type,  Status, and Inverse Reference Date/time is used to facilitate query by  problem.  This MUMPS-type, multi-field cross-reference by VISIT, DOCUMENT TYPE, STATUS, and INVERSE ENTRY/DICTATION DATE facilitates look-ups by visit.  This MUMPS-type, multi-field cross-reference by PATIENT, DOCUMENT CLASS, STATUS, and INVERSE REFERENCE DATE facilitates look-ups by PATIENT AND  DOCUMENT CLASS (e.g., all SIGNED Violence Postings for patient CPRSPATIENT,ONE).  This REGULAR FileMan Cross-reference by Reference Date/time is used for both look-ups and sorts.  This MUMPS-type, multi-field cross-reference by PATIENT, CLINICAL DOCUMENT CLASS, and INVERSE REFERENCE DATE facilitates look-ups by patient.  This MUMPS-type, multi-field cross-reference is used for look-ups  LOCATION, document type, status, and date  This MUMPS-Type, Multi-field cross-reference on Cosignature Date/time will assure that the cosigned notes are included in the ACLPT x-ref (completed,  by patient) upon cosignature.  This x-ref is used to extract lists based on context.  This x-ref is used to extract lists based on context. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1302         | ENTERED BY                    | ENTERED BY                    | TC  APTP  AAUP                                                                          | This REGULAR Filename type cross reference is used for sorting by the person who entered the original document.  This MUMPS-type, multi-field cross-reference is used for searching by enter person, document type, status and date range.  This x-ref is used to extract lists based on context                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1304         | RELEASE DATE/TIME             | RELEASE DATE/TIME             | E                                                                                       | This Regular, FileMan Cross-reference on Release Date/Time is used for sorting, and for the Released/unverified Report for the Verifying MRT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This Regular, FileMan Cross-reference on Release Date/Time is used for sorting, and for the Released/unverified Report for the Verifying MRT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1402         | TREATING SPECIALTY            | TREATING SPECIALTY            | TS  ATS                                                                                 | This REGULAR FileMan type cross-reference is used for support both look-ups and sorts by Treating Specialty  This MUMPS-type, multi-field cross-reference is optimized for searching by treating specialty, document type, status, and date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1404         | SERVICE                       | SERVICE                       | ASVC  SVC                                                                               | This MUMPS-type, multi-field cross-reference is optimized for searching by treating specialty, document type, status, and date range.  This REGULAR FileMan Cross-reference by Service will facilitate look-ups, sorts, and reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1405         | REQUEST-ING PACKAGE REFERENCE | REQUEST-ING PACKAGE REFERENCE | G                                                                                       | This REGULAR FM cross-reference by REQUESTING PACKAGE REFERENCE is used to  avoid multiple documents per request, and for look-ups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | This REGULAR FM cross-reference by REQUESTING PACKAGE REFERENCE is used to  avoid multiple documents per request, and for look-ups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1501         | SIGNATURE DATE/TIME           | SIGNATURE DATE/TIME           | ALOCP  APTP  AAUP  ACLPT  ACLEC  ACLAU                                                  | This MUMPS-type, multi-field cross-reference by Hospital Location and REGULAR Signature Date/Time is used to maintain the daily print queue for batch printing of documents (currently, just Progress Notes) on signature.  This MUMPS-type, multi-field cross-reference by Patient and REGULAR  Signature Date/Time is used to maintain the daily print queue for batch  printing of documents (currently, just Progress Notes) on signature.  This MUMPS-type, multi-field cross-reference by Author and REGULAR  Signature Date/Time is used to maintain the daily print queue for batch printing of documents (currently, just Progress Notes) on signature.  This MUMPS-Type, Multi-field cross-reference on Cosignature Date/time will  assure that the cosigned notes are included in the ACLPT x-ref  (completed,  by patient) upon cosignature.  This x-ref is used to extract lists based on context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1502         | SIGNED BY                     | SIGNED BY                     | ACLSB                                                                                   | This x-ref is used to extract lists based on context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This x-ref is used to extract lists based on context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 1507         | COSIGNA-TURE DATE/TIME        | COSIGNA-TURE DATE/TIME        | ACLEC  ACLPT                                                                            | This MUMPS-Type, Multi-field cross-reference on Cosignature Date/time will  assure that the cosigned notes are included in the ACLPT x-ref  (completed,  by patient) upon cosignature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1701         | SUBJECT                       | SUBJECT                       | ASUB                                                                                    | This MUMPS-type, multi-field cross-reference is used for queries by subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This MUMPS-type, multi-field cross-reference is used for queries by subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 1801         | ID PARENT                     | ID PARENT                     | VBC                                                                                     | This multi-field cross-reference by Entry Date/Time and VBC Line Count is included to optimize verification of billing for transcription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This multi-field cross-reference by Entry Date/Time and VBC Line Count is included to optimize verification of billing for transcription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2101         | ID PARENT                     | ID PARENT                     | GDAD                                                                                    | Used to find the children of an interdisciplinary note, given the interdisciplinary parent note.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Used to find the children of an interdisciplinary note, given the interdisciplinary parent note.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 15001        | VISIT ID                      | VISIT ID                      | VID                                                                                     | REGULAR FM Cross-reference by Visit ID facilitates look-up by CIRN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REGULAR FM Cross-reference by Visit ID facilitates look-up by CIRN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

#### 8925.1TIU DOCUMENT DEFINITION File

| ## Field #   | ## Field Name              | ## X-ref   | ## Description                                                                                                                                                                                                                                                                                     |
|--------------|----------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | NAME                       | B          | This KWIK cross-reference on document name will allow look-up based on sub-names, etc.                                                                                                                                                                                                             |
|              |                            | C          | This cross-reference will be used by the router/filer to identify a given report type                                                                                                                                                                                                              |
| .03          | PRINT NAME                 | AM1  D     | This MUMPS-type cross-reference is used to update the TIMESTAMP on both the current document and its parents when its PRINT NAME changes.  This REGULAR FileMan cross-reference by PRINT NAME will facilitate look-up.                                                                             |
| .04          | TYPE                       | AT         | This regular cross-reference is used for listing Document Definitions by Type.                                                                                                                                                                                                                     |
| .05          | PERSONAL OWNER             | AP         | This regular cross-reference is used for listing Document Definitions by Personal Owner.                                                                                                                                                                                                           |
| .06          | CLASS OWNER                | AC         | This regular cross reference is used to list Document Definitions by Class Owner.                                                                                                                                                                                                                  |
| .07          | STATUS                     | AS         | This regular cross-reference is used to list Document Definitions by Status.                                                                                                                                                                                                                       |
| 1,.14        | POSTING INDICATOR          | APOST      | This REGULAR FileMan Cross-reference by Posting Indicator will help to identify which Document Classes are associated with each of the currently supported Posting Types.                                                                                                                          |
| 1,.01        | HEADER PIECE               | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 1,.02        | ITEM NAME                  | C          | This REGULAR FileMan cross-reference on the ITEM NAME is used in the look-up and edit process.                                                                                                                                                                                                     |
| 1,.03        | FIELD NUMBER               | D          | This REGULAR FileMan cross-reference by field number is used by the filer-router to identify header-pieces with field numbers in the target file.                                                                                                                                                  |
| 1,.04        | LOOKUP LOCAL VARIABLE NAME | E          | This cross-reference is used by the router/filer to determine which pieces of the header should be set into special variables which may be required by the lookup routine.                                                                                                                         |
| 2,.01        | CAPTION                    | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 2,.02        | ITEM NAME                  | C          | This REGULAR FileMan cross-reference on the ITEM NAME is used in the look-up and filing processes.                                                                                                                                                                                                 |
| 2,.03        | FIELD NUMBER               | D          | This REGULAR FileMan cross-reference is used by the filer-router to identify header-fields with field numbers in the target file.                                                                                                                                                                  |
| 2,.04        | LOOKUP LOCAL VARIABLE NAME | E          | This REGULAR FileMan cross-reference  is used by the router/filer-to determine which fields of the header should be set into special variables which may be required by the lookup routine.                                                                                                        |
| 4,.01        | ITEM                       | B  AD  AMM | The REGULAR "B" cross-reference.  This cross-reference facilitates traversal from child to parent, up the class hierarchy.  This MUMPS-type cross-reference will update the timestamp on the parent document when the ITEM, MNEMONIC, or SEQUENCE changes.                                         |
| 4,2          | MNEMONIC                   | AMM        | This MUMPS-type cross-reference will update the timestamp on the parent document when the ITEM, MNEMONIC, or SEQUENCE changes.                                                                                                                                                                     |
| 4,.3         | SEQUENCE                   | AMM  AC    | This MUMPS-type cross-reference will update the timestamp on the parent document when the ITEM, MNEMONIC, or SEQUENCE changes.  This REGULAR FileMan cross-reference is used to list items by sequence number.                                                                                     |
| 4,4          | MENU TEXT                  | AMM  C     | This MUMPS-type cross-reference will update the timestamp on the parent document when the ITEM, MNEMONIC, or SEQUENCE changes.  This M cross-reference would be regular but it truncates to 40 characters instead of 30. It is used to display items with no sequence in alpha order by Menu Text. |
| 11,.01       | STAT AUTO PRINT EVENT      | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 12,.01       | ROUTINE AUTO PRINT EVENT   | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 13,.01       | PROCESSING STEP            | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 14,.01       | DIALOGUE PROMPT            | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                                                                                                   |
| 14,.03       | SEQUENCE                   | AS         | This REGULAR FileMan Cross-reference on the sequence sub-field of the Dialog Multiple will facilitate appropriate serialization of prompts.                                                                                                                                                        |
| ,99          | TIMESTAMP                  | AM         | This cross-reference invokes menu compilation in ^XUTL("XQORM", DA;TIU(8925.1, when the TIMESTAMP field is modified.                                                                                                                                                                               |

#### 8925.2TIU UPLOAD BUFFER File

| ## Field #   | ## Field Name     | ## X-ref   | ## Description                   |
|--------------|-------------------|------------|----------------------------------|
| .01          | PROCESS ID NUMBER | B          | The REGULAR "B" cross-reference. |
| 2,.01        | ERROR LOG ENTRIES | B          | The REGULAR "B" cross-reference. |

#### 8925.3TIU UPLOAD ERROR DEFINITION File

|   ## Field | ## Field     | ## X-ref   | ## Description                   |
|------------|--------------|------------|----------------------------------|
|      0.001 | ERROR CODE # | B          | The REGULAR "B" cross-reference. |

#### 8925.4TIU UPLOAD LOG File

|   Field # | Field Name        | X-ref   | Description                                                                                                  |
|-----------|-------------------|---------|--------------------------------------------------------------------------------------------------------------|
|      0.01 | EVENT DATE/TIME   | B       | The REGULAR "B" cross-reference.                                                                             |
|      0.06 | RESOLUTION STATUS | C       | This REGULAR, whole-file cross reference is used to identify unresolved errors for the filer/router process. |
|      0.08 | EVENT TYPE        | D       | This REGULAR FileMan Cross-Reference by EVENT TYPE is used for list building.                                |

#### 8925.5TIU AUDIT TRAIL File

|   ## Field # | ## Field Name           | ## X-ref   | ## Description                                                                                                                                                                              |
|--------------|-------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | TIU DOCUMENT NAME       | B  AR      | The REGULAR "B" cross-reference.  This MUMPS-type multi-field cross-reference by  TIU Document Pointer and  Reassignment date/time will help to identify records that have been reassigned. |
|         1.01 | REASSIGN-MENT DATE/TIME | AR         | This MUMPS-type multi-field cross-reference by  TIU Document Pointer and  Reassignment date/time will help to identify records that have been reassigned.                                   |

#### 8925.6TIU STATUS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                                                                                |
|--------------|-----------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | NAME            | B          | The REGULAR "B" cross-reference.                                                                                                              |
|         0.03 | SEQUENCE        | C          | This index is used for looking up and sorting document statuses by sequence number. Higher sequence numbers indicate more finished documents. |

#### 8925.7TIU MULTIPLE SIGNATURE File

|   ## Field # | ## Field Name       | ## X-ref   | ## Description                                                                                                                                                                      |
|--------------|---------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | TIU DOCUMENT NUMBER | B  AE      | The REGULAR "B" cross-reference.  This multi-field, MUMPS-type cross-reference by document and expected  cosigner facilitates the identification of privilege to sign the document. |
|         0.03 | EXPECTED SIGNER     | AE         | This multi-field, MUMPS-type cross-reference by document and expected  cosigner facilitates the identification of privilege to sign the document.                                   |

#### 8925.8TIU SEARCH CATEGORIES File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                                                                                                                                                     |
|--------------|-----------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | SEARCH CATEGORY | B          | The REGULAR "B" cross-reference.                                                                                                                                                                                   |
|         0.02 | CROSS REFERENCE | C  AM      | This REGULAR cross-reference is used to map SEARCH CATEGORY to CROSS REFERENCE  This MUMPS-type cross-reference is used to update the timestamp on the search category selection menu when a DISPLAY NAME changes. |
|         0.99 | TIMESTAMP       | AM         | This cross-reference invokes menu compilation in ^XUTL("XQORM", DA;TIU(8925.8, when the TIMESTAMP field is modified.                                                                                               |

#### 8925.9TIU PROBLEM LINK File

|   ## Field # | ## Field Name      | ## X-ref   | ## Description                                                                                                                                                                  |
|--------------|--------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | DOCUMENT           | B  APRB    | The REGULAR "B" cross-reference.  This MUMPS-type, multi-field cross-reference by Problem, Document type, Status, and Inverse Reference Date/time facilitates query by problem. |
|         0.05 | PROVIDER NARRATIVE | APRB       | This MUMPS-type, multi-field cross-reference by Problem, Document type, Status, and Inverse Reference Date/time facilitates query by problem.                                   |

#### 8925.91TIU LINK File

|   ## Field # | ## Field Name      | ## X-ref   | ## Description                                                                                                                                                                  |
|--------------|--------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | DOCUMENT           | B  APRB    | The REGULAR "B" cross-reference.  This MUMPS-type, multi-field cross-reference by Problem, Document type, Status, and Inverse Reference Date/time facilitates query by problem. |
|         0.05 | PROVIDER NARRATIVE | APRB       | This MUMPS-type, multi-field cross-reference by Problem, Document type, Status, and Inverse Reference Date/time facilitates query by problem.                                   |

#### 8925.93TIU PRINT PARAMETERS File

|   ## Field # | ## Field Name     | ## X-ref   | ## Description                   |
|--------------|-------------------|------------|----------------------------------|
|         0.01 | HOSPITAL LOCATION | B          | The REGULAR "B" cross-reference. |

#### 8925.94TIU DIVISION PRINT PARAMETERS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                   |
|--------------|-----------------|------------|----------------------------------|
|         0.01 | DIVISION        | B          | The REGULAR "B" cross-reference. |

#### 8925.95TIU DOCUMENT PARAMETERS File

|   ## Field # | ## Field Name       | ## X-ref   | ## Description                   |
|--------------|---------------------|------------|----------------------------------|
|         0.01 | DOCUMENT DEFINITION | B          | The REGULAR "B" cross-reference. |

#### 8925.97TIU CONVERSIONS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                   |
|--------------|-----------------|------------|----------------------------------|
|         0.01 | DATA CONVERTED  | B          | The REGULAR "B" cross-reference. |

#### 8925.98TIU PERSONAL DOCUMENT TYPE LIST File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                                                                                                                                                                              |
|--------------|-----------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01 | PERSON          | B  AC      | The REGULAR "B" cross-reference.  This multi-field, MUMPS-type cross-reference by User and Parent Document class is used to facilitate identification of the user's preferred list of documents within the context of a given parent class. |
|         0.03 | DISPLAY NAME    | AM         | This MUMPS-type cross-reference is used for marking records for menu  recompilation when the DISPLAY NAME for an item changes.                                                                                                              |
|         0.99 | TIMESTAMP       | AM         | This MUMPS-type cross reference on the TIMESTAMP field is used to accomplish menu compilation into ^XUTL("XQORM","DA;TIU(9025.98", for presentation of menus by ^XQORM.                                                                     |

#### 8925.99TIU PARAMETERS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                   |
|--------------|-----------------|------------|----------------------------------|
|         0.01 | INSTITU-TION    | B          | The REGULAR "B" cross-reference. |

#### 8926TIU PERSONAL PREFERENCES File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                                                         |
|--------------|-----------------|------------|------------------------------------------------------------------------------------------------------------------------|
|         0.01 | USER NAME       | B          | The REGULAR "B" cross-reference.                                                                                       |
|         0.05 | DISPLAY MENUS   | AMENU      | This MUMPS-type cross-reference evaluates the user's preference concerning display or suppression of menus within TIU. |

#### 8926.1TIU VHA ENTERPRISE STANDARD TITLE File

| ## Field #   | ## Field Name         | ## X-ref    | ## Description                                                                                                                                               |
|--------------|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | STANDARD TITLE        | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by VHA Enterprise Standard Title.                                                   |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .04          | SUBJECT MATTER DOMAIN | SMD         | This REGULAR FileMan cross-reference by Subject Matter Domain is for look-up and sorting.                                                                    |
| .05          | ROLE                  | ROLE        | This REGULAR FileMan cross-reference by Role is for look-up and sorting.                                                                                     |
| .06          | SETTING               | SET         | This REGULAR FileMan cross-reference by Setting is for look-up and sorting.                                                                                  |
| .07          | SERVICE               | SVC         | This REGULAR FileMan cross-reference by Service is for look-up and sorting.                                                                                  |
| .08          | DOCUMENT TYPE         | DTYP        | This REGULAR FileMan cross-reference by Document Type is for look-up and sorting.                                                                            |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |
| 2            | CODING SYSTEM         | B           | This multiple stores the coding system(s) associated with the codes identifying this TIU VHA ENTERPRISE STANDARD TITLE.                                      |

#### 8926.2TIU LOINC SUBJECT MATTER DOMAIN File

| ## Field #   | ## Field Name         | ## X-ref    | ## Description                                                                                                                                               |
|--------------|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | SUBJECT MATTER DOMAIN | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by Subject Matter Domain.                                                           |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .02          | ALTERNATE EXPRESSION  | SMD         | This REGULAR FileMan Cross-reference on Alternate Expression allows for look-up and sorting by synonym.                                                      |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |

#### 8926.3TIU LOINC ROLE File

| ## Field #   | ## Field Name         | ## X-ref    | ## Description                                                                                                                                               |
|--------------|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | ROLE                  | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by Role.                                                                            |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .02          | ALTERNATE EXPRESSION  | SMD         | This REGULAR FileMan Cross-reference on Alternate Expression allows for look-up and sorting by synonym.                                                      |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |

#### 8926.4TIU LOINC SETTING File

| ## Field #   | ## Field Name         | ## X-ref    | ## Description                                                                                                                                               |
|--------------|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | SETTING               | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by Setting.                                                                         |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .02          | ALTERNATE EXPRESSION  | SMD         | This REGULAR FileMan Cross-reference on Alternate Expression allows for look-up and sorting by synonym.                                                      |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |
| .01          | SERVICE               | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by Service.                                                                         |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .02          | ALTERNATE EXPRESSION  | SMD         | This REGULAR FileMan Cross-reference on Alternate Expression allows for look-up and sorting by synonym.                                                      |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |

#### 8926.6TIU LOINC DOCUMENT TYPE File

| ## Field #   | ## Field Name         | ## X-ref    | ## Description                                                                                                                                               |
|--------------|-----------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | DOCUMENT TYPE         | B           | This Regular FileMan cross-reference will facilitate look-up and sorting by Document Type.                                                                   |
|              |                       | KWIC        | This Key Word In Context (KWIC) cross-reference will facilitate look-up by partial names.                                                                    |
| .02          | ALTERNATE EXPRESSION  | SMD         | This REGULAR FileMan Cross-reference on Alternate Expression allows for look-up and sorting by synonym.                                                      |
| 99.98        | MASTER ENTRY FOR VUID | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.99        | VUID                  | AVUID       | This cross-reference is by VUID.                                                                                                                             |
|              |                       | AMASTERVUID | If multiple entries have the same VUID in the file, this cross-reference can be used to identify the Master entry for a VUID associated with a Term/Concept. |
| 99.991, .01  | EFFECTIVE DATE/TIME   | B           | This cross-reference is by Effective Date/Time.                                                                                                              |

#### 8926.72TIU LOINC SMD SYNONYMS File

|   ## Field # | ## Field Name         | ## X-ref   | ## Description                                                                                    |
|--------------|-----------------------|------------|---------------------------------------------------------------------------------------------------|
|         0.01 | SYNONYM               | B          | This Regular FileMan cross-reference will facilitate look-up and sorting by Synonym.              |
|         0.02 | SUBJECT MATTER DOMAIN | SMD        | This REGULAR FileMan Cross-reference by Subject Matter Domain is for look-ups as well as sorting. |

#### 8926.73TIU LOINC ROLE SYNONYMS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                       |
|--------------|-----------------|------------|--------------------------------------------------------------------------------------|
|         0.01 | SYNONYM         | B          | This Regular FileMan cross-reference will facilitate look-up and sorting by Synonym. |
|         0.02 | ROLE            | ROLE       | This REGULAR FileMan Cross-reference by Role is for look-ups as well as sorting.     |

#### TIU LOINC SETTING SYNONYMS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                       |
|--------------|-----------------|------------|--------------------------------------------------------------------------------------|
|         0.01 | SYNONYM         | B          | This Regular FileMan cross-reference will facilitate look-up and sorting by Synonym. |
|         0.02 | SETTING         | SET        | This REGULAR FileMan Cross-reference by Setting is for look-ups as well as sorting.  |

#### TIU LOINC SERVICE SYNONYMS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                       |
|--------------|-----------------|------------|--------------------------------------------------------------------------------------|
|         0.01 | SYNONYM         | B          | This Regular FileMan cross-reference will facilitate look-up and sorting by Synonym. |
|         0.02 | SERVICE         | SVC        | This REGULAR FileMan Cross-reference by Service is for look-ups as well as sorting.  |

#### 8926.76TIU LOINC DOCUMENT TYPE SYNONYMS File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                            |
|--------------|-----------------|------------|-------------------------------------------------------------------------------------------|
|         0.01 | SYNONYM         | B          | This Regular FileMan cross-reference will facilitate look-up and sorting by Synonym.      |
|         0.02 | DOCUMENT TYPE   | DTYP       | This REGULAR FileMan Cross-reference by Document Type is for look-ups as well as sorting. |

#### 8927TIU TEMPLATE File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                             |
|--------------|-----------------|------------|--------------------------------------------------------------------------------------------|
|         0.01 | NAME            | B          | The REGULAR "B" cross-reference.                                                           |
|         0.03 | TYPE            | AROOT      | Keeps track of active shared and personal template root folders.                           |
|         0.06 | PERSONAL OWNER  | PO         | This regular cross-reference on Personal Owner is used for look-ups and searches by owner. |

#### 8927.1TIU TEMPLATE FIELD FILE File

|   ## Field # | ## Field Name   | ## X-ref   | ## Description                                                                                       |
|--------------|-----------------|------------|------------------------------------------------------------------------------------------------------|
|         0.01 | NAME            | A  B       | New style FileMan cross-reference.  The REGULAR "B" cross-reference used to guarantee a unique name. |

### Archiving and Purging

Archiving utilities are not provided for the distributed files. Therefore, archival copies must be produced from the printed chart by methods familiar to your HIM Service (e.g., microfiche). A grace period for purge may then be defined in your parameter set-up.

### External Relations, RPCs, and APIs

TIU is dependent on the following **V** IST **A** packages to function correctly.

| Package                                                             |   Minimum Version |
|---------------------------------------------------------------------|-------------------|
| Adverse Reaction Tracking (ART)                                     |               4   |
| Authorization/Subscription (ASU)                                    |               1   |
| Health Summary (recommended)                                        |               2.7 |
| Incomplete Record Tracking (IRT), if you plan to interface with it. |               5.3 |
| Kernel                                                              |               8   |
| Patient Care Encounter (PCE)                                        |               1   |
| Patient Information Management System (PIMS)                        |               5.3 |
| VA FileMan                                                          |              21   |
| Visit Tracking                                                      |               2   |

**Patches:**

a.  Before TIU is installed, make sure these patches are on the system:

| Package                          | Patch       |
|----------------------------------|-------------|
| List Manager Patch               | VALM *1*1   |
| OE/RR Patch                      | OR*2.5*51   |
| Progress Notes                   | GMRP*2.5*44 |
| Incomplete Record Tracking (IRT) | DG*5.3*112  |
| XQOR (Unwinder) patch            | XU*8.0*56   |

b. Install the following patches ***after*** cutover to TIU:

| ## Package                      | ## Patch  Database Integration Agreements (DBIA) are available on the DBA menu on Forum.   |
|---------------------------------|--------------------------------------------------------------------------------------------|
| Adverse Reaction Tracking (ART) | GMRA*4*6                                                                                   |
| Health Summary                  | GMTS*2.7*12                                                                                |
| Progress Notes                  | GMRP*2.5*45                                                                                |

#### Database Integration Agreements

##### Remote Procedure Calls

Remote Procedure Calls (RPCs), Application Program Interfaces (APIs) and supported references to which you may subscribe are described on the DBA menu on Forum. See the DBA menu/Integration References for a complete list. The list below may not be complete.

**January 2012 Update:**

Patch TIU*1.0*252 provides Remote Procedure Call (RPC) TIU TEMPLATE GET TEMPLATE, which is used in DENT*1.2*59. It returns basic information about a given template in the TIU TEMPLATE FILE [#8927].

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Availability   |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| TIU ANCILLARY PACKAGE MESSAGE  | This remote procedure returns messages generated from other packages that contain data associated with a document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU AUTHORIZATION              | This RPC allows the calling application to evaluate privilege to perform any ASU-mediated action on a TIU document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU CAN CHANGE COSIGNER?       | BOOLEAN RPC to evaluate user's privilege to modify the expected cosigner, given the current status of the document, and the user's role with respect to it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | SUBSCRIPTION   |
| TIU CREATE ADDENDUM RECORD     | This Remote Procedure allows the creation of addenda to TIU Documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
| TIU CREATE RECORD              | This remote procedure allows the creation of TIU DOCUMENT records.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | SUBSCRIPTION   |
| TIU DELETE RECORD              | Deletes TIU Document records...Evaluates authorization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SUBSCRIPTION   |
| TIU DETAILED DISPLAY           | Gets details for display of a given record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | SUBSCRIPTION   |
| TIU DIV AND CLASS INFO         | Returns a list of Divisions and User Classes for a specific User.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SUBSCRIPTION   |
| TIU DOCUMENTS BY CONTEXT       | Returns lists of TIU Documents that satisfy the following search criteria:  1 - signed documents (all)  2 - unsigned documents  3 - uncosigned documents  4 - signed documents/author  5 - signed documents/date range                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
| TIU FIELD CAN EDIT             | Returns TRUE if the current user is allowed to edit template fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | RESTRICTED     |
| TIU FIELD CHECK                | Resolves template field names in template import file, and indicates if the imported fields are new or existing fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | RESTRICTED     |
| TIU FIELD DELETE               | Deletes an entry in the Template Field (8927.1) file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | RESTRICTED     |
| TIU FIELD DOLMTEXT             | Reads through an array of text and converts all entries of template fields to their associated List Manager text values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | RESTRICTED     |
| TIU FIELD EXPORT               | Exports Template Fields in XML format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | RESTRICTED     |
| TIU FIELD IMPORT               | Imports Template Fields from XML format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | RESTRICTED     |
| TIU FIELD LIST                 | Returns long list array of template fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | RESTRICTED     |
| TIU FIELD LIST ADD             | Adds fields in XML formatted lines to the global ^TMP("TIUFLDXML",$J).   Deletes previous lines if they existed for the current job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | RESTRICTED     |
<!-- rpc-table -->
| TIU FIELD LIST IMPORT          | Calls the IMPORT2^TIUSRVF routine to import the template fields in the ^TMP global entered via the TIU FIELD LIST ADD RPC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | RESTRICTED     |
| TIU FIELD LOAD                 | Returns a single Template Field object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | RESTRICTED     |
| TIU FIELD LOAD BY IEN          | Returns a single Template Field object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | RESTRICTED     |
| TIU FIELD LOCK                 | Locks a template field record for editing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | RESTRICTED     |
| TIU FIELD NAME IS UNIQUE       | Returns TRUE if the template field name is unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | RESTRICTED     |
| TIU FIELD SAVE                 | Saves a single Template Field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | RESTRICTED     |
| TIU FIELD UNLOCK               | Unlock Template Field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | RESTRICTED     |
| TIU GET ADDITIONAL SIGNERS     | Returns the list of additional signers currently identified for a given TIU document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
| TIU GET ALERT INFO             | Given a TIU XQAID, return the patient and document type for the item being alerted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | SUBSCRIPTION   |
| TIU GET ASSOCIATED IMAGES      | Given a Document, get the list of associated images.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | SUBSCRIPTION   |
| TIU GET BOILERPLATE            | Returns a title’s boilerplate text without resolving any objects embedded in the text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | AGREEMENT      |
<!-- rpc-table -->
| TIU GET DEFAULT PROVIDER       | This RPC returns the default provider as specified by the TIU Site Parameter DEFAULT PRIMARY PROVIDER, which has the following allowable values:  0 - NONE, DON'T PROMT  In which case the call will return 0^  1 - DEFAULT, BY LOCATION  In this case, the call will return the default provider for a given Hospital Location, as specified in the set-up for the Clinic in MAS. If a default provider is specified for the location in question, that person will be returned. If the Clinic set-up specifies use of the Primary Provider (defined) for the patient, then that person will be returned. The return format will be DUZ^LASTNAME,FIRSTNAME.  2 - AUTHOR (IF PROVIDER)  In this case, the call will return the current user (if they are a Provider). If they're not a known Provider, then the call will return 0^. | SUBSCRIPTION   |
| TIU GET DOC COUNT BY VISIT     | This remote procedure returns the number of documents that are linked to a particular visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
| TIU GET DOCUMENT PARAMETERS    | This Remote Procedure returns the parameters by which a given document or document type is to be processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | SUBSCRIPTION   |
| TIU GET DOCUMENT TITLE         | This remote procedure returns the pointer to the TIU DOCUMENT DEFINITION FILE that corresponds to the TITLE of the document identified in the TIUDA parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
| TIU GET DOCUMENTS FOR IMAGE    | Given an image, get the list of associated documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
| TIU GET DOCUMENTS FOR REQUEST  | Returns the list of documents associated with a given request (e. g., Consult Request, Surgical Case).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
| TIU GET DS TITLES              | Returns a set of discharge summary titles for use in a long list box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
| TIU GET DS URGENCIES           | Returns a set of discharge summary urgencies for use in a long list box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU GET LIST OF OBJECTS        | This RPC returns the list of TIU OBJECTS that the current user may select from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | SUBSCRIPTION   |
| TIU GET PERSONAL PREFERENCES   | Returns Users personal preferences for TIU in the following format:  TIUY = USER [1P] ^ DEFAULT LOCATION [2P] ^ REVIEW SCREEN SORT FIELD [3S] ^  REVIEW SCREEN SORT ORDER [4S] ^ DISPLAY MENUS [5S] ^ PATIENT SELECTION PREFERENCE [6S] ^ ASK 'Save changes?' AFTER EDIT [7S] ^ASK SUBJECT FOR PROGRESS NOTES [8S] ^                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | SUBSCRIPTION   |
| TIU GET PN TITLES              | This API returns a list of Progress Notes Titles, including a SHORT LIST of preferred titles as defined by the user, and a LONG LIST of all titles defined at the site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SUBSCRIPTION   |
| TIU GET PRINT NAME             | This Remote Procedure receives a pointer to the TIU DOCUMENT DEFINITION FILE (#8925.1) and returns a string containing the Print Name of the corresponding Document Definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | SUBSCRIPTION   |
| TIU GET PRF ACTIONS            | Returns PRF and TIU data for each PRF Flag Assignment/Action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | RESTRICTED     |
<!-- rpc-table -->
| TIU GET RECORD TEXT            | This RPC will get the textual portion of a TIU Document Record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | SUBSCRIPTION   |
| TIU GET REQUEST                | This Remote Procedure returns the variable pointer to the REQUESTING PACKAGE REFERENCE (File #8925, Field #1405). This would be the record in the Requesting Package (e.g., Consult/Request Tracking or Surgery) for which the resulting document has been entered in TIU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU GET SITE PARAMETERS        | This RPC returns the TIU Parameters for the Division the user is logged in to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU ID ATTACH ENTRY            | This RPC will attach a document as an Interdisciplinary (ID) entry to an ID Parent document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU ID CAN ATTACH              | This BOOLEAN RPC evaluates the question of whether a particular document may be attached as an entry to an Interdisciplinary Note (i.e., can this document be an ID Child?).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU ID CAN RECEIVE             | This BOOLEAN RPC evaluates the question of whether a particular document may receive an entry as an Interdisciplinary Parent Note (i.e., can this document be an ID Parent?).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
| TIU ID DETACH ENTRY            | This call will remove an ID Entry from an Interdisciplinary Note.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU IDENTIFY CONSULTS CLASS    | This RPC returns the record number of the class CONSULTS in the TIU DOCUMENT DEFINITION file (#8925.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SUBSCRIPTION   |
| TIU IDENTIFY SURGERY CLASS     | returns the record number of the new SURGICAL REPORTS Class in the TIU DOCUMENT DEFINITION file (#8925.1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU IS THIS A CONSULT?         | BOOLEAN RPC which evaluates whether the title indicated is that of a consult.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU IS THIS A SURGERY?         | BOOLEAN RPC which evaluates whether the title indicated is that of a SURGICAL REPORT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU IS USER A PROVIDER?        | This Boolean RPC returns TRUE if the user was a known provider on the date specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU JUSTIFY DELETE?            | BOOLEAN RPC that evaluates whether a justification is required for deletion (e.g., deletion is authorized, but the document has been signed, etc.).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LINK DOCUMENT TO IMAGE     | This RPC links a document with an image. It will support a many-to-many association between documents and images.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LOAD BOILERPLATE TEXT      | This RPC will load the boilerplate text associated with the selected title, and execute the methods for any objects embedded in the boilerplate text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LOAD RECORD FOR EDIT       | This RPC loads the return array with data in a format consistent with that required by the TIU UPDATE RECORD API. It should be invoked when the user invokes the Edit action, to load the dialog for editing the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LOCK RECORD                | This RPC will issue an incremental LOCK on the record identified by the TIUDA parameter, returning an integer truth value indicating success or failure in obtaining the LOCK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
| TIU LONG LIST BOILERPLATED     | Used by the GUI to supply a long list of boiler plated titles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | RESTRICTED     |
<!-- rpc-table -->
| TIU LONG LIST CONSULT TITLES   | This RPC serves data to a long list of selectable TITLES for CONSULTS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LONG LIST SURGERY TITLES   | This RPC serves lists of selectable titles within the SURGICAL REPORTS class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU LONG LIST OF TITLES        | This RPC serves data to a long list of selectable TITLES by CLASS. e.g., passing the class PROGRESS NOTES will return active Progress Notes titles which the current user is authorized to enter notes under.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
| TIU NEED TO SIGN               | When a user processes a notification, CPRS checks to see if the user’s signature is currently required for the document. If it is not required at that time, the notification will be deleted by CPRS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
| TIU NOTES                      | This API gets lists of progress notes for a patient, with optional parameters for STATUS, EARLY DATE/TIME, and LATE DATE/TIME.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
| TIU NOTES 16 BIT               | This API gets lists of progress notes for a patient, with optional parameters for STATUS, EARLY DATE/TIME, and LATE DATE/TIME.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
| TIU NOTES BY VISIT             | This API gets lists of Progress Notes by visit from TIU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | SUBSCRIPTION   |
| TIU ONE VISIT NOTE             | Gets parameters for DOCUMENT type. Can more than one document type per visit exist? The ALLOW > 1 RECORD PER DOCUMENT is ignored for any title in the DISCHARGE SUMMARY class and document class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SUBSCRIPTION   |
| TIU PERSONAL TITLE LIST        | This Remote Procedure returns the user's list of preferred titles for a given class of documents, along with the default title, if specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
| TIU PRINT RECORD               | Allows Printing of TIU Documents on demand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | SUBSCRIPTION   |
| TIU REM DLG OK AS TEMPLATE     | Returns TRUE is the passed in reminder dialog is allowed to be used in a TIU Template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | RESTRICTED     |
| TIU REMINDER DIALOGS           | Returns a list of reminder dialogs allowed for use as Templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | RESTRICTED     |
<!-- rpc-table -->
| TIU REMOVE LINK TO IMAGE       | This RPC will remove a link between a document and an image. Only valid links may be removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU REQUIRES COSIGNATURE       | This Boolean RPC simply evaluates whether the current user requires cosignature for TIU DOCUMENTS, and returns a 1 if true, or a 0 if false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
| TIU SET ADMINISTRATIVE CLOSURE | Sets the file attributes necessary to close a document by administrative action (either manual or by scanning a paper document that doesn't require the signature of an author, as a typical TIU Document would).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SUBSCRIPTION   |
| TIU SET DOCUMENT TEXT          | Buffers the transmittal of text (i.e., the body of TIU Documents) from the Client to the Server. It allows documents of indefinite size to be filed, without risk of an allocate error on the M Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SUBSCRIPTION   |
| TIU SIGN RECORD                | This API Supports the application of the user's electronic signature to a TIU document while evaluating authorization, and validating the user's electronic signature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | SUBSCRIPTION   |
| TIU SUMMARIES                  | This API gets lists of Discharge Summaries for a patient, with optional parameters for STATUS, EARLY DATE/TIME, and LATE DATE/TIME.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | SUBSCRIPTION   |
| TIU SUMMARIES BY VISIT         | This API returns lists of Discharge Summaries by visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SUBSCRIPTION   |
| TIU TEMPLATE ACCESS LEVEL      | Used to determine what access a user has to templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | RESTRICTED     |
<!-- rpc-table -->
| TIU TEMPLATE CHECK BOILERPLATE | This RPC will evaluate boilerplate passed in the input array, checking to see whether any of the embedded objects are inactive, faulty, or ambiguous.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
| TIU TEMPLATE CREATE/MODIFY     | This remote procedure allows creation and update of Templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU TEMPLATE DELETE            | This RPC will delete orphan entries in the Template file (i.e., only those entries that have been removed from any Groups, Classes, Personal or Shared Root entries).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SUBSCRIPTION   |
| TIU TEMPLATE GET DEFAULTS      | Returns Default Template Settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | RESTRICTED     |
| TIU TEMPLATE GET DESCRIPTION   | Returns a Template's Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | RESTRICTED     |
| TIU TEMPLATE GETBOIL           | Returns the boilerplate of a given template. TIU objects within the boilerplate are not expanded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | RESTRICTED     |
| TIU TEMPLATE GETITEMS          | Returns the children of a given template folder, group template or template dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | RESTRICTED     |
| TIU TEMPLATE GETPROOT          | Gets information about the user’s My Template folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | RESTRICTED     |
| TIU TEMPLATE GETROOTS          | Gets information about the user’s My Template folder, as well as the Shared Templates folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | RESTRICTED     |
| TIU TEMPLATE GET TEMPLATE      | Used in DENT*1.2*59. It returns basic information about a given template in the TIU TEMPLATE FILE [#8927]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | RESTRICTED     |
| TIU TEMPLATE GETTEXT           | Receives boilerplate text, expands any TIU objects contained within it, and returns the expanded text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | RESTRICTED     |
| TIU TEMPLATE ISEDITOR          | Returns TRUE if the user is allowed to edit shared templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | RESTRICTED     |
| TIU TEMPLATE LISTOWNR          | Uses in long lists to return a subset of users who have personal templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | RESTRICTED     |
| TIU TEMPLATE LOCK              | Locks Template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | RESTRICTED     |
| TIU TEMPLATE PERSONAL OBJECTS  | Returns a list or Patient Data Objects allowed in Personal Templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | RESTRICTED     |
| TIU TEMPLATE SET DEFAULTS      | Saves Template Default Settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | RESTRICTED     |
<!-- rpc-table -->
| TIU TEMPLATE SET ITEMS         | This RPC will create or update the items for a Group, Class, Root, or Dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SUBSCRIPTION   |
| TIU TEMPLATE UNLOCK            | Unlocks a template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | RESTRICTED     |
<!-- rpc-table -->
| TIU UNLOCK RECORD              | This RPC will decrement the lock on a given TIU Document Record, identified by the TIUDA input parameter. The return value will always be 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU UPDATE ADDITIONAL SIGNERS  | This RPC accepts a list of persons, and adds them as additional signers for the document identified by the first parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | SUBSCRIPTION   |
| TIU UPDATE  **RECORD**         | This API updates the record named in the TIUDA parameter, with the information contained in the TIUX(Field #) array. The body of the modified TIU document should be passed in the TIUX("TEXT",i,0) subscript, where i is the line number (i.e., the "TEXT" node should be ready to MERGE with a word processing field). Any filing errors which may occur will be returned in the single valued ERR parameter (which is passed by reference).                                                                                                                                                                                                                                                                                                                                                                                       | SUBSCRIPTION   |
| TIU USER CLASS LONG LIST       | Long List of active User Classes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | RESTRICTED     |
| TIU WAS THIS SAVED?            | This Boolean Remote Procedure will evaluate whether a given document was committed to the database, or whether the user who last edited it was disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SUBSCRIPTION   |
<!-- rpc-table -->
| TIU WHICH SIGNATURE ACTION     | This RPC infers whether the user is trying to sign or cosign the documents in question, and indicates which ASU ACTION the GUI should pass to the TIU AUTHORIZATION RPC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | SUBSCRIPTION   |

##### Protocols

Packages can subscribe to the following protocols to receive notifications from TIU and provide informational messages to TIU users upon request. An integration agreement is required before subscribing to these protocols.

###### TIU AVATAR MDM EVENT

**Note:** This protocol is temporary and vendor specific to the first vendor we are nationally releasing. The vendor specific name was retained because some sites are already using the interface in production. In the next release of the Opioid Treatment Project (OTP) updates, the goal is to create vendor-agnostic names for the required protocol.

This protocol receives and processes inbound Medical Document Management (MDM) messages from the MyAvatar ® system. Dispense information is captured in the OTP MEDICATION DISPENSE file (#101.22) as well as creating progress notes.

###### TIU AVATAR MDM SUB

**Note:** This protocol is temporary.

This protocol subscriber handles MDM messages with an event type of T02. This protocol handles the creation of TIU process notes containing dispense information from the OTP system.

###### TIU DOCUMENT ACTION EVENT

This protocol notifies subscribing packages when a document is deleted, retracted or  reassigned. This protocol uses both the TIU ACTIONS RESOURCE device and the TIUDAN TaskMan sync flag functionality to ensure that actions are broadcast to subscribers one at a time and in the order they occurred. If the TIU ACTIONS RESOURCE device becomes backed up, system administrators should use the TaskMan SYNC flag file control option [XUTM SYNC] to move to the next scheduled job. The name of the sync flag is TIUDAN.

###### TIU DOCUMENT ACTION DISPLAY

This protocol allows subscribing packages to display an onscreen message to TIU users when a document is deleted, retracted or reassigned. This message is displayed in both the roll n’ scroll VistA options and the Computerized Patient Record System (CPRS) graphical user interface (GUI), depending on which software the user initiates the action from.

### Package-Wide Variables

Text Integration Utilities has no package-wide variables.

### Online Documentation

#### Intranet WWW Documentation

TIU/ASU’s documentation set (Installation Guide, Implementation Guide, Technical Manual, and User Manual) is available on the System Design &amp; Development World Wide Web (WWW) page at the following address:

REDACTED

This address takes you to the Clinical Products page, which shows a listing of all the clinical software manuals. Click on the Text Integration Utilities link and it will take you to the TIU Homepage. You can also get there by going straight to the following address:

REDACTED

TIU documentation is also available in Adobe Acrobat pdf format on the REDACTED.

#### KIDS Install Print Options

##### Build File Print

Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software.

Select OPTION NAME: XPD MAIN     Kernel Installation &amp; Distribution System menu

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation &amp; Distribution System Option: Utilities

Build File Print

Install File Print

Convert Loaded Package for Redistribution

Display Patches for a Package

Purge Build or Install Files

Rollup Patches into a Build

Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities Option: Build File Print

Select BUILD NAME: TEXT INTEGRATION UTILITIES 1.0          TEXT INTEGRATION UTILITIES

DEVICE: HOME//   VAX

#### Print Results of the Installation Process

Use the KIDS Install File Print option if you’d like to print out the results of the installation process.

DEVICE: HOME//   ANYWHERE

PACKAGE: TEXT INTEGRATION UTILITIES 1.0            PAGE 1

COMPLETED           ELAPSED

------------------------------------------------------------------------------

STATUS: Install Completed                 DATE LOADED: JAN 21, 1997@12:49:03

INSTALLED BY: CPRSPROVIDER,FIVE

NATIONAL PACKAGE: TEXT INTEGRATION UTILITIES

INSTALL STARTED: JAN 21, 1997@12:49:53                    0:

ROUTINES:                                                 0:

FILES:

HEALTH SUMMARY TYPE                                       0:

TIU DOCUMENT                                              0:

TIU DOCUMENT DEFINITION                                   0:

TIU UPLOAD BUFFER                            12:50:29

TIU UPLOAD ERROR DEFINITION

TIU UPLOAD LOG                                            0:

TIU AUDIT TRAIL

TIU STATUS                                                0:

TIU MULTIPLE SIGNATURE

TIU SEARCH CATEGORIES

TIU PROBLEM LINK                                          0:

TIU EXTERNAL DATA LINK

TIU PRINT PARAMETERS                         12:50:33             0:00:01

TIU DIVISION PRINT PARAMETERS                12:50:33

TIU DOCUMENT PARAMETERS                      12:50:34             0:00:01

TIU CONVERSIONS                              12:50:35             0:00:01

TIU PERSONAL DOCUMENT TYPE LIST              12:50:35

TIU PARAMETERS                                            0:

TIU PERSONAL PREFERENCES

PATIENT POSTING SITE PARAMETERS                           0:

BULLETIN                                                  0:

SECURITY KEY

FUNCTION                                     12:50:43

PRINT TEMPLATE                                            0:

INPUT TEMPLATE                                            0:

DIALOG                                       12:50:50

PROTOCOL                                                  0:

OPTION                                                    0:

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED                                   0:

XPD POSTINSTALL COMPLETED

INSTALL QUESTION PROMPT                                              ANSWER

XPZ1

##### Other Kernel Print Options

Besides using the Kernel Installation &amp; Distribution (KIDS) options to get lists of routines, files, etc., you can also use other Kernel options to print online technical information.

###### Routines

XUPRROU (List Routines) prints a list of any or all of the TIU routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **list Routines**

Routine Print

Want to start each routine on a new page: No// **[ENTER]**

routine(s) ?   &gt; **TIU***

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each TIU subset routine.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?   &gt; **TIU***

###### Globals

The global unique to VA in the TIU package is ^TIU(.  Use the Kernel option XUPRGL (List Global) to print a list of any of these globals. This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **LIST Global**

Global ^^ **PX***

#### XINDEX

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls.

XINDEX is invoked from programmer mode:  D ^XINDEX.

When selecting routines, select TIU*.

#### Data Dictionaries/ Files

The number-spaces for TIU files unique to VA are 8925-8926. Use the VA FileMan DATA DICTIONARY UTILITIES, option #8 ( DILIST, List File Attributes), to print a list of these files. Depending on the FileMan template used to print the list, this option will print out all or part of the data dictionary for the TIU files.

**Example:**

&gt; **D P^DI**

VA FileMan 21.0

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: 8925

(1 entry)

GO TO WHAT FILE: 8925// 8926*

Select LISTING FORMAT: STANDARD// [Enter]

DEVICE: **PRINTER**

### Glossary

**ASU** Authorization/Subscription Utility, - a utility that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables.

**Action** A functional process that a clinician or clerk uses in the TIU computer program. “Edit,” “Create,” and “Find” are examples of actions.

**Boilerplate Text** A pre-defined Progress Notes or Discharge Summary template containing standard text, with blanks to fill in for specific data about a patient.

**Class** Classes are groups of groups which hold documents.

For example, Progress Notes is a Class with many Document Classes (kinds of progress notes) under it.

Classes may themselves be subdivided into Classes and/or may go straight to Document Class if no further subdivisions are desired. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.

**Clinician** A doctor or other provider in the medical center who is authorized to provide patient care.

**Component** Components are "sections" or "pieces" of documents, such as Subjective, Objective, Assessment, and Plan in a SOAP Progress Components may have (sub)Components as items. They may have Boilerplate Text.  Components may be designated SHARED.

**Discharge Summary** A discharge summary is a formal synopsis of a patient’s medical care during a single hospitalization. It includes the pertinent diagnostic and therapeutic tests and procedures as well as the conclusions generated by those tests. A discharge summary is prepared for all discharges and transfers from a VA medical center or domiciliary or from nursing home care. The automated Discharge Summary module provides an efficient and immediate mechanism for clinicians to capture transcribed patient discharge summaries online, where they’re available for review, signing, adding addendum, etc..

**Document Class** Document Classes group documents.  Document Class is the lowest level of class, and has Titles as items under it.

**Document Definition** The Document Definition utility provides the building blocks for TIU, by organizing types of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class.

**IRT** Incomplete Record Tracking

**MIS** Common abbreviation/synonym used at VA site facilities for the Medical Information Section of Medical Administration Service. may be called HIMS (Health Information Management Section).

**MIS Manager** Manager of the Medical Information Section of Medical Administration Service at the site facility who has ultimate responsibility to see that  MRTs complete their duties.

**MRT** Medical Record Technician in the Medical Information Section of Medical Administration Service at the site facility who completes the tasks of assuring that all discharge summaries placed in a patient’s medical record have been verified for accuracy and completion and that a permanent chart copy has been placed in a patient’s medical record for each separate admission to the hospital.

**Object** Objects are names or other text which may be embedded in the predefined boilerplate text of Titles. And example of an “Object” is “PATIENT AGE.” Objects are typed into the boilerplate text of a Title, enclosed by '|'s.  If a Title has boilerplate text:

Patient is a healthy |PATIENT AGE| year old male ...

Then a user who enters such a note for a 56 year old patient would be presented with the text:

Patient is a healthy 56 year old male ...

**PDMP** Prescription Drug-Monitoring Programs

**Progress Notes** The Progress Notes module of TIU is used by health care givers to enter and sign online patient progress notes and by transcriptionists to enter notes to be signed by caregivers at a later date. Caregivers may review progress notes online or print progress notes in chart format for filing in the patient’s record.

**TIU** Text Integration Utilities

**Title** Titles are definitions for documents. They store the behavior of the documents which use them.

**User Class** The basic component of ASU (Authorization/ Subscription Utility). The User Class file contains the different categories of users within a hospital. ASU allows sites to designate who is authorized to do what.

## MAS Options to Print Progress Notes [TIU PRINT PN MAS MENU]