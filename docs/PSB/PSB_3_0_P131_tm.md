---
app_name: 'Pharmacy: Bar Code Medication Administration (BCMA) (PSB)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2021-10
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PSB
patch: 131
patch_gap: null
section: ''
source_file: PSB_3_0_P131_tm.docx
status: draft
title: PSB 3 0 P131 tm.docx
---

<!-- image -->

BAR CODE MEDICATION ADMINISTRATION (BCMA)

TECHNICAL MANUAL/SECURITY GUIDE

Version 3.0

February 2004

(Revised October 2021)

<!-- image -->


###### Revision History

| Date    | Revised Pages                              | Patch Number   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/2021 | C-6,C-7                                    | PSB*3*131      | Added an example of a Zebra Printer Sample Terminal Type File with HAZ Control Code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 07/2021 | C-2  ,  C-3  ,  C-6  ,  C-9                | PSB*3*106      | Updated the tables to include the parameters for Hazardous to Handle and Hazardous to Dispose data, and added a sample label containing that information.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 01/2019 | 7  ,  8  ,  9                              | PSB*3*103      | Added new routine names to the Routines Installed table. Added "Report for Respiratory Therapy Medications" option to the Medication Administration Menu Pharmacy.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 12/2016 | i, 8, 9                                    | PSB*3*88       | Add “BCMA Drug IEN Synonym Check” option to Pharmacy Medication Administration Menu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
<!-- rpc-table -->
| 12/2016 | All  6  7  9  19                           | PSB*3*83       | Renumbered pages to remove sub-pages a, b, etc.  Updated number of routines in list.  Added new Routine “PSBVDLRM”.  Spelled out first use of acronym CHUI.  Added new RPC “PSB GETSETWP” to table and included RPC “PSB GETINJECTIONSITE” from previous patch.  REDACTED                                                                                                                                                                                                                                                                                                                        |
| 12/2013 | i-ii, 9, 10, 10a-10b,  14,  18a            | PSB*3*70       | Added “Documenting Backlog PRNs” to Manager’s Menu. Added note that Missed Medications, Ward Administration Times, and Due List BCMA CHUI reports are Inpatient, only.  Added PSB NO WITNESS Security Key. Missing Dose Request option removed from CHUI menus. Added “VHIC 4.0 Card Bar Code Scanning Support” to External Relations section.  REDACTED                                                                                                                                                                                                                                         |
| 01/2011 | i-ii, 6, 7, 10, 15,  B-2, B-4              | PSB*3*42       | Added note and list of BCMA Reports that were added to GUI only.  Added definition of data field change for Indian Health Service.  Added Indian Health Service terms to Glossary.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                     |
| 10/2009 | i-ii, 7, 9, 17                             | PSB*3*47       | Added PSBPXFL and PSBPXLP to the list of installed routines.  Add Immunizations Documentation by BCMA Nightly Task [PSB PX BCMA2PCE TASK] option to the  *Manager*  [PSB MGR] menu.  Added Patient Care Encounter to the External Relationships section.  REDACTED                                                                                                                                                                                                                                                                                                                               |
| 01/2009 | i-ii, iv, 6-7,  13-14,  18-19, 21          | PSB*3*28       | - Update Table of Contents to include Remote Procedure Calls. (p. iv)  - Increased the total for the BCMA V .3.0 routines to 85 and files to 6. (p.6-7)  - Updated the files and “BCMA V.3.0 Routines Installed onto VistA Server” Example. (p.7)  - Updated the Mail Group Types in BCMA V.3.0 to include scanning  failures. (p. 13)  - Updated Security Keys to include PSB UNABLE TO SCAN. (p. 14)  - Added list of Remote Procedure Calls (RPCs). (p. 18)  -Added new Glossary entry for LIMITED ACCESS BCMA. (p. 19)  - Added new Glossary entry for PSB UNABLE TO SCAN. (p. 21)  REDACTED |
| 03/2008 | 6-7, 9-10,  C-1, C-2,  C-4, C-5,  C-7, C-9 | PSB*3*2        | Description of [PSBO BZ] functionality added, code strings updated (p. C-1.)  - Updated Intermec Printer Team Type Codes Information, Intermec        Barcode Label Field Position Map, Intermec printer Sample Terminal Type File code descriptions updated (pp. C-4, C-5, C-7.)  - Barcode samples updated – references to “Dosage” changed to “Dose” and space between colon and dose measurement deleted (p. C-9.)  REDACTED                                                                                                                                                                 |
| 09/2007 | 6-7                                        | PSB*3*32       | – Increased the total for the BCMA V. 3.0. routines to 68. (p.6)  – Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routine: PSBO XA. (p. 7)  REDACTED                                                                                                                                                                                                                                                                                                                                                                                           |
| 08/2006 | 6-7,  9, 13                                | PSB*3*13       | – Increased the total for the BCMA V. 3.0. routines to 68. (p.6)  – Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routine: PSBO XA. (p. 7)  – Updated Manager Menu [PSB MGR] options list to include Missing Dose Follow-up (correction) and Unknown Action Status Report (new with this patch). (p. 9)  – Added description of the “Unknown Actions” mail group parameter. (p. 13)  REDACTED                                                                                                                                                  |
| 08/2006 | iv,  6,  C1-C10                            | PSB*3*2        | **Note**  : The functionality listed below will be activated with the release of PSB*3*2.  – Updated Table of Contents to include new Appendix C. (p. iv)  – Added reference to new Unit Dose label printing functionality and Appendix C. (p. 6)  – Added Appendix C: Interfacing with the Bar Code Label Printer. (p. C1-C10)  REDACTED                                                                                                                                                                                                                                                        |
| 12/2005 | 6-7                                        | PSB*3*16       | – Increased the total for the BCMA V. 3.0. routines to 67. (p.6)  – Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routines: PSBCSUTL, PSBCSUTX, PSBCSUTY. (p. 7)  REDACTED                                                                                                                                                                                                                                                                                                                                                                     |
| 01/2005 | 6-7,  14,  20-21                           | PSB*3*4        | – Increased the total for the BCMA V. 3.0. routines to 64. (p.6)  – Updated the “BCMA V. 3.0 Routines Installed on to VistA Server” example to include the PSBOPF routine. (p. 7).  – Added description for new PSB READ ONLY security key. (p.14)  – Added new Glossary entries for PSB READ ONLY and Read-Only BCMA. (p. 20-21)  REDACTED                                                                                                                                                                                                                                                      |
| 10/2004 | 6-7                                        | PSB*3*3        | – Increased the total for the BCMA V. 3.0 routines to 63. (p. 6)  – Updated the “BCMA V. 3.0 Routines Installed on to VistA Server” example to reflect the inclusion of routines PSBML2, PSBML3, and PSBMLLKU to the VistA Server. (p. 7)  REDACTED                                                                                                                                                                                                                                                                                                                                              |
| 02/2004 |                                            |                | Original Released BCMA V. 3.0 Technical Manual/Security Guide  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Table of Contents

BCMA V. 3.0 and This Guide	1

Benefits of BCMA V. 3.0	1

Benefits of This Guide	1

Our Target Audience	1

Other Sources of Information	2

Background/Technical Information	2

This Manual and Related Documentation	2

Conventions Used in This Guide	2

Obtaining On-line Help	3

Locating Detailed Listings	3

Routines	3

Data Dictionaries	3

Implementation and Maintenance	5

Minimum Required Packages	5

Installation Time Estimates	5

Resource Requirements	6

Response Time Monitor	6

Laptops and Bar Code Scanners	6

Printers	6

Unit Dose Label Printer Devices	6

IV Label Printer Devices	6

Files Required to Run BCMA V. 3.0	7

Routines Installed	7

Routine Mapping	7

Exported Options	8

BCMA CHUI Menus	8

Manager Menu [PSB MGR]	8

Medication Administration Menu Pharmacy [PSB PHARMACY]	9

Nursing Medication Administration Menu [PSB NURSE]	9

Archiving and Purging	11

Archive and Purge Capabilities	11

Security Features	12

Defining Mail Groups in BCMA	12

Creating Mail Groups for BCMA V. 3.0	12

Mail Group Types in BCMA V. 3.0	12

Assigning Menus to Users	13

CHUI Version	13

GUI Version	13

Allocating Security Keys to Users	13

Establishing Electronic Signature Codes	13

Developing a Contingency Plan	14

Internal and External Relations	15

Internal Relations	15

Options	15

Package-Wide Variables	15

Templates	15

External Relations	15

Callable Routines, Entry Points, and Variables	16

Database Integration Agreements (DBIAs)	16

Remote Procedure Calls (RPCs)	16

VHIC 4.0 Card Bar Code Scanning Support	17

Glossary	18

Learning BCMA V. 3.0 Lingo	18

Appendix A: Processing of Schedule Information	1

How BCMA Processes Schedule Information	1

Steps for Processing Schedule Information	1

Examples of Odd Schedules	4

Examples of Schedules That Are Not Odd Schedules	4

Appendix B: HL7 Messaging for BCMA	1

Sample HL7 Data Fields Broadcast to BCMA Subscribers	1

Definitions of Data Fields Under FIELD NAME Column	4

Sample HL7 Data Fields Passed in Each Trigger Event	8

Appendix C: Interfacing with the Bar Code Label Printer	1

Introduction	1

Hardware Setup	1

Software Setup	1

Printer Control Codes	2

Control Code Set Up	2

Example Terminal Type Files	6

Dot Matrix and Laser Printers	9

Printed Bar Code Unit Dose Label Sample	10

JCAHO Standard for Medication Labeling*	11

## BCMA V. 3.0 and This Guide

tip:

BCMA is designed to augment, not replace, the clinical judgment of the medication administrator, or clinician.

Use this guide for working with the CHUI version of BCMA, V. 3.0.

| tip:  BCMA is designed to augment, not replace, the clinical judgment of the medication administrator, or clinician.  <!-- image -->  <!-- image -->  ### Benefits of BCMA V. 3.0   | The Bar Code Medication Administration (BCMA) V. 3.0 software includes new routines and files, Phase Release changes, and maintenance fixes. This version also includes enhancements, which are a direct result of feedback from the BCMA Workgroup and our many end users.  The patch description for BCMA V. 2.0 includes more detailed information about the maintenance fixes and enhancements for Phase Releases I through IV, which were provided in patches PSB*2*20, *24, *31, and *36.  BCMA software is designed to improve the accuracy of the medication administration process. By automating this process, Department of Veterans Affairs Medical Centers (VAMCs) can expect enhanced patient safety and patient care.  The electronic information that BCMA V. 3.0 provides clinicians improves their ability to administer medications safely and effectively to patients on wards during their medication passes. It also helps to improve the daily communication that occurs between Nursing and Pharmacy staffs.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| tip:  Use this guide for working with the CHUI version of BCMA, V. 3.0.  <!-- image -->  <!-- image -->  ### Benefits of This Guide                                                 | This guide will help you discover the many technical and security aspects of BCMA V. 3.0. It describes implementation and maintenance features; interfaces, variables, and relationships; and security management.  #### Our Target Audience  We have developed this guide for members of the Automated Data Processing (ADP) group and the Information Resources Management (IRM) group who are responsible for maintaining and supporting this package.  We assume that individuals within these groups have the following experience or skills.  Experienced with other Veterans Health Information Systems and Technology Architecture () software  Have worked with or will work with an Applications Package Coordinator (ADPAC) or Clinical Applications Coordinator (CAC) familiar with the medication administration process in a VAMC                                                                                                                                                                                        |

