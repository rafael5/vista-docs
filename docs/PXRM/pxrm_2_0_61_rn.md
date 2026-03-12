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
source_file: pxrm_2_0_61_rn.docx
status: draft
title: pxrm 2 0 61 rn.docx
---

<!-- image -->

**PXRM*2*61**

**Clinical Reminders**

**NATIONAL TAXONOMY UPDATES INCREMENT 2**

**Release Notes**

**September 2015**

Product Development Office of Information Technology Department of Veterans Affairs

**Table of Contents**

INTRODUCTION	1

INSTALL DETAILS	3

APPENDIX A: INSTALL EXAMPLE	4

APPENDIX B: LIST OF INACTIVATED, UPDATED AND NEW TAXONOMIES	7

## Introduction

PXRM*2.0*61 contains 2 Reminder Exchange entries:

1. **PXRM*2.0*61 TAXONOMY UPDATES INC 2**
2. **PXRM*2.0*61 IRAQ UPDATES**

1. **National Taxonomy Updates:**

This patch is the second patch being developed and released to update national reminder taxonomies to include ICD10 and SNOMED codes. On October 1, 2015, the VA will begin to use ICD-10 diagnosis codes in place of ICD-9. In preparation for this change, the national clinical reminder taxonomies are being reviewed and updated by the responsible Program Offices in VACO. Some of the taxonomies are also being updated to include SNOMED-CT codes which are currently used in VistA/CPRS on the problem list. And in some cases HCPCS codes, CPT codes and ICD10 procedure codes are being added or updated. This taxonomy patch covers the second set of taxonomies whose review has been completed.

The process for review included a detailed review by HIMS coding staff to provide possible ICD10 codes for inclusion and then subsequent review by SMEs designated by the responsible Program Office. The responsible Program Office is listed as the sponsor in each taxonomy definition.

In the process of reviewing all the national taxonomies, a large number of old and outdated Taxonomies were found that were originally used in reminders that were distributed in 1996. Most of those old, antiquated reminders have already been inactivated and renamed but the taxonomies that were included in them had not been reviewed or updated. These taxonomies are being renamed with a leading 'ZZ' and inactivated by this patch. These taxonomies should not be in use at any site and there are no plans to support them or update them.

Sites should run a Taxonomy Inquiry for each taxonomy being updated (refer to appendix B) and either print out or save to a file for comparison after patch install.

.

1. **IRAQ&amp;AFGHAN POST-DEPLOYMENT SCREEN Reminder Dialog Update**

Remedy ticket xxxxxxxx was entered which listed an issue    with    the    URL’s    not   functioning   anymore.	These  URL’s  were  changed  and  now are    working    correctly    with     the     release     of this   patch.	To accomplish this, 2 reminder dialog    elements   were   changed.	They are as follows:

1. VA-TEXT OIF WEB SITES
2. VA-TEXT OIF INTRO

In the IRAQ&amp;AFGHAN POST-DEPLOYMENT SCREEN reminder dialog, the hyperlinks were no longer working. This was corrected and the number of links was reduced. Below are screenshots of Pre and Post install of PXRM*2.0*61

IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREEN reminder dialog prior to install of PXRM*2.0*61

<!-- image -->

IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREEN reminder dialog post install of PXRM*2.0*61

<!-- image -->

## Install Details

This patch is being distributed as a host file.  The name of the host file is PXRM\_2\_0\_61.KID. This file should be downloaded in ASCII format.

The preferred method for obtaining these files is to use File Transfer Protocol (FTP) to download them from: ftp://download.vista.med.va.gov/.

This transmits the files from the first available FTP server. Sites may also elect to retrieve the files directly from a specific server as follows:

Albany	REDACTED

Hines	REDACTED

Salt Lake City		REDACTED

| File Name:         | Description:          | Protocol:   |
|--------------------|-----------------------|-------------|
| ==========         | ============          | =========   |
| PXRM_2_0_61.KID    | PXRM*2.0*61 Host File | ASCII       |
| PXRM_2_0_61_RN.PDF | Release Notes         | Binary      |

Installation:

=============

This patch can be loaded with users on the system. Installation will take five to ten minutes. Refer to Release Notes, PXRM\_2\_0\_61\_RN.PDF, for complete details.

1. Use the "Load a Distribution' option on the KIDS installation

menu. When prompted to enter a host file type in PXRM\_2\_0\_61.KID

1. On the KIDS menu under the 'INSTALLATION' menu, use the following options, as desired:

Print Transport Global

Compare Transport global to Current System Verify Checksums in Transport Global Backup a Transport Global

