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
source_file: gmra_4_20_rn.docx
status: draft
title: gmra 4 20 rn.docx
---

<!-- image -->

**Adverse Reaction Tracking**

**(ART)**

Allergy Clean-up Utility

**GMRA*4*20**

Release Notes

August 2006

Health Systems Design and Development


Table of Contents

Allergy Clean-up Utility	1

Top Ten Sign/Symptom List Update	2

PSI/Remedy Tickets related to GMRA*4*20	3

How to Use the Allergy Clean-up Utility	4

Detailed Display	5

Mark Entered in Error	8

Update to New Reactant	9

Add/Edit Allergy File	12


### Allergy Clean-up Utility


**GMRA*4*17 - Allergy Free Text Utility**

Patch GMRA*4.0*17 provided a utility to help sites identify and fix allergy entries that have free-text reactants. With this patch, free-text entries were no longer allowed from within the Allergy Tracking package. A subsequent patch to CPRS (OR*3.0*215) prevented free-text entries from within CPRS as well.

The free-text utility that went out in patch 17 finds all free text allergies and groups them together so the site can take one of two actions on them: The site can either update them to a different allergy or they can mark the entries entered in error.

**GMRA*4*20 - Allergy data updates**

Patch 20 expands the utility to identify ingredient-based allergies as well as drug class-based allergies. The site can then take the same two actions on those lists as it can on free text.

This utility does NOT automatically match any entry to a “better” entry, nor does it suggest better entries.  It’s simply a tool for identifying allergies that may be problematic and allows you to take action on them.

Another patch, GMRA*4*29, will automatically update existing free-text entries to entries identified as being the best match for the free-text term.  Once patch 29 runs, the sites will still have entries in their free-text list, because the automated cleanup cannot get all of them.

It won’t matter if patch 29 or 20 is installed first. Sites currently have the ability to identify and fix free-text entries. The purpose of the automated cleanup is to do the majority of the work for the sites that haven’t begun working on the cleanup. Those sites will still need to fix the remaining free-text entries, as well as review the ingredient and drug class-based allergies for possible repair.

A new mail group, GMRA REQUEST NEW REACTANT, was added with patch 17.  Sites should populate this mail group with the people responsible for addressing requests to add new reactants. If users attempt to enter a reactant that is not found during the look-up process, they are asked if they would like to send an email requesting the addition of the new reactant. The request can then be reviewed for accuracy and new local entries can be added, if appropriate. Previously, users were asked if they wanted to add the new entry and it was immediately available in the patient’s record. Under the new system, the mail message that’s sent to the user now indicates in the text the name of the reactant that has not been added to the record.

**Order Checking**

Remedy tickets 67740, and 117610, as well as Patient Safety Issues PSI-03-050 and PSI-05-075, describe situations where order checks did not fire, due to the fact that only ingredient information was stored with the patient allergy. While this patch will not stop a user from selecting from the ingredient file while entering an allergy, it does give the site a tool to identify and fix entries that are associated with an ingredient file entry.

When reactants are selected from either the ingredient or drug class files, only that specific piece of information is stored with the patient’s allergy. Order checking looks at both the ingredients and the drug classes when determining if an order check should be activated. Therefore, reactants should be selected from either the GMR ALLERGY file or one of the pharmacy drug-related files, to increase the likelihood of producing an order check. The order in which the files are searched when looking for reactants was altered in patch GMRA*4*23 so that the ingredient and drug class files are at the bottom. This change helps promote selection from files that include both ingredients and drug classes as part of the definition of the reactant. The ingredient and drug class files are still available to choose from, as there are times when selection from one of these files is the best choice.

**Progress Note Updates**

The progress note that is sent when an allergy has been marked as entered in error has been updated to clarify that the reactant may have been entered in error or may have been found to no longer be an allergy or adverse reaction for the patient. Previously, when a patient’s allergy was marked entered in error (in the roll-and-scroll environment), if the patient didn’t have a location associated with them, you were asked for a location. If you didn't answer that question, a progress note wasn’t filed. With the update, the location question isn’t asked.

#### The progress note will include a statement similar to the following:

#### The adverse reaction to X was removed on --/--/--. This reaction was either an erroneous entry or was found to no longer be a true adverse reaction.

