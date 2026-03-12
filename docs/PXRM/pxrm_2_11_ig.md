---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: 112
patch_gap: null
section: ''
source_file: pxrm_2_11_ig.docx
status: draft
title: pxrm 2 11 ig.docx
---

**Clinical Reminders**

**Patch PXRM*2*11**

**National Reminder and Dialog Updates**

## INSTALLATION &amp; SETUP GUIDE

**October 2008**

Health Provider Systems


Contents

Introduction	1

Web Sites	1

Pre-Installation	2

Required Software	2

Estimated Installation Time	2

Pre-Installation Steps	2

Installation	5

1.	Retrieve the PXRM*2.0*11 build	5

2.	Install the build first in a training or test account.	5

3.	Load the distribution.	5

a.	Backup a Transport Global	5

b.	Compare Transport Global to Current System	5

c.	Verify Checksums in Transport Global	5

d.	Print Transport Global (optional)	6

4.	Install the build.	6

5.	Install File Print (optional)	7

6.	Build File Print (optional)	7

7.	Post-installation routine	7

8.	Deletion of init routines	8

Setup and Maintenance	9

Overview	9

Setup Steps	12

1.  Repeat the pre-installation reminder inquiry and compare the pre- and post-installation output.	12

2.  Map Local Findings to National Terms	13

3. Edit Reminder Dialogs	14

Mapping a consult quick order for the VA-TBI SCREENING reminder dialog:	17

4. Verify that the dialogs function properly	17

Appendix A: Installation Example	19

Appendix B: Setting up a TIU/HS Object for the AUDIT-C Test	21

Appendix C: Computed Finding Descriptions	24

## Introduction


Patch PXRM*2.0*11 includes the following modifications to the Clinical Reminders package:

- Updates eleven reminder definitions (and their dialogs if there is one attached), based on changes required by the Office of Patient Care Services and problems reported in Remedy tickets.
    - Installs four new reminders.
    - Installs 11 new or modified service-related computed findings.
    - Updates URLs in six reminders.
    - Modifies Location List exclusion functionality
    - Modifies Reminder Test output
    - Corrects several problems reported in Remedy tickets:
229723 	Nat'l reminder component "PXRM AUDC RESULT has errors
233994 	Discrepancy between VA-Iraq/Afghan Post Deploy reminder dialog and clinical maintenance display
242238 	Duplicate text in AIMS test
239704 	Display inconsistent for VA-IRAQ&amp;AFGHANISTAN POST DEPLOYMENT
234380. 	National OIF reminder is producing conflicting information in clinical maintenance vs the reminder dialog concerning section 4
238209 	Functionality of I/A and TBI reminders
See the Setup section of this manual for instructions about mapping terms and dialogs.

#### Web Sites

| **Site**                         | **URL**                                                              | **Description**                                                                            |
|----------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site | http://vista.med.va.gov/reminders                                    | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VA Mental Health Home            | [http://vaww.mentalhealth.va.gov/](http://vaww.mentalhealth.va.gov/) | Contains items of interest for all VA mental health clinicians                             |
| Document Library                 | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                     | Contains manuals for Clinical Reminders and Mental Health YS*5.01*85                       |


## Pre-Installation

This manual describes how to install and set up Clinical Reminders patch PXRM*2.0*11.

### Required Software

| **Package/Patch**                     | **Namespace**   |   **Version** | **Comments**   |
|---------------------------------------|-----------------|---------------|----------------|
| Clinical Reminders                    | PXRM            |          2    | Fully patched  |
| Health Summary                        | GMTS            |          2.7  | Fully patched  |
| HL7                                   | HL              |          1.6  | Fully patched  |
| Kernel                                | XU              |          8    | Fully patched  |
| MailMan                               | XM              |          7.1  | Fully patched  |
| Mental Health  YS*5.01*85             | YS              |          5.01 |                |
| Pharmacy Data Management  PSS*1.0*112 | PSS             |          1    |                |
| Outpatient Pharmacy  PSO*7.0*245      | PSO             |          7    |                |
| VA FileMan                            | DI              |         22    | Fully patched  |


### Estimated Installation Time

| Setup before installation                                                               | Approximately 30 minutes                                                                |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Installation                                                                            | About 5-10 minutes                                                                      |
| Setup after installation by the Reminder Manager or CAC to address local implementation | Approximately one hour (depending partly on the experience level of the manager or CAC) |


### Pre-Installation Steps

**1.  Do a reminder definition inquiry on the following reminders and save for post-installation comparisons:**

VA-ALCOHOL AUDIT-C POSITIVE F/U

VA-ALCOHOL USE SCREEN (AUDIT-C)

VA-BL DEPRESSION SCREEN

VA-BL PTSD SCREEN

VA-BL OEF/OIF FEVER

VA-BL OEF/OIF GI SX

VA-BL OEF/OIF SKIN SX

VA-DEPRESSION SCREENING

VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN

VA-MHV CERVICAL CANCER SCREEN

VA-MHV COLORECTAL CANCER SCREEN

VA-MHV DIABETES FOOT EXAM

VA-MHV DIABETES RETINAL EXAM

VA-MHV HYPERTENSION

VA-MHV INFLUENZA VACCINE

VA-MHV MAMMOGRAM SCREENING

VA-MHV PNEUMOVAX

VA-PTSD SCREENING

VA-TBI SCREENING


**2.  Do a reminder term inquiry and save for post-installation comparisons**


The following terms have changed and may need to be remapped, if previously mapped locally. **The ones in bold will almost definitely need remapping.** Please use the option, “Inquire about a reminder term” on these terms for post-installation comparison and remapping.