## BCMA V. 3.0 and This Guide

tip:

Bookmark these sites for future reference.

In a CHUI environment, when you press the ENTER key, instead of typing a response, the system accepts the default value shown to the left of the double slash (//) at a prompt or field.

In a CHUI environment, when you press **enter** , instead of typing a response, the system accepts the default value shown to the left of the double slash (//) at a prompt or a field.

| tip:  Bookmark these sites for future reference.  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  ### Other Sources of Information                                                                                                                 | Refer to the Web sites listed below when you want to receive more background and technical information about BCMA V. 3.0, and to download this manual and related documentation.  #### Background/Technical Information  From your Intranet, enter REDACTED in the Address field to access the BCMA Main Web page.  #### This Manual and Related Documentation  From your Intranet, enter  [http://www.va.gov/vdl](http://www.va.gov/vdl)  in the Address field to access this manual, and those listed below, from the VA Software Document Library (VDL).  Installation Guide  GUI User Manual  Nursing CHUI User Manual  Pharmacy CHUI User Manual  Manager’s User Manual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
|                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |
| tip:  In a CHUI environment, when you press the ENTER key, instead of typing a response, the system accepts the default value shown to the left of the double slash (//) at a prompt or field.  <!-- image -->  <!-- image -->  ### Conventions Used in This Guide | tip:  In a CHUI environment, when you press  **enter**  , instead of typing a response, the system accepts the default value shown to the left of the double slash (//) at a prompt or a field.  <!-- image -->  <!-- image -->  Before installing BCMA V. 3.0, review this section to learn the many conventions used throughout this guide.  **Keyboard Responses:**  Keys provided in  **boldface**  , within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see  **enter**  in the copy, press this key on your keyboard.  **Mouse Responses:**  Buttons provided in  **boldface**  , within the steps, indicate what you should click on your computer screen using the mouse. For example, when you see  **next, yes/no,**  or  **ok**  in the steps, click the appropriate button on your screen.  **Screen Captures:**  Provide “shaded” examples of what you will see on your computer screen, and possible user responses.  **Notes:**  Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our Staff, Developers, and Testers.  **Tips:**  Located in the left margin, these helpful hints are designed to help you work more efficiently with BCMA V. 3.0.  **Menu Options:**  Provided in italics. For example, You may establish Electronic Signatures Codes using the Kernel  *Electronic Signature code Edit*  [XUSESIG] option. |    |

## BCMA V. 3.0 and This Guide

tip:

**The BCMA Virtual Due List (VDL)** is called “BCMA VDL” in this guide to eliminate confusion with
the VA Software Document Library (VDL) also mentioned
in this guide.

| tip:  **The BCMA Virtual Due List (VDL)**  is called “BCMA VDL” in this guide to eliminate confusion with the VA Software Document Library (VDL) also mentioned in this guide.  <!-- image -->  <!-- image -->  ### Obtaining On-line Help   | On-line help is designed right into the Graphical User Interface (GUI) and Character-based User Interface (CHUI) versions of BCMA V. 3.0, making it quick and easy for you to get answers to your questions. Here’s how to access help in both versions of BCMA V. 3.0:  **GUI BCMA:**  Provides context-sensitive, on-line help and the Help menu.  **Context-Sensitive Help:**  Place your “focus” on a feature, button, or Tab on the BCMA Virtual Due List (VDL) using the  **tab**  key, and then press  **f1**  to receive help specific to that area of the BCMA VDL. In the case of a command, first highlight it in the Menu Bar or Right Click drop-down menu, and then press  **f1.**  **Help Menu:**  Open the Help menu, and then choose the Contents and Index command to receive help for every feature in GUI BCMA V. 3.0.  **CHUI BCMA:**  Lets you enter up to two question marks at any prompt to receive on-line help.  **One Question Mark:**  Provides a brief statement related to the prompt.  **Two Question Marks:**  Displays more detailed information about the prompt, plus any hidden actions.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Locating Detailed Listings                                                                                                                                                                                                                   | You can obtain  *and*  print listings about BCMA V. 3.0 routines, and Data Dictionaries using the information provided below.  #### Routines  Use the Kernel routine XINDEX to produce detailed listings of routines. Use the Kernel  *First Line Routine Print*  [XU FIRST LINE PRINT] option to print a list containing the first line of every PSB routine.  #### Data Dictionaries  You can use the VA FileMan  *List File Attributes*  [DILIST] option, under the  *Data Dictionary Utilities*  [DI DDU] option, to print the Dictionaries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Implementation and Maintenance

| ### Minimum Required Packages   | Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).   |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Minimum Required Packages and Versions

| Package                       |   Minimum Version Needed |
|-------------------------------|--------------------------|
| Inpatient Medications         |                      5   |
| Kernel                        |                      8   |
| MailMan                       |                      8   |
| Nursing                       |                      4   |
| Order Entry/Results Reporting |                      3   |
| Pharmacy Data Management      |                      1   |
<!-- rpc-table -->
| RPC Broker (32-bit)           |                      1.1 |
| Toolkit                       |                      7.3 |
| VA FileMan                    |                     22   |
| Vitals/Measurements           |                      5   |

important:

You should install and test BCMA in your test accounts ***before*** installing in your production accounts.

| ### Installation Time Estimates  important:  You should install and test BCMA in your test accounts  ***before***  installing in your production accounts.  <!-- image -->  <!-- image -->   | On average, it takes approximately two minutes to install BCMA V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its system resources.  Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Implementation and Maintenance

tip:

The approximate size for ^PSB was calculated using a “normal” medication pass for a Unit Dose and an IV medication order. This is only an estimated number; it serves as the “mean.”

The approximate size for ^PSB was calculated using a "normal”  for a Unit Dose and an IV medication order. This is only an estimated number; it serves as the “mean.”

| tip:  The approximate size for ^PSB was calculated using a “normal” medication pass for a Unit Dose and an IV medication order. This is only an estimated number; it serves as the “mean.”  The approximate size for ^PSB was calculated using a "normal”  for a Unit Dose and an IV medication order. This is only an estimated number; it serves as the “mean.”  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  ### Resource Requirements   | This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.  Routines		97  Globals		1 (^PSB)  Files		6 (53.66-53.79)  ^PSB Size		Unit Dose = 300 x # of Medications (in bytes)		Administered 		   IV = 2100 x # of IV Bags 		   Administered  FTEE Support		.2  FTEE Maintenance		.2  #### Response Time Monitor  BCMA V. 3.0 does not include Response Time Monitor hooks.  #### Laptops and Bar Code Scanners  The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas at your site that use BCMA  V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.  #### Printers  Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.  #### Unit Dose Label Printer Devices  BCMA V. 3.0 includes the  *Label Print*  [PSBO BL] option for printing individual or batch Unit Dose bar code labels. This option allows sites the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBL uses site-specific printers or terminals to produce labels. See Appendix C: “Interfacing with the Bar Code Label Printer” for detailed setup information.  #### IV Label Printer Devices  Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section “Interfacing with the Bar Code Label Printer” in the  *Inpatient Medications V. 5.0 Technical Manual/Security Guide*  for detailed setup information.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|

## Implementation and Maintenance

tip:

The namespace for the BCMA package is PSB and the primary global
is ^PSB.

| tip:  The namespace for the BCMA package is PSB and the primary global is ^PSB.  <!-- image -->  <!-- image -->  ### Files Required to Run BCMA V. 3.0   | BCMA V. 3.0 uses the following files installed on the VistA Server. “Journaling” is recommended.  ^PSB (53.66,	BCMA IV Parameters  ^PSB (53.68,	BCMA Missing Dose Request  ^PSB (53.69,	BCMA Report Request  ^PSB (53.77,	BCMA Unable to Scan Log  ^PSB (53.78,	BCMA Medication Variance Log  ^PSB (53.79,	BCMA Medication Log  Note: You can learn more about these files by generating a list with file attributes using VA FileMan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Routines Installed                                                                                                                                       | Review the listing below to learn the routines installed on your site’s VistA Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.  **Note:**  You can use the  *Kernel First Line Routine Print*  [XU FIRST LINE PRINT] option to print a list containing the first line of each PSB routine.  #### Routine Mapping  At this time, we do  *not*  offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory. |

Example: BCMA V. 3.0 Routines Installed onto VistA Server

| PSB3P103   | PSBALL   | PSBAPIPM   | PSBCHIVH   | PSBCHKIV   | PSBCSUTL   | PSBCSUTX   | PSBCSUTY   |
|------------|----------|------------|------------|------------|------------|------------|------------|
| PSBINJEC   | PSBMD    | PSBML      | PSBML1     | PSBML2     | PSBML3     | PSBMLEN    | PSBMLEN1   |
| PSBMLHS    | PSBMLLKU | PSBMLTS    | PSBMLU     | PSBMLVAL   | PSBMMRB    | PSBO       | PSBO1      |
| PSBOAL     | PSBOBL   | PSBOBLU    | PSBOBZ     | PSBOCE     | PSBOCE1    | PSBOCI     | PSBOCI1    |
| PSBOCM     | PSBOCM1  | PSBOCP     | PSBOCP1    | PSBODL     | PSBODL1    | PSBODO     | PSBOHDR    |
| PSBOHDR1   | PSBOIV   | PSBOIV1    | PSBOMD     | PSBOMH     | PSBOMH1    | PSBOMH2    | PSBOMH3    |
| PSBOML     | PSBOMM   | PSBOMM2    | PSBOMT     | PSBOMT1    | PSBOMV     | PSBOPE     | PSBOPF     |
| PSBOPI     | PSBOPM   | PSBOPM1    | PSBORT     | PSBOSF     | PSBOST     | PSBOVT     | PSBOWA     |
| PSBOXA     | PSBPAR   | PSBPARIV   | PSBPOIV    | PSBPRN     | PSBPRND    | PSBPXFL    | PSBPXLP    |
| PSBRPC     | PSBRPC1  | PSBRPC2    | PSBRPC3    | PSBRPCMO   | PSBRPCXM   | PSBSAGG    | PSBSVHL7   |
| PSBUTL     | PSBVAR   | PSBVDLIV   | PSBVDLPA   | PSBVDLPB   | PSBVDLRM   | PSBVDLTB   | PSBVDLU1   |
| PSBVDLU2   | PSBVDLU3 | PSBVDLUD   | PSBVDLVL   | PSBVITFL   | PSBVPR     | PSBVT      | PSBVT1     |
| PSBXMRG    |          |            |            |            |            |            |            |

## Exported Options

| BCMA CHUI Menus   | BCMA V. 3.0 exports three main menus. They include those listed below, in the Character-based User Interface (CHUI) version of BCMA V. 3.0. The options for each menu are listed in this section.  **Manager Menu:**  [PSB MGR] is assigned to managers  **Pharmacist Menu:**  [PSB PHARMACY] is assigned to all inpatient Pharmacists  **Nurse Menu:**  [PSB NURSE] is assigned to all clinicans and other personnel who administer active medication orders  #### Manager Menu [PSB MGR]  This menu includes the following options:  Documenting Backlog PRNs  Drug File Inquiry  Immunizations Documentation by BCMA Nightly Task  Medication Administration Menu Nursing  Medication Administration Log Report  Missed Medications Report (INPATIENT ONLY)  Ward Administration Times Report (INPATIENT ONLY)  Due List Report (INPATIENT ONLY)  PRN Effectiveness List Report  Enter PRN Effectiveness  Manual Medication Entry  Medication Administration History (MAH) Report  Medication Variance Log  Drug File Inquiry  Medication Administration Menu Pharmacy  Medication Administration Log Report  Missed Medications Report (INPATIENT ONLY)  Due List Report (INPATIENT ONLY)  Medication Administration History (MAH) Report  Missing Dose Followup  Missing Dose Report  Label Print  Drug File Inquiry  Barcode Label Print  BCMA Drug IEN Synonym Check  Report for Respiratory Therapy Medications  Missing Dose Followup  Reset User Parameters  Trouble Shoot Med Log  Unknown Action Status Report   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Exported Options

| BCMA CHUI Menus (cont.)   | #### Medication Administration Menu Pharmacy [PSB PHARMACY]  This menu includes the following options:  Medication Administration Log Report  Missed Medications Report (INPATIENT ONLY)  Due List Report (INPATIENT ONLY)  Medication Administration History (MAH) Report  Missing Dose Followup  Missing Dose Report  Label Print  Drug File Inquiry  Barcode Label Print  BCMA Drug IEN Synonym Check  Report for Respiratory Therapy Medications  #### Nursing Medication Administration Menu [PSB NURSE]  This menu includes the following options:  Medication Administration Log Report  Missed Medications Report (INPATIENT ONLY)  Ward Administration Times Report (INPATIENT ONLY)  Due List Report (INPATIENT ONLY)  PRN Effectiveness List Report  Enter PRN Effectiveness  Manual Medication Entry  Medication Administration History (MAH) Report  Medication Variance Log  Drug File Inquiry  **Note:**  The Missed Medications, Ward Administration Times, and Due List BCMA CHUI reports will only include Inpatient orders in the report.  The menus containing these options will be updated to include “(INPATIENT ONLY)” in the report label/description.  To run these reports for Clinic orders and updated report selection options, the reports must be generated in the BCMA GUI.  ## Note: The following reports have been added to BCMA and are available via GUI only, but have not been added to the CHUI menus.  Cover Sheet Reports  Medication Overview  PRN Overview  IV Overview   |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Exported Options

| BCMA CHUI Menus (cont.)   | Expired/DC’d/Expiring Orders  IV Bag Status Report  Medication Therapy Report  Unable to Scan Detailed Report  Unable to Scan Summary Report   |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

## Archiving and Purging

tip:

Archive and purge capabilities are *not* available in
BCMA V. 3.0.

Archive and purge capabilities are *not* available in this version of BCMA.

| tip:  Archive and purge capabilities are  *not*  available in BCMA V. 3.0.  Archive and purge capabilities are  *not*  available in this version of BCMA.  <!-- image -->  <!-- image -->  <!-- image -->  <!-- image -->  ### Archive and Purge Capabilities   | BCMA V. 3.0 stores detailed information about each inpatient at your VAMC, including medications administered to them and the PRN Effectiveness (when applicable).  **Average Unit Dose Administration**  : Requires about 300 bytes of disk space  **Average IV Administration:**  Requires about 2100 bytes of disk space  **Note:**  Although archive and purge capabilities are  *not*  currently available in BCMA V. 3.0, when they are, they will be consistent with the Computerized Patient Record System (CPRS) package. BCMA  V. 3.0 will offer this feature once it is made available in CPRS.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Security Features

| Defining Mail Groups in BCMA   | In BCMA V. 3.0, you can define two “Mail Groups” for notifying Pharmacy, IRM, and other internal staff about errors and Missing Dose Requests. This section describes how you can create mail groups, and the purpose of each group.  #### Creating Mail Groups for BCMA V. 3.0  Creating mail groups for BCMA V. 3.0 involves using the VistA Mail Group  *Enter/Edit*  [XMUSER] option to set the TYPE field to PUBLIC. Once this task is accomplished, you can then use the Parameters Tab of the GUI BCMA Site Parameters application to define the mail groups that you created.  #### Mail Group Types in BCMA V. 3.0  This section describes the mail groups that you can define using the Parameters Tab of the GUI BCMA Site Parameters application.  **Due List Error:**  Generates an E-mail message for any medication order that BCMA V. 3.0 cannot resolve for the BCMA VDL placement, and sends it to the mail group members. An example might include no administration times entered for a Continuous order.  **Missing Dose Notification:**  Generates an E-mail message for any Missing Dose Request entered using the BCMA V. 3.0 GUI menu option. The E-mail is sent to all members of the mail group, specifically Pharmacy, as a “fail safe” even if the designated Missing Dose printer is not functioning.  **Unknown Actions:**  This field generates an E-mail message for any administration with an “Unknown” status while processing administrations to display on the BCMA VDL.  **Unable to Scan:**  Generates an E-mail message to alert the mail group when a user creates a scanning failure entry, and to assist in researching the reasons for a scanning failure.   |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Security Features

| Assigning Menus to Users                | Use this section to assign menus to BCMA V. 3.0 CHUI and GUI users, if they have not already been assigned.  #### CHUI Version  Refer to this section for BCMA V. 3.0 CHUI menu assignments.  **PSB MGR:**  assign to a manager  **PSB PHARMACY:**  assign to all Inpatient Pharmacists  **PSB NURSE:**  assign to all clinicians and other personnel who administer active medication orders  #### GUI Version  Refer to this section for BCMA V. 3.0 GUI menu assignments.  **PSB GUI CONTEXT – USER:**  assign to all clinicians and other personnel who administer active medication orders                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Allocating Security Keys to Users       | Refer to this section to allocate the following security keys to appropriate site personnel.  **PSB MANAGER:**  designates the holder as a manager  **PSB INSTRUCTOR:**  designates the holder as a nursing instructor supervising student nurses  **PSB STUDENT:**  designates the holder as a student nurse, requiring that an instructor also sign on to BCMA V. 3.0 at the same time  **PSB CPRS MED BUTTON:**  designates the holder as a nurse who can document administered verbal- and phone-type STAT and NOW (One-Time) orders using the CPRS Med Order Button on the BCMA VDL  **PSB READ ONLY:**  designates the holder as a user that only has Read-Only access to BCMA. Note that users with Read-Only access will also be required to have the PSB GUI CONTEXT – USER secondary menu option.  **PSB UNABLE TO SCAN:**  designates the holder as a user that can run the Unable to Scan (Detailed and Summary) reports.  **PSB NO WITNESS:**  designates the holder as a BCMA user not authorized to witness high risk/high alert administrations, such as Unlicensed Assistive Personnel and Respiratory Therapists. |
|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Establishing Electronic Signature Codes | You may establish Electronic Signatures Codes using the Kernel  *Electronic Signature code Edit*  [XUSESIG] option.  **Note:**  For easier access by all users, this option is tied to the Common Options, under the  *User’s Toolbox*  [XUSERTOOLS] submenu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Security Features

| Developing a Contingency Plan   | In March 2006, patch PSB*3*8, the BCMA Backup System (BCBU), was reissued with significant enhancements to the field as a Class I solution for the BCMA Contingency Plan. This patch provides real-time backup of all inpatient medication activities on a designated workstation. Review the patch description to learn more about the benefits of this patch.   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Internal and External Relations

tip:

You can locate specific routines in the “Routines Installed” section of this guide.

| Internal Relations                                                                                                                                | This section describes options, package-wide variables, and templates within BCMA V. 3.0.  #### Options  You can invoke ALL options in BCMA V. 3.0 independently.  #### Package-Wide Variables  BCMA V. 3.0 does  *not*  include package-wide variables.  #### Templates  BCMA V. 3.0 does  *not*  include any templates for Sort, Input, or Print.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                       |
<!-- rpc-table -->
| tip:  You can locate specific routines in the “Routines Installed” section of this guide.  <!-- image -->  <!-- image -->  ### External Relations | BCMA V. 3.0 can only be run in an environment that already has several existing features, such as a standard MUMPS operating system.  It also requires the following Department of Veterans Affairs (VA) software packages (versions listed or higher) — and all current patches. Otherwise, BCMA V. 3.0 will  *not*  be fully functional for your users.  Inpatient Medications		5.0  Kernel 			8.0  MailMan			8.0  Nursing			4.0  Order Entry/Results			3.0 Reporting  Patient Care Encounter	1.0  Pharmacy Data 			1.0 Management  RPC Broker (32-bit)			1.1  Toolkit			7.3  VA FileMan			22.0  Vitals/Measurements		5.0                                                                                                                                                                                                                                                                                                                                                       |

## Internal and External Relations

| ### External Relations  ### (cont.)   | #### Callable Routines, Entry Points, and Variables  BCMA V. 3.0 includes two callable routines: PSBAPIPM and PSBMLHS. Each routine is described in this section, along with the entry points and variables information for each.  **PSBAPIPM:**  Provides information to Inpatient Medications V. 5.0 for determining the start date for a renewed order.  **PSBMLHS:**  Provides other software packages with the ability to call the BCMA Medication History Report. The report lists medications, that a patient has received, by orderable item.  #### Database Integration Agreements (DBIAs)  BCMA subscribes to Database Integration Agreements (DBIAs) with the Inpatient Medications, CPRS, Nursing, and Registration packages. BCMA V. 3.0 also offers DBIAs for other packages to subscribe to as well.  For detailed information about these DBIAs, log in to FORUM and select the  *Integration Agreements Menu*  [DBA IA ISC] option located under the  *DBA*  [DBA] option (Data Base Administrator). Once in the Integration Agreements Menu Option, select “Inquire” and type  **BCMA**  at the “Select INTEGRATION REFERENCES:” prompt.  #### Remote Procedure Calls (RPCs)  Following is a list of Remote Procedure Calls associated with BCMA.  1   PSB ALLERGY 2   PSB BAG DETAIL 3   PSB CHECK IV 4   PSB CHECK SERVER 5   PSB COVERSHEET1 6   PSB CPRS ORDER 7   PSB DEVICE 8   PSB FMDATE 9   PSB GETINJECTIONSITE 10   PSB GETIVPAR 11  PSB GETORDERTAB 12  PSB GETPRNS 13  PSB GETPROVIDER 14  PSB GETSETWP 15  PSB INSTRUCTOR 16  PSB IV ORDER HISTORY 17  PSB LOCK 18  PSB MAIL 19  PSB MAN SCAN FAILURE 20  PSB MAXDAYS 21  PSB MED LOG LOOKUP 22  PSB MEDICATION HISTORY 23  PSB MOB DRUG LIST 24  PSB NURS WARDLIST 25  PSB PARAMETER 26  PSB PUTIVPAR 27  PSB REPORT 28  PSB SCANMED 29  PSB SCANPT 30  PSB SERVER CLOCK VARIANCE 31  PSB SUBMIT MISSING DOSE 32  PSB TRANSACTION 33  PSB USERLOAD 34  PSB USERSAVE 35  PSB UTL XSTATUS SRCH 36  PSB VALIDATE ESIG 37  PSB VALIDATE ORDER 38  PSB VERSION CHECK 39  PSB VITAL MEAS FILE 40  PSB VITALS 41 PSB WARDLIST   |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


## Internal and External Relations

| External Relations (cont.)   | #### VHIC 4.0 Card Bar Code Scanning Support  To incorporate lookup of patients by scanning the bar code on the new VIC 4.0 card or a DoD CAC card, a new supported API (RPCVIC^DPTLK) from dependent patch DG*5.3*857 has been incorporated into PSB SCANPT, which returns a patient DFN for lookup in BCMA.   |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Glossary

| Learning BCMA V. 3.0 Lingo   | The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.   |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|

Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

| Acronym/Term            | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Archive                 | To transfer files from a computer onto long-term storage.                                                                                                                                                                                                                                                                                                                                                                                                         |
| BCMA Clinical Reminders | A marquee located in the lower, right-hand corner of the BCMA VDL that identifies PRN medication orders needing effectiveness documentation. The setting is based on the “PRN Documentation” site parameter, and applies to current admissions or the site parameter timeframe (whichever is greater). A mouse-over list displays when the pointer is placed over the PRN Effectiveness Activity, or a full list is available by double clicking on the Activity. |
| CHUI                    | **Ch**  aracter-based  **U**  ser  **I**  nterface.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Client                  | An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.                                                                                                                                                                                                                                                                                                           |
| CPRS                    | **C**  omputerized  **P**  atient  **R**  ecord  **S**  ystem. A  software application that allows users to enter patient orders into different packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.                                                             |
| Data Dictionary         | Also called “DD,” the dictionary that contains file attributes.                                                                                                                                                                                                                                                                                                                                                                                                   |
| DBIA                    | **D**  ata  **b**  ase  **I**  ntegration  **A**  greement. A formal understanding between two or more application packages which describes how data is shared or how packages interact. This Agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.                                                                                                                           |
| FileMan                 | The  database management system.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| GUI                     | **G**  raphical  **U**  ser  **I**  nterface. The type of interface chosen for BCMA V. 3.0.                                                                                                                                                                                                                                                                                                                                                                       |
| IV                      | A medication given intravenously (within a vein) to a patient from an IV bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.                                                                                                                                                                                                                                                                                                          |
| Journaling              | A record of changes made in files and messages transmitted. It is quite useful when recovering previous versions of a file before updates were made, or to reconstruct updates if an updated file gets damaged.                                                                                                                                                                                                                                                   |
| LIMITED ACCESS BCMA     | A mode in which BCMA can be accessed that provides medication administering users the ability to access patient records for non-medication administration documentation, review and reporting purposes without being at the patient’s bedside.                                                                                                                                                                                                                    |

## Glossary

| Learning BCMA V. 3.0 Lingo (cont.)   | The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|

Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

| Acronym/Term                  | Definition                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAH                           | **M**  edication  **A**  dministration  **H**  istory. A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The date column lists three asterisks (***) if a medication was Discontinued.                       |
| MAR                           | **M**  edication  **A**  dministration  **R**  ecord. The traditional, handwritten record used for noting when a patient received a medication. BCMA V. 3.0 replaces this record with an MAH.                                                                                                                                                                              |
| NOW Order                     | A medication order given ASAP to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the BCMA VDL, as defined by the order Start and Stop Date/Time.                                                                                                                                               |
| Patient Transfer Notification | A message that displays when a patient’s record is opened or the Unit Dose or IVP/IVPB Medication Tab is viewed for the first time. This message indicates that the patient has had a movement type (usually a transfer) within the site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe. |
| PRN Order                     | The Latin abbreviation for  **P**  ro  **R**  e  **N**  ata. A medication dosage given to a patient on an “as needed” basis.                                                                                                                                                                                                                                               |
| PSB CPRS MED BUTTON           | The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and NOW (One-Time) medication orders using the CPRS Med Order Button on the BCMA VDL.                                                                                                                                                                              |
| PSB INSTRUCTOR                | The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.                                                                                                                                                                                                             |
| PSB MANAGER                   | The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.                                                                                                                                                                                                                                            |
| PSB READ ONLY                 | The name of the security “key” that must be assigned to users that can only access BCMA in Read-Only mode. Users who are assigned the PSB READ ONLY security key will never be able to administer medications or perform any actions against a patient’s medical record. The PSB READ ONLY security key overrides all other BCMA security keys.                            |

## Glossary

| Learning BCMA V. 3.0 Lingo (cont.)   | The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|

Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

| Acronym/Term       | Definition                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSB STUDENT        | The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options within BCMA V. 3.0. This key also requires that a nursing instructor sign on to BCMA.                                                                                                                                                             |
| PSB UNABLE TO SCAN | The name of the security “key” that must be assigned to allow the user to run the Unable to Scan (Detailed and Summary) reports.                                                                                                                                                                                                                                                               |
| Purge              | To delete a set of data, and all references to the data.                                                                                                                                                                                                                                                                                                                                       |
| Read-Only BCMA     | A mode in which BCMA can be accessed that provides non-medication administering users the ability to view a patient’s BCMA VDL and print reports, without performing any actions against a patient’s medical record.                                                                                                                                                                           |
<!-- rpc-table -->
| RPC                | **R**  emote  **P**  rocedure  **C**  all. A procedure stored on the VistA Server, which is executed to return data to the Client.                                                                                                                                                                                                                                                             |
<!-- rpc-table -->
| RPC Broker         | A Client/Server System within the VA’s Veterans Health Information Systems and Technology Architecture () environment. It enables client applications to communicate and exchange data with M Servers.                                                                                                                                                                                         |
| Security Keys      | Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.                                                                                                                                                                                                                          |
| Server             | An architecture in which one computer can get information from another. The Server, which can be anything from a personal computer to a mainframe, supplies the requested data or services to the Client.                                                                                                                                                                                      |
| STAT Order         | A medication order given immediately to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the BCMA VDL, as defined by the order Start and Stop Date/Time.                                                                                                                                                            |
| VDL                | **V**  irtual  **D**  ue  **L**  ist. An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.  **Note:**  This is called BCMA VDL in this guide to eliminate confusion with the VA Software Document Library (VDL) also mentioned in this guide. |
|                    | **V**  eterans Health  **I**  nformation  **S**  ystems and  **T**  echnology  **A**  rchitecture.                                                                                                                                                                                                                                                                                             |
| Ward Stock         | Unit Dose and IV medications that are “stocked” on an ongoing basis on wards and patient care areas. They are packaged in a ready-to-use form or compounded by the medication administrator.                                                                                                                                                                                                   |
| ZPL                | **Z**  ebra  **P**  rogramming  **L**  anguage.                                                                                                                                                                                                                                                                                                                                                |

## Appendix A: Processing of Schedule Information

| How BCMA Processes Schedule Information   | This section describes how BCMA V. 3.0 processes Schedule information from Inpatient Medications V. 5.0, and how it determines when to display a Continuous medication order on the BCMA VDL. Keep in mind that BCMA displays medication orders on the BCMA VDL between the order Start and Stop Date and Time.  The information provided below defines term used in this section:  **Admin Time:**  The ADMIN TIMES field (#41) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the ADMINISTRATION TIMES field (#.12) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).  **Frequency:**  The FREQUENCY field (#42) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the SCHEDULE INTERVAL field (#.17) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).  **Schedule:**  The SCHEDULE field (#26) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the SCHEDULE field (#.09) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).  **Schedule Type:**  The SCHEDULE TYPE field (#7) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55). For IV orders, it refers to the pseudo-type determined by Inpatient Medications that is sent to BCMA.   |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Steps for Processing Schedule Information | This section describes the steps for processing schedule information from Inpatient Medications to BCMA.  BCMA checks the Inpatient Medications order for a Schedule Type of “Continuous.”  If a Schedule Type other than “Continuous” is listed, BCMA quits processing the order, and proceeds to the correct processing method for that order’s Schedule Type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Appendix A: Processing of Schedule Information

| Steps for Processing Schedule Information (cont.)   | BCMA verifies information provided in the Schedule of the Inpatient Medications order.  If the Schedule is blank, BCMA quits processing the order and sends a Due List Error Notification message. (  **Note:**  A blank indicates that no Schedule was specified.)  If the Schedule lists a Day of the Week (i.e.,  [MO-WE@1200](mailto:MO-WE@1200)  ), BCMA checks the Admin Time(s) for the correct two- or four-digit format (i.e., 12-14, 1200, 1400).  If an Admin Time is listed, BCMA displays the order on the BCMA VDL, on specified days, using the Admin Time.  If no Admin Time is listed, BCMA quits processing the order and sends a Due List Error Notification message.  If the Schedule lists an Admin Time (i.e., 12-14, 1200, 1400), BCMA checks the Admin Time in the Inpatient Medications order.  If the Admin Time is blank, BCMA quits processing the order and sends a Due List Error Notification message.  If an Admin Time is listed, BCMA verifies for the correct two- or four-digit format (i.e., 12-14, 1200, 1400). If  **valid**  , BCMA displays the order on the BCMA VDL every day using the Admin Time provided. If  **invalid**  , BCMA quits processing the order and sends a Due List Error Notification message.  BCMA verifies information provided in the Frequency of the Inpatient Medications order.  **(Note:**  The Frequency is the amount of time between medication administrations.)  If the Frequency is blank, contains a letter other than “O” (the letter), or lists a Frequency less than one minute, BCMA quits processing the order and sends a Due List Error Notification message. (  **Note:**  A blank indicates that no Frequency was specified.)  If the Frequency lists “O” (the letter), BCMA converts the Frequency to 1440 minutes (one day) and proceeds to Step #4.   |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix A: Processing of Schedule Information

| Steps for Processing Schedule Information (cont.)   | BCMA verifies whether the order contains an Odd Schedule by determining that data in the order Frequency is not divisible by 1440 minutes (one day), and that 1440 minutes is not divisible by the data in the order Frequency. See the examples provided below.  If the order contains an Odd Schedule and times in the Admin Time, BCMA quits processing the order and sends a Due List Error Notification message.  If the order contains an Odd Schedule, but no times in the Admin Time, BCMA displays the medication order on the BCMA VDL using the Frequency and order Start Date/Time provided by Inpatient Medications to calculate the Admin Times.  If the order does  *not*  contain an Odd Schedule and no times are listed in the Admin Time, BCMA displays the medication order on the BCMA VDL using the Frequency and order Start Date/Time provided by Inpatient Medications to calculate the Admin Times.  If the order does  *not*  contain an Odd Schedule, but times are listed in the Admin Time, BCMA verifies the Frequency listed in the order.  If the Frequency is  *less than*  1440 minutes (or one day), BCMA displays the medication order on the BCMA VDL every day, based on the Admin Times provided in the order.  If the Frequency is  *greater than*  1440 minutes (or one day), BCMA uses the Frequency information from Inpatient Medications to determine which day to display the medication order on the BCMA VDL, based on the Admin Time provided in the order.   |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix A: Processing of Schedule Information

| Steps for Processing Schedule Information (cont.)   | This section provides examples showing Schedule Types that are processed as Odd Schedules and those that are not.  **Note:**  For an Odd Schedule to occur, both statements for a Schedule Type must be False.  #### Examples of Odd Schedules  Schedule Type: Q5H (300 minutes)  300 minutes divided by 1440 minutes = fraction, not a whole number = False  1440 divided by 300 minutes = 4.8 (fraction, not a whole number) = False  Schedule Type: Q3XM (13440 minutes)  13440 minutes divided by 1440 minutes = 9.3 (fraction, not a whole number) = False  1440 divided by 13440 minutes = fraction, not a whole number = False  #### Examples of Schedules That Are Not Odd Schedules  Schedule Type: Q2H (120 minutes)  120 minutes divided by 1440 minutes = 8.3 (fraction, not a whole number) = False  1440 minutes divided by 120 = 12 (whole number) = True  Schedule Type: QOD (2880 minutes)  2880 minutes divided by 1440 minutes = 2 (whole number) = True  1440 minutes divided by 2880 = 0.5 (fraction, not a whole number) = False   |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix B: HL7 Messaging for BCMA

| Sample HL7 Data Fields Broadcast to BCMA Subscribers   | BCMA includes the Standards from the HL7 V. 2.4 (VistA Messaging) package. For more information, refer to the VistA Messaging and Interface Services Web site at: REDACTED.  This section provides a list of sample Health Level Seven (HL7) data fields that BCMA broadcasts to BCMA HL7 subscribers. Review the information to learn the “RAS” messages created for the administration and/or update of a medication order. The activities, which cause the broadcast of BCMA HL7 messages, are called “trigger events.” BCMA HL7 trigger events are MEDPASS, UPDATE STATUS, PRN EFFECTIVENESS, and ADD COMMENT.  **Note:**  Every message will not use every data field and every segment provided. Some segments may repeat as necessary. Some segments may not appear in the exact order depicted below for all trigger events, but they will be consistent for each specific trigger event.   |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: “RAS” Messages Created for the Administration of a Medication Order

| SEG   |   SEQ | Field Name                      | Example             | HL7 Type                                   |
|-------|-------|---------------------------------|---------------------|--------------------------------------------|
|       |       |                                 |                     |                                            |
| MSH   |     1 | Field Separator                 | ^                   | string                                     |
|       |     2 | Encoding Characters             | ~&#124;\&           | string                                     |
|       |     3 | Sending Application             | PSB HL7 SRV         | hierarchic designator                      |
|       |     4 | Sending Facility                |                     | hierarchic designator                      |
|       |     5 | Receiving Application           | PSB HL7 SUB         | hierarchic designator                      |
|       |     6 | Receiving Facility              |                     | hierarchic designator                      |
|       |     7 | D/T of Message                  | 20030530075514-0600 | HL7 format timestamp (yyyymmddhhnnss-0600) |
|       |     8 | Security                        |                     | string                                     |
|       |     9 | Message Type                    | RAS~O17             | composite                                  |
|       |    10 | Message Control ID              | 5001457             | string                                     |
|       |    11 | Processing ID                   | P                   | processing type                            |
|       |    12 | Version ID                      | 2.4                 | ID                                         |
|       |    13 | Sequence Number                 |                     | numeric                                    |
|       |    14 | Continuation Pointer            |                     | string                                     |
|       |    15 | Accept Acknowledgement Type     |                     | ID                                         |
|       |    16 | Application Acknowledgment Type | NE                  | ID                                         |
|       |    17 | Country Code                    |                     | ID                                         |
|       |    18 | Character Set                   |                     | ID                                         |
|       |    19 | Principal Language of Message   |                     | coded element                              |

## Appendix B: HL7 Messaging for BCMA

Example: “RAS” Messages Created for the Administration of a Medication Order
(cont.)

| SEG   |   SEQ | Field Name                                    | Example                         | HL7 Type                                             |
|-------|-------|-----------------------------------------------|---------------------------------|------------------------------------------------------|
|       |       |                                               |                                 |                                                      |
| PID   |     3 | Patient Identifier List                       | 748                             | composite ID                                         |
|       |     4 | Alternate Patient ID                          | 54~~~~AGE                       | extended composite ID                                |
|       |     5 | Patient Name                                  | BCMAPATIENT~TWO                 | patient name                                         |
|       |     7 | Date/Time of Birth                            | 19490101                        | HL7 format timestamp (yyyymmdd)                      |
|       |     8 | Administrative Sex                            | M                               | user table                                           |
|       |    19 | SSN Number (VA)  or HRN Number (IHS)– Patient | 000001000 (VA)  or 123456 (IHS) | string                                               |
| PV1   |     2 | Patient Class                                 | U                               | table 0004                                           |
|       |     3 | Patient Location                              | 7A GEN MED 724-A~~~500          | user table                                           |
|       |     7 | Attending Doctor                              | BCMAPROVIDER~ONE                | composite ID                                         |
| ORC   |     1 | Order Control                                 | XX                              | table 119                                            |
|       |     2 | Placer Order Number                           | 1045~PSB~1045~IEN               | entity identifier                                    |
|       |     3 | Filler Order Number                           | 13V                             | entity identifier                                    |
|       |     7 | Quantity/Timing                               | ~~~~~~~~~C                      | dosage, scheduled administration time, schedule type |
|       |     8 | Parent                                        | ~                               | composite                                            |
|       |     9 | D/T of Transaction                            | 20030530075514-0600             | HL7 format timestamp (yyyymmddhhnnss-0600)           |
|       |    10 | Entered by                                    | BCMANURSE~ONE                   | extended composite name                              |
|       |    15 | Order Effective D/T                           | 20030530075514-0600             | HL7 format timestamp (yyyymmddhhnnss-0600)           |
|       |    19 | Action By                                     | BCMANURSE~ONE                   | extended composite name                              |
| RXR   |     1 | Route                                         | IV                              | table 0162                                           |
|       |     2 | Administration Site                           | 3 INJECTION SITE                | table 0163                                           |
| RXO   |     1 | Requested Give Code                           | 269~FLUOROURACIL                | coded element                                        |
|       |     2 | Requested Give Amount                         |                                 | numeric                                              |
|       |    10 | Requested Dispense Code                       | 748V52                          | coded element                                        |
|       |    21 | Requested Give Rate Amount                    | ~250 ml/hr                      | string                                               |

## Appendix B: HL7 Messaging for BCMA

Example: “RAS” Messages Created for the Administration of a Medication Order
(cont.)

| SEG   |   SEQ | Field Name                         | Example                                        | HL7 Type                                                             |
|-------|-------|------------------------------------|------------------------------------------------|----------------------------------------------------------------------|
|       |       |                                    |                                                |                                                                      |
| RXC   |     1 | RX Component Type                  | A                                              | table 0166                                                           |
|       |     2 | Component Code                     | 20~5-FLUOURACIL                                | coded element                                                        |
|       |     3 | Component Amount                   | 5-FLUOURACIL                                   | numeric                                                              |
|       |     4 | Component Units                    |                                                | coded element                                                        |
| RXC   |     1 | RX Component Type                  | B                                              | table 0166                                                           |
|       |     2 | Component Code                     | 8~AMINO ACID SOLUTION 8.5%                     | coded element                                                        |
|       |     3 | Component Amount                   | AMINO ACID SOLUTION 8.5%                       | numeric                                                              |
|       |     4 | Component Units                    |                                                | coded element                                                        |
| RXA   |     1 | Give Sub-ID Counter                | 0                                              | number                                                               |
|       |     2 | Administration Sub-ID Counter      | 1                                              | number                                                               |
|       |     3 | Date/Time Start of Administration  | 20030530075514-0600                            | HL7 format timestamp (yyyymmddhhnnss-0600)                           |
|       |     5 | Administered Code                  | 20~5-FLUOURACIL                                | coded element                                                        |
|       |     6 | Administered Amount                | 450 MG                                         | number                                                               |
|       |     7 | Administered Unit                  |                                                |                                                                      |
|       |     9 | Administration Notes               |                                                | coded element                                                        |
|       |    18 | Substance/Treatment Refusal Reason | ~Elevated Blood Sugar                          | coded element                                                        |
|       |    19 | Indication                         | ~                                              | coded element                                                        |
|       |    20 | Completion Status                  | C                                              | user table                                                           |
| NTE   |     2 | Source of Comment                  |                                                | table 105                                                            |
|       |     3 | Comment                            | This is a comment …                            | free text                                                            |
|       |     4 | Comment Type                       | BCMANURSE~ONE~20030530075514-0600~Date Entered | coded element  (includes HL7 format timestamp [yyyymmddhhnnss-0600]) |

## Appendix B: HL7 Messaging for BCMA

| Definitions of Data Fields Under FIELD NAME Column   | This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field. The message header (i.e., the MSH segment) is constructed and supported by the VistA HL7 message development tool.  **Note:**  The MSH segment field names are  *not*  described below.  **PATIENT ID:**  Field (#.01) of the BCMA MEDICATION LOG file (#53.79) and Internal Entry Number (IEN) pointer to the PATIENT file (#2).  **PATIENT NAME:**  As returned by the Application Program Interface (API) VADPT.  **DATE OF BIRTH:**  As returned by the API VADPT.  **ADMINISTRATIVE SEX:**  As returned by the API VADPT.  SSN NUMBER (VA) or HRN NUMBER (IHS): As returned by the API VADPT.  **PATIENT LOCATION:**  Field (#.02) of the BCMA MEDICATION LOG file (#53.79), which contains the actual room-bed and ward location of the patient at the time the medication pass occurred. Also contains field (#.03) of the BCMA MEDICATION LOG file (#53.79), which contains the division number of the ward that the patient was on during the medication pass.  **PLACER ORDER NUMBER:**  IEN for the BCMA MEDICATION LOG file (#53.79).  **FILLER ORDER NUMBER:**  Contains the ORDER REFERENCE NUMBER field (#.11) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN of the actual medication order from the PHARMACY PATIENT file (#55)PREVIOUS ORDER NUMBER as returned by the API PSJBCMA1.  **QUANTITY/TIMING:**  Contains the order dosage, schedule type, and scheduled administration time data from the BCMA MEDICATION LOG file (#53.79), fields #.15, #.12, and #.13 respectively.  **PARENT:**  Contains the PREVIOUS ORDER NUMBER as returned by the PSB routine PSBVT.  **DATE/TIME OF TRANSACTION:**  Contains the ACTION DATE/TIME field (#.06) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time of the actual time that the action was taken.   |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix B: HL7 Messaging for BCMA

| Definitions of Data Fields Under FIELD NAME Column (cont.)   | This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.  **ENTERED BY:**  Field (#.05) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN pointer to the NEW PERSON file (#200) for the user who entered the data, along with the actual name of that person as returned by FileMan.  **ORDER EFFECTIVE DATE/TIME:**  Provides data from the ENTERED DATE/TIME field (#.04) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time that the action was taken.  **ACTION BY:**  Field (#.07) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN pointer to the NEW PERSON file (#200) for the user who took the action.  **ROUTE:**  Contains  data as returned by the PSB routine PSBVT. The ROUTE data is required for the RXR message segment.  **ADMINISTRATION SITE:**  Presents the INJECTION SITE field (#.16) of the BCMA MEDICATION LOG file (#53.79), which lists the injection site where the medication was administered.  **REQUESTED GIVE CODE:**  Presents the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), containing a pointer to the ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.  **REQUESTED GIVE AMOUNT:**  Provides the ORDER DOSAGE field (#.15) of the BCMA MEDICATION LOG file (#53.79), which contains the dosage from the original medication order.  **REQUESTED DISPENSE CODE:**  Presents the IV UNIQUE ID field (#.26) of the BCMA MEDICATION LOG file (#53.79), which contains the unique ID number for an IV bag.  **REQUESTED GIVE RATE AMOUNT:**  Presents the INFUSION RATE field (#.35) of the BCMA MEDICATION LOG file (#53.79), which contains the infusion rate for an IV bag.  **RX COMPONENT TYPE:**  Contains data specifying the “type” of item/component processed. Within the HL7 standard table, “A” signifies additive and “B” signifies base.   |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix B: HL7 Messaging for BCMA

tip:

The RXC segment may repeat, once for each solution and each additive, in an IV medication order. The RX COMPONENT TYPE is “A” for an additive” and “B” for a solution.

| tip:  The RXC segment may repeat, once for each solution and each additive, in an IV medication order. The RX COMPONENT TYPE is “A” for an additive” and “B” for a solution.  <!-- image -->  <!-- image -->  ### Definitions of Data Fields Under FIELD NAME Column (cont.)   | This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.  **COMPONENT CODE:**  Presents the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), containing a pointer to the ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.  **COMPONENT AMOUNT:**  Presents the DOSES ORDERED field (#.02) within the DISPENSE DRUG multiple (#.5) within the BCMA MEDICATION LOG file (#53.79), which contains the number of units.  **COMPONENT UNITS:**  Consists of the UNIT OF ADMINISTRATION field (#.04) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the unit(s) for the medication administered.  **GIVE SUB-ID COUNTER:**  A required field with a value of “00.”  **ADMINISTRATION SUB-ID COUNTER:**  A required field with a numeric value.  **DATE/TIME START OF ADMINISTRATION:**  Presents the ACTION DATE/TIME field (#.06) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time that the action was taken.  **ADMINISTERED CODE:**  Composed of the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), which contains a pointer to ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.  **ADMINISTERED AMOUNT:**  Consists of the DOSES GIVEN field (#.03) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the actual number of units administered to the patient.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix B: HL7 Messaging for BCMA

| Definitions of Data Fields Under FIELD NAME Column (cont.)   | This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.  **ADMINISTERED UNIT:**  UNIT OF ADMINISTRATION field (#.04) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the unit(s) for the medication administered.  **ADMINISTRATION NOTES:**  Consists of the AUDIT LOG field (#.9) and the AUDIT LOG field (#.01) of the AUDIT LOG multiple (#.9) within the BCMA MEDICATION LOG file (#53.79).  **SUBSTANCE/TREATMENT REFUSAL REASON:**  Field (#.21) of the BCMA MEDICATION LOG file (#53.79), which contains the PRN reason for administering a PRN medication.  **INDICATION:**  Consists of the ORDER ADMINISTRATION VARIANCE field (#.14), of the BCMA MEDICATION LOG file (#53.79), which if a Continuous medication order, will contain the minutes early (&lt;1) or late (&gt;1) that the medication was administered.  **COMPLETION STATUS:**  Consists of the ACTION STATUS field (#.09) of the BCMA MEDICATION LOG file (#53.79), which contains the status of the medication pass. Values in this field will equal an ACTION STATUS value.  **SOURCE OF COMMENTS:**  “O” source of the subsequent message.  **COMMENT:**  Contains the PRN EFFECTIVENESS field (#.22) of the BCMA MEDICATION LOG file (#53.79). When appropriate, contains a composite of the COMMENT field (#.3) and the COMMENT field (#.01) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the comments entered.  **COMMENT TYPE:**  Contains a composite of the ENTERED BY field (#.02) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the pointer to the NEW PERSON file (#200) for the user that entered the comment; along with the actual name of the user as returned by FileMan; as well as the ENTERED DATE/TIME field (#.03) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the date and time that the entry was filed and the string “Date Entered.”   |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix B: HL7 Messaging for BCMA

| Sample HL7 Data Fields Passed in Each Trigger Event   | This section identifies the HL7 data fields that are passed in each of the four “trigger events” associated with BCMA, and examples of medication administrations. The processed trigger events are MEDPASS, UPDATE STATUS, PRN EFFECTIVENESS, and ADD COMMENT. For each event, there is an order control code and a set of data fields listed. For any given event; however, some of the data fields may be empty. Administration Notes is such an example.  The protocols provided in the table, use the BCMA name spacing convention (“PSB”), as do the messages sent by BCMA. The BCMA HL7 messages are unsolicited; therefore, acknowledgment messages are unnecessary and not recognized by the PSB protocol.  **Note:**  Word wrapping is in effect for the example Medications Administrations on the following pages.   |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Data Fields Passed in Each Trigger Event Associated with BCMA HL7

| Action        | Broadcast from BCMA                                                                                                                                                        | Subscribing Application   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
|               |                                                                                                                                                                            |                           |
| MEDPASS       |                                                                                                                                                                            |                           |
| Protocol      | PSB RAS O17 SRV                                                                                                                                                            | PSB RAS O17 SUB           |
| Order Control | XX (Order/service changed)                                                                                                                                                 |                           |
| HL7 Fields    | MSH (as prepared by HL7 tool)  PID: 3,4,5,7,8,19  PV1: 2,3,7  ORC: 1,2,3,7,8,9,10,15,19  RXO: 1,2,10,21  NTE: 2,3,4  RXR: 1,2  RXC: 1,2,3,4  RXA: 1,2,3,4,5,6,7,9,18,19,20 |                           |

## Appendix B: HL7 Messaging for BCMA

Example: Medication Administrations

| ###### MEDPASS  Message:  MESSAGE HEADER:  MSH^~&#124;\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530075514-0600^^RAS~O17^5001559^P^2.4^^^^NE^  MESSAGE TEXT:  PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000  PV1^^U^7A GEN MED 724-A~~~500^^^^BCMANURSE~ONE  ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^200305300755140-600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE  RXO^269~FLUOROURACIL^^^^^^^^^748V52^^^^^^^^^^^~250 ml/hr  NTE^^O^1~This is a comment...^BCMANURSE~ONE~20030530075514-0600~Date Entered  RXR^IV^3 INJECTION SITE  RXC^A^20~5-FLUOURACIL^5-FLUOURACIL^  RXC^B^8~AMINO ACID SOLUTION 8.5%^AMINO ACID SOLUTION 8.5%^  RXA^0^1^20030530075514-0600^ ^20~5-FLUOURACIL^450 MG^^^^^^^^^^^^^~^I  RXA^0^2^20030530075514-0600^ ^8~AMINO ACID SOLUTION 8.5%^500 ML^^^^^^^^^^^^^~^I  ###### UPDATE STATUS  Message:  MESSAGE HEADER:  MSH^~&#124;\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530090340-0600^^RAS~O17^5001561^P^2.4^^^^NE^  MESSAGE TEXT:  PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000  PV1^^U^7A GEN MED 724-A~~~500^^^^BCMANURSE~ONE  ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^200305300903400-600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE  RXO^269~FLUOROURACIL^^^^^^^^^748V52^^^^^^^^^^^~250 ml/hr  NTE^^O^2~Add this comment to the administration...^BCMANURSE~ONE~20030530082444-0600~Date Entered  RXR^IV^3 INJECTION SITE  RXC^A^20~5-FLUOURACIL^5-FLUOURACIL^  RXC^B^8~AMINO ACID SOLUTION 8.5%^AMINO ACID SOLUTION 8.5%^  RXA^0^1^20030530090340-0600^ ^20~5-FLUOURACIL^450 MG^^^4~20030530090340-0600^^^^^^^^^^~^C  RXA^0^2^20030530090340-0600^ ^8~AMINO ACID SOLUTION 8.5%^500 ML^^^4~20030530090340-0600^^^^^^^^^^~^C   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Appendix B: HL7 Messaging for BCMA

Example: Medication Administrations (cont.)

###### PRN EFFECTIVENESS

Message:

MESSAGE HEADER:

MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530110049-0600^^RAS~O17^5001562^P^2.4^^^^NE^

MESSAGE TEXT:

PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000

ORC^XX^1040~PSB~1040~IEN^28U^^^^13oz~Q6H~~~~~~~~P^~^20030529132246-0600^BCMANURSE~ONE^^^^^20030529132246-0600^^^^BCMANURSE~ONE

NTE^^O^ Effectiveness comment for   admin...^BCMANURSE~ONE~20030530110049-0600~Date Entered~~1298~PRN Minutes

###### ADD COMMENT

Message:

MESSAGE HEADER:

MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530082444-0600^^RAS~O17^5001560^P^2.4^^^^NE^

MESSAGE TEXT:

PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000

ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^20030530075514-0600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE

NTE^^O^2~Add this comment to the administration...^BCMANURSE~ONE~20030530082444-0600~Date Entered

## Appendix C: Interfacing with the Bar Code Label Printer

| Introduction   | The Bar Code Medication Administration (BCMA) Medication package includes an interface between the  *Label Print*  [PSBO BL] option and the bar code label printer. The  *Label Print*  [PSBO BL] option currently prints Unit Dose labels on a label printer. This interface allows a unique bar code to be printed on the first line of the Unit Dose label.  Since users can now customize their own label formats using control codes, it is important to note that all Unit Dose and Ward Stock medication labels must conform to the JCAHO Standard for Medication Labeling (Standard MM.4.30). Please refer to the excerpt of the standard and references at the end of this Appendix.  Any printer that supports bar code printing can be used for the Unit Dose labels. However, the scan success rate will probably be lower if anything other than direct thermal transfer on synthetic labels is used. Labels from dot matrix printers, laser printers, or even bar code printers using other types of transfer, wipe off more easily. The label could become unreadable, especially in areas where the bag might become wet. With a direct thermal transfer onto a synthetic label, the print actually bonds to the label material. Essentially, the label would have to be ripped to damage the print.   |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hardware Setup | The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Software Setup | The type of printer will determine the next step. The Zebra and Intermec printers require control codes, where the dot matrix or laser printers do not require these codes. The Unit Does print routine checks the existence of the control codes before attempting to execute. It is not required for all control codes to be defined; just build the necessary control codes for the selected printer.  When setting up the Terminal Type file for the Zebra bar code printer device, the Terminal Type file entry must contains the word “ZEBRA” as part of the file name.  For example: P-ZEBRA  When setting up the Terminal Type file for the Intermec bar code printer device, the Terminal Type file entry must contains the word “INTERMEC” as part of the file name.  ## For example: P-INTERMEC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Appendix C: Interfacing with the Bar Code Label Printer

| ### Software Setup (cont’d)   | The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.  #### Printer Control Codes  For this type of printer to print a unique bar code on the Unit Dose labels, IRMs must build control codes. The CONTROL CODES fields [#55] are added to the TERMINAL TYPE file (#3.2) in the Kernel patch XU*8*205.  **This patch must be installed before proceeding**  .  #### Control Code Set Up  The Unit Dose label print routine currently uses printer control codes and code names that are built within FileMan. The following table illustrates the control codes and corresponding names for the Zebra printer.   |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Zebra Printer Terminal Type Control Codes

| Abbreviation   | Full Name               | Control Code                                                                                                                                                                                                                    |
|----------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ET             | End Text                | N/A                                                                                                                                                                                                                             |
| ETF            | End Text Field          | N/A                                                                                                                                                                                                                             |
| EB             | End Barcode             | W !,"^FO20,150^A0N,30,20^CI13^FR^FD"_TEXT_"^FS"                                                                                                                                                                                 |
| EBF            | End Barcode Field       | N/A                                                                                                                                                                                                                             |
| EL             | End Label               | W !,"^XZ"                                                                                                                                                                                                                       |
| FE             | Format End              | N/A                                                                                                                                                                                                                             |
| FI             | Format Initialization   | N/A                                                                                                                                                                                                                             |
| FI1            | Format Initialization 1 | N/A                                                                                                                                                                                                                             |
| FI2            | Format Initialization 2 | N/A                                                                                                                                                                                                                             |
| HAZ            | Hazardous Text          | S PSBTYPE=$S(PSBTLE="HAZTEXT":"20,60",1:"0,0")                                                                                                                                                                                  |
| SB             | Start Barcode           | =$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N") S:PSBSYM="" PSBBAR="NO-CODE"  W !,"^BY2,3.0^FO20,100^"_PSBTYPE_",N,80,Y,N^FR^FD"_PSBBAR_"^FS"                                                                                |
| SBF            | Start Barcode Field     | N/A                                                                                                                                                                                                                             |
| SL             | Start Label             | W !,"^XA",!,"^LH0,0^FS"                                                                                                                                                                                                         |
| ST             | Start Text              | W !,"^FO"_PSBTYPE_"^A0N,30,20^CI13^FR^FD"_TEXT_"^FS"                                                                                                                                                                            |
| STF            | Start Text Field        | S PSBTYPE=$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60", PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90", PSBTLE="PSBLOT":"350,120", PSBTLE="PSBEXP":"350,150", PSBTLE="PSBMFG":"500,150", PSBTLE="PSBFCB":"350,180" |

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | The field position map below identifies the specific control codes for the Zebra printer that direct the exact position in which the fields are printed on the bar code label.   |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Zebra Bar Code Label - Field Position Map

| Abbreviation   | Control Code ( Field Coordinates)    | Description                        |
|----------------|--------------------------------------|------------------------------------|
| EB             | FO20,150                             | “No – Code” statement              |
| HAZ            | PSBTLE="HAZTEXT":"20,60"             | Hazardous to Handle and/or Dispose |
| SB             | FO20,100 "                           | Bar Code Graph                     |
| STF            | PSBTLE="PSBDRUG":"20,25"             | Drug Name                          |
| STF            | PSBTLE="PSBDOSE":"20,60",            | Dosage                             |
| STF            | PSBTLE="PSBNAME":"350,60"            | Patient Name and Quality           |
| STF            | PSBTLE="PSBWARD":"350,90",           | Ward Location                      |
| STF            | PSBTLE="PSBLOT":"350,120",           | Number                             |
| STF            | PSBTLE="PSBEXP":"350,150",           | Expiration Date                    |
| STF            | PSBTLE="PSBMFG":"500,150",           | Manufacturer                       |
| STF            | PSBTLE=”PSBFCB”:350,180”,            | Filled By/Checked By               |

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | The following table illustrates the control codes and corresponding names for the Intermec printer.   |
|---------------------------|-------------------------------------------------------------------------------------------------------|

Example: Intermec Printer Terminal Type Control Codes

| Abbreviation   | Full Name               | Control Code                                                                                                                                                                                                                       |
|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ET             | End Text                | N/A                                                                                                                                                                                                                                |
| ETF            | End Text Field          | N/A                                                                                                                                                                                                                                |
| EB             | End Barcode             | W "<STX>H8;o50,40;f3;c7;h2;w2;d0,80;<ETX>",!                                                                                                                                                                                       |
| EBF            | End Barcode Field       | N/A                                                                                                                                                                                                                                |
| EL             | End Label               | W "<STX><ETB><ETX>",!                                                                                                                                                                                                              |
| FE             | Format End              | N/A                                                                                                                                                                                                                                |
| FI             | Format Initialization   | W "<STX><ESC>C<ETX>",!,"<STX><ESC>P<ETX>",!,"<STX>E2;F2<ESC><ETX>",!                                                                                                                                                               |
| FI1            | Format Initialization 1 | W "&lt;STX&gt;H7;o30,260;f3;c7;h2;w2;d0,80;&lt;ETX&gt;",!,"&lt;STX&gt;H6;o50,440;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H5;o50,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H4;o70,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!  |
| FI2            | Format Initialization 2 | W "&lt;STX&gt;H3;o90,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H2;o110,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H1;o110,40;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H0;o130,40;f3;c7;h2;w2;d0,40;&lt;ETX&gt;",! |
| SB             | Start Barcode           | W "<STX>"_TEXT_"<ETX>",!                                                                                                                                                                                                           |
| SBF            | Start Barcode Field     | S PSBTYPE=$S(PSBSYM="I25":"c2,0",PSBSYM="128":"c6,0",1:"c0,0") W "<STX>B8;o85,40;f3;"_PSBTYPE_";i1;do,25;p@;<ETX>",!,"<STX>I8;h1;w1;<ETX>",!                                                                                       |
| SL             | Start Label             | W "<STX>R;<EXT>",!,"<STX><ESC>E2<EXT>",!                                                                                                                                                                                           |
| ST             | Start Text              | W "<STX>"_TEXT_"<CR><ETX>",!                                                                                                                                                                                                       |
| STF            | Start Text Field        | N/A                                                                                                                                                                                                                                |

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | The field position map below identifies the specific control codes for the Intermec printer that direct the exact position in which the fields are printed on the bar code label.   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Intermec Bar Code Label - Field Position Map

| Abbreviation   | Control Code ( Field Coordinates)                                                               | Description              |
|----------------|-------------------------------------------------------------------------------------------------|--------------------------|
| EB             | <STX>H8;o50,40;f3;c7;h2;w2;d0,80;<ETX>                                                          | “No – Code” statement    |
| FI1            | <STX>H7;o30,260;f3;c7;h2;w2;d0,80;<ETX>                                                         | Filled By/Checked By     |
| FI1            | <STX>H6;o50,440;f3;c7;h2;w2;d0,20;<ETX>"                                                        | Manufacturer             |
| FI1            | <STX>H5;o50,260;f3;c7;h2;w2;d0,20;<ETX>                                                         | Expiration Date          |
| FI1            | <STX>H4;o70,260;f3;c7;h2;w2;d0,20;<ETX>                                                         | Number                   |
| FI2            | <STX>H3;o90,260;f3;c7;h2;w2;d0,20;<ETX>                                                         | Ward Location            |
| FI2            | <STX>H2;o110,260;f3;c7;h2;w2;d0,20;<ETX>                                                        | Patient Name and Quality |
| FI2            | <STX>H1;o110,40;f3;c7;h2;w2;d0,20;<ETX>                                                         | Dosage                   |
| FI2            | <STX>H0;o130,40;f3;c7;h2;w2;d0,40;<ETX>                                                         | Drug Name                |
| SBF            | &lt;STX&gt;B8;o85,40;f3;"\_PSBTYPE\_";i1;do,25;p@;&lt;ETX&gt;  &lt;STX&gt;I8;h1;w1;&lt;ETX&gt;" | Bar code Graph           |

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | #### Example Terminal Type Files  The following are examples of terminal type file setups that were used in the development process. These examples are provided to guide the user in the setup process. Please note that they are only examples, and may not be appropriate for your configuration.   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Zebra Printer Sample Terminal Type File

NUMBER: 1                               ABBREVIATION: SL

FULL NAME: Start Label                CONTROL CODE: W !,"^XA",!,"^LH0,0^FS"

NUMBER: 2                               ABBREVIATION: EL

FULL NAME: End Label                  CONTROL CODE: W !,"^XZ"

NUMBER: 3                               ABBREVIATION: SB

FULL NAME: Start Barcode

CONTROL CODE: S PSBTYPE=$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N") S:PSBSYM="" PSBBAR="NO-CODE"  W !,"^BY2,3.0^FO20,100^"\_PSBTYPE\_",N,80,Y,N^FR^FD"\_PSBBAR\_"^FS"

NUMBER: 4                               ABBREVIATION: EB

FULL NAME: End Barcode

CONTROL CODE: W !,"^FO20,150^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 5                               ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 6                               ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S PSBTYPE=$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60", PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90", PSBTLE="PSBLOT":"350,120", PSBTLE="PSBEXP":"350,150", PSBTLE="PSBMFG":"500,150", PSBTLE="PSBFCB":"350,180",1:"0,0")

Example: Zebra Printer Sample Terminal Type File with HAZ Control Code

NAME: P-TCP-ZEB-UD-HAZ 200DPI

NUMBER: 1                               CTRL CODE ABBREVIATION: SL

FULL NAME: Start Label                CONTROL CODE: W !,"^XA",!,"^LH0,0^FS"

NUMBER: 2                               CTRL CODE ABBREVIATION: EL

FULL NAME: End Label                  CONTROL CODE: W !,"^XZ"

NUMBER: 3                               CTRL CODE ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 4                               CTRL CODE ABBREVIATION: SB

FULL NAME: Start Barcode

CONTROL CODE: S PSBTYPE=$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N,N")

S:PSBSYM="" PSBBAR="NO-CODE"  W !,"^BY2,3.0,80^FO20,115^"\_                                                      PSBTYPE\_",60,Y,N^FR^FD"\_PSBBAR\_"^FS"

NUMBER: 5                               CTRL CODE ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S SBTYPE=SPSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,85",

PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90",

PSBTLE="PSBLOT":"350,120",PSBTLE="PSBEXP":"350,150",

PSBTLE="PSBMFG":"500,150",PSBTLE="PSBFCB":"350,180",1:"0,0")

NUMBER: 6                               CTRL CODE ABBREVIATION: HAZ

FULL NAME: Hazardous Text Field

CONTROL CODE: S PSBTYPE=$S(PSBTLE="HAZTEXT":"20,60",1:"0,0")  CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 6                               ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S PSBTYPE=$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60",1:”0,0”)

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | The following shows a sample Intermec printer terminal type file.   |
|---------------------------|---------------------------------------------------------------------|

Example: Intermec Printer Sample Terminal Type File

NUMBER: 1                               ABBREVIATION: SL

FULL NAME: Start Label

CONTROL CODE: W "&lt;STX&gt;R;&lt;EXT&gt;",!,"&lt;STX&gt;&lt;ESC&gt;E2&lt;EXT&gt;",!

NUMBER: 2                               ABBREVIATION: EL

FULL NAME: End Label               CONTROL CODE: W "&lt;STX&gt;&lt;ETB&gt;&lt;ETX&gt;",!

NUMBER: 3                               ABBREVIATION: FI1

FULL NAME: Format Initialization 1

CONTROL CODE: W "&lt;STX&gt;H7;o30,260;f3;c7;h2;w2;d0,80;&lt;ETX&gt;",!,"&lt;STX&gt;H6;o50,440;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H5;o50,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H4;o70,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!

NUMBER: 4                               ABBREVIATION: FI2

FULL NAME: Format Initialization 2

CONTROL CODE: W "&lt;STX&gt;H3;o90,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H2;o110,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H1;o110,40;f3;c7;h2;w2;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H0;o130,40;f3;c7;h2;w2;d0,40;&lt;ETX&gt;",!

NUMBER: 5                               ABBREVIATION: SBF

FULL NAME: Start Barcode Field

CONTROL CODE: S PSBTYPE=$S(PSBSYM="I25":"c2,0",PSBSYM="128":"c6,0",1:"c0,0") W "&lt;STX&gt;B8;o85,40;f3;"\_PSBTYPE\_";i1;do,25;p@;&lt;ETX&gt;",!,"&lt;STX&gt;I8;h1;w1;&lt;ETX&gt;",!

NUMBER: 6                              ABBREVIATION: SB

FULL NAME: Start Barcode              CONTROL CODE: W "&lt;STX&gt;"\_TEXT\_"&lt;ETX&gt;",!

NUMBER: 7                              ABBREVIATION: EB

FULL NAME: End Barcode

CONTROL CODE: W "&lt;STX&gt;H8;o50,40;f3;c7;h2;w2;d0,80;&lt;ETX&gt;",!

NUMBER: 8                              ABBREVIATION: FI

FULL NAME: Format Initialization

CONTROL CODE: W "&lt;STX&gt;&lt;ESC&gt;C&lt;ETX&gt;",!,"&lt;STX&gt;&lt;ESC&gt;P&lt;ETX&gt;",!,"&lt;STX&gt;E2;F2&lt;ESC&gt;&lt;ETX&gt;",!

NUMBER: 9                              ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W "&lt;STX&gt;"\_TEXT\_"&lt;CR&gt;&lt;ETX&gt;",!

## Appendix C: Interfacing with the Bar Code Label Printer

| Software Setup (cont’d)   | #### Dot Matrix and Laser Printers  The control codes in the TERMINAL TYPE file (#3.2) are not required for dot matrix and laser printers. However, the BAR CODE ON field [#60] and BAR CODE OFF field [#61] in the TERMINAL TYPE file (#3.2) are needed.  An example of each field is shown below for the Output Technology Corporation (OTC) printers. Please note that it is only an example and  may not be appropriate for your configuration.   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: OTC Printer Example

BAR CODE OFF: $C(27),"[0t",!

BAR CODE ON:  $C(27),"[4;4;0;2;4;2;4;2}",$C(27),"[3t"

## Appendix C: Interfacing with the Bar Code Label Printer

| Printed Bar Code Unit Dose Label Sample   | With this interface, a unique bar code will be printed on the first line of the Unit Dose label with the label number printed below it. Depending upon the type of printer used, the asterisks (*) may or may not be printed on either side of the label number.   |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example: Sample Unit Dose Bar Code Label

| Drug: BACLOFEN 10MG TABS (Qty: 1)   | Drug: BACLOFEN 10MG TABS (Qty: 1)                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Dosage: 25MG                        | Patient: BCMAPATIENT,ONE  Ward: GEN MED  : 123141  Exp: 4/5/2006  Mfg: UPJOHN  Filled/Checked By: XX/XX |
| <!-- image -->  *500-2564*          |                                                                                                         |

Example: Sample Ward Stock Bar Code Label

| Drug: BACLOFEN 10MG TABS (Qty: 1)   | Drug: BACLOFEN 10MG TABS (Qty: 1)                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Dosage: 25MG                        | Patient:  Ward:  : 123141  Exp: 4/5/2006  Mfg: UPJOHN  Filled/Checked By:\_\_\_\_\_\_\_/\_\_\_\_\_\_\_ |
| <!-- image -->  *500-2564*          |                                                                                                        |

Example: Sample Unit Dose Bar Code Label with HAZ Information

| Drug:   FLUOROURACIL 500MG/10ML (Qty: 1)  &lt;&lt;HAZ Handle&gt;&gt; &lt;&lt;HAZ Dispose&gt;&gt;   |                                                                                                          |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Dosage: 500MG                                                                                      | BCMAPATIENT,ONE  Ward: GEN MED  Lot#: 123987   Exp: MAY 4,2022  Mfg: PHARMCO  Filled/Checked By: ABC/ZYX |
| <!-- image -->  *500-2564*                                                                         |                                                                                                          |

## Appendix C: Interfacing with the Bar Code Label Printer

| JCAHO Standard for Medication Labeling*   | The following is an excerpt from  *The Comprehensive Accreditation Manual for Hospitals: The Official Handbook (CAMH)*  that lists the JCAHO standard for medication labeling. All printed medication labels must adhere to this standard.   |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Standard MM.4.30**                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Medications are labeled.                                                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| **Rationale for MM.4.30**                                                                                                                                                                                                     |
| A standardized method for labeling all medications will minimize errors.                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| **Elements of Performance for MM.4.30**                                                                                                                                                                                       |
| Medications are labeled in a standardized manner according to law or regulation and standards of practice.                                                                                                                    |
| Any time one or more medications or solutions are prepared but are not administered immediately, the medication container* must be labeled.                                                                                   |
| At a minimum, all medications prepared in the hospital are labeled with the following:                                                                                                                                        |
| Drug name, strength, amount (if not apparent from the container)                                                                                                                                                              |
| Expiration date† when not used within 24 hours                                                                                                                                                                                |
| Expiration time when expiration occurs in less than 24 hours                                                                                                                                                                  |
| The date prepared and the diluent for all compounded IV admixtures and parenteral nutrition solutions                                                                                                                         |
| When preparing individualized medications for multiple specific patients, or when the person preparing the individualized medications is not the person administering the  medication, the label also includes the following: |
| Patient name                                                                                                                                                                                                                  |
| Patient location                                                                                                                                                                                                              |
| Directions for use and any applicable cautionary statements either on the label or attached as an accessory label (for example, “requires refrigeration,” “for IM use only”)                                                  |

* Source : Joint Commission on Accreditation of Hospital Organizations (JCAHO). (January, 2006). *The Comprehensive Accreditation Manual for Hospitals: The Official Handbook (CAMH)* (pp. MM-11-MM-12). : Joint Commission Resources, Inc.  Web link: [http://vaww.oqp.med.va.gov/oqp\_services/accreditation/uploads/JCAHO2006/2006%20CAMH%20Core.pdf](http://vaww.oqp.med.va.gov/oqp_services/accreditation/uploads/JCAHO2006/2006%20CAMH%20Core.pdf)