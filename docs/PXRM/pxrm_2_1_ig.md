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
patch: 311
patch_gap: null
section: ''
source_file: pxrm_2_1_ig.docx
status: draft
title: pxrm 2 1 ig.docx
---

<!-- image -->

**Clinical Reminders**

**CPRS: Integration with Women’s Health**

### Patches: PXRM*2.0*1 WV*1.0*16 LR*5.2*311 OR*3.0*210

**INSTALLATION and SETUP GUIDE**

**February 2005**

**Updated March 2005**

##### Health Data Systems

**V** *IST* **A** HSD&amp;D

##### Department of Veterans Affairs

**Revision History**

| **Date**        |   **Page #** | **Description**                                                                                                                                                                                                    |
|-----------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| March 25,  2005 |           15 | Modified step 9, to remove printing to a printer. Added the following text:  “Do not queue the installation. Because the installation contains questions requiring responses, queuing will stop the installation.” |

**Table of Contents**

Introduction	1

**Table of Contents**

Overview of the WH Reminders Project	1

Description of patches in build	2

Impact on Sites	4

Purpose of This Guide	6

Our Target Audience	6

Other Sources of Information	6

This Manual and Related Documentation	6

Pre-Installation Information	7

Minimum Required Packages	7

Installation Time Estimates	7

Files Required to Run the WH Reminders application	8

Files installed	8

Pre and Post-Install Routines Installed	8

Routines Installed	9

Routine Mapping	9

Pre-Install Worksheet	10

Installation	12

Test Site info	12

Installation Instructions	13

Task 1: Download WH\_CPRS\_INTEGRATION Software	13

Task 2: Load the KIDS Distribution File	14

Task 3: Install WH\_CPRS\_INTEGRATION	14

Post-Installation Procedures	16

Setup Guide	20

Setup Overview	20

1. Set up Women’s Health Package	22
2. Map local findings to the national Reminder Terms.	37
3. Run the Reminder Test option after term definition mapping is completed	47
4. Use the Reminder Dialog options to edit the national (exported) dialogs.	48
5. Verify that the reminders function properly	52
6. Add the nationally distributed reminders to the CPRS Cover Sheet	54
7. Set up entries in the WV Notification Purpose file	56
8. Determine how and where letters will be printed.	56
9. Verify that the dialogs function properly	57
10. Activate alerts	61

Appendix A: KIDS Installation Example	62

Appendix B: Key Points to WH Reminders Installation and Setup	68

Appendix C: Reminders Installation with Reminder Exchange Utility	70

#### Appendix D: WV*1*16 Description	72

#### Appendix E: Setting up Notification Letters	80

#### Appendix F: Local Dialog Modification to Trigger Order Menu	91

#### Appendix G: How to customize WH reminders and dialogs after installation	93

#### Index	98

| **Overview of the WH Reminders Project**  This WH Reminders project provides a combined build consisting of the following Install(s):  WV*1.0*16 LR*5.2*311 OR*3.0*210 PXRM*2.0*1   | **Background to “CPRS: Integration with Women’s Health” Project**  The CPRS: Integration with Women’s Health project has been designed to fulfill the following VHA policy.  “It is VHA policy to provide a nationwide tracking system to ensure that consistent mammography and cervical screening follow-up is achieved and that patients have been properly notified of the test results.”  To meet the data requirements of this policy, the Women’s Health software was developed (Indian Health Service software was modified to be consistent with VA policy and VistA architecture). However, none of the information contained within the WH software interfaces with CPRS.  Therefore, it is the goal of the Women’s Veterans Health Program to enable CPRS, in its existing Clinical Reminders package, to interface with the Women’s Health VistA package. CPRS: Integration with Women’s Health (referred to in this manual as WH Reminders) accomplishes this goal.  **Benefits:**  - Enables capture of a greater percentage of data than is currently entered into the Women’s Health VistA package. - Eliminates the duplication of entering the identical data into both systems, while still allowing the Women’s Health package to perform its tracking and notification functions. - Significantly reduces discrepancies between WH data and data collected by Clinical Reminders. - Results in a signed progress note documenting the WH Mammogram and Pap Smear-related care and patient notifications.  The data captured will be used to automatically update the Women’s Health package, which allows continuation of Women’s Health Software reporting functionality.  The Mammogram Screening reminder replaces the following national reminders relating to mammograms and breast cancer screening:  VA-*BREAST CANCER SCREEN - rescinded 12/15/2003  VA-MAMMOGRAM - rescinded 12/15/2003  The Pap Screening reminder replaces the following national reminders relating to PAP smears and cervical cancer screening:  VA-*CERVICAL CANCER SCREEN VA-PAP SMEAR   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Description of patches in build

###### CPRS: Integration with Women’s Health is distributed in a combined build that consists of the following patches: PXRM*2.0*1, WV*1.0*16, LR*5.2*311, and OR*3.0*210.

**PXRM*2.0*1** adds four new reminders and dialogs, several new/revised taxonomies, and many new reminder terms, health factors, and computed findings to support the CPRS Integration with Women’s Health project. There are also several new entries for the WV NOTIFICATION PURPOSE file that need to be installed so references to these notifications can be resolved during reminder installation.

The patch installation takes advantage of the reminder exchange utility and installs the reminders into the host system “silently.” During reminder installation, you may be prompted for orders – you will need to substitute your local quick orders. See the table in the setup section for quick orders that are needed.

**WV*1.0*16**

This patch adds functionality that allows the Women's Health (WH) package to send data to the Clinical Reminders (CR) package to resolve Mammogram and Pap Smear reminders. Also, the CR package will be able to send data to the WH package to update the WH database.

Patch 16 introduces a new option, Link Pap Smear with SNOMED Codes [WV PAP SMEAR SNOMED CODES], which is added to the File Maintenance Menu, and also modifies several options: Edit Site Parameters [WV EDIT SITE PARAMETERS] option adds two new prompts: Update Result/Dx Field? and Update Treatment Needs? The Add/Edit a Notification Purpose &amp; Letter [WV ADD/EDIT NOT PURPOSE&amp;LETTER] option is modified to add four new prompts.

See Appendix D for complete details about the changes introduced by Patch 16.