VA-COGNITIVE IMPAIRMENT

**VA-DEPRESSION SCREEN OEF/OIF**

**VA-LDL**

**VA-MHV BARIUM ENEMA**

**VA-MHV COLONOSCOPY**

**VA-MHV DIABETIC FOOT EXAM COMPLETE**

**VA-MHV DIABETIC FOOT EXAM INSPECTION**

**VA-MHV DIABETIC FOOT EXAM MONOFILAMENT**

**VA-MHV DIABETIC FOOT EXAM PULSES**

**VA-MHV HBA1C &lt;8.0**

**VA-MHV HBA1C &gt;7.9**

**VA-MHV HBA1C ALL RESULTS**

**VA-MHV HDL – lab test and outside lab test**

VA-MHV INFLUENZA IMMUNIZATION

**VA-MHV LIPID PANEL ORDERABLE ITEMS**

**VA-MHV OCCULT BLOOD PANEL**

**VA-MHV OCCULT BLOOD SINGLE TEST**

VA-MHV OUTSIDE LDL

VA-MHV OUTSIDE LDL&gt;99

VA-MHV PNEUMOCOCCAL IMMUNIZATION

**VA-MHV SIGMOIDOSCOPY**

**VA-MHV TOTAL CHOLESTEROL**

**VA-MHV TRIGLYCERIDES**

VA-PTSD SCREEN

VA-WH HYSTERECTOMY W/CERVIX REMOVED

VA-WH MAMMOGRAM ORDER

VA-WH MAMMOGRAM SCREEN DEFER

VA-WH MAMMOGRAM SCREEN DONE

VA-WH MAMMOGRAM SCREEN NOT INDICATED

VA-WH PAP SMEAR DONE

VA-WH PAP SMEAR OBTAINED

VA-WH PAP SMEAR ORDER HEALTH FACTOR

VA-WH PAP SMEAR SCREEN NOT INDICATED

**3.  Create an Audit-C TIU/HS Object for the VA-Alcohol Use Screen Reminder (see instructions in** **Appendix B.**

**4.** The reminder dialog element VA-PDIQ POLYTRAUMA CONSULT, which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu or quick order that you use to order a TBI consult.


## Installation

This build can be installed with users on the system, but it should be done during non-peak hours.

***The installation needs to be done by a person with DUZ(0) set to "@."***

### 1 Retrieve the PXRM*2.0*11 build

Use ftp to access the build – the name of the host file is PXRM\_2\_0\_11.KID –  from one of the following locations:

Albany                         REDACTED                  REDACTED

Hines                           REDACTED                  REDACTED

Salt Lake City             REDACTED                  REDACTED

### 2 Install the build first in a training or test account.

Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### 3 Load the distribution.

In programmer mode type, D ^XUP, select the Kernel Installation &amp; Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution.  Enter your directory name and PXRM\_2\_0\_11.KID at the Host File prompt.

**Example**

Select Installation Option: **LOAD** a Distribution

Enter a Host File: **PXRM\_2\_0\_11.KID**

KIDS Distribution saved on June 14, 2008@11:53:53

Comment: PXRM*2.0*11

From the Installation menu, you may elect to use the following options:


### 4 Backup a Transport Global

This option will create a backup message of any routines exported with the patch.  It will NOT back up any other changes such as DDs or templates.

### 5 Compare Transport Global to Current System

This option will allow you to view all changes that will be made when the patch is installed.  It compares all components of the patch (routines, DDs, templates, etc.).

### 6 Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global.  If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.  Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again.  If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

### 7 Print Transport Global (optional)

This option will allow you to view the components of the KIDS build.

### 8 Install the build.

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s).  Select the build PXRM*2.0*11 and proceed with the install.  If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Select Installation &amp; Distribution System Option: **Installation**

Select Installation Option: **INSTALL PACKAGE(S)**

Select INSTALL NAME: PXRM*2.0*11

Answer "NO" to the following prompt:

Want KIDS to INHIBIT LOGONs during install? NO// **NO**

**NOTE: DO NOT QUEUE THE INSTALLATION** , because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

The reminder dialog element VA-PDIQ POLYTRAUMA CONSULT, which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu, order dialog, or quick order that you use to order a TBI consult. **Installation Example**

See Appendix A.

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: **XPD MAIN** Kernel Installation &amp; Distribution System menu

Select Kernel Installation &amp; Distribution System Option: **Installation**

Select Installation Option: **Install** Package(s)  [XPD INSTALL BUILD]

Select INSTALL NAME: PXRM*2.0*11

### 9 Install File Print (optional)

Use the KIDS Install File Print option to print out the results of the installation process.

Select Utilities Option: **Install** File Print

Select INSTALL NAME: **PXRM*2.0*11**

### 10 Build File Print (optional)

Use the KIDS Build File Print option to print out the build components.

Select Utilities Option:  Build File Print

Select BUILD NAME:    PXRM*2.0*11     CLINICAL REMINDERS

DEVICE: HOME//

### 11 Post-installation routine

The installation will place the following exchange file entries in the Reminder Exchange file #811.8:

**PATCH 11 ITEMS**

VA-ALCOHOL AUDIT-C POSITIVE F/U

