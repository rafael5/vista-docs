---
app_name: Radiology/Nuclear Medicine (RA)
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
package_id: RA
patch: null
patch_gap: null
section: ''
source_file: ra5_0tm.docx
status: draft
title: Department of Veterans Affairs
---

<!-- image -->

**RADIOLOGY/NUCLEAR MEDICINE**

**TECHNICAL MANUAL**

Version 5.0

January 2026

# Department of Veterans Affairs

Health System Design and Development

Provider Systems

This Page is intentionally left blank

**Revision History**

| **Date**       | **Page**                                  | **Change**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| January 2026   | 64, 40-41                                 | RA*5.0*226  Add new option ‘Activate/Inactivate Standard Procedures’ [RA PROCEDURE ACTIVATE]  Updated routine list: RACTCERN, RAIPS226                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| May 2025       | 38, 43                                    | RA*5.0*223  Add new file RADIOLOGY PROCEDURE MAP TO CC CONSULT (#71.1235)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| January 2025   | 15,16,73                                  | RA*5.0*220  Add new menu option ‘Reprocess locked study accession error’ [RA REPROC].  Add new option ‘Site Accession Number Set-up’ [RA SITEACCNUM] to the ‘IRM Menu’ [RA SITEMANGER]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| May 2023       | 7, 13, 32, 46, 51, 59, 61, 64, 67, 81, 84 | Status of options impacted by patch RA*5.0*198.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| January 2022   | 5-6                                       | RA*5.0*185  ‘Device Specifications for Imaging Locations’ [RA DEVICE] menu includes new “Alternate Request Printer” and associated parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| September 2021 | 57                                        | RA*5.0*184  New option ‘Inactivate a Location’ [RA SYSINACT] added to the ‘System Definition’ [RA SYSDEF] parent menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| June 2021      | 31,54,55                                  | RA*5*179  New option ‘Log of Discontinued Requests’ [RA ORDER DISCONTINUE] added to the ‘Menu of Request Log Options’ [RA ORDERLOG MENU]  New sub-menu ‘Rad/Nuc Med Report Management’ [RA REPORT MANAGEMENT] added to the ‘Supervisor Menu’ [RA SUPERVISOR]. Options to unverify/delete/restore a deleted report menus moved under this sub-menu.  New RA RPTMGR security key for the report manangement options. Previously locked with RA MGR and RA UNVERIFY.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| March 2021     | 43, 48, 49, 54, 74, 76, 85                | RA*5.0*175: Clarification of the ‘Discontinued’ and ‘Cancelled’ REQUEST STATUS values. Update the menu structure of the [RA ORDER] menu and ITS new [RA ORDERLOG MENU] sub-menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| March 2021     | 55                                        | MAG*3.0*231  New ‘Radiology Study Tracker Menu’ added to the Supervisor Menu [RA SUPERVISOR].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Feb 2021       | 44                                        | RA*5.0*170  Added new filed COMMUNITY CARE JUSTIFICATIONS (#75.3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Feb 2021       | 58                                        | RA*5.0*178  Added new ‘Outside Location Order Suppression’ [RA SYSUPLOC] to the RA SYSDEF menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| July 2019      | 31, 85                                    | RA*5.0*157  Added the ‘RA SWITCHLOC’ security key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| June 2019      | 34, 42, 58                                | RA*5.0*158  VA FileMan file security update to RAD/NUC MED REASON file (#75.2)  Remove ‘Reason Edit’ [RA REASON EDIT] menu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| March 2019     | 36, 55, 59                                | RA*5*148  Routine List updated  New Radiology menu item ‘Refer Selected Requests to COMMUNITY CARE Provider [RA ORDERREF]’ added to Radiology/Nuclear Med Order Entry Menu [RA ORDER]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| March 2019     | 52-54,62, 71                              | RA*5.0*153: Remove references to scaled wRVUs.  Change the upper file number values for Rad Nuc Med files from 79.2 to 79.7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| August 2018    | 31, 45, 58, 85                            | RA*5.0*124: The reference to the RA CANCEL input template has been removed.  Added the ‘RA UNVERIFY’ security key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| June 2017      | 5, 56                                     | RA*5*137  ‘Device Specifications for Imaging Locations’ [RA DEVICE] menu includes new “Registered Request Printer” parameter.  Removed RA EXAMSTATUS MASS OVERRIDE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| March 2017     | 31, 36, 39, 41, 46, 47, 55, 91            | RA*5*127  Added RADNTRT to the Mail Group section.  Added routines to the Routine List section for the NDS Radiology Reports patch.  Amended file #71 to state there are four new fields incorporated within the file for interoperability purposes  Added new files #71.11, #71.98, and #71.99 and their related information  Added RA PRO MAP template to the templates section.  Ammended the RA PROCEDURE EDIT template to state that there is a section to assocaite a “DETAILED” Type procedure with a cpt code to the MRPF.  Ammended the RA SUPERVISOR MENU option to include the new options: RALOINC ENTER, RA MAP TO MRPF, RA MAP ONE, and RA SEEDING DONE.  Added RA*5.0*127 patch description                                                                                                                                                                                                                                          |
| December 2016  | 58,61                                     | RA*5*133  ‘Radiology/Nuclear Med Order Entry Menu’ [RA ORDER] includes new ‘Update a Hold Request’ [RA ORDERREASON UPDATE]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| November 2013  | 19, 34, 36-37, 52, 53, 87                 | RA*5*113  Definition of ^RAD global Radiation Absorbed Dose file (#70.3)  VA FileMan File Protection on Radiation Absorbed Dose file (#70.3)  Routine List included; shows core Radiology routines (compiled routines may differ from site to site)  Special Reports’ [RA SPECRPTS] Menu update: includes new ‘Radiation Dose Summary Report’ [RA RAD DOSE SUMMARY] menu item  ‘Patient Profile Menu’ [RA PROFILES] includes new Exam Profile with Radiation Dosage Data [RA PROFRAD DOSE] menu item.  Software / Documentation Notes and Patch descriptions                                                                                                                                                                                                                                                                                                                                                                                        |
| September 2013 | 43, 71                                    | - RA*5*97: Added BI-RADS and AAA codes to DIAGNOSTIC CODES file (#78.3) - RA*5*97: Added definition for Abdominal Aortic Aneurysm (AAA)  RA*5*97: Added definition for Breast Imaging Reporting and Data System (BI-RADS  ™  )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| August 2011    | 13, 34, 51, 65, Glossary                  | Patch RA*5.0*47:  - Added a new option to turn on the site-specific accession number: Site Accession Number Set-up. - Replaced the example with an updated version. - Updated the names of the Rad/Nuc Med HL7 manuals. - Added a new option to the IRM Menu [RA SITEMANAGER]:  Site Accession Number Set-up. - Added four new protocols: RA CANCEL 2.4 RA EXAMINED 2.4 RA REG 2.4 RA RPT 2.4 - Added Site Specific Accession Number (SSAN) to the Glossary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| February 2010  | 15                                        | RA*5*99:  - Updated the section heading to reflect change in reporting periods; "Schedule Perf. Indic. Summary for Fifteenth of Month Following the Quarter End." - Updated “RA PERFORMIN SCHEDULE” to run quarterly vs. monthly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| May 2009       | 1, 32, 32, 69, 71                         | - RA*5*78: Added a phrase to the description of the interface in the Introduction - RA*5*78: Added the new mail group name and description, RAD HL7 MESSAGE - RA*5*78 :Added information about querying the VistA Radiology application for results - RA*5*78: Updated the screen capture of the DBIAs section - RA*5*78: Changed UCI to development environment in the note regarding XINDEX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| July 2008      | 52, 71, 84                                | - RA*5*56: Added new option, Outside Report Entry/Edit. - RA*5*56: Added a new option, Restore a Deleted Report. - RA*5*56: Added a definition for the ‘Deleted’ status. - RA*5*56: Added a definition for the ‘Electronically Filed’ status. - RA*5*56: Added two new valid report statuses to the definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| June 2008      | 63                                        | RA*5*84: Added four new protocols                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| September 2007 | 56                                        | RA*5*80: Added new option to RA HL7 MENU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| June 2007      | 35, 36, 46, 56                            | - Updated sections to reflect current functionality. (These updates are not associated with any particular patch.) - RA*5*81: Added file #79.7 to VA FileMan File Protection list. - RA*5*81: Added file #79.7 to the detailed list of files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| February 2007  | 19, Glossary                              | - RA*5*79: Added file to RA Global - RA*5*79: Added new file - #73.2 Radiology CPT By Procedure Type. - RA*5*79: Updated glossary entry for Procedure Type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| July 2006      | 51, 53, 54, Glossary                      | - RA*5*64: Added scaling factor description to File #79.2. - RA*5*64: Added five reports to [RA WKL] menu: Physician CPT Report by I-Type, and four Physician wRVU reports. - RA*5*64: Added two Procedure wRVU reports to [RA SPECRPTS] menu. - RA*5*64: Added glossary entries for RVU, wRVU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| April 2006     | 54                                        | RA*5*67: Renamed Performance Indicator menu to Timeliness Reports. Added Outpatient Procedure Wait Time menu and report to Timeliness Reports menu. Renamed Performance Indicator reports to Verification Timeliness reports (menu options unchanged).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| March 2006     | 20, Glossary                              | - RA*5*57: Added Key Variable RACCOUNT. - RA*5*57: Added glossary entries for PFSS, PFSS Account Reference, and PFSS Department Code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| August 2005    | 6                                         | - Miscellaneous formatting corrections throughout - RA*5*41: Text was deleted - On the Rad/Nuc Med patient file (#70), the activity log, clinical history, and exam status times are deleted. The entire request entry in the Rad/Nuc Med Orders file (#75.1) is deleted. - RA*5*41: Text deletion. – Item 5 - Order data (ORDER DATA CUT-OFF). Purges the record (entire procedure request) from File (#75.1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| August 2005    | 8, 9, 12, 10                              | - RA*5*41: The following text was deleted - The default number of days for the Order Data Cut-Off is 90 and, if changed, must be a whole number between 30 and 99999. The orders which will be purged include those whose last activity date is greater than the number of default days and whose order status is Discontinued, Hold, Complete, or Pending. Order purges can also be initiated by OE/RR. - RA*5*41: Additional text description - This number should 0, as the option no longer allows purging of orders. - RA*5*41: Text change and deletion - ^RAO - …but not data from ^RAO (order data) - …order data and changed 5 items to 4. - RA*5*41: Deletion of prompt and response " ORDER DATA CUT-OFF: 90// 99999". - RA*5*41: Deleted O - Orders only and A - All three. - RA*5*41: Purging orders/requests was deleted.                                                                                                             |
| May 2005       | 31, 34, 57, 57, 68, 70, 71, Glossary      | - RA*5.0*45: Reference to template compilation option has been updated to state that different sites may have different templates compiled. - RA*5.0*45: Reference to non-existent HL7 specific appendices in the Technical Manual removed. HL7 specific documents have been created to: 1) describe interfaces with COTS applications 2) general HL7 message definition - RA*5.0*45: The Procedure File Listings menu has two new items; ‘RA CMAUDIT HISTORY’ &amp; RA PROCMEDIA - RA*5*45: Included the CPT MODIFIER (#81.3) file in the External Relations section. - RA*5.0*45 changed the screen capture; the Version label erroneously displayed the version of the application as being 4.5, not version 5. - RA*5.0*45: Removed all references to %INDEX, issues with using XINDEX regarding RAUTL8 have been addressed by the Kernel development team. - RA*5.0*45: Updated definition of AMIS code. Removed references to contrast media. |
| January 2004   | 30                                        | RA*5*44: Added Schedule Perf. Indic. Summary for the fifteenth of the month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| May 2003       | 8, 10, 54                                 | - RA*5*34: Changed 9999 to 99999 - RA*5*34: Replaced example - RA*5*34: Added data recovery text - RA*5*37: Added RAD PERFORMANCE INDICATOR mail group. - RA*5*37: Performance Indicator Menu Options added                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| December 2002  | 59                                        | RA*5*35: Added new option to the User Utility Menu – Set preference for Long Display of Procedures [RA SET PREFERENCE LONG DISPLAY]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| September 2002 | 12, 49, 57, 58                            | - RA*5*31: Added new option - Credit Completed Exams for an Imaging Location - RA*5*31: Added new option to Exported Menus - RA*5*31: Added new option to [RA OVERALL] - RA*5*31: Added new option to [RA OVERALL]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| July 2002      | 52, 51                                    | - RA*5*25: Added Radiology HL7 Menu - RA*5*25: A number of new protocols added **Table of Contents** Department of Veterans Affairs	1 1.	Introduction	1 2.	Implementation	2 Implementation of a Virgin Installation	2 Implementation of an Installation over V. 4.5	3 Informational Messages	3 3.	Maintenance	4 Imaging Type Mismatch Report	4 IRM Menu	4 Device Specifications for Imaging Locations	4 Distribution Queue Purge	6 Failsoft Parameters	7 Imaging Type Activity Log	7 Purge Data Function	7 Rebuild Distribution Queues	12 Report File x-ref Clean-up Utility 	13 Site Accession Number Set-up 	14 Credit completed exams for an Imaging Location 	15 Enable HL7 reprocessing for locked studies	15 Resource Device Specifications for Division	16 Schedule Perf. Indic. Summary for Fifteenth of Month Following the Quarter End 	16 Template Compilation	17 4.	Globals	20 5.	Key Variables	23 Function	32 Bulletins	32 Mail Groups	33 6.	Security	34 Keys	34 RA ALLOC	34 RA MGR	34 RA VERIFY	34 RA RPTMGR	34 RA SWITCHLOC	34 Sign-on Security	35 Electronic Signature	35 VistA Options	35 COTS HL7 Interfaces	35 VA FileMan File Protection	38 Legal Requirements	39 7.	Routine List	40 8.	File List	41 Templates	49 Input Templates	49 Sort Templates	51 Print Templates	52 List Templates	53 9.	Exported Options	55 Exported Menus	55 IRM Menu [RA SITEMANAGER]	55 Rad/Nuc Med Total System Menu [RA OVERALL]	55 Rad/Nuc Med Clerk Menu [RA CLERKMENU]	64 Rad/Nuc Med Ward Clerk Menu [RA WARD]	65 Rad/Nuc Med File Room Clerk Menu [RA FILERM]	66 Interpreting Physician Menu [RA RADIOLOGIST]	66 Reports Menu [RA REPORTS]	67 Rad/Nuc Med Secretary Menu [RA SECRETARY]	68 Rad/Nuc Med Technologist Menu [RA TECHMENU]	69 Rad/Nuc Med Transcriptionist Menu [RA TRANSCRIPTIONIST]	70 Single Options	70 Menu/Option Assignment	70 Protocols	71 FileMan Options	72 10.	Archiving and Purging	73 11.	Callable Routines	73 12.	External Relations	73 DBIAs	74 13.	Internal Relations	76 14.	Package-wide Variables	76 15.	How to Generate On-line Documentation	77 Build File Print	77 Question Marks	77 XINDEX	77 Inquire to File Entries	78 Print Options File	78 List File Attributes	78 16.	Glossary	80                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| April 2002     | 7, TOC                                    | - RA*5*27: Added the word Additional to the Clinical                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |


## 2 Introduction

The Radiology/Nuclear Medicine package is a comprehensive software package designed to assist with the functions related to processing patients for imaging examinations.

The package automates a range of Radiology/Nuclear Medicine functions, including order entry of requests for exams by clinical staff, registration of patients for exams, processing of exams, recording reports/results, verification of reports on-line, displaying/printing results for clinical staff, automatic tracking of requests/exams/reports, and generation of management statistics/reports, both recurring and ad hoc.

The package automates many tedious tasks providing faster, more efficient and accurate data entry and more timely results reporting.

The package interfaces with the Record Tracking package for the purpose of tracking Radiology/Nuclear Medicine records and creating pull lists for those records needed for scheduled clinic appointments.

- It interfaces with and through the Health Level Seven (HL7) package for the exchange of exam and report information with other VistA applications as well as Commercial Off The Shelf (COTS) applications.
- It interfaces with the Health Summary package to allow users to see patient histories and test results which may influence the nature of the examination.
- It interfaces with the Computerized Patient Record System (CPRS) package to allow requesting of exams and viewing of reports.
- It interfaces with the Adverse Reaction Tracking (ART) package for the exchange of data concerning a patient's allergies.
- It interfaces with Patient Care Encounter (PCE) for crediting outpatient imaging procedures.
- It also interfaces with the AMIE package to display exam results.


## 4 Implementation

### Implementation of a Virgin Installation

Enter at least one division into the Rad/Nuc Med Division file #79 to activate the system. The division can be further defined by the ADPAC.

Give the ADPAC access to at least one Imaging Location (field #74) in the New Person file (#200). Without this, no one will be able to sign onto the system. Once the ADPAC has access, s/he must give each package user (technologist, interpreting resident physician, interpreting staff physician, or clerk) location access so they can sign on. The ADPAC can give users access with the Classification Enter/Edit [RA PNLCLASS] option. Without an assigned imaging location, a user simply cannot access the package.

Along with the ADPAC, determine the devices needed for each Imaging Location that will be defined. Use the option Device Specifications for Imaging Locations [RA DEVICE] in the IRM Menu [RA SITEMANAGER] to assign them.

Associate an existing or new mail group with each of the exported bulletins (see page 32) so users can receive these Radiology/Nuclear Medicine messages. The bulletins are generated when an important action has taken place, such as the deletion of a report. Consult with the package ADPAC to determine how many mail groups to create, what mail group(s) to associate with each bulletin and who should be the mail group coordinator. It is strongly recommended that a mail group with the ADPAC and possibly an IRM support person as recipients be established and associated with the RAD/NUC MED CREDIT FAILURE bulletin. This is the only way users can be notified of credit failure due to lack of data or wrong data in Radiology/Nuclear Medicine.

**Verifying reports** VistA reports: Give the RA VERIFY key to staff that will be verifying reports and make sure they have an electronic signature.

**COTS Voice Recognition Systems** : In addition to the above, assign verifying privileges to staff that will be verifying reports on a COTS Voice Recognition system. Also, assign an ID to each physician that matches his/her IEN in the New Person file #200.

**The IRM Menu** [RA SITEMANAGER] and the standalone option Imaging Type Mismatch Report [RA EXAM/STATUS ITYPE] covered in this chapter will help with the continued maintenance of the software. Further implementation and maintenance can be done by the ADPAC and is described in full in the *Radiology/Nuclear Medicine ADPAC Guide* .

### Implementation of an Installation over V. 4.5

1. Verifying reports **VistA reports** : Give the RA VERIFY key to staff that will be verifying reports and make sure they have an electronic signature.
COTS Voice Recognition Systems: In addition to the above, assign verifying privileges to staff that will be verifying reports on a COTS Voice Recognition system. Also, assign an ID to each physician that matches his/her IEN in the New Person file #200.
2. The burden of Implementation falls mainly on the ADPAC and is fully discussed in the *ADPAC Guide* with a checklist of steps to use in the implementation process.

### Informational Messages

There are two main messages that users may receive that concern IRM particularly during implementation after a virgin installation:

1. Radiology/Nuclear Medicine Division definition error. Call your site manager.
When a user calls about this message, it means there is insufficient information in the imaging location that was selected by the user. Make sure the ADPAC has assigned that location to a division in the Division Parameter Set-up option Rad/Nuc Med Division file (#79), field #50.

No default "ABC" printer has been assigned. Contact IRM.
This message appears when the ADPAC is editing an imaging location in the Location Parameter Set-up option and as yet, a printer has not been assigned for that activity (jacket labels, flash cards, or exam labels). Use the option Device Specifications for Imaging Locations [RA DEVICE] to assign them.


## 6 Maintenance

Information throughout this manual is meant to help IRM in the maintenance of the software. The discussion that follows here covers the options available to assist IRM in that maintenance.

### Imaging Type Mismatch Report

[RA EXAM/STATUS ITYPE]

This option is not assigned to any menu. It generates a report listing each case where the imaging type of the visit does not match the imaging type of the current exam status. These cases should be edited to Complete as soon as possible to correct the exam status. This mismatch condition may have happened around the time a previous version was installed, but new mismatches should not occur.

The report requires 132 column output and displays the patient name, SSN, exam date/time, case number, imaging type of the visit, exam status and imaging type of the exam status for each discrepancy. Radiology/Nuclear Medicine personnel can use the case edit options to move these exams to a Complete status which automatically resolves the mismatch.

### IRM Menu

[RA SITEMANAGER]

#### Device Specifications for Imaging Locations

[RA DEVICE]

This function allows you to assign device names for printers to which the software will direct various outputs. Each imaging location can be assigned its own set of printers.

When a user signs on the system and tries to access the module, the first action by the module will be to determine which division and location with which the user is associated. During the entire session, the system automatically uses the parameters that the coordinator has specified for that division and location. For example, the user need never be asked how many flash cards to print or what flash card format if the parameters contain that information.

Once parameters are entered for default printers (flash card, jacket label, radio-pharmaceutical dose ticket, report, request and request cancellation) and the printer names have been assigned to the location, output is automatically routed to these devices.

If a default printer is not entered, the user will be prompted to select a printer at the time they initially access the Radiology/Nuclear Medicine package. If a default printer is not selected at the time of initial access to the package, the user will be prompted for a printer each time they elect to print a flash card, jacket label, request, or report.

**Note** : When an exam is requested via the Request an Exam option, the prompt, "Submit Request To:" is screened. Therefore, if a Request Printer is malfunctioning, it will have to be changed for that location until the printer is fixed. This is an option that you may wish to assign to the package ADPAC.

One of the new fields, Dosage Ticket Printer, only appears if the Imaging Location you select is an Imaging Type of Nuclear Medicine or Cardiology Studies.

The option requests the Imaging Location name, and then default printer names for:

- Flash Cards
- Jacket Labels
- Requests
- Reports
- Dosage Tickets
- Cancelled Requests
- Registered Request Printer
- Alternate Request Printer

The Alternate Request Printer has additional parameters associated with it. These parameters are as follows:

ALTERNATE PRINTER USAGE – This parameter designates how the alternate request printer will be used. It is a set of codes: 1:After Hours Printer or 2:Alternate Printer

AFTER HOURS BEGIN TIME - This is the time of day that radiology requests will be routed to the alternate request printer you selected (i.e., 7:00PM)

AFTER HOURS END TIME - This is the time of day that radiology requests will revert to printing to your normal default request printer.(i.e., 7:00AM)

AFTER HOURS WEEKEND - This parameter allows the user to define weekends (Saturday/Sunday) as after hours. If set to YES, all requests will be routed to the alternate printer for the duration of the weekend.

AFTER HOURS HOLIDAY - This parameter allows the user to define holidays as after hours. If set to YES, all requests will be routed to the alternate printer on that day. ***Note that this parameter relies on the HOLIDAY file (#40.5) being populated correctly with the Federal holidays.***

ARP CATEGORY OF EXAM - This allows you to send ONLY outpatient or inpatient requests to the alternate printer (all other categories would print to the original request printer), or ALL exam categories (INP/OPT etc) to the after hours printer during the specified time frame.

ALTERNATE PRT REQUESTING LOC – This parameter can be used to identify requesting locations that will cause the request to be routed to the alternate request printer. This parameter **cannot** be used in conjunction with the after hours parameters.

#### Distribution Queue Purge

[RA RPTDISTPURGE]

The Distribution Queue Purge option allows you to purge the distribution files. This can be done to eliminate old reports that have already been printed or reprinted.

The information purged includes the Activity Log in the Reports Distribution Queue file (#74.3) and the reports in the Report Distribution file (#74.4).

You are prompted for a purge date and a device. Any reports printed prior to that specified date are purged from the distribution files.

A mail message will be sent to you with the results of the purge which includes the date/time the purge begins and ends.

Subj: Distribution Queue Purge [#12256] 09 Feb 97 11:34 4 Lines

From: Radiology Package in 'IN' basket.  Page 1 **NEW**

-----------------------------------------------------------------------

Purge distribution files of reports printed before JAN 1,1997

Distribution files purge process begun at FEB 9,1997 11:34

Distribution files purge process completed at FEB 9,1997 11:34

**Note** : Occasionally, a facility has kept the Distribution Queues active, but reports have not been printed for a long time causing a high volume of unprinted reports to sit in the queue. This purge option is not designed to purge unprinted reports. To delete unprinted, historical reports that you do not want to print from the queues, use the Rebuild Distribution Queues [RA RPTDISTREBUILD] option. Rebuilding also supports populating the queues with reports verified on or after a date, you choose.

#### Failsoft Parameters

[RA FAILSOFT]

The Failsoft Parameters option allows you to specify the Operating Conditions parameter. This feature will be obsolete in the future. It previously ignored imaging location devices if in emergency mode, but it no longer completely supports that.

#### Imaging Type Activity Log

[RA IMGLOG]

The Imaging Type Activity Log option enables you to acquire a hardcopy log of certain activities.

The log includes the following information by Imaging Type: the date on which the activity occurred, the type of activity, the user who initiated the activity, the number of exams affected (if any) and the number of reports affected (if any).

The types of activities listed are:

- Changes in imaging type parameters
- Scheduled data purges
- Completion of data purges
- Modification of on-line data criteria (changes made through the Purge Data Function option)

#### Purge Data Function

[RA PURGE]

RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] &amp; ‘Indicate No Purging of an Exam/report’ [RA PURGE] options. The information for the RA PURGE option has been retained for historical reference.

The Purge Data Function option enables you to purge specific data from the system without affecting the integrity of the patient records. The data purge deletes the report text, clinical history, and activity log entries from the Rad/Nuc Med Report file #74. However, if the report was amended, nothing is deleted.

You must enter cut off dates (or accept the default) for the following types of data which may be purged using this option:

1. Activity logs (ACTIVITY LOG CUT-OFF)
Purges the ACTIVITY LOG subfile from File #74 
and Purges the ACTIVITY LOG subfile from File #70
2. Reports (REPORT CUT-OFF)
Purges the REPORT TEXT (not the impressions) subfile from File # 74
3. Clinical histories (CLINICAL HISTORY CUT-OFF)
Purges the ADDITIONAL CLINICAL HISTORY  subfile from File #74
and
Purges the CLINICAL HISTORY FOR EXAM subfile from File #70
4. Status tracking times (TRACKING TIME CUT-OFF)
Purges the EXAM STATUS TIMES subfile from File #70

At each prompt concerning one of the above data types, you will be setting the imaging type parameter for the number of days to keep the various activity logs on-line. The number of days for each should be determined by the coordinator and the IRM site manager.

The number of days must be a whole number between 90 and 99999  for Activity Logs, Report, Clinical History, and Tracking Time. The report impressions will remain on-line even after purging.

This operation should be run during off-hours. A system backup should be completed prior to execution of the purge routine.

Output

The output will include the date/time the purge starts and finishes, and all purge statistics compiled for records processed, reports processed and requests processed. Entries are made to the imaging type activity log showing any changes to on-line criteria, purge routine scheduling, and a record of completion.

The following describes how to interpret the summary counts in the output.

Table 1 - Summary Counts

| **Count**                     | **Description**                                                                                |
|-------------------------------|------------------------------------------------------------------------------------------------|
| PURGE COUNTS                  | COUNT EVEN IF ONLY 1 OF 3 IS WITHIN CUT-OFF DAYS                                               |
| No. of exam records processed | ACTIVITY LOG CUT-OFF and/or CLINICAL HISTORY CUT-OFF and/or TRACKING TIME CUT-OFF              |
| No. of reports processed      | ACTIVITY LOG CUT-OFF and/or CLINICAL HISTORY CUT-OFF and/or REPORT CUT-OFF                     |
|                               | Count only if order was purged within cut-off day  AND other criteria                          |
| No. of requests processed     | ORDER DATA CUT-OFF  This number should be 0, as the option no longer allows purging of orders. |

By purging information that is unnecessary for the maintenance of the system and associated patient records, you will extend your disk space and possibly speed up processing time.

**Note** : Be sure to do a system backup before you choose to purge data.

The following is an example:

Select IRM Menu Option: Purge Data Function

+--------------------------------------------------------+

| This option is used to remove data from one or all of |

| these globals: ^RADPT, ^RARPT      |

|              |

| Make sure IRM keeps the backup that was made prior to |

| running this option, and NOT overwrite that backup for |

| at least 6 months. Data from ^RADPT and ^RARPT can be |

| recovered.            |

|              |

| The cut-off dates for the 4 items (activity log,  |

| report, clinical history, tracking time)    |

| are compared to the exam date of those items. If the |

| exam date for an item is older than the cut-off date |

| for that item, then that item would be purged.   |

+--------------------------------------------------------+

Do you want to edit the Imaging Type purge parameters? Yes// **&lt;RET&gt;**

Select IMAGING TYPE: ULTRASOUND

Please indicate how many days each type of data should remain on-line:

----------------------------------------------------------------------

ACTIVITY LOG CUT-OFF: 90// **?**

Enter a number between 90 and 99999, to indicate the number of

days to keep the various activity logs on-line.

ACTIVITY LOG CUT-OFF: 90// **99999**

REPORT CUT-OFF: 90// **99999**

CLINICAL HISTORY CUT-OFF: 90// **99999**

TRACKING TIME CUT-OFF: 90// **99999**

Select IMAGING TYPE:

Do you wish to schedule the data purge? No// **YES**

Select one of the following:

E   Exams only

R   Reports only

B   Both exams &amp; reports

Enter type of data to purge: Reports only// **Both exams &amp; reports**

IMAGING TYPES

-------------

1) ANGIO/NEURO/INTERVENTIONAL

2) CARDIOLOGY STUDIES (NUC MED)

3) CT SCAN

4) GENERAL RADIOLOGY

5) MAGNETIC RESONANCE IMAGING

6) MAMMOGRAPHY

