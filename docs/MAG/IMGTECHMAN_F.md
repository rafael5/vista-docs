---
app_name: VistA Imaging System (MAG)
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
package_id: MAG
patch: null
patch_gap: null
section: ''
source_file: IMGTECHMAN_F.docx
status: draft
title: VistA Imaging System Technical Manual
---

<!-- image -->

# VistA Imaging System Technical Manual

July 2019 – Revision 46 MAG*3.0*204

Department of Veterans Affairs Product Development

Health Provider Systems

**VistA Imaging Technical Manual VistA Imaging MAG*3.0*204, July 2019**

**Property of the US Government**

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Product Development Department of Veterans Affairs Internet: REDACTED

SharePoint: REDACTED

### Preface

The purpose of this manual is to provide information about the structure and function of the logical components of the Veterans Health Information Systems and Technology Architecture (VistA) Imaging V. 3.0 package (i.e., files, routines, and configuration that comprise the VistA Imaging System). Although this document describes some security functions, sensitive information regarding the VistA Imaging System can only be found in the Security Guide.

This document describes…

- How to implement and maintain the VistA Imaging System, its routines and files, options, and cross-references among files.
- How files are archived and purged.
- The established relations among the VistA Imaging System components and other components inside and outside of the Imaging software.

The VistA Imaging System Technical Manual is part of a suite of manuals that includes a release notes document, security guide, user manuals and installation guides. Information about various VistA Imaging System components (i.e., servers, workstations, and background processors) can be found in the Installation Guide.

***The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.***

***VA Policy states the following:***

***Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.***

***Modifying FDA regulated software under any other conditions is a severe violation of the Code of Federal Regulations. Local, that is field-based, developers are prohibited from modifying national software that is certified by the FDA.***

| **Revision History**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 July 2019           | MAG*3.0*204 ---  REDACTED  Update title page, footers, and TOC                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2 November 2018        | MAG*3.0*222 ---  REDACTED  Updated section 9.4.2                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 1 November 2018        | MAG*3.0*218 updates ---  REDACTED  Updated section 6.2.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 4 October 2018         | MAG*3.0*178,181,182,184,206 updates ---  REDACTED  Added chapter 19, sections 19.1, 19.1.1, 19.2                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 1 October 2018         | MAG*3.0*204 updates ---  REDACTED  Updated sections 5.1, 6.3.5, 7.2.1                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 24 September  2018     | MAG*3.0*162,166,174,180 ---  REDACTED  Updated section 6.2.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 08 February 2018       | MAG*3.0*188 , updates(rev 42) ---  REDACTED  Updated section 7.2.1, Chapter 7 VistA Imaging System M Files VA FileMan Files  -  Added two rows to table : ( MUSE TEST TYPES &amp; MUSE FORMAT TABLE                                                                                                                                                                                                                                                                                                                           |
| 2 Oct 2013             | MAG*3.0*130, 131, 133, 135, 140 updates (rev 41)—  REDACTED  Updated for MAG*3.0*130, 131, 133, 135, 140 applying the changes to the proper base document Updated sections 3.5.2, 6.3.1, 6.3.5, 8.7, Chapter 9 (numerous changes throughout the chapter) 12.5,  12.7, 12.9.2, 12.9.2.2, Index  - Deleted section A.2 BP Error Messages - Added section A.2, BP Troubleshooting                                                                                                                                                |
| 10 Sep 2013            | MAG*3.0*130, 131, 133, 135, 140 updates (rev 41)—  REDACTED  -  Updated sections 3.6.2, 6.31 6.3.5, 8.7, 12.15, Index  - Deleted section A.2 BP Error Messages - Added section A.2, BP Troubleshooting                                                                                                                                                                                                                                                                                                                        |
| 26 August 2013         | MAG*3.0*127 updates (rev. 40)—  REDACTED  - Updated sections 3.3, 6.3.1, 6..3.3, 8.1, A.1 MAG*3.0*34/1116/118 updates (rev. 40)—  REDACTED  **-**  Updated sections 1.4, 1.5, 1.7, 3.3, 3.6,, 3.6.1, 3.6.5, 3.9, 4.1, 5.1.1, 5.2.1, 5.3.1.8, 5.3.1.9,5.3.1.10, 6.1,  6.1.1, 6.2.1,6.2.2, 6.3.4, 6.3.9, 7.2.1, 7.7, 7.8, 8.2, 8.5, 8.6, 8.9.1, 8.10.1, 9.1,12.4,12.5, 12.6,15.1, A.3,  - Added sections 7.5, 7.6, 8.3, 8.4, 11.4, 11.4.1, 11.4.2.2,11.4.2.3  MAG*3.0*129 updates (rev. 40)—  REDACTED  - Updated section 6.3.1 |
| 15 Mar 2013            | MAG*3.0*124 updates (rev 39)—  REDACTED  - Updated sections 1.7, 3.1, 8.3: changed title to MAG Reason Edit [Mag Sys Menu]; Index - Added section 3.6.5, Security Keys for AWIV Web Application                                                                                                                                                                                                                                                                                                                               |
| 01 Dec 2012            | MAG*3.0*122 and MAG*3.0*123 updates (rev 38) –  REDACTED  .  - Updated sections 3.6.1, 3.11, 6.1.2, 6.3.1, 7.2.1, 7.3.1.                                                                                                                                                                                                                                                                                                                                                                                                      |
| 01 Aug 2012            | MAG*3.0*120 updates (rev 37) –  REDACTED  - Added section 1.2, VistARad Product Perspective and Features. - Added section 1.8, Windows 7 Considerations.  - Revised sections 2.1; 2.2; 2.3; 3.1.1; 3.2; 3.3; 6.3.1; and 8.12.  - Replaced section 12.7, CCOW Communication, and retitled it as Context Management; added four new subsections. - Added new section 12.8, CPRS Tools Menu Option for VistARad.                                                                                                                 |
| 25 Jan 2012            | MAG*3.0*121 updates (rev 36)  REDACTED  - Updated sections 6.3.2, 10.1 and 18.1.5 A.2.2.  - Added new section 12.8.3.                                                                                                                                                                                                                                                                                                                                                                                                         |
| 09 Nov 2011            | MAG*3.0*104 updates (rev 35)  REDACTED  r.  - Updated sections 1.6, 3.5 and 12.10 - Added new sections 6.3.8 and 9.9.                                                                                                                                                                                                                                                                                                                                                                                                         |
| 01 Sep 2011            | MAG*3.0*49,99,117 updates (rev 34)  REDACTED  MAG*3.0*49 – Updated sections 6.3.4, 8.2, 8.3, 8.4, 8.7, 12.1, 12.4.2.  Added new sections: 8.2.1, 8.2.1.1, 8.2.1.2, 12.2 12.3, 13.1.3, 13.1.4, 13.1.5.  MAG*3.0*99 – Updated sections 6.2.1, 6.3.4.  MAG*3.0*117 – Updated sections 3.6.2, 6.3.1, 7.2.1.                                                                                                                                                                                                                       |

| **Revision History**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 31 May 2011            | MAG*3.0*39 updates (rev 33)  REDACTED  - Updated sections 1.3, 5.1.1, 5.1.2, 5.3.1.5, 5.4, 5.5, 6.3.2, 6.3.3, 7.2.1, 8.2, 8.4, 9.3.2, 9.3.3,  9.3.3.1.1 to 9.3.3.1.8, and modified Chapter 9 name  - Added new sections 9.5.5 and 9.5.6 and renumbered existing subheadings affected  -- Re-organized subheadings in Chapter 9  - Made global corrections listed on page 1 of the Change Pages document                                                                           |
| 10 May 2011            | MAG*3.0*106 updates (rev 32)  REDACTED  - Updated sections 3.6.3, 6.3.1, and 7.2. Added new section 3.11.                                                                                                                                                                                                                                                                                                                                                                         |
| 21 Mar 2011            | MAG*3.0*115 updates (rev 31)  REDACTED  - Updated sections 6.3.5 and Appendix A.5 for Patch 115. - Added sections 12.9 and 13.2 for Patch 115.                                                                                                                                                                                                                                                                                                                                    |
| 01 Feb 2011            | MAG*3.0*105 and 98 updates (rev 30)  REDACTED  - Updated section 1.6 for Patch 105  - Updated sections 5.6, 6.3.7, 9.5.2.2, 9.5.2.3.1 for Patch 98                                                                                                                                                                                                                                                                                                                                |
| 01 Dec 2010            | MAG*3.0*53 and 66 updates (rev 29).  REDACTED  - Updated sections 3.3, 6.2.1, 6.3.4, 7.2.1, 8.7.1, 8.8.1, and 12.2.2 for Patch 53.  -  Updated sections 1. 4, 6.2.1, and 12.2.2 for Patch 66.                                                                                                                                                                                                                                                                                     |
| 05 Oct 2010            | MAG*3.0*108, 90, 94 and 114 updates (rev 28).  REDACTED  - Updated sections 3.6.4, 6.3.5, and Appendix 5 for Patch 90. - Updated sections 3.6.2, 10, and 18.1 for Patches 94 and 108. - Updated sections 6.3.3 and 15.1 for Patch 114.                                                                                                                                                                                                                                            |
| 09 Jul 2010            | MAG*3.0*83 updates, minor corrections (rev 27).  REDACTED  -  Updated sections: 1.4, 3.6.1, and 5.1.1; new sections 1.6, 3.5, and 12.8 for MAG*3.0*83.  -  General corrections: 6.1.2, 12.4, 18.1.1, and 18.1.2.                                                                                                                                                                                                                                                                  |
| 10 Feb 2010            | Patch 93 and Patch 101 updates, general cleanup (rev 26).  REDACTED  -  Updated sections 3.6.2, 6.3.1, 7.2.1, 7.2.3, 8.2, 11.1.2 for Patch 93.  -  New sections: 8.2 subsections, 11.1.3.4, 11.1.3.5, 11.1.3.6 for Patch 93.  -  Updated Sections 3.6.4, 6.3.5, 7.2.1, and Appendix A.5 for Patch 101.                                                                                                                                                                            |
| 20 Oct 2009            | Patch 72 and Patch 54 updates; general cleanup (rev 25).  REDACTED  - Updated sections 3.6.1 and 6.3.1 for Patch 72. - Revised content in section 6.2.3 (detail moved to Security Guide); removed outdated information from 15.1, 18.1.1, and 18.1.2.                                                                                                                                                                                                                             |
| 19 Aug 2008            | Patch 95 updates and misc. cleanup (rev 24)  REDACTED  - Updated and formatted patch list in section 3.1 - Updated section 6.3.1 for Patch 95 - Remove obsolete section related to test images and demo mode (6.3.1.1, 6.3.1.2, and 11.3.4.); remove redundant screen shots from Chapter 7; correct outdated content in section 9.5.2.1 (JL)                                                                                                                                      |
| 29 Feb 2008            | Patch 59 updates (rev 23) -  REDACTED  - Updated sections 6.3.1 and 6.3.3 for Patch 59. - New section Appendix B and B.1 for Means Tests Patch 59.                                                                                                                                                                                                                                                                                                                                |
| 14 Jan 2008            | Patch 76 updates and misc. corrections (rev 22). –  REDACTED  - Clarify MAG\_DECOMPRESSOR content in section 6.3.6. - Updated sections 3.6.4 and 3.6.5 for p76                                                                                                                                                                                                                                                                                                                    |
| 15 Nov 2007            | Patch 81 and 69 updates (rev 21) -  REDACTED  .  - Removed old info from chapter 17, added pointer to new info for p81 - Updated sections 6.2.1, 6.2.2, and 12.2.2; removed section 6.2.4 for p69                                                                                                                                                                                                                                                                                 |
| 04 May 2007            | Patch 77, 46 and 65 updates (rev 20) –  REDACTED  - Added revision # to revision table, title page, and footer, corrected typo in section 9.5.4.4. - Updated sections 8.2 and 12.5.2 for Patch 77. - New section 12.6 for Imaging site reports Patch 77.  -  Updated sections 3.1, 3.3, 6.4.1, 6.4.3, 7.2.1, 8.2, 12.3, and 15.1 for Patch 46.  - New section 12.5 for CCOW communication Imaging site reports for Patch 46. - Updates sections 3.3, 7.2.1, and 8.7 for Patch 65. |

| **Revision History**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 21 Jul 2006            | Patch 50 and 20 updates (rev 19) -  REDACTED  .  - Updated section 12.5.2 for patch 78.  -  Updated the following sections for patch 20: 1.3, 5.1.1, 5.3.1.5, 6.4.2-3, 9.3.2, 9.3.3.1.1-8, 11.1.1 and  12.5.2.  - Updated section 7.2.1 for patch 50.                                                                                                                                                                                                                                                                                    |
| 30 Jun 2006            | Patch 51 and 18 updates (rev 18) –  REDACTED  .  - Added new section 6.4.6 and updated section 7.2.1 for patch 51.  - Updated sections 3.3, 3.6, 5.1.2, 6.4.5, 7.2.1, 8.3, and A.5 for patch 18.  - Updated obsolete information in sections 1.4 and 7.2.3                                                                                                                                                                                                                                                                               |
| 12 Dec 2005            | Patch 57 updates (rev 17) -  REDACTED  .  - General typo corrections and formatting cleanup throughout document. - Removed old operating system references throughout document - Corrected/updated outdated content in sections 3.1, 3.6, 6.1.1, 6.3, 7.2.1, 8.2, 8.7, 9.5.4.4, and  12.5.2.1  -  Removed outdated content from sections: 1.5.3, 3.3, 3.4, 5.2.1, 5.3.2, 5.5, 6.4.4.4.2, 6.4.5, 7.4,  9.5.4.4, 13.1.2, and A.3  - Incorporated p45 change page: new chapter 18 - New section 3.10 covering Microsoft patch installation. |
| 5 April 2005           | Additional Updates (rev 16):  - Section 6.1.1 Checksums                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 28 Mar 2005            | Additional Updates (rev 15):  - Sections 6.4.1, 7.2.4, 10.2.3.1, 10.2.3.3, and 11.1.2, 16.1.2                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 9 Mar 2005             | Patch 48 Updates (rev 14):  -  Sections 3.6 Security Keys, 6.1.1 Checksums, 6.4.1 Clinical Workstation Files, 6.4.2 Background  Processor Files, 7.2.4 Further Information, 10.2.3.1 Input Array Sent to Import API, 10.2.3.3 Results Array Returned to Status Handler, 11.1.2 Delete Images and Pointers                                                                                                                                                                                                                                |
| 30 Sept 2004           | Patch 8 Updates (rev 13):  - Section 3.3 Site Parameters - Section 3.6 Security Keys - Chapter 6 – Section 6.1.1 Routine Descriptions - Section 6.4.1 Clinical Workstation Files - Section 7.2.1 VA FileMan Files - Section 8.2 Imaging System Manager Menu - Section 10.2.3.1 Input Array Sent to Import API - Section 11.3.4 VistA Imaging Display, Demo Mode - Section 11.3.5 VistA Imaging Capture, Test Mode                                                                                                                        |
| 23 June 2004           | Patch 33 Updates (rev 12):  - Section 6.4.1 Clinical Workstation Files - Appendix A.1 Clinical Workstation Error Messages - Appendix A.4 Setup Error Messages                                                                                                                                                                                                                                                                                                                                                                            |
<!-- rpc-table -->
| 30 April 2004          | Patch 11 Updates (rev 11):  - Chapter 6 Routine Descriptions - Section 7.2.1 VA FileMan Files - Section 8.9 Access to DICOM Gateway RPCs - Section 12.2.2 DICOM RPC Broker Calls                                                                                                                                                                                                                                                                                                                                                         |
| 6 April 2004           | Patch 3 Updates (rev 10):  - Revised sections 8.2, 11.1.1, and 12.5.2.1 to reflect the removal of Edit Image Write Location - Removed redundant sections 8.2.1-8.2.1.2 (i.e.,MAG ENTERPRISE information already exists in section 12.5). - Documented revisions for patches 7, 17. 23, 27, 25, 22, and 10.                                                                                                                                                                                                                               |
| 9 Dec 2003             | Patch 10 Updates (rev 9):  - Section 7.2.1 VA FileMan Files                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 5 Nov 2003             | Patch 22 Updates (rev 7):  - Appendix A.6 VistARad Error Messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 30 Sept 2003           | Patch 25 Updates (rev 8):  - Section 7.2.1 VA FileMan Files                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| **Revision History**   |                                                                                                                                                                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 23 July 2003           | Patch 23 Updates (rev 6):  - Section 8.2 Imaging System Manager Menu - Section 12.5 MailMan Messaging Patch 27 Updates: - Section 8.2 Imaging System Manager Menu - Section 12.5 MailMan Messaging                                                  |
| 7 May 2003             | Patch 17 Updates (rev 5):  - Section 7.2.1 VA FileMan Files - Section 7.5 Imaging Entity Relationship Diagram and Detailed Information                                                                                                              |
| 30 April 2003          | Patch 19 Updates (rev 4) to section 8.2 Imaging System Manager Menu                                                                                                                                                                                 |
| 30 Mar 2003            | Patch 16 Updates (rev 3): to Appendix A.5 VistARad Installation Error Messages                                                                                                                                                                      |
| 10 Dec 2002            | Patch 9 Updates (rev 2):  - Addition of files 2006.035, 2006.036, 2006.59, 2006.5906, 2006.596  - Additional fields for file 2005.2 - Additional security key MAGJ DEMAND ROUTE - Modification to table 3.3 (collapse line-items for DICOM Gateway) |
| 6 Sept 2002            | Patch 7 Updates (rev 1):  - Created changes pages for Sections 3.6, and 7.2.1. - Chapter 10 – revised                                                                                                                                               |

**Table of Contents**

### Table of Contents

Preface	3

Table of Contents	1

Chapter 1	Introduction	7

1.1.	Multimedia Patient Record	7

1.2.	VistARad Product Perspective and Features	3

1.3.	Automated DICOM Image Acquisition	3

1.4.	The VistA Imaging DICOM Gateway	4

1.5.	The Hybrid DICOM Image Gateway	4

1.6.	Background Processor	7

1.7.	Typical Configuration	9

1.8.	DICOM Gateway Networking Topology Options	9

1.9.	Cross-Enterprise Image Sharing	10

1.10.	Windows 7 Considerations	11

Chapter 2	Orientation	12

2.1.	Documentation Conventions	12

2.2.	Special Workstation Procedures	12

2.3.	Mouse/Windows Controls	13

Chapter 3	Implementation and Maintenance	16

3.1	VistA Package Requirements	16

3.2	Hardware and Software Requirements	17

3.3	Maintenance of Software on DICOM Gateway Workstations	17

3.4	Changes to IP Addresses or Ports	17

3.5	Security Keys	15

3.6	Workstation Hardware	24

3.7	Changes to DICOM Modalities	24

3.8	Changes to Windows Servers and Security	24

3.9	Microsoft Patch Installation Guidelines	24

3.10	Parameter Definitions	26

Chapter 4	Security Software Maintenance	25

4.1	Security and Anti-virus Considerations	25

Chapter 5	Space, Staffing, and Standard Operating Procedures for VistA Imaging	27

5.1	Infrastructure Resources	27

5.2	Support	29

5.3	Daily Activities	31

5.4	Maintenance	33

5.5	Weekly Activities	33

5.6	Other Periodic Activities	33

5.7	Scheduled Down Time for VistA Servers	34

Chapter 6	Routine Descriptions	35

6.1	VistA Imaging Routines on the VistA Hospital Information System	36

6.2	DICOM Gateway Routines	38

6.3	Non-M Routines Distributed as Executable Files	41

Windows 7 – C:\Program Files (x86)\Vista\Imaging\MAG\_VistARad\Help	71

Chapter 7	VistA Imaging System M Files	75

7.1	Introduction	75

7.2	VA FileMan Files that are Part of the VistA Imaging System	76

7.3	Input Templates	85

7.4	File List	86

7.5	Files Introduced in MAG*3.0*34	88

7.6	Sort and Print Templates	91

7.7	File List	94

7.8	File Security	94

7.9	Global Journaling	83

7.10	VistA System Outages	83

Chapter 8	Exported Options	85

8.1	Introduction: INI File Setup and Configuration of Workstations	85

8.2	Imaging System Manager Menu [MAG SYS MENU]	85

8.3	Configure AE Security Matrix Settings [MAGV AE SEC MX SETTINGS]	88

8.4	Delete Study by Accession Number [MAG SYS-DELETE STUDY]	90

8.5	Enter/Edit Reason [MAG REASON EDIT]	91

8.6	MAG Client Version Report [MAG CLIENT VERSION REPORT]	94

8.7	Imaging VistARad System Options	95

8.8	Imaging MAG WINDOWS Menu Option	95

8.9	Imaging VistARad MAGJ VISTARAD WINDOWS	96

8.10	Imaging DICOM Menu	96

8.11	Imaging Menu Options Documentation	96

8.12	Access to DICOM Gateway RPCs	97

8.13	Imaging Menu Options Documentation	97

Chapter 9	Archiving, Purging, Verifying, and Backup	99

9.1	Introduction	99

9.2	Archiving and Purging of Image FileMan Entries	99

9.3	Archiving and Purging of Image Files	99

9.4	Queue Management	100

9.5	Background Processor Configuration Tools	106

9.6	Background Processor Image and File Entry Verifier	131

9.7	Imaging Server and Jukebox Backup Information	132

9.8	DICOM-related Backup and Purge	132

9.9	VIX-related Backups	138

Chapter 10	Callable Routines/Application Programmer Interfaces (APIs)	140

10.1	Import API	140

10.1.1	VA Policy	140

10.1.2	FDA Policy	141

10.2	VistA Imaging Import API	141

10.2.1	Terms of Use	141

Chapter 11	Error Recovery, Troubleshooting, and Testing	143

11.1	Error Recovery	143

11.2	Troubleshooting / Error Messages	145

11.3	Test Software Available for Troubleshooting	146

11.4	Handling Processing and Storage Errors in the New Data Structures	147

Chapter 12	External Relations	152

12.1	HL7 Messages	152

12.2	HL7 Application Parameters	152

12.3	HL7 Logical Link	152

12.4	Imaging Broker Calls	153

12.5	Windows Messaging	153

12.6	Integration Agreements	153

12.7	Select the Context Management	154

12.8	CPRS Tools Menu Option for VistARad	157

12.9	Mailman Messaging	157

12.10	Imaging Site Reports	174

12.11	VistA Site Service	185

12.12	VistARad External Relations	185

Chapter 13	Internal Relations	187

13.1	Dependencies	187

13.2	VistARad Internal Relations	195

Chapter 14	Package-Wide Variables	179

Chapter 15	Online Documentation	181

15.1	Online Help	181

Chapter 16	Site-Specific Implementation	183

16.1	Site-Specific Implementation	183

Chapter 17	Database Integrity Checking	185

17.1	VistA Imaging MAG SYS MENU	185

17.2	Clinical Display Application	185

17.3	VistARad Application	186

17.4	Verifier Application in the Background Processor	186

Chapter 18	Remote Image Views	187

18.1	Configuration for Remote Image Views	187

Chapter 19	Two-Facto Authentication (2FA)	189

19.1	Two-Factor Authentication (2FA) Overview	189

19.2	Implementation History	190

Appendix A Error Messages	191

A.1	Clinical Workstation Error Messages	191

A.2	Troubleshooting General Startup Network Connection	196

A.3	Runtime	202

A.4	DICOM Gateway Error Messages	246

A.5	Clinical Display/Capture Setup Error Messages	247

A.6	VistARad Error Messages	247

Appendix B: Means Tests	235

B.1	Sending Means Tests to the HEC	235

Glossary	238

Index	242

A		242

B		242

C		242

D		242

F		243

G		243

H		243

I		243

J		244

K		244

L		244

M		244

N		245

O		245

P		245

Q		246

R		246

S		246

T		246

U		246

V		246

W		246

### Chapter 1	Introduction

#### 1 Multimedia Patient Record

The VistA Imaging System is an extension to the V eterans Health Information S ystem T echnology A rchitecture (VistA) hospital information system that captures clinical images, scanned documents, motion images, and other non-textual data files and makes them part of the patient's electronic medical record. Electrocardiogram (EKG) waveforms can be displayed as part of the electronic medical record. Image and text data are provided in an integrated manner that facilitates the clinician's task of correlating the data and making patient care decisions in a timely, accurate way.

The system is designed to provide the treating physician with a complete view of patient data and, at the same time, allow consulting physicians to have access to the image and text data. It serves as a tool to aid communication and consultation among physicians -- whether in the same department, in different medical services, or at different sites.

The VistA Imaging System is unique in that management of the medical images is handled by the hospital information system, allowing very close integration of multimedia data with traditional patient chart information.

Clinical users can capture images during procedures or images can be added at a later time, for example during the creation of a report or progress note. Automatic image acquisition can be performed by DICOM gateways. Images can be acquired from commercial radiology Picture Archiving and Communications Systems (PACS) or directly from radiology devices. The transfer of patient demographic and order information to the commercial PACS or radiology device plays a key role in the ability to add these images to the patient’s online medical record.

VistA Imaging workstations located throughout the hospital capture and display a wide variety of medical images including:

- Cardiology
- Endoscopy (GI, pulmonary, cystoscopy, arthroscopy, bronchoscopy, etc.)
- Ultrasound (vascular, echo cardiology)
- Microscopic (Surgical Pathology, Cytology, Autopsy, Hematology)
- Surgery
- Ophthalmology
- Dental
- Dermatology
- Radiology images
- Nursing
- Podiatry
- Scanned advanced directives, consent forms, and other documents

VistA Imaging VistARad diagnostic workstations are generally located in the Radiology Reading room and are used for softcopy reading of Radiology images. These workstations provide functions for the Radiologist to retrieve and display full-resolution images, associated Radiology reports, and update the Radiology exam status.

#### 2 VistARad Product Perspective and Features

VistARad is a VistA Imaging software component that provides filmless radiology functionality for radiologists and non-radiology clinicians. This maintenance patch (Maintenance VII) addresses various user needs including routine maintenance items, as well as two items described in this document that affect low-level design of certain features already implemented. In addition, support for patient context management is added to the design to eliminate potential safety concerns for those clinicians that require access to VistARad functionality and concurrent use of the VA Computerized Patient Record System (CPRS) and other CCOW-enabled applications.

The following product features and/or design modifications are included in Patch 120 and described in this document:

- Patch 120 provides support for the Windows 7™ operating system. The client installation file included with this patch will execute on either Windows XP™ or Windows 7. Certain installation details differ according to the target installation environment. These differences are noted elsewhere in this document.

**Note** : Some legacy display adapters for high-resolution screens may no longer be supported under Windows 7.

- Changes to the dictation system integration feature reduce potential mismatches between displayed exams and the accession number provided to the dictation system under certain usage scenarios.
- An added feature to the Teaching File interface allows the user to remove Personally Identifiable Information (PII) from images that have PII burned into the image pixel data. Previously, such “burned in” data could not be removed from images used for teaching purposes, raising a patient confidentiality issue. See the *VistARad User Guide* , **Teaching Files** .
- Patient Context Management Support is discussed. See section 0 **.**
#### 3 Automated DICOM Image Acquisition

**DICOM** is the abbreviation for the **D** igital **I** maging and **CO** mmunications in **M** edicine standard. DICOM brings open systems technology to the medical imaging marketplace and enables VistA to communicate directly with commercial medical imaging equipment.

DICOM is a set of networked client/server applications that are implemented on top of TCP/IP. DICOM is part of the VistA networked application suite, along with CPRS, Kernel Broker, MS Exchange, and Windows-based file servers. Similar networking techniques are used for installing and maintaining all of these applications.

#### 4 The VistA Imaging DICOM Gateway

The VistA Imaging DICOM Gateway, referred to as the DICOM Gateway for short, is a suite of VA-developed software that facilitates the transmission of DICOM images between the image acquisition modalities 1 and the equipment on which these images are permanently stored. The images and information about them are stored in the VistA database as a part of the patient record. Once images have been stored in the system, they are available for viewing from any VistA clinical or diagnostic workstation.

The VistA Imaging DICOM Gateway can have these functions, depending on its configuration:

- Text Gateway  A gateway that distributes event data from the VistA Hospital Information System to image acquisition modalities and Picture Archiving and Communication Systems (PACS). For more information, see the *VistA Imaging DICOM Gateway User Guide* .
- Image Gateway  A gateway that transfers image files from an acquisition modality or a commercial PACS to VistA, or from VistA to workstations or commercial PACS. For more information, see the *VistA Imaging DICOM Gateway User Guide* .
- Routing Gateway  A gateway that transmits studies acquired at one VistA site to a storage location at another VistA site. For more information, see the *VistA Imaging DICOM Gateway Routing Setup and User Guide* .
#### 5 The Hybrid DICOM Image Gateway

The Hybrid DICOM Image Gateway (HDIG) is a component of the DICOM Image Gateway, introduced in MAG*3.0*34 to enable the storage of the SOP classes for which support was introduced in MAG*3.0*34.

Figure 1: Hybrid DICOM Image Gateway

<!-- image -->

Note: The term “modality” is from the DICOM standard and denotes any equipment that produces images.

The HDIG includes these components:

- **DICOM Listener** . The DICOM Listener listens on a specific port for incoming DICOM objects from DICOM devices (Application Entities, or AEs) that are pre-defined in the DICOM AE SECURITY MATRIX. It validates all Service Object Pair (SOP) classes for which support was introduced in MAG*3.0*34 and stores the DICOM objects that pass the various validation checks in the new database structures. It forwards the SOP classes that were supported before MAG*3.0*34 for storage in the old database structures. The DICOM Listener includes:
- The server side of the Query/Retrieve application (Query/Retrieve for short). Query/Retrieve is an application that allows pre-defined application entities to query the VistA database. For more information about Query/Retrieve, see the *VistA Imaging DICOM Gateway User Manual* .
- The server side of the DICOM Importer II. The DICOM Importer II application provides the ability to import studies acquired at external facilities into the VistA database. It also provides a user-friendly graphical user interface for using DICOM Correct to correct errors in the processing flow. For more information about the DICOM Importer II, see the *DICOM Importer II User Manual* .
- **Archiver** . The Archiver archives the SOP classes for which support was introduced in MAG*3.0*34.
- **New Abstract Maker** . The new Abstract Maker creates abstracts (thumbnail icons) for the SOP classes for which support was introduced in MAG*3.0*34.

The following figure shows the HDIG components. You can select all components during installation, except the server side of the Query/Retrieve application (implemented in MAG*3.0*116) and the server side of the DICOM Importer II application (implemented in MAG*3.0*118), which are installed with the DICOM Listener.

<!-- image -->

Figure 2: HIG components diagram

For more information about installing the HDIG and its components, see the *VistA Imaging DICOM Gateway Installation Guide* .

From Patch 204 onward, the HDIG application will only run on 64-bit operating systems (Windows 2008 64-bit, Windows 2012, etc.) This software has not been tested on Windows 2016.

#### 6 Background Processor

The VistA Imaging Background Processor is a component in the VistA Imaging System and runs on a Windows file server. The Background Processor ensures the archiving of DICOM and clinical images from short-term storage (RAID groups) onto Tier 2 for long-term storage. These images are stored indefinitely on the archive device.

##### Queue Processor

The Queue Processor moves image data between Tier 1 and either remote or local Tier 2 storage. This activity is in response to activity from Capture and Display application requests.

##### Purge

The Purge removes image files from the Tier 1 based on file dates. An automatic purge process can be configured when Tier 1 storage becomes low and a regularly scheduled purge can be configured to operate during off-peak hours.

##### Verifier

The Verifier maintains and checks data integrity between the VistA Imaging database and the storage network location.

#### 7 Typical Configuration

The diagram below shows a typical configuration of a VistA Imaging system.

Figure 3: VistA Imaging Network Topology

<!-- image -->

#### 8 DICOM Gateway Networking Topology Options

The VistA DICOM Gateways may use either one or two networking interfaces depending upon whether the commercial DICOM devices are directly connected to the main network backbone or are located on separate physical networks.

##### Commercial DICOM Devices Connected to Main Network Backbone

Some sites may choose to have all devices (workstations, main hospital computer, DICOM imaging producing equipment, etc.) connected to a single high-speed switched network backbone. In this case, the VistA Image Servers, VistA DICOM Gateways, and Background Processor will all connect to the same switch on the high-speed backbone. Clinical and capture workstations will be connected to segments that feed into the backbone.

Figure 4: Single High-Speed Switched Network

<!-- image -->

##### Commercial DICOM Devices on Separate Physical Networks

Other sites may choose to have a separate dedicated network for the commercial DICOM devices and DICOM gateways. In this case, the VistA DICOM Gateway must have two network interfaces, one to connect to the main hospital network backbone, and the second to connect to the dedicated network for the commercial DICOM devices. This keeps the traffic on the two networks separate.

Figure 5: Separate Dedicated DICOM Network

<!-- image -->

#### 9 Cross-Enterprise Image Sharing

Sites that implement the VistA Imaging Exchange (VIX) service get:

- More efficient access to all types of remotely stored images and image-like artifacts (such as scanned documents) from other VA sites that also have a VIX.
- Remote radiology worklist monitoring and access to remotely stored radiology exams, using VistARad, without the need for routing.
- Access to DoD images for shared VA/DoD patients.
- For more information about the VIX, see the *VistA Imaging VIX Administrator’s Guide* . Sites that implement the Advanced Web Image Viewer (AWIV) get:
- The ability for users to view images, progress notes, radiology reports, and other artifacts from within VistAWeb.
- User access to images from any VA site via the Centralized VistA Imaging Exchange (CVIX) service, which is an extension of the VIX service.

For information about using the AWIV, see the *VistA Imaging AWIV User Manual* . Sites that implement the Advanced Web Image Viewer (AWIV) Web Application get:

- The ability for users to access images using the AWIV through Microsoft Internet Explorer.
- User access to all patient images from all sites at which a patient has been seen, not just the images associated with progress notes or radiology reports.
- User access to DoD artifacts, radiology images, and NCAT reports.

**NOTE** : The NCAT system must be online and available in order for AWIV users to view NCAT reports.

- User access to images via the AWIV using a thin client.

For information about using the AWIV WA, see the *VistA Imaging AWIV Web Application User Guide* .

#### 10 Windows 7 Considerations

VistARad runs successfully under Windows 7. The documentation will point out any differences when necessary, using notes such as the following:

**Note:** Restrictions on access to root directories (including C:\) mean that ordinary users cannot create files in the root directory C:\.

Some “system” file pathnames (including those for the VistARad application itself) are different on Windows 7 systems. See section 6.3.1 for details.

### Chapter 2	Orientation

#### 11 Documentation Conventions

The following conventions are used in this manual.

| **Convention**   | **Description**                                                                                                                                                                                                                                                               |                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Regular Type     | System-generated menu, dialog, output, etc. (in VistA screenprints)                                                                                                                                                                                                           | System-generated menu, dialog, output, etc. (in VistA screenprints)                                                                                 |
| Bold Type        | User Keyboard Entry (in VistA screenprints)                                                                                                                                                                                                                                   | User Keyboard Entry (in VistA screenprints)                                                                                                         |
| [XTSUMBLD- CHECK | Routines, VistA Menu options                                                                                                                                                                                                                                                  | Routines, VistA Menu options                                                                                                                        |
| <Enter>          | <!-- image -->                                                                                                                                                                                                                                                                | Enter (Return) key                                                                                                                                  |
| <Shift>          | <!-- image -->                                                                                                                                                                                                                                                                | Shift key                                                                                                                                           |
| <A>, <2>, <F2>   | Alpha, numeric or function key                                                                                                                                                                                                                                                | Alpha, numeric or function key                                                                                                                      |
| <Esc>            | <!-- image -->                                                                                                                                                                                                                                                                | Escape key                                                                                                                                          |
| <Num Lock>       | <!-- image -->                                                                                                                                                                                                                                                                | Top left key on the numeric keypad (above the 7); may also be labeled <Numeric Lock>. It is equivalent to the <Caps Lock> used for alphabetic keys. |
| <Num Lock>       | If &lt;Num Lock&gt; is on, the keypad key will produce the number shown on its surface.  If &lt;Num Lock&gt; is off, the keypad key moves the cursor as indicated by the label or symbol on the key; for example, the keypad &lt;6&gt; key will move the cursor to the right. |                                                                                                                                                     |

#### 12 Special Workstation Procedures

| **Command**   | **Action**                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reboot        | - Push the RESET button on the front of the workstation. - If there is no RESET button, power the workstation off and then on; the workstation will reboot. - The workstation will perform a virus check and load all required software; this takes about 30-60 seconds. - When the reboot process is complete, you should be able to sign back into the workstation. #### 13 Mouse/Windows Controls |

| **Control**        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mouse button click | - The mouse is a device used to point at positions on the screen. - The mouse may have one, two, or three buttons. - The mouse should be held at the end opposite the cord so the fingers can press the buttons. - The buttons are referred to as the "Right Mouse Button," the "Left Mouse Button", and the "Center Mouse Button." One kind of mouse, known as a “wheel mouse,” has a wheel in the center instead of a button. The wheel is normally used for scrolling up and or left to right on a screen. When the mouse is rolled around on a flat surface, the arrow cursor on the screen will move correspondingly. - Pressing and releasing a button is called "clicking". You may position the arrow over a portion of the window, such as a button or scroll bar, and then click. This will cause the computer to do something such as display an image, depending on the window. - When the instructions tell you to “press the mouse button,” you can assume that you are to press the left mouse button. - When it’s necessary to use the right mouse button, you will be told to “right click.” This is used, for example, to select items from a drop-down list or menu. |
| Select             | - You may also select a rectangular area on the window, by following these steps: - Position the arrow cursor so it is over the left upper corner of the area to be selected. - Press the left mouse button down and hold it down while you move the mouse to the right lower corner of the rectangle to be selected. - Release the mouse button. You will see a dotted rectangle on the window around the area selected. ### Chapter 3	Implementation and Maintenance #### 14 VistA Package Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Drag               | - If you want to move a window to another area of the window (e.g., to see something on a window that is underneath), follow these steps: - Position the cursor over the top colored title area of the window to be moved. - Press the left mouse button down, hold the mouse button down, and move the mouse until the window is where you want it. - Release the left mouse button.  - This is called "clicking and dragging" a window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <!-- image -->     | - You may adjust the size of the window by following these steps: - Place your mouse at the edge of the window that you would like to move. - When you see the cursor turn into a double headed arrow (), hold the left mouse button down, and move the mouse until the image is the width and/or height that you would like. Chapter 2 - Orientation This page is intentionally left blank.  <!-- image -->  - Release the left mouse button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

The VistA Imaging System is designed to be used in conjunction with the following VistA packages: Kernel, FileMan and RPC Broker are required packages; other packages depend on the site’s implementation requirements.

##### Packages Used in Conjunction with VistARad

The VistA Imaging System is designed to be used in conjunction with the following VistA packages. Kernel, FileMan and RPC Broker are required packages. Other packages will depend on the site’s implementation requirements.

| **Package Name and Version**    | **Required For**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kernel V. 8.0                   | Kernel is a vendor-independent applications development environment, as well as a run-time environment providing standard vendor-independent services to applications software. It is not an operating system, but a set of utilities and associated files that are executed in an M environment.                                                                                                                                                                                                                                                                                         |
| FileMan V. 22                   | VA FileMan creates and maintains a database management system that includes features such as:  - A report writer - A data dictionary manager - Scrolling and screen-oriented data entry - Text editors - Programming utilities - Tools for sending data to other systems - File archiving  VA FileMan can be used as a standalone database, as a set of interactive or "silent" routines, or as a set of application utilities; in all modes, it is used to define, enter, and retrieve information from a set of computer-stored files, each of which is described by a data dictionary. |
<!-- rpc-table -->
| RPC Broker 1.1                  | Interfacing with the hospital database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Consult/Request Tracking V. 3.0 | Capturing images to the Consult/Request Tracking package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Medicine V. 2.3                 | Capturing images to the Medicine package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Laboratory V. 5.2               | Capturing images to the Laboratory package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Radiology V. 5.0                | Capturing images to the Radiology package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Surgery V. 3.0                  | Capturing images to the Surgery package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| TIU V. 1.0                      | Capturing images to the Text Integration Utility package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PIMS V 5.3                      | Displaying Patient Profile report and patient security lookup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Health Summary 2.7              | Displaying Health Summary report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

#### 15 Hardware and Software Requirements

Contact your Implementation Manager for information about VistA Imaging equipment.

The VistA Imaging software requires that a network be present with sufficient capacity to transport image files in a reasonable amount of time. All network set-ups must be completed **before** VistA Imaging workstations can be installed.

#### 16 Maintenance of Software on DICOM Gateway Workstations

*This section is obsolete as of the release of Patch 11. Refer to the Imaging DICOM Gateway Installation Guide for information about software installation and maintenance.*

#### 17 Changes to IP Addresses or Ports

Any changes to the IP addresses for the VistA servers or changes to the Kernel RPC Broker Listening port(s) will require updating on the VistA Imaging workstations (refer to the Broker Technical and User Manuals).

The VistA Site Service will also need to be updated with the changes. (If the site service is not updated, remote VA sites will not be able to access locally stored images.) For information about the VistA Site Service, see section 12.11.

Sites that have implemented a VIX will need to update their VIX’s configuration to use the new site service values. This is done by re-running the VIX installer. Contact REDACTED for guidance.

Sites that have implemented a VIX will also need to update their VIX’s configuration after the site service has been updated. This is done by re-running the VIX Installation wizard which will detect the new connection information and reconfigure the VIX accordingly. See the *VIX Installation Guide* for more information.

#### 18 Security Keys

There are a number of security keys associated with the VistA Imaging system. The following tables summarize security keys and their function.

##### General Security Keys

**Note:** Please be cautious when assigning the following keys; the keys are intended for Imaging Support personnel. Review the descriptions before assigning these keys.

| **General Security Keys**   |                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAG ANNOTATE MGR            | This key gives the holder full annotation access at the local site. The holder can add, edit, and delete annotations.  Permissions provided by this key apply only to images at the site where the user has the key. This key also allows users to create annotations regardless of the settings of the user’s account in the PARAMETER DEFINITION (MAG IMAGE ALLOW ANNOTATE) specified at a given site. |
| MAGDFIX ALL                 | Allows the holder to perform DICOM CORRECT functions on any entry in the DICOM FAILED IMAGES file (#2006.575). Users who do not hold this key will only be able to correct entries that were captured on their own site's gateway.                                                                                                                                                                       |
| MAG DELETE                  | This key allows the holder to delete images from the IMAGE file (#2005) and from the new data structures. Pointers in parent packages such as Medicine, Surgery, Lab, Radiology, and TIU will also be deleted for images in file (#2005).                                                                                                                                                                |
| MAG PREFETCH                | This key allows a user to 'PreFetch' or Queue all images for a patient. This means that all images for a patient that are on the jukebox will be copied from the jukebox to the magnetic server cache.                                                                                                                                                                                                   |
| MAG SYSTEM                  | Given to person(s) managing VistA Imaging Systems. Required to modify site parameters via the Background Processor or to modify workstation parameters via the MAGSYS application. Also enables the display of DICOM header data for radiology images on Clinical Display workstations.                                                                                                                  |
| MAG VIX ADMIN               | This key grants access to the VIX transaction log and to update HDIG administration parameters (HDIG service accounts access/verify code and email addresses). This key should be assigned to VIX administrators, to the DICOM service account, and the Imaging System Manager account. For more information, see the  *VIX Administrator’s Guide*  .                                                    |

##### Security Keys for Clinical Display

The following keys are used for display of images and should be limited to appropriate personnel:

| **Display-related Security Keys**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAG RAD SETTINGS                    | User can edit the CT Presets in the Clinical Imaging Display Radiology Viewer window.                                                                                                                                                                                                                                                                                                                                                                                                           |
| MAG ROI                             | User can print, copy images, or make release of information (ROI) requests without having to enter an electronic signature. This key should be assigned only to the HIMS Release of Information Officer.                                                                                                                                                                                                                                                                                        |
| MAGDISP ADMIN                       | User can display administrative images/documents.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MAGDISP CLIN                        | User can display clinical images/documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MAG EDIT                            | The MAG EDIT key is used to correct an image field when an index field is incorrect or incomplete, such as correcting a wrong specialty that was selected. Only users assigned the MAG EDIT key can edit an image. The MAG EDIT key is also required to access the QA Review Utility when performing quality assurance reviews of the scanned images. Only the Chief, HIM or authorized designated personnel e.g., VistA Imaging Coordinator, Scanning Supervisor) should be assigned this key. |
| MAG PAT PHOTO ONLY                  | User can view only the patient photo.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MAG QA REVIEW                       | User can access QA Review and QA Review Report from Clinical Display Utilities Menu.                                                                                                                                                                                                                                                                                                                                                                                                            |
| MAG REVIEW NCAT                     | User can view NCAT reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MAG VIEW DOD IMAGES                 | In Patch 72 and 93 versions of Clinical Display, users must have this key to display DoD images.  In newer versions of Clinical Display, this key is not checked.                                                                                                                                                                                                                                                                                                                               |

##### Security Keys for Clinical Capture

**Note:** If the ‘CAPTURE KEYS’ site parameter has been initialized, the following keys will need to be assigned appropriately.

| **Capture-related Security Keys**   |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| MAG CAPTURE                         | Allow capture of images without an associated specialty (i.e. 'NONE' on the Imaging Capture configuration window). |
| MAG NOTE EFILE                      | User can electronically file notes without an electronic signature from the Imaging Capture workstation.           |
| MAGCAP ADMIN                        | Allow capture of images associated with the ‘Admin Document’ specialty.                                            |
| MAGCAP CP                           | Allow capture of Clinical Procedure images.                                                                        |
| MAGCAP LAB                          | User can capture Laboratory images from the Imaging Capture workstation.                                           |
| MAGCAP MED C                        | User can capture Cardiology images from the Imaging Capture workstation.                                           |
| MAGCAP MED G                        | User can capture GI images from the Imaging Capture workstation.                                                   |
| MAGCAP MED GEN                      | User can capture Generic Medicine images from the Imaging Capture workstation.                                     |
| MAGCAP MED H                        | User can capture Hematology images from the Imaging Capture workstation.                                           |
| MAGCAP MED HI                       | User can capture Internal Medicine / Hematology images from the Imaging Capture workstation.                       |
| MAGCAP MED I                        | User can capture Internal Medicine images from the Imaging Capture workstation.                                    |
| MAGCAP MED N                        | User can capture Neurology images from the Imaging Capture workstation.                                            |
| MAGCAP MED P                        | User can capture Pulmonary / Endoscopy images from the Imaging Capture workstation.                                |
| MAGCAP MED PF                       | User can capture Pulmonary Function Test images from the Imaging Capture workstation.                              |
| MAGCAP MED R                        | User can capture Rheumatology images from the Imaging Capture workstation.                                         |
| MAGCAP MED Z                        | User can capture Consult images from the Imaging Capture workstation.                                              |
| MAGCAP PHOTOID                      | User can capture Photo ID images from the Imaging Capture workstation.                                             |
| MAGCAP RAD                          | User can capture Radiology images from the Imaging Capture workstation.                                            |
| MAGCAP SUR                          | User can capture Surgery images from the Imaging Capture workstation.                                              |
| MAGCAP TIU                          | User can capture TIU images from the Imaging Capture workstation.                                                  |
| MAGCAP TRC                          | User can capture images associated with a "TeleReader Consult" from the Imaging Capture workstation.               |

##### Security Keys for VistARad

The following keys are related to VistARad and should be limited to appropriate personnel:

| **VistARad-related Security Keys**   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAGJ DEMAND ROUTE                    | User can access VistARad’s on-demand routing capability. On- demand routing can be used to manually send exams to remote sites. For more information, refer to the  *VistA Imaging Routing User Guide*  .                                                                                                                                                                                                                                     |
| MAGJ DEMAND ROUTE DICOM              | Allows the user to use the on-demand routing function to queue exam images to be routed to selected remote DICOM destinations. This function only works for sites that have been configured for routing of images. An updated Routing agreement needs to be submitted and approved by the VistA Imaging Group before this function can be used.                                                                                               |
| MAGJ OVERRIDE ANNOTATIONS            | Grants to a radiologist user of VistARad access to the menu option ‘Override Annotations’ when viewing an exam whose status is ‘Complete.’ This functionality is detailed in the  *VistARad User Guide*  .                                                                                                                                                                                                                                    |
| MAGJ REMOTE ACCESS CONTROL           | Allows a VistARad user to access the Monitored Sites configuration subset of the VIX Configuration settings tab, and to view exam list data in the Monitored Sites tab of the Manager.                                                                                                                                                                                                                                                        |
| MAGJ SEE BAD IMAGES                  | User can view images in VistARad that are associated with an exam that has failed the “Patient Safety” database checks.                                                                                                                                                                                                                                                                                                                       |
| MAGJ STORE IMAGES                    | Allows VistARad users to save Voxar images as secondary captures to VistA.                                                                                                                                                                                                                                                                                                                                                                    |
| MAGJ SYSTEM MANAGER                  | Allows access to Voxar-related settings in the VistARad Settings dialog. Grants access to additional data in the Imaging Internal Data display window. This functionality is detailed in the VistARad User Guide and Imaging System Installation Guide.  Should only be assigned to VistARad administrators. Assigned only to VistARad administrators. Grants access to the Local Site VIX configuration subset of the VIX Configuration tab. |
| MAGJ SYSTEM USER                     | Allows a user to create and delete site-level hanging protocols, templates, and image presets associated with the VistARad ‘sysAdmin’ user.                                                                                                                                                                                                                                                                                                   |
| MAGJ VOXAR COPYIMAGE                 | Allows VistARad users to copy images using Voxar (Enables the  **Copy to Clipboard**  button in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                                                                         |
| MAGJ VOXAR EXPORTCAPTURE             | Allows VistARad users to export images using Voxar (Enables the three  **Export**  -related buttons in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                                                                  |
| MAGJ VOXAR PRINTCOMPOSER             | Allows VistARad users to print images using Voxar (Enables the  **Print Composer**  button in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                                                                           |

##### Security Keys for AWIV Web Application

Users at the medical centers are allowed to view images based on their levels of access and/or user rights. Users must have at least one of the following keys to access images using the AWIV Web Application.

| **AWIV-Related Security Keys**   |                                                                                                                              |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| MAG REVIEW NCAT                  | User can view NCAT reports.                                                                                                  |
| MAGDISP ADMIN                    | User can display administrative images/documents.                                                                            |
| MAGDISP CLIN                     | User can display clinical images/documents.                                                                                  |
| MAG PAT PHOTO ONLY               | User can view only the patient photo.                                                                                        |
| MAG ROI                          | User can print or copy images without entering an electronic signature; granted only to HIMS Release of Information officer. |

**NOTE** : The NCAT system must be online and available in order for AWIV users to view NCAT reports.

Veterans Benefit Administration (VBA) users can view images without security keys, with the exception of NCAT reports.

##### Security Keys for the DICOM Importer II

The following keys are related to the DICOM Importer II and should be limited to appropriate personnel:

| **Security Keys for the DICOM Importer II**   |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAGV IMPORT MEDIA STAGER                      | Allows DICOM Importer II users to stage (copy) from media to staging persistent storage, where it waits for reconciliation processing.                                                                                                                                                                                                                                                                                                 |
| MAGV IMPORT STAGE MEDIA ADV                   | Allows DICOM Importer II users to:  - Stage (copy) study level artifacts from media to staging persistent storage and - View images on the media.                                                                                                                                                                                                                                                                                      |
| MAGV IMPORT RECON CONTRACT                    | Allows DICOM Importer II users to:  - Stage media at the study level - View images on the media - Associate study DICOM objects with an existing Radiology or Consult order for reconciliation.                                                                                                                                                                                                                                        |
| MAGV IMPORT RECON ARTIFACT                    | Allows DICOM Importer II users to:  - Stage media at the study level - View images on the media - Associate study DICOM objects with an existing Radiology or Consult order for reconciliation. - Place new Radiology orders using the Importer II user interface. - Use DICOM Correct to fix errors in studies in the DICOM Correct queue. - Manage the DICOM Importer II queue - Run, view, print and save DICOM Importer II reports |
| MAGV IMPORT REPORTS                           | Allows DICOM Importer II users to view, print, and save reports to a text file.                                                                                                                                                                                                                                                                                                                                                        |

#### 19 Workstation Hardware

Workstations tend to collect dust inside of the chassis. They should be periodically opened and cleaned. The accumulation of dust can lead to heat damage of workstation components. Only a qualified individual should do further hardware maintenance.

The monitors used with the VistARad diagnostic workstations require periodic calibration to maintain the proper grayscale luminance display characteristics necessary for accurate image quality. A program of maintenance for these monitors should be established and administered by the Biomedical Engineering staff. A calibration/maintenance log should be kept, as such documentation may be required for review by regulatory bodies.

#### 20 Changes to DICOM Modalities

When DICOM Modalities are added, or operational parameters are to be modified, see the *VistA Imaging DICOM Gateway User Manual* for the procedures to record the appropriate new values for the various parameters.

#### 21 Changes to Windows Servers and Security

Any changes to Image server shares or server security require updates to VistA files. See the

*VistA Imaging System Installation Guide* for details.

#### 22 Microsoft Patch Installation Guidelines

Sites should use the following guidelines for installing Microsoft patches on VistA Imaging Clinical workstations, DICOM gateways, VistARad workstations, DICOM Importer II workstations, and Imaging file servers.

The nature of the Microsoft patch dictates if it should be installed immediately, after validation, or not at all. For any patch that is installed, use steps detailed in “Procedures for Updates” below.

- **Critical security updates -** Install immediately after they are released from Microsoft.
- **Service Packs** - VistA Imaging will verify with solution vendors that there are no known issues and then will field test the service packs at 4 test sites with monitoring. The field test will last approximately 2 weeks. If no issues arise, all sites will be instructed to install the service pack.
- **Internet Explorer major version upgrades** – Are to be handled the same as service pack updates.

**Note:** IE-related critical security updates should be installed immediately after they are released from Microsoft.

- **Minor software updates** (media player, etc.) – Do not install unless validated by the VistA Imaging team.

###### Procedure for updates (critical components)

All updates should be applied methodically to critical Imaging components (file servers, gateways, VistARad Workstations).

1. Ensure that all VistA Imaging components are working properly before installing any updates.
2. Ensure that service packs, non-critical Internet Explorer upgrades, and minor software updates are validated by VistA Imaging (see above).
3. Schedule the installation for a time when system usage is low (in case a reboot is required).
4. Apply each update one at a time.
5. Apply each update to one critical system. Monitor that system for at least 1 day before updating other systems.
6. Do not load updates on all critical systems without first testing on a single system of each type.
7. Report any problems to the National Help Desk immediately.

###### Notes for Clinical Workstations

For clinical (non-diagnostic) workstations, the following is recommended:

- Microsoft patches should be loaded one at a time, and onto a single workstation only.
- After verifying that the workstation works properly, and that no unexpected issues arise, the patch can be installed on all workstations.

Any problems should be reported to the National Help Desk.

#### 23 Parameter Definitions

MAG TR ALLOW THIN CLIENT

Sites will be able to configure whether or not TeleReader will be able to access and read images on a workstation that accesses VistA Imaging through a Thin Client.

MAG IMAGE ALLOW ANNOTATE

This parameter definition controls the ability of users at a specific site to create annotations based on the following hierarchical levels:

- User
- Service
- Division
- System

The VistA administrator or Information Resources Management (IRM) personnel can allow users to create annotations by changing the value of the parameter MAG IMAGE ALLOW ANNOTATE for an individual user account, for the users of a specific service at the site, for the user accounts that are part of a division, or for the entire site.

Authorized users can access the MAG IMAGE ALLOW ANNOTATE parameter through the VistA menu option [XPAR EDIT PARAMETER].

This page is intentionally left blank.

### Chapter 4	Security Software Maintenance

#### 24 Security and Anti-virus Considerations

VistA workstations are multi-purpose, multi-function medical systems. These workstations usually enable the users to run all of the VA’s application software (including VistA Imaging), the Microsoft Office Suite, e-mail, Internet and other commercial products, as needed by the hospital staff. The workstations should be configured to provide medical information security (as specified by the VA’s security staff), and they must have the latest version of anti-virus software protecting them.

Additionally, if these workstations will be used to stage or import images from media (CD/DVDs), the media drives must be enabled. Ensure that the anti-virus software is configured to scan all files being staged, imported or copied from media.

Windows security features should be used to restrict user access and protect system and other areas that should not be accessed by users. For additional information, see the *VistA Imaging Installation Guide* and the *VistA Imaging DICOM Gateway Installation Manual* .

VistARad Diagnostic workstations must be excluded from automatic software update/inventory tracking packages, and any client software supporting these cannot be installed. For information about removing System Center Configuration Manager (SCCM), please review the *VistA Imaging Installation Guide* .

This page is intentionally left blank.

### Chapter 5	Space, Staffing, and Standard Operating Procedures for VistA Imaging

#### 25 Infrastructure Resources

##### Networking

VistA Imaging Clinical Workstations run best with at least a 100 mb/s network, however they can be run over a 10 mb/s network.

The Background Processor (BP) application operates on a Windows-based PC. It is recommended that it operate on a file server that has a minimum of two gigabytes of RAM.

The VistA Imaging DICOM Gateway requires a hospital network infrastructure having a backbone that will support Ethernet segments with at least 100 megabits per second throughput. It is best to place the servers and Background Processor on the same switch with the gateways. The HDIG runs several services that use several ports to communicate. These ports must be open. It is recommended the HDIG operates on a file server with eight gigabytes of RAM, the minimum is four gigabytes of RAM.

VistA Imaging VistARad workstations should be on their own separate 1Gb/s network connection to the file servers whenever possible. This is especially important when more than two diagnostic workstations are in use in the radiology department. The VistARad workstations can run acceptably on a 100Mb/s network, but speed of image retrieval and display may be compromised.

The VistA Imaging Exchange (VIX) service can be set up on the clustered server used for Imaging shares (recommended) or on a dedicated standalone server. If the VIX is set up on a standalone server, the server should have a 4Gb/s network connection to the Imaging cluster. For more information about the VIX, see the *VistA Imaging VIX Administrator’s Guide* .

##### Space

Each VistA Imaging DICOM Gateway runs on a Windows-based workstation with a monitor having a resolution of 1280x1024 pixels or better. Space is required for the system, its monitor, keyboard and mouse.

The Background Processor runs on a Windows-based file server and requires similar physical space.

The VistARad software runs on a Windows-based workstation using one to four monitors having a resolution sufficient for diagnostic reading. An additional workstation running voice dictation software may be present as well. Allow adequate space for the workstation(s), all monitors, keyboards, pointing devices, and dictation devices. In addition, plan for adequate room cooling and for room lighting that is suitable for diagnostic reading requirements.

##### Power

It is strongly recommended that the power supply to each VistA Imaging server, jukebox, DICOM Gateway, and Background Processor be safeguarded by means of an **U** ninterruptible **P** ower **S** upply (UPS). This will reduce line voltage problems as well as protect against power outages.

##### Remote Access

In order to allow the VistA Imaging Project Support Staff to gain access to the servers and workstations that are running the VistA Imaging, a copy of either PC-Anywhere (preferred) or Remotely Possible (servers) must be installed on each server or workstation. These should be configured as a *host* . These systems should never be hooked up to a modem.

##### Security

Remote access must be password protected. Be sure to keep the VistA Imaging Project Support Staff updated when any such passwords are changed.

#### 26 Support

##### IRM Support Staff Requirements

IRM support for VistA Imaging may require one or more staff members, depending on the size of the installation. These staff members must possess knowledge of VistA, Microsoft Windows, networking, and troubleshooting problems with Windows and TCP/IP. These staff members will need administrator privileges and should have a good foundation in Windows to cover troubleshooting, permissions and set-up. Network support will be needed to troubleshoot and maintain routing, wiring and configurations where packet filtering is in use.

Team members should be comfortable with the following areas:

- *User Manager* for Domains
- Setting permissions
- Shares
- *Server Manager* for setting up shares
- *Event Viewer*
- *Ping* , *TraceRT, NetStat,* and *DICOM\_Echo*
- *TCP/IP troubleshooting techniques*

These staff members will be responsible for supporting Windows-based magnetic and jukebox servers, installing VistA Imaging patches, correcting information in VistA relating to the relationships between patients and images, installing workstations and workstation capture devices, and managing the Background Processor and DICOM gateways. This staff member is responsible for assigning Imaging security keys and menus to the users.

VistA package support staff should cover the installation of Imaging KIDS patches and issues like translation tables and journaling. In addition, a staff member with experience in M should be available to assist in editing global variables and using FileMan to make corrections as necessary to correct situations such as the incorrect assignment of an image to a patient.

##### Biomedical Engineering Support Staff Requirements

Someone experienced in Biomedical Engineering and/or network support will be needed to install and troubleshoot modalities, display and capture workstations, capture devices, network and server systems, and to calibrate diagnostic workstation monitors. The amount of time required for these duties will vary with the size and specifics of the installation.

This staff will be responsible for ensuring that the modalities maintain their connections to the network and are able to communicate with the gateway systems. These staff members should be able to monitor modality traffic and to distribute modality traffic over different gateway processors, depending upon local traffic conditions and circumstances.

##### ADPAC Staff Requirements for Support for All Medical Services

These staff members will need to know how to use, teach, and support the VistA Imaging system. They should have a close relationship with the IRM staff so that problems may be reported and so that they may be of assistance in the resolution of these problems. The ADPACs will need to assist in implementing and customizing the VistA Imaging System for various specialties. They will need to trouble-shoot issues related to how VistA Imaging System fits into the practice of medicine. They will be the first line of support in the use of the VistA Imaging package and will need to assist the end-users. ADPACs should be able to train key users who can then, in turn, train other users on the VistA Imaging System.

The ADPACs will be responsible for being key advocates of the VistA Imaging system. It is essential that the ADPACs be proactive people. They will need to “walk the hospital” in the morning to be sure that users are not having problems. They will need to check on the modalities to ensure that they are working properly. These staff members may also be called upon to assist in correcting image header information, so that images are properly assigned to the right patients. The correcting of image headers is an event that does not happen often but one that may occur when the modality does not have an automatic worklist capability but requires end-user interaction to provide the patient name, social security number, and radiology accession number.

#### 27 Daily Activities

Standard practices should be followed, including doing complete backups prior to installation of any new software or patches. For every processor in the suite of equipment for the VistA Imaging system, documentation should be maintained indicating what versions of which software are running and when new versions or patches are installed. In addition, this documentation should include information on the dates of installation, and who participated in the installation of software, patches or updates, and any unusual occurrences at the time of installation. Records should be kept of any problems that occur at the site, their cause and resolution.

##### IRM Morning Routine

Each morning the standard operating procedure should be to perform the tasks listed below in order to ensure the normal daily operation of the system.Check the Imaging Network

Use Ping and other utilities, such as browsing, to ensure that all servers, gateways and modalities are reachable through the network.

###### Check Tier 2 for Sufficient Platters in the Write Path

Physically check Tier 2 and its console to see which platters are currently loaded. Ensure that there are sufficient disks loaded to cover the day’s operations and that there are new ones available to be used when needed.

###### Check Current Write Locations for Sufficient Disk Space

Check the disk space on the servers and gateways. If images are accumulating on the Image Gateway and are not being passed to the VistA Imaging Servers, check for gateway problems. Correct any header information to associate images with the correct patient and allow the gateway to get the images in question moved to the VistA Imaging Servers.

###### Check the Event Viewer Trap on Imaging Network

Use the *Event Viewer* (under Administrative Tools) to display alerts. These logs may be filtered to show only warnings and alerts. It is a good practice to periodically save these logs to removable media and flush the logs. This will keep disk space usage to a minimum and still allow for old logs to be viewed.

###### Check the Imaging Background Processor

Failed queues can be noted in the Queue Activity window in the BP Queue Processor window. Active and failed queue status, system wide, can be accessed from the menu option: View|Purge Re-queue by type.

Use the Queue Manager on the Background Processor to check for details about failed queues. The Queue Manager should be invoked by using the menu on the BP Queue Processor window. To check the failed queues, select **Edit | QueueManager| All or Edit | QueueManager|**

***{queue}*** and browse by queue type. The failed queues are sorted by error status.

<!-- image -->

Alternately select Edit|QueueManager | *Queue Type*

This information will provide some insight as to what processes are failing and why.

Right-clicking in the message or group level provides a menu to Re-Queue or Purge Queue.

###### Check that the DICOM Image and Text Gateways are Up and Functioning

Look for any error messages in the open windows. For each processor, make sure that there are windows open for listening and accepting images from those modalities that are assigned to that processor. MSM must be up and running on all gateways, as well as the display windows for the various monitoring sessions. If any of these are not running, restart them. Be sure that the VistA HIS is running.

###### Check that the DICOM Image Gateway Modalities are Sending Images

The ADPACs and end-users will generally let the IRM know if the modalities are not able to send or store images, however, it is good practice to check on this at the beginning of the day. Check the queue lengths.

###### Review the Image\_In Directory for Incomplete DCM Files

Review the entries in the Dicom\Image\_In directory for any files with “\_incomplete” appended to the file name. These are incomplete files received by a modality or a PACS interface that the DICOM image gateway could not process. Research the files to see if the entity resent them at a later time or the images were never received. These files will automatically be purged after one hour.

On the main hospital system, check to see if the DICOM FAILED IMAGES file (#2006.575) has entries that need correcting. If there are “failed image files”, work with the ADPACs and end-users to correct the information in the image headers and to associate these image files with the correct patients.

###### Review the M Error Traps

Review the M error traps on all of the DICOM Gateways and the main hospital system. Look for error messages related to the imaging routines (MAG*). If there are any errors that cannot be resolved by the local IRM staff, log a Remedy call so the VistA Imaging support staff may assist in their resolution. However, local IRM staff can easily address most error conditions.

###### Check the Hybrid Image DICOM Gateway (HDIG) Statistics and Log Files

For information about accessing the HDIG statistics and logs, see the *VistA Imaging DICOM Gateway User Manual* .

#### 28 Maintenance

Do an incremental tape backup of all active Imaging Tier 1 shares (for new images captured) or update copy media if doing media copies on the Tier 2 shares. Active Tier 1 shares can be isolated by RAID group configuration.

#### 29 Weekly Activities

A RAID Group is a group of one-to-many shares that will be recognized as a unit within the Imaging storage network. Its purpose is to reduce the number of active storage shares in order to facilitate quicker tape backups (both incremental and full). Newly acquired images are distributed evenly among all the shares within a RAID Group.

Do a full backup of active Imaging Tier 1 shares using the procedures in place at your site. For additional information, refer to Appendixes B and C in the *VistA Imaging Installation Guide* .

#### 30 Other Periodic Activities

Support for the VistA Imaging systems includes activities for support of Windows-based servers and the VistA System. Backups should be made for all systems. Current patches should be loaded for VistA. Service Packs for Windows and updates to the VistA Imaging software should be installed as they are released.

- Use the BP Queue Manager to re-queue failed entries and to purge the queues.
- Use the MagUtility program to maintain Tier 1 and Tier 2 storage resources. For details, see the *Storage Utilities User Manual* .
- Review the monthly Image Site Usage mail message to ensure all workstations have latest software installed.
- Before installing any new software or patches, first do a full backup, including the Registry files.
- For the VistARad diagnostic workstation monitors, calibration should be checked on a scheduled basis, at least monthly—more frequently is preferred. Consult the recommendations of the monitor manufacturer. Re-calibration should be performed whenever the calibration check reveals a need to do so. Also, whenever any part of the monitor/video driver hardware configuration is altered, a new calibration must be performed. Examples of configuration changes include: re-setting brightness or contrast controls; removing or replacing a monitor; removing or replacing a video board; replacing the system PC; etc.
#### 31 Scheduled Down Time for VistA Servers

During a VistA System outage, DICOM Gateways will continue to provide modality worklist functionality and to capture images that are temporarily stored on the gateway. This is important to allow the radiology department to continue to perform studies. If you anticipate that the VistA System must be down, it is best to take the following steps:

- Perform all DICOM fixes before the VistA System goes down. This will free the maximum space for temporary image storage.

During the outage, watch the gateways to be sure they still have adequate space to store images.

This page is intentionally left blank.

### Chapter 6	Routine Descriptions

***The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes*** *.*

***VA Policy states the following:***

***Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.***

**All routines, files and fields of the VistA Imaging package may not be altered except by the OI Technical Services (TS) staff. This software is regulated by the FDA and implements controlled procedures.t**

<!-- image -->

#### 32 VistA Imaging Routines on the VistA Hospital Information System

##### Build Checksums

The Calculate and Show Checksum Values [XTSUMBLD-CHECK] menu option can be used as shown below to display a list of checksums for a specified build (KIDS file).

<!-- image -->

##### Package Checksums

The Calculate and Show Checksum Values [XTSUMBLD-CHECK] menu option can be used as shown below to display a list of checksums for all routines in the Imaging Package. Imaging routines are under the MAG namespace.

<!-- image -->

##### Routine Descriptions

To obtain a brief description for all VistA Imaging routines, use the First Line Routine Print [XU FIRST LINE PRINT] menu option. Including the second line in the report will show which patches have made changes to the routine. This menu option is part of Programmer Options [XUPROG] under sub-menu Routine Tools [XUPR-ROUTINE-TOOLS].

VistA Imaging routines are under the MAG namespace. The following is an example:

<!-- image -->

#### 33 DICOM Gateway Routines

The VistA Imaging DICOM Gateway requires a number of M routines. Most of these are part of the VistA Imaging package. However, because the DICOM gateways run as standalone workstations, they must include some routines from other packages. A few routines must run in the manager UCI.

##### Checksums of VistA Imaging DICOM Gateway Routines

The following listing reflects the VistA Imaging M routines that reside on the VistA Imaging DICOM gateway system.

| **Routine**   |   **Checksum** | **Routine**   |   **Checksum** | **Routine**   |   **Checksum** |
|---------------|----------------|---------------|----------------|---------------|----------------|
| MAG7UP        |      35026309  | MAGDACU       |       9404510  | MAGDAIRM      |     117531807  |
| MAGBRTA4      |      73323436  | MAGDACU0      |      10807003  | MAGDAIRP      |      31922397  |
| MAGBRTA5      |      74916344  | MAGDACU1      |      38544788  | MAGDAIRR      |      91423560  |
| MAGBRTA6      |      10352181  | MAGDACU2      |       7237662  | MAGDAIRS      |      15785148  |
| MAGBRTB1      |      26772420  | MAGDACU3      |       8904229  | MAGDAIRU      |     124794686  |
| MAGBRTB2      |      62448973  | MAGDACW1      |      48007177  | MAGDAIRW      |      28060731  |
| MAGBRTB3      |      21639509  | MAGDACW2      |      26199743  | MAGDAUD1      |      21787487  |
| MAGBRTB4      |      29268889  | MAGDAIR1      |      38225804  | MAGDAUD2      |      11632745  |
| MAGBRTK       |      20097310  | MAGDAIR2      |     174066539  | MAGDAUD3      |       4475591  |
| MAGBRTLR      |      10848658  | MAGDAIR3      |      96391606  | MAGDBB        |      19747360  |
| MAGBRTP1      |      30941600  | MAGDAIR4      |     110325747  | MAGDBB2       |      44540545  |
| MAGDACP1      |      74390040  | MAGDAIR5      |      65081294  | MAGDCIGL      |      22088679  |
| MAGDACP2      |       5612621  | MAGDAIR6      |     179937644  | MAGDCIRL      |      14772888  |
| MAGDACP3      |      46008004  | MAGDAIRA      |      57712921  | MAGDCMPE      |      19614608  |
| MAGDACR1      |      33293963  | MAGDAIRC      |      21720426  | MAGDCST1      |      15269197  |
| MAGDACR2      |      16258693  | MAGDAIRD      |      93443153  | MAGDCST2      |      11326972  |
| MAGDACR3      |      55462381  | MAGDAIRL      |      21354401  | MAGDCST3      |      86034617  |
| MAGDCST4      |      37159893  | MAGDHR5       |       3902302  | MAGDIR7F      |      32599821  |
| MAGDCST5      |      11640174  | MAGDHR9       |       7550226  | MAGDIR7G      |       9410773  |
| MAGDCST6      |      21003965  | MAGDHRC       |      86680704  | MAGDIR7T      |      38613863  |
| MAGDDEL       |       4367093  | MAGDHRC0      |       7768511  | MAGDIRDE      |       8549629  |
| MAGDDEL1      |       7861418  | MAGDHRC1      |      32850852  | MAGDIW2A      |      17353490  |
| MAGDDEL2      |      31000923  | MAGDHRC2      |      25348186  | MAGDIW3       |      20340399  |
| MAGDDEL3      |       7544616  | MAGDHRC3      |     127795528  | MAGDIW3A      |      85967674  |
| MAGDDR0       |      57333954  | MAGDHRC4      |     138693297  | MAGDIW3B      |      39882981  |
| MAGDDR1       |      48401978  | MAGDHRC5      |     109418054  | MAGDIW3C      |      14730954  |
| MAGDDR2       |      33721647  | MAGDHRC6      |      32964204  | MAGDIW4       |      20553707  |
| MAGDDR2A      |     103732840  | MAGDHRC7      |      19766889  | MAGDIW6       |      33599253  |
| MAGDDR3       |      55887980  | MAGDHRCP      |      44418147  | MAGDIWB0      |       5743080  |
| MAGDDR7       |      19337667  | MAGDHRCU      |       4706071  | MAGDIWB1      |      82684636  |
| MAGDDW0       |      18480829  | MAGDIR3       |      32120170  | MAGDIWB2      |      51239563  |
| MAGDDW1       |      33395508  | MAGDIR4A      |       9771049  | MAGDIWB5      |      94186343  |
| MAGDDW2       |      52939670  | MAGDIR5       |       7586177  | MAGDIWB7      |      16107756  |
| MAGDDW3       |      37085878  | MAGDIR6       |      88850067  | MAGDIWBA      |      81638859  |
| MAGDDW4       |      82471058  | MAGDIR6A      |      13107192  | MAGDIWBB      |      69921591  |
| MAGDECHO      |       9429115  | MAGDIR6B      |      21857231  | MAGDIWBC      |      86128746  |
| MAGDEXC1      |      41469390  | MAGDIR6C      |      45366757  | MAGDIWBD      |      30843111  |
| MAGDEXC2      |      53045931  | MAGDIR6D      |      24854094  | MAGDIX        |       5690876  |
| MAGDFCNS      |      89968928  | MAGDIR6E      |      23447535  | MAGDIX1       |      28030316  |
| MAGDFND0      |      23608364  | MAGDIR6F      |      22472350  | MAGDLOGI      |      18187840  |
| MAGDFND1      |      17372953  | MAGDIR6G      |       8628791  | MAGDLOGN      |      67846184  |
| MAGDFND2      |     103160968  | MAGDIR7       |       4535461  | MAGDM2MB      |      16447591  |
| MAGDFND3      |     108714097  | MAGDIR71      |      67975394  | MAGDMENA      |      55414961  |
| MAGDFND4      |      46237039  | MAGDIR72      |       4436051  | MAGDMENL      |       7216238  |
| MAGDFND5      |      11438147  | MAGDIR73      |       5722083  | MAGDMENO      |      39923631  |
| MAGDFND9      |       5028212  | MAGDIR74      |       6275398  | MAGDMENU      |      51445030  |
| MAGDGEX1      |      76377251  | MAGDIR75      |      50725923  | MAGDMFB       |      47598711  |
| MAGDGEX2      |      25589452  | MAGDIR7C      |      89687601  | MAGDMFB1      |      85395849  |
| MAGDGLC       |      36322745  | MAGDIR7D      |      16648443  | MAGDMFB2      |      49214267  |
| MAGDMFB3      |      41066270  | MAGDQUE3      |      28047976  | MAGOSFIL      |      37547909  |
| MAGDMFB4      |      15205941  | MAGDQUE4      |      27764385  | MAGOSMSC      |      51783237  |
| MAGDMFB5      |      25775790  | MAGDRPC0      |       4862620  | MAGOSTCP      |      32979219  |
| MAGDMFB6      |      19405158  | MAGDSSD       |       6477867  | MAGSPID       |       3966944  |
| MAGDMFB7      |      26178773  | MAGDSTA1      |      68354778  | MAGUE         |      75297995  |
| MAGDMFB8      |      13147824  | MAGDSTAT      |      52825843  | MAGVCSTR      |      11185442  |
| MAGDMFB9      |      25588255  | MAGDSTRT      |      14101280  | MAGVDGW1      |      14542314  |
| MAGDMFBA      |      16186541  | MAGDTCP       |       6918159  |               |                |
| MAGDMFBB      |      53824931  | MAGDTCP1      |      69855871  |               |                |
| MAGDMFBC      |      36412183  | MAGDTCP2      |      29403903  |               |                |
| MAGDMFBD      |      38641825  | MAGDTCP3      |      10117098  |               |                |
| MAGDMFBE      |      86462667  | MAGDTGA       |       5398596  |               |                |
| MAGDMFBI      |      29578964  | MAGDTLOG      |      20351436  |               |                |
| MAGDMFBM      |      87591678  | MAGDUID1      |       3785565  |               |                |
| MAGDMFBN      |       5306612  | MAGDUID2      |       6700589  |               |                |
| MAGDMFBP      |      17921307  | MAGDUID4      |      21494340  |               |                |
| MAGDMFBS      |      52098283  | MAGDVRSN      |       3291181  |               |                |
| MAGDMFBT      |      19123785  | MAGDWLKL      |      36028521  |               |                |
| MAGDMFBW      |      97895675  | MAGDWLP2      |       3990165  |               |                |
| MAGDMFCC      |      25444929  | MAGDWLP3      |      78343810  |               |                |
| MAGDMFIC      |      46728636  | MAGDWLPA      |      69861115  |               |                |
| MAGDMLGV      |      76186792  | MAGDWLPB      |      55436315  |               |                |
| MAGDMLOG      |      32785216  | MAGDWLPC      |      16460081  |               |                |
| MAGDMMSG      |      53806690  | MAGDWLU       |       4339594  |               |                |
| MAGDMPPC      |       8533330  | MAGDWLU0      |      38702922  |               |                |
| MAGDMSGT      |       9617440  | MAGDWLU1      |      44796296  |               |                |
| MAGDOS        |       5971106  | MAGDWLU2      |     104897245  |               |                |
| MAGDQR15      |      17707603  | MAGDWLU3      |       5869877  |               |                |
| MAGDQRU0      |       5735145  | MAGDWLU4      |      59848201  |               |                |
| MAGDQUE0      |      30499869  | MAGM2VC       |      89722252  |               |                |
| MAGDQUE1      |      32915712  | MAGM2VCU      |      20477697  |               |                |
| MAGDQUE2      |      21951411  | MAGOSDIR      |       28047976 |               |                |

##### DICOM Gateway Routine Descriptions

The M routines on the DICOM Gateway can be listed using the FIRST ROUTINE LINE DISPLAY routine (%RFIRST). The following is an example of steps required to use the % RFIRST routine to list Imaging routines.

<!-- image -->

See the previous section for the checksums of the distributed routines.

##### Kernel RPC Broker Routines

Two RPC Broker routines are incorporated into the DICOM Gateway software. See the *VistA Imaging Security Guide* for more information.

#### 34 Non-M Routines Distributed as Executable Files

Executable, DLL and other supporting files, which are distributed, include capture device- specific imaging software and executable imaging software. The routine listing below is by function.

##### Clinical Workstation Files

The following tables list files installed on a Clinical (Display or Capture) workstation.

**Note:** Under Windows 7, some “system” files (including executable program files) may be stored in different directories than under Windows XP. Table headings below indicate only the Windows XP pathnames. Windows 7 pathnames are similar, with these changes:

| **Windows XP**          | **Windows 7**                              |
|-------------------------|--------------------------------------------|
| C:\Program Files\...    | C:\Program Files (x86)\...                 |
| C:\Windows\system32\... | C:\Windows\SystemWoW64 C:\Windows\System32 |

C:\Windows\SystemWoW64 is used for 32-bit files. C:\Windows\System32 is used for 64-bit files. This may sound backward, but it has to do with backward compatibility requirements.

SysWoW64, standing for **W** indows 32-bit **o** n **W** indows **64** -bit, contains program files for 32-bit compatibility used on a 64-bit system. A Windows 7 emulator redirects calls for any “System32” files to the SysWoW64 folder.

Configuration and log file pathnames are changed as follows:

| **Windows XP**                                                                                                                                                                                                 | **Windows 7**                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag.ini (TeleReader)  C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture) | C:\ProgramData\Vista\Imaging\mag.ini (TeleReader)  C:\ProgramData\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture) |
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging \MagTeleReaderConfig.ini                                                                                                                    | C:\ProgramData\Vista\Imaging\ MagTeleReaderConfig.ini                                                                              |
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging\Log\MagTeleReaderConfig100420120 34524PM.log*                                                                                               | C:\ProgramData\Vista\Imaging\ Log\MagTeleReaderConfig100420120345 24PM.log*                                                        |

*The name of the log file is based on MagTeleReaderConfig + date time stamp.

The following tables list files installed on a Clinical (Display or Capture) workstation.

| **Clinical Display &amp; Capture files**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging**   |                                                                           |                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABSTRTGA.EXE                                                                                                                                                | HSUMM.TXT                                                                 | MagScanFilm.EXE MagSCREEN.HLP  Magsys.cnt MAGSYS.EXE  Magsys.hlp MAGSYS.ini MagSysKey.CNT MAGSYSKEY.HLP  **MagTeleReader.exe MagTeleReaderConfig.exe**  magupdate.ini magwrks.CNT MAGWRKS.EXE  Magwrks.hlp MEANSTEST.HLP  SCNAPI.DLL |
| ActiveMILDefault.exe                                                                                                                                        | ImagDEMO.DAT                                                              |                                                                                                                                                                                                                                      |
| Annotation Editor Help.cnt                                                                                                                                  | mag308.ini*                                                               |                                                                                                                                                                                                                                      |
| ANNOTATION EDITOR HELP.HLP  demo12.txtDEMO1802.T XT                                                                                                         | MagDemos.TXTMagEKGVi ew.hlp  **MagImageCapture.e xe**  MAGIMAGEDELETE.HLP |                                                                                                                                                                                                                                      |
| DEMO2230.TXT                                                                                                                                                | **MagImageDisplay.exe**                                                   |                                                                                                                                                                                                                                      |
| demo3.txt                                                                                                                                                   | magIniPermissions.bat                                                     |                                                                                                                                                                                                                                      |
| DEMO446.TXT                                                                                                                                                 | MagMinibld.EXE                                                            |                                                                                                                                                                                                                                      |
| demolist.txt                                                                                                                                                | magPermissions.bat                                                        |                                                                                                                                                                                                                                      |
| DocScan.cnt                                                                                                                                                 | MagScan150N.BAT                                                           |                                                                                                                                                                                                                                      |
| DOCSCAN.HLP                                                                                                                                                 | MagScan75N.BAT                                                            |                                                                                                                                                                                                                                      |
| ERRLOOK.EXE                                                                                                                                                 | MagScanFile.EXE                                                           |                                                                                                                                                                                                                                      |
| ERRLOOK.HLP                                                                                                                                                 |                                                                           |                                                                                                                                                                                                                                      |
| FRAMGRAB.EXE                                                                                                                                                |                                                                           |                                                                                                                                                                                                                                      |
| *The main application files are shown in bold.*  *Files ending in ‘.cnt’ and ‘.hlp’ are contents for help files and help files.*                            |                                                                           |                                                                                                                                                                                                                                      |

| **Icons used by Clinical Display &amp; Capture**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging**   |                     |                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------|
| abscine.bmp                                                                                                                                                         | DoD_PDF.bmp         | magrtf.bmp       |
| absekg.bmp                                                                                                                                                          | DoD_PDF.psd         | magtext.bmp      |
| ABSERROR.BMP                                                                                                                                                        | DoD_RTF.bmp         | magwav.bmp       |
| absjbox.bmp                                                                                                                                                         | DoD_RTF.psd         | MotionVideo.bmp  |
| abspacg.bmp                                                                                                                                                         | DoD_Unavailable.bmp | Magblack.bmp     |
| abspaci.bmp                                                                                                                                                         | DoD_Unavailable.psd | magdoc.bmp       |
| absremote.bmp                                                                                                                                                       | DoD_Word.bmp        | maghtml.bmp      |
| AnnotPencilSmall.bmp                                                                                                                                                | DoD_Word.psd        | magpdf.bmp       |
| AnnotReadOnly.bmp                                                                                                                                                   | downarrow1.bmp      | magsensitive.bmp |
| AnnotReadOnly.psd                                                                                                                                                   | ImageQA.bmp         | magtext.bmp      |

| **Icons used by Clinical Display &amp; Capture**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging**   |                                     |                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------|
| BLANK2.bmp  BLANK.BMP                                                                                                                                               | InternalError.bmp FileOpenError.bmp | magwav.bmp  MotionVideo.bmp |
| Blank.tga                                                                                                                                                           | FullResFileNotFound.bmp             | MotionVideoAbs.bmp          |
| CAPTURE.BMP                                                                                                                                                         | FullResFileOpenError.bmp            | NOTEXIST.BMP                |
| DoD_ASCII.bmp                                                                                                                                                       | ImageUnavailable.bmp                | PRECAP.BMP                  |
| DoD_ASCII.psd                                                                                                                                                       | jboffln.abs                         | magBlockedImage.bmp         |
| DoD_Doc.bmp                                                                                                                                                         | JBOFFLN.bmp                         | magsensitive.bmp            |
| DoD_Doc.psd                                                                                                                                                         | JBOFFLN.tga                         | uparrow1.bmp                |
| DoD_JPG.bmp                                                                                                                                                         | magavi.bmp                          |                             |
| DoD_JPG.psd                                                                                                                                                         | magBlockedImage.bmp                 |                             |
| DoD_NCAT.bmp                                                                                                                                                        | magDeletedGroup.bmp                 |                             |
| DoD_NCAT.psd                                                                                                                                                        | magDeletedImage.bmp                 |                             |

| **Sample images (obsolete)**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Image Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Image**   |           |             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|
| *These files are no longer distributed as of Patch 8, but may be present on older workstations. These files are no longer used.*                            |           |             |
| BLACKBOX.TGA                                                                                                                                                | DILB3.BMP | Samples.txt |

| **XP 32-bit -- C:\Program Files\VistA\Imaging\Help\Client**  **Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Help\Client**   |                                                          |                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------|
| *All files in this directory are help files for the VistA Imaging Display and Capture clients.*                                         |                                                          |                                        |
| **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Lib Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Lib**                 |                                                          |                                        |
| ACE.dll AGM.dll BIB.dll                                                                                                                 | GEAR32PO.OCX  ig\_cmyk\_profile.icm ig\_rgb\_profile.icm | igMED15a.ocx igmed15d.dll igmed32s.dll |

| **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Lib Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Lib**   |                  |                           |
|---------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------|
| BIBUtils.dll                                                                                                              | igART15a.ocx     | IGMed32x.ocx              |
| DL70ACE.dll                                                                                                               | igartgui15d.dll  | igmult15d.dll             |
| DL70AdobeXMP.dll                                                                                                          | igCORE15a.ocx    | igMULTIMEDIA15a.ocx       |
| DL70AGM.dll                                                                                                               | igCORE15d.dll    | igPDF15a.ocx              |
| DL70ARE.dll                                                                                                               | igDISPLAY15a.ocx | igPROCESSING15a.ocx       |
| DL70AXE8SharedExpat.dll                                                                                                   | igDLGS15a.ocx    | igVECT15a.ocx             |
| DL70AXE16SharedExpat.dll                                                                                                  | igEFFECTS15a.ocx | igVIEW15a.ocx             |
| DL70BIB.dll                                                                                                               | igFORMATS15a.ocx | JP2KLib.dll               |
| DL70BIBUtils.dll                                                                                                          | igguidlg15a.dll  | kdu_v52R.dll              |
| DL70CoolType.dll                                                                                                          | igguiwin15a.dll  | MagAnnOCX.ocx             |
| DL70JP2KLib.dll                                                                                                           | igJPEG2K15a.ocx  | MagAnnTool.dllnserver.dll |
| DL70PDFL.dll                                                                                                              | igLZW15a.ocx     | SliceCalc.dll             |
|                                                                                                                           |                  | XRefUtils.dll             |

| **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Accusoft16.2 Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Accusoft16.2**   |                          |                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| ACE.dll                                                                                                                                               | ig_cmyk_profile.icm      | igMED16a.ocxigMULTIMEDIA16   |
| AGM.dll                                                                                                                                               | ig_rgb_profile.icm       | a.ocx                        |
| BIB.dll                                                                                                                                               | igART16a.ocx             | igPDF16a.ocxigPROCESSING16a. |
| BIBUtils.dll                                                                                                                                          | igartgui16d.dll          | ocx                          |
| DL81ACE.dll                                                                                                                                           | igArtX16a.ocx            | igtwain16a.ocx               |
| DL81AdobeXMP.dll                                                                                                                                      | igArtX16d.dll            | igtwain16d.dll               |
| DL81AGM.dll                                                                                                                                           | IGArtXGUI16a.ocx         | igVECT16a.ocxigVIEW16a.ocx   |
| DL81ARE.dll                                                                                                                                           | igArtXGUI16d.dll         | JP2KLib.dll                  |
| DL81AXE8SharedExpa                                                                                                                                    | igCORE16a.ocxigDISPLAY16 | kdu_v52R.dll                 |
| t.dll                                                                                                                                                 | a.ocx                    | mfc71.dll                    |
| DL81BIB.dll                                                                                                                                           | igDLGS16a.ocx            | msvcp71.dll                  |
| DL81BIBUtils.dll                                                                                                                                      | igEFFECTS16a.ocx         | msvcr71.dll                  |
| DL81CoolType.dll                                                                                                                                      | igFORMATS16a.ocx         | nserver.dll                  |
| DL81JP2KLib.dll                                                                                                                                       | igguidlg16a.ocx          |                              |
| DL81PDFL.dll                                                                                                                                          | igguidlg16a.dll          |                              |
|                                                                                                                                                       | igguiwin16a.dll          |                              |
|                                                                                                                                                       | igJBIG216a.ocx           |                              |
|                                                                                                                                                       | igJBIG216d.dll           |                              |
|                                                                                                                                                       | igJPEG2K16a.ocx          |                              |
|                                                                                                                                                       | igjpeg2k16d.dll          |                              |
|                                                                                                                                                       | igLZW16a.ocx             |                              |
|                                                                                                                                                       | iglzw16d.dll             |                              |

| **PDF support files**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\CMap Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\CMap**   |                |                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------|
| 78-EUC-H                                                                                                                                                                               | B5pc-H         | KSCms-UHC-H     |
| 78-EUC-V                                                                                                                                                                               | B5pc-UCS2      | KSCms-UHC-HW-H  |
| 78-H                                                                                                                                                                                   | B5pc-UCS2C     | KSCms-UHC-HW-V  |
| 78-RKSJ-H                                                                                                                                                                              | B5pc-V         | KSCms-UHC-UCS2  |
| 78-RKSJ-V                                                                                                                                                                              | CNS-EUC-H      | KSCms-UHC-V     |
| 78-V                                                                                                                                                                                   | CNS-EUC-V      | KSCpc-EUC-H     |
| 78ms-RKSJ-H                                                                                                                                                                            | CNS1-H         | KSCpc-EUC-UCS2  |
| 78ms-RKSJ-V                                                                                                                                                                            | CNS1-V         | KSCpc-EUC-UCS2C |
| 83pv-RKSJ-H                                                                                                                                                                            | CNS2-H         | KSCpc-EUC-V     |
| 90ms-RKSJ-H                                                                                                                                                                            | CNS2-V         | NWP-H           |
| 90ms-RKSJ-UCS2                                                                                                                                                                         | ETen-B5-H      | NWP-V           |
| 90ms-RKSJ-V                                                                                                                                                                            | ETen-B5-UCS2   | RKSJ-H          |
| 90msp-RKSJ-H                                                                                                                                                                           | ETen-B5-V      | RKSJ-V          |
| 90msp-RKSJ-V                                                                                                                                                                           | ETenms-B5-H    | Roman           |
| 90pv-RKSJ-H                                                                                                                                                                            | ETenms-B5-V    | UCS2-90ms-RKSJ  |
| 90pv-RKSJ-UCS2                                                                                                                                                                         | ETHK-B5-H      | UCS2-90pv-RKSJ  |
| 90pv-RKSJ-UCS2C                                                                                                                                                                        | ETHK-B5-V      | UCS2-B5pc       |
| 90pv-RKSJ-V                                                                                                                                                                            | EUC-H          | UCS2-ETen-B5    |
| Add-H                                                                                                                                                                                  | EUC-V          | UCS2-GBK-EUC    |
| Add-RKSJ-H                                                                                                                                                                             | Ext-H          | UCS2-GBpc-EUC   |
| Add-RKSJ-V                                                                                                                                                                             | Ext-RKSJ-H     | UCS2-KSCms-UHC  |
| Add-V                                                                                                                                                                                  | Ext-RKSJ-V     | UCS2-KSCpc-EUC  |
| Adobe-CNS1-0                                                                                                                                                                           | Ext-V          | UniCNS-UCS2-H   |
| Adobe-CNS1-1                                                                                                                                                                           | GB-EUC-H       | UniCNS-UCS2-V   |
| Adobe-CNS1-2                                                                                                                                                                           | GB-EUC-V       | UniCNS-UTF16-H  |
| Adobe-CNS1-3                                                                                                                                                                           | GB-H           | UniCNS-UTF16-V  |
| Adobe-CNS1-4                                                                                                                                                                           | GB-V           | UniCNS-UTF32-H  |
| Adobe-CNS1-B5pc                                                                                                                                                                        | GBK-EUC-H      | UniCNS-UTF32-V  |
| Adobe-CNS1-ETen-B5                                                                                                                                                                     | GBK-EUC-UCS2   | UniCNS-UTF8-H   |
| Adobe-CNS1-H-CID                                                                                                                                                                       | GBK-EUC-V      | UniCNS-UTF8-V   |
| Adobe-CNS1-H-Host                                                                                                                                                                      | GBK2K-H        | UniGB-UCS2-H    |
| Adobe-CNS1-H-Mac                                                                                                                                                                       | GBK2K-V        | UniGB-UCS2-V    |
| Adobe-CNS1-UCS2                                                                                                                                                                        | GBKp-EUC-H     | UniGB-UTF16-H   |
| Adobe-GB1-0                                                                                                                                                                            | GBKp-EUC-V     | UniGB-UTF16-V   |
| Adobe-GB1-1                                                                                                                                                                            | GBpc-EUC-H     | UniGB-UTF32-H   |
| Adobe-GB1-2                                                                                                                                                                            | GBpc-EUC-UCS2  | UniGB-UTF32-V   |
| Adobe-GB1-3                                                                                                                                                                            | GBpc-EUC-UCS2C | UniGB-UTF8-H    |
| Adobe-GB1-4                                                                                                                                                                            | GBpc-EUC-V     | UniGB-UTF8-V    |
| Adobe-GB1-GBK-EUC                                                                                                                                                                      | GBT-EUC-H      | UniHojo-UCS2-H  |
| Adobe-GB1-GBpc-EUC                                                                                                                                                                     | GBT-EUC-V      | UniHojo-UCS2-V  |
| Adobe-GB1-H-CID                                                                                                                                                                        | GBT-H          | UniHojo-UTF16-H |
| Adobe-GB1-H-Host                                                                                                                                                                       | GBT-V          | UniHojo-UTF16-V |

| **PDF support files**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\CMap Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\CMap**   |             |                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------|
| Adobe-GB1-H-Mac                                                                                                                                                                        | GBTpc-EUC-H | UniHojo-UTF32-H     |
| Adobe-GB1-UCS2                                                                                                                                                                         | GBTpc-EUC-V | UniHojo-UTF32-V     |
| Adobe-Japan1-0                                                                                                                                                                         | H           | UniHojo-UTF8-H      |
| Adobe-Japan1-1                                                                                                                                                                         | Hankaku     | UniHojo-UTF8-V      |
| Adobe-Japan1-2                                                                                                                                                                         | Hiragana    | UniJIS-UCS2-H       |
| Adobe-Japan1-3                                                                                                                                                                         | HKdla-B5-H  | UniJIS-UCS2-HW-H    |
| Adobe-Japan1-4                                                                                                                                                                         | HKdla-B5-V  | UniJIS-UCS2-HW-V    |
| Adobe-Japan1-5                                                                                                                                                                         | HKdlb-B5-H  | UniJIS-UCS2-V       |
| Adobe-Japan1-6                                                                                                                                                                         | HKdlb-B5-V  | UniJIS-UTF16-H      |
| Adobe-Japan1-90ms-RKSJ                                                                                                                                                                 | HKgccs-B5-H | UniJIS-UTF16-V      |
| Adobe-Japan1-90pv-RKSJ                                                                                                                                                                 | HKgccs-B5-V | UniJIS-UTF32-H      |
| Adobe-Japan1-H-CID                                                                                                                                                                     | HKm314-B5-H | UniJIS-UTF32-V      |
| Adobe-Japan1-H-Host                                                                                                                                                                    | HKm314-B5-V | UniJIS-UTF8-H       |
| Adobe-Japan1-H-Mac                                                                                                                                                                     | HKm471-B5-H | UniJIS-UTF8-V       |
| Adobe-Japan1-PS-H                                                                                                                                                                      | HKm471-B5-V | UniJISPro-UCS2-HW-V |
| Adobe-Japan1-PS-V                                                                                                                                                                      | HKscs-B5-H  | UniJISPro-UCS2-V    |
| Adobe-Japan1-UCS2                                                                                                                                                                      | HKscs-B5-V  | UniJISPro-UTF8-V    |
| Adobe-Japan2-0                                                                                                                                                                         | Hojo-EUC-H  | UniJISX0213-UTF32-H |
| Adobe-Korea1-0                                                                                                                                                                         | Hojo-EUC-V  | UniJISX0213-UTF32-V |
| Adobe-Korea1-1                                                                                                                                                                         | Hojo-H      | UniKS-UCS2-H        |
| Adobe-Korea1-2                                                                                                                                                                         | Hojo-V      | UniKS-UCS2-V        |
| Adobe-Korea1-H-CID                                                                                                                                                                     | Identity-H  | UniKS-UTF16-H       |
| Adobe-Korea1-H-Host                                                                                                                                                                    | Identity-V  | UniKS-UTF16-V       |
| Adobe-Korea1-H-Mac                                                                                                                                                                     | Katakana    | UniKS-UTF32-H       |
| Adobe-Korea1-KSCms-UHC                                                                                                                                                                 | KSC-EUC-H   | UniKS-UTF32-V       |
| Adobe-Korea1-KSCpc-EUC                                                                                                                                                                 | KSC-EUC-V   | UniKS-UTF8-H        |
| Adobe-Korea1-UCS2                                                                                                                                                                      | KSC-H       | UniKS-UTF8-V        |
| AdobeFnt09.lst                                                                                                                                                                         | KSC-Johab-H | V                   |
| B5-H                                                                                                                                                                                   | KSC-Johab-V | vssver2.scc         |
| B5-V                                                                                                                                                                                   | KSC-V       | WP-Symbol           |

| **PDF support files**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\Font Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\Font**   |    |    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|----|
| AdobeFnt09.lst vssver2.scc                                                                                                                                                             | zx	.mmm    | zy	.mmm    |

| **MUSE API support files**  **Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Muse Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Muse**   |                            |                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------|
| Bti.ini                                                                                                                                                 | lfmac80n.dll               | LTKRN80N.DLL                         |
| BUTIL.EXE                                                                                                                                               | lfmac80w.dll               | LTKRN80W.DLL                         |
| ccalc32.dll                                                                                                                                             | lfmsp80n.dll               | LTTHK80W.DLL                         |
| DCMUTL32.DLL                                                                                                                                            | lfmsp80w.dll               | LTTWN80N.DLL                         |
| lfavi80n.dll                                                                                                                                            | lfpcd80n.dll               | LTTWN80W.DLL                         |
| lfavi80w.dll                                                                                                                                            | lfpcd80w.dll               | LTWND80N.DLL                         |
| lfawd80n.dll                                                                                                                                            | lfpct80n.dll               | LTWND80W.DLL                         |
| lfbmp80n.dll                                                                                                                                            | lfpct80w.dll               | museapi.dll                          |
| lfbmp80w.dll                                                                                                                                            | lfpcx80n.dll               | museapi5a.dll                        |
| lfcal80n.dll                                                                                                                                            | lfpcx80w.dll               | MUSEAPI5e.dll                        |
| lfcal80w.dll                                                                                                                                            | lfpng80n.dll               | MUSEAPI7.dll                         |
| lfcmp80n.dll  lfcmp80w.dll                                                                                                                              | lfpng80w.dll  lfras80n.dll | museapiFAKE.dll (for non-MUSE sites) |
| lfdic80n.dll                                                                                                                                            | lfras80w.dll               | NWLOCALE.DLL                         |
| lfdic80w.dll                                                                                                                                            | lftga80n.dll               | PRINTLIB.DLL                         |
| lfeps80n.dll                                                                                                                                            | lftga80w.dll               | Tabctl32.ocx                         |
| lfeps80w.dll                                                                                                                                            | lftif80n.dll               | table32.dll                          |
| lffax80n.dll                                                                                                                                            | lftif80w.dll               | W3AIF103.DLL                         |
| lffax80w.dll                                                                                                                                            | lfwfx80n.dll               | W3BIF106.DLL                         |
| lffpx7.dll                                                                                                                                              | lfwfx80w.dll               | W3BTRV7.DLL                          |
| lffpx80n.dll                                                                                                                                            | lfwmf80n.dll               | W3CRS106.DLL                         |
| lfgif80n.dll                                                                                                                                            | lfwmf80w.dll               | W3MIF109.DLL                         |
| lfgif80w.dll                                                                                                                                            | lfwpg80n.dll               | W3NSL105.DLL                         |
| lfica80n.dll                                                                                                                                            | lfwpg80w.dll               | W3NSR103.DLL                         |
| lfica80w.dll                                                                                                                                            | LTANN80N.DLL               | W3SCMV7.DLL                          |
| lfimg80n.dll                                                                                                                                            | LTANN80W.DLL               | W3UPI104.DLL                         |
| lfimg80w.dll                                                                                                                                            | LTEFX80N.DLL               | WBEXEC.EXE                           |
| lfkodak.dll                                                                                                                                             | LTEFX80W.DLL               | WBTRCALL.DLL                         |
| lflma80n.dll lflma80w.dll                                                                                                                               | LTFIL80N.DLL LTFIL80W.DLL  | WBTRV32.DLL  wcalc32.dll             |
| lflmb80n.dll                                                                                                                                            | LTIMG80N.DLL               | zlib32.dll                           |
| lflmb80w.dll                                                                                                                                            | LTIMG80W.DLL               |                                      |

| **Annotation Editor support files - AccuSoft OCX files Windows XP 32-bit -- C:\windows\system32 Windows 7 64-bit -- C:\windows\SysWoW64**   |              |              |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
| igmed32s.dll                                                                                                                                | imgthumb.ocx | oissq400.dll |
| IGMed32x.ocx                                                                                                                                | jpeg1x32.dll | oitwa400.dll |
| imgadmin.ocx                                                                                                                                | jpeg2x32.dll | oiui400.dll  |
| imgcmn.dll                                                                                                                                  | oieng400.dll | tifflt.dll   |
| imgedit.ocx                                                                                                                                 | oiprt400.dll | xiffr3_0.dll |
| imgscan.ocx                                                                                                                                 | oislb400.dll |              |
| imgshl.dll                                                                                                                                  |              |              |

| **Display CDA Stylesheet support files -**  **Windows XP 32-bit -- C:\Program Files\Vista\Imaging\stylesheets Windows 7 64-bit -- C:\Program Files (x86)\Vista\Imaging\stylesheets**   |    |    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|----|
| **CDA.xsl**                                                                                                                                                                            |    |    |

| **Configuration File MAG.ini**   |                                                                            |
|----------------------------------|----------------------------------------------------------------------------|
| **Windows XP 32-bit**            | C:\Documents and Settings\All Users\Application Data\Vista\Imaging\MAG.ini |
| **Windows 7 64-bit**             | C:\ProgramData\Vista\Imaging\MAG.ini                                       |

**Note:** The directories in which some “system” files (including executable program files) are stored depend on the operating system on which the software is installed and on whether it is installed on a 32-bit computer or on a 64-bit computer. The following table lists the paths for the currently supported platforms.

| **Windows XP 32-bit**   | **Windows 7 64-bit**       |
|-------------------------|----------------------------|
| C:\Program Files\...    | C:\Program Files (x86)\... |
| C:\Windows\system32\... | C:\Windows\SysWoW64        |

Configuration and log file pathnames are changed as follows:

| Windows XP                                                                                                                                                                                                     | Windows 7                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag.ini (TeleReader)  C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture) | C:\ProgramData\Vista\Imaging\mag.ini (TeleReader)  C:\ProgramData\Vista\Imaging\mag308.ini(Cli nical Display and Clinical Capture) |
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging  \MagTeleReaderConfig.ini                                                                                                                   | C:\ProgramData\Vista\Imaging\ MagTeleReaderConfig.ini                                                                              |
| C:\Documents and Settings\All Users\Application Data\Vista\Imaging\Log\MagTeleReaderConf ig10042012034524PM.log*                                                                                               | C:\ProgramData\Vista\Imaging\ Log\MagTeleReaderConfig10042012034524P M.log*                                                        |

*The name of the log file is based on MagTeleReaderConfig + date time stamp.

##### Background Processor Files

| **File Name**          | **Description**                                                           |
|------------------------|---------------------------------------------------------------------------|
| GEAR32PO.OCX           | Used by mag_makeabs.exe to create derivative files.                       |
| igmed32s.dll           | Used by mag_makeabs.exe to create derivative files.                       |
| IGMed32x.ocx           | Used by mag_makeabs.exe to create derivative files.                       |
| MagImportXControl1.ocx | Import API Active X control file used by the Background Processor.        |
| mag_makeabs.exe        | Creates derivative files                                                  |
| Magbtm.exe             | Processes queues and configures imaging system files.                     |
| MagHTMLARchive.exe     | Creates HTML output log files                                             |
| MagVerifier.exe        | Performs database integrity checks.                                       |
| MagPurge.exe           | Removes old image files and recovers image files on VistA Imaging shares. |

##### Online Help Files

Online help files are installed with the Clinical Workstation, Background Processor (BP), and VistARad software.

All three of the BP applications are documented in MAG\_BPUserman.htm and the contents of the MAG\_BPUserman\_files subdirectory. The MAG\_BP\_User\_Manual.PDF can also be found in the application subdirectory and can be accessed from the Help menu of the BP Queue Processor main window.

The clinical workstation help system is located in the C:\Program Files\VistA\Imaging\Help

\Client\index.htm subdirectory. If the workstation is using the Windows 7 (64 bit) operating system, a separate help file for TeleReader is located in C:\Program Files(x86)\VistA\Imaging\Help\TeleReader. The file name is MAGTeleReaderConfig.pdf.

##### DICOM Gateway Files

The following tables list files that are part of a DICOM Gateway installation. Files are grouped by folder.

**C:\Program Files\VistA\Imaging\DICOM –** Primary program files

| **File Name**             | **Description**                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------|
| BATCH_SEND_IMAGE.BAT      | Batch file that takes a folder of DICOM objects and sends them to a storage provider.                            |
| CTN_VERSION.EXE           | Program that prints the current installed version of the Central Test Node software.                             |
| DCF_LicenseInstaller.bat  | Program that installs the DCF Toolkit license.                                                                   |
| DCM_DIFF.EXE              | Program that compares two DICOM files.                                                                           |
| DCM_DUMP_ELEMENT.EXE      | Program that dumps the content of a DICOM tag into a DICOM file.                                                 |
| DCM_DUMP_FILE.EXE         | Program that dumps the content of a DICOM file.                                                                  |
| DICOM_ECHO.EXE            | Program that can be used to test network connectivity with DICOM modalities.                                     |
| DRIVES.EXE                | Program that provides information on currently mounted disk drives.                                              |
| ERRLOOK.EXE               | Program that can be used to display the meaning of an MS-Windows error code.                                     |
| MAG_AbstrTGA.EXE          | Program that creates thumbnails of images.                                                                       |
| MAG_COMPRESSOR_AWARE.E XE | Program to compress image files before transmission.                                                             |
| MAG_CSTORE.EXE            | Program that runs on the DICOM Gateway to store images.                                                          |
| MAG_DCM_COPY.EXE          | Program that copies parts of DICOM files (used for modifying information in image headers).                      |
| MAG_DCMABSTRACT.EXE       | Program that creates abstracts (thumbnails of images) from DICOM objects.                                        |
| MAG_DCMTOTGA.EXE          | Program that converts DICOM images to Targa Images.                                                              |
| MAG_DCM_COPY.EXE          | Program that copies parts of DICOM files (used for modifying information in image headers).                      |
| MAG_MAKELINK.EXE          | Program to create icons.                                                                                         |
| MAG_RECON.EXE             | Program to reconstruct a DICOM File from an existing DICOM file and a script file containing header-information. |
| MAG_RECON.TXT             | Sample script file to be used with MAG_Recon.exe.                                                                |
| MAG_TELNET.CNT            | Table of contents for Help file.                                                                                 |
| MAG_ TELNET.EXE           | Help file for Telnet client application.                                                                         |
| MAG_ TELNET.HLP           | Telnet client application.                                                                                       |
| MAG_TGATODCM.EXE          | Program that converts Targa images to DICOM images.                                                              |
| MAG_VISTA_SEND_IMAGE.EX E | Program that transmits image files.                                                                              |
| MSVCR71.DLL               | Support library for executables compiled with Microsoft C Compiler.                                              |
| OD.EXE                    | Program that produces octal dumps of binary files.                                                               |
| PATHMAN.EXE               | Program that manipulates the default “path” lookup string.                                                       |
| SEND_IMAGE.EXE            | Program that transmits image files.                                                                              |
| SLEEP.EXE                 | Program that allows a batch file to “wait” for a couple of seconds.                                              |

| **File Name**   | **Description**                                      |
|-----------------|------------------------------------------------------|
| MAG_DCMVIEW.EXE | DICOM image viewer: Program to display DICOM images. |
| VIEWER1.ICO     | Icon for MAG_DCMView.exe program.                    |

**C:\Program Files\VistA\Imaging\DCMView –** DICOM Viewer program files

**C:\Program Files\VistA\Imaging\CVixInstaller** – CVIX installer files

This folder and its subfolders contain the files for the CVIX installer. They should not be modified or deleted.

**C:\Program Files\VistA\Imaging\HDIGInstaller** – HDIG installer files

This folder and its subfolders contain the files for the HDIG installer. They should not be modified or deleted.

**C:\Program Files\VistA\Imaging\VIXInstaller** – VIX installer files

This folder and its subfolders contain the files for the VIX installer. They should not be modified or deleted.

**C:\Program Files\VistA\Imaging\MAG\_MakeAbs –** Abstract generator files

| **File Name**        | **Description**                                                                |
|----------------------|--------------------------------------------------------------------------------|
| MAG_DCMABSTRACT.I CO | Icon for MAG_DCMabstract.exe.                                                  |
| README.TXT           | File, which provides status information about the Abstract Maker installation, |

**C:\DICOM –** Icon files

| **File Name**   | **Sample**     |
|-----------------|----------------|
| MAGCSTORE.ICO   | <!-- image --> |
| MAGVISTA.ICO    | <!-- image --> |

**C:\DICOM\Abstract –** Files used for generic abstracts for certain image types

| **File Name**      | **Description**                                                                             |
|--------------------|---------------------------------------------------------------------------------------------|
| CANNED_IMAGE.JPG   | Canned abstract for JPEG files.                                                             |
| MAG_CANNED_ECG.BMP | Canned abstract for ECG files.                                                              |
| MAG_CANNED_PDF.BMP | Canned abstract for PDF files.                                                              |
| MAG_WHATEVER.BMP   | Canned abstract for other types of files that cannot have abstracts generated “on the fly”. |

**C:\DICOM\Cache –** Caché database folder

| **File Name**      | **Description**                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| CACHE.DAT          | Program that has the Caché database for DICOM Gateways.                                                    |
| CSTORE.OUT         | Startup log file produced by backend M server for the MAG_CSTORE.EXE front end storage provider processes. |
| WORKLIST_60010.OUT | Startup log file produced by backend M server for the Modality Worklist provider processes.                |

**C:\DICOM\Data1 –** Text data folder; additional Data2, Data3, folders may exist

*May be stored in other local drives on older systems*

| **File Name**   | **Description**                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------|
| INIT_DICOM.BAT  | Program that re-initializes the subdirectories of the directory in which the BAT file is stored. |
| SEARCH.BAT      | Program that scans .TXT files for the occurrence of a specified string.                          |

**&lt;drive&gt;:\DICOM\Dict –** Dictionary files, typically stored in a network folder

| **File Name**     | **Description**                                                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AE_TITLE.DIC      | Dictionary file that maps DICOM Application Entity Titles to well-known aliases and provides descriptions.                                                     |
| AE_TITLE.SAMPLE   | Distributed initial version of AE_TITLE.DIC file.                                                                                                              |
| CT_PARAM.DIC      | Table containing prior settings for conversion parameters. Imported by ^MAGDMFB7.                                                                              |
| DATA_CR.DIC       | Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.                                                                                 |
| DATA_MRI.DIC      | Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.                                                                                 |
| DATAGECT.DIC      | Additional data fields to be displayed on DICOM Gateway (General Electric). Imported by ^MAGDIR4.                                                              |
| DATAMISC.DIC      | Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.                                                                                 |
| ELEMENT.DIC       | DICOM Element dictionary. Imported by ^MAGDMFB2.                                                                                                               |
| HL7.DIC           | VistA HL7 dictionary. Imported by ^MAGDMFB7.                                                                                                                   |
| INSTRUMENT.DIC    | List of image producing instruments, distributed as Instrument.Sample. Imported by ^MAGDMFB8                                                                   |
| INSTRUMENT.SAMPLE | Distributed initial version of INSTRUMENT.DIC.                                                                                                                 |
| MODALITY.DIC      | Image processing rules for modalities. Imported by  ^MAGDMFB8.                                                                                                 |
| MODALITY.SAMPLE   | Distributed initial version of MODALITY.DIC.                                                                                                                   |
| PORTLIST.DIC      | Locally edited list of network ports for DICOM services. Imported by ^MAGDMFB9.                                                                                |
| PORTLIST.SAMPLE   | Distributed initial version of PORTLIST.DIC.                                                                                                                   |
| ROUTE.DIC         | Locally edited list of image processing rules for automatic routing. Imported by ^MAGBTRB1.                                                                    |
| ROUTE.SAMPLE      | Distributed initial version of ROUTE.DIC.                                                                                                                      |
| SCP_LIST.DIC      | Provider application parameters. Imported by  ^MAGDMFB9.                                                                                                       |
| SCU_LIST.DIC      | List of Service Class User Applications, distributed as SCU_List.Sample. Imported by ^MAGDMFB9.                                                                |
| TEMPLATE.DIC      | Macros for event message templates. Imported by  ^MAGDMFB3.                                                                                                    |
| TEMPLATE.TMP      | Temporary file created when loading the TEMPLATE.dic dictionary.                                                                                               |
| UID.DIC           | UID dictionary. Imported by ^MAGDMFB4.                                                                                                                         |
| WORKLIST.DIC      | Locally edited list of the modality Called Application Entity Titles and the corresponding DICOM Modality Worklist database attributes. Imported by ^MAGDMFB8. |
| WORKLIST.SAMPLE   | Distributed initial version of WORKLIST.DIC.                                                                                                                   |

| **File Name**       | **Description**                                  |
|---------------------|--------------------------------------------------|
| MAGDICOM.SETUP.CSP  | Temporary file used in the installation process. |
| MAGDICOM.STATUS.CSP | Temporary file used in the installation process. |
| MAGLOGO1.GIF        | Temporary file used in the installation process. |
| MAGLOGO2.GIF        | Temporary file used in the installation process. |
| MAGMASTERFILE.CSP   | Temporary file used in the installation process. |
| VABKG.JPG           | Temporary file used in the installation process. |

**C:\DICOM\Web –** Contains temporary files that are used in the installation process.

###### Sample Files

For the purpose of testing that the software is properly installed, a number of sample files are included in the distribution kit.

###### Sample DICOM Images

The sample images that are available for the DICOM gateway can be used to perform trial image transmissions.

| **File**     | **Description**                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------|
| BabyFace.dcm | Ultrasound image (640x480 pixels)                                                                         |
| BoneScrw.dcm | CR image (2048x2577 pixels)                                                                               |
| Carotid.dcm  | Ultrasound image (640x480 pixels)                                                                         |
| EyeCLens.dcm | (640x560 pixels)                                                                                          |
| EyeClot.dcm  | (640x560 pixels)                                                                                          |
| EyeLens.dcm  | (640x560 pixels)                                                                                          |
| EyeSttch.dcm | (640x560 pixels)                                                                                          |
| Fillings.dcm | IO image (811x644 pixels)                                                                                 |
| GoldGate.dcm | Picture of the Golden Gate Bridge in San Francisco, labeled as modality type OT (other) (640x480 pixels). |
| Implant.dcm  | IO image (811x644 pixels)                                                                                 |
| PaceMkr.dcm  | CR image (1716x1910 pixels)                                                                               |
| Retina.dcm   | (640x480 pixels)                                                                                          |
| Roots.dcm    | IO image (811x644 pixels)                                                                                 |
| Skull.dcm    | CR mage (2048x2577 pixels)                                                                                |
| Spine.dcm    | CR image (2048x2495 pixels)                                                                               |
| test.txt_new | Sample command file, used for modifying information in image headers.                                     |

###### Sample HL7 Data Streams

The following sample HL7 streams are available.

| **File**      | **Description**   |
|---------------|-------------------|
| Baltimore.gbl | Small data set    |
| Boston.gbl    | Large data set    |

##### VistARad Workstation Files

Files that are installed on a VistARad workstation are listed below. Files are grouped by folder.

**Note** —the folder locations are different for Windows 7 and Windows XP. Each of the respective folder locations are noted for each of the files listed below.

Windows 7 – **C:\Users\Public\Desktop**

Windows XP – **C:\Documents and Settings\All Users\Desktop**

| **File**              | **Description**   |
|-----------------------|-------------------|
| MAG_VistARad_Patch133 | desktop shortcut  |

Windows 7 – **C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VistA Imaging Programs**

Windows XP – **C:\Documents and Settings\All Users\Start Menu\Programs\VistA Imaging Programs**

| **File**              | **Description**     |
|-----------------------|---------------------|
| MAG_VistARad_Patch133 | start menu shortcut |

Windows 7 – **C:\Program Files (x86)\Vista\Imaging\MAG\_VistARad**

Windows XP – **C:\Program Files\Vista\Imaging\MAG\_VistARad**

| **File**              | **Description**                                                                                                                                                                                                                                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bapi32_65_5.dll       | DLL for Broker ActiveX control; As part of the VistA Imaging SSOi effort, we will be upgrading this library and BDK, (expected version XWB*1.1*65 currently in development and beta testing), which has built-in integration to the IAM SSOi Secure Token Server (STS) authentication model including PIV/PIN prompt(s). |
| CCMBroker.dll         | core DLL                                                                                                                                                                                                                                                                                                                 |
| DimFileX.ocx          | DLL for Dome ActiveX control                                                                                                                                                                                                                                                                                             |
| Dimpl8.dll            | DLL for Dome ActiveX control                                                                                                                                                                                                                                                                                             |
| DimplX.ocx            | DLL for Dome ActiveX control                                                                                                                                                                                                                                                                                             |
| DXShared.dll          | DLL for Dome ActiveX control                                                                                                                                                                                                                                                                                             |
| FreeImage.dll         | DLL for image processing                                                                                                                                                                                                                                                                                                 |
| Launcher.exe          | utility executable to support monitored site auto-login function                                                                                                                                                                                                                                                         |
| LayoutSelect.dll      | VistARad core functionality DLL (core DLL)                                                                                                                                                                                                                                                                               |
| MAG_Vistarad.exe      | VistARad main executable file                                                                                                                                                                                                                                                                                            |
| MAG_Vistarad_Util.exe | VistARad teaching file support executable                                                                                                                                                                                                                                                                                |
| RPCBrokerCom.dll      | DLL for Broker ActiveX control                                                                                                                                                                                                                                                                                           |
| RpcDbAccessCom.dll    | core DLL                                                                                                                                                                                                                                                                                                                 |
| SliceCalc.dll         | core DLL                                                                                                                                                                                                                                                                                                                 |
| TargaFile.dll         | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_CaseManager.dll    | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_DelphiUtils.dll    | DLL for password decryption to gain access to image share                                                                                                                                                                                                                                                                |
| VA_DICOM.dll          | DLL for accessing DICOM files                                                                                                                                                                                                                                                                                            |
| VA_DxShared.dll       | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_GridCtrl.dll       | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_HPModule.dll       | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_ImgLdrCtrl.dll     | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_Manager.dll        | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_Shared.dll         | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_StackViewCtrl.dll  | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_TeachingFiles.dll  | core DLL                                                                                                                                                                                                                                                                                                                 |
| VA_Vistarad.dll       | core DLL                                                                                                                                                                                                                                                                                                                 |
| VergenceContextor.dll | DLL to support context management                                                                                                                                                                                                                                                                                        |
| VIXBroker.dll         | DLL for VistA Imaging Exchange broker                                                                                                                                                                                                                                                                                    |

### Windows 7 – C:\Program Files (x86)\Vista\Imaging\MAG\_VistARad\Help

Windows XP **– C:\Program Files\Vista\Imaging\MAG\_VistARad\Help**

| **File**                    | **Description**                     |
|-----------------------------|-------------------------------------|
| MAG_VistARad_User_Guide.pdf | VistARad help--user guide           |
| MAG_vrad_QSG.pdf            | VistARad help--quick start guide    |
| MAG_Vrad_Quick_Ref.pdf      | VistARad help--quick reference card |
| MAG_vrad_Shortcuts.pdf      | VistARad help--keyboard shortcuts   |

Windows 7 – **C:\ProgramData\VistA\Imaging\MAG\_VistARad\Log**

Windows XP – **C:\Documents and Settings\All Users\Application Data\VistA\Imaging\MAG\_VistARad\Log**

| **File**                                | **Description**    |
|-----------------------------------------|--------------------|
| MAG_VistARad_mmddyyyy_hhmmss_Lognnn.txt | VistARad log files |

Windows 7 – **C:\ProgramData\VistA\Imaging\MAG\_VistARad\Config**

Windows XP – **C:\Documents and Settings\All Users\Application Data\VistA\Imaging\MAG\_VistARad\Config**

| **File**                   | **Description**                            |
|----------------------------|--------------------------------------------|
| HPConfig.xml               | used for internal reference                |
| MAG_Dicom_Attributes.lst   | used for internal reference                |
| Mag_DicomTags.txt          | used for internal reference                |
| MAG_Special_Attributes.lst | used for internal reference                |
| Mag_statusdatasettings.txt | used for internal reference                |
| MAGJ.ini                   | VistARad settings                          |
| modality.txt               | used for internal reference                |
| radlextree.xml             | internally used for Teaching Files feature |
| template.dcm               | internally used to create DICOM files      |

Redistributable packages for necessary runtimes (typically installed in **C:\WINDOWS\system32**

and/or **C:\WINDOWS\WinSxS** )

| Microsoft OLE 2.40 for Windows NT(TM) and Windows 95(TM) Operating Systems   |
|------------------------------------------------------------------------------|
| Visual C++ 8.0 ATL (x86) WinSXS MSM                                          |
| Visual C++ 8.0 CRT (x86) WinSXS MSM                                          |
| Visual C++ 8.0 MFC.Policy (x86) WinSXS MSM                                   |
| Visual C++ 8.0 MFC (x86) WinSXS MSM                                          |
| Microsoft GDI+                                                               |
| Microsoft Visual C++ 2005 SP1 Redistributable Package MFC Update (x86)       |
| Windows Installer 3.1 (x86)                                                  |

##### MAG\_Decompressor Files

The following files are installed only on systems that are recipients of routed files that use compression. For more information, refer to the *Routing User Guide* .

Mag\_Decompressor files are installed in: C:\Program Files\VistA\Imaging\MAG\_Decompressor

awj2k.dll (not distributed by VistA Imaging; purchased from Aware Inc.) MAG\_Decompressor.exe (distributed by Imaging)

##### Storage Site Utilities

The following are maintenance utilities:

- MagUtility used for various maintenance tasks related to Tier 1, database, and Tier 2
- MagDexter used to provide jukebox platter reports for use with the new MagKat utility
- MagKat, a database maintenance tool used to backfill specific fields in the IMAGE file (#2005).

For details, see the *Storage Utilities User Manual* .

##### VIX Files

For a list of the files installed for the VIX (VistA Imaging Exchange) service, see the VIX Reference chapter in the *VIX Administrator’s Guide* .

##### DICOM Importer II Client Files

The following files are installed on workstations on which the DICOM Importer II client is installed:

- **..\logs\log.txt**
- **Dicom.dll**
- **DicomImporter.Common.dll**
- **DicomImporter.DataSources.dll**
- **DICOMImporter.unity.config**
- **DicomImporter.ViewModels.dll**
- **DicomImporter.Views.dll**
- **ImagingClient.Infrastructure.dll**
- **ImagingShell.exe**
- **ImagingShell.exe.config**
- **log4net.dll**
- **log4net.xml**
- **MAG\_DICOM\_Importer\_II\_User\_Manual.pdf**
- **Microsoft.Net.Http.dll**
- **Microsoft.Practices.Prism.dll**
- **Microsoft.Practices.Prism.Interactivity.dll**
- **Microsoft.Practices.Prism.Interactivity.xml**
- **Microsoft.Practices.Prism.MefExtensions.dll**
- **Microsoft.Practices.Prism.MefExtensions.xml**
- **Microsoft.Practices.Prism.UnityExtensions.dll**
- **Microsoft.Practices.Prism.UnityExtensions.xml**
- **Microsoft.Practices.Prism.xml**
- **Microsoft.Practices.ServiceLocation.dll**
- **Microsoft.Practices.ServiceLocation.xml**
- **Microsoft.Practices.Unity.Configuration.dll**
- **Microsoft.Practices.Unity.Configuration.xml**
- **Microsoft.Practices.Unity.dll**
- **Microsoft.Practices.Unity.xml**
- **NLog.dll**
- **System.Windows.Interactivity.dll**
- **System.Windows.Interactivity.xml**
- **VistaCommon.dll**
- **VistaCommon.XmlSerializers.dll**

### Chapter 7	VistA Imaging System M Files

***The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes*** *.*

***VA Policy states the following:***

***Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.***

All routines files and fields of the VistA Imaging package may not be altered except by the OI Technical Services (TS) staff. This software is regulated by the FDA and implements controlled procedures. The only exception is data changes made in accord with Chapter 8 of this manual.

<!-- image -->

#### 35 Introduction

The VistA Imaging System is based on the use of VA FileMan as an object-oriented database management system to store single or sequential images, and other multimedia object types.

This chapter first itemizes the various files that are used by the Imaging System (Clinical Capture/Display, Background Processor, and VistARad) and then describes how to obtain more detailed information about the files. Some of the files are used on the DICOM Image and Text Gateways and will reside on those systems and not on the VistA hospital system.

#### 36 VA FileMan Files that are Part of the VistA Imaging System

##### VA FileMan Files

|   **File** | **Name**                               | **Stored in**                     |
|------------|----------------------------------------|-----------------------------------|
|    2005    | IMAGE                                  | ^MAG(2005,D0,...                  |
|    2005.01 | -->EXPORT LOCATION                     | -->5,D1,...                       |
|    2005.01 | -->ROUTING TIMESTAMP                   | -->4,D1,...                       |
|    2005.01 | -->LONG DESCRIPTION                    | -->3,D1,...                       |
|    2005.01 | -->ROUTING LOG                         | -->6,D1,...                       |
|    2005.04 | -->OBJECT GROUP                        | -->1,D1,...                       |
|    2005.21 | --> PRESENTATION STATE                 | -->210,D1,...                     |
|    2005    | IMAGING STUDY                          | ^MAG(2005.001,D0,...              |
|    2005    | IMAGING ANNOTATION FILE                | ^MAG(2005.002,D0,...              |
|    2005.02 | OBJECT TYPE                            | ^MAG(2005.02,D0,...               |
|    2005.21 | -->ACTIONS                             | -->1,D1,...                       |
|    2005.24 | -->CHILD CLASS                         | -->3,D1,...                       |
|    2005.02 | IMAGE FILE TYPES                       | ^MAG(2005.021,D0,...              |
|    2005.03 | PARENT DATA FILE                       | ^MAG(2005.03,D0,...               |
|    2005.1  | IMAGE AUDIT                            | ^MAG(2005.1,D0,...                |
|    2005.11 | -->EXPORT LOCATION                     | -->5,D1,...                       |
|    2005.11 | -->ROUTING TIMESTAMP                   | -->4,D1,...                       |
|    2005.11 | -->LONG DESCRIPTION                    | -->3,D1,...                       |
|    2005.11 | --> ROUTING LOG                        | -->6,D1,...                       |
|    2005.14 | -->OBJECT GROUP                        | -->1,D1,...                       |
|    2005.2  | NETWORK LOCATION                       | ^MAG(2005.2,D0,...                |
|    2005.2  | -->EMAIL                               | -->5,D1,...                       |
|    2005.4  | IMAGE HISTOLOGICAL STAIN               | ^MAG(2005.4,D0,...                |
|    2005.41 | MICROSCOPIC OBJECTIVE                  | ^MAG(2005.41,D0,...               |
|    2005.6  | IMAGING PATIENT REFERENCE              | ^MAGV(2005.6,D0,...               |
|    2005.61 | IMAGING PROCEDURE REFERENCE            | ^MAGV(2005.61,D0,...              |
|    2005.62 | IMAGE STUDY                            | ^MAGV(2005.62,D0,...              |
|    2005.63 | IMAGE SERIES                           | ^MAGV(2005.63,D0,...              |
|    2005.64 | IMAGE SOP INSTANCE                     | ^MAGV(2005.64,D0,...              |
|    2005.65 | IMAGE INSTANCE FILE                    | ^MAGV(2005.65,D0,...              |
|    2005.66 | IMAGING DUPLICATE UID LOG              | ^MAGV(2005.66,DO,...              |
|    2005.71 | IMAGING DICOM FIELDS                   | ^MAG(2005.71,D0,...               |
|    2005.71 | MODULE                                 | -->”M”,D1,                        |
|    2005.71 | ELEMENT TAG                            | --> “E”,D2,                       |
|    2005.8  | IMAGING SERVICE INSTITUTION            | ^MAGV(2005.8,DO,...               |
|    2005.81 | MAG DESCRIPTIVE CATEGORIES             | ^MAG(2005.81,D0,...               |
|    2005.82 | IMAGE INDEX FOR CLASS                  | ^MAG(2005.82,D0,...               |
|    2005.83 | IMAGE INDEX FOR TYPES                  | ^MAG(2005.83,D0,...               |
|    2005.84 | IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY | ^MAG(2005.84,D0,...               |
|    2005.85 | IMAGE INDEX FOR PROCEDURE/EVENT        | ^MAG(2005.85,D0,...               |
|    2005.85 | --> SPECIALTY                          | --> 1,D1,...                      |
|    2005.86 | IMAGE ACTIONS                          | ^MAG(2005.86.D0,...               |
|    2005.87 | -->TYPE                                | -->2,D1,...                       |
|    2005.87 | IMAGE LIST FILTERS                     | ^MAG(2005.87,D0,...               |
|    2006.91 | DICOM GATEWAY INSTRUMENT DICTIONARY    | ^MAGDICOM(2006.911,D0...          |
|    2006.91 | DICOM GATEWAY MODALITY DICTIONARY      | ^MAGDICOM(2006.912,D0...          |
|    2006.91 | ARTIFACT KEYLIST                       | ^MAGV(2006.913,D0...              |
|    2006.91 | RETENTION POLICY                       | ^MAGV(2006.914,D0...              |
|    2006.91 | ARTIFACT DESCRIPTOR                    | ^MAGV(2006.915,D0...              |
|    2006.92 | ARTIFACT                               | ^MAGV(2006.916,D0...              |
|    2006.92 | STORAGE PROVIDER                       | ^MAGV(2006.917,D0...              |
|    2006.92 | ARTIFACT INSTANCE                      | ^MAGV(2006.918,D0...              |
|    2006.92 | MAGV GATEWAY CONFIGURATION             | ^MAGV(2006.9191,D0...             |
|    2006.92 | DICOM AE SECURITY MATRIX               | ^MAGV(2006.9192,D0,...            |
|    2006.92 | IMAGING APPLICATION SERVICE            | ^MAGV(2006.9193,D0,...            |
|    2006.92 | ARTIFACT RETENTION POLICY              | ^MAGV(2006.921,D0,...             |
|    2006.92 | RETENTION POLICY FULFILLMENT           | ^MAGV(2006.922,D0,...             |
|    2006.92 | RETENTION POLICY STORAGE PROVIDER MAP  | ^MAGV(2006.923,D0,...             |
|    2006.92 | STORAGE PROVIDER AVAILABILITY          | ^MAGV(2006.924,D0,...             |
|    2006.92 | TRANSFER STATISTICS                    | ^MAGV(2006.925,D0,...             |
|    2006.93 | STORAGE TRANSACTION                    | ^MAGV(2006.926,D0,...             |
|    2006.93 | QUEUE                                  | ^MAGV(2006.927,D0,...             |
|    2006.93 | QUEUE MESSAGE                          | ^MAGV(2006.928,D0,...             |
|    2006.93 | IMAGING EVENT AUDIT LOG                | ^MAGV(2006.93,D0,...              |
|    2006.93 | IMAGING EVENT AUDITABLE ACTION         | ^MAGV(2006.931,D0,...             |
|    2006.94 | MAG WORK ITEM                          | ^MAGV(2006.941,D0,...             |
|    2006.94 | WORKLIST                               | ^MAGV(2006.9412,D0,...            |
|    2006.94 | MAG WORK ITEM STATUS                   | ^MAGV(2006.9413,D0,...            |
|    2006.94 | MAG WORK ITEM SUBTYPE                  | ^MAGV(2006.9414,D0,...            |
|    2006.94 | MAGV IMPORT STUDY LOG                  | ^MAGV(2006.9421,D0,...            |
|    2006.94 | MAGV IMPORT MEDIA LOG                  | ^MAGV(2006.9422,D0,...            |
|    2005.88 | MAG REASON FILE                        | ^MAG(2005.88                      |
|    2005.99 | IMAGE INDEX FOR BODY PART              | ^MAG(2005.99,D0,…                 |
|    2006.03 | IMAGE BACKGROUND QUEUE                 | ^MAGQUEUE(2006.03,D0,...          |
|    2006.03 | IMAGE BACKGROUND QUEUE POINTER         | ^MAGQUEUE(2006.031,D0,...         |
|    2006.03 | OFFLINE IMAGES                         | ^MAGQUEUE(2006.033,D0,...         |
|    2006.03 | IMPORT QUEUE                           | ^MAG(2006.034,D0,...              |
|    2006.03 | -->IMAGE DATA                          | -->1,D1,...                       |
|    2006.04 | SEND QUEUE                             | ^MAGQUEUE(2006.035,D0,...         |
|    2006.04 | ROUTING STATISTICS                     | ^MAGQUEUE(2006.036,D0,...         |
|    2006.04 | -->DETAILS                             | -->1,D1,...                       |
|    2006.04 | ACQUISITION DEVICE                     | ^MAG(2006.04,D0,...               |
|    2006.04 | ACQUISITION SESSION                    | ^MAG(2007.041,D0,...              |
|    2006.1  | IMAGING SITE PARAMETERS                | ^MAG(2006.1,D0,...                |
|    2006.11 | -->MULTI NAMESPACE                     | -->4,D1,...                       |
|    2006.11 | -->FILE TYPES                          | -->2,D1,...                       |
|    2006.12 | --> ASSOCIATED INSTITUTIONS            | --> INSTS,D1,...                  |
|    2006.15 | DICOM UID ROOT                         | ^MAG(2006.15,D0,…                 |
|    2006.17 | --> BP MAIL MESSAGE                    | -->6,D1,...                       |
|    2006.17 | -->--> Mail Group                      | -->1,D2,...                       |
|    2006.17 | -->--> MESSAGE RECIPIENTS              | -->3,D2,...                       |
|    2006.17 | -->--> SECURITY KEYS                   | -->4,D2,...                       |
|    2006.17 | MUSE VERSIONS                          | ^MAG(2006.17,D0,...               |
|    2006.17 | MUSE TEST TYPES                        | ^MAG(2006.171,D0,…                |
|    2006.17 | MUSE FORMAT TABLE                      | ^MAG(2006.172,D0,…                |
|    2006.18 | IMAGING USER PREFERENCE                | ^MAG(2006.18,D0,...               |
|    2006.19 | -->PATIENT LIST                        | -->”PATLIST”,D1,...               |
|    2006.19 | IMAGING USERS                          | ^MAG(2006.19,D0,...               |
|    2006.19 | -->ADDITIONAL NAMESPACE                | -->1,D1,...                       |
|    2006.5  | PACS MESSAGE                           | ^MAGDHL7(2006.5,D0,...            |
|    2006.5  | -->MESSAGE SEGMENTS                    | -->1,D1,...                       |
|    2006.51 | DICOM DATA ELEMENT DICTIONARY          | ^MAGDICOM(2006.51,D0,...          |
|    2006.51 | -->ENUMERATED VALUE                    | -->1,D1,...                       |
|    2006.51 | DIAGNOSTIC INFO FIELD                  | ^MAGDICOM(2006.511,D0,...         |
|    2006.51 | -->TAG                                 | -->1,D1,...                       |
|    2006.52 | DICOM MESSAGE TEMPLATE DICTIONARY      | ^MAGDICOM(2006.52,D0,...          |
|    2006.52 | -->MESSAGE                             | -->1,D1,...                       |
|    2006.53 | DICOM UID DICTIONARY                   | ^MAGDICOM(2006.53,D0,...          |
|    2006.53 | -->UID                                 | -->1,D1,...                       |
|    2006.53 | EXTENDED SOP NEGOTIATION               | ^MAGDICOM(2006.531,D0,..          |
|    2006.53 | DICOM SOP CLASS                        | ^MAG(2006.532,D0,...              |
|    2006.54 | DICOM UID SPECIFIC ACTION              | ^MAGDICOM(2006.539,D0,...         |
|    2006.54 | -->PURPOSE                             | -->1,...                          |
|    2006.54 | PDU TYPE                               | ^MAGDICOM(2006.54,D0,...          |
|    2006.55 | DICOM WORKLIST PATIENT                 | ^MAGDWLST(2006.55,D0,...          |
|    2006.55 | -->PATIENT                             | -->1,D1,...                       |
|    2006.55 | -->-->MEDICAL ALERT                    | -->-->1,D2,...                    |
|    2006.56 | DICOM WORKLIST STUDY                   | ^MAGDWLST(2006.56,D0,...          |
|    2006.56 | -->STUDY                               | -->1,D1,...                       |
|    2006.56 | -->-->PATIENT HISTORY                  | -->-->2,D2,...                    |
|    2006.56 | -->-->APPOINTMENT SCHEDULE             | -->-->1,D2,...                    |
|    2006.56 | DICOM GATEWAY PARAMETER                | ^MAGDICOM(2006.563,D0,...         |
|    2006.56 | -->DATA PATH                           | -->“DATA PATH”,D1...              |
|    2006.56 | -->PROFILE                             | -->“PROFILE”,D1...                |
|    2006.56 | -->INSTALLATION                        | -->“INSTALL”,D1...                |
|    2006.56 | DICOM QUEUE                            | ^MAGDICOM(2006.564,D0,...         |
|    2006.56 | DICOM GATEWAY MACHINE ID               | ^MAGDICOM(2006.5641,D0,...        |
|    2006.57 | EXPORT DICOM RUN FILE                  | ^MAGDICOM(2006.565,D0,...         |
|    2006.57 | DICOM HL7 SEGMENT                      | ^MAGDICOM("HL7",D0,...            |
|    2006.57 | -->ELEMENT                             | -->1,D1,...                       |
|    2006.57 | DICOM RAW IMAGE                        | ^MAGDICOM(2006.571,D0,..          |
<!-- rpc-table -->
|    2006.57 | DICOM M2MB RPC QUEUE                   | ^MAGDINPT(2006.5711,D0,..         |
|    2006.57 | DICOM FIXED QUEUE                      | ^MAGDINPT(2006.5712,D0,..         |
|    2006.57 | DICOM UNKNOWN MODALITY                 | ^MAGDINPT(2006.5713,D0,..         |
|    2006.58 | DICOM RADIOLOGY PROCEDURE MODIFIIERS   | ^MAGDICOM(2006.5757,D0,...        |
|    2006.58 | DICOM RADIOLOGY PROCEDURES             | ^MAGDICOM(2006.5758,D0,...        |
|    2006.58 | OUTSIDE IMAGING LOCATION               | ^MAGD(2006.5759,D0,...            |
|    2006.58 | DICOM MESSAGE STATISTISTICS            | ^MAGDAUDT(2006.5761,D0,...        |
|    2006.58 | -->MESSAGE                             | -->1,D1,...                       |
|    2006.58 | DICOM INSTRUMENT STATISTICS            | ^MAGDAUDT(2006.5762,D0,...        |
|    2006.58 | -->LOCATION                            | -->1,D1,...                       |
|    2006.58 | -->-->INSTRUMENT                       | --&gt;--&gt;1,D2,...  CONSNON&gt; |
|    2006.58 | -->INSTRUMENT                          | -->1,D1,...                       |
|    2006.58 | DICOM PACS STATISTICS                  | ^MAGDAUDT(2006.5763,D0,...        |
|    2006.58 | -->ACCESSION NUMBER                    | -->1,D1,...                       |
|    2006.58 | -->-->EVENT                            | -->-->1,D2,...                    |
|    2006.58 | DICOM LOCAL INSTRUMENT STATISTICS      | ^MAGDICOM(2006.5764,D0,...        |
|    2006.58 | -->DATE                                | -->1,D1,...                       |
|    2006.58 | DICOM FIFO QUEUE                       | ^MAGDICOM(2006.577,D0,...         |
|    2006.58 | -->QUEUE LETTER                        | -->1,D1,...                       |
|    2006.58 | DICOM LOG                              | ^MAGDMLOG(D0,...                  |
|    2006.58 | -->TEXT                                | -->1,D1,...                       |
|    2006.58 | -->LINE                                | -->2,D1,...                       |
|    2006.58 | INSTRUMENT DICTIONARY                  | ^MAGDICOM(2006.581,D0,...         |
|    2006.58 | MODALITY TYPE DICTIONARY               | ^MAGDICOM(2006.582,D0,...         |
|    2006.58 | CT CONVERSION PARAMETERS               | ^MAGDICOM(2006.5821,D0,...        |
|    2006.58 | MODALITY WORKLIST DICTIONARY           | ^MAGDICOM(2006.583,D0,...         |
|    2006.58 | DICOM HEALTHCARE PROVIDER SERVICE      | ^MAGDICOM(2006.5831,D0,...        |
|    2006.58 | DICOM GMRC TEMP LIST                   | ^MAGDICOM(2006.5839,D0,...        |
|    2006.58 | TCP/IP PROVIDER PORT LIST              | ^MAGDICOM(2006.584,D0,...         |
|    2006.58 | TELEREADER ACQUISITION SERVICE         | ^MAG(2006.5841,D0,...             |
|    2006.58 | TELEREADER ACQUISITION SITE            | ^MAG(2006.5842,D0,...             |
|    2006.58 | TELEREADER READER                      | ^MAG(2006.5843,D0,...             |
|    2006.58 | TELEREADER READ/UNREAD LIST            | ^MAG(2006.5849,D0,...             |
|    2006.59 | USER APPLICATION                       | ^MAGDICOM(2006.585,D0,...         |
|    2006.59 | -->SOP CLASS                           | -->1,D1,...                       |
|    2006.59 | -->-->TRANSFER SYNTAX                  | -->-->1,D2,...                    |
|    2006.59 | PROVIDER APPLICATION                   | ^MAGDICOM(2006.586,D0,...         |
|    2006.59 | -->SOP                                 | -->1,D1,...                       |
|    2006.59 | -->-->TRANSFER SYNTAX UID              | -->-->1,D2,...                    |
|    2006.59 | DICOM TRANSMIT DESTINATION             | ^MAG(2006, 587,...                |
|    2006.59 | APPLICATION ENTITY TITLE               | ^MAGDICOM(2006.588,D0,...         |
|    2006.59 | ROUTING RULE                           | ^MAGDICOM(2006.59,D0,...          |
|    2006.59 | -->RAW TEXT                            | -->1,D1,...                       |
|    2006.59 | -->ACTION                              | -->ACTION,D1,...                  |
|    2006.59 | --> -->PARAMETER                       | --> -->1,D2,...                   |
|    2006.59 | -->CONDITION                           | --> -->1,D2,...                   |
|    2006.59 | --> -->TIMEFRAME                       | --> -->1,D2,...                   |
|    2006.59 | ROUTE LOAD BALANCE                     | ^MAGRT(2006.5906,D0,...           |
|    2006.59 | -->PARENT                              | -->1,D1,...                       |
|    2006.6  | ACTION QUEUE STATUS                    | ^MAGDICOM(2006.596,D0,...         |
|    2006.6  | -->THREAD                              | -->1,D1,...                       |
|    2006.6  | DICOM ERROR MESSAGE QUEUE              | ^MAGD(2006.598,D0,...             |
|    2006.6  | DICOM Error Log                        | ^MAGD(2006.599,D0,...             |
|    2006.62 | MAG CT PARAMETER                       | ^MAG(2006.621,D0,...              |
|    2006.62 | MAG CR PARAMETER                       | ^MAG(2006.623,D0,...              |
|    2006.63 | MAG RAD LIST DATA ELEMENTS             | ^MAG(2006.63,D0,...               |
|    2006.63 | MAG RAD LISTS DEFINITION               | ^MAG(2006.631,D0,...              |
|    2006.63 | -->COLUMNS                             | -->1,D1,...                       |
|    2006.63 | -->SORT                                | -->2,D1,...                       |
|    2006.63 | MAGJ ZLIST SEARCH FILE                 | ^MAG(2006.634,D0,...              |
|    2006.65 | MAG RAD PRIOR EXAM LOGIC               | ^MAG(2006.65,D0,...               |
|    2006.66 | -->PRIOR CASE MATCHING CPT GROUP       | -->1,D1,...                       |
|    2006.67 | MAG RAD CPT MATCHING                   | ^MAG(2006.67,D0,...               |
|    2006.67 | -->BODY PART                           | -->1,...                          |
|    2006.67 | -->MODALITY                            | -->2,...                          |
|    2006.68 | MAGJ USER DATA                         | ^MAG(2006.68,D0,...               |
|    2006.68 | -->VR-WS                               | -->VR-WS,D1,...                   |
|    2006.68 | -->-->DATA                             | -->-->VR-WS,D1,1,...              |
|    2006.68 | -->-->KEYS                             | -->-->VR-WS,D1,2,...              |
|    2006.68 | -->VR-HP                               | -->VR-HP...                       |
|    2006.68 | -->-->DATA                             | -->-->VR-HP,D1,1,...              |
|    2006.68 | -->-->KEYS                             | -->-->VR-HP,D1,2,...              |
|    2006.69 | MAG VISTARAD SITE PARAMETERS FILE      | ^MAG(2006.69,D0,...               |
|    2006.8  | BP WORKSTATIONS                        | ^MAG(2006.8,D0,...                |
|    2006.81 | IMAGING WINDOWS WORKSTATIONS           | ^MAG(2006.81,D0,...               |
|    2006.82 | IMAGING WINDOWS SESSIONS               | ^MAG(2006.82,D0,...               |
|    2006.82 | -->ACTIONS                             | -->"ACT",D1,...                   |
|    2006.82 | -->ERRORS                              | -->"ERR",D1,...                   |
|    2006.83 | DICOM WORKSTATION                      | ^MAG(2006.83,D0,...               |
|    2006.87 | DICOM GATEWAY INFORMATION              | ^MAG(2006.87,D0,...               |
|    2006.95 | IMAGE ACCESS LOG                       | ^MAG(2006.95,D0,...               |
|    2006.96 | IMAGE INDEX CONVERSION                 | ^MAGIXCVT (2006.96,D0...          |
|    2006.96 | MULTI IMAGE PRINT FILE                 | ^MAG(2006.961,                    |
|    2006.96 | -->IMAGES PRINTED SUB- FILE            | ^MAG(2006.961,D0,"IMG",           |

##### More Detailed Information

More detailed information about these files can be obtained using the FileMan option LIST FILE ATTRIBUTES. The Data Dictionaries are considered part of the online documentation for this software application. It may be necessary to print the Data Dictionaries in order to support the package at your site.

The Data Dictionaries for VistA Imaging files may be printed using the VA FileManager’s option LIST FILE ATTRIBUTES under the DATA DICTIONARY UTILITIES menu as follows:

<!-- image -->

The Data Dictionary will now print on the user's specified device.

#### 37 Input Templates

The distribution contains the following input templates:

FILE #2005 MAG IMAGE INDEX EDIT FILE #2006.1: MAG PURGE PARAMETERS FILE #2006.1: MAG SITE PARAMETERS FILE #2006.1: MAG MUSE PARAMETERS

FILE #2005.2: MAG ENTER/EDIT NETWORK LOC FILE #2005.2: MAG ENTER/EDIT MUSE NETWORK FILE #2005.575: MAGD-ENTRY

FILE #2005.575: MAGD-UPDT

FILE #2005.88: MAG REASON EDIT

FILE #2006.8: MAG EDIT BACKGRND WORKSTA FILE #2006.631: MAGJ LIST EDIT

FILE #2006.65: MAGJ PRIOR EDIT

##### Further Information

Every individual object (i.e., an image, audio clip, waveform, or scanned document) is an entry in the IMAGE file (#2005), where the object's attributes are managed. In addition, three auxiliary files are used:

- Object Type
- Network Location
- Parent Data

The objects are then related to the patient's VistA text data (medicine, surgery, laboratory, radiology reports or progress notes) through the use of pointers, both forward from the VistA PACKAGE file (#9.4) to the IMAGE file (#2005), and backwards from the IMAGE file (#2005) to the VistA PACKAGE file (#9.4). Software allows new objects to be added and displayed.

Several additional files are used by the system. These include:

- IMAGING WINDOWS WORKSTATIONS file (#2006.81), which contains information about every workstation on the network.
- IMAGE HISTOLOGICAL STAIN file (#2005.4), and the MICROSCOPIC OBJECTIVE file

(#2005.41) used by anatomic pathology.

- IMAGING SITE PARAMETERS file (#2006.1).
- Background Queue files, which are necessary to manage abstract creation, automatic file migration (movement of image/object files between optical disk jukebox and magnetic disk), file copies.
- IMAGE ACCESS LOG file (#2006.95) used to track system utilization.
- User preferences files, which store personal preferences for the software configuration of the workstation.
- IMAGE LIST FILTERS file (#2005.87), which stores personal filters for each user, and public filters for all users.
- IMAGE FILE TYPES file (#2005.021), which lists all image formats that VistA Imaging supports.
- IMAGING ANNOTATION file (#2005.002), which stores annotation information that is associated with an image.
- Parameters that are specific for each individual DICOM Gateway Computer.
- Master files that drive the operation of the DICOM Gateway.
- Modality Worklist file that contains the scheduled activities for the various modalities that acquire images.
- Incoming Images.
- Images that need manual intervention before they can be entered into the VistA HIS.
#### 38 File List

The VistA Imaging System files are in the 2005 through the 2006.999 numbering space. Full file and field documented attributes on any Imaging files can be obtained using the LIST FILE ATTRIBUTES sub-menu option located in the ‘Data Dictionary Utilities menu.

<!-- image -->

#### 39 Files Introduced in MAG*3.0*34

The new data structure introduced in MAG*3.0*34 includes these files:

- IMAGING PATIENT REFERENCE file (#2005.6)

The file contains information about each patient with which imaging procedures and studies are associated within VistA.

- IMAGING PROCEDURE REFERENCE file (#2005.61)

The file contains information about each procedure corresponding to an entry in the IMAGING PATIENT REFERENCE file (#2005.6).

- IMAGE STUDY file (#2005.62)

The file contains information about each study corresponding to an entry in the IMAGING PROCEDURE REFERENCE file (#2005.61).

- IMAGE SERIES file (#2005.63)

The file contains information about each series corresponding to an entry in the IMAGE STUDY file (#2005.62).

- IMAGE SOP INSTANCE file (#2005.64)

The file contains information about each SOP instance in the IMAGE SERIES file (#2005.63).

- IMAGE INSTANCE FILE file (#2005.65)

The file contains information about each physical file instance corresponding to an entry on the IMAGE SOP INSTANCE file (#2005.64).

- IMAGING DUPLICATE UID LOG file (#2005.66)

The file contains information about duplicate UIDs.

- IMAGING SERVICE INSTITUTION file (#2005.8)

The file contains entries indicating the Imaging institution associated with an action performed on an Imaging file entry.

- DICOM GATEWAY INSTRUMENT DICTIONARY file (#2006.911)

The file contains information about the instruments that communicate with the DICOM Gateway.

- DICOM GATEWAY MODALITY DICTIONARY file (#2006.912)

The file contains information about the various types of image acquisition devices that are present at a site. Note that a modality is a class of devices; an instrument is a specific device or an instance of such a class.

- ARTIFACT KEYLIST file (#2006.913)

The file includes information that allows clients of the storage system, such as display clients and the Query/Retrieve application to retrieve artifacts (images) stored in the VistA system at the site.

- RETENTION POLICY file (#2006.914)

The file contains information about the various retention policies available to the storage system. Retention policies can be user-definable or business.

- ARTIFACT DESCRIPTOR file (#2006.915)

The file acts as the entry point into the storage system. It holds information about a particular type of artifact (such as the artifact type MedicalImage, which is an image in DICOM format) and maps this type of artifact to its intrinsic retention policy. The file also stores the file extension that is used for files of the given type. Artifact descriptors records are created when the patch is installed. Users cannot delete or modify these records or create new ones.

- ARTIFACT file (#2006.916)

The file holds records with information about the artifact: CRC, size, who the artifact was created by, a link back to the artifact descriptor, and so on. (An artifact is an object that the storage system stores, such as an image, a text file, a report, an abstract.)

- STORAGE PROVIDER file (#2006.917)

The file includes information about the devices used at the site. It contains one record for each device. For example, if there is a consolidated site with a RAID in place A, a RAID in place B, and an archive in place B, there would be 3 entries in the file. The information in the file is used to determine whether a particular configuration is valid at configuration and at runtime.

- ARTIFACT INSTANCE file (#2006.918)

The file holds the details of a particular instance of the binary data for an artifact. Each record is owned by a specific provider and has a reference to its parent artifact record, as well as a URL that the given provider can understand and that can be used to return a stream for the artifact. The file also includes properties related to when the file was created, when it was last accessed, and so on.

- MAGV GATEWAY CONFIGURATION file (#2006.9191)

The file contains configuration parameters of the DICOM Gateways connected to the VistA system at the specific site.

- DICOM AE SECURITY MATRIX file (#2006.9192)

The file contains a list of the devices (application entities) that can connect to the VistA system and their parameters, which include the type of access they have to the system (defined as the DICOM service and role).

- IMAGING APPLICATION SERVICE file (#2006.9193)

The file contains VistA Imaging applications or services, such as HDIG, DICOM Importer II, and VI DICOM Storage SCP.

- ARTIFACT RETENTION POLICY file (#2006.921)

The file maps an artifact to the set of retention policies currently and also historically in effect for that artifact.

- RETENTION POLICY FULFILLMENT file (#2006.922)

The file maps a running history of how particular retention policies caused artifacts to be written to specific storage providers. It is also used by asynchronous archiving to determine which retention policies have not yet been satisfied and which storage providers still need to be written to.

- RETENTION POLICY STORAGE PROVIDER MAP file (#2006.923)

The file maps retention policies, through an acquisition location, to the storage providers that should be used to satisfy the retention policies. It also contains a flag indicating whether a particular storage provider should be called synchronously or asynchronously.

- STORAGE PROVIDER AVAILABILITY file (#2006.924)

The file contains information about the availability of a connection between an acquisition place and a particular storage (archive) provider. If there is a record for a particular storage provider/acquisition location pair, the connection is only available between the start and end times indicated in the record. If there is no record, the connection is always available.

- TRANSFER STATISTICS file (#2006.925)

The file contains statistics about network transfers between a storage provider and a client endpoint, including the time of day the transfer occurred, the duration of the transfer, and the size of the artifact.

- STORAGE TRANSACTION file (#2006.926)

The file records the actions for a particular artifact, such as: storing the artifact successfully in a specific storage provider; failed attempts to store the artifact in a storage provider; retrieving the artifact from a particular storage provider; failed attempts to retrieve the artifact from a storage provider.

- QUEUE file (#2006.927)

The file is a list of Queues (queue types). It contains the queue for asynchronous storage requests, the queue for failed asynchronous storage requests, the Abstract Maker queue and the queue for sending email notifications.

- QUEUE MESSAGE file (#2006.928)

The file stores the messages for the requests for all queues defined in the QUEUE file. Each record in the file contains information about the queued request: the message itself, a reference to the queue, the priority of the request, the minimum delivery date/time, and expiration date/time of the message. The file is used by internal processes to carry out the actions for all queued requests.

- IMAGING EVENT AUDIT LOG file (#2006.93)

The file contains a list of all audited events.

- IMAGING EVENT AUDITABLE ACTION file (#2006.931)

The file contains the list of VistA Imaging events that can be audited.

- MAG WORK ITEM file (#2006.941)

The file contains a queue of work items for worklists in the WORKLIST file (#2006.9412).

- WORKLIST file (#2006.9412)

The file contains entries for worklists and their current activity status.

- MAG WORK ITEM STATUS file (#2006.9413)

This file contains work item statuses.

- MAG WORK ITEM SUBTYPE file (#2006.9414)

This file contains work item subtypes.

- MAGV IMPORT STUDY LOG file (#2006.9421)

The file contains a log of import events carried out by the DICOM Importer II at the study level. These include user and study information, and counts of the total number of series and objects imported, the number of objects that failed to import, and of the number of objects imported for each modality contained within the study. This information allows generation of reports covering importer activity for a user-specified time period.

- MAGV IMPORT MEDIA LOG file (#2006.9422)

The file holds a log of import events carried out by the DICOM Importer II at the media bundle level. A media bundle is a group of studies under a single Importer II work item. A media bundle may or may not represent a single piece of media or a single network transaction. This file includes information about media validity, the user who reconciled the associated studies, the workstation, as well as the source of the imported media.

#### 40 Sort and Print Templates

Sort and Print Templates for the IMAGING PATIENT REFERENCE File (#2005.6)

- MAGV-PAT-QUERY – This sort template enables users to retrieve study, series, image, and file information for a single patient or a range of patients, based on the value of the ENTERPRISE PATIENT ID field (#.01).
- MAGV-PAT-QUERY – This print template returns a report with the following Binformation:

Sort and Print Templates for the IMAGING PROCEDURE REFERENCE File (#2005.61)

| For each requested patient:              | Name and social security number                     |
|------------------------------------------|-----------------------------------------------------|
| For each of the patient’s procedures:    | Procedure ID                                        |
| For each study within the procedure:     | Study instance UID  Description Modalities in study |
| For each series within the study:        | Series instance UID  Description Modality           |
| For each SOP instance within the series: | SOP instance UID  SOP class UID                     |
| For each file within the SOP instance:   | Fileref                                             |

- MAGV-PROC-QUERY – This sort template enables users to retrieve study and series information for a single procedure or a range of procedures, based on the value of the PROCEDURE ID field (#.01).
- MAGV-PROC-QUERY – This print template returns a report with the following information:

Sort and Print Templates for the ARTIFACT INSTANCE File (#2006.918)

| For each requested procedure:        | Procedure ID                                        |
|--------------------------------------|-----------------------------------------------------|
| For the associated patient:          | Social security number Name  Date of birth          |
| For each study within the procedure: | Study instance UID  Description Modalities in study |
| For each study within the procedure: | Study instance UID                                  |
| For each series within the study:    | Series instance UID                                 |

- MAGV-FILEREF-QUERY – This sort template enables users to retrieve patient, study, and series information for a single file or a range of files based on the value of the FILEREF field (#6).
- MAGV-FILEREF-QUERY – This print template returns the following information:

Sort Template for the QUEUE MESSAGE File (#2006.928)

| For each requested file:             | File name                                           |
|--------------------------------------|-----------------------------------------------------|
| For the associated patient:          | Social security number Name  Sex  Date of birth     |
| For each study within the procedure: | Study instance UID Description  Modalities in study |
| For each study within the procedure: | Study instance UID                                  |
| For each series within the study:    | Series instance UID                                 |

- MAGVA-ASYNC-STORAGE-ERRORS – This sort template is for system use only. It is used by Hybrid DICOM Gateway Menu [MAGV HDIG MENU] Option Find Async Storage Request Errors [MAGVA ASYNC STORAGE ERR QURY] to store results of a query for Asynchronous Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928), and by Option List Async Storage Request Errors [MAGVA ASYNC STORAGE ERR LIST] to display information about the entries.
#### 41 File List

The VistA Imaging System files are in the 2005 through the 2006.999 numbering space. Full file and field documented attributes on any Imaging files can be obtained using the LIST FILE ATTRIBUTES sub-menu option located in the ‘Data Dictionary’ Utilities menu.

<!-- image -->

#### 42 File Security

VistA Imaging recommends no access to any Imaging files by any end-user other than IRM personnel. Please review the Security manual to get a detail listing of all FileMan protections on all Imaging files. All updating of Imaging files is done via the GUI interface or by the Imaging System Manager menu (locked by the MAG SYSTEM security key) on the VistA hospital system. However, the recommended method is to use the VistA Imaging Background Processor application (GUI).

The following imaging entity relationship diagram shows the data structures that existed before the release of MAG*3.0*34.

Imaging Entity Relationship Diagram and Detailed Information

<!-- image -->

A detailed File Diagram can be obtained using the FileMan’s menu option ‘MAP POINTER RELATIONS’.

- Select ‘DATA DICTIONARIES UTILITIES’ from the FileMan menu.
- Select ‘MAP POINTER RELATIONS’ menu option.
- Respond to the ‘PACKAGE NAME’ prompt with IMAGING.

The following imaging entity relationship diagram shows the data structures that were introduced in MAG*3.0*34. The diagram includes key fields for each table, It also shows the pointers to other data structures: the old data structures and non-VistA Imaging data tables.

Imaging Entity Relationship Diagram: Data Structures Introduced in MAG*3.0*34

<!-- image -->

A detailed and current File Diagram can be obtained using the FileMan’s menu option ‘MAP POINTER RELATIONS’.

- Select ‘DATA DICTIONARIES UTILITIES’ from the FileMan menu.
- Select ‘MAP POINTER RELATIONS’ menu option.
- Respond to the ‘PACKAGE NAME’ prompt with IMAGING.
#### 43 Global Journaling

Journaling of the VistA Imaging global is mandatory. MAG* should be journaled.

During a scheduled VistA (hospital) server downtime, it is highly recommended to coordinate any data restore activities related to the VistA Imaging System with the IRM staff.

#### 44 VistA System Outages

During a VistA System outage, DICOM Gateways will continue to provide modality worklist functionality and to capture images that are temporarily stored on the gateway. This is important to allow the radiology department to continue to perform studies. If you anticipate that the VistA System must be down, it is best to take the following steps:

- Perform all DICOM fixes before the VistA System goes down. This will free the maximum space for temporary image storage.
- During the outage, watch the gateways to be sure they still have adequate space to store images.

This page is intentionally blank.

### Chapter 8	Exported Options

#### 45 Introduction: INI File Setup and Configuration of Workstations

INI files are DOS files with the extension .ini (such as win.ini and mouse.ini) that contain initialization information for programs. Initialization refers to the parameters that control the way a program is initially launched. They also customize the application to accommodate workstation-specific characteristics, such as the type of capture hardware installed (Refer to *VistA Imaging System Installation Guide* for further details). The INI files are set up initially when the software is first installed on the workstation.

#### 46 Imaging System Manager Menu [MAG SYS MENU]

The Imaging System Manager Menu [MAG SYS MENU] contains system manager functions. Access to these menu options requires the MAG SYSTEM security key.

Menu Diagram for Imaging System Manager Menu [MAG SYS MENU]

<!-- image -->

Editing the Network Location Status should be performed by using the Network Location Manager in the Background Processor.

Imaging Database Integrity checking should be performed in the Background Processor using the Verifier application.

**Note** : You can enter **???** at the Select Imaging System Manager Menu Option prompt for a description of each menu option.

See the *Background Processor User Manual* for more information.

For detailed information about the ‘Telereader Menu …’ option, refer to the TeleReader Configuration document.

For detailed information about the “Ad hoc Enterprise Site Report” option and the “Imaging Site Reports” option, refer to Chapter 12.

##### Imaging Hl7 Messaging Maintenance [Mag Hl7 Maint]

This option contains sub-options that allow you to modify parameters relating to the transmission of HL7 ADT messages to commercial PACS (cPACS) and to select the version of HL7 order messages that should be sent from VistA Radiology to cPACS and to the VistA Text Gateway.

**Note** : If you need help with the sub-options of this option, consult the designated HL7 specialist within the IRM department at your site.

Menu Diagram for Imaging HL7 Messaging Maintenance [MAG HL7 MAINT]

<!-- image -->

###### Maintain Subscriptions to Radiology Hl7 Drivers [Magd Maint Rad Hl7 Subs]

This option allows you to select the version of HL7 order messages that should be sent from VistA Radiology to cPACS and to the VistA Text Gateway.

From the Imaging System Manager Menu, select HL7:

<!-- image -->

From the Imaging HL7 Messaging Maintenance Menu, select RHL7:

<!-- image -->

VistA Imaging first verifies that all applicable HL7 protocols are available. There are two Imaging subscriber protocols and eight Radiology event driver protocols – four for HL7 Version 2.1 messages and four for HL7 Version 2.4 messages.

<!-- image -->

VistA Imaging then asks which version of HL7 you wish to be used to generate Radiology messages. Enter 2.1 or 2.4.

<!-- image -->

If the desired HL7 version is not currently in use, VistA Imaging adjusts protocol subscriptions to cause the desired version to come into use.

<!-- image -->

If the desired HL7 version is already in use, the system will take no action.

<!-- image -->

###### Configure Ihe-Based Hl7 Adt Interface To Pacs

This option allows you to modify parameters relating to the transmission of HL7 version 2.4 ADT messages to commercial PACS (if used) and the DICOM Text Gateway.

From the Imaging System Manager Menu, select HL7:

<!-- image -->

From the Imaging HL7 Messaging Maintenance Menu, select IHE:

<!-- image -->

VistA Imaging first asks you to verify the name of the sending application and the receiving application. These are the applications in the HL7 APPLICATION PARAMETER File (#771) whose NAME Field values are associated with the entries in field 3 and 5 respectively, and whose FACILITY NAME Field values are associated with the entries in fields 4 and 6 respectively, of the Message Header (MSH) segments of the outbound HL7 messages

**Note** : This option only changes the names of the sending and receiving applications. To change the names of the sending and receiving facilities, get help from the designated HL7 specialist within the IRM department at your site.

<!-- image -->

If you wish to accept the application names that are presented, enter **N** . Otherwise, enter **Y** and enter the desired new application names at the prompts:

<!-- image -->

VistA Imaging next asks you to enter the TCP/IP address and port number of the logical link over which the outbound VistA HL7 stream will be transmitted to cPACS.

<!-- image -->

Finally, you are asked whether you wish to turn on the IHE-based PACS interface, which will transmit IHE-conformant ADT HL7 messages from VistA HIS to cPACS (if used) and to the DICOM Text Gateway.

<!-- image -->

Enter **Y** to turn the interface on or **N** to turn it off.

#### 47 Configure AE Security Matrix Settings [MAGV AE SEC MX SETTINGS]

This menu lets users edit the DICOM AE SECURITY MATRIX file (#2006.9192). The file contains a list of application entity (AE) titles: all remote devices that can connect to the local VistA system and its components. It also determines which devices can connect to the VistA system and the type of access that they are allowed (a combination of DICOM service and the DICOM role associated with this service). For example, a device that is a Service Class User (SCU) of the Storage Service Class (C-STORE) can send DICOM objects to a DICOM Gateway that is defined as a Service Class Provider (SCP) of the Storage Service Class. If a device is not listed in the DICOM AE Security Matrix, it cannot access the VistA system or its components.

VistA Imaging system administrators use the menu option Configure AE Security Matrix Settings [MAGV AE SEC MX SETTINGS] after initial installation to define the remote devices that can connect to the local VistA system and its components. They will also use the menu option to remove devices, or to change device properties.

The Configure AE Security Matrix Settings [MAGV AE SEC MX SETTINGS] menu option is accessed from the Imaging System Manager Menu [MAG SYS MENU].

<!-- image -->

For information about the AE Security Matrix and about using the Configure AE Security Matrix Settings to configure the AE Security Matrix, see the *VistA Imaging DICOM Gateway Installation Guide* .

#### 48 Delete Study by Accession Number [MAG SYS-DELETE STUDY]

This menu allows a user with the MAG DELETE key to delete studies by accession number. In the data structures introduced in MAG*3.0*34, each study has a different accession number. The Delete Study by Accession Number is useful for deleting studies from the new data structures.

For deleting studies from the old data structures, you can still use the Delete Image Group option. This option deletes all images in the group, regardless if they are in the new or in the old data structures.

The [MAG SYS-DELETE STUDY] menu option is accessed from the Imaging System Manager Menu [MAG SYS MENU].

<!-- image -->

To delete a study by accession number:

1. From the Imaging System Manager Menu, select **Delete Study by Accession Number** :
<!-- image -->
2. Enter the accession number of the study you want to delete.
<!-- image -->
3. Select a reason for deleting the study.
<!-- image -->
4. Type **Yes** to confirm you want to delete the study.
<!-- image -->

The system displays a message that the study has been deleted. The study is marked for deletion in the database. It will no longer be available for viewing, queries or any other operations.

<!-- image -->

#### 49 Enter/Edit Reason [MAG REASON EDIT]

This menu option allows adding/editing of reasons for actions performed on images (copying, printing, etc.) stored in the MAG REASON file (#2005.88). The Reason codes and definitions shown are samples only.

<!-- image -->

From the System Manager menu [MAG SYS MENU] select **Enter/edit Reason** .

<!-- image -->

At the prompt **Select MAG REASON:** enter a reason number to display an existing reason; or a **?** to display a list of all MAG REASON numbers currently stored.

<!-- image -->

A new MAG REASON is added by entering the name of a new MAG REASON at the prompt.

<!-- image -->

Because new MAG REASON codes can be created either by the national VistA team, or by local site administrators, the MAG REASON code list varies from site to site. In some cases, the same reason appears on different site lists with different code numbers. For example, the latest nationally created reason—For use in Veterans Benefits Administration claims processing, which was created as part of the VIX maintenance Patch 124—is number 16 on the list of nationally created reasons. But if a site used the 16th place in its MAG REASON code list for a local reason before Patch 124, that local reason appears as L16 on that site’s MAG REASON list, and the new national code takes the next number in line. In that hypothetical case, For use in Veterans Benefits Administration claims processing would appear as code 17 on the site’s MAG REASON list.

The national MAG Reason Code list now contains 16 codes (see table). It contained 15 reason codes before site administrators were given the capability to create local reason codes. These 15 reasons are uniform across all VistA sites.

|   **Number** | **Reason**                                                                                          | **Type**   |   **Code** |
|--------------|-----------------------------------------------------------------------------------------------------|------------|------------|
|            1 | Clinical care for the patient whose images are being downloaded                                     | CP         |          1 |
|            2 | Clinical care for other VA patients                                                                 | CP         |          2 |
|            3 | For use in approved research by VA staff                                                            | CP         |          3 |
|            4 | For approved teaching purposes by VA staff                                                          | CP         |          4 |
|            5 | For use in approved VA publications                                                                 | CP         |          5 |
|            6 | Authorized release of medical records or health information (ROI)                                   | CP         |          6 |
|            7 | Corrupt image                                                                                       | D          |          7 |
|            8 | Low quality image                                                                                   | DS         |          8 |
|            9 | Wrong case/exam/accession number                                                                    | DS         |          9 |
|           10 | Wrong note title                                                                                    | D          |         10 |
|           11 | Wrong patient                                                                                       | D          |         11 |
|           12 | Image is incorrectly included in an image group                                                     | D          |         12 |
|           13 | All images were removed from the group                                                              | D          |         13 |
|           14 | HIMS document correction When a document or image needs to have the patient or image data corrected | DS         |         14 |
|           15 | Rescinded TIU Note                                                                                  | SD         |         15 |
|           16 | For use in Veterans Benefits Administration claims processing.                                      | CP         |         16 |

**Note:** The transaction log/report lists actions on images by type and reason. For an accurate understanding of the logs from any VA site, complete the steps in the first two paragraphs of this section to retrieve a list of all MAG REASON codes currently being used at the site. Locate the MAG REASON number on the site list. Each MAG REASON number on this list is paired with the text of the reason for the action.

#### 50 MAG Client Version Report [MAG CLIENT VERSION REPORT]

Imaging Clients Version Report [MAG CLIENT VERSION REPORT]. This option prints the list of workstations and clients that need updates. When the new version of the VistA server code is distributed, those clients may continue, but they are not supported.

From the Imaging System Menu [MAG SYS MENU], enter "Imaging Site Reports" at the prompt.

<!-- image -->

At the prompt, enter "Imaging Clients Version Report".

<!-- image -->

<!-- image -->

#### 51 Imaging VistARad System Options

The VistARad System Options Menu is used to set site parameters that control VistARad’s basic behaviors and performance, to create custom exam lists, and to review and manage VistARad’s prefetch and CPT (Current Procedural Terminology) code matching capabilities.

Menu Diagram for MAGJ MAIN

<!-- image -->

#### 52 Imaging MAG WINDOWS Menu Option

The menu option MAG WINDOWS should be assigned as a secondary menu option to end-users who need access to VistA Imaging, and to all users and operators of the DICOM Gateways and Background Processor applications. This menu outlines enables:

- Access to all the RPCs used by VistA Imaging
- An automated log-on to applications experiencing service interrupted by network and host system outages
#### 53 Imaging VistARad MAGJ VISTARAD WINDOWS

The menu option MAGJ VISTARAD WINDOWS should be assigned as a secondary menu option to end-users who need access to VistA Imaging VistARad. This menu outlines all the RPCs used by VistARad.Imaging MAG JB OFFLINE Menu option

This menu option is not part of any menu and is discussed in Chapter 9 of this manual; section Removing Jukebox Media - Offline Images.

#### 54 Imaging DICOM Menu

The VistA Imaging DICOM Gateway itself does not use VA Kernel software, and as a result, does not use any Options. However, on the VistA hospital system the following menu does relate to the DICOM Gateways. See the *Imaging DICOM User Manual* for full instructions on using this menu.

Menu Diagram for MAGD DICOM MENU

<!-- image -->

#### 55 Imaging Menu Options Documentation

A full description for all of the Imaging’s VistA menu options can be obtained by using FileMan print menu option.

<!-- image -->

#### 56 Access to DICOM Gateway RPCs

The VistA system grants access to Remote Procedures based on a relation between certain menu options and the RPCs in question. The DICOM Gateway uses two classes of RPCs: those that can be called by any user of the DICOM Gateway (“view-only access”) and those that can only be called by end-users with “full access”. In order to support this distribution of privileges, the following two menu options are present in the VistA system and should be assigned to the appropriate personnel:

MAG DICOM GATEWAY VIEW MAG DICOM GATEWAY FULL

#### 57 Imaging Menu Options Documentation

A full description for all of the Imaging VistA menu options can be obtained by using the FileMan print menu option.

<!-- image -->

**Note:** The output displayed by the option, Inquire VistARad CPT Matching Set [MAGJ INQUIRE CPT MATCHING SET], has been modified to display attributes defined for the entered CPT code, and also the matching CPT code values for its related "Similar CPT" and "Modality/Body Part" combinations.

**Note:** This change as implemented does not require any KIDS component, so no new or modified Menu options will be apparent in the KIDS definition or installation files.

This page is intentionally blank.

### Chapter 9	Archiving, Purging, Verifying, and Backup

#### 58 Introduction

This chapter explains how to archive, purge, and verify VistA Imaging files and VistA Imaging FileMan entries. Image files are part of the patient’s record and must be preserved for the required number of years. Image files may be kept online indefinitely. As image files get older and have not been accessed recently, they reside on the optical disk jukeboxes where they are still accessible to users, but access is less rapid. Some sites have taken platters out of jukeboxes for shelf storage, but these are reloaded when needed by a user. The state of the images on the storage devices and their relationship (through file references) to the VistA database require periodic verification.

Most of the information in this chapter describes archiving, purging, and backup using the Background Processor and refers to the data that is stored in the data structures that were used before MAG*3.0*34 (also referred to as the “old” data structures). This data includes the SOP classes that were supported before MAG*3.0*34.

DICOM objects and studies from the SOP classes for which support was introduced in MAG*3.0*34 are stored in the data structures that were introduced in MAG*3.0*34 (also referred to as the “new” data structures). The Archiver, which is installed with the HDIG, manages the archiving and data aging in the new data structures. For information about handling processing and storage errors in the new data structures, see section *11.4 Handling Processing and Storage Errors in the New Data Structures.*

#### 59 Archiving and Purging of Image FileMan Entries

Entries in the IMAGE file (#2005) should **not** be purged or archived.

#### 60 Archiving and Purging of Image Files

##### Automatic Image File Migration

The imaging workstation stores the full-size image file on the server when the image is captured. An abstract may be created by the capture workstation, or by placing an entry in the Abstract queue. An entry is placed in the JUKEBOX queue. The background processor then copies the images to Tier 2.

After a period of time during which an image is not accessed:

1. The full-size image will be deleted from the magnetic file server. It will still be accessible to users from Tier 2.
2. Next, the abstract will be deleted from the magnetic file server. If a subsequent request is made to display the full-size image or the abstract, that file will be copied back to the magnetic file server.

Because images are stored temporarily on the magnetic servers, these are referred to as VistA magnetic cache.

##### Purging Tier 1 Shares

The Background Processor’s Purge application clears disk space within the VistA Imaging shares. This space is necessary for newly captured files from Imaging modalities and the DICOM gateways. Space is also needed for files that are copied from Tier 2 when images are viewed on Imaging display workstations.

Each file on every VistA Imaging shares is evaluated to determine if it should be purged, as follows:

- The file name must consist of the local namespace followed by the number which coincides with its IMAGE file (#2005) internal entry number. If the corresponding IMAGE file (#2005) entry does not exist, the image file is unconditionally purged from the VistA Imaging shares.
- The file location is checked against the IMAGE file (#2005) settings. If the IMAGE file (#2005) entry has no current magnetic cache pointers set for this image, then the IMAGE file (#2005) entry is updated, and the file is not purged. If no Tier 2 pointer is set, then a Tier 2 copy (JUKEBOX queue) is queued.
- If the image file in the VistA Imaging shares is not where the IMAGE file (#2005) specifies it to be, then the location pointed to by the IMAGE file (#2005) is checked. If a proper image file is found, then the redundant image will be otherwise purged.
- The image is next characterized as Patient Photo or non-Photo image for a patient by checking its image type. If so, the Photo ID/Advance Directive’s purge criteria parameters will be used in evaluating this image.
- If the image (a) is found to be at a Tier 1 location other than that specified by the IMAGE file (#2005) entry, or (b) is not found at an IMAGE file (#2005) alternate site, or (c) is confirmed of size non-zero on Tier 2, then the file will be removed from the VistA Imaging Tier 1 according to the purge criteria.
#### 61 Queue Management

Failed and unprocessed queues are purged during the install procedures of the VistA Imaging System. Using the BP Edit|Queue Manager| *Queue Type* option on the main Background Processor form, one can update and manage queue file growth. After selecting a queue type and a queue status value, a list of the queues from eldest to most current will be shown with their status. The list will end at the current queue pointer. These reflect unprocessed (nil) and failed queues.

The user has the option of requeuing, purging or saving them to a file. These records reflect requests to move files to and from Tier 2 with the exception of Abstract and Delete queues

Normally, a site would not consider requeuing jukebox-to-hard disk copies (JBTOHD queue) as these files usually reflect old requests that, for the most part, will no longer be useful. The Tier 2 copies (JUKEBOX queue) may be requeued, however, the Purge process will automatically requeue those that are not currently archived on Tier 2

Each queue task has an active queue pointer that designates the next entry to be processed. This queue pointer can be manually moved forward to begin processing at another location in the queue by using the Set Queue Partition context menu option within the BP Queue Manager. A typical situation may be when a queue entry is corrupted. Then the active queue pointer can be moved to the next entry where processing will continue with the rest of the queue entries for that task. (See the *Background Processor User Manual* for more details).

##### Server Size

- Select **View | Server Size** from the BP Queue Processor menu bar.

BP Queue Processor Server Size Submenu

<!-- image -->

This window shows the amount of total space, free space and % Server Reserve space for Tier 1 and Tier 2 shares as well as RAID Groups.

GO Vista Storage Graphs

<!-- image -->

The VistA Storage area on the Queue Processor GUI can be refreshed with the most current storage utilization statistics for RAID Groups and Tier 1 shares by clicking the buttons **Refresh Current Write Group** or **Refresh All (Tier 1 Shares)** .

##### Background Processor: Open Log Functions Log Files

New log files are created as HTML files at the beginning of every session. HTML files are viewable, printable, and searchable. By default, the BP Queue Processor log files reside in the following subdirectories:

- Queue Processor - C:\Program Files\VistA\Imaging\BackProc\log\BackProc
- Purge - C:\Program Files\VistA\Imaging\BackProc\log\purge
- Verifier - C:\Program Files\VistA\Imaging\BackProc\log\verifier

You can access these files by selecting **File | Open Log** on the BP Queue Processor menu bar and double-clicking the desired file.

**Note:** The log files can also be imported into an Excel spreadsheet.

**Important** : These files should be kept for historical/troubleshooting reasons and added to the tape backup process to safeguard the files. (See *Appendix B: Backups* in the *VistA Imaging System Installation Guide.* )

Log File Format

BP Queue Processor log files are archived as HTML files and have the year-month-day and sequence number imbedded in the file name, as shown in the right pane of the window in this example.

BP Queue Processor Log Files

<!-- image -->

If more than one log file is created on the same day, the system appends a sequence number to the file name.

###### Queue Processor Log Files

The Queue Processor produces multiple log files for a processing run. Each file contains different information.

- BackProc Log

The BackProc.log file records all activity in the Event Log section in the Queue Processor window.

BackProc.log File Records

<!-- image -->

| **Name**        | **Description**                                               |
|-----------------|---------------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed         |
| Event_Queue_Ref | Queue name and entry number and status check info             |
| Message/Path    | Description of action taken (or statistics for status checks) |

- BP Error Log

The BPError.log file records error conditions with the operating system and Broker.

BPError.log File Records

<!-- image -->

| **Name**        | **Description**                                       |
|-----------------|-------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed |
| Event_Queue_Ref | Error category                                        |
| Message/Path    | Description of error condition                        |

###### Verifier Log Files

BP Verifier produces the following types of log files. For details on each log file, see the Verifier chapter in the *Background Processor User Manual* .

- Scan Log

The Scan log file lists entries with potential file integrity problems. The log records the operational events that take place to correct a particular problem. They are used to determine if and how the Verifier corrected the faulty condition. The IENs that the Verifier could not fix are listed in the ScanError log file.

- NoArchive Log

The NoArchive log file contains image file names that are missing on the jukebox and could not be created from existing files and/or could not be found on the RAID. The Verifier examines both the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1) for missing files. The 2005.1 column shown below indicates those missing files that have been deleted and the IMAGE file (#2005) record has been moved to the IMAGE AUDIT file (#2005.1).

- ScanError Log

The ScanError log file lists problems with IENs that could not be corrected. When a Verifier scan is completed, the contents of this file are sent as a mail message to the MAG SERVER mail group.

- DFNError Log

The DFNError log file displays integrity issues with patient data.

- VerifierdebugLog

The Verifier debug information is only logged when an error occurs. After 30 errors, debug mode is turned off. By turning off debug mode, the size of the Debug Log is restricted to limit overwhelming the local hard drive with repetitive data.

###### Purge Log Files

BP Purge produces the following types of log files. For details on each log file, see the Purge chapter in the Background Processor User Manual.

- Purge Log

The Purge.html log file records the current share being purged as well as all of the successful deletions and the reason they were deleted.

- PurgeError Log

The PurgeError.html log file records the current share being purged as well as all of the files that were not deleted and the reason they were not deleted.

##### Check Status of the JBTOHD Report

1. On the Background Processor main menu, select the **View | JBTOHD Report** option.
2. Select **File | Refresh** in the report window.

JBTOHD Report

<!-- image -->

The JBTOHD queue display is sorted by the individual that queued the entry. It displays the number and types of queues. It displays the patient along with the queue Internal Entry Number (IEN) to facilitate advancing the queue pointer.

#### 62 Background Processor Configuration Tools

##### Configuring BP Servers Guidelines

- At least one BP Server must be present to perform utility functions such as copying image files to and from Imaging servers (the Tier 1 shares) and Tier 2.
- The software does not permit redundant task assignments of BP activities. For example, you cannot specify that more than one BP Server perform the JUKEBOX queue task.
- The JUKEBOX and DELETE queue tasks should run on the same BP server. If not, the DELETE queue may be processed in advance of the image being written to the Tier 2, and the DELETE queue will eventually fail. These failed queues must be re-queued.
- The IMPORT and ABSTRACT tasks must run on the same server. There will be occasional archived FULL files that do not have abstracts. If you see these ABSTRACT tasks failing, the JBTOHD task should be added to server running the IMPORT/ABSTRACT task. Please note the IMPORT can execute on a single server.
- If the Verifier and Purge are to be run on servers other than those running the Queue Processor tasks, a new BP Server must be configured for those tasks.
- When the PREFET task is added to the VistA Imaging Display workstation configuration, this activity task must be checked assigned on the BP Server configuration window in order to have these queue types processed.
- A directory can be created on the Tier 1 shares or remote storage location to archive BP log files for later reference.

###### Adding a BP Server to the VistA Imaging System

Running multiple BP servers improves performance and redundancy by allowing the distribution of tasks, and allowing queues to be quickly reassigned in the event of a failure. Therefore, it is recommended that at least two BP servers be up and running. Though the facility may choose any server to host the BP (as long as the server meets the minimum requirements), an ideal location is directly on the two Image Cluster nodes.

###### To Set Up a BP Server Application

1. From the BP Queue Processor menu bar, select **Edit | BP Servers** .

BP Server

<!-- image -->

The BP Server Parameters window enables you to create a unique server name for a server and assign tasks to that server. The properties on these servers enable you to specify the location of the log files for all applications on each BP Server and the file’s size limit (described in “ *Specifying the Log File Location and* Size” in the *BP User Manual.)*

BP Server Parameters

<!-- image -->

1. Click the **Add New BP Server** button at the bottom of the tree pane.
2. In the BP Server Add dialog box displayed, enter a logical name for the BP Server such as **BP1** .

**Note** : The name must be at least three characters in length and can contain alpha and numeric characters and must be unique. Once the name is saved, it cannot be renamed. It can only be deleted when all the tasks assigned to it are removed.

BP Server Add

<!-- image -->

If the name is not valid, an error message is displayed. You can correct the name and repeat the steps.

###### Assigning Tasks (Queues) to a BP Server

By default, no tasks are assigned to BP Servers. The tasks will need to be assigned in order for that function of the BP software to operate. You can assign tasks based on the needs of your facility. As previously mentioned, a queue name identifies the task that the Queue Processor performs. All queues are available for you to assign to a BP Server, except EVAL.

**Note** : You should assign Purge as well as the Scheduled Verify to BP Servers. These features help maintain the system’s free-space and integrity without operator intervention.

Drag and drop a task from the Unassigned Tasks in the tree pane (shown) to the server that is designated to run that task.

BP Server Parameters

<!-- image -->

**Note** : The priority of tasks running on the same server is set internally and cannot be changed. The functions of each task are:

1. JBTOHD - populates the Tier 1 shares with images that have been deleted from Tier 1 through the Purge function.
2. PREFET - populates Tier 1 with images that were requested based on VistA Imaging Display workstation configuration parameters.
3. ABSTRACT - creates ABS derivative thumbnail files from FULL/BIG files when the file type is missing on Tier 1 and Tier 2.
4. IMPORT - provides a means for external applications to archive images in the VistA Imaging environment.
5. JUKEBOX - copies images to the long-term archival storage device
6. DELETE - removes images from Tier 1.
7. GCC - exports images to a share that is external to the local VistA Imaging network.
8. PURGE – This assignment includes both the auto purge and the scheduled purge tasks. Refer to the purge section of this document for more details.
9. SCHEDULED VERIFY – automatically runs the Verifier at the assigned time to check the integrity of the Image records in VistA with the file locations on Tier 1 and Tier 2 storage. Only the most recent unchecked IENs are verified.

Click **Apply** to save the changes or **OK** to save the changes and exit.

###### Removing a BP Server from the VistA Imaging System

1. From the Queue Processor menu bar, select Edit | BP Servers.
2. In the tree pane, right-click the server name and select Delete BP Server from the popup menu displayed.

**Note** : This popup menu can also be accessed from the keyboard by using Shift + F10.

BP Servers

<!-- image -->

The selected BP Server is removed from the tree pane.

**Note** : This same name can be added later.

###### Specifying the Log File Location and Size

1. Click a BP Server name in the tree pane and select Server Properties from the popup menu displayed.

**Note** : This popup menu can also be accessed from the keyboard by using Shift + F10.

BP Servers

<!-- image -->

The BP Server Properties dialog box is displayed.

BP Server Properties

<!-- image -->

1. Enter the size in megabytes in the Log File Size field. The default log file size limit is 2 MB.
2. Specify the Network Log file location on a local machine or a remote network location.

**Note** : By default, the log files are created on the local drive in the directory Program Files\VistA\Imaging\BackProc\Log. If a remote network location is entered, the Background Processor must have Read and Write access to it. Use the \\computer name\share name format and do not use a letter drive for the remote network location.

1. Click **OK** to save the information and close the window.

##### Background Processor Purge Configuration

The BP Purge / Verifier / RAID Group Advance Settings window is used for setting up the Scheduled Verifier, Scheduled Purge, and RAID Group Advance activities. In addition, the parameters for the Purge activity are set up through this window.

Selecting the Edit | Purge / Verifier / RG Settings menu in the Queue Processor window opens the BP Purge / Verifier / RAID Group Advance Settings window.

BP Purge/ Verifier /RAID Group Advance Settings

<!-- image -->

###### Purge Settings

The Purge process is used to remove image files from Tier 1when the free space is low or when older and/or not recently viewed image files can be purged to allow room for newly acquired images. It is important to note that no file is purged from Tier 1 shares if it has not been verified and confirmed as saved on Tier 2.

The Purge can be run manually in standalone mode or as a part of the Queue Processor. The Purge Parameters are used to control the purge activities in auto, manual and scheduled modes.

###### Guidelines for Setting Retention Days on Files for the Purge

General guidelines:

- Determine the span of dates of images that will be preserved on the **Imaging shares** .
- The shorter the timeframe, the more space will be free on Tier 1 when the purge completes.
- Multiple purges may be required to determine the retention days. It is advisable to start with one share with a large retention days value.
- Not all sites capture all the file types specified in the parameter list (e.g. BIG, Photo ID).
- If the frequency and the results of purging are acceptable, then it is not advisable to change the Purge values.
- If there is still not enough free space after the purge, decrease the Retention Days in Purge Parameters (BIG and FULL files, in particular) and repeat the purge until the desired free space is obtained.

Factors that determine the best set of purge parameters for an individual site are:

- The frequency of purges
- The volume of image acquisition rate
- The volume of image file retrieval
- The use of Pre-Fetch
- The capacity of disk space for VistA Imaging Tier 1 shares

Some sites have extended their Tier 1 capacities and are able to maintain five or more years of images on the shares. These sites may only need to purge once per year to purge off the latest year of images (year 6). Others who have smaller Tier 1 sets have to purge more frequently and can only have a limited amount of images on their shares.

For your site, strive to keep the shares between 80% and 90% full (or between 10% and 20% free space). When the Purge process completes and the resulting free space is in excess of this values, then adjust the parameters accordingly.

###### Configuring the Retention Days Settings

Retention Days Configuration Settings

<!-- image -->

**Retention Days and Retention Dates box**

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Full Files              | Source: Images from the DICOM Gateways, Clinical Capture workstations and Imports  File extensions: 756,ASC,AVI, BMP,BW,DCM, DOC, HTM, HTML, JPG, MHT, MHTML, MP3, MP4, MPEG, MPG, PAC, PDF, RTF, TGA, TIF, WAV  Range: 0 - 99,999 (number of days back from the current date that files should be retained) |
| Big Files               | Source: Images from the DICOM gateway and Clinical Capture workstations.  File extensions: BIG  Range: 0 - 99,999 (number of days back from the current date that files should be retained)                                                                                                                  |
| Abstract Files          | Source: Images from the DICOM gateways, Clinical Capture workstations and Imports. Abstract files are derivatives of the TGA/BIG format files.  File extensions: ABS  Range: 0 - 99,999 (number of days back from the current date that files should be retained)                                            |
| Photo IDs/Ad Direct     | Source: Source: Patient photo images and Advance Directives from the Clinical Capture workstations.  File extension: JPG  Range: 0 - 99,999 (number of days back from the current date that files should be retained)                                                                                        |

1. Enter the number of days that each of the four file types above should remain on the shares based on the purge date criteria in the section *Configuring Purge Date Criteria Settings* ***.***

**Note** : The FULL and BIG files are typically larger file sizes and consume more free space on the shares than the abstracts and photo IDs and Advance Directives.

1. As a result of different file type sizes, set fewer retention days for the larger file to free more space.
2. Because the abstracts and photo IDs are smaller files, set the retention days for purging these two types of files to a higher value than the values for the FULL/BIG file retention days. Also, the availability of Photo IDs and Advance Directives on Tier 1 has a great impact on patient care.
3. Because the abstract files are viewed as thumbnails on the Clinical Display workstation, set the retention days to retain a minimum of 5 years (1,825 days) on the shares regardless of the capacity of the Tier 1 to make viewing on the Clinical Display workstations more efficient.

###### Configuring Purge Date Criteria Settings

Purge Criteria Selection

<!-- image -->

| **Purge Criteria**   |                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------|
| Date Accessed        | Date when the file (image) was last viewed on a VI workstation                                                    |
| Date Created         | Date when the file was copied to the current disk share                                                           |
| Date Modified        | Date when the file was last changed. On the initial save, the Date Created will be the same as the Date Modified. |

Any of the three file date/times can be used (date accessed, date modified, date created) to purge the shares. There have been instances where third party utilities have changed the access dates on all the files it “touched” to the same recent date.

When the purge is activated, no files are deleted as none of the file access dates are purge candidates. It is recommended that the Date Modified be used. This date is retained when files are moved across storage media and is a reliable date for purging.

Configuring Scheduled/Express Purge Settings

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto Purge              | Enables the Purge to run when the high water mark is reached on a RAID Group.  **Important**  : Auto Purge should always be enabled.                                                                                                                                            |
| Last Purge BP Server    | BP Server on which the last purge was run                                                                                                                                                                                                                                       |
| Purge Factor            | Multiple of the % Server Reserve (found on the Imaging Site Parameters window). When the free space falls below value of the % Server Reserve times the purge factor, a purge is initiated on the next available online RAID Group. The default value of the purge factor is 2. |

**Express Purge Section**

| **Field or Checkbox**   | **Description**                                                                                                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active                  | Enables an Express Purge                                                                                                                                                                                      |
| Purge Rate              | When the number of image entries that have been evaluated for purging (based on the date criterion), without deletion, the purge process for that share will cease.  The default Purge Rate value is 100,000. |

**Scheduled Purge Section**

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active                  | Enable scheduled purges                                                                                                                                                                                                                        |
| Last Purge Date:        | Date when the last purge was run                                                                                                                                                                                                               |
| Frequency (in days)     | The number of days added to the Last Purge Date to determine the next Scheduled Purge Date.  If this field is left blank, the Scheduled Purge can be scheduled for a single event. When the event takes place, the Next Purge Date is cleared. |
| Next Purge Date         | Next scheduled Purge date                                                                                                                                                                                                                      |
| Purge Time              | Time of day for the next scheduled Purge                                                                                                                                                                                                       |

**Note** : Before an automatic purge is set up, a manual purge should be run on a share to make sure the Purge Parameters are set properly.

The automatic purge will use these same Purge Parameters and if not set properly, will result in unsatisfactory results. As the volume of images increases from the gateways, etc., these parameters should be adjusted to compensate for the increase.

Scheduled purges typically are set up on a monthly basis, but this will vary per site. The goal is to keep the shares between 80% and 90% full. Some adjustments in scheduling will need to be made after a scheduled purge cycle has completed.

Enabling Express Purge will greatly enhance the purging process by eliminating unnecessary file traversals that are not candidates for purging and thus significantly decrease the time to purge a share. The Purge Factor is set to control when the purge on a share is terminated.

When the number of files that are traversed and not deleted has exceeded the number in the Purge Factor, the purge stops on that share and begins purging the next share (automatic mode).

##### Network Location Manager: Adding a New Tier 1 or Tier 2 Storage Location and other Storage Types

**Note** : The following procedure applies to all the tabs in the Network Location Manager window.

1. From the Queue Processor menu bar, select **Edit | Network Location Manager** to open the following window.

Network Location Manager

<!-- image -->

The Tier 1 tab is automatically selected.

1. To add a new network location, click the **New** button at the bottom. The Network Location Properties window will be displayed.

Network Location Properties Blank

<!-- image -->

1. Type the Share Name.
2. At the Network Share field, either type the path to the location where images are to be stored, or click the **browse (…)** button and specify the path.
3. Select the appropriate option at the Storage Type field.
4. Click **Apply** .

Additional fields relevant to the storage type are displayed. The example below is for Storage Type RAID only.

**Note** : The STORAGE TYPE field is preselected depending on the Network Location tab selected. If the EKG tab is selected, then the STORAGE TYPE will be set to EKG, and so forth. However, the preselected value can be modified.

Network Location Properties Filled In

<!-- image -->

1. Leave the **Operational Status** check box selected by default setting, or clear it.
2. Leave the **Read Only** check box cleared by default setting or select it.
3. Click **Apply** to add the changes to the database or click **OK** to add the changes and exit.

##### Background Processor Imaging Site Parameters Edit Functions Imaging Site Parameters Window

The Edit | Imaging Site Parameters menu on the Queue Processor menu bar opens the Imaging Site Parameters window used to modify and save parameters in the VistA database. Each of the boxed areas in the window is described below.

Imaging Site Parameters

<!-- image -->

Administrative Settings

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Current Namespace       | Each VHA facility has its own unique 3-character designator. The Current Namespace file is used to store this 3 letter facility designator. It is used in Imaging as the first 3 characters of the 14-character name given to image files captured at this site. The VistA Imaging development and support teams maintain a central database with each sites 3 letter designator. The Current Namespace field is not configurable. This is necessary to ensure that image file names across VHA are unique. |
| Tier 1 Write Location   | All images from the gateways, Capture, etc. will be written to this share. The selected Current RAID Group determines which shares are listed on this dropdown list.                                                                                                                                                                                                                                                                                                                                        |
| Generic Carbon Copy     | Remote share where files will be exported. The share permissions must match the login credentials for the BP Server.                                                                                                                                                                                                                                                                                                                                                                                        |
| Current RAID Group      | The current active RAID Group includes the Tier 1 Write Location (described above). When new images are processed, they are stored on the Tier 1 Write Location share within this group. The RAID Groups are set up with the Network Location Manager.                                                                                                                                                                                                                                                      |
| Import Queue Security   | Checks users Imaging security keys for permission to capture images                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Site Code               | Three-letter acronym for the site location. This is used for AutoRouting and MUSE.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Associated Institutions | This set of institution values will allow users from other institutions to access local images.  **Note**  : Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift + F10.                                                                                                                                                                                                                                                                  |

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VistARad Grouping       | The radiologist can lock/interpret exams for other divisions (including the Parent Institution or other Associated Institutions), when those divisions are included in this set of institutions. Note that this setting controls exam locking and updating, as well as filtering of the UNREAD Exams lists to show only the Institutions that are defined here.  **Note**  : Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift + F10. |

Storage Functions Settings

<!-- image -->

| **Field or Checkbox**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tier 2 Write Location      | Tier 2 share where newly acquired images are currently being written.                                                                                                                                                                                                                                                                                                                                                                         |
| % Tier 1 Reserve           | The purpose of the reserve is to provide a significant amount of reserved primary storage to allow time for corrective action to create more space on the shares. Enter an integer between 1 and 50.                                                                                                                                                                                                                                          |
| % Tier 2 Reserve           | The default value is 5%. The values can be set in the range 0- 50%. When the allocated space does not meet this watermark, then no JUKEBOX queues will be processed and Tier 2 retrieval requests may be compromised, depending on the Tier 2 technology.                                                                                                                                                                                     |
| Auto Write Location Update | At the interval of every 20 minutes or 100 images written to a share, the Queue Processor will determine which share within a group has the most space and will use that share as the current write location for newly acquired images.  To manually select a Tier 1 Write Location, uncheck the Auto Write Location Update box. Images will be written to the selected Tier 1 share until it is filled or manually changed to another share. |

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple Namespace      | List of all the legacy namespaces that have been used at a site and are reflected in the filenames on the Tier 1 and Tier 2 shares.  **Note**  : Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift  + F10. |
| File Types              | File extensions outside of the standard extensions that the BP products will recognize and treat as a standard extension file.  **Note**  : Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift  + F10.      |

TeleReader

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET SITE SERVICE        | The web service used by Remote Image Views to gain access to remote sites                                                                                                                                          |
| Timeout TeleReader      | The number of minutes that the TeleReader application will remain active before closing due to inactivity. If this field is undefined, the application will not timeout. Max value is 999999, no decimals allowed. |

Clinical Workstation Settings

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Use Capture Keys        | Check users’ Imaging security keys for permission to capture images.                                                                       |
| Timeout Windows Display | Number of minutes until the Imaging Display application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600). |

| **Field or Checkbox**   | **Description**                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Timeout Windows Capture | Number of minutes until the Imaging Capture application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600).          |
| Timeout VistARad        | Number of minutes until the Imaging VistARad application will close due to inactivity. There is no default setting.                                 |
| Default MUSE Site       | MUSE site number that the Imaging Display application will connect to. Site numbers are usually 1, 2, 3, …. If left empty, the field defaults to 1. |
| Default User Preference | A specified user’s parameter settings will be used for first-time users of the Imaging system.                                                      |

Service Accounts Settings

<!-- image -->

These credentials are shared between the DICOM Gateway, Image cluster, Jukebox Server, and Background Processor.

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Username        | Imaging Administrator domain Service Account (IA Account) used to access the Imaging shares on the RAID and archive (jukebox) share. Both the RAID and archive (jukebox) shares must have READ/WRITE permission to this account.                                                                                                                                                                                                   |
| Windows Password        | Domain password used to access the Imaging shares on the RAID and archive (jukebox) share.                                                                                                                                                                                                                                                                                                                                         |
| VistA Access            | Encrypted access code for the Imaging Service Account in VistA. This account will be used to automatically re-log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).  **Note**  : The Imaging Service Account must have the MAG SYSTEM security key and secondary menu option MAG WINDOWS. The VERIFY CODE never expires. This user must have a single division designation. |
| VistA Verify            | Encrypted verify code for the Imaging Service Account in VistA. This account will be used to automatically re- log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).                                                                                                                                                                                                        |

DICOM Interface Settings

<!-- image -->

| **Field or Checkbox**                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DICOM Gateway Write Location             | RAID share where newly acquired images are currently being written.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DICOM Gateway Interface Switch Update    | Indicates presence of a DICOM Gateway on the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Retention Days HL7 – Modality Work Lists | This field is used as the default value, in days, by the DICOM Text Gateway for three different user menu driven purges:  - This field is used by the Purge Old Modality Worklist Entries menu option to determine the number of retention days from the date of creation of Modality Worklist Entries. - This field is used by the Purge Old DICOM Message Files menu option to determine the number of retention days from the date of creation of DICOM messages that were sent to commercial PACS. - This field is used by the Purge Old HL7 Transaction Global Nodes menu option to determine the number of retention days from the date of creation of HL7 messages sent from VistA to the DICOM Text Gateway.  **Note**  : This value may be overridden by the user when executing any of these menu options. |
| % Free Space DICOM Messages              | Minimum percentage of free disk space for DICOM HL7 messages on the text gateway. A typical value is 25%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Retention Days DICOM Messages            | Number of days to retain DICOM HL7 messages on the text gateway, 30 days is recommended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

##### Scheduled BP Verifier

The Scheduled Verifier should be set up to run nightly. It will verify the integrity of any image records not validated since the previous Verifier run (Manual or Scheduled). It is suggested that the Verifier be run manually over the entire range of image records before incremental Verifier runs are started. The application that runs for the Scheduled Verifier is the same as the Manual Verifier. Reference the Manual Verifier in the BP User Manual for specific information about the GUI and log files.

###### Guidelines for Setting Parameters for the Scheduled Verifier

The following guidelines for using the Scheduled Verifier will help maintain the integrity of the Imaging records in the VistA database.

**Important** : If the PC that has Scheduled or Auto events is not a server class, the task will not start.

- Set the Active check box to enable scheduled runs of the BP Verifier. The scheduled runs of the Verifier will only check the most recent VistA records of new images that have been created since the last Scheduled Verifier run.
- Do not select the Check Text Files check box. The contents of the text files on Tier 1 will be compared to the information in VistA. This processing will slow down the Verifier processing and utilities are not available at the present time to correct any issues that surface.
- The Last Verifier Date field is set by the system and cannot be set by the user.
- When the Active parameter is checked, the Frequency (in days) field setting should be 1 so that the Verifier runs daily.
- Initially set the Next Verifier Date to today’s date. The scheduling frequency will be based on this date.
- Set the Verifier Time to an inactive period of the day –typically after hours when image creation activity is low.

Description of the Scheduled Verifier Settings

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| Last Verify BP Server   | BP Server on which the Verifier was last run (Display only, set by application) |

###### Scheduled Verifier

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active                  | Enables scheduling the Verifier                                                                                                                                                                                                                                                                                                                                                          |
| Check Text Files        | Read text files on Tier 1 and determine if:  1. the file is binary or unreadable 2. there are unprintable characters in the file 3. The SSN does not match the one in VistA 4. SOP Instance UID mismatch with VistA 5. Study Instance UID mismatch with VistA 6. SOP Instance UID and/or Study Instance UID are blank 7. SSN in the top part of the text file does not match the bottom. |
| Frequency (in days)     | Number of days added to the date of the last time the Verifier application ran to determine the next time the Scheduled Verifier should be run.                                                                                                                                                                                                                                          |
| Last Verifier Date      | Date when the Verifier was last run                                                                                                                                                                                                                                                                                                                                                      |
| Next Verifier Date      | Date of the next scheduled Verifier will run based on the Frequency (in days) parameter                                                                                                                                                                                                                                                                                                  |
| Verifier Time           | Time of day when the Verifier will run                                                                                                                                                                                                                                                                                                                                                   |

###### Setting Up the Scheduled Verifier

Use the guidelines above to set up the Scheduled Verifier.

1. Select **Edit | BP Servers** .
2. Drag the SCHEDULED VERIFY task on the BP Server to the location where the Verifier is to be run.
3. Click **OK** to close the window.
4. Select the **Edit | Purge / Verifier /RG Settings** tab.
5. Set the following fields in the Scheduled Verifier box:

| **Field**           | **Setting**                                               |
|---------------------|-----------------------------------------------------------|
| Active              | Checked                                                   |
| Check Text Files    | Unchecked                                                 |
| Frequency (in days) | 1                                                         |
| Next Verifier Date  | (starting date)                                           |
| Verifier Time       | (time of day the Verifier will run – after hours is best) |

##### Scheduled RAID Group Advance

The RAID Group Advance is configured on the Imaging Site Parameters window. RAID groups are used to organize Tier 1 shares into logical groups for easy tape backup and restore processing. During the install, all existing online Imaging shares are placed into the first RAID Group, RG-XXX1. This configuration is the same and has been in existence for past years. The Auto Update functionality is also the same. At regular intervals, the current write location will change to the share with the most free space. The Auto-Write function will reset the current write location to provide load balancing within the RAID group. When the % Server Reserve within the group has been reached, the Auto-Write will set the next RAID group as the current write group. In addition, when the used space in that RAID group has reached the high water mark, the next RAID Group that has online shares will become the current RAID group.

###### Guidelines for Setting Parameters for the Scheduled RAID Group Advance

Sites can choose a configuration that suits them best, as follows:

- Use the initial configuration where all the shares are in the same RAID Group. The new images will be evenly distributed among all the shares.
- Nightly incremental tape backups, as well as monthly/quarterly tape backups, must be done on a regular basis on all the shares.
- Distribute the shares among multiple RAID Groups. Fill the shares in each group to the Server Size, and then switch the current write group to the next. New image files will be distributed over all the shares assigned to that group.
- Nightly incremental tape backups, as well as monthly/quarterly tape backups, must be done only on that RAID Group.
- When the RAID group has reached capacity, a final full backup should be done on all of that RAID group’s shares. Nightly incremental tape backups and monthly/quarterly tape backups should be started on the next current write group.

Scheduled RAID Group Advance Settings

<!-- image -->

| **Field or Checkbox**   | **Description**                                                                                                                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active                  | Enable RAID Group Advance scheduling                                                                                                                                                                                                                                                         |
| Last RAID Advance       | Date when the last scheduled RAID Group Advance occurred                                                                                                                                                                                                                                     |
| Frequency (in days)     | Number of days added to the date of the last RAID Group Advance to determine the next time the RAID Group Advance will run. If the Frequency parameter is set, the next RAID Group Advance will be scheduled automatically. If the frequency is not set, no automatic scheduling will occur. |
| Next Advance Date       | Date of the next scheduled RAID Group Advance                                                                                                                                                                                                                                                |
| Advance Time            | Required. Time of day of the next scheduled RAID Group Advance                                                                                                                                                                                                                               |

###### Setting Up the Scheduled RAID Group Advance

This option is applicable when the there are multiple active RAID Groups. Use the guidelines above to set up the Scheduled RAID Group Advance.

1. Select the **Edit | Purge / Verifier /RG Settings** tab.
2. Set the following fields in the Scheduled RAID Group Advance box:

| **Field**           | **Setting**                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| Active              | Checked                                                                                          |
| Frequency (in days) | Set by determining how long a span of time images will be written to a set of shares in a Group. |
| Next Advance Date   | Set the starting date when the system will move to the next RAID Group.                          |
| Advance Time        | Set the starting time of day when the system will move to the next RAID Group.                   |

1. Click **OK** to close the window.
2. Click **Start** on the Queue Processor main window.

(A Queue Processor must be in the running state in order for the RAID Group Advance to run on the designated server.)

#### 63 Background Processor Image and File Entry Verifier

Background Processor Image and File Entry Verifier submenu

<!-- image -->

As a separate executable, it is necessary to launch the Verifier application from the Programs menu, unless you set up a desktop shortcut. The executable is installed by default in the program files/vista/imaging/backproc subdirectory.

The process examines each non-group entry within the selected range of IMAGE file (#2005) entries. It searches each network magnetic and jukebox share indicated by each IMAGE file (#2005) entry for all extensions of the indicated filename. For each, it does the following:

- When more than one Tier 2 share contains images of the same file name, the Verifier will aggregate those files on a current Tier 2 Write location. It will update the JB references in the IMAGE file (#2005) entry and IMAGE AUDIT file (#2005.1) entry. The Activity column of the Verifier will display this activity as “Aggregate”.
- If any extension of the image file is missing from the referenced Tier 2 share and is both referenced and available on the VistA Imaging Shares, then the Verifier will copy it to Tier 2 and update the appropriate Tier 2 IMAGE file (#2005) references.
- If the VistA Imaging Shares references in the IMAGE file (#2005) entry are not accurate and the appropriate files are available at another network location, then the VistA Imaging Shares references are updated.
- If there is no TGA or ABS file on the network, but a BIG file exists, then the Verifier will create the missing file(s) at the current network write location, aggregate it to the Tier 2, and update the image file jukebox references.
#### 64 Imaging Server and Jukebox Backup Information

Sites should establish weekly and daily schedules for backing up images from the VistA Imaging network servers and Tier 2 unit(s). A copy of the backed up media should be kept off site. Full backups and incremental backups are recommended. For further information, refer to the “Backups” section of Appendix B of the *VistA Imaging System Installation Guide* .

#### 65 DICOM-related Backup and Purge

As the software in the VistA Imaging DICOM Gateway is being used, information is created and stored. If left alone, this information would accumulate in an unbounded fashion and would eventually exceed any reasonable storage capability.

A number of entities are purged automatically as the software is being used, based on retention parameters that can be set using the software itself.

The storage of images takes a lot of space, and, as a result, images are typically only stored temporarily on the magnetic disks that are connected to the various workstations and servers. For long-term storage, images are typically copied to a jukebox, and then removed from their temporary cache storage.

##### Growing entities

The VistA Imaging software creates the following entities:

- Image files (pixel data) temporarily stored on VistA magnetic cache servers
- Image Background Queue (^MAGQUEUE(2006.03,i,…))
- Modality Worklist Entries (^MAGDWLST(2006.56, i, …) )
- DICOM and PACS Messages (^MAGDHL7(2006.5,i,…))
- DICOM Failed Images (^MAGD(2006.575,i,…))
- DICOM Incomplete Images (^MAGD(2006.593,i,…))
- DICOM Error Log (^MAGD(2006.599,i,…))
- Error log on DICOM Gateways
##### Tier 2 Archive

###### File Migration

As a part of normal procedure, captured images are copied to long term storage. The process that copies these files observes the following rules:

- Long-term storage media should be non-rewritable optical media.
- Overwrites are not allowed.
- All image-related files (“Full”, “Big”, and “Abstract”) are copied to Tier 2.
- Site-specified additional file types are copied to Tier 2. (“TXT” is part of the default install setting).
- If a file copy fails, additional attempts are made to copy the file. This is controlled by a site parameter whose default is three attempts.
###### Removing Jukebox Media - Offline Images

The VistA Imaging System is capable of tracking images on platters that have been removed from the jukebox. This is sometimes necessary when all platters in all of slots in the jukebox are full, and a new jukebox has not been purchased or installed. Some sites use this option to archive platters on a first in, first out manner instead of buying additional hardware. By removing a platter, the images on the platter are marked offline. The clinical display software will display an “Archived Image” abstract (thumbnail) for any offline images. If the user clicks on the abstract, a message-box will appear with offline image and associated platter information. If the user chooses to view that image, they can notify an imaging system manager so the platter can be put back into the jukebox. System Managers can also be notified automatically with an email message whenever an offline image is accessed. The OFFLINE IMAGE TRACKERS mail group is installed on the system during the VistA Imaging KIDS installation. System managers that would like to receive notifications should add themselves to the mail group. The procedure below outlines the steps necessary to track offline images.

**Note** : See the *Storage Utilities User Manual* for the procedure to remove jukebox media.

###### Taking Images Offline

1. Go to DEX Administrator.
2. Click on **View | Reports** , then choose **Media Files** .
3. Click **Next** .
4. Select the media (platter) that will be taken offline. (Multiple select is allowed)
5. Click **Finish** .
6. When the report is available, save it to a file (use Save As) - Be sure to save as type Text (*.txt)
7. Move file to VistA System (ftp; use ASCII mode, not binary mode)
8. Run M option MAG JB OFFLINE (shown below); this procedure will require a FileMan access of “@”.

To Check Which Platters are Offline

<!-- image -->

<!-- image -->

To Put Images Back Online

<!-- image -->

##### Purge Image Files from VistA Magnetic Cache Manually

The Background Processor Purge software purges image files from the VistA Magnetic Cache, depending upon certain criteria set by the site.

To manually operate this software:

1. From the Windows Start | All Programs menu, select **VistA Imaging Programs | Background Processor | Purge** .

Background Processor Purge software

<!-- image -->

The display box in the upper left quadrant shows the files that will be purged and the date of last access by user application. All listed items are captured in the current Purge.log file. The display is cleared after every 50 items to conserve application memory.

1. To select a subset of image shares for purging, select **Edit | Select Shares** . The Purge Share Select window displays the shares.

Purge Share Select Window

<!-- image -->

1. Select the share(s) to be purged and click **OK** .
2. Review the Purge parameters and share selection on the Purge window.
3. In the Purge application, click **Start** and **OK** in the confirmation message displayed.

The Activities display (immediately below the start button) shows the time of execution and gives running totals for the VMC files evaluated, the number purged, and the number that were queued to be copied to the Jukebox (JB) because they could not be confirmed on the jukebox.

The Share Processing display lists each online, non-routed, magnetic type share in the NETWORK LOCATION file (#2005.2). These are input values for each step of the purge process and they are appended with a Purged status as they are successfully processed.

The two graphical displays reflect the runtime categorization of image files evaluated and purged as the purge process progresses. Note that the vertical axis units change over the processing period. Also, the units tend to differ between the two graphs.

Steps in the purge process are:

1. The processor initially gets the information from VistA including site parameters governing file aging criteria and online magnetic file server shares.
2. The hierarchical directory structures on each imaging server share are traversed. For each file in each directory, the date of last access is compared against the VistA site file aging criteria for that file type.
3. Files meeting VistA purge criteria are removed from the Imaging magnetic server share, and the IMAGE file (#2005) is updated in the VistA database to indicate the current Tier 2 Write location of the files on the Tier 2.
4. If the image file being evaluated resides on an imaging server share other than the one indicated in the IMAGE file (#2005) in the VistA database, then the file on the unreferenced share is purged regardless of the date of last access as long as the file is present at its referenced location.
5. If there is no corresponding IMAGE file (#2005) entry in the VistA database for this file, the file is purged regardless of age criteria.
6. If the IMAGE file (#2005) in the VistA database is synchronized with the Tier 1, but there is no reference to the file’s location on the Tier 2 then a Tier 2 copy is queued and the file is left in place on the Tier 1 share.
7. A site parameter exists for evaluating radiology image files to be held regardless of age if the specific file is related to a radiology package entry with the “NOPURGE” node set.

**Note** : A monthly verification process may be added to validate the file server references in the IMAGE file (#2005) in the VistA database.

##### Entities That Are Purged at the Discretion of the Site Supervisor

##### Purge Old Modality Worklist Entries

Old entries may be purged by selecting the option “ **Purge old Modality Worklist Entries** ” from the “ **Text Gateway** ” menu.

The subroutine that is called for this menu-option (ENTRY^MAGDDEL1) removes entries in

^MAGDWLST(2006.55,…) that were time-stamped more than a certain number of days (the default is the number of days specified in ^MAGDICOM(2006.563,1,"DELETE DAYS")) before the current date.

##### Purge Old DICOM Message Files

Old files and directories may be purged by selecting the option “ **Purge old DICOM message files** ” from the “ **Text Gateway** ” menu.

The subroutine that is called for this menu-option (DICOM^MAGDDEL2) removes files and directories that were time-stamped more than a certain number of days (the default is the number of days specified in ^MAGDICOM(2006.563,1,"DELETE DAYS")) before the current date.

Names of directories that may play a role in this context are stored in

^MAGDICOM(2006.563,1,"DATA PATH",…).

##### Purge PACS Messages

Old messages may be purged by selecting the option “ **Purge old HL7 transaction global nodes** ” from the “ **Text Gateway** ” menu; these messages are stored in global

^MAGDHL7(2006.5.

The subroutine that is called for this menu-option (HL7^MAGDDEL3) removes entries in

^MAGDHL7(2006.5,…) that were time-stamped more than the number of days specified in

^MAGDICOM(2006.563,1,"DELETE DAYS") before the current date.

##### Process DICOM Failed Images

Entries are removed from this file by using the Correct RAD-DICOM File Entries [MAGD FIX DICOM FILE] or the Correct Clinical Specialties DICOM File Entries [MAGD FIX CLINSPEC DICOM FILE] menu options. Using this menu will mark the entries as corrected and will be reprocessed by the VistA DICOM Image Gateway. Entries are stored in global

^MAGD(2006.575).

##### Removal of DICOM Incomplete Images

Entries in this file will automatically be removed after an hour’s time span; entries are temporary stored in global ^MAGD(2006.593).

##### DICOM Error Log

This file should not be purged. It records incomplete files received and images requested to be deleted from the DICOM FAILED IMAGES file (#2006.575). Entries are stored in global ^MAGD(2006.599.

##### MSM Error log

See the *VistA Imaging DICOM Gateway User Manual* for instructions on how to view and purge entries from the MSM Error Log located in global ^UTILITY(“%ER”,+$H.

#### 66 VIX-related Backups

No special backup processes are needed for the VIX (VistA Image Exchange) service.

- Metadata and images stored on the VIX’s dedicated cache are considered transitory copies and are not a part of the patient record. The site from which the data originates is the official custodian of the data, not the VIX.
- The VIX transaction log, which is the primary record of VIX activities, is retained on the server where the VIX is installed for 90 days. A permanent remote backup of the VIX transaction log is also made by the VIX Log Collector service; this is a remote automated service that requires no site configuration or activation.

For more information about the VIX cache and the VIX Log Collector service, refer to the *VIX Administrator’s Guide.*

This page is intentionally blank.

### Chapter 10	Callable Routines/Application Programmer Interfaces (APIs)

### 1 Import API

The Import API (Application Programming Interface) was built in VistA Imaging patches 15 and 38 and is used to allow non-imaging VA and commercial vendors to build applications that import images into the VistA database and connect them to the patient record. The Import API was modified in VistA Imaging Patch 108.

The Import API is used by the VA Veteran's ID Card (VIC) and Clinical Procedures applications, as well as commercial applications such as iMed consent and DocManager. The VIC software is used to acquire photographic images of patients. These images are sent to the National Card Management Directory (NCMD).A copy of these photo images are also automatically sent to VistA Imaging through the VistA Imaging Import API.

The Import API also has the following capabilities:

- To check VistA Imaging and verify if a patient has a photo ID on file in VistA Imaging.
- To retrieve a current list of indexing terms.
- To create a new TIU Note stub and attach an image to it.
- To watermark images associated with a Rescinded Advance Directive with the text “Rescinded”.

For more details on the Import API reference the *VistA Imaging System Import API Programmer Guide* . The Import API Programmer Guide can be requested from the VistA Imaging Development Team.

The Import API cannot be used without a written agreement between the VistA Imaging group and the party wishing to use the Import API. All imported images must meet image quality and documentation requirements of VistA Imaging. In addition to the written agreement the VA Policy in section 10.1.1 and FDA Policy in section 10.1.2 must be followed.

#### VA Policy

***VA Policy states the following*** ***:***

Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure contain a controlled or strictly defined interface or report data to a database external to the local facility must not be altered except by the VistA Imaging OED staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated VistA Imaging OED staff that are located at the registered manufacturing site and operating in the designated production environment. **Note** : Any party interested in interfacing with the VistA Imaging software will need to contact the VistA Imaging development team to get an integration agreement in place.

#### FDA Policy

***FDA Policy states the following*** ***:***

The Food and Drug Administration (FDA) classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.

### 2 VistA Imaging Import API

#### Terms of Use

**Note:** The Import API, as a part of the VistA Imaging software, is regulated as a medical device. The Import API cannot be used without a written agreement between the VistA Imaging HSD&amp;D group and the party wishing to use the Import API.

To secure an agreement for the use of the Import API, the following criteria must be met:

1. Any products built or interfaced using the VistA Imaging Import API must be tested with VistA Imaging. Testing will be performed by the VistA Imaging team with assistance from field sites and the calling package. This testing must demonstrate that there are no adverse interactions affecting the safety, efficacy or performance of the VistA Imaging software or the devices interfaced to VistA Imaging.
2. Any changes to packages/product(s) using the VistA Imaging Import API must be reported to the VistA Imaging Project Office for review and testing before release. Retesting of VistA Imaging with the product(s) is required with any change.
3. Documentation that imported reports/objects meet VHA, regulatory, and quality requirements must be on file with the Vista Imaging Project Office prior to any clinical use. Sample imported reports/objects shall be provided initially to the VistA Imaging Project Office by the package using the API. Sites installing the VistA Imaging API must comply with all VistA Imaging requirements and are responsible for filing all required documentation with the VistA Imaging Project Office, including image quality and data forms and sample reports/objects from any interfaced device.
4. Additional requirements may apply to non-VA software using the Import API.

### Chapter 11	Error Recovery, Troubleshooting, and Testing

#### Error Recovery

##### Server or Disk Drive Failure

When a server or disk drive fails, the VistA Imaging System allows immediate action to be taken so that system operation may continue. The following steps should be taken when a server or drive has failed:

- Use the Network Location Manager menu option on the Background Processor and place the share(s) “OFFLINE”. If these are magnetic drives, their images will be automatically pulled from Tier 2.
- If the Image Network Write Location or PACS Image Write Location field in the IMAGING SITE PARAMETERS file (#2006.1) points to a device that is down, edit it to point to a location that is operational. Use the Edit/Site Parameters menu option on the Background Processor.
- When your server or disk drive has been repaired, edit the Operational Status field (#5) of the NETWORK LOCATION file (#2005.2) to “ONLINE”.
- Run the Verifier software on your magnetic shares to synchronize any pointers changed during the failure, and archive unprocessed files to Tier 2.
##### Delete Image and Pointers

Images can be deleted using the VistA Imaging Display application. When an image is deleted, the image itself and all "derivative" images (such as abstracts) are deleted from the image servers. Additionally, the IMAGE file (#2005) entry for the image, and any pointers to applications (Laboratory, Medicine, etc.) for that image, are deleted as well. To delete images, a user must have the MAG DELETE security key. For Clinical Display users with this key, there will be a Delete in the main menu of the Image List and Radiology Viewer windows. The Delete option will also be available in pop-up menus for images and abstracts.

The following occurs once an image has been flagged for deletion:

1. An entry is made in the Background Queue file and will be processed on a first-in-first-out basis by the Background Processor.
2. The IMAGE AUDIT file (#2005.1) will record the information on the deleted image entry.
3. An entry will be made in the IMAGE ACCESS LOG file (#2006.95) to indicate that an image was deleted.
4. The image entry will be deleted from the IMAGE file (#2005) and any pointed to entries will also be updated.
5. All DOS files relating to the image will be deleted from the Imaging server(s), but not from the jukebox.
###### ATTENTION: Caution Must Be Taken when Granting the Image Deletion Key.

**Note:** Anyone who holds the Image Deletion Key is allowed to delete any image, regardless of who created the image in question.

When images are deleted, a reason code must be entered to note why the image was deleted. Sites can optionally add site-specific reason codes by using the MAG REASON EDIT System Manager Menu option, which is explained in Section 8.2 of this document.

##### Correcting Image Capture Errors

When an image is captured under the wrong patient, it is **strongly recommended** that you use the following procedure to make the needed correction—provided that the images still reside on the Radiology modality, or a hard copy of the image is still available:

1. Correct the patient information on the modality, then resend the image; **or** , if a hard copy (X- Ray film) of the image is available, digitize the image
2. Review the new images acquired
3. Follow the instructions in the section above to delete the incorrect images

If the above approach is not feasible then contact the Imaging Support staff to assist in correcting the images. The steps they will use are covered below.

Two (2) types of errors can be made during image capture:

- An image is captured that the user did not want to save. This type of error is corrected by the image and pointer deletion procedure described above.
- The user identified the patient incorrectly and therefore saved patient B's images with patient A's text record. Presently, this second type of error must be corrected manually by imaging system manager staff using the following procedure.
##### Delete Incorrect Image Pointers from Incorrect Patient's Record

1. Use the edit option of File Manager to access the image field of the parent package (e.g., radiology, cardiology, laboratory, etc.) for the incorrect patient.
2. Identify and write down the names of the images that were incorrectly placed in this file.
3. Delete these entries.

##### Add Correct Image Pointers to Correct Patient's Record

1. Use the edit option to select the correct patient's report file.
2. Edit the image field and enter the exact same image names that were deleted from the incorrect patient.

##### Verify Correction

Ask the user to examine the image of the correct and incorrect patients, and determine whether the correction was done properly.

##### QA Review Utility

In Clinical Display or Clinical Capture, users who have the MAG SYSTEM or MAG EDIT security keys have access to the QA Review Utility. This utility allows users with the appropriate security key to specify date ranges and perform quality assurance checks on captured images from specified users.

The QA Review Utility also allows the reviewers of the images to change the image indexes by using the Image Index Edit Utility.

##### Image Index Edit Utility

The Image Index Edit Utility is available to users who have the MAG SYSTEM or MAG EDIT security keys. Through this utility, an authorized user can select an image and modify the indexing terms for the image.

##### QA Review Reports

The QA Review Reports are available to users who have the MAG SYSTEM or MAG EDIT security keys. The reports are run for a specified date range and for specific users. The reports give details for users to scan for the date range, status, number of entries and pages, and a percentage representing the total number of images reviewed.

#### Troubleshooting / Error Messages

Users may encounter several types of errors as they use the VistA Imaging System. Some of these errors are…

- **Processing errors** : which means that the VistA Imaging System failed to complete a processing task.
- **Data errors:** which means that the VistA Imaging System attempted to use data that was incomplete or formatted incorrectly.
- **Command errors:** which means that users and other programs that interact with Imaging issued commands that conflicted with other commands or with the VistA Imaging System processing state.

A table of error messages, descriptions and causes or solutions is provided in Appendix A of this document and in the *VistA Imaging Error Message Guide* .

#### Test Software Available for Troubleshooting

##### Introduction

When setting up a workstation, it is often necessary to use software to test isolated workstation functions. A number of executables are available for testing:

- Network connectivity
- Connectivity to the Kernel RPC Broker
- Ability to display images
- Connectivity to image servers
- Network timing tests

These exetables are described in the following sections.

##### PING, TRACERT

The PING and TRACERT commands are available in the DOS directory on the workstations. Using these commands can help determine if the IP address supplied in the HOSTS or LMHOST file is reachable, or if a possible routing problem exists. The local PC support person in IRM can assist with the usage of these commands and the local network IP addressing scheme.

##### RPCTEST.EXE

The RPCTEST.EXE file is located in the Program Files\VISTA\BROKER directory. This file can be used to test the Broker Client Manager connection to the VistA servers. Once this file is executed, the VistA Access/Verify Code Window should display. If it does not, one or a combination of the following could be happening:

- The TCP Listener is not running on the VistA hospital system.
- An invalid IP address or listening port number was configured during the Broker Client Manager software installation on the workstation.

**Note** : Please review the Kernel RPC documentation on the usage of this executable file and installation of the RPC Client Manager software.

##### VistA Imaging Capture, Test Mode

The VistA Imaging Capture software has a Test mode that allows testing of input devices (scanners, video capture boards, etc.). The Test mode features…

- Testing of the capture functions without a connection to the VistA servers.
- No requirement to identify patients.

In addition, the image test file will not be saved. This mode is helpful when interfacing and testing new equipment.

To set the application to test mode, select **Test Mode** from the **Configuration | Configuration Settings | All Settings** menu.

**Note** : See the Capture online help for additional information.

#### Handling Processing and Storage Errors in the New Data Structures

The HDIG and the Archiver handle errors in storing the SOP classes for which support was introduced in MAG*3.0*34. These SOP classes are stored in the data structures that were introduced in MAG*3.0*34.

The section does not apply to processing and storage errors of the SOP classes that were supported before the release of MAG*3.0*34.

##### How the HDIG and the Archiver Handle Processing and Storage Errors

The HDIG uses the DICOM Gateway notification mechanism to send notifications about processing and storage errors to the email group defined in its configuration. It also sends information about such errors to the modality that sent the DICOM object.

When the HDIG stores an image, it uses two queues defined in the QUEUE file (#2006.927). The Archiver uses the Async Storage Request Queue to archive the objects in long term storage asynchronously. It uses the Async Storage Request Error Queue to record failed storage attempts. Both queues operate through entries made in the QUEUE MESSAGE file (#2006.928). The Archiver attempts to process storage requests from QUEUE MESSAGE file (#2006.928) entries for the Async Storage Request Queue. If the Archiver is not able to store the object, it waits for 20 minutes before trying again. The Archiver will try to store an object five times. After five unsuccessful attempts to store the object, the Archiver deletes the Async Storage Request Queue entry in the QUEUE MESSAGE file (#2006.928) and creates a corresponding entry for the Async Storage Request Error Queue.

After the error queue message is created, the Archiver cannot make further attempts to store the object until a user examines the failed attempts, resolves the source of the error, and re-enters an Async Storage Request Queue entry in the QUEUE MESSAGE file (#2006.928) for the object.

You can identify and view Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) using VistA options on the Hybrid DICOM Gateway Menu [MAGV HDIG MENU] as described in *Using Hybrid DICOM Gateway [MAGV HDIG MENU] Options to Get Information About Asynchronous Storage Error Queue Entries in the QUEUE MESSAGE File (#2006.928) .* After correcting the problem, you can return the archive request back to the Async Storage Request Queue. For information about the procedure, see *Retrying Failed Archive Requests.*

##### Getting Information About Processing and Storage Errors

There are two ways to get information about processing and storage errors:

- Getting emails from the DICOM Gateway notification mechanism
- Using the Hybrid DICOM Gateway Menu [MAGV HDIG MENU] Options
##### Getting Emails from the DICOM Gateway Notification Mechanism

The HDIG saves processing and storage errors. It sends messages with all processing and storage errors to the email address defined in the configuration of the DICOM Gateway. The HDIG sends an email immediately for processing or storage errors. Image RESENDs and IOD violation errors accumulate during the day and are sent either in groups of 25 or at the end of the day (if fewer than 25).

If you get information about storage and processing errors, you need to identify the cause of the error and correct it. This typically involves identifying the object that caused the error, the cause of the error, and correcting the problem.

##### Using Hybrid DICOM Gateway [MAGV HDIG MENU] Options to Get Information About Asynchronous Storage Error Queue Entries in the QUEUE MESSAGE File (#2006.928)

You can view the information for Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) using the Find and List options on the Hybrid DICOM Gateway Menu [MAGV HDIG MENU].

1. Log into your VistA account and select the Imaging System Manager Menu [MAG SYS MENU].
<!-- image -->
2. Select Find Async Storage Request Errors [MAGVA ASYNC STORAGE ERR QURY]. This option selects QUEUE MESSAGE file (#2006.928) entries with a QUEUE field value of Async Storage Request Error Queue, and stores them in the MAGV-ASYNC- STORAGE-ERRORS Template.
<!-- image -->
3. Select List Async Storage Request Errors [MAGVA ASYNC STORAGE ERR LIST].

This option lists detailed information about the QUEUE MESSAGE file (#2006.928) entries selected in the preceding step. The following shows the sample output for the first three of 18 error messages in the Async Storage Request Error Queue.

<!-- image -->

The Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) provide information about the type of object that is stored and about its token. The listing displays the logged storage error(s) for an artifact resolved using its token. The sequence in the preceding sample was generated following these steps.

- Uses the artifactToken to look up the artifact identifier (IEN of the artifact) from the ARTIFACT file (#2006.916).
- Retrieves the storage transactions for the artifact from the STORAGE TRANSACTION file (#2006.926), filtering for failed transactions. (Those with a STATUS field value of **F** ).
- Displays the MESSAGE field (#7) of the STORAGE TRANSACTION file (#2006.926) entry, which is likely to contain an error.
- Displays the lastError item from the MESSAGE field (#6) in the QUEUE MESSAGE file (#2006.928).
##### Retrying Failed Archive Requests

The Archiver makes five attempts to archive a file before moving it to the Async Storage Request Error Queue. After correcting the cause of the error, a site administrator must manually move the messages from the error queue to the Async Storage Request Queue. This notifies the Archiver to try and store the record again.

This section demonstrates how to move all the messages from the Async Storage Request Error Queue to the Async Storage Request Queue.

From the Hybrid DICOM Gateway Menu, [MAGV HDIG MENU], select Requeue Async Storage Request Errors [MAGVA ASYNC STORAGE ERR REQU].

In this first example, all of the entries are requeued.

<!-- image -->

In this example, the entries have previously been requeued, but the sort template has not been refreshed (with a subsequent **F** ind operation).

<!-- image -->

You should run the menu options in this order:

- Find Async Storage Request Errors
- List Async Storage Request Errors
- Requeue Async Storage Request Errors

A List operation displays the current contents of the sort template.

Before running the Requeue option, you must resolve the cause of the storage error.

If the entries have already been requeued when you attempt to requeue them, you should initiate a new Find operation to re-initialize the sort template.

If a situation, such as a server power outage, is the cause of many archive failure errors, it is more efficient to verify a representative sample of the error messages and then requeue the entire set with the Requeue option after the event that has caused the storage failures is corrected.

### Chapter 12	External Relations

#### HL7 Messages

The Text gateway processes the following HL7 message types to construct and maintain the Modality Worklist Database:

ADT	Admission, Discharge, Transfer

SCH	Patient Appointment and Scheduling Segment MFN	Master File Notification

ORM	Order Message

ORU	Observational Result – Unsolicited

#### HL7 Application Parameters

VistA Imaging includes the following HL7 application parameters:

- MAG COMRCL PACS

This application name represents the destination for HL7 messages, and will appear in field 5 of the Message Header segment (MSH-5) of the HL7 message generated by VistA. The value in its FACILITY NAME Field will appear in MSH-6.

- MAG VISTA IMGNG

This application name represents the origin for HL7 messages, and will appear in MSH-

3. The value in its FACILITY NAME Field will appear in MSH-4.

These entries are added to the HL7 APPLICATION PARAMETER File (#771) during installation.

<!-- image -->

You can change the value of the NAME or FACILITY NAME attributes through VistA option HL EDIT APPL PARAM.

#### HL7 Logical Link

VistA Imaging includes the HL7 logical link MAG CPACS.

This entry will be added to the HL7 LOGICAL LINK File (#870) during installation:

<!-- image -->

This logical link contains information about the commercial PACS destination, including its TCP/IP parameters (IP address and port number). The VistA HL7 package uses the IP address and port number to route messages to their destination over the network. You can change the value of the IP address and port number using VistA option HL EDIT LOGICAL LINKS.

#### Imaging Broker Calls

###### Imaging Broker Calls

All VistA Imaging remote procedure calls are documented in the REMOTE PROCEDURE file (#8994) and can be viewed using FileMan Print File Entries [DIPRINT] or Inquire to File Entries [DIINQUIRY] menu options. VistA Imaging remote procedures use the MAG namespace.

<!-- image -->

#### Windows Messaging

In order to communicate with CPRS, windows messages are exchanged on the workstation. The VistA Imaging display clients must be launched from the CPRS menu option to enable the exchange of these messages.

If CCOW is enabled, VistA Imaging Clinical Display and VistA Imaging Clinical Capture will synchronize patient and user context with other CCOW applications (such as CPRS) using CCOW. If CCOW is unavailable, VistA Imaging Clinical Display and VistA Imaging Clinical Capture will continue to synchronize with CPRS when launched from CPRS using Windows messages.

#### Integration Agreements

Integration Agreements (IAs) describe how one VistA application uses routines that belong to another VistA application.

To display the ICRs that cover non-Imaging routines used by Imaging, perform the steps below.

1. Sign on to the FORUM system.
2. Select the DBA menu.
3. Select the INTEGRATION CONTROL REGISTRATIONS [IAs] menu.
4. Select the Subscriber Package Menu [SUBS].
5. Choose the “Print ACTIVE by Subscribing Package” option.
6. Enter “IMAGING” at the “START WITH SUBSCRIBING PACKAGE: FIRST//”

prompt.

1. Enter “IMAGINGZ” at the “GO TO SUBSCRIBING PACKAGE: LAST//’ prompt.
2. Select the device for printing.

To display the IAs that cover Imaging routines used by other applications, perform the steps below.

1. Sign on to the FORUM system.
2. Select the DBA menu.
3. Select the INTEGRATION CONTROL REGISTRATIONS [IAs] menu.
4. Select the Custodial Package Menu [CUST].
5. Choose the “ACTIVE ICRs by Custodial Package” option.
6. Enter “IMAGING” for the package prompt.
#### Select the Context Management

This section includes:

- Context Management
- The Clinical Context Object Workgroup Protocol
- The Context Management Settings Tab
- Context Changes
- CPRS Tools Menu for VistARad
##### Context Management

Context Management (CM) allows users to choose a subject once in one application, and have all applications containing information on that same subject “tune” to the data they contain. This eliminates the need for the user to redundantly select the subject in the varying applications. In the healthcare industry, for example, multiple applications operating “in context” through use of a context manager would allow a user to select a patient ( *that is,* the subject) in one application. See the expanded discussion for end users in the *VistARad User Guide* , under **Context Management** .

Context Management is gaining in prominence in healthcare due to the creation of a standardized protocol, the Clinical Context Object Workgroup (CCOW) Protocol, enabling applications to function in a “context-aware” state.

##### The Clinical Context Object Workgroup Protocol

CCOW is a Health Level 7 (HL7) standard protocol designed to enable dissimilar healthcare software applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.

CCOW is the primary standard protocol used in healthcare to facilitate the Context Management process. Although both CCOW and non-CCOW compliant applications can use CM, the CCOW standard helps facilitate a more robust and near “plug-and-play” interoperability across applications.

When CCOW is available, the VistARad client uses CCOW to synchronize patient and user context management with the Computerized Patient Record System (CPRS) and other CCOW-enabled applications. A new Settings tab, Context Management, is used to enable context management; the setting Enable Context Management must be checked to use the context management functionality.

The TeleReader application requires CCOW to synchronize patient and user context with other applications such as CPRS and VistA Imaging Display. TeleReader cannot work if CCOW is unavailable. TeleReader will close if CCOW is not functioning properly.

##### The Context Management Settings Tab

The Context Management settings tab allows the user to manage how CM operates on the individual workstation. The user must check the Enable Context Management in order to use CM capability.

##### Context Changes

A context indicator (icon) appears at the top of the various VistARad windows to the left of the Patient Name and demographics. A Context menu item appears on the Manager and Viewer menu bars for options to Suspend/Resume context, etc. The application also automatically changes the displayed icon to reflect the change in context. See the expanded discussion for end users in the VistARad User Guide, under **Context Management** .

| **Icon**       | **Title**    | **Meaning**                                                                                                                                                                                                                                                                                                            |
|----------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image --> | **Changing** | Displayed when the Clinical Link is changing. This icon may appear so briefly that the user may not see it. It is displayed when the common (linked) patient is changing. For example, if VistARad is linked with CPRS and CPRS changes from one patient to another, this icon will display during the change process. |
|                |              | **Patient Context is Changing**                                                                                                                                                                                                                                                                                        |
| <!-- image --> | **Broken**   | Displayed when an application is not linked or the application is “out of patient context.” For example, if CPRS is linked and displaying one patient and VistARad is displaying a different patient, then VistARad is said to be “out of patient context” and will display this icon.                                 |
|                |              | **Patient Context is Broken**                                                                                                                                                                                                                                                                                          |
| <!-- image --> | **Linked**   | Displayed when an application is utilizing CCOW to maintain patient context with the CCOW server. For example, if VistARad is open and displaying the same patient (as defined by the CCOW server) for all linked applications, then VistARad will display this icon.                                                  |
|                |              | **Patient Context is Joined**                                                                                                                                                                                                                                                                                          |

#### CPRS Tools Menu Option for VistARad

Sites may also configure a new CPRS Tools menu option for launching VistARad from CPRS. Refer to the *VistA Imaging Installation Guide* , under **Associating Display and Capture with CPRS** , for background information on this configuration step. To configure for launching VistARad, add a Sequence, then enter this line of text exactly as shown (no line breaks, no extra spaces):

<!-- image -->

#### Mailman Messaging

This section describes the types of MailMan messages that are sent to a site’s MAG SERVER mail group.

The MAG SERVER mail group is established when VistA Imaging is installed. MAG SERVER initially contains the addresses of the person that installed VistA Imaging and of the VistA Imaging development team.

- Typical members of this group should be key IRM support staff, radiology managers, and/or ADPACS.
- Text pagers can be added to the MAG SERVER mail group as a “Remote Member”, provided that the domain portion of the remote mail member address is defined in the DOMAIN file (#4.2).

**Note:** The “ REDACTED ” is a required member of this group.

The members of the MAG SERVER mail group (aka the Local Imaging Mail Group) can be edited as described in Chapter 6 of the Background Processor User Manual.

##### “Image Cache Critically Low” Messages

The Image Cache Critically Low message is generated automatically when the Background Processor is unable to update the network write location within the VistA Magnetic Cache. This happens when the low level mark has been reached and the current location has only 5% (default value) of its capacity available at the time this message is generated.

The following is a sample Image Cache Critically Low Message:

<!-- image -->

This mechanism ensures that the remaining cache locations can be manually referenced during the free space recovery process (BP Purge) that the VistA Imaging System Manager MUST initiate. It is advised that while the purge is running the Auto Write Location update process be turned off, and that the Network Write Location and the PACS Write Location be manually updated to different locations. For more information, see Chapter 6 in the *Background Processor User Manual* .

##### “Image Site Usage” Messages

When VistA Imaging is installed, a process used to generate monthly Image Site Usage messages is established. Image Site Usage messages contain information about VistA Imaging statistics (images displayed, images captured, etc.) and the software and patch versions installed. The information in these messages is used for the VistA Imaging VISN (Veterans Integrated Service Network) Performance Monitor Report.

Image Site Usage messages are automatically generated at 4:01 AM (VistA System time) on the first day of each month, and will be sent to the MAG SERVER mail group. They can also be generated on demand as described on the next page.

A sample monthly Image Site Usage message is shown below.

<!-- image -->

<!-- image -->

<!-- image -->

The following sections explain how an Ad Hoc (on demand) version of an Image Site Usage message can be generated, describe the contents of a typical Site Usage message, and outline how automatic Image Site Usage message generation can be disabled.

###### Ad Hoc Image Site Usage Messages

To generate an on-demand version of the Imaging Site Usage message, perform the following steps.

1. Access the Imaging System Manager Menu [MAG SYS MENU] and run the Ad Hoc Enterprise Site Report option.
<!-- image -->

<!-- image -->
2. At the next two prompts, enter the date range that you want the report to cover. The prompts will default to the previous month.
<!-- image -->
3. After the report is generated, it will be sent in a MailMan message to the MAG SERVER mail group. The subject of the message will be “Ad Hoc Image Site Usage.”

###### Contents of an Image Site Usage Message

The contents of the Image Site Usage message are described in the following table. Note that some entries in the message are dependent on the Imaging components and patches installed— for example, entries specific to VistARad workstations will not be present at sites that do not use VistARad.

| **Entry Name**                                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Site                                             | The name of the medical center for which the message was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Reporting Period                                 | The time period covered by the report. Note that for Ad-Hoc reports, the date range specified by the user is indicated (which may be greater than the date range of the available data).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Date                                             | The date the message was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Domain                                           | The VistA mail domain name where the message was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2005 Entries                                     | The number of entries in the IMAGE file (#2005), based on the value in the IMAGE File header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2006.81 Entries                                  | The total number of Clinical Display and Clinical Capture workstations, as indicated in the IMAGING WINDOWS WORKSTATIONS file (#2006.81).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Production Account                               | The value is equal to "1" if the message is generated from the site's production database environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| WS DIS VERS                                      | An array showing installations of the VistA Imaging Clinical Display software. The array contains the following values:  VERSION ^ OPERATING\_SYSTEM ^ #INSTALLED  An entry will be generated for each unique combination of VERSION and OPERATING\_SYSTEM, for all Display workstations that have been accessed in the last 180 days.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| WS CAP VERS                                      | An array showing installations of the VistA Imaging Clinical Capture software. The array contains the following values:  VERSION ^ OPERATING\_SYSTEM ^ #INSTALLED  An entry will be generated for each unique combination of VERSION and OPERATING\_SYSTEM, for all Capture workstations that have been accessed in the last 180 days.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| WS VR VERS                                       | An array showing installations of the VistARad workstation software. The array contains the following values:  VERSION ^ OPERATING\_SYSTEM ^ #INSTALLED  An entry will be generated for each unique combination of VERSION and OPERATING\_SYSTEM, for all VistARad workstation that have been accessed in the last 180 days.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| VistARad Version                                 | The most recently installed version of VistARad. For the installation history of all instances of VistARad, refer to the “Imaging Package Installation HX” field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DICOM Error Log                                  | The total number of unresolved DICOM errors present in the DICOM Error Log (#2006.599) on the date the report was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DICOM Failed Images                              | The total number of entries in the DICOM FAILED IMAGES file (#2006.575) on the date the report was generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Queue File Count                                 | The total number of entries in the IMAGE BACKGROUND QUEUE file (#2006.03), including failed entries that will not be processed without user intervention. (Successfully processed entries are deleted from the file.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Unprocessed Queue Entries                        | The total number of unprocessed entries currently in the IMAGE BACKGROUND QUEUE file (#2006.03).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *N*  day Image Workstation Sessions              | The number of login sessions that occurred on all workstations (Display, Capture, and VistARad) for the period of the report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *N*  day Image Workstation Patients              | The number of patient lookups performed on Display and Capture workstations for the period of the report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| *N*  day Image Workstation Images                | The total number of images accessed from all Clinical Display and Capture workstations for the period of the report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *N*  day Image Workstation Captures              | The number of images acquired using Capture workstations for the period of the report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *N*  day VistARad WS Display                     | An array containing information for studies displayed on all VistARad workstations for the period of the report. The array contains the following values:  STUDIES ^ IMAGES ^ PATIENTS ^ RAD/NONRAD ^ ROUTED/LOCAL ^  STUDIES\_PER\_MODALITY  STUDIES: The number of studies displayed.  IMAGES: The number of images displayed.  PATIENTS: The number of patient records accessed.  RAD/NONRAD: The number of studies displayed by radiologists and non-radiologists, respectively.  ROUTED/LOCAL: The number of routed and non-routed exams displayed, respectively.  STUDIES\_PER\_MODALITY: An array of modalities and the numbers of displayed studies for each modality.                                                                                 |
| *N*  day VistARad WS Interpretations             | An array containing information for studies interpreted using all VistARad workstations for the period of the report. The array contains the following values:  STUDIES ^ IMAGES ^ PATIENTS ^ RAD/NONRAD ^ ROUTED/LOCAL ^  STUDIES\_PER\_MODALITY  STUDIES: The number of studies interpreted. IMAGES: The number of images interpreted. PATIENTS: The number of patient records accessed.  RAD/NONRAD: The number of studies interpreted by radiologists and non-radiologists, respectively (the value for non-radiologist interpretations should always be 0).  ROUTED/LOCAL: The number of routed and non-routed exams interpreted, respectively.  STUDIES\_PER\_MODALITY: An array of modalities and the numbers of interpreted studies for each modality. |
| *N*  day average daily routed images             | The average number of studies routed per day.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BP Vers. Num. Date                               | An array showing installations of the Background Processor client software. The array contains the following values:  CLIENT\_VERSION ^ OPERATING\_SYSTEM ^ #INSTALLED ^  BUILD\_DATE  An entry will be generated for each unique combination of VERSION and OPERATING\_SYSTEM for all Background Processor workstations.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VistA Image Version/Build                        | The most recent VistA Imaging KIDS installation, presented in an array with the following values:  RELEASE ^ PATCH ^ INSTALL\_DATE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DICOM Gateway Version                            | An array showing installations of the DICOM Gateway workstation software. The array is based on the contents of the DICOM WORKSTATION file (#2006.83), and contains the following values:  VERSION;PACKAGE\_NAME;PATCHES;BUILD\_DATE ^ #\_INSTALLED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Image file namespace(s)                          | The unique 1-, 2-, or 3-character filename prefix used for images stored at this site. If multiple prefixes are used by a site, each prefix will be shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| From FileMan Date Until FileMan Date             | Fields that provide information which may be helpful to support staff when the report contains unexpected values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Resolution                                       | Reports the number of workstations and the resolutions being used by their monitors.  CLASS ^ COLUMNS ^ ROWS ^ BITS ^ TYPE ^ COUNT  CLASS: Indicates if the monitors in this group have acceptable or unacceptable display capabilities.  COLUMNS^ROWS: The number or vertical and horizontal pixels.  BITS: The bit-depth.  TYPE : The workstation type (PC or Thin Client (TC)).  COUNT: The number of workstations.                                                                                                                                                                                                                                                                                                                                         |
| DICOM Capture                                    | An array showing the modality and number of images acquired by all DICOM Image Gateways during the reporting period. The array contains the following values.  MODALITY\_ABBR ^ IMAGES\_ACQUIRED ^ MODALITY\_NAME ^  GROUPS\_ACQUIRED  An entry will be generated for each modality that images are acquired from.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Import API                                       | Provides a count of images and image groups that were acquired by the Import API, broken down by sending application (origin).  SOURCE\_APP ^ #IMAGES ^ #GROUPS  Only present for sites that use the Import API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Clin Capture                                     | An array showing the PROCEDURE Field (#2005,6) and number of images acquired by all Capture workstations during the reporting period. The array contains the following values.  PROC\_FIELD ^ IMAGES\_CAPTURED  An entry will be generated for each procedure field entry that images are captured for.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Other Consents                                   | An array showing the number of captured consent forms , based on the contents of the SHORT DESCRIPTION field (#2005,10) for the report period.  SHORT\_DESC\_FIELD^ IMAGES  An entry will be generated for each SHORT DESCRIPTION field value containing the word “consent”. (For example, CONSENT and INFORMED CONSENT would be shown in two different entries).                                                                                                                                                                                                                                                                                                                                                                                              |
| Consent Forms                                    | The number of consent forms captured for the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Image file group parents                         | The number of image group parent entries added to the IMAGE  file (#2005) during the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Image file objects                               | The number of entries (excluding group parent entries) added to the IMAGE file (#2005) during the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Image file deletes                               | The number of entries deleted from the IMAGE file (#2005) during the report period. Note that this value indicates only those entries that were both added AND deleted within the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Document Images (TIF)                            | The number of scanned document images acquired during the reporting period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Document Groups (TIF)                            | The number of scanned document groups acquired during the reporting period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Total Image Objects for Place                    | The count for entire institutional database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Total Group Parents for Place                    | The count for entire institutional database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Total Image Entry Deletes for Place              | The count for entire institutional database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Unique Image Patients Captured                   | The number of individual patients that had new images added (using VistA Imaging) during the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Unique Image Patients Display                    | The number of individual patients that had images displayed using Clinical Display or VistARad during the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Unique Image Patients All                        | The total number of individual patients that had images displayed or captured during the report period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Total Non-Verified Images for Place              | Count for reporting period                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Total Verified Images for Place                  | Count for reporting period                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Total Duplicate Images for Place                 | Count for reporting period                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TLR SPECIALITY                                   | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR PROCEDURE                                    | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR LOCAL STUDIES                                | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR REMOTE STUDIES                               | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR LOCAL IMAGES                                 | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR REMOTE IMAGES                                | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR LOCAL READING TIME                           | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR REMOTE READING TIME                          | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR RESULTED LOCALLY BY TELEREADER               | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR RESULTED LOCALLY BY CPRS                     | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR RESULTED REMOTELY BY TELEREADER              | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR RESULTED REMOTELY BY CPRS                    | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR LOCAL ACQUISITION TIME                       | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TLR REMOTE ACQUISITION TIME                      | TeleReader reporting period count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Advance Directive Scanned Administrative Closure | <for future use>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Advance Directive Unscanned Manual Closure       | The number of signed Advance Directive notes that do not have attached scanned documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Advance Directive – UNC  -  *title*              | The number of Advance Directive notes without attached scanned documents, broken down by TIU note title.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Advance Directive Scanned Manual Closure         | The number of signed Advance Directive notes that have attached scanned documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Advance Directive – SMC  -  *title*              | The number of Advance Directive notes with attached scanned documents, broken down by TIU note title.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Imaging Package Installation HX                  | An array showing the installation history of the VistA Imaging KIDS software. The array is based on the PACKAGE file (#9.4), and contains the following values:  SEQ\_NUM ^ PACKAGE ^ VERSION ^ DATE ^ INSTALLER  SEQ\_NUM: Installation sequence.  PACKAGE: The package being installed. “Imaging” is used for the VistA Imaging KIDS packages; “MAGJ Radiology” refers to pre-3.0 Imaging installations of the VistARad software.  VERSION: The version number of the software.  DATE: The date the software was installed.  INSTALLER: The user account used to install the software.  Entries will be generated both for current and pre-existing software versions.                                                                                       |
| Local Network Locations                          | Each line shows information about a NETWORK LOCATION file (#2005.2) entry defined at the site. The first line (the one that begins with 0) is a header line that show the names of the values reported in subsequent lines. Subsequent lines show 2005.2 entries that:  - Have a Storage Type other than ‘Export’ or ‘Diagram’ - Are on-line  Are not ‘Routing’ shares.                                                                                                                                                                                                                                                                                                                                                                                        |
| Associated Institutions                          | This is the list of institutions whose designated users will use the imaging resources, Images, and shares associated with this this Imaging configuration while logged in to the primary host system. This is a function of the multiple platform design necessary to implement the consolidated Imaging system.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ACCESS TYPE(1)                                   | Clinical care for the patient whose images are being downloaded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ACCESS TYPE(2) ACCESS TYPE(B)                    | Clinical care for other VA patients                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ACCESS TYPE(A)                                   | DICOM transmit to SITE_NAME for reason 1,Clinical care for the patient whose images are being transmitted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ACCESS TYPE(3) ACCESS TYPE(C)                    | For use in approved research by VA staff                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ACCESS TYPE(4)                                   | For approved teaching purposes by VA staff                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ACCESS TYPE(D)                                   | DICOM transmit to SITE_NAME for reason 4,Approved teaching purposes by VA staff                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ACCESS TYPE(5) ACCESS TYPE(E)                    | For use in approved VA publications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ACCESS TYPE(6) ACCESS TYPE(R)                    | Authorized release of medical records or health information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ACCESS TYPE(F)                                   | DICOM transmit to SITE for reason 6: Copy to HIPAA Compliant Storage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ACCESS TYPE(16)                                  | For use in Veterans Benefits Administration claims processing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCESS TYPE(17)                                  | Prints from a Display Client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCESS TYPE(18)                                  | Prints from a Display Client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCESS TYPE(AWIVTC)                              | VistA Web Sessions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ACCESS TYPE(CAP)                                 | Clinical Captures                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ACCESS TYPE(DELETE)                              | Clinical Display Deletes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ACCESS TYPE(EXPORT->..)                          | GCC queue export events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ACCESS TYPE(IMGVW)                               | Imaging Displays                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCESS TYPE(IMGMM)                               | ?? We may need to examine the Windows Session file entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ACCESS TYPE(INDEX- 42)                           | IMAGE INDEX field sets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ACCESS TYPE(INDEX- ALL)                          | All INDEX type field sets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ACCESS TYPE(INDEX- 45)                           | Package Index updates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ACCESS TYPE(INDEX- CR)                           | Procedure/ Event Index updates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ACCESS TYPE(INDXCHG)                             | Image Index fields updates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ACCESS TYPE(LABRPT)                              | Lab Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ACCESS TYPE(LONGDES)                             | Parent Record Descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ACCESS TYPE(MAG ANNOT)                           | Imaging Annotation using CLINICAL_DISPLAY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ACCESS TYPE(MAG UTIL)                            | Storage Utility Updates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ACCESS TYPE(MEDRPT)                              | Medicine Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCESS TYPE(NOIMAGE)                             | Capture failure/corrupt records                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ACCESS TYPE(QFAIL)                               | Failed Setting JukeBox Queues                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCESS TYPE(P17CV)                               | Image Index Commits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ACCESS TYPE(RADRPT)                              | Radiology reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ACCESS TYPE(RESCIND)                             | Rescinded IMPORT Images                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ACCESS TYPE(RVDODVA)                             | VIX / VistA Rad Remote View DOD view of VA images                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ACCESS TYPE(RVVADOD)                             | VIX / VistA Rad Remote View VA view of DOD images                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ACCESS TYPE(RVVAVA)                              | VIX / VistA Rad Remote View VA view of VA image                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ACCESS TYPE(SURGRPT)                             | Surgical Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCESS TYPE(TIURPT)                              | TIU Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ACCESS TYPE(VR-INT)                              | VistA Rad Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ACCESS TYPE(VR-VW)                               | VistARad Display                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCESS TYPE(VR- VW/REM)                          | Remote VistARad Displays                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

###### MAGREPSTART and MAGREPSTOP

The MAGREPSTART and MAGREPSTOP options can be run to stop and restart the generation of monthly Image Site Usage messages. MAGREPSTART and MAGREPSTOP are not part of any menu, and should be assigned to a system manager or IRM before they need to be executed.

**Note:** Image Site Usage messages are used to fulfill FDA requirements related to medical device monitoring MAGREPSTART and MAGREPSTOP should only be run at the direction of the VistA Imaging Group. Use of these options is not necessary under normal conditions.

**Note:** If the generation of monthly Image Site Usage messages is suspended using MAGREPSTOP, no monthly messages will be generated until the process is restarted using MAGREPSTART.

##### Watermarking Messages

When a patient’s Advance Directive Note is rescinded, the images that are attached to that note are queued for watermarking with the text “Rescinded”. As part of the watermarking process, the subscribers of the G.MAG SERVER mail group will receive an email with information about the status of the operation when:

- Watermarking is successful
- Watermarking fails
###### “Rescinded” Watermarking Succeeded

Following is an example of the email message generated when the image was watermarked with “Rescinded”:

Subj: Import API Report [#31292] 06/22/11@08:14 8 lines From: PROVIDER, ONE In 'IN' basket. Page 1

<!-- image -->

1. 1^1 Image(s) Copied OK. 0 Errors.
2. MAGRSND;3110622.081451.3
3. 31
4. RESCINDED IMAGE FILE^\\SERVER1\IMAGE1$\SLA0\00\00\02\05\SLA00000020542.TIF

The preceding array was generated by the VistA Imaging Import API while processing a 'RESCIND' Image action.

Enter message action (in IN basket): Ignore//

###### “Rescinded” Watermarking Failed

Following is an example of the email message generated if the image could not be watermarked with “Rescinded”.

Subj: Import API Report [#31341] 06/23/11@09:52 9 lines From: PROVIDER, ONE In 'IN' basket. Page 1

<!-- image -->

1. 0^Image is already Rescinded.
2. Image(1) 0^&lt; *error message for rescind failure* &gt;
3. Image(1) RESCIND Action is Canceled.
4. Image(1) IEN: 20924
5. TIU Note: 697

The preceding array was generated by the VistA Imaging Import API while processing a 'RESCIND' Image action.

Enter message action (in IN basket): Ignore//

#### Imaging Site Reports

Imaging Site Reports is an ad hoc reporting tool used to evaluate user productivity and details of the variety of images being created by the VistA Imaging application. The audience for these reports will be the managers of the VistA Imaging application.

##### Document Counts Report

This is a report of the IMAGE file (#2005) of Image Types for an ‘Acquisition Site’ and a 'From' and 'To' Date/Time Image Saved date range. The report will give totals for each Acquisition Site, Object Type, for each user, within the Acquisition Site and date range. A grand total of images within the Acquisition Site and date range are given at the end of the report.

<!-- image -->

<!-- image -->

##### Image Count by User Report

This is a report of the IMAGE file (#2005) of Image Types for an ‘Acquisition Site’ and a 'From' and 'To' Date/Time Image Saved date range. The report will give totals for each Acquisition Site, Object Type, for each user, within the Acquisition Site and date range. A grand total of images within the Acquisition Site and date range are given at the end of the report.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

##### Means Test Report

This is a report of the IMAGE file (#2005) sorted by ‘Acquisition Site’, 'From' and 'To' Date/Time Image Saved date range, Export Location = ALL (including null), and Index Type From ‘MEANS’ to ‘MEANSZ’. Report detail will include: Acquisition Site, Patient Name, SSN, Index Type, Date/Time Image Saved, and Export Location.

<!-- image -->

##### Package Index Contains ‘Note’ Report

This is a report of the IMAGE file (#2005) sorted by ‘Acquisition Site, 'From' and 'To' Date/Time Image Saved date range, Short Description, and Package index containing ‘NOTE’. Report detail will include: Acquisition Site, Patient Name, SSN, Short Description, Date/Time Image Saved, and Image Saved by. Sub-counts and counts are given per Scanned By, with Short Description, within Patient.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

#### VistA Site Service

The VistA Site Service is a central repository of information used by Imaging components (such as Clinical Display) to connect to other sites. Using the site service eliminates the need to store other sites’ connection information locally. Local Imaging components access the site service using a special entry in the NETWORK LOCATION file (#2005.2) as described in Chapter 18.

The site service stores the following information for each site:

- Three-digit site number
- Site name
- Region ID (VISN number)
- Station number (field #99 in the INSTITUTION file (#4))
- VistA server hostname
- VistA server port number
- VIX server hostname
- VIX server port number

The last two values in the preceding list only apply at sites that have implemented the VistA Imaging Exchange (VIX) service. See the *VIX Administrator’s Guide* for details.

**Note:** If any of the information above changes, you must contact the VistA Imaging development group to have the site service updated. Incorrect or outdated information will interfere with remote image access.

Sites that have implemented a VIX will also need to update their VIX’s configuration after the site service has been updated. This is done by re-running the VIX Installation wizard which will detect the new connection information and reconfigure the VIX accordingly. See the *VIX Installation Guide* for more information.

#### VistARad External Relations

VistARad is able, optionally, to interface with the following types of non-VistA Imaging applications.

##### Voice Dictation Software

VistARad can be configured to interface with voice dictation software on the same diagnostic workstation, or elsewhere on the network. When a voice dictation interface is configured, VistARad sends identifying information for the current exam to the dictation software. Currently, Talk and PowerScribe are supported.

##### Medical Visualization/3D Reconstruction Software

VistARad can be configured to interface with medical visualization/3D reconstruction software on the same diagnostic workstation. When a medical visualization interface is configured, VistARad can send an exam to the visualization software for various manipulations such as multi-planar reconstruction, 3D reconstruction, and PET/CT Fusion. Currently, Toshiba’s Voxar 3D software is supported.

##### Medical Imaging Resource Center (MIRC) “Teaching File” server

VistARad can be configured to interface with a Medical Imaging Resource Center (MIRC) server. When this interface is configured, VistARad can send an image, an image set, or an entire exam of interest to the server as a “teaching file”. Additionally, VistARad can launch a web browser to the same server, making its teaching file contents available. Only one MIRC server interface can be configured, at any given time, per diagnostic workstation. The MIRC server will not be hosted on the diagnostic workstation.

More information on setting up the interfaces is available from Chapter 3 of the *VistA Imaging Installation Guide* .

### Chapter 13	Internal Relations

#### Dependencies

##### Entry/Exit Logic

The VistA Imaging System contains no options that rely on entry or exit logic from other options.

##### Synchronization

###### Clinical, Diagnostic, and Background Processor Workstations

The VistA Imaging software installed on the VistA Hospital Information System must be synchronized with compatible versions of the software installed on the individual workstations.

###### DICOM Modalities and PACS

The main purpose of the VistA Imaging DICOM Gateway is to act as an interface between external equipment and the VistA Hospital Information System. For each gateway function, in order for that function to be operational, the equipment on both sides of the interface must be up- and-running. In order to test and verify the operational status of equipment, see the *VistA Imaging DICOM Gateway User Manual* for a description of the programs **Ping** and **DICOM\_Echo.**

##### Radiology HL7 v2.1 Protocols

The VistA Imaging DICOM Gateway is dependent on Radiology protocols being active. VistA Imaging must be a subscriber to these protocols. Review the following protocols; the highlighted protocol is the VistA Imaging protocol subscriber. Please review the DICOM Installation manual in the section *VistA - PACS Radiology Interface Setup Instructions* for a step-by-step procedure to setup the protocols.

<!-- image -->

##### Radiology HL7 v2.4 Protocols

Currently HL7 Version 2.4 is the version of HL7 sanctioned for use in the VA enterprise and the version against which commercial PACS have been tested for conformance. Therefore, the v2.4 protocols will ordinarily be subscribed to by VistA Imaging in preference to the v2.1 protocols described in the previous section.

<!-- image -->

<!-- image -->

##### VistA Imaging ADT Protocols

Beginning with the release of Patch MAG*3.0*49, VistA Imaging uses HL7 messages to communicate ADT (admission / discharge / transfer) events directly to commercial PACS. ADT information had formerly been sent from the VistA DICOM Gateway using customized DICOM protocols, which have since been deprecated.

VistA Imaging generates and sends these messages through the VistA HL7 package using the following protocols.

<!-- image -->

<!-- image -->

##### Radiology Protocols (VistARad)

VistA Imaging VistARad can be set to automatically prefetch archived images for prior radiology exams. Prefetch is activated by subscribing to the RA REG protocol—the VistARad client protocol is MAGJ PREFETCH SEND/ORM. Review the example RA REG protocol below; the bolded protocol is the VistARad protocol subscriber. The Installation Guide has a step-by-step procedure to set up the protocol.

Patient Movement Protocol (DICOM)

<!-- image -->

The VistA Imaging DICOM gateway is dependent on the Patient Movement (DGPM MOVEMENT EVENTS) protocol being active. VistA Imaging must be a subscriber to this event protocol. The following is an example of this event protocol; the highlighted protocol is the Imaging protocol subscriber. ATTENTION: This is only pertinent if a VistA Imaging DICOM gateway configuration has been defined. Please review the DICOM Installation manual under section *VistA - PACS Radiology Interface Setup Instructions* for a step-by-step procedure to setup the protocols.

<!-- image -->

<!-- image -->

#### VistARad Internal Relations

VistARad interfaces with the following components of VistA Imaging.

##### VistA Site Service

VistARad will query the VistA Site Service if VistARad is configured to detect a local VistA Imaging Exchange (VIX) server. It may do this even if there is no local VIX available.

##### VistA Imaging Exchange (VIX) servers

If a local VIX server is accessible, VistARad will query the local VIX for relevant patient exams &amp; ancillary information from other remote sites, including those in the DoD. If configured for remote site monitoring, VistARad will also periodically query the VIX for exam list information from the configured monitored sites. Additional information on configuring VistARad for VIX- enabled reading and list monitoring is available in the “VistARad Settings” and “Monitoring Exam Lists of Remote Sites” sections of the VistARad User Guide.

This page is intentionally blank.

### Chapter 14	Package-Wide Variables

The VistA Imaging System does not contain any package-wide variables.

This page is intentionally blank.

### Chapter 15	Online Documentation

#### Online Help

Online help is available from the Help menu for Clinical Display, Clinical Capture, MagSys (clinical workstation configuration manager), Background Processor, Verifier, VistARad, TeleReader, TeleReader Configurator, and DICOM Importer II.

This page is intentionally blank.

### Chapter 16	Site-Specific Implementation

#### Site-Specific Implementation

##### Radiology Report Transcription Service

Local routines that automatically upload radiology reports from a transcription service should be reviewed and/or modified to ensure that proper consideration has been made for VistA Imaging. When an image is captured via the DICOM Image Gateway and the radiology case number does not have an existing radiology report entry (in file #74), then the VistA Imaging software creates a report stub entry for that case number with limited information. (See box below -- example of radiology report stub entry made by Imaging.) Please note that the stub report entry has an image pointer stored in the IMAGE field, no report status is on file and the activity log indicates that images were collected. The VistA Imaging System executes a Radiology Package API called CREATE^RARIC to create this entry. The RAD/NUC MED PATIENT file (#70) is also updated with the report pointer in the Report Text field.

Imaging has experienced problems when the auto-upload routine updates the REPORT TEXT field (#17) in the RAD/NUC MED PATIENT file (#70). Often the problems result from the program not expecting the Report file entry to exist at the time of the upload. However, the DICOM image capture process guarantees that at the time the transcribed reports are uploaded to the system, a Report file entry already exists, although no Report text nodes exist. Differences in implementations of the local upload programs at various sites have led to other problems as well. Therefore, if your site uses such a program for uploading and/or updating the Radiology report, you must carefully review all aspects of its functionality in light of the changes introduced by the VistA Imaging System.

Example: Radiology Report stub entry made by the VistA Imaging application.

<!-- image -->

##### HL7 MESSAGE TEXT File (#772)

VistA Imaging is a subscriber to the Radiology protocols that create HL7 messages. When Radiology protocols are executed, entries are created in the HL7 MESSAGE TEXT file (#772). The purging of this file is handled by the menu option for this application. Sites are requested to review the purging parameters for this file. Use menu option ‘Purge Message Text File Entries’ under the HL7 Main menu.

##### Incomplete DICOM Files Received on the DICOM Image Gateway

During the processing of DICOM files on the DICOM image gateway, it is possible for a modality or a PACS interface to send an incomplete file (possibly just header information without the image information). The image processing routine will log these entries in a temporary file (M global) and check periodically to see if the entire file has been received. If, after an hour’s time span, the file is still incomplete, the entry is removed from the temporary file (M global) and the file is renamed by appending “\_incomplete” to the filename. These files do remain in the DICOM\IMAGE\_IN directory and will require site personnel to research the possible failure. In addition, these files will require manual intervention for file maintenance (deletion). Please see the *VistA Imaging DICOM User Manual* for additional information.

### Chapter 17	Database Integrity Checking

The VistA Imaging System performs database integrity checking at the system level and within various applications.

#### VistA Imaging MAG SYS MENU

In the VistA Imaging system, the MAG SYS MENU has an Integrity Checker Menu with the following submenus:

- GM Global Move Inconsistency Report
- QA Pointer Inconsistency Report
- SC Scan Database for Integrity Issues
| **Where**   | **Means**                                                                                                                                                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GM          | Global Move Inconsistency Report [MAG\_IC\_RPT\_GM]  DESCRIPTION: Report from Imaging Integrity Check, limited to items required for Central Office  ROUTINE: RPT^MAGCRPT("CO")  UPPERCASE MENU TEXT: GLOBAL MOVE INCONSISTENCY REPO |
| QA          | Pointer Inconsistency Report [MAG\_IC\_RPT\_QA]  DESCRIPTION: Report from Imaging Integrity Check, including all items required for Quality Assurance  ROUTINE: RPT^MAGCRPT("QA")  UPPERCASE MENU TEXT: POINTER INCONSISTENCY REPORT |
| SC          | Scan Database for Integrity Issues [MAG\_IC\_SCAN] DESCRIPTION: Menu option to scan the Imaging database  EXIT ACTION: K MAGN100,MAGZ,VALID,Z ROUTINE: RPT^MAGGSQI(.Z,1E11)  UPPERCASE MENU TEXT: SCAN DATABASE FOR INTEGRITY IS     |

#### Clinical Display Application

The *Clinical Display Workstation User Manual* contains two references to Questionable Integrity (QI):

- A “Not Viewable” icon is displayed if the user attempts to view an image that has internal references that suggest some degree of integrity risk. For details, see the section Images That Are Not Viewable Due to an Error.
- An image that is blocked from view can be attributed to a number of reasons. One is if the image data does not pass the QI check, then the image is marked as QI. For details, see the section Blocked Images in the Abstracts Window.

Additionally, see the *Clinical Display Workstation User Manual* section *Deleting Images with Questionable Integrity (QI Issues)* in *Appendix C: Deleting Images* .

#### VistARad Application

The *VistARad User Guide* contains a reference to a “Severe Alert” icon that is displayed when a user attempts to view an exam and the system detects a data integrity problem with the exam. For details, see the section *Opening Exams* .

#### Verifier Application in the Background Processor

The BP Verifier provides a report called the Imaging Patient Integrity Issues in the DFNError Log file, which displays integrity issues with patient data. For details, see Section *5.7.1.4 DFN Log File* in the *Background Processor User Manual* .

### Chapter 18	Remote Image Views

#### Configuration for Remote Image Views

The Remote Image Views functionality uses a Network Location entry that points to the VistA Site Service to determine the server and port of remote VistA databases. This Network Location entry is present at all sites running Patch 45 or later. By default, this Network Location is enabled.

The URL defined in the VistA Site Service Network Location must be accessible to all clients attempting to access remote images.

Patch 111 provides the availability of the Broker Security Enhancement (BSE) for VistA Imaging clients. BSE is a token based authentication method that provides enhanced security over the previously used CAPRI login method.

Patch 94 modifies remote image view functionality in Display and TeleReader to make use of BSE. The client will first use BSE when attempting to connect to remote sites. If BSE fails, the client will use the CAPRI remote site login. When CAPRI is used, the system will generate a log entry to track the usage of the CAPRI authentication method. Using the BSE or CAPRI remote login method does not affect the usability of the applications, and it is transparent to the user.

The Kernel Team will release a patch to disable the CAPRI authentication method after Patch 94 is released. When the Kernel Team disables the CAPRI authentication method, only clients 94 and later will be able to connect to sites for remote image viewing.

##### Enabling/Disabling Remote Image Views for Site

To enable/disable Remote Image Views for your entire site, you may do so by changing the Operational Status of the NETWORK LOCATION file (#2005.2). Setting the Operational Status to On-Line enables Remote Image Views for your entire site. Setting the Operational Status to Off-Line disables Remote Image Views for your entire site. Enabling and disabling this option does **not** prevent remote sites from accessing your data. This only prevents users at your local site from accessing remote data.

<!-- image -->

<!-- image -->

##### Updating VistA Site Service URL

The remote image viewing capability uses a VistA Site Service to determine the server details of remote VistA0 systems. The following describes how to change the URL for this service if necessary.

<!-- image -->

### Chapter 19	Two-Facto Authentication (2FA)

#### Two-Factor Authentication (2FA) Overview

SSOi implemented by replacing the existing RPC Broker for those VistA Imaging applications that require VistA login credentials to access. The VistA Imaging login interface and workflow has changed from username and password to PIV card and PIN entry as part of the 2FA mandate. VistA Imaging components currently consume and reference a Delphi RPC Broker Development Kit (BDK) including a compiled BAPI32.DLL library. This RPC library exposes several procedure calls used to authenticate a user within a VistA application. As part of the VistA Imaging SSOi effort, we will be upgrading this library and BDK, (expected version XWB*1.1*65 currently in development and beta testing), which will have built-in integration to the IAM SSOi Secure Token Server (STS) authentication model including PIV/PIN prompt(s).

##### PIV/PIN Login

Figures 1 and 2 represent the screens that will display during login with 2FA SSOi integration. The user must have a valid PIV card attached to their computer, select the corresponding identity certificate, and enter their PIN.

<!-- image -->

PIV Identity Certificate Selection Display

PIV PIN Entry Display

<!-- image -->

#### Implementation History

MAG*3.0*178 introduced 2FA for the Clinical Capture application, replacing username and password login process.

MAG*3.0*181 introduced 2FA for the Clinical Display application, replacing username and password login process.

MAG*3.0*182 introduced 2FA for the Telereader application, replacing username and password login process.

MAG*3.0*184 introduced 2FA for the VistARAD application, replacing username and password login process.

MAG*3.0*206 introduced 2FA for the Importer application, replacing username and password login process.

### Appendix A Error Messages

#### Clinical Workstation Error Messages

| **Error Message**                                                      | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You don’t have the proper Security Keys to capture LAB images.         | The USE CAPTURE KEY field in the IMAGING SITE PARAMETERS file (#2006.1) has been turned on and the user has not been assigned the proper key. Please review the Security Key section in the  *VistA Imaging Security Guide.*                                                                                                   |
| Error in connecting to Server  \\servername\image\                     | Possible causes:  - The workstation has not been set up properly. - The account used to access the server has not been given the proper security level or has not been set up properly. - The listed server is down.  Find the associated error number and use the Help &#124; Error Code Lookup option in Imaging Display.    |
| AutoUpdating is disabled. Network Configuration file doesn’t exist.    | The MAGNET.ini file is not on the Network Update directory. Auto Update is not configured properly.  1. Contact network administrator and request that a copy of the MAGNET.ini file be placed in the Network Update directory. 2. Review the VistA Imaging System Installation Guide for proper configuration of Auto Update. |
| AutoUpdating disabled. The network update directory doesn’t exist.     | Cannot connect to the directory or it does not exist.  - User does not have privileges to the distribution directory. - Workstation log-on profile does not connect to Network Update directory. - Contact network administrator.                                                                                              |
| AutoUpdating disabled. Workstation isn’t configured for Auto Updating. | No update directory in the MAG308.ini file under section SYS\_AUTOUPDATE for variable DIRECTORY.  Run MAGASET.EXE from the Network Update directory. This will automatically define the DIRECTORY entry in the MAG308.ini file for the current workstation.                                                                    |

| **Error Message**                            | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoUpdating canceled. No Updates available. | The MAGSETUP.EXE file does not reside in the Network Update directory.  Contact the network administrator and request a copy of the MAGSETUP.EXE file be placed on the Network Update directory.                                                                                                                                                                                     |
| Abstract not found.                          | Possible causes:  - The abstract was removed from the server. - The abstract was not generated, or could not be written to the share. - Network problems. - Mapped Image share - Permission to access the share is not granted. Diagnostic process and corrective action: - Check file and folder permissions for the image shares. - Check to see if the files exist on the shares. |
| ERROR_ACCESS_ DENIED                         | Possible causes:  - Account or share permissions are not set up properly. - Account password was changed on the server, but not updated in the IMAGING SITE PARAMETERS file (#2006.1).                                                                                                                                                                                               |
| Error connecting to server.                  | Possible causes:  - Incorrect configuration. Diagnostic process and corrective action: - Check for error number in the message history window. Look it up using the Error Lookup option on the Imaging Display help menu. - Use ping or tracert to check the availability of the file server.                                                                                        |

| **Error Message**                                                            | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 Images on file.                                                            | Possible causes:  - Normal condition.  Diagnostic process and corrective action:  - This refers to images, not EKGs! A patient can have one without the other. Check "user preferences" to see if "always display EKG window" is selected. Click the EKG button to display the EKGs.                                    |
| The File Does Not Exist - Notify IRM.                                        | Possible causes:  - Missing or inaccessible file. Diagnostic process and corrective action: - Check to see if the file pointed by the database exist and is accessible.                                                                                                                                                 |
<!-- rpc-table -->
| Launching Imaging from CPRS causes RPC Broker dialog for access/verify code. | Possible Causes:  - Incorrect configuration. Diagnostic process and corrective action: - AutoSignon or multiple signon is not enabled for the site (KERNEL SYSTEM PARAMETERS file (#8989.3)) or  the user (NEW PERSON file (#200)).  - DEFAULT AUTO SIGN-ON cannot be set to “Disabled” in Kernel site parameters file. |
| Error Accessing Group Image - See VistA Error Log.                           | Possible causes:  - Database inconsistency. Diagnostic process and corrective action: - This error is found on the clinical display when you try to delete an "Abstract not Found" entry. The software identifies this entry as a group image and because you cannot expand the group, it cannot be deleted.            |

| **Error Message**                                                                       | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No MUSE Servers available.                                                              | Possible causes:  - No MUSE servers are configured in the Network Location file (#2005.2). - All MUSE servers in the Network Location file are configured as off-line.  Diagnostic process and corrective action:  - Add the MUSE Servers to the Network Location file. - Bring the MUSE servers back On-Line in the Network Location file. |
| No MUSE Servers available. Select a failed connection to see the error code.            | Possible causes:  - The application failed to connect to the all of the MUSE Servers. - MUSE servers are down. Diagnostic process and corrective action: - Click on a specific connection to see the error details.                                                                                                                         |
| No Muse EKGs on File for this patient                                                   | Possible causes:  - Patient ID (SSN) entered does not match MUSE patient ID. - The Patient has no Muse EKGs on file. Diagnostic process and corrective action: - Verify that the entered patient ID (SSN) is identical in the MUSE and VistA databases.                                                                                     |
| Error connecting to MUSE Server  \\&lt;ServerName&gt;\  &lt;ServerShare&gt;: status =53 | Possible causes:  - The network path was not found. - Permission problem on share. - MUSE server down.  Diagnostic process and corrective action:  - Be sure you can ping the server. - Ensure that the Physical Reference field in the Network Location file (#2005.2) is defined correctly.                                               |

| **Error Message**                                                                        | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Error connecting to MUSE Server  \\&lt;ServerName&gt;\  &lt;ServerShare&gt;: status =104 | Possible causes:  - Error message displayed when user selects a failed connection in the EKG selection list. The MUSE API flag is not enabled.  Diagnostic process and corrective action:  - This requires a call to GE so they can enable the API by installing a VOL000\system\sysinf\MUSEAPI.FIX file. - If this file was created with Notepad, be sure that it is not named MUSEAPI.FIX.TXT. Notepad adds a .txt extension when it creates a file. |
| Invalid File : MUSEAPI.DLL Call IRM  to get an updated file.                             | Possible causes:  - The MUSE API files were not installed correctly. - The MUSE API files are not installed. Diagnostic process and corrective action: - Call IRM for help - Reinstall VistA Imaging. #### 2.30 Troubleshooting General Startup Network Connection                                                                                                                                                                                     |

Check all the online VistA Imaging Tier 1 shares and Tier 2 shares by one of the following means to determine if the BP has access to the folders/files on the shares. There are several methods to test the connectivity:

1. From the Main BP window, select the **View &gt; Server Size** option. The free space should display for each share.

Main BP Window “View” Menu Options

<!-- image -->

1. Using Windows Explorer on the destination device (Image cluster or Windows-based Jukebox server), show the properties of the VistA Imaging Tier 1 shares and Tier 2 shares.

The VHAxxxIA account that is used to log into the BP Server should have READ/WRITE access to both the shares and folders/files on those shares.

**Note** : For sites using the Archive Appliance (AA), contact the HP Expert Center.

1. Open a DOS window. At the command prompt type *dir* [*\\server\share*](file://server/share) (the server could be a cluster server or the jukebox server). Traverse down a couple folders under the main level the folders/files should be visible
2. If any of these methods fail, open a DOS window and use the DOS *ping* command to see if the server is accessible on the network.
3. If the server is accessible, try mapping the share thru Windows Explorer. Explorer will display any error messages. If the server is not accessible, contact the network admin to troubleshoot.
###### Broker Failures

When the connection to the Broker fails:

- Verify the PORT and Server are correct in the registry
- Close and restart the application.
- Open a DOS window and use the *ping* command to see if the VistA server is available
- Verify that the listener is running in VistA
- Validate that the Access/Verify codes have not expired.
- Check the security on the Access/Verify account. Make sure:
- The All MAG* RPC's [MAG WINDOWS]menu option is assigned

###### Not Enough Server Cache

This message indicates that:

- The share on the server is not accessible. Follow the steps in section *0 Network Connection* to troubleshoot.
- The free space on the Image shares is below the % Server Reserve.
    - Disable the Auto Write Location Update option.
    - Set the write location manually to a share with cache space available.
    - If no share has adequate free space, create a second BP Server and manually launch a Purge (in **Error! Reference source not found. Error! Reference source not found.** ) to run on all shares. When the Purge has run and generated free space on a share, set the Write location manually to that share.

###### Not Enough Process Memory

Close all the applications and reboot the server. If the problem persists, contact the National Helpdesk **.**

###### Not Enough Write Cache Available

This message refers to the DiskXtender cache on the jukebox and indicates there is no free space on the jukebox share, or for Archive Appliance sites a possible space issue exists.

- Verify the share is accessible. Follow the steps in section *0 Network Connection* to troubleshoot.
- Click the Extended Drive in DiskXtender to see if there is free space available. Also, use Windows Explorer on the JB server to see if Windows is properly reporting free space.
- Check the Move Group within the DiskXtender application to see if there are platters with available space. If not, add additional optical platters to the Move Group. See the *DiskXtender User Manual* .
- Run a Drive Scan on the share. See the *DiskXtender User Manual* .

##### Queue Processor Startup

| **Message**                                                                                           | **Explanation**                                                                                              | **Action**                                                                                                                          |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Create Process failed'+ProgramName                                                                    | A system error occurred staring the process                                                                  | Follow your local, VISN, or regional procedures for problem resolution/escalation                                                   |
| Increment  *queue\_name*  Ptr^Failed                                                                  | The QUEUE POINTER (#1) in the IMAGE BACKGROUND QUEUE POINTER file  (#2006.031) in VistA could not be updated | On the main BP window, use the Edit > Refresh Queue Counts to correct the current counts. Close the BP and restart the application. |
| Initialization Failure^Log Files at: C:\Program Files\Vista\Imaging\BackprocLo g\BackProc\BPError.log | Log file could not be created                                                                                | Check permissions on the log folder                                                                                                 |
| RAID groups not properly configured                                                                   | An active RAID Group has no online shares                                                                    | Make sure online RAID Group has online shares.  Use the Network Location Manager to reset your RAID groups                          |
| Requeue Failure trying to Requeue:                                                                    | An attempt to re-queue a failed queue entry failed                                                           | Use the Queue Manager and step past the queue entry. Determine the problem with the entry that would not re-queue.                  |

| **Message**                                                                                                                                                                                                               | **Explanation**                                                                                                                          | **Action**                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SetTime Handle – Destin: C:\Program Files\Vista\Imaging\BackprocLo g\BackProc\BPError.log  Access is Denied                                                                                                               | Could not write the Access Date on the log file                                                                                          | Check the file permissions on the log folder listed.                                                                                                                                                                                                                                                                                |
| The Background Processor client software is version  *n.n.n.n*  .  VistA Imaging Host system has version  *m*  installed. Please update to compatible client and host software. Shutting down the Background Processor... | The client software that is installed does not match the KIDS version installed on VistA.                                                | Install the correction version of the KIDS and client software.                                                                                                                                                                                                                                                                     |
| The Patch 135 KIDS install on the VistA host system is required for this Version of the:  *site name*  BP Queue Processor                                                                                                 | The KIDS file for this most recent patch has not been installed in VistA.                                                                | Install the KIDS file on VistA.                                                                                                                                                                                                                                                                                                     |
| The Site parameter context could not be determined. The application will terminate.                                                                                                                                       | The PLACE global is corrupt                                                                                                              | Follow your local, VISN, or regional procedures for problem resolution/escalation.                                                                                                                                                                                                                                                  |
| <!-- image -->                                                                                                                                                                                                            | The Broker is not properly configured in the registry of this server.                                                                    | Edit the registry on this server to meet the connection requirements on the host server with proper host server name and port number.  Note: on 64 bit OS the hive is [HKEY\_LOCAL\_MACHINE\SO  FTWARE\Wow6432Node\Vista\B roker\Servers]                                                                                           |
| This server is not yet configured for BP queue task processing!                                                                                                                                                           | There is either no BP Server name with this network name in the BP Server file (#2006.8) or there are no task(s) assigned to this server | Create a BP Server through the GUI and assign tasks to it BP Servers menu/tab                                                                                                                                                                                                                                                       |
| InitLogFile: procedure NewCreationDate &#124; SetFileTime Failed  *WIN32\_Error*                                                                                                                                          | Log File Initialization error                                                                                                            | See above The log files should not have a local drive in the BP Server Parameters. The designated path should be a network share. Note: The Computer name is automatically set by the application software. Setting the server name in the parameter will create a confusing duplicate descendant server tree on the Network share. |

#### Runtime

| **Message**                                                                                        | **Explanation**                                                                                                                                                                                    | **Action**                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0^Accusoft Control creation error : &lt;  *error message*  &gt;                                    | The Import API uses the AccuSoft Image Gear Toolkit to create the watermarked image. If an error occurs during the creation of AccuSoft controls, the error message displays describing the error. | The AccuSoft controls are installed during MAG*3.0*135 installation. If this error message occurs, contact the VistA Imaging system manager.                                                                                                                          |
| 0^Image is missing from input data.                                                                | The image to be watermarked is not in the Import Queue Data.                                                                                                                                       | Check the IMAGE file (#2005) to see if the data is corrupt.                                                                                                                                                                                                           |
| 0^Watermark failure : &lt;  *error message*  &gt;                                                  | The process of burning the “Rescinded” watermark onto the image file failed.                                                                                                                       | The AccuSoft ToolKit could not create the watermarked image.  Check if the rescinded bitmap exists in the image directory  **C:\Program Files\vista\Imaging\Bmp\MagRe scinded.bmp**  .  You may need to reinstall MAG*3.0*135 to correct AccuSoft ImageGear problems. |
| An Abstract for this file is on the Jukebox, a JBTOHD is being queued                              | ABSTRACT - The abstract pointer on the Tier 1 is empty. The abstract will be copied from the jukebox                                                                                               | None                                                                                                                                                                                                                                                                  |
| Could not complete                                                                                 | DELETE - file could not be deleted                                                                                                                                                                 | Check permissions on Tier 1  share                                                                                                                                                                                                                                    |
| Could not complete/Requeued                                                                        | DELETE - file could not be deleted                                                                                                                                                                 | Check permissions on Tier 1  share                                                                                                                                                                                                                                    |
| Current Tier 1 Shares^Exception: No RAID group Assigned                                            | The Tier 1 share must be assigned to a RAID Group                                                                                                                                                  | On the BP main window, use Edit  &gt; Network Location Manager to assign the Tier 1 share(s) to a RAID Group.                                                                                                                                                         |
| False Positive Copy f  *ilename(Source)*  ,  *filenames source file size*  ,  *file size(jukebox)* | File sizes on source and destination don’t match. File not copied.                                                                                                                                 | Determine if images are for different patients                                                                                                                                                                                                                        |
| File copied was of size zero                                                                       | IMPORT - The file size is zero                                                                                                                                                                     | Resend image from import source                                                                                                                                                                                                                                       |

- The MAG SYSTEM security key is assigned

| **Message**                                                   | **Explanation**                                                                                                               | **Action**                                                                        |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| File of size zero created then deleted                        | MAKEABS - file of zero length was created by Mag_MakeAbs.exe. It was deleted.                                                 | Follow your local, VISN, or regional procedures for problem resolution/escalation |
| File was not found                                            | IMPORT - file does not exist on the image share                                                                               | Resend image from import source                                                   |
| *filename*  Source file does not exist.                       | Could not find source file                                                                                                    | Run Verifier to correct VistA pointers                                            |
| *fileshare*  : Cannot connect to the Export Share.            | EXPORT - Cannot map to the remote share                                                                                       | Check for network connectivity. Check permissions..                               |
| ForceDirectories failed:                                      | DELETE - could not create directory on jukebox share                                                                          | Check permissions on jukebox share                                                |
| Image File type:  *filename.ext*  is an Unsupported Format    | ABSTRACT - The Full file is not a supported Imaging file type. So the abstract cannot be created.                             | Examine the "foreign" file and determine if the extension was misnamed.           |
| Invalid Imaging Network Username or Password.                 | The BP processor operator does not have write permissions on Tier 1, Tier 2, the Network Log file share, or the IMPORT share. | Check permissions on the share the write share associated with this error.        |
| Jukebox is not available:  *filepath Volume label*            | Tier 2- the jukebox share is not available                                                                                    | Ping the jukebox server. Check the jukebox share permissions.                     |
| Jukebox sourcefile unavailable                                | JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is not set.                                  | None                                                                              |
| JUKEBOX:  *queue \_pointer*  ^f  *ile\_extension*  Not copied | JUKEBOX - Alternate file extension (i.e. .TXT) was not copied                                                                 | Check file permissions                                                            |
| Login Message^Pausing 3 minutes and will then retry           | AUTOLOGIN - could not relog into the Broker                                                                                   | Check for network connectivity.                                                   |
| Login Message^Silent Login attempt failed!                    | AUTOLOGIN - could not relog into the Broker                                                                                   | Check for network connectivity.                                                   |
| Make AbstractError / abs is already present                   | ABSTRACT- file already exists at the Tier 1 location specified in VistA                                                       | None                                                                              |
| Make AbstractError / f  *ilename*                             | MAKEABS- the  Mag\_MakeAbs.exe could not create the abstract file                                                             | Follow your local, VISN, or regional procedures for problem resolution/escalation |

| **Message**                                                                             | **Explanation**                                                                                                                                                 | **Action**                                                                                                       |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| NetConError Using User credentials  *WIN32\_Error*                                      | GCC - Could not logon to the remote location with the Username/Password in VistA                                                                                | Correct the Username/Password for the  GCC location in VistA                                                     |
| NetConError,'There is no password associated with this Network Location:  *share\_name* | GCC - The password field is empty for this Network Location                                                                                                     | Enter a password for this GCC location                                                                           |
| No Image file entry was created!                                                        | IMPORT - an IEN was not created in the image file                                                                                                               | Resend image from import source                                                                                  |
| No Jukebox sourcefile available  / Attempting Abstract Queue                            | JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is set. The Queue Processor will attempt to make on from the Full or BIG file. | None                                                                                                             |
| No Tracking ID IMPORT failed                                                            | IMPORT - unique Tracking ID parameter is missing from IMPORT                                                                                                    | Resend image from import source.  Use the Queue Manager to check the Import queue Properties for failed IMPORTS. |
| Problem renaming log file:  *filename*                                                  | Could not rename log file to a versioned copy                                                                                                                   | Check permissions on the existing folder/files                                                                   |
| *queue\_pointer*  '^Size Mismatch  *queue\_type*  copy not overwritten.                 | File sizes on source and destination don’t match. File not copied.                                                                                              | Determine if images are for different patients                                                                   |
| SetFileTime Failed                                                                      | Could not set Access date on the log file.                                                                                                                      | None                                                                                                             |
| The BP Queue executed a scheduled RAID Group Advance                                    | The Queue Processor performed a the scheduled RAID Group Advance to the next group with adequate free space per the site parameter configuration                | Verify that the tape backup schedule are synchronized with this Tier 1 write location update                     |
| The BP Queue executed an automatic RAID Group Advance                                   | The Queue Processor performed an automatic RAID Group to the next group with adequate free space per the site parameter watermark configuration                 | Verify that the tape backup schedule are synchronized with this Tier 1 write location update                     |
| The jukebox copy:  *filename*  does not exist -- attempting a copy...                   | DELETE -Could not find the file on jukebox shares. Try to copy from Tier 1 shares to jukebox                                                                    | None                                                                                                             |
| The RAID share is not on-line                                                           | IMPORT - The Tier 1 share is not available                                                                                                                      | Check the permissions on the image share indicated                                                               |

| **Message**                                                     | **Explanation**                                                               | **Action**                                                                                                        |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| The  *src\_filename*  to  *dest\_filename*  copy failed.        | EXPORT - file could not be copied                                             | Check for network connectivity. Check permissions.                                                                |
| The VistA cache file:  *filename*  not found                    | DELETE -Could not find the file on Tier 1share to delete                      | None                                                                                                              |
| This Server is not yet configured!                              | A BP Server has not been associated with this server.                         | Create a BP Server for this processor                                                                             |
| Unable to copy to the Jukebox: Not enough write cache available | JUKEBOX - The Tier 2 share is not available or is full                        | Add new platters to the jukebox. Determine why the Tier 2share is full. Possibly add new platters to the jukebox. |
| Zero size  *queue\_type*  copy NOT overwritten                  | Zero size file on the destination could not be overwritten                    | Remove zero size file                                                                                             |
| No Connection to VISTA                                          | The VistA Access and Verify codes of the user or service account are invalid. | Update the Access and Verify codes on the BP Site parameter window.                                               |


##### Verifier Start/Run

| **Message**                                                                                                                                                          | **Explanation**                                                                                           | **Action**                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| About to exit without processing: 0                                                                                                                                  | There are no IEN records within the range.                                                                | Choose another IEN range                                                                                      |
<!-- rpc-table -->
| Broker Connection to server could not be established!                                                                                                                | VistA RPC Broker is not currently in a listening state OR the application has timed out.                  | Close the application and restart. Check with the VistA system manager for the status of the Broker listener. |
<!-- rpc-table -->
| CC:createcontext  ("MAG WINDOWS") could not be established!                                                                                                          | The user does not have All MAG* RPC's [MAG  WINDOWS] menu option assigned.                                | Assign the user this menu option.                                                                             |
| lbCacheShare.items.Count < 1: MAGQ SHARES                                                                                                                            | There are no online, non-router VMC shares.                                                               | Use the Queue Processor’s Network Location Manager to check/add the shares.                                   |
| Invalid Input Range                                                                                                                                                  | The From and To values entered in the Range are not correct (e.g. Start: 0 End: 0).                       | Enter a valid  *From*  and  *To*  range.                                                                      |
| jukebox shares are not setup                                                                                                                                         | The Tier 2 share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).                    | Create/Edit the Tier 2 shares in the Network Location Manager on the Queue Processor.                         |
| This workstation is not currently setup as a Background Processor.                                                                                                   | There is no BP Server set up for this machine.                                                            | Use the option  *BP Servers*  on the Queue Processor to register this server.                                 |
| Verifier client software is version nnn. VistA Imaging Host software is version mmm. Please update to compatible client and host software. Shutting down Verifier... | The version of the KIDS file installed on VistA does not match the executable version on the workstation. | Install the latest KIDS and client software.                                                                  |
| VistA shares are not setup                                                                                                                                           | The image share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).                     | Create/Edit the shares in the Network Location Manager on the Queue Processor.                                |

##### Output HTML Messages

| **Message**                            | **Explanation**                                                                                     | **Action**                                                                                        |
|----------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Aggregate JB Copy Error:               | Could not copy from alternate Tier 2 to the current Tier 2 Write location.                          | Check permissions                                                                                 |
| Abs to JB:                             | Abstract has been created and copied to the jukebox                                                 | None                                                                                              |
| Aggregate Function - Enabled           | Software is enabled to copy files from secondary jukebox, if necessary                              | None                                                                                              |
| BIG Aggregate Failed                   | Could not copy BIG file from secondary jukebox                                                      | Check file existence/permissions                                                                  |
| Create Process failed                  | Could not create process on VistA for Verifier                                                      | Check Error Trap                                                                                  |
| Empty FBIG node                        | "FBIG" node has no pointers set in IMAGE file (#2005) record.                                       | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.         |
| File of size zero created then deleted | Abstract file created of size zero. Then it is deleted.  (Likely corruption of BIG and/or TGA file) | None                                                                                              |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary Tier 2.                                                     | Check file existence/permissions                                                                  |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary Tier 2.                                                     | Check file existence/permissions                                                                  |
| Images JB share is OFF-LINE:           | Tier 2 is offline                                                                                   | Set Tier 2 back ONLINE                                                                            |
| Make AbstractError                     | Abstract file could not be created from TGA/BIG  (BIG/TGA not found or image file corruption).      | Check shares for existence of BIG/TGA file. If not found, restore BIG/TGA file from backup tapes. |
| New Abs to CWL                         | An abstract file has been created and copied to the current write image share                       | None                                                                                              |
| No ABS file VC Ptr Cleared             | Abstract file not found on the Image share                                                          | None                                                                                              |

| **Message**                           | **Explanation**                                                                                 | **Action**                                                                                  |
|---------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| No ABS file VC Share OFF- Line        | Image share is offline at location of abstract file                                             | Set share back online and re-run Verifier                                                   |
| No ABS JB Files                       | No abstract file found on Tier 2                                                                | Check shares for existence of ABS file. If not found, restore ABS file from backup tapes    |
| No Acquisition Site in Image file     | The ACQUISITION SITE field #100 in the IMAGE file (#2005) is missing. This is a required field. | Contact IRM  Update the field with the proper site ID.                                      |
| No FULL JB Files                      | FULL file not found on the Tier 2                                                               | Check shares for existence of Full file. If not found, restore Full file from backup tapes  |
| No FULL VC Files                      | FULL file not found on the Tier 1 share                                                         | None                                                                                        |
| No jukebox BIG Files                  | BIG file not found on the Tier 2                                                                | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.   |
| No jukebox FULL Files                 | FULL file not found on the Tier 2                                                               | Check shares for existence of Full file. If not found, restore Full file from backup tapes. |
| No Network References                 | No IMAGE file (#2005) record exists for this image                                              | Re-import image thru the Capture client                                                     |
| No Network References: Archived Image | Image has been archived, resides in the IMAGE AUDIT file (#2005.1)                              | None                                                                                        |
| No VC BIG Files                       | Could not find the BIG file on the Tier 1 share                                                 | None                                                                                        |
| Not Certed                            | Could not find/create file type on  Tier 2                                                      | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.   |
| Problem rename log file:              | Permission problem with log file                                                                | Set WRITE permissions set on share/folder/file for Windows login account.                   |
| Text file Patient ID not in VistA     | Could not locate patient ID in VistA                                                            | Contact IRM                                                                                 |
| TXT to BIG VC                         | Copy TXT file to same share as BIG file                                                         | None                                                                                        |
| TXT to FULL VC                        | Copy TXT file to same share as FULL file                                                        | None                                                                                        |
| **"Check Text" Option Messages**      |                                                                                                 |                                                                                             |
| Text File Corruption Error Type 1:    | Text file is binary or unreadable                                                               | Restore file from Tier 2/backup tapes                                                       |
| Cannot determine Text file type:      | Foreign text file was not likely generated on the image gateway                                 | Restore file from Tier 2/backup tapes                                                       |
| Text File Corruption Error Type 2:    | Text file is ASCII but has unprintable characters or truncated                                  | Restore file from Tier 2/backup tapes                                                       |
| Text/Image DFN Mismatch:              | Patient ID in text file does not match that in VistA                                            | Future utility patch                                                                        |

| **Message**                   | **Explanation**                                                          | **Action**                              |
|-------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Text/Image SOP/UID Mismatch   | The Series Instance UID in the text file does not match the one in VistA | Future utility patch                    |
| Text/Image Study/UID Mismatch | The Study Instance UID in the text file does not match the one in VistA  | Future utility patch                    |
| Text/Image UID Mismatch       | SOP and/or Study UID are/is blank in text file                           | Future utility patch                    |
| Updated Text file             | Text file has been edited                                                | Validate file has been copied to Tier 2 |
| No SSN Found                  | Patient ID field missing in text file                                    | Future utility patch                    |

##### Integrity Messages on Patient Data

There are integrity issues that will prevent their respective images from being displayed and others that will not impact the viewing. See Appendix C for sample output.

###### Conditions Preventing Viewing

An integrity error message will be generated when the image is retrieved for viewing on these conditions and the patient image will not be viewable until the condition is corrected or the user has the proper key to view these images.

| **Message**                 | **Explanation**                                                                                                                                                          | **Action**           |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| No Image Ptr in AP          | The Clinical Association Report (AP) for this image does not contain an image entry that points back to this image.                                                      | Future utility patch |
| GP has no images            | Image series that does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition. | Future utility patch |
| Conflicting AP & Image DFNs | The patient file reference (DFN) in the Clinical Association Report (AP) does not match the DFN in the IMAGE file (#2005).                                               | Future utility patch |
| Invalid Image Ptr to AP     | The Clinical Association Report (AP) has image references that are not in the IMAGE file (#2005).                                                                        | Future utility patch |
| Conflicting GP and GO DFN   | The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.                                                                 | Future utility patch |

| **Message**                          | **Explanation**                                                                                                                                                                                                                      | **Action**           |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| GP & GO AP Mismatch                  | The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.                                                                                                                             | Future utility patch |
| GP Missing GO Ptr                    | The Group Object multiple of the referenced Group Parent does not reference this group object.                                                                                                                                       | Future utility patch |
| No AP Mult Ptr                       | This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005).record is missing the  *PARENT DATA FILE IMAGE*  *POINTER*  (#17) for a Clinical Association Report (AP). | Future utility patch |
| GO DFN mismatches                    | Some image file Group Objects have different PATIENT references (DFN).                                                                                                                                                               | Future utility patch |
| Image entry is structurally abnormal | The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non-Group image (NG) is corrupt.                                                                                                     | Future utility patch |
| Missing Group Objects                | The Group Parent has Group Object references that are missing.                                                                                                                                                                       | Future utility patch |
| DFN Mismatches in AP Image Mult      | The Clinical Association Report (AP) references a Group Parent that has image files with a different PATIENT reference (DFN) than the report.                                                                                        | Future utility patch |

###### Conditions Allowing Viewing

The following integrity issues will **not** prevent their respective images from being displayed. These are informational messages.

| **Message**     | **Explanation**                                                                                                                                                                                        | **Action**           |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| No AP Ptr       | The IMAGE file (#2005) record is missing the PARENT DATA FILE# (#16) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified.            | Future utility patch |
| No AP entry Ptr | This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the  *PARENT GLOBAL ROOT DO*  *(#17)*  for a Clinical Association Report (AP). | Future utility patch |

##### Purge

| **Message**                                                               | **Explanation**                                                                                                                      | **Action**                                 |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Broker Reconnection failed                                                | Auto login after a Broker disconnect failed                                                                                          | Check network. Contact IRM                 |
| Create Process failed  *ProgramName*  ,                                   | Windows failed to create a process.                                                                                                  | Reboot the server.                         |
| Express Purge Rate limit reached:  *PurgeRate*  on share:  *CurrentShare* | The purge terminated on the given share because Express Purge was active and the Purge process exceeded the user defined purge rate. | None                                       |
| File Delete failure:  *filename*                                          | The file listed could not be deleted.                                                                                                | Check permissions on the share/folder/file |
| File in use:  *filename*                                                  | The log file is in use                                                                                                               | Exit from the Purge and restart            |
| File purged:  *filename*  . 'The Image file (#2005) was not updated'      | The file was deleted on Tier 1, but the pointer in VistA could not be updated.                                                       | Validate the IEN record exists in VistA.   |
| Findfirst failed  *filename*                                              | The directory traversal failed                                                                                                       | Exit from the Purge and restart            |
| Log File Archival reset to:  *FilePath2*  instead of:  *FilePath1*        | The logs files are now being stored at another location.                                                                             | None                                       |

| **Message**                                                                       | **Explanation**                                                                | **Action**                                                                    |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Login Message^Broker Reconnection Successful                                      | After a Broker disconnect, the application was able to reconnect to VistA.     | None                                                                          |
| Login Message^Pausing 3 minutes and will then retry                               | After a Broker disconnect, the application tries 3 times to reconnect to VistA | None                                                                          |
| Login Message^Silent Login attempt failed!                                        | After a Broker disconnect, the application was not able to reconnect to VistA. | Check network connections.                                                    |
| NewCreationDate^SetFileTime Failed  *filename*                                    | Could not set the date of last Access on filename                              | None                                                                          |
| Non-Connection related Broker error                                               | Broker disconnected                                                            | Check VistA for error trap                                                    |
| NOT Purged criteria:  *EvalCriteria*  NOT PURGED- JUKEBOX QUEUED  *filename date* | File was not deleted. See Section  6.4 Purge Criteria.                         | None                                                                          |
| Problem renaming log file  *filename1*  -&gt;  *filename2*                        | Could not rename log file to versioned log file name                           | Check permissions.                                                            |
| Purge Criteria:  *EvalCriteria filename filedate*                                 | See Section 6.4 Purge Criteria                                                 | None                                                                          |
| Purge Criteria:  *EvalCriteria*  NOT PURGED  *filename filedate*                  | File was deleted. See Section 6.4 Purge Criteria                               | None                                                                          |
| Silent Login attempt                                                              | Broker was disconnected. Auto login is initiated.                              | None                                                                          |
| Start Date failure                                                                | Problem with Date of Last Purge on Scheduled Purge                             | Contact IRM to clear the record in the Imaging Site Parameter file (#2006.1). |

##### Import API

The Import API OCX (IAPI OCX) traps System Error Codes in all of the Windows function calls that are made during Import processing. When an Error occurs, the Error Code and Error Description are listed in the Result Array that is returned by the Import API.

Descriptions of the error codes are returned using the Windows function: GetLastError.

**Note** : The System Error Codes are very broad. Each one can occur in one of many hundreds of locations in the system. Consequently the descriptions of these codes cannot be very specific. Use of these codes requires some amount of investigation and analysis. Make note of the run- time context in which these errors occur.

Along with the System Error code and description, the values of other IAPI parameters will also be listed in the Result Array when an error occurs. The other values will help determine the exact cause of the error.

Not all of the values listed below will be returned in the Result Array. Depending on the type of error, some values will be listed while others may or may not exist at the point in the process when the error occurred.

An example of this is the Access Verify codes. These values will be listed if an error occurs during login to the dabatase only.

Other values include:

- Import Queue number
- Image Share File Path
- Password
- Tracking ID
- Server\Share Name
- Access Code
- File to Import Full Patch
- Username
- Verify Code
###### Example

The following is an example of returned Error array

(0): 0~ERROR: 0 Images copied

1. : MAG135;20130122 12:31:21-43	&lt;&lt; Tracking ID
2. : 21	&lt;&lt; Import Queue Number
3. :	Image Security for Filename: \\vhaiswclu4\User1$\TestImages\CardioMR.jpg
4. :	ParseServerShare: Input= \\vhaiswclu4\User1$\TestImages\CardioMR.jpg
5. : ------	ExtractFilePath : \\vhaiswclu4\User1$\TestImages\
6. : ------	Result \\Server\Share: \\vhaiswclu4\User1$
7. : ------  Confirming UserName and Password...
8. : ------  Username: vhamaster\vhaiswIU Password Access1.
9. :	OSConnectToServer Start : 1/22/2013 12:32:35 PM
10. :	GetLastError: 1219 - Multiple connections to a server or shared resource by the

same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again

1. : ------  Credential conflict, continuing as current User...
2. :	OSConnectToServer Success: 1/22/2013 12:32:35 PM
3. :	Success: Image Directory is accessible. \\vhaiswclu4\User1$
4. : Error copying \\vhaiswclu4\User1$\TestImages\CardioMR.jpg

to Server : 30168~\\isw-kirin-lt\image1$\GFB0\00\00\03\01\~GFB00000030168.JPG

1. :	:File doesn't exist : \\vhaiswclu4\User1$\TestImages\CardioMR.jpg
2. : 1~VistA Image Entry deleted: 30168
3. : 1~Status Callback was called

The most common types of errors that will occur in the IAPI OCX are network connection errors and network read/write errors.

The exact errors that may occur at a site are unknown, but the most probable are listed below:

2: The system cannot find the file specified

3: The system cannot find the path specified

4: The system cannot open the file

5: Access is denied

8: Not enough storage is available to process this command

1: The access code is invalid

14: Not enough storage is available to complete this operation

15: The system cannot find the drive specified

19: The media is write protected

20: The system cannot find the device specified

21: The device is not ready

25: The drive cannot locate a specific area or track on the disk

26: The specified disk or diskette cannot be accessed

29: The system cannot write to the specified device

30: The system cannot read from the specified device

31: A device attached to the system is not functioning

32: The process cannot access the file because it is being used by another process

33: The process cannot access the file because another process has locked a portion of the file

36: Too many files opened for sharing

39: The disk is full

51: Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator

52: You were not connected because a duplicate name exists on the network. Go to System in Control Panel to change the computer name and try again

53: The network path was not found

54: The network is busy

57: A network adapter hardware error occurred

59: An unexpected network error occurred

64: The specified network name is no longer available

65: Network access is denied

67: The network name cannot be found

70: The remote server has been paused or is in the process of being started

71: No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept

80: The file exists

82: The directory or file cannot be created

86: The specified network password is not correct

88: A write fault occurred on the network

89: The system cannot start another process at this time Import API : System Error Codes

##### Queue Processor Application Error Messages Startup

| **Message**                                                     | **Explanation**                                                                                                                                                                                    | **Action**                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0^Accusoft Control creation error : &lt;  *error message*  &gt; | The Import API uses the AccuSoft Image Gear Toolkit to create the watermarked image. If an error occurs during the creation of AccuSoft controls, the error message displays describing the error. | The AccuSoft controls are installed during MAG*3.0*121  installation. If this error message occurs, contact the VistA Imaging system manager.  You may need to reinstall MAG*3.0*121 to correct AccuSoft ImageGear problems.                                          |
| 0^Image is missing from input data.                             | The image to be watermarked is not in the Import Queue Data.                                                                                                                                       | Check the IMAGE file (#2005) to see if the data is corrupt.                                                                                                                                                                                                           |
| 0^Watermark failure :  &lt;  *error message*  &gt;              | The process of burning the “Rescinded” watermark onto the image file failed.                                                                                                                       | The AccuSoft ToolKit could not create the watermarked image.  Check if the rescinded bitmap exists in the image directory  **C:\Program Files\vista\Imaging\Bmp\ MagRescinded.bmp**  .  You may need to reinstall MAG*3.0*121 to correct AccuSoft ImageGear problems. |
| Create Process failed'+ProgramName                              | A system error occurred staring the process                                                                                                                                                        | Log a Remedy ticket                                                                                                                                                                                                                                                   |
| Increment  *queue\_name*  Ptr^Failed                            | The QUEUE POINTER  (#1) in the IMAGE BACKGROUND QUEUE  POINTER file (#2006.031) in VistA  could not be updated                                                                                     | On the main BP window, use the Edit &#124; Refresh Queue Counts to correct the current counts. Close the BP and restart the application.                                                                                                                              |

| **Message**                                                                                                                                                                                                               | **Explanation**                                                                           | **Action**                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Initialization Failure^Log Files at: C:\Program Files\Vista\Imaging\Backp rocLog\BackProc\BPError.log                                                                                                                     | Log file could not be created                                                             | Check permissions on the log folder                                                                                |
| RAID groups not properly configured  Use the Network Location Manager to reset your RAID groups                                                                                                                           | An active RAID Group has no online shares                                                 | Make sure online RAID Group has online shares                                                                      |
| Requeue Failure trying to Requeue:                                                                                                                                                                                        | An attempt to re-queue a failed queue entry failed                                        | Use the Queue Manager and step past the queue entry. Determine the problem with the entry that would not re-queue. |
| SetTime Handle – Destin: C:\Program Files\Vista\Imaging\Backp rocLog\BackProc\BPError  .log Access is Denied                                                                                                              | Could not write the Access Date on the log file                                           | Check the file permissions on the log folder listed.                                                               |
| The Background Processor client software is version  *n.n.n.n*  . VistA Imaging Host system has version  *m*  installed. Please update to compatible client and host software.  Shutting down the Background Processor... | The client software that is installed does not match the KIDS version installed on VistA. | Install the correction version of the KIDS and client software.                                                    |
| The Patch 39 KIDS install on the VistA host system is required for this Version of the:  *site name*  BP Queue Processor                                                                                                  | The KIDS file for this most recent patch has not been installed in VistA.                 | Install the KIDS file on VistA.                                                                                    |
| The Site parameter context could not be determined. The application will terminate.                                                                                                                                       | The PLACE global is corrupt                                                               | Log a Remedy ticket                                                                                                |

| **Message**                                                     | **Explanation**                                    | **Action**                                                 |
|-----------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------|
| This server is not yet configured for BP queue task processing! | There is no BP Server name assigned to this server | Create a BP Server through the GUI and assign tasks to it. |

###### Runtime

| **Message**                                                                                      | **Explanation**                                                                                    | **Action**                                                                                                   |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| An Abstract for this file is on the Jukebox, a JBTOHD is being queued                            | ABSTRACT - The abstract pointer on the RAID is empty. The abstract will be copied from the jukebox | None                                                                                                         |
| Could not complete                                                                               | DELETE - file could not be deleted                                                                 | Check permissions on RAID share                                                                              |
| Could not complete/Requeued                                                                      | DELETE - file could not be deleted                                                                 | Check permissions on RAID share                                                                              |
| Current RAID Shares^Exception: No RAID group Assigned                                            | The RAID share must be assigned to a RAID Group                                                    | On the BP main window, use Edit &#124; Network Location Manager to assign the RAID share(s) to a RAID Group. |
| False Positive Copy f  *ilename(Source)*  ,  *filenames source filesize*  ,  *filesize(jukebox)* | File sizes on source and destination don’t match. File not copied.                                 | Determine if images are for different patients                                                               |
| File copied was of size zero                                                                     | IMPORT - The file size is zero                                                                     | Resend image from import source                                                                              |
| File of size zero created then deleted                                                           | MAKEABS - file of zero length was created by Mag_MakeAbs.exe. It was deleted.                      | Log a Remedy ticket                                                                                          |
| File was not found                                                                               | IMPORT - file does not exist on the image share                                                    | Resend image from import source                                                                              |
| *filename*  Source file does not exist.                                                          | Could not find source file                                                                         | Run Verifier to correct VistA pointers                                                                       |

| **Message**                                                      | **Explanation**                                                                                   | **Action**                                                              |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| *fileshare*  : Cannot connect to the Export Share.               | EXPORT - Cannot map to the remote share                                                           | Check for network connectivity.  Check permissions..                    |
| ForceDirectories failed:                                         | DELETE - could not create directory on jukebox share                                              | Check permissions on jukebox share                                      |
| Image File type:  *filename.ext*  is an Unsupported Format       | ABSTRACT - The Full file is not a supported Imaging file type. So the abstract cannot be created. | Examine the "foreign" file and determine if the extension was misnamed. |
| Jukebox is not available:  *filepath Volume label*               | JUKEBOX - the jukebox share is not available                                                      | Ping the jukebox server. Check the jukebox share permissions.           |
| Jukebox sourcefile unavailable                                   | JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is not set.      | None                                                                    |
| JUKEBOX:  *queue*  *\_pointer*  ^f  *ile\_extension*  Not copied | JUKEBOX - Alternate file extension (i.e. .TXT) was not copied                                     | Check file permissions                                                  |
| Login Message^Pausing 3 minutes and will then retry              | AUTOLOGIN - could not relog into the Broker                                                       | Check for network connectivity.                                         |
| Login Message^Silent Login attempt failed!                       | AUTOLOGIN - could not relog into the Broker                                                       | Check for network connectivity.                                         |
| Make AbstractError / abs is already present                      | ABSTRACT- file already exists at the RAID location specified in VistA                             | None                                                                    |
| Make AbstractError / f  *ilename*                                | MAKEABS- the  Mag\_MakeAbs.exe could not create the abstract file                                 | Log a Remedy ticket                                                     |
| NetConError Using User credentials  *WIN32\_Error*               | GCC - Could not logon to the remote location with the Username/Password in VistA                  | Correct the Username/Password for the GCC location in VistA             |

| **Message**                                                                             | **Explanation**                                                                                                                                                 | **Action**                                          |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| NetConError,'There is no password associated with this Network Location:  *share\_name* | GCC - The password field is empty for this Network Location                                                                                                     | Enter a password for this GCC location              |
| No Image file entry was created!                                                        | IMPORT - an IEN was not created in the image file                                                                                                               | Resend image from import source                     |
| No Jukebox sourcefile available / Attempting Abstract Queue                             | JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is set. The Queue Processor will attempt to make on from the Full or BIG file. | None                                                |
| No Tracking ID IMPORT failed                                                            | IMPORT - unique Tracking ID parameter is missing from IMPORT                                                                                                    | Resend image from import source                     |
| No valid RAID share found                                                               | IMPORT - no RAID  pointer is set in VistA for the image                                                                                                         | Resend image from import source                     |
| Problem renaming log file:  *filename*                                                  | Could not rename log file to a versioned copy                                                                                                                   | Check permissions on the existing folder/files      |
| *queue\_pointer*  '^Size Mismatch  *queue\_type*  copy not overwritten.                 | File sizes on source and destination don’t match. File not copied.                                                                                              | Determine if images are for different patients      |
| SetFileTime Failed                                                                      | Could not set Access date on the log file.                                                                                                                      | None                                                |
| The jukebox copy:  *filename*  does not exist -- attempting a copy...                   | DELETE -Could not find the file on jukebox shares. Try to copy from RAID shares to jukebox                                                                      | None                                                |
| The RAID share is not on- line                                                          | IMPORT - The Image share is not available                                                                                                                       | Check the permissions on the image share indicated  |
| The  *src\_filename*  to  *dest\_filename*  copy failed.                                | EXPORT - file could not be copied                                                                                                                               | Check for network connectivity.  Check permissions. |

| **Message**                                                     | **Explanation**                                            | **Action**                                                                                                           |
|-----------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| The VistA cache file:  *filename*  not found                    | DELETE -Could not find the file on RAID shares to delete   | None                                                                                                                 |
| This Server is not yet configured!                              | A BP Server has not been associated with this server.      | Create a BP Server for this processor                                                                                |
| Unable to copy to the Jukebox: Not enough write cache available | JUKEBOX - The jukebox share is not available or is full    | Add new platters to the jukebox. Determine why the jukebox share is full.  Possibly add new platters to the jukebox. |
| Zero size  *queue\_type*  copy NOT overwritten                  | Zero size file on the destination could not be overwritten | Remove zero size file                                                                                                |

##### Verifier Application Error Messages Start/Run

| **Message**                                                 | **Explanation**                                                                          | **Action**                                                                                                    |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| About to exit without processing: 0                         | There are no IEN records within the range.                                               | Choose another IEN range                                                                                      |
<!-- rpc-table -->
| Broker Connection to server could not be established!       | VistA RPC Broker is not currently in a listening state OR the application has timed out. | Close the application and restart. Check with the VistA system manager for the status of the Broker listener. |
| CC:createcontext ("MAG WINDOWS")  could not be established! | The user does not have the MAG WINDOWS menu  option assigned.                            | Assign the user this menu option.                                                                             |
| lbCacheShare.items.Count  &lt; 1: MAGQ SHARES               | There are no online, non- router VMC shares.                                             | Use the Queue Processor’s Network Location Manager to check/add the shares.                                   |
| Invalid Input Range                                         | The From and To values entered in the Range are not correct (e.g. Start: 0 End: 0).      | Enter a valid  *From*  and  *To*  range.                                                                      |
| jukebox shares are not setup                                | The jukebox share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).  | Create/Edit the jukebox shares in the Network Location Manager on the Queue Processor.                        |

| **Message**                                                                                                                                                          | **Explanation**                                                                                           | **Action**                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| This workstation is not currently setup as a Background Processor.                                                                                                   | There is no BP Server set up for this machine.                                                            | Use the option  *BP Servers*  on the Queue Processor to register this server.  |
| Verifier client software is version nnn. VistA Imaging Host software is version mmm. Please update to compatible client and host software. Shutting down Verifier... | The version of the KIDS file installed on VistA does not match the executable version on the workstation. | Install the latest KIDS and client software.                                   |
| VistA shares are not setup                                                                                                                                           | The image share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).                     | Create/Edit the shares in the Network Location Manager on the Queue Processor. |

###### Output HTML Messages

| **Message**                            | **Explanation**                                                                                    | **Action**                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Aggregate JB Copy Error:               | Could not copy from alternate jukebox to current jukebox                                           | Check permissions                                                                         |
| Abs to JB:                             | Abstract has been created and copied to the jukebox                                                | None                                                                                      |
| Aggregate Function - Enabled           | Software is enabled to copy files from secondary jukebox, if necessary                             | None                                                                                      |
| BIG Aggregate Failed                   | Could not copy BIG file from secondary jukebox                                                     | Check file existence/permissions                                                          |
| Create Process failed                  | Could not create process on VistA for Verifier                                                     | Check Error Trap                                                                          |
| Empty FBIG node                        | "FBIG" node has no pointers set in 2005 record.                                                    | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes. |
| File of size zero created then deleted | Abstract file created of size zero. Then it is deleted. (Likely corruption of BIG and/or TGA file) | None                                                                                      |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary jukebox                                                    | Check file existence/permissions                                                          |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary jukebox                                                    | Check file existence/permissions                                                          |

| **Message**                           | **Explanation**                                                                                  | **Action**                                                                                        |
|---------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Images JB share is OFF- LINE:         | jukebox is offline                                                                               | Set jukebox back ONLINE                                                                           |
| Make AbstractError                    | Abstract file could not be created from TGA/BIG (BIG/TGA not found or image file corruption).    | Check shares for existence of BIG/TGA file. If not found, restore BIG/TGA file from backup tapes. |
| New Abs to CWL                        | An abstract file has been created and copied to the current write image share                    | None                                                                                              |
| No ABS file VC Ptr Cleared            | Abstract file not found on the Image share                                                       | None                                                                                              |
| No ABS file VC Share OFF-Line         | Image share is offline at location of abstract file                                              | Set share back online and re- run Verifier                                                        |
| No ABS JB Files                       | No abstract file found on the jukebox                                                            | Check shares for existence of ABS file. If not found, restore ABS file from backup tapes          |
| No Acquisition Site in Image file     | The ACQUISITION SITE  field #100 in the IMAGE file (#2005) is missing. This is a required field. | Contact IRM  Update the field with the proper site ID.                                            |
| No FULL JB Files                      | FULL file not found on the jukebox                                                               | Check shares for existence of Full file. If not found, restore Full file from backup tapes        |
| No FULL VC Files                      | FULL file not found on the Image share                                                           | None                                                                                              |
| No jukebox BIG Files                  | BIG file not found on the jukebox                                                                | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.         |
| No jukebox FULL Files                 | FULL file not found on the jukebox                                                               | Check shares for existence of Full file. If not found, restore Full file from backup tapes.       |
| No Network References                 | No IMAGE file (#2005)  record exists for this image                                              | Re-import image thru the Capture client                                                           |
| No Network References: Archived Image | Image has been archived, resides in the IMAGE AUDIT file (#2005.1)                               | None                                                                                              |
| No VC BIG Files                       | Could not find the BIG file on the image share                                                   | None                                                                                              |
| Not Certed                            | Could not find/create file type on jukebox                                                       | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.         |

| **Message**                       | **Explanation**                          | **Action**                                                                |
|-----------------------------------|------------------------------------------|---------------------------------------------------------------------------|
| Problem rename log file:          | Permission problem with log file         | Set WRITE permissions set on share/folder/file for Windows login account. |
| Text file Patient ID not in VistA | Could not locate patient ID in VistA     | Contact IRM                                                               |
| TXT to BIG VC                     | Copy TXT file to same share as BIG file  | None                                                                      |
| TXT to FULL VC                    | Copy TXT file to same share as FULL file | None                                                                      |

**"Check Text" Option Messages**

| **Message**                        | **Explanation**                                                          | **Action**                                   |
|------------------------------------|--------------------------------------------------------------------------|----------------------------------------------|
| Text File Corruption Error Type 1: | Text file is binary or unreadable                                        | Restore file from jukebox/backup tapes       |
| Cannot determine Text file type:   | Foreign text file was not likely generated on the image gateway          | Restore file from jukebox/backup tapes       |
| Text File Corruption Error Type 2: | Text file is ASCII but has unprintable characters or truncated           | Restore file from jukebox/backup tapes       |
| Text/Image DFN Mismatch:           | Patient ID in text file does not match that in VistA                     | Future utility patch                         |
| Text/Image SOP/UID Mismatch        | The Series Instance UID in the text file does not match the one in VistA | Future utility patch                         |
| Text/Image Study/UID Mismatch      | The Study Instance UID in the text file does not match the one in VistA  | Future utility patch                         |
| Text/Image UID Mismatch            | SOP and/or Study UID are/is blank in text file                           | Future utility patch                         |
| Updated Text file                  | Text file has been edited                                                | Validate file has been copied to the jukebox |
| No SSN Found                       | Patient ID field missing in text file                                    | Future utility patch                         |

###### Integrity Messages on Patient Data

There are integrity issues that will prevent their respective images from being displayed and others that will not impact the viewing. See Appendix C in the *Background Processor User Manual* for sample output.

###### Conditions Preventing Viewing

An integrity error message will be generated when the image is retrieved for viewing on these conditions and the patient image will not be viewable until the condition is corrected or the user has the proper key to view these images.

| **Message**                          | **Explanation**                                                                                                                                                                                                                    | **Action**           |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| No Image Ptr in AP                   | The Clinical Association Report (AP for this image does not contain an image entry that points back to this image.                                                                                                                 | Future utility patch |
| GP has no images                     | Image series that does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition.                                                           | Future utility patch |
| Conflicting AP & Image DFNs          | The patient file reference (DFN) in the Clinical Association Report (AP does not match the DFN in the IMAGE file (#2005).                                                                                                          | Future utility patch |
| Invalid Image Ptr to AP              | The Clinical Association Report (AP) has image references that are not in the IMAGE file (#2005).                                                                                                                                  | Future utility patch |
| Conflicting GP and GO DFN            | The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.                                                                                                                           | Future utility patch |
| GP & GO AP Mismatch                  | The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.                                                                                                                           | Future utility patch |
| GP Missing GO Ptr                    | The Group Object multiple of the referenced Group Parent does not reference this group object.                                                                                                                                     | Future utility patch |
| **Message**                          | **Explanation**                                                                                                                                                                                                                    | **Action**           |
| No AP Mult Ptr                       | This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005).record is missing the  *PARENT DATA FILE IMAGE POINTER*  (#17)  for a Clinical Association Report (AP). | Future utility patch |
| GO DFN mismatches                    | Some image file Group Objects have different PATIENT references (DFN).                                                                                                                                                             | Future utility patch |
| Image entry is structurally abnormal | The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non- Group image (NG) is corrupt.                                                                                                  | Future utility patch |
| Missing Group Objects                | The Group Parent has Group Object references that are missing.                                                                                                                                                                     | Future utility patch |
| DFN Mismatches in AP Image Mult      | The Clinical Association Report (AP) references a Group Parent that has image files with a different PATIENT reference (DFN) than the report.                                                                                      | Future utility patch |

###### Conditions Allowing Viewing

The following integrity issues will **not** prevent their respective images from being displayed. These are informational messages.

| **Message**     | **Explanation**                                                                                                                                                                                        | **Action**           |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| No AP Ptr       | The IMAGE file (#2005) record is missing the PARENT DATA FILE#  (#16) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified.           | Future utility patch |
| No AP entry Ptr | This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the  *PARENT GLOBAL ROOT*  *DO (#17)*  for a Clinical Association Report (AP). | Future utility patch |

##### Purge Application Error Messages

| **Message**                                                                       | **Explanation**                                                                                                                      | **Action**                                                          |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Broker Reconnection failed                                                        | Auto login after a Broker disconnect failed                                                                                          | Check network. Contact IRM                                          |
| Create Process failed  *ProgramName*  ,                                           | Windows failed to create a process.                                                                                                  | Reboot the server.                                                  |
| Express Purge Rate limit reached:  *PurgeRate*  on share:  *CurrentShare*         | The purge terminated on the given share because Express Purge was active and the Purge process exceeded the user defined purge rate. | None                                                                |
| File Delete failure:  *filename*                                                  | The file listed could not be deleted.                                                                                                | Check permissions on the share/folder/file                          |
| File in use:  *filename*                                                          | The log file is in use                                                                                                               | Exit from the Purge and restart                                     |
| **Message**                                                                       | **Explanation**                                                                                                                      | **Action**                                                          |
| File purged:  *filename*  . 'The Image file (#2005) was not updated'              | The file was deleted on the RAID, but the pointer in VistA could not be updated.                                                     | Validate the IEN record exists in VistA.                            |
| Findfirst failed  *filename*                                                      | The directory traversal failed                                                                                                       | Exit from the Purge and restart                                     |
| Log File Archival reset to:  *FilePath2*  instead of:  *FilePath1*                | The logs files are now being stored at another location.                                                                             | None                                                                |
| Login Message^Broker Reconnection Successful                                      | After a Broker disconnect, the application was able to reconnect to VistA.                                                           | None                                                                |
| Login Message^Pausing 3 minutes and will then retry                               | After a Broker disconnect, the application tries 3 times to reconnect to VistA                                                       | None                                                                |
| Login Message^Silent Login attempt failed!                                        | After a Broker disconnect, the application was not able to reconnect to VistA.                                                       | Check network connections.                                          |
| NewCreationDate^SetFile Time Failed  *filename*                                   | Could not set the date of last Accesses on filename                                                                                  | None                                                                |
| Non-Connection related Broker error                                               | Broker disconnected                                                                                                                  | Check VistA for error trap                                          |
| NOT Purged criteria:  *EvalCriteria*  NOT PURGED-JUKEBOX  QUEUED  *filename date* | File was not deleted. See Section 6.4 Purge Criteria.                                                                                | None                                                                |
| Problem renaming log file  *filename1*  -&gt;  *filename2*                        | Could not rename log file to versioned log file name                                                                                 | Check permissions.                                                  |
| Purge Criteria:  *EvalCriteria filename filedate*                                 | See Section 6.4 Purge Criteria                                                                                                       | None                                                                |
| Purge Criteria:  *EvalCriteria*  NOT PURGED  *filename filedate*                  | File was deleted. See Section 6.4 Purge Criteria                                                                                     | None                                                                |
| Silent Login attempt                                                              | Broker was disconnected. Auto login is initiated.                                                                                    | None                                                                |
| Start Date failure                                                                | Problem with Date of Last Purge on Scheduled Purge                                                                                   | Contact IRM to clear the record in the Imaging Site Parameter file. |

#### DICOM Gateway Error Messages

Information about DICOM Gateway Error messages is available in the *VistA Imaging Error Message Guide.*

#### Clinical Display/Capture Setup Error Messages

The following errors are possible during the MAGINSTALL.EXE file execution. When the MAGINSTALL file is transported via FTP, it should be in binary format (or possible file corruption may occur).

| **Error Message**                                                                                                                      | **Notes**                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Incorrect Windows version.                                                                                                             | Review the installation manual regarding the application’s Windows compatibility. |
| Invalid executable file.                                                                                                               | Possible corrupted MAGINSTALL.EXE file.                                           |
| Type of executable file was unknown.                                                                                                   | Possible corrupted MAGINSTALL.EXE file.                                           |
| Attempt was made to load a second instance of an executable file containing multiple data segments that were not marked for read-only. | Possible corrupted MAGINSTALL.EXE file.                                           |
| Dynamic Link Library (DLL) file was invalid.                                                                                           | One of the DLLs required to run this application was corrupt.                     |
| [2] Imaging Display                                                                                                                    | The Imaging Display application is open. Close the application and click retry.   |
| [1] Imaging Capture                                                                                                                    | The Imaging Capture application is open. Close the application and click retry.   |

#### VistARad Error Messages

Error messages associated with the VistARad application are listed below. Messages are listed alphabetically. This list is not exhaustive. It omits some messages which are informational, supply their own remediation instruction, or are otherwise self-evident. If a message not on this list appears and requires further explanation, please contact the National Help Desk.

| **Error Message**                                                                  | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case #nnn is already locked by you, perhaps at another workstation.                | A user has attempted to lock an exam that is already locked in their name. This could occur from two different logons from different workstations; or, it could result from a failed connection that left a process hanging without a connected client.                                                   |
| Case %s: all images failed to load.                                                | No images for the selected case could be found. If any valid headers are located, one or more “dummy” thumbnails may be displayed in the Preview window, but no actual images are available.  Close the exam, then attempt to re-open it. If the problem persists, contact the local Imaging Coordinator. |
| Case #nnn is Locked by [Name/Unknown]; Status Update will NOT be allowed.          | Between the time that the exam was opened and locked, and the time the exam was closed for update, the Exam lock information had changed, making the exam not updateable. If this occurs, check for problems in the lock table or with the Broker connection.                                             |
| Case #nnn locked by [name], not locked by [user]--No Status update performed       | Between the time that the exam was opened and locked, and the time the exam was closed for update, the lock information either was killed, or over-written with another user’s information.                                                                                                               |
| Case #nnn was previously locked by [Radiologist]. The lock is now assigned to you. | The radiologist that previously had the lock likely had the M session abnormally terminated.                                                                                                                                                                                                              |
| Case %s: no valid headers found.                                                   | Images in the exam do not have valid headers and cannot be processed properly. The exam load is considered successful.  You can display images by loading the “IMG\_INVALID\_TEXT” stack in the Preview window into the Viewer; the exam can be locked for interpretation.                                |

| **Error Message**                                                                                                      | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case %s: some image(s) are missing.                                                                                    | Some images and/or headers could not be found. The exam load is considered incomplete.  Depending on what is missing, one or more placeholders will be used in the Preview and Viewer windows. The exam cannot be locked or interpreted.  Close the exam, then attempt to re-open it. If the problem persists, contact the local Imaging Coordinator. |
| Case %s: some image(s) have invalid or missing headers.                                                                | The headers for some images in the case could not be found. Images that can be processed properly will be displayed normally; images that could not be processed due to missing header data will be loaded into the Preview window only with an “IMG\_INVALID\_TEXT” label.  The exam can be locked and interpreted.                                  |
| Case with number xxx will not be loaded, Error 0x %x.                                                                  | A VistARad internal error occurred while opening the exam.                                                                                                                                                                                                                                                                                            |
| Could not send files to MIRC Server at  &lt;Host Name&gt; and Port &lt;Port Number&gt; with AE Title &lt;AE Title&gt;. | Ensure that the MIRC server configuration information is correct, that the MIRC server is online, and that it can receive messages.                                                                                                                                                                                                                   |
| Current Case Not Accessible for Updating                                                                               | A user request to close an exam cannot be processed because the data does not have valid information that correctly identifies a Radiology study. Check the exam data stored in the Radiology database.                                                                                                                                               |
| Current Case not accessible to close--no action taken                                                                  | A user request to close an exam cannot be processed because the data does not have valid information for the Radiology study. Check the exam data stored in the Radiology database.                                                                                                                                                                   |
| Don't know how to read this image element.                                                                             | An unexpected value was found in the last DICOM tag listed in the Viewport Info tab of the Hanging Protocol Definition dialog. The hanging protocol definition cannot be saved. Verify that the image header is populated properly for the DICOM tag in question.                                                                                     |

| **Error Message**                                                          | **Cause(s)/Solutions**                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Error getting shared CPT-HP association info.                              | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                            |
| Error Initializing HP module.                                              | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                            |
| Error occurred while performing search.                                    | The VistARad client was not able to contact the VistARad host. Check for status details at the bottom of the manager window.                                                                                                                                     |
| Error Reading File MAGJ.ini                                                | MAGJ.ini not present in expected location (C:\Program Files\Vista\Imaging\MAG_ VistARad). The software will start, but users will not be able to display local copies of routed exams or use integrated voice dictation functions until the problem is resolved. |
| Error reading settings. VistARad will exit.                                | The client was unable to retrieve monitor information from the VistARad back end on the VistA Host. Verify that the VistA Host is accessible and running.                                                                                                        |
| Error retrieving monitor information (Error:%d). VistARad will exit.       | The VistARad client could not retrieve monitor information stored on the VistARad back end. System queried back end for monitor information but gets no response. Verify that a connection is present and that the VistA system is up and running.               |
| Exam is for Station (nnn); you are logged on to #mmm". Exam is NOT Locked. | The exam being opened is exam registered at a consolidated site that is a not the user’s logon site (division). The exam can be displayed but its status cannot be updated.                                                                                      |
| Exam Manager failed to Initialize. VistARad will exit.                     | The client was unable contact VistARad back end on the VistA Host. Verify that the VistA Host is accessible and running, and that the correct KIDS version is installed.                                                                                         |

| **Error Message**                                                                      | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exam Status for Case #nnn CANNOT be updated; current status remains: [Status]          | The status update cannot proceed because there is insufficient information in the radiology record to allow the status to advance.  If this occurs frequently, then the site has not properly performed VistARad system setup regarding Radiology Exam Status codes definition—refer to Chapter 3 in the  *VistA Imaging Installation Guide*  . |
| Failed to get HP info from the backend for default system user. Error code 0x80004005. | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                                                                                                           |
| Failed to import user profile. Click OK to exit VistARad.                              | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                                                                                                           |
| Failed to read in xxx preset definition of the current or system user correctly.       | There was a problem processing the specified image preset definition. Do not use the specified image preset until the problem is resolved.                                                                                                                                                                                                      |
| Failed to read in xxx template definition of the current or system user correctly.     | There was a problem processing the specified template definition. Do not use the specified template until the problem is resolved.                                                                                                                                                                                                              |
| Failed to retrieve a preset xxx for user xxx                                           | There was a problem retrieving preset information from the VistARad back end. Verify that a connection is present and that the VistA system is up and running.                                                                                                                                                                                  |
| For Case #nnn, current Status is [status]; Stats Update will NOT be allowed            | Between the time the exam list indicated an exam was lockable and the time the exam was opened, the exam status had changed, making the exam not lockable. If this happens frequently, exam list compile intervals specified in the MAG VISTARAD SITE PARAMETERS file  (#2006.69) may need to be adjusted.                                      |
<!-- rpc-table -->
| For MAGJ STUDYDATA  (TX="\_TXID\_") invalid params passed to rpc call.                 | Invalid request for key image and/or presentation state data was received on the VistA host; could indicate a database problem with the exam or images in the exam being looked at.                                                                                                                                                             |

| **Error Message**                                                                                            | **Cause(s)/Solutions**                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HP creation failed, error code xxxx                                                                          | An application error prevented creation of the hanging protocol; record the error code and contact Customer Support.                                                                                                                                                              |
| HP named xxx could not be read in correctly.                                                                 | There was a problem processing the specified hanging protocol definition. Do not use the specified hanging protocol until the problem is resolved.                                                                                                                                |
| Insufficient memory; cannot load all text files, thumbnails and/or key images. Load aborted for case(s) XXX. | Exit and restart VistARad to clear any potential memory issues. Attempt to reload the exam in question. Contact your Imaging Coordinator if the error persists.                                                                                                                   |
| Invalid Request (ListType=xxx)                                                                               | An attempt to compile an exam list failed. The exam list definition in MAG RAD LISTS DEFINITION file (#2006.631) may be corrupted. The exam list definition should be fixed or disabled.                                                                                          |
<!-- rpc-table -->
| Invalid transaction (TX="_TXID_") requested by MAGJ STUDYDATA RPC call.                                      | Invalid request for key image and/or presentation state data was received on the VistA host; could indicate a database problem with the exam or images in the exam being looked at.                                                                                               |
| Modality type xxx not found in the configuration file.                                                       | hpconfig.xml does not contain information for the modality associated with the active exam. Verify that modality for the exam in question is being correctly identified and that hpconfig.xml file stored in the VistARad application folder is present and not corrupt.          |
| Modality xxx not found. Please contact your system administrator"                                            | The hpconfig.xml file does not contain information for the modality associated with the active exam. Verify that modality for the exam in question is being correctly identified and that hpconfig.xml file stored in the VistARad application folder is present and not corrupt. |
| No data supplied for History List update/delete.                                                             | The client software performed an invalid request to update the History list.                                                                                                                                                                                                      |
| No modality in this stack of images                                                                          | The exam being opened does not contain modality information.                                                                                                                                                                                                                      |

| **Error Message**                                                                                                                                                                               | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No Update Allowed for Case #nnn-- current status is [Status]                                                                                                                                    | Between the time that the exam was opened and locked, and the time the exam was closed for update, the Exam Status information had changed, making the exam not updateable. This can occur if a data entry operation was performed in Radiology package while the exam was being read. |
| Image loading has been paused: not enough memory to load all images at once.  Use the Preview window's List view mode to load and/or purge selected image sets.                                 | Using the Preview window in List View mode, click “Purge” on one or more (partially) loaded series to free their memory. Then click “Resume” on the series of interest that was paused.                                                                                                |
| Request Contains Invalid Case Pointer (nnn^nnn^nnn^nnn).                                                                                                                                        | A user request to open an exam cannot be processed because the data does not have valid information that correctly identifies a Radiology study. Check the exam data stored in the Radiology database.                                                                                 |
| Resource limit exceeded! Close some images                                                                                                                                                      | The maximum number of DIMPLX controls allowed by the operating system has been exceeded. Use the layout controls in VistARad to reduce the number of visible viewports.                                                                                                                |
| Startup problem: cannot launch background case loader.  Startup problem: cannot launch background cleaner.  Startup problem: cannot create image load/display objects.                          | Exit and restart VistARad; contact customer support if this error persists.                                                                                                                                                                                                            |
| The current History List may not be updated by the current user.                                                                                                                                | The client software performed an invalid request to update the History list.                                                                                                                                                                                                           |
| The Exam file for this exam has patient [Pat1]; the corresponding Report file has patient [Pat2]. This is a serious problem, immediately report it to Radiology management and Imaging support! | The exam failed a “Patient Safety” check.                                                                                                                                                                                                                                              |

| **Error Message**                                                                                                                                                                                                                | **Cause(s)/Solutions**                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This exam has no report entry for associating images; no images can be accessed.                                                                                                                                                 | There is no Radiology Report link for the images in the exam being opened. Could be normal; or, a database problem (e.g., induced by deleting a Report without first correcting images). |
| This exam has problems in the Radiology files, with two different Case Numbers referenced Ref1 and Ref2.  This is a potentially serious problem— immediately report it to Radiology management and Imaging support staff!        | The exam failed a “Patient Safety” check.                                                                                                                                                |
| This exam has problems in the Radiology Report file, with two different report entries referenced Ref1 and Ref2. This is a potentially serious problem--immediately report it to Radiology management and Imaging support staff! | The exam failed a “Patient Safety” check.                                                                                                                                                |
| This exam is linked to Report entry #nnn, but some of its images may be linked to Report entry #mmm. This is a potentially serious problem-- immediately report it to Radiology management and Imaging support staff!            | The exam failed a “Patient Safety” check.                                                                                                                                                |
| This exam is registered for [Pat1]; however, it is linked to images for patient [Pat2]. This is a serious problem, immediately report it to Radiology management and Imaging support staff!                                      | The exam failed a “Patient Safety” check.                                                                                                                                                |
| The resolution of the display is not suitable for displaying diagnostic quality images. VistARad will exit.                                                                                                                      | This message appears if monitor resolution width is less than 1024, or if monitor resolution height is less than 700, or if monitor bit depth is less than 8.                            |
| Unable to access HISTORY File for deleting records; try again later.                                                                                                                                                             | A delete or other update operation cannot be performed because the current M process cannot lock the file for the user.                                                                  |

| **Error Message**                                                                                                     | **Cause(s)/Solutions**                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unable to connect to specified host/port  or  Unable to obtain VIX connection information for the specified Site code | VistARad cannot establish a connection to the specified remote VIX server. Verify correct data entry. If necessary, consult your local ADPAC to confirm that the specified VIX server is on-line and the Site Service is configured properly.                                                                                                             |
<!-- rpc-table -->
| Unable to get/update user data (USER_name) for MAGJ USER DATA RPC call.                                               | The system could not retrieve data from the MAGJ USER DATA file (#2006.68).                                                                                                                                                                                                                                                                               |
| Unable to open device 'IMAGING WORKSTATION'                                                                           | Attempt to display a VistARad report fails because the host system cannot open the device for host file output.  Fix the device file entry.                                                                                                                                                                                                               |
| Unable to retrieve images for Case #nnn                                                                               | Probably a database problem; the system expected to find images, but did not find any.                                                                                                                                                                                                                                                                    |
| Unable to update Interpreting Radiologist:[Explanation provided ]                                                     | The Status Update cannot proceed because the user fails Radiology package user security checks.                                                                                                                                                                                                                                                           |
| Update failed                                                                                                         | There was a problem saving preset information to the VistARad back end. Verify that a connection is present and that the VistA system is up and running.                                                                                                                                                                                                  |
| Updates not allowed at this site--no action taken                                                                     | After the exam was closed and locked, the back end “Enable Status Update” setting has been disabled.                                                                                                                                                                                                                                                      |
| VistARad cannot run in a terminal services client environment. VistARad will exit.                                    | VistARad cannot be launched using a remote desktop connection or terminal services client.                                                                                                                                                                                                                                                                |
| VistARad is already running. Exiting application.                                                                     | Another instance of VistARad is running on the workstation. If that instance cannot be accessed from the Windows Taskbar, you may need to kill the process named “VistARad Viewer” using the Windows Task Manager; you may need to end the MAG\_Vistarad.exe process from within the Processes tab of the Windows Task Manager.  Then re-launch VistARad. |

This page intentionally left blank.

### Appendix B: Means Tests

#### Sending Means Tests to the HEC

The following is the current list of ‘Image Types’ that need to be sent to the HEC (Health Eligibility Center):

- MEANS TEST (10-10EZ)
- MEANS TEST (10-10EZR)*
- MEANS TEST (10-10F)

* The (HEC) has requested that a third type of Means Test (EZR) be copied to them. Sites need to add the MEANS TEST (10-10EZR) Image Index Type to the IMAGE ACTIONS file (#2005.86) to allow the transfer of this type of Means Test.

- A qualified person at the site needs to use FileMan to edit the IMAGE ACTIONS file (#2005.86); select the TYPE field (#5); and choose HEC COPY at the Image Action name field prompt.
- You can also log a Remedy ticket and have VistA Support guide you through this process.

An example of adding a new Index Type to be sent to HEC is shown below. User entries are shown in **bold** .

<!-- image -->

<!-- image -->

Appendix B – Means Tests

**Note:** Sites would only want to add/expand on what gets sent to the Health Eligibility Center (HEC) upon a direct request from the Health Eligibility Center (HEC) to do so. This is usually a rare occurrence, and all sites will be notified if this occurs.

This page intentionally left blank.

### Glossary

AE\_Title	The unique name assigned to a DICOM application to identify the application to other DICOM applications on the network. AE\_Title will be used to log machine-to-machine communication within this patch.

CD	Compact Disc

cPACS	Commercial PACS

DICOM Correct	The name assigned to the software routine used to correct DICOM Objects that fail processing on the DICOM Gateway.

DICOM Gateway	Interface between VistA and external DICOM application entities.

See *VistA Imaging DICOM Gateway* .

DICOM Importer II	Refers to the software that performs the automated DICOM import process from outside facilities.

DICOMDIR	A file that is a unique and mandatory DICOM Directory file that

contains the Media Storage Directory SOP Class as described in DICOM PS 3.10 2008.

DoD	Department of Defense

DUZ	The internal entry number of a VistA user’s entry in the NEW PERSON file (#200).

DVD	Digital Versatile Disc

GUI	Graphical User Interface

HDIG	Hybrid DICOM Image Gateway: An image gateway that combines the legacy DICOM Gateway and the new VISA Gateway. It implements DICOM services.

HIPAA	Health Insurance Portability and Accountability Act

IA	Integration Agreement

IHE	Integrating the Healthcare Enterprise

IHS	Indian Health Services

KIDS	Kernel Installation and Distribution System

PACS	Picture Archiving and Communications System

Partial Study	A study where only a subset of the available images have been

staged or imported.

PHI	Protected health information: Individually identifiable health information transmitted by electronic media, maintained in electronic media, or transmitted or maintained in any other form or medium.

RPC	Remote Procedure Call

SCP	Service Class Provider

SCU	Service Class User

SOP	Service Object Pair

SOP Class	Unique identifier assigned by the DICOM Standard to identify

DICOM objects.

Staging	Copying study data from either media or an authorized network location into temporary persistent storage for later reconciliation. There are two

types of staging (controlled by Security Keys):

Basic Staging: An authorized user copies all study data from an authorized source to Importer II Persistent Storage.

Advanced Staging: An authorized user can view source data by study and copy data by study to Importer II Persistent Storage.

Storage media	The physical device onto which data is recorded.

Supported SOP Class	A DICOM Object that can be processed by the DICOM Gateway

and delivered to other VistA Imaging applications for use within VistA Imaging.

TWAIN	An interface standard for scanners, cameras and other input devices.

A TWAIN driver is generally supplied by the equipment vendor.

UID	DICOM unique identifier

VA	US Department of Veterans Affairs

VISA	VistA Imaging Services Architecture

VISN	Veterans Integrated Service Network

VIX	VistA Imaging eXchange – Software platform for managing site service and other VISA services.

## Index

**%**

% Server Reserve, 123

### A

ad hoc reporting, 157

ADPAC staff requirements, 29 ADT protocols, 171

archiving, 97

Auto-Write function, 123

### B

Background Processor configuration guidelines, 104 files installed on, 50 overview, 5

BackProc.log file, 101, 102

backward compatibility, 169 biomedical staff requirements, 29

### C

CCOW, iv, v, 2, 144, 145, 146

Check text files, 122 Clinical Workstation

files installed on, 42

CONFIGURE IHE-BASED HL7 ADT

INTERFACE TO PACS menu option, 87 Context Management, iv, 2, 145, 146

CPRS, iv, 2, 144, 145, 146, 147, 155, 189

### D

DFNError log file, 103 DICOM error log, 131 DICOM Gateway, 125

and PACS, 169

HL7 messages and, 143 DICOM overview, 2

DICOM\_Echo, 28 document counts report, 157 drag, 11

**E**

error log DICOM, 131

MSM, 131

Error messages, 214

event viewer, 28, 30

exported options, 85

### F

failed images, processing, 130 file migration, 126

file security, 79

FileMan files, 63

### G

global journaling, 83

### H

hardware maintenance, 21

HEC, sending means tests to, 223 HL7 application parameters, 143 HL7 logical link, 143

HL7 MESSAGE TEXT file (#772), 181

HL7 messages, 143 HL7 protocols

Radiology v.2.1, 169

Radiology v.2.4, 170

### I

ICRs (integration control registrations), 144 Image Cache, 147

image count by user report, 158 IMAGE file (#2005)

deletion, 98

migration, 97

IMAGE file (#2005)

archiving or purging, 97 images

taking offline, 126

viewing remotely, 185

IMAGING HL7 MESSAGING MAINTENANCE, 85

Imaging package requirements, 13 Imaging Site parameters, 115 Imaging system

general maintenance, 29

overview, 1

RPC calls, 144

Import API, 134

input templates, 72

Integration Agreement, 144, 225

Integration Agreements, 144

Internal Relations, 169 IRM staff requirements, 28

### J

journaling, 83

jukebox backups, 125

### K

Kernel, 2, 13, 14, 41, 94, 137, 138, 185, 189

KIDS, 28, 36, 95, 126, 152, 155, 202, 203,

207, 217

### L

Log files

Background Processor, 100

BackProc.log, 101, 102

DFNError log, 103

NoArchive log, 102

Purge.html log, 103

PurgeError.html log, 103

Queue Processor, 101

Scan log, 102

ScanError log, 103 Verifier log files, 102

### M

MAG CLIENT VERSION REPORT menu

option, 92

MAG CPACS, 143

MAG HL7 MAINT menu option, 85 MAG REASON EDIT menu option, iv, 90 MAG SERVER mail group, 147, 148

MAG\_Decompressor, 60

MAGD MAINT RAD HL7 SUBS menu

option, 86

MAGREPSTART, 156

MailMan messages, 147 MAINTAIN SUBSCRIPTIONS TO

RADIOLOGY HL7 DRIVERS menu

option, 86 maintenance

general, 29

hardware, 21

security software, 25 means test report, 161 means tests, 223 Menus

Imaging System Manager, 85 VistARad System Options, 93

messages HL7, 143

Image Cache, 147

MailMan, 147

site usage, 148

Windows, 144

Microsoft patches, installing, 21 modalities, changes to, 21 mouse, 10

MSM error log, 131

### N

Network Location Manager, using, 113 network resources, 27

NoArchive log file, 102

### O

offline images, 126

online help, 179

### P

package index contains ‘note’ report, 162 package requirements, 13

package-wide variables, 177 patches, Microsoft, installing, 21 patient movement protocol, 174 PII, 2

ping, 28

power requirements, 28 processing failed images, 130

productivity reports, 157 protocols

patient movement, 174

radiology, 169, 173

Purge configuration, 108 Purge log files, 103 Purge.html log file, 103 PurgeError.html log file, 103 purging, 97, 98

image shares, 128

message files, 130

modality worklist, 130

PACS messages, 130

### Q

Queue Processor overview, 5

### R

Radiology HL7 v2.1 protocols, 169 Radiology HL7 v2.4 protocols, 170 radiology protocols

DICOM, 169

VistARad, 173

radiology report transcription service, 181 RAID Group Advance, 123

reboot, 9

remote access requirements, 28 Remote Image Views, 185 reports, imaging site, 157 routines

non-M, 41 RPC calls

VistA Imaging, 144

### S

Scan log file, 102 ScanError log file, 103 Scheduled Verifier, 121

security, 25

file, 79

security keys, 15

server manager, 28

site parameters for Imaging, 115 site usage messages, 148

space requirements, 27 staff requirements

ADPAC, 29

biomedical, 29

IRM, 28

system outages, 83

### T

TeleReader, 18, 22, 51, 118, 146, 154, 155,

185

TraceRT, 28

Two-Factor Authentication (2FA), 189

### U

user manage *r* , 28

### V

Verifier overview, 6

Verifier, using, 125

VistA Imaging ADT protocols, 171 VistA Site Service, 14, 166, 186

VIX, 7, 27, 61, 131, 166

### W

window controls, 10

Windows 7, iv, 2, 8, 41, 42, 49

Windows messaging, 144 Windows servers, changes to, 21 Workstations, 9