VA-ALCOHOL USE SCREEN (AUDIT-C

VA-BL DEPRESSION SCREEN

VA-BL PTSD SCREEN

VA-BL OEF/OIF EMBEDDED FRAGMENTS

VA-BL OEF/OIF FEVER

VA-BL OEF/OIF GI SX

VA-BL OEF/OIF SKIN SX

VA-CV ELIG W/HF FOR NO SERVICE

VA-CV INELG W/HF FOR SERVICE

VA-DEPRESSION SCREENING

VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN

VA-MHV CERVICAL CANCER SCREEN

VA-MHV COLORECTAL CANCER SCREEN

VA-MHV DIABETES FOOT EXAM

VA-MHV DIABETES RETINAL EXAM

VA-MHV HYPERTENSION

VA-MHV INFLUENZA VACCINE

VA-MHV MAMMOGRAM SCREENING

VA-MHV PNEUMOVAX

VA-OEF/OIF MONITOR REPORTING

VA-PTSD SCREENING

VA-TBI SCREENING

The post-init will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

### 12 Deletion of init routines

After everything has been successfully installed you may delete the following init routines:  PXRMP11I, PXRMP11E

## Setup and Maintenance

#### Overview

PXRM*2.0*11 includes the following additions and modifications:

- New and modified national reminder definitions and dialogs
    - New reminders to help clerks reconcile HEC data and self-reported VA-IRAQ/AFGHAN SERVICE health factor
    - New national reminder for the monitor
- New and modified computed findings
- Modified Location List exclusion functionality
- Modified Reminder Test output
- Fixes to My HealtheVet reminders function finding pointers

**New Reminder Definitions**

| VA-BL OEF/OIF EMBEDDED FRAGMENTS                             | New reminder for branching logic in the new 4  th  question in the last section of the OEF/OIF reminder. Used for branching logic to indicate in the reminder dialog that an item is already completed or not needed.                                                                 |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-CV ELIG W/HF FOR NO SERVICE  VA-CV INELG W/HF FOR SERVICE | These two reminders are designed to aid sites in identifying patients whose combat veteran eligibility data and data collected from the OEF/OIF Screening reminder are not in agreement.  Reminder patient list functionality can be used to identify patients needing reconciliation |
| VA-OEF/OIF MONITOR REPORTING                                 | New reminder for reporting this monitor.  Excludes non-combat vets from the denominator; requires two visits after discharge separation.                                                                                                                                              |

**Modified national reminder definitions**

- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- VA-ALCOHOL USE SCREEN (AUDIT-C)
- VA-BL OEF/OIF FEVER
- VA-BL OEF/OIF GI SX
- VA-BL OEF/OIF SKIN SX
- VA-DEPRESSION SCREENING
- VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN
- VA-MHV COLORECTAL CANCER SCREEN
- VA-MHV HYPERTENSION
- VA-MHV DIABETES RETINAL EXAM
- VA-PTSD SCREENING
- VA-TBI SCREENING

**New and modified Service-related Computed Findings**

- VA-AGENT ORANGE EXPOSURE
- VA-COMBAT SERVICE
- VA-COMBAT VET ELIGIBILITY
- VA-LAST SERVICE SEPARATION DATE  (modified)
- VA-OEF SERVICE
- VA-OIF SERVICE
- VA-POW
- VA-PURPLE HEART
- VA-SERVICE BRANCH
- VA-UNKNOWN OEF/OIF SERVICE
- VA-VETERAN (modified)

**Modified Location List exclusion functionality**

- Exclusion location list can be defined once
- Any location lists can reference the pre-defined Exclusion location list

**Modified My HealtheVet Reminders**

- Updated URLs:

VA-MHV CERVICAL CANCER SCREEN

VA-MHV DIABETES FOOT EXAM

VA-MHV DIABETES RETINAL EXAM

VA-MHV HYPERTENSION

VA-MHV INFLUENZA VACCINE

VA-MHV MAMMOGRAM SCREENING

- VA-MHV COLORECTAL CANCER SCREEN

Added reminder term for barium enema

- VA-MHV DIABETES RETINAL EXAM

Updated to use only prior exam as indication of frequency of exams instead of HbA1c level and use of insulin.

- VA-MHV HYPERTENSION

Converted findings to national reminder terms.

- VA-MHV INFLUENZA VACCINE

Updated the date to August 2008

- VA-MHV PNEUMOVAX

The reminder term VA-MHV HIGH RISK FOR PNEUMONIA was made national.

**Dialog Updates**

| VA-DEPRESSION SCREEN                         | PHQ-9 not required; MH test in dialog set to ‘2’ – required if opened; informational text for dialog edited to remove PHQ-9                                                                                                                                    |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-PTSD SCREENING                            | - MH test in dialog set to ‘2’ – required if opened - Added Acute Illness to dialog - Added cognitive impairment - Added done elsewhere - Doesn’t ask the “Did you serve…? “ question if combat vet eligible - Substituted Q4D – asks about embedded fragments |
| VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN |                                                                                                                                                                                                                                                                |

#### Setup Steps

### Repeat the pre-installation reminder inquiry and compare the pre- and post-installation output.

The following reminder definitions have been changed. These may require remapping.  The ones in red may require remapping as well as a check of the dialog for any orders that need to be re-linked.

| **Reminder**                                 | **Change**                                                                                                                                                                                                                                           |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL         | Fixed branching logic                                                                                                                                                                                                                                |
| VA-ALCOHOL USE SCREEN (AUDIT-C)              | Changes to dialog.  Removed date from term and moved to the health factor for “No alcohol in the past 1 year”                                                                                                                                        |
| VA-BL OEF/OIF FEVER                          | Fixed logic                                                                                                                                                                                                                                          |
| VA-BL OEF/OIF GI SX                          | Fixed logic                                                                                                                                                                                                                                          |
| VA-BL OEF/OIF SKIN SX                        | Fixed logic                                                                                                                                                                                                                                          |
| VA-DEPRESSION SCREENING                      | Changes to terms and dialog; verify/report any changes                                                                                                                                                                                               |
| VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN | Multiple changes:  - Added Combat Vet to logic - Excluded those who did not serve from denominator - Added cognitive impairment to exclusions - Added done elsewhere to resolutions - Updated dates of health factors for depression/PTSD to 10/1/08 |
| VA-MHV COLORECTAL CANCER SCREEN              | VA-MHV BARIUM ENEMA added                                                                                                                                                                                                                            |
| VA-MHV HYPERTENSION                          | Uses reminder terms                                                                                                                                                                                                                                  |
| VA-MHV DIABETES RETINAL EXAM                 | Frequency depends on no retinopathy only                                                                                                                                                                                                             |
| VA-PTSD SCREENING                            | Added veteran status  Added Acute Illness to the dialog                                                                                                                                                                                              |
| VA-TBI SCREENING                             | Two new Finding Items were added: VA-COMBAT VET and (FI10) VA-COGNITIVE IMPAIRMENT, and a change in the Cohort and Resolution logic                                                                                                                  |

#### Map Local Findings to National Terms

The following terms have changed and may need to be remapped, if previously mapped locally:

**The ones in bold will almost definitely need remapping.**

| **Term**                                       | **Mapping**                                                                                                        |    |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----|
| VA-COGNITIVE IMPAIRMENT                        |                                                                                                                    |    |
| **VA-DEPRESSION SCREEN OEF/OIF**               |                                                                                                                    |    |
| **VA-LDL**                                     | **All local lab tests for LDL**                                                                                    |    |
| **VA-MHV BARIUM ENEMA**                        | **Add outside BE**                                                                                                 |    |
| **VA-MHV COLONOSCOPY**                         | **Add outside colonoscopies or other HFs**                                                                         |    |
| **VA-MHV DIABETIC FOOT EXAM COMPLETE**         | **All 3 components completed**                                                                                     |    |
| **VA-MHV DIABETIC FOOT EXAM INSPECTION**       | **Local exams and/or HFs**                                                                                         |    |
| **VA-MHV DIABETIC FOOT EXAM MONOFILAMENT**     | **Local exams and/or HFs**                                                                                         |    |
| **VA-MHV DIABETIC FOOT EXAM PULSES**           | **Local exams and/or HFs**                                                                                         |    |
| **VA-MHV HBA1C &lt;8.0**                       | **Local labs with condition I +V&lt;8and outside HFs**                                                             |    |
| **VA-MHV HBA1C &gt;7.9**                       |                                                                                                                    |    |
| **VA-MHV HBA1C ALL RESULTS**                   |                                                                                                                    |    |
| **VA-MHV HDL – lab test and outside lab test** |                                                                                                                    |    |
| VA-MHV INFLUENZA IMMUNIZATION                  | Two national entries are included                                                                                  |    |
| **VA-MHV LIPID PANEL ORDERABLE ITEMS**         |                                                                                                                    |    |
| **VA-MHV OCCULT BLOOD PANEL**                  | **Lab test for panel**                                                                                             |    |
| **VA-MHV OCCULT BLOOD SINGLE TEST**            | **Lab test for individual tests in the occult blood panel e.g. occult blood #1, occult blood #2, occult blood #3** |    |
| VA-MHV OUTSIDE LDL                             | Local HFs for outside LDLs, national HFs are included                                                              |    |
| VA-MHV OUTSIDE LDL>99                          | Outside HFs, national HFs are included                                                                             |    |
| VA-MHV PNEUMOCOCCAL IMMUNIZATION               | National entry is included                                                                                         |    |
| **VA-MHV SIGMOIDOSCOPY**                       | **Outside sigmoidoscopies or other HFs**                                                                           |    |
| **VA-MHV TOTAL CHOLESTEROL**                   | **Local labs and outside HFs**                                                                                     |    |
| **VA-MHV TRIGLYCERIDES**                       | **Local labs and outside HFs**                                                                                     |    |
| VA-PTSD SCREEN                                 |                                                                                                                    |    |
| VA-WH HYSTERECTOMY W/CERVIX REMOVED            | Includes taxonomy and national HF                                                                                  |    |
| VA-WH MAMMOGRAM ORDER                          | Orderable item and HF included, add local HFs or orders                                                            |    |
| VA-WH MAMMOGRAM SCREEN DEFER                   | Two national HFs included                                                                                          |    |
| VA-WH MAMMOGRAM SCREEN DONE                    | Taxonomies and national HF included, add any local HFs                                                             |    |
| VA-WH MAMMOGRAM SCREEN NOT INDICATED           | Includes terminal cancer and limited life expectancy, add local HFs for limited life expectancy                    |    |
| VA-WH PAP SMEAR DONE                           | Includes taxonomy and national HF                                                                                  |    |
| VA-WH PAP SMEAR OBTAINED                       | Includes national taxonomy                                                                                         |    |
| VA-WH PAP SMEAR ORDER HEALTH FACTOR            | Already contains four national HFs                                                                                 |    |
| VA-WH PAP SMEAR SCREEN NOT INDICATED           | Limited life expectancy and terminal cancer taxonomy, add local HFs for limited life expectancy                    |    |

**Example: Mapping a Local Health Factor Finding to the National Reminder Term**

Select Reminder Term Management Option: **te** Add/Edit Reminder Term

Select Reminder Term: **VA-ALCOHOL USE SCREEN** NATIONAL

Enter local health factors or exams that your site uses to represent positive or negative screens for alcohol use.

...OK? Yes//   (Yes)

Select FINDING ITEM: 10-Question Audit

Searching for a MENTAL HEALTH INSTRUMENT, (pointed-to by FINDING ITEM)

Searching for a MENTAL HEALTH INSTRUMENT

TENS

...OK? Yes//   (Yes)

Are you adding 'TENS' as a new FINDINGS (the 6TH for this REMINDER TERM)? No//

**Y** (Yes)

Editing Finding Number: 6  FINDING ITEM: 10-Question Audit

EFFECTIVE PERIOD:

USE INACTIVE PROBLEMS:

WITHIN CATEGORY RANK:

EFFECTIVE DATE:

MH SCALE:

CONDITION:

CONDITION CASE SENSITIVE:

RX TYPE:

Select FINDING ITEM:


#### Edit Reminder Dialogs

Several Dialog Elements may need to be remapped after patch 11 is installed. For example, the reminder dialog element **VA-PDIQ POLYTRAUMA CONSULT,** which is used to order a TBI consult, is overwritten in the install. You will need to re-enter the finding item for this element using the menu or quick order that you use to order a TBI consult. **VA-GP ALC SCREEN POS REFERRAL** and **TBI OI CONSULT FOR KNOWN TBI** **are also overwritten.**

The objects in the element TXT ALC LABS &amp; VS, in the VA-GP ALC AUDIT &gt;7 (added after Patch 6 was installed) will also need to be remapped.

Check the dialogs for any orders that need to be re-linked for the following:

- VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
- VA-ALCOHOL USE SCREEN (AUDIT-C)
    - VA-BL DEPRESSION SCREENING
        - VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN
            - VA-IRAQ/AFGHAN SERVICE
            - VA-MHV HIGH RISK FOR PNEUMONIA
            - VA-MHV INFLUENZA IMMUNIZATION
                - VA-PTSD SCREENING
            **Steps to add or edit dialog elements:**
            a.  Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):Select Reminder Managers Menu Option: **DM** Reminder Dialog Management
            DP     Dialog Parameters ...
            DI     Reminder DialogsSelect Reminder Dialog Management Option: **DI** Reminder Dialogs
            Dialog List                   Aug 30, 2007@09:55:38          Page:    1 of    8
            REMINDER VIEW (ALL REMINDERS BY NAME)
            Item Reminder Name                      Linked Dialog Name &amp; Dialog Status
            1  AGETEST                            AGETEST                       Disabled
            7  ALCOHOL USE SCREEN                 ALCOHOL USE SCREEN DIALOG
            3  HIV HEPATITIS A SEROLOGIC TESTING  HIV HEPATITIS A SEROLOGIC T
            4  HYPERTENSION                       HYPERTENSION GROUP            Disabled
            5  Hypertension Screen (VHACHS)       Hypertension Screen (local)
            **+         Enter ?? for more actions                                          &gt;&gt;&gt;**
            AR   All reminders        LR   Linked Reminders     QU   Quit
            CV   Change View          RN   Name/Print Name
            **Select Item: Next Screen//**
            b.  Use the Change View (CV) action to see the Dialog Elements view.
            **Select Item: Next Screen// CV**
            Select one of the following:
            D         Reminder Dialogs
            E         Dialog Elements
            F         Forced Values
            G         Dialog Groups
            P         Additional Prompts
            R         Reminders
            RG        Result Group (Mental Health)
            RE        Result Element (Mental Health)**TYPE OF VIEW: R// E** Dialog Elements
            Dialog List                   Sep 04, 2007@10:36          Page:    1 of  120
            DIALOG VIEW (DIALOG ELEMENTS)
            Item Dialog Name                             Dialog type              Status
            1  04 AUDIT-C                              Dialog Element
            2  ABILITY FAIR (SLC)                      Dialog Element
            3  ABILITY FAIR 1                          Dialog Element
            4  ABILITY GOOD                            Dialog Element
            5  ABILITY POOR                            Dialog Element
            6  ADD'L INFO                              Dialog Element
            7  ADDITIONAL COMMENTS (PXRM COMMENT)      Dialog Element
            8  ADDITIONAL COMMENTS(2 LINES WP)         Dialog Element
            **+         + Next Screen   - Prev Screen   ?? More Actions                    &gt;&gt;&gt;**
            AD   Add                  CV   Change View          INQ  Inquiry/Print
            CO   Copy Dialog          PT   List/Print All       QU   Quit
            Select Item: Next Screen//
            c.  Use the Search List (SL) action to get to the dialog element you want the edit.
            Select Item: Next Screen// SL   SL
            Search for: VA-HF DEP
            ...searching for 'VA-HF DEP'............
            e. Make edits, as needed, by entering the dialog element number.
            Find Next 'VA-HF DEP'? Yes// NO
            Dialog List                   Sep 04, 2007@10:25:40          Page:   77 of  120
            DIALOG VIEW (DIALOG ELEMENTS)
            +Item Dialog Name                             Dialog type              Status
            1232  VA-HF DEP 2 QUESTION NEG                Dialog Element
            1233  VA-HF DEP 2 QUESTION POS                Dialog Element
            1234  VA-HF DEP ACUTE ILLNESS                 Dialog Element
            1235  VA-HF DEP ACUTE MED CONDITION           Dialog Element
            1236  VA-HF DEP CHRONIC MED CONDITION         Dialog Element
            1237  VA-HF DEP REFERRAL TO MHC               Dialog Element
            1238  VA-HF DEP TO BE MANAGED IN PC           Dialog Element
            1239  VA-HF DEP TO BE MANAGED IN PC (2)       Dialog Element
            1240  VA-HF ETOH ADVISE NEGOTIATED LEVEL      Dialog Element
            1241  VA-HF ETOH ADVISE PT RESPONSE NO CHANGE Dialog Element
            1242  VA-HF ETOH ADVISE PT RESPONSE WILL PLAN Dialog Element
            1243  VA-HF ETOH DSM IV CONTINUED USE         Dialog Element
            1244  VA-HF ETOH DSM IV DRINKS LARGE AMT      Dialog Element
            **1245  VA-HF ETOH DSM IV IMPAIRED CONTROL      Dialog Element**
            1246  VA-HF ETOH DSM IV NEGLECT OTHER RESPONS Dialog Element
            1247  VA-HF ETOH DSM IV TOLERANCE             Dialog Element
            **+         + Next Screen   - Prev Screen   ?? More Actions                    &gt;&gt;&gt;**
            AD   Add                  CV   Change View          INQ  Inquiry/Print
            CO   Copy Dialog          PT   List/Print All       QU   Quit
            Select Item: Next Screen// 1234
            Dialog Name:  VA-HF DEP ACUTE ILLNESS
            Current dialog element/group name: VA-HF DEP ACUTE ILLNESS
            Used by:  VA-GP DEP UNABLE TO SCREEN (Dialog Group)
            VA-GP PTSD UNABLE TO SCREEN (Dialog Group)
            FINDING ITEM: UNABLE TO SCREEN - ACUTE ILLNESS//


