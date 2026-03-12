---
app_name: Decision Support System (DSS) Extracts
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
package_id: ECX
patch: null
patch_gap: null
section: ''
source_file: ecx_3_tm.docx
status: draft
title: '# Decision Support System 3.0'
---

# Decision Support System 3.0

# Technical Manual

<!-- image -->

November 2025


Revision History

| Date      |   Revision | Description                                                                                                                                                                                                                                                                                                                                             | Author               |
|-----------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 11/2025   |        2.5 | Updated for Patch  **ECX*3.0*196**  Updated Table 7  Field Changes in DSS for Current Release                                                                                                                                                                                                                                                           | Booz Allen Hamilton  |
| 10/2024   |        2.4 | Updated for Patch  **ECX*3.0*190**  Updated Table 1  DSS Reference Material  Updated Table 2  Management Menu Options and Activities with four (4) new report names  Updated Table 7  Field Changes in DSS for Current Release                                                                                                                          | Booz Allen Hamilton  |
| 04/2023   |        2.3 | Updated for Patch  **ECX*3.0*187**  Updated Table 1  DSS Reference Material  Updated Table 7  Field Changes in DSS for Current Release                                                                                                                                                                                                                  | Booz Allen Hamilton  |
| 12/2022   |        2.2 | Updated for Patch  **ECX*3.0*185**  Updated Table 1  DSS Reference Material  Updated Table 7  Field Changes in DSS for Current Release, reflecting no changes.                                                                                                                                                                                          | Booz Allen Hamilton  |
| 4/2022    |        2.1 | Updated for Patch  **ECX*3.0*184**  Added content to section 7.1 Integration Control Registrations  Modified Table 2 to include name of new Pre-Extract Audit Report: Event Capture Pre-Extract Missing DSS Identifier Report  Updated number of bytes per record in Table 9  Extract Name/Bytes per Record  Updated Figure 1  Data Transmission Header | Booz Allen Hamilton  |
| 5/28/2021 |        2   | Updated for Patch  **ECX*3.0*181**  Updated for Compliance with Current OIT Style Guide  Updated for Compliance with Current TM Template                                                                                                                                                                                                                | Liberty IT Solutions |
| 5/28/2020 |        1   | Initial Document                                                                                                                                                                                                                                                                                                                                        | Liberty IT Solutions |

Table of Contents

1	Introduction	1

1.1	Purpose	1

1.2	Overview	1

1.2.1	Functions of the Software	2

1.3	Document Orientation	2

1.3.1	Disclaimers	2

1.3.2	References	3

2	Implementation and Maintenance	4

2.1	System Requirements	5

2.1.1	Hardware Requirements	5

2.1.2	Software Requirements	5

2.1.3	Database Requirements	6

2.2	System Setup and Configuration	7

2.2.1	Background Job Options	7

3	Files	8

3.1	Global Placement	8

3.2	File List	8

3.3	Field List	10

3.3.1	Templates and File Flow	10

3.4	Resource Requirements	11

3.5	Special Note on IVP and UDP Extracts	12

3.6	Special Note on Pharmacy Extract Files	12

3.7	Run Time Estimates for Extracts	13

4	Routines	13

4.1	Routine List	13

4.2	XINDEX	14

5	Exported Options	14

5.1	Decision Support System Security Keys	14

5.2	Menu Outline	15

5.3	Menu Diagrams	15

6	Mail Groups, Alerts, and Bulletins	15

7	Public Interfaces	16

7.1	Integration Control Registrations	16

7.2	Application Programming Interfaces	18

7.3	Remote Procedure Calls	18

7.4	HL7 Messaging	18

7.5	Web Services	18

8	Standards and Conventions Exemptions	18

8.1	Internal Relationships	18

8.2	Software-wide Variables	18

9	Security	18

9.1	Security Menus and Options	19

9.2	Security Keys and Roles	19

9.3	File Security	19

9.4	Electronic Signatures	21

9.5	Secure Data Transmission	21

9.5.1	Remote Systems	22

10	Archiving	22

10.1	Deleting or Purging	22

10.1.1	Recommendations	23

11	Non-Standard Cross-References	23

12	Troubleshooting	23

12.1	Special Instructions for Error Correction	23

12.2	National Service Desk and Organizational Contacts	23

12.3	Generating Online Resources	23

12.3.1	Inquire to Option File	24

12.3.2	Print Options File	24

12.3.3	List File Attributes	24

Appendix A	Acronyms and Abbreviations	A-1

Appendix B	Glossary	B-1

Appendix C	Index	C-1

Table of Tables

Table 1  DSS Reference Material	3

Table 2  Management Menu Options and Activities	4

Table 3  External Package Minimum Versions Required	5

Table 4  Steps to Obtain DBIAs	6

Table 5  Required Queued Background Task	7

Table 6  DSS File List	8

Table 7  Field Change(s) in DSS for Current Release	10

Table 8  Steps to List DSS Templates and Map Menu Options	11

Table 9  Extract Name/Bytes per Record	11

Table 10  Steps to Recreate IVP and UDP Holding Files	12

Table 11  Audited fields when Updates Occur	12

Table 12  Extract Run Time Estimates	13

Table 13  Steps to List DSS Routines	13

Table 14  Extract Manager’s Options	15

Table 15  Steps to Obtain Information on Exported Menus	15

Table 16  Steps to Obtain Security Key Information	19

Table 17  VA FileMan Access Codes	19

Table 18  Recreate IVP and UDP Holding File Options	22

Table 19  Acronyms and Abbreviations	A-1

Table 20  Glossary	B-1

Table of Figures

Figure 1  Data Transmission Header	21

## 1 Introduction

