---
app_name: 'CPRS: Adverse Reaction Tracking (ART) (GMRA)'
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
package_id: GMRA
patch: null
patch_gap: null
section: ''
source_file: gmra_4_0_tm.docx
status: draft
title: gmra 4 0 tm.docx
---

## Adverse Reaction Tracking 4.0 
Technical Manual

<!-- image -->

January 2024


Enterprise Program Management Office

Preface

This manual was developed to assist the Information Resource Management (IRM) Support personnel and Enterprise VistA Support (EVS) personnel in understanding the component structures of the Adverse Reaction Tracking (ART) package. In addition, materials relating to security, resource requirements, and relationships to other VistA packages are included. Familiarity with the M programming language and VistA is assumed.

Revision History

When updates occur, the Title Page lists the new revised date and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates.

Table 1-Revision History

| Revision Date         | Page or Chapter                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| January 2024          | 2  47  43-44  v, 43, 46, 47, 53, 68, 82, 84                 | Added description of Patch GMRA*4.0*68  Added GMRA EDIT VERIFIED DATA to the Protocol section  Updated the File Security section.  Added a caption to every table in this document                                                                                                                                                                                                                                 |
| September 2022        | 3  46  53  Global                                           | Added description of patch GMRA*4*51  REMOTE ALLERGY COMMENT-120.88  Added new file to File List FileList 120.88  Added new file (GMR 120.88) to Resource Requirements  Updated Dates on Title page and TOC                                                                                                                                                                                                        |
| June 2020             | 2  3  48                                                    | Added GMRA*4*53 to the list of patches.  Added a short description of patch GMRA*4*53.  Added information about the GMRA ASSESSMENT CHANGE protocol.                                                                                                                                                                                                                                                               |
| November 2018         | 2  70                                                       | Added a description of patch GMRA*4*59  Updated the GMRA MARK CHART bulletin entry in the Glossary.                                                                                                                                                                                                                                                                                                                |
| October 2018          | Page 2                                                      | Inclusion of details for GMRA*4*58                                                                                                                                                                                                                                                                                                                                                                                 |
| April 2017            | Page 2                                                      | Inclusion of details for GMRA*4*55 patch.                                                                                                                                                                                                                                                                                                                                                                          |
| April 2016            | Page 3  Pages 36 and 36                                     | Updated description of the GMRA*4*48 - Assessment Clean Up Utility patch.  Revised the Assessment Clean Up Utility section. This included describing the process of accessing the GMRA ASSESSMENT UTILITY for the first time.                                                                                                                                                                                      |
| April 2016            | i thru 89  iv  3  3, 50  55, 56, 57, 57, 58, 60, 61, and 62 | Made grammatical and formatting changes throughout the document. Updated footer to reflect April 2016 date.  Updated Revision History.  Reference to GMRA*4*46.  Added patch summary for GMRA*4*46. Added step 1 to 1. Enter/Edit Site Configurable File menu option.  Added information on Patch GMRA*4*46 to clarify Version 1 and 2 for callable routine GMRADPT.                                               |
| April 2016            | 3, 36, 36, 38, and 39  36, 61, 70, and 71  48  50           | Added summary description of GMRA*4*48 – Assessment Clean Up Utility. Also, added description of Assessment Clean-up Utility distributed in GMRA*4.0*48  Added note, rephrased sentence defining a record in Patient Allergies file. Changed definition of Historical, Observed, and True Allergy in Glossary.  Added protocols used by GMRA Assessment Utility  Added Assessment Clean Up Utility to Menu Options |
| October 2013          | 24  48                                                      | Updates to Allergy Clean-up Option  Updates to protocol list                                                                                                                                                                                                                                                                                                                                                       |
| April 2006            |                                                             | Updates for GMRA*4.0*26                                                                                                                                                                                                                                                                                                                                                                                            |
| April-July 2005       |                                                             | Updates for GMRA*4.0*23                                                                                                                                                                                                                                                                                                                                                                                            |
| December 2004         | Throughout manual.                                          | Edits based on SQA review, including removal of Marked on Chart prompts.                                                                                                                                                                                                                                                                                                                                           |
| November 2004         | Pages 1 & 39                                                | NKA deletion enhancement added                                                                                                                                                                                                                                                                                                                                                                                     |
| October/November 2004 | Throughout manual                                           | Patient name and SSN and provider name updates to comply with Patient privacy SOP.                                                                                                                                                                                                                                                                                                                                 |
| October 2004          |                                                             | CPRS GUI 25 Release Notes for ART added and updated.                                                                                                                                                                                                                                                                                                                                                               |
| January 2004          |                                                             | Patch 17 (GMRA*4*17) Free Text Allergy Clean Up Utility info added.                                                                                                                                                                                                                                                                                                                                                |

Table of Contents

Introduction	1

ART and Data Standardization	1

GMRA*4.0*68	2

GMRA*4.0*59	2

GMRA*4*58 – Suppress Non-Drug Ingredient Level Alert	2

GMRA*4*55 – Native Domain Standardization Patch	3

GMRA*4.0*51 – CPRS V32b Modifications	3

GMRA*4*53 - CPRS V31.B - ART BUG FIXES	3

GMRA*4*48 - Assessment Clean Up Utility	3

GMRA*4*46 Allergy Order Check Signs/Symptoms	4

GMRA*4*42 - Progress Notes and Historical Allergy Entries	4

GMRA*4*41 - Pharmacy Encapsulation Changes	5

GMRA*4*40 - Updating ANGIOTEN-Related Allergies	5

GMRA*4*38 - Add Allergy-Related Progress Note to CPRS Signature	5

GMRA*4*37 - Add Remote Data to Contrast Media Order Checks	6

GMRA*4*35 - Possible Problem with List by Location Unassessed	6

GMRA*4*36 - Remove Ability to Delete Allergy Records	6

GMRA*4*34 - Update to HL7 Messages	8

GMRA*4*33 - Prevent Test Patients From Appearing on Live Report	8

GMRA*4*31 - Check for Compiled Cross-References in File 120.8	8

GMRA*4*30 - Prevent Deceased Patients from Appearing on Report	8

GMRA*4*29 - Automated Clean Up of Free Text Allergies	9

GMRA*4*27 – Allergy Order Check Does Not Fire for Contrast Media	9

GMRA*4.0*26 - Remote Data Interoperability (RDI) Update	9

GMRA*4.0*25 - Blank Sign/Symptom Problem	9

GMRA*4*24 - Update HDR Trigger Code	10

GMRA*4.0*23 - HDR/DS Changes	10

Data Dictionary Changes	10

Mailman Changes	10

GMRA Package (* Affects GUI Functionality)	11

GMRA*4.0*22 - HDR Application Installation	11

GMRA*4*21 - Removal of Allergies as Orders	11

GMRA*4*20 - Allergy Data Updates	12

GMRA*4*19 - Notifications from CPRS When Allergies Are Added	12

GMRA*4.0*18 - HDR/VistA Data Extraction Framework (VDEF) Updates	13

GMRA*4.0*17 - Free Text Allergy Clean Up Utility	13

Overview of Adverse Reaction Tracking Functionality	14

Implementation and Maintenance	16

Site Parameters	16

Edit Allergy File	17

Enter/Edit Signs/Symptoms Data	17

Enter/Edit Site Parameters	17

Sign/Symptoms List	22

Allergies File List	23

Allergy Clean-up Utility	24

Free Text Allergy Clean Up Utility	24

Detailed Display	26

Mark Entered in Error	28

Update to New Reactant	29

Add/Edit Patient Reaction	32

Add/Edit Allergy File	34

Assessment Clean Up Utility	36

Signing off on Allergies	40

Q&amp;A Tips:	41

Menu Assignment	42

Security Key Assignment	42

Mail Group Membership	42

Bulletins List	42

Security	43

Security Keys	43

File Security	43

Option Delegation	44

Privacy Act Statement	44

Electronic Signature	44

GMRA UPDATE RESOURCE	45

Routines	46

File List	47

Templates	48

Protocols	48

Exported Options	50

Options Not on a Menu	50

Menu Options	50

Cross References	52

Archiving and Purging	53

Resource Requirements	54

Callable Routines	55

Version 1	55

Version 2	59

External Relations	63

Database Integration Agreements	63

SACC Exemptions	64

Internal Relations	65

Package-wide Variables	66

How to Generate On-line Documentation	67

Question Marks	67

XINDEX	67

Inquire to File Entries	67

Print Options File	67

List File Attributes	67

Glossary	69

Appendix 1: CPRS (25 and 26) Release Notes Related to ART	73

PATCH OR*3*233	73

GUI 26	73

GUI 25	73

Deleting an Assessment of NKA	76

Appendix 2: ART Data Standardization FAQ	78

ART Data Standardization FAQ	78

VA Enterprise Terminology Services (VETS) Push and Deployment Questions	85

New Term Rapid Turnaround (NTRT) Process Questions	86

Site Clean-up Questions	88

Health Data Repository (HDR) Questions	89


### Introduction

The objective of ART is to track and report patient allergy and adverse reaction data. This is accomplished through two interfaces:

1. CPRS GUI
2. ART menus and options within legacy .

Use of ART within CPRS is primarily described in CPRS documentation, but some examples are provided in the ART manuals.

### ART and Data Standardization

ART has been modified in order to standardize the data stored in the allergy package.  Standardized data is necessary for inclusion in the Health Data Repository (HDR).

Two new cross-references and a new Application Programmer Interface (API) were created that will allow changes to existing reactant terms to propagate through existing allergy entries in the PATIENT ALLERGIES file (120.8).

The GMR ALLERGIES file (120.82) and the SIGNS/SYMPTOMS file (120.83) are being standardized.  As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files.  In addition, users will no longer be able to add “free text” signs /symptoms.

Changes have been made to ART through the following ART patches:

GMRA*4*17    Free text utility

GMRA*4*18    HDR/VistA Data Extraction Framework (VDEF) update

GMRA*4*19    Notifications from CPRS when allergies are added

GMRA*4*2      Deleting Soundex x-ref &amp; misc

GMRA*4*20    Allergy data

GMRA*4*21    Removal of allergies as orders

GMRA*4*22    HDR Application Installation

GMRA*4*23    HDR/DS Changes

GMRA*4*24    Update HDR trigger code

GMRA*4*25    Blank sign/symptom problem

GMRA*4*26    Remote Data Interoperability (RDI) update

GMRA*4*27    ALLERGY ORDER CHECK DOES NOT FIRE FOR CONTRAST MEDIA

GMRA*4*29    Automated clean-up of free text allergies

GMRA*4*30    PREVENT DECEASED PATIENTS FROM APPEARING ON REPORT

GMRA*4*31    Check for compiled cross-references in file 120.8

GMRA*4*33    PREVENT TEST PATIENTS FROM APPEARING ON LIVE REPORT

GMRA*4*34    Update to HL7 messages

GMRA*4*36    Remove ability to delete allergy records

GMRA*4*37    Add remote data to contrast media order checks

GMRA*4*38    Add allergy related progress note to CPRS signature

GMRA*4*40    Updating ANGIOTEN related allergies

GMRA*4*41    Pharmacy Encapsulation Changes

GMRA*4*42    PROGRESS NOTES AND HISTORICAL ALLERGY ENTRIES

GMRA*4*44    RDI VHIM COMPLIANCE UPDATES

GMRA*4*45    ORDER CHECK API UPDATE

GMRA*4*46    ALLERGY ORDER CHECK SIGNS/SYMPTOMS

GMRA*4*48    ASSESSMENT CLEAN UP UTILITY

GMRA*4*53	  CPRS V31.B - ART BUG FIXES

GMRA*4*55    Native Domain Standardization Patch

GMRA*4*58    SUPPRESS NON-DRUG INGREDIENT LEVEL ALERTS

GMRA*4*59	  VistA Mailman Mark Patient Chart

GMRA*4*51	  CPRS V32b Modifications

GMRA*4*68    32A ENTER/EDIT PATIENT REACTION DATA DEFECT AND

VDIF ALLERGY UPDATE

#### GMRA*4.0*68

This patch fixes issues with using Enter/Edit Patient Reaction Data to record a historical reaction, and allergies not displaying in the reaction results in the HealthShare application.  This patch adds the  GMRA EDIT VERIFIED DATA protocol to the ART package. It gets activated whenever a user edits a verified allergy, including adding or editing observations.

#### GMRA*4.0*59

This patch enables the ART package to generate a real-time VistA MailMan bulletin when allergy or adverse reaction information is entered into CPRS. As described in *Appendix 1: CPRS (25 and 26) Release Notes Related to ART* , the ability to generate this bulletin through CPRS was disabled by CPRS GUI version 26. Patch GMRA*4*59 restores this functionality by sending a bulletin to the GMRA MARK CHART mail group when providers enter allergy/adverse reaction information in the CPRS “Enter Allergy or Adverse Reaction” window, accessed from either the CPRS Orders tab or Cover Sheet. The bulletin provides a reminder that the patient chart must be updated with the allergy/adverse reaction information displayed in the bulletin message.

#### GMRA*4*58 – Suppress Non-Drug Ingredient Level Alert