7) NUCLEAR MEDICINE

8) ULTRASOUND

9) VASCULAR LAB

Select Imaging Type(s) to Purge: (1-9): **8**

Do you wish to re-purge records that have been purged in the past? No// **&lt;RET&gt;**

You have chosen to purge Exam &amp; Report records from ULTRASOUND

Do you wish to proceed with the purge? No// **YES**

DEVICE: HOME// **QUEUE** TO PRINT ON

DEVICE: HOME// printer name

Requested Start Time: NOW// **&lt;RET&gt;**

Request Queued. Task #: 10157

Purge data routine started at MAR 1,1997 01:05.

Purging exams/reports.

Data purge completed at MAR 1,1997 01:18.

The following purge statistics were compiled:

No. of exam records processed  : 863

No. of reports processed   : 620

No. of requests processed   : 796

If purged data needs to be recovered, IRM can start the data recovery by running routine RARECOV from the backup volume, and later the RARESTOR routine from production.

There are no options assigned to this recovery operation.

The instructions for recovering purged data are displayed when routine RARECOV is run.

The following is an example from the backup volume.

**D ^RARECOV**

Instructions for recovering purged exam and/or report data

Step 0.

Find out:

1 - the DATE that the purge was done

2 - how many DAYS back from that date was used as cut-off

i.e., what was entered as "ddd" in "T-ddd" ?

Step 1. From the Backup Volume:

D ^RARECOV

enter cut-off dates that you had used in the purge function

Step 2. From the Backup Volume:

D ^%GTO (or your system's global copy out utility)

enter output file name

enter ^XTMP("RARECOV"

Step 3. From the Production volume that holds ^XTMP:

D ^%GTI (or your system's global restore utility)

enter the file name from step 2

Step 4. From the Production volume:

D ^RARESTOR

routine will automatically read from ^XTMP("RARECOV"

and copy data back into ^RADPT and/or ^RARPT

IMAGING TYPES

-------------

1) ANGIO/NEURO/INTERVENTIONAL

2) CARDIOLOGY STUDIES (NUC MED)

3) CT SCAN

4) GENERAL RADIOLOGY

5) MAGNETIC RESONANCE IMAGING

6) MAMMOGRAPHY

7) NUCLEAR MEDICINE

8) ULTRASOUND

9) VASCULAR LAB

Select Imaging Type(s) to recover purged data: (1-9): **9**

Select one of the following:

E   Exam data

R   Report data

B   Both

Enter type of data to recover: Report data// **EXAM** Exam data

Cut-off Date Selection **** VASCULAR LAB ****

Enter date that the Radiology Purge was done : **3/1/02** (MAR 01, 2002)

Enter number of days subtracted from that date as cut-off : **90**

The default value can be changed as needed.

Cut-off Date for ACTIVITY LOG CUT-OFF : DEC 01, 2001// **&lt;RET&gt;**

Cut-off Date for REPORT CUT-OFF : DEC 01, 2001// **&lt;RET&gt;**

Cut-off Date for CLINICAL HISTORY CUT-OFF : DEC 01, 2001// **&lt;RET&gt;**

Cut-off Date for TRACKING TIME CUT-OFF : DEC 01, 2001// **&lt;RET&gt;**

Do you want to proceed ? NO// &lt;RET&gt;

-- Nothing Done --

#### Rebuild Distribution Queues

[RA RPTDISTREBUILD]

The Rebuild Distribution Queue option allows you to rebuild distribution files with reports verified on or after a selected date.

Rebuilding the distribution queues allows the user to reprint reports that have been printed through the Distribution Queue Menu and then purged through the Distribution Queue Purge option. This might be necessary if the original reports were misplaced, if a printer has jammed, etc.

This option can also be used if a facility which has not been using Distribution Queues wants to clean out the queues completely and rebuild with only the reports verified after a chosen date. In this way, the queues can be cleared without printing any reports.