1. On the KIDS menu under the 'INSTALLATION' menu, use the following option to install the patch:

Install Package(s)

When prompted for INSTALL NAME, use PXRM*2.0*61

1. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//," respond 'NO'.

1. When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// respond 'NO'.

1. After successful installation, the following init routines may be deleted

PXRMP61E PXRMP61I

## Appendix A: Install Example

Select Installation &lt;TEST ACCOUNT&gt; Option: 1 Load a Distribution Enter a Host File: USER$:[PATRICK]TEST61.KID

KIDS Distribution saved on Aug 10, 2015@11:14:19 Comment: National taxonomy updates, increment 2.

This Distribution contains Transport Globals for the following Package(s): Build PXRM*2.0*61 has been loaded before, here is when:

PXRM*2.0*61 **Transport Global already exists**

**NOTHING LOADED**

Select Installation &lt;TEST ACCOUNT&gt; Option: 1 Load a Distribution Enter a Host File: USER$:[PATRICK]TEST61.KID

KIDS Distribution saved on Aug 10, 2015@11:14:19 Comment: National taxonomy updates, increment 2.

This Distribution contains Transport Globals for the following Package(s): PXRM*2.0*61

Distribution OK!

Want to Continue with Load? YES// Loading Distribution...

PXRM*2.0*61

Use INSTALL NAME: PXRM*2.0*61 to install this Distribution.

1. Load a Distribution
2. Verify Checksums in Transport Global
3. Print Transport Global
4. Compare Transport Global to Current System
5. Backup a Transport Global
6. Install Package(s)

Restart Install of Package(s) Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option You've got PRIORITY mail!

Select Installation &lt;TEST ACCOUNT&gt; Option: INstall Package(s) Select INSTALL NAME: PXRM*2.0*61	8/11/15@07:51:48

=&gt; National taxonomy updates, increment 2. ;Created on Aug 10, 2015@11:1

This Distribution was loaded on Aug 11, 2015@07:51:48 with header of National taxonomy updates, increment 2. ;Created on Aug 10, 2015@11:14:19 It consisted of the following Install(s):

PXRM*2.0*61

Checking Install for Package PXRM*2.0*61 Install Questions for PXRM*2.0*61 Incoming Files:

811.8	REMINDER EXCHANGE (including data)

Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH Virtual Terminal

Install Started for PXRM*2.0*61 : Aug 11, 2015@07:51:55

Build Distribution Date: Aug 10, 2015 Installing Routines:

Aug 11, 2015@07:51:55

Running Pre-Install Routine: PRE^PXRMP61I

Checking for obsolete national taxonomies to be inactivated. Installing Data Dictionaries:

Aug 11, 2015@07:51:55

Installing Data:

Aug 11, 2015@07:51:56

Running Post-Install Routine: POST^PXRMP61I There are 2 Reminder Exchange entries to be installed.

1. Installing Reminder Exchange entry PXRM*2.0*61 IRAQ UPDATES
2. Installing Reminder Exchange entry PXRM*2.0*61 TAXONOMY UPDATES INC 2 Updating Routine file...

Updating KIDS files...

PXRM*2.0*61 Installed.

Aug 11, 2015@07:54:14

Not a production UCI

PXRM*2.0*61

Install Completed

## Appendix B: List of inactivated and updated

List to be inactivated and renamed VA-IM FLU H1N1 (1 DOSE)

List to be updated by patch 61 VA-ECOE DIAGNOSIS CODES

VA-DEPRESSION DX OUTPT VISIT VA-DEPRESSION DIAGNOSIS

VA-PTSD DX OUTPT PRIMARY VA-PTSD DX OUTPT VISIT

VA-PTSD DIAGNOSIS VA-SCHIZOPHRENIA VA-DIABETES

VA-DIABETES HEDIS

VA-DIABETES HEDIS PROB LIST

VA-EBOLA RISK TRIAGE DIAGNOSIS CODE VA-PALLI CONS CANCER/HEMA COND

VA-PALLI CONS CARDIO COND OTHER THAN CA VA-PALLI CONS CNS COND OTHER THAN CA

VA-PALLI CONS DERM CONDITION DX VA-PALLI CONS GI OTHER THAN CA VA-PALLI CONS INFECTIOUS COND

VA-PALLI CONS RENAL OTHER THAN CA VA-PALLI CONS RHEUM/VASC/THROMB

VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES) VA-WH TUBAL LIGATION CODES (TAXONOMY)

VA-PSYCHOTHERAPY CPT CODES