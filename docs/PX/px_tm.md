---
app_name: Patient Care Encounter (PCE) (PX)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2026-03
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PX
patch: 246
patch_gap: null
section: ''
source_file: px_tm.docx
status: draft
title: Patient Care Encounter (PCE)
---

# Patient Care Encounter (PCE)

# Technical Manual

<!-- image -->

Version 1.0

March 2026


Revision History

| Date       | Version                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Authors   |
|------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 03/2026    | PX*1*246                                    | Updated the following section:  File Descriptions on 818 - Compact Act Episode of Care                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED  |
| 11/2025    | PX*1*241                                    | Updated the following sections:  3.1 Patient Care Encounter Files  15.1 Added COMPACT ACT DISPLAY DATA and COMPACT ACT EOC EDIT in Menu assignment  15.2 Security Keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED  |
| 10/2024    | PX*1*240                                    | Updated the following sections: 3.1, 13, 15.1, and 15.2  3.1 – Added COMPACT Act Episode of Care file  13 – Added COMPACT Act Acute Suicidal Crisis Episode of Care Definition  15.1 – Added PCE COMPACT Act Episode of Care Menu assignment  15.2 – Added PX EOC EDIT Security Key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED  |
| 12/2023    | PX*1*235                                    | Updates were made to the following sections:  **7.**  External Relations - Updated for COMPACT ACT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED  |
| 06/2023    | PX*1*234                                    | Added Appendix D- PX HF MEASUREMENT REPAIR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED  |
| 09/2022    | PX*1*217                                    | Updates were made to the following areas:  - Updated the Skin Test node section – added one entry, deleted eight entries - Updated the Immunization node section – added five entries, deleted eight entries - Added the Imm Contra/Refusal node section - Updated the PX Save Data screenshot - Updated the PXVIMM ICR List screenshot - Updated the PXVIMM IMM DETAILED screenshot in three places: 1, 2, 3 - Updated the PXVIMM IMM Short List screenshot - Removed the duplicate Immunization Provider row in the Immunization table - Added the Ordered by Policy field to the Immunization node and the PX Save Data screenshot. - Rewrote most of Section 2.2.1 – Table Maintenance Options. - Added PXTT FILE INQUIRY to Section 2.2.2 - PCE Information Only Menu - Deleted Section 2.2.3 - PCE Reminder Maintenance Menu. Section 2.2.3 is now called PCE Clinical Reports. - Section 12 - Troubleshooting and Helpful Hints - Deleted the bullet point that tells where to go if clinical reminders are not displaying correctly on Health Summaries - Removed PCE Taxonomy (811.2), PCE Reminder Type (811.8) and PCE Reminder/Maintenance Item (811.9) from the following sections:  - 3.1 – PCE Patient Care Encounter Files table and descriptions - 15.3 – VA FileMan File Protection - 15.4 – Access Recommended for Sites Using Kernel Part III                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED  |
| 05/2021    | PX*1*211                                    | Revised dates on Title page and in Footers  Reviewed for 508 Accessibility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED  |
| 09/17/2019 | Incorporated missing revisions              | After it was determined that 4 previous revisions were missing, they were added to this document. The revision dates and versions are as follows:  - 12/2017 - PX*1*219 - 11/2016 - OI&amp;T TW Updates and Section    508 remediation - 08/2016 - PX*1*216 - 08/2016 - PX*1*215  Please see the respective sections below for descriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |           |
| 04/16/2019 | PX*1*211                                    | Changes were made to the following areas:  - Made some minor changes to the description of PKG and Source for DATA2PCE parameter description - Also, a change for PPEDIT description - Added some information for ACCOUNT returned values - Added a comment that a hospital location is not required for a service category of E - Added information about the encounter type not needed to be if a hospital location is set and further explanation of how the encounter type is not stored in the VISIT file, but is stored in ELAP data - Noted a change in the Encounter subscript for Encounter type changed from required to optional - Added information about the PFSS reference - Added a comment on changing primary providers - Added information about the Provider node PACKAGE information - Added information about the Provider node SOURCE information - Added to the DX/PL node that the data format - Changed the order of the listing for service connected conditions and moved them to the end of the table - Added an “or” to the data format listing for procedure modifier - Added information for Procedure quantity. If a value is not entered, it would default to 1 - Changed the explanation of the procedure category - Expanded the definition for the procedure reference piece - Expanded on the procedure department piece relating to PFSS functionality - Added information about the PACKAGE and SOURCE pieces - Removed information about skin test and passing a diagnosis. See Note - Added information for Skin Test PACKAGE and SOURCE pieces - Added information about the Immunization Override reason - Added information about the Immunization ordering provider piece - Removed information about diagnosis being sent with immunization information as this is no longer allowed. - Added information about the Immunization PACKAGE and SOURCE pieces. - Added a new section on Education Topics - Added information about the exam Ordering Provider and Encounter Provider - Added information about the exam PACKAGE and SOURCE pieces - Added information about the Health Factor node - Added information about the Standard Codes node - Added a section on DATA2PCE return values and errors - Added a definition of Standard Code |           |
| 12/2017    | PX*1*219                                    | Made updates to sections: 2.1, 15.1.  Added section 2.2.3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| 11/2016    | OI&T TW Updates and Section 508 remediation | VIMM 2.0 IPT/BAM enhancements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |           |
| 08/2016    | PX*1*216                                    | Made updates to sections:  2.1, 3.1, 10.1, 10.5, 10.6, 10.8, 15.3. Added sections 10.15 thru 10.19.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |           |
| 08/2016    | PX*1*215                                    | Made updates to sections:  1.4, 2.1, 2.2.1 thru 2.2.4, 3.1, 6.5.  Added  sections 6.6, 10.2 thru 10.14.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |           |
| 01/2016    | PX*1*210                                    | Made updates to sections: 2.1, 6.4, 6.5, 10, 15.3; Added section 15.2 and formatting edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |           |
| 03/2015    | PX*1*206                                    | Updates to Skin Test and Immunization information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |           |
| 12/2014    | PX*1*201                                    | Remediated doc for 508 compliance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |           |
| 08/2014    | PX*1*201                                    | Made additions to File Description section and formatting edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |           |
| 06/2014    |                                             | PX*1*199 – Updates for ICD-10 (pp. 27, 34, 42, 64, 73, 74, 76, 77, 79, 80) Technical Edit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |           |
| 03/30/2009 | PX*1*168                                    | PX*1*168 – Enrollment VistA Changes Release 2 (EVC R2) Changed environmental contaminants to SW Asia Conditions Added Project 112/SHAD Indicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |           |
| 10/31/2008 |                                             | Formatting Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |           |
| 02/03/2006 |                                             | Technical Edit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |           |
| 02/01/2006 | PX*1*164                                    | Manual updated to show changes with patch PX*1*164                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |           |
| 09/05/2005 | PX*1*124                                    | Manual updated to show changes with patch PX*1*124                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |           |
| 08/10/2005 | PX*1*153                                    | Manual updated to show changes with patch PX*1*153: added option PCE Delete Encounters W/O Visit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |           |
| 03/17/2005 | PX*1*151                                    | Manual updated to show changes with Patch PX*1*151  See section: $$CLNCK^SDUTL2(CLN,DSP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |           |
| 11/19/2004 |                                             | Manual updated to comply with SOP 192-352 Displaying Sensitive Data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |           |

###### 1 Table of Contents

1.	Introduction	1

1.1.	Purpose of PCE	1

1.2.	Functionality	1

1.2.1.	Interactive interfaces	1

1.2.2.	Non-interactive interfaces	1

1.3.	Impact of PCE on IRM	2

1.3.1.	MSM Sites	2

1.3.2.	SAC Exemption	2

1.3.3.	DSM Sites	3

1.4.	Impact of PCE on Providers	5

2.	Implementation and Maintenance	6

2.1.	Implementation	6

2.2.	Maintenance	25

2.2.1.	Table Maintenance Options	25

2.2.2.	PCE Information Only Menu	25

2.2.3.	PCE Clinical Reports	27

3.	File Descriptions	29

3.1.	PCE Patient Care Encounter Files	29

4.	Archiving and Purging	39

5.	Callable Routines	39

6.	Enhanced API	41

6.1.	Provider	51

6.2.	DX/PL	53

6.3.	Procedure	58

6.4.	Skin Test	64

6.5.	Immunization	67

6.6.	Imm Contra/Refusal	74

6.7.	Education Topics	76

6.8.	Exams	77

6.9.	Health Factors	79

6.10.	Standard Codes	81

6.11.	Example of Data Passed Using $DATA2PCE^PXAPI	84

6.12.	DATA2PCE Return Values and Error Arrays	85

6.13.	$$CLNCK^SDUTL2(CLN,DSP)	88

7.	External Relations	89

8.	Package-Wide Variables	89

9.	Integration Control Registrations	89

10.	Remote Procedure Call	90

10.1.	PX Save Data	90

10.2.	PXVIMM ADMIN CODES	92

10.3.	PXVIMM ADMIN ROUTE	93

10.4.	PXVIMM ADMIN SITE	94

10.5.	PXVIMM ICR LIST	95

10.6.	PXVMM IMM DETAILED	96

10.7.	PXVIMM IMM FORMAT	98

10.8.	PXVIMM IMM LOT	98

10.9.	PXVIMM IMM MAN	100

10.10.	PXVIMM IMM SHORT LIST	102

10.11.	PXVIMM IMMDATA	103

10.12.	PXVIMM INFO SOURCE	104

10.13.	PXVIMM VICR EVENTS	105

10.14.	PXVIMM VIS	106

10.15.	PXVIMM IMM DISCLOSURE	107

10.16.	PXVIMM VIMM DATA	108

10.17.	PXVSK DEF SITES	116

10.18.	PXVSK SKIN SHORT LIST	116

10.19.	PXVSK V SKIN TEST LIST	117

11.	Generating Online Documentation	118

11.1.	Routines	118

11.2.	Globals	118

11.3.	Files	118

11.4.	XINDEX	118

11.5.	Data Dictionaries	119

12.	Troubleshooting and Helpful Hints	120

12.1.	Shortcuts	120

12.2.	Device Interface Error Report	121

13.	Glossary	122

14.	Appendix A – Developer Guide – PCE Device Interface Module	125

15.	Appendix B – PCE Security	139

15.1.	Menu Assignment	139

15.2.	Security Keys	140

15.3.	VA FileMan File Protection	140

15.4.	Access Recommended for Sites Using Kernel Part III	142

15.5.	Visit Tracking	143

16.	Appendix C – Visit Tracking Technical Information	145

16.1.	Introduction	145

16.2.	Background	145

16.3.	Relationship to Other Packages	145

16.4.	Functions Provided	145

16.5.	Benefits	146

16.6.	Dependencies	146

16.7.	Visit Creation	147

16.7.1.	Two Approaches for Creating Clinical Visits	147

16.8.	IRM Responsibility	147

16.9.	Guidelines for Developers	147

16.10.	Supported Entry Points	148

16.11.	Conventions	148

16.12.	Create and/or Match Visit Using Input Criteria	148

16.13.	Update Dependent Entry Counter	149

16.14.	Only the DFN is Required	151

16.15.	Package-Wide Variables	152

17.	Appendix D – PX HF MEASUREMENT REPAIR	154

17.1.	Introduction	154

17.2.	Background	154

17.3.	PX HF MEASUREMENTS REPAIR	154

17.3.1.	HEALTH FACTORS WITH INCOMPLETE MESUREMENT DEFINITION	154

17.3.2.	V HEALTH FACTORS measurement repair	155

## 1 Introduction

### Purpose of PCE

Patient Care Encounter (PCE) helps sites collect, manage, and display outpatient encounter data (including providers, procedure codes, and diagnostic codes) in compliance with the 10/1/96 Ambulatory Care Data Capture mandate from the Undersecretary of Health.

Patient Care Encounter (PCE) adds to current VISTA (DHCP) patient information by capturing clinical data resulting from a patient encounter, including problems treated, procedures done and provider information, as well as immunizations, skin tests, treatments, and patient education.

The goal of PCE is to provide an underlying database structure which enables the collection and management of clinical data from multiple data collection sources, including scanners, user interfaces, and non-interactive ancillary interfaces. The key users of this clinical data are clinicians, management, Quality Assurance, and Scheduling personnel.

### Functionality

The primary functions exported with Version 1.0 of PCE are:

- Collection and management of outpatient encounter data.
- Presentation of outpatient encounter data through Health Summary components and Clinical Reports.

Outpatient encounter data is captured through interactive and non-interactive interfaces.

#### Interactive interfaces

- Online data capture through a user interface developed with List Manager tools.
- Online data capture in which Scheduling integrates with PCE to collect checkout information.

#### Non-interactive interfaces

- PCE Device Interface, which supports the collection of encounter form data from scanners such as PANDAS, Teleform, and Automated Information Collection System (AICS), also supports workstation collection of outpatient encounter data.
- PCE application programming interfaces (API) which support the collection of outpatient encounter data from ancillary packages such as Laboratory, Radiology, Text Integration Utility (TIU), and Computerized Patient Record System (CPRS).

### Impact of PCE on IRM

Sites must evaluate functionality exported with PCE and then choose to implement the portions that will enhance current data collection practices at their facilities.

PCE will need a clinical coordinator to help facilitate data capture implementation and health summary type modifications.

Patient Care Encounter is used as a clinical repository for data from many data collection sources, including scanning devices such as PANDAS and TELEFORM, the Automated Information Collection System (AICS), or the Graphical User Interface (GUI) physician workstation, as well as manual data entry options in Scheduling and PCE. The table below lists estimated disk space requirements for PCE/Visit Tracking for four levels of facility complexity. Estimates are based on adding 83k to the database for every 100 encounters, where each encounter averages two procedures, one diagnosis, and one provider. Each visit averages 1.9 encounters, based on stop code reporting per visit transmitted to Austin.

|   Complexity Level |   Average # of Ambulatory Visits/Year | Estimated Disk Space Requirements/Year   |
|--------------------|---------------------------------------|------------------------------------------|
|                  1 |                               254,018 | 400mb                                    |
|                  2 |                               149,101 | 234mg                                    |
|                  3 |                                92,761 | 146mb                                    |
|                  4 |                                71,371 | 112mb                                    |

#### MSM Sites

Increase your Stack/Stap to 24k to avoid STKOV errors, and the size of your partitions to 85k to avoid PGMOV errors.

#### SAC Exemption

PCE has requested an exemption to SAC 2.2.7, which states the maximum routine size.

To avoid PGMOV errors, add an entry and exit action to dynamically increase/decrease the partition size as described below for the following options:

Appointment Management [SDAM APPT MGT]

Appointment Check-in/Check-out [SDAM APPT CHECK IN/OUT]

Add/Edit Stop Codes [SDADDEDIT]

Check-in/Unsched. Visit [SDI]

Make Appointment [SDM]

Multiple Appointment Booking [SDMULTIBOOK]

Disposition an Application [DG DISPOSITION APPLICATION]

Disposition Log Edit [DG DISPOSITION EDIT]

Entry action: S %K=85 D INT^%PARTSIZ

Exit action:  S %K=40 D INT^%PARTSIZ

#### DSM Sites

Expand string length for data and global references to accommodate Standards and Conventions (SAC) 2.3.2.2 which extends the full evaluated length of a global reference to 200 characters.

Since the current default for maximum global reference length is 128 for DSM sites, do the following:

What UCI:  MGR

YOU'RE IN UCI:  MGR,DEV

&gt;D ^VOLMAN

Volume Management Utilities

1.  ADD                             (ADD^VOLMAN)

2.  CREATE                          (CREATE^VOLMAN)

3.  EXTEND                          (EXTEND^VOLMAN)

4.  MAXIMUM GLOBALS                 (MAXGLO^VOLMAN2)

5.  STRING LENGTH                   (EXPSTR^VOLMAN2)

Select Option &gt; 5.  STRING LENGTH

Volume Set to set EXPANDED STRING LENGTH flag for   &gt; ^TMP

Expanded string length for data and global references is currently DISALLOWED on this Volume Set:

255 bytes is the maximum data length, and

128 bytes is the maximum global reference length.

When you enable expanded strings and global references on a Volume Set, then:

512 bytes is the maximum data length, and

249 bytes is the maximum global reference length.

*** WARNING *** Once you have enabled a Volume Set for use with expanded strings and subscripts, that flag may NOT be reset.

Allow expanded string lengths on Volume Set ^TMP [Y OR N] ? &lt;N&gt; Y

Expanded string length is now ENABLED on Volume Set ^TMP.

Note:  The new settings will not take effect until the DSM configuration is shut down and re-started on all nodes.

### Impact of PCE on Providers

Providers will be impacted by PCE through entry and retrieval of outpatient encounter data. Below is a scenario demonstrating a possible sequence of events:

1. A provider has a patient encounter (appointment, walk-in, telephone call, Hospital Based Home Care (HBHC), etc.).

Materials available to a provider which relate to PCE:

- Health Summary with new components summarizing previous encounters, and a health reminders component with reminders based on clinical repository data.
- Encounter Form (hard copy or workstation with pre-defined terminology for the provider’s clinic/service type). This is the instrument for documenting the encounter information.
    1. The provider enters encounter information directly into PCE or onto an encounter form.
    2. A data entry clerk scans the encounter form or manually enters the information from the encounter form into PCE. Scanned encounter data is passed to the PCE Device Interface Module, where the data is stored in PCE files. The encounter data is automatically passed from PCE to Scheduling for clinical workload reporting and billing purposes.
Types of Encounter Form data collected and stored in PCE:
    - Encounters
    - Providers
    - Problems/Diagnosis/symptoms treated at visit
    - CPT procedures performed
    - Immunizations (CPT-mappable)
    - Skin tests (CPT-mappable)
    - Patient education
    - Exams (non-CPT-mappable
    - Treatments (non-CPT-mappable)
        1. The provider may later view information relating to these encounters on clinical reports or on health summaries. Reminders and maintenance information relating to patients can also be printed on health summaries.

## 2 Implementation and Maintenance

### Implementation

1. Assign PCE Menu and Options

PCE IRM Main Menu

(This menu includes all options exported with PCE.)

SP	PCE 	Site Parameters Menu ...

SITE  	PCE Site Parameters Edit

RPT   	PCE HS/RPT Parameter Menu ...

PRNT	PCE HS/RPT Parameters Print

HS     PCE HS Disclaimer Edit

RPT	PCE Report Parameter Edit

DISP	PCE Edit Disposition Clinics

TBL	PCE Table Maintenance ...

INFO	PCE Information Only ...

ACT	Activate/Inactivate Table Items ...

CED	Education Topic Copy

DEF    Immunization Default Responses Enter/Edit

DEWO   PCE Delete Encounters W/O Visit

ED     Education Topic Add/Edit

EX     Examinations Add/Edit

HF     Health Factors Add/Edit

IM     Immunizations Add/Edit
                  	**&gt; Out of order:  Do not use!
                  	Placed out of order by PX*1*201

LOT	Immunization Lot Add/Edit/Display

SK   	Skin Tests Add/Edit
                  	**&gt; Out of order:  Do not use!
                  	Placed out of order by PX*1*206

TR    	Treatments Add/Edit

DE    PCE/SD Debugging Utilities ...

U 	User’s Visit Review

V   	PCE V File Cross Reference Repair

INFO	   PCE Information Only ...

ACT    Activate/Inactivate Table Items ...

E   	Exams

ET  	Education Topics

H   	Health Factors

I	Immunizations
                    **&gt; Out of order:  Do not use!
                    Placed out of order by PX*1*201

S  	Skin Tests

**&gt; Out of order:  Do not use!
                    Placed out of order by PX*1*206

T   	Treatments

ED     Education Topic List

EDI    Education Topic Inquiry

EX     	Exam List

HF     	Health Factors List

IM     	Immunizations List

SK     	Skin Tests List

TR     	Treatments List

CM     	PCE Code Mapping List

RM     PCE Reminder Maintenance Menu ...

RL     	List Reminder Definitions

RI     	Inquire about Reminder Item

RE     	Add/Edit Reminder Item

RC    		Copy Reminder Item

RA     	Activate/Inactivate Reminders

RT     	List Reminder Types Logic

TL     	List Taxonomy Definitions

TI     	Inquire about Taxonomy Item

TE     	Edit Taxonomy Item

TC     	Copy Taxonomy Item

TA     	Activate/Inactivate Taxonomies

CR     PCE Clinical Reports ...

PA    		Patient Activity by Clinic

CP     	Caseload Profile by Clinic

WL 		Workload by Clinic

DX     	Diagnoses Ranked by Frequency

LE     	Location Encounter Counts

PE     	Provider Encounter Counts

HOME   	Directions to Patient's Home Add/Edit

CO     PCE Coordinator Menu ...

SUP  		PCE Encounter Data Entry - Supervisor

PCE 		PCE Encounter Data Entry

DEL   		PCE Encounter Data Entry and Delete

NOD		PCE Encounter Data Entry without Delete

TBL   		PCE Table Maintenance ...

INFO 		PCE Information Only ...

HOME   	Directions to Patient's Home Add/Edit

MDR 		CIDC Missing Data Report

PARM   	PCE HS/RPT Parameters Menu ...

DIS    	Accounting Of Immunization Disclosures Report

DIE    	PCE Device Interface Error Report

DISP		PCE Edit Disposition Clinics

CL      PCE Clinician Menu

RPT  		PCE Clinical Reports ...

ENC 		PCE Encounter Data Entry and Delete

INFO		PCE Information Only...

HOME   	Directions to Patient's Home Add/Edit

PCE IRM Main Menu Descriptions

PX SITE PARAMETER MENU – Site Parameter Menu

This menu includes all options that deal with defining and displaying entries in the PCE PARAMETERS file (#815). The PCE Site Parameters Edit option includes all editable fields, for IRM/ADPAC use. The PCE HS/RPT Parameter Print option can be included on a Health Summary Coordinator's menu if the coordinator is involved with the definition of Clinical Reminders to be printed on the Health Summary.

This option is also included on the PCE Coordinators menu and the PCE Reports option menu. The PCE HS Parameters option can be included on a Health Summary Coordinators menu, and is included on the PCE Coordinator's menu.

This user should be familiar with the PCE Reminders and the use of the reminder disclaimer on the "Clinical Maintenance" and "Clinical Reminder" components. The PCE Report Parameters Setup option can be included on a PCE Coordinator's menu to set up the local file definitions to use to represent Emergency Clinics and various categories of Lab tests by the PCE Report Module.

PXTT TABLE MAINTENANCE – PCE Table Maintenance

The options on this menu are used to add or edit the types of data to be collected by PCE such as Health Factors, Patient Education, etc. Once these tables have been defined, the table entries will be selectable for encounter data entry (PCE package) and encounter form definitions (AICS package). The patient information collected based on these table definitions is viewable on Health Summaries. This menu also includes options to edit the Clinical Reminder/Health Maintenance definitions, based on your site's clinical terminology in the tables. Once reminder criteria have been defined, they may be included in the Health Summary Type definitions for the "Clinical Reminder" and "Health Maintenance" Components.

These options may be used in conjunction with the "PCE Information Only" menu options to manage the contents of the files or tables supporting PCE.

The option PCE Delete Encounters W/O Visit has been created to provide a routine utility to remove Encounters that have missing Visits. (This is described in detail in the text of patch PX*1*153.)

PXQ PCE/SD DEBUGGING UTILITIES – PCE/SD Debugging Utilities

Main menu for the PCE/Scheduling Debugging Utilities. Below is a description of options.

PXQ USER REVIEW – User’s Visit Review

This is a report of the visits and the files that store the visit-related information.

PX V File Repair – PCE V File Cross Reference Repair

This option provides a number of options that allow the user to both report on and fix broken V File Cross References.

Details regarding both of these options are covered in Appendix A-11 of the User Manual Appendices document. Details regarding the User’s Visit Review option are covered in the User Manual.

PXTT PCE INFORMATION ONLY – PCE Information Only

This is a menu of options that list information about the files/tables used by PCE. Some of the files/tables determine what clinical data will be collected as the sites' clinical terminology for specific categories of data such as Immunizations, Skin Tests, Patient Education, and Treatments. The reminder lists allow the user to see what the clinical reminders definitions are for use with the Health Summary package.

PXRM REMINDER MENU – PCE Reminder Maintenance Menu

This is the menu for editing reminder logic and making queries about the files involved with Clinical Reminders and Clinical Maintenance components in the Health Summary package.

PXRR CLINICAL REPORTS – PCE Clinical Reports

This is a menu of PCE clinical reports that clinicians can use for summary level information about their patients, workload activity, and encounter counts.

PX EDIT LOCATION OF HOME – Directions to Patient's Home Add/Edit

This option lets you enter directions to a patient's home; especially useful for Hospital-Based Home Care staff. The Health Summary package contains a new PCE component that displays the directions entered through this option.

PX PCE CLINICIAN MENU – PCE Clinician Menu

This menu contains PCE options which may be useful to the clinician.

PX PCE COORDINATOR MENU – PCE Coordinator Menu

This is the menu for the ADPAC for PCE. It includes all of the user interface options as well as the options for file maintenance. The data entry options may be assigned to clerk and/or clinician menus as needed. The HS and Report parameter options manage fields for site specific preferences/definitions in the Health Summary and PCE Reports.

The first four options/menus are used by IRM staff or coordinators who will be responsible for setting up PCE, maintaining the entries in the PCE tables (such as Patient Education, Immunization, Treatments, etc.), and defining the clinical reminders/maintenance system for your site. Data entry options on the PCE Coordinator and PCE Clinician Menus should be assigned as follows:

- Assign PCE Encounter Data Entry – Supervisor to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries.
- Assign PCE Encounter Data Entry to data entry staff who can document a clinical encounter and who can delete their own entries.
- Assign PCE Encounter Date Entry and Delete to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries.
- Assign PCE Encounter Data Entry without Delete to users who can document a clinical encounter, but should not be able to delete any entries, including ones that they have created.
    1. Set PCE Site Parameters using the PCE Site Parameters Menu on the PCE IRM Menu. This menu includes all options that deal with defining and displaying entries in the PCE PARAMETERS file (815) and all editable fields for IRM/ADPAC use.
PCE Site Parameter Menu
PX PCE SITE PARAMETERS EDIT – PCE Site Parameters Edit
This option is used to edit entries in the PCE PARAMETERS file. The parameters that are set are used as the default controls for the user interface when it starts up. You can set your default view as Appointment or Encounter and a range of dates.
PX HS DISCLAIMER EDIT – PCE HS Disclaimer Edit
This option is used to specify a Site Reminder Disclaimer to be used by the Health Summary package whenever the Health Summary "Clinical Maintenance" and "Clinical Reminder" components are displayed in a Health Summary.
PX HS/RPT PARAMETERS PRINT – PCE HS/RPT Parameters Print
This option prints the current PCE Parameter definitions that are used by Health Summary and some of the PCE Reports.
PX REPORT PARAMETER EDIT – PCE Report Parameter Edit
This option is used to define parameters that will be used by the PCE Report Module. The report edit option allows your site to specify which clinics in file 44 represent "Emergency Room" clinics, and what Lab tests from file 60 should be used for looking up patient data for Glucose, Cholesterol, LDL Cholesterol, and HBA1C lab results. These fields are used by the reports Caseload Profile by Clinic, and Patient Activity by Clinic. To get a printout of current definitions in the PCE Parameters fields for these fields, use the PCE HS/RPT Parameters Print.
PCE EDIT DISPOSITION CLINICS – PCE Edit Disposition Clinics
This option is used to define which clinics are used as Administrative Disposition Clinics.
The PCE HS/RPT Parameter Print and PCE HS Parameters options can be included on a Health Summary Coordinator's menu if the coordinator is involved with the definition of Clinical Reminders to be printed on the Health Summary. These options are also included on the PCE Coordinator menu and the PCE Reports option menu.
PCE exports a disclaimer to appear on Health Summaries:  Default Reminder Disclaimer:
The following disease screening, immunization, and patient education recommendations are offered as guidelines to assist in your practice.
These are only recommendations, not practice standards. The appropriate utilization of these for your individual patient must be based on clinical judgment and the patient's current status.
If your site determines it would prefer a site defined reminder disclaimer instead of the disclaimer distributed by PCE, use the HS Disclaimer Edit option to define your site's disclaimer text. This disclaimer appears on the top of each display of Health Summary "Clinical Maintenance" and "Clinical Reminder" components.
The PCE Report Parameters Edit option can be included on a PCE Coordinator's menu to set up the local file definitions to use to represent Emergency Clinics and various categories of Lab tests by the PCE Report Module. The Caseload Profile by Clinic and Patient Activity by Clinic reports track Critical Lab Values and Emergency Room Visits. The PCE Report Parameter Edit option allows your site to specify which clinics in file 44 represent "Emergency Room" clinics and what tests from the Laboratory Test file (#60) should be used for looking up patient data for Glucose, Cholesterol, LDL Cholesterol and HBA1C lab results. (This is necessary since the Laboratory Test File is not standardized and each site may have customized it differently.)
PCE HS/RPT Parameters Print Example
Select PCE HS/RPT Parameter Menu Option:prnt PCE HS/RPT Parameters Print
DEVICE:   VAX    RIGHT MARGIN: 80// [ENTER]
PCE HS/RPT PARAMETERS PRINT          MAY 21,1996  11:52  PAGE 1
------------------------------------------------------
PARAMETERS related to HEALTH SUMMARY
-------------------------------------
Default Reminder Disclaimer:
The following disease screening, immunization and patient education recommendations are offered as guidelines to assist in your practice.
These are only recommendations, not practice standards.
The appropriate utilization of these for your individual
patient must be based on clinical judgment and the
patient's current status.
Site Reminder Disclaimer (Replaces default disclaimer if defined):
PARAMETERS related to PCE REPORTS
----------------------------------
Report ER Clinic Names: EYE
Report Glucose Names: URINE GLUCOSE
Report Cholesterol Names: CHOLESTEROL
Report LDL Cholesterol Names:
Report HBA1C Names:
PCE Site Parameters Edit
The default Startup View may be set to Appointment or Visit/Encounter. We recommend that you set the default Startup View to Appointment, which displays all the appointments that have been made during the default date range.
The default date range is determined by values that are defined for the Date Offset fields. There are four Date Offset fields. The first two, Beginning Patient Date Offset and Ending Patient Date Offset, determine the default date range for display of patient data. The last two, Beginning Hos Loc Date Offset and Ending Hos Loc Date Offset, determine the default date range for display of patient data based on hospital location (clinic or ward). A number subtracted from today’s date is the Beginning Patient Date Offset (e.g., -30) and a number added to today’s date is the Ending Patient Date Offset (e.g., 1). Do not put in specific dates, but count backwards and forward from the current date.
The Multiple Primary Diagnosis prompt lets sites that use scanning devices choose whether to receive warnings or not have the encounter processed if more than one diagnosis is listed as primary.
You can also set the switch-over date from using the Scheduling interface for checkouts and dispositions, and the starting date for displaying PCE data on Health Summaries.
Select PCE IRM Main Menu Option: SP  PCE Site Parameter Menu
SITE   PCE Site Parameters Edit
RPT    PCE HS/RPT Parameter Menu ...
DISP   PCE Edit Disposition Clinics
Select PCE Site Parameter Menu Option: SI PCE Site Parameters Edit
Select PCE PARAMETERS ONE: 1
STARTUP VIEW: ENCOUNTER
BEGINNING PATIENT DATE OFFSET: -30//[ENTER]
ENDING PATIENT DATE OFFSET: 1//[ENTER]
BEGINNING HOS LOC DATE OFFSET: -7//[ENTER]
ENDING HOS LOC DATE OFFSET: 0//[ENTER]
RETURN WARNINGS: YES//[ENTER]
MULTIPLE PRIMARY DIAGNOSES: RETURN WARNING//?     If errors are returned by the Device Interface then the whole encounter is
not processed.
Choose from:
0        RETURN WARNING
1        RETURN ERROR
MULTIPLE PRIMARY DIAGNOSES: RETURN WARNING//[ENTER]
SD/PCE SWITCH OVER DATE: JUL 1,1996
HEALTH SUMMARY START DATE: JUL 28,1996 Select PCE PARAMETERS ONE: [ENTER]
    1. Review entries contained in PCE Supporting Files: Data is exported for Education Topics, Examinations, Health Factors, Immunizations, Skin Tests, and Treatments. With the exception of “treatments” data was exported with a status of “active.” Entries in each of the supporting files should be evaluated and assigned an appropriate status. Use the Activate/Inactivate Table Items Menu option to review and assign a status for entries. Unless you activate current entries or create new entries for “Treatments,” users will not be able to add treatments to an encounter.
Example of Activating Treatment Items
Select PCE Coordinator Menu Option: TBL  PCE Table Maintenance
Select PCE Table Maintenance Option: ACT  Activate/Inactivate Table Items
E      Exams
ET     Education Topics
H      Health Factors
I      Immunizations
            **&gt; Out of order:  Do not use! Placed out of order by PX*1*201
S      Skin Tests
            **&gt; Out of order:  Do not use! Placed out of order by PX*1*206
T      Treatments
Select Activate/Inactivate Table Items Option:
T      Treatments
Select TREATMENT NAME: WOUND CARE
INACTIVE FLAG: INACTIVE// ??
This field is used to inactivate a treatment type.  If this field
contains a "1" then the treatment is inactive.  Inactive treatments
cannot be selected in the manual data entry process.  Treatment
entries should be made inactive when they are no longer used.  Do
not delete the entry or change the meaning of the treatment entry.
To make an inactive treatment type active, enter the "@" symbol to
delete the "1" from the field.
Choose from:
1        INACTIVE
INACTIVE FLAG: INACTIVE// @
Select TREATMENT NAME: Continue to enter treatments, as needed.
    1. Edit the Report Parameters using the PCE Report Parameter Edit option. This option is used to define parameters that will be used by the PCE Report Module. You need to identify which clinics are considered Emergency Room clinics by clinicians. You also need to identify the lab test names that are used by your site to identify the following types of Lab tests: Glucose, Cholesterol, LDL Cholesterol, and HBA1C.
To get a printout of current definitions in the PCE Parameters fields for these fields, use the PCE HS/RPT Parameters Print.
Example of Editing Report Parameters
Select PCE Coordinator Menu Option: parm  PCE HS/RPT Parameter Menu
PRNT   PCE HS/RPT Parameters Print
HS     PCE HS Disclaimer Edit
RPT    PCE Report Parameter Edit

```vista
Select PCE HS/RPT Parameter Menu Option: RPT  PCE Report Parameter Edit
Select PCE PARAMETERS ONE: 1
Select ER CLINIC NAME: eye
```
Are you adding 'EYE' as a new REPORT ER CLINIC NAMES (the 1ST for this PCE PARAMETERS)? y  (Yes)
Select ER CLINIC NAME: 2a
Are you adding '2A' as a new REPORT ER CLINIC NAMES (the 2ND for this PCE PARAMETERS)? y  (Yes)
Select ER CLINIC NAME: [ENTER]
Select GLUCOSE NAMES: ?
Answer with REPORT EMERGENCY CLINICS GLUCOSE NAMES
You may enter a new REPORT EMERGENCY CLINICS, if you wish
Enter the name(s) of the BLOOD GLUCOSE lab assays as they appear in
the Laboratory Test (60) file . DO NOT INCLUDE Glucose Tolerance or Fluid
Glucose test names.
LAB TEST STORED ONLY AT THE "CH" NODE
Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or
PRINT NAME
Do you want the entire LABORATORY TEST List? n  (No)
Select GLUCOSE NAMES: glu
1   GLUCAGON
2   GLUCOSE
3   GLUCOSE, OTHER
4   GLUTAMINE
5   GLUTETHIMIDE
TYPE '^' TO STOP, OR
CHOOSE 1-5:
6   GLU  URINE GLUCOSE
CHOOSE 1-6: 6  URINE GLUCOSE
Are you adding 'URINE GLUCOSE' as
a new REPORT EMERGENCY CLINICS (the 1ST for this PCE PARAMETERS)? y  (Yes)
Select GLUCOSE NAMES:[ENTER]
Select CHOLESTEROL NAMES: ??
This field will contain the names of any and all TOTAL CHOLESTEROL
assays as they appear in the Laboratory Test (60) file to allow the clinic
reporting module of the Patient Care Encounter Package to monitor Quality
of Care Markers. Entries should be made either by IRM personnel or
Clinic coordinator.
Select CHOLESTEROL NAMES: chol
1   CHOLESTEROL
2   CHOLESTEROL CRYSTALS
3   CHOLINESTERASE
4   CHOLYLGLYCINE
CHOOSE 1-4: 1
Are you adding 'CHOLESTEROL' as
a new REPORT CHOLESTEROL NAMES (the 1st for this PCE PARAMETERS)? Y  (Yes)
Select LDL CHOLESTEROL NAMES: ??
This field will contain the names of any and all LDL CHOLESTEROL assays
as they appear in the Laboratory Test (60) file to allow the clinic
reporting module of the Patient Care Encounter Package to monitor
Quality Assurance
Select LDL CHOLESTEROL NAMES:  CHOLYLGLYCINE
Are you adding 'CHOLYLGLYCINE' as a new REPORT LDL CHOLESTEROL NAMES (the 1ST for this PCE PARAMETERS)? y (Yes)
Select LDL CHOLESTEROL NAMES:[ENTER]
Select HBA1C NAMES: ?
Answer with REPORT HBA1C NAMES
You may enter a new REPORT HBA1C NAMES, if you wish
Enter the name(s) of the Glycosolated Hemoglobin assays as they
appear in the Laboratory Test (60) file.
LABS STORED ONLY AT THE "CH" NODE
Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or
PRINT NAME
Do you want the entire LABORATORY TEST List? n  (No)
Select HBA1C NAMES: glycoSYLATED HEMOGLOBIN A1C
Are you adding 'GLYCOSYLATED HEMOGLOBIN A1C' as
a new REPORT HBA1C NAMES (the 1ST for this PCE PARAMETERS)? y  (Yes)
Select HBA1C NAMES:[ENTER]
Select PCE PARAMETERS ONE:[ENTER]
    1. Make sure the following EVENTS are on the appropriate ITEM protocols:
EVENT	PROTOCOL
SDAM PCE EVENT	ITEM multiple of the PXK VISIT DATA EVENT
IBDF PCE EVENTS	ITEM multiple of the PXK VISIT DATA EVENT
PXK SDAM TO V-FILES	ITEM multiple of the SDAM APPOINTMENT EVENTS
IBDF PCE EVENTS	ITEM multiple of PXCA DATA EVENT
VSIT PATIENT STATUS	ITEM multiple of DGPM MOVEMENT EVENTS.
Example of EVENT placement on PROTOCOLS
[DVF,DEV]&gt;D P^DI
VA FileMan 21.0
Select OPTION: INQUIRE TO FILE ENTRIES
OUTPUT FROM WHAT FILE: PROTOCOL      (3091 entries)
Select PROTOCOL NAME: PXK VISIT DATA EVENT          VISIT RELATED DATA
ANOTHER ONE: SDAM APPOINTMENT EVENTS          Appointment Event Driver
ANOTHER ONE: PXCA DATA EVENT       PCE Device Interface Module's Data Event
ANOTHER ONE:DGPM MOVEMENT EVENTS....
STANDARD CAPTIONED OUTPUT? Yes// [ENTER]  (Yes)
Include COMPUTED fields:  (N/Y/R/B): NO// [ENTER] - No record number (IEN), no Computed Fields
NAME: PXK VISIT DATA EVENT              ITEM TEXT: VISIT RELATED DATA
TYPE: extended action                 CREATOR: EATON,DENIS
DESCRIPTION:   This is a Protocol that PIMS can hook onto to find the data
that was collected by PCE using List Manager, Scanning etc.
PIMS has developed a protocol, SDAM PCE EVENT, which will use the visit related data to do an auto-checkout.
ITEM: SDAM PCE EVENT
ITEM: IBDF PCE EVENT
EXIT ACTION: K PXKSPX                 ENTRY ACTION: S PXKSPX=1
TIMESTAMP: 56796,37384
NAME: SDAM APPOINTMENT EVENTS           ITEM TEXT: Appointment Event Driver
TYPE: extended action                 CREATOR: EATON,DENIS
PACKAGE: SCHEDULING
DESCRIPTION:  This extended action contains all the actions that need to
be performed when an action is taken upon an appointment, such as checking in.
ITEM: ORU PATIENT MOVMT
ITEM: IBACM OP LINK                     SEQUENCE: 1
ITEM: DG MEANS TEST REQUIRED
ITEM: VAFED EDR OUTPATIENT CAPTURE
ITEM: SDAM LATE ENTRY                   SEQUENCE: 2
ITEM: RMPR SCH EVENT                    SEQUENCE: 3
ITEM: DVBA C&amp;P SCHD EVENT               SEQUENCE: 8
ITEM: PXK SDAM TO V-FILES
ENTRY ACTION: D ANC^SDVSIT2           TIMESTAMP: 56796,37371
NAME: PXCA DATA EVENT
ITEM TEXT: PCE Device Interface Module's Data Event
TYPE: extended action                 CREATOR: EATON,DENIS
DESCRIPTION:   This is the event point invoked by PCE Device Interface Module when it has not found any errors in the data passed to it.  This makes the data available to other users of the data including users of any Local data that may be included.
ITEM: IBDF PCE EVENT
TIMESTAMP: 56796,37383
NAME: DGPM MOVEMENT EVENTS              ITEM TEXT: MOVEMENT EVENTS v 5.0
TYPE: extended action                 CREATOR: SCHLEHUBER,PAMELA
PACKAGE: REGISTRATION
DESCRIPTION:
At the completion of a patient movement the following events
take place through this option:
1. The PTF record is updated when a patient is admitted,
discharged or transferred.
2. The appointment status for a patient is updated to 'inpatient'
for admissions and 'outpatient' for discharges.  Admissions
to the domiciliary have an 'outpatient' appointment status.
3. When a patient is admitted, dietetics creates a dietetic
patient file entry and creates an admission diet order.
When a patient is discharged, all active diet
orders are discontinued.  If a patient is absent or on
pass, the diet orders are suspended.
4. Inpatient Pharmacy cancels all active orders when a patient is admitted, discharged or on unauthorized absence.
A patient cannot be given Unit Dose meds unless s/he is admitted to a ward. The patient can receive IV meds; however.
When a patient is transferred, an inpatient system parameter is used to determine whether or not the orders should be cancelled. When a patient goes on authorized absence, the inpatient system parameter is used to determine whether the orders should be cancelled, placed on hold or no action taken.
When a patient returns from authorized absence any orders placed on hold will no longer be on hold.
5. With ORDER ENTRY/RESULTS REPORTING v2.2,
MAS OE/RR NOTIFICATIONS may be displayed to
USERS defined in an OE/RR LIST for the patient. These notifications
are displayed for admissions and death discharges.
FILE LINK: 11754;DIC(19,
ITEM: ORU AUTOLIST
ITEM: ORU PATIENT MOVMT
ITEM: FHWMAS
ITEM: GMRVOR DGPM
ITEM: PSJ OR PAT ADT
ITEM: IB CATEGORY C BILLING             SEQUENCE: 10
ITEM: DG MEANS TEST DOM                 SEQUENCE: 8
ITEM: DGJ INCOMPLETE EVENT              SEQUENCE: 6
ITEM: DGOERR NOTE                       SEQUENCE: 7
ITEM: DGPM TREATING SPECIALTY EVENT     SEQUENCE: 1
ITEM: VAFED EDR INPATIENT CAPTURE
ITEM: SD APPT STATUS                    SEQUENCE: 2
ITEM: GMRADGPM MARK CHART
ITEM: YS PATIENT MOVEMENT
ITEM: DVB ADMISSION HINQ
ITEM: VSIT PATIENT STATUS
TIMESTAMP: 56803,40994
Select PROTOCOL NAME: [ENTER]
    1. Use the Visit Tracking Parameters Edit option to ensure that the entries in the VISIT TRACKING PARAMETERS file (#150.9) are correct. (This option is not on a menu¾ go through MenuMan to access it.) The post-installation routine ^VSITPOST, which is called automatically by the installation process, checks to see if the VISIT TRACKING PARAMETERS file (#150.9) has an entry. If not, it will configure it with default values.
Answer the SITE PART OF VISIT ID prompt with TEST ACCOUNT if this is in your test or training account.
Answer with the three-letter identifier for your facility if you are in production.
Example of Editing Visit Tracking Parameters
&gt;D ^XUP
Select OPTION NAME: VSIT TRACKING PARM EDIT Visit Tracking Parameters edits.
Select VISIT TRACKING PARAMETERS NAME: 1
DEFAULT TYPE: VA//[ENTER]
DEFAULT INSTITUTION: Enter your institution name here
Select PACKAGE:  PCE PATIENT CARE ENCOUNTER          PX
...OK? Yes// [ENTER]  (Yes)
PACKAGE: PCE PATIENT CARE ENCOUNTER//[ENTER]
ACTIVE FLAG: ON//[ENTER]
Select PACKAGE: SCHEDULING          SD
...OK? Yes// [ENTER] (Yes)
PACKAGE: SCHEDULING//[ENTER]
ACTIVE FLAG: OFF// ON
Select PACKAGE: ORDER ENTRY/RESULTS REPORTING         OR
...OK? Yes// [ENTER] (Yes)
PACKAGE: ORDER ENTRY/RESULTS REPORTING//[ENTER]
ACTIVE FLAG: ON//[ENTER]
Select PACKAGE:[ENTER]
SITE PART OF VISIT ID: ??
This is a three letter identifier for this computer system that is unique in the VA, or "TEST" of a test account. This is appended after a "-" onto the sequence number to form the unique Visit Id in the VA system.  It is important that this is set to the correct value and not changed.
Choose from:
ALBANY, NY      	ALN
ALBUQUERQUE, NM  ALB
ALEXANDRIA, LA   ALX
ALLEN PARK, MI   ALL     (continuing to display all sites)
Select VISIT TRACKING PARAMETERS NAME:[ENTER]
    1. Create a PXCA PCE ERROR BULLETIN mail group in MAIL GROUP file (#3.8):
&gt;D P^DI
VA FileMan 20.0
Select OPTION: ENTER OR EDIT FILE ENTRIES
INPUT TO WHAT FILE: MAIL GROUP// [ENTER]
EDIT WHICH FIELD: ALL// [ENTER]
Select MAIL GROUP NAME: PXCA PCE ERROR BULLETIN
ARE YOU ADDING 'PXCA PCE ERROR BULLETIN' AS
A NEW MAIL GROUP (THE 65TH)? Y  (YES)
Select MEMBER: USER,JOE
ARE YOU ADDING 'USER,JOE' AS A NEW MEM (THE 1ST FOR THIS MAIL GROUP)?Y(YES)
Select MEMBER: [ENTER]
DESCRIPTION:
1&gt;A mail group to send error bulletin messages from PXCA.
2&gt;Used by "PXCA PCE ERROR BULLETIN" bulletin.
3&gt;[ENTER]
EDIT Option: [ENTER]
TYPE: PU  public
ORGANIZER:[ENTER]
COORDINATOR: USER,ANOTHER//[ENTER]
Select AUTHORIZED SENDER:[ENTER]
ALLOW SELF ENROLLMENT?: NO
REFERENCE COUNT:[ENTER]
LAST REFERENCED:[ENTER]
RESTRICTIONS: LOCAL

```vista
Select MEMBER GROUP NAME:[ENTER]
Select REMOTE MEMBERS:[ENTER]
Select DISTRIBUTION LIST:[ENTER]
Select MAIL GROUP NAME:[ENTER]
Select OPTION: ENTER OR EDIT FILE ENTRIES
```
INPUT TO WHAT FILE: MAIL GROUP// BULLETIN      (86 entries)
EDIT WHICH FIELD: ALL// MAIL GROUP      (multiple)
EDIT WHICH MAIL GROUP SUB-FIELD: ALL// [ENTER]
THEN EDIT FIELD:[ENTER]
Select BULLETIN NAME: PXCA PCE ERROR BULLETIN
Select MAIL GROUP: PXCA PCE ERROR BULLETIN
ARE YOU ADDING 'PXCA PCE ERROR BULLETIN' AS
A NEW MAIL GROUP (THE 1ST FOR THIS BULLETIN)? Y  (YES)
Select MAIL GROUP:[ENTER]
Select BULLETIN NAME:[ENTER]
    1. Create VSIT CREATE ERROR as a mail group (as described above) adding appropriate members. Visit Tracking sends a message to this mail group when it has an error that prevents it from creating a visit.
    2. Activate PCE components in the Health Summary Component file.
    3. Implement the PCE Reminder/Maintenance items to appear on Health Summaries.
The Clinical Reminders feature of PCE uses a combination of PCE Table Maintenance options, PCE Clinical Reminders options, PCE Taxonomy options, Health Summary Create/Modify Health Summary Type options, and AICS Encounter Form options. The PCE User Manual Appendices document (Appendix A) provides a more detailed description of developing and customizing clinical reminders.
Follow the steps below, as applicable, to implement Clinical Reminders.
Note:  Most of these steps are optional, to be performed only if you want to modify items to meet site needs.
    - Use the List Reminder Definitions option to print the nationally distributed reminder definitions (both the "VA" and "VA-*" prefixed). Determine if you want to use the distributed definitions.
Example of List Reminder Definitions (1st page)
Select PCE IRM Main Menu Option: rm  PCE Reminder Maintenance Menu
RL     List Reminder Definitions
RI     Inquire about Reminder Item
RE     Add/Edit Reminder Item
RC     Copy Reminder Item
RA     Activate/Inactivate Reminders
RT     List Reminder Types Logic
TL     List Taxonomy Definitions
TI     Inquire about Taxonomy Item
TE     Edit Taxonomy Item
TC     Copy Taxonomy Item
TA     Activate/Inactivate Taxonomies
Select PCE Reminder Maintenance Menu Option: RL  List Reminder Definitions
DEVICE: [ENTER]   VAX    RIGHT MARGIN: 80// [ENTER]
PCE REMINDER/MAINTENANCE ITEM LIST             MAY 22,1996  08:57    PAGE 1
-----------------------------------------------------------------------
BREAST CANCER SCREEN
-----------------------------------
Print Name:                   Breast Cancer Screen
Related VA-* Reminder:        555002
Reminder Description:
Mammogram should be given every 2 years to female patients, ages 50-69.
The "VA-*Breast Cancer Screen" reminder is based on the following
"Breast Cancer Screen" guidelines specified in the "Guidelines for
Health Promotion and Disease Prevention", M-2, Part IV, Chapter 9.
Target Condition: Early detection of breast cancer.
Target Group:     All women ages 50-69.
    - Identify the reminders that your site wants to implement. Copy, as necessary, using the Copy Reminder Item option. After copying the reminders, you can alter the new reminders to meet your site's needs.
Note:  The "VA-" prefix represents the nationally distributed set. When you copy items, the VA-prefix is dropped. "VA-*" represents the minimum requirements as defined by the National Center for Health Promotion (NCHP). As an alternative, you can create a local site reminder item using the Edit Taxonomy Item option.
    - Use the Health Summary package to activate Clinical Reminders and Clinical Maintenance components. Then rebuild the Ad hoc Health Summary Type.
        1. Identify which Health Summary Type is used by the implementing clinic.
        2. Add the Clinical Reminders and/or the Clinical Maintenance components to the Health Summary Type.
        3. Edit component parameters, identifying desired selection items.
            - If a taxonomy definition related to a reminder needs modification, do the following steps:
                1. Copy the taxonomy using the Copy Taxonomy Item option.
                2. Modify the taxonomy, using the Edit Taxonomy Item option.
                3. Copy the related Reminder.
                4. Modify the Reminder to reflect the newly created taxonomy, using the Add/Edit Reminder Item option.
                5. As an alternative to copying a taxonomy, local site taxonomy items can be created, using the Edit Taxonomy Item.
            Modify the Treatment, Patient Ed, Exam, and Health Factors files, if necessary, through PCE Table Maintenance options. If clinical reminders are not showing up correctly on Health Summaries, see Appendix A-7 in the PCE User Manual Appendices document for troubleshooting information which IRM staff with programmer access can use.
                - Coordinate the use of Encounter Forms (through the AICS package) with the use of Health Summary Clinical Maintenance Components. Make sure that the relevant encounter forms contain all appropriate list bubbles for PCE data: Health Factors, Exams, Immunizations, Diagnosis, Patient Education, Procedures, and Skin Tests.
                - Inactivate reminders that will not be used, with the Activate/Inactive Reminders option.
                1. (Optional) Add Health Summary, Problem List, and Progress Notes as actions on PCE screens to allow quick access to those programs while using PCE.
            Example of adding programs to PCE screens
            &gt;D P^DI
            VA FileMan 21.0
            Select OPTION: ENTER OR EDIT FILE ENTRIES
            INPUT TO WHAT FILE: 101  PROTOCOL
            (2978 entries)
            EDIT WHICH FIELD: ALL// ITEM
            EDIT WHICH ITEM SUB-FIELD: ALL// .01  ITEM
            THEN EDIT ITEM SUB-FIELD: MNEMONIC
            THEN EDIT ITEM SUB-FIELD: [ENTER]
            THEN EDIT FIELD: [ENTER]
            Select PROTOCOL NAME: PXCE SDAM MENU               Appointment Menu      AV
            Select ITEM: PXCE BLANK HS// [ENTER]
            ITEM: PXCE BLANK HS// PXCE GMTS HS ADHOC         Health Summary        HS
            MNEMONIC: HS
            Select ITEM: PXCE BLANK PN
            ...OK? Yes//[ENTER]  (Yes)
            ITEM: PXCE BLANK PN// PXCE GMRP REVIEW SCREEN    Progress Notes        PN
            MNEMONIC: PN
            Select ITEM: PXCE BLANK PL
            ...OK? Yes// [ENTER]  (Yes)
            ITEM: PXCE BLANK PL// PXCE GMPL OE DATA ENTRY    Patient Problem List  PL
            MNEMONIC: PL
            Select ITEM:[ENTER]
            Select PROTOCOL NAME: PXCE MAIN MENU
            Select ITEM: PXCE BLANK HS// [ENTER]
            ITEM: PXCE BLANK HS// PXCE GMTS HS ADHOC         Health Summary        HS
            MNEMONIC: HS
            Select ITEM: PXCE BLANK PN
            ...OK? Yes// [ENTER]  (Yes)
            ITEM: PXCE BLANK PN// PXCE GMRP REVIEW SCREEN    Progress Notes        PN
            MNEMONIC: PN
            Select ITEM: PXCE BLANK PL
            ...OK? Yes// [ENTER]  (Yes)
            ITEM: PXCE BLANK PL// PXCE GMPL OE DATA ENTRY    Patient Problem List  PL
            MNEMONIC: PL
            Select ITEM: [ENTER]
            Select PROTOCOL NAME: [ENTER]
                1. Create a DISPOSITION CLINIC for each division in your facility using the "Set-up a Clinic" option on the Scheduling Supervisor Menu. If you are a multi-divisional facility and you want to credit disposition workload for each division, you will need to set up a DISPOSITION CLINIC for each division. Make sure you define each DISPOSITION CLINIC so that it is easily associated with the division for which you want to credit workload.
                    - If you are a single-division facility, you should define only one DISPOSITION CLINIC.
                    - The DISPOSITION CLINICS will only be used with Dispositions.
                    - PCE recommends creating a clinic defined as Disposition, with a Stop Code number of 102. This clinic should be used with all dispositions.
                    - Use "PCE Edit Disposition Clinics" option located on the "PCE Site Parameter Menu" to enter the DISPOSITION CLINICs that were defined for use with Dispositions for your facility. The purpose of this is to restrict the Hospital Location for a Disposition to DISPOSITION CLINICs only.
                    - In single-division facilities, the hospital location for Dispositions will be stuffed automatically, and you will not be prompted to select a DISPOSITION HOSPITAL LOCATION.
                PCE Edit Disposition Clinics Example
                Select PCE Site Parameter Menu Option: PCE Edit Disposition Clinics
                Select PCE PARAMETERS ONE: 1
                Select DISPOSITION HOSPITAL LOCATIONS: ?
                Answer with DISPOSITION HOSPITAL LOCATIONS
                Choose from:
                DISPOSITION 1
                DISPOSITION 2
                You may enter a new DISPOSITION HOSPITAL LOCATIONS, if you wish
                Answer with HOSPITAL LOCATION NAME, or ABBREVIATION
                Do you want the entire 58-Entry HOSPITAL LOCATION List? n
                Select DISPOSITION HOSPITAL LOCATIONS: DISPOSITION 1

### Maintenance

#### Table Maintenance Options

Table Maintenance options let sites add or edit items such as Health Factors and Education topics. Once these tables have been defined, table entries can be selected for encounter data entry via Reminder Dialogs and Encounter Forms. They can be used for clinical decision support as findings in Reminder Definitions and Reminder Terms.

The PCE Table Maintenance Menu options are:

- ED	Education Topic Management
- EX	Exam Management
- HF	Health Factor Management
- TS	Text/Keyword Search
- IMC	Inactive Mapped Codes Report
- LOT	Immunization Lot Add/Edit/Display
- DEF	Immunization Default Responses Enter/Edit
- SKC	Edit Skin Test Reading CPT Code
- INFO	PCE Information Only …

Education Topic Management, Exam Management, and Health Factor Management provide comprehensive functionality for creating, editing, and managing these data elements.

Text/Keyword Search probes a list of PCE data elements for keywords.

Inactive Mapped Codes Report searches the PCE data elements for inactive mapped codes.

Immunization Lot Add/Edit/Display provides functionality for managing vaccine inventory.

Immunization Default Responses Enter/Edit provides functionality for entering and editing default values when recording immunizations, contraindications, and refusals.

Edit Skin Test Reading CPT Code allows for entering/editing the CPT code used for skin test reading.

PCE Information Only is a link to the PCE Information Only menu.

These options may be used in conjunction with the "PCE Information Only" menu options to manage the contents of the files or tables supporting PCE.

#### PCE Information Only Menu

This is a menu of options that list information about the files/tables used by the Patient Care Encounter (PCE) package. Some of the files/tables determine what clinical data will be collected as the sites' clinical terminology for specific categories of data such as Immunizations, Skin Tests, Patient Education, and Treatments. Below is a description of the options.

PXTT LIST ACTIVE EDUC TOPICS - Active Educ. Topic List - Detailed

This lists the current detailed definition of the goals and standards defined for the active education topics.

PXTT LIST ALL EDUC TOPICS - Education Topic List

This option prints a brief list of ALL Education Topics using only two fields: Inactive Flag status and Topic Name.

PXTT INQUIRE EDUC TOPIC - Education Topic Inquiry

This option can be used to print the definition of a specific Education Topic definition.

PXTT LIST EXAMS - Exam List

This option lists all of the exam names, with their Active Status, that are defined in the Exam file for use with PCE.

PXTT LIST HEALTH FACTORS - Health Factor List

This option lists the Health Factors by Category, with their Active Status, that have been defined in the Health Factor file for use with PCE.

PXTT LIST IMMUNIZATIONS - Immunization List

This option lists all immunizations, with their Active Status, which have been defined in the Immunization file for use with PCE.

**Note:** To see what CPT codes may be related to the immunization entries, print the PCE Code Mapping List.

PXTT LIST SKIN TESTS - Skin Test List

This option lists all skin tests, with their Active Status, that have been defined in the Skin Test file for use with PCE.

PXTT LIST TREATMENTS - Treatment List

This option lists all treatments, with their active status, that have been defined in the Treatment file for use with PCE

PX PCE CODE MAPPING LIST - PCE Code Mapping List

This option allows the user to see the mapping between CPT codes and a related entry in a PCE supporting file. For example, the CPT code 90732 is related to the Immunization file entry PNEUMOCCOCAL. PCE uses the code mapping relationships to populate multiple files from one data entry step. For example, an entry of PNEUMOCCOCAL in the V Immunization file will also create a CPT entry, 90732 in the V CPT file which is then passed to PIMS.

**Note:** As of patch PX*1.0*215, the PCE CODE MAPPING file (#811.1) has been superseded. The mappings of immunizations and skin tests to CPT codes are now contained in the CODING SYSTEM multiple of the IMMUNIZATION (#9999999.14) and SKIN TEST (#9999999.28) files themselves.

PXTT FILE INQUIRY – PCE File Inquiry

This option allows a user to look up an entry from one of the PCE source files. The selectable files are limited to:

- Education Topics (#9999999.09)
- Exam (#9999999.15)
- Health Factors (#9999999.64)
- Immunization (#9999999.14)
- Imm Contraindication Reasons (#920.4)
- Imm Refusal Reasons (#920.5)
- Skin Test (#9999999.28)
- Treatment ((#9999999.17).

#### PCE Clinical Reports

The PCE Clinical Reports options provide clinicians and managers with data never before available. They extract data from various files in VISTA, including laboratory, pharmacy, and PIMS to create output reports which have been requested by physicians all over the VA. Below is a description of the options.

PXRR PATIENT ACTIVITY BY CL - Patient Activity by Clinic

This report provides a summary of patient data for one or more clinics as a measure of continuity of care.

PXRR CASELOAD PROFILE BY CL - Caseload Profile by Clinic

This report generates a profile of the patients in a clinic's caseload, given a selected date range. One or more clinics or a stop code may be selected to represent the caseload; it combines PCE encounter, Lab, Radiology, Outpatient Pharmacy, and Admissions data, with report areas of demographics, preventive medicine, quality of care markers, and utilization.

PXRR CLINIC WORKLOAD - Workload by Clinic

This report provides a summary of clinic workload based on the evaluation and management codes associated with encounters occurring within a selected date range. The report will have the most complete information if it is run for a date range where clinic activities have been documented online. The representative period of time for the selected date range may be determined by clinical staff.

PXRR MOST FREQUENT DIAGNOSES - Diagnoses Ranked by Frequency

This report lists the most frequent diagnostic codes (ICD9 or ICD10) and the most frequent diagnostic categories.

PXRR LOCATION ENCOUNTER COUNTS - Location Encounter Counts

This report counts PCE outpatient encounters in a date range by location. The location selection can be based on facility, hospital location(s), or clinic stop(s). The report can be run for all hospital locations or clinic stops in a facility or selected hospital locations or clinic stops.

PXRR PROVIDER ENCOUNTER COUNTS - Provider Encounter Counts

This report lists provider counts related to PCE outpatient encounters (in detailed or summary reports). The selection criteria includes facility, service category, provider, and date range.

## 3 File Descriptions

### PCE Patient Care Encounter Files

|   File Number | File Name                           | Global       | Data   | Journaling   |
|---------------|-------------------------------------|--------------|--------|--------------|
| 811.1         | PCE Code Mapping                    | ^PXD(811.1,  | YES    |              |
| 815           | PCE Parameters                      | ^PX(815,     | NO     |              |
| 818           | COMPACT Act Episode of Care         | ^PXCOMP(818, | YES    |              |
| 839.01        | PXCA Device Interface Module Errors | ^PX(839.01,  | NO     | ON           |
| 839.7         | Data Source                         | ^PX(839.7,   | YES    |              |
| 920           | Vaccine Information Statement       | ^AUTTIVIS(   | YES    |              |
| 920.05        | Imm Default Responses               | ^PXV(920.05, | NO     |              |
| 920.1         | Immunization Info Source            | ^PXV(920.1,  | YES    |              |
| 920.2         | Imm Administration Route            | ^PXV(920.2,  | YES    |              |
| 920.3         | Imm Administration Site (Body)      | ^PXV(920.3,  | YES    |              |
| 920.4         | Imm Contraindications               | ^PXV(920.4,  | YES    |              |
| 920.5         | Imm Refusals                        | ^PXV(920.5,  | YES    |              |
| 920.6         | Imm Routes To Sites                 | ^PXV(920.6,  | YES    |              |
| 920.71        | Imm External Agency                 | ^PXV(920.71, | NO     |              |
|   9e+06       | Patient/IHS                         | ^AUPNPAT(    | NO     | ON           |
|   9.00001e+06 | V Provider                          | ^AUPNVPRV(   | NO     | ON           |
|   9.00001e+06 | V POV                               | ^AUPNVPOV(   | NO     | ON           |
|   9.00001e+06 | V Immunization                      | ^AUPNVIMM(   | NO     | ON           |
|   9.00001e+06 | V Skin Test                         | ^AUPNVSK(    | NO     | ON           |
|   9.00001e+06 | V Exam                              | ^AUPNVXAM(   | NO     | ON           |
|   9.00001e+06 | V Treatment                         | ^AUPNVTRT(   | NO     | ON           |
|   9.00001e+06 | V Patient Ed                        | ^AUPNVPED(   | NO     | ON           |
|   9.00001e+06 | V CPT                               | ^AUPNVCPT(   | NO     | ON           |
|   9.00001e+06 | V Health Factors                    | ^AUPNVHF(    | NO     | ON           |
|   9.00001e+06 | V Imm Contra/Refusal Events         | ^AUPNVICR(   | NO     |              |
|   9.00008e+06 | V Immunization Deleted              | ^AUPDVIMM(   | NO     |              |
|   1e+07       | Imm Manufacturer                    | ^AUTTIMAN(   | YES    |              |
|   1e+07       | Location                            | ^AUTTLOC(    | NO     |              |
|   1e+07       | Education Topics                    | ^AUTTEDT(    | YES    | ON           |
|   1e+07       | Immunization                        | ^AUTTIMM(    | YES    |              |
|   1e+07       | Exam                                | ^AUTTEXAM(   | YES    |              |
|   1e+07       | Treatment                           | ^AUTTTRT(    | YES    |              |
|   1e+07       | Provider Narrative                  | ^AUTNPOV(    | NO     | ON           |
|   1e+07       | Skin Test                           | ^AUTTSK(     | YES    |              |
|   1e+07       | Immunization Lot                    | ^AUTTIML(    | NO     |              |
|   1e+07       | Health Factors                      | ^AUTTHF(     | YES    | ON           |

811.1 - PCE CODE MAPPING FILE

This file is used to map entries from two different files such as between CPT codes and a related entry in a PCE supporting file. For example, the CPT code 90732 is related to the Immunization file entry PNEUMOCCOCAL. PCE uses the code mapping relationships to populate multiple files from one data entry step. For example, an entry of PNEUMOCCOCAL in the V Immunization file will also create a CPT entry, 90732 in the V CPT file, which will then be passed to PIMS.

**NOTE:** As of patch PX*1.0*215, this file has been superseded. The mappings of immunizations and skin tests to CPT codes are now contained in the CODING SYSTEM multiple of the IMMUNIZATION (#9999999.14) and SKIN TEST (#9999999.28) files themselves.

815 - PCE PARAMETERS FILE

This file has one entry which contains parameters used by PCE. Users can set defaults for start-up views (Appointment or Encounter lists), for a range of dates that will be displayed, whether to display warnings if no diagnoses or procedures are passed, and several Health Summary/Reminders/Reports parameters.

818 – COMPACT Act Episode of Care

This file contains Episode of Care data elements that capture the Patient ID, EOC Open/Close flag, Episode Start Date, Episode End Date, Source of Crisis End, Crisis End Authorized By, Crisis End Other Comment, Benefit End Date (for Inpatient and Outpatient), Episode Final Status, Episode Source, Last COMPACT Act Administrative Eligibility, and the Remaining Inpatient and Outpatient Days of each episode for that patient. It also contains Inpatient and Outpatient extension fields: Extension Start Date, Benefit End Date, Remaining Days, Date Time Created, Start Created By, Start Authorized By, and Type of Care and Comments.

NOTE: In DG*5.3*1104 and PX*1.0*240,  the Episode of Care flag was named “Acute Suicidal Crisis flag”. In DG*5.3*1117 and PX*1.0*241, the Episode of Care flag was renamed “EOC Open/Close flag”.   The functionality and logic behind the flag did not change only the name in the file and any references to the name were also updated in DG*5.3*1117 and PX*1.0*241.

In addition, the PXCOMPACTDISP routine will display COMPACT Act Episode of Care information to the user via the PX COMPACT ACT EOC DISPLAY menu option.

This file contains pointers to the PTF file and the VISIT file. These pointers track the number of treatments for entries that were marked YES or NO.  Those marked YES indicates the treatment is related to the COMPACT Act benefit and thus, all first-party co-pays for this care should be cancelled. These Treatment For values are shared with Integrated Billing via the REQUEST^PXCOMPACTIB(FILENM,IEN) API.

In addition, Episode of Care values are shared with VHA Enrollment System via the PXCOMPACTHL7 API that creates a custom ZCA segment for the IVM Patient File, #301.5.

When FileMan errors occur related to starting a new Episode of Care, error messages are sent to the processing person, or a MailMan Group named COMPACT ACT COORDINATORS.  For the errors to go to a MailMan group, the MailMan Group must be set up at each local facility to collect these errors.  The members of this MailMan Group should be locally designated personnel that have responsibility for maintaining the data integrity of the COMPACT Act Acute Suicidal Crisis Episodes of Care.

The PX COMPACT TE BACKGROUND JOB allows the system to automatically check for Current Date &gt; the Benefit End Date and end the Episode of Care.   This Background Job sets: the EOC Open/Close Flag to NO to close the Episode of Care, sets the End Date and Benefit End Date to NOW, and marks the record with the Source of Crisis End code, ‘TE’ for Time Expired.   After the Episode of Care has ended, the system will not allow further treatment to be marked as eligible for the COMPACT Act benefit.

The PX COMPACT TE BACKGROUND JOB will be set up as part of the Post Install Instructions for release PX*1.0*240.   The Background Job should be scheduled to run once a day using the following steps:

1. Use VistA menu option XUTM SCHEDULE.
2. Enter PX COMPACT TE BACKGROUND JOB as the option.
3. Under the QUEUED TO RUN AT WHAT TIME field, enter today’s date@01:00. 
Example: MAY 1,2024@01:00
4. For the RESCHEDULING FREQUENCY field, enter 1D.
5. Enter through the rest of the prompts and Save them.

The PX COMPACT NE BACKGROUND JOB is created with the release of DG*5.3*1123 and PX*1*246 to monitor eligibility changes and end the episode of care if the patient is NOT ELIGIBLE.

The background job will be set up as part of the Post Install Instructions for release PX*1.0*246 and should be scheduled to run once a day using the following steps:

1. Use VistA menu option XUTM SCHEDULE.
2. Enter PX COMPACT NE BACKGROUND JOB as the option.
3. Under the QUEUED TO RUN AT WHAT TIME field, enter tomorrow’s date@02:00. The 2:00 am time is a recommendation only, but it is best to run this early in the morning before users log in.
4. For the RESCHEDULING FREQUENCY field, enter 1D.
5. Enter through the rest of the prompts and save them.

839.01 - PCE DEVICE INTERFACE MODULE ERROR FILE

This file holds the PXCA and PXKERROR variables when PXK returns error(s) to the device interface.

839.7 - DATA SOURCE FILE

This file holds the names of the sources that PCE receives encounter data from ¾ scanning devices, scheduling package, PCE User Interface, etc.

920 - VACCINE INFORMATION STATEMENT FILE

This file stores Vaccine Information Statements (VISs). These are information sheets produced by the Centers for Disease Control and Prevention (CDC) that explain both the benefits and risks of a vaccine to vaccine recipients.

920.05¾IMM DEFAULT RESPONSES FILE

This file stores the facility default responses for data prompts in the immunization data entry process.

920.1 - IMMUNIZATION INFO SOURCE FILE

This file is a table of standard possible sources from which the information about a particular immunization event was obtained. The data in this file are derived from the CDC-defined Immunization Information Source table (NIP001).

920.2 - IMM ADMINISTRATION ROUTE FILE

This file is a table of routes of administration for vaccines/immunization events. The data in this table are from the HL7-defined Table 0162 - Route of Administrations.

920.3 - IMM ADMINISTRATION SITE FILE

This is a table of administration sites - areas of the patient's body through which a vaccine/immunization can be administered. The values in this table are from the HL7-defined Table 0163 - Administrative site.

920.4 - IMM CONTRAINDICATIONS FILE

This is a table of contraindications regarding immunizations and skin tests. The data for this table is derived from the CDC table Vaccinations Contraindications.

920.5 - IMM REFUSALS FILE

This is a table of reason for refusal of an immunization or skin test. The data in this file has been derived from the CDC-defined table NIP002 – Substance Refusal Reason.

920.6 – IMM ROUTES TO SITES FILE

This file contains a mapping of applicable immunization administration sites for a given administration route.

920.71 – IMM EXTERNAL AGENCY

This file is used to maintain a list of external agencies (e.g., State Immunization Information Registries) to whom immunization data has been transmitted. The data in this file is automatically populated and is not editable by the end-user.

V Files – Files Originally from Indian Health Service and Involved in Joint Sharing

In all V-files, the patient name is a pointer to the IHS Patient file, and the visit is a pointer to the visit file. Both of these must exist before data can be entered into any V file. The .01 field may be duplicated in multiple records. Also, a V file can have multiple entries for a visit, to capture multiple procedures, etc. For example, a patient may have several performed; each one would be a separate entry in V-CPT, each pointing to the same patient and visit.

9000010 - VISIT

This file contains a record of all patient visits at health care facilities or by health care providers, including direct outpatient and clinic visits, as well as inpatient encounters with providers of care. All other visit related files, such as purpose of visit (diagnoses), operative procedures, immunizations, examinations, etc. will point to a visit in this file. The records are maintained by date/time of visit, and the patient name field is a pointer to the IHS Patient file, where the patient must exist before data can be added here.

9000010.06 - V PROVIDER

Stores providers related to a visit. There can be multiple providers for a given visit. The primary/ secondary field identifies which provider is considered the primary provider for this visit.

9000010.07 - V POV

Stores problems treated at a visit. At least one purpose of visit (POV) is required for workload and billing purposes for each patient outpatient visit, regardless of the discipline of the provider (i.e. dental, CHN, mental health, etc.). There is no limit to the number of POVs that can be entered for a patient for a given encounter.

9000010.11 - V IMMUNIZATION

This file contains immunizations specific to a particular visit for a particular patient.

9000010.12 - V SKIN TEST

Stores skin tests done at a visit. There will be one record for each type of skin test given to a patient on a given visit. The record is normally created when a skin test is given, and the results, if available, are entered at a later date and matched to the original record. If results are entered and a skin test given does not exist, a new record is created.

9000010.13 - V EXAM

Stores exams done at a visit which do not map to a CPT code. This file contains exam information specific to a particular visit for a particular patient.

9000010.15 - V TREATMENT

Stores miscellaneous clinical data not fitting into any other V-file global. This file contains a record for each treatment provided to a patient on a given patient visit. There will be multiple treatment records for the same treatment (.01) field based on the date on which it was given.

9000010.16 - V PATIENT ED

Stores patient education done at a visit.

9000010.18 - V CPT

Stores CPT-related services performed at a visit.

9000010.23 - V HEALTH FACTORS

Stores patient health factors as of the visit date.

9000010.707 – V IMM CONTRA/REFUSAL EVENTS

This file is used to document immunization non-administration events, capturing the reasons for not administering immunizations, either that administration was contraindicated or that it was refused by the patient.

9000080.11 – V IMMUNIZATION DELETED

Stores entries that were deleted out of the V IMMUNIZATION file (#9000010.11). Immediately prior to deleting an entry from the V IMMUNIZATION file, a copy of the record is made and filed here.

Supporting Files (evolved from IHS/VA Joint Sharing)

9000001 - Patient/HIS

This file is IHS's primary patient data file. The NAME (.01) field of this file is a pointer to the VA's patient file (#2). Fields in common between the two dictionaries actually exist only in the VA patient file and are referenced by the IHS patient file as computed fields. All other files containing patient data have backward pointers linking them to this file.  The linkage is by patient name and the internal FileMan generated number of the ancillary file is the same number used in this file.

9999999.04 - IMM MANUFACTURER

This file is a table of immunization and/or vaccine manufacturers. The data in this file are derived from the CDC (Center for Disease Control) HL7 Table 0227 (Manufacturers of Vaccines (MVX)).

9999999.06 - LOCATION

Dinumed to the Institution file (#4).

9999999.09 - EDUCATION TOPICS

This file contains Patient Education Topics. Patient Education topics are subjects on which a patient needs may receive additional health-related information to facilitate better health care habits. For example, a patient may have had some podiatry work done and therefore was instructed with information about “foot care.” The "foot care" information is in this file. It is pointed to by the V Patient Ed file.

9999999.14 - IMMUNIZATION

This file contains a list of Immunizations and is pointed to by the V Immunization file. This file contains a full descriptive name for each Immunization, a shortened name of ten characters which is used in the Health Summary Immunization components and on other clinical reports.

9999999.15 - EXAM

This file contains a list of Physical Exams and associated codes used to document Examinations performed during an Outpatient or Inpatient Encounter. This file is pointed to by V Exam file. Some of the Exams are used in Surveillance Computations.

9999999.17 - TREATMENT

This file contains Patient Treatments which are not included in the CPT codes, but are needed for clinical documentation. This file is pointed to by the V Treatment file. These treatments generally reflect nursing activities performed during a patient encounter, such as ear irrigation, or instructions or counseling given to a patient for a medical problem.

9999999.27 - PROVIDER NARRATIVE

This file contains each unique NARRATIVE QUALIFIER.

9999999.28 - SKIN TEST

This file contains Skin Tests and their associated codes. It is pointed to by V Skin Test.

9999999.41 - IMMUNIZATION LOT

This file contains the Immunization Manufacturers' LOT NUMBERS for the immunizations/vaccines administered in the VA.  The LOT NUMBERs themselves may not be unique, but the combination of LOT NUMBER and MANUFACTURER must form a unique entry. This file also relies on a nightly background task that checks the entries' EXPIRATION DATE field.  If the date is equal to that day's date, or has passed, that entry's STATUS is set to EXPIRED.

9999999.64 - HEALTH FACTORS

This file contains Health Factors terms or phrases which describe patient health characteristics (e.g., Current Smoker, Non-Tobacco User), and is pointed to by V Health Factors file. Some entries in this file are categories, used to group related health factors (e.g., Smoking).

## 4 Archiving and Purging

Archiving and purging utilities are not provided in this version of PCE. Initially, PCE was developed to provide a longitudinal database which would document patient care activities.

## 5 Callable Routines

This package provides APIs as callable entry points for use by other developers, as well as those of the PCE Device Interface, which are described in Appendix A of this manual. These APIs and entry points are all by subscription only.

$$CLNCK^SDUTL2

Patient Care Encounter application was modified to check the clinic associated with an encounter to ensure that its corresponding stop pairs conform to the stop code restriction. The following components were affected:

Routines PXBAPI1, PXCEVSIT and PXCE were modified to call API,

$$CLNCK^SDUTL2 which checks to ensure a clinic has valid stop code pairs in accordance with restriction type.

PCE APIs

$$INTV^PXAPI(WHAT,PKG,SOURCE,.VISIT,.HL,.DFN,APPT, LIMITDT,ALLHLOC)

This API should be used by subscribing packages to prompt for Visit and related V-file data. The parameters passed by the subscribing packages determine which prompts will be displayed. If VISIT, HL or DFN are passed by reference (.), a value will be returned for those variables.

Parameter Description:

WHAT

Required parameter that defines the series of prompts that will be displayed.

INTV - Includes all prompts for the checkout interview:

1. Patient (if not defined)
2. Hospital Location (if not defined)
3. Appointment/Eligibility (Call to Scheduling API if the encounter is not associated with an appointment and is a new encounter.)
4. Check Out Date/Time
5. Service Connected/Classification Questions
    - Service Connected
    - Agent Orange Exposure
    - Ionizing Radiation Exposure
    - SW Asia Conditions
    - Military Sexual Trauma
    - Head and/or Neck Cancer
    - Combat Veteran
    - Project 112/SHAD
        1. Provider (multiple)
            - Provider
            - Primary/Secondary Designation
                1. Procedures (multiple)
                    - CPT code
                    - Quantity
                        1. Diagnosis (multiple)
                            - ICD code
                            - Primary/Secondary Designation

## 6 Enhanced API

The DATA2PCE and PXCA Application Program Interface (API) Files, which are used by other packages to exchange data with the PCE files, were updated to include the CPT associated diagnoses and the diagnosis classifications of  SC, CV, AO, IR, EC, MST, HNC, and Project 12/SHAD.

$$DATA2PCE^PXAPI(INPUTROOT,PKG,SOURCE,.VISIT,USER,ERRDISP,.ERRARRAY,PPEDIT,.ERRPROB, .ACCOUNT)

This is a function which will return a value identifying the status of the call. Data that is processed by PCE will be posted on the PXK VISIT DATA EVENT protocol.

Parameter Description:

1.  INPUTROOT

(Required) Where INPUTROOT is a unique variable name, either local array or global array, which identifies the defined data elements for the encounter. An example of an INPUTROOT is ^TMP(”LRPXAPI”,$J) or ^TMP(”RAPXAPI”,$J). The gross structure of the array includes four additional subscripts (ENCOUNTER, PROVIDER, DX/PL, PROCEDURE and STOP) for defining the data passed. A detailed description of this array and its structure are included below in a table format.

2.  PKG

(Required when creating a new encounter) Where PKG is a pointer to the Package file #9.4, or the name of the package, or the Prefix.

**Note:** This field is uneditable, once the Visit has been created it cannot be changed.

3.  SOURCE

(Required when creating a new encounter) Where SOURCE is a pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. Examples of SOURCE are: “LAB DATA” or “RADIOLOGY DATA” or “PXCE DATA ENTRY” or “AICS ENCOUNTER FORM.”

**Note:** This field is uneditable, once the Visit has been created it cannot be changed.

4.  VISIT

(Optional) A dotted variable name. Where VISIT is a pointer to the Visit file (9000010) which identifies the encounter which this data should be associated with.

5.  USER

(Optional) User who is responsible for add/edit/delete action on the encounter. Pointer to the New Person file (200). If USER is not defined, DUZ will be used.

6.  ERRDISP

(Optional) To display errors during development, this variable may be set to “1”. If it is defined the errors will be displayed on screen when the error occurs. If ERRDISP is not defined, errors will be posted on the defined INPUTROOT subscripted by “DIERR”. BLD^DIALOG is used to manage errors.  Review BLD^DIALOG and MSG^DIALOG descriptions included in the FileManager v. 21.0 Programmer Manual on pages 189 - 200.

7.  ERRARRAY

(Optional) A dotted variable name. When errors and warning occur, the array will contain the PXKERROR array elements to the caller.

8.  PPEDIT

(Optional) If an existing encounter already has a Primary Provider and you want to edit it, set this to 1. See the Provider section below for the details on how this works.

9.  ERRPROB

(Optional) A dotted variable name. When errors and warnings occur, they will be passed back in the form of an array with the general description of the problem.

10.  ACCOUNT

(Optional) A dotted variable name, where ACCOUNT is the PFSS Account Reference associated with the data being passed by the calling application. Each PFSS Account Reference represents an internal entry number in the PFSS ACCOUNT file (375).

Returned Value:

1	If no errors occurred and data was processed.

-1	An error occurred. Data may or may not have been processed. If ERR\_DISPLAY is undefined; errors will be posted on the INPUT\_ROOT subscripted by “DIERR”.

-2	Unable to identify a valid VISIT. No data was processed.

-3	API was called incorrectly. No data was processed.

-4	Could not get a lock on the encounter.

-5	Warnings only were returned.

ENCOUNTER

All data must be associated with an entry in the VISIT file (9000010). Only one “ENCOUNTER” node may be passed with each call to $$DATA2PCE^PXAPI. The “ENCOUNTER” node documents encounter specific information and must be passed:

1. To create an entry in the VISIT file (#9000010). All provider, diagnosis and procedure data is related to an entry in the VISIT file.
2. To enable adding, editing or deleting existing “ENCOUNTER” node data elements. The VISIT parameter may be passed in lieu of defining an “ENCOUNTER” node.

| SUBSCRIPT                         | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ”ENCOUNTER”,1,”ENC D/T”)          | This is the encounter date/ time for primary encounters or the date for occasions of service. If the encounter is related to an appointment, this is the appointment date/time. If this is an occasion of service created by an ancillary package, this is the date/time of the instance of care.  Imprecise dates are allowed for historical encounters.  Encounter date/time may be added, but not edited. *Deletions of encounters can occur only when nothing is pointing to the encounter | R         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| “ENCOUNTER”,1,”PATIENT”)          | This is the patient DFN. This cannot be edited or deleted                                                                                                                                                                                                                                                                                                                                                                                                                                      | R         | Pointer to IHS Patient file (9000001)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “ENCOUNTER”,1,”HOS LOC”)          | This is the hospital location where the encounter took place for primary encounters, or this is the ordering location for ancillary encounters. Not required if the Service Category is “E”                                                                                                                                                                                                                                                                                                    | R         | Pointer to Hospital Location file (44)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| “ENCOUNTER”,1,”SC”)               | This encounter is related to a service connected condition                                                                                                                                                                                                                                                                                                                                                                                                                                     | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”CV”)               | This encounter is related to Combat Veteran                                                                                                                                                                                                                                                                                                                                                                                                                                                    | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”AO”)               | This encounter is related to Agent Orange exposure                                                                                                                                                                                                                                                                                                                                                                                                                                             | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”IR”)               | This encounter is related to Ionizing Radiation exposure                                                                                                                                                                                                                                                                                                                                                                                                                                       | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”EC”)               | This encounter is related to SW Asia Conditions                                                                                                                                                                                                                                                                                                                                                                                                                                                | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”SHAD”)             | This encounter is related to Project 112/SHAD                                                                                                                                                                                                                                                                                                                                                                                                                                                  | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”MST”)              | This encounter is related to Military Sexual Trauma                                                                                                                                                                                                                                                                                                                                                                                                                                            | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”HNC”)              | This encounter is related to Head and/or Neck Cancer via Nose and/or Throat Radium treatment                                                                                                                                                                                                                                                                                                                                                                                                   | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”CHECKOUT D/T”)     | This is the date/time when the encounter was checked out                                                                                                                                                                                                                                                                                                                                                                                                                                       | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| “ENCOUNTER”,1,”ELIGIBILITY”)      | This is the eligibility of the patient for this encounter                                                                                                                                                                                                                                                                                                                                                                                                                                      | O         | Pointer to Eligibility Code file (8)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “ENCOUNTER”,1,”SERVICE CATEGORY”) | This denotes the type of encounter                                                                                                                                                                                                                                                                                                                                                                                                                                                             | R         | A::=Ambulatory  Should be used for clinic encounters.  “A” s are changed to “I”s by Visit Tracking if patient is an inpatient at the time of the encounter.  H::=Hospitalization  Should be used for an admission.  I::=In Hospital  C::=Chart Review  T::=Telecommunications  N::=Not Found  S::=Day Surgery  O::=Observation  E::=Event  (Historical) Documents encounters that occur outside of this facility. Not used for workload credit or 3rd party billing.  R::=Nursing Home  D::=Daily Hospitalization Data  X::=Ancillary Package Daily Data  “X” s are changed to “D”s by Visit Tracking if patient is an inpatient at the time of the encounter |
| “ENCOUNTER”,1,”DSS ID”)           | *This is required for ancillary occasions of service such as laboratory and radiology or telephone encounters. If Hospital Location is specified, this will be set automatically, so in most cases it is not needed                                                                                                                                                                                                                                                                            | *O        | Pointer to Clinic Stop file (40.7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| “ENCOUNTER”,1,”APPT”)             | This is the appointment type of the encounter. It is not stored in the Visit file but is included on the “ELAP” node of the data published by PXK VISIT DATA EVENT                                                                                                                                                                                                                                                                                                                             | O         | Pointer to Appointment Type file (409.1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| “ENCOUNTER”,1,”OUTSIDE LOCATION”) | Free text location of service if outside the VA.  If set, then the type of visit is set to “Other”                                                                                                                                                                                                                                                                                                                                                                                             | O         | Free Text  (1-50 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “ENCOUNTER”,1,”INSTITUTION”)      | Facility of service. If set, then the type of visit is set to “VA”                                                                                                                                                                                                                                                                                                                                                                                                                             | O         | Pointer to the Location file (#9999999.06)   This field points to the Institution file (#4) and has the same internal number as that file. The Location has the same name as the Institution file (#4). The location is also referred to as the Facility                                                                                                                                                                                                                                                                                                                                                                                                      |
| “ENCOUNTER”,1,”ENCOUNTER TYPE”)   | This identifies the type of encounter, e.g., primary encounter, ancillary encounter, etc.  A “Primary” designation indicates that the encounter is associated with an appointment or is a standalone.  Examples of ancillary encounters include Laboratory and Radiology instances of care                                                                                                                                                                                                     | O         | Set of Codes.  P::=Primary  O::=Occasion of Service  S::=Stop Code  A::=Ancillary  Ancillary packages such a Laboratory and Radiology  should pass an “A”  C::=Credit Stop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “ENCOUNTER”,1,”PARENT”)           | This is the parent encounter for which the ENCOUNTER is a supporting encounter.  For example, this would be the primary encounter for which this occasion of service supports and should be associated                                                                                                                                                                                                                                                                                         | O         | Pointer to Visit file (#9000010)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “ENCOUNTER”,1,”PXACCNT”)          | This is the PFSS Account reference                                                                                                                                                                                                                                                                                                                                                                                                                                                             | O         | Pointer to PFSS Account file (#375)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| “ENCOUNTER”,1,”COMMENT”)          | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “ENCOUNTER”,1,”DELETE”)           | This is a flag that denotes deletion of the encounter entry.  Encounter will not be deleted if other data is pointing to it                                                                                                                                                                                                                                                                                                                                                                    | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Provider

The “PROVIDER” node may have multiple entries (i) and documents the provider, indicates whether he/she is the primary provider, and indicates whether the provider is the attending provider. Comments may also be passed. To delete the entire “PROVIDER” entry, set the “DELETE” node to 1.

Changing the primary provider on an encounter can be done several ways. One is to  delete the current primary provider and then add a new one. Another way is to change the primary status of the original primary provider and add a new one. Any editing of an existing primary provider requires that PPEDIT is set to 1.

| SUBSCRIPT                 | DESCRIPTION                                                                      | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------|----------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ”PROVIDER”,i,”NAME”)      | Provider’s IEN                                                                   | R         | Pointer to NEW PERSON file (200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “PROVIDER”,i,”PRIMARY”)   | Indicator that denotes this provider as the “primary” provider for the encounter | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                               |
| “PROVIDER”,i,”ATTENDING”) | Indicator that denotes this provider as the attending provider                   | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                               |
| “PROVIDER”,i,”COMMENT”)   | Comment                                                                          | O         | Free text (1 - 245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| “PROVIDER”,i,”PKG”)       | Package                                                                          | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it cannot be changed                                                                                                                                                                                                 |
| “PROVIDER”,i,”SOURCE”)    | Source                                                                           | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it cannot be changed |
| “PROVIDER”,i,”DELETE”)    | This is a flag that denotes deletion of the Provider entry                       | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### DX/PL

The “DX/PL” node may have multiple entries (i) and documents diagnoses and/or problems. Only active ICD-9-CM or ICD-10-CM codes will be accepted. The “DX/PL” node adds diagnoses to the PCE database as well as adding an active or inactive diagnosis or problem to the Problem List. If a diagnosis or problem already exists on the Problem List, this node may be used to update it. To delete the entire “DX/PL” entry from PCE (not Problem List); set the “DELETE” node to 1.

| SUBSCRIPT                     | DESCRIPTION                                                                                                                                                                             | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “DX/PL”,i,”DIAGNOSIS”)        | Diagnosis code                                                                                                                                                                          | O         | Code or Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PRIMARY”)          | Code that specifies that the diagnosis is the “primary” diagnosis for this encounter.  Only one “primary” diagnosis is recorded for each encounter                                      | N/A       | “P”::=Primary  “S”::=Secondary  Alternatively  1::=Primary  0::=Secondary                                                                                                                                                                                                                                                                                                                                                                                 |
| “DX/PL”,i,”ORD/RES”)          | Code that specifies that the diagnosis is either an “ordering” diagnosis or is a “resulting” diagnosis or both for this encounter                                                       | N/A       | “O”::=Ordering  “R”::=Resulting  “OR”::=Ordering and Resulting                                                                                                                                                                                                                                                                                                                                                                                            |
| “DX/PL”,i,”LEXICON TERM”)     | This is a term that is contained in the Clinical Lexicon                                                                                                                                | O         | Pointer to the Expressions file (757.01)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “DX/PL”,i,”PL IEN”)           | This is the problem IEN that is being acted upon.  *This node is required to edit an existing problem on the Problem List                                                               | *O        | Pointer to Problem List file (9000011)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “DX/PL”,i,”PL ADD”)           | *This is required to Add a diagnosis/problem to the Problem List. “1” indicates that the entry should be added to the Problem List                                                      | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL ACTIVE”)        | This documents whether a problem is active or inactive. The Default is Active if not specified                                                                                          | O         | A::=Active  I::=Inactive                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “DX/PL”,i,”PL ONSET DATE”)    | The date that the problem began                                                                                                                                                         | O         | FileManager Internal Format for date                                                                                                                                                                                                                                                                                                                                                                                                                      |
| “DX/PL”,i,”PL RESOLVED DATE”) | The date that the problem was resolved                                                                                                                                                  | O         | FileManager Internal Format for date                                                                                                                                                                                                                                                                                                                                                                                                                      |
| “DX/PL”,i,”NARRATIVE”)        | The provider’s description of the diagnosis/problem.  *If NARRATIVE is not passed for a diagnosis/problem, the Description from the ICD Diagnosis file (80) will be used as the default | *O        | Free text (2-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “DX/PL”,i,”CATEGORY”)         | A term that denotes a grouping or category for a set of related diagnosis/problem                                                                                                       | N/A       | Free text (2-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “DX/PL”,i,”ORD PROVIDER”)     | If the ICD code documents a procedure, this is the provider who ordered it.                                                                                                             | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “DX/PL”,i,”ENC PROVIDER”)     | Provider who documented the diagnosis/problem                                                                                                                                           | R/Add     | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “DX/PL”,i,”EVENT D/T”)        | Date/Time Diagnosis was documented                                                                                                                                                      | N/A       | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “DX/PL”,i,”COMMENT”)          | Comment                                                                                                                                                                                 | O         | DX Free Text  (1-245 char)  PL  Free Text (3-60 char)                                                                                                                                                                                                                                                                                                                                                                                                     |
| “DX/PL”,i,”PKG”)              | Package                                                                                                                                                                                 | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable. Once it has been set, it cannot be changed                                                                                                                                                                                                 |
| “DX/PL”,i,”SOURCE”)           | Source                                                                                                                                                                                  | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable. Once it has been set, it cannot be changed |
| “DX/PL”,i,”DELETE”)           | This is a delete flag used to denote deletion of the diagnosis entry                                                                                                                    | N/A       | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “DX/PL”,i,”PL SC”)            | This problem is related to a service connected condition                                                                                                                                | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL AO”)            | This problem is related to Agent Orange exposure                                                                                                                                        | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL IR”)            | This problem is related to Ionizing Radiation exposure                                                                                                                                  | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL EC”)            | This problem is related to SW Asia Conditions                                                                                                                                           | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL MST”)           | This problem is related to Military Sexual Trauma                                                                                                                                       | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL HNC”)           | This problem is related to Head and/or Neck Cancer                                                                                                                                      | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL CV”)            | This problem is related to Combat Veteran                                                                                                                                               | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “DX/PL”,i,”PL SHAD”)          | This problem is related to Project 112/SHAD                                                                                                                                             | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                |

There can only be one primary diagnosis per encounter, the data validation will check for multiple primary diagnoses and return an error if multiple primary diagnoses are found. A primary diagnosis is required for an encounter to be checked out so if no primary diagnosis is found a warning will be returned.

### Procedure

The “PROCEDURE” node may have multiple entries (i). Only active CPT/HCPCS codes will be accepted. The “PROCEDURE” node documents the procedure(s), the number of times the procedure was performed, the diagnosis the procedure is associated with and the narrative that describes the procedure. It also enables documentation of the provider who performed the procedure, the date/time the procedure was performed and any comments that are associated with the procedure. To delete the entire “PROCEDURE” entry, set the “DELETE” node to 1.

| SUBSCRIPT                              | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                       | REQ/ OPT                                          | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “PROCEDURE”,i,”PROCEDURE”)             | Procedure code                                                                                                                                                                                                                                                                                                                                                                                    | R                                                 | Code or Pointer to CPT file (81)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “PROCEDURE”,i,”MODIFIERS”, MODIFIER=”” | Modifiers associated with procedure                                                                                                                                                                                                                                                                                                                                                               | O                                                 | External or pointer to CPT Modifier file (81.3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “PROCEDURE”,i,”QTY”)                   | Number of times the procedure was performed                                                                                                                                                                                                                                                                                                                                                       | O  If a value is not entered it will default to 1 | Whole number > 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “PROCEDURE”,i,”DIAGNOSIS”)             | The first diagnosis that is associated with the identified procedure and is the primary diagnosis associated with this procedure                                                                                                                                                                                                                                                                  | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 2”)           | The second diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                             | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 3”)           | The third diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                              | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 4”)           | The fourth diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                             | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 5”)           | The fifth diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                              | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 6”)           | The sixth diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                              | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 7”)           | The seventh diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                            | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”DIAGNOSIS 8”)           | The eighth diagnosis that is associated with the identified procedure                                                                                                                                                                                                                                                                                                                             | O                                                 | Pointer to ICD Diagnosis file (80)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “PROCEDURE”,i,”NARRATIVE”)             | The provider’s description of the procedure performed. *If NARRATIVE is not passed for a procedure, the Short Name from the CPT file (81) will be used as the default                                                                                                                                                                                                                             | *O                                                | Free text (2-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “PROCEDURE”,i,”CATEGORY”)              | This field is the heading or category used to represent the provider narrative on the scanner form.  It may be useful for understanding how providers are grouping data for use on the encounter form, and may help determine clinical data base definitions in the future                                                                                                                        | O                                                 | Free text (2-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “PROCEDURE”,i,”ENC PROVIDER”)          | Provider who performed the procedure                                                                                                                                                                                                                                                                                                                                                              | O                                                 | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “PROCEDURE”,i,”ORD PROVIDER”)          | Provider who ordered the procedure                                                                                                                                                                                                                                                                                                                                                                | O                                                 | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| “PROCEDURE”,i,”ORD REFERENCE”)         | Order reference for the ordered procedure. This field is created to provide a place for the surgery package to place the pointer to the entry in the order file (#100) that is associated with this procedure                                                                                                                                                                                     | O                                                 | Pointer to Order file (100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| “PROCEDURE”,i,”EVENT D/T”)             | Date/Time procedure was done                                                                                                                                                                                                                                                                                                                                                                      | O                                                 | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| “PROCEDURE”,i,”DEPARTMENT”)            | A 3-digit code that defines the service area.  Missing Department Codes will be assigned a Department Code. The Department Code will be the Stop Code associated (in the HOSPITAL LOCATION file, #44) with the Hospital Location of the patient visit. This is stored only if the PFSS functionality is on. The value of the field Master Switch in file #372 determines whether it is on or off. | O                                                 | 108::=Laboratory  160::=Pharmacy  419::=Anesthesiology  423::=Prosthetics  180::=Oral Surgery  401::=General Surgery  402::=Cardiac Surgery  401::=General Surgery  402::=Cardiac Surgery  403::=Otorhinolaryngology (ENT)  404::=Gynecology  406::=Neurosurgery  407::=Ophthalmology  409::=Orthopedics  410::=Plastic Surgery (inc. H&amp;N)  411::=Podiatry  412::=Proctology  413::=Thoracic Surgery  415::=Peripheral Vascular  457::=Transplantation  105::=General Radiology  109::=Nuclear Medicine  109::=Cardiology Studies (Nuclear Med)  115::=Ultrasound  703::=Mammography  150::=CT Scan  151::=Magnetic Resonance Imaging  152::=Angio-Neuro-Interventional  421::=Vascular Lab |
| “PROCEDURE”,i,”COMMENT”)               | Comment                                                                                                                                                                                                                                                                                                                                                                                           | O                                                 | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| “PROCEDURE”,i,”PKG”)                   | Package                                                                                                                                                                                                                                                                                                                                                                                           | O                                                 | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it cannot be changed                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| “PROCEDURE”,i,”SOURCE”)                | Source                                                                                                                                                                                                                                                                                                                                                                                            | O                                                 | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it cannot be changed                                                                                                                                                                                                                                        |
| “PROCEDURE”,i,”DELETE”)                | This is a flag that denotes deletion of the Procedure entry                                                                                                                                                                                                                                                                                                                                       | O                                                 | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Skin Test