The message notes whether the entry being marked entered in error is an adverse reaction or an allergy, so the text will change depending on how the entry was entered.

#### Top Ten Sign/Symptom List Update

This patch also includes a post-installation routine that will review the site's “top 10” sign/symptom list to make sure it only has 10 entries. In a previously released patch, additional sign/symptoms may have been added at positions 11 or higher. The site is unable to delete or edit these entries and the user never sees these entries as possible choices when adding signs/symptoms. However, when NTRT updates are sent out, it is possible to get an email message telling you that an entry on the top 10 list is now inactive and that you must update the entry. As stated above, you have no way to do that and entries above number 10 shouldn't be part of the definition. This post-install will remove any entries numbered 11 or higher.

**Invalid Pointers Check**

The post-install also identifies any allergies with an invalid pointer in the GMR ALLERGY field of file 120.8.  If invalid data is found the entry is converted to a “free text” entry and an email message with information related to that allergy is sent to the installer after the post-install finishes. The allergy clean-up utility can then be used to fix the entry.

The line “no active orders” was also added in the order checking segment of the utility, so you’ll be aware that the check was made and the patient had no active orders.

#### PSI/Remedy Tickets related to GMRA*4*20

PSI-03-050

PSI-05-075

Remedy #67740

Remedy #117610

### How to Use the Allergy Clean-up Utility

When you start the utility, a list of currently existing free-text entries is displayed in alphabetical order. This list may take a few minutes to generate, as all existing entries need to be evaluated to determine which ones are “free text.” The list shows the name of the reactant and the number of entries for that reactant. In most cases, they will be unique, but there will be some that have many entries (such as an entry for NO KNOWN ALLERGIES).

When entering the utility, any users who are currently working in the utility will be listed. If users are listed as working with the utility, you will not be allowed to update the list. You can only update the list when nobody else is working in the utility.

Once the list is displayed, you can do two things:

1. Mark the entry as entered in error
2. Update the record so that it points to a reactant selected from GMR Allergy file or             one of the National Drug Files.

Select OPTION NAME: **GMRA SITE FILE MENU** Enter/Edit Site Configurable Files     menu

1      Edit Allergy File

**NOTE:** When you start the utility, you may see 3 different things: 1) If the list has never been built, you’ll see the message below (building list…), 2) If the list has been previously built and nobody is using the utility, you’ll see a message indicating the last time the list was built and you will be asked if you’d like to rebuild the list, 3) If the list is currently being built, you’ll get a message indicating that you must wait. Most times a user will see the message in number 2.

<!-- image -->

3      Enter/Edit Site Parameters

4      Sign/Symptoms List

5      Allergies File List

6      Allergy clean up utility

Select Enter/Edit Site Configurable Files Option: 6

Allergy clean up utility

Select one of the following:

1         Free Text

2         Ingredient

3         Drug Class

Select the list you wish to work with: 1  Free Text

The free text list was last built on

Do you want to rebuild the list? NO//

**Allergy Tracking Update       Mar 28, 2006@11:00          Page:    1 of    1**

**Allergy Tracking Free Text Entries**

**Reactant                                 # Active Entries**

**1   ANTIGEN IN SERUM (FREE TEXT)                   1**

**2   CATHETER, RED RUBBER (FREE TEXT)               1**

**3   Diabetes Mellitus Type II (FREE TEXT)          1**

**4   NO KNOWN ALLERGIES (FREE TEXT)                 1**

**5   PENICILLIN                                     6**

**6   ZANAMIVIR                                      1**

**Select one or more entries**

**AE  Add/Edit Allergy File EE  Mark entered in error**

**DD  Detailed Display        Update to new reactant**

**Select Item(s): Quit//** ??

Use AE to add local allergies to the GMR ALLERGY file.  This should only be done if you're sure no existing reactant matches your needs.

Use EE to mark all entries within the selected group as entered in error.  You may select multiple groups if you like.

Use DD to get a detailed display.  It's highly recommended that you use the detailed display menu to make all changes.

Use  to update the reactant.  Extreme caution should be used when doing mass updates.  It would be better to do the updates from within the detailed display menu.

Press enter to continue:

#### Detailed Display