| NOTE: All alerts are exported in a disabled state; sites will need to go into the CPRS Manager Menu (CPRS Configuration (Clin Coord)/Notification Mgmt Menu) to enable these alerts – at a system, site, location, or individual level.   | **Description of patches in build, cont’d**  **LR*5.2*311**  1. Currently the ADD^LRWOMEN utility notifies a Women's Health package utility whenever a Cytology or Surgical Pathology report is verified for a female patient. This functionality was provided with LR*5.2*231.  After installation of patch LR*5.2*311, the ADD^LRWOMEN utility will also notify a new CPRS utility (LAB^ORB3LAB) for all patients, not just female patients. Integration Agreement #4287 grants the LABORATORY package permission to call the ORB3LAB routine.  1. The code in the MOVE entry point of the LRWOMEN routine was replaced with a QUIT command. With the release of LR*5.2*259, this entry point is no longer called. The entry point will be deleted in a future patch.  **OR*3.0*210**  adds three new notification/alerts:  #69 - Mammogram Results #70 - Pap Smear Results  #71 - Anatomic Pathology Results  All three alerts are informational (no follow-up action). Alerts 69 and 70 are sent to providers and/or designated recipients when radiology and lab results are available. Alert 71 (Anatomic Pathology Results) will be sent to the practitioner requesting the AP procedure if that user has the notification/alert enabled (turned on). Alerts 69 and 70 are triggered within the Women's Health package and are intended to support that package. Alert 71 is triggered within the Lab package.  These notification/alerts are exported with a deletion parameter value of “Individual Recipient.” This means the alert will be deleted for each recipient individually.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| These steps are described in more detail in the Setup section of this manual   | **Impact on Sites**  - **Setup and implementation by local team**  The following steps are required after the reminders have been installed on the system:  1. Sites will need to determine if the review reminders should be released to the field. If a site is not set up for automatic update of WH, these reminders will not come due, so releasing the review reminders and dialogs might be confusing.  The VA-WH PAP SMEAR REVIEW RESULTS reminder  will only come due if all of the following are true:  - PAP smear results are recorded and verified in VistA Lab package - VistA Lab package uses SNOMED codes - WH package has SNOMED codes mapped to the codes used by the VistA Lab package - WH parameters are set up to automatically receive VistA Lab results when the PAP smear procedure is verified and released  The VA-WH MAMMOGRAM REVIEW RESULTS reminder  will only come due if all of the following are true:  - Mammogram results are recorded and verified in VistA Radiology package - WH parameters are set up to automatically receive VistA Radiology results when the mammogram procedure is verified and released, and status of received mammogram result is set to OPEN   |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| These steps are described in more detail in the Setup section of this manual.  **TIP:**  We strongly  		recommend that you complete the  Pre-Installation Worksheet on Page 12 before installing the software.   | **Impact on Sites**  - **Setup and implementation by local team, cont’d**  1. Clinicians and CPRS/Reminder CACs will need to be informed about the new reminders and dialogs, the procedure clinical interpretation updates, and new patient notification tracking features. 2. Reminder CACs will need to map certain national Reminder Terms to identify local processing for documenting Pap Smears and Mammograms in PCE. 3. Reminder CACs will need to create quick orders for PAP smears and Mammograms, if needed. If these orders are created prior to reminder installation, sites will be able to associate their local orders with the dialogs at the time of installation. If the orders are not created before, sites will have to edit the reminder dialogs after installation to add references to local orders. 4. The Women’s Health Case Manager will need to understand the impact on WH files and the impact on the case manager’s normal work processing due to WH data entered from the CPRS GUI. This project updates some data in the WH package, not all of it. A case manager will be required to set up parameters and to monitor printing of notifications. 5. Reminder CACs and Women’s Health Case Managers will need to agree on notification methods, printers, etc., and set these up, as needed.  See the Pre-Installation Worksheet on Page 12; this should be completed before installing the combined build for this project.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Purpose of This Guide**        | This Installation and Setup Guide is designed to help you prepare your site for the installation and implementation of the Women’s Health Reminders. It includes detailed information such as system requirements, installation time estimates and instructions, and procedures that will get you up and running with this project.  **Our Target Audience**  We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:  - Information Resources Management (IRM) - Clinical Application Coordinator (CAC) - Enterprise **V** *IST* **A** Support (EVS) - Software Quality Assurance (SQA)  **Documentation Retrieval**  Your site can retrieve the Clinical Reminders V. 2.1 documentation from the Anonymous directories. The preferred method is to “FTP” the files from  [**download.vista.med.va.gov**](ftp://ftp.fo-slc.med.va.gov/)  . This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. Use binary mode.  **Note:**  If you prefer, you can retrieve the software  *directly*  from one of the FTP Servers, listed below, under the FTP Address column.   |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Other Sources of Information** | You can also retrieve documentation from the following websites:  [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders)  Clinical Reminders Main Web page.  [http://www.va.gov/vdl](http://www.va.gov/vdl)  the  **V**  *IST*  **A**  Documentation Library (VDL).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**FTP Addresses Available for Downloading Clinical Reminders Documentation**

| **OI Field Office**   | **FTP Address**   | **Directory**   |
|-----------------------|-------------------|-----------------|
| Albany                | REDACTED          | REDACTED        |
| Hines                 | REDACTED          | REDACTED        |
| Salt Lake City        | REDACTED          | REDACTED        |

<!-- image -->

## Pre-Installation Information

| **Minimum Required Packages**   | Before installing the WH Reminders build, make sure that your system includes the following software packages and versions (those listed or higher).   |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|

**Minimum Required Packages and Versions**

| **Package**                             | **Namespace**   |   **MINIMUM VERSION NEEDED** | **Required Patches**                           |
|-----------------------------------------|-----------------|------------------------------|------------------------------------------------|
| **Clinical Reminders**                  | PXRM            |                          2   | PXRM*1.5*12                                    |
| **CPT**                                 | ICPT            |                          6   |                                                |
| **HL7**                                 | HL              |                          1.6 |                                                |
| **ICD**                                 | ICD             |                         18   |                                                |
| **Kernel**                              |                 |                          8   |                                                |
| **Lexicon**                             | LEX             |                          2   |                                                |
| **MailMan**                             | XM              |                          8   | XM*8.0*16 –  Mailman/HL7 Messaging  XM*DBA*154 |
| **Order Entry**  **/Results Reporting** | OR              |                          3   | OR*3.0*195                                     |
| **Radiology/Nuclear Medicine**          | RA              |                          5   |                                                |
| **Text Integration Utilities**          | TIU             |                          1   | TIU*1.0*112  TIU*1.0*113                       |
| **VA FileMan**                          | DI              |                         22   |                                                |

| **Installation Time Estimates**  NOTE: You should  		install and test the CPRS-WH combined  build in your test accounts  ***before***  installing in your production accounts.   | On average, it takes approximately fifteen minutes to install PXRM V. 2.0*1 and the combined build. This estimate was provided by a few of our beta test sites. Actual times may vary, depending on how your site is using its system resources.  Suggested time to install: non-peak requirement hours. During the install process, Clinical Reminders users should not be accessing the Software.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Files Required to Run the WH Reminders application**   | **Files installed**  790.02	WV SITE PARAMETER  790.1	WV PROCEDURE  790.2	WV PROCEDURE TYPE  790.404 WV NOTIFICATION PURPOSE  100.9	OE/RR NOTIFICATIONS  1. REMINDER DIALOG 2. REMINDER GUI PROCESS  801.45	REMINDER FINDING TYPE PARAMETER  811.8	REMINDER EXCHANGE FILE  Note: You can learn more about these files by generating a list with file attributes using VA FileMan.  **Pre and Post-Install Routines Installed**  PXRMCWH PXRMWHPI PXRMWHEV  PXRMWHPI has both the pre and post-install calls: PRE-INIT ROUTINE : PRE^PXRMWHPI  POST-INIT ROUTINE : POST^PXRMWHPI   |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Routines Installed**   | **Note:**  You can use the  *Kernel First Line Routine Print*  [XU FIRST LINE PRINT] option to print a list containing the first line of each PXRM routine.  **Routine Mapping**  At this time, we do  *not*  offer any recommendations for routine mapping. However, if you choose to map the Clinical Reminders V.  2.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory.   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Pre-Install Worksheet

During the installation of the combined build, you will be prompted for many Order Dialog names, since these can’t be installed via KIDS. To make this easier, we recommend that you complete the worksheet below prior to the install. Fill in the blanks with Order Dialog names – either ones that already exist at your site, or placeholders until you can create appropriate order dialog elements. Coordination among ADPACs, CACs, and representatives from Radiology, Women’s Health, and Clinical Reminders will help facilitate this.

Suggestion: You may want to create one dummy quick order, use it for every quick order prompt during the installation, and then replace the dummy orders with actual quick orders later.

The WV Notification Purpose file should be installed before the reminders (i.e., so the dialogs can find the entries they need at load time.

Example prompt

Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME

.

.

Q.WH BREAST ULTRASOUND - UNILATERAL does not exist.

ADDITIONAL FINDING entry

Installing reminder VA-WH MAMMOGRAM REVIEW RESULTS

**Pre-Install Worksheet**

This chart should be used as a worksheet by the CAC **prior** to the installation.

| **Reminder**                            | **Dialog Element**                   | **File Reference for Entry**    | **Your dialog entry**                                    |
|-----------------------------------------|--------------------------------------|---------------------------------|----------------------------------------------------------|
| **VA-WH MAMMOGRAM**  **REVIEW RESULTS** | Q.WH BREAST ULTRASOUND- UNILATERAL   | Quick Order in Order file #100  |                                                          |
|                                         | Q.WH BREAST ULTRASOUND - BILATERAL   | Order file #100                 |                                                          |
|                                         | Q.WH MAMMOGRAM -  UNILATERAL         | Order file #100                 |                                                          |
|                                         | Q.WH MAMMOGRAM -  BILATERAL          | Order file #100                 |                                                          |
| **VA-WH MAMMOGRAM**  **SCREENING**      | RP.MAMMOGRAM BILAT                   | Rad/Nuc Med Procedure file #71  |                                                          |
|                                         | RP.MAMMOGRAM BILAT  SCREEN           | Rad/Nuc Med  Procedure file #71 |                                                          |
|                                         | RP.MAMMOGRAM UNILAT                  | Rad/Nuc Med Procedure file #71  |                                                          |
|                                         | RP.MAMMOGRAM BILAT                   | Rad/Nuc Med  Procedure file #71 |                                                          |
|                                         | RP.MAMMOGRAM UNILAT                  | Rad/Nuc Med  Procedure file #71 |                                                          |
|                                         | Q.WH REFER TO WOMEN'S HEALTH CLINIC  | Order file #100                 |                                                          |
|                                         | Q.WH MAMMOGRAM -  UNILATERAL         | Order file #100                 |                                                          |
|                                         | Q.WH MAMMOGRAM - BILATERAL           | Order file #100                 |                                                          |
|                                         | Q.WH MAMMOGRAM –  BILATERAL  SCREEN  | Order file #100                 |                                                          |
| **VA-WH PAP SMEAR REVIEW RESULTS**      | Q.WH CERVICAL ORDERS                 | Order file #100                 |                                                          |
|                                         | Q.WH PAP SMEAR REPEAT CONSULT        | Order file #100                 | **Consult – repeat PAP smear**  **Consult – colposcopy** |
| **VA-WH PAP SMEAR SCREENING**           | Q.WH REFER TO WOMEN'S  HEALTH CLINIC | Order file #100                 |                                                          |

**Installation Order:**

Install the software in this order:

PXRM*1.5*12	CR Index Global

PXRM*2.0	Clinical Reminders v2.0 WV\_PXRM\_CPRS\_INTEGRATION.KID	Combined build

This Global Transport contains patches: WV*1.0*16

LR*5.2*311 OR*3.0*210 PXRM*2.0*1

***The install needs to be done by a person with DUZ(0) set to "@."***

| **Installation Instructions**  **IMPORTANT:**  You should install and test Clinical Reminders 2.0..1 in your test accounts  ***before***  installing in your production accounts.   | Perform the steps that follow to download the combined build, WV\_PXRM\_CPRS\_INTEGRATION.KID from an FTP Server. Then you will be ready to use this section for loading the Kernel Installation &amp; Distribution System (KIDS) Distribution file, and for installing PXRM V. 2.0 on to the VISTA Server.  **Task 1: Download WV\_PXRM\_CPRS\_INTEGRATION Software**  **1.**  Download the Host File WV\_PXRM\_CPRS\_INTEGRATION.KID from an FTP Server using an address listed in the table below.  The preferred method is to “FTP” the files from REDACTED  . This location automatically transmits files from the  *first*  available FTP Server. (See the order listed below under the FTP Address column).  - .EXE or .PDF files need to be FTP in BINARY. - KIDS Build needs to be FTP in ASCII.  **Note:**  If you prefer, you can retrieve the software  *directly*  from one of the FTP Servers, listed below, under the FTP Address column.  **2.**  Move the files to the appropriate directory on your system.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: FTP Addresses Available for Downloading WV\_PXRM\_CPRS\_INTEGRATION.KID Software**

| **OI Field Office**   | **FTP Address**   | **Directory**   |
|-----------------------|-------------------|-----------------|
| Albany                | REDACTED          | REDACTED        |
| Hines                 | REDACTED          | REDACTED        |
| Salt Lake City        | REDACTED          | REDACTED        |

| **V**  *IST*  **A Server Installation Instructions (cont.)**  Suggested time to install: non-peak requirement hours.   | **Task 2: Load the KIDS Distribution File**  Perform the steps listed below to load the KIDS Distribution file.  1. Sign in to the UCI where the KIDS Distribution file will be loaded and PXRM V. 2.0*1 will be installed. 2. At the “Select OPTION NAME:” prompt, type **XPD MAIN** , and then press **ENTER** . 3. At the “Select Kernel Installation &amp; Distribution System Option:” prompt, type **INSTALL** ation, and then press **ENTER** . 4. At the “Select Installation Option:” prompt, type **Load a Distribution,** and then press **ENTER** to prepare for loading the KIDS Distribution file. 5. At the “Enter a Host File:” prompt, type **the directory where you have stored the Host File** , followed by **WV\_PXRM\_CPRS\_INTEGRATION.KID** . Then press **ENTER** . 6. At the “Want to Continue with Load YES//?” prompt, press  **ENTER**  . The system then loads the file to this location.  **Task 3: Install WV\_PXRM\_CPRS\_INTEGRATION**  During the install process, Clinical Reminders users should not be accessing the software.  1. Request that all Clinical Reminders users log off CPRS. 2. Review mapped sets for PXRM* namespaces. 3. If the routines are mapped, remove them from the mapped set at this time. 4. Back up your system. This step is optional, but recommended. 5. At the “Select INSTALL NAME:” prompt, type WV*1.0*16 and then press enter to install the combined build.   |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Installation Instructions (cont.)**  **NOTE:**  **Do NOT queue the installation!**  **Because this installation contains questions requiring responses, queuing will stop the installation.**   | **Task 3: Install WV\_PXRM\_CPRS\_INTEGRATION (cont.)**  1. At the “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” prompt, type NO, and then press enter.  1. At the “Want KIDS to INHIBIT LOGONs during the install? YES//” prompt, type NO, and then press enter.  1. At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” prompt, type YES.  When asked what options to put out of order, respond with: GMTS*  PXRM*  IBDF PRINT*  OR CPRS GUI CHART  ORS HEALTH SUMMARY  When asked what protocols to place out of order, respond with: ORS AD HOC HEALTH SUMMARY  ORS HEALTH SUMMARY  PXRM PATIENT DATA CHANGE  1. At the “DEVICE:” prompt, press enter to use the default device HOME (the screen) for printing the Installation message.  10 If routines were unmapped as part of the installation process, return them to the mapped set once the installation of PXRM* 2.0*1 is completed.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Select Reminder Managers Menu Option: **RM** Reminder Definition Management

1. **Verify correct installation of the packed reminders** .

RL	List Reminder Definitions

You cannot make changes to these National reminders. You may copy the national reminder to a local reminder definition name and make any changes necessary.

RI	Inquire about Reminder Definition RE	Add/Edit Reminder Definition

The post-install routine, POST^PXRMWHP, installs the packed reminders into your Exchange File. If you discover that the reminders didn’t get installed, you can use the Reminders Exchange options on the Reminders Manager Menu to install the “packed” reminders. See Appendix C for an example of installing via Exchange.

RC	Copy Reminder Definition

RA	Activate/Inactivate Reminders

1. Using *Inquire about Reminder Definition* on the Reminder Management Menu, ensure that the four reminder definitions have been installed. Review the reminders to become familiar with the definitions and terms.

Select Reminder Definition Management Option: **RI** Inquire about Reminder Definition

Select Reminder Definition: **VA-WH**

###### 1 NOTE See Appendix C for an example of installing missing reminders or dialogs through Reminders Exchange

1. Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:

**Mammogram Terms**

1. VA-TERMINAL CANCER PATIENT
2. VA-WH BILATERAL MASTECTOMY
3. VA-WH BREAST CARE ORDER HEALTH FACTOR
4. VA-WH HX BREAST CANCER/ABNORMAL MAM
5. VA-WH MAMMOGRAM ORDER
6. VA-WH MAMMOGRAM PENDING REVIEW
7. VA-WH MAMMOGRAM SCREEN DEFER
8. VA-WH MAMMOGRAM SCREEN DONE
9. VA-WH MAMMOGRAM SCREEN FREQ - 1Y
10. VA-WH MAMMOGRAM SCREEN FREQ - 2Y
11. VA-WH MAMMOGRAM SCREEN FREQ - 4M
12. VA-WH MAMMOGRAM SCREEN FREQ - 6M
13. VA-WH MAMMOGRAM SCREEN IN RAD PKG
14. VA-WH MAMMOGRAM SCREEN IN WH PKG
15. VA-WH MAMMOGRAM SCREEN NOT INDICATED
16. VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG

#### Pap Smear Terms

1. VA-WH HX CERVICAL CANCER/ABNORMAL PAP
2. VA-WH HYSTERECTOMY
3. VA-WH PAP SMEAR DONE
4. VA-WH PAP SMEAR OBTAINED
5. VA-WH PAP SMEAR ORDER
6. VA-WH PAP SMEAR ORDER HEALTH FACTOR
7. VA-WH PAP SMEAR PENDING REVIEW
8. VA-WH PAP SMEAR SCREEN DEFER
9. VA-WH PAP SMEAR SCREEN FREQ - 1Y
10. VA-WH PAP SMEAR SCREEN FREQ - 2Y
11. VA-WH PAP SMEAR SCREEN FREQ - 3Y
12. VA-WH PAP SMEAR SCREEN FREQ - 4M
13. VA-WH PAP SMEAR SCREEN FREQ - 6M
14. VA-WH PAP SMEAR SCREEN IN LAB PKG
15. VA-WH PAP SMEAR SCREEN IN WH PKG
16. VA-WH PAP SMEAR SCREEN NOT INDICATED

#### VA FileMan Print from the Reminder Term File

###### You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **c. (cont’d) Verify that the WH dialogs are installed on your system.**  **NOTE**  : Do not autogenerate dialogs for the reminders. Dialogs are included with the packed reminder installation.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dialog List**  Jan 23, 2004@09:59:11	Page:	12 of	13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  +Item Reminder Dialog Name	Source Reminder	Status  1. VA-WH MAMMOGRAM REVIEW RESULTS	VA-WH MAMMOGRAM REVIEW RE Linked 2. VA-WH MAMMOGRAM SCREENING	VA-WH MAMMOGRAM SCREENING Linked 3. VA-WH PAP SMEAR REVIEW RESULTS	VA-WH PAP SMEAR REVIEW RE Linked 4. VA-WH PAP SMEAR SCREENING	VA-WH PAP SMEAR SCREENING Linked 5. VA-WV TEST ORDERS	ZZ-WH ABNORMAL PAP SMEAR 6. VIAGRA (SILDENAFIL) INITIATION	Test	Linked 7. WPBTEST	WPBTEST Disabled |                                                                                                                                                                                                    |
| **+	Enter ?? for more actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                    |
| Find Next ‘VA WH’? Yes//  **no**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                    |

| **Setup Overview**   | **Project Goals**  - Enable CPRS GUI to interface with the Women’s Health (WH) VistA package  - Update Pap Smear and Mammogram screening reminders  - Provide review reminders that store clinical review results in the WH package.  Review reminders will only work if the data automatically updates WH from the Lab and Radiology package (requires setup in WH package). Procedures entered manually into WH will not make the review reminders due.  - Provide dialogs for the screening and review reminders clinicians can use to document PAP &amp; mammogram procedures  The VA-WH reminders have been developed to interface with the Women’s Health package. The associated reminder dialogs will update the WH package at the same time that clinical care is recorded in CPRS GUI, thus eliminating the need for dual data entry.   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

###### February 2005	CPRS: Integration with Women’s Health Installation Guide	20

| **Women’s Health Package**  **NOTE:**  Your site can choose whether to include the Print Now checkbox on review reminder dialogs. This can be set with a new option on the CPRS Reminder Configuration menu: PXRM WH PRINT NOW  The default will be not to display the Print Now checkbox.   | **Overview of Women’s Health Package**  *Patient Management*  - manage individual patient care  - Maintain date of the next procedure (PAP smear &amp; mammogram) - Track the patient's individual procedures: the date performed, the provider and clinic, the results or diagnosis - Track notifications (letters, in person, phone calls) - Maintain a file of form letters that may be edited and personalized for a clinic's particular needs - Queue reminder letters months in advance of a future appointment, print and mail shortly before the tentative appointment  *Manager’s Functions*  - provide the ADPAC with a set of utilities for configuring the software to the specific needs of the site  - Maintain site-specific parameters - Maintain the text of form letters and notifications - Print notification letters - Determine how and when letters get printed - Map SNOMED codes to those SNOMED codes used by the VistA Lab package for PAP smear procedures  *Print Now versus Queue to Print during next Batch Run*  – Default is to print during next batch run in WH unless Print Now is selected.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 1. **Set up Women’s Health Package**  In order for reminders to interface with the Women's Health (WH) package, the WH package must be installed and maintained. Specific features of WH that must be in place in order for these reminders to work as designed include the following:  On the File Maintenance Menu [WV MENU-FILE MAINTENANCE]:  1. Add at least one case manager ( **Required** ) Option: *Add/Edit Case Managers* 2. Add your facility ( **Required** ) 3. Identify the default case manager. This person is someone you added via the Add/Edit Case Manager option (#1) ( **Required** ) 4. If you are going to really use the WH package, answer the other prompts on page 1 also. You must reply “yes” to both ‘Update Result/Dx Field?’ and ‘Update Treatment Needs?’ prompts. This will allow the Reminder Dialogs to update the WH package. 5. On page 2, answer 'Yes' to the 'Import Mammograms from Radiology' and 'Import Tests from Laboratory’ prompts. This turns on the link to the radiology/NM and Lab packages. You also need to set ‘Status Given to Imported Mammograms’ to “OPEN.” (See note below) This ensures that you get results at least for veterans. ( **Required** )  Option:  *Edit Site Parameters*  (Required)  1. Add the Morphology and Topography codes that your Lab uses to result pap smears.  Option:  *Link Pap Smear with SNOMED Codes*  (  **Required**  )  1. Create and customize the letters you want to send to your patients ( **Optional** )  Option:  *Add/Edit a Notification Purpose &amp; Letter*  **Note**  : A mammogram procedure in the WH package with the status of “Open” will cause the MAMMOGRAM REVIEW reminder to be due. This will prompt the clinician to review the results and document them in a progress note. If the status is set to “Closed” when the results are entered into the WH package, the MAMMO- GRAM REVIEW reminder will not be due. Note that the WH mammogram review reminder will not be due if the WH package is set up to assign a diagnostic code to a mammogram as it is loaded from Radiology. The WH package sees a procedure as “Pending” review (which triggers the review reminder) if the status is OPEN and the Result/Diagnosis field is blank.  If Result/Diagnosis is filled in when the mammogram is loaded into WH, then WH thinks it has been reviewed and won’t send Reminders the “Pending” status.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NOTE: If your site doesn’t use the Women’s Health package:**  Only the screening reminders can be used; you won’t be able to use the review reminders.                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| The WH package should be installed and WH SNOMED codes should be mapped to SNOMED codes used by the VistA Lab package to represent PAP smear results. This is required for the new Lab computed finding to resolve the VA-WH PAP SMEAR SCREENING  reminder.  NOTE: Lab entries must have SNOMED codes entered in the TOPOGRAPHY multiple for the WH code to process correctly and receive an alert. If SNOMED codes are not entered in the TOPOGRAPHY multiple, WH will process the lab entry the old way by sending a MailMan message to the WH user - no CPRS alert is sent. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| **WH Package Setup, cont’d**   | **Alternate Setup**  For sites who would like to use the Notification functionality and receive alerts without actively using the WH package, the following actions need to take place:  - Have the WH package activated and populated with women veterans. - Assign a phony name for the WH Coordinator - Set the parameters in the WH package as in the example below.  By taking this action, the “Next Need” field doesn’t get set, but the notification letter is still sent to be printed at the location identified under “Print Now.” If “Print Now” is not selected, the letter is sent to the WH queue for printing and the progress note indicates the letter was sent to the WH package for printing.  To receive “Alerts” – Based on the changes made in the parameters set above, the results will be sent to the phony name created and to the “Provider” requesting the result.   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: To receive alerts without using the WH package**

* * *	EDIT SITE PARAMETERS FOR ………….. HCS	* * *

Default Case Manager: **WHPROVIDER,THREE**

Ask Case Manager: **NO**

Autoqueue Normal PAP Letters: **NO**

PAP Result Normal Letter: Autoqueue Normal MAM Letters: **NO**

MAM Result Normal Letter: Default #days to print letter:

Update Result/Dx Field?: **NO**

Update Treatment Needs?: **NO**

RADIOLOGY:		Import Mammograms from Radiology: **YES** Status Given to Imported Mammograms: **OPEN** Include ALL Non-Veterans(Y/N)?: **YES**

ELIGIBILITY CODE(S):

LABORATORY: Import Tests from Laboratory: **YES**

Include ALL Non-Veterans(Y/N)?: **YES**

ELIGIBILITY CODE(S):

| **Women’s Health Setup, cont’d**   | **Women’s Health File Maintenance Menu**  Options used to set up parameters related to the CPRS/Reminders integration are highlighted in yellow.   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Women’s Health File Maintenance Menu**

| **Women’s Health Setup, cont’d**   | **1a. Edit Site Parameters**  The highlighted fields are required for Review Reminders   |
|------------------------------------|------------------------------------------------------------------------------------------|

**ESP	Edit Site Parameters**

| * * *	EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS	* * *                                                                                                                                                                                                                                                                                                                                                                                  |                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Default Case Manager:  **CRPROVIDER,TWO**                                                                                                                                                                                                                                                                                                                                                                                                |                                  |
| Ask Case Manager:  **YES**                                                                                                                                                                                                                                                                                                                                                                                                               |                                  |
| Autoqueue Normal PAP Letters: NO                                                                                                                                                                                                                                                                                                                                                                                                         | Autoqueue Normal PAP Letters: NO |
| PAP Result Normal Letter:  **PAP result NEM, next PAP 3Y**                                                                                                                                                                                                                                                                                                                                                                               |                                  |
| Autoqueue Normal MAM Letters: NO                                                                                                                                                                                                                                                                                                                                                                                                         | Autoqueue Normal MAM Letters: NO |
| MAM Result Normal Letter:  **MAM result NEM, next MAM 2Y**                                                                                                                                                                                                                                                                                                                                                                               |                                  |
| Default #days to print letter:  **30**                                                                                                                                                                                                                                                                                                                                                                                                   |                                  |
| Update Result/Dx Field?:  **YES**                                                                                                                                                                                                                                                                                                                                                                                                        |                                  |
| Update Treatment Needs?:  **YES**                                                                                                                                                                                                                                                                                                                                                                                                        |                                  |
| (PAGE 1 OF 6)                                                                                                                                                                                                                                                                                                                                                                                                                            | (PAGE 1 OF 6)                    |
| COMMAND:	Press &lt;PF1&gt;H for help  * * *	EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS	* * *  RADIOLOGY:	Import Mammograms from Radiology:  **YES**  Status Given to Imported Mammograms:  **OPEN**  Include ALL Non-Veterans(Y/N)?: YES  ELIGIBILITY CODE(S):  LABORATORY: Import Tests from Laboratory:  **YES**  Include ALL Non-Veterans(Y/N)?:  **YES**  ELIGIBILITY CODE(S):  (PAGE 2 OF 6)  COMMAND:	Press &lt;PF1&gt;H for help | Insert                           |

| **Women’s Health Setup, cont’d**  NOTE: After all letter modifications have been made, determine where letters will print and who will be responsible for retrieving and mailing these.   | **1b. Set up Notification Letters**  See Appendix E for an example of all the steps for customizing notification letters.  **Edit Generic Letter in WV Letter File**  The generic letter needs to be customized locally. This is done through file #790.6, WV Letter. Each facility needs to add its local site address and case manager information. Once this is done, you can edit letters for each of the Notification Purposes through the option AEP Add/Edit a Notification Purpose &amp; Letter.  Go into VA FileMan, Enter or Edit File Entries, and select file 790.6. When prompted for letter, enter Generic.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|$P(NAME,",",2)| |$P(NAME,",")|

|COMPLETE ADDRESS|

These fields will be filled in when you print your letters.

|SSN#|

|TODAY|

10&gt;

11&gt;

12&gt;

13&gt;

14&gt;

15&gt;

16&gt;

17&gt;

EDIT Option: List line: 1//	to: 43// 1&gt;|NOWRAP|

2&gt;

3&gt;|CENTER("Women's Health Clinic")| 4&gt;

5&gt;|CENTER(" 7 Your Street")| 6&gt;

7&gt;|CENTER("Your City, ST	77777")|

8&gt;

9&gt;

printed: |NOW|

WHPROVIDER,THREE, LPN

Women's Health Program phone: 666-7777

38&gt;

39&gt;

40&gt;

41&gt;

42&gt;

43&gt;

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: WV LETTER// EDIT WHICH FIELD: ALL//

Select WV LETTER: GENERIC SAMPLE LETTER LETTER: GENERIC SAMPLE LETTER	Replace LETTER TEXT:. . .

. . .

35&gt;

36&gt;

37&gt;

These fields need to be modified.

g. hat

from may

cine

| **Women’s Health Setup, cont’d**                                                                                                                                                                                                                                                                                                                                                                                                                                          | **1b. Notification letter setup, cont’d**  **Edit Generic Letter in WV Letter File, cont’d**   |                                                                        |    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|----|
| 18&gt;  19&gt;	This will be filled in when you  20&gt;	print the letter.  21&gt;- -	- -  22&gt;                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                |                                                                        |    |
| 23&gt;	Dear Ms. &#124;$P(NAME,",",1)&#124;,  24&gt;  25&gt;  The results of your recent Pap smear are something, somethin 26&gt;  This is the body of the letter and should be edited to say w 27&gt; you want for this Purpose of Notification.  28&gt;  29&gt;  It may go on to say: Your next something will be due one year 30&gt;  now.  At that time we will mail you a reminder letter, or you 31&gt; schedule the appointment yourself by calling our Family Medi |                                                                                                | This text is modified through the option Add/Edit Notification letters |    |
| 32&gt;	Clinic at 777-7777 or our Women's Clinic at 777-7777.  33&gt;  34&gt;	Sincerely,  35&gt;  36&gt;  37&gt;	Modify this text in FileMan –  38&gt;	WHProvider, THREE, LPN	#790.6 WV Letter  39&gt;	Women's Health Program  40&gt;	phone: 666-7777  41&gt;  42&gt;  43&gt;	printed: &#124;NOW&#124;  EDIT Option:                                                                                                                                                       |                                                                                                |                                                                        |    |

| **Women’s Health Setup, cont’d**   | **1b. Notification Letter Setup, cont’d Add and Edit Notification Letters**  Each letter (Notification Purpose) needs to be customized locally. The first time you use this option to edit each letter, enter Yes, to load your edited generic sample letter at the following prompt:  Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?  Enter Yes or No: NO//  **Yes**  For subsequent letter-editing, enter No.   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**AEP	Add/Edit a Notification Purpose &amp; Letter Example**

To edit the letter, tab to the “+” sign and press Enter.

| **Women’s Health Setup, cont’d**   | **1b. Notification Letter Setup, cont’d**  **Modify Default Letter Format to Customize for this Notification Purpose, cont’d**   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| **Women’s Health Setup, cont’d**   | **1b. Notification Letter Setup, cont’d**  **New Purposes of Notification (letter types) added with this patch**  Letters for each of these Purposes of Notification need to be customized for local use.  See instructions in Appendix E for adding new Purposes as dialog elements.   |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

CPRS UPDATE PAP TX NEED 4M

CPRS UPDATE PAP TX NEED 6M

CPRS UPDATE PAP TX NEED 3Y CPRS UPDATE PAP TX NEED 2Y CPRS UPDATE PAP TX NEED 1Y CPRS UPDATE MAM TX NEED 1Y CPRS UPDATE MAM TX NEED 2Y CPRS UPDATE MAM TX NEED 6M CPRS UPDATE MAM TX NEED 4M

MAM result NEM, next MAM 1Y MAM result NEM, next MAM 2Y MAM result NEM, next MAM 4M MAM result NEM, next MAM 6M

MAM result abnormal, F/U MAM 4M MAM result abnormal, F/U MAM 6M PAP result NEM, next PAP 1Y

PAP result NEM, next PAP 2Y PAP result NEM, next PAP 3Y PAP result NEM, next PAP 4M PAP result NEM, next PAP 6M

PAP result abnormal, F/U PAP 4M PAP result abnormal, F/U PAP 6M MAM unsatisfactory, need repeat Pap unsatisfactory, need repeat

PAP result NEM, further screening not required MAM result NEM, further screening not required

| **Women’s Health Setup, cont’d**   | **1c**  .  **Link Pap Smear with SNOMED Codes**  NOTE: Your site may use different codes from the Morphology and Topography SNOMED codes listed here.   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|

Select File Maintenance Menu Option: **PAP** Link Pap Smear with SNOMED Codes Select a MORPHOLOGY SNOMED CODE: **?**

Answer with MORPHOLOGY SNOMED CODE Choose from:

UNSATISFACTORY SPECIMEN	If codes other than the ones

ABNORMAL APPEARANCE	listed here appear, link the NEGATIVE FOR MALIGNANT CELLS	appropriate ones to the Pap NO EVIDENCE OF MALIGNANCY	Smear.

SUSPICIOUS FOR MALIGNANT CELLS CERVICAL MUCOUS ARBORIZATION VAGINA, SECRETORY ALTERATION

You may enter a new MORPHOLOGY SNOMED CODE, if you wish Answer with MORPHOLOGY FIELD NAME

Do you want the entire 3609-Entry MORPHOLOGY FIELD List? UNSA??

Answer with 'Yes' or 'No': **N** (No)

Select a MORPHOLOGY SNOMED CODE: **UNSATISFACTORY SPECIMEN** 09010

...OK? Yes// **&lt;Enter&gt;** (Yes)

MORPHOLOGY SNOMED CODE: UNSATISFACTORY SPECIMEN// **&lt;Enter&gt;**

DIAGNOSIS: Unsatisfactory// **&lt;Enter&gt;**

Select a MORPHOLOGY SNOMED CODE: **&lt;Enter&gt;**

Select a TOPOGRAPHY SNOMED CODE: **?**

Answer with TOPOGRAPHY SNOMED CODE

Choose from:	Your site may use different codes from VAGINAL-CERVICAL CYTOLOGIC MATERIAL these. These should only be related to VAGINAL CYTOLOGIC MATERIAL	PAP smears.

CERVICAL CYTOLOGIC MATERIAL

You may enter a new TOPOGRAPHY SNOMED CODE, if you wish Answer with TOPOGRAPHY FIELD NAME

Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? **N** (No)

Select a TOPOGRAPHY SNOMED CODE: **CERVICAL CYTOLOGIC MATERIAL** 8X310

...OK? Yes// **&lt;Enter&gt;** (Yes)

TOPOGRAPHY SNOMED CODE: CERVICAL CYTOLOGIC MATERIAL

// **&lt;Enter&gt;**

Select a TOPOGRAPHY SNOMED CODE: **&lt;Enter&gt;**

| **Women’s Health Setup, cont’d**   | **Women’s Health Patient Management Menu**   |
|------------------------------------|----------------------------------------------|

WOMEN'S HEALTH:	*	PATIENT MANAGEMENT MENU	*	SALT LAKE CITY HCS

PC	Edit/Print Patient Case Data

PP	Patient Profile	You can manually add a

FS    Print Patient Demographic Info (Face Sheet)     patient to the WH package BD     Browse Patients With Needs Past Due	with Edit/Print Patient Case LAB    Save Lab Test as Procedure	Data, if you don’t use the

AP     Add a NEW Procedure	Automatically Load

EP	Edit a Procedure	Patients option. Also,

HS	Health Summary	patients will be

BP	Browse Procedures	automatically added if lab

PR	Print a Procedure	or radiology results are

HIS	Add an HISTORICAL Procedure	sent by those applications.

RA	Add a Refusal of Treatment RE	Edit a Refusal of Treatment AN	Add a New Notification

EN	Edit a Notification BN	Browse Notifications

PL	Print Individual Letters PQ	Print Queued Letters

Select Patient Management Option:

**1c. Women’s Health Patient Profile (brief)**

| *********************** CONFIDENTIAL PATIENT INFORMATION *********************  * * *	Patient Profile	* * * Run Date: SEP 16, 2003		14:14  Patient Name: WHPATIENT,ONE (56y/o)	SSN: 666-33-5525  Case Manager: WHPROVIDER,ONE	Facility: SALT LAKE CITY HCS Cx Tx Need	: Routine PAP (by 09/09/04)	Cx Facility:  PAP Regimen : Undetermined (began NO DATE)	Pr Provider: UNKNOWN Br Tx Need	: Mammogram, Screening (by 04/11/04)Br Facility:  Hx of BR CA : &gt;1 1st degree relatives  Elig Code	:	Veteran: Yes  MST	: Unknown, not screened	CST:  ================================================================================ DATE	PROCEDURE	RESULTS/DIAGNOSIS	STATUS   |    |      |    |                           |    |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|------|----|---------------------------|----|--------|
| 1)	04/30/03                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    | PAP  |    | No Evidence of Malignancy |    | CLOSED |
| 2)	04/11/03                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    | PAP  |    | No Evidence of Malignancy |    | CLOSED |
| 3)	04/11/03                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    | MAMB |    | NOT ENTERED               |    | OPEN   |
| 4)	04/10/03                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    | BRUL |    | NOT ENTERED               |    | DELINQ |