The “SKIN TEST” node may have multiple entries (i). To delete the entire “SKIN TEST” entry, set the “DELETE” node to 1.

| SUBSCRIPT                               | DESCRIPTION                                                                                                          | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “SKIN TEST”,i,”TEST”)                   | Skin Test code                                                                                                       | R         | Pointer to Skin Test file (9999999.28)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “SKIN TEST”,i,”READING”)                | Numeric measurement of the surface area tested (in millimeters)                                                      | O         | Whole number between 0 and 40 inclusive                                                                                                                                                                                                                                                                                                                                                                                                                   |
| “SKIN TEST”,i,”RESULT”)                 | Results of the Skin Test                                                                                             | O         | P ::=Positive  D ::=Doubtful  N ::=Negative  O ::=No Take                                                                                                                                                                                                                                                                                                                                                                                                 |
| “SKIN TEST”,i,”D/T READ”)               | Date/Time Skin Test was read                                                                                         | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “SKIN TEST”,i,”PLACEMENT”)              | Placement entry that this reading entry should be linked to. (It should only be passed in when recording a reading.) | O         | Pointer to V Skin Test file (9000010.12)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “SKIN TEST”,i,”ENC PROVIDER”)           | Provider who performed the Skin Test                                                                                 | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “SKIN TEST”,i,”EVENT D/T”)              | Date/Time Skin Test was done                                                                                         | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “SKIN TEST”,i,”COMMENT”)                | Comment                                                                                                              | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "SKIN TEST",i,"READER")                 | The person who read the skin test                                                                                    | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| "SKIN TEST",i,"ORD PROVIDER")           | The provider who ordered this skin test                                                                              | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| "SKIN TEST",i,"D/T PLACEMENT RECORDED") | The date and time of documentation of the placement of the skin test.                                                | O         | FileMan Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                     |
| "SKIN TEST",i,"ANATOMIC LOC")           | The anatomic location of skin test placement                                                                         | O         | Pointer to Imm Administration Site (Body) file (920.3)                                                                                                                                                                                                                                                                                                                                                                                                    |
| "SKIN TEST",i,"D/T READING RECORDED")   | The date and time of documentation of the reading of the skin test.                                                  | O         | FileMan Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                     |
| "SKIN TEST",i,"READING COMMENT")        | Comment related to the reading of the patient's skin test                                                            | O         | Free Text field (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| “SKIN TEST”,i,”PKG”)                    | Package                                                                                                              | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set, it cannot be changed                                                                                                                                                                                                 |
| “SKIN TEST”,i,”SOURCE”)                 | Source                                                                                                               | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed |
| “SKIN TEST”,i,”DELETE”)                 | This is a flag that denotes deletion of the Skin Test entry                                                          | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Note:** As of patch PX*1*211 ICD diagnosis codes can no longer be stored in the V SKIN TEST file. If any diagnosis codes are passed a warning will be returned in ERRARRAY and ERRPROB.