#### Mapping a consult quick order for the VA-TBI SCREENING reminder dialog:

1.  Type the name of the dialog element, VA-PDIQ POLYTRAUMA CONSULT (or TBI OI CONSULT FOR KNOWN TBI?)

Select Item: Next Screen// SL   SL

Search for: VA-TBI OI CONSULT FOR KNOWN TBI

...searching for ' VA-TBI OI CONSULT FOR KNOWN TBI'............

2.  At the “Find Next” prompt, type No.

3. Type the item number next to the element.

4.  At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.

5. Press Enter at the Additional Finding prompt.

#### Verify that the dialogs function properly

Test the reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.

***Steps to test dialogs:***

1. On the cover sheet, click on the Reminders icon.
2. Click on reminders in the Reminders box to see details of a reminder
3. Open the Notes tab and select New Note. Enter a title and visit information.
4. Open the Reminders drawer and review the contents.
5. Locate the reminder dialog and open it.
6. In the dialog box, check relevant actions.
7. Finish the reminder processing.
8. Review the text added to the note to assure its correctness.
9. Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.
10. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.

1. Repeat steps 5-10 for the Depression Assessment, Iraq &amp; Afghan Post-Deployment Screen, and VA-PTSD SCREENING dialogs.

**NOTE: Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately. This is especially critical if you’re doing the screening reminder and want to see the follow-up reminder become due because of positive results.**


