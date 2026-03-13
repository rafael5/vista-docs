---
app_name: Mental Health (YS)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: YS
patch: 191
patch_gap: null
section: ''
source_file: ys_mha_tm.docx
status: draft
title: ys mha tm.docx
---

**Mental Health**

**And**

**Mental Health Assistant Version 3**

<!-- image -->

**Technical Manual/Security Guide**

**Version 2.5**

**March 2012**

**Revised September 2021**

**Department of Veterans Affairs**

**Office of Information and Technology (OIT)**

**Product Development**

**Revision History**

| **Date**     |   **Version** | **Change**                                                                                                                                                                                       | **Project Manager**   | **Technical Writer**                |
|--------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------|
| Sept. 2021   |           2.5 | Patch YS*5.01*191: Informational patch for redactions and 508 comp.                                                                                                                              | CPRS Dev. Team        | CPRS Dev. Team                      |
| May 2021     |           2.4 | Patch YS*5.01*170: Updated the OPTION file (#19) entry in the Mental Health Remote Procedure Context Option section.  Made the “Routines Deleted by Mental Health Patch 60” table more readable. | CPRS Development Team | CPRS Development Team               |
| Dec. 2020    |           2.3 | Updated dates                                                                                                                                                                                    | REDACTED              | Liberty IT Solutions  HI&amp;M Team |
| Nov. 2020    |           2.2 | Revised for grammar and spelling errors                                                                                                                                                          | VA                    | REDACTED                            |
| Nov. 2020    |           2.1 | Updated version for patch 149. Added Appendix B. Updated Remote Systems, Transmission Options, File Manager Access Codes, and sections and footers.                                              | REDACTED              | Liberty IT Solutions  HI&amp;M Team |
| August 2020  |           2   | Updated version for patch 166. Added DBIA #4480 to Mental Health File Relationships table.                                                                                                       | REDACTED              | Liberty ITS HI&M Project Team       |
| March 2020   |           1.9 | Updated version for Patch 150                                                                                                                                                                    | REDACTED              | Booz Allen SPP Project Team         |
| June 2019    |           1.8 | Updated version for Patch 145                                                                                                                                                                    | REDACTED              | Booz Allen SPP Project Team         |
| May 2019     |           1.7 | Updated version for Patch 147                                                                                                                                                                    | REDACTED              | Booz Allen SPP Project Team         |
| Feb. 2019    |           1.6 | Updated version for Patches 138, 139                                                                                                                                                             | REDACTED              | Booz Allen SPP Project Team         |
| Sept. 2018   |           1.5 | Updated version for Patch 136                                                                                                                                                                    | REDACTED              | Booz Allen SPP Project Team         |
| August 2018  |           1.4 | Updated version numbers for Patch 134                                                                                                                                                            | REDACTED              | Booz Allen SPP Project Team         |
| March 2018   |           1.3 | Updated Title and Footers;                                                                                                                                                                       | REDACTED              | Booz Allen SPP Project Team         |
| August 2014  |           1.2 | Updated Title page  Updated Revision  History, p. i-ii  Updated Table of  Contents, pp. iii-iv  Changed ICD9 reference to ICD on page 19.                                                        | REDACTED              | REDACTED                            |
| 29 Feb. 2012 |           1.1 | Added table “MHA3 Patch YS*5.01*129 exports the following folders and files” to page 14                                                                                                          | REDACTED              | MHE-OM  Developer Team              |
| 13 Feb. 2012 |           1   | Removed “YS GAF Score Sent” from the mail group list. Final version. Peer review done and accepted                                                                                               | MHE-OM Team           | REDACTED                            |
| 6 Feb. 2012  |           0.4 | Uploaded to VA SharePoint for peer review                                                                                                                                                        | REDACTED              | REDACTED                            |
| 2 Feb. 2012  |           0.4 | Content from Security Guide incorporated into document. Document renamed to reflect change.                                                                                                      | REDACTED              | MHE Developer Team                  |
| 23 Jan. 2012 |           0.3 | Updated by developers. Obsolete content deleted.                                                                                                                                                 | REDACTED              | MHE Developer Team                  |
| 7 Jan. 2012  |           0.2 | Format Changes                                                                                                                                                                                   | REDACTED              | REDACTED                            |
| 7-Jul-11     |           0.1 | Initial Draft                                                                                                                                                                                    | REDACTED              | MHE-OM Team                         |

(This page included for double-sided copying)

**Table of Contents**

Introduction	7

Overview	7

Software and Manual Retrieval	7

VistA Intranet	8

Screen Displays	8

Implementation &amp; Maintenance	8

Minimum Requirements	8

Routines and Checksums	9

Routine Descriptions	10

Files	10

File Descriptions	13

VA File Manager Access Codes	13

Pointer Relations	14

Exported Options	14

Mental Health Menu Distributions	15

Transmission Options [YSCL HL7 MAIN]	15

Clinical Record [YSCLINRECORD]	16

Seclusion/Restraint [YSSR SEC/RES]	16

Seclusion/Restraint Report Utilities [YSSR REPORTS]	17

Global Assessment of Functioning	17

MHS Manager	17

Mental Health System Site Parameters	17

MHA2 Psych Test Utilities	18

Seclusion/Restraint Management Utilities	18

MHA3 Utilities	18

Menu Diagrams	18

Mental Health Protocols (File #101)	19

Remote Procedure Calls	19

Database Integration Agreements	19

External Relations	19

Non-M Software Distributed with Mental Health Assistant 3 (MHA3)	20

MHA3 Server Options	21

Remote Systems	21

Mental Health File Relationships	23

Mental Health Mail Group File (#3.8) Entries	25

Archiving	26

Package Security	26

Security Keys (File #19.1)	26

Glossary	27

Abbreviations, Acronyms, and Descriptions	30

Appendix A	32

Files Deleted by Mental Health Patch 60	32

Options Deleted by Mental Health Patch 60	32

Routines Deleted by Mental Health Patch 60	34

Appendix B	35

NCCC HL7 Message Specification	35

Conventions	35

HL7 Messages	35

Date/Time of Message Format	35

Message and Segment Boundaries	35

Segment Tables	35

Message Notations	36

Network Connections	36

NCR Patient Registration Message: ADT^A28	36

NCR Patient Registration MSH Segment	37

NCR Patient Registration EVN Segment	39

NCR Patient Registration PID Segment	40

NCR Patient Registration ROL Segment	44

NCR Patient Registration PV1 Segment	46

NCR Patient Registration OBX(1) Segment	48

NCR Patient Registration OBX(2) Segment	50

NCR Patient Registration OBX(3) Segment	52

NCR Patient Registration OBX(4) Segment	54

NCR Patient Registration OBX(5) Segment	56

NCR Patient Registration OBX(6) Segment	57

NCR Clozapine Dispense Message: RDE^O11	61

NCR Clozapine Dispense MSH Segment	61

NCR Clozapine Dispense PID Segment	63

NCR Clozapine Dispense PV1 Segment	67

NCR Clozapine Dispense ORC Segment	69

NCR Clozapine Dispense RXE Segment	72

NCR Clozapine Dispense TQ1 Segment	77

NCR Clozapine Dispense RXR Segment	78

## Introduction

The Mental Health Technical Manual V. 5.01 is designed as a reference manual to provide a technical description of the Mental Health package for the Department of Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS), Automated Data Processing Application Coordinators (ADPAC), and Clinical Coordinators.  For more information regarding options and menus, please see the Mental Health User Manual V. 5.01.

### Overview

The Mental Health V. 5.01 package is designed to provide a means of rapidly gathering, storing, and reporting clinical information for patients receiving mental health treatment and /or assistance with vocational issues. The clinical information stored in the VistA database is readily accessible to clinical staff throughout the various Mental Health Treatment Service areas and other clinics in the Medical Center. It can also be sent to enterprise storage facilities such as the Austin Information Technology Center (AITC).

#### Software and Manual Retrieval

The following software and documentation files are exported as part of Mental Health patch YS*5.01*150:

| **File Name**     | **Contents**                               | **Format**   |
|-------------------|--------------------------------------------|--------------|
| YS_501_150_IG.PDF | YS_MHA3 Installation Guide                 | Binary       |
| YS_MHA3_UM.PDF    | YS_MHA3 User Manual                        | Binary       |
| YS_MHA3_TM.PDF    | YS\_MHA3 Technical Manual /Security  Guide | Binary       |

The software files are available on the following OI Field Offices' [ANONYMOUS.SOFTWARE] directories. Use the following FTP address to connect to the first available FTP server: **REDACTED**

| **OI FIELD OFFICE**   | **FTP ADDRESS**   | **DIRECTORY**   |
|-----------------------|-------------------|-----------------|
| REDACTED              | REDACTED          | REDACTED        |
| REDACTED              | REDACTED          | REDACTED        |

#### VistA Intranet

Refer to the Web sites listed below when you want to receive more background and technical information about the Mental Health package v 5.01, and to download this manual and related documentation.

Online Documentation for this product is available at: http://www.va.gov/vdl/ . This website is the VistA Documentation Library (VDL), which has a listing of all the software manuals for VistA. Click on the Mental Health link, and it will take you to the Mental Health v 5.01 documentation.

#### Screen Displays

Before installing Mental Health package v 5.01, review this section to learn the many conventions used throughout this guide.

- **Keyboard Responses** : Keys provided in boldface, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see **enter** in the copy, press this key on your keyboard.
- **Screen Captures** : Provide “shaded” examples of what you will see on your computer screen, and possible user responses. The computer dialogue appears in Courier font.
- **Notes** : Provided within the steps describe exceptions or special cases about the information presented. They reflect the experience of our staff, developers, and testers.
- **Note:** This *boxed* element highlights special details about the current topic.
- **Other Names** : File and field names, and Security keys provided in uppercase. For example, you may select a patient's name from the PATIENT file (#2).
- **Menu Options** : Provided in italics. For example, you may establish Electronic Signatures Codes using the Kernel Electronic Signature Code Edit [XUSESIG] option.

## Implementation &amp; Maintenance

### Minimum Requirements

Before installing Mental Health package v 5.01, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).

| **Application Name**   | **Minimum Version Needed**   |
|------------------------|------------------------------|
| CPRS                   | 31 A                         |
| Clinical Reminders     | 2.0                          |
| Kernel                 | 8.0                          |
<!-- rpc-table -->
| RPC Broker             | 1.1                          |
| PIMS                   | 5.3                          |
| VA FileMan             | 22.0                         |
| Mailman                | 8.0                          |

### Routines and Checksums

The Calculate and Show Checksum Values [XTSUMBLD-CHECK] menu option can be used as shown below to display a list of checksums for Mental Health package V. 5.01. The Mental Health routines are in the YS* and YT* namespaces.

Select Programmer Options Option: Calculate and Show Checksum Values

This option determines the current Old (CHECK^XTSUMBLD) or New

(CHECK1^XTSUMBLD) logic checksum of selected routine(s).

Select one of the following:

1. Old
2. New

New or Old Checksums: New// 2New New Checksum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1. Any comment line with a single semi-colon is presumed to be followed by comments and only the line tag will be included.

1. Line 2 will be excluded from the count.

1. The total value of the routine is determined (excluding exceptions noted above) by multiplying the ASCII value of each character by its position on the line and position of the line in the routine being checked.

Select one of the following:

Package

Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: YS*5.01*150MENTAL HEALTH

YS150PST	value = 9122642

YTQAPI2D	value = 6639144

YTSACE		value = 2551823

YTSBSL23	value = 3044905

YTSCMQ		value = 2552097

YTSEAT26	value = 6312697

YTSFOCI		value = 4656413

YTSMHRM	value = 2499615

YTSNUDEC	value = 13752134

YTSSIP30	value = 5052592

YTSSIPST		value = 5906306

YTSSWEM	value = 6610853

### Routine Descriptions

To obtain a brief description for all Mental Health routines, use the First Line Routine Print [XU FIRST LINE PRINT] menu option. Including the second line in the report will show which patches have made changes to the routine. This menu option is part of Programmer Options [XUPROG] on the Routine Tools [XUPR-ROUTINE-TOOLS] menu.

## Files

The following is a listing of the files exported with Mental Health package v. 5.01:

|   **File Number** | **File Name**                    | **Global**    |
|-------------------|----------------------------------|---------------|
|           601     | MH Instrument                    | **^YTT(601,** |
|           601.2   | PSYCH INSTRUMENT PATIENT         | ^YTD(601.2,   |
|           601.3   | COPYRIGHT HOLDER                 | ^YTT(601.3,   |
|           601.4   | INCOMPLETE PSYCH TEST PATIENT    | ^YTD(601.4,   |
|           601.6   | MH MULTIPLE SCORING              | ^YTT(601.6,   |
|           601.71  | MH TESTS AND SURVEYS             | ^YTT(601.71,  |
|           601.72  | MH QUESTIONS                     | ^YTT(601.72,  |
|           601.73  | MH INTRODUCTIONS                 | ^YTT(601.73,  |
|           601.74  | MH RESPONSE TYPES                | ^YTT(601.74,  |
|           601.75  | MH CHOICES                       | ^YTT(601.75,  |
|           601.751 | MH CHOICETYPES                   | ^YTT(601.751, |
|           601.76  | MH INSTRUMENT CONTENT            | ^YTT(601.76,  |
|           601.77  | MH BATTERIES                     | ^YTT(601.77,  |
|           601.78  | MH BATTERY CONTENTS              | ^YTT(601.78,  |
|           601.781 | MH BATTERY USERS                 | ^YTT(601.781, |
|           601.79  | MH SKIPPED QUESTIONS             | ^YTT(601.79,  |
|           601.81  | MH SECTIONS                      | ^YTT(601.81,  |
|           601.82  | MH RULES                         | ^YTT(601.82,  |
|           601.83  | MH INSTRUMENTRULES               | ^YTT(601.83,  |
|           601.84  | MH ADMINISTRATIONS               | ^YTT(601.84,  |
|           601.85  | MH ANSWERS                       | ^YTT(601.85,  |
|           601.86  | MH SCALEGROUPS                   | ^YTT(601.86,  |
|           601.87  | MH SCALES                        | ^YTT(601.87,  |
|           601.88  | MH DISPLAY                       | ^YTT(601.88,  |
|           601.89  | MH CHOICEIDENTIFIERS             | ^YTT(601.89,  |
|           601.91  | MH SCORING KEYS                  | ^YTT(601.91,  |
|           601.92  | MH RESULTS                       | ^YTT(601.92,  |
|           601.93  | MH REPORT                        | ^YTT(601.93,  |
|           601.94  | MH CR SCRATCH                    | ^YTT(601.94,  |
|           603.01  | CLOZAPINE PATIENT LIST           | ^YSCL(603.01, |
|           603.02  | CLOZAPINE LAB TEST               | ^YSCL(603.02, |
|           603.03  | CLOZAPINE PARAMETERS             | ^YSCL(603.03, |
|           603.04  | CLOZAPINE TESTS                  | ^YSCL(603.04, |
|           603.05  | CLOZAPINE HL7 TRANSMISSION       | ^YSCL(603.05, |
|           604     | ADDICTION SEVERITY INDEX         | ^YSTX(604,    |
|           604.26  | ASI PROGRAM TYPE                 | ^YSTX(604.26, |
|           604.3   | ASI LEGAL CODE                   | ^YSTX(604.3,  |
|           604.4   | ASI LIVING ARRANGEMENTS          | ^YSTX(604.4,  |
|           604.45  | ASI PATIENT RATING SCALE         | ^YSTX(604.45, |
|           604.48  | ASI ROUTE OF ADMINISTRATION      | ^YSTX(604.48, |
|           604.5   | ASI FAMILY HX CODES              | ^YSTX(604.5,  |
|           604.55  | ASI FOLLOW UP                    | ^YSTX(604.55, |
|           604.66  | ASI QUICK FORM                   | ^YSTX(604.66, |
|           604.68  | ASI NARRATIVE                    | ^YSTX(604.68, |
|           604.77  | ASI SUBSTANCE CODE               | ^YSTX(604.77, |
|           604.8   | ASI PARAMETERS                   | ^YSTX(604.8,  |
|           615.2   | SECLUSION/RESTRAINT              | ^YS(615.2,    |
|           615.5   | S/R REASONS                      | ^YSR(615.5,   |
|           615.6   | S/R CATEGORY                     | ^YSR(615.6,   |
|           615.7   | S/R RELEASE CRITERIA             | ^YSR(615.7,   |
|           615.8   | S/R ALTERNATIVES                 | ^YSR(615.8,   |
|           615.9   | S/R OBSERVATION CHECKLIST        | ^YSR(615.9,   |
|           627.7   | DSM                              | ^YSD(627.7,   |
|           627.8   | DIAGNOSTIC RESULTS MENTAL HEALTH | ^YSD(627.8,   |
|           627.9   | DSM MODIFIERS                    | ^DIC(627.9,   |

### File Descriptions

For a complete description of each file and fields, use the List File Attributes [DILIST] option of the VA File Manager. See the list above for the file names and numbers.

### VA File Manager Access Codes

This list shows all Mental Health package files and their VA File Manager access codes:

YGO					   		DD	  RD	    WR	DEL	  LA

FILE					   NUMBER	ACCESS  ACCESS  ACCESS  ACCESS

ACCESS

-----------------------------------------------------------------------------

MH INSTRUMENT			   601	@	  Y	    y	      y 	  y

PSYCH INSTRUMENT PATIENT	   601.2.	@	  Y	    Y		y 	  Y

COPYRIGHT HOLDER			   601.3.	@	  Y	    y		y 	  y

INCOMPLETE PSYCH TEST PATIENT    601.4.	@	  Y	    Y		Y 	  Y

MH MULTIPLE SCORING 		   601.6	@	  @	    @		@	  @

MH TESTS AND SURVEYS		   601.71	@	  @	    @		@ 	  @

MH QUESTIONS			   601.72	@	  @	    @		@	  @

MH INTRODUCTIONS			   601.73	@	  @	    @		@ 	  @

MH RESPONSE TYPES			   601.74	@	  @	    @		@ 	  @

MH CHOICES				   601.75	@	  @	    @		@ 	  @

MH CHOICETYPES 			   601.751	@	  @	    @		@	  @

MH INSTRUMENT CONTENT		   601.76	@	  @	    @		@	  @

MH BATTERIES			   601.77	@	  @	    @		@	  @

MH BATTERY CONTENTS 		   601.78	@	  @	    @		@	  @

MH BATTERY USERS			   601.781	@	  @	    @		@	  @

MH SKIPPED QUESTIONS		   601.79	@	  @	    @		@	  @

MH SECTIONS				   601.81	@	  @	    @		@	  @

MH RULES				   601.82	@	  @	    @		@	  @

MH INSTRUMENTRULES		   601.83	@	  @	    @		@	  @

MH ADMINISTRATIONS		   601.84	@	  @	    @		@	  @

MH ANSWERS				   601.85	@	  @	    @		@	  @

MH SCALEGROUPS 			   601.86	@	  @	    @		@	  @

MH SCALES 				   601.87	@	  @	    @		@	  @

MH DISPLAY				   601.88	@	  @	    @		@	  @

MH CHOICEIDENTIFIERS		   601.89	@	  @	    @		@	  @

MH SCORING KEYS			   601.91	@	  @	    @		@	  @

MH RESULTS				   601.92	@	  @	    @		@	  @

MH REPORT 				   601.93	@	  @	    @		@	  @

MH CR SCRATCH			   601.94	@	  @	    @		@	  @

CLOZAPINE PATIENT LIST		   603.01	----------------NONE--------------

CLOZAPINE LAB TEST		   603.02	@	  @	    @		@	  @

CLOZAPINE PARAMETERS		   603.03	@	  @	    @		@	  @

CLOZAPINE TESTS			   603.04	----------------NONE--------------

CLOZAPINE HL7 TRANSMISSION FILE  603.05	@	  Y	    @		@	  @

ADDICTION SEVERITY INDEX 	   604	----------------NONE--------------

ASI PROGRAM TYPE			   604.26	----------------NONE--------------

ASI LEGAL CODE 			   604.3	----------------NONE--------------

ASI LIVING ARRANGEMENTS		   604.4	----------------NONE--------------

ASI PATIENT RATING SCALE 	   604.45	----------------NONE--------------

ASI ROUTE OF ADMINISTRATION	   604.48	----------------NONE--------------

ASI FAMILY HX CODES		   604.5	----------------NONE--------------

ASI FOLLOW UP			   604.55	----------------NONE--------------

ASI QUICK FORM			   604.66	----------------NONE--------------

ASI NARRATIVE			   604.68	----------------NONE--------------

ASI SUBSTANCE CODE		   604.77	----------------NONE--------------

ASI PARAMETERS 			   604.8	----------------NONE--------------

SECLUSION/RESTRAINT 		   615.2.	@	  Y	    Y		y	  Y

S/R REASONS				   615.5.	@	  Y	    y		y	  y

S/R CATEGORY			   615.6.	@	  Y	    y		y	  y

S/R RELEASE CRITERIA		   615.7.	@	  Y	    y		y	  y

S/R ALTERNATIVES			   615.8.	@	  Y	    y		y	  y

S/R OBSERVATION CHECKLIST	   615.9.	@	  Y	    y		y	  y

DSM					   627.7	----------------NONE--------------

DIAGNOSTIC RESULTS-MENTAL HEALTH 627.8.	@	  Y	    Y		Y	  Y

DSM-III-R MODIFIERS 		   627.9.	@	  Y	    @		@	  @

### Pointer Relations

Use the Map Pointer Relations [DI DDMAP] option to create a visual representation of the file pointer relationships.

## Exported Options

The menu and options exported by the Mental Health package V. 5.01 are in the YS* and YT* namespaces. Individual options can be viewed by using the Kernel option XUINQUIRE (Inquire).

### Mental Health Menu Distributions

The following is a display of the options in the Mental Health V. 5.01 package.

**Mental Health [YSUSER] Menu**

The Mental Health [YSUSER] menu is the Mental Health package primary menu. This menu contains two options.

After you select the Mental Health [YSUSER] menu, you will see a display similar to the one below. Assignment of privileges will determine what options are available for your use.

** Mental Health version 5.01 **

1 Clinical Record ...

6 Global Assessment of Functioning ...

Each of the options listed submenus that lead to other options and menus. These are described below.

**Note: Functionality within some options is controlled by security keys. See the Security Key section for a complete description of the keys.**

### Transmission Options [YSCL HL7 MAIN]

For Clozapine HL7 Transmission Options, patient Clozapine pharmacy orders and Clozapine lab results are to be sent nightly to the National Clozapine Registry (NCR) via the scheduled Transmit Clozapine Rx HL7 Messages [YSCL HL7 CLOZ TRANSMISSION] option.

The Clozapine HL7 Transmission Options [YSCL HL7 MAIN] menu includes options that allow patient Clozapine HL7 pharmacy orders and Clozapine lab results to be manually sent or re-sent to the NCR database. Previously sent Clozapine HL7 messages may also be printed.

Options:

- Clozapine HL7 Messages Summary
- List of Clozapine Prescriptions
- Print HL7 Report by Date
- Queue Clozapine Rx HL7 Messages
- Retransmit Clozapine Rx HL7 Messages

### Clinical Record [YSCLINRECORD]

The Clinical Record [YSCLINRECORD] menu includes options and menus that allow you to access and input patient data.

*** MENTAL HEALTH ***

CLINICAL RECORD

3 Diagnosis ...

13Seclusion/Restraint ...

Diagnosis [YSDIAG]

1. Enter Diagnosis
2. Print Diagnoses
3. Print DXLS History

### Seclusion/Restraint [YSSR SEC/RES]

The Seclusion/Restraint [YSSR SEC/RES] menu includes options for information regarding seclusion/restraint. If there are patients in the Seclusion /Restraint files, you will see the following heading above the menu.

The following patient(s) are currently listed as being in Seclusion/Restraint:

DATE &amp; TIMETOTAL

PATIENT SSNINITIATEDORDERED BYTIME

================================================================================

YSPATIENT,ONExxxx*JAN 21, 2012@14:42YSPROVIDER,ONE2400:7

* Written order required.

1. Entry of Patient to Seclusion/Restraint
2. Release of Patient from Seclusion/Restraint
3. Fifteen-Minute Check
4. **4 Seclusion/Restraint Report Utilities..**

### Seclusion/Restraint Report Utilities [YSSR REPORTS]

The Seclusion/Restraint Report Utilities [YSSR REPORTS] menu includes options to display Seclusion/Restraint information in various formats.

1. MONTHLY..Monthly Report (VA Form 10-2683)
2. PATIENT..S/R Mgmt Report by Patient Episode
3. DATE.....S/R Mgmt Report by Date
4. NURSING..S/R Mgmt Report by Nursing Shift
5. REVIEW...S/R Mgmt Report of Review Actions

6      WARD.....S/R Mgmt Ward Report

### Global Assessment of Functioning

The Global Assessment of Functioning [YSGAF MAIN] menu is the top menu to enter, graph and print GAF scores. These scores are equivalent to the DSM IV Axis 5 diagnosis.

1. Enter GAF by Clinic Visit
2. Print GAF's by Clinic/Date
3. Single Patient GAF Entry
4. Historical GAF listing
5. Edit/mark errors on GAF

### MHS Manager

The MHS Manager [YSMANAGER] menu is exported with the Mental Health package; it is typically assigned to a user's secondary menu. This menu provides managerial utilities such as the Psychological Test Utilities that should be assigned only to individuals who are responsible for maintaining the Mental Health software.

*** MENTAL HEALTH ***

MHS MANAGER FUNCTIONS

1. Mental Health System site parameters ...
2. MHA2 Psych test utilities ...

5 Seclusion/Restraint Management Utilities ...

7 MHA3 Utilities ...

### Mental Health System Site Parameters

The Mental Health System site parameters [YS SITE PARAMETERS] menu includes options for use by the Mental Health Application Coordinator. Through it, site-specific files are maintained by the coordinator.

REASONS......Edit S/R Reasons File

CATEGORY.....Edit S/R Category File

RELEASE......Edit S/R Release Criteria File

ALTERNATIVES.Edit S/R Alternatives File

CHECKLIST....Edit S/R Checklist File

INSTRUMENT...Edit Instrument Restart Day Limit

### MHA2 Psych Test Utilities

The MHA2 Psych test utilities [YSUTIL] menu includes options to access the psych testing utilities options. This is a legacy option and does not affect MHA3.

*** LEGACY Mental Health ***

MHA2 Utilities

1. Audit test/interview data
2. Check Psych Data Base
    1. Delete Patient Data
    2. Print test/interview items
    3. Delete incomplete tests/interviews

### Seclusion/Restraint Management Utilities

Seclusion/Restraint Management Utilities [YSSR MGT UTILITY] menu contains options required for the management of the Seclusion/Restraint features.

MHS Manager Functions

1. Review of Seclusion/Restraint Action
2. Written Order Edit
3. Edit Seclusion/Restraint Entry
4. Delete Seclusion/Restraint Entry

### MHA3 Utilities

The MHA3 Utilities [YTQ MHA3 MENU] menu includes options for MHA3 settings and utilities.

*** Mental Health ***

MHA3 Utilities

1. Print Test Form
2. Detailed Definition
3. Delete Patient Data
4. Stop/Re-Start Progress Notes for an Instrument
5. Exempt Test
6. Test Usage
7. XML Output
8. Instrument Exchange

## Menu Diagrams

The options comprising the Mental Health package are arranged on menus according to functionality.

The Mental Health [YSUSER] option is used by most Mental Health package users. The MHS Manager [YSMANAGER] menu is for supervisors. Use the Menu Diagrams [XQDIAGMENU] option to create a visual representation of the menu structure.

## Mental Health Protocols (File #101)

YS GAFYS GAF A08 SERVERYS GAF A08 CLIENTYS GAF A08 CLENT

YS MHA A08 CLIENTYS MHA A08 CLIENT

YS MHA A08 EVENT

Used by List Manager for Exchange Utility --

YTXCHG BROWSE SPEC	Browse Specification

YTXCHG CREATE ENTRY	Create New Entry

YTXCHG DELETE ENTRY	Delete Entry

YTXCHG DRYRUN		Trial Install &lt;Dry Run&gt;

YTXCHG INSTALL		Install Exchange Entry

YTXCHG LOAD HOST	Load Host File

YTXCHG LOAD URL	 Load from URL

YTXCHG MAIN MENU	Instrument Exchange Menu

YTXCHG REBUILD ENTRY	 Rebuild Entry

YTXCHG SAVE HOST	Create Host File

## Remote Procedure Calls

The Mental Health V. 5.01 Remote Procedure Calls (RPC’S) are in the YS* and YT* namespaces. Use the FileMan Print functionality to find and display the entries in the REMOTE PROCEDURE file (#8994).

## Database Integration Agreements

To view the details of a Database Integration Agreements (DBIA) use the VA Forum option “Inquire to an Integration Control Registration” to display the DBIAS where the Mental Health package is the custodial or the subscribing package.

## External Relations

The VistA Mental Health Assistant (MHA) is the graphical user interface (GUI) for the VistA Mental Health package. MHA was developed to create an effective and efficient tool for all clinicians and their patients to use for the administration and scoring of assessment instruments and interviews. Additionally, results are displayed in report and graphical formats. MHA supports mental health assessments (e.g., psychological testing, structured interviews, questionnaires, etc.) that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA).

To better meet the needs of clinicians and patients in different treatment programs, particularly in nontraditional settings, MHA can now be run in a standalone mode to administer instruments offline for later uploading to Vista. For detailed instructions and requirements installing and implementing the MHA Graphical User Interface (GUI) software application, see the MHA3 Installation Guide.

### Non-M Software Distributed with Mental Health Assistant 3 (MHA3)

Here are typical examples of the storage locations for the MHA3 files (executable, DLL and other supporting files) installed on a workstation:

C:\Program Files\Vista\YS\MHA3

YS\_MHA.exe	(From Patch YS*5.01*123)

YS\_MHA.HLP (From Patch YS*5.01*85)

YS\_MHA.JCF (From Patch YS*5.01*85)

Borlndmm.dll 	(From Patch YS*5.01*123) Uninst000.dat uninst000.exe

C:\Program Files\Vista\Common Files

YS\_MHA\_A.dll

YS\_MHA\_AUX.dll

MHA3 Patch YS*5.01*150 exports the following folders and files:

| **FILE NAMES**       | **CONTENTS**                                                                  | **RETRIEVAL FORMATS**   |
|----------------------|-------------------------------------------------------------------------------|-------------------------|
| YS_501_150_IG.pdf    | Mental Health Assistant Version 3 (MHA3) Installation Guide Patch YS*5.01*150 | BINARY                  |
| **YS\_MHA3\_UM.pdf** | Mental Health Assistant Version 3 (MHA3) User Manual Patch YS*5.01*150        | BINARY                  |
| **YS\_MHA3\_TM.pdf** | Mental Health Assistant Version 3 (MHA3) Technical Manual Patch YS*5.01*150   | BINARY                  |

**Mental Health Remote Procedure Context Option**

The OPTION file (#19) entry **“YS BROKER1 version 1.0.3.85~1.0.5.11~1.0.3.86” [YS BROKER1]** provides the context necessary to interface the **V** *ist* **A** Mental Health Assistant Version 3 application to the VistA database via Remote Procedure Calls (RPC).

### MHA3 Server Options

The server options being used in the Mental Health package V. 5.01:

**Clozapine Data Server [YSCLSERVER]**

DESCRIPTION: This is a server to allow the National Clozapine Coordinating Center (NCCC) in Dallas to authorize Clozapine registration numbers for use at individual sites.

ROUTINE: YSCLSERV SERVER ACTION: RUN IMMEDIATELY

Mental Health Test Usage Server [YS TEST USAGE]

DESCRIPTION: Used by the National Mental Health Strategic Healthcare Group to determine the annual psychological test usage by site. This option reports the number of each test by station within any given time period.

The MAILMAN message must be in FILEMAN date format 3031001^3040930

ROUTINE: YSTUSESERVER ACTION: RUN IMMEDIATELY

Server test usage MHA3 stats [YTQTUSE]

DESCRIPTION: *** MHA3 *** Used by the National Mental Health Strategic Healthcare Group to determine the annual psychological test usage by site. This option reports the number of each test by station within any given time period.

The MAILMAN message must be in FILEMAN date format 3031001^3040930

ROUTINE: YTQTUSESERVER ACTION: RUN IMMEDIATELY

### Remote Systems

All Global Assessment of Functioning (GAF) scores entered through the Mental Health GAF form are dynamically sent to the National Patient Care Database (NPCD) at the Austin Information Technology Center (AITC).

Mental Health Entries in the HL LOGICAL LINK file (#870):

**YS GAF-SND**

LLP TYPE: MAILMAN

DEVICE TYPE: N

TIME STOPPED: MAR 16, 2011@15:49:59

SHUTDOWN LLP? YES

MESSAGE NUMBER: 1

STATUS: PENDING

**NODE: YSCL-NCCC**

LLP TYPE: TCP

QUEUE SIZE: 10

DESCRIPTION: This is the logical link for the National Clozapine Registry NCR). The NCR is maintained by the National Clozapine Coordinating Center NCCC).

Mental Health entries in the HL7 APPLICATION PARAMETER file (#771):

**NAME: YS GAF**

ACTIVE/INACTIVE: ACTIVE

MAIL GROUP: YS GAF TO NPCD

COUNTRY CODE: USA

**NAME: YS MHA**

ACTIVE/INACTIVE: ACTIVE

MAIL GROUP: YS MHA-MHNDB

COUNTRY CODE: USA

HL7 ENCODING CHARACTERS: ~^\&amp;

HL7 FIELD SEPARATOR: |

HL7 MESSAGE: ADT

PROCESSING ROUTINE: ACKMHA^YTQHL7

HL7 SEGMENT: PID

FIELDS USED IN THIS SEGMENT: 1,2

HL7 SEGMENT: MSH

FIELDS USED IN THIS SEGMENT: 1

HL7 SEGMENT: MSA

FIELDS USED IN THIS SEGMENT: 1,3,7,8,9,10

Mental Health entries in the HLO APPLICATION REGISTRY file (#779.2):

**APPLICATION NAME: YSCL-REG-REC**

HL7 MESSAGE TYPE: ADT

HL7 EVENT: A28

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

HL7 MESSAGE TYPE: RDE

HL7 EVENT: O11

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

Package File Link: MENTAL HEALTH

**APPLICATION NAME: YSCL-REG-SEND**

HL7 MESSAGE TYPE: ADT

HL7 EVENT: A28

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

HL7 MESSAGE TYPE: RDE

HL7 EVENT: O11

ACTION TAG: ACCEPTAR

ACTION ROUTINE: YSCLHLAD

HL7 VERSION: 2.5.1

MINIMUM RETENTION TIME: 10

Package File Link: MENTAL HEALTH

## Mental Health File Relationships

Files accessed by the Mental Health package V. 5.01:

|   **File #** | **File Name**                   | **Package**              | **Agreement Status**                         |
|--------------|---------------------------------|--------------------------|----------------------------------------------|
|         0.5  | FUNCTION file                   | KERNEL                   | Supported reference                          |
|         2    | PATIENT file                    | REGISTRATION             | Read Only, Supported reference & DBIA #87    |
|         3.1  | TITLE file                      | KERNEL                   | Pointed to by File #200, Read only Reference |
|         4    | INSTITUTION file                | KERNEL                   | Supported reference, Read only               |
|         5    | STATE file                      | KERNEL                   | Supported reference, Read only               |
|         8    | ELIGIBILITY CODE                | REGISTRATION             | DBIA #87                                     |
|        13    | RELIGION                        | REGISTRATION             | DBIA #277                                    |
|        19.1  | SECURITY KEY                    | MENU DRIVER              | Supported reference                          |
|        22    | POW PERIOD                      | REGISTRATION             | DBIA #277                                    |
|        23    | BRANCH OF SERVICE               | REGISTRATION             | DBIA #277                                    |
|        24    | NON-VETERAN CLASS               | REGISTRATION             | DBIA #277                                    |
|        25    | TYPE OF DISCHARGE               | REGISTRATION             | DBIA #277                                    |
|        31    | DISABILITY CONDITION            | REGISTRATION             | DBIA #277                                    |
|        35    | OTHER FEDERAL AGENCY            | REGISTRATION             | DBIA #277                                    |
|        36    | INSURANCE COMPANY               | REGISTRATION             | DBIA #277                                    |
|        37    | DEPOSITION                      | REGISTRATION             | DBIA #277                                    |
|        41.1  | SCHEDULED ADMISSION             | REGISTRATION             | DBIA#87                                      |
|        41.9  | CENSUS file                     | SCHEDULING               | DBIA #47                                     |
|        42    | WARD LOCATION file              | SCHEDULING               | Support reference, Read only                 |
|        42.4  | SPECIALITY file                 | REGISTRATION             | DBIA #277                                    |
|        44    | HOSPITAL LOCATION               | SCHEDULING               | Support reference, Read only                 |
|        45    | PTF (Patient Treatment file)    | DRG GROUPER REGISTRATION | DBIA #27 & #87  Support reference            |
|        45.7  | TREATING SPECIALTY file         | REGISTRATION             | DBIA #277                                    |
|        50    | DRUG file                       | OUTPATIENT PHARMACY      | DBIA #221                                    |
|        52    | PRESCRIPTION file               | OUTPATIENT PHARMAHCY     | DBIA #276                                    |
|        52.5  | RX SUSPENSE file                | OUTPATIENT PHARMACY      | DBIA #276                                    |
|        55    | PHARMACY PATIENT file           | OUTPATIENT PHARMACY      | DBIA #276  DBIA #4480                        |
|        80    | ICD DIAGNOSIS file              | DRG                      | Support reference, Read only                 |
|        80.1  | ICD OPERATION / PROCEDURE       | DRG                      | Support reference, Read only                 |
|       200    | NEW PERSON file                 | KERNEL                   | Support reference                            |
|       211.6  | NURSTOUR of DUTY file           | NURSING                  | DBIA #278                                    |
|       405    | PATIENT MOVEMENT                | PIMS                     | Support reference                            |
|       801.41 | REMINDER DIALOG                 | Clinical Reminders       | Supported reference                          |
|       801.43 | REMINDER FINDING ITEM PARAMETER | Clinical Reminders       | Supported reference                          |

## Mental Health Mail Group File (#3.8) Entries

**YS ASI PERFORMANCE MEASURES** - Members of this mail group will be used to receive the ASI Case Finder Report.

**YS GAF TO NPCD** - This mail group is being used by Mental Health to transmit data to the National Patient Care Database via HL7.

REMOTE MEMBER: XXX@Q-NPT.MED.VA.GOV

**YS GAF TRANSMISSION ACK** - This mail group will receive a message when a GAF score is transmitted to the National Patient Care Database or an error in the transmission has occurred.

**YS MHA-MHNDB** - This group receives error messages from the HL7 system when problems arise, sending messages to the Mental Health National database.

**YS PSYCHTEST** - Used to notify clinicians when tests and interviews are administered to patients at the requests of someone other than the person administering the test.

**YSCLHL7 LOGS** – This Mail Group is used for the receipt of mail messages that are created to log the transmission of HL7 messages for Clozapine patients.

## Archiving

Data archiving capabilities are not currently available for the Mental Health package.

## Package Security

Security in this package is controlled almost exclusively by the menu option that is assigned to a person.

Deletion of entries in many Mental Health files is prohibited under ordinary conditions.

### Security Keys (File #19.1)

Allocate the following security keys to appropriate site personnel:

**Name Description**

**YSCL AUTHORIZED** - The presence of this key designates an authorized Clozapine Provider.

**YSD** - Allows verification of ICD diagnoses. This is a clinical privilege. The chief of psychiatry will determine who may have this key.

**YSP** - Provides access to psychological test options. The Chief of

Psychology Service will determine who may have this key.

**YSQ** - Allows verification of DSM-III diagnoses. The Chiefs of

Clinical Services will determine who may have this key.

**YSZ** - Allows Mental Health technicians/aides to queue tests/interviews after completion.

## Glossary

This glossary contains definition of terms and abbreviations that may not be familiar to all users. Basic terms, acronyms, and phrases that are used throughout the Vista environment are included.

| **Term**                | **Definition**                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @                       | The at symbol (@) is used to delete an entry in a FileMan file.                                                                                                                                                                                                                                                                                                              |
| ADT                     | ADMISSIONS DISCHARGES, and TRANSFERS (part of the PIMS package).                                                                                                                                                                                                                                                                                                             |
| ABBREVIATED RESPONSE    | Data entry by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.                                                                                                                                                                                                            |
| AXIS 4                  | A numeric representation of the severity of psychological stressors.                                                                                                                                                                                                                                                                                                         |
| AXIS 5                  | A numeric representation of the global assessment of functioning.  AXIS 5 is a clinician’s overall judgment of a patient’s social/psychological and occupational functioning on a continuum of mental health-illness.                                                                                                                                                        |
| CRISIS NOTES            | A note containing patient information that displays automatically wherever the patient’s name is entered into the system.                                                                                                                                                                                                                                                    |
| CROSS-  REFERENCE       | An index of file entries. For a description see the VA File Manager documentation.                                                                                                                                                                                                                                                                                           |
| DEFAULT                 | A response the considered the most probable answer to the prompt being displayed. A default is identified by two slash marks (//) immediately following the computer-displayed response. You may accept the default answer by pressing the ENTER (or RETURN) key. To change the default answer, type in your response.                                                       |
| DELETE                  | The key on your keyboard that enables deletion of individual characters. Place the CURSOR immediately after the last character of the string of characters you wish to delete and press the DELETE or RUBOUT key.                                                                                                                                                            |
| DRG                     | DIAGNOSIS RELATED GROUP is a prospective payment system, based on a complex set of criteria, which established a reimbursement fee determined by the primary diagnosis. Each diagnosis is assigned a DRG number.                                                                                                                                                             |
| DUZ                     | A user identification number assigned by Vista. It is the IEN of the NEW PERSON file (#200).                                                                                                                                                                                                                                                                                 |
| DX                      | Diagnosis.                                                                                                                                                                                                                                                                                                                                                                   |
| DXLS                    | Diagnosis Length of Stay. The diagnosis most responsible for the patient’s length of stay during the current admission.                                                                                                                                                                                                                                                      |
| ENTER                   | Press the RETURN or ENTER key to instruct the system to store the information you just entered.                                                                                                                                                                                                                                                                              |
| FIELD                   | A FIELD is similar to questions on a questionnaire. It is a statement that requests information. Your response is the value entered into that field. For example, the prompt, “DOB” is a field in which you enter your birth date.                                                                                                                                           |
| GLOBAL VARIABLE         | Usually referred to as a global. A disc-resident structure (e.g. ^YTT(601), used to store data in the VistA database.                                                                                                                                                                                                                                                        |
| HELP                    | Assistance displayed on your terminal screen. The HELP function displays menus and describes options. To obtain HELP, enter 1-4 question marks in response to a prompt. The level of help you receive increases with the number of question marks you enter.                                                                                                                 |
| IEN                     | The INTERNAL ENTRY NUMBER of a record in a File Manager file.                                                                                                                                                                                                                                                                                                                |
| KERNEL                  | The VA kernel is the software suite that integrates the operating system with other software applications such as Mental Health, Laboratory, and Pharmacy.                                                                                                                                                                                                                   |
| LOS                     | Length of stay.                                                                                                                                                                                                                                                                                                                                                              |
| LEVEL                   | Patients are assigned a LEVEL, a scaled position. The definition of each level is up to the local station. For example, a level 1 patent may require staff supervision when involved in off-ward activities, whereas a level 2 patient may leave the ward when accompanied by a level 3 patient.                                                                             |
| MASTER  TREATMENT  PLAN | The comprehensive Treatment Plan for the TREATMENT of an individual patient during each hospitalization. The plan is reviewed at regular intervals and adjusted to accommodate the needs of the patient.                                                                                                                                                                     |
| MH                      | Mental Health                                                                                                                                                                                                                                                                                                                                                                |
| MENU                    | A list of options that may include submenus or options.                                                                                                                                                                                                                                                                                                                      |
| NOK                     | Next of kin.                                                                                                                                                                                                                                                                                                                                                                 |
| ONSET                   | The beginning of a symptom or disease.                                                                                                                                                                                                                                                                                                                                       |
| OPTION NAME             | The formal name of an option. By convention, it is displayed in brackets and is the .01 field of the OPTION file (#19).                                                                                                                                                                                                                                                      |
| PATIENT MESSAGE         | Information concerning a patient that is not part of the permanent clinical record. If a message has been entered for a patient, a notation indicating that a PATIENT MESSAGE exists is displayed every time the patient’s name is entered into the system. A Patient Message may be transferred to a Progress Note where, it becomes part of the permanent clinical record. |
| PRIMARY                 | The condition that is chiefly responsible for the DIAGNOSIS the patient’s treatment.                                                                                                                                                                                                                                                                                         |
| PRIORITY CATEGORY       | Codes used to denote the order in which a patient’s acceptance into a program or clinic is determined.                                                                                                                                                                                                                                                                       |
| PROGRESS NOTES          | A note containing information concerning a patient. There are numerous kinds of progress notes such as admission, discharge, pre-operative, social work, nursing, etc. A progress note is included in the patient’s permanent clinical record.                                                                                                                               |
| PSYCHOSIS               | Gross impairment in reality testing.                                                                                                                                                                                                                                                                                                                                         |
| PROMPT                  | The system interacts with the user by issuing questions and statements called PROMPTS, and the user enters a response.                                                                                                                                                                                                                                                       |
| SIGNATURE BLOCK         | Used with electronic signatures. A SIGNATURE BLOCK indicates the author’s complete name and title.                                                                                                                                                                                                                                                                           |
| SSN                     | Social Security Number.                                                                                                                                                                                                                                                                                                                                                      |
| TEAM                    | An organizational sub-unit of a ward which is often composed of residents, medical students, psychologists, social workers, nurses, etc.                                                                                                                                                                                                                                     |
| VA FileManager          | The Database Management System (DBMS) used by Vista. It is often referred to as FileMan.                                                                                                                                                                                                                                                                                     |
| VERIFY CODE             | An additional security precaution used in conjunction with ACCESS CODE. Like the access code, it is also 6-11 digits in length and if entered incorrectly, the user is not allowed access to the computer. Both codes are invisible on the terminal screen to provide user-protection.                                                                                       |

## Abbreviations, Acronyms, and Descriptions

| **Abbreviation or Acronym**   | **Description**                                                                                  |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| API                           | Application Programmer Interface                                                                 |
| AITC                          | Austin Information Technology Center                                                             |
| ARTS                          | Adverse Reaction Tracking                                                                        |
| CPRS                          | Computerized Patient Record System                                                               |
| DBMS                          | Database Management System                                                                       |
| DFN                           | Internal entry number of a record in the PATIENT file (#2). DFN is the name of a local variable. |
| DVA                           | Department of Veterans Affairs                                                                   |
| FDA                           | Food and Drug Administration                                                                     |
| GUI                           | Graphical User Interface                                                                         |
| HL7                           | Health Level 7 (a data-transmission protocol).                                                   |
| HSD&D                         | Health System Design and Development                                                             |
| ICN                           | Integration Control Number, or national VA patient record number                                 |
| IEN                           | Internal Entry Number (of a record in a FileMan file).                                           |
| IMG                           | Information Management Group                                                                     |
| IRM                           | Information Resource Management                                                                  |
| KIDS                          | Kernel Installation and Distribution System                                                      |
| M                             | Alternate name for MUMPS                                                                         |
| MHA                           | Mental Health Assistant                                                                          |
| MUMPS                         | Massachusetts General Hospital Utility Multiprogramming System                                   |
| OINT                          | Office of Information National Training and Education Office                                     |
| PCE                           | Patient Care Encounter                                                                           |
| PIMS                          | Patient Information Management Systems                                                           |
| PMO                           | Project Management Office                                                                        |
| PTF                           | Patient Treatment File                                                                           |
| SI                            | System Implementation                                                                            |
| SPP                           | Suicide Prevention Project                                                                       |
| VA                            | Department of Veteran Affairs                                                                    |
| VERA                          | Veterans Equitable Resource Allocation                                                           |
| VHA                           | Veterans Health Administration                                                                   |

## Appendix A

The Mental Health package contains a number of software elements that were deprecated (marked as obsolescent) in 2004 or earlier. These software components are deleted or disabled in Mental Health Patch 60 (YS*5.01*60). The following is a description of those items which will become obsolete with the release of Patch 60.

The obsolete software may contain scoring algorithms that are no longer correct, outdated data structures, and code that doesn’t meet current VA software standards and conventions.

### Files Deleted by Mental Health Patch 60

|  File Name           |   File # |  Global Location   |
|----------------------|----------|--------------------|
| MEDICAL RECORD       |    90    | ^MR(               |
| PT. TEXT             |    99    | ^PTX(              |
| CRISIS NOTE DISPLAY  |   600.7  | ^YSG("CNT",        |
| MH TEXT              |   605    | ^YTX(              |
| MH CLINICAL FILE     |   615    | ^YS(615,           |
| MH WAIT LIST         |   617    | ^YSG("WAIT",       |
| MENTAL HEALTH CENSUS |   618    | ^YSG("CEN",        |
| MENTAL HEALTH TEAM   |   618.2  | ^YSG("SUB",        |
| MENTAL HEALTH INPT   |   618.4  | ^YSG("INP",        |
| PROBLEM              |   620    | ^DIC(620,          |
| JOB BANK             |   624    | ^YSG("JOB",        |
| INDICATOR            |   625    | ^DIC(625,          |
| DSM3                 |   627    | ^DIC(627,          |
| DSM-III-R            |   627.5  | ^DIC(627.5,        |
| DSM CONVERSION       |   627.99 | ^YSD(627.99,       |
| YSEXPERT             |   628    | ^YS(628,           |

### Options Deleted by Mental Health Patch 60

1. YS SITE-FILE 16 - SIGNATURE....Edit Signature Block Title
2. YS SITE-FILE 602 TEST LIM - INSTRUMENT...Edit Instrument Restart Day Limit
3. YS SITE-FILE 602 WWU - WWU..........Edit Weighted Work Unit (WWU)
4. YSADMTEST - Psychological tests/interviews (administer)
5. YSAPROB - Add a new problem
6. YSAS CASE FINDER - ASI Case Finder
7. YSAS FOLLOWUP FINDER - ASI Followup Finder
8. YSCENCAD - Cancel a MH Census Discharge
9. YSCENCL - Custom List
10. YSCENCRISIS - Crisis notes and Messages
11. YSCENDAYHX - Previous Admissions by Date
12. YSCENDCDOC - Discharge Comments Entry
13. YSCENDIA - Active Diagnoses
14. YSCENED - Enter/Edit Current Inpatient Data
15. YSCENEDM - Enter/Edit MH Inpatient Data
16. YSCENFS - Census
17. YSCENGED - Group Data Entry/Edit
18. YSCENIL - Individual Patient List
19. YSCENLOS - Current Inpatient Days
20. YSCENMAIN - Inpatient Features
21. YSCENMEDS - Outpatient Medications
22. YSCENMGR - Inpatient Features management functions
23. YSCENNAM - Name Search
24. YSCENNEW - Recent Admissions
25. YSCENPAHX - Individual Data Look Up
26. YSCENPASS - Pass/Last Transfer List
27. YSCENPL - Patient Lists
28. YSCENPP - Patient Profile Data
29. YSCENREM - Graph of Patients Remaining
30. YSCENROT - Rotation of Teams31. YSCENSL - Short Patient List
    1. YSCENSUBUP - Team Definition
    2. YSCENTAH - Team Admissions Record
    3. YSCENTCEN - Team Census
    4. YSCENTESTING - Psychological Tests and Interviews
    5. YSCENTMHX - Ward/Team History - LOS, DRG and DXLS
    6. YSCENTPTE - Treatment Plan Tracking data entry
    7. YSCENTPTP - Treatment Plan Tracking Report
    8. YSCENUNITUP - Ward Definition
    9. YSCENUNT - Group Data Lookup
    10. YSCENWDM - Statistics
    11. YSCENWL - Work List
    12. YSCLERK - Clerk-entered tests
    13. YSCOMMENT - Append comments to tests and interviews
    14. YSCRISNOT - Crisis note
    15. YSDECTREES-R - Decision Tree Shell
    16. YSDIRTEST - Staff entry of tests/interviews
    17. YSEPROB - Edit a problem
    18. YSEXTESTS - Exempt psychological tests
    19. YSFPROB - Formulate new problem list
    20. YSGAF CASE FINDER - GAF Case Finder
    21. YSHX1 - History - present illness
    22. YSHXPAST - Past medical history
    23. YSHXPASTR - Past medical history (results of pt. report)
    24. YSINST RESTART LIMIT - Edit Instrument Restart Limit
    25. YSIPROB - Inactivate an active problem
    26. YSJOBINQ - Inquire to job bank
    27. YSJOBKILL - Purge job bank
    28. YSJOBLIST - Search job bank
    29. YSJOBUPDATE - Update job bank
    30. YSMANAGEMENT - General Management
    31. YSMLST - List Tests &amp; Interviews
    32. YSMOVP - Move crisis notes and messages
    33. YSPATMSG - Patient message
    34. YSPATPROF - Profile of patient
    35. YSPERSHX - Psychosocial history
    36. YSPERSHXR - Psychosocial history (results of pt. report)
    37. YSPHYEXAM - Physical exam
    38. YSPLDX - DSM Diagnosis (Problem list)
    39. YSPLPDX - ICD9 Diagnosis (Problem list)
    40. YSPPROB - Print the problem list
    41. YSPRINT - Tests and interviews (results)
    42. YSPROBLIST - Problem list
    43. YSPTINSTRU - Patient-administered Instruments
    44. YSRAPROB - Reactivate an inactive problem
    45. YSREVSYS - Review of systems
    46. YSREVSYSR - Review of systems (results of pt. report)
    47. YSRFPROB - Reformulate a problem79. YSRSPROB - Resolve a problem
        1. YSTESTBAT - Test battery utility
        2. YSVOCATIONAL - Vocational Rehabilitation
        3. YSWAITCR - Create/edit wait lists
        4. YSWAITE - Add patient to wait list
        5. YSWAITEDI - Edit patient list data
        6. YSWAITLST - Wait lists
        7. YSWAITP - Print wait list
        8. YSWAITREM - Remove patient from list
        9. YSWAITSHUF - Move patient on list
        10. YT SF36 HEALTH SURVEY - SF-36 Health Survey

### Routines Deleted by Mental Health Patch 60

| YS03ENV   | YS04ENV   | YS04POST   | YS05ENV   | YS05POST   | YS06ENV   | YS23ENV   | YS23POST   |
|-----------|-----------|------------|-----------|------------|-----------|-----------|------------|
| YS24ENV   | YS24POST  | YS26ENV    | YS29ENV   | YS30ENV    | YS30PRE   | YS32ENV   | YS33ENV    |
| YS37ENV   | YS38ENV   | YS38POST   | YS39POST  | YS42ENV    | YS43POST  | YS501100  | YS501P82   |
| YS501P83  | YS85POST  | YS85PRE    | YS96POST  | YS97POST   | YSANTEG   | YSAPOST   | YSASCF     |
| YSCEN     | YSCEN1    | YSCEN10    | YSCEN13   | YSCEN14    | YSCEN2    | YSCEN21   | YSCEN22    |
| YSCEN23   | YSCEN24   | YSCEN26    | YSCEN3    | YSCEN31    | YSCEN32   | YSCEN33   | YSCEN34    |
| YSCEN35   | YSCEN36   | YSCEN37    | YSCEN39   | YSCEN4     | YSCEN41   | YSCEN5    | YSCEN51    |
| YSCEN52   | YSCEN53   | YSCEN54    | YSCEN55   | YSCEN56    | YSCEN6    | YSCEN61   | YSCEN7     |
| YSCEN8    | YSCEN81   | YSCPAF     | YSCPAG    | YSCPAI     | YSCPAK    | YSCPAL    | YSCPAM     |
| YSCPAQ    | YSCUP     | YSCUP000   | YSCUP001  | YSCUP002   | YSCUP003  | YSCUP004  | YSD40030   |
| YSD40031  | YSD40032  | YSD40040   | YSD40041  | YSD40042   | YSD40050  | YSD40051  | YSD40052   |
| YSD40060  | YSD40061  | YSD40062   | YSD4C000  | YSD4CK00   | YSD4DSM   | YSD4E010  | YSD4E020   |
| YSD4POS0  | YSD4POST  | YSD4PRE    | YSD4PRE0  | YSD4UT01   | YSDX0001  | YSDX0002  | YSDXR000   |
| YSDXR1    | YSEMSG    | YSESA      | YSESD     | YSESE      | YSESED    | YSESH     | YSESL      |
| YSESLOG   | YSESM     | YSESN      | YSESP     | YSESR      | YSESUT    | YSHELP    | YSHX1      |
| YSHX1R    | YSJOB     | YSJOBK     | YSKFASI1  | YSKFASI2   | YSKFASIF  | YSKFASIM  | YSMV       |
| YSMV1     | YSNTEG    | YSNTEG0    | YSONIT    | YSONIT1    | YSONIT2   | YSONIT3   | YSPDR1     |
| YSPDXR    | YSPHY     | YSPHY1     | YSPHYR    | YSPP       | YSPP1     | YSPP1A    | YSPP2      |
| YSPP3     | YSPP4     | YSPP5      | YSPP6     | YSPP7      | YSPP8     | YSPP9     | YSPPJ      |
| YSPRBR1   | YSPRBR2   | YSPROB     | YSPROB1   | YSPROB2    | YSPROB3   | YSPROB4   | YSPROB5    |
| YSPROBR   | YSPROBR1  | YSPROSE    | YSPTX     | YSPTX1     | YSPTXR    | YSWX      | YSWX1      |
| YSWZ      | YSXRAA    | YSXRAA1    | YSXRAA2   | YSXRAA3    | YSXRAA4   | YSXRAF    | YSXRAF1    |
| YSXRAF2   | YSXRAF3   | YSXRAF4    | YSXRAF5   | YSXRAF6    | YSXRAG    | YSXRAG1   | YSXRAG2    |
| YSXRAJ    | YSXRAJ1   | YSXRAJ2    | YSXRAJ3   | YSXRAJ4    | YSXRAK1   | YSXRAK10  | YSXRAK11   |
| YSXRAK12  | YSXRAK2   | YSXRAK3    | YSXRAK4   | YSXRAK5    | YSXRAK6   | YSXRAK7   | YSXRAK8    |
| YSXRAK9   | YSXRAQ    | YSXRAQ1    | YSXRAQ2   | YSXRAQ3    | YSXRAQ4   | YSXRAR    | YSXRAR1    |
| YSXRAR2   | YSXRAS    | YSXRAS1    | YSXRAS2   | YSXRAT     | YSXRAT1   | YSXRAT2   | YSXRAT3    |
| YSXRAT4   | YSXRAT5   | YSXRAT6    | YSXRAU    | YSXRAU1    | YSXRAU2   | YSXRAV    | YSXRAV1    |
| YSXRAV2   | YSXRAW1   | YSXRAW2    | YSXRAZ1   | YSXRAZ2    | YSXRAZ3   | YSXRAZ4   | YSXRAZ5    |
| YSXRAZ6   | YSXRBA    | YSXRBA1    | YSXRBA2   | YSXRBA3    | YSXRBA4   | YSXRBA5   | YSXRBA6    |
| YTEX      | YTQQI001  | YTQQI002   | YTQQI003  | YTQQI004   | YTQQI005  | YTQQI006  | YTQQI007   |
| YTQQI008  | YTQQI009  | YTQQI00A   | YTQQI00B  | YTQQI00C   | YTQQI00D  | YTQQI00E  | YTQQI00F   |
| YTQQI00G  | YTQQI00H  | YTQQI00I   | YTQQI00J  | YTQQI00K   | YTTB      |           |            |

These routines are deleted by KIDS during the patch installation.

## Appendix B

### NCCC HL7 Message Specification

This describes the data being moved through the HL7 interface.

#### Conventions

The following are the conventions for HL7 messages.

##### HL7 Messages

HL7 messages shall follow the standard HL7 version 2.5.1 format documented in An Application Protocol for Electronic Data Exchange in Healthcare Environments.

##### Date/Time of Message Format

The format for MSH-7, Date/Time of Message, is YYYYMMDD[HHMM[SS]] [+-ZZZZ] where:

- YYYY is the 4-digit year, e.g., “2002”
- MM is the month number, ranging from “01” to “12”
- DD is the day number within the month, ranging from “01” to “31”
- HH is the hour from “00” to “23”.? MM is the minute from “00” to “59”
- SS is the second from “00” to “59”
- +-ZZZZ represents the time zone as a leading signed value time offset from Greenwich Mean Time of the form HHMM using the same convention for HH and MM as given above. For example, Eastern Standard Time (EST) is given as “–0500”

##### Message and Segment Boundaries

Message starts with American Standard Code for Information Interchange (ASCII) character 11 10 , vertical tab (VT).

Segment terminates with ASCII character 13 10 , carriage return (CR).

Message terminates with ASCII character 28 10 , file separator (FS), followed by ASCII character 13 10, carriage return (CR).

The prototypical form is:

- &lt;VT&gt;segment&lt;CR&gt;segment&lt;CR&gt;&lt;FS&gt;&lt;CR&gt;

&lt;VT&gt; as the prefix and &lt;FS&gt;&lt;CR&gt; as the suffix are part of the HL7 Minimal Lower Layer Protocol, (MLLP).

##### Segment Tables

In the Segment tables that follow, missing sequence numbers indicate that the respective fields are empty in the segment. An empty field has no characters between its boundaries (start of the segment, field separators, and the end of the segment).

The Seq column contains the sequence number of the element.

The Name column gives the HL7 name for the element or sub-element. In those cases where HL7 does not supply a name, this document defines that name for use solely within the VistA and NCR interface.

Following the element name, data type information drawn from the HL7 2.5.1 standard *may* appear in the DT column.

The Len column contains the length of the element.

The Opt column value “R” indicates that the element requires a value and so the sender must place a non-empty value into this HL7 element. The value “O” marks those elements in which a value is optional. The value of optional elements may be empty. “RE” indicates conditional use and “NS” means not supported.

The Rep column contains “TRUE” if the element is repeatable and “FALSE” (or blank) if it isn’t.

The Fixed Value column contains “TRUE” if the value of this element will be fixed for every message of this type. (In this case the example value in the Ex Val column is the value.)

The Code Tbl column contains the relevant code table number.

The Example Value column contains an example value for this element.

The Implementation Notes column contains any relevant implementation notes.

##### Message Notations

A message notation presents the segment IDs in the correct order. Curly brackets ({}) surround one or more segments that are to be repeated one or more times. Square brackets ([]) surround optional segments. Using both kinds of brackets declares that the enclosed segments may appear zero or more times.

#### Network Connections

VistA connects to the designated TCP port and IP domain, listed in section 5.1.1, using TCP/IP to send HL7 messages to the NCR InterSystems HealthShare Server on the Cloud Server.

The NCR HealthShare Server returns negative commit acknowledgments for incomplete HL7 messages that it receives to the TCP port on the destination VistA system using TCP/IP.

#### NCR Patient Registration Message: ADT^A28

The ADT^A28 Registration message is triggered when the YSCL at the individual VAMC VistA system extracts Clozaril Rollup data to generate HL7 messages.

The ADT^A28 Message Type is constructed of the following HL7 segments in the order listed:

- MSH - Message Header
- EVN - Event Type
- PID - Patient Identification
- ROL - Role
- PV1 - Patient Visit
- OBX(1) – Observation/Result - Patient Clozapine Status
- OBX(2) – Observation/Result - WBC
- OBX(3) – Observation/Result - ANC
- OBX(4) – Observation/Result - Site DEA
- OBX(5) – Observation/Result – Site

The notation is: MSH, EVN, PID, ROL, PV1, OBX, OBX, OBX, OBX, OBX

##### NCR Patient Registration MSH Segment

Table: MSH Segment

| MSH Field Name                          |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value                     | Implementation Notes                                                                                   |
|-----------------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------------------------|--------------------------------------------------------------------------------------------------------|
| Field Separator                         |    1  | ST   |    1  | R     | False | True          |            | &#124;                            |                                                                                                        |
| Encoding Characters                     |    2  | ST   |    4  | R     | False | True          |            | ^~\&                              |                                                                                                        |
| Sending Application                     |    3  | HD   |  227  | R     | False |               |      0361  |                                   |                                                                                                        |
| Namespace ID                            |    1  | IS   |   20  | R     |       | True          |      0300  | YSCL CLOZ REGISTRY                | This is always “YSCL CLOZ REGISTRY”                                                                    |
| Universal ID                            |    2  | ST   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Universal ID Type                       |    3  | ID   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Sending Facility                        |    4  | HD   |  227  | R     | False |               |      0362  |                                   |                                                                                                        |
| Namespace ID                            |    1  | IS   |   20  | R     |       |               |      0300  | 501 or 501GF                      | This is the site number of the sending site, e.g., 501 (parent facility) or 501GF (satellite facility) |
| Universal ID                            |    2  | ST   |   50  | R     |       |               |            | HL7.SMA.FO-ALBANY.MED.VA.GOV:5001 | URL and port number of the sending facility HL7 server                                                 |
| Universal ID Type                       |    3  | ID   |   20  | R     |       |               |       0301 | DNS                               |                                                                                                        |
| Receiving Application                   |    5  | HD   |  227  | R     | False |               |      0361  |                                   |                                                                                                        |
| Namespace ID                            |    1  | IS   |   20  | R     |       | True          |      0300  | NCR CLOZ REGISTRY                 | This is always “NCR CLOZ REGISTRY”                                                                     |
| Universal ID                            |    2  | ST   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Universal ID Type                       |    3  | ID   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Receiving Facility                      |    6  | HD   |  227  | R     | False |               |       0362 |                                   |                                                                                                        |
| Namespace ID                            |    1  | IS   |   20  | R     |       | True          |      0300  | 3000                              | Receiving facility identifier (TBD for HealthShare server - alphanumeric)                              |
| Universal ID                            |    2  | ST   |   50  | R     |       |               |            | devazrclzpv01.dev.dss.local:5001  | URL and port number of the receiving facility HL7 server                                               |
| Universal ID Type                       |    3  | ID   |   20  | R     |       |               |       0301 | DNS                               |                                                                                                        |
| Date/Time of Message                    |    7  | TS   |   26  | R     | False |               |            |                                   |                                                                                                        |
| Time                                    |    1  | DTM  |   24  | R     |       |               |            | 20170328134602-0500               | Date/time the message was created in format YYYYMMDD[HHMM[SS]][+-ZZZZ]00                               |
| Degree of Precision                     |    2  | ID   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Security                                |    8  | ST   |   40  | NS    |       |               |            |                                   |                                                                                                        |
| Message Type                            |    9  | MSG  |   15  | R     | False |               |            |                                   |                                                                                                        |
| Message Code                            |    1  | ID   |    3  | R     |       | True          |      0076  | ADT                               | This is always “ADT”                                                                                   |
| Trigger Event                           |    2  | ID   |    3  | R     |       | True          |      0003  | A28                               | This is always “A28”                                                                                   |
| Message Structure                       |    3  | ID   |    7  | R     |       | True          |      0354  | ADT_A05                           | This is always “ADT_A05”                                                                               |
| Message Control ID                      |   10  | ST   |   20  | R     | False |               |            | 12345                             | Assigned by the HL7 package on VistA by the                                                            |
| Processing ID                           |   11  | PT   |    3  | R     | False |               |            |                                   |                                                                                                        |
| Processing ID                           |    1  | ID   |    1  | R     |       |               |      0103  | P                                 | “P” -Production  “T” - Test                                                                            |
| Processing Mode                         |    2  | ID   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Version ID                              |   12  | VID  |  973  | R     | False |               |            |                                   |                                                                                                        |
| Version ID                              |    1  | ID   |    5  | R     |       | True          |      0104  | 2.5.1                             | This is always “2.5.1”                                                                                 |
| Internationalization Code               |    2  | CE   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| International Version ID                |    3  | CE   |    0  | NS    |       |               |            |                                   |                                                                                                        |
| Sequence Number                         |   13  | NM   |   15  | NS    |       |               |            |                                   |                                                                                                        |
| Continuation Pointer                    |   14  | ST   |  180  | NS    |       |               |            |                                   |                                                                                                        |
| Accept Acknowledgment Type              |   15  | ID   |    2  | R     | False | True          |      0155  | AL                                | This is always “AL”                                                                                    |
| Application Acknowledgment Type         |   16  | ID   |    2  | R     | False | True          |      0155  | AL                                | This is always “AL”                                                                                    |
| Country Code                            |   17  | ID   |    3  | NS    |       |               |            |                                   |                                                                                                        |
| Character Set                           |   18  | ID   |   16  | NS    |       |               |            |                                   |                                                                                                        |
| Principal Language of Message           |   19  | CE   |  483  | NS    |       |               |            |                                   |                                                                                                        |
| Alternate Character Set Handling Scheme |   20  | ID   |   20  | NS    |       |               |            |                                   |                                                                                                        |
| Message Profile Identifier              |   21  | EI   |  427  | NS    |       |               |            |                                   |                                                                                                        |

##### NCR Patient Registration EVN Segment

Table: EVN Segment

| EVN Field Name          |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   | Code Tbl   | Example Value       | Implementation Notes         |
|-------------------------|-------|------|-------|-------|-------|---------------|------------|---------------------|------------------------------|
| Event Type Code         |    1  | ID   |    3  | NS    |       |               |            |                     |                              |
| Recorded Date/Time      |    2  | TS   |   26  | R     | False |               |            |                     |                              |
| Time                    |    1  | DTM  |   24  | R     |       |               |            | 20170328134602-0500 | YYYYMMDD[HHMM  [SS]][+-ZZZZ] |
| Degree of Precision     |    2  | ID   |    0  | NS    |       |               |            |                     |                              |
| Date/Time Planned Event |    3  | TS   |   26  | NS    |       |               |            |                     |                              |
| Event Reason Code       |    4  | IS   |    3  | NS    |       |               |            |                     |                              |
| Operator ID             |    5  | XCN  | 2930  | NS    |       |               |            |                     |                              |
| Event Occurred          |    6  | TS   |   26  | NS    |       |               |            |                     |                              |
| Event Facility          |    7  | HD   |  241  | NS    |       |               |            |                     |                              |

##### NCR Patient Registration PID Segment

Table: PID Segment

| PID Field Name                                     |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   | Code Tbl   | Example Value                                              | Implementation Notes                                                                                                                                                                                                              |
|----------------------------------------------------|-------|------|-------|-------|-------|---------------|------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID - PID                                       |    1  | SI   |    4  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient ID                                         |    2  | CX   | 1913  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Identifier List                            |    3  | CX   | 1912  | R     | True  |               |            |                                                            |                                                                                                                                                                                                                                   |
| ID Number                                          |    1  | ST   |   15  | R     |       |               |            | VA12345  or  111223344 or  1000720100V271387 or  100234567 | The 1st instance is the patient's Clozaril authorization number (NCR's number – 2 letters followed by 5 numbers). The 2nd instance is the patient's SSN. The 3rd instance is the patient ICN. The 4th instance is the patient DFN |
| Check Digit                                        |    2  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Check Digit Scheme                                 |    3  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Assigning Authority                                |    4  | HD   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Identifier Type Code                               |    5  | ID   |   20  | R     |       |               | 0203       | PN or SS                                                   | The 1st instance is "PN" - Patient's Clozaril authorization number. The 2nd instance is "SS" – Patient’s Social Security.                                                                                                         |
| Assigning Facility                                 |    6  | HD   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Effective Date                                     |    7  | DT   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Expiration Date                                    |    8  | DT   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Assigning Jurisdiction                             |    9  | CWE  |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Assigning Agency or Department                     |   10  | CWE  |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Alternate Patient ID - PID                         |    4  | CX   | 1913  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Name                                       |    5  | XPN  | 1044  | R     |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Family Name                                        |    1  | FN   |  194  | R     |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Surname                                            |    1  | ST   |    20 | R     |       |               |            | Doe                                                        | Last Name                                                                                                                                                                                                                         |
| Own Surname Prefix                                 |    2  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Own Surname                                        |    3  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Surname Prefix from Partner/Spouse                 |    4  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Surname from Partner/Spouse                        |    5  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Given Name                                         |    2  | ST   |   20  | R     |       |               |            | John                                                       | First Name                                                                                                                                                                                                                        |
| Second and Further Given Names or Initials Thereof |    3  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Suffix (e.g., JR or III)                           |    4  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Prefix (e.g., DR)                                  |    5  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Degree (e.g., MD)                                  |    6  | IS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name Type Code                                     |    7  | ID   |    1  | R     |       | True          | 0200       | L                                                          | This is always "L"                                                                                                                                                                                                                |
| Name Representation Code                           |    8  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name Context                                       |    9  | CE   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name Validity Range                                |   10  | DR   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name Assembly Order                                |   11  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Effective Date                                     |   12  | TS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Expiration Date                                    |   13  | TS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Professional Suffix                                |   14  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Mother's Maiden Name                               |    6  | XPN  | 1044  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Date/Time of Birth                                 |    7  | TS   |   26  | R     | False |               |            |                                                            |                                                                                                                                                                                                                                   |
| Time                                               |    1  | DTM  |   24  | R     |       |               |            | 19700101                                                   | YYYYMMDD                                                                                                                                                                                                                          |
| Degree of Precision                                |    2  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Administrative Sex                                 |    8  | IS   |    1  | R     | False |               | 0001       | F                                                          |                                                                                                                                                                                                                                   |
| Patient Alias                                      |    9  | XPN  | 1044  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Race                                               |   10  | CE   |  478  | R     | False |               |            |                                                            |                                                                                                                                                                                                                                   |
| Identifier                                         |    1  | ST   |   20  | R     |       |               | 0005       | 2028-9                                                     |                                                                                                                                                                                                                                   |
| Text                                               |    2  | ST   |   20  | R     |       |               |            | Asian                                                      | Race Identifier description                                                                                                                                                                                                       |
| Name of Coding System                              |    3  | ID   |   20  | R     |       | True          | 0396       | HL70005                                                    | HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70005”.HL7000570005L7                                                                                                                                 |
| Alternate Identifier                               |    4  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Alternate Text                                     |    5  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name of Alternate Coding System                    |    6  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Address                                    |   11  | XAD  |  513  | R     | False |               |            |                                                            |                                                                                                                                                                                                                                   |
| Street Address                                     |    1  | SAD  |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Other Designation                                  |    2  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| City                                               |    3  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| State or Province                                  |    4  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Zip or Postal Code                                 |    5  | ST   |   12  | R     |       |               |            | 33408                                                      |                                                                                                                                                                                                                                   |
| Country                                            |    6  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Address Type                                       |    7  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Other Geographic Designation                       |    8  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| County/Parish Code                                 |    9  | IS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Census Tract                                       |   10  | IS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Address Representation Code                        |   11  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Address Validity Range                             |   12  | DR   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Effective Date                                     |   13  | TS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Expiration Date                                    |   14  | TS   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| County Code                                        |   12  | IS   |    4  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Phone Number - Home                                |   13  | XTN  |  651  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Phone Number - Business                            |   14  | XTN  |  651  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Primary Language                                   |   15  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Marital Status                                     |   16  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Religion                                           |   17  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Account Number                             |   18  | CX   | 1912  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| SSN Number - Patient                               |   19  | ST   |   16  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Driver's License Number - Patient                  |   20  | DLN  |   66  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Mother's Identifier                                |   21  | CX   | 1912  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Ethnic Group                                       |   22  | CE   |  478  | R     | False |               |            |                                                            |                                                                                                                                                                                                                                   |
| Identifier                                         |    1  | ST   |   20  | R     |       |               | 0189       | U                                                          |                                                                                                                                                                                                                                   |
| Text                                               |    2  | ST   |   20  | R     |       |               |            | Unknown                                                    | Ethnic Identifier description                                                                                                                                                                                                     |
| Name of Coding System                              |    3  | ID   |   20  | R     |       | True          | 0396       | HL70189                                                    | HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70189”.                                                                                                                                               |
| Alternate Identifier                               |    4  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Alternate Text                                     |    5  | ST   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Name of Alternate Coding System                    |    6  | ID   |    0  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Birth Place                                        |   23  | ST   |  250  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Multiple Birth Indicator                           |   24  | ID   |    1  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Birth Order                                        |   25  | NM   |    2  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Citizenship                                        |   26  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Veterans Military Status                           |   27  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Nationality                                        |   28  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Death Date and Time                        |   29  | TS   |   26  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Patient Death Indicator                            |   30  | ID   |    1  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Identity Unknown Indicator                         |   31  | ID   |    1  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Identity Reliability Code                          |   32  | IS   |   20  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Last Update Date/Time                              |   33  | TS   |   26  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Last Update Facility                               |   34  | HD   |  241  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Species Code                                       |   35  | CE   |  478  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Breed Code                                         |   36  | CE   |  478  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Strain                                             |   37  | ST   |   80  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Production Class Code                              |   38  | CE   |  483  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |
| Tribal Citizenship                                 |   39  | CWE  |  705  | NS    |       |               |            |                                                            |                                                                                                                                                                                                                                   |

##### NCR Patient Registration ROL Segment

| ROL Field Name                                     |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   | Code Tbl   | Example Value         | Implementation Notes                                                                                                                   |
|----------------------------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Role Instance ID                                   |    1  | EI   |  424  | NS    |       |               |            |                       |                                                                                                                                        |
| Action Code                                        |    2  | ID   |    2  | R     | False |               | 0287       | UP                    | This is always “UP”                                                                                                                    |
| Role-ROL                                           |    3  | CE   |  478  | R     | False |               |            |                       |                                                                                                                                        |
| Identifier                                         |    1  | ST   |   20  | R     |       | True          | 0443       | PPRX PRPX             | This is always “PRX”. Need to add “PRX” to table 0443                                                                                  |
| Text                                               |    2  | ST   |   30  | R     |       | True          |            | Prescribing Physician | This is always “Prescribing Physician”                                                                                                 |
| Name of Coding System                              |    3  | ID   |   20  | R     |       | True          | 0396       | HL70443               | HL7 Defined Code where nnnn is the HL7 table number 0443. This is always “HL70443”.                                                    |
| Alternate Identifier                               |    4  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Alternate Text                                     |    5  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name of Alternate Coding System                    |    6  | ID   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Role Person                                        |    4  | XCN  | 2930  | R     | True  |               |            |                       |                                                                                                                                        |
| ID Number                                          |    1  | ST   |   15  | R     |       |               |            | AR7071296             | 1st instance: This is the DEA number of the prescribing physician.  2nd instance: This is the NPI number of the prescribing physician. |
| Family Name                                        |    2  | FN   |  194  | R     |       |               |            |                       |                                                                                                                                        |
| Surname                                            |    1  | ST   |   50  | R     |       |               |            | Lastname              | Last name of the prescribing physician                                                                                                 |
| Own Surname Prefix                                 |    2  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Own Surname                                        |    3  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Surname Prefix from Partner/Spouse                 |    4  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Surname from Partner/Spouse                        |    5  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Given Name                                         |    3  | ST   |   30  | R     |       |               |            | Firstname             | First name of the prescribing physician                                                                                                |
| Second and Further Given Names or Initials Thereof |    4  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Suffix (e.g., JR or III)                           |    5  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Prefix (e.g., DR)                                  |    6  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Degree (e.g., MD)                                  |    7  | IS   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Source Table                                       |    8  | IS   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Assigning Authority                                |    9  | HD   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name Type Code                                     |   10  | ID   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Identifier Check Digit                             |   11  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Check Digit Scheme                                 |   12  | ID   |    0  |       |       |               |            |                       |                                                                                                                                        |
| Identifier Type Code                               |   13  | ID   |    3  | R     |       |               | 0203       | DEA                   | 1st instance: This is "DEA". Need to add “DEA” to table 0203  2nd instance: This is "NPI".                                             |
| Assigning Facility                                 |   14  | HD   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name Representation Code                           |   15  | ID   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name Context                                       |   16  | CE   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name Validity Range                                |   17  | DR   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Name Assembly Order                                |   18  | ID   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Effective Date                                     |   19  | TS   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Expiration Date                                    |   20  | TS   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Professional Suffix                                |   21  | ST   |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Assigning Jurisdiction                             |   22  | CWE  |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Assigning Agency or Department                     |   23  | CWE  |    0  | NS    |       |               |            |                       |                                                                                                                                        |
| Role Begin Date/Time                               |    5  | TS   |   26  | NS    |       |               |            |                       |                                                                                                                                        |
| Role End Date/Time                                 |    6  | TS   |   26  | NS    |       |               |            |                       |                                                                                                                                        |
| Role Duration                                      |    7  | CE   |  483  | NS    |       |               |            |                       |                                                                                                                                        |
| Role Action Reason                                 |    8  | CE   |  483  | NS    |       |               |            |                       |                                                                                                                                        |
| Provider Type                                      |    9  | CE   |  483  | NS    |       |               |            |                       |                                                                                                                                        |
| Organization Unit Type                             |   10  | CE   |  483  | NS    |       |               |            |                       |                                                                                                                                        |
| Office/Home Address/Birthplace                     |   11  | XAD  |  513  | NS    |       |               |            |                       |                                                                                                                                        |
| Phone                                              |   12  | XTN  |  651  | NS    |       |               |            |                       |                                                                                                                                        |

##### NCR Patient Registration PV1 Segment

Table: PV1 Segment

| PV1 Field Name            |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes              |
|---------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|-----------------------------------|
| Set ID - PV1              |    1  | SI   |    4  | NS    |       |               |            |                 |                                   |
| Patient Class             |    2  | IS   |    1  | R     | False |               |      0004  | O or I          | “O” - Outpatient  “I” - Inpatient |
| Assigned Patient Location |    3  | PL   | 1230  | NS    |       |               |            |                 |                                   |
| Admission Type            |    4  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Preadmit Number           |    5  | CX   | 1912  | NS    |       |               |            |                 |                                   |
| Prior Patient Location    |    6  | PL   | 1230  | NS    |       |               |            |                 |                                   |
| Attending Doctor          |    7  | XCN  | 2930  | NS    |       |               |            |                 |                                   |
| Referring Doctor          |    8  | XCN  | 2930  | NS    |       |               |            |                 |                                   |
| Consulting Doctor         |    9  | XCN  | 2945  | NS    |       |               |            |                 |                                   |
| Hospital Service          |   10  | IS   |    3  | NS    |       |               |            |                 |                                   |
| Temporary Location        |   11  | PL   | 1230  | NS    |       |               |            |                 |                                   |
| Preadmit Test Indicator   |   12  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Re-admission Indicator    |   13  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Admit Source              |   14  | IS   |    6  | NS    |       |               |            |                 |                                   |
| Ambulatory Status         |   15  | IS   |    2  | NS    |       |               |            |                 |                                   |
| VIP Indicator             |   16  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Admitting Doctor          |   17  | XCN  | 2930  | NS    |       |               |            |                 |                                   |
| Patient Type              |   18  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Visit Number              |   19  | CX   | 1912  | NS    |       |               |            |                 |                                   |
| Financial Class           |   20  | FC   |   50  | NS    |       |               |            |                 |                                   |
| Charge Price Indicator    |   21  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Courtesy Code             |   22  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Credit Rating             |   23  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Contract Code             |   24  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Contract Effective Date   |   25  | DT   |    8  | NS    |       |               |            |                 |                                   |
| Contract Amount           |   26  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Contract Period           |   27  | NM   |    3  | NS    |       |               |            |                 |                                   |
| Interest Code             |   28  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Transfer to Bad Debt Code |   29  | IS   |    4  | NS    |       |               |            |                 |                                   |
| Transfer to Bad Debt Date |   30  | DT   |    8  | NS    |       |               |            |                 |                                   |
| Bad Debt Agency Code      |   31  | IS   |   10  | NS    |       |               |            |                 |                                   |
| Bad Debt Transfer Amount  |   32  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Bad Debt Recovery Amount  |   33  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Delete Account Indicator  |   34  | IS   |    1  | NS    |       |               |            |                 |                                   |
| Delete Account Date       |   35  | DT   |    8  | NS    |       |               |            |                 |                                   |
| Discharge Disposition     |   36  | IS   |    3  | NS    |       |               |            |                 |                                   |
| Discharged to Location    |   37  | DLD  |   47  | NS    |       |               |            |                 |                                   |
| Diet Type                 |   38  | CE   |  483  | NS    |       |               |            |                 |                                   |
| Servicing Facility        |   39  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Bed Status                |   40  | IS   |    1  | NS    |       |               |            |                 |                                   |
| Account Status            |   41  | IS   |    2  | NS    |       |               |            |                 |                                   |
| Pending Location          |   42  | PL   | 1230  | NS    |       |               |            |                 |                                   |
| Prior Temporary Location  |   43  | PL   | 1230  | NS    |       |               |            |                 |                                   |
| Admit Date/Time           |   44  | TS   |   26  | NS    |       |               |            |                 |                                   |
| Discharge Date/Time       |   45  | TS   |   26  | NS    |       |               |            |                 |                                   |
| Current Patient Balance   |   46  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Total Charges             |   47  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Total Adjustments         |   48  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Total Payments            |   49  | NM   |   12  | NS    |       |               |            |                 |                                   |
| Alternate Visit ID        |   50  | CX   | 1912  | NS    |       |               |            |                 |                                   |
| Visit Indicator           |   51  | IS   |    1  | NS    |       |               |            |                 |                                   |
| Other Healthcare Provider |   52  | XCN  | 2945  | NS    |       |               |            |                 |                                   |

##### NCR Patient Registration OBX(1) Segment

Table: OBX(1) Segment

| OBX(1) Field Name                        |   Seq | DT     |    Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes                                                  |
|------------------------------------------|-------|--------|--------|-------|-------|---------------|------------|-----------------|-----------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |     4  | R     | False | True          |            | 1               | This is always “1” to indicate the 1  st  instance of the OBX segment |
| Value Type                               |    2  | ID     |     2  | R     | False | True          |      0125  | CE              | This is always “CE” in the 1  st  instance of the OBX segment         |
| Observation Identifier                   |    3  | CE     |   478  | R     | False |               |            |                 |                                                                       |
| Identifier                               |    1  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Text                                     |    2  | ST     |    20  | R     |       | True          |            | PTSTAT          | This is always “PTSTAT” in the 1  st  OBX instance                    |
| Name of Coding System                    |    3  | ID     |     0  | NS    |       |               |            |                 |                                                                       |
| Alternate Identifier                     |    4  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Alternate Text                           |    5  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Name of Alternate Coding System          |    6  | ID     |     0  | NS    |       |               |            |                 |                                                                       |
| Observation Sub-ID                       |    4  | ST     |    20  | NS    |       |               |            |                 |                                                                       |
| Observation Value                        |    5  | CE     | 99999  | R     | False |               |            |                 |                                                                       |
| Identifier                               |    1  | ST     |     1  | R     |       |               |            | A or D          | Patient status:  “A” – Active  “D” - Discontinued                     |
| Text                                     |    2  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Name of Coding System                    |    3  | ID     |     0  | NS    |       |               |            |                 |                                                                       |
| Alternate Identifier                     |    4  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Alternate Text                           |    5  | ST     |     0  | NS    |       |               |            |                 |                                                                       |
| Name of Alternate Coding System          |    6  | ID     |     0  | NS    |       |               |            |                 |                                                                       |
| Units                                    |    6  | CE     |   483  | NS    |       |               |            |                 |                                                                       |
| References Range                         |    7  | ST     |    60  | NS    |       |               |            |                 |                                                                       |
| Abnormal Flags                           |    8  | IS     |     5  | NS    |       |               |            |                 |                                                                       |
| Probability                              |    9  | NM     |     5  | NS    |       |               |            |                 |                                                                       |
| Nature of Abnormal Test                  |   10  | ID     |     2  | NS    |       |               |            |                 |                                                                       |
| Observation Result Status                |   11  | ID     |     1  | R     | False | True          |      0085  | F               | This is always “F”                                                    |
| Effective Date of Reference Range Values |   12  | TS     |    26  | NS    |       |               |            |                 |                                                                       |
| User Defined Access Checks               |   13  | ST     |    20  | NS    |       |               |            |                 |                                                                       |
| Date/Time of the Observation             |   14  | TS     |    26  | NS    |       |               |            |                 |                                                                       |
| Producer's Reference                     |   15  | CE     |   483  | NS    |       |               |            |                 |                                                                       |
| Responsible Observer                     |   16  | XCN    |  2930  | NS    |       |               |            |                 |                                                                       |
| Observation Method                       |   17  | CE     |   483  | NS    |       |               |            |                 |                                                                       |
| Equipment Instance Identifier            |   18  | EI     |   427  | NS    |       |               |            |                 |                                                                       |
| Date/Time of the Analysis                |   19  | TS     |    26  | NS    |       |               |            |                 |                                                                       |
| Reserved for harmonization with V2.6     |   20  | varies |     1  | NS    |       |               |            |                 |                                                                       |
| Reserved for harmonization with V2.6     |   21  | varies |     1  | NS    |       |               |            |                 |                                                                       |
| Reserved for harmonization with V2.6     |   22  | varies |     1  | NS    |       |               |            |                 |                                                                       |
| Performing Organization Name             |   23  | XON    |   567  | NS    |       |               |            |                 |                                                                       |
| Performing Organization Address          |   24  | XAD    |   631  | NS    |       |               |            |                 |                                                                       |
| Performing Organization Medical Director |   25  | XCN    |  3002  | NS    |       |               |            |                 |                                                                       |

##### NCR Patient Registration OBX(2) Segment

Table: OBX(2) Segment

| OBX(2) Field Name                        |   Seq | DT     |    Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes                                               |
|------------------------------------------|-------|--------|--------|-------|-------|---------------|------------|-----------------|--------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |     4  | R     | False | True          |            | 2               | This is always “2” to indicate the 2nd instance of the OBX segment |
| Value Type                               |    2  | ID     |     2  | R     | False | True          |      0125  | CE              | This is always “CE” in the 2nd instance of the OBX segment         |
| Observation Identifier                   |    3  | CE     |   478  | R     | False |               |            |                 |                                                                    |
| Identifier                               |    1  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Text                                     |    2  | ST     |    20  | R     |       | True          |            | PTSTAT          | This is always “Dispense Frequency” in the 2nd OBX instance        |
| Name of Coding System                    |    3  | ID     |     0  | NS    |       |               |            |                 |                                                                    |
| Alternate Identifier                     |    4  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Alternate Text                           |    5  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Name of Alternate Coding System          |    6  | ID     |     0  | NS    |       |               |            |                 |                                                                    |
| Observation Sub-ID                       |    4  | ST     |    20  | NS    |       |               |            |                 |                                                                    |
| Observation Value                        |    5  | CE     | 99999  | R     | False |               |            |                 |                                                                    |
| Identifier                               |    1  | ST     |     1  | R     |       |               |            | 7 Days          | Dispense Frequency:  7 Days, 14 Days, or 28 Days.                  |
| Text                                     |    2  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Name of Coding System                    |    3  | ID     |     0  | NS    |       |               |            |                 |                                                                    |
| Alternate Identifier                     |    4  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Alternate Text                           |    5  | ST     |     0  | NS    |       |               |            |                 |                                                                    |
| Name of Alternate Coding System          |    6  | ID     |     0  | NS    |       |               |            |                 |                                                                    |
| Units                                    |    6  | CE     |   483  | NS    |       |               |            |                 |                                                                    |
| References Range                         |    7  | ST     |    60  | NS    |       |               |            |                 |                                                                    |
| Abnormal Flags                           |    8  | IS     |     5  | NS    |       |               |            |                 |                                                                    |
| Probability                              |    9  | NM     |     5  | NS    |       |               |            |                 |                                                                    |
| Nature of Abnormal Test                  |   10  | ID     |     2  | NS    |       |               |            |                 |                                                                    |
| Observation Result Status                |   11  | ID     |     1  | R     | False | True          |      0085  | F               | This is always “F”                                                 |
| Effective Date of Reference Range Values |   12  | TS     |    26  | NS    |       |               |            |                 |                                                                    |
| User Defined Access Checks               |   13  | ST     |    20  | NS    |       |               |            |                 |                                                                    |
| Date/Time of the Observation             |   14  | TS     |    26  | NS    |       |               |            |                 |                                                                    |
| Producer's Reference                     |   15  | CE     |   483  | NS    |       |               |            |                 |                                                                    |
| Responsible Observer                     |   16  | XCN    |  2930  | NS    |       |               |            |                 |                                                                    |
| Observation Method                       |   17  | CE     |   483  | NS    |       |               |            |                 |                                                                    |
| Equipment Instance Identifier            |   18  | EI     |   427  | NS    |       |               |            |                 |                                                                    |
| Date/Time of the Analysis                |   19  | TS     |    26  | NS    |       |               |            |                 |                                                                    |
| Reserved for harmonization with V2.6     |   20  | varies |     1  | NS    |       |               |            |                 |                                                                    |
| Reserved for harmonization with V2.6     |   21  | varies |     1  | NS    |       |               |            |                 |                                                                    |
| Reserved for harmonization with V2.6     |   22  | varies |     1  | NS    |       |               |            |                 |                                                                    |
| Performing Organization Name             |   23  | XON    |   567  | NS    |       |               |            |                 |                                                                    |
| Performing Organization Address          |   24  | XAD    |   631  | NS    |       |               |            |                 |                                                                    |
| Performing Organization Medical Director |   25  | XCN    |  3002  | NS    |       |               |            |                 |                                                                    |

##### NCR Patient Registration OBX(3) Segment

Table: OBX(3) Segment

| OBX(3) Field Name                        |   Seq | DT     |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value       | Implementation Notes                                                                               |
|------------------------------------------|-------|--------|-------|-------|-------|---------------|------------|---------------------|----------------------------------------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |    4  | R     | False | True          |            | 3                   | This is always “3” to indicate the 3rd OBX instance                                                |
| Value Type                               |    2  | ID     |    2  | R     | False |               |      0125  | CE                  | This is always “CE” in the 3rd OBX instance                                                        |
| Observation Identifier                   |    3  | CE     |  478  | R     | False |               |            |                     |                                                                                                    |
| Identifier                               |    1  | ST     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Text                                     |    2  | ST     |   20  | R     |       | True          |            | WBC                 | This is always “WBC” in the 3rd OBX instance                                                       |
| Name of Coding System                    |    3  | ID     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Alternate Identifier                     |    4  | ST     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Alternate Text                           |    5  | ST     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Name of Alternate Coding System          |    6  | ID     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Observation Sub-ID                       |    4  | ST     |   20  | NS    |       |               |            |                     |                                                                                                    |
| Observation Value                        |    5  | NM     |   20  | R     | False |               |            | 7800                | The White Blood Count result in the format expected by the manufacturer of the drug (whole number) |
| Units                                    |    6  | CE     |  483  | NS    |       |               |            |                     |                                                                                                    |
| References Range                         |    7  | ST     |   60  | NS    |       |               |            |                     |                                                                                                    |
| Abnormal Flags                           |    8  | IS     |    5  | NS    |       |               |            |                     |                                                                                                    |
| Probability                              |    9  | NM     |    5  | NS    |       |               |            |                     |                                                                                                    |
| Nature of Abnormal Test                  |   10  | ID     |    2  | NS    |       |               |            |                     |                                                                                                    |
| Observation Result Status                |   11  | ID     |    1  | R     | False | True          |      0085  | F                   | This is always “F”                                                                                 |
| Effective Date of Reference Range Values |   12  | TS     |   26  | NS    |       |               |            |                     |                                                                                                    |
| User Defined Access Checks               |   13  | ST     |   20  | NS    |       |               |            |                     |                                                                                                    |
| Date/Time of the Observation             |   14  | TS     |   26  | R     | False |               |            |                     |                                                                                                    |
| Time                                     |    1  | DTM    |   24  | R     |       |               |            | 20170328134602-0500 | Date and time of blood sample collection for the WBC Test in the format YYYYMMDD[HHMM[SS]][+-ZZZZ] |
| Degree of Precision                      |    2  | ID     |    0  | NS    |       |               |            |                     |                                                                                                    |
| Producer's Reference                     |   15  | CE     |  483  | NS    |       |               |            |                     |                                                                                                    |
| Responsible Observer                     |   16  | XCN    | 2930  | NS    |       |               |            |                     |                                                                                                    |
| Observation Method                       |   17  | CE     |  483  | NS    |       |               |            |                     |                                                                                                    |
| Equipment Instance Identifier            |   18  | EI     |  427  | NS    |       |               |            |                     |                                                                                                    |
| Date/Time of the Analysis                |   19  | TS     |   26  | NS    |       |               |            |                     |                                                                                                    |
| Reserved for harmonization with V2.6     |   20  | varies |    1  | NS    |       |               |            |                     |                                                                                                    |
| Reserved for harmonization with V2.6     |   21  | varies |    1  | NS    |       |               |            |                     |                                                                                                    |
| Reserved for harmonization with V2.6     |   22  | varies |    1  | NS    |       |               |            |                     |                                                                                                    |
| Performing Organization Name             |   23  | XON    |  567  | NS    |       |               |            |                     |                                                                                                    |
| Performing Organization Address          |   24  | XAD    |  631  | NS    |       |               |            |                     |                                                                                                    |
| Performing Organization Medical Director |   25  | XCN    | 3002  | NS    |       |               |            |                     |                                                                                                    |

##### NCR Patient Registration OBX(4) Segment

Table: OBX(4) Segment

| OBX(4) Field Name                        |   Seq | DT     |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value       | Implementation Notes                                                                         |
|------------------------------------------|-------|--------|-------|-------|-------|---------------|------------|---------------------|----------------------------------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |    4  | R     | False | True          |            | 4                   | This is always “4” to indicate the 4th OBX instance                                          |
| Value Type                               |    2  | ID     |    2  | R     | False | True          |      0125  | CE                  | This is always “CE” in the 4th OBX instance                                                  |
| Observation Identifier                   |    3  | CE     |  478  | R     | False |               |            |                     |                                                                                              |
| Identifier                               |    1  | ST     |    0  | NS    |       |               |            |                     |                                                                                              |
| Text                                     |    2  | ST     |   20  | R     |       | True          |            | ANC                 | This is always “ANC” in the 4th OBX instance                                                 |
| Name of Coding System                    |    3  | ID     |    0  | NS    |       |               |            |                     |                                                                                              |
| Alternate Identifier                     |    4  | ST     |    0  | NS    |       |               |            |                     |                                                                                              |
| Alternate Text                           |    5  | ST     |    0  | NS    |       |               |            |                     |                                                                                              |
| Name of Alternate Coding System          |    6  | ID     |    0  | NS    |       |               |            |                     |                                                                                              |
| Observation Sub-ID                       |    4  | ST     |   20  | NS    |       |               |            |                     |                                                                                              |
| Observation Value                        |    5  | NM     |   20  | R     | False |               |            | 300                 | ANC test result                                                                              |
| Units                                    |    6  | CE     |  483  | NS    |       |               |            |                     |                                                                                              |
| References Range                         |    7  | ST     |   60  | NS    |       |               |            |                     |                                                                                              |
| Abnormal Flags                           |    8  | IS     |    5  | NS    |       |               |            |                     |                                                                                              |
| Probability                              |    9  | NM     |    5  | NS    |       |               |            |                     |                                                                                              |
| Nature of Abnormal Test                  |   10  | ID     |    2  | NS    |       |               |            |                     |                                                                                              |
| Observation Result Status                |   11  | ID     |    1  | R     | False | True          |      0085  | F                   | This is always “F”                                                                           |
| Effective Date of Reference Range Values |   12  | TS     |   26  | NS    |       |               |            |                     |                                                                                              |
| User Defined Access Checks               |   13  | ST     |   20  | NS    |       |               |            |                     |                                                                                              |
| Date/Time of the Observation             |   14  | TS     |   26  | R     | False |               |            |                     |                                                                                              |
| Time                                     |    1  | DTM    |   24  | R     |       |               |            | 20170328134602-0500 | Date of the blood sample collection for the ANC test in the format YYYYMMDD[HHMM[SS]][+-ZZZZ |
| Degree of Precision                      |    2  | ID     |    0  | NS    |       |               |            |                     |                                                                                              |
| Producer's Reference                     |   15  | CE     |  483  | NS    |       |               |            |                     |                                                                                              |
| Responsible Observer                     |   16  | XCN    | 2930  | NS    |       |               |            |                     |                                                                                              |
| Observation Method                       |   17  | CE     |  483  | NS    |       |               |            |                     |                                                                                              |
| Equipment Instance Identifier            |   18  | EI     |  427  | NS    |       |               |            |                     |                                                                                              |
| Date/Time of the Analysis                |   19  | TS     |   26  | NS    |       |               |            |                     |                                                                                              |
| Reserved for harmonization with V2.6     |   20  | varies |    1  | NS    |       |               |            |                     |                                                                                              |
| Reserved for harmonization with V2.6     |   21  | varies |    1  | NS    |       |               |            |                     |                                                                                              |
| Reserved for harmonization with V2.6     |   22  | varies |    1  | NS    |       |               |            |                     |                                                                                              |
| Performing Organization Name             |   23  | XON    |  567  | NS    |       |               |            |                     |                                                                                              |
| Performing Organization Address          |   24  | XAD    |  631  | NS    |       |               |            |                     |                                                                                              |
| Performing Organization Medical Director |   25  | XCN    | 3002  | NS    |       |               |            |                     |                                                                                              |

##### NCR Patient Registration OBX(5) Segment

Table: OBX(5) Segment

| OBX(5) Field Name                        |   Seq | DT     |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value       | Implementation Notes                                                                                                          |
|------------------------------------------|-------|--------|-------|-------|-------|---------------|------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |    4  | R     | False | True          |            | 5                   | This is always “5” to indicate the 5  th  OBX instance                                                                        |
| Value Type                               |    2  | ID     |    2  | R     | False | True          |      0125  | CE                  | This is always “CE” in the 5  th  OBX instance                                                                                |
| Observation Identifier                   |    3  | CE     |  478  | R     | False |               |            |                     |                                                                                                                               |
| Identifier                               |    1  | ST     |    0  | NS    |       |               |            |                     |                                                                                                                               |
| Text                                     |    2  | ST     |  199  | R     |       |               |            | Facility DEA number | DEA number type description: "Facility DEA number" or "Clinic DEA number" or Pharmacy DEA number" or "Pharmacist DEA number". |
| Name of Coding System                    |    3  | ID     |    0  | NS    |       |               |            |                     |                                                                                                                               |
| Alternate Identifier                     |    4  | ST     |    0  | NS    |       |               |            |                     |                                                                                                                               |
| Alternate Text                           |    5  | ST     |    0  | NS    |       |               |            |                     |                                                                                                                               |
| Name of Alternate Coding System          |    6  | ID     |    0  | NS    |       |               |            |                     |                                                                                                                               |
| Observation Sub-ID                       |    4  | ST     |   20  | NS    |       |               |            |                     |                                                                                                                               |
| Observation Value                        |    5  | ST     |   50  | R     | False |               |            | AG9698296           | This is a DEA number (in the format 2 letters and 7 numbers)                                                                  |
| Units                                    |    6  | CE     |  483  | NS    |       |               |            |                     |                                                                                                                               |
| References Range                         |    7  | ST     |   60  | NS    |       |               |            |                     |                                                                                                                               |
| Abnormal Flags                           |    8  | IS     |    5  | NS    |       |               |            |                     |                                                                                                                               |
| Probability                              |    9  | NM     |    5  | NS    |       |               |            |                     |                                                                                                                               |
| Nature of Abnormal Test                  |   10  | ID     |    2  | NS    |       |               |            |                     |                                                                                                                               |
| Observation Result Status                |   11  | ID     |    1  | R     | False | True          |      0085  | F                   | This is always “F”                                                                                                            |
| Effective Date of Reference Range Values |   12  | TS     |   26  | NS    |       |               |            |                     |                                                                                                                               |
| User Defined Access Checks               |   13  | ST     |   20  | NS    |       |               |            |                     |                                                                                                                               |
| Date/Time of the Observation             |   14  | TS     |   26  | NS    |       |               |            |                     |                                                                                                                               |
| Producer's Reference                     |   15  | CE     |  483  | NS    |       |               |            |                     |                                                                                                                               |
| Responsible Observer                     |   16  | XCN    | 2930  | NS    |       |               |            |                     |                                                                                                                               |
| Observation Method                       |   17  | CE     |  483  | NS    |       |               |            |                     |                                                                                                                               |
| Equipment Instance Identifier            |   18  | EI     |  427  | NS    |       |               |            |                     |                                                                                                                               |
| Date/Time of the Analysis                |   19  | TS     |   26  | NS    |       |               |            |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     |   20  | varies |    1  | NS    |       |               |            |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     |   21  | varies |    1  | NS    |       |               |            |                     |                                                                                                                               |
| Reserved for harmonization with V2.6     |   22  | varies |    1  | NS    |       |               |            |                     |                                                                                                                               |
| Performing Organization Name             |   23  | XON    |  567  | NS    |       |               |            |                     |                                                                                                                               |
| Performing Organization Address          |   24  | XAD    |  631  | NS    |       |               |            |                     |                                                                                                                               |
| Performing Organization Medical Director |   25  | XCN    | 3002  | NS    |       |               |            |                     |                                                                                                                               |

##### NCR Patient Registration OBX(6) Segment

Table: OBX(6) Segment

| OBX(6) Field Name                        |   Seq | DT     |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value              | Implementation Notes                                                                                                                                 |
|------------------------------------------|-------|--------|-------|-------|-------|---------------|------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID - OBX                             |    1  | SI     |    4  | R     | False | True          |            | 6                          | This is always “6” to indicate the 6  th  OBX instance                                                                                               |
| Value Type                               |    2  | ID     |    2  | R     | False | True          |      0125  | CE                         | This is always “CE” in the 6  th  OBX instance                                                                                                       |
| Observation Identifier                   |    3  | CE     |  478  | R     | False |               |            |                            |                                                                                                                                                      |
| Identifier                               |    1  | ST     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Text                                     |    2  | ST     |   20  | R     |       | True          |            | SITELOC                    | This is always “SITELOC” in the 6  th  OBX instance                                                                                                  |
| Name of Coding System                    |    3  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Alternate Identifier                     |    4  | ST     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Alternate Text                           |    5  | ST     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Name of Alternate Coding System          |    6  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Observation Sub-ID                       |    4  | ST     |   20  | NS    |       |               |            |                            |                                                                                                                                                      |
| Observation Value                        |    5  | ST     |   50  | R     | False |               |            | 22                         | Pointer to QUIC SORT DATA FILE (#736), that is the pointer to the Hospital Location (file #44) which is associated with the Ward Location (file #42) |
| Units                                    |    6  | CE     |  483  | NS    |       |               |            |                            |                                                                                                                                                      |
| References Range                         |    7  | ST     |   60  | NS    |       |               |            |                            |                                                                                                                                                      |
| Abnormal Flags                           |    8  | IS     |    5  | NS    |       |               |            |                            |                                                                                                                                                      |
| Probability                              |    9  | NM     |    5  | NS    |       |               |            |                            |                                                                                                                                                      |
| Nature of Abnormal Test                  |   10  | ID     |    2  | NS    |       |               |            |                            |                                                                                                                                                      |
| Observation Result Status                |   11  | ID     |    1  | R     | False | True          |      0085  | F                          | This is always “F”                                                                                                                                   |
| Effective Date of Reference Range Values |   12  | TS     |   26  | NS    |       |               |            |                            |                                                                                                                                                      |
| User Defined Access Checks               |   13  | ST     |   20  | NS    |       |               |            |                            |                                                                                                                                                      |
| Date/Time of the Observation             |   14  | TS     |   26  | NS    |       |               |            |                            |                                                                                                                                                      |
| Producer's Reference                     |   15  | CE     |  483  | NS    |       |               |            |                            |                                                                                                                                                      |
| Responsible Observer                     |   16  | XCN    | 2930  | NS    |       |               |            |                            |                                                                                                                                                      |
| Observation Method                       |   17  | CE     |  483  | NS    |       |               |            |                            |                                                                                                                                                      |
| Equipment Instance Identifier            |   18  | EI     |  427  | NS    |       |               |            |                            |                                                                                                                                                      |
| Date/Time of the Analysis                |   19  | TS     |   26  | NS    |       |               |            |                            |                                                                                                                                                      |
| Reserved for harmonization with V2.6     |   20  | varies |    1  | NS    |       |               |            |                            |                                                                                                                                                      |
| Reserved for harmonization with V2.6     |   21  | varies |    1  | NS    |       |               |            |                            |                                                                                                                                                      |
| Reserved for harmonization with V2.6     |   22  | VARIES |  567  | NS    |       |               |            |                            |                                                                                                                                                      |
| Performing Organization Name             |   23  | XON    |  179  | R     | False |               |            |                            |                                                                                                                                                      |
| Organization Name                        |    1  | ST     |   50  | R     |       |               |            | VAMC Name                  | Site Name                                                                                                                                            |
| Organization Name Type Code              |    2  | IS     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| ID Number                                |    3  | NM     |    0  | B     |       |               |            |                            |                                                                                                                                                      |
| Check Digit                              |    4  | NM     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Check Digit Scheme                       |    5  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Assigning Authority                      |    6  | HD     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Identifier Type Code                     |    7  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Assigning Facility                       |    8  | HD     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Name Representation Code                 |    9  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Organization Identifier                  |   10  | ST     |   20  | R     |       |               |            | 402                        | Site Number                                                                                                                                          |
| Performing Organization Address          |   24  | XAD    |  631  | R     | False |               |            |                            |                                                                                                                                                      |
| Street Address                           |    1  | SAD    |  134  | R     |       |               |            |                            |                                                                                                                                                      |
| Street or Mailing Address                |    1  | ST     |  120  | R     |       |               |            | 123 Main St.               | The 1st Line of the street address of the VAMC where patient has been treated                                                                        |
| Street Name                              |    2  | ST     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Dwelling Number                          |    3  | ST     |   12  | O     |       |               |            |                            |                                                                                                                                                      |
| Other Designation                        |    2  | ST     |  120  | RE    |       |               |            | 2nd line of street address | The 2nd Line of the street address of the VAMC where patient has been treated, if available                                                          |
| City                                     |    3  | ST     |   50  | R     |       | 1             |            | North Palm Beach address   | City where the VAMC is located                                                                                                                       |
| State or Province                        |    4  | ST     |   50  | R     |       | 1             |            | FL                         | VACM state                                                                                                                                           |
| Zip or Postal Code                       |    5  | ST     |   12  | R     |       | 1             |            | 33408                      | VAMC zip code                                                                                                                                        |
| Country                                  |    6  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Address Type                             |    7  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Other Geographic Designation             |    8  | ST     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| County/Parish Code                       |    9  | IS     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Census Tract                             |   10  | IS     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Address Representation Code              |   11  | ID     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Address Validity Range                   |   12  | DR     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Effective Date                           |   13  | TS     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Expiration Date                          |   14  | TS     |    0  | NS    |       |               |            |                            |                                                                                                                                                      |
| Performing Organization Medical Director |   25  | XCN    | 3002  | NS    |       |               |            |                            |                                                                                                                                                      |

#### NCR Clozapine Dispense Message: RDE^O11

The RDE^O11 Clozapine Dispense message is triggered when the YSCL at the individual VAMC VistA system extracts Clozaril Rollup data to generate HL7 messages.

The RDE^O11 Message Type is constructed of the following HL7 segments in the order as listed:

- MSH – Message Header
- PID – Patient Identification
- PV1 – Patient Visit
- ORC – Common Order
- RXE – Pharmacy/Treatment Encoded Order
- TQ1 – Timing/Quantity
- RXR – Pharmacy/Treatment Route
- PV1 – Patient Visit

The notation is: MSH, PID, PV1, ORC, RXE, {TQ1}, RXR

##### NCR Clozapine Dispense MSH Segment

Table: MSH Segment

| MSH Field Name                          |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value                       | Implementation Notes                                                                                   |
|-----------------------------------------|-------|------|-------|-------|-------|---------------|------------|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Field Separator                         |     1 | ST   |     1 | R     | False | True          |            | &#124;                              |                                                                                                        |
| Encoding Characters                     |     2 | ST   |     4 | R     | False | True          |            | ^~\&                                |                                                                                                        |
| Sending Application                     |     3 | HD   |   227 | R     | False |               |       0361 |                                     |                                                                                                        |
| Namespace ID                            |     1 | IS   |    20 | R     |       | True          |       0300 | YSCL CLOZ REGISTRY                  | This is always “YSCL CLOZ REGISTRY”                                                                    |
| Universal ID                            |     2 | ST   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Universal ID Type                       |     3 | ID   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Sending Facility                        |     4 | HD   |   227 | R     | False |               |       0362 |                                     |                                                                                                        |
| Namespace ID                            |     1 | IS   |    20 | R     |       |               |       0300 | 501 or 501GF                        | This is the site number of the sending site, e.g., 501 (parent facility) or 501GF (satellite facility) |
| Universal ID                            |     2 | ST   |    50 | R     |       |               |            | HL7.SMA.FO-  ALBANY.MED.VA.GOV:5001 | URL and port number of the sending facility HL7 server                                                 |
| Universal ID Type                       |     3 | ID   |    20 | R     |       |               |       0301 | DNS                                 |                                                                                                        |
| Receiving Application                   |     5 | HD   |   227 | R     | False |               |       0361 |                                     |                                                                                                        |
| Namespace ID                            |     1 | IS   |    20 | R     |       | True          |       0300 | NCR CLOZ REGISTRY                   | This is always “NCR CLOZ REGISTRY”                                                                     |
| Universal ID                            |     2 | ST   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Universal ID Type                       |     3 | ID   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Receiving Facility                      |     6 | HD   |   227 | R     | False |               |       0362 |                                     |                                                                                                        |
| Namespace ID                            |     1 | IS   |    20 | R     |       | True          |       0300 | 3000                                | Receiving facility identifier (TBD for HealthShare server - alphanumeric)                              |
| Universal ID                            |     2 | ST   |    50 | R     |       |               |            | devazrclzpv01.dev.dss.local:5001    | URL and port number of the receiving facility HL7 server                                               |
| Universal ID Type                       |     3 | ID   |    20 | R     |       |               |       0301 | DNS                                 |                                                                                                        |
| Date/Time of Message                    |     7 | TS   |    26 | R     | False |               |            |                                     |                                                                                                        |
| Time                                    |     1 | DTM  |    24 | R     |       |               |            | 20170328134602-0500                 | Date/time the message was created in format YYYYMMDD[HHMM[SS]][+-ZZZZ]00                               |
| Degree of Precision                     |     2 | ID   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Security                                |     8 | ST   |    40 | NS    |       |               |            |                                     |                                                                                                        |
| Message Type                            |     9 | MSG  |    15 | R     | False |               |            |                                     |                                                                                                        |
| Message Code                            |     1 | ID   |     3 | R     |       | True          |       0076 | ADT                                 | This is always “RDE”                                                                                   |
| Trigger Event                           |     2 | ID   |     3 | R     |       | True          |       0003 | A28                                 | This is always “O11”                                                                                   |
| Message Structure                       |     3 | ID   |     7 | R     |       | True          |       0354 | ADT_A05                             | This is always “RDE_O11”                                                                               |
| Message Control ID                      |    10 | ST   |    20 | R     | False |               |            | 12354                               | Generated by the HL7 module in VistA                                                                   |
| Processing ID                           |    11 | PT   |     3 | R     | False |               |            |                                     |                                                                                                        |
| Processing ID                           |     1 | ID   |     1 | R     |       |               |       0103 | P                                   | “P” -Production  “T” - Test                                                                            |
| Processing Mode                         |     2 | ID   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Version ID                              |    12 | VID  |   973 | R     | False |               |            |                                     |                                                                                                        |
| Version ID                              |     1 | ID   |     5 | R     |       | True          |       0104 | 2.5.1                               | This is always “2.5.1”                                                                                 |
| Internationalization Code               |     2 | CE   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| International Version ID                |     3 | CE   |     0 | NS    |       |               |            |                                     |                                                                                                        |
| Sequence Number                         |    13 | NM   |    15 | NS    |       |               |            |                                     |                                                                                                        |
| Continuation Pointer                    |    14 | ST   |   180 | NS    |       |               |            |                                     |                                                                                                        |
| Accept Acknowledgment Type              |    15 | ID   |     2 | R     | False | True          |       0155 | AL                                  | This is always “AL”                                                                                    |
| Application Acknowledgment Type         |    16 | ID   |     2 | R     | False | True          |       0155 | AL                                  | This is always “AL”                                                                                    |
| Country Code                            |    17 | ID   |     3 | NS    |       |               |            |                                     |                                                                                                        |
| Character Set                           |    18 | ID   |    16 | NS    |       |               |            |                                     |                                                                                                        |
| Principal Language of Message           |    19 | CE   |   483 | NS    |       |               |            |                                     |                                                                                                        |
| Alternate Character Set Handling Scheme |    20 | ID   |    20 | NS    |       |               |            |                                     |                                                                                                        |
| Message Profile Identifier              |    21 | EI   |   427 | NS    |       |               |            |                                     |                                                                                                        |

##### NCR Clozapine Dispense PID Segment

Table: PID Segment

| PID Field Name                                     |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value                                             | Implementation Notes                                                                                                                                                                                                                    |
|----------------------------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID - PID                                       |     1 | SI   |     4 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient ID                                         |     2 | CX   |  1913 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Identifier List                            |     3 | CX   |  1912 | R     | True  |               |            |                                                           |                                                                                                                                                                                                                                         |
| ID Number                                          |     1 | ST   |    15 | R     |       |               |            | VA12345 or  111223344 or  1000720100V271387 or  100234567 | The 1st instance is the patient's Clozaril authorization number (NCR's number – 2 letters followed by 5 numbers). The 2nd instance is the patient's SSN. The 3  rd  instance is the patient ICN. The 4  th  instance is the patient DFN |
| Check Digit                                        |     2 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Check Digit Scheme                                 |     3 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Assigning Authority                                |     4 | HD   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Identifier Type Code                               |     5 | ID   |    20 | R     |       |               |       0203 | PN or SS                                                  | The 1  st  instance is "PN" - Patient's Clozaril authorization number. The 2  nd  instance is "SS" – Patient’s Social Security.                                                                                                         |
| Assigning Facility                                 |     6 | HD   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Effective Date                                     |     7 | DT   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Expiration Date                                    |     8 | DT   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Assigning Jurisdiction                             |     9 | CWE  |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Assigning Agency or Department                     |    10 | CWE  |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Alternate Patient ID - PID                         |     4 | CX   |  1913 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Name                                       |     5 | XPN  |  1044 | R     |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Family Name                                        |     1 | FN   |   194 | R     |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Surname                                            |     1 | ST   |    50 | R     |       |               |            | Doe                                                       | Last Name                                                                                                                                                                                                                               |
| Own Surname Prefix                                 |     2 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Own Surname                                        |     3 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Surname Prefix from Partner/Spouse                 |     4 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Surname from Partner/Spouse                        |     5 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Given Name                                         |     2 | ST   |    50 | R     |       |               |            | John                                                      | First Name                                                                                                                                                                                                                              |
| Second and Further Given Names or Initials Thereof |     3 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Suffix (e.g., JR or III)                           |     4 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Prefix (e.g., DR)                                  |     5 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Degree (e.g., MD)                                  |     6 | IS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name Type Code                                     |     7 | ID   |     1 | R     |       |               |       0200 | L                                                         | This is always "L"                                                                                                                                                                                                                      |
| Name Representation Code                           |     8 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name Context                                       |     9 | CE   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name Validity Range                                |    10 | DR   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name Assembly Order                                |    11 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Effective Date                                     |    12 | TS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Expiration Date                                    |    13 | TS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Professional Suffix                                |    14 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Mother's Maiden Name                               |     6 | XPN  |  1044 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Date/Time of Birth                                 |     7 | TS   |    26 | R     | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Time                                               |     1 | DTM  |    24 | R     |       |               |            | 19700101                                                  | YYYYMMDD                                                                                                                                                                                                                                |
| Degree of Precision                                |     2 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Administrative Sex                                 |     8 | IS   |     1 | R     | False |               |       0001 | M                                                         |                                                                                                                                                                                                                                         |
| Patient Alias                                      |     9 | XPN  |  1044 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Race                                               |    10 | CE   |   478 | R     | False |               |       0005 |                                                           |                                                                                                                                                                                                                                         |
| Identifier                                         |     1 | ST   |    20 | R     |       |               |       0005 | 2028-9                                                    |                                                                                                                                                                                                                                         |
| Text                                               |     2 | ST   |    20 | R     |       |               |            | Asian                                                     | Race Identifier description                                                                                                                                                                                                             |
| Name of Coding System                              |     3 | ID   |    20 | R     |       | True          |       0396 | HL70005                                                   | HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70005”.                                                                                                                                                     |
| Alternate Identifier                               |     4 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Alternate Text                                     |     5 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name of Alternate Coding System                    |     6 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Address                                    |    11 | XAD  |   513 | R     | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Street Address                                     |     1 | SAD  |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Other Designation                                  |     2 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| City                                               |     3 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| State or Province                                  |     4 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Zip or Postal Code                                 |     5 | ST   |    12 | R     |       |               |            | 33408                                                     |                                                                                                                                                                                                                                         |
| Country                                            |     6 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Address Type                                       |     7 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Other Geographic Designation                       |     8 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| County/Parish Code                                 |     9 | IS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Census Tract                                       |    10 | IS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Address Representation Code                        |    11 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Address Validity Range                             |    12 | DR   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Effective Date                                     |    13 | TS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Expiration Date                                    |    14 | TS   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| County Code                                        |    12 | IS   |     4 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Phone Number - Home                                |    13 | XTN  |   651 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Phone Number - Business                            |    14 | XTN  |   651 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Primary Language                                   |    15 | CE   |   483 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Marital Status                                     |    16 | CE   |   483 | NS    | False |               |            | 3.4.2.16                                                  |                                                                                                                                                                                                                                         |
| Religion                                           |    17 | CE   |   483 | NS    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Account Number                             |    18 | CX   |  1912 | NS    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| SSN Number - Patient                               |    19 | ST   |    16 | NS    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Driver's License Number - Patient                  |    20 | DLN  |    66 | NS    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Mother's Identifier                                |    21 | CX   |  1912 | NS    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Ethnic Group                                       |    22 | CE   |   478 | RE    | False |               |            |                                                           |                                                                                                                                                                                                                                         |
| Identifier                                         |     1 | ST   |    20 | R     |       |               |       0189 | U                                                         |                                                                                                                                                                                                                                         |
| Text                                               |     2 | ST   |    20 | R     |       |               |            | Unknown                                                   | Ethnic Identifier description                                                                                                                                                                                                           |
| Name of Coding System                              |     3 | ID   |    20 | R     |       | True          |       0396 | HL70189                                                   | HL7 Defined Code where nnnn is the HL7 table number 0005. This is always “HL70189”.                                                                                                                                                     |
| Alternate Identifier                               |     4 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Alternate Text                                     |     5 | ST   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Name of Alternate Coding System                    |     6 | ID   |     0 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Birth Place                                        |    23 | ST   |   250 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Multiple Birth Indicator                           |    24 | ID   |     1 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Birth Order                                        |    25 | NM   |     2 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Citizenship                                        |    26 | CE   |   483 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Veterans Military Status                           |    27 | CE   |   483 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Nationality                                        |    28 | CE   |   483 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Death Date and Time                        |    29 | TS   |    26 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Patient Death Indicator                            |    30 | ID   |     1 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Identity Unknown Indicator                         |    31 | ID   |     1 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Identity Reliability Code                          |    32 | IS   |    20 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Last Update Date/Time                              |    33 | TS   |    26 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Last Update Facility                               |    34 | HD   |   241 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Species Code                                       |    35 | CE   |   478 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Breed Code                                         |    36 | CE   |   478 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Strain                                             |    37 | ST   |    80 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Production Class Code                              |    38 | CE   |   483 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |
| Tribal Citizenship                                 |    39 | CWE  |   705 | NS    |       |               |            |                                                           |                                                                                                                                                                                                                                         |

##### NCR Clozapine Dispense PV1 Segment

Table: PV1 Segment

| PV1 Field Name            |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes              |
|---------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|-----------------------------------|
| Set ID - PV1              |     1 | SI   |     4 | NS    |       |               |            |                 |                                   |
| Patient Class             |     2 | IS   |     1 | R     | False |               |       0004 | O or I          | “O” - Outpatient  “I” - Inpatient |
| Assigned Patient Location |     3 | PL   |  1230 | NS    |       |               |            |                 |                                   |
| Admission Type            |     4 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Preadmit Number           |     5 | CX   |  1912 | NS    |       |               |            |                 |                                   |
| Prior Patient Location    |     6 | PL   |  1230 | NS    |       |               |            |                 |                                   |
| Attending Doctor          |     7 | XCN  |  2930 | NS    |       |               |            |                 |                                   |
| Referring Doctor          |     8 | XCN  |  2930 | NS    |       |               |            |                 |                                   |
| Consulting Doctor         |     9 | XCN  |  2945 | NS    |       |               |            |                 |                                   |
| Hospital Service          |    10 | IS   |     3 | NS    |       |               |            |                 |                                   |
| Temporary Location        |    11 | PL   |  1230 | NS    |       |               |            |                 |                                   |
| Preadmit Test Indicator   |    12 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Re-admission Indicator    |    13 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Admit Source              |    14 | IS   |     6 | NS    |       |               |            |                 |                                   |
| Ambulatory Status         |    15 | IS   |     2 | NS    |       |               |            |                 |                                   |
| VIP Indicator             |    16 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Admitting Doctor          |    17 | XCN  |  2930 | NS    |       |               |            |                 |                                   |
| Patient Type              |    18 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Visit Number              |    19 | CX   |  1912 | NS    |       |               |            |                 |                                   |
| Financial Class           |    20 | FC   |    50 | NS    |       |               |            |                 |                                   |
| Charge Price Indicator    |    21 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Courtesy Code             |    22 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Credit Rating             |    23 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Contract Code             |    24 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Contract Effective Date   |    25 | DT   |     8 | NS    |       |               |            |                 |                                   |
| Contract Amount           |    26 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Contract Period           |    27 | NM   |     3 | NS    |       |               |            |                 |                                   |
| Interest Code             |    28 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Transfer to Bad Debt Code |    29 | IS   |     4 | NS    |       |               |            |                 |                                   |
| Transfer to Bad Debt Date |    30 | DT   |     8 | NS    |       |               |            |                 |                                   |
| Bad Debt Agency Code      |    31 | IS   |    10 | NS    |       |               |            |                 |                                   |
| Bad Debt Transfer Amount  |    32 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Bad Debt Recovery Amount  |    33 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Delete Account Indicator  |    34 | IS   |     1 | NS    |       |               |            |                 |                                   |
| Delete Account Date       |    35 | DT   |     8 | NS    |       |               |            |                 |                                   |
| Discharge Disposition     |    36 | IS   |     3 | NS    |       |               |            |                 |                                   |
| Discharged to Location    |    37 | DLD  |    47 | NS    |       |               |            |                 |                                   |
| Diet Type                 |    38 | CE   |   483 | NS    |       |               |            |                 |                                   |
| Servicing Facility        |    39 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Bed Status                |    40 | IS   |     1 | NS    |       |               |            |                 |                                   |
| Account Status            |    41 | IS   |     2 | NS    |       |               |            |                 |                                   |
| Pending Location          |    42 | PL   |  1230 | NS    |       |               |            |                 |                                   |
| Prior Temporary Location  |    43 | PL   |  1230 | NS    |       |               |            |                 |                                   |
| Admit Date/Time           |    44 | TS   |    26 | NS    |       |               |            |                 |                                   |
| Discharge Date/Time       |    45 | TS   |    26 | NS    |       |               |            |                 |                                   |
| Current Patient Balance   |    46 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Total Charges             |    47 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Total Adjustments         |    48 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Total Payments            |    49 | NM   |    12 | NS    |       |               |            |                 |                                   |
| Alternate Visit ID        |    50 | CX   |  1912 | NS    |       |               |            |                 |                                   |
| Visit Indicator           |    51 | IS   |     1 | NS    |       |               |            |                 |                                   |
| Other Healthcare Provider |    52 | XCN  |  2945 | NS    |       |               |            |                 |                                   |

##### NCR Clozapine Dispense ORC Segment

Table: ORC Segment

| ORC Field Name                                     |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes                                 |
|----------------------------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|------------------------------------------------------|
| Order Control                                      |     1 | ID   |     2 | R     | False | True          |       0119 | RE              | This is always “RE”                                  |
| Placer Order Number                                |     2 | EI   |   424 | NS    |       |               |            |                 |                                                      |
| Filler Order Number                                |     3 | EI   |   424 | NS    |       |               |            |                 |                                                      |
| Placer Group Number                                |     4 | EI   |   427 | NS    |       |               |            |                 |                                                      |
| Order Status                                       |     5 | ID   |     2 | NS    |       |               |            |                 |                                                      |
| Response Flag                                      |     6 | ID   |     1 | NS    |       |               |            |                 |                                                      |
| Quantity/Timing                                    |     7 | TQ   |  1778 | NS    |       |               |            |                 |                                                      |
| Parent                                             |     8 | EIP  |   855 | NS    |       |               |            |                 |                                                      |
| Date/Time of Transaction                           |     9 | TS   |    26 | R     | False |               |            |                 |                                                      |
| Time                                               |     1 | DTM  |    24 | R     |       |               |            | 20170328        | Date prescribed YYYYMMDD                             |
| Degree of Precision                                |     2 | ID   |     0 | NS    |       |               |            |                 |                                                      |
| Entered By                                         |    10 | XCN  |  2930 | NS    |       |               |            |                 |                                                      |
| Verified By                                        |    11 | XCN  |  2930 | NS    |       |               |            |                 |                                                      |
| Ordering Provider                                  |    12 | XCN  |  2930 | R     | False |               |            |                 |                                                      |
| ID Number                                          |     1 | ST   |    20 | R     |       |               |            | 1235319599      | This is the NPI number of the prescribing physician. |
| Family Name                                        |     2 | FN   |   194 | R     |       |               |            |                 |                                                      |
| Surname                                            |     1 | ST   |    50 | R     |       |               |            | Lastname        | Last name of the prescribing physician               |
| Own Surname Prefix                                 |     2 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Own Surname                                        |     3 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Surname Prefix from Partner/Spouse                 |     4 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Surname from Partner/Spouse                        |     5 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Given Name                                         |     3 | ST   |    30 | R     |       |               |            | Firstname       | First name of the prescribing physician              |
| Second and Further Given Names or Initials Thereof |     4 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Suffix (e.g., JR or III)                           |     5 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Prefix (e.g., DR)                                  |     6 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Degree (e.g., MD)                                  |     7 | IS   |     0 | NS    |       |               |            |                 |                                                      |
| Source Table                                       |     8 | IS   |     0 | NS    |       |               |            |                 |                                                      |
| Assigning Authority                                |     9 | HD   |     0 | NS    |       |               |            |                 |                                                      |
| Name Type Code                                     |    10 | ID   |     0 | NS    |       |               |            |                 |                                                      |
| Identifier Check Digit                             |    11 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Check Digit Scheme                                 |    12 | ID   |     0 |       |       |               |            |                 |                                                      |
| Identifier Type Code                               |    13 | ID   |     3 | R     |       | True          |       0203 | NPI             | This is always "NPI"                                 |
| Assigning Facility                                 |    14 | HD   |     0 | NS    |       |               |            |                 |                                                      |
| Name Representation Code                           |    15 | ID   |     0 | NS    |       |               |            |                 |                                                      |
| Name Context                                       |    16 | CE   |     0 | NS    |       |               |            |                 |                                                      |
| Name Validity Range                                |    17 | DR   |     0 | NS    |       |               |            |                 |                                                      |
| Name Assembly Order                                |    18 | ID   |     0 | NS    |       |               |            |                 |                                                      |
| Effective Date                                     |    19 | TS   |     0 | NS    |       |               |            |                 |                                                      |
| Expiration Date                                    |    20 | TS   |     0 | NS    |       |               |            |                 |                                                      |
| Professional Suffix                                |    21 | ST   |     0 | NS    |       |               |            |                 |                                                      |
| Assigning Jurisdiction                             |    22 | CWE  |     0 | NS    |       |               |            |                 |                                                      |
| Assigning Agency or Department                     |    23 | CWE  |     0 | NS    |       |               |            |                 |                                                      |
| Enterer's Location                                 |    13 | PL   |  1230 | NS    |       |               |            |                 |                                                      |
| Call Back Phone Number                             |    14 | XTN  |   651 | NS    |       |               |            |                 |                                                      |
| Order Effective Date/Time                          |    15 | TS   |    26 | NS    |       |               |            |                 |                                                      |
| Order Control Code Reason                          |    16 | CE   |   483 | NS    |       |               |            |                 |                                                      |
| Entering Organization                              |    17 | CE   |   483 | NS    |       |               |            |                 |                                                      |
| Entering Device                                    |    18 | CE   |   483 | NS    |       |               |            |                 |                                                      |
| Action By                                          |    19 | XCN  |  2930 | NS    |       |               |            |                 |                                                      |
| Advanced Beneficiary Notice Code                   |    20 | CE   |   483 | NS    |       |               |            |                 |                                                      |
| Ordering Facility Name                             |    21 | XON  |   563 | NS    |       |               |            |                 |                                                      |
| Ordering Facility Address                          |    22 | XAD  |   513 | NS    |       |               |            |                 |                                                      |
| Ordering Facility Phone Number                     |    23 | XTN  |   651 | NS    |       |               |            |                 |                                                      |
| Ordering Provider Address                          |    24 | XAD  |   513 | NS    |       |               |            |                 |                                                      |
| Order Status Modifier                              |    25 | CWE  |   705 | NS    |       |               |            |                 |                                                      |
| Advanced Beneficiary Notice Override Reason        |    26 | CWE  |   697 | NS    |       |               |            |                 |                                                      |
| Filler's Expected Availability Date/Time           |    27 | TS   |    26 | NS    |       |               |            |                 |                                                      |
| Confidentiality Code                               |    28 | CWE  |   705 | NS    |       |               |            |                 |                                                      |
| Order Type                                         |    29 | CWE  |   705 | NS    |       |               |            |                 |                                                      |
| Enterer Authorization Mode                         |    30 | CNE  |   697 | NS    |       |               |            |                 |                                                      |
| Parent Universal Service Identifier                |    31 | CWE  |   705 | NS    |       |               |            |                 |                                                      |

##### NCR Clozapine Dispense RXE Segment

Table: RXE Segment

| RXE Field Name                                                |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes                                                                                                                                       |
|---------------------------------------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quantity/Timing                                               |     1 | TQ   |  1778 | NS    | False |               |            |                 |                                                                                                                                                            |
| Give Code                                                     |     2 | CE   |   478 | R     | False |               |            |                 |                                                                                                                                                            |
| Identifier                                                    |     1 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Text                                                          |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Coding System                                         |     3 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Identifier                                          |     4 | ST   |    20 | R     |       |               |            | 64725-1260      | NDC Number                                                                                                                                                 |
| Alternate Text                                                |     5 | ST   |   199 | R     |       |               |            | Clozaril        | Drug Name                                                                                                                                                  |
| Name of Alternate Coding System                               |     6 | ID   |    20 | R     |       | True T        |       0396 | NDC             | This is always “NDC”                                                                                                                                       |
| Give Amount - Minimum                                         |     3 | NM   |    20 | R     | False |               |            | 100             |                                                                                                                                                            |
| Give Amount - Maximum                                         |     4 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Units                                                    |     5 | CE   |   478 | R     | False |               |            |                 |                                                                                                                                                            |
| Identifier                                                    |     1 | ST   |    20 | R     |       |               |            | MG              |                                                                                                                                                            |
| Text                                                          |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Coding System                                         |     3 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Identifier                                          |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Text                                                |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Alternate Coding System                               |     6 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Dosage Form                                              |     6 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Provider's Administration Instructions                        |     7 | CE   |   483 | RE    | False |               |            |                 |                                                                                                                                                            |
| Identifier                                                    |     1 | ST   |     0 | R     |       |               |            | 91              |                                                                                                                                                            |
| Text                                                          |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Coding System                                         |     3 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Identifier                                          |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Text                                                |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Alternate Coding System                               |     6 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Deliver-To Location                                           |     8 | LA1  |   790 | NS    |       |               |            |                 |                                                                                                                                                            |
| Substitution Status                                           |     9 | ID   |     1 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispense Amount                                               |    10 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispense Units                                                |    11 | CE   |   478 | NS    |       |               |            |                 |                                                                                                                                                            |
| Number of Refills                                             |    12 | NM   |     3 | NS    |       |               |            |                 |                                                                                                                                                            |
| Ordering Provider's DEA Number                                |    13 | XCN  |  2930 | NS    |       |               |            |                 |                                                                                                                                                            |
| Pharmacist/Treatment Supplier's Verifier ID                   |    14 | XCN  |  2930 | CE    |       |               |            |                 | Only if REX.7 is populated                                                                                                                                 |
| ID Number                                                     |     1 | ST   |    20 | R     |       |               |            | AR7071296       | The 1st instance is the DEA number of  the prescriber who approved the  denial/override.  The 2nd instance is this prescriber's  DUZ number from file 200. |
| Family Name                                                   |     2 | FN   |   194 | R     |       |               |            |                 |                                                                                                                                                            |
| Surname                                                       |     1 | ST   |    50 | R     |       |               |            | Lastname        | Last name of the prescriber who approved the  denial/override.                                                                                             |
| Own Surname Prefix                                            |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Own Surname                                                   |     3 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Surname Prefix from Partner/Spouse                            |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Surname from Partner/Spouse                                   |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Given Name                                                    |     3 | ST   |    30 | R     |       |               |            | Firstname       | First name of prescriber who approved the denial/override.                                                                                                 |
| Second and Further Given Names or Initials Thereof            |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Suffix (e.g., JR or III)                                      |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Prefix (e.g., DR)                                             |     6 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Degree (e.g., MD)                                             |     7 | IS   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Source Table                                                  |     8 | IS   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Assigning Authority                                           |     9 | HD   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name Type Code                                                |    10 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Identifier Check Digit                                        |    11 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Check Digit Scheme                                            |    12 | ID   |     0 |       |       |               |            |                 |                                                                                                                                                            |
| Identifier Type Code                                          |    13 | ID   |     3 | R     |       |               |       0203 | DEA             | The 1st instance is "DEA", the 2nd instance is "PN".                                                                                                       |
| Assigning Facility                                            |    14 | HD   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name Representation Code                                      |    15 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name Context                                                  |    16 | CE   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name Validity Range                                           |    17 | DR   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name Assembly Order                                           |    18 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Effective Date                                                |    19 | TS   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Expiration Date                                               |    20 | TS   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Professional Suffix                                           |    21 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Assigning Jurisdiction                                        |    22 | CWE  |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Assigning Agency or Department                                |    23 | CWE  |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Prescription Number                                           |    15 | ST   |    20 | C     |       |               |            | 13519100        | If patient type in PV1.2 is "I" (Inpatient), then it is an order number.  If patient type in PV1.2 is "O"  (Outpatient), it is a prescription number.      |
| Number of Refills Remaining                                   |    16 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Number of Refills/Doses Dispensed                             |    17 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| D/T of Most Recent Refill or Dose Dispensed                   |    18 | TS   |    26 | NS    |       |               |            |                 |                                                                                                                                                            |
| Total Daily Dose                                              |    19 | CQ   |   499 | NS    |       |               |            |                 |                                                                                                                                                            |
| Needs Human Review                                            |    20 | ID   |     1 | NS    |       |               |            |                 |                                                                                                                                                            |
| Pharmacy/Treatment Supplier's Special Dispensing Instructions |    21 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Per (Time Unit)                                          |    22 | ST   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Rate Amount                                              |    23 | ST   |     6 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Rate Units                                               |    24 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Strength                                                 |    25 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Strength Units                                           |    26 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Indication                                               |    27 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispense Package Size                                         |    28 | NM   |    20 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispense Package Size Unit                                    |    29 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispense Package Method                                       |    30 | ID   |     2 | NS    |       |               |            |                 |                                                                                                                                                            |
| Supplementary Code                                            |    31 | CE   |   483 | NS    |       |               |            |                 |                                                                                                                                                            |
| Original Order Date/Time                                      |    32 | TS   |    26 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Drug Strength Volume                                     |    33 | NM   |     5 | NS    |       |               |            |                 |                                                                                                                                                            |
| Give Drug Strength Volume Units                               |    34 | CWE  |   705 | NS    |       |               |            |                 |                                                                                                                                                            |
| Controlled Substance Schedule                                 |    35 | CWE  |   705 | NS    |       |               |            |                 |                                                                                                                                                            |
| Formulary Status                                              |    36 | ID   |     1 | NS    |       |               |            |                 |                                                                                                                                                            |
| Pharmaceutical Substance Alternative                          |    37 | CWE  |   705 | NS    |       |               |            |                 |                                                                                                                                                            |
| Pharmacy of Most Recent Fill                                  |    38 | CWE  |   705 | NS    |       |               |            |                 |                                                                                                                                                            |
| Initial Dispense Amount                                       |    39 | NM   |   250 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispensing Pharmacy                                           |    40 | CWE  |   705 | NS    |       |               |            |                 |                                                                                                                                                            |
| Identifier                                                    |     1 | ST   |    20 | R     |       |               |            | 1234567         | This is pharmacy number NCPDP                                                                                                                              |
| Text                                                          |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Coding System                                         |     3 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Identifier                                          |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Text                                                |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Name of Alternate Coding System                               |     6 | ID   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Coding System Version                                         |     7 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Alternate Coding System Version ID                            |     8 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Original Text                                                 |     9 | ST   |     0 | NS    |       |               |            |                 |                                                                                                                                                            |
| Dispensing Pharmacy Address                                   |    41 | XAD  |   513 | NS    |       |               |            |                 |                                                                                                                                                            |
| Deliver-to Patient Location                                   |    42 | PL   |  1230 | NS    |       |               |            |                 |                                                                                                                                                            |
| Deliver-to Address                                            |    43 | XAD  |   513 | NS    |       |               |            |                 |                                                                                                                                                            |
| Pharmacy Order Type                                           |    44 | ID   |     1 | NS    |       |               |            |                 |                                                                                                                                                            |

##### NCR Clozapine Dispense TQ1 Segment

Table: TQ1 Segment

| TQ1 Field Name                  |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   | Code Tbl   | Example Value   | Implementation Notes                                                           |
|---------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|--------------------------------------------------------------------------------|
| Set ID - TQ1                    |     1 | SI   |     4 | R     | False |               |            | 1               | This is consecutive numbers 1, 2, 3, etc. to indicate the order of repetitions |
| Quantity                        |     2 | CQ   |   500 | R     | False |               |            |                 |                                                                                |
| Quantity                        |     1 | NM   |    16 | R     |       |               |            | 100             | This is drug dosage amount                                                     |
| Units                           |     2 | CE   |   483 | R     |       |               |            |                 |                                                                                |
| Identifier                      |     1 | ST   |    20 | R     |       |               |            | MG              | This is drug dosage units                                                      |
| Text                            |     2 | ST   |     0 | NS    |       |               |            |                 |                                                                                |
| Name of Coding System           |     3 | ID   |     0 | NS    |       |               |            |                 |                                                                                |
| Alternate Identifier            |     4 | ST   |     0 | NS    |       |               |            |                 |                                                                                |
| Alternate Text                  |     5 | ST   |     0 | NS    |       |               |            |                 |                                                                                |
| Name of Alternate Coding System |     6 | ID   |     0 | NS    |       |               |            |                 |                                                                                |
| Repeat Pattern                  |     3 | RPT  |   984 | NS    |       |               |            |                 |                                                                                |
| Explicit Time                   |     4 | TM   |    20 | NS    |       |               |            |                 |                                                                                |
| Relative Time and Units         |     5 | CQ   |   500 | NS    |       |               |            |                 |                                                                                |
| Service Duration                |     6 | CQ   |   500 | NS    |       |               |            |                 |                                                                                |
| Start date/time                 |     7 | TS   |    26 | NS    |       |               |            |                 |                                                                                |
| End date/time                   |     8 | TS   |    26 | NS    |       |               |            |                 |                                                                                |
| Priority                        |     9 | CWE  |   705 | NS    |       |               |            |                 |                                                                                |
| Condition text                  |    10 | TX   |   250 | NS    |       |               |            |                 |                                                                                |
| Text instruction                |    11 | TX   |   250 | NS    |       |               |            |                 |                                                                                |
| Conjunction                     |    12 | ID   |    10 | NS    |       |               |            |                 |                                                                                |
| Occurrence duration             |    13 | CQ   |   500 | NS    |       |               |            |                 |                                                                                |
| Total occurrence's              |    14 | NM   |    10 | NS    |       |               |            |                 |                                                                                |

##### NCR Clozapine Dispense RXR Segment

Table: RXR Segment

| RXR Field Name               |   Seq | DT   |   Len | Opt   | Rep   | Fixed Value   |   Code Tbl | Example Value   | Implementation Notes          |
|------------------------------|-------|------|-------|-------|-------|---------------|------------|-----------------|-------------------------------|
| Route                        |     1 | CE   |   478 | R     | False |               |            |                 |                               |
| Identifier                   |     1 | ST   |    20 | R     |       | True          |       0162 | PO              | This is always “PO” for oral. |
| Text                         |     2 | ST   |   199 | R     |       | True          |            | ORAL            | This is always “ORAL”         |
| Name of Coding System        |     3 | ID   |    20 | R     |       | True          |       0396 | HL70162         | This is always “HL70162”      |
| Alternate Identifier         |     4 | ST   |     0 | NS    |       |               |            |                 |                               |
| Alternate Text               |     5 | ST   |     0 | NS    |       |               |            |                 |                               |
| Alternate Coding System Name |     6 | ID   |     0 | NS    |       |               |            |                 |                               |
| Administration Site          |     2 | CWE  |   705 | NS    |       |               |            |                 |                               |
| Administration Device        |     3 | CE   |   483 | NS    |       |               |            |                 |                               |
| Administration Method        |     4 | CWE  |   705 | NS    |       |               |            |                 |                               |
| Routing Instruction          |     5 | CE   |   483 | NS    |       |               |            |                 |                               |
| Administration Site Modifier |     6 | CWE  |   705 | NS    |       |               |            |                 |                               |