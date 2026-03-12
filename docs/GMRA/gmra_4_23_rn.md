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
source_file: gmra_4_23_rn.docx
status: draft
title: gmra 4 23 rn.docx
---

<!-- image -->

<!-- image -->

**ADVERSE REACTION TRACKING**

**Release Notes**

Version 4.0 GMRA*4.0*23

August 2005

Health Data Systems Veterans Health Administration Department of Veterans Affairs

**Table of Contents**

Introduction	1

Goals for Allergy standardization	1

Software for Allergy Domain Standardization	1

Changes to ART in Patch 23	2

Allergy Domain Potential Issues	3

1. Order Checking	3
2. Clinical Reminders	5
3. Synonyms	5

Additional known changes to Allergies	6

ART Changes in CPRS	8

CPRS GUI 26	9

What can sites do?	10

**Adverse Reaction Tracking Patch 23**

## Introduction

This patch introduces the changes necessary to standardize the data stored in the allergy package. Standardized data is necessary for inclusion in the Health Data Repository (HDR). As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files. In addition, users will no longer be able to add “free text” signs /symptoms.

## Goals for Allergy standardization

- Allergy data will be centrally maintained by Enterprise Terminology Service (ETS).

- Allergy data that is standardized will be:
    - Stored in HDR
    - Interoperable with DoD
        - SNOMED-CT mapping
    - Used in order checking

## Software for Allergy Domain Standardization

The following patches are part of the Allergy Domain standardization. They are listed in order of recommended installation:

1. XU*8*382

2. HDI*1*1

3.  PSN*4*101

4.  PSO*7*205

5. OR*3*233

6.  GMRA*4*23

7.  GMRA*4*24

The following is a brief description of all of the patches. For more detailed information, please refer to the patch descriptions or the associated documentation.

#### XU*8*382 - MFS for Allergies

This patch enhances the Master File Server (MFS) mechanism by extending the error reporting with ERR segments in the application acknowledgement. The patch also distributes Allergies parameters.

#### HDI*1*1

This patch establishes VUIDs for the Allergies and Pharmacy packages.

#### PSN*4*101