### Immunization

The “IMMUNIZATION” node may have multiple entries (i). To delete the entire “IMMUNIZATION” entry, set the “DELETE” node to 1.

| SUBSCRIPT                            | DESCRIPTION                                                                                                                                                                      | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “IMMUNIZATION”,i,”IMMUN”)            | Immunization code                                                                                                                                                                | R         | Pointer to Immunization file (9999999.14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “IMMUNIZATION”,i,”SERIES”)           | Series specifies the sequence of the series for the immunization that was administered                                                                                           | O         | P ::=Partially complete  C ::=Complete  B ::=Booster  1 ::=Series1 thru  8::=Series8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| “IMMUNIZATION”,i,”REACTION”)         | Observed reaction to the immunization                                                                                                                                            | O         | 0 ::=None  1 ::=Fever  2 ::=Irritability  3 ::=Local reaction or swelling  4 ::=Vomiting  5 ::=Rash or itching  6 ::=Lethargy  7 ::=Convulsions  8 ::=Arthritis or arthralgias  9 ::=Anaphylaxis or collapse  10 ::=Respiratory distress  11 ::=Other                                                                                                                                                                                                                                                                                                                                                                                                                      |
| “IMMUNIZATION”,i,”CONTRAINDICATED”)  | This field may be used to indicate that this immunization should not be administered again. “1” indicates that the immunization should not be given to the patient in the future | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “IMMUNIZATION”,i,”OVERRIDE REASON”)  | This is the reason for overriding the warning of existing contraindication and/or refusal  reasons                                                                               | O         | Free Text  (3-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “IMMUNIZATION”,i,” ORD BY POLICY”)   | This field indicates if this immunization was ordered by policy.                                                                                                                 | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “IMMUNIZATION”,i,”ORD PROVIDER”)     | Provider who ordered the Immunization                                                                                                                                            | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| “IMMUNIZATION”,i,”EVENT D/T”)        | Date/Time Immunization was done                                                                                                                                                  | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “IMMUNIZATION”,i,”COMMENT”)          | Comment                                                                                                                                                                          | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| “IMMUNIZATION”,i,”LOT NUM”)          | The lot number of the Immunization entered for this event                                                                                                                        | O         | Pointer to Immunization Lot file (#9999999.41)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| “IMMUNIZATION”,i,”INFO SOURCE”)      | The source of the information obtained for this immunization event                                                                                                               | O         | Pointer to Immunization Info Source file (#920.1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “IMMUNIZATION”,i,”ADMIN ROUTE”)      | The method this vaccine was administered                                                                                                                                         | O         | Pointer to Imm Administration Route file (#920.2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| “IMMUNIZATION”,i,”ANATOMIC LOC”)     | The area of the patient's body through which the vaccine was administered                                                                                                        | O         | Pointer to Imm Administration Site (Body) file (#920.3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| “IMMUNIZATION”,i,”DOSE”)             | The amount of vaccine product administered for this immunization                                                                                                                 | O         | Numeric (between 0 and 999, 2 fractional digits)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| “IMMUNIZATION”,i,”DOSE UNITS”)       | The units that reflect the actual quantity of the vaccine product administered                                                                                                   | O         | Pointer to the UCUM Codes file (#757.5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| "IMMUNIZATION",i,"VIS",SEQ #,0)      | The Vaccine Information Statement (VIS) offered to or given to the patient before administration of the immunization, and the date it was offered or given                       | O         | Format: VISIEN^DATE  "VISIEN" is a pointer to the Vaccine Information Statement file (#920). "DATE" is a date (without time) in FileManager internal format.  Note:  If the caller is updating a previously recorded immunization:  1) If the caller passes in VIS data in the "VIS" subscript, the system will purge the previously filed VIS data before filing the updates.  2) If the caller does not pass in any VIS data, the previously filed VIS data persists.  3) If the caller wants to delete the previously filed VIS without replacing it with anything else, that is done explicitly by setting the "VIS" subscript as follows: "IMMUNIZATION",i,"VIS")="@" |
| "IMMUNIZATION",i,"REMARKS", SEQ #,0) | Comments related to the immunization encounter with the patient                                                                                                                  | O         | Free-text in the format of a FileManager word-processing field.  Note:  If the caller is updating a previously recorded immunization:  1) If the caller passes in remarks in the "REMARKS" subscript, the system will purge the previously filed remarks before filing the updates.  2) If the caller does not pass in any remarks, the previously filed remarks persist.  3) If the caller wants to delete the previously filed remarks without replacing it with anything else, that is done explicitly by setting the "REMARKS" subscript as follows: "IMMUNIZATION",i, "REMARKS")="@"                                                                                  |
| "IMMUNIZATION",i,"ORD PROVIDER")     | The provider who ordered the immunization.                                                                                                                                       | O         | Pointer to New Person file (#200).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "IMMUNIZATION",i,"WARNING ACK")      | This field indicates acknowledgement of a contraindication/refusal event warning for this immunization with the decision to proceed with administration.                         | O         | [ 1 &#124; 0 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| "IMMUNIZATION",i,"OVERRIDE REASON"   | This is the reason for overriding the warning of existing contraindication and/or refusal reasons.                                                                               | O         | Free Text (3-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| "IMMUNIZATION",i,"RESULT"            | This is the interpretation of the inoculation result.                                                                                                                            | O         | T ::=Rake  N ::=No Take  I ::=Indeterminate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| "IMMUNIZATION",i,"READING"           | This is the objective, measurable reading following the inoculation.                                                                                                             | O         | Whole number between 0 and 40 inclusive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| "IMMUNIZATION",i,"D/T READ"          | This is the date and time of the reading of the immunization results.                                                                                                            | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| "IMMUNIZATION",i,"READER"            | This is the name of the person who read and interpreted the results of the inoculation.                                                                                          | O         | Pointer to New Person file (200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| "IMMUNIZATION",i,"READING COMMENT"   | This is a comment related to the reading of the patient's inoculation.                                                                                                           | O         | Free Text field (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “IMMUNIZATION”,i,”PKG”)              | Package                                                                                                                                                                          | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set, it cannot be changed                                                                                                                                                                                                                                                                                                                                                                                                                  |
| “IMMUNIZATION”,i,”SOURCE”)           | Source                                                                                                                                                                           | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set, it cannot be changed                                                                                                                                                                                                                  |
| “IMMUNIZATION”,i,”DELETE”)           | This is a flag that denotes deletion of the Immunization entry                                                                                                                   | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Note: As of patch PX*1*211 ICD diagnosis codes can no longer be stored in the V IMMUNIZATION file. If any diagnosis codes are passed a warning will be returned in ERRARRAY and ERRPROB.