**Women’s Health Setup, cont’d**

**Women’s Health Patient Profile (detailed)**

Outcome: NOT ENTERED	Status: CLOSED

-------------&lt; NOTIFICATIONS &gt;---------------------------------

08/01/03	LETTER, FIRST: PAP result NEM, next PAP 1Y.

2)

*********************** CONFIDENTIAL PATIENT INFORMATION *********************

* * *	Patient Profile	* * * Run Date: SEP 16, 2003		14:14

Patient Name: WHPATIENT,ONE (56y/o)	SSN: 666-33-5525

Case Manager: WHPROVIDER,ONE	Facility: SALT LAKE CITY HCS Cx Tx Need	: Routine PAP (by 09/09/04)	Cx Facility:

PAP Regimen : Undetermined (began NO DATE)	Pr Provider: UNKNOWN Br Tx Need	: Mammogram, Screening (by 04/11/04)Br Facility:

Hx of BR CA : &gt;1 1st degree relatives

Elig Code	:	Veteran: Yes

MST	: Unknown, not screened	CST:

================================================================================

------------------------------&lt; PROCEDURE: PAP &gt;--------------------------------

1)	PS2003-17	04/30/03	Res/Diag: No Evidence of Malignancy

Provider: WHPROVIDER,ONE	Status: CLOSED

| **Women’s Health Setup, cont’d**  **NOTE:**  The WH  mammogram review reminder will not be due if the WH package is set up to assign a diagnostic code to a mammograms as it is loaded from Radiology.  The WH package sees a procedure as "Pending" review (which triggers our review reminder) if the status is OPEN and the Result/Diagnosis field is blank.  If Result/Diagnosis is filled in when the mammogram is loaded into WH, then WH thinks it's been reviewed and won't send us the "Pending" status.   | **Status Given to Imported Mammograms**  The WH package can be set up to receive mammogram results from the Radiology package. This is controlled by the WH site parameters and diagnostic code translation options under Management Functions/File Maintenance:  ESP	Edit Site Parameters  EDX	Edit Diagnostic Code Translation File PDX	Print Diagnostic Code Translation File  The Mammogram Review reminder will only be due with this combination of settings:  - Status Given to Imported Mammograms: OPEN - **Diagnostic code translations are not assigned, so there is nothing entered into Result/Diagnosis field and the WH Patient Profile shows NOT ENTERED**  The Mammogram Review reminder will not be due if any of these settings combinations exist instead:  - **Diagnostic code translations assigned so something is entered into the Result/Diagnosis field** - Status Given to Imported Mammograms: CLOSED - Diagnostic code translations are or are not assigned  The "Status Given to Imported Mammograms" is entered on the second page of Edit Site Parameters and can be set to "OPEN" or "CLOSED"   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

* * *	EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS	* * *

RADIOLOGY:	Import Mammograms from Radiology: YES **Status Given to Imported Mammograms: OPEN** Include ALL Non-Veterans(Y/N)?: YES

ELIGIBILITY CODE(S):

. . .	(PAGE 2 OF 6)

| **Women’s Health Setup, cont’d**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Status Given to Imported Mammograms**  Diagnostic codes from the Radiology package can be translated into a Result/Diagnosis code.  This is what a diagnostic codes report looks like when diagnostic codes have not been assigned using WH option PDX Print Diagnostic Code Translation File:   |    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | WV DIAGNOSTIC CODE TRANSLATION LIST	DEC 20,2004 09:40 PAGE 1  *** NO RECORDS TO PRINT ***                                                                                                                                                                                                          |    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This is what you see if you decide to edit diagnostic code translations for the first time using WH option EDX	Edit Diagnostic Code Translation File:                                                                                                                                              |    |
| * * * WOMEN’S HEALTH: EDIT WV DIAGNOSTIC CODE TRANSLATION FILE	* * *  Select RESULT/DIAGNOSIS: ?  You may enter a new WV DIAGNOSTIC CODE TRANSLATION, if you wish Choose the women's health results/diagnosis code you wish to match to a radiology diagnostic code.  Only Results/Diagnoses that apply to Mammograms may be selected.  Answer with WV RESULTS/DIAGNOSIS  Do you want the entire WV RESULTS/DIAGNOSIS List? y	(Yes)Choose from:  Abnormal	90  Assessment Is Incomplete	2  Benign Finding, Negative	5  Highly Sug of Malig, Tk Action	1  Indicated, But Not Performed	5  Negative	90  No Evidence of Malignancy	90  Not Indicated	50  Prbly Benign, Short Int F/U	4  Suspicious Abnorm, Consider Bx	1  Unsatisfactory for Dx	2  Select RESULT/DIAGNOSIS: |                                                                                                                                                                                                                                                                                                    |    |

**Women’s**

**Status Given to Imported Mammograms**

WV DIAGNOSTIC CODE TRANSLATION LIST	DEC 20,2004	09:25	PAGE 1

**Health Setup,**

This is what a diagnostic codes report looks like when codes have been assigned (using PDX Print Diagnostic Code Translation File). The text in the WOMEN'S HEALTH field will be entered into the Result/Diagnosis field when the mammogram procedure is loaded, based on the Radiology diagnosis code:

**cont’d**

WOMEN'S HEALTH: Assessment Is Incomplete RADIOLOGY: UNSATISFACTORY/INCOMPLETE EXAM

WOMEN'S HEALTH: Highly Sug of Malig, Tk Action RADIOLOGY: ABNORMALITY, ATTN. NEEDED

WOMEN'S HEALTH: Negative RADIOLOGY: NORMAL

###### 

| TIP:  Coordination between CACs and Women’s Health Case Managers will help the mapping process   | 1. **Map local findings to the national Reminder Terms.**  *Option: Reminder Term Management*  on the  *Reminder Management Menu.*  Before using WH reminders, map the local findings your site uses to represent the national reminder terms, if necessary.  - Prepare a list of your local findings – health factors, taxonomies, etc. that you use to represent WH terms. - Review the national term definitions (use the options on the Reminder Term Management menu), to compare these to what you are using locally to represent WH terms.   |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Term Mapping Recommendations**

**Mammogram Terms**

| **Term**                   | **Mapping**                                                                                                                                                                                                                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Patient Cohort Findings*  | *The following reminder terms determine whether the reminder applies to the patient.*                                                                                                                                                                                                                              |
| VA-TERMINAL CANCER PATIENT | No mapping necessary. Use the VA- TERMINAL CANCER PATIENTS reminder  taxonomy that has been previously distributed.                                                                                                                                                                                                |
| VA-WH BILATERAL MASTECTOMY | This term will use the VA-WH BILATERAL MASTECTOMY taxonomy to find coded bilateral mastectomies. The health factor WH  BILATERAL MASTECTOMY distributed with this term may be used or add any local health factor that  represents the patient had a bilateral mastectomy and no longer needs mammogram screening. |

**Mammogram Terms, cont’d**

| **Term**                          | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Resolution Findings*             | *The following are reminder terms that resolve the reminder. Function Findings use these findings to determine whether a result is the most recent finding or whether a short-term resolution finding is the most recent finding. If the most recent finding is a short-term resolution finding, the reminder will be due based on one of the following Function Finding frequency periods: 4 months or 6 months. If the result is the most recent finding, the baseline age/frequency is used. However, the baseline frequency will be overridden if the Functional*  *Findings determine that an information finding exists which alters the baseline frequency to 1 or 2 years.* |
| VA-WH MAMMOGRAM SCREEN IN WH PKG  | No mapping necessary. This term uses the pre-mapped computed finding: VA-WH MAMMOGRAM IN WH PKG to find mammogram screening findings in the  Women's Health Package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VA-WH MAMMOGRAM SCREEN IN RAD PKG | Mapping is needed. This term represent Mammogram results documented in the Radiology package. Map local radiology procedures that represent the following procedures:  MAMMOGRAM BILAT MAMMOGRAM UNILAT MAMMOGRAM SCREEN  Each finding should have a condition added to exclude unsatisfactory results.                                                                                                                                                                                                                                                                                                                                                                             |
| VA-WH MAMMOGRAM SCREEN DONE       | Some mapping may be appropriate. This reminder term will use the previously distributed VA- MAMMOGRAM/SCREEN taxonomy to find ICD DIAGNOSIS or CPT coded results.  Use the new WH MAMMOGRAM OUTSIDE health factor to document Mammogram results completed outside the VA when the Mammogram results are not documented in Radiology, Women's Health or Consult packages.  Map local findings, such as consult orders related to Mammogram Screening. Use appropriate condition logic to indicate Mammogram screening has been completed.                                                                                                                                            |

**Mammogram Terms, cont’d**

