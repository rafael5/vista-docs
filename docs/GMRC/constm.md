---
app_name: 'CPRS: Consult/Request Tracking (GMRC)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2024-08
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMRC
patch: 206
patch_gap: null
section: ''
source_file: constm.docx
status: draft
title: '#'
---

# Consult/Request Tracking 3.0

# Technical Manual

<!-- image -->

November 2024

Department of Veterans Affairs (VA)


## Revision History

**NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date     | Patch                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Author                |
|----------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 11/2024  | GMRC*3.0*189                                                             | Sections updated to include changes for patch GMRC*3.0*189.  Updated Revision History, Table of Contents, New Features section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| 08/2024  | GMRC*3.0*206                                                             | Updated for 508 compliance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | CPRS Development Team |
| 11/2023  | GMRC*3.0*185                                                             | Document content transferred to latest OIT template.  Sections updated to include changes for patch GMRC*3.0*185.  Applied section numbering schema throughout for greater ease of reference.  Converted ‘computer screen’ content to figures to comply with accessibility requirements and greater ease of reference.  Updated Revision History, Table of Contents, index, section 5.35 Interfacility Consults When Used With Cerner-Converted Sites, and HL7 field descriptions.  Redrew Figure 8-1: Consult Request Tracking File Diagram in Visio for greater clarity and maintainability. |                       |
| 08/2023  | GMRC*3.0*199                                                             | Updated for GMRC*3.0*199.  Updated Figure 5-46: Running an IFC Possible Erroneous Comment Report.  Added bulleted SCR and CSV descriptive text to section 5.31.  Added section 5.31.1. Viewing the Possible Erroneous Comment Report in Excel.                                                                                                                                                                                                                                                                                                                                                 |                       |
| 03/2023  | GMRC*3.	0*193                                                                          | Updated for GMRC*3.	0*193  Added IFC Possible Erroneous Comments Report to menu options on Table 5-1, Table 5-4, Table 7-1 Figure 7-4, and Figure 7-7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| 01/ 2023 | GMRC*3.0*184                                                             | Sections updated to include changes for patch GMRC*3.0*184.  Updated Revision History, Table of Contents, Interfacility Consults When Used With Cerner Converted Sites section and HL7 field descriptions.                                                                                                                                                                                                                                                                                                                                                                                     |                       |
| 04/2022  | GMRC*3.	0*186                                                                          | Describes the new field to be displayed when editing or entering a community care consult service (Figure 5-10)  Review and approval of changes in section 2 and Figure 5-10.                                                                                                                                                                                                                                                                                                                                                                                                                  |                       |
| 09/2021  | GMRC*3.0*176                                                             | Update for GMRC*3.0*176  Refer to section 5.	39: On an incoming HL7 message from a Cerner-converted site, if the urgency code in ORC.7.	6 is “S” (STAT), which gets converted to “N” (NEXT AVAILABLE”).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| 05/ 2021 | GMRC*3.0*84                                                              | NSR 20110210:  Described GMRC*3.0*84 in section 2.	 Added information about Prosthetics Consult Updated to the list of consult notifications in section 7.	6 to the deletion of notifications and the implementation and maintenance sections in Appendix A: Install, Planning, and Implementation Checklist	.  Added information about enabling the Prosthetics Consult Updated notification and deleted redundant information throughout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| 03/ 2021 | GMRC*3.	0*170                                                                          | Replaced sentence in section 6.	2 with: “  **Error! Reference source not found.**  .”  Updated Title page, Revision History, Table of Contents, Index, and Footers (Title, ii, vi, 217, all)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.0*145                                                             | Added section 2.	2, which describes patch GMRC*3.0*145.  Revised dates on Title page and footers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*154                                                                          | Section 5.	35 and Appendix F                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*88                                                                          | Changes for Consults in v31b.  Added an item to Figure 5-1 to Define FSC HCP Mail Group.  Added notes in section 5 that update users can order tracking consults.  Added a reference in Figure 7.	16 to the GMRC FSC HCP SUPPORT EMAIL parameter.  Provided a full definition in Table 14-11 of the GMRC FSC SUPPORT EMAIL PARAMETER.  Listed in Table 9-1 the above parameter in an option list by options and display name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.0*139                                                             | Added to DST Consult handling in section 2.	3 and section 14.	20.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*123                                                                          | Added details for new patch in Table 14-7, section 14.	3.	3, section 14.4.	3, and section 14.5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*124                                                                          | Adds Decision Support Tool (DST) comment to a Consult when a Consult Order is signed and there is a DST comment listed in the Order. See section 14-20  and Table D-6.                                                                                                                                                                                                                                                                                                                                                                                                                         |                       |
| REDACTED | GMRC*3.	0*112                                                                          | Added details for new patch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                       |
| REDACTED | GMRC*3.	0*113                                                                          | Added details for Cancelled To Discontinued Consults. See section 6.	3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*110                                                                          | Added text and new screen shot to show the new field “UCID Display” on the order detail. See section 5.	34.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*107                                                                          | Added details for new GMRC Reports to support the ADMIN KEY consults for consults that are Administratively released by Policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*99 and GMRC*3.0*106                                                                          | Added features and setup for new logical link. See Table 14-3, Table 14-6, and section 14.	4.	2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*89                                                                          | Added information related to new functionality: Consult Closure Tool, Secondary Printer option for SF 513, and printing age and cell phone number on SF 513.                                                                                                                                                                                                                                                                                                                                                                                                                                   |                       |
| REDACTED | GMRC*3.	0*83                                                                          | Added information about the new MUMPS cross reference AG to be used only by the Scheduling Package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                       |
| REDACTED | GMRC*3.	0*81                                                                          | Changed Earliest Appropriate Date to Clinically Indicated Date. See section 5.	12.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*75                                                                          | Added information on components of a bi-directional interface that will connect Consults and HCPS. Refer to Table 14-2, Table 14-5, and section 14.	3.	1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3*73                                                                | ICD-10 Updates. Added info about changes made for the ICD-10 project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                       |
| REDACTED | Clarified “Service Team to Notify” field in Add Consult Services option. | Refer to section 5.	2 and Table 5-1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| REDACTED | GMRC*3.	0*76                                                                          | Added notes that the Ordering Provider will NOT receive an alert; added note that the clinician who requested the order is notified electronically.  Noted EARLIEST APPROPRIATE DATE will be used in place of DATE OF REQUEST.                                                                                                                                                                                                                                                                                                                                                                 |                       |
| REDACTED | GMRC*3.	0*74                                                                          | Added Define Fee Services (GMRC FEE PARAM) option and GMRC FEE SERVICES parameter and supporting GMRCFP* routines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                       |
| REDACTED | GMRC*3.	0*71                                                                          | Modified description for CONSULT/REQUEST UPDATED.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                       |
| REDACTED | Earliest Appropriate Date                                                | Refer to section 5-12.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                       |
| REDACTED | GMRC*3.	0*63                                                                          | Modified report format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                       |
| REDACTED | Patch 60                                                                 | Performance Monitor Report. Refer to section 5-12, Figure 5-18  , Figure 5-19  , and Figure 5-20  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                       |
|          | Patch 41                                                                 | Performance Monitor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                       |
|          | Include Patch 22                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patch 23                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patch 17                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patch 21                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patch 15, 19, and 20                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patches 13, 14, 16, and 18                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Add Patches 6 thru 8, 11, and 12                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Include Patches 1 thru 5                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |
|          | Originally released                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                       |

Table of Contents

Revision History	ii

List of Figures	xi

List of Tables	xiii

1.	Introduction	1

1.1.	Purpose of the Consult/Request Tracking Package	1

1.2.	Scope of the Manual	1

1.3.	Audience	1

2.	New Features	2

2.1.	GMRC*3.0*84	2

2.2.	GMRC*3.0*145	2

2.3.	GMRC*3.0*139	2

2.4.	GMRC*3.0*184	2

2.5.	GMRC*3.0*185	2

2.6.	GMRC*3.0*189	3

3.	Overview of Consults/Request Tracking	3

4.	Package Orientation	5

5.	Implementation and Maintenance	6

5.1.	Install, Planning, and Implementation Checklist	6

5.2.	Menu/Option Diagram	6

5.3.	Define Service Hierarchy	7

5.4.	Service Usage Definition	8

5.5.	Determine Service Functionality	10

5.6.	Set Up Consult Services (SS)	13

5.7.	Healthcare Claims Processing System (HCPS), CCRA COMMUNITY CARE, and DOD TREATMENT Consult Service Set-up	21

5.8.	Quick Orders	22

5.9.	Service Consults Pending Resolution	25

5.10.	Service User Management (SU)	26

5.11.	Group Update (GU)	31

5.12.	Consults Performance Monitor Report (PM)	34

5.13.	Print Consults by Provider, Location, or Procedure (PL)	37

5.14.	Print Test Page (TP)	38

5.15.	Determine Users' Update Authority (UA)	39

5.16.	Determine if User is Notification Recipient (UN)	39

5.17.	Determine Notification Recipients for a Service (NR)	40

5.18.	Test Default Reason for Request (TD)	41

5.19.	List Consult Service Hierarchy (LH)	43

5.20.	Copy Prosthetics Services (CP)	43

5.21.	Consult Closure Tool (CCT)	45

5.21.1.	Edit Configuration Component	45

5.22.	Inquire Configuration Component	48

5.23.	Run Configuration Component	48

5.23.1.	Searching for Patient Consults / Appointments / Notes	49

5.23.2.	Closing Out Consults	50

5.23.3.	Printing/Updating the CPRS Team List	52

5.24.	Duplicate Sub-Service (DS)	52

5.25.	Define Fee Services (FS)	53

5.26.	Inter-Facility Consults Reports	55

5.27.	IFC Requests	55

5.28.	Print IFC Requests	58

5.29.	IFC Requests by Patient	59

5.30.	IFC Requests by Remote Ordering Provider	60

5.31.	IFC Possible Erroneous Comment Report	62

5.31.1.	Viewing the Possible Erroneous Comment Report in Excel	63

5.32.	ADMIN KEY Reports	64

5.33.	Unique Consult ID (UCID) Conversion	64

5.34.	Unique Consult ID (UCID) Display	64

5.35.	Interfacility Consults When Used with Cerner Converted Sites	65

5.36.	VDIF	65

5.37.	MPI Patient Registration	65

5.38.	Cerner Mail Groups	66

5.39.	GMRC*3.0*176	66

6.	Cancelled to Discontinued Consults	67

6.1.	Overview	67

6.2.	Overnight Job	67

6.3.	Update of the New Index During Installation of Patch GMRC*3.0*113	68

6.4.	Installation Background Job that Updates the Index	68

6.5.	Editing the Entries in the New Parameter	68

7.	Inter-Facility Consults Management Options	70

7.1.	Test IFC Implementation	70

7.2.	List Incomplete IFC Transactions	71

7.3.	IFC Transaction Report	74

7.4.	Locate IFC by Remote Consult Number	76

7.5.	Monitor IFC Background Job Parameters	77

7.6.	Notification Parameters	77

7.7.	Consult Service Tracking	78

7.7.1.	Functionality	78

7.8.	Text Integration Utilities (TIU) Setup	79

7.8.1.	Consults Resulting Process	79

7.8.2.	Recommended Document Hierarchies	79

7.8.3.	Advantages of Strategy A	80

7.8.4.	Disadvantages of Strategy A	80

7.8.5.	Advantages of Strategy B	80

7.8.6.	Disadvantages of Strategy B	80

7.9.	TIU Setup Options	81

7.9.1.	TIU Define Consults	81

7.10.	Create Document Definitions	82

7.11.	TIU Maintenance	84

7.11.1.	Correcting Misdirected Results	84

7.12.	Medicine Interface	86

7.12.1.	Procedure Setup	87

7.12.2.	Linking Med Results to Procedure Request	89

7.12.3.	Removing Medicine Results from a Request	89

7.13.	Parameters	89

7.13.1.	GMRC CONSULT LIST DAYS	89

7.13.2.	GMRC FEE SERVICES	90

8.	Files	91

8.1.	File Globals	92

9.	Exported Menus	94

10.	Cross-References	97

11.	Archiving and Purging	102

12.	External Relations	103

12.1.	Private DBIA Agreements	103

13.	Internal Relations	105

13.1.	Package-Wide Variables	105

14.	Package Interface	106

14.1.	HL7 Fields	106

14.2.	Package Interface Notes	111

14.3.	HL7 Protocols	112

14.3.1.	Patch GMRC*3.0*75	112

14.3.2.	Patch GMRC*3.0*99	113

14.3.3.	Patch GMRC*3.0*123	114

14.4.	HL7 Application Parameters	114

14.4.1.	Patch GMRC*3.0*75	114

14.4.2.	Patch GMRC*3.0*99	115

14.4.3.	Patch GMRC*3.0*123	115

14.5.	HL7 Logical Link	115

14.6.	HL7 Referral Messages	116

14.7.	REF\_I12 Message Definition Tables	118

14.7.1.	REF\_I12 MSH - Message Header Segment	118

14.8.	REF\_I13 Message Definition Tables	129

14.8.1.	REF\_I13 MSH - Message Header Segment	129

14.9.	RRI\_I13 Message Definition Tables	139

14.9.1.	RRI\_I13 MSH - Message Header Segment	139

14.10.	REF\_I14 Message Definition Tables	150

14.11.	REF\_IN Message Definition Tables	158

14.12.	HL7 ACK Messages	161

14.13.	HL 7 Mailbox	166

14.14.	Order Event Messages	166

14.14.1.	Front Door – Consults	167

14.15.	Back Door Consults	168

14.16.	Orderable Item Updates – Request Services	171

14.17.	Orderable Item Updates - Procedures	172

14.18.	Ordering Parameters	173

14.19.	Procedure Calls	174

14.20.	Auto-forwarding	175

15.	How to Generate On-Line Documentation	176

15.1.	Routines	176

15.2.	Globals	176

15.2.1.	Files	176

15.3.	Menu/Options	176

15.4.	XINDEX	176

16.	Glossary	178

17.	Appendix A: Install, Planning, and Implementation Checklist	180

18.	Appendix B: Consult Tracking Worksheets	185

19.	Appendix C: Request Services Distributed with Consults	189

20.	Appendix D: Package Security	190

20.1.	Service Update and Tracking Security	190

20.1.1.	GMRC MGR Menu	192

20.1.2.	GMRC GENERAL SERVICE USER Menu	192

20.1.3.	GMRC PHARMACY USER Menu	192

20.1.4.	GMRC SERVICE TRACKING Option	192

20.1.5.	GMRC PHARMACY TPN CONSULTS Option	192

20.2.	Security Keys	192

20.2.1.	File Security	192

20.3.	Service Update Tracking Security	193

20.3.1.	GMRCACTM PHARMACY PKG MENU	193

20.4.	Routine Descriptions	193

20.5.	Routine Mapping	200

21.	Appendix E: Algorithms	201

21.1.	User Authority	201

22.	Appendix F: “Converted” Facility Error Notifications	202

## List of Figures

Figure 5-1: Service Usage	9

Figure 5-2: Set-Up Example	17

Figure 5-3: Set-Up Example (continued)	18

Figure 5-4: Set-Up Consult Services Group Example	19

Figure 5-5: Quick Order Example	21

Figure 5-6: Quick Order Example (continued)	22

Figure 5-7: Quick Order Example (continued)	23

Figure 5-8: Service Consults Pending Resolution Example	24

Figure 5-9: Notification Set-Up Example	26

Figure 5-10: Set-Up without Notification Example	26

Figure 5-11: Individual Set-Up Example	27

Figure 5-12: Individual with Privileges Set-Up Example	28

Figure 5-13: Team with Privileges Set-Up Example	29

Figure 5-14: Predefined Location-based Team Set-Up Example	29

Figure 5-15: Discontinued Service End-of-Year Consults Example	31

Figure 5-16: Discontinued Service End-of-Year Consults Example (continued)	32

Figure 5-17: Notification of Resolution Example	32

Figure 5-18: Consults Performance Monitor Report Example	33

Figure 5-19: Consults Performance Monitor Report Example(continued)	34

Figure 5-20: Delimited Consults Performance Monitor Report Example(continued)	35

Figure 5-21: EKG Consult Generation Example	36

Figure 5-22: EKG Consult Generation Example (continued)	37

Figure 5-23: Print Test Page Example	37

Figure 5-24: Determine Users' Update Authority Example	38

Figure 5-25: Determine if User is Notification Recipient Example	38

Figure 5-26: Determine Notification Recipients for a Service Example	39

Figure 5-27: Test Default Reason for Request – SS Option	41

Figure 5-28: Test Default Reason for Request – TD Option	41

Figure 5-29: List Consult Service Hierarchy	42

Figure 5-30: Copy Prosthetics Services Example	43

Figure 5-31: Edit Configuration Components Example .	45

Figure 5-32: Run Configuration Component	47

Figure 5-33: Close-Out Example	49

Figure 5-34: Browse Switch Managers Screen Example	50

Figure 5-35: Printing/Updating the CPRS Team List Example	51

Figure 5-36: Printing/Updating the CPRS Team List Example	52

Figure 5-37: Define Fee Services Option Example	52

Figure 5-38: Deleting a Service Example	53

Figure 5-39: Save and Quit Example	53

Figure 5-40: Dental Consults Report Example	55

Figure 5-41: Status Change Example	56

Figure 5-42: Print IFC Requests Example	57

Figure 5-43: IFC Requests by Patient Example	58

Figure 5-44: Medical Consult Example	59

Figure 5-45: Medical Consult Example (continued)	60

Figure 5-46: Running an IFC Possible Erroneous Comment Report	61

Figure 5-47: IFC Possible Erroneous Comment Report Example	62

Figure 6-1: Editing Entries Example	67

Figure 7-1: Checking Setup Example	70

Figure 7-2: List Incomplete IFC Transactions Example	71

Figure 7-3: List Incomplete IFC Transactions Example (continued)	72

Figure 7-4: IFC Transaction Log	74

Figure 7-5: IFC Transaction Log (continued)	74

Figure 7-6: Locating IFC by Remote Consult Number	75

Figure 7-7: IFC background job parameters	76

Figure 7-8: Plan B Example	80

Figure 7-9: Creating Document Definitions	81

Figure 7-10: Creating Document Definitions (continued)	81

Figure 7-11: Creating Document Definitions (continued)	82

Figure 7-12: Creating Document Definitions (continued)	82

Figure 7-13: Creating Document Definitions (continued)	83

Figure 7-14: TIU Maintenance Example	84

Figure 7-15: TIU Maintenance Example (continued)	85

Figure 7-16: Procedure Setup Example	86

Figure 7-17: GMRC CONSULT LIST DAYS Example	89

Figure 8-1: Consult Request Tracking File Diagram	92

Figure 14-1: New, signed Referral for Non VA Care Radiology Example	126

Figure 14-2: New, signed Referral for Non VA Care Radiology Example (continued)	127

Figure 14-3: New, signed Referral for Non VA Care Dental Example	127

Figure 14-4: Receive Referral Example	136

Figure 14-5: Schedule Referral Example	136

Figure 14-6: Comment Referral Example	137

Figure 14-7: Complete Referral Example	137

Figure 14-8: Receive Referral Example	147

Figure 14-9: Schedule Referral Example	147

Figure 14-10: Comment Referral Example	148

Figure 14-11: Complete Referral Example	148

Figure 14-12: Cancel Referral Example	156

Figure 14-13: Discontinue Referral Example	156

Figure 14-14: HL7 ACK Message Table Headings	161

Figure 14-15: Consult Example - Pulmonary Consult at bedside to rule out pneumonia	166

Figure 14-16: Consult Example - 	EKG at Bedside	167

Figure 14-17: Consult Example – Family Counseling	167

Figure 14-18: Consult Example - Pulmonary Consult at Bedside to Rule Out Pneumonia	169

Figure 14-19: Orderable Item Updates Example	171

Figure 14-20: Orderable Item Updates – Procedures Example	172

Figure 14-21: Procedure Calls Example	173

Figure 14-22: Procedure Calls Example (continued)	173

Figure 14-23: Procedure Calls Example (continued)	174

Figure 21-1: The Select Consult Management Option	200

## List of Tables

Table 5-1: Consult Management [GMRC MGR} Menu Options	5

Table 5-2: Service Functionality	10

Table 5-3: Supported Objects	40

Table 5-4: Inter-Facility Consults Report Descriptions	54

Table 7-1: Inter-Facility Consults Management Menu Options	69

Table 8-1: File Globals	91

Table 9-1: GMRC MCG Menu	93

Table 9-2: GMRC REPORTS Menu	93

Table 9-3: GMRC GENERAL SERVICE USER Menu	94

Table 9-4: GMRC PHARMACY USER Menu	94

Table 9-5: GMRC CONSULT CLOSURE TOOL Menu	94

Table 9-6: GMRC IFC MGMT Menu	95

Table 12-1: External Relations – Other VA Software	102

Table 12-2: External Relations – Other VA Software	102

Table 14-1: Private DBIA Agreements	105

Table 14-2: Patch GMRC*3.0*75 Protocol Description	111

Table 14-3: Patch GMRC*3.0*99 Protocol Description	112

Table 14-4: Patch GMRC*3.0*123 Protocol Description	113

Table 14-5: Patch GMRC*3.0*75 Application Parameters	114

Table 14-6: Patch GMRC*3.0*99 Application Parameters	114

Table 14-7: Patch GMRC*3.0*123 Application Parameters	114

Table 14-8: REF Message Standard Segments	115

Table 14-9: RRI Message Standard Segments	116

Table 14-10: REF\_I12 Message Header Table	117

Table 14-11: REF\_I12 RF1 - Referral Information Segment	118

Table 14-12: REF\_I12 PRD - Provider Data Segment	119

Table 14-13: REF\_I12 PID-Patient Id Segment	120

Table 14-14:  REF\_I12 DG1 - Diagnosis Segment	123

Table 14-15: REF\_I12 OBR - Observation Request Segment	123

Table 14-16: REF\_I12 PV1 – Patient Visit Segment	124

Table 14-17: REF\_112 NTE – Notes and Comments Segment	125

Table 14-18: REF\_I13 MSH - Message Header Segment	128

Table 14-19: REF\_I13 RF1 – Referral Information Segment	129

Table 14-20: REF\_I13 PRD - Provider Data Segment (Same for all message types)	130

Table 14-21: REF\_I13 PID – Patient Id Segment generated by the VistA API (Same for all message types)	131

Table 14-22: REF\_I13 DG1 – Diagnosis Segment (Same for all message types)	133

Table 14-23: REF\_I13 OBR – Observation Request Segment (Same for all message types)	133

Table 14-24: REF\_I13 PV1 - Patient Visit Segment (Same for all message types)	134

Table 14-25: REF\_I13 NTE – Notes and Comments Segment	135

Table 14-26: RRI\_I13 MSH - Message Header Segment Table	138

Table 14-27: RRI\_I13 RF1 – Referral Information Segment	139

Table 14-28: RRI\_I13 PRD - Provider Data Segment (Same for all message types)	140

Table 14-29: RRI\_I13 PID – Patient Id Segment (Same for all message types)	141

Table 14-30: RRI\_I13 DG1 – Diagnosis Segment (Same for all message types)	143

Table 14-31: RRI\_I13 OBR – Observation Request Segment (Same for all message types)	143

Table 14-32: RRI\_I13 PV1 – Patient Visit Segment (Same for all message types)	144

Table 14-33: RRI\_I13 NTE – Notes and Comments Segment	146

Table 14-34: REF\_I14 MSH - Message Header Segment	149

Table 14-33: REF\_I14 RF1 – Referral Information Segment	150

Table 14-36: REF\_I14 PRD – Provider Data Segment (Same for all message types)	151

Table 14-37: REF\_I14 PID – Patient Id Segment (Same for all message types)	152

Table 14-38: REF\_I14 DG1 - Diagnosis Segment (Same for all message types)	153

Table 14-39: REF\_I14 OBR – Observation Request Segment (Same for all message types)	154