### Imm Contra/Refusal

The “IMM CONTRA/REFUSAL” node may have multiple entries (i). To delete the entire “IMM CONTRA/REFUSAL” entry, set the “DELETE” node to 1.

| SUBSCRIPT                                       | DESCRIPTION                                                                                                                                                              | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "IMM CONTRA/REFUSAL",i,"CONTRA/REFUSAL")        | The Contraindication or Refusal Reason.                                                                                                                                  | R         | Variable Pointer to: IMM Contraindication Reasons file (920.4) or IMM Refusal Reasons file (920.5).                                                                                                                                                                                                                                                                                                                                                       |
| "IMM CONTRA/REFUSAL",i,"IMMUN")                 | The immunization contraindicated or refused.                                                                                                                             | R         | Pointer to Immunization file (9999999.14)                                                                                                                                                                                                                                                                                                                                                                                                                 |
| "IMM CONTRA/REFUSAL",i,"WARN UNTIL DATE")       | The date until a warning should be given for this contraindication/refusal.                                                                                              | O         | FileManager Internal Format for date.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| "IMM CONTRA/REFUSAL",i,"EVENT D/T")             | The date/time of this contraindication/refusal event.                                                                                                                    | O         | FileManager Internal Format for date/time.                                                                                                                                                                                                                                                                                                                                                                                                                |
| "IMM CONTRA/REFUSAL",i,"ENC PROVIDER")          | This is the provider who recorded the contraindication/refusal event.                                                                                                    | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "IMM CONTRA/REFUSAL",i,"REFUSED VACCINE GROUP") | When recording a refusal reason, specify if the patient is refusing all the immunizations in this vaccine group (typical), or just this specific formulation of vaccine. | O         | 0 ::=No, refused only this specific formulation of vaccine  1 ::= Yes, refused all immunizations in this vaccine group                                                                                                                                                                                                                                                                                                                                    |
| "IMM CONTRA/REFUSAL",i,"COMMENT")               | Comment                                                                                                                                                                  | O         | Free Text (1-245 characters).                                                                                                                                                                                                                                                                                                                                                                                                                             |
| “IMM CONTRA/REFUSAL”,i,”PKG”)                   | Package                                                                                                                                                                  | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed                                                                                                                                                                                                 |
| “IMM CONTRA/REFUSAL”,i,”SOURCE”)                | Source                                                                                                                                                                   | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed |
| “IMM CONTRA/REFUSAL”,i,”DELETE”)                | This is a flag that denotes deletion of the IMM Contra/Refusal entry                                                                                                     | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Education Topics

The “PATIENT ED” node may have multiple entries (i). To delete the entire “PATIENT ED” entry, set the “DELETE” node to 1.

| SUBSCRIPT                      | DESCRIPTION                                                    | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------|----------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “PATIENT ED”,i,”TOPIC”)        | Education Topic                                                | R         | Pointer to Education Topics file (9999999.09)                                                                                                                                                                                                                                                                                                                                                                                                             |
| “PATIENT ED”,i,”UNDERSTANDING) | Level of Understanding                                         | O         | Set of Codes  1=Poor  2=Fair  3=Good  4=Group-no assessment  5=Refused                                                                                                                                                                                                                                                                                                                                                                                    |
| “PATIENT ED”,i,”EVENT D/T”)    | Date/Time education was given                                  | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “PATIENT ED”,i,”COMMENT”)      | Comment                                                        | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "PATIENT ED",i,"ORD PROVIDER") | The provider who ordered the education                         | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "PATIENT ED",i,"ENC PROVIDER") | The provider who gave the education                            | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “PATIENT ED”,i,”MAGNITUDE”)    | The size of the measurement associated with the entry          | O         | Numeric (in the range defined by Minimum Value, Maximum Value, and Maximum Decimals)                                                                                                                                                                                                                                                                                                                                                                      |
| “PATIENT ED”,i,”PKG”)          | Package                                                        | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed                                                                                                                                                                                                 |
| “PATIENT ED”,i,”SOURCE”)       | Source                                                         | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed |
| “PATIENT ED”,i,”DELETE”)       | This is a flag that denotes deletion of the V Patient ED entry | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Exams

The “EXAM” node may have multiple entries (i). To delete the entire “EXAM” entry, set the “DELETE” node to 1.

| SUBSCRIPT                | DESCRIPTION                                              | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------|----------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “EXAM”,i,”EXAM”)         | Exam                                                     | R         | Pointer to Exam file (9999999.15)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “EXAM”,i,”RESULT”)       | Result                                                   | O         | Set of Codes  A=ABNORMAL  N=NORMAL                                                                                                                                                                                                                                                                                                                                                                                                                        |
| “EXAM”,i,”EVENT D/T”)    | Date/Time exam was performed                             | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “EXAM”,i,”COMMENT”)      | Comment                                                  | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "EXAM",i,"ORD PROVIDER") | The provider who ordered the exam                        | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "EXAM",i,"ENC PROVIDER") | The provider who performed the exam                      | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “EXAM”,i,”MAGNITUDE”)    | The size of the measurement associated with the exam     | O         | Numeric (in the range defined by Minimum Value, Maximum Value, and Maximum Decimals)                                                                                                                                                                                                                                                                                                                                                                      |
| “EXAM”,i,”PKG”)          | Package                                                  | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed                                                                                                                                                                                                 |
| “EXAM”,i,”SOURCE”)       | Source                                                   | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed |
| “EXAM”,i,”DELETE”)       | This is a flag that denotes deletion of the V Exam entry | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Health Factors

The “HEALTH FACTOR” node may have multiple entries (i). To delete the entire “HEALTH FACTOR” entry, set the “DELETE” node to 1.

| SUBSCRIPT                           | DESCRIPTION                                                       | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------|-------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “HEALTH FACTOR”,i,”HEALTH FACTOR”)  | Health Factor                                                     | R         | Pointer to HEALTH FACTOR file (9999999.64)                                                                                                                                                                                                                                                                                                                                                                                                                |
| “HEALTH FACTOR”,i,”LEVEL/SEVERITY”) | Level/Severity                                                    | O         | Set of Codes  M=MINIMAL  MO=MODERATE  H=HEAVY/SEVERE                                                                                                                                                                                                                                                                                                                                                                                                      |
| “HEALTH FACTOR”,i,”EVENT D/T”)      | Date/Time health factor was given                                 | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “HEALTH FACTOR”,i,”COMMENT”)        | Comment                                                           | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "HEALTH FACTOR",i,"ORD PROVIDER")   | The provider who ordered the health factor                        | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "HEALTH FACTOR",i,"ENC PROVIDER")   | The provider who documented the health factor                     | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “HEALTH FACTOR”,i,”MAGNITUDE”)      | The size of the measurement associated with the health factor     | O         | Numeric (in the range defined by Minimum Value, Maximum Value, and Maximum Decimals)                                                                                                                                                                                                                                                                                                                                                                      |
| “HEALTH FACTOR”,i,”PKG”)            | Package                                                           | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed                                                                                                                                                                                                 |
| “HEALTH FACTOR”,i,”SOURCE”)         | Source                                                            | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set it, cannot be changed |
| “HEALTH FACTOR”,i,”DELETE”)         | This is a flag that denotes deletion of the V Health Factor entry | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Standard Codes

The “STD CODES” node may have multiple entries (i). To delete the entire “STD CODES” entry, set the “DELETE” node to 1.

