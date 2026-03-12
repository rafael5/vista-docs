---
app_name: 'CPRS: Adverse Reaction Tracking (ART) (GMRA)'
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
package_id: GMRA
patch: null
patch_gap: null
section: ''
source_file: gmra_4_26_rn.docx
status: draft
title: gmra 4 26 rn.docx
---

<!-- image -->

**ADVERSE REACTION TRACKING**

**Release Notes**

Version 4.0

GMRA*4.0*26

March 2007

Health Provider Systems


**Table of Contents**

GMRA*4.0*26 - Remote Data Interoperability (RDI) update	1

Important Note!!	1

Description of Changes	1

Order Checks for Allergies to Drugs	1

GMRA UPDATE RESOURCE	2

Upcoming Related Patches	3

Other Recent ART Patches	3

ART Data Standardization FAQ	12

VA Enterprise Terminology Services (VETS) Push and Deployment Questions	17

New Term Rapid Turnaround (NTRT) Process Questions	18

Site Clean-up Questions	21

Health Data Repository (HDR) Questions	22

**GMRA*4.0*26 Release Notes**

### GMRA*4.0*26 - Remote Data Interoperability (RDI) update

### Important Note!!

This patch must be installed immediately before the installation of patch OR*3.0*232, which is the Order Entry/Results Reporting portion of the Remote Data Interoperability project. This project’s aim is to include DoD and VA-wide data in the data set used to perform order checking on new patient orders.

### Description of Changes

GMRA*4.0*26 provides the Remote Data Interoperability (RDI) project the ability to use remote allergy data when determining drug-allergy order checks.

The remote data will come from the Health Data Repository (HDR) and that data will be used to determine if an order check should be given on the local system for the drug being ordered.

#### Order Checks for Allergies to Drugs