## Appendix A: Installation Example

Select Installation Option: INSTAll Package(s)

Select INSTALL NAME:    PXRM*2.0*11     Loaded from Distribution  10/7/08@14:01:56

=&gt; PXRM*2.0*11  ;Created on Sept 26, 2008@11:08:46

It consisted of the following Install(s):

PXRM*2.0*11

Install Started for PXRM*2.0*11 :

Oct 07, 2008@05:47:49

Build Distribution Date: Sep 26, 2008

Installing Routines:               Oct 07, 2008@05:47:49

Running Pre-Install Routine: PRE^PXRMP11I

DISABLE options.

DISABLE protocols.

Removing old data dictionaries.

Deleting data dictionary for file # 810.9

Installing Data Dictionaries:               Oct 07, 2008@05:47:50

Installing Data:

Oct 07, 2008@05:47:52

Running Post-Install Routine: POST^PXRMP11I

Rebuilding Function Finding internal data structures.

ENABLE options.

ENABLE protocols.

There are 25 Reminder Exchange entries to be installed.

Installing Reminder Exchange entry PATCH 11 LOCATION LIST

Installing Reminder Exchange entry VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL

Installing Reminder Exchange entry VA-ALCOHOL USE SCREEN (AUDIT-C)

Installing Reminder Exchange entry VA-BL OEF/OIF EMBEDDED FRAGMENTS