The Decision Support System (DSS) is the designated Managerial Cost Accounting (MCA) System of the Department of Veterans Affairs (VA) as mandated in the Veterans Health Administration (VHA) Directive 1750 VHA Managerial Cost Accounting System (Decision Support System (DSS), March 24, 2015.

DSS is a derived database built from standard VHA data sources. The Managerial Cost Accounting Office (MCAO) uses clinical and financial data to provide state-of-the-art activity-based costing and clinical productivity analyses.

This is a design-to-schedule project with a compulsory Patch Release date of no later than November 1 of the new Fiscal Year (FY). This project enables the MCAO to accurately accommodate changes to the primary Clinical Transaction Systems made during the preceding year, ensuring the workload data has been accurately captured and costed to the Product Level.

MCA Cost Data is used at all levels of the VA for functions such as budgeting and resource allocation. Additionally, the system contains a rich repository of clinical information used to promote a proactive approach to the care of high-risk (e.g., diabetes and acute coronary patients) and high-cost patients.

### Purpose

The DSS Technical Manual serves the following purposes:

Provides technical information to aid Automated Data Processing Application Coordinators (ADPACs) and Office of Information and Technology (OIT) service staff responsible for implementing and maintaining the software.

Provides technical information to aid Database Administrator (DBA) personnel responsible for maintaining database files.

Provides security information for Information Security Officer (ISO) and Regional Information Security Officer (RISO) staff.

### Overview

The DSS Extracts Version 3.0 software provides a means of exporting data from selected Veterans Health Information Systems and Technology Architecture (VistA) software modules and transmitting it to a DSS database residing at the Austin Information Technology Center (AITC).

This transfer is accomplished through a set of extract routines, intermediate files, and transmission routines. Data from VistA packages is stored by the extract routines in the intermediate files, where it is temporarily available for local use and auditing. The data is then transmitted to the AITC, where it is formatted and uploaded into commercial software. After the data has been successfully uploaded into the commercial software, it is purged from the intermediate files.

#### Functions of the Software

The DSS Extracts software provides the following functionalities:

Implements Extracts Processes

Schedules Extracts

Verifies Extracts against other VistA Reports

Transmits Extracts to Commercial Software

Verifies Transmissions

Allows Deletion of Extracts

Allows Purging of Holding Files for the Intravenous (IV) Detail Extract (IVP), the Unit Dose Local Extract (UDP), and the VistA Blood Establishment Computer Software (VBECS) Blood Bank Extract (LBB)

### Document Orientation

The intended audience for this document is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

The namespace assigned to the DSS Extracts software is ECX.

The References section of this document lists DSS resources that can be found on the VA Software Document Library (VDL).

Package security information is located in the Security Keys sections of this manual.

User responses in the examples presented in this manual are displayed in **bold** type.

Internal document links and VDL links in this manual are displayed in blue type.

#### Disclaimers

##### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

##### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### References

Table 1 lists the manuals related to DSS that are available to view in the [VA Software Document Library (VDL) for DSS.](https://www.va.gov/vdl/application.asp?appid=35)

Table 1  DSS Reference Material

| File Name       | Manual Name                                                                                                     | Description                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ECX_3_196_DIBRG | *Decision Support System Version 3.0 Deployment, Installation, Back-out and Rollback Guide (Updated ECX*3*196)* | Provides detailed information for site IT staff for distributing, installing, backing out and rolling back DSS Extracts application software patches. |
| ECX_3_196_TM    | *Decision Support System Version 3.0 Technical Manual (Updated ECX*3*196)*                                      | Describes the DSS Extract technical (high-level) terminology.                                                                                         |
| ECX_3_196_UG    | *Decision Support System Version 3.0 User Guide (Updated ECX*3*196)*                                            | Provides guidance for users of the DSS application software.                                                                                          |
| ECX_3_196_DDD   | *Decision Support System Version 3.0 Data Definitions Document (Updated ECX*3*196)*                             | Provides technical and source information regarding each extract for users of the DSS application software.                                           |

## Notes

## 2 Implementation and Maintenance

The Management Menu enables the Extract Manager or designee to perform a variety of functions, listed in Table 2.

Refer to the DSS Deployment, Installation, Back-out, and Rollback (DIBR) Guide for more information about installing and implementing the software.

Table 2  Management Menu Options and Activities

| **Option**                | **Activity**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maintenance               | Produce the Community Based Outpatient Clinic (CBOC) Activity Report  Perform Current Procedural Terminology (CPT) and International Classification of Diseases (ICD) Inquiries  Perform DSS Ward Management Activities  Add or Modify Pharmacy IV Room Division Entries  Print the Pharmacy IV Room Worksheet  Perform Pharmacy Menu National Drug Code (NDC) Lookup  Perform Pharmacy Volume Log Maintenance Activities  Print the DRG Codes  Print the Feeder Key Listings  Print the Feeder Location Listings  Print Stations and Divisions  Produce the MAS Movement Type List  Produce the Prosthetics Reports  Maintain Prosthetics Extract Quantity Information  Produce the Treating Specialty Report  Perform DSS Clinic Setup Activities  Produce the DSS Clinic Setup Reports  Perform Inpatient Census Setup Activities  Produce the Test Patient List  View Gains and Losses (G&amp;L) Corrections Listings |
| Pre-Extract Audit Reports | Produce the Event Capture Pre-Extract Missing DSS Identifier Report  Produce the Event Capture Pre-Extract Unusual Volume Report  Produce the Laboratory Blood Bank (LBB) Pre-Extract Audit  Produce the Pharmacy Pre-Extract Incomplete Feeder Key Reports  Produce the Pharmacy Pre-Extract Unusual Cost Reports  Produce the Pharmacy Pre-Extract Unusual Volume Reports  Produce the IVP/UDP Source Audit Reports  Produce the IV Holding File Report  Produce the Prosthetic Pre-Extract Unusual Cost Report  Produce the Surgery Pre-Extract Volume Report  Produce the Surgery Pre-Extract Unusual Volume Report  Produce the Surgery Pre-Extract Observation Report                                                                                                                                                                                                                                               |
| Package Extracts          | Generate the Admissions Extract  Generate the BCMA Extract  Generate the Blood Bank Extract  Generate the Clinic Visit Extract  Generate the Event Capture Extract  Generate the IV Extract  Generate the Lab Extract  Generate the Prescription Extract  Generate the Prosthetics Extract  Generate the Radiology Extract  Generate the Surgery Extract  Generate the Transfer and Discharge Extract  Generate the Treating Specialty Change Extract  Generate the Unit Dose Extract                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SAS Extract Audit Reports | Produce the SAS Prescription Audit Report  Produce the SAS Radiology Audit Report  Produce the SAS Surgery Audit Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Extract Audit Reports     | Create Extract Audit Reports  Produce the Radiology Extract CPT Code Audit Report  Produce the Extract Stop Code Validity Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Transmission Management   | Review Extracts for Transmission  Transmit Extract Files  Produce the Summary Report of Extract Logs  Stop an Extract that is Running or Queued  Delete Extract Files  Purge Extract Holding Files  Recreate Extract Holding Files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### System Requirements

This VistA software is a Kernel Installation and Distribution System (KIDS) software release.

#### Hardware Requirements

N/A

#### Software Requirements

The DSS Extract Package relies on the following external packages based upon the minimum software versions depicted in Table 3 **.**

Table 3  External Package Minimum Versions Required

| Software Product Name              | Acronym   |   Minimum Version Required |
|------------------------------------|-----------|----------------------------|
| Admission Discharge Transfer       | ADT       |                       5.3  |
| Bar Code Medication Administration | BCMA      |                       3    |
| DSS Extracts                       | DSS       |                       3    |
| Event Capture                      | -         |                       2    |
| FileMan                            | -         |                      22.2  |
| Health Level 7                     | HL7       |                       1.6  |
| Kernel                             | -         |                       8    |
| Laboratory                         | -         |                       5.2  |
| Lab: Blood Bank                    | -         |                       5.2  |
| MailMan                            | -         |                       8    |
| Mental Health                      | -         |                       5.01 |
| Order Entry/Results Reporting      | OE/RR     |                       3    |
| Patient Care Encounter             | PCE       |                       1    |
| Pharmacy: Data Management          | PDM       |                       1    |
| Pharmacy: Inpatient Medications    | -         |                       5    |
| Pharmacy: National Drug File       | NDF       |                       4    |
| Pharmacy: Outpatient Pharmacy      | -         |                       7    |
| Prosthetics                        | -         |                       3    |
| Radiology                          | -         |                       5    |
| Registration                       | -         |                       5.3  |
| Scheduling                         | -         |                       5.3  |
| Surgery                            | -         |                       3    |

#### Database Requirements

Perform the steps in Table 4 from the FORUM Menu to obtain the DBIAs for DSS Extracts 3.0.

Table 4  Steps to Obtain DBIAs

|   **Step** | **Custodial Package**                                                                                       | **Subscriber Package**                               |
|------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
|          1 | DBA MENU                                                                                                    | DBA MENU                                             |
|          2 | INTEGRATION CONTROL REGISTRATIONS (ICR)                                                                     | INTEGRATION CONTROL REGISTRATIONS                    |
|          3 | Custodial Package Menu                                                                                      | Subscriber Package Menu                              |
|          4 | ACTIVE ICRs by Custodial Package                                                                            | Print ACTIVE by Subscribing Package                  |
|          5 | Select PACKAGE NAME:  **DSS**                                                                               | Start with subscribing package: A//  **DSS**         |
|          6 | DEVICE: HOME// &lt;  **Enter**  &gt;   SSH VIRTUAL TERMINAL &lt;  **Enter**  &gt;  Note: Secure Shell (SSH) | Go to Subscribing package: ZZZ//  **DSS**            |
|          7 | N/A                                                                                                         | DEVICE:   &lt;  **Enter**  &gt; SSH VIRTUAL TERMINAL |

### System Setup and Configuration

Decision Support System does not require site parameters *.*

#### Background Job Options

There are no routine background jobs that must run to maintain normal package operation for DSS Extracts. However, when running a DSS data extract, users must execute it as a background task (queued through TaskManager).

Both Statistical Analysis System (SAS) and Extract Audit reports can be displayed on the user’s screen, printed immediately to a print device, or queued to a print device. All other reports can only be printed as queued background jobs and cannot be stopped through the TaskMan User [XUTM USER] option.

Table 5 lists the functions that must be queued as background tasks.

Table 5  Required Queued Background Task

| Function                     | Menu Option   | Details                                                                                                                                                                                                                                                                  |
|------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transmit extract data        | [ECXTRANS]    | Transmit Data from Extract Files                                                                                                                                                                                                                                         |
| Stop extract Background Task | [XUTM USER]   | TaskMan user option.  Users can stop the Extract Background Task while it is running by using the TaskMan user [XUTM USER] option.  If queued as a background task, users can stop the background task while it is running by using the TaskMan user [XUTM USER] option. |
| Delete extract data          | [ECXDELEF]    | Delete Extract Files  Data in any resulting incomplete extract should be deleted using the Delete Extract Files [ECXDELEF] option.                                                                                                                                       |
| Purge extract holding files  | [ECXPURG]     | Purge Extract Holding Files.  Data in the holding files for the IVP, UDP and VBECS files can be purged using the Purge Extract Holding Files [ECXPURG] option.                                                                                                           |

## 3 Files

This section contains information pertaining to the files manipulated by the DSS application software.

### Global Placement

DSS Extracts use one global file for data storage: ^ECX. During first-time installation, use global protection and placement when appropriate.

### File List

The DSS Extracts software, with all patches installed, exports the files that appear in Table 6. Use the Systems Manager Menu &gt; VA FileMan &gt; Data Dictionary Utilities &gt; List File Attributes option to print the Data Dictionary (DD).

VA Directive 6402, Modifications to Standardized National Software, August 28, 2013 prohibits local modification of these files.

Table 6 lists the file names, associated file numbers, and extract abbreviations (where applicable).

Table 6  DSS File List

|   File Number | Abbreviation   | File Name                               |
|---------------|----------------|-----------------------------------------|
|       727     | -              | DSS EXTRACT LOG                         |
|       727.1   | -              | EXTRACT DEFINITIONS                     |
|       727.2   | -              | DSS LAB TESTS                           |
|       727.29  | -              | DSS LOINC FILE                          |
|       727.3   | -              | DSS DIVISION IDENTIFIER                 |
|       727.4   | -              | DSS WARD                                |
|       727.5   | -              | DSS MH TESTS                            |
|       727.7   | -              | LAB RESULTS TRANSLATION                 |
|       727.802 | ADM            | ADMISSION EXTRACT                       |
|       727.804 | -              | CLINIC NOSHOW EXTRACT                   |
|       727.805 | -              | NURSING EXTRACT                         |
|       727.806 | -              | DENTAL EXTRACT                          |
|       727.808 | MOV            | PHYSICAL MOVEMENT EXTRACT               |
|       727.809 | UDP            | UNIT DOSE LOCAL EXTRACT                 |
|       727.81  | PRE            | PRESCRIPTION EXTRACT                    |
|       727.811 | SUR            | SURGERY EXTRACT                         |
|       727.812 | -              | MENTAL HEALTH EXTRACT                   |
|       727.813 | LAB            | LABORATORY EXTRACT                      |
|       727.814 | RAD            | RADIOLOGY EXTRACT                       |
|       727.815 | ECS            | EVENT CAPTURE LOCAL EXTRACT             |
|       727.816 | -              | CLINIC I EXTRACT                        |
|       727.817 | TRT            | TREATING SPECIALTY CHANGE EXTRACT       |
|       727.818 | -              | CLINIC II EXTRACT                       |
|       727.819 | IVP            | IV DETAIL EXTRACT                       |
|       727.82  | -              | ADMISSION SETUP EXTRACT                 |
|       727.821 | -              | PHYSICAL MOVEMENT SETUP EXTRACT         |
|       727.822 | -              | TREATING SPECIALTY CHANGE SETUP EXTRACT |
|       727.823 | -              | PAI EXTRACT                             |
|       727.824 | -              | LAB RESULTS EXTRACT                     |
|       727.826 | PRO            | PROSTHETICS EXTRACT                     |
|       727.827 | CLI            | CLINIC EXTRACT                          |
|       727.829 | LBB            | BLOOD BANK EXTRACT                      |
|       727.831 | -              | DSS TREATING SPECIALTY TRANSLATION      |
|       727.832 | -              | NUTRITION EXTRACT                       |
|       727.833 | BCM            | BCMA EXTRACT                            |
|       728     | -              | DSS EXTRACTS                            |
|       728.113 | -              | IV EXTRACT DATA                         |
|       728.44  | -              | CLINICS AND STOP CODES                  |
|       728.441 | -              | NATIONAL CLINIC                         |
|       728.442 | -              | MCA LABOR CODE                          |
|       728.45  | -              | DSS NUTRITION PRODUCT WORKSHEET         |
|       728.46  | -              | DSS NUTRITION DIVISION WORKSHEET        |
|       728.506 | -              | DSS DRUG PRODUCT CODE                   |
|       728.904 | -              | UNIT DOSE EXTRACT DATA                  |
|       729     | -              | DSS PRODUCTION UNIT                     |

### Field List

The modifications associated with the release of DSS FY26 Extract Sustainment Patch ECX*3.0*196 include the following list (Table 7) of modified field names and numbers by extract.

Table 7  Field Change(s) in DSS for Current Release

| Extract File Name                 | Abbrev.   |   File Number |   VistA Field Number | Field Name              |
|-----------------------------------|-----------|---------------|----------------------|-------------------------|
| ADMISSION EXTRACT                 |           |       727.802 |                  102 | *SELF IDENTIFIED GENDER |
| PHYSICAL MOVEMENT EXTRACT         |           |       727.808 |                   41 | *SELF IDENTIFIED GENDER |
| UNIT DOSE LOCAL EXTRACT           |           |       727.809 |                   94 | *SELF IDENTIFIED GENDER |
| PRESCRIPTION EXTRACT              |           |       727.81  |                  110 | *SELF IDENTIFIED GENDER |
| SURGERY EXTRACT                   |           |       727.811 |                  141 | *SELF IDENTIFIED GENDER |
| LABORATORY EXTRACT                |           |       727.813 |                   56 | *SELF IDENTIFIED GENDER |
| RADIOLOGY EXTRACT                 |           |       727.814 |                   59 | *SELF IDENTIFIED GENDER |
| EVENT CAPTURE LOCAL EXTRACT       |           |       727.815 |                  133 | *SELF IDENTIFIED GENDER |
| TREATING SPECIALTY CHANGE EXTRACT |           |       727.817 |                   47 | *SELF IDENTIFIED GENDER |
| IV DETAIL EXTRACT                 |           |       727.819 |                   98 | *SELF IDENTIFIED GENDER |
| PROSTHETICS EXTRACT               |           |       727.826 |                  109 | *SELF IDENTIFIED GENDER |
| CLINIC EXTRACT                    |           |       727.827 |                  169 | *SELF IDENTIFIED GENDER |
| BLOOD BANK EXTRACT                |           |       727.829 |                   34 | *SELF IDENTIFIED GENDER |
| BCMA EXTRACT                      |           |       727.833 |                   93 | *SELF IDENTIFIED GENDER |

#### Templates and File Flow

Perform the steps listed in Table 8 from the Systems Manager Menu. These steps are used to obtain information about the templates and mapped file-flow relationships for DSS Extracts when all patches are installed.

Table 8  Steps to List DSS Templates and Map Menu Options

|   Step | Actions/Menu Options for Templates                                                  | Actions/Menu Options for File Flows (Relationships between Files)                                            |
|--------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|      1 | VA FileMan                                                                          | VA FileMan                                                                                                   |
|      2 | Print File Entries                                                                  | Data Dictionary Utilities                                                                                    |
|      3 | Output from what File:  **Print Template**  or  **Sort Template**                   | Map Pointer Relations                                                                                        |
|      4 | SORT BY: NAME//  **Name**                                                           | Select PACKAGE NAME:  **DSS EXTRACTS**                                                                       |
|      5 | START WITH NAME: FIRST//  **ECX**                                                   | Remove FILE: &lt;  **Enter**  &gt;                                                                           |
|      6 | GO TO NAME: LAST//  **ECXZ**                                                        | Add FILE:  &gt; Enter name or number for files to include in the output.  **Note:**  This prompt will repeat |
|      7 | WITHIN NAME, SORT BY: &lt;  **Enter**  &gt;                                         | Add FILE:&lt;  **Enter**  &gt;                                                                               |
|      8 | FIRST PRINT FIELD:  **Name**                                                        | Enter name of file group for optional graph header: DSS EXTRACTS// &lt;  **Enter**  &gt;                     |
|      9 | THEN PRINT FIELD: &lt;  **Enter**  &gt;                                             | DEVICE: &lt;  **Enter**  &gt; HOME  (CRT)  &lt;  **Enter**  &gt;                                             |
|     10 | Heading (S/C): PRINT TEMPLATE LIST// &lt;  **Enter**  &gt;                          | Not Applicable (N/A)                                                                                         |
|     11 | START AT PAGE: 1// &lt;  **Enter**  &gt;                                            | N/A                                                                                                          |
|     12 | DEVICE: &lt;  **Enter**  &gt; HOME  (CRT)  Right Margin: 80// &lt;  **Enter**  &gt; | N/A                                                                                                          |

### Resource Requirements

Table 9 provides information on extract files. The bytes per record estimates in this table include the file cross-reference.

Table 9  Extract Name/Bytes per Record

| Extract Name                            |   ## Bytes per Record  ## (Estimated Mean Size) |
|-----------------------------------------|-------------------------------------------------|
| ADM - Admission Extract                 |                                             350 |
| BCM – BCMA Extract                      |                                             450 |
| CLI - Clinic Extract                    |                                             485 |
| ECS - Event Capture Local Extract       |                                             472 |
| IVP - IV Detail Extract                 |                                             552 |
| LAB - Laboratory Extract                |                                             272 |
| LBB - Blood Bank Extract                |                                             222 |
| MOV - Physical Movement Extract         |                                             247 |
| PRE - Prescription Extract              |                                             447 |
| PRO - Prosthetics Extract               |                                             422 |
| RAD - Radiology Extract                 |                                             357 |
| SUR - Surgery Extract                   |                                             447 |
| TRT - Treating Specialty Change Extract |                                             297 |
| UDP - Unit Dose Local Extract           |                                             397 |

### Special Note on IVP and UDP Extracts

IV orders will accumulate in the IV EXTRACT DATA file (#728.113); Unit Dose orders will accumulate in the UNIT DOSE EXTRACT DATA file (#728.904). These files are loaded dynamically as Pharmacy orders for IV and unit dose medicines are processed. Each record in these files uses approximately 100 bytes.

Extreme caution must be used when performing maintenance on the IV EXTRACT DATA file (#728.113) and the UNIT DOSE EXTRACT DATA file (#728.904). If data in either file is purged, the IVP or UDP monthly extract may be incomplete. It is strongly recommended that, at a minimum, sites maintain all data from the current fiscal year.

The holding files for IVP and UDP can be purged. Two functions were created to regenerate purged IVP and UDP holding file data. The steps shown in Table 10 must be executed from the Extract Manager’s Options menu to access these options.

Holding files can become quite large if appropriate purging is not performed. The option, Purge Extract Holding Files [ECXPURG], purges holding files from IVP and UDP by date range.

Table 10  Steps to Recreate IVP and UDP Holding Files

|   Step | Action/Menu Option             |
|--------|--------------------------------|
|      1 | Extract Manager’s Options      |
|      2 | Transmission Management        |
|      3 | Recreate Extract Holding Files |

### Special Note on Pharmacy Extract Files

The Pharmacy DSS Extract files shown in Table 11 are audited when entries are edited through the menu option Pharmacy Volume Edit [ECX PHA VOL EDIT]. Entries are stored in the AUDIT file (#1.1).

Table 11  Audited fields when Updates Occur

| File                    | File #   | Audited Fields                                                              |
|-------------------------|----------|-----------------------------------------------------------------------------|
| PRESCRIPTION EXTRACT    | #727.81  | The QUANTITY and UNIT OF ISSUE fields are audited.                          |
| UNIT DOSE LOCAL EXTRACT | #727.809 | Only updates to the QUANTITY field are audited.                             |
| IV DETAIL EXTRACT       | #727.819 | Updates to the QUANTITY and TOTAL DOSES PER DAY fields are audited.         |
| BCMA EXTRACT            | #727.833 | Updates to the COMPONENT DOSE GIVEN and COMPONENT UNITS fields are audited. |

### Run Time Estimates for Extracts

Extracts generally require approximately two to four minutes per 1000 records extracted and should be queued to run during a non-peak system usage period.

Table 12 contains examples of approximate run times for extracts.

Table 12  Extract Run Time Estimates

| Extract Name                    | Approximate Length of Time   |
|---------------------------------|------------------------------|
| Admission (ADM)                 | Less than ten minutes        |
| Clinic (CLI)                    | 5 hours for 48,000 records   |
| Laboratory (LAB)                | 6 hours for 100,000 records  |
| Physical Movement (MOV)         | Less than ten minutes        |
| Prescription (PRE)              | 3.5 hours for 49,000 records |
| Treating Specialty Change (TRT) | Less than ten minutes        |

## Note:

## Note:

## 4 Routines

This section describes relevant technical aspects of DSS Application routines.

### Routine List

From the Systems Manager Menu, perform the steps outlined in Table 13 to obtain a list of routines contained in the DSS package.

Table 13  Steps to List DSS Routines

|   Step | Action/Menu Option                                                                             |
|--------|------------------------------------------------------------------------------------------------|
|      1 | Programmer Options                                                                             |
|      2 | Routine Tools                                                                                  |
|      3 | First Line Routine Print                                                                       |
|      4 | All Routines? No =&gt; &lt;  **Enter**  &gt;                                                   |
|      5 | Routine:  **ECX**  *                                                                           |
|      6 | Routine: &lt;  **Enter**  &gt;                                                                 |
|      7 | (A)lpha, (D)ate, (P)atched, OR (S)ize ORDER: A// &lt;  **Enter**  &gt;                         |
|      8 | Include line (2), Include lines 2&amp;(3), (N)one: None/ &lt;  **Enter**  &gt;                 |
|      9 | DEVICE: HOME// &lt;  **Enter**  &gt;   HOME  (CRT)    Right Margin: 80// &lt;  **Enter**  &gt; |

### XINDEX

This option analyzes the structure of a routine(s) to determine if the routine(s) adhere(s) to VistA Programming Standards. The XINDEX output includes the following components:

Compiled list of errors and warnings

Routine listing

Local variables

Global variables

Naked globals

Label references

External references

When the user executes XINDEX for a specified set of routines, deviations from VistA Programming Standards in the selected routine(s) and routine interactions (including routines called or called by other routines) are displayed.

To run XINDEX for the DSS software, specify the following namespaces at the "routine(s)? &gt;" prompt: **ECX*** .

When XINDEX runs the DSS initialization routines residing in the User Class Identifier (UCI), compiled template routines and local routines found within the ECX namespace should be omitted at the "routine(s) ?&gt;" prompt. To omit routines from selection, prefacing the namespace with a minus sign (-) is required.

## 5 Exported Options

This section provides an overview of the main menu and submenus available in the DSS application.  The user must hold the appropriate security keys in order to access all options.

### Decision Support System Security Keys

Security keys are assigned in VistA using the menu option **Key Management** , and then choosing the submenu **Allocation of Security Keys** .

**ECXMGR** : Gives a user access to the ECX Management Menu.  This key should be allocated to the DSS manager or his/her designee to perform data extraction from VistA files and transmit this data to the commercial DSS database.

**ECXPVE** : Gives a DSS user access to the ‘Pharmacy Volume Edit and Edit Log’ option.

**ECX DSS TEST** : Gives a DSS user access to the ECX FISCAL YEAR EXTRACT option.  This key should be given only to holders of the ECXMGR key whenever the site has been enrolled as an official DSS test site for the fiscal year conversion.  This key should be removed from the user(s) whenever the national released version of the DSS Fiscal Year patch is installed.

### Menu Outline

The DSS Extracts software contains one primary menu option, Extract Manager’s Options [ECXMGR], which contains options for the following six submenus. These options are fixed and are not subject to modification except by the software developers. These options are accessed by entering Extract Manager’s Options from the Systems Manager Menu; the menu options are listed in Table 14.

Table 14  Extract Manager’s Options

| Menu Option   | Description               |
|---------------|---------------------------|
| M             | Maintenance               |
| R             | Pre-Extract Audit Reports |
| P             | Package Extracts          |
| S             | SAS Extract Audit Reports |
| E             | Extract Audit Reports     |
| T             | Transmission Management   |

### Menu Diagrams

From the Systems Manager Menu, perform the steps listed in Table 15 to obtain information concerning the menus exported with the DSS Extracts software.

Table 15  Steps to Obtain Information on Exported Menus

|   Step | Action/Menu Option                                                                         |
|--------|--------------------------------------------------------------------------------------------|
|      1 | Menu Management                                                                            |
|      2 | Display Menus and Options                                                                  |
|      3 | Menu Diagrams (with Entry/Exit Actions)                                                    |
|      4 | Select USER (U.xxxxx) or OPTION (O.xxxxx) name:  **ECXMGR**                                |
|      5 | DEVICE: HOME//  &lt;  **Enter**  &gt; HOME (CRT)  Right Margin: 80// &lt;  **Enter**  &gt; |

## 6 Mail Groups, Alerts, and Bulletins

DSS Extracts utilize several mail groups. The name of each mail group is prefaced with the letters “DSS”. There is a mail group for each type of data extract (e.g., DSS-BCM, DSS-ADMS, etc.) for the purpose of receiving messages when extracts are generated and data is transmitted to the AITC. DSS also utilizes mail groups DMS, DMV and DMU for the purpose of receiving confirmation messages from the AITC. DSS Extracts do not utilize alerts.

## 7 Public Interfaces

There is no special interfacing required for the VistA DSS Extracts software.

### Integration Control Registrations

This section lists the Integration Control Registrations (ICRs) created and/or used by DSS. They are categorized by the subscriber relationship to the software. No private ICRs are documented below.

**Subscriber:**

ICR # 103

Type: File

File: #130

Root: SRF(

ICR # 218 - DBIA218-A

Type: File

File: #45.3

Root: DIC(45.3,

ICR # 322 - DBIA322

Type: File

File: #45.7

Root: DG(45.7,

ICR # 363

Type: File

File: #405.2

Root: DG(405.2,

ICR # 417

Type: File

File: #40.8

Root: DG(40.8

ICR #427

Type: File

File: #8

Root: DIC(8,

ICR # 524 - DBIA67-B

Type: File

File: #61

Root: LAB(61,

ICR # 525 - DBIA67-C

Type: File

File: #63

Root: LR(

ICR # 557

Type: File

File: #40.7

Root: DIC(40.7,

ICR # 1337

Type: File

File: #42.4

Root: DIC(42.4,

ICR # 1848 - DBIA184

Type: File

File: #42

Root: DIC(42,

ICR # 1850

Type: File

File: #2

Root: DPT(

ICR # 1860

Type: File

File: #79.1

Root: RA(79.1,

ICR # 1861

Type: File

File: #10

Root: DIC(10,

ICR # 1865

Type: File

File: #405

Root: DGPM(

ICR # 1873

Type: File

File: #721

Root: ECH(

ICR # 1874

Type: File

File: #725

Root: EC(725,

ICR # 1876 - DBIA1876

Type: File

File: #59

Root: PS(59,

ICR # 1884 - DBIA1884

Type: File

File: #59.5

Root: PS(59.5,

ICR # 1894 – DBIA1889-F

Custodial Package: PCE PATIENT CARE ENCOUNTER

Usage: Controlled Subscription

Type: Routine

Routine: PXAPI

ICR # 1910 – DBIA1910

Type: File

File: #409.68

Root: SCE(

ICR # 1949 - LAB DSS EXTRACT

Type: File

File: #64

Root: LAM(

ICR # 2233

Type: File

File: #43

Root: DG(43,

ICR # 2237

Type: File

File: #133

Root: SRO(133

ICR # 2248 – DBIA2248

Custodial Package: Registration

Usage: Controlled Subscription

Type: Routine

Routine: DGACT

ICR # 2480

Type: File

File: #70

Root: RADPT

ICR # 2533 – DBIA2533

Custodial Package: KERNEL

Usage: Controlled Subscription

Type: Routine

Routine: XUSER

ICR # 2817

Type: File

File: #40.8

Root: DG(40.8

ICR # 2849

Type: File

File: #100

Root: OR(100,

ICR # 3260 - Imaging 3260 - Lab Referral file.

Type: File

File: #67

Root: LRT(67

ICR # 3628 – SET VARIABLES FOR OPERATION REPORT

Custodial Package: SURGERY

Usage: Controlled Subscription

Type: Routine

Routine: SROVAR

ICR # 3629 – PRINT OPERATION REPORT

Custodial Package: SURGERY

Usage: Controlled Subscription

Type: Routine

Routine: SROPRPT1

ICR # 3812 – DBIA3812

Custodial Package: Registration

Usage: Controlled Subscription

Type: Routine

Routine: DGENA

ICR # 3860 – DBIA3860

Custodial Package: Registration

Usage: Controlled Subscription

Type: Routine

Routine: DGPFAPI

ICR # 3989 – DBIA398c

Custodial Package: Event Capture

Usage: Supported

Type: Routine

Routine: ECPRVMUT

ICR # 3989 – DBIA3989

Custodial Package: Enrollment Application

Usage: Controlled Subscription

Type: Routine

Routine: EASUER

ICR # 4069

Type: File

File: #772

Root: HL(772,

ICR # 4532 – NPI UTILITIES

Custodial Package: KERNEL

Usage: Controlled Subscription

Type: Routine

Routine: XUSNPI

ICR # 4652 – CLNCHK - SDUTL2 (RESTRICTING STOP CODE)

Custodial Package: PCE PATIENT CARE ENCOUNTER

Usage: Supported

Type: Routine

Routine: SDUTL2

ICR # 4658 – DBIA4658

Custodial Package: CLINICAL PROCEDURES

Usage: Supported

Type: Routine

Routine: MCARDSS

ICR # 4658 – DBIA4658

Custodial Package: Lab Service

Usage: Controlled Subscription

Type: Routine

Routine: LRRPU

ICR # 4872

Type: File

File: #136

Root: SRO(136

ICR # 5379 – DBIA5379

Custodial Package: Registration

Usage: Controlled Subscription

Type: Routine

Routine: DGENA

ICR # 6888 – NPIUSED

Custodial Package: KERNEL

Usage: Controlled Subscription

Type: Routine

Routine: XUSNPI1

### Application Programming Interfaces

N/A

### Remote Procedure Calls

N/A

### HL7 Messaging

N/A

### Web Services

N/A

## 8 Standards and Conventions Exemptions

N/A

### Internal Relationships

All the DSS Extracts options have been designed to be stand-alone options. Each option may be independently invoked.

### Software-wide Variables

The DSS Extracts software does not contain any package-wide variables that must be defined or are required for the package to run.

## 9 Security

There are no additional security management related concerns associated with the DSS application.

The DSS Extracts software does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements.

### Security Menus and Options

N/A

### Security Keys and Roles

From the Systems Manager’s Menu, perform the steps listed in Table 16 to obtain the security keys information contained in the DSS Extracts Package.

Table 16  Steps to Obtain Security Key Information

|   Step | Action/Menu Option                                           |
|--------|--------------------------------------------------------------|
|      1 | VA FileMan                                                   |
|      2 | Print File Entries                                           |
|      3 | Output from what File: Audit//  **SECURITY KEY**             |
|      4 | Sort by:  NAME// &lt;  **Enter**  &gt;                       |
|      5 | Start with NAME: FIRST//  **ECX**                            |
|      6 | Go to NAME: last//  **ECXZ**                                 |
|      7 | Within NAME, Sort by: &lt;  **Enter**  &gt;                  |
|      8 | First Print FIELD:  **NAME**                                 |
|      9 | Then Print FIELD:  **DESCRIPTION**  (word-processing)        |
|     10 | Then Print FIELD: &lt;  **Enter**  &gt;                      |
|     11 | Heading (S/C): SECURITY KEY List// &lt;  **Enter**  &gt;     |
|     12 | START at PAGE: 1// &lt;  **Enter**  &gt;                     |
|     13 | DEVICE: HOME (CRT)  Right Margin: 80// &lt;  **Enter**  &gt; |

### File Security

Table 17 lists the recommended VA FileMan access codes for the DSS Extract Software.

Table 17  VA FileMan Access Codes

<!-- rpc-table -->
| File Name                               |   File # | ## Data Definition  ## (DD)   | ## Read Access  ## (RD)   | ## Write Access  ## (WR)   | ## Delete Access  ## (DEL)   | ## Learn-As- You-Go  ## (LAYGO)  ## 10 Archiving  DSS Extracts have no archiving capability. There is an option to delete the local extract files after transmission to the commercial software. See section 10.1.  ### 10.1 Deleting or Purging  DSS Extracts export the Delete Extract Files [ECXDELEF] option which can be used to delete individual extracts residing in files #727.802 through #727.833, or a range of extracts.  Data that resides in the holding files for VBECS (VBECS DSS EXTRACT file (#6002.03)), IVP (IV EXTRACT DATA file (#728.113)), and UDP (UNIT DOSE EXTRACT DATA file (#728.904)) extracts can be purged using the Purge Extract Holding Files [ECXPURG].  Extreme caution should be exercised when purging or deleting data for the following reasons:  Any existing extract may be deleted (including transmitted and un-transmitted), as well as extracts that did not run to completion due to errors or system problems.  Choosing a range of extracts or holding files sometimes results in an excessively large number of records to be deleted or purged, and may be very resource intensive. These tasks should be scheduled for non-peak hours, and the number of deleted or holding files purged should be limited to a single queued session.  Extreme caution must be used when performing maintenance to the IV EXTRACT DATA file (#728.113) and the UNIT DOSE EXTRACT DATA file (#728.904). If data in either file is purged, the IVP or UDP monthly extract may be incomplete. It is strongly recommended that, at a minimum, sites maintain all data from the *current fiscal year* .  A user can only delete extracts that are associated with the division assigned in their NEW PERSON file (#200).  Two functions were created to regenerate IVP and UDP holding file data that has been purged. These functions are located at:  Extract Manager Options &gt; Transmission Management &gt; Recreate Extract Holding Files  The functions are listed in Table 18.  Table 18  Recreate IVP and UDP Holding File Options  Option Description I Recreate IVP Extract Holding File (#728.113) U Recreate UDP Extract Holding File (#728.904)  #### 10.1.1 Recommendations  Purging of any local VistA extract data or VistA source of extract data (i.e., lab data, etc.) is not recommended until a facility has successfully created extracts, transmitted them to the AITC, audited the counts, loaded the data into DSS, and the validation results are successful.  The IV EXTRACT DATA file (#728.113) and UNIT DOSE EXTRACT DATA file (#728.904) can become quite large if appropriate purging is not performed. The file purge option, Purge Extract Holding Files [ECXPURG], removes the data from these files by date range. It is recommended that records over two fiscal years old should be purged from the IV EXTRACT DATA file (#728.113) and the UNIT DOSE EXTRACT DATA file (#728.904).  VBECS holding files can also be purged. The VBECS holding file cannot be regenerated; therefore, extreme care must be used when purging these files.  ## 11 Non-Standard Cross-References  N/A  ## 12 Troubleshooting  Technical users of the DSS software should ensure that a local contingency plan is used in the event of application problems in a live environment. The plan should identify the procedure(s) for maintaining the functionality provided by the DSS Extracts software in the event of a system outage. Field Station ISOs can get assistance from the Regional ISO.  ### 12.1 Special Instructions for Error Correction  Specific error correction guidance is provided in the ECX*3.0*196 DIBRG, which can be found in the VA Software Document Library (VDL).  ### 12.2 National Service Desk and Organizational Contacts  The Enterprise Service Desk (ESD) Provides critical IT support to Veterans Affairs.  Contact information can be found online at the VA YourIT service portal.  ### 12.3 Generating Online Resources  This section describes some of the various methods for users to access DSS Technical documentation. Online DSS technical documentation pertaining to the DSS software, in addition to that which is located in the Help prompts and Online Help screens, are imbedded throughout the DSS package and can be accessed through utilization of several KERNEL options. These include, but are not limited to, *XINDEX, Menu Management Inquire Option File, Print Option File,* and *FileMan List File Attributes* .  Entering question marks at the "Select ... Option:" prompt provides users with valuable technical information. For example:  A single question mark (?) lists all options accessible from the current option.  Entering two question marks (??) lists all options accessible from the current option displaying the formal name and lock for each.  Three question marks (???) displays a brief description for each option in a menu.  An option name preceded by a single question mark (?) displays extended Help, if available, for that option.  To obtain a listing of the available options and additional information about other utilities for online technical information, refer to the [VA Software Document Library](https://www.va.gov/vdl/) (VDL) for Kernel documentation.  #### 12.3.1 Inquire to Option File  To access information about DSS options, the user must specify the name or namespace of the desired option(s). The Menu Manager option provides the following information about user-specified option(s):  Option name  Menu text  Option description  Type of option  Lock (if any)  #### 12.3.2 Print Options File  Use this utility to generate a listing of options from the OPTION file (#19). Users can choose to print all of the entries in this file specifying a single option or a range of options. To obtain a list of DSS options, enter “ECX” when prompted for the namespace.  #### 12.3.3 List File Attributes  Use the “List Attributes” option in FileMan to generate documentation pertaining to files and file structures. Use the Standard format option to obtain the following data dictionary information for a specified file(s):  File name and description  Identifiers  Cross-references  Files pointed to by the file specified  Files which point to the file specified  Input, print, and sort templates  In addition, the following information is supplied for each field in the selected file:  Field name and number  Global location  Description  Help prompt  Cross-reference(s)  Input transform  Date last edited  Notes  Use the Global Map format option to generate an output listing of the following:  All cross-references for the selected file  Global location of each field in the file  Input, print, and sort templates  ####### 1 Acronyms and Abbreviations  Abbreviations and acronyms used throughout the DSS Technical Manual appear in Table 19.  Table 19  Acronyms and Abbreviations  Acronym Description ADM Admission Extract ADPAC Automated Data Processing Application Coordinator ADT Admission Discharge Transfer AITC Austin Information Technology Center API Application Programmer Interface BCM BCMA Extract BCMA Bar Code Medication Administration CBOC Community Based Outpatient Clinic CLI Clinic Extract CPRS Computerized Patient Record System CPT Current Procedural Terminology CRT Cathode Ray Tube DBA Database Administrator DBIA Database Integration Agreement DD Data Dictionary DSS Decision Support System ECS Event Capture Local Extract ECX DSS Extracts Namespace HL7 Health Level 7 ICD International Classification of Diseases ICR Integration Control Registration IEN Internal Entry Number ISO Information Security Officer IV Intravenous IVP IV Detail Extract LAB Laboratory Extract LAYGO Learn-As-You-Go LBB Blood Bank Extract LOINC Logical Observation Identifiers, Names, and Codes MCAO Managerial Cost Accounting Office MOV Physical Movement Extract N/A Not Applicable NDC National Drug Code NDF National Drug File OE/RR Order Entry/Results Reporting OIT Office of Information and Technology PCE Patient Care Encounter PDM Pharmacy Data Management PRE Prescription Extract PRO Prosthetics Extract RAD Radiology Extract RD Read Access RISO Regional Information Security Officer SAS Statistical Analysis System SSH Secure Shell SUR Surgery Extract TRT Treating Specialty Change Extract UCI User Class Identifier UDP Unit Dose Local Extract VA Department of Veterans Affairs VBECS VistA Blood Establishment Computer Software VDL VA Software Document Library VHA Veterans Health Administration VistA Veterans Health Information Systems and Technology Architecture  ####### 2 Glossary  Table 20 lists terms used throughout the Technical Manual.  Table 20  Glossary  Term Definition FileMan This system implements the VistA database engine and is the basis for several patient safety controls, as well as fiscal integrity controls. It implements security, confidentiality, and privacy controls, and is a critical component in meeting the requirements of Enterprise Architecture. Kernel This system implements security, confidentiality, and privacy controls for VistA, including user authentication algorithms. It provides many tools for the safe construction of local software, and it implements many national control files, including, but not limited to, New Person, Institution, State, etc. This system is a critical component in meeting the requirements of Enterprise Architecture. Remote Procedure Call (RPC) This system supports client and/or server messaging used by CPRS, Bar Code Medication Administration (BCMA), and others, to access the MUMPS database through APIs. It provides a development kit for local development, and it implements security, confidentiality, and privacy controls. This system is a critical component in meeting the requirements of Enterprise Architecture.  ####### 3 Index  ADPAC	1  AITC	1, 15, 21  Alerts	15  Archiving	22  Background Job Options	7  Contingency Plan	23  Data Transmission	21  Database Requirements	6  DBA	1, 6  DBIA	6  Deleting	22  Disclaimers	2  ECX Namespace	14  Extract Manager Options	15  Field List	10  File List	8  FileMan	10  Functions	2, 4, 7, 12, 22  Global Map	24  Global Placement	8  Help	23  Inquire to Option File	24  Introduction	1  ISO	23  IVP and UDP Extracts	12  Kernel	5, 23  KIDS	5  List File Attributes	24  Mail Groups	15  MailMan	21  Maintenance	12, 22  Management Menu	4  MCA	1  MCAO	1  Menu Diagrams	15  Menu Manager	24  Menu Outline	15  Namespace	2, 24  National Service Desk	23  Online Help Screens	23  Orientation	2  Overview	1  Pharmacy Extract Files	12  Print Options File	24  Purging	22  Purpose	1  References	3  Resource Requirements	11  Routines	13  Run Time Estimates	13  SAS	7, 21  Security	18  Security Keys	19  Software Requirements	5  System Requirements	5  Systems Manager Menu	10  TaskMan	7  TaskManager	7  Templates and File Flow	10  Troubleshooting	23  UCI	14  User Class Identifier	14  VA Software Document Library	3  VA Software Documentation Library	23  VBECS	2, 7, 22  VistA	1, 2, 5, 13, 14, 15, 22, B-1  Web Services	18  XINDEX	13, 14, 23     |
|-----------------------------------------|----------|-------------------------------|---------------------------|----------------------------|------------------------------|-----|
| DSS EXTRACT LOG                         |  727     | @                             | N/A                       | @                          | @                            | @   |
| EXTRACT DEFINITIONS                     |  727.1   | ^                             | N/A                       | ^                          | ^                            | ^   |
| DSS LOINC FILE                          |  727.29  | ^                             | N/A                       | ^                          | ^                            | ^   |
| DSS DIVISION IDENTIFIER                 |  727.3   | ^                             | N/A                       | ^                          | ^                            | ^   |
| DSS WARD                                |  727.4   | ^                             | N/A                       | ^                          | ^                            | ^   |
| DSS MH TESTS                            |  727.5   | ^                             | N/A                       | ^                          | ^                            | ^   |
| LAB RESULTS TRANSLATION                 |  727.7   | @                             | N/A                       | N/A                        | N/A                          | N/A |
| ADMISSION EXTRACT                       |  727.802 | @                             | @                         | @                          | @                            | @   |
| CLINIC NOSHOW EXTRACT                   |  727.804 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| NURSING EXTRACT                         |  727.805 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| DENTAL EXTRACT                          |  727.806 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| PHYSICAL MOVEMENT EXTRACT               |  727.808 | @                             | @                         | @                          | @                            | @   |
| UNIT DOSE LOCAL EXTRACT                 |  727.809 | @                             | @                         | @                          | @                            | @   |
| PRESCRIPTION EXTRACT                    |  727.81  | @                             | @                         | @                          | @                            | @   |
| SURGERY EXTRACT                         |  727.811 | @                             | @                         | @                          | @                            | @   |
| LABORATORY EXTRACT                      |  727.813 | @                             | @                         | @                          | @                            | @   |
| RADIOLOGY EXTRACT                       |  727.814 | @                             | @                         | @                          | @                            | @   |
| EVENT CAPTURE LOCAL EXTRACT             |  727.815 | @                             | @                         | @                          | @                            | @   |
| CLINIC I EXTRACT                        |  727.816 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| TREATING SPECIALTY CHANGE EXTRACT       |  727.817 | @                             | @                         | @                          | @                            | @   |
| CLINIC II EXTRACT                       |  727.818 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| IV DETAIL EXTRACT                       |  727.819 | @                             | @                         | @                          | @                            | @   |
| ADMISSION SETUP EXTRACT                 |  727.82  | @                             | @                         | @                          | @                            | @   |
| PHYSICAL MOVEMENT SETUP EXTRACT         |  727.821 | @                             | @                         | @                          | @                            | @   |
| TREATING SPECIALTY CHANGE SETUP EXTRACT |  727.822 | @                             | @                         | @                          | @                            | @   |
| PAI EXTRACT                             |  727.823 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| LAB RESULTS EXTRACT                     |  727.824 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| PROSTHETICS EXTRACT                     |  727.826 | @                             | @                         | @                          | @                            | @   |
| CLINIC EXTRACT                          |  727.827 | @                             | @                         | @                          | @                            | @   |
| BLOOD BANK EXTRACT                      |  727.829 | @                             | @                         | @                          | @                            | @   |
| DSS TREATING SPECIALTY TRANSLATION      |  727.831 | @                             | @                         | @                          | @                            | @   |
| BCMA EXTRACT                            |  727.833 | @                             | @                         | @                          | @                            | @   |
| DSS EXTRACTS                            |  728     | @                             | N/A                       | @                          | @                            | @   |
| IV EXTRACT DATA                         |  728.113 | @                             | @                         | @                          | @                            | @   |
| CLINICS AND STOP CODES                  |  728.44  | @                             | N/A                       | @                          | @                            | @   |
| NATIONAL CLINIC                         |  728.441 | @                             | N/A                       | @                          | @                            | @   |
| DSS DRUG PRODUCT CODE                   |  728.506 | N/A                           | N/A                       | N/A                        | N/A                          | N/A |
| UNIT DOSE EXTRACT DATA                  |  728.904 | @                             | @                         | @                          | @                            | @   |
| DSS PRODUCTION UNIT                     |  729     | ^                             | N/A                       | ^                          | ^                            | ^   |

### Electronic Signatures

The DSS Extracts software does not use electronic signatures.

### Secure Data Transmission

Data is transmitted to the AITC using VA MailMan mail messages. The first line of each message is a header that identifies the following entities: Site, Extract, Year and Month, SAS version identifier, and Fiscal Year Logic in the format shown in Figure 1.

Figure 1  Data Transmission Header

<!-- image -->

#### Remote Systems

DSS Extracts transmit messages containing extracted data to a specified queue located at the AITC. Data is transmitted via VA MailMan at the site’s discretion. Confirmation messages are received from the AITC indicating the extract messages were successfully transmitted.