The detailed display window shows the patient name and the list of currently active allergies, separated by a tilde (~).  This way, you can quickly look and see if the patient already has an active allergy that is the same as the free-text entry.  In this case, you would mark it as entered in error.

The “free text detailed display” action lets you see a Fileman inquiry-style listing of the free text entry for selected patient(s). You'll now be able to see the comments, reactions, and other associated information for the free text entry that you're fixing.

When doing a group update or selecting multiple patients for updating from the detailed display listing, the reactant you select for the first patient in the list will become the default for the remaining patients. The exception to that would be if you decide to not accept the default while updating one of the patients. In that case, the last chosen reactant will become the default for the next patient. The default only holds while working with a particular group. Once you select a new reactant group or a new group of patients, you must re-select the reactant. This should cut down on the amount of time needed in selecting the reactant for each patient.

**1.** Select the Allergy clean up utility, [GMRA FREE TEXT UTILITY], from the GMRA SITE FILE MENU.

**2.** Select the list you wish to work with – one of the following:

1         Free Text

2         Ingredient

3         Drug Class

If you’ve built this list before, you’ll be asked if you want to rebuild the list.

**3.** Select the number of a reactant first, and then select DD to see details about the reactant. (Alternatively, you can select the action, DD, and then select the number of the reactant.)

NOTE: For detailed display, you can only select one group at a time.

GMRA SITE FILE MENU     Enter/Edit Site Configurable Files menu

1      Edit Allergy File

2      Enter/Edit Signs/Symptoms Data

3      Enter/Edit Site Parameters

4      Sign/Symptoms List

5      Allergies File List

6      Allergy clean up utility

Select Enter/Edit Site Configurable Files Option: 6

Allergy clean up utility

Select one of the following:

1         Free Text

2         Ingredient

3         Drug Class

Select the list you wish to work with: 1  Free Text

The free text list was last built on

Do you want to rebuild the list? NO//

**Allergy Tracking Update       Mar 28, 2006@11:00          Page:    1 of    1**

**Allergy Tracking Free Text Entries**

**Reactant                                 # Active Entries**

**1   ANTIGEN IN SERUM (FREE TEXT)                   1**

**2   CATHETER, RED RUBBER (FREE TEXT)               1**

**3   Diabetes Mellitus Type II (FREE TEXT)          1**

**4   NO KNOWN ALLERGIES (FREE TEXT)                 1**

**5   PENICILLIN                                     6**

**6   ZANAMIVIR                                      1**

**+         Select one or more entries**

**AE  Add/Edit Allergy File EE  Mark entered in error**

**DD  Detailed Display        Update to new reactant**

Select Item(s): Next Screen// 3

Allergy Tracking Update       Mar 28, 2006@11:00          Page:    1 of    1

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

**Reactant Detailed Display     Mar 28, 2006@11:08:04          Page:    1 of    1**

**Patient listing for reactant DIABETES MELLITUS TYPE II (FREE TEXT)**

**Patient Name                   Last 4**

**1   CPRSPATIENT,TWELVE              6572**

**Allergies: AMOXICILLIN~ASPIRIN~MILK~ERYTHROMYCIN~CHROMA-PAK INJECTION~**

**Diabetes Mellitus Type II (FREE TEXT)~PENICILLINS~NUTS~DUST~**

**AMPICILLIN~CHOCOLATE**

**Select a patient**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Allergy Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit// **DD** Allergy Detailed Display

Select Entries from list: **1**

PATIENT: CPRSPATIENT,TWELVE

REACTANT: Diabetes Mellitus Type II (FREE TEXT)

GMR ALLERGY: OTHER ALLERGY/ADVERSE REACTION

ORIGINATION DATE/TIME: JAN 14, 1998@15:46

ORIGINATOR: CPRSPROVIDER,SIX          OBSERVED/HISTORICAL: HISTORICAL

ORIGINATOR SIGN OFF: YES              MECHANISM: UNKNOWN

VERIFIED: NO                          ALLERGY TYPE: FOOD

REACTION: HYPOTENSION                   ENTERED BY: CPRSPROVIDER,SIX

DATE/TIME COMMENT ENTERED: JAN 14, 1998@15:46

USER ENTERING: CPRSPROVIDER,SIX       COMMENT TYPE: OBSERVED

COMMENTS:   Acute