Installing Reminder Exchange entry VA-BL OEF/OIF FEVER

Installing Reminder Exchange entry VA-BL OEF/OIF GI SX

Installing Reminder Exchange entry VA-BL OEF/OIF SKIN SX

Installing Reminder Exchange entry VA-CV ELIG W/HF FOR NO SERVICE

Installing Reminder Exchange entry VA-CV INELG W/HF FOR SERVICE

Installing Reminder Exchange entry VA-DEPRESSION SCREENING

Installing Reminder Exchange entry VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN

Installing Reminder Exchange entry VA-MHV BMI &gt; 25.0

Installing Reminder Exchange entry VA-MHV CERVICAL CANCER SCREEN

Installing Reminder Exchange entry VA-MHV COLORECTAL CANCER SCREEN

Installing Reminder Exchange entry VA-MHV DIABETES FOOT EXAM

Installing Reminder Exchange entry VA-MHV DIABETES RETINAL EXAM

Installing Reminder Exchange entry VA-MHV HYPERTENSION

Installing Reminder Exchange entry VA-MHV INFLUENZA VACCINE

Installing Reminder Exchange entry VA-MHV LDL CONTROL

Installing Reminder Exchange entry VA-MHV MAMMOGRAM SCREENING

Finding RP.MAMMOGRAM UNILAT does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: **MAMMOGRAPHY SCREENING** (RAD  Detailed) CPT:77057