GMRA*4*58 suppresses Non-Drug Ingredient Level Alert that was introduced in patch GMRA*4*50.  This patch will add a filter to suppress those alerts where ALLERGY TYPE field (#3.1) in the PATIENT ALLERGY file (#120.8), does not contain the Drug code of “D”, as no action is needed to be taken for this scenario.

#### GMRA*4*55 – Native Domain Standardization Patch

GMRA*4*55 installs the Native Domain Standardization Patch, which implements a new coding system field with the future intent to store the nationally standardized codes in the GMR ALLERGIES (#120.82) and the SIGNS/SYMPTOMS (#120.83) files.

This new coding system field is intended to aid the effort of interoperability between the VA and the entities that use its data including the DoD.  There are two subfields “CODING SYSTEM” and “CODE” within the new coding system fields to house the relevant coding system name (i.e. RxNorm) and the relevant code when available.

These new fields are meant to reside within VistA and will not impact any current Graphical User Interface (GUI) or disrupt daily operations relating to the Allergies domain.

#### GMRA*4.0*51 – CPRS V32b Modifications

Patch GMRA*4*51 is part of the Computerized Patient Record System (CPRS) v32b updates.

This patch also implements NSR 20071211 which reduces the potential for patient allergy information to be overlooked by nurses, pharmacists, and physicians by making updates to the Adverse Reaction Tracking and Pharmacy VistA packages.

This patch also implements NSR 20100825 which improves drug-allergy order checking, which now considers the nuances of allergies recorded to multi-ingredient products, even when the reaction is likely only caused by one of the components. Drug-allergy order checks show all ingredients and the drug class associated with the entry in the allergy file, so that the ordering clinician can make a better-informed decision of whether to continue the prescription/order being placed.

#### GMRA*4*53 - CPRS V31.B - ART BUG FIXES

This patch resolves issues identified during the testing of CPRS v31.b as well as post-release issues with recently released patches.

#### GMRA*4*48 - Assessment Clean Up Utility

GMRA*4*48 installs the Assessment Clean Up Utility, allowing sites to identify and correct any discrepancies between the ADVERSE REACTION ASSESSMENT file (#120.86) and the PATIENT ALLERGIES file (#120.8).

A data discrepancy issue was discovered between the ADVERSE REACTION ASSESSMENT file (#120.86) and the PATIENT ALLERGIES file (#120.8). Specifically, a patient had a value of NO for the assessment and yet they had active reactions. The discrepancy could generate a hard error when attempting to process an Outpatient prescription.

When the patch is installed, the ‘B’ cross-reference for the ADVERSE REACTION ASSESSMENT file (#120.86) is re-indexed. The installer will be notified when the re-indexing is complete.

After the re-indexing is complete, the site should run the GMRA ASSESSMENT UTILITY option. *See Page 36 for further information.*

#### GMRA*4*46 Allergy Order Check Signs/Symptoms

This patch will enable the Adverse Reaction Tracking package to return additional data within the medication order check message to the Computerized Patient Record System (CPRS) and Pharmacy. This data includes the signs and symptoms of the reaction, the reaction’s severity and the item (ingredient or drug class) that was matched.

#### GMRA*4*42 - Progress Notes and Historical Allergy Entries

In the allergy package, a progress note is created whenever an observed drug allergy is entered for a patient.  That note is then added to the list of items to be signed when changing the patient or refreshing the patient's data.

Historical allergies, regardless of whether they are drug related or not, do not create progress notes.

During internal testing of another issue, it was discovered that a note can be associated, or appear to be associated, to an historical allergy entry.

At this point, any addition historical entries will appear to have a note associated with it.  In fact, what is happening is the same note is appearing on the "to be signed" list even though it may already be signed.  No new notes are created and the note stays associated with the correct patient and correct allergy.

After the installation of this patch, the system will correctly handle the creation of the progress note for observed entries and will no longer associate a progress note with an historical entry.

While testing this patch, it was discovered that the zero node of the XTMP global entry that stores data from the HDR isn't correctly set at the time the data is retrieved.  As a result, the daily clean-up process that clears out the XTMP global will not clear this data, which may cause an unnecessary buildup of data in XTMP.  The zero node will now be set correctly.

Related to the HDR work, the code that indicates when new allergy data should be sent to the HDR would sometimes stop processing due to a task manager issue.  The code has been modified to add a fail-safe so that if the data isn't sent to the HDR as a result of a task related error, a new task will be created to send the data.  Previously, manual intervention was required **.**

#### GMRA*4*41 - Pharmacy Encapsulation Changes

This patch converts GMRA routines to the new Pharmacy Encapsulation Cycle II APIs (Application Programmer Interfaces).  GMRA routines no longer read data directly from Pharmacy files 50.605, 50.416, 50.6.

#### GMRA*4*40 - Updating ANGIOTEN-Related Allergies

In patch GMRA*4*29, existing free text entries were updated in one of three ways.  The entry was either updated to a standardized term, marked   as entered in error, or left as free text with the phrase (FREE TEXT) appended to the term.

A group of terms that were included in the updated matrix that had the text ANGIOTEN in common were identified as needing to be updated to ACE INHIBITORS.  Of the 19 terms that fell into this group, 6 were correctly identified as needing to be updated to ACE INHIBITORS.  The other 13 terms should have been updated to either ANGIOTENSIN II INHIBITORS or should have been updated to free text if the existing term didn't provide enough information to accurately update it to a standardized term.

Prior to standardization, we were aware that there were about 50 allergies on file at all sites for the 19 "ANGIOTEN" based terms.  In addition, the ACE INHIBITORS and ANGIOTENSIN II INHIBITORS are in related classes (CV800 and CV805 respectively) which will cause drug class related order checks to fire when an allergy to either class is on file and an item from either class is ordered.

This patch will find any ANGIOTEN based allergies that were updated by patch 29 and update them to the correct term if need be.

In addition, the post-install will delete and rebuild the "B" cross-reference of the PATIENT ALLERGIES file (#120.8).  During installation of patch 29, a few sites reported problems with the post-install not completing.  It was discovered that a "B" cross-reference existed for an entry that was no longer in the file.  The "B" cross-reference will be deleted and rebuilt to ensure accuracy.

#### GMRA*4*38 - Add Allergy-Related Progress Note to CPRS Signature

Currently, when a new observed allergy is entered or an existing allergy is marked as entered in error a progress note is created.  When these actions are taken from within CPRS GUI the note is not added to the items requiring signature.  As a result, when the user is finished working with that patient the progress note is not displayed for signature as is expected.

The progress note is created outside of the context of CPRS and CPRS is therefore unaware of the fact that the progress note needs to be signed.

Beginning with CPRS v27 and the installation of this patch, CPRS will be made aware of the creation of the progress note and it will be added to the list of items to be signed when the patient record is exited or if the sign items action is taken.

Patch 38 also includes a post-install that will identify any allergy entries in the PATIENT ALLERGIES file (#120.8) that have an incorrect pointer value in the GMR ALLERGY field and convert it to a free text entry.  The installer will receive an email listing any entries that were updated.  The site will need to use the 'allergy clean up utility' to fix those entries.

#### GMRA*4*37 - Add Remote Data to Contrast Media Order Checks

Patch GMRA*4*26 introduced remote data interoperability (RDI) functionality so that remotely entered allergy data would be considered when determining if an order check should be produced.

Patch 26 only included functionality for pharmacy allergy order checking.  This patch will expand the RDI functionality to include remotely entered data when determining if there is a contrast media allergy when ordering radiological procedures.

Upon entering a radiological request that uses contrast, either from within the radiology package or within CPRS, an order check will be displayed if there is contrast media allergy data on file either locally or remotely.

Patch OR*3*267 includes updates to enhance the order check display and should be installed at the same time as this patch.  However, these patches can be installed independently of each other without any adverse effect.

#### GMRA*4*35 - Possible Problem with List by Location Unassessed

Add notation to code for option - List by Location of Undocumented

This report will show patients as not having received an assessment if the assessment was entered after the end date of the range.  For this reason, it is recommended to end the range

#### GMRA*4*36 - Remove Ability to Delete Allergy Records

Clear Quest/Remedy/PSIs

-----------------------

CQ 6683 - ID BAND marked question asked multiple times.  This question is now asked only one time per allergy entered.

CQ 8690 - ALLERGY TYPE (3.1) field in PATIENT ALLERGIES (120.8) file is not updated when the associated entry in the GMR ALLERGIES (120.82) file is changed.  Code has been modified so that when the ALLERGY TYPE (1) field in the GMR ALLERGIES (120.82) file is updated so is the same field in the PATIENT ALLERGIES (120.8) file.  In addition, the post-install routine GMRAY36 will make sure all GMR ALLERGIES (120.82) file entries are in synch.

CQ 12731 - An allergy assessment message is sent to the HDR when a user enters an up-arrow or blank return when prompted with the "does this patient have any allergies" prompt in the roll and scroll environment.  The system currently creates an entry in the ADVERSE REACTION ASSESSMENT file (120.86) before the user enters their response to the question.  If the user enters an up-arrow or hits return then the entry is deleted, which causes the HL7 message to be sent to the HDR.  The entry will now only be created after the user answers the question.

Files Updated

-------------

120.82 - GMR ALLERGIES, updated to have a new cross-reference so changes to the ALLERGY TYPE (1) field propagate through all allergy entries.  Also, the DRUG INGREDIENTS (4) multiple is modified so only primary ingredients can be chosen.

#### GMRA*4*34 - Update to HL7 Messages

In patch GMRA*4*23, routines were distributed to send HL7 messages containing allergy data to the Health Data Repository (HDR).  This patch adds a check for HL7 control characters that are embedded in text type data elements in the HL7 message and converts these control characters to the correct HL7 Escape Sequence.

**NOTE** You must suspend the VDEF Request Queue before installing this patch and then re-enable it after installation of the patch.  The steps for doing that are outlined in the installation instructions.

#### GMRA*4*33 - Prevent Test Patients From Appearing on Live Report

This patch will update the Adverse Reaction Tracking reports that display the patient name and/or SSN, and reports that produce counts of reaction data so that they all exclude test patients.

#### GMRA*4*31 - Check for Compiled Cross-References in File 120.8

In preparation for the installation of the data standardization related patches, sites needed to check to see if file 120.8 had compiled cross-references.

Patch GMRA*4*23, which installed the necessary data dictionary updates in support of the allergies data standardization, added some new cross-references to file 120.8.

In some cases, sites may have compiled the cross-references on file120.8.  If that is the case, then the cross-references that will be added by patch GMRA*4*23 won't be executed as a result of the compilation of the existing cross-references.

In general, the only sites that will have this problem are integrated sites.  In some cases, during the integration of the site's database, the cross-references for file 120.8 may have been compiled.  In order to ensure that file 120.8 does not have compiled cross-references this informational patch was provided to give directions on how to identify and fix this issue if it existed on a local system.

#### GMRA*4*30 - Prevent Deceased Patients from Appearing on Report

This patch addresses Remedy ticket HD67463, where deceased patients are appearing on the Patient Not Asked Report [GMRA PRINT-PATIENTS NOT ASKED].  The sites use this report to identify patients who have not had an allergy/adverse reaction assessment.  The sites then follow up with the patients on the list to get the allergy information.

By preventing deceased patients from appearing on this list, the sites will not be attempting to contact the family of a deceased individual for this assessment.

#### GMRA*4*29 - Automated Clean Up of Free Text Allergies

This patch will find all active free text allergies in the PATIENT ALLERGIES (120.8) file and will update the entry in one of three ways based on data in the conversion matrix.

#### GMRA*4*27 – Allergy Order Check Does Not Fire for Contrast Media

PSI-05-054 documents a patient safety issue due to allergy bulletin not being fired if the contrast media has a VA DRUG CLASS of DX109. Ticket is HD99674.  This patch corrects the problem.

#### GMRA*4.0*26 - Remote Data Interoperability (RDI) Update

GMRA*4.0*26 provides RDI the ability to use remote allergy data when determining drug-allergy order checks.

The remote data will come from the Health Data Repository (HDR) and that data will be used to determine if an order check should be given on the local system for the drug being ordered.

ART retrieves active allergies from HDR-Hx and HDR-IMS via a CPRS API call to CDS and includes those in the drug allergy-drug order checks performed on the local system for the drug being ordered.

#### GMRA*4.0*25 - Blank Sign/Symptom Problem

Patient Safety Issue - PSI-05-049 identifies a problem where an allergy may be stored without the corresponding drug classes or drug ingredients.  As a result, order checking may not occur as expected.

In version 25 of the GUI, a change was made to the way allergies are entered.  When the list of signs/symptoms is displayed on the form the site's top ten entries are listed first and then there's a space and a dashed line and another space.  It's possible for the user to accidentally select the dashed line or the space as a sign/symptom.  When this happens the system fails when attempting to store the allergy data.

With this update, the allergy package will no longer attempt to store non-existent signs/symptoms.

This patch also contains a post-installation routine that will attempt to identify any allergies that may not have been saved correctly.  Upon completion of the post-install, a report will be generated listing any patients and their associated allergies that need to be reviewed.  In general, the best course of action is to mark the existing allergy as entered in error and then re-enter the allergy information to make sure all required data is accounted for.

#### GMRA*4*24 - Update HDR Trigger Code

The logic used to determine when messages should be sent to the HDR is updated in this patch.  If the patient is a test patient or if a patient merge is occurring at the site, the allergy data will no longer be sent to the HDR.

#### GMRA*4.0*23 - HDR/DS Changes

This patch introduces the changes necessary to standardize the data stored in the allergy package.  Standardized data is necessary for inclusion in the Health Data Repository (HDR).

In addition, this patch introduces two new cross-references and a new Application Programmer Interface (API) that will allow changes to existing reactant terms to propagate through existing allergy entries in the PATIENT ALLERGIES file (120.8).

The GMR ALLERGIES file (120.82) and the SIGNS/SYMPTOMS file (120.83) are being standardized.  As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files.  In addition, users will no longer be able to add “free text” signs /symptoms.

##### Data Dictionary Changes

- Updated the reactant field to include all of the files that are searched (file 50 was missing)
- Removed the text related to free-text entries
- Changed the description for the OTHER REACTIONS field of the REACTIONS (S/S) multiple in anticipation of standardizing that file.  Once standardization is completed on file 120.83 (SIGNS/SYMPTOMS), then the OTHER REACTIONS field will no longer store “user entered text.”
- Changed the help text for the REACTIONS field of the REACTIONS multiple so that it doesn’t say to contact the nursing ADP coordinator to add new signs/symptoms.  It now says to contact the allergy coordinator to have the new term added (NTRT).

##### Mailman Changes

- Changed email message that is sent when a user attempts to add a free-text term indicating that the NTRT (new term rapid turnaround) process should be used.

##### GMRA Package (* Affects GUI Functionality)

- Updated cross-reference that allows for auto-updating of existing allergies when definitions related to the allergen are changed
- Updated file structures to support DS (field for VUID)
- Updated code to allow filtering of terms for DS (active/inactive) *
- Removal of the ability to add free text reactions *
- Updated code so that new local entries can no longer be added to the GMR ALLERGIES and SIGNS/SYMPTOMS files
- Changed routine so test patient data is not sent to the HDR (5 leading zeros)
- Incorporated messaging team changes to the HL7 messaging of data to the HDR
- The post-installation routine that converts existing free-text data to standardized terms if appropriate (#120.82 clean-up)
- Prohibit selecting a reactant from #50 *

#### GMRA*4.0*22 - HDR Application Installation

GMRA*4.0*22 was the second patch in support of the VistA Data Extraction Framework

(VDEF) effort, allowing changes to the PATIENT ALLERGIES (#120.8), ADVERSE

REACTION REPORTING (#120.85) and ADVERSE REACTION ASSESSMENT (#120.86) files to be transmitted to the HDR (Health Data Repository).

This patch added the infrastructure needed to create and send the HL7 messages to the HDR.

###### 

#### GMRA*4*21 - Removal of Allergies as Orders

**NOTE:** The following functionality is available only to sites that have installed patches OR*3.0*195, OR*3.0*216, and GMRA*4.0*21.  Sites that have not installed these patches will continue to receive the ART functionality that exists in CPRS GUI 24.

At sites that have installed the patches listed above, users can no longer enter allergies and adverse reactions as orders that are placed in the *ORDERS* file.  Patch OR*3.0*216 exports a modified order-dialog entry— *GMRAOR ALLERGY* —in the *ORDER DIALOG* file.  This entry enables CPRS to interact directly with the Adverse Reaction Tracking (ART) package (i.e., CPRS adds new allergies and adverse reactions directly into the ART package as users submit them.)

With supporting patches OR*3.0*216 and GMRA*4.0*21, CPRS GUI 25 does not display allergy information on the **Orders** tab.  It displays allergy information only on the **Cover Sheet** tab.  Nevertheless, users can still enter allergy information from the **Orders** tab by selecting **Allergies** in the **Write Orders** pane. (i.e., users can still go to a familiar place to enter allergies.)

In addition, users can no longer select **OTHER ALLERGY/ADVERSE REACTION** as a type of causative agent, nor can they select **OTHER REACTION** as a type of sign/symptom. Changes to the ART package have eliminated these items as choices.  These changes mark a continuing effort to end free-text and unspecific entries.  If type of causative agent’ references the field ALLERGY TYPE, the GUI interface does not allow the user to enter this information.  It is determined internally by the selection made during the Reactant lookup process.

Also, CPRS now requires users to enter information about the nature of the reaction that they are documenting ( **Allergy** , **Pharmacological** , or **Unknown** ).

Finally, CPRS GUI 24 introduced a dialog through which users can request that a causative agent be added to their site’s *ALLERGIES* file.  Users access this dialog via a warning that pops up when they attempt to enter a free-text causative agent.  The warning dialog asks users to indicate—by clicking either its **YES** or **NO** button—if they want to send a causative-agent inclusion request.  In CPRS GUI 24, the default button was **YES** .  In CPRS GUI 25, the default button is **NO** .  Furthermore, when users click the system **X** button (located in the top right-hand corner of each screen) to exit any of the screens that comprise the inclusion-request dialog, CPRS now cancels the request action.

#### GMRA*4*20 - Allergy Data Updates

This patch updates the free text utility that was distributed in patch GMRA*4*17 so that it can now be used to identify ingredient file based and drug class file-based allergies.

#### GMRA*4*19 - Notifications from CPRS When Allergies Are Added

This patch addressed a couple of issues related to the utility that was released in patch GMRA*4*17.  In addition, the sending of bulletins related to new allergy entry, need for verification, and need for marking chart/ID bands will now be done when entering an allergy from CPRS GUI.  Due to the change that will cause bulletins to be sent, sites should review all GMRA related mail groups to be sure they are correctly populated.

This patch also changes the order in which files that contain matching reactants appear to the user.  With patch GMRA*4*17, the names of the files that contained matching selections were displayed before the list of matches.  Although this helps identify the file from which you're choosing, users will still often pick the first match that they see.  Selections from the ingredient and drug class file, while legitimate, only supply partial information that is required for order checking to work.  As a result, the ingredient and drug class files were moved to the bottom of the selection list to encourage selection from one of the drug related files or the GMR ALELRGIES file (#120.82), which will provide complete information.

Changes in the order in which files appear in the tree view and the prohibition of free text entries for CPRS GUI will be released in v24 (patch OR*3.0*190).  Once v24 is installed, the entry of allergies will be consistent between the ART package and CPRS GUI.

This patch also includes a post-install that will review the VERIFIED field (#19) of the PATIENT ALLERGIES file (#120.8) for null entries.  A previous patch fixed a problem with the VERIFIED field being incorrectly set to null but did not update entries affected by this problem.  The post-install will compare the allergy against the site's auto-verification settings and either mark the allergy as verified or mark it as not verified.  For those entries marked as not verified, the sites can use standard allergy options to verify the remaining allergy entries.  Each entry that is updated by this process will have a comment indicating that the entry was auto-updated by the patch 19 post-install.  In addition, a mail message will be sent to the installer when the post-install finishes to let them know how many entries were reviewed and how many were updated.

#### GMRA*4.0*18 - HDR/VistA Data Extraction Framework (VDEF) Updates

This patch installed the necessary "triggers" to identify when data should be sent to the HDR.

###### 

#### GMRA*4.0*17 - Free Text Allergy Clean Up Utility

Patch GMRA*4.0*17 provided a utility to help sites identify and fix allergy entries that have free-text reactants.  With this patch, free-text entries are no longer allowed from within the Allergy Tracking package.  A subsequent patch to CPRS prevents free-text entries from within CPRS as well.

Lower-case entries are also no longer allowed. Previously, lower-case entries could be added to the GMR ALLERGIES file (120.82).  A post-installation routine will identify any local entries and update the entries to upper-case.  Synonyms will also be checked and converted to upper-case, if required.

A new mail group, GMRA REQUEST NEW REACTANT, is added with this patch.  Sites should populate this mail group with the people responsible for addressing requests to add new reactants.  If users attempt to enter a reactant that is not found during the look-up process, they are asked if they would like to send an email requesting the addition of the new reactant.  The request can then be reviewed for accuracy and new local entries can be added, if appropriate.  Previously, users were asked if they wanted to add the new entry and it was immediately available in the patient’s record. Under the new system, the new reactant must be reviewed before it is added to the patient’s record.

### Overview of Adverse Reaction Tracking Functionality

The four major components of the package are:

Data Entry Options - Adverse Reaction Tracking has two options where a user can enter data.

1. Enter/Edit Patient Reaction Data - This option allows the clinical users (i.e., doctors, nurses, other clinicians and clerks) to enter data into ART.
2. Verify Patient Reaction Data - This option allows the verifiers designated by ART to verify the correctness of data entered by the clinical users into ART.  This option does NOT perform evaluation of suspected Advanced Drug Reactions (ADR) as described in Section 5.a.(2).(d) of Directive 10- 92-070.

Reporting options - These options report the patient causative agent data to the user via a print option.  Also, this data is made available to other software applications via a data extract utility.

Enter/Edit Site Configurable Files - This menu allows the various site configurable files to be modified to allow ART to better meet the needs of an individual site.

Adverse Drug Reaction (ADR) options - These options support implementation of Directive 10-92-070.  It allows for the evaluation of a suspected ADR by a qualified individual (e.g., clinical pharmacist, clinical pharmacologist) other than the attending physician, as specified in Section 5.a.(2).(d) of Directive 10-92-070.  This component also generates the reports needed by the FDA.

There are four major users of the software:

Clinical Users - These are the doctors, nurses, other clinicians, and clerks entering the data into ART.  They are required to enter data pertinent for a particular allergy/adverse reaction.  If the allergy/adverse reaction was observed at the site, data pertaining to any possible legal action could be tracked.  This data is then available to users of any service through the Reporting options, thus avoiding any errors in care.  Two other data elements that are tracked are the date/time that the patient chart was marked and the date/time that the patient ID band was marked, indicating the patient’s reaction to the particular causative agent.  Automated mail bulletins are sent to the appropriate users when the date/time patient chart marked data field has not been recorded.

Verifiers - These are users designated by the site to verify the correctness of the data in ART.  The verifiers are designated when the Information Resources Management Service (IRM) allocates the GMRA-ALLERGY VERIFY security key to a user and assigns the ART Verifier Menu.  The verifiers may be clinical pharmacists, dietitians, or other clinical personnel.  Automated mail bulletins are sent to the ART verifiers when an allergy/adverse reaction has been entered and signed (completed) by a user.  Verification may be important in observed instances of adverse drug reactions where a Quality Assurance (QA) investigation may be conducted.  In general, it is a good principle to have someone verify all of the data entered into ART.

Pharmacy and Therapeutics (P&amp;T) Committee users - These users are the members of the hospital's P&amp;T Committee and are assigned the P&amp;T Committee Menu option.  They use the information in ART to review Adverse Drug Reactions (ADRs) in the hospital, classify them as significant reactions and determine whether they are related to particular drugs, and depending on the severity of the ADRs, may report them further to the FDA.  A printed copy of the form used to report to the Food and Drug Administration (FDA) can be generated by ART.  Automated mail bulletins are sent to the P&amp;T Committee users when an observed drug reaction is entered into the system.

Software developers - These users use the data extract utility (GMRADPT routine) to gather ART data for display within their specific **V** *IST* **A** application.

### Implementation and Maintenance

There are several important considerations for the Application Coordinator (ADPAC) or IRM support person to consider following installation of this software.  They include editing site parameters, assigning menus to users, and assigning security keys.

#### Site Parameters

The Enter/Edit Site Configurable Files menu [GMRA SITE FILE MENU] has six options that the site can use to customize and maintain their use of the software:

1     Edit Allergy File

2     Enter/Edit Signs/Symptoms Data

3     Enter/Edit Site Parameters

4     Sign/Symptoms List

5     Allergies File List

6     Allergies Clean Up Utility

#### Edit Allergy File

[GMRA ALLERGY FILE EDIT]

#### Enter/Edit Signs/Symptoms Data

[GMRA REACTION FILE EDIT]

The GMR ALLERGIES file (#120.82) and the SIGNS/SYMPTOMS file (#120.83) are being standardized.  As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files.  In addition, users will no longer be able to add "free text" signs/symptoms.

#### Enter/Edit Site Parameters

**[GMRA SITE FILE]**

The Enter/Edit Site Parameters option allows site configuration for multiple divisions at the site.  The software provides a generic site configuration entry called HOSPITAL.  The site can customize this entry to fit its needs.  These parameters are stored in the GMR Allergy Site Parameters file (#120.84).

The site can configure the following:

1. The list of the ten most common signs/symptoms the user will see.

2.     The autoverification of data. Autoverification is the process by which the software automatically changes the status of the data to verified when the user who entered the data signs off (completes) on it.  The site can determine which of the types of reactions are to be auto-verified and which are to follow the normal verification procedure.

Three parameters are used to auto-verify data:

- Auto-verify Food/Drug/Other
- Auto-verify Observed/Historical
- Auto-verify Logical Operator

The verification of data is important.  Minimally, all drug reactions will need verification.  Depending on the site, food and other allergies may also need to be verified.  The users who will verify the data must have the GMRA-ALLERGY VERIFY security key.

3.     Whether the originator of the data should provide comments.

4.      Whether the site documents the marking of a patient’s ID band or chart to indicate the presence of an allergy/adverse reaction.  There are four parameters with regards to this documentation; Mark ID Band, Flag Method of Notification, Alert ID Band/Chart Mark, and Send Chart Mark Bulletin for New Admissions.

5.	FDA reporting data.  The site can choose to require the user to enter FDA data at the time a reaction is entered.  Also, the site may edit the reporter information that will appear on the FDA Adverse Reaction reports.

6.     Whether to allow comments to be added to the reaction data that is entered in error.  This allows the user to indicate why the data is incorrect.

**Example** :

Select Enter/Edit Site Configurable Files Option: **3** Enter/Edit Site Parameters

Select GMR ALLERGY SITE PARAMETERS NAME: **??**

HOSPITAL

You may enter a new GMR ALLERGY SITE PARAMETERS, if you wish

This field is the name of this set of parameters.  The name of the base

set that is sent out is "HOSPITAL".  The code will work more efficiently

if the name of the base set of parameters is not changed from "HOSPITAL"

.

Select GMR ALLERGY SITE PARAMETERS NAME: HOSPITAL

NAME: HOSPITAL// (No editing)

Select DIVISION: SALT  CITY OIFO// **?**

Answer with DIVISION

Choose from:

HINES ISC

ELY

SALT  CITY OIFO

You may enter a new DIVISION, if you wish

Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

OFFICIAL VA NAME, or CURRENT LOCATION, or CODING SYSTEM/ID PAIR, or

NAME (CHANGED FROM), or CODING SYSTEM

Do you want the entire INSTITUTION List? **N** (No)

Select DIVISION: SALT  CITY OIFO// **&lt;Enter&gt;**

The following are the ten most common signs/symptoms:

1. CHILLS                          6. DIARRHEA

2. ITCHING,WATERING EYES           7. HIVES

3. HYPOTENSION                     8. DRY MOUTH

4. DROWSINESS                      9. DRY NOSE

5. NAUSEA,VOMITING                10. RASH

Enter the number of the sign/symptom that you would like to edit: **??**

ENTER THE CORRECT NUMBER (1-10) OF THE SIGN/SYMPTOM TO BE EDITED

Enter the number of the sign/symptom that you would like to edit: **6**

REACTION: DIARRHEA// ??

One of the ten most commonly selected reactions.

Choose from:

AGITATION        NATIONAL SIGN/SYMPTOM

AGRANULOCYTOSIS        NATIONAL SIGN/SYMPTOM

ALOPECIA        NATIONAL SIGN/SYMPTOM

ANAPHYLAXIS        NATIONAL SIGN/SYMPTOM

ANEMIA        NATIONAL SIGN/SYMPTOM

ANOREXIA        NATIONAL SIGN/SYMPTOM

ANXIETY        NATIONAL SIGN/SYMPTOM

APNEA        NATIONAL SIGN/SYMPTOM

APPETITE,INCREASED        NATIONAL SIGN/SYMPTOM

ARRHYTHMIA        NATIONAL SIGN/SYMPTOM

ASTHENIA        NATIONAL SIGN/SYMPTOM

ASTHMA        NATIONAL SIGN/SYMPTOM

ATAXIA        NATIONAL SIGN/SYMPTOM

ATHETOSIS        NATIONAL SIGN/SYMPTOM

BRACHYCARDIA        NATIONAL SIGN/SYMPTOM

BREAST ENGORGEMENT        NATIONAL SIGN/SYMPTOM

BRONCHOSPASM        NATIONAL SIGN/SYMPTOM

CARDIAC ARREST        NATIONAL SIGN/SYMPTOM

CHEST PAIN        NATIONAL SIGN/SYMPTOM

**^**

REACTION: DIARRHEA// **AGITATION** NATIONAL SIGN/SYMPTOM

The following are the ten most common signs/symptoms:

1. CHILLS                          6. AGITATION

2. ITCHING,WATERING EYES           7. HIVES

3. HYPOTENSION                     8. DRY MOUTH

4. DROWSINESS                      9. DRY NOSE

5. NAUSEA,VOMITING                10. RASH

Enter the number of the sign/symptom that you would like to edit: **&lt;Enter&gt;**

AUTOVERIFY FOOD/DRUG/OTHER: NO AUTOVERIFY// **??**

This field determines which types of allergies a site wants autoverified

at the user sign off.

Choose from:

0        NO AUTOVERIFY

1        AUTOVERIFY DRUG ONLY

2        AUTOVERIFY FOOD ONLY

3        AUTOVERIFY DRUG/FOOD

4        AUTOVERIFY OTHER ONLY

5        AUTOVERIFY DRUG/OTHER

6        AUTOVERIFY FOOD/OTHER

7        AUTOVERIFY ALL

AUTOVERIFY FOOD/DRUG/OTHER: NO AUTOVERIFY// **&lt;Enter&gt;**

AUTOVERIFY OBSERVED/HISTORICAL: NO AUTOVERIFY// **??**

This field is configurable by the site to allow autoverification of

observed or historical allergies.

Choose from:

0        NO AUTOVERIFY

1        AUTOVERIFY HISTORICAL ONLY

2        AUTOVERIFY OBSERVED ONLY

3        AUTOVERIFY BOTH

AUTOVERIFY OBSERVED/HISTORICAL: NO AUTOVERIFY//

AUTOVERIFY LOGICAL OPERATOR: OR// ??

This field will determine how the Autoverify Food/Drug/Other and

Autoverify Observed/Historical parameters relate to each other.  OR means

that the reaction will be autoverified if it meets the criteria of one of

the two parameters, while AND means the reaction will be autoverified only

if it meets the criteria of both parameters.  If this field is left null,

the OR condition will be used.

For example, if you want to verify only observed drug reactions, you would

set the Autoverify Food/Drug/Other parameter to AUTOVERIFY FOOD/OTHER

and the Autoverify Observed/Historical to AUTOVERIFY HISTORICAL ONLY

, and the

Autoverify Logical Operator to OR.  This means that a reaction that has

a type of Food/Other OR is Historical will be autoverified, thus leaving

observed drug reactions to be verified.

Another example would be if you wanted to verify all observed reactions

and all drug reactions whether observed or historical.  The parameters

should be set accordingly:  Autoverify Food/Drug/Other to AUTOVERIFY

FOOD/OTHER, Autoverify Observed/Historical to AUTOVERIFY HISTORICAL ONLY and

Autoverify Logical Operator to AND.  In this case to be autoverifed, a

reaction has to have a type of Food/Other AND it must be Historical, all

other reactions will need to be verified.

Choose from:

!        OR

&amp;        AND

AUTOVERIFY LOGICAL OPERATOR: OR// **&lt;Enter&gt;**

REQUIRE ORIGINATOR COMMENTS: NO// **??**

This field indicates whether the originator will be required to enter

comments for an OBSERVED reaction.

Choose from:

0        NO

1        YES

REQUIRE ORIGINATOR COMMENTS: NO// **&lt;Enter&gt;**

MARK ID BAND FLAG: YES// **??**

This field is an indicator to denote whether the site wants

to document if the patient ID band should be marked for

a certain allergy.

The system will assume the site wants to document the marking of inpatient

ID bands.  If this field is answered NO, the site does not want to

document the marking of inpatient ID bands.

Choose from:

0        NO

1        YES

MARK ID BAND FLAG: YES// **&lt;Enter&gt;**

METHOD OF NOTIFICATION: BULLETIN// **??**

This field tells ART if or how the users should be notified for chart

or ID band markings.  There are three methods. The first method is the

use of BULLETINs,  which is the current way ART works.  The

second method is the use of OE/RR Teams.  If this method is used, then

you will need to set up different teams for each ward and also assign

printers to these teams.  The third method is to turn off the function.

Choose from:

0        BULLETIN

1        OE/RR TEAMS

2        NO NOTIFICATION

METHOD OF NOTIFICATION: BULLETIN// **&lt;Enter&gt;**

ALERT ID BAND/CHART MARK: YES// **??**

This field is to let the system know if you want to issue alerts

if the fields have not been answered in the Enter/Edit Patient Reaction

Data portion of the system.  If the field is answered yes(1) or is null

then, the system will continue to issue the alerts.  If this field is

no(0), then the system will not issue alerts for this record.

Choose from:

1        YES

0        NO

ALERT ID BAND/CHART MARK: YES// **&lt;Enter&gt;**

SEND CHART MARK BULLETIN FOR NEW ADMISSIONS: YES// **??**

This is to indicate if the site wants to send chart mark bulletin

for a new admission.

Choose from:

1        YES

0        NO

SEND CHART MARK BULLETIN FOR NEW ADMISSIONS: YES// **&lt;Enter&gt;**

FDA DATA REQUIRED: YES// ??

This field will indicate whether the entry of FDA Data should be required

during the Enter/Edit Patient Reaction Data.  If this field is answered "YES",

then the user must enter the FDA Data at the time of entering a reaction.

If this field is left null or answered "NO", then the FDA Data entry will

not be required during the Enter/Edit Patient Reaction Data option.

Choose from:

y        YES

n        NO

FDA DATA REQUIRED: YES// **&lt;Enter&gt;**

ENABLE COMMENTS FIELD FOR REACTIONS THAT ARE ENTERED IN ERROR: NO

// **??**

Permit users to indicate why a reaction was Entered in Error.

Choose from:

1        YES

0        NO

ENABLE COMMENTS FIELD FOR REACTIONS THAT ARE ENTERED IN ERROR: NO

// **&lt;Enter&gt;**

REPORTER NAME:

ADDRESS:

CITY:

STATE:

ZIP:

PHONE:

OCCUPATION:

Do you want to edit Reporter Information shown above? No// **&lt;Enter&gt;** (No)

1      Edit Allergy File

2      Enter/Edit Signs/Symptoms Data

3      Enter/Edit Site Parameters

4      Sign/Symptoms List

5      Allergies File List

6      Allergy clean up utility

You have PENDING ALERTS

Enter  "VA to jump to VIEW ALERTS option

Select Enter/Edit Site Configurable Files Option:

Reporter information will appear on FDA reports generated by the software.  This information may be left blank.  The user will be prompted for the reporter information when creating an FDA report.

#### Sign/Symptoms List

**[GMRA PRINT SIGN/SYMPTOMS LIST]**

The Sign/Symptoms List option prints a listing of all or selected signs/symptoms, with the national or local classification and synonym (when there is one) of each sign/ symptom.  This option can be a useful tool for the ADPAC to maintain the Sign/Symptoms file (#120.83).

**Example** :

Select Enter/Edit Site Configurable Files Option: **4** Sign/Symptoms List

START WITH NAME: FIRST// **&lt;ret&gt;**

DEVICE: (Enter a printer name for a hard copy or &lt;ret&gt; to bring the output to your screen)

SIGN/SYMPTOMS LIST                               PAGE 1

NAME                            Nat'l/Local  SYNONYM

-----------------------------------------------------------------------

AGITATION                       National

AGRANULOCYTOSIS                 National

ALOPECIA                        National

ANAPHYLAXIS                     National

ANEMIA                          National

ANOREXIA                        National

ANXIETY                         National     ANX

APNEA                           National

APPETITE,INCREASED              National

ARRHYTHMIA                      National

ASTHENIA                        National

ASTHMA                          National

ATAXIA                          National

ATHETOSIS                       National

BRACHYCARDIA                    National

BREAST ENGORGEMENT              National

BRONCHOSPASM                    National

CARDIAC ARREST                  National

CHEST PAIN                      National

CHILLS                          National

COMA                            National

CONFUSION                       National

CONGESTION,NASAL                National

CONJUNCTIVAL CONGESTION         National

CONSTIPATION                    National

COUGHING                        National

DEAFNESS                        National

DELERIUM                        National

DELUSION                        National

DEPRESSION                      National

DEPRESSION,MENTAL               National

DEPRESSION,POSTICTAL            National

...

#### Allergies File List

**[GMRA PRINT ALLERGIES LIST]**

This option prints a captioned list of all entries in the GMR Allergies file (#120.82).  The list is sorted alphabetically by NAME.  The user may list all entries by accepting the default answer “FIRST” to the “START WITH NAME” prompt or may select a subset to print.  The list contains the allergy name, type, whether it is a nationally distributed entry, synonyms if any, VA Drug Class if applicable, and drug ingredients if applicable.  This option is meant to be a helpful tool for maintaining the GMR Allergies file.

**Example**

Select Enter/Edit Site Configurable Files Option: **5** Allergies File List

START WITH NAME: FIRST// **&lt;ret&gt;**

DEVICE: (Enter a printer name for a hard copy or &lt;ret&gt; to bring the output to your screen)

GMR ALLERGIES LIST                                   PAGE 1

-----------------------------------------------------------------------------

NAME: ADHESIVE TAPE                     ALLERGY TYPE: OTHER

NATIONAL ALLERGY: NATIONAL ALLERGY

NAME: ALCOHOL                           ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

DRUG INGREDIENT: ALCOHOL

NAME: ANIMAL HAIR                       ALLERGY TYPE: OTHER

NATIONAL ALLERGY: NATIONAL ALLERGY

NAME: ANISE OIL                         ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

DRUG INGREDIENT: ANISE OIL

NAME: ANTIRABIES SERUM                  ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

VA DRUG CLASSES: IM400

DRUG INGREDIENT: ANTIRABIES SERUM

NAME: ASCORBIC ACID                     ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

VA DRUG CLASSES: VT400

DRUG INGREDIENT: ASCORBIC ACID

NAME: ASPARTAME                         ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

SYNONYM: NUTRA SWEET

DRUG INGREDIENT: ASPARTAME

NAME: ASPIRIN                           ALLERGY TYPE: DRUG, FOOD

NATIONAL ALLERGY: NATIONAL ALLERGY

VA DRUG CLASSES: MS101

DRUG INGREDIENT: ASPIRIN

...


#### Allergy Clean-up Utility

This utility will identify either free text reactants, ingredient-based reactants or drug class-based reactants.  The user will then be allowed to either update the reactant to a more appropriate choice or they can mark it as entered in error.

Select Enter/Edit Site Configurable Files &lt;TEST ACCOUNT&gt; Option: 6  Allergy clean up utility

Select one of the following:

1         Free Text

2         Ingredient

3         Drug Class

Select the list you wish to work with:

#### Free Text Allergy Clean Up Utility

Patch GMRA*4.0*17 provided a utility to help sites identify and fix allergy entries that have free-text reactants.

With this patch, free-text entries are no longer allowed from within the Allergy Tracking package.  A subsequent patch to CPRS prevents free-text entries from within CPRS as well.

Lower-case entries are also no longer allowed.  Previously, lower-case entries could be added to the GMR ALLERGIES file (#120.82).  A post-installation routine will identify any local entries and update the entries to upper-case.  Synonyms will also be checked and converted to upper-case, if required.

A new mail group, GMRA REQUEST NEW REACTANT, is added with this patch.  Sites should populate this mail group with the people responsible for addressing requests to add new reactants.  If users attempt to enter a reactant that is not found during the look-up process, they are asked if they would like to send an email requesting the addition of the new reactant.  The request can then be reviewed for accuracy and new local entries can be added, if appropriate.  Previously, users were asked if they wanted to add the new entry and it was immediately available in the patient’s record.  Under the new system, the new reactant must be reviewed before it is added to the patient’s record.

When you start the utility, a list of currently existing free-text entries is displayed in alphabetical order.  This list may take a few minutes to generate, as all existing entries need to be evaluated to determine which ones are “free text.”  The list shows the name of the reactant and the number of entries for that reactant.  In most cases, they will be unique, but there will be some that have many entries (such as an entry for NO KNOWN ALLERGIES).

When entering the utility, any users who are currently working in the utility will be listed.  If users are listed as working with the utility, you will not be allowed to update the list.  You can only update the list when nobody else is working in the utility.

Once the list is displayed, you can do three things:

1. Mark the entry as entered in error
2. Update it so that it points to an existing reactant (hopefully, the one that it should have been pointed to originally).
3. Add new reactants to the GMR ALLERGIES file (120.82) as local entries, if they are not found in any existing files.
<!-- image -->

#### Detailed Display

The detailed display window shows the patient name and the list of currently active allergies, separated by a tilde (~).  This way, you can quickly look and see if the patient already has an active allergy that is the same as the free-text entry.  In this case, you would mark it as entered in error.

The “free text detailed display” action lets you see a FileMan inquiry-style listing of the free text entry for selected patient(s).  You'll now be able to see the comments, reactions, and other associated information for the free text entry that you're fixing.

When doing a group update or selecting multiple patients for updating from the detailed display listing, the reactant you select for the first patient in the list will become the default for the remaining patients.  The exception to that would be if you decide to not accept the default while updating one of the patients.  In that case, the last chosen reactant will become the default for the next patient.  The default only holds while working with a particular group.  Once you select a new reactant group or a new group of patients, you must re-select the reactant.  This should cut down on the amount of time needed in selecting the reactant for each patient.

1. Select the Free text allergy clean up utility [GMRA FREE TEXT UTILITY] from the GMRA SITE FILE MENU.

Select the number of a reactant first, and then select DD to see details about the reactant.  (Alternatively, you can select the action, DD, and then select the number of the reactant.)

**NOTE:** For detailed display, you can only select one group at a time.

GMRA SITE FILE MENU     Enter/Edit Site Configurable Files menu

1      Edit Allergy File

2      Enter/Edit Signs/Symptoms Data

3      Enter/Edit Site Parameters

4      Sign/Symptoms List

5      Allergies File List

6      Free text allergy clean up utility

You have PENDING ALERTS

Enter  "VA to jump to VIEW ALERTS option

Select Enter/Edit Site Configurable Files Option: **6** Free text allergy clean up

utility

Building list of free text allergies...this may take a few minutes

**Allergy Tracking Update** Oct 24, 2003@15:09:28          Page:    1 of    1

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   COCA COLA SYRUP 8OZ                            1

2   Diabetes Mellitus Type II                      1

3   NO ALLERGIES                                   1

4   NO KNOWN ALLERGIES                             1

5   Penicillin                                     1

6   PIZZA                                          1

**7   POLLEN ANTIGEN MIX                             1**

**+         Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Next Screen// 3

**Allergy Tracking Update** Oct 24, 2003@15:09:28          Page:    1 of    1

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   COCA COLA SYRUP 8OZ                            1

2   Diabetes Mellitus Type II                      1

3   NO ALLERGIES                                   1

4   NO KNOWN ALLERGIES                             1

5   Penicillin                                     1

6   PIZZA                                          1

7   POLLEN ANTIGEN MIX                             1

**+         Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Next Screen// **DD** Detailed Display

**Reactant Detailed Display** Oct 24, 2003@15:09:28          Page:    1 of    1

Patient listing for reactant CEFAZOLIN SOD 1GM INJ

Patient Name                   Last 4

1   REDACTED	                   REDACTED

Allergies: PENICILLIN VK ORAL SOLUTION~AMIKACIN~PEANUT OIL~CORTISONE~NUTS~DUST~

STRAWBERRIES~CHICKEN~CHOCOLATE~PHENOL~HAYFEBROL SF~ASA~BILE SALTS~

BILBERRY EXTRACT~POLLEN~POLLEN ALLERGENIC EXTRACT~

ANTIHEMOPHILIC FACTOR,HUMAN~CEFAZOLIN SOD 1GM INJ~SHELL FISH~

RANITIDINE

**Select a patient**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Free Text Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit// **DD** Free Text Detailed Display

Select Entries from list: **1**

PATIENT: BABBIT,VERONA                  REACTANT: CEFAZOLIN SOD 1GM INJ

GMR ALLERGY: OTHER ALLERGY/ADVERSE REACTION

ORIGINATION DATE/TIME: OCT 02, 2003@14:02

ORIGINATOR: NABER,DAVID A             OBSERVED/HISTORICAL: HISTORICAL

ORIGINATOR SIGN OFF: YES              NATURE OF REACTION: UNKNOWN

VERIFIED: NO                          ALLERGY TYPE: DRUG

Press return to continue or '^' to stop: **&lt;Enter&gt;**

##### Mark Entered in Error

You can mark an entire group as entered in error from this opening screen.  Upon marking the reaction as entered in error, a check is made to see if there are still active reactions for the patient.  If there are not any, then you are prompted to enter an updated assessment for the patient.

1. Select the Free text allergy clean up utility [GMRA FREE TEXT UTILITY] from the GMRA SITE FILE MENU.
2. Select the number of the reactant(s) you wish to mark as entered in error.  (Alternatively, you can select the action, Mark Entered in Error, and then select the number of the reactant(s).)

Select Enter/Edit Site Configurable Files Option: **6** Free text allergy clean up

utility

Building list of free text allergies...this may take a few minutes

**Allergy Tracking Update** Sep 19, 2003@11:18:04             Page:    1 of    4

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   COCA COLA SYRUP 8OZ                            1

2   COLD AIR                                       1

3   Diabetes Mellitus Type II                      1

4   DOG HAIR                                       1

5   DONUTS                                         1

6   DOUGH                                          1

7   DR P'S SNAKE OIL ELIXIR                        1

8   DRUGS                                          1

9   EIEIO                                          1

10  ENCAINIDE 25MG                                 1

**Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Quit// **5**

**3.** Type EE for Mark entered in error, and then answer Yes to confirm that you want to mark ALL allergies as entered in error.

Select Item(s): Next Screen// **EE** Mark entered in error

You are about to mark ALL allergies with the selected reactant

as entered in error.

ARE YOU SURE? NO// **Yes**

#### Update to New Reactant

You may select and update groups of entries from the opening menu; however, it is recommended that you use the detailed display option to review entries in a group before doing a mass update. ***Changes cannot be undone*** !  When the entry is updated, a comment is stored in the PATIENT ALLERGY file indicating who made the change, date/time of change, and a comment that indicates what the previous value was and what the new value is.  In addition, the new reactant is compared against current orders and order checking information is returned, if appropriate.  When a new reactant is selected, checks are made for duplicate entries and previously entered-in-error information.

NOTE: Due to the way the order checking software works, you may get “false positives.”  In other words, if the patient currently has an allergy order check for some other order not related to this new reactant, you may still see the order check.

Finally, the drug ingredient/drug class information is updated, if appropriate.

1. Select the Free text allergy clean up utility [GMRA FREE TEXT UTILITY] from the GMRA SITE FILE MENU.
2. Select a reactant number and then select the action DD.

Select Enter/Edit Site Configurable Files Option: **6** Free text allergy clean up

utility

Building list of free text allergies...this may take a few minutes

**Allergy Tracking Update** Oct 27, 2003@08:35:56          Page:    1 of    1

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   CEFAZOLIN SOD 1GM INJ                          1

2   Diabetes Mellitus Type II                      1

3   NO ALLERGIES                                   1

4   NO KNOWN ALLERGIES                             1

5   Penicillin                                     1

**6   WATERMELON                                     3**

**Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Quit// **6**

**Allergy Tracking Update** Oct 27, 2003@08:36:38          Page:    1 of    1

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   CEFAZOLIN SOD 1GM INJ                          1

2   Diabetes Mellitus Type II                      1

3   NO ALLERGIES                                   1

4   NO KNOWN ALLERGIES                             1

5   Penicillin                                     1

6   WATERMELON                                     3

**+         Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Quit// **dd** Detailed Display

**Reactant Detailed Display** Oct 27, 2003@08:25:50          Page:    1 of    1

Patient listing for reactant WATERMELON

Patient Name                   Last 4

1   BENOIT,JEAN                     8847

Allergies: WATERMELON

2   ARMSTRONG,BJ                    8989

Allergies: WATERMELON

3   BAXTER,NATHAN                   8840

**Allergies: ASPIRIN~WATERMELON**

**+         Select one or more entries**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Free Text Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit// **1**

**3.** Select an item # in the Detailed Display, then select  for Update to New Reactant.

**Reactant Detailed Display** Oct 27, 2003@08:40:29          Page:    1 of    1

Patient listing for reactant WATERMELON

Patient Name                   Last 4

1   REDACTED                     REDACTED

Allergies: WATERMELON

2   REDACTED                     REDACTED

Allergies: WATERMELON

3   REDACTED                     REDACTED

Allergies: ASPIRIN~WATERMELON

**Select a patient                                                  &gt;&gt;&gt;**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Free Text Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit// **ur** Update to new reactant

You are about to update the selected patient's

WATERMELON allergy to a new reactant.

ARE YOU SURE? NO// **YES**

For patient BENOIT,JEAN

Enter Causative Agent: **ONION**

Checking GMR ALLERGIES (#120.82) file for matches...

Now checking INGREDIENT (#50.416) file for matches...

EXTRACT

...OK? Yes// **&lt;ENTER&gt;** (Yes)

You selected ONION EXTRACT

Is this correct? Y// **&lt;ENTER&gt;** ES

Performing order checking...No problems found

Press enter to continue: **&lt;ENTER&gt;**

Reactant Detailed Display     Oct 27, 2003@08:44:13          Page:    1 of    1

Patient listing for reactant WATERMELON

Patient Name                   Last 4

1   REDACTED                    REDACTED

Allergies: WATERMELON

2   REDACTED                   REDACTED

Allergies: ASPIRIN~WATERMELON

**Select a patient                                                  &gt;&gt;&gt;**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Free Text Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit//

#### Add/Edit Patient Reaction

This action allows you to add/edit patient reactions.  This allows reviewers using the utility to add a new reaction if you receive a free-text reaction such as MORPHINE, PENICILLIN.  When you correct this type of entry, you can only make it be one or the other.

**Reactant Detailed Display** Sep 19, 2003@13:05:28          Page:    1 of    1

Patient listing for reactant DIABETES MELLITUS TYPE II

Patient Name                   Last 4

1   REDACTED				REDACTED

Allergies: AMOXICILLIN~ASPIRIN~MILK~ERYTHROMYCIN~CHROMA-PAK INJECTION~

Diabetes Mellitus Type II~PENICILLINS

**Select a patient**

**EE  Entered in Error                    PR  Add/Edit Patient Reaction**

**UR  Update to new reactant              DD  Free Text Detailed Display**

**AE  Add/Edit Allergy File**

Select Item(s): Quit// **PR** Add/Edit Patient Reaction

You should use this option to add NEW reactions only.  If you mark

existing free text entries as entered in error from within this option it will

not update the utility's display until the list is rebuilt upon re-entry

of this option.  This could cause confusion as the list will no longer

be accurate.

Press enter to continue: **&lt;Enter&gt;**

Select PATIENT NAME:    ABC,PATIENT           222324321     YES     ACTIVE DUTY

Enrollment Priority:            Category: IN PROCESS    End Date:

OBS/

REACTANT                                             VER.   MECH.   HIST  TYPE

--------                                             ----  -------  ----  ----

ALUMINUM ACETATE                                     AUTO  UNKNOWN  HIST  DRUG

Reactions: CHILLS

AMOXICILLIN                                           NO   UNKNOWN  HIST  DRUG

AMPICILLIN                                            NO   UNKNOWN  HIST  DRUG

CARAMEL                                              YES   ALLERGY  HIST  DRUG

Reactions: HIVES, ITCHING,WATERING EYES

CN900                                                YES   ALLERGY  HIST  DRUG

(AMITRIPTYLINE, PERPHENAZINE)

Reactions: ITCHING,WATERING EYES, ANXIETY,

DRY MOUTH

HAYFEBROL SF                                          NO   UNKNOWN  HIST  DRUG

(CALCIUM PHOSPHATE, CELLULOSE, CHLORPHENIRAMINE,

MAGNESIUM STEARATE, POVIDONE, PSEUDOEPHEDRINE,

SODIUM STARCH GLYCOLATE)

Reactions: ITCHING,WATERING EYES

LOMEFLOXACIN                                         YES   UNKNOWN  OBS   DRUG

Reactions: ITCHING,WATERING EYES

PENICILLINS                                           NO   UNKNOWN  HIST  DRUG

Press RETURN to continue or '^' to stop listing:

OBS/

REACTANT                                             VER.   MECH.   HIST  TYPE

--------                                             ----  -------  ----  ----

PENTAMIDINE                                          YES   ALLERGY  HIST  DRUG

PENTAZOCINE                                          YES   ALLERGY  HIST  DRUG

RANITIDINE                                           AUTO  UNKNOWN  OBS   DRUG

(CITRIC ACID, SODIUM CHLORIDE, SODIUM PHOSPHATE)

Reactions: CHILLS

TAPE                                                  NO   UNKNOWN  HIST  DRUG

TAVIST                                                NO   UNKNOWN  HIST  DRUG

(CLEMASTINE)

TAVIST                                                NO   UNKNOWN  HIST  DRUG

(CLEMASTINE)

CHOCOLATE                                            YES   UNKNOWN  HIST  DRUG

(CHOCOLATE FLAVORING)                                                    FOOD

FISH                                                  NO   UNKNOWN        DRUG

(FISH LIVER OIL)                                                         FOOD

FLUPHENAZINE DECANOATE                                NO   UNKNOWN  HIST  DRUG

FOOD

PEANUT OIL                                            NO   UNKNOWN  OBS   DRUG

Reactions: ITCHING,WATERING EYES, ANXIETY                             FOOD

Press RETURN to continue or '^' to stop listing:

OBS/

REACTANT                                             VER.   MECH.   HIST  TYPE

--------                                             ----  -------  ----  ----

NUTS                                                 YES   ALLERGY  HIST  FOOD

Reactions: HIVES

STRAWBERRIES                                         YES   UNKNOWN  HIST  FOOD

DUST                                                 YES   UNKNOWN  HIST  OTHER

Enter Causative Agent:

##### Add/Edit Allergy File

The final thing that you can do with the utility is to add a new local allergy, if no good choices exist.  This is the last resort and should only be used if no other possibility exists.  However, due to regional variances, etc., there might be a need to add a local allergy.  Once entered, this allergy will then be available for assignment to currently existing free-text entries

1. Select the Free text allergy clean up utility, to start the ART Clean-up Utility.
2. Select AE, Add/Edit Allergy File.

Select Enter/Edit Site Configurable Files Option: **6** Free text allergy clean up

utility

Building list of free text allergies...this may take a few minutes

**Allergy Tracking Update** Sep 19, 2003@13:05:28         Page:    1 of    4

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   COCA COLA SYRUP 8OZ                            1

2   COLD AIR                                       1

3   Diabetes Mellitus Type II                      1

4   DOG HAIR                                       1

5   DONUTS                                         1

6   DOUGH                                          1

7   DR P'S SNAKE OIL ELIXIR                        1

8   DRUGS                                          1

9   EIEIO                                          1

10  ENCAINIDE 25MG                                 1

**+         Enter ?? for more actions**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Next Screen// **AE** Add/Edit Allergy File

Select a LOCAL ALLERGY/ADVERSE REACTION: **DANDER**

Are you adding 'DANDER' as a new GMR ALLERGIES (the 112TH)? No// **Y** (Yes)

GMR ALLERGIES ALLERGY TYPE: ?

Answer with type(s) of this reaction.  E.g., FOOD or DRUG, FOOD or F or

DF.

GMR ALLERGIES ALLERGY TYPE: **???**

This field contains the type(s) for this allergy/adverse reaction .  The

user can enter the type(s) separated by commas, or the following codes:

D=Drug, F=Food, O=Other.  If codes are used, do not use commas to

separate multiple codes.  Examples of valid entries are:  DRUG or DRUG,

FOOD or D or DF or OTHER.

GMR ALLERGIES ALLERGY TYPE: **O**

NAME: DANDER// **&lt;Enter&gt;**

Select SYNONYM:

1   Drug

2   Food

3   Other

Select Classification(s) of Causative Agent: 3// **&lt;Enter&gt;**

Select DRUG INGREDIENT: **??**

You may enter a new DRUG INGREDIENTS, if you wish

This is one of the drug ingredients that make up this causative agent.

Choose from:

1,1,1 TRICHLOROETHANE

2-AMINO-2-METHYL-1-PROPANOL

2-PHENYLBENZIMIDAZOLE-5-SULFONIC ACID

4-DILAURATE

ABACAVIR SULFATE

ABCIXIMAB

ABSORPTION BASE

ACACIA

ACACIA POWDER

ACARBOSE

ACEBUTOLOL

ACEBUTOLOL HYDROCHLORIDE

ACEMANNAN

ACETAMIDE MEA

ACETAMINOPHEN

ACETANILIDE

ACETATE

ACETAZOLAMIDE

ACETAZOLAMIDE SODIUM

^

Select DRUG INGREDIENT: **&lt;Enter&gt;**

Select VA DRUG CLASSES: ?

You may enter a new VA DRUG CLASSES, if you wish

Answer with VA DRUG CLASS CODE, or CLASSIFICATION

Do you want the entire 573-Entry VA DRUG CLASS List? **N** (No)

Select VA DRUG CLASSES: **&lt;Enter&gt;**

#### Assessment Clean Up Utility

The first time GMRA ASSESSMENT UTILITY is accessed, a search will process through the ADVERSE REACTION ASSESSMENT file (#120.86) and the PATIENT ALLERGIES file (#120.8), looking for any possible discrepancies. Here is an example of running the utility the first time after installation:

Select OPTION NAME: GMRA ASSESSMENT UTILITY       Assessment clean up utility

Assessment clean up utility

I will create a task to build the list of assessments that need review and send you an email when the list is built.

Shall I notify anyone else when the list is built? NO//

Do you want to include deceased patients in the list? NO//

Enter the date and time below when the assessment list builder should start.

Requested Start Time: NOW//  (APR 27, 2016@16:53:53)

Successfully queued the assessment list builder; task #1645492.

When the search is completed, the person who started the task, as well as any additional recipients will receive a MailMan message entitled GMRA ASSESSMENT FIX LIST BUILD STATUS.

At this time, the user can go back into the GMRA ASSESSMENT UTILITY option and see a list of patients (if any) who have discrepancies that need to be reviewed and corrected.

**NOTE** : After the initial search is completed, accessing the option again will show the original list of patients and the status of the discrepancy for each patient.

**NOTE** : Installation of this patch does not by itself prevent the undefined error from occurring.  Sites must use the tool to correct any problems that it identifies in order to prevent the error from occurring.

**NOTE** : Once the allergies are displayed for the selected patient, the user should review the list for accuracy and mark any that need to be as entered in error. The review should be done **BEFORE** modifying the assessment.

**Example**

Select Systems Manager Menu &lt;TEST ACCOUNT&gt; Option: ART  Adverse Reaction Tracking

1      Enter/Edit Site Configurable Files ...

2      Adverse Reaction Tracking User Menu ...

3      Adverse Reaction Tracking Clinician Menu ...

4      Adverse Reaction Tracking Verifier Menu ...

5      P&amp;T Committee Menu ...

Select Adverse Reaction Tracking &lt;TEST ACCOUNT&gt; Option: 1  Enter/Edit Site Configurable Files

1      Edit Allergy File

2      Enter/Edit Signs/Symptoms Data

3      Enter/Edit Site Parameters

4      Sign/Symptoms List

5      Allergies File List

6      Allergy clean up utility

7      Assessment clean up utility

Select Enter/Edit Site Configurable Files &lt;TEST ACCOUNT&gt; Option: **7** Assessment clean up utility

**Assessment Corrector** Apr 11, 2013@11:33:33          Page:    1 of    1

Allergy Tracking Assessment Corrector

Line Patient Name                    Assessment  # of Allergies  Status

1.    FIFTYONE,INPATIENT                  No            2

2.    FIFTYTWO,INPATIENT                 Yes            0

3.    FIFTYFIVE,INPATIENT             No Assess.        3

**Enter ?? for more actions**

SP  Select Patient

Select Action: Quit// **SP** Select Patient

Enter a number (1-3): **1**

**Patient Detailed Display** Apr 11, 2013@11:33:45          Page:    1 of    1

Patient: FIFTYONE,INPATIENT (0851)                                     Inpatient

Assessment: No known reactions

Line Reactant                        Entered in Error

1.    DUST                            NO

2.    QUINOLONES                      NO

**Enter ?? for more actions**

MA  Modify Assessment                   EE  Change all to 'Entered in Error'

RR  Review Reaction

Select Action: Quit// **RR** Review Reaction

Enter a number (1-2): **1**

NUMBER: 968                             PATIENT: FIFTYONE,INPATIENT

REACTANT: DUST                        GMR ALLERGY: DUST

ORIGINATION DATE/TIME: APR 11, 2013@07:37

ORIGINATOR: PROVIDER,ONE              OBSERVED/HISTORICAL: HISTORICAL

ORIGINATOR SIGN OFF: YES              MECHANISM: ALLERGY

VERIFIED: YES

VERIFICATION DATE/TIME: APR 11, 2013@07:39:43

ALLERGY TYPE: OTHER

REACTION: ITCHING,WATERING EYES         ENTERED BY: PROVIDER,ONE

DATE ENTERED: APR 1990

REACTION: SNEEZING                      ENTERED BY: PROVIDER,ONE

DATE ENTERED: APR 1990

DATE/TIME: APR 11, 2013@07:39:43        USER ENTERING: PROVIDER,ONE

Would you like to mark this allergy as 'Entered in Error'? NO// **YES**

**Patient Detailed Display** Apr 11, 2013@11:34:48          Page:    1 of    1

Patient: FIFTYONE,INPATIENT (0851)                                     Inpatient

Assessment: No known reactions

Line Reactant                        Entered in Error

1.    DUST                            YES

2.    QUINOLONES                      NO

**Enter ?? for more actions**

MA  Modify Assessment                   EE  Change all to 'Entered in Error'

RR  Review Reaction

Select Action: Quit// **MA** Modify Assessment

Does this patient have any known allergies or adverse reactions? : No// **Yes**

**Patient Detailed Display** Apr 11, 2013@11:35:52          Page:    1 of    1

Patient: FIFTYONE,INPATIENT (0851)                                     Inpatient

Assessment: Has known reactions

Line Reactant                        Entered in Error

1.    DUST                            YES

2.    QUINOLONES                      NO

**Enter ?? for more actions**

MA  Modify Assessment                   EE  Change all to 'Entered in Error'

RR  Review Reaction

Select Action: Quit// **&lt;Enter&gt;**

**Assessment Corrector** Apr 11, 2013@11:36:32          Page:    1 of    1

Allergy Tracking Assessment Corrector

Line Patient Name                    Assessment  # of Allergies  Status

1.    FIFTYONE,INPATIENT                 Yes            1         **FIXED**

2.    FIFTYTWO,INPATIENT                 Yes            0

3.    FIFTYFIVE,INPATIENT             No Assess.        3

**Enter ?? for more actions**

SP  Select Patient

Select Action: Quit// **SP** Select Patient

Enter a number (1-3): **3**

**Patient Detailed Display** Apr 11, 2013@11:37:12          Page:    1 of    1

Patient: FIFTYFIVE,INPATIENT (0855)                                    Inpatient

Assessment: None on file

Line Reactant                        Entered in Error

1.    CONTRAST MEDIA                  NO

2.    STRAWBERRIES                    NO

3.    POLLEN                          NO

**Enter ?? for more actions**

MA  Modify Assessment                   EE  Change all to 'Entered in Error'

RR  Review Reaction

Select Action: Quit// EE   Change all to 'Entered in Error'

You are about to mark all of this patient's allergies as 'Entered in Error'.

Do you want to continue? NO// YES

Marking CONTRAST MEDIA as ‘Entered in Error’...

Marking STRAWBERRIES as ‘Entered in Error’...

Marking POLLEN as 'Entered in Error'...

**NOTE: By marking this reaction as entered in error, FIFTYFIVE,INPATIENT

no longer has an assessment on file.  You may reassess this patient

now by answering the following prompt or hit return to do it later.

Does this patient have any known allergies or adverse reactions? : NO

**Patient Detailed Display** Apr 11, 2013@11:38:29          Page:    1 of    1

Patient: FIFTYFIVE,INPATIENT (0855)                                    Inpatient

Assessment: No known reactions

Line Reactant                        Entered in Error

1.    CONTRAST MEDIA                  YES

2.    STRAWBERRIES                    YES

3.    POLLEN                          YES

**Enter ?? for more actions**

MA  Modify Assessment                   EE  Change all to 'Entered in Error'

RR  Review Reaction

Select Action: Quit// **&lt;Enter&gt;**

**Assessment Corrector** Apr 11, 2013@11:40:21          Page:    1 of    1

Allergy Tracking Assessment Corrector

Line Patient Name                    Assessment  # of Allergies  Status

1.    FIFTYONE,INPATIENT                 Yes            1         **FIXED**

2.    FIFTYTWO,INPATIENT                 Yes            0

3.    FIFTYFIVE,INPATIENT                 No            0         **FIXED**

**Enter ?? for more actions**

SP  Select Patient

Select Action: Quit//

#### Signing off on Allergies

Before patch 17, the allergy tracking package allowed users to leave entries in a “not signed off” state.  Although not complete, the allergy became part of the patient’s record, even though the user was told that it would not be.  Depending on how the entry was made, an alert might not be sent indicating that the entry needed to be signed off.  Ultimately, an unfinished entry might never be finished, but still appear in the patient’s record.

A change has been made so that no new entry can be left in a “not signed off” state.  Upon entering a new allergy, if the user enters an “^” at any point during the data gathering process, the entry will be deleted.  Upon completing the new entry, the user will be asked if the entry is okay.  If the user enters no, then they’ll be given the opportunity to edit or delete the entry.  The entry must then be deleted or accepted before exiting this process.  As a result, no new entries will be allowed to be in an unsigned state.

**NOTE** : Sites should run the “Patient Allergies Not Signed Off” option to identify all existing entries that have not yet been completed.  Each entry should be reviewed and marked as entered-in-error or completed by entering the required information.  Once these entries are cleaned up, then no unsigned entries should appear in the patient’s chart.  You are not required to update these entries as data may not be available but you should review them and take action if possible.  The post-installation routine will also list any allergies that are observed, have been signed off, but are missing either an observed date or a sign/symptom.  These entries should also be reviewed and updated if possible.

GMRA CLINICIAN MENU     Adverse Reaction Tracking Clinician Menu

1      Enter/Edit Patient Reaction Data

2      FDA Enter/Edit Menu ...

3      Reports Menu ...

4      Edit Chart and ID Band

5      Online Reference Card

You have PENDING ALERTS

Enter  "VA to jump to VIEW ALERTS option

Select Adverse Reaction Tracking Clinician Menu Option: **3** Reports Menu

1      Active Listing of Patient Reactions

2      Print Patient Reaction Data

3      Print an FDA Report for a Patient

4      List by Location of Unmarked ID Bands/Charts

5      Patient Allergies Not Signed Off

6      List by Location of Undocumented Allergies

7      List by Location Not Verified Reactions

8      List by Location and Date All Signed Reactions

9      List FDA Data by Report Date

You have PENDING ALERTS

Enter  "VA to jump to VIEW ALERTS option

Select Reports Menu Option: **5** Patient Allergies Not Signed Off

DEVICE: HOME//   ANYWHERE

ALLERGY/ADVERSE REACTIONS TO BE SIGNED OFF

Run Date/Time:  12:12:09 pm

ORIGINATOR              PATIENT            ALLERGY        ORIGINATION DATE/TIME

-------------------------------------------------------------------------------

NO DATA FOR THIS REPORT

Enter RETURN to continue or '^' to exit:

##### Q&amp;A Tips:

**What do you do with an entry like number 1?**

This entry actually has multiple reactants listed and you need to make sure your account for each of the reactants that are listed.  We recommend that you go to the detailed display for the entry in question and then use the add/edit patient reaction option to add the extra reactants and then to update the entry to the first reactant listed.

**We have a problem with No Known Allergies type entries; why don’t they appear on the list?**

If you’re one of the sites that added NKA as a local allergy, it won’t appear in this list.  If you haven’t already done so, you need to check your GMR Allergies file to see if there is an entry for NKA or something similar.  If there is, then you’ll need to enter a NOIS and we’ll help you get rid of that entry.

**Do I need to fix every entry that’s listed?**

That would be the goal but the truth is, if you can’t figure out what it should be linked to, or if the entry as it exists in the patient allergy file has all of the drug class and drug ingredient information, you can leave it alone.  It’s better to have information available that you may not be sure is correct and be wrong than to get rid of the information and have it be correct.

### Menu Assignment

Assign menus to the users. See the Option Delegation portion of the Security chapter in this manual to determine how the package’s menus should be assigned.

#### Security Key Assignment

Assign security keys when necessary.  See the Security Keys portion of the Security chapter of this manual to determine how the package’s keys should be assigned.

#### Mail Group Membership

The software installation process checks for the existence of the necessary package mail groups.  If they do not exist, they are created at the time of software installation.  The site should review the mail group membership and update it if necessary.  The mail group names are as follows:

1. GMRA MARK CHART

2. GMRA P&amp;T COMMITTEE FDA

3. GMRA VERIFY DRUG ALLERGY

4. GMRA VERIFY FOOD ALLERGY

5. GMRA VERIFY OTHER ALLERGY

6. GMRA REQUEST NEW REACTANT

##### Bulletins List

The following bulletins are created:

1. GMRA ENTERED IN ERROR

2. GMRA MARK CHART

3. GMRA P&amp;T COMMITTEE FDA

4. GMRA SIGNS/SYMPTOMS UPDATE

5. GMRA VERIFY ALLERGY

There are no Forms, Help Frames, or Window Objects exported with this version.

### Security

#### Security Keys

GMRA-ALLERGY VERIFY:  This key should be given to personnel (e.g., clinical pharmacists) who verify allergy/adverse reactions.

GMRA-SUPERVISOR:  This key should be given to personnel (e.g., ART package ADPAC) who may need to override the package security in order to edit the data.

#### File Security

The File Security table below lists the levels of access to a specific field:

- @ - The “at” sign indicates that users with programmer access can perform a specific function (i.e., read, write, delete) on a specific VistA file.
- ^ - The “caret” sign indicates that users with programmer access cannot perform a specific function on a specific VistA file.
- If there is no “at” or “caret” sign, users without programmer access can perform a specific function on a specific VistA file.

Table 2 – File Security

|   File #  | File Name                   | Data Dictionary (DD)   | Read (RD)   | Write (WR)   | Delete (DEL)   | Learn as You Go (LAYGO)   | AUDIT   |
|-----------|-----------------------------|------------------------|-------------|--------------|----------------|---------------------------|---------|
|    120.8  | Patient Allergies           | @                      |             | @            | @              | @                         | @       |
|    120.82 | GMR Allergies               | @                      |             | @            | @              |                           | @       |
|      2    | National Allergy            |                        |             | ^            | ^              |                           |         |
|    120.83 | Sign/Symptoms               | @                      |             | @            | @              |                           | @       |
|      1    | National Sign/Symptoms      |                        |             | ^            | ^              |                           |         |
|    120.84 | GMR Allergy Site Parameters | @                      | @           | @            | @              | @                         | @       |
|    120.85 | Adverse Reaction Reporting  | @                      |             | @            | @              | @                         | @       |
|    120.86 | Adverse Reaction Assessment | @                      | @           | @            | @              | @                         | @       |
|    120.87 | GMRA Document               | @                      |             | @            | @              | @                         | @       |

A description of the columns in the File Security table is listed below:

- File # – File number.
- File Name – Name of the file.
- Data Dictionary (DD) – The DD security property controls who is allowed to modify the data dictionary.
- Read (RD) – The RD security property controls who can read the file.
- Write (WR) – The WR security property controls who can update the file.
- Delete (DEL) – The DEL security property controls who can delete an existing record contained within the file.
- Learn As You Go (LAYGO) – The LAYGO security property allows a user to add a new record to a file. However, to add new entries, Write Access to the file is required in addition to the LAYGO security property.
- AUDIT – The AUDIT security property controls the setting of auditing characteristics and deletion of audit trails.

### Option Delegation

Security is partially controlled by the delegation of one of six menus:

- GMRAMGR
- GMRA SITE FILE MENU
- GMRA USER MENU
- GMRA CLINICIAN MENU
- GMRA VERIFIER MENU
- GMRA P&amp;T MENU

IRM personnel and the ART Application Coordinator and their designees should be given the GMRAMGR MENU option.  Clinical users (e.g., nurses) of ART should be given the GMRA CLINICIAN MENU option.  Clerks should be given the GMRA USER MENU option.

Verifiers (e.g. clinical pharmacists) should be given the GMRA VERIFIER MENU option, and P&amp;T Committee Members should be given the GMRA P&amp;T MENU option.

#### Privacy Act Statement

In accordance with Office of Personnel Management and VA policies, this information is to be furnished for use only as authorized.  It will not be reproduced or used for any other purpose.  Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties.  Disposal will be by burning, shredding, or other treatment to destroy their legibility.

#### Electronic Signature

The software does not prompt for or store a user’s electronic signature.  However, the software does have a programming interface with the Progress Notes package and that package does prompt for an electronic signature when a progress note is generated.

#### GMRA UPDATE RESOURCE

ADI (Allergy Domain Implementation/Data Standardization) uses a resource device to control the updating of existing patient allergies.  When changes are made to existing allergy definitions in file #120.82, all associated patient allergies in file #120.8 are updated to match the new definition of the entry from #120.82.  The resource device controls the updating process.  Because of the way the updates are implemented, the resource device needs to manage the updates one at a time.  As a result, the resource slots field is set to one and should not be changed.

### Routines

**Namespace** : *GMRA*

XUPRROU (List Routines) prints a list of any or all of the GMRA routines.  This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.  See the list of checksums in the Install Guide.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **list Routines**

Routine Print

Want to start each routine on a new page: No// **[ENTER]**

routine(s) ?   &gt; **GMRA***

The first line of each routine contains a brief description of the general function of the routine.  Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each GMRA subset routine.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?   &gt; **GMRA***

### File List

Table 3-File List

|   NUMBER | NAME                         | GLOBAL NAME    | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   120.8  | PATIENT ALLERGIES            | ^GMR(120.8,    | Contains patient allergy/adverse reaction information. No data exported with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|   120.82 | GMR ALLERGIES                | ^GMRD(120.82,  | Contains a listing of allergies from which user can select.  Per VHA directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to VHA Directive 2005-044 shall not be supported. |
|   120.83 | SIGN/SYMPTOMS                | ^GMRD(120.83,  | A listing of possible allergic reactions. Per VHA directive 2005-044, this file has been "locked down" by Data Standardization (DS).  The file definition (i.e. data dictionary) shall not be modified.  All additions, changes and deletions to entries in the file shall be done by Enterprise Reference Terminology (ERT) using the Master File Server (MFS), provided by Common Services (CS).  Creating and/or editing locally defined fields in the file are not permitted.  Use of locally defined fields that were created prior to VHA Directive 2005-044 shall not be supported.                    |
|   120.84 | GMR ALLERGY SITE  PARAMETERS | ^GMRD(120.84 , | Site configurable features for the package. Data comes with the file, but will be added only if no data exists in the file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|   120.85 | ADVERSE REACTION  REPORTING  | ^GMR(120.85,   | This file contains all the data for an Observed Drug reaction.  No data exported with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|   120.86 | ADVERSE REACTION  ASSESSMENT | ^GMR(120.86,   | This file is a listing of all the patients who have been asked about allergies/ adverse reactions (ADRs). It contains a pointer to File 2 (PATIENT) and a flag to indicate if the patient has or does not have an Allergy/ADR . No data exported with this file.                                                                                                                                                                                                                                                                                                                                              |
|   120.87 | GMRA DOCUMENT                | ^GMRD(120.87,  | This file contains the name and text of documents that can be displayed to the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|   120.88 | REMOTE ALLERGY COMMENT       | ^GMR(120.88,   | This file contains locally entered comments relating to allergies entered for a patient at a separate (remote) facility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Templates

Table 4-Templates

| TYPE       | NAME                          |   FILE # | DESCRIPTION                                                                                                                                                                  |
|------------|-------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input None | Print GMRA PRINT AUTOVERIFIED |   120.8  | This print template is used to print out autoverified reactions over a date range. It is run from the List Autoverified Reaction Data [GMRA PRINT AUTOVERIFIED DATA] option. |
|            | GMRA PRT AUTO HDR             |   120.8  | This print template is used to add the header for the GMRA PRINT AUTOVERIFIED print template.                                                                                |
| Sort       | GMRA PRINT FILE               |   120.83 | This print template prints a list of signs/symptoms in the Sign/Symptoms file (#120.83).  It is called from the Sign/Symptoms List [GMRA PRINT SIGN /SYMPTOMS LIST] option.  |
|            | GMRA SORT AUTOVERIFIED        |   120.8  | This sort template sorts the data to be printed by the GMRA PRINT AUTOVERIFIED print template.                                                                               |

### Protocols

Table 5-Protocols

| Name                                     | Description                                                                                                                                                          |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMRA ASSESS DET ALL EIE     New          | These protocols are used by the GMRA ASSESSMENT UTILITY                                                                                                              |
| GMRA ASSESS DET ASSESSMENT  New          |                                                                                                                                                                      |
| GMRA ASSESS DET MENU        New          |                                                                                                                                                                      |
| GMRA ASSESS DET REVIEW      New          |                                                                                                                                                                      |
| GMRA ASSESS MENU            New          |                                                                                                                                                                      |
| GMRA ASSESS SELECT PATIENT  New          |                                                                                                                                                                      |
| GMRA ASSESSMENT CHANGE                   | This protocol will be invoked whenever a patient’s assessment value changes.                                                                                         |
| GMRA EDIT VERIFIED DATA                  | This protocol is activated whenever a user edits a verified allergy, including adding or editing observations.                                                       |
| GMRA ENTERED IN ERROR                    | This protocol will be invoked whenever a reaction is Entered in Error.                                                                                               |
| GMRA FIX DETAIL MENU                     |                                                                                                                                                                      |
| GMRA FIX ADD/EDIT ALLERGY FILE           | Add/Edit Allergy File                                                                                                                                                |
| GMRA FIX ADD/EDIT ALLERGY FILE IN DETAIL | Add/Edit Allergy File                                                                                                                                                |
| GMRA FIX DETAIL IN DETAIL                | Allergy Detailed Display                                                                                                                                             |
| GMRA FIX DETAIL LIST                     | Detailed Display                                                                                                                                                     |
| GMRA FIX ENTERED IN ERROR                | Mark entered in error                                                                                                                                                |
| GMRA FIX ENTERED IN ERROR IN DETAIL      | Mark entered in error                                                                                                                                                |
| GMRA FIX FREE TEXT LIST                  | Free text entries                                                                                                                                                    |
| GMRA FIX PATIENT A/AR EDIT IN DETAIL     | Add/Edit Patient Reaction                                                                                                                                            |
| GMRA FIX UPDATE REACTANT                 | Update to new reactant                                                                                                                                               |
| GMRA FIX UPDATE REACTANT IN DETAIL       | Update to new reactant                                                                                                                                               |
| GMRA MEDWATCH DATA COMPLETE              | This protocol will be activated whenever a reaction has a MEDWatch form entered.                                                                                     |
| GMRA RECEIVE                             | This protocol is invoked when a Health Level Seven (HL7) message is received from the OE/RR package.                                                                 |
| GMRA  DATA                               | This protocol will be activated whenever a reaction is Signed (completed).                                                                                           |
| GMRA VDEF ORU R01 ADV ASSESS HR          |                                                                                                                                                                      |
| GMRA VDEF ORU R01 ADV ASSESS VS          |                                                                                                                                                                      |
| GMRA VDEF ORU R01 ADV REACT HR           |                                                                                                                                                                      |
| GMRA VDEF ORU R01 ADV REACT VS           |                                                                                                                                                                      |
| GMRA VDEF ORU R01 ALLERGY HR             |                                                                                                                                                                      |
| GMRA VDEF ORU R01 ALLERGY VS             |                                                                                                                                                                      |
| GMRA VERIFY DATA                         | This protocol will be activated whenever a reaction is Verified.                                                                                                     |
| GMRADGPM MARK CHART                      | This protocol will hang off of the DGPM MOVEMENT EVENTS protocol and for a new admission will send a bulletin to mark that patient’s chart for all active allergies. |
| GMRAOR ALLERGY ENTER/EDIT                | This protocol will allow the user to enter/edit patient allergy/adverse reaction data.                                                                               |

### Exported Options

#### Options Not on a Menu

List by Location Not Verified Reaction (Task) [GMRA TASK A/AR NV] is an option meant to be tasked for a daily run.

### Menu Options

Adverse Reaction Tracking menu [GMRAMGR]

1      Enter/Edit Site Configurable Files ... [GMRA SITE FILE MENU]

2      Adverse Reaction Tracking User Menu ... [GMRA USER MENU]

3      Adverse Reaction Tracking Clinician Menu ... [GMRA CLINICIAN MENU]

4      Adverse Reaction Tracking Verifier Menu ... [GMRA VERIFIER MENU]

5      P&amp;T Committee Menu ... [GMRA P&amp;T MENU]

1.  Enter/Edit Site Configurable Files

1.  Edit Allergy File

2.  Enter/Edit Signs/Symptoms Data

3.  Enter/Edit Site Parameters

4.  Sign/Symptoms List

5.  Allergies File List

6.  Allergy clean up utility

7.  Assessment Clean Up Utility

2.  Adverse Reaction Tracking User Menu

1.  Enter/Edit Patient Reaction Data

2.  Active Listing of Patient Reactions

3.  Edit Chart and ID Band

4.  List by Location of Unmarked ID Bands/Charts

5.  Patient Allergies Not Signed Off

6.  List by Location of Undocumented Allergies

7.  Print Patient Reaction Data

8.  Online Reference Card

3.  Adverse Reaction Tracking Clinician Menu

1.  Enter/Edit Patient Reaction Data

2.  FDA Enter/Edit Menu…

3.  Reports Menu…

4.  Edit Chart and ID Band

5.  Online Reference Card

4.  Adverse Reaction Tracking Verifier Menu

1.  Enter/Edit Patient Reaction Data

2.  Verify Patient Reaction Data

3.  Reports Menu…

4.  Edit Chart and ID Band

5.  FDA Enter/Edit Menu…

6.  Online Reference Card

5. P&amp;T Committee Menu

1.  Enter/Edit P&amp;T Committee Data

2.  Enter/Edit FDA Report Data

3.  Reports Menu…

1.  Print an FDA report for a Patient

2.  Print all FDA events within D/T range

3.  Print Patient FDA Exception Data

4.  Print all FDA Exceptions within a D/T range

5.  Patient Allergies Not Signed Off

6.  Print Patient Reaction Data

7.  Active Listing of Patient Reactions

8.  List by Location of Undocumented Allergies

9.  List Autoverified Reaction Data

10.  List by Location Not Verified Reactions

11.  List by Location and Date all Sign Reactions

12.  List FDA Data by Report Date

13.  List of Fatal Reaction Over a Date Range

14.  Print Summary of Outcomes

15.  Frequency Distribution of Causative Agents

16.  Frequency Distribution of Drug Classes

17.  Total Reported Reactions Over a Date Range

18.  P&amp;T Committee adr Outcome Report

19.  P&amp;T Committee ADR Report

### Cross References

Patch 23 (GMRA*4.0*23) introduces two new cross-references to support data standardization for the Health Data Repository (HDR): AVUID and AMASTERVUID.

120.82^AVUID

AMASTERVUID (#493)    RECORD    REGULAR    IR    SORTING ONLY

Short Descr:  Identifies Master entry for a VUID

Description:  If multiple entries have the same VUID in the file, this

cross-reference can be used to identify the Master entry

for a VUID associated with a Term/Concept.

Set Logic:  S ^GMRD(120.82,"AMASTERVUID",$E(X(1),1,30),X(2),DA)=""

Kill Logic:  K ^GMRD(120.82,"AMASTERVUID",$E(X(1),1,30),X(2),DA)

Whole Kill:  K ^GMRD(120.82,"AMASTERVUID")

X(1):  VUID  (120.82,99.99)  (Subscr 1)  (Len 30)  (forwards)

X(2):  MASTER ENTRY FOR VUID  (120.82,99.98)  (Subscr 2)

(forwards)

The AHDR cross-reference sends data to HDR upon entry.

AHDR (#443)    RECORD    MUMPS        ACTION

Short Descr:  Sends data to HDR upon entry

Description:  This cross reference will send the HDR allergy data upon

entry or editing of allergy related data

### Archiving and Purging

Archiving only needs to be done to the Patient Allergies (#120.8) file.  Because of the importance of this data, it should be retained as long as the corresponding Patient (#2) file record exists.  Software to perform archiving of this data will be made available in a later release.

No purging capabilities are provided with this version.


### Resource Requirements

The disk requirements are estimated as follows:

Table 6-Disk Requirements Table

| Globals     | Type of Data              | Size                                                                                                                                                                                   |
|-------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMRD(120.82 |                           |                                                                                                                                                                                        |
| GMRD(120.83 | Static data for ART       | 40K                                                                                                                                                                                    |
| GMRD(120.84 |                           |                                                                                                                                                                                        |
| GMRD(120.87 |                           |                                                                                                                                                                                        |
| GMR(120.8   | Patient data for ART      | 0.4K per Allergy entry                                                                                                                                                                 |
| GMR(120.85  | Observed, FDA             | 0.4K per Reaction                                                                                                                                                                      |
| GMR(120.86  | Patient NKA data          | 0.01K per Patient                                                                                                                                                                      |
| GMR(120.88  | Remote comment (optional) | Reactive field – 30 char  Patient field – pointer IEN – 15 char  Enter date/time: 14 char  Enter by – ptr – 15 char  Comment – 250 char  Size to be calculated from above  Per Comment |


### Callable Routines

GMRADPT 	GMRADPT extracts data from the Patient Allergies (120.8) file for a specified patient based on the criteria specified in the GMRA input parameter.  The data will be returned in a local array.

#### Version 1

Patch GMRA*4*46 introduced significant changes to the input and output of this routine. Existing calls to this routine will invoke the Version 1 implementation of this routine (Pre-patch GMRA*4*46 changes).  To take advantage of the changes introduced in Patch GMRA*4*46, see Version 2 section below.

Input:

DFN 	The internal entry number in the Patient file for the patient whose allergy data needs to be extracted.

GMRA 	This is an optional three-piece variable that will determine which kinds of allergy data will be returned by the extract.  The default values which will be used are shown in the discussion of each piece.  Consider the variable GMRA with the format P1^P2^P3^P4 where

P1 can have the value 0, 1, or 2 where

1. means extract all allergies and adverse reactions
2. means extract allergies only
3. means extract adverse reactions only

A record stored in the Patient Allergies file is an adverse reaction. **Every true allergy is an adverse reaction, but not every adverse reaction is an allergy.** This determination is made by the verifier of the allergy data.  The default value for this piece is 0.

P2 	can have the value 0, 1, or 2 where

1. means extract all verified and non-verified records
2. means extract verified records only
3. means extract non-verified records only

A record can either be verified by some allergy verifier, or it has not yet been verified.  In the case that the site is using autoverification, the record is automatically verified at the time the originator of the record signs off (completes) on it.  No record can be extracted before it has been signed off (completed) by the originator, as it is not part of the medical record.  The default value for this piece is 0.

P3	is a three-character string, where each character can have a value of 0 or 1.  Consider P3 represented as XYZ where X, Y, and Z are the three different characters.  Then the following is what each of these characters represent:

**X** determines whether to extract records with the type of Other. If

X=0 then records with the type Other will not be extracted, and if X=1 then they will be extracted.

**Y** determines whether to extract records with the type of Food. If

Y=0 then records with the type Food will not be extracted, and if

Y=1 then they will be extracted.

**Z** determines whether to extract records with the type of Drug. If

Z=0 then records with the type Drug will not be extracted, and if            Z=1 then they will be extracted.

A record has a type associated with it.  The three types are Food, Drug and Other.  This variable will help to determine which of these types of records will be extracted, and which types will not be extracted.  The default value for this piece is 111.

P4	can have the value 0 or 1 where

0	means return reactions documented locally

1	means return reactions documented locally and remote reactions stored in the Health Data Repository (HDR)

Output:

GMRAL 	This variable is an array of the patient's data extracted by this utility based on the criteria specified in the optional GMRA variable.  The format of this variable is:

GMRAL=(1,0,NULL) GMRAL(DA)=A^B^C^D^E^F^G^H^I^J^K GMRAL(DA,"S",COUNT)=SIGN

GMRAL("REMOTE",RCOUNT)= A^B^C^D^E^F^G^H^I^J^K

GMRAL("REMOTE",RCOUNT, "S",COUNT)=SIGN

GMRAL("REMOTE",RCOUNT, "SITE")=SITE

Where

GMRAL is 1 if patient has Adverse Reaction. is 0 if patient has no known Adverse Reaction. null if patient has not been asked about Adverse Reaction.

DA is the internal entry number of the record in the Patient Allergies (120.8) file.

A is the patient's DFN (from input variables).

B is the name of the allergen.

*C is the type of the allergen where D=Drug, F=Food, and O=Other.

D is a flag denoting if the allergy has been verified where

1=verified and 0=non-verified.

E 	is a flag denoting whether the allergy is a true allergy, or if it is an adverse reaction where 1=adverse reaction and 0=true allergy.

**F is both the external and internal representation of the allergy Mechanism.  It is stored in the format External";"Internal.

Mechanism

External 			Internal

--------------			------------

Allergy 			0

Pharmacologic 		2

Unknown 		U

G is the type of the reaction in the form of"F", "D", or "0" or a combination of the three types.

Types

Internal 		External format

-------------		-----------------------

D 			is a drug reaction.

DF 		is a drug/food reaction

DFO 		is a drug/food/other reaction

DO 		is a drug/other reaction

F 			is a food reaction

FO			 is a food/other reaction

O I			s a other reaction

H 	is both the external and internal representation of the Adverse Reaction Mechanism.  It is stored in the format External";"Internal.

Mechanism

External 		Internal

-------------		------------

Allergy 		A

Pharmacologic 	P

Unknown 		U

I is a variable pointer to the allergen

J is the observed/historical of the reaction.  It is stored in the format External";"Internal

External 		Internal

-------------		------------

OBSERVED	o

HISTORICAL	h

K is the severity of the reaction.  It is stored in the format External";"Internal

External 		Internal

-------------		------------

MILD		1

MODERATE	2

SEVERE		3

SIGN is the sign/symptom of the reaction.  It is stored in the format External";"Internal where Internal is the pointer to the SIGN/SYMPTOMS file (#120.83).

SITE is the institution that documented the reaction.  It is stored in the format INSTITUTION file (#4) pointer"^"Station name"^"Station number

#### Version 2

Patch GMRA*4*46 introduced significant changes to the input and output of this routine.  The primary changes are returning remote records and returning additional data for each reaction.  To take advantage of the changes introduced in Patch GMRA*4*46, use the EN2 line-tag instead of directly calling the routine.

Input:

DFN 	The internal entry number in the Patient file for the patient whose allergy data needs to be extracted.

GMRA 	This is an optional four-piece variable that will determine which kinds of allergy data will be returned by the extract.  The default values which will be used are shown in the discussion of each piece.  Consider the variable GMRA with the format P1^P2^P3^P4 where

P1 can have the value 0, 1, or 2 where

0 	means extract all allergies and adverse reactions

1 	means extract allergies only

2 	means extract adverse reactions only

A record stored in the Patient Allergies file is an adverse reaction. **Every true allergy is an adverse reaction, but not every adverse reaction is an allergy.** This determination is made by the verifier of the allergy data. The default value for this piece is 0.

P2 	can have the value 0, 1, or 2 where

0 	means extract all verified and non-verified records

1 	means extract verified records only

2 	means extract non-verified records only

A record can either be verified by some allergy verifier, or it has not yet been verified.  In the case that the site is using autoverification, the record is automatically verified at the time the originator of the record signs off (completes) on it.  No record can be extracted before it has been signed off (completed) by the originator, as it is not part of the medical record.  The default value for this piece is 0.

P3 	is a three-character string, where each character can have the value of 0 or 1.  Consider P3 represented as XYZ where X, Y and Z are the three different characters.  Then the following is what each of these characters represents:

X 	determines whether to extract records with the type of Other. If X=0 then records with the type Other will not be extracted, and if X=1 then they will be extracted.

Y 	determines whether to extract records with the type of Food. If Y=0 then records with the type Food will not be extracted, and if Y=1 then they will be extracted.

Z 	determines whether to extract records with the type of Drug. If Z=0 then records with the type Drug will not be extracted, and if Z=1 then they will be extracted.

A record has a type associated with it.  The three types are Food, Drug and Other. This variable will help to determine which of these types of records will be extracted, and which types will not be extracted.  The default value for this piece is 111.

P4 	can have the value 0 or 1 where

1. means only return records documented at the local site
2. means return records documented at both the local and all  remote sites

Output:

GMRAL 	This variable is an array of the patient's data extracted by this utility based on the criteria specified in the optional GMRA variable.  The format of this variable is:

GMRAL=(1,0,NULL) GMRAL(DA)=A^B^C^D^E^F^G^H^I^J GMRAL(DA,"S",COUNT)=K

GMRAL(DA,"O",COUNT)=L

GMRAL(DA,"SITE")=M

Where

GMRAL 	is 1 if patient has Adverse Reaction.

is 0 if patient has no known Adverse Reaction.

null if patient has not been asked about Adverse Reaction.

DA	 for locally documented records, the internal entry number of the record in the Patient Allergies (120.8) file and for remotely documented records, the letter "R" followed by the reaction's number in the ^XTMP("ORRDI","ART",DFN) global (DFN is the patient's internal entry number in the PATIENT file).

A 	is the patient's DFN (from input variables).

B 	is the name of the allergen.

C 	is null; use G.

D 	is a flag denoting if the allergy has been verified where 1=verified and 0=non-verified.

E	 is a flag denoting whether the allergy is a true allergy, or if it is an adverse reaction where 1=adverse reaction and 0=true allergy.

F 	is null; use H.

G	is the type of the reaction in the form of "F", "D", or "0" or a combination of the three types.

Types

Internal			External format

--------------			---------------

D 				is a drug reaction.

DF 			is a drug/food reaction

DFO 			is a drug/food/other reaction

DO 			is a drug/other reaction

F 				is a food reaction

FO 			is a food/other reaction

O 				is a other reaction

H	is both the external and internal representation of the Adverse Reaction Mechanism.  It is stored in the format External";"Internal.

Mechanism

External			 Internal

--------------		---------------

Allergy 			    A Pharmacologic 		    P

Unknown 		                U

I	is a pointer to the reaction in variable pointer format; refer to the data

dictionary for the GMR ALLERGY field for details.

J	is both the external and internal representation of the OBSERVED/HISTORICAL field.  It is stored in the format

External";"Internal.

K	is both the external and internal representation of the allergy Signs/Symptoms and the date/time it was entered.  Each of the Signs/Symptoms will be stored on its own "S" node in the following format.

External";"Internal pointer to Signs/Symptoms file (120.83)"^"External";"Internal date entered.  If the pointer equals the "OTHER REACTION" then the free text stored in the patient file will be stored in the external representation.

COUNT	 is the order which the Signs/Symptoms are stored in the GMRAL(DA,"S",COUNT) Array. Count is a positive whole number.

L	is both the external and internal representation of the reaction’s severity and date/time of the event.  Each severity is stored on its own "O" node in the following format:

External";"Internal severity"^"External";"Internal date/time of event.

COUNT	is the order which the observations are stored in the GMRAL(DA,"O",COUNT) Array. Count is a positive whole number.

M	is the site that documented the reaction.  Only reactions documented remotely will have a "SITE" node defined.  It has the following format:

External"^"Internal pointer to Institution file (#4)"^"Station number

### External Relations

ART v4.0, patch 23 requires installation of the following packages before its installation:

Health Data &amp; Informatics (HDI) 1.0

Master File Server (MFS) patch XU*8.0*299

Kernel V. 8.0+

VA FileMan V. 21+

MAS V. 5.3+

National Drug File V. 3+

### Database Integration Agreements

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

To obtain the current list of IAs, to which ART is a custodian, do the following:

Select Integration Agreements Menu Option: **8 &lt;Enter&gt;** Custodial Package Menu

1 ACTIVE by Custodial Package

2 Print ALL by Custodial Package

3 Supported References Print All

Select Custodial Package Menu Option: **1 &lt;Enter&gt;** ACTIVE by Custodial Package

Select PACKAGE NAME: **GMRA**

DEVICE: HOME// **&lt;Enter&gt;** UCX DEVICE Right Margin: 80// **&lt;Enter&gt;**

A new application programming interface (API) was added in patch 23 to allow updates to definitions of reactants to be propagated through existing allergies in the PATIENT ALLERGIES file (120.8).

UPDATE^GMRAUTL2(ENTRY,ING,CLASS)

ENTRY is IEN;FILE REFERENCE^TEXT OF FILE ENTRY - For example

23;GMRD(120.82,^STRAWBERRIES

ING - Array of ingredients in the format of ING("A",IEN in file 50.416)

for ingredients being added and ING("D",IEN in file 50.416) for

ingredients being deleted.

CLASS - Array of drug classes in the format of CLASS("A",IEN in file

50.605) for classes being added and CLASS("D",IEN in file 50.605) for

those classes being deleted.

See DBIA #4667 for complete details regarding this API.

### SACC Exemptions

The SACC has granted the following exemptions:

1. Routines may exceed the 5K limit.

2. Use of the $GET command with two arguments is permitted.

3. Use of reverse $ORDER looping is permitted.

4. Use of the MERGE command is permitted.

5. Passing null values in a parameter list is permitted.

6. Use of $TEXT on a line that does not contain a double semicolon (i.e., ;;) is permitted.

### Internal Relations

All options can be independently invoked.

### Package-wide Variables

There are no package-wide variables.

### How to Generate On-line Documentation

This section describes various methods by which users may generate ART technical documentation.

#### Question Marks

Entering question marks at the "Select ... Option:" prompt provide users with valuable technical information.  For example, a single question mark (?) lists all options which can be accessed from the current option.  Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock (if applicable) for each.  Three question marks (???) display a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for the option.

#### XINDEX

This utility analyzes routines to determine if they adhere to **V** *IST* **A** Programming Standards.  The %INDEX output may include the following components: Compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Global References, Label References and External References.  To run the XINDEX utility (DO ^XINDEX) for the ART package, specify the namespace **GMRA*** when prompted for routine names.

#### Inquire to File Entries

This VA FileMan option provides the following information about a specified option: option name, menu text, option description, type of option.  All fields that have a value will be displayed (e.g., Entry Action).  To secure information about the ART options, the user must specify the name of the options desired (File #19).  The options exported with this package begin with the letters GMRA.

#### Print Options File

Use this VA FileMan option to generate ad hoc reports about options from the Option file (#19).  The user may choose one, many or all ART options.  The options exported with this package begin with the letters GMRA.

#### List File Attributes

This VA FileMan option allows the user to generate documentation pertaining to files and file structure.  The ART file numbers 120.8-120.87. See the File List section of this manual for a specific listing.  Select the 'Standard' format to get the following data dictionary information for a specified file: file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates and sort templates.  In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-references, input transform, and date last edited.  Select the 'Global Map' format to generate an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates and sort templates.  For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the **V** *IST* **A** Kernel Systems Manual.

### Glossary

Table 7-Glossary

| Term                                   | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Adverse Reaction**                   | Any condition precipitated by a drug that requires patient treatment, admission or transfer; prompts a specialty consultation; or causes injury or death.  Every allergy is an adverse reaction, but every adverse reaction is not an allergy.                                                                                                                                                 |
| **Adverse Reaction Only**              | Something that is an adverse reaction but not an allergy.                                                                                                                                                                                                                                                                                                                                      |
| **Adverse Reaction Tracking**          | The software package that stores and reports the patient allergy or adverse reaction data.                                                                                                                                                                                                                                                                                                     |
| **Allergy**                            | A state of hypersensitivity induced by exposure to a certain agent                                                                                                                                                                                                                                                                                                                             |
| **Application**                        | A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.  Examples of  **V**  *IST*  **A**  applications are the MAS and Nursing modules                                                                                                                                                                            |
| **Application Coordinator**            | The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as Nursing, MAS, etc.                                                                                                                                                                                                                            |
| **ART**                                | See Adverse Reaction Tracking.                                                                                                                                                                                                                                                                                                                                                                 |
| **Causative Agent**                    | The name of the item which caused the patient to have a reaction (e.g., penicillin).                                                                                                                                                                                                                                                                                                           |
| **Data Standardization (DS)**          | The Data Standardization Program is the cornerstone of the VHA’s plan to share health information across the entire VHA system.  Data standardization establishes a consistent way of defining data that enables all sites in the VA health system to speak the same language and will ensure that data not only crosses from system to system, but retains the same meaning.                  |
| **Date/Time Chart Marked**             | In ART, this field indicates when the patient's chart has been marked to indicate this allergy or adverse reaction.                                                                                                                                                                                                                                                                            |
| **Date/Time ID Band Marked**           | In ART, this field indicates when the patient ID band or bracelet has been marked to indicate this allergy or adverse reaction                                                                                                                                                                                                                                                                 |
| **Date/Time MD Notified**              | A field in ART that indicates when the primary physician has been alerted about a patient allergy or adverse reaction.                                                                                                                                                                                                                                                                         |
| **Dechallenge**                        | Discontinuation/removal of allergen.                                                                                                                                                                                                                                                                                                                                                           |
| **GMR Allergies File**                 | A file of allergies/adverse reactions that are used by ART. The file number is 120.82.                                                                                                                                                                                                                                                                                                         |
| **GMRA MARK CHART bulletin**           | This bulletin is generated when providers enter allergies or adverse reactions in the ART package or through the CPRS “Enter Allergy or Adverse Reaction” window, accessed from either the CPRS Orders tab or Cover Sheet.                                                                                                                                                                     |
| **GMRA MARK CHART mail group**         | This is the group of people who are charged with the responsibility to see that all data entered into ART gets recorded in the patient's chart.                                                                                                                                                                                                                                                |
| **GMRA VERIFY ALLERGY bulletin**       | Warning that an allergy or adverse reaction has been signed off (completed) by the originator and that it is ready for the verification process.                                                                                                                                                                                                                                               |
| **GMRA-VERIFY ALLERGY security key**   | Should be given to all verifiers in ART.  Allows a verifier access to the verification process                                                                                                                                                                                                                                                                                                 |
| **Historical**                         | An allergy or adverse reaction that has been stated by some source versus one that has actually been witnessed by some personnel at this facility before initiation of new therapy.                                                                                                                                                                                                            |
| **Ingredient file**                    | A file (#50.416) which contains generic drugs which are components of various drug products.                                                                                                                                                                                                                                                                                                   |
| **Likelihood**                         | A measure of the probability that an allergy or adverse reaction was the cause of the patient problems indicated by the signs/symptoms.  This field is calculated via an FDA algorithm                                                                                                                                                                                                         |
| **Local Drug File**                    | The list of medications used at a particular VA facility. This file is also sent out by the  **V**  *IST*  **A**  Pharmacy developers. The file number is 50.                                                                                                                                                                                                                                  |
| **Mechanism**                          | In the context of ART, this is an indicator of whether the data for a patient is an adverse reaction only, or an allergy.                                                                                                                                                                                                                                                                      |
| **National Drug File**                 | This file is a list of drug products available which includes specific information for each product.  Information included for the products are trade name, NDC number, manufacturer, VA Drug Class code, dosage form, route of administration, strength and units, ingredients, ingredient strength and units, package code, package size, package type, VA product name and VA generic name. |
| **Observed**                           | An allergy or adverse reaction that has actually been witnessed by some personnel at this facility or reported by the patient, or his or her caregiver after initiation of a new therapy.                                                                                                                                                                                                      |
| **Patient Allergies File**             | The file where the patient allergy/adverse reaction data is stored in ART.  The file number of this file is 120.8.                                                                                                                                                                                                                                                                             |
| **Rechallenge**                        | Reintroduction of allergen after dechallenge.                                                                                                                                                                                                                                                                                                                                                  |
| **Severity**                           | This is an index of how the allergy/adverse reaction affected the patient.                                                                                                                                                                                                                                                                                                                     |
| **Sign/Symptom**                       | Something that could be subjectively or objectively measured that indicates an allergy or adverse reaction.                                                                                                                                                                                                                                                                                    |
| **Sign/Symptoms File**                 | A list of signs/symptoms that can be selected for a patient allergy or adverse reaction.  The file number is 120.83.                                                                                                                                                                                                                                                                           |
| **Top Ten Signs/Symptoms**             | A site-configurable set of indicators of an allergy or adverse reaction that is used to expedite data entry of these indicators.                                                                                                                                                                                                                                                               |
| **Treatment**                          | This is some lab test or drug intervention that was performed as a result of an allergy or adverse reaction.                                                                                                                                                                                                                                                                                   |
| **True Allergy**                       | A reaction triggered by the immune system; however, there are a vast number of symptoms or conditions caused by sensitivities that may or may not involve the immune system. A ‘true allergy’ COULD require patient treatment, admission or transfer, prompt a specialty consultation, or cause injury or death.                                                                               |
| **VA Drug Classification System file** | A file (#50.605) which contains the VA Drug Classification codes and their descriptions.  Each drug product in the National Drug file is assigned a primary code which is part of the information stored for each drug product in the National Drug file.                                                                                                                                      |
| **Verification**                       | The process of reviewing and approving the data entered by some clinical user.  This process is done by a verifier.                                                                                                                                                                                                                                                                            |
| **Verifier**                           | A person who has the GMRA-VERIFY ALLERGY security key.  This person can perform verification of patient data in ART.                                                                                                                                                                                                                                                                           |
| **VHA Unique Identifier (VUID)**       | A unique meaningless integer assigned to reference terms VHA-wide for data standardization.                                                                                                                                                                                                                                                                                                    |

### Appendix 1: CPRS (25 and 26) Release Notes Related to ART

#### PATCH OR*3*233

**Support for Allergy Synonyms** –Allergy synonyms, if present, are now included in the SIGNS/SYMPTOMS selection box.  This is included in patch OR*3*233, which will be distributed with GMRA patch 23.

#### GUI 26

The “Bulletin has been sent” message that CPRS displays after the user requests the addition of a new causative agent now includes the same warning included in the bulletin about that reactant not being added to the patient's record.

**Marking Allergies as Entered in Error Now Controlled by Parameter** - In CPRS v25, any user could enter new allergies, mark a patient as NKA (no known allergies), and mark allergies entered in error from the cover sheet and the detailed display window.  In v.26, the Entered in Error option requires the new parameter OR ALLERGY ENTERED IN ERROR to be enabled for the user.  The other options remain open to all users as before.

**Free-Text Signs and Symptoms No Longer Allowed** – To support of data standardization efforts, developers removed the ability to enter free-text signs/symptoms.  Users must now select items from the list of available signs/symptoms.

**Inconsistent Sending of Bulletin for Marked on Chart** – CPRS always sent the “Marked on Chart” bulletin if the user entered an allergy from the Orders tab.  CPRS never sent the bulletin if the user entered the allergy from the Cover Sheet.  This inconsistency has been corrected, and CPRS will never send the bulletin when the user enters a new allergy.

#### GUI 25

The following functionality is available only to sites that have installed OR*3.0*195, OR*3.0*216, and GMRA*4.0*21.  Sites that have not installed these patches will continue to receive the ART functionality that exists in CPRS GUI 24.

**Allergies No Longer Entered as Orders (NOIS: SHR-0603-71103)** – At sites that have installed the patches listed above, users can no longer enter allergies and adverse reactions as orders that are placed in the *ORDERS* file.  Patch OR*3.0*216 exports a modified order-dialog entry— *GMRAOR ALLERGY* —in the *ORDER DIALOG* file.  This entry enables CPRS to interact directly with the Adverse Reaction Tracking (ART) package (i.e., CPRS adds new allergies and adverse reactions directly into the ART package as users submit them).

With supporting patches OR*3.0*216 and GMRA*4.0*21, CPRS GUI 25 does not display allergy information on the **Orders** tab.  It displays allergy information only on the **Cover Sheet** tab.  Nevertheless, users can still enter allergy information from the **Orders** tab by selecting **Allergies** in the **Write Orders** pane. (i.e., users can still go to a familiar place to enter allergies.)

In addition, users can no longer select **OTHER ALLERGY/ADVERSE REACTION** as causative agent, nor can they select **OTHER REACTION** as a sign/symptom.  Changes to the ART package have eliminated these items as choices.  These changes mark a continuing effort to end free-text and unspecific entries.

If ‘type of causative agent’ references the field ALLERGY TYPE, the GUI interface doesn’t allow the user to enter this information.  It is determined internally by the selection made during the Reactant lookup process.

Also, CPRS now requires users to enter information about the nature of the reaction that they are documenting ( **Allergy** , **Pharmacological** , or **Unknown** ).

Finally, CPRS GUI 24 introduced a dialog through which users can request that a causative agent be added to their site’s *ALLERGIES* file.  Users access this dialog via a warning that pops up when they attempt to enter a free-text causative agent.  The warning dialog asks users to indicate—by clicking either its **YES** or **NO** button—if they want to send a causative-agent inclusion request.  In CPRS GUI 24, the default button was **YES** . In CPRS GUI 25, the default button is **NO** .  Furthermore, when users click the system **X** button (located in the top right-hand corner of each screen) to exit any of the screens that comprise the inclusion-request dialog, CPRS now cancels the request action.

**Allergy Changes on the Cover Sheet** - CPRS now enables users to perform several ART-related actions from the **Cover Sheet** tab—including the following:

- **Enter new allergy**
- **Mark selected allergy as entered in error**
- **Mark patient as having “No Known Allergies” (NKA)**

When users right-click within the **Allergies/Adverse Reactions** pane, CPRS displays a menu offering the three selections listed in the previous paragraph (or a sub-set, depending on the current Allergy information recorded for the patient).  When users left click to select one of the allergies listed within the **Allergies/Adverse Reactions** pane, CPRS opens a window that displays details about this allergy-as it always has.  However, this window now includes two additional buttons: **Add New** and **Entered in Error** .  As the names of these buttons suggest, clicking them enables users to add new allergies and designate the selected allergy as entered in error, respectively.  When users mark allergy entries as entered in error, the ART package notifies (via MailMan bulletins) sites’ GMRA MARK CHART mail group.

Depending on how sites have configured their *GMR ALLERGIES SITE PARAMETERS* files, the ART package could also send bulletins to one or more of the following mail groups:  GMRA VERIFY DRUG ALLERGY, GMRA VERIFY FOOD ALLERGY, and GMRA VERIFY OTHER ALLERGY.  In addition, marking an allergy entry as entered in error triggers the Text Integration Utility (TIU) package to generate an Allergy/Adverse Reaction progress note that is sent to the originator to document the erroneous entry.  Whether users enter new allergies via the **Cover Sheet** or **Orders** tab, CPRS displays an **Enter Allergy or Adverse Reaction** dialog, through which users enter adverse reactions and allergies directly into the ART package.  This dialog includes several changes, including the following changes:

CPRS no longer allows users to enter future origination dates or future dates for observed allergies; if users attempt to enter future dates for these items, CPRS prevents them from doing so when they click OK to submit their allergy entries

A new button containing a question mark is associated with the Severity dialog; when users select this button, CPRS displays a text box defining severity selections

CPRS displays a hover hint when users mouse over the Observed and Historical option buttons; a user group (as opposed to OI staff) specified the text of the hover-hint

When the amount of text in the Comments dialog exceeds its viewing area, CPRS adds a scroll bar to the dialog

Developers altered the tabbing sequence to more closely match users’ expectations

When an allergy is marked as “Entered in Error,” Drug allergy, this action generates a Progress Note for the user who marked it as “entered in error” to sign.  Once the user who marked the allergy as entered in error or an administrative user signs the note, all CPRS users can view the note to know that an allergy has been removed from the list.

When an allergy is entered as an “Observed, Drug allergy,” this action generates a Progress Note for the user who entered the Allergy/Adverse reaction to sign.  Once the user who made the entry or an administrative user signs the note, all CPRS users can view the note.

The **Enter Allergy or Adverse Reaction** dialog also contains a new check box: **ID Band Marked** .  If the patients are inpatients and the sites have set the MARK ID BAND parameter in the *GMR ALLERGY SITE PARAMETERS* file to **1 (YES)** , users can select this check box to indicate whether they have marked allergies and adverse reactions on the patient’s identification (ID ) bands.  If users submit an allergy entry without selecting activated **ID Band Marked** check box, the ART package automatically notifies sites’ GMRA MARK CHART mail group via a MailMan bulletin. *GMR ALLERGY SITE PARAMETER* file settings also determine to which verification mail groups (GMRA VERIFY DRUG ALLERGY, GMRA VERIFY FOOD ALLERGY, or GMRA VERIFY OTHER ALLERGY) the ART package sends MailMan bulletins when users enter specific combinations of allergy information.

#### Deleting an Assessment of NKA

From within the ART package, it is now possible to delete an assessment of NKA.

When you select a patient for entering/editing allergies and that patient doesn't have any active allergies on file, the “Does this patient have any known allergies or adverse reactions?” prompt is presented to you.  If the patient has no assessment, there is no default answer.  If the patient has been assessed as NKA, the default is NO.

In the case where the default answer is NO (meaning, the patient is NKA), you may enter an @ sign to indicate that the assessment should be deleted and the patient should be returned to the 'not assessed' state.  This would be used in those rare cases where an assessment is erroneously assigned to the wrong patient.

Examples:

1) Patient who is currently not assessed:

Select PATIENT NAME: **ARTPATIENT,ONE** 456334567     YES     MILITARY RETIREE      THIS IS A TEST

Does this patient have any known allergies or adverse reactions? :

2) Patient who has been assessed as NKA:

Select PATIENT NAME: **ARTPATIENT,ONE** 456334567     YES     MILITARY RETIREE      THIS IS A TEST

Does this patient have any known allergies or adverse reactions? : No//

At this point, if I enter a ?, I see what my choices are:

Choose from:

1        Yes

0        No

You may also enter @ to delete a previous NKA assessment and return the patient to a 'not assessed' state.  Use this if the NKA assessment was previously incorrectly entered.

Does this patient have any known allergies or adverse reactions? : No//

The information regarding the use of the @ will only show if the patient is currently NKA.  If they are not, then it doesn't show.

3) Finally, here's what it looks like when you delete the assessment:

Select PATIENT NAME: **ARTPATIENT,ONE** 456334567     YES     MILITARY RETIREE      THIS IS A TEST

Does this patient have any known allergies or adverse reactions? : No// **@**

Assessment deleted.

### Appendix 2: ART Data Standardization FAQ

#### ART Data Standardization FAQ

Is there a checklist of everything sites need to do to standardize the Allergy/Outpatient Pharmacy domains?

The release notes for the GMRA*4*23 patch provide a list of patches in the order that they need to be installed in [.  To view the release notes, please click this link](https://www.va.gov/vdl/documents/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/gmra_4_23_rn.pdf) .  This list of patches and other activities that need to be completed are also available in the PowerPoint slides that were sent to the sites. Can sites continue to enter local allergies after standardization is complete?

No.  The files have been locked down and local additions for allergies are not permitted.  The ability to enter free-text additions to the GMR Allergies file 120.82 was taken away from sites two years ago.  Removing the ability to enter free-text additions to the Sign/Symptoms file 120.83 was included in the standardization process.  Sites can request additions to the GMR Allergies file 120.82 and to the Sign/Symptoms file 120.83 through the New Term Rapid Turnaround (NTRT) process.  Please see the NTRT process section of this document for more information.

What will happen if different sites have different attributes, such as drug ingredients, designated to the same inactive term for entries in GMR Allergies file 120.82?  Will the attributes stay the same after standardization at each site?

The attributes will stay the same, including drug classes and drug ingredients, for inactive terms after standardization is complete.

What happens to local allergies in GMR Allergy file 120.82 that are currently on file when standardization occurs?

If a local allergy on file is in the standard, then the term will remain active, but all of the term attributes (e.g. synonyms, drug classes and drug ingredients) will be overwritten by the standardized file.  This standardized term will be available for recording new allergies in the future.

If a local allergy on file is *not* in the standard, then the term will become inactive, and all term attributes (e.g. synonyms, drug classes and drug ingredients) will remain the same, and the data, if applicable, will be available for order checks.  However, this term will not be available for selection when recording new allergies.

Is there a Sign/Symptom term called “other” in the new standard for file 120.83 Sign/Symptoms?

No.  “Other” does not exist in the list of standardized terms for Sign/Symptoms file 120.83. If there is a term that is not available in the Sign/Symptoms list and it needs to be added, please enter an NTRT request.  See the NTRT process section of this document for more information.

What does the allergy “contrast media” look like in the new standard for GMR Allergies file 120.82?  Will the new standard also contain the many drug classes associated with this allergy?

The contrast media allergy is in the standard GMR Allergies file 120.82.  In the standard, this allergy also includes the many drug classes that are associated with this entry.  We encourage sites to review and ensure that the standard is comprehensive.  Compare the drug ingredients and drug classes that have been recorded in your site’s file with what is in the standard.

If differences exist between what is in the standard and what is in your file, your site data will be overwritten.  Submit an NTRT request if you believe that drug classes, drug ingredients, or synonyms should be included in the standards that are not included.  Please see the NTRT process section of this document for more information.

Should a local allergy of “Bufferin” be changed to Aspirin in the GMR Allergies file 120.82?

No. Sites are not being asked to change local allergies in the GMR Allergies file 120.82.

Will non-standard (inactivated) terms continue to be used for order checking? How?

Yes.  Although inactivated terms are not available for new documentation, those that have been stored in patients’ records will continue to be used for order checking.  The internal entry numbers (IENs) of the inactivated terms have been preserved, and it is the IENs that are needed for order checking.

When will sites receive the standard for GMR Allergies file 120.82 and Sign/Symptoms file 120.83, so they can start comparing it against their local files?

These files were sent to the sites by the HDR Implementation managers.  If you have not received them, please contact your HDR Implementation manager.

What is the work-around for a site, if the item that the patient is allergic to is not found in the standard GMR Allergies file 120.82 and the terms needs to be entered as an NTRT request?  How does the end user document that a patient is allergic to an item that is not in the standard?

The ability to enter free-text allergies in GMR Allergies file 120.82 was taken away from sites two years ago.  Please continue to use your site-developed processes to handle this documentation.

Currently, there is a message or pop-up box telling an end user in CPRS that the allergy term they are searching for was not found, but that they can request that it be added (Figure 1).  However, this message box is not available if a Sign/Symptom is not available.  What is the desired work-around for a site to request that a Sign/Symptom term be added, since they will not have the instructions from this pop-up box?

<!-- image -->

Figure 1.  Causative Agent Not On File Dialog

**Sites may wish to handle these additions in the same manner as when requesting a** new reactant, or they may wish to handle it differently.  We recommend that sites communicate to the end users their desired work-around for handling these requests for additions of Sign/Symptoms.

End users are encouraged to update the patient record with the Sign/Symptom term when it becomes available in the standard.  End users can enter free text Sign/Symptoms until CPRS GUI v26 is installed.  However, these additions of free text Sign/Symptoms prior to CPRS GUI v26 release are highly discouraged.

What are sites being asked to do regarding the Top 10 List for Sign/Symptoms?

After standardization, the Top 10 List for Sign/Symptoms file #120.83 may have inactive terms.  The GMRA REQUEST NEW REACTANT mail group will be notified of inactive Top 10 terms at your site after the VETS push has occurred.  Sites are being asked to replace inactivated terms with standard terms as soon as possible, to prevent end users from viewing empty space in the GUI.  If the inactivated terms are not replaced by active terms in the standard, the end user will need to click on the scrollbar for the Sign/Symptoms.  This will cause the empty space to be auto-adjusted and the gap will no longer display in the GUI. CPRS GUI v26 will fix this so that there is no blank space.

It is possible to receive an email indicating that there are terms on the top ten list that need to be updated, but those terms do not appear when using the option to edit the terms.  Some sites actually have more than 10 terms stored in the top 10 list but only the first 10 show to the user.  If one of the additional terms is now inactivated, it will be included in the update message although you won’t actually see it in the list.

If the e-mail update message contains terms that do not appear to be on your Top 10 list, you may ignore those terms.  This problem will be fixed in a future patch.

To change inactive entries:

1. Use the Menu Option GMRA SITE FILE. The parameter is HOSPITAL.
2. Enter the number of the Sign/Symptoms that you need to change.

Why are sites getting e-mail messages about order checks to the GMRA mail group as the patch is being loaded and post routines are being run from this GMRA*4*23 patch?

Receipt of these messages is a result of the updates that are occurring to the Patient Allergy file 120.8 when GMR Allergies file 120.82 is standardized.  Any time a file 120.82 entry has a change of drug classes or drug ingredients, and a patient has a previous allergy recorded to this entry, then the new drug classes or drug ingredients will be propagated to the Patient Allergy file 120.8.  The purpose of the message is to inform the Allergy Clinical Application Coordinator of the possibility of a missed order check based on the updated allergy information. Order checks only occur when the order is placed, which means that updated allergy information is not compared against existing orders.  During the update, the new allergy information is compared against the patient’s active orders to determine if there are any possible drug-allergy conflicts based on the new information.  There is a slight possibility of a false-positive report but each entry should be reviewed for a possible drug-allergy interaction.

What is the name of the mail group that will receive the e-mail notifications regarding order checks, as mentioned in the previous question?

The GMRA Request New Reactant mail group will receive these order check notifications through e-mail.

How can we record that a patient has No Known Allergies (NKA), when this term is not included in the standard for GMR Allergies file 120.82 and will be inactivated for future selection?

Enter no-known-allergies (NKA) assessments for patients who have no active allergies by taking the following steps in the CPRS GUI from the Coversheet:

1.	Right-click within the Allergies/Adverse Reactions pane.

2.	From this menu, select “Mark patient as having No Known Allergies (NKA).” CPRS displays the No Known Allergies dialog.

Note : CPRS will allow you to record a patient as having No Known Allergies (NKA) only for patients who have no active allergies.  When patients have active allergies, CPRS deactivates this menu selection.

3.	Click OK.

Can we continue to record allergies and No Known Allergies (NKA) from the Write Orders menu in the CPRS GUI?

Yes.  You can continue to record new patient allergies or NKA from the Write Orders menu, or on other site-configured menus on the Orders tab in the CPRS GUI.

How do we record that the patient has an “unknown reaction,” since this term is not included in the Sign/Symptoms file 120.83 for selection when recording a patient allergy reaction?

In CPRS GUI v25 you can still enter free-text Sign/Symptoms.  This option has been disabled in List Manager.  In the GUI, you must press &lt;Enter&gt; after you type the free-text Sign/Symptom.  It is also possible to leave the Sign/Symptoms field blank and make a note in the Comment field that the Sign/Symptom is unknown.  Typing free-text Sign/Symptoms will not be possible with CPRS GUI v26.  This FAQ will be updated when more information is available.

Will sites need to continue to update the Top 10 list of Sign/Symptoms when each NTRT push occurs?

Yes.  If the new NTRT push inactivates entries on the Top 10 list of Sign/Symptoms, then an e-mail message will be sent to the “GMRA Request New Reactant” mail group.  The message will list which terms have been inactivated and remind sites to use the menu option GMRA SITE FILE to correct these entries.

Details of what was contained in the NTRT push can be learned from the Automated Notification Report (ANR) message that will be sent, or from the NTRT Web site.  The content list for a push will give you an idea about alternative terms that would be appropriate replacements for inactivated terms.  If you are not currently receiving the ANR messages, please log a Remedy ticket to be added to the distribution of these messages.

If the e-mail update message contains terms that do not appear to be on your Top 10 list, you may ignore those terms.  A problem has been identified where some sites have more than ten entries in their Top 10 list.  This problem will be fixed in a future patch.

What is an example of a Top 10 List term that may need to be replaced due to an NTRT push?

The Enterprise Reference Terminologists are currently going through the standard for file 120.83 Sign/Symptoms and changing the primary terms to more user- or clinician-friendly terms.  For example, in the most current update, some terms such as “Aptyalism,” “Face Goes Red,” and “Cutaneous Eruption” are being made inactive as primary terms, but are being added as synonyms to other primary terms.  See question six in the NTRT section of this document for additional information.

In the Top 10 list, you may need to update the Top 10 list to display the updated active terms.

Table 8-Example of Updated Active Terms

| INACTIVATE as Primary term  (Added as Synonym)   | ACTIVATE as Primary term   |
|--------------------------------------------------|----------------------------|
| **Aptyalism**                                    | **Dry Mouth**              |
| **Face Goes Red**                                |                            |
| **Cutaneous Eruption**                           | **Rash**                   |


#### VA  Terminology Services (VETS) Push and Deployment Questions

1. How long will it take for a large integrated site to complete the cross-referencing of all the files after the initial VETS push or deployment has occurred, for the Allergy/Outpatient Pharmacy domain?

It is estimated to take three hours.  This is approximately the amount of time it took a large integrated test site to complete this process.

What happens to an end user who is entering an allergy on a patient when the VETS push or deployment occurs?

There are not any effects visible to the end user who is entering in allergies while a VETS push or deployment is occurring.

Has this software been tested in production and the impact assessed for the use of Bar Coding Medication Administration (BCMA) and passing medications during the VETS push or deployment?

Yes.  The three test sites reported that there were no reports of any adverse impacts to BCMA.  Also, the software quality assurance testing included BCMA testing by the pharmacy team.

When will the VETS pushes or deployments occur?

The VETS pushes or deployments will be scheduled with the sites, most likely on a regular schedule to be determined.  The deployments or pushes will be coordinated with the site, the HDR Implementation Manager, and the ERT team.  The site will be notified prior to a VETS push.

Do sites need to have staff on site when the VETS push or deployment occurs?

No.  Site Staff do not need to be present when the VETS deployment or push occurs.

Is the VETS push or deployment  equivalent to a patch load?

No, a push is not the same as a patch load. The VETS push or deployment is the final step in the standardization of the files after patches are loaded.  These pushes or deployments will also continue as new terms are requested from the field.  The pushes are HL7 messages that are sent through the interface engine to VistA.

Is the VETS push or deployment a site-initiated process?

No, it is not.  However, the site will be contacted prior to the VETS push or deployment.

#### New Term Rapid Turnaround (NTRT) Process Questions

1. How fast will the NTRT request be granted? Are weekends taken into consideration?

At this time, NTRT requests will be deployed nationally every Thursday.  The cutoff date for inclusion of a term in the Thursday deployment is COB the Friday before the scheduled deployment.  Over the next 7 months, this timeframe may be adjusted.  Any changes to the frequency of NTRT deployments will be communicated to sites and support personnel.

If there are a large number of New Term Rapid Turnaround (NTRT) requests at a site, is it necessary to enter each request separately?

If sites have a large number of NTRT requests that need to be submitted, your HDR Implementation Manager can help you get these entries to the ERT team without having to enter all of the requests into the NTRT website.

If there is a local term that is a synonym of a national standard term, then is an NTRT request needed for that local term?

No.  The local term will not need to be added to the standard.  If there is a compelling case for why it should be added, then that can be forwarded on as an NTRT request.

Consider the following example:

Table 9-Example of Not Adding the Local Term to the Standard

| **Local Term**   | **New Standard Term**             | **Add to standard?**                                     |
|------------------|-----------------------------------|----------------------------------------------------------|
| Garbanzo beans   | Chickpeas  Synonym	Garbanzo beans | No.  Synonyms are available for searching terms in CPRS. |

If a new drug ingredient is needed, do we go through the NTRT process or will these still be handled through National Drug File (NDF) updates?

New drug ingredients will need to be added through the NDF process.

How has the issue related to Sulfa allergy documentation and order checking in  been resolved?

A generic Sulfa entry in the GMR Allergy file (120.82) will be deployed nationally.  Standardization identified the need for consistent screening for Sulfa-containing drugs.  The Data Standardization and Enterprise Reference Terminology teams have worked with the National Drug File manager to determine which drugs need to be linked to the new generic sulfa entry in the GMR Allergy file 120.82.  Once deployed, order check screening for Sulfa allergies will work consistently and completely on all  systems.

Concerns have been raised about user-friendly terms and equivalents in the Sign/Symptoms file 120.83 from some sites.  What is being done to resolve these concerns?

A review of the Sign/Symptoms file 120.83 is underway.  The group reviewing this file is comprised of clinicians from the field, as well as terminologists and other key stakeholders.

Concerns have been raised from sites regarding clinical terms that are not user-friendly.  For example, “cutaneous eruption” is the primary term in the standard and “Rash” is a synonym.  Primary terms are stored in the patient record and on the patient arm band.  Clinicians would like to see Rash become the primary term and cutaneous eruption the synonym.  A complete review of the standard is being conducted to identify other terms that may also benefit from a similar change.

Concerns have been raised that some terms in the standard are not equivalent and should not remain as synonyms to the primary term.  For example, “Congestion of the Throat” is not the same as “Swelling of the Throat” and should be fixed in the standard.  Other non-equivalent synonyms are being identified and will be associated with two separate terms when applicable.

Another area of need is documenting the business rules that apply to the standard, and only modifying the standard in a way that is consistent with those rules.  This issue is being addressed and documentation is pending.

How are sites being notified that NTRT additions are being made to the standardized files for Allergies?

An Automated Notification Report (ANR) is being sent out through the National Help Desk by e-mail messages that alert sites about the changes that are being made to the Sign/Symptom file 120.83 and the GMR Allergies file 120.82.  If you are not currently receiving these ANR messages and would like to in the future, please submit a Remedy ticket and you can be added to the distribution list for future information.

The information about the changes being made by NTRT can also be viewed on the NTRT Web site, under “NTRT Deployment Log.”  Those interested can also join the NTRT listserv which provides the same information as the ANR messages, along with the potential for supplementary information.

Is it true that sites are not to update or change the resource slots associated with the GMRA UPDATE Resource device?

Yes.  The slot is set to one and needs to stay at one. It is very important that sites not change the number of slots for this resource device.  If the resource device does not stay at one, then NTRT pushes may be processed inaccurately and may potentially corrupt Allergy files.  If sites have changed this, they need to set it back to one.  Then sites will need to work with the ERT team for a redeployment of the push. ERT is looking at ways to control the order in which updates are done in the future.  However, in the meantime sites need to be aware of this potential issue and to monitor the GMRA UPDATE Resource device to ensure it stays set at one slot.

#### Site Clean-up Questions

After allergy standardization, what is the impact to a site that has many free-text patient allergies that need to be cleaned up?

Sites will be able to continue cleaning up the free-text patient allergy entries after Allergy/Outpatient Pharmacy standardization is complete.  The patches will not affect this clean-up effort.  After standardization, there will be a more comprehensive list of allergies for your site to use for cleaning up free-text patient allergy entries.

New terms should not be added to GMR Allergies file 120.82 prior to standardization in order to map a free text patient allergy.  The GMRA*4*23 patch locked down this file so sites can no longer add terms through the roll-and-scroll interface.  Sites should clean up the patient allergy file 120.8 prior to standardization with what is currently available.  Once standardization is complete, more terms will be available in the GMR Allergies file 120.82 to correct the remaining free text patient allergies.

An automated clean-up patch is being written to help sites in the free-text patient allergy clean-up effort.  This patch will be released sometime after the standardization patches.  The content required for this patch is currently being reviewed.  Sites have been asked to clean up free-text entries that have a low number of occurrences.  Free-text patient allergies that occur one or two times in the clean-up utility should be cleaned up first.  Also, free-text patient allergies that have multiple allergies on one line (e.g. “Aspirin, Penicillin, chocolate”) should be cleaned up by recording each allergy separately for that patient.

The automated clean-up patch will help sites clean up free-text patient allergy entries, but not all data can be cleaned up in an automated fashion.  Patient allergy data that has clinical relevance will be left as free text and will need to be cleaned up by the site.

What is the impact of Outpatient Pharmacy standardization to sites if they have not finished linking local drugs to the National Drug File (NDF)?

Sites can continue to clean-up the local drug file or file 50 mapping to the National Drug File (NDF) after standardization.  The data in the local drug file needs to be mapped so that order checks work optimally.

#### Health Data Repository (HDR) Questions

What happens in the Health Data Repository (HDR) when one site has entered an allergy for Penicillin and another site has entered Penicillin as “entered in error”?

Allergies that are entered in error at one site will not overwrite the allergies recorded at another site.  The HDR will err on the side of safety.  The HDR will store both pieces of information: the patient allergy record and the “entered in error” record.

In regards to the question above, will one site be notified that another site has entered an allergy in error?

At this time, there is not a mechanism to do this.  Site-to-site notification will not be done until a national process is put in place that determines when a site’s allergy record can be overruled.  The clinician should get the information via Remote Data Views (RDV) and work with the patient to make sure the record is correct.

Where do we go for technical information about turning on the VDEF triggers?  Is that something HDR Implementation Managers will help with?

Yes.  The HDR Implementation Mangers will be in contact with sites when it is time to turn on the VDEF triggers.  They will communicate the necessary technical steps at that time.

In the CPRS GUI, the end user now sees that a light is blue on the HDR section of Remote Data Views (RDVs).  Why is this there?

HDR data can now be seen in RDV.  Vitals data has been standardized and it is being sent to the HDR.  This blue text means that the patient has vital sign data stored in the HDR.  With the release of CPRS GUI v. 26, end users will be able to view data from the HDR.

This may be confusing to some end users, because some patients will only have vital sign data available at the local site and the light will not be blue.