Press return to continue or '^' to stop: **&lt;Enter&gt;**

#### Mark Entered in Error

You can mark an entire group as entered in error from this opening screen. Upon marking the reaction as entered in error, a check is made to see if there are still active reactions for the patient. If there are not any, then you are prompted to enter an updated assessment for the patient.

NOTE: No progress notes are generated when you mark allergies as entered in error using this utility.

**1.** Select the Allergy clean-up utility, [GMRA FREE TEXT UTILITY], from the GMRA SITE FILE MENU.

**2.** Select the list you wish to work with – one of the following:

1         Free Text

2         Ingredient

3         Drug Class

If you’ve built this list before, you’ll be asked if you want to rebuild the list.

**3.** Select the number of the reactant(s) you wish to mark as entered in error. (Alternatively, you can select the action, Mark Entered in Error, and then select the number of the reactant(s).)

Select Enter/Edit Site Configurable Files Option: 6  Allergy clean up utility

Select one of the following:

1         Free Text

2         Ingredient

3         Drug Class

Select the list you wish to work with: 1  Free Text

The free text list was last built on

Do you want to rebuild the list? NO//

Allergy Tracking Update       Mar 28, 2006@11:13:44          Page:    1 of    1

Allergy Tracking Free Text Entries

Reactant                                 # Active Entries

1   ANTIGEN IN SERUM (FREE TEXT)                   1

2   CATHETER, RED RUBBER (FREE TEXT)               1

3   Diabetes Mellitus Type II (FREE TEXT)          1

4   NO KNOWN ALLERGIES (FREE TEXT)                 1

5   PENICILLIN                                     6

6   ZANAMIVIR                                      1

**Select one or more entries**

AE  Add/Edit Allergy File EE  Mark entered in error

DD  Detailed Display      UR  Update to new reactant

Select Item(s): Quit// **5**

**4.** Type EE for Mark entered in error, and then answer Yes to confirm that you want to mark ALL allergies as entered in error.

Select Item(s): Next Screen// **EE** Mark entered in error

You are about to mark ALL allergies with the selected reactant

as entered in error.

ARE YOU SURE? NO// **Yes**

#### Update to New Reactant

You may select and update groups of entries from the opening menu; however, it is recommended that you use the detailed display option to review entries in a group before doing a mass update. ***Changes cannot be undone*** ! When the entry is updated, a comment is stored in the PATIENT ALLERGY file indicating who made the change, date/time of change, and a comment that indicates what the previous value was and what the new value is. In addition, the new reactant is compared against current orders and order checking information is returned, if appropriate. When a new reactant is selected, checks are made for duplicate entries and previously entered-in-error information.

NOTE: Due to the way the order checking software works, you may get “false positives.”  In other words, if the patient currently has an allergy order check for some other order not related to this new reactant, you may still see the order check.

Finally, the drug ingredient/drug class information is updated, if appropriate.

**1.** Select the Allergy clean up utility, [GMRA FREE TEXT UTILITY], from the GMRA SITE FILE MENU.

**2.** Select the list you wish to work with – one of the following:

1         Free Text

2         Ingredient

3         Drug Class

If you’ve built this list before, you’ll be asked if you want to rebuild the list.

**3.** Select a reactant number and then select the action DD.

Select Enter/Edit Site Configurable Files Option: **6** Allergy clean up utility

Select one of the following:

1         Free Text

2         Ingredient

3         Drug Class

Select the list you wish to work with: 1  Free Text

The free text list was last built on

Do you want to rebuild the list? NO//

**4.** Select an item # in the Detailed Display, then select  for Update to New Reactant.

**Allergy Tracking Update       May 31, 2006@12:07:58          Page:    1 of    1**

**Allergy Tracking Free Text Entries**

**Reactant                                 # Active Entries**

**1   ANTIGEN IN SERUM (FREE TEXT)                   1**

**2   ASPIRIN 325MG                                  1**

**3   CATHETER, RED RUBBER (FREE TEXT)               1**

**4   Diabetes Mellitus Type II (FREE TEXT)          1**

**5   NO KNOWN ALLERGIES (FREE TEXT)                 1**

**6   PENICILLIN                                     6**

**7   ZANAMIVIR                                      1**

**8   ZANTAC (FREE TEXT)                             1**