Finding RP.MAMMOGRAM UNILAT does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: **MAMMOGRAPHY SCREENING** (RAD  Detailed) CPT:77057

Installing Reminder Exchange entry VA-MHV PNEUMOVAX

Installing Reminder Exchange entry VA-OEF/OIF MONITOR REPORTING

Installing Reminder Exchange entry VA-PTSD SCREENING

Installing Reminder Exchange entry VA-TBI SCREENING

Installing Reminder Exchange entry PATCH 11 ITEMS

Removing PATCH 11 ITEMS transport reminder.

Removing PATCH 11 DIALOG transport dialog.

Updating Routine file...

Updating KIDS files...

PXRM*2.0*11 Installed.

Oct 07, 2008@05:51:35

Install Message sent #xxxxxxxxxxxxx
Install Completed

## Appendix B: Setting up a TIU/HS Object for the

## AUDIT-C Test

Before using the VA-Alcohol Use Screen reminder, a TIU/HS Object needs to be created to look for the last occurrence of an AUDIT-C test done on a patient. The TIU/HS Object must be named AUDIT-C for the object to work in the reminder dialog.

**NOTE** : For some reason, Health summary doesn’t allow occurrence count or time period for MH tests, so you may need to enter these first, as follows:

The components MHAL and MHAS should have values of 'Y' for both fields #2

- TIME LIMITS APPLICABLE and #4 - MAXIMUM OCCURRENCES APPLICABLE.

You can edit both those fields locally by doing the following:

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: HEALTH SUMMARY COMPONENT//

EDIT WHICH FIELD: ALL// MAXIMUM OCCURRENCES APPLICABLE

THEN EDIT FIELD:

Select HEALTH SUMMARY COMPONENT NAME: MH

1   MHA

2   MHA Administration List

3   MHA Score

4   MHV REMINDERS DETAIL DISPLAY

5   MHV REMINDERS SUMMARY DISPLAY

CHOOSE 1-5: 3  MHA Score

MAXIMUM OCCURRENCES APPLICABLE: Y  yes

You can do this for both MHAL and MHAS components.

**Create TIU/Health Summary Objects**

To create the TIU/Object, use the menu option “Create TIU/Health Summary Objects” under the Manager Document Definition Menu on the TIU Maintenance Menu. An example of how to set this up is provided below. The bolded parts must be exact; the non-bolded parts are site preferences.

Select OPTION NAME: TIU IRM MAINTENANCE MENU     TIU Maintenance Menu     menu

1      TIU Parameters Menu ...

2      Document Definitions (Manager) ...

3      User Class Management ...

4      TIU Template Mgmt Functions ...

5      TIU Alert Tools

7      TIUHL7 Message Manager

Title Mapping Utilities ...

6      Active Title Cleanup Report

Select TIU Maintenance Menu Option: 2  Document Definitions (Manager)

--- Manager Document Definition Menu ---

1      Edit Document Definitions

2      Sort Document Definitions

3      Create Document Definitions

4      Create Objects

5      Create TIU/Health Summary Objects

Select Document Definitions (Manager) Option: 5  Create TIU/Health Summary Objects

TIU Health Summary Object

Jul 30, 2008@12:13:19                      		Page:    1 of    1

TIU Object Name                   Health Summary Type

1    BRADEN SCALE 30D                  VA-BRADEN SCALE 30D

2    PRESSURE ULCER                    VA-PRESSURE ULCER

3    PU INTERVENTIONS                  VA-PU INTERVENTIONS

4    TIU TPBN FUTURE APPTS             TIU TPBN FUTURE APPTS

Create New TIU Object                   Find

Detailed Display/Edit TIU Object        Detailed Display/Edit HS Object

Quit Select Action: Quit// CRE   Create New TIU Object

--- Create TIU/Health Summary Object ---

Enter a New TIU OBJECT NAME: **AUDIT-C** this must be exact.

Object Name: AUDIT-C

Is this correct? YES// **&lt;Enter&gt;**

Use a pre-existing Health Summary Object? NO// **&lt;Enter&gt;**

Checking AUDIT-C (TIU) with Health Summary...

Creating Health Summary Object 'AUDIT-C (TIU)'

Select Health Summary Type: **AUDC**

Are you adding 'OB AUDC' as

a new HEALTH SUMMARY TYPE (the 181th)?   No// **YES**

NAME:  AUDC// **&lt;Enter&gt;**

TITLE: AUDC

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **&lt;Enter&gt;**

SUPPRESS SENSITIVE PRINT DATA: **&lt;Enter&gt;**

LOCK: **&lt;Enter&gt;**

OWNER: // **&lt;Enter&gt;**

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// **NO**

Select COMPONENT: **MHAS** MHA Score        MHAS

SUMMARY ORDER: 5// **5**

OCCURRENCE LIMIT: **1**

HEADER NAME: MHA Score// **&lt;Enter&gt;**

No selection items chosen.

Select new items one at a time in the sequence you want them displayed.

You may select up to 99 items.

Select SELECTION ITEM: **AUDC**

Searching for a MH TESTS AND SURVEYS, (pointed-to by SELECTION ITEM)

Searching for a MH TESTS AND SURVEYS

1   AUDC

2   AUDCR

CHOOSE 1-2: **1** AUDC

Select SELECTION ITEM: **&lt;Enter&gt;**

Select COMPONENT: **&lt;Enter&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;Enter&gt;**

Please hold on while I resequence the summary order.

Do you want to overwrite the TIME LIMITS in the Health

Summary Type ' AUDC'?  N// **&lt;Enter&gt;** O

Print standard Health Summary Header with the Object?  N// **&lt;Enter&gt;** O