Table 14-40: REF\_14 PV1 – Patient Visit Segment (Same for all message types	154

Table 14-41: REF\_I14 NTE – Notes and Comments Segment	155

Table 14-42: REF\_IN1 Segment (Valid for all above REF messages)	157

Table 14-43: REF\_IN3 Segment (Valid for all above REF messages)	159

Table 14-44: Standard ACK Message Segments	160

Table 14-45: ACK MSH - Message Header Segment	161

Table 14-46: ACK MSH - Message Header Segment	162

Table 14-47: ACK MSA - Message Acknowledgment Segment	163

Table 14-48: ACK ERR - Error Segment	163

Table 14-49: HL7 Table 0357 - Message Error Condition Codes	164

Table 14-50: MSA Message for NACK – Negative Application Acknowledgment Segment	165

Table 14-51: Front Door – Consults	166

Table 14-52: Back Door – Consults	168

Table 14-53: Orderable Item Updates – Request Services	170

Table 14-54: Orderable Item Updates - Procedures	171

Table 16-1: Glossary	177

Table 20-1: Package Security Options	189

Table 20-2: Consult Notifications Criteria	189

Table 20-3: Privileges	190

Table 20-4: Files	190

Table 20-5: Recommended FileMan Access Codes	191

Table 20-6: Routine Descriptions	192

Table 20-7: Routine Mapping	199

Table 22-1: Facility Error Notifications	201

## 1 Introduction

### Purpose of the Consult/Request Tracking Package

The Consult/Request Tracking package (Consults) has been developed to improve the quality of patient care by providing an efficient mechanism for clinicians to order consults and requests using Computerized Patient Record System (CPRS) Order Entry, and to permit hospital services to track the progress of a consult order from the point of receipt through its final resolution.

### Scope of the Manual

This manual provides technical descriptions of Consults tracking routines, protocols, files, globals, options, security data, menu diagrams and any other information required to effectively set up and use the Consults package.

From time-to-time, improvements are made to the Consults package. The latest information about Consults, as well as the latest version of this manual, is posted on the Consults Web Page at: vista.med.va.gov/consults.

### Audience

Information in this manual is technical in nature and is intended to be used by Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS) staff members and Clinical Application Coordinators (CAC's).

## 2 New Features

### GMRC*3.0*84

This patch, part of the software release for CPRS graphical user interface (GUI) v32a, introduces the new PROSTHETICS CONSULT UPDATED notification. This notification will be generated whenever users add comments to or take the schedule action upon a prosthetics consult in CPRS GUI.

### GMRC*3.0*145

This patch, part of the larger CPRS GUI v31 Mission Act release, assists with implementing the Decision Support Tool (DST) and Consult Toolbox (CTB) directly into CPRS GUI. Please consult the DST and CTB user manuals on the Veterans Health Information System and Technology Architecture (VistA) Document Library for detailed information regarding use of these features.

### GMRC*3.0*139

This patch adds auto-forwarding functionality. When the DST transmits the auto-forward information to CPRS, the existing CPRS remote procedure call (RPC) process will detect the auto-forward request and forward the order to a new consult location, which is referenced in the REQUEST SERVICE file (#123.5).

### GMRC*3.0*184

This patch adds functionality for IFC order communication between non-converted VistA sites and converted Cerner sites. Data required by Cerner are extracted from HL7 order messages and saved in the REQUEST/CONSULTATION file (#123) for later use, so VDIF (Veterans Data Integration and Federation) is no longer required to do so. PID and OBR segments are added to outgoing HL7 messages destined for Cerner populated per Cerner requirements. Cumulative comments are sent to converted sites except if the IFC is for Prosthetics.

### GMRC*3.0*185

This patch loads data required by Cerner in PID and OBR segments for IFCs entered prior to the release of GMRC*3.0*184. It adds functionality for IFC order communication between non-converted VistA sites and converted Cerner sites. Prosthetics data required by Cerner are extracted from HL7 order messages and saved in the REQUEST/CONSULTATION file (#123) for later use, so VDIF (Veterans Data Integration and Federation) is no longer required to do so. Cumulative comments are sent to converted sites for 5 additional CPRS actions not included in patch 184. Finally, the VistA instance station number replaces the ORDERING FACILITY (field #.05 of file #123) in the outgoing OBR segment.

### GMRC*3.0*189

This patch adds the following functionality for IFCs exchanged between non-converted VistA sites and Cerner:

- Recognizes when an IFC order sent by VistA to Cerner is received but not processed by Cerner, queues the order for re-transmission the next day by adding the order to the IFC MESSAGE LOG (file #123.6) with an error code 203 – Patient not in Cerner.
- For IFC orders incoming from Cerner to VistA, modifies the processing when the referenced patient is not found in the PATIENT file (#2) by calling the proxy add API introduced by DG*5.3*1096.
- Researching issues for IFCs between VistA and Cerner is hampered by the quick purging of HL7 records from VistA.  GMRC*3*189 calls APIs to record HL7 messages for IFCs sent by Cerner to a non-converted VistA site or by VistA to Cerner in the HL7 message repository provided by EHM*1*10.
- Increases the size of the REMOTE CONSULT FILE ENTRY field (#.06) of the REQUEST/CONSULTATION file (#123)  from 12 to 20 digits to handle longer Cerner order numbers expected in the future. Recognizes when a patient is missing from the converted VistA that corresponds to the Cerner ordering site and calls the proxy add API introduced by DG*5.3*1096.
- When a comment is entered on a consult post-complete, the patch changes the comment status sent in OBX-11 from Preliminary (P) to Changed (C).
- GMRC*3*154 introduced a mechanism for the IFC interface to proxy add a patient to Cerner before transmitting a new order.  The proxy add API operates asynchronously in part with the update to the Treating Facility List being done after a return value is sent back to the calling routine. As a result, the new order messages cannot always be routed to Cerner after the API is called.  GMRC*3*189 generates a 205 error (waiting for treating facility to update) and re-queues the new order for transmission the next time the Background Processor runs.
- When the proxy add process fails, patch GMRC*3*189 generates a Mailman message to the IFC PATIENT ERROR MESSAGES mail group.

## 3 Overview of Consults/Request Tracking

The Consults package provides an interface with CPRS Order Entry which permits clerks or clinicians to enter, edit, and review consults and requests within the CPRS package.

- Service/Specialty personnel targeted to receive consults may use this package to:
- Have consults or requests electronically relayed to them.
- Track the service/specialty's activity concerning the consult or request, from the time of its receipt to its final resolution.
- Associate Text Integration Utility (TIU) consult reports with the consult request.

When a consult or request is updated on-line to a "completed” or “discontinued” status by the specialty service personnel, the original clinician who requested the order is notified electronically of the order's resolution. The clinician may then use “View Alerts” or the Detailed Display option in either the Consults or CPRS packages to review any comments or results which may be associated with the order's resolution.

**Note:** When using the Group Update functionality, the Ordering Provider will NOT receive an alert when a consult or request is updated online to a “completed” or “discontinued” status.

Functionality has been provided for IRMS/ADPAC personnel to set up and manage the consult service hierarchy.

A checklist is provided (in Appendix A of this manual) to help you install, plan, and implement the Consults package. Use the checklist in conjunction with the detailed information provided in the **Implementation and Maintenance** section of this manual.

## 4 Package Orientation

This technical manual provides IRMS/ADPAC personnel with technical descriptions of Consults routines, files, options, and other necessary information required to effectively implement and use the Consults package.

This manual should assist you in:

- Setting up a hierarchy of site-specific services/specialties.
- Setting up Notification users/teams related to a service, who will be notified when an order is released by CPRS order entry.
- Setting up tracking update capabilities for specific services/specialties to track the progress of ordered consults or procedures from receipt to their completion or discontinuance.
- Setting up procedures to be used in the resulting process for specified services.

**Note:** The primary care clinician and clinic clerk add, edit, discontinue, and sign capabilities for ordering consults or requests are provided through CPRS V. 1.	0. See the CPRS Clinical Coordinator &amp; User Manual for descriptions of how to use the CPRS options.

For package-specific user conventions, please refer to the Package Orientation section of the Consult/Request Tracking User Manual.

## 5 Implementation and Maintenance

### Install, Planning, and Implementation Checklist

A checklist is provided to help you install, plan, and implement the Consults package (see Appendix A). Use the checklist in conjunction with the detailed information provided in this "Implementation and Maintenance" section.

### Menu/Option Diagram

The tools required to implement and maintain the Consults package are found in the Consult Management [GMRC MGR] menu. Refer to Table 5-1, which lists and defines all of the options distributed with the Consults package

Table 5-1: Consult Management [GMRC MGR} Menu Options

| Menu Option   | Menu Option Description                            |
|---------------|----------------------------------------------------|
| RPT           | Consult Tracking Reports ...                       |
| ST            | Completion Time Statistics                         |
| PC            | Service Consults Pending Resolution                |
| CC            | Service Consults Completed                         |
| CP            | Service Consults Completed or Pending Resolution   |
| IFC           | IFC Requests                                       |
| IP            | IFC Requests By Patient                            |
| IR            | IFC Requests by Remote Ordering Provider           |
| NU            | Service Consults with Consults Numbers             |
| PI            | Print IFC Requests                                 |
| PL            | Print Consults by Provider, Location, or Procedure |
| PM            | Consult Performance Monitor Report                 |
| PR            | Print Service Consults by Status                   |
| SC            | Service Consults By Status                         |
| TS            | Print Completion Time Statistics Report            |
| SS            | Set up Consult Services                            |
| SU            | Service User Management                            |
| CS            | Consult Service Tracking                           |
| RX            | Pharmacy TPN Consults                              |
| TP            | Print Test Page                                    |
| GU            | Group update of consult/procedure requests         |
| UA            | Determine users' update authority                  |
| UN            | Determine if user is notification recipient        |
| NR            | Determine notification recipients for a service    |
| TD            | Test Default Reason for Request                    |
| LH            | List Consult Service Hierarchy                     |
| PR            | Setup procedures                                   |
| CP            | Copy Prosthetics services                          |
| CCT           | Menu for Closure Tools…                            |
| EDT           | Consult Closure Tool Edit Configuration            |
| INQ           | Consult Closure Tool Inquire Configuration         |
| RUN           | Consult Closure Tool Run Configuration             |
| DS            | Duplicate Sub-Service                              |
| FS            | Define Fee Services                                |
| IFC           | IFC Management Menu                                |
| TI            | Test IFC implementation                            |
| LI            | List incomplete IFC transactions                   |
| IFC           | IFC Requests                                       |
| TR            | IFC Transaction Report                             |
| LK            | Locate IFC by Remote Cslt #                        |
| BK            | Monitor IFC background job parameters              |
| EC            | IFC Possible Erroneous Comment Report              |
| IP            | IFC Requests By Patient                            |
| IR            | IFC Requests by Remote Ordering Provider           |
| PI            | Print IFC Requests                                 |

To get you started placing “CONSULT...” orders via CPRS, the option above which requires immediate attention is the Set up Consult Services (SS) option. Before setting up services, you should define your service hierarchy and determine service functionality.

### Define Service Hierarchy

At this point the site must determine which services/specialties should be set up to receive consults and requests. Consults Tracking Service Worksheets, along with descriptions of the type of information that should be recorded in each field on the worksheets, are provided in Appendix B of this manual to assist you in this process.

The Request Services file (#123.5) is distributed with a small selection of services. The hierarchical relationships are not in place upon distribution. See Appendix C for an example of how these services could be related hierarchically to get you started. Appendix C will Illustrate the file's hierarchy capabilities (similar to the Option file (#19) hierarchy) with “ALL SERVICES” representing the top of the hierarchy.

**Note:** Due to the tight relationship between CPRS orderable items and this file, a service should NEVER be deleted at any point. The best recommendation would be to disable the service and remove it from the ALL SERVICE hierarchy.

The Service/Specialty hierarchy you define can be as complex as needed to meet service requirements at your site. To get started, you will probably want to specify a small subset of services/specialties and add to them over a period of time. "ALL SERVICES" needs to be the top entry in the hierarchy.

**Note:** “ALL SERVICES” should be the top hierarchy service. All Services should never be the sub-service of another service.

In order to build the service hierarchy, you will need to know how the service entry in the Request Services file (#123.5) is used. Some services will be used as a GROUPER ONLY and other services may be used for TRACKING ONLY. The SERVICE USAGE field is provided for you to differentiate the services in the hierarchy.

To see your site's hierarchy, use the List Consult Service Hierarchy [GMRC LIST HIERARCHY] option.

**User Guidance: If your site is getting an allocation of partition space type of error when ALL SERVICES or another service is specified at the "Select Service/Specialty:" prompt, this is an indication that the hierarchy is set up wrong. This is typically caused by a service being made a sub-service of itself. A service being a sub-service of one of its own sub-services will also manifest this error.**

### Service Usage Definition

Whenever a value is defined for the SERVICE USAGE field in the Set up Consults Services [GMRC SETUP REQUEST SERVICES] option, the Service entry will NOT be selectable to send consults to in the CPRS ordering process. Instead, entries in this field reserve the service for special uses within the Consults flow of information.

Service Usages cause functioning as follows:

- UBLANKU: Permits consults and procedure requests to be sent to this service. A service may be reset to blank by entering an @ sign.
- UGROUPER ONLYU: Permits a service to be used for grouping other services together for review purposes, and aids in defining the service hierarchy (e.g., ALL SERVICES, INPATIENT SERVICES, OUTSIDE SERVICES). During the order process, a user selecting a grouper only service will be shown the service hierarchy under that service grouper. A grouper only service should never be a service a consult is sent to.
- UTRACKING ONLYU: Permits a service to be defined in a hierarchy, but does not permit users ordering consults in CPRS to be able to see or select a service marked for TRACKING ONLY (e.g., Psychology may be defined with its Service Usage blank, and its sub-specialty multiple defined with services of which some or all may be TRACKING ONLY services. This hierarchy facilitates the situation when a service such as Psychology prefers a UcommonU location for all related consults to be sent to. A tracking user at the UcommonU location then “Forward(s)” the request to one of the TRACKING ONLY services for completion). These services are viewable and may be selected directly by Update users for that service.
- UDISABLEDU: Disabled services are not selectable for ordering or tracking. An example of a potential hierarchy a user would see when ? or ?? are entered at a “Select Service/Specialty: ALL SERVICES” prompt follows. It includes notations for Service Usage definition examples.

Refer to Figure 5-1.

Figure 5-1: Service Usage

<!-- image -->

### Determine Service Functionality

The primary option needed to set up your hierarchy of services is the Set up Consults Services (SS) option. This option updates the Request Services file (#123.5).

You can enable the following functionality, depending on how much information you define for each hospital service in the Request Services file (#123.5).

Functionality you define may vary by Service/Specialty. Also, functionality may or may not be inherited, depending on the setting of the PROCESS PARENTS FOR UPDATES (.07) and PROCESS PARENTS FOR NOTIFS (.08) fields. If a child service has a Yes in these fields, then parents are checked for the appropriate actions. If all services are set to Yes, then all services are checked to the top of the service hierarchy. Alternately, some services can be marked Yes and others marked No. In this case the hierarchy is checked until a No is encountered.

Refer to Table 5-2.	 Two options provided in the Consult Management [GMRC MGR] menu option permit definition and maintenance of this functionality. All of the fields below may be updated using the Set Up Consult Services [GMRC SETUP REQUEST SERVICES] option. For ongoing maintenance of service users specified in 3 and 4 below, use the Service User Management [GMRC SERVICE USER MGMT] option.

Table 5-2: Service Functionality

| Functionality Enabled                                                                                                                                            | Related Fields That May Be Completed   | Related Fields That May be Completed        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|---------------------------------------------|
| Feature                                                                                                                                                          | Field #                                | Field Name                                  |
|                                                                                                                                                                  |                                        |                                             |
| Ordering consults from the "ALL SERVICES" hierarchy in CPRS and Review of Consults via the Consults options distributed to users.                                | .01                                    | NAME                                        |
|                                                                                                                                                                  | 2                                      | SERVICE USAGE                               |
|                                                                                                                                                                  | 10                                     | SUB-SERVICE/SPECIALTY (multiple)            |
| Automatic print of a Consultation Form (SF 513) at the service receiving the consult when CPRS order entry releases the order.                                   | 123.09                                 | SERVICE PRINTER                             |
| Service/Specialty update of Consults activity with automatic notification to the requesting service and to the original requester of the order upon resolution.  | .06                                    | UNRESTRICTED ACCESS                         |
|                                                                                                                                                                  | 123.03                                 | NOTIFY SERVICE ON DC                        |
|                                                                                                                                                                  | 123.04                                 | SERVICE INDIVIDUAL TO NOTIFY                |
|                                                                                                                                                                  | 123.08                                 | SERVICE TEAM TO NOTIFY (multiple)           |
|                                                                                                                                                                  | 123.1                                  | UPDATE USERS W/O NOTIFICATIONS (multiple)   |
|                                                                                                                                                                  | 123.3                                  | UPDATE TEAMS W/O NOTIFICATIONS (multiple)   |
| Service/Specialty update of Consults activity with automatic notification to the requesting service and to the original requester of the order upon resolution.  | 123.35                                 | UPDATE USER CLASSES W/O NOTIFS (multiple)   |
| Automatic notification to service individuals or teams when CPRS releases the order. Assuming these users have the "NEW SERVICE CONSULT" notification turned on. | 123.08                                 | SERVICE INDIVIDUAL TO NOTIFY                |
|                                                                                                                                                                  | 123.1                                  | SERVICE TEAM(S) TO NOTIFY (multiple)        |
|                                                                                                                                                                  | 123.2                                  | NOTIFICATION BY PATIENT LOCATION (multiple) |
| Ability to administratively complete consults, either singly or by date range.                                                                                   | 123.33                                 | ADMINISTRATIVE UPDATE USER (multiple)       |
|                                                                                                                                                                  | 123.34                                 | ADMINISTRATIVE UPDATE TEAM (multiple)       |
|                                                                                                                                                                  | 123.5                                  | SPECIAL UPDATES INDIVIDUAL                  |
| Ability to administratively complete consults, either singly or by date range.                                                                                   | 123.33                                 | ADMINISTRATIVE UPDATE USER (multiple)       |
|                                                                                                                                                                  | 123.34                                 | ADMINISTRATIVE UPDATE TEAM (multiple)       |
|                                                                                                                                                                  | 123.5                                  | SPECIAL UPDATES INDIVIDUAL                  |
| Inter-Facility Service Configuration.                                                                                                                            | 123.5134                               | IFC ROUTING SITE                            |
| IFC REMOTE NAME                                                                                                                                                  |                                        |                                             |
| IFC SENDING FACILITY                                                                                                                                             |                                        |                                             |
| IFC COORDINATOR                                                                                                                                                  |                                        |                                             |
| Secondary Consult Service Printer for Consultation Form (SF 513)                                                                                                 | 689                                    | SECONDARY PRINTER                           |

### Set Up Consult Services (SS)

The Set Up Consult Services command creates and maintains new records in the REQUEST SERVICES (#123.5) file. The following fields are involved:

- **SERVICE NAME:** This is the Name of a service or specialty which may receive consult/requests. This may also be a name which represents a group of services or specialties.
- **ABBREVIATED PRINT NAME:** This is a commonly known Abbreviation for this Service/Specialty. This name is used to build Consult Notifications and must be 7 characters or less in length.
- **INTERNAL NAME:** This is an alternate name for the service. This name does not appear on printouts or displays but can be used to access the service through the Setup Services (SS) option, or with FileMan.
- **SYNONYM:** Identifies the commonly known names and abbreviations for the Service named in the .01 Name field. Synonyms identified here are used in the look-up of services at “Select Service/Specialty:” prompts as well as during ordering in CPRS.
- **SERVICE USAGE:** Whenever a value is defined in the SERVICE USAGE field, the Service entry will NOT be selectable to send consults TO in the OE/RR ordering process. Service Usages cause functioning as follows:
    - **GROUPER ONLY:** Allows a service to be used for grouping other services together for review purposes, and aids in defining the service hierarchy (e.g., ALL SERVICES, INPATIENT SERVICES, OUTSIDE SERVICES). During the order process, a user selecting a grouper only service will be shown the service hierarchy under that service grouper. A Grouper ONLY service should never be a "TO" Service on a consult.
    - **TRACKING ONLY:** Allows a service to be defined in a hierarchy but will not allow users ordering consults in OE/RR to be able to see or select a service marked for TRACKING ONLY. (e.g., Psychology may be defined with its Service Usage blank, and its Sub-specialty multiple defined with services of which some or all may be "TRACKING ONLY" services. This hierarchy facilitates the situation when a service, such as Psychology, prefers a common location for all related consults to be sent to. A Tracking user at the common location then "Forwards" the request to one of the sub-service TRACKING ONLY services for completion.) Update users for the service can see and order directly to a tracking service.
    - **DISABLED:** Disabled services are not selectable for ordering or tracking. Existing requests for a disabled service may still be processed to completion.
    - **SERVICE PRINTER:** Allows the service/specialty to identify a device that will be used for printing Consult Forms (SF 513) 'automatically' at the service when the consult/request order is released by CPRS. If the device is not defined, the Consult Form will not print unless a default service copy device is defined for the Consults package for the ordering location. The default service copy device parameter can be found by using the Print Parameters for Wards/Clinics [OR PARAM PRINTS (LOC)] option.
    - **SECONDARY PRINTER:** Allows the service/specialty to identify a secondary printer device that will be used for printing Consult Forms (SF 513) at a second location when the consult/request order is released by CPRS and during any print request for SF 513.
    - **NOTIFY SERVICE ON DC** : Controls when members configured to receive notifications for this service in the Consult hierarchy will be alerted to a consult being discontinued. This field can be set to ALWAYS, NEVER, or REQUESTOR ACTION. REQUESTOR ACTION stipulates notification only if the user discontinuing the consult is not an update user for the consulting service.
    - **REPRINT 513 ON DC:** This field will determine if the SF 513 should reprint to the consulting service when a consult is discontinued. Again, the three choices are ALWAYS, NEVER, or REQUESTOR ACTION. REQUESTOR ACTION stipulates reprinting only if the user discontinuing the consult is not an update user for the consulting service.
    - **PROVISIONAL DX PROMPT:** Used by CPRS to determine how to prompt for the provisional diagnosis when ordering consults for this service. If this field is set to OPTIONAL, the user will be prompted for the provisional diagnosis but may bypass answering the prompt. If the field is set to SUPPRESS, the user will not be presented with the provisional diagnosis prompt. If set to REQUIRED, the user must answer the prompt to continue placing the order.
    - **PROVISIONAL DX INPUT:** Determines the method that CPRS uses to prompt the user for input of the provisional diagnosis when ordering a consult. If set to FREE TEXT, the user may type any text from 2-80 characters in length. If set to LEXICON, the user will be required to select a coded diagnosis from the Clinical Lexicon.
    - **PREREQUISITE:** This word-processing field is utilized to communicate pre-requisite information to the ordering person prior to ordering a consult to this service. This field is presented to the ordering person upon selecting a Consult service and allows them to abort the ordering at that time if they choose. TIU objects may be embedded within this field which are resolved for the current patient during ordering. Any TIU objects must be contained within vertical bars (e.g. |BLOOD PRESSURE|).
    - **DEFAULT REASON FOR REQUEST:** The default text used as the reason for request when ordering a consult for this service. This field allows a boilerplate of text to be imported into the reason for request when placing consult orders for this service. If the user places an order using a quick order having boilerplate text, that text supersedes any default text stored in this field. This field may contain any text including TIU objects. TIU Objects must be enclosed in vertical bars (e.g. |PATIENT NAME|).
    - **RESTRICT DEFAULT REASON EDIT:** If a DEFAULT REASON FOR REQUEST exists for this service this field effects the ordering person's ability to edit the default reason while placing an order. This variable can be set to UNRESTRICTED, NO EDITING, or ASK ON EDIT ONLY. If the third value, ASK ON EDIT ONLY, is used, the user is only allowed to edit the default reason if the order is edited before releasing to the service.
    - The following three fields are only filled in if this is an Inter-Facility consult. The first two are used if you are a requesting facility. The third, IFC SENDING FACILITY, is used if you are a consulting facility.
        - **IFC ROUTING SITE:** This field contains the VA facility that will perform consults requested for this service. When a consult for this service is ordered, it will automatically be routed to the VA facility in this field.
        - **IFC REMOTE NAME:** This field contains the name of the service that will be requested at the VAMC defined in the IFC ROUTING SITE field. Enter the name of the service exactly as it is named at the remote facility. If this name does not match the name of the service at the routing site, the request will fail to be filed at the remote site. This will delay or prohibit the performance and processing of this request.
        - **IFC SENDING FACILITY** : This is a multiple containing the facilities from which your site may receive Inter-Facility Consults for this consult. As with all IFC fields, they must be an exact match.
- **SERVICE INDIVIDUAL TO NOTIFY:** A user may be identified in this field as having primary responsibility for receiving consults and tracking them through to completion or discontinuance. This individual will receive a "NEW SERVICE CONSULT" notification type when a new order is released to the service through CPRS. The user must have the "NEW SERVICE CONSULT/REQUEST" notification type enabled.
- **SERVICE TEAM TO NOTIFY:** The name of the Service Team that is to receive notifications of actions taken on a consult. A team of users may be identified (from the OE/RR LIST file #100.21) who will receive a "NEW SERVICE CONSULT" notification when a new order is released to the service through OE/RR. The individuals on the teams must have the "NEW SERVICE CONSULT/REQUEST" notification type turned "ON". Team members will be able to perform update tracking capabilities.

**Note:** The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment. (Remedy Ticket 903302 pointed this out.)

- **NOTIFICATION BY PT LOCATION:** A ward location or hospital location which the service wishes to assign a service individual or team to. When a consult or request is ordered, notifications to the receiving service checks to see if the patient’s location is defined here. If defined, notifications are sent to an individual and/or members of a team specifically associated with this location.
- **PROCESS PARENTS FOR NOTIFS:** This field, if set to YES, causes the parent service of this service to be processed when determining notification recipients. The check is carried up the chain until ALL SERVICES is reached or until a service is marked NO.
- **UPDATE USERS W/O NOTIFICATIONS:** A list of individuals who can do update tracking, but who will not get a notification.
- **UPDATE TEAMS W/O NOTIFICATIONS:** A list of teams to be assigned update authority for this service. All clinicians in the teams have update authority no matter what patients are in the teams.
- **UPDATE USER CLASS W/O NOTIFS:** A list of user classes to be assigned update authority for this service. All persons assigned to the user classes included have update authority with the current service.
- **ADMINISTRATIVE UPDATE USER:** A list of the users for a service who can perform Administrative Completes (Completes without a note attached). Optionally, this individual can be set as a notification recipient.
- **ADMINISTRATIVE UPDATE TEAM:** This is a list that contains the names of team lists from the OE/RR LIST (#100.21) file. All provider/users of the teams will have administrative update authority for requests directed to this service and the teams can optionally be designated as notification recipients.
- **PROCESS PARENTS FOR UPDATES:** This field, if set to YES, will cause the parent services of this service to be screened to determine update authority for a given user. Hence, if an individual is set as an update user in a grouper service, this individual will have privileges for all sub-services that have this field set to YES.
- **SPECIAL UPDATES INDIVIDUAL:** This individual will have privileges to perform group status updates for this service or any of the entries in the SUB-SERVICE/ SPECIALTY field. It is recommended that this individual be a responsible service update user or a Clinical Application Coordinator. If given the option Group update of consult/procedure requests [GMRCSTSU], the user will be able to choose all requests within a date range that are pending, active or both and update the request to discontinued or complete. This will also update the related order in CPRS to the same status.
- **RESULT MGMT USER CLASS:** This field defines the Authorization/Subscription User Class that is permitted to disassociate a Medicine result from a Consult request. It is recommended that this function be restricted to a very select group of individuals.
- **UNRESTRICTED ACCESS:** This field, if set to yes will allow all users to perform the full range of update activities on consult or procedure requests directed to this service. If this field is set to yes, all other fields related to assignment of update users are ignored. The SERVICE INDIVIDUAL TO NOTIFY and the SERVICE TEAM(S) TO NOTIFY fields are still used to determine notification recipients for each individual service.
- **SUB-SERVICE/SPECIALTY:** This is the list of sub-service/specialties that are grouped under this Service. The sub-service/specialty entries must each be defined as entries in this file. There is no limit on how deep the hierarchy of services may be defined. The only requirement is that the "ALL SERVICES" entry be at the top of the hierarchy. It is also highly recommended that a service be defined as the sub-service of only one entry in the hierarchy.
- **ADMINISTRATIVE:** This field, if set to yes, will allow requests placed to this service to be excluded from the Consults Performance Monitor report. When a request is directed to a service marked as administrative, the request itself is also marked as administrative. This is done via a Trigger cross-reference on the TO SERVICE field of file 123.

Refer to Figures 5-2 to 5-5, which furnish an example of the set-up of a new service, ARTHRITIS.

Figure 5-2: Set-Up Example

<!-- image -->

Figure 5-3: Set-Up Example (continued)

<!-- image -->

**Note:** When you create a new service, it is not automatically linked into the Consults hierarchy. You must explicitly group each service under ALL SERVICES or under another service that in turn is grouped under ALL SERVICES. Until this is done, the new service is not visible in the service hierarchy and cannot be selected for any action.

Use the Set-Up Consult Services (SS) action to group services. Refer to Figure 5-4. In this example, the ARTHRITIS service is grouped under ALL SERVICES:

Figure 5-4: Set-Up Consult Services Group Example

<!-- image -->

### Healthcare Claims Processing System (HCPS), CCRA COMMUNITY CARE, and DOD TREATMENT Consult Service Set-up

Use the following steps to send a consult to HCPS or to CCRA:

1. Select SS Set Up Consult Services.
2. Set up a new consult service that contains ‘NON VA CARE HCPS’ (e.g., NON VA CARE HCPS HEMODIALYSIS). Note that the service name must contain “NON VA CARE HCPS” as the prefix in order to be processed by HCPS. This naming convention was created to adhere to existing Non VA Care (NVC) naming and reporting standards.  All NVC services begin with “NON VA CARE”. “HCPS” was also added to identify the transactions that will be sent to HCPS.  All services that are intended to be sent to HCPS must contain “HCPS” after “NON VA CARE” (e.g., NON VA CARE HCPS…). To send consults to CCRA, the consult service needs to begin with “COMMUNITY CARE-“. This exact naming will allow the system to transfer community care consults to CCRA’s HealthShare Referral Manager (HSRM) application. Similarly, for DOD, the service name needs to begin with “DOD TREATMENT”.
3. When setting up a community care consult service, you will be prompted to enter a community care clinic to use when making an appointment. When editing or entering a community care consult service, you will be prompted with the following:

**SELECT HOSPITAL LOCATION NAME** : This field is only displayed if the consult service is for a community care consult. If entering or editing a community care consult, select a community care clinic that will be used when scheduling appointments.

1. Associate the new consult service with the appropriate template.
2. When the template is selected from the Order a Consult screen, it will be routed to HCPS once filled out and accepted.

### Quick Orders

1. Define the quick order with the Enter/edit quick orders option of the Order Menu Management menu.
2. Put the quick order on an order entry menu with the Enter/edit order menus option of the Order Menu Management menu.

Refer to Figures 5-5 to 5-7, which depict the set-up of a quick order called NUTRITION:

Figure 5-5: Quick Order Example

<!-- image -->

Figure 5-6: Quick Order Example (continued)

<!-- image -->

<!-- image -->

Figure 5-7: Quick Order Example (continued)

<!-- image -->

### Service Consults Pending Resolution

The purpose of the Service Consults Pending Resolution option is to list the pending and active consults. Use it to stay informed about the overall status of consults for your service. Someone in each clinic or service should review this list daily to make sure that all consults are being attended to. Refer to Figure 5-8.	 In this example, the option is used to view pending and active Pulmonary consults.

Figure 5-8: Service Consults Pending Resolution Example

<!-- image -->

### Service User Management (SU)

This option is used to make the most needed changes after a service has been created. This option changes fields that are all in records in the REQUEST SERVICES (#123.5) file. They include the following:

- **SERVICE INDIVIDUAL TO NOTIFY:** An individual who will receive a default notification of any action taken on a consult.
- **SERVICE TEAM TO NOTIFY:** The name of the Service Team that is to receive notifications of any actions taken on a consult.

**Note:** The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment. (Remedy Ticket 903302 pointed this out.)

- **NOTIFICATION BY PT LOCATION:** The name of a hospital location that is to receive notifications of any actions taken on a consult.
- **UPDATE USERS W/O NOTIFICATIONS:** The name of an individual who can do update tracking, but who will not get a notification.
- **UPDATE TEAMS W/O NOTIFICATIONS:** A team list of users to be assigned update authority for this service.
- **UPDATE USER CLASS W/O NOTIFS:** A user class to be assigned update authority for this service.
- **ADMINISTRATIVE UPDATE USER:** An individual who can perform Administrative Completes (Completes without a note attached).
- **ADMINISTRATIVE UPDATE TEAM:** A team who can perform Administrative Completes (Completes without a note attached).
- **SPECIAL UPDATES INDIVIDUAL:** This is the individual who can perform special updates for this particular service.

In order for the Service users to actually receive a new consult notification, the users must have the notification “NEW SERVICE CONSULT/REQUEST” turned ON for their use. See the CPRS Clinical Coordinator &amp; User Manual NOTIFICATION MGMT MENU option for more information on notifications and how to set them up.

Teams of users may be defined by an individual or team members with access to the “Team Management Menu” provided by CPRS. See the CPRS Clinical Coordinator &amp; User Manual for more information on Team Management and its recommended menu access. It is important to know that team users are sent the notification regardless of any patients who may be defined in that team list.

An example of setting up notifications is shown on the next page.

Refer to Figure 5-9. In the following example no changes are made. The prompts in the Service User Management option are cycled through so the prompts are identifiable.

Figure 5-9: Notification Set-Up Example

<!-- image -->

The individual and team names displayed are the current default values. In most cases they are the most recently used value for that prompt.

Refer to Figure 5-10. To set-up an individual to have update activities but receive no notification, do the following. This example sets up CPRSProvider, Three will have update privileges.

Figure 5-10: Set-Up without Notification Example

<!-- image -->

Sometimes it is necessary to administratively Complete (CT) consults that for one reason or another have not been resolved. To set up an individual who can complete other people’s consults do the following. This example sets up Ben Casey as an administrative user who can complete any Medicine Consult without a signature. Refer to Figure 5-11.

Figure 5-11: Individual Set-Up Example

<!-- image -->

Providers in the following categories have the authority to complete a consult for a service by writing a TIU document or attaching a medicine result:

- SERVICE INDIVIDUAL TO NOTIFY
- SERVICE TEAM TO NOTIFY
- NOTIFICATION BY PT LOCATION
- NOTIFICATION BY PT LOCATION, INDIVIDUAL and/or TEAM
- UPDATE USERS W/O NOTIFICATIONS
- UPDATE TEAMS W/O NOTIFICATIONS
- UPDATE USER CLASS W/O NOTIFS

Administrative updates differ from other complete actions in that they do not require a TIU note. The intention is for consults that are not to be completed normally (i.e., pt no-show) to be taken off the books. In the GUI (Windows) interface, Administrative Complete has its own menu command under consults tracking. If the current user has these privileges, then the menu command is activated by the program. In the List Manager interface, there is only the Complete (CT) command. If a user has both regular completion privileges and Administrative Complete privileges, the program inquiries regarding which Complete to pursue. To set up an individual who has update privileges and receives “NEW SERVICE CONSULT/REQUEST” notifications do the following. This example sets up Dr. Maven to receive alerts when a consult comes to the Medicine clinic. Refer to Figure 5-12.

Figure 5-12: Individual with Privileges Set-Up Example

<!-- image -->

To set up a predefined team of clinicians for a service that has update privileges and receives NEW SERVICE CONSULT/REQUEST notifications do the following. In this example, to set up the Gold team to receive notifications do the following: (Team set up is discussed in the CPRS Clinical Coordinator &amp; User Manual.) Refer to Figure 5-13.

Figure 5-13: Team with Privileges Set-Up Example

<!-- image -->

To set up individuals and a predefined team associated with a hospital ward location that have update activities and receives “NEW SERVICE CONSULT/REQUEST” notifications: (In this example we set up ward 2B Medical to receive notifications, along with Dr. Snow and the Green team. Team set up is discussed in the CPRS Clinical Coordinator &amp; User Manual.) The users entered in the NOTIFICATION BY LOCATION sub-fields will ONLY be notified if the requesting location for the consult matches the location for which they are entered here. So, in the case of the following example CPRSPROVIDER,ONE would only be notified for consults coming from 2B MED. Refer to Figure 5-14.

Figure 5-14: Predefined Location-based Team Set-Up Example

<!-- image -->

### Group Update (GU)

A Group Update can only be performed by an individual who has been set as the Special Updates Individual with the Set Up Consult Service (SS) or Service User Management (SU) option of the Consult Management (GMRC MGR) menu. This option should be exercised with great care because it can affect a large number of consults.

Refer to Figures 5-15 and 5-16. In this example, all consults before the first of the year that are not complete are discontinued for a specific service:

Figure 5-15: Discontinued Service End-of-Year Consults Example

<!-- image -->

Figure 5-16: Discontinued Service End-of-Year Consults Example (continued)

<!-- image -->

**Note** : When using the Group Update functionality, the Ordering Provider will NOT receive an alert when a consult or request is updated online to a “completed” or “discontinued” status by the specialty service personnel. The original clinical who requested the order is notified electronically of the order’s resolution.

Refer to Figure 5-17.

Figure 5-17: Notification of Resolution Example

<!-- image -->

### Consults Performance Monitor Report (PM)

This report was added with Consults patch GMRC*3*41 to satisfy performance monitor reporting requirements of the Veterans Integrated Service Network (VISN) Support Services Center (VSSC). For FY08, the VHA Deputy Undersecretary for Health for Operations and Management has published updates to the monitor definitions, and patch GMRC*3.	0*60 implements those updates.

- This report comes in two forms, a summary report for local use in tracking performance and a delimited report for use with spreadsheets software. The report will now have the following exclusions: Prosthetics consults, consults with a status of Cancelled or Discontinued, Administrative consults, and Inpatient consults.
- The ability to mark a service as administrative (via the Setup Services option) is new in patch GMRC*3.0*60. This new capability is an attempt to further refine the process of measuring the completion rate performance.
- With Patch GMRC*3.0*81, developers changed the report to use CLINICALLY INDICATED DATE in place of EARLIEST APPROPRIATE DATE.
- In the following example a Summary report is printed for the Cardiology service for the third quarter of FY05:

Refer to Figures 5-18 and 5-19.

Figure 5-18: Consults Performance Monitor Report Example

<!-- image -->

Figure 5-19: Consults Performance Monitor Report Example(continued)

<!-- image -->

Refer to Figure 5-20. In this example a Delimited report is generated covering the Medicine grouper for second quarter, FY 2005 (setting the columns to 256 will prevent values from wrapping to the next line).

Figure 5-20: Delimited Consults Performance Monitor Report Example(continued)

<!-- image -->

### Print Consults by Provider, Location, or Procedure (PL)

This provides three different reports under one menu option [GMRC PRINT BY SEARCH]. The option asks for search criteria: Sending Provider, Location, or Procedure. You can further limit the search by entering a date range and CPRS status. The option also prompts for report format. The report format can be one of the following:

- 80 column standard print [STANDARD].
- 132 column standard print.
- Table without headers (export to another application).

Refer to Figures 5-21 and 5-22. In this example, a list of EKG consults is generated.

Figure 5-21: EKG Consult Generation Example

<!-- image -->

Figure 5-22: EKG Consult Generation Example (continued)

<!-- image -->

### Print Test Page (TP)

Sometimes the pagination on SF 513 is correct on some printers but incorrect on others. The Print Test Page command is provided for diagnosing incorrectly paginated SF 513s. Instructions for correcting this situation are printed with the test page. Bring the test page to IRM for resolution of the problem.

Refer to Figure 5-23. In this example, we run the Print Test Page option on a specified printer.

Figure 5-23: Print Test Page Example

<!-- image -->

### Determine Users' Update Authority (UA)

Sometimes it is necessary to quickly check on the authority of a service user. The Determine Users’ Update Authority option of the Consults Management menu does this.

Refer to Figure 5-24. In this example, the authority for Dr. Snow is checked for the Cardiology service:

Figure 5-24: Determine Users' Update Authority Example

<!-- image -->

### Determine if User is Notification Recipient (UN)

Sometimes it is necessary to quickly check a user’s notification status for a service. The Determine if User is Notification Recipient option of the Consults Management menu accomplishes this.

Refer to Figure 5-25: In the following example CPRSPROVIDER,ONE notification status is checked for the Podiatry Clinic.

Figure 5-25: Determine if User is Notification Recipient Example

<!-- image -->

### Determine Notification Recipients for a Service (NR)

Occasionally it is necessary to see the entire list of notification recipients for a service. The Determine Notification Recipients for a Service option of the Consults Management menu performs the function.

Refer to Figure 5-26. In the following example, notification recipients are listed for the Medicine service:

Figure 5-26: Determine Notification Recipients for a Service Example

<!-- image -->

### Test Default Reason for Request (TD)

The Test Default Reason for Request option of the Consults Management menu is provided so that the boilerplate entered in the default reason for request can be tested. It is important to test this boilerplate, especially if it contains TIU objects (TIU objects are contained in vertical bars as such: |PATIENT NAME|.)

Refer to Table 5-3. TIU can vary from site to site. There are only a certain number of objects that are common to all sites—these are the Supported Objects. The following table contains a list of these objects.

Table 5-3: Supported Objects

| Object Name                   | Object Name          |
|-------------------------------|----------------------|
| ACTIVE MEDICATIONS            | PATIENT HEIGHT       |
| ACTIVE MEDICATIONS            | PATIENT NAME         |
| ACTIVE MEDS COMBINED          | PATIENT RACE         |
| ALLERGIES/ADR                 | PATIENT RELIGION     |
| BLOOD PRESSURE                | PATIENT SEX          |
| CURRENT ADMISSION             | PATIENT SSN          |
| DETAILED ACTIVE MEDS          | PATIENT WEIGHT       |
| DETAILED RECENT MEDS          | PULSE                |
| NOW                           | RECENT MEDICATIONS   |
| PAIN                          | RECENT MEDS COMBINED |
| PATIENT AGE                   | RESPIRATION          |
| PATIENT DATE OF BIRTH         | TEMPERATURE          |
| PATIENT DATE OF DEATH+ Status | TODAY'S DATE         |

Further information about objects can be obtained at the following VA intranet address: **REDACTED** .

Refer to Figure 5-27. In the following example, we first use the SS option to enter a default reason for request as such.

Figure 5-27: Test Default Reason for Request – SS Option

<!-- image -->

Next, use the TD option to check this for a specific patient. Refer to Figure 5-28.

Figure 5-28: Test Default Reason for Request – TD Option

<!-- image -->

### List Consult Service Hierarchy (LH)

This option of the Consults Management menu gives a complete list of the Consult Service Hierarchy as it currently exists. All services, including disabled ones, are listed with their current status. At the end of the hierarchy listing, it will show any services that are not part of the hierarchy.

Refer to Figure 5-29. In this example we start to list the service hierarchy from our test account on the computer screen:

Figure 5-29: List Consult Service Hierarchy

<!-- image -->

### Copy Prosthetics Services (CP)

The Copy Prosthetics Services option of the Consult Management menu is provided to assist you in configuring the prosthetics services at your medical center. . . .

The four (4) nationally exported services for Prosthetics include:

- PROSTHETICS REQUEST
- EYEGLASS REQUEST
- CONTACT LENS REQUEST
- HOME OXYGEN REQUEST

The basis of the interface between Consult/Request Tracking and Prosthetics is the name of the Consult service being requested. When a request for a consult is ordered, if the name of the service requested is one of the nationally exported services, the order will be filed in the Prosthetics package as well as Consult/Request Tracking. Since the name of the service is critical to the stability of the interface, the name of each of the above services will not be editable.

Each of the services have several other fields defined based on requirements of the interface. The fields that are restricted are:

- (#.01) NAME
- (#1.	01) PROVISIONAL DX PROMPT
- (#1.	02) PROVISIONAL DX INPUT
- (#124) DEFAULT REASON FOR REQUEST

When a request is copied, all these fields remain intact so that a request to that service is processed by the Prosthetics Package.

Refer to Figure 5-30. In the following example, the Copy Prosthetics action is used to create an Eyeglass Request service with the location name “Provo” appended to it. To be useful, the following additional actions should be taken:

1. Use the Setup Service (SS) action to place the service in the hierarchy.
2. Use the Setup Service (SS) action to activate the service.

Figure 5-30: Copy Prosthetics Services Example

<!-- image -->

### Consult Closure Tool (CCT)

The Consult Closure Tool provides options to identify consult requests that are incorrectly left in Pending status and efficiently closes out those consults. Search parameters can be configured in the tool, providing a list that allows you to close out consults by attaching a relevant note within the tool. There are also options to export the search results from the tool to a printable format and update a team list in CPRS.

The VistA Consult Closure tool consists of three components:

- Edit Configuration: Enables the user to configure the tool to identify pending consults based on search parameters, including clinics, orders, consult services, and procedures. The user also selects relevant note titles to use in closing pending consults. One or more valid configurations must be created prior to using the Run Configuration option.
- Inquire Configuration: Enables the user to print and view the configuration to ensure that it is set up properly.
- Run Configuration: Enables the user to select eligible note titles to close an open consult, perform the closure action, and/or create team lists that are viewable in CPRS.

The Consult Closure Tool is located in the GMRC MGR menu. This menu is normally allocated to IRMS/ADPAC personnel.

1. Navigate to the GMRC MGR menu option.
2. Type “CCT” to open the Menu for Closure Tools.

The following options appear:

- EDT    Consult Closure Tool Edit Configuration
- NQ    Consult Closure Tool Inquire Configuration
- RUN    Consult Closure Tool Run Configuration

#### Edit Configuration Component

The first step is to set up the configuration(s) using the Consult Closure Tool Edit Configuration menu option.

The key points when setting up a Consult Closure configuration include:

- The Config Name is free text. It is strongly suggested that simple names be used for the configurations and that they closely match existing consult service naming conventions.
- Configurations may contain Clinical Procedure requests, as well as specific consult orderable items, in addition to standard consult services. For example, one configuration for PULMLAB might encompass Pulmonary Function Test Request Consults, CP Pulmonary Function Test Procedure Requests, and specific orderable items for Pulmonary Sleep Studies.
- In order to view the team lists that can be generated out of this tool in CPRS, team lists must be created in VistA prior to using this tool. It is strongly suggested that a naming convention be established prior to creating the first configuration. For example, begin the team list name with "CONSULT\_REPORT\_" with the specific configuration name following. In this way, all of the team 's patient lists created within this tool are in sequence when browsed for on the CPRS Patient Selection screen in the Patient List pane.
- In the Configuration Editor screen, each of the four “Consults –“ fields are optional, but at least one of the four must be filled in to run the configuration. All four of the options allow for multiple selections. The search operates as a Boolean “AND” search for the entries into these fields. Therefore, each additional entry narrows your search because a consult request must meet all of the entries.

**Note:** Wildcard selection (ABC*) or exclusion (-ABC*) can be used in the editor in all of the entry fields. For example, all note titles beginning with ABC would be selected by entering ABC*.  To exclude all note titles beginning with ABC, enter –ABC*.

The key components of the editor are shown in Figure 5-31, below.

Figure 5-31: Edit Configuration Components Example .

<!-- image -->

To create or edit a Consult Closure configuration:

1. In the GMRC MGR menu, type "CCT" and then press Enter to open the Menu for Closure Tools.
2. Type "EDT" and then press Enter.
3. At the initial Consult Closure Tool Edit Configuration prompt, enter the new or existing configuration name. For a new configuration, type “Yes” when asked if you want to add this as a new consult configuration.
4. Press Enter. The Configuration Editor screen opens with the **Config Name** field highlighted and editable.
5. In the **Days Cons -&gt; Apt** field, enter the maximum number of days between the date of the consult entry and the clinic appointment. The tool will search for pending consults that fall within this time period. A shorter interval will make the tool run faster.
6. In the **CPRS Team** field, enter the name of the CPRS team that will be populated when this configuration is run. The team must already exist.
7. In the **Days Appt -&gt; Note** field, enter the maximum number of days between the clinic appointment date and the date of the eligible note that can be associated with the consult in the Run Configuration option.
8. In the Inactive field, enter NO (the default option) to make this configuration active. If a configuration is marked inactive, it is not selectable when running the Consult Closure Tool. It is still selectable in the Edit and Inquire options.
9. (optional) In the **Consults - Service** field, enter the name(s) of the consult service(s) to be used as search parameters.
10. (optional) In the **Consults - Procedure** field, enter the Procedure(s) to be used as search parameters. The Consults-Procedure field is for Medicine package procedure requests that do not use the Clinical Procedure (CP) interface.
11. (optional) In the **Consults – Order Item** field, enter specific orderable item(s) to be used as search parameters.
12. (optional) In the Consults – Clinical Procedure field, enter the Clinical Procedure(s) to be used as search parameters.
13. In the **Clinics** field, enter the Clinics to be used as search parameters. In lieu of entering individual clinics, you can enter the relevant **Stop Code** (s) to capture all associated clinics if they have already been correctly mapped in VistA. Adding more clinics broadens your search (operating as a Boolean "OR"), as the patient only has to be associated with one of them for their consult request to be returned when running the configuration.
14. In the **Note Titles** field, enter all eligible note titles to be associated with pending consults during Run Configuration. Define an appropriately comprehensive set of note titles, but be aware that an overly broad list might result in a higher likelihood of incorrect association with a pending consult.  This step is key as it allows non-consult class TIU documents that have been completed subsequent to a consult request to be associated with the consult, thus converting that pending consult’s status to Completed.
15. Press &lt;PF1&gt;E to save and exit. This returns you to the CCT menu. For a complete list of help options, press &lt;PF1&gt;H.

If the configuration is incomplete, you are notified when saving the configuration. Once the search configuration is completed, you are able to run a report using the Run Configuration option.

### Inquire Configuration Component

Once a configuration is created, it can be viewed and printed using the Consult Closure Tool Inquire Configuration menu option. This option is useful for verifying that the configuration is set up properly. At the Menu for Closure Tools, type "INQ" to view the configuration information.

### Run Configuration Component

Use the Consult Closure Tool Run Configuration menu option to implement the search for pending consults. When you are done using the Run Configuration, press &lt;PF1&gt;E to return to the CCT menu. Refer to Figure 5-32.

Figure 5-32: Run Configuration Component

<!-- image -->

#### Searching for Patient Consults / Appointments / Notes

To run a configuration:

1. In the GMRC MGR menu, type "CCT" and then press Enter to open the Menu for Closure Tools.
2. On the CCT menu screen, type “RUN” and then press Enter.
3. At the “Select CONSULT CONFIGURATION:” prompt, enter the name of the configuration to be run and then press Enter. This prompt defaults to your last selection, allowing you to just press Enter to access the last run configuration.
4. At the “Select date range:” prompt, select a consult request date range. Type the first letter of the desired range (e.g., "M" for monthly). The default range is “U” for User Selectable. Note: The larger the selected date range, the longer the Consult Closure Tool takes to run.
5. If you selected User Selectable, enter the desired date range at the “Beginning date:” and “Ending date:” prompts. The default dates are the beginning and ending day of the previous month.
6. At the “Select APPOINTMENT STATUS:” prompt, choose consult requests for which the patients have been seen or not seen in a clinic (the clinic list or stop code was delineated in the Configuration Editor). The default option is “Seen in clinic.”
7. At the “Select NOTE STATUS:” prompt, choose consult requests that have an eligible note or no eligible note. The default option is “Has a note.” This is the standard selection for completing consults with an encounter for which a note has been written. Most commonly, this involves a non-consult class note title being selected for the care documentation.

If you selected “Has a note,” then the “Interactive consult update:” prompt displays. The default response is Yes. Select Yes to interactively view the pending consults and the notes specified in the configuration, and optionally complete each consult by selecting a note to associate with it. More information is provided in the Closing Out Consults section below. Select No to print a report of the pending consults and notes and/or update the CPRS team list associated with the selected configuration. The default selection when selecting No is to both print and update the CPRS team list.

If "Does not have a note" is selected, you have the option to print a report of the pending consults and notes and/or update the CPRS team list associated with the selected configuration.

#### Closing Out Consults

If you selected Yes at the “Interactive consult update:” prompt while running the configuration, then you can use the Closure Tool to review and close out pending consults. The tool will search for patient consults, appointments, and notes. This might take some time (possibly up to 20

minutes) depending on the search criteria specified in the configuration and the date range. When the search is complete, the number of patients, consults, and notes is displayed.

The Consult Closure Tool has identified the following meeting your selected criteria:

- Patients:	6
- Consults: 	6
- Notes:		9

Press RETURN to continue.

Press Enter to see the first patient’s Consult Narrative. The patients’ Consult Narrative screens appear in alphabetical order by patient last name:

Refer to Figure 5-33

Figure 5-33: Close-Out Example

<!-- image -->

Patient and consult information is displayed first, followed by the consult and/or notes associated with the patient. You can scroll through the text by using the arrow and page up/down keys.

The Consult Narrative appears first for each patient. To toggle to the eligible notes on the BROWSE SWITCH MANAGER, select Num-Lock/S or &lt;PF1&gt;S. This opens the BROWSE SWITCH MANAGER screen, where you can view the notes available to close out the consult.

Refer to Figure 5-34.

Figure 5-34: Browse Switch Managers Screen Example

<!-- image -->

The BROWSE SWITCH MANAGER screen displays the eligible notes selected in the Configuration Editor. Selecting a note displays the contents of the note. When viewing the selected note, press &lt;PF1&gt;S to return to the list of notes on the BROWSE SWITCH MANAGER screen. After you have reviewed the consult and the identified notes and are ready to close the consult or move on to the next patient, press Num-Lock/E or &lt;PF1&gt;E to exit the current screen. This opens the Consult closure screen.

**Note:** The notes on the BROWSE SWITCH MANAGER screen are displayed in reverse chronological order, grouped by note title. If there are multiple available and relevant note titles for a given patient within each of the note title groups, then the oldest note appears at the bottom. However, the note at the bottom of the list is only the oldest for that note title group and might not be the oldest note of all note titles (that is, closest in time to the date of the pending consult itself) that are available for that patient.

Consult closure for patient: CPRSPatient,One 09/25/1933
MEDICAL SERVICE OTHER (p) 11/12/2010

Select the note to close the consult

**0** - Do not close the consult

**1** - Note 01: 10-10ED EMERGENCY DEPARTMENT NOTE

**2** - Redisplay the consult/progress note(s)

**^** - Exit the Consult Closure Tool

Select NOTE TO CLOSE CONSULT: 2//.

In the Consult closure screen (pictured above), you can select from the following options: a) Do not close the consult, b) Close the consult with one of the identified notes, c) Return to the consult/note display screen for further review, or d) Exit the Consult Closure Tool. If you select option a), then no action is taken on the consult and the tool automatically displays the next consult. If you select option b), then the tool closes the consult with the selected note and automatically displays the next patient’s Consult Narrative. This process continues until all consults are processed or you exit the Consult Closure Tool.

#### Printing/Updating the CPRS Team List

If you selected No at the "Interactive consult update" prompt in Run Configuration, then you can print a consult/note report list and/or update the CPRS team list associated with the selected configuration. The default is to both print the report and update the team list.

Refer to Figure 5-35.

Figure 5-35: Printing/Updating the CPRS Team List Example

<!-- image -->

For the Print option, the report may be printed in a human readable format (the default No option) or a carat (“^”) delimited format for import into another program (such as an Excel spreadsheet). The report requires a 132-column output device.

For the Team update option, the selected configuration updates the CPRS patient team list associated with it. When run, any pre-existing patients on the list are removed and replaced with the newly-identified patients. The user running the Consult Closure Tool and the users associated with the team list will receive alerts when the team update has completed.

### Duplicate Sub-Service (DS)

The Duplicate Sub-Service option of the Consult Management menu is provided to assist you in debugging your service hierarchy. It displays services that are listed as a sub-service of more than one service. Having a service as a sub-service of more than one service has several undesirable effects. These include:

1. Reports that span more than one level of the hierarchy inaccurately report statistics.
2. Notification recipients may be inaccurately determined.

Refer to Figure 5-36.

Figure 5-36: Printing/Updating the CPRS Team List Example

<!-- image -->

### Define Fee Services (FS)

The Define Fee Services option of the Consult Management menu is provided to assist you in modifying the list of services defined as being fee basis services in the GMRC FEE SERVICES system parameter.

In the following example, we begin with an empty list of services. Refer to Figure 5-37.

Figure 5-37: Define Fee Services Option Example

<!-- image -->

Refer to Figure 5-38. Now, starting with a list of a few services, we delete a service.

Figure 5-38: Deleting a Service Example

<!-- image -->

Finally, we save our list and quit. Refer to Figure 5-39.

Figure 5-39: Save and Quit Example

<!-- image -->

**Note:** The list must be saved for changes to take effect. If the user quits without saving, he or she will be prompted to save changes before quitting.

### Inter-Facility Consults Reports

The Inter-Facility Consults reports are available on the Consult Tracking Reports menu [GMRC REPORTS] and the IFC Management Menu [GMRC IFC MGMT]. Currently four Inter-Facility Consults reports show up on this menu. Refer to Table 5-4.

Table 5-4: Inter-Facility Consults Report Descriptions

| Report Synonym   | Report Name                              | Option Name                      |
|------------------|------------------------------------------|----------------------------------|
| IFC              | IFC Requests                             | [GMRC IFC RPT CONSULTS]          |
| IP               | IFC Requests by Patient                  | [GMRC IFC RPT CONSULTS BY PT]    |
| PI               | Print IFC Requests                       | [GMRC IFC PRINT RPT NUMBERED]    |
| IR               | IFC Requests by Remote Ordering Provider | [GMRC IFC RPT CONSULTS BY REMPR] |
| EC               | IFC Possible Erroneous Comment Report    | [GMRC IFC ERR COMM RPT]          |

IFC Requests (IFC) provides detailed information regarding inter-facility consults. The Inter-Facility Consult Requests (PI) is the same report formatted for a printer.

The IFC Request by Patient (IP) is similar to option Consult Service Tracking, except only displays inter-facility consults as a requesting or consulting facility.

The IFC Requests by Remote Ordering Provider (IR) provides detailed information regarding inter-facility consults by remote ordering provider for consulting sites to utilize. The display is similar to the IFC/PI options.

### IFC Requests

This report provides such information as:

- Total Requests to Service
- Total Requests Scheduled to Service
- Total Requests Completed to Service
- Mean Days Completed to Service

This report provides information for both requesting and consulting facilities. In the following example depicted in Figure 5-40, we examine all Dental consults we originate as a requesting facility.

Figure 5-40: Dental Consults Report Example

<!-- image -->

There are additional fields that are not visible on an 80-column screen such as the screen in the example. They can be viewed by using the Shift to View Right action (&gt;). Using the Shift to View Left (&lt;) action restores the screen. If the report is for a consulting site, then the additional fields are: Routing Facility, Days Diff, and Red Date. If the report is for a requesting site, then the additional fields are Routing Facility and Days Diff.

There are five actions you can do besides the default actions (like Next Screen, Previous Screen, Quit, &gt;, &lt;, …). These include the following:

- **Change Service:** Change Service action allows you to re-display the report for a different service.
- **Number on/off:** Number on/off action changes the format of the report to include the consult number. To do this, it preserves the other columns but makes them narrower.
- **Description of Data:** Description of Data action gives a detailed description for applicable data columns.
- **Status:** Status action allows you to change which statuses are displayed in the report. In the following example the statuses displayed are changed from All Statuses to just the Pending, Active, and Scheduled consults.
- **Print List:** Displays the print list.

Refer to Figure 5-41.

Figure 5-41: Status Change Example

<!-- image -->

### Print IFC Requests

The Print IFC Requests (PI) is the same report as the IFC Requests (IFC) except that it formats the report so you can send it to a printer device.

Refer to Figure 5-42, which lists all active requests for the Dental service. Note only two consults are displayed.

Figure 5-42: Print IFC Requests Example

<!-- image -->

### IFC Requests by Patient

The IFC Requests by Patient (IP) report is the same as the Consult Service Tracking (CS) option, except that it only displays inter-facility consults. As such, once it has been invoked, all actions normally available to you in the Consult Service Tracking option are usable.

Refer to Figure 5-43.

Figure 5-43: IFC Requests by Patient Example

<!-- image -->

### IFC Requests by Remote Ordering Provider

If you need to determine the status of consults at your facility ordered from a certain provider at another facility, then you can use the IFC Requests by Remote Ordering Provider option.

When using this option, you must specify the name of the provider exactly at the prompt. If you enter a question mark, a screened list of ordering providers is displayed.

Refer to Figures 5-44 and 5-45. In this example we look at the Medicine consults from a provider at Boise:

Figure 5-44: Medical Consult Example

<!-- image -->

Figure 5-45: Medical Consult Example (continued)

<!-- image -->

There are three other fields that are not visible on an 80-column screen such as the screen in the example. They include Routing Facility, Days Diff, and Rec Date. They can be viewed by using the Shift to View Right action (&gt;). Using the Shift to View Left (&lt;) action restores the screen.

There are five actions you can do besides the default actions (like Next Screen, Previous Screen, Quit, &gt;, &lt;, …). These include the following:

- **Change Service:** Change Service action allows you to re-display the report for a different service.
- **Number on/off:** Number on/off action changes the format of the report to include the consult number. To do this, it preserves the other columns but makes them narrower.
- **Description of Data:** Description of Data action gives a detailed description for applicable data columns.
- **Status:** Status action allows you to change which statuses are displayed in the report. In the following example the statuses displayed are changed from All Statuses to just the Pending, Active, and Scheduled consults.
- **Print List:** Displays the print list.

### IFC Possible Erroneous Comment Report

The IFC Possible Erroneous Comment Report (EC) provides a list of patient files with erroneous verbiage on IFC referral comments. Refer to Figure 5-46, which depicts an example of a user running the report.

**Note:** A Help Desk ticket will be required to remove the “Erroneous Comment(s)”.

Figure 5-46: Running an IFC Possible Erroneous Comment Report

<!-- image -->

- **SCR** displays the report on screen. This option is designed for screen view and print.
- **CSV** displays the report on screen in a pipe-delimited format.

The user can press Return/Enter to accept the default date.

OR

The user can enter the desired beginning date.

- **Note** : The larger the selected time range the longer the report takes. It is not recommended to use large time ranges.
- **Note** : The total count found is at the top of the report and each instance found is numbered.

Refer to Figure 5-47.

Figure 5-47: IFC Possible Erroneous Comment Report Example

<!-- image -->

#### Viewing the Possible Erroneous Comment Report in Excel

To view the Possible Erroneous Comment Report in Excel:

1. The user must modify their terminal settings. Adjust the terminal settings to allow output to be as wide as possible (999 or max allowed characters).
2. Copy and paste the report into a text editor (word, notepad, etc...) or output the report to a log .txt file.
3. Combine all wrapped text lines into one field.
4. Save the file.
5. Open the file in Excel.
6. Select Delimited with Headers, and then click Next&gt;.
7. Select Other, enter | in the text field, and then click Next&gt;.
8. Locate the Data Preview box, select all text, and then click Finish.
9. Manipulate the columns for display/wrap as desired.

### ADMIN KEY Reports

A new GRMC Patch for “Admin Key Reporting” has been created to generate three (3) new GRMC Reports.

- GMRC RPT ADMIN RELEASE CONSULT
- GMRC RPT ADMIN REL CONS USER
- GMRC RPT ADMIN REL CONS GROUPR

The details for the Admin Key that has been created include the new Admin key for services that contain “-DS” or “-Admin” in the service name. A new VistA index has been created to capture this information. It is sorted by a FileMan date and then an internal Consult IEN.

An example of the GMRC RPT ADMIN RELEASE CONSULT report access is shown below:

### Unique Consult ID (UCID) Conversion

Patch GMRC*3.0*110 has a post-install routine that does the following:

1. Reads the Station ID, extracts the first three characters (STA3N), and then updates the GMRC UNIQUE CONSULT SITE ID with this STA3N.
2. Finds all consult records in file #123 (REQUEST/CONSULTATION) that have an existing UCID, starting with 01/01/2018 and going forward, and changes the first three characters of that UCID to the ID constructed in step 1 above.

### Unique Consult ID (UCID) Display

Patch GMRC*3.	0*110: When a user clicks on a Consult Order on the CPRS Orders tab, and right-clicks to show the Order Details, the display will now show the Unique Consult ID (UCID) which is in file #123 (REQUEST/CONSULTATION) in field #80 (UNIQUE CONSULT ID). The UCID is a tracking number used by Community Care.

### Interfacility Consults When Used with Cerner Converted Sites

The release of GMRC*3.0*154 adds three new components to the Interfacility Consults (IFC) system.

1. VDIF (Veterans Data Integration and Federation) integration
2. MPI Patient Registration
3. Cerner Mail Groups

### VDIF

When a facility has been “converted” to Cerner, it will be necessary for the Interfacility Consults (IFC) system to recognize that the HL7 message should no longer be routed to the VistA instance but should be routed to the VDIF (Veterans Data Integration and Federation) router. If the status of the treating facility is “converted”, the system will reference the Parameter GMRC IFC REGIONAL ROUTER file (#8989.5). This Parameter contains the Logical Link (GMRC IFC1 – GMRC IFC6) used to connect to one of the six VDIF (Veteran Data Integration and Federation) Regional Routers. The Logical Link will be substituted in the HL7 message in order to route the message to Cerner, rather than the VistA instance.

### MPI Patient Registration

Nonconverted VistA to Nonconverted VistA

If the patient is not registered at the treating facility, MPI will not return the patient’s identifier and the Proxy Add Patient API (part of MPIF*1.	0*73) will be initiated to add the patient to the facility. Once the patient is registered at the treating facility, a 201 error code is logged in the IFC Message Log (file #123.6).  The IFC background job will read this message and resend the consult order as long as the message is at least one hour old.

Nonconverted VistA to Converted VistA (Cerner)

When placing a new InterFacility Consult order, the Master Patient Index is queried to determine if the patient is registered at the treating facility, if the treating facility has been converted to Cerner, and if the patient is registered in the Cerner Millennium system.  If the patient is registered at the treating facility and the facility has been converted, MPI will return the patient’s identifier.  This will include the assigning authority, assigning facility, and the converted status of “C” for the facility (e.g.,“1234^PI^USVHA^668^C”).  If the patient is also registered in the Cerner Millennium system, MPI will return another patient identifier that contains the EDIPI with the assigning facility of 200CRNR (e.g., “109867654^PI^USVHA^200CRNR^A”).  If MPI does not return the two identifiers, the Proxy Add Patient API (part of MPIF*1.	0*73) will be initiated to add the patient to the treating facility and Cerner Millennium.  Once the patient is registered at the treating facility, a 201 error code is logged in the IFC Message Log (file #123.6).  The IFC background job will read this message and resend the consult order as long as the message is at least one hour old.

**NOTE:** There may be an instance where MPI fails to register the patient.  This will not generate a 201 negative acknowledgement and therefore will not send any notifications to the mail groups.  If the new consult order does not appear in Cerner within two hours, perform the following steps.

1. Check with MPI and retrigger the add
2. Replay the consult message from VDIF

### Cerner Mail Groups

A “converted” facility is not able to process HL7 application negative acknowledgement (NAK) in the same manner as a “nonconverted” facility.  Due to this technical limitation, four new mail groups (file #3.	8) have been created to notify subscribers of application negative acknowledgements.

- GMRC CRNR IFC ERRORS
- GMRC CRNR IFC CLIN ERRORS
- GMRC CRNR IFC TECH ERRORS
- GMRC TIER II CRNR IFC ERROR

Data validation of a HL7 message is performed at the receiving facility. During the validation process, the MSH-8 segment of the HL7 message is examined to determine the origin of the message.  If a HL7 message contains an MSH-8 segment of “CRNR”, the message originated from a “converted” facility. When the receiving facility fails to process the HL7 message, an application negative acknowledgement (NACK) is generated with a specific error code. NAKs generated by a “converted” facility HL7 message, initiate MailMan to notify one or more of the new mail groups listed above.

**Note:** Refer to Appendix E for list of mail group notifications based on error code.

Additional details can be found in the following documents: The Department of Veterans Affairs Electronic Health Record Modernization (EHRM) Interfacility Consults (IFC) Interface Control Document (ICD), and the Cerner Design Summary for Inter-Facility Consults. These two documents are stored on a site maintained by Cerner Corporation.

### GMRC*3.0*176

The release of GMRC*3.0*176 contains one modified routine, GMRCIACT, in the Interfacility Consults (IFC) system. The modification is as follows:

- When an Urgency of "Urgent" is picked in Cerner, ORC7.6 in the HL7 message contains an urgency code which is mapped to an entry in the PROTOCOL file (#101). When the field is equal to "S" meaning "STAT", this patch will change the urgency text to "NEXT AVAILABLE”.

## 6 Cancelled to Discontinued Consults

### Overview

A new patch has been created that has several components as follows:

- A new option, GMRC CHANGE STATUS X TO DC. This is not a user option; it is only present to facilitate the overnight job that converts consults from “Cancelled” to “Discontinued”.
- A new multi-valued parameter, CSLT CANCELLED TO DISCONTINUED, that contains three fields as follows:
    - Is the overnight cancelled to discontinued job active?
    - How many days back to start with?
    - How many days back to end with?
- A new index called “ASTATUS” on file #123 (REQUEST/CONSULTATION), field #40 (REQUEST PROCESSING ACTIVITY), sub-fields #.01 (DATE/TIME OF ACTION) and #1 (ACTIVITY).
- A new entry in file #19.2 (OPTION SCHEDULING), GMRC CHANGE STATUS X TO DC, which causes an overnight job to run which discontinues any consults that were cancelled within the day range specified in the second bullet in this list.
- A new menu option, GMRC CX TO DC PARAMETER EDIT, which allows a user to edit the parameter outlined in the second bullet in this list.

There are no new roll and scroll or GUI screens associated with this patch, but FileMan may be used as outlined below.

### Overnight Job

The GMRC CHANGE STATUS X TO DC overnight job is executed by TaskMan according to the schedule referred to in the OPTION SCHEDULING file as outlined in 4.	 Above. It uses the new index referred to in 3 above to find consults that were cancelled in the date range (T-“days back to start with”) to (T-“days back to end with”), this processing being in reverse chronological order. Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued. Note that the overnight job is disabled when the patch is installed – the Is the overnight cancelled to discontinued job active? Parameter is set to NO.

A temporary file is used to log any consults that have been discontinued. The temporary file is set to be purged after 60 days.

### Update of the New Index During Installation of Patch GMRC*3.0*113

The new ASTATUS index is created during the installation of the patch. During a post-install process, it is necessary to add to the index all existing consult records in file #123. In a production environment this could go into the millions. It is not advisable to do this in the foreground during the patch installation, so the job of doing this is transferred into the background using TaskMan.

The background job will pause periodically to avoid consuming system resources.  The pause interval is set to 50,000 and resumes processing after a pause of 1800 (30 minutes).

### Installation Background Job that Updates the Index

During the installation of the patch, a background job will be started to set up entries in the new ASTATUS index, and installation will complete within a few seconds. A message will be output as follows:

Post-install queued as task #nnnnnnnn where nnnnnnnn is the TaskMan job and will be something like this: 270120.

This job can be stopped if necessary, using the TaskMan User option. It can then be restarted by re-installing the patch. The job will the n continue where it left off.

### Editing the Entries in the New Parameter

Refer to Figure 6-1, which shows how the values in the new multi-valued parameter, CSLT CANCELLED TO DISCONTINUED, can be edited by the new function GMRC CX TO DC PARAMETER EDIT.

Figure 6-1: Editing Entries Example

<!-- image -->

**NOTE:** After installation of the patch or when the job is set to run with the parameter, “Is the overnight cancelled to discontinued job active?”, the “How many days back to start with” parameter should be set to nine (9).

## 7 Inter-Facility Consults Management Options

The Inter-Facility Consults Options [GMRC IFC MGMT] menu is part of the Consults Management [GMRC MGR] menu. Refer to Table 7-1, which lists the menu options available to the user.

Table 7-1: Inter-Facility Consults Management Menu Options

| Synonym   | Name                                       | Command                          |
|-----------|--------------------------------------------|----------------------------------|
| TI        | Test IFC implementation                    | [GMRC IFC TEST SETUP]            |
| LI        | List incomplete IFC transactions           | [GMRC IFC INC TRANS]             |
| IFC       | Inter-Facility Consult Requests            | [GMRC IFC RPT CONSULTS]          |
| TR        | IFC Transaction Report                     | [GMRC IFC TRANS]                 |
| LK        | Locate IFC by Remote Cslt #                | [GMRC IFC REMOTE NUMBER]         |
| BK        | Monitor IFC background job parameters      | [GMRC IFC BKG PARAM MON]         |
| EC        | IFC Possible Erroneous Comment Report      |                                  |
| IP        | Inter-facility Consult Requests By Patient | [GMRC IFC RPT CONSULTS BY PT]    |
| IR        | IFC Requests by Remote Ordering Provider   | [GMRC IFC RPT CONSULTS BY REMPR] |
| PI        | Print Inter-facility Consult Requests      | [GMRC IFC PRINT RPT NUMBERED]    |

Inter-Facility Consult Requests (IFC), Inter-Facility Consult Requests by Patient (IP), Print Inter-Facility Consult Requests (PI), and IFC Requests by Remote Ordering Provider (IR)  are covered under the Inter-Facility Consults Reports section above.

### Test IFC Implementation

Refer to Figure 7-1, which shows how to use the Test IFC Implementation option to check the setup of a procedure or consult service.

Figure 7-1: Checking Setup Example

<!-- image -->

The following are the five most common errors that may be indicated with this option:

- 301 – Service not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Service (SS) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.
- 401 – Procedure not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Procedure (PR) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.
- 501 – Error in procedure name. Could not find a matching procedure at the consulting facility. You probably need to verify the spelling and use the Setup Procedure (PR) option to make sure the IFC REMOTE PROCEDURE NAME is correct in your Procedure file (#123.3).
- 601 – Multiple services matched to procedure. At the consulting facility, the RELATED SERVICES multiple must only contain a single value.
- 701 – Error in Service name. Could not find a matching service at the consulting facility. You probably need to verify the spelling and use the Setup Service (SS) option to make sure the IFC REMOTE NAME is correct in your Request Services (#123.5).

**Note:** Any error occurring within the VistA HL7 messaging system is also indicated in this option.

### List Incomplete IFC Transactions

GMRC IFC INC TRANS is a tool for reviewing incomplete Inter-Facility Consult (IFC) Transactions. With this option you can retransmit an action that is not yet resolved.

This option can accept the following inputs when selecting a consult request:

- Consult Number
- Patient Name
- Service Name
- A question mark to see a screened list of consults with incomplete activities

Refer to Figures 7-2 and 7-3. The following screen capture error is inspected and a retransmit if performed.

Figure 7-2: List Incomplete IFC Transactions Example

<!-- image -->

Figure 7-3: List Incomplete IFC Transactions Example (continued)

<!-- image -->

### IFC Transaction Report

This option lists the current contents of the IFC Message Log (#123.6) for one or all consults. This log is used by the Inter-Facility Consults software to ensure transmission of Inter-Facility Consult requests. The IFC background job checks this log and takes appropriate action on requests that have not yet successfully completed.

Old transactions are discarded by the software. You can control this function by using the Edit Parameter Values [XPAR EDIT PARAMETER] option, set the GMRC RETAIN IFC ACTIVITY DAYS parameter to a number between 7 and 180. If this parameter is not set, completed transactions will be retained for 7 days. The higher the number set in this parameter the more disk space will be used by the IFC MESSAGE LOG file. See the section on Error Handling below for more complete details.

At the “Select Consult/Request Number:” prompt, you may enter any one of the following:

- ALL to list all entries.
- The consult number to list that single consult.
- The patient name to select a consult from the consults on file for that patient.
- The to or from service to select a consult from the consults to or from that service.
- The date of request to select a consult originated on that date.
- The CPRS status, such as PENDING or PARTIAL RESULTS, to select a consult with that status.
- The sending provider to select a consult originated by that provider.

Refer to Figures 7-4 and 7-5 on the following page, which list all entries in the IFC Transaction Log.

Figure 7-4: IFC Transaction Log

<!-- image -->

Figure 7-5: IFC Transaction Log (continued)

<!-- image -->

### Locate IFC by Remote Consult Number

This option is designed to assist consulting facilities with consult inquiries from requesting facilities. E.g., “Do you have the consult with Boise number 845?” All other reports are based on the local consult number. When a call is made from a requesting facility for information on the status of a consult, they are not likely to have the consulting facility’s number—only their own number for that consult. This option gets around that problem by keying on the original consult number.

Refer to Figure 7-6. In this example, a CAC at Salt Lake assists a Physician at Boise in looking up Boise consult number 845:

Figure 7-6: Locating IFC by Remote Consult Number

<!-- image -->

### Monitor IFC Background Job Parameters

This option lists the current state of parameters covering the IFC background jobs. It also gives an alternate method of changing these parameters. E.G., If the running of the IFC Background job should be delayed for any reason (e.g. to install a GMRC patch or system maintenance), it may be delayed by using the Edit background job start parameter action and setting the start time parameter to a date/time in the future.

Refer to Figure 7-7. In this example, we view the IFC background job parameters.

Figure 7-7: IFC background job parameters

<!-- image -->

### Notification Parameters

There are five (5) Consults notifications:

- #23:	CONSULT/REQUEST RESOLUTION
- #27
- :	NEW SERVICE CONSULT/REQUEST
- #30:	CONSULT/REQUEST CANCEL/HOLD
- #63:	CONSULT/REQUEST UPDATED
- #89:	PROSTHETICS CONSULT UPDATED

Any user who wants to receive these notifications must have the notifications enabled for themselves. To turn on these notifications, use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.

**Note:** Unless Consult notifications are set to mandatory, individual users may use the Enable/Disable My Notifications option of the Notifications Management Menu to individually disable the notifications they do not want to receive.

Also, the deletion parameter for these notifications is set to Individual Recipient. This means that when an individual reviews one of these notifications, the notification is deleted for only that individual. This parameter may be set to All Recipients, in which case a notification is deleted for all recipients when any one of them reviews it.

To change the deletion parameter for any of the Consults notifications, use the Set Deletion Parameters for Notifications option of the Notification Mgmt Menu.

### Consult Service Tracking

#### Functionality

The Consult Service Tracking (GMRC SERVICE TRACKING) option is a generic “User” option that:

- Provides a “by patient” lookup of consults and procedure requests which is similar to CPRS’s “by patient” lookup of orders.
- Provides a “by Service” lookup of consults and procedure requests. Users may select a service/specialty at any level in the hierarchy of services defined by IRMS/ADPAC personnel.

**Note:** The Consults “Select Service (SS)” action lumps all consult and procedure request orders under a Display Group called “CONSULT...” The only way for users to breakdown these orders by request service is to use the “Select Service (SS)” action provided by this option.

Displays a review screen of consults/requests in sequence by inverted “order released date/time” (most recent consults first).

Includes the Service’s “Last Activity” update and the updated CPRS status for each consult/request displayed.

Provides basic “Select Action:” prompt capabilities which parallel CPRS actions. Exactly which actions are displayed depends on the privileges accorded to the person using the system. Privileged actions such as Complete (CT), Cancel (DY), Discontinue (DC), Forward (FR), Receive (RC), Schedule (SC), Significant Findings (SF), and Make Addendum (MA) are not displayed if the user cannot perform them.

To determine whether a user can perform privileged actions or not, Consults checks the following fields from the Requests Services (#123.5) file:

- Service Individual to Notify—123.08
- Service Team(s) to Notify—123.08
- Update Users W/O Notifications—123.1
- Update Teams W/O Notifications—123.3
- Administrative update users—123.33
- Administrative update teams—123.34

### Text Integration Utilities (TIU) Setup

The Text Integration Utilities package is essential for completing consults under V. 3.	0. It gives you several benefits not previously available. Among them are the ability to use boilerplate for selected consult types and the ability to file results in the TIU data base.

In this section we first review the process of Consults resulting. Then we present two different document definition hierarchies that may be used for Consults results. Finally, we present the TIU options you need to set up the TIU part of Consults Resulting.

#### Consults Resulting Process

The diagram, Consults Resulting Process, shows the consults process with emphasis on the resulting phase. To complete a consult, three things must happen:

- An authorized user must select the complete action.
- The results must be entered or uploaded.
- The results must be signed (and, if appropriate, cosigned).

If TIU’s upload utility is used, the use of the complete action may be bypassed. TIU generates a notification permitting the responsible person to sign the results and complete the consult.

If the end-user is to enter the results, either the complete action prompts for results, or the results may be entered through TIU directly. If the results are entered through TIU, the user is prompted to link the TIU document with a consult request. In doing this, TIU lists consults that are available for resulting. The parameter GMRC CONSULT LIST DAYS controls how many days back TIU searches for qualifying consults. (The package default for this parameter is 365 days.)

Once these three things are accomplished, the consult is marked as complete and TIU files the results. Also, a chart copy of the completed consult may be printed.

Your site may choose to result consults by use of Progress Notes. In this case the resulting user sees essentially the same prompts, but the results entered are visible both as a consult result and in the Progress Notes system.

#### Recommended Document Hierarchies

You should have TIU already set up on your system and be familiar with the Text Integration Utilities (TIU) Implementation Guide.

We present here two document hierarchies found useful by hospitals in the VHA system. Strategy A creates Consults as an independent class under Clinical Documents. Strategy B creates Consults as a document class under Progress Notes.

#### Advantages of Strategy A

- Provides a CLEAR separation of Consults from Progress Notes and minimizes the number of choices for the end-user.
- Simple, with few concerns for maintainability (e.g., no question as to whether heritable methods and properties of Progress Notes were appropriately overridden, etc.).

#### Disadvantages of Strategy A

- Not necessarily consistent with the way providers have been documenting their Consult Results in the past. (i.e., if they have been using PN titles to "result" consults and referring to the notes on the SF 513's in the past, this will be a departure from that practice).
- Limits flexibility of access to the information. (i.e., if set-up this way, they may only access the data through Integrated Document Management options on the TIU-side, and through the Consults tab of the CPRS chart).

#### Advantages of Strategy B

- Consistent with the way many providers have been documenting their Consult Results in the past. (i.e., if they have been using PN titles to "result" consults, they may continue to do so, with the results showing up on both the 509 and SF 513).
- Enhances flexibility of access to the information. (i.e., if set-up this way, they may access the data through any option on the TIU side, as well as through EITHER the Consults or Progress Notes tabs of the CPRS chart).

#### Disadvantages of Strategy B

- Does NOT Provide a CLEAR separation of Consults from Progress Notes and may offer too many choices for the end-user.
- Complex, with some concerns for maintainability (e.g., if printing or filing appear incorrect, may result from heritable methods and properties of Progress Notes not being appropriately overridden, etc.).

You need to plan the set-up of the Document Definition Hierarchy in some detail, including the titles you want to use at your site, before proceeding with the TIU DEFINE CONSULTS option. The worksheet included in Appendix A of the Text Integration Utilities (TIU) Implementation Guide may prove useful in this process.

The option TIU DEFINE CONSULTS, exported with TIU*1*4, is used to select one or the other of these strategies and set them up at your hospital.

### TIU Setup Options

#### TIU Define Consults

This option is exported with TIU*1*4. Once you have decided which Document Definition strategy to use, run the TIU DEFINE CONSULTS option. This option must be run before Consults may be completed using TIU documents.

Refer to Figure 7-8. In the following example we elect Plan B from the discussion on the preceding pages.

Figure 7-8: Plan B Example

<!-- image -->

### Create Document Definitions

After TIU DEFINE CONSULTS has been run, you need to enter the rest of the TIU hierarchy. You should have planned this out in detail according to instructions given in the Text Integration Utility (TIU) Implementation Guide. The Create Document Definitions option permits you to enter this hierarchy.

Refer to Figures 7-9 to 7-13. In the following example, a document title CARDIOLOGY CONSULT is added to the TIU document hierarchy.

Figure 7-9: Creating Document Definitions

<!-- image -->

Figure 7-10: Creating Document Definitions (continued)

<!-- image -->

Figure 7-11: Creating Document Definitions (continued)

<!-- image -->

Figure 7-12: Creating Document Definitions (continued)

<!-- image -->

Figure 7-13: Creating Document Definitions (continued)

<!-- image -->

### TIU Maintenance

#### Correcting Misdirected Results

Occasionally, a consult result is linked to the wrong consult. If this is detected prior to signature, it is possible for the author of a consult result to re-direct the record to a different consult request by any of several methods:

1. Through the Link to Request action, when processing the alert for the unsigned Consult Result.
2. Through the Individual Patient Document option.
3. You may choose the Link action from the All My Unsigned Documents Option.
4. From the CPRS Chart.

There are examples of the above four methods in the Consult/Request Tracking User Manual.

Following signature, such corrections can only be made by those persons who are granted permission to do so under the Authorization/ Subscription Utility (ASU). Information on how to make this kind of correction is shown in Figures 7-14 and 7-15.

Figure 7-14: TIU Maintenance Example

<!-- image -->

Figure 7-15: TIU Maintenance Example (continued)

<!-- image -->

### Medicine Interface

The Procedures module of Consult/Request Tracking has been enhanced. The two major enhancements are:

1. A complete change to the method of creating and activating procedures for use in CPRS and Consult/Request Tracking is introduced including a new file to store the procedures data.
2. The ability to link results stored in the VistA Medicine package to a procedure request has been re-established.

#### Procedure Setup

**Warning:** The GMRC PROCEDURES (#123.3) file should NOT be edited via VA FileMan. The interface between CPRS and Consult/Request Tracking depends on the use of the Setup procedures [GMRC PROCEDURE SETUP] option.

Refer to Figure 7-16.

Figure 7-16: Procedure Setup Example

<!-- image -->

- **INTERNAL NAME** in an alternate name for the service. This name does not appear on printouts or displays but can be used to access the service through the Setup Services (SS) option, or with FileMan.
- **RELATED SERVICES:** The RELATED SERVICES field in the procedure setup indicates which services from the Consult hierarchy will receive and process procedures of this type. If more than one related service is entered in this field the ordering person will have to choose which service to direct the procedure to. The users that will be notified and the users allowed to update procedure requests of this type are determined by the receiving service.
- **TYPE OF PROCEDURE:** The TYPE OF PROCEDURE field in the procedure setup essentially turns on the interface to the Medicine package for this type of procedure. The field is a pointer to the PROCEDURE/SUBSPECIALTY (#697.2) file in the Medicine package. If this field is not set, no medicine procedure results may be linked to this type of procedure request.
- **PROVISIONAL DX PROMPT:** Used by CPRS to determine how to prompt for the provisional diagnosis when ordering this procedure. If this field is set to OPTIONAL, the user will be prompted for the provisional diagnosis but may bypass answering the prompt. If the field is set to SUPPRESS, the user will not be presented with the provisional diagnosis prompt. If set to REQUIRED, the user must answer the prompt to continue placing the order.
- **PROVISIONAL DX INPUT:** Determines the method that CPRS uses to prompt the user for input of the provisional diagnosis when ordering this procedure. If set to FREE TEXT, the user may type any text from 2-80 characters in length. If set to LEXICON, the user will be required to select a coded diagnosis from the Clinical Lexicon.
- **PREREQUISITE:** This word-processing field is utilized to communicate pre-requisite information to the ordering person prior to ordering this procedure. This field is presented to the ordering person upon selecting a procedure and allows them to abort the ordering at that time if they choose. TIU objects may be embedded within this field which are resolved for the current patient during ordering. Any TIU objects must be contained within vertical bars (e.g. |BLOOD PRESSURE| ).
- **DEFAULT REASON FOR REQUEST:** The default text used as the reason for request when ordering this procedure. This field allows a boilerplate of text to be imported into the reason for request when placing orders for this procedure. If the user places an order using a quick order having boilerplate text, that text supersedes any default text stored in this field. This field may contain any text including TIU objects. TIU Objects must be enclosed in vertical bars (e.g. |PATIENT NAME| ).
- **RESTRICT DEFAULT REASON EDIT:** If a DEFAULT REASON FOR REQUEST exists for this service this field effects the ordering person's ability to edit the default reason while placing an order. This variable can be set to UNRESTRICTED, NO EDITING, or ASK ON EDIT ONLY. If the third value, ASK ON EDIT ONLY, is used, the user is only allowed to edit the default reason if the order is edited before releasing to the service.
- **IFC ROUTING SITE:** This field contains the VA facility that will perform consults requested for this service. When a consult for this service is ordered, it will automatically be routed to the VA facility in this field.

- **IFC REMOTE NAME:** This field contains the name of the service that will be requested at the VAMC defined in the IFC ROUTING SITE field. Enter the name of the service exactly as it is named at the remote facility. If this name does not match the name of the service at the routing site, the request will fail to be filed at the remote site. This will delay or prohibit the performance and processing of this request.
- **IFC SENDING FACILITY:** This is a multiple containing the facilities from which your site may receive Inter-Facility Consults for this consult. As with all IFC fields, they must be an exact match.

#### Linking Med Results to Procedure Request

In the Consult Service Tracking option and in CPRS list manager Consults tab, medicine results can be associated with the procedure request by using the complete/update action. If the selected item is a procedure and is configured for medicine resulting, users will be given the option of attaching medicine procedure result and/or writing a TIU document. In the CPRS GUI, associating medicine procedure results will be done via a separate menu item on the Action Menu of the Consults tab

#### Removing Medicine Results from a Request

This action provides a mechanism to disassociate a medicine result from a request that was linked by mistake. The ability to take this action is controlled by membership in a USR USER CLASS. A new field was exported for the REQUEST SERVICES (#123.5). Field (#1.	06) RESULT MGMT USER CLASS is a pointer to the USR USER CLASS (#8930) file and the appropriate user class of individuals who may take this action should be listed here. It is recommended that the user class entered here be in line with the business rule involving the LINK action as it pertains to TIU documents.

The action to disassociate a medicine result is provided through an action on the Consult Service Tracking option or the Consults tab of CPRS list manager and CPRS GUI.

### Parameters

There are two parameters associated with the Consults package:

- GMRC CONSULT LIST DAYS
- GMRC FEE SERVICES.

#### GMRC CONSULT LIST DAYS

The GMRC CONSULT LIST DAYS parameter controls the number of days TIU searches for consults that can be associated with a TIU note.

When completing consults from the notes tab, after selecting a title, you are given a list of consults to which the note may be linked. This list is limited to consults entered in the last 365 days by default. The parameter “GMRC CONSULT LIST DAYS” allows sites to vary this value. The default parameter “PKG” is set to 365 days.

Refer to Figure 7-17. The following example shows setting this parameter for a division (in a multi-divisional medical center) to 180 days:

Figure 7-17: GMRC CONSULT LIST DAYS Example

<!-- image -->

#### GMRC FEE SERVICES

The GMRC FEE SERVICES parameter controls which services (from the REQUEST SERVICES (#123.5) file) are defined as fee basis services.

When a commercial-off-the-shelf (COTS) fee basis system, such as Fee Basis Claims System (FBCS) or Healthcare Claims Processing System (HCPS), accesses a list of consults, it will use this parameter to limit its search to consults with fee basis services.

The list of consult services is stored internally as a word-processing field consisting of the IENs for FEE Basis or NON –VA Care Consults stored in the REQUEST SERVICES (#123.5) file. This list can be modified using the Define Fee Services [GMRC FEE PARAM] option under the GMRC MGR menu.

**Note:** This parameter cannot be edited via the XPAR menu. It should only be edited using the Define Fee Services [GMRC FEE PARAM] option under the GMRC MGR menu.

## 8 Files

*** Request/Consultation (#123)**

This file contains consult and request orders originating primarily via the CPRS process. Once the order exists in this file, receiving service users perform update activities. An audit trail of the update activities is maintained in this file.

*** Request Action Types (#123.1)**

This file identifies the action types that may be used by a service to track activity related to a consult or request.

*** GMRC Procedures (#123.3)**

This file identifies procedures that may be ordered and processed in CPRS.

File 123.3 must NOT be edited via VA FileMan. The interface between CPRS and Consult/Request Tracking depends on the use of the Setup procedures [GMRC PROCEDURE SETUP] option.

*** Request Services (#123.5)**

This file permits Services and Specialties to be grouped in a hierarchy representing the site’s available services. This grouping capability may be used with Review screens to filter out consults to a service, sub service, specialty, or sub-specialty of consults/requests.

The main entry in this file is the “ALL SERVICES” entry. Other entries should be subordinate in the hierarchy.

The “ALL SERVICES” entry is used to display the hierarchy of the hospital services when the Clinician ordering the consult is prompted for “Select Service/Specialty:” to send the consult to.

*** IFC Message Log (#123.6)**

This is a log used by the Inter-Facility Consults software to ensure transmission of Inter-Facility Consult requests. The IFC background job checks this log and takes appropriate action on requests that have not yet successfully completed.

### File Globals

Refer to Table 8-1. The following is a listing of the files contained in the Consults package. Listed for each file are its file number, name, global location, and an indicator as to whether or not data comes with the file.

Table 8-1: File Globals

|   Synonym | Name                      | Global     | Data    |
|-----------|---------------------------|------------|---------|
|     123   | REQUEST/CONSULTATION FILE | ^GMR(123,  | NO      |
|     123.1 | REQUEST ACTION TYPES      | ^GMR(123.1 | YES     |
|     123.3 | GMRC PROCEDURES           | ^GMR(123.3 | YES     |
|     123.5 | REQUEST SERVICES          | ^GMR(123.5 | YES     |
|     123.6 | IFC MESSAGE LOG           | ^GMR(123.6 | NO      |

A file diagram of the above Consults package files and their relationship to other packages is depicted below in Figure 8-1.

Figure 8-1: Consult Request Tracking File Diagram

<!-- image -->

## 9 Exported Menus

There are five menus distributed with the Consults package. The GMRC MGR option is a composite of all Option file (#19

) entries distributed in the GMRC namespace. The GMRC REPORTS is a composite of reports distributed with Consults. The GMRC GENERAL SERVICE USER, and GMRC PARMACY USER contain the most frequently performed actions for their respective user types.

Table 9-1: GMRC MCG Menu

| Option Name                 | Display Text                                    |
|-----------------------------|-------------------------------------------------|
| GMRC REPORTS                | Consults Tracking Reports                       |
| GMRC SETUP REQUEST SERVICES | Set up Consults Services                        |
| GMRC SERVICE USER MGMT      | Service User Management                         |
| GMRC SERVICE TRACKING       | Consults Service Tracking                       |
| GMRC PHARMACY TPN CONSULTS  | Pharmacy TPN Consults                           |
| GMRC PRINT TEST PAGE        | Print Test Page                                 |
| MRCSTSU                     | Group Update of Consults Requests               |
| GMRC UPDATE AUTHORITY       | Determine Users' Update Authority               |
| GMRC USER NOTIFICATION      | Determine if User is Notification Recipient     |
| GMRC NOTIFICATION RECIPS    | Determine Notification Recipients for a Service |
| GMRC TEST DEFAULT REASON    | Test Default Reason for Request                 |
| GMRC LIST HIERARCHY         | List Consult Service Hierarchy                  |
| GMRC PROCEDURE SETUP        | Setup Procedures                                |
| GMRC CLONE PROSTHETICS      | Copy Prosthetics services                       |
| GMRC CONSULT CLOSURE TOOL   | Menu for Closure Tools                          |
| GMRC DUPLICATE SUB-SERVICE  | Duplicate Sub-Service                           |
| GMRC FEE PARAM              | Define Fee Services                             |
| GMRC IFC MGMT               | IFC Management Menu                             |
| GMRC FSC HCP MAIL GROUP     | Define FSC HCP Mail Group                       |

Table 9-2: GMRC REPORTS Menu

| Option Name                    | Display Text                                       |
|--------------------------------|----------------------------------------------------|
| GMRC COMPLETION STATISTICS     | Completion Time Statistics                         |
| GMRC RPT PENDING CONSULTS      | Service Consults Pending Resolution                |
| GMRC RPT COMPLETE CONSULTS     | Service Consults Completed                         |
| GMRC RPT COMPLETE/PENDING      | Service Consults Completed or Pending Resolution   |
| GMRC IFC RPT CONSULTS          | IFC Requests                                       |
| GMRC IFC RPT CONSULTS BY PT    | IFC Requests By Patient                            |
| GMRC IFC RPT CONSULTS BY REMPR | IFC Requests by Remote Ordering Provider           |
| GMRC RPT NUMBERED CONSULTS     | Service Consults with Consults #s                  |
| GMRC IFC PRINT RPT NUMBERED    | Print IFC Requests                                 |
| GMRC PRINT BY SEARCH           | Print Consults by Provider, Location, or Procedure |
| GMRC RPT PERF MONITOR          | Print Consult Performance Monitor Report           |
| GMRC PRINT RPT NUMBERED        | Print Service Consults by Status                   |
| GMRC RPT CONSULTS BY STATUS    | Service Consults By Status                         |
| GMRC PRINT COMPLETION STAT     | Print Completion Time Statistics Report            |

Table 9-3: GMRC GENERAL SERVICE USER Menu

| Option Name                | Display Text               |
|----------------------------|----------------------------|
| GMRC SERVICE TRACKING      | Consults Service Tracking  |
| GMRC RPT PENDING           | Service Consults Pending   |
| GMRC COMPLETION STATISTICS | Completion Time Statistics |

Table 9-4: GMRC PHARMACY USER Menu

| Option Name                | Display Text               |
|----------------------------|----------------------------|
| GMRC PHARMACY TPN CONSULTS | Pharmacy TPN Consults      |
| GMRC RPT PENDING           | Service Consults Pending   |
| GMRC COMPLETION STATISTICS | Completion Time Statistics |

Table 9-5: GMRC CONSULT CLOSURE TOOL Menu

| Option Name                 | Display Text                               |
|-----------------------------|--------------------------------------------|
| GMRC CONSULT CLOSE TOOL EDT | Consult Closure Tool Edit Configuration    |
| GMRC CONSULT CLOSE TOOL INQ | Consult Closure Tool Inquire Configuration |
| GMRC CONSULT CLOSE TOOL RUN | Consult Closure Tool Run Configuration     |

Table 9-6: GMRC IFC MGMT Menu

| Option Name                    | Display Text                             |
|--------------------------------|------------------------------------------|
| GMRC IFC TEST SETUP            | Test IFC implementation                  |
| GMRC IFC INC TRANS             | List incomplete IFC transactions         |
| GMRC IFC RPT CONSULTS          | IFC Requests                             |
| GMRC IFC TRANS                 | IFC Transaction Report                   |
| GMRC IFC REMOTE NUMBER         | Locate IFC by Remote Cslt #              |
| GMRC IFC BKG PARAM MON         | Monitor IFC background job parameters    |
| GMRC IFC RPT CONSULTS BY PT    | IFC Requests By Patient                  |
| GMRC IFC RPT CONSULTS BY REMPR | IFC Requests by Remote Ordering Provider |
| GMRC IFC PRINT RPT NUMBERED    | Print IFC Requests                       |

It should be noted the options GMRC PHARMACY TPN CONSULTS, and GMRC SERVICE TRACKING are options which utilize review screens and “Select Action:” capabilities similar to CPRS review screen protocol menus. These three options should be distributed to the appropriate users, based on the “Menu/Option Access	” recommendations found in the Package Security section of this manual.

In addition to the Option file (#19

) menu, the Protocol file (#101) has several protocol menus distributed in the GMRC namespace. These menus are not for distribution to users. These menus represent the set of responses permitted at specific prompts during Consults processing.

## 10 Cross-References

The Consults files contain the following cross-references:

Request/Consultation file (#123)

**AC^GMR(123, “AC”, OE/RR FILE NUMBER, DA)**

This cross-reference permits determination of the request entry in this file based on the ORIFN (pointer to File 100) from CPRS.

**AD^GMR(123, “AD”, Patient, Inverted Date of Request, DA)**

This is the primary cross-reference used by Consults to display consults/requests for a patient, with the most recent Date of Request first.

**AD1^GMR(123, “AD1”, Date of Request, DA)**

**AE^GMR(123, “AE”, To Service, CPRS Status, Inverted Date of Request, DA)**

This cross-reference is used to display consults/requests for a particular service and CPRS status, with the most recent Date of Request first.

**AE1^GMR(123, “AE1”, Date of Request, DA)**

**AE2^GMR(123, “AE2”, CPRS Status, DA)**

**AIFC^GMR(123,”AIFC”,ROUTING FACILITY,REMOTE CONSULT FILE ENTRY,DA)**

This cross-reference is used to prevent duplicate entries from being filed if a new inter-facility consult is sent multiple times.

**AG**

This cross reference contains entries of the REQUEST/CONSULTATION file that do not have an appointment scheduled. This is determined based on the content and order of the entries in the REQUEST PROCESSING ACTIVITY multiple field 40. This cross reference will be updated with any update to the ACTIVITY field under the REQUEST PROCESSING ACTIVITY multiple and that update will be determined based on all REQUEST PROCESSING ACTIVITY entries. This cross reference was added in GMRC*3.	0*83.

**AL^GMR(123,”AL”,PATIENT LOCATION,DA)**

**AP^GMR(123,”AP”,PROCEDURE/REQUEST TYPE,DA)**

**B^GMR(123, “B”, File Entry Date, DA)**

The “B” Cross-reference is the regular cross-reference for this file.

**C^GMR(123, “C”, TO Service, DA)**

The “C” cross-reference enables VA FileMan look-up of information based on the TO Service.

**D^GMR(123, “D”, CPRS Status, DA)**

The “D” cross-reference enables VA FileMan lookup of information based on the CPRS status.

**E^GMR(123, “E”, Date of Request, DA)**

The “E” cross-reference enables VA FileMan lookup of information based on the Date of Request.

**F^GMR(123, “F”, Patient, DA )**

The “F” cross-reference enables VA FileMan lookup of information based on the Patient Name.

**G^GMR(123,"G",sending provider,DA)**

The “G” cross-reference allows look-up of consults by sending provider.

**H^GMR(123,"H",requesting location,DA)**

The “H” cross-reference allows look-up of consults by the requesting location.

**R^GMR(123,”R”,associated result,DA)**

The “R” cross-reference allows look-up of consults based on the results associated with them.

Request Action Types file (#123.1)

**AC^GMR(123.1, “AC”, CPRS Status, DA)**

This cross-reference is used when the call to RESULT^GMRCR returns a CPRS status. This CPRS status is used to determine the action type to use to update activity tracking.

**B^GMR(123.1, “B”, Action Type, DA)**

The “B” cross-reference is the regular cross-reference for this file.

**C^GMRC(123.1, “C”, Related Action Protocol, DA)**

This cross-reference is used to associate the action type with the protocol selected from the “Select Action:” prompt. The action type internal number is then used to set the variable

GMRCA for audit trail processing.

GMRC PROCEDURES file (#123.3)

**AP^GMR(123.3,"AP",protocol number,DA)**

This cross-reference is utilized during the procedure conversion process and will be removed in a future enhancement.

**B^GMR(123.3,"B",procedure name,DA)**

The “B” cross-reference is the regular cross-reference for this file, permitting lookup by procedure name.

**C^GMR(123.3,"C",synonym,DA)**

The “C” cross-reference permits SYNONYMS to be used to look up the procedure by synonym.

**E^GMR(123.3,”E”,internal name,DA)**

Request Services file (#123.5)

**B^GMR(123.5, “B”, Service Name, DA)**

The “B” cross-reference is the regular cross-reference for this file, permitting lookup by Service Name.

**C^GMR(123.5, “C”, Related Treating Specialty, DA)**

The “C” cross-reference enables VA FileMan lookup of information, based on the RELATED TREATING SPECIALTY. (Note: This field exists but is not currently used by the package.)

**D^GMR(123.5, “D”, Synonym, DA)**

The “D” cross-reference permits SYNONYMS to be used to find the Service to send a consult/request to.

**E^GMR(123.5,”E”,internal name,DA)**

**AAT^GMR(123.5, ADMINISTRATIVE UPDATE TEAM,DA)**

This cross-reference is used to locate and delete pointers to the  OE/RR LIST (#100.21) file that have been deleted.

**AC1^GMR(123.5, SERVICE NAME, DA)**

This cross-reference is what helps maintain the alphabetical look-up of services.

**ANT^GMR(123.5, TEAM TO NOTIFIY, DA)**

The "ANT" cross reference is used for deletion of pointer values when an entry is deleted from the OE/RR LIST (#100.21) file.

**APC^GMR(123.5, SUB-SERVICE/SPECIALTY, DA)**

This cross-reference is used to find the parents of a given service. This helps identify AC cross-references that need to be updated when the .01 name changes and helps manage forwarding to services.

**APR^GMR(123.5, PROCEDURE TYPE, DA)**

This cross reference is used to find all services which process a procedure type.

**AST^GMRC(123.5, SERVICE TEAM TO NOTIFY, DA)**

The "AST" cross reference is used for deletion of pointer values when  an entry is deleted from the OE/RR LIST (#100.21) file.

**AUT^GMR(123.5, UPDATE TEAMS W/O NOTIFICATIONS, DA)**

This cross-reference is used to locate and delete pointers to the OE/RR LIST (#100.21) file that have been deleted.

**IFC MESSAGE LOG (#123.6)**

**AC	^GMR(123.6,”AC”,CONSULT/REQUEST #,ACTIVITY #,INCOMPLETE,DA)**

This cross-reference is used by the IFC background job to manage incomplete entries.

**AI^GMR(123.6, INCOMPLETE, DA)**

The “AI” cross-reference is used to locate IFC consults that have not been processed successfully.

**AM^GMR(123.6, MESSAGE #, DA)**

The “AM” cross-reference is used to locate the HL7 message number.

**B^GMR(123.6, DATE/TIME OF ENTRY, DA)**

The “B” cross-reference if the regular cross-reference for this file, permitting lookup by

DATE/TIME of Entry.

**C^GMR(123.6,”C”,CONSULT/REQUEST #,ACTIVITY #,DA)**

This cross-reference is used to look up IFC MESSAGE LOG entries by consult number.

## 11 Archiving and Purging

No archiving or purging utilities are provided in this version for Consults distributed files.

## 12 External Relations

The Consults package is dependent upon other VA software to function correctly. Refer to Table 12-1.

Table 12-1: External Relations – Other VA Software

| Package    | Version   | Notes                                           |
|------------|-----------|-------------------------------------------------|
| VA FileMan | 21        |                                                 |
| OE/RR      | 3.	0           |                                                 |
| KERNEL     | 8.	0 (+ Patches)           | “Select Action:”prompts, and Alert capabilities |
| PIMS       | 5.	3           | Calls to VADPT                                  |

### Private DBIA Agreements

Refer to Table 12-2.

Table 12-2: External Relations – Other VA Software

|   DEA Number | Custodial Package   |   DBA Number | Custodial Package   |
|--------------|---------------------|--------------|---------------------|
|          147 | Medicine            |          868 | OE/RR               |
|          165 | OE/RR               |          869 | OE/RR               |
|          167 | Kernel              |          870 | OE/RR               |
|          169 | Kernel              |          871 | OE/RR               |
|          181 | OE/RR               |          872 | OE/RR               |
|          510 | VA FileMan          |          873 | OE/RR               |
|          615 | Medicine            |          875 | OE/RR               |
|          616 | Medicine            |         2038 | OE/RR               |
|          627 | OE/RR               |         2638 | OE/RR               |
|          628 | OE/RR               |         2290 | OE/RR               |
|          629 | OE/RR               |         2699 | TIU                 |
|          630 | OE/RR               |         2700 | OE/RR               |
|          631 | OE/RR               |         2713 | OE/RR               |
|          632 | Kernel              |         2761 | OE/RR               |
|          635 | OE/RR               |         2764 | OE/RR               |
|          636 | OE/RR               |         2849 | OE/RR               |
|          637 | OE/RR               |         3042 | MEDICINE            |
|          638 | OE/RR               |         3138 | CLINICAL PROC       |
|          639 | OE/RR               |         3168 | OE/RR               |
|          640 | OE/RR               |         3171 | OE/RR               |
|          861 | OE/RR               |         6184 | GMRC                |
|          862 | OE/RR               |              |                     |
|          863 | OE/RR               |              |                     |
|          864 | OE/RR               |              |                     |
|          865 | OE/RR               |              |                     |
|          866 | OE/RR               |              |                     |
|          867 | OE/RR               |              |                     |

## 13 Internal Relations

All options are independently evocable.

### Package-Wide Variables

There are no package-wide variables exported with this package that require SACC exemption.

## 14 Package Interface

### HL7 Fields

Refer to Table 14-1, which lists HL7 fields used in transactions between OE/RR v.3.0 and the Consult package. Not every field will be used in every message.

Table 14-1: Private DBIA Agreements

| **SEG**   |   **SEQ** | **Field Name**                                                                                                                                         | **Example**                                                                                                                          | **HL7 Type**       |
|-----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| MSH       |         1 | Field Separator                                                                                                                                        | &#124;                                                                                                                               | string             |
|           |         2 | Encoding Characters                                                                                                                                    | ^~\&                                                                                                                                 | string             |
|           |         3 | Sending Application                                                                                                                                    | ORDER ENTRY                                                                                                                          | string             |
|           |         4 | Sending Facility                                                                                                                                       | 660                                                                                                                                  | string             |
|           |         9 | Message Type                                                                                                                                           | ORM                                                                                                                                  | ID                 |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| RF1       |         1 | Referral Status                                                                                                                                        | IP^ADDED COMMENT                                                                                                                     | string             |
|           |         2 | Referral Priority                                                                                                                                      | ROUTINE                                                                                                                              | string             |
|           |         3 | Referral Type                                                                                                                                          | 553^NON-VA COLONOSCOPY^^32563^NON-VA COLONOSCOPY v6.2                                                                                | coded element      |
|           |         5 | Referral Category                                                                                                                                      | O                                                                                                                                    | table 284          |
|           |         6 | Originating Referral Identifier                                                                                                                        | 486410                                                                                                                               | string             |
|           |         7 | Effective Date                                                                                                                                         | 201403111904-0400                                                                                                                    | timestamp          |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| PRD       |         1 | Provider Role                                                                                                                                          | RP                                                                                                                                   | table 286          |
|           |         2 | Provider Name                                                                                                                                          | CPRSPROVIDER^THREE^^^^^^^10000000046                                                                                                 | composite ID       |
|           |         3 | Provider Address                                                                                                                                       | 1 STREET ADDRESS^^CITY^ST^00011                                                                                                      | string             |
|           |         5 | Provider Communication Information                                                                                                                     | ^^^CPRS3@VA.GOV^^555^555-5555                                                                                                        | string             |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| IN1       |           | 1                                                                                                                                                      | SetIDIN1                                                                                                                             |                    |
|           |         2 | InsurancePlanID                                                                                                                                        |                                                                                                                                      | Coded element      |
|           |         3 | InsuranceCompanyID                                                                                                                                     |                                                                                                                                      | ID                 |
|           |         4 | InsuranceCompanyName                                                                                                                                   |                                                                                                                                      | string             |
|           |         5 | InsuranceCompanyAddress                                                                                                                                |                                                                                                                                      | address            |
|           |         6 | InsuranceCoContactPerson                                                                                                                               |                                                                                                                                      | string             |
|           |         7 | InsuranceCoPhoneNumber                                                                                                                                 |                                                                                                                                      | string             |
|           |         8 | GroupNumber                                                                                                                                            |                                                                                                                                      | string             |
|           |         9 | GroupName                                                                                                                                              |                                                                                                                                      | string             |
|           |        10 | InsuredsGroupEmpID                                                                                                                                     |                                                                                                                                      | string             |
|           |        11 | InsuredsGroupEmpName                                                                                                                                   |                                                                                                                                      | string             |
|           |        12 | PlanEffectiveDate                                                                                                                                      |                                                                                                                                      | date               |
|           |        13 | PlanExpirationDate                                                                                                                                     |                                                                                                                                      | date               |
|           |        14 | AuthorizationInformation                                                                                                                               |                                                                                                                                      | string             |
|           |        15 | PlanType                                                                                                                                               |                                                                                                                                      | string             |
|           |        16 | NameOfInsured                                                                                                                                          |                                                                                                                                      | string             |
|           |        17 | InsuredsRelationshipToPatien                                                                                                                           |                                                                                                                                      | string             |
|           |        18 | InsuredsDateOfBirth                                                                                                                                    |                                                                                                                                      | date               |
|           |        19 | InsuredsAddress                                                                                                                                        |                                                                                                                                      | address            |
|           |        20 | AssignmentOfBenefits                                                                                                                                   |                                                                                                                                      | string             |
|           |        21 | CoordinationOfBenefits                                                                                                                                 |                                                                                                                                      | string             |
|           |        22 | CoordOfBenPriority                                                                                                                                     |                                                                                                                                      | string             |
|           |        23 | NoticeOfAdmissionFlag                                                                                                                                  |                                                                                                                                      | string             |
|           |        24 | NoticeOfAdmissionDate                                                                                                                                  |                                                                                                                                      | date               |
|           |        25 | ReportOfEligibilityFlag                                                                                                                                |                                                                                                                                      | string             |
|           |        26 | ReportOfEligibilityDate                                                                                                                                |                                                                                                                                      | date               |
|           |        27 | ReleaseInformationCode                                                                                                                                 |                                                                                                                                      | string             |
|           |        28 | PreAdmitCertPAC                                                                                                                                        |                                                                                                                                      | string             |
|           |        29 | VerificationDateTime                                                                                                                                   |                                                                                                                                      | date               |
|           |        30 | VerificationBy                                                                                                                                         |                                                                                                                                      | string             |
|           |        31 | TypeOfAgreementCode                                                                                                                                    |                                                                                                                                      | string             |
|           |        32 | BillingStatus                                                                                                                                          |                                                                                                                                      | string             |
|           |        33 | LifetimeReserveDays                                                                                                                                    |                                                                                                                                      | number             |
|           |        34 | DelayBeforeLRDay                                                                                                                                       |                                                                                                                                      | number             |
|           |        35 | CompanyPlanCode                                                                                                                                        |                                                                                                                                      | string             |
|           |        36 | PolicyNumber                                                                                                                                           |                                                                                                                                      | string             |
|           |        37 | PolicyDeductible                                                                                                                                       |                                                                                                                                      | number             |
|           |        38 | PolicyLimitAmount                                                                                                                                      |                                                                                                                                      | number             |
|           |        39 | PolicyLimitDays                                                                                                                                        |                                                                                                                                      | number             |
|           |        40 | RoomRateSemiPrivate                                                                                                                                    |                                                                                                                                      | number             |
|           |        41 | RoomRatePrivate                                                                                                                                        |                                                                                                                                      | number             |
|           |        42 | InsuredsEmploymentStatus                                                                                                                               |                                                                                                                                      | string             |
|           |        43 | InsuredsAdministrativeSex                                                                                                                              |                                                                                                                                      | string             |
|           |        44 | InsuredsEmployersAddress                                                                                                                               |                                                                                                                                      | address            |
|           |        45 | VerificationStatus                                                                                                                                     |                                                                                                                                      | string             |
|           |        46 | PriorInsurancePlanID                                                                                                                                   |                                                                                                                                      | string             |
|           |        47 | CoverageType                                                                                                                                           |                                                                                                                                      | string             |
|           |        48 | Handicap                                                                                                                                               |                                                                                                                                      | string             |
|           |        49 | InsuredsIDNumber                                                                                                                                       |                                                                                                                                      | ID                 |
|           |        50 | SignatureCode                                                                                                                                          |                                                                                                                                      | string             |
|           |        51 | SignatureCodeDate                                                                                                                                      |                                                                                                                                      | date               |
|           |        52 | InsuredsBirthPlace                                                                                                                                     |                                                                                                                                      | string             |
|           |        53 | VIPIndicator                                                                                                                                           |                                                                                                                                      | string             |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| IN3       |           | 1                                                                                                                                                      | SetIDIN3                                                                                                                             |                    |
|           |         2 | CertificationNumber                                                                                                                                    |                                                                                                                                      | string             |
|           |         3 | CertifiedBy                                                                                                                                            |                                                                                                                                      | string             |
|           |         4 | CertificationRequired                                                                                                                                  |                                                                                                                                      | string             |
|           |         5 | Penalty                                                                                                                                                |                                                                                                                                      | string             |
|           |         6 | CertificationDateTime                                                                                                                                  |                                                                                                                                      | date               |
|           |         7 | CertificationModifyDateTime                                                                                                                            |                                                                                                                                      | date               |
|           |         8 | Operator                                                                                                                                               |                                                                                                                                      | string             |
|           |         9 | CertificationBeginDate                                                                                                                                 |                                                                                                                                      | date               |
|           |        10 | CertificationEndDate                                                                                                                                   |                                                                                                                                      | date               |
|           |        11 | Days                                                                                                                                                   |                                                                                                                                      | number             |
|           |        12 | NonConcurCodeDescription                                                                                                                               |                                                                                                                                      | string             |
|           |        13 | NonConcurEffectiveDateTime                                                                                                                             |                                                                                                                                      | date               |
|           |        14 | PhysicianReviewer                                                                                                                                      |                                                                                                                                      | string             |
|           |        15 | CertificationContact                                                                                                                                   |                                                                                                                                      | string             |
|           |        16 | CertificationContactPhoneNum                                                                                                                           |                                                                                                                                      | string             |
|           |        17 | AppealReason                                                                                                                                           |                                                                                                                                      | string             |
|           |        18 | CertificationAgency                                                                                                                                    |                                                                                                                                      | string             |
|           |        19 | CertificationAgencyPhoneNumb                                                                                                                           |                                                                                                                                      | string             |
|           |        20 | PreCertificationRequirement                                                                                                                            |                                                                                                                                      | string             |
|           |        21 | CaseManager                                                                                                                                            |                                                                                                                                      | string             |
|           |        22 | SecondOpinionDate                                                                                                                                      |                                                                                                                                      | date               |
|           |        23 | SecondOpinionStatus                                                                                                                                    |                                                                                                                                      | string             |
|           |        24 | SecondOpinionDocumentationRe                                                                                                                           |                                                                                                                                      | string             |
|           |        25 | SecondOpinionPhysician                                                                                                                                 |                                                                                                                                      | string             |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| PID       |         3 | Patient ID  ------------  Between VistA and Cerner, this field includes the ICN and the EDIPI                                                          | 5340747  -----------------------  Between VistA and Cerner: Ex: 123456789V9999999^^^ICN^VETID~98765431^^^EDIPI^EDIPI                 | composite ID       |
|           |         5 | Patient Name                                                                                                                                           | Doe,John H                                                                                                                           | patient name       |
|           |        18 | Patient Account Number (FIN)  -Populated for HL7 messages sent by VistA to Cerner                                                                      |                                                                                                                                      | string             |
|           |        19 | SSN Number – Patient                                                                                                                                   | 123456789                                                                                                                            | string             |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| DG1       |         3 | Diagnosis Code – DG1                                                                                                                                   | 784.0^Headache                                                                                                                       | coded element      |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| PV1       |         2 | Patient Class                                                                                                                                          | I                                                                                                                                    | table 4            |
|           |         3 | Patient Location                                                                                                                                       | 32^234-4                                                                                                                             | user table         |
|           |         7 | Attending Doctor                                                                                                                                       | 1234^DOE, JOHN M                                                                                                                     | composite ID       |
|           |        16 | VIP Indicator                                                                                                                                          | R                                                                                                                                    | user table         |
|           |        17 | Admitting Doctor                                                                                                                                       | 1234^DOE, JOHN M                                                                                                                     | composite ID       |
|           |        19 | Visit Number                                                                                                                                           | 1241243                                                                                                                              | composite ID       |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| { ORC}    |         1 | Order Control                                                                                                                                          | NW                                                                                                                                   | table 119          |
|           |         2 | Placer Order Number                                                                                                                                    | 234123;1^OR                                                                                                                          | number^application |
|           |         3 | Filler Order Number                                                                                                                                    | 870745^GMRC                                                                                                                          | number^application |
|           |         5 | Order Status                                                                                                                                           | IP                                                                                                                                   | table 38           |
|           |         7 | Quantity/Timing                                                                                                                                        | ^^^19940415^^R                                                                                                                       | ^^^timestamp^^priority  coded per HL7 4.	4                    |
|           |         9 | Date/Time of Transaction                                                                                                                               | 199404141425                                                                                                                         | timestamp          |
|           |        10 | Entered By                                                                                                                                             | 1166                                                                                                                                 | composite ID       |
|           |        12 | Ordering Provider                                                                                                                                      | 1270                                                                                                                                 | composite ID       |
|           |        15 | Order Effective D/T                                                                                                                                    | 199404141430                                                                                                                         | timestamp          |
|           |        16 | Order Control       Reason                                                                                                                             | S^Service Correction^99ORN^^^                                                                                                        | coded element      |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| NTE       |         1 | Set ID                                                                                                                                                 | 16                                                                                                                                   | set ID             |
|           |         2 | Source of Comment                                                                                                                                      | L                                                                                                                                    | table 105          |
|           |         3 | Comment                                                                                                                                                | Cancelled by Service                                                                                                                 | formatted text     |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| OBR       |         2 | Placer Order Number                                                                                                                                    | 5587658;1^OR                                                                                                                         | number^application |
|           |         3 | Filler Order Number                                                                                                                                    | 486410;GMRC^GMRC                                                                                                                     | number^application |
|           |         4 | Universal Service ID                                                                                                                                   | ^^^58^Cardiology^99CON                                                                                                               | coded element      |
|           |         6 | Requested Date/Time                                                                                                                                    | 20140311                                                                                                                             | timestamp          |
|           |        16 | Cerner Ordering Provider                                                                                                                               | For VistA to Cerner messages, the format of this field is:  Provider NPI^provider last name^provider first name^provider middle name | Free text          |
|           |        18 | Placer Field 1 (used for place of consultation                                                                                                         | B                                                                                                                                    | string             |
|           |        19 | Placer Field 2 (used for attention)  Between VistA and Cerner, populated with Field #508 Cerner Placer Field 1 in the REQUEST/CONSULTATION file (#123) | 1044                                                                                                                                 | string             |
|           |        20 | Filler Field 1  Between VistA and Cerner, populated with Field #511 OPT IN FOR FINAL STATUS in the REQUEST/CONSULTATION file (#123)                    | Y or N                                                                                                                               | string             |
|           |        22 | Results Rpt/Status Change - Date/Time                                                                                                                  | 199404150635                                                                                                                         | timestamp          |
|           |        25 | Result Status                                                                                                                                          | F                                                                                                                                    | table 123          |
|           |        27 | Quantity/Timing  Between VistA and Cerner, component 4 populated with Field #512 PERFORMED DATE/TIME in the REQUEST/CONSULTATION file (#123)           | ^^^202305030933+0600                                                                                                                 | string             |
|           |        32 | Principle Result Interpreter                                                                                                                           | 1345                                                                                                                                 | composite ID       |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| ZSV       |         1 | Request Service ID                                                                                                                                     | ^^^12^Psychiatry^99CON                                                                                                               | coded element      |
|           |         2 | Consult Type                                                                                                                                           | Family Counseling                                                                                                                    | string             |
|           |           |                                                                                                                                                        |                                                                                                                                      |                    |
| { OBX }   |         1 | Set ID                                                                                                                                                 | 1                                                                                                                                    | number             |
|           |         2 | Value Type                                                                                                                                             | TX                                                                                                                                   | table 125          |
|           |         3 | Observation ID                                                                                                                                         | 2000.02^Reason for Request^AS4                                                                                                       | coded element      |
|           |         4 | Observation Sub-ID                                                                                                                                     | 1                                                                                                                                    | string             |
|           |         5 | Observation Value                                                                                                                                      | r/o TB                                                                                                                               | string             |
| }         |         8 | Abnormal Flag                                                                                                                                          | N                                                                                                                                    | table 78           |

### Package Interface Notes

The following items merit emphasis:

- Sending Application is the name of the DHCP package generating the message; Sending Facility is the station number.
- Originating Referral Identifier is the IEN of the record entry in the Request/Consultation file.
- Patient ID is patient DFN (pointer to file 2)
- Patient Location, for an inpatient, is Hospital Location IEN^Room-Bed. For and outpatient, it is the Hospital Location IEN. In both cases it is the location from which the order is being placed.
- VIP Indicator is ‘R’ if patient is restricted/sensitive.
- Visit Number is the IEN of the visit in the Visit file.
- Placer Order Number is the OE/RR order number.
- Filler Order Number is the Consult order number.
- Order Status is needed when Consults releases an order; possible values from HL7 table 38 include the following:
    - **DC:** Discontinued
    - **SC:** Active
    - **A:** Partial Results
    - **CM:** Completed
    - **ZC:** Scheduled
    - **CA:** Cancelled (Denied)
    - **IP:** Pending
    - **RP:** DC’d due to Edit
- Quantity/Timing will contain Clinically Indicated Date in the fourth ^-piece and urgency in the sixth ^-piece, whose possible values include:
    - **S:** Stat
    - **Z24:** Within 24 hours
    - **ZW:** Within 1 week
    - **R:** Routine
    - **Z48:** Within 48 hours
    - **ZM:** Within 1 month
    - **ZT:** Today
    - **Z72:** Within 72 hours
    - **ZNA:** Next available
    - **ZE:** Emergency
- Entered By and Ordering Provider are IENs in the New Person file.
- Universal Service ID is a national code in the first part. The alternate code is a pointer to either the Request Services or GMRC Procedures file.
- Placer Field 1 will contain the place of consultation, as a set of codes. Possible values include:
    - B: Bedside
    - E: Emergency Room
    - OC: Consultant’s choice
- Placer Field 2 will contain the IEN in the New Person file of the user to whom this consult should be directed.
- The OBX segment is used to transmit related data about the patient when placing a consult request; possible observation IDs include:
    - Reason for Request (AS4 2000.02) = text
    - Provisional Diagnosis (not coded) = text
    - Provisional Diagnosis	(coded element) = ICD ^ text
- Observation ID is used for ordering OBX segments.

### HL7 Protocols

#### Patch GMRC*3.0*75

Patch GMRC*3.0*75 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with the Healthcare Claims Processing System (HCPS), which processes non-VA healthcare. Refer to Table 14-2.

Table 14-2: Patch GMRC*3.0*75 Protocol Description

| Protocol                | Description                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| GMRC CONSULTS TO HCP    | Creates and sends an REF^12, REF^13, or REF^14 HL7 message to the HCPS application when a consult is generated for Non-VA Care. |
| GMRC HCP REF-I12 SERVER | Sends REF^I12 HL7 messages to the HCPS application for new Non-VA Care Referrals.                                               |
| GMRC HCP REF-I12 CLIENT | Sends REF^I12 HL7 messages to the HCPS application for new Non-VA Care referrals.                                               |
| GMRC HCP REF-I13 SERVER | Sends HL7 REF^I13 messages to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).                     |
| GMRC HCP REF-I13 CLIENT | Sends HL7 REF^I13 messages from HCPS to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).           |
| GMRC HCP RRI-I13 SERVER | Sends HL7 RRI^I13 messages to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).                     |
| GMRC HCP RRI-I13 CLIENT | Sends HL7 RRI^I13 messages from HCPS to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).           |
| GMRC HCP REF-I14 SERVER | Sends REF^I14 HL7 messages to the HCPS application for canceled or discontinued Non-VA Care referrals.                          |
| GMRC HCP REF-I14 CLIENT | Sends REF^I14 HL7 messages to the HCPS application for cancelled or discontinued Non-VA Care referrals.                         |

#### Patch GMRC*3.0*99

Patch GMRC*3.0*99 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with CCRA for Non-VA COMMUNITY CARE consults. Refer to Table 14-3.

Table 14-3: Patch GMRC*3.0*99 Protocol Description

| Protocol                      | Description                                                                                                       |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GMRC CCRA REF-I12 CLIENT      | Sends HL7 REF^I12 v2.5 messages from CCRA to HSRM application for new Non-VA Care Referrals.                      |
| GMRC CCRA REF-I13 CLIENT      | Sends HL7 REF^I13 v2.5 messages to CCRA application for updated Non-VA Care Referrals.                            |
| GMRC CCRA REF-I14 CLIENT      | Sends HL7 REF^I14 v2.5 messages from CPRS to CCRA application for canceled or discontinued Non-VA Care Referrals. |
| GMRC CCRA-HSRM REF-I12 SERVER | Sends HL7 REF^I12 v2.5 messages from CPRS to CCRA application for new Non-VA Care Referrals.                      |
| GMRC CCRA-HSRM REF-I13 SERVER | Sends HL7 REF^I13 v2.5 messages from CPRS to CCRA application for new Non-VA Care Referrals.                      |
| GMRC CCRA-HSRM REF-I14 SERVER | Sends HL7 REF^I14 v2.5 messages from CPRS to CCRA application for cancellation of Non-VA Care Referrals.          |

#### Patch GMRC*3.0*123

Patch GMRC*3.0*123 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with CCRA for Non-VA COMMUNITY CARE consults. Refer to Table 14-4.

Table 14-4: Patch GMRC*3.0*123 Protocol Description

| Protocol                      | Description                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| GMRC HSRM-CCRA REF-I13 CLIENT | Sends HL7 REF^I13 v2.5 messages from HSRM application to CPRS. This is to update the consult record with new status (scheduled/complete) |
| GMRC HSRM-CCRA REF-I13 SERVER | Sends HL7 REF^I12 v2.5 messages from HSRM application to CPRS This is for consult status updates from HSRM                               |
| GMRC HSRM-CCRA REF-I14 CLIENT | Sends HL7 REF^I14 v2.5 messages from HSRM application to CPRS. This message type is to send to VistA an update to cancel the consult     |
| GMRC HSRM-CCRA REF-I14 SERVER | Sends HL7 REF^I12 v2.5 messages from HSRM application to CPRS. This is for consult status updates - cancel appointment.                  |

### HL7 Application Parameters

#### Patch GMRC*3.0*75

Patch GMRC*3.0*75 added the capability of using the following HL7 application parameters to enable communication between the consult system and the HCPS. Refer to Table 14-5.

Table 14-5: Patch GMRC*3.0*75 Application Parameters

| Protocol         | Description                                              |
|------------------|----------------------------------------------------------|
| GMRC HCP SEND    | This parameter is used to set up the sending facility.   |
| GMRC HCP RECEIVE | This parameter is used to set up the receiving facility. |

#### Patch GMRC*3.0*99

Patch GMRC*3.0*99 added the capability of using the following HL7 application parameters to enable communication between the consult system and the CCRA. Refer to Table 14-6.

Table 14-6: Patch GMRC*3.0*99 Application Parameters

| Protocol          | Description                                              |
|-------------------|----------------------------------------------------------|
| GMRC CCRA SEND    | This parameter is used to set up the sending facility.   |
| GMRC CCRA RECEIVE | This parameter is used to set up the receiving facility. |

#### Patch GMRC*3.0*123

Patch GMRC*3.0*123 added the capability of using the following HL7 application parameters to enable communication between the consult system and the CCRA. Refer to Table 14-7.

Table 14-7: Patch GMRC*3.0*123 Application Parameters

| Protocol               | Description                                              |
|------------------------|----------------------------------------------------------|
| GMRC HSRM-CCRA SEND    | This parameter is used to set up the sending facility.   |
| GMRC HSRM-CCRA RECEIVE | This parameter is used to set up the receiving facility. |

### HL7 Logical Link

HL7 Logical Links include the following:

- **GMRCHCP:** This Logical link is used to setup the network path between Consults and Healthcare Claims Processing System (HCPS).
- **GMRCCCRA:** This Logical link is used to set up the network path between CPRS and CCRA. This was created by patch GMRC*3.0*99
- **CCRA-NAK:** This logical link is used to send HSRM an application NAK when a message is rejected because the user does not exist or have permissions in VistA to make updates.   This was created by patch GMRC*3.0*123
    - **GMRC*3.0*99:** To enable the HL7 interface link created by this patch, go into the VistA HL main menu, and select the Filer and Link Management Options. From there, select the SL Stop/Start Links option, as shown below.
        - Once this logical link is thus enabled, messages can proceed through the interface.
    - **GMRC*3.0*106:** This logical link is the same as the one for GMRC*3.0*99.

### HL7 Referral Messages

Patch GMRC*3.0*75 added the capability of using the following HL7 referral messages to enable communication between the consult system and HCPS.

- REF\_I12 will be sent from CPRS to HCPS for new referrals (signed Non-VA Care Consult). NTE segments will contain the “Entered By”, “Date/time stamp”, the “Reason for Request” header, and Non-VA Care Referral template data.
- REF\_I13 will be sent from CPRS to HCPS for status updates and resubmitted referrals. NTE segments will contain the “Entered By” and “Date/time stamp”, “Progress Note” header, and Non-VA Care Referral template data.
- REF\_I13 will be sent from CPRS to HCPS for complete and addended note referrals. NTE segments will contain the “Entered By”, “Date/time stamp”, “Progress Note” header, and Non-VA Care Referral template data.
- RRI\_I13 will be sent from HCPS to CPRS for changes made in HCPS-RAS. A proxy user will be implemented in VistA to populate the “Entered By” field. The proxy user will identify updates to CPRS/Consults originating in HCPS-RAS and transmitted via the interface.
- REF\_I14 will be sent from CPRS to HCPS for cancelled or discontinued referrals. NTE segments will contain “Activity Comment” header and Non-VA Care Referral template date.

Note that IN1 and IN3 segments were added to the REF messages. Since these segments are the same, they will be listed once at the end of the section previously created in this manual.

The REF messages will contain the standard segments listed and described in Table 14-8.

Table 14-8: REF Message Standard Segments

| ## Segment  A standard HL7 v2.5 RRI message will be generated for status updates and/or changes made to an existing referral in HCPS. This event triggers a message to update CPRS with changes made in HCPS. The RRI message will contain the standard segments listed and described in Table 14-9.  Table 14-9: RRI Message Standard Segments  Segment Description Required/Optional MSH Message Header REQUIRED RRI Return Referral Information REQUIRED PRD Provider Data REQUIRED PID Patient Identification REQUIRED DG1 Diagnosis OPTIONAL OBR Observation Request REQUIRED PV1 Patient Visit REQUIRED NTE Notes and Comments REQUIRED  The following tables contain the HL7 message definition for the REF/RRI/ACK messages. Table columns include the following:  1. SEQ = HL7 sequence# 2. LEN = HL7 field length 3. DT = HL7 data type 4. R/O = R=Require, O=Optional, C=Conditional, NS=Not supported 5. TBL = HL7 table definition 6. Element Name = HL7 field name 7. VistA Description = information on what will be pulled from VistA for this element, or hard-coded data.   | Description            | Required/Optional            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------------|
| MSH:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Message Header         | REQUIRED                     |
| RF1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Referral Information   | REQUIRED                     |
| PRD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Provider Data          | REQUIRED                     |
| PID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Patient Identification | REQUIRED                     |
| IN1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                        | Patient Insurance (Optional) |
| IN3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                        | Patient Insurance (Optional) |
| DG1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Diagnosis              | OPTIONAL                     |
| OBR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Observation Request    | REQUIRED                     |
| PV1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Patient Visit          | REQUIRED                     |
| NTE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Notes and Comments     | REQUIRED                     |

### REF\_I12 Message Definition Tables

#### REF\_I12 MSH - Message Header Segment

The REF\_I12 MSH - Message Header Segment is generated by the VistA HL7 package using the HL7 Application and Protocol entries for the GMRC components.

Refer to Table 14-10.

Table 14-10: REF\_I12 Message Header Table

|   SEQ | LEN          | DT      | R/O   |   TBL# | Element Name                    | VistA Description                                                                              |
|-------|--------------|---------|-------|--------|---------------------------------|------------------------------------------------------------------------------------------------|
|     1 | 1            | ST      | R     |        | Field Separator                 | &#124;                                                                                         |
|     2 | 4            | ST      | R     |        | Encoding Characters             | ^~\&                                                                                           |
|     3 | 15           | ST      | R     |        | Sending Application             | GMRC HCP SEND                                                                                  |
|     4 | 20           | ST      | R     |        | Sending Facility                | Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND      |
|     5 | 30           | ST      | R     |        | Receiving Application           | GMRC HCP RECEIVE                                                                               |
|     6 | 30           | ST      | NS    |        | Receiving Facility              | Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE |
|     7 | 26           | TS      | R     |        | Date/Time Of Message            | System date/time generated by the VistA HL7 package                                            |
|     8 | 40           | ST      | NS    |        | Security                        | Not used                                                                                       |
|     9 | 7            | CM      | R     |   0076 |                                 |                                                                                                |
|  0003 | Message Type | REF^I12 |       |        |                                 |                                                                                                |
|    10 | 20           | ST      | R     |        | Message Control ID              | Facility and sequence number automatically generated by the VistA HL7 Package                  |
|    11 | 1            | ID      | R     |        | Processing ID                   | P for Production, T for Test                                                                   |
|    12 | 8            | ID      | R     |   0104 | Version ID                      | 2.	5                                                                                                |
|    13 | 15           | NM      | NS    |        | Sequence Number                 | Not used                                                                                       |
|    14 | 180          | ST      | NS    |        | Continuation Pointer            | Not used                                                                                       |
|    15 | 2            | ID      | R     |   0155 | Accept Acknowledgment Type      | AL=Always                                                                                      |
|    16 | 2            | ID      | R     |   0155 | Application Acknowledgment Type | AL=Always                                                                                      |
|    17 | 3            | ID      | R     |   0399 | Country Code                    | USA                                                                                            |

Note the following:

- MSH fields past MSH.17 are not used and not shown to save space.
- VistA MSH.16 does not support ER to just return Application Acknowledgments for errors, so all messages required acknowledgment – either AA or AE in the MSA.

Refer to Table 14-11.

Table 14-11: REF\_I12 RF1 - Referral Information Segment

| SEQ                                                                         |   LEN | DT   | R/O   |   TBL# | Element Name                    | VistA Description                                                                                                                                                         |
|-----------------------------------------------------------------------------|-------|------|-------|--------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                                                                           |   250 | CE   | O     |   0283 | Referral Status                 | NW^CPRS RELEASED ORDER                                                                                                                                                    |
| 2                                                                           |   250 | CE   | O     |   0280 | Referral Priority               | From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY,  TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS |
| 3                                                                           |   250 | CE   | O     |        | Referral Type                   | Service IEN^Service Name^^Template IEN                                                                                                                                    |
| ^Template Name                                                              |       |      |       |        |                                 |                                                                                                                                                                           |
| Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927. |       |      |       |        |                                 |                                                                                                                                                                           |
| 4                                                                           |   250 | CE   | NS    |        | Referral Disposition            | Not used                                                                                                                                                                  |
| 5                                                                           |   250 | CE   | O     |   0284 | Referral Category               | I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.             |
| 6                                                                           |    30 | EI   | R     |        | Originating Referral Identifier | IEN to File 123                                                                                                                                                           |
| 7                                                                           |    26 | TS   | O     |        | Effective Date                  | Referral Date of Request from File 123, field .01                                                                                                                         |
| 8                                                                           |    26 | TS   | NS    |        | Expiration Date                 | Not used                                                                                                                                                                  |
| 9                                                                           |    26 | TS   | NS    |        | Process Date                    | Not used                                                                                                                                                                  |
| 10                                                                          |   250 | CE   | NS    |        | Referral Reason                 | Not used                                                                                                                                                                  |
| 11                                                                          |    30 | EI   | NS    |        | External Referral Identifier    | Not used                                                                                                                                                                  |

Refer to Table 14-12.	 Note REF\_I12 PRD - Provider Data Segment is the same for all message types.

Table 14-12: REF\_I12 PRD - Provider Data Segment

| SEQ                              |   LEN | DT   | R/O   |   TBL# | Element Name                          | VistA Description                                                                                   |
|----------------------------------|-------|------|-------|--------|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| 1                                |   250 | CE   | R     |   0286 | Provider Role                         | RP  for Referring Provider                                                                          |
| 2                                |   250 | XPN  | O     |        | Provider Name                         | Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ                    |
| Provider from File 123, field 10 |       |      |       |        |                                       |                                                                                                     |
| 3                                |   250 | XAD  | O     |        | Provider Address                      | Street Address 1^Street Address 2^City^State^Zip from File 200, fields .111, .112, .114, .115, .116 |
| 4                                |    60 | PL   | NS    |        | Provider Location                     | Not used                                                                                            |
| 5                                |   250 | XTN  | O     |        | Provider Communication Information    | ^^^Email Address^^Office Phone Area Code^Office Phone Number from File 200, fields .151, .132       |
| 6                                |   250 | CE   | NS    |        | Preferred Method of Contact           | Not used                                                                                            |
| 7                                |   100 | PLN  | NS    |        | Provider Identifiers                  | Not used                                                                                            |
| 8                                |    26 | TS   | NS    |        | Effective Start Date of Provider Role | Not used                                                                                            |
| 9                                |    26 | TS   | NS    |        | Effective End Date of Provider Role   | Not used                                                                                            |

Refer to Table 14-13. Note that REF\_I12 PID-Patient Id Segment is generated by the VistA API, and is the same for all msg types.

Table 14-13: REF\_I12 PID-Patient Id Segment

| SEQ                                                          | LEN                                                                                                                                                                                                                                       | DT   | R/O   |   TBL# | Element Name                                                 | VistA Description                                                                                                    |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-------|--------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|                                                              | 4                                                                                                                                                                                                                                         | SI   | O     |        | Set ID – PID                                                 | Sequential Number                                                                                                    |
| 2                                                            | 20                                                                                                                                                                                                                                        | CX   | R     |        | Patient ID                                                   | ICN, including V checksum for backwards compatibility                                                                |
| 3                                                            | 250                                                                                                                                                                                                                                       | CX   | R     |        | Patient Identifier List (list is not in any specified order) |                                                                                                                      |
| Following are PID.3.5 Identifier Type Codes:                 |                                                                                                                                                                                                                                           |      |       |        |                                                              |                                                                                                                      |
| NI=ICN                                                       |                                                                                                                                                                                                                                           |      |       |        |                                                              |                                                                                                                      |
| PI=Patient DFN                                               |                                                                                                                                                                                                                                           |      |       |        |                                                              |                                                                                                                      |
| SS=SSN                                                       |                                                                                                                                                                                                                                           |      |       |        |                                                              |                                                                                                                      |
| PN=Claim Number                                              | Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5). |      |       |        |                                                              |                                                                                                                      |
| 4                                                            | 20                                                                                                                                                                                                                                        | CX   | NS    |        | Alternate Patient ID – PID                                   | Not used                                                                                                             |
| 5                                                            | 250                                                                                                                                                                                                                                       | XPN  | R     |        | Patient Name                                                 | Patient Name and all Alias entries                                                                                   |
| 6                                                            | 250                                                                                                                                                                                                                                       | XPN  | O     |        | Mother’s Maiden Name                                         | Mother’s Maiden Name                                                                                                 |
| 7                                                            | 26                                                                                                                                                                                                                                        | TS   | O     |        | Date/Time of Birth                                           | Date of Birth                                                                                                        |
| 8                                                            | 1                                                                                                                                                                                                                                         | IS   | O     |   0001 | Administrative Sex                                           | Sex                                                                                                                  |
| 9                                                            | 250                                                                                                                                                                                                                                       | XPN  | NS    |        | Patient Alias                                                | Not used. Alias is passed in PID-5                                                                                   |
| 10                                                           | 250                                                                                                                                                                                                                                       | CE   | O     |   0005 | Race                                                         | Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded. |
| 11                                                           | 250                                                                                                                                                                                                                                       | XAD  | O     |        | Patient Address                                              | P=Permanent Address~N=Place of Birth~Confidential Address                                                            |
| 12                                                           | 4                                                                                                                                                                                                                                         | IS   | O     |   0289 | County Code                                                  | County                                                                                                               |
| 13                                                           | 250                                                                                                                                                                                                                                       | XTN  | O     |        | Phone Number – Home                                          | Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email                                                            |
| 14                                                           | 250                                                                                                                                                                                                                                       | XTN  | O     |        | Phone Number – Business                                      | Work Phone (backward compatibility)                                                                                  |
| 15                                                           | 250                                                                                                                                                                                                                                       | CE   | NS    |   0296 | Primary Language                                             | Not used                                                                                                             |
| 16                                                           | 250                                                                                                                                                                                                                                       | CE   | O     |   0002 | Marital Status                                               | Marital Status^^^^^^M                                                                                                |
| 17                                                           | 250                                                                                                                                                                                                                                       | CE   | O     |   0006 | Religion                                                     | Religious Preference (code)                                                                                          |
| 18                                                           | 250                                                                                                                                                                                                                                       | CX   | NS    |        | Patient Account Number                                       | Not used                                                                                                             |
| 19                                                           | 16                                                                                                                                                                                                                                        | ST   | R     |        | SSN Number – Patient                                         | SSN                                                                                                                  |
| 20                                                           | 25                                                                                                                                                                                                                                        | DLN  | NS    |        | Driver’s License Number – Patient                            | Not used                                                                                                             |
| 21                                                           | 250                                                                                                                                                                                                                                       | CX   | NS    |        | Mother’s Identifier                                          | Not used                                                                                                             |
| 22                                                           | 250                                                                                                                                                                                                                                       | CE   | O     |   0189 | Ethnic Group                                                 | Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC                                                         |
| See Appendix A for coded values. 2186 and CDC are hardcoded. |                                                                                                                                                                                                                                           |      |       |        |                                                              |                                                                                                                      |
| 23                                                           | 250                                                                                                                                                                                                                                       | ST   | O     |        | Birthplace                                                   | Place of birth city and place of birth state                                                                         |
| 24                                                           | 1                                                                                                                                                                                                                                         | ID   | O     |   0136 | Multiple Birth Indicator                                     | Multiple Birth Indicator [Y for multiple birth]                                                                      |

- Note (PID fields past PID.24 not used and not shown to save space.

Refer to Table 14-14. REF\_I12 DG1 - Diagnosis Segment is the same for all message types.

Table 14-14:  REF\_I12 DG1 - Diagnosis Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name            | VistA Description                                                        |
|-------|-------|------|-------|--------|-------------------------|--------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – DG1            | 1                                                                        |
|     2 |     2 | ID   | NS    |        | Diagnosis Coding Method | Not used                                                                 |
|     3 |   250 | CE   | R     |   0051 | Diagnosis Code – DG1    | Provisional Diagnosis Code^Diagnosis Description from File 123, field 30 |
|     4 |    40 | ST   | B     |        | Diagnosis Description   | Not Used                                                                 |
|     5 |    26 | TS   | O     |        | Diagnosis Date/Time     | Not Used                                                                 |
|     6 |     2 | IS   | R     |   0052 | Diagnosis Type          | “W” - Working                                                            |

- Note DG1 fields past DG1.6 are not used and not shown to save space.

Refer to Table 14-15. Note REF\_I12 OBR - Observation Request Segment is the same for all message types.

Table 14-15: REF\_I12 OBR - Observation Request Segment

|   SEQ |   LEN | DT   | R/O   | TBL#   | Element Name                 | VistA Description                                                            |
|-------|-------|------|-------|--------|------------------------------|------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – OBR                 | 1                                                                            |
|     2 |    22 | EI   | R     |        | Placer Order Number          | Order entry internal number;Orderable Item entry^OR from File 123, field .03 |
|     3 |    22 | EI   | R     |        | Filler Order Number          | Consult entry internal number;GMRC^GMRC                                      |
|     4 |   250 | CE   | R     |        | Universal Service Identifier | Hardcoded value of “ZZ”                                                      |
|     5 |     2 | ID   | NS    |        | Priority – OBR               | Not used                                                                     |
|     6 |    26 | TS   | O     |        | Requested Date/Time          | Clinically Indicated Date from File 123, field 17                            |

- OBR fields past OBR.6 are not used and not shown to save space.

Refer to Table 14-16.	 REF\_I12 PV1 – Patient Visit Segment is the same for all message types. Further, the PV1 segment data is created using the IN5^VADPT call to determine current inpatient status. See PIMS technical manual for definition of the returned array VAIP. Fields not returned by the IN5^VADPT API are not used in the PV1 segment.

Table 14-16: REF\_I12 PV1 – Patient Visit Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name              | VistA Description                                      |
|-------|-------|------|-------|--------|---------------------------|--------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PV1              | 1                                                      |
|     2 |     1 | IS   | R     |   0004 | Patient Class             | I: inpatient  O: outpatient                            |
|     3 |    80 | PL   | O     |        | Assigned Patient Location | Location of last inpatient movement event from VAIP(5) |
|     4 |     2 | IS   | NS    |        | Admission Type            | Not used                                               |
|     5 |   250 | CX   | NS    |        | Preadmit Number           | Not used                                               |
|     6 |    80 | PL   | NS    |        | Prior Patient Location    | Not used                                               |
|     7 |   250 | XCN  | O     |   0010 | Attending Doctor          | Attending Provider from VAIP(18  )                     |
|     8 |   250 | XCN  | O     |   0010 | Referring Doctor          | Not used (Referring provider sent in PRD segment)      |
|     9 |   250 | XCN  | NS    |        | Consulting Doctor         | Not used                                               |
|    10 |     3 | IS   | NS    |        | Hospital Service          | Not used                                               |
|    11 |    80 | PL   | NS    |        | Temporary Location        | Not used                                               |
|    12 |     2 | IS   | NS    |        | Preadmit Test Indicator   | Not used                                               |
|    13 |     2 | IS   | NS    |        | Re-admission Indicator    | Not used                                               |
|    14 |     6 | IS   | NS    |        | Admit Source              | Not used                                               |
|    15 |     2 | IS   | NS    |        | Ambulatory Status         | Not used                                               |
|    16 |     2 | IS   | O     |   0099 | VIP Indicator             | R if patient restricted/sensitive                      |
|    17 |   250 | XCN  | O     |        | Admitting Doctor          | Primary Physician for admission from VAIP (13,5)       |

- Note PV1 fields past PV1.17 are not used and not shown to save space.

Refer to Table 14-17.

Table 14-17: REF\_112 NTE – Notes and Comments Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name      | VistA Description                          |
|-------|-------|------|-------|--------|-------------------|--------------------------------------------|
|     1 |     4 | SI   | O     |        | Set ID – NTE      | Sequential Number 1-n                      |
|     2 |     8 | ID   | O     |   0105 | Source of Comment | P for Placer                               |
|     3 | 65536 | FT   | O     |        | Comment           | Reason for Request from file 123, field 20 |
|     4 |   250 | CE   | O     |        | Comment Type      | Not used.                                  |

Refer to Figures 14-1 and 14-2.

Figure 14-1: New, signed Referral for Non VA Care Radiology Example

<!-- image -->

Figure 14-2: New, signed Referral for Non VA Care Radiology Example (continued)

<!-- image -->

Refer to Figure 14-3.

Figure 14-3: New, signed Referral for Non VA Care Dental Example

<!-- image -->

### REF\_I13 Message Definition Tables

#### REF\_I13 MSH - Message Header Segment

The REF\_I13 MSH Message Header segment is generated by the VistA HL7 package using the HL7 Application and Protocol entries for the GMRC components.

Refer to Table 14-18.

Table 14-18: REF\_I13 MSH - Message Header Segment

|   SEQ |   LEN | DT   | R/O   | TBL#      | Element Name                    | VistA Description                                                                              |
|-------|-------|------|-------|-----------|---------------------------------|------------------------------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |           | Field Separator                 | &#124;                                                                                         |
|     2 |     4 | ST   | R     |           | Encoding Characters             | ^~\&                                                                                           |
|     3 |    15 | ST   | R     |           | Sending Application             | GMRC HCP SEND                                                                                  |
|     4 |    20 | ST   | R     |           | Sending Facility                | Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND      |
|     5 |    30 | ST   | R     |           | Receiving Application           | GMRC HCP RECEIVE                                                                               |
|     6 |    30 | ST   | NS    |           | Receiving Facility              | Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE |
|     7 |    26 | TS   | R     |           | Date/Time Of Message            | System date/time generated by the VistA HL7 package                                            |
|     8 |    40 | ST   | NS    |           | Security                        | Not used                                                                                       |
|     9 |     7 | CM   | R     | 0076 0003 | Message Type                    | REF^I13                                                                                        |
|    10 |    20 | ST   | R     |           | Message Control ID              | Facility and sequence number automatically generated by the HL7 Package                        |
|    11 |     1 | ID   | R     |           | Processing ID                   | P for Production, T for Test                                                                   |
|    12 |     8 | ID   | R     | 0104      | Version ID                      | 2.	5                                                                                                |
|    13 |    15 | NM   | NS    |           | Sequence Number                 | Not used                                                                                       |
|    14 |   180 | ST   | NS    |           | Continuation Pointer            | Not used                                                                                       |
|    15 |     2 | ID   | R     | 0155      | Accept Acknowledgment Type      | AL=Always                                                                                      |
|    16 |     2 | ID   | R     | 0155      | Application Acknowledgment Type | AL=Always                                                                                      |
|    17 |     3 | ID   | R     | 0399      | Country Code                    | USA                                                                                            |

Note the following:

- MSH fields past MSH.17 are not used and not shown to save space.
- MSH.16 does not support ER to just return Application Acknowledgements for errors, so all messages required acknowledgement – either AA or AE in the MSA.

Refer to Table 14-19.

Table 14-19: REF\_I13 RF1 – Referral Information Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                    | VistA Description                                                                                                                                                         |
|-------|-------|------|-------|--------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | O     |   0283 | Referral Status                 | SC^RECEIVED  SC^SCHEDULED IP^RESUBMITTED IP^ADD COMMENT XX^FORWARDED  CM^COMPLETE CM^ADDENDED                                                                             |
|     2 |   250 | CE   | O     |   0280 | Referral Priority               | From File 123, Field 5 (Urgency). Values are:  1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS |
|     3 |   250 | CE   | O     |        | Referral Type                   | Service IEN^Service Name^^Template IEN ^Template Name Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.                                         |
|     4 |   250 | CE   | NS    |        | Referral Disposition            | Not used                                                                                                                                                                  |
|     5 |   250 | CE   | O     |   0284 | Referral Category               | I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.             |
|     6 |    30 | EI   | R     |        | Originating Referral Identifier | IEN to File 123                                                                                                                                                           |
|     7 |    26 | TS   | O     |        | Effective Date                  | Referral Date of Request from File 123, field .01                                                                                                                         |
|     8 |    26 | TS   | NS    |        | Expiration Date                 | Not used                                                                                                                                                                  |
|     9 |    26 | TS   | NS    |        | Process Date                    | Not used                                                                                                                                                                  |
|    10 |   250 | CE   | NS    |        | Referral Reason                 | Not used                                                                                                                                                                  |
|    11 |    30 | EI   | NS    |        | External Referral Identifier    | Not used                                                                                                                                                                  |

- HCPS will send the Originating Referral Identifier that was sent in the initial REF^I12 from VistA and blanks for everything else.

Refer to Table 14-20.

Table 14-20: REF\_I13 PRD - Provider Data Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                          | VistA Description                                                                                                  |
|-------|-------|------|-------|--------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | R     |   0286 | Provider Role                         | RP for Referring Provider                                                                                          |
|     2 |   250 | XPN  | O     |        | Provider Name                         | Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ  Provider from File 123, field 10 |
|     3 |   250 | XAD  | O     |        | Provider Address                      | Street Address 1^Street Address 2^City^State^Zip from File 2, fields .111, .112, .114, .115, .116                  |
|     4 |    60 | PL   | NS    |        | Provider Location                     | Not used                                                                                                           |
|     5 |   250 | XTN  | O     |        | Provider Communication Information    | ^^^Email Address^^Office Phone Area Code^Office Phone Number from File 2, fields .151, .132                        |
|     6 |   250 | CE   | NS    |        | Preferred Method of Contact           | Not used                                                                                                           |
|     7 |   100 | PLN  | NS    |        | Provider Identifiers                  | Not used                                                                                                           |
|     8 |    26 | TS   | NS    |        | Effective Start Date of Provider Role | Not used                                                                                                           |
|     9 |    26 | TS   | NS    |        | Effective End Date of Provider Role   | Not used                                                                                                           |

- HCPS will send the Provider Role that was sent in the initial REF^I12 from VistA and blanks for everything else.

Refer to Table 14-21.

Table 14-21: REF\_I13 PID – Patient Id Segment generated by the VistA API (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                                                                                                                                            | VistA Description                                                                                                                                                                                                                         |
|-------|-------|------|-------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PID                                                                                                                                            | Sequential Number                                                                                                                                                                                                                         |
|     2 |    20 | CX   | R     |        | Patient ID                                                                                                                                              | ICN, including V checksum for backwards compatibility                                                                                                                                                                                     |
|     3 |   250 | CX   | R     |        | Patient Identifier List (list is not in any specified order): Following are PID.3.5 Identifier Type Codes: NI=ICN PI=Patient DFN SS=SSN PN=Claim Number | Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5). |
|     4 |    20 | CX   | NS    |        | Alternate Patient ID – PID                                                                                                                              | Not used                                                                                                                                                                                                                                  |
|     5 |   250 | XPN  | R     |        | Patient Name                                                                                                                                            | Patient Name and all Alias entries                                                                                                                                                                                                        |
|     6 |   250 | XPN  | O     |        | Mother’s Maiden Name                                                                                                                                    | Mother’s Maiden Name                                                                                                                                                                                                                      |
|     7 |    26 | TS   | O     |        | Date/Time of Birth                                                                                                                                      | Date of Birth                                                                                                                                                                                                                             |
|     8 |     1 | IS   | O     |      1 | Administrative Sex                                                                                                                                      | Sex                                                                                                                                                                                                                                       |
|     9 |   250 | XPN  | NS    |        | Patient Alias                                                                                                                                           | Not used. Alias is passed in PID-5                                                                                                                                                                                                        |
|    10 |   250 | CE   | O     |      5 | Race                                                                                                                                                    | Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.                                                                                                                      |
|    11 |   250 | XAD  | O     |        | Patient Address                                                                                                                                         | P=Permanent Address~N=Place of Birth~Confidential Address                                                                                                                                                                                 |
|    12 |     4 | IS   | O     |    289 | County Code                                                                                                                                             | County                                                                                                                                                                                                                                    |
|    13 |   250 | XTN  | O     |        | Phone Number – Home                                                                                                                                     | Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email                                                                                                                                                                                 |
|    14 |   250 | XTN  | O     |        | Phone Number – Business                                                                                                                                 | Work Phone (backward compatibility)                                                                                                                                                                                                       |
|    15 |   250 | CE   | NS    |    296 | Primary Language                                                                                                                                        | Not used                                                                                                                                                                                                                                  |
|    16 |   250 | CE   | O     |      2 | Marital Status                                                                                                                                          | Marital Status^^^^^^M                                                                                                                                                                                                                     |
|    17 |   250 | CE   | O     |      6 | Religion                                                                                                                                                | Religious Preference (code)                                                                                                                                                                                                               |
|    18 |   250 | CX   | NS    |        | Patient Account Number                                                                                                                                  | Not used                                                                                                                                                                                                                                  |
|    19 |    16 | ST   | R     |        | SSN Number – Patient                                                                                                                                    | SSN                                                                                                                                                                                                                                       |
|    20 |    25 | DLN  | NS    |        | Driver’s License Number – Patient                                                                                                                       | Not used                                                                                                                                                                                                                                  |
|    21 |   250 | CX   | NS    |        | Mother’s Identifier                                                                                                                                     | Not used                                                                                                                                                                                                                                  |
|    22 |   250 | CE   | O     |    189 | Ethnic Group                                                                                                                                            | Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC                                                                                                                                                                              |
|       |       |      |       |        |                                                                                                                                                         | See Appendix A for coded values. 2186 and CDC are hardcoded.                                                                                                                                                                              |
|    23 |   250 | ST   | O     |        | Birthplace                                                                                                                                              | Place of birth city and place of birth state                                                                                                                                                                                              |
|    24 |     1 | ID   | O     |    136 | Multiple Birth Indicator                                                                                                                                | Multiple Birth Indicator [Y for multiple birth]                                                                                                                                                                                           |

- HCPS will only send the original information in the initial REF^I12 from VistA for sequences 1, 2, 3, 5, and 19.

Refer to Table 14-22.

Table 14-22: REF\_I13 DG1 – Diagnosis Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name            | VistA Description                                                        |
|-------|-------|------|-------|--------|-------------------------|--------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – DG1            | 1                                                                        |
|     2 |     2 | ID   | NS    |        | Diagnosis Coding Method | Not used                                                                 |
|     3 |   250 | CE   | R     |        | Diagnosis Code – DG1    | Provisional Diagnosis Code^Diagnosis Description from File 123, field 30 |
|     4 |    40 | ST   | B     |        | Diagnosis Description   | Not Used                                                                 |
|     5 |    26 | TS   | O     |        | Diagnosis Date/Time     | Not Used                                                                 |
|     6 |     2 | IS   | R     |   0052 | Diagnosis Type          | “W” - Working                                                            |

- DG1 fields past DG1.6 are not used and not shown to save space.

Refer to Table 14-23.

Table 14-23: REF\_I13 OBR – Observation Request Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   | TBL#   | Element Name                 | VistA Description                                                                                                                                 |
|-------|-------|------|-------|--------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – OBR                 | 1                                                                                                                                                 |
|     2 |    22 | EI   | R     |        | Placer Order Number          | Order entry internal number;Orderable Item entry^OR from File 123, field .03                                                                      |
|     3 |    22 | EI   | R     |        | Filler Order Number          | Consult entry internal number;GMRC^GMRC for all comments and TIU note internal entry number; TIU^TIU for all signed progress notes and addendums. |
|     4 |   250 | CE   | R     |        | Universal Service Identifier | Hardcoded value of “ZZ”                                                                                                                           |
|     5 |     2 | ID   | NS    |        | Priority – OBR               | Not used                                                                                                                                          |
|     6 |    26 | TS   | O     |        | Requested Date/Time          | Clinically Indicated Date from File 123, field 17                                                                                                 |

Note the following:

- OBR fields past OBR.6 are not used and not shown to save space.
- REF\_I13 PV1 – Patient Visit Segment (same for all message types)
- The PV1 segment data is creating using the IN5^VADPT call to determine current inpatient status. See PIMS technical manual for definition of the returned array VAIP.
- Fields not returned by the IN5^VADPT API are not used in the PV1 segment.

Refer to Table 14-24.

Table 14-24: REF\_I13 PV1 - Patient Visit Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name              | VistA Description                                      |
|-------|-------|------|-------|--------|---------------------------|--------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PV1              | 1                                                      |
|     2 |     1 | IS   | R     |   0004 | Patient Class             | I: inpatient O: outpatient                             |
|     3 |    80 | PL   | O     |        | Assigned Patient Location | Location of last inpatient movement event from VAIP(5) |
|     4 |     2 | IS   | NS    |        | Admission Type            | Not used                                               |
|     5 |   250 | CX   | NS    |        | Preadmit Number           | Not used                                               |
|     6 |    80 | PL   | NS    |        | Prior Patient Location    | Not used                                               |
|     7 |   250 | XCN  | O     |   0010 | Attending Doctor          | Attending Provider from VAIP(18  )                     |
|     8 |   250 | XCN  | O     |   0010 | Referring Doctor          | Not used (Referring provider sent in PRD segment)      |
|     9 |   250 | XCN  | NS    |        | Consulting Doctor         | Not used                                               |
|    10 |     3 | IS   | NS    |        | Hospital Service          | Not used                                               |
|    11 |    80 | PL   | NS    |        | Temporary Location        | Not used                                               |
|    12 |     2 | IS   | NS    |        | Preadmit Test Indicator   | Not used                                               |
|    13 |     2 | IS   | NS    |        | Re-admission Indicator    | Not used                                               |
|    14 |     6 | IS   | NS    |        | Admit Source              | Not used                                               |
|    15 |     2 | IS   | NS    |        | Ambulatory Status         | Not used                                               |
|    16 |     2 | IS   | O     |   0099 | VIP Indicator             | R if patient restricted/sensitive                      |
|    17 |   250 | XCN  | O     |   0010 | Admitting Doctor          | Primary Physician for admission from VAIP(13,5)        |

Note the following:

- HCPS will only send the original information in the initial REF^I12 from VistA for sequences 1 and 2.
- (PV1 fields past PV1.17 are not used and not shown to save space)

Refer to Table 14-25.

Table 14-25: REF\_I13 NTE – Notes and Comments Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name      | VistA Description                                                                                                                                                                                                                                                                                                                                                         |
|-------|-------|------|-------|--------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | O     |        | Set ID – NTE      | Sequential Number 1-n                                                                                                                                                                                                                                                                                                                                                     |
|     2 |     8 | ID   | O     |   0105 | Source of Comment | P for Placer L for Ancillary                                                                                                                                                                                                                                                                                                                                              |
|     3 | 65536 | FT   | O     |        | Comment           | Based on message type, Resubmitted consults messages (RF1.1= IP^RESUBMITTED) will contain Reason for Request from file 123, field 20  , Completed or Addended (RF1.1= CM^COMPLETE CM^ADDENDED) will contain TIU Progress Note from file 8925 (signed notes/addendums only).  All other I13 messages will contain Activity Comments from file 123, subfile 123.25 field 5. |
|     4 |   250 | CE   | O     |        | Comment Type      | Not used.                                                                                                                                                                                                                                                                                                                                                                 |

- HCPS will send Notes/Comments/Status changes made in the Referral in HCPS.

Refer to Figure 14-4.

Figure 14-4: Receive Referral Example

<!-- image -->

Refer to Figure 14-5. Note no comment entered during Schedule denotes no NTE segment sent.

Figure 14-5: Schedule Referral Example

<!-- image -->

Refer to Figure 14-6.

Figure 14-6: Comment Referral Example

<!-- image -->

Refer to Figure 14-7.

Figure 14-7: Complete Referral Example

<!-- image -->

### RRI\_I13 Message Definition Tables

HCPS will update CPRS with information entered into HCPS via HL7 message RRI (Return Referral Information). The RRI^I13 message structure is exactly the same as the REF^I13 used by CPRS to send referral information to HCPS.

#### RRI\_I13 MSH - Message Header Segment

The RRI\_I13 MSH - Message Header segment is generated by the VistA HL7 package using HL7 Application and Protocol entries for the GMRC components.

Refer to Table 14-26.

Table 14-26: RRI\_I13 MSH - Message Header Segment Table

|   SEQ | LEN          | DT      | R/O   |   TBL# | Element Name                    | VistA Description                                                                              |
|-------|--------------|---------|-------|--------|---------------------------------|------------------------------------------------------------------------------------------------|
|     1 | 1            | ST      | R     |        | Field Separator                 | &#124;                                                                                         |
|     2 | 4            | ST      | R     |        | Encoding Characters             | ^~\&                                                                                           |
|     3 | 15           | ST      | R     |        | Sending Application             | GMRC HCP SEND                                                                                  |
|     4 | 20           | ST      | R     |        | Sending Facility                | Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND      |
|     5 | 30           | ST      | R     |        | Receiving Application           | GMRC HCP RECEIVE                                                                               |
|     6 | 30           | ST      | NS    |        | Receiving Facility              | Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE |
|     7 | 26           | TS      | R     |        | Date/Time Of Message            | System date/time generated by the VistA HL7 package                                            |
|     8 | 40           | ST      | NS    |        | Security                        | Not used                                                                                       |
|     9 | 7            | CM      | R     |   0076 |                                 |                                                                                                |
|  0003 | Message Type | RRI^I13 |       |        |                                 |                                                                                                |
|    10 | 20           | ST      | R     |        | Message Control ID              | Facility and sequence number automatically generated by the HL7 Package                        |
|    11 | 1            | ID      | R     |        | Processing ID                   | P for Production, T for Test                                                                   |
|    12 | 8            | ID      | R     |   0104 | Version ID                      | 2.	5                                                                                                |
|    13 | 15           | NM      | NS    |        | Sequence Number                 | Not used                                                                                       |
|    14 | 180          | ST      | NS    |        | Continuation Pointer            | Not used                                                                                       |
|    15 | 2            | ID      | R     |   0155 | Accept Acknowledgment Type      | AL=Always                                                                                      |
|    16 | 2            | ID      | R     |   0155 | Application Acknowledgment Type | AL=Always                                                                                      |
|    17 | 3            | ID      | R     |   0399 | Country Code                    | USA                                                                                            |

Note the following:

- (MSH fields past MSH.17 are not used and not shown to save space)
- MSH.16 does not support ER to just return Application Acknowledgements for errors, so all messages required acknowledgement, either AA or AE in the MSA.

Refer to Table 14-27.

Table 14-27: RRI\_I13 RF1 – Referral Information Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                    | VistA Description                                                                                                                                                        |
|-------|-------|------|-------|--------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | O     |   0283 | Referral Status                 | SC^RECEIVED SC^SCHEDULED IP^RESUBMITTED IP^COMMENT XX^FORWARDED CM^COMPLETE CM^ADDENDED                                                                                  |
|     2 |   250 | CE   | O     |   0280 | Referral Priority               | From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS |
|     3 |   250 | CE   | O     |        | Referral Type                   | Service IEN^Service Name^^Template IEN ^Template Name Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.                                        |
|     4 |   250 | CE   | NS    |        | Referral Disposition            | Not used                                                                                                                                                                 |
|     5 |   250 | CE   | O     |   0284 | Referral Category               | I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.            |
|     6 |    30 | EI   | R     |        | Originating Referral Identifier | IEN to File 123                                                                                                                                                          |
|     7 |    26 | TS   | O     |        | Effective Date                  | Referral Date of Request from File 123, field .01                                                                                                                        |
|     8 |    26 | TS   | NS    |        | Expiration Date                 | Not used                                                                                                                                                                 |
|     9 |    26 | TS   | NS    |        | Process Date                    | Not used                                                                                                                                                                 |
|    10 |   250 | CE   | NS    |        | Referral Reason                 | Not used                                                                                                                                                                 |
|    11 |    30 | EI   | NS    |        | External Referral Identifier    | Not used                                                                                                                                                                 |

- HCPS will send the Originating Referral Identifier that was sent in the initial REF^I12 from VistA and blanks for everything else.

Refer to Table 14-28.

Table 14-28: RRI\_I13 PRD - Provider Data Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                          | VistA Description                                                                                                 |
|-------|-------|------|-------|--------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | R     |   0286 | Provider Role                         | RP for Referring Provider                                                                                         |
|     2 |   250 | XPN  | O     |        | Provider Name                         | Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ Provider from File 123, field 10 |
|     3 |   250 | XAD  | O     |        | Provider Address                      | Street Address 1^Street Address 2^City^State^Zip from File 2, fields .111, .112, .114, .115, .116                 |
|     4 |    60 | PL   | NS    |        | Provider Location                     | Not used                                                                                                          |
|     5 |   250 | XTN  | O     |        | Provider Communication Information    | ^^^Email Address^^Office Phone Area Code^Office Phone Number from File 2, fields .151, .132                       |
|     6 |   250 | CE   | NS    |        | Preferred Method of Contact           | Not used                                                                                                          |
|     7 |   100 | PLN  | NS    |        | Provider Identifiers                  | Not used                                                                                                          |
|     8 |    26 | TS   | NS    |        | Effective Start Date of Provider Role | Not used                                                                                                          |
|     9 |    26 | TS   | NS    |        | Effective End Date of Provider Role   | Not used                                                                                                          |

- HCPS will send the Provider Role that was sent in the initial REF^I12 from VistA and blanks for everything else.

Refer to Table 14-29. The RRI\_I13 PID Patient Id segment is generated by the VistA AP. PID fields past PID.24 not used and not shown to save space.

Table 14-29: RRI\_I13 PID – Patient Id Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                                                                                                                                           | VistA Description                                                                                                                                                                                                                         |
|-------|-------|------|-------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PID                                                                                                                                           | Sequential Number                                                                                                                                                                                                                         |
|     2 |    20 | CX   | R     |        | Patient ID                                                                                                                                             | ICN, including V checksum for backwards compatibility                                                                                                                                                                                     |
|     3 |   250 | CX   | R     |        | Patient Identifier List (list is not in any specified order) Following are PID.3.5 Identifier Type Codes: NI=ICN PI=Patient DFN SS=SSN PN=Claim Number | Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5). |
|     4 |    20 | CX   | NS    |        | Alternate Patient ID – PID                                                                                                                             | Not used                                                                                                                                                                                                                                  |
|     5 |   250 | XPN  | R     |        | Patient Name                                                                                                                                           | Patient Name and all Alias entries                                                                                                                                                                                                        |
|     6 |   250 | XPN  | O     |        | Mother’s Maiden Name                                                                                                                                   | Mother’s Maiden Name                                                                                                                                                                                                                      |
|     7 |    26 | TS   | O     |        | Date/Time of Birth                                                                                                                                     | Date of Birth                                                                                                                                                                                                                             |
|     8 |     1 | IS   | O     |   0001 | Administrative Sex                                                                                                                                     | Sex                                                                                                                                                                                                                                       |
|     9 |   250 | XPN  | NS    |        | Patient Alias                                                                                                                                          | Not used. Alias is passed in PID-5                                                                                                                                                                                                        |
|    10 |   250 | CE   | O     |   0005 | Race                                                                                                                                                   | Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.                                                                                                                      |
|    11 |   250 | XAD  | O     |        | Patient Address                                                                                                                                        | P=Permanent Address~N=Place of Birth~Confidential Address                                                                                                                                                                                 |
|    12 |     4 | IS   | O     |   0289 | County Code                                                                                                                                            | County                                                                                                                                                                                                                                    |
|    13 |   250 | XTN  | O     |        | Phone Number – Home                                                                                                                                    | Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email                                                                                                                                                                                 |
|    14 |   250 | XTN  | O     |        | Phone Number – Business                                                                                                                                | Work Phone (backward compatibility)                                                                                                                                                                                                       |
|    15 |   250 | CE   | NS    |   0296 | Primary Language                                                                                                                                       | Not used                                                                                                                                                                                                                                  |
|    16 |   250 | CE   | O     |   0002 | Marital Status                                                                                                                                         | Marital Status^^^^^^M                                                                                                                                                                                                                     |
|    17 |   250 | CE   | O     |   0006 | Religion                                                                                                                                               | Religious Preference (code)                                                                                                                                                                                                               |
|    18 |   250 | CX   | NS    |        | Patient Account Number                                                                                                                                 | Not used                                                                                                                                                                                                                                  |
|    19 |    16 | ST   | R     |        | SSN Number – Patient                                                                                                                                   | SSN                                                                                                                                                                                                                                       |
|    20 |    25 | DLN  | NS    |        | Driver’s License Number – Patient                                                                                                                      | Not used                                                                                                                                                                                                                                  |
|    21 |   250 | CX   | NS    |        | Mother’s Identifier                                                                                                                                    | Not used                                                                                                                                                                                                                                  |
|    22 |   250 | CE   | O     |   0189 | Ethnic Group                                                                                                                                           | Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC                                                                                                                                                                              |
|       |       |      |       |        |                                                                                                                                                        | See Appendix A for coded values. 2186 and CDC are hardcoded.                                                                                                                                                                              |
|    23 |   250 | ST   | O     |        | Birthplace                                                                                                                                             | Place of birth city and place of birth state                                                                                                                                                                                              |
|    24 |     1 | ID   | O     |   0136 | Multiple Birth Indicator                                                                                                                               | Multiple Birth Indicator [Y for multiple birth]                                                                                                                                                                                           |

- HCPS will only send the original information in the initial REF^I12 from VistA for sequences 1, 2, 3, 5, and 19.

Refer to Table 14-30.

Table 14-30: RRI\_I13 DG1 – Diagnosis Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name            | VistA Description                                                        |
|-------|-------|------|-------|--------|-------------------------|--------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – DG1            | 1                                                                        |
|     2 |     2 | ID   | NS    |        | Diagnosis Coding Method | Not used                                                                 |
|     3 |   250 | CE   | R     |        | Diagnosis Code – DG1    | Provisional Diagnosis Code^Diagnosis Description from File 123, field 30 |
|     4 |    40 | ST   | B     |        | Diagnosis Description   | Not Used                                                                 |
|     5 |    26 | TS   | O     |        | Diagnosis Date/Time     | Not Used                                                                 |
|     6 |     2 | IS   | R     |   0052 | Diagnosis Type          | “W” - Working                                                            |

- DG1 fields past DG1.6 are not used and not shown to save space.

Refer to Table 14-31.

Table 14-31: RRI\_I13 OBR – Observation Request Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   | TBL#   | Element Name                 | VistA Description                                                                                                                                 |
|-------|-------|------|-------|--------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – OBR                 | 1                                                                                                                                                 |
|     2 |    22 | EI   | R     |        | Placer Order Number          | Order entry internal number;Orderable Item entry^OR from File 123, field .03                                                                      |
|     3 |    22 | EI   | R     |        | Filler Order Number          | Consult entry internal number;GMRC^GMRC for all comments and TIU note internal entry number; TIU^TIU for all signed progress notes and addendums. |
|     4 |   250 | CE   | R     |        | Universal Service Identifier | Hardcoded value of “ZZ”                                                                                                                           |
|     5 |     2 | ID   | NS    |        | Priority – OBR               | Not used                                                                                                                                          |
|     6 |    26 | TS   | O     |        | Requested Date/Time          | Clinically Indicated Date from File 123, field 17                                                                                                 |

- OBR fields past OBR.6 are not used and not shown to save space.

Refer to Table 14-32. The PV1 segment data is created using the IN5^VADPT call to determine current inpatient status. See PIMS technical manual for definition of the returned array VAIP. Fields not returned by the IN5^VADPT API are not used in the PV1 segment.

Table 14-32: RRI\_I13 PV1 – Patient Visit Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name              | VistA Description                                      |
|-------|-------|------|-------|--------|---------------------------|--------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PV1              | 1                                                      |
|     2 |     1 | IS   | R     |   0004 | Patient Class             | I: inpatient O: outpatient                             |
|     3 |    80 | PL   | O     |        | Assigned Patient Location | Location of last inpatient movement event from VAIP(5) |
|     4 |     2 | IS   | NS    |        | Admission Type            | Not used                                               |
|     5 |   250 | CX   | NS    |        | Preadmit Number           | Not used                                               |
|     6 |    80 | PL   | NS    |        | Prior Patient Location    | Not used                                               |
|     7 |   250 | XCN  | O     |   0010 | Attending Doctor          | Attending Provider from VAIP(18  )                     |
|     8 |   250 | XCN  | O     |   0010 | Referring Doctor          | Not used (Referring provider sent in PRD segment)      |
|     9 |   250 | XCN  | NS    |        | Consulting Doctor         | Not used                                               |
|    10 |     3 | IS   | NS    |        | Hospital Service          | Not used                                               |
|    11 |    80 | PL   | NS    |        | Temporary Location        | Not used                                               |
|    12 |     2 | IS   | NS    |        | Preadmit Test Indicator   | Not used                                               |
|    13 |     2 | IS   | NS    |        | Re-admission Indicator    | Not used                                               |
|    14 |     6 | IS   | NS    |        | Admit Source              | Not used                                               |
|    15 |     2 | IS   | NS    |        | Ambulatory Status         | Not used                                               |
|    16 |     2 | IS   | O     |   0099 | VIP Indicator             | R if patient restricted/sensitive                      |
|    17 |   250 | XCN  | O     |   0010 | Admitting Doctor          | Primary Physician for admission from VAIP(13,5)        |

Note the following:

- HCPS will only send the original information in the initial REF^I12 from VistA for sequences 1 and 2.
- PV1 fields past PV1.17 are not used and not shown to save space.

Refer to Table 14-33.

Table 14-33: RRI\_I13 NTE – Notes and Comments Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name      | VistA Description                                                                                                                                                                                                                                                                                                                                                         |
|-------|-------|------|-------|--------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | O     |        | Set ID – NTE      | Sequential Number 1-n                                                                                                                                                                                                                                                                                                                                                     |
|     2 |     8 | ID   | O     |   0105 | Source of Comment | P for Placer L for Ancillary                                                                                                                                                                                                                                                                                                                                              |
|     3 | 65536 | FT   | O     |        | Comment           | Based on message type, Resubmitted consults messages (RF1.1= IP^RESUBMITTED) will contain Reason for Request from file 123, field 20  , Completed or Addended (RF1.1= CM^COMPLETE CM^ADDENDED) will contain TIU Progress Note from file 8925 (signed notes/addendums only).  All other I13 messages will contain Activity Comments from file 123, subfile 123.25 field 5. |
|     4 |   250 | CE   | O     |        | Comment Type      | Not used.                                                                                                                                                                                                                                                                                                                                                                 |

- HCPS will send Notes/Comments/Status changes made in the Referral in HCPS.

Refer to Figure 14-8.

Figure 14-8: Receive Referral Example

<!-- image -->

Refer to Figure 14-9.	 Note no comment is entered during Schedule denotes no NTE segment sent.

Figure 14-9: Schedule Referral Example

<!-- image -->

Refer to Figure 14-10.

Figure 14-10: Comment Referral Example

<!-- image -->

Refer to Figure 14-11.

Figure 14-11: Complete Referral Example

<!-- image -->

### REF\_I14 Message Definition Tables

The MSH - Message Header Segment is generated by the VistA HL7 package using the HL7 Application and Protocol entries for the GMRC components.

Refer to Table 14-34.

Table 14-34: REF\_I14 MSH - Message Header Segment

|   SEQ |   LEN | DT   | R/O   | TBL#      | Element Name                    | VistA Description                                                                              |
|-------|-------|------|-------|-----------|---------------------------------|------------------------------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |           | Field Separator                 | &#124;                                                                                         |
|     2 |     4 | ST   | R     |           | Encoding Characters             | ^~\&                                                                                           |
|     3 |    15 | ST   | R     |           | Sending Application             | GMRC HCP SEND                                                                                  |
|     4 |    20 | ST   | R     |           | Sending Facility                | Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND      |
|     5 |    30 | ST   | R     |           | Receiving Application           | GMRC HCP RECEIVE                                                                               |
|     6 |    30 | ST   | NS    |           | Receiving Facility              | Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE |
|     7 |    26 | TS   | R     |           | Date/Time Of Message            | System date/time generated by the VistA HL7 package                                            |
|     8 |    40 | ST   | NS    |           | Security                        | Not used                                                                                       |
|     9 |     7 | CM   | R     | 0076 0003 | Message Type                    | REF^I14                                                                                        |
|    10 |    20 | ST   | R     |           | Message Control ID              | Facility and sequence number automatically generated by the VistA HL7 Package                  |
|    11 |     1 | ID   | R     |           | Processing ID                   | P for Production, T for Test                                                                   |
|    12 |     8 | ID   | R     | 0104      | Version ID                      | 2.	5                                                                                                |
|    13 |    15 | NM   | NS    |           | Sequence Number                 | Not used                                                                                       |
|    14 |   180 | ST   | NS    |           | Continuation Pointer            | Not used                                                                                       |
|    15 |     2 | ID   | R     | 0155      | Accept Acknowledgment Type      | AL=Always                                                                                      |
|    16 |     2 | ID   | R     | 0155      | Application Acknowledgment Type | AL=Always                                                                                      |
|    17 |     3 | ID   | R     | 0399      | Country Code                    | USA                                                                                            |

Refer to Table 14-35.

Table 14-35: REF\_I14 RF1 – Referral Information Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                    | VistA Description                                                                                                                                                        |
|-------|-------|------|-------|--------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | O     |   0283 | Referral Status                 | CA^CANCELLED DC^DISCONTINUED                                                                                                                                             |
|     2 |   250 | CE   | O     |   0280 | Referral Priority               | From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS |
|     3 |   250 | CE   | O     |        | Referral Type                   | Service IEN^Service Name^^Template IEN ^Template Name Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.                                        |
|     4 |   250 | CE   | NS    |        | Referral Disposition            | Not used.                                                                                                                                                                |
|     5 |   250 | CE   | O     |   0284 | Referral Category               | I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.            |
|     6 |    30 | EI   | R     |        | Originating Referral Identifier | IEN to File 123                                                                                                                                                          |
|     7 |    26 | TS   | O     |        | Effective Date                  | Referral Date of Request from File 123, field .01                                                                                                                        |
|     8 |    26 | TS   | NS    |        | Expiration Date                 | Not used                                                                                                                                                                 |
|     9 |    26 | TS   | NS    |        | Process Date                    | Not used                                                                                                                                                                 |
|    10 |   250 | CE   | NS    |        | Referral Reason                 | Not used                                                                                                                                                                 |
|    11 |    30 | EI   | NS    |        | External Referral Identifier    | Not used                                                                                                                                                                 |

Refer to Table 14-36.

Table 14-36: REF\_I14 PRD – Provider Data Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                          | VistA Description                                                                                                 |
|-------|-------|------|-------|--------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|     1 |   250 | CE   | R     |   0286 | Provider Role                         | RP  for Referring Provider                                                                                        |
|     2 |   250 | XPN  | O     |        | Provider Name                         | Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ Provider from File 123, field 10 |
|     3 |   250 | XAD  | O     |        | Provider Address                      | Street Address 1^Street Address 2^City^State^Zip from File 200, fields .111, .112, .114, .115, .116               |
|     4 |    60 | PL   | NS    |        | Provider Location                     | Not used                                                                                                          |
|     5 |   250 | XTN  | O     |        | Provider Communication Information    | ^^^Email Address^^Office Phone Area Code^Office Phone Number from File 200, fields .151, .132                     |
|     6 |   250 | CE   | NS    |        | Preferred Method of Contact           | Not used                                                                                                          |
|     7 |   100 | PLN  | NS    |        | Provider Identifiers                  | Not used                                                                                                          |
|     8 |    26 | TS   | NS    |        | Effective Start Date of Provider Role | Not used                                                                                                          |
|     9 |    26 | TS   | NS    |        | Effective End Date of Provider Role   | Not used                                                                                                          |

Refer to Table 14-37. Note REF\_I14 PID – Patient Id Segment is generated by the VistA API.

Table 14-37: REF\_I14 PID – Patient Id Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                      | VistA Description                                                                                                                                                                                                                         |
|-------|-------|------|-------|--------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PID                      | Sequential Number                                                                                                                                                                                                                         |
|     2 |    20 | CX   | R     |        | Patient ID                        | ICN, including V checksum for backwards compatibility.                                                                                                                                                                                    |
|     3 |   250 | CX   | R     |        | Patient Identifier List (list is not in any specified order) Following are PID.3.	5 Identifier Codes: NI=ICN,  PI=Patient DFN, SS=SSN  PN=Claim Number                                   | Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (PID-5). |
|     4 |    20 | CX   | NS    |        | Alternate Patient ID – PID        | Not used                                                                                                                                                                                                                                  |
|     5 |   250 | XPN  | R     |        | Patient Name                      | Patient Name and all Alias entries                                                                                                                                                                                                        |
|     6 |   250 | XPN  | O     |        | Mother’s Maiden Name              | Mother’s Maiden Name                                                                                                                                                                                                                      |
|     7 |    26 | TS   | O     |        | Date/Time of Birth                | Date of Birth                                                                                                                                                                                                                             |
|     8 |     1 | IS   | O     |   0001 | Administrative Sex                | Sex                                                                                                                                                                                                                                       |
|     9 |   250 | XPN  | NS    |        | Patient Alias                     | Not used. Alias is passed in PID-5                                                                                                                                                                                                        |
|    10 |   250 | CE   | O     |   0005 | Race                              | Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.                                                                                                                      |
|    11 |   250 | XAD  | O     |        | Patient Address                   | P=Permanent Address~N=Place of Birth~Confidential Address                                                                                                                                                                                 |
|    12 |     4 | IS   | O     |   0289 | County Code                       | County                                                                                                                                                                                                                                    |
|    13 |   250 | XTN  | O     |        | Phone Number – Home               | Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email                                                                                                                                                                                 |
|    14 |   250 | XTN  | O     |        | Phone Number – Business           | Work Phone (backward compatibility)                                                                                                                                                                                                       |
|    15 |   250 | CE   | NS    |   0296 | Primary Language                  | Not used                                                                                                                                                                                                                                  |
|    16 |   250 | CE   | O     |   0002 | Marital Status                    | Marital Status^^^^^^M                                                                                                                                                                                                                     |
|    17 |   250 | CE   | O     |   0006 | Religion                          | Religious Preference (code)                                                                                                                                                                                                               |
|    18 |   250 | CX   | NS    |        | Patient Account Number            | Not used                                                                                                                                                                                                                                  |
|    19 |    16 | ST   | R     |        | SSN Number – Patient              | SSN                                                                                                                                                                                                                                       |
|    20 |    25 | DLN  | NS    |        | Driver’s License Number – Patient | Not used                                                                                                                                                                                                                                  |
|    21 |   250 | CX   | NS    |        | Mother’s Identifier               | Not used                                                                                                                                                                                                                                  |
|    22 |   250 | CE   | O     |   0189 | Ethnic Group                      | Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC  See Appendix A for coded values. 2186 and CDC are hardcoded.                                                                                                                |
|    23 |   250 | ST   | O     |        | Birthplace                        | Place of birth city and place of birth state                                                                                                                                                                                              |
|    24 |     1 | ID   | O     |   0136 | Multiple Birth Indicator          | Multiple Birth Indicator [Y for multiple birth]                                                                                                                                                                                           |

- PID fields past PID.24 are not used and are not shown to save space.

Refer to Table 14-38.

Table 14-38: REF\_I14 DG1 - Diagnosis Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name            | VistA Description                                                        |
|-------|-------|------|-------|--------|-------------------------|--------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – DG1            | 1                                                                        |
|     2 |     2 | ID   | NS    |        | Diagnosis Coding Method | Not used                                                                 |
|     3 |   250 | CE   | R     |        | Diagnosis Code – DG1    | Provisional Diagnosis Code^Diagnosis Description from File 123, field 30 |
|     4 |    40 | ST   | B     |        | Diagnosis Description   | Not used                                                                 |
|     5 |    26 | TS   | O     |        | Diagnosis Date/Time     | Not used                                                                 |
|     6 |     2 | IS   | R     |   0052 | Diagnosis Type          | “W” - Working                                                            |

- DG1 fields past DG1.6 are not used and are not shown to save space.

Refer to Table 14-39.

Table 14-39: REF\_I14 OBR – Observation Request Segment (Same for all message types)

|   SEQ |   LEN | DT   | R/O   | TBL#   | Element Name                 | VistA Description                                                            |
|-------|-------|------|-------|--------|------------------------------|------------------------------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – OBR                 | 1                                                                            |
|     2 |    22 | EI   | R     |        | Placer Order Number          | Order entry internal number;Orderable Item entry^OR from File 123, field .03 |
|     3 |    22 | EI   | R     |        | Filler Order Number          | Consult entry internal number;GMRC^GMRC                                      |
|     4 |   250 | CE   | NS    |        | Universal Service Identifier | Hardcoded value of “ZZ”                                                      |
|     5 |     2 | ID   | NS    |        | Priority – OBR               | Not used                                                                     |
|     6 |    26 | TS   | O     |        | Requested Date/Time          | Clinically Indicated Date from File 123, field 17                            |

Note the following:

- OBR fields past OBR.6 are not used and not shown to save space.
- REF\_I14 PV1 – Patient Visit Segment (same for all message types)
- The PV1 segment data is created using the IN5^VADPT call to determine current inpatient status. See PIMS technical manual for definition of the returned array VAIP.
- Fields not returned by the IN5^VADPT API are not used in the PV1 segment.

Refer to Table 14-40.

Table 14-40: REF\_14 PV1 – Patient Visit Segment (Same for all message types

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name              | VistA Description                                      |
|-------|-------|------|-------|--------|---------------------------|--------------------------------------------------------|
|     1 |     4 | SI   | R     |        | Set ID – PV1              | 1                                                      |
|     2 |     1 | IS   | R     |   0004 | Patient Class             | I: inpatient O: outpatient                             |
|     3 |    80 | PL   | O     |        | Assigned Patient Location | Location of last inpatient movement event from VAIP(5) |
|     4 |     2 | IS   | NS    |        | Admission Type            | Not used                                               |
|     5 |   250 | CX   | NS    |        | Preadmit Number           | Not used                                               |
|     6 |    80 | PL   | NS    |        | Prior Patient Location    | Not used                                               |
|     7 |   250 | XCN  | O     |   0010 | Attending Doctor          | Attending Provider from VAIP(18  )                     |
|     8 |   250 | XCN  | NS    |        | Referring Doctor          | Not used (Referring provider sent in PRD segment)      |
|     9 |   250 | XCN  | NS    |        | Consulting Doctor         | Not used                                               |
|    10 |     3 | IS   | NS    |        | Hospital Service          | Not used                                               |
|    11 |    80 | PL   | NS    |        | Temporary Location        | Not used                                               |
|    12 |     2 | IS   | NS    |        | Preadmit Test Indicator   | Not used                                               |
|    13 |     2 | IS   | NS    |        | Re-admission Indicator    | Not used                                               |
|    14 |     6 | IS   | NS    |        | Admit Source              | Not used                                               |
|    15 |     2 | IS   | NS    |        | Ambulatory Status         | Not used                                               |
|    16 |     2 | IS   | O     |   0099 | VIP Indicator             | R if patient restricted/sensitive                      |
|    17 |   250 | XCN  | O     |   0010 | Admitting Doctor          | Primary Physician for admission from VAIP(13,5)        |

- PV1 fields past PV1.17 are not used and are not shown to save space.

Refer to Table 14-41.

Table 14-41: REF\_I14 NTE – Notes and Comments Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name      | VistA Description                                       |
|-------|-------|------|-------|--------|-------------------|---------------------------------------------------------|
|     1 |     4 | SI   | O     |        | Set ID – NTE      | Sequential Number 1-n                                   |
|     2 |     8 | ID   | O     |   0105 | Source of Comment | L for Ancillary                                         |
|     3 | 65536 | FT   | O     |        | Comment           | Activity Comments from file 123, subfile 123.25 field 5 |
|     4 |   250 | CE   | O     |        | Comment Type      | Not used.                                               |

Refer to Figure 14-12.

Figure 14-12: Cancel Referral Example

<!-- image -->

Refer to Figure 14-13. Note that no DX is entered during order entry and no DG1 segment is sent. Also note the example shows PID with more fields, Sensitive Patient.

Figure 14-13: Discontinue Referral Example

<!-- image -->

### REF\_IN Message Definition Tables

Refer to Table 14-42.

Table 14-42: REF\_IN1 Segment (Valid for all above REF messages)

|   SEQ |   LEN | DT            | R/O   | TBL#   | Element Name                 | VistA Description                 |
|-------|-------|---------------|-------|--------|------------------------------|-----------------------------------|
|     1 |     4 |               | R     |        | SetIDIN1                     | Set ID - IN1 XE "1                |
|     2 |   250 | Coded element | R     |        | InsurancePlanID              | Insurance Plan ID                 |
|     3 |   250 | ID            | R     |        | InsuranceCompanyID           | Insurance Company ID              |
|     4 |   250 | string        | O     |        | InsuranceCompanyName         | Insurance Company Name            |
|     5 |   250 | address       | O     |        | InsuranceCompanyAddress      | Insurance Company Address         |
|     6 |   250 | string        | O     |        | InsuranceCoContactPerson     | Insurance Co Contact Person       |
|     7 |   250 | string        | O     |        | InsuranceCoPhoneNumber       | Insurance Co Phone Number         |
|     8 |    12 | string        | O     |        | GroupNumber                  | Group Number                      |
|     9 |   250 | string        | O     |        | GroupName                    | Group Name                        |
|    10 |   250 | string        | O     |        | InsuredsGroupEmpID           | Insured's Group Emp ID            |
|    11 |   250 | string        | O     |        | InsuredsGroupEmpName         | Insured's Group Emp Name          |
|    12 |     8 | date          | O     |        | PlanEffectiveDate            | Plan Effective Date               |
|    13 |     8 | date          | O     |        | PlanExpirationDate           | Plan Expiration Date              |
|    14 |   239 | string        | O     |        | AuthorizationInformation     | Authorization Information         |
|    15 |     3 | string        | O     |        | PlanType                     | Plan Type                         |
|    16 |   250 | string        | O     |        | NameOfInsured                | Name Of Insured                   |
|    17 |   250 | string        | O     |        | InsuredsRelationshipToPatien | Insured's Relationship To Patient |
|    18 |    26 | date          | O     |        | InsuredsDateOfBirth          | Insured's Date Of Birth           |
|    19 |   250 | address       | O     |        | InsuredsAddress              | Insured's Address                 |
|    20 |     2 | string        | O     |        | AssignmentOfBenefits         | Assignment Of Benefits            |
|    21 |     2 | string        | O     |        | CoordinationOfBenefits       | Coordination Of Benefits          |
|    22 |     2 | string        | O     |        | CoordOfBenPriority           | Coord Of Ben. Priority            |
|    23 |     1 | string        | O     |        | NoticeOfAdmissionFlag        | Notice Of Admission Flag          |
|    24 |     8 | date          | O     |        | NoticeOfAdmissionDate        | Notice Of Admission Date          |
|    25 |     1 | string        | O     |        | ReportOfEligibilityFlag      | Report Of Eligibility Flag        |
|    26 |     8 | date          | O     |        | ReportOfEligibilityDate      | Report Of Eligibility Date        |
|    27 |     2 | string        | O     |        | ReleaseInformationCode       | Release Information Code          |
|    28 |    15 | string        | O     |        | PreAdmitCertPAC              | Pre-Admit Cert (PAC)              |
|    29 |    26 | date          | O     |        | VerificationDateTime         | Verification Date/Time            |
|    30 |   250 | string        | O     |        | VerificationBy               | Verification By                   |
|    31 |     2 | string        | O     |        | TypeOfAgreementCode          | Type Of Agreement Code            |
|    32 |     2 | string        | O     |        | BillingStatus                | Billing Status                    |
|    33 |     4 | number        | O     |        | LifetimeReserveDays          | Lifetime Reserve Days             |
|    34 |     4 | number        | O     |        | DelayBeforeLRDay             | Delay Before L.R. Day             |
|    35 |     8 | string        | O     |        | CompanyPlanCode              | Company Plan Code                 |
|    36 |    15 | string        | O     |        | PolicyNumber                 | Policy Number                     |
|    37 |    12 | number        | O     |        | PolicyDeductible             | Policy Deductible                 |
|    38 |    12 | number        | B     |        | PolicyLimitAmount            | Policy Limit - Amount             |
|    39 |     4 | number        | O     |        | PolicyLimitDays              | Policy Limit - Days               |
|    40 |    12 | number        | B     |        | RoomRateSemiPrivate          | Room Rate - Semi-Private          |
|    41 |    12 | number        | B     |        | RoomRatePrivate              | Room Rate - Private               |
|    42 |   250 | string        | O     |        | InsuredsEmploymentStatus     | Insured's Employment Status       |
|    43 |     1 | string        | O     |        | InsuredsAdministrativeSex    | Insured's Administrative Sex      |
|    44 |   250 | address       | O     |        | InsuredsEmployersAddress     | Insured's Employer's Address      |
|    45 |     2 | string        | O     |        | VerificationStatus           | Verification Status               |
|    46 |     8 | string        | O     |        | PriorInsurancePlanID         | Prior Insurance Plan ID           |
|    47 |     3 | string        | O     |        | CoverageType                 | Coverage Type                     |
|    48 |     2 | string        | O     |        | Handicap                     | Handicap                          |
|    49 |   250 | ID            | O     |        | InsuredsIDNumber             | Insured's ID Number               |
|    50 |     1 | string        | O     |        | SignatureCode                | Signature Code                    |
|    51 |     8 | date          | O     |        | SignatureCodeDate            | Signature Code Date               |
|    52 |   250 | string        | O     |        | InsuredsBirthPlace           | Insured's Birth Place             |
|    53 |     2 | string        | O     |        | VIPIndicator                 | VIP Indicator                     |

Refer to Table 14-43.

Table 14-43: REF\_IN3 Segment (Valid for all above REF messages)

|   SEQ |   LEN | DT     | R/O   | TBL#   | Element Name                 | VistA Description                     |
|-------|-------|--------|-------|--------|------------------------------|---------------------------------------|
|     1 |     4 |        | R     |        | SetIDIN3                     | Set ID - IN3 XE "1                    |
|     2 |   250 | string | O     |        | CertificationNumber          | Certification Number                  |
|     3 |   250 | string | O     |        | CertifiedBy                  | Certified By                          |
|     4 |     1 | string | O     |        | CertificationRequired        | Certification Required                |
|     5 |    23 | string | O     |        | Penalty                      | Penalty                               |
|     6 |    26 | date   | O     |        | CertificationDateTime        | Certification Date/Time               |
|     7 |    26 | date   | O     |        | CertificationModifyDateTime  | Certification Modify Date/Time        |
|     8 |   250 | string | O     |        | Operator                     | Operator                              |
|     9 |     8 | date   | O     |        | CertificationBeginDate       | Certification Begin Date              |
|    10 |     8 | date   | O     |        | CertificationEndDate         | Certification End Date                |
|    11 |     6 | number | O     |        | Days                         | Days                                  |
|    12 |   250 | string | O     |        | NonConcurCodeDescription     | Non-Concur Code/Description           |
|    13 |    26 | date   | O     |        | NonConcurEffectiveDateTime   | Non-Concur Effective Date/Time        |
|    14 |   250 | string | O     |        | PhysicianReviewer            | Physician Reviewer                    |
|    15 |    48 | string | O     |        | CertificationContact         | Certification Contact                 |
|    16 |   250 | string | O     |        | CertificationContactPhoneNum | Certification Contact Phone Number    |
|    17 |   250 | string | O     |        | AppealReason                 | Appeal Reason                         |
|    18 |   250 | string | O     |        | CertificationAgency          | Certification Agency                  |
|    19 |   250 | string | O     |        | CertificationAgencyPhoneNumb | Certification Agency Phone Number     |
|    20 |    40 | string | O     |        | PreCertificationRequirement  | Pre-Certification Requirement         |
|    21 |    48 | string | O     |        | CaseManager                  | Case Manager                          |
|    22 |     8 | date   | O     |        | SecondOpinionDate            | Second Opinion Date                   |
|    23 |     1 | string | O     |        | SecondOpinionStatus          | Second Opinion Status                 |
|    24 |     1 | string | O     |        | SecondOpinionDocumentationRe | Second Opinion Documentation Received |
|    25 |   250 | string | O     |        | SecondOpinionPhysician       | Second Opinion Physician              |

### HL7 ACK Messages

Patch GMRC*3.0*75 added the ability to use the following HL7 ACK messages to enable communications between the consult system communication with the Healthcare Claims Processing System (HCPS). Accept Acknowledgment (AA) will be sent for messages that are parsed correctly and sent to HCPS. Application Error (AE) will be sent when a parsing issue is discovered, such as missing a required field.

HL7 v2.5 ACK messages will be sent to HCPS in enhanced mode, as follows:

- Commit accept (CA) in MSA-1 acknowledgment code if the message can be accepted for processing
- Commit reject (CR) in MSA-1 acknowledgment code if one of the values of MSH-9 message type, MSH-12 version ID or MSH-11 processing ID is not acceptable to the receiving application
- Commit error (CE) in MSA-1 acknowledgment code if the message cannot be accepted for any other reason

A standard HL7 v2.5 ACK message will be returned by HCPS for each consult message received. Refer to Table 14-44, which lists the three standard ACK message segments.

Table 14-44: Standard ACK Message Segments

| Segment   | Segment Name           | Optional/Required   |
|-----------|------------------------|---------------------|
| MSH       | Message Header         | REQUIRED            |
| MSA       | Message Acknowledgment | REQUIRED            |
| ERR       | Error                  | OPTIONAL            |

The following tables contain the HL7 message definition for the ACK messages.

The table columns are as follows:

1. SEQ = HL7 sequence#
2. LEN = HL7 field length
3. DT = HL7 data type
4. R/O = R=Require, O=Optional, C=Conditional, NS=Not supported
5. TBL = HL7 table definition
6. Element Name = HL7 field name
7. VistA Description = information on what will be pulled from VistA for this element, or hard-coded data.

For ease of reference, refer to Figure 14-14.

Figure 14-14: HL7 ACK Message Table Headings

<!-- image -->

Refer to Table 14-45.

Table 14-45: ACK MSH - Message Header Segment

|   SEQ |   LEN | DT   | R/O   | TBL#      | Element Name                    | Description                                                                |
|-------|-------|------|-------|-----------|---------------------------------|----------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |           | Field Separator                 | &#124;                                                                     |
|     2 |     4 | ST   | R     |           | Encoding Characters             | ~^\&                                                                       |
|     3 |    15 | ST   | R     |           | Sending Application             | GMRC HCP RECEIVE                                                           |
|     4 |    20 | ST   | R     |           | Sending Facility                | Sending Facility                                                           |
|     5 |    30 | ST   | R     |           | Receiving Application           | GMRC HCP SEND                                                              |
|     6 |    30 | ST   | NS    |           | Receiving Facility              | Receiving Facility                                                         |
|     7 |    26 | TS   | R     |           | Date/Time Of Message            | System date/time                                                           |
|     8 |    40 | ST   | NS    |           | Security                        | Not used                                                                   |
|     9 |     7 | CM   | R     | 0076 0003 | Message Type                    | ACK                                                                        |
|    10 |    20 | ST   | R     |           | Message Control ID              | Return the Message Control ID from the REF^I1n message received from VistA |
|    11 |     1 | ID   | R     |           | Processing ID                   | P for Production, T for Test                                               |
|    12 |     8 | ID   | R     | 0104      | Version ID                      | 2.	5                                                                            |
|    13 |    15 | NM   | NS    |           | Sequence Number                 | Not used                                                                   |
|    14 |   180 | ST   | NS    |           | Continuation Pointer            | Not used                                                                   |
|    15 |     2 | ID   | R     | 0155      | Accept Acknowledgment Type      | AL                                                                         |
|    16 |     2 | ID   | R     | 0155      | Application Acknowledgment Type | NE                                                                         |
|    17 |     3 | ID   | R     | 0399      | Country Code                    | USA                                                                        |

Refer to Table 14-46.

Table 14-46: ACK MSH - Message Header Segment

|   SEQ |   LEN | DT   | R/O   | TBL#      | Element Name                    | Description                                                                |
|-------|-------|------|-------|-----------|---------------------------------|----------------------------------------------------------------------------|
|     1 |     1 | ST   | R     |           | Field Separator                 | &#124;                                                                     |
|     2 |     4 | ST   | R     |           | Encoding Characters             | ~^\&                                                                       |
|     3 |    15 | ST   | R     |           | Sending Application             | GMRC HCP RECEIVE                                                           |
|     4 |    20 | ST   | R     |           | Sending Facility                | Sending Facility                                                           |
|     5 |    30 | ST   | R     |           | Receiving Application           | GMRC HCP SEND                                                              |
|     6 |    30 | ST   | NS    |           | Receiving Facility              | Receiving Facility                                                         |
|     7 |    26 | TS   | R     |           | Date/Time Of Message            | System date/time                                                           |
|     8 |    40 | ST   | NS    |           | Security                        | Not used                                                                   |
|     9 |     7 | CM   | R     | 0076 0003 | Message Type                    | ACK                                                                        |
|    10 |    20 | ST   | R     |           | Message Control ID              | Return the Message Control ID from the REF^I1n message received from VistA |
|    11 |     1 | ID   | R     |           | Processing ID                   | P for Production, T for Test                                               |
|    12 |     8 | ID   | R     | 0104      | Version ID                      | 2.	5                                                                            |
|    13 |    15 | NM   | NS    |           | Sequence Number                 | Not used                                                                   |
|    14 |   180 | ST   | NS    |           | Continuation Pointer            | Not used                                                                   |
|    15 |     2 | ID   | R     | 0155      | Accept Acknowledgment Type      | AL                                                                         |
|    16 |     2 | ID   | R     | 0155      | Application Acknowledgment Type | NE                                                                         |
|    17 |     3 | ID   | R     | 0399      | Country Code                    | USA                                                                        |

Refer to Table 14-47.

Table 14-47: ACK MSA - Message Acknowledgment Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                | Description                                        |
|-------|-------|------|-------|--------|-----------------------------|----------------------------------------------------|
|     1 |     2 | ID   | R     |   0008 | Acknowledgment Code         | AA for Application Accept AE for Application Error |
|     2 |    20 | ST   | R     |        | Message Control ID          | Same as MSH.10 above                               |
|     3 |    80 | ST   | NS    |        | Text Message                | Not supported                                      |
|     4 |    15 | NM   | NS    |        | Expected Sequence Number    | Not used                                           |
|     5 |       |      | NS    |        | Delayed Acknowledgment Type | Not used                                           |
|     6 |   250 | CE   | NS    |        | Error Condition             | Not used                                           |

Refer to Table 14-48.

Table 14-48: ACK ERR - Error Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name            | Description                                                   |
|-------|-------|------|-------|--------|-------------------------|---------------------------------------------------------------|
|     1 |   493 | ELD  | NS    |        | Error Code and Location | Not used                                                      |
|     2 |    18 | ERL  | O     |        | Error Location          | Segment^Sequence^Field^Fld Repetition^Component^Sub-component |
|     3 |   705 | CWE  | R     |   0357 | HL7 Error Code          | Value^Description  See table 0357 below.                      |

- ERR fields past ERR.3 are not used and are not shown to save space.

Refer to Table 14-49.

Table 14-49: HL7 Table 0357 - Message Error Condition Codes

|   Value | Description                | Comment                                                                                                                                             |
|---------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|       0 | Message Accepted           | Success. Optional, as the AA conveys success. Used for systems that must always return a status code.                                               |
|     100 | Segment Sequence Error     | Error: The message segments were not in proper order, or required segments are missing.                                                             |
|     101 | Required Field Missing     | Error: A required field is missing from a segment.                                                                                                  |
|     102 | Data Type Error            | Error: The field contained data of the wrong data type, e.g., an NM field contained “FOO”.                                                          |
|     103 | Table Value Not Found      | Error: A field of data type ID or IS was compared against the corresponding table, and no match was found.                                          |
|     200 | Unsupported Message Type   | Rejection: The Message Type is not supported.                                                                                                       |
|     201 | Unsupported Event Code     | Rejection: The Event Code is not supported.                                                                                                         |
|     202 | Unsupported Processing ID  | Rejection: The Processing ID is not supported.                                                                                                      |
|     203 | Unsupported Version ID     | Rejection: The Version ID is not supported.                                                                                                         |
|     204 | Unknown Key Identifier     | Rejection: The ID of the patient, order, etc., was not found. Used for transactions other than additions, e.g., transfer of a non-existent patient. |
|     205 | Duplicate Key Identifier   | Rejection: The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.)                   |
|     206 | Application Record Locked  | Rejection: The transaction could not be performed at the application storage level, e.g., database locked.                                          |
|     207 | Application Internal Error | Rejection: A catchall for internal errors not explicitly covered by other codes.                                                                    |

For the Application NACK that GMRC *3.0*123 returns  for Errors  during processing of the REF I13/I14 messages, the MSA segment will be populated as  shown in Table 14-50 below.

Table 14-50: MSA Message for NACK – Negative Application Acknowledgment Segment

|   SEQ |   LEN | DT   | R/O   |   TBL# | Element Name                | Description                                                                                                                        |
|-------|-------|------|-------|--------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|     1 |     2 | ID   | R     |   0008 | Acknowledgment Code         | AE for Application Error                                                                                                           |
|     2 |    20 | ST   | R     |        | Message Control ID          | Same as MSH.10 of the Request Message                                                                                              |
|     3 |    80 | ST   | NS    |        | Text Message                | Error Message Description                                                                                                          |
|     4 |    15 | NM   | NS    |        | Expected Sequence Number    | Not used                                                                                                                           |
|     5 |       |      | NS    |        | Delayed Acknowledgment Type | Not used                                                                                                                           |
|     6 |   250 | CE   | NS    |        | Error Condition             | Patient ICN^Patient NAME^Station ID^Consult ID^Date/Time Stamp when the REF I12/I13 Message is being processed on the VistA System |

### HL 7 Mailbox

GMRC HCP HL7 MESSAGE is used to report errors in HL7 message generation and processing for GMRC consults.

### Order Event Messages

Table 14-51 identifies the HL7 fields passed in each kind of event associated with OE/RR. For each event there is an order control code and a set of fields listed. For any given event, however, some of the fields may be empty (observation sub-id, for example).

The protocols identified in the table use OE/RR namespacing conventions. The messages sent by OE/RR will use the OR namespaced protocols indicated. Individual packages may use whatever protocol names they wish.

#### Front Door – Consults

Refer to Table 14-51.

Table 14-51: Front Door – Consults

| Action        | Request from OE/RR                                                                     | Consults Accepts                                          | Consults Rejects                                                                  |
|---------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------|
| Protocol      | OR EVSEND GMRC                                                                         | GMRC EVSEND OR                                            | GMRC EVSEND OR                                                                    |
| Order Control | NW (new order)                                                                         | OK (accepted)                                             | OC (canceled)                                                                     |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5 PV1: 2,3,19  ORC: 1,2,7,10,12,15 OBR: 4,18  ,19  OBX: 1,2,3,5 | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3                      | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,12,15,16 OBR: 4                              |
| Protocol      | OR EVSEND GMRC                                                                         | GMRC EVSEND OR                                            | GMRC EVSEND OR                                                                    |
| Order Control | CA (cancel)  DC (discontinue)  HD (hold)  RL (release)                                 | CR (canceled)  DR (discontinued)  HR (held) OR (released) | UC (unable to cancel) UD (unable to dc)  UH (unable to hold)  OC (order canceled) |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,10,12,15,16                                       | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,5                    | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,16                                           |

Refer to Figure 14-15.

Figure 14-15: Consult Example - Pulmonary Consult at bedside to rule out pneumonia

<!-- image -->

Refer to Figure 14-16.

Figure 14-16: Consult Example -	 	EKG at Bedside

<!-- image -->

Refer to Figure 14-17.

Figure 14-17: Consult Example – Family Counseling

<!-- image -->

### Back Door Consults

Back door orders are handled by sending OE/RR the ORM message for a Consult order with a ‘send number’ order control code. This permits OE/RR to store the order in its database and return the OE/RR order number to consults with a ‘number assigned’ order control code. OE/RR cannot actually reject Consult events. The ‘data errors’ order control code is just used as some way to communicate to Consults that OE/RR could not interpret the ORM message. This should generally not happen. Use of the ‘back door’ by packages for ordering is optional. It is still necessary to post an event when results are available.

Refer to Table 14-52.

Table 14-52: Back Door – Consults

| Action        | Event from Consults                                                                        | OE/RR Accepts                                                              | OE/RR Rejects                           |
|---------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------|
| Protocol      | GMRC EVSEND OR                                                                             | OR EVSEND GMRC                                                             | OR EVSEND GMRC                          |
| Order Control | SN (send number)                                                                           | NA (number assigned)                                                       | DE (data errors)                        |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5  PV1: 2,3,19  ORC: 1,3,7,10,12,15  OBR: 4,18  ,19  OBX: 1,2,3,4,5 | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3                                       | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,3,16   |
|               |                                                                                            |                                                                            |                                         |
| Protocol      | GMRC EVSEND OR                                                                             |                                                                            | OR EVSEND GMRC                          |
| Order Control | OC (cancel)  OD (discontinue)  OH (hold)  RL (release)                                     | There is no return event. OE/RR must accept the instruction from Consults. | DE (data errors)                        |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,12,15,16  OBR: 4                                      |                                                                            | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,16 |
|               |                                                                                            |                                                                            |                                         |
| Protocol      | GMRC EVSEND OR                                                                             |                                                                            | OR EVSEND GMRC                          |
| Order Control | SC (accepted)                                                                              |                                                                            | DE (data errors)                        |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,5,12,15  OBR: 4                                       | There is no return event. OE/RR must accept the instruction from Consults. | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,16 |
|               |                                                                                            |                                                                            |                                         |
| Protocol      | GMRC EVSEND OR                                                                             |                                                                            | OR EVSEND GMRC                          |
| Order Control | XX (forwarded)                                                                             |                                                                            | DE (data errors)                        |
| HL7 Fields    | MSH: 1,2,3,4,9 PID: 3,5 ORC: 1,2,3,7,10,12,15 OBX: 1,2,3,4,5                               | There is no return event. OE/RR must accept the instruction from Consults. | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,16 |
|               |                                                                                            |                                                                            |                                         |
| Protocol      | GMRC EVSEND OR                                                                             |                                                                            | OR EVSEND GMRC                          |
| Order Control | RE (completed)                                                                             |                                                                            | DE (data errors)                        |
| HL7 Fields    | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,12,15  OBR: 4,7,22,25,32  OBX: 1,2,3,4,5,8            | There is no return event. OE/RR must accept the instruction from Consults. | MSH: 1,2,3,4,9  PID: 3,5  ORC: 1,2,3,16 |

Refer to Figure 14-18.

Figure 14-18: Consult Example - Pulmonary Consult at Bedside to Rule Out Pneumonia

<!-- image -->

### Orderable Item Updates – Request Services

When Consults makes request services available for ordering, OE/RR needs to be notified. This is done via a protocol event point which should be defined by Consults. When this event point is invoked, an HL7 master file update message is sent. Information that should be available in this segment is listed in Table 14-53 below.

Table 14-53: Orderable Item Updates – Request Services

| SEG     |   SEQ | Field Name              | Example                        | HL7 Type                                      |
|---------|-------|-------------------------|--------------------------------|-----------------------------------------------|
| MSH     |     1 | Field Separator         | &#124;                         | string                                        |
|         |     2 | Encoding Characters     | ^~\&                           | string                                        |
|         |     3 | Sending Application     | CONSULTS                       | string                                        |
|         |     4 | Sending Facility        | 660                            | string                                        |
|         |     9 | Message Type            | MFN                            | ID                                            |
|         |       |                         |                                |                                               |
| MFI     |     1 | Master File ID          | 123.5^Request Services^99DD    | coded element                                 |
|         |     3 | File-Level Event Code   | REP                            | table 178                                     |
|         |     6 | Response Level Code     | NE                             | table 179                                     |
|         |       |                         |                                |                                               |
| { MFE   |     1 | Record-Level Event Code | MAD                            | table 180                                     |
|         |     4 | Primary Key             | ^^^25^Cardiology Consult^99CON | coded element                                 |
|         |       |                         |                                |                                               |
| ZCS     |     1 | Service Usage           | 2                              | coded value (1=Grouper only, 2=Tracking only) |
|         |       |                         |                                |                                               |
| { ZSY } |     1 | Set ID                  | 1                              | Numeric                                       |
| }       |     2 | Synonym                 | CARD                           | string                                        |

Note the following:

- When doing the initial population of the orderable items file, the File Level Event Code should be REP. After the initial population, subsequent changes should have the UPD code.
- Orderable item updates always originate from Consults.
- There may be multiple MFE segments passed in a single transaction.
- The record-level event code tells whether this transaction is an update, addition, inactivation, etc.
- The primary key is the coded element normally passed when creating an order. By using the coded element, we can know the national and local names for a consult.

Refer to Figure 14-19.

Figure 14-19: Orderable Item Updates Example

<!-- image -->

### Orderable Item Updates - Procedures

When Consults makes procedures available for ordering or inactivates a procedure, OE/RR needs to be notified. This is done via a protocol event point which should be defined by Consults. When this event point is invoked, an HL7 master file update message is sent. Information that should be available in this segment is listed in Table 14-51 below.

Refer to Table 14-54.

Table 14-54: Orderable Item Updates - Procedures

| SEG    |   SEQ | Field Name              | Example                         | HL7 Type      |
|--------|-------|-------------------------|---------------------------------|---------------|
| MSH    |     1 | Field Separator         | &#124;                          | string        |
|        |     2 | Encoding Characters     | ^~\&                            | string        |
|        |     3 | Sending Application     | PROCEDURES                      | string        |
|        |     4 | Sending Facility        | 660                             | string        |
|        |     9 | Message Type            | MFN                             | ID            |
|        |       |                         |                                 |               |
| MFI    |     1 | Master File ID          | 123.3^Procedures^99DD           | coded element |
|        |     3 | File-Level Event Code   | REP                             | table 178     |
|        |     6 | Response Level Code     | NE                              | table 179     |
|        |       |                         |                                 |               |
| { MFE  |     1 | Record-Level Event Code | MAD                             | table 180     |
|        |     4 | Primary Key             | ^^^1225^Electrocardiogram^99PRC | coded element |
|        |       |                         |                                 |               |
| { ZSY} |     1 | Set ID                  | 1                               | numeric       |
| }      |     2 | Synonym                 | EKG                             | string        |

Note the following:

- When doing the initial population of the orderable items file, the File Level Event Code should be REP. After the initial population, subsequent changes should have the UPD code.
- Orderable item updates always originate from Consults.
- There may be multiple MFE segments passed in a single transaction.
- The record-level event code tells whether this transaction is an update, addition, inactivation, etc.
- The primary key is the coded element that is normally passed when creating an order. By using the coded element, we can know the national and local names for a procedure.

Refer to Figure 14-20.

Figure 14-20: Orderable Item Updates – Procedures Example

<!-- image -->

### Ordering Parameters

There are no Consult ordering parameters identified at this time.

### Procedure Calls

We need entry points defined in the Consults package that will handle the following procedure calls. It is up to the developers exactly how entry points are defined and named. Note that to behave properly in a windowed environment, all variables used in the calls must be NEWed properly. The calls must also be silent (no reads or writes).

Refer to Figures 14-21 to 14-23.

Figure 14-21: Procedure Calls Example

<!-- image -->

<!-- image -->

Figure 14-22: Procedure Calls Example (continued)

<!-- image -->

Figure 14-23: Procedure Calls Example (continued)

<!-- image -->

### Auto-forwarding

A new feature, Auto-forwarding, has been added with patch GMRC*3.0*139. When the Decision Support Tool (DST) determines that a Consult should be forwarded to a different location, the DST data returned will contain the text “DAF-DST Auto-forwarding:”. When the routine ^GMRCDST detects this text, it will examine the text after the colon. If it detects “YES”, then the code will mark this Consult as being forwarded. The routine will then look for the text “AFD-DST Forward to:” text and forward this Consult Order to the requested REQUEST SERVICE entry (#123.5), using the $$FR^GMRCGUIA utility.

If the REQUEST SERVICE entry does not exist, the error message "DVE-DST Error from VistA: Auto-forward target not found" will be placed in the original Consult entry. If DST does not send the “AFD-DST Forward to:” text, the error message will appear as "DVE-DST ID ISSUE: No Content sent from DST". This error message will be placed in the Original Consult entry.

## 15 How to Generate On-Line Documentation

### Routines

The namespace for the Consults package is GMRC. A listing/printout of any or all of the Consults routines can be produced by using the Kernel option XUPRROU (List Routines). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option. When prompted with “routine(s) ? &gt;:” type in GMRC* to get a listing of all Consults routines.

The first line of each routine contains a brief description of the general function of the routine. A listing of just the first line of each Consults routine can be produced by using the Kernel option XU FIRST LINE PRINT (First Line Routine Print). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

### Globals

The globals used in the Consults package are ^GMR(123, ^GMR(123.1, ^GMR(123.3, ^GMR(123.5 and ^GMR(123.6. A listing/printout of any of these globals can be produced by using the Kernel option XUPRGL (List Global). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

#### Files

The number-space for Consults files is 123. A listing of these files can be obtained by using the VA FileMan option DILIST (List File Attributes). Depending on the FileMan template used to print the listing, this option will print out all or part of the data dictionary for the Consults files.

### Menu/Options

The menu and options exported by the Consults package all begin with the GMRC namespace. Individual options can be viewed by using the Kernel option XUINQUIRE (Inquire). This option is found on the menu XUMAINT (Menu management), which is a sub-menu of the EVE (Systems Manager Menu) option.

A diagram of the structure of the Consults menu and its options can be produced by using the Kernel option XUUSERACC (Diagram Menus). Choosing XUUSERACC permits you to further select XUUSERACC1 or XUUSERACC2 menu diagrams with entry/exit actions or abbreviated menu diagrams. This option is found on the menu XUMAINT (Menu management), which is a sub-menu of the EVE (Systems Manager Menu) option.

### XINDEX

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a listing of internal and external routine calls. XINDEX is invoked from programmer mode: D ^XINDEX. When selecting routines, select GMRC*.

## 16 Glossary

Refer to Table 16-1.

Table 16-1: Glossary

| Term                  | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action                | An action in Consults can be selected throughout processing to 1) control screen movement, or 2) process existing orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Consult               | Referral of a patient by the primary care physician to another hospital service/specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion. For instance, if a primary care physician orders a patient evaluation from Cardiology Service, and the cardiology specialist orders an Electrocardiogram (EKG) to complete the evaluation and provide an opinion concerning the patient’s condition, this type of order is considered a “Consult.” |
| Discontinued Orders   | Orders that are discontinued. When an order is discontinued, it must be completely re-entered to be resubmitted. However, if an order is canceled,  it can be edited to correct some deficiency and resubmitted.                                                                                                                                                                                                                                                                                                                                                                         |
| Order                 | A request for a consult (service/sub-specialty evaluation) or procedure (Electrocardiogram) to be completed for a patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Order Cancellation    | The cancellation of a consult or procedure request which allows the requesting provider to edit a portion of the original request and re-submit the request to the consulting service.                                                                                                                                                                                                                                                                                                                                                                                                   |
| Order Discontinuation | A request to stop (discontinue) performance of a consult/procedure request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HCPS                  | The Healthcare Claims Processing System is a centralized, automated system that will support the management of purchased care referrals/authorizations.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IFC                   | Inter-Facility Consults permits the transmitting of consults and related information between Department of Veterans Affairs facilities. Consult requests are made to remote facilities because the needed service is not locally available or for patient convenience. Although the Consult Package is utilized in the hospital settings, Consult requests between facilities have been done manually in the past.                                                                                                                                                                       |
| MPI                   | Master Patient Index. An index of VA patients that is global in nature, showing patients that have been seen by more than one VA facility and giving information about which facilities are involved.                                                                                                                                                                                                                                                                                                                                                                                    |
| MVI                   | Master Veteran Index, see MPI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| NVC                   | Non VA Care. Care provided to eligible Veterans when VA facilities are not feasibly available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Procedure Request     | Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without requiring formal consultation first.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Result                | A consequence of an order. Refers to evaluation or status results. In regard to Consult/Request Tracking, results refer to a TIU document or Medicine procedure result attached to the consult or procedure request.                                                                                                                                                                                                                                                                                                                                                                     |
| Requestor             | This is the health care provider (e. g., the physician/clinician) who requests the order to be done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Screen Context        | This term refers to the particular selection of orders displayed on the screen (e. g., Medicine consults for the patient Ralph Jones).                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Service               | A clinical or administrative specialty (or department) within a Medical Center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Status                | A result that indicates the processing state of an order; for example, a Cardiology Consult order may be “discontinued (dc)” or “completed (c)”.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Status Symbols        | Codes used in order entry and Consults displays to designate the status of the order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## 17 Appendix A: Install, Planning, and Implementation Checklist

This checklist can help you determine if you have completed the steps needed to implement the Consults package. IRMS/ADPAC personnel should carefully read the Consult/Request Tracking Technical Manual for the details related to IRMS/ADPAC implementation.

**Note:** Important changes since Consults/Request Tacking Version 2.5 are emphasized with a note.

**Installation:**

The Consult/Request Tracking V. 3.0 package installs automatically when CPRS V. 1.0 installed.

**Planning:**

Participants: IRMS/ADPAC and Service personnel

**NOTE: Effective with Consults/Request Tracking V. 3.0:**

- A service is only selectable for update/tracking if it is defined as part of the ALL SERVICES hierarchy.
- Disabled services can be left in the ALL SERVICES hierarchy so their order results can be returned but are not selectable in the ordering process.
- Tracking services must be in the ALL SERVICES hierarchy in order to be receive forwarded consults. The tracking service can only be selectable in the order forwarding process if the user is an update user for the tracking service or its parent service.

1. Plan the Consult Service Hierarchy.
    1. Identify services to receive consults or to be Inter-Facility Services.
    2. Determine if the service should be selectable in the ordering process from CPRS.
                    1. For some consults, the order may need to be sent to a Service control point for Forwarding by the control point to a service which has been identified as a “Tracking Only” service. (Tracking Only services are not selectable during the initial CPRS order process.) Where a service control point is preferred, the tracking services should be sub-specialties under the control point service within the ALL SERVICES hierarchy.
    3. Determine if there should be a service that would be used as a “Grouper Only” (e.g., Inpatient Services, Outpatient Services, and Outside Services might be good Services to define as groupers).
    4. When a Grouper Only service is selected in the CPRS order process, the service hierarchy defined under the grouper service will be displayed to select from. The Grouper Only cannot be selected to receive an order. The ALL SERVICES service is a Grouper Only provided to build the Consult Service hierarchy upon.
2. For each Service, Identify the Service.
    5. Select a unique name to identify the service while ordering. If the service is to be on Inter-Facility Consults (IFC) service, we suggest you include the site name in the service (Example: Eye Clinic—Boise).
    6. Optionally, select an abbreviated print name to be used when displaying notifications. This should be a short name that is easily recognized by users as belonging to the service.
    7. Optionally, select one or more synonyms that can be used when entering the service name into the computer.
    8. Identify the service printer which will be used to automatically print Consult Form SF 513 when a consult order is received from CPRS.

**Note:** Effective with Consult/Request Tracking V. 3.	0, All Consult Form SF 513 prints are done from consult routines. OE/RR print formats are no longer used for consult prints.

1. Plan Actions to take for a Discontinued Consult
    1. Decide if the service should be notified when a consult is discontinued.
    2. Decide if the SF 513 should be reprinted to the receiving service when a consult is discontinued.
2. Determine Provisional Diagnosis requirements for the Service.
    3. Decide if consults going to this service should be required to have a provisional diagnosis. The provisional diagnosis can be required, set as optional, or suppressed.
    4. Decide if provisional diagnosis going to this service should be taken from the Clinical Lexicon, or if free text is allowed.
3. Plan Prerequisites and Boilerplate.
    5. Decide if consults going to this service should have a prerequisite. A prerequisite is a text message that reminds the referring physician what needs to be done before a consult can be sent to this service. The prerequisite message gives the referring physician a chance to back out of the consult dialog.
    6. Decide if consults going to this service should provide a default reason for request when an order is placed. This is a piece of boilerplate text, including TIU objects, that is consistent for each consult received.
    7. If this service is to be an IFC service, then enter the IFC Remote Site name and IFC Remote Service name.
    8. If this service is to be an to receive IFC requests from other sites, then enter the IFC Sending Facility name(s).
    9. Decide if editing of the default reason for request should be restricted. Editing can be unrestricted, restricted, or allowed only before release to the service.
4. Plan Notification Recipients.
    10. Identify individuals at the receiving service who should be notified when a consult is being sent to the receiving service.
    11. Identify service teams of clinicians or service users which should receive notifications. Team definitions may be used in addition to or in lieu of naming individuals to receive notifications.
    12. Identify hospital locations that are assumed to be part of this service. Any consult activity on patients in that location triggers a notification. Specify one individual to notify and/or a team to notify.
    13. Decide if parent services of this service should be notified of activities occurring on consults for this service.
    14. Decide if notifications should be deleted on an individual basis, or if all notifications should be deleted when one individual reviews it. The default is Individual Recipient, so if All Recipients is desired, use the Set Deletion Parameters for Notifications option of the Notification Mgmt Menu to change this value for each of the five consult notifications. They are:
                    1. #23	CONSULT/REQUEST RESOLUTION
                    2. #27
                    3. NEW SERVICE CONSULT/REQUEST
                    4. #30	CONSULT/REQUEST CANCEL/HOLD
                    5. #63	CONSULT/REQUEST UPDATED
                    6. #89 	PROSTHETICS CONSULT
5. Plan Service Users.
    15. Decide if you are going to allow unrestricted access to this service. If so, you may skip to step 13.
    16. Identify individuals at the receiving service who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.
    17. Identify teams at the receiving service who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.
    18. Identify user classes who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.
    19. Identify administrative update users. Such a user can perform administrative completions on consults at this service. These users can, optionally, be included as notifications recipients for this service.
    20. Identify administrative update teams for this service. The members of these teams can, optionally, be included as notifications recipients for this service.
    21. Decide if update users of the parent services should be allowed to update consults for this service.
    22. Identify a special updates individual (someone who can perform group updates) for this service. This individual should already be a service user.
    23. Identify sub-services of this service.
6. Implementation and Maintenance (Abbreviated Guidelines)

Participants: IRMS/ADPAC

1. You may set up a team for each consult service. The team members being the identified clinical users. Use the Team Mgmt Menu option, ORLP TEAM MENU.
2. Turn on the NEW SERVICE CONSULT/REQUEST notification for each of the individuals who were identified to receive notifications. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.

**Note:** Unless Consult notifications are set to mandatory, individual users may use the Enable/Disable My Notifications option of the Notifications Management Menu to individually disable the notifications they do not want to receive.

1. Turn on the CONSULT/REQUEST RESOLUTION notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.
2. Turn on the CONSULT/REQUEST CANCEL/HOLD notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.
3. Turn on the CONSULT/REQUEST UPDATED notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.
4. Turn on the PROSTHETICS CONSULT UPDATED notification for each ordering provider identified to receive this notification, or train them to do it themselves.
5. PROSTHETICS CONSULT UPDATED should be enabled for identified personnel requiring updates to prosthetics consults. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.
6. Define the Service hierarchy in the Request Services File (#123.5) with the associated users and service printer. Use the “Set up Consult Services” option, GMRC SETUP REQUEST SERVICES.

**Note:** You must NOT use VA FileMan to modify services in the hierarchy. The Consult/Request Tracking interface to CPRS depends on the services being defined using the GMRC SETUP REQUEST SERVICES option.

1. Assign the Setup Service Users GMRC SETUP SERVICE USERS option to the users permitted to manage service users.
2. Assign the following two options to Service update users’ primary or secondary menu option: Consult Tracking [GMRC SERVICE TRACKING] and Service Consults Pending Resolution [GMRC RPT PENDING CONSULTS].
    1. Setup
        1. Plan your hospital’s TIU hierarchy. See the Text Integration Utility (TIU) Implementation Guide for details on this step.
        2. If you have not already done so, install TIU*1*4.
        3. Run the TIU DEFINE CONSULTS option.**Note:** If you do not run the TIU DEFINE CONSULTS option, no status update takes place when the TIU note is entered.
        1. Enter the rest of your planned TIU document hierarchy using the Manager Document Definition Menu.
        2. Define consult document parameters (as recommended on page 70 of this manual) using the Document Parameter Edit option.**Note:** We particularly recommend entering Yes to ALLOW &gt;1 RECORDS PER VISIT.
        1. Check the value for parameter GMRC CONSULT LIST DAYS. The parameter controls how many days are searched when looking for consult to associate with a progress note. The default is 365 days.

## 18 Appendix B: Consult Tracking Worksheets

In this section there are several worksheets that may be removed from the manual and copied. These worksheets assist you in setting up each Service/Specialty and in setting up Service Notification assignments for individuals or teams who will be receiving consult results.

The first and second worksheets may be used for small Services, with very few Specialty services under them, who will be receiving on-line consults and/or procedure requests.

The third and fourth worksheets should be used by large complex Services with multiple Specialty services under them, who will be receiving on-line consults and/or procedure requests.

**Consult Services Worksheet**

Service Set up

Service/Specialty Name:							\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviated Print Name:							\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This optional abbreviation are used when building notifications.

Synonyms:	 								 \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_

These optional abbreviations are used when selecting the service.

Service Usage:							     Blank  Grouper  Tracking

Service Printer:								\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A service may define a device to which its Consult forms automatically print.

Notify Service on DC:								 Yes  No

Update users of a service may be notified when a consult is discontinued.

Reprint 513 on DC:									 Yes  No

The SF 513 may be reprinted to the consulting service when a consult is discontinued.

Provisional DX Prompt: 				           	 Required  Optional  Suppressed

Set whether a diagnosis is required, optional, or suppressed when ordering.

Provisional DX Input: 							 Lexicon  Free Text

If the diagnosis is not suppressed, specifies whether the diagnosis must be from the Clinical Lexicon or not.

Prerequisite:

Prerequisite information may be displayed to the consult ordering physician before proceeding with the ordering of a consult to this service. This may include TIU fields (enclosed in |).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Default Reason for Request:

Boilerplate may be supplied for the reason for request. This may include TIU fields (enclosed in |).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	                                                                   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	                                                                   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Restrict Default Reason Edit: 		 Unrestricted  No Editing  Ask

Determines if the boilerplate can be edited by the ordering physician.

Page 1 of 3

Consult Services Worksheet

Notification Users

Service Individual to Notify:						\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Individual who needs to receive Notifications  for this service should be listed here.

Service Team to Notify:

All full update users to receive notifications need to be defined on one of these teams.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Notification by Pt Location:

Locations in which all patients are considered belonging to this service should be listed here. For each location, you can specify one individual and one team to be notified.

Location \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  	Individual \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_									Team \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Location \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  	Individual \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_									Team \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Process Parents for Notifications:	 Yes  No

Determines whether the notification recipients defined for the parent service should be notified of actions on consults directed to this service.

Update Users

Update Users without Notifications:

Service users who should be able to perform update capabilities, but DO NOT receive  notifications should be defined here. The same algorithm is used to determine the recipients for all types of consult notifications.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Update Teams without Notifications:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Update User Class without Notifications:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page 2 of  3

Consult Services Worksheet

Administrative Update Users:

Users who may close consults without attaching a TIU note are defined here.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Notification Recipient?					 Yes  No

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Notification Recipient?					 Yes  No

Administrative Update Teams:

Teams whose members may close consults without attaching a TIU note are defined here.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Notification Recipient?					 Yes  No

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Notification Recipient?					 Yes  No

Process Parents for Updates:		 						Yes  No

Determines whether the update users defined for the parent service should have the same update privileges on consults directed to this service.

Special Update Individual:							\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A user who is allowed to perform batch updating of status on consults.

Unrestricted Access:								 	 Yes  No

If marked yes, any user may have update access to this service.

Miscellaneous

Sub-Service Specialty:

Services that are below this one in the Consults Service Hierarchy.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## 19 Appendix C: Request Services Distributed with Consults

**Note:** The distributed services are those services shown below with an asterisk(*). The hierarchy shown below via the sub-service specialty column is not distributed. Use the Set up Consults Services option to build the hierarchy for your service. Remember, the top of the hierarchy must be ALL SERVICES.

**REQUEST SERVICES LIST**

**NAME**

SUB-SERVICE SPECIALTY

*ALL SERVICES

MEDICINE

PHARMACY SERVICE

*CARDIOLOGY

*GASTROENTEROLOGY

*HEMATOLOGY

*MEDICINE

CARDIOLOGY

GASTROENTEROLOGY

HEMATOLOGY

PULMONARY

RHEUMATOLOGY

*PHARMACY SERVICE

*PULMONARY

*RHEUMATOLOGY

The indented services represent sub-service/specialties making up the hierarchy.

**CAUTION:** New services must be added to ALL SERVICES if not a sub-service specialty.

## 20 Appendix D: Package Security

### Service Update and Tracking Security

You can use the Consult Service User Management option, in conjunction with availability to various menus and options, to control access to Consults functionality. The menus that can be provided are:

- Consult Service Tracking
- Pharmacy Consult User

The Consult Service Tracking menu provides access to basic consult tracking functions and reports but can also provide complete update capabilities if you have been granted update privileges by your ADPAC.

Individual options in the Consults package that may be useful to users and what access they provide, are detailed in Table 20-1.

Table 20-1: Package Security Options

| Option                              | Services                                                                        |
|-------------------------------------|---------------------------------------------------------------------------------|
| Consult Service Tracking            | Tracking and/or update functionality depending upon your individual privileges. |
| Pharmacy TPN Consults               | Tracking, and update functionality.                                             |
| Completion Time Statistics          | Reporting.                                                                      |
| Service Consults Pending Resolution | Reporting.                                                                      |

With the GMRC Service User Management option you can set users up to be update users for one or more services at your hospital. In addition, you can grant the ability to receive consult notifications according to criteria outlined in Table 20-2.

Table 20-2: Consult Notifications Criteria

| Category                                           | Notifications Received                                                                                                       |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| UPDATE USERS W/O NOTIFICATIONS                     | Unless otherwise set up, will not receive notifications.                                                                     |
| SERVICE INDIVIDUAL TO NOTIFY                       | Receive consult notifications for your service.                                                                              |
| SERVICE TEAM TO NOTIFY                             | Receive consult notifications for your service. These teams send notifications regardless of the patients contained on them. |
| NOTIFICATION BY PT LOCATION - INDIVIDUAL TO NOTIFY | Receive all consult notifications for your service for patients in a specified ward.                                         |
| NOTIFICATION BY PT LOCATION - TEAM TO NOTIFY       | Receive consult notifications for patients in a specified ward.                                                              |
| NOTIFICATION BY PT LOCATION - TEAM TO NOTIFY       | Receive consult notifications for patients in a specified ward.                                                              |

These categories are not mutually exclusive, meaning a user may receive notifications based on being present on one or more of the lists detailed in the preceding table.

Refer to Table 20-3, which lists privileges a user may want and who that privilege is granted to.

Table 20-3: Privileges

| Privilege               | Granted                                                            |
|-------------------------|--------------------------------------------------------------------|
| Originate a consult     | Anyone with access to CPRS                                         |
| Sign a consult          | Anyone who can sign an order                                       |
| Change a consult status | Anyone with update privileges                                      |
| View or print a consult | Anyone with the Consult Service Tracking option or access to CPRS. |

In summary, update user capabilities vary depending on the following:

The option(s) that you are assigned.

Privileges granted in the Consults Service User Management option.

Menu/Option Access

Refer to Table 20-4, which lists the menus/options available with the Consults package for distribution to users.

Table 20-4: Files

| Option Name               |   File |
|---------------------------|--------|
| GMRC MGR                  |     19 |
| GMRC GENERAL SERVICE USER |     19 |
| GMRC PHARMACY USER        |     19 |
| GMRC SERVICE TRACKING     |     19 |
| GMRC TPN CONSULTS         |     19 |
| GMRC RPT PENDING CONSULTS |     19 |
| GMRC REVIEW SCREEN        |    101 |

#### GMRC MGR Menu

This option should be given to IRMS/ADPAC personnel. It is composed of all options distributed with the Consults package.

#### GMRC GENERAL SERVICE USER Menu

This menu provides access to the most commonly used Consults options that a general user, other than Medicine, would be interested in. This option should be added to their primary or secondary menu options.

#### GMRC PHARMACY USER Menu

This menu provides access to the most commonly used Consults options that a user of the Pharmacy TPN option would be interested in. This option should be added to their primary or secondary menu options.

#### GMRC SERVICE TRACKING Option

The Consult Service Tracking (GMRC SERVICE TRACKING) option may be given to “review only” UANDU service “update” users. This option should be added to their primary or secondary menu options.

You may want to add the GMRC SERVICE TRACKING option to the OR MAIN MENU options in the Option file (#19) as well, since users of these OR options are likely interested in reviewing consult/request activities services may have taken.

#### GMRC PHARMACY TPN CONSULTS Option

Pharmacy personnel who need to be able to update File 123, REQUEST/CONSULTATION file, with service activity tracking updates should have the GMRC PHARMACY TPN CONSULTS option added to their primary or secondary menu options.

### Security Keys

#### File Security

Refer to Table 20-5, which provides a list of recommended VA FileMan access codes associated with each file contained in the Consults package.

Table 20-5: Recommended FileMan Access Codes

| File Number   | File Name            | DD Access   | RD Access   | WR Access   | DEL Access   | LAYGO Access   |
|---------------|----------------------|-------------|-------------|-------------|--------------|----------------|
| (#123)        | Request/Consultation |             |             |             |              |                |
| (#123.1)      | Request Action Types |             |             |             |              |                |
| (#123.3)      | GMRC Procedures      |             |             |             |              |                |
| (#123.5)      | Request Services     |             |             |             |              |                |

### Service Update Tracking Security

The Consults Package is distributed for all Services at a facility to track consult/request activity. Security at the Service level is set up by IRMS/ADPAC personnel in the Request Services file (#123.5). Specific fields which provide security restrictions include GMRCACTM PHARMACY PKG MENU, described below.

#### GMRCACTM PHARMACY PKG MENU

This is the PROTOCOL ACTION MENU exported for use by Pharmacy Service personnel to process Pharmacy TPN Consults.

### Routine Descriptions

Refer to Table 20-6.

Table 20-6: Routine Descriptions

| Routine       | Description                                                                                                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMRC101       | Create Protocol entries for OE/RR ADD orders screens                                                                                                                                                                                                                                                                   |
| GMRC101C      | Create Protocol entries for OE/RR ADD orders screens (Continued)                                                                                                                                                                                                                                                       |
| GMRC101H      | Set up HL-7 message to update OERR orderable items file with new consult type.                                                                                                                                                                                                                                         |
| GMRC15EN      | Environment check GMRC*3*15                                                                                                                                                                                                                                                                                            |
| GMRC513U      | Obsolete utility deleted with GMRC*3*4.                                                                                                                                                                                                                                                                                |
| GMRC7L        | List Template Exporter.                                                                                                                                                                                                                                                                                                |
| GMRC75P       | Add the ‘HCPS, APPLICATION PROXY’ user the NEW PERSON (#200) file.                                                                                                                                                                                                                                                     |
| GMRCA1        | Actions taken from Review Screens.                                                                                                                                                                                                                                                                                     |
| GMRCA2        | Select prompt for processing actions.                                                                                                                                                                                                                                                                                  |
| GMRCAAC       | Administrative Complete action consult logic.                                                                                                                                                                                                                                                                          |
| GMRCACMT      | Comment Action and alerting.                                                                                                                                                                                                                                                                                           |
| GMRCACTM      | Set GMRCACTM with action menu based on Service.                                                                                                                                                                                                                                                                        |
| GMRCADC       | Discontinue Action taken from List Manager.                                                                                                                                                                                                                                                                            |
| GMRCAFRD      | Forward Req (FR) Action from Review Screen.                                                                                                                                                                                                                                                                            |
| GMRCALOR      | Process a consult from an alert notification.                                                                                                                                                                                                                                                                          |
| GMRCALRT      | List Manager alert action interface.                                                                                                                                                                                                                                                                                   |
| GMRCAR        | Associate Results (AR) Action taken from Review Screen.                                                                                                                                                                                                                                                                |
| GMRCART       | Result display logic.                                                                                                                                                                                                                                                                                                  |
| GMRCASF       | Significant Findings Action.                                                                                                                                                                                                                                                                                           |
| GMRCAST       | Select OE/RR Status (ST) Action.                                                                                                                                                                                                                                                                                       |
| GMRCASV       | Build ^TMP("GMRCS" of Svc(s)/Specialties.                                                                                                                                                                                                                                                                              |
| GMRCASV1      | Hierarchy Mgmt cont'd.                                                                                                                                                                                                                                                                                                 |
| GMRCAU        | Action Utilities.                                                                                                                                                                                                                                                                                                      |
| GMRCCA        | Report Prompting for Configuration Tool                                                                                                                                                                                                                                                                                |
| GMRCCB        | Data Gathering                                                                                                                                                                                                                                                                                                         |
| GMRCCC        | Output Data                                                                                                                                                                                                                                                                                                            |
| GMRCCD        | Interactive Consult Update                                                                                                                                                                                                                                                                                             |
| GMRCCX        | Configuration File Utilities                                                                                                                                                                                                                                                                                           |
| GMRCCY        | Consult Closure Tool: Date Range Selector                                                                                                                                                                                                                                                                              |
| GMRCCLR       | Kill-off all variables used for consults tracking.                                                                                                                                                                                                                                                                     |
| GMRCCPRS      | Routine To Give Actions For Consults From The OE/RR Menu's.                                                                                                                                                                                                                                                            |
| GMRCDDX       | AC cross-reference logic for 123.5, field .01.                                                                                                                                                                                                                                                                         |
| GMRCDST       | Retrieve decision from DST server                                                                                                                                                                                                                                                                                      |
| GMRCDIS       | LM routine to disassociate med results                                                                                                                                                                                                                                                                                 |
| GMRCDPCK      | Check for a duplicate Consult/Request that has a status of active, pending or scheduled.                                                                                                                                                                                                                               |
| GMRCDRFR      | Default reason for request utils.                                                                                                                                                                                                                                                                                      |
| GMRCEDIT      | Edit cancelled consult-main driver.                                                                                                                                                                                                                                                                                    |
| GMRCEDT1      | Edit a consult and re-send as new.                                                                                                                                                                                                                                                                                     |
| GMRCEDT2      | Resubmit a cancelled consult.                                                                                                                                                                                                                                                                                          |
| GMRCEDT3      | For a Cancelled Consult - File edited data for tracking consult.                                                                                                                                                                                                                                                       |
| GMRCEDT4      | Utilities for editing fields.                                                                                                                                                                                                                                                                                          |
| GMRCFP        | GMRC FEE PARAM List Utilities                                                                                                                                                                                                                                                                                          |
| GMRC FPA      | GMRC FEE PARAM List Utilities                                                                                                                                                                                                                                                                                          |
| GMRCFX23      | Consult postinit file maintenance.                                                                                                                                                                                                                                                                                     |
| GMRCGUIA      | File Consult actions from GUI.                                                                                                                                                                                                                                                                                         |
| GMRCGUIB      | GUI actions for consults.3                                                                                                                                                                                                                                                                                             |
| GMRCGUIC      | GUI actions for editing consults.                                                                                                                                                                                                                                                                                      |
| GMRCGUIU      | Kill off variables from GUI routines.                                                                                                                                                                                                                                                                                  |
| GMRCHK        | GMRC check for programmer access.                                                                                                                                                                                                                                                                                      |
| GMRCHL7       | HL-7 formatting routine for consult information to be passed to OER.                                                                                                                                                                                                                                                   |
| GMRCHL72      | HL-7 formats OBX and NTE segments.                                                                                                                                                                                                                                                                                     |
| GMRCHL7A      | Receive HL-7 Message form OERR and break it into its components and store it in File 123.                                                                                                                                                                                                                              |
| GMRCHL7B      | Process order parameters from ^GMRCHL7A and place data into ^GMR(123 global.                                                                                                                                                                                                                                           |
| GMRCHL7H      | Receive consult event messages. Called by GMRCACMT and GMRCGUIB.                                                                                                                                                                                                                                                       |
| GMRCHL7I      | Processes incoming messages from HCPS.                                                                                                                                                                                                                                                                                 |
| GMRCHL7P      | Generate HL7 v2.5 REF messages. Called by GMRCH7H.                                                                                                                                                                                                                                                                     |
| GMRCHL7U      | Utilities associated with HL7 messages.                                                                                                                                                                                                                                                                                |
| GMRCHLP       | List Manager help logic.                                                                                                                                                                                                                                                                                               |
| GMRCIAC1      | File IFC activities cont'd.                                                                                                                                                                                                                                                                                            |
| GMRCIAC2      | File IFC activities cont'd.                                                                                                                                                                                                                                                                                            |
| GMRCIACT      | Process actions on IFC.                                                                                                                                                                                                                                                                                                |
| GMRCIBKG      | IFC background error processor.                                                                                                                                                                                                                                                                                        |
| GMRCIBKM      | Monitor IFC background params.                                                                                                                                                                                                                                                                                         |
| GMRCIERR      | Process IFC message error alert.                                                                                                                                                                                                                                                                                       |
| GMRCIEV1      | IFC events cont'd .                                                                                                                                                                                                                                                                                                    |
| GMRCIEVT      | Process events and build HL7 message.                                                                                                                                                                                                                                                                                  |
| GMRCILKP      | Look up IFC by remote consult number.                                                                                                                                                                                                                                                                                  |
| GMRCIMSG      | IFC message handling routine.                                                                                                                                                                                                                                                                                          |
| GMRCINC       | List incomplete IFC transactions.                                                                                                                                                                                                                                                                                      |
| GMRCIR        | IFC request data & statistics.                                                                                                                                                                                                                                                                                         |
| GMRCISEG      | Create IFC HL7 segments.                                                                                                                                                                                                                                                                                               |
| GMRCISG1      | Build IFC HL7 segments cont'd.                                                                                                                                                                                                                                                                                         |
| GMRCITR       | IFC transactions.                                                                                                                                                                                                                                                                                                      |
| GMRCITST      | Test IFC setup.                                                                                                                                                                                                                                                                                                        |
| GMRCIUTL      | Utilities for inter-facility consults.                                                                                                                                                                                                                                                                                 |
| GMRCMCP       | List Manager Format Routine To Collect Medicine Package Consults and format them for display by List Manager.                                                                                                                                                                                                          |
| GMRCMED       | Medicine interface routines.                                                                                                                                                                                                                                                                                           |
| GMRCMED1      | Extract medicine results for consult tracking.                                                                                                                                                                                                                                                                         |
| GMRCMENU      | Select List Manager menu for user characteristics.                                                                                                                                                                                                                                                                     |
| GMRCMER       | Print Medicine Results in List Manager Format.                                                                                                                                                                                                                                                                         |
| GMRCMP        | List Manager routine: Medical Service and sub-specialty consults.                                                                                                                                                                                                                                                      |
| GMRCMSS       | Setup Request Services.                                                                                                                                                                                                                                                                                                |
| GMRCMU        | Add protocols to GMRC protocol menus.                                                                                                                                                                                                                                                                                  |
| GMRCNOTF      | Notification recipient utilities.                                                                                                                                                                                                                                                                                      |
| GMRCP         | Message audit and status process.                                                                                                                                                                                                                                                                                      |
| GMRCP5        | Print Consult form 513 (main entry).                                                                                                                                                                                                                                                                                   |
| GMRCP513      | Print Consult form 513.                                                                                                                                                                                                                                                                                                |
| GMRCP5A       | Print Consult form 513 (Gather Data - TIU Results).                                                                                                                                                                                                                                                                    |
| GMRCP5B       | Print Consult form 513 (Gather Data - Footers, Provisional Diagnosis and Reason For Request).                                                                                                                                                                                                                          |
| GMRCP5C       | Print Consult form 513 (Assemble Segments And Print).                                                                                                                                                                                                                                                                  |
| GMRCP5D       | Print Consult form 513 (Gather Data - Addendums, Headers, Service reports and Comments).                                                                                                                                                                                                                               |
| GMRCPC        | List Manager Routine: Collect and display consults by service and status.                                                                                                                                                                                                                                              |
| GMRCPC1       | List Manager Routine: Collect and display consults by service and status.                                                                                                                                                                                                                                              |
| GMRCPH        | Process XQORM helps.                                                                                                                                                                                                                                                                                                   |
| GMRCPOR       | Get DOC,LOC,TS in interactive defaults.                                                                                                                                                                                                                                                                                |
| GMRCPOS       | Consult postinit file maintenance.                                                                                                                                                                                                                                                                                     |
| GMRCPOS1      | Post init to move Services from file 123.5 to the orderable items file, 101.43, and orderables in file 101 to file 101.43.                                                                                                                                                                                             |
| GMRCPOS2      | Consult postinit file maintenance.                                                                                                                                                                                                                                                                                     |
| GMRCPOST      | Post init driver routine.                                                                                                                                                                                                                                                                                              |
| GMRCPP        | Print GMRC consult/request tracking protocols - List Manager routine.                                                                                                                                                                                                                                                  |
| GMRCPR        | GMRC List Manager Routine - Get information for abbreviated print of GMRC protocols and format for List Manager.                                                                                                                                                                                                       |
| GMRCPR0       | Data Entry Promptint actions.                                                                                                                                                                                                                                                                                          |
| GMRCPREF      | Setup package/procedure protocols.                                                                                                                                                                                                                                                                                     |
| GMRCPROT      | Consult postinit file maintenance.                                                                                                                                                                                                                                                                                     |
| GMRCPRP       | Set protocol information into ^TMP global for print and display by List Manager.                                                                                                                                                                                                                                       |
| GMRCPRPS      | List Manager GMRC Routine -- List GMRC (Consults/Request) Protocols in abbreviated form.                                                                                                                                                                                                                               |
| GMRCPS        | Select Service/specialty to send Consult to.                                                                                                                                                                                                                                                                           |
| GMRCPSL1      | Main entry point for reports search by provider, location, or procedure.                                                                                                                                                                                                                                               |
| GMRCPSL2      | Build ^TMP(“GMRCRPT) for GMRCPSL1.                                                                                                                                                                                                                                                                                     |
| GMRCPSL3      | Generate reports using ^TMP(“GMRCRPT”).                                                                                                                                                                                                                                                                                |
| GMRCPSL4      | Generate reports using ^TMP(“GMRCRPT”).                                                                                                                                                                                                                                                                                |
| GMRCPSL1      | Special Consult reports.                                                                                                                                                                                                                                                                                               |
| GMRCPSL2      | Special Consult reports.                                                                                                                                                                                                                                                                                               |
| GMRCPSL3      | Special Consult reports.                                                                                                                                                                                                                                                                                               |
| GMRCPSEL      | Select Range Of Items From List.                                                                                                                                                                                                                                                                                       |
| GMRCPURG      | Purge orders from the Order File 100.                                                                                                                                                                                                                                                                                  |
| GMRCPX        | Select a new pharmacy patient for list manager consult tracking display.                                                                                                                                                                                                                                               |
| GMRCPZ        | GMRC List Manager Routine -- Main menu actions for Pharmacy consults request tracking.                                                                                                                                                                                                                                 |
| GMRCQC        | GMRC List Manager routine to print Consults pending resolution for QC purposes.                                                                                                                                                                                                                                        |
| GMRCQCST      | Gather all consults for QC that do not have status of discontinued, complete, or expired.                                                                                                                                                                                                                              |
| GMRCR         | Driver for reviewing patient consult/requests - Used by Medicine Package to link Consults to Medicine results.                                                                                                                                                                                                         |
| GMRCR0        | Add original consult via backdoor service.                                                                                                                                                                                                                                                                             |
| GMRCR06       | Complete a consult/request.                                                                                                                                                                                                                                                                                            |
| GMRCRA        | Build ^TMP("GMRCR",$J, array of consults.                                                                                                                                                                                                                                                                              |
| GMRCREXT      | Clean-up all variables and ^TMP globals upon exit.                                                                                                                                                                                                                                                                     |
| GMRCRFIX      | Consult postinit save GMRCR protocol file links.                                                                                                                                                                                                                                                                       |
| GMRCRPOS      | Consult postinit save GMRCR protocol file links.2                                                                                                                                                                                                                                                                      |
| GMRCS         | Review consults by Patient and Service.                                                                                                                                                                                                                                                                                |
| GMRCSL        | Active Consults by Service.                                                                                                                                                                                                                                                                                            |
| GMRCSLDT      | Get a consults detailed tracking history formatted for List Manager.                                                                                                                                                                                                                                                   |
| GMRCSLM       | List Mgr routine for consult tracking list.                                                                                                                                                                                                                                                                            |
| GMRCSLM1      | Gather data and format ^TMP global for consult tracking Silent call for use by List Manager and GUI.                                                                                                                                                                                                                   |
| GMRCSLM2      | List Manager routine - Detailed consult display and printing.                                                                                                                                                                                                                                                          |
| GMRCSLM3      | Extract medicine results for consult tracking.                                                                                                                                                                                                                                                                         |
| GMRCSLM4      | List Manager routine - Activity Log Detailed Display.                                                                                                                                                                                                                                                                  |
| GMRCSLMA      | List Manager protocol entry, exit actions.                                                                                                                                                                                                                                                                             |
| GMRCSLMU      | Utilities for displaying consults in List manager.                                                                                                                                                                                                                                                                     |
| GMRCSLMV      | Set Video attributes for list manager screens.                                                                                                                                                                                                                                                                         |
| GMRCSPD       | Change Date Range in CSLT Tracking Module.                                                                                                                                                                                                                                                                             |
| GMRCSRVS      | Add/Edit services in File 123.5.                                                                                                                                                                                                                                                                                       |
| GMRCSSP       | List Manager Format Routine To Collect Pharmacy TPN Consults that are Not Completed Or Have Been Discontinued.                                                                                                                                                                                                         |
| GMRCST        | Statistics on how long to complete consult/requests for a service.                                                                                                                                                                                                                                                     |
| GMRCST0       | Statistics on how long to complete consult/requests for a service.                                                                                                                                                                                                                                                     |
| GMRCST00      | Statistics on how long to complete consult/requests for a service.                                                                                                                                                                                                                                                     |
| GMRCSTAT      | List Manager Ancillary routine - Restrict display of consults to a given status or statuses on List Manager Screen.                                                                                                                                                                                                    |
| GMRCSTL1      | List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.                                                                                                                                                                                                            |
| GMRCSTL2      | List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.                                                                                                                                                                                                            |
| GMRCSTLM      | List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.                                                                                                                                                                                                            |
| GMRCSTS       | Group update status of consult and order.                                                                                                                                                                                                                                                                              |
| GMRCSTS1      | Group update of consults cont'd.                                                                                                                                                                                                                                                                                       |
| GMRCSTS2      | Change status based on result activity.                                                                                                                                                                                                                                                                                |
| GMRCSTSI      | Special processing to change status of selected consult and order                                                                                                                                                                                                                                                      |
| GMRCSTSU      | Change status based on current order status.                                                                                                                                                                                                                                                                           |
| GMRCSTSZ      | Loop "AE" and get entries, dump in ^TMP.                                                                                                                                                                                                                                                                               |
| GMRCSTU       | Statistic Utilities for Consult/Request Package.                                                                                                                                                                                                                                                                       |
| GMRCSTU1      | Statistic Utilities for Consult/Request Package.                                                                                                                                                                                                                                                                       |
| GMRCSUBS      | Routine to check if a Service has more than one patient service.                                                                                                                                                                                                                                                       |
| GMRCSVCU      | Utility to put services from file 123.5 into file 101.43 when service exists in 123.5 but not.                                                                                                                                                                                                                         |
| GMRCT         | Get DUZ's of users for notification to service.                                                                                                                                                                                                                                                                        |
| GMRCTIU       | TIU utilities for exchanging info with Consults.                                                                                                                                                                                                                                                                       |
| GMRCTIU1      | More CT/TIU interface modules.                                                                                                                                                                                                                                                                                         |
| GMRCTIU2      | Enter TIU Browse with DFN and TIUDA.7                                                                                                                                                                                                                                                                                  |
| GMRCTIU3      | Extract medicine results for consults tracking.                                                                                                                                                                                                                                                                        |
| GMRCTIUA      | Add the TIU note to the results multiple.                                                                                                                                                                                                                                                                              |
| GMRCTIUE      | Complete/Update TIU notes.                                                                                                                                                                                                                                                                                             |
| GMRCTIUL      | Get list of existing results for consults.                                                                                                                                                                                                                                                                             |
| GMRCTIUP      | TIU utilities for exchanging info with Consults.                                                                                                                                                                                                                                                                       |
| GMRCTU        | Consults - Terminated users/remove pointers.                                                                                                                                                                                                                                                                           |
| GMRCTU1       | Get DD Info.                                                                                                                                                                                                                                                                                                           |
| GMRCU         | Consult/Request Utilities.                                                                                                                                                                                                                                                                                             |
| GMRCUTIL      | Utilities for formatting word processing fields and setting into ^TMP("GMRCR" globals for use by List Manager routines.                                                                                                                                                                                                |
| GMRCUTL1      | General Utilities.                                                                                                                                                                                                                                                                                                     |
| GMRCUTL2      | Secondary Printer for printing SF 513                                                                                                                                                                                                                                                                                  |
| GMRCXQ        | Routine to allow follow-up on legacy alerts.                                                                                                                                                                                                                                                                           |
| GMRCYP15      | Convert procedures from 101 to 123.3                                                                                                                                                                                                                                                                                   |
| GMRCYP16      | PRE/POST INSTALL FOR GMRC*3*16.                                                                                                                                                                                                                                                                                        |
| GMRCYP18      | Post Install for patch 18  .                                                                                                                                                                                                                                                                                           |
| GMRCYP23      | Post Install for patch 23.                                                                                                                                                                                                                                                                                             |
| GMRCYP7       | Consult clean-up unreleased at test sites.                                                                                                                                                                                                                                                                             |
| GMRCYP8       | Post Install for GMRC*3*8.                                                                                                                                                                                                                                                                                             |
| GMRCCCRA      | Generates the appropriate HL7 messages when a community care consult is entered into the system. ( Modified by patches 99, 106 and 123)                                                                                                                                                                                |
| POST^GMRCP99  | Used during the installation process to set up the appropriate HL7 application protocols and logical links. (Patch 99)                                                                                                                                                                                                 |
| GMRCGUIB      | This existing routine is modified at the line tag CMT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that includes the comment. (Patch 99)                                                                                        |
| GMRCACMT      | This existing routine is modified at the line tag COMMENT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that will include the comment. (Patch 99)                                                                                |
| GMRCCCR1      | This is a subroutine from GMRCCCRA created in Patch 106 and updated for patch 123.  It also contains subroutines used by the GMRCCCRI routine.                                                                                                                                                                         |
| GMRCCCRI      | This routine is used by VistA to parse and process the consult update received from HSRM. This routine is new in patch 123.                                                                                                                                                                                            |
| LINK^GMRC123P | This is a pre-install routine used by patch 123. It checks to see if the CCRA-NAK logical link exists in the system. If not, it asks for the Health Connect Server IP Address and Port number, then creates the logical link in the VistA system. This link is required to receive consult updates from HSRM to VistA. |

### Routine Mapping

Refer to Table 20-7.	 For systems that can use routine mapping, this is a list of routines in the Consults package that should be mapped.

Table 20-7: Routine Mapping

| Routine Prefix   | Routine Usage                                   |
|------------------|-------------------------------------------------|
| GMRCA*           | Action routines                                 |
| GMRCP*           | CPRS interface routines                         |
| GMRCR*           | Consults review/tracking routines               |
| GMRCS            | Service entry point to review/tracking routines |
| GMRCU*           | Utility routines                                |
| GMRCXQ           | View Alerts follow-up                           |
| GMRCD*           | Decision Support Tool Utilities                 |

- An asterisk (*) denotes a wild card specification. Any routines beginning with the characters before the asterisks are included in the set.
- The other routines do not need to be mapped due to their smaller frequency of usage.

## 21 Appendix E: Algorithms

### User Authority

Refer to Figure E-1, which depicts the Select Consult Management Option on the Consult Management Menu, which is used to determine the user authority for any given user. This authority can be checked by using the Determine Users' Update Authority (UA) action.

Figure 21-1: The Select Consult Management Option

<!-- image -->

## 22 Appendix F: “Converted” Facility Error Notifications

Refer to Table 22-1.

Table 22-1: Facility Error Notifications

|   Error Number | Description                                                                                                                    | Notification Group                                                               |
|----------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|            101 | Unknown Consult or Procedure request number                                                                                    | GMRC CRNR IFC ERRORS                                                             |
|            301 | Sending facility not registered at consulting facility for the requested Service                                               | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS  GMRC TIER II CRNR IFC ERRORS,  |
|            401 | Sending facility not registered at consulting facility for the requested Procedure                                             | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS   |
|            501 | Error in the Procedure name (Procedure name not found at consulting facility)                                                  | GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS    |
|            601 | Multiple services attached to a Procedure                                                                                      | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS,  GMRC TIER II CRNR IFC ERRORS  |
|            701 | Error in service name (Service name not found at consulting facility)                                                          | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS,  GMRC TIER II CRNR IFC ERRORS  |
|            702 | Service is disabled at Consulting Site                                                                                         | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS   |
|            703 | Procedure is Inactivated at Consulting Site                                                                                    | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS   |
|            801 | Consult records at the two facilities may be out of synch with regards to status                                               | GMRC CRNR IFC ERRORS,  GMRC CRNR IFC TECH ERRORS,  GMRC TIER II CRNR IFC ERRORS, |
|            802 | The activity or the consult request in question has been transmitted to the remote site multiple times and is already on file. | GMRC CRNR IFC ERRORS,  GMRC TIER II CRNR IFC ERRORS                              |