**Select one or more entries**

**AE  Add/Edit Allergy File EE  Mark entered in error**

**DD  Detailed Display        Update to new reactant**

**Select Item(s): Quit// 6**

**Allergy Tracking Update       May 31, 2006@12:08:06          Page:    1 of    1**

**Allergy Tracking Free Text Entries**

**Reactant                                 # Active Entries**

**1   ANTIGEN IN SERUM (FREE TEXT)                   1**

**2   ASPIRIN 325MG                                  1**

**3   CATHETER, RED RUBBER (FREE TEXT)               1**

**4   Diabetes Mellitus Type II (FREE TEXT)          1**

**5   NO KNOWN ALLERGIES (FREE TEXT)                 1**

**6   PENICILLIN                                     6**

**7   ZANAMIVIR                                      1**

**8   ZANTAC (FREE TEXT)                             1**

**Select one or more entries**

**AE  Add/Edit Allergy File EE  Mark entered in error**

**DD  Detailed Display        Update to new reactant**

**Select Item(s): Quit// DD   Detailed Display**

**Reactant Detailed Display     May 31, 2006@12:08:11          Page:    1 of    1**

**Patient listing for reactant PENICILLIN**

**Patient Name                   Last 4**

**1   GMRAPATIENT,ONE                0299**

**Allergies: PENICILLIN~ASPIRIN~ASPRI~PHENOBARBITAL/PHENYTOIN**

**2   GMRAPATIENT,SIX               4444**

**Allergies: PENICILLIN~MILK~DUST**

**3   GMRAPATIENT,FIVE               5545**

Allergies: ASPIRIN TABLETS E.C.~ASPIRIN~CHOCOLATE~PENICILLIN~IODINE~ZANTAC~

**MORPHINE~WATER BOTTLE~CHICKEN~LATEX GLOVE**

**Select a patient                                                  &gt;&gt;&gt;**

**EE  Entered in Error                    PR  Add/Edit Patient Reaction**

**Update to new reactant              DD  Allergy Detailed Display**

**AE  Add/Edit Allergy File**

**Select Item(s): Quit//    Update to new reactant**

**Select Entries from list: 2**

**You are about to update the selected patient's**

**PENICILLIN allergy to a new reactant.**

**ARE YOU SURE? NO// YES**

**For patient GMRAPATIENT,SIX**

Enter Causative Agent: **penicillin**

Checking GMR ALLERGIES (#120.82) file for matches...

Now checking the National Drug File - Generic Names (#50.6)

1   PENICILLIN

2   PENICILLIN/PROBENECID

CHOOSE 1-2: **2** PENICILLIN/PROBENECID

You selected PENICILLIN/PROBENECID

Is this correct? Y// ES

Performing order checking...

Patient has a(n) PENDING order for OPIOID ANALGESICS, order #10003616

Press enter to continue: **&lt;Enter&gt;**

Reactant Detailed Display     May 31, 2006@12:13:16          Page:    1 of    1

Patient listing for reactant PENICILLIN

Patient Name                   Last 4

1   GMRAPATIENT,ONE                0299

Allergies: PENICILLIN~ASPIRIN~ASPRI~PHENOBARBITAL/PHENYTOIN

2   GMRAPATIENT,SIX               4444

Allergies: PENICILLIN~MILK~DUST

3   GMRAPATIENT,FIVE               5545

Allergies: ASPIRIN TABLETS E.C.~ASPIRIN~CHOCOLATE~PENICILLIN~IODINE~ZANTAC~

MORPHINE~WATER BOTTLE~CHICKEN~LATEX GLOVE

**Select a patient                                                  &gt;&gt;&gt;**

EE  Entered in Error                    PR  Add/Edit Patient Reaction

UR  Update to new reactant              DD  Allergy Detailed Display

AE  Add/Edit Allergy File

Select Item(s): Quit//

#### Add/Edit Allergy File

Because of national standardization of the contents of this file, local site addition and modification functions are no longer available. If you wish to request a new term or modify an existing term, please refer to the New Term Rapid Turnaround (NTRT) web site located at http://vista.med.va.gov/ntrt/.  If you have any questions regarding this new term request process, please contact the ERT NTRT Coordinator via e-mail at VHA OI SDD HDS NTRT.