| ## SUBSCRIPT  ### 6.11 Example of Data Passed Using $DATA2PCE^PXAPI  Below is an example of data passed to $$DATA2PCE^PXAPI where Laboratory is the ancillary package reporting the data.  $$DATA2PCE^PXAPI(“^TMP(““LRPXAPI””,$J)”,182,“LAB DATA”)  This is an example where Laboratory passes two laboratory tests (Glucose and CPK) which were collected on 3/27/03 at 12:00 P.m. The provider who resulted the tests is Fred Jones. This occasion of service is defined as an Ancillary Package Daily Data (X). There are two diagnoses to support the tests, both of which are non–service connected; however, both are associated with Agent Orange exposure.  ^TMP(“LRPXAPI”,543173595,"DX/PL”,1,”DIAGNOSIS”)=465  ^TMP(“LRPXAPI”,543173595,"DX/PL”,1,”PRIMARY”)=1  ^TMP(“LRPXAPI”,543173595,"DX/PL”,1,”PL SC”)=0  ^TMP(“LRPXAPI”,543173595,"DX/PL”,1,”PL AO”)=1  ^TMP(“LRPXAPI”,543173595,"DX/PL”,2,”DIAGNOSIS”)=466  ^TMP(“LRPXAPI”,543173595,"DX/PL”,2,”PL SC”)=0  ^TMP(“LRPXAPI”,543173595,"DX/PL”,2,”PL AO”)=1  ^TMP(“LRPXAPI”,543173595,"ENCOUNTER",1,"DSS ID") = 59  ^TMP(“LRPXAPI”,543173595,"ENCOUNTER",1,"ENC D/T") = 3030328  ^TMP(“LRPXAPI”,543173595,"ENCOUNTER",1,"HOS LOC") = 19  ^TMP(“LRPXAPI”,543173595,"ENCOUNTER",1,"PATIENT") = 281  ^TMP(“LRPXAPI”,543173595,"ENCOUNTER",1,"SERVICE CATEGORY") = X  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"ENC PROVIDER") = 58  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"ORD PROVIDER") = 66  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"EVENT D/T") = 3030327.12  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"PROCEDURE") = 82950  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"DIAGNOSIS") = 465  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"DIAGNOSIS 2") = 466  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"MODIFIER”,22)=””  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",1,"QTY") = 1  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"ENC PROVIDER") = 58  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"ORD PROVIDER") = 66  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"EVENT D/T") = 3030327.12  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"PROCEDURE") = 82552  ^TMP(“LRPXAPI”,543173595,"PROCEDURE",2,"QTY") = 1  ### 6.12 DATA2PCE Return Values and Error Arrays  Returns:  1  	If no errors and process completely.  -1  	If errors occurred but processed completely as possible.  -2  	If could not get a visit.  -3  	If called incorrectly.  -4  	If could not get a lock on the encounter.  -5	Warnings only were returned.  Detailed validation/verification errors in ERRARRY and summary in ERRPROB. Processing errors are put into PXKERROR which are returned in ERRARRY. If ERRDISP is not defined errors will also be returned in INPUTROOT(“DIERR”).  The first subscript of ERRARRY is the data type, i.e., “DX/PL”, “HEALTH FACTOR”, etc. The second subscript the entry number, the first “DX/PL”, the second “DX/PL” etc. The third subscript is the line number of the output. For example:  ERRARRAY("DX/PL",1,1)="ERROR MESSAGE FROM DATA2PCE^PXAPI"  ERRARRAY("DX/PL",1,2)="TO: 1342  XXXXX,YYYYY  ERRARRAY("DX/PL",1,3)=""  ERRARRAY("DX/PL",1,4)="250.01 is NOT an Active ICD code."  ERRARRAY("DX/PL",1,5)=" "  ERRARRAY("DX/PL",1,6)="INPUT..""DX/PL"",1,""DIAGNOSIS"")=250.01"  ERRARRAY("DX/PL",1,7)="       "  ERRARRAY("DX/PL",1,8)=""  ERRARRAY("DX/PL",1,9)="Calling Package .... -1"  ERRARRAY("DX/PL",1,10)="Source ............. -1"  ERRARRAY("DX/PL",1,11)="Visit Pointer ...... 8508"  ERRARRAY("DX/PL",1,12)="User ............... 1342  XXXX,YYY"  ERRARRAY("DX/PL",2,1)="ERRARRAY MESSAGE FROM DATA2PCE^PXAPI"  ERRARRAY("DX/PL",2,2)="TO: 1342  XXXX,YYY"  ERRARRAY("DX/PL",2,3)=""  ERRARRAY("DX/PL",2,4)="The ICD diagnosis is missing."  ERRARRAY("DX/PL",2,5)=" "  ERRARRAY("DX/PL",2,6)="INPUT..""DX/PL"",2,""DIAGNOSIS"")="  ERRARRAY("DX/PL",2,7)="       "  ERRARRAY("DX/PL",2,8)=""  ERRARRAY("DX/PL",2,9)="Calling Package .... -1"  ERRARRAY("DX/PL",2,10)="Source ............. -1"  ERRARRAY("DX/PL",2,11)="Visit Pointer ...... 8508"  ERRARRAY("DX/PL",2,12)="User ............... 1342  XXXX,YYY"  If present, ERRPROB will contain errors and warnings with a general description of the problem.  The third subscript of ERRPROB defines what type of information is being passed back. If it is “ERROR1” then ERRPROB will contain general errors in the format:  ERRPROB($J,COUNT,"ERROR1",PASSED IN 'FILE',PASSED IN FIELD, INPUT SUBSCRIPT)=Error message  Where  COUNT is an integer that starts at 1 and is incremented for each distinct entry in ERRPROB  PASSED IN FILE is the name of the data type  PASSED IN FIELD is the name of the field  INPUT SUBSCRIPT is the subscript of the item in INPUTROOT  For example, if INPUTROOT is:  INPUT("EXAM",1,"EXAM")=660004  INPUT("EXAM",1,"EVENT D/T")=3160802.09  INPUT("EXAM",1,"MAGNITUDE")=123.4  INPUT("EXAM",1,"UCUM CODE")=20  INPUT SUBSCRIPT=1, PASSED IN FILE=EXAM, the PASSED IN FIELDS are: EXAM, EVENT D/T, MAGNITUDE, and UCUM CODE.  When the third subscript is “ERROR4” errors specific to adding to Problem List are being returned:  ERRPROB($J,6,"ERROR4","PX/DL", INPUT SUBSCRIPT)=Error message  When the third subscript is “WARNING2” then a general warning is being returned:  ERRPROB($J,3,"WARNING2","PROCEDURE","QTY",INPUT SUBSCRPT)=Warning  When it is “WARNING3” warnings specific to Service Connection are being returned:  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"AO")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"EC")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"IR")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"SC")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"MST")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"HNC")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"CV")=Warning message  ERRPROB($J,1,"WARNING3","ENCOUNTER”,1,"SHAD")=Warning message  Errors will also be returned in the INPUT array.  ### 6.13 $$CLNCK^SDUTL2(CLN,DSP)  This API will be used by the subscribing package to check the clinic associated with an encounter to ensure that its corresponding stop pairs conform to the stop code restriction. Effective 10/1/2003, stop codes (also known as DSS Identifiers) are assigned a restriction type of primary, secondary, or either. Primary types can only be used in the primary stop code position; secondary types can only be used in the secondary stop code position; and those with a type of either can be used in the primary or secondary stop code position.  Stop codes that have a restriction type of primary or secondary will also have a restriction date to track when the stop code is designated as a restricted stop code.  Parameter Description:  CLN	The internal entry number of the clinic from file #44  DSP	Interactive display of error message, 1 - Display or 0 No Display  Returned Value:  1	If clinic has conforming stop codes.  0^error	If clinic has non-conforming stop codes plus error message.   | DESCRIPTION                                                        | REQ/OPT   | DATA FORMAT                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “STD CODES”,i,”CODE”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Code from the specified coding system                              | R         | Text                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| “STD CODES”,i,”CODING SYSTEM”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Coding system                                                      | R         | Lexicon Standard Abbreviation  SCT= SNOMED CT                                                                                                                                                                                                                                                                                                                                                                                                             |
| “STD CODES”,i,”EVENT D/T”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Date/Time code was recorded                                        | O         | FileManager Internal Format for date/time                                                                                                                                                                                                                                                                                                                                                                                                                 |
| “STD CODES”,i,”COMMENT”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Comment                                                            | O         | Free Text  (1-245 characters)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "STD CODES",i,"ORD PROVIDER")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The provider who ordered the code                                  | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "STD CODES",i,"ENC PROVIDER")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The provider who documented the code or performed the procedure    | O         | Pointer to New Person file (#200)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| “STD CODES”,i,”MAGNITUDE”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The size of the measurement associated with the entry              | O         | Numeric                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| “STD CODES”,i,”UCUM CODE”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The units for the measurement associated with this entry           | O         | Pointer to the UCUM Codes file (#757.5)                                                                                                                                                                                                                                                                                                                                                                                                                   |
| “STD CODES”,i,”PKG”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Package                                                            | O         | A pointer to the Package file #(9.4), or the name of the package, or the Prefix. This only needs to be included if it is different than the Package stored with the Visit. Note that this field is uneditable, once it has been set, it cannot be changed                                                                                                                                                                                                 |
| “STD CODES”,i,”SOURCE”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Source                                                             | O         | A pointer to the PCE Data Source file (#839.7) or a string of text (3-64 characters) identifying the source of the data. The text is the SOURCE NAME field (.01) of the PCE Data Source file (#839.7). If the SOURCE currently does not exist in the file, it will be added. This only needs to be included if it is different than the Data Source stored with the Visit. Note that this field is uneditable, once it has been set, it cannot be changed |
| “STD CODES”,i,”DELETE”)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This is a flag that denotes deletion of the V Standard Codes entry | O         | [ 1 &#124; null ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 7 External Relations

PCE is dependent upon the following **relationships** :

| Vista Package                                                     | Minimum Version   |
|-------------------------------------------------------------------|-------------------|
| Kernel                                                            | 8.0               |
| VA FileMan                                                        | 21                |
| Patient Information Management System (PIMS)                      | 5.3               |
| Order Entry/Results Reporting (OE/RR)                             | 2.5               |
| Automated Information Collection System (AICS)                    | 2.1               |
| PCE Patient/IHS Subset (PXPT)                                     | 1.0               |
| VA Enrollment System*                                             | Minimum Version   |
| Web Service – Eligibility and Enrollment Service (aka E&E Service |                   |

*Access to this service allows for one of the COMPACT Act Administrative Eligibility Statuses (Eligible, Undetermined, Not-Eligible) to be retrieved and to retrieve updates to the status as cases are adjudicated by Member Services.

## 8 Package-Wide Variables

No package-wide variables have been defined for use throughout the Patient Care Encounter package.

The PX namespace is reserved for use by PCE; however, the joint sharing of files between the Department of Veterans Affairs and the Indian Health Service has necessitated use of some AU-name spaced variables established for use by the Indian Health Service and by the Department of Veterans Affairs to facilitate joint sharing.

## 9 Integration Control Registrations

Integration Control Registrations (ICRs) are available on the DBA menu on Forum.

## 10 Remote Procedure Call

### PX Save Data

An integration control registration (ICR #6023) for the remote procedure call PX SAVE DATA is available for subscription by calling applications.

NAME: PX SAVE DATA                      TAG: SAVE

ROUTINE: PXRPC                        RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            APP PROXY ALLOWED: Yes

DESCRIPTION:

The purpose of this RPC is to allow the calling application to save data

to PCE, such as Immunization data. See the Integration Control

Registration document for the full description of the data needed.

INPUT PARAMETER: PCELIST                PARAMETER TYPE: LIST

MAXIMUM DATA LENGTH: 10000            REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

PCELIST (n)=VST^DT^Encounter date/time

(n)=VST^PT^Encounter patient (DFN)

(n)=VST^HL^Encounter location

(n)=VST^VC^ Encounter Service Category

(n)=VST^ET^Encounter Type (defaults to 'P')

If  applicable:

(n)=VST^PR^ Parent for secondary visit

(n)=VST^OL^ Outside Location for Historical visits

(n)=VST^SC^ Service Connected related?

(n)=VST^AO^ Agent Orange related?

(n)=VST^IR^ Ionizing Radiation related?

(n)=VST^EC^ Environmental Contaminates related?

(n)=VST^MST^ Military Sexual Trauma related?

(n)=VST^HNC^ Head and/or Neck Cancer related?

(n)=VST^CV^ Combat Vet related?

(n)=VST^SHD^ Shipboard Hazard and Defense related?

(n)=PRV(+:  add, -: delete) ^ Provider IEN ^^^ Provider Name ^

Primary Provider?

(n)=POV(+:  add, -: delete) ^ ICD diagnosis code ^ Category  ^

Narrative (Diagnosis description) ^ Primary Diagnosis? ^

Provider String ^ Add to Problem List? ^^^ Next comment

sequence # if saving comments

(n)=COM^COM (Comments) ^ Next comment sequence # ^ @ = no

comments added

(n)=CPT (+:  add, -: delete) ^ Procedural  CPT code ^ Category ^

Narrative (Procedure description) ^ Quantity ^ Provider IEN

^^^ [# of modifiers;  Modifier code/Modifier IEN ^ Next

comment sequence # ^

(n)=IMM (+:  add, -: delete) ^ Immunization IEN ^ Category ^

Narrative (Immunization description/name) ^ Series ^

Encounter Provider ^ Reaction ^ Contraindicated? ^ ^

Next comment sequence # ^ CVX Code ^ Event Info Source HL7

Code;IEN ^ Dose;Units;Units IEN ^ Route Name;HL7 Code;IEN ^

Admin Site Name;HL7 Code;IEN ^ Lot#;IEN ^ Manufacturer ^

Expiration Date ^ Event Date and Time ^ Ordering Provider ^

VIS IEN/VIS Date; VIS IEN n/VIS Date n ^ Remarks Start Seq

#;Remarks End Seq # ^ Warning Ack ^ Override Reason (Seq #)

^ Result (Smallpox) ^ Reading ^ D/T Read ^ Reader ^ Reading

Comment Seq # ^ V Immunization IEN (should only be populated

for a reading) ^ Ordered By Policy

(n)=SK (+:  add, -: delete) ^ Skin Test IEN ^ Category ^

Narrative (Skin Test description/name) ^ Results ^ Enc

Provider ^ Reading ^ D/T Read ^ ^ Next comment sequence # ^

Reader ^ ^ ^ Reading Comment (Seq #) ^ Anatomic Location of

Placement;HL7 Code;IEN ^ Placement V Skin Test IEN ^ ^ ^ Event

D/T ^ Ordering Provider

(n)=PED (+:  add, -: delete) ^ Patient Education IEN ^ Category ^

Narrative (Patient Education description/name) ^ Level of

understanding ^^^^^ ^^ Next comment sequence #

(n)=HF (+:  add, -: delete) ^ Health Factor IEN ^ Category ^

Narrative (Health Factor description/name) ^ Level ^^^^^ Next

comment sequence # ^ Get Reminder

(n)=XAM(+:  add, -: delete) ^ Exam IEN ^ Category ^ Narrative

(Exam description/name) ^ Results ^^^^^ Next comment sequence


(n)=ICR (+:  add, -: delete) ^ Variable Pointer IMM

Contraindication Reasons/IMM Refusal Reasons ^ Category ^

Narrative ^ Immunization IEN ^ Warn Until Date ^ Event

Date/Time ^ Enc Provider IEN ^ Refused Vaccine Group

^ Next comment sequence #

(n)=SC (+:  add, -: delete) ^ Code ^ Category ^ Narrative ^

Coding System ^ Enc Provider ^ Magnitude ^ UCUM Code ^ ^ Next

comment sequence # ^ Event D/T ^ Ordering Provider

INPUT PARAMETER: LOC                    PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 40               REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

This is the hospital location. This is not used when the information is

from an outside source.

INPUT PARAMETER: PKGNAME                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 3

DESCRIPTION:

The package name that is sending the data to PCE. This should be the

full package name, such as PATIENT CARE ENCOUNTERS.

INPUT PARAMETER: SRC                    PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 4

DESCRIPTION:

The source of the data - such as VLER E-HEALTH EXCHANGE.

INPUT PARAMETER: VISIT                  PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: NO

SEQUENCE NUMBER: 5

DESCRIPTION:

(Optional) A pointer to the Visit file (9000010), which identifies the

encounter that this data should be associated with.

INPUT PARAMETER: RETVISIT               PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 6

DESCRIPTION:

Set to 1 if you want the Visit IEN to be returned to the calling

application.

RETURN PARAMETER DESCRIPTION:

The only return will be the one passed back to the calling application.

Returned Value:

1  If no errors occurred and data was processed.

-1  If errors occurred, but data was processed as completely as possible.

-2  Unable to identify a valid Visit. No data was processed.

-3  RPC was called incorrectly. No data was processed.

-4  If cannot get a lock on the encounter.

-5  If there were only warnings.

Optionally, if the argument RETVISIT was "1", than the Visit IEN will be

returned as the second piece (e.g., "1^65234").

### PXVIMM ADMIN CODES

NAME: PXVIMM ADMIN CODES                TAG: IMMADMCD

ROUTINE: PXVRPC4                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns immunization administration CPT codes.

INPUT PARAMETER: PXDATE                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Code status will be based off this date. (Optional; Defaults to TODAY).

RETURN PARAMETER DESCRIPTION:

PXRSLT(0) = Count of elements returned (0 if nothing found)

PXRSLT(n) =

Note: Only active codes (based off PXDATE) are returned.

1: "CPT-ADM" or "CPT-ADD"

2: Code

3: Variable pointer. e.g., IEN;ICPT(

4: Short Description

### PXVIMM ADMIN ROUTE

NAME: PXVIMM ADMIN ROUTE                TAG: IMMROUTE

ROUTINE: PXVRPC2                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns entries from the IMM ADMINISTRATION ROUTE file (920.2).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Filter. Possible values are:

R:XXX - Return entry with IEN XXX.

H:XXX - Return entry with HL7 Code XXX.

N:XXX - Return entry with #.01 field equal to XXX

S:X   - Return all entries with a status of X.

Possible values of X:

A - Active Entries

I - Inactive Entries

B - Both active and inactive entries

Defaults to "S:B".

INPUT PARAMETER: PXVSITES               PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:

Controls if the available sites for a give route are returned.

RETURN PARAMETER DESCRIPTION:

PXVRSLT(0)=Count of elements returned (0 if nothing found)

PXVRSLT(n)=IEN^Name^HL7 Code^Status (1:Active, 0:Inactive)

If PXVSITES=1, the sites for a given route will also be returned.

o If only a subset of sites are selectable for a route, that list will

be returned in:

PXVRSLT(n+1)=SITE^Site IEN 1

PXVRSLT(n+2)=SITE^Site IEN 2

PXVRSLT(n+x)=SITE^Site IEN x

o If all sites are selectable for a route, the RPC will return:

PXVRSLT(n+1)=SITE^ALL

o If no sites are selectable for a route, the RPC will return:

PXVRSLT(n+1)=SITE^NONE

equal 0, and there will be no data returned in the subsequent subscripts.

### PXVIMM ADMIN SITE

NAME: PXVIMM ADMIN SITE                 TAG: IMMSITE

ROUTINE: PXVRPC2                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns entries from the IMM ADMINISTRATION SITE (BODY) file (920.3).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Filter. Possible values are:

R:XXX - Return entry with IEN XXX.

H:XXX - Return entry with HL7 Code XXX.

N:XXX - Return entry with #.01 field equal to XXX

S:X   - Return all entries with a status of X.

Possible values of X:

A - Active Entries

I - Inactive Entries

B - Both active and inactive entries

Defaults to "S:B".

RETURN PARAMETER DESCRIPTION:

Returns:

PXVRSLT(0)=Count of elements returned (0 if nothing found)

PXVRSLT(n)=IEN^Name^HL7 Code^Status (1:Active, 0:Inactive)

When filtering based off IEN, HL7 Code, or #.01 field, only one entry will

be returned in PXVRSLT(1).

When filtering based off status, multiple entries can be returned. The

first entry will be returned in subscript 1, and subscripts will be

incremented by 1 for further entries. Entries will be sorted

alphabetically.

If no entries are found based off the filtering criteria, PXVRSLT(0) will

equal 0, and there will be no data returned in the subsequent subscripts.

### PXVIMM ICR LIST

NAME: PXVIMM ICR LIST                   TAG: GETICR

ROUTINE: PXVRPC5                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns entries from the IMM CONTRAINDICATION REASONS (#920.4) and IMM

REFUSAL REASONS (#920.5) files.

INPUT PARAMETER: PXFILE                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Which file to pull from.

(Optional; Leave this null to pull entries from both files)

Possible values are:

"920.4" - Only return entries from IMM CONTRAINDICATION REASONS

(#920.4)

"920.5" - Only return entries from IMM REFUSAL REASONS (#920.5)

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:

Filter (Optional; Defaults to "S:A")

Possible values are:

R:X   - Return entry with IEN X (PXFILE must be passed in with this

option).

C:X^Y - Return entry with Concept Code^Coding System X^Y (used only for

#920.4).

H:X   - Return entry with HL7 Code X (used only for #920.5).

N:X   - Return entry with #.01 field equal to X

I:X   - Return all active entries that are selectable for Immunization

IEN X.

S:A   - Return all active entries.

S:I   - Return all inactive entries.

S:B   - Return all entries (both active and inactive.

INPUT PARAMETER: PXINST                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Institution IEN

INPUT PARAMETER: PXLOC                  PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Location IEN (If Institution IEN is not passed in, the loc will be used to

get the institution).

RETURN PARAMETER DESCRIPTION:

PXRSLT(0)=Count of elements returned (0 if nothing found)

For 920.4 Entry:

PXRSLT(n)=IEN;PXV(920.4,^Name^Status (1:Active, 0:Inactive)^Code|Coding

System^NIP004^Contraindication/Precaution^Allergy-Related

(1:Yes, 0:No) ^ Default Warn Until Date ("Forever" means it should be

forever)

For 920.5 Entry:

PXRSLT(n)=IEN;PXV(920.5,^Name^Status (1:Active, 0:Inactive)^HL7 Code ^ Default

Warn Until Date ("Forever" means it should be forever)

### PXVMM IMM DETAILED

NAME: PXVIMM IMM DETAILED               TAG: IMMRPC

ROUTINE: PXVRPC4                      RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION:

Returns a detailed Immunization record

INPUT PARAMETER: PXIMM                  PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

Pointer to #9999999.14 (Required)

INPUT PARAMETER: PXDATE                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:

Immunization status and Codes will be based off this date

(Optional; Defaults to NOW)

INPUT PARAMETER: PXLOC                  PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 3

DESCRIPTION:

Used to determine Institution, when filtering Lot and Defaults (Optional).

Possible values are:

"I:X": Institution (#4) IEN #X

"V:X": Visit (#9000010) IEN #X

"L:X": Hopital Location (#44) IEN #X

If PXLOC is not passed in OR could not make determination based off input,

then default to DUZ(2), and if DUZ(2) is not defined, default to Default

Institution.

RETURN PARAMETER DESCRIPTION:

^TMP("PXVIMMRPC",$J,0)

1:  1 - Immunization was found. The "1" node will be returned, but the

other nodes are optional.

-1 - Immunization was not found; no other nodes will be returned

^TMP("PXVIMMRPC",$J,1)

Note: Status (in the 5th piece) is determined as follows:

- If PXDATE is today, the status is based off the Inactive Flag

(#.07)

- If PXDATE is different than today, we will look when an update was

last made to the Immunization file (based off the Audits). If there

have not been any changes since PXDATE, we will get the status

based off the Inactive Flag, otherwise, we will get the status for

that date by calling GETSTAT^XTID.

1: "IMM"

2: #9999999.14 IEN

3: Name (#.01)

4: CVX Code (#.03)

5: Status (1: Active; 0: Inactive)

6: Selectable for Historic (#8803)

7: Mnemonic (#8801)

8: Acronym (#8802)

9: Max # In Series (#.05)

10: Combination Immunization (Y/N) (#.2)

11: Reading Required (#.51)

12: Series Required (calculated)

^TMP("PXVIMMRPC",$J,x)

1: "VIS"

2: #920 IEN

3: Name (#920,#.01)

4: Edition Date (#920,#.02)

5: Edition Status (#920,#.03)

6: Language (#920, #.04)

7: 2D Bar Code (#100)

8: VIS URL (#101)

^TMP("PXVIMMRPC",$J,x)

1: "CDC"

2: CDC Product Name (#9999999.145, #.01)

^TMP("PXVIMMRPC",$J,x)

1: "GROUP"

2: Vaccine Group Name (#9999999.147, #.01)

^TMP("PXVIMMRPC",$J,x)

1: "SYNONYM"

2: Synonym (#9999999.141, #.01)

^TMP("PXVIMMRPC",$J,x)

Note: Only active codes (based off PXDATE) are returned.

1: "CS"

2: Coding System (#9999999.143, #.01)

3: Code (#9999999.1431,#.01)

4: Variable pointer. e.g., IEN;ICPT(

5: Short Description

^TMP("PXVIMMRPC",$J,x)

Note: Only active lots for the given division are returned.

Also, the Expiration date must be &gt;= PXDATE

1: "LOT"

2: #9999999.41 IEN

3: Lot Number (#9999999.41, #.01)

4: Manufacturer (#9999999.04, #.01)

5: Expiration Date (#9999999.41, #.09)

6: Doses Unused (#9999999.41, #.12)

7: Low Supply Alert (#9999999.41, #.15)

8: NDC Code (#9999999.41, #.18)

^TMP("PXVIMMRPC",$J,x)

Note: Only active contraindications are returned

1: "CONTRA"

2: #920.4 variable pointer: IEN;PXV(920.4,

3: Name (#920.4, #.01)

4: Status (1:Active, 0:Inactive)

5: Code|Coding System (#920.4, #.02 and .05)

6: NIP004 (#920.4, #.04)

7: Contraindication/Precaution (#920.4, #.06)

8: Allergy-Related (1:Yes, 0:No)

9: Default Warn Until Date ("Forever" means it should be forever)

^TMP("PXVIMMRPC",$J,x)

1: "DEF"

2: Default Route (#920.051, #1302)

3: Default Site (#920.051, #1303)

4: Default Dose (#920.051, #1312)

5: Default Dose Units (#920.051, #1313)

6: Default Dose Units (external format) (#920.051, #1313)

7: Default Non-Standard Dose Units (#920.051, #1314)

^TMP("PXVIMMRPC",$J,x)

1: "DEFC"

2: Default Comments (#920.051, #81101)

### PXVIMM IMM FORMAT

NAME: PXVIMM IMM FORMAT                 TAG: GETTEXT

ROUTINE: PXVRPC6                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

This RPC takes an input array of immunization properties set from the GUI.

It returns a formatted text of an immunization for use in documentation.

INPUT PARAMETER: INPUT                  PARAMETER TYPE: LIST

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

INPUT(n)=IMM ^ Imm IEN ^  ^ Date Administered (for immunizations) / Date

Contra-Refusal Event Documented (for contra/refusals) ^ Warn

Until Date (for contra/refusals) ^ Series ^ Refusal reason ^

Contraindication Reason ^ Ordered By ^ Administered By (for VA

administered) / Documented By (for historical) ^ Document Type

("Historical"/"Administered") ^ Information Source

(n)=LOC ^ File #44 IEN ^  ^  ^ Outside Location (for historicals)

(n)=ROUTE ^ Route ^ Site ^ Dosage

(n)=VIS ^ VIS Name ^ Edition Date ^ Language

(n)=LOT ^ Lot # ^ Manufacturer ^ Exp Date

(n)=COM ^ Comment

(n)=OVER ^ Override Reason

RETURN PARAMETER DESCRIPTION:

Formatted text of an immunization for use in documentation.

### PXVIMM IMM LOT

NAME: PXVIMM IMM LOT                    TAG: ILOT

ROUTINE: PXVRPC1                      RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION:

This RPC returns information from the IMMUNIZATION LOT file

(#9999999.41).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: NO

SEQUENCE NUMBER: 1

DESCRIPTION:

This input parameter is used to specify the IMMUNIZATION LOT file

records to be returned. Possible values:

R:XXX - return entry with ien XXX

N:XXX - return entry with lot number XXX

S:A   - return list of all active lot numbers

S:I   - return list of all inactive lot num

S:B   - return list of all lot numbers, active and inactive

If this parameter is null, it defaults to "S:B".

INPUT PARAMETER: PXVI                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

This optional input parameter is used to return an alternate array with record data in a caret delimited string. If this parameter is null or 0, the return defaults to the other array.

1 - return alternate array with internal values in delimited string

INPUT PARAMETER: PXLOC                  PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: NO

SEQUENCE NUMBER: 3

DESCRIPTION:

This optional input parameter is used to specify the institution (division) for which records should be returned at multidivisional facilities that may have immunization inventory specific to divisions.

Possible values are:

"I:X": Institution (#4) IEN #X

"V:X": Visit (#9000010) IEN #X

"L:X": Hopital Location (#44) IEN #X

If determination cannot be made based off input, then default to DUZ(2),

and if DUZ(2) is not defined, default to Default Institution.

RETURN PARAMETER DESCRIPTION:

Returns with PXVI not equal to 1:

PXVRETRN  - returned information is stored in ^TMP("PXVLST",$J))

- return info format: Data Element Name^Data Element Value

-       error format: -1^error message

For each record returned in the global array, the top value returned will indicate the record number in the array and the total number of records returned, e.g., "RECORD^1 OF 3".

This RPC returns the internal entry number (IEN) of the record and data in external  format from the following data fields in the IMMUNIZATION LOT file:

- LOT NUMBER (#.01)

- MANUFACTURER (#.02)

- STATUS (#.03)

- VACCINE (#.04)

- EXPIRATION DATE (#.09)

- ASSOCIATED VA FACILITY (#.1)

- DOSES UNUSED (#.12)

- LOW SUPPLY ALERT (#.15)

- NDC CODE (VA) (#.18)

Example Global Array Returned:

^TMP("PXVLST",$J,"P92A8769LN 1",0)="RECORD^1 OF 1"

.001)="IEN^6"

.01)="LOT NUMBER^P92A8769LN"

.02)="MANUFACTURER^SCLAVO, INC."

.03)="STATUS^ACTIVE"

.04)="VACCINE^ANTHRAX"

.09)="EXPIRATION DATE^DEC 31, 2016"

.1)="ASSOCIATED VA FACILITY^ALBANY"

.12)="DOSES UNUSED^94"

.15)="LOW SUPPLY ALERT^10"

.18)="NDC CODE (VA)^"

Example Global Array Returned if No Records Found:

^TMP("PXVLST",$J,0)="0 RECORDS"

Example error messages:

^TMP("PXVLST",$J,0)="-1^Invalid input value"

^TMP("PXVLST",$J,0)="-1^Invalid input for immunization lot IEN"

^TMP("PXVLST",$J,0)="-1^Invalid input for lot number"

Returns with PXVI equal to 1:

PXVRETRN  - returned information is stored in ^TMP("PXVLST",$J))

Each record is a caret-delimited list of values. Within the caret-delimited list, for fields with different internal and external values, both the internal and external values are included, delimited by a tilde (~) as indicated below:

Piece# Field# Field Name

------ ------ ----------

1             IEN

2      .01    LOT NUMBER

3      .02    MANUFACTURER  (Internal~External)

4      .03    STATUS (Internal~External)

5      .04    VACCINE (Internal~External)

6      .09    EXPIRATION DATE (Internal~External)

7      .12    DOSES UNUSED

8      .15    LOW SUPPLY ALERT

9      .18    NDC CODE (VA) (Internal~External)

10      .1     ASSOCIATED VA FACILITY (Internal~External)

Example Alternate Global Array:

^TMP("PXVLST",$J,0)=1 RECORD

6)="6^P92A8769LN^49~SCLAVO, INC.^0~ACTIVE^41~ANTHRAX^

3161231~DEC 31, 2016^93^10^~^500~ALBANY"

### PXVIMM IMM MAN

NAME: PXVIMM IMM MAN                    TAG: IMAN

ROUTINE: PXVRPC1                      RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION:

This RPC returns information from the IMM MANUFACTURER file

(#9999999.04).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 80               REQUIRED: NO

SEQUENCE NUMBER: 1

DESCRIPTION:

This input parameter is used to specify the IMMUNIZATION LOT file

records to be returned. Possible values:

R:XXX - return entry with ien XXX

M:XXX - return entry with MVX code XXX

N:XXX - return entry with imm manufacturer name XXX

S:A   - return list of all active manufacturers

S:I   - return list of all inactive manufacturers

S:B   - return list of all manufacturers, active and inactive

If this parameter is null, it defaults to "S:B".

INPUT PARAMETER: PXVDATE                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 7                REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

This optional input parameter is used in determining status. Input

should be in VA FileMan date format. The default value is the current

date.

INPUT PARAMETER: PXVI                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 3

DESCRIPTION:

This optional input parameter is used to return an alternate array with

record data in a caret delimited string. If this parameter is null or 0,

the return defaults to the other array.

1 - return alternate array with internal values in delimited string

RETURN PARAMETER DESCRIPTION:

Returns with PXVI not equal to 1:

PXVRETRN  - returned information is stored in ^TMP("PXVLST",$J))

- return info format: Data Element Name^Data Element Value

-       error format: -1^error message

For each record returned in the global array, the top value returned will

indicate the record number in the array and the total number of records

returned, e.g., "RECORD^1 OF 3".

This RPC returns the internal entry number (IEN) of the record and data

in external format from the following data fields in the IMM

MANUFACTURER file:

- NAME (#.01)

- MVX (#.02)

- INACTIVE FLAG (#.03)

- CDC NOTES (#201)

- STATUS (computed by Data Standardization utility)

Example Global Array Returned:

^TMP("PXVLST",$J,"WYETH-AYERST 1",0)="RECORD^1 OF 1"

.001)="IEN^55"

.01)="NAME^WYETH-AYERST"

.02)="MVX CODE^WA"

.03)="INACTIVE FLAG^INACTIVE"

201)="CDC NOTES^became WAL, now owned by

Pfizer"

"STATUS")="STATUS^INACTIVE"

Example Global Array Returned if No Records Found:

^TMP("PXVLST",$J,0)="0 RECORDS"

Example error messages:

^TMP("PXVLST",$J,0)="-1^Invalid input value"

^TMP("PXVLST",$J,0)="-1^Invalid input for manufacturer IEN"

^TMP("PXVLST",$J,0)="-1^Invalid input for MVX code"

^TMP("PXVLST",$J,0)="-1^Invalid input for manufacturer name"

Returns with PXVI equal to 1:

PXVRETRN  - returned information is stored in ^TMP("PXVLST",$J))

Each record is a caret-delimited list of values. Within the

caret-delimited list, for fields with different internal and external

values, both the internal and external values are included, delimited

by a tilde (~) as indicated below:

Piece# Field# Field Name

------ ------ ----------

1             IEN

2      .01    NAME

3      .02    MVX CODE

4      .03    INACTIVE FLAG (Internal~External)

5      201    CDC NOTES

6             STATUS (computed by Data Standardization utility)

### PXVIMM IMM SHORT LIST

NAME: PXVIMM IMM SHORT LIST             TAG: IMMSHORT

ROUTINE: PXVRPC4                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns a short list of immunizations.

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Filter (Optional; Defaults to "B")

Possible values are: ;

"A": Only return active entries

"H": Only return entries marked as Selectable for Historic

"B": Return both active entries and those marked as Selectable for

Historic

INPUT PARAMETER: PXDATE                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:

Date (optional; defaults to TODAY)

Used for determining immunization status (both for filtering and for

return value)

INPUT PARAMETER: PXOREXC                PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 3

DESCRIPTION:

Should entries defined in ORWPCE EXCLUDE IMMUNIZATIONS be excluded?

INPUT PARAMETER: PXLOC                  PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 4

DESCRIPTION:

Used when excluding entried listed in ORWPCE EXCLUDE IMMUNIZATIONS. (Optional)

This is the location used when getting the paramater value at the Location level.

Also used to get division when checking if there is a linked lot.

RETURN PARAMETER DESCRIPTION:

PXRTRN(x)

Note: Status (in the 5th piece) is determined as follows:

- If PXDATE is today, the status is based off the Inactive Flag

(#.07)

- If PXDATE is different than today, we will look when an update was

last made to the Immunization file (based off the Audits). If there

have not been any changes since PXDATE, we will get the status

based off the Inactive Flag, otherwise, we will get the status for

that date by calling GETSTAT^XTID.

1: "IMM"

2: #9999999.14 IEN

3: Name (#.01)

4: CVX Code (#.03)

5: Status (1: Active; 0: Inactive)

6: Selectable for Historic (#8803)

7: Mnemonic (#8801)

8: Acronym (#8802)

9: Active Lot linked to this Immunization? (1:Yes; 0:No)

PXRTRN(x)

1: "CDC"

2: CDC Product Name (#9999999.145, #.01)

PXRTRN(x)

1: "GROUP"

2: Vaccine Group Name  (#9999999.147, #.01)

### PXVIMM IMMDATA

NAME: PXVIMM IMMDATA                    TAG: IMMDATA

ROUTINE: PXVRPC3                      RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION:

Returns entries from the IMMUNIZATION file (9999999.14).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

This parameter is used to specify the IMMUNIZATION file records to be

returned. Possible values:

R:XXX - return entry with ien XXX

S:A   - return list of active immunizations

S:H   - return list of [selectable for] historic immunizations

S:*   - return all records regardless of their status

If this parameter is null, it defaults to "S:A".

INPUT PARAMETER: SUBFILES               PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

A value of 1 or Y indicates that all subfile multiples should be included.

RETURN PARAMETER DESCRIPTION:

The first record of the returned array contains the count of records

being returned.

Each record is a caret-delimited list of values.

Piece# Field# Field Name

------ ------ ----------

1             IEN

2      .01    NAME

3      .02    SHORT NAME

4      .03    CVX CODE

5      .05    MAX # IN SERIES

6      .07    INACTIVE FLAG

7      8801   MNEMONIC

8      8802   ACRONYM

9      8803   SELECTABLE FOR HISTORIC

(These subfiles are included when the SUBFILES parameter is set to 1)

(Each multiple is separated by the pipe (|) character)

10     2      CDC FULL VACCINE NAME

11     3      CODING SYSTEM

(For each CODING SYSTEM, there are multiple CODE values.)

(CODING SYSTEM1~CODE1;;CODE2|CODING SYSTEM2~CODE3;;CODE4)

12     4      VACCINE INFORMATION STATEMENT

(VIS1-IEN~VIS1-NAME|VIS2-IEN~VIS2-NAME)

13     5      CDC PRODUCT NAME

14     7      VACCINE GROUP NAME

15     10     SYNONYM

16     99.991 EFFECTIVE DATE/TIME

(There are date/time and status fields in each multiple.)

(EFFECTIVE DATE/TIME1~STATUS1|EFFECTIVE DATE/TIME2~STATUS2)

### PXVIMM INFO SOURCE

NAME: PXVIMM INFO SOURCE                TAG: IMMSRC

ROUTINE: PXVRPC2                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns entries from the IMMUNIZATION INFO SOURCE file (920.1).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Filter. Possible values are:

R:XXX - Return entry with IEN XXX.

H:XXX - Return entry with HL7 Code XXX.

N:XXX - Return entry with #.01 field equal to XXX

S:X   - Return all entries with a status of X.

Possible values of X:

A - Active Entries

I - Inactive Entries

B - Both active and inactive entries

Defaults to "S:B".

RETURN PARAMETER DESCRIPTION:

Returns:

PXVRSLT(0)=Count of elements returned (0 if nothing found)

PXVRSLT(n)=IEN^Name^HL7 Code^Status (1:Active, 0:Inactive)

When filtering based off IEN, HL7 Code, or #.01 field, only one entry will

be returned in PXVRSLT(1).

When filtering based off status, multiple entries can be returned. The

first entry will be returned in subscript 1, and subscripts will be

incremented by 1 for further entries. Entries will be sorted

alphabetically.

If no entries are found based off the filtering criteria, PXVRSLT(0) will

equal 0, and there will be no data returned in the subsequent subscripts.

### PXVIMM VICR EVENTS

NAME: PXVIMM VICR EVENTS                TAG: GETVICR

ROUTINE: PXVRPC5                      RETURN VALUE TYPE: ARRAY

DESCRIPTION:

Returns "active" entries from the V IMM CONTRA/REFUSAL EVENTS file

(#9000010.707) that are related to the given patient and immunization.

"Active" is defined as entries where the Event Date and Time is &gt;= PXDATE

and the Warn Until Date is null or greater than PXDATE.

INPUT PARAMETER: DFN                    PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

Pointer to file #2.

INPUT PARAMETER: PXVIMM                 PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 2

DESCRIPTION:

Pointer to #9999999.14.

INPUT PARAMETER: PXDATE                 PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 3

DESCRIPTION:

Used to determine if entry is "active" (Optional; Defaults to TODAY)

INPUT PARAMETER: PXFORMAT               PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 4

DESCRIPTION:

Format that return array should be returned (Optional; Defaults to "L")

Possible values are:

"L": Return a caret-delimited list of entries.

"W": Returns a warning message.

RETURN PARAMETER DESCRIPTION:

PXRSLT(0)=Count of elements returned (0 if nothing found)

If PXFORMAT="L":

PXRSLT(n)="VICR" ^ V IMM Contra/Refusal Events IEN ^ Visit IEN ^

Contra/Refusal variable pointer | Contra/Refusal Name ^

Immunization IEN | Name ^ Warn Until Date ^ D/T Recorded ^

Event D/T ^ Encounter Provider IEN | Name

PXRSLT(n)="COM" ^ Comments

If PXFORMAT["W":

PXRSLT(n)=Warning text

### PXVIMM VIS

NAME: PXVIMM VIS                        TAG: IVIS

ROUTINE: PXVRPC1                      RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION:

This RPC returns information from the VACCINE INFORMATION STATEMENT file

(#920).

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 55               REQUIRED: NO

SEQUENCE NUMBER: 1

DESCRIPTION:

This input parameter is used to specify the VACCINE INFORMATION

STATEMENT file records to be returned.

R:XXX - return entry with ien XXX

N:XXX - return entry with VIS name XXX

S:A   - return list of all active VISs

S:I   - return list of all inactive VISs

S:B   - return list of all VISs, active and inactive

If this parameter is null, it defaults to "S:B".

INPUT PARAMETER: PXVDATE                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 7                REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

This optional input parameter is used in determining status. Input

should be in VA FileMan date format. The default value is the current

date.

RETURN PARAMETER DESCRIPTION:

Returns:

PXVRETRN  - returned information is stored in ^TMP("PXVLST",$J))

- return info format: Data Element Name^Data Element Value

-       error format: -1^error message

For each record returned in the global array, the top value returned will

indicate the record number in the array and the total number of records

returned, e.g., "RECORD^1 OF 3".

This RPC returns the internal entry number (IEN) of the record and data

in external format from the following data fields in the VACCINE

INFORMATION STATEMENT file:

- NAME (#.01)

- EDITION DATE (#.02)

- EDITION STATUS (#.03)

- LANGUAGE (#.04)

- VIS TEXT (#2) (word-processing)

- 2D BAR CODE (#100)

- VIS URL (#101)

- STATUS (computed by Data Standardization utility)

Example Global Array Returned:

(Stored in ^TMP("PXVLST",$J,"SHINGLES VIS 1",)

0)="RECORD^1 OF 1"

.001)="IEN^27"

.01)="NAME^SHINGLES VIS"

.02)="EDITION DATE^OCT 06, 2009"

.03)="EDITION STATUS^CURRENT"

.04)="LANGUAGE^ENGLISH"

2,1)="VIS TEXT 1^Shingles  Vaccine: What you need to know "

2)="VIS TEXT 2^ "

3)="VIS TEXT 3^1. What is shingles?"

4)="VIS TEXT 4^ "

5)="VIS TEXT 5^Shingles is a painful skin rash, often with blisters. It

is also called "

.

.

.

117)="VIS TEXT 117^ "

118)="VIS TEXT 118^Department of Health and Human Services"

119)="VIS TEXT 119^Centers for Disease Control and Prevention"

100)="2D BAR CODE^253088698300020211091006"

101)="VIS URL^http://www.immunize.org/vis/shingles.pdf"

"STATUS")="STATUS^ACTIVE"

Example Global Array Returned if No Records Found:

^TMP("PXVLST",$J,0)="0 RECORDS"

Example error messages:

^TMP("PXVLST",$J,0)="-1^Invalid input value"

^TMP("PXVLST",$J,0)="-1^Invalid input for VIS IEN"

^TMP("PXVLST",$J,0)="-1^Invalid input for VIS name"

### PXVIMM IMM DISCLOSURE

NAME: PXVIMM IMM DISCLOSURE             TAG: SETDIS

ROUTINE: PXVRPC9                      RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION:

Save immunization disclosure information.

INPUT PARAMETER: VIMM                   PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

V Immunization IEN.

INPUT PARAMETER: AGENCY                 PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 2

DESCRIPTION:

Agency Name this record was disclosed to.

INPUT PARAMETER: DATE                   PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 3

DESCRIPTION:

Date/Time this record was disclosed.

INPUT PARAMETER: TIMEZONE               PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 4

DESCRIPTION:

Time zone of the Date/Time (either as the 3-character time zone

designation or the UTC time offset, in the format -/+HHMM).

RETURN PARAMETER DESCRIPTION:

0^error message - If we could not save the disclosure information (either

the RPC was called incorrectly, or the V Immunization

IEN did not exist).

1               - Successfully saved the disclosure information.

2^error message - We attempted to save the disclosure information, but

encountered an error when filing the data to the

database.

### PXVIMM VIMM DATA

NAME: PXVIMM VIMM DATA                  TAG: RPC

ROUTINE: PXVRPC7                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            WORD WRAP ON: FALSE

DESCRIPTION:

Returns immunization records from the V Immunization and V Immunization

Deleted file. There are two methods for defining the criteria to determine

which records to return.

1. A specific list of record IDs can be passed in, and only those

records will be returned (if they exist on the system). When called

in this way, the list of records should be passed in LIST, and FILTER

should not be defined (if both LIST and FILTER are defined, only the

records listed in LIST will be returned, and the search criteria in

FILTER will be ignored).

If an invalid IEN was passed in, the following error will be

returned: "Record with IEN #xxx does not exist."

If the record could not be returned for some other reason, the

following error will be returned: "Unable to return record with IEN

#xxx."

2. A time range (and other filter criteria) can be passed in FILTER, and

a list of records that meet that criteria will be returned. Any

record last modified or deleted (if FILTER("INC DELETE")=1) within

that time range will be returned.

To limit the number of records returned, FILTER("MAX") can be set to

the maximum number of records to be returned. The RPC will return a

value called "BOOKMARK". That value can be used to call the RPC

again, this time passing in the "BOOKMARK" value in

FILTER("BOOKMARK") (all other parameters should be defined exactly as

when previously called), and the RPC will return the next n number of

records that meet the search criteria, and starting where the

previous call left off. So for example, if there are 1,000 records

that meet the search criteria, and FILTER("MAX") is set to return a

maximum of 100 records, the RPC will need to be called 10 times in

order to return all 1,000 records. Each subsequent time the RPC is

called, the caller would set FILTER("BOOKMARK") to the bookmark value

returned in the previous call. The caller would know when they reach

the end and that there are no more records to be returned, when the

RPC returns TOTAL ITEMS=0.

Note: All date/time references are to be in FileMan format.

INPUT PARAMETER: FILTER                 PARAMETER TYPE: LIST

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Search criteria (Optional).

("START") - Start date/time to begin search from (Defaults to T-1)

("STOP") - Stop date/time to end search (if time is not

specified, midnight is assumed). (Defaults to T-1)

("DATA SRC EXC") - A semi-colon delimited list of Data Source names (in

external format) (e.g., SRC1;SRC2;SRCn). (Optional)

Any immunization record whose DATA SOURCE matches one

of the data names in this list will be filtered out,

and will not be returned.

("MAX") - The maximum number of records to return (defaults to

99)

("BOOKMARK") - If wanting to get the next n number of records, the

bookmark value returned in the previous call should be

passed here. (Optional)

("INC DELETE") - Flag to control if records should also be returned

from the V IMMUNIZATION DELETED file. (defaults to

"1").

1 - Include records from both the V IMMUNIZATION and V

IMMUNIZATION DELETED files

0 - Only include records from the V IMMUNIZATION file.

INPUT PARAMETER: LIST                   PARAMETER TYPE: LIST

REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:

A list of record numbers (IENs) to return. (Optional)

To specify an IEN from the V IMMUNIZATION file, set LIST(IEN)="".

To specify an IEN from the V IMMUNIZATION DELETED file, set

LIST(IEN\_"D")=""  (e.g., PXLIST("123D")="").

INPUT PARAMETER: DATE                   PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 3

DESCRIPTION:

A date in FileMan format. (Optional)

It is used when the caller wants to see how the records being returned

changed since that date. When populated, it is used in a number of ways:

1. Additions: If a record was added after that date, and later edited,

we will return the record as if it's a new record (i.e., TYPE="ADD")

(even though it's truly an edited record), as from that date's

perspective this is a new record.

2. Edits: a) We will return two versions of an edited record. One, will

be the way the record existed on that date (i.e.,

TYPE="UPDATE-BEFORE"). Two, will be the current state of the record

(i.e., TYPE="UPDATE-AFTER"). b) if no significant changes have been

made to this record since that date (i.e., the record was edited

after that date, but none of the fields that are returned in this

call were modified with that edit), then we will not return this

record, as nothing significant changed since that date.

3. Deletes: a) If a record was added after that date and later deleted,

we won't return the record, as on that date the record did not exist,

and the current record is deleted, so nothing really changed since

that date. b) If a record was edited after that date and then

deleted, the deleted record will be returned the way it existed on

that date, as from that date's perspective that is what the deleted

record looked like.

INPUT PARAMETER: DEMOGRAPHICS           PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 4

DESCRIPTION:

Return patient demographics? (1=Yes/0=No). (Defaults to "1").

RETURN PARAMETER DESCRIPTION:

A list of records that meet the search criteria.

Each item returned will contain an immunization object, and if

demographics are requested, a Patient object.

The immunization object can be called: IMm-ADD, IMM-DELETE, IMM-UPDATE,

IMM-UPDATE-BEFORE, or IMM-UPDATE-AFTER.

o IMM-ADD - Used when the immunization record is a "new" record.

o IMM-DELETE - Used when the immunizatin record is a deleted record.

o IMM-UPDATE - Used wehn the immunizatin record was edited (and the

caller did not pass in DATE).

o IMM-UPDATE-BEFORE/IMM-UPDATE-AFTER - Used when the immunizatin record

was edited and the called passed in DATE. Two objects will be

returned. The IMM-UPDATE-BEFORE object will be the way the record

existed before that date, and the IMM-UPDATE-AFTER will be the current

state of the record.

For more details on the fields and attributes of the immunization and

patient objects, please see the documentation.

The following is a table that lists the data elements returned by the RPC.

| ELEMENTS               | ATTRIBUTES                       | CONTENT                                                                                                                                         |
|------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| TOTAL ITEMS            |                                  | Number of immunization records being returned.                                                                                                  |
| FACILITY ID            |                                  | Institution #4 Station Number  (The system’s default Institution.)                                                                              |
| BOOKMARK               |                                  | String.  (To return next n number of records after bookmark.)                                                                                   |
| PATIENT                |                                  |                                                                                                                                                 |
| FACILITY[n]            | NAME                             | Institution #4 Name  (All known VA facilities where a patient visited in the last 12 months; pulled from the Treating Facility File (#391.91)). |
|                        | STATION NUMBER                   | Institution #4 Station Number                                                                                                                   |
| NAME (Last, First M)   |                                  | Patient #2 Name                                                                                                                                 |
| ADDRESS                | STREET 1                         | Patient #2 Street Address 1                                                                                                                     |
|                        | STREET 2                         | Patient #2 Street Address 2                                                                                                                     |
|                        | STREET 3                         | Patient #2 Street Address 3                                                                                                                     |
|                        | CITY                             | Patient #2 City                                                                                                                                 |
|                        | STATE                            | Patient #2 State                                                                                                                                |
|                        | ZIP                              | Patient #2 Zip                                                                                                                                  |
| PHONE                  |                                  | Patient #2 Phone Residence                                                                                                                      |
| ICN                    |                                  | Patient #2 Integration Control Number (with checksum)                                                                                           |
| DFN                    |                                  | Patient #2 IEN                                                                                                                                  |
| DOB                    |                                  | Patient #2 Date of Birth                                                                                                                        |
| SEX                    |                                  | Patient #2 Sex                                                                                                                                  |
| RACE[n]                | NAME                             | Patient #2 Race Information                                                                                                                     |
|                        | HL7 CODE                         | Race #10 HL7 Value                                                                                                                              |
| ETHNICITY[n]           | NAME                             | Patient #2 Ethnicity Information                                                                                                                |
|                        | HL7 CODE                         | Ethnicity #10.2 HL7 Value                                                                                                                       |
| PLACE OF BIRTH         | CITY                             | Patient #2 Place of Birth[City]                                                                                                                 |
|                        | STATE                            | Patient #2 Place of Birth[State]                                                                                                                |
| MOTHER MAIDEN NAME     |                                  | Patient #2 Mother's Maiden Name                                                                                                                 |
| DATE OF DEATH          |                                  | Patient #2 Date of Death                                                                                                                        |
| SUPPORT[n]             | TYPE                             | NOK = Next of Kin  ECON = Emergency Contact                                                                                                     |
|                        | NAME                             | string                                                                                                                                          |
|                        | RELATIONSHIP                     | string                                                                                                                                          |
|                        | PHONE                            | string                                                                                                                                          |
|                        | STREET 1                         | string                                                                                                                                          |
|                        | STREET 2                         | string                                                                                                                                          |
|                        | STREET 3                         | string                                                                                                                                          |
|                        | CITY                             | string                                                                                                                                          |
|                        | STATE                            | State #5 Name                                                                                                                                   |
|                        | ZIP                              | string                                                                                                                                          |
| IMMUNIZATION           |                                  |                                                                                                                                                 |
| ID                     |                                  | V Immunization #9000010.11 IEN                                                                                                                  |
| IMMUNIZATION           | IEN                              | Immunization #9999999.14 IEN                                                                                                                    |
|                        | NAME                             | Immunization #9999999.14 Name                                                                                                                   |
| CVX                    |                                  | Immunization File #9999999.14 CVX Code                                                                                                          |
| FACILITY               | NAME                             | Institution #4 Name  (Administering facility)                                                                                                   |
|                        | STATION NUMBER                   | Institution #4 Station Number                                                                                                                   |
| INFO SOURCE            | IEN                              | Immunization Info Source #920 IEN                                                                                                               |
|                        | NAME                             | Immunization Info Source #920 Name                                                                                                              |
|                        | HL7 CODE                         | Immunization Info Source #920 HL7 Code                                                                                                          |
| COMPLETION STATUS      |                                  | "COMPLETE"  (Currently stuffing all records with "COMPLETE".)                                                                                   |
| MANUFACTURER           | IEN                              | Imm Manufacturer #9999999.04 IEN                                                                                                                |
|                        | NAME                             | Imm Manufacturer #9999999.04 Name                                                                                                               |
|                        | MVX CODE                         | Imm Manufacturer #9999999.04 MVX Code                                                                                                           |
| ADMINISTERED DATE TIME |                                  | V Immunization #9000010.11 Event Date and Time  If Event Date and Time is null then default to Visit Date/Time.                                 |
| LOT NUMBER             | IEN                              | Immunization Lot #9999999.41 IEN                                                                                                                |
|                        | NAME                             | Immunization Lot #9999999.41 Lot Number                                                                                                         |
| SERIES                 |                                  | PARTIALLY COMPLETE, COMPLETE, BOOSTER, SERIES 1-8                                                                                               |
| DOSE                   |                                  | V Immunization #9000010.11 Dose                                                                                                                 |
| DOSE UNITS             |                                  | V Immunization #9000010.11 Dose Units                                                                                                           |
| EXPIRATION DATE        |                                  | Immunization Lot #9999999.41 Expiration Date                                                                                                    |
| ADMIN ROUTE            | IEN                              | Imm Administration Route #920.2 IEN                                                                                                             |
|                        | NAME                             | Imm Administration Route #920.2 Route                                                                                                           |
|                        | HL7 CODE                         | Imm Administration Route #920.2 HL7 Code                                                                                                        |
| ADMIN SITE             | IEN                              | Imm Administration Site (Body) # 920.3 IEN                                                                                                      |
|                        | NAME                             | Imm Administration Site (Body) # 920.3 Site                                                                                                     |
|                        | HL7 CODE                         | Imm Administration Site (Body) # 920.3 HL7 Code                                                                                                 |
| ENCOUNTER PROVIDER     | IEN                              | New Person #200 IEN                                                                                                                             |
|                        | NAME                             | New Person #200 Name                                                                                                                            |
|                        | NPI                              | New Person #200 NPI                                                                                                                             |
|                        | VPID                             | New Person #200 VPID                                                                                                                            |
| DOCUMENTER             | IEN                              | New Person #200 IEN                                                                                                                             |
|                        | NAME                             | New Person #200 Name                                                                                                                            |
|                        | NPI                              | New Person #200 NPI                                                                                                                             |
|                        | VPID                             | New Person #200 VPID                                                                                                                            |
| DATE RECORDED          |                                  | V Immunization #9000010.11, Date and Time Recorded                                                                                              |
| DATA SOURCE            | IEN                              | PCE Data Source #839.7 IEN                                                                                                                      |
|                        | NAME                             | PCE Data Source #839.7 Source Name                                                                                                              |
| VACCINE GROUPS[n]      |                                  | Immunization #9999999.14 Vaccine Group Name                                                                                                     |
| WARNING ACK            |                                  | V Immunization #9000010.11 Warning Acknowledged                                                                                                 |
| OVERRIDE REASON        |                                  | V Immunization #9000010.11 Warning Override Reason                                                                                              |
| CODING SYSTEM[n]       | Name of coding system (e.g. CPT) | Immunization #9999999.14 Coding System                                                                                                          |
| COMMENTS               |                                  | V Immunization #9000010.11 Comments                                                                                                             |
| CONTRAINDICATED        |                                  | V Immunization #9000010.11 Contraindicated                                                                                                      |
| LOCATION               | IEN                              | Hospital Location #44 IEN                                                                                                                       |
|                        | NAME                             | Hospital Location #44 Name                                                                                                                      |
| REACTION               |                                  | V Immunization #9000010.11 Reaction                                                                                                             |
| ORDERING PROVIDER      | IEN                              | New Person #200 IEN                                                                                                                             |
|                        | NAME                             | New Person #200 Name                                                                                                                            |
|                        | NPI                              | New Person #200 NPI                                                                                                                             |
|                        | VPID                             | New Person #200 VPID                                                                                                                            |
| VIS OFFERED[n]         | DATE OFFERED                     | V Immunization File #9000010.11, Sub-file 9000010.112 Date VIS Offered/Given                                                                    |
|                        | IEN                              | Vaccine Information Statement #920 IEN                                                                                                          |
|                        | NAME                             | Vaccine Information Statement #920 Name                                                                                                         |
|                        | EDITION DATE                     | Vaccine Information Statement #920 Edition Date                                                                                                 |
|                        | LANGUAGE                         | Language #.85 Name                                                                                                                              |
| VISIT                  |                                  | Visit #9000010 IEN                                                                                                                              |
| VISIT DATE TIME        |                                  | Visit #9000010 IEN Visit/Admit Date &Time                                                                                                       |
| PATIENT                | DFN                              | Patient #2 IEN                                                                                                                                  |
|                        | NAME                             | Patient #2 Name                                                                                                                                 |

### PXVSK DEF SITES

NAME: PXVSK DEF SITES                   TAG: SKSITES

ROUTINE: PXVRPC8                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION:

Returns a list of default administration sites for skin tests.

RETURN PARAMETER DESCRIPTION:

(0)=Count of elements returned (0 if nothing found)

(n)=IEN^NAME

### PXVSK SKIN SHORT LIST

NAME: PXVSK SKIN SHORT LIST             TAG: SKSHORT

ROUTINE: PXVRPC8                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION:

Returns active list of skin tests.

INPUT PARAMETER: DATE                   PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 1

DESCRIPTION:

Used for determining skin test status. (Defaults to TODAY).

RETURN PARAMETER DESCRIPTION:

(0)=Count of elements returned (0 if nothing found)

(n)=SK^IEN^NAME^PRINT NAME

(n)=CS^Coding System^Code^Variable pointer^Short Description

### PXVSK V SKIN TEST LIST

NAME: PXVSK V SKIN TEST LIST            TAG: SKLIST

ROUTINE: PXVRPC8                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION:

Returns a list of V Skin Test entries that have been placed within the

last x days. The number of days to look back is defined in the PXV SK DAYS

BACK parameter.

INPUT PARAMETER: DFN                    PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

Only V Skin Test entries for this patient will be returned.

INPUT PARAMETER: SKINTEST               PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 2

DESCRIPTION:

Skin Test IEN. Only V Skin Test entries for this Skin Test will be

returned.

INPUT PARAMETER: DATE                   PARAMETER TYPE: LITERAL

REQUIRED: NO                          SEQUENCE NUMBER: 3

DESCRIPTION:

The system will search back x number of days from this date. Defaults to

TODAY.

RETURN PARAMETER DESCRIPTION:

(0)=Count of elements returned (0 if nothing found)

(n)=DATERANGE^Start Date^Stop Date

(n)=PLACEMENT^IEN^Skin Test Name^Date/Time of Placement

## 11 Generating Online Documentation

### Routines

The namespace for the PCE package is PX. Some AU* routines are distributed by PCE. Use the Kernel option, List Routines [XUPRROU], to print a list of any or all of the PCE routines. This option is found on the Routine Tools [XUPR-ROUTINE-TOOLS] menu on the Programmer Options [XUPROG] menu, which is a sub-menu of the Systems Manager Menu [EVE] option.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: list Routines

Routine Print

Want to start each routine on a new page: No// [ENTER]

routine(s) ?   &gt; PX*

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option, First Line Routine Print [XU FIRST LINE PRINT] to print a list of just the first line of each Health Summary subset routine.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: routine Tools

Select Routine Tools Option: First Line Routine Print

PRINTS FIRST LINES

routine(s) ?   &gt;PX*

### Globals

Globals exported by PCE include ^PX, ^PXD, and ^AU*. Use the Kernel option, List Global [XUPRGL], to print a list of any of these globals. This option is found on the Programmer Options menu [XUPROG], which is a sub-menu of the Systems Manager Menu [EVE] option.

Select Systems Manager Menu Option: programmer Options

Select Programmer Options Option: LIST Global

Global ^^PX*

### Files

The number-spaces assigned to PCE include 800-839.99, and 9000001, 900010.xx, and 9999999.xx. Use the VA FileMan option, List File Attributes [DILIST] to print a list of these files.

### XINDEX

XINDEX is a routine that produces a report called the VA Cross-Reference. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls. XINDEX is invoked from programmer mode:  D ^XINDEX. When prompted to select routines, enter PX*.

### Data Dictionaries

The Data Dictionaries (DDs) are considered part of the online documentation. Use VA FileMan option #8 (DATA DICTIONARY UTILITIES) to print DDs.

&gt;D P^DI

VA FileMan 21.0

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: V MEASUREMENT// 9000010  VISIT

(1 entry)

GO TO WHAT FILE: VISIT// &lt;RET&gt;

Select LISTING FORMAT: STANDARD// &lt;RET&gt;

DEVICE: PRINTER

## 12 Troubleshooting and Helpful Hints

- The Automated Information Collection System (AICS) package includes a Print Manager that allows sites to define reports that should print along with the encounter forms. This can save considerable time preparing and collecting reports for appointments. See the Automated Information Collection System User Manual for instructions.
- You can add Health Summary, Problem List, and Progress Notes as actions to PCE, to allow quick access to these programs. When you press the [RETURN] key at the quit prompts (or up-arrow out), you are automatically returned to PCE.
- Since problems can occur if you delete patients (the internal entry number of the file can be reassigned, causing discrepancies in the data), we recommend that you NOT delete any patients.
- If you see zeroes instead of numbers on encounter dates (e.g., 00/00/95 or 01/00/96) – on reports or encounter displays – they are for Historical Encounters where the exact date is not known.

### Shortcuts

- After entering a diagnosis, a prompt for Provider Narrative appears. If you don't want to enter additional descriptive information, press the [ENTER] key, and the ICD9 or ICD10 short description for the diagnosis will be stored in the Provider Narrative field. (This only works if you're entering directly into the PCE user interface.)

More Shortcuts

- After Diagnosis has been entered, if the Provider Narrative is an exact match, you can enter = and the diagnosis will be duplicated here.
- The equals sign (=) can also be used as a shortcut when selecting an action plus encounters or appointments from a list in a single response (e.g., Select Action: ED=2).
- To quickly add or edit encounter information, select an appointment number at the first appointment screen.

### Device Interface Error Report

The PCE Device Interface Error Report lets you look up PCE device interface errors by Error Number, Error Date and Time, Encounter Date and Time, or by Patient Name.

Select PCE Coordinator Menu Option: die  PCE Device Interface Error Report

Select one of the following:

ERN       Error Number

PDT       Processing Date and Time

EDT       Encounter Date and Time

PAT       Patient Name

Look up PCE device interface errors based on: ERN//   Error Number

Enter the beginning error number:  (1-4): 1// [ENTER]

Enter the ending error number:  (1-4): 4//  [ENTER]

DEVICE: HOME//   [ENTER] VAX    RIGHT MARGIN: 80//  [ENTER]

Aug 08, 1996 4:05:09 pm  Page 1

PCE Device Interface Error Report

Report based on Error Numbers 1 through 26.

------------------------------------------------------

Error Number: 1

Patient:  PCEPATIENT,ONE 000-45-6789

Hospital Location:  DIABETES CLINIC

Encounter date:  May 06, 1996@14:53:17

Processing date: May 06, 1996@16:18:53

File: 9000010.07 (V POV)  IEN: 0  Field .04 (PROVIDER NARRATIVE)

Error message: Missing Required Fields

Node: Missing

Original: Missing

Updated: Missing

File: 9000010.07 (V POV)  IEN: 0  Field .04 (PROVIDER NARRATIVE)

Error message: Missing Required Fields

Node: Missing

Original: Missing

Updated: Missing     ETC.

## 13 Glossary

**AICS:** Automated Information Collection System, formerly Integrated Billing, the program that manages the definition, scanning, and tracking of Encounter Forms.

**Action:** A functional process that a clinician or clerk uses in the PCE computer program. For example, “Update Encounter” is an action that allows the user to pick an encounter and edit information that was previously entered (either through PCE or the PIMS Checkout process) or add new information (such as an immunization or patient education).

**Ambulatory Care Data Capture project:** A project assigned to coordinate the efforts of various VISTA (DHCP) software packages to meet the 10/1/96 outpatient minimum data set mandate from the Under Secretary for Health.

**Ancillary Service:** (Occasion of Service) A specified instance of an act of service involved in the care of the patient or consumer which is not an encounter.

**Appointment:** A scheduled meeting with a provider at a clinic; an appointment can include several encounters involving other providers, tests, procedures, etc.

**Checkout Process:** Part of Medical Administration (PIMS) appointment processing. The checkout process documents administrative and clinical data related to the appointment.

**Clinician:** A doctor or other provider in the medical center who is authorized to provide patient care.

**COMPACT Act Acute Suicidal Crisis Episode of Care** : A COMPACT Act Acute Suicidal Crisis episode of care (EOC) encompasses all encounters related to a patient’s care during an acute suicidal crisis. A patient is deemed to be in an acute suicidal crisis until the patient is stabilized and the crisis is over. The duration of a COMPACT Act Acute Suicidal Crisis episode of care includes the initial care and follow-up care that ensures, to the extent practicable, immediate safety and reduces: the severity of distress, the need for urgent care, or the likelihood that the severity of distress or need for urgent care will increase during the transfer of that individual from a facility at which the individual has received care for that acute suicidal crisis. The end of a COMPACT Act Acute Suicidal Crisis episode of care is dependent on the clinical determination that the patient is no longer in crisis.  Encounters within the COMPACT Acute Suicidal Crisis episode of care should be marked appropriately so that all first-party co-pays for the acute suicidal crisis episode of care will be canceled by Integrated Billing.

**Encounter:** A contact between a patient and a provider who has responsibility for assessing and treating the patient at a given contact, exercising independent judgment. A patient can have multiple encounters per visit.

**Encounter Form:** A paper form used to display and collect data pertaining to an outpatient encounter, developed by the AICS package.

**Episode of Care:** Many encounters for the same problem can constitute an episode of care. An outpatient episode of care may be a single encounter or can encompass multiple encounters over a long period of time. The definition of an episode of care may be interpreted differently by different professional services even for the same problem. Therefore, the duration of an episode of care is dependent on the viewpoints of individuals delivering or reviewing the care provided.

**Health Summary:** A Health Summary is a clinically oriented, structured report that extracts many kinds of data from VISTA and displays it in a standard format. The individual patient is the focus of health summaries, but health summaries can also be printed or displayed for groups of patients. The data displayed covers a wide range of health-related information such as demographic data, allergies, current active medical problems, laboratory results, etc.

**Indian Health Service (IHS):** IHS developed a computer program similar to VA’s VISTA, which contains Patient Care Component (PCC) from which PCE and many of its components were derived.

**Inpatient Visit:** Inpatient encounters include the admission of a patient to a VAMC and any clinically significant change related to treatment of that patient. For example, a treating specialty change is clinically significant, whereas a bed switch is not. The clinically significant visits created throughout the inpatient stay would be related to the inpatient admission visit. If the patient is seen in an outpatient clinic while an Inpatient, this is treated as a separate encounter.

**Integrated Billing (IB):** A VISTA package responsible for identifying billable episodes of care, creating bills, and tracking the whole billing process through to the passing of charges to Accounts Receivable (AR). Includes the Encounter Form utility.

**MCCR:** Medical Care Cost Recovery, a VISTA entity which supports Integrated Billing and many data capture pilot projects related to PCE.

**Minimum Data Set:** Each ambulatory encounter and/or ancillary service with associated provider, procedure, and diagnosis information must be reported to the National Patient Care Data Base (NPCDB), as of 10/1/96.

**NPCDB:** National Patient Care Data Base, a database located in the Austin Accounting Center.

**Occasion of Service:** A specified instance of an act of service involved in the care of a patient or consumer which is not an encounter. These occasions of service may be the result of an encounter; for example, tests or procedures ordered as part of an encounter. A patient may have multiple occasions of service per encounter or per visit.

**Outpatient Encounter:** Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communications with a patient may be represented by a separate visit entry.

**Outpatient Visit:** The visit of an outpatient to one or more units or facilities located in or directed by the provider maintaining the outpatient health care services (clinic, physician’s office, hospital/medical center) within one calendar day.

**Person Class:** As part of the October 1, 1996 mandate, VAMCs must collect provider information. The provider information reported is the "Person Class" defined for all providers associated with ambulatory care delivery. All VAMC providers must be assigned a Profession/ Occupation code (Person Class) so that a Person Class can be associated with each ambulatory patient encounter.

**Provider:** The entity which furnishes health care to a consumer. It includes a professionally licensed practitioner who is authorized to operate a health care delivery facility ¾ an individual or defined group of individuals who provides a defined unit of health care services (defined = codable) to one or more individuals at a single session.

**Standard Code:** There are a number of systems to classify and code medical terminology, examples include CPT (Current Procedural Terminology), ICD (International Classifications of Diseases), and SNOMED CT (Systemized Nomenclature of Medicine- Clinical Terms)

**Stop Code:** A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit. Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit. After 10/1/96, stop codes will become DSS Identifiers.

**Visit:** The visit of a patient to one or more units of a facility within one calendar day.

**Visit Tracking:** A VISTA utility that creates and manages entries in the Visit file which links patient-related information for patient encounters.

**VISTA:** Veterans Information System Technology Architecture, the new name for DHCP.

## 14 Appendix A – Developer Guide – PCE Device Interface Module

PCE Device Interface module local array structures exported with PCE.

Conventions

An Error Suspension file records data that fails the verification process

or if there are errors in storing.

1. In listings of valid values [1 | 0 | null]

1 denotes TRUE or YES

0 denotes FALSE or NO

null denotes VALUE NOT SUPPLIED BY DATA CAPTURE APPLICATION

2. The PCE Device Interface uses a locally name-spaced array (called

LOCAL in this document) with the following gross structure to

receive data from an external device. Developers should use an

array in their namespace to represent the LOCAL array. It is

possible that data from multiple providers was captured for the

encounter. The ENCOUNTER node records information about the

"main" provider. It is mandatory that this person be identified

in the ENCOUNTER node. Data will NOT be moved to VISTA if such a

provider is not identified on the ENCOUNTER node. The remaining

nodes in the LOCAL( array [VITALS, DIAGNOSIS, PROCEDURE,

PROBLEM... ] are specific to the particular PROVIDER associated

with the data on that node. If the provider is unknown, (for

example, the identity of the nurse who took the vitals was not

captured on a scanned encounter form) the provider subscript

&lt;PROVIDER IEN&gt; may be set to zero except provider is required for

PROBLEM. This is a concession to reality, and should not be

encouraged. If a provider CAN be identified, they SHOULD be

identified.

Locally name-spaced array:

LOCAL("DIAGNOSIS/PROBLEM",&lt;PROVIDER IEN&gt;)

LOCAL("PROBLEM",&lt;PROVIDER IEN&gt;)

LOCAL("SOURCE")

LOCAL("ENCOUNTER")

LOCAL("DIAGNOSIS",&lt;PROVIDER IEN&gt;)

LOCAL("PROCEDURE",&lt;PROVIDER IEN&gt;)

LOCAL("PROVIDER",&lt;PROVIDER IEN&gt;)

LOCAL("IMMUNIZATION",&lt;PROVIDER IEN&gt;)

LOCAL("SKIN TEST",&lt;PROVIDER IEN&gt;)

LOCAL("EXAM",&lt;PROVIDER IEN&gt;)

LOCAL("PATIENT ED",&lt;PROVIDER IEN&gt;)

LOCAL("HEALTH FACTORS",&lt;PROVIDER IEN&gt;)

LOCAL("VITALS",&lt;PROVIDER IEN&gt;)

Vitals are not processed by PCE but are passed to the   Vitals/Measurement package.

LOCAL("LOCAL",

This data doesn PCE and will not be

processed by PCE, but it may be used to pass local data

to a local process (see protocol for local data processing).

3. The Encounter and Source nodes are required; the rest are

optional.

4. All entries in the local array are resolved to internal values as

defined below.

5. By convention; use a DUZ = .5 (the POSTMASTER) as a default when

one cannot be determined. This is only for tasked jobs on some

systems.

6. The data in the ENCOUNTER, PROCEDURE, and DIAGNOSIS/

PROBLEM or DIAGNOSIS nodes are the minimal set for capturing

Workload starting 10/1/96. The data in the rest of the nodes with the

associated providers build on the clinically relevant data set and are

not used for workload.

7. While ENCOUNTER, PROCEDURE, and DIAGNOSIS/PROBLEM or DIAGNOSIS values are    required to capture workload and generate a \bill, they may not be present in every data set passed through this event point. For   example, data on Vitals may be collected by a Nurse and passed through the event point for storage independent of other data associated with the encounter. Because of this, these are NOT required values in this version.

8. If there is a different (ancillary) hospital location for this

patient encounter, you have to do a separate encounter. Separate

calls for each hospital location are required.

Required Input

LOCAL(        LOCAL( is a local array as defined in the remainder

of this document. Developers should use an array in

their namespace to represent the LOCAL array; e.g.,

IBDFPCE.

Result returned

PXCASTAT      1 = event processing occurred and the data was passed to DHCP.

0 = event processing could not occur. There is data

in LOCAL("ERROR" explaining why.

LOCAL("ERROR" as described below. Denotes Errors. Data associated

with the error was not filed. The node does not

exist if errors do not occur.

LOCAL("ERROR",&lt;NODE&gt;,&lt;PROVIDER

IEN&gt;,&lt;i&gt;,&lt;PIECE&gt;)="Free text message^REJECTED VALUE"

Where     &lt;NODE&gt;      ::=  "ENCOUNTER" | "VITALS" |

"DIAGNOSIS" | "PROCEDURE" |

"PROBLEM" | rest of list|

&lt;PROVIDER IEN&gt;   ::=    internal entry number of

provider. Is 0 (ZERO) for ENCOUNTER

and SOURCE

&lt;i&gt;   ::=  sub-entry 'i' for that provider

Is 0 (ZERO) for ENCOUNTER, SOURCE

and PROVIDER

&lt;PIECE&gt;    ::=    $P( selector in

LOCAL(&lt;NODE&gt;,&lt;PROVIDER IEN&gt;,&lt;i&gt;)

that failed.

The value of &lt;PIECE&gt; may be 0

(ZERO) if a  problem is found that

does not relate to a single

specific piece.

LOCAL("WARNING" as described below. Denotes problems with the

data that did not prevent processing. Processing

continued after the warnable condition was detected.

The node does not exist if warning, conditions do

not occur. Warnings do NOT affect the value of

PXCASTAT.

LOCAL("WARNING",&lt;NODE&gt;,&lt;PROVIDER IEN&gt;,&lt;i&gt;,&lt;PIECE&gt;)

="Free text message^QUESTIONABLE VALUE"

Where     &lt;NODE&gt;      ::=  "ENCOUNTER" | "VITALS" |

"DIAGNOSIS" | "PROCEDURE" |

"PROBLEM"

&lt;PROVIDER IEN&gt;   ::=    internal entry number of

provider. Is 0 (ZERO) for ENCOUNTER

and SOURCE

&lt;i&gt;   ::=  sub-entry 'i' for that provider

Is 0 (ZERO) for ENCOUNTER, SOURCE,

and PROVIDER

&lt;PIECE&gt;    ::=    $P( selector in

LOCAL(&lt;NODE&gt;,&lt;PROVIDER IEN&gt;,&lt;i&gt;) in

question.

The value of &lt;PIECE&gt; may be 0

(ZERO) if a  problem is found that

does not relate to a single

specific piece.

Entry Point for processing the data in the foreground

FOREGND^PXCA(.LOCAL,.PXCASTAT)     All data for the event driver is

to be stored in the local array, LOCAL(, in the proper format by the source prior to calling this entry point. This entry point validates and

verifies the data and then if there are no validation errors, the data is processed in the foreground. Computation by the source will not continue until all processing is completed by any and all 'down-stream' protocol event points.

Entry Point for processing the data in the background on the Host

BACKGND^PXCA(.LOCAL,.PXCASTAT)     All data for the event driver is

to be stored in the local array, LOCAL(, in the proper format by the source prior to calling this entry point. This entry point validates and verifies the data and then if there are no validation errors, the data is processed in the background via TASKMAN. Computation by the source may continue.

Entry Point for data validation

VALIDATE^PXCA(.LOCAL)  The data in the local  array, LOCAL(, is validated and verified, but is not processed. Use of this entry point by your application will result in the data being validated twice, since it is validated prior to processing by the FOREGND^PXCAEP and BACKGND^PXCAEP entry points. If a piece of data cannot be validated, an entry is placed in the LOCAL("ERROR" node as described above

Protocol for local data processing

PXCA DATA EVENT Other developers who wish to use any of the data in the local array, including local additions, can attach a protocol that

calls their routines to the item multiple of this protocol. This protocol is activated if there are no errors in the data validation and after PCE has processed the data.

For data unique to the encounter

SOURCE data LOCAL("SOURCE") = 1^2^3^4^5, where:

Piece 1

Data Source

Required for PCE

Required for SD

Format:  DATA SOURCES file (#839.7)

Piece 2

DUZ

Required for PCE

Required for Scheduling

Piece 3

Form numbers

Not stored by PCE Piece 4

Batch ID

Not stored by PCE Piece 5

Record ID

Not stored by PCE

Encounter data LOCAL("ENCOUNTER") =

1^2^3^4^5^6^7^8^9^10^11^12^13^14^15^16^17^18, where:

LOCAL("ENCOUNTER",modifier[E;1/.01]) = ""

Piece 1

Appointment Date/Time

Required for PCE

Required for Scheduling

Format: Fileman Date/Time

Piece 2

Patient DFN

Required for PCE

Required for Scheduling

Format: Pointer to IHS PATIENT file (#9000001)

Piece 3

Hospital Location IEN

Each hospital location is a separate encounter P,S

Format: Pointer to HOSPITAL LOCATION file (#44)

Piece 4

Provider IEN

This is the person that saw the Patient at the scheduled date and

time.

Required for PCE

Format: Pointer to NEW PERSON file (#200)

Piece 5

Visit CPT code IEN

Format: Pointer to TYPE OF VISIT (#357.69)

Piece 6

SC Condition

Format: [1 | 0 | null]

Piece 7

AO Condition

Format: [1 | 0 | null]

Piece 8

IR Condition

Format: [1 | 0 | null]

Piece 9

EC Condition

Format: [1 | 0 | null]

Piece 10

MST Condition

Format: [1 | 0 | null]

Piece 13

Eligibility Code IEN

Format: Pointer to ELIGIBILITY CODE file (#8)

Piece 14

Check-out date and time

Format: Fileman Date/Time

Piece 15

Provider indicator (relates to 4)

Required for PCE

Format: Set of Codes

P ::= Primary

S ::= Secondary

Piece 16

Attending Physician IEN

(May or may not be the same as 4)

Format: Pointer to NEW PERSON file (#200)

Piece 17

HNC Condition

Format:  [ 1 | 0 | null ]

Piece 18

CV Condition

Format:  [ 1 | 0 | null ]

All of the remaining entries in the LOCAL( array are specific to a

particular Provider associated with the data on that node. If the

provider is unknown, (for example, the identity of the nurse who

took the vitals isn’t recorded on a scanned encounter form), the

provider subscript &lt;PROVIDER IEN&gt; may be set to zero.

Diagnosis and/or Problems, specific to one provider

We recommend that you use these nodes instead of the separate Diagnosis

and Problem nodes.

If no Diagnosis and/or Problems, $D(LOCAL("DIAGNOSIS/PROBLEM")) is true.

LOCAL("DIAGNOSIS/PROBLEM",&lt;PROVIDER IEN&gt;, i) =

1^2^3^4,...17^18 where:

Piece 1

Diagnosis Code IEN

Required for PCE

Required for Scheduling

Format: Pointer to ICD DIAGNOSIS file (#80)

Piece 2

Diagnosis Specification Code

Required for PCE

N/A for Problem List

Format: Set of Codes

P  ::=  Primary

S  ::=  Secondary

Piece 3

Clinical Lexicon Term IEN

Format: Pointer to EXPRESSIONS file (#757.01)

Piece 4

Problem IEN

Required by Problem List for existing

Format: Pointer to PROBLEM LIST file (#9000011)

Piece 5

Add to Problem List

N/A for PCE

Required by Problem List for new problem

Format: [1 | 0 | null]

Piece 6

Problem Active?

Default is Active if not specified

N/A for PCE

Format: Set of Codes

A  ::= Active

I  ::= Inactive

Piece 7

Problem Onset Date

N/A for PCE

Format: Fileman Date/Time

Piece 8

Problem Resolved Date

N/A for PCE

Format: Fileman Date/Time

Piece 9

SC Condition

Format: [1 | 0 | null]

Piece 10

AO Condition

Format: [1 | 0 | null]

Piece 11

IR Condition

Format: [1 | 0 | null]

Piece 12

EC Condition

Format: [1 | 0 | null]

Piece 13

Provider Narrative

Required for PCE

Required by Problem List for new problem

Format: free text, 2-80 Characters

Piece 14

Category Header for Provider Narrative

N/A for Problem List

Format: free text, 2-80 Characters

Piece 15

MST Condition

Format:  [ 1 | 0 | null ]

Piece 16

HNC Condition

Format:  [ 1 | 0 | null ]

Piece 17

CV Condition

Format:  [ 1 | 0 | null ]

Piece 18

Order/Resulting

Format: Set of Codes

O  ::= Ordering

R  ::= Resulting

B  ::= Both Ordering and Resulting

LOCAL("DIAGNOSIS/PROBLEM",&lt;PROVIDER IEN&gt;,i,"NOTE") = 1, where:

Piece 1

Provider  N/A for PCE

Format: free text, 3-60 Characters

NOTE:  If the NOTE node is not needed, it does not have to exist.

NOTE:  Information is passed to Problem List if there is data for any of

the positions 5-8 on the "DIAGNOSIS/PROBLEM" node or if there is "NOTE" node.

NOTE:  A provider is required to add a new problem to the Problem List.

Diagnosis data list, specific to one provider, for Problems being treated

at this encounter:

If no Diagnoses, then '$D(LOCAL("DIAGNOSIS",&lt;PROVIDER IEN&gt;))is

true.

LOCAL("DIAGNOSIS",&lt;PROVIDER IEN&gt;,i) = 1^2^3^4^...^13^14 where:

Piece 1

Diagnosis code IEN

Required for PCE

Required for Scheduling

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 2

Diagnosis specification code

Will default to "S" if blank

Format: Set of Codes.

P ::= Primary

S ::= Secondary

Piece 3

SC Condition

Format: [1 | 0 | null]

Piece 4

AO Condition

Format: [1 | 0 | null]

Piece 5

IR Condition

Format: [1 | 0 | null]

Piece 6

EC Condition

Format: [1 | 0 | null]

Associated Problem IEN

Format: Pointer to PROBLEM LIST file 9000011

Piece 8

Physician's term for Diagnosis

Required for PCE

Format: free text, 2-80 Characters

Piece 9

Physician's term for Category Header

May have been used as a grouping for a set of related Diagnosis

which the provider selected from

Format: free text, 2-80 Characters

Piece 10

Lexicon IEN

Format:  Pointer to EXPRESSIONS File (#757.01)

Piece 11

MST Condition

Format:  [ 1 | 0 | null ]

Piece 12

HNC Condition

Format:  [ 1 | 0 | null ]

Piece 13

CV Condition

Format:  [ 1 | 0 | null ]

Piece 14

Order/Resulting

Format: Set of Codes

O  ::= Ordering

R  ::= Resulting

B  ::= Both Ordering and Resulting

NOTE:  PCE recommends using the DIAGNOSIS/PROBLEM node so that

the diagnosis can point to the problem that it relates to.

Procedures data list, specific to one provider

If no Procedures, then '$D(LOCAL("PROCEDURE",&lt;PROVIDER IEN&gt;)) is

true.

LOCAL("PROCEDURE",&lt;PROVIDER IEN&gt;,i) = 1^2^3^4^5^6^7^8^9^10^

11^12^13^14,(pieces defined below)

LOCAL("PROCEDURE",&lt;PROVIDER IEN&gt;,i,modifier[E;1/.01]) = ""

Piece 1

CPT4 Procedure code

Required by PCE for V CPT file (Procedures)

if this field is blank then will be stored in V TREATMENT file

Required for Scheduling

Format: Pointer to CPT file (#81)

Piece 2

Quantity Performed

Required for PCE

Required for Scheduling

Format: number &gt; 0

Piece 3

Procedure specification code

For CPT only.

Format: Set of Codes

P ::= Primary

S ::= Secondary

Piece 4

Date/Time Procedure performed

Format: Fileman Date/Time

Piece 5

Primary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 6

Physician's term for Procedure

Required for PCE

Format: free text, 2-80 Characters

Piece 7

Physician's term for Category Header

May have been used as a grouping for a set of related Procedures

which the provider selected from

Format: free text, 2-80 Characters

Piece 8

1st Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 9

2nd Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 10

3rd Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 11

4th Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 12

5th Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 13

6th Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 14

7th Secondary Associated Diagnosis IEN For this CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

NOTE:  If a Procedure doesn’t have a

CPT code, it can be passed without one and will be stored in the

V Treatment file but will not be used for workload or billing.

Problem data list, specific to one provider

If no Problems, then '$D(LOCAL("PROBLEM",&lt;PROVIDER IEN&gt;)) is true.

LOCAL("PROBLEM",&lt;PROVIDER IEN&gt;,i) = 1^2^3^4^5^...^15 where:

Piece 1

Problem Name

Required for new Problem List, i.e. if Pos. 10 is null

Format: free text

Piece 2

Problem Onset Date

Format: Fileman Date/Time

Piece 3

Problem Active?

Default is ACTIVE if not specified

Format: [1 | 0 | null]

Piece 4

Problem Date Resolved

Format: Fileman Date/Time

Piece 5

SC Condition

Format: [1 | 0 | null]

Piece 6

AO Condition

Format: [1 | 0 | null]

Piece 7

IR Condition

Format: [1 | 0 | null]

Piece 8

EC Condition

Format: [1 | 0 | null]

Piece 9

ICD Code value {optional}

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 10

Problem IEN

Must be null if new problem

Required for editing existing Problem

Format: Pointer to PROBLEM LIST file 9000011

Piece 11

Physician's term for Problem

Null if new problem

Format: free text, 60 Characters Max

Piece 12

Lexicon IEN

Format: Pointer to EXPRESSIONS File (#757.01)

Piece 13

MST Condition

Format:  [ 1 | 0 | null ]

Piece 14

HNC Condition

Format:  [ 1 | 0 | null ]

Piece 15

CV Condition

Format:  [ 1 | 0 | null ]

NOTE:  The data in this node is passed to Problem List. A Provider is

required to add a new problem to the Problem List. When a new problem is

added to the Problem List, the problem IEN is not required. If data is

passed to edit existing data, the problem IEN must be passed.

NOTE:  It is better to use the DIAGNOSIS/PROBLEM node so that the

Diagnosis can point to the problem that it relates to.

Provider data list, specific to one provider

Use this node to pass of additional providers which do not have data

associated with them.

If no additional Providers, then '$D(LOCAL("PROVIDER",&lt; PROVIDER

IEN&gt;)) is true.

LOCAL ("PROVIDER",&lt;PROVIDER IEN&gt;= 1^2 where:

Piece 1

Provider indicator

Required for PCE

Format: Set of Codes.

P: = Primary

S: = Secondary

Piece 2

Attending

Format: [1|0| null]

NOTE:  If a provider is on the Encounter node and also on this node

then the data on this node will be used for Primary/Secondary indicator.

Immunization data list, specific to one provider

If no immunization entries, then '$D(LOCAL("IMMUNIZATION",&lt;PROVIDER IEN&gt;))

is true.

LOCAL ("IMMUNIZATION",&lt;PROVIDER IEN&gt;,i)=1^2^3^4^5^6^7^8^9^10^11^12^13^14^15

Piece 1

Immunization

Required for PCE

Format: Pointer to IMMUNIZATION File (9999999.14)

Piece 2

Series

Format: Set of Codes.

P::=Partially complete

C::=Complete

B::=Booster

1::=Series1

...

8::=Series8

Piece 4

Reaction

REACTION Field (9000010.11,.06) SET

Format: Set of Codes.

'0' FOR NONE

'1' FOR FEVER;

'2' FOR IRRITABILITY;

'3' FOR LOCAL REACTION OR SWELLING;

'4' FOR VOMITING;

'5' FOR RASH OR ITCHING;

'6' FOR LETHARGY;

'7' FOR CONVULSIONS;

'8' FOR ARTHRITIS OR ARTHRALGIAS;

'9' FOR ANAPHYLAXIS OR COLLAPSE;

'10' FOR RESPIRATORY DISTRESS;

'11' FOR OTHER;

Piece 5

Contraindicated

Format: [1|0|null]

Piece 6

Event D/T

Format: Fileman Date/Time

Piece 7

Remarks

Format: Comment

Piece 8

Primary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80

Piece 9

1st Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 10

2nd Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 11

3rd Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 12

4th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 13

5th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 14

6th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 15

7th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Skin Test data list, specific to one provider

If no skin test entries, then '$D(LOCAL("SKIN TEST",&lt;PROVIDER IEN&gt;))

is true.  LOCAL ("SKIN TEST",&lt;PROVIDER

IEN&gt;,i)=1^2^3^4^5^6^7^8^9^10^11^12^13

Piece 1

SKIN TEST

Required for PCE

Format: Pointer to SKIN TEST File (9999999.28)

Piece 2

READING

Format: Whole number between 0 and 40 inclusive

Piece 3

RESULT

Format: Set of Codes.

P::=Positive

N::=Negative

D::=Doubtful

0::=No Take

Piece 4

Date Read

Format: Fileman Date/Time

Piece 5

Date of Injection

Format: Fileman Date/Time

Piece 6

Primary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80

Piece 7

1st Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 8

2nd Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 9

3rd Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 10

4th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 11

5th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 12

6th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Piece 13

7th Secondary Associated Diagnosis IEN For this mapped CPT only.

Format: Pointer to ICD DIAGNOSIS File (#80)

Examination data list, specific to one provider

If no examination entries, then '$D(LOCAL("EXAM",&lt;PROVIDER IEN&gt;))

is true.

LOCAL ("EXAM",&lt;PROVIDER.IEN&gt;")=1^2

Piece 1

EXAM

Required for PCE

Format: Pointer to EXAM File (9999999.15)

Piece 2

RESULT

Format: Set of Codes.

A::=Abnormal

N::=Normal

Patient Education data list, specific to one provider

If no Patient Education entries, then '$D(LOCAL("PATIENT ED",&lt;PROVIDER

IEN&gt;)) is true.  LOCAL ("PATIENT ED",&lt;PROVIDER IEN&gt;,i)=1^2

Piece 1

Topic

Required for PCE

Format: Pointer to EDUCATION TOPICS File (9999999.09)

Piece 2

Level of Understanding

Format: Set of Codes.

1::=Poor

2::=Fair

3::=Good

4::=Group - No Assessment

5::=Refused

Health Factors data list, specific to one provider

If no Health Factors entries, then

'$D(LOCAL("HEALTH FACTORS",&lt;PROVIDER IEN&gt;)) is true.  LOCAL ("HEALTH

FACTORS",&lt;PROVIDER IEN&gt;,i)=1^2

Piece 1

Health Factor

Required for PCE

Format: Pointer to HEALTH FACTORS File (9999999.64)

Piece 2

Level/Severity

Format: Set of Codes.

M::=Minimal

MO::=Moderate

H::=Heavy/Severe

Vitals data list, specific to one provider

If no Vitals, then '$D(LOCAL("VITALS",&lt;PROVIDER IEN&gt;)) is true.

LOCAL("VITALS",&lt;PROVIDER IEN&gt;,i) = 1^2^3^4, where:

Piece 1

Type

Required for PCE

Format: Set of Codes.

AG::= ABDOMINAL GIRTH

AUD::= AUDIOMETREY

BP::= BLOOD PRESSURE

FH::= FUNDAL HEIGHT

FT::= FETAL HEART TONES

HC::= HEAD CIRCUMFERENCE

HE::= HEARING

HT::= HEIGHT

PU::= PULSE

RS::= RESPIRATIONS

TMP::=TEMPERATURE

TON::=TONOMETRY

VC::= VISION CORRECTED

VU::= VISION UNCORRECTED

WT::= WEIGHT

Piece 2

Value

Required for PCE

Format: Numeric

Piece 3

Units

Not stored; used for conversions

Format: Set of Codes.

C::=Centigrade (degrees)

CM::=Centimeter

F::= Fahrenheit (degrees)

IN::=Inches

KG::=Kilograms

LB::=Pounds

Piece 4

Date/Time Measurement taken

Format: Fileman Date/Time

If the TYPE is HT:  If the UNIT is CM it is converted to IN so that it                        can be stored. If the UNIT is "" it is assumed to be IN. If the TYPE is WT   If the UNIT is KG it is converted to LB so that it can be stored. If the UNIT is "" it is assumed to be LB. If the TYPE is TMP If the UNIT is C it is    converted to F so that it can be stored. If the UNIT is "" it is assumed to be F.

NOTE:  This data is passed to the Vitals/Measurement package for

validation and storage.

Local data list, specific to one provider

If no local entries, then '$D(LOCAL("LOCAL",&lt;PROVIDER IEN&gt;)) is true.

LOCAL("LOCAL",&lt;PROVIDER IEN&gt;,i) = Site Specific data encoding

Pieces All

Site Specific data encoding

Not stored in PCE

Format: Site Specific

NOTE:  LOCAL("LOCAL" where "LOCAL" is replaced by locally namespaced string.

## 15 Appendix B – PCE Security

PCE security is maintained through menu assignment and VA FileMan protection.

### Menu Assignment

PCE exports one main menu, the PCE IRM Menu, which contains several sub-menus.

SP     PCE Site Parameters Menu ...

TBL    PCE Table Maintenance ...

INFO   PCE Information Only ...

RM     PCE Reminder Maintenance Menu ...

CR     PCE Clinical Reports ...

HOME   Directions to Patient's Home Add/Edit

CO     PCE Coordinator Menu ...

CL     PCE Clinician Menu

- Assign the PCE IRM Main Menu to the IRM person who will maintain and set up the package, including reminder items and will need access to all of the PCE options.
- The first four options/menus will be used by IRM staff or coordinators who are responsible for setting up PCE, maintaining the entries in the PCE tables (such as Patient Education, Immunization, Treatments, etc.), and defining the clinical reminders/maintenance system for your site.
- Assign the PCE Coordinator Menu to the Application Coordinator who teach and support PCE. The PCE Coordinator Menu contains all of the supporting options/menus, plus the data entry options.
- Assign the PCE Clinician Menu to clinicians who enter or edit data, use clinical reports, need the PCE Information Only menu to see the basis for reminders, and might add or edit directions to a patient's home for display on a health summary.
- Assign the PCE COMPACT Act EOC Menu to the locally designated personnel that has the “PX EOC Edit” security key to edit data in the COMPACT ACT EPISODE OF CARE file (#818).
- Assign Directions to Patient's Home Add/Edit to anyone who needs to enter directions to a patient's home-especially useful for Hospital-Based Home Care staff (directions can be viewed on Health Summaries).
- Assign PCE Encounter Data Entry - Supervisor to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries. This action also allows adding and editing in fields not asked in the other PCE Encounter Data Entry options.
- Assign PCE Encounter Data Entry to data entry staff who can document a clinical encounter and who can delete their own entries.
- Assign PCE Encounter Date Entry and Delete to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries.
- Assign PCE Encounter Data Entry without Delete to users who can document a clinical encounter, but should not be able to delete any entries, including ones that they have created.
- Assign the COMPACT ACT EOC EDIT to the locally designated personnel that has the “PX EOC Edit” security key to edit data in the COMPACT ACT EPISODE OF CARE file (#818).
- Assign the COMPACT ACT DISPLAY EOC DATA to the locally designated personnel that has the “PX EOC Edit” security key to display data in the COMPACT ACT EPISODE OF CARE file (#818).

### Security Keys

The following security keys are associated with the PCE package.

| Security Key          | Description                                                                                                                                                                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PXV IMM INVENTORY MGR | This key is assigned to users responsible for immunization inventory management                                                                                                                                                                    |
| PX EOC EDIT           | This key is assigned to users holding the menu options COMPACT Act Display EOC Data and COMPACT Act EOC Edit. Users will be able to display and edit data in the COMPACT ACT EPISODE OF CARE file (#818) through the menus assigned with this key. |

### VA FileMan File Protection

The following VA FileMan file protection has been assigned to the files exported by PCE and Visit Tracking **.**

|   File Number | Name                                | DD   | RD   | WR   | DEL   | LAY   |
|---------------|-------------------------------------|------|------|------|-------|-------|
| 150.1         | ANCILLARY DSS ID                    | @    |      | @    | @     | @     |
| 150.2         | VSIT SITE CODES                     | @    |      | @    | @     | @     |
| 150.9         | VISIT TRACKING PARAMETERS           | @    |      |      | @     | @     |
| 811.1         | PCE Code Mapping                    | @    |      | @    | @     | @     |
| 815           | PCE Parameters                      | @    |      |      | @     | @     |
| 818           | Compact Act Episode of Care File    | @    | @    | @    | @     | @     |
| 839.01        | PXCA Device Interface Module Errors | @    |      |      |       |       |
| 839.7         | PCE Data Source                     | @    |      |      | @     |       |
| 920           | Vaccine Information Statement       | @    |      | @    | @     | @     |
| 920.05        | Imm Default Responses               | @    | @    | @    | @     | @     |
| 920.1         | Immunization Info Source            | @    | @    | @    | @     | @     |
| 920.2         | Imm Administration Route            | @    |      | @    | @     | @     |
| 920.3         | Imm Administration Site (Body)      | @    |      | @    | @     | @     |
| 920.4         | Imm Contraindications Reasons       | @    |      | @    | @     | @     |
| 920.5         | Imm Refusals Reasons                | @    |      | @    | @     | @     |
| 920.6         | Imm Routes To Sites                 | @    | @    | @    | @     | @     |
| 920.71        | Imm External Agency                 | @    | @    | @    | @     | @     |
|   9e+06       | Patient/HIS                         | @    |      |      |       |       |
|   9.00001e+06 | V Provider                          | @    |      |      |       |       |
|   9.00001e+06 | V POV                               | @    |      |      |       |       |
|   9.00001e+06 | V Immunization                      | @    |      |      |       |       |
|   9.00001e+06 | V Skin Test                         | @    |      |      |       |       |
|   9.00001e+06 | V Exam                              | @    |      |      |       |       |
|   9.00001e+06 | V Treatment                         | @    |      |      |       |       |
|   9.00001e+06 | V Patient Ed                        | @    |      |      |       |       |
|   9.00001e+06 | V CPT                               | @    |      |      |       |       |
|   9.00001e+06 | V Health Factors                    | @    |      |      |       |       |
|   9.00001e+06 | V Imm Contra/Refusal Events         | @    | @    | @    | @     | @     |
|   9.00008e+06 | V Immunization Deleted              | @    | @    | @    | @     | @     |
|   1e+07       | Imm Manufacturer                    | @    |      | @    | @     | @     |
|   1e+07       | Location                            | @    |      |      |       |       |
|   1e+07       | Education Topics                    | @    |      |      | @     |       |
|   1e+07       | Immunization                        | @    |      | @    | @     | @     |
|   1e+07       | Exam                                | @    |      |      | @     |       |
|   1e+07       | Treatment                           | @    |      |      | @     |       |
|   1e+07       | Provider Narrative                  | @    |      |      | @     |       |
|   1e+07       | Skin Test                           | @    |      | @    | @     | @     |
|   1e+07       | Immunization Lot                    | @    | @    | @    | @     | @     |
|   1e+07       | Health Factors                      | @    |      |      | @     |       |

### Access Recommended for Sites Using Kernel Part III

|   File Number | Name                                | User   | Coordinator   |
|---------------|-------------------------------------|--------|---------------|
| 811.1         | PCE Code Mapping                    | R      | R             |
| 815           | PCE Parameters                      | R      | RW            |
| 839.01        | PXCA Device Interface Module Errors | RWDL   | RWDL          |
| 839.7         | PCE Data Source                     | RL     | RL            |
|   9e+06       | Patient/HIS                         | RWL    | RWL           |
|   9.00001e+06 | V Provider                          | RWDL   | RWDL          |
|   9.00001e+06 | V POV                               | RWDL   | RWDL          |
|   9.00001e+06 | V Immunization                      | RWDL   | RWDL          |
|   9.00001e+06 | V Skin Test                         | RWDL   | RWDL          |
|   9.00001e+06 | V Exam                              | RWDL   | RWDL          |
|   9.00001e+06 | V Treatment                         | RWDL   | RWDL          |
|   9.00001e+06 | V Patient Ed                        | RWDL   | RWDL          |
|   9.00001e+06 | V CPT                               | RWDL   | RWDL          |
|   9.00001e+06 | V Health Factors                    | RWDL   | RWDL          |
|   1e+07       | Location                            | R      | R             |
|   1e+07       | Education Topics                    | R      | RWL           |
|   1e+07       | Immunization                        | R      | RWL           |
|   1e+07       | Exam                                | R      | RWL           |
|   1e+07       | Treatment                           | R      | RWL           |
|   1e+07       | Provider Narrative                  | RWL    | RWL           |
|   1e+07       | Skin Test                           | R      | RWL           |
|   1e+07       | Health Factors                      | R      | RWL           |

### Visit Tracking

|   File Number | Name                      | User   | Coordinator   |
|---------------|---------------------------|--------|---------------|
| 150.1         | Ancillary DSS ID          | R      | R             |
| 150.2         | Visit Site Codes          | R      | R             |
| 150.9         | Visit Tracking Parameters | R      | RW            |
|   9.00001e+06 | Visit                     | RWDL   | RWDL          |

## 16 Appendix C – Visit Tracking Technical Information

### Introduction

The Visit Tracking software is designed to link patient-related information in a file structure that will allow meaningful reporting and historically accurate categorization of patient events and episodes of care.

### Background

This version of Visit Tracking is a hybrid of a Visit Tracking module developed by and operating at Indian Health Service (IHS) facilities as part of their Patient Care Component (PCC) and Visit Tracking V. 1.0 developed by the Dallas Information Systems Center (ISC) for the Joint Venture Sharing (JVS) sites and operating at Albuquerque, NM. The primary data file (VISIT file #9000010) developed by IHS is used with some additional fields and modifications for VA needs. The supporting software was developed with the intent to operate without modification in either facility.

### Relationship to Other Packages

Visit Tracking is not a stand-alone application. Other packages will normally call PCE, which will handle the calls to Visit Tracking.

Where appropriate, VISTA packages will be able to link an event to a patient visit entry, thereby linking that event to any number of events occurring throughout the hospital during the patient’s visit or admission. By linking events to a “visit,” historical information surrounding that event can be retrieved from the VISIT file (#9000010) that might ordinarily be unknown, such as the patient’s eligibility at time of the event, the category of patient, or the Hospital Location.

### Functions Provided

The Visit Tracking system provides three primary functions:

- Creating and/or matching a visit record using input criteria and user interaction (optionally)
- Providing a list of visits matching input criteria
- Maintaining the VISIT file (#9000010) and its records

Visit Tracking is a utility that can be used by a variety of VISTA modules, with potential benefits for clinical, administrative, and fiscal applications. Visit Tracking will allow VISTA packages to link an event to a patient visit entry, thereby linking that event to any number of events occurring throughout the hospital during the patient’s outpatient and/or inpatient episode.

### Benefits

- The VISIT file (#9000010) will be a key file in the implementation of the clinical repository.
- The VISIT file provides a home for documenting when and where other facility events have occurred.
- Medical Care Cost Recovery (MCCR) can obtain billing information related to a clinic visit, a step towards itemized billing.
- Visit Tracking provides an environment for relating clinical information to the service visit for workload tracking or query by service views, as well as by the aggregate clinic visit view.
- Users have the potential to control the Visit level of granularity while reviewing patient information (e.g., only view visits from the primary clinic visit level: an aggregate view or only ancillary visits).
- The date and time stamp on clinic and ancillary visits could be useful for retrospective workflow analysis. It may be exploitable as a Clinical Event Summary file useful to researchers doing longitudinal patient studies.
- A breakdown of clinical care provided by primary and secondary providers could help document the clinical experience of trainees (including residents, interns, and other clinicians) who require this information for privileging and credentialing purposes.
- Visit tracking has the capability to generate patient activity reports that are based on accurate historical information.
- The category of patient receiving care can be identified based on a specific episode of care.
- Medical data can be stored for historical purposes without the requirements of specific fields, except for the patient and date.
- Visit tracking has the ability to associate ancillary services provided to a patient with a DSS ID, admission, and non-patient encounter (phone contact, pharmacy mail-out, etc.)

### Dependencies

Visit Tracking depends on Patient Care Encounter (PCE). **V** *IST* **A** packages that will support and/or use Visit Tracking will require some programming modifications.

### Visit Creation

The creation of visits is facilitated by the Visit Tracking module. In order to ensure a consistent implementation of visit creation across packages, each package needs to have an agreement with the Visit Administrator to create visits.

The key to the creation of visits will be to ensure the clinical meaningfulness of visits.

Additionally, when a package works out an agreement with Visit Tracking, it must add the triggered cross-reference ADD^AUPNVSIT, SUB^AUPNVSIT, as well as a regular (whole file) cross-reference on the Visit pointer. This ensures that the visit will not be removed by Visit Tracking utilities because the dependent entry counter has been updated.

#### Two Approaches for Creating Clinical Visits

1. A team of providers can be associated with a primary clinical visit (this is the traditional view taken by IHS).
2. A primary clinic visit can represent the primary provider’s care, and a separate visit can be created to reflect the secondary provider’s care.

Additionally, the VISIT file will be able to provide a breakdown of other ancillary services provided during the clinically significant visit. Laboratory or Radiology occasions of service are other examples of services provided that could have a separate visit reflecting the service involvement related to a clinic appointment on the same day. DSS and Outpatient Workload will benefit from a service breakdown.

### IRM Responsibility

IRM will be responsible for updating the VISIT TRACKING PARAMETERS file (#150.9). IRM will also have the capability to indicate if a package is active or inactive. No other maintenance is required by IRM.

### Guidelines for Developers

This section describes the guidelines which should be used for VA developers populating visits in the Visit file. These guidelines are based on a combination of the experience of Albuquerque’s joint venture sharing, IHS’ PCC pilot test at Tucson VAMC, MCCR data capture pilots, HSR&amp;D workload reporting studies at Hines VAMC, and DMMS/DSS event data capture.

The purpose of the VISIT file in the VA:

The VISIT file has multiple purposes. The primary role is to record when and where clinical encounters related to a patient have occurred. Visits will be recorded for both Outpatient and Inpatient encounters. The initial focus of the Visit file will be for tracking outpatient encounter activity.

- Outpatient encounters include scheduled appointments and walk-in unscheduled visits.
- Inpatient encounters include the admission of a patient to a VAMC and any clinically significant change related to treatment of that patient. For example, a treating specialty change is clinically significant, whereas a bed switch is not. The clinically significant visits created throughout the inpatient stay are related to the inpatient admission visit.
- If the patient is seen in a clinic while an Inpatient, a separate visit will be created representing the appointment visit – this visit is related to the Admission visit.
- A clinician’s telephone communications with a patient may be represented by a separate visit.
- The clinical visits can be viewed from two approaches: 1) a team of providers can be associated with a primary clinical visit (this is the traditional view taken by IHS); or 2) a primary clinic visit can represent the primary provider’s care, and a separate visit can be created to reflect the secondary provider’s care.
- Additionally, the VISIT file can provide a breakdown of other ancillary services provided during the clinically significant visit. Laboratory or Radiology services are other examples of services provided that could have a separate visit reflecting the service involvement related to a clinic appointment on the same day.

### Supported Entry Points

Creating visit entries in the VISIT file is not a free-for-all. Packages wishing to create visits or call Visit Tracking must publish agreements with the DBA. The DBA office provides oversight on agreements.

### Conventions

Italic formatting indicates argument names that are replaced with actual values. The notation “.argument” indicates a call by reference.

Note:  [  ] indicates optional choices; {  } indicates required choices.

Refer to the section “Description of VISIT file fields” to see which fields are required, which ones will generate default values, and which ones can be used in matching/screening when selecting preexisting visits.

### Create and/or Match Visit Using Input Criteria

^VSIT

(See the Package-Wide Variables section)

INPUT:	VSIT	&lt;visit date [and time] in FM format&gt;

(time will default to 12 noon if not specified)

DFN	&lt;patient file pointer&gt;

[VSIT(0]	&lt;a string of characters that defines how the visit

processor will function, see package-wide variables&gt;

[VSIT("&lt;xxx&gt;")]	&lt;array with mnemonic subscript&gt;

(used in match logic if VSIT(0)["M”)

(for SVC, TYP, INS, CLN, ELG, LOC)

Note:  For multiple field values use [&lt;field

value&gt;[^...]]

i.e., VSIT("SVC")="H^D"  (will find both)

VSITPKG	&lt;package name space&gt;

OUTPUT:		VSIT(&lt;ien	N^S[^1]

where: N	&lt;internal entry number of visit&gt;

or -1 if could not get a visit

or -2 if calling package is not active

in Visit Package Parameters

S	&lt;value of .01 field of visit&gt;

1	&lt;indicates that a new visit was added&gt;

VSIT(&lt;ien&gt;,&lt;xxx&gt;)	returns the data that is stored in the Visit file

### Update Dependent Entry Counter

These calls are customarily done through a MUMPS cross reference on the pointer field. The input parameter X is set by FileMan.

ADD^AUPNVSIT

Increase the dependent entry count by one.

INPUT	X	Visit IEN

SUB^AUPNVSIT

Decrease the dependent entry count by one	INPUT	X	Visit IEN

$$PKG2IEN^VSIT(PKG)

Returns a pointer to the Package file when you pass in the package namespace

INPUT	PKG		Package namespace

OUTPUT			Pointer to the package in the Package file #9.4

$$PKG^VSIT(PKG,VALUE)

Entry point to add or edit package to multiple in tracking param

INPUT	PKG		Package Name Space

VALUE	Value on the ON/OFF flag under package

Multiple 1=ON  0=OFF

$$PKGON^VSIT(PKG)

Returns the active flag for the package

INPUT	PKG		Package Name Space

OUTPUT			1 the package can create visits

0 the package cannot create visits

-1 called wrong or could not find package in VT

parameters file

$$IEN2VID^VSIT(IEN)

Returns the Visit ID when you pass in a pointer to a visit

INPUT	IEN		Visit IEN

OUTPUT			Visit ID

$$VID2IEN^VSIT(VID)

Returns a pointer to a visit when you pass in the Visit ID

INPUT	VID		Visit ID

OUTPUT			Visit IEN

$$LOOKUP^VSIT(IEN,FMT,WITHIEN)

Look up a visit and return all of its information

INPUT	IEN		Visit IEN OR the Visit's ID

FORMAT is the format that you want the output

in, where:

I ::= internal format

E ::= external format

B ::= both internal and external format

B is the default if anything other than "I" or "E"

WITHIEN 0 if you do not want the ien of the visit

as the first subscript

1 if you do.  "1" is the default.

OUTPUT			-1 if IEN was not a valid IEN or Visit ID

otherwise returns IEN

VSIT(&lt;ien&gt;,&lt;xxx&gt;)

or		VSIT(&lt;xxx&gt;)	depending on the value of WITHIEN

The array is all of the fields in the visit file. If both internal and external format are returned the format is:  internal^external

SELECTED^VSIT(DFN,SDT,EDT,HOSLOC,ENCTYPE,NENCTYPE,SERVCAT,NSERVCAT,LASTN)

Returns selected visits depending on screens passed in.

INPUT	DFN	DFN			of Patient (only required input)

SDT			Start Date

EDT			End Date

HOSLOC			Hospital Location

ENCTYPE		Encounter types to include

NENCTYPE		Encounter types to exclude

SERVCAT		Service Categories to include

NSERVCAT		Service Categories to exclude

LASTN		How many starting with the Date and

going backwards until have that many

or all of them, whichever is first

### Only the DFN is Required

Encounter types are a string of all the encounter types wanted. e.g. "OA" for only Ancillary and Occasion of service. Not Encounter types is a string of all the encounter types not wanted. e.g. "T" for do not include Telephone. If Encounter types and Not Encounter types are null or not passed, then all encounter types will be included. Service Categories is a string of all the service categories to include. If none is passed all is assumed.  e.g. "H" for just historical, "T" for just Telephone, "AIT" for ambulatory (in and out patient) and Telephone. Not Service categories is a string of all the service categories to not include.

OUTPUT	^TMP("VSIT",$J,vsit ien,#)

Piece 1:: Date and Time from the Visit File Entry

Piece 2:: Hospital Location ien (pointer to file#44)\_";"\_

External Value

If service category = "H" then this Piece becomes

the following:: Location of Encounter

ien (Pointer to file #9999999.06)\_";"\_External Value

Piece 3:: Service Category (Value of field .07 set of codes)

Piece 4:: Service Connected (Value of field 80001 External Value)

Piece 5:: Patient Status in/out (Value of field 15002 set of codes)

Piece 6:: Clinic Stop ien (Pointer to file # 40.7) ";" External value)

$$HISTORIC^VSIT(IEN)

Returns a flag indicating whether the visit is historical.

INPUT	IEN		Visit IEN

OUTPUT			1 if it is an Historical visit ("E" in #.07)

0 if it is not an Historical visit.

-1 if the IEN is bad

MODIFIED^VSIT(IEN)

Sets the Date Last Modified (.13) field to NOW

INPUT	IEN		Visit IEN

KILL^VSITKIL(IEN)

Deletes the visit if there is no files pointing to it.  Before deleting checks all the backware pointers to see if the visit is being pointed to.

INPUT	IEN		Visit IEN

### Package-Wide Variables

Visit Tracking V2.0 has no package-wide variables requiring SACC exemptions. Package developers making calls to Visit Tracking must clean up locally created variables before exiting the application option.

The following are local package-wide variables under the VSIT namespace.

VSIT(&lt;xxx&gt;)	Variable Names for VISIT file fields,

file: 9000010, global: ^AUPNVSIT( Where &lt;xxx&gt; is a general reference to the field mnemonic.

Key			Indicates

r			indicated a required field

m			matching/screening logic can/does apply

s			system generated

e			strongly encouraged

Key	Variable	Description

.001	VSIT("IEN”)	NUMBER (visit internal entry number)

rm	.01	VSIT("VDT”)	VISIT/ADMIT DATE&amp;TIME (date)

s	.02	VSIT("CDT”)	DATE VISIT CREATED (date)

m	.03	VSIT("TYP”)	TYPE (set)

rm	.05	VSIT("PAT”)	PATIENT NAME (pointer PATIENT file

#9000001) (IHS file DINUMed to PATIENT

file #2)

m	.06	VSIT("INS”)	LOC. OF ENCOUNTER (pointer LOCATION

file #9999999.06) (IHS file DINUMed to

INSTITUTION file #4)

.07	VSIT("SVC”)	SERVICE CATEGORY (set)

me	.08	VSIT("DSS”)	DSS ID (pointer to CLINIC STOP file)

.09	VSIT("CTR”)	DEPENDENT ENTRY COUNTER (number)

.11	VSIT("DEL”)	DELETE FLAG (set)

.12	VSIT("LNK”)	PARENT VISIT LINK (pointer VISIT file

#9000010)

.13	VSIT("MDT”)	DATE LAST MODIFIED (date)

.18	VSIT("COD") ; 	CHECK OUT DATE&amp;TIME (date)

.21	VSIT("ELG”)	ELIGIBILITY (pointer ELIGIBILITY CODE

file #8)

Key	Variable	Description

mr	.22	VSIT("LOC”)	HOSPITAL LOCATION (pointer HOSPITAL

LOCATION file #44)

.23	VSIT("USR”)	CREATED BY USER (pointer NEW PERSON

file #200)

.24	VSIT("OPT”)	OPTION USED TO CREATE (pointer

OPTION file #19)

.25	VSIT("PRO")	PROTOCOL (pointer PROTOCOL file #101)

.26	VSIT("ACT")	PFSS ACCOUNT REFERENCE (pointer

PFSS ACCOUNT file #375)

2101	     VSIT("OUT”)	OUTSIDE LOCATION (free text)

80001 	     VSIT("SC")	SERVICE CONNECTED (set)

80002 	     VSIT("AO"	AGENT ORANGE EXPOSURE (set)

80003	     VSIT("IR")	IONIZING RADIATION EXPOSURE (set)

80004	     VSIT("EC")	SW ASIA CONDITIONS (set)

80005	     VSIT("MST")	MILITARY SEXUAL TRAUMA (set)

80006	     VSIT("HNC")	HEAD AND/OR NECK CANCER (set)

80007	     VSIT("CV")	COMBAT VETERAN

80008	     VSIT("SHAD")	PROJ 112/SHAD (set)

15001	     VSIT("VID")	VISIT ID (free text)

15002	     VSIT("IO")	PATIENT STATUS IN/OUT (set)

15003	     VSIT("PRI")	ENCOUNTER TYPE (set)

81101	     VSIT("COM")	COMMENTS

81202	     VSIT("PKG")	PACKAGE (pointer PACKAGE file #9.4)

81203	     VSIT("SOR")	DATA SOURCE (pointer PCE DATA SOURCE file #839.7)

VSIT(0)	A string of characters that defines how the visit

processor will function.

F	Force adding a new entry.

I	Interactive mode

E	Use patient’s primary eligibility if not defined on call

with VSIT("ELG").

N	Allow creation of new visit.

D	Look back “n” number of days for match, defaults to one

(1). D[&lt;number of days&gt;] i.e., VSIT(0)="D7" e.g.,

VSIT(0)="D5" (visit date to visit date - 4) use "D0" to

require exact match on visit date and time.

M	Impose criteria on matching/screening of visits. Uses the

VSIT(&lt;xxx&gt;) array: Matching elements must equal their

corresponding field.

DFN	Internal entry number of the patient file.

VSIT	The date (and time) of the visit.

VSIT(&lt;ien&gt;	N^S[^1]

where:

N = &lt;internal entry number of visit&gt;

S = &lt;value of .01 field of visit&gt;

1 = &lt;indicates that a new visit was added

^TMP("VSITDD",$J,&lt;xxx&gt;&lt;visit subscript&gt;;&lt;field #&gt;;&lt;node&gt;;&lt;piece&gt;;

&lt;error message&gt;

VSITPKG	Package Name Space

## 17 Appendix D – PX HF MEASUREMENT REPAIR

### Introduction

The emergency PX*1*234 patch addresses PCE V Health Factors Measurements Repair and introduces the option PX HF MEASUREMENT REPAIR. This option is used to edit/delete corrupted data measurements in V Health Factor entries due to a bug in patch PX*1*211.

### Background

Patch PX*1*211 had a bug, when a health factor (HF) that had a measurement defined was given to a patient, the VHF entry had the UCUM CODE stored even though a measurement was not being recorded. Patch PX*1*217 corrected the bug.

### PX HF MEASUREMENTS REPAIR

When the PX*1*234 patch is installed, an automatic repair of the corrupted data is applied. Members of the PCE Management Mail Group will receive one and possibly two MailMan messages. Each of these messages will have a different course of action.

#### HEALTH FACTORS WITH INCOMPLETE MESUREMENT DEFINITION

When a message with the subject: HEALTH FACTORS WITH INCOMPLETE MEASUREMENT DEFINITION is received, it means that one or more health factors having an incomplete measurement definition were found during the installation process. The user can add the missing fields using the Health Factor Management menu option.

**Sample message:**

Subj: HEALTH FACTORS WITH INCOMPLETE MEASUREMENT DEFINITION (#109720)

12/15/22@16:46  18 lines

From: PCE Support   In ‘IN’ basket.   Page 1  *New*

--------------------------------------------------------------------------------------

The following health factors have incomplete measurement definitions, they should be completed as soon as possible.

Example 1

MINIMUM VALUE: 32

MAXIMUM VALUE: 123

MAXIMUM DECIMALS: 1

UCUM CODE: Weber

PROMPT CAPTION: Missing

UCUM DISPLAY: Missing

Example 2

MINIMUM VALUE: -12.3

MAXIMUM VALUE: 12.3

MAXIMUM DECIMALS: 1

UCUM CODE: part per million

PROMPT CAPTION: Missing

UCUM DISPLAY: Missing

Enter message action (in IN basket): Ignore//

If there are any HFs with incomplete measurement definitions they should be corrected before starting the manual VHF repair.

#### V HEALTH FACTORS measurement repair

When a message with the subject: V HEALTH FACTORS MEASUREMENT REPAIR is received, it means that there are VHF entries that could not be automatically repaired. These items will require human interaction for correction.

**Note** : If there are LCS HEALTH FACTORS listed, the site LCS coordinator should assist with the correction.

The sample message below shows entry 188201 cannot be automatically repaired. It is missing the MAGNITUDE entry.

**Sample message:**

Subj: V HEALTH FACTORS MEASUREMENT REPAIR (#295925)

01/04/23@11:43  26 lines

From: PCE Support   In ‘IN’ basket.   Page 1  *New*

--------------------------------------------------------------------------------------

V HEALTH FACTORS measurement repair completed at Jan 04, 2023@11:43:10

Measurements were repaired for 3 entries.

There were 2 V HEALTH FACTORS entries that could not be automatically repaired:

Health Factor: VA-HTN SELF-RECORDED SYSTOLIC BLOOD PRESSURE

Minimum Value: 5

Maximum Value: 300

Maximum Decimals: 0

UCUM Code: millimeter of mercury

V Health Factors IEN: 188201

Visit: Jan 04, 2023@7:42

Patient: CPRSONE, PATIENT

MAGNITUDE: Missing; UCUM CODE: millimeter of mercury

Comments: EIGHTY

Enter message action (in IN basket): Ignore//

**To make repairs:**

In VistA use the option PX HF MEASUREMENT REPAIR and follow the below prompts. This option should be assigned to the person who will make the repairs. It starts a repair measurement editor.

**Note:** You will need the VHF IEN listed in the MailMan message.

V HEALTH FACTOR MEASUREMENT REPAIR

Edit the measurement for selected V HEALTH FACTOR entries.
Input the internal entry number, or press ENTER to exit: **188201 &lt;Enter&gt;**

VA-HTN SELF-RECORDED SYSTOLIC BLOOD PRESSURE     CPRSONE,PATIENT     JAN 4,2023@07:42       
NATIONAL

...OK? **Yes//** (Yes)

Health Factor: VA-HTN SELF-RECORDED SYSTOLIC BLOOD PRESSURE
 MINIMUM VALUE: 5
 MAXIMUM VALUE: 300
 MAXIMUM DECIMALS: 0
 UCUM DESCRIPTION: millimeter of mercury
 COMMENTS: EIGHTY
 MAGNITUDE: **80 &lt;Enter&gt;**

UCUM CODE: millimeter of mercury// **&lt;Enter&gt;**

The editor displays the allowed range and units for the measurement. In the above example, a human can interpret “EIGHTY” in the COMMENTS field to be the number 80 and recognize that it is in the inclusive range 5 to 300, so the MAGNITUDE can be set to 80.

As you work through the list, there will be COMMENTS where it is straight forward to determine a magnitude and others where a magnitude cannot be determined. When a magnitude cannot be determined, the UCUM CODE should be deleted.

V HEALTH FACTOR MEASUREMENT REPAIR

Edit the measurement for selected V HEALTH FACTOR entries.
Input the internal entry number, or press ENTER to exit: **188114 &lt;Enter&gt;**

VA-HTN SELF-RECORDED SYSTOLIC BLOOD PRESSURE     CPRSONE,PATIENT     JAN 4,2023@07:42       
NATIONAL

...OK? **Yes//** (Yes)

Health Factor: VA-HTN SELF-RECORDED SYSTOLIC BLOOD PRESSURE
 MINIMUM VALUE: 5
 MAXIMUM VALUE: 300
 MAXIMUM DECIMALS: 0
 UCUM DESCRIPTION: millimeter of mercury
 COMMENTS: Can’t recall

MAGNITUDE: **&lt;Enter&gt;**

UCUM CODE: millimeter of mercury//@ **&lt;Enter&gt;**

When there is a valid measurement, both MAGNITUDE and UCUM CODE must be stored in the VHF entry. If there is no measurement, then neither MAGNITUDE nor UCUM CODE should be present. If only one of those two fields is present it can cause Health Summary errors.

Shown below are the two LCS health factors measurement definitions and some actual COMMENTS from a site. Each comment is followed by a suggestion for what to do about setting the magnitude. In the suggestions, CNBD stands for Cannot be Determined, in those cases if the UCUM CODE is present it should be deleted.

LCS PACKS/DAY

MINIMUM VALUE: 0        MAXIMUM VALUE: 10                     MAXIMUM DECIMALS: 2

UCUM CODE: number     PROMPT CAPTION: Packs/day       UCUM DISPLAY: NO DISPLAY

In determining packs/day, it is helpful to know a pack contains 20 cigarettes.

COMMENTS:
3/4   =  0.75
4 CIGARS PER DAY = CNBD, this is for cigarette smoking only.
"3 days to finish pack" = 0.33
"I never smoked a pack in a day" = CNBD 
chews all day. = CNBD, this is for smoking cigarettes, not chewing.
unkn  = CNBD
3- 4 cans per week  = CNBD, this is for smoking cigarettes, not chewing.
1 CIGARETTE DAILY  = 1/20 = 0.05
3 cig/day = CNBD, this is for cigarette smoking only.

LCS YEARS SMOKED

MINIMUM VALUE: 0        MAXIMUM VALUE: 80                  MAXIMUM DECIMALS: 1

UCUM CODE: number     PROMPT CAPTION: # of years     UCUM DISPLAY: NO DISPLAY

COMMENTS:
3 cigarettes a day for 60 years = 60
10 cigarettes per day = CNBD
&gt;15 years = 15
pt reports smoking 1 pack daily for over 40 yrs = 40
unsure = CNBD
1/2 pack per day for 30 years = 30
1/2 pk per day or less over 30 years = 30
1 CIGAR EVERY SUNDAY = CNBD
40+ years = 40