| **Term**                             | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-WH MAMMOGRAM SCREEN NOT INDICATED | Use the findings distributed with this reminder term or map any local findings that indicate a Mammogram screen is not indicated for this patient.  This term is distributed with mapping to the following health factors:  INACTIVATE BREAST CANCER SCREEN  (distributed with the first version of the Clinical Reminder package in 1996 to inactivate the BREAST CANCER reminder).  WH PAP MAMMOGRAM SCREEN NOT INDICATED VA LIMITED LIFE EXPECTANCY  Use in National VA-WH MAMMOGRAM SCREENING reminder:  This term is used in WH reminders to inactivate the Mammogram screening reminder. A clinician can  **reactivate the reminder**  by selecting one of the frequencies from the screening reminder dialog. The 4M, 6M, 1Y, and 2Y health factors are used by function findings to set the reminder frequency.  Begin date  **of T-6M**  has been added to HF.VA LIMITED LIFE EXPECTANCY and TX.VA-TERMINAL  CANCER PATIENTS so screening will come due again if the patient lives longer than expected or if the patient has been misdiagnosed.  Sites may prefer to use local LIMITED LIFE EXPECTANCY health factors and add their health factors to other reminder terms, which cause the Mammogram Screening reminder to be due without requiring a clinician to select a finding to reactivate the reminder. (E.g., Add the local life expectancy health factor for "local LIFE EXPECTANCY 6M" to the VA- WH MAMMOGRAM SCREEN NOT INDICATED  term. |

**Mammogram Terms, cont’d**

| **Term**                                  | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-WH BREAST CARE ORDER HEALTH FACTOR     | Use the health factors distributed with the reminder term if they are appropriate for your facility to track breast care orders. This reminder term represents the action taken from the dialog to indicate the clinician intends to place an order related to mammogram screening. The health factor date will be used to calculate the resolution frequency, instead of the Start date related to the order actually placed.  Health factors distributed with this term:  - WH ORDER MAMMOGRAM SCREEN HF (Use this if an order menu is referenced as the quick order, or use for a quick order for mammogram screening to radiology or consults) - WH ORDER MAMMOGRAM BILAT HF (Use when quick order is for bilateral mammogram) - WH ORDER MAMMOGRAM UNILAT HF (Use when quick order is for unilateral mammogram) |
| VA-WH MAMMOGRAM SCREEN DEFER              | Use the WH MAMMOGRAM DEFERRED or WH  MAMMOGRAM DECLINED health factors distributed with this term or add any local health factor representing that mammogram screening should be satisfied for one  week.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VA-MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG | Mapping will be necessary. This term represent Mammogram results documented in the Radiology package. Map local radiology procedures that represent the following procedures:  MAMMOGRAM BILAT MAMMOGRAM UNILAT MAMMOGRAM SCREEN  Each finding should have a condition that checks for unsatisfactory results. No mapping is necessary for the WH package. Use the VA-WH MAMMOGRAM IN WH PKG computed finding and the value  UNSATISFACTORY" to find unsatisfactory results documented in the WH package.                                                                                                                                                                                                                                                                                                            |
| VA-WH MAMMOGRAM PENDING REVIEW            | No mapping necessary. New VA-WH MAMMOGRAM REVIEW computed finding will be installed with this reminder. This computed findings will make the VA-WH MAMMOGRAM REVIEW reminder due when the condition is: I V="Pending". It will then return mammogram results pending clinician review from the  WH package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Mammogram Terms, cont’d**

| **Term**                            | **Mapping**                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Information Findings*              | *The following are information reminder terms that are used in Function Findings to alter the baseline Age/Frequency. If the most recent resolution finding is a documented result, the frequency for the next Mammogram screen will be based on these reminder*  *terms.*                                                                                   |
| VA-WH MAMMOGRAM SCREEN FREQ - 4M    | Use the WH MAMMOGRAM SCREEN FREQ - 4M  health factor distributed with this reminder term, or add any local findings that indicate mammogram screening should occur every 4 months.                                                                                                                                                                           |
| VA-WH MAMMOGRAM SCREEN FREQ - 6M    | Use the WH MAMMOGRAM SCREEN FREQ - 6M  health factor distributed with this reminder term, or add any local findings that indicate mammogram screening  should occur every 6 months.                                                                                                                                                                          |
| VA-WH MAMMOGRAM SCREEN FREQ - 1Y    | Use the WH MAMMOGRAM SCREEN FREQ – 1Y  health factor distributed with this reminder term, or add any local findings that indicate mammogram screening should occur every 1 year.                                                                                                                                                                             |
| VA-WH MAMMOGRAM SCREEN FREQ - 2Y    | Use the WH MAMMOGRAM SCREEN FREQ - 2Y  health factor distributed with this term or add any local  health factor that represents mammogram screening should occur every two years                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                                                                                                                              |
| *Information Only*                  | *The following reminder terms are "information only" terms that are not used to alter the frequency, but provide*  *information that may be helpful to the clinician.*                                                                                                                                                                                       |
| VA-WH HX BREAST CANCER/ABNORMAL MAM | Use the previously distributed VA-BREAST TUMOR and VA-MASTECTOMY taxonomies mapped to this term. This term uses computed finding VA-WH MAMMOGRAM ABNORMAL IN WH PKG to search  for the existence of any abnormal results in the WH Package.                                                                                                                  |
| VA-WH MAMMOGRAM ORDER               | Map local orderable items that represent mammogram related orders (e.g., Consult order to Women's Health Clinic). Use the conditions that indicate the order is not completed, discontinued, or cancelled. This reminder term represents orders pending completion.  This term can also be used to indicate the patient is being followed by a gynecologist. |

**Pap Smear Reminder Terms**

| **Term**                            | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Patient Cohort Findings*           | *The following reminder terms determine whether the reminder applies to the patient.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VA-TERMINAL CANCER PATIENT          | No mapping necessary. Use the VA-TERMINAL CANCER PATIENTS reminder taxonomy that has  been previously distributed.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VA-WH HYSTERECTOMY W/CERVIX REMOVAL | No mapping necessary. Use the VA-WH HYSTERECTOMY W/CERVIX REMOVED  reminder taxonomy distributed with this term. Note the VA-CERVICAL CA/ABNORMAL PAP reminder  taxonomy is now used for information only and should not be mapped to this reminder term since it contains codes where the cervix may not have been removed.  This reminder term is also mapped to the new health  factor WH HYSTERECTOMY W/CERVIX REMOVED.                                                                                                                                                  |
| *Resolution Findings*               | *The following reminder terms resolve the reminder. These resolution terms are defined with a "Use in Resolution Logic,” but no Frequency. Frequency for this reminder will be determined by Function Findings (FF) logic, which examines the most recent findings:*  - *If Function Findings determine that the most recent finding is a result, the baseline age and frequency will be used.* - *If Function Findings determine that an information finding exists that alters the baseline frequency to 4M, 6M, 1Y, 2Y or 3Y, the baseline frequency will be overridden.* |
| VA-WH PAP SMEAR SCREEN IN WH PKG    | No mapping necessary. This term represents PAP Smear results documented in the Women's Health (WH) Package. Use the new VA-WH PAP SMEAR IN WH PKG computed finding distributed with this reminder term. This computed finding looks for PAP  smear results in the Women's Health Package.                                                                                                                                                                                                                                                                                    |

**Pap Smear Reminder Terms, cont’d**

| **Term**                            | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-WH PAP SMEAR SCREEN IN LAB PKG   | No mapping necessary. This term represents PAP Smear results documented in the Laboratory package. Use the new VA-WH PAP SMEAR IN LAB PKG computed finding distributed with this reminder term. This computed finding looks for PAP smear results in the Laboratory package.  This computed finding will only work if the Women's Health WV PROCEDURE TYPE file entry for PAP SMEAR has SNOMED codes defined that are used for PAP Smear results at your facility. The SNOMED codes  need to be defined regardless of whether the Women's Health Package is being used.                                                                                                                                                      |
| VA-WH PAP SMEAR DONE                | No mapping necessary. Use the new VA-WH PAP SMEAR DONE CODES taxonomy distributed with this reminder term. This taxonomy is similar to the VA- CERVICAL CANCER SCREEN taxonomy distributed to the field with the first reminder package distribution. The new taxonomy should be used because it does not include codes such as Q0091, which represents PAP smears obtained by the clinician.  Use the new WH PAP SMEAR OUTSIDE health factor to document PAP Smear results completed outside the VA when the PAP Smear results are not documented in Lab, Women's Health or Consult packages.                                                                                                                               |
| VA-WH PAP SMEAR OBTAINED            | No mapping is necessary. Use the new taxonomy VA-  WH PAP SMEAR OBTAINED. This term represents the clinician's actions taken to obtain the PAP smear.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VA-WH PAP SMEAR ORDER HEALTH FACTOR | The following health factors are distributed with this term:  - WH ORDER PAP SMEAR SCREEN HF (for use when an order menu with a PAP Smear Screen order is used from the reminder dialog). - WH ORDER REFER WH CLINIC GYN CARE HF (for use when a quick order is used for WH CLINIC GYN CARE referral in reminder dialogs). - WH ORDER REFER GYNECOLOGIST HF (for use when a quick order is used for GYNECOLOGY referral in reminder dialogs).  This reminder term represents the action taken from the dialog to indicate the clinician selected an element that could generate an order for PAP Smear. The health factor  date will be used to calculate the resolution frequency, instead of using the Order's Start date. |

**Pap Smear Reminder Terms, cont’d**

| **Term**                                     | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-WH PAP SMEAR SCREEN NOT INDICATED         | Use the findings distributed with this reminder term or map any local findings that indicate a PAP smear screen is not  indicated for this patient. This term is distributed with mapping to the following health factors:  INACTIVATE CERVIX CANCER SCREEN (distributed with the first version of the Clinical Reminder package in 1996 to inactivate the CERVICAL CANCER reminder).  WH PAP SMEAR SCREEN NOT INDICATED VA LIMITED LIFE EXPECTANCY  and the following taxonomy:  VA-TERMINAL CANCER PATIENTS  This term is used in WH reminders to inactivate the PAP Smear Screening reminder. A clinician can reactivate the reminder by selecting one of the frequencies from the screening reminder dialog. The 4M, 6M, 1Y, 2Y, and 3Y health factors are used by function findings to set the reminder frequency.  Begin date  **of T-6M**  has been added to HF.VA LIMITED LIFE EXPECTANCY and TX.VA-TERMINAL CANCER PATIENTS so  screening will come due again if the patient lives longer than expected or if the patient has been misdiagnosed.  Sites may prefer to use local LIMITED LIFE EXPECTANCY health factors and add their health factors to other reminder terms which cause the PAP Smear Screening reminder to be due without requiring a clinician to  select a finding to reactivate the reminder. (E.g., Add the local life expectancy  health factor for "local LIFE EXPECTANCY 6M” to the VA-WH PAP SCREEN NOT INDICATED term. |
| VA-WH PAP SMEAR SCREEN DEFER                 | Use the WH PAP SMEAR DECLINED and/or WH PAP SMEAR  DEFERRED health factors distributed with this term, or add any local health factors representing that PAP smear screening should be deferred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VA-WH PAP SMEAR UNSATISFACTORY IN LAB/WH PKG | No mapping necessary. This term represents unsatisfactory \ PAP Smear results documented in the Laboratory package. Use the new VA-WH PAP SMEAR IN LAB PKG computed finding  distributed with this reminder term. This computed finding looks for PAP smear results in the Laboratory package where the Result Status that is "Unsatisfactory"  **This computed finding will only work if the Women's Health WV PROCEDURE TYPE file entry for PAP SMEAR has SNOMED codes defined that are used by your local Lab Service to document PAP Smear results in the Lab Package.  The SNOMED codes need to be defined regardless of whether the Women's Health**  **Package is being used.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Pap Smear Reminder Terms, cont’d**

| **Term**                         | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Information Findings:*          | *Function Findings (FF) will be used to determine the frequency of these reminders. The following are information reminder terms that are used in Function Findings to alter the baseline Age/Frequency. If the most recent resolution finding is a documented result, the frequency for the next PAP Smear will be based on these reminder terms. If more than one of the frequency findings is recorded at the same date/time, the finding that makes*  *the reminder due most often will prevail.* |
| VA-WH PAP SMEAR SCREEN FREQ – 4M | Use the WH PAP SMEAR SCREEN - FREQ 4M health factor distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every 4 months.                                                                                                                                                                                                                                                                                                                     |
| VA-WH PAP SMEAR SCREEN FREQ – 6M | Use the WH PAP SMEAR SCREEN FREQ - 6M health factor distributed with this reminder term or add any local findings  that indicate PAP smear screening should occur every 6 months.                                                                                                                                                                                                                                                                                                                     |
| VA-WH PAP SMEAR SCREEN FREQ – 1Y | Use the WH PAP SMEAR SCREEN FREQ - 1Y health factor  distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every year.                                                                                                                                                                                                                                                                                                                        |
| VA-WH PAP SMEAR SCREEN FREQ – 2Y | Use the WH PAP SMEAR SCREEN FREQ - 2Y health factor distributed with this reminder term, or add any local findings that  indicate the PAP smear screening should occur every 2 years.                                                                                                                                                                                                                                                                                                                 |
| VA-WH PAP SMEAR SCREEN FREQ – 3Y | Use the WH PAP SMEAR SCREEN FREQ - 3Y health factor distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every 3 years.                                                                                                                                                                                                                                                                                                                      |
| *Information Only*               | *The following reminder terms are "information only" terms that are not used to alter the frequency, but provide information that may be helpful to the clinician.*                                                                                                                                                                                                                                                                                                                                   |
| VA-WH HYSTERECTOMY               | This reminder term represents hysterectomy related procedures. It is pre-mapped to use the VA-HYSTERECTOMY taxonomy, which was distributed, to the field in 1996. It is not used to alter the patient cohort because it contains hysterectomy codes that indicate the patient’s cervix may or may not have been removed.                                                                                                                                                                              |

**Pap Smear Reminder Terms, cont’d**

| **Term**                              | **Mapping**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA-WH HX CERVICAL CANCER/ABNORMAL PAP | This reminder term is mapped to the taxonomy VA-CERVICAL CA/ABNORMAL PAP findings. This term represents ICD9, ICD0, and CPT codes that indicate the patient has a history of cervical cancer or a diagnosis for abnormal PAP. Sites may choose to only use documented diagnosis and procedure codes removing mapping to Women's Health.  This reminder term is also mapped to the computed finding  VA-WH PAP SMEAR SCREEN IN WH PKG with a condition check for "Abnormal" used for the search. If PAP smear results are documented in the Women's Health package, the computed finding VA-WH PAP SMEAR SCREEN IN WH PKG will find the most recent PAP Smear entry that has an "Abnormal" result.  **Sites can remove this mapped item if they are not using the Women's Health package to store PAP results.**  The reminder term may also be mapped to the computed finding VA-WH PAP SMEAR SCREEN IN LAB PKG with a condition check for "Abnormal" Result Type. The Result Type is based on Procedure definitions in the Women's Health Package. |
| VA-WH PAP SMEAR ORDER                 | Map local orderable items that represent PAP smear related orders (e.g., Consult order to Women's Health Clinic).  Use the conditions that indicate the order is not completed,  discontinued, or cancelled. This reminder term represents orders pending completion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| **Test the reminders**                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **3. Run the Reminder Test option after term definition mapping is completed.**  **Review the results of patient data with each of the findings mapped to the term.**  *Option: Reminders Test*  on the  *Reminder Managers Menu*  Select Reminder Managers Menu Option:  **RT**  Reminder Test Select Patient:  **CRPATIENT,SIX**  4-30-44  666809999	YES	EMPLOYEE  Enrollment Priority: GROUP 5	Category: IN PROCESS End Date:  Select Reminder: VA-WH MAMMOGRAM SCREENING |

| **Do not edit these dialog elements: VA-WH MAMMOGRAM RESULTS and VA-WH PAP SMEAR**  **RESULTS.**  These dialog elements do not have finding items associated with them in Dialog Management. The finding items and the text that appear in the elements are set when the dialogs are being loaded into CPRS.  NOTE: Do not install and release the PAP review reminder to the field if PAP cytology results are not recorded in the VistA Lab package and are not updating WH package.  TIP  Coordination between CACs and Women’s Health Case Managers will help the dialog edit process   |    | 1. **Use the Reminder Dialog options to edit the national (exported) dialogs.**  After mapping local findings to the national terms, determine whether to use local findings as the data elements that are captured, or the national findings that are already mapped to the national terms. Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs. Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.  - If using local findings, edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding.  Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.  - Add local dialog elements with local Order Dialogs for additional ordering options for the clinicians. Some sites have clinicians order a consult to a service that provides PAP smears. If your site does this, copy the reminder dialog to a local reminder dialog and then add the local dialog element for the consult order to the reminder dialog so this practice can continue. - Some sites have local entries in the Women's Health WV Notification Purpose file. If your site does this, copy the reminder dialog to a local reminder dialog, then add or modify the notifications so this practice can continue. Under reminder findings, use the new "WH" finding type to point to the entries. - If your site chooses not to send letters via the WH package, copy the appropriate national dialog components to local components and remove the findings related to WH notifications.  The national reminders and dialogs can  ***only***  be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Steps to add or edit dialog elements:**  a. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI) and Change View (CV) to see the  Dialog view:   |                                                   |    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----|
| Select Reminder Managers Menu Option:  **DM**  Reminder Dialog Management DP	Dialog Parameters ...  DI	Reminder Dialogs DR	Dialog Reports ...  IA	Inactive Codes Mail Message  Select Reminder Dialog Management Option:  **DI**  Reminder Dialogs  Dialog List	Mar 24, 2004@08:52:46	Page:	1 of	18 REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog Status  1. A BLOOD EXPOSURE	DIABETIC EXAM DIALOG 2. A NEW REMINDER	A NEW REMINDER	Disabled 3. AGP ABNORMAL WH STUFF                                                                                                                                                                                                                              |                                                                                                                                                                                      |                                                   |    |
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                      | **&gt;&gt;&gt;**                                  |    |
| AR	All reminders	LR	Linked Reminders	QU	Quit CV	Change View	RN	Name/Print Name  Select Item: Next Screen//  **CV**  Select one of the following:	Select Change View (CV) to change to the  1. Reminder Dialogs	Dialog View 2. Dialog Elements 3. Forced Values 4. Dialog Groups  P	Additional Prompts  R	Reminders  RG	Result Group (Mental Health) RE	Result Element (Mental Health)  TYPE OF VIEW: R//  **D**  Reminder Dialogs  AD	Add Reminder Dialog	PT	List/Print All	QU	Quit  Dialog List	Mar 24, 2004@08:47	Page:	1 of	14 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)  Item Reminder Dialog Name	Source Reminder	Status  1. A NEW BP CHECK	*NONE*	Disabled 2. A NEW REMINDER	*NONE*	Disabled 3. A NEW REMINDER DIALOG	*NONE* |                                                                                                                                                                                      |                                                   |    |
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                      | **&gt;&gt;&gt;**                                  |    |
| CV	Change View	RN	Name/Print Name Select Item: Next Screen//  **SL**  SL  Search for:  **V-WH**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                      | Select SL (Search List) to jump to the WH dialogs |    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                      |                                                   |    |

**Editing Dialogs**

1. Use the Search List (SL) action to get to the WH–named dialogs, and then enter the number of the reminder.

**Dialog List** Mar 24, 2004@08:52:46	Page:	12 of	13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

**+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**

ADD	Add Element/Group	DS	Dialog Summary	INQ	Inquiry/Print CO	Copy Dialog	DO	Dialog Overview	QU	Quit

Find Next 'VA-WH'? Yes// **NO**

DD	Detailed Display	DT	Dialog Text

1. Select the dialog number to see details.

+Item Reminder Dialog Name	Source Reminder	Status

Select Item: Quit// **181**

DP	Progress Note Text	ED	Edit/Delete Dialog

1. VA-WH MAMMOGRAM REVIEW RESULTS	VA-WH MAMMOGRAM REVIEW RE Linked

Dialog Edit List	Mar 24, 2004@08:58:33	Page:	1 of	4

Select Item: Next Screen//

1. Make edits, as needed, by entering the dialog element number.
    1. VA-WH MAMMOGRAM SCREENING	VA-WH MAMMOGRAM SCREENING Linked
REMINDER DIALOG NAME: VA-WH PAP SMEAR SCREENING [NATIONAL] *LIMITED EDIT*
    1. VA-WH PAP SMEAR REVIEW RESULTS	VA-WH PAP SMEAR REVIEW RE Linked
Item	Seq.	Dialog Summary
    1. VA-WH PAP SMEAR SCREENING	VA-WH PAP SMEAR SCREENING Linked
        1. 5	Group: VA-WH GP PAP SCREEN HEADER
        1. 5.5	Element: VA-WH PAP HEADER1 - SCREEN
        1. 5.10	Group: VA-WH GP PAP SCREEN HEADER-EXPANDED
        1. 5.10.5	Element: VA-WH PAP HEADER2 - SCREEN
        1. 6	Element: VA-WH DOTTED LINE
        1. 10	Group: VA-WH GP PAP SCREEN
        1. 10.5	Element: VA-WH PAP SMEAR OBTAINED
        1. 10.15	Element: VA-WH PAP SMEAR COMPLETED OUTSIDE

1. Two new **forced values** are included with this project.

###### 2 PXRM WH NOTIFICATION TYPE

- PXRM WH UPDATE TREATMENT NEED

Note: These forced values are only used with the VA-WH MAMMOGRAM REVIEW and VA-WH PAP SMEAR REVIEW

reminders and dialogs.

PXRM WH NOTIFICATION TYPE is a **forced value** that allows sites to identify a notification type that will update **the Women’s Health package** . For this **forced value** to work properly, you must set it equal to one or more of three codes “L”, “I”, or “P” and must separate multiple codes by a colon (i.e. L:I or L:P:I)

**Notification type definitions** :

“L” stands for Letter notification type = letter will notify Patient. The WH package is updated to send a result letter, which will be printed with the next WH batch run.

“I” stands for In-Person notification type = patient was notified of results in person. The WH package is updated with this information.

“P” stands for Phone Call notification type = patient was notified of results by phone. The WH package is updated with this information.

This **forced value** will also update the progress note. PXRM WH UPDATE TREATMENT NEED

This **forced value** is used with the “CPRS UPDATE” notification purposes. It updates the WH treatment need information, but does not generate a letter. This **forced value** must be set to “CPRS.”

**Ordering a Consult:**

If your site wants to be able to order consults from the screening reminders to a service that does pap smears or mammograms, you need to create a quick order for the consult or a menu and put it in the finding item field indicated below:

| **Test Reminders**   | 1. **Verify that the reminders function properly.**  1. Run a Reminders Due Report to determine if the WH Clinical Reminder statuses reported are correct.  *Option: Reminders Due*  on the  *Reminder Reports menu*  This report can be displayed at the beginning of the day for patients being seen that day. Reminder reports offer a way to review how the mapping and the local data will potentially be viewed by the extracts that will be sent to the Austin database from the reminders.  - Each of the reminders can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder. - The reports can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved. - Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.  1. Use the Reminder Test option to test the reminders.  *Option: Reminders Test*  on the  *Reminder Management menu*  1. Select a patient who had a mammogram screening done within the past year.  Run the Reminder Test option on the VA-WH MAMMOGRAM SCREENING reminder definition.  The status of the reminder should be “RESOLVED.” Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “RESOLVED.”   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Test Reminders**   | 1. If you use the WH package, select a patient whose most recent mammogram in the WH package has a RESULTS/DIAGNOSIS that is blank and a STATUS that is OPEN.  Run the Reminder Test option on the VA-WH MAMMOGRAM REVIEW RESULTS reminder definition.  The status of the reminder should be “DUE.”  Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “DUE.”  1. Select a patient whose most recent mammogram screening took place within the past year and the results have been recorded. Run the Reminder Test option on VA-WH MAMMOGRAM SCREENING reminder definition.  The status of the reminder should be “Applicable.”  Use the clinical maintenance view in the CPRS GUI. The status of the reminder should be "Applicable."  1. Repeat steps 1-3 for the PAP Reminders.   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Add Reminders to CPRS Cover Sheet**   | 1. **Add the nationally distributed reminders to the CPRS Cover Sheet.**  (NOTE: Make sure that New Reminders Parameter on the CPRS Configuration Menu is set to Yes. This is required in order to use the “Edit Cover Sheet Reminder List” functionality.)  1. Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”   |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Edit Cover Sheet Reminder List option

Action option

Reminders Clock

**CRPROVIDER,ONE**

**CRPROVIDER,ONE**

| **Add Reminders to CPRS Cover Sheet**   | **Adding Reminders to Cover Sheet, cont’d**  1. When the Cover Sheet Reminder List opens, set the Cover sheet parameter level. Click on the System, Division, Service, User Class, and/or User buttons, as appropriate for your site.  1. Locate and click on the VA-WH MAMMOGRAM SCREENING reminder; click the Add button (or double-click the reminder).  1. Click on the VA-WH MAMMOGRAM REVIEW RESULTS reminder and click the Add button (or double-click the reminder).   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **CRPROVIDER,ONE**   |
|----------------------|
| **CRPROVIDER,ONE**   |
| **CRPROVIDER,ONE**   |
| **CRPROVIDER,ONE**   |

| **WV Notification Setup**  **NOTE:**  Your site can choose whether to include the Print Now button on screening reminder dialogs. This can be set with a new option on the CPRS Reminder Configuration menu: PXRM WH PRINT NOW   | 1. **Set up entries in the WV Notification Purpose file**  Use the AEP Add/Edit a Notification Purpose &amp; Letter manager option in the Women's Health package to customize letters in the WV Notification Purpose file for each PAP and mammogram entry installed as part of this project. The breast or cervical treatment need and due date should be set and the default letter text should be modified to explain the reason for the letter.  *See Step 1c and Appendix E in this manual for examples.*  **NOTE:**  If your site chooses not to send letters via the WH package, copy the appropriate national dialog components to local components and remove the findings related to WH notifications.  **NOTE**  : Several entries beginning with “CPRS UPDATE” were made in the WV Notification Purpose file as part of the WH installation. These notification purposes are used by the screening reminders dialogs to set screening frequency and should not be modified.  1. **Determine how and where letters will be printed.**  Your site needs to determine if letters will be queued to the WH package and will be printed in the Case Manager’s office, or if the clinician will use the Print Now option, to print and mail the letters from the clinician’s office.  **Print Now flag**  : The “Print Now” selection is optional. A parameter can be set (at the system level) to allow the “Print Now” button to be added to the dialog. By default “Print Now” is turned off: the CPRS Reminder Configuration Option called WH Print Now Active is released with a Value of NO. If the value is changed to YES, the “Print Now” button will appear on the dialog. Whether the “Print Now” button is added to the dialog or not, the default will always be that the letter is queued to the WH package.  The text in the progress note will be one of the following:  Print Now Active/  **Yes**  : Letter queued to print at Device Name on finish Date/Time  Print Now Active/  **No**  : Letter queued to WH package Date/Time  **If your site chooses No, identify where letters will print and who will be responsible for retrieving and mailing these.**   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Test Dialogs**   | 1. **Verify that the dialogs function properly**  Test the WH Reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:  - Correct Progress Note text is posted - Finding Item gets sent to PCE - Reminder is satisfied  Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.  ***Steps to test dialogs:***  1. On the cover sheet, click on the Reminders icon. 2. Click on reminders in the Reminders box to see details of a reminder. 3. Open the Notes tab and select New Note. Enter a title. 4. Open the Reminders drawer and review the contents.   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Test Dialogs**   | 1. **(cont’d) Verify that the dialogs function properly**  ***Steps to test dialogs:***  1. Locate the VA-WH Mammogram Screening reminder dialog and open it. 2. In the dialog box, check relevant actions. 3. Finish the reminder processing. 4. Review the text added to the note to assure its correctness. 5. Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Mammogram Screening Dialog**

<!-- image -->

| **Test Dialogs**   | 1. **(cont’d) Verify that the dialogs function properly**  1. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.  1. Repeat steps 5-10 for all the dialogs.   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

**Example: Mammogram Screening Clinical Maintenance Display**

Setup Guide – Testing Dialogs

| **Test Dialogs**   | **9. (cont’d) Verify that the dialogs function properly**  **NOTE: Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately. This is especially critical if you’re doing the screening reminder and want to see if the screening reminder has been resolved.**  Also remember to save notes and change the visit date between tests to simulate a normal process.  **To test features like change in frequency**  , you may need to enter a series of historical entries. Some findings resolve the reminder for up to 9 months, while others make the reminder due again in 4 or 6 months, 1, 2 or 3 years. You will need to create visits within these time frames of 4 -6 months or 1-2-3 years in order to see the results.  **To test the PAP smear review reminder**  , you will need to enter a PAP smear into the VistA Lab package. Once the results are verified and released, results will be added to WH if the WH parameters have been set up to receive them. See page 12. If the patient is not in the WH package, a WH patient record will be added; then the results will be loaded and the PAP reminder will be due.  **To test the mammogram review reminder**  , you will need to enter mammogram results into the VistA Radiology package. Once the results are verified and released, results will be added to WH if the WH parameters have been set up to receive them. See page 12. If the patient is not in the WH package, a WH patient record will be added; then the results will be loaded and the mammogram reminder will be due.   |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **10. Activate alerts**  Three new information alerts are exported with this software. They notify clinicians or designated users when radiology and lab results are available.  All new notifications/alerts are exported in a "disabled" state. This allows sites to selectively enable them when they are ready and the users have been forewarned. CACs enable notifications/alerts as follows:   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select OPTION NAME:  **ORMGR**  CPRS Manager Menu	menu  Select CPRS Manager Menu Option:  **PE**  CPRS Configuration (Clin Coord) Select CPRS Configuration (Clin Coord) Option:  **NO**  Notification Mgmt Menu Select Notification Mgmt Menu Option:  **1**  Enable/Disable Notifications  Set PROCESSING FLAG Parameters for Notifications Processing Flag may be set for the following:  1. User	USR	[choose from NEW PERSON] 2. Team (OE/RR)	OTL	[choose from OE/RR LIST] 3. Service	SRV	[choose from SERVICE/SECTION] 4. Location	LOC	[choose from HOSPITAL LOCATION] 5. Division	DIV	[choose from INSTITUTION] 6. System		SYS	[xxx] Enter selection: **6** System  ------- Setting Processing Flag	for System: DEVCUR.FO-SLC.MED.VA.GOV -------  Select Notification:  **ANATOMIC PATHOLOGY RESULTS**  Notification: ANATOMIC PATHOLOGY RESULTS//  **&lt;Enter&gt;**  ANATOMIC PATHOLOGY RESULTS ANATOMIC PATHOLOGY RESULTS  Value: Disabled//  **Enabled**  Select Notification:  **MAMMOGRAM RESULTS**  Are you adding MAMMOGRAM RESULTS as a new Notification? Yes//  **&lt;Enter&gt;**  YES  Notification: MAMMOGRAM RESULTS//  **&lt;Enter&gt;**  MAMMOGRAM RESULTS	MAMMOGRAM RESULTS  Value:  **Enabled**  Select Notification:  **PAP SMEAR RESULTS**  Are you adding PAP SMEAR RESULTS as a new Notification? Yes//  **&lt;Enter&gt;**  YES  Notification: PAP SMEAR RESULTS//  **&lt;Enter&gt;**  PAP SMEAR RESULTS	PAP SMEAR RESULTS  Value:  **Enabled** |                                                                                                                                                                                                                                                                                                                                                                                                       |

Install Package(s)

Select INSTALL NAME: **wv*1.0*16** Loaded from Distribution	Loaded from Distribution 2/5/05@16:08:06

=&gt; WV*1.0*16, LR*5.2*311, OR*3.0*210, PXRM*2.0*1	;Created on Feb 04, 200

This Distribution was loaded on Feb 05, 2005@16:08:06 with header of

WV*1.0*16, LR*5.2*311, OR*3.0*210, PXRM*2.0*1	;Created on Feb 04, 2005@17:17

:36

It consisted of the following Install(s):

WV*1.0*16	LR*5.2*311	OR*3.0*210	PXRM*2.0*1

Checking Install for Package WV*1.0*16 Install Questions for WV*1.0*16 Incoming Files:

790.02	WV SITE PARAMETER	(Partial Definition) Note:	You already have the 'WV SITE PARAMETER' File.

1. WV PROCEDURE	(Partial Definition) Note:	You already have the 'WV PROCEDURE' File.

1. WV PROCEDURE TYPE

Note:	You already have the 'WV PROCEDURE TYPE' File.

790.404	WV NOTIFICATION PURPOSE	(Partial Definition) Note:	You already have the 'WV NOTIFICATION PURPOSE' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// **n** NO Checking Install for Package LR*5.2*311

Install Questions for LR*5.2*311

Checking Install for Package OR*3.0*210 Install Questions for OR*3.0*210 Incoming Files:

100.9	OE/RR NOTIFICATIONS	(including data) Note:	You already have the 'OE/RR NOTIFICATIONS' File. I will OVERWRITE your data with mine.

Checking Install for Package PXRM*2.0*1

Will first run the Environment Check Routine, PXRMWHEV Environment check passed, ok to install PXRM*2.0*1 Install Questions for PXRM*2.0*1

Incoming Files:

1. REMINDER DIALOG	(including data) Note:	You already have the 'REMINDER DIALOG' File. I will OVERWRITE your data with mine.

1. REMINDER GUI PROCESS	(including data) Note:	You already have the 'REMINDER GUI PROCESS' File. I will REPLACE your data with mine.

801.45	REMINDER FINDING TYPE PARAMETER	(including data) Note:	You already have the 'REMINDER FINDING TYPE PARAMETER' File. I will OVERWRITE your data with mine.

811.8	REMINDER EXCHANGE	(including data) Note:	You already have the 'REMINDER EXCHANGE' File. I will REPLACE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? YES// **n** NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// **n** NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME// 0;80;99999	TELNET	WV*1.0*16

Install Started for WV*1.0*16 :

Feb 05, 2005@16:22:38

Build Distribution Date: Feb 04, 2005 Installing Routines:

Feb 05, 2005@16:22:39

Installing Data Dictionaries:

Feb 05, 2005@16:22:39

Installing PACKAGE COMPONENTS:

Installing FORM

Feb 05, 2005@16:22:41

Running Post-Install Routine: ^WV16PST

Will build new 'AC' x-ref on FILE 790.1 in background job #2272

Updating Routine file... Updating KIDS files...

WV*1.0*16 Installed.

Feb 05, 2005@16:22:42

Install Message sent #432 [1;1H	LR*5.2*311 Install Started for LR*5.2*311 :

Feb 05, 2005@16:22:43

Build Distribution Date: Feb 04, 2005 Installing Routines:

Feb 05, 2005@16:22:43

Running Post-Install Routine: EN^LR311PST Creating index definition ...

Creating index definition ... Updating Routine file...

Updating KIDS files...

LR*5.2*311 Installed.

Feb 05, 2005@16:22:45

Install Message sent #433	OR*3.0*210 Install Started for OR*3.0*210 :

Feb 05, 2005@16:22:45

Build Distribution Date: Feb 04, 2005 Installing Routines:

Feb 05, 2005@16:22:45

Installing Data Dictionaries:

Feb 05, 2005@16:22:45

Installing Data:

Feb 05, 2005@16:22:46

Running Post-Install Routine: POST^ORY210 Updating Routine file...

Updating KIDS files...

OR*3.0*210 Installed.

Feb 05, 2005@16:22:46

Install Message sent #434	PXRM*2.0*1 Install Started for PXRM*2.0*1 :

Feb 05, 2005@16:22:46

Build Distribution Date: Feb 04, 2005 Installing Routines:

Feb 05, 2005@16:22:47

Running Pre-Install Routine: PRE^PXRMWHPI Installing Data Dictionaries:

Feb 05, 2005@16:22:49

Installing Data:

Feb 05, 2005@16:22:51

Running Post-Install Routine: POST^PXRMWHPI Installing reminder VA-WH MAMMOGRAM REVIEW RESULTS

ADDITIONAL FINDING entry Q.WH BREAST ULTRASOUND - UNILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH BREAST ULTRASOUND - BILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH MAMMOGRAM - UNILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

Installing reminder VA-WH MAMMOGRAM SCREENING

Finding RP.MAMMOGRAM BILAT SCREEN does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: **chest**

1. chest 2 views pa&amp;lat	CHEST 2 VIEWS PA&amp;LAT	(RAD	Detailed) CPT:71020
2. chest 4 views	CHEST 4 VIEWS	(RAD	Detailed) CPT:71030
3. chest apical lordotic	CHEST APICAL LORDOTIC	(RAD	Detailed) CPT:71021
4. chest include fluoro	CHEST INCLUDE FLUORO	(RAD	Detailed) CPT:71034
5. chest oblique projections	CHEST OBLIQUE PROJECTIONS	(RAD	Detailed) CPT:71022

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **1** CHEST 2 VIEWS PA&amp;LAT	(RAD	Detailed) CPT:71020

Finding RP.MAMMOGRAM BILAT SCREEN does not exist; input a replacement or ^ to quit the install.

Select RAD/NUC MED PROCEDURES NAME: **chest**

1. chest 2 views pa&amp;lat	CHEST 2 VIEWS PA&amp;LAT	(RAD	Detailed) CPT:71020
2. chest 4 views	CHEST 4 VIEWS	(RAD	Detailed) CPT:71030
3. chest apical lordotic	CHEST APICAL LORDOTIC	(RAD	Detailed) CPT:71021
4. chest include fluoro	CHEST INCLUDE FLUORO	(RAD	Detailed) CPT:71034

1. chest oblique projections	CHEST OBLIQUE PROJECTIONS	(RAD	Detailed) CPT:71022

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **2** CHEST 4 VIEWS	(RAD	Detailed) CPT:71030 ADDITIONAL FINDING entry Q.WH REFER TO WOMEN'S HEALTH CLINIC does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH MAMMOGRAM - UNILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

Installing reminder VA-WH PAP SMEAR REVIEW RESULTS

ADDITIONAL FINDING entry Q.WH CERVICAL ORDERS	does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

ADDITIONAL FINDING entry Q.WH PAP SMEAR REPEAT CONSULT does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

Installing reminder VA-WH PAP SMEAR SCREENING

FINDING entry Q.WH REFER TO WOMEN'S HEALTH CLINIC does not exist.

Select one of the following:

D	Delete (from the reminder/dialog)

P	Replace (in the reminder/dialog) with an existing entry Q	Quit the install

Enter response: **p** Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: **zzPRE-OP**

UPDATING FORCE VALUE: PXRM WH UPDATE TREATMENT NEED UPDATING FORCE VALUE: PXRM WH NOTIFICATION TYPE

Updating Routine file... Updating KIDS files...

PXRM*2.0*1 Installed.

Feb 05, 2005@16:23:37

Install Message sent #435 Install Completed

## Appendix B: Key Points to WH Reminders Installation and Setup

###### 3 PAP and Mammogram screening and review reminders will be installed as part of the patch.

1. The Screening reminders replace prior national screening reminders
2. All four reminders have new dialogs to assist with data entry

1. To satisfy the PAP smear screening reminder, completed PAP Smears must be recorded in the patient record as one of the following:
    1. Laboratory package Cytology or Surgical Pathology SNOMED results
    2. Women's Health package procedure with results
    3. Health Factor (Historical outside results)
    4. PCE CPT procedure code
    5. Completed consult order for outside procedure

1. To satisfy the mammogram screening reminder, completed mammograms must be recorded in the patient record as one of the following:
    1. Verified results in the Radiology package
    2. Women's Health package procedure with results
    3. Health Factor (Historical outside results)
    4. PCE CPT procedure code
    5. Completed consult order for outside procedure

1. PAP review reminder will only come due if:
    1. WH is automatically updated with procedure results from the VistA Lab package
    2. If this does not take place, do not release the PAP review reminder

1. Mammogram review reminder will only come due if:
    1. WH is automatically updated with procedure results from the VistA Radiology package &amp; status for imported mammograms is set to “OPEN”
    2. If this does not take place, do not release the Mammogram review reminder

1. If your site does not record PAP smear results in the VistA Lab package:
    1. You could change procedures at your site so PAP smear results are entered into the VistA Lab package
    2. Recording and verifying/releasing results in the VistA Lab package will automatically satisfy the PAP screening reminder
    3. Recording results in the WH package will automatically satisfy the PAP screening reminder
    4. Automatically updating WH from the Vista Lab package will allow sites to use the PAP Review reminder
    5. If your site does not automatically update WH from Lab, the PAP smear review reminder will not come due, and you might choose not to release it.

1. If your site does not record mammogram results in the VistA Radiology package:
    1. You could change procedures at your site so mammogram results are entered into the VistA Radiology package
    2. Recording and verifying results in the VistA Radiology package will automatically satisfy the mammogram screening reminder
    3. Recording results in the WH package will automatically satisfy the mammogram screening reminder
    4. Automatically updating WH from the Vista Radiology package will allow sites to use the mammogram review reminder.
    5. If your site does not automatically update WH from Radiology, the mammogram review reminder will not come due, and you might choose not to release it.

1. Apply updates to WV NOTIFICATION PURPOSE file before installing reminders:
    1. Several new entries created to work with the screening and review reminders
    2. Review reminders reference these entries and will be resolved if they have been added to the file
    3. Sites will have to go back after the install and manually enter each item into the dialogs if the file is not updated first,

1. Update Notification boilerplate text with your site address and content:
    1. If necessary, edit your WH default notification letter so it contains your site’s address and phone number
    2. Copy your default WH notification into each of the new notifications and customize the text of each new notification to fit the needs of your site, using WH option “AEP -Add/Edit a Notification Purpose &amp; Letter”
    3. Once you set up the letter you want, respond with “NO” when asked if you want to replace the custom letter with the default letter

1. For the new Lab computed finding to work, sites must use the WH option

“PAP-Link Pap Smear with SNOMED Codes” to map Lab SNOMED codes to WH

1. New Functional Finding logic is used to alter reminder frequency, so frequency is not specified on the findings.

1. Enable new alerts through CPRS Manager menu, so that informational alerts about lab pap smears and radiology mammogram results are sent to clinicians.

## Appendix C: Reminders Installation with Reminder Exchange Utility

The post-install routine, POST^PXRMV2I, installs the packed reminders into your Exchange File. If you discover that the reminder didn’t get installed, you can use the Exchange options on the Reminders Manager Menu to install the “packed” reminders. The following examples can guide you in doing this.

1. Select Reminder Exchange from the Reminder Managers Menu. From the Reminder Exchange actions, select IFE for the reminder that contains the dialog that is not installed. You may need to press enter one or more times (or use the Search List action) to locate the correct entry.

| Clinical Reminder Exchange	Jul 15, 2004@13:32:42	Page:	1 of	8  Exchange File Entries.  Entry	Source	Date Packed  1. AGP DIALOG GROUP TEST	CRPROVIDER@SALT LAKE	07/01/2004@11:00:03 2. AGP INSTALL TEST	CRPROVIDER@SALT LAKE	06/30/2004@12:55:48 3. BDI II RESULT GROUP	CRPROVIDER@SALT LAKE	04/13/2004@15:53:47 4. CDUE	CRPROVIDER@SALT LAKE	08/08/2003@10:59:52 5. CHA UNVESTED PATIENTS	CRUSER@CHARLESTON,S	09/26/2001@13:00:59 6. CODE SET TEST	CRPROVIDER@SALT LAKE	06/26/2003@12:17:02 7. CONDTEST	CRPROVIDER@SALT LAKE	08/18/2003@12:02:18 8. Dialog Transport Reminder	CRUSER@DURHAM	12/16/2002@15:37:51 9. FFTEST	CRPROVIDER@SALT LAKE	09/10/2003@15:14:21 10. GMTSMHV	CRPROVIDER@SALT LAKE	07/06/2004@15:06:21   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CFE	Create Exchange File Entry	IH	Installation History CHF	Create Host File	LHF	Load Host File  CMM	Create MailMan Message	LMM	Load MailMan Message  DFE	Delete Exchange File Entry	LR	List Reminder Definitions IFE	Install Exchange File Entry	RI	Reminder Definition Inquiry Select Action: Next Screen//  **IFE**                                                                                                                                                                                                                                                                                                                                                                                                     |

1. When you are prompted for the entry number, select the number for the dialog.

| Clinical Reminder Exchange	Jul 15, 2004@13:36:59      | Clinical Reminder Exchange	Jul 15, 2004@13:36:59      | Clinical Reminder Exchange	Jul 15, 2004@13:36:59      | Clinical Reminder Exchange	Jul 15, 2004@13:36:59      | Page:	8 of	8                                          |
|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Exchange File Entries.                                | Exchange File Entries.                                | Exchange File Entries.                                | Exchange File Entries.                                |                                                       |
| +	Entry	Source                                        | +	Entry	Source                                        | +	Entry	Source                                        | +	Entry	Source                                        | Date Packed                                           |
| 45	TIU*1*112 20040325	CRDeveloper@ALBANY              | 45	TIU*1*112 20040325	CRDeveloper@ALBANY              | 45	TIU*1*112 20040325	CRDeveloper@ALBANY              | 45	TIU*1*112 20040325	CRDeveloper@ALBANY              | 03/25/2004@14:20:47                                   |
| 46	TIU512 TEST	CRPROVIDER@SALT LAKE                   | 46	TIU512 TEST	CRPROVIDER@SALT LAKE                   | 46	TIU512 TEST	CRPROVIDER@SALT LAKE                   | 46	TIU512 TEST	CRPROVIDER@SALT LAKE                   | 07/26/2002@06:48:34                                   |
| 47	VA-*IHD 412 ELEVATED LDL RE	CRPROVIDER@SALT LAKE   | 47	VA-*IHD 412 ELEVATED LDL RE	CRPROVIDER@SALT LAKE   | 47	VA-*IHD 412 ELEVATED LDL RE	CRPROVIDER@SALT LAKE   | 47	VA-*IHD 412 ELEVATED LDL RE	CRPROVIDER@SALT LAKE   | 05/11/2004@11:30:33                                   |
| 48	VA-*IHD 412 LIPID PROFILE R	CRPROVIDER@SALT LAKE   | 48	VA-*IHD 412 LIPID PROFILE R	CRPROVIDER@SALT LAKE   | 48	VA-*IHD 412 LIPID PROFILE R	CRPROVIDER@SALT LAKE   | 48	VA-*IHD 412 LIPID PROFILE R	CRPROVIDER@SALT LAKE   | 05/11/2004@11:32:04                                   |
| 49	VA-*IHD ELEVATED LDL REPORT	CRPROVIDER@SALT LAKE   | 49	VA-*IHD ELEVATED LDL REPORT	CRPROVIDER@SALT LAKE   | 49	VA-*IHD ELEVATED LDL REPORT	CRPROVIDER@SALT LAKE   | 49	VA-*IHD ELEVATED LDL REPORT	CRPROVIDER@SALT LAKE   | 05/11/2004@11:27:07                                   |
| 50	VA-*IHD LIPID PROFILE REPOR	CRPROVIDER@SALT LAKE   | 50	VA-*IHD LIPID PROFILE REPOR	CRPROVIDER@SALT LAKE   | 50	VA-*IHD LIPID PROFILE REPOR	CRPROVIDER@SALT LAKE   | 50	VA-*IHD LIPID PROFILE REPOR	CRPROVIDER@SALT LAKE   | 05/11/2004@11:28:42                                   |
|                                                       | **+ Next Screen	- Prev Screen**                       |                                                       | **?? More Actions**                                   |                                                       |
| CFE                                                   | Create Exchange File Entry                            | IH                                                    | Installation History                                  | Installation History                                  |
| CHF	Create Host File	LHF	Load Host File               | CHF	Create Host File	LHF	Load Host File               | CHF	Create Host File	LHF	Load Host File               | CHF	Create Host File	LHF	Load Host File               | CHF	Create Host File	LHF	Load Host File               |
| CMM	Create MailMan Message	LMM	Load MailMan Message   | CMM	Create MailMan Message	LMM	Load MailMan Message   | CMM	Create MailMan Message	LMM	Load MailMan Message   | CMM	Create MailMan Message	LMM	Load MailMan Message   | CMM	Create MailMan Message	LMM	Load MailMan Message   |
| DFE                                                   | Delete Exchange File Entry                            | LR                                                    | List Reminder Definitions                             | List Reminder Definitions                             |
| IFE                                                   | Install Exchange File Entry                           | RI                                                    | Reminder Definition Inquiry                           | Reminder Definition Inquiry                           |
| Select Action: Quit// IFE	Install Exchange File Entry | Select Action: Quit// IFE	Install Exchange File Entry | Select Action: Quit// IFE	Install Exchange File Entry | Select Action: Quit// IFE	Install Exchange File Entry | Select Action: Quit// IFE	Install Exchange File Entry |
| Select Entry(s):	(45-50):  **47**                     |                                                       |                                                       |                                                       |                                                       |

1. When the dialog screen comes up select IA.

| Exchange File Components	Jul 15, 2004@13:46:52	Page:	1 of	4  Component	Category	Exists  Reminder:	VA-*IHD 412 ELEVATED LDL REPORTING Source:	CRPROVIDER,THREE at SALT LAKE CITY OIFO  Date Packed: 05/11/2004@11:30:33  Description:  Compliance reporting measures the management of IHD patients with an ICD-9 412.nn diagnosis, whose most recent LDL is greater than or equal to 120mg/dl as defined by the VA External Peer Review Program (EPRP) performance measure and the maximum guideline recommended below:  The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends an LDL goal of &lt;120 mg/dl for patients with Ischemic Heart Disease; and the NCEP Adult Treatment Panel II recommends a more stringent goal of &lt;100 mg/dl.  This national IHD 412 Elevated LDL Reporting reminder is used monthly   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	Enter ?? for more actions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| IA	Install all Components	IS	Install Selected Component Select Action: Next Screen//  **IA**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

1. If you are prompted for items that are missing, either replace or delete the item. Do not select quit. This should install the dialog.

**Appendix D: WV*1*16 Description**

DHCP Patch Display	Page: 1

=============================================================================

Run Date: SEP 30, 2004	Designation: WV*1*16	TEST v9

Package : WOMEN'S HEALTH	Priority	: MANDATORY

Version : 1	Status	: UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)WV*1*9	&lt;&lt;= must be installed BEFORE `WV*1*16' (v)WV*1*10		&lt;&lt;= must be installed BEFORE `WV*1*16' (v)WV*1*15		&lt;&lt;= must be installed BEFORE `WV*1*16' (v)WV*1*17		&lt;&lt;= must be installed BEFORE `WV*1*16'

Subject: WH-CLINICAL REMINDERS LINK

Category:	ROUTINE

DATA DICTIONARY ENHANCEMENT OTHER INFORMATIONAL

Description:

===========

Associated NOIS: &lt;None&gt; Associated E3Rs: 18684

Test Sites:

===========

Northern California HCS Loma Linda

Washington D.C.

This patch is part of a multi-KIDS build that includes PXRM*2*1 (Clinical Reminders), LR*5.2*311 (Laboratory) and OR*3*210 (CPRS). Please see the patch description for PXRM*2*1 for information on retrieving the host file containing these patches.

The Technical Integration approval has been received for the data dictionary changes.

This patch is an enhancement. It adds functionality that allows the Women's Health (WH) package to send data to the Clinical Reminders (CR) package to resolve Mammogram and Pap Smear reminders. Also, the CR package will be able to send data to the WH package to update the WH database.

1. The following APIs are added:

1. GETPARAM^WVSITE returns WH site parameters for the facility indicated. It is documented in Integration Agreement (IA) 4101.

GETPARAM(.RESULT,IEN)

Input:

.RESULT = Array name to return data in. (Required) IEN = INSTITUTION file (#4) IEN. (Required)

Output:

RESULT(0)=1st piece is 1 (for Success) or -1 (Failure) 2nd piece is the reason for failure

RESULT(1)=1st piece is 1 (for Yes) or 0 (for No or null).

This is the value of the UPDATE RESULTS/DX (#.11) field in the WV SITE PARAMETER (#790.02) file.

2nd piece is 1 (for Yes) or 0 (for No or null).

This is the value of the UPDATE TREATMENT NEEDS (#.12) field in the WV SITE PARAMETER (#790.02) file.

Example:

- D GETPARAM(.RESULT,499) ZW RESULT
- RESULT(0)=1^
- RESULT(1)=1^1

1. RESULTS^WVALERTS returns an array with data for the WV PROCEDURE (#790.1) file entry specified. It is documented in IA 4102.

RESULTS(.RESULT,IEN)

Input:

.RESULT = Array name to return data in. (Required)

IEN = The internal entry number of a WV PROCEDURE (#790.1) file entry. (Required)

Output:

RESULT(0) = piece1^piece2^piece3^piece4^piece5^piece6^piece7^piece8

^piece9^piece10

where:	piece1 = WV PROCEDURE (#790.1) file entry number piece2 = patient DFN

piece3 = 'Breast Ultrasound', 'Mammogram' or 'Pap Smear' piece4 = Date of procedure (FileMan internal format) piece5 = Radiology procedure name

piece6 = Primary radiology diagnosis

piece7 = One or more radiology modifiers separated by tildes (~)

piece8 = Lab package test date (external format) piece9 = Lab accession number

piece10 = Lab specimen text

If the entry is not found, piece 1 will contain '-1' and piece 3 will contain an error message.

If the entry is a Pap Smear, then pieces 5 through 7 are null.

If the entry is a Mammogram or Breast Ultrasound, then pieces 8 through 10 are not returned.

Example of a Pap Smear:

- D RESULTS(.RESULT,313) ZW RESULT
- RESULT(0)=313^94^Pap Smear^3030131^^^^01/31/2003^CY 03 6^PAP SMEAR

Example of a Mammogram:

- D RESULTS(.RESULT,314) ZW RESULT

- RESULT(0)=314^94^Mammogram^3030321^MAMMOGRAM SCREENING^NORMAL

^LEFT~RIGHT

1. LETTER^WVRPCNO1 returns the letter text for the WV NOTIFICATION PURPOSE (#790.404) file entry specified. It is documented in IA 4103.

LETTER(.RESULT,IEN)

Input:

.RESULT = Array name to return data in. (Required)

IEN = WV NOTIFICATION PURPOSE (#790.404) file IEN. (Required)

Output:

RESULT(0) = Blank if the entry exists	&lt;OR&gt; -1^error message RESULT(n) = Lines of letter text where 'n' is a sequential number

Example:

- D LETTER(.RESULT,1) ZW RESULT
- RESULT(0)=
- RESULT(1)=
- RESULT(2)=
- RESULT(3)=	Women's Health Clinic
- RESULT(4)=
- RESULT(5)=	123 Main Street
- RESULT(6)=
- RESULT(7)=	CHICAGO, IL 60612
- RESULT(n)= ...

1. NEW^WVRPCNO is used to update a procedure result in File 790.1, create a notification entry in FILE 790.4, print a notification and update a patient's treatment needs. It is documented in IA 4104.

NEW(.RESULT,.NOTIF)

Input:

RESULT = This is an array that identifies what FILE 790.1 entries will be updated and the result code to use. (Optional) RESULT(n)=FILE 790.1 IEN^"A", "N" or "U"

Where: n is a number greater than zero.

The first piece is the WV PROCEDURE (790.1) file IEN.

The second piece is a one character code that identifies the diagnosis. 'A' stands for Abnormal, 'N' stands for Normal and 'U' stands for Unsatisfactory (e.g., 1234^N).

NOTIF = This is an array that identifies the notification purposes to use to create entries in the WV NOTIFICATION (790.4) file. (Optional)

NOTIF(FILE 790.404 IEN,n) = FILE 790.1 IEN^Type^FILE 3.5

NAME^DFN

Where: The first array subscript is a FILE 790.404 internal entry number (IEN).

The second subscript is a sequential number starting with 1.

The first piece of data in the node is the FILE

790.1 IEN which identifies the procedure performed.

The second piece is a one character code that identifies the type of notification. 'I' stands for In-person, 'L' stands for Letter and 'P' stands for "Phone".

The third piece identifies the print device. It consists of the FILE 3.5 IEN, a semi-colon and the .01 value of the entry (e.g., 5;HPLASERJET).

The fourth piece is the patient IEN (i.e., DFN) from FILE 2.

Output: A notification letter for a patient may be printed based on the input parameter values. However, no values are sent back to the calling routine.

Example:

- S RESULT(1)="313^N"
- S NOTIF(20,1)="313^L^5;HPLASERJET^94"
- D NEW(.RESULT,.NOTIF)

One new field is added to the WV PROCEDURE (#790.1) file. It is:

.16 PROCESSED Y/N?

1. LATEST^WVRPCPR returns a list of entries for Pap Smear, Mammogram or Breast Ultrasound in reverse chronological order for the search criteria identified in the input parameters. It is documented in IA 4105.

LATEST(.RESULT,DFN,TYPE,DATES,MAX,DX)

Input:

.RESULT = Array name for return values. (Required) DFN = Patient DFN. (Required)

TYPE = A set of codes where "P" stands for Pap Smear, "M" for Mammogram or "U" for Breast Ultrasound. (Required)

DATES = A date range in FileMan internal format separated by an uparrow (e.g., 3020101^3021231). (Optional).

The default is the previous 3 years.

MAX = The maximum number of entries to return. (Optional) The default value is 10.

DX = A set of codes that identify a category of results where "N" stands for Normal, "A" stands for Abnormal, "P" stands for Pending and "*" (asterisk) stands for everything. (Optional)

The default is "*". It returns entries that

are marked as "Unsatisfactory for DX" as well as Normal, Abnormal and Pending.

Output:

RESULT(0) = Number of matches

RESULT(n) = IEN^DFN^DATE^TYPE^DX CATEGORY^DX Result^RAD/LAB link

^STATUS

where		n = A sequential number starting with 1 IEN = FILE 790.1 internal entry number

DFN = FILE 2 internal entry number

DATE = Procedure date in FileMan format TYPE = Procedure name (from FILE 790.2)

DX Category = 'Normal', 'Abnormal' or 'Pending' DX Result = FILE 790.31, Field .01 value

RAD/LAB LINK = 0 stands for no link to radiology

or lab package

1 stands for link to radiology or lab package

STATUS = FILE 790.1 entry status. 'OPEN' or 'CLOSED'

If no matches were found, RESULT(0)=-1^error message.

Example:

- D LATEST(.RESULT,94,"M","3030101^3031231",10,"*") ZW RESULT
- RESULT(0)=1^
- RESULT(1)=314^94^3030321^MAMMOGRAM SCREENING^Normal^Negative^1^OPEN

1. RESULTS^WVALERTF returns any report text for a pap smear, mammogram or breast ultrasound for the WV PROCEDURE (#790.1) file entry identified. It is documented in IA 4106.

RESULTS(.RESULT,IEN)

Input:

RESULT = Array name that will identify the global reference containing the report text (Required).

IEN = The internal entry number of the FILE 790.1 entry to return data on (Required).

Output:

^TMP("WV RPT",$J,n,0) = report text

where n is a sequential number starting with 1.

If the entry is not found, the first node of the global array is returned with a '-1' in the first piece and an error message

in the third piece:

^TMP("WV RPT",557902502,1,0) = -1^^Entry not found.

Example of report text found:

- D RESULTS(.RESULT,313) ZW RESULT
- RESULT=^TMP("WV RPT",557902502)
- D ^%G
- ^TMP("WV RPT",557902502,1,0) =	DAY-CASE #: 032103-1515
- ^TMP("WV RPT",557902502,2,0) =	EXAM DATE/TIME: MAR 21, 2003@13:30
- ^TMP("WV RPT",557902502,3,0) = VERIFYING PHYSICIAN: TAYLOR,FRANK
- ^TMP("WV RPT",557902502,4,0) =	PROCEDURE: MAMMOGRAM SCREENING
- ...
- ...

1. A new option, Link Pap Smear with SNOMED Codes [WV PAP SMEAR SNOMED CODES], is added to the File Maintenance Menu [WV MENU-FILE MAINTENANCE]. With this option facilities can identify SNOMED codes used by their Lab Service when coding a Lab test that is a Pap Smear. The SNOMED codes

identified here can be matched to the SNOMED codes used in a Lab report to determine if that test is a Pap Smear. Currently, the WH user must look at the lab test and decide whether the lab test is a pap smear. After this patch is installed and the SNOMED codes are entered here, the WH software can make that determination automatically.

Several new fields are added to the WV PROCEDURE TYPE (#790.2) file. They are: 1	MORPHOLOGY SNOMED CODE (subfile #790.21)

.01 MORPHOLOGY SNOMED CODE

1	DIAGNOSIS

2	TOPOGRAPHY SNOMED CODE (subfile #790.22)

.01 TOPOGRAPHY SNOMED CODE

1. The Edit Site Parameters [WV EDIT SITE PARAMETERS] option is modified to add two new prompts:

1. "Update Result/Dx Field?:" - If set to YES, the data sent from CR will be used to update the patient's procedure data in FILE 790.1. If set to NO or null, no updating will be done.

The value for this response is stored in a new field, UPDATE RESULTS/DX (.11), in the WV SITE PARAMETER (#790.02) file.

1. "Update Treatment Needs?:" - If set to YES, the data sent from CR will be used to update the patient's treatment needs in FILE 790. If set to NO or null, no updating will be done.

The value for this response is stored in a new field, UPDATE TREATMENT NEEDS (.12), in the WV SITE PARAMETER (#790.02) file.

1. The Add/Edit a Notification Purpose &amp; Letter [WV ADD/EDIT NOT PURPOSE&amp;LETTER] option is modified to add four new prompts:

1. "Breast Treatment Need:" - This prompt is for a new field, BR

TX NEED (.07), in the WV NOTIFICATION PURPOSE (#790.404) file. This

field points to FILE 790.51 and shows the choices related to breast treatment needs.

1. "Breast Treatment Due Date:" - This prompt is for a new field, BR TX DUE DATE (.08), in the WV NOTIFICATION PURPOSE (#790.404) file. This field is the amount of time to add to a procedure

date or the current date to calculate a new breast treatment due date. The value should be a number followed by "D", "M" or "Y" (without the quotes). D indicates days. M indicates months. Y indicates years. For example, "90D" means add 90 days to the procedure date or current date to calculate the new breast treatment due date. This new treatment date will be automatically assigned to the patient in the WV PATIENT file (#790).

1. "Cervical Treatment Need:" - This prompt is for a new field, CX

TX NEED (.09), in the WV NOTIFICATION PURPOSE (#790.404) file. This

field points to FILE 790.5 and shows the choices related to cervical treatment needs.

1. "Cervical Treatment Due Date:" - This prompt is for a new field, CX TX DUE DATE (.1), in the WV NOTIFICATION PURPOSE (#790.404) file. This field is the amount of time to add to procedure date or the current date to calculate a new cervical treatment due date. The value should be a number followed by "D", "M" or "Y" (without the quotes). D indicates days. M indicates months. Y indicates years. For example, "90D" means add 90 days to the procedure date or current date to calculate the new cervical treatment due date. This new treatment date will be automatically assigned to the patient in the WV PATIENT file (#790).

If the "Update Treatment Needs?" parameter (3b above) is set to Yes and there are values in fields a-d, the software will use these values to update the patient's treatment needs in the WV PATIENT (#790) file.

1. The Print Notification Purpose &amp; Letter File [WV PRINT NOTIF PURPOSE&amp;LETTER] option is modified to display in the report output the values of the four new fields identified in #4 above.

1. The following new entries are added to the WV NOTIFICATION PURPOSE (#790.404) file:

CPRS UPDATE PAP TX NEED 4M CPRS UPDATE PAP TX NEED 6M CPRS UPDATE PAP TX NEED 3Y CPRS UPDATE PAP TX NEED 2Y CPRS UPDATE PAP TX NEED 1Y CPRS UPDATE MAM TX NEED 1Y CPRS UPDATE MAM TX NEED 2Y CPRS UPDATE MAM TX NEED 6M CPRS UPDATE MAM TX NEED 4M

MAM result NEM, next MAM 1Y MAM result NEM, next MAM 2Y MAM result NEM, next MAM 4M MAM result NEM, next MAM 6M

MAM result abnormal, F/U MAM 4M MAM result abnormal, F/U MAM 6M PAP result NEM, next PAP 1Y

PAP result NEM, next PAP 2Y PAP result NEM, next PAP 3Y PAP result NEM, next PAP 4M PAP result NEM, next PAP 6M

PAP result abnormal, F/U PAP 4M PAP result abnormal, F/U PAP 6M MAM unsatisfactory, need repeat Pap unsatisfactory, need repeat

PAP result NEM, further screening not required MAM result NEM, further screening not required

Facilities may customize these entries and use them when resolving Pap Smears and Mammograms or continue to use the entries they created locally. Use the Add/Edit a Notification Purpose &amp; Letter [WV ADD/EDIT NOT PURPOSE&amp;LETTER] option to customize these new entries.

1. The following entries are added or modified in the WV RESULTS/DIAGNOSIS (#790.31) file:

1. No Evidence of Malignancy - This is a new entry that can be used to result a mammogram, pap smear or breast ultrasound.
2. Abnormal - This is a new entry that can be used to result a mammogram, pap smear or breast ultrasound.
3. Unsatisfactory for DX - This is an existing entry that is modified to result a breast ultrasound, too.

1. A new-style Index is added to the WV PROCEDURE (#790.1) file. The 'AC' index will provide a quicker search for entries needed by CR. A post-installation routine will index the existing entries in the file. The format of the index node is: ^WV(790.1,"AC",DFN,DATE,DA)=""

where: DFN = is the FILE 2 IEN of the patient

DATE = the date of procedure (FileMan internal format) DA = the FILE 790.1 IEN

1. Before this patch, a mail message was sent to the patient's WH Case Manager when a mammogram was added to the WH database by the link with the Radiology/NM package or when a lab report was verified by the Lab package.

After this patch is installed, the WH package will tell the CPRS package to send a CPRS alert notification to the WH Case Manager and to the provider associated with the procedure.

## Appendix E: Setting up Notification Letters

#### Step 1 – Edit default letter (one time only)

###### Use FileMan to edit the default WH letter template in WV LETTER file #790.6. Edit all the parts that will be common to all letters:

Site address

Site phone number Greeting Signature

WH looks for the name GENERIC SAMPLE LETTER.

###### This should be done by a CAC or ADPAC, not by the end user.

&gt;&gt; **D P^DI**

VA FileMan 22.0

Select OPTION: 1	ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: WV LETTER//

EDIT WHICH FIELD: ALL//

Note: This site has more than one default letter, but WH will only use the one named GENERIC SAMPLE LETTER.

Select WV LETTER: **?**

Answer with WV LETTER Choose from:

GENERIC SAMPLE LETTER

OLD GENERIC SAMPLE LETTER TEST GENERIC LETTER

You may enter a new WV LETTER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH PUNCTUATION

Note: The letter templates contain objects that will be used to pull in patient information. This text is from page 2.3 of the WH User Manual:

The patient’s name, address, and SSN will appear automatically within the letter at the places demarcated by the vertical bars “||” (e.g., |SSN|) when the letter is printed. This information is obtained from the WV PATIENT file (#790). If you do not wish to have a certain piece of information displayed in the letter, you should edit the text of the letter and remove that field name (e.g., SSN) and the vertical bars that surround it.

Other information that appears in the letter is the clinic name and address. This information is typed within quotes. You should edit the text between the quotes to display the correct clinic name and address (Note: Leave the quotes). If you plan on printing your letters on paper that

contains a letterhead you will want to remove altogether the lines containing the clinic name and address.

The field |NOWRAP| should be left as is. This permits the text of the letter to be printed as it appears on the terminal screen. Other fields may be deleted if not desired. For example,

|TODAY| and |NOW| will print out the current date and date/time respectively. Future appointments may be included to print in a notification letter by typing the text “|APPOINTMENTS|” (without the quotes) in the text of the letter.

Because of the specific syntax of the fields and the possibility of corrupting them during edits, a recovery utility has been provided. The program to edit a purpose of notification always asks first if you wish to replace the existing form letter with a ‘generic sample letter’. Answering ‘Yes’ to that question will replace the existing form with a generic sample letter, which includes all of the original fields in their proper syntax.

Select WV LETTER: **generIC SAMPLE LETTER**

LETTER: GENERIC SAMPLE LETTER	Replace

LETTER TEXT:. . .

. . .

Person’s Name, title Your clinic

Your phone number: nnn-nnnn

printed: |NOW| Edit? NO// **y	YES**

Note: Now editing GENERIC SAMPLE LETTER – change items that are highlighted Before the default GENERIC SAMPLE LETTER is edited:

==[ WRAP ]==[ INSERT ]=============&lt; LETTER TEXT &gt;===========[ &lt;PF1&gt;H=Help ]====

|NOWRAP|

|CENTER(" **Women's Health Clinic** ")|

|CENTER(" **Your Street** ")|

|CENTER(" **Your City, ST	Zip Code** ")|

|TODAY|

|$E(SSN#,6,9)|

|$P(NAME,",",2)| |$P(NAME,",")|

|COMPLETE ADDRESS|

- -	- -

Dear Ms. |$P(NAME,",",1)|,

This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

Sincerely,

###### Person’s Name, title Your clinic

**Your phone number: nnn-nnnn**

printed: |NOW|

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

After the default GENERIC SAMPLE LETTER has been edited:

==[ WRAP ]==[ INSERT ]=============&lt; LETTER TEXT &gt;===========[ &lt;PF1&gt;H=Help ]====

|NOWRAP|

|CENTER(" **Women's Health Clinic** ")|

|CENTER(" **123 Clinic Street** ")|

|CENTER(" **Clinic City, SS	77777** ")|

|TODAY|

|$E(SSN#,6,9)|

|$P(NAME,",",2)| |$P(NAME,",")|

|COMPLETE ADDRESS|

- -	- -

Dear Ms. |$P(NAME,",",1)|,

This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

Sincerely,

###### WHNURSE, ONE, LPN

**Women's Health Program Phone: 777-7777**

printed: |NOW|

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

#### Step 2 – Edit/customize each individual notification letter (at least one time for each letter)

Use the WH option **AEP	Add/Edit a Notification Purpose &amp; Letter** to edit each individual notification letter in the WV NOTIFICATION PURPOSE file # 790.404.

###### MF	Manager's Functions ...

FM	File Maintenance Menu ...

AEP	Add/Edit a Notification Purpose &amp; Letter

Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

Enter Yes or No: NO//

Reply “YES” to this question the first time you edit each individual notification letter, to copy the GENERIC SAMPLE LETTER from WV LETTER file into the letter you are editing. When you save the customized letter, it will be saved in the WV NOTIFICATION PURPOSE file.

Reply “NO” to this question if you need to further customize a letter that has already been customized. Otherwise, by replying “YES” again, you will replace the customized letter with the default letter and lose all your former customized text. This may be desirable if some of the special coding has been corrupted and needs to be replaced so the letter will pull in the patient data correctly.

DVF,DEV&gt; **D ^XUP**

Select OPTION NAME: **women'S HEALTH MENU	WVMENU** Women's Health Menu	menu Women's Health Main Menu v1.0			SALT LAKE CITY HCS

PM	Patient Management ... MR	Management Reports ... MF	Manager's Functions ...

Select Women's Health Menu Option: **mf	Manager's Functions**

WOMEN'S HEALTH:	*	MANAGER'S FUNCTIONS	*	SALT LAKE CITY HCS

FM	File Maintenance Menu ... PQ	Print Queued Letters

MPM	Manager's Patient Management ... LDE	Lab Data Entry Menu ...

Select Manager's Functions Option: fm **File Maintenance Menu**

WOMEN'S HEALTH:	*	FILE MAINTENANCE MENU	*	SALT LAKE CITY HCS

AEP Add/Edit a Notification Purpose &amp; Letter PPL Print Notification Purpose &amp; Letter File ESN Edit Synonyms for Notification Types

OUT Add/Edit Notification Outcomes ESP Edit Site Parameters

CM Add/Edit Case Managers

TR	Transfer a Case Manager's Patients AUTO	Automatically Load Patients

RAD	Import Radiology/NM Exams PRD	Print Results/Diagnosis File

ESR	Edit Synonyms for Results/Diagnoses PSR	Print Synonyms for Results/Diagnoses EDX	Edit Diagnostic Code Translation File PDX	Print Diagnostic Code Translation File RS	Add/Edit to Referral Source File

PAP	Link Pap Smear with SNOMED Codes

Select File Maintenance Menu Option: **aep	Add/Edit a Notification Purpose &amp; Letter**

* * *	WOMEN'S HEALTH: EDIT NOTIFICATION PURPOSE &amp; LETTER FILE	* * *

Select WV NOTIFICATION PURPOSE: **pap result nem**

1. PAP RESULT NEM, FURTHER SCREEN	PAP result NEM, further screening not r equired		ROUTINE
2. PAP RESULT NEM, NEXT PAP 1Y	PAP result NEM, next PAP 1Y	PN1Y	ROUTI

NE

1. PAP RESULT NEM, NEXT PAP 2Y	PAP result NEM, next PAP 2Y	PN2Y	ROUTI

NE

1. PAP RESULT NEM, NEXT PAP 3Y	PAP result NEM, next PAP 3Y	PN3Y	ROUTI

NE

1. PAP RESULT NEM, NEXT PAP 4M	PAP result NEM, next PAP 4M	PN4M	ROUTI

NE

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR CHOOSE 1-5: **2	PAP result NEM, next PAP 1Y	PN1Y	ROUTINE**

First edit: Enter “YES” to copy the GENERIC SAMPLE LETTER to start a brand new letter or to replace an existing letter

Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

Enter Yes or No: NO// **YES**

Additional edits: Enter “NO” if you want to edit the text of an existing letter and DO NOT want to replace existing letter content with the GENERIC SAMPLE LETTER:

Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

Enter Yes or No: NO// **NO**

Tab to the FORM LETTER (WP) field and hit RETURN key:

* * *	EDIT NOTIFICATION PURPOSE &amp; LETTER	* * *

Purpose of Notification: PAP result NEM, next PAP 1Y

Active: YES Synonym: PN1Y

Priority: ROUTINE	FORM LETTER (WP): **+**

Result or Reminder Letter: RESULT Associate with BR or CX Tx: CERVICAL

Breast Treatment Need: Breast Treatment Due Date:

Cervical Treatment Need: Routine PAP

Cervical Treatment Due Date: 1Y

After the GENERIC SAMPLE LETTER has been copied into the FORM LETTER for the

**PAP result NEM, next PAP 1Y notification** letter and before this individual notification letter has been customized:

==[ WRAP ]==[ INSERT ]=============&lt; LETTER TEXT &gt;===========[ &lt;PF1&gt;H=Help ]====

|NOWRAP|

|CENTER("Women's Health Clinic")|

|CENTER("123 Clinic Street")|

|CENTER("Clinic City, SS	77777")|

|TODAY|

|$E(SSN#,6,9)|

|$P(NAME,",",2)| |$P(NAME,",")|

|COMPLETE ADDRESS|

- -	- -

Dear Ms. |$P(NAME,",",1)|,

###### This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

Sincerely,

WHNURSE, ONE, LPN

Women's Health Program Phone: 777-7777

printed: |NOW|

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

After the individual notification letter has been customized:

==[ WRAP ]==[ INSERT ]=============&lt; LETTER TEXT &gt;===========[ &lt;PF1&gt;H=Help ]====

|NOWRAP|

|CENTER("Women's Health Clinic")|

|CENTER("123 Clinic Street")|

|CENTER("Clinic City, SS	11111")|

|TODAY|

|$E(SSN#,6,9)|

|$P(NAME,",",2)| |$P(NAME,",")|

|COMPLETE ADDRESS|

- -	- -

Dear Ms. |$P(NAME,",",1)|,

###### The results of your latest PAP smear are NEM (No Evidence of Malignancy).

**We would like to see you again in 1 year for your regular PAP smear screening.	We will mail you a reminder letter in advance of that date, or you may schedule the appointment yourself by calling our Family Medicine Clinic at 777-7777 or our Women's Clinic at 777-7777.**

Sincerely,

WHNURSE, ONE

Women's Health Program Phone: 555-7777

printed: |NOW|

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

Override

#### Adding a new Dialog Element/Purpose of Notification

**Steps**

###### 4 Create a new note in WH

1. Create a dialog element that includes WH.note, HF.health factor, and prompt PXRM WH NOTE TYPE
2. Copy National reminder dialog to a local reminder dialog
3. Add your new dialog element to the local copy of reminder dialog

**Create dialog element**

The items added are **bold** , and the things that are necessary are underlined. Screen shots follow.

ELEMENT COMPONENTS:

Sequence:	5

Additional prompt:	PXRM WH NOTE TYPE Prompt caption:	Patient notified:

caption:	Patient notified:

Start new line:	YES Exclude from P/N:

Required:	YES

**new WH letter**

**new health factor**

Dialog Text:	LET'S DO LUNCH SOON, ok?

Alternate P/N Text:	Invited the patient to lunch.

Exclude from P/N: Resolution type:	OTHER

**Finding Item:	LET'S DO LUNCH HF**

Vital Prompt Caption: Orderable item:	N/A

Suppress Checkbox: Exclude Mental Health

Test Text from P/N: ADDITIONAL FINDINGS:

**Finding item:	LET'S DO LUNCH**

Result Element/Group:

Edit Comments:	Copied from VA-WH MAM RESULTS NEM NEXT MAM 2Y

Used by:	VA-WH GP MAM RESULTS NEM (Dialog Group)

Edit By: WHNURSE,TWO

Edit History:

Edit Date: OCT	3,2004	14:24

NUMBER: 1131

Name: **LET'S DO LUNCH**

Type:	dialog element Class: LOCAL

Sponsor: Review Date:

Oct 03, 2004 3:03:39 pm	Page 1

REMINDER DIALOG INQUIRY

This is what will make the letter display and update WH.

Text displays on screen and in progress note

New dialog element;

Add it to your local copy of the WH reminder dialog.

<!-- image -->

**In Women’s Health package:**

Women's Health Main Menu v1.0

MF	Manager's Functions ...

FM	File Maintenance Menu ...

AEP	Add/Edit a Notification Purpose &amp; Letter

Select WV NOTIFICATION PURPOSE: **LET'S DO LUNCH	ASAP**

###### Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

Enter Yes or No: NO//

**Appendix F: Local Dialog Modification to Trigger Order** **Menu**

<!-- image -->

Then when the Finish button is clicked, the order menu comes up:

<!-- image -->

**Appendix G: How to customize WH reminders and** **dialogs after installation**

###### During testing at the Washington D.C. VA, we had some problems. Here is what we did to fix them. We hope this information helps sites fix problem reminders and reminder dialogs

The clinician noticed these problems with the VA-WH Mammogram Screening reminder and reminder dialog:

1. Order selection item **Mammogram – screening** was linked to the wrong quick order

###### 5 Selection item for other mammogram orders were not linked to any quick order and needed to be removed

<!-- image -->

###### These are the changes that were made to the dialog, using options on the PXRM MANAGERS MENU:

1. Copy the national reminder dialog to create a local reminder dialog
    1. National dialog:	VA-WH MAMMOGRAM SCREENING Print name:	Mammogram Screening
    2. Local dialog:	DC VA-WH MAMMOGRAM SCREENING Print name:	Mammogram Screening – Local

1. **Order mammogram** is a group, so you need to copy the national group over to a local group
    1. National group:	VA-WH GP ORDERS - MAMMOGRAM SCREEN
    2. Local group:	DC VA-WH GP ORDERS - MAMMOGRAM SCREEN

1. This is what the new group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN looks like:
    1. Group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
    1. 5	Element: VA-WH OR MAMMOGRAM SCREENING
    2. 10	Element: VA-WH OR MAMMOGRAM BILAT
    3. 15	Element: VA-WH OR MAMMOGRAM UNILAT

###### 6 Edit the local group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN and remove selection options 3 &amp; 4 from the dialog group and this is what the group will look like when you’re done:

1. Group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN

1. 5	Element: VA-WH OR MAMMOGRAM SCREENING

1. **Order mammogram** is also part of a group **Screening** , so you need to copy this national group over to a local group:

###### 7 National group:	VA-WH GP MAMMOGRAM SCREENING

1. This is what the new group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN looks like:
###### 1 Group: DC VA-WH GP MAMMOGRAM SCREENING

###### 8 Edit the local group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN and remove selection options 3 &amp; 4 from the dialog group and this is what the group will look like when you’re done:

###### 2 Group: DC VA-WH GP MAMMOGRAM SCREENING

1. 5	Group: **DC VA-WH GP ORDERS - MAMMOGRAM SCREEN**
2. 5.5	Element: VA-WH OR MAMMOGRAM SCREENING

i. 10	Element: VA-WH MAMMOGRAM DONE OUTSIDE

###### 9 Edit the local dialog DC VA-WH MAMMOGRAM SCREENING and replace the national group with the local group:

1. National group:	VA-WH GP ORDERS - MAMMOGRAM SCREEN
2. Local group:	DC VA-WH GP ORDERS - MAMMOGRAM SCREEN

1. Edit the local dialog DC VA-WH MAMMOGRAM SCREENING and remove this selection options
    1. Order – refer to Women’s Health Provider

1. Create a quick order for mammogram screening if your site does not already have one using option ORCM QUICK ORDERS Enter/edit quick orders

1. Edit the national element VA-WH OR MAMMOGRAM SCREENING to point ADDITIONAL FINDINGS to the correct quick order:

Select ADDITIONAL FINDINGS: Q.GMRCZ

1	GMRCZ CARDIOLOGY CONSULT

1. GMRCZ DIETICIAN
2. GMRCZ EEG
3. GMRCZ MAMMOGRAM
4. GMRCZ PT FOR PNEUMONIA

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR CHOOSE 1-5: 5	GMRCZ MAMMOGRAM

Select ADDITIONAL FINDINGS: ?

Answer with ADDITIONAL FINDINGS:

GMRCZ MAMMOGRAM

**IRM noticed these problems during installation:**

###### 10 Finding items for Radiology mammogram procedures could not be mapped because all mammograms are done off site and VistA Radiology package did not have procedures for mammograms.

1. When the order selections were removed from the dialog, it left health factor findings in the reminder that needed to be removed.

These are the changes that needed to be made to the reminder:

1. Copy the national Mammogram Screening reminder to a local reminder
    1. National:	VA-WH MAMMOGRAM SCREENING
    2. Local:	DC VA-WH MAMMOGRAM SCREENING

1. Edit the print name so you will be able to tell it from the national reminder
    1. National:	Mammogram Screening
    2. Local:	Mammogram Screening - Local

1. Copy this national reminder term to local reminder term and remove all the finding items for Radiology. Also edit the description of the term to explain why you are removing the findings.
    1. National:	VA-WH MAMMOGRAM SCREEN IN RAD PKG
    2. Local: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG

---- Begin: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG	(FI(5)=RT(462)) -------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Mapped Findings:

###### Mapped Finding Item: RP.MAMMOGRAM BILAT

Condition: I V("PDX")'["UNSATISFACTORY"&amp;(V("SDX","*")'["UNSATISFACTORY")

###### Mapped Finding Item: RP.MAMMOGRAM BILAT

Condition: I V("PDX")'["UNSATISFACTORY"&amp;(V("SDX","*")'["UNSATISFACTORY")

###### Mapped Finding Item: RP.MAMMOGRAM UNILAT

Condition: I V("PDX")'["UNSATISFACTORY"&amp;(V("SDX","*")'["UNSATISFACTORY")

---- End: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG ------------------------

###### 11 Copy this national reminder term to a local reminder term and remove all the finding items for Radiology (RP.)

3. National: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG

---- Begin: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG (FI(10)=RT(473))

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Mapped Findings:

###### Mapped Finding Item: RP.MAMMOGRAM BILAT

Condition: I V("PDX")["UNSATISFACTORY"&amp;(V("SDX","*")["UNSATISFACTORY")

###### Mapped Finding Item: RP.MAMMOGRAM BILAT

Condition: I V("PDX")["UNSATISFACTORY"&amp;(V("SDX","*")["UNSATISFACTORY")

###### Mapped Finding Item: RP.MAMMOGRAM UNILAT

Condition: I V("PDX")["UNSATISFACTORY"&amp;(V("SDX","*")["UNSATISFACTORY")

Mapped Finding Item: CF.VA-WH MAMMOGRAM IN WH PKG Condition: I (V("VALUE")="Unsatisfactory")

Condition Case Sensitive: NO

---- End: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG ----------------

###### 12 Copy this national reminder term to local reminder term and remove the finding items for the two health factors belonging to the orders we removed from the dialog:

5. National:	VA-WH BREAST CARE ORDER HEALTH FACTOR

---- Begin: VA-WH BREAST CARE ORDER HEALTH FACTOR	(FI(7)=RT(471)) -----

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Beginning Date/Time: T-9M

Mapped Findings:

Mapped Finding Item: HF.WH ORDER MAMMOGRAM SCREEN HF Health Factor Category: WH MAMMOGRAM

###### Mapped Finding Item: HF.WH ORDER MAMMOGRAM BILAT HF

Health Factor Category: WH MAMMOGRAM

###### Mapped Finding Item: HF.WH ORDER MAMMOGRAM UNILAT HF

Health Factor Category: WH MAMMOGRAM

---- End: VA-WH BREAST CARE ORDER HEALTH FACTOR -----------------------

###### 13 Edit the local Mammogram Screening reminder and replace the three national reminder terms with the three local terms:

Reminder Definition Findings Choose from:

| **RT**   | **DC VA-WH BREAST CARE ORDER HEALTH FACTOR**    |         | **Finding**   | **#:**   | **7**   |
|----------|-------------------------------------------------|---------|---------------|----------|---------|
| **RT**   | **DC VA-WH MAMMOGRAM SCREEN IN RAD PKG**        |         | **Finding**   | **#:**   | **5**   |
| **RT**   | **DC VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH** | **PKG** | **Finding**   | **#:**   | **10**  |
| RT       | VA-TERMINAL CANCER PATIENT                      |         | Finding       | #:       | 3       |
| RT       | VA-WH BILATERAL MASTECTOMY                      |         | Finding       | #:       | 2       |
| RT       | VA-WH HX BREAST CANCER/ABNORMAL MAM             |         | Finding       | #:       | 15      |
| RT       | VA-WH MAMMOGRAM ORDER                           |         | Finding       | #:       | 16      |
| RT       | VA-WH MAMMOGRAM SCREEN DEFER                    |         | Finding       | #:       | 9       |
| RT       | VA-WH MAMMOGRAM SCREEN DONE                     |         | Finding       | #:       | 6       |
| RT       | VA-WH MAMMOGRAM SCREEN FREQ - 1Y                |         | Finding       | #:       | 13      |
| RT       | VA-WH MAMMOGRAM SCREEN FREQ - 2Y                |         | Finding       | #:       | 14      |
| RT       | VA-WH MAMMOGRAM SCREEN FREQ - 4M                |         | Finding       | #:       | 11      |
| RT       | VA-WH MAMMOGRAM SCREEN FREQ - 6M                |         | Finding       | #:       | 12      |
| RT       | VA-WH MAMMOGRAM SCREEN IN WH PKG                |         | Finding       | #:       | 4       |
| RT       | VA-WH MAMMOGRAM SCREEN NOT INDICATED            |         | Finding       | #:       | 8       |

###### This is the result of the dialog changes:

<!-- image -->

**Index**

###### Activate alerts, 61

Add and Edit Notification Letters, 28 Add Reminders to CPRS Cover Sheet, 54 Add/Edit Case Managers, 22

alerts, 3, 23, 61

APPENDIX A: KIDS Load &amp; Installation Example, 62

APPENDIX B: Key Points to WH Reminders Installation and Setup, 68

APPENDIX C: Reminders Installation with Reminder Exchange Utility, 70

Appendix D: WV*1*16 Description, 72 Appendix E: Setting up Notification Letters,

80

Appendix F – Local Dialog Modification to trigger order menu, 91

Appendix G: How to customize WH reminders and dialogs after installation, 93

Benefits, 1

case manager, 22

CPRS GUI, 20

CPT, 7

Default Case Manager, 25 Diagnostic Code, 35

dialogs, 18

dummy quick order, 10

Edit Diagnostic Code Translation File:, 35 Edit Site Parameters, 25

Editing Dialogs, 48

Exchange Utility, 70

File Maintenance Menu, 24 Files, 8

forced values, 51

FTP, 13

FTP Addresses, 13

HL7, 7

ICD, 7

Import Mammograms from Radiology, 25 Import Tests from Laboratory, 25 Installation Example, 62

Installation Instructions, 13

Installation Order, 12

Installation Time, 7

Installation with Reminder Exchange Utility, 70

interface with the Women's Health, 22

Kernel, 7

Key Points to WH Reminders Installation and Setup, 68

KIDS, 14

LABORATORY, 25

letters, 56

Lexicon, 7

Link Pap Smear with SNOMED Codes, 31 Local Dialog Modification to trigger order

menu, 91

LR*5.2*311, 3

MailMan, 7

Mammogram Review, 34 Mammogram Screening Dialog, 58 Mammogram Terms, 37

Mapping, 37

Notification, 23

Notification Letters, 26, 80

Notification Purpose, 29 Notification type definitions, 51 notification/alerts, 3

options to put out of order, respond with:, 15 OR*3.0*210, 3

Order Dialog, 10

Order Entry/Results Reporting, 7 order menu, 91

Ordering a Consult, 51 Overview, 1

packed reminders, 16 patches in build, 2 POST^PXRMWHP, 16

Post-Installation Procedures, 16 Pre and Post-Install Routines, 8 Pre-Install Worksheet, 10, 11

Print Diagnostic Code Translation File, 35 Print Now flag, 56

Project Goals, 20

PXRM WH UPDATE TREATMENT NEED, 51

queued, 56

queued letters, 56

quick orders, 5

RADIOLOGY, 25

refresh” the screen, 60

Reminder Term Management, 37 Reminder Test, 47

Required Packages, 7

rescinded, 1

Result/Diagnosis code, 35

Routine Mapping, 9

Routines, 9

Set up entries in the WV Notification Purpose file, 56

Setup Overview, 20

SNOMED, 4, 22

Status Given to Imported Mammograms, 34, 35

Term Mapping Recommendations, 37 terms, 17

Test Dialogs, 57

Testing Reminders, 53 Text Integration Utilities, 7 TOPOGRAPHY, 22

VA FileMan, 7

VA FileMan Print from the Reminder Term File, 17

VA-*BREAST CANCER SCREEN, 1

VHA policy, 1

Web sites, 6

WH dialogs, 19

Women’s Health Case Manager, 5 Women’s Health Package, 21 WV*1*16 Description, 72

WV*1.0*16, 2