Depending on the category of the report and the requirements of the distribution queue, there will be an entry made in the Report Distribution file (#74.4) for each report and the corresponding queue. In other words, if a report has a category of Outpatient and both the Clinic Reports Queue and the File Room Queue include outpatient reports, two entries will be made in the Report Distribution file (#74.4).

The output from this option will show the number of reports used to rebuild the distribution files.

This report should be queued to a printer.

#### Report File x-ref Clean-up Utility

[RA XREF CLEANUP]

This option can be used to clean-up left-over "ASTF" and "ARES" x-refs from the RAD/NUC MED REPORTS file (#74). It will list and optionally delete the left-over "ASTF" and "ARES" cross-references.

This option is locked by the RA MGR key.

Here is an example:

RAD/NUC MED UTILITY TO LIST/DELETE LEFT-OVER REPORT X-REFS

Do you want to print a list of left-over x-refs?? YES// **&lt;RET&gt;**

Select Device: HOME// **&lt;RET&gt;** TELNET Right Margin: 80// **&lt;RET&gt;**

LEFT-OVER ^RARPT("ARES") X-REFS

===============================

RESIDENT PHYSICIAN     CASE # OF LEFT-OVER X-REF

------------------     -------------------------

RAPROVIDER, ONE      Unknown report #99999992

LEFT-OVER ^RARPT("ASTF") X-REFS

===============================

STAFF PHYSICIAN      CASE # OF LEFT-OVER X-REF

---------------      -------------------------

RAPROVIDER, TWO     Unknown report #7852353

Do you want to clean up these 2 left-over x-refs?? NO// **YES**

^RARPT("ARES",4570,99999992) deleted

^RARPT("ASTF",6738,7852353) deleted

Press RETURN to continue...

Select IRM Menu Option: Report File x-ref Clean-up Utility

RAD/NUC MED UTILITY TO LIST/DELETE LEFT-OVER REPORT X-REFS

Do you want to print a list of left-over x-refs?? YES// **&lt;RET&gt;**

Select Device: HOME// **&lt;RET&gt;** TELNET Right Margin: 80// **&lt;RET&gt;**

LEFT-OVER ^RARPT("ARES") X-REFS

===============================

RESIDENT PHYSICIAN     CASE # OF LEFT-OVER X-REF

------------------     -------------------------

&lt; There are no left-over "ARES" x-refs found. &gt;

LEFT-OVER ^RARPT("ASTF") X-REFS

===============================

STAFF PHYSICIAN      CASE # OF LEFT-OVER X-REF

---------------      -------------------------

&lt; There are no left-over "ASTF" x-refs found. &gt;

Press RETURN to continue.. **&lt;RET&gt;** .

#### Site Accession Number Set-up

[RA SITEACCNUM]

This option is used to turn on use of the Site Specific Accession Number when registering new cases in the Radiology/Nuc Med package for the facility selected.

The user is asked to select a facility and then is allowed to edit the “USE SITE ACCESSION NUMBER?” division parameter for the selected facility. Until this field is set to ‘YES,’ the system will not use the Site Specific Accession Number during registration of a new case.

Only when all devices are able to handle the Site Specific Accession Number, should this field be set to ‘YES’, at which point the system will begin to use the Site Specific Accession Number.

Here is an example:

Select OPTION NAME: RA SITEMANAGER  IRM Menu

Device Specifications for Imaging Locations

Distribution Queue Purge

Failsoft Parameters

Imaging Type Activity Log

Rebuild Distribution Queues

Report File x-ref Clean-up Utility

Site Accession Number Set-up

Credit completed exams for an Imaging Location

Resource Device Specifications for Division

Schedule Perf. Indic. Summary for 15th of month

Template Compilation

Select IRM Menu Option: Site Accession Number Set-up

Warning: Turning on the Site Specific Accession Number should only

be done in conjunction with using the RA v2.4 messaging protocols.

NOTE: Changing the Site Specific Accession Number parameter at a

multidivisional site will change the parameter for ALL divisions.

Current value of Site Specific Accession Number parameter: NO

Use Site Specific Accession Number? YES

#### Credit completed exams for an Imaging Location

[RA CREDIT IMAGING LOCATION]

This option is used to assign "REGULAR CREDIT" to completed exams that have all required data, but did not receive credit because their Imaging Location was incorrectly assigned as "NO CREDIT".

Before this option can be used, the incorrectly defined Imaging Location must have its CREDIT METHOD field changed from "NO CREDIT" to "REGULAR CREDIT".

Then this option will change the exams for the specified Imaging Location and date range from "NO CREDIT" to "REGULAR CREDIT", and pass the information to the PCE package for crediting.

This option should *not* be used to credit exams that were completed by overriding the exam status to "COMPLETE", because the overridden exams probably do not have all required data and would be rejected by the PCE package resulting in many credit failure mail messages.

The option will prompt for the Imaging Location, then the starting and ending exam dates. The user should choose no more than a month's worth of data to process each time, because of the background tasks involved in crediting an exam.

Here is an example:

Select an Imaging Location from the IMAGING LOCATIONS (#79.1) file that is active, receives regular credit, and has a valid DSS ID.

Enter the Imaging Location that you wish to credit: RADIOLOGY LAB

Enter the starting date: : (1/1/1911 - 7/19/2002): **2/1/2002** (FEB 01, 2002)

Enter the ending date: : (2/1/2002 - 7/19/2002): **2/28/2002** (FEB 28, 2002)

Requested Start Time: NOW// **&lt;RET&gt;** (JUL 19, 2002@16:40:32)

Request queued: 362160 @ Jul 19, 2002@16:40:32

#### Enable HL7 reprocessing for locked studies

[RASAN ENABLE REPROCESSING]

This option This option enables a sending application for reprocessing of HL7

result messages that were rejected due to a locked study error. Additionally,

it includes a flag that, when set, overrides the radiology NOSEND flag and sends the reprocessed result message back to the sending application.

Select RAD/NUC MED HL7 APPLICATION EXCEPTION HL7 APPLICATION NAME: **RA-PSCRIBE-TCP** ACTIVE

Are you adding 'RA-PSCRIBE-TCP' as

a new RAD/NUC MED HL7 APPLICATION EXCEPTION (the 3RD)? No// **y** (Yes)

ENABLE LOCK STUDY REPROCESSING: **Y** YES

REPROCESS RETURN TO SENDER: **Y** YES

#### Resource Device Specifications for Division

[RA RESOURCE DEVICE]

If your facility wishes to control the rate at which tasked exam status updates are released to be processed, use this option to enter resource device specifications. This is advised if the facility is experiencing drastic system slowdowns due to periodic heavy use of the online report verification and batch verification of reports options, which can queue a large number of tasks at once.

However, if you choose to enter a Resource Device in this field, you should be careful to completely follow all directions in Kernel documentation after a system crash to bring this Resource Device back up.

Failure to follow those directions could result in Rad/Nuc Med tasks being severely delayed and data corruption.

When you select the option, you are asked to enter a Division and the Device.

#### Schedule Perf. Indic. Summary for Fifteenth of Month Following the Quarter End

[RA PERFORMIN SCHEDULE]

Normally, the Taskman Task List should show:

nnnnnn: RA PERFORMIN TASKLM - Run Previous Quarter's Summary Report. No device.

sss,ttt. From mm/dd/yyyy at hh:mm, By anananan. Scheduled for mm/15/yyyy at hh:mm

This task was submitted to Taskman by patch RA*5*44. The task is supposed to run on the fifteenth of each month following the quarter-end. The quarters are calendar quarters (i.e., Jan, Feb, Mar = 1st quarter).

However, if this task is lost from the Taskman queue, this option should be used to put the option, RA PERFORMIN TASKLM, back on the Taskman queue to run on the fifteenth of the current month following the quarter-end or the next month following the quarter-end, whichever is the closest date in the future.

#### Template Compilation

[RA COMPILE TEMPLATES]

This option recompiles Radiology/Nuclear Medicine input and print templates that are currently compiled. It is advised that all Radiology/Nuclear Medicine users be off the system while the templates are being recompiled.

The user may select compiled templates from any or all of the Radiology/Nuclear Medicine package files that have compiled templates. Also, the user will select the maximum size of the compiled routines.

Here is an example ( **Note:** sites may have compiled templates other than those listed in this example):

Template Compilation

This option will compile all Radiology/Nuclear Medicine input

and print templates (within the defined file number range) which

are currently compiled on your system. Since these templates

are critical to the operation of the software, it is strongly

advised that all Radiology/Nuclear Medicine users be off the

system. It is also strongly advised that the compilation of

templates be done when system activity is at a minimum.

Is it ok to continue? No// **YES**

Maximum routine size on this computer in bytes. (2400-5000) : 5000// **&lt;RET&gt;**

Select Rad/Nuc Med Input Template: **??**

Select a INPUT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g. -NAME.

To get all NAMES type ALL.

Use an asterisk (*) to do a wildcard selection, e.g.,

enter NAME* to select all entries that begin

with the text 'NAME".

Choose from:

RA ORDER EXAM File #: 75.1

RA QUICK EXAM ORDER File #: 75.1

RA REGISTER File #: 70

RA REPORT EDIT File #: 74

RA VERIFY REPORT ONLY File #: 74

Select Rad/Nuc Med Input Template: **ALL**

Another one (Select/De-Select): **-RA REPORT EDIT** File #: 74

Another one (Select/De-Select): **??**

Select a INPUT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g., -NAME.

To get all NAMES type ALL.

Use an asterisk (*) to do a wildcard selection, e.g.,

enter NAME* to select all entries that begin

with the text 'NAME'. Wildcard selection is

case sensitive.

You have already selected:

RA ORDER EXAM File #: 75.1

RA QUICK EXAM ORDER File #: 75.1

RA REGISTER File #: 70

RA VERIFY REPORT ONLY File #: 74

Choose from:

RA REPORT EDIT File #: 74

Another one (Select/De-Select): **&lt;RET&gt;**

Select Rad/Nuc Med Print Template: **ALL**

Another one (Select/De-Select): ??

Select a PRINT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g., -NAME.

To get all NAMES type ALL.

Use an asterisk (*) to do a wildcard selection, e.g.,

enter NAME* to select all entries that begin

with the text 'NAME'. Wildcard selection is

case sensitive.

You have already selected:

RA REPORT PRINT STATUS File #: 74

Choose from:

Another one (Select/De-Select): **&lt;RET&gt;**

Are you sure you wish to compile the selected templates? No// **YES**

Input template to be compiled: RA ORDER EXAM

For file #75.1: RAD/NUC MED ORDERS

Routines filed under the following namespace: 'RACTOE'.

Compiling RA ORDER EXAM Input Template of File 75.1...

'RACTOE' ROUTINE FILED.....

'RACTOE1' ROUTINE FILED......

'RACTOE4' ROUTINE FILED......

'RACTOE5' ROUTINE FILED.....

'RACTOE6' ROUTINE FILED.......

'RACTOE8' ROUTINE FILED..

'RACTOE2' ROUTINE FILED..

'RACTOE3' ROUTINE FILED...

'RACTOE7' ROUTINE FILED.

Done!

Input template to be compiled: RA QUICK EXAM ORDER

For file #75.1: RAD/NUC MED ORDERS

Routines filed under the following namespace: 'RACTQE'.

Compiling RA QUICK EXAM ORDER Input Template of File 75.1....

'RACTQE' ROUTINE FILED......

'RACTQE1' ROUTINE FILED......

'RACTQE3' ROUTINE FILED.......

'RACTQE4' ROUTINE FILED...

'RACTQE6' ROUTINE FILED..

'RACTQE2' ROUTINE FILED...

'RACTQE5' ROUTINE FILED.

Done!

Input template to be compiled: RA REGISTER

For file #70: RAD/NUC MED PATIENT

Routines filed under the following namespace: 'RACTRG'.

Compiling RA REGISTER Input Template of File 70..

'RACTRG' ROUTINE FILED.....

'RACTRG1' ROUTINE FILED....

'RACTRG2' ROUTINE FILED....

'RACTRG3' ROUTINE FILED.......

'RACTRG6' ROUTINE FILED.......

'RACTRG7' ROUTINE FILED......

'RACTRG8' ROUTINE FILED...

'RACTRG11' ROUTINE FILED..

'RACTRG4' ROUTINE FILED..

'RACTRG5' ROUTINE FILED..

'RACTRG9' ROUTINE FILED...

'RACTRG10' ROUTINE FILED...

'RACTRG12' ROUTINE FILED.

Done!

Input template to be compiled: RA VERIFY REPORT ONLY

For file #74: RAD/NUC MED REPORTS

Routines filed under the following namespace: 'RACTVR'.

Compiling RA VERIFY REPORT ONLY Input Template of File 74...

'RACTVR' ROUTINE FILED....

'RACTVR1' ROUTINE FILED.....

'RACTVR2' ROUTINE FILED.....

'RACTVR3' ROUTINE FILED...

'RACTVR4' ROUTINE FILED.

Done!

Print template to be compiled: RA REPORT PRINT STATUS

For file #74: RAD/NUC MED REPORTS

Routines filed under the following namespace: 'RACTRT'.

Compiling RA REPORT PRINT STATUS Print Template of File 74......................

...

'RACTRT' ROUTINE FILED........

Done!


## 8 Globals

Table 2 - Globals

| **NAME**   | **DESCRIPTION**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RA         | Description: This global contains all of the general table type files used by the Radiology/Nuclear Medicine package. These files are pointed to by other files and contain various types of parameters that may be set up at each site to customize the package to meet that site's needs. The files contained in this global are:  Contract/Sharing Agreements (#34)  Route of Administration (#71.6)  Site of Administration (#71.7)  Radiopharmaceutical Source (#71.8)  Radiopharmaceutical Lot (#71.9)  Examination Status (#72)  Radiology CPT By Procedure Type (#73.2)  Standard Reports (#74.1)  Rad/Nuc Med Reason (#75.2)  Complication Types (#78.1)  LBL/HDR/FTR Formats (#78.2)  Diagnostic Codes (#78.3)  Film Sizes (#78.4)  Camera/Equip/Rm (#78.6)  Label Print Fields (#78.7)  Rad/Nuc Med Division (#79)  Imaging Locations (#79.1)  Imaging Type (#79.2)  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory |
| RAD        | Description: This RAD global contains data for the Radiation Absorbed Dose file (#70.3). Journalling is mandatory for this global.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RADPT      | Description: This global contains data for the Rad/Nuc Med Patient file (#70).  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RADPTN     | Description: This global contains patient exam data specific to radiopharmaceuticals for the Nuc Med Exam Data file (#70.2).  The global should be journaled and translated if the operating system supports these functions.  Journaling: 	Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| RAMIS      | Description: This global contains all the files related to Rad/Nuc Med AMIS reporting. The files contained in this global are:  Rad/Nuc Med Procedures (#71)  Major Rad/Nuc Med AMIS Codes (#71.1)  Procedure Modifiers (#71.2)  Rad/Nuc Med Common Procedure (#71.3)  Rad/Nuc Med Procedure Message (#71.4)  Imaging Stop Codes (#71.5)  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RABTCH     | Description: This global contains data for:  Report Batches (#74.2)  Report Distribution Queue (#74.3)  Report Distribution (#74.4)  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RAO        | Description: This global contains the data for Rad/Nuc Med Orders file (#75.1).  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RARPT      | Description: This global contains only data for Rad/Nuc Med Reports file (#74).  The global should be journaled and translated if the operating system supports these functions.  Journaling: Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 9 Key Variables

Table 3 - Key Variables

| **NAME**     | **DESCRIPTION**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RACCESS      | This local array identifies the user's division, imaging type and imaging location access. This variable, along with RAIMGTY, RAMLC, RAMDV, and RAMDIV are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist.  The routine series RAPSET* sets these variables.  For any initial menu for the Radiology/Nuclear Medicine package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.  The array elements that identify the user's division access look like the following: RACCESS(DUZ,"DIV",File #79 IEN,File #79.1 IEN)=File #4 IEN^Division name  The array elements that identify the user's imaging type access look like the following: RACCESS(DUZ,"IMG",File #79.2 IEN,File #79.1 IEN) =null^Imaging Type name  The array elements that identify the user's location access look like the following: RACCESS(DUZ,"LOC",File #79.1 IEN)=File #44 IEN^Hospital Location name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RABED        | Bedsection name. First piece of the zeroth-node for an entry in File #42.4 [Specialty - ^DIC(42.4,]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RABTCH       | Internal entry number to File #74.2 [Report Batches - ^RABTCH( ] that is used during various batch processing functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RACCOUNTPFSS | Account Reference Returned from calling GETACCT^IBBAPI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RACLNC       | Default clinic name used in the initial exam entry process. First piece of the zeroth-node of an entry in File #44 [Hospital Location - ^SC( ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RACN         | Case Number for an exam;  ^RADPT(RADFN,"DT",RADTI,"P",RACNI,0)=RACN^...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RACNI        | Internal entry number for an exam;  ^RADPT(RADFN,"DT",RADTI,"P",RACNI,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RACRT        | This variable is used by the various workload report routines and it contains either a 'y' for 'yes' or an 'n' for 'no' to indicate to the routine whether the exam being processed should be used in the compilation of the report.  The value of RACRT is obtained from the Examination Status file (#72) entry for which the exam being processed points to. In the Examination Status file there is a field for each workload report.  The variable name RACRT comes from 'CRiTeria'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RACS         | RACS="Y" if the crediting has already been given to PCE (Patient Care Encounter) for the exam currently being processed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RACT         | Internal set value for the various activity logs through out the system; for example, in the exam activity log 'E' means 'Exam Entry'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RADATE       | Date of registered exam expanded to a user readable format. (i.e., Jun 17,1984)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RADFN        | Internal entry number to Files #2 and #70 [Patient - ^DPT( ]; [Rad/Nuc Med Patient - ^RADPT( ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RADIV        | Used in the various workload reports, such as RAWKL*, RAPRC*, RALWKL*, RAMIS*, RAFLM*, to indicate the division currently being processed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RADOB        | Patient's date of birth. Third piece of the zeroth node of an entry in File #2 [Patient - ^DPT( ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RADTE        | Exam registration date/time; ^RADPT(RADFN,"DT",RADTI,0)=RADTE^....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RADTI        | Internal entry number of exam registration date/time; also the inverse exam registration date/time; ^RADPT(RADFN,"DT",RADTI,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RADUZ        | Most of the time this is the same as DUZ variable. However, the Radiology/Nuclear Medicine package has the 'feature' to require the user to input their access code during certain processes. RADUZ is equal to that access code's DUZ number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RAEXFM       | Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the 'exam' label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RAEXLBLS     | Number of exam labels to be produced by RAFLH* routines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RAF5         | RAF5=IEN of the ward for the patient if the exam being processed was done while the patient was an Inpatient. RAF5's value is taken from the Ward field of the exam subfile of the Rad/Nuc Med Patient file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RAFIN        | This variable is a flag that is set inside the RA REGISTER input template. If defined after the template is exited, then the system knows that the registration process went to normal completion.  If it is not defined, then the system will automatically delete that current exam because not all questions were answered during the registration process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RAFLH        | This variable can take on two different meanings depending on the routine that is being executed.  When you first log on to the package, the routine RAPSET is executed. This routine computes various parameters for the current logon session. One of the parameters set is the printer where all the flash cards requested by the user are printed. The variable RAFLH is used to store this printer information temporarily until it is set in the third piece of the variable RAMLC. (See RAMLC description for more information.)  The variable RAFLH, throughout the rest of the system, is used to specify which LBL/HDR/FTR Formats file (#78.2) entry to use when printing a flash card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RAFMT        | Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2 ] used to produce one of the following:  flash card (RAFLH)  exam label (RAEXFM)  film jacket label (RAJAC)  report header (RAHDFM)  report footer (RAFTFM)  Before each of the above is produced, their respective routine sets RAFMT to their associated format entry and then PRT^RAFLH is called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RAFTFM       | Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the report footer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RAGE         | Patient's age                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| RAHDFM       | Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the report header                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RAHEAD       | This is the header used when executing the utility routine RAPTLU. This routine displays the current exams on file for a patient. Depending on what the user is currently doing, the header is different.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RAIMGTY      | This variable, along with RACCESS, RAMLC, RAMDV, and RAMDIV are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.  For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.  This variable tracks the Imaging Type for each user based on the location determined at sign-on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RAJAC        | Default jacket label printer information. (Used only in RAPSET*, the parameter setting routine executed upon logging into the program.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RAKEY        | During various processes in the Radiology/Nuclear Medicine system, the user must have a certain key. By setting RAKEY equal to this key and then calling USER^RAUTL the system uses one common set of code to check and verify if the user is qualified to do the current process and asks for an access code if required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RAMDIV       | This variable, along with RACCESS, RAMLC, RAMDV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.  For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.  The variable RAMDIV is the internal entry number to File #79 [Rad/Nuc Med Division - ^RA(79, ]. This is the division that the current location is associated with.  **Note:**  An imaging location can only be associated with one division.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RAMDV        | This variable, along with RACCESS, RAMLC, RAMDIV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.  For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.  The variable RAMDV has 26 pieces. Each piece contains parameter information pertaining to the current 'division' the user is signed on under. All values are '1' for 'yes' or '0' for 'no'.  The following is a description of each piece:  Piece Description [not used] should a flash card be printed for each exam [no longer used] [no longer used] [no longer used] various activity logs are kept during the processing of exams and their reports. This piece indicates whether the user should be asked for their access code during each process or should the system automatically use the user code associated with the initial logon. If 'yes' then system assumes the logon user code (DUZ). should entry of a 'Detailed' or 'Series' procedure be required during initial exam registration. If '0' then user can enter a 'Broad' code. However, before the exam can be placed in a 'Complete' status the procedure must be changed to a 'Detailed' or 'Series' procedure. should a jacket label be printed automatically during each visit should 'camera/equipment/room' be asked during exam editing should the system automatically collect the time when the exam status changes If piece 10 is set to '1', collect status change time data, then should the user be asked the time of the status change or should the system automatically use the current date and time. (If you are batch filing the changes then this parameter would be '1' so that the user can put in the actual change time.) should the transcriptionist be given the opportunity to select a standard report during initial report entry should the transcriptionist be given the opportunity to place reports in a batch during report entry should the transcriptionist be given the opportunity to copy the contents of one report into another [not used] require that an impression be given on a report before the report can be verified and the exam to be considered 'complete' should the transcriptionist be prompted for the date the exam was requested allow interpreting residents to verify other interpreting physicians' reports while using the On-line Verifying of Reports option collect the date and the time of request status changes [not used] indicate that the user should be asked when requesting an exam, which Imaging Location the request should be forwarded to if a user without the RA MGR key can enter a report on a cancelled case [not used] the number of hours in the future (0-168) that a user may register a patient for an exam should the report status appear on unverified reports should an e-mail of the radiology/nuclear medicine report findings be automatically sent to the requesting physician  **Note:**  These parameters are permanently stored in the .1 node of the appropriate entry in File #79 [Rad/Nuc Med Division - ^RA(79,]. The Division Parameter Set-up option under the System Definition Menu is used to set this node. |
| RAMLC        | This variable, along with RACCESS, RAMDIV, RAMDV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.  For any initial menu for the Radiology/Nuclear Medicine package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.  The variable RAMLC has thirteen pieces. Each piece contains parameter information pertaining to the current imaging location the user is signed on under.  The following is a description of each piece: (IEN ==&gt; internal entry number)  Piece Description IEN to File #79.1 [Imaging Location] - used to stuff proper location in registration record how many flash cards to produce per patient visit flash card printer name - used to automatically queue flash cards and exam labels without having to ask the user the device question how many jacket labels to print per visit jacket label printer name - used to automatically queue jacket labels without having to ask the user the device question IEN to File #79.2 [Imaging Type] - used to stuff proper imaging type in registration record (always Rad/Nuc Med's internal number) default flash card format  IEN to File #78.2 [LBL/HDR/FTR Formats] used when queuing a flash card to print; this format is the default flash card for the current location how many exam labels to produce for each exam - when flash cards are queued to print, the system must also be told how many exam labels to print. default exam label format  IEN to File #78.2 [LBL/HDR/FTR Formats]  used when queuing an exam label to print; this format is the default 'exam label' for the current location  Note: Exam labels always print after flash card labels are printed. report printer name - used to automatically queue reports without having to ask the user the device question default jacket label format  IEN to File #78.2 [LBL/HDR/FTR Formats]  used when queuing a jacket label to print; this format is the default jacket label for the current location default report header format  IEN to File #78.2 [LBL/HDR/FTR Formats]  used when queuing a report to print; this format is the default 'header' for the current location default report footer format  IEN to File #78.2 [LBL/HDR/FTR Formats]  used when queuing a report to print; this format is the default footer for the current location  **Note**  : These parameters are permanently stored in the zeroth node of the appropriate entry in File #79.1 [Imaging Location - ^RA(79.1,]  The Location Parameter Set-up option under the System Definition Menu is used to set this no.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| RAMUL        | Internal entry number to File #71.2 [Procedure Modifiers - ^RAMIS(71.2, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RANME        | Patient's name. First piece of the zeroth-node of File #2 [Patient - ^DPT( ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RANUM        | Number of flash cards, exam labels or jacket labels to produce when there is a call to PRT^RAFLH. RANUM is always one for report header and footer production.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RAPHY        | Default provider name used in the initial exam entry process. First piece of the zeroth-node of an entry in File #200 [New Person - ^VA(200, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RAPRC        | Exam Procedure name. First piece of the zeroth-node of an entry in File #71 [Rad/Nuc Med Procedures - ^RAMIS(71, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RAPRI        | Internal entry number to File #71 [Rad/Nuc Med Procedures - ^RAMIS(71, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| RAQUICK      | This variable is used inside the 'Edit Exam' template to properly log an entry into the exam's activity log. The variable is set before going into the template. If set to '1' then the template knows that the editing is occurring through the case number edit routine and if set to '0' then it means the editing is occurring from the edit by patient routine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RARPT        | Internal entry number to File #74 [Rad/Nuc Med Reports - ^RARPT( ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RASER        | Service name. First piece of the zeroth-node of an entry in File #49 [Service/Section - ^DIC(49, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| RASSN        | Patient's SSN. Ninth piece of the zeroth-node of an entry in File #2 (Patient - ^DPT( )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RAST         | This variable can have three meanings depending on where it is used.  In routine RADEM1, the patient demographic display routine, it is equal to the first piece of the zeroth node of an entry in File #72 [Examination Status - ^RA(72, ]  In routine RARTR, the report print routine, it is equal to the set code for the report status.  Otherwise, this variable is normally equal to the internal entry number of an entry in File #72 [Examination Status - ^RA(72, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RASTI        | Internal entry number to File #72 [Examination Status - ^RA(72, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RAWARD       | Ward Name. First piece of the zeroth-node of an entry in File #42 [Ward Location - ^DIC(42, ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Function

Table 4 - Function

| **NAME**   | **DESCRIPTION**                                                                                                                                                                                                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RACAT      | Uses the RAUTL1 routine to compute the location (inpatient, outpatient, contract/sharing agreement, research) and convert time of day to external format. It computes the exam status and updates the status log and OE/RR. It sends alert/notification to OE/RR after the patient is examined. |

### Bulletins

We recommend that when setting up mail groups for each of the following bulletins, you name the mail group something similar to the bulletin.

Table 5 - Bulletins

| **BULLETIN NAME**             | **DESCRIPTION**                                                                                                                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RAD/NUC MED CREDIT FAILURE    | Bulletin will notify users in the selected mailgroup(s) that a crediting failure occurred.                                                                                                 |
| RAD/NUC MED EXAM DELETED      | Bulletin used to notify the radiology supervisor that a radiology exam has been deleted and the computer user who did deletion.                                                            |
| RAD/NUC MED REPORT DELETION   | Bulletin used to notify a mail group that a radiology report has been deleted.                                                                                                             |
| RAD/NUC MED REPORT UNVERIFIED | Bulletin used to notify the radiology supervisor, ADPAC and other selected recipients that a 'verified' radiology report was 'unverified' and the computer user who did the 'unverifying'. |
| RAD/NUC MED REQUEST CANCELLED | Bulletin used to notify the recipient mail group (usually named 'RA REQUEST CANCELLED') that a radiology request has been cancelled.                                                       |
| RAD/NUC MED REQUEST HELD      | Bulletin used to notify the 'RA REQUEST HELD' mail group thatradiology request has been held.                                                                                              |

### Mail Groups

Table 6 - Mail Groups

| MAIL GROUP NAME         | DESCRIPTION                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RADPERFORMANCEINDICATOR | Mail group containing names of local users who are to receive a copy of the Radiology Performance Indicator Summary Report in their VistA mail basket.                                                |
| RADHL7MESSAGE           | This mail group is used to inform radiology users about issues regarding the HL7 interface between the VistA Radiology/Nuclear Medicine application and Commercial Off The Shelf (COTS) applications. |
| RADNTRT                 | This mail group will be used in communication with the NTRT team for new radiology procedures.                                                                                                        |


## 11 Security

### Keys

#### RA ALLOC

Ownership of the RA ALLOC key overrides the location access security given to personnel through Classification Enter/Edit. Owners of the RA ALLOC key have expanded access to Imaging Locations, Imaging Types, and Divisions. In the case of most workload reports, this means they can select from a list of all Divisions and Imaging Types to include on the report. In the case of various edit and ordering functions, it means they can select from all locations within the Imaging Type to which they are currently signed on through the "Select sign-on location prompt.

#### RA MGR

The RA MGR key gives the user access to supervisor-type functions. Those functions are the following:

1. Editing Completed Exams
2. Adding An Exam To A Visit That Is Older Than Yesterday
3. Showing The User All Non-Completed Exams, Not Just Those Associated With The User's Current Division, During Execution Of The "Status Tracking" Function.
4. Updating The Exam Status Of An Exam To Complete
5. Deleting Exams
6. Deleting Reports
7. Entering A Report On A Cancelled Exam If Site Parameters Don't Allow It
8. Deleting Printed Batches By Date
9. Synching Up Exams With CPRS &amp; Radiology Orders

#### RA VERIFY

The RA VERIFY key allows users to verify reports.

#### RA RPTMGR

The RA RPTMGR key gives the user supervisor-type privilege to unverify a report, delete a report, and restore a deleted report.

#### RA SWITCHLOC

The RA SWITCHLOC key gives the user the ability to register an exam under a different modality than the order.

### Sign-on Security

Upon entering a Radiology/Nuclear Medicine menu, the user is prompted to select a "sign-on Imaging Location". The set of locations the user is privileged to access is controlled by the ADPAC or IRM through the Classification Enter/Edit option. Most options are screened by a combination of Imaging Type, Division and Location. Others are screened by ownership. For a thorough discussion of how users are allowed into the Radiology/Nuclear Medicine package options, see the Screening Methods section of the Radiology/Nuclear Medicine ADPAC Guide.

### Electronic Signature

#### VistA Options

When an Interpreting Staff physician wants to verify a report via VistA’s On-line Verifying of Reports or Resident On-Line Pre-Verification option, he must hold the RA VERIFY key and enter an electronic signature code before he can verify the report. This electronic signature code is encrypted.

#### COTS HL7 Interfaces

When an Interpreting Staff physician verifies a report on a COTS Voice Recognition system (such as TalkStation or PowerScribe ) interfaced to VistA *,* the electronic signature processing is not the same as with the VistA options.

The system administrator for the COTS system assigns verifying privileges, similar to the RA VERIFY key, to each physician. An ID that matches the IEN of the physician in the New Person file #200 is also assigned to the physician. When the physician logs on to the COTS application, an ID and secure password are entered to identify the physician.

When a report has been signed and released on the COTS system, it is transmitted over the TCP/IP interface and is received by the Radiology HL7 "bridge" routine RAHLTCPB. Based on the HL7 status of the report, the processing logic will determine if the report has been verified on the COTS system.

This routine will get the verifying physician from the OBR segment's Principal Result Interpreter field (OBR-32) in the HL7 Unsolicited Observation (ORU) report message. If this physician holds the RA VERIFY key, and the physician has a valid electronic signature defined in File #200, the report is filed in the Rad/Nuc Med Report file as VERIFIED with the electronic signature printed block name attached. This process does not currently use any encryption technology, and the processing routine assumes that the verifying physician ID in the OBR segment of the HL7 message belongs to the physician that signed the report on the COTS system.

Even though the VistA routine RAHLTCPB uses certain data items to validate the report sent from the COTS system before it assigns a signature to the report, it can not prevent a renegade software application from sending bogus HL7 messages to the Radiology/Nuclear Medicine system.

While the sending of bogus HL7 messages is not a likely occurrence, it must be recognized as a real and potential breach that could have an impact on Rad/Nuc Med Reports.

Technical Services is considering the use of Public Key Encryption schemes. When an encryption scheme such as this is implemented as a standard, the Radiology developers will issue a patch for COTS interfaces that use the Public Key Encryption schemes for electronic signatures.

Patch RA*5.0*78 - *Query the VistA Radiology/Nuclear Medicine application for results* allows the VistA Radiology/Nuclear Medicine application to accept an inbound query from ScImage and return radiology results back to ScImage. This historical information serves as a reference for the teleradiologists working for the National Teleradiology Project.

**Note** : ScImage is a specific vendor. The query was developed to be vendor independent. There are two different sort criteria for the query. The client (ScImage) can request results based on:

A single accession number (one patient/one result)

A patient record number, within a patient care event date/time window, and maximum number of results to be returned on that patient.

The following components are exported with RA*5.0*78:

File Number			File Name							Record Name

779.2				HLO APPLICATION REGISTRY		RA-NTP-QUERY

RA-NTP-RSP

3.8					MAIL GROUP						RAD HL7 MESSAGES

**Note** : The Electronic Signature for COTS HL7 interfaces can be enabled or disabled in the VistA Radiology/Nuclear Medicine application for each division record in the RAD/NUC MED DIVISION (#79) file. For information on setting up the COTS HL7 interface electronic signature feature, please refer to the following Radiology/Nuclear Medicine v5.0 manuals:

Radiology/Nuclear Medicine 5.0 HL7 Setup/Implementation Manual

Radiology/Nuclear Medicine 5.0 HL7 Interface Specification

### VA FileMan File Protection

Table 7 - VA FileMan File Protection

|   **#** | **Name**                               | **DD**   | **RD**   | **WR**   | **DEL**   | **LAYGO**   |
|---------|----------------------------------------|----------|----------|----------|-----------|-------------|
| 34      | Contract/Sharing Agreements            | @        |          |          |           |             |
| 70      | Rad/Nuc Med Patient                    | @        |          |          |           |             |
| 70.2    | Nuc Med Exam Data                      | @        |          |          |           |             |
| 70.3    | Radiation Absorbed Dose                | @        |          |          |           |             |
| 71      | Rad/Nuc Med Procedures                 | @        |          |          |           |             |
| 71.1    | Major Rad/Nuc Med AMIS Codes           | @        |          |          |           |             |
| 71.1235 | Radiology Procedure Map to CC Consult  | @        | @        | @        | @         | @           |
| 71.2    | Procedure Modifiers                    | @        |          |          |           |             |
| 71.3    | Rad/Nuc Med Common Procedure           | @        |          |          |           |             |
| 71.4    | Rad/Nuc Med Procedure Message          | @        |          |          |           |             |
| 71.5    | Imaging Stop Codes                     | @        |          |          |           |             |
| 71.6    | Route of Administration                | @        |          |          |           |             |
| 71.7    | Site of Administration                 | @        |          |          |           |             |
| 71.8    | Radiopharmaceutical Source             | @        |          |          |           |             |
| 71.9    | Radiopharmaceutical Lot                | @        |          |          |           |             |
| 71.98   | Master Radiology Site File             | @        |          |          |           |             |
| 71.99   | Master Radiology Procedure File (MRPF) | @        |          |          |           |             |
| 72      | Examination Status                     | @        |          |          |           |             |
| 74      | Rad/Nuc Med Reports                    | @        |          |          |           |             |
| 74.1    | Standard Reports                       | @        |          |          |           |             |
| 74.2    | Report Batches                         | @        |          |          |           |             |
| 74.3    | Report Distribution Queue              | @        |          |          |           |             |
| 74.4    | Report Distribution                    | @        |          |          |           |             |
| 75.1    | Rad/Nuc Med Orders                     | @        |          |          |           |             |
| 75.2    | Rad/Nuc Med Reason                     | @        |          | @        | @         | @           |
| 78.1    | Complication Types                     | @        |          |          |           |             |
| 78.2    | LBL/HDR/FTR Formats                    | @        |          |          |           |             |
| 78.3    | Diagnostic Codes                       | @        |          |          |           |             |
| 78.4    | Film Sizes                             | @        |          |          |           |             |
| 78.6    | Camera/Equip/Rm                        | @        |          |          |           |             |
| 78.7    | Label Print Fields                     | @        |          |          |           |             |
| 79      | Rad/Nuc Med Division                   | @        |          |          |           |             |
| 79.1    | Imaging Locations                      | @        |          |          |           |             |
| 79.2    | Imaging Type                           | @        |          |          |           |             |
| 79.3    | HL7 Message Exceptions                 | @        | @        | @        | @         | @           |
| 79.7    | Rad/Nuc Med HL7 Application Exceptions | @        |          |          |           |             |

### Legal Requirements

The Radiology/Nuclear Medicine package uses the Current Procedural Terminology (CPT) coding system which is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA.


## 13 Routine List

The routines exported in the VistA Radiology/Nuclear Medicine application are namespaced ‘RA’. Routine names are alphanumeric characters (uppercase letters only) with a maximum length of eight characters.

Excludes in the list of routines are the following namespaces: ‘RAI’ (Radiology initialization routines), ‘RACT*’ (Radiology routines compiled by VA FileMan) and ‘RAZ*’ (locally developed Radiology routines).

Short Listing of Selected Routine/Include Files

Namespace: DEVRAD

19 May 2025 11:59 AM  Page 1

-- .INT --

RA    RA01   RAAPI   RABAR   RABAR1  RABIRAD  RABTCH  RABTCH1

RABTCH2  RABTCH3  RABUL   RABUL1  RABUL2  RABUL3  RABWIBB  RABWIBB2

RABWORD  RABWORD1 RABWORD2 RABWPCE  RABWRTE  RABWUTL  RACDR   RACDR1

RACMHIS  RACMP   RACMP1  RACMP2  RACMPLE  RACNLU  RACNVRT3 RACOMDEL

RACPT   RACPT1  RACPTCSV RACPTMSC RACTCERN RACTRG  RACTRG1  RACTRG2

RADD1   RADD2   RADD3   RADD4   RADELSVR RADEM   RADEM1  RADEM2

RADLQ1  RADLQ2  RADLQ3  RADLY   RADLY1  RADOSTIK RADPA   RADRPT1

RADRPT1A RADRPT2  RADRPT2A RADTICK  RADUTL  RAEDCN  RAEDCN1  RAEDPT

RAERR   RAERR01  RAERRPT  RAESO   RAESR   RAESR1  RAESR2  RAESR3

RAFLH   RAFLH1  RAFLH2  RAFLM   RAFLM1  RAFLM2  RAFLM3  RAHL7C

RAHL7L  RAHL7O  RAHL7Q  RAHL7Q1  RAHLACK  RAHLBKVQ RAHLBKVR RAHLBMS

RAHLCV  RAHLCV1  RAHLEX  RAHLEX1  RAHLEXF  RAHLNTEG RAHLO   RAHLO1

RAHLO2  RAHLO3  RAHLO4  RAHLOPT  RAHLQ   RAHLQ1  RAHLR   RAHLR1

RAHLR1A  RAHLROUT RAHLRPC  RAHLRPRO RAHLRPT  RAHLRPT1 RAHLRPT2 RAHLRPTT

RAHLRS  RAHLRS1  RAHLRU  RAHLRU1  RAHLTCPB RAHLTCPU RAHLTCPX  RAIPS226

RAJAC RAKRDIT  RALIST  RALIST1  RALOCK  RALOCK01 RALWKL  RALWKL1  RALWKL2

RALWKL3  RALWKL4  RAMAG   RAMAG02  RAMAG02A RAMAG03  RAMAG03A RAMAG03C

RAMAG03D RAMAG04  RAMAG05  RAMAG06  RAMAG06A RAMAG07  RAMAGHL  RAMAGRP1

RAMAGRP2 RAMAGU01 RAMAGU02 RAMAGU03 RAMAGU04 RAMAGU05 RAMAGU06 RAMAGU07

RAMAGU08 RAMAGU09 RAMAGU10 RAMAGU11 RAMAGU12 RAMAGU13 RAMAGU14 RAMAIN

RAMAIN1  RAMAIN2  RAMAIN3  RAMAIN4  RAMAIN5  RAMAINP  RAMAINP1 RAMAINU

RAMAINU1 RAMAORPT RAMGI001 RAMGI002 RAMGI003 RAMGI004 RAMGINI0 RAMGINI1

RAMGINI2 RAMGINI3 RAMGINIT RAMIS   RAMIS1  RAMIS2  RAMRPIN  RANEWPRO

RANMED1  RANMPRT1 RANMPT1  RANMUSE1 RANMUSE2 RANMUSE3 RANMUTL1 RANPRO

RANPRO1  RANPRO4  RANPRO5  RANPROU  RANPROU2 RANTEG  RAO7CH  RAO7CMP

RAO7MFN  RAO7NEW  RAO7OKR  RAO7OKS  RAO7PC1  RAO7PC1A RAO7PC2  RAO7PC3

RAO7PC4  RAO7PURG RAO7RCH  RAO7RO  RAO7RO1  RAO7ROCN RAO7RON  RAO7RON1

RAO7SCH  RAO7UTL  RAO7UTL1 RAO7VLD  RAO7XX  RAONDEM  RAONI001 RAONIT

RAONIT1  RAONIT2  RAONIT3  RAORD   RAORD1  RAORD1A  RAORD2  RAORD3

RAORD4  RAORD5  RAORD6  RAORD61  RAORD7  RAORD7A  RAORD8  RAORDC

RAORDC1  RAORDCP  RAORDP  RAORDQ  RAORDR  RAORDR1  RAORDR2  RAORDS

RAORDU  RAORDU1  RAORR   RAORR1  RAORR2  RAORR3  RAOUT   RAPAST

RAPAT23  RAPAT23A RAPCE   RAPCE1  RAPCE2  RAPERR  RAPERR1  RAPINFO

RAPM   RAPM1   RAPM2   RAPM3   RAPM4   RAPMW   RAPMW1  RAPMW2

RAPMW3  RAPNL   RAPRC   RAPRC1  RAPRE4  RAPRI   RAPRINT  RAPRINT1

RAPROD  RAPROD1  RAPROD2  RAPROQ  RAPROS  RAPSAPI  RAPSAPI2 RAPSAPI3

RAPSET  RAPSET1  RAPTLU  RAPURGE  RAPURGE1 RAPXRM  RARD   RARECOV

RAREG   RAREG1  RAREG2  RAREG3  RAREG4  RARESTOR RARIC   RARIC1

RARPTUT  RART   RART1   RART2   RART3   RARTE   RARTE1  RARTE2

RARTE3  RARTE4  RARTE5  RARTE6  RARTE7  RARTFLDS RARTR   RARTR0

RARTR1  RARTR2  RARTR3  RARTRPV  RARTRPV1 RARTST  RARTST1  RARTST2

RARTST2A RARTST3  RARTUTL  RARTUTL1 RARTUVR  RARTUVR1 RARTUVR2 RARTUVR3

RARTVER  RARTVER1 RARTVER2 RASELCT  RASERV  RASETU  RASIGU  RASITE

RASTAT  RASTED  RASTEXT  RASTEXT1 RASTREQ  RASTREQ1 RASTREQN RASTRPT

RASTRPT1 RASTRPT2 RASYNCH  RASYNCHLU RASYS   RASYS1  RATIMBUL RATRAN

RAUTL   RAUTL0  RAUTL00  RAUTL1  RAUTL10  RAUTL11  RAUTL12  RAUTL13

RAUTL14  RAUTL15  RAUTL16  RAUTL16A RAUTL17  RAUTL18  RAUTL19  RAUTL19A

RAUTL19B RAUTL19C RAUTL2  RAUTL20  RAUTL21  RAUTL22  RAUTL23  RAUTL3

RAUTL4  RAUTL5  RAUTL6  RAUTL7  RAUTL7A  RAUTL8  RAUTL9  RAUTODC

RAWFR1  RAWFR2  RAWFR3  RAWFR4  RAWKL   RAWKL1  RAWKL2  RAWKL3

RAWKLU  RAWKLU1  RAWKLU2  RAWKLU3  RAWORK  RAWRVUP  RAXMLSND RAXREF

RAXSTAT

## 14 File List

Table 8: File Numbers and Description

| FILE NUMBER                                    | GLOBAL FILE DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 34  Contract/Sharing Agreements                | ^DIC(34  This file contains the Contract and Sharing agreements used in Radiology.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 70  Rad/Nuc Med Patient                        | ^RADPT(  This file contains imaging information for patients. It is the focal point of the package.  No data comes with the file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 70.2  Nuc Med Exam Data                        | ^RADPTN(  This file contains information specific to nuclear medicine studies in which radiopharmaceuticals are used.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 70.3  Radiation Absorbed Dose                  | ^RAD(  This file is used to measure the amount of radiation absorbed by a person, known as the “absorbed dose,” this tallies the amount (quantity) of radioactive energy that radioactive sources deposit in patients. Occurs on a study by study, case by case basis that the subject patient is involved in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 71  Rad/Nuc Med Procedures                     | ^RAMIS(71  This file contains all the procedures that may be associated with an imaging exam. If the procedure has an inactivation date less than the current date then it is not a valid choice and will not appear as a selection to the user. Entries should be deactivated rather than deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 71.1  Major Rad/Nuc Med AMIS Codes             | ^RAMIS(71.1  This file contains the valid AMIS codes, descriptions and weighted work units as assigned by VACO. The data in this file is used in the compilation of various workload reports.  Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 71.11  New Rad Procedure Workup                | ^RAMIS(71.11  This file houses the new procedures being created in file 71 with a “Detailed” Type temporarily while the procedure is being created and will be removed from thos location once the procedure has been completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 71.1235  Radiology Procedure Map to CC Consult | ^RA(71.1235  This file is added with radiology patch RA*5.0*223 and contains  radiology procedures that are associated with a consult service for the purpose of community care referrals of radiology orders. The entries in this file are used by the radiology option 'Refer Selected Requests to COMMUNITY CARE Provider' [RA ORDERREF] to determine if a special consult title should be used for the community care consult order. The entries in this file are maintained nationally and should not be modified.                                                                                                                                                                                                                                                                                                              |
| 71.2  Procedure Modifiers                      | ^RAMIS(71.2  This file contains the modifiers that can be associated with an imaging exam. These modifiers are used to further describe the procedure associated with the exam.  Data comes with the file. It is ADDed ONLY IF NEW to the site's existing entries. Only modifiers with an internal entry number of less than 6 are exported with this version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 71.3  Rad/Nuc Med Common Procedure             | ^RAMIS(71.3  This file contains the procedures used in the display of the common procedures when requesting a procedure. Forty active procedures are allowed per imaging type.  No data comes with the file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 71.4  Rad/Nuc Med Procedure Message            | ^RAMIS(71.4  This file contains messages concerning special requirements when ordering a procedure. One or more of these messages can be tied to a procedure in the Rad/Nuc Med Procedures file (#71) so that they are displayed to a requestor at the time an order is placed.  No data comes with the file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 71.5  Imaging Stop Codes                       | ^RAMIS(71.5  This file contains valid imaging stop codes. It is not pointed to by any other file. The Rad/Nuc Med ADPAC should make sure this file is updated. Obsolete or unused entries should be deleted. This file should contain all stop codes that can be assigned to imaging locations at the facility.  No data comes with the file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 71.6  Route of Administration                  | ^RAMIS(71.6  This file contains possible routes of radiopharmaceutical administration used in imaging exams.  Data comes with this file. Routes may be added/edited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 71.7  Site of Administration                   | ^RAMIS(71.7  This file contains frequently-used sites of radiopharmaceutical administration for imaging exams.  Data comes with this file. Sites may be added/edited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 71.8  Radiopharmaceutical Source               | ^RAMIS(71.8  This file contains the names of vendors, pharmacies, and other sources of radiopharmaceuticals.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 71.9  Radiopharmaceutical Lot                  | ^RAMIS(71.9  This file is used to record names of radiopharmaceutical lots, batches, vials, syringes, or kits at the discretion of the facility.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 71.98  Master Radiology Site File              | This VistA file is a national file used by all VA VistA sites that includes a configurable parameter that will indicate whether ISAAC is active or not, a field named “SEEDING COMPLETE” that controls whether messages are sent to NTRT when a new procedure is created, and monitors the mapping of radiology procedures to the Master Radiology Procedure File (MRPF) and allows the user to stop and restart the mapping process without losing their place in the RAD/NUC MED PROCEDURE file (#71).                                                                                                                                                                                                                                                                                                                             |
| 71.99  Master Radiology Procedure File (MRPF)  | This VistA file is a national file used by all VA VistA sites with the following fields: reflecting the standardized procedure the GOLD NAME field which points to the MRPF NAME field in file 71, the VUID NUMBER, the CPT Code, the LOINC Code, LOINC Long description, LOINC Short description, and MRPF LONG NAME for the purposes of interoperability between VA offices and external entities.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 72  Examination Status                         | ^RA(72  This file contains the statuses an imaging exam may be in, as it is processed. Each status has a set of parameters that drives exam processing and management report logic.  Data comes with the file. It is MERGE'd with existing entries. Statuses can be edited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 73.1  Rad Modality Defined Terms               | VistA Imaging software will build a modality work list using this file and the Rad/Nuc Med Procedure file (#71) entries. The work list identifies the scheduled radiology cases to be performed on the individual modality (equipment). Entries in this file are as defined in the DICOM Standards PS 3.3 - 1998 under section General Series Attribute Descriptions (C.7.3.1.1).  Data comes with this file. Do not change/add/delete any records in this file.                                                                                                                                                                                                                                                                                                                                                                     |
| 73.2  Radiology CPT By Procedure Type          | ^RA(73.2  This file contains Procedure Types and CPT Codes supplied by the Office of Patient Care Services.  Data comes with this file. The data cannot be edited locally. Records may be added by the Office of Patient Care Services via a new Radiology patch; existing records may be updated but never deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 74  Rad/Nuc Med Reports                        | ^RARPT(  This file contains the reports for registered exams.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 74.1  Standard Reports                         | ^RA(74.1  This file contains the standard report text the interpreting physician can choose from when dictating a report.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 74.2  Report Batches                           | ^RABTCH(74.2  This file provides the mechanism to group draft reports into logical categories to help in the efficient processing of these reports.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 74.3  Report Distribution Queue                | ^RABTCH(74.3  This file contains the names of the distribution queues and the category of reports for each queue.  Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 74.4  Report Distribution                      | ^RABTCH(74.4  This file points to the Rad/Nuc Med Reports file (#74). It contains the only verified reports associated with the various active distribution queues.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 75.1  Rad/Nuc Med Orders                       | ^RAO(75.1  This file contains all information pertaining to an imaging order entered for a patient.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 75.2  Rad/Nuc Med Reason                       | ^RA(75.2  This file contains the reasons a user may select from when placing an order in the Hold or Cancelled status.  Data comes with this file. Changing or adding data to this file is prohibited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 75.3  Community Care Justifications            | ^RA(75.3  WARNING: ENTRIES SHOULD NOT BE ADDED/DELETED/CHANGED FROM THIS FILE.  This file contains only data supplied by the Office of Community  Care. The data are sent to the Radiology development and  maintenance teams.  This file contains the justifications a user may select from when  referring an order to Community Care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 78.1  Complication Types                       | ^RA(78.1  This file contains the types of complications that may occur while a procedure is being performed.  Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 78.2  Lbl/Hdr/Ftr Formats                      | ^RA(78.2  This file contains the print formats for flash cards, exam labels, jacket labels, report headers and report footers.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 78.3  Diagnostic Codes                         | ^RA(78.3  This file contains the diagnostic codes that can be associated with an exam. The diagnostic code represents a quick overall summary of what the interpreting physician wrote in the report concerning the exam. The diagnostic code is not the impression. The impression is stored in the Impression field (#300) of the Rad/Nuc Med Reports file (#74).  Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.  Patch RA*5.0*97 added the following Diagnostic Codes to this file:  1100 BI-RADS CATEGORY 0  1101 BI-RADS CATEGORY 1  1102 BI-RADS CATEGORY 2  1103 BI-RADS CATEGORY 3  1104 BI-RADS CATEGORY 4  1105 BI-RADS CATEGORY 5  1106 BI-RADS CATEGORY 6  1200 ABDOMINAL AORTIC ANEURYSM NOT PRESENT  1201 ABDOMINAL AORTIC ANEURYSM PRESENT  1202 DOES NOT SATISFY SCREEN FOR AAA |
| 78.4  Film Sizes                               | ^RA(78.4  This file contains the allowable film sizes that the technologist can choose from when entering the film data for an exam.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 78.6  Camera/Equip/Rm                          | ^RA(78.6  This file contains all the rooms that may be used to perform imaging examinations. The Imaging Locations file (#79.1) uses this file to indicate which rooms are allowable choices when the technologist attaches a camera/equipment/room to an exam that is performed.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 78.7  Label Print Fields                       | ^RA(78.7  This file contains the names of the data fields that can be printed on a flash card, exam label, jacket label, report header and report footer. The formats indicating which fields to print are stored in the Lbl/Hdr/Ftr Formats file (#78.2).  Data comes with this file. It OVERWRITE's existing entries in the site's data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 79  Rad/Nuc Med Division                       | ^RA(79  The package is designed to handle multiple divisions within a medical center. This file contains, for each division entry, parameters that the package uses during various stages of exam and report processing.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 79.1  Imaging Locations                        | ^RA(79.1  Within an imaging division there may be a number of physical locations where an imaging procedure can be performed. This file contains for each imaging location entry, parameters that the module uses during various stages of exam and report processing and inquiring.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 79.2  Imaging Type                             | ^RA(79.2  This file contains for each imaging type entry parameters that the package uses during various stages of exam and report processing.  Data comes with the file. It is MERGE'd with existing entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 79.3  HL7 Message Exceptions                   | ^RA(79.3  This file contains details of HL7 messages from Sending Applications that have been rejected by Rad/Nuc Med.  No data comes with this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 79.7  Rad/Nuc Med HL7 Application Exceptions   | ^RA(79.7  This file contains parameters related to application exceptions in processing of HL7 Radiology messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Templates

#### Input Templates

Table 9 - Input Templates

|   **FILE** | **NAME**                  | **DESCRIPTION**                                                                                                                                                                                                                                           |
|------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       70   | RA DIAGNOSTIC BY CASE     | This template is used by the Diagnostic Code Entry by Case No. option.                                                                                                                                                                                    |
|       70   | RA EXAM EDIT              | This template is used to edit exams.                                                                                                                                                                                                                      |
|       70   | RA LAST PAST VISIT        | This template is used when adding the last visit prior to implementing the VistA Radiology/Nuclear Medicine package.                                                                                                                                      |
|       70   | RA NO PURGE SPECIFICATION | This template is used to set the no purge flag for an exam in the Indicate No Purging of an Exam/report option. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] & ‘Indicate No Purging of an Exam/report’ [RA PURGE] options. |
|       70   | RA OUTSIDE ADD            | This template is used to enter outside films for tracking purposes.                                                                                                                                                                                       |
|       70   | RA OUTSIDE EDIT           | This template is used to edit information on outside film tracking.                                                                                                                                                                                       |
|       70   | RA OUTSIDE SUPEROK        | This template is used to flag an outside film as needing a supervisor's concurrence in order to be released.                                                                                                                                              |
|       70   | RA OVERRIDE               | This template is used to override the status of an exam and set it to Complete.                                                                                                                                                                           |
|       70   | RA REGISTER               | This template is used to register patients for exams. It is compiled into the RACTRG* routines.                                                                                                                                                           |
|       70   | RA STATUS CHANGE          | This template is used for the Status Tracking of Exams option.                                                                                                                                                                                            |
|       71   | RA PRO MAP                | Used in mapping the file 71 to file 71.99                                                                                                                                                                                                                 |
|       71   | RA PROCEDURE EDIT         | This template is used to enter and edit procedures.  There is an option to select a Master Radiology Procedure File (MRPF) entry when a CPT code is associated with a “DETAILED” Type procedure.                                                          |
|       71.3 | RA COMMON PROCEDURE EDIT  | This template is used to set up and change the common procedure display used when requesting an exam.                                                                                                                                                     |
|       72   | RA STATUS ENTRY           | This template is used to enter and edit a status for an exam.                                                                                                                                                                                             |
|       74   | RA PRE-VERIFY REPORT EDIT | This template is used by interpreting resident physicians to edit and pre-verify their reports.                                                                                                                                                           |
|       74   | RA PRE-VERIFY REPORT ONLY | This template is used by interpreting resident physicians to pre-verify their reports only.                                                                                                                                                               |
|       74   | RA REPORT EDIT            | This template is used to enter and edit reports in File #74. It is compiled into the RACTWR* routines.                                                                                                                                                    |
|       74   | RA VERIFY REPORT ONLY     | This template is used to verify reports in File #74. It is compiled into the RACTVR* routines.                                                                                                                                                            |
|       74.1 | RA STANDARD REPORT ENTRY  | This template is used to enter standard reports into File #74.                                                                                                                                                                                            |
|       74.3 | RA DISTRIBUTION EDIT      | This template is used in the Reports Distribution Edit option.                                                                                                                                                                                            |
|       74.3 | RA DISTRIBUTION LOG       | This template is used to enter data in the activity log of File #74.3.                                                                                                                                                                                    |
|       75.1 | RA OERR EDIT              | This template is to edit requests by OE/RR V. 2.5 users. It is compiled into the RACTOE* routines.                                                                                                                                                        |
|       75.1 | RA ORDER EXAM             | This template is used to request an exam.                                                                                                                                                                                                                 |
|       75.1 | RA QUICK EXAM ORDER       | This template is used by OE/RR V. 2.5 users for ordering an exam. It is compiled into the RACTQE* routines.                                                                                                                                               |
|       78.2 | RA FLASH CARD EDIT        | This template is used to enter and edit flash cards, jacket labels, exam labels, report headers and report footers.                                                                                                                                       |
|       79   | RA DIVISION PARAMETERS    | This template is used to enter division parameters for the package.                                                                                                                                                                                       |
|       79.1 | RA LOCATION PARAMETERS    | This template is used to enter the location parameters for the package.                                                                                                                                                                                   |
|       79.1 | RA SITE MANAGER           | This template is used by the IRM Service to define input and printing devices for the package.                                                                                                                                                            |
|       79.2 | RA IMAGE PARAMETERS       | This template is used to enter parameters for an imaging type.                                                                                                                                                                                            |
|       79.2 | RA ON-LINE CRITERIA       | This template is used to enter data associated with the storing of on-line data for an imaging location.                                                                                                                                                  |
|      200   | RA PERSONNEL              | This template is used to enter Radiology/ Nuclear Medicine personnel into the package.                                                                                                                                                                    |

#### Sort Templates

Table 10 - Sort Templates

|   **FILE** | **NAME**                    | **DESCRIPTION**                                                                                        |
|------------|-----------------------------|--------------------------------------------------------------------------------------------------------|
|       70   | RA DAILY LOG                | This template is used to sort exams by exam date and hospital division.                                |
|       70   | RA OUTSIDE LIST             | This template is used to sort the outside film registry.                                               |
|       71   | RA ALPHA LIST OF ACTIVES    | This template is used to determine which procedures are active and put them in alphabetical order.     |
|       71   | RA PROCEDURES BY AMIS       | This template is used to sort procedures by major AMIS code.                                           |
|       71   | RA PROCEDURES BY AMIS CODES | This template sorts procedures by AMIS code and then by CPT code.                                      |
|       71   | RA SERIES ONLY              | This template is used to sort procedures by "Series" type only.                                        |
|       74.4 | RA ALL UNPRINTED            | This template is used to sort the Unprinted Reports List for the report distribution queue.            |
|       74.4 | RA CLINIC BY PRINT DATE     | This template sorts the distribution queue by clinic location. Also, it sorts reports by print status. |
|       74.4 | RA WARD BY PRINT DATE       | This template sorts reports in the ward distribution queue by print date.                              |
|       75.1 | RA REQ REJECTED SORT        | This template sorts orders by date desired.                                                            |
|       78.2 | RA FLASH PRINT              | This template sorts the print formats by name for printing label set-ups.                              |
|       79.1 | RA EXAM ROOM LIST           | This template sorts examination rooms by Radiology/Nuclear Medicine location.                          |
|       79.1 | RA IMAGE LOC LIST           | This template is used to sort location parameters by imaging location.                                 |
|      200   | RA PERSONNEL LIST           | This template sorts Radiology/Nuclear Medicine personnel by classification (e.g., technologist).       |

#### Print Templates

Table 11 - Print Templates

|   **FILE** | **NAME**                 | **DESCRIPTION**                                                                                                                                                             |
|------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       70   | RA DAILY LOG             | This template is used to print a daily log of registered examinations.                                                                                                      |
|       70   | RA OUTSIDE LIST          | This template is used to generate the Delinquent Outside Film Report for outpatients.                                                                                       |
|       71   | RA ALPHA LIST OF ACTIVES | This template produces an alphabetic listing of all active Radiology/Nuclear Medicine procedures.                                                                           |
|       71   | RA PROCEDURE BY AMIS     | This template is used to generate the Short Active Procedure List.                                                                                                          |
|       71   | RA PROCEDURE LIST        | This template is used to generate the Long Procedure List.                                                                                                                  |
|       71   | RA PROCEDURE SHORT LIST  | This template is used to generate the Inactive Short Procedure List.                                                                                                        |
|       74.1 | RA STANDARD REPORTS LIST | This template is used in the Standard Reports Print option.                                                                                                                 |
|       74.3 | RA DISTRIBUTION          | This template is used in the Report Distribution List.                                                                                                                      |
|       74.4 | RA ALL UNPRINTED REPORTS | This template is used to generate a list of reports in the distribution queue that have not been printed.                                                                   |
|       74.4 | RA PRINTED REPORTS       | This template is used in the List Reports in a Batch option.                                                                                                                |
|       74.4 | RA UNPRINTED REPORTS     | This template is used to generate reports in the distribution queue that have not yet been printed                                                                          |
|       75.1 | RA REQ REJECTED PRINT    | This template generates reports that identify orders rejected by CPRS within a date range determined by the date desired.                                                   |
|       78.2 | RA FLASH PRINT           | This template is used to generate the Flash Card/Label List.                                                                                                                |
|       78.3 | RA DIAGNOSTIC CODE PRINT | This template is used to print the Diagnostic Code List.                                                                                                                    |
|       78.4 | RA FILM SIZE             | This template is used to provide information about types of film (e.g., inactivation date).                                                                                 |
|       79   | RA IMAGE DIV LIST        | This template is used to generate a list of divisions.                                                                                                                      |
|       79.1 | RA EXAM ROOM LIST        | This template is used to generate an exam room list.                                                                                                                        |
|       79.1 | IMAGE LOC LIST           | This template is used to generate a list of imaging locations.                                                                                                              |
|       79.2 | RA ACTIVITY LOG          | This template is used to print the activity log from File #79.2.                                                                                                            |
|      200   | RA PERSONNEL LIST        | This template is used to generate a list of personnel who have a Radiology/Nuclear Medicine classification and their inactivation date, if applicable.                      |
|      200   | RA RESIDENT RADIOLOGIST  | This template is used to generate a list of personnel who have a Radiology/Nuclear Medicine classification, their inactivation date and whether a staff review is required. |

#### List Templates

Table 12 - List Templates

|   **FILE** | **NAME**          | **DESCRIPTION**                                                                                                       |
|------------|-------------------|-----------------------------------------------------------------------------------------------------------------------|
|       79.3 | RA HL7 EXCEPTIONS | This template is used to display and print HL7 messages which have been rejected by VistA Radiology/Nuclear Medicine. |


## 16 Exported Options

### Exported Menus

#### IRM Menu [RA SITEMANAGER]

Device Specifications for Imaging Locations [RA DEVICE]

Distribution Queue Purge [RA RPTDISTPURGE]

Failsoft Parameters [RA FAILSOFT]

Imaging Type Activity Log [RA IMGLOG]

Rebuild Distribution Queues [RA RPTDISTREBUILD]

Report File x-ref Clean-up Utility [RA RPTDISTREBUILD]

Site Accession Number Set-up [RA SITEACCNUM]

Credit Completed Exams for an Imaging Location

Enable HL7 reprocessing for locked studies [RASAN ENABLE REPROCESSING]

Resource Device Specifications for Division [RA RESOURCE DEVICE]

Schedule Perf Indic Summary for 15 th of month [RA PERFORMIN SCHEDULE]

Template Compilation [RA COMPILE TEMPLATES]

#### Rad/Nuc Med Total System Menu [RA OVERALL]

Exam Entry/Edit Menu [RA EXAMEDIT]

Add Exams to Last Visit [RA ADDEXAM]

Cancel an Exam [RA CANCEL]

Case No. Exam Edit [RA EDITCN]

Diagnostic Code and Interpreter Edit by Case No. [RA DIAGCN]

Edit Exam by Patient [RA EDITPT]

Enter Last Past Visit Before DHCP [RA PAST]

Exam Status Display [RA STATLOOK]

Register Patient for Exams [RA REG]

Status Tracking of Exams [RA STATRACK]

Switch Locations [RA LOC SWITCH]

View Exam by Case No. [RA VIEWCN]

Films Reporting Menu [RA RPT]

Batch Reports Menu [RA BTCH]

Add/Remove Report From Batch [RA BTCHREMOVE]

Create a Batch [RA BTCHNEW]

Delete Printed Batches [RABTCHDEL]

List Reports in a Batch [RA BTCHLIST]

Print a Batch of Reports [RA BTCHPRINT]

Verify Batch [RA BTCHVERIFY] **LOCKED: RA VERIFY**

Display a Rad/Nuc Med Report [RA RPTDISP]

Distribution Queue Menu [RA RPTDIST]

Activity Logs [RA RPTDISTACTIVITY]

Clinic Distribution List [RA RPTDISTLISTCLINIC]

Individual Ward [RA RPTDISTSINGLEWARD]

Print By Routing Queue [RA RPTDISTQUE]

Report's Print Status [RA RPTDISTPRINTSTATUS]

Single Clinic [RA RPTDISTSINGLECLINIC]

Unprinted Reports List [RA RPTDISTLISTUNPRINTED]

Ward Distribution List [RA RPTDISTLISTWARD]

Draft Report (Reprint) [RA REPRINT]

On-line Verifying of Reports [RA RPTONLINEVERIFY] **LOCKED: RA VERIFY**

Outside Report Entry/Edit [RA OUTSIDE RPTENTRY]

Report Entry/Edit [RA RPTENTRY]

Resident On-Line Pre-Verification [RA RESIDENT PRE-VERIFY]

Select Report to Print by Patient [RA RPTPAT]

Switch Locations [RA LOC SWITCH]

Verify Report Only [RA RPTVERIFY] **LOCKED: RA VERIFY**

Management Reports Menu [RA MGTRPTS]

Daily Management Reports [RA DAILYRPTS]

Abnormal Exam Report [RA ABNORMAL]

Complication Report [RA COMPLICATION]

Daily Log Report [RA LOG]

Delinquent Outside Film Report for Outpatients [RA OUTSIDERPT]

Delinquent Status Report [RA DELINQUENT]

Examination Statistics [RA DAISTATS]

Incomplete Exam Report [RA INCOMPLETE]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Radiopharmaceutical Usage Report [RA RADIOPHARM USAGE]

Unverified Reports [RA DAIUVR]

Functional Area Workload Reports [RA LWKL]

Clinic Report [RA LWKLCLINIC]

PTF Bedsection Report [RA LWKLBEDSEC]

Service Report [RA LWKLSERVICE]

Sharing Agreement/Contract Report [RA LWKLSHARING]

Ward Report [RA LWKLWARD]

Personnel Workload Reports [RA WKL]

Physician CPT Report by Imaging Type [RA WKLIPHY CPT ITYPE]

Physician Report [RA WKLPHY]

Physician scaled wRVU Report by Imaging Type [RA WKLIPHY SWRVU ITYPE]

Physician scaled wRVU Report by CPT [RA WKLIPHY SWRVU CPT]

Physician wRVU Report by CPT [RA WKLIPHY WRVU CPT]

Physician wRVU Report by Imaging Type [RA WKLIPHY WRVU ITYPE]

Radiopharmaceutical Administration Report [RA RADIOPHARM ADMIN]

Resident Report [RA WKLRES]

Staff Report [RA WKLSTAFF]

Technologist Report [RA WKLTECH]

Transcription Report [RA TRANSRIP REPORT]

Special Reports [RA SPECRPTS]

AMIS Code Dump by Patient [RA AMISDUMP]

AMIS Report [RA AMIS]

Camera/Equip/Rm Report [RA WKLROOM]

Cost Distribution Report [RA CDR REPORT]

Detailed Procedure Report [RA WKLPROCEDURE]

Film Usage Report [RA FILMUSE]

Procedure Scaled wRVU/CPT Report [RA PROC CPTSWRVU]

Procedure wRVU/CPT Report [RA PROC CPTWRVU]

Procedure/CPT Statistics Report [RA CPTSTATS]

Radiation Dose Summary Report [RA RAD DOSE SUMMARY]

Status Time Report [RA STATRPT]

Wasted Film Report [RA WASTED FILM RPT]

Timeliness Reports [RA TIMELINESS MENU] ,

Outpatient Procedure Wait Time [RA TIMELINESS OUTPATIENT MENU]

Summary/Detail report [RA TIMELINESS REPORT]

Verification Timeliness [RA TIMELINESS VER MENU]

Enter/Edit OUTLOOK mail group [RA PERFORMIN MAIL GROUP ENTRY]

Run Previous Month's Summary Report [RA PERFORMIN TASKLM]

Summary/Detail report [RA PERFORMIN RPTS]

Outside Films Registry Menu [RA OUTSIDE]

Add Films to Registry [RA OUTADD]

Delinquent Outside Film Report for Outpatients [RA OUTSIDERPT]

Edit Registry [RA OUTEDIT]

Flag Film to Need 'OK' Before Return [RA OUTFLAG]

Outside Films Profile [RA OUTPROF]

Patient Profile Menu [RA PROFILES]

Detailed Request Display [RA ORDERDISPLAY]

Display Patient Demographics [RA PROFDEMOS]

Exam Profile (selected sort) [RA PROFSORT]

Exam Profile with Radiation Dosage Data [RA PROFRAD DOSE]

Outside Films Profile [RA OUTPROF]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Radiology/Nuclear Med Order Entry Menu [RA ORDER]

Menu of Request Log Options ... [RA ORDERLOG MENU]

Log of Discontinued Requests [RA ORDER DISCONTINUED]

Log of CPRS Rejected Requests by Date Desired [RA ORDERLOG REJECTED]

Pending/Hold Rad/Nuc Med Request Log [RA ORDERPENDING]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Ward/Clinic Scheduled Request Log [RA ORDERLOGLOC]

Refer Selected Requests to COMMUNITY CARE Provider [RA ORDERREF]

Cancel a Request [RA ORDERCANCEL]

Detailed Request Display [RA ORDERDISPLAY]

Hold a Request [RA ORDERHOLD]

Print Rad/Nuc Med Requests by Date [RA ORDERPRINTS]

Print Selected Requests by Patient [RA ORDERPRINTPAT]

Rad/Nuc Med Procedure Information Look-Up [RA DISPLAY IMAGPROCINFO]

Request an Exam [RA ORDEREXAM]

Schedule a Request [RA ORDERSCHEDULE]

Update a Hold Request [RA ORDERREASON UPDATE]

Supervisor Menu [RA SUPERVISOR]

Radiology HL7 Menu [RA HL7 MENU]

Rad/Nuc Med HL7 Voice Reporting Errors [RA HL7 VOICE REPORTING ERRORS]

Resend Radiology HL7 Message [RA HL7 MESSAGE RESEND] **LOCKED: RA MGR**

Resend Radiology HL7 Message by Date Range [RA HL7 RESEND BY DATE RANGE]

Radiology Study Tracker Menu [MAGD RAD STUDY TRACKER]

Check a Radiology or Consult Study for Images [MAGD ACN CHECK]

Report Radiology Studies without Images [MAGD RAD RANGE CHECK]

**Locked with MAGD QR REPORT

DICOM Query Client [MAGD QUERY]

DICOM Query/Retrieve Client [MAGD QUERY/RETRIEVE]

**&gt; Locked with MAGD QR MANUAL RETRIEVE

Compare Radiology Image Count on PACS with VistA [MAGD RAD COUNT COMPARE] **Locked with MAGD QR REPORT

Retrieve Missing Radiology Images from PACS [MAGD RAD AUTO RETRIEVE] **Locked with MAGD QR AUTO RETRIEVE

Display stats for automatic radiology Q/R runs [MAGD Q/R RAD RUN STATI

STICS]

Delete the stats for automatic radiology Q/R runs [MAGD RAD STATISTICS

DELETE] **Locked with MAG SYSTEM

Stop automatic Q/R processes [MAGD STOP AUTOMATIC PROCESSES]

**Locked with MAGD QR REPORT

Rad/Nuc Med Report Management [RA REPORT MANAGEMENT]

Delete a Report [RA DELETERPT] **Locked with RA RPTMGR

Restore a Deleted Report [RA RESTORE REPORT] **Locked with RA RPTMGR

Unverify a Report for Amendment [RA UNVERIFY] **Locked with RA RPTMGR

Access Uncorrected Reports [RA UNCORRECTED REPORTS]

Delete Printed Batches By Date [RA BTCHDELDATE]** LOCKED: RA MGR**

Exam Deletion [RA DELETEXAM] **LOCKED: RA MGR**

Inquire to File Entries [DIINQUIRE]

List Exams with Inactive/Invalid Statuses [RA INVALID EXAM STATUSES}

Maintenance Files Print Menu [RA MAINTENANCEP]

Complication Type List [RA COMPRINT]

Diagnostic Code List [RA DIAGP]

Examination Status List [RA EXAMSTATUSP]

Film Sizes List [RA FILMP]

Label/Header/Footer Format List [RA FLASHFORMP]

Major AMIS Code List [RA MAJORAMISP]

Modifier List [RA MODIFIERP]

Nuclear Medicine List Menu [RA NM PRINT MENU]

Lot (Radiopharmaceutical) Number List [RA NM PRINT LOT]

Route of Administration List [RA NM PRINT ROUTE]

Site of Administration List [RA NM PRINT SITE]

Vendor/Source (Radiopharmaceutical) List [RA NM PRINT SOURCE]

Procedure File Listings [RA PROCLISTS]

Display Rad/NM Procedure Contrast Media History [RA CMAUDIT HISTORY]

Active Procedure List (Long) [RA PROCLONG]

Active Procedure List (Short) [RA PROCSHORT]

Alpha Listing of Active Procedures [RA ALPHALIST]

Barcoded Procedure List [RA BARPROCPRINT]

Inactive Procedure List (Long) [RA INACPRCLONG]

Invalid CPT/Stop Code List [RA INVALID CPT/STOP]

List of Inactive Procedures (Short) [RA INACPRCSHORT]

List of Procedures with Contrast [RA PROCMEDIA]

Parent Procedure List [RA PROCPARENT]

Procedure Message List [RA PROCMSGPRINT]

Series of Procedures List [RA PROCSERIES]

Report Distribution Lists [RA DISTP]

Sharing Agreement/Contract List [RA SHARINGP]

Standard Reports Print [RA STANDPRINT]

VistaRad Category Print [RA VISTARAD CATEGORY P]

Override a Single Exam Status to 'complete' [RA OVERRIDE]**LOCKED: RA MGR**

Print File Entries [DIPRINT]

Rad/Nuc Med Personnel Menu [RA PNL]

Classification Enter/Edit [RA PNLCLASS]

Clerical List [RA PNLCLERK]

Interpreting Resident List [RA PNLRES]

Interpreting Staff List [RA PNLSTAFF]

Technologist List [RA PNLTECH]

Search File Entries [DISEARCH]

Switch Locations [RA LOC SWITCH]

System Definition Menu [RA SYSDEF]

Camera/Equip/Rm Entry/Edit [RA SYSEXROOM]

Division Parameter Set-up [RA SYSDIV]

Inactivate a Location [RA SYSINACT]

List of Cameras/Equip/Rms [RA SYSEXLIST]

Location Parameter List [RA SYSLOCLIST]

Location Parameter Set-up [RA SYSLOC]

Outside Location Order Suppression [RA SYSUPLOC]

Print Division Parameter List [RA SYSDIVLIST]

Update Exam Status [RA UPDATEXAM]

Utility Files Maintenance Menu [RA MAINTENANCE]

Complication Type Entry/Edit [RA COMPEDIT]

Diagnostic Code Enter/Edit [RA DIAGEDIT]

Examination Status Entry/Edit [RA EXAMSTATUS]

Film Type Entry/Edit [RA FILMEDIT]

HL7 Interface Exceptions List [RA HL7 EXCEPTIONS]

Label/Header/Footer Formatter [RA FLASHFORM]

Major AMIS Code Entry/Edit [RA MAJORAMIS]

Nuclear Medicine Setup Menu [RA NM EDIT MENU]

Lot (Radiopharmaceutical) Number Enter/Edit [RA NM EDIT LOT]

Route of Administration Enter/Edit [RA NM EDIT ROUTE]

Site of Administration Enter/Edit [RA NM EDIT SITE]

Vendor/Source (Radiopharmaceutical) Enter/Edit [RA NM EDIT SOURCE]

Order Entry Procedure Display Menu [RA ORDERDISPLAY MENU]

Common Procedure Enter/Edit [RA COMMON PROCEDURE]

Create OE/RR Protocol from Common Procedure [RA CREATE OE/RR PROTOCOL]

Display Common Procedure List [RA DISPLAY COMMON PROCEDURES]

Procedure Edit Menu [RA PROCEDURE EDIT MENU]

Activate/Inactivate Standard Procedures [RA PROCEDURE ACTIVATE]

Cost of Procedure Enter/Edit [RA PROCOSTEDIT]

Procedure Enter/Edit [RA PROCEDURE]

Procedure Message Entry/Edit [RA PROCMSGEDIT]

Procedure Modifier Entry [RA MODIFIER]

Reports Distribution Edit [RA DISTEDIT]

Sharing Agreement/Contract Entry/Edit [RA SHARING]

Standard Reports Entry/Edit [RA STANDRPTS]

Valid Imaging Stop Codes Edit [RA VALID STOP CODES] **LOCKED: RA MGR**

VistaRad Category Entry/Edit [RA VISTARAD CATEGORY E]

Update Patient Record [RA PTEDIT]

User Utility Menu [RA USERUTL]

SYN Synch Exams with CPRS &amp; RIS Orders [RA EXAM ORDER SYNCH]

**&gt;Locked with RA MGR

Duplicate Dosage Ticket [RA DOSAGE TICKET]

Duplicate Flash Card [RA FLASH]

Jacket Labels [RA LABELS]

Print Worksheets [RA WORKSHEETS]

Set preference for Long Display of Procedures [RA SET PREFERENCE LONG DISPLAY]

Switch Locations [RA LOC SWITCH]

Test Label Printer [RA LABELTEST]

#### Rad/Nuc Med Clerk Menu [RA CLERKMENU]

Add Exams to Last Visit [RA ADDEXAM]

Cancel an Exam [RA CANCEL]

Case No. Exam Edit [RA EDITCN]

Display a Rad/Nuc Med Report [RA RPTDISP]

Display Patient Demographics [RA PROFDEMOS]

Duplicate Flash Card [RA FLASH]

Exam Status Display [RA STATLOOK]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Radiology/Nuclear Med Order Entry Menu [RA ORDER]

Refer Selected Requests to COMMUNITY CARE Provider [RA ORDERREF]

Cancel a Request [RA ORDERCANCEL]

Detailed Request Display [RA ORDERDISPLAY]

Hold a Request [RA ORDERHOLD]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Pending/Hold Rad/Nuc Med Request Log [RA ORDERPENDING]

Print Rad/Nuc Med Requests by Date [RA ORDERPRINTS]

Print Selected Requests by Patient [RA ORDERPRINTPAT]

Rad/Nuc Med Procedure Information Look-Up [RA DISPLAY IMAGPROCINFO]

Request an Exam [RA ORDEREXAM]

Schedule a Request [RA ORDERSCHEDULE]

Update a Hold Request [RA ORDERREASON UPDATE]

Ward/Clinic Scheduled Request Log [RA ORDERLOGLOC]

Register Patient for Exams [RA REG]

Switch Locations [RA LOC SWITCH]

View Exam by Case No. [RA VIEWCN]

#### Rad/Nuc Med Ward Clerk Menu [RA WARD]

Cancel a Request [RA ORDERCANCEL]

Detailed Request Display [RA ORDERDISPLAY]

Display a Rad/Nuc Med Report [RA RPTDISP]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Request an Exam [RA ORDEREXAM]

Ward/Clinic Scheduled Request Log [RA ORDERLOGLOC]

#### Rad/Nuc Med File Room Clerk Menu [RA FILERM]

Detailed Request Display [RA ORDERDISPLAY]

Display a Rad/Nuc Med Report [RA RPTDISP]

Display Patient Demographics [RA PROFDEMOS]

Outside Films Registry Menu [RA OUTSIDE]

Add Films to Registry [RA OUTADD]

Delinquent Outside Film Report for Outpatients [RA OUTSIDERPT]

Edit Registry [RA OUTEDIT]

Flag Film To Need 'OK' Before Return [RA OUTFLAG]

Outside Films Profile [RA OUTPROF]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Select Report to Print by Patient [RA RPTPAT]

User Utility Menu [RA USERUTL]

SYN Synch Exams with CPRS &amp; RIS Orders [RA EXAM ORDER SYNCH]

**&gt; Locked with RA MGR

Duplicate Dosage Ticket [RA DOSAGE TICKET]

Duplicate Flash Card [RA FLASH]

Jacket Labels [RA LABELS]

Print Worksheets [RA WORKSHEETS]

Switch Locations [RA LOC SWITCH]

Test Label Printer [RA LABELTEST]

View Exam by Case No. [RA VIEWCN]

Ward/Clinic Scheduled Request Log [RA ORDERLOGLOC]

#### Interpreting Physician Menu [RA RADIOLOGIST]

Detailed Request Display [RA ORDERDISPLAY]

Display a Rad/Nuc Med Report [RA RPTDISP]

Draft Report (Reprint) [RA REPRINT]

On-line Verifying of Reports [RA RPTONLINEVERIFY] **LOCKED: RA VERIFY**

Print Selected Requests by Patient [RA ORDERPRINTPAT]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Resident On-Line Pre-Verification [RA RESIDENT PRE-VERIFY]

Select Report to Print by Patient [RA RPTPAT]

Switch Locations [RA LOC SWITCH]

View Exam by Case No. [RA VIEWCN]

#### Reports Menu [RA REPORTS]

Abnormal Exam Report [RA ABNORMAL]

Complication Report [RA COMPLICATION]

Daily Log Report [RA LOG]

Delinquent Outside Film Report for Outpatients [RA OUTSIDERPT]

Delinquent Status Report [RA DELINQUENT]

Duplicate Flash Card [RA FLASH]

Film Usage Report [RA FILMUSE]

Functional Area Workload Reports [RA LWKL]

Clinic Report [RA LWKLCLINIC]

PTF Bedsection Report [RA LWKLBEDSEC]

Service Report [RA LWKLSERVICE]

Sharing Agreement/Contract Report [RA LWKLSHARING]

Ward Report [RA LWKLWARD]

Jacket Labels [RA LABELS]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Personnel Workload Reports [RA WKL]

Physician CPT Report by Imaging Type [RA WKLIPHY CPT ITYPE]

Physician Report [RA WKLPHY]

Physician scaled wRVU Report by Imaging Type [RA WKLIPHY SWRVU ITYPE]

Physician scaled wRVU Report by CPT [RA WKLIPHY SWRVU CPT]

Physician wRVU Report by CPT [RA WKLIPHY WRVU CPT]

Physician wRVU Report by Imaging Type [RA WKLIPHY WRVU ITYPE]

Radiopharmaceutical Administration Report [RA RADIOPHARM ADMIN]

Resident Report [RA WKLRES]

Staff Report [RA WKLSTAFF]

Technologist Report [RA WKLTECH]

Transcription Report [RA TRANSCRIP REPORT]

Print Worksheets [RA WORKSHEETS]

Status Time Report [RA STATRPT]

Test Label Printer [RA LABELTEST]

#### Rad/Nuc Med Secretary Menu [RA SECRETARY]

Display a Rad/Nuc Med Report [RA RPTDISP]

Draft Report (Reprint) [RA REPRINT]

Rad/Nuc Med Personnel Menu [RA PNL]

Classification Enter/Edit [RA PNLCLASS]

Clerical List [RA PNLCLERK]

Interpreting Resident List [RA PNLRES]

Interpreting Staff List [RA PNLSTAFF]

Technologist List [RA PNLTECH]

Radiology/Nuclear Med Order Entry Menu [RA ORDER]

Cancel a Request [RA ORDERCANCEL]

Detailed Request Display [RA ORDERDISPLAY]

Hold a Request [RA ORDERHOLD]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Pending/Hold Rad/Nuc Med Request Log [RA ORDERPENDING]

Print Rad/Nuc Med Requests by Date [RA ORDERPRINTS]

Print Selected Requests by Patient [RA ORDERPRINTPAT]

Rad/Nuc Med Procedure Information Look-Up [RA DISPLAY IMAGPROCINFO]

Request an Exam [RA ORDEREXAM]

Schedule a Request [RA ORDERSCHEDULE]

Update a Hold Request [RA ORDERREASON UPDATE]

Ward/Clinic Scheduled Request Log [RA ORDERLOGLOC]

Report Entry/Edit [RA RPTENTRY]

Select Report to Print by Patient [RA RPTPAT]

Switch Locations [RA LOC SWITCH]

Verify Batch [RA BTCHVERIFY] **LOCKED: RA VERIFY**

Verify Report Only [RA RPTVERIFY] **LOCKED: RA VERIFY**

View Exam by Case No. [RA VIEWCN]

#### Rad/Nuc Med Technologist Menu [RA TECHMENU]

Add Exams to Last Visit [RA ADDEXAM]

Cancel an Exam [RA CANCEL]

Case No. Exam Edit [RA EDITCN]

Display a Rad/Nuc Med Report [RA RPTDISP]

Duplicate Flash Card [RA FLASH]

Log of Scheduled Requests by Procedure [RA ORDERLOG]

Patient Profile Menu [RA PROFILES]

Detailed Request Display [RA ORDERDISPLAY]

Display Patient Demographics [RA PROFDEMOS]

Exam Profile (selected sort) [RA PROFSORT]

Outside Films Profile [RA OUTPROF]

Profile of Rad/Nuc Med Exams [RA PROFQUICK]

Print Selected Requests by Patient [RA ORDERPRINTPAT]

Register Patient for Exams [RA REG]

Status Tracking of Exams [RA STATRACK]

Switch Locations [RA LOC SWITCH]

View Exam by Case No. [RA VIEWCN]

#### Rad/Nuc Med Transcriptionist Menu [RA TRANSCRIPTIONIST]

Batch Reports Menu [RA BTCH]

Add/Remove Report From Batch [RA BTCHREMOVE]

Create a Batch [RA BTCHNEW]

Delete Printed Batches [RA BTCHDEL]

List Reports in a Batch [RA BTCHLIST]

Print a Batch of Reports [RA BTCHPRINT]

Verify Batch [RA BTCHVERIFY] **LOCKED: RA VERIFY**

Diagnostic Code and Interpreter Edit by Case No. [RA DIAGCN]

Display a Rad/Nuc Med Report [RA RPTDISP]

Draft Report (Reprint) [RA REPRINT]

Report Entry/Edit [RA RPTENTRY]

Select Report to Print by Patient [RA RPTPAT]

Standard Reports Entry/Edit [RA STANDRPTS]

### Single Options

The following options do not appear on any menu:

- Rad/Nuc Med [RA OERR EXAM]
- Imaging Type Mismatch Report [RA EXAM/STATUS ITYPE MISMATCH]
- Autopurge of Distribution Queues [RA RPTDISTAUTOPURGE]
- Reprocess locked study accession error [RA REPROC] – This option should be scheduled to run and it will reprocess HL7 result messages that are rejected due to LOCK errors.

### Menu/Option Assignment

The RA SITEMANAGER menu may be assigned to the IRM staff member who supports this package. Descriptions of the RA SITEMANAGER options are in the Implementation and Maintenance section of this manual.

The RA OVERALL menu is the most extensive menu and may be assigned to the ADPAC.

All other menu and option assignments should be decided upon by the ADPAC. Descriptions of non-RA SITEMANAGER options may be found in the *ADPAC Guide* or *User Manual* .

### Protocols

The following protocols are exported with this version:

RA CANCEL

RA CANCEL 2.3

RA CANCEL 2.4

RA EVSEND OR

RA EXAMINED

RA EXAMINED 2.3

RA EXAMINED 2.4

RA HL7 EXCEPTIONS DELETE

RA HL7 EXCEPTIONS MENU

RA HL7 EXCEPTIONS NEXT

RA HL7 EXCEPTIONS PREVIOUS

RA HL7 EXCEPTIONS PRINT

RA HL7 EXCEPTIONS RESEND

RA OERR DEFAULT PROTOCOL

RA OERR EXAM

RA OERR PROFILE

RA ORDERABLE ITEM UPDATE

RA PSCRIBE ORM

RA PSCRIBE ORU

RA PSCRIBE TCP REPORT

RA PSCRIBE TCP SERVER RPT

RA RECEIVE

RA REG

RA REG 2.3

RA REG 2.4

RA RPT

RA RPT 2.3

RA RPT 2.4

RA SCIMAGE ORM

RA SCIMAGE ORU

RA SCIMAGE TCP REPORT

RA SCIMAGE TCP SERVER RPT

RA SEND ORM

RA SEND ORU

RA TALKLINK ORM

RA TALKLINK ORU

RA TALKLINK TCP REPORT

RA TALKLINK TCP SERVER RPT

RA TCP ORM

RA TCP ORU

RA VOICE TCP REPORT

RA VOICE TCP SERVER RPT

### FileMan Options

Three FileMan namespaced options are exported with this software to allow users to inquire, print or search Radiology/Nuclear Medicine package files. They are:

- DIINQUIRE
- DIPRINT
- DISEARCH

## 17 Archiving and Purging

This version of the Radiology/Nuclear Medicine package does not provide for the archiving of its data.

## 18 Callable Routines

For the latest information on active supported references, use the Custodial Package menu under the DBA's Integration Agreement menu on FORUM.

Select DBA Option: **i** ntegration Agreements Menu

O  Instructions for Entering IA's

1  Get New Integration #'s

2  Add/Edit

3  Inquire

4  Roll-up into Mail Message

5  File Agreements Menu ...

6  Routine Agreements Menu ...

7  Subscriber Package Menu ...

8  Custodial Package Menu ...

9  Print Other

10  Print Pending

11  Print Active

12  Print All

13  Supported References Menu ...

14  Private References Menu ...

15  Controlled Subscription References Menu ...

16  Agreement Lookup by Variable

Select Integration Agreements Menu Option: **8** Custodial Package Menu

1  ACTIVE by Custodial Package

2  Print ALL by Custodial Package

3  Supported References Print All

Select Custodial Package Menu Option: **1** ACTIVE by Custodial Package

Select PACKAGE NAME: **RADIOLOGY/NUCLEAR MEDICINE** RA

DEVICE: (Enter a device)

## 19 External Relations

The Radiology/Nuclear Medicine package relies on the following external packages to run effectively:

Table 13 - External Relations

| **PACKAGE**                     |   **MINIMUM VERSION NEEDED** |
|---------------------------------|------------------------------|
| Kernel                          |                          8   |
| VA FileMan                      |                         21   |
| MailMan                         |                          7.1 |
| PIMS                            |                          5.3 |
| Health Level Seven              |                          1.6 |
| Adverse Reaction Tracking (ART) |                          4   |
| OE/RR                           |                          2.5 |
| PCE                             |                          1   |
| Visit Tracking                  |                          2   |

The following external files are expected to be present, with data:

- CPT (#81)
- CPT Categories (#81.1)
- CPT Modifier (#81.3)
- Hospital Location (#44)
- Medical Center Division (#40.8)
- New Person (#200)
- Patient (#2)
- Ward Location (#42)

Also, the Electronic Signature fields in the New Person file (#200) are used by this package to verify reports.

### DBIAs

For the latest information on active supported references, use the Subscriber Package Menu under the DBA's Integration Agreement Menu on FORUM.

Select Software Services Primary Menu Option: DBA MENU

Select DBA MENU Option: integration CONTROL REGISTRATIONS

Select INTEGRATION CONTROL REGISTRATIONS Option: ?

HELP Instructions for Entering ICRs

GET# GET NEW Integration Control Registration #(s)

ADD ADD/EDIT Pending Integration Control Registration

ROLL Roll up ICR into Mail Message

FILE File-type Integration Control Registrations Menu ...

ROU Routine-type ICRs Menu ...

RPC Remote Procedure Call-type ICRs Menu ...

OTH Print 'Other'-type ICRs

SUPP Supported References Menu ...

CONT Controlled Subscription ICRs Menu ...

PRIV Private ICRs Menu ...

CUST Custodial Package Menu ...

INQ Inquire to an Integration Control Registration

SUBS Subscriber Package Menu ...

APIS Supported API Report

VBLE Lookup ICRs by Variable

PEND Print ICRs in Pending Status

ACTV Print Active ICRs

ALL Print ALL ICRs

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select INTEGRATION CONTROL REGISTRATIONS Option: SUBS Subscriber Package Menu

Select Subscriber Package Menu Option: ?

1  Print ACTIVE by Subscribing Package

2  Print ALL by Subscribing Package

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Subscriber Package Menu Option: 1 Print ACTIVE by Subscribing Package

* Previous selection: SUBSCRIBING PACKAGE equals INTEGRATED BILLING

START WITH SUBSCRIBING PACKAGE: INTEGRATED BILLING// RADIOLOGY/NUCLEAR MEDICINE

GO TO SUBSCRIBING PACKAGE: LAST// RADIOLOGY/NUCLEAR MEDICINE

DEVICE: (Enter a device)

## 20 Internal Relations

All options in the Radiology/Nuclear Medicine 5.0 package can function independently. Most options require the use of the following package-wide variables: RACCESS, RAMDV, RAMLC, RAMDIV and RAIMGTY. Descriptions of these variables can be found under Package-wide Variables and under Key Variables of the Implementation and Maintenance section of this manual.

If they do not already exist, these variables are set at the time the option is invoked. They are only killed by the exit action of the user's main Radiology/Nuclear Medicine menu (e.g., Rad/Nuc Med Transcriptionist Menu). If other options are invoked independently, these variables should be killed by adding 'D KILL^RAPSET1' to the exit action of the option.

## 21 Package-wide Variables

Table 14 - Package-Wide Variables

| NAME    | DESCRIPTION                                                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RACCESS | This array identifies the user's division, imaging location and imaging type access.                                                                          |
| RAIMGTY | This is the name of imaging type (File #79.2 entry) of the user based on the imaging location selected.                                                       |
| RAMDIV  | The internal entry number of the division (File #79) the user has signed-on to.                                                                               |
| RAMDV   | The division parameters for a File #79 entry. The parameters that make up this variable are identified in the Key Variables portion, page 23, of this manual. |
| RAMLC   | The imaging location parameters for a File #79.1 entry. The parameters that make up this variable are identified in the Key Variables portion of this manual. |

These variables are created or changed when the user selects a sign-on imaging location usually during the log-in process or in the Switch Locations option.

The variables are also set by the individual options if they do not already exist. The routine series RAPSET* sets these variables.

Example of when the package-wide variables are created or changed:

Please select a sign-on Imaging Location: X-RAY// &lt;RET&gt;   (GENERAL RADIOLOGY)

--------------------------------------------------------------------------

Welcome, you are signed on with the following parameters:

Printer Defaults

Version  : 5.0      ----------------

Division : HINES     Flash Card : RAD/NM FLASH CARDS

Location : X-RAY         1 card/exam

Img. Type: GENERAL RADIOLOGY  Jacket Label: RAD/NM JACKET LBLS

User  : RADUSER,ONE    1 labels/visit

Report  : RAD/NM REPORT PTR

--------------------------------------------------------------------------

These variables are killed when the user exits the package menu they logged in under. The variables are killed by calling KILL^RAPSET1.

## 22 How to Generate On-line Documentation

This section describes various methods by which users may generate Radiology/ Nuclear Medicine technical documentation.

### Build File Print

The Build File Print option, found under the KIDS Utilities menu, lists the complete definition of the package, including all files, components, install questions, and the environment, pre-install, and post-install routines

### Question Marks

Entering question marks at the "Select Option:" prompt provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option.

Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock (if applicable) for each.

Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for the option.

### XINDEX

This utility analyzes routines to determine if they adhere to VistA Programming Standards. The XINDEX output may include the following components: Compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Global References, Label References and External References.

To run XINDEX for the Radiology/Nuclear Medicine package, specify the following namespace at the "routine(s) ?&gt;" prompt: **RA*** .

RACT* routines are compiled template routines, which you may not wish to examine (i.e., - **RACT*** ).

**Note** : If you run an XINDEX  you may run into several errors caused by references to routines not in the development environment if the imaging package and/or OE/RR V. 3.0 (CPRS) are not yet installed or released. These errors are benign and do not affect the operation of the Radiology/Nuclear Medicine package.

Routines involved are:

MAGRIC	MAGSET3	ORMFN	ORXP		ORERR

### Inquire to File Entries

This option provides the following information about a specified option: option name, menu text, option description, type of option. All fields that have a value will be displayed (e.g., Entry Action).

To secure information about the Radiology/Nuclear Medicine options, the user must specify the name of the options desired (File #19). The options exported with this package begin with the letters RA.

### Print Options File

Use this option to generate ad hoc reports about options from the Option file (#19). The user may choose one, many or all Radiology/Nuclear Medicine options. The options exported with this package begin with the letters RA.

### List File Attributes

This option allows the user to generate documentation pertaining to files and file structure. The Radiology/Nuclear Medicine file numbers are 34 and 70-79.7. See the File List section page 41, of this manual for a specific listing.

Select the Standard format to get the following data dictionary information for a specified file: file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates and sort templates.

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-references, input transform, and date last edited.

Select the Global Map format to generate an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates and sort templates.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the *VistA Kernel Systems Manual* .

## 23 Glossary

Table 15 - Glosary Terms

| **TERM**                                                                 | **MEANING**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abdominal Aortic Aneurysm  (AAA)                                         | A weakness in the body’s main artery for that portion of the aorta located in the abdomen. If untreated, it can lead to serious internal bleeding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Active                                                                   | An order status that occurs when a request to perform a procedure on a patient has been registered as an exam, but before it has reached a status of Complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Activity log                                                             | A log of dates and times data was entered and/or changed. The Radiology/Nuclear Medicine system is capable of maintaining activity logs for reports, exam status changes, imaging type parameter changes, purge dates, outside film registry activity, and order status changes.                                                                                                                                                                                                                                                                                                                                     |
| Alert                                                                    | Alerts consist of information displayed to specific users triggered by an event. For example, alerts pertaining to Rad/Nuc Med include the Stat Imaging Request alert, an Imaging Results Amended alert, and an Abnormal Imaging Results alert. The purpose of an alert is to make a user aware that something has happened that may need attention. Refer to Kernel and CPRS documentation.                                                                                                                                                                                                                         |
| AMIS code                                                                | For imaging, one of 27 codes used to categorize procedures, calculate workload crediting, and weighted work units. AMIS codes are determined by VA Central Office and should not be changed at the medical centers.                                                                                                                                                                                                                                                                                                                                                                                                  |
| AMIS weight multiplier                                                   | A number associated with a procedure-AMIS code pair that is multiplied by the AMIS code weighted work units. If the multiplier is greater than 1, a single exam receives multiple exam credits.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Attending physician                                                      | The Radiology/Nuclear Medicine software obtains this data from the PIMS package, which is responsible for its entry and validity. Refer to PIMS documentation for more information and a description of the meaning of this term as it applies to VistA.                                                                                                                                                                                                                                                                                                                                                             |
| Batch                                                                    | In the Radiology/Nuclear Medicine system, a batch is a set of results reports. Transcriptionists may create batches to keep similar reports together and cause them to print together. One possible purpose might be to print all reports dictated by the same physician together.                                                                                                                                                                                                                                                                                                                                   |
| Bedsection                                                               | See PTF Bedsection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Bilateral                                                                | A special type of modifier that can be associated with an exam, a procedure, or an AMIS code. When an exam is bilateral due to one of the aforementioned associations, workload credit and exam counts are doubled for that exam on most workload and AMIS reports.                                                                                                                                                                                                                                                                                                                                                  |
| BI-RADS  **™**                                                           | Breast Imaging Reporting and Data System: A system created by the American College of Radiology (ACR) to standardize assessment and categorization of breast imaging results and reports.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Broad procedure                                                          | A non-specific procedure that is useful for ordering when the ordering party is not familiar enough with imaging procedures to be able to specify the exact procedure that is to be performed. Before an exam status can progress to Complete, the imaging service must determine a more specific procedure and change the exam procedure to reflect the actual Detailed or Series procedure done. Depending on site parameters, broad procedures may or may not be used at a given facility. Also see Detailed and Series procedure.                                                                                |
| Bulletin                                                                 | A special type of mail message that is computer-generated and sent to a designated user or members of a mail group. Bulletins are usually created to inform someone of an event triggered by another user's data entry, or exam and request updates that require some action on the part of the bulletin recipient.                                                                                                                                                                                                                                                                                                  |
| Camera/Equipment/Room                                                    | The specific room or piece of equipment used for a patient's imaging exam. Each is associated with one or more imaging locations. The Radiology/Nuclear Medicine system supports, but does not require users to record the camera/equipment/room used for each exam.                                                                                                                                                                                                                                                                                                                                                 |
| Cancelled                                                                | A general status that can be associated with a radiology exam or order. A radiology order is cancelled when the order is rejected on the CPRS side. It is important to note that history shows that ‘discontinued’ and ‘cancelled’ were used synonymously when discussing the status of a CPRS or Radiology order prior to the release of RA*5.0*169. Post patch 169 ‘discontinued’ and ‘cancelled’ have distinct meanings.                                                                                                                                                                                          |
| Case number                                                              | A computer-generated number assigned to the record generated when one patient is registered for one procedure at a given date/time.  When multiple procedures are registered for a patient at the same date/time, each procedure will be given a different case number. Case numbers will be recycled and reused by a new patient/procedure/date instance when the exam attains a Complete status.                                                                                                                                                                                                                   |
| Category of exam                                                         | For the purposes of this system, category of exam must be Outpatient, Inpatient, Contract, Sharing, Employee, or Research. Several workload and statistical reports print exam counts by category. Others use the category to determine whether exams should be included on the report.                                                                                                                                                                                                                                                                                                                              |
| Clinic                                                                   | Hospital locations where outpatients are cared for. In VistA, clinics are represented by entries in the Hospital Location file (#44). Radiology/Nuclear Medicine Imaging Locations, represented by entries in the Imaging Location file (#79.1), are a subset of the Hospital Location file.                                                                                                                                                                                                                                                                                                                         |
| Clinical history                                                         | Data entered in the Radiology/Nuclear Medicine system during exam ordering and exam edit. Usually entered by the requesting party to inform the imaging service why the exam needs to be done and what they hope to find out by doing the exam.                                                                                                                                                                                                                                                                                                                                                                      |
| Clinical history message                                                 | Text that, if entered in system parameter setup, will always display when the user is prompted for clinical history. Generally used to instruct the user on what they should enter for clinical history.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Common Procedure                                                         | A frequently ordered procedure that will appear on the order screen. Up to 40 per imaging type are allowed by the system. Other active Rad/Nuc Med procedures are selectable for ordering, but only the ones designated as common procedures and given a display sequence number will be displayed prior to selection.                                                                                                                                                                                                                                                                                               |
| Complete                                                                 | A status that can be attained by an order or an exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Complication                                                             | A problem that occurs during or resulting from an exam, commonly a contrast medium reaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Contract                                                                 | A possible category of exam when imaging services are contracted out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Contrast medium                                                          | A radio-opaque injectable or ingestible substance that appears on radiographic images and is helpful in image interpretation. It is used in many imaging procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Contrast reaction message                                                | A warning message that will display when a patient who has had a previous contrast medium reaction is registered for a procedure that uses contrast media. The message text is entered during Rad/Nuc Med division parameter setup.                                                                                                                                                                                                                                                                                                                                                                                  |
| CPT code                                                                 | See Current Procedural Terminology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Credit stop code                                                         | See Stop Code. Also see PIMS documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Current Procedural Terminology (CPT)                                     | A set of codes published annually by the American Medical Association which include Radiology/Nuclear Medicine procedures. Each active detailed or series procedure must be assigned a valid, active CPT code to facilitate proper workload crediting. In VistA, CPT's are represented by entries in the CPT file #81.                                                                                                                                                                                                                                                                                               |
| **Deleted (X)**                                                          | A report status that refers to a report deleted from a case but remains in the database. The deleted report status is seen on the Report Activity Log after the deleted report is restored. A deleted report is not viewable from any Radiology options.                                                                                                                                                                                                                                                                                                                                                             |
| Descendent                                                               | A type of Rad/Nuc Med procedure. One of several associated with a 'Parent' type of procedure. The descendent procedures are actually registered and performed. Also see Parent.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Desired date (of an order)                                               | The date the ordering party would like for the exam to be performed. Not an appointment date. The imaging service is at liberty to change the date depending on their availability.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Detailed procedure                                                       | A procedure that represents the exact exam performed, and is associated with a CPT code and an AMIS code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Diagnostic code                                                          | Represented, for the purposes of this system, by entries in the Diagnostic Codes file (#78.3). Diagnostic codes describe the outcome of an exam, such as normal, abnormal. A case may be given one or more (or no) diagnostic code(s).                                                                                                                                                                                                                                                                                                                                                                               |
| Discontinued                                                             | An order status that occurs when a user cancels an order. CPRS’ order field and the Radiology order request status get updated to ‘Discontinued’.  Post patch RA*5.0*169 ‘Discontinued’ and ‘Cancelled’ have distinct meanings.                                                                                                                                                                                                                                                                                                                                                                                      |
| Distribution queue                                                       | A mechanism within the Radiology/Nuclear Medicine system that facilitates printing results reports at various hospital locations, such as the patient's current ward or clinic, the file room, and medical records.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Division, Rad/Nuc Med                                                    | A subset of the VistA Institution file (#4). Multi-divisional sites are usually sites responsible for imaging at more than one facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Draft                                                                    | A report status that is assigned to all Rad/Nuc Med results reports as soon as they are initially entered into the system, but before they are changed to a status of Verified or (if allowed) Released/Not Verified.                                                                                                                                                                                                                                                                                                                                                                                                |
| DSS ID                                                                   | Formerly Stop Code associated with each procedure, now DSS ID associated with each Imaging Location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Electronic signature code                                                | A security code that the user must enter to identify him/herself to the system. This is required before the user is allowed to electronically verify Rad/Nuc Med reports. This is not the same as the Access/Verify codes.                                                                                                                                                                                                                                                                                                                                                                                           |
| **Electronically Filed (EF)**                                            | A report status that refers to a report interpreted outside the Rad/Nuc Med Department. The content is not the actual interpreted report, but canned or manually entered text referring to the outside interpreted report.                                                                                                                                                                                                                                                                                                                                                                                           |
| Exam label                                                               | One of 3 types of labels that can be printed at the time exam registration is done for a patient. Also see jacket label, flash card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Exam set                                                                 | An exam set contains a Parent procedure and its Detailed or Series descendent procedures. Requesting a Parent will automatically cause each descendent to be presented for registration as separate cases under a single visit date and time.                                                                                                                                                                                                                                                                                                                                                                        |
| Exam status                                                              | The state of an exam that describes its level of progress. Valid exam statuses are represented in this system by entries in the Examination Status file (#72). Examples are ordered, cancelled, complete, waiting for exam, called for exam, and transcribed. The valid set of exam statuses can, to a degree, be tailored by the site. There are many parameters controlling required data fields, status tracking and report contents that are determined when the parameters of this file are set up. There are separate and different set of statuses for requests and reports.                                  |
| Exam status parameter setup                                              | See Exam status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Exam status time                                                         | The date/time when an exam's status changes, triggered by exam data entry that can be done through over a dozen different options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Film size                                                                | Represented by entries in the Film Sizes file (#78.4) in this system. Used to facilitate film use/waste tracking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Flash card                                                               | One of 3 labels that can be generated at the time an exam is registered for a patient. The flash card was named because it can be photographed along with an x-ray, and its image will appear on the finished x-ray. Helpful in marking x-ray images with the patient's name, SSN, etc. to insure that x-rays are not mixed up.                                                                                                                                                                                                                                                                                      |
| Footer                                                                   | The last lines of the results report, the format of which can be specified using the Label/Header/Footer Formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Format                                                                   | The specification for print locations of fields on a printed page. In this system, print formats can be specified using the Label/Header/Footer Formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Header                                                                   | The top lines of the results report, the format of which can be specified using the Label/Header/Footer Formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Health Summary                                                           | Refers to a report or VistA software package that produces a report showing historical patient data. Can be configured to meet various requirements. Refer to the Health Summary documentation for more information.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Hold                                                                     | An order status occurring when a users puts an order on hold, indicating that a study should not yet be done or scheduled, but that it will likely be needed in the future.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Hospital location                                                        | Represented in VistA by entries in the Hospital Location file (#44). Rad/Nuc Med locations are a subset of the Hospital Location file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Imaging location                                                         | One of a subset of Hospital Locations (See Hospital location) that is represented in the Imaging Location file #79.1, and is a location where imaging exams are performed.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Imaging type                                                             | For the Rad/Nuc Med software, the set of valid imaging types is:  - ANGIO/NEURO/INTERVENTIONAL - GENERAL RADIOLOGY - MAMMOGRAPHY - NUCLEAR MEDICINE - ULTRASOUND - VASCULAR LAB - CARDIOLOGY STUDIES (NUC MED) - CT SCAN - MAGNETIC RESONANCE IMAGING  These are the imaging types that are supported by this version of the software. Each imaging location and procedure may be associated with only one imaging type.                                                                                                                                                                                             |
| Impression                                                               | A short description or summary of a patient's exam results report. Usually mandatory data to complete an exam. The impression is not purged from older reports even though the lengthier report text is.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Inactivate                                                               | The process of making a record in a file inactive, usually by entering an inactive date on that record or deleting a field that is necessary to keep it active. When a record is inactive, it becomes essentially "invisible" to users. Procedures, common procedures, modifiers, and exam statuses can be inactivated.                                                                                                                                                                                                                                                                                              |
| Inactivation date                                                        | A date entered on a record to make it inactive. See Inactivate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Information Resources Management                                         | The service within VA hospitals that supports the installation, maintenance, troubleshooting, and sometimes local modification of VistA software packages and the hardware that they run on.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Interpreting physician  (also Interpreting Resident, Interpreting Staff) | The resident or staff physician who interprets exam images.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IRM                                                                      | See Information Resources Management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Jacket label                                                             | One of the 3 types of labels that can be generated at the time an exam is registered for a patient. Usually affixed to the x-ray film jacket. (See also exam label, flash card.)                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Key                                                                      | See security key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Label print fields                                                       | Fields that are selectable for printing on a label, report header, or report footer on formats that are designed using the Label/Header/Footer Formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Label/Header/Footer Formatter                                            | The name given to the option/mechanism that allows users to define formats for labels and for headers and footers on results reports. Users can specify which fields to print at various columns and lines on the label or report header/footer.                                                                                                                                                                                                                                                                                                                                                                     |
| LOINC                                                                    | Logical Observation Identifiers Names and Codes (LOINC) is a database and universal standard for identifying medical laboratory observations. LOINC Codes exist within File 71.99 for the purposes of interoperability and standardization.                                                                                                                                                                                                                                                                                                                                                                          |
| Mode of transport                                                        | The patient's method of moving within the hospital, (ambulatory, wheelchair, portable, stretcher) designated at the exam is ordered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Modifier                                                                 | Additional information about the characteristics of an exam or procedure (such as bilateral, operating room, portable, left, right). Also see bilateral, operating room, portable.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| No purge indicator                                                       | A flag that can be set on the exam record to force the purge process to bypass the record. Guarantees that the record will not be purged when a historic data purge is scheduled by IRM. Also see Purge. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] & ‘Indicate No Purging of an Exam/report’ [RA PURGE] options.                                                                                                                                                                                                                                                                   |
| Non-credit stop code                                                     | Certain stop codes, usually for health screening, that do not count toward workload credit. If a non-credit stop code is assigned to a procedure, another credit stop code must also be assigned. Also see Stop code.                                                                                                                                                                                                                                                                                                                                                                                                |
| On-line verification                                                     | The option within the Radiology/Nuclear Medicine package that allows physicians to review, modify, and electronically sign patient result reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Operating room                                                           | A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Operating Room.                                                                                                                                                                                                                                                                                                                                                                                    |
| Order                                                                    | The paper or electronic request for an imaging exam to be performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Order Entry                                                              | The process of requesting that one or more exams be performed for a patient. Order entry for Radiology / Nuclear Medicine procedures can be accomplished through a Rad/Nuc Med software option or through a separate VistA package, CPRS.                                                                                                                                                                                                                                                                                                                                                                            |
| Order Entry/Results Reporting                                            | A VistA package that performs that functions of ordering for many clinical packages, including Radiology/Nuclear Medicine. This package has been replaced by CPRS.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Outside films registry                                                   | A mechanism in this system that allows users to track films done outside of the medical center. This can also be accomplished through the VistA Record Tracking package. Refer to Record Tracking documentation for more information.                                                                                                                                                                                                                                                                                                                                                                                |
| Parent procedure                                                         | A type of Rad/Nuc Med procedure that is used for ordering purposes. It must be associated with Descendent procedures that are of procedure type Detailed and/or Series.  At the time of registration the descendent procedures are actually registered. Setting up a parent procedure provides a convenient way to order multiple related procedures on one order.  Parent/descendent procedure relationships must be set up ahead of time during system definition and file tailoring by the ADPAC.                                                                                                                 |
| Pending                                                                  | An order status that every Rad/Nuc Med order is placed in as soon as it is ordered through this system's ordering option. This system also receives orders from CPRS and places them in a pending status.                                                                                                                                                                                                                                                                                                                                                                                                            |
| **PFSS / Patient Financial Services System**                             | The PFSS project will prepare the VistA environment for implementation of a commercial off-the-shelf (COTS) billing replacement system.  The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system.                                                                                                                                                                                                                                                                     |
| **PFSS Account Reference**                                               | A PFSS reference to the Account Number entry (external billing visit number) in the VistA Integrated Billing subsystem (IBB) account file. Other VistA applications use this to point to the account number in IBB.                                                                                                                                                                                                                                                                                                                                                                                                  |
| PFSS Department Code                                                     | A 3-character numeric code representing the  Department Code for Radiology used by PFSS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Portable                                                                 | A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Portable.                                                                                                                                                                                                                                                                                                                                                                                          |
| Pre-verification                                                         | The process whereby a resident reviews a report and affixes his/her electronic signature to indicate that the report is ready for staff (attending) review, facilitated through an option in this system for Resident Pre-verification.                                                                                                                                                                                                                                                                                                                                                                              |
| Primary Interpreting Staff/ Resident                                     | The attending or resident primarily responsible for the interpretation of the case. (See also Secondary Interpreting Staff/Resident.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Primary physician                                                        | The Radiology/Nuclear Medicine software obtains this data from PIMS, which is responsible for its entry and validity. Refer to the PIMS documentation for more information and a description of the meaning of this term as it applies to VistA.                                                                                                                                                                                                                                                                                                                                                                     |
| Principal clinic                                                         | For the purposes of the Radiology/Nuclear Medicine system, this term is usually synonymous with 'referring clinic'. However, for the purposes of crediting, it is defined as the DSS (clinic/stop) code that is associated with the imaging location where the exam was performed.                                                                                                                                                                                                                                                                                                                                   |
| Printset                                                                 | A printset contains a Parent procedure and its Detailed or Series descendent procedures. If the parent is defined to be a printset, the collection and printing of all common report related data between the descendents is seen as one entity.                                                                                                                                                                                                                                                                                                                                                                     |
| Problem draft                                                            | A report status that occurs when a physician identifies a results report as having unresolved problems, and designates the status to be Problem Draft. Depending on site parameters, a report may be designated as a Problem Draft due to lack of an impression. Also see Problem statement.                                                                                                                                                                                                                                                                                                                         |
| Problem statement                                                        | When a results report is in the Problem Draft status, the physician or transcriptionist is required to enter a brief statement of the problem. This problem statement appears on report displays and printouts.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Procedure                                                                | For the purposes of this system, a medical procedure done with imaging technology for diagnostic purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Procedure message                                                        | Represented in this system by entries in the Rad/Nuc Med Procedure Message file (#71.4). If one or more procedure messages are associated with a procedure, the text of the messages will be displayed when the procedures is ordered, registered, and printed on the request form.  Useful in alerting ordering clinicians and imaging personnel of special precautions, procedures, or requirements of a given procedure.                                                                                                                                                                                          |
| **Procedure type**                                                       | A characteristic of a Rad/Nuc Med procedure that affects exam processing and workload crediting. See Detailed, Series, Broad, and Parent.  Also used in Outpatient Procedure Wait Time reports to standardize the reporting of performance monitors throughout VA. Procedure Type categories have been assigned by the Office of Patient Care Services.                                                                                                                                                                                                                                                              |
| PTF Bedsection                                                           | See PIMS documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Purge                                                                    | The process that is scheduled at some interval by IRM to purge historic computer data. In this system, purges are done on results report text, orders, activity logs, and clinical history. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] & ‘Indicate No Purging of an Exam/report’ [RA PURGE] options.                                                                                                                                                                                                                                                                                |
| Registration (of an exam)                                                | The process of creating a computer record for one or more patient/procedure/visit date-time instances. Usually done when the patient arrives at the imaging service for an exam.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Relative Value Unit (RVU)**                                            | This is a "unit of work" assigned to a CPT code. RVUs are based on the cost of providing a particular service to a patient and are broken down into three components: the Work RVU is the provider time, the Practice Expense RVU is what that time is costing in overhead, and the Malpractice RVU is the liability cost (likelihood of complications).  Each RVU is a weight based on complexity, and is used as a multiplier to calculate Medicare and other fee schedules.                                                                                                                                       |
| Released/not verified                                                    | A results report status that may or may not be implemented at a given medical center. Reports in this status may be viewed or printed by hospital staff outside of the imaging service.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Report batch                                                             | See Batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Report status**                                                        | The state of a report that describes its progress level. Valid report statuses in this system are Draft, Problem Draft, Released/Not Verified (if the site allows this status), Verified, Electronically Filed, and Deleted.  The status of a report may affect the status of an exam. Also see Exam status. Exams and requests each have a separate and different set of statuses.                                                                                                                                                                                                                                  |
| Request                                                                  | Synonymous with order. See Order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Request status                                                           | The state of a request (order) that describes its progress level. Valid request statuses in this system are Unreleased(only if created through CPRS), Pending, Hold, Scheduled, Active, Discontinued, Cancelled and Complete.  Reports and exams each have a separate and different set of statuses.                                                                                                                                                                                                                                                                                                                 |
| Request urgency                                                          | Data entered at the time an exam is ordered to describe the priority/criticality of completing the exam quickly (i.e. Stat, Urgent, Routine).                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Requesting location                                                      | Usually the location where the patient was last seen or treated (an inpatient's ward, or an outpatient's clinic). All requesting locations are represented by an entry in the VistA Hospital Location file (#44).  The requesting location may be, but is usually not an imaging location.                                                                                                                                                                                                                                                                                                                           |
| Requesting physician                                                     | The physician who requested the exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Research source                                                          | A research project or institution that refers a patient for a Radiology/Nuclear Medicine exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Scheduled                                                                | An order status that occurs when imaging personnel enter a date when the exam is expected to be performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Secondary Interpreting Staff/Resident                                    | This generally refers to an attending/resident who assisted or sat in on review of the case, but is not primarily responsible for it.  It may also be used to indicate a second reviewer of the case, for quality control or peer review purposes.                                                                                                                                                                                                                                                                                                                                                                   |
| Security key                                                             | Represented by an entry in the VistA Security Key file. Radiology/Nuclear Medicine keys include RA MGR, RA ALLOC, RA UNVERIFY, RA VERIFY and RA SWITCHLOC. Various options and functions within options require that the user "own" a security key.                                                                                                                                                                                                                                                                                                                                                                  |
| Site Specific Accession Number (SSAN)                                    | This is a case number with the 3-digit Site ID and the Date appended at the beginning of it in the format of ‘SSS-MMDDYY-CASE#’.  An example is 141-052709-23457, where 141 is the site ID, 052709 is the date and 23457 is the case number.  (see also, Case Number above)                                                                                                                                                                                                                                                                                                                                          |
| Staff                                                                    | Imaging Attending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Staff review (of reports)                                                | The requirement where an attending imaging physician is required to review the reports written by a resident imaging physician.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Standard report                                                          | Represented in this system by entries in the Standard Reports file (#74.1). Standard reports can be created by the ADPAC during system definition and set-up. If the division setup specifies that they are allowed, transcriptionists will be offered a selection of standard report text and impressions to minimize data entry effort.                                                                                                                                                                                                                                                                            |
| Status tracking                                                          | The mechanism within this system that facilitates exam tracking from initial states to the complete state. ADPACs must specify during exam status parameter setup which statuses will be used, which data fields will be required to progress to each status, which data fields will be prompted, and exams of which statuses will be included on various management reports.                                                                                                                                                                                                                                        |
| Stop code                                                                | Member of a coding system designed by VA Central Office to aid in determining workload and reimbursement of the medical centers. Stop codes are controlled by VA Central Office. The set of valid stop codes is revised October 1 of each year.  At this time, the PIMS developers issue a maintenance patch to the Vist  *A*  software updating the file containing stop codes. Imaging stop codes are represented by entries in the Valid Imaging Stop Code file #71.5.  Imaging stop codes are a subset of the Vist  *A*  Clinic Stop file #40.7. See PIMS documentation for more information. (Also see DSS ID.) |
| Synonym                                                                  | In the Radiology/Nuclear Medicine package, synonyms are alternate terms that can be associated with procedures for the purposes of convenient look-up/retrieval.  A given procedure may have more than one synonym, and a given synonym may be used for more than one procedure.                                                                                                                                                                                                                                                                                                                                     |
| Technologist                                                             | Radiology/Nuclear Medicine personnel who usually are responsible for performing imaging exams and entering exam data into the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Time-out                                                                 | The amount of time allowed before a user is automatically logged out of the system if no keystrokes are entered. This is a security feature, to help prevent unauthorized users from accessing your VistA account in case you forget to log off the system or leave your terminal unattended.                                                                                                                                                                                                                                                                                                                        |
| Transcribed                                                              | An exam status that may occur when a results report is initially entered into the system for an exam. If this status is not activated at the site, it will not occur.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Unreleased                                                               | An order status that occurs when an exam order is created, but no authorization to carry out the order has been given. This is possible only if the order is created through the PIMS software.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Verification                                                             | For the purposes of this system, the process of causing a results report to progress to the status of Verified. This happens when a physician affixes his/her electronic signature to the report, or when a transcriptionist, with the proper authorization, enters the name of a physician who has reviewed and approved a report.  This is analogous to a physician signing a paper report.  **Verification Timeliness reports are available to show the amount of time elapsed between registration of an exam and its transcription and/or verification.**                                                       |
| Verified                                                                 | A results report status that occurs at the time of verification. A report is verified when the interpreting physician electronically signs the report or gives his/her authorization that the report is complete and correct. Also see Verification.                                                                                                                                                                                                                                                                                                                                                                 |
| VistA                                                                    | Veterans Health Information Systems and Technology Architecture. Formerly known as DHCP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VUID                                                                     | Veterans Health Administration Unique Identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Waiting for exam                                                         | An exam status that occurs as soon as the exam is first registered. The system automatically places all exams in this status upon registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ward                                                                     | The hospital location where an inpatient resides. In VistA, wards are a subset of the Hospital Location file (#44).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Weighted work unit                                                       | The number that results from multiplying the weight of a procedure's AMIS code with the procedure's AMIS weight multiplier for that AMIS code.  If a procedure has more than one AMIS code, the multiplication is done for each and the results are summed.                                                                                                                                                                                                                                                                                                                                                          |
| **Work Relative Value Unit (wRVU)**                                      | The work RVU correlates time, intensity, and difficulty of service. For example, a service with a work RVU of "2" would be considered to involve twice as much physician work as a service with a work RVU of "1".                                                                                                                                                                                                                                                                                                                                                                                                   |
| Workload credit                                                          | A general term that refers to the CPT type of workload credit that is used in the VA to calculate reimbursement to medical centers for work done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |


**SOFTWARE AND DOCUMENTATION NOTES**

RADIOLOGY/NUCLEAR MEDICINE TECHNICAL MANUAL VERSION 6.0 contains the Rad/Nuc Med Patch RA*5.0*113 and RA*5.0*116. These manuals are available in MS Word (.doc) format and the Portable Document Format (.pdf) on the VA Software Documentation Library in the Clinical Section http://www4.va.gov/vdl/

RADIOLOGY / NUCLEAR MEDICINE USER MANUAL VERSION 6.0 contains the Rad/Nuc Med Patch RA*5.0*113 and RA*5.0*116 software and documentation files and it is available in MS Word (.doc) format and the Portable Document Format (.pdf) on the VA Software Documentation Library in the Clinical Section [http://www4.va.gov/vdl/](http://www4.va.gov/vdl/)

To download these files the preferred method is to FTP the files from ftp://download.vista.med.va.gov/. This transmits the files from the first available FTP server.

**PATCHES**

Table 16 - Patches

<!-- rpc-table -->
| **Patch RA*5.0*113**  The Patient Specific Radiation Dose Aggregation patch collects patient radiation information and how many Rankin’s study patients were exposed to  Patient Radiation dose data is available in two report options; Exam Profile with Radiation Dosage Data and a Radiation Dose Summary Report.  The Radiation Dose Summary Report lists completed exams performed within the selected date range for which dose data has been collected. Users must select the type of report format and which filters should apply.  Studies for which dose parameters are captured are currently limited to Computed Tomography and Fluoroscopy. These two modalities are directly related to the CT Scan and General Radiology imaging type records found in the IMAGING TYPE (#79.2) file.  The data returned from the application program interface (API) will be filed in the new RADIATION ABSORBED DOSE (#70.3) file. As long as the study exists and is tied to an active radiation dose record, the radiation dose data will be available to radiology users in the form of report options.  Exported in this patch are new options:  Exam Profile with Radiation Dosage Data - RA PROFRAD DOSE allows the user to select the type of report and the filters applied to the report.  Radiation Dose Summary Report - RA RAD DOSE SUMMARY behaves just as the current patient profile options but the reports may be printed.  When an exam is deleted using the 'Exam Deletion' RA DELETEXAM option, all radiation dosage information associated with that study will be deleted in the RADIATION ABSORBED DOSE file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Patch RA*5.0*116**  The VistA Imaging Importer III (for the Radiology Information System Support (RIS)), is a DICOM Image Gateway application for transfering DICOM objects from PAC studies performed outside of the VA, into VistA Imaging.  DICOM objects may be electronically transferred or directly from portable media (such as CDs, DVDs, Flash Drives). Portable media must conform to:  •	DICOM Standards  •	IHE Portable Data for Imaging PDI profiles  CDs and DVDs saved in proprietary formats usually cannot be transferred by (and used) by VistA Imaging nor can saved Report files (future release).  The VistA Imaging Importer III can correct patient and/or study identification information mismatchs previously processed by older utility software.  Diagnostic codes may be used to generate alerts to the requesting clinician whenever an examination has an abnormal result.  Exported Components (ex-routines), Component Type  RAMAG EXAM COMPLETE, Remote Procedure Call (RPC)   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Patch RA*5.0*127**  The Department of Veterans Affairs (VA) Interagency Program Office (IPO)and the Department of Defense (DoD) is tasked by its charter withleading the Departments’ efforts “to implement national health datastandards for interoperability and [be] responsible for establishing,monitoring, and approving the clinical and technical standards profileand processes to ensure a seamless [exchange] of health data.” This task of Native Domain standardization is aligned with achieving the goalsoutlined in the 2014 National Defense Authorization Act (NDAA) requiringthat the Departments’ “healthcare data [are] computable in real-time and[comply] with existing national data standards” and that the “data [are]standardized as national standards continue to evolve.”  VA clinicians historically used non-standardized clinical terminologies which are inconsistent within the VA user community as well as within the currently accepted data standards as established by Office of the National Coordinator for Health Information Technology (ONC). Implementation of Native Standardization will allow a streamlined method for data sharing, performing clinical decision support and engaging in national data reporting and analysis. The VA has recently established a process for implementing standard terminology/terminologies within individual clinical domains for the exchange of data. The intent of this effort is to provide the detailed groundwork necessary for industry-wide interoperability. By providing a detailed analysis of the current state of the applicable domains and recommendations regarding the path forward, the Native Domain Standardization supports VA’s efforts toremain at the forefront of healthcare data exchange.  The system will include the addition of a new field to the RAD/NUC MED PROCEDURE file (#71) and creation of the Master Radiology Procedure File (MRPF) Gold File (#71.99).  The local facility Automated Data Processing Application Coordinator (ADPAC) will need to associate the local procedure names in file #71 to Gold Names in file #71.99.  It will be necessary to develop a national standard of radiology procedures and map to their respective Current Procedural Terminology (CPT) code and Logical Observation Identifiers Names and Codes (LOINC) will be populated under the direction of the VHA Radiology Program Office prior to implementation of any of the data within these files. The objective of this process is to enable the most user friendly interface as possible in the implementation of the native standardization along with all of the activities required to operationalize the change within the VistA environment and the associated terminology consuming applications. The Radiology ADPAC will match each active entry in the RAD/NUC MED PROCEDURES file (# 71) to an entry in the MASTER RADIOLOGY PROCEDURES file (#71.99) (MRPF). This is all that is required outside the normal day-to-day operations. When a new procedure is entered into the RAD/NUC MED PROCEDURES file (# 71) an email is automatically sent to the NEW TERMINOLOGY RAPID TURNAROUND (NTRT) team for the creation of a new entry in the MRPF. The results of the NTRT process will be one of three possible results. 1) A new entry will be created in the MRPF and will be in he next file release. 2) A match was found in the MRPF and the facility should use that entry for a match. 3) There is no LOINC that matches this procedure and a request for a new LOINC has been submitted.  An On Demand report is available to the VHA Radiology Program Office that will allow them to monitor new procedure creation activity. A bulletin will be sent to a local mail group, the VHA Radiology Program Office, and NTRT whan a new procedure reaches a specified number of days from creation and it has not been matched to a MASTER RADIOLOGY PROCEDURES file (# 71.99) entry. While the MASTER RADIOLOGY PROCEDURES file (# 71.99) is locked down and cannot be changed at the local facility, the RAD/NUC MED PROCEDURES file (# 71) will remain accessable to the local facility. |   |