This patch adds the VUID data to the following National Drug File files: DRUG INGREDIENTS (#50.416), VA GENERIC (#50.6), VA DRUG CLASS (#50.605), VA PRODUCT (#50.68).

#### PSO*7*205

This patch makes changes to the Outpatient Pharmacy VDEF message. Among those changes is the addition of the VUID from the VA PRODUCT (#50.68) File, for the Drug of the prescription.

#### OR*3*233

Reactants may no longer be selected from file 50 in the GUI interface. Sites may now use synonyms when selecting signs/symptoms.

#### GMRA*4*23

Locks down and prepares files 120.82 and 120.83 for standardization. Software updated so that only active, standardized terms may be used. Removes ability for site to add local reactants to file 120.82 or to add signs/symptoms to file 120.83. Removes file 50 from the list of files to select a reactant from in the roll and scroll interface.

#### GMRA*4*24

Filters out test patients and patients being merged from having their data sent to the HDR.

## Changes to ART in Patch 23

The GMR ALLERGIES file (120.82) and the SIGNS/SYMPTOMS file (120.83) are being standardized. As a result of standardization, sites will no longer be allowed to add or edit entries in either of these files. In addition, users will no longer be able to add "free text" signs /symptoms.

The data standardization team has reviewed existing local entries at the sites and has added those terms to files 120.82 and 120.83 as appropriate. Requests for new terms will be made via the New Term Rapid Turnaround (NTRT) process.  If approved, the new term will be sent to all sites for inclusion in file 120.82 or 120.83. For more information on this process, see

- Data Standardization Project Website: REDACTED
- The NTRT Program website. REDACTED

In addition to the updates to files 120.82 and 120.83, existing active entries in file 120.8 need to be updated to use standard reactants. In a previous allergy patch, a utility was

distributed that identified free text entries. The utility also included options that allowed the user to fix these entries by either updating them or marking them as entered in error.

This patch also introduces two new cross-references and a new Application Programmer Interface (API) that will allow changes to existing reactant terms to propagate through existing allergy entries in the PATIENT ALLERGIES file (120.8).

After standardization patches are installed, VistA files will now contain VUIDs, but not a complete copy of the allergy standard. No changes will be visible in the allergy package until **Enterprise Reference Terminology** (ERT) pushes the rest of the standard data and the implementation is flagged as “complete.” The ERT push will occur after hours (after 6 pm local site time). This may happen the same day or several days after installation of the standardization patches.

## Allergy Domain Potential Issues

Due to the process of data standardization, there will be additions of new terms to the standard files and inactivation of terms that are not supported in the standard. INACTIVE terms are not selectable for future allergies and Order checks continue to work for INACTIVE terms.

### 1 Order Checking

- The volume of order checks will increase due to standardization
- Dietary items such as sea foods and radiology dyes will now contain a drug ingredient of Iodine.

- Standardization includes more terms than most sites currently have.

- Increased order checking supports increased patient safety.

- If a site has altered a nationally released entry by adding drug classes or ingredients or has added a local entry that is now included in the standard, the standardized entry's drug classes and drug ingredients will overwrite any local changes made that are not part of the standard. This may result in decreased order checks, especially if changes were made to accommodate cross-sensitivity.

- For terms that are made INACTIVE by the standard, order checking will continue to work from the recorded drug ingredients and drug classes for the item the allergy was recorded against in File 120.82. However, this term will not be available for future selection.

#### Order Checking Example

- Existing site files have drug ingredients not included in the standardized file:
- Standard includes 2 Drug Ingredients: peanut and peanut oil

- Order checking after standardization will be triggered by ingredients included in standardized files for Active REACTANTS. There will be two drug ingredients that now trigger order checks.

- The ingredients listed at the site before standardization will be replaced with the standardized drug ingredients for this REACTANT.

- Order checks will now be triggered by the standardized drug ingredients.

#### Example of REACTANTS Before Standardization

| **Site**   | **Drug Ingredient**                                | **Drug Class**   |
|------------|----------------------------------------------------|------------------|
| Peanut Oil | Peanut Peanut oil Ipratropium Bromide  Ipratropium | xxxx             |
| Caffeine   | Caffeine                                           | xxxx             |

#### Example of REACTANTS After Standardization

| **Site**   | **Drug Ingredient**   | **Drug Class**   |
|------------|-----------------------|------------------|
| Peanut Oil | Peanut Peanut oil     | xxxx             |
| Caffeine   | Caffeine              | CN809 CN105      |

### 2 Clinical Reminders

- Site has Peanut oil in file 120.82 and has 4 Drug ingredients: Peanuts, Peanut oil, IPRATROPIUM and IPRATROPIUM BROMIDE.

- Sites may need to change existing clinical reminders,
<!-- image -->

- If a clinical reminder was triggered to display based on a recording of an allergy to horse serum, this clinical reminder must be modified now to reflect the change to **horse serum proteins** .

- We learned from Martinsburg that the more common case is an example of Influenza that was added to File 120.82 at their site. They have a clinical reminder that is being suppressed for any patient that has an allergy to influenza vaccine.

- We are asking sites to assess the impact of standardization of the Allergy files on local clinical reminders.

- National clinical reminders have been thoroughly tested in the SQA process and are working as designed.

### 3 Synonyms

- Some synonyms will no longer be available: Examples: ASA, PCN

With the removal of most drugs from 120.82 and the removal of file 50 from the allergy selection, some synonyms users are accustomed to may no longer be available. The national drug files do not have synonyms. They do have Trade Names, which handles some synonyms, but not the “ASA” for Aspirin or “PCN” for Penicillin type of synonym.

- An NTRT request must be made for additions that sites want to see in the standard.

## Additional known changes to Allergies

#### The Top 10 List for Signs and Symptoms from File 120.83 may now have inactive terms.

ARTPROVIDER,ONE

<!-- image -->

- The **GMRA REQUEST NEW REACTANT** mail group will be notified of inactive Top 10 terms at your site after the VETS push has occurred. A new mail message is sent with each push if new entries are inactivated

- Please replace inactivated terms with standard terms ASAP to prevent clinicians from viewing empty space in the GUI. .

- If the above action is not done, the clinician can click on the scrollbar for the sign and symptom and the empty space will be auto-adjusted and the gap will no longer display.

- CPRS GUI v 26 fill fix this so that there is no blank space.

#### Many new synonyms have been added to the ALLERGY REACTANT file #120.82, as part of data standardization.

When you open the Allergy Reactant Lookup window and enter three characters for a causative agent, you might see a list of matches such as this:

(The new synonyms are the ones in the &lt;&gt; brackets)

<!-- image -->

## ART Changes in CPRS

#### PATCH OR*3*233

**Support for Allergy Synonyms** –Allergy synonyms, if present, are now included in the SIGNS/SYMPTOMS selection box. This is included in patch OR*3*233, which will be distributed with GMRA patch 23. The Signs and Symptoms box in CPRS is populated from File 120.83 REACTIONS or Signs/Symptoms. The synonym for these items in file

120.83 will show in the GUI “Enter or Edit Adverse Reaction” box (in &lt; &gt; brackets after the Sign/Symptom.

#### Example:

CPRSPROVIDER,, ONE

<!-- image -->

You can also search for items in file 120.82 REACTANT by typing in a synonym when entering in an allergy in the GUI. E.g. Tape Adhesive is a synonym of Adhesive Tape.

<!-- image -->

## CPRS GUI 26

1. **Marking Allergies as Entered in Error Now Controlled by Parameter** - In CPRS v25, any user could enter new allergies, mark a patient as NKA (no known allergies), and mark allergies entered in error from the cover sheet and the detailed display window. In v.26, the Entered in Error option requires the new parameter OR ALLERGY ENTERED IN ERROR to be enabled for the user. The other options remain open to all users as before.

1. **Free-Text Signs and Symptoms No Longer Allowed** – To support data standardization efforts, the ability to enter free-text signs/symptoms was removed. Users must now select items from the list of available signs/symptoms.

1. **Inconsistent Sending of Bulletin for Marked on Chart** – CPRS always sent the “Marked on Chart” bulletin if the user entered an allergy from the Orders tab. CPRS never sent the bulletin if the user entered the allergy from the Cover Sheet. This inconsistency has been corrected, and CPRS will never send the bulletin when the user enters a new allergy.

1. The “Bulletin has been sent” message that CPRS displays after the user requests the addition of a new causative agent now includes the same warning included in the bulletin about that reactant not being added to the patient’s record.

## What can sites do?

The standard has been sent to sites to enable an assessment of the impact of standardizing files 120.82, and 120.83 on site-added content to these two files. Specifically, sites should compare standardized content with site content for these two files. Then assess the impact standardized content will have on order checks and clinical reminders.

Following this assessment, sites should create a mitigation plan to ensure the application of the standard does not disrupt site-developed processes. Content requests will follow the NTRT process after the standard has been implemented.

#### Site Preparation

#### Before installing GMRA*4*23

- From FileMan, print file entries for File 120.82 (REACTANTS) and

120.83 (REACTIONS)

#### After installing GMRA*4*23

- From FileMan, print file entries for File 120.82 (REACTANTS) and

120.83 (REACTIONS)

#### Compare file prints from Before and After

- Look for items that are at your site but are not in the Standardized Files.

- Look for Drug ingredients or drug classes not in the standard that you think should be included.

- Identify any Clinical Reminders that would be triggered by local terms that have been removed or changed within the standard.

- Update the Clinical Reminder using the appropriate standard term.

#### Request additions to standardized files using the NTRT process

- To enter a request go to: REDACTED

- Submit research that supports requests for additions, to help expedite the process.

**NOTE:** Please wait for contact from your Technical Support Office (TSO) Partner before activating your Allergy and Outpatient Pharmacy VDEF triggers in the VDEF software. They will contact you as soon as they learn from the Data Standardization team that all necessary steps have been completed for your site to be considered fully standardized for Allergy and Outpatient Pharmacy data. Once activated in the VDEF software, your site data will begin transmitting allergy and outpatient pharmacy data to the National HDR.