- Drug Allergy Order Check upon Placing a Medication Order
    1. At the time an outpatient or inpatient medication order is entered into the Computerized Patient Record System (CPRS) by a provider, CPRS will provide the details of the order to the Adverse Reaction Tracking (ART) application. If known, CPRS will also provide the standardized VUID (VHA Unique Identifiers) of the drug from the VA Product file (#50.68).
    2. ART will check the patient’s active allergies to attempt to determine if potential allergy-drug interactions exist.
        - ART retrieves active allergies from HDR-Hx and HDR-IMS via a CPRS API call to CDS and include those in the drug allergy-drug order checks.
        - ART queries the National Drug File Pharmacy application for the drug ingredients and the drug classes associated with the product, and compares the ingredient and drug class information against the information on file for the patient.
        - The first check is on the ingredients; if no match is found, the next check is for drug classes.
    3. ART provides any potential interactions to CPRS, and CPRS notifies the ordering provider if potential interactions exist at the time the order is entered and before the order is signed.

- **ART converts VUIDs to IENs if necessary**

If RDI sends a drug ingredient or drug class VUID to ART, ART calls an API to convert drug ingredient VUIDs to IENs and drug class VUIDs to drug class codes in order to accomplish order checking.

- **Display of Potential Drug Allergy Interactions**

At the time the order is entered, CPRS will display, in a pop-up window, any potential drug-allergy interactions.

##### 1 Outpatient Pharmacy and Allergies

Outpatient Pharmacy calls a CPRS API to retrieve the patient’s allergy information from all sites where the patient has been seen in order to perform allergy/adverse reaction checking.

- **Inpatient Medication Drug Allergy Order Checks for Backdoor Orders**
    1. When a new order is entered, a pending order is finished, or an order is copied or renewed in the Inpatient Order Entry [PSJ OE] option, the Non-Verified/ Pending Orders [PSJU VBW] option, the Order Entry [PSJU NE] option, or the Order Entry (IV) [PSJI ORDER] option, a call is made to the ART order checking API, which returns any drug allergy information to Inpatient Medications, including the site where the allergy was entered.
    2. If interactions exist, this information is displayed to the finishing pharmacist to be acted upon. This display includes the name of the site where the drug order and/or allergy interaction originated.
    3. RDI allergy calls are made for entry of Non-VA med and also when a RAD order that is marked for contrast media is entered.

#### GMRA UPDATE RESOURCE

ADI (Allergy Domain Implementation/Data Standardization) uses a resource device to control the updating of existing patient allergies. When changes are made to existing allergy definitions in file 120.82, all associated patient allergies in file 120.8 are updated to match the new definition of the entry from 120.82. The resource device controls the updating process. Because of the way the updates are implemented, the resource device needs to manage the updates one at a time. As a result, the resource slots field is set to one and should not be changed.

### Related Patches

**GMRA*4*37 - Add Remote Data To Contrast Media Order Checks**

Patch GMRA*4*37 will expand RDI functionality to include remotely entered allergy data when determining if there is a contrast media allergy when ordering radiological procedures.

**OR*3*267 -  Remote Contrast Media Order Checking**

The purpose of this patch is to implement changes related to CONTRAST MEDIA order checking. The specific changes occur in the OE/RR EXPERT SYSTEM in order to allow the display of the designation for the facility on the order checks when an allergy is found to be against a remotely recorded allergy. The changes to implement the actual usage of remote data for CONTRAST MEDIA order checks are located in patch GMRA*4.0*37.

### Other Recent ART Patches

**GMRA*4*36 - Eliminate Originator Delete**

Previously, if a user edited an existing allergy in  that had the ORIGINATOR SIGN OFF (15) field in the PATIENT ALLERGIES (120.8) file set to “no,” the user would be given the option to delete the entry.

With the Health Data Repository (HDR) now in place for allergies, deletions of data that are already part of the HDR can’t be allowed. As a result, any existing allergy that hasn't been “signed off” will be marked entered in error if the user chooses to “delete” the entry.

In a previously released patch, a post-installation routine identified allergy entries that should have been auto-verified but weren't, due to a logic issue. Those entries were then auto-verified as they should have been. When those entries were auto-verified, the ORIGINATOR SIGN OFF (15) field in the PATIENT ALLERGIES (120.8) file should have been set to yes.

A post-install routine, GMRAY36, has been added to this patch to identify and fix any auto-verified allergies that have the ORIGINATOR SIGN OFF (15) field set to “no.”

The post-install will also review existing allergy entries to make sure that the ALLERGY TYPE (3.1) field in the PATIENT ALLERGIES (120.8) file is consistent with its corresponding entry in the GMR ALLERGIES (120.82) file. Prior to this patch, any changes to the ALLERGY TYPE (1) field in GMR ALLERGIES (120.82) file made by the standardization team would not have updated existing patient allergies. The ALLERGY TYPE (1) field in the GMR ALLERGIES (120.82) file has also been updated to include a new style cross-reference that will now update existing patient allergies, should the value change. The new style cross-reference will be added during the post-install.

The post-install will also make sure that the name of the reactant that is stored in the PATIENT ALLERGIES (120.8) file matches the name of the reactant from the GMR ALLERGIES (120.82) file. Prior to standardization, it was possible for a site to change the name of a locally entered allergy without that change updating existing allergies.  The post install will check existing allergies associated with the GMR ALLERGIES (120.82) file and make sure the reactant field matches the name of the allergy.

The post-install will also identify any patient allergies that are associated with an entry from the GMR ALLERGIES (120.82) file that is inactive and convert it to a free text entry.

Finally, the post-install will check for patient allergies that are associated with the DRUG (50) file. While the DRUG (50) file may no longer be selected from, there are pre-standardization entries that may be pointing to locally created entries in the DRUG (50) file that did not have ingredient and/or drug class information. In cases where the entry doesn't have appropriate drug information, the allergy will be converted to a free text entry.

This patch updates the GMR ALLERGIES (120.82) file so that the DRUG INGREDIENTS (4) multiple will only allow primary ingredients to be selected. The DRUG INGREDIENTS (2) multiple in the PATIENT ALLERGIES (120.8) file has had this restriction for quite some time.  This update will get them in synch.  As the GMR ALLERGIES (120.82) file is standardized, this change has effectively been in place since standardization but this will assure compliance.

This patch also fixes the problem where a user may have been asked the “have the ID BANDS been marked” question more than once when entering or verifying allergies in the roll-and-scroll environment.

During internal testing, it was noted that in the roll-and-scroll package, when the user is asked “does the patient have any known allergies or adverse reactions,” an entry is created in the ADVERSE REACTION ASSESSMENT (120.86) file before the question is asked. If the user hits return or enters an “^,” the entry is then deleted from the file.  This causes unnecessary traffic to the HDR. The entry is now created after the question is answered by the user.

NOTE:

A mail message is sent to the installer indicating the total number of entries that were converted to free text. When patch GMRA*4*29, currently in testing, is installed most of the entries that were converted to free text will be automatically updated to a standardized term.  As a result, you do not need to take any action on the newly created free text entries at this time.

**GMRA*4*35 - Possible Problem With List By Location Unassessed**

When a user ran the report List by Location of Undocumented Allergies [GMRA PRINT-PATIENTS NOT ASKED] option, the listing showed a patient that had allergies, were autoverified, and should not have shown up on the list

Resolution:

A notation message was added to the code to further help the user in how to run the report:

“Please note! This report will show patients as not having received an assessment if the assessment was entered after the end date of the range.  For this reason, it is recommended to end the range with today. This can be done with an entry of 'T' (for Today) at the 'Enter END Date (time optional): T//' prompt.”

Remedy Ticket: HD67868 -  ALX-0204-70164  Possible problem with List by Location Unassessed Allergies

GMRA*4*34  - Update to HL7 messages

In patch GMRA*4*23, routines were distributed to send HL7 messages containing allergy data to the Health Data Repository (HDR). This patch adds a check for HL7 control characters that are embedded in text type data elements in the HL7 message and converts these control characters to the correct HL7 Escape Sequence.

**NOTE** You must suspend the VDEF Request Queue before installing this patch and then re-enable it after installation of the patch.  The steps for doing that are outlined in the installation instructions.

**GMRA*4*31 - Check for compiled cross-references in file 120.8**

In preparation for the installation of the data standardization related patches, sites needed to check to see if file 120.8 compiled cross-references.

Patch GMRA*4*23, which installed the necessary data dictionary updates in support of the allergies data standardization, added some new cross-references to file 120.8.

In some cases, sites may have compiled the cross-references on file120.8.  If that is the case, then the cross-references that will be added by patch GMRA*4*23 won't be executed as a result of the compilation of the existing cross-references.

In general, the only sites that will have this problem are integrated sites. In some cases, during the integration of the site's database, the cross-references for file 120.8 may have been compiled. In order to ensure that file 120.8 does not have compiled cross-references this informational patch was provided to give directions on how to identify and fix this issue if it existed on a local system.

**GMRA*4*30 - Prevent Deceased Patients From Appearing On Report**

This patch addresses Remedy ticket HD67463, where deceased patients are appearing on the Patient Not Asked Report [GMRA PRINT-PATIENTS NOT ASKED].

The sites use this report to identify patients who have not had an allergy/adverse reaction assessment. The sites then follow up with the patients on the list to get the allergy information. By preventing deceased patients from appearing on this list, the sites will not be attempting to contact the family of a deceased individual for this assessment.

**GMRA*4*29 - Automated clean up of free text allergies**

This patch finds all active free text allergies and updates the entry in one of three ways.

1. If the free-text term is found in the conversion matrix, then the term will be updated to the associated term from the matrix. The conversion matrix is loaded into the ^XTMP global when the patch is installed and is used to determine if there is an update that can be done.
2. If the free-text term is not found in the matrix or if the term to update to would cause a duplicate term, then the free-text term is updated to include the phrase (FREE TEXT) after the term. This will now serve as a visual cue that the term is a free-text term and will not be considered during order checking.
3. Finally, if the matrix indicates that the term is an erroneous term, then the allergy will be marked as entered in error.

When the post-install has reviewed all active free-text allergy terms, a mailman message is sent indicating the outcome of the conversion. The report includes the number of entries that were updated, any entries that couldn’t be updated, and the reason. Upon completion of the update, the allergy free-text utility can be used to review the remaining free text entries for manual updating.

For more information about patch 29, see the VistaU CPRS Monthly Teleconference February 2007 presentation: REDACTED

**GMRA*4*27 - Allergy Order Check Does Not Fire For Contrast Media**

PSI-05-054 documents a patient safety issue due to allergy bulletins not being fired if the contrast media has a VA DRUG CLASS of DX109. This patch corrects the problem.

**GMRA*4.0*25 - BLANK SIGN/SYMPTOM PROBLEM**

Patient Safety Issue - PSI-05-049 identifies a problem where an allergy may be stored without the corresponding drug classes or drug ingredients.  As a result, order checking may not occur as expected.

In version 25 of the GUI, a change was made to the way allergies are entered.  When the list of signs/symptoms is displayed on the form the site’s top ten entries are listed first, followed by a space and a dashed line and another space. It’s possible for the user to accidentally select the dashed line or the space as a sign/symptom. When this happens, the system fails when attempting to store the allergy data.

With this update, the allergy package will no longer attempt to store non-existent signs/symptoms.

This patch also contains a post-installation routine that attempts to identify any allergies that may not have been saved correctly. Upon completion of the post-install, a report is generated listing any patients and their associated allergies that need to be reviewed. In general, the best course of action is to mark the existing allergy as entered in error and then re-enter the allergy information to make sure all required data is accounted for.

**GMRA*4*24 - Update HDR trigger code**

The logic used to determine when messages should be sent to the HDR is updated in this patch.  If the patient is a test patient or if a patient merge is occurring at the site, the allergy data will no longer be sent to the HDR.

**GMRA*4.0*23** - **HDR/DS Changes**

This patch introduced the changes necessary to standardize the data stored in the allergy package. Standardized data is necessary for inclusion in HDR.

In addition, this patch introduces two new cross-references and a new Application Programmer Interface (API) that will allow changes to existing reactant terms to propagate through existing allergy entries in the PATIENT ALLERGIES file (120.8).

The GMR ALLERGIES file (120.82) and the SIGNS/SYMPTOMS file (120.83) are being standardized.  As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files. In addition, users will no longer be able to add "free text" signs /symptoms.

The data standardization team has reviewed existing local entries at the sites and has added those terms to files 120.82 and 120.83 as appropriate. Requests for new terms will be made via the New Term Rapid Turnaround (NTRT) process. If approved, the new term will be sent to all sites for inclusion in file 120.82 or 120.83. For more information on this process, see these websites:

- Standards and Terminology Project Website: REDACTED
- NTRT Program website. REDACTED

In addition to the updates to files 120.82 and 120.83, existing active entries in file 120.8 need to be updated to use standard reactants.  In a previous allergy patch, a utility was distributed that identified free text entries.  The utility also included options that allowed the user to fix these entries by either updating them or marking them as entered in error.

GMRA*4.0*21

Free-text allergies may no longer be entered through CPRS. At sites that have installed OR*3.0*195, OR*3.0*216, and GMRA*4.0*21, CPRS users can no longer enter allergies and adverse reactions as orders that are placed in the *ORDERS* file, and allergies do not appear on the Orders tab. Patch OR*3.0*216 includes a post-installation routine that changes the status of all active allergy orders to complete and, therefore, removes the allergy orders from the Orders tab.

In addition, users can no longer select OTHER ALLERGY/ADVERSE REACTION as a type of causative agent, nor can they select OTHER REACTION as a type of sign/symptom. Changes to the ART package have eliminated these items as choices. These changes mark a continuing effort to end free-text and unspecific entries.

CPRS GUI 24 introduced a dialog through which users can request that a causative agent be added to their site’s *ALLERGIES* file. Users access this dialog via a warning that pops up when they attempt to enter a free-text causative agent. The warning dialog asks users to indicate— by clicking either its YES or NO button—if they want to send a causative-agent inclusion request. In CPRS GUI 24, the default button was YES. In this version, the default button is NO. Furthermore, when users click the system X button (located in the top right-hand corner of each screen) to exit any of the screens that comprise the inclusion-request dialog, CPRS now cancels the request action.

**No Known Allergies (NKA):** It is now possible to delete an assessment of NKA from within the ART package. When you select a patient for entering/editing allergies and that patient doesn't have any active allergies on file, the “Does this patient have any known allergies or adverse reactions?” prompt is presented to you. If the patient has no assessment, there is no default answer. If the patient has been assessed as NKA, the default is NO. In the case where the default answer is NO (meaning, the patient is NKA), you may enter an @ sign to indicate that the assessment should be deleted and the patient should be returned to the 'not assessed' state. This would be used in those rare cases where an assessment is erroneously assigned to the wrong patient.

**GMRA*4*20 - Allergy Data Updates**

Patch 20 expanded the free-text utility to identify ingredient-based allergies as well as drug class-based allergies. The site can then take the same two actions on those lists as it can on free text.

This utility does NOT automatically match any entry to a “better” entry, nor does it suggest better entries.  It’s simply a tool for identifying allergies that may be problematic and allows you to take action on them.

Another patch, GMRA*4*29, will automatically update existing free-text entries to entries identified as being the best match for the free-text term.  Once patch 29 runs, the sites will still have entries in their free-text list, because the automated cleanup cannot get all of them.

Sites currently have the ability to identify and fix free-text entries. The purpose of the automated cleanup is to do the majority of the work for the sites that haven’t begun working on the cleanup. Those sites will still need to fix the remaining free-text entries, as well as review the ingredient and drug class-based allergies for possible repair.

A new mail group, GMRA REQUEST NEW REACTANT, was added with patch 17.  Sites should populate this mail group with the people responsible for addressing requests to add new reactants. If users attempt to enter a reactant that is not found during the look-up process, they are asked if they would like to send an email requesting the addition of the new reactant. The request can then be reviewed for accuracy and new local entries can be added, if appropriate. Previously, users were asked if they wanted to add the new entry and it was immediately available in the patient’s record. Under the new system, the mail message that’s sent to the user now indicates in the text the name of the reactant that has not been added to the record.

**Order Checking**

Remedy tickets 67740, and 117610, as well as Patient Safety Issues PSI-03-050 and PSI-05-075, describe situations where order checks did not fire, due to the fact that only ingredient information was stored with the patient allergy. While this patch will not stop a user from selecting from the ingredient file while entering an allergy, it does give the site a tool to identify and fix entries that are associated with an ingredient file entry.

When reactants are selected from either the ingredient or drug class files, only that specific piece of information is stored with the patient’s allergy. Order checking looks at both the ingredients and the drug classes when determining if an order check should be activated. Therefore, reactants should be selected from either the GMR ALLERGY file or one of the pharmacy drug-related files, to increase the likelihood of producing an order check. The order in which the files are searched when looking for reactants was altered in patch GMRA*4*23 so that the ingredient and drug class files are at the bottom. This change helps promote selection from files that include both ingredients and drug classes as part of the definition of the reactant. The ingredient and drug class files are still available to choose from, as there are times when selection from one of these files is the best choice.

**Progress Note Updates**

The progress note that is sent when an allergy has been marked as entered in error has been updated to clarify that the reactant may have been entered in error or may have been found to no longer be an allergy or adverse reaction for the patient. Previously, when a patient’s allergy was marked entered in error (in the roll-and-scroll environment), if the patient didn’t have a location associated with them, you were asked for a location. If you didn't answer that question, a progress note wasn’t filed. With the update, the location question isn’t asked.

The progress note will include a statement similar to the following:

**The adverse reaction to X was removed on --/--/--. This reaction was either an erroneous entry or was found to no longer be a true adverse reaction.**

The message notes whether the entry being marked entered in error is an adverse reaction or an allergy, so the text will change depending on how the entry was entered.

**Top Ten Sign/Symptom List Update**

This patch also includes a post-installation routine that will review the site's “top 10” sign/symptom list to make sure it only has 10 entries. In a previously released patch, additional sign/symptoms may have been added at positions 11 or higher. The site is unable to delete or edit these entries and the user never sees these entries as possible choices when adding signs/symptoms. However, when NTRT updates are sent out, it is possible to get an email message telling you that an entry on the top 10 list is now inactive and that you must update the entry. As stated above, you have no way to do that and entries above number 10 shouldn't be part of the definition. This post-install will remove any entries numbered 11 or higher.

**Invalid Pointers Check**

The post-install also identifies any allergies with an invalid pointer in the GMR ALLERGY field of file 120.8.  If invalid data is found the entry is converted to a “free text” entry and an email message with information related to that allergy is sent to the installer after the post-install finishes. The allergy clean-up utility can then be used to fix the entry.

The line “no active orders” was also added in the order checking segment of the utility, so you’ll be aware that the check was made and the patient had no active orders.

##### CPRS Changes affecting ART

**Patch OR*3*233**

**Support for Allergy Synonyms** – Allergy synonyms, if present, are now included in the SIGNS/SYMPTOMS selection box. This is included in patch OR*3*233, which will be distributed with GMRA patch 23.

**CPRS GUI 26**

**Marking Allergies as Entered in Error Now Controlled by Parameter** - In CPRS v25, any user could enter new allergies, mark a patient as NKA (no known allergies), and mark allergies entered in error from the cover sheet and the detailed display window.  In v.26, the Entered in Error option requires the new parameter OR ALLERGY ENTERED IN ERROR to be enabled for the user. The other options remain open to all users as before.

**Free-Text Signs and Symptoms No Longer Allowed** – To support of data standardization efforts, developers removed the ability to enter free-text signs/symptoms. Users must now select items from the list of available signs/symptoms.

**Inconsistent Sending of Bulletin for Marked on Chart** – CPRS always sent the “Marked on Chart” bulletin if the user entered an allergy from the Orders tab. CPRS never sent the bulletin if the user entered the allergy from the Cover Sheet. This inconsistency has been corrected, and CPRS will never send the bulletin when the user enters a new allergy.

The "Bulletin has been sent" message that CPRS displays after the user requests the addition of a new causative agent now includes the same warning included in the bulletin about that reactant not being added to the patient's record.

Use of ART within CPRS is primarily described in CPRS documentation, but some examples are provided in this manual.

**Test plan for allergy enhancements in CPRS GUI v26**

1. In CPRS v25, any user was allowed to enter new allergies, mark a patient as NKA, and mark allergies entered in error from the coversheet and the detailed display window.  In version 26, the entered in error option will require the new parameter OR ALLERGY ENTERED IN ERROR to be enabled for the user.   GUI Mark Allergy Entered in Error has been added to the GUI PARAMETERS menu that is on the CPRS Configuration (Clin Coord) menu. The other options remain open to all users as before.

To test, right-click in the allergies box. If the Entered in Error parameter has been enabled, the option mentioned above should be selectable, if appropriate. If the Entered in Error parameter is not enabled, the option should be grayed-out.

In addition, you should click on an existing allergy in the allergies box, which will open the detailed display. If the Entered in Error parameter has been enabled, you should see the selectable box marking the existing entry as entered in error. Without the parameter being enabled, the box should be grayed-out and unavailable for selection.

1. The “Bulletin has been sent” message displayed to the user after requesting addition of a new causative agent now also includes the same warning included in the bulletin about that reactant not being added to the patient’s record.

### ART Data Standardization FAQ

Can sites continue to enter local allergies after standardization is complete?

No. The files have been locked down and local additions for allergies are not permitted. The ability to enter free-text additions to the GMR Allergies file 120.82 was taken away from sites two years ago. Removing the ability to enter free-text additions to the Sign/Symptoms file 120.83 was included in the standardization process. Sites can request additions to the GMR Allergies file 120.82 and to the Sign/Symptoms file 120.83 through the New Term Rapid Turnaround (NTRT) process. Please see the NTRT process section of this document for more information.

What will happen if different sites have different attributes, such as drug ingredients, designated to the same inactive term for entries in GMR Allergies file 120.82? Will the attributes stay the same after standardization at each site?

The attributes will stay the same, including drug classes and drug ingredients, for inactive terms after standardization is complete.

What happens to local allergies in GMR Allergy file 120.82 that are currently on file when standardization occurs?

If a local allergy on file is in the standard, then the term will remain active, but all of the term attributes (e.g. synonyms, drug classes and drug ingredients) will be overwritten by the standardized file.  This standardized term will be available for recording new allergies in the future.

If a local allergy on file is *not* in the standard, then the term will become inactive, and all term attributes (e.g. synonyms, drug classes and drug ingredients) will remain the same, and the data, if applicable, will be available for order checks. However, this term will not be available for selection when recording new allergies.

Is there a Sign/Symptom term called “other” in the new standard for file 120.83 Sign/Symptoms?

No. “Other” does not exist in the list of standardized terms for Sign/Symptoms file 120.83. If there is a term that is not available in the Sign/Symptoms list and it needs to be added, please enter an NTRT request. See the NTRT process section of this document for more information.

What does the allergy “contrast media” look like in the new standard for GMR Allergies file 120.82?  Will the new standard also contain the many drug classes associated with this allergy?

The contrast media allergy is in the standard GMR Allergies file 120.82.  In the standard, this allergy also includes the many drug classes that are associated with this entry. We encourage sites to review and ensure that the standard is comprehensive. Compare the drug ingredients and drug classes that have been recorded in your site’s file with what is in the standard.

If differences exist between what is in the standard and what is in your file, your site data will be overwritten. Submit an NTRT request if you believe that drug classes, drug ingredients, or synonyms should be included in the standards that are not included.  Please see the NTRT process section of this document for more information.

Should a local allergy of “Bufferin” be changed to Aspirin in the GMR Allergies file 120.82?

No. Sites are not being asked to change local allergies in the GMR Allergies file 120.82.

Will non-standard (inactivated) terms continue to be used for order checking? How?

Yes. Although inactivated terms are not available for new documentation, those that have been stored in patients’ records will continue to be used for order checking.  The internal entry numbers (IENs) of the inactivated terms have been preserved, and it is the IENs that are needed for order checking.

What is the workaround for a site, if the item that the patient is allergic to is not found in the standard GMR Allergies file 120.82 and the terms needs to be entered as an NTRT request?  How does the end user document that a patient is allergic to an item that is not in the standard?

The ability to enter free-text allergies in GMR Allergies file 120.82 was taken away from sites two years ago. Please continue to use your site-developed processes to handle this documentation.

Currently, there is a message or pop-up box telling an end user in CPRS that the allergy term they are searching for was not found, but that they can request that it be added (shown below).  However, this message box is not available if a Sign/Symptom is not available.  What is the desired work-around for a site to request that a Sign/Symptom term be added, since they will not have the instructions from this pop-up box?

<!-- image -->

Sites may wish to handle these additions in the same manner as when requesting a new reactant, or they may wish to handle it differently. We recommend that sites communicate to the end users their desired work-around for handling these requests for additions of Sign/Symptoms.

End users are encouraged to update the patient record with the Sign/Symptom term when it becomes available in the standard.  End users can enter free text Sign/Symptoms until CPRS GUI v26 is installed. However, these additions of free text Sign/Symptoms prior to CPRS GUI v26 release are highly discouraged.

What are sites being asked to do regarding the Top 10 List for Sign/Symptoms?

After standardization, the Top 10 List for Sign/Symptoms file #120.83 may have inactive terms. The GMRA REQUEST NEW REACTANT mail group will be notified of inactive Top 10 terms at your site after the VETS push has occurred. Sites are being asked to replace inactivated terms with standard terms as soon as possible, to prevent end users from viewing empty space in the GUI. If the inactivated terms are not replaced by active terms in the standard, the end user will need to click on the scrollbar for the Sign/Symptoms. This will cause the empty space to be auto-adjusted and the gap will no longer display in the GUI. CPRS GUI v26 will fix this so that there is no blank space.

It is possible to receive an email indicating that there are terms on the top ten list that need to be updated, but those terms do not appear when using the option to edit the terms. Some sites actually have more than 10 terms stored in the top 10 list but only the first 10 show to the user. If one of the additional terms is now inactivated, it will be included in the update message although you won’t actually see it in the list.

If the e-mail update message contains terms that do not appear to be on your Top 10 list, you may ignore those terms. This problem will be fixed in a future patch.

To change inactive entries:

1. Use the Menu Option GMRA SITE FILE. The parameter is HOSPITAL.
2. Enter the number of the Sign/Symptoms that you need to change.

Why are sites getting e-mail messages about order checks to the GMRA mail group as the patch is being loaded and post routines are being run from this GMRA*4*23 patch?

Receipt of these messages is a result of the updates that are occurring to the Patient Allergy file 120.8 when GMR Allergies file 120.82 is standardized. Any time a file 120.82 entry has a change of drug classes or drug ingredients, and a patient has a previous allergy recorded to this entry, then the new drug classes or drug ingredients will be propagated to the Patient Allergy file 120.8.  The purpose of the message is to inform the Allergy Clinical Application Coordinator of the possibility of a missed order check based on the updated allergy information. Order checks only occur when the order is placed, which means that updated allergy information is not compared against existing orders. During the update, the new allergy information is compared against the patient’s active orders to determine if there are any possible drug-allergy conflicts based on the new information. There is a slight possibility of a false-positive report but each entry should be reviewed for a possible drug-allergy interaction.

What is the name of the mail group that will receive the e-mail notifications regarding order checks, as mentioned in the previous question?

The GMRA Request New Reactant mail group will receive these order check notifications through e-mail.

How can we record that a patient has No Known Allergies (NKA), when this term is not included in the standard for GMR Allergies file 120.82 and will be inactivated for future selection?

Enter no-known-allergies (NKA) assessments for patients who have no active allergies by taking the following steps in the CPRS GUI from the Coversheet:

1.	Right-click within the Allergies/Adverse Reactions pane.

2.	From this menu, select “Mark patient as having No Known Allergies (NKA).” CPRS displays the No Known Allergies dialog. Note : CPRS will allow you to record a patient as having No Known Allergies (NKA) only for patients who have no active allergies. When patients have active allergies, CPRS deactivates this menu selection.

3.	Click OK.

Can we continue to record allergies and No Known Allergies (NKA) from the Write Orders menu in the CPRS GUI?

Yes. You can continue to record new patient allergies or NKA from the Write Orders menu, or on other site-configured menus on the Orders tab in the CPRS GUI.

How do we record that the patient has an “unknown reaction,” since this term is not included in the Sign/Symptoms file 120.83 for selection when recording a patient allergy reaction?

In CPRS GUI v25 you can still enter free-text Sign/Symptoms. This option has been disabled in List Manager. In the GUI, you must press &lt;Enter&gt; after you type the free-text Sign/Symptom. It is also possible to leave the Sign/Symptoms field blank, and make a note in the Comment field that the Sign/Symptom is unknown. Typing free-text Sign/Symptoms will not be possible with CPRS GUI v26. This FAQ will be updated when more information is available.

Will sites need to continue to update the Top 10 list of Sign/Symptoms when each NTRT push occurs?

Yes. If the new NTRT push inactivates entries on the Top 10 list of Sign/Symptoms, then an e-mail message will be sent to the “GMRA Request New Reactant” mail group. The message will list which terms have been inactivated and remind sites to use the menu option GMRA SITE FILE to correct these entries.

Details of what was contained in the NTRT push can be learned from the Automated Notification Report (ANR) message that will be sent, or from the NTRT Web site at REDACTED (under “NTRT Deployment Log”).  The content list for a push will give you an idea about alternative terms that would be appropriate replacements for inactivated terms. If you are not currently receiving the ANR messages, please log a Remedy ticket to be added to the distribution of these messages.

If the e-mail update message contains terms that do not appear to be on your Top 10 list, you may ignore those terms. A problem has been identified where some sites have more than ten entries in their Top 10 list.  This problem will be fixed in a future patch.

What is an example of a Top 10 List term that may need to be replaced due to an NTRT push?

The Enterprise Reference Terminologists are currently going through the standard for file 120.83 Sign/Symptoms and changing the primary terms to more user- or clinician-friendly terms.  For example, in the most current update, some terms such as “Aptyalism,” “Face Goes Red,” and “Cutaneous Eruption” are being made inactive as primary terms, but are being added as synonyms to other primary terms. See question six in the NTRT section of this document for additional information.

In the Top 10 list, you may need to update the Top 10 list to display the updated active terms.

Example:

| INACTIVATE as Primary term  (Added as Synonym)   | ACTIVATE as Primary term   |
|--------------------------------------------------|----------------------------|
| Aptyalism                                        | Dry Mouth                  |
| Face Goes Red                                    |                            |
| Cutaneous Eruption                               | Rash                       |

#### REDACTED

#### VA  Terminology Services (VETS) Push and Deployment Questions

1. How long will it take for a large integrated site to complete the cross-referencing of all the files after the initial VETS push or deployment has occurred, for the Allergy/Outpatient Pharmacy domain?

It is estimated to take three hours. This is approximately the amount of time it took a large integrated test site to complete this process.

What happens to an end user who is entering an allergy on a patient when the VETS push or deployment occurs?

There are not any effects visible to the end user who is entering in allergies while a VETS push or deployment is occurring.

Has this software been tested in production and the impact assessed for the use of Bar Coding Medication Administration (BCMA) and passing medications during the VETS push or deployment?

Yes. The three test sites reported that there were no reports of any adverse impacts to BCMA.  Also, the software quality assurance testing included BCMA testing by the pharmacy team.

When will the VETS pushes or deployments occur?

The VETS pushes or deployments will be scheduled with the sites, most likely on a regular schedule to be determined. The deployments or pushes will be coordinated with the site, the HDR Implementation Manager, and the ERT team. The site will be notified prior to a VETS push.

Do sites need to have staff on site when the VETS push or deployment occurs?

No. Site staff do not need to be present when the VETS deployment or push occurs.

Is the VETS push or deployment equivalent to a patch load?

No, a push is not the same as a patch load. The VETS push or deployment is the final step in the standardization of the files after patches are loaded.  These pushes or deployments will also continue as new terms are requested from the field.  The pushes are HL7 messages that are sent through the interface engine to .

Is the VETS push or deployment a site-initiated process?

No, it is not. However, the site will be contacted prior to the VETS push or deployment.

**8.  Is it true that sites are not to update or change the resource slots associated with the GMRA UPDATE Resource device?**

Yes. The slot is set to one and needs to stay at one. It is very important that sites not change the number of slots for this resource device. If the resource device does not stay at one, then NTRT pushes may be processed inaccurately and may potentially corrupt Allergy files. If sites have changed this, they need to set it back to one. Then sites will need to work with the ERT team for a redeployment of the push. ERT is looking at ways to control the order in which updates are done in the future. However, in the meantime sites need to be aware of this potential issue and to monitor the GMRA UPDATE Resource device to ensure it stays set at one slot.

REDACTED

#### New Term Rapid Turnaround (NTRT) Process Questions

1. How fast will the NTRT request be granted? Are weekends taken into consideration?

At this time, NTRT requests will be deployed nationally every Thursday. The cutoff date for inclusion of a term in the Thursday deployment is COB the Friday before the scheduled deployment. Over the next 7 months, this timeframe may be adjusted. Any changes to the frequency of NTRT deployments will be communicated to sites and support personnel.

If there are a large number of New Term Rapid Turnaround (NTRT) requests at a site, is it necessary to enter each request separately?

If sites have a large number of NTRT requests that need to be submitted, your HDR Implementation Manager can help you get these entries to the ERT team without having to enter all of the requests into the NTRT website.

If there is a local term that is a synonym of a national standard term, then is an NTRT request needed for that local term?

No.  The local term will not need to be added to the standard.  If there is a compelling case for why it should be added, then that can be forwarded on as an NTRT request.

Consider the following example:

| Local Term     | New Standard Term                  | Add to standard?                                         |
|----------------|------------------------------------|----------------------------------------------------------|
| Garbanzo beans | Chickpeas  Synonym: Garbanzo beans | No.  Synonyms are available for searching terms in CPRS. |

If a new drug ingredient is needed, do we go through the NTRT process or will these still be handled through National Drug File (NDF) updates?

New drug ingredients will need to be added through the NDF process.

How has the issue related to Sulfa allergy documentation and order checking in  been resolved?

A generic Sulfa entry in the GMR Allergy file (120.82) has been deployed nationally.  Standardization identified the need for consistent screening for Sulfa-containing drugs.  The Data Standardization and Enterprise Reference Terminology teams have worked with the National Drug File manager to determine which drugs need to be linked to the new generic sulfa entry in the GMR Allergy file 120.82.  Order check screening for Sulfa allergies works consistently and completely on all  systems.

Concerns have been raised about user-friendly terms and equivalents in the Sign/Symptoms file 120.83 from some sites. What is being done to resolve these concerns?

A review of the Sign/Symptoms file 120.83 has been completed. This file was reviewed by a group comprised of clinicians from the field as well as terminologists and other key stakeholders.

Concerns have been raised from sites regarding clinical terms that are not user friendly.  For example “cutaneous eruption” is the primary term in the standard and “Rash” is a synonym.  Primary terms are stored in the patient record and on the patient arm band.  Clinicians would like to see Rash become the primary term and cutaneous eruption the synonym.  A complete review of the standard was conducted to identify other terms that may also benefit from a similar change.

Concerns have been raised that some terms in the standard are not equivalent and should not remain as synonyms to the primary term.  For example, “Congestion of the Throat” is not the same as “Swelling of the Throat” and should be fixed in the standard.  Other non-equivalent synonyms were identified and are associated with two separate terms when applicable.

How are sites being notified that NTRT additions are being made to the standardized files for Allergies?

An Automated Notification Report (ANR) is sent out through the National Help Desk by e-mail messages that alert sites about the changes that are being made to the Sign/Symptom file 120.83 and the GMR Allergies file 120.82.  If you are not currently receiving these ANR messages and would like to in the future, please submit a Remedy ticket and you can be added to the distribution list for future information.

The information about the changes being made by NTRT can also be viewed on the NTRT Web site, under “NTRT Deployment Log.”  Those interested can also join the NTRT listserv which provides the same information as the ANR messages, along with the potential for supplementary information. Join by going to REDACTED and clicking the link in the middle of the screen called "NTRT Notification Listserv."

Why didn’t I receive an order check mail message when NTRT updates were made to the GMR Allergies file 120.82 for an entry that contained drug class and drug ingredient information?

The order check mail messages only fire for patients who meet the following conditions:

- Not deceased
- Not test patients
- File 120.82 entry not marked Entered in Error
- Matching allergy entry selected from File 120.82 is not a free text entry
- The patient has an active order that does not have an order check already logged against it that should have one based on the updated allergy information.

#### REDACTED

#### Site Clean-up Questions

1. After allergy standardization, what is the impact to a site that has many free-text patient allergies that need to be cleaned up?

Sites will be able to continue cleaning up the free-text patient allergy entries after Allergy/Outpatient Pharmacy standardization is complete. The patches will not affect this clean-up effort. After standardization, there will be a more comprehensive list of allergies for your site to use for cleaning up free-text patient allergy entries.

New terms should not be added to GMR Allergies file 120.82 prior to standardization in order to map a free text patient allergy. The GMRA*4*23 patch locked down this file so sites can no longer add terms through the roll-and-scroll interface. Sites should clean up the patient allergy file 120.8 prior to standardization with what is currently available.  Once standardization is complete, more terms will be available in the GMR Allergies file 120.82 to correct the remaining free text patient allergies.

An automated clean-up patch is being written to help sites in the free-text patient allergy clean-up effort. This patch will be released sometime after the standardization patches.  The content required for this patch is currently being reviewed. Sites have been asked to clean up free-text entries that have a low number of occurrences. Free-text patient allergies that occur one or two times in the clean-up utility should be cleaned up first.  Also, free-text patient allergies that have multiple allergies on one line (e.g. “Aspirin, Penicillin, chocolate”) should be cleaned up by recording each allergy separately for that patient.

The automated clean-up patch will help sites clean up free-text patient allergy entries, but not all data can be cleaned up in an automated fashion.  Patient allergy data that has clinical relevance will be left as free text and will need to be cleaned up by the site.

What is the impact of Outpatient Pharmacy standardization to sites if they have not finished linking local drugs to the National Drug File (NDF)?

Sites can continue to clean-up the local drug file or file 50 mapping to the National Drug File (NDF) after standardization.  The data in the local drug file needs to be mapped so that order checks work optimally.

#### Health Data Repository (HDR) Questions

1. What happens in the Health Data Repository (HDR) when one site has entered an allergy for Penicillin and another site has entered Penicillin as “entered in error”?

Allergies that are entered in error at one site will not overwrite the allergies recorded at another site. The HDR will err on the side of safety. The HDR will store both pieces of information: the patient allergy record and the “entered in error” record.

In regard to the question above, will one site be notified that another site has entered an allergy in error?

At this time, there is not a mechanism to do this. Site-to-site notification will not be done until a national process is put in place that determines when a site’s allergy record can be overruled.  The clinician should get the information via Remote Data Views (RDV) and work with the patient to make sure the record is correct.

Where do we go for technical information about turning on the VDEF triggers? Is that something HDR Implementation Managers will help with?

Yes. The HDR Implementation Mangers will be in contact with sites when it is time to turn on the VDEF triggers. They will communicate the necessary technical steps at that time.

In the CPRS GUI, the end user now sees that a light is blue on the HDR section of Remote Data Views (RDVs).  Why is this there?

HDR data can now be seen in RDV.  Vitals data has been standardized and it is being sent to the HDR.  This blue text means that the patient has vital sign data stored in the HDR.  With the release of CPRS GUI v. 26, end users will be able to view data from the HDR.

This may be confusing to some end users, because some patients will only have vital sign data available at the local site and the light will not be blue. VistaWeb is also impacted, but the new version of VistaWeb that should be available at the end of August will be able to retrieve the HDR data.

REDACTED

REDACTED