Partial Header:

Print Report Date?  N// O

Print Confidentiality Banner?  N// O

Print Report Header?  N// O

Print the standard Component Header?  Y// ES

Use report time/occurence limits?  N// O

Underline Component Header?  N// O

Add a Blank Line after the Component Header?  N// **&lt;Enter&gt;** O

Print the date a patient was deceased?  N// **&lt;Enter&gt;** O

Print a LABEL before the Health Summary Object?  N// **&lt;Enter&gt;** O

Suppress Components without Data?  N// **&lt;Enter&gt;** O

OBJECT DESCRIPTION:

No existing text

Edit? NO// **&lt;Enter&gt;**

Create a TIU Object named: AUDIT-C

Ok? YES// **&lt;Enter&gt;**

TIU Object created successfully.

Enter RETURN to continue...

## Appendix C: Computed Finding Descriptions

The following are new or modified computed findings distributed by PXRM*2*11:

**NAME: VA-AGENT ORANGE EXPOSURE          ROUTINE: PXRMMSER**

ENTRY POINT: AORANGE                  PRINT NAME: VA-Agent  Exposure

TYPE: MULTIPLE

DESCRIPTION:  This computed finding will be true if the patient has an agent

orange exposure registration date in the date range specified by Beginning

Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**NAME: VA-COMBAT SERVICE                 ROUTINE: PXRMMSER**

ENTRY POINT: COMBAT                   PRINT NAME: VA-Combat Service

TYPE: MULTIPLE

DESCRIPTION:   This computed finding will be true if combat service is found

in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**NAME: VA-COMBAT VET ELIGIBILITY         ROUTINE: PXRMMSER**

ENTRY POINT: CVELIG                   PRINT NAME: VA-Combat Vet Eligibility

TYPE: MULTIPLE

DESCRIPTION:  This computed finding will be true if the patient qualifies as

a combat vet.

The possible values that can be used in a Condition are: "Eligible",

"Expired", and "Not eligible". An example is:

I V="Not eligible"

If the patient was eligible on the evaluation date then the Value for use in a Condition will be "Eligible". If the patient is not eligible and the

evaluation date is greater than the eligibility end date then the Value is

"Expired", otherwise the value is "Not eligible".

CLASS: NATIONAL

**(** ***modified)*** **NAME: VA-LAST SERVICE SEPARATION DATE   ROUTINE: PXRMMSER**

ENTRY POINT: DISCHDT                  PRINT NAME: Veteran Last Separation Date

TYPE: SINGLE

DESCRIPTION:  This is a single occurrence computed finding that returns the

most recent  Service Separation Date for the veteran as a FileMan date. It can be used as the value in the Condition. For example: I V&gt;3030101.

The computed finding will be true if a separation date is found; otherwise it will be false. If the computed finding is true, the date of the finding will be the most recent Service Separation Date.

CLASS: NATIONAL                       SPONSOR: Office of Quality &amp; Performance

**NAME: VA-OEF SERVICE                    ROUTINE: PXRMMSER**

ENTRY POINT: OEF                      PRINT NAME: VA-OEF Service

TYPE: MULTIPLE

DESCRIPTION:  This multi-occurrence computed finding will search for periods

of OEF service in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**NAME: VA-OIF SERVICE                    ROUTINE: PXRMMSER**

ENTRY POINT: OIF                      PRINT NAME: VA-OIF Service

TYPE: MULTIPLE

DESCRIPTION:  This multi-occurrence computed finding will search for periods

of OIF service in the date range specified by Beginning Date/Time and Ending

Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**NAME: VA-POW                            ROUTINE: PXRMMSER**

ENTRY POINT: POW                      PRINT NAME: VA-POW

TYPE: MULTIPLE

DESCRIPTION:  This computed finding will be true if the patient was a POW in

the date range specified by Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**NAME: VA-PURPLE HEART                   ROUTINE: PXRMMSER**

ENTRY POINT: PHEART                   PRINT NAME: VA-Purple Heart

TYPE: SINGLE

DESCRIPTION:   This computed finding will be true if the patient is a Purple

Heart recipient.

There is no value for use in a Condition.

CLASS: NATIONAL

**NAME: VA-SERVICE BRANCH                 ROUTINE: PXRMMSER**

ENTRY POINT: SBRANCH                  PRINT NAME: VA-Service Branch

TYPE: MULTIPLE

DESCRIPTION:   This computed finding will return service branch information

for a maximum of three service periods in the date range specified by

Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"BRANCH"

"DISCHARGE TYPE"

"ENTRY DATE"

"SEPARATION DATE"

"SERVICE COMPONENT"

The default value is "DISCHARGE TYPE".

CLASS: NATIONAL

**NAME: VA-UNKNOWN OEF/OIF SERVICE        ROUTINE: PXRMMSER**

ENTRY POINT: UNKOEIF                  PRINT NAME: VA-Unknown OEF/OIF Service

TYPE: MULTIPLE

DESCRIPTION:   This multi-occurrence computed finding will search for periods of OEF/OIF service with an unknown location in the date range specified by Beginning Date/Time and Ending Date/Time.

Subscripts that can be used in a Condition are:

"LOCATION"

The default value is "LOCATION".

CLASS: NATIONAL

**(** ***modified)*** **NAME: VA-VETERAN                        ROUTINE: PXRMMSER**

ENTRY POINT: VETERAN                  PRINT NAME: Patient is a Veteran

TYPE: SINGLE

DESCRIPTION:   This single occurrence computed finding is true if the patient is a veteran and false otherwise.

There are no values that can be used in a Condition.

CLASS: NATIONAL